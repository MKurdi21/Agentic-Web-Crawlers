# Audited Gaps and Research Directions for Agentic Web Systems

## Scope, claim discipline, and audit method

This document is a gap analysis of the **48 papers represented in `Summaries/`**, not a systematic review of every paper on web agents, crawling, extraction, or agent security. “The collection does not evaluate X” therefore means only that X is absent or inadequately tested in this closed evidence base. A field-wide absence or first-of-its-kind claim would require a separate literature search and is intentionally not made here.

The audit applies four rules:

1. A gap is residual: it begins with what the collection has already answered, then identifies what remains untested.
2. A headline number is kept with its experimental scope. Results from self-hosted sites, synthetic attacks, one model family, or a short time window are not generalized to the open web.
3. Capability, safety, and governance are distinct. Detecting a crawler is not consent enforcement; blocking an injected instruction is not evidence verification; task completion is not authorization.
4. Proposed novelty is collection-relative. Each proposal should be described as a new combination, extension, or evaluation target relative to these 48 papers unless a broader review substantiates a field-wide novelty claim.

### Coverage of the 48-paper evidence base

The following map makes the audit boundary explicit and prevents papers from disappearing merely because they do not anchor a standalone gap:

- Reasoning and tool foundations: **ReAct, Toolformer, and Gorilla**.
- Browser navigation and controlled interaction: **AutoWebGLM, Mind2Web, SeeAct, BrowserGym, WebArena, VisualWebArena, WebShop, WorkArena, WorkArena++, AndroidWorld, WebVoyager, and WebLINX**.
- Web research and long-horizon information seeking: **WebGPT, WebDancer, WebSailor, BrowseComp, BEARCUBS, Mind2Web 2, and MMInA**.
- Traversal, crawling, extraction, and web testing: **WebWalker, Go-Browse, LASER, AutoScraper, Webscraper, EvoCrawl, YuraScanner, and AWE**.
- Attacks, defenses, policy, and ecosystem measurement: **BackdoorAgent, SkillTrojan, Toward Secure LLM Agents, Identifying AI Web Scrapers Using Canary Tokens, WARD, When AI Meets the Web, Unsafe LLM-Based Search, WASP, Overcoming the Retrieval Barrier, ToolHijacker, SafeArena, ST-WebAgentBench, FORGE, Not What You’ve Signed Up For, SearchGEO, ACE, Formalizing and Benchmarking Prompt Injection, and RENNERVATE**.

Some papers span clusters. The map is organizational, not a claim that (for example) Go-Browse is only a crawler or that ACE is only a defense paper.

## Gap 1: Goal-directed crawling lacks a common, safety-aware coverage standard

### What this collection establishes

The earlier claim that LLM-guided crawling is simply “underdeveloped” is too coarse. Four papers already answer important parts of the problem:

- **Go-Browse** performs structured graph exploration to generate WebArena training data. It produced 3,422 unique tasks; its 7B model reached 17.9% overall WebArena success and 5.33% on Online-Mind2Web, versus 4.00% for NNetNav-7B. Prefixed sampling helped at deeper nodes, and feasibility filtering used only 13% of collection steps while preserving the same amount of positive data.
- **WebWalker** directly benchmarks traversal from a supplied root URL. GPT-4o WebWalker reached 37.50% overall accuracy; the strongest search-enhanced system reached 40.73%, while the best hard multi-source category result was only 16.67%. Performance fell with depth and multi-source requirements.
- **YuraScanner** generated 2,361 tasks on ten applications, of which 77.0% described valid functionality and 61.3% reached it fully or partially. Its task-driven policy found an attack surface complementary to Black Widow and BFS: only 18.3% of forms and 16.9% of URLs were shared on average, and it found 12 of 13 reported unique zero-day vulnerabilities. This is strong evidence for semantic exploration, but also evidence that it does not dominate conventional crawling.
- **EvoCrawl** uses evolutionary state exploration and dependency tracking rather than an LLM frontier policy. It reported an average 59% code-coverage increase over BlackWidow and found eight zero-day XSS/IDOR vulnerabilities, establishing a serious non-LLM baseline for stateful web-application exploration.

**AWE** further shows that specialized, memory-using web testing can be effective after discovery: 20/23 XBOW challenges (87%) versus 13/23 (57%) for MAPTA, although MAPTA was better on SSTI and command injection. **BrowserGym** supplies a reusable interaction substrate, while **WebArena**, **VisualWebArena**, **Mind2Web**, **SeeAct**, and **AutoWebGLM** establish navigation tasks and action representations. None, however, provides a shared crawl-frontier ground truth spanning URLs, rendered states, authenticated states, semantic goals, and prohibited boundaries.

### Residual gap and scope caveat

Within this collection, no benchmark compares semantic, graph, evolutionary, and task-generation policies on the **same stateful sites, budgets, and safety rules**. URL count is not state coverage; task success is not frontier quality; code coverage is not goal relevance. The evidence is strongest for self-hosted applications and supplied roots, not arbitrary public-web crawling.

### Actionable research design

Build a versioned suite of instrumented sites with a known state graph containing static URLs, client-side routes, forms, role-dependent views, prerequisite chains, duplicate/alias states, traps, rate limits, and explicit allowed/forbidden regions. Publish three goal families: exhaustive inventory, goal-relevant discovery, and vulnerability-relevant state discovery. Require every crawler to emit a typed frontier decision log: state signature, candidate edge, predicted value, risk, and reason for expansion or pruning.

Baselines should include BFS/DFS, randomized BFS, sitemap/robots-guided traversal, a conventional state-aware crawler such as Black Widow, EvoCrawl-style evolutionary search, Go-Browse-style graph exploration, YuraScanner-style task generation, WebWalker-style explorer/critic, and an oracle upper bound. Hold browser engine, credentials, seed roots, request/action budget, concurrency, and reset state constant.

Primary metrics should include reachable-state recall; URL, DOM-state, form, transition, and server-side code coverage; goal-relevant precision/recall; unique prerequisite chains recovered; vulnerability reachability; area under the coverage–action curve; duplicate-state rate; invalid-action rate; requests, tokens, wall time, and cost; server load; and policy violations. Report complementarity (unique discoveries and overlap), not just who found more.

Threat model: pages may contain loops, crawl traps, prompt injections, attacker-selected links, expensive actions, and out-of-scope origins. The crawler has only declared credentials and cannot bypass access controls. Measure unsafe frontier expansion, attempted privilege crossing, secret transmission, and rate-limit or policy breaches separately from coverage.

Likely validity risks include incomplete state ground truth, unstable browser fingerprints, privileged instrumentation that favors white-box methods, artificial traps, stochastic model/API drift, and treating equivalent rendered states as distinct. Validate state signatures manually on a stratified sample and report results both with and without instrumentation-derived ground truth.

### Research questions

- When do semantic policies add states that conventional and evolutionary crawlers miss, and when do they merely spend more?
- Can uncertainty-calibrated frontier selection improve goal recall without reducing broad coverage?
- What coverage is achievable under origin, role, rate, and side-effect constraints?
- Do policies trained on self-hosted sites transfer to unseen live sites without violating boundaries?

## Gap 2: Extraction systems lack enforceable governance and lifecycle evaluation

### What this collection establishes

**AutoScraper** and **Webscraper** partly answer scraper generation and repeated extraction. AutoScraper with GPT-4-Turbo reached 88.69 F1 on SWDE, above its listed supervised systems, and its measured break-even point versus direct LLM extraction averaged 19.5 pages. Yet direct extraction beat AutoScraper for seven of eight tested models; XPath fragility, multi-valued fields, and within-site layout changes remained. The supervised comparison was unequal, and the summary notes inconsistent source counts and no confidence intervals.

Webscraper’s prompt-plus-tool system beat its prompt-only and baseline variants on six news sites, and scored 0.242 on Momo and 0.422 on Amazon versus baseline scores of 0 and 0.027. Its seven-day check on only three sites showed less than 5% change, but this is not evidence of long-term maintenance. It explicitly excludes access-control bypass and notes copyright, load, and misuse concerns.

**Canary Tokens** provides rare empirical governance evidence: tokens mapped chatbot answers to first-party, generic-browser, and third-party search crawlers; cached material could persist after sites went offline; and taking sites offline or adding `robots.txt` did not uniformly remove previously acquired content. This supports attribution and observability, not a reliable method for expressing consent, proving compliance, or distinguishing legitimate purposes. **When AI Meets the Web** similarly measures real deployments and third-party content flows, while **Unsafe LLM-Based Search** examines hazards in search systems. Neither supplies a general extraction authorization protocol.

### Residual gap and scope caveat

The collection does not connect extraction accuracy to a machine-enforceable lifecycle: discover policy, authorize purpose and fields, minimize collection, limit rate and retention, attach provenance, handle revocation, and revalidate generated wrappers after drift. Robots.txt is neither a complete consent language nor a legal determination. A technical benchmark must not label one policy syntax “lawful” across jurisdictions.

### Actionable research design

Create an extraction-governance benchmark in which each site exposes versioned, machine-readable policy fixtures covering agent identity, purpose, fields, rate, temporal window, retention, redistribution, attribution, and revocation. Include conflicts among site policy, task request, organizational policy, and user role. Seed public, personal, sensitive, and prohibited fields plus canaries whose appearance in requests, logs, stored datasets, or outputs is traceable.

An evaluated system should compile an extraction plan into a deterministic or inspectable wrapper where possible, bind it to a policy version and data schema, enforce request and retention budgets at runtime, and stop or seek approval when policy changes. Test clean extraction, ambiguous policies, missing policies, deceptive in-page statements, post-consent revocation, DOM drift, and cached copies.

Baselines: direct extraction; AutoScraper; Webscraper prompt-only and prompt-plus-tool; conventional XPath/CSS wrappers; robots-only compliance; prompt-only “responsible scraper”; a policy engine without semantic interpretation; and an oracle policy parser. Canary-token monitoring should be evaluated as detection, not conflated with prevention.

Metrics: field-level precision/recall/F1; wrapper executability and cross-page generalization; time to breakage and repair after drift; compliant coverage; forbidden-field and canary leakage; requests per valid record; peak request rate; bytes and server load; policy-parsing accuracy; appropriate abstention; approval burden; retention/deletion conformance; provenance completeness; reproducibility; and audit-log verifiability.

Threat model: a requester may ask for prohibited data; a page may contain sensitive fields or malicious policy text; a scraper may misidentify itself, exceed rate limits, retain revoked data, or extract via a cache after the origin changes. Defenses should assume that prompt-only compliance can be bypassed and enforce policy outside the model.

Validity risks include encoding contested norms as ground truth, synthetic policies unlike operator practice, canaries changing agent behavior, inability to verify downstream deletion, and conflating technical compliance with legal or ethical legitimacy. Report results by policy dimension and stakeholder assumption rather than a single “responsibility” score.

## Gap 3: Adversarial web evaluation remains fragmented across instruction, retrieval, evidence, and action attacks

### What this collection establishes

The draft correctly identified a disconnect, but “mainstream benchmarks rarely include adversarial pages” needs qualification. The collection contains several substantial adversarial suites:

- **WASP** pairs benign VisualWebArena-style tasks with feasible security violations. Intermediate compromise ranged roughly from 17% to 86%, but end-to-end attacker-goal success was 0% to about 17%, showing why merely judging whether an agent appears distracted overstates realized harm.
- **WARD** constructs paired benign/malicious HTML and screenshot observations at scale (90,802 benign and 86,783 malicious samples) and trains a multimodal guard. This is broad detection evidence, not proof that guarded agents remain safe over full trajectories or adaptive distribution shift.
- **Formalizing and Benchmarking Prompt Injection** compares five attacks and ten defenses with target utility, attack-success value, false positives, and false negatives; it shows strong dependence on injected task and defense trade-offs.
- **RENNERVATE** reports fine-grained detection above 97.88% across evaluated backbones with low reported false-positive/false-negative rates and sanitization experiments, but its FIPI distribution and NLP subtasks do not substitute for open-ended browser trajectories.
- **Not What You’ve Signed Up For** demonstrates real application attack paths including persuasion, search-query exfiltration, malicious links, and persistent memory, but provides no attack-rate, replication, or statistical estimates.
- **Overcoming the Retrieval Barrier** shows optimized retrieval triggers: at length 10, seven datasets reached 100% Recall@5, FEVER 99.8%, but MS MARCO 74.0% and ArguAna 77.5%; cross-model and position transfer varied sharply.
- **ToolHijacker** reports 74.3%–100% attack success in its main table and malicious-document retrieval above 96% on ToolBench despite 9,650 benign documents. This is a tool-document retrieval/selection setting, not a browser-action result.
- **SearchGEO** and **FORGE** show non-instructional evidence and recommendation manipulation. FORGE finds that one polluted page can suffice, retrieval rank matters, models may invent social proof, and simple skepticism/corroboration defenses are incomplete.
- **BackdoorAgent** and **SkillTrojan** extend the threat beyond page text. BackdoorAgent examples combine high attack success with nearly unchanged or improved task accuracy; SkillTrojan reached 97.2% attack success with 89.3% clean accuracy on one model and produced deterministic external side effects, while simple encoding changes reduced a Base64 heuristic’s flag rate from 78% to 21%.

**SafeArena**, **ST-WebAgentBench**, **Unsafe LLM-Based Search**, **ACE**, **When AI Meets the Web**, and the **Toward Secure LLM Agents** survey broaden misuse, policy, architecture, deployment, and lifecycle coverage. The residual problem is integration, not lack of any adversarial evaluation.

### Residual gap and threat model

No suite in the collection composes all four layers on matched tasks: (1) malicious or deceptive page content, (2) retrieval/ranking manipulation, (3) compromised tools, skills, or memory, and (4) consequential browser actions. Attacker knowledge and capabilities vary between papers, making raw attack-success rates incomparable.

Define explicit tiers: content-only attacker; content-plus-search-rank attacker; registered-tool/skill supplier; compromised memory producer; and adaptive attacker who observes defenses but not secrets. Separate integrity, confidentiality, availability, financial, reputational, and physical consequences. Require a realizable end state for “attack success”; also report intermediate compromise and near misses.

### Actionable research design

Create clean/adversarial twins of the same tasks across WebArena/VisualWebArena, WorkArena, research QA, and crawl/extraction scenarios. Factor attacks by channel (visible text, hidden HTML, image, review/comment, search snippet, retrieved document, tool description, memory, installed skill), goal, knowledge, persistence, and adaptivity. Include benign lookalikes such as legitimate page instructions, unfamiliar products, unusual forms, and genuine policy warnings to measure overblocking.

Baselines: unprotected ReAct and browser agents; instruction-hierarchy prompting; delimiter/spotlighting defenses; WARD-style guards; RENNERVATE-style detection/sanitization; retrieval filtering and provenance re-ranking; cross-document corroboration; action allowlists; ST-WebAgentBench-style policy checking; and ACE-style plan/data separation where its tool model applies. Run adaptive attacks against every defense and disclose whether defenses see the user goal, raw DOM, screenshot, proposed action, memory, and tool metadata.

Metrics: benign task success; intermediate compromise; end-to-end attack success; time/steps to compromise; goal-conditioned false-positive and false-negative rates; harmful state change; bytes/secrets exfiltrated; polluted-source influence; recommendation/answer shift; clean utility; latency and cost; user approval burden; persistence across episodes; detection before versus after an irreversible action; and recovery completeness.

Validity risks: templated attacks, attack-generator leakage into detectors, unrealistic attacker access, model-judge circularity, evaluator blind spots, and reporting only the strongest attack or weakest defense. Use held-out attack authors, adaptive red teams, rule/state-based end evaluators, confidence intervals across seeds and tasks, and preregistered aggregation.

## Gap 4: Privacy is demonstrated as an attack consequence but not measured as continuous information flow

### What this collection establishes

Privacy is not absent from the corpus. **WASP** includes concrete exfiltration goals whose success requires data to reach an attacker server. **Not What You’ve Signed Up For** demonstrates query- and URL-based exfiltration and multi-turn elicitation. **Overcoming the Retrieval Barrier** includes a code-execution scenario that attempts to exfiltrate SSH keys. **ToolHijacker**, **When AI Meets the Web**, and **ACE** cover tool-mediated leakage and cross-app information flow. ACE’s restricted planning language and static information-flow analysis handle explicit and implicit flows, including delayed loop leakage; it reported 100% security over 1,054 INJECAGENT cases while retaining up to 85.3% overall utility in that benchmark. This is a substantive partial answer, not merely a proposal.

However, ACE assumes a particular app/tool architecture and ahead-of-time abstract planning. Browser agents also leak through ordinary, non-adversarial operations: search queries, form autocomplete, URLs, referrers, screenshots, clipboard, downloads, logs, citations, analytics, and final answers. **WebLINX** supplies multi-turn dialogue histories and **WorkArena/WorkArena++** supply enterprise context, but their primary evaluations do not label secret flow.

### Residual gap and threat model

Within this collection there is no end-to-end privacy benchmark that assigns provenance and permitted sinks to every sensitive datum throughout a multi-site trajectory. The adversary may control a page, tool, third-party origin, analytics endpoint, or installed skill; the agent may also leak accidentally without an adversary. Secrets should vary by type, user, organization, purpose, and permitted destination.

### Actionable research design

Instrument a browser and tool runtime with typed canaries and dynamic taint labels. Seed credentials, personal facts, enterprise records, conversation history, location, and task-only secrets. Define allowed transformations and sinks—for example, an address may be submitted to an approved checkout origin but not placed in a search query or third-party URL. Log model-visible context as well as network and state side effects.

Compare an unconstrained ReAct agent, prompt-only privacy instructions, context minimization, origin-based allowlists, field-level redaction, retrieval isolation, capability-scoped secrets, dynamic taint tracking, and ACE-inspired static planning. Include tasks where some secret use is necessary, so blanket refusal is not rewarded.

Metrics: secret recall by unauthorized sink; weighted leakage severity; number of origins exposed; query/URL/form/tool/final-answer leakage rates; minimum secret subset used; task success under privacy constraints; false blocks; approvals; detection latency; residual copies after revocation; and information-flow coverage. Report exact and semantic leakage separately because paraphrases can disclose meaning without matching a canary.

Validity risks include canary memorability, incomplete browser/network instrumentation, ambiguous permitted use, model providers retaining prompts outside the test harness, and equating absence of observed leakage with confidentiality. The benchmark should state which channels are observable and treat uninstrumented channels as unknown.

## Gap 5: Live-web realism and reproducibility are not yet reconciled by versioned evidence

### What this collection establishes

The corpus already spans controlled and live designs. **WebArena**, **VisualWebArena**, **WebShop**, **WorkArena**, **WorkArena++**, and **AndroidWorld** emphasize resettable state and automatic outcome checks. AndroidWorld adds parameterized tasks and system-state rewards. **BrowserGym/AgentLab/AgentXRay** unify benchmarks and capture execution artifacts, though the paper still reports reproducibility limits.

At the other end, **WebVoyager**, **BEARCUBS**, **BrowseComp**, **Mind2Web 2**, and parts of the deep-research evaluations use real or live websites. WebVoyager’s error analysis attributed 44.4% of failures to getting stuck, 24.8% to visual grounding, 21.8% to hallucination, and 9.0% to prompt misalignment. BEARCUBS found 84.7% human versus 65.8% for its strongest agent and reported short-run baseline stability, but its source-quality counts contain a small internal inconsistency. BrowseComp audited 118 zero-pass items and removed 21 defective labels, illustrating that even carefully built research questions decay or contain defects. Mind2Web 2 identifies 57 explicitly time-varying tasks and reports 23% hallucination even for its best system. **Webscraper** tests only a seven-day interval on three sites, insufficient for long-term drift claims.

### Residual gap and scope caveat

No paper in the collection runs matched tasks across live, replayed, archived, and self-hosted versions long enough to quantify which conclusions survive content, UI, ranking, account, and model drift. A screenshot plus DOM is not necessarily executable replay; a self-hosted clone can preserve mechanics while losing contemporary search and adversarial conditions.

### Actionable research design

Build a hybrid benchmark with a canonical task identifier and four synchronized modes: live execution, network/browser replay, executable archived clone, and semantically equivalent self-hosted task. At each release, store timestamps, task and site versions, DOM/accessibility tree, screenshots, network records subject to permission, action trace, evaluator version, model/API version, search results, source snapshots or hashes, and final evidence bundle.

Use rolling cohorts: immutable historical tasks for longitudinal comparison, refreshed tasks for current realism, and bridge tasks run in both. Re-evaluate a fixed panel monthly and after known site/model changes. Baselines should include WebVoyager-style multimodal interaction, BrowserGym generic agents, text/DOM agents, and human operators.

Metrics: task and answer drift; action-path edit distance; replay fidelity; state-reward agreement; source availability; evaluator disagreement; ranking drift; success variance over time; maintenance hours and legal exclusions; live-to-clone transfer; and security-event rate. Report a benchmark “half-life”: time until a prespecified fraction of tasks or labels require repair.

Validity risks include archive permissions, personal data capture, third-party resources that cannot be replayed, authentication expiry, anti-bot differences, selective survival of easy sites, and model API changes. Reproducibility artifacts should minimize captured personal data and distinguish unavailable evidence from agent failure.

## Gap 6: Long-horizon, multi-site work remains brittle despite substantial new benchmarks

### What this collection establishes

The draft understated existing coverage. **WebGPT** established browser-assisted, citation-bearing QA with human feedback and warned about cherry-picking, citation-based authority, and noisy human evaluation. **WebDancer** and **WebSailor** train agents on synthetic and filtered research trajectories; their results show gains from trajectory quality and reinforcement learning but leave open contamination, instability, and transfer questions. **BrowseComp** reaches deliberately difficult, obscure questions: GPT-4o with browsing scored 1.9%, o1 without browsing 9.9%, and Deep Research 51.5%; best-of-64 rose to roughly 78%, at high compute, while calibration errors were 65%–91%.

**BEARCUBS** tests computer-using research with primary/secondary/ungrounded sources. **Mind2Web 2** evaluates compositional agentic search and structured evidence nodes. **MMInA** is especially direct evidence for horizon collapse: GPT-4V achieved 42.91% success on single-hop tasks, 3.03% at 2–4 hops, and 0% at 5+; humans achieved 99.02%, 95.34%, and 88.12%, respectively. **WebWalker** similarly reports sharp depth and multi-source degradation. **WorkArena++** adds compositional enterprise tasks and identifies insufficient exploration, thought–action inconsistency, hallucinated controls/consequences, and repeated useless actions.

### Residual gap

The collection measures difficult endpoints, but less consistently measures state maintenance, evidence accumulation, contradiction resolution, stopping, recovery, and delegation as separable competencies. High parallel-sampling scores can hide poor single-trajectory reliability and large cost. “Long horizon” also conflates many clicks on one site with evidence-bearing work across independent sites.

### Actionable research design

Construct tasks from explicit evidence graphs: required facts, alternative valid paths, source identities and dependencies, contradictions, stale facts, distractors, and sufficient stopping sets. Include three horizon axes independently: interaction depth, number of origins, and number of dependent claims. Add controlled perturbations mid-run: a source disappears, a value changes, a login expires, or a prior observation is shown to be wrong.

Baselines: ReAct; WebGPT-style browsing; WebWalker explorer/critic; WebDancer/WebSailor-style trained search agents; generic BrowserGym agents; single-pass RAG; best-of-N/majority aggregation; and humans under matched time budgets. Include a graph oracle and a retrieval oracle to separate evidence discovery from synthesis.

Metrics: final correctness; claim-level precision/recall; evidence-node and source coverage; citation entailment and source identity/diversity; contradiction detection and resolution; stale-evidence use; belief revision after perturbation; stopping regret; calibration/selective accuracy; success per request/token/dollar/minute; pass@1 and pass@N; horizon-conditioned success; and recovery without restart.

Validity risks: synthetic evidence graphs may make the web too tidy; source independence is difficult to establish; open-web facts change; LLM judges may reward verbosity; and leaked benchmark questions can inflate results. Combine state/rule checks with blinded human evidence audits, version every source, and report per-task distributions rather than only macro averages.

## Gap 7: Trajectory quality is partially observed but lacks a validated, causal measurement standard

### What this collection establishes

It is inaccurate to say evaluation only rewards final success. **Mind2Web** evaluates element and action prediction; **WebLINX** evaluates action components and multi-turn behavior; **BrowserGym** records full episodes; **WebShop** reports reward components and trajectories; **WebVoyager** and **Mind2Web 2** use automatic judges plus human validation; **WASP** distinguishes intermediate compromise from realized end-state harm; **ST-WebAgentBench** evaluates policy adherence; and **ACE** reports step and overall accuracy. **ReAct** manually classified failures and found loops, reasoning errors, and unhelpful retrieval. **LASER** shows performance degrading with longer paths and uses a backup strategy. **WorkArena++** explicitly catalogs repeated actions and thought–action inconsistency.

These are valuable but heterogeneous. Action efficiency may punish necessary verification; imitation distance may punish a valid alternative path; a safe refusal may look like failure; and model-based trajectory judges may miss hidden side effects. ACE’s result that lower step accuracy can coexist with higher overall relational-task accuracy is a concrete warning against treating reference-trace match as universal quality.

### Residual gap and actionable design

Develop a trajectory schema that separates observation, belief, evidence, plan, action proposal, authorization decision, executed side effect, and recovery. Annotate a stratified set with multiple expert raters and causal counterfactuals: remove or replace one action and test whether success, safety, or evidence quality changes. This distinguishes unnecessary steps from harmless alternatives.

Baselines should include shortest valid/reference traces, successful human traces, ReAct, a memoryless actor, a planner–executor, and policy-gated agents. Evaluate rule-based detectors, process-reward models, and blinded human auditors against held-out sites and agent families.

Metrics: valid-action and grounding rate; progress per action; duplicate/loop rate; causal action necessity; excess irreversible actions; unsafe intermediate states; exposure surface; recoverability and rollback success; belief/evidence consistency; citation-to-observation traceability; policy margin; hidden side effects; judge inter-rater reliability; judge calibration; and correlation with downstream task/safety outcomes. Keep final success as a separate axis rather than folding all properties into an opaque scalar.

Validity risks include hindsight bias, multiple valid paths, unobservable internal beliefs, leaked chain-of-thought, strategic judge gaming, and disagreement about optimality. Do not require private reasoning traces; use concise inspectable state/evidence records and executed actions. Publish sensitivity analyses for metric weights.

## Gap 8: Enterprise benchmarks test workflows and policy, but not a full authorization lifecycle

### What this collection establishes

**WorkArena** supplies resettable ServiceNow tasks across lists, forms, knowledge, catalogs, dashboards, and menus. **WorkArena++** adds 235 L3 instances with compositional planning, reasoning, memorization, and infeasible tasks. **ST-WebAgentBench** adds policy-sensitive evaluation. **BrowserGym** provides the environment layer. **ACE** demonstrates plan separation and information-flow checks for LLM-integrated apps.

This is meaningful coverage, so the residual gap is not “enterprise agents need auditability” in the abstract. Rather, the collection does not jointly evaluate identity, delegated authority, least privilege, segregation of duties, approval, policy versioning, audit evidence, revocation, and incident reconstruction across enterprise browser workflows. Role simulation in WebArena or a fixed benchmark account is not the same as organizational authorization.

### Actionable research design and threat model

Extend a WorkArena-like environment with users, groups, service identities, scoped credentials, temporal roles, delegated tasks, conflicting duties, approval chains, break-glass access, and revocation during execution. Policies should be both machine-enforceable and accompanied by natural-language rationales; create ambiguous cases where the correct behavior is to ask a targeted question.

Threats include an overprivileged agent, malicious page/tool content, confused-deputy actions, stale authorization, approval spoofing, cross-tenant leakage, self-approval, and audit-log tampering. The model must never possess ambient credentials beyond the capability needed for the current approved action.

Baselines: role-based access control; attribute/policy-based control; prompt-only policy reminders; ST-WebAgentBench-style compliance checking; per-action human approval; risk-tiered approval; capability tokens; and ACE-style restricted planning. Include human employees under the same policies and task deadlines.

Metrics: task success; unauthorized attempt and executed-violation rates; least-privilege distance; privilege lifetime; approval precision/recall and burden; time to revoke; cross-tenant exposure; correct escalation; explanation faithfulness; audit completeness and tamper evidence; policy-version attribution; rollback/recovery; and productivity cost. Score infeasible tasks for correct abstention, not completion.

Validity risks include one vendor/domain, synthetic policies, unrealistic employee behavior, policy ambiguity, and benchmark shortcuts. Use multiple organizational templates, hidden policy tests, adversarial role changes, and separate evaluator access from agent access.

## Gap 9: Containment and provenance have promising components but are not compositional across the agent lifecycle

### What this collection establishes

The earlier “remain immature” claim obscured a strong result: **ACE** blocks its three new architecture-level attacks and all 1,054 INJECAGENT cases under its tested assumptions, with structural plan/data separation and static information-flow verification rather than prompt recognition alone. Its scope is nevertheless an LLM-integrated app system with a restricted planning language, not unrestricted browser/OS interaction.

**BackdoorAgent** shows triggers propagating through planning, memory, tools, and sequential environments while clean task accuracy can remain high. **SkillTrojan** shows that installed skills can reconstruct segmented encrypted payloads through ordinary-looking workflow steps and execute externally verified side effects. **ToolHijacker** attacks tool discovery; **Gorilla** shows that retrieval-aware training improves API selection and adaptation to changed documentation but does not authenticate tool intent; **Toolformer** studies self-supervised tool use rather than permission safety. The **Toward Secure LLM Agents** survey argues that defenses do not compose well across lifecycle stages.

### Residual gap and threat model

No evaluated system in this collection binds artifact provenance, declared permissions, runtime capabilities, memory lineage, data-flow labels, network egress, side-effect monitoring, revocation, and post-incident repair into one browser-agent lifecycle. Signing proves publisher/key provenance, not benign behavior. Static scanning cannot see all reconstructed payloads; runtime monitoring alone may act too late.

Assume malicious or compromised skill publishers, tool documents, memories, web pages, and dependency updates; stolen signing keys; colluding components; and payloads split across time. Exclude kernel compromise unless explicitly tested, and state whether the attacker can modify the model, orchestrator, browser, or OS.

### Actionable research design

Build an installable-skill and browser-tool testbed with signed manifests, reproducible package hashes, declared inputs/outputs/side effects, granular capabilities, isolated storage, origin-scoped network access, tainted memory, and revocation lists. Generate benign, vulnerable, overprivileged, backdoored, and colluding packages. Test installation, clean use, trigger, persistence, update, discovery, quarantine, credential rotation, memory repair, and replay of affected traces.

Baselines: signature only; static scanner; prompt/description scanner; sandbox only; allowlist; least-privilege capabilities; runtime syscall/network monitor; ACE-style information-flow verifier; and layered combinations. Include native useful skills so security is not won by disabling extension.

Metrics: verified external attack success; clean task utility; malicious install/select/execute rates; permission overbreadth and bypass; provenance coverage; detection latency; blocked benign side effects; cross-stage propagation; persistence after restart; egress volume; quarantine and revocation success; time to identify affected runs; and complete remediation. Test adaptive evasion and key compromise.

Validity risks include toy payloads, platform-specific APIs, known scanners, unrealistic signing trust, and incomplete monitoring. Keep exploit artifacts safe, report capability boundaries, and distinguish prevented execution from merely detected behavior.

## Gap 10: Evidence integrity needs source-identity and claim-lineage defenses, not citations alone

### What this collection establishes

**WebGPT** demonstrates that citations improve perceived and evaluated answers but explicitly warns about cherry-picking, authority effects, bias, and synthesis errors. **BEARCUBS** labels primary, secondary, and ungrounded sourcing and shows that correct answers can still rely on weaker evidence. **Mind2Web 2** uses structured evidence nodes and a high-performing verifier, but its judge audit is small and includes inconsistent-source cases. **BrowseComp** demonstrates label defects and extreme miscalibration. **SearchGEO** and **FORGE** show that attackers can manipulate generative search or recommendations without giving imperative instructions; FORGE reports that a single polluted page can be enough and that models invent unsupported social proof. **Overcoming the Retrieval Barrier** and **ToolHijacker** show how attacker documents enter evidence/tool contexts despite large benign corpora.

Thus “provide citations” and “retrieve multiple sources” are already partly answered and are insufficient. Several URLs can derive from the same press release, affiliate network, scraped page, or attacker. A true statement can be attached to an irrelevant citation; a credible source can be stale; and a valid page can be selectively quoted.

### Residual gap and threat model

The collection lacks an end-to-end claim ledger linking each answer claim to exact source spans, retrieval events, source ownership/derivation, timestamps, transformations, contradictions, and confidence. The attacker may create many apparently independent domains, poison ranking, clone reputable content, manipulate snippets, or update a page after retrieval.

### Actionable research design

Create an evidence-integrity benchmark with controlled source families and a hidden derivation graph. Vary factual correctness, relevance, authority, recency, independence, popularity, rank, and adversarial ownership independently. Include one polluted page, sybil corroboration, stale-but-credible sources, citation laundering, snippet/page mismatch, post-retrieval edits, and novel legitimate products that conflict with model priors.

Require agents to output a claim ledger: normalized claim, supporting and opposing spans, retrieval timestamp, content hash, source identity and dependency hypothesis, confidence, and unresolved uncertainty. Evaluate answers with and without access to the hidden graph.

Baselines: WebGPT-style citation generation; vanilla RAG/search; rank-based trust; domain allowlists; skepticism prompting; model-prior consensus; FORGE-style cross-document corroboration; source-cluster-aware corroboration; and an oracle derivation graph.

Metrics: claim correctness; citation entailment, completeness, and relevance; unsupported-claim rate; independent-evidence recall; sybil-adjusted corroboration; source-diversity after clustering; contradiction and staleness detection; polluted-page influence; recommendation rank shift; calibration; evidence freshness; and ledger replayability. Evaluate task utility so defenses do not reject genuinely new information.

Validity risks include subjective authority labels, hidden real-world ownership, model prior contamination, copyrighted snapshot constraints, and benchmark artifacts that reveal attacker pages. Use multiple domains and languages, independent fact checking, time-split attacks, and sensitivity to alternative source-independence assumptions.

## Gap 11: Evaluation reporting is too heterogeneous for reliable cross-paper conclusions

### What this collection establishes

The papers collectively contribute rich metrics—exact match, success, reward, element/action F1, code and state coverage, attack success, policy compliance, false positives/negatives, citation quality, cost, latency, and human preference. **BrowserGym** is an important standardization step, and controlled environments such as WebArena, WorkArena, AndroidWorld, and WebShop provide automatic state rewards. Yet the summaries expose recurrent reporting issues:

- AutoScraper has inconsistent page/domain counts, unequal supervised comparisons, and no significance tests.
- Webscraper reports 30-run confidence-interval motivation but lacks recoverable per-site values and formal test details for claimed significance.
- BEARCUBS has a small inconsistency in source-percentage reporting.
- BrowseComp found 21 defective items among 118 audited zero-pass questions.
- WorkArena++ notes an internal reporting inconsistency.
- WebWalker relies partly on an LLM judge and includes values visually approximated from figures.
- WebVoyager and Mind2Web 2 validate judges, but on bounded samples; model judges remain a source of correlated error.
- Security studies use incompatible attacker access, intermediate versus end-state success, and clean-utility definitions.

These do not invalidate the papers; they limit synthesis and show why a shared report should carry denominators, uncertainty, exclusions, and threat assumptions.

### Actionable research design

Define a minimum Web-Agent Evaluation Card and machine-readable result schema. Required fields should include task/site versions; reachable population and sampling; model, prompt, temperature, tools, and API date; observation/action modes; maximum steps/time/cost; resets and credentials; seeds and repeats; exclusions and failures; evaluator implementation/version; human/judge agreement; threat model; attack adaptivity; clean and adversarial utility; per-task raw outcomes; confidence intervals; and artifact availability.

Require three layers of outcome where relevant: final state/answer, trajectory/process, and external side effects. Report pass@1 separately from best-of-N, total compute for aggregation, and paired clean/adversarial deltas. For live tasks, distinguish agent failure, site failure, task invalidity, evaluator failure, and unavailable evidence.

Baselines should include a simple non-agentic/search baseline, a conventional automation baseline, a representative ReAct/generic agent, a strong contemporary agent, humans where feasible, and an oracle for the isolated capability being studied. Do not compare methods with different budgets without both budget-matched and unconstrained views.

Core statistical practice: publish task-level data; use paired bootstrap or an appropriate hierarchical model over tasks/sites/runs; include uncertainty and effect sizes; correct or disclose multiple comparisons; preregister primary metrics; and audit a stratified sample of wins, failures, refusals, and judge disagreements. A leaderboard should display a Pareto surface for task success, risk, cost, and reproducibility rather than a single composite rank.

Validity risks include checklist compliance without better science, excessive reporting burden, benchmark gaming, and false precision from correlated tasks. Keep a small mandatory core plus domain modules, and explicitly model clustering by site and task family.

## Prioritization framework

A research direction should be ranked on six dimensions, each scored 1–5 with evidence and uncertainty:

1. **Expected harm reduction:** severity and reversibility of failures addressed.
2. **Exposure:** how often deployed web agents plausibly encounter the condition.
3. **Evidence deficit:** how little the 48-paper collection answers the residual question, not how fashionable the topic is.
4. **Measurement readiness:** availability of safe environments, ground truth, and reliable evaluators.
5. **Transfer leverage:** usefulness across crawling, research, extraction, and enterprise action.
6. **Reproducibility/maintenance cost:** reverse-scored; high legal, operational, or refresh burden lowers near-term priority.

Do not collapse the scores mechanically. Apply two gates first: research must be conductible without material uncontrolled harm, and its central outcome must be externally observable. Then publish the dimension scores and a short rationale.

Using only the evidence in this collection, the recommended sequence is:

- **Priority A — common infrastructure:** evaluation/reporting schema (Gap 11), trajectory and side-effect instrumentation (Gap 7), and hybrid versioning (Gap 5). These make later claims comparable.
- **Priority B — high-consequence integration:** compositional adversarial evaluation (Gap 3), privacy flow (Gap 4), enterprise authorization (Gap 8), and lifecycle containment/provenance (Gap 9). Existing attacks show realized or externally verified consequences, while deployed defenses cover only subsets.
- **Priority C — capability with guardrails:** common crawl coverage (Gap 1), extraction governance (Gap 2), long-horizon evidence graphs (Gap 6), and evidence integrity (Gap 10). These should reuse Priority A/B instrumentation rather than create isolated leaderboards.

This ordering is not a claim that Priority C is less scientifically important. It reflects dependency: coverage and research gains are difficult to trust without reproducible traces, authorization, privacy, and adversarial accounting.

## Cross-gap research program: the Versioned, Accountable Web Agent Testbed

A justified cross-gap program would be a shared testbed rather than a single “unified score.” It should have four interoperable layers:

1. **Versioned environments:** instrumented crawl sites, research/evidence sites, extraction sites, and WorkArena-like enterprise sites, each with live/clone/replay identifiers.
2. **Typed execution substrate:** observations, candidate frontier edges, evidence spans, plans, capabilities, approvals, actions, state changes, network egress, and provenance events share one logged schema.
3. **Factorial scenario generator:** vary horizon, number of sites, authorization, sensitive data, source dependence, content attack, retrieval attack, tool/skill compromise, and site drift independently. Every adversarial task has a benign twin.
4. **Modular evaluation:** capability, evidence integrity, privacy, authorization, security, trajectory quality, cost, and reproducibility remain separate scorecards with Pareto reporting.

### First three studies

**Study 1: Safe semantic crawling.** Compare BFS, state-aware, evolutionary, Go-Browse-like, YuraScanner-like, and LLM frontier policies on the same instrumented sites. Cross coverage with origin/rate/role constraints and adversarial pages. This directly resolves Gap 1 while validating the logging and threat-model layers.

**Study 2: Authorized research-to-extraction.** Agents must find multi-site evidence, resolve conflicts, generate a reusable extractor, and deliver a provenance-bearing dataset under field, rate, retention, and privacy constraints. This connects Gaps 2, 4, 6, 8, and 10 without pretending they are one metric.

**Study 3: Persistent compromise and recovery.** Introduce matched page injections, polluted evidence, malicious tool descriptions, poisoned memory, and backdoored skills. Compare guards, sanitizers, provenance filters, capability sandboxes, information-flow controls, and layered defenses. Evaluate external effects, clean utility, revocation, memory repair, and affected-run discovery, addressing Gaps 3 and 9.

### Program-level hypotheses

- Agents with better nominal task success will not necessarily have better trajectory, privacy, or authorization outcomes.
- Structural controls will generalize better than prompt-only controls for enforceable boundaries, but may incur higher abstention or planning failures.
- Source-aware and provenance-aware agents will resist content pollution better than agents that merely increase retrieval count.
- Semantic crawling and conventional crawling will remain complementary; hybrid policies will dominate only when budgets and boundary constraints are explicit.
- Live-to-clone performance gaps will be systematic enough to estimate, but different for navigation, evidence, and security outcomes.

### Exit criteria

The program should be considered successful only if independent teams can reproduce a release; raw task-level results and evaluator disagreements are available; attack success is tied to externally observed outcomes; clean utility and false positives are reported; claims are stratified by site, horizon, model, and threat tier; and results remain interpretable after sites, models, or policies change. A single aggregate “WebAgent360” score would undermine these goals and is therefore not recommended.

## Audited novelty language for future papers

Appropriate claims based on this evidence base include:

- “We provide a matched comparison not present in the 48-paper collection reviewed here.”
- “We extend Go-Browse/YuraScanner/EvoCrawl-style exploration with common safety and coverage ground truth.”
- “We compose attack and defense layers that the reviewed papers evaluate separately.”
- “We introduce a collection-relative benchmark for continuous privacy flow / authorization lifecycle / source-dependency integrity.”

Claims to avoid without a broader review include “the first LLM crawler,” “no prior adversarial web-agent benchmark,” “the first safe agent architecture,” “prompt injection is unsolved by all defenses,” “citations solve evidence integrity,” and “no benchmark evaluates trajectories.” The collection itself contradicts each categorical formulation or supplies a substantial partial answer.
