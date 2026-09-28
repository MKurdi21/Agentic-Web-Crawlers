"""Freeze exact new orchestration inputs before first source release."""
import sys,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parents[1]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def entries():
 paths=list((O/'orchestration').glob('*.py'))+list((O/'orchestration').glob('*.json'))+list((O/'orchestration').glob('*.md'))+list((O/'orchestration').glob('*.txt'))
 paths += [O/x for x in ['init_recovery.py','MODEL_ROUTING_POLICY.json','MODEL_ROUTING_WORKER_RULES.json']]
 return [{'relative_path':p.relative_to(O).as_posix(),'size_bytes':p.stat().st_size,'sha256':h(p)} for p in sorted(paths)]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
target=O/'ORCHESTRATION_IMMUTABLE_MANIFEST.json'
if sys.argv[1]=='freeze':
 with target.open('xb') as f:f.write(canonical({'version':'phase4b-model-context-transport-v1.0.0','files':entries()}))
 print('FROZEN',h(target))
elif sys.argv[1]=='verify':
 old=json.loads(target.read_bytes())
 if old['files']!=entries():raise RuntimeError('ORCHESTRATION_METHODOLOGY_DRIFT')
 print('PASS',h(target))
