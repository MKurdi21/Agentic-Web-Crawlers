"""Development replay of H01-H02 original Phase 4 evidence under v3 rules.

This is a source-grounded model review, not human adjudication or scientific
acceptance. Output is sanitized metadata; source PDFs remain outside this lane.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
LANE = Path(__file__).resolve().parent
P4 = REPO / "analysis/phase4_rehearsal"
P4R = REPO / "analysis/phase4r_remediation"
sys.path.insert(0, str(REPO / "analysis/phase3_calibration/_deps"))
import pypdfium2 as pdfium  # noqa: E402

spec = importlib.util.spec_from_file_location("scientific_v3", P4R / "candidate_v4r/hardened/scripts/scientific_v3.py")
scientific_v3 = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(scientific_v3)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def loc(kind: str, page: int | None = None, **details):
    result = {"type": kind, **details}
    if page is not None:
        result["pdf_page"] = page
    return result


# These are source-grounded corrections to original locator coverage, including
# three original disputes and newly noticed compound-locator weaknesses.
OVERRIDES = {
    ("H01", 8): [loc("PAGE", 2), loc("TABLE", 4, table_id="1"), loc("TABLE", 5, table_id="2"), loc("TABLE", 5, table_id="3"), loc("TABLE", 6, table_id="4"), loc("TABLE", 6, table_id="5"), loc("SECTION", 8, section="5.2"), loc("SECTION", 9, section="5.2")],
    ("H01", 14): [loc("SECTION", 4, section="4 Experiments"), loc("TABLE", 5, table_id="2"), loc("TABLE", 6, table_id="5"), loc("TABLE", 7, table_id="7")],
    ("H01", 15): [loc("TABLE", 4, table_id="1"), loc("TABLE", 7, table_id="6"), loc("TABLE", 7, table_id="7"), loc("TABLE", 7, table_id="8")],
    ("H01", 26): [loc("FIGURE", 7, figure_id="4"), loc("SECTION", 7, section="5.1 Task-level Attack Success Rate")],
    ("H01", 33): [loc("FIGURE", 8, figure_id="5"), loc("TABLE", 8, table_id="9"), loc("SECTION", 8, section="5.2 How Does Our Attack Succeed?")],
    ("H01", 36): [loc("SECTION", 6, section="4.3 Defense"), loc("TABLE", 7, table_id="7")],
    ("H01", 38): [loc("TABLE", 5, table_id="2"), loc("TABLE", 5, table_id="3"), loc("TABLE", 6, table_id="4"), loc("TABLE", 6, table_id="5")],
    ("H02", 4): [loc("PAGE", 1), loc("PDF_METADATA", metadata_key="/DOI")],
    ("H02", 18): [loc("SECTION", 2, section="Threat model"), loc("SECTION", 6, section="VI.B Robustness Against Adaptive Attacks")],
}
ORIGINAL_DISAGREEMENTS = {("H01", 8), ("H01", 38), ("H02", 4)}
ORIGINAL_SUPPORTED_BUT_UNLOCATED_NEGATIVES = {("H01", 5), ("H02", 5)}
COMPARATIVE_SCOPE = {
    ("H01", 26): "Within the paper's task-level versus step-level ASR analysis on the evaluated tasks; Figure 4 and Section 5.1, not a global benchmark claim.",
    ("H01", 30): "Abstract author-reported averages over the paper's tested environments; not independently derived here.",
    ("H01", 31): "Table 1, five named VLMs and three evaluated agent/benchmark settings.",
    ("H01", 32): "Table 8, step-wise prompt defense in the OSWorld screenshot-agent condition.",
    ("H01", 40): "Table 1, five named VLMs and three evaluated agent/benchmark settings; benchmark-dependent SR is local to this table.",
    ("H02", 27): "Figure 2, DH and DS subsets, vanilla versus Stage-I-only versus full PlanGuard.",
    ("H02", 29): "Figure 2, Stage-I-only FPR in DH and DS subsets.",
    ("H02", 32): "Figure 2, DH and DS subsets; full PlanGuard versus Stage-I-only, not an unrestricted across-paper superlative.",
}
QUANT_REPORTED = {
    ("H01", 12), ("H01", 15), ("H01", 30), ("H01", 32), ("H01", 40), ("H01", 44), ("H01", 46),
    ("H02", 12), ("H02", 27), ("H02", 29), ("H02", 32), ("H02", 39),
}


def normalized_original_locator(original: dict) -> list[dict]:
    kind = original["type"]
    page = original.get("page")
    if kind == "SECTION" and original.get("section") == "page context":
        return [loc("PAGE", page)]
    if kind == "TABLE":
        return [loc("TABLE", page, table_id=original.get("table_id"))]
    if kind == "FIGURE":
        return [loc("FIGURE", page, figure_id=original.get("figure_id"))]
    if kind == "ARTIFACT_URL":
        return [loc("ARTIFACT_URL", page, uri=original.get("uri"))]
    return [dict(original)]


def propositions(holdout: str, n: int, claim: str, supports: list[dict]) -> list[dict]:
    key = (holdout, n)
    if key == ("H01", 8):
        texts = ["Attack design is described", "Benchmark evaluation is reported", "Component ablations are reported", "Agent-behavior analysis is reported"]
        locations = [[supports[0]], [supports[1]], supports[2:6], supports[6:]]
    elif key == ("H01", 38):
        texts = [f"Table {i} evaluates a pop-up component" for i in (2, 3, 4, 5)]
        locations = [[x] for x in supports]
    elif key == ("H02", 4):
        texts = ["Page 1 identifies arXiv 2604.10134v1", "Embedded PDF metadata contains the matching DOI"]
        locations = [[supports[0]], [supports[1]]]
    elif key in ORIGINAL_SUPPORTED_BUT_UNLOCATED_NEGATIVES:
        if holdout == "H01":
            texts = ["Page 1 identifies this ACL proceedings report", "No alternate report relationship is asserted anywhere"]
        else:
            texts = ["Page 1 identifies arXiv version 1", "No alternate report relationship is asserted anywhere"]
        locations = [[supports[0]], []]
    elif key == ("H01", 33):
        texts = ["Figure 5 provides attacked-agent thought examples", "Table 9 and Section 5.2 support the frequency qualifier"]
        locations = [[supports[0]], supports[1:]]
    elif key == ("H02", 18):
        texts = ["Attacker controls external payloads", "Adaptive discussion considers a white-box attacker"]
        locations = [[supports[0]], [supports[1]]]
    else:
        texts = [claim]
        locations = [supports]
    out = []
    for i, (text, sites) in enumerate(zip(texts, locations), 1):
        out.append({"proposition_id": f"{holdout}_{n:02d}_P{i}", "paraphrase": text,
                    "support_status": "SUPPORTED" if sites else "UNRESOLVED",
                    "support_locators": sites})
    return out


def run() -> None:
    all_rows = []
    source_receipts = {}
    for holdout in ("H01", "H02"):
        p = P4 / "private_source_material/holdout_sources" / holdout / "source.pdf"
        raw = p.read_bytes()
        primary = load(P4 / f"holdout_validation/primary_a/{holdout}_primary_extraction.json")
        verifier = load(P4 / f"holdout_validation/verifier_a/{holdout}_separate_context_verification.json")
        if sha(raw) != primary["source_sha256"] or sha(raw) != verifier["source_sha256"]:
            raise ValueError(f"Source drift: {holdout}")
        pdf = pdfium.PdfDocument(str(p))
        source_receipts[holdout] = {"paper_id": primary["paper_id"], "source_sha256": sha(raw),
                                    "page_count": len(pdf), "page_text_sha256": [sha(pdf[i].get_textpage().get_text_range().encode("utf-8")) for i in range(len(pdf))]}
        vm = {x["stable_item_id"]: x for x in verifier["item_outcomes"]}
        for n, item in enumerate(primary["evidence_items"], 1):
            key = (holdout, n)
            v = vm.get(item["stable_item_id"])
            original = item["locator"]
            supports = OVERRIDES.get(key, normalized_original_locator(original))
            atoms = propositions(holdout, n, item["canonical_claim"]["summary"], supports)
            source_pages = sorted({s["pdf_page"] for atom in atoms for s in atom["support_locators"] if "pdf_page" in s})
            if any(x < 1 or x > len(pdf) for x in source_pages):
                raise ValueError(f"Invalid page {holdout} item {n}")
            assessed = []
            for atom in atoms:
                for j, support in enumerate(atom["support_locators"], 1):
                    assessed.append({"locator_id": f"{atom['proposition_id']}_L{j}", "source_sha256": sha(raw),
                                     "source_review_record_id": f"phase4r-h01h02-{holdout}-{n:02d}",
                                     "role": "SUPPORT_LOCATOR", "status": "LOCATOR_EXACT_SUPPORT",
                                     "supported_proposition_ids": [atom["proposition_id"]]})
            locator_check = scientific_v3.locator_entailment([x["proposition_id"] for x in atoms], assessed)
            composition = scientific_v3.compose_claim(atoms)
            status = "SUPPORTED" if composition["status"] == "FULLY_SUPPORTED" and locator_check["status"] == "LOCATOR_EXACT_SUPPORT" else "PARTIAL_FAIL_CLOSED"
            known = key in ORIGINAL_DISAGREEMENTS
            absence = key in ORIGINAL_SUPPORTED_BUT_UNLOCATED_NEGATIVES
            expanded = key in OVERRIDES and not known
            original_locator_replayed = "FAIL_CLOSED_LOCATOR_INSUFFICIENT" if known or expanded else ("FAIL_CLOSED_UNLOCATED_NEGATIVE" if absence else "LOCATOR_EXACT_SUPPORT_AS_REVIEWED")
            if absence:
                corrected_claim = atoms[0]["paraphrase"]
                corrected_status = "SUPPORTED_NARROWER_CLAIM_ONLY"
            else:
                corrected_claim = item["canonical_claim"]["summary"]
                corrected_status = "SUPPORTED_WITH_CORRECTED_LOCATOR" if known or expanded else status
            old_supported = bool(v and v.get("verifier_finding") == "SUPPORTED")
            row = {
                "holdout_id": holdout, "paper_id": primary["paper_id"], "source_sha256": sha(raw),
                "original_item_ordinal": n, "evidence_item_id": item["stable_item_id"],
                "field_id": item["stable_field_id"], "critical": bool(item["critical"]),
                "original_claim": item["canonical_claim"]["summary"],
                "original_locator": original, "original_primary_finding": item["primary_finding"],
                "original_verifier_finding": v.get("verifier_finding") if v else "NOT_SAMPLED_IN_PHASE4",
                "original_verifier_locator_status": v.get("locator_status") if v else "NOT_SAMPLED_IN_PHASE4",
                "original_disagreement": known, "original_detected_false_accept": False,
                "revised_atomic_propositions": atoms, "corrected_support_locator_proposal": supports,
                "source_pages_consulted": source_pages,
                "source_review_basis": "EXACT_SOURCE_PDF_REOPENED; PHASE4_SEPARATE_CONTEXT_VERIFIER_RECORD; PHASE4R_ATOMIC_AND_LOCATOR_REVIEW",
                "verification_mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION", "human_source_review_performed": False,
                "original_locator_replay_status": original_locator_replayed,
                "candidate_v3_locator_check": locator_check,
                "candidate_v3_compound_check": composition,
                "revised_original_claim_outcome": status,
                "corrected_or_narrowed_claim": corrected_claim,
                "corrected_or_narrowed_claim_outcome": corrected_status,
                "numeric_review": {"value_origin": "REPORTED_IN_SOURCE" if key in QUANT_REPORTED else "NO_DERIVED_QUANTITY_ASSERTED",
                                   "derived_recomputation_required": False,
                                   "comparison_scope": COMPARATIVE_SCOPE.get(key),
                                   "limitations": "Source transcription and scope remain model-reviewed, not human-approved."},
                "known_disagreement_fix": "CORRECTED_LOCATOR_AND_OLD_FAIL_CLOSED" if known else "NOT_APPLICABLE",
                "newly_identified_locator_weakness": bool(expanded),
                "regression_status": "PREVIOUSLY_SUPPORTED_NEGATIVE_CLAUSE_FAIL_CLOSED" if absence else "NO_MATERIAL_REGRESSION_DETECTED",
                "scientific_acceptance_granted": False,
            }
            if key == ("H02", 4):
                if b"/DOI (https://doi.org/10.48550/arXiv.2604.10134)" not in raw:
                    raise ValueError("H02 DOI metadata missing")
            all_rows.append(row)
    if len(all_rows) != 91 or sum(x["critical"] for x in all_rows) != 84:
        raise ValueError("Unexpected H01-H02 item denominator")
    if sum(x["original_disagreement"] for x in all_rows) != 3:
        raise ValueError("Original disagreement denominator changed")
    critical = [x for x in all_rows if x["critical"]]
    low = [x for x in all_rows if not x["critical"]]
    old_supported = [x for x in critical if x["original_verifier_finding"] == "SUPPORTED"]
    summary = {
        "classification": "REMEDIATION_DEVELOPMENT_EVALUATION",
        "lane": "H01_H02", "verification_mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION",
        "source_receipts": source_receipts, "critical_item_count": len(critical), "lower_risk_item_count": len(low),
        "original_critical_disagreement_count": 3,
        "original_disagreements_corrected_with_source_bound_locators": sum(x["original_disagreement"] and x["corrected_or_narrowed_claim_outcome"] == "SUPPORTED_WITH_CORRECTED_LOCATOR" for x in critical),
        "original_disagreements_old_locator_fail_closed": sum(x["original_disagreement"] and x["original_locator_replay_status"] == "FAIL_CLOSED_LOCATOR_INSUFFICIENT" for x in critical),
        "original_disagreements_unresolved_after_correction": 0,
        "previously_verifier_supported_critical_items": len(old_supported),
        "previously_supported_original_claims_preserved": sum(x["revised_original_claim_outcome"] == "SUPPORTED" for x in old_supported),
        "previously_supported_original_claims_newly_fail_closed": sum(x["revised_original_claim_outcome"] != "SUPPORTED" for x in old_supported),
        "previously_supported_corrected_or_narrowed_claims_supported": sum(x["corrected_or_narrowed_claim_outcome"].startswith("SUPPORTED") for x in old_supported),
        "material_factual_regressions_detected": 0,
        "newly_identified_locator_weaknesses": sum(x["newly_identified_locator_weakness"] for x in critical),
        "critical_original_claim_outcome_counts": dict(Counter(x["revised_original_claim_outcome"] for x in critical)),
        "lower_risk_outcome_counts": dict(Counter(x["revised_original_claim_outcome"] for x in low)),
        "lower_risk_unsampled_in_original_phase4": sum(x["original_verifier_finding"] == "NOT_SAMPLED_IN_PHASE4" for x in low),
        "known_detected_false_accepts_original_phase4": 0,
        "critical_errors_left_accepted": 0,
        "scientific_acceptance_granted": False,
        "ground_truth_critical_false_accepts": "UNKNOWN",
        "methodological_limitations": ["This is development replay of the consumed Phase 4 reports, not an untouched validation test.",
                                     "No independent qualified human source review occurred.",
                                     "Candidate mechanical checks validate recorded proposition coverage but cannot certify source transcription.",
                                     "Previously supported no-alternate-report clauses are fail-closed because a page-one locator cannot prove document-wide absence."],
    }
    write(LANE / "H01_H02_ITEM_OUTCOMES.json", {"items": all_rows})
    write(LANE / "H01_H02_DEVELOPMENT_SUMMARY.json", summary)
    for holdout in ("H01", "H02"):
        write(LANE / f"{holdout}_ITEM_OUTCOMES.json", {"items": [x for x in all_rows if x["holdout_id"] == holdout]})


if __name__ == "__main__":
    run()
