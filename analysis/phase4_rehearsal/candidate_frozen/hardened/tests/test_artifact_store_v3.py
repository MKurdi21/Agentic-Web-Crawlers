import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from common import *
from db import connect,transaction
from artifact_store import bind_store,publish,reconcile,STORE_METADATA

class ArtifactStoreV3(unittest.TestCase):
 def setUp(self):
  self.root=SHADOW/'synthetic'/uid('store_v3');self.root.mkdir(parents=True);self.db=self.root/'state.sqlite3'
  with connect(self.db,create=True):pass
 def store(self,name='store'):
  root=self.root/name
  with connect(self.db) as c:bind_store(c,root)
  return root
 def register(self,path,h):
  with connect(self.db) as c,transaction(c):
   c.execute('INSERT INTO artifacts VALUES(?,?,?,?,?,?,?,?,?)',(uid('artifact'),h,'ACCEPTED_IMMUTABLE_ARTIFACT','synthetic',None,str(path),str(path),'SYNTHETIC','{}'))
 def scan(self,root):
  with connect(self.db,readonly=True) as c:return reconcile(c,[root])
 def test_valid_complete_store(self):
  root=self.store();p,h=publish(root,b'valid');self.register(p,h);r=self.scan(root)
  self.assertTrue(r['gate_passed']);self.assertEqual(r['classification_counts']['VALID_REFERENCED_BLOB'],1);self.assertEqual(r['classification_counts']['EXPECTED_CONTROL_FILE'],1)
  self.assertTrue(r['store_id'].startswith('store_'));self.assertTrue(r['database_id'].startswith('db_'));self.assertEqual(r['scanned_root'],str(root.resolve()));self.assertEqual(len(r['scan_fingerprint']),64)
 def test_explicitly_allowed_control_file(self):
  root=self.store();r=self.scan(root)
  self.assertTrue(r['gate_passed']);self.assertEqual([(pathlib.Path(x['path']).name,x['classification']) for x in r['entries']],[(STORE_METADATA,'EXPECTED_CONTROL_FILE')])
 def test_arbitrary_unexpected_file_fails(self):
  root=self.store();(root/'surprise.txt').write_text('synthetic',encoding='utf-8');r=self.scan(root)
  self.assertFalse(r['gate_passed']);self.assertEqual(r['classification_counts']['UNEXPECTED_FILE'],1);self.assertIn('UNEXPECTED_FILE',{x['code'] for x in r['failure_reasons']})
 def test_abandoned_root_staging_file_fails(self):
  root=self.store();(root/'staging_0123456789abcdef.tmp').write_text('synthetic',encoding='utf-8');r=self.scan(root)
  self.assertFalse(r['gate_passed']);self.assertEqual(r['classification_counts']['UNEXPECTED_FILE'],1)
 def test_missing_accepted_blob_fails(self):
  root=self.store();p=root/'aa'/('a'*64);self.register(p,'a'*64);r=self.scan(root)
  self.assertFalse(r['gate_passed']);self.assertEqual(r['classification_counts']['MISSING_REFERENCED_BLOB'],1)
 def test_corrupted_accepted_blob_fails(self):
  root=self.store();p,h=publish(root,b'valid');self.register(p,h);p.write_bytes(b'corrupt');r=self.scan(root)
  self.assertFalse(r['gate_passed']);self.assertEqual(r['classification_counts']['HASH_MISMATCH'],1)
 def test_orphan_blob_is_visible_and_policy_controlled(self):
  root=self.store();publish(root,b'orphan');r=self.scan(root)
  self.assertTrue(r['gate_passed']);self.assertEqual(r['classification_counts']['ORPHAN_BLOB'],1)
 def test_unrelated_database_store_is_refused(self):
  other_db=self.root/'other.sqlite3'
  with connect(other_db,create=True) as other:bind_store(other,self.root/'other_store')
  r=self.scan(self.root/'other_store')
  self.assertFalse(r['gate_passed']);self.assertEqual(r['entries'],[]);self.assertIn('STORE_IDENTITY',{x['code'] for x in r['failure_reasons']})

if __name__=='__main__':unittest.main()
