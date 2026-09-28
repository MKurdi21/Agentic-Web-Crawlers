# Root-cause closure on consumed development reports

All 43 original critical disagreements were source-adjudicated: 35 locator-only defects, five partially correct primary/verifier assessments, and three verifier-correct findings. Nine primary root-cause classes were observed. The status below concerns a **migration-candidate methodology**, not production scientific correctness.

| Observed root cause | Count | Closure | Evidence and remaining limit |
|---|---:|---|---|
| `MULTIPLE_PROPOSITIONS_SINGLE_LOCATOR` | 32 | MITIGATED | Atomic proposition and compound support-locator rules; source-bound development corrections or fail-closed status. Source review remains necessary to establish entailment. |
| `COMPOUND_CLAIM_OVERREACH` | 4 | MITIGATED | Full support now requires all material propositions. Synthetic mixed-support tests pass; decomposition completeness still needs reviewer judgment. |
| `GLOBAL_RESULT_RECONCILIATION_FAILURE` | 1 | MITIGATED | H03 is narrowed; a later higher synthetic result defeats a global-best claim. Inventory completeness and value transcription remain source-review duties. |
| `LOCATOR_INSUFFICIENT_EVIDENCE` | 1 | FAIL_CLOSED | Incomplete support cannot be counted as exact support; corrected compound location may be proposed. |
| `LOCATOR_WRONG_PAGE` | 1 | FAIL_CLOSED | Cited-page entailment is mandatory; source metadata needs its own typed locator. |
| `QUALIFIER_OMISSION` | 1 | MITIGATED | Atomic conditions and scope fields force explicit qualification. |
| `NEGATIVE_RESULT_COUNT_ERROR` | 1 | MITIGATED | H04 table rows deterministically recompute four zeros and 16 affected; cell transcription remains a source-review step. |
| `SAMPLE_DENOMINATOR_SCOPE_ERROR` | 1 | MITIGATED | H05's 300 sampled tasks no longer become 300 failures; unknown failure count fails closed. |
| `LOCATOR_POINTS_TO_CONTEXT_NOT_SUPPORT` | 1 | FAIL_CLOSED | H06 page-27 context is rejected for the broad proposition; discovery and support locations are distinct. |

None of these categories is marked `FIXED` solely because an original report now has a correction proposal. The generalized synthetic tests exercise comparative ranking, arithmetic, denominator scope, atomic aggregation, locator coverage, and source-result conflicts. Of the 42 original locator failures, 38 have source-bound correction proposals and four remain fail-closed. Ten previously supported original claims were newly limited by the stricter protocol; their original support is not silently carried forward. No original detected false accept received scientific acceptance.

The remaining methodological uncertainty is intentional: automatic checks cannot certify PDF transcription, table layout, proposition completeness, or human scientific judgment. The next untouched holdout must challenge the frozen candidate. Human-reviewed ground truth remains `UNKNOWN`.
