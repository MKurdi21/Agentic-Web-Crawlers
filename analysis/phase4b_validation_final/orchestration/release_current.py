"""Current-report-only delivery after reviewed packet and actual model ACK."""
import sys,json
from pathlib import Path
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
import model_transport as m
O=Path(__file__).resolve().parents[1];R=O.parents[1]
def release(holdout):
 order=m.read(O/'HOLDOUT_PROCESSING_ORDER.json')['order'];x=next(i for i in order if i['holdout_id']==holdout)
 tracker=m.read(O/'HOLDOUT_STATE_TRACKER.json')
 previous=order[:order.index(x)]
 for p in previous:
  row=next(i for i in tracker['reports'] if i['holdout_id']==p['holdout_id'])
  m.fail(row.get('result') in ['HOLDOUT_VALIDATION_PASS','HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS'] and row['completed'],'PREVIOUS_REPORT_GATE')
 d=O/'private_worker_material'/(holdout+'_preaccess');wrapper=d/'PRIMARY_MODEL_WRAPPER.json';ack=d/'MODEL_ACK.json';raw=m.read(d/'SEMANTIC_REVIEW_RAW.json')
 m.fail(raw['status']=='SEMANTIC_CONTEXT_CLEAN' and raw['packet_sha256']==m.filehash(d/'approved_generic_packet.json') and raw['actual_model_wrapper_sha256']==m.filehash(wrapper),'MODEL_SEMANTIC_REVIEW')
 entry={**x,'development_id':holdout,'source_path':str(R/x['path']),'source_role':'UNTOUCHED_VALIDATION_EVIDENCE','prior_consumption_state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE'}
 review={**raw,'wrapper_sha256':m.filehash(m.BD/'integration_layer/worker_contract.json'),'current_identity_exception_approved':True,'review_mode':'SEPARATE_CONTEXT_MODEL_VERIFICATION','review_protocol_sha256':m.read(m.C/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json')['semantic_review_protocol_sha256'],'exception_scope':{'/binding/holdout_id':holdout,'/binding/paper_id':x['report_id']},'actual_model_wrapper_status':raw['status']}
 auth={'reports':{x['report_id']:entry},'reserved_denied_report_ids':[i['report_id'] for i in order if i!=x],'permitted_source_roles':['UNTOUCHED_VALIDATION_EVIDENCE'],'model_boundary':{'wrapper_sha256':m.filehash(wrapper),'routing_policy_path':str(O/'MODEL_ROUTING_POLICY.json'),'routing_policy_sha256':m.filehash(O/'MODEL_ROUTING_POLICY.json'),'adapter_sha256':m.filehash(m.__file__),'primary_context_id':m.read(ack)['context_id']}}
 for name,obj in [('TRANSPORT_REVIEW.json',review),('AUTHORIZATION.json',auth)]:
  p=d/name
  if p.exists():m.fail(m.read(p)==obj,'CONTROL_REPLAY_CONFLICT')
  else:m.exclusive(p,m.canonical(obj))
 root=O/'private_worker_material'/holdout
 transport=m.ModelTransport(root,ack,wrapper)
 if not (root/'configuration.json').exists():transport.create(d/'AUTHORIZATION.json',x['report_id'],d/'TRANSPORT_REVIEW.json')
 transport.prepare();transport.preaccess();receipt=transport.release_source()
 row=next(i for i in tracker['reports'] if i['holdout_id']==holdout)
 row.update(opened=True,consumed=True,state='VALIDATION_IN_PROGRESS',primary_context_id=receipt['primary_context_id'],source_access_receipt_sha256=m.filehash(root/'durable/outputs/consumption.json'))
 m.replace(O/'HOLDOUT_STATE_TRACKER.json',tracker)
 print(json.dumps({'status':'SOURCE_DELIVERED_AFTER_COMMIT','holdout_id':holdout,'source_snapshot':receipt['source_path'],'source_sha256':receipt['source_sha256']}))
if __name__=='__main__':release(sys.argv[1])
