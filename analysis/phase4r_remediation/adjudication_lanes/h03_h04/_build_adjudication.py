"""Reconstruct H03/H04 disagreement records from immutable Phase 4 inputs.

Private excerpts are derived from the exact Phase 4 source-PDF text extraction and
kept in this lane's private directory. The public JSON contains only short
paraphrases, page references and hashes of the private evidence files.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
P4 = ROOT / "analysis/phase4_rehearsal"
OUT = Path(__file__).resolve().parent
PRIVATE = OUT / "private_source_evidence"
PRIVATE.mkdir(parents=True, exist_ok=True)

FILES = {
    "H03": (
        P4 / "holdout_validation/primary_a/H03_primary_extraction.json",
        P4 / "holdout_validation/verifier_a/H03_separate_context_verification.json",
        "item_outcomes",
        P4 / "private_source_material/primary_a/H03/pages",
    ),
    "H04": (
        P4 / "holdout_validation/primary_b/H04_report_5b76dc0b8a92199dbda22672.json",
        P4 / "holdout_validation/verifier_b/H04_verification.json",
        "verified_evidence_items",
        P4 / "private_source_material/primary_b/H04",
    ),
}

# Outcome, root cause, severity, corrected page set, source anchors,
# sanitized adjudication, generalized fix. Anchors are extracted verbatim from
# prior exact-source PDF extraction, never from verifier commentary.
SPEC = {
    ("H03", "methods.metrics"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [4, 5],
        [(4, "exact_match:"), (4, "eval_vqa:"), (5, "eval_fuzzy_image_match:"), (5, "webpage state")],
        "Four evaluator families are source-supported, but PAGE 4 alone omits state and image similarity; pages 4-5 are needed.",
        "Split evaluator primitives into atomic claims or use a source-bound compound locator covering each primitive.",
    ),
    ("H03", "results.quantitative"): (
        "VERIFIER_CORRECT", "GLOBAL_RESULT_RECONCILIATION_FAILURE", "CRITICAL", [8, 13],
        [(8, "GPT-4V 9.83% 17.14% 19.31% 16.37%"), (8, "Human Performance - - Webpage"),
         (13, "GPT-4o Image + Caps + SoM"), (13, "outperforms GPT-4V (16.37%)")],
        "16.37% is the GPT-4V+SoM main-baseline value and 88.70% the human comparator. Appendix Table 5 reports GPT-4o at 19.78%; unqualified 'best-agent' is false.",
        "Require document-wide comparative reconciliation and explicit comparison-set/section scope before any superlative or overall claim.",
    ),
    ("H03", "results.ablations"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "MODERATE", [8, 9, 13, 14],
        [(8, "SoM Improves Navigability"), (9, "Task Subset"), (13, "C Further Analysis"), (14, "Figure 6:")],
        "Representation and subset analyses are present, but the appendix-start locator alone does not substantiate their full spread across main results and appendix.",
        "Represent each comparison separately or require an enumerated multi-location evidence set.",
    ),
    ("H04", "identity.year_version"): (
        "LOCATOR_ONLY_DEFECT", "LOCATOR_WRONG_PAGE", "HIGH", [1],
        [(1, "August 12–14, 2026"), (1, "35th USENIX Security Symposium")],
        "The proceedings year is on the PDF cover at page 1; the primary page-2 locator does not establish it.",
        "Bind bibliographic year to the exact dated front-matter page, not a nearby title page or footer.",
    ),
    ("H04", "methods.benchmark"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [11, 13],
        [(11, "final dataset comprises 20 open-source"), (13, "absence of a public benchmark"),
         (13, "38 verified vulnerabilities")],
        "The 20-agent target set is described on page 11; the constructed 38-vulnerability comparison benchmark and lack of a public benchmark are on page 13.",
        "Separate target-set and comparison-benchmark propositions with independent locators and a benchmark-provenance field.",
    ),
    ("H04", "methods.experiment_design"): (
        "LOCATOR_ONLY_DEFECT", "COMPOUND_CLAIM_OVERREACH", "HIGH", [11, 12, 13],
        [(11, "randomly sampled 5%"), (12, "20-minute"), (12, "skip"),
         (13, "three variants")],
        "The design elements are supported across pages 11-13, while the single page-11 locator substantiates only the lifecycle sampling portion.",
        "Break multi-stage experimental designs into separately located lifecycle, fuzzing-limit, comparison and ablation records.",
    ),
    ("H04", "methods.baselines"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [12, 13],
        [(12, "AgentFuzz locates sink"), (13, "three variants"), (13, "w/o Generation")],
        "The AgentFuzz comparison is on page 12; ablation variants are specified on page 13.",
        "Use separate baseline and ablation entities with exact source locators.",
    ),
    ("H04", "methods.metrics"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [11, 12, 13],
        [(11, "identification accuracy was 95.2%"), (12, "119.08 CPU hours"),
         (12, "Recall(%)"), (13, "Result of ablation study")],
        "Lifecycle accuracy, resource cost, precision/recall and ablation metrics are located across pages 11-13, beyond the primary page-11 locator.",
        "Create atomic metric definitions and make each metric require its own table/section locator.",
    ),
    ("H04", "results.quantitative"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [3, 11, 12, 15],
        [(3, "95.2%"), (11, "identification accuracy was 95.2%"),
         (12, "AgentDoS 36 0 2 100% 94.7%"), (12, "15 CVE identifiers"),
         (15, "affecting 16 applications")],
        "The figures are supported, but Table 3 alone contains only the 36, 100% and 94.7% comparison figures; other quantities occur in separate sections.",
        "Store each numeric finding as a scoped, provenance-bound value and reject a compound locator that omits any component.",
    ),
    ("H04", "results.negative"): (
        "VERIFIER_CORRECT", "NEGATIVE_RESULT_COUNT_ERROR", "CRITICAL", [11, 15],
        [(11, "Quivr 38.1k 6.1k 0 / 0"), (11, "Owl 17.2k 15.2k 0 / 0"),
         (11, "Bisheng 9.0k 144.3k 0 / 0"), (11, "Taskweaver 5.8k 16.4k 0 / 0"),
         (15, "requires source")],
        "Table 2 has four zero-vulnerability agents (Quivr, Owl, Bisheng, Taskweaver), not three. The black-box/source-access limitation is supported separately on page 15.",
        "Parse the complete table into rows, independently count all zero rows, reconcile against the stated 16/20 affected total, and split unrelated negative findings.",
    ),
    ("H04", "results.comparative"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [12, 13],
        [(12, "AgentFuzz 3 0 35 100% 7.9%"), (12, "AgentDoS 36 0 2 100% 94.7%"),
         (13, "all of"), (13, "False Negatives in AgentFuzz")],
        "Table 3 gives the 36-versus-3 result; page 13 states the subset relationship and explains the two classes of misses.",
        "Require explicit comparison scope and locate count, set-inclusion and causal-explanation propositions independently.",
    ),
    ("H04", "validity.assumptions"): (
        "BOTH_PARTIAL", "QUALIFIER_OMISSION", "HIGH", [7, 11, 12, 15],
        [(7, "Python’s built-in containers"), (11, "manually identified the APIs"),
         (12, "resource usage remains"), (15, "requires source")],
        "Source access and manually identified entry points are explicit. Python scope and observable resource feedback follow the design, but should be labeled analyst-derived conditions, not unqualified author-stated assumptions.",
        "Represent explicit author assumptions separately from analyst-derived operating conditions, each with supporting locations and inference labels.",
    ),
    ("H04", "validity.limitations"): (
        "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "HIGH", [7, 11, 15],
        [(7, "difficulty of resolving im-"), (11, "unresolved indi-"),
         (15, "requires source")],
        "The black-box/source-code limitation is explicit on page 15; indirect-call/static-analysis limitations are discussed on pages 7 and 11.",
        "Split multiple limitations into atomic records with their own source location and scope.",
    ),
    ("H04", "validity.threats"): (
        "BOTH_PARTIAL", "COMPOUND_CLAIM_OVERREACH", "HIGH", [7, 11, 12],
        [(7, "difficulty of resolving"), (11, "manually identified the APIs"),
         (11, "minimum required"), (12, "20-minute")],
        "The factors are source-supported design choices, but their effect on generalization is an analyst inference, and the page-11 locator does not cover all components.",
        "Separate observed design facts from inferred validity threats; require explicit inference status and individually supported premises.",
    ),
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


rows = list(csv.DictReader((P4 / "HOLDOUT_DISAGREEMENTS.csv").open(encoding="utf-8-sig", newline="")))
rows = [r for r in rows if r["holdout_id"] in FILES]
assert len(rows) == 14, len(rows)
public = []
for row in rows:
    holdout = row["holdout_id"]
    field = row["stable_field_id"]
    spec = SPEC[(holdout, field)]
    primary_path, verifier_path, verifier_key, pages_dir = FILES[holdout]
    primary = json.loads(primary_path.read_text(encoding="utf-8"))
    verifier = json.loads(verifier_path.read_text(encoding="utf-8"))
    item_id = row["stable_item_id"]
    item = next(x for x in primary["evidence_items"] if x["stable_item_id"] == item_id)
    vitem = next(x for x in verifier[verifier_key] if x["stable_item_id"] == item_id)
    evidence = []
    for page, anchor in spec[4]:
        page_path = pages_dir / f"page_{page:03d}.txt"
        page_text = page_path.read_text(encoding="utf-8", errors="replace")
        idx = page_text.casefold().find(anchor.casefold())
        if idx < 0:
            raise ValueError((holdout, field, page, anchor))
        line_start = page_text.rfind("\n", 0, idx) + 1
        line_end = page_text.find("\n", idx)
        if line_end < 0:
            line_end = len(page_text)
        previous_start = page_text.rfind("\n", 0, max(0, line_start - 1)) + 1
        following_end = page_text.find("\n", line_end + 1)
        if following_end < 0:
            following_end = len(page_text)
        exact_excerpt = page_text[previous_start:following_end]
        evidence.append({
            "pdf_page": page,
            "exact_extracted_excerpt": exact_excerpt,
            "page_text_sha256": sha(page_path.read_bytes()),
            "source_rendering_inspected": (holdout, page) in {
                ("H03", 8), ("H03", 13), ("H04", 11), ("H04", 12), ("H04", 13)
            },
        })
    evidence_obj = {
        "disagreement_id": f"{holdout}:{item_id}",
        "source_sha256": primary["source_sha256"],
        "exact_source_evidence": evidence,
        "source_pdf": f"analysis/phase4_rehearsal/private_source_material/holdout_sources/{holdout}/source.pdf",
    }
    private_path = PRIVATE / f"{holdout}_{field.replace('.', '_')}_{item_id[3:11]}.json"
    private_bytes = (json.dumps(evidence_obj, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    private_path.write_bytes(private_bytes)
    primary_value = item.get("canonical_claim", {}).get("summary") if holdout == "H03" else item["statement"]
    verifier_value = vitem.get("source_note") if holdout == "H03" else vitem.get("note")
    public.append({
        "disagreement_id": f"{holdout}:{item_id}",
        "holdout_id": holdout,
        "paper_id": primary["paper_id"],
        "source_sha256": primary["source_sha256"],
        "field_id": field,
        "evidence_item_id": item_id,
        "claim_type": item.get("canonical_claim", {}).get("claim_type", "ANALYST_SYNTHESIS" if field.startswith("validity.") else "AUTHOR_REPORTED"),
        "primary_value": primary_value,
        "verifier_value": verifier_value,
        "primary_locator": item["locator"],
        "verifier_locator": {"source_sha256": primary["source_sha256"], "pdf_pages_reopened": vitem.get("source_pages_reopened") or [vitem.get("source_pdf_page_reopened")]},
        "exact_source_evidence": {"private_path": str(private_path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha(private_bytes), "pdf_pages": spec[3]},
        "adjudicated_outcome": spec[0],
        "adjudicated_value": spec[5],
        "root_cause_code": spec[1],
        "severity": spec[2],
        "criticality": "CRITICAL_EVIDENCE_ITEM",
        "workflow_component_responsible": ["PRIMARY_EXTRACTION", "LOCATOR_VALIDATION", "VERIFICATION_GATE"] if spec[0] != "VERIFIER_CORRECT" else ["PRIMARY_EXTRACTION", "CROSS_DOCUMENT_RECONCILIATION" if holdout == "H03" else "TABLE_AGGREGATION", "VERIFICATION_GATE"],
        "candidate_generalized_fix": spec[6],
        "phase4_original_error_codes": row["error_codes"].split(";"),
        "adjudication_basis": "EXACT_SOURCE_PDF_TEXT_AND_RENDERED_PAGE_WHERE_TABLE_OR_LAYOUT_MATTERS",
        "scientific_acceptance": "NOT_GRANTED",
    })

assert len(public) == 14
assert len({x["evidence_item_id"] for x in public}) == 14
output = {
    "schema_version": "phase4r-adjudication-v1",
    "scope": "H03_H04_ORIGINAL_PHASE4_CRITICAL_DISAGREEMENTS",
    "record_count": len(public),
    "source_of_original_disagreements": "analysis/phase4_rehearsal/HOLDOUT_DISAGREEMENTS.csv",
    "private_evidence_root": "analysis/phase4r_remediation/adjudication_lanes/h03_h04/private_source_evidence",
    "records": public,
}
(OUT / "ADJUDICATION_H03_H04.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {len(public)} records and {len(list(PRIVATE.glob('*.json')))} private evidence files")
