"""Independently compare protected Phase 4B inputs with the captured baseline."""
import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


missing = []
changed = []
size_changed = []
protected = rows(OUT / "PROTECTED_FILE_HASHES_INITIAL.csv")
for row in protected:
    path = ROOT / row["path"]
    if not path.is_file():
        missing.append(row["path"])
        continue
    if digest(path) != row["sha256"]:
        changed.append(row["path"])
    if path.stat().st_size != int(row["size"]):
        size_changed.append(row["path"])

p4r = ROOT / "analysis/phase4r_remediation"
p4r_changed = []
for row in rows(OUT / "PHASE4R_FILE_HASHES_INITIAL.csv"):
    path = p4r / row["relative_path"]
    if not path.is_file() or digest(path) != row["sha256"]:
        p4r_changed.append(row["relative_path"])

initial_git = (OUT / "GIT_STATUS_INITIAL.txt").read_text(encoding="utf-8-sig").splitlines()
current_git_raw = subprocess.run(["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, check=True, capture_output=True).stdout
(OUT / "GIT_STATUS_FINAL.txt").write_bytes(current_git_raw)
current_git = current_git_raw.decode("utf-8-sig").splitlines()


def outside(rows):
    return sorted(row for row in rows if "analysis/phase4b_validation/" not in row and "analysis/phase4b_validation_package.zip" not in row)


git_diff = sorted(set(outside(initial_git)) ^ set(outside(current_git)))
review = json.loads((ROOT / "analysis/reviews.json").read_text(encoding="utf-8"))
rehearsal_absent = not (OUT / "rehearsal_runtime").exists() and not (OUT / "candidate_v4r/shadow").exists()
source_private_count = len(list((OUT / "private_source_material").rglob("*.pdf")))
result = {
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "protected_file_count": len(protected),
    "protected_missing": missing,
    "protected_hash_changes": changed,
    "protected_size_changes": size_changed,
    "phase4r_file_count": len(rows(OUT / "PHASE4R_FILE_HASHES_INITIAL.csv")),
    "phase4r_changes": p4r_changed,
    "git_status_changes_outside_phase4b": git_diff,
    "live_source_verified": 0 if review == {} else "UNKNOWN",
    "live_promoted": 0 if review == {} else "UNKNOWN",
    "phase4b_private_pdf_count": source_private_count,
    "lane_b_runtime_absent": rehearsal_absent,
    "passed": not (missing or changed or size_changed or p4r_changed or git_diff) and review == {} and rehearsal_absent and source_private_count == 1,
}
(OUT / "PRESERVATION_CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("passed", "protected_file_count", "phase4r_file_count", "live_source_verified", "live_promoted", "phase4b_private_pdf_count", "lane_b_runtime_absent")}))
if not result["passed"]:
    print(json.dumps({k: result[k] for k in ("protected_missing", "protected_hash_changes", "phase4r_changes", "git_status_changes_outside_phase4b")}))
    raise SystemExit(1)
