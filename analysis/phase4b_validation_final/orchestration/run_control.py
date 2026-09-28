"""Durable coordinator milestones and disposable root exports.

Report-local Phase4BD engines alone authorize source consumption. This engine
records engineering milestones; no source-release function is exposed here.
"""
import sys,shutil,json
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parents[1];R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
from bridge import Engine,canonical,filehash,read
def export():
 root=O/'durable_run'
 for name in ['RECOVERY_STATE.json','RECOVERY_EVENTS.jsonl']:
  if (root/name).exists():shutil.copyfile(root/name,O/name)
 dest=O/'milestone_receipts';dest.mkdir(exist_ok=True)
 for p in (root/'milestone_receipts').glob('*') if (root/'milestone_receipts').exists() else []:
  q=dest/p.name
  if q.exists() and q.read_bytes()!=p.read_bytes():raise RuntimeError('RECEIPT_EXPORT_CONFLICT')
  if not q.exists():shutil.copyfile(p,q)
def commit(unit,records,next_operation):
 e=Engine(O/'durable_run')
 payload={'unit':unit,'records':[{'path':str(p.resolve()),'size':p.stat().st_size,'sha256':filehash(p)} for p in sorted(map(Path,records))]}
 with e.lock('coordinator'):
  start=e.begin(unit,{'record_manifest':__import__('hashlib').sha256(canonical(payload)).hexdigest()},['outputs/'+unit.lower()+'.json'])
  if not start.get('already_committed'):e.commit({'outputs/'+unit.lower()+'.json':canonical(payload)},next_operation=next_operation)
  elif read(e.root/('outputs/'+unit.lower()+'.json'))!=payload:raise RuntimeError('COORDINATOR_REPLAY_CONFLICT')
 export()
if __name__=='__main__':
 if sys.argv[1]=='export':export()
 else:commit(sys.argv[1],sys.argv[3:],sys.argv[2])
