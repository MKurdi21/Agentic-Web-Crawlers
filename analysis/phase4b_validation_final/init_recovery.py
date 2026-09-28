"""Initialize frozen recovery engine without opening a scientific source."""
import sys,os,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1];D=R/'analysis/phase4bd_real_source_continuity';S=R/'analysis/phase4bc_supplement'
sys.path.insert(0,str(D/'integration_layer'))
import bridge
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def h(p):return bridge.filehash(p)
def put(n,v):
 with (O/n).open('x',encoding='utf-8') as f:json.dump(v,f,sort_keys=True,indent=2)
b=read(O/'PHASE4B_FINAL_BASELINE.json');policy=read(O/'MODEL_ROUTING_POLICY.json')
if b['status']!='PASS' or not policy['frozen_before_source_access']:raise RuntimeError('PRE_SOURCE_BINDING_FAILED')
x=read(O/'HOLDOUT_PROCESSING_ORDER.json')['order'][0]
entry={**x,'development_id':x['holdout_id'],'source_path':str(R/x['path']),'source_role':'UNTOUCHED_VALIDATION_EVIDENCE','prior_consumption_state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE'}
packet,meta=bridge.packet(entry)
if bridge.codehash()!=b['frozen_pins']['real_source_continuity']:raise RuntimeError('INTEGRATION_DRIFT')
pins={'methodology_sha256':b['frozen_pins']['scientific_methodology'],'context_architecture_sha256':b['frozen_pins']['context_architecture'],'immutable_code_sha256':b['frozen_pins']['real_source_continuity'],'protected_file_manifest_sha256':h(O/'PROTECTED_FILES_INITIAL.csv'),'source_sha256':x['source_sha256'],'current_packet_sha256':bridge.digest(packet)}
names=['PHASE4B_FINAL_BASELINE.json','MODEL_ROUTING_POLICY.json','MODEL_ROUTING_POLICY.md','HOLDOUT_PROCESSING_ORDER.json','PROTECTED_FILES_INITIAL.csv','baseline.py','init_recovery.py']
bindings=[{'path':str(O/n),'sha256':h(O/n)} for n in names]
bindings += [{'path':str(p),'sha256':h(p)} for p in [D/'INTEGRATION_MANIFEST.json',D/'FINAL_HANDOFF.json',D/'integration_layer/bridge.py',S/'recovery_protocol/engine.py',S/'RECOVERY_STATE.schema.json']]
# New orchestration wrapper must exist before durable initialization and be bound.
for n in sys.argv[1:]:
 p=(O/n).resolve()
 if not p.is_relative_to(O) or not p.is_file():raise RuntimeError('WRAPPER_BINDING_REQUIRED')
 bindings.append({'path':str(p),'sha256':h(p)})
if len(sys.argv)<2:raise RuntimeError('WRAPPER_BINDING_REQUIRED')
if not all(len(v)==64 and all(c in '0123456789abcdef' for c in v) for v in pins.values()):raise RuntimeError('PIN_SCHEMA')
put('RECOVERY_INITIALIZATION_BINDINGS.json',{'phase':'PHASE4B_FINAL','pins':pins,'bindings':bindings,'routing_policy_sha256':h(O/'MODEL_ROUTING_POLICY.json'),'path_containment_sha256':b['frozen_pins']['path_containment'],'recovery_protocol_sha256':b['frozen_pins']['recovery_protocol'],'continuity_adapter_sha256':b['frozen_pins']['continuity_adapter'],'generic_builder_sha256':h(D/'integration_layer/bridge.py'),'packet_binding_internal_compatibility_phase':'PHASE4BD_DEVELOPMENT','source_opened':False,'source_consumed':False,'packet_metadata':meta})
bindings.append({'path':str(O/'RECOVERY_INITIALIZATION_BINDINGS.json'),'sha256':h(O/'RECOVERY_INITIALIZATION_BINDINGS.json')})
e=bridge.Engine(O/'durable_run')
with e.lock('/root/sol_preflight'):state=e.init('phase4b-validation-final',pins,phase='PHASE4B_FINAL',bindings=bindings)
# Root exports are disposable views; durable_run remains coordinator authority.
for name in ['RECOVERY_STATE.json','RECOVERY_EVENTS.jsonl']:
 (O/name).write_bytes((O/'durable_run'/name).read_bytes())
print(json.dumps({'status':'RECOVERY_INITIALIZED','next_permitted_operation':state['next_permitted_operation'],'packet_sha256':pins['current_packet_sha256'],'routing_policy_sha256':h(O/'MODEL_ROUTING_POLICY.json')}))
