"""Publish complete immutable blobs before SQL references; reconcile without repair."""
from common import *
def publish(root,data,expected=None,failpoint=lambda _:None):
 root=guard(root);root.mkdir(parents=True,exist_ok=True);h=sha(data)
 if expected and expected!=h:raise Failure('SUBMISSION_HASH')
 target=guard(root/h[:2]/h);target.parent.mkdir(exist_ok=True)
 if target.exists():
  if digest(target)!=h or target.read_bytes()!=data:raise Failure('BLOB_INTEGRITY',str(target))
  return target,h
 temp=guard(root/('staging_'+uuid.uuid4().hex+'.tmp'))
 failpoint('before_stage')
 with temp.open('xb') as f:
  f.write(data);failpoint('during_stage');f.flush();os.fsync(f.fileno())
 if digest(temp)!=h:raise Failure('STAGING_HASH')
 failpoint('after_stage')
 try:
  if os.name=='nt':
   # No REPLACE_EXISTING and no COPY_ALLOWED: same-volume, non-overwriting publication.
   import ctypes
   kernel=ctypes.WinDLL('kernel32',use_last_error=True)
   move=kernel.MoveFileExW;move.argtypes=[ctypes.c_wchar_p,ctypes.c_wchar_p,ctypes.c_ulong];move.restype=ctypes.c_int
   if not move(str(temp),str(target),0x8):
    err=ctypes.get_last_error()
    if err in (80,183):raise FileExistsError(str(target))
    raise ctypes.WinError(err)
  else:os.link(temp,target)  # atomic non-overwriting publication
 except FileExistsError:
  if digest(target)!=h or target.read_bytes()!=data:raise Failure('BLOB_INTEGRITY',str(target))
 except OSError as e:raise Failure('PUBLICATION_UNSUPPORTED',str(e)) from e
 if temp.exists():temp.unlink()
 if digest(target)!=h:raise Failure('PUBLISHED_HASH')
 failpoint('after_publish')
 return target,h

def reconcile(c,roots):
 registry={r['path']:r['sha256'] for r in c.execute('SELECT path,sha256 FROM artifacts')}
 result=[];seen=set()
 for root in roots:
  root=guard(root)
  if not root.exists():continue
  for p in root.rglob('*'):
   if not p.is_file():continue
   guard(p,root);seen.add(str(p));h=digest(p);expected=registry.get(str(p))
   if expected:kind='VALID_REFERENCED_BLOB' if h==expected else 'HASH_MISMATCH'
   elif len(p.name)==64 and all(x in '0123456789abcdef' for x in p.name):kind='ORPHAN_BLOB' if p.name==h else 'HASH_MISMATCH'
   else:kind='UNEXPECTED_FILE'
   result.append({'path':str(p),'classification':kind,'sha256':h})
 for path,h in registry.items():
  if path not in seen:
   p=guard(path)
   result.append({'path':path,'classification':'MISSING_REFERENCED_BLOB' if not p.is_file() else 'VALID_REFERENCED_BLOB' if digest(p)==h else 'HASH_MISMATCH','sha256':h})
 return {'passed':not any(x['classification'] in ('MISSING_REFERENCED_BLOB','HASH_MISMATCH') for x in result),'blobs':result}

def collect(c,roots,execute=False,grace_seconds=86400):
 """Caller holds coordinator lock. Destruction restricted to synthetic test stores."""
 report=reconcile(c,roots)
 if not report['passed']:raise Failure('STORE_INTEGRITY',canonical(report))
 protected={r[0] for r in c.execute('SELECT sha256 FROM retention')}
 candidates=[]
 for row in report['blobs']:
  p=pathlib.Path(row['path'])
  if row['classification']=='ORPHAN_BLOB' and row['sha256'] not in protected and time.time()-p.stat().st_mtime>=grace_seconds:
   candidates.append(str(p))
   if execute:
    guard(p,SHADOW/'synthetic')
    if c.execute('SELECT 1 FROM artifacts WHERE sha256=?',(row['sha256'],)).fetchone():raise Failure('GC_RACE')
    p.unlink()
 return {'dry_run':not execute,'candidates':candidates}
