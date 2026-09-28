"""Synthetic, generalized scientific-method regression tests."""
import copy
import json
import pathlib
import unittest

from scientific_v3 import (
    ScientificFailure, check_derived_claim, compose_claim, derive,
    detect_result_conflicts, locator_entailment, reconcile_comparison,
    validate_scientific_payload, check_table_row_coverage, verify_denominator_scope,
)
from validate_semantics import validate, ValidationError

SCHEMA = pathlib.Path(__file__).resolve().parents[1] / "schemas" / "scientific_evidence_v3.schema.json"
FIXTURES = pathlib.Path(__file__).resolve().parents[3] / "phase4_failure_fixtures"


def cell(row, value, *, missing=False):
    return {"table_id": "T1", "row_label": f"r{row}", "column_label": "outcome", "locator_id": f"l{row}", "value": value, "missing": missing}


def result(rid, value, *, condition="same", location="main"):
    return {"result_id": rid, "subject": rid, "metric": "success", "value": value,
            "unit": "percent", "task": "task", "dataset": "set", "benchmark": "bench",
            "split": "test", "condition": condition, "model_configuration": "cfg",
            "source_location_id": location, "support_locator_ids": [f"loc_{rid}"]}


def inventory(rows, *, complete=True):
    return {"document_wide_complete": complete,
            "searched_locations": ["ABSTRACT", "MAIN_RESULTS", "TABLES", "FIGURES", "ABLATIONS", "APPENDICES", "SUPPLEMENTARY", "LATER_COMPARISONS"],
            "results": rows}


def claim(scope="DOCUMENT_WIDE"):
    return {"scope": scope, "target_result_id": "early", "comparison_result_ids": ["early", "later"],
            "support_locator_ids": ["loc_early"], "direction": "MAX", "strict": False}


def payload():
    source = "a" * 64
    return {
        "schema_version": "3.0.0", "paper_report_id": "report_1", "source_sha256": source,
        "result_inventory": {"document_wide_complete": False, "searched_locations": ["MAIN_RESULTS"], "results": []},
        "table_cells": [],
        "atomic_propositions": [{"proposition_id": "p1", "statement": "A source-bound claim", "support_status": "SUPPORTED", "support_locator_ids": ["loc1"]}],
        "locator_assessments": [{"locator_id": "loc1", "role": "SUPPORT_LOCATOR", "status": "LOCATOR_EXACT_SUPPORT", "source_sha256": source,
                                 "source_review_record_id": "review1", "supported_proposition_ids": ["p1"],
                                 "locator_components": [{"type": "PAGE", "reference": "p. 3"}]}],
        "claims": [{"claim_id": "c1", "statement": "A source-bound claim", "claim_type": "AUTHOR_REPORTED", "atomic_proposition_ids": ["p1"],
                    "support_status": "FULLY_SUPPORTED", "quantity_type": None, "value": None, "unit": None, "metric": None,
                    "directionality": None, "scope": None, "comparison_result_ids": [], "condition": None,
                    "reported_or_derived": "NOT_QUANTITATIVE", "derivation": None, "source_values": [], "uncertainty": None,
                    "target_result_id": None, "direction": "NONE", "support_locator_ids": ["loc1"]}],
        "source_result_conflicts": [],
    }


class ScientificV3(unittest.TestCase):
    def test_sanitized_regression_fixture_inventory(self):
        fixtures = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(FIXTURES.glob("*.json"))]
        self.assertGreaterEqual(len(fixtures), 8)
        self.assertEqual(len({x["fixture_id"] for x in fixtures}), len(fixtures))
        self.assertTrue(all(x["source_content_included"] is False for x in fixtures))
        expected = {x["fixture_id"]: x["expected_outcome"] for x in fixtures}
        self.assertEqual(expected["sample_size_not_failure_count"], verify_denominator_scope(quantity_type="FAILURES", sample_size=300, event_count=None, claimed_value=300)["status"])
        self.assertEqual(expected["table_page_missing_rows"], check_table_row_coverage([f"r{i}" for i in range(1, 21)], ["r1"])["status"])
    def test_v3_payload_valid_but_not_scientifically_accepted(self):
        result = validate_scientific_payload(payload(), SCHEMA)
        self.assertFalse(result["scientific_acceptance"])
        self.assertEqual(validate("scientific_evidence_v3", payload())["schema_version"], "3.0.0")

    def test_v3_schema_version_required(self):
        p = payload(); p["schema_version"] = "2.0.0"
        with self.assertRaisesRegex(ScientificFailure, "SCHEMA"):
            validate_scientific_payload(p, SCHEMA)

    def test_v3_context_only_locator_fails_full_support(self):
        p = payload(); p["locator_assessments"][0]["status"] = "LOCATOR_CONTEXT_ONLY"
        with self.assertRaisesRegex(ScientificFailure, "LOCATOR_FALSE_SUPPORT"):
            validate_scientific_payload(p, SCHEMA)
        with self.assertRaises(ValidationError) as caught:
            validate("scientific_evidence_v3", p)
        self.assertEqual(caught.exception.layer, 4)

    def test_v3_cross_source_locator_rejected(self):
        p = payload(); p["locator_assessments"][0]["source_sha256"] = "b" * 64
        with self.assertRaisesRegex(ScientificFailure, "CROSS_SOURCE_LOCATOR"):
            validate_scientific_payload(p, SCHEMA)

    def test_v3_partial_proposition_cannot_make_full_claim(self):
        p = payload(); p["atomic_propositions"][0]["support_status"] = "PARTIALLY_SUPPORTED"
        with self.assertRaisesRegex(ScientificFailure, "COMPOUND_FALSE_SUPPORT"):
            validate_scientific_payload(p, SCHEMA)

    def test_later_appendix_higher_rejects_global_best(self):
        r = reconcile_comparison(claim(), inventory([result("early", 16.37), result("later", 19.78, location="appendix")]))
        self.assertEqual(r["status"], "CONTRADICTED")
        self.assertEqual(r["competing_result_ids"], ["later"])

    def test_local_best_requires_scope(self):
        q = claim("LOCAL"); q["comparison_result_ids"] = ["early", "other"]
        r = reconcile_comparison(q, inventory([result("early", 16.37), result("other", 12.1), result("later", 19.78)]))
        self.assertEqual(r["status"], "SUPPORTED_WITHIN_EXPLICIT_SCOPE")

    def test_global_inventory_incomplete_fails_closed(self):
        r = reconcile_comparison(claim(), inventory([result("early", 16.37)], complete=False))
        self.assertEqual(r["status"], "COMPARISON_SCOPE_UNRESOLVED")

    def test_appendix_not_searched_fails_closed(self):
        data = inventory([result("early", 16.37)])
        data["searched_locations"].remove("APPENDICES")
        self.assertEqual(reconcile_comparison(claim(), data)["status"], "COMPARISON_SCOPE_UNRESOLVED")

    def test_different_conditions_require_declared_set(self):
        q = claim(); q["comparison_result_ids"] = []
        r = reconcile_comparison(q, inventory([result("early", 16.37), result("later", 19.78, condition="other")]))
        self.assertEqual(r["status"], "COMPARISON_SCOPE_UNRESOLVED")

    def test_different_conditions_do_not_falsely_compete(self):
        q = claim(); q["comparison_result_ids"] = ["early"]
        r = reconcile_comparison(q, inventory([result("early", 16.37), result("later", 19.78, condition="other")]))
        self.assertEqual(r["status"], "SUPPORTED_WITHIN_EXPLICIT_SCOPE")

    def test_zero_row_count_and_affected_recomputed(self):
        cells = [cell(i, 0 if i in (2, 7, 12, 19) else 1) for i in range(20)]
        self.assertEqual(derive("COUNT_ZERO", cells)["result"], "4")
        self.assertEqual(derive("AFFECTED_FROM_TOTAL_MINUS_ZERO", cells, total=20)["result"], "16")
        self.assertEqual(derive("PERCENT_NONZERO", cells, total=20)["result"], "80")

    def test_table_row_coverage_requires_all_eligible_rows(self):
        self.assertEqual(check_table_row_coverage(["r1", "r2"], ["r1"])["status"], "INSUFFICIENT_TABLE_ROW_COVERAGE")

    def test_sample_size_is_not_failure_count(self):
        self.assertEqual(verify_denominator_scope(quantity_type="FAILURES", sample_size=300, event_count=None, claimed_value=300)["status"], "DENOMINATOR_SCOPE_UNRESOLVED")
        self.assertEqual(verify_denominator_scope(quantity_type="SAMPLED_TASKS", sample_size=300, event_count=None, claimed_value=300)["status"], "SUPPORTED_QUANTITY_SCOPE")

    def test_derived_claim_wrong_value_rejected(self):
        cells = [cell(i, 0 if i in (2, 7, 12, 19) else 1) for i in range(20)]
        q = {"reported_or_derived": "DERIVED", "value": 3,
             "derivation": {"operation": "COUNT_ZERO", "input_cell_keys": [list((c["table_id"], c["row_label"], c["column_label"])) for c in cells]}}
        with self.assertRaisesRegex(ScientificFailure, "DERIVED_VALUE_MISMATCH"):
            check_derived_claim(q, cells)

    def test_missing_is_excluded_not_zero(self):
        cells = [cell(1, 0), cell(2, None, missing=True), cell(3, 2)]
        self.assertEqual(derive("COUNT_ZERO", cells)["result"], "1")
        self.assertEqual(len(derive("COUNT_ZERO", cells)["excluded_missing_cell_keys"]), 1)

    def test_total_must_match_observed_nonmissing_rows(self):
        with self.assertRaisesRegex(ScientificFailure, "TOTAL_ROW_COUNT_MISMATCH"):
            derive("AFFECTED_FROM_TOTAL_MINUS_ZERO", [cell(1, 0), cell(2, 1)], total=3)

    def test_duplicate_table_cell_rejected(self):
        with self.assertRaisesRegex(ScientificFailure, "DUPLICATE_CELL"):
            derive("SUM", [cell(1, 1), cell(1, 1)])

    def test_unlocated_table_cell_rejected(self):
        x = cell(1, 1); x["locator_id"] = ""
        with self.assertRaisesRegex(ScientificFailure, "UNLOCATED_CELL"):
            derive("SUM", [x])

    def test_max_min_difference(self):
        self.assertEqual(derive("MAX", [cell(1, 3), cell(2, 8)])["result"], "8")
        self.assertEqual(derive("MIN", [cell(1, 3), cell(2, 8)])["result"], "3")
        self.assertEqual(derive("DIFFERENCE", [cell(1, 8), cell(2, 3)])["result"], "5")

    def test_true_number_false_superlative_compound_is_partial(self):
        p = [{"proposition_id": "value", "support_status": "SUPPORTED"},
             {"proposition_id": "global_best", "support_status": "CONTRADICTED"}]
        self.assertEqual(compose_claim(p)["unsupported_proposition_ids"], ["global_best"])

    def test_locator_context_only_not_support(self):
        x = {"locator_id": "l1", "source_sha256": "a" * 64, "source_review_record_id": "review1",
             "role": "SUPPORT_LOCATOR", "status": "LOCATOR_CONTEXT_ONLY", "supported_proposition_ids": ["p1"]}
        self.assertEqual(locator_entailment(["p1"], [x])["status"], "LOCATOR_COMPOUND_INSUFFICIENT")

    def test_discovery_locator_does_not_count(self):
        x = {"locator_id": "l1", "source_sha256": "a" * 64, "source_review_record_id": "review1",
             "role": "DISCOVERY_LOCATOR", "status": "LOCATOR_EXACT_SUPPORT", "supported_proposition_ids": ["p1"]}
        self.assertEqual(locator_entailment(["p1"], [x])["unsupported_proposition_ids"], ["p1"])

    def test_compound_support_needs_multiple_locators(self):
        base = {"source_sha256": "a" * 64, "source_review_record_id": "review1", "role": "SUPPORT_LOCATOR", "status": "LOCATOR_EXACT_SUPPORT"}
        a = {**base, "locator_id": "l1", "supported_proposition_ids": ["p1"]}
        b = {**base, "locator_id": "l2", "supported_proposition_ids": ["p2"]}
        self.assertEqual(locator_entailment(["p1", "p2"], [a])["status"], "LOCATOR_COMPOUND_INSUFFICIENT")
        self.assertEqual(locator_entailment(["p1", "p2"], [a, b])["status"], "LOCATOR_EXACT_SUPPORT")

    def test_partial_locator_requires_policy(self):
        x = {"locator_id": "l1", "source_sha256": "a" * 64, "source_review_record_id": "review1",
             "role": "SUPPORT_LOCATOR", "status": "LOCATOR_PARTIAL_SUPPORT", "supported_proposition_ids": ["p1"]}
        self.assertEqual(locator_entailment(["p1"], [x])["status"], "LOCATOR_COMPOUND_INSUFFICIENT")
        self.assertEqual(locator_entailment(["p1"], [x], allow_partial=True)["status"], "LOCATOR_PARTIAL_SUPPORT")

    def test_same_condition_conflicting_values_preserved(self):
        conflicts = detect_result_conflicts([result("early", 16.37), result("later", 19.78, location="appendix")])
        self.assertEqual(len(conflicts), 0)  # different subjects are competitors, not contradictory measurements
        later = result("later", 19.78, location="appendix"); later["subject"] = "early"
        self.assertEqual(detect_result_conflicts([result("early", 16.37), later])[0]["status"], "SOURCE_RESULT_CONFLICT")

    def test_different_condition_values_are_not_conflict(self):
        later = result("later", 19.78, condition="new", location="appendix"); later["subject"] = "early"
        self.assertEqual(detect_result_conflicts([result("early", 16.37), later]), [])


if __name__ == "__main__":
    unittest.main()
