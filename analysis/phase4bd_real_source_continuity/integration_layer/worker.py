"""Fresh stdin-only PDF worker. Emits one development field, not validation."""
from pathlib import Path
import sys,json,hashlib,io,unicodedata
O=Path(__file__).resolve().parents[1];R=O.parents[1]
from runtime_guard import verify
deps=R/'analysis/phase4br_remediation/candidate_v4br/_deps'
verify(deps,json.loads((deps.parents[1]/'DEPENDENCY_MANIFEST.json').read_text())['files'])
sys.path.insert(0,str(deps))
import pypdfium2
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
header=json.loads(sys.stdin.buffer.readline())
assert set(header)=={'packet','source_sha256','report_id','source_size','context_id','stage','wrapper_sha256'}
packet=header['packet'].encode();body=json.loads(packet)
assert body['binding']['paper_id']==header['report_id'] and body['binding']['source_sha256']==header['source_sha256']
assert body['fork_history']=='none' and not body['coordinator_summary_included'] and not body['previous_holdout_scientific_content_included']
assert header['stage'] in ['EXTRACT','VERIFY']
assert header['wrapper_sha256']==hashlib.sha256((O/'integration_layer/worker_contract.json').read_bytes()).hexdigest()
sys.stdout.buffer.write(canonical({'context_id':header['context_id'],'packet_sha256':hashlib.sha256(packet).hexdigest(),'status':'ACKNOWLEDGED','fork_history':'none'})+b'\n');sys.stdout.buffer.flush()
source=sys.stdin.buffer.read(header['source_size']);assert len(source)==header['source_size'] and hashlib.sha256(source).hexdigest()==header['source_sha256']
doc=pypdfium2.PdfDocument(source);page=doc[0];tp=page.get_textpage()
text=unicodedata.normalize('NFC',tp.get_text_range());lines=[x for x in text.splitlines() if x.strip()];assert lines
value=lines[0];start=text.index(value)
tp.close();page.close();doc.close()
result={'report_id':header['report_id'],'source_sha256':header['source_sha256'],'field':'first_nonempty_text_line_on_pdf_page_1','value':value,'locator':{'type':'TEXT_SPAN','pdf_page':1,'text_artifact_sha256':hashlib.sha256(text.encode()).hexdigest(),'offset_convention':'Unicode code points in NFC extraction representation','start':start,'end':start+len(value)},'origin':'DIRECT_FROM_SOURCE','namespace':'DEVELOPMENT_TRANSPORT_ONLY','scientific_acceptance':False,'stage':header['stage']}
sys.stdout.buffer.write(canonical(result));sys.stdout.buffer.flush()
