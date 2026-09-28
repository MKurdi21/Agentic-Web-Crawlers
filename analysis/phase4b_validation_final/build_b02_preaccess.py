"""Metadata-only current B02 packet and source-independent primary wrapper."""
import sys,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1];D=R/'analysis/phase4bd_real_source_continuity'
sys.path.insert(0,str(D/'integration_layer'))
import bridge
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(p,v):
 with p.open('xb') as f:f.write(bridge.canonical(v))
x=read(O/'HOLDOUT_PROCESSING_ORDER.json')['order'][0]
if x['holdout_id']!='B02':raise RuntimeError('ORDER')
entry={**x,'development_id':'B02','source_path':str(R/x['path']),'source_role':'UNTOUCHED_VALIDATION_EVIDENCE','prior_consumption_state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE'}
data,meta=bridge.packet(entry);scan=bridge.scan(data,entry)
P=O/'private_worker_material/B02_preaccess';P.mkdir(parents=True,exist_ok=True)
with (P/'approved_generic_packet.json').open('xb') as f:f.write(data)
rules=read(O/'MODEL_ROUTING_WORKER_RULES.json');template=read(O/'orchestration/PRIMARY_TASK_TEMPLATE.json')
identity={k:x[k] for k in ['holdout_id','report_id','source_file_id','source_sha256']}
wrapper={'version':'phase4b-model-primary-wrapper-v1.0.0','identity':identity,'phase':'PHASE4B_FINAL','scientific_namespace':'NON_AUTHORITATIVE_VALIDATION','operational_authorization':template['operational_authorization'],'generic_packet_sha256':bridge.digest(data),'routing_policy_sha256':bridge.filehash(O/'MODEL_ROUTING_POLICY.json'),'primary_task_template':template,'model_routing_worker_rules':rules,'source_delivered':False,'source_derived_material':'NEVER_PACKAGE'}
raw=bridge.canonical(wrapper)
if any(q in raw for q in [b'B01',b'AgentDojo',b'prior holdout results',b'historical Phase4 failures']):raise RuntimeError('FORBIDDEN_HISTORY')
with (P/'PRIMARY_MODEL_WRAPPER.json').open('xb') as f:f.write(raw)
put(P/'PACKET_BUILD_METADATA.json',meta);put(P/'PACKET_STATIC_SCAN.json',scan)
hashes={p.name:bridge.filehash(p) for p in P.iterdir() if p.is_file()}
put(P/'PREACCESS_METADATA_MANIFEST.json',{'status':'METADATA_PACKET_BUILT_PENDING_SEMANTIC_REVIEW','source_opened':False,'source_consumed':False,'identity':identity,'files':hashes,'generic_builder_sha256':bridge.filehash(D/'integration_layer/bridge.py'),'routing_policy_sha256':wrapper['routing_policy_sha256'],'private_classification':'NEVER_PACKAGE'})
print(json.dumps({'directory':str(P),'hashes':hashes,'source_opened':False,'source_consumed':False}))
