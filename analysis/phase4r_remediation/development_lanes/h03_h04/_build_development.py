"""Phase 4R development replay for consumed H03/H04 validation reports.

This does not edit Phase 4 records or create scientific acceptance. It uses
source adjudication and immutable Phase 4 source-review findings to propose
version-3 atomic/locator repairs and exercise deterministic guardrails.
"""
from __future__ import annotations

import collections
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
P4 = ROOT / "analysis/phase4_rehearsal"
P4R = ROOT / "analysis/phase4r_remediation"
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "analysis/phase3_calibration/_deps"))
SV3_PATH = P4R / "candidate_v4r/hardened/scripts/scientific_v3.py"
spec = importlib.util.spec_from_file_location("scientific_v3", SV3_PATH)
assert spec and spec.loader
sv3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sv3)

SOURCES = {
    "H03": (
        P4 / "holdout_validation/primary_a/H03_primary_extraction.json",
        P4 / "holdout_validation/verifier_a/H03_separate_context_verification.json",
        "item_outcomes",
        P4 / "private_source_material/holdout_sources/H03/source.pdf",
    ),
    "H04": (
        P4 / "holdout_validation/primary_b/H04_report_5b76dc0b8a92199dbda22672.json",
        P4 / "holdout_validation/verifier_b/H04_verification.json",
        "verified_evidence_items",
        P4 / "private_source_material/holdout_sources/H04/source.pdf",
    ),
}
ADJ = json.loads((P4R / "adjudication_lanes/h03_h04/ADJUDICATION_H03_H04.json").read_text(encoding="utf-8"))
ADJ_BY_ID = {r["evidence_item_id"]: r for r in ADJ["records"]}
assert len(ADJ_BY_ID) == 14

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def locator(source_hash: str, page: int, label: str = "PAGE") -> dict:
    return {"type": label, "source_sha256": source_hash, "pdf_page": page}

def correction(item: dict, adj: dict) -> tuple[str, list[dict], str]:
    """Proposed atomic values and exact support-page set, not acceptance."""
    src = adj["source_sha256"]
    f = item["stable_field_id"]
    pages = adj["exact_source_evidence"]["pdf_pages"]
    locs = [locator(src, p) for p in pages]
    if f == "results.quantitative" and adj["holdout_id"] == "H03":
        atoms = [
            {"proposition": "GPT-4V+SoM overall agent success is 16.37% within the Table 3 main-baseline comparison.", "support_locators": [locator(src, 8, "TABLE_3")]},
            {"proposition": "The Table 3 human reference overall success is 88.70%.", "support_locators": [locator(src, 8, "TABLE_3")]},
            {"proposition": "Appendix Table 5 reports GPT-4o overall agent success of 19.78%, exceeding 16.37%.", "support_locators": [locator(src, 13, "TABLE_5")]},
        ]
        return "KNOWN_FALSE_GLOBAL_COMPARISON_CORRECTED_TO_LOCAL_SCOPE", atoms, "CORRECTED_VALUE_PROPOSED"
    if f == "results.negative" and adj["holdout_id"] == "H04":
        atoms = [
            {"proposition": "Four of 20 target agents have zero reported vulnerabilities in Table 2.", "reported_or_derived": "DERIVED", "support_locators": [locator(src, 11, "TABLE_2_20_ROWS")]},
            {"proposition": "Sixteen of 20 target agents have nonzero reported vulnerabilities in Table 2.", "reported_or_derived": "DERIVED", "support_locators": [locator(src, 11, "TABLE_2_20_ROWS")]},
            {"proposition": "The authors say the source-code requirement prevents direct application to black-box commercial agents.", "support_locators": [locator(src, 15, "LIMITATIONS")]},
        ]
        return "KNOWN_FALSE_NEGATIVE_COUNT_CORRECTED", atoms, "CORRECTED_VALUE_PROPOSED"
    if adj["adjudicated_outcome"] == "BOTH_PARTIAL":
        atoms = [{"proposition": item.get("canonical_claim", {}).get("summary") or item["statement"], "support_locators": locs, "origin": "ANALYST_DERIVED_CONDITION_OR_THREAT", "verification_required": True}]
        return "FAIL_CLOSED_PENDING_ATOMIC_INFERENCE_REVIEW", atoms, "UNRESOLVED"
    atoms = [{"proposition": item.get("canonical_claim", {}).get("summary") or item["statement"], "support_locators": locs, "requires_atomic_split_when_multiple_material_propositions": True}]
    return "ORIGINAL_LOCATOR_REJECTED_CORRECTED_SUPPORT_SET_PROPOSED", atoms, "CORRECTED_LOCATOR_PROPOSED"

all_rows = []
lower = []
for holdout, (primary_path, verifier_path, verifier_key, pdf_path) in SOURCES.items():
    primary = json.loads(primary_path.read_text(encoding="utf-8"))
    verifier = json.loads(verifier_path.read_text(encoding="utf-8"))
    assert digest(pdf_path) == primary["source_sha256"] == verifier["source_sha256"]
    v_by_id = {x["stable_item_id"]: x for x in verifier[verifier_key]}
    for item in primary["evidence_items"]:
        item_id = item["stable_item_id"]
        v = v_by_id.get(item_id)
        original_claim = item.get("canonical_claim", {}).get("summary") or item.get("statement")
        if not item["critical"]:
            lower.append({
                "holdout_id": holdout,
                "paper_id": primary["paper_id"],
                "evidence_item_id": item_id,
                "field_id": item["stable_field_id"],
                "phase4_sampled": v is not None,
                "phase4_verifier_finding": v["verifier_finding"] if v else None,
                "phase4r_status": "PREVIOUSLY_SAMPLED_SUPPORTED_NOT_INDEPENDENT_REVALIDATION" if v and v["verifier_finding"] == "SUPPORTED" else "NOT_SAMPLED_NOT_REEVALUATED",
                "scientific_acceptance": False,
            })
            continue
        assert v is not None, (holdout, item_id)
        row = {
            "holdout_id": holdout,
            "paper_id": primary["paper_id"],
            "source_sha256": primary["source_sha256"],
            "evidence_item_id": item_id,
            "field_id": item["stable_field_id"],
            "critical": True,
            "original_claim": original_claim,
            "original_locator": item["locator"],
            "phase4_verifier_finding": v["verifier_finding"],
            "phase4_verification_mode": verifier["verification_mode"],
            "source_review_basis": "PHASE4_EXACT_SOURCE_VERIFIER_RECORD_PLUS_PHASE4R_TARGETED_SOURCE_ADJUDICATION" if item_id in ADJ_BY_ID else "PHASE4_EXACT_SOURCE_VERIFIER_RECORD_REPLAYED_UNDER_V3_RULES",
            "scientific_acceptance": False,
            "independent_human_source_review": False,
        }
        if item_id in ADJ_BY_ID:
            a = ADJ_BY_ID[item_id]
            assert a["source_sha256"] == primary["source_sha256"]
            status, atoms, fix_status = correction(item, a)
            row.update({
                "phase4r_outcome": status,
                "proposed_atomic_propositions": atoms,
                "proposed_corrected_value_status": fix_status,
                "source_adjudication_outcome": a["adjudicated_outcome"],
                "root_cause_code": a["root_cause_code"],
                "phase4r_source_evidence_ref": a["exact_source_evidence"],
                "original_supported_by_v3": False,
                "known_failure_corrected_or_fail_closed": True,
                "previously_verifier_supported": False,
                "preserved_or_regressed": "ORIGINAL_NOT_FULLY_SUPPORTED",
            })
        elif holdout == "H03" and item["stable_field_id"] == "identity.report_relationships":
            row.update({
                "phase4r_outcome": "FAIL_CLOSED_ABSENCE_CLAIM_NOT_PROVED_BY_SINGLE_PAGE",
                "proposed_atomic_propositions": [{"proposition": "Contribution/version relationship remains UNRESOLVED pending full report/corpus identity review.", "support_locators": [locator(primary["source_sha256"], 1)], "negative_claim_not_inferred": True}],
                "proposed_corrected_value_status": "UNRESOLVED",
                "original_supported_by_v3": False,
                "known_failure_corrected_or_fail_closed": False,
                "previously_verifier_supported": True,
                "preserved_or_regressed": "REGRESSED_SCOPE",
            })
        elif holdout == "H04" and item["stable_field_id"] == "identity.identifiers":
            row.update({
                "phase4r_outcome": "FAIL_CLOSED_DOCUMENT_WIDE_DOI_ABSENCE_NOT_PROVED_BY_COVER",
                "proposed_atomic_propositions": [
                    {"proposition": "The USENIX presentation URL appears on the source cover.", "support_locators": [locator(primary["source_sha256"], 1, "COVER_URL")]},
                    {"proposition": "DOI status UNKNOWN until source text, PDF metadata and publisher record are checked.", "support_locators": [], "negative_claim_not_inferred": True},
                ],
                "proposed_corrected_value_status": "PARTIAL_PRESERVED_AND_UNKNOWN",
                "original_supported_by_v3": False,
                "known_failure_corrected_or_fail_closed": False,
                "previously_verifier_supported": True,
                "preserved_or_regressed": "REGRESSED_SCOPE",
            })
        elif holdout == "H03" and item["stable_field_id"] == "results.negative" and "best model" in original_claim.lower():
            row.update({
                "phase4r_outcome": "CONTENT_PRESERVED_BUT_GLOBAL_SCOPE_LOCATOR_EXPANDED",
                "proposed_atomic_propositions": [
                    {"proposition": "The main Table 3 highest agent result is 16.37% while human reference is 88.70%.", "support_locators": [locator(primary["source_sha256"], 8, "TABLE_3")]},
                    {"proposition": "The later Table 5 GPT-4o result is 19.78%, still below the Table 3 human reference.", "support_locators": [locator(primary["source_sha256"], 13, "TABLE_5"), locator(primary["source_sha256"], 8, "TABLE_3")]},
                ],
                "proposed_corrected_value_status": "CONTENT_PRESERVED_LOCATOR_CORRECTED",
                "original_supported_by_v3": False,
                "known_failure_corrected_or_fail_closed": False,
                "previously_verifier_supported": True,
                "preserved_or_regressed": "REGRESSED_LOCATOR_ONLY",
            })
        else:
            row.update({
                "phase4r_outcome": "PREVIOUS_VERIFIER_SUPPORT_PRESERVED_PROVISIONALLY",
                "proposed_atomic_propositions": [{"proposition": original_claim, "support_locators": [item["locator"]], "decomposition_review_required_before_v3_acceptance": True}],
                "proposed_corrected_value_status": "UNCHANGED_PROVISIONAL",
                "original_supported_by_v3": "PENDING_FULL_ATOMIC_PAYLOAD",
                "known_failure_corrected_or_fail_closed": False,
                "previously_verifier_supported": True,
                "preserved_or_regressed": "PRESERVED_PROVISIONAL",
            })
        all_rows.append(row)

assert len(all_rows) == 73
assert len(lower) == 9
assert sum(x["known_failure_corrected_or_fail_closed"] for x in all_rows) == 14
assert sum(x["previously_verifier_supported"] for x in all_rows) == 59

# Deterministic actual-source regression: main Table 3 is only a local scope.
common = {
    "metric": "task_success_rate", "unit": "percent", "task": "all_VisualWebArena_tasks",
    "dataset": "VisualWebArena", "benchmark": "VisualWebArena",
    "split": "overall", "condition": "agent_evaluation",
}
main_values = [
    1.10, 1.76, 2.20, 2.20, 7.25, 0.66, 1.87, 2.75, 2.97, 3.85,
    12.75, 0.77, 0.33, 6.04, 15.05, 0.99, 0.33, 5.71, 16.37,
]
main = [{**common, "result_id": f"table3_agent_{i:02}", "value": str(v),
         "subject": f"table3_agent_{i:02}", "model_configuration": f"table3_agent_{i:02}",
         "source_location_id": "H03_TABLE_3_PDF_PAGE_8",
         "support_locator_ids": ["H03_TABLE_3_PDF_PAGE_8"]}
        for i, v in enumerate(main_values, start=1)]
target_id = main[-1]["result_id"]
appendix = [{**common, "result_id": "table5_gpt4o", "value": "19.78",
             "subject": "table5_gpt4o", "model_configuration": "table5_gpt4o",
             "source_location_id": "H03_TABLE_5_PDF_PAGE_13",
             "support_locator_ids": ["H03_TABLE_5_PDF_PAGE_13"]}]
local_claim = {"scope": "LOCAL", "target_result_id": target_id,
               "comparison_result_ids": [x["result_id"] for x in main],
               "support_locator_ids": ["H03_TABLE_3_PDF_PAGE_8"], "direction": "MAX", "strict": True}
local_result = sv3.reconcile_comparison(local_claim, {"results": main + appendix})
cross_claim = dict(local_claim, comparison_result_ids=[target_id, "table5_gpt4o"])
cross_result = sv3.reconcile_comparison(cross_claim, {"results": main + appendix})
global_claim = dict(local_claim, scope="DOCUMENT_WIDE")
global_result = sv3.reconcile_comparison(global_claim, {"results": main + appendix, "document_wide_complete": False})
assert local_result["status"] == "SUPPORTED_WITHIN_EXPLICIT_SCOPE"
assert cross_result["status"] == "CONTRADICTED"
assert global_result["status"] == "COMPARISON_SCOPE_UNRESOLVED"

# Rendered Table 2 was inspected and these exact 20 row/cell values transcribed.
vulnerabilities = [
    ("AutoGPT", 7), ("Dify", 1), ("LangFlow", 4), ("RagFlow", 2),
    ("Autogen", 1), ("Quivr", 0), ("LangChatchat", 2), ("Khoj", 1),
    ("Kotaemon", 1), ("GPT-Researcher", 3), ("Owl", 0), ("MaxKB", 1),
    ("DB-GPT", 1), ("SuperAGI", 3), ("DeerFlow", 1), ("Chuanhu", 1),
    ("AgentZero", 1), ("Bisheng", 0), ("AgentScope", 6), ("Taskweaver", 0),
]
cells = [{"table_id": "H04_Table_2", "row_label": name,
          "column_label": "Vulns", "locator_id": f"H04_TABLE2_{name.replace('-', '_')}",
          "value": value, "missing": False} for name, value in vulnerabilities]
zero = sv3.derive("COUNT_ZERO", cells)
affected = sv3.derive("AFFECTED_FROM_TOTAL_MINUS_ZERO", cells, total=20)
total_vulns = sv3.derive("SUM", cells)
assert (zero["result"], affected["result"], total_vulns["result"]) == ("4", "16", "36")
wrong_three = None
try:
    sv3.check_derived_claim({
        "reported_or_derived": "DERIVED", "value": 3,
        "derivation": {"operation": "COUNT_ZERO", "input_cell_keys": zero["input_cell_keys"]},
    }, cells)
except sv3.ScientificFailure as exc:
    wrong_three = exc.code
assert wrong_three == "DERIVED_VALUE_MISMATCH"

checks = {
    "schema_version": "phase4r-h03-h04-deterministic-receipts-v1",
    "data_role": "CONSUMED_VALIDATION_SET_DIAGNOSTIC_AND_REMEDIATION_DATA",
    "candidate_scientific_v3_sha256": digest(SV3_PATH),
    "h03": {
        "source_sha256": digest(SOURCES["H03"][3]),
        "main_table3_result_count": len(main),
        "main_table3_local_16_37": local_result,
        "cross_table_16_37_vs_19_78": cross_result,
        "unqualified_global_16_37": global_result,
        "source_review": "Rendered PDF Table 3 page 8 and Table 5 page 13 checked",
    },
    "h04": {
        "source_sha256": digest(SOURCES["H04"][3]),
        "table2_row_count": len(cells),
        "table2_source_cells": cells,
        "zero_vulnerability_count": zero,
        "affected_agent_count": affected,
        "total_vulnerabilities": total_vulns,
        "incorrect_three_check": wrong_three,
        "source_review": "Rendered PDF Table 2 page 11 checked",
    },
    "scientific_acceptance": False,
    "independent_validation": False,
}
(OUT / "GENERALIZED_CHECK_RECEIPTS_H03_H04.json").write_text(json.dumps(checks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

summary = {
    "critical_item_count": len(all_rows),
    "lower_risk_item_count": len(lower),
    "original_disagreement_count": 14,
    "known_failures_corrected_or_fail_closed": sum(x["known_failure_corrected_or_fail_closed"] for x in all_rows),
    "previously_verifier_supported_count": 59,
    "previously_supported_preserved_provisionally": sum(x["preserved_or_regressed"] == "PRESERVED_PROVISIONAL" for x in all_rows),
    "previously_supported_regressed_scope": sum(x["preserved_or_regressed"] == "REGRESSED_SCOPE" for x in all_rows),
    "previously_supported_regressed_locator_only": sum(x["preserved_or_regressed"] == "REGRESSED_LOCATOR_ONLY" for x in all_rows),
    "lower_risk_previously_sampled_supported": sum(x["phase4_sampled"] and x["phase4_verifier_finding"] == "SUPPORTED" for x in lower),
    "lower_risk_not_sampled": sum(not x["phase4_sampled"] for x in lower),
    "phase4r_scientific_acceptance_granted": False,
    "human_ground_truth": "UNKNOWN",
}
result = {
    "schema_version": "phase4r-h03-h04-development-v1",
    "data_role": "CONSUMED_VALIDATION_SET_DIAGNOSTIC_AND_REMEDIATION_DATA",
    "method": "Original critical evidence replay with revised atomic, comparative, derived-numeric and locator-entailment rules; exact-source Phase 4 verifier/adjudication retained; deterministic H03/H04 checks rerun.",
    "limitations": [
        "This is development remediation on the consumed Phase 4 holdout, not independent validation.",
        "Previously supported findings are preserved provisionally from Phase 4 exact-source verification; full V3 atomic payload construction is still required before any scientific acceptance.",
        "No qualified independent human source review occurred; ground-truth false-accept count remains UNKNOWN.",
    ],
    "source_pdf_hashes": {h: digest(files[3]) for h, files in SOURCES.items()},
    "summary": summary,
    "critical_items": all_rows,
    "lower_risk_items": lower,
    "generalized_check_receipts": "analysis/phase4r_remediation/development_lanes/h03_h04/GENERALIZED_CHECK_RECEIPTS_H03_H04.json",
}
(OUT / "DEVELOPMENT_REPLAY_H03_H04.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
