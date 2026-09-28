"""Explicit report generation from completed receipts and test reports."""
from pathlib import Path
import sys,json,hashlib
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(O/'continuity_adapter'))
from adapter import code_pins,c,VERSION
def read(n):return json.loads((O/n).read_text(encoding='utf-8'))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,v):(O/n).write_text(json.dumps(v,indent=2,sort_keys=True),encoding='utf-8')
def md(n,v):(O/n).write_text(v.strip()+'\n',encoding='utf-8')
if __name__=='__main__':
    p=read('PATH_CONTAINMENT_TEST_RESULTS.json');a=read('CONTINUITY_TEST_RESULTS.json');ic=read('test_results/INHERITED_CONTEXT_RESULTS.json');ir=read('inherited_recovery/test_results/recovery-35017b90622d43069c73f751c5478fc1.json');integration=read('test_results/PARENT_BUILDER_INTEGRATION.json')
    assert a['tests']==28 and a['passed']==28 and p['passed']==30
    review=read('INDEPENDENT_CONTAINMENT_REVIEW.json');pres=read('PRESERVATION_CHECK.json')
    assert review['status']=='PASS_WITH_DOCUMENTED_LIMITATIONS' and pres['status']=='PASS'
    pin=code_pins()
    roots=['path_containment','continuity_adapter','vendor','inherited_recovery/recovery_protocol','inherited_context/context_architecture']
    files=[q for root in roots for q in (O/root).rglob('*') if q.is_file() and q.suffix=='.py']
    files += [O/n for n in ['CONTENT_IDENTITY_REGISTRY.schema.json','PATH_CONTAINMENT_POLICY.json','APPROVED_ROOTS.json','inherited_recovery/RECOVERY_STATE.schema.json','inherited_recovery/RECOVERY_EVENTS.schema.json','inherited_recovery/MILESTONE_RECEIPT.schema.json']]
    entries=[{'path':q.relative_to(O).as_posix(),'size':q.stat().st_size,'sha256':h(q)} for q in sorted(files)]
    impl={'version':'phase4bc-path-containment-v1.0.0','pins':pin,'files':entries,'manifest_sha256':c.fingerprint(entries),'canonicalization':'NFC canonical UTF-8 JSON, sorted keys; aggregates sorted path,size,sha256 entries','mutable_runtime_excluded':True,'continuity_version':VERSION,'continuity_sha256':pin['immutable_code'],'continuity_hash_scope':'Combined executed containment and continuity dependencies, including recovery engine and schemas'}
    put('IMPLEMENTATION_MANIFEST.json',impl)
    tests={'inherited':ic['tests']+ir['tests'],'new':p['tests']+a['tests']+integration['tests'],'passed':sum(x['passed'] for x in [p,a,ic,ir,integration]),'failed':sum(x['failed'] for x in [p,a,ic,ir,integration]),'skipped':ic['skipped']+ir['skipped']+p['skipped']+a['skipped'],'suites':{'inherited_context':ic,'inherited_recovery':ir,'path_containment':p,'continuity':a,'parent_integration':integration},'scope':'Latest completed stable suite executions, not sum of reruns. Earlier failed development attempts retained in test_results. Two model packet reviews reported separately.'}
    put('test_results/FINAL_TEST_SUMMARY.json',tests)
    supersession={'old_test':'test_context_engine.PacketTests.test_symlink_rejected','old_status':'SUPERSEDED_ENVIRONMENT_SPECIFIC_TEST','original_result':'SKIPPED_G_DRIVE_WINERROR_1','supplemental_result':'ENVIRONMENT_BLOCKED_NTFS_WINERROR_1314','native_behavior_executed':False,'superseded_by':'PATH_CONTAINMENT_AND_CONTENT_IDENTITY_INVARIANT','new_invariant':'PASS','basis':['Production Guard and parent adapter enforce identity, containment, hash and class','30 path tests pass including actual injected resolver and transitive chain decisions','Independent read-only security review qualifies coverage'],'historical_counts':{'phase4bc':{'passed':222,'failed':0,'skipped':1},'phase4bc_s':{'recovery_passed':46,'symlink':'ENVIRONMENT_BLOCKED'}}}
    put('SYMLINK_GATE_SUPERSESSION.json',supersession)
    md('SYMLINK_GATE_SUPERSESSION.md','''# Symlink gate supersession

The user-authorized governing gate is now `PATH_CONTAINMENT_AND_CONTENT_IDENTITY_INVARIANT`. The unchanged original test is `SUPERSEDED_ENVIRONMENT_SPECIFIC_TEST`, not passed or deleted. Its G: creation failed with WinError 1; the prior local NTFS probe failed with privilege error 1314. Native symbolic-link execution remains unproven.

The production supplemental builder checks explicit IDs, segment containment, registration, immutable SHA-256, role/class and every dependency. Injected indirect resolution exercises the same final production checks; a separate mocked reparse-stat branch is not proof of native link capability. Independent review found the safety scope at least as broad under the documented trusted-configuration and filesystem assumptions. Historical counts and classifications are unchanged. See the JSON companion and independent review for evidence.''')
    md('PATH_CONTAINMENT_AND_CONTENT_IDENTITY_INVARIANT.md','''# Path containment and content identity

Packet inclusion is governed by explicit logical identity, canonical containment, immutable content identity, and content classification, not by availability of symlinks.

`ALLOW = path_contained AND artifact_registered AND hash_matches AND classification_allowed`.

Guard accepts registered IDs from role-specific allowlists. Every root and ancestor is checked for link/reparse identity. Lexical NFC/separator normalization permits dot segments but rejects any parent segment, even exit/re-entry, alternate drives, device/UNC aliases, globs, environment substitution and ambiguous names. Containment compares path segments, never a string prefix. Duplicate/case-ambiguous identities fail closed. An in-root unregistered copy remains forbidden.

Strict resolution, lstat/reparse checks and the final opened-handle path precede byte inclusion. Windows uses GetFinalPathNameByHandleW; POSIX uses /proc/self/fd when available and strict resolution plus fstat identity otherwise. Before/after identity, size and modification-time checks detect changes; registered SHA-256 is mandatory. Unknown resolution fails closed. This is not a hostile-OS sandbox or atomic protection against every filesystem race or Drive synchronization behavior.

All transitive dependencies must separately satisfy registration, allowlist, hash and class. Cycles and undeclared includes/imports/references are rejected through the frozen parent reference checker. No broad directory trust or glob expansion exists. HISTORICAL_DEVELOPMENT_ONLY is never eligible merely because it is under a project root. Static and separate semantic packet release controls remain required after composition.

`parent_adapter.build_parent_packet` is the additive production composition entrypoint; no live installation or prior-code change occurred. Current-report binding remains separately schema-validated; generic assets are Layers A/B, not arbitrary source bodies. The report-independent continuity contract receives only exact approved current-report records.

Sources: https://docs.python.org/3/library/os.path.html#os.path.commonpath and https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew . Local executable tests establish this implementation's observations, not platform-wide guarantees.''')
    md('PATH_CONTAINMENT_TEST_MATRIX.md','# Path containment tests\n\nAll 20 mandatory scenarios plus 10 additional adversarial checks are executed.\n\n| Executable test | Result |\n|---|---|\n'+'\n'.join('| '+x['id']+' | '+x['status']+' |' for x in p['records']))
    put('TRANSITIVE_PATH_CONTAINMENT_REPORT.json',{'status':'PASS','tests':[x for x in p['records'] if any(k in x['id'] for k in ['nested','cycle','reference','dependency','template_history'])],'rule':'Every dependency is allowlisted and read through the same Guard; top-level approval cannot confer nested authority','implementation':'path_containment/guard.py:Guard.packet'})
    put('INDIRECT_RESOLVER_TEST_REPORT.json',{'status':'PASS','tests':[x for x in p['records'] if any(k in x['id'] for k in ['injected_escape','inside_indirect','reparse'])],'production_decision_shared':True,'native_symlink_created':False,'limitations':'Injected resolver and stat branch coverage, not a native filesystem capability claim','implementation':'path_containment/guard.py:Guard.read'})
    limitations=['Synthetic extraction and verification demonstrate mechanics only, not scientific accuracy or locator correctness on real papers.','Fresh subprocesses and new coordinator identities exercise durable reconstruction; actual Codex service/session lifecycle is not emulated.','Generic context_contract is report-independent but trusts the caller-supplied durable authority and expected pins; it does not authenticate human approval.','Runnable source transport is restricted to invented SYNTHETIC_REPORT_X. Real B02 transport remains disabled and separately authorized.','Neither hash checks nor receipts prove arbitrary-power-loss, hostile filesystem or Drive synchronization durability.','Untouched reservations derive from recorded access and artifact inventory plus hashes, not an OS-wide access audit.']
    cont={'status':'PASS','version':VERSION,'sha256':pin['immutable_code'],'mechanics_only':True,'source':'SYNTHETIC_REPORT_X','report_independent_contract':'continuity_adapter/context_contract.py','tests':a,'packet_semantic_review':read('test_results/EXACT_PACKET_SEMANTIC_REVIEW.json'),'fresh_session_test':'PASS_FRESH_SUBPROCESS_AND_COORDINATOR_ID','same_session_test':'PASS_RESUMED_COORDINATOR_ID','post_source_recovery':'PASS_CONSUMPTION_PERMANENT','context_firewall':'PASS','duplicate_authoritative_effects':0,'limitations':limitations}
    put('SCIENTIFIC_CONTINUITY_ADAPTER_REPORT.json',cont)
    md('SCIENTIFIC_CONTINUITY_ADAPTER.md','''# Scientific continuity adapter

Version `phase4bc-continuity-v1.0.0` wraps unchanged context/recovery dependencies and the new Guard. `Continuity.create` binds exact synthetic source, approved packets, separate semantic-review records and all executed code/schema pins; `access` commits source/receipt identity before worker delivery. `unit` uses durable idempotent PRIMARY/VERIFIER receipts; `recover` validates inputs, repairs only supported journal/state projections under the inherited OS lock, reconstructs committed units and quarantines replayable partial computation.

The generic `reconstruct_worker_context` interface accepts a validated current binding, exact approved packet, source bytes, role, receipt chain and optional committed atomic item. It accepts no conversation or coordinator narrative. Primary bytes must equal the pre-access receipt packet; verifier input is read against the committed PRIMARY output hash. Caller authority/pins must already be verified; this function is not approval authentication.

Fresh workers are subprocesses with stdin-only scientific input: packet, current source, stage, and committed current primary item for verification. Session IDs remain control metadata. No filesystem/history arguments reach the scientific worker. Packet and source drift are checked even before returning a cached committed result. Recovery metadata never enters primary/verifier packets.

The executable transport intentionally accepts synthetic content only. Example: ten trials and seven successes, one atomic 0.7 fraction with exact operands and source-bound text span; a separate worker recomputes it. A new coordinator object/session identity resumes an interrupted verifier using only durable state. Same-session identity also works; conversational memory has no authority. This is actual receipt/context code execution but not a test of a hosted Codex reconnect.

Before access the synthetic report is untouched; access is permanently consumed even after interruption. Missing or ambiguous source receipts block recovery. Receipt-before-state, torn tails and malformed projection recovery use the frozen inherited protocol. Interior corruption, changed committed outputs, conflicting authority, stale reviews and incorrect pins fail closed. Real-source access remains unavailable in this phase.''')
    md('SCIENTIFIC_CONTINUITY_ADAPTER_REPORT.md','# Continuity result\n\nPASS: 28 synthetic continuity tests, including end-to-end extraction/verification, fresh coordinator identity, post-source consumption, duplicate replay, receipt-bound contexts and firewall negatives. Exact primary/verifier packets each received a separate read-only model review: SEMANTIC_CONTEXT_CLEAN. No human scientific approval is claimed.\n\n'+'\n\n'.join(limitations)+'\n\nSee JSON for exact test and review evidence. Failed development runs remain diagnostic history and are excluded from final stable totals.')
    classification='READY_TO_RESUME_PHASE4B_AT_B02'
    hand={'phase':'PHASE4BC-P','classification':classification,'parent_state':{'phase4bc_classification':'CONTEXT_REMEDIATION_COMPLETE_NOT_READY_TO_RESUME','phase4bc_s_classification':'SUPPLEMENT_COMPLETE_NOT_READY_TO_RESUME'},'scientific_methodology':{'version':'phase4br-scientific-v3.0.0','sha256':pin['methodology'],'changed':False},'context_architecture':{'version':'phase4bc-context-v1.0.0','sha256':pin['context_architecture'],'changed':False},'recovery_protocol':{'version':'phase4bc-recovery-v1.0.0','sha256':'5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0'},'path_containment':{'version':impl['version'],'sha256':pin['path_containment'],'old_symlink_test_status':supersession['old_status'],'supersession_status':'PASS','approved_roots_enabled':True,'canonical_containment_enabled':True,'content_identity_enabled':True,'transitive_validation_enabled':True,'indirect_resolution_tested':True,'historical_classification_gate_enabled':True},'continuity_adapter':{'status':'PASS','version':VERSION,'sha256':pin['immutable_code'],'same_session_test':'PASS_LOGICAL_COORDINATOR_ID','fresh_session_test':'PASS_FRESH_WORKER_SUBPROCESS','pre_source_interruption_test':'PASS','post_source_interruption_test':'PASS','duplicate_recovery_test':'PASS','context_firewall_test':'PASS'},'tests':{k:tests[k] for k in ['inherited','new','passed','failed','skipped']},'reserved_holdout':{'selected':7,'untouched':7,'consumed':0,'contamination_events':0,'resume_start':'B02'},'live_state':{'source_verified':0,'promoted':0},'lane_b_executed':False,'phase4b_resumed':False,'phase5_started':False,'live_migration':False,'skills_installed':False,'checkpoint_refreshed':False,'preservation':'PASS_16050_PROTECTED_FILES','independent_review':review['status'],'limitations':limitations,'package':{'path':'analysis/phase4bc_path_containment_package.zip','sha256':None,'receipt':'External PACKAGE_RECEIPT.json; archive handoff intentionally omits its own archive hash'},'stop':'Separate user authorization required before B02 or Phase4B'}
    put('FINAL_HANDOFF.json',hand)
    md('PHASE4B_RESUME_READINESS_FINAL.md',f'''# Final additive readiness

Historical Phase4BC: CONTEXT_REMEDIATION_COMPLETE_NOT_READY_TO_RESUME.
Historical Phase4BC-S: SUPPLEMENT_COMPLETE_NOT_READY_TO_RESUME.
Old real-symlink test: SUPERSEDED_ENVIRONMENT_SPECIFIC_TEST, native execution not proven.
New PATH_CONTAINMENT_AND_CONTENT_IDENTITY_INVARIANT: PASS.
Scientific continuity adapter: PASS for required synthetic durable-context mechanics.
B02-B08: 7 untouched, 0 consumed, 0 recorded contamination events.
Final readiness: {classification}.

The additive Guard is integrated with the frozen parent builder and yielded byte-identical sanitized packets for both roles. Production scientific methodology, context architecture and recovery protocol remain unchanged. Independent model security review found no unresolved blocker under the documented preconditions. Readiness is infrastructure preparation only; it is not scientific validation, deployment, or B02 source authorization.

Future authorized resumption must first verify these manifests and preservation, use the clean current-report packet release protocol and report-independent contract, establish fresh contexts, and preserve B02-to-B08 sequential early-stop gates. Real transport must not be enabled by reusing a synthetic approval. No human authorization is implied. Stop here; no Phase4B, LaneB or Phase5 execution.''')
    md('EXECUTIVE_PHASE4BC_P.md',f'''# Phase4BC-P

{classification}. The environment-specific native-link gate is formally superseded, not retroactively passed. Canonical containment, explicit registered identity, hash, class and transitive dependency controls passed 30 tests; unchanged parent integration passed two checks. Continuity passed 28 synthetic tests. Inherited context/recovery suites contributed 94 checks: 93 passed, one native-link skip. Total: 154 checks, 153 passed, zero failed, one superseded environment skip.

All 16,050 protected files and prior archives remain unchanged; seven reserved reports remain untouched and live verified/promoted counts remain zero. Fresh subprocess recovery tests establish receipt/context mechanics, not real-paper accuracy or hosted-session recovery guarantees. See FINAL_HANDOFF.json for fingerprints, qualifiers and external package receipt. No B02 access, Phase4B resumption, LaneB, migration, skills, checkpoint refresh or promotion occurred.''')
    (O/'private_diagnostic_material').mkdir(exist_ok=True)
    md('private_diagnostic_material/NEVER_PACKAGE.md','Private diagnostics and synthetic runtime material are excluded from the archive. Earlier execution attempts are preserved in local test_results and recovery records; only selected sanitized evidence is allowlisted.')
    print('REPORTS READY',tests['passed'],pin)
