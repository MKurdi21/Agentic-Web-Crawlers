import json,hashlib,csv,sys
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;A=O/'context_architecture'
sys.path.insert(0,str(A/'scripts'));import context_engine as e
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cfg=json.loads((O/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json').read_text(encoding='utf-8'))
fields=['packet_type','packet_id','methodology_fingerprint','policy_fingerprint','template_fingerprint','current_report_binding_fingerprint','included_artifacts','included_artifact_hashes','excluded_historical_layers','denylist_scan_result','semantic_review_result','build_timestamp','builder_version','packet_sha256']
props={k:{'type':'string','minLength':1} for k in fields}
for k in ['methodology_fingerprint','policy_fingerprint','template_fingerprint','current_report_binding_fingerprint','packet_sha256']:props[k]={'type':'string','pattern':'^[0-9a-f]{64}$'}
for k in ['included_artifacts','included_artifact_hashes','excluded_historical_layers']:props[k]={'type':'array','items':{'type':'string'},'minItems':1}
props['packet_type']={'enum':['primary','verifier']}
props['denylist_scan_result']={'enum':['STATIC_CONTEXT_CLEAN','STATIC_CONTEXT_CONTAMINATED']}
props['semantic_review_result']={'enum':['SEMANTIC_CONTEXT_CLEAN','SEMANTIC_CONTEXT_CONTAMINATED','SEMANTIC_CONTEXT_UNRESOLVED']}
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','additionalProperties':False,'required':fields,'properties':props}
save(O/'CONTEXT_PACKET_MANIFEST.schema.json',schema)
rows=[{'relative_path':p.relative_to(A).as_posix(),'size_bytes':p.stat().st_size,'sha256':h(p)} for p in sorted(A.rglob('*')) if p.is_file()]
rows=sorted(rows,key=lambda x:x['relative_path'])
e.verify_immutable(A,rows)
save(O/'IMMUTABLE_EXECUTION_MANIFEST.json',{'files':rows,'sha256':e.fingerprint(rows)})
cfg.update(immutable_execution_code_sha256=e.fingerprint(rows),semantic_review_protocol_sha256=h(O/'SEMANTIC_REVIEW_PROTOCOL.md'),freeze_status='FROZEN_CANDIDATE_REVIEW_GATED',scope_note='Generic and policy fingerprints cover master registered sets; each packet metadata additionally fingerprints its delivered subset. Parent scientific hash is provenance.')
cfg.pop('context_packet_architecture_sha256',None)
cfg['context_packet_architecture_sha256']=e.fingerprint(cfg)
save(O/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json',cfg)
for role in ['primary','verifier']:
 d=O/'B02_PREACCESS_PACKET_DRY_RUN';meta=json.loads((d/(role+'.manifest.json')).read_text(encoding='utf-8'));scan=json.loads((d/(role+'.scan.json')).read_text(encoding='utf-8'))
 manifest={'packet_type':role,'packet_id':role+'_'+meta['packet_sha256'][:20],'methodology_fingerprint':cfg['generic_methodology_sha256'],'policy_fingerprint':cfg['policy_sha256'],'template_fingerprint':cfg[role+'_template_sha256'],'current_report_binding_fingerprint':cfg['binding_sha256'],'included_artifacts':[x['artifact_id'] for x in meta['included']],'included_artifact_hashes':[x['sha256'] for x in meta['included']],'excluded_historical_layers':['D:HISTORICAL_DEVELOPMENT_ONLY'],'denylist_scan_result':scan['status'],'semantic_review_result':'SEMANTIC_CONTEXT_UNRESOLVED','build_timestamp':datetime.now(timezone.utc).isoformat(),'builder_version':e.VERSION,'packet_sha256':meta['packet_sha256']}
 save(d/(role+'.release_manifest.json'),manifest)
print('Manifest schema and frozen architecture fingerprint',cfg['context_packet_architecture_sha256'])
