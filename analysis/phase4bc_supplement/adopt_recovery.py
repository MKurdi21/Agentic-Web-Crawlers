"""Explicit bootstrap-to-library handoff, preserving every bootstrap record."""
import sys
from pathlib import Path
O=Path(__file__).resolve().parent
sys.path.insert(0,str(O/'recovery_protocol'))
from engine import *
state=read(O/'RECOVERY_STATE.json')
assert state['last_committed_milestone']=='BOOTSTRAP_RECONCILIATION'
assert filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json')==state['last_committed_milestone_receipt_sha256']
receipt=read(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json')
for p,h in receipt['output_fingerprints'].items():assert filehash(O/p)==h
latest=max((O/'test_results').glob('recovery-*.json'),key=lambda p:p.stat().st_mtime_ns)
tests=read(latest);assert tests['tests']==46 and tests['failed']==0
files=[*sorted((O/'recovery_protocol').glob('*.py')),*sorted(O.glob('*.schema.json'))]
manifest={'version':VERSION,'files':[{'path':p.relative_to(O).as_posix(),'size':p.stat().st_size,'sha256':filehash(p)} for p in files]}
manifest['sha256']=digest(canonical(manifest['files']))
exclusive(O/'RECOVERY_IMPLEMENTATION_MANIFEST.json',canonical(manifest))
pins={k:state.get(k) for k in PIN_KEYS};pins['immutable_code_sha256']=manifest['sha256']
bindings=[{'path':str(p),'sha256':filehash(p)} for p in files]
bindings.extend({'path':str(O/p),'sha256':filehash(O/p)} for p in ['RECOVERY_PREFLIGHT.json','PROTECTED_FILES_INITIAL.csv','PHASE4BC_S_BASELINE.json','RECOVERY_IMPLEMENTATION_MANIFEST.json'])
e=Engine(O/'recovery_coordination')
with e.lock('/root'):
    e.init('phase4bc-s-durable',pins,phase='PHASE4BC-S',bindings=bindings)
    e.begin('IMPLEMENT_RECOVERY_PROTOCOL',{'bootstrap_receipt':filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),'implementation_manifest':manifest['sha256']},['outputs/implementation_manifest.json','outputs/recovery_test_results.json'])
    e.commit({'outputs/implementation_manifest.json':canonical(manifest),'outputs/recovery_test_results.json':canonical(tests)},next_operation='FINAL_REPORTS_AND_PRESERVATION')
exclusive(O/'RECOVERY_TEST_RESULTS.json',canonical(tests))
exclusive(O/'RECOVERY_COORDINATION_INDEX.json',canonical({'canonical_state':'recovery_coordination/RECOVERY_STATE.json','canonical_journal':'recovery_coordination/RECOVERY_EVENTS.jsonl','canonical_receipts':'recovery_coordination/milestone_receipts/','bootstrap_state_preserved':'RECOVERY_STATE.json','bootstrap_journal_preserved':'RECOVERY_EVENTS.jsonl','bootstrap_receipt_sha256':filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),'reason':'Explicit versioned adoption; old bootstrap format not rewritten or misrepresented as new engine format.','scientific_continuation_authorized':False}))
print('IMPLEMENT_RECOVERY_PROTOCOL durably committed; next FINAL_REPORTS_AND_PRESERVATION')
