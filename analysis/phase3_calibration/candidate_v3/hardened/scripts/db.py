"""The sole sqlite3.connect call site. Explicit fail-closed bootstrap."""
import contextlib,json,pathlib,sqlite3
from common import *
APP_ID=0x4C525632
SCHEMA=DESIGN/'hardened/db/schema_v2.sql'
PROFILE={'foreign_keys':1,'journal_mode':'delete','synchronous':3,'application_id':APP_ID,'user_version':2,'busy_timeout':5000,'read_uncommitted':0,'ignore_check_constraints':0,'trusted_schema':0,'temp_store':2}

def observed(c): return {k:c.execute('PRAGMA '+k).fetchone()[0] for k in PROFILE}
def verify_profile(c):
    got=observed(c)
    if got!=PROFILE: raise Failure('SQLITE_CONFIGURATION',canonical(got))
    return got

@contextlib.contextmanager
def connect(path,create=False,readonly=False,backup_target=False):
    p=guard(path)
    if create or backup_target:
        if p.exists(): raise Failure('DATABASE_EXISTS',str(p))
        p.parent.mkdir(parents=True,exist_ok=True)
    elif not p.is_file(): raise Failure('DATABASE_MISSING',str(p))
    c=sqlite3.connect(p.as_uri()+('?mode=ro' if readonly else '?mode=rwc' if create or backup_target else '?mode=rw'),uri=True,isolation_level=None)
    c.row_factory=sqlite3.Row
    try:
        for k,v in PROFILE.items():
            if k not in ('application_id','user_version','journal_mode'): c.execute(f'PRAGMA {k}={v}')
        if create or backup_target:
            c.execute('PRAGMA journal_mode=DELETE')
            c.execute(f'PRAGMA application_id={APP_ID}');c.execute('PRAGMA user_version=2')
        verify_profile(c)
        if create:
            c.executescript('BEGIN IMMEDIATE;\n'+SCHEMA.read_text(encoding='utf-8')+'\nCOMMIT;')
            with transaction(c):
                c.executemany('INSERT INTO metadata VALUES(?,?)',[('database_uuid',uid('db')),('schema_sha256',digest(SCHEMA)),('authority','NON_AUTHORITATIVE_SHADOW'),('created_at',stamp())])
            integrity(c)
        if not backup_target:
            meta=dict(c.execute('SELECT key,value FROM metadata'))
            if meta.get('authority')!='NON_AUTHORITATIVE_SHADOW' or meta.get('schema_sha256')!=digest(SCHEMA): raise Failure('DATABASE_IDENTITY')
        if readonly: c.execute('PRAGMA query_only=ON')
        yield c
    finally: c.close()

@contextlib.contextmanager
def transaction(c):
    c.execute('BEGIN IMMEDIATE')
    try: yield;c.execute('COMMIT')
    except BaseException:
        if c.in_transaction:c.execute('ROLLBACK')
        raise

def integrity(c):
    result={'integrity_check':[r[0] for r in c.execute('PRAGMA integrity_check')],'foreign_key_check':[list(r) for r in c.execute('PRAGMA foreign_key_check')]}
    if result!={'integrity_check':['ok'],'foreign_key_check':[]}: raise Failure('DATABASE_INTEGRITY',canonical(result))
    return result

def event(c,kind,subject,payload,identity=None):
    c.execute('INSERT OR IGNORE INTO events VALUES(?,?,?,?,?)',(identity or uid('event'),kind,subject,canonical(payload),stamp()))
