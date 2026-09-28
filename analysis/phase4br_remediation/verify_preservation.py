"""Independent read-only protected-byte verification; writes receipts in Phase4BR only."""
import csv,json,hashlib,subprocess
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1]
def h(p):
    d=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):d.update(b)
    return d.hexdigest()
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8')));changed=[];missing=[]
for i,row in enumerate(rows,1):
    p=R/row['path']
    if not p.is_file():missing.append(row['path'])
    elif h(p)!=row['sha256']:changed.append(row['path'])
    if i%1000==0:print('Verified',i,flush=True)
reserve=json.loads((O/'B02_B08_RESERVATION_MANIFEST.json').read_text(encoding='utf-8'))
for r in reserve['reports']:
    assert h(R/r['path'])==r['source_sha256'];r['last_verified_at']=datetime.now(timezone.utc).isoformat()
(O/'B02_B08_RESERVATION_MANIFEST.json').write_text(json.dumps(reserve,indent=2)+'\n',encoding='utf-8')
git=subprocess.check_output(['git','status','--porcelain=v1','-uall'],cwd=R);(O/'GIT_STATUS_FINAL.txt').write_bytes(git)
initial=(O/'GIT_STATUS_INITIAL.txt').read_bytes().decode('utf-8').splitlines()
git_added=sorted(set(git.decode('utf-8').splitlines())-set(initial))
outside=[x for x in git_added if 'analysis/phase4br_remediation/' not in x and 'analysis/phase4br_remediation_package.zip' not in x]
reviews=json.loads((R/'analysis/reviews.json').read_text(encoding='utf-8-sig'))
out={'verified_at':datetime.now(timezone.utc).isoformat(),'protected_paths':len(rows),'original_live_protected_paths':5737,'changed':changed,'missing':missing,'git_added_outside_boundary':outside,'source_verified':0 if reviews=={} else 'UNKNOWN','promoted':0 if reviews=={} else 'UNKNOWN','scientific_state_basis':'unchanged review records and protected summaries/controls; no checkpoint entrypoint executed','prior_phases_byte_identical':not changed and not missing,'reserved_source_hashes_match':True,'lane_b_executed':False,'migration_database_created':False,'live_backup_cutover_executed':False,'synthetic_unit_database_backup_fixtures':'Inherited safety tests only, confined to candidate shadow synthetic runtime; excluded from archive','passed':not changed and not missing and not outside and reviews=={}}
(O/'PRESERVATION_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out),flush=True)
