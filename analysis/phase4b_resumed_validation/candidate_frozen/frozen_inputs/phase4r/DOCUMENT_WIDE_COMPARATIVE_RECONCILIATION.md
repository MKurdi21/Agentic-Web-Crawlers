# Document-wide comparative reconciliation, version 2

This protocol applies before a comparative or superlative proposition can be marked supported. It covers best, highest, lowest, maximum, minimum, overall, top, state of the art, outperforms, improved, and equivalent language. A local table maximum is a **local result only** until the comparison set and document-wide coverage are established.

1. Build a result inventory from source locations, not from the proposed narrative. Search the abstract, main results, tables, figures, ablations, appendices, available supplements, and later comparison sections. Record each location inspected or unavailable.
2. For each candidate value bind metric, value, unit, subject, task, dataset, benchmark, split, condition, model configuration, result class, and support locator. Distinguish main, appendix, supplementary, ablation, and secondary results.
3. Declare the proposed comparison set and direction. Compare only commensurate conditions. An unqualified document-wide claim requires complete coverage of relevant result-bearing locations; unavailable material is a limitation, not silent evidence of absence.
4. Recompute the ranking over the declared candidate set. If another result exceeds the target in the same scope, mark the proposed claim contradicted. If conditions differ, preserve the qualification or mark `COMPARISON_SCOPE_UNRESOLVED`.
5. Check that the support locators establish both the target number and the comparison. A discovery page or a local table cannot alone establish a document-wide superlative.

The generalized synthetic regression uses an earlier 16.37 value and a later 19.78 value. This is fixture evidence, not a paper-specific production exception. The Phase 4 H03 failure is the source-grounded trigger. `scientific_v3.reconcile_comparison` supplies deterministic ranking and fail-closed coverage checks; separate source review still verifies transcription and comparability.

If apparently inconsistent values share a subject and condition, create `SOURCE_RESULT_CONFLICT` with both locations and an unresolved status. Do not select the value that makes a narrative convenient. A narrower table may still support a qualified `LOCAL_RESULT_ONLY` claim.
