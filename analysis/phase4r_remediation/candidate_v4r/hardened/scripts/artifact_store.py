"""Immutable blob publication and fail-closed, database-bound reconciliation."""
from common import *

STORE_METADATA = '.artifact-store.json'
STORE_METADATA_VERSION = 1
FAILURE_CLASSES = {'MISSING_REFERENCED_BLOB', 'HASH_MISMATCH', 'UNEXPECTED_FILE'}

def database_id(c):
 row=c.execute("SELECT value FROM metadata WHERE key='database_uuid'").fetchone()
 if not row or not row[0]:raise Failure('DATABASE_IDENTITY')
 return row[0]

def expected_store_id(db_id,root):
 root=guard(root)
 return 'store_'+sha((db_id+'\x00'+str(root.resolve())).encode('utf-8'))[:24]

def _metadata(root,db_id,artifact_store_id=None):
 root=guard(root)
 return {'metadata_version':STORE_METADATA_VERSION,'artifact_store_id':artifact_store_id or expected_store_id(db_id,root),'database_id':db_id,'root':str(root.resolve())}

def bind_store(c,root,artifact_store_id=None):
 """Create the sole allowed control file, or verify its exact store binding."""
 root=guard(root);root.mkdir(parents=True,exist_ok=True);wanted=_metadata(root,database_id(c),artifact_store_id);control=guard(root/STORE_METADATA,root)
 if control.exists():
  try:actual=json.loads(control.read_text(encoding='utf-8'))
  except (OSError,UnicodeError,json.JSONDecodeError) as e:raise Failure('STORE_METADATA_INVALID',str(control)) from e
  if actual!=wanted:raise Failure('STORE_IDENTITY',canonical({'expected':wanted,'actual':actual}))
  return wanted
 temp=guard(root/(STORE_METADATA+'.'+uuid.uuid4().hex+'.tmp'),root)
 with temp.open('x',encoding='utf-8',newline='\n') as f:
  f.write(json.dumps(wanted,indent=2,ensure_ascii=False,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
 try:
  os.link(temp,control)
 except FileExistsError:pass
 except OSError as e:
  if os.name!='nt':raise Failure('STORE_METADATA_PUBLICATION',str(e)) from e
  try:
   import ctypes
   kernel=ctypes.WinDLL('kernel32',use_last_error=True);move=kernel.MoveFileExW;move.argtypes=[ctypes.c_wchar_p,ctypes.c_wchar_p,ctypes.c_ulong];move.restype=ctypes.c_int
   if not move(str(temp),str(control),0x8):
    err=ctypes.get_last_error()
    if err not in (80,183):raise ctypes.WinError(err)
  except OSError as win_error:raise Failure('STORE_METADATA_PUBLICATION',str(win_error)) from win_error
 finally:
  if temp.exists():temp.unlink()
 if json.loads(control.read_text(encoding='utf-8'))!=wanted:raise Failure('STORE_IDENTITY')
 return wanted

def publish(root,data,expected=None,failpoint=lambda _:None):
 root=guard(root);root.mkdir(parents=True,exist_ok=True);h=sha(data)
 if expected and expected!=h:raise Failure('SUBMISSION_HASH')
 target=guard(root/h[:2]/h);target.parent.mkdir(exist_ok=True)
 if target.exists():
  if digest(target)!=h or target.read_bytes()!=data:raise Failure('BLOB_INTEGRITY',str(target))
  return target,h
 run_id='publish_'+uuid.uuid4().hex;submission_id='submission_'+uuid.uuid4().hex
 stage_dir=guard(root/'.staging'/run_id/submission_id,root);stage_dir.mkdir(parents=True,exist_ok=False)
 temp=guard(stage_dir/'candidate.tmp',root);failpoint('before_stage')
 with temp.open('xb') as f:
  f.write(data);failpoint('during_stage');f.flush();os.fsync(f.fileno())
 if digest(temp)!=h:raise Failure('STAGING_HASH')
 failpoint('after_stage')
 try:
  if os.name=='nt':
   import ctypes
   kernel=ctypes.WinDLL('kernel32',use_last_error=True);move=kernel.MoveFileExW;move.argtypes=[ctypes.c_wchar_p,ctypes.c_wchar_p,ctypes.c_ulong];move.restype=ctypes.c_int
   if not move(str(temp),str(target),0x8):
    err=ctypes.get_last_error()
    if err in (80,183):raise FileExistsError(str(target))
    raise ctypes.WinError(err)
  else:os.link(temp,target)
 except FileExistsError:
  if digest(target)!=h or target.read_bytes()!=data:raise Failure('BLOB_INTEGRITY',str(target))
 except OSError as e:raise Failure('PUBLICATION_UNSUPPORTED',str(e)) from e
 if temp.exists():temp.unlink()
 for directory in (stage_dir,stage_dir.parent,stage_dir.parent.parent):
  try:directory.rmdir()
  except OSError:break
 if digest(target)!=h:raise Failure('PUBLISHED_HASH')
 failpoint('after_publish');return target,h

def _active_staging(relative,active_publications):
 parts=relative.parts
 return len(parts)==4 and parts[0]=='.staging' and (parts[1],parts[2],relative.as_posix()) in active_publications

def reconcile(c,roots,active_publications=()):
 """Scan explicit roots. Never initialize, repair, or cross DB identities."""
 db_id=database_id(c);roots=[guard(r) for r in roots];resolved=[r.resolve() for r in roots]
 if len(set(resolved))!=len(resolved):raise Failure('DUPLICATE_STORE_ROOT')
 for i,a in enumerate(resolved):
  for b in resolved[i+1:]:
   if a.is_relative_to(b) or b.is_relative_to(a):raise Failure('OVERLAPPING_STORE_ROOTS')
 registry={str(pathlib.Path(r['path']).resolve()):r['sha256'] for r in c.execute('SELECT path,sha256 FROM artifacts')}
 result=[];seen=set();failure_reasons=[];store_ids=[];active=set(active_publications)
 for root in roots:
  if not root.exists():failure_reasons.append({'code':'STORE_ROOT_MISSING','root':str(root)});continue
  control=guard(root/STORE_METADATA,root)
  try:
   meta=json.loads(control.read_text(encoding='utf-8'));expected=_metadata(root,db_id,meta.get('artifact_store_id'))
   if meta!=expected:raise ValueError('metadata fields or database/root binding differ')
   if meta['artifact_store_id'] in store_ids:raise ValueError('duplicate artifact_store_id')
   store_ids.append(meta['artifact_store_id'])
  except (OSError,UnicodeError,json.JSONDecodeError,ValueError,AttributeError) as e:
   failure_reasons.append({'code':'STORE_IDENTITY','root':str(root),'detail':str(e)});continue
  for p in sorted(root.rglob('*'),key=lambda q:q.as_posix()):
   if not p.is_file():continue
   guard(p,root);absolute=str(p.resolve());seen.add(absolute);h=digest(p);expected_hash=registry.get(absolute);relative=p.relative_to(root)
   if p==control:kind='EXPECTED_CONTROL_FILE'
   elif _active_staging(relative,active):kind='EXPECTED_CONTROL_FILE'
   elif expected_hash:kind='VALID_REFERENCED_BLOB' if h==expected_hash else 'HASH_MISMATCH'
   elif len(p.name)==64 and all(x in '0123456789abcdef' for x in p.name):kind='ORPHAN_BLOB' if p.name==h else 'HASH_MISMATCH'
   else:kind='UNEXPECTED_FILE'
   result.append({'path':absolute,'classification':kind,'sha256':h})
 for path,h in registry.items():
  if path not in seen:
   p=guard(path);result.append({'path':path,'classification':'MISSING_REFERENCED_BLOB' if not p.is_file() else 'VALID_REFERENCED_BLOB' if digest(p)==h else 'HASH_MISMATCH','sha256':h})
 counts={kind:sum(x['classification']==kind for x in result) for kind in ['VALID_REFERENCED_BLOB','EXPECTED_CONTROL_FILE','ORPHAN_BLOB','MISSING_REFERENCED_BLOB','HASH_MISMATCH','UNEXPECTED_FILE']}
 failure_reasons += [{'code':kind,'count':counts[kind]} for kind in sorted(FAILURE_CLASSES) if counts[kind]]
 gate=not failure_reasons;scan_body={'artifact_store_ids':store_ids,'database_id':db_id,'scanned_roots':[str(r.resolve()) for r in roots],'entries':result}
 return {'store_id':store_ids[0] if len(store_ids)==1 else store_ids,'database_id':db_id,'scanned_root':str(roots[0].resolve()) if len(roots)==1 else [str(r.resolve()) for r in roots],'classification_counts':counts,'entries':result,'gate_passed':gate,'failure_reasons':failure_reasons,'scan_fingerprint':sha(canonical(scan_body).encode('utf-8')),'passed':gate,'blobs':result}

def collect(c,roots,execute=False,grace_seconds=86400):
 """Caller holds coordinator lock. Destruction restricted to synthetic test stores."""
 report=reconcile(c,roots)
 if not report['passed']:raise Failure('STORE_INTEGRITY',canonical(report))
 protected={r[0] for r in c.execute('SELECT sha256 FROM retention')};candidates=[]
 for row in report['entries']:
  p=pathlib.Path(row['path'])
  if row['classification']=='ORPHAN_BLOB' and row['sha256'] not in protected and time.time()-p.stat().st_mtime>=grace_seconds:
   candidates.append(str(p))
   if execute:
    guard(p,SHADOW/'synthetic')
    if c.execute('SELECT 1 FROM artifacts WHERE sha256=?',(row['sha256'],)).fetchone():raise Failure('GC_RACE')
    p.unlink()
 return {'dry_run':not execute,'candidates':candidates}
