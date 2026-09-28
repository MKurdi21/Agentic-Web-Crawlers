"""Read the finished Phase 4R archive independently of its builder."""
import csv
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

OUT = Path(__file__).resolve().parent
ZIP = OUT.parent / "phase4r_remediation_package.zip"


def sha(data):
    return hashlib.sha256(data).hexdigest()


with (OUT / "PROTECTED_FILE_HASHES_INITIAL.csv").open(encoding="utf-8", newline="") as stream:
    protected = {
        r["sha256"] for r in csv.DictReader(stream)
        if r["path"].casefold().endswith((".pdf", "comprehensive_summary.md", "/article.txt"))
        or r["path"].casefold().startswith("analysis/evidence_runs/")
    }

forbidden_parts = {
    "private_source_material", "private_source_evidence", "shadow", "rehearsal_runtime",
    "phase4_failure_evidence", "adjudication_lanes", "development_lanes", "__pycache__",
}
forbidden_suffixes = {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".sqlite", ".sqlite3", ".db", ".zip", ".7z", ".gz", ".log", ".pyc"}
errors = []
observed = {}
with zipfile.ZipFile(ZIP) as archive:
    infos = archive.infolist()
    names = [x.filename for x in infos]
    if len(names) != len(set(n.casefold() for n in names)):
        errors.append("duplicate_or_case_colliding_member")
    for info in infos:
        name = info.filename
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name:
            errors.append(f"unsafe_path:{name}")
        if forbidden_parts.intersection(x.casefold() for x in path.parts):
            errors.append(f"private_or_runtime_path:{name}")
        if path.suffix.casefold() in forbidden_suffixes:
            errors.append(f"forbidden_suffix:{name}")
        if path.name.casefold() in {"article.txt", "checkpoint.json", "reviews.json", "baseline.json", "agents.md"}:
            errors.append(f"known_original_filename:{name}")
        try:
            data = archive.read(info)
        except Exception as exc:
            errors.append(f"crc_or_read_error:{name}:{type(exc).__name__}")
            continue
        digest = sha(data)
        observed[name] = {"sha256": digest, "size_bytes": len(data)}
        if digest in protected:
            errors.append(f"protected_hash:{name}")
        if data.startswith((b"%PDF", b"\x89PNG", b"SQLite format 3", b"PK\x03\x04")):
            errors.append(f"forbidden_signature:{name}")
    if "PACKAGE_MANIFEST.json" not in observed:
        errors.append("missing_manifest")
        manifest = {"inventory": []}
    else:
        manifest = json.loads(archive.read("PACKAGE_MANIFEST.json"))

listed = {x["path"]: x for x in manifest["inventory"]}
if len(listed) != len(manifest["inventory"]):
    errors.append("duplicate_manifest_inventory")
if set(observed) != set(listed) | {"PACKAGE_MANIFEST.json"}:
    errors.append("manifest_membership_mismatch")
for name, item in listed.items():
    if name not in observed:
        errors.append(f"missing_member:{name}")
    elif observed[name] != {"sha256": item["sha256"], "size_bytes": item["size_bytes"]}:
        errors.append(f"member_hash_or_size_mismatch:{name}")
    source = OUT / name
    if not source.is_file() or sha(source.read_bytes()) != item["sha256"]:
        errors.append(f"source_inventory_mismatch:{name}")

result = {
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "archive_path": str(ZIP),
    "archive_sha256": sha(ZIP.read_bytes()),
    "member_count": len(observed),
    "inventory_count": len(listed),
    "protected_hash_count": len(protected),
    "crc_integrity": not any(e.startswith("crc_or_read_error") for e in errors),
    "errors": errors,
    "passed": not errors,
}
(OUT / "test_results/INDEPENDENT_PACKAGE_VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
(OUT / "PACKAGE_RECEIPT.json").write_text(json.dumps({
    "archive_path": str(ZIP), "sha256": result["archive_sha256"],
    "member_count": result["member_count"], "independent_validation_passed": result["passed"],
    "validation_receipt": "test_results/INDEPENDENT_PACKAGE_VALIDATION.json",
}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("archive_sha256", "member_count", "inventory_count", "passed", "errors")}))
if errors:
    raise SystemExit(1)
