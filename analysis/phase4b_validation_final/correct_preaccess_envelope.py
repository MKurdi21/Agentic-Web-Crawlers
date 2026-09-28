"""Pre-freeze wrapper authorization clarification. No scientific asset changes."""
import json,sys
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
import bridge
P=O/'private_worker_material/B02_preaccess'
old_wrapper=bridge.filehash(P/'PRIMARY_MODEL_WRAPPER.json')
old_manifest=bridge.filehash(P/'PREACCESS_METADATA_MANIFEST.json')
packet_hash=bridge.filehash(P/'approved_generic_packet.json')
wrapper=bridge.read(P/'PRIMARY_MODEL_WRAPPER.json');template=bridge.read(O/'orchestration/PRIMARY_TASK_TEMPLATE.json')
wrapper.update({'phase':'PHASE4B_FINAL','scientific_namespace':'NON_AUTHORITATIVE_VALIDATION','operational_authorization':template['operational_authorization'],'primary_task_template':template})
raw=bridge.canonical(wrapper)
if any(x in raw for x in [b'B01',b'AgentDojo',b'prior holdout results',b'historical Phase4 failures']):raise RuntimeError('FORBIDDEN_HISTORY')
(P/'PRIMARY_MODEL_WRAPPER.json').write_bytes(raw)
manifest=bridge.read(P/'PREACCESS_METADATA_MANIFEST.json')
manifest['files']['PRIMARY_MODEL_WRAPPER.json']=bridge.digest(raw)
manifest['primary_task_template_sha256']=bridge.filehash(O/'orchestration/PRIMARY_TASK_TEMPLATE.json')
manifest['pre_freeze_correction']='OUTER_OPERATIONAL_AUTHORIZATION_CLARIFIED'
(P/'PREACCESS_METADATA_MANIFEST.json').write_bytes(bridge.canonical(manifest))
if bridge.filehash(P/'approved_generic_packet.json')!=packet_hash:raise RuntimeError('SCIENTIFIC_PACKET_CHANGED')
log={'phase':'PHASE4B_FINAL','reason':'PRE_FREEZE_OPERATIONAL_AUTHORIZATION_CLARIFICATION','old_wrapper_sha256':old_wrapper,'new_wrapper_sha256':bridge.digest(raw),'old_manifest_sha256':old_manifest,'new_manifest_sha256':bridge.filehash(P/'PREACCESS_METADATA_MANIFEST.json'),'unchanged_generic_packet_sha256':packet_hash,'source_access':False,'source_consumed':False,'other_report_content_included':False,'historical_findings_included':False,'frozen_scientific_assets_changed':False}
with (O/'PRE_FREEZE_AUTHORIZATION_CORRECTION.json').open('xb') as f:f.write(bridge.canonical(log))
print(json.dumps(log))
