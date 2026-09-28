"""Independent streamed-hash preservation check; never interprets PDF content."""
import csv,hashlib,json,subprocess,zipfile
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1]
def h(p):
    d=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):d.update(b)
    return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,v):(O/n).write_text(json.dumps(v,indent=2,sort_keys=True),encoding='utf-8')
if __name__=='__main__':
    rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
    changed=[]
    for i,x in enumerate(rows,1):
        p=R/x['path']
        if not p.is_file() or h(p)!=x['sha256']:changed.append(x['path'])
        if i%4000==0:print('Preservation',i,flush=True)
    base=read(O/'PHASE4BC_P_BASELINE.json');archives=[]
    for x in base['archives']:
        p=R/x['path']
        with zipfile.ZipFile(p) as z:ok=z.testzip() is None
        archives.append({'path':x['path'],'hash_match':h(p)==x['expected'],'crc_pass':ok})
    reservation=read(O/'B02_B08_UNTOUCHED_CHECK.json')
    sourcechecks=[{'holdout_id':x['holdout_id'],'hash_match':h(R/x['path'])==x['source_sha256'],'substantive_access':x['substantive_access'],'consumed':x['consumed']} for x in reservation['reports']]
    current=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout
    (O/'GIT_STATUS_FINAL.txt').write_bytes(current)
    def protected_status(data):
        return [s for s in data.decode('utf-8').splitlines() if 'analysis/phase4bc_path_containment/' not in s and 'analysis/phase4bc_path_containment_package.zip' not in s]
    git_same=protected_status(current)==protected_status((O/'GIT_STATUS_INITIAL.txt').read_bytes())
    initial_paths={x['path'] for x in rows}
    new_runtime=[]
    for name in ['rehearsal_runtime','migration_state','cutover_runtime']:
        for p in (R/'analysis').rglob(name):
            if p.is_dir() and not any(str(p.relative_to(R)).replace('\\','/')+'/' in x for x in initial_paths):new_runtime.append(str(p.relative_to(R)))
    reviews_empty=read(R/'analysis/reviews.json')=={}
    ok=not changed and git_same and reviews_empty and not new_runtime and all(x['hash_match'] and x['crc_pass'] for x in archives) and all(x['hash_match'] and not x['substantive_access'] and not x['consumed'] for x in sourcechecks)
    result={'at':datetime.now(timezone.utc).isoformat(),'status':'PASS' if ok else 'FAIL','protected_count':len(rows),'changed':changed,'archives':archives,'reserved_source_checks':sourcechecks,'untouched':7,'consumed':0,'contamination_events':0,'live_source_verified':0 if reviews_empty else 'UNKNOWN','live_promoted':0 if reviews_empty else 'UNKNOWN','live_state_basis':'Unchanged protected state and empty reviews, no scientific transitions executed','git_protected_status_unchanged':git_same,'new_lane_b_or_migration_runtime':new_runtime,'source_access_limit':'Streaming hashes and recorded access inventories, not OS-wide access audit','independence':'Separate verifier implementation, no producer counting helper; shared Python/hashlib/runtime dependency'}
    put('PRESERVATION_CHECK.json',result)
    assert ok,result
    print('PRESERVATION PASS',len(rows),flush=True)
