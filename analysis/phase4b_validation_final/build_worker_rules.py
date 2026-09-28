"""Derive source-independent operative routing rules, excluding history labels."""
import hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent
p=O/'MODEL_ROUTING_POLICY.json';raw=p.read_bytes();policy=json.loads(raw)
keys=['version','requested_models','mandatory_A_I_escalation_exact','SOL_responsibilities_exact','ASTRA_responsibilities_exact','whole_report_escalation_exact','whole_report_reason_codes','lower_risk_sampling_exact','sampling_algorithm','sampling_size','no_numeric_confidence_threshold','policy_failure']
rules={k:policy[k] for k in keys}
rules.update({'routing_policy_sha256':hashlib.sha256(raw).hexdigest(),'independent_verification':'Receive only current source, frozen methodology, atomic proposition, proposed support locators, required support roles, necessary current source context. No persuasive processor rationale. Independently determine source support; structured result only.','immutable_for_all_selected_reports':True,'no_result_adaptive_routing':True,'runtime_model_identity':'MODEL_RUNTIME_IDENTITY_UNVERIFIED'})
data=json.dumps(rules,sort_keys=True,indent=2).encode()
if b'B01' in data or b'AgentDojo' in data:raise RuntimeError('HISTORICAL_IDENTIFIER')
with (O/'MODEL_ROUTING_WORKER_RULES.json').open('xb') as f:f.write(data)
with (O/'MODEL_ROUTING_CONTROL_CLASSIFICATION.json').open('x',encoding='utf-8') as f:json.dump({'MODEL_ROUTING_POLICY.json':'COORDINATOR_ONLY_NEVER_WORKER_PACKET','MODEL_ROUTING_POLICY.md':'COORDINATOR_ONLY_NEVER_WORKER_PACKET','MODEL_ROUTING_WORKER_RULES.json':'GENERIC_NORMATIVE_ROUTING_PENDING_CONTEXT_REVIEW','routing_policy_sha256':rules['routing_policy_sha256']},f,sort_keys=True,indent=2)
print('ROUTING_POLICY_SHA256',rules['routing_policy_sha256'],'WORKER_RULES_SHA256',hashlib.sha256(data).hexdigest())
