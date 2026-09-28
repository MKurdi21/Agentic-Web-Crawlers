"""Additive, fail-closed recovery coordinator. No scientific/source delivery API.

All mutating methods require an OS-held lease. Outputs are immutable and receipts
are the commit authority. This module does not certify power-loss durability.
"""
import argparse
import contextlib
import ctypes
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import time
import unicodedata
import uuid
from datetime import datetime, timezone

VERSION = 'phase4bc-recovery-v1.0.0'
STATES = ['NOT_STARTED','PREFLIGHT','READY','ATOMIC_UNIT_IN_PROGRESS',
          'MILESTONE_COMMITTED','PREEMPTION_SAFE_POINT','PREEMPTED_BY_USAGE_LIMIT',
          'RECOVERY_PREFLIGHT','RECOVERABLE','RECOVERY_BLOCKED','RUN_COMPLETE','RUN_FAILED']
POLICIES = ['CAN_REPLAY_SAFELY','REQUIRES_CLEAN_RESTART','MUST_NOT_REPLAY']
PIN_KEYS = ['methodology_sha256','context_architecture_sha256','immutable_code_sha256',
            'protected_file_manifest_sha256','source_sha256','current_packet_sha256']
class Blocked(RuntimeError): pass
class Crash(RuntimeError): pass
def now(): return datetime.now(timezone.utc).isoformat()
def ident(s):
    if not isinstance(s,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',s): raise Blocked('IDENTITY')
    return s
def digest(b): return hashlib.sha256(b).hexdigest()
def filehash(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def canonical(v):
    def norm(x):
        if isinstance(x,str): return unicodedata.normalize('NFC',x)
        if isinstance(x,list): return [norm(i) for i in x]
        if isinstance(x,dict):
            out={}
            for k,val in x.items():
                nk=norm(k)
                if nk in out: raise Blocked('NORMALIZED_DUPLICATE_KEY')
                out[nk]=norm(val)
            return out
        return x
    return json.dumps(norm(v),ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def loads(b):
    def pairs(v):
        d={}
        for k,x in v:
            if k in d: raise Blocked('DUPLICATE_KEY')
            d[k]=x
        return d
    try: return json.loads(b,object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(Blocked('NONFINITE')))
    except (ValueError,UnicodeError) as e: raise Blocked('MALFORMED_JSON') from e
def read(p): return loads(Path(p).read_bytes())
def validate_record(value,name):
    """Validate the finite keywords used by our own contracts, not arbitrary schemas."""
    schema=read(Path(__file__).resolve().parents[1]/name)
    def check(v,s):
        types={'object':dict,'array':list,'string':str,'null':type(None),'boolean':bool,'integer':int}
        if 'type' in s:
            ts=s['type'] if isinstance(s['type'],list) else [s['type']]
            if not any(type(v) is types[t] for t in ts):raise Blocked('SCHEMA_TYPE')
        if 'const' in s and v!=s['const']:raise Blocked('SCHEMA_CONST')
        if 'enum' in s and v not in s['enum']:raise Blocked('SCHEMA_ENUM')
        if isinstance(v,str) and 'pattern' in s and not re.fullmatch(s['pattern'],v):raise Blocked('SCHEMA_PATTERN')
        if type(v) is int and 'minimum' in s and v<s['minimum']:raise Blocked('SCHEMA_MINIMUM')
        if isinstance(v,list):
            for x in v:check(x,s.get('items',{}))
        if isinstance(v,dict):
            if set(s.get('required',[]))-v.keys():raise Blocked('SCHEMA_REQUIRED')
            for k,x in v.items():
                if k in s.get('properties',{}):check(x,s['properties'][k])
                elif s.get('additionalProperties') is False:raise Blocked('SCHEMA_EXTRA')
                elif isinstance(s.get('additionalProperties'),dict):check(x,s['additionalProperties'])
    check(value,schema)
def exclusive(p,b):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f: f.write(b);f.flush();os.fsync(f.fileno())
    if p.read_bytes()!=b: raise Blocked('WRITE_READBACK')
def replace(p,v):
    p=Path(p);q=p.with_name(p.name+'.'+uuid.uuid4().hex+'.tmp')
    exclusive(q,canonical(v));os.replace(q,p)
    if p.read_bytes()!=canonical(v): raise Blocked('STATE_READBACK')
def bounded(root,relative):
    p=Path(relative)
    if p.is_absolute() or '..' in p.parts or ':' in str(p): raise Blocked('PATH_ESCAPE')
    root=Path(root).resolve();target=root/p
    for q in [target,*target.parents]:
        if q==root: break
        if q.is_symlink() or (q.exists() and getattr(q.lstat(),'st_file_attributes',0)&0x400): raise Blocked('REPARSE_PATH')
    if not target.resolve().is_relative_to(root): raise Blocked('PATH_ESCAPE')
    return target
def output_path(root,relative):
    # One canonical namespace avoids Windows case/separator/dot/ADS aliases.
    if not isinstance(relative,str) or not re.fullmatch(r'outputs/(?:[a-z0-9_-]+/)*[a-z0-9_-]+(?:\.[a-z0-9_-]+)*',relative):raise Blocked('OUTPUT_NAMESPACE')
    reserved={'con','prn','aux','nul',*[f'com{i}' for i in range(1,10)],*[f'lpt{i}' for i in range(1,10)]}
    if any(x.split('.')[0] in reserved for x in relative.split('/')):raise Blocked('WINDOWS_RESERVED_PATH')
    return bounded(root,relative)
def process_start(pid):
    if os.name!='nt': raise Blocked('UNSUPPORTED_LOCK_PLATFORM')
    k=ctypes.WinDLL('kernel32',use_last_error=True)
    k.OpenProcess.restype=ctypes.c_void_p
    k.OpenProcess.argtypes=[ctypes.c_uint32,ctypes.c_int,ctypes.c_uint32]
    k.GetProcessTimes.argtypes=[ctypes.c_void_p,*([ctypes.c_void_p]*4)]
    k.CloseHandle.argtypes=[ctypes.c_void_p]
    handle=k.OpenProcess(0x1000,False,pid)
    if not handle:
        if ctypes.get_last_error()==87:return None
        raise Blocked('OWNER_LIVENESS_UNKNOWN')
    a,b,c,d=[ctypes.c_uint64() for _ in range(4)]
    try:
        if not k.GetProcessTimes(handle,*[ctypes.byref(x) for x in (a,b,c,d)]):raise Blocked('PROCESS_START_UNKNOWN')
        return str(a.value)
    finally:k.CloseHandle(handle)

class Engine:
    def __init__(self,root): self.root=Path(root).resolve();self.held=False
    @contextlib.contextmanager
    def lock(self,session_id=None):
        import msvcrt
        self.root.mkdir(parents=True,exist_ok=True)
        lock=self.root/'coordinator.lock'
        f=lock.open('a+b');f.seek(0)
        if lock.stat().st_size==0:f.write(b'0');f.flush()
        f.seek(0)
        try:msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:
            f.close();raise Blocked('OS_LOCK_BUSY')
        try:
            p=self.root/'RUN_LOCK.json'
            if p.exists():
                old=read(p)
                if old.get('status')=='HELD':
                    alive=process_start(old['pid'])
                    if alive==old['process_start']: raise Blocked('OWNER_STILL_ALIVE')
                    exclusive(self.root/'lock_diagnostics'/f'{uuid.uuid4().hex}.json',canonical({'old':old,'observed_start':alive,'decision':'RECLAIM_AFTER_OS_LOCK_AND_LIVENESS_CHECK'}))
            self.held=True;self.session_id=session_id
            try:run_id=read(self.root/'RECOVERY_STATE.json').get('run_id')
            except (Blocked,FileNotFoundError):run_id=None
            replace(p,{'pid':os.getpid(),'process_start':process_start(os.getpid()),'session_id':session_id,'heartbeat':now(),'status':'HELD','run_id':run_id})
            yield self
        finally:
            if self.held:
                replace(self.root/'RUN_LOCK.json',{'pid':os.getpid(),'process_start':process_start(os.getpid()),'session_id':session_id,'heartbeat':now(),'status':'RELEASED'})
            self.held=False;f.seek(0);msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1);f.close()
    def require(self,ignore_latch=False):
        if not self.held:raise Blocked('LOCK_REQUIRED')
        latch=self.root/'BLOCKED_LATCH.json'
        if not ignore_latch and latch.exists() and read(latch)['active']:raise Blocked('RECOVERY_LATCHED')
    def state(self):
        s=read(self.root/'RECOVERY_STATE.json')
        validate_record(s,'RECOVERY_STATE.schema.json')
        if s.get('status') not in STATES or s.get('protocol_version')!=VERSION:raise Blocked('STATE_SCHEMA')
        for k in PIN_KEYS:
            if s.get(k) is not None and not re.fullmatch('[0-9a-f]{64}',s[k]):raise Blocked('HASH_FORMAT')
        return s
    def save(self,s):
        s['updated_at']=now();validate_record(s,'RECOVERY_STATE.schema.json');replace(self.root/'RECOVERY_STATE.json',s)
    def journal(self,repair=False):
        files=sorted(self.root.glob('RECOVERY_EVENTS*.jsonl'));events=[];prev=None;seq=0
        for index,p in enumerate(files):
            lines=p.read_bytes().splitlines(keepends=True)
            for j,line in enumerate(lines):
                try:
                    e=loads(line);validate_record(e,'RECOVERY_EVENTS.schema.json');claimed=e.pop('event_sha256')
                    if claimed!=digest(canonical(e)) or e['previous_event_sha256']!=prev or e['sequence']!=seq+1:raise Blocked('JOURNAL_CHAIN')
                except (Blocked,KeyError):
                    marker=self.root/'journal_repairs'/(p.name+'.json')
                    if marker.exists():
                        m=read(marker)
                        if m['segment_sha256']!=filehash(p) or m['line']!=j:raise Blocked('REPAIRED_SEGMENT_CHANGED')
                        break
                    # Only a non-newline-terminated *last* record can be torn.
                    if not repair or index!=len(files)-1 or j!=len(lines)-1 or line.endswith(b'\n'):raise Blocked('JOURNAL_CORRUPTION')
                    exclusive(self.root/'private_quarantine'/f'torn-{uuid.uuid4().hex}.bin',line)
                    exclusive(marker,canonical({'segment_sha256':filehash(p),'line':j,'previous_event_sha256':prev,'reason':'TORN_TERMINAL_RECORD'}))
                    exclusive(self.root/f'RECOVERY_EVENTS_{len(files):04d}.jsonl',b'')
                    break
                e['event_sha256']=claimed;events.append(e);prev=claimed;seq+=1
        return events
    def event(self,kind,**payload):
        self.require(ignore_latch=kind.startswith('RECOVERY_') or kind in ['MILESTONE_RECOVERED','QUARANTINE']);events=self.journal();e={'event_id':uuid.uuid4().hex,'sequence':len(events)+1,'previous_event_sha256':events[-1]['event_sha256'] if events else None,'event_type':kind,'timestamp':now(),'session_id':self.session_id,**payload}
        e['event_sha256']=digest(canonical(e));files=sorted(self.root.glob('RECOVERY_EVENTS*.jsonl'))
        validate_record(e,'RECOVERY_EVENTS.schema.json')
        p=files[-1] if files else self.root/'RECOVERY_EVENTS.jsonl'
        with p.open('ab') as f:f.write(canonical(e)+b'\n');f.flush();os.fsync(f.fileno())
        return e
    def init(self,run_id,pins,phase='SYNTHETIC',bindings=None):
        self.require();ident(run_id)
        if (self.root/'RECOVERY_STATE.json').exists():raise Blocked('RUN_EXISTS')
        for k in PIN_KEYS:
            if pins.get(k) is not None and not re.fullmatch('[0-9a-f]{64}',pins[k]):raise Blocked('PIN_FORMAT')
        s=dict(run_id=run_id,phase_id=phase,phase_version='1.0.0',protocol_version=VERSION,status='READY',methodology_version='phase4br-scientific-v3.0.0',context_architecture_version='phase4bc-context-v1.0.0',current_atomic_unit=None,current_atomic_unit_id=None,atomic_unit_status=None,last_committed_milestone=None,last_committed_milestone_receipt_sha256=None,next_permitted_operation='BEGIN',active_holdout_id=None,active_holdout_state='UNTOUCHED_RESERVED_VALIDATION_EVIDENCE',source_access_started=False,source_access_event_id=None,primary_context_id=None,verifier_context_ids=[],live_source_verified_count=0,live_promoted_count=0,lane_b_state='NOT_AUTHORIZED',created_at=now(),updated_at=now(),usage_headroom='USAGE_HEADROOM_UNKNOWN',bindings=bindings or [],**{k:pins.get(k) for k in PIN_KEYS})
        exclusive(self.root/'INITIAL_STATE.json',canonical(s));self.save(s);self.event('RUN_START',run_id=run_id)
        return s
    def receipts(self):
        remaining=[];genesis=read(self.root/'INITIAL_STATE.json');units=set();owned=set()
        for p in (self.root/'milestone_receipts').glob('*.json'):
            r=read(p)
            validate_record(r,'MILESTONE_RECEIPT.schema.json')
            if r.get('status')!='COMMITTED' or r.get('protocol_version')!=VERSION:raise Blocked('RECEIPT_SCHEMA')
            if r['run_id']!=genesis['run_id'] or r['pins']!={k:genesis[k] for k in PIN_KEYS}:raise Blocked('RECEIPT_IDENTITY')
            if p.stem!=r['attempt_id'] or r['input_sha256']!=digest(canonical(r['input_fingerprints'])):raise Blocked('RECEIPT_INPUT_IDENTITY')
            intent=self.intent(self.root/'intents'/f'{ident(r["attempt_id"])}.json')
            if any(r.get(k)!=v for k,v in intent.items()):raise Blocked('RECEIPT_INTENT_MISMATCH')
            if set(r['output_fingerprints'])!=set(r['expected_outputs']):raise Blocked('RECEIPT_SCOPE')
            if r['atomic_unit_id'] in units or owned.intersection(r['expected_outputs']):raise Blocked('DUPLICATE_COMMIT_OWNERSHIP')
            units.add(r['atomic_unit_id']);owned.update(r['expected_outputs'])
            for rel,h in r['output_fingerprints'].items():
                q=bounded(self.root,rel)
                if not q.is_file() or filehash(q)!=h:raise Blocked('COMMITTED_OUTPUT_MISMATCH')
            remaining.append((filehash(p),r))
        chain=[];prev=None
        while remaining:
            candidates=[x for x in remaining if x[1]['previous_receipt_sha256']==prev]
            if len(candidates)!=1:raise Blocked('RECEIPT_BRANCH_OR_GAP')
            x=candidates[0];chain.append(x);remaining.remove(x);prev=x[0]
        return chain
    def intent(self,p):
        i=read(p);g=read(self.root/'INITIAL_STATE.json')
        expected={'run_id','atomic_unit_id','attempt_id','input_fingerprints','input_sha256','expected_outputs','replay_policy','previous_receipt_sha256','start_time','pins'}
        if set(i)!=expected:raise Blocked('INTENT_FIELDS')
        if ident(i['attempt_id'])!=Path(p).stem or i['run_id']!=g['run_id']:raise Blocked('INTENT_IDENTITY')
        ident(i['atomic_unit_id'])
        if i['pins']!={k:g[k] for k in PIN_KEYS} or i['input_sha256']!=digest(canonical(i['input_fingerprints'])):raise Blocked('INTENT_PINS')
        if i['replay_policy'] not in POLICIES or not isinstance(i['expected_outputs'],list) or len(set(i['expected_outputs']))!=len(i['expected_outputs']):raise Blocked('INTENT_POLICY')
        for rel in i['expected_outputs']:output_path(self.root,rel)
        if i['previous_receipt_sha256'] is not None and not re.fullmatch('[0-9a-f]{64}',i['previous_receipt_sha256']):raise Blocked('INTENT_PREVIOUS_HASH')
        return i
    def begin(self,unit,inputs,outputs,policy='CAN_REPLAY_SAFELY',expensive=False,near_exhaustion=False):
        self.require();s=self.state();ident(unit)
        if expensive and near_exhaustion:raise Blocked('USAGE_NEAR_EXHAUSTION')
        if policy not in POLICIES:raise Blocked('REPLAY_POLICY')
        fingerprint=digest(canonical(inputs))
        for ip in (self.root/'intents').glob('*.json'):
            old=self.intent(ip)
            if old['atomic_unit_id']==unit and old['input_sha256']!=fingerprint:raise Blocked('IDEMPOTENCY_CONFLICT')
        for _,r in self.receipts():
            if r['atomic_unit_id']==unit:
                if r['input_sha256']!=fingerprint:raise Blocked('IDEMPOTENCY_CONFLICT')
                return {'already_committed':True,'receipt':r}
        if s['status'] not in ['READY','RECOVERABLE','MILESTONE_COMMITTED','PREEMPTION_SAFE_POINT']:raise Blocked('ILLEGAL_BEGIN')
        if s['current_atomic_unit_id']:raise Blocked('ACTIVE_UNIT_EXISTS')
        for o in outputs:output_path(self.root,o)
        owned={p for _,r in self.receipts() for p in r['output_fingerprints']}
        if owned.intersection(outputs):raise Blocked('COMMITTED_OUTPUT_OWNERSHIP')
        if len(set(outputs))!=len(outputs):raise Blocked('DUPLICATE_OUTPUT')
        attempt=uuid.uuid4().hex
        intent={'run_id':s['run_id'],'atomic_unit_id':unit,'attempt_id':attempt,'input_fingerprints':inputs,'input_sha256':fingerprint,'expected_outputs':outputs,'replay_policy':policy,'previous_receipt_sha256':s['last_committed_milestone_receipt_sha256'],'start_time':now(),'pins':{k:s[k] for k in PIN_KEYS}}
        exclusive(self.root/'intents'/f'{attempt}.json',canonical(intent))
        replace(self.root/'ACTIVE_OPERATION.json',intent)
        s.update(status='ATOMIC_UNIT_IN_PROGRESS',current_atomic_unit=unit,current_atomic_unit_id=unit,atomic_unit_status='INTENT_PERSISTED',next_permitted_operation='COMMIT_OR_RECOVER');self.save(s)
        self.event('ATOMIC_UNIT_START',unit=unit,attempt_id=attempt,input_sha256=fingerprint)
        return intent
    def commit(self,payloads,next_operation='BEGIN',crash_at=None):
        self.require();s=self.state()
        if s['status']!='ATOMIC_UNIT_IN_PROGRESS':raise Blocked('ILLEGAL_COMMIT')
        i=read(self.root/'ACTIVE_OPERATION.json')
        frozen=self.intent(self.root/'intents'/f'{ident(i["attempt_id"])}.json')
        if i!=frozen or i['run_id']!=s['run_id'] or i['atomic_unit_id']!=s['current_atomic_unit_id'] or i['pins']!={k:s[k] for k in PIN_KEYS} or i['previous_receipt_sha256']!=s['last_committed_milestone_receipt_sha256']:raise Blocked('ACTIVE_INTENT_MISMATCH')
        if set(payloads)!=set(i['expected_outputs']):raise Blocked('OUTPUT_SCOPE')
        outputs={}
        for rel,b in payloads.items():
            if not isinstance(b,bytes):raise Blocked('OUTPUT_BYTES_REQUIRED')
            tmp=self.root/'staging'/i['attempt_id']/rel;exclusive(tmp,b)
            dest=output_path(self.root,rel)
            # Existing bytes without a receipt must be reconciled, not overwritten.
            exclusive(dest,tmp.read_bytes());outputs[rel]=filehash(dest)
        if crash_at=='outputs':raise Crash('OUTPUTS_BEFORE_RECEIPT')
        r={**i,'protocol_version':VERSION,'output_fingerprints':outputs,'commit_time':now(),'status':'COMMITTED','side_effects_committed':['IMMUTABLE_FILE_PUBLICATION'],'scientific_source_access':s['source_access_started'],'validation_consumption_effect':0,'next_operation':next_operation}
        p=self.root/'milestone_receipts'/f'{i["attempt_id"]}.json';exclusive(p,canonical(r))
        if crash_at=='receipt':raise Crash('RECEIPT_BEFORE_JOURNAL')
        self.event('ATOMIC_UNIT_COMMIT',receipt_sha256=filehash(p),unit=i['atomic_unit_id'])
        if crash_at=='journal':raise Crash('JOURNAL_BEFORE_STATE')
        s.update(status='MILESTONE_COMMITTED',last_committed_milestone=i['atomic_unit_id'],last_committed_milestone_receipt_sha256=filehash(p),current_atomic_unit=None,current_atomic_unit_id=None,atomic_unit_status='COMMITTED',next_permitted_operation=next_operation);self.save(s)
        return r
    def preempt(self,reason='USAGE_LIMIT_PREEMPTION'):
        self.require();s=self.state()
        if s['status'] in ['RUN_COMPLETE','RUN_FAILED','RECOVERY_BLOCKED']:raise Blocked('TERMINAL_STATE')
        self.event(reason,last_milestone=s['last_committed_milestone'])
        s['status']='PREEMPTED_BY_USAGE_LIMIT' if reason=='USAGE_LIMIT_PREEMPTION' else 'PREEMPTION_SAFE_POINT';self.save(s)
    def recover(self,observed_pins,continuity=None,session_mode='NEW_SESSION'):
        self.require(ignore_latch=True)
        try:
            self.journal(repair=True)
            try:s=self.state()
            except Blocked as state_error:
                if str(state_error)!='MALFORMED_JSON':raise
                # Preserve damaged material; reconstruct only from immutable genesis + chain.
                raw=(self.root/'RECOVERY_STATE.json').read_bytes();exclusive(self.root/'private_quarantine'/f'state-{uuid.uuid4().hex}.bin',raw)
                s=read(self.root/'INITIAL_STATE.json')
            genesis=read(self.root/'INITIAL_STATE.json');validate_record(genesis,'RECOVERY_STATE.schema.json')
            if any(s.get(k)!=genesis.get(k) for k in [*PIN_KEYS,'run_id','phase_id','bindings','protocol_version']):raise Blocked('STATE_AUTHORITY_DRIFT')
            self.event('RECOVERY_REQUEST',session_mode=session_mode,journal_segment_links=[read(p) for p in sorted((self.root/'journal_repairs').glob('*.json'))])
            for k in PIN_KEYS:
                if observed_pins.get(k)!=s.get(k):raise Blocked('PIN_DRIFT:'+k)
            for b in s['bindings']:
                if filehash(Path(b['path']))!=b['sha256']:raise Blocked('BOUND_INPUT_DRIFT')
            chain=self.receipts();events=self.journal()
            receipt_hashes={h for h,_ in chain}
            for event in events:
                if event['event_type'] in ['ATOMIC_UNIT_COMMIT','MILESTONE_RECOVERED'] and event.get('receipt_sha256') not in receipt_hashes:raise Blocked('COMMITTED_RECEIPT_MISSING')
            if s['last_committed_milestone_receipt_sha256'] and s['last_committed_milestone_receipt_sha256'] not in receipt_hashes:raise Blocked('STATE_COMMIT_ANCHOR_MISSING')
            access=[e for e in events if e['event_type']=='SOURCE_ACCESS_BEGAN']
            if access:
                s.update(source_access_started=True,source_access_event_id=access[-1]['event_id'],active_holdout_state='CONSUMED_VALIDATION_EVIDENCE')
                required={'same_report','unchanged_pins','clean_context','known_scientific_milestone','unambiguous_acceptance','fresh_packet_review'}
                if not continuity or any(continuity.get(k) is not True for k in required):raise Blocked('POST_SOURCE_CONTINUITY_UNKNOWN')
            if chain:
                sha,r=chain[-1]
                if not any(e.get('receipt_sha256')==sha for e in events):self.event('MILESTONE_RECOVERED',receipt_sha256=sha)
                s.update(last_committed_milestone=r['atomic_unit_id'],last_committed_milestone_receipt_sha256=sha,next_permitted_operation=r['next_operation'])
            committed_attempts={r['attempt_id'] for _,r in chain}
            committed_paths={p for _,r in chain for p in r['output_fingerprints']}
            for ip in (self.root/'intents').glob('*.json'):
                i=self.intent(ip)
                if i['attempt_id'] in committed_attempts:continue
                if (self.root/'quarantine'/f'{i["attempt_id"]}.json').exists():continue
                if i['replay_policy']=='MUST_NOT_REPLAY':raise Blocked('AMBIGUOUS_SIDE_EFFECT')
                moved=[]
                for rel in i['expected_outputs']:
                    if rel in committed_paths:raise Blocked('QUARANTINE_COMMITTED_OWNERSHIP')
                    q=bounded(self.root,rel)
                    if q.exists():
                        dest=self.root/'private_quarantine'/i['attempt_id']/rel;dest.parent.mkdir(parents=True,exist_ok=True);os.replace(q,dest);moved.append({'path':rel,'sha256':filehash(dest)})
                exclusive(self.root/'quarantine'/f'{i["attempt_id"]}.json',canonical({'classification':'UNCOMMITTED_RECOVERY_QUARANTINE','intent':i,'moved':moved,'staging_retained':True}))
                self.event('QUARANTINE',attempt_id=i['attempt_id'],replay_policy=i['replay_policy'])
            self.receipts() # Verify no quarantine operation touched committed bytes.
            controls={'INITIAL_STATE.json','RECOVERY_STATE.json','RUN_LOCK.json','ACTIVE_OPERATION.json','BLOCKED_LATCH.json','coordinator.lock'}
            roots={'intents','milestone_receipts','staging','quarantine','private_quarantine','lock_diagnostics','blocked_diagnostics','journal_repairs'}
            known_bound={str(Path(b['path']).resolve()) for b in genesis['bindings']}
            unknown=[]
            for p in self.root.rglob('*'):
                if not p.is_file():continue
                rel=p.relative_to(self.root).as_posix()
                if rel in controls or rel in committed_paths or rel.split('/')[0] in roots or re.fullmatch(r'RECOVERY_EVENTS(?:_\d{4})?\.jsonl',rel) or str(p.resolve()) in known_bound:continue
                unknown.append({'path':rel,'sha256':filehash(p),'classification':'UNCOMMITTED_RECOVERY_QUARANTINE'})
            if unknown:
                exclusive(self.root/'private_quarantine'/f'unregistered-{uuid.uuid4().hex}.json',canonical(unknown))
                raise Blocked('UNREGISTERED_OUTPUTS')
            completed=any(e['event_type']=='RUN_END' for e in events)
            s.update(status='RUN_COMPLETE' if completed else 'RECOVERABLE',current_atomic_unit=None,current_atomic_unit_id=None,atomic_unit_status=None)
            self.event('RECOVERY_PREFLIGHT_PASS',last_milestone=s['last_committed_milestone'],hashes=observed_pins,session_mode=session_mode)
            replace(self.root/'BLOCKED_LATCH.json',{'active':False,'cleared_by':'RECOVERY_PREFLIGHT_PASS','timestamp':now()})
            self.save(s);return s
        except (Blocked,OSError,KeyError) as e:
            # Never conceal corrupt journal by appending into its committed prefix.
            exclusive(self.root/'blocked_diagnostics'/f'{uuid.uuid4().hex}.json',canonical({'verdict':'RECOVERY_BLOCKED','reason':str(e),'timestamp':now()}))
            replace(self.root/'BLOCKED_LATCH.json',{'active':True,'reason':str(e),'timestamp':now()})
            raise Blocked(str(e)) from e
    def source_access_synthetic(self,approval):
        self.require();s=self.state()
        if s['phase_id']!='SYNTHETIC':raise Blocked('REAL_SOURCE_ACCESS_NOT_IMPLEMENTED')
        if approval.get('packet_sha256')!=s['current_packet_sha256'] or approval.get('semantic_status')!='SEMANTIC_CONTEXT_CLEAN':raise Blocked('STALE_PACKET_REVIEW')
        e=self.event('SOURCE_ACCESS_BEGAN',synthetic=True)
        s.update(source_access_started=True,source_access_event_id=e['event_id'],active_holdout_state='CONSUMED_VALIDATION_EVIDENCE');self.save(s)
    def finish(self):
        self.require();s=self.state()
        if s['current_atomic_unit_id'] or s['status'] not in ['RECOVERABLE','MILESTONE_COMMITTED','READY']:raise Blocked('UNFINISHED_UNIT')
        self.receipts();self.event('RUN_END');s['status']='RUN_COMPLETE';s['next_permitted_operation']='STOP';self.save(s)

def sqlite_check(path):
    """Synthetic diagnostics only; never repair or initialize a damaged database."""
    try:
        with sqlite3.connect(Path(path).resolve().as_uri()+'?mode=ro',uri=True) as c:
            c.execute('PRAGMA foreign_keys=ON')
            if c.execute('PRAGMA foreign_keys').fetchone()!=(1,):raise Blocked('FK_CONFIGURATION')
            integrity=c.execute('PRAGMA integrity_check').fetchall();fk=c.execute('PRAGMA foreign_key_check').fetchall()
        return {'integrity_check':integrity,'foreign_key_check':fk,'passed':integrity==[('ok',)] and not fk}
    except sqlite3.DatabaseError as e:return {'passed':False,'quarantine_required':True,'error':str(e)}

def main():
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['init','begin','commit','preempt','recover','finish']);p.add_argument('root');p.add_argument('--request',required=True)
    a=p.parse_args();request=read(a.request)
    with Engine(a.root).lock(request.pop('session_id',None)) as e:
        if a.operation=='commit':
            request['payloads']={k:Path(v).read_bytes() for k,v in request['payload_files'].items()};del request['payload_files']
        result=getattr(e,a.operation)(**request)
        print(canonical(result).decode())
if __name__=='__main__':main()
