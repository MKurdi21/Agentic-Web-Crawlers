import sys,pathlib,unittest,copy,json,subprocess,os
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from common import *
from db import *
from litrevctl_v2 import *
from artifact_store import *
from validate_semantics import *
from backup_shadow import backup

class Hardening(unittest.TestCase):
 def setUp(self):
  self.root=SHADOW/'synthetic'/uid('test');self.root.mkdir(parents=True);self.db=self.root/'state.sqlite3';self.source=self.root/'source.txt';self.source.write_bytes(b'Synthetic source A');self.h=digest(self.source)
  with connect(self.db,create=True) as c,transaction(c):
   c.execute('INSERT INTO sources VALUES(?,?,?)',('source_A',self.h,20));c.execute('INSERT INTO observations VALUES(?,?,?)',(str(self.source),'source_A',stamp()));c.execute('INSERT INTO reports VALUES(?,?,?,?,?,?,?)',('report_A','synthetic.md','source_A',str(self.source),'pending','RAW_IMPORTED_ARTIFACT','{}'))
  keys=set(k for v in PINKEYS.values() for k in v)|{'code','runtime','worker_protocol'}
  self.pins={k:{'version':'2.0.0','sha256':sha(k.encode())} for k in keys};self.run=make_run(self.db,self.pins)
 def tearDown(self):
  with connect(self.db,readonly=True) as c:integrity(c)
 def task(self,stage='NORMALIZE',pre=None):
  tid=enqueue(self.db,self.run,'report_A',stage,pre);p=claim(self.db,tid,'worker_A');return tid,p
 def payload(self):
  return {'paper_report_id':'report_A','source_sha256':self.h,'schema_version':'2.0.0','text_sha256':sha(b'normalized'),'inventory':[{'object_id':'section_1','object_type':'SECTION','locator':{'type':'PAGE','source_sha256':self.h,'page':1}}]}
 def envelope(self,p,data=None):
  payload=self.payload() if data is None else data;b=canonical(payload).encode();path=pathlib.Path(p['outbox'])/'result.json';path.write_bytes(b)
  return {k:p[k] for k in ('task_id','attempt_id','attempt_number','run_id','worker','token','generation','paper_report_id','source_sha256')}|{'submission_id':uid('submission'),'kind':'normalized_paper','output_path':str(path),'output_sha256':sha(b)}
 def assertCode(self,code,fn):
  with self.assertRaises(Failure) as cm:fn()
  self.assertEqual(cm.exception.code,code)
 def test_configuration_and_foreign_keys(self):
  with connect(self.db) as c:
   self.assertEqual(observed(c),PROFILE)
   with self.assertRaises(Exception):c.execute('INSERT INTO observations VALUES(?,?,?)',('bad','missing',stamp()))
   c.execute('PRAGMA foreign_keys=OFF');self.assertCode('SQLITE_CONFIGURATION',lambda:verify_profile(c))
 def test_schema_identity_fail_closed(self):
  with connect(self.db) as c:c.execute('PRAGMA user_version=9')
  self.assertCode('SQLITE_CONFIGURATION',lambda:self.open_db())
  # Restore only synthetic test header using the same bootstrap through a diagnostic fixture.
  from unittest.mock import patch
  with patch('db.PROFILE',{**PROFILE,'user_version':9}):
   with connect(self.db) as c:c.execute('PRAGMA user_version=2')
 def open_db(self):
  with connect(self.db):pass
 def test_boundary(self):
  self.assertCode('BOUNDARY',lambda:guard(WORKSPACE/'analysis/checkpoint.json'))
 def test_alias_collision(self):
  with connect(self.db) as c:
   with self.assertRaises(Exception):c.execute('INSERT INTO reports VALUES(?,?,?,?,?,?,?)',('other','SYNTHETIC.MD','source_A',str(self.source),'pending','RAW_IMPORTED_ARTIFACT','{}'))
 def test_valid_acceptance_and_replay(self):
  tid,p=self.task();e=self.envelope(p);r=accept(self.db,e);r2=accept(self.db,e);self.assertEqual(r,r2)
  with connect(self.db) as c:self.assertEqual(c.execute('SELECT count(*) FROM accepted').fetchone()[0],1);self.assertEqual(c.execute('SELECT count(*) FROM replay').fetchone()[0],1)
 def test_conflicting_replay(self):
  tid,p=self.task();e=self.envelope(p);accept(self.db,e);changed=copy.deepcopy(e);changed['worker']='other';self.assertCode('REPLAY_CONFLICT',lambda:accept(self.db,changed))
 def test_expired_and_reaped_result(self):
  tid,p=self.task();e=self.envelope(p)
  with connect(self.db) as c:c.execute('UPDATE attempts SET expiry=0')
  self.assertCode('STALE_ATTEMPT',lambda:accept(self.db,e));self.assertEqual(len(reap(self.db)),1);claim(self.db,tid,'worker_B');self.assertCode('STALE_ATTEMPT',lambda:accept(self.db,e))
 def test_wrong_worker_token_generation(self):
  for field in ('worker','token','generation','attempt_number'):
   tid,p=self.task();e=self.envelope(p);e[field]=99 if field in ('generation','attempt_number') else 'wrong';self.assertCode('ENVELOPE_'+field.upper(),lambda:accept(self.db,e))
 def test_source_mutation_after_dispatch(self):
  tid,p=self.task();e=self.envelope(p);self.source.write_bytes(b'Synthetic source B');self.assertCode('SOURCE_CHANGED',lambda:accept(self.db,e))
  with connect(self.db) as c:
   self.assertEqual(row(c,'tasks','task_id',tid)['state'],'INVALIDATED');self.assertEqual(c.execute('SELECT count(*) FROM sources').fetchone()[0],2);self.assertEqual(c.execute('SELECT count(*) FROM accepted').fetchone()[0],0)
 def test_current_pins_and_selective_taxonomy(self):
  tid,p=self.task();e=self.envelope(p);update_pins(self.db,self.run,{'taxonomy':{'version':'2.1.0','sha256':sha(b'newtax')}});accept(self.db,e)
  tid,p=self.task();e=self.envelope(p);update_pins(self.db,self.run,{'normalization':{'version':'2.1.0','sha256':sha(b'newnormal')}});self.assertCode('STALE_ATTEMPT',lambda:accept(self.db,e))
 def test_prerequisite_gate(self):self.assertCode('PREREQUISITES_REQUIRED',lambda:enqueue(self.db,self.run,'report_A','VERIFY',[]))
 def test_output_hash_and_scope(self):
  tid,p=self.task();e=self.envelope(p);e['output_sha256']='0'*64;self.assertCode('SUBMISSION_HASH',lambda:accept(self.db,e));e['output_path']=str(self.source);self.assertCode('BOUNDARY',lambda:accept(self.db,e))
 def test_blob_reuse_and_corruption(self):
  root=self.root/'store';p,h=publish(root,b'synthetic');self.assertEqual(publish(root,b'synthetic')[0],p);p.write_bytes(b'corruption');self.assertCode('BLOB_INTEGRITY',lambda:publish(root,b'synthetic'))
 def test_database_missing_blob_distinct_from_integrity(self):
  tid,p=self.task();e=self.envelope(p);r=accept(self.db,e)
  with connect(self.db) as c:
   path=pathlib.Path(c.execute('SELECT path FROM artifacts WHERE artifact_id=?',(r['artifact_id'],)).fetchone()[0]);path.unlink();self.assertEqual(integrity(c)['integrity_check'],['ok']);self.assertFalse(reconcile(c,[])['passed'])
 def test_orphan_collection_protects_retention(self):
  root=self.root/'store';p,h=publish(root,b'orphan')
  with coordinator(),connect(self.db) as c:
   c.execute('INSERT INTO retention VALUES(?,?)',(h,'event'));self.assertEqual(collect(c,[root],True,0)['candidates'],[]);self.assertTrue(p.exists())
 def test_crash_injection_each_phase(self):
  phases=['before_stage','during_stage','after_stage','after_publish','before_transaction','during_transaction','after_commit','before_view','during_view']
  for phase in phases:
   tid,p=self.task();e=self.envelope(p,{**self.payload(),'text_sha256':sha(phase.encode())})
   def crash(current):
    if current==phase:raise RuntimeError('INJECTED:'+phase)
   with self.assertRaises(RuntimeError):accept(self.db,e,crash)
   with connect(self.db) as c:
    integrity(c);n=c.execute('SELECT count(*) FROM accepted WHERE task_id=?',(tid,)).fetchone()[0];self.assertEqual(n,1 if phase in ('after_commit','before_view','during_view') else 0)
   recover(self.db)
 def test_actual_process_crash_after_publish(self):
  tid,p=self.task();e=self.envelope(p);packet=self.root/'envelope.json';packet.write_text(canonical(e))
  code="import sys,os,json;sys.path.insert(0,sys.argv[1]);from litrevctl_v2 import accept;accept(sys.argv[2],json.load(open(sys.argv[3])),lambda p:os._exit(73) if p=='after_publish' else None)"
  proc=subprocess.run([sys.executable,'-B','-c',code,str(DESIGN/'hardened/scripts'),str(self.db),str(packet)],capture_output=True)
  self.assertEqual(proc.returncode,73);result=recover(self.db);self.assertTrue(result['store']['passed'])
  with connect(self.db) as c:self.assertEqual(c.execute('SELECT count(*) FROM accepted').fetchone()[0],0)
 def test_backup_restore(self):
  tid,p=self.task();accept(self.db,self.envelope(p));result=backup(self.db,self.root/'backup.sqlite3');self.assertTrue(result['passed'])
 def test_untrusted_review_is_not_approval(self):
  self.assertCode('BOUNDARY',lambda:approve_fixture(SHADOW/'current.sqlite3',self.h,self.h,{}))

class Semantics(unittest.TestCase):
 def test_parse_duplicate_and_invalid(self):
  for data in [b'{"a":1,"a":2}',b'\xff',b'{',b'NaN']:
   with self.assertRaises(ValidationError):parse(data)
 def test_all_schema_documents(self):
  for p in (DESIGN/'hardened/schemas').glob('*.json'):Draft202012Validator.check_schema(json.loads(p.read_text()))
 def test_formats(self):
  for name,good,bad in [('timestamp','2026-09-13T12:00:00Z','yesterday'),('sha256','a'*64,'xyz'),('identifier','report_A','bad id'),('semver','2.0.0','two'),('doi','10.1234/example','no'),('http-uri','https://example.org/item','javascript:evil')]:self.assertTrue(fmt(name,good));self.assertFalse(fmt(name,bad))
 def test_locator_variants(self):
  from build_schemas import LOCATORS
  samples={'PAGE':{'page':1},'PAGE_RANGE':{'start':1,'end':2},'SECTION':{'heading':'Methods'},'FIGURE':{'identifier_or_caption':'Fig1'},'TABLE':{'identifier':'T1'},'EQUATION':{'identifier_or_anchor':'Eq1'},'APPENDIX':{'heading':'A'},'TEXT_SPAN':{'text_sha256':'a'*64,'start':0,'end':5,'offset_convention':'UNICODE_CODEPOINT'},'ARTIFACT_URL':{'url':'https://example.org/item'},'REPOSITORY_FILE':{'repository':'repo','revision':'abc','path':'src/file.py'},'UNKNOWN':{'reason':'Unavailable supplement','missing_context':'Missing author attachment'}}
  for t,fields in samples.items():
   loc={'type':t,'source_sha256':'a'*64,**fields};p={'schema_version':'2.0.0','paper_report_id':'P1','source_sha256':'a'*64,'text_sha256':'b'*64,'inventory':[{'object_id':'O1','object_type':'SECTION','locator':loc}]};validate('normalized_paper',p)
   p['inventory'][0]['locator']={'type':t,'source_sha256':'a'*64}
   with self.assertRaises(ValidationError):validate('normalized_paper',p)
 def test_empty_and_unrelated_evidence(self):
  p={'schema_version':'2.0.0','paper_report_id':'P1','source_sha256':'a'*64,'items':[],'entities':[]}
  with self.assertRaises(ValidationError):validate('evidence',p)
  p['items']=[{'record_id':'E1','paper_report_id':'P2','claim_type':'AUTHOR_CLAIM','statement':'Something','locator':{'type':'PAGE','source_sha256':'a'*64,'page':1},'confidence':'LOW'}]
  with self.assertRaises(ValidationError):validate('evidence',p)
if __name__=='__main__':unittest.main()
