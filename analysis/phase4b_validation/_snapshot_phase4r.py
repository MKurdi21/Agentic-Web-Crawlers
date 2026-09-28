"""Capture all original Phase 4R file bytes for final preservation comparison."""
import csv
import hashlib
from pathlib import Path

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent / "phase4r_remediation"
DEST = OUT / "PHASE4R_FILE_HASHES_INITIAL.csv"
assert not DEST.exists()


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


with DEST.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["relative_path", "size_bytes", "sha256"])
    for path in sorted(SOURCE.rglob("*")):
        if path.is_file():
            writer.writerow([path.relative_to(SOURCE).as_posix(), path.stat().st_size, sha(path)])
print(sum(1 for _ in DEST.open(encoding="utf-8")) - 1)
