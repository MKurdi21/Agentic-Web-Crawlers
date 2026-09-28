from test_hardening import Hardening
from litrevctl_v2 import *
from validate_semantics import *
class Scientific(Hardening):
 # Inherited operational tests deliberately not rediscovered here: methods are assigned below.
 def pipeline(self):
  normal,p=self.task();accept(self.db,self.envelope(p))
  claimobj={'record_id':'evidence_A','paper_report_id':'report_A','claim_type':'OBSERVABLE_EVIDENCE','statement':'Synthetic benchmark measured one unit','locator':{'type':'PAGE','source_sha256':self.h,'page':1},'confidence':'HIGH'}
  summary,p=self.task('SUMMARIZE',[normal]);payload={'schema_version':'2.0.0','paper_report_id':'report_A','source_sha256':self.h,'narrative':'Synthetic narrative','claims':[claimobj],'coverage':{'reviewed_object_ids':[],'unreviewed_object_ids':['section_1'],'limitations':['Unreviewed synthetic fixture']}};e=self.envelope(p,payload);e['kind']='summary';accept(self.db,e)
  evidence,p=self.task('EXTRACT',[summary]);payload={'schema_version':'2.0.0','paper_report_id':'report_A','source_sha256':self.h,'items':[claimobj],'entities':[]};e=self.envelope(p,payload);e['kind']='evidence';receipt=accept(self.db,e)
  verification,p=self.task('VERIFY',[evidence]);payload={'schema_version':'2.0.0','paper_report_id':'report_A','source_sha256':self.h,'items':[{'record_id':'verification_A','evidence_id':'evidence_A','evidence_sha256':receipt['sha256'],'status':'SUPPORTED','rationale':'Synthetic known fixture','locator':claimobj['locator']}],'protocol_sha256':self.pins['verification']['sha256']};e=self.envelope(p,payload);e['kind']='verification'
  return verification,p,e
 def test_verification_missing_then_trusted_fixture(self):
  tid,p,e=self.pipeline();self.assertCode('HUMAN_APPROVAL_REQUIRED',lambda:accept(self.db,e));approve_fixture(self.db,e['output_sha256'],self.h,p['pins']);accept(self.db,e)
  with connect(self.db) as c:self.assertEqual(c.execute('SELECT count(*) FROM records WHERE kind=\'verification\'').fetchone()[0],1)
 def test_review_altered_and_superseded(self):
  tid,p,e=self.pipeline();rid=approve_fixture(self.db,e['output_sha256'],self.h,p['pins'])
  with connect(self.db) as c:c.execute("UPDATE reviews SET payload_json='{}' WHERE review_id=?",(rid,))
  self.assertCode('REVIEW_CONTENT_CHANGED',lambda:accept(self.db,e))
  with connect(self.db) as c:c.execute('UPDATE reviews SET current=0 WHERE review_id=?',(rid,))
  self.assertCode('HUMAN_APPROVAL_REQUIRED',lambda:accept(self.db,e))
 def test_review_wrong_hash(self):
  tid,p,e=self.pipeline();approve_fixture(self.db,'0'*64,self.h,p['pins']);self.assertCode('HUMAN_APPROVAL_REQUIRED',lambda:accept(self.db,e))
 def test_review_wrong_source(self):
  tid,p,e=self.pipeline();approve_fixture(self.db,e['output_sha256'],'0'*64,p['pins']);self.assertCode('REVIEW_INPUT_CHANGED',lambda:accept(self.db,e))
 def test_verification_nonexistent_evidence(self):
  tid,p,e=self.pipeline();payload=json.loads(pathlib.Path(e['output_path']).read_text());payload['items'][0]['evidence_id']='missing';e=self.envelope(p,payload);e['kind']='verification';self.assertCode('REFERENCE_NOT_CURRENT',lambda:accept(self.db,e))
 def test_taxonomy_unknown_term_and_version(self):
  with connect(self.db) as c:
   tax={'record_id':'tax1','schema_version':'2.0.0','version':'2.0.0','terms':[{'term_id':'T1','definition':'Definition','inclusion':'Included','exclusion':'Excluded'}]};c.execute('INSERT INTO records VALUES(?,?,?,?,?,1)',('tax1','taxonomy','report_A','a'*64,canonical(tax)))
   p={'schema_version':'2.0.0','paper_report_id':'report_A','source_sha256':self.h,'taxonomy_id':'tax1','taxonomy_version':'2.0.0','codes':[{'term_id':'MISSING','evidence_ids':['E1'],'rationale':'test'}]}
   self.assertCode('TAXONOMY_TERM',lambda:validate('paper_taxonomy_coding',p,c));p['taxonomy_version']='3.0.0';self.assertCode('TAXONOMY_VERSION',lambda:validate('paper_taxonomy_coding',p,c))
 def test_synthesis_requires_verified_inputs_and_resolved_objects(self):
  with connect(self.db) as c:
   c.execute('INSERT INTO records VALUES(?,?,?,?,?,1)',('E1','claim','report_A','a'*64,'{}'))
   obj={'state':'UNRESOLVED','members':['report_A']};c.execute('INSERT INTO records VALUES(?,?,?,?,?,1)',('O1','research_object','report_A','b'*64,canonical(obj)))
   p={'schema_version':'2.0.0','record_id':'S1','input_ids':['E1'],'input_fingerprint':sha(canonical([('E1','a'*64)]).encode()),'report_ids':['report_A'],'research_object_ids':['O1'],'report_count':1,'object_count':1,'coverage':'COMPLETE_ELIGIBLE_SCOPE','exclusions':[],'matrix':[{'row_id':'M1','evidence_ids':['E1'],'finding':'Synthetic'}]}
   self.assertCode('SYNTHESIS_UNVERIFIED',lambda:validate('synthesis',p,c));c.execute('INSERT INTO reviews VALUES(?,?,?,?,?,1,1)',('R1','a'*64,'fixture','APPROVE','{}'));self.assertCode('SYNTHESIS_UNVERIFIED',lambda:validate('synthesis',p,c))
   from unittest.mock import patch
   c.execute('INSERT INTO records VALUES(?,?,?,?,?,1)',('V1','verification','report_A','c'*64,canonical({'evidence_id':'E1','evidence_sha256':'a'*64,'status':'SUPPORTED'})))
   with patch('validate_semantics.trusted_receipt',return_value=True):self.assertCode('UNRESOLVED_OBJECT',lambda:validate('synthesis',p,c))
   p['report_count']=2;self.assertCode('DENOMINATOR',lambda:validate('synthesis',p,c))
 def test_invalidation_propagates_to_downstream(self):
  tid,p,e=self.pipeline();update_pins(self.db,self.run,{'prompt':{'version':'2.1.0','sha256':sha(b'newprompt')}})
  with connect(self.db) as c:
   self.assertEqual(row(c,'tasks','task_id',tid)['state'],'INVALIDATED');self.assertEqual(c.execute("SELECT state FROM tasks WHERE stage='NORMALIZE'").fetchone()[0],'ACCEPTED')
 def test_append_only_event_history(self):
  with connect(self.db) as c:
   with self.assertRaises(Exception):c.execute('DELETE FROM events')

# Reuse setup/helpers without duplicating the inherited test suite.
for name in list(Hardening.__dict__):
 if name.startswith('test_') and name not in Scientific.__dict__:setattr(Scientific,name,None)
def load_tests(loader,tests,pattern):return loader.loadTestsFromTestCase(Scientific)
