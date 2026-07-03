#!/usr/bin/env python3
"""Generate deterministic synthetic block JSON files for analyzer smoke tests."""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path


def make_run(run_index: int, out: Path, effect: float, seed: int, block_bits: int = 100_000) -> Path:
    rng = random.Random(seed + run_index)
    conditions = ["control"] * 10 + ["intervention"] * 10
    rng.shuffle(conditions)
    start = datetime(2026, 7, 3, 0, 0, tzinfo=timezone.utc) + timedelta(hours=run_index)
    blocks = []
    for idx, condition in enumerate(conditions):
        base = 0.5 + rng.gauss(0, 0.00155)
        p = base + (effect if condition == "intervention" else 0.0)
        p = max(0.0, min(1.0, p))
        ones = round(block_bits * p)
        blocks.append({
            "block_index": idx,
            "condition": condition,
            "bit_count": block_bits,
            "ones": ones,
            "p_hat": ones / block_bits,
            "start_time": (start + timedelta(minutes=idx)).isoformat(),
            "end_time": (start + timedelta(minutes=idx + 1)).isoformat(),
        })
    data = {
        "run_id": f"synthetic_formal_{run_index:03d}",
        "operator_id": "synthetic-smoke-test",
        "device_id_hash": "synthetic-not-a-device",
        "intervention": "meditation",
        "randomization_seed": seed + run_index,
        "direction": "two-sided",
        "blocks": blocks,
    }
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"synthetic_formal_{run_index:03d}.json"
    path.write_text(json.dumps(data, indent=2))
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--effect", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=20260703)
    args = parser.parse_args()
    paths = [make_run(i + 1, args.out, args.effect, args.seed) for i in range(args.runs)]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
