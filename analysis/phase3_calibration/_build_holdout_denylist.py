from __future__ import annotations

import csv, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader((HERE / "PHASE4_VALIDATION_HOLDOUT.csv").open(encoding="utf-8-sig")))
payload = {
    "version": "phase3-holdout-denylist-v1",
    "holdout_csv_sha256": hashlib.sha256((HERE / "PHASE4_VALIDATION_HOLDOUT.csv").read_bytes()).hexdigest(),
    "paper_report_ids": sorted({r["paper_report_id"] for r in rows}),
    "source_file_ids": sorted({r["source_file_id"] for r in rows}),
    "source_sha256": sorted({r["source_sha256"] for r in rows}),
    "prohibited_operations": [
        "CLAIM_EXTRACTION", "SUMMARY_EVALUATION", "STRUCTURED_EVIDENCE_EXTRACTION",
        "SCIENTIFIC_VERIFICATION", "LOCATOR_QUALITY_EVALUATION", "GAP_ANALYSIS",
        "TAXONOMY_CODING", "METHODOLOGY_RESULTS_INSPECTION", "REUSE_QUALITY_ASSESSMENT"
    ],
    "allowed_operations": [
        "IDENTITY_CONFIRMATION", "SOURCE_HASH_CONFIRMATION", "ARTIFACT_INVENTORY",
        "PROCESSING_STATE_CONFIRMATION", "SELECTION_STRUCTURAL_METADATA"
    ]
}
(HERE / "HOLDOUT_DENYLIST.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
