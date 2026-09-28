import json,unittest
from pathlib import Path
from support_v4 import validate_graph,SupportFailure
F=Path(__file__).resolve().parents[3]/'b01_failure_fixtures'
class B01Generalized(unittest.TestCase):pass
def make_test(path):
    def test(self):
        x=json.loads(path.read_text(encoding='utf-8'));validate_graph(x['positive'])
        with self.assertRaisesRegex(SupportFailure,x['expected_error']):validate_graph(x['negative'])
    return test
for path in sorted(F.glob('F*.json')):setattr(B01Generalized,'test_'+path.stem,make_test(path))
