"""Independent, read-only preservation and frozen-methodology check."""
import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


changed, missing = [], []
with (OUT / "PROTECTED_FILE_HASHES_INITIAL.csv").open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))
for row in rows:
    path = ROOT / row["path"]
    if not path.is_file():
        missing.append(row["path"])
    elif sha(path) != row["sha256"]:
        changed.append(row["path"])

config = json.loads((OUT / "REMEDIATED_WORKFLOW_CONFIGURATION.json").read_text(encoding="utf-8"))
mismatches = []
for component, data in config["components"].items():
    if "files" not in data:
        continue
    for entry in data["files"]:
        path = OUT / "candidate_v4r" / entry["path"]
        if not path.is_file() or sha(path) != entry["sha256"]:
            mismatches.append(f"{component}:{entry['path']}")

receipt = json.loads((OUT / "PHASE4B_HOLDOUT_SELECTION_RECEIPT.json").read_text(encoding="utf-8"))
contamination = json.loads((OUT / "PHASE4B_HOLDOUT_CONTAMINATION_LOG.json").read_text(encoding="utf-8"))
holdout_ok = (
    receipt["holdout_sha256"] == sha(OUT / "PHASE4B_VALIDATION_HOLDOUT.csv")
    and receipt["methodology_fingerprint"] == config["configuration_sha256"]
    and receipt["report_count"] == 8
    and not contamination["events"]
    and contamination["holdout_sha256"] == receipt["holdout_sha256"]
)

status = subprocess.run(["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
(OUT / "GIT_STATUS_FINAL.txt").write_bytes(status)
initial = set((OUT / "GIT_STATUS_INITIAL.txt").read_text(encoding="utf-8").splitlines())
final = set(status.decode("utf-8").splitlines())
added = sorted(final - initial)
removed = sorted(initial - final)
outside_added = [line for line in added if not line[3:].replace('"', '').replace('\\', '/').startswith("analysis/phase4r_remediation/") and line[3:].replace('"', '').replace('\\', '/') != "analysis/phase4r_remediation_package.zip"]

result = {
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "protected_file_count": len(rows),
    "changed_count": len(changed),
    "missing_count": len(missing),
    "changed_paths": changed,
    "missing_paths": missing,
    "frozen_component_mismatch_count": len(mismatches),
    "frozen_component_mismatches": mismatches,
    "holdout_csv_sha256": receipt["holdout_sha256"],
    "holdout_frozen_and_uncontaminated": holdout_ok,
    "phase4_original_status_unchanged": not any(p.startswith("analysis/phase4_rehearsal/") for p in changed),
    "phase4_lane_b_runtime_exists": (ROOT / "analysis/phase4_rehearsal/rehearsal_runtime").exists(),
    "phase4r_migration_rehearsal_runtime_exists": (OUT / "rehearsal_runtime").exists(),
    "live_source_verified_inherited_unchanged": 0,
    "live_promoted_inherited_unchanged": 0,
    "no_live_mutation_evidence": not changed and not missing and not outside_added and not removed,
    "git_status_initial_sha256": sha(OUT / "GIT_STATUS_INITIAL.txt"),
    "git_status_final_sha256": sha(OUT / "GIT_STATUS_FINAL.txt"),
    "git_status_new_outside_boundary": outside_added,
    "git_status_removed_from_initial": removed,
}
(OUT / "PRESERVATION_CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ["protected_file_count", "changed_count", "missing_count", "frozen_component_mismatch_count", "holdout_frozen_and_uncontaminated", "no_live_mutation_evidence"]}))
