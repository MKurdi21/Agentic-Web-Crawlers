# Proposition support model — 3.0.0

Evidence schema 4.0.0 implements REPORT → FIELD → CLAIM → ATOMIC_PROPOSITION → SUPPORT_REQUIREMENT → SUPPORT_SET → LOCATOR → SOURCE_ELEMENT. Each material proposition has an explicit support state and verification state. A compound claim is fully source-supported only when every material proposition passes its required roles. Omitting a troublesome component is narrowing, not repair: preserve the original item, record the removed component and reason, and keep a crosswalk to revised propositions.

Proposition origin is required: SOURCE_REPORTED, ANALYST_INFERENCE, ARTIFACT_METADATA, or PROCESS_PROVENANCE. Analyst interpretation has an explicit rationale and may be INFERENCE_GROUNDED or unresolved; it never aliases direct source support or makes a compound claim fully source-supported. Artifact metadata and process provenance are retained separately, not supported by a paper-page locator. SOURCE_REPORTED means what the paper reports, not externally established truth.

A support set uses SINGLE or ALL_ELEMENTS. Partial constituent locators may jointly entail a proposition only when a source reviewer has explicitly reviewed the complete set. CONTEXT_ONLY, IRRELEVANT, CONTRADICTORY and UNRESOLVED cannot contribute exact support. Entailment belongs to a proposition/locator/role triple, not to a locator globally.

source_elements identify page, type and precise human-readable reference. content_sha256 binds exact extracted-page bytes, not a bounding box or cell transcript. validate_source_bindings checks those byte hashes against the identified source/extraction. It does not establish cell correctness, completeness, or entailment; those require source-grounded review, including rendered content when needed. No JSON payload can prove its own scientific truth.

support_dependencies(graph, locator_id) identifies propositions affected by removal. proposition_elements(graph, proposition_id) identifies required source elements. Missing requirements, cross-source links, unbound operands, source conflicts, and full support over partial material components fail closed.

This is a breaking schema revision. Preserve schema-v3 bytes and pins; create a new v4 artifact and explicit old-item → new-claim/proposition mapping. No automatic v3 approval transfer, no regeneration of historical summaries, and no live import. The controller retains old operational stage contracts; v4 is an explicit scientific validation gate via validate_semantics, not a new production acceptance/approval route. Future integration must preserve that gate and must not bypass it through legacy evidence acceptance.

Parsing, structure, format, semantic graph validation and external source-binding checks remain distinct. Test fixtures are synthetic. Model review is not trusted-human approval. No production human approval mechanism is configured.
