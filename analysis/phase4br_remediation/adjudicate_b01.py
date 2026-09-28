"""B01-only development adjudication. Exact excerpts stay in NEVER_PACKAGE storage."""
import json,re,hashlib,csv,collections
from pathlib import Path
O=Path(__file__).resolve().parent
P=O/'private_source_material'; OLD=P/'original_phase4b/holdout_validation/B01/private'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
parts=re.split(r'=+ PDF PAGE (\d+) =+', (OLD/'extracted_pages.txt').read_text(encoding='utf-8'))
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
challenges=read(P/'challenges.json')

# Hand-authored atomic development assertions. Each tuple binds a paraphrase to a
# source page and a precise section/table/paragraph reference, never verifier votes.
D={
1:[('Untrusted tool-return data carry indirect instructions.',1,'Abstract'),('Slack tasks include web and file access.',5,'Task suites: Slack'),('Injection success varies with relative position.',21,'Figure 21a caption and bars')],
3:[('The baseline directs the malicious task before the user task.',7,'Section 4.1 Important message paragraph'),('The attack impersonates the user and addresses the model.',8,'Section 4.2 opening paragraph')],
7:[('The report identifies the NeurIPS 2024 venue.',1,'Venue footer'),('The dataset card identifies version v1.0.',24,'F.3.2 Version details'),('The dataset card dates release and last update to June 2024.',24,'F.3.2 Version details')],
10:[('Document-wide absence of formal hypotheses remains unproven by the original single-page locator.',1,'Abstract; insufficient for document-wide absence')],
16:[('Table 2 varies knowledge of user and model names.',8,'Table 2 caption and rows'),('Table 4 compares attack phrasings.',20,'Table 4 caption and columns'),('Table 5 compares defense configurations.',20,'Table 5 caption and columns'),('Figure 21 examines injection position.',21,'Figure 21a')],
17:[('The agent receives a user task.',3,'Section 3 user task definition'),('Tools read or mutate application state.',4,'Tools paragraph'),('Tool documentation is included in agent prompts.',4,'Tools paragraph'),('The runtime formats tool outputs as YAML.',4,'Tools paragraph')],
21:[('Attacker tasks include exfiltration of authentication information.',5,'Task suites paragraph on sensitive information'),('Attacker tasks include phishing, expensive reservations and money transfers.',6,'Table 1 injection-task examples'),('Untargeted attacks aim to prevent user task completion.',20,'Appendix D Untargeted attacks')],
22:[('Agents expose a query interface.',5,'Section 3.2 query function'),('Modular pipelines combine components.',5,'Section 3.2 pipeline description'),('Most tested agents use provider function calling.',7,'Opening continuation of Section 4'),('Llama 3 uses an additional tool-calling prompt.',7,'Opening continuation of Section 4')],
25:[('The framework supports extensible stateful evaluations.',3,'Section 3 framework definitions'),('The initial benchmark has four task suites.',5,'Task suites'),('Table 1 lists 97 user tasks and 27 injection targets.',6,'Table 1 caption and rows'),('The study reports 629 security test cases.',7,'Section 4 evaluation paragraph'),('The framework defines utility and security checks.',3,'Section 3 formal evaluation criteria')],
28:[('Utility and security are defined through environment-state checks.',3,'Section 3 formal evaluation criteria'),('User tasks expose a reference sequence of tool calls.',4,'User tasks paragraph'),('Injection tasks specify attacker goals and reference call sequences.',5,'Injection tasks paragraph'),('Some environment content is designated as injection placeholders.',3,'Section 3 environment definition')],
32:[('Max combines success across candidate attack phrasings per task.',8,'Section 4.2 Max definition'),('The paper describes the aggregate as modeling adaptive attack choice.',6,'Section 3.4 final paragraph'),('Future adaptive attacks are proposed.',6,'Section 3.3 dynamic framework paragraph')],
35:[('The prose reports zero success for Travel injection task 6.',7,'Section 4.1 final paragraph; Figure 7 is on page 8')],
36:[('The six stored author identities, including Florian Tramèr, match the title page.',1,'Author block')],
39:[('Environment state is populated with dummy data.',4,'Opening paragraph'),('Success criteria inspect environment state.',3,'Section 3 formal evaluation criteria'),('The tested attacks and defenses are described as generic.',2,'Introduction evaluation discussion')],
42:[('The evaluation covers ten listed agent models.',6,'Section 4 model roster continued on page 7'),('Agents are evaluated on 97 tasks and 629 security cases.',7,'Section 4 evaluation paragraph'),('Additional attack and defense studies focus on GPT-4o.',7,'Section 4 evaluation paragraph'),('Attacker-knowledge and phrasing ablations are reported.',8,'Section 4.2'),('Position effects are reported separately.',21,'Figure 21')],
43:[('The report introduces AgentDojo.',1,'Title and abstract'),('The report links a benchmark implementation.',2,'Code and website links'),('The supplement describes associated code and data.',22,'E.1 and E.3')],
44:[('Benign utility measures success without attacks.',6,'Section 3.4 Benign Utility'),('Utility under attack requires task success without adversarial side effects.',6,'Section 3.4 Utility Under Attack'),('Targeted ASR measures attacker-goal success over security cases.',6,'Section 3.4 Targeted Attack Success Rate'),('Appendix tables report 95 percent intervals.',20,'Tables 3-5 captions')],
46:[('The proposed attacker may know user and model names.',6,'Section 3.3 prior knowledge paragraph'),('Table 2 tests correct and incorrect name guesses.',8,'Table 2')],
48:[('Attacker text fills designated tool-output placeholders.',16,'Appendix A attack construction'),('Controlled output fraction varies by suite.',21,'Figure 21b')],
49:[('The paper reports a tendency for higher-utility models to be easier to target.',7,'Section 4.1 inverse scaling discussion'),('Later injection positions were more effective in the reported experiment.',21,'Figure 21a'),('Tool filtering reduces reported targeted ASR.',9,'Tool isolation discussion'),('Tool filtering has stated planning and shared-tool limitations.',9,'Tool isolation limitations paragraph')],
50:[('Tool filtering selects tools before untrusted data are read.',9,'Opening continuation of Section 4.3'),('Unpredictable future tool needs can defeat advance planning.',9,'This defense fails paragraph'),('Necessary tools are also sufficient for attacks in a reported 17 percent of cases.',9,'This defense fails paragraph'),('Persistent context across tasks is a hypothetical uncovered failure setting.',9,'Multiple tasks without resetting context paragraph')],
55:[('The study names ten tested agent models.',6,'Section 4 model roster continued on page 7'),('Attack variants include four phrasings and a Max aggregate.',8,'Section 4.2 attack enumeration'),('Defense variants include delimiters, detection, repeated prompts and tool filtering.',8,'Section 4.3 defense enumeration')],
57:[('Tasks use explicit utility and security criteria.',3,'Section 3 evaluation definitions'),('Reference tool-call sequences are supplied for user tasks.',4,'User tasks paragraph'),('Reference tool-call sequences are supplied for injection tasks.',5,'Injection tasks paragraph'),('The supplement claims documentation and example notebooks.',22,'E.3 Reproducibility')],
59:[('The checklist names statsmodels proportion_confint for intervals.',15,'Checklist 3c'),('Tables 3-5 display 95 percent intervals.',20,'Tables 3-5 captions and values')],
60:[('The paper links a GitHub implementation.',2,'Code link'),('The supplement says code was attached at submission.',22,'E.1'),('The stated license is MIT with marked exceptions.',22,'E.1 license statement')],
62:[('The benchmark defines four mutable simulated environments.',3,'Section 3.1 environments'),('Dummy state was generated manually or with models and inspected.',4,'Opening paragraph'),('The suites cover workspace, messaging/web access, travel and banking.',5,'Task suite enumeration')],
65:[('The evaluation addresses agent utility and attack/defense effectiveness.',2,'Introduction'),('Experiments vary models and suites.',7,'Section 4.1'),('Experiments vary attacker knowledge.',8,'Table 2'),('Experiments vary injection position.',21,'Figure 21a')],
66:[('The supplement states that model conversations and outputs are released as JSON.',22,'E.3'),('A separate output archive is linked.',22,'E.3'),('Environment data are synthetic.',4,'Opening paragraph'),('A dataset card describes the release.',24,'F.3')],
67:[('The paper describes present attacks and defenses as relatively simple.',9,'Section 5 item i'),('Task and utility criteria are manually specified.',9,'Section 5 item ii'),('Multimodal tasks are proposed as future work.',10,'Section 5 item iv'),('Injection constraints are proposed as future work.',10,'Section 5 item v'),('Tool filtering has planning limitations.',9,'Tool isolation limitations paragraph')],
70:[('Synthetic state and manually designed tasks motivate an analyst external-validity caution.',4,'Opening paragraph; analyst inference'),('The tool total differs across report locations.',6,'Table 1 caption versus row sum; also page 4 prose'),('Attack values must retain experiment-specific provenance.',20,'Tables 3-5; analyst synthesis caution')],
72:[('The paper identifies model families and provider APIs.',7,'Section 4 opening continuation'),('Supplemental prompts are shown.',17,'Figures 14-16; continued page 18'),('The runtime emits YAML tool outputs.',4,'Tools paragraph'),('The supplement claims a dependency requirements file.',22,'E.3')],
74:[('The benchmark reports 97 user tasks.',6,'Table 1 user column'),('The benchmark reports 27 injection targets.',6,'Table 1 injection column'),('The study evaluates 629 security cases.',7,'Section 4 evaluation paragraph'),('The dataset card lists 124 tasks.',24,'F.3 dataset snapshot'),('The dataset card lists 136 KB of environment data.',24,'F.3 dataset snapshot')],
75:[('User tasks can require up to 18 tool calls.',5,'Task suites paragraph'),('Injection tasks can require up to 20 steps.',5,'Task suites paragraph'),('The reported GPT-4o security-suite cost is approximately 35 US dollars.',20,'Appendix D API cost paragraph'),('The reported benign-suite cost is approximately 4 US dollars.',20,'Appendix D API cost paragraph')],
77:[('Travel injection task 6 is reported with zero success.',7,'Section 4.1 final paragraph'),('Some tasks fail without attacks.',7,'Section 4.1 benign utility discussion'),('Detector false positives reduce utility.',9,'Section 4.3 detector discussion'),('Tool filtering has documented failure settings.',9,'Tool isolation limitations paragraph')],
80:[('The dataset card supplies a Zenodo dataset DOI.',23,'F.1 Links: DOI'),('The code repository is linked.',23,'F.1 Links: Repository'),('The project website is linked.',1,'Project website line')],
}
notes={
7:'PDF creation time is an artifact-metadata observation, not page-1 scientific evidence. It is preserved separately and excluded from the source-claim graph.',
10:'A single page and keyword absence cannot establish report-wide absence. Retain unresolved; do not assert that no hypothesis exists.',
32:'Retain the author adaptive-aggregate terminology; do not reinterpret it as a demonstrated online feedback attack.',
35:'The prose entails zero; the Figure 7 page attribution is wrong. Correct the support to page-7 prose and page-8 figure.',
36:'UTF-8 decoding and rendered title-page inspection confirm U+00E8 in the stored name. The verifier mojibake allegation is not a source error.',
43:'Separate introduction/code facts from an unresolved companion-report absence and analyst link-access provenance. Do not infer an approved research object.',
46:'Narrow to explicitly described name-knowledge experiments. Broad information-availability absence remains unproven.',
59:'Preserve interval evidence. Leave document-wide absence of seed distributions or significance tests unresolved.',
60:'External-link noninspection is workflow provenance, not a source-backed paper claim.',
65:'These are analyst-derived questions, not verbatim author RQs; label inference and retain supporting evaluation locations.',
66:'External archive availability was not checked. Preserve the paper claim of release separately from actual availability.',
70:'Label validity assessment as analyst inference. Different-table attack rates do not alone prove a same-condition contradiction.',
72:'Actual external runtime dependency versions remain unknown; no links were followed.',
80:'Bind the DOI to the dataset card, not automatically to the scientific article.'}
partial={43,46,59,70,80}
D[1].append(('Workspace tasks include email, calendar and cloud-drive data.',5,'Task suites: Workspace'))
D[17].append(('The benchmark defines four simulated environments.',3,'Section 3.1 environments'))
D[25].append(('The paper evaluates initial attacks and defenses.',1,'Abstract'))
D[39].append(('The dummy state is intended to reflect possible initial application state.',4,'Opening paragraph'))
D[67].append(('The persistent multi-task setting is not covered by the current benchmark.',9,'Tool isolation limitations paragraph'))
D[70].append(('The limited fixed attack collection motivates an analyst caution about adaptive risk.',6,'Section 3.3; analyst inference'))
D[74].extend([('The benchmark defines four environments.',3,'Section 3.1 environments'),('Environment data are synthetic.',4,'Opening paragraph')])
out=[];private=[]
for x in challenges:
    n=int(x['challenge_id'][2:]);a=x['primary'];c=a['claim'];numeric=a['stable_field_id']=='results.quantitative'
    if numeric:
        benign=c['metric']=='benign utility';table=3 if c['result_id'].startswith('r_t3') else 5
        cond=('absence of attacks; 97 user tasks' if benign else ('Important message baseline; 629 security cases' if table==3 else 'GPT-4o defense experiment against the stated strongest attack; security-case denominator'))
        atoms=[(f"{c['subject']} has reported {c['metric']} {c['value']} percent in Table {table}.",20,a['locator']['note']),
               (f"The metric is {c['metric']} and its unit is percent.",6,'Section 3.4 metric definition'),
               (f"The measurement condition is {cond}.",6 if benign else 7 if table==3 else 8,'Section 3.4' if benign else 'Section 4.1' if table==3 else 'Section 4.3'),
               (f"The value is local to Table {table}, not a cross-experiment global comparison.",20,f'Table {table} caption and headers')]
        category='BOTH_PARTIAL' if benign else 'LOCATOR_ONLY_DEFECT';claim='CLAIM_PARTIAL' if benign else 'CLAIM_CORRECT';loc='LOCATOR_PARTIALLY_SUPPORTS'
        roots=['CONDITION_UNSUPPORTED','CONDITION_DENOMINATOR_CONFLATION'] if benign else ['COMPOUND_SUPPORT_SET_MISSING','CAPTION_CONTEXT_MISSING']
        reason='Correct cell value; benign utility cannot inherit an attack condition or security-case denominator.' if benign else 'Cell value matches rendered table; metric and experimental condition require separate source locations.'
        fixture='F04' if benign else 'F03'
        paraphrase=f"Table {table} measurement for {c['subject']}: {c['metric']}, including its condition and denominator."
    else:
        atoms=D[n];category='LOCATOR_ONLY_DEFECT';claim='CLAIM_CORRECT';loc='LOCATOR_COMPOUND_INCOMPLETE'
        roots=['MULTIPLE_PROPOSITIONS_ONE_LOCATOR','COMPOUND_SUPPORT_SET_MISSING'];fixture='F01'
        reason=notes.get(n,'The source supports the bounded components across the listed locations; the original locator covers only part of the material proposition set.')
        paraphrase=' / '.join(t[0] for t in atoms)
        if n in partial:category='BOTH_PARTIAL';claim='CLAIM_PARTIAL';roots+=['CLAIM_OVERGENERALIZATION'];fixture='F05'
        if n==10:category='UNRESOLVED';claim='CLAIM_UNRESOLVED';loc='LOCATOR_UNRESOLVED';roots=['ABSENCE_NOT_ESTABLISHED'];fixture='F06'
        if n==36:category='PRIMARY_CORRECT';loc='LOCATOR_FULLY_SUPPORTS';roots=['VERIFIER_ENCODING_ERROR'];fixture='F07'
        if n==35:loc='LOCATOR_PARTIALLY_SUPPORTS';roots=['LOCATOR_WRONG_PAGE'];fixture='F08'
        if n==70:fixture='F09'
        if n in (60,66,72):roots+=['SOURCE_VS_PROCESS_PROVENANCE']
    pid=[x['challenge_id']+'_P'+str(i+1) for i in range(len(atoms))]
    row={'challenge_id':x['challenge_id'],'paper_report_id':a['paper_id'],'evidence_item_id':a['stable_item_id'],'field_id':a['stable_field_id'],
      'proposition_ids':pid,'primary_claim_paraphrase':paraphrase,'primary_support_locators':[a['locator']],
      'original_support_decision':a['primary_support_status'],'verifier_finding':x['verifier']['source_bound_finding'],'verifier_proposed_support_status':x['verifier']['verdict'],
      'claim_correctness':claim,'locator_correctness':loc,'challenge_disposition':category,
      'comparison_scope_correctness':'LOCAL_MEASUREMENT_ONLY' if numeric else 'NOT_A_RANKING_CLAIM; interpretation qualified where noted',
      'proposition_decomposition_correctness':'DECOMPOSED_IN_REMEDIATION' if len(atoms)>1 else 'SINGLE_PROPOSITION',
      'root_causes':roots,'severity':'CRITICAL_SUPPORT_GATE' if n!=36 else 'VERIFIER_FALSE_FLAG',
      'source_adjudication_rationale':reason,'source_evidence':[{'page':p,'reference':r,'page_text_sha256':sha(pages[p].encode('utf-8'))} for _,p,r in atoms],
      'private_exact_evidence_path':f'private_source_material/adjudication/{x["challenge_id"]}.json',
      'revised_rule':'Require proposition-specific roles and complete source-bound support sets; keep unknowns and analyst interpretation distinct.',
      'remediation_fixture_id':fixture,'development_rerun_result':'PENDING','review_mode':'MODEL_SOURCE_REVIEW','ground_truth_critical_false_accepts':'UNKNOWN'}
    # Full page bytes and exact original claims remain private, with specific source references above.
    prv={'original':x,'adjudication':row,'revised_atoms':[{'proposition_id':p,'text':t,'page':pg,'reference':ref} for p,(t,pg,ref) in zip(pid,atoms)],
      'exact_source_pages':{str(pg):pages[pg] for _,pg,_ in atoms}}
    write(P/'adjudication'/f'{x["challenge_id"]}.json',prv)
    row['private_exact_evidence_sha256']=sha((P/'adjudication'/f'{x["challenge_id"]}.json').read_bytes());out.append(row);private.append(prv)
write(O/'B01_SUPPORT_ADJUDICATION.json',{'scope':'B01 DEVELOPMENT_REMEDIATION_DATA','source_sha256':challenges[0]['primary']['source_sha256'],'adjudications':out,'distribution':dict(collections.Counter(x['challenge_disposition'] for x in out))})
write(P/'adjudication_atoms.json',private)
def csv_write():
    with (O/'B01_SUPPORT_ADJUDICATION_MATRIX.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader()
        for r in out:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
csv_write()
print(json.dumps({'count':len(out),'distribution':dict(collections.Counter(x['challenge_disposition'] for x in out))}))
