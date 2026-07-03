#!/usr/bin/env python3
"""Run deterministic GATE-03 smoke tests."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / "tmp" / "smoke"
RESULTS = TMP / "results"


def run(args: list[str]) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def load_status(path: Path) -> str:
    return json.loads(path.read_text())["decision"]["status"]


def main() -> None:
    if TMP.exists():
        shutil.rmtree(TMP)
    null_dir = TMP / "synthetic_formal_null"
    positive_dir = TMP / "synthetic_formal_positive"
    RESULTS.mkdir(parents=True, exist_ok=True)

    run([sys.executable, "scripts/make_synthetic_blocks.py", "--out", str(null_dir)])
    run([
        sys.executable,
        "scripts/analyze_blocks.py",
        *[str(path) for path in sorted(null_dir.glob("*.json"))],
        "--out",
        str(RESULTS / "ci_synthetic_null_report.json"),
        "--md-out",
        str(RESULTS / "ci_synthetic_null_report.md"),
    ])

    run([
        sys.executable,
        "scripts/make_synthetic_blocks.py",
        "--out",
        str(positive_dir),
        "--effect",
        "0.006",
    ])
    run([
        sys.executable,
        "scripts/analyze_blocks.py",
        *[str(path) for path in sorted(positive_dir.glob("*.json"))],
        "--out",
        str(RESULTS / "ci_synthetic_positive_report.json"),
        "--md-out",
        str(RESULTS / "ci_synthetic_positive_report.md"),
    ])

    null_status = load_status(RESULTS / "ci_synthetic_null_report.json")
    positive_status = load_status(RESULTS / "ci_synthetic_positive_report.json")
    if null_status != "not_promotable":
        raise SystemExit(f"Unexpected null status: {null_status}")
    if positive_status != "candidate_support_requires_attestation":
        raise SystemExit(f"Unexpected positive status: {positive_status}")

    print(json.dumps({
        "null_status": null_status,
        "positive_status": positive_status,
        "manifest": "unchanged",
    }, indent=2))


if __name__ == "__main__":
    main()
