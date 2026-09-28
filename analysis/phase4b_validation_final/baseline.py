"""Pre-source baseline: metadata and streaming hashes only; no PDF parsing."""
import csv, hashlib, json, os, subprocess, sys, zipfile
from pathlib import Path
O=Path(__file__).resolve().parent; R=O.parents[1]
D=R/'analysis/phase4bd_real_source_continuity'; S=R/'analysis/phase4bc_supplement'
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(D/'integration_layer'))
import bridge
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(n,v):
 p=O/n
 with p.open('x',encoding='utf-8') as f:json.dump(v,f,sort_keys=True,indent=2)
def require(b,msg):
 if not b:raise RuntimeError(msg)
require(not (O/'PHASE4B_FINAL_BASELINE.json').exists(),'BASELINE_ALREADY_EXISTS')
git=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout
(O/'GIT_STATUS_INITIAL.txt').write_bytes(git)
expected={x['path']:x['sha256'] for x in csv.DictReader((D/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig'))}
paths={n:R/n for n in expected}
for p in D.rglob('*'):
 if p.is_file():paths[p.relative_to(R).as_posix()]=p
paths['analysis/phase4bd_real_source_continuity_package.zip']=R/'analysis/phase4bd_real_source_continuity_package.zip'
rows=[]; drift=[]
for i,(n,p) in enumerate(sorted(paths.items()),1):
 if not p.is_file():drift.append({'path':n,'reason':'MISSING'});continue
 actual=h(p)
 if n in expected and expected[n]!=actual:drift.append({'path':n,'reason':'HASH_CHANGED'})
 rows.append({'path':n,'sha256':actual,'size':p.stat().st_size})
 if i%4000==0:print('Streaming baseline',i,flush=True)
put('INPUT_DRIFT_DIAGNOSTIC.json',{'status':'STOP_UNEXPECTED_BEHAVIOR_AFFECTING_DRIFT' if drift else 'NO_RELEVANT_DRIFT','drift':drift,'scientific_source_parsed':False})
require(not drift,'PROTECTED_DRIFT')
with (O/'PROTECTED_FILES_INITIAL.csv').open('x',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['path','sha256','size']);w.writeheader();w.writerows(rows)
hand=read(D/'FINAL_HANDOFF.json')
require(hand['classification']=='READY_TO_RESUME_PHASE4B_AT_B02' and hand['latest_blocker']['closed'],'READINESS')
require(all(v is True for k,v in hand['real_source_continuity'].items() if k.endswith('_passed') or k in ['consumption_irreversible','duplicate_recovery_idempotent','real_source_transport_exercised','source_delivery_after_commit_only']),'CONTINUITY')
require(hand['reserved_holdout']['untouched']==7 and hand['reserved_holdout']['consumed']==0 and hand['reserved_holdout']['contamination_events']==0,'RESERVATION')
require(hand['live_state']=={'source_verified':0,'promoted':0} and read(R/'analysis/reviews.json')=={},'LIVE_STATE')
want='3f33ac37175db0399cebf2447a2129d5091b42e9401b9bcc2fe67f6789e55068'
manifest=read(D/'INTEGRATION_MANIFEST.json');require(manifest['sha256']==want and bridge.codehash()==want,'INTEGRATION_HASH')
for x in manifest['files']:require(h(R/x['path'])==x['sha256'],'PARENT_MANIFEST_FILE:'+x['path'])
recovery=read(S/'RECOVERY_IMPLEMENTATION_MANIFEST.json')
require(recovery['sha256']==hand['recovery_protocol']['sha256'],'RECOVERY_PIN')
for x in recovery['files']:require(h(S/x['path'])==x['sha256'],'RECOVERY_FILE')
bridge.runtime_integrity()
archive=R/hand['package']['path'];require(h(archive)=='9607d54a964239ac9a60aabb113e0d5ad0e81398ba9b1fe67c5113dafa85e3b9','ARCHIVE_HASH')
with zipfile.ZipFile(archive) as z:require(z.testzip() is None,'ARCHIVE_CRC')
reserve=read(D/'B02_B08_UNTOUCHED_CHECK.json')['reports']
require([x['holdout_id'] for x in reserve]==['B02','B03','B04','B05','B06','B07','B08'],'ORDER')
entries=[]
for x in reserve:
 require(not x['substantive_access'] and not x['consumed'] and h(R/x['path'])==x['source_sha256'],'RESERVED_SOURCE')
 entries.append({k:x[k] for k in ['holdout_id','report_id','source_file_id','source_sha256','path']})
pins={k:hand[k]['sha256'] for k in ['scientific_methodology','context_architecture','path_containment','recovery_protocol','real_source_continuity']}
pins['continuity_adapter']='3494b44b5316a9ed98bbd4d903299e48f347dccd05330b369590e382015b373e'
put('PHASE4B_FINAL_BASELINE.json',{'status':'PASS','phase':'PHASE4B_FINAL','protected_count':len(rows),'protected_manifest_sha256':h(O/'PROTECTED_FILES_INITIAL.csv'),'frozen_pins':pins,'parent_handoff_sha256':h(D/'FINAL_HANDOFF.json'),'parent_archive_sha256':h(archive),'parent_archive_crc':'PASS','reserved_untouched':7,'reserved_consumed':0,'live_source_verified':0,'live_promoted':0,'checkpoint_refreshed':False,'lane_b_executed':False,'evidence_limit':'Streaming hashes and recorded state, not OS-wide audit'})
attachment=Path('C:/Users/moham/.codex/attachments/d2de35c6-826e-443e-85a8-13c68644f403/Pasted text.txt')
text=attachment.read_text(encoding='utf-8-sig')
def section(n):
 import re
 m=re.search(r'\n'+str(n)+r'\. [^\n]+\n=+\n(.*?)(?=\n=+\n\d+\. )',text,re.S)
 require(m is not None,'POLICY_SECTION');return m.group(1).strip()
policy={'version':'phase4b-final-model-routing-v1.0.0','frozen_before_source_access':True,'requested_models':{'SOL':'GPT-6 Sol','ASTRA':'GPT-6 Astra'},'runtime_model_identity':'MODEL_RUNTIME_IDENTITY_UNVERIFIED','actual_token_usage':None,'actual_cost':None,'no_inferred_cost':True,'SOL_responsibilities_exact':section(5),'ASTRA_responsibilities_exact':section(6),'mandatory_A_I_escalation_exact':section(7),'whole_report_escalation_exact':section(8),'independence_exact':section(9),'audit_exact':section(11),'no_adaptive_policy_exact':section(12),'lower_risk_sampling_exact':section(24),'sampling_algorithm':'sha256-lexicographic-v1','sampling_size':'min(N, max(3, ceil(0.25 * N)))','no_numeric_confidence_threshold':True,'whole_report_reason_codes':['GLOBAL_EXPERIMENTAL_CONTEXT_REQUIRED','MULTI_SECTION_THREAT_MODEL','DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION','MAIN_APPENDIX_RESULT_CONFLICT'],'policy_failure':'MODEL_ROUTING_POLICY_FAILURE','authority_attachment_sha256':h(attachment)}
put('MODEL_ROUTING_POLICY.json',policy)
(O/'MODEL_ROUTING_POLICY.md').write_text('# Frozen model routing\n\nRuntime identity: MODEL_RUNTIME_IDENTITY_UNVERIFIED. Requested models: GPT-6 Sol / GPT-6 Astra. No guessed token or cost figures.\n\n'+'\n\n'.join(section(n) for n in [5,6,7,8,9,11,12,24]),encoding='utf-8')
put('HOLDOUT_PROCESSING_ORDER.json',{'phase':'PHASE4B_FINAL','order':entries,'sequential':True,'next_report':'B02','later_report_access_requires_previous_pass':True})
put('HOLDOUT_STATE_TRACKER.json',{'reports_selected':7,'reports_opened':0,'reports_consumed':0,'reports_completed':0,'reports_not_run':7,'reports_remaining_untouched':7,'contamination_events':0,'reports':[{**x,'state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE','opened':False,'consumed':False,'completed':False,'primary_context_id':None,'verifier_context_ids':[]} for x in entries]})
put('HOLDOUT_CONTEXT_ISOLATION.json',{'status':'PRE_SOURCE','source_derived_material':'NEVER_PACKAGE','scientific_worker_history':'NONE','worker_allowed':'exact current source, frozen generic methodology, atomic proposition, proposed support set, required support roles, necessary current source context','worker_denied':['prior holdout results','historical Phase4 failures','B01 scientific findings','coordinator interpretation','persuasive Sol rationale'],'fresh_context_per_report':True,'fresh_independent_critical_verifier':True})
(O/'MODEL_ROUTING_LEDGER.jsonl').touch(exist_ok=False)
print('BASELINE_PASS',len(rows),'ROUTING_SHA256',h(O/'MODEL_ROUTING_POLICY.json'),flush=True)
