# Locator entailment protocol, version 2

Separate `DISCOVERY_LOCATOR` from `SUPPORT_LOCATOR`. A topic, number, or related context appearing at a location does not establish that the specified locator entails the full proposition. A support review records source hash, locator ID and components, proposition IDs, reviewer record, and one of:

`LOCATOR_EXACT_SUPPORT`, `LOCATOR_PARTIAL_SUPPORT`, `LOCATOR_CONTEXT_ONLY`, `LOCATOR_WRONG_LOCATION`, `LOCATOR_NOT_LOCATABLE`, or `LOCATOR_COMPOUND_INSUFFICIENT`.

Only exact support qualifies by default. Partial support requires an explicit field-risk policy and cannot silently become exact support. Context-only, wrong-location, not-locatable, and compound-insufficient records fail closed. `scientific_v3.locator_entailment` checks recorded proposition coverage; it does not infer entailment from keywords or replace source inspection.

Support compound locators when a proposition spans a main result and appendix, multiple tables or pages, text plus figure, or multiple text spans. A compound claim can use several support locations; each proposition must be covered. Typed components include page, range, section, table, figure, equation, appendix, text span, artifact URL, repository file, and source PDF metadata. The latter addresses identifiers present in embedded `/DOI` metadata but not on a cited page. Metadata is not a substitute for author-provided scientific evidence.

For tables, record the table ID plus relevant row/column or cell keys; merely pointing at the table page is insufficient for a derived count. For rendered layout, check caption association, merged headers, reading order, and page-spanning content. If source and extraction disagree, preserve both observations and use the rendered PDF to adjudicate.
