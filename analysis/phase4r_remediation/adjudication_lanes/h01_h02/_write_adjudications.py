"""Reproduce H01-H02 source adjudications from immutable Phase 4 PDFs.

The private evidence files contain PDF-extracted source text and are NEVER_PACKAGE.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "analysis/phase3_calibration/_deps"))
import pypdfium2 as pdfium  # noqa: E402

LANE = Path(__file__).resolve().parent
PHASE4 = REPO / "analysis/phase4_rehearsal"
PRIVATE = LANE / "private_source_material"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save_json(path: Path, data: dict) -> str:
    raw = (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    path.write_bytes(raw)
    return digest(raw)


def source_evidence(holdout: str, pages: list[int], render_refs: dict[int, str]) -> tuple[str, str]:
    pdf_path = PHASE4 / "private_source_material/holdout_sources" / holdout / "source.pdf"
    pdf_hash = digest(pdf_path.read_bytes())
    pdf = pdfium.PdfDocument(str(pdf_path))
    evidence: dict = {
        "classification": "PRIVATE_SOURCE_EVIDENCE_NEVER_PACKAGE",
        "holdout_id": holdout,
        "source_pdf": pdf_path.relative_to(REPO).as_posix(),
        "source_sha256": pdf_hash,
        "pdf_page_count": len(pdf),
        "pages": [],
    }
    for page in pages:
        text = pdf[page - 1].get_textpage().get_text_range()
        page_entry = {
            "pdf_page": page,
            "exact_pdf_extracted_text": text,
        }
        if page in render_refs:
            render_path = PHASE4 / render_refs[page]
            page_entry["rendered_page_reference"] = render_path.relative_to(REPO).as_posix()
            page_entry["rendered_page_sha256"] = digest(render_path.read_bytes())
        evidence["pages"].append(page_entry)
    if holdout == "H02":
        b = pdf_path.read_bytes()
        start = b.find(b"/DOI (")
        if start < 0:
            raise ValueError("H02 PDF has no embedded DOI metadata")
        end = b.find(b")", start)
        evidence["exact_pdf_metadata_entry_ascii"] = b[start : end + 1].decode("ascii")
        evidence["metadata_byte_offset"] = start
    path = PRIVATE / f"{holdout}_{'_'.join(map(str, pages))}_source_evidence.json"
    evidence_hash = save_json(path, evidence)
    return path.relative_to(REPO / "analysis/phase4r_remediation").as_posix(), evidence_hash


def main() -> None:
    h01_src = "24e0d5a90275064313ffe5d791e3c5a46f694716b8c803d02afab118a73efd74"
    h02_src = "eb6b5ebaed769c95ec05de10b08c4feae53fd00ba028e737241a1aa7909023c3"
    h01_e1 = source_evidence("H01", [2, 8, 9], {
        8: "private_source_material/verifier_a/H01_page008.png",
        9: "private_source_material/verifier_a/H01_page009.png",
    })
    h01_e2 = source_evidence("H01", [5, 6], {
        5: "private_source_material/primary_a/H01/rendered/page_005.png",
        6: "private_source_material/primary_a/H01/rendered/page_006.png",
    })
    h02_e = source_evidence("H02", [1], {
        1: "private_source_material/primary_a/H02/rendered/page_001.png",
    })
    records = [
        {
            "disagreement_id": "H01:ei_ead0495e419b2a34b07f1a88e3cc6939dc7b88a3a488aa9714680f473c00f9ec",
            "holdout_id": "H01",
            "paper_id": "report_930591b4e381bdca32354589",
            "source_sha256": h01_src,
            "field_id": "framing.claimed_contributions",
            "evidence_item_id": "ei_ead0495e419b2a34b07f1a88e3cc6939dc7b88a3a488aa9714680f473c00f9ec",
            "claim_type": "AUTHOR_REPORTED",
            "primary_value": "Paper contributes the attack design, benchmark evaluation, component ablations, and behavioral analysis.",
            "verifier_value": "Underlying contribution claim is supported across the paper, but the single page-2 locator omits behavioral analysis on pages 8-9.",
            "primary_locator": {"type": "SECTION", "page": 2, "section": "page context"},
            "verifier_locator": {"type": "COMPOUND_SUPPORT", "pdf_pages": [2, 5, 6, 8, 9], "behavioral_analysis": "Section 5.2, pages 8-9"},
            "exact_source_evidence": {"private_path": h01_e1[0], "sha256": h01_e1[1], "never_package": True},
            "sanitized_source_finding": "Page 2 supports the attack design and summarizes evaluation and ablations; behavioral analysis is documented in Section 5.2 on pages 8-9. The page-2 locator alone does not entail all four propositions.",
            "adjudicated_outcome": "LOCATOR_ONLY_DEFECT",
            "root_cause_code": "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR",
            "secondary_root_cause_codes": ["LOCATOR_INSUFFICIENT_EVIDENCE", "COMPOUND_CLAIM_OVERREACH"],
            "severity": "HIGH",
            "criticality": True,
            "workflow_component_responsible": ["primary_evidence_locator_assignment", "compound_claim_evidence_model"],
            "candidate_generalized_fix": "Decompose contribution lists into atomic propositions; require each material proposition to carry one or more support locators; verify locator entailment clause by clause before composing the field value.",
            "original_phase4_status": "EXCLUDED_FROM_SUPPORTED; SOURCE_REVIEW_PENDING",
            "original_false_accept_detected": False,
            "scientific_acceptance_granted": False,
        },
        {
            "disagreement_id": "H01:ei_3d2357ffd051c58c274664709b2574b5fd0bd1b2638d180b022f33fe4277feb5",
            "holdout_id": "H01",
            "paper_id": "report_930591b4e381bdca32354589",
            "source_sha256": h01_src,
            "field_id": "results.ablations",
            "evidence_item_id": "ei_3d2357ffd051c58c274664709b2574b5fd0bd1b2638d180b022f33fe4277feb5",
            "claim_type": "AUTHOR_REPORTED",
            "primary_value": "Tables 2-5 isolate pop-up components.",
            "verifier_value": "Tables 2-3 are on PDF page 5; Tables 4-5 are on PDF page 6. A single-page table locator covers only half of the cited tables.",
            "primary_locator": {"type": "TABLE", "page": 5, "table_id": "Tables 2-5"},
            "verifier_locator": {"type": "COMPOUND_SUPPORT", "tables": [{"table_id": "2", "pdf_page": 5}, {"table_id": "3", "pdf_page": 5}, {"table_id": "4", "pdf_page": 6}, {"table_id": "5", "pdf_page": 6}]},
            "exact_source_evidence": {"private_path": h01_e2[0], "sha256": h01_e2[1], "never_package": True},
            "sanitized_source_finding": "Rendered PDF pages confirm Tables 2 and 3 on page 5 and Tables 4 and 5 on page 6; each addresses a different pop-up component. The original compound table locator names all four but binds only page 5.",
            "adjudicated_outcome": "LOCATOR_ONLY_DEFECT",
            "root_cause_code": "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR",
            "secondary_root_cause_codes": ["LOCATOR_INSUFFICIENT_EVIDENCE"],
            "severity": "HIGH",
            "criticality": True,
            "workflow_component_responsible": ["primary_evidence_locator_assignment", "table_evidence_model"],
            "candidate_generalized_fix": "Represent each cited table as a typed table locator with its own page and table ID; allow a compound support set for claims spanning tables or pages; reject a multi-table label bound to one page without complete support.",
            "original_phase4_status": "EXCLUDED_FROM_SUPPORTED; SOURCE_REVIEW_PENDING",
            "original_false_accept_detected": False,
            "scientific_acceptance_granted": False,
        },
        {
            "disagreement_id": "H02:ei_773cbff38764774ee4ec846e96dc9023237a25991ba32b0d840472b63eca8e77",
            "holdout_id": "H02",
            "paper_id": "report_c73e0d842744a9a2abde5d88",
            "source_sha256": h02_src,
            "field_id": "identity.identifiers",
            "evidence_item_id": "ei_773cbff38764774ee4ec846e96dc9023237a25991ba32b0d840472b63eca8e77",
            "claim_type": "AUTHOR_REPORTED",
            "primary_value": "The PDF metadata and page identify arXiv 2604.10134v1; metadata supplies its arXiv DOI.",
            "verifier_value": "The arXiv identifier/version appear on page 1, while the DOI is in embedded PDF metadata, not page content.",
            "primary_locator": {"type": "SECTION", "page": 1, "section": "page context"},
            "verifier_locator": {"type": "COMPOUND_SUPPORT", "components": [{"type": "PAGE", "page": 1}, {"type": "PDF_METADATA", "key": "/DOI"}]},
            "exact_source_evidence": {"private_path": h02_e[0], "sha256": h02_e[1], "never_package": True},
            "sanitized_source_finding": "Page 1 prints the arXiv identifier and version. The source PDF's embedded /DOI metadata entry supplies the DOI. A page-one section locator does not locate metadata.",
            "adjudicated_outcome": "LOCATOR_ONLY_DEFECT",
            "root_cause_code": "LOCATOR_INSUFFICIENT_EVIDENCE",
            "secondary_root_cause_codes": ["SCHEMA_EXPRESSIVENESS_FAILURE", "MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR"],
            "severity": "HIGH",
            "criticality": True,
            "workflow_component_responsible": ["primary_evidence_locator_assignment", "typed_locator_schema"],
            "candidate_generalized_fix": "Split page-visible and embedded-metadata identifiers; add a typed, source-hash-bound PDF_METADATA locator with exact key/value; require each identifier to be validated against its own support location.",
            "original_phase4_status": "EXCLUDED_FROM_SUPPORTED; SOURCE_REVIEW_PENDING",
            "original_false_accept_detected": False,
            "scientific_acceptance_granted": False,
        },
    ]
    expected = {"H01": h01_src, "H02": h02_src}
    for holdout, hash_ in expected.items():
        p = PHASE4 / "private_source_material/holdout_sources" / holdout / "source.pdf"
        if digest(p.read_bytes()) != hash_:
            raise ValueError(f"Source hash changed: {holdout}")
    for rec in records:
        name = rec["holdout_id"] + "_" + rec["evidence_item_id"] + ".json"
        save_json(LANE / name, rec)
    summary = {
        "lane": "H01_H02",
        "original_disagreement_count": 3,
        "adjudicated_count": len(records),
        "outcome_counts": {"LOCATOR_ONLY_DEFECT": 3},
        "original_detected_false_accept_count": 0,
        "quantitative_error_count": 0,
        "private_evidence_root": "adjudication_lanes/h01_h02/private_source_material/",
        "private_evidence_policy": "NEVER_PACKAGE",
        "source_directly_reopened": True,
        "pdf_layout_visually_checked": True,
        "human_source_review_performed": False,
        "ground_truth_critical_false_accepts": "UNKNOWN",
    }
    save_json(LANE / "LANE_SUMMARY.json", summary)


if __name__ == "__main__":
    main()
