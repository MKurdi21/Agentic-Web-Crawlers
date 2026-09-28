"""Real consumed-development PDF integration and failure boundaries."""
from bridge import *
import unittest,tempfile,copy
PRIVATE=O/'private_development_source_material';PRIVATE.mkdir(exist_ok=True)
AUTH=O/'DEVELOPMENT_AUTHORIZATION.json';REVIEW=O/'test_results/PACKET_SEMANTIC_REVIEW.json';ID=next(iter(read(AUTH)['reports']))
class RealTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(dir=PRIVATE);self.run=Path(self.tmp.name)/'run';self.a=RealContinuity(self.run).create(AUTH,ID,REVIEW);self.addCleanup(self.cleanup)
 def cleanup(self):self.a.close_worker();self.tmp.cleanup()
 def ready(self):self.a.prepare();self.a.preaccess()
 def count(self):return len([x for x in self.a.e.journal() if x['event_type']=='SOURCE_ACCESS_BEGAN'])
 def test_01_before_ack(self):
  with self.assertRaises(Exception):self.a.unit('EXTRACTION')
  self.assertEqual(self.count(),0);self.assertFalse(self.a.e.state()['source_access_started'])
 def test_02_after_ack(self):
  self.a.prepare()
  with self.assertRaises(Exception):self.a.unit('EXTRACTION')
  self.assertEqual(self.count(),0)
 def test_03_after_preaccess(self):
  self.ready();self.assertEqual(self.count(),0);self.assertFalse((self.run/'real_helper/SOURCE_ACCESS_BEGAN.json').exists())
 def test_04_consumption_before_delivery(self):
  self.ready()
  with self.assertRaises(Crash):self.a.unit('EXTRACTION',crash='after_consumption')
  self.a.close_worker();s=RealContinuity(self.run).recover('new');self.assertTrue(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'CONSUMED_VALIDATION_EVIDENCE')
  self.assertFalse((self.run/'real_helper/SOURCE_ACCESS_BEGAN.json').exists())
 def test_05_during_delivery(self):
  self.ready();self.a.unit('EXTRACTION',crash='during_delivery');a=RealContinuity(self.run);a.recover('fresh');self.a=a
  self.assertTrue(a.e.state()['source_access_started']);self.assertEqual(a.unit('EXTRACTION')['namespace'],'DEVELOPMENT_TRANSPORT_ONLY')
 def test_06_after_delivery_before_commit(self):
  self.ready();self.a.unit('EXTRACTION',crash='before_unit_commit');self.a=RealContinuity(self.run);self.a.recover('fresh');self.a.unit('EXTRACTION');self.assertEqual(self.count(),1)
 def test_07_after_unit_commit(self):
  self.ready();first=self.a.unit('EXTRACTION');n=len(self.a.e.receipts());self.a.recover('fresh');self.assertEqual(self.a.unit('EXTRACTION'),first);self.assertEqual(len(self.a.e.receipts()),n)
 def test_08_full_real_source(self):
  self.ready();out=self.a.unit('EXTRACTION');self.assertTrue(out['value']);self.assertEqual(out['locator']['pdf_page'],1);self.assertFalse(out['scientific_acceptance']);self.assertEqual(self.count(),1)
 def test_09_fresh_session_second_unit(self):
  self.ready();first=self.a.unit('EXTRACTION');self.a.unit('VERIFICATION','VERIFY','during_unit');self.a=RealContinuity(self.run);self.a.recover('entirely-new');second=self.a.unit('VERIFICATION','VERIFY');self.assertEqual(first['value'],second['value']);self.assertEqual(first['locator'],second['locator']);self.assertEqual(self.count(),1)
 def test_10_duplicate_recovery(self):
  self.ready();self.a.unit('EXTRACTION');self.a.recover('new1');self.a.recover('new2');self.assertEqual(self.count(),1);ids=[r['atomic_unit_id'] for _,r in self.a.e.receipts()];self.assertEqual(len(ids),len(set(ids)))
 def test_11_duplicate_ack(self):
  a=self.a.prepare();self.assertEqual(a,self.a.prepare());self.assertEqual(len(self.a.e.receipts()),1)
 def test_12_duplicate_preaccess(self):
  self.ready();p=self.a.preaccess();self.assertEqual(p,self.a.preaccess());self.assertEqual(self.count(),0)
 def mutate_config(self,key,value):
  p=self.run/'configuration.json';obj=read(p);obj['entry'][key]=value;p.write_bytes(canonical(obj))
 def test_13_correct_report_wrong_source(self):
  self.mutate_config('source_path',str(self.run/'wrong.pdf'))
  with self.assertRaises(Blocked):self.a.check()
 def test_14_correct_source_wrong_hash(self):
  self.mutate_config('source_sha256','0'*64)
  with self.assertRaises(Blocked):self.a.check()
 def test_15_correct_hash_wrong_report(self):
  self.mutate_config('report_id','unrelated_report')
  with self.assertRaises(Blocked):self.a.check()
 def test_16_wrong_source_file_id(self):
  self.mutate_config('source_file_id','sha256:'+'0'*64)
  with self.assertRaises(Blocked):self.a.check()
 def test_17_wrong_packet_binding(self):
  p=self.run/'packet.json';body=c.load(p);body['binding']['paper_id']='wrong';p.write_bytes(canonical(body))
  with self.assertRaises(Blocked):self.a.check()
 def test_18_stale_packet(self):
  (self.run/'packet.json').write_bytes(b'{}')
  with self.assertRaises(Blocked):self.a.check()
 def test_19_stale_receipt(self):
  self.ready();p=self.a.e.root/'outputs/pre_access.json';v=read(p);v['packet_sha256']='0'*64;p.write_bytes(canonical(v))
  with self.assertRaises(Blocked):self.a.recover('new')
 def test_20_missing_ack(self):
  self.ready();(self.a.e.root/'outputs/packet_ack.json').unlink()
  with self.assertRaises(Exception):self.a.recover('new')
 def test_21_event_before_projection(self):
  self.ready()
  with self.assertRaises(Crash):self.a.unit('EXTRACTION',crash='event_before_state')
  self.a.close_worker();self.a=RealContinuity(self.run);s=self.a.recover('new');self.assertTrue(s['source_access_started']);self.a.unit('EXTRACTION');self.assertEqual(self.count(),1)
 def test_22_consumption_cannot_revert(self):
  self.ready();self.a.unit('EXTRACTION')
  with self.a.e.lock('simulate_stale_projection'):
   s=self.a.e.state();s['source_access_started']=False;s['active_holdout_state']='UNTOUCHED_RESERVED_VALIDATION_EVIDENCE';self.a.e.save(s)
  s=self.a.recover('new');self.assertTrue(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'CONSUMED_VALIDATION_EVIDENCE')
 def test_23_committed_output_mutation(self):
  self.ready();self.a.unit('EXTRACTION');(self.a.e.root/'outputs/extraction.json').write_bytes(b'{}')
  with self.assertRaises(Exception):self.a.recover('new')
 def test_24_firewall_history(self):
  data,_=packet(self.a.entry);body=c.loads(data);body['context'][0]['content']+=' previous holdout found a prior false accept'
  with self.assertRaises(Blocked):scan(canonical(body),self.a.entry)
 def test_25_identity_exception_not_broad(self):
  data,_=packet(self.a.entry);body=c.loads(data);body['context'][0]['content']+=' B01'
  with self.assertRaises(Blocked):scan(canonical(body),self.a.entry)
 def test_26_reserved_registry_rejected(self):
  with self.assertRaises(Blocked):RealContinuity(Path(self.tmp.name)/'reserved').create(AUTH,read(AUTH)['reserved_denied_report_ids'][0],REVIEW)
 def test_27_postsource_helper_tamper(self):
  self.ready();self.a.unit('EXTRACTION');(self.run/'real_helper/SOURCE_ACCESS_BEGAN.json').write_bytes(b'{}')
  with self.assertRaises(Exception):self.a.recover('new')
 def test_28_before_ack_recovery(self):
  s=self.a.recover('fresh');self.assertFalse(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'CONSUMED_VALIDATION_EVIDENCE')
 def test_29_ack_only_recovery(self):
  self.a.prepare();self.a.close_worker();s=self.a.recover('fresh');self.assertFalse(s['source_access_started']);self.a.preaccess();self.a.unit('EXTRACTION')
 def test_30_scientific_stage_binding(self):
  self.ready()
  with self.assertRaises(Blocked):self.a.unit('EXTRACTION','VERIFY')
 def test_31_code_drift(self):
  import unittest.mock
  with unittest.mock.patch('bridge.codehash',return_value='0'*64):
   with self.assertRaises(Blocked):self.a.check()
 def test_32_stale_semantic_review(self):
  data,_=packet(self.a.entry);review=read(REVIEW);review['packet_sha256']='0'*64
  with self.assertRaises(Blocked):review_valid(data,review,self.a.entry)
 def test_33_verifier_prerequisite(self):
  self.ready()
  with self.assertRaises(Blocked):self.a.unit('VERIFICATION','VERIFY')
  self.assertEqual(self.count(),0)
 def test_34_initial_wrong_ack_protocol(self):
  from unittest.mock import patch
  original=self.a._commit
  def altered(unit,obj):
   if unit=='PACKET_ACK':obj={**obj,'methodology_sha256':'0'*64}
   return original(unit,obj)
  with patch.object(self.a,'_commit',side_effect=altered):self.a.prepare()
  self.a.preaccess()
  with self.assertRaises(Blocked):self.a.unit('EXTRACTION')
  self.assertEqual(self.count(),0)
 def test_35_helper_wrong_identity_before_adoption(self):
  self.ready()
  with self.assertRaises(Crash):self.a.unit('EXTRACTION',crash='after_consumption')
  d=self.run/'real_helper';b=read(d/'PRE_ACCESS_RECEIPT.json')
  helper.open_source(d,self.a.entry['source_path'],b,allowed_reports={self.a.entry['development_id']})
  event=read(d/'SOURCE_ACCESS_BEGAN.json');event['holdout_id']='WRONG_REPORT';(d/'SOURCE_ACCESS_BEGAN.json').write_bytes(canonical(event))
  with self.assertRaises(Blocked):self.a.unit('EXTRACTION')
  self.assertFalse((self.a.e.root/'outputs/delivery_authority.json').exists())
 def test_36_runtime_dependency_hash(self):
  from unittest.mock import patch
  original=filehash
  def changed(p):
   if str(p).replace('\\','/').endswith('_deps/pypdfium2/__init__.py'):return '0'*64
   return original(p)
  with patch('bridge.filehash',side_effect=changed):
   with self.assertRaises(Blocked):runtime_integrity()
 def test_37_review_protocol_rejected(self):
  data,_=packet(self.a.entry);review=read(REVIEW);review['review_protocol_sha256']='0'*64
  with self.assertRaises(Blocked):review_valid(data,review,self.a.entry)
 def test_38_review_mode_rejected(self):
  data,_=packet(self.a.entry);review=read(REVIEW);review['review_mode']='SELF_ASSERTED'
  with self.assertRaises(Blocked):review_valid(data,review,self.a.entry)
 def test_39_fresh_coordinator_process(self):
  self.ready();self.a.unit('EXTRACTION');self.a.unit('VERIFICATION','VERIFY','during_unit')
  result=subprocess.run([sys.executable,'-B',str(O/'integration_layer/cli.py'),'verify',str(self.run)],capture_output=True,check=True,timeout=180)
  receipt=json.loads(result.stdout);self.assertNotEqual(receipt['pid'],os.getpid());self.assertTrue(receipt['consumed']);self.assertIn('VERIFICATION',receipt['committed_units']);self.assertEqual(self.count(),1)
 def test_40_added_importable_dependency(self):
  from runtime_guard import verify
  root=Path(self.tmp.name)/'invented_deps';root.mkdir();(root/'known.py').write_text('pass');manifest=[{'relative_path':'known.py','sha256':filehash(root/'known.py')}];verify(root,manifest)
  (root/'shadow.py').write_text('pass')
  with self.assertRaisesRegex(RuntimeError,'INVENTORY_DRIFT'):verify(root,manifest)

if __name__=='__main__':
 class Result(unittest.TextTestResult):
  def startTest(self,t):super().startTest(t);self.records=getattr(self,'records',[])
  def addSuccess(self,t):
   super().addSuccess(t);self.records.append({'id':t.id(),'status':'PASS'});(O/'test_results/REAL_TEST_PROGRESS.json').write_bytes(canonical({'status':'IN_PROGRESS','completed':self.records}))
  def addError(self,t,e):super().addError(t,e);self.records.append({'id':t.id(),'status':'ERROR','diagnostic':self._exc_info_to_string(e,t)})
  def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'id':t.id(),'status':'FAIL','diagnostic':self._exc_info_to_string(e,t)})
 r=unittest.TextTestRunner(verbosity=2,resultclass=Result).run(unittest.defaultTestLoader.loadTestsFromTestCase(RealTests))
 report={'tests':r.testsRun,'passed':r.testsRun-len(r.errors)-len(r.failures),'failed':len(r.errors)+len(r.failures),'skipped':len(r.skipped),'records':r.records,'integration_sha256':codehash(),'real_development_source':ID,'scientific_validation':False}
 exclusive(O/'test_results'/('real-'+uuid.uuid4().hex+'.json'),canonical(report))
 if r.wasSuccessful():(O/'REAL_SOURCE_CONTINUITY_TEST_RESULTS.json').write_bytes(canonical(report))
 raise SystemExit(not r.wasSuccessful())
