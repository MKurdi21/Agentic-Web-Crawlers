"""Deterministic Phase 4R scientific guardrails.

These checks reject unsupported numeric/comparative assertions. They do not
establish that a model transcribed the PDF correctly or replace source review.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
import json
import pathlib
import re

from jsonschema import Draft202012Validator


class ScientificFailure(ValueError):
    def __init__(self, code: str, detail: str = ""):
        self.code = code
        super().__init__(f"{code}: {detail}")


def number(value) -> Decimal:
    if isinstance(value, bool) or value is None:
        raise ScientificFailure("INVALID_NUMBER")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ScientificFailure("INVALID_NUMBER", str(value)) from exc
    if not result.is_finite():
        raise ScientificFailure("INVALID_NUMBER", str(value))
    return result


def derive(operation: str, source_cells: list[dict], *, total=None) -> dict:
    """Recompute from explicitly transcribed, source-located cells.

    The caller must verify transcription against the PDF. Missing values are
    excluded, never silently interpreted as zero.
    """
    if not source_cells:
        raise ScientificFailure("MISSING_SOURCE_CELLS")
    seen = set()
    values = []
    excluded = []
    for cell in source_cells:
        for key in ("table_id", "row_label", "column_label", "locator_id"):
            if not isinstance(cell.get(key), str) or not cell[key].strip():
                raise ScientificFailure("UNLOCATED_CELL", key)
        key = tuple(cell[k] for k in ("table_id", "row_label", "column_label"))
        if key in seen:
            raise ScientificFailure("DUPLICATE_CELL", str(key))
        seen.add(key)
        if cell.get("missing", False):
            excluded.append(key)
            continue
        values.append((key, number(cell.get("value"))))
    if not values:
        raise ScientificFailure("NO_NUMERIC_CELLS")
    nums = [v for _, v in values]
    if operation == "COUNT_ZERO":
        result = Decimal(sum(v == 0 for v in nums))
    elif operation == "COUNT_NONZERO":
        result = Decimal(sum(v != 0 for v in nums))
    elif operation == "SUM":
        result = sum(nums, Decimal(0))
    elif operation == "MEAN":
        result = sum(nums, Decimal(0)) / len(nums)
    elif operation == "MAX":
        result = max(nums)
    elif operation == "MIN":
        result = min(nums)
    elif operation == "AFFECTED_FROM_TOTAL_MINUS_ZERO":
        t = number(total)
        if t != len(values):
            raise ScientificFailure("TOTAL_ROW_COUNT_MISMATCH")
        result = t - sum(v == 0 for v in nums)
    elif operation == "PERCENT_NONZERO":
        t = number(total)
        if t != len(values):
            raise ScientificFailure("TOTAL_ROW_COUNT_MISMATCH")
        result = Decimal(100) * sum(v != 0 for v in nums) / t
    elif operation == "DIFFERENCE":
        if len(nums) != 2:
            raise ScientificFailure("DIFFERENCE_REQUIRES_TWO_VALUES")
        result = nums[0] - nums[1]
    else:
        raise ScientificFailure("UNKNOWN_DERIVATION", operation)
    return {
        "reported_or_derived": "DERIVED",
        "operation": operation,
        "result": str(result),
        "input_cell_keys": [list(key) for key, _ in values],
        "excluded_missing_cell_keys": [list(key) for key in excluded],
        "verification_method": "DETERMINISTIC_DECIMAL_RECOMPUTATION",
    }


def check_derived_claim(claim: dict, source_cells: list[dict]) -> dict:
    if claim.get("reported_or_derived") != "DERIVED":
        raise ScientificFailure("DERIVED_PROVENANCE_REQUIRED")
    derivation = claim.get("derivation") or {}
    actual = derive(derivation.get("operation"), source_cells, total=derivation.get("total"))
    if number(claim.get("value")) != number(actual["result"]):
        raise ScientificFailure("DERIVED_VALUE_MISMATCH")
    declared = list(map(tuple, derivation.get("input_cell_keys", [])))
    if declared != list(map(tuple, actual["input_cell_keys"])):
        raise ScientificFailure("DERIVATION_INPUT_MISMATCH")
    return actual


def same_comparison_condition(a: dict, b: dict) -> bool:
    """Conditions must be explicit; different conditions cannot be ranked."""
    keys = ("metric", "unit", "task", "dataset", "benchmark", "split", "condition")
    for key in keys:
        if not a.get(key) or not b.get(key):
            return False
        if a[key] != b[key]:
            return False
    return True


def reconcile_comparison(claim: dict, inventory: dict) -> dict:
    """Fail closed on unscoped superlatives and incomplete result inventories."""
    scope = claim.get("scope")
    if scope not in ("LOCAL", "DOCUMENT_WIDE"):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "SCOPE_MISSING"}
    if scope == "DOCUMENT_WIDE" and not inventory.get("document_wide_complete"):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "GLOBAL_INVENTORY_INCOMPLETE"}
    required_locations = {"ABSTRACT", "MAIN_RESULTS", "TABLES", "FIGURES", "ABLATIONS", "APPENDICES", "SUPPLEMENTARY", "LATER_COMPARISONS"}
    if scope == "DOCUMENT_WIDE" and not required_locations <= set(inventory.get("searched_locations", [])):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "RESULT_LOCATIONS_NOT_RECONCILED"}
    rows = inventory.get("results", [])
    target = next((r for r in rows if r.get("result_id") == claim.get("target_result_id")), None)
    if target is None:
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "TARGET_MISSING"}
    if scope == "LOCAL":
        comparison_ids = set(claim.get("comparison_result_ids", []))
        if not comparison_ids or target["result_id"] not in comparison_ids:
            return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "LOCAL_SET_MISSING"}
        candidates = [r for r in rows if r.get("result_id") in comparison_ids]
        if len(candidates) != len(comparison_ids):
            return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "LOCAL_SET_INCOMPLETE"}
    else:
        candidates = [r for r in rows if same_comparison_condition(target, r)]
        if len(candidates) != len(rows):
            # Unrelated experimental conditions can coexist, but a global
            # claim must declare the exact comparison set rather than silently
            # drop them.
            declared = set(claim.get("comparison_result_ids", []))
            if not declared or declared != {r["result_id"] for r in candidates}:
                return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "CONDITION_SET_AMBIGUOUS"}
    if any(not same_comparison_condition(target, r) for r in candidates):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "CONDITION_MISMATCH"}
    if detect_result_conflicts(candidates):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "SOURCE_RESULT_CONFLICT"}
    if not claim.get("support_locator_ids") or not target.get("support_locator_ids"):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "SUPPORT_LOCATOR_MISSING"}
    if not set(claim["support_locator_ids"]) & set(target["support_locator_ids"]):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "TARGET_LOCATOR_MISMATCH"}
    direction = claim.get("direction")
    if direction not in ("MAX", "MIN"):
        return {"status": "COMPARISON_SCOPE_UNRESOLVED", "reason": "DIRECTION_MISSING"}
    vals = {r["result_id"]: number(r["value"]) for r in candidates}
    extreme = max(vals.values()) if direction == "MAX" else min(vals.values())
    if vals[target["result_id"]] != extreme:
        return {"status": "CONTRADICTED", "reason": "COMPETING_RESULT_BETTER", "competing_result_ids": [rid for rid, val in vals.items() if val == extreme]}
    if len([v for v in vals.values() if v == extreme]) > 1 and claim.get("strict", False):
        return {"status": "CONTRADICTED", "reason": "TIED_NOT_STRICTLY_BEST"}
    return {"status": "SUPPORTED_WITHIN_EXPLICIT_SCOPE", "comparison_result_ids": sorted(vals)}


def compose_claim(propositions: list[dict]) -> dict:
    if not propositions:
        raise ScientificFailure("EMPTY_COMPOUND_CLAIM")
    ids = [x.get("proposition_id") for x in propositions]
    if any(not x for x in ids) or len(ids) != len(set(ids)):
        raise ScientificFailure("PROPOSITION_IDENTITY")
    unsupported = [x["proposition_id"] for x in propositions if x.get("support_status") != "SUPPORTED"]
    return {"status": "FULLY_SUPPORTED" if not unsupported else "PARTIALLY_SUPPORTED_COMPOUND_CLAIM", "unsupported_proposition_ids": unsupported}


def locator_entailment(proposition_ids: list[str], locator_assessments: list[dict], *, allow_partial=False) -> dict:
    """Enforce recorded proposition-level source judgments, not keyword hits."""
    if not proposition_ids or len(proposition_ids) != len(set(proposition_ids)):
        raise ScientificFailure("PROPOSITION_IDENTITY")
    covered = set()
    rejected = []
    partial = []
    for assessment in locator_assessments:
        status = assessment.get("status")
        if status not in {"LOCATOR_EXACT_SUPPORT", "LOCATOR_PARTIAL_SUPPORT", "LOCATOR_CONTEXT_ONLY", "LOCATOR_WRONG_LOCATION", "LOCATOR_NOT_LOCATABLE", "LOCATOR_COMPOUND_INSUFFICIENT"}:
            raise ScientificFailure("LOCATOR_STATUS")
        if not assessment.get("locator_id") or not assessment.get("source_sha256") or not assessment.get("source_review_record_id"):
            raise ScientificFailure("LOCATOR_REVIEW_PROVENANCE")
        if assessment.get("role") == "DISCOVERY_LOCATOR":
            continue
        if assessment.get("role") != "SUPPORT_LOCATOR":
            raise ScientificFailure("LOCATOR_ROLE")
        if status == "LOCATOR_EXACT_SUPPORT" or (allow_partial and status == "LOCATOR_PARTIAL_SUPPORT"):
            covered.update(assessment.get("supported_proposition_ids", []))
            if status == "LOCATOR_PARTIAL_SUPPORT":
                partial.append(assessment["locator_id"])
        else:
            rejected.append(assessment["locator_id"])
    missing = sorted(set(proposition_ids) - covered)
    status = "LOCATOR_COMPOUND_INSUFFICIENT" if missing or rejected else ("LOCATOR_PARTIAL_SUPPORT" if partial else "LOCATOR_EXACT_SUPPORT")
    return {"status": status, "unsupported_proposition_ids": missing, "rejected_locator_ids": rejected, "partial_locator_ids": partial}


def detect_result_conflicts(results: list[dict]) -> list[dict]:
    """Preserve apparently incompatible source values for human/source review."""
    groups = {}
    keys = ("subject", "metric", "unit", "task", "dataset", "benchmark", "split", "condition", "model_configuration")
    for result in results:
        if not result.get("result_id") or not result.get("source_location_id"):
            raise ScientificFailure("RESULT_PROVENANCE_MISSING")
        if any(not result.get(key) for key in keys):
            raise ScientificFailure("RESULT_SCOPE_MISSING")
        groups.setdefault(tuple(result[key] for key in keys), []).append(result)
    conflicts = []
    for scope, rows in groups.items():
        values = {number(row.get("value")) for row in rows}
        if len(values) > 1:
            conflicts.append({"status": "SOURCE_RESULT_CONFLICT", "result_ids": sorted(r["result_id"] for r in rows), "source_location_ids": sorted(r["source_location_id"] for r in rows), "values": sorted(str(v) for v in values), "resolution_status": "UNRESOLVED"})
    return conflicts


def check_table_row_coverage(eligible_row_ids: list[str], located_row_ids: list[str]) -> dict:
    if not eligible_row_ids or len(eligible_row_ids) != len(set(eligible_row_ids)):
        raise ScientificFailure("ELIGIBLE_ROW_SET_INVALID")
    if len(located_row_ids) != len(set(located_row_ids)):
        raise ScientificFailure("DUPLICATE_LOCATED_ROW")
    missing = sorted(set(eligible_row_ids) - set(located_row_ids))
    extra = sorted(set(located_row_ids) - set(eligible_row_ids))
    return {"status": "COMPLETE_TABLE_ROW_COVERAGE" if not missing and not extra else "INSUFFICIENT_TABLE_ROW_COVERAGE", "missing_row_ids": missing, "extra_row_ids": extra}


def verify_denominator_scope(*, quantity_type: str, sample_size, event_count, claimed_value) -> dict:
    """Keep sampled tasks distinct from failures/events within the sample."""
    if quantity_type not in ("SAMPLED_TASKS", "FAILURES", "SUCCESSES"):
        raise ScientificFailure("QUANTITY_TYPE")
    if number(sample_size) < 0:
        raise ScientificFailure("SAMPLE_SIZE")
    if quantity_type == "SAMPLED_TASKS":
        expected = number(sample_size)
    else:
        if event_count is None:
            return {"status": "DENOMINATOR_SCOPE_UNRESOLVED", "reason": "EVENT_COUNT_NOT_OBSERVED"}
        expected = number(event_count)
        if expected < 0 or expected > number(sample_size):
            raise ScientificFailure("EVENT_COUNT_RANGE")
    return {"status": "SUPPORTED_QUANTITY_SCOPE" if number(claimed_value) == expected else "DENOMINATOR_SCOPE_CONTRADICTED", "expected_value": str(expected)}


def validate_scientific_payload(payload: dict, schema_path: pathlib.Path) -> dict:
    """Structural, format, semantic, and cross-record guards, in that order.

    Source truth still requires a separate source reviewer. This function
    deliberately never marks a claim scientifically accepted.
    """
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    failures = list(Draft202012Validator(schema).iter_errors(payload))
    if failures:
        raise ScientificFailure("SCHEMA", failures[0].message)
    sha_re = re.compile(r"[0-9a-f]{64}\Z")
    id_re = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]*\Z")
    if not sha_re.fullmatch(payload["source_sha256"]) or not id_re.fullmatch(payload["paper_report_id"]):
        raise ScientificFailure("FORMAT_TOP_LEVEL")
    for loc in payload["locator_assessments"]:
        if not sha_re.fullmatch(loc["source_sha256"]) or not all(id_re.fullmatch(loc[k]) for k in ("locator_id", "source_review_record_id")):
            raise ScientificFailure("FORMAT_LOCATOR")
        if loc["source_sha256"] != payload["source_sha256"]:
            raise ScientificFailure("CROSS_SOURCE_LOCATOR")
    results = payload["result_inventory"]["results"]
    props = payload["atomic_propositions"]
    locs = payload["locator_assessments"]
    claims = payload["claims"]
    for rows, key in ((results, "result_id"), (props, "proposition_id"), (locs, "locator_id"), (claims, "claim_id")):
        values = [x[key] for x in rows]
        if len(values) != len(set(values)) or any(not id_re.fullmatch(v) for v in values):
            raise ScientificFailure("RECORD_IDENTITY", key)
    result_ids = {x["result_id"] for x in results}
    prop_ids = {x["proposition_id"] for x in props}
    loc_ids = {x["locator_id"] for x in locs}
    for loc in locs:
        if not set(loc["supported_proposition_ids"]) <= prop_ids:
            raise ScientificFailure("LOCATOR_PROPOSITION_REFERENCE")
    for proposition in props:
        if not set(proposition["support_locator_ids"]) <= loc_ids:
            raise ScientificFailure("PROPOSITION_LOCATOR_REFERENCE")
    proposition_by_id = {x["proposition_id"]: x for x in props}
    for claim in claims:
        if not set(claim["atomic_proposition_ids"]) <= prop_ids:
            raise ScientificFailure("CLAIM_PROPOSITION_REFERENCE")
        if not set(claim["support_locator_ids"]) <= loc_ids:
            raise ScientificFailure("CLAIM_LOCATOR_REFERENCE")
        if not set(claim["comparison_result_ids"]) <= result_ids:
            raise ScientificFailure("CLAIM_RESULT_REFERENCE")
        if (claim["value"] is None) != (claim["reported_or_derived"] == "NOT_QUANTITATIVE"):
            raise ScientificFailure("QUANTITY_CLASSIFICATION")
        composition = compose_claim([proposition_by_id[x] for x in claim["atomic_proposition_ids"]])
        if claim["support_status"] == "FULLY_SUPPORTED" and composition["status"] != "FULLY_SUPPORTED":
            raise ScientificFailure("COMPOUND_FALSE_SUPPORT")
        supporting = [loc for loc in locs if loc["locator_id"] in claim["support_locator_ids"]]
        entailment = locator_entailment(claim["atomic_proposition_ids"], supporting)
        if claim["support_status"] == "FULLY_SUPPORTED" and entailment["status"] != "LOCATOR_EXACT_SUPPORT":
            raise ScientificFailure("LOCATOR_FALSE_SUPPORT")
        if claim["reported_or_derived"] == "DERIVED":
            if not isinstance(claim["derivation"], dict):
                raise ScientificFailure("DERIVED_PROVENANCE_REQUIRED")
            cells = [c for c in payload["table_cells"] if (c["table_id"], c["row_label"], c["column_label"]) in set(map(tuple, claim["derivation"].get("input_cell_keys", [])))]
            normalized = [{"table_id": c["table_id"], "row_label": c["row_label"], "column_label": c["column_label"], "locator_id": c["locator_id"], "missing": c["missing"], "value": c["cell_value"]} for c in cells]
            check_derived_claim(claim, normalized)
        if claim["direction"] != "NONE" or re.search(r"\b(best|highest|lowest|maximum|minimum|overall|top|outperform|underperform|most effective|least effective)\b", claim["statement"], re.I):
            comparison = reconcile_comparison(claim, payload["result_inventory"])
            if claim["support_status"] == "FULLY_SUPPORTED" and comparison["status"] != "SUPPORTED_WITHIN_EXPLICIT_SCOPE":
                raise ScientificFailure("COMPARATIVE_FALSE_SUPPORT", comparison["reason"])
    for conflict in payload["source_result_conflicts"]:
        if not set(conflict["result_ids"]) <= result_ids:
            raise ScientificFailure("CONFLICT_RESULT_REFERENCE")
        if conflict["resolution_status"] == "UNRESOLVED":
            affected = set(conflict["result_ids"])
            if any(c["support_status"] == "FULLY_SUPPORTED" and affected & set(c["comparison_result_ids"]) for c in claims):
                raise ScientificFailure("UNRESOLVED_RESULT_CONFLICT_ACCEPTED")
    return {"status": "STRUCTURALLY_AND_SEMANTICALLY_VALID", "scientific_acceptance": False}
