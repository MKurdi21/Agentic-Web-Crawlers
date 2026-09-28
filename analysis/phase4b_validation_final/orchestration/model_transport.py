"""Explicit model-context boundary around unchanged Phase4BD transport.

No scientific extraction semantics are implemented here. Actual model ACK is
provided by the fresh agent before any source delivery; deterministic PDF worker
startup is replaced only at the declared coordinator hook, not by monkeypatching
frozen modules. Parent source/receipt/consumption logic remains unchanged.
"""
from pathlib import Path
import sys
O=Path(__file__).resolve().parents[1];R=O.parents[1]
BD=R/'analysis/phase4bd_real_source_continuity'
sys.path.insert(0,str(BD/'integration_layer'))
from bridge import *
VERSION='phase4b-model-context-transport-v1.0.0'
class ModelTransport(RealContinuity):
 def __init__(self,root,ack_path,wrapper_path):
  super().__init__(root);self.ack_path=Path(ack_path);self.wrapper_path=Path(wrapper_path)
 def model_boundary(self):
  cfg,data=self.check();auth=read(cfg['authorization_path']);ack=read(self.ack_path)
  fail(filehash(self.wrapper_path)==auth['model_boundary']['wrapper_sha256'],'MODEL_WRAPPER_DRIFT')
  fail(filehash(auth['model_boundary']['routing_policy_path'])==auth['model_boundary']['routing_policy_sha256'],'MODEL_ROUTING_DRIFT')
  fail(filehash(Path(__file__))==auth['model_boundary']['adapter_sha256'],'MODEL_ADAPTER_DRIFT')
  fail(ack['packet_sha256']==cfg['packet_sha256'] and ack['source_sha256']==self.entry['source_sha256'] and ack['report_id']==self.entry['report_id'],'MODEL_ACK_BINDING')
  fail(ack['wrapper_sha256']==auth['model_boundary']['wrapper_sha256'] and ack['routing_policy_sha256']==auth['model_boundary']['routing_policy_sha256'],'MODEL_ACK_CONTROL_PINS')
  fail(ack['status']=='ACKNOWLEDGED' and ack['fork_history']=='none' and ack['previous_scientific_content_included'] is False,'MODEL_CONTEXT_ISOLATION')
  fail(ack['context_id']==auth['model_boundary']['primary_context_id'] and ack['source_accessed'] is False,'MODEL_CONTEXT_ACK_IDENTITY')
  review=read(cfg['review_path'])
  fail(review['actual_model_wrapper_sha256']==filehash(self.wrapper_path) and review['actual_model_wrapper_status']=='SEMANTIC_CONTEXT_CLEAN','MODEL_WRAPPER_REVIEW')
  self.context_id=ack['context_id']
  return ack
 def _worker_start(self,stage):
  fail(stage=='EXTRACT','MODEL_PREACCESS_STAGE')
  ack=self.model_boundary();self.context_id=ack['context_id'];self.worker_stage=stage
  return {k:ack[k] for k in ['context_id','packet_sha256','status','fork_history']}
 def release_source(self):
  self.model_boundary();source=self._source_bytes();fail(self.e.state()['source_access_started'],'MODEL_DELIVERY_BEFORE_CONSUMPTION')
  directory=self.root/'source_delivery';directory.mkdir(exist_ok=True)
  target=directory/'current_source.pdf'
  if target.exists():fail(filehash(target)==self.entry['source_sha256'],'SOURCE_SNAPSHOT_CONFLICT')
  else:exclusive(target,source)
  receipt={'report_id':self.entry['report_id'],'source_sha256':self.entry['source_sha256'],'packet_sha256':self.cfg['packet_sha256'],'primary_context_id':self.context_id,'source_path':str(target),'consumption_sha256':filehash(self.e.root/'outputs/consumption.json'),'model_ack_sha256':filehash(self.ack_path),'routing_policy_sha256':read(self.ack_path)['routing_policy_sha256'],'wrapper_sha256':filehash(self.wrapper_path),'state':'CONSUMED_VALIDATION_EVIDENCE','namespace':'NON_AUTHORITATIVE_VALIDATION','source_bytes_delivered_to_private_snapshot':True}
  with self.e.lock('model-source-delivery'):self._commit('MODEL_SOURCE_DELIVERY',receipt)
  return receipt
