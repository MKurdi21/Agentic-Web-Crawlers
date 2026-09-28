"""Metadata-only Phase 4BE-C checkpoint forensics. Never reads PDF content beyond SHA-256."""
import csv
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STATE = ROOT / 'analysis'
DRIFT = json.loads((STATE / 'checkpoint.json').read_text(encoding='utf-8'))
MANIFEST = list(csv.DictReader((STATE / 'manifest.csv').open(encoding='utf-8-sig', newline='')))
DIAG = json.loads((STATE / 'phase4be_freeze_repair_and_validation' / 'RECOVERY_LATEST_USAGE_BLOCKED_DIAGNOSTIC.json').read_text())

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def dump(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')

def classify(path):
    p = Path(path)
    parts = p.parts
    phase = next((x for x in parts if x.startswith('phase4')), None)
    if 'NEVER_PACKAGE' in parts:
        kind = 'phase4be_test_or_runtime_source_delivery_copy'
    elif 'private_source_material' in parts:
        kind = 'prior_phase_private_rehearsal_or_validation_copy'
    else:
        kind = 'other_operational_pdf'
    return kind, phase

def main():
    mapped = {Path(r['Pdf'].replace('\\','/')).as_posix() for r in MANIFEST}
    allpdf = sorted(ROOT.rglob('*.pdf'))
    registered_hashes = {r['source_sha256'] for r in DRIFT['papers'] if r['source_sha256']}
    holdouts = {x['holdout_id']: x['expected_sha256'] for x in json.loads((STATE/'phase4be_freeze_repair_and_validation'/'PHASE4BE_BASELINE.json').read_text())['source_hash_checks']}
    by_hash = defaultdict(list)
    for p in allpdf:
        by_hash[sha(p)].append(p.relative_to(ROOT).as_posix())
    issues = [x.removeprefix('Unmapped PDF: ') for x in DRIFT['issues'] if x.startswith('Unmapped PDF: ')]
    entries=[]
    for path in issues:
        p=ROOT/path
        digest=sha(p) if p.is_file() else None
        kind,phase=classify(path)
        matches=[k for k,v in holdouts.items() if v==digest]
        entries.append(dict(path=path,sha256=digest,size=p.stat().st_size if p.is_file() else None,
                            path_classification=kind,owning_phase=phase,
                            under_NEVER_PACKAGE='NEVER_PACKAGE' in p.parts,
                            under_private_source_material='private_source_material' in p.parts,
                            synthetic=('synthetic' in path.lower() or 'fixture' in path.lower()),
                            rehearsal_test_development_material=True,
                            matches_registered_corpus_source_hash=digest in registered_hashes,
                            matches_B02_B08_source_hashes=matches,
                            exact_copies=[x for x in by_hash[digest] if x!=path] if digest else [],
                            should_be_corpus_source=False))
    dump('UNMAPPED_PDF_FORENSIC_INVENTORY.json',entries)
    with (HERE/'UNMAPPED_PDF_FORENSIC_INVENTORY.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(entries[0]) if entries else ['path'])
        w.writeheader()
        for x in entries:
            w.writerow({k:json.dumps(v) if isinstance(v,list) else v for k,v in x.items()})
    paper_hashes={r['Pdf'].replace('\\','/'):r['source_sha256'] for r in DRIFT['papers']}
    source_checks=[dict(path=p,exists=(ROOT/p).is_file(),hash_matches=(sha(ROOT/p)==h if (ROOT/p).is_file() else False)) for p,h in paper_hashes.items()]
    duplicate_checks=[dict(**d,current_hash_matches=(ROOT/d['path']).is_file() and sha(ROOT/d['path'])==d['sha256']) for d in DRIFT['duplicates']]
    accounting=dict(tracked_paper_count=len(DRIFT['papers']),manifest_count=len(MANIFEST),status_sum=sum(DRIFT['counts'].values()),
                    status_counts=DRIFT['counts'],unmapped_pdf_count=len(issues),unmapped_operational_count=len(entries),
                    archived_duplicate_count=len(DRIFT['duplicates']),scanner_canonical_count=DRIFT['canonical_pdf_count'],
                    scanner_total_pdf_count=DRIFT['total_pdf_count'],live_physical_pdf_count=len(allpdf),
                    canonical_minus_tracked_equals_unmapped=DRIFT['canonical_pdf_count']-len(DRIFT['papers'])==len(entries),
                    total_equals_canonical_plus_duplicates=DRIFT['total_pdf_count']==DRIFT['canonical_pdf_count']+len(DRIFT['duplicates']),
                    all_unmapped_under_analysis=all(x['path'].startswith('analysis/') for x in entries),
                    all_tracked_sources_exist_and_match=all(x['exists'] and x['hash_matches'] for x in source_checks),
                    all_duplicate_hashes_match=all(x['current_hash_matches'] for x in duplicate_checks),
                    source_checks=source_checks,duplicate_checks=duplicate_checks,
                    unmapped_class_counts=dict(Counter(x['path_classification'] for x in entries)),
                    current_scanner_set_matches_drift=set(issues)=={p.relative_to(ROOT).as_posix() for p in allpdf if '99_Duplicates' not in p.relative_to(ROOT).parts}-mapped)
    dump('CORPUS_ACCOUNTING_RECONCILIATION.json',accounting)
    roots=sorted({Path(r['Pdf'].replace('\\','/')).parts[0] for r in MANIFEST})
    root_counts=dict(Counter(Path(r['Pdf'].replace('\\','/')).parts[0] for r in MANIFEST))
    dump('CORPUS_BOUNDARY_POLICY.json',dict(authorized_canonical_source_roots=roots,manifest_counts_by_root=root_counts,
         source_of_authority='analysis/manifest.csv, current 112 tracked source paths',
         duplicate_extra_root='99_Duplicates',duplicate_semantics='hash must match registered canonical source',
         excluded_operational_roots=['analysis','docs','scripts','.summary_v2','Summaries'],
         discovery_rule='only PDFs immediately or recursively within manifest-derived numbered source roots; 99_Duplicates separate'))
    bfiles=[]
    for p in allpdf:
        rel=p.relative_to(ROOT).as_posix()
        matches=re.findall(r'(?<![A-Za-z0-9])B0[2-8](?![A-Za-z0-9])',rel,re.I)
        if matches:
            h=sha(p)
            bfiles.append(dict(path=rel,sha256=h,size=p.stat().st_size,labels=sorted(set(x.upper() for x in matches)),
                               equals_frozen_holdout=[k for k,v in holdouts.items() if v==h],
                               path_context=classify(rel)[0]))
    event_path=STATE/'phase4be_freeze_repair_and_validation'/'RECOVERY_EVENTS.jsonl'
    events=[json.loads(x) for x in event_path.read_text().splitlines() if x.strip()]
    access=[dict(sequence=e.get('sequence'),event_type=e.get('event_type'),holdout=e.get('holdout_id'),source_access=e.get('source_access_started')) for e in events if 'SOURCE_ACCESS_BEGAN' in e.get('event_type','') or e.get('source_access_started') is True]
    states={k:'UNTOUCHED_CONFIRMED' if not access and DIAG['holdout_states'].get(k,'').startswith('UNTOUCHED') and not DIAG['scientific_source_access'] else 'UNRESOLVED' for k in holdouts}
    dump('B02_B08_ACCESS_AUDIT.json',dict(frozen_hashes=holdouts,b_looking_files=bfiles,
         durable_authority_event_count=len(events),source_access_events=access,
         diagnostic_holdout_states=DIAG['holdout_states'],diagnostic_scientific_source_access=DIAG['scientific_source_access'],
         diagnostic_stage_b=DIAG['actual_stage_b_started'],diagnostic_lane_b=DIAG['actual_lane_b_started'],
         states=states,limitation='Filesystem copies alone do not establish worker delivery; authority-event and diagnostic checks are the recorded evidence.'))
    print(json.dumps({k:accounting[k] for k in ('tracked_paper_count','unmapped_pdf_count','scanner_canonical_count','scanner_total_pdf_count','live_physical_pdf_count','all_tracked_sources_exist_and_match','current_scanner_set_matches_drift')}))
    print('roots',root_counts,'B-looking files',len(bfiles),'exact-holdout-byte copies',sum(bool(x['equals_frozen_holdout']) for x in bfiles))

if __name__=='__main__':
    main()
