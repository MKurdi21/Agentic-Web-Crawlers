"""Private derived representations of an already durably consumed current PDF."""
import sys,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parents[1];R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
import bridge as b
def extract(holdout):
 root=O/'private_worker_material'/holdout
 t=b.RealContinuity(root);t.chain(require_access=True)
 b.fail(t.e.state()['source_access_started'],'NO_CONSUMPTION')
 src=root/'source_delivery/current_source.pdf';b.fail(b.filehash(src)==t.entry['source_sha256'],'SNAPSHOT_HASH')
 receipts={r['atomic_unit_id']:r for _,r in t.e.receipts()}
 b.fail('MODEL_SOURCE_DELIVERY' in receipts,'NO_MODEL_DELIVERY_RECEIPT')
 delivery=b.read(t.e.root/'outputs/model_source_delivery.json')
 b.fail(delivery['source_sha256']==t.entry['source_sha256'] and delivery['consumption_sha256']==b.filehash(t.e.root/'outputs/consumption.json'),'MODEL_DELIVERY_LINK')
 b.runtime_integrity()
 import pypdfium2 as pdf
 out=root/'derived';out.mkdir(exist_ok=True);doc=pdf.PdfDocument(str(src));pages=[]
 for idx in range(len(doc)):
  page=doc[idx];tp=page.get_textpage();text=tp.get_text_range();raw=text.encode('utf-8');name=f'page_{idx+1:03}.txt';p=out/name
  if p.exists():b.fail(p.read_bytes()==raw,'TEXT_REPLAY_CONFLICT')
  else:b.exclusive(p,raw)
  image=out/f'page_{idx+1:03}.png'
  import io
  buffer=io.BytesIO();page.render(scale=1.5).to_pil().save(buffer,format='PNG');image_bytes=buffer.getvalue()
  if image.exists():b.fail(image.read_bytes()==image_bytes,'RENDER_REPLAY_CONFLICT')
  else:b.exclusive(image,image_bytes)
  pages.append({'page':idx+1,'text_path':str(p),'text_sha256':b.digest(raw),'image_path':str(image),'image_sha256':b.filehash(image)})
  tp.close();page.close()
 doc.close()
 manifest={'holdout_id':holdout,'source_sha256':t.entry['source_sha256'],'source_page_count':len(pages),'pages':pages,'classification':'NEVER_PACKAGE','text_is_derived_navigation_only':True}
 target=out/'SOURCE_REPRESENTATION_MANIFEST.json'
 if target.exists():b.fail(b.read(target)==manifest,'DERIVED_REPLAY_CONFLICT')
 else:b.exclusive(target,b.canonical(manifest))
 print(json.dumps({'holdout_id':holdout,'page_count':len(pages),'manifest_sha256':b.filehash(target)}))
if __name__=='__main__':extract(sys.argv[1])
