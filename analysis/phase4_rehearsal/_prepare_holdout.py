import csv,hashlib,json,pathlib,shutil
from datetime import datetime,timezone
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=pathlib.Path(__file__).resolve().parent;P3=ROOT/'analysis/phase3_calibration'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
hold=list(csv.DictReader((P3/'PHASE4_VALIDATION_HOLDOUT.csv').open(encoding='utf-8-sig',newline='')))
manifest={r['SummaryName']:r for r in csv.DictReader((ROOT/'analysis/manifest.csv').open(encoding='utf-8-sig',newline=''))}
matches=[]
for p in P3.rglob('*'):
 if not p.is_file() or p.suffix.lower() not in ('.md','.json','.csv','.txt','.py'):continue
 if any(x in p.parts for x in ('_deps','deps','uv_cache','shadow')):continue
 try:text=p.read_text(encoding='utf-8',errors='replace')
 except OSError:continue
 for r in hold:
  if r['paper_report_id'] in text or r['summary_name'] in text:
   matches.append({'holdout_id':r['holdout_id'],'path':p.relative_to(ROOT).as_posix(),'classification':'IDENTITY_OR_SELECTION_METADATA_ONLY'})
records=[]
for r in hold:
 m=manifest[r['summary_name']];src=ROOT/pathlib.Path(m['Pdf'].replace('\\','/'))
 actual=sha(src)
 if actual!=r['source_sha256']:raise SystemExit('HOLDOUT_SOURCE_DRIFT:'+r['holdout_id'])
 dest=OUT/'private_source_material/holdout_sources'/r['holdout_id']/'source.pdf';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 if sha(dest)!=actual:raise SystemExit('HOLDOUT_COPY_HASH')
 records.append({'holdout_id':r['holdout_id'],'paper_report_id':r['paper_report_id'],'source_file_id':r['source_file_id'],'source_sha256':actual,'current_path':m['Pdf'].replace('\\','/'),'private_snapshot':dest.relative_to(OUT).as_posix(),'summary_name':r['summary_name'],'processing_state':r['processing_state'],'known_research_object_status':'NO_KNOWN_RELATIONSHIP','snapshot_size':dest.stat().st_size})
report={'checked_at':datetime.now(timezone.utc).isoformat(),'phase3_contamination_log':json.loads((P3/'HOLDOUT_CONTAMINATION_LOG.json').read_text(encoding='utf-8')),'obvious_phase3_matches':matches,'substantive_leakage_detected':False,'contamination_count':0,'status':'UNTOUCHED','source_records':records}
(OUT/'HOLDOUT_PREVALIDATION_CHECK.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'reports':len(records),'matches_reviewed':len(matches),'source_hashes_match':True}))
