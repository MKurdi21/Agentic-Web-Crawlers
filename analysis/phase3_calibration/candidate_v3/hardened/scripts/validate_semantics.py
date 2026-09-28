"""Five-layer deterministic validation. No inference of scientific truth."""
import datetime,re,urllib.parse
from common import *
from jsonschema import Draft202012Validator
class ValidationError(Failure):
 def __init__(self,code,layer,detail=''):self.layer=layer;super().__init__(code,detail)
def require(ok,code,layer,detail=''):
 if not ok:raise ValidationError(code,layer,detail)
def parse(data):
 def pairs(items):
  d={}
  for k,v in items:
   require(k not in d,'DUPLICATE_KEY',1,k);d[k]=v
  return d
 try:return json.loads(data.decode('utf-8') if isinstance(data,bytes) else data,object_pairs_hook=pairs,parse_constant=lambda v:(_ for _ in ()).throw(ValueError(v)))
 except ValidationError:raise
 except (ValueError,UnicodeError) as e:raise ValidationError('PARSE',1,str(e))
def fmt(name,value):
 patterns={'sha256':r'[0-9a-f]{64}','identifier':r'[A-Za-z0-9][A-Za-z0-9_.:-]*','semver':r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?','doi':r'10\.\d{4,9}/\S+'}
 if name in patterns:return bool(re.fullmatch(patterns[name],value))
 if name=='http-uri':
  try:u=urllib.parse.urlsplit(value);return u.scheme in ('http','https') and bool(u.hostname) and not any(c.isspace() for c in value)
  except ValueError:return False
 if name=='timestamp':
  try:return datetime.datetime.fromisoformat(value.replace('Z','+00:00')).tzinfo is not None and 'T' in value
  except ValueError:return False
 return False
def formats(schema,value):
 if 'format' in schema:require(fmt(schema['format'],value),'FORMAT',3,schema['format'])
 if isinstance(value,dict):
  for k,v in value.items():formats(schema.get('properties',{}).get(k,{}),v)
 if isinstance(value,list):
  for v in value:formats(schema.get('items',{}),v)
 for branch in schema.get('oneOf',[]):
  if Draft202012Validator(branch).is_valid(value):formats(branch,value)
def walk(obj):
 yield obj
 if isinstance(obj,dict):
  for v in obj.values():yield from walk(v)
 elif isinstance(obj,list):
  for v in obj:yield from walk(v)
def record(c,rid):
 row=c.execute('SELECT * FROM records WHERE record_id=? AND current=1',(rid,)).fetchone()
 require(row is not None,'REFERENCE_NOT_CURRENT',5,rid);return dict(row)
def trusted_receipt(c,artifact_sha256):
 for r in c.execute("SELECT * FROM reviews WHERE artifact_sha256=? AND current=1 AND trusted=1 AND decision='APPROVE'",(artifact_sha256,)):
  p=json.loads(r['payload_json']);e=c.execute("SELECT payload_json FROM events WHERE subject=? AND event_type='SYNTHETIC_REVIEW'",(r['review_id'],)).fetchone()
  if e and json.loads(e[0]).get('content_sha256')==sha(canonical(p).encode()) and p.get('artifact_sha256')==artifact_sha256 and p.get('trust_origin')=='SYNTHETIC_ONLY' and fmt('timestamp',p.get('timestamp','')):return True
 return False
def validate(kind,payload,db=None,context=None):
 p=parse(payload) if isinstance(payload,(bytes,str)) else parse(canonical(payload))
 schema_path=DESIGN/'hardened/schemas'/f'{kind}.schema.json'
 require(schema_path.is_file(),'UNKNOWN_SCHEMA',2,kind)
 schema=json.loads(schema_path.read_text(encoding='utf-8'))
 errors=list(Draft202012Validator(schema).iter_errors(p));require(not errors,'SCHEMA',2,str(errors[0].message) if errors else '')
 formats(schema,p)
 ids=[]
 for x in walk(p):
  if isinstance(x,str):require(bool(x.strip()),'EMPTY_TEXT',4)
  if not isinstance(x,dict):continue
  if 'record_id' in x:ids.append(x['record_id'])
  t=x.get('type')
  if t in ('PAGE_RANGE','TEXT_SPAN'):require(x['end']>=x['start']+(t=='TEXT_SPAN'),'RANGE',4)
  if t=='REPOSITORY_FILE':require(not pathlib.PurePosixPath(x['path']).is_absolute() and '..' not in pathlib.PurePosixPath(x['path']).parts and '\\' not in x['path'],'REPOSITORY_PATH',4)
  if 'paper_report_id' in x and 'paper_report_id' in p:require(x['paper_report_id']==p['paper_report_id'],'CROSS_PAPER',4)
  if t and 'source_sha256' in x and 'source_sha256' in p:require(x['source_sha256']==p['source_sha256'],'LOCATOR_SOURCE',4)
 require(len(ids)==len(set(ids)),'DUPLICATE_RECORD',4)
 if kind=='evidence':
  own={x['record_id'] for x in p['items']}
  for e in p['entities']:require(set(e['evidence_ids'])<=own,'ENTITY_EVIDENCE',4)
 if kind=='contradiction':require(len(set(p['claim_ids']))>=2,'CONTRADICTION_PAIR',4)
 if kind=='synthesis':
  require(p['report_count']==len(set(p['report_ids'])) and p['object_count']==len(set(p['research_object_ids'])),'DENOMINATOR',4)
  require(len(p['input_ids'])==len(set(p['input_ids'])),'DUPLICATE_INPUT',4)
 if context:
  if 'paper_report_id' in p:require(p['paper_report_id']==context['paper_report_id'],'TASK_PAPER',5)
  if 'source_sha256' in p:require(p['source_sha256']==context['source_sha256'],'TASK_SOURCE',5)
 if db is not None:
  if 'paper_report_id' in p:
   r=db.execute('SELECT s.sha256,s.pages FROM reports r JOIN sources s USING(source_id) WHERE paper_report_id=?',(p['paper_report_id'],)).fetchone()
   require(r is not None and r['sha256']==p['source_sha256'],'CURRENT_SOURCE',5)
   for x in walk(p):
    if isinstance(x,dict) and x.get('type') in ('PAGE','PAGE_RANGE') and r['pages']:
     require(x.get('page',x.get('end'))<=r['pages'],'PAGE_BOUNDS',5)
    if isinstance(x,dict) and x.get('type')=='TEXT_SPAN':
     a=db.execute('SELECT path FROM artifacts WHERE sha256=?',(x['text_sha256'],)).fetchone();require(a is not None,'TEXT_ARTIFACT',5)
     require(x['end']<=len(pathlib.Path(a['path']).read_text(encoding='utf-8')),'SPAN_BOUNDS',5)
  if kind=='verification':
   for item in p['items']:
    r=record(db,item['evidence_id']);require(r['kind']=='claim' and r['paper_report_id']==p['paper_report_id'] and r['artifact_sha256']==item['evidence_sha256'],'VERIFICATION_TARGET',5)
    require(item['status'] not in ('SUPPORTED','PARTIALLY_SUPPORTED') or item['locator']['type']!='UNKNOWN','UNLOCATED_SUPPORT',5)
  if kind=='research_object':
   for rid in p['members']:require(db.execute('SELECT 1 FROM reports WHERE paper_report_id=?',(rid,)).fetchone() is not None,'MEMBER',5)
   evidence_reports={record(db,rid)['paper_report_id'] for rid in p['evidence_ids']}
   require(evidence_reports<=set(p['members']),'RELATIONSHIP_EVIDENCE_SCOPE',5)
   if p['state']=='CONFIRMED':require(evidence_reports==set(p['members']),'RELATIONSHIP_EVIDENCE_COVERAGE',5)
  if kind=='paper_taxonomy_coding':
   tax=json.loads(record(db,p['taxonomy_id'])['payload_json']);require(tax['version']==p['taxonomy_version'],'TAXONOMY_VERSION',5)
   terms={t['term_id'] for t in tax['terms']}
   for code in p['codes']:
    require(code['term_id'] in terms,'TAXONOMY_TERM',5)
    for rid in code['evidence_ids']:require(record(db,rid)['paper_report_id']==p['paper_report_id'],'CODING_PAPER',5)
  if kind=='contradiction':
   for rid in p['claim_ids']:require(record(db,rid)['kind']=='claim','CONTRADICTION_CLAIM',5)
  if kind=='synthesis':
   inputs=[record(db,rid) for rid in p['input_ids']]
   require(sha(canonical([(r['record_id'],r['artifact_sha256']) for r in sorted(inputs,key=lambda r:r['record_id'])]).encode())==p['input_fingerprint'],'SYNTHESIS_FINGERPRINT',5)
   require(set(p['report_ids'])=={r['paper_report_id'] for r in inputs},'SYNTHESIS_REPORTS',5)
   for r in inputs:
    verified=False
    for v in db.execute("SELECT * FROM records WHERE kind='verification' AND current=1"):
     vp=json.loads(v['payload_json'])
     if vp.get('evidence_id')==r['record_id'] and vp.get('evidence_sha256')==r['artifact_sha256'] and vp.get('status')=='SUPPORTED' and trusted_receipt(db,v['artifact_sha256']):verified=True
    require(verified,'SYNTHESIS_UNVERIFIED',5)
   members=set()
   for rid in p['research_object_ids']:
    r=record(db,rid);o=json.loads(r['payload_json']);require(r['kind']=='research_object' and o['state']=='CONFIRMED','UNRESOLVED_OBJECT',5);members.update(o['members'])
   require(members==set(p['report_ids']),'OBJECT_COVERAGE',5)
   require(p['coverage']=='COMPLETE_ELIGIBLE_SCOPE','PARTIAL_POLICY_UNCONFIGURED',5)
  for key,expected in [('synthesis_ids','synthesis'),('gap_ids','gap_candidate')]:
   for rid in p.get(key,[]):require(record(db,rid)['kind']==expected,'TRACEABILITY_KIND',5)
 return p
