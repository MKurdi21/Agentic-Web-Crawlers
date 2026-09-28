"""Verify the exact frozen third-party inventory before importing its code."""
import hashlib,json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
def filehash(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def verify(root,manifest,hashfn=filehash):
 root=Path(root);expected={x['relative_path']:x['sha256'] for x in manifest}
 entries=list(root.rglob('*'))
 if any(p.is_symlink() for p in entries):raise RuntimeError('RUNTIME_DEPENDENCY_LINK')
 actual={p.relative_to(root).as_posix() for p in entries if p.is_file()}
 if actual!=set(expected):raise RuntimeError('RUNTIME_DEPENDENCY_INVENTORY_DRIFT')
 with ThreadPoolExecutor(max_workers=8) as pool:
  if not all(pool.map(lambda rel:hashfn(root/rel)==expected[rel],sorted(expected))):raise RuntimeError('RUNTIME_DEPENDENCY_DRIFT')
 return True
