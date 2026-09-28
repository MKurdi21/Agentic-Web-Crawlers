"""Independent record/count/fingerprint arithmetic; no producer validation helpers."""
import json,hashlib,csv,re
from pathlib import Path
from decimal import Decimal
O=Path(__file__).resolve().parent;P=O/'private_source_material';C=O/'candidate_v4br'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=read(P/'original_phase4b/holdout_validation/B01/private/normalized_evidence_items.json')
ver=read(P/'original_phase4b/holdout_validation/B01/private/COMBINED_VERIFICATION_RESULTS.json')['results']
expected={x['stable_item_id'] for x in ver if x['critical'] and x['detected_false_accept']}
rows=read(O/'B01_SUPPORT_ADJUDICATION.json')['adjudications'];assert len(rows)==80 and len({x['challenge_id'] for x in rows})==80 and {x['evidence_item_id'] for x in rows}==expected
assert len(list(csv.DictReader((O/'B01_SUPPORT_ADJUDICATION_MATRIX.csv').open(encoding='utf-8'))))==80
cross=read(O/'DEVELOPMENT_ITEM_CROSSWALK.json')['items'];assert {x['original_evidence_item_id'] for x in cross}=={x['stable_item_id'] for x in old}
cfg=read(O/'REMEDIATED_WORKFLOW_CONFIGURATION.json');definition={k:v for k,v in cfg.items() if k in ['methodology_version','evidence_schema_version','parent_methodology_sha256','candidate_files','dependency_manifest_sha256','runtime_python']}
computed=hashlib.sha256(json.dumps(definition,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest();assert computed==cfg['methodology_sha256']
for x in cfg['candidate_files']:assert h(C/x['relative_path'])==x['sha256']
comparisons=[]
for f in sorted((P/'development_graphs').glob('COMP_*.json')):
    g=read(f);cl=g['claims'][0];co=cl['comparison'];values=[Decimal(r['value']) for r in g['results']];v=max(values) if co['operation']=='MAX' else min(values)
    assert v==Decimal(co['expected']);assert sum(x==v for x in values)==1
    comparisons.append({'graph_id':f.stem,'row_count':len(values),'ranking_matches':True,'unique_extremum':True})
reg=read(O/'test_results/B01_REGRESSION_RESULTS.json');assert len(reg['items'])==45 and len({x['original_evidence_item_id'] for x in reg['items']})==45 and reg['regressed']==0 and reg['now_unresolved']==0
receipt=read(P/'access/final_development/PRE_ACCESS_RECEIPT.json');event=read(P/'access/final_development/SOURCE_ACCESS_BEGAN.json');assert receipt['created_at']<=event['created_at'] and receipt['sequence']==1 and event['sequence']==2
assert event['receipt_sha256']==hashlib.sha256(json.dumps(receipt,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
reservation=read(O/'PHASE4B_RESUME_HOLDOUT_MANIFEST.json');assert [x['holdout_id'] for x in reservation['reports']]==['B02','B03','B04','B05','B06','B07','B08'] and all(x['substantive_access'] is False and x['contamination_count']==0 for x in reservation['reports'])
out={'challenges_expected':80,'unique_adjudications':80,'original_items_accounted':len(old),'original_critical_items':sum(x['critical'] for x in old),'regression_cohort':45,'comparisons':comparisons,'methodology_hash_recomputed':computed,'immutable_bytes_match':True,'receipt_order_and_hash':True,'reserved_reports':7,'reserved_substantive_access_recorded':False,'passed':True,'limitations':'Independent implementation verifies IDs, counts, numeric arithmetic, hashes and recorded access state. It does not replace source adjudication, human ground truth, or OS-level access attestation.'}
(O/'test_results/INDEPENDENT_EQUIVALENCE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
