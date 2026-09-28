import sys,pathlib,unittest,zipfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from common import *
from package_release import allowed,inspect_candidate
from validate_archive import verify_archive
class Packaging(unittest.TestCase):
 def test_private_paths_and_types(self):
  for p in ['shadow/private_source_material/raw/abc','hardened/tests/paper.pdf','hardened/tests/article.txt','deploy_payload/AGENTS.md','../outside.md','hardened/scripts/x.zip','test_results/summary_comprehensive_summary.md']:self.assertFalse(allowed(p))
 def test_renamed_original_bytes(self):
  data=b'Synthetic original input content for exclusion test'
  with self.assertRaises(Failure):inspect_candidate('hardened/tests/renamed.py',data,{sha(data)},[])
 def test_raw_and_base64_sample(self):
  import base64
  data=b'Synthetic sensitive sample'
  for sample in [data,base64.b64encode(data)]:
   with self.assertRaises(Failure):inspect_candidate('hardened/tests/renamed.py',b'prefix'+sample+b'suffix',set(),[sample])
 def test_archive_private_member_rejected(self):
  p=guard(SHADOW/'synthetic'/uid('badarchive')).with_suffix('.zip')
  with zipfile.ZipFile(p,'w') as z:z.writestr('integration_design/shadow/private_source_material/leak.md','synthetic')
  with self.assertRaises(Failure):verify_archive(p,{'allowlist':[]})
 def test_archive_duplicate_members_rejected(self):
  import warnings
  p=guard(SHADOW/'synthetic'/uid('badarchive')).with_suffix('.zip')
  with warnings.catch_warnings():
   warnings.simplefilter('ignore')
   with zipfile.ZipFile(p,'w') as z:
    z.writestr('integration_design/PACKAGE_MANIFEST.json','{}');z.writestr('integration_design/PACKAGE_MANIFEST.json','{}')
  with self.assertRaises(Failure):verify_archive(p,{'allowlist':[]})
