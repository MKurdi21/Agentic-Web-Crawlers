import test_hardening as base
from litrevctl_v2 import *
from validate_semantics import *
class Additional(base.Hardening):
 def test_retry_limit(self):
  tid,p=self.task()
  for i in range(3):
   with connect(self.db) as c:c.execute('UPDATE attempts SET expiry=0 WHERE task_id=?',(tid,))
   reap(self.db)
   if i<2:claim(self.db,tid,'worker_retry')
  self.assertCode('NOT_CLAIMABLE',lambda:claim(self.db,tid,'worker_retry'))
 def test_authoritative_pins_not_only_packet(self):
  tid,p=self.task();e=self.envelope(p)
  with connect(self.db) as c:
   pins=json.loads(row(c,'runs','run_id',self.run)['pins_json']);pins['normalization']['sha256']='0'*64;c.execute('UPDATE runs SET pins_json=? WHERE run_id=?',(canonical(pins),self.run))
  self.assertCode('STALE_PINS',lambda:accept(self.db,e))
 def test_wrong_attempt_and_paper(self):
  tid,p=self.task();e=self.envelope(p);other,q=self.task();e['attempt_id']=q['attempt_id'];self.assertCode('ATTEMPT_TASK',lambda:accept(self.db,e));e['attempt_id']=p['attempt_id'];e['paper_report_id']='wrong';self.assertCode('ENVELOPE_PAPER_REPORT_ID',lambda:accept(self.db,e))
 def test_missing_source(self):
  tid,p=self.task();e=self.envelope(p);self.source.unlink();self.assertCode('SOURCE_CHANGED',lambda:accept(self.db,e))
 def test_replay_does_not_resurrect_invalidated(self):
  tid,p=self.task();e=self.envelope(p);original=accept(self.db,e);update_pins(self.db,self.run,{'normalization':{'version':'3.0.0','sha256':'a'*64}});self.assertEqual(accept(self.db,e),original)
  with connect(self.db) as c:self.assertEqual(c.execute('SELECT valid FROM accepted').fetchone()[0],0)
 def test_actual_sql_failure_rolls_back(self):
  tid,p=self.task();e=self.envelope(p)
  with connect(self.db) as c:c.execute("CREATE TRIGGER injected_failure BEFORE INSERT ON accepted BEGIN SELECT RAISE(ABORT,'injected SQL failure'); END")
  with self.assertRaises(Exception):accept(self.db,e)
  with connect(self.db) as c:self.assertEqual(c.execute('SELECT count(*) FROM accepted').fetchone()[0],0);self.assertEqual(c.execute('SELECT count(*) FROM replay').fetchone()[0],0)
 def test_foreign_key_integrity_is_separate(self):
  bad=self.root/'known_corrupt_fixture.sqlite3'
  with connect(bad,create=True) as c:
   c.execute('PRAGMA foreign_keys=OFF');c.execute('INSERT INTO observations VALUES(?,?,?)',('synthetic','missing',stamp()));c.execute('PRAGMA foreign_keys=ON')
   self.assertEqual([r[0] for r in c.execute('PRAGMA integrity_check')],['ok']);self.assertCode('DATABASE_INTEGRITY',lambda:integrity(c))
  # Deliberately retained bad synthetic fixture; no automatic repair.
 def test_schema_valid_invalid_range(self):
  p=self.payload();p['inventory'][0]['locator']={'type':'PAGE_RANGE','source_sha256':self.h,'start':5,'end':2};self.assertCode('RANGE',lambda:validate('normalized_paper',p))
 def test_page_outside_source(self):
  tid,p=self.task();obj=self.payload();obj['inventory'][0]['locator']['page']=21;self.assertCode('PAGE_BOUNDS',lambda:accept(self.db,self.envelope(p,obj)))
 def test_coordinator_excludes_second_writer(self):
  with coordinator():self.assertCode('COORDINATOR_BUSY',lambda:make_run(self.db,self.pins))
 def test_fixture_cannot_approve_real_inputs(self):
  with connect(self.db) as c:c.execute('UPDATE reports SET source_path=?',(str(WORKSPACE/'analysis/PROMPT.md'),))
  self.assertCode('NON_SYNTHETIC_REVIEW_INPUT',lambda:approve_fixture(self.db,self.h,self.h,{}))
 def test_unexpected_file_classification(self):
  root=self.root/'store';root.mkdir();(root/'surprise.txt').write_text('Synthetic')
  with connect(self.db) as c:self.assertEqual(reconcile(c,[root])['blobs'][0]['classification'],'UNEXPECTED_FILE')
for name in list(base.Hardening.__dict__):
 if name.startswith('test_') and name not in Additional.__dict__:setattr(Additional,name,None)
def load_tests(loader,tests,pattern):return loader.loadTestsFromTestCase(Additional)
