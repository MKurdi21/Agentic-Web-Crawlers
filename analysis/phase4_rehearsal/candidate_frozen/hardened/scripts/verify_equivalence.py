"""Independent SQL/filesystem reconciliation; does not call importer counting helpers."""
import csv,collections,importlib.util
from common import *
from db import connect,integrity,verify_profile
def verify(workspace,db):
 workspace=pathlib.Path(workspace)
 with (workspace/'analysis/manifest.csv').open(encoding='utf-8-sig',newline='') as f:manifest=list(csv.DictReader(f))
 with (workspace/'analysis/workspace_audit/ARTIFACT_INVENTORY.csv').open(encoding='utf-8-sig',newline='') as f:expected_artifacts=list(csv.DictReader(f))
 spec=importlib.util.spec_from_file_location('oracle',workspace/'scripts/summary_state.py');oracle=importlib.util.module_from_spec(spec);spec.loader.exec_module(oracle)
 with connect(db,readonly=True) as c:
  counts={t:c.execute('SELECT count(*) FROM '+t).fetchone()[0] for t in ['sources','observations','reports','artifacts','accepted','relationships','reviews','events','records','unknowns']}
  reports={r['summary_name']:dict(r) for r in c.execute('SELECT * FROM reports')};errors=[];export=[]
  if set(reports)!={r['SummaryName'] for r in manifest}:errors.append('ALIAS_SET')
  for m in manifest:
   r=reports[m['SummaryName']];source=workspace/m['Pdf'].replace('\\','/');draft=workspace/m['StageTarget'].replace('\\','/');final=workspace/m['FinalTarget'].replace('\\','/')
   h=digest(source);status='pending' if not draft.is_file() else 'structural_pass' if oracle.check_structure(draft)['passed'] else 'needs_repair'
   if r['source_id']!='sha256:'+h or json.loads(r['manifest_json'])!=m or r['legacy_status']!=status:errors.append('REPORT:'+m['SummaryName'])
   export.append({'paper_report_id':r['paper_report_id'],'summary_name':m['SummaryName'],'source_path':m['Pdf'],'source_sha256':h,'draft_path':m['StageTarget'],'draft_sha256':digest(draft) if draft.exists() else None,'final_path':m['FinalTarget'],'final_sha256':digest(final) if final.exists() else None,'legacy_status':status,'scientific_state':r['scientific_state']})
  actual_pdfs={str(p.resolve()):digest(p) for p in workspace.rglob('*.pdf') if not p.is_relative_to(DESIGN)}
  observations={r['path']:r['sha256'] for r in c.execute('SELECT path,sha256 FROM observations JOIN sources USING(source_id)')}
  if actual_pdfs!=observations:errors.append('PDF_OBSERVATIONS')
  for a in expected_artifacts:
   r=c.execute('SELECT * FROM artifacts WHERE origin_path=?',(a['artifact_path'],)).fetchone()
   if not r or r['role']!='RAW_REGISTERED_HISTORICAL_ARTIFACT' or r['privacy']!='NEVER_PACKAGE' or r['sha256']!=a['sha256'] or digest(r['path'])!=a['sha256']:errors.append('ARTIFACT:'+a['artifact_path'])
  verified=c.execute("SELECT count(*) FROM reports WHERE scientific_state IN ('SOURCE_VERIFIED','PROMOTED_NARRATIVE','ACCEPTED_STRUCTURED_EVIDENCE')").fetchone()[0]
  expected={'sources':112,'observations':117,'reports':112,'artifacts':len(expected_artifacts),'accepted':0,'relationships':2,'reviews':0,'events':1,'records':0,'unknowns':13}
  if counts!=expected or verified:errors.append('COUNTS_OR_FALSE_PROMOTION')
  duplicate_extras=sum(n-1 for n in collections.Counter(actual_pdfs.values()).values())
  if duplicate_extras!=5:errors.append('DUPLICATES')
  # Independent semantic fingerprint includes full metadata rows, not raw source bytes.
  semantic={t:[dict(r) for r in c.execute('SELECT * FROM '+t+' ORDER BY 1')] for t in expected}
  result={'passed':not errors,'errors':errors,'counts':counts,'legacy_statuses':dict(collections.Counter(r['legacy_status'] for r in reports.values())),'duplicate_extras':duplicate_extras,'source_verified':verified,'promoted':0,'integrity':integrity(c),'sqlite_configuration':verify_profile(c),'semantic_fingerprint':sha(canonical(semantic).encode()),'reports':export}
  return result
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--db',required=True);a=ap.parse_args();result=verify(WORKSPACE,a.db);write_json(DESIGN/'test_results/COMPATIBILITY_EXPORT.json',result);print(canonical({k:v for k,v in result.items() if k!='reports'}))
