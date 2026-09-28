"""Derive handoff reports from completed, fingerprint-matched evidence."""
from pathlib import Path
import sys,json
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
def put(n,v):(O/n).write_bytes(canonical(v))
def md(n,t):(O/n).write_text(t+'\n',encoding='utf-8')
new=read(O/'REAL_SOURCE_CONTINUITY_TEST_RESULTS.json');demo=read(O/'test_results/RETAINED_REAL_E2E.json')
assert new['failed']==0 and new['tests']==40 and new['integration_sha256']==demo['integration_sha256']==codehash()
inherited=[read(p) for p in sorted((O/'test_results').glob('INHERITED_*.json'))];assert all(x['failed']==0 for x in inherited)
firewall=read(O/'test_results/FIREWALL_ACCEPTANCE.json');assert firewall['failed']==0 and firewall['integration_sha256']==codehash()
totals={'inherited':sum(x['tests'] for x in inherited),'new':new['tests']+firewall['tests'],'new_core':new['tests'],'new_post_freeze_acceptance':firewall['tests'],'passed':new['passed']+firewall['passed']+sum(x['passed'] for x in inherited),'failed':0,'skipped':sum(x['skipped'] for x in inherited),'retained_real_demonstrations':1,'skip_reason':'Native real symlink creation unavailable on Google Drive; unchanged inherited skip, previously superseded by approved platform-independent containment policy; not counted as pass','interrupted_attempts_counted':False}
assert totals=={**totals,'inherited':154,'new':45,'passed':198,'skipped':1}
put('test_results/FINAL_TEST_SUMMARY.json',totals)
manifest={'version':VERSION,'sha256':codehash(),'files':code_manifest(),'hash_scope':'canonical sorted aggregate of listed code, schema, tests, worker contract and parent execution dependencies; third-party manifest pins additionally verified actual inventory'};put('INTEGRATION_MANIFEST.json',manifest)
e=Engine(O/'recovery_receipts')
with e.lock('phase4bd-implementation-finalization'):
 current=e.state()
 if current['last_committed_milestone'] is None:
  assert current['current_atomic_unit_id']=='IMPLEMENT_REAL_SOURCE_INTEGRATION'
  e.commit({'outputs/integration_manifest.json':canonical(manifest),'outputs/test_summary.json':canonical(totals)},next_operation='REPORTS_PRESERVATION_REVIEW_PACKAGE')
 else:assert filehash(e.root/'outputs/integration_manifest.json')==filehash(O/'INTEGRATION_MANIFEST.json')
md('FAILURE_BOUNDARY_TEST_REPORT.md','''# Failure boundaries

The completed real-source suite covers all required A–G boundaries using consumed B01. Tests 01–03 reject before acknowledgement, before pre-access, and before access respectively. Test 04 commits irreversible consumption then aborts before helper delivery. Tests 05–06 interrupt during delivery and after output generation but before unit commit; recovery quarantines incomplete attempts. Test 07 returns a committed unit without replay. Tests 21–22 recover an event-before-projection crash and a deliberately stale untouched projection without undoing consumption.

Tests 13–20, 27, 30–38 reject identity, protocol, stage and authority-chain problems. Tests 34–35 include malformed-but-committed/receipt-linked records, not only changes caught by a file hash. Private test corruption is invented or confined to copied development runtime; no prior phase or source is altered.

These are process-level fault injections, not arbitrary-power-loss tests. A committed access event before failed delivery intentionally leaves B01 consumed. Source-derived results and diagnostic scratch remain NEVER_PACKAGE. See REAL_SOURCE_CONTINUITY_TEST_RESULTS.json for exact test IDs and integration fingerprint.''')
md('FRESH_SESSION_RECOVERY_REPORT.md',f'''# Fresh-process recovery

PASS for the scoped development transport. Test 39 and test_results/RETAINED_REAL_E2E.json launch cli.py in a new coordinator process after extraction commits and a second unit is preempted. Original coordinator PID: {demo['original_coordinator_pid']}; new PID: {demo['fresh_coordinator']['pid']}. The CLI reconstructs configuration, packet, receipt chain and consumed state from files. It starts a fresh worker and commits the verification unit without hidden conversation state.

The retained run has one access event, one consumption receipt and one commit for each of EXTRACTION and VERIFICATION. The private results agree on field value and source-bound locator; only hashes and equality measurements are exported. The usage interruption is simulated, not an estimate of account allowance. This is a deterministic source-derived atomic unit, not model scientific review.''')
md('IDEMPOTENCY_REPORT.md',f'''# Idempotency

PASS. Tests 07 and 10–12 exercise committed-unit, repeated recovery, acknowledgement and pre-access replay. The retained process demonstration verifies unique authoritative unit IDs, {demo['source_access_events']} source-access event, {demo['consumption_receipts']} consumption receipt, {demo['extraction_commits']} extraction commit and {demo['verification_commits']} verification commit. A second fresh-process recovery adds diagnostics, not another scientific effect.

Fresh worker contexts may have their own acknowledgement receipts; they do not replace or duplicate the original report access transition. Uncommitted attempts are quarantined and safely recomputed only for the same authorized source, packet and pins. No generic exactly-once guarantee for arbitrary external effects is claimed.''')
md('CONTEXT_FIREWALL_RECOVERY_REPORT.md','''# Recovery context firewall

The worker is a fresh deterministic subprocess with a closed input header: exact approved packet, source/report identity, size, stage, context ID and wrapper hash, followed by the authorized current PDF bytes. Recovery narratives and coordinator history are never serialized into this input. Unknown header keys fail. It inherits operating-system permissions and environment; this is not an OS sandbox or independent human review.

The separate-context packet reviewer inspected exact packet and wrapper bytes and returned SEMANTIC_CONTEXT_CLEAN. Only B01 and its report ID in two current-binding fields receive the narrowly reviewed identity exception. Tests 24–25 reject injected historical narrative and a B01 identifier in the content body. Inherited context tests cover other forbidden examples and historical leakage. Static scanning and model review have detection limits; exact reconstruction prevents later contextual additions rather than claiming universal paraphrase detection.

Known runtime hardening limitations are preserved in the protocol and independent review. No diagnostic reviewer serves as a scientific validation worker. B02–B08 never enter worker source delivery.''')
put('INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json',{'status':'NO_SCOPED_CODE_BLOCKER_CONDITIONAL_ON_FINAL_TESTS','reviewer':'/root/real_integration_review','mode':'READ_ONLY_MODEL_TECHNICAL_REVIEW','source_access':False,'writes':False,'scientific_or_human_approval':False,'initial_findings':['stage/result mismatch','actual dependency pinning','helper event identity','semantic review pins','derived continuity evidence','cross-record binding checks'],'revisions_reviewed':True,'conclusion':'No remaining blocker identified for narrowly scoped already-consumed B01 transport/recovery test, conditional on pending suite passing against final frozen bytes.','limitations':['Dependency-root Windows reparse/junction ancestor checks not explicit','Worker assert checks may be disabled by optimized-Python environment; startup ACK read lacks timeout','Fresh processes inherit environment and filesystem permissions; not OS sandbox','Hash chains are not authentication against rewrite of all authority files'],'interrupted_review':'One reviewer turn hit usage limit; later read-only review completed','final_suite_passed':True,'final_integration_sha256':codehash(),'final_artifact_review':'PENDING'})
put('REQUIREMENTS_TRACEABILITY.json',{'phase':'PHASE4BD','sections':[{'requirement_section':n,'evidence':(['PHASE4BD_BASELINE.json','PRESERVATION_CHECK.json'] if n in [2,3,4,22,25,30] else ['REAL_SOURCE_INTEGRATION_FIXTURE.json'] if n==5 else ['REAL_SOURCE_CONTINUITY_PROTOCOL.md','REAL_SOURCE_CONTINUITY_TEST_RESULTS.json','test_results/RETAINED_REAL_E2E.json'] if n in list(range(6,21))+[23,24] else ['REAL_SOURCE_HELPER_INTEGRATION_REPORT.md'] if n==21 else ['INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json'] if n==26 else ['PACKAGE_MANIFEST.json','PACKAGE_RECEIPT.json'] if n==31 else ['FINAL_HANDOFF.json','PHASE4B_RESUME_READINESS_FINAL.md'])} for n in range(1,36)],'all_scientific_validation_claims':False})
print(json.dumps({'integration_sha256':codehash(),'tests':totals,'next':'PRESERVATION_AND_FINAL_REVIEW'}))
