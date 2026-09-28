"""Build and independently validate the Phase 4 gate-failure handoff ZIP."""
from __future__ import annotations

import csv
import hashlib
import json
import os
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent
ZIP = ROOT.parent / "phase4_rehearsal_package.zip"
MANIFEST = ROOT / "PACKAGE_MANIFEST.json"
RECEIPT = ROOT / "PACKAGE_RECEIPT.json"
EXACT_FILES = [
    "PHASE4_BASELINE.json",
    "INPUT_DRIFT_REPORT.md",
    "CANDIDATE_FROZEN_RECEIPT.json",
    "FROZEN_VALIDATION_CONFIGURATION.json",
    "FROZEN_VALIDATION_CONFIGURATION.md",
    "FROZEN_CONFIG_GUARD.json",
    "HOLDOUT_PREVALIDATION_CHECK.json",
    "HOLDOUT_VERIFICATION_SAMPLE_MANIFEST.json",
    "HOLDOUT_DISAGREEMENTS.csv",
    "HOLDOUT_VALIDATION_METRICS.json",
    "HOLDOUT_VALIDATION_REPORT.md",
    "HOLDOUT_LIMITATIONS.md",
    "EXECUTIVE_PHASE4.md",
    "PHASE4_READINESS.md",
    "LANE_B_BLOCKED.json",
    "LANE_B_REHEARSAL_REPORT.md",
    "CROSS_STORE_SNAPSHOT_PROTOCOL.md",
    "CROSS_STORE_SNAPSHOT_RECEIPT.json",
    "ARTIFACT_CLOSURE_MANIFEST.json",
    "CROSS_STORE_SNAPSHOT_TESTS.md",
    "PHASE4_POLICY_STATUS.md",
    "PHASE5_CUTOVER_PROPOSAL.md",
    "PRESERVATION_CHECK.json",
    "FINAL_HANDOFF.json",
    "test_results/CROSS_STORE_SNAPSHOT_TESTS.json",
]
ALLOW_ROOTS = ("candidate_frozen", "holdout_validation")
FORBIDDEN_PARTS = {
    "private_source_material", "rehearsal_runtime", "calibration_records", "__pycache__",
    ".git", "backups", "artifact_store", "source_pages", "page_images",
}
FORBIDDEN_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".db", ".sqlite", ".sqlite3", ".zip", ".7z", ".gz"}
ALLOWED_SUFFIXES = {".md", ".json", ".csv", ".py", ".sql", ".txt", ".yaml", ".yml", ".toml"}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def assert_path(name: str) -> None:
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or "\\" in name or ":" in name:
        raise RuntimeError(f"unsafe archive path: {name}")
    if set(x.casefold() for x in p.parts) & FORBIDDEN_PARTS:
        raise RuntimeError(f"private/runtime path: {name}")
    if p.suffix.lower() in FORBIDDEN_SUFFIXES or p.suffix.lower() not in ALLOWED_SUFFIXES:
        raise RuntimeError(f"forbidden type: {name}")


files = [ROOT / name for name in EXACT_FILES]
for root_name in ALLOW_ROOTS:
    files.extend(p for p in (ROOT / root_name).rglob("*") if p.is_file())
files = sorted(files, key=lambda p: p.relative_to(ROOT).as_posix().casefold())
if len(files) != len(set(files)):
    raise RuntimeError("duplicate file on allowlist")

protected = set()
with (ROOT / "PROTECTED_FILE_HASHES_INITIAL.csv").open(encoding="utf-8", newline="") as handle:
    for row in csv.DictReader(handle):
        p = row["path"].lower()
        if (p.endswith(".pdf") or p.endswith("comprehensive_summary.md")
                or p.endswith("/article.txt") or p.startswith("analysis/evidence_runs/")):
            protected.add(row["sha256"])

inventory = []
for p in files:
    if not p.is_file():
        raise RuntimeError(f"missing allowlisted file: {p}")
    rel = p.relative_to(ROOT).as_posix()
    assert_path(rel)
    data = p.read_bytes()
    if data.startswith((b"%PDF", b"\x89PNG", b"SQLite format 3", b"PK\x03\x04")):
        raise RuntimeError(f"forbidden content signature: {rel}")
    digest = sha_bytes(data)
    if digest in protected:
        raise RuntimeError(f"protected original bytes: {rel}")
    inventory.append({"path": rel, "size_bytes": len(data), "sha256": digest, "classification": "PACKAGEABLE_DESIGN_OUTPUT"})

manifest = {
    "schema_version": "phase4-explicit-allowlist-v1",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "result": "NO_GO",
    "allowlisted_roots": list(ALLOW_ROOTS),
    "exact_files": EXACT_FILES,
    "forbidden_roots": sorted(FORBIDDEN_PARTS),
    "forbidden_suffixes": sorted(FORBIDDEN_SUFFIXES),
    "inventory": inventory,
    "archive_manifest_member": "PACKAGE_MANIFEST.json",
}
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=8) as archive:
    for row in inventory:
        archive.write(ROOT / row["path"], arcname=row["path"])
    archive.write(MANIFEST, arcname="PACKAGE_MANIFEST.json")

# Validate the resulting archive independently of the candidate-path enumeration.
with zipfile.ZipFile(ZIP, "r") as archive:
    names = archive.namelist()
    if archive.testzip() is not None:
        raise RuntimeError("archive CRC failed")
    if len(names) != len(set(names)) or len(names) != len(set(n.casefold() for n in names)):
        raise RuntimeError("duplicate or case-colliding archive member")
    expected = {row["path"] for row in inventory} | {"PACKAGE_MANIFEST.json"}
    if set(names) != expected:
        raise RuntimeError("archive membership differs from allowlist")
    embedded = json.loads(archive.read("PACKAGE_MANIFEST.json"))
    if embedded["inventory"] != inventory:
        raise RuntimeError("archive manifest mismatch")
    for row in embedded["inventory"]:
        name = row["path"]
        assert_path(name)
        data = archive.read(name)
        if len(data) != row["size_bytes"] or sha_bytes(data) != row["sha256"]:
            raise RuntimeError(f"archive member integrity failure: {name}")
        if data.startswith((b"%PDF", b"\x89PNG", b"SQLite format 3", b"PK\x03\x04")) or sha_bytes(data) in protected:
            raise RuntimeError(f"forbidden archive content: {name}")

receipt = {
    "created_at": datetime.now(timezone.utc).isoformat(),
    "archive_path": str(ZIP),
    "archive_sha256": sha(ZIP),
    "archive_member_count": len(inventory) + 1,
    "manifest_sha256": sha(MANIFEST),
    "crc_passed": True,
    "exact_membership_passed": True,
    "member_hashes_passed": True,
    "forbidden_path_and_type_check_passed": True,
    "protected_original_hash_check_passed": True,
    "private_source_included": False,
}
RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
