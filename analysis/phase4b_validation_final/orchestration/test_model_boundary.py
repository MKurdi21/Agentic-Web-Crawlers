"""Synthetic model ACK boundary tests; never opens scientific source bytes."""
import sys,json,tempfile,unittest
from pathlib import Path
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
import model_transport as m
class BoundaryTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]/'private_worker_material');self.p=Path(self.t.name)
  self.wrapper=self.p/'wrapper.json';self.wrapper.write_text('{}')
  self.policy=self.p/'policy.json';self.policy.write_text('{}')
  self.auth=self.p/'auth.json';self.review=self.p/'review.json';self.ack=self.p/'ack.json'
  self.entry={'report_id':'synthetic','source_sha256':'a'*64}
  self.cfg={'authorization_path':str(self.auth),'review_path':str(self.review),'packet_sha256':'b'*64,'entry':self.entry}
  self.a={'status':'ACKNOWLEDGED','context_id':'synthetic-context','fork_history':'none','previous_scientific_content_included':False,'source_accessed':False,'source_sha256':'a'*64,'report_id':'synthetic','packet_sha256':'b'*64,'wrapper_sha256':m.filehash(self.wrapper),'routing_policy_sha256':m.filehash(self.policy)}
  self.auth.write_text(json.dumps({'model_boundary':{'wrapper_sha256':m.filehash(self.wrapper),'routing_policy_path':str(self.policy),'routing_policy_sha256':m.filehash(self.policy),'adapter_sha256':m.filehash(m.__file__),'primary_context_id':'synthetic-context'}}))
  self.review.write_text(json.dumps({'actual_model_wrapper_sha256':m.filehash(self.wrapper),'actual_model_wrapper_status':'SEMANTIC_CONTEXT_CLEAN'}))
  class Synthetic(m.ModelTransport):
   def check(this):return self.cfg,b''
   @property
   def entry(this):return self.entry
  self.obj=Synthetic(self.p,self.ack,self.wrapper)
 def tearDown(self):self.t.cleanup()
 def check(self,mut=None):
  a=dict(self.a)
  if mut:a.update(mut)
  self.ack.write_text(json.dumps(a));return self.obj.model_boundary()
 def test_valid(self):self.assertEqual(self.check()['context_id'],'synthetic-context')
 def test_wrong_source(self):
  with self.assertRaises(m.Blocked):self.check({'source_sha256':'c'*64})
 def test_inherited_history(self):
  with self.assertRaises(m.Blocked):self.check({'fork_history':'all'})
 def test_previous_science(self):
  with self.assertRaises(m.Blocked):self.check({'previous_scientific_content_included':True})
 def test_access_before_ack(self):
  with self.assertRaises(m.Blocked):self.check({'source_accessed':True})
 def test_wrong_context(self):
  with self.assertRaises(m.Blocked):self.check({'context_id':'wrong'})
 def test_wrapper_mutated(self):
  self.wrapper.write_text('{"changed":true}')
  with self.assertRaises(m.Blocked):self.check()
 def test_policy_mutated(self):
  self.policy.write_text('{"changed":true}')
  with self.assertRaises(m.Blocked):self.check()
if __name__=='__main__':unittest.main()
