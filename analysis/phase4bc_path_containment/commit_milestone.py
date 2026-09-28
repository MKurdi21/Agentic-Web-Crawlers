"""Durable finalization milestones via the unchanged parent recovery engine."""
from pathlib import Path
import sys,json,hashlib
O=Path(__file__).resolve().parent
sys.path.insert(0,str(O.parent/'phase4bc_supplement/recovery_protocol'))
from engine import Engine,canonical,filehash
e=Engine(O/'recovery_coordination')
mode=sys.argv[1]
with e.lock('/root-finalization'):
    if mode=='implementation':
        assert e.state()['current_atomic_unit_id']=='IMPLEMENT_CONTAINMENT_AND_CONTINUITY'
        e.commit({'outputs/implementation_manifest.json':(O/'IMPLEMENTATION_MANIFEST.json').read_bytes(),'outputs/test_results.json':(O/'test_results/FINAL_TEST_SUMMARY.json').read_bytes()},next_operation='REPORTS_AND_PRESERVATION')
    elif mode=='reports':
        names=['INDEPENDENT_CONTAINMENT_REVIEW.json','PRESERVATION_CHECK.json','FINAL_HANDOFF.json','PHASE4B_RESUME_READINESS_FINAL.md','SYMLINK_GATE_SUPERSESSION.json','SCIENTIFIC_CONTINUITY_ADAPTER_REPORT.json']
        entries=[{'path':n,'sha256':filehash(O/n)} for n in names]
        e.begin('REPORTS_AND_PRESERVATION',{'implementation':filehash(O/'IMPLEMENTATION_MANIFEST.json')},['outputs/report_manifest.json'])
        e.commit({'outputs/report_manifest.json':canonical({'files':entries,'package_handoff_convention':'External FINAL_HANDOFF will add archive hash; this receipt binds pre-package handoff bytes which are retained in archive'})},next_operation='PACKAGE_AND_INDEPENDENT_ARCHIVE_CHECK')
    elif mode=='package':
        receipt=json.loads((O/'PACKAGE_RECEIPT.json').read_text());assert receipt['status']=='PASS'
        e.begin('PACKAGE_AND_INDEPENDENT_ARCHIVE_CHECK',{'manifest':filehash(O/'PACKAGE_MANIFEST.json')},['outputs/package_receipt.json'])
        e.commit({'outputs/package_receipt.json':(O/'PACKAGE_RECEIPT.json').read_bytes()},next_operation='STOP_WITHOUT_B02_ACCESS')
        e.finish()
    else:raise ValueError(mode)
    print(e.state()['status'],e.state()['last_committed_milestone'],e.state()['next_permitted_operation'])
