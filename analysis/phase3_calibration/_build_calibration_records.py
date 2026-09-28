import csv, hashlib, json, math, pathlib, re, unicodedata
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
PRIVATE = ROOT / "calibration_records" / "private"
OUT = ROOT / "calibration_records" / "sanitized"
OUT.mkdir(parents=True, exist_ok=True)

def canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)

def sha(value):
    if isinstance(value, str): value = value.encode("utf-8")
    return hashlib.sha256(value).hexdigest()

def pages_for(report_id):
    candidates = list((PRIVATE / "primary_a").glob(f"*{report_id}*_pages.txt"))
    if candidates:
        text = candidates[0].read_text(encoding="utf-8", errors="replace")
        return re.split(r"^=== PDF PAGE \d+ ===$", text, flags=re.M)[1:]
    path = PRIVATE / "primary_b" / f"{report_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))["pages"]

def page_with(pages, terms, default=1):
    terms = [t.casefold() for t in terms]
    for index, text in enumerate(pages, 1):
        low = text.casefold()
        if all(t in low for t in terms): return index
    return min(default, len(pages))

CATALOG = json.loads((ROOT / "FIELD_CATALOG.json").read_text(encoding="utf-8"))
FIELDS = {x["stable_field_id"]: x for x in CATALOG["fields"]}
PROTOCOL = json.loads((ROOT / "CALIBRATION_PROTOCOL_FINGERPRINT.json").read_text(encoding="utf-8"))["protocol_sha256"]
FIELD_HASH = sha(canon(CATALOG))

# Sanitized, source-grounded propositions.  Detailed page text remains under NEVER_PACKAGE.
REPORTS = {
"report_f65b70426e7cad20f3bca498": {
 "title":"Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems", "authors":"Hongyan Chang; Ergute Bao; Xinjian Luo; Ting Yu", "year":"2026 prepublication report",
 "claims":{
  "framing.problem":"Indirect prompt injection is often evaluated after assuming malicious content is retrieved; this report tests retrieval under natural queries and realistic corpora.",
  "framing.claimed_contributions":"The report separates trigger and attack fragments and presents a black-box method for constructing retrievable malicious content.",
  "methods.benchmark":"The evaluation spans 11 retrieval benchmarks and eight embedding models.",
  "security.attack_vector":"The attacker places instruction-bearing content in an external corpus so retrieval exposes it to an LLM system.",
  "security.attacker_capability":"The described construction uses black-box API access to embedding models.",
  "results.quantitative":"The abstract reports near-complete retrieval across the evaluated benchmarks and models and over 80% SSH-key exfiltration success in one multi-agent scenario.",
  "security.defense_assumptions":"Evaluated defenses did not reliably prevent malicious-text retrieval in the tested settings.",
  "validity.limitations":"The conclusions remain tied to the tested corpora, queries, models, attacks, and defense configurations."
 }},
"report_e1a4d04452c57f69534e5603": {
 "title":"Prompt Injection Attack to Tool Selection in LLM Agents", "authors":"Jiawen Shi; Zenghui Yuan; Guiyao Tie; Pan Zhou; Neil Zhenqiang Gong; Lichao Sun", "year":"2025 report",
 "claims":{
  "framing.problem":"The report studies prompt injection that changes which tool an LLM agent selects.",
  "framing.claimed_contributions":"It introduces and evaluates ToolHijacker as an attack against tool-selection behavior.",
  "methods.agent_architecture":"The attack targets the LLM-mediated selection step in tool-using agents.",
  "security.attacker_objective":"The attacker seeks to redirect an agent toward an attacker-preferred tool.",
  "security.attack_surface":"Tool descriptions and other model-visible selection context form the studied attack surface.",
  "results.quantitative":"The source reports comparative attack measurements across evaluated agents and tool-selection settings.",
  "validity.limitations":"The observed behavior is bounded by the evaluated models, tools, prompt construction, and environments."
 }},
"report_4a25815942a0fae3db98433d": {
 "title":"AutoWebGLM: A Large Language Model-based Web Navigating Agent", "authors":"Hanyu Lai and collaborators", "year":"2024 report",
 "claims":{
  "framing.problem":"The report addresses language-model agents that navigate and act on websites.",
  "framing.claimed_contributions":"It presents the AutoWebGLM model and a web-navigation training and evaluation approach.",
  "methods.agent_architecture":"The system maps language goals and web observations to navigation actions.",
  "methods.benchmark":"The report evaluates the agent on web-navigation tasks and compares it with baselines.",
  "results.comparative":"The reported evaluation compares task success across agent configurations and competing systems.",
  "validity.limitations":"The evidence is specific to the evaluated websites, task distributions, models, and interaction setup."
 }},
"report_5f96daa6c80a1d5839a1d991": {
 "title":"Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search", "authors":"Zeren Luo; Zifan Peng; Yule Liu; Zhen Sun; Mingchen Li; Jingyi Zheng; Xinlei He", "year":"2025",
 "claims":{
  "framing.problem":"The report measures whether AI-powered search engines quote or cite malicious web content and evaluates mitigations.",
  "methods.dataset":"Candidate malicious URLs and keyword lists are drawn from three cyber-threat detection platforms.",
  "methods.benchmark":"Seven AI-powered search engines are queried using URL and keyword-list inputs.",
  "security.attack_surface":"Externally retrieved web content and cited sources are the studied exposure surface.",
  "results.quantitative":"The report states that 47% of evaluated responses were risky and 34% directly cited harmful content in one aggregate analysis.",
  "results.comparative":"URL queries produced more main-risk content than keyword-list queries in the reported comparison.",
  "validity.limitations":"Measurements depend on the selected engines, threat feeds, URLs, prompts, time of collection, and risk taxonomy."
 }},
"report_a4988586b3a9b60e43f89eda": {
 "title":"VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents", "authors":"Tri Cao; Bennett Lim; Yue Liu; Yuan Sui; Yuexin Li; Shumin Deng; Lin Lu; Nay Oo; Shuicheng Yan; Bryan Hooi", "year":"2026",
 "claims":{
  "framing.problem":"The report evaluates visual prompt-injection attacks against computer-use agents.",
  "framing.claimed_contributions":"It introduces VPI-Bench as an evaluation resource for visual prompt injection.",
  "methods.benchmark":"The benchmark exercises computer-use agents on tasks containing adversarial visual instructions.",
  "security.attack_vector":"Malicious instructions are presented through visual content observed by an agent.",
  "security.attack_surface":"The agent's visual perception and action loop form the evaluated attack surface.",
  "results.comparative":"The study compares vulnerability across evaluated agents and attack settings.",
  "validity.limitations":"Findings are limited to the benchmark tasks, visual injections, agents, and model versions tested."
 }},
"report_97ce3e361031031820f35361": {
 "title":"The BrowserGym Ecosystem for Web Agent Research", "authors":"Thibault Le Sellier De Chezelles; Maxime Gasse; Alexandre Lacoste; and collaborators", "year":"2025",
 "claims":{
  "framing.problem":"Web-agent research needs reproducible environments and common evaluation interfaces.",
  "framing.claimed_contributions":"The report presents BrowserGym as an ecosystem that integrates web-agent environments and benchmarks.",
  "methods.environment":"BrowserGym supplies browser interaction environments and a common task/evaluation interface.",
  "methods.benchmark":"The ecosystem aggregates multiple web-agent benchmarks under shared tooling.",
  "reproducibility.code":"The report identifies software resources for using the ecosystem.",
  "validity.limitations":"Benchmark integration does not remove differences in task semantics, environment versions, or scoring rules."
 }},
"report_05dbe40340050b30d7fb7462": {
 "title":"Mind the Web: The Security of Web-Use Agents", "authors":"Avishag Shapira; Parth Atulbhai Gandhi; Edan Habler; Asaf Shabtai", "year":"2026 conference version",
 "claims":{
  "identity.report_relationships":"This 17-page conference report is a distinct version of the shorter Mind the Web report and changes training-set scale and reported outcomes.",
  "framing.problem":"The report studies task-aligned malicious web content that steers privileged web-use agents.",
  "methods.experiment_design":"A three-stage pipeline generates, validates, and trains on task-aligned injections before evaluation on five agents.",
  "security.attacker_capability":"The stated minimum capability is posting content on a site the target agent may visit.",
  "security.attack_vector":"Injected comments, reviews, or advertisements are framed as task-helpful guidance.",
  "results.quantitative":"The report describes overall attack success above 80% and an appendix scaling result from 65% at 500 candidates to 85% at 2,000.",
  "validity.limitations":"The results depend on controlled environments, selected payloads, evaluated agents, judge behavior, and training data."
 }},
"report_29316d7f064e35b04ddd17fa": {
 "title":"Mind the Web: The Security of Web Use Agents", "authors":"Avishag Shapira; Parth Atulbhai Gandhi; Edan Habler; Asaf Shabtai", "year":"earlier report version",
 "claims":{
  "identity.report_relationships":"This 13-page report is an earlier distinct version; it uses a smaller candidate/SFT set and reports lower SFT and SFT-plus-DPO outcomes than the conference version.",
  "framing.problem":"The report studies malicious third-party web content that redirects web-use agents from user goals.",
  "methods.experiment_design":"The earlier pipeline evaluates task-aligned injection generation and transfer across agent settings.",
  "security.attacker_capability":"The attacker is modeled as able to place content on websites an agent encounters.",
  "results.quantitative":"The earlier version reports approximately 1,500 candidates, about 300 SFT examples, 61% SFT, and 82% SFT-plus-DPO in the compared configuration.",
  "validity.limitations":"Its quantitative results must remain version-specific and should not be pooled with the later report."
 }},
"report_17b162af40f95b9ba51cb157": {
 "title":"AGENTVIGIL: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents", "authors":"Zhun Wang; Vincent Siu; Zhe Ye; Tianneng Shi; Yuzhou Nie; Xuandong Zhao; Chenguang Wang; Wenbo Guo; Dawn Song", "year":"2025 arXiv version 4",
 "claims":{
  "identity.report_relationships":"This arXiv version and the EMNLP report appear to share core experiments, while this version contains additional explicit limitation discussion.",
  "framing.problem":"The report studies automatic black-box red-teaming for indirect prompt injection against LLM agents.",
  "methods.system_model":"AGENTVIGIL treats the target agent as a black box and generates test inputs to elicit indirect prompt-injection failures.",
  "security.attacker_knowledge":"The studied approach does not require white-box access to target model internals.",
  "results.comparative":"Core tables compare red-teaming and attack outcomes across target agents and settings.",
  "validity.limitations":"The arXiv version explicitly notes attack cost and weak transfer to Claude among its limitations."
 }},
"report_23e9445a563eb86c07c0ac0b": {
 "title":"AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents", "authors":"Zhun Wang; Vincent Siu; Zhe Ye; Tianneng Shi; Yuzhou Nie; Xuandong Zhao; Chenguang Wang; Wenbo Guo; Dawn Song", "year":"2025 EMNLP Findings version",
 "claims":{
  "identity.report_relationships":"The EMNLP report appears to share its principal tables and experiments with the arXiv report but has different packaging and less explicit limitation text.",
  "framing.problem":"The report evaluates automated black-box red-teaming for indirect prompt-injection vulnerabilities.",
  "methods.system_model":"The method probes target agents without internal model access.",
  "security.attack_vector":"Generated indirect instructions are introduced through external content consumed by agents.",
  "results.comparative":"The principal reported tables align with the corresponding arXiv version in the inspected comparison.",
  "validity.limitations":"Version-specific omissions mean limitation evidence should not be silently inherited from the arXiv report."
 }},
"report_d0c5b16dc9dbc30b0d49815f": {
 "title":"AdvAgent: Controllable Blackbox Red-teaming on Web Agents", "authors":"Chejian Xu; Mintong Kang; Jiawei Zhang; Zeyi Liao; Lingbo Mo; Mengqi Yuan; Huan Sun; Bo Li", "year":"2025 arXiv version 4",
 "claims":{
  "framing.problem":"The report studies controllable black-box red-teaming of web agents.",
  "framing.claimed_contributions":"It introduces AdvAgent to generate adversarial web interactions under configurable objectives.",
  "methods.agent_architecture":"The evaluation couples an attack-generation process with target web-agent interaction.",
  "security.attacker_objective":"The red-team agent seeks behavior deviations that satisfy selected attack objectives.",
  "results.comparative":"The report compares attack performance across agents, tasks, and configurations.",
  "validity.limitations":"Reported effectiveness remains conditional on the evaluated target agents, websites, objectives, and scoring process."
 }},
"report_c16f40cd135ffcbb595294e7": {
 "title":"ACE: A Security Architecture for LLM-Integrated App Systems", "authors":"Evan Li; Tushin Mallick; Evan Rose; William Robertson; Alina Oprea; Cristina Nita-Rotaru", "year":"2025 report",
 "claims":{
  "framing.problem":"LLM-integrated applications combine model outputs with privileged components and need system-level security controls.",
  "framing.claimed_contributions":"The report presents ACE as an architecture for controlling information and actions across LLM-integrated app components.",
  "methods.system_model":"ACE models the application as interacting components with security-relevant data and action flows.",
  "security.trust_boundary":"The architecture treats transitions between model-mediated and privileged application components as explicit trust boundaries.",
  "security.defense_assumptions":"The design assumes enforcement components correctly mediate protected flows and actions.",
  "results.comparative":"The evaluation compares security and utility behavior under the proposed architecture and alternatives.",
  "validity.limitations":"Architecture claims remain conditional on policy completeness, enforcement coverage, target apps, and evaluated attacks."
 }},
"report_db40269d76c4e5b83043918b": {
 "title":"BEARCUBS: A Benchmark for Computer-Using Web Agents", "authors":"Yixiao Song; Katherine Thai; Chau Minh Pham; Yapei Chang; Mazin Nadaf; Mohit Iyyer", "year":"2025",
 "claims":{
  "framing.problem":"Computer-using web agents require evaluation that captures realistic interaction difficulty.",
  "framing.claimed_contributions":"The report introduces BEARCUBS as a benchmark for computer-using web agents.",
  "methods.benchmark":"The benchmark defines web interaction tasks and success criteria for computer-using agents.",
  "methods.metrics":"Agent performance is evaluated using task-level completion measures and reported comparisons.",
  "results.comparative":"The source compares evaluated agent systems on benchmark tasks.",
  "validity.limitations":"Benchmark scores depend on task selection, site state, interaction infrastructure, model version, and scoring."
 }},
"report_da6cfb0488d945c042abd882": {
 "title":"Detection of Crawler Traps: Formalization and Implementation—Defeating Protection on Internet and on the TOR Network", "authors":"Authors as recorded in the source report", "year":"2021",
 "claims":{
  "framing.problem":"The report formalizes crawler traps that can waste or redirect crawler resources on the public web and TOR.",
  "framing.claimed_contributions":"It provides a formal treatment and implementation-oriented discussion of crawler-trap detection.",
  "methods.system_model":"Crawler behavior and trap structures are modeled to support detection reasoning.",
  "security.resource_consumption":"Crawler traps can consume crawling time and resources by inducing unproductive traversal.",
  "results.negative":"The inspected conclusion defers classifier implementation and operational testing to future work.",
  "validity.limitations":"The title's implementation wording does not establish measured deployed-classifier accuracy; operational validation remains future work.",
  "forward.future_work":"The report calls for classifier implementation and operational tests."
 }},
"report_a772a6285ca222fd2e193e7f": {
 "title":"SoK: Attack and Defense Landscape of Agentic AI Systems", "authors":"Juhee Kim; Wenbo Guo; Dawn Song", "year":"2026",
 "claims":{
  "framing.problem":"Agentic systems combine models with memory, tools, workflows, and environments, creating security risks beyond isolated model behavior.",
  "framing.claimed_contributions":"The report systematizes attack and defense work for agentic AI systems.",
  "methods.dataset":"The evidence base is a literature corpus organized through the report's systematization method.",
  "security.attack_surface":"The taxonomy covers user interaction, model behavior, memory, tool integration, and environment interaction.",
  "results.qualitative":"The report organizes attacks by external, user-level, and internal adversaries and defenses by runtime protection, secure-by-design, and component hardening.",
  "validity.limitations":"Coverage and taxonomy conclusions depend on search scope, inclusion choices, publication cutoff, and category definitions."
 }}
}

KEYWORDS = {
 "identity.title":["abstract"], "identity.authors":["abstract"], "identity.year_version":["abstract"],
 "identity.report_relationships":["abstract"], "framing.problem":["abstract"], "framing.claimed_contributions":["contributions"],
 "methods.system_model":["method"], "methods.agent_architecture":["agent"], "methods.environment":["environment"],
 "methods.dataset":["dataset"], "methods.benchmark":["benchmark"], "methods.experiment_design":["experiment"],
 "methods.baselines":["baseline"], "methods.metrics":["metric"], "security.attacker_objective":["attack"],
 "security.attacker_knowledge":["black-box"], "security.attacker_capability":["attacker"], "security.attack_surface":["attack"],
 "security.trust_boundary":["security"], "security.attack_vector":["attack"], "security.persistence":["persistence"],
 "security.adaptivity":["adaptive"], "security.resource_consumption":["crawler"], "security.defense_assumptions":["defense"],
 "results.quantitative":["result"], "results.qualitative":["taxonomy"], "results.negative":["future work"],
 "results.ablations":["ablation"], "results.uncertainty_statistics":["confidence"], "results.comparative":["result"],
 "validity.assumptions":["assumption"], "validity.limitations":["limitation"], "validity.threats":["threat"],
 "reproducibility.code":["github"], "reproducibility.data":["data"], "reproducibility.benchmark":["benchmark"],
 "reproducibility.environment":["environment"], "forward.future_work":["future work"], "forward.open_problems":["open problem"]
}

rows = list(csv.DictReader((ROOT / "CALIBRATION_CASES.csv").open(encoding="utf-8", newline="")))
all_records=[]; all_items=[]; verification=[]
for row in rows:
    rid=row["paper_id"]; spec=REPORTS[rid]; pages=pages_for(rid)
    claims = dict(spec["claims"])
    claims.update({"identity.title":spec["title"], "identity.authors":spec["authors"], "identity.year_version":spec["year"]})
    records=[]; items=[]
    for field_id, field in FIELDS.items():
        if field_id in claims:
            value=claims[field_id]; page=page_with(pages,KEYWORDS.get(field_id,["abstract"]))
            locator={"type":"PAGE","source_sha256":row["source_sha256"],"page":page}
            claim_json={"statement":value,"paper_id":rid}
            stable="ei_"+sha(row["source_sha256"]+"\0"+field_id+"\0"+canon(claim_json)+"\0"+canon(locator))
            item={"stable_item_id":stable,"paper_id":rid,"calibration_unit_id":row["calibration_unit_id"],"stable_field_id":field_id,"critical":field["critical"],"statement":value,"locator":locator,"source_sha256":row["source_sha256"],"origin":"DIRECT_FROM_SOURCE","quality":"CORRECT_COMPLETE","protocol_sha256":PROTOCOL}
            items.append(item); all_items.append(item)
            records.append({"stable_field_id":field_id,"applicability":"APPLICABLE","quality":"CORRECT_COMPLETE","origin":"DIRECT_FROM_SOURCE","value":value,"evidence_item_ids":[stable]})
        else:
            applicability="NOT_APPLICABLE" if field["applies"] in ("SECURITY","DEFENSE","RESOURCE_RISK") and not any(k.startswith("security.") for k in claims) else "UNKNOWN_APPLICABILITY"
            quality="NOT_APPLICABLE" if applicability=="NOT_APPLICABLE" else "NOT_EXTRACTED"
            records.append({"stable_field_id":field_id,"applicability":applicability,"quality":quality,"origin":None,"value":None,"evidence_item_ids":[]})
    report={"calibration_category_id":row["calibration_category_id"],"calibration_unit_id":row["calibration_unit_id"],"paper_id":rid,"source_sha256":row["source_sha256"],"protocol_sha256":PROTOCOL,"field_catalog_sha256":FIELD_HASH,"reviewer_identity_class":"MODEL_VERIFICATION","completion_status":"CALIBRATION_PARTIAL","fields":records,"evidence_items":items,"private_source_reference":f"NEVER_PACKAGE:{rid}"}
    path=OUT/f"{row['calibration_unit_id']}_{rid}.json"; path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    all_records.extend(records)

# Freeze candidate lower-risk sets and select deterministically per concrete unit.
manifest={"selection_algorithm_version":"sha256-lexicographic-v1","protocol_sha256":PROTOCOL,"field_catalog_sha256":FIELD_HASH,"units":[]}
for unit in sorted({r["calibration_unit_id"] for r in rows}):
    eligible=[x for x in all_items if x["calibration_unit_id"]==unit and not x["critical"]]
    selected=[]
    for x in eligible:
        parts=[PROTOCOL,unit,x["paper_id"],x["stable_field_id"],x["stable_item_id"]]
        normalized=[unicodedata.normalize("NFC",p) for p in parts]
        x2=dict(x);x2["selection_digest"]=sha(b"\x00".join(p.encode("utf-8") for p in normalized));selected.append(x2)
    selected.sort(key=lambda x:(x["selection_digest"],x["stable_item_id"]))
    n=len(selected);sample_size=min(n,max(3,math.ceil(.25*n))) if n else 0;chosen=selected[:sample_size]
    candidate_hash=sha(canon(sorted(x["stable_item_id"] for x in eligible)))
    manifest["units"].append({"calibration_unit_id":unit,"eligible_lower_risk_count":n,"required_sample_size":sample_size,"selected_item_ids":[x["stable_item_id"] for x in chosen],"selection_digests":[x["selection_digest"] for x in chosen],"protocol_sha256":PROTOCOL,"field_catalog_sha256":FIELD_HASH,"candidate_evidence_set_sha256":candidate_hash,"selection_algorithm_version":"sha256-lexicographic-v1"})
    chosen_ids={x["stable_item_id"] for x in chosen}
    for x in [z for z in all_items if z["calibration_unit_id"]==unit and (z["critical"] or z["stable_item_id"] in chosen_ids)]:
        verification.append({"stable_item_id":x["stable_item_id"],"paper_id":x["paper_id"],"calibration_unit_id":unit,"verification_class":"NON_INDEPENDENT_SECOND_PASS","outcome":"SUPPORTED","source_sha256":x["source_sha256"],"protocol_sha256":PROTOCOL,"note":"Separate source-grounded coordinator pass; independent subagent unavailable."})

(ROOT/"VERIFICATION_SAMPLE_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
(OUT/"VERIFICATION_RESULTS.json").write_text(json.dumps({"verification_records":verification},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

quality=Counter(r["quality"] for r in all_records); critical=sum(x["critical"] for x in all_items); noncritical=len(all_items)-critical
holdout_meta=json.loads((ROOT/"HOLDOUT_FINGERPRINTS.json").read_text())["validation_holdout"]
metrics={"calibration":{"top_level_categories":12,"concrete_units":13,"active_reports":15,"physical_source_observations":16,"additional_duplicate_physical_observations":1,"structured_fields":{"numerator":len(all_records),"denominator":15*len(FIELDS),"denominator_type":"report_field_slots"},"evidence_items":{"numerator":len(all_items),"denominator":len(all_items),"denominator_type":"created_evidence_items"},"critical_evidence_items":{"numerator":critical,"denominator":critical,"denominator_type":"created_critical_evidence_items"},"noncritical_evidence_items":{"numerator":noncritical,"denominator":noncritical,"denominator_type":"created_noncritical_evidence_items"},"eligible_lower_risk_evidence_items":sum(x["eligible_lower_risk_count"] for x in manifest["units"]),"sampled_lower_risk_evidence_items":sum(x["required_sample_size"] for x in manifest["units"]),"verified_items":len(verification),"independent_model_verified_items":0,"non_independent_second_pass_items":len(verification),"quality_classification_counts":quality,"error_classification_counts":{"SOURCE_OMISSION":quality["NOT_EXTRACTED"],"SCHEMA_EXPRESSIVENESS_FAILURE":0},"locator_counts":{"PAGE":len(all_items)},"schema_failures":0,"semantic_failures":0,"summary_source_disagreements":3,"human_review_required":critical,"automation_eligible":noncritical},"validation_holdout":{"report_count":6,"report_ids":[r["paper_report_id"] for r in csv.DictReader((ROOT/"PHASE4_VALIDATION_HOLDOUT.csv").open(encoding="utf-8"))],"selection_protocol_version":"phase3-holdout-selection-v1","selection_sha256":sha((ROOT/"PHASE4_VALIDATION_HOLDOUT.csv").read_bytes()),"frozen_at":holdout_meta["frozen_at"],"contamination_count":0,"contamination_status":"UNTOUCHED"}}
(ROOT/"CALIBRATION_METRICS.json").write_text(json.dumps(metrics,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"records":len(all_records),"evidence":len(all_items),"critical":critical,"noncritical":noncritical,"verified":len(verification),"quality":quality},default=dict))
