from pathlib import Path
import sys,json
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
fixture=read(O/'REAL_SOURCE_INTEGRATION_FIXTURE.json')
entry={k:fixture[k] for k in ['source_role','report_id','development_id','source_file_id','source_sha256','source_path','prior_consumption_state']}
auth={'version':'phase4bd-development-authorization-v1','reports':{entry['report_id']:entry},'permitted_source_roles':['CONSUMED_DEVELOPMENT_EVIDENCE'],'reserved_denied_report_ids':fixture['reserved_reports_excluded'],'scope':'User-authorized Phase4BD already-consumed development evidence only; no holdout access'}
exclusive(O/'DEVELOPMENT_AUTHORIZATION.json',canonical(auth))
data,meta=packet(entry);static=scan(data,entry)
(O/'test_results').mkdir(exist_ok=True)
exclusive(O/'test_results/development_packet.json',data)
exclusive(O/'test_results/PACKET_BUILD.json',canonical(meta))
exclusive(O/'test_results/PACKET_STATIC_SCAN.json',canonical(static))
e=Engine(O/'recovery_receipts');base=read(O/'PHASE4BD_BASELINE.json')
pins={'methodology_sha256':METHOD,'context_architecture_sha256':base['frozen_pins']['context_architecture'],'immutable_code_sha256':base['recovery_sha256'],'protected_file_manifest_sha256':filehash(O/'PROTECTED_FILES_INITIAL.csv'),'source_sha256':entry['source_sha256'],'current_packet_sha256':digest(data)}
with e.lock('/root'):
 e.init('phase4bd',pins,phase='PHASE4BD_ENGINEERING',bindings=[{'path':str(S/'recovery_protocol/engine.py'),'sha256':filehash(S/'recovery_protocol/engine.py')}])
 e.begin('IMPLEMENT_REAL_SOURCE_INTEGRATION',{'baseline':filehash(O/'PHASE4BD_BASELINE.json')},['outputs/integration_manifest.json','outputs/test_summary.json'])
print('Prepared packet',digest(data),'wrapper',filehash(O/'integration_layer/worker_contract.json'))
