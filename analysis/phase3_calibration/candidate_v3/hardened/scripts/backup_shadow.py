"""Quiesced SQLite backup plus independent reopen/restore and store verification."""
import shutil
from common import *
from db import connect,integrity,verify_profile
from artifact_store import reconcile
def snapshot(c):
 tables=[r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
 return {t:[list(r) for r in c.execute('SELECT * FROM '+t+' ORDER BY 1')] for t in tables}
def backup(db,destination):
 destination=guard(destination);restored=guard(destination.with_name(destination.stem+'.restored.sqlite3'))
 with coordinator(),connect(db) as source:
  integrity(source);before=snapshot(source);metadata=dict(source.execute('SELECT key,value FROM metadata'))
  with connect(destination,backup_target=True) as target:source.backup(target);verify_profile(target);integrity(target)
  h=digest(destination)
  # Separate store snapshot. Real research remains inside NEVER_PACKAGE private storage.
  real=any(r[7]=='NEVER_PACKAGE' for r in before['artifacts'])
  store=guard((SHADOW/'private_source_material' if real else SHADOW/'synthetic')/'backups'/uid('store'))
  store.mkdir(parents=True);copied={}
  for r in before['artifacts']:
   sourcepath=pathlib.Path(r[5]);expected=r[1]
   if digest(sourcepath)!=expected:raise Failure('BACKUP_SOURCE_ARTIFACT')
   dest=guard(store/expected)
   if not dest.exists():shutil.copyfile(sourcepath,dest)
   if digest(dest)!=expected:raise Failure('BACKUP_ARTIFACT_COPY')
   copied[expected]=str(dest)
  with connect(destination,readonly=True) as independent:
   checks=integrity(independent);actual=snapshot(independent)
   if actual!=before:raise Failure('BACKUP_SEMANTIC_MISMATCH')
  if digest(destination)!=h:raise Failure('BACKUP_MUTATED_BY_VALIDATION')
  if restored.exists():raise Failure('RESTORE_EXISTS')
  shutil.copyfile(destination,restored)
  with connect(restored,readonly=True) as verify:
   restorechecks=integrity(verify)
   if snapshot(verify)!=before:raise Failure('RESTORE_SEMANTIC_MISMATCH')
   references={r[0] for r in verify.execute('SELECT DISTINCT sha256 FROM artifacts')}
   if references!=set(copied) or any(digest(p)!=h for h,p in copied.items()):raise Failure('RESTORE_STORE_INTEGRITY')
   stores={'passed':True,'referenced_hash_count':len(references),'independent_copies_verified':len(copied)}
  return {'passed':True,'database_uuid':metadata['database_uuid'],'schema_sha256':metadata['schema_sha256'],'schema_version':2,'created_at':stamp(),'source_event_count':len(before['events']),'source_snapshot_sha256':sha(canonical(before).encode()),'backup_sha256':h,'backup':str(destination),'restored':str(restored),'integrity':checks,'restored_integrity':restorechecks,'store':stores,'limitation':'Independent artifact-copy closure verified; relocating immutable registry paths for live cutover remains a separately authorized adapter. No sync durability claim'}
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--db',required=True);ap.add_argument('--destination',required=True);a=ap.parse_args();write_json(DESIGN/'test_results/BACKUP_REPORT.json',backup(a.db,a.destination))
