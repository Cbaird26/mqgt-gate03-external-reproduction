#!/usr/bin/env python3
"""Build SHA-256 manifest for the GATE-03 packet."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_PARTS = {
    ".DS_Store",
    ".git",
    ".pytest_cache",
    "__pycache__",
    "tmp",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDE_PARTS for part in rel.parts):
        return False
    if rel.name == "PACKET_MANIFEST.json":
        return False
    return path.is_file()


def main() -> None:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not include(path):
            continue
        rel = path.relative_to(ROOT)
        files.append({
            "path": str(rel),
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
        })
    manifest = {
        "packet": "GATE03_external_reproduction_packet_v0_1",
        "status": "historical_not_operator_ready",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(files),
        "files": files,
        "boundary": (
            "Historical v0.1 only; no endpoint swap on old bits; no v0.2 "
            "packet before Objects 1-5 are apparatus-sourced; no final ToE "
            "closure promotion."
        ),
    }
    (ROOT / "PACKET_MANIFEST.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps({"file_count": len(files), "manifest": str(ROOT / "PACKET_MANIFEST.json")}, indent=2))


if __name__ == "__main__":
    main()
