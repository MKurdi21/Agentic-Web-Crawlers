"""Immutable input and context-packet preflight; not an OS access sandbox."""
import hashlib,json
from pathlib import Path
MUTABLE={'shadow','outbox','test_runtime','test_results','__pycache__','_deps','cache','backups','logs'}
def digest(b):return hashlib.sha256(b).hexdigest()
def manifest(root):
    root=Path(root);rows=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(root)
        if any(x in MUTABLE for x in rel.parts):continue
        if p.suffix in ('.pyc','.tmp','.log'):continue
        rows.append({'relative_path':rel.as_posix(),'size_bytes':p.stat().st_size,'sha256':digest(p.read_bytes())})
    return rows
def verify_manifest(root,frozen):
    actual=manifest(root)
    if actual!=frozen:raise ValueError('METHODOLOGY_DRIFT')
    return True
def verify_packet(packet,*,current_report,frozen_protocol_hash,allowed_input_hashes):
    if packet['report_id']!=current_report:raise ValueError('CONTEXT_REPORT')
    if packet['frozen_protocol_hash']!=frozen_protocol_hash:raise ValueError('CONTEXT_PROTOCOL')
    if packet['fork_history']!='none' or packet['previous_holdout_scientific_content_included'] or packet['coordinator_summary_included']:raise ValueError('VALIDATION_CONTEXT_CONTAMINATION')
    if set(packet['input_hashes'])-set(allowed_input_hashes):raise ValueError('CONTEXT_INPUT_OUTSIDE_ALLOWLIST')
    return True
