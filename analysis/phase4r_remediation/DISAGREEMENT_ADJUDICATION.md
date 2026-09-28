# Phase 4R source adjudication

All **43/43** original Phase 4 critical disagreement IDs match a Phase 4R source-adjudication record. Exact source evidence is stored only in private Phase 4R paths and every referenced private file passed SHA-256 verification. No record grants scientific acceptance or qualified human ground truth.

| Outcome | Count |
|---|---:|
| `BOTH_PARTIAL` | 5 |
| `LOCATOR_ONLY_DEFECT` | 35 |
| `VERIFIER_CORRECT` | 3 |

Primary root-cause counts:

| Root cause | Count |
|---|---:|
| `MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR` | 32 |
| `COMPOUND_CLAIM_OVERREACH` | 4 |
| `GLOBAL_RESULT_RECONCILIATION_FAILURE` | 1 |
| `LOCATOR_INSUFFICIENT_EVIDENCE` | 1 |
| `LOCATOR_POINTS_TO_CONTEXT_NOT_SUPPORT` | 1 |
| `LOCATOR_WRONG_PAGE` | 1 |
| `NEGATIVE_RESULT_COUNT_ERROR` | 1 |
| `QUALIFIER_OMISSION` | 1 |
| `SAMPLE_DENOMINATOR_SCOPE_ERROR` | 1 |

Decisive source findings: H03's 16.37% main-table result is narrower than the later 19.78% appendix result; H04 has four zero-vulnerability rows rather than three; H05 sampled 300 tasks rather than observing 300 failures; H06's page-27 locator does not entail its broad qualitative conclusion. These reports are now development evidence, not untouched validation data.

See `DISAGREEMENT_ADJUDICATION.json` for every item, source hash, original and verifier positions, private evidence hash, outcome, severity, and candidate generalized fix.
