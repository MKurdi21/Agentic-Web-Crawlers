# Research catalog

Current working question: How can adversarial web environments induce and sustain task-dependent navigation traps in autonomous AI web agents, and what determines whether agents escape, recover, or continue unproductive interaction?

All 112 canonical entries below are retained. Source paths, methods and per-paper relevance analyses preserve the completed records, including their earlier comparison-oriented interpretation; those entries do not individually define current priorities. Use the [trap roadmap](synthesis/AI_WEB_AGENT_TRAP_RESEARCH_ROADMAP.md), [evidence map](synthesis/THEMATIC_EVIDENCE_MAP.md) and [foundation handoff](../docs/RESEARCH_FOUNDATION_HANDOFF.md). The standalone comparison is secondary; no trap experiment has started. This is an editorial introduction change, not a regenerated catalog or changed catalog.json.

Relevance statements are analyst interpretation. Completion denotes lightweight checks, not scientific validation.

## AutoWebGLM: A Large Language Model-based Web Navigating Agent

[Summary](summaries/autowebglm_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/AutoWebGLM_A_Large_Language_Model-based_Web_Navigating_Agent.pdf`

**Method:** ChatGLM3-6B-based browser agent using simplified HTML, OCR-assisted parsing, task/location/history observations, and ten browser action categories. Hybrid rules/human/LLM data supports simple-to-complex SFT, 20-sample contrastive DPO plus SFT, and separate successful-trajectory RFT in MiniWoB++ and WebArena. Evaluation covers bilingual AutoWebBench, Mind2Web, MiniWoB++, WebArena, runtime decomposition, ablations, and operational error analysis.

**Attack surface:** ANALYST INFERENCE — potential interfaces include webpage HTML and screenshot acquisition, OCR/parsing, prompt assembly with page content and history, operable-element identifiers, URL/tab navigation, typing and clicking, and model-output execution. These are observable system interfaces, not demonstrated exploits. Attacker control, protected assets, authorization boundaries, and malicious-input conditions are unspecified.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: the paper is relevant to identifying security-sensitive interfaces because externally obtained webpage representations and interaction history feed model decisions that become executable browser actions. It also documents operational failures that could motivate adversarial investigation. It does not directly compare standalone LLMs with browser agents under attacks. The comparative vulnerability effect is UNKNOWN from this paper.

**Limitations:** Navigation-performance study rather than a security study. No standalone-versus-agent security control, adversarial test set, attack-success measure, or formal threat model. Environment-specific RFT and unequal candidate/training conditions qualify baseline comparisons. Missing uncertainty estimates, timing units/hardware, exact dataset allocation, and error denominators limit interpretation. Loss-weighting notation is unresolved. Repository and external artifacts were not supplied or reviewed.

## Go-Browse: Training Web Agents with Structured Exploration

[Summary](summaries/go_browse_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/Go-Browse_Training_Web_Agents_with_Structured_Exploration.pdf`

**Method:** Graph-based automatic demonstration collection with a remembered URL frontier; NavExplorer and PageExplorer propose interaction-grounded tasks; Claude-3.7-Sonnet attempts feasibility within three tries and a GPT-4o-based VLM judges completion; cheaper solvers collect prefixed and unprefixed trajectories. Successful trajectories fine-tune Qwen-2.5-7B-Instruct. Evaluation uses WebArena, Online-Mind2Web, descriptive component analyses, cost accounting, and paired bootstrap comparisons.

**Attack surface:** Analyst-inferred investigation points, not demonstrated attacks: current accessibility-tree observations, interaction histories and errors, executable model action outputs, navigation and content-modification capabilities, automatically proposed tasks, final-state screenshots supplied to the judge, and accepted trajectories used for training. Attacker control, authorization boundaries, exfiltration routes, injection resistance, and malicious-content handling are not specified or tested.

**Relevance:** MEDIUM confidence, analyst inference: relevant to the architecture of web agents because webpage observations, model-produced browser actions, automated task generation, VLM evaluation, and training-data feedback create boundaries worth examining in a security study. The paper directly measures task-solving capability and exploration efficiency, not vulnerability. It does not compare standalone LLMs against web agents under adversarial conditions; comparative vulnerability is UNKNOWN from this source.

**Limitations:** Five-domain collection scope; success-only training; model/prompt bias propagation acknowledged by authors; no adversarial or standalone-LLM security comparison; no judge-accuracy audit or explicit leakage check; incomplete implementation and repeated-run details; weak statistical support for some small benchmark margins; worse truly OOD results than NNetNav; unresolved failure-count and transfer-count inconsistencies; linked artifacts were not inspected.

## GPT-4V(ision) is a Generalist Web Agent, if Grounded

[Summary](summaries/seeact_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/GPT-4V(ision)_is_a_Generalist_Web_Agent_if_Grounded.pdf`

**Method:** Empirical multimodal web-agent study: screenshot-only action generation; attribute, textual-choice, image-annotation, and human-oracle grounding; cleaned Multimodal Mind2Web evaluation across tasks, websites, and domains; offline model and grounding comparisons; 90-task human-monitored live evaluation using Playwright; task-horizon analysis; 100 selected annotation-grounding errors; markup ablation; qualitative planning, knowledge, ambiguity, alternative-path, and recovery examples.

**Attack surface:** Analyst-inferred operational exposure includes screenshot and HTML observations, ranked element representations, label-to-element matching, generated action descriptions, browser execution, and iterative state feedback. The authors identify privacy-sensitive profiles, financial transactions, and application submissions as deployment concerns. No attacker control, prompt-injection attack, exploit, or attack success rate is demonstrated.

**Relevance:** MEDIUM confidence, analyst inference: the paper is relevant to why web-agent operation introduces risks beyond text generation because model decisions are grounded into browser events, grounding mistakes can cascade, and the authors observed possible harmful actions requiring human validation. It does not directly compare adversarial vulnerability of web agents with standalone LLMs, and its GPT-4 baseline is itself a web agent. Comparative vulnerability remains unestablished.

**Limitations:** No adversarial security experiment or standalone-LLM security comparison. Live evaluation excludes login, final submissions, and potentially harmful operations and includes human safety review, oracle assistance in one condition, and manual pop-up closure. Mixed subset conditions, missing uncertainty statistics, unspecified ablation sample, incomplete implementation settings, unlabeled plot values, and unreconciled numerical prose limit interpretation. Released artifacts were not inspected.

## LASER: LLM Agent with State-Space Exploration for Web Navigation

[Summary](summaries/laser_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/LASER_LLM_Agent_with_State-Space_Exploration_for_Web_Navigation.pdf`

**Method:** AUTHOR-REPORTED — HIGH confidence: Manually categorize shopping observations into four states; provide state-specific instructions and permissible actions; generate a rationale and select an action using GPT-4-0613 function calling; retain examined items for backup; permit at most 15 transitions and trigger history selection after 13 if unfinished. Evaluate 500 WebShop test instructions, 200-instruction ablations, the first 100 test instructions on converted Amazon pages, and 30 development-set error cases. Amazon trials stop at the decision to buy.

**Attack surface:** ANALYST INFERENCE — MEDIUM confidence: Candidate surfaces for a future security analysis include website observations and product details, search results, retained histories, rationale-to-function selection, action arguments, and Buy_Now execution. These are architectural components visible in the supplied method, not demonstrated exploit paths. The paper does not test prompt injection, exfiltration, malicious pages, authorization bypass, or adversarial manipulation.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper is indirectly relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis' because it documents an observation–rationale–function–execution loop and explicitly warns that real-world actions can have hard-to-recover consequences. It supports examination of how model errors become consequential actions and why human verification may be needed. It does not directly compare standalone LLMs with agents, specify an adversary, test attacks, or establish greater vulnerability. Confidence in a comparative vulnerability conclusion is UNKNOWN.

**Limitations:** AUTHOR-REPORTED and ANALYST OBSERVATIONS: Shopping target-item finding is the only evaluated task; manual states favor specific domains; real actions require caution and possible human verification. No completed real purchases, adversarial tests, standalone-LLM security comparison, reported statistical uncertainty, complete reward formula, full function parameters, or detailed annotation agreement are supplied. External code and guideline references were not reviewed.

## ReAct: Synergizing Reasoning and Acting in Language Models

[Summary](summaries/react_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf`

**Method:** Closed-document analysis of all 33 supplied text pages and 16 supplied rendered pages. The paper's main method uses frozen PaLM-540B with interleaved thoughts, actions and observations; dense thoughts for knowledge tasks, sparse thoughts for interactive tasks; component-removal baselines; CoT self-consistency hybrids; conditional manual error classification; ALFWorld prompt permutations; WebShop evaluation; smaller-model fine-tuning; and appendix GPT-3 and human-editing examples.

**Attack surface:** Analyst inference only: candidate surfaces include Wikipedia search/lookup responses, WebShop product titles, descriptions and options, accumulated interaction context, and the interface translating generated commands into actions. Authorized thought editing illustrates context sensitivity but does not establish attacker access. The paper specifies no adversary, malicious payload, exploit, or attack success rate.

**Relevance:** MEDIUM confidence, analyst inference: ReAct describes how environmental observations enter an LLM's context and guide subsequent actions, providing an architectural basis for studying external-input influence and action consequences. HIGH confidence scope finding: the paper does not directly compare adversarial vulnerability of web agents and standalone LLMs. Comparative vulnerability remains UNKNOWN.

**Limitations:** Security conclusions are limited by the absence of adversarial experiments and a matched standalone comparator. WebShop purchases are simulated and Wikipedia edits are prohibited. Reliability errors do not establish attacks. Exact plot values, omitted observations, uninspected code, missing statistical uncertainty, different evaluation conditions, and the Table 7 prompt inconsistency constrain further inference.

## WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

[Summary](summaries/webvoyager_comprehensive_summary.md) · Source: `01_Core_Web_Agent_Architectures/WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models.pdf`

**Method:** Closed-document analysis of all 27 supplied text pages and 24 rendered page images. The paper's method uses Selenium, screenshot-first multimodal observations with rule-based numbered element marking, seven action types, three recent observations plus full thought/action history, a 15-step budget, a 643-task/15-website benchmark, human task-success judgments, automatic multimodal evaluation, additional GAIA and SeeAct tasks, backbone/evaluator comparisons, and manual failure analysis.

**Attack surface:** Analyst-inferred potential interfaces, not demonstrated exploits: live webpage screenshots; interactive-element text, types, and aria-label content; parsed downloaded PDFs; execution-error feedback; model-selected Click, Type, Scroll, and search actions; file downloads and website requests. Attacker capabilities, prompt-injection mechanisms, permissions, and exploitation outcomes are not specified or tested.

**Relevance:** MEDIUM confidence, analyst inference: WebVoyager documents how live website screenshots, element text, and parsed files enter a model-driven browser loop whose decisions become external actions. Together with explicit author warnings about malicious downloads, private-data submission, and fake requests, this is relevant to analyzing why browser integration may introduce additional exposure and consequences. The paper does not directly compare standalone LLM security, test adversaries, or establish greater vulnerability.

**Limitations:** HIGH confidence in source boundaries: no security experiment, explicit attacker model, standalone-LLM comparison, authenticated-task evaluation, or tested defense. Non-login manually inspected harmless tasks constrain security relevance. Raw data, code, complete trajectories, full prompts, and separate supplements were not inspected. Pages 10–12 received text-only coverage; small embedded webpage details remain partially unreadable. Relevance beyond documented risks is labeled analyst inference.

## BEARCUBS: A benchmark for computer-using web agents

[Summary](summaries/bearcubs_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/BEARCUBS_A_benchmark_for_computer-using_web_agents.pdf`

**Method:** A curated 111-question live-web benchmark with 56 text-based and 55 multimodal items; author/freelancer creation; at least two author validators; text-workaround filtering; human evaluation; five baseline conditions; seven commercial agents; manual answer and trajectory assessment; auxiliary automatic-classifier agreement and limited four-run DeepSeek stability analysis.

**Attack surface:** ANALYST INFERENCE — MEDIUM confidence: live webpages, search results, alternative sources, multimedia, access prompts, and mouse/keyboard interactions are candidate surfaces for a future security study. The supplied work reports reliability and access problems, not attacker-controlled exploitation, exfiltration, or prompt-injection success.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: the paper informs investigation of live-web exposure, source trust, interface decisions, trajectory observability, and repeated actions. HIGH confidence: it does not measure adversarial attacks or establish that web agents are more security-vulnerable than standalone LLMs. Its zero-shot LLM comparisons concern factual task accuracy.

**Limitations:** Single short answer per task; limited multilingual scope; heterogeneous trajectory detail; changing websites and commercial products; different testing dates and 15/45-minute limits; no supplied inferential significance tests; conflicting human subgroup and source-proportion numbers; absent linked artifacts; no security threat model or adversarial comparison.

## BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

[Summary](summaries/browsecomp_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/BrowseComp_A_Simple_Yet_Challenging_Benchmark_for_Browsing_Agents.pdf`

**Method:** Human-created benchmark of 1,266 difficult short-answer questions; model and search screening; partial second-trainer checks; post-hoc topic classification; AI semantic-equivalence grading; human search campaign on 1,255 attempted questions; five model-configuration comparisons; browsing-effort scaling; 64-output aggregation and 64-trial task pass-rate analyses; answer-provided evidence retrieval and reference-quality review.

**Attack surface:** Analyst inference only: retrieved webpages, external source content, and the process of synthesizing multiple sources are candidate exposure points suggested by the described browsing workflow. Attacker control, prompt injection, unauthorized tool actions, data exfiltration, permissions, and attack success are not evaluated. Confidence in a specific comparative vulnerability conclusion is UNKNOWN.

**Relevance:** MEDIUM confidence, analyst inference: the paper provides relevant evidence about repeated web-information exposure, reasoning over retrieved content, and confidence-related reliability. It directly compares browsing and non-browsing model configurations on accuracy and calibration, but does not compare their security vulnerability. It cannot establish that web agents are more vulnerable to attacks than standalone LLMs.

**Limitations:** The benchmark intentionally omits common-query representativeness, long-answer ergonomics, and ambiguity resolution. Answer uniqueness is not guaranteed. Deep Research has task-oriented training. Calibration formula, grading-model identity, detailed budgets, uncertainty estimates, and implementation details are absent. Human times are self-reported. The 118-task review count and 14% zero-pass rate are not transparently reconciled. No security threat model or attacked-system comparison is supplied.

## Mind2Web: Towards a Generalist Agent for the Web

[Summary](summaries/mind2web_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/Mind2Web_Towards_a_Generalist_Agent_for_the_Web.pdf`

**Method:** Dataset and benchmark construction from 137 real websites and 2,350 retained tasks, with human proposals, demonstrations, author verification, page snapshots, and interaction traces. MindAct uses DeBERTa-v3-base candidate ranking followed by Flan-T5 or GPT multiple-choice element selection and operation/value generation. Evaluation uses independent steps with ground-truth histories across Cross-Task, Cross-Website, and Cross-Domain settings; auxiliary analyses examine random grouping, zero-shot XL, and matched GPT-4 task subsets.

**Attack surface:** Analyst inference only: task/context construction, webpage HTML and DOM-derived candidate representations, candidate ranking, pruned snippets in action prompts, operation/value generation, and possible execution of consequential clicks are architectural boundaries relevant to security investigation. The authors do not define attacker control over them, evaluate prompt injection, or demonstrate exfiltration or transaction attacks. Their stated safety concerns include financial transactions, user control, transparency, CAPTCHA circumvention, and malicious use.

**Relevance:** MEDIUM confidence analyst inference: the paper describes how a language-model web agent consumes external webpage representations and predicts executable interactions, and explicitly discusses sensitive actions and deployment safety. This informs possible exposure boundaries and consequences relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?' It does not establish the comparative premise. Comparative vulnerability, attack success, and specific exploitation mechanisms remain UNKNOWN because no standalone security baseline or adversarial experiment is supplied.

**Limitations:** English/U.S.-centered website coverage; MTurk sampling; text-only MindAct; limited modeling of dynamics and ongoing human interaction; cached offline alternative-path false negatives; cleared or omitted pop-ups and CAPTCHAs; fake consequential clicks during collection; low whole-task success; GPT-4's 50-task and top-10 restrictions; unresolved split-count and metric-label inconsistencies; absent security threat model, adversarial testing, and standalone-LLM vulnerability comparison. Linked artifacts were not inspected.

## MMInA: Benchmarking Multihop Multimodal Internet Agents

[Summary](summaries/mmina_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/MMInA_Benchmarking_Multihop_Multimodal_Internet_Agents.pdf`

**Method:** A 1,050-task multimodal web benchmark with 14 website-category entries and 1–10 hops; ordered completion queues; keyword or language-model single-hop evaluation; hop/task success comparisons across text, caption, multimodal, history, specialized-agent, and human conditions; hop-position analyses; and Gemini-Pro-Vision memory-history ablation.

**Attack surface:** ANALYST INFERENCE: candidate interfaces for future security investigation include accessibility-tree content, downloaded images, generated captions, browser action selection, replayed trajectories, and semantic evaluator inputs. These are observed or described data/control interfaces, not demonstrated exploitable attack surfaces. Attacker capabilities, trust boundaries, credentials, and harmful outcomes are unspecified.

**Relevance:** MEDIUM confidence, ANALYST INFERENCE: the paper supplies architectural and reliability evidence relevant to investigating why web agents may expose additional security boundaries. Website text, images, and histories influence executable browser actions. It does not directly compare adversarial vulnerability with standalone conversational LLMs, and no vulnerability increase or attack-success rate can be inferred from task-failure percentages.

**Limitations:** Live-web framing has offline and open-source exceptions. Hop totals conflict, table denominators are incompletely specified, long-task samples are small, Figure 5 has unlabeled exact values, and statistical uncertainty is unreported. Five pages have text-only coverage. The loss equation is extraction-sensitive. Code, task files, raw trajectories, and separate supplements were not supplied. Security relevance is indirect.

## The BrowserGym Ecosystem for Web Agent Research

[Summary](summaries/browsergym_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf`

**Method:** Systems and benchmark-integration work extending BrowserGym and introducing AgentLab, demonstrated by GenericAgent with six historical model backbones across six benchmark families and eight configurations. Evaluation uses task-performance means and standard errors, benchmark-specific validators, selected seeds/test splits/curricula, cost and runtime accounting, and one qualitative paired WorkArena L2 trace. VisualWebArena tests only three multimodal model conditions; most non-Claude WorkArena L3 values are reused or marked skipped.

**Attack surface:** Author-described components include raw Python execution, Playwright browser control, DOM/AXTree and screenshot observations, goals/chat history, navigation, file-upload primitives, external websites, and shared backend records. Analyst-inferred trust boundaries lie between externally controlled page content and model input, generated actions and execution, and concurrent agents and shared state. The paper discusses prompt injection but supplies no concrete attack protocol, attacker budget, exploit-success measurement, or validated isolation specification.

**Relevance:** MEDIUM confidence, analyst inference: the paper documents how web agents ingest external page observations and turn model outputs into executable code and consequential browser actions. Its authors explicitly discuss arbitrary untrusted code, prompt injection, sensitive-information leakage, and unwanted transactions. It offers architectural evidence and prospective risk arguments relevant to why agent compromise may have broader consequences than standalone text generation. It does not experimentally establish greater attack susceptibility or a vulnerability ratio compared with standalone LLMs; that comparison is UNKNOWN.

**Limitations:** Author-stated limitations include dynamic-site and model-service drift, localization and software differences, robot detection, open-web risks, shared-state collisions, synchronous interaction delays, retrieval underperformance, qualitative error analysis, and budget-related evaluation omissions. Additional analyst limitations include heterogeneous metrics, missing full execution artifacts, unresolved text/table inconsistencies, no security ablation, no attack dataset, and no standalone-LLM comparator. All 33 pages have supplied-text coverage; 23 have direct visual coverage.

## VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks

[Summary](summaries/visualwebarena_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/VisualWebArena_Evaluating_Multimodal_Agents_on_Realistic_Visual_Web_Tasks.pdf`

**Method:** A closed-document analysis of all 25 supplied text pages and 23 rendered pages. The paper constructs 910 visually grounded tasks across self-hosted Classifieds, Shopping, and Reddit, evaluates text-only, caption-augmented, screenshot/accessibility-tree, and screenshot/SoM agents using binary execution-based rewards, compares a 230-task human sample, and reports prompting, difficulty, subset, trajectory, later-model, and qualitative failure analyses.

**Attack surface:** Analyst-inferred candidate surfaces are encountered webpage text and images, accessibility-tree and caption representations, annotated element grounding, URLs, multiple tabs/sites, and browser operations that change account, shopping, posting, or comment state. These are observed interfaces and action affordances, not demonstrated attack vectors. No attacker capabilities, malicious artifacts, exploitation procedure, security assets, or measured trust-boundary violations are specified.

**Relevance:** MEDIUM confidence for architectural relevance; UNKNOWN for comparative security vulnerability. Analyst inference: the paper shows how web agents combine multiple observation channels with persistent state-changing actions and documents fragile multi-step execution. These features motivate hypotheses about broader exposure and greater consequences than text-only response generation. The authors explicitly caution that agents may cause more harm than regular LLMs without safeguards. However, the work does not experimentally compare standalone LLMs with web agents under attack, measure prompt injection, or establish why web agents are more attack-vulnerable.

**Limitations:** Capability success is not security vulnerability. No adversarial experiment or standalone-model security control is supplied. Human and agent task samples differ; observation budgets vary across models; model-mediated evaluators lack reported independent validation; uncertainty/repeated-run information is absent. Specific text-table and prompt inconsistencies remain unresolved. Pages 5 and 11 are text-only, tiny screenshot details are partly unreadable, and external implementations or supplements were not reviewed.

## WebArena: A Realistic Web Environment for Building Autonomous Agents

[Summary](summaries/webarena_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf`

**Method:** Closed-document analysis of all 22 supplied page texts and 17 supplied page images. The paper constructs a self-hosted web environment and 812-task benchmark, evaluates functional outcomes through reference answers and programmatic state checks, compares few-shot language-model browser agents, ablates the unachievable hint, examines template consistency, measures sampled human performance, checks evaluator accuracy, and presents qualitative failure cases. No tools, external research, or supplementary-artifact inspection were used.

**Attack surface:** ANALYST INFERENCE; confidence MEDIUM: Candidate surfaces include webpage content represented through accessibility trees or HTML, cross-site information flows, browser action interfaces, role-specific authenticated accounts, and the benchmark prompt's credential-listing page. These are architectural exposure points, not demonstrated exploitable vulnerabilities. Attacker control, malicious payloads, exfiltration destinations, and exploit success are unspecified; exploitability confidence is UNKNOWN.

**Relevance:** ANALYST INFERENCE; confidence MEDIUM: WebArena describes the additional interfaces and consequences introduced by browser agency—website observations, iterative action selection, authenticated account access, and persistent content/configuration changes. Its stopping and observation failures motivate security questions about instruction sensitivity and state interpretation. It does not directly compare standalone LLMs, test attacks, or establish greater security vulnerability. Confidence in the absence of that direct comparison within the supplied paper is HIGH.

**Limitations:** Reliability failures cannot be treated as attack success. There is no explicit adversarial threat model, malicious-content test, security metric, defense evaluation, or standalone-LLM baseline. Human and agent sampling differ; 170 human-evaluation templates versus 241 collected templates is unresolved. Main runs use temperature 1.0 without reported repeated-run uncertainty. Geographic and dataset sampling, account privileges, transition limits, evaluator scope, and uninspected public artifacts constrain conclusions.

## WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue

[Summary](summaries/weblinx_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/WebLINX_Real-World_Website_Navigation_with_Multi-Turn_Dialogue.pdf`

**Method:** Expert-built static conversational browser benchmark: 2,337 demonstrations across 155 websites; eight annotators; browser/chat/video recording and curation; dual-encoder Dense Markup Ranking; top-ten candidate selection; enriched and truncated text representation; nineteen zero-shot/finetuned model configurations; intent-gated geometric and lexical turn-level metrics; domain-shift tests; qualitative cases; human alternative-action agreement on 134 validation turns.

**Attack surface:** Analyst-inferred candidate surfaces include webpage DOM/HTML and screenshots incorporated into model input, conversational history, candidate selection and truncation, structured action generation, output parsing, and coordinate-to-element mapping. The paper specifies these components but does not test attacker control, prompt injection, data exfiltration, permission escalation, or exploitability.

**Relevance:** MEDIUM confidence, analyst inference: WEBLINX provides evidence about the complexity and consequences of grounding conversational decisions in browser actions, including wrong targets, credential-field confusion, missing history, and unintended-action warnings. It does not directly compare web-agent and standalone-LLM adversarial vulnerability. Use it as background evidence about action interfaces and reliability conditions, not as proof that agents have higher attack susceptibility.

**Limitations:** Static states do not support meaningful alternative rollout evaluation. Only five intents are scored; seven are training targets. Finetuning uses one run per configuration. Main results lack confidence intervals. Modality comparisons mix model architecture, size, training, and candidate access. Annotators stop before consequential purchases/bookings, and sites are selected as safe. Multiple reporting inconsistencies remain unresolved. No causal security comparison with standalone LLMs or adversarial evaluation is present.

## WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents

[Summary](summaries/webshop_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/WebShop_Towards_Scalable_Real-World_Web_Interaction_with_Grounded_Language_Agents.pdf`

**Method:** Benchmark/system and empirical machine-learning study: 1,181,436 products, 12,087 product-conditioned instructions, deterministic simulated retrieval/transitions, automatic matching reward, BART search imitation, BERT/ResNet attention-based action choice, optional policy-gradient fine-tuning, 500-instruction simulated testing over three reported model trials, component/trajectory/oracle diagnostics, and manually scored zero-shot transfer on 100 instructions across Amazon and eBay.

**Attack surface:** Analyst-inferred candidate study surfaces are product titles/descriptions/overviews, images, option and navigation labels, search retrieval, HTML-to-simple observation conversion, generated query candidates, and executable search/choose actions. The supplied paper does not establish attacker control, a malicious-content mechanism, credential exposure, prompt injection, or actual monetary purchases.

**Relevance:** MEDIUM confidence, analyst inference: WebShop documents how external webpage/product information and action labels enter a policy that performs sequential actions, making it relevant to identifying boundaries for a future security analysis. It does not directly explain or establish why web AI agents are more vulnerable than standalone LLMs. Confidence in any comparative vulnerability conclusion from this paper is UNKNOWN.

**Limitations:** No explicit security threat model, adversarial experiments, or standalone-LLM control. The i.i.d. shopping benchmark and two-site transfer do not establish broad web or security generalization. Appendices A–D are absent; key implementation/statistical details are unavailable. Numeric and notation inconsistencies are preserved rather than silently reconciled. Visual inspection covers pages 1–10; pages 11–14 are text-only.

## WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?

[Summary](summaries/workarena_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/WorkArena_How_Capable_are_WebAgents_at_Solving_Common_Knowledge_Work_Tasks.pdf`

**Method:** HIGH confidence: benchmark and systems development plus empirical capability evaluation. WorkArena has 33 task types and 19,912 available instances on ServiceNow. BrowserGym uses Chromium, CDP, and Playwright. GPT-4o, GPT-3.5, and Llama3-70B configurations are selected through random search on WorkArena and MiniWoB, then reevaluated with a different seed. Evaluation uses ten seeds per WorkArena/MiniWoB task, one per WebArena task, a 15-step limit, and 1,000 stratified-bootstrap mean samples. Tables 3–5 report feature ablations; GPT-4o-V adds a Set-of-Mark screenshot.

**Attack surface:** MEDIUM confidence, analyst inference: candidate surfaces are HTML/AXTree/screenshot observations, chat and error information entering prompts, model-generated browser actions, optional arbitrary Python execution, navigation, enterprise data writes, catalog submission, impersonation, and outgoing user messages. These are documented interfaces or capabilities, not demonstrated exploit paths. Table 1's evaluated agents use bid-only actions; unrestricted Python is an environment option.

**Relevance:** MEDIUM confidence, analyst inference: the paper documents the operational connections that make browser agents security-relevant—external observations, executable actions, enterprise record changes, orders, identity switching, and information transmission. It does not establish that web agents are more vulnerable than standalone LLMs. The comparative security hypothesis remains UNKNOWN because no matched standalone baseline, adversarial evaluation, or attack-success metric is supplied.

**Limitations:** HIGH confidence for source boundaries: no direct comparative security study, formal threat model, attack workload, validated defense, or standalone-LLM security baseline. Some tasks may exceed the 15-step limit; prompts are truncated; model-specific configurations and context budgets vary. Oracle solutions may be nonoptimal. Synthetic knowledge content and limited task seeds constrain generalization. Repository code and raw outputs were not inspected. Textual inconsistencies and unreadable exact Figure 4 statistics remain explicit.

## WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks

[Summary](summaries/workarena_plus_comprehensive_summary.md) · Source: `02_Web_Agent_Benchmarks_Environments/WorkArena_Towards_Compositional_Planning_and_Reasoning-based_Common_Knowledge_Work_Tasks.pdf`

**Method:** Benchmark and systems study: 341 ServiceNow workflows at L2 and L3 yield 682 tasks; coded oracles and validators support reproducible curricula of 235 instances per level. Five agent variants operate through restricted BrowserGym actions under a 50-step cap. Evaluation includes a 15-person human study on 98 instances, qualitative trace analysis, oracle action-length characterization, and an L1 context-length ablation.

**Attack surface:** Analyst-inferred candidate surfaces include ticket descriptions, knowledge-base instructions, accessibility-tree content, screenshot-to-element grounding, action identifiers, and record-changing frontend operations. These are legitimate workflow inputs and interfaces in the paper; no attacker control, injection payload, exploitation result, or validated security boundary is supplied.

**Relevance:** MEDIUM confidence, analyst inference: the paper informs 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?' by documenting how browser agents integrate page-resident instructions, target interface elements, change enterprise records, and sometimes misjudge resulting state. It does not compare standalone LLMs with web agents, measure adversarial vulnerability, or establish that one is more vulnerable.

**Limitations:** Safety and malicious-behavior robustness are explicitly outside scope. The environment is ServiceNow only; the human sample is small and biased; human and agent action budgets differ; model context budgets vary; qualitative errors lack prevalence estimates. Task-count, offboarding, and context-configuration inconsistencies remain unresolved. Repository and supplementary artifacts were not reviewed.

## AUTOSCRAPER: A Progressive Understanding Web Agent for Web Scraper Generation

[Summary](summaries/autoscraper_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/AutoScraper_A_Progressive_Understanding_Web_Agent_for_Web_Scraper_Generation.pdf`

**Method:** Two-phase scraper generation: progressive top-down XPath selection with step-back DOM-context recovery, followed by selection among candidate sequences using their extraction results across seed pages. Evaluation covers SWDE, Extended SWDE, and DS1 with eight LLMs, COT and Reflexion baselines, six case-outcome categories, mean per-case extraction metrics, synthesis ablation, seed-count variation, direct and supervised comparisons, runtime amortization, golden-label generation, action lengths, and predicate fragility. Main seed counts are 3, 3, and 1 respectively; DS1 omits synthesis.

**Attack surface:** ANALYST INFERENCE — Candidate interfaces for a future security analysis are preprocessed HTML input, extraction and thought history, LLM-generated XPath submitted to a parser, step-back judgments, and synthesis selection over candidate sequences and results. No attacker capabilities, malicious-content conditions, privileged actions, exfiltration paths, or demonstrated exploit are reported. Removal of script/style nodes and non-class attributes is preprocessing, not an evaluated security defense.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence for architectural relevance; UNKNOWN confidence for comparative vulnerability. The paper illustrates a workflow in which webpage HTML influences LLM-generated XPath, parser outputs feed back into reasoning, and a selected extraction sequence is reused. These interfaces can inform questions about content manipulation and propagation of erroneous rules. The work does not directly compare the security of web agents and standalone LLMs; its direct-extraction comparison measures extraction performance rather than attack susceptibility.

**Limitations:** Author-stated boundaries include vertical-page extraction, limited transfer to broad interactive environments, backbone dependence, non-generalizable layouts, missed multi-valued information, and XPath fragility. Analyst observations include absent security experiments, absent main-result confidence intervals, incomplete reproduction settings, unclear sample accounting, DS1 166/186-page inconsistency, Extended inventory 297/294 discrepancy, eight/ten runtime-domain mismatch, and pseudocode ambiguities. Text-only inspection applies to pages 9–11 and 17; external implementation and supplementary artifacts were not reviewed.

## Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge

[Summary](summaries/mind2web_2_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/Mind2Web_2_Evaluating_Agentic_Search_with_Agent-as-a-Judge.pdf`

**Method:** 130 validated tasks across six domains and 24 subdomains; 10 public development tasks and 120 private test tasks; task-specific rubric trees with critical gates, non-critical averaging, and sequential dependencies; Python judges using o4-mini extraction/verification and cached webpage evidence; Claude-3.7-Sonnet initial script generation, debugging, reflection, and two-stage human refinement. Ten systems are evaluated three times per task using April–June 2025 answers; human comparison and error analysis use Subset-30; judge validation uses 15 tasks, two held-out answers each, and 720 leaf checks.

**Attack surface:** Analyst inference only: examined interfaces include agent answers, cited URLs, retrieved webpage text and screenshots, browser interaction, generated tool code, and the evaluator's LLM inputs. These are relevant places to investigate untrusted-content handling, but the paper does not demonstrate exploitation of them. Its attribution framework assumes truthful and credible sources and does not assess source credibility.

**Relevance:** MEDIUM confidence, analyst inference: the paper informs the question 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis' through evidence of complex browser environments, long contexts, improper tool invocation, source-memory failures, fabricated URLs, and unsupported synthesis. It is a reliability and benchmark study, not an adversarial security comparison. No standalone tool-free LLM control, attacker model, or attack-success measurement is supplied, so greater comparative vulnerability is not established.

**Limitations:** Authors acknowledge limited task scope, assumed source truthfulness, single-page attribution requirements, possible LLM judgment errors, and proprietary-system opacity. Additional analyst observations include unequal agent/human task sets, mixed timing procedures, observational rather than controlled mechanism comparisons, one primary judge-study evaluator with developer adjudication, unavailable reproduction artifacts, and possible completeness/scoring issues in the illustrative script. Original authors are Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, and Yu Su; affiliations are The Ohio State University and Amazon AGI. The supplied version is arXiv:2506.21506v2, 3 July 2025.

## WebDancer: Towards Autonomous Information Seeking Agency

[Summary](summaries/webdancer_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/WebDancer_Towards_Autonomous_Information_Seeking_Agency.pdf`

**Method:** AUTHOR-REPORTED, HIGH confidence: Four-stage pipeline: synthesize CRAWLQA and E2HQA; sample short/long-CoT ReAct trajectories with rejection sampling and quality filtering; apply observation-masked supervised fine-tuning; apply on-policy DAPO with binary format and model-judged correctness rewards weighted 0.1 and 0.9. Evaluation uses 103 GAIA text-only validation questions and 680 WebWalkerQA test questions, with additional BrowseComp evaluations and training/data ablations.

**Attack surface:** ANALYST INFERENCE, MEDIUM confidence: Candidate interfaces visible in the current system include search titles/snippets, visited web content, summarizer-produced evidence and summaries, tool-response dialogue context, and generated search/visit arguments. No malicious-content experiment, privilege model, credential exposure, or exploit is supplied. Browser modules and a Python sandbox for external APIs are future proposals and are excluded from the evaluated current surface.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper is relevant as architectural and reliability evidence for investigating why web-agent security might differ from standalone-model security. External observations guide subsequent reasoning and actions, and tool responses are serialized as user messages. These are interfaces for future security tests. The paper directly compares task performance across base, RAG, and agentic configurations; it does not compare their adversarial vulnerability or establish that web agents are more vulnerable.

**Limitations:** AUTHOR-REPORTED plus clearly labeled ANALYST OBSERVATIONS: Current tools and short-answer tasks are limited; RL uses a small subset under compute/stability constraints; rollouts are costly; long reasoning can generate invalid or repetitive outputs, nonexistent tools, and redundant actions. Analyst observations include absent security tests, no uncertainty intervals, incomplete reproducibility settings, an action-filter/count contradiction, an unexplained Figure 3 count mismatch, and an unrelated thought in the case study. No absent supplement or external repository was reviewed.

## WebGPT: Browser-assisted question-answering with human feedback

[Summary](summaries/webgpt_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/WebGPT_Browser-assisted_question-answering_with_human_feedback.pdf`

**Method:** Empirical machine-learning and restricted-browser systems study: GPT-3 models of 760M, 13B, and 175B parameters learn from human browser demonstrations; pairwise comparisons train reward models; PPO and best-of-n selection are compared. Main configurations use behavior cloning plus 4, 16, or 64 candidates, temperature 0.8, and at most 100 browsing actions. Evaluations cover ELI5 preferences, TruthfulQA truthfulness/informativeness, TriviaQA extraction, scaling, framing, cultural bias, and contractor surveys.

**Attack surface:** ANALYST INFERENCE: Potential security-relevant boundaries include Bing queries and result text, fetched pages, HTML/PDF-to-text conversion, indexed links, collected quotations, and browser commands. The implemented external actions are restricted to queries and following existing links. Form submission and direct page editing are absent. Prompt injection, exfiltration, credential theft, and successful privilege escalation are not evaluated.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: WebGPT is relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?' because its browser architecture adds external-source ingestion, evidence selection, and externally executed actions. Its discussion identifies selective references, citation-induced overreliance, and conditional evidence manipulation with broader permissions. It does not directly compare security vulnerability against standalone LLMs. Its actual GPT-3 comparison concerns truthfulness and favors WebGPT under the reported conditions.

**Limitations:** No formal attacker model or controlled security comparison; current browser lacks direct write actions. Human preference and supportedness do not equal independently established truth. TruthfulQA uses different evaluator types for GPT-3 and WebGPT and truncates WebGPT answers. The framing study is small, cultural bias is a single-question case study, some scaling uses a learned proxy, and smaller-model RL has a disclosed EMA bug. Linked supplementary artifacts were not inspected.

## WebSailor: Navigating Super-human Reasoning for Web Agent

[Summary](summaries/websailor_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/WebSailor_Navigating_Super-human_Reasoning_for_Web_Agent.pdf`

**Method:** Graph-based SailorFog-QA synthesis with ambiguous clues; successful expert action-observation traces with reconstructed short reasoning; correctness, length and tool-call filtering; observation-masked RFT cold start; DUPO RL with group-relative rewards and duplication of informative batch cases; benchmark and ablation evaluation of Qwen-2.5-based 3B, 7B, 32B and 72B agents using search and visit tools.

**Attack surface:** ANALYST INFERENCE, MEDIUM confidence for architectural identification; UNKNOWN confidence for exploitability: search-result titles, snippets and URLs; full webpage content retrieved through Jina; Qwen-2.5-72B goal-conditioned page summaries; accumulated tool-response context; and model-based answer judging. No attacker-controlled condition, demonstrated exploit, security objective, or attack success rate is supplied.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper describes how external search results, retrieved webpages, goal-conditioned summaries, and repeated observations enter an agent's later decision context. These are useful boundaries for studying why web agents might differ from standalone LLMs in security exposure. The paper compares direct inference and browsing for accuracy, not vulnerability, and does not establish that web agents are more vulnerable.

**Limitations:** Security relevance is indirect. There is no explicit threat model or matched standalone-versus-agent security experiment. Performance evaluation uses heterogeneous baseline provenance, partial benchmark coverage, LLM judging, and no reported confidence intervals. Synthetic answers may be nonunique. Context limits, over-thinking and synchronous training constrain the system. Several reproducibility settings and scoring details are absent; external artifacts were not inspected.

## WEBSCRAPER: LEVERAGE MULTIMODAL LARGE LANGUAGE MODELS FOR INDEX-CONTENT WEB SCRAPING

[Summary](summaries/webscraper_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/Webscraper_Leverage_Multimodal_Large_Language_Models_for_Index-Content_Web_Scraping.pdf`

**Method:** Experimental AI systems study using Anthropic Computer Use with a guiding five-stage prompt and custom Parse/Merge Tools. It compares baseline, prompt-only, and full configurations on six news sites and two e-commerce sites, with temperature 0, clean Firefox starts, 30 reported repetitions, a CI convergence analysis, and a seven-day temporal repeat. News Correctness requires exact URL matching and title/content ROUGE-L scores of at least 0.8; product Correctness is stricter but incompletely defined.

**Attack surface:** ANALYST INFERENCE: candidate interfaces include screenshot and HTML ingestion, agent-to-tool decisions, Bash network and filesystem operations, file editing, delegated model inputs, generated Python execution, and output consolidation. These are described capabilities and analytical boundaries, not demonstrated exploit paths; permissions and security controls are unspecified.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper provides a concrete architecture for examining how external webpage observations connect to computer actions, network/file tools, delegated parsing, and generated-code execution. It does not directly compare standalone LLMs with web agents, define an adversary, or establish greater vulnerability. Confidence in any comparative security outcome from this paper is UNKNOWN.

**Limitations:** Index-and-content scope; visual-navigation and generated-code failures; difficulty with streaming and advanced virtual scrolling; incomplete benchmark sizes, statistical details, product matching rules, prompt stages, and implementation access; unresolved GPT-o3 versus GPT-o3-mini wording. Figures 1–4 and Tables 1–2 were visually reviewed on pages 1–5; pages 6–7 were text-only. No adversarial evaluation or standalone-LLM control is reported.

## WebWalker: Benchmarking LLMs in Web Traversal

[Summary](summaries/webwalker_comprehensive_summary.md) · Source: `03_Agentic_Search_Scraping_Info_Seeking/WebWalker_Benchmarking_LLMs_in_Web_Traversal.pdf`

**Method:** Mixed benchmark and empirical AI systems study: 680 human-refined QA pairs across 1,373 webpages; single-source and two-page multi-source construction with depth-based difficulty; explorer–critic WebWalker compared with ReAct and Reflexion across six listed backbones in zero-shot conditions with a principal 15-action budget; GPT-4 factual grading and correct-execution action counts; additional domain/language, error-category, search-system, RAG-integration, and action-budget analyses.

**Attack surface:** Analyst-inferred candidate surfaces are extracted webpage Markdown, clickable HTML button descriptions, associated URLs, explorer interaction history, critic relevance extraction and memory, sufficiency decisions, and memory appended to retrieved documents. These are documented information-flow components, not demonstrated attacks. No attacker capability, malicious payload, protected asset, exploit success rate, or security defense is evaluated.

**Relevance:** MEDIUM confidence, analyst inference: the work is relevant as a concrete architecture for identifying where external webpage content enters agent observations, navigation decisions, persistent critic memory, and RAG generation context. It does not directly answer why web AI agents are more vulnerable than standalone LLMs. Its close-book comparisons measure factual QA accuracy, not adversarial vulnerability; actual relative vulnerability is UNKNOWN from this source.

**Limitations:** Author-stated limits include dataset size, approximately 14k insufficiently human-verified silver pairs, HTML-DOM-only interaction, no additional agent training, and supplied root URLs in hybrid integration. Analyst observations include missing statistical uncertainty and evaluator calibration, success-conditioned cost measurement, incomplete configurations and artifacts, unresolved numerical/notation/example inconsistencies, and complete absence of adversarial or matched security comparisons. Table 3 Qwen2.5-7B ReAct overall action count is below all displayed subgroup means; the aggregation remains unresolved.

## AdvAgent: Controllable Blackbox Red-teaming on Web Agents

[Summary](summaries/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AdvAgent_Controllable_Blackbox_Red-teaming_on_Web_Agents.pdf`

**Method:** GPT-4 generates candidate adversarial prompts with replaceable target placeholders. Victim-agent responses label candidates as successful or failed. A Mistral-7B-Instruct-v0.2 prompter receives positive-only supervised fine-tuning and then direct preference optimization using positive and negative prompts with a fixed SFT reference. Evaluation uses SeeAct with gpt-4-vision-preview and gemini-1.5-flash on a four-domain Mind2Web subset of 440 tasks split into 240 training and 200 testing tasks, with exact action-triplet step ASR.

**Attack surface:** Webpage HTML accessible to SeeAct during action grounding, primarily non-rendered aria-label attributes near the expected target element; an id-field variation is also evaluated. The attacker controls HTML and obtains black-box feedback but lacks agent-framework, model-weight, logit, and gradient access. The formal objective changes the action argument while preserving operation and target element.

**Relevance:** MEDIUM confidence, analyst inference: the paper shows how attacker-controlled, visually hidden HTML can influence a web agent's executable action arguments. Its relevance to why agents may face greater security exposure concerns environmental inputs, HTML grounding, and consequential action execution. It does not conduct a matched comparison against standalone LLMs and cannot establish a comparative vulnerability rate.

**Limitations:** Author-stated limitations are offline victim-feedback optimization and step-based evaluation that does not fully capture complete-task risks. Analyst observations include one evaluated agent framework, two backend identifiers, four selected domains, conditional reuse experiments, incomplete denominators and reproduction details, no matched standalone-LLM comparison, no measured completed financial harm, and no review of the linked code or absent supplements.

## AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents

[Summary](summaries/agentfuzzer_generic_black_box_fuzzing_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AGENTFUZZER_Generic_Black-Box_Fuzzing_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf`

**Method:** Black-box adaptive fuzzing using collected prompt templates, GPT-4o-mini-assisted Shorten, Expand, Rephrase, Crossover, and GenerateSimilar mutations, attack-success plus intended new-task-coverage scoring, and MCTS-inspired UCB1 seed selection. Evaluation covers AgentDojo and VWA-adv, held-out tasks, other model backbones, selected defenses, two ablation conditions, a local shopping-site case, extra models, additional baselines, and scenario breakdowns.

**Attack surface:** Attacker-controlled external data read during legitimate agent execution, including environment-state placeholders, text triggers in web tasks, and customer reviews in a local shopping site. The attacker lacks internal model and agent access, can test similar tasks, and receives binary attack feedback. Image-trigger optimization and direct infrastructure compromise are outside the reported evaluation scope.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains an agent-specific attack pathway in which third-party web content enters an LLM planner and redirects tool-mediated actions. This is relevant to understanding additional exposure and consequences in web agents. The paper does not directly compare standalone LLMs with agents, so it cannot establish a comparative vulnerability rate or prove the research question's premise.

**Limitations:** No standalone-LLM control, uncertainty intervals, repeated-run variability, complete corpus, exact split memberships, numerical scoring weights, complete query costs, or measured scalability results are supplied. Transfer gains are not universal, especially for Claude. Scoring and selection are ablated jointly. VWA headline/table results, defense prose/table interpretations, and Appendix B.1/Table 4 values have unresolved inconsistencies. The practical example is locally deployed, and web attacks focus on text triggers.

## AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents

[Summary](summaries/agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AgentVigil_Generic_Black-Box_Red-teaming_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf`

**Method:** Black-box iterative fuzzing using curated prompt templates, GPT-4o-mini-assisted mutations, ASR plus new-task coverage scoring, UCB-based one/two-seed selection, and ancestry visit updates. Evaluated on AgentDojo and VWA-adv with optimization, selected-prompt transfer, defenses, adaptive repeat-defense testing, ablation, additional baselines/models, scenario breakdowns, and a local shopping-site demonstration.

**Attack surface:** Attacker-controlled external data encountered by benign-user agents: environmental placeholders, shopping reviews, email/calendar-style content, and VWA-adv text triggers. Image-trigger attack generation, direct harmful-user misuse, and infrastructure attacks are outside the evaluated scope.

**Relevance:** ANALYST INFERENCE; confidence MEDIUM. The paper explains how external content consumed during multi-step agent execution can influence the planning LLM and trigger tool-mediated unauthorized actions. This is relevant to why web-agent interfaces may expose additional attack pathways. It does not directly compare matched standalone LLMs with web agents or establish a numerical increase in vulnerability due to agentization.

**Limitations:** Author-stated high computational cost and weak transfer to models such as Claude. Analyst observations include missing reproducibility parameters and uncertainty statistics, combined scoring/selection ablation, text-trigger-only web attacks, no standalone control, local case-study denominator/trace limitations, and unresolved prose/table and coverage/ASR discrepancies. Version relationship: this published AGENTVIGIL paper and the previously summarized AgentFuzzer/AGENTVIGIL arXiv version belong to the same study family. Their overlapping results are not independent replication; the adaptive Repeat-defense result is version-specific evidence and must retain its separate protocol.

## Attacking Vision-Language Computer Agents via Pop-ups

[Summary](summaries/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Attacking_Vision-Language_Computer_Agents_via_Pop-ups.pdf`

**Method:** Author-reported, HIGH confidence: a four-component pop-up attack evaluated with five closed-source VLM backbones on 50 selected easy OSWorld tasks and 72 selected easy VisualWebArena tasks, with model comparisons, component ablations, prompt defenses, task-level attack metrics, generated-thought analysis, accessibility-template comparisons, and delayed attack onset.

**Attack surface:** Author-reported, HIGH confidence: attacker-controlled pop-up pixels and associated accessibility-tree content, including ALT descriptors and clickable-element roles. The default attacker knows the user query, pop-up position, and agent framework; reduced-information variants are evaluated.

**Relevance:** Analyst inference, MEDIUM confidence: the paper identifies mechanisms relevant to why web and computer agents may acquire additional vulnerabilities—untrusted environmental instructions, combined visual/accessibility exposure, executable actions, and repeated opportunities for malicious clicks. It does not directly compare agents with standalone LLMs, so any claim that agents are more vulnerable in magnitude is UNKNOWN from this study.

**Limitations:** Author-reported and analyst-observed: closed-source-only evaluation; no advanced optimized or persuasive jailbreak construction; idealized default attacker knowledge; selected task subsets; ignored malicious clicks without actual redirection; no matched standalone-LLM or human control; no reported confidence intervals or repeated-run counts; causal explanations partly hypothetical; code and separate supplements not inspected.

## Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks

[Summary](summaries/commercial_llm_agents_are_already_vulnerable_to_simple_yet_dangerous_attacks_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Commercial_LLM_Agents_Are_Already_Vulnerable_to_Simple_Yet_Dangerous_Attacks.pdf`

**Method:** Taxonomy plus handcrafted illustrative attacks. A four-stage web pipeline is evaluated through trusted-platform exposure, destination redirection, and harmful action, with a direct-link comparison and qualitative post-feature ablation. Scientific tests insert one malicious document into a synthetic database of over 10,000 documents and examine PaperQA retrieval and ChemCrow obfuscation-related outputs.

**Attack surface:** External web posts and destination sites, search-mediated discovery, sensitive memory and system-prompt information, download/execution tools, authenticated email access, scientific retrieval databases, and chemical-name safeguards. Memory poisoning, API compromise, and multimodal manipulation are also taxonomic surfaces, but are not all separately evaluated.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains mechanisms relevant to why web AI agents may be more vulnerable than standalone LLMs, including attacker-controlled environmental inputs, memory and retrieval dependencies, accessible sensitive information, delegated tool authority, and context-dependent safety. The authors explicitly argue that agent components make attacks easier, but do not report a matched quantitative standalone-versus-agent experiment.

**Limitations:** Small and narrow web trial sets; conditional exposure rather than natural encounter rates; unspecified trial independence and configurations; proprietary internals unknown; MultiOn unavailable for extensive systematic evaluation; privacy counts not product-disaggregated; qualitative ablation without numeric details; synthetic scientific database; unquantified ChemCrow bypass trials; redacted screenshot; no matched standalone baseline or evaluated defense; behavioral proxies rather than demonstrated downstream physical or financial harm.

## Dissecting Adversarial Robustness of Multimodal LM Agents

[Summary](summaries/dissecting_adversarial_robustness_of_multimodal_lm_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Dissecting_Adversarial_Robustness_of_Multimodal_LM_Agents.pdf`

**Method:** Closed-document analysis of the supplied 22-page text and 18 rendered page images. The paper constructs 200 VWA-Adv tasks with targeted execution-based evaluation and ensured trigger exposure, models component information flow with ARE, and evaluates prompt injection, white-box captioner optimization, CLIP surrogate transfer, reflexion, shallow tree search, defenses, and transfer ablations.

**Attack surface:** Attacker-owned listing or post content: one injected text fragment or one image perturbed within an infinity-norm bound of 16/256. The image occupies less than 5% of webpage pixels in the described setting. Downstream recipients include captioners, policies, trajectory evaluators, and value functions; direct modification of the legitimate user goal or agent is excluded.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper explains how environmental inputs, image-to-text preprocessing, evaluators, and value functions distribute an agent's attack surface and propagate attacker influence into actions. Clean added components can improve robustness, while attacked components can worsen it. This supports a mechanism-based security analysis of web agents, but does not establish that agents are quantitatively more vulnerable than standalone LLMs under matched experimental conditions.

**Limitations:** Fixed web environments and selected agent/model snapshots; attacks establish lower-bound risk rather than maximum possible risk; two-attempt reflexion and branching-three/depth-one search; curated solvable tasks and guaranteed trigger exposure; no matched standalone-LLM comparison; incomplete uncertainty and optimization reporting; unresolved relative-percentage discrepancies. Pages 11–13 and 22 were reviewed as text only, and external repository/supplementary contents were not inspected.

## EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage

[Summary](summaries/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/EIA_ENVIRONMENTAL_INJECTION_ATTACK_ON_GENERALIST_WEB_AGENTS_FOR_PRIVACY_LEAKAGE.pdf`

**Method:** Offline SeeAct evaluation with GPT-4V, Llava-1.6-Mistral-7B, and Llava-1.6-Qwen-72B on 177 curated Mind2Web action steps. Specific-PII experiments compare FI text, FI aria, and Mirror Injection across eight placements at opacity zero. Full-request experiments introduce FI text at opacity 0.2. Additional analyses examine tool detection, next-action continuation, three defensive prompts, five adapted webpages, subgroup results, and element selection versus content leakage.

**Attack surface:** Compromised webpage HTML elements, text and aria-label attributes, DOM-relative placement, CSS-controlled visibility, and automatic transmission from injected fields. Invisible content targets grounding; faintly visible content can also target screenshot-based generation.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains mechanisms relevant to why web agents may add security exposure—attacker-controlled HTML and screenshots are processed alongside private task context and converted into executable browser actions, permitting disclosure with continued task progress. It does not directly compare web agents with standalone LLMs and cannot establish a general comparative vulnerability rate.

**Limitations:** Offline step-level evaluation rather than real-time end-to-end tasks; one framework; sparse subgroup counts; no standalone-LLM baseline; no controlled human-detection study; narrow defense family; incomplete reported reproduction settings and absent implementation artifacts; unlabeled curve values and Table 1 variance/aggregation inconsistencies. Broader relevance is analyst inference, not an author-tested comparison.

## How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation

[Summary](summaries/searchgeo_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/How_Much_Can_We_Trust_LLM_Search_Agents_Measuring_Endorsement_Vulnerability_to_Web_Content_Manipulation.pdf`

**Method:** HIGH confidence; author-reported. SearchGEO combines a cached/live hybrid search proxy, embedding-based query routing, controlled result replacement, 44 tasks across four domains, 13 main backends, five conceptual modes implemented as six attack conditions, paired clean controls, and LLM-judged ASR, baseline-adjusted OSS, and blind SS. Additional experiments examine source count/rank, prompt and adapted OpenClaw defenses, skill recommendations, generator control, and bounded judge coupling.

**Attack surface:** HIGH confidence; author-reported. Structured web-search results comprising URL, title, snippet, optional extracted text, and multi-result relationships. The user is benign; attacker placement is assumed within query clusters. Attackers cannot access system prompts, internal reasoning, memory, or tool configurations, and do not control real high-authority domains.

**Relevance:** MEDIUM confidence; ANALYST INFERENCE. The paper demonstrates how web retrieval exposes agents to publisher-controlled metadata, page content, fabricated authority, apparent consensus, and citation dependencies that can become recommendations. This provides a mechanism relevant to why web agents may face additional vulnerability. It does not directly compare matched standalone LLMs with web agents, establish universal greater vulnerability, or estimate the comparative gap.

**Limitations:** HIGH confidence for stated boundaries. Static proxy and assumed exposure omit live ranking dynamics; approximately 30% of cached results are snippet-only; skill probes are small and mechanism-level; GPT-mini is both subject and judge; bounded validation sample sizes are unspecified and full cross-family judging is absent. Analyst observations include no standalone comparator, limited uncertainty reporting, unequal source counts across modes, adapted rather than untouched OpenClaw conditions, no command execution demonstration, and unavailable raw artifacts.

## Identifying AI Web Scrapers Using Canary Tokens

[Summary](summaries/canary_tokens_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Identifying_AI_Web_Scrapers_Using_Canary_Tokens.pdf`

**Method:** AUTHOR-REPORTED: Deploy 20 dynamic fictional websites with ten canary placeholders each; assign stable content versions to UA–ASN pairs; promote indexing; query 22 production chatbots using two tailored prompts; extract and filter matching values; infer associations; compare a two-month accessible baseline with ten offline sites and ten robots.txt-restricted sites at one- and two-week intervals, then repeat after restoration. Attribution is obtained for 18 systems. The printed threshold rule is internally inconsistent.

**Attack surface:** ANALYST INFERENCE: Relevant information-entry and retention surfaces are dynamic webpages, scraper requests identified by User-Agent and ASN, search-engine indexes, retained content, and retrieved material incorporated into chatbot answers. The study uses benign fictional tokens as a measurement instrument, not adversarial instructions or an implemented exploit.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper provides evidence that web-enabled chatbot outputs incorporate website-controlled values through diverse scraper and intermediary paths, and that previously acquired information can persist after origin access changes. This informs analysis of provenance, external-input exposure, and downstream control boundaries. It does not directly compare web AI agents with standalone LLMs, establish that web agents are more vulnerable, or measure prompt injection or harmful tool actions.

**Limitations:** AUTHOR-REPORTED: Twenty websites, one U.S. university-network vantage point, finite observation window, prompt-dependent visibility, insufficient output evidence, and scaling/adversarial-token challenges. ANALYST OBSERVATIONS: Undefined F notation and contradictory acceptance logic; incomplete detailed temporal coverage; unspecified service versions and randomization; no controlled accuracy estimates; cache ownership unresolved; no standalone comparison or demonstrated attack; external code/data artifacts were not reviewed.

## Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

[Summary](summaries/indirect_prompt_injection_real_world_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Not_What_You've_Signed_Up_For_Compromising_Real-World_LLM-Integrated_Applications_with_Indirect_Prompt_Injection.pdf`

**Method:** AUTHOR-REPORTED: Threat-based cybersecurity taxonomy plus manually constructed qualitative proof-of-concept attacks. Synthetic applications use OpenAI API models, selected described tools, prepared interface responses, and sampling temperature 0. text-davinci-003 uses LangChain/ReAct; GPT-4 uses chat-format tool descriptions and direct instructions. Real-system tests use Bing Chat through local Edge HTML and GitHub Copilot through injected package context. Outcomes are reported as triggered behaviors rather than statistical benchmark results.

**Attack surface:** AUTHOR-REPORTED: Inference-time third-party content including retrieved websites, the current page read through the Bing/Edge sidebar, incoming email, imported package comments and documentation, personal or documentation files, and persistent memory. Delivery families are passive, active, user-driven, and hidden. Consequences depend on available tools such as search, URL retrieval, email, address-book access, and memory. Public-web discovery, image-hidden payloads, and some other proposed delivery routes are discussed without corresponding live deployment measurements.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper helps explain why web-connected AI agents can acquire additional security exposure relative to a model receiving only authorized direct instructions. Third-party retrieval supplies attacker-influenced input, tool interfaces turn altered model decisions into application actions, persistent memory can reintroduce injections, and subsequent searches can reinforce manipulated narratives. These mechanisms are supported by the supplied taxonomy and demonstrations. The paper does not directly compare standalone LLMs and web agents under matched conditions and does not quantify their relative vulnerability.

**Limitations:** AUTHOR-REPORTED: Local HTML replaces public injection, some applications were inaccessible, systematic success-rate and user-persuasion measurement is deferred, Copilot attacks are context-sensitive, and black-box dynamism limits exact reproducibility. ANALYST OBSERVATIONS: Missing total trial counts and full supplied artifacts constrain reliability estimates and reconstruction; prepared synthetic tools do not establish real-network harm; researcher interactions do not measure victim conversion; no matched standalone-versus-agent comparison or evaluated robust defense is supplied.

## One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders

[Summary](summaries/forge_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/One_Polluted_Page_Is_Enough_Evaluating_Web_Content_Pollution_in_Generative_Recommenders.pdf`

**Method:** FORGE freezes ten accepted search documents for each of 225 Chinese product queries across fifteen categories and five scenarios. A three-stage LLM/rule/human pipeline selects brand anchors. Twelve models receive top-three entity replacement at temperature zero; secondary experiments vary rank, count, attack style, language, and reasoning. Audits assess false positives and endorsement; analyses connect evidence-free brand agreement and trace characteristics to vulnerability; defenses are measured alongside legitimate-recommendation removal.

**Attack surface:** Open-web content consumed through search-result evidence bundles. The live threat assumes fake-page publication and indirect SEO visibility; the actual experiments locally manipulate selected documents after retrieval. Default entity replacement preserves original URLs, ordering, and surrounding context. The evaluated asset is recommendation integrity, not credentials, tool execution, purchases, or multi-step agent control.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper helps explain how web-connected recommendation systems acquire an additional attacker-influenced evidence channel, and how plausible polluted content can become an on-task false recommendation with invented justification. It does not directly establish that web AI agents are more vulnerable than standalone LLMs: there is no matched standalone attack comparison, and evidence-free controls measure spontaneous fake-prefix emission rather than equivalent adversarial exposure.

**Limitations:** Local placement bypasses upstream indexing/ranking costs; several experiments cover only open-weights models or Digital Products; English replication uses three fresh categories and changed geography; evidence is a single April 2026 snapshot; attacks are unoptimized; richer attack styles change multiple dimensions. Raw artifacts were not supplied. Important unresolved issues include reasoning-baseline mismatch, Rec/mention scope, and prose claims contradicted by the English and defense tables.

## Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems

[Summary](summaries/retrieval_barrier_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Overcoming_the_Retrieval_Barrier_Indirect_Prompt_Injection_in_the_Wild_for_LLM_Systems.pdf`

**Method:** Adapt the Cross-Entropy Method to optimize a factorized distribution over short token prefixes maximizing cosine similarity between the query and the combined trigger/attack document. Defaults: ten trigger tokens, 5,000 candidates per iteration, thirty iterations, elite fraction .2, smoothing .55. Evaluate eleven BEIR datasets with 100 target queries each; eight embedding models on FiQA; transfer, position, dispersion, cost, RAG, controlled email-agent outcomes, and selected adaptive defenses.

**Attack surface:** Author-reported external-corpus poisoning under embedding-based top-five retrieval. The attacker knows the target query, provides an attack fragment, injects one item, and can query the embedding API without reading the clean corpus or accessing model parameters. Downstream surfaces include answer generation, email sending, contact enumeration, code execution, and inter-agent coordination.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence. The paper supports mechanisms by which retrieval-enabled agents gain additional exposure: attacker-controlled external content can enter context, tools can convert redirected instructions into harmful actions, and agent delegation can amplify code-execution risk. It compares two controlled email-agent configurations for GPT-4o code execution, with adapted payloads and workflows that prevent isolating agent count as the causal factor. It does not directly compare web AI agents with matched standalone LLMs, and its agent experiments concern email workflows rather than web browsing.

**Limitations:** Embedding-only retrieval; no evaluated hybrid search or reranking; uneven cross-model transfer; no standalone-LLM or web-agent control; narrow one-user/ten-FAQ agent setup; adapted multi-agent payloads confound causal attribution; conditional additive-score theorem with missing proof; absent full-version defense and multimodal evidence; inconsistent appendix averages and RAG model counts; no supplied significance tests or independent replication.

## Prompt Injection Attack to Tool Selection in LLM Agents

[Summary](summaries/toolhijacker_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Prompt_Injection_Attack_to_Tool_Selection_in_LLM_Agents.pdf`

**Method:** ToolHijacker constructs shadow queries, shadow documents, and substitute retrieval/selection components. It sequentially optimizes a retrieval-oriented description subsequence R and a selection-oriented subsequence S. Gradient-free selection uses attacker-LLM rewrites, shadow evaluation, pruning, and feedback. Gradient-based optimization uses shadow gradients, retrieval similarity, output alignment, malicious-name consistency, and readability losses. Evaluation covers two datasets, eight target LLMs, four retrievers, baselines, ablations, six automated defenses, human detection, specificity, library expansion, and resource cost.

**Attack surface:** Attacker-controlled tool names and descriptions in a third-party tool library. The malicious document must enter the retrieved top-k shortlist and influence the selection LLM. The assumed attacker knows the task category but cannot inspect or directly query target components. Harmful execution is an assumed possible consequence, not an evaluated deployed outcome.

**Relevance:** ANALYST INFERENCE, HIGH confidence: The paper explains a relevant agent-specific mechanism by which untrusted tool documentation enters retrieval and then influences selection of an external service. This supports discussion of added attack surfaces and potential action consequences in web AI agents. The experiments do not directly compare standalone LLMs with agents, do not specifically benchmark a web-browsing workflow, and do not establish a quantitative relative-vulnerability result.

**Limitations:** Controlled document injection and selection outcomes do not measure deployment feasibility or downstream harm. The paper lacks a matched standalone-LLM comparison. Most ablations use a single task, detector tests use ten malicious documents per dataset, and the human study uses six participants and seven malicious tools. Complete attacker prompts, task lists, code, payloads, seeds, model snapshots, and statistical uncertainty are absent from the supplied material. Detection and dynamic-library reporting contain unresolved text–table inconsistencies, and Algorithm 1 contains literal implementation ambiguities.

## Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search

[Summary](summaries/unsafe_llm_search_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Unsafe_LLM-Based_Search_Quantitative_Analysis_and_Mitigation_of_Safety_Risks_in_AI_Web_Search.pdf`

**Method:** Seven-product manual risk evaluation using 100 malicious-site-derived keyword lists, 100 GPT-4o-generated natural-language questions, and 457 risk-conditioned URL follow-ups; placement-sensitive URL and response labels; questionnaire and query-realism checks; a later 40-query multilingual comparison with Google and Bing; two fictional Perplexity website attacks across eight model choices; and GPT-4.1-based prompt/agent defenses evaluated on 46 selected main-risk responses and 204 accessible classified URLs.

**Attack surface:** Publicly accessible webpages, malicious technical documentation, deceptive official-source claims, retrieved webpage snapshots, answer references, broader source lists, and direct URL follow-up requests. The attacker controls external content and may buy domains, publish sites or public-platform material, and perform SEO; the demonstrated case studies use basic websites without SEO.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains a web-specific exposure mechanism in which attacker-controlled retrieved content becomes generated guidance, code, or source-authority judgments. Its direct URL follow-ups show that less-visible malicious sources can become prominent answer content. It does not experimentally establish that web AI agents are more vulnerable than matched standalone LLMs, and its traditional-search comparison addresses a different baseline.

**Limitations:** Manual, relatively small-scale, malicious-derived sampling; time-sensitive websites; unresolved annotation assigned none risk; incomplete frozen product configurations; no repeated-run uncertainty or standalone-model baseline; provider disclosure before the later comparison; Perplexity-only constructed attacks; warning conversion rather than measured harm prevention; defense exclusion of direct URL queries; unavailable private data and exact HtmlLLM prompt; incomplete training details; and unresolved numerical/reporting inconsistencies.

## VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents

[Summary](summaries/vpi_bench_visual_prompt_injection_attacks_for_computer_use_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/VPI-Bench_Visual_Prompt_Injection_Attacks_for_Computer-Use_Agents.pdf`

**Method:** An interactive benchmark of 306 cases across five reconstructed platform types, divided into 219 Computer-Use and 87 Browser-Use cases. Eight main framework/model configurations are evaluated on their respective subsets, with three-run attempted/success means and standard deviations. Three LLM judges provide majority-vote labels, validated against manual labels on 100 logs. Separate analyses examine behavior categories, early/late injection, a system-prompt defense, reply-versus-summary semantic context, and UI-TARS 7B execution limitations.

**Attack surface:** Rendered webpage pop-ups, chat messages, and emails encountered during benign delegated tasks. Prompts are visually available to screenshot-based agents and can also be present in HTML for browser agents. Downstream assets include local files, terminal commands, applications, cloud Drive data, and messaging/email actions. The modeled attack requires content-placement capability rather than a platform breach, and assumes no continuing human supervision.

**Relevance:** Analyst inference, MEDIUM confidence: the paper helps explain agent-specific security exposure through malicious environmental instructions, delegated resource access, and multi-step execution. It shows how instruction-following errors can become private-data transfers, file operations, communications, or command execution. It does not directly compare web agents with standalone LLMs, quantify that difference, or isolate the contribution of autonomy, tools, perception modality, and framework defenses. The user's research-question title appears as a cited work on page 12 and is not this paper's title.

**Limitations:** Explicit author limitation: users may notice malicious content and intervene, unlike the unsupervised study assumption. Analyst observations: no standalone-LLM control; confounded CUA/BUA and defense comparisons; reconstructed interfaces and synthetic data; incomplete settings and sample-size reporting for some analyses; imperfect model judging; no formal significance tests supplied; execution failure can conceal susceptibility; tiny graphical values remain uncertain; external artifacts and unreported experiments were not reviewed.

## WAAA! Web Adversaries Against Agentic Browsers

[Summary](summaries/waaa_web_adversaries_against_agentic_browsers_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WAAA_Web_Adversaries_Against_Agentic_Browsers.pdf`

**Method:** Expert-guided extension of See→Act and traditional web attacker models; search-based browser capability discovery; independent review and consensus mapping of dimension combinations; 18 proof-of-concept scenarios evaluated primarily with Playwright-MCP and BrowserOS; selected commercial cases; four BrowseSafe confusion examples; repeated model trials with 10 runs per tested condition. Four model columns are supplied, but only 13 numeric attack rows appear despite a claim of 14 generalized attacks.

**Attack surface:** Four capability classes—page interaction, navigation, browser UI, and integration—combined with HTML or screenshot input, gadget/markup or full-page/script attacker control, and same-site, cross-site, or system targets. Five failure modes organize 20 categories: same-site bridging, cross-site bridging, URL hallucination, LLM/prompt exposure, and integrated-tool misuse.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains mechanisms relevant to why web AI agents can face risks beyond standalone LLMs—attacker-controlled observations influence an authorized agent that can bridge sites, act on private data, and invoke external tools. It does not directly compare standalone LLMs with web agents. The user's research-question title is the title of a separate work cited as reference [25], whose contents were not supplied.

**Limitations:** Selected crafted scenarios and capability-dependent configurations; absent full artifacts; incomplete sampling and detector settings; no statistical uncertainty estimates or standalone-LLM baseline; inconsistent taxonomy/generalizability bookkeeping; partial visual coverage; evolving prompts/tools; proposed defenses are not evaluated. Unsupported capabilities and action-execution failures must not be interpreted as proven model-level security.

## WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers

[Summary](summaries/webcloak_characterizing_and_mitigating_threats_from_llm_driven_web_agents_as_intelligent_scrapers_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WebCloak_Characterizing_and_Mitigating_Threats_from_LLM-Driven_Web_Agents_as_Intelligent_Scrapers.pdf`

**Method:** Construct 237 offline pages from 50 websites with 10,895 annotated images; screen 32 variants across L2S/LNC/LWA on five pages; characterize three representatives across the benchmark; evaluate dynamic structural obfuscation plus iteratively optimized semantic cues against baselines, task instructions, backends, adaptation, prompt removal, environments, usability, and overhead.

**Attack surface:** Page HTML/DOM, conventional image tags and source attributes, parser simplification and Markdown conversion, hidden pre/post elements and image alt text, rendered browser representations, and client-side restoration. The attacker in the paper is a malicious scraper operator; the website owner uses structural and semantic interference defensively.

**Relevance:** MEDIUM confidence, analyst inference: the paper shows how webpage preprocessing and LLM interpretation create agent-specific dependencies and opportunities for hidden contextual redirection. This is relevant to explaining additional attack surfaces in web-connected systems. It studies agent-as-attacker scraping and defensive interference, however, and does not directly compare matched web agents with standalone LLMs. Comparative vulnerability magnitude is UNKNOWN from the supplied work.

**Limitations:** Novice/intermediate scalable-attacker scope; local offline snapshots; JavaScript-dependent restoration; expert reverse engineering remains possible; ten-page audio/text extension; small human studies; absent statistical uncertainty and detailed version/configuration information; unresolved numerical inconsistencies; no direct standalone-LLM comparison; underlying artifacts not supplied.

## WebInject: Prompt Injection Attack to Web Agents

[Summary](summaries/webinject_prompt_injection_attack_to_web_agents_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WebInject_Prompt_Injection_Attack_to_Web_Agents.pdf`

**Method:** Train a U-Net mapping approximation for each target monitor, replace resizing with a differentiable surrogate during optimization, minimize target-action negative log probability with projected gradient descent under an infinity-norm bound and shared-visible-region mask, then implement the perturbation in webpage rendering code while retaining transparent original interactive elements.

**Attack surface:** Rendered visual observations originating from attacker-controlled webpage source code. The attacker changes raw webpage pixels through injected code; screenshots and genuine local histories remain outside the attacker's direct access. The evaluated model parameters are accessible to the attacker.

**Relevance:** Analyst inference, MEDIUM confidence: the paper shows how attacker-controlled webpages introduce a visual environmental input pathway into screenshot-based agents and how influence can target operational action strings. This is relevant to explaining additional exposure and consequences in web agents. It does not directly compare web agents against standalone LLMs, establish that agents are universally more vulnerable, or quantify a relative vulnerability rate.

**Limitations:** Requires target-page source modification and white-box MLLM access; closed-source transfer is explicitly untested. Evaluation uses selected real/synthetic snapshots, generated prompts, random histories, and exact action output. Human perceptual stealth, downstream harmful execution, unseen-environment robustness, and statistical uncertainty are not established. Phi-4 aggregation, prompt-generator identity, image dimensions, and optimization granularity contain unresolved inconsistencies or ambiguities.

## When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins

[Summary](summaries/when_ai_meets_web_comprehensive_summary.md) · Source: `04_Adversarial_Web_Prompt_Injection_Content_Manipulation/When_AI_Meets_the_Web_Prompt_Injection_Risks_in_Third-Party_AI_Chatbot_Plugins.pdf`

**Method:** Selection of 7 WordPress and 10 generic plugins; HTML-marker discovery in Common Crawl; functionality checks; local protocol and scraper inspection; selected live P1 prompt, review-exposure, and tool measurements; an 11-model local simulation with three prompt designs, supported injection roles, five RAG insertion modes, wrapping conditions, and 10 trials per configuration at temperature 0.5; small prototype-defense evaluations.

**Attack surface:** Browser-supplied HTTP conversation histories; fabricated assistant and system messages; scraped reviews and comments; persistent RAG knowledge; privileged retrieved-content insertion; Search and Notification tools; leaked tool metadata, system prompts, and an API key. The threat model excludes unrelated classical web exploits.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper explains how web integrations can amplify an underlying LLM's vulnerabilities by allowing forged privileged roles, ingesting third-party content into trusted context, and exposing tools to adversarial argument selection. Controlled role and insertion comparisons support these mechanisms. The paper does not report an otherwise matched standalone-LLM versus web-agent adversarial comparison, and its findings should not be generalized to every agent architecture.

**Limitations:** Selected-plugin and crawl coverage, P1-centered live measurements, heuristic live leakage labeling, model-dependent role inference, failed deployed-model fingerprinting, limited non-adaptive proof-of-concept attacks, one product-domain simulation, two evaluated tools, ten trials without reported statistical uncertainty, absent implementation details, unresolved prose/table discrepancies, and unclear adaptive robustness of defenses. Current vulnerability status was not verified.

## AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks

[Summary](summaries/agentlab_benchmarking_llm_agents_against_long_horizon_attacks_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/AgentLAB_Benchmarking_LLM_Agents_against_Long-Horizon_Attacks.pdf`

**Method:** A modular benchmark with agent, environment, task, and attack components; 28 environments and 644 malicious tasks; five attack families; coordinated planner, attacker, judge, and optional verifier; adaptive task injection with bridge actions and exemplar retrieval; two-phase memory poisoning; six target model families; ASR and success-conditional T2S; one-shot comparison, turn/optimization ablations, and baseline defense evaluation.

**Attack surface:** User instruction interfaces; webpage and search-result text; product descriptions and reviews; email and document content; repository comments; API/tool outputs; automatically extracted persistent preferences; and, in the task-injection implementation, attacker-visible tool trajectories and intermediate reasoning.

**Relevance:** MEDIUM confidence; analyst inference. The paper provides mechanisms relevant to why web AI agents may face additional security exposure: repeated contact with attacker-controlled environmental text, tool-mediated actions, harmful composition across steps, gradual goal changes, and persistent poisoned memory. It empirically compares attack strategies on agents, not matched standalone LLMs against web agents, so it does not establish the magnitude or universal existence of that comparative vulnerability gap.

**Limitations:** Preliminary evaluation without a matched standalone baseline, reported uncertainty intervals, repeated-run counts, exact per-condition allocations, complete prompts, or full target version identifiers. The supplied material contains unresolved category-count, aggregation, and Llama-result discrepancies. Some attacks assume privileged reasoning access, memory settings differ from defaults, frugality is undefined, and separate artifacts were not reviewed.

## AI Agent Traps

[Summary](summaries/ai_agent_traps_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/AI_Agent_Traps.pdf`

**Method:** Conceptual functional-architecture taxonomy and narrative literature synthesis. Six overlapping families target perception, reasoning, memory/learning, action, multi-agent dynamics, and human oversight. Mechanisms are illustrated using prior studies and scenarios; mitigation pathways and evaluation priorities are proposed. No reproducible systematic-search protocol or original controlled experiment is reported.

**Attack surface:** AUTHOR-REPORTED: Webpages and other digital resources; hidden HTML/CSS/metadata; dynamically cloaked responses; media and formatting syntax; retrieved corpora; persistent memory; demonstrations and feedback; emails, pop-ups, and API/tool responses; delegated control flow; shared environmental signals; counterfeit agent identities; human-facing outputs.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The taxonomy explains additional attack paths when web agents ingest externally controlled content, use privileged tools, preserve memory, adapt from context, delegate, interact collectively, or influence human approval. It does not directly compare matched standalone LLMs and web agents or quantify a comparative vulnerability increase.

**Limitations:** Uneven research maturity; some systemic and human-targeted mechanisms remain theoretical or preliminary; compositional fragment traps are explicitly more hypothetical; delegation mechanisms need further work; suggested defences are not evaluated. Secondary empirical outcomes use different tasks, privileges, metrics, and conditions and cannot be pooled. Direct visual review covers five supplied pages, while all 25 pages were reviewed as text.

## Breaking Agents: Compromising Autonomous LLM Agents Through Malfunction Amplification

[Summary](summaries/breaking_agents_compromising_autonomous_llm_agents_through_malfunction_amplification_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Breaking_Agents_Compromising_Autonomous_LLM_Agents_Through_Malfunction_Amplification.pdf`

**Method:** Empirical security and robustness study using an LLM-emulated sandbox with 144 test cases, a reported 36 toolkits and more than 300 tools, plus implemented LangChain Gmail and CSV agents. Compares infinite-loop and incorrect-function goals; prompt injection, SCPN/VIPER/GCG perturbations, and adversarial demonstrations; three core LLMs; tool properties; entry surfaces; two multi-agent workflows; and policy versus malfunction self-examination. ASR is failed-task percentage assessed through agent self-reflection.

**Attack surface:** Author-reported: direct user instructions, intermediate tool outputs such as received email and CSV content, and agent memory. Advanced scenarios transmit attack-bearing outputs from an attacker-controlled upstream agent to downstream agents. Susceptibility is conditional: Gmail external content is effective in tested cases, CSV external content and listed memory attacks are not.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains mechanisms relevant to why web-connected AI agents can have greater exposure and more consequential failures than text-only LLM use: extra component-mediated entry points, autonomous tool execution, iterative planning, and downstream agent communication. It does not experimentally compare matched standalone LLMs and agents or establish universal greater vulnerability.

**Limitations:** Author-stated limitations include two implemented agents, three core model variants, restricted agent categories, potential self-reflection errors, and emulator uncertainty for actual tool reactions. Analyst observations include missing matched standalone baselines, per-cell denominators, uncertainty statistics, model snapshots and runtime details, unequal toolkit representation, limited memory-dependent testing, no measured resource or propagation scaling, and no end-to-end protected-task evaluation. Text-only coverage applies to six pages; plot estimates and several text–table inconsistencies remain disclosed.

## Context manipulation attacks : Web agents are susceptible to corrupted memory

[Summary](summaries/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Context_manipulation_attacks_Web_agents_are_susceptible_to_corrupted_memory.pdf`

**Method:** Empirical evaluation of Agent-E and Browser-use using a four-category Plan Injection Benchmark with 15 samples per category and five executions per sample, plus 45 WebVoyager-Privacy scenarios across nine domains. Compares non-contextual, task-aligned, and context-chained attacks; weak/strong retrieved-content prompt attacks; and Undefended, SECURE, and SECURE+SANDWICH configurations. Uses GPT-4o controller/planner components, GPT-4o-mini browser navigation as described, headless execution, and attack success rate with partial/full privacy outcomes.

**Attack surface:** Stored execution context and high-level task plans, alongside a general taxonomy covering user prompts, retrieved external data, and interaction history. The restricted context attacker cannot alter the original user instruction, browser observations, system prompts, or code. Acquiring storage write access is assumed or motivated through possible deployment scenarios, not experimentally quantified.

**Relevance:** MEDIUM confidence, ANALYST INFERENCE: The paper supplies a mechanism relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis': multi-step agents depend on mutable application-managed context, and corrupted plans/history can lead to unauthorized browser actions despite tested retrieved-content prompt defenses. It does not directly compare a standalone-LLM baseline with web agents. The similarly titled Chiang et al. work is only a cited reference, not the supplied target paper.

**Limitations:** No direct standalone-model comparison, controlled architecture ablation, confidence intervals, or reported statistical tests. Privacy-suite repetitions, exact prompts, model snapshots, grading implementation, and injection interfaces are unspecified. Linked benchmark artifacts are unavailable. Figure 5 conflicts with the blanket undefended greater-than-80-percent statement for weak-prompt bars. Headline percentages do not consistently identify partial versus full success. The similarity analysis is descriptive and subset-based; proposed stronger-model and memory-integrity defenses are not comprehensively evaluated.

## Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

[Summary](summaries/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Hidden_in_Memory_Sleeper_Memory_Poisoning_in_LLM_Agents.pdf`

**Method:** Reusable actor–critic payload optimization; constrained embedding-oriented goal rewriting; 700 injection pairs; 400 standardized downstream samples; two writing regimes; full-context, LLM-managed, and top-k semantic retrieval; six principal target models; conditional IR/RR/AUR and five-model coupled end-to-end compositions; four prompt defenses, scanners, benign-save checks, activation probes, attention analyses, wording/position/language ablations, selected production transfer, and provider/manager swaps.

**Attack surface:** Author-reported external contexts include webpages, uploaded/shared documents, emails, repositories, transcripts, and workspace files. The targeted asset is the integrity of persistent user memory and later behavior. The attacker lacks direct memory-store access and is absent from future sessions. External writing can additionally launder adversarial claims through the target assistant's completion into a separate extractor.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper explains a specific route through which externally exposed, memory-enabled, tool-using agents can incur additional risk: untrusted content becomes durable user state, later retrieval gives that state renewed influence, and tool access translates contextual assimilation into operational pursuit. This supports mechanisms relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis.' It does not directly compare matched standalone LLMs and web agents or establish a general vulnerability ratio.

**Limitations:** Author limitations include judge disagreement, reconstructed provider pipelines, single-document scope, and omitted deletion/correction/review/provenance defenses. Analyst observations include standardized-memory fallback, broad action-uptake scoring, selected production validation, bundled setup effects, incompletely specified probe grouping and operational detector costs, estimated semantic end-to-end rates, unresolved text/table/figure discrepancies, and absent supplementary artifacts. All supplied text was inspected; visual inspection was limited to the 56 supplied rendered pages.

## How Adversarial Environments Mislead Agentic AI?

[Summary](summaries/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/How_Adversarial_Environments_Mislead_Agentic_AI.pdf`

**Method:** POTEMKIN intercepts tool responses using an MCP-compatible server or Python integration, serves frozen snapshots, and applies seeded transformations. Five original agents are evaluated across contamination, linguistic style, matched hedge/booster framing, cycle length, plausibility, and clean baselines; analyses include engagement conditioning, Llama-3 Reflexion, SHAP, cross-dimension logistic-regression transfer, five-model frontier validation, and exploratory defenses.

**Attack surface:** Compromised runtime tool outputs: poisoned search snippets and retrieved evidence for breadth attacks; fabricated paper metadata, entry points, and directed reference connections for depth attacks. The stated attacker cannot access model weights, system prompts, or internal state.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains additional vulnerabilities introduced when agents trust external observations and repeatedly navigate tool-provided structures. This is relevant to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' but the work does not directly compare matched standalone LLMs with web agents, and empirical validation on general web-search agents remains future work.

**Limitations:** Citation-graph domain, no standalone-model comparator, restricted independent-verification assumption, heterogeneous agent interfaces and scaffolds, API exclusions, incomplete condition-level and statistical documentation, absent release artifacts, and unresolved figure/table/prose inconsistencies. Figures A1–A2 were text-only in the supplied material; all other identified figures had supplied images. Supplemental analyst review visually confirmed Figure A2/Table A5 inconsistencies on physical pages15–16; no reconciliation is inferred.

## It’s a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents

[Summary](summaries/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Its_a_TRAP_Task-Redirecting_Agent_Persuasion_Benchmark_for_Web_Agents.pdf`

**Method:** AUTHOR-REPORTED, HIGH confidence: REAL-based browser-agent evaluation with AXTree observations and Playwright actions; 18 benign tasks paired with 35 templates formed from seven persuasion principles and five manipulation methods, yielding 630 combinations per original model and 3,780 attacked runs across six models. Separate analyses examine source-conditioned transfer, component composition, paired interface form, location/targeting, and light tailoring. The main metric is initial clicked redirection, alongside separate benign utility.

**Attack surface:** AUTHOR-REPORTED, HIGH confidence: textual prompt injections placed in selected user-editable fields of six deterministic website clones, including email content, event fields, reviews, posts, and profile text; injected buttons or hyperlinks trigger navigation to a designated attacker-controlled destination. Image injection is supported by the framework but excluded from this study.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper explains a plausible added-risk mechanism for web agents through third-party editable content, executable browser controls, repeated observation–action cycles, task-dependent exposure, and redirection into attacker-controlled context. It does not directly compare matched standalone LLMs with browser-agent versions and cannot quantify a vulnerability increase attributable solely to agentization.

**Limitations:** AUTHOR-REPORTED and ANALYST OBSERVATIONS: cloned/synthetic environments, textual focus, narrow task sample, one principal full-dataset run, selected small-sample tailoring, no evaluated defenses, initial-redirection rather than downstream-harm measurement, hosted-model reproducibility limits, and changed environments for newer-model results. ANALYST OBSERVATION, MEDIUM confidence: Tables 5 and 15 do not reconcile on location aggregation. HIGH confidence: no matched standalone comparison or independent inspection of the referenced repository was supplied.

## Mind the Web: The Security of Web-Use Agents

[Summary](summaries/mind_the_web_the_security_of_web_use_agents_5a834c4e_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web-Use_Agents.pdf`

**Method:** AUTHOR-REPORTED — HIGH confidence: Approximately 2,000 candidate injections for P4/P5/P6/P8 are generated at temperature 1.6, tested through Browser-Use with GPT-4o or Gemini-2.0-Flash, and scored by GPT-5. Approximately 400 score-qualified examples support SFT of Qwen-3-4B-Instruct, followed by DPO on ordered candidates. Fine-tuning is offline after preprocessing. Evaluation reports 100 trials per experiment, selected payload/model transfer, scaling, expert judge validation, and manual demonstrations on four additional agents.

**Attack surface:** AUTHOR-REPORTED — HIGH confidence: Visible third-party comments, reviews, advertisements, posts, emails, shared documents, and image content can influence the agent's perception and planning. Resulting harms depend on available sessions, stored credentials, pre-granted camera/microphone permissions, or local-file access. P5/P6/P8/P9 have no additional payload-specific prerequisite in Table 2, beyond encountering the injected content.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper helps explain additional exposure and harm when an LLM reads attacker-controlled web content and executes actions with delegated browser privileges. It supports a mechanism-based account of vulnerability amplification, not a measured claim that web agents are more susceptible than matched standalone LLMs. Its base-model comparisons concern injection generators, not standalone victim models.

**Limitations:** HIGH confidence for source boundaries; MEDIUM confidence for analyst validity observations: No matched standalone-LLM comparison, no reported ASRs for P2/P3, no quantitative rates for every agent, two controlled training/evaluation environments, incomplete split/version/hyperparameter details, no ASR uncertainty intervals, and no numerical defense benchmark. Main text and appendix differ on judge sampling and positive-fulfillment precision; threshold equality and example scoring are inconsistent. Visual coverage is partial, and no external code or supplementary artifacts were reviewed. Version-family qualification (analyst observation from authorized corpus identity review): this published 17-page PDF and the separately cataloged 13-page manuscript Mind the Web: The Security of Web Use Agents are versions of the same study, not independent replications. Preserve version-specific results: this version reports approximately 2,000 candidates, approximately 400 SFT examples and 64%/85% SFT/DPO ASR; the manuscript reports 1,500 candidates, approximately 300 examples and 61%/82%. Repeated payload-transfer rates across versions must not be counted as independent experiments.

## Mind the Web: The Security of Web Use Agents

[Summary](summaries/mind_the_web_the_security_of_web_use_agents_comprehensive_summary.md) · Source: `05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web_Use_Agents.pdf`

**Method:** AUTHOR-REPORTED: Task-aligned injection; three-stage candidate generation, agent-execution/LLM-judge validation, and offline SFT followed by DPO. Qwen3-4B-Instruct generates approximately 1,500 candidates for four payload classes; approximately 300 successful examples and 12,000 preference pairs support training. Quantitative method and payload tests are supplemented by backend-model transfer tests and manual cross-agent demonstrations.

**Attack surface:** AUTHOR-REPORTED: Third-party comments, reviews, advertisements, posts, emails, shared documents, and text/image content encountered during benign browsing. Assets and consequences depend on deployment architecture, authenticated state, camera/microphone permissions, local-file access, and autonomous execution.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper explains how autonomous browser execution combines LLM instruction susceptibility with repeated exposure to attacker-controlled web content, authenticated sessions, navigation, forms, and sometimes local-resource permissions. These features broaden exposure and potential harm compared with a standalone text responder. The paper does not conduct a matched standalone-LLM-versus-web-agent victim comparison, so it does not establish a universal susceptibility ranking or quantitative vulnerability ratio.

**Limitations:** No matched standalone victim comparison; no separate quantitative ASR for every agent product; selected controlled environments and open-ended tasks; LLM-judged success without reported calibration; inconsistent 0.5 boundary; Claude version ambiguity; manual adaptation in the Operator P9 example; completed file delivery not independently established; proposed defenses not quantitatively evaluated; missing detailed splits, uncertainty estimates, software versions, and training settings. Visual coverage is pages 1–12, with page 13 reviewed as text only. Version-family qualification (analyst observation from authorized corpus identity review): this 13-page manuscript and the separately cataloged published 17-page Mind the Web: The Security of Web-Use Agents are versions of the same study, not independent replications. This manuscript reports approximately 1,500 candidates, approximately 300 SFT examples, approximately 12,000 preference pairs and 61%/82% SFT/DPO ASR; the published version reports approximately 2,000 candidates, approximately 400 SFT examples and 64%/85%. Repeated payload-transfer rates must not be counted as independent experiments. Published judge calibration and implemented defense observations must not be imported into this manuscript.

## Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents

[Summary](summaries/autonomy_comes_with_costs_detecting_denial_of_service_vulnerabilities_caused_by_resource_abusing_in_llm_based_agents_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/Autonomy_Comes_with_Costs_Detecting_Denial-of-Service_Vulnerabilities_Caused_by_Resource_Abusing_in_LLM-based_Agents.pdf`

**Method:** Directed grey-box fuzzing: static source analysis identifies memory/disk sinks, classifies resource lifecycles, and filters candidates by input influence and size constraints. Runtime system-prompt capture informs LLM seed generation. CFG proximity, semantic scores, resource consumption, and selection frequency guide scheduling; Explorer and Exploiter mutations refine tool reachability and resource intensity. Lifecycle-aware dispatch and an availability oracle produce reports, followed by manual confirmation.

**Attack surface:** Ordinary remote prompt interfaces to benign, uncompromised agent applications; user-influenced download, parsing, container-growth, tool-output, logging, and disk-write operations. Exhaustion may occur within one request, across turns in one session, or across sessions depending on cleanup timing. Detector source access is distinct from attacker capabilities.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper explains how web-accessible agents add tool execution, memory buffers, downloaded files, and lifecycle-dependent retention to LLM inference, creating additional resource-exhaustion attack surfaces. It does not directly compare standalone LLMs with agents, measure a relative vulnerability rate, or establish that agents are universally more vulnerable.

**Limitations:** Source access is required; black-box adaptation is proposed rather than evaluated. The corpus contains 20 selected open-source web agents using GPT-4.1 and minimum/fallback Docker resources. Recall is based on 38 constructed verified cases, with sampled false-negative review, a 20-minute per-site cap, and early-stop heuristics. Missing reproduction details and source inconsistencies are disclosed. Referenced artifacts and external citations were not reviewed.

## Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents

[Summary](summaries/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/Beyond_Max_Tokens_Stealthy_Resource_Amplification_via_Tool_Calling_Chains_in_LLM_Agents.pdf`

**Method:** Phase-gated Monte Carlo Tree Search over localized text edits, reusable seed templates, two-stage rollout evaluation, and a template-governed progression/validation/termination mechanism. Six target LLMs are evaluated on filtered ToolBench and BFCL tasks using a shared Qwen-Agent-based emulator, vLLM, eight H200 GPUs, fixed concurrency 25, and a 16,384-token completion cap per generation.

**Attack surface:** MCP tool-server text-visible fields and intermediate progress/repair responses after legitimate tool invocation. The stated attacker does not alter the user query, prompts, retrieval, target model, or agent policy; terminal benign payload semantics are retained.

**Relevance:** MEDIUM confidence, analyst inference: the paper identifies an additional agent vulnerability mechanism in which externally supplied tool feedback steers repeated decisions and verbose generations while preserving a correct final answer. It supports a process-level explanation relevant to web agents that use comparable tool loops. It does not directly compare standalone LLMs with web agents, evaluate live browser attacks, or establish a universal vulnerability ranking.

**Limitations:** Controlled emulator, deterministic placeholder tool results, originally single-tool/single-turn benchmark subsets, one principal runtime/hardware configuration, no inspected reproduction artifacts, incomplete numerical search configuration, no final-run uncertainty reporting, and no direct standalone-versus-web-agent experiment. Some headline statements are broader than individual table cells.

## Denial of wallet—Defining a looming threat to serverless computing

[Summary](summaries/denial_of_wallet_defining_a_looming_threat_to_serverless_computing_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/Denial_of_wallet_Defining_a_looming_threat_to_serverless_computing.pdf`

**Method:** Exploratory security and systems study combining a threat taxonomy, a four-desktop isolated OpenFaaS/Apache environment, ModSecurity and Snort protection, a Python pricing emulator, a one-hour unprotected LOIC flood, a qualitative protected rerun, five image-size conditions with five runtime tests each on AWS Lambda at 512 MB, and theoretical four-provider cost projections using a 2950-ms benchmark.

**Attack surface:** Author-reported: exposed or leaked function API endpoints, application-mediated function triggers, user-account creation and authenticated functionality, storage-upload events, input-processing workloads, and adaptive traffic defenses. The target asset is the application owner's finances; false usage analytics are an additional hypothesized harm.

**Relevance:** Analyst inference, MEDIUM confidence: the paper identifies a financial attack mechanism potentially relevant when web AI agents perform actions that trigger paid backend functions. Automated application interactions, fake users, large inputs, and repeated requests can translate into resource consumption and charges. The paper supplies no AI-agent or LLM evaluation and does not establish that web AI agents are more vulnerable than standalone LLMs.

**Limitations:** Preliminary study with author-reported absence of known historical attacks; local platform behavior and modeled billing are not validated against sustained commercial attacks. Quantitative protected-run evidence, full pricing formulas, raw traces, exact image geometry, and detailed hardware are absent. Long-term stealth, fake-user abuse, and proposed detection methods are not experimentally established. Visual coverage is partial by page but includes all numbered figures and the table.

## Overthinking Loops in Agents: A Structural Risk via MCP Tools

[Summary](summaries/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/Overthinking_Loops_in_Agents_A_Structural_Risk_via_MCP_Tools.pdf`

**Method:** Normal-versus-mixed registry comparisons in ReAct and Qwen-Code; attack-only versus mixed ReAct comparison; NoWait-enabled normal-versus-mixed comparison. ReAct uses 100 benign tools plus 14 attack additions on AIME2025, GPQA Diamond, and HumanEval. Qwen-Code uses 44 benign tools plus 14 attack additions on seven CodeElo problems retained from ten sampled tasks after all-model baseline screening. Five repetitions, 1,000-turn session limits, and tool-call depth 20 per turn are reported. Metrics are total input/output tokens, accuracy, and Qwen-Code runtime.

**Attack surface:** MCP tool registries, provider-controlled names/descriptions/schemas, and returned messages incorporated into subsequent model context. Fourteen attack tools across three servers induce repetition, refinement cycles, and distraction. The experimentally threatened assets are token budgets, runtime, and task completion; exfiltration is mentioned as background rather than tested.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains an additional agent exposure channel through third-party tool metadata and runtime outputs that influence repeated action selection and accumulate resource costs. This mechanism is relevant to web AI agents when they possess comparable tool orchestration. The paper does not directly compare standalone LLMs with web agents, isolate browser interaction, or establish a universal quantitative vulnerability difference.

**Limitations:** Narrow reasoning/programming task scope, seven screened CodeElo tasks, mostly autonomous configurations, exclusion of proprietary production APIs, and only one systematically tested defense family. No uncertainty intervals, full traces, prompts, seeds, executable attack code, detailed scoring procedures, or complete stop thresholds are supplied. Headline aggregation, GLM version differences, and NoWait cardinality/notation remain unresolved. Pages 7–9 are text-only; all four figures and six tables have supplied visual coverage.

## RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks

[Summary](summaries/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/RecurGuard_Runtime_Monitoring_for_Reasoning-Token_Consumption_Attacks.pdf`

**Method:** RecurGuard embeds non-overlapping 64-word exposed reasoning chunks using normalized 384-dimensional all-MiniLM-L6-v2 vectors. It combines recurrence over a 20-chunk window, change in mean pairwise distance, and query similarity minus maximum similarity to all prior chunks. It triggers after three consecutive joint alarms with RR>0.20, VG<0.01, TP<−0.738 and chunk index at least 3. Benign-only calibration uses 50 SQuAD traces plus 30 each from three long-form tasks. QDM is an attack-informed, post-hoc fallback using mean query similarity of 80-word final-output chunks and a 0.318 cutoff.

**Attack surface:** Text-bearing inference context D, including retrieved documents, tool outputs, user-controlled inputs, and external strings. The attacker can choose token-consuming decoys and know the general defense design, but cannot modify model weights, decoding parameters, the system prompt directly, or the detector, and has no gradient access. The harm is excessive output-token consumption and possible failure to return a usable answer.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains how attacker-controlled web pages, retrieved documents, and tool outputs can introduce benign-looking but computationally expensive instructions into reasoning context. This supports a mechanism relevant to web-agent exposure and resource exhaustion. It does not directly compare standalone LLMs with matched web agents, measure the incremental risk of browsing, or establish that web agents are universally more vulnerable. End-to-end RAG deployment testing is explicitly future work.

**Limitations:** Requires nonempty exposed reasoning and streaming/cancellation for token savings; summarized reasoning lowers sensitivity and hidden reasoning makes RecurGuard inapplicable. C1 retains 11.9× amplification with approximately 50% joint miss on the primary model. C4 fully evades both semantic monitors at 2.2× amplification, which remains overhead. Adaptive transfer is unestablished, white-box optimization is excluded, B2 is a compression proxy, full long-form profiles reuse some calibration examples, and supplementary/repository results were not inspected. The paper does not provide a direct standalone-versus-web-agent comparison.

## When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents

[Summary](summaries/when_agents_do_not_stop_uncovering_infinite_agentic_loops_in_llm_agents_comprehensive_summary.md) · Source: `06_Resource_Exhaustion_Availability_Denial_of_Wallet/When_Agents_Do_Not_Stop_Uncovering_Infinite_Agentic_Loops_in_LLM_Agents.pdf`

**Method:** Python static analysis using project indexing and AST extraction, framework-independent Agent IR, ALDG construction, SCC-based feedback candidate discovery, controller classification, effective bound-coverage verification, benign-loop filtering, optional evidence-constrained LLM negative pruning, and manual author confirmation. Eight frameworks are modeled. The corpus contains 6,549 starred Python downstream repositories; RQ2/RQ3 use 264 candidate-containing projects.

**Attack surface:** AUTHOR-REPORTED: normal prompts, task requests, documents, URLs, issue reports, tickets, workflow parameters, and API inputs can influence model outputs, tool arguments, retrieved content, external observations, and errors. Source code, framework configuration, deployment environment, and trusted tools are outside attacker modification powers. The analyzed failure concerns structurally visible unbounded agentic feedback and resource/availability amplification.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper explains an added security mechanism in agent systems—untrusted inputs can influence model outputs, tools, observations, state updates, retries, and delegation, creating feedback that amplifies a request into repeated costly execution. This is relevant to web agents receiving URLs, documents, and retrieved content. The paper does not directly compare web agents with standalone LLMs or quantify their relative vulnerability.

**Limitations:** Author-stated limitations include static over-approximation, restricted language/framework coverage, limited custom stopping semantics, and unstable or incomplete LLM pruning. Analyst observations include absent artifacts, a candidate-selected comparison subset, constrained baseline access, incomplete global ground truth, no measured live attack/resource-loss outcomes, and no standalone-versus-web-agent vulnerability experiment.

## AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

[Summary](summaries/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/AgentDojo_A_Dynamic_Environment_to_Evaluate_Prompt_Injection_Attacks_and_Defenses_for_LLM_Agents.pdf`

**Method:** HIGH confidence for described design: four synthetic mutable environments; 97 legitimate tasks, 27 injection targets, and 629 within-suite paired cases; executable Python tools; deterministic output/state checks; ten-model baseline comparison; GPT-4o attack-template, name-knowledge, defense, denial-of-service, and positional analyses. Tables 3–5 report 95% confidence intervals. Code and reproduction assets are described but not inspected.

**Attack surface:** HIGH confidence, author-reported: indirect prompt injections in designated third-party-data placeholders reached through tool outputs, including email, web pages, files, and application content. Consequences include malicious messages, information exfiltration, inappropriate bookings, and transactions. Attacker knowledge and controlled-output fraction vary; operating-system or model-weight compromise is not evaluated.

**Relevance:** MEDIUM confidence, analyst inference: AgentDojo explains a consequential exposure pathway relevant to web AI agents—untrusted pages and other tool outputs can influence planning and trigger user-privileged actions. Its dynamic, stateful evaluation and tool-filter results help separate text influence from available action capabilities. The paper does not directly compare matched standalone LLMs and therefore does not establish or quantify that agents are more vulnerable.

**Limitations:** HIGH confidence for explicit boundaries and observed discrepancies: relatively simple attacks/defenses, manual task/check construction, synthetic text-only state, omitted persistent multi-task contexts, tool-filter failure when needed capabilities also enable attacks, and a requirement for strong adaptive evaluation. No standalone control exists. Tool counts, baseline rates, Figure 8/Table 4 values, and tool-filter prose/table rates conflict. Run-level settings and supplementary artifacts are unavailable in this analysis.

## Formalizing and Benchmarking Prompt Injection Attacks and Defenses

[Summary](summaries/formalizing_prompt_injection_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf`

**Method:** Formal target/injected-task definition and compromised-data construction A(x^t,s^e,x^e); five heuristic attack strategies; ten LLMs; seven NLP tasks and 49 target/injected combinations; disjoint pools of 100 target and 100 injected examples per task; 100 sampled pairs for ASV/MR/FNR; five prevention and five detection defenses; task-dependent accuracy, GLEU, and Rouge-1 scoring. Detailed five-attack plots cover GPT-4 and PaLM 2, and default defense experiments chiefly use GPT-4, with Llama-2-13b-chat for PPL detection.

**Attack surface:** Application-consumed external data, including résumés, social-media posts, and hosted webpages. The benchmark assumes arbitrary instruction/data insertion, unknown application internals, no required black-box victim access during payload construction, no target-instruction modification, and intact backend LLMs.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains a mechanism relevant to web-agent exposure. An LLM-integrated application reads externally controlled content, allowing a webpage author to place competing instructions in data without controlling the legitimate user instruction or backend model. The paper does not directly compare standalone LLMs with web agents, quantify a vulnerability ratio, or evaluate browser tools and autonomous action execution.

**Limitations:** No direct standalone-versus-web-agent comparison; no live browsing or tool-action evaluation; heuristic attacks and standard models; known-answer detection limited to one prompt; concurrent defenses excluded; sampled-pair estimates without displayed uncertainty intervals; mixed task metrics complicate aggregate interpretation; extended report tables and repository absent; several implementation details and source inconsistencies remain unresolved.

## Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?

[Summary](summaries/indirect_prompt_injections_are_firewalls_all_you_need_or_stronger_benchmarks_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/Indirect_Prompt_Injections_Are_Firewalls_All_You_Need_or_Stronger_Benchmarks.pdf`

**Method:** Author-reported, HIGH confidence: a Tool-Input Firewall minimizes outgoing arguments using trusted task context, while a Tool-Output Firewall sanitizes incoming responses using task, tool, argument, and output context. Prompt-based JSON procedures are supplied. Evaluation uses AgentDojo tool_knowledge attacks, ASB context-ignoring and combined attacks, InjecAgent DH/DS base and enhanced settings, and Tau-Bench augmented with DoomArena data-stealing attacks. Original/fixed benchmark comparisons investigate measurement flaws.

**Attack surface:** Author-reported, HIGH confidence: malicious instructions embedded in external content or tool responses, including web pages, calendar entries, email, database fields, and files. The formal attacker controls returned content, not tool implementations, the user prompt, or the system prompt. Dynamic planning allows received content to influence later calls.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains an additional risk pathway relevant to web AI agents—attacker-controlled web pages and other retrieved content can enter agent context and redirect subsequent tool actions, including private-information disclosure and unauthorized operations. It does not experimentally compare standalone LLMs with web agents, quantify their relative vulnerability, or isolate browsing from other agent capabilities.

**Limitations:** HIGH confidence for source-bounded limitations: residual attacks and model-specific utility costs qualify broad headline claims; InjecAgent has no utility metrics; current attacks may be rigid or context-agnostic; ASB and AgentDojo metrics contain identified confounds. Analyst observations include missing implementation/statistical settings, ambiguous ASB correction comparisons, unexplained InjecAgent averages, unsupported probability independence, inconsistent example details, and no direct standalone-LLM comparison. No absent supplement or release code was reviewed.

## SafeArena: Evaluating the Safety of Autonomous Web Agents

[Summary](summaries/safearena_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/SafeArena_Evaluating_the_Safety_of_Autonomous_Web_Agents.pdf`

**Method:** A 500-task benchmark pairs 250 harmful tasks with 250 safe counterparts across five harm categories. Human-designed and GPT-4o-Mini-assisted tasks undergo author review. Five vision-capable instruction-tuned model backbones operate through BrowserGym. Evaluation combines functional binary reference checks, normalized safety score, GPT-4o ARIA judging, a separate refusal detector, and human trajectory annotation for Claude and Qwen. Additional analyses examine priming, selected manual decomposition, curation source, website/category variation, and completion divergence.

**Attack surface:** Malicious user instructions executed through authorized browser functions in four controlled website simulations: forum posts/comments, repository operations, shopping functions, and retail administration. Tested manipulations are direct harmful prompting, manual sequential task decomposition, and rule-based changes to starting URLs and remaining-task wording. Indirect prompt injection, privilege escalation, and production-system compromise are contextual concerns rather than demonstrated primary experiments.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper informs 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?' through evidence of harmful browser execution, poor reported alignment transfer, and selected decomposition and priming bypasses. Browser access expands consequences, and sequential or state-dependent interactions can undermine refusal. However, there is no matched standalone-LLM baseline, so the paper does not directly establish or quantify greater relative vulnerability.

**Limitations:** Explicit harmful intents; granted task permissions; simulated websites; brittle reference checks; no matched standalone-model control; selected manual decomposition cases; bundled priming changes; absent repeated-run uncertainty and several reproducibility details. Functional completion and judge-based results differ. Table 5 weighting, a 10.10% HITL safe result, Figure 24's category caption, and Table 10's first explanation remain unresolved. External artifacts and raw trajectories were not supplied or reviewed. Additional analyst check: reported NSS cannot be reconstructed from the Figure 3 functional totals under the stated same-pair binary-outcome assumption; reward/subset aggregation remains unresolved.

## SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents

[Summary](summaries/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/SecureWebArena_A_Holistic_Security_Evaluation_Benchmark_for_LVLM-based_Web_Agents.pdf`

**Method:** Six SoM-instrumented simulated applications, six attack families, 330 adversarial task-adversary combinations, nine LVLM agents, and 2,970 trajectories. RVR measures initial reasoning compliance using GPT-4o, BCR measures unsafe actions using expert annotation, and PDR measures final attacker-goal achievement using environment logs. Additional analyses examine stage changes, environment profiles, two qualitative failure pathways, and three agents on Amazon/Wikipedia under user-level attacks.

**Attack surface:** Author-reported: malicious user goals through direct prompt injection and jailbreak; untrusted webpage observations through pop-ups, visual distraction, deceptive advertisements, and indirect prompt injection. Environment attackers control website DOM, CSS, content, and injected scripts, but are excluded from browser chrome and the agent system prompt.

**Relevance:** Analyst inference, MEDIUM confidence: the paper provides mechanisms relevant to why web agents may face additional vulnerability—untrusted visual and textual website observations influence multistep decisions that become consequential actions. It does not directly compare standalone LLMs with matched web-agent configurations and therefore cannot establish the comparative vulnerability magnitude or isolate the causal effect of agent deployment.

**Limitations:** Authors acknowledge simulation-to-real gaps, evolving/composite threats, and agent-scope limits. Analyst observations include absent standalone baselines, limited live coverage, unclear live denominators, no reported uncertainty intervals or repeated-run variation, incomplete reproduction details, annotation error, and several text–table inconsistencies. Exact radar vertices and some fine visual content remain unreadable; no absent supplements were reviewed.

## ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents

[Summary](summaries/st_webagentbench_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/ST-WebAgentBench_A_Benchmark_for_Evaluating_Safety_and_Trustworthiness_in_Web_Agents.pdf`

**Method:** AUTHOR-REPORTED — HIGH confidence: A BrowserGym benchmark comprising 375 tasks and 3,057 policy instances across GitLab, ShoppingAdmin, and SuiteCRM; six stakeholder-informed safety/trustworthiness dimensions; ten reusable templates; deterministic evaluators with RapidFuzz message checks; injected policy hierarchy/context; simulated auto-approval; three public gpt-4o-backed agents; completion/compliance metrics, scoring-dimension removal, and policy-load grouping.

**Attack surface:** AUTHOR-REPORTED — HIGH confidence: Partially trusted DOM content, form fields, historical records, job-title/description strings, restricted values, conflicting instructions, incomplete forms, and disruptive pop-ups. In-scope risks include environmental prompt injection, fabricated inputs, incorrect policy priority, and irreversible or high-impact actions without confirmation. Network attacks, model-weight attacks, supply-chain compromise, and multi-agent collusion are excluded.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper helps explain additional risk opportunities created by browser integration: partially trusted page content becomes model input, generated decisions become consequential actions, policies must persist across workflows, and consent or clarification can be skipped. It does not directly compare standalone LLMs with browser agents or establish a comparative vulnerability rate. Its statement about safe models not guaranteeing safe agents is partly motivated through cited prior work, which was not independently reviewed.

**Limitations:** AUTHOR-REPORTED and ANALYST OBSERVATIONS — HIGH confidence for explicit scope, MEDIUM for methodological interpretation: Three open agents, shared backbone, English-only interaction, three applications, limited runs, one policy hierarchy, organizational-panel bias, and restricted adversarial coverage. No standalone-model control, raw artifacts, modality-specific results, controller evaluation, or adequate detail for independent statistical reconstruction. Several numerical, definition, and figure-reference discrepancies remain unresolved.

## WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks

[Summary](summaries/wasp_comprehensive_summary.md) · Source: `07_Security_Benchmarks_Evaluation/WASP_Benchmarking_Web_Agent_Security_Against_Prompt_Injection_Attacks.pdf`

**Method:** Empirical benchmark using two self-hosted VisualWebArena applications, 21 listed attacker goals, two benign objectives per environment, 42 reported scenarios, and two main injection templates yielding 84 reported attack tasks. Tests span VisualWebArena, Claude CURI, and a modified tool-calling loop. Goal-specific final-state rules measure end-to-end ASR, a GPT-4o judge measures intermediate compromise, and 37 separate legitimate tasks measure utility. Main comparisons, manual behavioral labeling, defense comparisons, template ablations, and task-knowledge ablations are distinct analyses.

**Attack surface:** Attacker-created GitLab issues/comments and Reddit/Postmill posts/comments encountered by an authenticated web agent; task-related or task-agnostic instructions can induce navigation and subsequent unauthorized operations. URL fragments provide a persistence channel when the current URL remains in context. Attackers lack detailed agent implementation knowledge and cannot arbitrarily modify site layout, add form fields, or create pop-ups.

**Relevance:** MEDIUM confidence, explicitly analyst inference: WASP demonstrates how third-party webpage instructions, URL/state persistence, and browser actions create consequential attack surfaces for web AI agents. It supports a mechanism-based security analysis of the user's question, but does not directly compare matched standalone LLMs and web agents or establish a numerical vulnerability increase.

**Limitations:** Two environments and limited manually written prompt diversity; no direct standalone-LLM control; partial visual-page coverage; absent repository/supplementary implementation inspection; no reported statistical uncertainty; incomplete compute and inference details; judge validation not supplied; forced exposure does not measure live-web encounter prevalence; unresolved scenario wording and o1 developer aggregation discrepancy.

## ACE: A Security Architecture for LLM-Integrated App Systems

[Summary](summaries/ace_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/ACE_A_Security_Architecture_for_LLM-Integrated_App_Systems.pdf`

**Method:** AUTHOR-REPORTED: Query-only trusted abstract app/program generation; embedding filtering and independent abstract/concrete matching with a compatibility layer; lattice-based static information-flow checks including implicit branch/loop dependencies; restricted Python execution through a privileged orchestrator and isolated Docker workers; three attack cases, adapted INJECAGENT and ASB, StruQ comparison, and LangChain Tool Usage evaluation.

**Attack surface:** AUTHOR-REPORTED: Installed application implementation, schema, name, natural-language description, and outputs under the strong threat model; planning integrity, execution integrity, execution availability, and execution privacy. Demonstrations target IsolateGPT's description-based planner and raw-output execution manager.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper supports a mechanism-based explanation for additional vulnerability in application-connected agents: untrusted descriptions affect selection, outputs enter shared planning context, chained actions propagate influence, and applications receive sensitive data and execution capabilities. It mentions web search as an indirect-injection source but does not directly compare web agents with standalone LLMs or quantify their relative vulnerability.

**Limitations:** Single-query and standalone-app scope; simulated injection benchmarks do not measure output correctness; no formal privacy-soundness guarantee for Python/runtime; acknowledged container-escape and crafted-message risks; incomplete experiment configuration and uncertainty reporting; detailed extended results absent; several caption, numerical, and language-example inconsistencies; no controlled standalone-LLM or web-agent comparison.

## Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs

[Summary](summaries/rennervate_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/Attention_is_All_You_Need_to_Defend_Against_Indirect_Prompt_Injection_Attacks_in_LLMs.pdf`

**Method:** RENNERVATE collects target-model attention features for each external-data token, applies response-wise and head-wise attentive statistics pooling, predicts token classes, smooths outputs with a mean filter, aggregates consecutive injected predictions, and optionally removes flagged tokens. FIPI supplies fine-grained labels. Evaluation covers five target models, 15 distinct baselines with model-specific availability, unseen cross-task settings, gradient attacks, adaptive attacks, ablations, and hyperparameter sensitivity.

**Attack surface:** External textual data retrieved by an LLM-integrated application. The attacker is assumed to control external sources and may use response feedback or gradients. Evaluations primarily measure injected-task following and response outcomes, rather than complete browser-action or exfiltration workflows.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper explains an architectural mechanism relevant to why web AI agents acquire additional vulnerability: legitimate instructions are concatenated with externally retrieved, potentially attacker-controlled data, and the model's response may lead to API actions. It does not directly compare standalone LLMs with matched web agents or quantify their relative vulnerability.

**Limitations:** Requires internal attention access; shadow-model deployment is proposed but not separately validated end to end. Utility can degrade severely when injected-task-specific content remains. Transfer results are heterogeneous, including 23.90% residual ASR in one unseen setting. No matched standalone comparison, universal robustness proof, repeated-run uncertainty, or comprehensive autonomous-web-agent evaluation is supplied. Pages 11–15 and 18 have text-only coverage; underlying artifacts are absent.

## BrowseSafe: Understanding and Detecting Prompt Injection Within AI Browser Agents

[Summary](summaries/browsesafe_understanding_and_preventing_prompt_injection_within_ai_browser_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/BrowseSafe_Understanding_and_Preventing_Prompt_Injection_Within_AI_Browser_Agents.pdf`

**Method:** Construct 14,719 synthesized benign/malicious HTML samples informed by 100,000 anonymized production tool outputs; split into 11,039 training and 3,680 test examples; evaluate detector families and content-difficulty factors; fine-tune Qwen3-30B-A3B-Instruct-2507 for one epoch; integrate raw-content scanning, tool trust flags, parallel chunk classification, logical OR aggregation, and replacement placeholders; assess same-data Qwen3-8B fine-tuning, latency, refusals, and held-out characteristic generalization.

**Attack surface:** Untrusted textual web content entering browser-agent tool outputs, including HTML comments, data attributes, hidden text, form fields, semantic attributes, paragraphs, lists, footers, and table cells. Attackers may control an entire website or submit content on a legitimate site. Non-textual and vision-specific attacks are excluded.

**Relevance:** ANALYST INFERENCE; MEDIUM confidence. The paper explains mechanisms relevant to why browser agents may face greater exposure and consequences than standalone LLM interactions: repeated attacker-controlled tool observations, complex HTML, hidden and coherent visible instructions, provenance-obscuring transformations, and tool-mediated actions. It does not directly compare matched standalone LLMs and browser agents or quantify their relative compromise probability.

**Limitations:** Synthetic/template-based workload; most objectives are exfiltration-related; limited multilingual coverage; very small footer/table rewrite groups; no uncertainty estimates or detailed timing hardware; incomplete calibration, annotation, and reproducibility details; unresolved text–figure and counting inconsistencies; ambiguous refusal scoring; no direct standalone comparison; no benchmarked non-text attacks or comprehensive end-to-end agent security evaluation.

## CELLMATE: Sandboxing Browser AI Agents

[Summary](summaries/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/ceLLMate_Sandboxing_Browser_AI_Agents.pdf`

**Method:** Agent-agnostic Chrome-extension sandbox mediating HTTP requests through developer-provided agent sitemaps and trusted policies. Separate LLM domain prediction and per-domain minimal policy selection instantiate permissions, which users confirm. Compiled authorization lookup, runtime conditions, DOM monitoring, caching, and optional request counters enforce decisions. Evaluation includes curated model-selection benchmarks, 12 scripted GitLab attacker goals across two user tasks, and latency/memory measurements.

**Attack surface:** Attacker-controlled issue descriptions, product reviews, and separate websites encountered by an authenticated browser agent; low-level navigation/click/type tools; sensitive HTTP operations and external destinations. Trusted browser enforcement, policies, and sitemap sources are assumed. Misuse entirely within permitted actions remains outside the evaluated protection.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: the paper explains how browser agents combine inherited LLM prompt-injection susceptibility with authenticated-session authority, sensitive-resource access, external communication, untrusted web content, and ambiguous UI tools. These mechanisms can amplify harm and complicate enforcement. It does not directly compare standalone LLMs with browser agents or measure a relative vulnerability rate.

**Limitations:** Single-turn focus; trusted browser and non-interfering privileged components; agent confinement to webpage operations; dependence on correct maintained sitemaps and policies; no general control/data-flow integrity; no prevention of all allowed-action misuse; freshness challenges for DOM arguments; general WebSocket enforcement left for future work. Security evaluation is restricted to scripted forbidden GitLab goals. Domain counts and one overhead percentage are inconsistent. No direct standalone-LLM comparison or reviewed external supplementary artifacts.

## Defeating Prompt Injections by Design

[Summary](summaries/defeating_prompt_injections_by_design_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/Defeating_Prompt_Injections_by_Design.pdf`

**Method:** CaMeL separates a privileged code-generating planner from a tool-free quarantined parser, executes restricted Python through a custom interpreter, propagates provenance and permitted-reader capabilities, and checks policies before tool execution. NORMAL and STRICT dependency modes are evaluated alongside AgentDojo utility, attack counts, policy triggers, baseline defenses, failure examples, and token overhead.

**Attack surface:** AUTHOR-REPORTED: Untrusted tool outputs, web pages, emails, shared documents, spreadsheets, extracted tool arguments, data-driven dispatch branches, error feedback, and behavioral side channels. Main assumptions trust the user prompt and memory. Malicious tools and rogue users are discussed as stronger conceptual scenarios outside the explicit AgentDojo evaluation.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper explains mechanisms by which tool-using web agents connect untrusted pages, messages, and tool outputs to privileged actions, sensitive data, and externally observable behavior. These mechanisms support an architectural explanation of increased attack exposure and potential harm. The experiments compare native tool-calling agents against CaMeL agents, not agents against standalone LLMs; no relative standalone-versus-web vulnerability rate is established.

**Limitations:** No direct standalone comparison; text-only manipulation and phishing are non-goals; utility loss varies substantially by model/suite; policies and annotations require maintenance; user approval can cause fatigue; partial side effects lack rollback; side channels remain possible; interpreter formal verification is future work; several numbers and appendix labels conflict; uncertainty and repetition reporting is incomplete; source-code artifacts were not supplied or inspected.

## Defending Against Indirect Prompt Injection Attacks With Spotlighting

[Summary](summaries/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/Defending_Against_Indirect_Prompt_Injection_Attacks_With_Spotlighting.pdf`

**Method:** AUTHOR-REPORTED: Spotlighting combines optional input transformation with explanatory system-prompt instructions. Variants are boundary delimiters, markers interleaved throughout text, and encoding. Evaluation uses 1000 synthetic attack documents, summarization and document Q&A, text-davinci-003 and June 2023 GPT-3.5-Turbo/GPT-4, and temperature 1.0. Separate benchmark accuracy experiments examine task preservation; an appendix examines few-shot defenses and strict ASR scoring.

**Attack surface:** AUTHOR-REPORTED: Untrusted external text, including websites, emails, and text messages, processed alongside legitimate instructions. The attacker embeds instructions in that content and may know the system prompt. Evaluated attacks seek full task replacement with a special keyword; broader session hijacking and exfiltration are motivating discussion rather than measured outcomes.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper provides a mechanism-level explanation relevant to why web AI agents may face additional risk: they ingest outside content that can contain unauthorized instructions, and their plugins, access patterns, and capabilities can increase the consequences of following those instructions. It does not directly compare standalone LLMs with web agents, quantify a relative vulnerability rate, or evaluate an end-to-end browser agent. Its direct experiments concern source transformations, synthetic keyword attacks, and language-task performance.

**Limitations:** AUTHOR-STATED: Delimiter imitation, whitespace-free attacks against simple marking, decoding-related utility loss, use-case dependence, imperfect shared-channel security, incomplete mechanism understanding, and few-shot example/test correlation. ANALYST OBSERVATIONS: Narrow keyword takeover metric; missing exact configurations, splits, repetitions, uncertainty estimates, data, and code; unexplained baseline shifts; a below-3% versus 3.10% discrepancy; no direct standalone-versus-web-agent comparison; and no quantitative evaluation of proposed dynamic marking against adaptive attackers.

## IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems

[Summary](summaries/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/IsolateGPT_An_Execution_Isolation_Architecture_for_LLM-Based_Agentic_Systems.pdf`

**Method:** A hub-and-spoke architecture with process-isolated apps, dedicated LLM instances and memory, deterministic non-LLM operators, hub-mediated ISC messages, structural validation, ephemeral identifiers, and configurable user permissions. Evaluation uses an enhanced 1,598-attack benchmark, four case studies, four LangChain functionality/performance workloads, and a 10% query cost sample. Both compared systems use GPT-4; artifact details identify version 0613.

**Attack surface:** AUTHOR-REPORTED: malicious app descriptions, hostile content processed by benign apps, shared model execution/context, app and system memory, cross-app exchanges, online service APIs, and outbound information flows. Attacker goals include changing other apps or LLM behavior and stealing sensitive data. Ambiguous benign instructions can also cause unintended sharing or interference. Within-app attacks remain outside the defense scope.

**Relevance:** ANALYST INFERENCE — HIGH confidence in the relevance boundary: the paper explains how third-party apps, untrusted emails/websites, shared context, persistent user data, online services, and executable API actions introduce opportunities for cross-app manipulation and data theft. These mechanisms help explain why web-connected agents can have additional exposure relative to text-only models. However, its empirical comparison is IsolateGPT versus VanillaGPT, both GPT-4-based agentic systems; it does not directly measure agents against standalone LLMs.

**Limitations:** Permission-mediated protection depends on user decisions; the artifact assumes rejection of warned requests for two cases. Warning rate is not directly comparable to baseline attack success. No human permission study, formal proof, standalone-LLM comparison, broad model comparison, or supplied repeated-run statistics appears. Benchmarks omit some complex real-world cases. Timings assume cold starts and automatically granted permissions. External artifacts were referenced but not reviewed.

## MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents

[Summary](summaries/melon_provable_defense_against_indirect_prompt_injection_attacks_in_ai_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/MELON_Provable_Defense_Against_Indirect_Prompt_Injection_Attacks_in_AI_Agents.pdf`

**Method:** Training-free masked re-execution preserves retrieved outputs while replacing user input and deleting generated-action history. A cache accumulates masked proposed tool calls, and embedding-based similarity detects matching original calls before execution. MELON-Aug adds Repeat Prompt. A distinct multi-prompt ensemble receives conditional theoretical error bounds.

**Attack surface:** AUTHOR-REPORTED: tool-retrieved websites, emails, files, and other external observations. Attackers manipulate this information to redirect legitimate user tasks; they do not control the model's internal input/output under the stated threat model.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper explains an additional risk path in tool-using and web-connected agents, where attacker-controlled retrieved content can redirect subsequent executable actions. Its state model and examples connect external information, persistent observations, and tool permissions. It does not directly compare standalone LLMs with web agents or quantify a comparative vulnerability increase.

**Limitations:** Response-based harms evade call-only monitoring; redundant calls, state hallucination, and nonexistent-function calls cause mismatches. Benign delegated instructions can trigger detections. Model calls and API costs approximately double. Main evaluation uses AgentDojo, three models, four general text attacks, and no standalone control; VWA-Adv is excluded. The source contains unresolved numerical and notational inconsistencies, and exact reproduction settings are incomplete.

## PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification

[Summary](summaries/planguard_defending_agents_against_indirect_prompt_injection_via_planning_based_consistency_verification_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/PlanGuard_Defending_Agents_against_Indirect_Prompt_Injection_via_Planning-based_Consistency_Verification.pdf`

**Method:** AUTHOR-REPORTED: Training-free isolated planning from the user instruction and tool definitions generates a reference action set. Execution-time verification passes exact matches, blocks non-reference tools, and sends permitted-tool parameter mismatches to an LLM intent verifier. Evaluation uses InjecAgent, DeepSeek-V3.2, Vanilla Agent, Stage-I Only, and full PlanGuard.

**Attack surface:** AUTHOR-REPORTED: Malicious payloads embedded in untrusted external context or tool-return content, with the user instruction remaining trusted. Target outcomes are unauthorized tool selection and malicious arguments to an otherwise appropriate tool. Parameter-borne attacks against the intent verifier are discussed theoretically.

**Relevance:** ANALYST INFERENCE: The paper explains a mechanism relevant to why web-connected AI agents may face additional security exposure: attacker-controlled webpages, emails, or retrieved documents can enter the agent's context, and tool permissions can translate instruction confusion into unauthorized actions. It does not directly compare standalone LLMs with web agents or quantify a comparative vulnerability gap. Its empirical evidence compares three agent-defense configurations on InjecAgent under a compliance-inducing victim prompt.

**Limitations:** AUTHOR-STATED: Additional inference/token overhead and lack of ground truth for arguments that depend on external content. ANALYST OBSERVATIONS: One named backbone, modified victim prompt, unspecified benign/subset denominators and aggregation, no reported uncertainty or measured overhead, no dedicated adaptive-attack evaluation, and no direct standalone-versus-agent comparison. Referenced code and benchmark artifacts were not supplied or inspected.

## Prismata: Confining Cross-Site Prompt Injection in Web Agents

[Summary](summaries/prismata_confining_cross_site_prompt_injection_in_web_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/Prismata_Confining_Cross-Site_Prompt_Injection_in_Web_Agents.pdf`

**Method:** Task-only origin policy; per-element critical-path action gating; top-down Biba-inspired provenance and capability labeling; minimum-capability composition; deterministic observation filtering and identifier-based action checks. Evidence includes a 5,664-DOM structural corpus, WebArena attack/utility experiments, WASP/adaptive stress tests, expert agreement on 20 observations, and caching/overhead measurements.

**Attack surface:** AUTHOR-REPORTED: text injected into user content, hosted-party content, or external content on benign websites can influence an agent and exploit legitimate browser/site features. Trusted-origin arbitrary JavaScript execution is outside scope. Within-task persuasion and non-textual attacks are not covered by the evaluated protection.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper explains additional web-agent exposure through mixed-origin page content, ambiguous click/fill semantics, data-dependent workflows, and access to consequential site features. It does not directly compare web agents with standalone LLMs and cannot establish a numerical comparative vulnerability gap.

**Limitations:** Conditional structural guarantees; fallible labeling and incomplete structural cues; residual Case 3 exposure; textual modality; broad-permission tasks; captured/live DOM drift; small benign expert sample; limited adaptive protocol disclosure; model-roster inconsistencies; no direct standalone-LLM control or reported component ablation.

## SecAlign: Defending Against Prompt Injection with Preference Optimization

[Summary](summaries/secalign_defending_against_prompt_injection_with_preference_optimization_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/SecAlign_Defending_Against_Prompt_Injection_with_Preference_Optimization.pdf`

**Method:** Construct preference triples automatically from instruction datasets: attacked input, authorized-task answer, and injected-task answer. Train using direct preference optimization with a supervised reference model; synthetic attacks are 90% Straightforward and 10% Completion. Evaluate utility and six attack families across five main model configurations, with additional benchmark and ablation studies.

**Attack surface:** Untrusted data fields, retrieved external content, documents, and API/tool results. The modeled attacker knows the trusted instruction and format, can inject arbitrary-length text into data, and has white-box access for optimized attacks, but cannot alter the trusted instruction or prompt format.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains how external pages, documents, and API results bring attacker-controlled instructions into trusted workflows and evaluates malicious API calling. This supports a mechanism for added exposure and consequential failures in agents. It does not directly compare matched standalone LLMs with web AI agents or quantify their relative vulnerability.

**Limitations:** Requires explicit instruction/data separation and consistent templates; empirical protection is incomplete and position-dependent. Main optimized ASRs include a 14% result. Multi-turn agent attacks, later fine-tuning, multiple benign instructions, and multimodal inputs remain unresolved. InjecAgent lacks utility evaluation. Several numerical inconsistencies and missing reproduction details are disclosed in the narrative.

## SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents

[Summary](summaries/snapguard_lightweight_prompt_injection_detection_for_screenshot_based_web_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/SnapGuard_Lightweight_Prompt_Injection_Detection_for_Screenshot-Based_Web_Agents.pdf`

**Method:** External screenshot-only pre-action detection using variance of grayscale gradient magnitudes, a benign-calibrated VSI threshold, selective inversion of pixels above grayscale intensity 240, OCR candidate union from original and transformed images, and action-oriented pattern categories. Main implementation uses Pytesseract and CPU processing. Exact branch-fusion logic and full pattern rules are unavailable in the supplied pages.

**Attack surface:** Attacker-controlled webpage renderings, third-party or user-generated images, product images, interface layouts, visually concealed instructions, and pixel-level perturbations. The threat model includes malicious content providers and website owners, with iterative refinement using surrogate or publicly available agents.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper supports a mechanism-based explanation relevant to why web-agent workflows face additional security exposure. Agents consume attacker-influenced environmental screenshots and translate interpreted content into executable actions, while screenshot-only interfaces complicate reuse of text-centric defenses. The study does not directly compare standalone LLMs and web agents under matched attack conditions and does not quantify their relative vulnerability.

**Limitations:** Benchmark image classification rather than live end-to-end agent-security measurement; VWA-shot TPR 0.13 and benign screenshot FPR 0.14; absent referenced appendices; unspecified metric aggregation and implementation details; no reported statistical uncertainty; Gaussian noise is the demonstrated perturbation rather than all realistic rendering distortions; zero GPU memory does not mean zero CPU memory; no direct standalone-LLM comparison.

## StruQ: Defending Against Prompt Injection with Structured Queries

[Summary](summaries/struq_defending_against_prompt_injection_with_structured_queries_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/StruQ_Defending_Against_Prompt_Injection_with_Structured_Queries.pdf`

**Method:** Secure front-end with separate prompt/data inputs, reserved-token encoding, recursive removal of delimiter spellings and double hash marks, and structured instruction tuning of base Llama-7B and Mistral-7B. Training nominally combines 50% clean, 25% Naive, and 25% Completion-Other samples while retaining the original task response; empty-data examples remain unchanged. Evaluation includes security, AlpacaEval utility, adaptive delimiter attacks, component ablations, and defense comparisons.

**Attack surface:** Attacker-controlled data inside a programmatic LLM query. The attacker knows the trusted prompt and formatting but cannot modify the prompt. Attacks include direct instructions, ignore directives, escape characters, fabricated response/instruction boundaries, competition attacks, LLM-generated TAP attacks, and white-box gradient-guided GCG suffixes. The measured property is primarily output integrity through an attacker-selected target string.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains how LLM-integrated applications create a security boundary between a trusted developer's instruction and an untrusted data source. This mechanism is relevant to web agents ingesting external text, but the paper does not directly compare autonomous web agents with standalone LLMs, quantify greater vulnerability, or evaluate an end-to-end browsing/action agent.

**Limitations:** Optimized attacks remain effective: defended GCG ASR is 58% for Llama and 56% for Mistral; TAP is 9% and 36%. Scope excludes ordinary open-ended multi-turn web chatbots and attacks such as jailbreaks and data extraction. Evidence comes from two 7B models and specific text benchmarks, with no direct autonomous-web-agent comparison. BIPIA comparisons use different starting models, some source numbers differ across tables, and full implementation artifacts, run variation, and complete training configuration were not reviewed.

## The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents

[Summary](summaries/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/The_Task_Shield_Enforcing_Task_Alignment_to_Defend_Against_Indirect_Prompt_Injection_in_LLM_Agents.pdf`

**Method:** Test-time extraction of actionable instructions, maintenance of a user-task set, LLM scoring of direct or indirect contribution to user goals, zero-contribution misalignment detection, feedback with user-goal reminders, and prevention of misaligned tool-call execution.

**Attack surface:** Instructions embedded in external documents, webpages, and tool outputs encountered during legitimate user tasks; subsequent assistant plans and tool calls can propagate the injected objective.

**Relevance:** Analyst inference, MEDIUM confidence: the paper supports an explanation of added agent exposure through attacker-influenced external content, multi-turn instruction propagation, and consequential tool actions. It does not directly compare standalone LLMs with web agents or quantify a comparative vulnerability gap.

**Limitations:** LLM extraction/scoring can fail or be adversarially probed; full shielding adds substantial latency; evaluation uses one trial per task, one benchmark, and GPT-family models with synthetic conversations. No matched standalone comparison, open-source evaluation, independent code review, or supplied supplementary review was performed. Numerical and prompt inconsistencies remain unresolved.

## Untrusted Content Masking for Web Agents with Security Guarantees

[Summary](summaries/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/Untrusted_Content_Masking_for_Web_Agents_with_Security_Guarantees.pdf`

**Method:** Client-side DOM masking replaces labeled untrusted content with unique placeholders before agent observation. A separate Q-Model answers targeted questions through parser-validated bool, bounded int, bounded float, enum, or date outputs. Human-reviewed strings provide a distinct fallback. Evaluation covers 100 custom tasks, 41 GitLab templates, twelve strengthened WASP goals, data-flow red teaming, and sanitized-DOM selector inference on three sites.

**Attack surface:** Attacker-controlled text and images inside untrusted regions of honest websites, including comments, reviews, issue descriptions, names, and externally sourced content. Correct masking removes direct agent exposure, but the remaining Q-Model channel can carry false well-typed data. Mislabeling exposes the original prompt-injection channel. Active-content escape, browser/OS compromise, and malicious site owners are outside the stated protection model.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: the paper explains a structural exposure mechanism relevant to why web agents may be more vulnerable: rendered pages intermingle trusted controls with third-party text and images, while the agent uses observations to select actions. It contrasts this with text-based tool interfaces where reasoning may use trusted interface definitions without processing untrusted content. It does not experimentally compare web agents with standalone LLMs or quantify a comparative vulnerability gap.

**Limitations:** Guarantees are conditional on correct trust labels and implementation enforcement. Typed outputs do not ensure truth or prevent selection hijacking. Automatic labeling has nonzero misses on Booking and GitLab. Free-text utility recovery adds a human-review assumption. Main utility tests are attack-free, the attack target differs from utility models, uncertainty conventions and some trial counts are unspecified, and no matched standalone-LLM baseline is evaluated.

## WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections

[Summary](summaries/ward_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/WARD_Adversarially_Robust_Defense_of_Web_Agents_Against_Prompt_Injections.pdf`

**Method:** Two-branch WARD-Base construction, generator–evaluator reasoning annotation, sequential full supervised fine-tuning on WARD-Base and WARD-PIG, then three-cycle memory-assisted adaptive attack generation and GRPO guard updates. Qwen-3.5-0.8B and 2B guards receive intended task, preprocessed HTML, and screenshot and run in parallel with the agent.

**Attack surface:** Author-reported: HTML-only, screenshot-only, and joint injections through interface overlays and native platform content; guard-targeted fake verdicts; adaptive contextual attacks; and fabricated task-relevant information. Imperceptible pixel-level environmental attacks are outside the main defended scope.

**Relevance:** Analyst inference, MEDIUM confidence: the paper explains mechanisms relevant to why web agents can face additional vulnerabilities—repeated consumption of untrusted HTML and visual interfaces, attacker-controlled native communication fields, task-aligned camouflage, and actions influenced by observations. It does not directly compare otherwise matched standalone LLMs and web agents or quantify a vulnerability increase caused by web agency.

**Limitations:** Authors acknowledge pixel-level attack limitations, a task-aligned camouflage failure, false-positive tradeoffs, dual use, and over-reliance risks. Analyst observations include shared teacher/attacker/validator dependence, bounded attack budgets, limited uncertainty reporting, proxy-agent validation, small malicious-only benchmarks, unspecified enforcement details, and unresolved platform/model/channel inconsistencies. External artifacts were not reviewed.

## WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents

[Summary](summaries/webagentguard_a_reasoning_driven_guard_model_for_detecting_prompt_injection_attacks_in_web_agents_comprehensive_summary.md) · Source: `08_Defenses_Guards_Containment/WebAgentGuard_A_Reasoning-Driven_Guard_Model_for_Detecting_Prompt_Injection_Attacks_in_Web_Agents.pdf`

**Method:** A dedicated multimodal guard runs in parallel with agent action generation, receiving user intent, processed HTML, and screenshot according to the explicit input descriptions. A gateway executes actions when approved by the guard or explicitly authorized by a human. Qwen3-VL 4B/8B backbones are trained on GPT-5-generated synthetic data using explanation-augmented supervised fine-tuning followed by GRPO with a binary format-and-correctness reward.

**Attack surface:** Attacker-modified webpage HTML whose instructions are perceivable through processed text, rendered screenshots, or both; recreated pop-ups and supplied VPI-Bench/EIA attacks; one guard-directed instruction inserted at the head or tail of malicious HTML. The formulation includes harmful action examples such as API-key leakage, and qualitative cases include file manipulation and coordinate-click commands.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper explains a relevant vulnerability pathway in which attacker-controlled webpage observations influence an agent's internal state and executable actions. It also attributes difficulty to coupling task completion with safety assessment. It does not directly compare matched standalone LLMs with web agents or quantify their relative vulnerability. Language-model detection baselines must not be interpreted as that comparison.

**Limitations:** No matched standalone-LLM comparison; synthetic-data and split-separation uncertainties; positive-only VPI/EIA evaluation cannot measure benign false positives; external benchmark denominators and statistical uncertainty are absent; robustness testing uses one explicit guard-directed attack string; utility declines and false negatives remain; mean timing supports only conditional latency conclusions; training explanations are label-conditioned; Table 2 metric discrepancies and Table 7 text–table disagreement remain unresolved.

## AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories

[Summary](summaries/agentrewardbench_evaluating_automatic_evaluations_of_web_agent_trajectories_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/AgentRewardBench_Evaluating_Automatic_Evaluations_of_Web_Agent_Trajectories.pdf`

**Method:** Empirical benchmark construction and evaluator comparison: 351 tasks across five benchmarks; four agent backbones; 1,302 trajectories; six expert annotators; 3,906 binary labels; task-based development/test splits; twelve LLM judge configurations plus official rules; primary precision with auxiliary recall/F1; GPT-4o Mini representation ablation; evaluator-dependent agent success-rate analysis; qualitative error taxonomy; auxiliary side-effect and repetition results.

**Attack surface:** ANALYST INFERENCE, MEDIUM confidence for conceptual relevance and LOW confidence for demonstrated exploitability: Potential security-relevant boundaries include webpage observations, accessibility-tree and screenshot representations, model-generated reasoning, executable browser actions, and judge approval or reward decisions. The paper observes non-adversarial failures across these boundaries; it does not establish attacker control, malicious payloads, exfiltration, authorization bypass, or exploitation.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The work informs verification weaknesses relevant to browser agents: their action histories and changing webpage states must be checked against goals, and judges sometimes accept misleading reasoning or incomplete execution. It does not directly answer why web agents are more vulnerable than standalone LLMs, because there is no matched standalone condition, adversary, attack experiment, or vulnerability-rate comparison.

**Limitations:** Security relevance is indirect. No standalone-LLM security baseline or adversarial threat model is present. Agreement covers only the GPT-4o/WebArena success subset. Statistical uncertainty, class counts, exact aggregation, inference settings, raw data, and code are unavailable here. Tables 9–12 duplicate Table 8 despite agent-specific captions; prompt and method differ on optimality and screenshot availability; judge counts and one task-category label conflict. All pages were read as supplied text, but visual coverage is limited to nineteen images.

## An Illusion of Progress? Assessing the Current State of Web Agents

[Summary](summaries/an_illusion_of_progress_assessing_the_current_state_of_web_agents_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/An_Illusion_of_Progress_Assessing_the_Current_State_of_Web_Agents.pdf`

**Method:** Closed-document empirical benchmark and evaluator analysis: 300 live-web tasks across 136 websites; six web agents with start URLs and Google Search restrictions; human binary labels from at least two annotators plus adjudication; three-stage WebJudge; judge comparisons, difficulty and efficiency analyses, ablations, three-run evaluator repeatability, and transfer to 1,302 AgentRewardBench trajectories. WebJudge-7B replaces screenshot relevance processing with a trained local model while retaining two LLM API stages.

**Attack surface:** Analyst-inferred candidate surfaces are task interpretation, browser observations, screenshot selection, action grounding, navigation/filter execution and outcome judgment. The paper studies ordinary reliability at these components, not attacker control or exploitation. No demonstrated prompt injection, exfiltration, credential compromise or unauthorized-action attack is reported.

**Relevance:** MEDIUM, analyst inference: the paper supplies evidence about failures when language-model decisions become live website actions and about weak verification of claimed success. It identifies mechanisms worth studying in security, including constraint mistranslation, grounding errors, long-trajectory evidence loss and unsupported final assertions. It does not directly compare standalone LLMs with web agents under attacks; the proposition that web agents are more adversarially vulnerable remains UNKNOWN from this source.

**Limitations:** Security relevance is indirect. Agent configurations and budgets differ, strong bot-protected sites are excluded, some numerical mappings are inconsistent, annotation agreement and main-result uncertainty intervals are absent, and training task-level separation is unspecified. Linked artifacts and raw trajectories were not supplied or inspected. Precision, recall, agreement and success-rate gaps must not be conflated.

## FocusAgent: Simple Yet Effective Ways of Trimming the Large Context of Web Agents

[Summary](summaries/focusagent_simple_yet_effective_ways_of_trimming_the_large_context_of_web_agents_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/FocusAgent_Simple_Yet_Effective_Ways_of_Trimming_the_Large_Context_of_Web_Agents.pdf`

**Method:** A lightweight LLM selects task-relevant numbered AxTree line spans at each step; post-processing removes other lines and inserts removed-span placeholders before a larger model predicts actions. The default uses soft prompting without retriever history. DefenseFocusAgent adds warnings and malicious-content-removal instructions. Evaluation uses BrowserGym/Agentlab, WorkArena L1, a WebArena test subset, and DoomArena attacks.

**Attack surface:** Author-reported and visually observed: text-only AxTree observations carrying injected instructions through SVG/banner alt fields and popup-associated text, including a contaminated close-button label. Error and image-only pages can become dominated by attack content. Popup state can obstruct actions even when the malicious text is omitted from the agent observation.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper informs why web agents can face additional security exposure by demonstrating indirect instructions in environmental page content, redirection toward attacker-designated browser actions, and popup interference with legitimate interaction. It does not directly compare agents with standalone LLMs and cannot establish their relative vulnerability rates.

**Limitations:** Prompt dependence; residual malicious content; untested contexts above 128k; poor popup task completion despite low ASR; limited attack types and Reddit security scope; no standalone comparator; normalized input-cost assumptions excluding latency and full-prompt processing; incomplete reproducibility details; and unresolved reporting inconsistencies.

## GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis

[Summary](summaries/guide_interpretable_gui_agent_evaluation_via_hierarchical_diagnosis_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/GUIDE_Interpretable_GUI_Agent_Evaluation_via_Hierarchical_Diagnosis.pdf`

**Method:** HIGH confidence for author-described method: training-free retrospective trajectory evaluation using text-only semantic segmentation, multimodal subtask diagnosis with success/partial/fail verdicts and corrective recommendations, and model-based task-level aggregation. Evaluation covers 932 industrial trajectories, 1,302 web trajectories, and 480 Android trajectories, plus length analysis, module ablations, and segmentation-quality validation.

**Attack surface:** UNKNOWN for demonstrated security attack surfaces. The supplied system processes task instructions, action summaries, screenshots, inferred subtask descriptions, and model-generated diagnoses, but these are documented evaluation inputs rather than tested attack surfaces. No malicious-content construction, attacker capabilities, unauthorized action, or data-exposure experiment is reported.

**Relevance:** MEDIUM confidence, explicitly analyst inference: the paper contributes a method for localizing failures in long, visually grounded web-agent workflows and evidence that holistic evaluators can lose reliability with trajectory length. It does not directly answer why web AI agents are more vulnerable than standalone LLMs: there is no matched standalone-LLM comparison, adversarial evaluation, or security-outcome measurement.

**Limitations:** HIGH confidence for author-stated domain-knowledge limitations and missing Appendix; MEDIUM for analyst-applied validity concerns. The paper reports business-convention errors, lacks direct security comparisons, does not quantify diagnostic faithfulness or actual repair success, omits cost and runtime results, and gives limited uncertainty outside Android. Several prose claims conflict with plotted values or tables.

## Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks

[Summary](summaries/odysseys_benchmarking_web_agents_on_realistic_long_horizon_tasks_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/Odysseys_Benchmarking_Web_Agents_on_Realistic_Long_Horizon_Tasks.pdf`

**Method:** Dataset/benchmark construction from 248 participants and 2,380 labeled browsing journeys; LLM and author refinement; embedding-based clustering and GPT-5.4 task composition; author-written tasks and generated hard-task expansion; 200 final tasks with 1,225 rubric items. Eight general computer-use models are evaluated through OSWorld virtual Ubuntu environments, primarily Chrome, under a main 100-step cap. Gemini-based per-rubric judging is compared with human annotations and a holistic judge. Additional analyses cover difficulty, efficiency, qualitative behavior, and a 200-step budget.

**Attack surface:** ANALYST INFERENCE: Relevant documented interaction surfaces include live pages, multiple tabs, raw HTML and embedded structured metadata, archived content, browser controls, clipboard operations, saved artifacts, and some virtual-machine programmatic capabilities. The authors explicitly discuss possible scraping, phishing, access-control circumvention, and unintended reuse of browser primitives. No formal attacker capabilities, exploit chains, or evaluated security boundaries are specified.

**Relevance:** MEDIUM confidence, ANALYST INFERENCE: The paper informs a security analysis by documenting extended interaction with heterogeneous websites and browser/system capabilities, including source inspection, archive retrieval, clipboard use, and programmatic actions. It does not directly compare standalone LLMs against web agents, expose agents to controlled malicious instructions, or measure security compromise. Its task-failure percentages must not be interpreted as vulnerability or attack-success rates.

**Limitations:** No adversarial experiment or standalone-LLM comparator; public-page and low-impact scope; model-specific implementations and Qwen summary prompting; limited reported human-annotation detail; no supplied execution artifacts; undefined uncertainty bars and absent repeated-run statistics. Several appendix counts and bounds conflict or lack clear denominators. All 29 pages were read textually, but only 22 had visual renderings; fine browser screenshot text was partially unreadable.

## The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break

[Summary](summaries/the_long_horizon_task_mirage_diagnosing_where_and_why_agentic_systems_break_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/The_Long-Horizon_Task_Mirage_Diagnosing_Where_and_Why_Agentic_Systems_Break.pdf`

**Method:** HORIZON constructs progressively extended tasks across WebArena, AgentBench OS, MAC-SQL databases, and IsaacSim embodied simulation. More than 700 tasks yield 3100+ trajectories. GPT-5-mini and Claude-4-Sonnet are tested across domains, full GPT-5 additionally on embodied tasks, and a GPT-5 judge assigns failures using a seven-category taxonomy. Success curves use three runs with standard deviations; human validation reports κ = 0.61 and κ = 0.84 on 40-trajectory studies.

**Attack surface:** Analyst inference only: webpage observations, dynamic UI state, action interfaces, retained interaction history, and intermediate artifacts are relevant places to investigate manipulation or policy violation. The supplied study specifies no attacker-controlled surface, attacker capability, exploit, or attack-success rate.

**Relevance:** MEDIUM — Analyst inference: the paper identifies interactive failure mechanisms that may contribute to security risk in web agents, including stale-state actions, constraint loss, unverified premises, and cascading mistakes. It does not directly compare web agents with standalone LLMs or establish greater adversarial vulnerability.

**Limitations:** No standalone-LLM or adversarial comparator; proposed mitigations are not tested. Validation sample descriptions and rubric precedence conflict. Exact per-condition denominators, active contexts, code, seeds, and supplementary review records are absent. Aggregate failure distributions do not directly show category shifts with horizon. Visual inspection covers 21 of 47 pages; remaining pages were analyzed from supplied text.

## WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks

[Summary](summaries/webchorearena_evaluating_web_browsing_agents_on_realistic_tedious_web_tasks_comprehensive_summary.md) · Source: `09_Progress_Long_Horizon_Benign_Controls/WebChoreArena_Evaluating_Web_Browsing_Agents_on_Realistic_Tedious_Web_Tasks.pdf`

**Method:** A manually constructed 532-task benchmark over four simulated WebArena websites and cross-site settings, with 117 templates, overlapping capability labels, observation requirements, textual/URL/functional scoring, five principal proprietary LLMs in two agent frameworks, human evaluation, and fifteen separately registered empirical analyses including supplementary appendix experiments.

**Attack surface:** ANALYST INFERENCE: candidate components for future examination include webpage observations through accessibility trees and screenshots, information retained in memory or summaries, browser navigation and state-changing actions, optional scratchpad/calculator interfaces, and cross-site login context. These are documented interaction components, not experimentally established attack surfaces or demonstrated exploits in this study.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper documents observation channels, persistent memory, browser actions, cross-site context, and ordinary execution failures that can help organize a security analysis. It does not directly compare web agents with standalone LLMs or measure adversarial vulnerability. Confidence in a comparative vulnerability conclusion from this paper alone is UNKNOWN.

**Limitations:** Controlled environments trade real-world coverage for diagnosis; website APIs are excluded; evaluation primarily scores final outcomes. Additional analyst observations include different human task coverage, confounded architecture comparisons, absent uncertainty estimates, optional-tool adoption effects, incomplete prompt examples, and no adversarial threat model or standalone-LLM security baseline.

## Detection of crawler traps: formalization and implementation—defeating protection on internet and on the TOR network

[Summary](summaries/detection_of_crawler_traps_formalization_and_implementation_defeating_protection_on_internet_and_on_the_tor_network_comprehensive_summary.md) · Source: `10_Traditional_Crawling_Crawler_Traps/Detection_of_crawler_traps_formalization_and_implementation—defeating_protection_on_internet_and_on_the_TOR_network.pdf`

**Method:** Compare three established and five proposed page-distribution measures using content-based overlapping word bigrams from 13 families with 500 pages each. Evaluate interval overlap while varying t in [μ−tσ, μ+tσ] under individual-family, merged regular/trap, and unmerged cross-category conditions. Describe a dynamic two-cluster detector with robust statistics and trimmed k-means; operational implementation and testing are not established by the reported experiments.

**Attack surface:** Author-described surface: website-controlled page text, page identifiers, link structures, dynamically generated pages, and trap activation during sequential crawling. The crawler consumes material and follows links supplied by an environment whose goals can conflict with useful collection. Site owners frame traps as anti-bot protection; treating them as attacks on an agent is an analyst perspective.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper illustrates an interaction-level hazard relevant to web AI agents: externally controlled pages, changing content, and links can induce repeated unproductive actions and contaminate collected information. This provides a mechanism to investigate when comparing web-enabled agents with standalone models. It does not study LLMs, prompt injection, or a direct agent-versus-standalone comparison, and therefore does not establish comparative vulnerability.

**Limitations:** No LLM-specific evaluation or matched standalone-model baseline. Selected sources include only four trap families, two of which are notEvil timing variants, and two locally generated trap datasets. No prediction-level confusion matrix, measured detector accuracy, latency, resource savings, repeated-run uncertainty, hardware configuration, or complete implementation specification. Some formulas and overlap normalization are unresolved. Dataset and software links were not inspected.

## IRLbot: Scaling to 6 Billion Pages and Beyond

[Summary](summaries/irlbot_scaling_to_6_billion_pagesand_beyond_comprehensive_summary.md) · Source: `10_Traditional_Crawling_Crawler_Traps/IRLbot_Scaling_to_6_Billion_Pagesand_Beyond.pdf`

**Method:** Mixed computer-systems, algorithmic, and theoretical study: DRUM provides bucket-based disk check/update operations; STAR assigns pay-level-domain budgets using incoming-domain links; BEAST schedules deferred URLs with expanding queues. Seven theorems model disk, cache, and budget costs. Trace simulations and memory-structure measurements accompany one 41.27-active-day single-server crawl producing 6,380,051,942 successful HTML responses.

**Attack surface:** Author-reported crawler exposure includes dynamically generated pages and hostnames, high-density link farms, effectively infinite Web structures, deliberate HTTP/DNS delays targeting the crawler's IP address, and politeness-induced backlogs. The protected outcomes are operational progress and resource use. Semantic instruction attacks, credential compromise, and data exfiltration are not evaluated.

**Relevance:** MEDIUM confidence, analyst inference: the paper explains how repeated interaction with Web-controlled resources exposes an automated system to branching traps, delays, DNS burdens, queue growth, and resource-allocation manipulation. These mechanisms are indirectly relevant to operational vulnerability in Web AI agents. It contains no standalone LLM comparison, prompt-injection experiment, AI-agent evaluation, or measured comparative vulnerability.

**Limitations:** One integrated deployment without reported component ablations or repeated full-scale runs; coarse PLD reputation; qualitative legitimacy review; disabled content deduplication; approximate hash-collision analysis; fixed-RAM asymptotic limits; projected extreme-scale results; unavailable implementation and raw traces. Visual coverage is partial by page, although all numbered figures are supplied visually. The paper cannot establish why Web AI agents are more vulnerable than standalone LLMs.

## Measuring What the Crawler Sees: Discovery Curves, Core Persistence, and Shell Dynamics in Longitudinal Web Crawls

[Summary](summaries/measuring_what_the_crawler_sees_discovery_curves_core_persistence_and_shell_dynamics_in_longitudinal_web_crawls_comprehensive_summary.md) · Source: `10_Traditional_Crawling_Crawler_Traps/Measuring_What_the_Crawler_Sees_Discovery_Curves_Core_Persistence_and_Shell_Dynamics_in_Longitudinal_Web_Crawls.pdf`

**Method:** Closed-document mathematical and observational analysis: homogeneous dynamic-urn modeling; closed-form containment and cumulative discovery; independent cross-observable fitting and overlay; persistent-core/changing-shell extension; Common Crawl domain-level analysis over 51 crawls in 2020–2025; GAW URL-level single-trajectory check over 2013–2019. All supplied text and all five figures were reviewed, with partial page-image coverage.

**Attack surface:** Not studied. No attacker, malicious payload, agent action interface, trust boundary, exploit, or security defense is evaluated. Upstream fetch coverage is a measured selection boundary in the paper, not an empirically demonstrated attack surface.

**Relevance:** ANALYST INFERENCE; MEDIUM confidence in indirect relevance. The study can inform a measurement discussion about selective, incomplete, and temporally varying web observations. It does not directly answer why web AI agents are more vulnerable than standalone LLMs, compare those systems, or measure security outcomes. Any causal bridge from crawler coverage to agent vulnerability remains unsupported by this paper.

**Limitations:** Residual shell-coverage disagreement; weak discovery-only core identifiability; GAW single trajectory; no explicit rebirth mechanism; conjectural policy attribution; incomplete implementation and statistical uncertainty reporting; different units and cadences across archives; unresolved core-floor normalization and inversion wording; small legend readability limits; no direct evidence about agent-versus-LLM vulnerability.

## The Impact of Crawl Policy on Web Search Effectiveness

[Summary](summaries/the_impact_of_crawl_policy_on_web_search_effectiveness_comprehensive_summary.md) · Source: `10_Traditional_Crawling_Crawler_Traps/The_Impact_of_Crawl_Policy_on_Web_Search_Effectiveness.pdf`

**Method:** Empirical sandbox-based crawl-policy evaluation using human-judgment maxNDCG, click-count corroboration, policy unions, domain budgets, and repeated approximately 100-million-page selections assessed by Jaccard overlap, membership churn and helpful-page counts.

**Attack surface:** ANALYST INFERENCE — The only defensible connection is the selection of externally sourced Web pages and link-derived information. The authors mention robustness against manipulation increasing spam as a desirable corpus property. No adversarial payload, prompt-injection pathway, attacker capability, execution tool or security boundary is tested.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence for indirect relevance; UNKNOWN for comparative vulnerability. The study shows that acquisition policies change which information is available and how collections evolve. This can inform acquisition-layer questions in Web-agent security, but the paper neither studies AI agents nor compares them with standalone LLMs.

**Limitations:** Potential retrieval effectiveness rather than actual retrieval or security performance; incomplete judged-URL coverage; requested-versus-successful acquisition distinction; HTTPS and trap-domain filtering; absent uncertainty estimates and implementation artifacts; one fewer TD iteration; unresolved numerical/text inconsistencies; no direct evidence about Web-agent versus standalone-LLM vulnerability.

## Web Crawling

[Summary](summaries/web_crawling_comprehensive_summary.md) · Source: `10_Traditional_Crawling_Crawler_Traps/Web_Crawling.pdf`

**Method:** Technical narrative survey combining historical architecture descriptions, crawl-ordering and freshness models, reported empirical studies, adversarial-content mechanisms, and deep-web query models. This analysis used only supplied text for physical pages 1–74 and the 27 supplied page images, including all eight numbered figures.

**Attack surface:** Author-described crawler exposure includes provider-controlled HTML and hyperlinks, dynamically generated URL spaces, address aliases and mirrors, keyword and link spam, User-Agent/IP-based cloaking, and JavaScript or META REFRESH redirection. Mapping these surfaces to LLM-agent instruction handling is an analyst inference, not an evaluated result.

**Relevance:** MEDIUM confidence, explicitly analyst inference: the survey documents adversarial web content, manipulation of discovery and ranking, crawler traps, identity-dependent responses, and browser/crawler execution differences. These mechanisms motivate investigation of the external exposure of web AI agents. It does not directly compare web AI agents with standalone LLMs, test prompt injection, or establish a comparative vulnerability increase; that conclusion has UNKNOWN support from this paper.

**Limitations:** No systematic literature-search protocol or pooled statistical analysis is reported. Many study summaries omit full configurations and uncertainty. Referenced artifacts were not independently inspected. Some internal citation mappings and weighted-coverage terminology are inconsistent. No LLM-specific threat model, standalone-model baseline, agent security benchmark, or attack-success measurement is present.

## A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents

[Summary](summaries/a_survey_on_autonomy_induced_security_risks_in_large_model_based_agents_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/A_Survey_on_Autonomy-Induced_Security_Risks_in_Large_Model-Based_Agents.pdf`

**Method:** Narrative/conceptual security survey using a five-level autonomy taxonomy, qualitative comparisons across three system classes, seven architectural risk loci, eight attack-surface categories, capability-specific CMDP models, a layered defense synthesis, and the proposed R2A2 architecture. No reproducible search protocol or original experimental evaluation is reported.

**Attack surface:** User instructions; untrusted web and environmental content; multimodal perception; reasoning and planning; persistent memory and retrieved knowledge; privileged tools and browser APIs; irreversible action interfaces; inter-agent messages and shared stores; live private-data retrieval and transmission. Exposure and impact depend on permissions, persistence, oversight, and validation.

**Relevance:** MEDIUM confidence; analyst inference for the web-specific research question. The paper explicitly compares standalone LLMs with autonomous agents in Tables 1 and 2. Its discussion of unverified web content, deceptive environmental inputs, browser APIs, persistent memory, planning, and external actions explains additional web-agent exposure and consequences. It does not provide a controlled web-agent-versus-standalone-LLM experiment or a numerical vulnerability multiplier.

**Limitations:** Qualitative risk ratings lack a calibrated measurement protocol; no original attack rates, effect sizes, overhead measurements, or R2A2 deployment results are reported. CMDP guarantees are conditional and the supplied article does not prove end-to-end applicability. Some taxonomy assignments and terminology conflict internally. Six pages have text-only inspection, and cited primary studies and supplementary artifacts were not reviewed.

## A Survey on Trustworthy LLM Agents: Threats and Countermeasures

[Summary](summaries/a_survey_on_trustworthy_llm_agents_threats_and_countermeasures_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/A_Survey_on_Trustworthy_LLM_Agents_Threats_and_Countermeasures.pdf`

**Method:** Qualitative taxonomy-driven survey organized by intrinsic/extrinsic components, attack/defense/evaluation techniques, and five core trustworthiness dimensions. Contains six conceptual figures, one survey-comparison table, and Appendix A definitions. No reported systematic search/screening protocol, original benchmark experiment, or pooled quantitative synthesis.

**Attack surface:** AUTHOR-REPORTED: Brain inputs and reasoning; long-term memory poisoning and leakage; short-term dialogue misuse; tool planning, selection, execution, injection, and forged commands; tool-enabled attacks on external entities; cooperative and infectious inter-agent influence; dynamic physical/digital environments and user interactions. Availability of each surface depends on actual access and capabilities.

**Relevance:** ANALYST INFERENCE; MEDIUM confidence: The survey explains mechanisms relevant to why web AI agents can have greater exposure and consequences than standalone LLMs: additional external inputs, retrievable and persistent memory, multi-turn context, tool planning/selection/execution, environmental actions, and inter-agent propagation. It is not itself a controlled comparative web-agent security study and supplies no universal vulnerability ratio.

**Limitations:** Review coverage cannot be independently reproduced from search details supplied here. Threat models and evaluation measures are heterogeneous; numerical benchmark sizes do not establish comparative vulnerability. Selected citations are mismatched or duplicated. Underlying cited studies and advertised repository were not inspected. Page 9 is text-only; small diagram labels are partly uncertain.

## A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework

[Summary](summaries/a_systematic_survey_of_security_threats_and_defenses_in_llm_based_ai_agents_a_layered_attack_surface_framework_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/A_Systematic_Survey_of_Security_Threats_and_Defenses_in_LLM-Based_AI_Agents_A_Layered_Attack_Surface_Framework.pdf`

**Method:** PRISMA-inspired systematic survey of 116 retained papers from 1,634 records across four databases and two search phases, with single-author layer/time coding into 144 reported assignments; conceptual architecture, conditional theorem sketch, defense/benchmark mapping, five-case taxonomy comparison, and four reported robustness protocols.

**Attack surface:** Seven author-defined analytical layers: foundation, cognition, memory, tool execution, coordination, ecosystem, and governance. Web-specific exposure includes page-mediated indirect prompt injection, adversarial pixels, file and API returns, tool permissions, persistent writes, and MCP/tool-description initialization. Temporalities distinguish immediate, within-session, cross-session memory, and drift/dormant-trigger effects.

**Relevance:** ANALYST INFERENCE — HIGH conceptual relevance to why web agents introduce additional vulnerabilities: repeated exposure to untrusted pages and images, tool-output trust inversion, consequential actions, persistent memory, and peer propagation. The paper does not itself perform a matched controlled comparison establishing that all web agents are more vulnerable than standalone LLMs or quantifying a general vulnerability multiplier.

**Limitations:** Single-coder classification; no inter-rater reliability; selective venue/citation/gap inclusion; excluded industry evidence; missing supplements; heterogeneous secondary metrics; unmeasured severity construct; claimed rather than validated defense coverage; internal numerical, coding, cutoff, and citation inconsistencies; no new controlled standalone-versus-agent security experiment.

## SoK: Attack and Defense Landscape of Agentic AI Systems

[Summary](summaries/sok_attack_and_defense_landscape_of_agentic_ai_systems_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/SoK_Attack_and_Defense_Landscape_of_Agentic_AI_Systems.pdf`

**Method:** Literature-based cybersecurity systematization of knowledge. The authors report a 2023–October 2025 review, four keyword dimensions, venue/source prioritization, manual exclusion of standalone-model work, and 128 papers including 51 attack methods and 60 defense methods. They synthesize design dimensions, threat models, interacting risks, defense mechanisms, and an Appendix A MITRE ATLAS crosswalk.

**Attack surface:** AUTHOR-REPORTED: external pages and documents, third-party tool names/descriptions/implementations, direct user inputs, model components, memory and RAG stores, user interfaces, tool credentials, and external resources. Attack vectors V1–V6 are distinct from risks R1–R7.

**Relevance:** ANALYST INFERENCE; MEDIUM confidence in the web-specific application. The paper directly discusses conceptual differences between agentic systems and standalone LLMs, including expanded interfaces and amplified consequences. Its framework helps explain conditional web-agent vulnerability through untrusted pages, dynamic tool use, memory, sensitive access, and action authority. It does not conduct a controlled comparison or establish that every web agent is more vulnerable than every standalone deployment.

**Limitations:** No original experiments, empirical effect sizes, shared benchmark comparison, or normalized defense performance. Search databases, full queries, screening flow, coding agreement, and evidence-quality ratings are not supplied. Internal inconsistencies include nine versus seven risks and an unexplained November-identified citation relative to the October search endpoint. Visual inspection covers 13 rendered pages; all remaining pages were text-only.

## Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks

[Summary](summaries/talk_is_not_cheap_a_taxonomy_and_benchmark_coverage_audit_for_llm_attacks_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/Talk_is_Not_Cheap_A_Taxonomy_and_Benchmark_Coverage_Audit_for_LLM_Attacks.pdf`

**Method:** Literature-derived taxonomy and benchmark coverage audit: Gemini 3.1 Pro extracts 6,366 mentions from 932 arXiv papers; normalization yields 2,521 groups; direct, fuzzy, and semantic matching assign taxonomy leaves; authors construct a 507-leaf hierarchy and 4×6 operational matrix. Human, cross-model, recall, novelty, and provenance spot-checks qualify the dataset. Manual documentation mapping audits six benchmarks, and a worked specification proposes metrics for an uncovered disruption cell.

**Attack surface:** Author-reported surfaces include direct prompts, web content, files, API responses, tool descriptions and returned content, agent-to-agent interactions, stateful or memory-related channels, multimodal inputs, and selected internal-generation or routing mechanisms. Attacker access varies; white-box internal mechanisms must be distinguished from externally supplied web content.

**Relevance:** MEDIUM confidence, analyst inference: the paper helps explain additional web-agent failure channels through external-data instructions, tool-mediated side effects, exfiltration, and resource consumption. Its output-versus-execution distinction shows why harmful-text testing does not establish action security. It does not directly compare standalone LLMs with web agents, estimate a vulnerability multiplier, or causally isolate browsing and tool access.

**Limitations:** English arXiv corpus from one database with unpublished formal inclusion criteria; incomplete H1 2026 collection; shared-model extraction/classification dependence; limited and partly anchored recall evaluation; uncertain fine-grained boundaries; 106 unpopulated placeholders; approximate provenance; only six public benchmarks; no new attack execution or direct web-agent-versus-standalone experiment. Several prose claims conflict with tables or arithmetic, especially the assertion of zero overlap between all primary benchmarks.

## Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation

[Summary](summaries/toward_secure_llm_agents_comprehensive_summary.md) · Source: `11_Surveys_Taxonomies_SoK/Toward_Secure_LLM_Agents_Threat_Surfaces_Attacks_Defenses_and_Evaluation.pdf`

**Method:** A lifecycle-based cybersecurity survey of 247 normalized papers, searched over a declared 1 January 2023–27 April 2026 window using six sources, GPT-5.4-assisted candidate expansion, and backward/forward snowballing. Screening starts from 275 records, removes 24, and reduces four through duplicate/version normalization. Three authors independently annotate the corpus, using single-label descriptive fields and multi-label technical fields; overall pre-harmonization Fleiss' kappa is reported as 0.86. Analyses are descriptive counts, co-occurrence matrices, and qualitative systems/engineering synthesis.

**Attack surface:** AUTHOR-REPORTED: user prompts, web content, tool outputs, retrieved content, files/code, planning loops, memory/scratchpads, and inter-agent channels. For web agents, the central path is low-authority external content entering reasoning and influencing privileged action. Memory and multi-agent propagation are conditional additional surfaces, not properties of every browser agent.

**Relevance:** MEDIUM confidence, explicitly ANALYST INFERENCE: the survey provides a mechanism-based explanation for additional web-agent exposure relative to text-only LLM applications. Untrusted page content can influence planning and action selection under delegated permissions; tool feedback, persistent memory, and coordination can extend effects when those capabilities exist. The paper directly discusses the architectural distinction but does not conduct a matched standalone-versus-web-agent experiment or establish a universal numerical vulnerability increase.

**Limitations:** AUTHOR-REPORTED: overlapping categories, judgment-sensitive manual screening/annotation, search/publication bias, preprint instability, and retrieval-model bias. ANALYST OBSERVATIONS: no controlled standalone comparison, no pooled efficacy estimate, absent raw review artifacts, ambiguous Figure 5 denominator, unresolved publication-date markings, and an Appendix C.1 prose/matrix discrepancy. All 40 supplied text pages were read; 27 were visually inspected. No absent supplementary artifact or referenced paper was claimed as reviewed.

## AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents

[Summary](summaries/androidworld_comprehensive_summary.md) · Source: `12_Contextual_Borderline/AndroidWorld_A_Dynamic_Benchmarking_Environment_for_Autonomous_Agents.pdf`

**Method:** A controlled Android benchmark with reported 116 tasks across 20 apps, seeded parameter generation, task-specific initialization and teardown, filesystem/database/system-state or UI validators, and composite partial rewards. M3A uses zero-shot action reasoning and post-action reflection; baselines include M3A-Simple and adapted SeeAct. The main evaluation uses seed 30 and temperature 0, with Gemini 1.5 Pro, GPT-4 Turbo, and Gemma 2 27B. MobileMiniWoB++ implements 92 tasks but evaluates 62. Additional analyses change seeds, repeat five selected tasks, inspect qualitative failures, and test Pixel 5/Android 12 alongside Pixel 6/Android 13.

**Attack surface:** ANALYST INFERENCE, MEDIUM confidence: Candidate security-relevant interfaces include task prompts, screenshots, accessibility-element text and descriptions, stored app content, action-history/reflection content, and UI/API execution. The paper documents these system interfaces but does not establish attacker control over each one. Privileged adb state access belongs to the benchmark harness and must not automatically be attributed to all tested agents. Appendix B names altered prompts and screen outputs as possible malicious-use mechanisms.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper helps identify how interactive agents consume task instructions, screenshots, and accessibility-derived UI content and turn decisions into device actions. Its ethics appendix explicitly mentions malicious alteration of prompts or screen outputs. It does not directly compare web-agent vulnerability with standalone LLM vulnerability, conduct adversarial attacks, or report attack-success rates. It is relevant as an architectural and evaluation-method source, not as direct evidence of the requested comparative security claim.

**Limitations:** Selected open-source and built-in apps, fixed emulator state, local storage, and no required authentication limit scope. Main results lack confidence intervals; repeated robustness trials cover five tasks, and statistical-test details are incomplete. Human performance uses two engineers. Table 4 task counts, app sourcing, MiniWoB++ porting counts, and several catalog rows contain unresolved inconsistencies. Only 17 pages were visually supplied; other pages were text-only. No implementation or supplement was reviewed. No standalone-LLM security baseline, adversarial condition, defense experiment, or comparative vulnerability result is present.

## AWE: Adaptive Agents for Dynamic Web Penetration Testing

[Summary](summaries/awe_comprehensive_summary.md) · Source: `12_Contextual_Borderline/AWE_Adaptive_Agents_for_Dynamic_Web_Penetration_Testing.pdf`

**Method:** AUTHOR-REPORTED — Three-layer memory-augmented architecture with LLM orchestration, eight vulnerability-specific agents, reconnaissance, structured context/filter probing, constrained payload mutation, and browser-backed verification. Model selection uses DVWA; system comparison uses 104 XBOW challenges against published MAPTA results. Correct flag retrieval is required for a counted XBOW success.

**Attack surface:** AUTHOR-REPORTED — The attacked surface is the target web application's HTTP endpoints and attacker-controlled parameters, headers, cookies, request bodies, and dynamic client-side content. Included families are XSS, SQL injection, SSTI, command injection, file inclusion/path traversal, XXE, SSRF, and authenticated unauthorized object access. The security attack surface of AWE itself is not evaluated.

**Relevance:** ANALYST INFERENCE — Indirect relevance only. The paper shows how HTTP interaction, browser verification, authentication state, memory, specialized procedures, and execution flexibility shape agents' web-exploitation capabilities. It does not measure attacks against AI agents, include a standalone-LLM vulnerability control, or establish that web AI agents are more vulnerable than standalone LLMs. Confidence: HIGH for this scope distinction.

**Limitations:** AUTHOR-REPORTED — Injection-centric scope, limited multi-step planning, heuristic context/filter abstractions, and model sensitivity. ANALYST OBSERVATIONS — Different models and historical baseline measurements confound architectural attribution; small category samples, missing uncertainty estimates, no component ablations, unexplained DVWA percentages, a cost-per-solve inconsistency, and Figure 4 caption–visual misalignment limit inference. No direct evidence addresses comparative vulnerability of web agents and standalone LLMs.

## BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents

[Summary](summaries/backdooragent_comprehensive_summary.md) · Source: `12_Contextual_Borderline/BackdoorAgent_A_Unified_Framework_for_Backdoor_Attacks_on_LLM-based_Agents.pdf`

**Method:** A modular stage-aware runtime with injection hooks, component-local attack wrappers, configurable agent execution, and structured trajectory logging; benchmark evaluations across QA, Code, Web, and Drive; seven named attacks; clean task accuracy, attack success rate, and attacked task accuracy; family aggregation, poisoning-ratio and token-overhead analyses, and exploratory probability-based detection.

**Attack surface:** Author-reported: planning artifacts, external memory or retrieval content, and tool/environment feedback. Attacks modify one component or its outputs, which may influence later context and state. Agent Web includes multimodal perception and action, with interface misdirection such as incorrect purchases described as a harm example.

**Relevance:** HIGH confidence analyst inference: the paper explains mechanisms relevant to why Web AI agents could acquire additional security risks through persistent intermediate artifacts, planning/memory/tool interfaces, and recurrent feedback. Its Web evaluation demonstrates heterogeneous backdoor susceptibility across four multimodal backbones. It does not directly compare matched standalone LLMs with Web agents, so it cannot establish a quantitative increase in vulnerability caused by agency.

**Limitations:** Controlled benchmark coverage is acknowledged as incomplete. No direct standalone baseline, concrete logged trajectory, named dataset sizes, numerical step budgets, run counts, uncertainty intervals, or full attack/detection configurations are supplied. Web results vary sharply across model and attack. Abstract persistence terminology differs from Table 6 ASR labeling; selected prose examples conflict with tables. The linked implementation and data were not reviewed.

## Don’t Click That: Teaching Web Agents to Resist Deceptive Interfaces

[Summary](summaries/dont_click_that_teaching_web_agents_to_resist_deceptive_interfaces_comprehensive_summary.md) · Source: `12_Contextual_Borderline/Dont_Click_That_Teaching_Web_Agents_to_Resist_Deceptive_Interfaces.pdf`

**Method:** DUDE evaluates screenshot, task, and candidate click using a ternary label and confidence; Stage 1 uses asymmetric hybrid-reward learning, Stage 2 summarizes persistent failures with successful anchors into contextual guidance, and inference gates execution with rejection/rethinking. RUC supplies 1,407 annotated examples; general reported evaluation uses 200 tasks across four domains, with Stage-1 training assessed separately through ablation.

**Attack surface:** Visible webpage interfaces: deceptive pop-ups, fake download or continuation buttons, misleading visual hierarchy, preselected subscription controls, overlays, urgency cues, and commercial prompts misaligned with the user's task. Purely backend exploits without visible manifestations are outside the defense's stated scope.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper illustrates how untrusted visual interfaces can redirect task-driven agents from perception into harmful or intention-misaligned clicks. Its evaluator gate addresses this environment-to-action boundary. It does not directly compare agents with standalone LLMs, so it cannot establish the size or existence of a matched agent-versus-standalone vulnerability difference.

**Limitations:** Static screenshots; no asynchronous live-environment validation; English-focused data; ecological rather than maximal adversariality; visual-only coverage; evaluator-dependent task regressions; single-stage DFR increases; no matched standalone-LLM baseline; missing uncertainty estimates; unresolved step accounting, table averages, test-suite relationships, transfer denominator, confidence thresholds, and confidence-adjustment formula/rationale.

## DoomArena: A Framework for Testing AI Agents Against Evolving Security Threats

[Summary](summaries/doomarena_a_framework_for_testing_ai_agents_against_evolving_security_threats_comprehensive_summary.md) · Source: `12_Contextual_Borderline/DoomArena_A_framework_for_Testing_AI_Agents_Against_Evolving_Security_Threats.pdf`

**Method:** A modular security-testing layer uses attack configurations, reusable attack implementations, environment-specific gateways, success filters, and optional aborting defenses. Evaluations use 50 airline tasks, 115 retail tasks, 114 Reddit tasks, 192 Shopping tasks, and a stated 39-task OSWorld subset. Metrics are attack success, legitimate task success with and without attacks, and joint-success stealth.

**Attack surface:** Malicious user conversations; queried product catalogs and databases; webpage banners using accessibility attributes; pop-ups with hidden accessibility-tree-like instructions; screenshot overlays in desktop environments. Attacker control and success criteria differ across these surfaces.

**Relevance:** MEDIUM confidence, analyst inference: DoomArena provides evidence about mechanisms relevant to why web agents may be vulnerable, including attacker-controlled webpage content, hidden accessibility representations, repeated observation/action loops, and tools that enact malicious requests. Its own experiments do not directly compare standalone LLMs with matched agent implementations. Statements about such a comparative gap on page 2 summarize cited prior work, not DoomArena experiments.

**Limitations:** No matched standalone-model control; text-only browser evaluation; restricted LlamaGuard category selection; abort-based judge defense can eliminate attacked-task utility; conditional combined-attack denominators; unclear browser/desktop uncertainty procedures; incomplete exact execution configuration; unresolved main/appendix numerical discrepancies; Figure 3 raw trend data and Figure 5 exact category data unavailable. No absent supplement or external source was reviewed.

## EvoCrawl: Exploring Web Application Code and State using Evolutionary Search

[Summary](summaries/evocrawl_comprehensive_summary.md) · Source: `12_Contextual_Borderline/EvoCrawl_Exploring_Web_Application_Code_and_State_using_Evolutionary_Search.pdf`

**Method:** A rapid Page Collection Module exchanges URLs with an Evolutionary Search Module. The latter searches element–interaction sequences using crossover, dependency-aware mutation, gene elimination, and weighted browser/database feedback. Modular XSS tracing and sitemap/replay/three-user IDOR analysis evaluate security consequences. Evaluation includes ten applications, 24-hour crawling, baseline comparisons, dependency ablation, selected known XSS, and new-finding reports.

**Attack surface:** Author-studied surfaces are HTML inputs, JavaScript-triggered controls, hidden forms and links, stored/reflected XSS injection points, and directly requested resources with differing user privileges. Some reported findings require trusted administrator/editor privileges, and some are outside developer threat models.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: the paper shows that browser interaction sequences reach persistent application states, executable inputs, and authorization-sensitive resources. These are relevant environmental pathways for web AI agents. It does not directly compare agents with standalone LLMs, measure prompt injection, or establish a comparative vulnerability rate.

**Limitations:** Indirect relevance to AI-agent security; no standalone-LLM comparison. Required-field formats, cross-user workflows, inferred privacy, URL redundancy, token handling, instrumentation access, limited statistical specification, benchmark-version differences, and unresolved table/prose inconsistencies constrain conclusions. Referenced software artifacts were not inspected.

## Gorilla: Large Language Model Connected with Massive APIs

[Summary](summaries/gorilla_comprehensive_summary.md) · Source: `12_Contextual_Borderline/Gorilla_Large_Language_Model_Connected_with_Massive_APIs.pdf`

**Method:** Closed-document analysis of all 22 supplied text pages and 16 supplied page renderings. The paper constructs APIBench, generates instruction–API pairs with GPT-4, fine-tunes LLaMA-7B with and without documentation, compares four retrieval settings, evaluates selected API structure using AST matching, and includes constraint, documentation-change, manual-execution, prompting, DocPrompting, and base-model analyses.

**Attack surface:** Analyst inference: candidate surfaces include API documentation appended to a prompt, the retriever/API database, generated repository and model arguments, and supporting execution code. The authors do not define these as attack surfaces or evaluate attacker control, prompt injection, privilege misuse, data theft, or malicious repositories.

**Relevance:** Analyst inference, MEDIUM confidence: the paper identifies retrieval-conditioned API generation and a gap between API correctness and complete-program execution. These components are relevant to investigating how external information can influence an agent's actions. It does not establish that web AI agents are more vulnerable than standalone LLMs and contains no direct adversarial comparison.

**Limitations:** Reliability study rather than security evaluation; single-call scope; asymmetric HuggingFace scoring; conflicting dataset and result values; qualitative documentation-update examples; unspecified API-disjoint splits; single LLM runs; limited manual execution sample; absent separate supplements and uninspected artifacts. Research relevance is interpretive, not an author-reported security finding.

## InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

[Summary](summaries/injecagent_benchmarking_indirect_prompt_injections_in_tool_integrated_large_language_model_agents_comprehensive_summary.md) · Source: `12_Contextual_Borderline/InjecAgent_Benchmarking_Indirect_Prompt_Injections_in_Tool-Integrated_Large_Language_Model_Agents.pdf`

**Method:** GPT-4-assisted generation and manual refinement of 17 user cases and 62 attacker cases; full cross-product yields 1,054 cases in each of base and fixed-prefix enhanced settings. Thirty agent configurations are evaluated through parsed tool requests. Direct harm requires a harmful invocation; data stealing requires extraction plus transmission using a GPT-4-simulated extraction response. Results distinguish ASR-valid, ASR-all, and output validity, with additional association, content-freedom, sensitivity, quality, and prompt-length analyses.

**Attack surface:** Attacker-modifiable fields in retrieved tool responses, including website snippets, emails, reviews, notes, tweets, profiles, calendar events, and product/task descriptions. The attacker attempts to convert external content into instructions for harmful tools. Evaluation conditions on successful retrieval and receipt of the injected response.

**Relevance:** ANALYST INFERENCE — MEDIUM confidence: The paper supports a mechanism relevant to why web-capable agents face additional security exposure: third-party content enters their decision context and can redirect available tools toward unauthorized actions or data disclosure. Browser snippets are one tested content type, but the benchmark also covers email, finance, home devices, and other domains. It does not directly compare matched standalone LLMs with agents or quantify a comparative vulnerability increase.

**Limitations:** Authors identify one fixed enhancement prefix, limited mixed benign/malicious content, single-turn attacks of at most two steps, and only two fine-tuned configurations. Additional analyst observations include simulated continuation-based evaluation, restricted tool menus, absent standalone baseline, imperfect proxy metrics, configuration/version confounding, missing uncertainty estimates, and unresolved text–table and plot–table inconsistencies.

## SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

[Summary](summaries/skilltrojan_comprehensive_summary.md) · Source: `12_Contextual_Borderline/SkillTrojan_Backdoor_Attacks_on_Skill-Based_Agent_Systems.pdf`

**Method:** Encrypt and partition an attacker-selected payload into indexed fragments; modify skill instructions and actions for trigger-conditioned emission; collect fragments during normal workflow execution; verify completeness, reconstruct by index, decrypt, and execute a side effect. Evaluate clean ACC and triggered ASR on EHR SQL and SWE-Bench Verified, plus scanner, fragmentation, encoding, trigger-prevalence, native-skill, and cross-framework analyses.

**Attack surface:** Installed skill packages combining natural-language specifications and executable scripts; conditional skill instructions, tool-output fields, run-local trajectories, fragment-emitting actions, and an attacker-modified verification action. Persistence resides in installed packages; reconstruction state is single-run only. Payload consequences depend on execution permissions.

**Relevance:** ANALYST INFERENCE; MEDIUM confidence. The paper demonstrates an additional execution-layer attack surface in agents that install reusable third-party skills: persistent executable code can cause hidden side effects while the underlying LLM remains unchanged and the returned answer appears benign. This supports a conditional explanation of agent risk beyond model output behavior. It does not directly compare standalone LLMs against web AI agents, establish a general vulnerability ratio, or use web browsing as its main benchmark.

**Limitations:** No direct standalone-LLM or dedicated web-agent comparison. Missing benchmark denominators, uncertainty, seeds, complete environment, judge identity, detailed Hybrid encoding, and independently inspected release artifacts. Native controls cover four open-weight models only. Cross-framework results use a separate unnamed coding benchmark and report ASR without clean ACC. Utility and superiority have model-specific exceptions, including a Table 7 prose–table conflict. Proposed sandboxing and runtime defenses are not evaluated.

## The Hidden Dangers of Browsing AI Agents

[Summary](summaries/the_hidden_dangers_of_browsing_ai_agents_comprehensive_summary.md) · Source: `12_Contextual_Borderline/The_Hidden_Dangers_of_Browsing_AI_Agents.pdf`

**Method:** Mixed security systems analysis: benchmark-informed selection of Browser Use; literature- and demonstration-informed architecture reconstruction; seven-layer MAESTRO mapping; narrative defense synthesis; white-box URL-validation analysis for version 0.1.44; and a GPT-4o-based credential-exfiltration proof-of-concept setup. No systematic review protocol or repeated-trial security benchmark is supplied.

**Attack surface:** Author-described surfaces include webpage HTML/DOM and screenshots, prompt construction, reasoning/planning loops, tool arguments and registries, sensitive-data replacement, URL allowlists, browser sessions, containers, remote debugging, telemetry, credential stores, shared memory, and multi-agent delegation. Only domain validation and prompt-driven credential exfiltration receive detailed Browser Use case treatment.

**Relevance:** ANALYST INFERENCE — The paper explains additional vulnerability pathways arising when an LLM repeatedly ingests untrusted web content and its outputs control browser actions, sensitive-data substitution, authenticated sessions, and infrastructure. Its Browser Use cases support this system-level mechanism. It does not directly measure browsing agents against matched standalone LLM baselines, so it cannot establish a general comparative vulnerability rate.

**Limitations:** One detailed open-source case; inaccessible proprietary implementations; unspecified attack repetition and success criteria; missing execution traces and complete dependency configuration; no controlled standalone comparison or implemented mitigation evaluation; qualitative appendix severity judgments; and unresolved internal ordering, numbering, duplication, and reference inconsistencies. Remediation in 0.1.45 is an author-reported historical claim.

## Toolformer: Language Models Can Teach Themselves to Use Tools

[Summary](summaries/toolformer_comprehensive_summary.md) · Source: `12_Contextual_Borderline/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools.pdf`

**Method:** Few API demonstrations condition candidate-call generation over CCNet text. Calls are executed and filtered by weighted continuation-loss reduction against no-call and no-response baselines. Retained calls are inserted into text for GPT-J fine-tuning. Evaluation compares unmodified GPT-J, CCNet-only fine-tuning, Toolformer with and without active calls, and larger models across factual completion, arithmetic, QA, multilingual QA, temporal tasks, perplexity, scaling, decoding, and qualitative call quality.

**Attack surface:** ANALYST INFERENCE: candidate boundaries include model-generated API names and arguments, externally returned QA or search text, translation output, date context, and the runtime insertion of responses before generation resumes. These are information-flow interfaces visible in the method, not demonstrated exploitable attack surfaces. The search tool retrieves Wikipedia snippets; the evaluated system is not an unrestricted interactive web browser.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence for architectural relevance: Toolformer shows how model-generated requests invoke external APIs and how returned text enters subsequent generation, providing a concrete interface to examine when studying external-content influence. The paper does not directly compare the security of web agents and standalone LLMs, introduce an attacker model, or measure vulnerability. Confidence in the proposition that web agents are more vulnerable based on this paper alone is UNKNOWN.

**Limitations:** Author-stated limits include no chaining, no interactive search, wording-sensitive call decisions, sample inefficiency, and no cost-aware selection. Evaluation permits at most one call per input. Analyst observations include absent adversarial tests, no security threat model, task-specific relaxed answer matching, generally missing evaluation sample counts and uncertainty statistics, external-model resource differences, and text-only visual coverage for pages 11–16.

## YuraScanner: Leveraging LLMs for Task-driven Web App Scanning

[Summary](summaries/yurascanner_comprehensive_summary.md) · Source: `12_Contextual_Borderline/YURASCANNER_Leveraging_LLMs_for_Task-driven_Web_App_Scanning.pdf`

**Method:** Goal-based crawler using semantic DOM abstractions, an LLM bridge with six-action history, concrete browser actuators, depth-one task discovery, CRUD-oriented ordering, separated form-filling prompts, and replay followed by Black Widow XSS testing. Evaluation includes ten-application manual task and coverage analysis and 20-application vulnerability testing, with four-hour tool runs.

**Attack surface:** AUTHOR-REPORTED: URLs, forms, input fields, JavaScript-driven interactions, authenticated administration interfaces, and workflow-dependent application states. ANALYST INFERENCE: Browser actuation and persistent application changes are relevant to studying agent risk, but hostile webpage control over the agent is not evaluated.

**Relevance:** ANALYST INFERENCE, MEDIUM confidence: The paper shows how an LLM becomes an action-taking web system through page observations, recent history, browser actuators, and state-changing tasks. The documented deletion of the only account illustrates consequences beyond textual output. It does not directly compare web-agent vulnerability with standalone LLM vulnerability, test prompt injection, or measure agent compromise. Its confirmed vulnerabilities concern target web applications.

**Limitations:** Partial execution is combined with full execution in the 61.3% headline. WordPress is excluded after prompt-size failures. Authentication is manually prepared. Model-selection scores, repeated-run uncertainty, costs, and exact GPT-4 snapshot are absent. Dataset naming and vulnerability-distance scope are ambiguous. Moodle is not direct XSS and has a reported no-impact developer assessment. Source access is vetted, artifacts were not supplied, and no direct standalone-LLM security comparison is conducted.
