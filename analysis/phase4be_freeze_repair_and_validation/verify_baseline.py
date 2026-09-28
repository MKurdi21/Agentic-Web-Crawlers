"""Read-only parent component verification and historical archive reconciliation."""
import hashlib, importlib, json, sys, zipfile
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd().resolve();OUT=ROOT/'analysis/phase4be_freeze_repair_and_validation';OLD=ROOT/'analysis/phase4b_validation_final'
sys.path.insert(0,str(OUT/'execution_candidate/orchestration'))
import freeze_code as f
from prepare_stage_a import digest
def verify():
    baseline=f.read(OUT/'PHASE4BE_BASELINE.json');checks=[];external=[]
    specs=[('phase4br_remediation','REMEDIATED_WORKFLOW_CONFIGURATION.json','candidate_files','candidate_v4br'),('phase4bc_context_isolation','IMMUTABLE_EXECUTION_MANIFEST.json','files','context_architecture'),('phase4bc_path_containment','IMPLEMENTATION_MANIFEST.json','files',''),('phase4bc_supplement','RECOVERY_IMPLEMENTATION_MANIFEST.json','files',''),('phase4bd_real_source_continuity','INTEGRATION_MANIFEST.json','files','PROJECT')]
    for folder,name,key,prefix in specs:
        base=ROOT/'analysis'/folder;manifest=f.read(base/name)
        for x in manifest[key]:
            rel=x.get('relative_path',x.get('path'));p=(ROOT if prefix=='PROJECT' else base/prefix)/rel
            actual=digest(p);expected=x['sha256'];checks.append({'path':p.relative_to(ROOT).as_posix(),'expected':expected,'actual':actual,'status':'PASS' if actual==expected else 'FAIL'});external.append({'path':str(p),'sha256':expected})
        external.append({'path':str(base/name),'sha256':digest(base/name)})
    sys.path.insert(0,str(ROOT/'analysis/phase4bd_real_source_continuity/integration_layer'));b=importlib.import_module('bridge')
    checks.append({'component':'real_source_continuity','expected':'3f33ac37175db0399cebf2447a2129d5091b42e9401b9bcc2fe67f6789e55068','actual':b.codehash(),'status':'PASS' if b.codehash()=='3f33ac37175db0399cebf2447a2129d5091b42e9401b9bcc2fe67f6789e55068' else 'FAIL'})
    try:runtime_digest=b.runtime_integrity();runtime_status='PASS'
    except Exception as ex:runtime_digest=None;runtime_status='FAIL:'+repr(ex)
    archive=ROOT/'analysis/phase4b_validation_final_package.zip';expected='8250fcc75725c6461f22b762ad0df435b0fa9a310631846b706503ef740e373f';actual=digest(archive);members=[]
    with zipfile.ZipFile(archive) as z:
        crc='PASS' if z.testzip() is None else 'FAIL'
        for n in z.namelist():
            if n.endswith('/'):continue
            candidates=[OLD/n,ROOT/n];p=next((x for x in candidates if x.exists()),None)
            data=z.read(n);hashed=hashlib.sha256(data).hexdigest();status='MISSING' if p is None else 'PASS' if digest(p)==hashed else 'DIFFERENT'
            if p is not None and p.name=='FINAL_HANDOFF.json' and status=='DIFFERENT':
                packaged=json.loads(data);current=f.read(p)
                for obj in [packaged,current]:
                    for key in ['package','package_sha256','package_member_count','external_post_package_verification_records','git_status_comparison_sha256','independent_archive_validation','independent_archive_validation_sha256','git_status_comparison']:obj.pop(key,None)
                status='PASS_DOCUMENTED_EXTERNAL_PACKAGE_METADATA' if packaged==current else status
            members.append({'name':n,'sha256':hashed,'status':status})
    hand=f.read(OLD/'FINAL_HANDOFF.json');post=[]
    for name,key in [('INDEPENDENT_ARCHIVE_VALIDATION.json','independent_archive_validation_sha256'),('GIT_STATUS_COMPARISON.json','git_status_comparison_sha256')]:post.append({'path':name,'status':'PASS' if digest(OLD/name)==hand[key] else 'FAIL','sha256':digest(OLD/name)})
    baseline.update(live_reviews_empty=f.read(ROOT/'analysis/reviews.json')=={},parent_hash_verification='PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL',parent_component_checks=checks,parent_runtime_integrity=runtime_status,parent_runtime_digest=runtime_digest,prior_archive_sha256=actual,prior_archive_expected_sha256=expected,prior_archive_hash_status='PASS' if actual==expected else 'FAIL',prior_archive_crc=crc,prior_archive_members=members,external_post_package_checks=post)
    f.replace(OUT/'PHASE4BE_BASELINE.json',baseline);f.replace(OUT/'PARENT_EXTERNAL_PINS.json',{'files':external})
    print(json.dumps({'parent_checks':len(checks),'parent_status':baseline['parent_hash_verification'],'archive_status':baseline['prior_archive_hash_status'],'runtime':runtime_status,'member_failures':sum(not x['status'].startswith('PASS') for x in members)}))
if __name__=='__main__':verify()
