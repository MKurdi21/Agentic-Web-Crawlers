from pathlib import Path
import csv,json,hashlib,zipfile,re,urllib.parse,collections,subprocess,datetime,ast
R=Path(__file__).resolve().parents[2];O=R/'analysis/workspace_audit'
def csvread(n):return list(csv.DictReader((R/n).open(encoding='utf-8-sig')))
def dumpcsv(n,rs):
    keys=list(dict.fromkeys(k for r in rs for k in r))
    with (O/n).open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rs)
def h(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rp(p):return p.relative_to(R).as_posix()
links=[]
for p in [R/'README.md',*sorted((R/'docs').glob('*.md')),R/'agentic_ai_web_agents_literature_search_report.md']:
    for ln,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
        for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',line):
            s=m.group(1).strip().strip('<>');s=urllib.parse.unquote(s.split('#')[0])
            if not s or re.match(r'^[a-zA-Z]+:',s):continue
            target=(p.parent/s).resolve();links.append({'file':rp(p),'line':ln,'target':s,'resolved_path':str(target),'exists':target.exists()})
dumpcsv('LINK_RECONCILIATION.csv',links)
pdfs=csvread('analysis/workspace_audit/CORPUS_INVENTORY.csv');by_path={r['path']:r for r in pdfs}
historical=csvread('docs/paper_inventory.csv');issues=[]
for i,r in enumerate(historical,2):
    p=r['current_path'].replace('\\','/');actual=by_path.get(p)
    if not actual or actual['sha256']!=r['sha256']:issues.append({'row':i,'type':'current_path_or_hash_mismatch','path':p})
    if r['exact_duplicate_of'] and not (R/r['exact_duplicate_of'].replace('\\','/')).exists():issues.append({'row':i,'type':'historical_duplicate_pointer','path':r['exact_duplicate_of']})
for i,r in enumerate(csvread('docs/near_duplicate_candidates.csv'),2):
    if not (R/r['original_path'].replace('\\','/')).exists():issues.append({'file':'docs/near_duplicate_candidates.csv','row':i,'type':'historical_near_duplicate_pointer','path':r['original_path']})
a=csvread('analysis/workspace_audit/ARTIFACT_INVENTORY.csv');seen={r['artifact_path'] for r in a}
for p in list((R/'analysis').glob('*'))+list(R.glob('*'))+list((R/'scripts').glob('*'))+list((R/'.agents').rglob('*')):
    if not p.is_file() or rp(p) in seen or p.suffix.lower() in ['.zip','.pdf']:continue
    t=p.read_text(encoding='utf-8-sig',errors='replace')
    a.append({'artifact_path':rp(p),'kind':'CONTROL_OR_DOCUMENTATION' if p.suffix not in ['.py','.ps1'] else 'SCRIPT','summary_name':'','source_pdf':'','mapping_status':'INTENTIONAL_NON_PAPER','mapping_confidence':'HIGH','size_bytes':p.stat().st_size,'sha256':h(p),'characters':len(t),'words':len(t.split()),'lines':len(t.splitlines()),'heading_count':len(re.findall(r'(?m)^#{1,6}\s',t)),'notes':'current input/control artifact; generation authority analyzed in reports'})
dumpcsv('ARTIFACT_INVENTORY.csv',a)
ref=[];schemas=[];syntax=[]
zpath=R/'Codex_Literature_Review_Production_Architecture.zip'
with zipfile.ZipFile(zpath) as z:
    for n in z.namelist():
        inf=z.getinfo(n);b=z.read(n) if not inf.is_dir() else b''
        ref.append({'reference_path':n,'is_directory':inf.is_dir(),'size_bytes':inf.file_size,'sha256':hashlib.sha256(b).hexdigest() if b else '', 'classification':'REFERENCE_TARGET_ARCHITECTURE','inspection':'MEMBER_INVENTORY' if inf.is_dir() or n.endswith('.gitkeep') else 'CONTENT_INSPECTED'})
        if n.endswith('.py'):
            ast.parse(b.decode('utf-8'));syntax.append(n)
        if '/schemas/' in n and n.endswith('.json'):
            d=json.loads(b);schemas.append({'path':n,'title':d['title'],'required':d.get('required',[]),'properties':list(d.get('properties',{}))})
dumpcsv('REFERENCE_PACKAGE_INVENTORY.csv',ref)
matrix=csvread('analysis/workspace_audit/PAPER_PROCESSING_MATRIX.csv');legacy={r['summary_name'] for r in matrix if r['legacy_summary']};v2={r['summary_name'] for r in matrix if r['v2_summary']}
result={'historical_inventory_rows':len(historical),'inventory_current_path_hash_mismatches':[i for i in issues if i['type']=='current_path_or_hash_mismatch'],'historical_pointer_issues':issues,'link_counts':{p:{'total':sum(x['file']==p for x in links),'missing':sum(x['file']==p and not x['exists'] for x in links)} for p in sorted(set(x['file'] for x in links))},'legacy_and_v2':sorted(legacy&v2),'legacy_only':sorted(legacy-v2),'v2_only':sorted(v2-legacy),'unprocessed':sorted(r['summary_name'] for r in matrix if r['newest_apparent_workflow_state']=='NO_PROCESSING_ARTIFACT_FOUND'),'reference_schemas':schemas,'reference_python_syntax_checked':syntax,'git_history':subprocess.run(['git','--no-optional-locks','log','-8','--format=%h %ad %s','--date=iso'],cwd=R,capture_output=True,text=True).stdout,'prompt_sha256':h(R/'analysis/PROMPT.md'),'git_lfs_config_present': 'filter=lfs' in (R/'.gitattributes').read_text() or 'lfs' in (R/'.git/config').read_text(),'manual_review_files':len(list((R/'98_Manual_Review').rglob('*'))),'pdf_identity_text_checks':len(pdfs),'reference_file_count':sum(not x['is_directory'] for x in ref)}
(O/'RECONCILIATION_DETAILS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['reference_schemas','unprocessed','legacy_only','v2_only','legacy_and_v2']},indent=2))
