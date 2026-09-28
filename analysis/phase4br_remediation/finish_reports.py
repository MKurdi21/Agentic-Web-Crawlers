import json,collections
from pathlib import Path
O=Path(__file__).resolve().parent
def read(n):return json.loads((O/n).read_text(encoding='utf-8-sig'))
def write(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def md(n,t):(O/n).write_text(t.strip()+'\n',encoding='utf-8')
m=read('REMEDIATION_DEVELOPMENT_METRICS.json');cfg=read('REMEDIATED_WORKFLOW_CONFIGURATION.json');tests=read('test_results/UNIT_INTEGRATION_RESULTS.json');reg=read('test_results/B01_REGRESSION_RESULTS.json');pres=read('PRESERVATION_CHECK.json');reserve=read('PHASE4B_RESUME_HOLDOUT_MANIFEST.json')
assert m['development_gate_passed'] and pres['passed'] and tests['failed']==0 and read('test_results/INDEPENDENT_EQUIVALENCE_CHECK.json')['passed']
inherited=sum(not x['test'].startswith(('test_support_v4.','test_b01_generalized.','test_validation_guard.')) for x in tests['tests']);assert inherited==86
md('REMEDIATION_DEVELOPMENT_RESULTS.md',f'''# B01 development evaluation

Evaluation: REMEDIATION_DEVELOPMENT_EVALUATION, not untouched or independent scientific validation. Frozen method: {cfg['methodology_version']}; SHA-256 `{cfg['methodology_sha256']}`.

All 131 original items (127 critical) are accounted for. The 135 evaluated graphs contain 458 material propositions, including seven explicitly marked analyst inferences and four separately checked local rankings. No critical unknown or inferred proposition is silently counted as a direct supported source fact.

Of the 80 challenged decisions, 73 have corrected claims or completed locators, six are explicitly qualified/fail-closed, and one original decision was correct. This does not mean 80 true claim errors. Claim correctness: 59 correct, 20 partial, one unresolved. Locator correctness: 32 compound-incomplete, 46 partially supporting, one unresolved, one fully supporting. Ground-truth critical false accepts remain UNKNOWN.

Known detected false support or locator failures left fully supported: zero under this development review. This is a bounded model-based finding, not proof that no undiscovered error exists. No artifact received production scientific acceptance.

Previously supported cohort: {reg['previously_correct']} items (44 critical, one noncritical), independently reconciled by identity. Still correct: {reg['still_correct']}; improved/decomposed: {reg['improved']}; narrowed: {reg['narrowed']}; regressed: {reg['regressed']}; newly unresolved: {reg['now_unresolved']}. Cohort membership originated in the prior verifier and was source-rechecked for development; it is not human ground truth. Additional persistence absence was corrected outside the 80 challenges.

All {tests['tests_run']} executable tests passed ({inherited} inherited, {tests['tests_run']-inherited} new), zero failed/skipped. Original safety-test files are byte-identical. An initial environment setup run had two packaging-test errors due to missing protected-hash input; supplying the real baseline corrected these without weakening tests. Synthetic unit fixtures include database/backup safety tests, as required by the inherited suite; no live-data migration, Lane B, or backup/restore rehearsal occurred.

The final pre-access receipt precedes source release; immutable candidate bytes match before/after evaluation. Separate record/count/arithmetic/hash checks are in test_results/INDEPENDENT_EQUIVALENCE_CHECK.json. Exact source bodies and full-table development graphs remain private. The graph validator cannot infer scientific entailment from page hashes or automatically prove inventory completeness.

The review found and corrected missing inference origin, unsupported denominator, role-union loopholes, residual compound records, and omitted source components. Their negative tests reject those known failure modes. Remaining scientific/governance limitations are explicit in the resume plan. B01 is permanently consumed development evidence.
''')
md('REVIEW_FINDINGS_AND_RESOLUTIONS.md','''# Read-only review findings and resolutions

Reviewer: separate Codex context /root/phase4br_final_review, explicitly authorized by the user. This is technical/source-adjudication review, not independent human scientific review. It accessed no B02-B08 substantive content and made no writes.

1. Analyst inference lacked structured origin: added required origin/rationale and INFERENCE_GROUNDED; full source support cannot be granted to inferred/process assertions. CH065/CH070 updated.
2. Percentage denominator could be an unsupported scalar: added denominator element identity, exact value matching and source-role binding.
3. Derivation/comparison checks borrowed unrelated support roles: now require DERIVATION_INPUT, RANKING_SUPPORT, COMPARISON_SET_SUPPORT, SCOPE_SUPPORT and VALUE_SUPPORT specifically.
4. DEV030/047/049 remained composite: decomposed numbers and experiment/version qualifiers explicitly.
5. CH074 omitted source components: restored four environments and synthetic data; also audited other omissions.

The reviewer verified the corrections and found no remaining blocker in them; 135 graph prechecks passed. Final reports and package are subject to the external INDEPENDENT_FINAL_REVIEW.json receipt. One earlier reviewer attempt hit a usage limit; work was preserved and resumed, not falsely marked reviewed.

Page text hashes prove page-byte integrity, not cell transcription or entailment. Application receipts prove recorded ordering, not OS-wide access isolation. These limitations are retained rather than disguised by passing tests.
''')
md('PHASE4B_RESUME_PLAN.md',f'''# Resumed Phase 4B — preparation only

No resume is authorized by this file. Proposed validation type: SEQUENTIAL_RESERVED_HOLDOUT_VALIDATION. Candidate methodology `{cfg['methodology_version']}`, fingerprint `{cfg['methodology_sha256']}`; evidence schema 4.0.0. B01 is excluded permanently from untouched validation and retained only as development evidence. This is a seven-report reserved remainder after B01-driven remediation, not the original eight-report validation cohort and not a representative corpus accuracy estimate.

After separate user authorization, verify the prior archives, new package receipt, methodology/configuration, candidate code and dependency manifests. Reconfirm source hashes and recorded untouched status for B02-B08 without inspecting scientific content. Reuse is supported by audited access/context records and confined work, not an OS-wide assertion. If contamination is discovered, exclude the report and document it; never silently replace it.

Order remains B02 → B03 → B04 → B05 → B06 → B07 → B08. For each report, verify immutable execution-copy equality; create a fresh primary context with fork_history=none; commit its durable report-bound PRE_ACCESS_RECEIPT before substantive access; record SOURCE_ACCESS_BEGAN separately. Complete primary fields, result inventory, atomic support graph, typed roles, quantitative checks, separate-context verification, disagreement handling and mandatory gate before opening the next report. Fresh verifier packets contain only current source/item/protocol inputs, no earlier findings or coordinator persuasion. If meaningful isolation cannot be established, stop before opening another source.

Apply v4 scientific validation explicitly; legacy operational evidence acceptance cannot substitute for it. Full source support requires all material propositions and roles; inferred statements retain origin and cannot alias reported facts. Use rendered tables/figures where needed. Bind all operands/denominators; inventory relevant result scopes before maxima/minima. Preserve conflicts, absence reasons, partials and unknowns. Verify every critical item and the frozen deterministic lower-risk sample; freeze sample membership after the complete eligible set and before review.

Retain the mandatory zero-accepted-known-error gate: no unresolved critical fact supported, invalid locator accepted, numeric disagreement silently correct, local result promoted global, incorrect derived value, unsupported material compound component, silently resolved source conflict, automatic contribution merge, software human approval, or live scientific mutation. Any mandatory failure stops immediately and preserves later reports untouched. Never tune against opened holdouts and continue; a relevant change consumes exposed evidence for development and requires an explicitly versioned new validation design.

Named denominators must distinguish selected/opened/completed/consumed/unrun/untouched reports, fields, items, propositions and criticality. Before/after each report, compare immutable manifest and dependency hashes. Runtime mutation is checked separately. No silent re-freeze.

AI-only success is capped at HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS. Model agreement is not independent human review or production trusted approval; ground-truth false accepts remain UNKNOWN. Human-required production transitions fail closed. Owner decisions on storage, trusted reviewers, thresholds, contribution authority, inclusion/partial synthesis, taxonomy, retention, scoring and external search remain unresolved unless separately approved.

Lane B stays NOT_RUN_GATE_BLOCKED until the entire eligible reserved sequence succeeds without a mandatory blocker and separate execution authorization covers the rehearsal. If reached later, retain fresh runtime, read-only lossless import, independent equivalence, semantic idempotency, stale/replay/source-mutation tests, separate SQLite integrity/foreign-key checks, store reconciliation, quiesced matching database/artifact snapshot, concurrent-acceptance boundary tests, paired restore/rollback and single-writer cutover simulation. None of that ran in Phase4BR.

No live migration, authority switch, promotion, checkpoint refresh, installed skills or Phase5 execution is authorized. Phase5 requires explicit owner authorization even after conditional technical readiness.
''')
md('PACKAGE_POLICY.md','''# Package isolation and receipt policy

The convenience ZIP is constructed from explicit root filenames, the frozen immutable candidate inventory, named sanitized test reports, and synthetic fixture JSON. Never recurse over the entire design tree. Exclude private source snapshots, full text, summaries, page images, copied tables, private development graphs, runtime databases/blobs/backups, dependencies/cache directories, credentials and prior archives.

PACKAGE_MANIFEST.json contains exact path/size/hash inventory. Its own bytes are an explicitly named self-member; it does not hash itself. HANDOFF_SNAPSHOT.json is an immutable package-time handoff. FINAL_HANDOFF.json, PACKAGE_RECEIPT.json and INDEPENDENT_FINAL_REVIEW.json are external completion receipts so the ZIP hash never requires a circular self-hash. The external final handoff is authoritative for completed archive validation/readiness.

The independent validator reopens the archive, checks CRC and every hash/member, rejects traversal, case collisions, duplicates, private/runtime paths, known protected source hashes and binary/article signatures. It does not import builder functions. Content scanning has limits; constrained output generation and physical private separation are primary controls. Metadata references to private paths are allowed; the referenced bytes are not packaged.
''')
md('EXECUTIVE_PHASE4BR.md',f'''# Phase 4BR remediation handoff

B01 remediation gates pass, subject to the final external package/review receipts. See FINAL_HANDOFF.json for final classification; this immutable packaged report does not authorize execution.

80/80 challenges source-adjudicated: 58 locator-only, 20 both-partial, one unresolved and one primary-correct. 73 corrected/completed, six qualified/fail-closed, one false verifier flag. No known detected support failure remains fully supported under the development protocol; human ground truth is UNKNOWN.

Generalized support graph and typed roles, explicit inference provenance, source-bound denominators, scoped ranking checks and durable pre-access receipts are implemented. All {tests['tests_run']} tests pass, including all 86 inherited tests unchanged. Development regression cohort: 45 items, zero regressions. New methodology `{cfg['methodology_version']}` / `{cfg['methodology_sha256']}`.

All 8,993 protected paths (including the original 5,737) were unchanged with zero missing. B02-B08 remain seven untouched reserved reports under recorded-access evidence; contamination count zero. Proposed resume starts B02 after separate authorization. No live scientific promotion, migration, installation or Lane B occurred. Source-verified=0; promoted=0. This is a development candidate, not scientific validation or deployment readiness.
''')
handoff={'phase':'PHASE4BR','classification':None,'candidate_classification':'READY_TO_RESUME_PHASE4B_AT_B02','completion_status':'AWAITING_FINAL_PACKAGE_AND_REVIEW_RECEIPTS',
 'b01':{'challenges_total':80,'challenges_adjudicated':80,'primary_correct':1,'verifier_correct':0,'both_partial':20,'both_incorrect':0,'locator_only_defects':58,'claim_only_defects':0,'unresolved':1,'source_ambiguous':0,'ground_truth_critical_false_accepts':'UNKNOWN'},
 'support_model':{'methodology_version':cfg['methodology_version'],'methodology_sha256':cfg['methodology_sha256'],'proposition_support_enabled':True,'locator_roles_enabled':True,'compound_support_sets_enabled':True,'comparative_scope_gate_enabled':True,'inference_origin_separated':True},
 'development_rerun':{'critical_items':127,'original_items':131,'graphs':135,'propositions':458,'original_failures_corrected':73,'qualified_or_fail_closed':6,'original_decision_correct':1,'false_accepts_left_accepted':0,'locator_failures_left_accepted':0,'regressions':0,'scope':'Known detected defects only; model development evaluation, not human ground truth or untouched validation'},
 'tests':{'inherited':inherited,'new':tests['tests_run']-inherited,'passed':tests['passed'],'failed':tests['failed'],'skipped':tests['skipped']},
 'resume_holdout':{'reserved_reports':7,'report_ids':[x['report_id'] for x in reserve['reports']],'untouched_count':7,'contamination_count':0,'resume_start_id':'B02','proof_limit':'Controlled task/access records and source hashes; not OS-wide attestation'},
 'receipt_protocol':{'pre_access_receipt_required':True,'timing_tests_passed':True},'live_state':{'source_verified':0,'promoted':0},'lane_b_executed':False,'phase4b_resume_authorized':False,'live_migration_occurred':False,'skill_installation_occurred':False,'independent_review_status':'CORRECTIONS_REVIEWED_FINAL_ARCHIVE_REVIEW_PENDING','preservation_passed':pres['passed'],'package':{'path':str(O.parent/'phase4br_remediation_package.zip'),'sha256':None,'external_receipt':'PACKAGE_RECEIPT.json'}}
write('FINAL_HANDOFF.json',handoff);write('HANDOFF_SNAPSHOT.json',handoff)
print('Final reports prepared; release receipts still pending')
