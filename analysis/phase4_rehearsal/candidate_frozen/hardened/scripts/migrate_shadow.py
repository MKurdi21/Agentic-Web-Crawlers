"""Lossless metadata import; historical bytes are private, never scientific acceptance."""
import csv,importlib.util,argparse
from common import *
from db import connect,transaction,integrity,event
from artifact_store import publish,bind_store
def csvrows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def report_id(alias):return 'report_'+sha(alias.encode())[:24]
def import_workspace(workspace,db_path):
 workspace=pathlib.Path(workspace).resolve();audit=workspace/'analysis/workspace_audit';db_path=guard(db_path)
 corpus=csvrows(audit/'CORPUS_INVENTORY.csv');arts=csvrows(audit/'ARTIFACT_INVENTORY.csv');matrix=csvrows(audit/'PAPER_PROCESSING_MATRIX.csv');manifest=csvrows(workspace/'analysis/manifest.csv');byalias={r['summary_name']:r for r in matrix}
 if len(manifest)!=112 or len({r['SummaryName'].casefold() for r in manifest})!=112:raise Failure('MANIFEST_IDENTITIES')
 measured={}
 for r in corpus:
  p=workspace/r['path']
  if not p.is_file() or digest(p)!=r['sha256']:raise Failure('AUDIT_SOURCE_DRIFT',r['path'])
  measured[r['path']]=r
 # Every artifact is checked before the first import transaction.
 for r in arts:
  p=workspace/r['artifact_path']
  if not p.is_file() or digest(p)!=r['sha256']:raise Failure('AUDIT_ARTIFACT_DRIFT',r['artifact_path'])
 spec=importlib.util.spec_from_file_location('legacy_readonly',workspace/'scripts/summary_state.py');legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
 checks={}
 for r in manifest:
  draft=workspace/r['StageTarget'].replace('\\','/');status='pending' if not draft.is_file() else 'structural_pass' if legacy.check_structure(draft)['passed'] else 'needs_repair'
  if status!=byalias[r['SummaryName']]['observed_status']:raise Failure('AUDIT_STATE_DRIFT',r['SummaryName'])
  checks[r['SummaryName']]=status
 if json.loads((workspace/'analysis/reviews.json').read_text())!={}:raise Failure('REVIEW_DRIFT')
 with coordinator(),connect(db_path,create=not db_path.exists()) as c:
  existing=dict(c.execute('SELECT key,value FROM metadata'));inputfp=sha(canonical({'corpus':corpus,'artifacts':arts,'manifest':manifest}).encode())
  if 'import_fingerprint' in existing:
   if existing['import_fingerprint']!=inputfp:raise Failure('IMPORT_DRIFT')
   return {'identical_import':True,'integrity':integrity(c),'input_fingerprint':inputfp}
  with transaction(c):
   now=stamp()
   raw_store=SHADOW/'private_source_material/raw';bind_store(c,raw_store)
   for r in corpus:
    c.execute('INSERT OR IGNORE INTO sources VALUES(?,?,?)',(r['source_id'],r['sha256'],int(r['pdf_pages']) if r['pdf_pages'] else None));c.execute('INSERT INTO observations VALUES(?,?,?)',(str(workspace/r['path']),r['source_id'],now))
   for r in manifest:
    rel=r['Pdf'].replace('\\','/');source=measured[rel];m=byalias[r['SummaryName']];state='SOURCE_REVIEW_PARTIAL' if m['newest_apparent_workflow_state']=='DRAFT_WITH_PARTIAL_REVIEW' else 'STRUCTURALLY_VALID' if checks[r['SummaryName']]=='structural_pass' else 'RAW_IMPORTED_ARTIFACT'
    c.execute('INSERT INTO reports VALUES(?,?,?,?,?,?,?)',(report_id(r['SummaryName']),r['SummaryName'],source['source_id'],str(workspace/rel),checks[r['SummaryName']],state,canonical(r)))
   for r in arts:
    data=(workspace/r['artifact_path']).read_bytes();p,h=publish(raw_store,data,r['sha256']);rid=report_id(r['summary_name']) if r['summary_name'] in byalias else None
    prov={'observed_at':now,'historical_generation':'UNKNOWN','audit_path':r['artifact_path'],'mapping_status':r['mapping_status'],'kind':r['kind']}
    c.execute('INSERT INTO artifacts VALUES(?,?,?,?,?,?,?,?,?)',('historical_'+sha(r['artifact_path'].encode())[:24],h,'RAW_REGISTERED_HISTORICAL_ARTIFACT',r['kind'],rid,str(p),r['artifact_path'],'NEVER_PACKAGE',canonical(prov)))
   for name in ['baseline.json','checkpoint.json','reviews.json']:
    data=(workspace/'analysis'/name).read_bytes();p,h=publish(raw_store,data)
    c.execute('INSERT INTO history VALUES(?,?,?)',(name,'DATED_OBSERVATION',canonical({'path':str(p),'sha256':h,'meaning':name})))
    c.execute('INSERT OR IGNORE INTO retention VALUES(?,?)',(h,'HISTORICAL_CONTROL'))
   # Preserve all retained historical run metadata in the private bytes, without backfilling older runs.
   measures=json.loads((audit/'AUDIT_MEASUREMENTS.json').read_text())
   bypath={r['Pdf'].replace('\\','/'):report_id(r['SummaryName']) for r in manifest}
   for pair in measures['near_candidates']:
    a,b=bypath[pair['path_a']],bypath[pair['path_b']]
    c.execute('INSERT INTO relationships VALUES(?,?,?,?,?)',('relationship_'+sha((a+b).encode())[:24],a,b,'UNRESOLVED',canonical(pair)))
   for u in json.loads((audit/'UNRESOLVED_REGISTER.json').read_text()):c.execute('INSERT INTO unknowns VALUES(?,?)',(u['id'],canonical(u)))
   c.execute('INSERT INTO metadata VALUES(?,?)',('import_fingerprint',inputfp));event(c,'HISTORICAL_IMPORT',inputfp,{'reports':112,'source_verified':0,'promoted':0},'import_'+inputfp)
  return {'identical_import':False,'integrity':integrity(c),'input_fingerprint':inputfp}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--db',required=True);a=ap.parse_args();print(canonical(import_workspace(WORKSPACE,a.db)))
if __name__=='__main__':main()
