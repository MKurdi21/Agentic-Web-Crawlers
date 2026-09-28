"""Phase 4B preflight: read-only inputs; writes diagnostics only in Phase 4B."""
import csv
import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
P4R = ROOT / "analysis/phase4r_remediation"


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


archive_expected = {
    "phase1": ("analysis/workspace_audit_for_integration.zip", "ae594106080cbe9469d242fb3378079368552178142c4984f3211cce85eb7abd"),
    "phase2": ("analysis/integration_design_package.zip", "8b63bb35d632496bd98303c6878d9030941538180cf47ca5569ba1448fa54b76"),
    "phase3": ("analysis/phase3_calibration_package.zip", "0768d7fa6b57b41f118f71f8365aaffbf7b92198c3447f8458ff3560a198339e"),
    "phase4": ("analysis/phase4_rehearsal_package.zip", "5faa27a32784c89d262bb30b680fae743bc3e31e5bc6cff06b9644d1636d7ebf"),
    "phase4r": ("analysis/phase4r_remediation_package.zip", "ac188344776cf4827e838ec326f07688b9ddf5e430e27068c28796fcf1c9146e"),
}
archives = {}
errors = []
for label, (rel, expected) in archive_expected.items():
    path = ROOT / rel
    observed = sha(path)
    with zipfile.ZipFile(path) as archive:
        bad_crc = archive.testzip()
        names = archive.namelist()
    archives[label] = {"path": rel, "sha256": observed, "expected": expected, "member_count": len(names), "crc_ok": bad_crc is None}
    if observed != expected or bad_crc:
        errors.append(f"{label}_archive_mismatch")

manifest = json.loads((P4R / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
with zipfile.ZipFile(ROOT / archive_expected["phase4r"][0]) as archive:
    members = set(archive.namelist())
    listed = {item["path"]: item for item in manifest["inventory"]}
    if members != set(listed) | {"PACKAGE_MANIFEST.json"}:
        errors.append("phase4r_archive_membership")
    for rel, item in listed.items():
        if not (P4R / rel).is_file() or sha(P4R / rel) != item["sha256"]:
            errors.append("phase4r_file_drift:" + rel)

protected_rows = rows(P4R / "PROTECTED_FILE_HASHES_INITIAL.csv")
protected = []
for row in protected_rows:
    path = ROOT / row["path"]
    observed = sha(path) if path.is_file() else None
    protected.append({"path": row["path"], "size": path.stat().st_size if path.is_file() else None, "sha256": observed})
    if observed != row["sha256"]:
        errors.append("protected_input_drift:" + row["path"])
with (OUT / "PROTECTED_FILE_HASHES_INITIAL.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["path", "size", "sha256"])
    w.writeheader()
    w.writerows(protected)

config_path = P4R / "REMEDIATED_WORKFLOW_CONFIGURATION.json"
config = json.loads(config_path.read_text(encoding="utf-8"))
canonical = json.dumps({k: v for k, v in config.items() if k != "configuration_sha256"}, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
fingerprint = hashlib.sha256(canonical).hexdigest()
if fingerprint != config["configuration_sha256"] or fingerprint != "ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb":
    errors.append("methodology_fingerprint")
for component, data in config["components"].items():
    if isinstance(data, dict) and "files" in data:
        for entry in data["files"]:
            path = P4R / "candidate_v4r" / entry["path"]
            if not path.is_file() or sha(path) != entry["sha256"]:
                errors.append("candidate_component_drift:" + component + ":" + entry["path"])

holdout_path = P4R / "PHASE4B_VALIDATION_HOLDOUT.csv"
holdout = rows(holdout_path)
holdout_sha = sha(holdout_path)
if holdout_sha != "5dd9b5edd41f93912290058731c6304e24d657470ff1a45835b5522bd10b0536":
    errors.append("holdout_csv_hash")
contamination = json.loads((P4R / "PHASE4B_HOLDOUT_CONTAMINATION_LOG.json").read_text(encoding="utf-8"))
if contamination.get("events") or contamination.get("contamination_count") != 0 or contamination.get("holdout_sha256") != holdout_sha:
    errors.append("holdout_contamination_record")
manifest_rows = {r["SummaryName"]: r for r in rows(ROOT / "analysis/manifest.csv")}
source_checks = []
for row in holdout:
    match = manifest_rows.get(row["summary_name"])
    if not match:
        errors.append("holdout_alias_missing:" + row["holdout_id"])
        continue
    rel = match["Pdf"].replace("\\", "/")
    path = ROOT / rel
    observed = sha(path) if path.is_file() else None
    source_checks.append({"holdout_id": row["holdout_id"], "paper_id": row["paper_report_id"], "path": rel, "expected_sha256": row["source_sha256"], "observed_sha256": observed})
    if observed != row["source_sha256"]:
        errors.append("holdout_source_drift:" + row["holdout_id"])
if len(holdout) != 8 or len({r["paper_report_id"] for r in holdout}) != 8 or len({r["source_sha256"] for r in holdout}) != 8:
    errors.append("holdout_identity_count")

reviews = json.loads((ROOT / "analysis/reviews.json").read_text(encoding="utf-8"))
if reviews != {}:
    errors.append("review_state_drift")
git = subprocess.run(["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, check=True, capture_output=True).stdout
(OUT / "GIT_STATUS_INITIAL.txt").write_bytes(git)
result = {
    "captured_at": datetime.now(timezone.utc).isoformat(),
    "archives": archives,
    "phase4r_archive_membership_count": len(listed) + 1,
    "protected_file_count": len(protected),
    "methodology_version": config["methodology_version"],
    "methodology_fingerprint": fingerprint,
    "holdout_sha256": holdout_sha,
    "holdout_count": len(holdout),
    "holdout_sources": source_checks,
    "holdout_contamination_count": contamination.get("contamination_count"),
    "live_source_verified": 0 if reviews == {} else "UNKNOWN",
    "live_promoted": 0 if reviews == {} else "UNKNOWN",
    "git_status_initial_sha256": hashlib.sha256(git).hexdigest(),
    "errors": errors,
    "passed": not errors,
}
(OUT / "PHASE4B_BASELINE.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
(OUT / "INPUT_DRIFT_REPORT.md").write_text("# Phase 4B input drift\n\n" + ("NO_RELEVANT_DRIFT\n" if not errors else "NO_GO_INPUT_DRIFT\n\n" + "\n".join("- " + e for e in errors) + "\n"), encoding="utf-8")
print(json.dumps({"passed": not errors, "errors": errors[:20], "protected": len(protected), "holdout": len(holdout), "archives": {k: v["member_count"] for k,v in archives.items()}}))
if errors:
    raise SystemExit(1)
