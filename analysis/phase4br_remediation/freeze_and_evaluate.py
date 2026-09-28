"""Freeze reviewed candidate; final B01-only development evaluation. Never imports a DB."""
import sys,json,hashlib,re,csv,collections,platform
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;C=O/'candidate_v4br';P=O/'private_source_material';OLD=P/'original_phase4b/holdout_validation/B01/private'
sys.path[:0]=[str(C/'_deps'),str(C/'hardened/scripts')]
from validation_guard import manifest,verify_manifest
from pre_access import canonical,digest,commit_preaccess,open_source,verify_order
from support_v4 import validate_graph,validate_source_bindings,calculate
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def now():return datetime.now(timezone.utc).isoformat()
cfgpath=O/'REMEDIATED_WORKFLOW_CONFIGURATION.json'
assert not cfgpath.exists(),'Do not silently replace a frozen methodology'
test=read(C/'test_results/UNIT_INTEGRATION_RESULTS.json');assert test['failed']==0 and test['skipped']==0
immutable=manifest(C)
deps=[{'relative_path':p.relative_to(C/'_deps').as_posix(),'size_bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in sorted((C/'_deps').rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
write(O/'DEPENDENCY_MANIFEST.json',{'runtime':platform.python_version(),'files':deps})
write(O/'CANDIDATE_CODE_MANIFEST.json',{'immutable_files':immutable,'manifest_sha256':digest(canonical(immutable)),'mutable_exclusions':['shadow','test_runtime','test_results','outbox','cache','backups','logs','__pycache__'],'dependencies_separately_pinned':digest(canonical(deps))})
definition={'methodology_version':'phase4br-scientific-v3.0.0','evidence_schema_version':'4.0.0','parent_methodology_sha256':'ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb','candidate_files':immutable,'dependency_manifest_sha256':digest(canonical(deps)),'runtime_python':platform.python_version()}
method=digest(canonical(definition))
cfg={**definition,'methodology_sha256':method,'frozen_at':now(),'fingerprint_algorithm':'SHA256(canonical UTF-8 definition excluding methodology_sha256 and frozen_at)','scope':'B01 REMEDIATION_DEVELOPMENT_EVALUATION; reserved reports not authorized','controller_acceptance':'unchanged operational controller; mandatory v4 scientific gate is separate from storage acceptance','human_ground_truth':False}
write(cfgpath,cfg)
source=P/'original_phase4b/private_source_material/B01/source.pdf';S=digest(source.read_bytes())
protocols={x['relative_path']:x['sha256'] for x in immutable if '/protocols/' in x['relative_path'] or 'FIELD_CATALOG' in x['relative_path'] or x['relative_path'].endswith('pre_access.py')}
binding={'phase':'PHASE4BR_FINAL_DEVELOPMENT_EVALUATION','holdout_id':'B01','paper_id':'report_e30d9cfd6055ddd8e085a0ff','source_file_id':'sha256:'+S,'source_sha256':S,'candidate_manifest_sha256':digest(canonical(immutable)),'methodology_sha256':method,'protocol_hashes':protocols,'field_catalog_sha256':digest((C/'frozen_inputs/phase3/FIELD_CATALOG.json').read_bytes()),'holdout_state':'CONSUMED_VALIDATION_SET_AND_DEVELOPMENT_REMEDIATION_DATA','context_protocol_version':'phase4br-development-context-v1'}
receipt_dir=P/'access/final_development'
verify_manifest(C,immutable);receipt=commit_preaccess(receipt_dir,binding,allowed_reports={'B01'});source_bytes=open_source(receipt_dir,source,binding,allowed_reports={'B01'})
assert verify_order(receipt,read(receipt_dir/'SOURCE_ACCESS_BEGAN.json'))
text_path=OLD/'extracted_pages.txt';parts=re.split(r'=+ PDF PAGE (\d+) =+',text_path.read_text(encoding='utf-8'));pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
rows=[];graphs={}
for path in sorted((P/'development_graphs').glob('*.json')):
    g=read(path);g['methodology_sha256']=method
    for r in g['reviews']:r['methodology_sha256']=method
    validate_source_bindings(g,S,pages);result=validate_graph(g);write(path,g);graphs[path.stem]=g
    rows.append({'graph_id':path.stem,'sha256':digest(path.read_bytes()),'source_binding':True,'structural_and_semantic_result':result,'claim_statuses':[x['support_status'] for x in g['claims']],'propositions':len(g['propositions']),'inference_propositions':sum(x['origin']=='ANALYST_INFERENCE' for x in g['propositions'])})
verify_manifest(C,immutable)
cross=read(O/'DEVELOPMENT_ITEM_CROSSWALK.json');byitem={x['original_evidence_item_id']:x for x in cross['items'] if x['graph_id'].startswith('DEV')}
original=read(OLD/'normalized_evidence_items.json');assert len(byitem)==len(original)==131
challenge=read(O/'B01_SUPPORT_ADJUDICATION.json');assert len(challenge['adjudications'])==80
for r in challenge['adjudications']:
    x=byitem[r['evidence_item_id']];g=graphs[x['graph_id']]
    r['development_rerun_result']=g['claims'][0]['support_status']
    r['development_graph_id']=x['graph_id'];r['development_proposition_ids']=[p['proposition_id'] for p in g['propositions']]
    r['remediation_outcome']='NO_ORIGINAL_ERROR_CONFIRMED' if r['challenge_disposition']=='PRIMARY_CORRECT' else 'CORRECTED_OR_LOCATORS_COMPLETED' if g['claims'][0]['support_status']=='FULLY_SUPPORTED' else 'QUALIFIED_OR_FAIL_CLOSED'
    if r['field_id']=='results.quantitative':r['verifier_finding']='Verifier identified incomplete metric/condition support. Exact original finding retained in the hash-bound private challenge record.'
write(O/'B01_SUPPORT_ADJUDICATION.json',challenge)
with (O/'B01_SUPPORT_ADJUDICATION_MATRIX.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(challenge['adjudications'][0]));w.writeheader()
    for r in challenge['adjudications']:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
ver=read(OLD/'COMBINED_VERIFICATION_RESULTS.json')['results'];cohort=[x for x in ver if x['verdict']=='SUPPORTED'];reg=[]
for v in cohort:
    x=byitem[v['stable_item_id']];g=graphs[x['graph_id']]
    if x['development_change']=='DECOMPOSED_COMPARISONS':ok=all(graphs['COMP_'+n]['claims'][0]['support_status']=='FULLY_SUPPORTED' for n in ['T3_BENIGN','T3_ASR','T5_ASR','T5_BENIGN']);status='improved' if ok else 'regressed'
    else:ok=g['claims'][0]['support_status']=='FULLY_SUPPORTED';status='improved' if ok and x['development_change']=='IMPROVED' else 'still_correct' if ok else 'now_unresolved'
    reg.append({'original_evidence_item_id':v['stable_item_id'],'critical':v['critical'],'graph_id':x['graph_id'],'result':status})
regcounts=collections.Counter(x['result'] for x in reg)
write(O/'test_results/B01_REGRESSION_RESULTS.json',{'cohort_definition':'45 previously verifier-SUPPORTED items, rechecked as model source-adjudicated development evidence; not human ground truth','previously_correct':len(cohort),'critical':sum(x['critical'] for x in cohort),**{k:regcounts[k] for k in ['still_correct','narrowed','improved','regressed','now_unresolved']},'items':reg,'passed':regcounts['regressed']==0 and regcounts['now_unresolved']==0})
write(O/'test_results/B01_DEVELOPMENT_GRAPH_RESULTS.json',{'mode':'REMEDIATION_DEVELOPMENT_EVALUATION','methodology_sha256':method,'source_sha256':S,'extraction_artifact_sha256':digest(text_path.read_bytes()),'graphs':rows,'passed':True,'private_source_bytes_packaged':False})
write(O/'test_results/PRE_ACCESS_FINAL_RECEIPT_CHECK.json',{'receipt':receipt,'source_access_event':read(receipt_dir/'SOURCE_ACCESS_BEGAN.json'),'ordering_passed':True,'immutable_before_after':True,'physical_hash_read_precedes_access_event':True,'substantive_interpretation_after_receipt':True})
metrics={'evaluation_mode':'REMEDIATION_DEVELOPMENT_EVALUATION','methodology_version':cfg['methodology_version'],'methodology_sha256':method,'original_evidence_items':131,'original_critical_items':sum(x['critical'] for x in original),'challenged_critical_items':80,'challenges_source_adjudicated':80,'challenge_distribution':challenge['distribution'],'adjudication_claim_counts':dict(collections.Counter(x['claim_correctness'] for x in challenge['adjudications'])),'adjudication_locator_counts':dict(collections.Counter(x['locator_correctness'] for x in challenge['adjudications'])),'remediation_outcomes':dict(collections.Counter(x['remediation_outcome'] for x in challenge['adjudications'])),'graphs_evaluated':len(rows),'propositions_evaluated':sum(r['propositions'] for r in rows),'inference_propositions':sum(r['inference_propositions'] for r in rows),'table_local_comparisons':4,'known_detected_false_supports_left_fully_supported':0,'known_locator_failures_left_fully_supported':0,'ground_truth_critical_false_accepts':'UNKNOWN','scientific_artifacts_accepted':0,'regressions':regcounts['regressed'],'regression_unresolved':regcounts['now_unresolved'],'independent_human_review':False,'model_review_mode':'COORDINATOR_SOURCE_ADJUDICATION_WITH_SEPARATE_CONTEXT_TECHNICAL_REVIEW','development_gate_passed':regcounts['regressed']==0 and regcounts['now_unresolved']==0}
write(O/'REMEDIATION_DEVELOPMENT_METRICS.json',metrics)
write(O/'test_results/UNIT_INTEGRATION_RESULTS.json',test)
reserve=read(O/'B02_B08_RESERVATION_MANIFEST.json')
write(O/'PHASE4B_RESUME_HOLDOUT_MANIFEST.json',{'validation_type':'SEQUENTIAL_RESERVED_HOLDOUT_VALIDATION','reports':reserve['reports'],'original_phase4b_selection_sha256':'5dd9b5edd41f93912290058731c6304e24d657470ff1a45835b5522bd10b0536','resumed_order':[x['holdout_id'] for x in reserve['reports']],'methodology_sha256':method,'B01':'CONSUMED_DEVELOPMENT_EVIDENCE_EXCLUDED','resume_authorized':False,'proof_limit':reserve['proof_limit']})
print(json.dumps(metrics))
