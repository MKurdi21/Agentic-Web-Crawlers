"""Generate the closed recovery records' Draft 2020-12 contracts."""
from pathlib import Path
from engine import *
O=Path(__file__).resolve().parents[1]
S={'type':'string'};N={'type':['string','null']};H={'type':'string','pattern':'^[0-9a-f]{64}$'};NH={'type':['string','null'],'pattern':'^[0-9a-f]{64}$'}
ID={'type':'string','pattern':'^[A-Za-z0-9_-]{1,100}$'}
def schema(name,props,required=None,extra=False):
    d={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':name,'type':'object','properties':props,'required':required or list(props),'additionalProperties':extra}
    (O/name).write_bytes(canonical(d)+b'\n')
state={k:N for k in ['current_atomic_unit','current_atomic_unit_id','atomic_unit_status','last_committed_milestone','active_holdout_id','source_access_event_id','primary_context_id']}
state.update({k:S for k in ['phase_id','phase_version','methodology_version','context_architecture_version','next_permitted_operation','active_holdout_state','lane_b_state','created_at','updated_at','usage_headroom']})
state.update({k:NH for k in PIN_KEYS});state.update(run_id=ID,protocol_version={'const':VERSION},status={'enum':STATES},last_committed_milestone_receipt_sha256=NH,source_access_started={'type':'boolean'},verifier_context_ids={'type':'array','items':S},live_source_verified_count={'type':'integer','minimum':0},live_promoted_count={'type':'integer','minimum':0},bindings={'type':'array','items':{'type':'object','required':['path','sha256'],'properties':{'path':S,'sha256':H},'additionalProperties':False}})
schema('RECOVERY_STATE.schema.json',state)
event={'event_id':ID,'sequence':{'type':'integer','minimum':1},'previous_event_sha256':NH,'event_sha256':H,'event_type':{'enum':['RUN_START','ATOMIC_UNIT_START','ATOMIC_UNIT_COMMIT','USAGE_LIMIT_PREEMPTION','OTHER_INTERRUPTION','RECOVERY_REQUEST','RECOVERY_PREFLIGHT_PASS','RECOVERY_PREFLIGHT_FAIL','REPLAY_START','REPLAY_COMPLETE','QUARANTINE','RUN_END','MILESTONE_RECOVERED','SOURCE_ACCESS_BEGAN']},'timestamp':S,'session_id':N}
# Event payloads vary by event kind; identity/hash/sequence envelope is mandatory.
schema('RECOVERY_EVENTS.schema.json',event,extra=True)
r={'run_id':ID,'atomic_unit_id':ID,'attempt_id':ID,'input_fingerprints':{'type':'object'},'input_sha256':H,'expected_outputs':{'type':'array','items':S},'replay_policy':{'enum':POLICIES},'previous_receipt_sha256':NH,'start_time':S,'pins':{'type':'object','properties':{k:NH for k in PIN_KEYS},'required':PIN_KEYS,'additionalProperties':False},'protocol_version':{'const':VERSION},'output_fingerprints':{'type':'object','additionalProperties':H},'commit_time':S,'status':{'const':'COMMITTED'},'side_effects_committed':{'type':'array','items':S},'scientific_source_access':{'type':'boolean'},'validation_consumption_effect':{'type':'integer','minimum':0},'next_operation':S}
schema('MILESTONE_RECEIPT.schema.json',r)
