"""Build the source-adjudication root-cause catalog with explicit unobserved classes."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
adjudication = json.loads((OUT / "DISAGREEMENT_ADJUDICATION.json").read_text(encoding="utf-8"))
actual = adjudication["primary_root_cause_counts"]

# Code, definition, detection, prevention, affected component.
rows = [
    ("LOCAL_RESULT_MISREAD", "A value or label is transcribed incorrectly at its local source.", "Compare value, row/column, and caption with rendered source.", "Require exact source-bound value and table-cell review.", "extraction, verification"),
    ("GLOBAL_RESULT_RECONCILIATION_FAILURE", "A local result is characterized as document-wide without examining later relevant results.", "Inventory and compare main, appendix, supplementary, and later result locations.", "Gate global comparative claims on complete result inventory and explicit scope.", "result inventory, synthesis"),
    ("TABLE_ROW_COUNT_ERROR", "The eligible table row count is wrong.", "Enumerate source-located row keys and recompute count.", "Use deterministic row enumeration with inclusion criteria.", "table extraction, arithmetic"),
    ("TABLE_CELL_ALIGNMENT_ERROR", "A value is assigned to the wrong row, column, or merged heading.", "Inspect rendered table layout and compare extraction order.", "Bind row, column, header, footnote, and condition per cell.", "table extraction, locator"),
    ("DERIVED_VALUE_ERROR", "A calculated value differs from its stated operands or operation.", "Recompute with deterministic decimal logic.", "Store operands and reject mismatched result.", "numeric validator"),
    ("ARITHMETIC_VERIFICATION_MISSING", "A derived claim lacks an independent recomputation receipt.", "Check derivation type, inputs, operation, and verification method.", "Require deterministic recomputation for supported derived claims.", "numeric validator, verification"),
    ("MAIN_TEXT_APPENDIX_CONFLICT", "Main text and appendix appear to report incompatible values.", "Compare exact experimental conditions and source locations.", "Preserve a source-result conflict until conditions explain it.", "result inventory, verification"),
    ("MAIN_TABLE_LATER_TABLE_CONFLICT", "A later table changes or narrows an earlier table conclusion.", "Search all result tables and compare metric/condition scope.", "Inventory later tables before document-wide prose.", "result inventory, synthesis"),
    ("RESULT_SCOPE_CONFUSION", "A local, subset, or specific-condition result is reported as broader.", "Bind dataset, split, task, condition, and comparison set.", "Require explicit scope for every comparative proposition.", "extraction, synthesis"),
    ("COMPARATIVE_LANGUAGE_OVERREACH", "Comparative prose asserts more than candidate values show.", "Decompose comparison and recompute ranking.", "Fail closed on unsupported comparison propositions.", "claim decomposition, verification"),
    ("SUPERLATIVE_WITHOUT_GLOBAL_SEARCH", "A best/highest claim lacks document-wide candidate search.", "Inspect inventory completeness and searched locations.", "Limit claim to local result or mark scope unresolved.", "result inventory, synthesis"),
    ("CONDITION_OMISSION", "A result loses a material experimental condition.", "Compare claim qualifiers with table heading and methods.", "Require condition in quantitative claim structure.", "extraction, schema"),
    ("QUALIFIER_OMISSION", "A material narrower qualifier is omitted from a claim.", "Compare each atomic proposition with source qualifiers.", "Preserve qualifiers before composing narrative.", "claim decomposition, verification"),
    ("COMPOUND_CLAIM_OVERREACH", "A multi-part claim is treated as fully supported although a part is not.", "Review proposition-level statuses and aggregate mechanically.", "Full support requires all material propositions supported.", "claim decomposition, locator"),
    ("MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR", "One locator is reused for propositions supported in different locations.", "Map each atomic proposition to the exact pages/tables it needs.", "Use multiple or compound support locators.", "locator, verification"),
    ("LOCATOR_WRONG_PAGE", "The cited page does not contain the supporting source material.", "Open cited PDF page and compare exact proposition.", "Require source-page entailment before support.", "locator"),
    ("LOCATOR_INSUFFICIENT_EVIDENCE", "The locator supports only part of a proposed claim.", "Inspect cited location against every proposition.", "Add necessary source locations or fail closed.", "locator, verification"),
    ("LOCATOR_TOO_BROAD", "The locator covers an area too broad to reproduce the evidence efficiently.", "Check whether a smaller page, table, row, or span can identify support.", "Prefer specific typed source objects and cell keys.", "locator"),
    ("LOCATOR_POINTS_TO_CONTEXT_NOT_SUPPORT", "The cited location discusses the topic but does not entail the proposition.", "Ask whether the exact location alone substantiates the claim.", "Separate discovery from support locator and reject context-only support.", "locator, verification"),
    ("LOCATOR_LAYOUT_MISREAD", "Text-order or page rendering causes a table/figure locator to bind incorrectly.", "Compare extracted text with rendered page, caption, and columns.", "Require visual review for layout-sensitive evidence.", "PDF extraction, locator"),
    ("TEXT_EXTRACTION_ORDER_ERROR", "Extraction reorders content in a way that changes meaning or proximity.", "Compare text artifact order to rendered source.", "Retain page coordinates and visual confirmation.", "PDF extraction"),
    ("MULTICOLUMN_EXTRACTION_ERROR", "Columns are interleaved or read in the wrong sequence.", "Inspect rendered page and extracted block coordinates.", "Use layout-aware extraction or manual review.", "PDF extraction"),
    ("NEGATIVE_RESULT_COUNT_ERROR", "A count of zero or negative outcomes is wrong.", "Enumerate all eligible rows and independently recompute zero/nonzero counts.", "Differentiate zero, absent, and untested, then recompute.", "numeric validator, negative findings"),
    ("ABSENCE_VS_ZERO_CONFUSION", "Missing/unreported data is treated as observed zero.", "Check cell symbols, notes, and row eligibility.", "Keep missing distinct from zero in schema and arithmetic.", "table extraction, numeric validator"),
    ("VERSION_OR_SECTION_CONFUSION", "A value or identifier belongs to another version, appendix, or section context.", "Compare version/date and result location metadata.", "Bind every result to source version and section.", "identity, result inventory"),
    ("SCHEMA_EXPRESSIVENESS_FAILURE", "The structured contract cannot represent the needed scientific distinction.", "Attempt lossless mapping of source evidence into schema.", "Version schema and add typed fields rather than forcing prose.", "schema"),
    ("VERIFICATION_PROTOCOL_FAILURE", "Review omits a needed source check or treats model agreement as proof.", "Audit verifier questions and source reopening record.", "Require explicit locator, arithmetic, scope, and contradiction checks.", "verification"),
    ("SKILL_INSTRUCTION_FAILURE", "Inactive skill guidance fails to prompt a required step or creates conflicting triggers.", "Trace workflow step to skill instruction and test triggering.", "Keep focused skill boundaries and deterministic checks in scripts.", "skills"),
    ("SAMPLE_DENOMINATOR_SCOPE_ERROR", "A described count refers to a sample rather than all failures or observations.", "Identify sampled population, included outcomes, and denominator phrase in source.", "Represent sample size separately from event counts and verify denominators.", "extraction, quantitative schema, verification"),
    ("OTHER", "An adjudicated cause not covered by this versioned catalog.", "Require explicit rationale and source evidence.", "Add a specific versioned class if it recurs.", "governance"),
]

observed_by_code = {}
for record in adjudication["records"]:
    observed_by_code.setdefault(record["root_cause_code"], []).append(f'{record["holdout_id"]}:{record["field_id"]}')
assert set(actual) <= {row[0] for row in rows}
catalog = []
for code, definition, detection, prevention, components in rows:
    examples = sorted(set(observed_by_code.get(code, [])))[:3]
    catalog.append({
        "code": code,
        "definition": definition,
        "observed_primary_count": actual.get(code, 0),
        "examples": examples if examples else ["Not observed among the 43 source-adjudicated primary causes; retained as a testable risk class."],
        "detection_strategy": detection,
        "prevention_strategy": prevention,
        "affected_workflow_components": [x.strip() for x in components.split(",")],
    })

machine = {"schema_version": "phase4r-root-cause-taxonomy-v1", "source_adjudication_count": 43, "classification_count": len(catalog), "classes": catalog}
(OUT / "ROOT_CAUSE_TAXONOMY.json").write_text(json.dumps(machine, indent=2) + "\n", encoding="utf-8")
lines = ["# Root-cause taxonomy, version 1", "", "The 43 source-adjudicated disagreements produce nine observed primary classes. The remaining classes are explicit risks for generalized testing, not claims that they occurred in Phase 4. Codes may be refined only with preserved source evidence and a new taxonomy version.", "", "| Code | Observed | Definition | Detection | Prevention | Components |", "|---|---:|---|---|---|---|"]
for x in catalog:
    lines.append(f'| `{x["code"]}` | {x["observed_primary_count"]} | {x["definition"]} | {x["detection_strategy"]} | {x["prevention_strategy"]} | {", ".join(x["affected_workflow_components"])} |')
lines += ["", "Observed examples and counts are in `ROOT_CAUSE_TAXONOMY.json`; exact source evidence remains private. A category is not `FIXED` solely because a familiar paper now passes: the generalized synthetic mechanism and consumed-development regression must also pass."]
(OUT / "ROOT_CAUSE_TAXONOMY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(json.dumps({"classes": len(catalog), "observed_classes": len(actual), "observed_total": sum(actual.values())}))
