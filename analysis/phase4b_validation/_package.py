"""Build and independently inspect a Phase 4B allowlist-only handoff archive."""
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
PACKAGE = OUT.parent / "phase4b_validation_package.zip"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return digest(path.read_bytes())


top_level = [
    "EXECUTIVE_PHASE4B.md", "PHASE4B_BASELINE.json", "INPUT_DRIFT_REPORT.md",
    "FROZEN_PHASE4B_CONFIGURATION.json", "FROZEN_PHASE4B_CONFIGURATION.md",
    "PHASE4B_HOLDOUT_PROCESSING_ORDER.json", "PHASE4B_HOLDOUT_PROCESSING_ORDER.md",
    "CANDIDATE_CODE_MANIFEST.json", "CANDIDATE_CODE_MANIFEST.md",
    "HOLDOUT_ACCESS_LEDGER.json", "HOLDOUT_CONTEXT_ISOLATION.json",
    "HOLDOUT_CONSERVATION_REPORT.md", "HOLDOUT_VALIDATION_REPORT.md",
    "HOLDOUT_VALIDATION_METRICS.json", "HOLDOUT_DISAGREEMENTS.csv",
    "HOLDOUT_LIMITATIONS.md", "HOLDOUT_PREVALIDATION_CHECK.json",
    "PHASE4B_POLICY_STATUS.md", "PHASE4B_READINESS.md",
    "PHASE5_CUTOVER_PROPOSAL.md", "FINAL_HANDOFF.json",
    "PRESERVATION_CHECK.json",
]
b01 = [
    "holdout_validation/B01/IMMUTABLE_CHECK_BEFORE.json",
    "holdout_validation/B01/IMMUTABLE_CHECK_AFTER.json",
    "holdout_validation/B01/PER_REPORT_GATE.json",
    "holdout_validation/B01/VERIFICATION_SAMPLE_MANIFEST.json",
    "holdout_validation/B01/VERIFIER_METRICS.json",
]
test_results = ["test_results/LANE_A2_GATE.json"]
scripts = sorted(p.name for p in OUT.glob("_*.py"))
candidate = sorted(
    p.relative_to(OUT).as_posix()
    for p in (OUT / "candidate_frozen").rglob("*")
    if p.is_file() and "__pycache__" not in p.parts and p.suffix.lower() != ".pyc"
)
allowed = sorted(set(top_level + b01 + test_results + scripts + candidate))
excluded_roots = {
    "private_source_material", "rehearsal_runtime", "candidate_v4r", "shadow",
    "calibration_records", "outbox", "backup", "backups", "_deps", "__pycache__",
}
forbidden_extensions = {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".sqlite", ".db", ".zip", ".7z", ".gz", ".bin", ".pyc"}
forbidden_names = {"article.txt", "accessibility.txt", "PRIMARY_CONTEXT_PACKET.json", "PRIMARY_SUMMARY.md", "VERIFIER_DISPATCH_MANIFEST.json"}
name_re = re.compile(r"(^|/)(staging_[^/]+\.tmp|article\.txt|source\.pdf)(/|$)", re.I)
inventory = []
for rel in allowed:
    path = OUT / rel
    if not path.is_file():
        raise RuntimeError("Missing allowlisted file: " + rel)
    parts = Path(rel).parts
    if set(parts) & excluded_roots or path.suffix.lower() in forbidden_extensions or path.name in forbidden_names or name_re.search(rel):
        raise RuntimeError("Forbidden allowlisted path: " + rel)
    data = path.read_bytes()
    if data.startswith((b"%PDF-", b"PK\x03\x04", b"\x89PNG\r\n\x1a\n", b"SQLite format 3")):
        raise RuntimeError("Forbidden content signature: " + rel)
    inventory.append({
        "path": rel,
        "size_bytes": len(data),
        "sha256": digest(data),
        "classification": "FROZEN_PACKAGEABLE_CANDIDATE_CODE" if rel.startswith("candidate_frozen/") else "SANITIZED_DESIGN_OUTPUT",
    })
manifest = {
    "schema_version": "phase4b-package-manifest-v1",
    "package_roots": ["candidate_frozen/", "holdout_validation/B01/", "test_results/"],
    "explicit_top_level_files": top_level + scripts,
    "never_package_roots": sorted(excluded_roots | {"holdout_validation/B01/private", "holdout_validation/B02", "holdout_validation/B03", "holdout_validation/B04", "holdout_validation/B05", "holdout_validation/B06", "holdout_validation/B07", "holdout_validation/B08"}),
    "inventory": inventory,
}
manifest_path = OUT / "PACKAGE_MANIFEST.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for entry in inventory:
        archive.write(OUT / entry["path"], arcname=entry["path"])
    archive.write(manifest_path, arcname="PACKAGE_MANIFEST.json")

# The validator uses the written ZIP and manifest bytes, not the builder's in-memory inventory.
validation_errors = []
with zipfile.ZipFile(PACKAGE) as archive:
    names = archive.namelist()
    if archive.testzip() is not None:
        validation_errors.append("CRC_FAILURE")
    if len(names) != len(set(names)):
        validation_errors.append("DUPLICATE_MEMBER")
    if len(names) != len({name.casefold() for name in names}):
        validation_errors.append("CASE_COLLISION")
    for name in names:
        if name.startswith("/") or "\\" in name or any(part in {"", ".", ".."} for part in name.split("/")):
            validation_errors.append("UNSAFE_PATH:" + name)
        if set(Path(name).parts) & excluded_roots or Path(name).suffix.lower() in forbidden_extensions or Path(name).name in forbidden_names or name_re.search(name):
            validation_errors.append("FORBIDDEN_PATH:" + name)
    decoded_manifest = json.loads(archive.read("PACKAGE_MANIFEST.json"))
    expected = {item["path"]: item for item in decoded_manifest["inventory"]}
    if set(names) != set(expected) | {"PACKAGE_MANIFEST.json"}:
        validation_errors.append("MEMBERSHIP_MISMATCH")
    for name, entry in expected.items():
        data = archive.read(name)
        if len(data) != entry["size_bytes"] or digest(data) != entry["sha256"]:
            validation_errors.append("CONTENT_MISMATCH:" + name)
        if data.startswith((b"%PDF-", b"PK\x03\x04", b"\x89PNG\r\n\x1a\n", b"SQLite format 3")):
            validation_errors.append("FORBIDDEN_SIGNATURE:" + name)
        if re.search(rb"(?m)^-----BEGIN (?:OPENSSH )?PRIVATE KEY-----\r?\n", data):
            validation_errors.append("CREDENTIAL_SIGNATURE:" + name)
    b01_source_hash = json.loads((OUT / "PHASE4B_BASELINE.json").read_text())["holdout_sources"][0]["expected_sha256"]
    if any(item["sha256"] == b01_source_hash for item in expected.values()):
        validation_errors.append("PRIVATE_PDF_HASH_MATCH")

receipt = {
    "created_at": datetime.now(timezone.utc).isoformat(),
    "package_path": str(PACKAGE),
    "sha256": sha(PACKAGE),
    "size_bytes": PACKAGE.stat().st_size,
    "member_count": len(names),
    "inventory_count": len(inventory),
    "manifest_sha256": sha(manifest_path),
    "crc_passed": "CRC_FAILURE" not in validation_errors,
    "independent_archive_validation_passed": not validation_errors,
    "errors": validation_errors,
    "excluded_private_material": True,
    "lane_b_artifacts_absent": not (OUT / "rehearsal_runtime").exists(),
}
(OUT / "PACKAGE_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: receipt[k] for k in ("sha256", "member_count", "size_bytes", "independent_archive_validation_passed", "errors")}))
if validation_errors:
    raise SystemExit(1)
