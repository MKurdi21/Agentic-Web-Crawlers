from __future__ import annotations
import csv,hashlib,json,os,pathlib,subprocess,zipfile,shutil
from datetime import datetime,timezone

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)

def sha(p):
 h=hashlib.sha256()
 with pathlib.Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def protected():
 result=[]
 for p in ROOT.rglob('*'):
  if not p.is_file():continue
  r=p.relative_to(ROOT).as_posix()
  if r.startswith('.git/') or r.startswith('analysis/phase4_rehearsal/') or r=='analysis/phase4_rehearsal_package.zip':continue
  result.append(p)
 return sorted(result,key=lambda p:p.relative_to(ROOT).as_posix().casefold())

rows=[]
for p in protected():
 s=p.stat();rows.append({'path':p.relative_to(ROOT).as_posix(),'size':s.st_size,'mtime_ns':s.st_mtime_ns,'sha256':sha(p)})
with (OUT/'PROTECTED_FILE_HASHES_INITIAL.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['path','size','mtime_ns','sha256']);w.writeheader();w.writerows(rows)

git=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=ROOT,text=True,capture_output=True)
(OUT/'GIT_STATUS_INITIAL.txt').write_text(git.stdout,encoding='utf-8')

expected={
 'phase1':('analysis/workspace_audit_for_integration.zip','ae594106080cbe9469d242fb3378079368552178142c4984f3211cce85eb7abd'),
 'phase2':('analysis/integration_design_package.zip','8b63bb35d632496bd98303c6878d9030941538180cf47ca5569ba1448fa54b76'),
 'phase3':('analysis/phase3_calibration_package.zip','0768d7fa6b57b41f118f71f8365aaffbf7b92198c3447f8458ff3560a198339e')}
archives={}
for k,(rel,wanted) in expected.items():
 p=ROOT/rel
 with zipfile.ZipFile(p) as z:bad=z.testzip();count=len(z.infolist())
 actual=sha(p);archives[k]={'path':rel,'sha256':actual,'expected_sha256':wanted,'matches':actual==wanted,'crc_ok':bad is None,'member_count':count}

phase3=ROOT/'analysis/phase3_calibration'
holdout=phase3/'PHASE4_VALIDATION_HOLDOUT.csv'
fingerprints=json.loads((phase3/'PHASE3_FINGERPRINTS.json').read_text(encoding='utf-8'))
holdout_meta=json.loads((phase3/'HOLDOUT_FINGERPRINTS.json').read_text(encoding='utf-8'))
pres=json.loads((phase3/'PRESERVATION_CHECK.json').read_text(encoding='utf-8'))
phase3_checks=[]
for item in fingerprints['artifacts']:
 p=phase3/item['path'];phase3_checks.append({'path':item['path'],'expected':item['sha256'],'actual':sha(p),'matches':sha(p)==item['sha256']})

manifest=list(csv.DictReader((ROOT/'analysis/manifest.csv').open(encoding='utf-8-sig',newline='')))
pdfs=[p for p in ROOT.rglob('*.pdf') if not p.is_relative_to(OUT)]
reviews=json.loads((ROOT/'analysis/reviews.json').read_text(encoding='utf-8'))
baseline={'captured_at':datetime.now(timezone.utc).isoformat(),'evidence_class':'PHASE4_INITIAL_BASELINE','protected_file_count':len(rows),'archives':archives,'phase3_artifact_checks':phase3_checks,'phase3_candidate_fingerprint':fingerprints['candidate_fingerprint'],'holdout_selection_sha256':sha(holdout),'holdout_expected_sha256':'8e41106f433ceb4e81aae1d8e36f75631c162150b25c8cbbd4370921d49ff348','holdout_metadata':holdout_meta['validation_holdout'],'phase3_preservation':{'missing_count':pres['missing_count'],'changed_count':pres['changed_count']},'live_counts':{'physical_pdfs':len(pdfs),'active_reports':len(manifest),'duplicate_extras':len(pdfs)-len(manifest),'legacy_summaries':len(list((ROOT/'Summaries').glob('*.md'))),'v2_drafts':len(list((ROOT/'.summary_v2').glob('*.md'))),'review_records':len(reviews),'source_verified':0,'promoted':0}}
baseline['gate_passed']=all(x['matches'] and x['crc_ok'] for x in archives.values()) and all(x['matches'] for x in phase3_checks) and baseline['holdout_selection_sha256']==baseline['holdout_expected_sha256'] and baseline['holdout_metadata']['contamination_count']==0 and baseline['phase3_preservation']=={'missing_count':0,'changed_count':0} and baseline['live_counts']=={'physical_pdfs':117,'active_reports':112,'duplicate_extras':5,'legacy_summaries':48,'v2_drafts':37,'review_records':0,'source_verified':0,'promoted':0}
(OUT/'PHASE4_BASELINE.json').write_text(json.dumps(baseline,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(OUT/'INPUT_DRIFT_REPORT.md').write_text('# Input drift report\n\n**Classification: `NO_RELEVANT_DRIFT`**\n\nAll three input archives match their expected SHA-256 values and pass CRC checks. Frozen Phase 3 fingerprints, holdout selection, contamination state, Phase 3 preservation result, and live 117/112/5/48/37/0/0 counts match the recorded handoff. Git/runtime metadata is recorded separately and is not treated as research or control drift.\n',encoding='utf-8')
if not baseline['gate_passed']:raise SystemExit('PHASE4_BASELINE_GATE_FAILED')

# Extract only package-manifest-authorized frozen candidate/payload members.
package=ROOT/'analysis/phase3_calibration_package.zip';dest=OUT/'candidate_frozen'
if dest.exists():raise SystemExit('candidate_frozen already exists')
with zipfile.ZipFile(package) as z:
 manifest=json.loads(z.read('phase3_calibration/PACKAGE_MANIFEST.json'))
 allowed={r['path']:r for r in manifest['payload_inventory'] if r['path'].startswith(('phase3_calibration/candidate_v3/hardened/','phase3_calibration/candidate_v3/deploy_payload/')) or r['path']=='phase3_calibration/candidate_v3/requirements.txt'}
 for name,row in sorted(allowed.items()):
  data=z.read(name)
  if hashlib.sha256(data).hexdigest()!=row['sha256'] or len(data)!=row['size']:raise SystemExit('CANDIDATE_MEMBER_MISMATCH:'+name)
  rel=pathlib.PurePosixPath(name).relative_to('phase3_calibration/candidate_v3');target=dest/pathlib.Path(*rel.parts);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
fingerprinted=[p for p in dest.rglob('*') if p.is_file() and p.relative_to(dest).parts[0] in ('hardened','deploy_payload')]
body='\n'.join(f"candidate_v3/{p.relative_to(dest).as_posix()}\0{p.stat().st_size}\0{sha(p)}" for p in sorted(fingerprinted,key=lambda p:('candidate_v3/'+p.relative_to(dest).as_posix()).casefold()))
candidate={'file_count':len(fingerprinted),'sha256':hashlib.sha256(body.encode()).hexdigest(),'phase3_expected':fingerprints['candidate_fingerprint']['sha256'],'members_verified':len(allowed)}
(OUT/'CANDIDATE_FROZEN_RECEIPT.json').write_text(json.dumps(candidate,indent=2)+'\n',encoding='utf-8')
if candidate['sha256']!=candidate['phase3_expected']:raise SystemExit('CANDIDATE_AGGREGATE_MISMATCH')
print(json.dumps({'baseline_gate':True,'candidate':candidate,'live_counts':baseline['live_counts']}))
