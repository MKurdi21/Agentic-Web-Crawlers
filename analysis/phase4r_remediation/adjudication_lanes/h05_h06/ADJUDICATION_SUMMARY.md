# H05-H06 Phase 4R source adjudication

This lane reexamined all 26 Phase 4 critical primary/verifier disagreements for H05 WebVoyager and H06 IRLbot against the exact source PDFs. Both PDF SHA-256 values match the Phase 4 primary and verifier records. Verbatim source excerpts and rendered pages remain under `private/` and are never packageable. The packageable record is `H05_H06_DISAGREEMENT_ADJUDICATION.json`; each record points to a hash-verified private excerpt.

| Holdout | Disagreements | Locator-only defects | Both partial | Verifier correct |
|---|---:|---:|---:|---:|
| H05 | 12 | 10 | 2 | 0 |
| H06 | 14 | 12 | 1 | 1 |
| Total | 26 | 22 | 3 | 1 |

The H05 `methods.experiment_design` item contains an additional substantive count/scope error missed by Phase 4 verification: the primary record says **300 failures** were analyzed, while the paper says **300 tasks** were sampled and the failed cases within that sample were categorized (PDF page 8). The verifier correctly detected incomplete locator support but did not detect this denominator error. The outcome is `BOTH_PARTIAL`, root cause `SAMPLE_DENOMINATOR_SCOPE_ERROR`, severity `HIGH`.

The H06 `results.qualitative` item is a strict locator false accept. Its submitted page-27 locator contains crawl measurements, while the no-bottlenecks conclusion is supported by the abstract and conclusion on pages 1 and 32. The outcome is `VERIFIER_CORRECT`, root cause `LOCATOR_POINTS_TO_CONTEXT_NOT_SUPPORT`, severity `HIGH`.

Most other disagreements arise because a single page or table is attached to a statement combining propositions from multiple source locations. Two validity-threat items also blur source observations with analyst inference. The proposed general repairs are atomic claim decomposition, complete proposition-to-locator coverage, explicit inference labeling, and numeric-denominator checks. These are remediation findings on a consumed validation set, not independent workflow validation or human-reviewed ground truth.
