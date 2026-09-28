from pathlib import Path
import json
O=Path(__file__).resolve().parents[1]
def write(name,fields):
 props={}
 for key,kind in fields.items():
  if kind=='hash':props[key]={'type':'string','pattern':'^[0-9a-f]{64}$'}
  elif kind=='string':props[key]={'type':'string','minLength':1}
  elif isinstance(kind,dict):props[key]=kind
  else:props[key]={'type':kind}
 (O/(name+'.schema.json')).write_text(json.dumps({'$schema':'https://json-schema.org/draft/2020-12/schema','$id':name+'.schema.json','type':'object','properties':props,'required':list(props),'additionalProperties':False},sort_keys=True,indent=2),encoding='utf-8')
write('PACKET_ACKNOWLEDGEMENT',{**{k:'string' for k in ['acknowledgement_id','run_id','report_id','primary_context_id','timestamp']},**{k:'hash' for k in ['source_sha256','methodology_sha256','context_architecture_sha256','path_containment_sha256','recovery_protocol_sha256','packet_template_sha256','packet_sha256']},'status':{'const':'ACKNOWLEDGED'},'fork_history':{'const':'none'}})
write('PRE_ACCESS_RECEIPT',{**{k:'string' for k in ['run_id','atomic_unit_id','report_id','source_file_id','packet_acknowledgement_id','static_status','role','prior_consumption_state','commit_timestamp']},**{k:'hash' for k in ['source_sha256','packet_sha256','ack_sha256','helper_receipt_sha256']},'immutable_fingerprints':{'type':'object','required':['methodology','context','path','recovery','integration'],'additionalProperties':{'type':'string','pattern':'^[0-9a-f]{64}$'}},'semantic_status':{'const':'SEMANTIC_CONTEXT_CLEAN'},'source_access_started':{'const':False}})
write('SOURCE_ACCESS_EVENT',{**{k:'string' for k in ['event_id','timestamp','session_id','run_id','report_id','context_id','prior_state']},**{k:'hash' for k in ['event_sha256','previous_event_sha256','source_sha256','packet_sha256','triggering_receipt_sha256']},'sequence':{'type':'integer','minimum':1},'event_type':{'const':'SOURCE_ACCESS_BEGAN'},'new_state':{'const':'CONSUMED_VALIDATION_EVIDENCE'}})
write('CONSUMPTION_STATE',{**{k:'string' for k in ['run_id','report_id','source_access_event_id','prior_state']},'source_sha256':'hash','state':{'const':'CONSUMED_VALIDATION_EVIDENCE'},'irreversible':{'const':True}})
