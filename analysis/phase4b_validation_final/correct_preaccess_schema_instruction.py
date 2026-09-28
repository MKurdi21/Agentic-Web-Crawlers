"""Correct an unfrozen template instruction; frozen scientific schema unchanged."""
import sys,json
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
import bridge
P=O/'private_worker_material/B02_preaccess';p=P/'PRIMARY_MODEL_WRAPPER.json'
old=bridge.filehash(p);w=bridge.read(p);w['primary_task_template']=bridge.read(O/'orchestration/PRIMARY_TASK_TEMPLATE.json')
p.write_bytes(bridge.canonical(w));m=P/'PREACCESS_METADATA_MANIFEST.json';v=bridge.read(m)
v['files'][p.name]=bridge.filehash(p);v['primary_task_template_sha256']=bridge.filehash(O/'orchestration/PRIMARY_TASK_TEMPLATE.json');v['pre_freeze_schema_correction']='DECLARED_SCHEMA_ENUM_UNREVIEWED_OR_UNRESOLVED';m.write_bytes(bridge.canonical(v))
log={'reason':'PRE_FREEZE_TEMPLATE_SCHEMA_ENUM_CORRECTION','old_wrapper_sha256':old,'wrapper_sha256':bridge.filehash(p),'manifest_sha256':bridge.filehash(m),'scientific_schema_changed':False,'source_opened':False,'source_consumed':False}
with (O/'PRE_FREEZE_SCHEMA_INSTRUCTION_CORRECTION.json').open('xb') as f:f.write(bridge.canonical(log))
print(json.dumps(log))
