"""Source-adjudicate the Phase 4 H05/H06 critical disagreements.

Only Phase 4R lane outputs are written. Source PDFs and Phase 4 records are read-only.
Verbatim source excerpts stay in the lane's private directory.
"""

from __future__ import annotations

import hashlib
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, "analysis/phase3_calibration/_deps")
logging.getLogger("pypdf").setLevel(logging.ERROR)
from pypdf import PdfReader  # type: ignore

ROOT = Path("analysis/phase4r_remediation/adjudication_lanes/h05_h06")
PHASE4 = Path("analysis/phase4_rehearsal")
SRC = PHASE4 / "private_source_material/holdout_sources"
RECORDS = PHASE4 / "holdout_validation"
PRIVATE = ROOT / "private/source_excerpts"

# The entries are PDF page numbers and search anchors in the exact PDF text.
# An anchor is used only to select a verbatim excerpt; it is never evidence
# that a page supports an assertion without the source review recorded below.
EVIDENCE = {
    "H05": {
        "methods.agent_architecture": [(3, "Selenium"), (4, "auxiliary text"), (4, "action space")],
        "methods.environment": [(3, "Selenium"), (4, "CAPTCHA"), (5, "1024")],
        "methods.experiment_design": [(6, "human evaluation"), (8, "300"), (9, "Failure Ratio")],
        "methods.baselines": [(5, "GPT-4"), (6, "SeeAct"), (7, "Claude-3-Opus")],
        "methods.metrics": [(6, "Kappa"), (7, "standard deviation"), (9, "Failure Ratio")],
        "results.negative": [(6, "text-heavy"), (9, "Failure Ratio")],
        "results.uncertainty_statistics": [(6, "Fleiss"), (7, "standard deviation")],
        "results.comparative": [(6, "30%"), (7, "Table 1"), (7, "Table 3")],
        "validity.assumptions": [(4, "CAPTCHA"), (5, "Possible"), (6, "human evaluation")],
        "validity.limitations": [(9, "Drag"), (10, "file formats"), (10, "potential risks")],
        "validity.threats": [(3, "constant updates"), (5, "15 steps"), (6, "GPT-4V"), (8, "bias")],
        "reproducibility.environment": [(3, "Selenium"), (5, "1024"), (5, "15 steps")],
    },
    "H06": {
        "framing.claimed_contributions": [(3, "open problem"), (4, "DRUM"), (4, "STAR"), (4, "BEAST")],
        "methods.system_model": [(3, "single"), (4, "DRUM"), (4, "STAR"), (22, "Rate Limiting")],
        "methods.benchmark": [(4, "crawl"), (14, "Table III"), (26, "EXPERIMENTS")],
        "methods.experiment_design": [(4, "model"), (14, "Table III"), (16, "LRU Hit Rates"), (26, "EXPERIMENTS")],
        "methods.baselines": [(5, "RELATED WORK"), (14, "Mercator-B"), (16, "LRU Hit Rates"), (17, "Balanced tree"), (24, "naive version")],
        "methods.metrics": [(14, "Overhead"), (16, "LRU Hit Rates"), (26, "download rate"), (27, "394,619"), (30, "collision")],
        "security.resource_consumption": [(3, "RAM"), (4, "STAR"), (22, "Rate Limiting"), (26, "16GB RAM")],
        "results.quantitative": [(26, "41.27"), (26, "319"), (27, "394,619")],
        "results.qualitative": [(1, "bottlenecks"), (27, "394,619"), (32, "CONCLUSION")],
        "results.negative": [(27, "mystery"), (30, "does not perform")],
        "results.comparative": [(4, "thousands of times"), (5, "RELATED WORK"), (14, "Mercator-B"), (26, "1,789")],
        "validity.assumptions": [(14, "R = 1GB"), (26, "quad-CPU"), (31, "uniformly random")],
        "validity.limitations": [(29, "duplicate"), (30, "collisions"), (31, "Disk Sort"), (32, "Robot Expiration")],
        "validity.threats": [(3, "spam sites"), (4, "bottleneck"), (26, "bandwidth"), (27, "mystery"), (30, "duplicate")],
    },
}

SPECIAL = {
    ("H05", "methods.experiment_design"): (
        "BOTH_PARTIAL", "SAMPLE_DENOMINATOR_SCOPE_ERROR", "HIGH",
        "The source says 300 tasks were sampled and failed cases within that sample were categorized. The primary claim says 300 failures, and the verifier flagged only the locator, missing this count/scope error.",
        "Represent sample size, subset-selection rule, failed-item count, and analysis denominator separately; verify each number's noun and condition against the source.",
    ),
    ("H05", "validity.threats"): (
        "BOTH_PARTIAL", "COMPOUND_CLAIM_OVERREACH", "HIGH",
        "This is a multi-source analyst synthesis, not one enumerated author claim. Some factors are source-grounded, but the original page alone cannot support the whole causal/generalizability inference.",
        "Split source observations from analyst inference; require provenance and a locator for each premise plus an inference label.",
    ),
    ("H06", "results.qualitative"): (
        "VERIFIER_CORRECT", "LOCATOR_POINTS_TO_CONTEXT_NOT_SUPPORT", "HIGH",
        "PDF page 27 reports crawl measurements and URL statistics. The broad no-bottlenecks claim is in the abstract (page 1) and conclusion (page 32); the original locator cannot verify it.",
        "Reject support when a locator points only to context; require proposition-level source entailment and exact supporting page(s).",
    ),
    ("H06", "validity.threats"): (
        "BOTH_PARTIAL", "COMPOUND_CLAIM_OVERREACH", "HIGH",
        "The list mixes observed operating conditions and analyst inferences about generalization. The single cited page is insufficient for the full claim.",
        "Represent each limitation premise separately, label synthesis/inference, and require complete premise locators.",
    ),
}

# Pages actually visually inspected by the adjudicator, not merely rendered.
LAYOUT_PAGES = {"H05": {7, 9}, "H06": {14, 26, 27}}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snippet(page_text: str, anchor: str, *, before: int = 200, after: int = 900) -> str:
    i = page_text.casefold().find(anchor.casefold())
    if i < 0:
        raise ValueError(f"Anchor missing: {anchor!r}")
    return page_text[max(0, i - before) : min(len(page_text), i + len(anchor) + after)].strip()


def build() -> None:
    PRIVATE.mkdir(parents=True, exist_ok=True)
    outputs = []
    for holdout_id in ("H05", "H06"):
        pdf = SRC / holdout_id / "source.pdf"
        verifier_path = RECORDS / "verifier_b" / f"{holdout_id}_verification.json"
        primary_path = next((RECORDS / "primary_b").glob(f"{holdout_id}_report_*.json"))
        verifier = json.loads(verifier_path.read_text(encoding="utf-8"))
        primary = json.loads(primary_path.read_text(encoding="utf-8"))
        assert sha(pdf) == verifier["source_sha256"] == primary["source_sha256"]
        assert sha(primary_path) == verifier["primary_record_sha256"]
        source = PdfReader(pdf)
        primary_items = {x["stable_item_id"]: x for x in primary["evidence_items"]}
        disagreements = set(verifier["critical_disagreement_item_ids"])
        selected = [x for x in verifier["verified_evidence_items"] if x["stable_item_id"] in disagreements]
        assert len(selected) == len(disagreements) == len(EVIDENCE[holdout_id])
        assert {x["stable_field_id"] for x in selected} == set(EVIDENCE[holdout_id])
        for idx, verified in enumerate(selected, 1):
            field = verified["stable_field_id"]
            item = primary_items[verified["stable_item_id"]]
            disagreement_id = f"D-{holdout_id}-{idx:03d}"
            source_sections = []
            page_numbers = []
            for page, anchor in EVIDENCE[holdout_id][field]:
                page_text = source.pages[page - 1].extract_text()
                source_sections.append(f"PDF PAGE {page}; ANCHOR {anchor!r}\n{snippet(page_text, anchor)}")
                page_numbers.append(page)
            excerpt_path = PRIVATE / f"{disagreement_id}.txt"
            excerpt_path.write_text("\n\n---\n\n".join(source_sections) + "\n", encoding="utf-8")
            if (holdout_id, field) in SPECIAL:
                outcome, cause, severity, rationale, fix = SPECIAL[(holdout_id, field)]
            else:
                outcome, cause, severity = "LOCATOR_ONLY_DEFECT", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "MODERATE"
                rationale = (
                    "Source passages on the listed pages support the components of the primary statement, "
                    "but its one-page or one-table locator covers only part of the compound claim. "
                    "The verifier's partial-support finding is correct for the submitted evidence/locator pair."
                )
                fix = (
                    "Decompose compound claims into atomic propositions; require each proposition's "
                    "typed locator to entail that proposition before aggregating the field."
                )
            if not verified["critical"] or item["critical"] is not True:
                raise AssertionError("Non-critical disagreement selected")
            outputs.append({
                "disagreement_id": disagreement_id,
                "holdout_id": holdout_id,
                "paper_id": primary["paper_id"],
                "source_sha256": primary["source_sha256"],
                "field_id": field,
                "evidence_item_id": verified["stable_item_id"],
                "claim_type": "ANALYST_SYNTHESIS" if field == "validity.threats" else "COMPOUND_FIELD_CLAIM",
                "primary_value": item["statement"],
                "verifier_value": {"finding": verified["verifier_finding"], "note": verified["note"]},
                "primary_locator": item["locator"],
                "verifier_locator": {"status": "SOURCE_PAGES_REOPENED_BY_PHASE4_VERIFIER", "pages": verified["source_pages_reopened"]},
                "exact_source_evidence": {
                    "classification": "PRIVATE_SOURCE_EXCERPT_NEVER_PACKAGE",
                    "private_path": str(excerpt_path).replace("\\", "/"),
                    "sha256": sha(excerpt_path),
                    "pdf_pages": sorted(set(page_numbers)),
                    "rendered_pages_visually_inspected": sorted(set(page_numbers) & LAYOUT_PAGES[holdout_id]),
                    "source_pdf_sha256": sha(pdf),
                },
                "adjudicated_outcome": outcome,
                "root_cause_code": cause,
                "contributing_root_cause_codes": (
                    ["LOCATOR_INSUFFICIENT_EVIDENCE", "VERIFICATION_PROTOCOL_FAILURE"]
                    if (holdout_id, field) == ("H05", "methods.experiment_design") else
                    ["LOCATOR_INSUFFICIENT_EVIDENCE", "SCHEMA_EXPRESSIVENESS_FAILURE"]
                    if field == "validity.threats" else
                    ["LOCATOR_INSUFFICIENT_EVIDENCE"]
                    if outcome == "LOCATOR_ONLY_DEFECT" else
                    ["COMPOUND_CLAIM_OVERREACH"]
                ),
                "severity": severity,
                "criticality": "CRITICAL",
                "workflow_component_responsible": (
                    "QUANTITATIVE_DENOMINATOR_AND_LOCATOR_VERIFICATION"
                    if (holdout_id, field) == ("H05", "methods.experiment_design") else
                    "CLAIM_DECOMPOSITION_AND_LOCATOR_VALIDATION"
                    if outcome == "LOCATOR_ONLY_DEFECT" else
                    "SCIENTIFIC_INFERENCE_REPRESENTATION_AND_LOCATOR_VALIDATION"
                    if field == "validity.threats" else
                    "LOCATOR_ENTAILMENT_VERIFICATION"
                ),
                "candidate_generalized_fix": fix,
                "adjudication_rationale": rationale,
                "phase4_primary_record_sha256": sha(primary_path),
                "phase4_verifier_record_sha256": sha(verifier_path),
                "phase4_verification_mode": verifier["verification_mode"],
                "human_source_review_performed": False,
                "ground_truth_critical_false_accepts": "UNKNOWN",
            })
    out = ROOT / "H05_H06_DISAGREEMENT_ADJUDICATION.json"
    out.write_text(json.dumps({
        "schema_version": "phase4r-source-adjudication-v1",
        "scope": "H05_H06_ONLY",
        "record_count": len(outputs),
        "records": outputs,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for x in outputs:
        key = (x["holdout_id"], x["adjudicated_outcome"])
        counts[key] = counts.get(key, 0) + 1
    print(out)
    print("counts", counts)


if __name__ == "__main__":
    build()
