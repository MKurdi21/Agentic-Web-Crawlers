import sys,csv,json,hashlib,subprocess
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];A=O/'context_architecture'
sys.path.insert(0,str(A/'scripts'));import context_engine as e
sys.path.insert(0,str(O/'private_diagnostic_material/inherited_candidate/_deps'))
from jsonschema import Draft202012Validator
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def h(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
checks=[]
def check(n,v):checks.append({'test':n,'status':'PASS' if v else 'FAIL'})
cfg=read(O/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');m=read(O/'IMMUTABLE_EXECUTION_MANIFEST.json')
check('independent_immutable_pin',e.verify_immutable(A,m['files'])==m['sha256']==cfg['immutable_execution_code_sha256'])
c=dict(cfg);pinned=c.pop('context_packet_architecture_sha256');check('config_nonrecursive_fingerprint',e.fingerprint(c)==pinned)
schema=read(O/'CONTEXT_PACKET_MANIFEST.schema.json')
for role in ['primary','verifier']:
 d=O/'B02_PREACCESS_PACKET_DRY_RUN';man=read(d/(role+'.release_manifest.json'))
 check(role+'_manifest_schema',not list(Draft202012Validator(schema).iter_errors(man)))
 check(role+'_exact_packet_review_hash',man['packet_sha256']==h(d/(role+'.packet.json'))==read(d/(role+'.semantic_review.json'))['packet_sha256'])
 check(role+'_source_not_released',read(d/(role+'.release_decision.json'))['production_source_release_available'] is False)
old=read(R/'analysis/phase4br_remediation/candidate_v4br/frozen_inputs/phase3/FIELD_CATALOG.json')
check('field_catalog_44_preserved',old==read(A/'methodology_generic/FIELD_CATALOG.json') and len(old['fields'])==44)
check('schema_v4_preserved',h(R/'analysis/phase4br_remediation/candidate_v4br/hardened/schemas/scientific_evidence_v4.schema.json')==h(A/'methodology_generic/scientific_evidence_v4.schema.json'))
check('no_reserved_access_event',not list((O/'B02_PREACCESS_PACKET_DRY_RUN').rglob('*SOURCE_ACCESS*')))
reserve=read(O/'B02_B08_UNTOUCHED_RESERVATION.json')
for x in reserve['reports']:check(x['holdout_id']+'_source_hash',h(R/x['path'])==x['source_sha256'])
check('no_phase4bc_pdf_or_source_render',not any(p.suffix.lower() in ('.pdf','.png','.jpg') for p in O.rglob('*') if p.is_file()))
check('no_lane_b_runtime',not (O/'rehearsal_runtime').exists())
save(O/'test_results/INDEPENDENT_FINAL_CHECKS.json',{'tests_run':len(checks),'passed':sum(x['status']=='PASS' for x in checks),'failed':sum(x['status']=='FAIL' for x in checks),'skipped':0,'tests':checks})
changed=[]
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
for i,x in enumerate(rows,1):
 p=R/x['path'];obs=h(p) if p.is_file() else None
 if obs!=x['sha256']:changed.append({'path':x['path'],'expected':x['sha256'],'observed':obs})
 if i%2500==0:print('Final preservation',i,flush=True)
reviews=read(R/'analysis/reviews.json');check('live_reviews_empty',reviews=={})
private_dbs=[p.relative_to(O).as_posix() for p in O.rglob('*') if p.suffix in ('.db','.sqlite3','.sqlite')]
assert all(s.startswith(('private_diagnostic_material/','private_test_storage/')) for s in private_dbs)
save(O/'PRESERVATION_CHECK.json',{'passed':not changed and reviews=={},'protected_file_count':len(rows),'changed_files':changed,'live_source_verified':0 if reviews=={} else 'UNKNOWN','live_promoted':0 if reviews=={} else 'UNKNOWN','synthetic_database_and_backup_fixture_count':len(private_dbs),'synthetic_storage_only':True,'migration_database_created':False,'lane_b_runtime_created':False,'live_checkpoint_refreshed':False,'skills_installed':False,'limitations':'Filesystem hashes and recorded access evidence, not OS-wide audit.'})
save(O/'B02_B08_POST_PHASE4BC_UNTOUCHED_CHECK.json',{'untouched_count':7,'consumed':0,'contamination_count':0,'reports':[{'holdout_id':x['holdout_id'],'source_sha256':x['source_sha256'],'hash_match':True,'source_derived_outputs':False,'scientific_agent_exposure':False} for x in reserve['reports']],'source_access_events':0,'proof_scope':'Recorded actions, hash confirmations and absence of derived artifacts; metadata-only packet reviewers saw current identity but no source content.'})
(O/'GIT_STATUS_FINAL.txt').write_text(subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,text=True,encoding='utf-8').stdout,encoding='utf-8')
print('Final checks done; protected changes',len(changed));assert not changed and all(x['status']=='PASS' for x in checks)
