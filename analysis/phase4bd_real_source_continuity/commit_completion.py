"""Durable finalization; committed outputs are immutable copies of evidence."""
from pathlib import Path
import sys,json
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
e=Engine(O/'recovery_receipts')
receipt=read(O/'PACKAGE_RECEIPT.json');hand=read(O/'FINAL_HANDOFF.json')
assert receipt['status']=='PASS' and hand['classification']=='READY_TO_RESUME_PHASE4B_AT_B02'
assert hand['package']['sha256']==filehash(R/hand['package']['path'])==receipt['sha256']
assert codehash()==hand['real_source_continuity']['sha256']
assert read(O/'PRESERVATION_CHECK.json')['status']=='PASS'
assert read(O/'PRESERVATION_FINAL.json')['status']=='PASS'
assert read(O/'FINAL_ARCHIVE_REVIEW.json')['status']=='PASS_WITH_EXPLICIT_LIMITATIONS'
with e.lock('phase4bd-completion'):
 chain=e.receipts();units={r['atomic_unit_id'] for _,r in chain}
 if 'FINAL_REPORTS_AND_ACCEPTANCE' not in units:
  outputs={n:filehash(O/n) for n in ['FINAL_HANDOFF.json','EXECUTIVE_PHASE4BD.md','PHASE4B_RESUME_READINESS_FINAL.md','INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json','FINAL_ARCHIVE_REVIEW.json','PRESERVATION_CHECK.json','PRESERVATION_FINAL.json','test_results/FIREWALL_ACCEPTANCE.json','test_results/FINAL_TEST_SUMMARY.json']}
  e.begin('FINAL_REPORTS_AND_ACCEPTANCE',{'implementation_manifest':filehash(O/'INTEGRATION_MANIFEST.json'),'final_review':filehash(O/'INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json')},['outputs/final_report_fingerprints.json','outputs/final_test_summary.json'])
  e.commit({'outputs/final_report_fingerprints.json':canonical(outputs),'outputs/final_test_summary.json':canonical(read(O/'test_results/FINAL_TEST_SUMMARY.json'))},next_operation='COMMIT_VERIFIED_PACKAGE')
 if 'VERIFIED_PACKAGE' not in units:
  e.begin('VERIFIED_PACKAGE',{'archive':receipt['sha256'],'manifest':filehash(O/'PACKAGE_MANIFEST.json')},['outputs/package_receipt.json','outputs/final_handoff.json'])
  e.commit({'outputs/package_receipt.json':canonical(receipt),'outputs/final_handoff.json':canonical(hand)},next_operation='STOP_BEFORE_B02')
 if e.state()['status']!='RUN_COMPLETE':e.finish()
 assert e.state()['next_permitted_operation']=='STOP'
print(json.dumps({'status':e.state()['status'],'last_milestone':e.state()['last_committed_milestone'],'next_operation':e.state()['next_permitted_operation'],'milestones':[r['atomic_unit_id'] for _,r in e.receipts()],'classification':hand['classification'],'package_sha256':receipt['sha256']}))
