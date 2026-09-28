"""Durable, version-bound source access receipts. No scientific authority."""
import hashlib, json, os, re
from pathlib import Path
from datetime import datetime, timezone

class ReceiptFailure(ValueError): pass

def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def digest(b): return hashlib.sha256(b).hexdigest()
def stamp(): return datetime.now(timezone.utc).isoformat()
REQUIRED=('phase','holdout_id','paper_id','source_file_id','source_sha256','candidate_manifest_sha256','methodology_sha256','protocol_hashes','field_catalog_sha256','holdout_state','context_protocol_version')

def durable_new(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:
        f.write(canonical(obj));f.flush();os.fsync(f.fileno())
    # Reopening confirms bytes after the OS flush; this is not a power-loss guarantee.
    if path.read_bytes()!=canonical(obj):raise ReceiptFailure('RECEIPT_READBACK')

def commit_preaccess(directory,binding,*,allowed_reports):
    directory=Path(directory)
    if binding.get('holdout_id') not in allowed_reports:raise ReceiptFailure('RESERVED_REPORT_DENIED')
    if any(k not in binding or binding[k] in ('',None,{}) for k in REQUIRED):raise ReceiptFailure('INCOMPLETE_BINDING')
    for k in ('source_sha256','candidate_manifest_sha256','methodology_sha256','field_catalog_sha256'):
        if not re.fullmatch('[0-9a-f]{64}',binding[k]):raise ReceiptFailure('HASH_FORMAT')
    if any(not re.fullmatch('[0-9a-f]{64}',v) for v in binding['protocol_hashes'].values()):raise ReceiptFailure('PROTOCOL_HASH_FORMAT')
    if (directory/'SOURCE_ACCESS_BEGAN.json').exists():raise ReceiptFailure('SOURCE_ACCESS_PRECEDES_RECEIPT')
    record={**binding,'event':'PRE_ACCESS_RECEIPT_COMMITTED','sequence':1,'created_at':stamp(),'substantive_source_access_started':False}
    durable_new(directory/'PRE_ACCESS_RECEIPT.json',record)
    return record

def verify_order(receipt,event):
    if receipt.get('event')!='PRE_ACCESS_RECEIPT_COMMITTED' or receipt.get('substantive_source_access_started') is not False:raise ReceiptFailure('INVALID_PREACCESS_RECORD')
    if receipt.get('sequence')!=1 or event.get('sequence')!=2:raise ReceiptFailure('EVENT_ORDER')
    if event.get('event')!='SOURCE_ACCESS_BEGAN' or event.get('receipt_sha256')!=digest(canonical(receipt)):raise ReceiptFailure('EVENT_BINDING')
    if datetime.fromisoformat(receipt['created_at'])>datetime.fromisoformat(event['created_at']):raise ReceiptFailure('TIMESTAMP_ORDER')
    return True

def open_source(directory,source_path,current_binding,*,allowed_reports):
    directory=Path(directory)
    if current_binding.get('holdout_id') not in allowed_reports:raise ReceiptFailure('RESERVED_REPORT_DENIED')
    p=directory/'PRE_ACCESS_RECEIPT.json'
    if not p.is_file():raise ReceiptFailure('MISSING_DURABLE_RECEIPT')
    receipt=json.loads(p.read_bytes())
    if any(receipt.get(k)!=current_binding.get(k) for k in REQUIRED):raise ReceiptFailure('BINDING_MISMATCH')
    if receipt.get('sequence')!=1 or receipt.get('substantive_source_access_started') is not False:raise ReceiptFailure('INVALID_PREACCESS_RECORD')
    # Hash confirmation is metadata-only; return no bytes until access has a durable event.
    data=Path(source_path).read_bytes()
    if digest(data)!=receipt['source_sha256']:raise ReceiptFailure('SOURCE_HASH_MISMATCH')
    event={'event':'SOURCE_ACCESS_BEGAN','sequence':2,'created_at':stamp(),'receipt_sha256':digest(canonical(receipt)),'source_sha256':digest(data),'holdout_id':receipt['holdout_id']}
    verify_order(receipt,event);durable_new(directory/'SOURCE_ACCESS_BEGAN.json',event)
    return data
