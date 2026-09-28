"""Conservative Phase 4R development reassessment of H05/H06 Phase 4 items.

The input reports, prior source adjudications, protocols, and exact source PDFs
are read-only. This writes only within this H05/H06 development lane. No
record grants scientific acceptance or claims human-reviewed ground truth.
"""

from __future__ import annotations

import collections
import hashlib
import json
from pathlib import Path

ROOT = Path("analysis/phase4r_remediation/development_lanes/h05_h06")
PHASE4 = Path("analysis/phase4_rehearsal/holdout_validation")
ADJ_PATH = Path("analysis/phase4r_remediation/adjudication_lanes/h05_h06/H05_H06_DISAGREEMENT_ADJUDICATION.json")
PROTOCOLS = [
    Path("analysis/phase4r_remediation/ATOMIC_CLAIM_DECOMPOSITION.md"),
    Path("analysis/phase4r_remediation/LOCATOR_ENTAILMENT_PROTOCOL.md"),
    Path("analysis/phase4r_remediation/VERIFICATION_PROTOCOL_V2.md"),
    Path("analysis/phase4r_remediation/DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION.md"),
    Path("analysis/phase4r_remediation/candidate_v4r/deploy_payload/protocols/SCIENTIFIC_EVIDENCE_V3.md"),
]

# Previously Phase 4 verifier-supported items that do not meet the new exact
# support-locator contract as originally represented. Source truth is retained;
# the locator/atomic representation regresses under the stricter contract.
SUPPORTED_REPAIRS = {
    ("H05", "results.quantitative"): {
        "pages": [7],
        "table_cells": [
            {"table": "Table 1", "row": "WebVoyager human labels", "column": "Overall", "value": "59.1%"},
            {"table": "Table 2", "row": "Full trajectory", "columns": ["Agreement", "kappa"], "values": ["85.3%", "0.70"]},
        ],
        "reason": "The original TABLE locator names both tables but omits the rows/columns required by v3 for two distinct quantitative propositions.",
    },
    ("H05", "results.qualitative"): {
        "pages": [6, 8], "figures": ["Figure 6"],
        "reason": "The text-heavy contrast is discussed on pages 6/8; the website-complexity relationship uses Figure 6. A single page locator lacks proposition-specific text/figure binding.",
    },
    ("H05", "reproducibility.benchmark"): {
        "pages": [4, 5], "figures": ["Figure 3"],
        "reason": "Website selection begins on page 4; task construction and 643-task composition are on page 5. The original page-5 locator does not cover all parts.",
    },
    ("H06", "framing.problem"): {
        "pages": [1, 2, 3],
        "reason": "Page 2 frames scale, speed, bounded resources, spam and politeness; the explicit single-server condition is on pages 1/3. The original page-2 locator is incomplete.",
    },
    ("H06", "framing.research_questions"): {
        "pages": [2, 3],
        "reason": "The first open problem starts on page 2; second and third are on page 3. The original page-3 locator does not cover all three.",
    },
}

SPECIAL_VALUES = {
    ("H05", "methods.experiment_design"): (
        "The study compares multimodal, text-only, and GPT-4 tool baselines; human raters and model evaluators assess trajectories. The authors sampled 300 tasks from the benchmark and categorized failures among that sample; the count of failed cases is not stated as 300.",
        "SAMPLE_DENOMINATOR_SCOPE_ERROR corrected from '300 failures' to '300 tasks sampled; failed subset count unspecified'.",
    ),
    ("H06", "results.qualitative"): (
        "In the authors' reported single-server crawl, their combined techniques avoided the bottlenecks encountered in prior experiments; this is a reported case outcome, not a general guarantee.",
        "Original page 27 is context-only. Proposed source support is abstract page 1 and conclusion page 32, with the single-crawl qualifier retained.",
    ),
}

FAIL_CLOSED = {
    ("H05", "validity.threats"): "Mixed source observations and analyst inference need separate premise and inference records; the original composite is not accepted.",
    ("H06", "validity.threats"): "Mixed source observations and analyst inference need separate premise and inference records; the original composite is not accepted.",
}

LOWER_RISK_REPAIRS = {
    ("H05", "forward.future_work"): [6, 9, 10],
    ("H05", "forward.open_problems"): [8, 9, 10],
    ("H06", "framing.motivation"): [2, 3],
    ("H06", "forward.open_problems"): [29, 30, 31, 32],
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def locator_pages(locator: dict) -> list[int]:
    if "page" in locator:
        return [locator["page"]]
    if "start" in locator and "end" in locator:
        return list(range(locator["start"], locator["end"] + 1))
    return []


def compound_proposal(pages: list[int], source_sha256: str, repair: dict | None = None) -> dict:
    repair = repair or {}
    components = [{"type": "PAGE", "page": n, "source_sha256": source_sha256} for n in sorted(set(pages))]
    for cell in repair.get("table_cells", []):
        components.append({"type": "TABLE_CELL_PROPOSAL", **cell, "source_sha256": source_sha256})
    for fig in repair.get("figures", []):
        components.append({"type": "FIGURE_PROPOSAL", "figure_identifier": fig, "source_sha256": source_sha256})
    return {
        "type": "COMPOUND_SUPPORT_PROPOSAL" if len(components) > 1 else "SINGLE_SUPPORT_PROPOSAL",
        "components": components,
        "proposition_to_component_mapping": "REQUIRED_BEFORE_ACCEPTANCE",
        "source_entailment_recheck": "REQUIRED_BEFORE_ACCEPTANCE",
        "status": "DEVELOPMENT_PROPOSAL_NOT_ACCEPTED",
    }


def build() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    adjudications = json.loads(ADJ_PATH.read_text(encoding="utf-8"))["records"]
    adj_by_item = {x["evidence_item_id"]: x for x in adjudications}
    assert len(adj_by_item) == 26
    protocol_hashes = {str(p).replace("\\", "/"): sha(p) for p in PROTOCOLS}
    rows: list[dict] = []
    lower_rows: list[dict] = []
    for holdout in ("H05", "H06"):
        verifier_path = PHASE4 / "verifier_b" / f"{holdout}_verification.json"
        primary_path = next((PHASE4 / "primary_b").glob(f"{holdout}_report_*.json"))
        verifier = json.loads(verifier_path.read_text(encoding="utf-8"))
        primary = json.loads(primary_path.read_text(encoding="utf-8"))
        source_path = Path(f"analysis/phase4_rehearsal/private_source_material/holdout_sources/{holdout}/source.pdf")
        assert sha(source_path) == primary["source_sha256"] == verifier["source_sha256"]
        by_verifier = {x["stable_item_id"]: x for x in verifier["verified_evidence_items"]}
        disagreements = set(verifier["critical_disagreement_item_ids"])
        critical_count = 0
        for item in primary["evidence_items"]:
            key = (holdout, item["stable_field_id"])
            verified = by_verifier.get(item["stable_item_id"])
            original_pages = locator_pages(item["locator"])
            if not item["critical"]:
                lower_rows.append({
                    "holdout_id": holdout,
                    "paper_id": primary["paper_id"],
                    "source_sha256": primary["source_sha256"],
                    "evidence_item_id": item["stable_item_id"],
                    "field_id": item["stable_field_id"],
                    "phase4_sampling_status": "SAMPLED" if verified else "NOT_SAMPLED",
                    "phase4_verifier_finding": verified["verifier_finding"] if verified else None,
                    "v3_development_status": "LOCATOR_REPAIR_PROPOSED_NOT_ACCEPTED" if key in LOWER_RISK_REPAIRS else "PREVIOUS_SOURCE_SUPPORT_RETAINED_NOT_ACCEPTED",
                    "corrected_support_locator_proposal": compound_proposal(LOWER_RISK_REPAIRS.get(key, original_pages), primary["source_sha256"]),
                    "scientific_acceptance_granted": False,
                })
                continue
            critical_count += 1
            assert verified is not None
            is_disagreement = item["stable_item_id"] in disagreements
            adj = adj_by_item.get(item["stable_item_id"])
            assert bool(adj) == is_disagreement
            if is_disagreement:
                pages = adj["exact_source_evidence"]["pdf_pages"]
                if key == ("H06", "results.qualitative"):
                    pages = [1, 32]  # page 27 was discovery/context, not support
                if key in FAIL_CLOSED:
                    outcome = "FAIL_CLOSED_UNRESOLVED_INFERENCE"
                    value = None
                    note = FAIL_CLOSED[key]
                    disposition = "FAIL_CLOSED"
                else:
                    outcome = "CORRECTION_PROPOSED_NOT_ACCEPTED"
                    value, note = SPECIAL_VALUES.get(key, (item["statement"], adj["adjudication_rationale"]))
                    disposition = "CORRECTION_PROPOSED"
                repair = None
            else:
                repair = SUPPORTED_REPAIRS.get(key)
                if repair:
                    pages = repair["pages"]
                    outcome = "PREVIOUSLY_SUPPORTED_LOCATOR_REGRESSED_UNDER_V3"
                    value = item["statement"]
                    note = repair["reason"]
                else:
                    pages = original_pages
                    outcome = "PREVIOUS_SOURCE_SUPPORT_RETAINED_NOT_ACCEPTED"
                    value = item["statement"]
                    note = "The original source-grounded support is retained at field level; v3 atomic records and independent acceptance were not created."
                disposition = None
            numeric_origin = (
                "REPORTED_BY_SOURCE" if key in {("H05", "results.quantitative"), ("H06", "results.quantitative"), ("H06", "results.uncertainty_statistics")} else
                "SAMPLE_COUNT_CORRECTED" if key == ("H05", "methods.experiment_design") else
                "NOT_APPLICABLE_OR_NOT_ASSERTED"
            )
            rows.append({
                "evaluation_mode": "REMEDIATION_DEVELOPMENT_EVALUATION",
                "holdout_id": holdout,
                "paper_id": primary["paper_id"],
                "source_sha256": primary["source_sha256"],
                "original_evidence_item_id": item["stable_item_id"],
                "field_id": item["stable_field_id"],
                "original_statement": item["statement"],
                "original_locator": item["locator"],
                "phase4_verifier_finding": verified["verifier_finding"],
                "phase4_disagreement": is_disagreement,
                "phase4_disagreement_id": adj["disagreement_id"] if adj else None,
                "phase4_source_adjudicated_outcome": adj["adjudicated_outcome"] if adj else None,
                "v3_assessment": outcome,
                "original_v2_payload_remains_fail_closed": is_disagreement or bool(repair),
                "disagreement_disposition": disposition,
                "corrected_value_proposal": value,
                "corrected_support_locator_proposal": compound_proposal(pages, primary["source_sha256"], repair),
                "atomic_decomposition_status": "REQUIRED_BEFORE_ACCEPTANCE",
                "quantitative_origin": numeric_origin,
                "comparative_reconciliation_status": "REQUIRED_BEFORE_ACCEPTANCE" if item["stable_field_id"].endswith("comparative") else "NOT_APPLICABLE",
                "source_review_pdf_pages": sorted(set(pages)),
                "source_evidence_private_reference": adj["exact_source_evidence"] if adj else {"source_pdf_sha256": primary["source_sha256"], "source_pages": sorted(set(pages)), "classification": "EXACT_SOURCE_READ_ONLY"},
                "reason_or_correction": note,
                "verification_mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION_IN_PHASE4_PLUS_PHASE4R_DEVELOPMENT_REVIEW",
                "human_source_review_performed": False,
                "ground_truth_critical_false_accepts": "UNKNOWN",
                "scientific_acceptance_granted": False,
            })
        assert critical_count == (27 if holdout == "H05" else 25)
    assert len(rows) == 52 and len(lower_rows) == 8
    assert sum(x["phase4_disagreement"] for x in rows) == 26
    assert sum(x["v3_assessment"] == "CORRECTION_PROPOSED_NOT_ACCEPTED" for x in rows) == 24
    assert sum(x["v3_assessment"] == "FAIL_CLOSED_UNRESOLVED_INFERENCE" for x in rows) == 2
    assert sum(x["v3_assessment"] == "PREVIOUS_SOURCE_SUPPORT_RETAINED_NOT_ACCEPTED" for x in rows) == 21
    assert sum(x["v3_assessment"] == "PREVIOUSLY_SUPPORTED_LOCATOR_REGRESSED_UNDER_V3" for x in rows) == 5
    report = {
        "schema_version": "phase4r-development-rerun-h05-h06-v1",
        "scope": "H05_H06_CONSUMED_DEVELOPMENT_SET_ONLY",
        "source_human_ground_truth": "UNKNOWN",
        "scientific_acceptance_granted": False,
        "protocol_sha256": protocol_hashes,
        "phase4r_adjudication_sha256": sha(ADJ_PATH),
        "critical_original_item_count": len(rows),
        "original_disagreement_count": 26,
        "original_disagreement_correction_proposals": 24,
        "original_disagreement_fail_closed": 2,
        "original_disagreement_original_payloads_accepted": 0,
        "previously_verifier_supported_count": 26,
        "previously_verifier_supported_retained_source_support": 21,
        "previously_verifier_supported_locator_regressions": 5,
        "previously_verifier_supported_material_value_regressions_detected": 0,
        "lower_risk_original_item_count": len(lower_rows),
        "lower_risk_sampled_in_phase4": sum(x["phase4_sampling_status"] == "SAMPLED" for x in lower_rows),
        "lower_risk_not_sampled_in_phase4": sum(x["phase4_sampling_status"] == "NOT_SAMPLED" for x in lower_rows),
        "critical_items": rows,
        "lower_risk_status": lower_rows,
    }
    out = ROOT / "H05_H06_DEVELOPMENT_RERUN.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    print("critical", len(rows), "outcomes", dict(collections.Counter(x["v3_assessment"] for x in rows)))
    print("lower_risk", len(lower_rows), "sampled", report["lower_risk_sampled_in_phase4"])


if __name__ == "__main__":
    build()
