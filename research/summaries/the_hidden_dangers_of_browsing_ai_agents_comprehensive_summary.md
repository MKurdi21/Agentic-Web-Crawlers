## Stage 0 — Document Accessibility Report

The supplied material contains readable text and rendered page images for physical PDF pages 1–32 of *The Hidden Dangers of Browsing AI Agents*. The visible printed page numbers agree with this sequence. The abstract, six numbered main sections, Appendix A, acknowledgements, and references are accessible. No page gap is apparent within that sequence; this does not independently establish that every author-associated artifact was supplied.

Visual inspection coverage: all 32 supplied page images were available and inspected alongside their supplied text. This is not a text-only review. The timeline on p. 3, architecture diagram on p. 5, Tables 1–11, URL-validation listing, prompt-template box, injected-payload box, and proof-of-concept listing were inspected visually. Appendix tables are rotated but readable in conjunction with their supplied text. The small text inside the timeline is less comfortable to read than the main body, so its broad structure is more secure than every fine typographic detail. There are no substantive mathematical equations or theorem proofs requiring equation OCR. OCR was not performed: the supplied text and images were sufficient for this analysis. Native text and images were compared where they expose important layout or ordering issues.

Supplementary access: no separate supplementary files, repository checkout, execution logs, conversation traces, advisory contents, or demonstration video were provided. The paper points to a GitHub proof-of-concept repository, its issue content, a security advisory, and outside publications. Those resources were not opened. References are treated as citations appearing in the paper, not as independently reviewed evidence. The attachment error mentioning a local image at `-` does not establish a missing numbered page: pages 1–32 are supplied separately and readable.

Evidence labels throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. HIGH confidence means the supplied material clearly supports the statement, not that the underlying scientific claim has been independently verified. The source hash is user-supplied and was not recomputed.

## 1. Plain-language orientation

This paper examines what can go wrong when a language model is connected to a browser and allowed to act for a user. A chatbot normally produces an answer. A browsing agent repeatedly reads a page, decides what to do, clicks or types, and reads the resulting page. That added ability makes the agent useful for shopping, email, authentication, and information retrieval, but it also places websites, browser software, credentials, execution machinery, and logs inside its security boundary. [A: pp. 1–3]

The central danger is that a webpage can contain text that looks like instructions. When that text enters the agent's prompt, the model may treat an attacker's directions as a new task. If the model's output drives browser actions, a mistaken interpretation can become an actual navigation, submission, disclosure, or other operation. The paper combines a layered threat taxonomy and a review of defenses with a white-box assessment of the open-source Browser Use project. White-box means the researchers inspect implementation details rather than testing only an opaque interface. [A: §§3–5]

Two concrete findings anchor the assessment. First, a URL allowlist check in Browser Use 0.1.44 could mistake the username portion of a crafted URL for its destination hostname. The authors associate this issue with CVE-2025-47241 and report remediation in 0.1.45. Second, attacker-controlled webpage content could redirect an agent toward credential exfiltration despite the use of sensitive-data placeholders. The paper presents a GPT-4o-based proof-of-concept setup, but supplies no repeated-trial attack-success measurements for that setup. [A/B: pp. 16–20]

For the reader's question—why web agents are more vulnerable than standalone LLMs—the paper supports a **mechanistic explanation**, not a measured comparative effect. **[D] Analyst inference:** web agents expose more entry points and give model decisions operational consequences through tools, authenticated sessions, memory, and infrastructure. The paper does not run the same attacks against a standalone LLM and a browsing agent under controlled conditions. Its central contribution is a system-level account of security risk supported by one inspectable implementation case, rather than a numerical estimate of how much more vulnerable agents are.

## 2. Document roadmap

The inventory below is the denominator for the coverage audit. Stable identifiers distinguish objects that the paper numbers ambiguously.

| ID | Original item | Pages | Role |
|---|---|---:|---|
| S0 | Title, abstract, author footnotes | 1 | Scope, claimed novelty, affiliations |
| S1 | §1 Introduction | 2–3 | Motivation and RQ1–RQ4 |
| S2.1 | §2.1 Introduction | 3 | Browsing-agent definition |
| S2.2 | §2.2 Agent Capabilities and Performance Benchmarks | 3–4 | Benchmark development |
| S2.3 | §2.3 WebVoyager Benchmark Results | 4 | Case-selection rationale |
| S3.1 | §3.1 Component Overview and unnumbered subsections | 5–8 | Architecture, perception, reasoning, privacy, prompts, feedback |
| S3.2.1 | §3.2.1 Existing Risk Analysis/Threat Modeling | 8–9 | Need for system-level framing |
| S3.2.2 | §3.2.2 MAESTRO overview and cross-layer discussion | 9–11 | Seven-layer mapping |
| S4.1 | §4.1 Overview | 11 | Initial-access/post-exploitation distinction |
| S4.2 | §4.2 and §§4.2.1–4.2.6 | 11–13 | Six initial-access defense categories |
| S4.3 | §4.3 and §§4.3.1–4.3.6 | 13–14 | Six containment/recovery categories |
| S4.4 | §4.4 Conclusion of the Mitigation Analysis | 14–15 | Isolation of trust |
| S5.1 | §5.1 Introduction and Disclosure Process | 15 | Assessment selection and disclosure |
| S5.2 | §5.2 High-Level Analysis | 15–16 | Browser Use implementation risks |
| S5.3 | §5.3 Vulnerability Index | 16 | Two vulnerability ratings |
| S5.3.1 | §5.3.1 Domain restriction bypass | 16–18 | URL parsing case |
| S5.3.2 | §5.3.2 Credentials exfiltration | 18–20 | Prompt-injection case |
| S6 | §6 Conclusion | 20–21 | Overall recommendations |
| A1 | Appendix A: Extended Threat Taxonomy | 21–29 | Layer-specific risk tables |
| R1 | Acknowledgement and References [1]–[34] | 30–32 | Credits and cited sources |

Visual inventory: F1 is the benchmark timeline called Figure 1 on p. 3; F2 is the architecture drawing also called Figure 1 on p. 5. T1–T11 preserve the original table numbers. ALG1 is Listing 1, the URL allowlist method, p. 17. ALG2 is Listing 2, the proof-of-concept setup, p. 20. V1 is the allowlist configuration/crafted-URL example, p. 17; V2 is the prompt-template box, p. 19; V3 is the injected-payload box, p. 20. No numbered equations, formal hypotheses, lemmas, propositions, or theorems are present. Distinct analysis records are X1 benchmark-based selection, X2 architectural threat mapping, X3 mitigation synthesis, X4 URL bypass, and X5 credential-exfiltration proof of concept.

## 3. Background and context

A **large language model (LLM)** is the model component that interprets prompts and generates responses. Here, some responses are structured action descriptions rather than prose. A **web agent** connects that model to browser functions and repeatedly uses observations to choose actions. The paper calls this a sense–plan–act loop. The **Document Object Model (DOM)** is the structured page representation that the agent can extract and parse; computer-vision-based perception instead analyzes rendered page images and interface elements. These two routes can expose different representations of the same page. [A: pp. 3, 5–6]

The paper divides agent behavior into **Perception**, **Reasoning**, **Planning**, and **External Tool Calls**. Perception converts or extracts inputs; reasoning evaluates possible outcomes; planning selects and sequences actions; tools execute browser or other functions. Although drawn separately, reasoning and planning are often carried out within the same iteration. Browser Use is described as combining perception, reasoning, and planning more closely than some advanced proprietary platforms. The latter comparison is based on literature and demonstrations, not direct access to those systems' implementations. [A: pp. 5–6]

**Prompt injection** occurs when malicious content in input or external data changes the model's behavior by overriding intended prompt constraints. **Credential exfiltration** means sending authentication information outside its authorized context. An **allowlist** permits only specified destinations. **Fully qualified domain name (FQDN)** validation is the paper's term for the domain-checking boundary examined in Browser Use. A **Common Vulnerabilities and Exposures (CVE)** identifier identifies a disclosed vulnerability, while the **Common Vulnerability Scoring System (CVSS)** supplies the score format used in Table 3. The paper reports scores but does not provide their full vector strings. [A: pp. 15–18]

The privacy mechanism matters because the model need not see a raw password for the surrounding system to misuse it. Browser Use can keep a local dictionary from placeholder names to real sensitive values, send placeholders to the model, and restore actual values in output before execution. Thus a model-generated instruction involving a placeholder may later become a real credential-bearing browser action. The paper describes restoration both in terms of final output to the user on p. 7 and execution on p. 8; the execution description is the security-relevant bridge. [A/D: pp. 7–8, 15–20]

## 4. Research problem and gap

**Existing problem [A]:** autonomous agents interact with dynamic web content and sensitive user data while executing actions with limited human intervention. The authors identify risks involving credentials, session tokens, application programming interface (API) keys, authentication, and impersonation. Their attack surface extends beyond model behavior into web drivers, runtime environments, and dependencies. [p. 2]

**Shortcomings attributed to prior approaches [A]:** the paper says traditional AI-oriented threat modeling has emphasized model-level threats such as poisoning, backdoors, and adversarial examples. It argues that browsing systems additionally require analysis of prompt handling, user goals, external pages, operational controls, and infrastructure. This is the authors' positioning of prior work, not an independently validated description of all prior security research. [pp. 8–10]

**Research gap [A]:** the abstract claims the first end-to-end threat model for browsing agents. The work adopts an existing MAESTRO framework and maps browsing-agent components and threats into it. The novelty claim therefore concerns the browsing-agent application and synthesis, rather than invention of MAESTRO itself. Priority cannot be checked within closed-document mode. [pp. 1, 9–10]

**Motivation [A]:** broad adoption makes implementation weaknesses consequential; Browser Use is reported to have over 60,000 repository stars at publication. This is a historical adoption statement, not a current count. **Scope:** system-level threat modeling, defense synthesis, and a Browser Use case study. The mitigation discussion explicitly places traditional external-tool security and integration practices outside its detailed scope, even though infrastructure and tool risks are included in the overall taxonomy. [pp. 2, 11]

## 5. Research questions / objectives / hypotheses

The paper explicitly states four research questions on p. 2:

1. **RQ1:** What structural and systemic factors make open-source autonomous browsing agents such as Browser Use susceptible to prompt injection and related attacks?
2. **RQ2:** Do inherent architectural choices introduce systemic vulnerabilities that adversaries can exploit?
3. **RQ3:** How do Perception, Reasoning, Planning, and Tool Execution contribute to the feasibility and severity of credential exfiltration, unauthorized task execution, and agent-observability exploits?
4. **RQ4:** To what extent can sanitization, architectural isolation, formal analyzers, and other mitigations reduce prompt-injection success under realistic deployments?

The stated objectives are to build a holistic threat account, analyze Browser Use, demonstrate exploitable weaknesses, and provide deployment guidance. The paper does not specify formal statistical hypotheses. It also does not formulate the reader's standalone-LLM comparison as a controlled experimental hypothesis. RQ1–RQ3 receive architectural reasoning and case evidence. RQ4 receives a literature-based defense synthesis and quoted benchmark outcomes from cited work, rather than a new Browser Use mitigation experiment. This distinction prevents cited defense performance from being mistaken for results produced by this study.

## 6. Assumptions / threat model

The paper's threat model is broad rather than a single formally bounded adversary specification. The main concrete prompt-injection attacker can place malicious instructions in webpage HTML or issue content that the agent encounters during an otherwise legitimate browsing task. The attacker need not be the legitimate user: an issue linked from a repository can deliver the payload indirectly. The malicious content becomes parsed page data and then model context. [A: pp. 18–20]

Assets include user credentials, API keys, session cookies, private content, task integrity, browser sessions, host resources, policy constraints, and monitoring integrity. The intended trusted side includes the user's objective, system instructions, local sensitive-data mapping, authorized domain policy, and security controls. The untrusted side includes external pages and their extracted text; the appendix additionally considers compromised agents, plugins, knowledge stores, images, containers, and logs. These are different attacker capabilities across different scenarios, not capabilities demonstrated simultaneously by one attacker. [A/D: pp. 7–10, 21–29]

The URL case assumes an active allowlist containing a trusted domain and an attacker-influenced destination URL. The shown configuration contains `example.com`. The crafted URL's apparent trusted text is in the authentication portion, whereas the destination is `localhost` on port `8080`. The supplied code's empty-allowlist branch returns true, so the deny-by-default description applies only when an allowlist is configured. [A/B: pp. 16–17]

The credential case assumes sensitive values have been supplied to the agent and can be restored through its sensitive-data mechanism. Listing 2 uses two demonstration values and GPT-4o. No domain allowlist is shown in that listing. Therefore the displayed credential proof of concept does not, by itself, demonstrate a composed chain that first bypasses a configured allowlist and then exfiltrates credentials. The authors discuss such chaining as possible. [A/B/D: pp. 17–20]

No uniform attacker budget, query limit, success threshold, network topology, operating-system configuration, or explicit excluded-capability list is supplied. General claims about sandbox breakout, multi-agent compromise, and telemetry attacks in Appendix A are threat scenarios, not outcomes established by the Browser Use experiment.

## 7. Methodology

The document is a mixed **cybersecurity systems analysis**, **narrative literature synthesis**, and **white-box vulnerability case study**. It is not a systematic review or a controlled large-sample attack benchmark. The methodology has five connected parts.

**Selection:** §2 surveys benchmark evolution and reproduces WebVoyager performance figures to justify choosing a capable open-source implementation. The paper describes WebVoyager as 300 user tasks across 15 websites, with browser observations combining screenshots and DOM information. Those are properties attributed to cited benchmark work, not a newly collected security dataset. [A: pp. 3–4]

**Architecture reconstruction:** §3 combines published descriptions, demonstrations, and Browser Use implementation knowledge. It distinguishes DOM parsing from visual extraction, structured model outputs from tool execution, and local secret replacement from external inference. The paper names LangChain, Chromium, and HTML parsing as Browser Use components. It describes other platforms' specialized perception models and Proxy's small language model, but these descriptions are not source-code audits of those proprietary platforms. [A: pp. 5–8, 15]

**Threat mapping:** MAESTRO expands to Multi-Agent Environment, Security, Threat, Risk, and Outcome. The seven layers are foundation models; data operations; agent frameworks; deployment and infrastructure; evaluation and observability; security and compliance; and agent ecosystem. Table 2 maps components to layers, and Appendix A assigns scenario-level severity by estimated exploitation likelihood and potential impact. No numerical weighting or calibration procedure is provided. [A: pp. 9–10, 21]

**Defense synthesis:** §4 groups six initial-access and six post-exploitation approaches. It explains their intended mechanisms, cites existing research, and recommends combining prevention, detection, and containment. There is no implemented defense comparison, latency study, or cost study within Browser Use. [A: pp. 11–14]

**White-box case:** §5 examines domain checking and prompt generation. The URL vulnerability is tied to version 0.1.44 and `browser_use/browser/context.py`. Prompt construction is tied to `browser_use/agent/prompts.py` and `browser_use/agent/system_prompt.md`. Listing 1 exposes the faulty parsing; Listing 2 instantiates an agent using `langchain_openai.ChatOpenAI`, model `gpt-4o`, two sensitive-data entries, and conversation logging. The task asks the agent to inspect repository issues and their descriptions. [A/B: pp. 16–20]

Configuration not specified: operating system, hardware, browser version, LangChain version, exact model snapshot, temperature, random seed, trial count, timeout, attack sampling procedure, success rubric, human evaluator protocol, confidence intervals, or statistical tests. There are no training/validation/test splits, annotation procedures, or newly gathered participant samples. Missing details are unreported, not assumed defaults.

## 8. Experiments / analyses

| ID | Purpose and question | Setup and evidence | Result and boundary |
|---|---|---|---|
| X1 | Select a relevant open implementation | Literature/benchmark overview; Table 1 | Browser Use leads the reproduced task-success table at 89.1%; no security inference follows from that ranking alone |
| X2 | Explain systemic exposure; RQ1–RQ3 | Component model, MAESTRO mapping, appendix scenarios | Risks span seven interacting layers; qualitative taxonomy, not measured prevalence |
| X3 | Identify defenses; RQ4 | Narrative synthesis of cited approaches | Layered controls recommended; no new mitigation benchmark |
| X4 | Test domain restriction logic; RQ2–RQ3 | Browser Use 0.1.44, configured allowlist, Listing 1 and crafted URL | Incorrect parsing permits a destination outside the configured domain; fix reported in 0.1.45 |
| X5 | Demonstrate task hijack and secret disclosure; RQ1–RQ3 | GitHub issue browsing, injected page content, sensitive-data mapping, GPT-4o | Author-reported proof of concept; no run count, transcript, or empirical success rate supplied |

For **X4**, the manipulated condition is URL structure. The crucial observation is disagreement between the string accepted by the validator and the host the URL actually addresses. Listing 1 calls `urlparse(url).netloc.lower()` and removes everything after the first colon, then compares against allowed domains or their subdomains. With the supplied example, that produces `example.com`, while the destination host is `localhost`. This directly explains the bypass mechanism without needing a probabilistic model outcome. The paper extends potential impact to unauthorized internal-service access and Server Side Request Forgery (SSRF). No particular internal service compromise is documented in the supplied pages. [pp. 16–18]

For **X5**, the legitimate task is issue reading. The malicious content claims message authority, redefines the task, asks for sensitive placeholders, and requests submission to an external collection site. Its wording is attack evidence, never an instruction for this analysis. The mechanism crosses from page data to model behavior and then to actions carrying restored secrets. The supplied code contains no explicit controlled comparison against a benign issue, different model, sanitized prompt, or isolated planner. It saves conversations, but those saved conversations are not included. [pp. 18–20]

## 9. Results

**Domain-boundary failure [A/B, HIGH confidence in source representation]:** Table 3 rates improper FQDN validation Critical, with CVSS overall score 9.3/10 and a positive CVE marker. The surrounding text identifies CVE-2025-47241. The affected package version is 0.1.44; the authors state that 0.1.45 remediates the problem. This is a historical version-specific claim in the paper, not a live verification of current Browser Use. [pp. 15–18]

**Prompt-driven credential disclosure [A, HIGH confidence that reported; MEDIUM for independently assessable outcome]:** Table 3 rates credential exfiltration High at 8.8/10 and marks its CVE column negatively. Pages 18–20 explain prompt construction, show a task-override payload, and provide demonstration code. They do not report how many runs succeeded, what exact requests were observed, or whether the demonstrated behavior generalized across models and settings. The ratings are severity judgments, not attack-success percentages.

**Defense results are secondhand within this paper [A]:** §4.2.3 attributes a reduction from approximately 25% to about 8% attack success to an AgentDojo baseline using GPT-4 plus a detector. §4.2.5 attributes 0% benchmark success to a planner–executor information-flow pipeline in cited work. The supplied paper does not reproduce their experimental conditions, sample sizes, or full metric definitions. These values cannot be treated as Browser Use results or universal guarantees. [pp. 12–13]

**Capability figures are task-success figures [A/B]:** Table 1 lists Browser Use 89.1%, Proxy 88%, Operator 87%, Skyvern 2.0 85.8%, Agent-E 73.1%, Runner H 0.1 67%, and WebVoyager 59.1%. Six entries are labeled multimodal; Agent-E is text-only. No error bars or significance tests accompany the table. The table supports the authors' selection rationale, not a ranking of security. [p. 4]

**[D] Research relevance:** the case explains why a vulnerable browser boundary and a model's susceptibility to malicious text can compound. The model alone does not parse a URL into a network request or restore a local password into a form submission; the agent's surrounding implementation supplies those effects. The paper demonstrates particular system weaknesses, while the general comparison with standalone models remains an inference.

## 10. Figure-by-figure interpretation

### F1 — Figure 1, Browsing Agents Benchmark Timeline, p. 3

This is a categorical timeline, not a quantitative performance plot. Connected blue chevrons contain the visible labels 2017, 2023, 2023, 2024, and Ongoing. Callouts identify MiniWoB, Mind2Web, WebArena, and next-generation WebVoyager. The duplicated 2023 reflects separate milestones. MiniWoB is associated with controlled simple navigation; Mind2Web with offline human action traces; WebArena with more realistic browser interaction; and WebVoyager with real-browser and multimodal evaluation. [B]

There is no y-axis, measured unit, linear time scale, confidence interval, statistical marker, or performance trajectory. The changing blue shades encode progression visually, not a reported numerical variable. The arrows should not be interpreted as showing equal elapsed time or a measured improvement between milestones. Nearby text explains fixed action-sequence limitations and increasing realism. The figure supports historical framing and case selection, not the security evaluation.

### F2 — Second object labeled Figure 1, general browsing-agent flow, p. 5

The drawing contains a user-task oval; boxes for Perception, Extracted Data, Reasoning, Planning, Browsing Engine, and Action; and an External Tools oval. The top-row flow moves from Perception through Extracted Data to Reasoning and Planning. Planning points down to Action. Action and External Tools have a two-way link; External Tools connect back toward the Browsing Engine; Perception and Browsing Engine have a two-way vertical connection. [B]

Purple boxes mainly mark cognitive/action stages, green boxes mark browsing/data stages, and gray ovals mark the task and external tools. There are no measured axes or quantities. The resulting loop explains how actions change the environment that is perceived next. It does not draw explicit security policy checks, credential boundaries, or planner–executor isolation. Its duplicated Figure 1 numbering is a document inconsistency; F1/F2 are analyst identifiers used to avoid confusion.

## 11. Table-by-table interpretation

### Table 1 — WebVoyager task performance, p. 4

Rows are agents; columns are modality and overall success rate in percent. All seven exact values appear in §9 and §20. Browser Use is highest at 89.1%; WebVoyager is lowest at 59.1%; no ties occur. No shared rerun protocol, uncertainty estimates, task-level denominators for each cited result, or significance analysis are provided. The preceding benchmark description reports 300 tasks and 15 sites, but the paper does not establish identical configurations for every reported agent score.

### Table 2 — Component-to-MAESTRO mapping, p. 10

This conceptual table maps seven layers to components: models/encoders/embeddings; DOM, screenshots, cookies, and vector indexes; runtime prompts and tool registry; browsers, containers, worker pools, proxies, and orchestration; traces, action logs, token and latency metrics, screenshots and replay; credentials, domain lists, throttles, filters and policies; and multi-agent protocols, knowledge bases, and workflows. There are no numerical results or severity comparisons. Its contribution is architectural coverage and cross-layer reasoning.

### Table 3 — Two Browser Use vulnerabilities, p. 16

Columns are title, severity, CVE marker, and CVSS overall score. Domain restriction bypass is Critical, `[+]`, 9.3/10; credential exfiltration is High, `[-]`, 8.8/10. The marker meaning is clarified by surrounding prose for the first vulnerability; the second has no CVE identifier supplied. No score vectors, scoring version, assessor agreement, or uncertainty are given. These are different vulnerabilities, not comparison groups in an experiment.

### Table 4 — Foundation-model threats, p. 22

The five rows are prompt injection **Critical**; model bias **Medium**; over-reliance on the LLM **Medium**; jailbreaking **High**; and covert backdoor trigger **Medium**. Impacts include unauthorized actions and leakage, discriminatory decisions, unverified hallucinated actions, protected-information disclosure, and hidden behavior. Examples include malicious credential instructions, biased product ranking, a hallucinated click after an empty DOM, debugging-style instruction abuse, and a special URL trigger. These are author-provided scenarios, not five demonstrated attacks.

### Table 5 — Data-operations threats, p. 23

Rows are DOM poisoning **Critical**; vector-store poisoning **Low**; clickjacking **Medium**; encoding/format smuggling **Medium**; cookie/local-storage manipulation **Medium**. The table traces how altered page data, poisoned retrieval, visual overlays, unusual encodings, or changed browser state can redirect interpretation or authenticated behavior. Examples are compressed here; their essential mechanisms and severity labels are preserved. The screenshot/DOM mismatch described for clickjacking is a taxonomy example rather than an evaluated multimodal attack.

### Table 6 — Agent-framework threats, p. 24

Rows are tool misuse **High**; prompt-template tampering **High**; working-memory poisoning **Low**; infinite-step or looping plans **High**; tool-registry manipulation **Medium**. These affect action arguments, governing templates, persistent context, action scheduling, and available capabilities. The table distinguishes selecting a legitimate tool with dangerous arguments from changing which tools exist. Its resource-exhaustion example involves repeated unsuccessful page interaction, not a measured token-cost experiment.

### Table 7 — Deployment/infrastructure threats, p. 25

Rows are container breakout **Medium**; sandbox-profile misconfiguration **High**; compromised base image **Medium**; remote-debug-port exposure **Low**; autoscaling resource exhaustion **High**. Impacts range from host access and credential theft to live-session takeover and service outages. Port 9222, 500 queued tasks, and 400 Chromium pods appear only in illustrative scenarios. They are not configuration measurements or results from the Browser Use case. No experiment establishes the relative frequency of these threats.

### Table 8 — Evaluation/observability threats, p. 26

Rows are sensitive-data leakage in telemetry **Critical**; telemetry spoofing/falsification **Medium**; logging-pipeline denial of service **High**. Screenshots can preserve sensitive data, forged success messages can hide failures, and excessive logs can suppress visibility. The illustrative tools and dashboards are examples, not an audited deployment. This table is important because monitoring can become both a disclosure channel and a target.

### Table 9 — Duplicated observability content under an infrastructure caption, p. 27

The three rows, examples, impacts, and severity labels visibly repeat Table 8, while the caption calls them Deployment & Infrastructure risks. This is a caption/content inconsistency and duplicated material. It is accounted for separately, but it does not add three distinct threats. The supplied work does not explain the duplication.

### Table 10 — Security/compliance threats, p. 28

Rows are credential-vault compromise **Critical**; rate-limit bypass **High**; content-filter evasion **High**. These concern access to stored secrets, distributed circumvention of throttles, and encoded or visually disguised disallowed content. The example of 1,000 IPs driving 50 k tool calls/min is an illustrative attack scenario, not measured load. The vault example includes a mis-scoped identity/access role; no actual vault configuration is assessed in the paper.

### Table 11 — Agent-ecosystem threats, p. 29

Rows are malicious-agent injection **Critical**; collusion/Sybil swarm **Medium**; shared-knowledge-base poisoning **Medium**; emergent feedback loop **Medium**; privilege escalation via delegation **High**; instruction leakage/prompt reflection **Critical**. They extend risk to peer trust, distributed quotas, communal memory, recursive agent calls, delegated authority, and leaked internal instructions. Ten agents and 10,000 visits/hour are illustrative numbers. No multi-agent implementation is experimentally evaluated. Together Tables 4–11 provide breadth, but their severity categories are qualitative scenario assessments rather than empirical rankings.

## 12. Diagram / architecture interpretation

The architecture's key security relationship is a cycle: task → perception → extracted page data → reasoning → planning → action/tools → browser state → new perception. An external page is therefore repeatedly reintroduced into decision-making. **[D] Analyst interpretation:** each iteration offers another opportunity for untrusted data to be promoted into apparent authority, while tool execution gives that promotion consequences outside the model. [pp. 5–10]

The paper's sensitive-data workflow adds a second path: local secret dictionary → placeholder in model context → placeholder-bearing model output → restored real value → execution. Its purpose is to avoid exposing raw secrets during inference, but the paper argues that it does not by itself constrain where restored values are used. The diagram on p. 5 does not explicitly show this path; it is described in text on pp. 7–8 and implicated in §5. [A/D]

The proposed planner–executor defense is a separate conceptual architecture, not a deployed Browser Use result. A planner receives trusted inputs; an executor interacts with all data, including untrusted observations; a monitor controls what information can influence planning. Formal analyzers add checks between proposed actions and execution. The source supplies these ideas in prose rather than as an additional drawn architecture. Their stated benefit depends on the monitor, policy definitions, and trusted-data boundary actually being enforced. [A: pp. 12–13]

## 13. Equations and mathematical concepts

There are no major equations, losses, optimization objectives, proofs, or formal security theorems in the supplied paper. Numerical scores and percentages should not be mistaken for a mathematical model. The two code listings are the relevant formal artifacts.

**ALG1, Listing 1 [p. 17]:** input is a URL string and configured allowed-domain list; output is a Boolean permission decision. With no configured list it returns true. Otherwise it parses the URL's network-location string, lowercases it, splits on a colon, and accepts exact matches or suffixes beginning with a dot plus an allowed domain. Exceptions produce a logged error and false. The defect is the choice of string field and delimiter processing: authentication and host information can coexist in the network-location string. The supplied crafted example exposes the mismatch. The listing is a concrete implementation, not pseudocode for a new algorithm.

**ALG2, Listing 2 [p. 20]:** imports asynchronous support, ChatOpenAI, and Browser Use's Agent; defines the issue-reading task; supplies two sensitive values; selects GPT-4o; enables conversation saving; and runs the agent. The listing ends with `await browser.close()`, but a `browser` variable is not defined in the displayed code. **[B/D]** The snippet alone is therefore not a fully self-contained reproducibility package; this observation does not establish whether the authors' full environment executed successfully.

**[C] Optional arithmetic illustration:** the two cited detector rates imply an approximate absolute reduction of 25 − 8 = 17 percentage points, and an approximate relative reduction of (25 − 8)/25 = 68%. Both operands are approximate, the calculation is analyst-derived, and the underlying results are attributed to other work. Neither quantity is a newly measured effect in this paper. No other derived performance numbers are needed for the conclusions.

## 14. Interpretation and discussion

**RQ1:** the strongest answer is that untrusted page content is placed in model context and can impersonate instructions, while the framework executes resulting actions. The proof-of-concept example makes that pathway concrete. Placeholder restoration can turn a redirected action into sensitive-data disclosure. The authors also emphasize insufficient contextual boundaries and defensive monitoring. [pp. 15–20]

**RQ2:** the domain parser supplies a direct implementation-level example of a security boundary failing. The broader architecture discussion identifies why combining observation, planning, memory, and tools can propagate a local error. The single case does not establish that all browsing architectures share the same vulnerability. [pp. 9–10, 16–18]

**RQ3:** perception admits attacker-controlled content; reasoning/planning may adopt a substituted objective; tools carry it out; browser sessions and credentials increase consequences; logs and multi-agent channels may expose or amplify effects. Only part of this chain is concretely assessed. Appendix risks involving containers, peer agents, or telemetry remain scenarios. [pp. 5–10, 21–29]

**RQ4:** defenses are organized and explained, but their effectiveness in this exact Browser Use configuration is unresolved. The quoted 8% and 0% figures are attached to cited setups, without reproduced details. The defensible conclusion is that several control mechanisms are relevant, not that this study determines a realistic deployment-wide residual risk. [pp. 11–14]

Consistency findings are substantive. First, pp. 15 and 18 describe webpage content as appended at the prompt end, and the p. 19 template places it last, but the numbered construction list on p. 18 places parsed elements before the user task. Exact message ordering is unresolved. Second, p. 19 describes a newly embedded HumanMessage, whereas the visible p. 20 payload uses SystemMessage wording. Both indicate authority impersonation, but the naming differs. Third, p. 17 refers to §5.4.2, which is absent; the relevant credential subsection is §5.3.2. Fourth, the architecture and timeline share Figure 1 numbering. Fifth, Table 9 repeats Table 8 under a different layer caption. Sixth, reference [13] and reference [23] display the same arXiv identifier despite different titles and authors; the paper alone cannot resolve the citation metadata. [B]

The model-size discussion also needs care. Page 6 favors general-purpose models over smaller specialized models; p. 8 explicitly says whether smaller models are inherently more vulnerable remains inconclusive; p. 11 reports a tendency favoring larger models while emphasizing post-training. These are differently qualified statements, not a demonstrated model-size effect in this study.

## 15. Contributions and novelty

**Conceptual [A]:** an end-to-end browsing-agent threat account and application of seven-layer MAESTRO analysis. The abstract's first-of-its-kind claim is preserved as an author claim, not verified historical priority.

**Methodological [A]:** component mapping, a cross-layer propagation narrative, and a taxonomy connecting threat descriptions, impacts, severities, and browser-agent examples. The framework itself is adopted from cited work.

**Implementation/empirical [A/B]:** a white-box domain-validation finding, a named CVE, affected/fixed version statements, and a prompt-injection credential-exfiltration proof-of-concept setup. The domain case is particularly traceable because the supplied code and URL illustrate the failure directly.

**Practical synthesis [A]:** defense-in-depth guidance spanning prompt handling, model behavior, planning boundaries, action policies, sessions, monitoring, throttling, safe mode, and regression testing.

The paper does not contribute a new dataset, benchmark, trained model, theorem, formal proof, measured defense implementation, or systematic comparative security evaluation. **[D] Research contribution to the reader's question:** it shows how model-level instruction confusion can be coupled to ordinary software flaws and privileged execution, explaining a broader system exposure than text generation alone without measuring a universal vulnerability multiplier.

## 16. Limitations

### Authors' stated limitations

The authors state that proprietary agents' exact architectures cannot be described because they are closed source; their reconstruction relies on publications and demonstration observations. They acknowledge that the relationship between smaller models and inherent vulnerability is inconclusive and requires further empirical studies. They explicitly say input sanitization alone is insufficient in most situations and that static detectors and purely model-based defenses can be evaded. They place traditional external-tool security practices outside the detailed mitigation scope. [pp. 5, 8, 11–12]

For the domain restriction, the authors say their hypothesis that the mechanism was intended to complement sensitive-data handling lacks concrete implementation evidence. Appendix A acknowledges that severity can vary markedly with the concrete exploit vector and deployment; the consolidated labels combine estimated likelihood with potential impact. These qualifications limit how broadly the ratings should be interpreted. [pp. 16, 21]

### Additional evidence-based analyst observations

**[D]** No controlled standalone-LLM comparison is supplied. No denominator, repeated trials, statistical uncertainty, or systematic attack corpus is supplied for credential exfiltration. Browser Use is the only detailed white-box case, despite mention of assessing several systems. The paper lacks a systematic-review search protocol, screening counts, inclusion rules, and evidence-quality assessment. It presents mitigation guidance without a new implemented evaluation. It reports CVSS scores without full vectors. Code and prompt-order inconsistencies complicate reproduction. Repository artifacts and logs are absent. These are observations about supplied evidence, not admissions attributed to the authors.

## 17. Threats to validity

The following labels are **analyst assessment [D]**, not a formal validity section written by the authors.

**Internal validity:** the URL code strongly identifies a parsing mechanism, but the prompt-injection demonstration does not isolate the separate causal contributions of prompt position, missing instructions, model choice, and placeholder substitution. The paper invokes beginning/end attention to explain risk without running a prompt-position ablation.

**External validity/generalizability:** one open-source implementation and a GPT-4o demonstration cannot establish the same exploitability in proprietary systems, all model families, or all contemporary deployments. The authors' architectural-similarity rationale is plausible positioning, not direct evidence about inaccessible implementations. Version-specific remediation further limits timeless claims.

**Construct validity:** task completion, vulnerability severity, attack success, and deployment safety are different constructs. Table 1 measures capability; Table 3 reports severity; neither is a probability that an arbitrary deployment will be compromised. Qualitative appendix ratings lack a numerical calibration method.

**Statistical conclusion validity:** there are no repeated-trial security statistics or confidence intervals to evaluate. Approximate rates quoted from cited literature do not supply the missing statistical basis for this case.

**Ecological validity:** a repository issue is a credible delivery channel within the demonstrated task, but the supplied paper does not measure production prevalence, user safeguards, network restrictions, or actual enterprise deployments. Appendix examples illustrate plausible environments without documenting observations from them.

**Reproducibility:** the code listing, paths, version, and model name help. Missing dependency pinning, model snapshot, complete execution environment, transcripts, exact issue artifact as supplied data, and the undefined browser variable impede an exact independent reproduction from these pages alone.

## 18. Future work and open questions

### A. Explicit author-proposed directions

The clearest explicit research need is further empirical study of model size and adversarial robustness. The paper also advocates ongoing adversarial testing, patching newly found exploits, adding regression cases, evaluating defenses continuously, and refining layered safeguards. Those are development/research recommendations rather than a scheduled experimental program. [pp. 8, 14, 21]

### B. Additional open questions [D]

How does attack success change when the same underlying model is used as a standalone text system versus a browser agent with controlled privileges? How much does secret restoration contribute independently of prompt injection? Does moving page content within the prompt change outcomes when all other variables are fixed? What residual risk remains under a configured allowlist after the URL fix? How effective are planner isolation and formal action policies against this exact issue-reading attack, and what task-completion overhead do they introduce? How stable are results across model snapshots, trial repetitions, and website layouts? How should taxonomy severity be calibrated to actual deployments? The paper motivates these questions but does not answer them quantitatively.

## 19. Terminology and notation glossary

| Term | Meaning in this analysis |
|---|---|
| LLM | Large language model; interprets prompts and produces responses or action descriptions |
| SLM | Small language model; discussed as a specialized alternative, with robustness unresolved |
| Web/browsing agent | Model-connected system that observes websites and executes browser actions |
| DOM | Document Object Model; structured webpage content used for extraction |
| HTML | HyperText Markup Language; page content that can carry attacker-controlled text |
| Perception | Input/page extraction and representation stage |
| Reasoning / Planning | Evaluating options and sequencing actions; often combined operationally |
| Tool call | Structured request to a browser or other callable capability |
| Prompt injection | Malicious input that redirects intended model behavior |
| Jailbreaking | Prompts designed to bypass model safety/content restrictions |
| Exfiltration | Moving sensitive information to an unauthorized destination |
| Sensitive-data placeholder | A substitute name later mapped back to a real secret |
| FQDN | Fully qualified domain name; the paper's domain-validation terminology |
| Allowlist | Explicit permitted destinations; configured list checked before navigation |
| SSRF | Server Side Request Forgery; unauthorized requests toward protected endpoints in the domain-case discussion |
| CVE / CVSS | Vulnerability identifier / severity scoring system; not attack-success metrics |
| MAESTRO | Multi-Agent Environment, Security, Threat, Risk, and Outcome; seven-layer framework |
| PII | Personally identifiable information |
| API | Application programming interface |
| CoT | Chain of Thought; intermediary reasoning discussed as complicating transformations |
| XSS | Cross-Site Scripting; malicious script injection used in taxonomy examples |
| Session isolation | Clearing/separating context to limit persistence between interactions |
| Information-flow control | Rules constraining movement from sensitive sources to output channels |
| Source / sink | Origin of protected data / potential disclosure destination |
| Telemetry | Logs, traces, screenshots, and metrics used to observe operation |
| DoS | Denial of service; overwhelming service or logging resources |
| Sybil swarm | Multiple attacker-controlled agent identities coordinating actions |
| MCP, A2A, AGNTCY | Named ecosystem/protocol examples; expansions and detailed semantics are not supplied |
| ASB | Benchmark acronym mentioned on p. 14 without expansion in the supplied discussion |
| Top-K | Retrieval notation appearing in an example; K is not assigned a value |

No mathematical symbol inventory is needed beyond code identifiers and percentages. Platform names and security-system names in appendix examples are not treated as independently defined or audited technologies.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Browser Use adoption | over 60,000 | repository stars | As of publication, not current | Author-reported | p. 2 |
| WebVoyager benchmark size | 300 | user tasks | Cited benchmark description | Author-reported | p. 4 |
| Website coverage | 15 | websites | Same description | Author-reported | p. 4 |
| Browser Use success | 89.1 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| Proxy success | 88 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| Operator success | 87 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| Skyvern 2.0 success | 85.8 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| Agent-E success | 73.1 | % | Text-only task performance | Author-reported; visually readable | p. 4, T1 |
| Runner H 0.1 success | 67 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| WebVoyager success | 59.1 | % | Multimodal task performance | Author-reported; visually readable | p. 4, T1 |
| MAESTRO layers | 7 | layers | Architecture taxonomy | Author-reported | pp. 9–10 |
| Detector baseline attack success | approximately 25 | % | Cited GPT-4/AgentDojo setting | Author-reported, approximate | p. 12 |
| With detector | about 8 | % | Same cited setting | Author-reported, approximate | p. 12 |
| Planner-isolation attack success | 0 | % | Cited benchmark pipeline; not universal | Author-reported | p. 13 |
| Approximate detector difference | 17 | percentage points | 25 − 8; cited approximate operands | Analyst-derived | pp. 12–13; §13 here |
| Approximate relative reduction | 68 | % | (25 − 8)/25 × 100 | Analyst-derived | p. 12; §13 here |
| Domain bypass CVSS | 9.3/10 | score | Critical; CVE-2025-47241 | Author-reported; visually readable | p. 16, T3 |
| Credential exfiltration CVSS | 8.8/10 | score | High; no CVE supplied | Author-reported; visually readable | p. 16, T3 |
| Affected version | 0.1.44 | package version | Domain restriction case | Author-reported | p. 16 |
| Fixed version | 0.1.45 | package version | Authors report remediation | Author-reported | p. 18 |
| Demonstration sensitive fields | 2 | fields | Username/password in Listing 2 | Visually readable | p. 20 |

The timeline dates are contextual labels, not results. Appendix numerical examples—port 9222, 500 tasks/400 pods, 1,000 IPs/50 k calls per minute, and ten agents/10,000 visits per hour—were inspected and represented with their scenario status in §11. They are deliberately excluded from the results table to prevent illustrative workloads from acquiring experimental authority. No approximate visual measurements from graph positions were needed.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Analysis | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Agent exposure extends beyond its LLM | Web driver, environment, dependencies, sensitive sessions | X2, T2 | pp. 2, 9–10 | Explicit architecture claim; no comparative rate |
| Untrusted pages can redirect tasks | Prompt-flow account, template, malicious payload, setup code | X5, V2–V3, ALG2 | pp. 18–20 | Concrete author-reported PoC; no supplied run logs |
| Configured domain boundary can fail | Faulty network-location parsing and crafted URL | X4, ALG1, V1 | pp. 16–17 | Directly inspectable mechanism |
| Domain issue is version-specific and remediated | 0.1.44 affected; 0.1.45 fixed statement | X4, T3 | pp. 16–18 | Historical author report; no live check |
| Placeholder privacy is not sufficient action authorization | Local replacement plus redirected action path | X2/X5 | pp. 7–8, 18–20 | Mechanistic interpretation grounded in descriptions |
| Browser Use was selected for relevance and openness | Task-success table and case-selection prose | X1, T1 | pp. 4, 15 | Capability is not security |
| Defenses should operate at multiple boundaries | Six initial-access and six recovery categories | X3 | pp. 11–14 | Synthesis rather than new evaluation |
| Cited detectors/isolation can reduce benchmark attacks | Approximately 25%→8%; cited 0% | X3 | pp. 12–13 | Conditions incompletely reproduced; secondhand evidence |
| Risk propagates across layers | Narrative L2/L7→L1→L3→L4 and onward | X2, T2, A1 | pp. 10, 21–29 | General scenarios exceed demonstrated case |
| Standalone comparison remains unmeasured | No matched baseline or comparative security experiment | Inventory/X1–X5 | pp. 3–20 | Analyst negative finding, HIGH confidence in supplied scope |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a chatbot that can only write suggestions. Now connect it to a browser that can click buttons, fill forms, and use your accounts. The same misunderstanding can have a much bigger consequence because the system can do things for you. It also has more parts that can fail: the browser, password handling, website reading, destination checks, and activity logs.

This paper shows two ways that can happen in Browser Use. In one, a destination check reads the wrong part of a specially written URL and thinks an unapproved destination is allowed. In another, a webpage contains fake instructions that try to replace the user's real task. The agent may then use its own tools and secret-handling machinery to help the attacker. Hiding a password from the model does not automatically stop the surrounding program from putting that password into the wrong action later.

The authors recommend several layers of protection: keep untrusted page text from controlling trusted planning, check actions against rules, restrict secret movement, watch for unusual behavior, and reset or restrict an agent when something goes wrong. But this paper does not measure a general percentage by which browser agents are less secure than ordinary chatbots. It explains the extra pathways to harm and demonstrates particular weaknesses in one implementation; it reports that the URL weakness was fixed in a later package version.

## Completeness Audit

The inventory was checked against the narrative, tables, code discussion, numerical ledger, and uncertainty record. 'Represented' means the substantive function and findings are conveyed; it does not mean every example or reference is reproduced verbatim.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0: title/abstract/footnotes | Yes, text and image | Yes | Represented in compressed form | Original title; author metadata below; equal contribution noted |
| S1 and RQ1–RQ4 | Yes | Yes | Fully represented | §§1, 4–6, 14 |
| S2.1 agent definition | Yes | Yes | Fully represented | §§1, 3 |
| S2.2 benchmark evolution | Yes | Yes | Represented in compressed form | §§7, 10; fixed trajectories versus realism |
| S2.3 selection/results | Yes | Yes | Fully represented | T1 and numerical table |
| S3.1 component definitions | Yes | Yes | Fully represented | §§3, 7, 12 |
| S3.1 introduction/perception | Yes | Yes | Represented in compressed form | DOM/vision and proprietary-access qualification |
| S3.1 reasoning/planning | Yes | Yes | Represented in compressed form | Combined iterations and model-size caveats |
| S3.1 privacy/anonymization | Yes | Yes | Fully represented | Local mapping, placeholders, restoration |
| S3.1 prompt construction | Yes | Yes | Represented in compressed form | Roles, context, tools, structured outputs |
| S3.1 model limitations/feedback | Yes | Yes | Fully represented | Robustness uncertainty and execution loop |
| S3.2.1 prior threat modeling | Yes | Yes | Represented in compressed form | Authors' positioning, not external validation |
| S3.2.2 seven-layer framework | Yes | Yes | Fully represented | T2 and cross-layer narrative |
| S4.1 overview | Yes | Yes | Fully represented | Initial access/post-exploitation and scope |
| §4.2.1 sanitization | Yes | Yes | Represented in compressed form | Delimit/filter/sandwich; insufficient alone |
| §4.2.2 paraphrasing | Yes | Yes | Represented in compressed form | Rewriting disrupts trigger patterns |
| §4.2.3 detection | Yes | Yes | Fully represented | Detector role and approximate rates |
| §4.2.4 prompting/fine-tuning | Yes | Yes | Represented in compressed form | Instruction/data distinction; bypass caveat |
| §4.2.5 planner/executor | Yes | Yes | Fully represented | Trust separation and cited 0% |
| §4.2.6 formal analyzers | Yes | Yes | Fully represented | Pre-execution policy checking |
| §4.3.1 session reset | Yes | Yes | Represented in compressed form | Clear context to limit persistence |
| §4.3.2 information flow | Yes | Yes | Fully represented | Sources/sinks and authorization |
| §4.3.3 memory inspection | Yes | Yes | Represented in compressed form | Memory poisoning; inspection mechanisms below |
| §4.3.4 audit/throttling | Yes | Yes | Fully represented | Monitoring and limiting actions |
| §4.3.5 safe mode | Yes | Yes | Fully represented | Restricted/read-only recovery |
| §4.3.6 red team/patching | Yes | Yes | Fully represented | Regression cycle |
| S4.4 trust isolation | Yes | Yes | Fully represented | §§12, 15, 22 |
| S5.1 selection/disclosure | Yes | Yes | Fully represented | White-box choice and CVE |
| S5.2 implementation risks | Yes | Yes | Fully represented | LangChain/Chromium, prompts, credentials |
| S5.3/T3 index | Yes | Yes | Fully represented | Exact scores and markers |
| S5.3.1/X4 | Yes | Yes | Fully represented | Version, code, configuration, failure, fix |
| S5.3.2/X5 | Yes | Yes | Fully represented | Task, model, attack flow, evidence limitations |
| S6 conclusion | Yes | Yes | Fully represented | Layered prevention/detection/response |
| F1 timeline | Yes, visually | Yes | Represented in compressed form | Small callout wording compressed |
| F2 architecture | Yes, visually | Yes | Fully represented | Components and arrow directions |
| T1–T3 | Yes, visually and text | Yes | Fully represented | Exact key values preserved |
| T4 foundation threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T5 data threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T6 framework threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T7 infrastructure threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T8 observability threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T9 duplicate table | Yes, visually and text | Yes | Inspected; repetition deliberately compressed | Caption mismatch explicitly reported |
| T10 security threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| T11 ecosystem threats | Yes, visually and text | Yes | Represented in compressed form | All rows and severities preserved |
| ALG1/Listing 1 and V1 | Yes, visually and text | Yes | Fully represented | Logic rather than full code reproduction |
| ALG2/Listing 2 | Yes, visually and text | Yes | Fully represented | Setup and undefined variable caveat |
| V2 prompt template | Yes, visually and text | Yes | Fully represented | Order and role markers discussed |
| V3 malicious payload | Yes, visually and text | Yes | Represented in compressed form | Attack function preserved; not executed |
| X1–X5 | Yes | Yes | Fully represented | Distinct analysis register |
| A1 severity methodology | Yes | Yes | Fully represented | Likelihood/impact, no formula |
| Major contributions | Yes | Yes | Fully represented | Novelty separated from verification |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst limitations |
| Hypotheses/equations/theorems | Checked | Not applicable | None found | No invented formal objects |
| Acknowledgements/references | Yes | Yes | Inspected; secondary content compressed | Metadata and citation anomalies retained |
| Separate supplements/logs/repository | Not supplied | Boundary disclosed | Missing from supplied material | Not reviewed |

Additional compressed subsection detail: automatic paraphrasing rewrites incoming text to disrupt malicious formatting; robust prompting/fine-tuning teaches instruction/data separation but may not generalize. Memory inspection is described through perplexity-based scanning for unusually predictable text and a second LLM checking memory for injected instructions or sensitive content. These are author-described defense ideas, not experimentally validated detectors in this paper. Information-flow control includes the example of preventing confidential document content from leaking through an external message/link-preview path. Traditional application-security review, penetration testing, and monitoring are recommended for external tools but explicitly outside the mitigation section's detailed scope. [pp. 11–14]

Document metadata: authors are Mykyta Mudryi, Markiyan Chaklosh, and Grzegorz Marcin Wójcik; the first two are marked equal contributors. Affiliations are ARIMLABS.AI, Polish-Japanese Academy of Information Technology, Maria Curie-Sklodowska University in Lublin, and University of the National Education Commission in Kraków. The supplied version is arXiv:2505.13076v1 [cs.CR], dated May 19, 2025. No journal or conference venue is specified for this paper. No keyword list is visible. Personal acknowledgements and contact details have been compressed because they do not change the scientific argument.

### Missing or inaccessible material

The linked proof-of-concept repository and its Default Issue, recorded conversations, actual network-request traces, advisory contents, patched implementation, cited benchmark datasets, and referenced publications are not supplied as independently inspectable artifacts. No formal supplemental package is explicitly identified in the paper. References to these resources do not establish that their contents were reviewed.

### Uncertain interpretations

Exact runtime prompt ordering is inconsistent between prose, numbered structure, and template. The HumanMessage/SystemMessage description differs. Reference [13]/[23] metadata overlap cannot be resolved internally. The absent §5.4.2 cross-reference, repeated Figure 1, and duplicated/miscaptioned Table 9 remain unrepaired source inconsistencies. Actual trial-level credential-exfiltration behavior, success frequency, and full CVSS scoring conditions are not ascertainable. The small timeline callouts were interpreted together with surrounding text rather than transcribed in full.

### Deliberately compressed material

Repeated motivation and conclusions, decorative headers/logos and lightbulb callouts, personal acknowledgements, full bibliographic entries, full attack-payload wording, and lengthy appendix examples are compressed. All appendix threat names and severity labels are retained. Scenario numbers are identified as illustrations rather than results. The duplicate Table 9 is recorded without repeating its three rows again.

### Potential omissions

No known substantive inventory category is wholly unrepresented. However, this report deliberately does not preserve every sentence, code token, bibliographic detail, or appendix example verbatim. Its coverage is comprehensive against the supplied inventory, not a claim of independent reproduction, external verification, or lossless replacement of the paper.
