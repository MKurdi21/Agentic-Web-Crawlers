import sys,json,csv,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1];A=O/'context_architecture'
sys.path.insert(0,str(A/'scripts'))
import context_engine as e
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(e.canonical(x))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
templates={
'PRIMARY_CONTEXT_PACKET_TEMPLATE.json':{'role':'primary','task':'Apply only supplied generic methodology and frozen policy to the single bound report when separately authorized. This dry run has no source content and permits no source access.','current_report_binding':'BOUND_SEPARATELY','forbidden_history':True,'source_state':'NOT_YET_OPENED'},
'VERIFIER_CONTEXT_PACKET_TEMPLATE.json':{'role':'verifier','task':'Review only the current atomic proposition and its support set under the supplied verification rules. No source or candidate evidence exists in this dry run. Do not fetch any.','current_report_binding':'BOUND_SEPARATELY','atomic_proposition':None,'support_set':None,'necessary_current_evidence':None,'numeric_table_metadata':None,'forbidden_history':True},
'COORDINATOR_CONTEXT_TEMPLATE.json':{'role':'coordinator','task':'Compose worker dispatch only from frozen registered templates and current binding. Historical context remains coordinator-only. Do not append commentary, results, root causes or hints.','worker_history_injection':False}}
for n,v in templates.items():save(O/n,v);save(A/'packet_templates'/n,v)
arts=[];allows={'primary':[],'verifier':[]}
exclude_verifier={'EXTRACTION_PROTOCOL.md','FIELD_CATALOG.json','FIELD_AUTOMATION_POLICY.csv','SAMPLING_POLICY.md','RESEARCH_OBJECT_POLICY.md'}
for folder,layer in [('methodology_generic','A'),('policy_frozen','B'),('packet_templates','B')]:
 for p in sorted((A/folder).iterdir()):
  if not p.is_file() or p.name.startswith('COORDINATOR'):continue
  aid=folder+'.'+p.stem;role='both'
  if p.name.startswith('PRIMARY_CONTEXT'):role='template_primary'
  elif p.name.startswith('VERIFIER_CONTEXT'):role='template_verifier'
  elif p.name in exclude_verifier:role='primary'
  entry={'artifact_id':aid,'path':p.relative_to(A).as_posix(),'sha256':h(p),'layer':layer,'role':role,'reason':'Frozen generic rule or role-specific policy; no historical scientific findings','permitted_content_category':'GENERIC_METHODOLOGY' if layer=='A' else 'FROZEN_POLICY_OR_TEMPLATE','dependencies':[]}
  arts.append(entry)
  if role in ('both','primary','template_primary'):allows['primary'].append(aid)
  if role in ('both','verifier','template_verifier'):allows['verifier'].append(aid)
registry={'artifacts':arts};save(A/'registry.json',registry);save(A/'allowlists.json',allows)
for role in allows:save(O/(role.upper()+'_CONTEXT_ALLOWLIST.json'),{'role':role,'default':'DENY','artifacts':[x for x in arts if x['artifact_id'] in allows[role]]})
with (O/'VALIDATION_PACKET_CONTENT_REGISTRY.csv').open('w',encoding='utf-8',newline='') as f:
 fields=['logical_role','path','sha256','layer','primary_allowed','verifier_allowed','coordinator_allowed','historical_scientific_content','reason'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for x in arts:w.writerow(dict(logical_role=x['artifact_id'],path=x['path'],sha256=x['sha256'],layer=x['layer'],primary_allowed=x['artifact_id'] in allows['primary'],verifier_allowed=x['artifact_id'] in allows['verifier'],coordinator_allowed=True,historical_scientific_content=False,reason=x['reason']))
patterns=[]
def add(text,cat):
 if text and text not in [x['text'] for x in patterns]:patterns.append({'id':'deny_%03d'%(len(patterns)+1),'text':text,'category':cat})
for path,only in [(R/'analysis/phase3_calibration/PHASE4_VALIDATION_HOLDOUT.csv',False),(R/'analysis/phase4r_remediation/PHASE4B_VALIDATION_HOLDOUT.csv',True)]:
 for x in csv.DictReader(path.open(encoding='utf-8-sig')):
  if only and x['holdout_id']!='B01':continue
  add(x['holdout_id'],'PRIOR_REPORT_IDENTITY');add(x['paper_report_id'],'PRIOR_REPORT_IDENTITY');add(x['summary_name'],'PRIOR_REPORT_TITLE');add(x['summary_name'].replace('_comprehensive_summary.md','').replace('_',' '),'PRIOR_REPORT_TITLE')
for text in ['16.37','19.78','H05 sampled','H04 zero-row','H03 global-best','B01_REGRESSION','B01_DEVELOPMENT','PHASE4_REHEARSAL','PHASE4B_VALIDATION','prior false accept','previous holdout found','the earlier holdout where','131 original','127 critical','80 challenges','58 locator-only','RESEARCH_OBJECT_ADJUDICATION_PACKET','HOLDOUT_DISAGREEMENTS','coordinator scientific summary']:
 add(text,'HISTORICAL_FINDING_OR_DIAGNOSTIC')
deny={'version':'phase4bc-deny-v1.0.0','patterns':patterns};save(O/'VALIDATION_CONTEXT_DENYLIST.json',deny);save(A/'deny_rules/denylist.json',deny)
save(A/'historical_forbidden/CLASSIFICATION.json',{'classification':'HISTORICAL_DEVELOPMENT_ONLY','originals_moved':False,'worker_eligible':False,'categories':['previous validation findings','adjudications','real-paper fixtures','historical metrics','coordinator scientific summaries'],'inventory_reference':'CONTEXT_LEAKAGE_INVENTORY.csv'})
b=json.loads((O/'B02_B08_UNTOUCHED_RESERVATION.json').read_text(encoding='utf-8'))['reports'][0]
binding={'phase':'PHASE4BC_DRY_RUN','holdout_id':'B02','paper_id':b['report_id'],'source_sha256':b['source_sha256'],'methodology_sha256':'ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f','context_protocol_version':e.VERSION,'current_report_source':'NOT_YET_OPENED'}
D=O/'B02_PREACCESS_PACKET_DRY_RUN';D.mkdir(exist_ok=True);save(D/'binding.json',binding)
scans={};metas={}
for role in allows:
 packet,meta=e.build_packet(A,registry,allows,binding,role)
 assert e.build_packet(A,registry,allows,binding,role)[0]==packet
 (D/(role+'.packet.json')).write_bytes(packet);save(D/(role+'.manifest.json'),meta)
 scans[role]=e.scan_packet(packet,deny);metas[role]=meta;save(D/(role+'.scan.json'),scans[role])
save(O/'STATIC_CONTEXT_SCAN.json',scans)
save(O/'TRANSITIVE_CONTEXT_DEPENDENCY_REPORT.json',{'passed':True,'composition':'exact role artifact IDs; no recursive discovery','artifact_count':len(arts),'dependencies':{x['artifact_id']:x['dependencies'] for x in arts},'includes':'none','ambient_instruction_limit':'Framework system/developer/repository instructions require future dispatch inventory; not an OS sandbox.'})
config={'scientific_methodology_version':'phase4br-scientific-v3.0.0','scientific_methodology_sha256':binding['methodology_sha256'],'context_packet_architecture_version':e.VERSION,'generic_methodology_sha256':e.fingerprint([x for x in arts if x['layer']=='A']),'policy_sha256':e.fingerprint([x for x in arts if x['layer']=='B' and not x['role'].startswith('template')]),'primary_template_sha256':h(O/'PRIMARY_CONTEXT_PACKET_TEMPLATE.json'),'verifier_template_sha256':h(O/'VERIFIER_CONTEXT_PACKET_TEMPLATE.json'),'binding_sha256':e.fingerprint(binding),'primary_packet_sha256':metas['primary']['packet_sha256'],'verifier_packet_sha256':metas['verifier']['packet_sha256'],'registry_sha256':e.fingerprint(registry),'allowlists_sha256':e.fingerprint(allows),'denylist_sha256':e.fingerprint(deny),'source_release_available':False,'freeze_status':'PENDING_REVIEWS_AND_CODE_FINALIZATION'}
save(O/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json',config)
print('Packets built',[(k,v['status']) for k,v in scans.items()])
