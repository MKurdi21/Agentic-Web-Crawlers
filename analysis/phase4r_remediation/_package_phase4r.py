"""Allowlist-only convenience archive. Private source and runtime stay outside."""
import csv
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
ZIP = ROOT.parent / "phase4r_remediation_package.zip"
EXACT_ROOT_FILES = [
    "EXECUTIVE_PHASE4R.md", "PHASE4R_BASELINE.json", "PHASE4_FAILURE_EVIDENCE_MANIFEST.json",
    "DISAGREEMENT_ADJUDICATION.md", "DISAGREEMENT_ADJUDICATION.json", "DISAGREEMENT_RESOLUTION_MATRIX.csv",
    "ROOT_CAUSE_TAXONOMY.md", "ROOT_CAUSE_TAXONOMY.json", "ROOT_CAUSE_CLOSURE_REPORT.md",
    "DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION.md", "DERIVED_NUMERIC_VERIFICATION.md",
    "LOCATOR_ENTAILMENT_PROTOCOL.md", "ATOMIC_CLAIM_DECOMPOSITION.md", "TABLE_EVIDENCE_MODEL.md",
    "FIELD_AUTOMATION_MATRIX_V2.csv", "VERIFICATION_PROTOCOL_V2.md", "SKILL_REMEDIATION_REPORT.md",
    "REMEDIATED_WORKFLOW_CONFIGURATION.json", "CONTROLLER_V4R_CHANGELOG.md",
    "REMEDIATION_DEVELOPMENT_RESULTS.md", "REMEDIATION_DEVELOPMENT_METRICS.json",
    "PHASE4B_HOLDOUT_SELECTION_PROTOCOL.md", "PHASE4B_VALIDATION_HOLDOUT.csv",
    "PHASE4B_HOLDOUT_SELECTION_RECEIPT.json", "PHASE4B_HOLDOUT_CONTAMINATION_LOG.json",
    "PHASE4B_ENTRY_CRITERIA.md", "PHASE4B_VALIDATION_PLAN.md",
    "FINAL_HANDOFF.json", "PRESERVATION_CHECK.json", "FINAL_REVIEW_STATUS.json", "FINGERPRINT_CORRECTION.md",
    "test_results/CANDIDATE_TEST_RESULTS.json",
    "test_results/INDEPENDENT_DEVELOPMENT_RECONCILIATION.json",
    "test_results/LIVE_SCIENTIFIC_STATE_CHECK.json",
    "candidate_v4r/requirements.txt",
    "candidate_v4r/deploy_payload/AGENTS.proposed.md",
]
ALLOW_ROOTS = [
    "candidate_v4r/hardened/scripts", "candidate_v4r/hardened/schemas", "candidate_v4r/hardened/tests",
    "candidate_v4r/hardened/db", "candidate_v4r/deploy_payload/skills",
    "candidate_v4r/deploy_payload/protocols", "phase4_failure_fixtures",
]
FORBIDDEN_PARTS = {"private_source_material", "private_source_evidence", "source_excerpts", "rendered_pages", "shadow", "rehearsal_runtime", "phase4_failure_evidence", "adjudication_lanes", "development_lanes", "_deps", "__pycache__", ".git"}
FORBIDDEN_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".sqlite", ".sqlite3", ".db", ".zip", ".7z", ".gz", ".log", ".pyc"}
ALLOWED_SUFFIXES = {".json", ".md", ".csv", ".py", ".sql", ".txt", ".yaml", ".yml", ".toml"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe(name):
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or "\\" in name or ":" in name:
        raise RuntimeError("unsafe path: " + name)
    if set(x.casefold() for x in p.parts) & FORBIDDEN_PARTS:
        raise RuntimeError("private/runtime path: " + name)
    if p.suffix.lower() in FORBIDDEN_SUFFIXES or p.suffix.lower() not in ALLOWED_SUFFIXES:
        raise RuntimeError("forbidden type: " + name)
    if p.name.lower() in {"article.txt", "checkpoint.json", "reviews.json", "baseline.json", "agents.md"} or p.name.lower().endswith("_comprehensive_summary.md"):
        raise RuntimeError("forbidden original name: " + name)


protected = set()
with (ROOT / "PROTECTED_FILE_HASHES_INITIAL.csv").open(encoding="utf-8", newline="") as stream:
    for row in csv.DictReader(stream):
        name = row["path"].lower()
        if name.endswith(".pdf") or name.endswith("comprehensive_summary.md") or name.endswith("/article.txt") or name.startswith("analysis/evidence_runs/"):
            protected.add(row["sha256"])

files = [ROOT / name for name in EXACT_ROOT_FILES]
for folder in ALLOW_ROOTS:
    files.extend(p for p in (ROOT / folder).rglob("*") if p.is_file())
files.sort(key=lambda p: p.relative_to(ROOT).as_posix().casefold())
inventory = []
seen = set()
for path in files:
    if not path.is_file():
        raise RuntimeError("missing allowlist file: " + str(path))
    relative = path.relative_to(ROOT).as_posix()
    safe(relative)
    if relative.casefold() in seen:
        raise RuntimeError("duplicate/case collision: " + relative)
    seen.add(relative.casefold())
    data = path.read_bytes()
    digest = sha(data)
    if data.startswith((b"%PDF", b"\x89PNG", b"SQLite format 3", b"PK\x03\x04")) or digest in protected:
        raise RuntimeError("protected content: " + relative)
    inventory.append({"path": relative, "size_bytes": len(data), "sha256": digest, "classification": "PACKAGEABLE_DESIGN_OUTPUT"})

manifest = {
    "schema_version": "phase4r-allowlist-v1",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "approved_package_roots": ALLOW_ROOTS,
    "approved_exact_files": EXACT_ROOT_FILES,
    "forbidden_parts": sorted(FORBIDDEN_PARTS),
    "forbidden_suffixes": sorted(FORBIDDEN_SUFFIXES),
    "never_package": ["private source PDFs/text/page images", "diagnostic import copies", "adjudication exact-source excerpts", "development-lane raw table observations", "runtime databases/stores/backups", "Phase 1–4 ZIPs"],
    "inventory": inventory,
    "manifest_member": "PACKAGE_MANIFEST.json",
}
(ROOT / "PACKAGE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=8) as archive:
    for item in inventory:
        archive.write(ROOT / item["path"], arcname=item["path"])
    archive.write(ROOT / "PACKAGE_MANIFEST.json", arcname="PACKAGE_MANIFEST.json")
print(json.dumps({"path": str(ZIP), "members": len(inventory) + 1, "sha256": sha(ZIP.read_bytes())}))
