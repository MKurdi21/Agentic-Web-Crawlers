# Derived numeric verification, version 2

Classify a quantity as `REPORTED` only when the precise value appears in the identified source location. Otherwise mark it `DERIVED` and record the operation, input values, table-row/cell keys, source locators, unit, missing-value policy, and deterministic recomputation receipt. The model may identify candidate cells; it cannot certify its own arithmetic or transcription.

For table claims, record each relevant row and column, including zeros, missing entries, and footnotes. Distinguish zero reported vulnerabilities from not tested, not reported, no effect, failed task, and absent data. Missing values are excluded from arithmetic, never silently converted to zero. A derived affected count must reconcile with the declared total and zero count.

The candidate's `scientific_v3.derive` uses decimal arithmetic and refuses missing source-cell identifiers, duplicate cells, invalid numbers, or inconsistent totals. `check_derived_claim` rejects a value that differs from recomputation and rejects a different ordered operand list. All eligible rows and zero/nonzero totals must reconcile. Source review remains responsible for confirming that each transcribed cell and category matches the PDF, including merged headings and table notes.

Counts, percentages, ratios, differences, sums, averages, medians, extrema, rankings, zero-row counts, success/failure counts, and negative-result counts require this provenance when derived. Unverifiable critical derivations remain unresolved and cannot support synthesis.
