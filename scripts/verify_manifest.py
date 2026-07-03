#!/usr/bin/env python3
"""Verify current files against PACKET_MANIFEST.json."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKET_MANIFEST.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    failures: list[str] = []
    for item in manifest["files"]:
        path = ROOT / item["path"]
        if not path.exists():
            failures.append(f"missing: {item['path']}")
            continue
        actual = sha256(path)
        if actual != item["sha256"]:
            failures.append(f"hash mismatch: {item['path']}")
    if failures:
        print(json.dumps({"status": "failed", "failures": failures}, indent=2))
        raise SystemExit(1)
    print(json.dumps({
        "status": "ok",
        "file_count": len(manifest["files"]),
        "boundary": manifest.get("boundary"),
    }, indent=2))


if __name__ == "__main__":
    sys.exit(main())
