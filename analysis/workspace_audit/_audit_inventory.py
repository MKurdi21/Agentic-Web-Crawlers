from pathlib import Path
import csv, json, hashlib, re, collections, datetime, zipfile, difflib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/workspace_audit'
def rel(p): return p.relative_to(ROOT).as_posix()
def sha(p):
    if not p.is_file(): return None
    with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def readcsv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def writecsv(name,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def norm(s):return re.sub('[^a-z0-9]+',' ',s.lower()).strip()
def path(s):return ROOT/s.replace('\\','/')
manifest=readcsv(ROOT/'analysis/manifest.csv'); historical=readcsv(ROOT/'docs/paper_inventory.csv')
cp=json.loads((ROOT/'analysis/checkpoint.json').read_text(encoding='utf-8-sig'))
baseline=json.loads((ROOT/'analysis/baseline.json').read_text(encoding='utf-8-sig'))
reviews=json.loads((ROOT/'analysis/reviews.json').read_text(encoding='utf-8-sig'))
by_path={rel(path(r['Pdf'])):r for r in manifest}; by_name={r['SummaryName']:r for r in manifest}
checkpoint={r['SummaryName']:r for r in cp['papers']}
pdfs=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower()=='.pdf' and not p.is_relative_to(OUT))
rows=[]; excerpts={}; groups=collections.defaultdict(list)
for i,p in enumerate(pdfs,1):
    h=sha(p);m=by_path.get(rel(p),{}); meta={};text='';error='';pages=None
    try:
        reader=PdfReader(p);meta=dict(reader.metadata or {});pages=len(reader.pages);text=reader.pages[0].extract_text() or ''
    except Exception as e:error=str(e)
    mt=str(meta.get('/Title','')).strip();mt='' if mt.lower() in ['none','untitled',''] else mt
    lines=[s.strip() for s in text.splitlines() if s.strip()]
    fallback=p.stem.replace('_',' ')
    title=mt or fallback
    status='PDF_METADATA' if mt else 'FILENAME_WITH_FIRST_PAGE_AVAILABLE' if text else 'FILENAME_ONLY'
    # Preserve page text separately for analyst identity checking, not as a packaged artifact.
    excerpts[rel(p)]={'metadata':{k:str(v) for k,v in meta.items()},'first_page_lines':lines[:35],'error':error}
    cat='DUPLICATE_STORAGE' if '99_Duplicates' in p.parts else 'MANUAL_REVIEW' if '98_Manual_Review' in p.parts else 'ACTIVE_MANIFEST' if m else 'LEGACY_UNCLASSIFIED'
    row={'source_id':'sha256:'+h,'path':rel(p),'filename':p.name,'sha256':h,'size_bytes':p.stat().st_size,'collection':p.relative_to(ROOT).parts[0],'title':title,'title_evidence':status,'title_verified':bool(mt),'pdf_pages':pages,'canonical_status':cat,'duplicate_of':'','identical_paths':'','version_relation':'','manual_review':cat=='MANUAL_REVIEW','summary_name':m.get('SummaryName',''),'legacy_summary':rel(path(m['FinalTarget'])) if m and path(m['FinalTarget']).is_file() else '', 'v2_summary':rel(path(m['StageTarget'])) if m and path(m['StageTarget']).is_file() else '', 'evidence_workspace':rel(ROOT/'analysis/evidence'/Path(m['SummaryName']).stem) if m and (ROOT/'analysis/evidence'/Path(m['SummaryName']).stem).is_dir() else '', 'notes':error}
    rows.append(row);groups[h].append(row)
    print(f'PDF {i}/{len(pdfs)} {p.name}',flush=True)
for group in groups.values():
    canonical=next((r for r in group if r['canonical_status']=='ACTIVE_MANIFEST'),group[0])
    for r in group:
        r['identical_paths']=' | '.join(x['path'] for x in group if x is not r)
        if r is not canonical and len(group)>1:
            r['duplicate_of']=canonical['path'];r['summary_name']=canonical['summary_name']
            for k in ['legacy_summary','v2_summary','evidence_workspace']:r[k]=canonical[k]
        if len(group)>1:r['version_relation']='EXACT_DUPLICATE; probable renamed copy' if len(set(x['filename'] for x in group))>1 else 'EXACT_DUPLICATE'
near=[]
for i,a in enumerate(rows):
    for b in rows[i+1:]:
        if a['sha256']==b['sha256']:continue
        score=difflib.SequenceMatcher(None,norm(a['filename']),norm(b['filename'])).ratio()
        if score>=.87:
            near.append({'path_a':a['path'],'path_b':b['path'],'similarity':round(score,4),'classification':'UNRESOLVED_SIMILARITY','evidence':'filename similarity >=0.87; different SHA256'})
            if 'Mind_the_Web' in a['filename'] and 'Mind_the_Web' in b['filename']:
                for r in [a,b]:r['version_relation']='PROBABLE_ALTERNATE_VERSION; distinct source retained'
                near[-1]['classification']='PROBABLE_ALTERNATE_VERSION'
required=['Plain-Language Orientation','Document Roadmap','Background and Context','Research Problem and Gap','Research Questions','Assumptions / Threat Model','Methodology','Experiments / Analyses','Results','Figure-by-Figure','Table-by-Table','Diagram / Architecture','Equations and Mathematical','Interpretation and Discussion','Contributions and Novelty','Limitations','Threats to Validity','Future Work and Open Questions','Terminology and Notation Glossary','Key Numerical Results','Evidence Map','Very Simple Explanation']
def structure(p):
    if not p.is_file():return {'passed':False,'characters':0,'missing':[]}
    t=p.read_text(encoding='utf-8-sig');heads=[norm(s) for s in re.findall(r'(?m)^#{1,6}\s+(.+)$',t)];positions=[];missing=[]
    for i,title in enumerate(required,1):
        matches=[j for j,h in enumerate(heads) if re.match(rf'^{i}\s+',h) and norm(title) in h]
        if matches:positions.append(matches[0])
        else:missing.append(title)
    if not any('stage 0' in h for h in heads):missing.append('Stage 0')
    if not any('completeness audit' in h for h in heads):missing.append('Completeness Audit')
    return {'passed':not missing and positions==sorted(set(positions)) and len(t)>=20000,'characters':len(t),'missing':missing}
matrix=[];diffs=[];baseline_changes=[]
for row in rows:
    if row['canonical_status']=='DUPLICATE_STORAGE':continue
    m=by_path.get(row['path'],{});n=m.get('SummaryName','');st=path(m['StageTarget']) if m else OUT/'__missing';fin=path(m['FinalTarget']) if m else OUT/'__missing'
    sh=sha(st);fh=sha(fin);s=structure(st);c=checkpoint.get(n,{});rv=reviews.get(n,{})
    reviewed=bool(row['sha256'] and sh and s['passed'] and rv.get('source_sha256')==row['sha256'] and rv.get('draft_sha256')==sh and rv.get('prompt_sha256')==sha(ROOT/'analysis/PROMPT.md') and rv.get('reviewed_at') and rv.get('notes_path') and path(rv['notes_path']).is_file())
    status='promoted' if reviewed and sh==fh else 'source_verified' if reviewed else 'pending' if not sh else 'structural_pass' if s['passed'] else 'needs_repair'
    ev=ROOT/'analysis/evidence'/Path(n).stem; scratch=sorted(p for p in ROOT.glob('.summary_work_*') if n and p.name.startswith('.summary_work_'+Path(n).stem+'_'))
    run=json.loads((ev/'run.json').read_text(encoding='utf-8-sig')) if (ev/'run.json').is_file() else {}
    issues=[]
    for k,v in [('source_sha256',row['sha256']),('draft_sha256',sh),('final_sha256',fh),('status',status)]:
        if c.get(k)!=v:diffs.append({'summary_name':n,'field':k,'saved':c.get(k),'observed':v});issues.append('checkpoint '+k+' differs')
        if k!='status' and baseline['papers'].get(n,{}).get(k)!=v:baseline_changes.append({'summary_name':n,'field':k,'baseline':baseline['papers'].get(n,{}).get(k),'observed':v})
    matrix.append({'source_id':row['source_id'],'source_pdf':row['path'],'summary_name':n,'manifest_status':'MAPPED' if m else 'UNMAPPED','older_manifest_entry':n in {x['SummaryName'] for x in readcsv(ROOT/'.summary_manifest.csv')},'checkpoint_status':c.get('status','UNMAPPED'),'observed_status':status,'baseline_entry':n in baseline['papers'],'legacy_summary':row['legacy_summary'],'v2_summary':row['v2_summary'],'draft_characters':s['characters'],'structure_pass':s['passed'],'evidence_workspace':row['evidence_workspace'],'scratch_workspaces':' | '.join(rel(p) for p in scratch),'article_txt':(ev/'article.txt').is_file(),'accessibility_json':(ev/'accessibility.json').is_file(),'images_txt':(ev/'images.txt').is_file(),'page_png_count':len(list(ev.glob('*.png'))),'ledger':(ev/'ledger.md').is_file(),'run_json':(ev/'run.json').is_file(),'generation_log':(ev/'generation.log').is_file(),'review_notes':(ev/'review.md').is_file(),'review_state':'VALID_ATTESTATION' if reviewed else 'NO_ATTESTATION' if not rv else 'INVALID_ATTESTATION','run_status':run.get('status',''),'duplicate_state':row['version_relation'],'manual_review':row['manual_review'],'newest_apparent_workflow_state':'SOURCE_VERIFIED' if reviewed else 'DRAFT_WITH_PARTIAL_REVIEW' if (ev/'ledger.md').is_file() else 'UNREVIEWED_DRAFT' if sh else 'EXTRACTION_ONLY' if scratch or ev.is_dir() else 'LEGACY_ONLY' if fh else 'NO_PROCESSING_ARTIFACT_FOUND','mapping_confidence':'HIGH' if m else 'UNRESOLVED','issues':' | '.join(issues)})
artifacts=[]
roots=[ROOT/'Summaries',ROOT/'.summary_v2',ROOT/'analysis/evidence',*ROOT.glob('.summary_work_*'),ROOT/'docs']
for root in roots:
    for p in sorted(root.rglob('*')):
        if not p.is_file():continue
        kind='LEGACY_SUMMARY' if root.name=='Summaries' else 'CURRENT_SUMMARY' if root.name=='.summary_v2' else 'HISTORICAL_ANALYSIS' if root.name=='docs' else 'SCRATCH_EVIDENCE' if root.name.startswith('.summary_work') else 'DURABLE_EVIDENCE'
        n=p.name if kind.endswith('SUMMARY') else root.name[len('.summary_work_'):].rsplit('_',1)[0]+'.md' if kind=='SCRATCH_EVIDENCE' else p.relative_to(root).parts[0]+'.md' if kind=='DURABLE_EVIDENCE' else ''
        m=by_name.get(n,{});text=p.read_text(encoding='utf-8-sig',errors='replace') if p.suffix in ['.md','.txt','.json','.csv','.log'] else ''
        artifacts.append({'artifact_path':rel(p),'kind':kind,'summary_name':n,'source_pdf':m.get('Pdf','').replace('\\','/'),'mapping_status':'MAPPED' if m else 'INTENTIONAL_NON_PAPER' if kind=='HISTORICAL_ANALYSIS' else 'UNMAPPED','mapping_confidence':'HIGH' if m else 'UNRESOLVED' if kind!='HISTORICAL_ANALYSIS' else 'HIGH','size_bytes':p.stat().st_size,'sha256':sha(p),'characters':len(text),'words':len(text.split()),'lines':len(text.splitlines()),'heading_count':len(re.findall(r'(?m)^#{1,6}\s',text)),'notes':'observed bytes; not proof of generation provenance'})
top=[]
for p in sorted(ROOT.iterdir()):
    if p.name=='analysis':role='ANALYSIS'
    elif p.name=='Codex_Literature_Review_Production_Architecture.zip':role='REFERENCE_TARGET_ARCHITECTURE'
    elif p.name=='.git':role='CONTROL_STATE'
    elif p.name=='.agents':role='CODEX_SKILL'
    elif p.name=='AGENTS.md':role='CODEX_INSTRUCTION'
    elif p.name.startswith('99_'):role='DUPLICATE_STORAGE'
    elif p.name.startswith('98_'):role='MANUAL_REVIEW'
    elif re.match(r'^\d\d_',p.name):role='SOURCE_CORPUS'
    elif p.name=='Summaries':role='LEGACY_SUMMARY'
    elif p.name=='.summary_v2':role='CURRENT_SUMMARY'
    elif p.name.startswith('.summary_work'):role='WORKING_CACHE'
    elif p.name in ['New','Security','Borderline']:role='HISTORICAL_ARTIFACT'
    elif p.name=='scripts' or p.suffix in ['.py','.ps1']:role='SCRIPT'
    elif p.name=='.summary_manifest.csv' or p.name=='.gitattributes':role='CONTROL_STATE'
    elif p.name=='docs' or p.suffix=='.md':role='DOCUMENTATION'
    else:role='UNKNOWN'
    top.append({'path':p.name,'item_type':'directory' if p.is_dir() else 'file','classification':role,'direct_entries':len(list(p.iterdir())) if p.is_dir() else '', 'notes':'reference input excluded from current implementation' if role=='REFERENCE_TARGET_ARCHITECTURE' else ''})
writecsv('CORPUS_INVENTORY.csv',rows);writecsv('PAPER_PROCESSING_MATRIX.csv',matrix);writecsv('ARTIFACT_INVENTORY.csv',artifacts);writecsv('TOP_LEVEL_INVENTORY.csv',top)
(OUT/'_pdf_identity_excerpts.json').write_text(json.dumps(excerpts,indent=2,ensure_ascii=False),encoding='utf-8')
stats={'pdfs':len(rows),'unique_pdf_hashes':len(groups),'active_canonical':len(matrix),'duplicate_copies':sum(len(v)-1 for v in groups.values()),'duplicate_groups':[[r['path'] for r in v] for v in groups.values() if len(v)>1],'near_candidates':near,'statuses':dict(collections.Counter(r['observed_status'] for r in matrix)),'frontier':dict(collections.Counter(r['newest_apparent_workflow_state'] for r in matrix)),'checkpoint_differences':diffs,'baseline_changes':baseline_changes,'review_count':len(reviews),'legacy_count':sum(r['kind']=='LEGACY_SUMMARY' for r in artifacts),'v2_count':sum(r['kind']=='CURRENT_SUMMARY' for r in artifacts),'evidence_runs':len([p for p in (ROOT/'analysis/evidence').iterdir() if p.is_dir()]),'scratch_dirs':len(list(ROOT.glob('.summary_work_*'))),'unmapped_artifacts':[r['artifact_path'] for r in artifacts if r['mapping_status']=='UNMAPPED'],'title_metadata_count':sum(r['title_evidence']=='PDF_METADATA' for r in rows),'title_errors':[r['path'] for r in rows if r['notes']]}
(OUT/'AUDIT_MEASUREMENTS.json').write_text(json.dumps(stats,indent=2),encoding='utf-8');print(json.dumps(stats,indent=2))
