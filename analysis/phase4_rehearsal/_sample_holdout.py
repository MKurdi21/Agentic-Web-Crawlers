"""Frozen Phase 3 SHA-256 selection, applied to completed Phase 4 units."""
import hashlib,json,math,pathlib,unicodedata
from datetime import datetime,timezone
R=pathlib.Path(__file__).resolve().parent
P3=R.parent/'phase3_calibration'
protocol=hashlib.sha256((P3/'CALIBRATION_PROTOCOL.md').read_bytes()).hexdigest()
field_hash=hashlib.sha256((P3/'FIELD_CATALOG.json').read_bytes()).hexdigest()
records=[]
for lane in ('primary_a','primary_b'):
 for p in sorted((R/'holdout_validation'/lane).glob('H*.json')):
  j=json.loads(p.read_text(encoding='utf-8'))
  records.append({'holdout_id':j['holdout_id'],'paper_id':j['paper_id'],'source_sha256':j['source_sha256'],'items':j['evidence_items']})
if len(records)!=6 or len({r['holdout_id'] for r in records})!=6:raise SystemExit('HOLDOUT_UNIT_SET_INCOMPLETE')
units=[]
for rec in sorted(records,key=lambda x:x['holdout_id']):
 eligible=[]
 for item in rec['items']:
  if item['critical']:continue
  parts=[protocol,rec['holdout_id'],rec['paper_id'],item['stable_field_id'],item['stable_item_id']]
  parts=[unicodedata.normalize('NFC',str(x)) for x in parts]
  if any(not x for x in parts):raise SystemExit('EMPTY_SELECTION_COMPONENT')
  d=hashlib.sha256(b'\x00'.join(x.encode('utf-8') for x in parts)).hexdigest()
  eligible.append({'stable_item_id':item['stable_item_id'],'stable_field_id':item['stable_field_id'],'selection_digest':d})
 eligible.sort(key=lambda x:(x['selection_digest'],x['stable_item_id']))
 n=len(eligible);size=min(n,max(3,math.ceil(.25*n)))
 candidate_hash=hashlib.sha256(json.dumps(sorted(x['stable_item_id'] for x in eligible),separators=(',',':')).encode()).hexdigest()
 units.append({'holdout_id':rec['holdout_id'],'paper_id':rec['paper_id'],'eligible_lower_risk_count':n,'required_sample_size':size,'selected_item_ids':[x['stable_item_id'] for x in eligible[:size]],'selection_digests':[x['selection_digest'] for x in eligible[:size]],'protocol_sha256':protocol,'field_catalog_sha256':field_hash,'candidate_evidence_set_sha256':candidate_hash,'selection_algorithm_version':'sha256-lexicographic-v1'})
manifest={'generated_at':datetime.now(timezone.utc).isoformat(),'selection_algorithm_version':'sha256-lexicographic-v1','protocol_sha256':protocol,'units':units}
path=R/'HOLDOUT_VERIFICATION_SAMPLE_MANIFEST.json'
if path.exists():raise SystemExit('SAMPLE_MANIFEST_ALREADY_FROZEN')
path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'units':len(units),'eligible':sum(x['eligible_lower_risk_count'] for x in units),'selected':sum(x['required_sample_size'] for x in units),'manifest_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
