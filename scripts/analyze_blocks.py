#!/usr/bin/env python3
"""Standalone GATE-03 block-level analyzer."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def block_p1(block: dict[str, Any]) -> tuple[float, str]:
    n = int(block.get("bit_count", block.get("n_bits", 0)))
    if n <= 0:
        raise ValueError(f"Invalid bit_count in block {block.get('block_index')}")
    if "ones" in block:
        return int(block["ones"]) / n, "ones_over_bit_count"
    if "p_hat" in block:
        return float(block["p_hat"]), "p_hat"
    raise ValueError(f"Block {block.get('block_index')} lacks ones or p_hat")


def permutation_p(control: list[float], intervention: list[float], n_perm: int, seed: int = 42) -> float:
    if not control or not intervention:
        return math.nan
    obs = mean(intervention) - mean(control)
    combined = control + intervention
    rng = random.Random(seed)
    count = 0
    n_control = len(control)
    for _ in range(n_perm):
        shuffled = combined[:]
        rng.shuffle(shuffled)
        c = shuffled[:n_control]
        i = shuffled[n_control:]
        if abs(mean(i) - mean(c)) >= abs(obs):
            count += 1
    return (count + 1) / (n_perm + 1)


def analyze_run(path: Path, n_perm: int) -> dict[str, Any]:
    data = json.loads(path.read_text())
    blocks = data.get("blocks")
    if not isinstance(blocks, list):
        raise ValueError(f"{path} has no blocks list")

    control: list[float] = []
    intervention: list[float] = []
    methods: set[str] = set()
    bit_counts: list[int] = []

    for block in blocks:
        condition = block.get("condition")
        p1, method = block_p1(block)
        methods.add(method)
        bit_counts.append(int(block.get("bit_count", block.get("n_bits", 0))))
        if condition == "control":
            control.append(p1)
        elif condition == "intervention":
            intervention.append(p1)
        else:
            raise ValueError(f"{path} block {block.get('block_index')} has invalid condition {condition!r}")

    c_mean = mean(control)
    i_mean = mean(intervention)
    diff = i_mean - c_mean
    formal = (
        len(blocks) == 20
        and len(control) == 10
        and len(intervention) == 10
        and all(n >= 100_000 for n in bit_counts)
    )

    return {
        "path": str(path),
        "sha256": sha256(path),
        "run_id": data.get("run_id", path.stem.removesuffix("_blocks")),
        "operator_id": data.get("operator_id", ""),
        "device_id_hash": data.get("device_id_hash", ""),
        "intervention": data.get("intervention", ""),
        "direction": data.get("direction", "two-sided"),
        "block_count": len(blocks),
        "control_blocks": len(control),
        "intervention_blocks": len(intervention),
        "total_bits": sum(bit_counts),
        "min_block_bits": min(bit_counts) if bit_counts else 0,
        "control_mean_p1": c_mean,
        "intervention_mean_p1": i_mean,
        "difference_i_minus_c": diff,
        "permutation_p": permutation_p(control, intervention, n_perm),
        "formal_run": formal,
        "p1_source_methods": sorted(methods),
    }


def pooled_report(runs: list[dict[str, Any]], n_perm: int) -> dict[str, Any]:
    control: list[float] = []
    intervention: list[float] = []
    for run in runs:
        data = json.loads(Path(run["path"]).read_text())
        for block in data["blocks"]:
            p1, _ = block_p1(block)
            if block["condition"] == "control":
                control.append(p1)
            elif block["condition"] == "intervention":
                intervention.append(p1)
    return {
        "control_blocks": len(control),
        "intervention_blocks": len(intervention),
        "control_mean_p1": mean(control),
        "intervention_mean_p1": mean(intervention),
        "difference_i_minus_c": mean(intervention) - mean(control),
        "permutation_p": permutation_p(control, intervention, n_perm),
    }


def same_nonzero_direction(diffs: list[float]) -> bool:
    nonzero = [d for d in diffs if d != 0]
    if len(nonzero) != len(diffs) or not nonzero:
        return False
    return all(d > 0 for d in nonzero) or all(d < 0 for d in nonzero)


def decide(formal_runs: list[dict[str, Any]], pooled: dict[str, Any], alpha: float, min_runs: int) -> dict[str, Any]:
    reasons: list[str] = []
    if len(formal_runs) < min_runs:
        reasons.append(f"formal_run_count_below_{min_runs}")
    if formal_runs and not same_nonzero_direction([r["difference_i_minus_c"] for r in formal_runs]):
        reasons.append("formal_runs_not_same_nonzero_direction")
    if math.isnan(pooled.get("permutation_p", math.nan)) or pooled["permutation_p"] >= alpha:
        reasons.append("pooled_permutation_p_not_below_alpha")
    if reasons:
        return {
            "status": "not_promotable",
            "reasons": reasons,
            "gate03_effect": "no_gate_promotion",
        }
    return {
        "status": "candidate_support_requires_attestation",
        "reasons": ["formal_statistical_criteria_met_but_external_attestation_required"],
        "gate03_effect": "candidate_only_not_final_closure",
    }


def markdown(report: dict[str, Any]) -> str:
    pooled = report["formal_pooled"]
    lines = [
        "# GATE-03 Block Analysis Report",
        "",
        f"Generated UTC: `{report['generated_utc']}`",
        f"Decision: `{report['decision']['status']}`",
        "",
        "## Formal Pooled Result",
        "",
        f"- Formal runs: {report['formal_run_count']}",
        f"- Control blocks: {pooled.get('control_blocks', 0)}",
        f"- Intervention blocks: {pooled.get('intervention_blocks', 0)}",
        f"- Difference I-C: {pooled.get('difference_i_minus_c', math.nan):+.9f}",
        f"- Permutation p: {pooled.get('permutation_p', math.nan):.6f}",
        f"- Alpha: {report['alpha']}",
        "",
        "## Decision Reasons",
        "",
    ]
    lines.extend(f"- `{reason}`" for reason in report["decision"]["reasons"])
    lines.extend([
        "",
        "## Per Run",
        "",
    ])
    for run in report["runs"]:
        lines.append(
            f"- `{run['run_id']}` formal={run['formal_run']} diff={run['difference_i_minus_c']:+.9f} p={run['permutation_p']:.6f} sha256={run['sha256']}"
        )
    lines.extend([
        "",
        "## Boundary",
        "",
        "This report can affect only GATE-03. It cannot promote final Theory-of-Everything closure.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("block_json", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--md-out", type=Path)
    parser.add_argument("--alpha", type=float, default=0.01)
    parser.add_argument("--min-formal-runs", type=int, default=3)
    parser.add_argument("--permutations", type=int, default=10_000)
    args = parser.parse_args()

    runs = [analyze_run(path, args.permutations) for path in args.block_json]
    formal_runs = [run for run in runs if run["formal_run"]]
    formal_pooled = pooled_report(formal_runs, args.permutations) if formal_runs else {}
    all_pooled = pooled_report(runs, args.permutations)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "analyzer": "GATE03_external_reproduction_packet_v0_1/scripts/analyze_blocks.py",
        "alpha": args.alpha,
        "min_formal_runs": args.min_formal_runs,
        "permutations": args.permutations,
        "input_count": len(runs),
        "formal_run_count": len(formal_runs),
        "runs": runs,
        "formal_pooled": formal_pooled,
        "all_pooled": all_pooled,
        "decision": decide(formal_runs, formal_pooled, args.alpha, args.min_formal_runs),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2))
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(markdown(report))
    print(json.dumps({
        "decision": report["decision"]["status"],
        "formal_run_count": report["formal_run_count"],
        "formal_pooled_p": formal_pooled.get("permutation_p"),
        "formal_diff": formal_pooled.get("difference_i_minus_c"),
    }, indent=2))


if __name__ == "__main__":
    main()
