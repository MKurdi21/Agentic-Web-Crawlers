# Comparative support protocol — 3.0.0

Before comparative prose, inventory main results, tables, figures, ablations, appendices, supplements actually present, and later competing results. Record reported versus derived values, missing versus zero, metric/unit, task, dataset, split, condition, configuration, subject, and source location. Linked external supplements remain unavailable unless separately authorized; no links are followed in closed-document mode.

Decompose subject/value, metric, condition, comparison set, scope, and ranking. Each needs its own evidence role. The target value locator need not equal the scope or ranking locator. The complete required set must be bound; this replaces the failed locator-ID equality assumption without weakening entailment.

For fully supported local maxima/minima, require complete-within-declared-scope inventory, all rows bound, equivalent comparison conditions, matching target, deterministic max/min and tie check, and explicit scope evidence. Document-wide claims additionally require recorded reconciliation across all relevant locations. Completeness/reconciliation are reviewed attestations, not a guarantee inferred by the numeric engine.

Use Decimal arithmetic for max/min/rank/ties, greater/less, counts, sums, differences, ratios and percentages. Preserve operand locations and rounding policy; do not infer denominators. PERCENT requires a source-bound denominator element with matching value and DERIVATION_INPUT coverage. Any mismatch fails; this engine currently expects exact declared Decimal equality rather than silently tolerating rounding.

Different experiment tables do not automatically conflict. Preserve table-specific values and unresolved condition equivalence. Within-report contradictions require comparable propositions and explicit resolution evidence. Missing role → PARTIALLY_SUPPORTED or UNRESOLVED, never full support. A local best cannot become a global best. A conceptual adaptive-attack aggregate must not be described as an observed online adaptive process without support.
