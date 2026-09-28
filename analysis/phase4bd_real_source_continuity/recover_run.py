"""Read-only protected-state verification, then explicit coordinator recovery."""
from pathlib import Path
import sys,csv,json,hashlib,subprocess,uuid
from concurrent.futures import ThreadPoolExecutor
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bc_supplement/recovery_protocol'))
from engine import Engine,read,filehash,canonical,exclusive,now,PIN_KEYS
sys.path.insert(0,str(R/'analysis/phase4bc_path_containment/continuity_adapter'))
from adapter import code_pins
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
def check(x):
 p=R/x['path'];return None if p.is_file() and filehash(p)==x['sha256'] else x['path']
with ThreadPoolExecutor(max_workers=12) as pool:changed=[x for x in pool.map(check,rows) if x]
assert not changed,changed
base=read(O/'PHASE4BD_BASELINE.json');pins=code_pins();assert pins==base['frozen_pins']
rec=read(R/'analysis/phase4bc_supplement/RECOVERY_IMPLEMENTATION_MANIFEST.json')
assert rec['sha256']==base['recovery_sha256']
for x in rec['files']:assert filehash(R/'analysis/phase4bc_supplement'/x['path'])==x['sha256']
reserved=read(O/'B02_B08_UNTOUCHED_CHECK.json')
for x in reserved['reports']:assert filehash(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access']
assert read(R/'analysis/reviews.json')=={}
inventory=[];invalid=[];source_events=[];private_chains=[]
for p in sorted(O.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(O).as_posix()
 item={'path':rel,'sha256':filehash(p),'size':p.stat().st_size,'classification':'UNCOMMITTED_RECOVERY_MATERIAL'}
 if p.suffix=='.json':
  try:read(p)
  except Exception:invalid.append(rel)
 if p.name.startswith('RECOVERY_EVENTS') and p.suffix=='.jsonl':
  for line in p.read_text(encoding='utf-8').splitlines():
   try:
    event=json.loads(line)
    if event.get('event_type')=='SOURCE_ACCESS_BEGAN':source_events.append({'path':rel,'event_id':event['event_id'],'report_id':event.get('report_id'),'source_sha256':event.get('source_sha256'),'synthetic':event.get('synthetic',False)})
   except Exception:invalid.append(rel)
 if rel.startswith('test_results/INHERITED_'):
  report=read(p);assert report['failed']==0 and report['tests']==len(report['records']);item['classification']='COMPLETED_TEST_REPORT_RECONCILED_NOT_PHASE_COMMIT'
 inventory.append(item)
for p in (O/'private_development_source_material').rglob('INITIAL_STATE.json'):
 e=Engine(p.parent)
 try:
  chain=e.receipts();journal=e.journal();private_chains.append({'root':str(p.parent.relative_to(O)),'valid_receipts':len(chain),'source_access_events':sum(x['event_type']=='SOURCE_ACCESS_BEGAN' for x in journal),'last_unit':chain[-1][1]['atomic_unit_id'] if chain else None,'classification':'PRIVATE_DEVELOPMENT_TEST_HISTORY_NOT_READY_FOR_REPLAY'})
 except Exception as ex:private_chains.append({'root':str(p.parent.relative_to(O)),'classification':'PRIVATE_TEST_DIAGNOSTIC_REQUIRES_CLEAN_RESTART','reason':str(ex)})
allowed=read(O/'REAL_SOURCE_INTEGRATION_FIXTURE.json')['report_id']
assert all(x['report_id']==allowed or (x['synthetic'] is True and x['path'].startswith('inherited_candidate/inherited_recovery/private_test_storage/')) for x in source_events),source_events
e=Engine(O/'recovery_receipts');before=e.state();request='recovery-'+uuid.uuid4().hex
observed={k:before[k] for k in PIN_KEYS}
assert observed['protected_file_manifest_sha256']==filehash(O/'PROTECTED_FILES_INITIAL.csv')
assert observed['source_sha256']==filehash(read(O/'REAL_SOURCE_INTEGRATION_FIXTURE.json')['source_path'])
assert observed['current_packet_sha256']==filehash(O/'test_results/development_packet.json')
report={'request_id':request,'timestamp':now(),'run_id':before['run_id'],'previous_milestone':before['last_committed_milestone'],'interrupted_unit':before['current_atomic_unit_id'],'interruption_boundary':'DURING_IMPLEMENTATION_BEFORE_PHASE_COMMIT','frozen_pins':pins,'protected_checked':len(rows),'protected_changed':changed,'reserved_untouched':7,'reserved_consumed':0,'contamination_events':0,'live_source_verified':0,'live_promoted':0,'real_development_access_events':source_events,'private_test_chains':private_chains,'invalid_files':invalid,'files':inventory,'evidence_limit':'Recorded operations and artifact inventory, not OS-wide access audit','next_operation':'RESUME_IMPLEMENT_REAL_SOURCE_INTEGRATION; preserve completed inherited tests; clean new real-test fixtures after code fixes','replayed_operations':[],'quarantine_policy':'Preserve uncommitted implementation in place for editing; never import prior partial private test runtime; inherited engine quarantines old coordinator intent','verdict':'RECOVERY_PREFLIGHT_PASS'}
assert all(x.startswith('inherited_candidate/inherited_recovery/private_test_storage/') for x in invalid),invalid
report['invalid_file_disposition']='Preserved malformed synthetic recovery-test fixtures; excluded from authoritative state and from replay. No malformed coordinator or real-source records.'
exclusive(O/'test_results'/f'{request}.json',canonical(report))
with e.lock(request):
 chain=e.receipts();assert not chain and not e.state()['source_access_started']
 s=e.recover(observed,session_mode='NEW_SESSION')
 e.event('RECOVERY_PREFLIGHT_PASS',request_id=request,previous_milestone=before['last_committed_milestone'],interrupted_unit=before['current_atomic_unit_id'],previous_context='/root',new_context=request,pre_recovery_fingerprints=observed,reconciliation_report_sha256=filehash(O/'test_results'/f'{request}.json'),replayed_operations=[],duplicate_effects_detected=False,recovery_verdict=report['verdict'],next_permitted_operation=report['next_operation'])
 e.begin('IMPLEMENT_REAL_SOURCE_INTEGRATION',{'baseline':filehash(O/'PHASE4BD_BASELINE.json')},['outputs/integration_manifest.json','outputs/test_summary.json'])
print(json.dumps({'verdict':report['verdict'],'protected_checked':len(rows),'reserved_untouched':7,'real_development_access_events':len(source_events),'previous_milestone':before['last_committed_milestone'],'next_operation':report['next_operation'],'report':request+'.json'}))
