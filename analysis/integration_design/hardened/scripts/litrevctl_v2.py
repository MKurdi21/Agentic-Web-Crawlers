"""Non-authoritative shadow controller. No generation or deployment command."""
import argparse
from common import *
from db import connect,transaction,event,integrity
from artifact_store import publish,reconcile,collect
from validate_semantics import validate
STAGES={'NORMALIZE':'normalized_paper','SUMMARIZE':'summary','EXTRACT':'evidence','VERIFY':'verification','RESOLVE_OBJECT':'research_object','CODE_TAXONOMY':'paper_taxonomy_coding','TAXONOMY':'taxonomy','CONTRADICTION':'contradiction','SYNTHESIS':'synthesis','GAP':'gap_candidate','RQ':'research_question'}
PRE={'NORMALIZE':[],'SUMMARIZE':['NORMALIZE'],'EXTRACT':['SUMMARIZE'],'VERIFY':['EXTRACT'],'RESOLVE_OBJECT':['VERIFY'],'CODE_TAXONOMY':['VERIFY'],'TAXONOMY':[],'CONTRADICTION':['VERIFY'],'SYNTHESIS':['VERIFY','RESOLVE_OBJECT','CODE_TAXONOMY'],'GAP':['SYNTHESIS'],'RQ':['GAP']}
PINKEYS={'NORMALIZE':['source','normalization'],'SUMMARIZE':['source','prompt','summary_schema'],'EXTRACT':['source','prompt','evidence_schema'],'VERIFY':['source','verification'],'RESOLVE_OBJECT':['source','research_object'],'CODE_TAXONOMY':['source','taxonomy'],'TAXONOMY':['taxonomy'],'CONTRADICTION':['synthesis'],'SYNTHESIS':['taxonomy','research_object','synthesis'],'GAP':['synthesis','gap_policy'],'RQ':['synthesis','gap_policy','external_policy']}
def fingerprint(pins,stage):
 result={k:pins[k] for k in ['code','runtime','worker_protocol',*PINKEYS[stage]]}
 result['effective_code']={'version':'2.0.0','sha256':sha(canonical({name:digest(DESIGN/'hardened/scripts'/name) for name in ['common.py','db.py','artifact_store.py','validate_semantics.py','litrevctl_v2.py']}).encode())}
 result['effective_schema']={'version':'2.0.0','sha256':digest(DESIGN/'hardened/schemas'/f'{STAGES[stage]}.schema.json')}
 result['effective_runtime']={'version':'2.0.0','sha256':sha(sys.version.encode())}
 if stage in ('SUMMARIZE','EXTRACT'):result['effective_prompt']={'version':'2.0.0','sha256':digest(WORKSPACE/'analysis/PROMPT.md')}
 return result
def row(c,table,key,value):
 r=c.execute(f'SELECT * FROM {table} WHERE {key}=?',(value,)).fetchone()
 if r is None:raise Failure('NOT_FOUND',f'{table}:{value}')
 return dict(r)
def make_run(db,pins):
 for key in set(k for vals in PINKEYS.values() for k in vals)|{'code','runtime','worker_protocol'}:
  if key not in pins or set(pins[key])!={'version','sha256'}:raise Failure('PIN_REQUIRED',key)
  from validate_semantics import fmt
  if not fmt('sha256',pins[key]['sha256']) or not fmt('semver',pins[key]['version']):raise Failure('PIN_FORMAT',key)
 with coordinator(),connect(db) as c,transaction(c):
  rid=uid('run');c.execute('INSERT INTO runs(run_id,pins_json) VALUES(?,?)',(rid,canonical(pins)));event(c,'RUN_CREATED',rid,{'pins':pins});return rid
def enqueue(db,run,report,stage,prerequisites=None):
 if stage not in STAGES:raise Failure('STAGE')
 with coordinator(),connect(db) as c,transaction(c):
  r=row(c,'reports','paper_report_id',report);pins=json.loads(row(c,'runs','run_id',run)['pins_json']);pre=prerequisites or []
  found=[]
  for t in pre:
   q=row(c,'tasks','task_id',t)
   if q['run_id']!=run or q['paper_report_id']!=report:raise Failure('PREREQUISITE_SCOPE')
   found.append(q['stage'])
  if set(found)!=set(PRE[stage]):raise Failure('PREREQUISITES_REQUIRED',canonical(PRE[stage]))
  tid=uid('task');c.execute('INSERT INTO tasks(task_id,run_id,paper_report_id,stage,state,source_id,pins_json,prerequisites_json) VALUES(?,?,?,?,?,?,?,?)',(tid,run,report,stage,'PENDING',r['source_id'],canonical(fingerprint(pins,stage)),canonical(pre)));event(c,'TASK_CREATED',tid,{'stage':stage});return tid
def prerequisites(c,t):
 for tid in json.loads(t['prerequisites_json']):
  a=c.execute('SELECT a.valid,t.state FROM accepted a JOIN tasks t USING(task_id) WHERE task_id=?',(tid,)).fetchone()
  if not a or not a['valid'] or a['state']!='ACCEPTED':raise Failure('PREREQUISITE_NOT_ACCEPTED',tid)
def claim(db,task,worker,ttl=300):
 if ttl<=0 or ttl>3600:raise Failure('LEASE_DURATION')
 with coordinator(),connect(db) as c,transaction(c):
  t=row(c,'tasks','task_id',task);prerequisites(c,t)
  if t['state'] not in ('PENDING','RETRYABLE'):raise Failure('NOT_CLAIMABLE')
  count=c.execute('SELECT count(*) FROM attempts WHERE task_id=?',(task,)).fetchone()[0]
  if count>=t['max_attempts']:raise Failure('RETRY_LIMIT')
  aid=uid('attempt');token=uuid.uuid4().hex;gen=t['generation']+1
  r=row(c,'reports','paper_report_id',t['paper_report_id'])
  private=not pathlib.Path(r['source_path']).resolve().is_relative_to(SHADOW/'synthetic')
  outbox=guard((SHADOW/'private_source_material' if private else SHADOW/'synthetic')/'outboxes'/aid);outbox.mkdir(parents=True)
  expiry=time.time()+ttl
  c.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?,?,?)',(aid,task,count+1,worker,token,gen,expiry,'CLAIMED',str(outbox)))
  c.execute("UPDATE tasks SET current_attempt=?,generation=?,state='CLAIMED' WHERE task_id=?",(aid,gen,task));event(c,'CLAIMED',task,{'attempt_id':aid,'generation':gen})
  return {'task_id':task,'attempt_id':aid,'attempt_number':count+1,'run_id':t['run_id'],'worker':worker,'token':token,'generation':gen,'expiry':expiry,'source_sha256':row(c,'sources','source_id',t['source_id'])['sha256'],'paper_report_id':r['paper_report_id'],'stage':t['stage'],'pins':json.loads(t['pins_json']),'outbox':str(outbox)}
def heartbeat(db,attempt,worker,token,ttl=300):
 if ttl<=0 or ttl>3600:raise Failure('LEASE_DURATION')
 with coordinator(),connect(db) as c,transaction(c):
  a=row(c,'attempts','attempt_id',attempt);t=row(c,'tasks','task_id',a['task_id'])
  if a['worker']!=worker or a['token']!=token or a['expiry']<=time.time() or t['current_attempt']!=attempt or a['state'] not in ('CLAIMED','RUNNING'):raise Failure('HEARTBEAT_STALE')
  c.execute("UPDATE attempts SET expiry=?,state='RUNNING' WHERE attempt_id=?",(time.time()+ttl,attempt));c.execute("UPDATE tasks SET state='RUNNING' WHERE task_id=?",(t['task_id'],));event(c,'HEARTBEAT',attempt,{})
def reap(db):
 with coordinator(),connect(db) as c,transaction(c):
  ids=[]
  for a in c.execute("SELECT * FROM attempts WHERE state IN ('CLAIMED','RUNNING','RESULT_READY') AND expiry<=?",(time.time(),)).fetchall():
   c.execute("UPDATE attempts SET state='SUPERSEDED' WHERE attempt_id=?",(a['attempt_id'],));c.execute("UPDATE tasks SET state=CASE WHEN generation>=max_attempts THEN 'FAILED' ELSE 'RETRYABLE' END WHERE task_id=? AND current_attempt=?",(a['task_id'],a['attempt_id']));event(c,'LEASE_REAPED',a['attempt_id'],{});ids.append(a['attempt_id'])
  return ids
def invalidate(c,t,reason):
 pending=[t];seen=set()
 while pending:
  q=pending.pop()
  if q['task_id'] in seen:continue
  seen.add(q['task_id']);c.execute("UPDATE tasks SET state='INVALIDATED' WHERE task_id=?",(q['task_id'],));c.execute('UPDATE accepted SET valid=0 WHERE task_id=?',(q['task_id'],))
  if q['current_attempt']:c.execute("UPDATE attempts SET state='INVALIDATED' WHERE attempt_id=?",(q['current_attempt'],))
  c.execute('UPDATE records SET current=0 WHERE artifact_sha256 IN (SELECT ar.sha256 FROM artifacts ar JOIN accepted a USING(artifact_id) WHERE task_id=?)',(q['task_id'],))
  event(c,'INVALIDATED',q['task_id'],{'reason':reason})
  for other in c.execute('SELECT * FROM tasks WHERE run_id=?',(q['run_id'],)):
   if q['task_id'] in json.loads(other['prerequisites_json']):pending.append(dict(other))
def update_pins(db,run,pins):
 with coordinator(),connect(db) as c,transaction(c):
  old=json.loads(row(c,'runs','run_id',run)['pins_json']);old.update(pins)
  for key,value in pins.items():
   from validate_semantics import fmt
   if set(value)!={'version','sha256'} or not fmt('sha256',value['sha256']) or not fmt('semver',value['version']):raise Failure('PIN_FORMAT',key)
  c.execute('UPDATE runs SET pins_json=? WHERE run_id=?',(canonical(old),run))
  for t in c.execute('SELECT * FROM tasks WHERE run_id=?',(run,)).fetchall():
   if json.loads(t['pins_json'])!=fingerprint(old,t['stage']):invalidate(c,dict(t),'PINS_CHANGED')
  event(c,'PINS_CHANGED',run,{'changed':list(pins)})
def guarded(c,t,a,e):
 if t['current_attempt']!=a['attempt_id'] or a['state'] not in ('CLAIMED','RUNNING','RESULT_READY') or t['state'] not in ('CLAIMED','RUNNING','RESULT_READY') or a['expiry']<=time.time():raise Failure('STALE_ATTEMPT')
 for k,actual in [('worker',a['worker']),('token',a['token']),('attempt_number',a['number']),('generation',a['generation']),('run_id',t['run_id']),('paper_report_id',t['paper_report_id'])]:
  if e[k]!=actual:raise Failure('ENVELOPE_'+k.upper())
 if t['generation']!=a['generation'] or t['source_id']!=row(c,'reports','paper_report_id',t['paper_report_id'])['source_id']:raise Failure('SOURCE_VERSION')
 if e['source_sha256']!=row(c,'sources','source_id',t['source_id'])['sha256']:raise Failure('SOURCE_VERSION')
 if e['kind']!=STAGES[t['stage']]:raise Failure('STAGE_OUTPUT')
 if json.loads(t['pins_json'])!=fingerprint(json.loads(row(c,'runs','run_id',t['run_id'])['pins_json']),t['stage']):raise Failure('STALE_PINS')
 prerequisites(c,t)
def accept(db,envelope,failpoint=lambda _:None):
 e=validate('worker_result',envelope);data=None;blob=None;h=None;t=None
 with coordinator(),connect(db) as c:
  try:
   t=row(c,'tasks','task_id',e['task_id']);a=row(c,'attempts','attempt_id',e['attempt_id'])
   if a['task_id']!=t['task_id']:raise Failure('ATTEMPT_TASK')
   output=guard(e['output_path'],pathlib.Path(a['outbox']));data=output.read_bytes();h=sha(data)
   if h!=e['output_sha256']:raise Failure('SUBMISSION_HASH')
   key=(e['run_id'],e['task_id'],e['attempt_id'],e['submission_id']);request_hash=sha((canonical(e)+h).encode())
   prior=c.execute('SELECT * FROM replay WHERE run_id=? AND task_id=? AND attempt_id=? AND submission_id=?',key).fetchone()
   if prior:
    if prior['digest']!=request_hash:raise Failure('REPLAY_CONFLICT')
    prior_art=row(c,'artifacts','artifact_id',json.loads(prior['receipt_json'])['artifact_id'])
    if not pathlib.Path(prior_art['path']).is_file() or digest(prior_art['path'])!=prior_art['sha256']:raise Failure('REPLAY_ARTIFACT_INTEGRITY')
    return json.loads(prior['receipt_json'])
   guarded(c,t,a,e)
   r=row(c,'reports','paper_report_id',t['paper_report_id']);path=pathlib.Path(r['source_path'])
   observed=digest(path) if path.is_file() else None
   if observed!=e['source_sha256']:
    with transaction(c):
     if observed:
      sid='sha256:'+observed;c.execute('INSERT OR IGNORE INTO sources VALUES(?,?,NULL)',(sid,observed));c.execute('INSERT OR IGNORE INTO observations VALUES(?,?,?)',(str(path),sid,stamp()));c.execute('UPDATE reports SET source_id=? WHERE paper_report_id=?',(sid,r['paper_report_id']))
     invalidate(c,t,'SOURCE_CHANGED')
    raise Failure('SOURCE_CHANGED')
   p=validate(e['kind'],data,c,{'paper_report_id':t['paper_report_id'],'source_sha256':e['source_sha256']})
   if e['kind']=='verification' and p['protocol_sha256']!=json.loads(t['pins_json'])['verification']['sha256']:raise Failure('VERIFICATION_PROTOCOL')
   privacy='SYNTHETIC' if path.resolve().is_relative_to(SHADOW/'synthetic') else 'NEVER_PACKAGE'
   root=(SHADOW/'synthetic' if privacy=='SYNTHETIC' else SHADOW/'private_source_material')/'stores'/sha(str(pathlib.Path(db).resolve()).encode())[:24]
   blob,h=publish(root,data,h,failpoint)
   failpoint('before_transaction')
   with transaction(c):
    t=row(c,'tasks','task_id',e['task_id']);a=row(c,'attempts','attempt_id',e['attempt_id']);guarded(c,t,a,e)
    if digest(path)!=e['source_sha256']:raise Failure('SOURCE_CHANGED_DURING_ACCEPTANCE')
    if not blob.is_file() or digest(blob)!=h:raise Failure('PUBLISHED_BLOB_CHANGED')
    validate(e['kind'],data,c,{'paper_report_id':t['paper_report_id'],'source_sha256':e['source_sha256']})
    # Human-required decisions cannot be invented by workers. Trusted fixture backend is test-only.
    if t['stage'] in ('VERIFY','RESOLVE_OBJECT','TAXONOMY','CODE_TAXONOMY','SYNTHESIS'):
     approvals=c.execute("SELECT * FROM reviews WHERE artifact_sha256=? AND trusted=1 AND current=1 AND decision='APPROVE'",(h,)).fetchall()
     if not approvals:raise Failure('HUMAN_APPROVAL_REQUIRED')
     for review in approvals:
      rp=json.loads(review['payload_json'])
      attestation=c.execute("SELECT payload_json FROM events WHERE event_type='SYNTHETIC_REVIEW' AND subject=?",(review['review_id'],)).fetchone()
      if not attestation or json.loads(attestation[0]).get('content_sha256')!=sha(canonical(rp).encode()):raise Failure('REVIEW_CONTENT_CHANGED')
      if rp.get('trust_origin')!='SYNTHETIC_ONLY' or not pathlib.Path(db).resolve().is_relative_to(SHADOW/'synthetic'):raise Failure('REVIEW_TRUST')
      if rp.get('source_sha256')!=e['source_sha256'] or rp.get('pins')!=json.loads(t['pins_json']):raise Failure('REVIEW_INPUT_CHANGED')
    aid=uid('artifact');receipt={'artifact_id':aid,'sha256':h,'task_id':t['task_id'],'accepted_at':stamp()}
    c.execute('INSERT INTO artifacts VALUES(?,?,?,?,?,?,?,?,?)',(aid,h,'ACCEPTED_IMMUTABLE_ARTIFACT',e['kind'],t['paper_report_id'],str(blob),str(output),privacy,canonical({'attempt_id':a['attempt_id'],'source_sha256':e['source_sha256'],'pins':json.loads(t['pins_json'])})))
    c.execute('INSERT INTO replay VALUES(?,?,?,?,?,?)',(*key,request_hash,canonical(receipt)))
    c.execute("UPDATE attempts SET state='ACCEPTED' WHERE attempt_id=?",(a['attempt_id'],));c.execute("UPDATE tasks SET state='ACCEPTED' WHERE task_id=?",(t['task_id'],))
    for rec in ([p] if 'record_id' in p else [])+p.get('items',[]) if e['kind'] in ('evidence','verification') else ([p] if 'record_id' in p else []):
     rid=rec['record_id'];existing=c.execute('SELECT * FROM records WHERE record_id=?',(rid,)).fetchone()
     if existing:raise Failure('RECORD_ID_COLLISION',rid)
     c.execute('INSERT INTO records VALUES(?,?,?,?,?,1)',(rid,'claim' if e['kind']=='evidence' else e['kind'],t['paper_report_id'],h,canonical(rec)))
    c.execute('INSERT INTO accepted VALUES(?,?,1)',(t['task_id'],aid));event(c,'ACCEPTED',t['task_id'],receipt);failpoint('during_transaction')
   failpoint('after_commit');publish_views(c,db,failpoint);return receipt
  except Exception as ex:
   # A committed acceptance is never downgraded because a disposable view failed.
   if t:
    with transaction(c):
     event(c,'RESULT_ERROR',t['task_id'],{'code':getattr(ex,'code',type(ex).__name__),'sha256':h})
     if data is not None:
      private=not pathlib.Path(row(c,'reports','paper_report_id',t['paper_report_id'])['source_path']).resolve().is_relative_to(SHADOW/'synthetic')
      rejected=(SHADOW/'private_source_material' if private else SHADOW/'synthetic')/'rejected'/sha(str(pathlib.Path(db).resolve()).encode())[:24]
      try:
       b,rh=publish(rejected,data);aid=uid('rejected');c.execute('INSERT INTO artifacts VALUES(?,?,?,?,?,?,?,?,?)',(aid,rh,'REJECTED_PRESERVED_ARTIFACT',e['kind'],t['paper_report_id'],str(b),e['output_path'],'NEVER_PACKAGE' if private else 'SYNTHETIC',canonical({'error':getattr(ex,'code',type(ex).__name__)})));c.execute('INSERT OR IGNORE INTO retention VALUES(?,?)',(rh,'REJECTED_PRESERVED'))
      except Failure:event(c,'REJECTION_PRESERVATION_FAILED',t['task_id'],{'sha256':h})
   raise
def publish_views(c,db,failpoint=lambda _:None):
 failpoint('before_view');rows=[dict(r) for r in c.execute('SELECT task_id,artifact_id,valid FROM accepted ORDER BY task_id')];failpoint('during_view');write_json(guard(pathlib.Path(db).with_suffix('.view.json')),rows)
def recover(db):
 with coordinator(),connect(db) as c:
  checks=integrity(c);store=reconcile(c,[SHADOW/'synthetic/stores',SHADOW/'synthetic/rejected',SHADOW/'private_source_material/stores',SHADOW/'private_source_material/rejected',SHADOW/'private_source_material/raw'])
  if not store['passed']:raise Failure('STORE_INTEGRITY',canonical(store))
  publish_views(c,db);return {'database':checks,'store':store}
def approve_fixture(db,artifact_sha256,source_sha256,pins,actor='synthetic_reviewer'):
 guard(db,SHADOW/'synthetic')
 with coordinator(),connect(db) as c,transaction(c):
  if any(not pathlib.Path(r[0]).resolve().is_relative_to(SHADOW/'synthetic') for r in c.execute('SELECT source_path FROM reports')):raise Failure('NON_SYNTHETIC_REVIEW_INPUT')
  rid=uid('review');payload={'actor':actor,'timestamp':stamp(),'artifact_sha256':artifact_sha256,'source_sha256':source_sha256,'pins':pins,'decision':'APPROVE','rationale':'Synthetic protocol fixture; no real scientific approval','trust_origin':'SYNTHETIC_ONLY'}
  c.execute('INSERT INTO reviews VALUES(?,?,?,?,?,1,1)',(rid,artifact_sha256,actor,'APPROVE',canonical(payload)))
  event(c,'SYNTHETIC_REVIEW',rid,{'content_sha256':sha(canonical(payload).encode())});return rid
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('command',choices=['init','run','enqueue','claim','heartbeat','accept','reap','recover','integrity','update-pins']);ap.add_argument('--db',required=True);ap.add_argument('--input');a=ap.parse_args();p=json.loads(pathlib.Path(a.input).read_text()) if a.input else {}
 if a.command=='init':
  with coordinator(),connect(a.db,create=True) as c:result=integrity(c)
 elif a.command=='run':result=make_run(a.db,p)
 elif a.command=='enqueue':result=enqueue(a.db,**p)
 elif a.command=='claim':result=claim(a.db,**p)
 elif a.command=='heartbeat':result=heartbeat(a.db,**p)
 elif a.command=='accept':result=accept(a.db,pathlib.Path(a.input).read_bytes())
 elif a.command=='update-pins':result=update_pins(a.db,**p)
 elif a.command=='reap':result=reap(a.db)
 else:result=recover(a.db)
 print(canonical(result))
if __name__=='__main__':main()
