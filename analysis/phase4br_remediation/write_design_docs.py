import json,collections
from pathlib import Path
O=Path(__file__).resolve().parent;C=O/'candidate_v4br'
def md(name,text): (O/name).write_text(text.strip()+'\n',encoding='utf-8')
docs={
'PROPOSITION_SUPPORT_MODEL.md':'''# Proposition support model — 3.0.0

Evidence schema 4.0.0 implements REPORT → FIELD → CLAIM → ATOMIC_PROPOSITION → SUPPORT_REQUIREMENT → SUPPORT_SET → LOCATOR → SOURCE_ELEMENT. Each material proposition has an explicit support state and verification state. A compound claim is fully source-supported only when every material proposition passes its required roles. Omitting a troublesome component is narrowing, not repair: preserve the original item, record the removed component and reason, and keep a crosswalk to revised propositions.

Proposition origin is required: SOURCE_REPORTED, ANALYST_INFERENCE, ARTIFACT_METADATA, or PROCESS_PROVENANCE. Analyst interpretation has an explicit rationale and may be INFERENCE_GROUNDED or unresolved; it never aliases direct source support or makes a compound claim fully source-supported. Artifact metadata and process provenance are retained separately, not supported by a paper-page locator. SOURCE_REPORTED means what the paper reports, not externally established truth.

A support set uses SINGLE or ALL_ELEMENTS. Partial constituent locators may jointly entail a proposition only when a source reviewer has explicitly reviewed the complete set. CONTEXT_ONLY, IRRELEVANT, CONTRADICTORY and UNRESOLVED cannot contribute exact support. Entailment belongs to a proposition/locator/role triple, not to a locator globally.

source_elements identify page, type and precise human-readable reference. content_sha256 binds exact extracted-page bytes, not a bounding box or cell transcript. validate_source_bindings checks those byte hashes against the identified source/extraction. It does not establish cell correctness, completeness, or entailment; those require source-grounded review, including rendered content when needed. No JSON payload can prove its own scientific truth.

support_dependencies(graph, locator_id) identifies propositions affected by removal. proposition_elements(graph, proposition_id) identifies required source elements. Missing requirements, cross-source links, unbound operands, source conflicts, and full support over partial material components fail closed.

This is a breaking schema revision. Preserve schema-v3 bytes and pins; create a new v4 artifact and explicit old-item → new-claim/proposition mapping. No automatic v3 approval transfer, no regeneration of historical summaries, and no live import. The controller retains old operational stage contracts; v4 is an explicit scientific validation gate via validate_semantics, not a new production acceptance/approval route. Future integration must preserve that gate and must not bypass it through legacy evidence acceptance.

Parsing, structure, format, semantic graph validation and external source-binding checks remain distinct. Test fixtures are synthetic. Model review is not trusted-human approval. No production human approval mechanism is configured.
''',
'SUPPORT_LOCATOR_ROLE_MODEL.md':'''# Proposition-specific locator roles

VALUE_SUPPORT identifies the reported cell or text value. METRIC_SUPPORT defines what was measured and its unit. CONDITION_SUPPORT binds dataset, denominator, task, model, split, attack/benign status and configuration. COMPARISON_SET_SUPPORT enumerates eligible alternatives. RANKING_SUPPORT binds all compared numeric values. SCOPE_SUPPORT establishes the local/table/document-wide boundary. DERIVATION_INPUT binds every operand, including percentage denominators. QUALIFIER_SUPPORT preserves attribution, version and uncertainty. NEGATIVE_RESULT_SUPPORT locates the negative finding. LIMITATION_SUPPORT locates a stated limitation.

A locator can play several roles only if each proposition-role relation has a recorded source review. Topic proximity is not support. A correct value cannot compensate for a wrong attack condition. A table cell alone rarely supplies a complete experimental condition; use caption, methods and relevant context as separate locators. Discovery locations remain separate from support locations.

SOURCE_REPORTED assertions use EXACT/PARTIAL/CONTEXT_ONLY/CONTRADICTORY/IRRELEVANT/UNRESOLVED entailment. Grounded analyst inferences retain their distinct origin and partial source entailment. Unknown absence is not zero or not-applicable. An unsupported whole-document absence stays unresolved rather than acquiring a broad page range.
''',
'COMPARATIVE_SUPPORT_PROTOCOL.md':'''# Comparative support protocol — 3.0.0

Before comparative prose, inventory main results, tables, figures, ablations, appendices, supplements actually present, and later competing results. Record reported versus derived values, missing versus zero, metric/unit, task, dataset, split, condition, configuration, subject, and source location. Linked external supplements remain unavailable unless separately authorized; no links are followed in closed-document mode.

Decompose subject/value, metric, condition, comparison set, scope, and ranking. Each needs its own evidence role. The target value locator need not equal the scope or ranking locator. The complete required set must be bound; this replaces the failed locator-ID equality assumption without weakening entailment.

For fully supported local maxima/minima, require complete-within-declared-scope inventory, all rows bound, equivalent comparison conditions, matching target, deterministic max/min and tie check, and explicit scope evidence. Document-wide claims additionally require recorded reconciliation across all relevant locations. Completeness/reconciliation are reviewed attestations, not a guarantee inferred by the numeric engine.

Use Decimal arithmetic for max/min/rank/ties, greater/less, counts, sums, differences, ratios and percentages. Preserve operand locations and rounding policy; do not infer denominators. PERCENT requires a source-bound denominator element with matching value and DERIVATION_INPUT coverage. Any mismatch fails; this engine currently expects exact declared Decimal equality rather than silently tolerating rounding.

Different experiment tables do not automatically conflict. Preserve table-specific values and unresolved condition equivalence. Within-report contradictions require comparable propositions and explicit resolution evidence. Missing role → PARTIALLY_SUPPORTED or UNRESOLVED, never full support. A local best cannot become a global best. A conceptual adaptive-attack aggregate must not be described as an observed online adaptive process without support.
''',
'PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md':'''# Per-report pre-access receipt protocol — 1.0.0

Construct a fresh report-specific context packet from the frozen methodology and current-report inputs only. Verify immutable-code equality and current source identity using metadata/hash access. Write PRE_ACCESS_RECEIPT.json with exclusive creation, flush/fsync, close and byte readback before substantive interpretation. Required bindings: phase, holdout/report ID, paper ID, source-file ID/hash, immutable candidate manifest hash, methodology hash, protocol hashes, field-catalog hash, holdout state, context protocol version, creation time, and substantive_source_access_started=false.

The source-access helper refuses absent/mismatched receipts and unapproved report IDs. It reads bytes to confirm the source hash, writes a separate SOURCE_ACCESS_BEGAN event bound to the receipt, then releases bytes to analysis. Physical hashing reads precede that event; substantive interpretation must not. Never backdate, overwrite or reconstruct a pre-access receipt. Sequence 1 must precede sequence 2; timestamp ordering is supplementary.

The Phase4BR allowlist contains B01 only. Future resumed validation must explicitly authorize one current report after the prior report gate passes. No next-report source read, rendered page, extraction or verifier task before its receipt. Sequential stopping and fresh-context construction remain mandatory.

This is application-level enforcement with auditable receipts, not an OS sandbox, human proof, or arbitrary power-loss guarantee. Direct tool access outside the helper must be prevented by orchestration and independently audited. If isolation cannot be established, stop before another reserved report is opened.
''',
'VERIFICATION_PROTOCOL_V3.md':'''# Verification protocol — 3.0.0

For each material atomic proposition, answer separately: is the proposition correct; does this locator entail it; is support exact or partial; which additional location is required; is the statement comparative; are set, condition and scope established; is ranking valid; is the number reported or derived; do all operands including denominator have support; are all qualifiers/material components covered?

Record claim correctness independently from locator correctness. Correct claim plus incomplete locator remains unacceptable as fully verified structured evidence. Do not vote between models: reopen exact source bytes and inspect relevant rendered elements. Preserve primary, verifier and adjudicated records separately. Unicode text must be decoded as UTF-8; terminal rendering is not evidence of misspelling.

Use PRIMARY_MODEL_EXTRACTION, SEPARATE_CONTEXT_MODEL_VERIFICATION and NON_INDEPENDENT_SECOND_PASS accurately. None aliases INDEPENDENT_HUMAN_SOURCE_REVIEW or TRUSTED_HUMAN_APPROVAL. No software actor or TEST_FIXTURE_NOT_A_HUMAN can authorize production scientific acceptance. Ground-truth false accepts remain UNKNOWN without qualified human adjudication.

Frozen future validation retains all critical-item review and deterministic sha256-lexicographic-v1 lower-risk sampling: complete eligible set first, min(N,max(3,ceil(.25*N))), manifest before review. Item IDs and UTF-8 canonicalization follow inherited frozen sampling rules. Do not select by extraction order, difficulty or earlier validation findings. Source and methodology hashes bind every review.

Every future primary/verifier report context is fresh, fork_history=none, with a packet-hash allowlist. No earlier holdout findings, coordinator scientific summary, hints or running metrics enter later contexts. Context receipt flags are evidence about dispatched inputs, not an OS-wide proof. A leak stops validation and conserves remaining holdouts.

Critical gate remains zero detected errors left accepted; zero unresolved material facts counted supported; zero invalid support locators, unsupported global rankings, wrong derived values, unsupported compound components, silently harmonized source conflicts or automatically consolidated research objects; zero software human approvals and zero live scientific-state mutation.

B01 development reruns are not untouched validation. Success is known failures corrected or fail-closed, with no demonstrated regression, not proof of generalization. AI-only future holdout success is capped at PASS_WITH_LIMITATIONS and conditional Phase5 readiness. Separate authorization is required to resume, rehearse or deploy.
'''}
for name,text in docs.items():
    md(name,text);d=C/'deploy_payload/protocols'/name;d.parent.mkdir(parents=True,exist_ok=True);d.write_text(text.strip()+'\n',encoding='utf-8')
for skill in ('paper-evidence-processing','verification-adjudication'):
    p=C/'deploy_payload/skills'/skill/'SKILL.md';t=p.read_text(encoding='utf-8')
    t=t.replace('[scientific evidence protocol](../../protocols/SCIENTIFIC_EVIDENCE_V3.md)','[proposition support protocol](../../protocols/PROPOSITION_SUPPORT_MODEL.md)')
    if 'Phase 4BR refinement' not in t:t+='\n## Phase 4BR refinement\n\nUse the [role model](../../protocols/SUPPORT_LOCATOR_ROLE_MODEL.md), [comparative protocol](../../protocols/COMPARATIVE_SUPPORT_PROTOCOL.md), [verification protocol](../../protocols/VERIFICATION_PROTOCOL_V3.md), and [pre-access receipt](../../protocols/PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md). Preserve source-reported facts separately from analyst inference and process provenance. Bind every material proposition, condition, comparison set and denominator to the required source elements. Do not treat one locator or a correct number as support for an entire compound statement. Repeated checks belong in support_v4.py and pre_access.py. No software review creates human approval.\n'
    p.write_text(t,encoding='utf-8')
md('SKILL_REMEDIATION_REPORT.md','''# Inactive skill remediation

Retained the five-skill decomposition; modified only paper-evidence-processing and verification-adjudication. Their positive triggers are extraction/support construction and source/relationship verification. Negative triggers include approving scientific state, installing skills, corpus-wide generation, and operational migration. Coordinator, taxonomy/synthesis and gap/RQ skills retain their prior responsibilities.

New conditional references cover proposition origin, support roles, comparative scopes, source-bound denominators and pre-access timing. Deterministic logic is in scripts. No active .agents/skills or AGENTS.md was written. This is an inactive payload, not an installation or model-behavior validation claim. Frontmatter/reference checks and explicit trigger-case review are recorded in test results.
''')
a=json.loads((O/'B01_SUPPORT_ADJUDICATION.json').read_text(encoding='utf-8'))
counts=collections.Counter(r for x in a['adjudications'] for r in x['root_causes'])
tax={'scope':'B01 source-adjudicated development findings; multi-label counts do not sum to 80','classes':[{'root_cause':k,'affected_challenges':v} for k,v in sorted(counts.items())], 'additional_generalized_gates':['COMPARISON_SCOPE_UNSUPPORTED','VALUE_SUPPORTED_RANKING_UNSUPPORTED','COMPARISON_SET_UNSUPPORTED','CONTEXT_ONLY_TREATED_AS_SUPPORT','TABLE_CELL_NOT_BOUND','APPENDIX_RECONCILIATION_MISSING','UNBOUND_DENOMINATOR','INFERENCE_ALIASED_TO_SOURCE_FACT']}
(O/'B01_SUPPORT_ROOT_CAUSE_TAXONOMY.json').write_text(json.dumps(tax,indent=2)+'\n',encoding='utf-8')
md('B01_SUPPORT_ROOT_CAUSE_TAXONOMY.md','# B01 support root causes\n\nMulti-label, source-adjudicated counts. These are 80 challenges, not 80 proven claim errors.\n\n| Root cause | Challenges |\n|---|---:|\n'+'\n'.join(f'| {k} | {v} |' for k,v in sorted(counts.items()))+'\n\nSchema/validator regression classes additionally cover unbound denominators, inferred-versus-source facts, local/global scope, ranking, context-only support, missing comparison rows and source conflicts. Synthetic fixtures generalize these defects rather than copying paper tables.')
md('B01_SUPPORT_ADJUDICATION.md','''# B01 source adjudication

All 80 challenged critical decisions have unique records and private exact-source evidence. Distribution: 58 LOCATOR_ONLY_DEFECT, 20 BOTH_PARTIAL, 1 UNRESOLVED, 1 PRIMARY_CORRECT; all other disposition categories zero. Claim and locator correctness are separate fields. The source, not verifier majority, controls this model-based development adjudication.

Fifteen benign-utility values were correctly transcribed but inherited an attack condition/security denominator. Correct them to no-attack utility over user tasks. Thirty other table-cell challenges require separate metric/condition support while retaining table-specific experimental scope. Most remaining challenges combine facts drawn from several pages.

CH036 is a false verifier flag: UTF-8 source data has the correct accented author name. CH010 cannot establish document-wide absence from its original locator. CH043/046/059 retain unresolved broad absence/coverage qualifiers. CH065 and CH070 explicitly separate analyst inference from directly reported facts. CH080 binds the DOI to the dataset record. PDF creation metadata and external-link noninspection are separate artifact/process provenance, not paper-page evidence.

The JSON/CSV crosswalk identifies every original item, proposition mapping, source reference, review finding, revised rule and fixture. Exact original claims and full source pages are in NEVER_PACKAGE private records; public entries contain paraphrases and hash-bound references. Whole-page text hashes prove byte consistency only; entailment and table transcription remain model source judgments. No qualified human ground truth was obtained.

Original Phase4B validator rejection remains preserved. The new graph permits different value/rank/scope locators while requiring all relevant source elements. Four table-local rankings are tested as separate claims. Original scientific acceptance is not retroactively granted, and B01 never returns to untouched status.
''')
md('SCHEMA_MIGRATION_NOTE.md','''# Schema and methodology migration

scientific_evidence_v4.schema.json version 4.0.0 is a breaking graph contract. Methodology phase4br-scientific-v3.0.0 is distinct from schema version. No v3 artifact is modified or automatically accepted. New origin, support requirement, role, support-set, entailment, comparison and source-bound denominator semantics require explicit reconstruction and source review. Legacy v3 code/tests remain pinned and runnable for compatibility comparison; future validation uses v4 gate explicitly.

Historical metadata and source bytes remain private. All current live state remains authoritative. This package has no production trust backend and no authorization to install or migrate. SQL schema and authority model are unchanged.
''')
print('Design protocols and inactive skill references written')
