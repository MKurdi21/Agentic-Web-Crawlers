"""Preparation only. Never opens/parses PDFs; streaming digest checks only."""
import csv, hashlib, json, os, shutil, sys, zipfile
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd().resolve(); OUT=ROOT/'analysis/phase4be_freeze_repair_and_validation'; OLD=ROOT/'analysis/phase4b_validation_final'; EX=OUT/'execution_candidate'
sys.path.insert(0,str(EX/'orchestration'))
import freeze_code as f
def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as stream:
        for b in iter(lambda:stream.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def write(name,obj): f.replace(OUT/name,obj)
def baseline():
    rows=list(csv.DictReader((OLD/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8'))); initial=len(rows)
    known={r['path'] for r in rows}
    for p in OLD.rglob('*'):
        if p.is_file() and p.relative_to(ROOT).as_posix() not in known: rows.append({'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p),'size':p.stat().st_size})
    archive=ROOT/'analysis/phase4b_validation_final_package.zip'
    if archive.exists():rows.append({'path':archive.relative_to(ROOT).as_posix(),'sha256':digest(archive),'size':archive.stat().st_size})
    drift=[]
    for r in rows:
        p=ROOT/r['path']
        if not p.exists() or p.stat().st_size!=int(r['size']) or digest(p)!=r['sha256']:drift.append(r['path'])
    write('PROTECTED_BASELINE_EXTENDED.json',{'files':rows,'original_count':initial,'extended_count':len(rows)})
    crc='UNAVAILABLE'
    if archive.exists():
        with zipfile.ZipFile(archive) as z: crc='PASS' if z.testzip() is None else 'FAIL'
    order=f.read(OLD/'HOLDOUT_PROCESSING_ORDER.json')['order']
    source_checks=[{'holdout_id':x['holdout_id'],'sha256':digest(ROOT/x['path']),'expected_sha256':x['source_sha256'],'status':'PASS' if digest(ROOT/x['path'])==x['source_sha256'] else 'FAIL'} for x in order]
    checkpoint=f.read(ROOT/'analysis/checkpoint.json')
    write('PHASE4BE_BASELINE.json',{'protected_original_count':initial,'protected_extended_count':len(rows),'protected_drift':drift,'prior_archive_crc':crc,'source_hash_checks':source_checks,'source_body_access':False,'live_reviews_empty':f.read(ROOT/'analysis/reviews.json')=={},'prior_live_source_verified':0,'prior_live_promoted':0,'parent_hash_verification':'BLOCKER_PENDING_INDEPENDENT_PARENT_MANIFEST_VERIFICATION','stage':'PREPARATION','routing_policy_sha256':digest(OLD/'MODEL_ROUTING_POLICY.json'),'observational_only':True})

def prepare():
    f.require(digest(OLD/'MODEL_ROUTING_POLICY.json')==f.POLICY_SHA,'ROUTING_POLICY_INTEGRITY_FAILURE')
    # Initial authoring is bootstrap drafts, not retrospectively guarded writes.
    control=OUT/'control_state';freeze=OUT/'freeze_state'
    inventory=OUT/'BEHAVIOR_FILE_INVENTORY.json';deps=OUT/'DEPENDENCY_CLOSURE.json'
    b=f.Barrier(EX,control,freeze,inventory,deps)
    if not (control/'FREEZE_STATE.json').exists():b.initialize()
    with b.writer():
        snapshot=OUT/'NEVER_PACKAGE/bootstrap_drafts';snapshot.mkdir(parents=True,exist_ok=True)
        records=[]
        for p in sorted(EX.rglob('*')):
            if p.is_file():
                rel=p.relative_to(EX);q=snapshot/rel;q.parent.mkdir(parents=True,exist_ok=True)
                if not q.exists():shutil.copyfile(p,q)
                records.append({'path':rel.as_posix(),'sha256':digest(p),'bootstrap_draft':True})
        for name in ['MODEL_ROUTING_POLICY.json','MODEL_ROUTING_WORKER_RULES.json']:
            source=OLD/name;target=EX/name
            intent={'path':name,'expected_sha256':digest(source),'state':'INTENT'}
            f.replace(control/(name+'.intent.json'),intent)
            if not target.exists():shutil.copyfile(source,target)
            f.require(digest(target)==digest(source),'COPY_DRIFT')
            f.replace(control/(name+'.completion.json'),{**intent,'state':'COMPLETED','actual_sha256':digest(target)})
        for name in ['PRIMARY_TASK_TEMPLATE.json','VERIFIER_TASK_TEMPLATE.json','PRIMARY_DISPATCH_TEMPLATE.txt']:
            source=OLD/'orchestration'/name;target=EX/'orchestration'/name
            f.replace(control/(name+'.intent.json'),{'path':target.relative_to(EX).as_posix(),'expected_sha256':digest(source),'state':'INTENT'})
            if not target.exists():shutil.copyfile(source,target)
            f.require(digest(target)==digest(source),'COPY_DRIFT')
            f.replace(control/(name+'.completion.json'),{'path':target.relative_to(EX).as_posix(),'actual_sha256':digest(target),'state':'COMPLETED'})
        f.replace(control/'BOOTSTRAP_ENROLLMENT.json',{'status':'DRAFTS_PRESERVED_NOT_FORMALLY_REPUBLISHED','drafts':records,'blocker':'FORMAL_DRAFT_REPUBLICATION_AND_COMPLETE_STAGEB_IMPLEMENTATION_REQUIRED'})
    members=[]
    for p in sorted(EX.rglob('*')):
        if p.is_file():
            suffix=p.suffix;members.append({'path':p.relative_to(EX).as_posix(),'classification':'executable' if suffix=='.py' else 'config' if suffix=='.json' else 'template','behavior_role':'freeze_or_scientific_execution','dependency_role':'LOCAL'})
    write('BEHAVIOR_FILE_INVENTORY.json',{'files':members,'status':'DRAFT_NOT_FINAL','independent_discovery':'BLOCKER_PENDING'})
    write('DEPENDENCY_CLOSURE.json',{'local_file_dependencies':[m['path'] for m in members],'external_pins':[],'status':'BLOCKER','blockers':['parent external closure not fully enumerated','runtime version/inventory not verified','dynamic file loads not yet fully classified']})
    write('FREEZE_STATE.json',b.state())
    write('ROUTING_POLICY_PRESERVATION.json',{'expected':f.POLICY_SHA,'failedrun_raw_sha256':digest(OLD/'MODEL_ROUTING_POLICY.json'),'candidate_raw_sha256':digest(EX/'MODEL_ROUTING_POLICY.json'),'unchanged':True,'canonicalization':'RAW_FILE_BYTES'})
    baseline()
    for name in ['PREPARATION_COMPLETE_RECEIPT','IMMUTABLE_MANIFEST','FREEZE_RECEIPT','POST_FREEZE_EQUALITY_CHECK','PRE_B02_IMMUTABLE_EQUALITY_CHECK','INDEPENDENT_FREEZE_REVIEW']:
        write(name+'.json',{'status':'NOT_RUN','reason':'PREPARATION_INCOMPLETE_STOP_BEFORE_QUIESCENCE','stage_a_pass':False})
    write('FREEZE_REMEDIATION_TEST_RESULTS.json',{'status':'BLOCKER','required_count':18,'passed_count':0,'not_run_count':18,'reason':'COMPLETE_BEHAVIOR_IMPLEMENTATION_REQUIRED_BEFORE_FORMAL_TESTS'})
    write('CONCURRENCY_STRESS_TEST_RESULTS.json',{'status':'NOT_RUN','reason':'SUBPROCESS_BARRIER_HARNESS_NOT_YET_COMPLETE'})
    write('MODEL_BOUNDARY_TEST_RESULTS.json',{'status':'NOT_RUN','required_count':8,'passed_count':0})
    rootcause={'classification':'ESTABLISHED_CONCURRENT_PREPARATION_AND_INCOMPLETE_FREEZE_BARRIER','established':['root edited freeze helper and dispatch template while Sol preflight froze candidate','freeze helper hash changed after freeze','dispatch template absent from historical manifest'],'exact_modification_timestamps':'UNKNOWN','unknown':['exact OS process timing','whether generators retained active OS handles'],'evidence_basis':'prior immutable gate failure plus task-provided chronology','historical_manifest_sha256':'42f3fdc444a99ca68acdf21ac565636cbd281ec3e3e8e2dbf34b3796f0c98431'}
    write('FREEZE_RACE_ROOT_CAUSE.json',rootcause)
    (OUT/'FREEZE_RACE_ROOT_CAUSE.md').write_text('# Freeze race root cause\n\nEstablished: the root preparation task edited the freeze helper and added the dispatch template while the Sol preflight task froze the candidate. The immutable gate detected both the changed helper and unmanifested template. Exact OS timings are UNKNOWN. The orchestration lacked a completed preparation barrier and single final behavior writer. Historical failure remains engineering-only; no scientific source access occurred.\n',encoding='utf-8')
    blockers=['full explicit-root model transport and actual context provenance gate','complete packet/release/representation commands','full immutable dependency closure and parent pins','complete LaneB pre-frozen orchestration','18 synthetic + 8 boundary tests and subprocess stress','formal bootstrap enrollment','independent review and postfreeze equality']
    write('PREPARATION_BLOCKERS.json',{'status':'BLOCKER','blockers':blockers,'stage_a_pass':False,'freeze_committed':False,'B02_access':False})
    (OUT/'EXECUTIVE_PHASE4BE.md').write_text('PREPARATION INCOMPLETE. No quiescence or freeze commitment. Stage A does not pass. Candidate drafts and blockers preserved. B02 not opened; no model science, Lane B, live migration, promotion, or skill installation.\n',encoding='utf-8')
    (OUT/'PHASE4B_READINESS.md').write_text('PREPARATION_IN_PROGRESS. Stage B blocked pending engineering completion and independent review. No terminal classification has been reached.\n',encoding='utf-8')
    write('PREPARATION_HANDOFF.json',{'classification':'NOT_YET_CLASSIFIED','status':'PREPARATION_IN_PROGRESS','stage_a_pass':False,'B02_access':False,'reports_opened':0,'reports_consumed':0,'reports_untouched':7,'lane_b_executed':False,'actual_model_identity':'UNVERIFIED','cost':None,'silent_refreeze':False,'blockers':blockers})
if __name__=='__main__':prepare()
