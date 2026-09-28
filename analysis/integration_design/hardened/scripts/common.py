"""Shadow-only boundary and serialization primitives. No live deployment mode."""
import contextlib, hashlib, json, os, pathlib, sys, time, uuid
DESIGN = pathlib.Path(__file__).resolve().parents[2]
WORKSPACE = DESIGN.parents[1]
SHADOW = DESIGN / 'shadow'
sys.dont_write_bytecode = True
sys.path.insert(0, str(DESIGN / '_deps'))

class Failure(RuntimeError):
    def __init__(self, code, detail=''):
        self.code = code
        super().__init__(f'{code}: {detail}')

def guard(path, root=SHADOW):
    p = pathlib.Path(path).absolute()
    root = pathlib.Path(root).absolute()
    if not p.resolve().is_relative_to(root.resolve()):
        raise Failure('BOUNDARY', str(p))
    for q in [p, *p.parents]:
        if q.exists() and (q.is_symlink() or getattr(q, 'is_junction', lambda:False)()):
            raise Failure('REPARSE', str(q))
        if q == root: break
    return p

def sha(data): return hashlib.sha256(data).hexdigest()
def digest(path):
    with pathlib.Path(path).open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()
def canonical(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
def uid(prefix): return prefix + '_' + uuid.uuid4().hex
def stamp():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write_json(path,obj):
    p=guard(path,DESIGN);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_name(p.name+'.'+uuid.uuid4().hex+'.tmp')
    with temp.open('w',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
    os.replace(temp,p)

@contextlib.contextmanager
def coordinator():
    """Cross-process OS lock; crash releases handle. Includes publication and GC."""
    SHADOW.mkdir(parents=True,exist_ok=True)
    p=guard(SHADOW/'coordinator.lock')
    with p.open('a+b') as f:
        if p.stat().st_size==0: f.write(b'0');f.flush()
        f.seek(0)
        if os.name=='nt':
            import msvcrt
            try: msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
            except OSError as e: raise Failure('COORDINATOR_BUSY') from e
            try: yield
            finally: f.seek(0);msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1)
        else:
            import fcntl
            fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
            try: yield
            finally: fcntl.flock(f,fcntl.LOCK_UN)
