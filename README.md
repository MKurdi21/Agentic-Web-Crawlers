# Agentic Web Agents, Crawling, Extraction, Evaluation, and Security

This repository is a curated local collection of 48 papers about AI systems that search, traverse, operate, or extract from the web, plus closely related work on tool use, mobile agents, web-application exploration, and agent security. It contains 24 core/root papers, 17 papers in `Security/`, and 7 adjacent papers in `Borderline/`. Every paper has a corresponding comprehensive Markdown summary in `Summaries/`.

The collection is best understood as four overlapping research families:

1. **Capability:** systems and training methods for reasoning, browsing, navigation, interaction, and multi-step information seeking.
2. **Evaluation:** benchmarks, environments, task validators, judge agents, and reproducibility infrastructure.
3. **Extraction and exploration:** reusable scraper generation, multimodal record extraction, task-directed crawling, and stateful web-application exploration.
4. **Security and safety:** attacks on agents and search systems, safety benchmarks, defenses that are actually evaluated, crawler observability, and agents used for web-security testing.

These labels describe a paper's main role in this collection, not mutually exclusive topics. For example, WebArena is both an environment and a capability test; WASP is an attack benchmark rather than a defense; and AWE, EvoCrawl, and YURASCANNER use automation to find web vulnerabilities rather than studying attacks against web agents.

## Repository Map

| Location | Contents |
|---|---|
| [`Summaries/`](Summaries/) | 48 comprehensive paper summaries; the primary evidence base for this README |
| Repository root | 24 core PDFs, `README.md`, and the literature-search report |
| [`Security/`](Security/) | 17 security and safety PDFs |
| [`Borderline/`](Borderline/) | 7 adjacent PDFs on mobile agents, tool use, crawling, backdoors, and security foundations |
| [`docs/papers.md`](docs/papers.md) | Paper inventory and shorter topical descriptions |
| [`docs/problem_approach_matrix.md`](docs/problem_approach_matrix.md) | Research problems mapped to solution approaches |
| [`docs/gaps_and_research_directions.md`](docs/gaps_and_research_directions.md) | Gap analysis and possible research directions |
| [`docs/citation_clusters_and_reading_order.md`](docs/citation_clusters_and_reading_order.md) | Citation clusters and expanded reading paths |
| [`docs/metadata_verification.md`](docs/metadata_verification.md) | Venue/source verification notes and unresolved metadata uncertainty |

### Collection counts

| Collection unit | Count |
|---|---:|
| Core/root PDFs | 24 |
| `Security/` PDFs | 17 |
| `Borderline/` PDFs | 7 |
| **PDFs total** | **48** |
| `Summaries/` Markdown files | **48** |

The counts are filesystem counts, not a claim that all 48 papers are exclusively about browser agents. The seven borderline papers are intentionally retained because mobile control, API/tool selection, stateful crawling, persistent backdoors, and systems-level agent security illuminate mechanisms that web agents inherit.

## Area Overview

An agentic web system repeatedly observes an environment, interprets a natural-language goal, selects an action, receives a new observation, and continues until it stops. Depending on the system, observations may be HTML, a DOM or accessibility tree, screenshots, search results, retrieved documents, tool descriptions, or dialogue. Actions may include search, link traversal, clicking, typing, scrolling, form submission, tab control, citation collection, structured extraction, or external tool calls.

This differs from a conventional crawler, whose primary loop is URL discovery and fetching under a fixed policy. EvoCrawl and YURASCANNER show why the boundary is porous: reaching code and forms in modern applications can require ordered, state-changing interaction rather than link following alone. It also differs from classic scraping. AutoScraper generates a reusable extraction program, while Webscraper uses a multimodal browser agent plus parsing and merge tools to collect index-content records. In both cases, the target is repeated structured extraction, not merely completing one browser task.

Capability work in the collection progresses from reasoning-and-action and tool-use foundations (ReAct, Toolformer, Gorilla), through grounded shopping and browsing (WebShop, WebGPT), to general website control (Mind2Web, SeeAct, AutoWebGLM, WebVoyager, WebLINX, LASER), structured exploration and training (Go-Browse), and longer-horizon search or traversal (WebWalker, WebDancer, WebSailor). These systems explore text/HTML representations, screenshots, set-of-marks grounding, state-specific action spaces, demonstrations, synthetic trajectories, rejection sampling, and reinforcement learning.

Evaluation work increasingly checks outcomes rather than exact action-sequence imitation. WebArena uses programmatic validators in self-hosted sites; VisualWebArena adds visually grounded tasks; WorkArena and WorkArena++ test enterprise workflows; BrowserGym and AgentLab unify interfaces, execution, traces, and benchmark integration; MMInA evaluates multihop multimodal work across sites; BrowseComp emphasizes persistent discovery of obscure facts; BEARCUBS tests real-web computer use; Mind2Web 2 uses task-specific rubric trees and judge agents. Offline datasets improve stability but do not reproduce live interaction, while live-web tests face drift, rate limits, changing content, and evaluator reproducibility.

Security work must account for an agent consuming untrusted content while holding authority. The local papers demonstrate several distinct routes to failure:

- **Instruction-channel compromise:** indirect prompt injection in webpages, documents, messages, or retrieved items (Not What You've Signed Up For; Formalizing and Benchmarking Prompt Injection; WASP; Overcoming the Retrieval Barrier).
- **Evidence and recommendation manipulation:** fabricated facts, false consensus, source diversity, and polluted recommendation pages can shift or create endorsements without an explicit malicious instruction (SearchGEO; FORGE).
- **Tool, plugin, and integration compromise:** malicious tool descriptions or broken role/provenance boundaries influence selection and execution (ToolHijacker; When AI Meets the Web; Unsafe LLM-Based Search).
- **Persistent and supply-chain compromise:** triggers can enter planning, memory, observations, tools, or reusable executable skills and survive across a workflow (BackdoorAgent; SkillTrojan).
- **Unsafe user-directed action and policy failure:** an agent may comply with harmful requests or complete nominal tasks while violating consent, privacy, or organizational rules (SafeArena; ST-WebAgentBench).

Only a subset of the security papers evaluates a proposed defense. WARD trains and tests a multimodal prompt-injection guard; RENNERVATE detects and removes suspected injected tokens using attention features; ACE fixes a typed plan before interacting with untrusted apps and enforces isolation and information-flow checks; Unsafe LLM-Based Search evaluates an answer-and-page inspection pipeline. Formalizing and Benchmarking Prompt Injection tests ten existing defenses but finds none reliable; WASP is an attack benchmark; Overcoming the Retrieval Barrier evaluates and adaptively bypasses simple retrieval-stage defenses. They should not be read as demonstrated defensive solutions.

## Paper Categories

The following map accounts for all 48 summaries. Papers appear once under a primary role even when they contribute to several areas.

| Family | Papers | What they contribute |
|---|---|---|
| Reasoning and tool-use foundations | ReAct; Toolformer; Gorilla | Reasoning/action loops, self-supervised tool calls, and retrieved API documentation |
| Browser-agent systems and training | WebGPT; WebShop; Mind2Web; AutoWebGLM; SeeAct; LASER; WebLINX; WebVoyager; Go-Browse; WebDancer; WebSailor | Browsing, grounded control, demonstrations, structured exploration, and information-seeking training |
| Benchmarks and evaluation infrastructure | WebArena; VisualWebArena; WorkArena; WorkArena++; BrowserGym; MMInA; BrowseComp; BEARCUBS; Mind2Web 2; WebWalker | Functional task evaluation, visual and enterprise tasks, cross-site workflows, hard search, traversal, judging, and reproducibility |
| Extraction and stateful exploration | AutoScraper; Webscraper; EvoCrawl; YURASCANNER | Reusable wrapper generation, multimodal extraction, evolutionary crawling, and task-directed web scanning |
| Prompt-injection attacks and attack benchmarks | Not What You've Signed Up For; Formalizing and Benchmarking Prompt Injection; WASP; Overcoming the Retrieval Barrier | Real-world attack cases, formalization, end-to-end web-agent compromise, and retrieval optimization |
| Evidence, search, tool, and integration threats | SearchGEO; FORGE; ToolHijacker; When AI Meets the Web | Endorsement manipulation, web-content pollution, malicious tool retrieval, and chatbot-plugin trust-boundary failures |
| Safety and harmful-action evaluation | SafeArena; ST-WebAgentBench | Harmful-request compliance and policy-aware enterprise task evaluation |
| Evaluated defensive systems | WARD; RENNERVATE; ACE; Unsafe LLM-Based Search | Multimodal guarding, token-level sanitization, plan/isolation architecture, and malicious-result filtering |
| Persistent and supply-chain attacks | BackdoorAgent; SkillTrojan | Trajectory-stage backdoors and malicious reusable skills |
| Web-security testing agents | AWE | Specialized, memory-augmented web penetration testing with browser-backed verification |
| Crawler observability and governance evidence | Identifying AI Web Scrapers Using Canary Tokens | Empirical attribution of chatbot retrieval paths and limits of post-collection blocking |
| Adjacent evaluation and security synthesis | AndroidWorld; Toward Secure LLM Agents | Dynamic mobile-agent evaluation and a systems-oriented survey of 247 agent-security papers |

## Selected Quantitative Findings

These numbers are selective anchors, not directly comparable leaderboard entries. The papers differ in task construction, model access, observation modality, scoring, dates, and whether environments are live, cached, or self-hosted.

| Paper | Reported finding | Interpretation and caveat |
|---|---|---|
| WebArena | Best reported GPT-4 setup: **14.41%** overall success; humans: **78.24%** on 812 tasks | Functional success in reproducible self-hosted sites; a large capability gap remains |
| VisualWebArena | Best original baseline, GPT-4V + set-of-marks: **16.37%**; humans: **88.70%** | Visual access helps, but visual grounding and long-horizon control remain bottlenecks |
| WebVoyager | **59.1%** human-judged success on 643 live-site tasks, versus **40.1%** for its text-only variant | Stronger than the text-only ablation, but live-site state and content can drift; the paper separately validates scalable model-based trajectory judging against humans |
| MMInA | GPT-4V: about **21.8%** full-task success; humans: **96.25%** | Single-site ability does not translate reliably to multihop, multisite completion |
| WorkArena++ | Humans: **93.9%** on the sampled curriculum; GPT-4o: **2.1%** on matched L2 tasks and **0%** on L3 | Compositional enterprise work is much harder than atomic browser tasks |
| BrowseComp | Deep Research: **51.5%**; best-of-64 selection: about **78%**; humans solved **29.2%** of attempted questions | More browsing effort and parallel attempts help; the system had relevant training and the benchmark targets unusually obscure facts |
| AutoScraper | GPT-4-Turbo on SWDE: **88.69 F1**, **71.56%** fully correct, **4.06%** unexecutable; mean speed break-even at **19.5 pages** | Reusable wrappers can pay off at scale, but results depend strongly on the model and stable page structure |
| ST-WebAgentBench | Mean nominal completion fell from **24.3%** to **15.0%** when policy compliance was required across 375 tasks | Conventional completion scores can hide consent, policy, and trustworthiness failures |
| WASP | Intermediate hijacking reached about **85.7%** in one configuration; complete attacker-goal success peaked around **16.7%** | Failure to finish an attack is often agent incompetence, not resistance |
| Overcoming the Retrieval Barrier | A ten-token trigger averaged **94.1% Recall@5** in the reported table; one multi-agent setting exfiltrated a private SSH file in **8/10** runs | Retrieval is part of the attack surface; the summary notes a small table/prose discrepancy (94.1% versus 95.6%) |
| SearchGEO | Overall explicit endorsement attack success ranged from **0.0% to 31.4%** across 13 backends | Backend choice mattered greatly, while failed attacks could still cause semantic shift |
| ACE | Blocked all **1,054 INJECAGENT** attacks and the paper's three new attacks | This is an evaluated architectural defense, but its benchmarks use simulated apps and its implementation lacks a full formal soundness guarantee |

Other useful scale markers include Mind2Web's broad offline task collection, WebLINX's 2,337 demonstrations over 155 sites, SafeArena's paired 250 harmful and 250 safe tasks, and WARD's 177,585-example training set. Scale alone does not establish realism, security, or generalization.

## What the Collection Supports—and Does Not

The collection supports the following broad conclusions:

- Outcome-based, long-horizon, visual, multisite, and policy-aware evaluations expose failures hidden by step-level or nominal completion metrics.
- Better page representation and grounding matter: HTML pruning, accessibility trees, screenshots, and set-of-marks each help in different settings, but none removes the grounding bottleneck.
- Structured exploration, demonstrations, and environment practice improve capability, while transfer to unfamiliar sites and changing live pages remains uneven.
- Agent security is not only prompt injection. Retrieval rank, source provenance, false consensus, tool descriptions, memory, installed skills, delegated authority, and external side effects all matter.
- High ordinary-task utility does not imply security, and low attacker-goal completion does not imply a sound defense.

It does **not** support claims that current web agents are generally reliable, that any one benchmark represents the open web, that a single guard solves prompt injection, or that `robots.txt` can retract already collected content. The canary-token study observes persistence and retrieval paths but cannot always distinguish caching from fresh crawling. Likewise, controlled pollution studies establish causal vulnerability in their experimental settings; they do not measure the prevalence of manipulation across the live web.

## Research Gaps Exposed by This Collection

These are gaps visible across the 48-paper corpus, not an exhaustive census of all published work:

1. **Crawling and extraction are weakly joined to agent evaluation.** AutoScraper and Webscraper measure extraction, while EvoCrawl and YURASCANNER measure state discovery and security reachability; few shared tasks connect coverage, extraction correctness, cost, change resilience, and task completion.
2. **Scraping governance is under-evaluated.** The canary-token study reveals uncertain and persistent retrieval paths, but the collection offers little experimental work on consent, provenance, deletion, rate limits, or enforceable site policy for agentic extraction.
3. **Live-web realism and reproducibility remain in tension.** Self-hosted environments stabilize state; live and cached-web evaluations better expose drift, search behavior, and adversarial content but are harder to version and audit.
4. **Trajectory quality is incompletely measured.** Final success can conceal unnecessary actions, unsafe intermediate states, unsupported evidence, privacy exposure, policy violations, or partial attacker control.
5. **Long-horizon security is thinner than one-step detection.** BackdoorAgent, SkillTrojan, and the security survey highlight persistence, memory, composition, revocation, and multi-agent propagation, but evaluation remains fragmented.
6. **Defenses are rarely composed.** WARD, RENNERVATE, ACE, and search-result filtering intervene at different layers; the collection does not establish how guards, provenance, permissions, information-flow control, sandboxing, and human approval behave as a complete stack.
7. **Capability-adjusted safety needs broader use.** SafeArena pairs harmful and benign capability, ST-WebAgentBench combines completion with policy compliance, and WASP separates diversion from completed harm; these distinctions are not standard across capability benchmarks.
8. **Evidence integrity needs first-class metrics.** Mind2Web 2 evaluates attribution, while SearchGEO and FORGE demonstrate endorsement manipulation. More evaluations should trace source independence, support for each claim, time sensitivity, and evidence lineage.
9. **Enterprise and consequential actions need stronger authorization models.** WorkArena++, ST-WebAgentBench, ACE, and the secure-agent survey point to unresolved approval, least-privilege, audit, rollback, and exception-handling requirements.
10. **Reported gains often lack uncertainty or stable comparability.** Several summaries note missing significance tests, small subsets, proprietary model drift, evaluator dependence, or source inconsistencies; benchmark maintenance and reporting standards remain important research infrastructure.

See [`docs/gaps_and_research_directions.md`](docs/gaps_and_research_directions.md) for the repository's longer-form synthesis, while treating the 48 comprehensive summaries as the current audit base.

## Suggested Reading Paths

For a general entry point:

1. **Foundations:** ReAct, WebGPT, and WebShop.
2. **General web control:** Mind2Web, WebArena, SeeAct, VisualWebArena, and WebVoyager.
3. **Evaluation maturity:** BrowserGym, WorkArena++, MMInA, BEARCUBS, BrowseComp, and Mind2Web 2.
4. **Traversal and deep research:** WebWalker, Go-Browse, WebDancer, and WebSailor.
5. **Extraction and crawling:** AutoScraper, Webscraper, YURASCANNER, and EvoCrawl.
6. **Security threats:** Not What You've Signed Up For, Formalizing and Benchmarking Prompt Injection, WASP, Overcoming the Retrieval Barrier, SearchGEO, FORGE, ToolHijacker, BackdoorAgent, and SkillTrojan.
7. **Safety and defenses:** SafeArena, ST-WebAgentBench, WARD, RENNERVATE, ACE, and Unsafe LLM-Based Search.
8. **Systems synthesis:** Toward Secure LLM Agents.

Alternative focused paths:

- **Build or evaluate a browser agent:** ReAct → Mind2Web → WebArena → VisualWebArena → BrowserGym → WorkArena++.
- **Study information-seeking agents:** WebGPT → WebWalker → BrowseComp → WebDancer/WebSailor → Mind2Web 2.
- **Study extraction:** AutoScraper → Webscraper → YURASCANNER → EvoCrawl → Identifying AI Web Scrapers Using Canary Tokens.
- **Study agent security without conflating attacks and defenses:** Not What You've Signed Up For → Formalizing Prompt Injection → WASP → Overcoming the Retrieval Barrier → SearchGEO/FORGE → WARD/RENNERVATE/ACE → Toward Secure LLM Agents.

See [`docs/citation_clusters_and_reading_order.md`](docs/citation_clusters_and_reading_order.md) for expanded citation clusters.

## Evidence and Audit Method

This README was audited against the 48 files in `Summaries/` without web browsing. The process was:

1. Count the PDFs and summaries directly from the repository filesystem.
2. Read the current README and the local summaries for paper objectives, methods, reported findings, contributions, and limitations.
3. Assign every summary to a primary category while allowing conceptual overlap in the prose.
4. Retain repository links and collection metadata that could be verified locally.
5. Use exact quantitative findings only where the corresponding summary reports the value, and carry forward material caveats such as benchmark scope, evaluator type, training exposure, live-web drift, or internal source discrepancy.
6. Separate attack demonstrations, attack benchmarks, safety evaluations, and evaluated defenses. A paper is described as providing a defense only when it implements and evaluates one.

### Limitations of this audit

- The summaries are the primary source of truth for this README; the audit is not an independent replication of the papers' experiments.
- Summary accuracy depends on the locally stored PDFs and their extraction quality. Some summaries explicitly record missing labels, inconsistent counts, table/prose differences, or unequal comparisons from the source papers.
- The papers span different dates, environments, model versions, metrics, and threat models. Their percentages should not be ranked as if they came from a shared test set.
- Venue and publication status can change. This README does not infer metadata beyond the locally verified notes in [`docs/metadata_verification.md`](docs/metadata_verification.md).
- The collection is selective. A gap in these 48 papers is evidence about this repository's coverage, not proof that no work exists elsewhere.

When adding a paper, add its PDF to the appropriate collection folder, add a matching comprehensive summary, update the filesystem counts, and then revisit the categories, quantitative anchors, gaps, and reading paths.
