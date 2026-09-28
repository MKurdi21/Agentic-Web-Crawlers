import json,csv,hashlib
from collections import Counter
from pathlib import Path
O=Path(__file__).resolve().parent
def read(n):return json.loads((O/n).read_text(encoding='utf-8'))
def save(n,x):(O/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def h(n):return hashlib.sha256((O/n).read_bytes()).hexdigest()
cfg=read('CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');leaks=list(csv.DictReader((O/'CONTEXT_LEAKAGE_INVENTORY.csv').open(encoding='utf-8-sig')))
tests=[read('test_results/'+n) for n in ['INHERITED_TEST_RESULTS.json','CONTEXT_ENGINE_TESTS.json','SEMANTIC_CHALLENGE_RESULTS.json','INDEPENDENT_FINAL_CHECKS.json']]
tot={k:sum(x[k] for x in tests) for k in ['tests_run','passed','failed','skipped']};tot.update(inherited=tests[0]['tests_run'],new=sum(x['tests_run'] for x in tests[1:]))
save('test_results/TEST_TOTALS.json',tot)
classification='CONTEXT_REMEDIATION_COMPLETE_NOT_READY_TO_RESUME'
handoff={'phase':'PHASE4BC','classification':classification,'failure_reinterpreted_as':'CONTEXT_DELIVERY_ARCHITECTURE_FAILURE','leakage':{'leakage_items_total':len(leaks),'denominator':'grouped history-bearing source occurrences including admitted dependencies; not papers or scientific errors','leakage_classes':dict(Counter(x['leakage_class'] for x in leaks)),'all_known_leakage_removed':True},'architecture':cfg,'packets':{k:h(n) for k,n in [('primary_template_sha256','PRIMARY_CONTEXT_PACKET_TEMPLATE.json'),('verifier_template_sha256','VERIFIER_CONTEXT_PACKET_TEMPLATE.json'),('primary_allowlist_sha256','PRIMARY_CONTEXT_ALLOWLIST.json'),('verifier_allowlist_sha256','VERIFIER_CONTEXT_ALLOWLIST.json'),('denylist_sha256','VALIDATION_CONTEXT_DENYLIST.json'),('dry_run_primary_packet_sha256','B02_PREACCESS_PACKET_DRY_RUN/primary.packet.json'),('dry_run_verifier_packet_sha256','B02_PREACCESS_PACKET_DRY_RUN/verifier.packet.json')]},'contamination_controls':{'static_scan_passed':True,'semantic_review_passed':True,'transitive_dependency_check_passed':True,'independent_packet_review_status':'COMPLETED','real_filesystem_link_integration':'SKIPPED_HOST_UNSUPPORTED','remaining_blocker':'Required actual symlink integration unrun; mocked reparse rejection is not equivalent host proof.'},'pre_access':{'durable_receipt_required':True,'source_access_after_receipt_only':True,'timing_tests_passed':True,'scope':'synthetic-only; no operational reserved-source capability or receipt issued'},'reserved_holdout':{'total':7,'untouched':7,'consumed':0,'contamination_count':0,'resume_start':'B02'},'tests':tot,'live_state':{'source_verified':0,'promoted':0},'lane_b_executed':False,'phase4b_resume_executed':False,'phase5_started':False,'synthetic_test_exception_used':True,'preservation':read('PRESERVATION_CHECK.json'),'independent_final_review':read('INDEPENDENT_FINAL_REVIEW.json'),'package':{'path':'analysis/phase4bc_context_isolation_package.zip','sha256':'SEE_EXTERNAL_PACKAGE_RECEIPT','convention':'Archived handoff refers to external receipt; external handoff receives final ZIP hash after archive finalization.'}}
save('FINAL_HANDOFF.json',handoff)
text=f'''# Phase 4BC outcome

**{classification}**

Historical development findings are separated from the clean worker packets. The baseline verified eight archives and 12,876 protected files; final protected hashes are unchanged. All seven reserved sources remain untouched, with zero consumed and zero source-contamination events. No extraction accuracy claim exists for this phase.

The inventory contains {len(leaks)} grouped history-bearing occurrences, including observed exposure and admitted dependencies. This is not a scientific error or paper denominator. Both exact primary/verifier dry-run packets passed static scans and separate-context semantic review. Four blinded synthetic semantic challenges were correctly classified. The scientific methodology remains phase4br-scientific-v3.0.0; schema and 44 field/automation assignments are preserved.

Architecture version: phase4bc-context-v1.0.0. Fingerprint: `{cfg['context_packet_architecture_sha256']}`. Scientific parent fingerprint: `{cfg['scientific_methodology_sha256']}`. New generic-content hash is separately recorded; sanitized bytes are not claimed to retain the parent hash.

Tests: {tot['tests_run']} total, {tot['passed']} passed, {tot['failed']} failed, {tot['skipped']} skipped ({tot['inherited']} inherited, {tot['new']} new including semantic/final checks). The skipped actual symlink integration test could not create a link on Drive. Mocked reparse checks passed but do not close that host-level gap. This required unrun check prevents READY_TO_RESUME. Initial dependency/layout setup failures and false-positive scan diagnostics are preserved separately; final assertions were not weakened.

Receipt ordering, stale packet/review rejection and source refusal passed synthetic tests. Actual B02 delivery is unavailable; dry-run approval cannot open a paper. Context identity/isolation remains a documented orchestration boundary, not an OS sandbox or human scientific approval.

No Lane B, live migration, promotion, skill installation or checkpoint refresh occurred. Live source_verified and promoted remain zero. Synthetic SQLite/backup fixtures were used only in private test storage under the explicit exception and are excluded from packaging.

Before a separate resume authorization: resolve the required real-link integration limitation on an authorized filesystem/environment, rerun affected checks, preserve packet/code pins and review evidence. No source content is needed to resolve this limitation. The future run must also supply a reviewed real-source release adapter; this phase intentionally implements synthetic mechanics and dry-run packets only. Do not open B02 as part of remediation.
'''
(O/'EXECUTIVE_PHASE4BC.md').write_text(text,encoding='utf-8')
groups=[(range(1,6),'Preservation/baseline','PHASE4BC_BASELINE.json;PRESERVATION_CHECK.json;B02_B08_UNTOUCHED_RESERVATION.json'),(range(6,15),'Layer sanitization and firewall','CONTEXT_LEAKAGE_INVENTORY.csv;HISTORICAL_TO_GENERIC_RULE_MAPPING.csv;COORDINATOR_FIREWALL_PROTOCOL.md'),(range(15,24),'Deterministic composition/fingerprints/release','context_architecture/scripts/context_engine.py;CONTEXT_PACKET_MANIFEST.schema.json;PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md'),(range(24,31),'Adversarial and transitive controls','test_results/CONTEXT_ENGINE_TESTS.json;test_results/SEMANTIC_CHALLENGE_RESULTS.json;TRANSITIVE_CONTEXT_DEPENDENCY_REPORT.json'),(range(31,35),'Reserved dryrun and independent review','B02_PREACCESS_PACKET_DRY_RUN;INDEPENDENT_PACKET_REVIEW.json;B02_B08_POST_PHASE4BC_UNTOUCHED_CHECK.json'),(range(35,41),'Tests/readiness/future conservation','test_results/TEST_TOTALS.json;PHASE4B_RESUME_V2_PLAN.md;FINAL_HANDOFF.json'),(range(41,49),'Outputs/preservation/package/final interpretation','PACKAGE_MANIFEST.json;PACKAGE_RECEIPT.json;PRESERVATION_CHECK.json;EXECUTIVE_PHASE4BC.md')]
with (O/'REQUIREMENTS_TRACEABILITY.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.writer(f);w.writerow(['request_section','responsibility','evidence','limitation'])
 for ids,resp,paths in groups:
  for i in ids:w.writerow([i,resp,paths,'Real symlink host integration unrun; no READY claim. Review is model-based and input controls are not OS sandbox.'])
print(classification,tot)
