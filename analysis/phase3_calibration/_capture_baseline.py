from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXCLUDED_PREFIXES = {
    "analysis/phase3_calibration/",
}
EXCLUDED_FILES = {"analysis/phase3_calibration_package.zip"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def protected_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        r = rel(path)
        if r.startswith(".git/") or r in EXCLUDED_FILES:
            continue
        if any(r.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
        files.append(path)
    return sorted(files, key=lambda p: rel(p).casefold())


def zip_info(path: Path, expected: str) -> dict:
    digest = sha256(path)
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        names = zf.namelist()
    return {
        "path": rel(path),
        "size": path.stat().st_size,
        "sha256": digest,
        "expected_sha256": expected,
        "hash_matches": digest == expected,
        "member_count": len(names),
        "crc_ok": bad is None,
        "first_bad_member": bad,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in protected_files():
        stat = path.stat()
        rows.append({
            "path": rel(path),
            "size": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "sha256": sha256(path),
        })
    with (OUT / "PROTECTED_FILE_HASHES_INITIAL.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "size", "mtime_ns", "sha256"])
        writer.writeheader()
        writer.writerows(rows)

    git = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    (OUT / "GIT_STATUS_INITIAL.txt").write_text(git.stdout, encoding="utf-8")

    manifest_rows = list(csv.DictReader((ROOT / "analysis/manifest.csv").open(encoding="utf-8-sig")))
    pdfs = [p for p in ROOT.rglob("*.pdf") if "analysis/phase3_calibration" not in p.as_posix()]
    active_pdfs = [p for p in pdfs if "99_Duplicates" not in p.parts]
    duplicate_pdfs = [p for p in pdfs if "99_Duplicates" in p.parts]
    legacy = list((ROOT / "Summaries").glob("*.md"))
    v2 = list((ROOT / ".summary_v2").glob("*.md"))
    reviews = json.loads((ROOT / "analysis/reviews.json").read_text(encoding="utf-8"))
    checkpoint = json.loads((ROOT / "analysis/checkpoint.json").read_text(encoding="utf-8"))
    cp_counts = checkpoint.get("counts", checkpoint.get("summary", {}))

    phase1 = zip_info(
        ROOT / "analysis/workspace_audit_for_integration.zip",
        "ae594106080cbe9469d242fb3378079368552178142c4984f3211cce85eb7abd",
    )
    phase2 = zip_info(
        ROOT / "analysis/integration_design_package.zip",
        "8b63bb35d632496bd98303c6878d9030941538180cf47ca5569ba1448fa54b76",
    )
    baseline = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "root": str(ROOT),
        "evidence_class": "PHASE3_INITIAL_BASELINE",
        "protected_file_count": len(rows),
        "protected_hash_inventory": "PROTECTED_FILE_HASHES_INITIAL.csv",
        "git_status_exit_code": git.returncode,
        "counts": {
            "manifest_reports": len(manifest_rows),
            "physical_pdfs": len(pdfs),
            "active_pdf_paths": len(active_pdfs),
            "duplicate_pdf_paths": len(duplicate_pdfs),
            "legacy_summaries": len(legacy),
            "v2_structural_drafts": len(v2),
            "review_records": len(reviews),
            "checkpoint_counts": cp_counts,
        },
        "archives": {"phase1": phase1, "phase2": phase2},
        "expected": {
            "physical_pdfs": 117,
            "active_reports": 112,
            "additional_exact_duplicates": 5,
            "legacy_summaries": 48,
            "v2_structural_drafts": 37,
            "source_verified": 0,
            "promoted": 0,
            "audit_unknowns": 13,
            "phase2_tests_passed": 50,
            "phase2_archive_members": 89,
        },
    }
    (OUT / "INITIAL_BASELINE.json").write_text(
        json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
