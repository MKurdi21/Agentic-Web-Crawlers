# Academic Literature Audit: Agentic AI / LLM Agents Interacting with the Web

**Topic:** Agentic AI and LLM agents for web browsing, traversal, scraping, information seeking, browser automation, and web security
**Prepared for:** Mohammad Alkurdi  
**Historical search window documented locally:** June 3, 2021–July 22, 2026
**Corpus audit completed:** July 22, 2026

---

## Audit basis, scope, and terminology

This revision is a **closed-corpus audit**. Its primary evidence is the full set of 48 files in `Summaries/`, each corresponding to one locally held PDF: **24 core/root PDFs, 17 PDFs in `Security/`, and 7 PDFs in `Borderline/`**. No web verification was performed for this revision. URLs already documented in the prior report are preserved unless the local summary clearly contradicts the associated metadata; a URL is not evidence that it was rechecked on July 22, 2026.

The inventory below distinguishes:

- **Core/root:** a local PDF directly about web interaction, navigation, information seeking, traversal, scraping, or a web-agent benchmark/environment.
- **Security:** a local PDF whose primary contribution is an attack, defense, safety evaluation, security architecture, malicious-content study, security scanner, or closely related web/agent threat.
- **Borderline:** a local PDF useful for context but not centrally about LLM-based web agents (general tool/API/mobile agents, conventional web crawling, or broad agent security).
- **Historical-search-only:** a relevant item named by the earlier web search, but not represented by a local PDF or one of the 48 summaries. These items are not counted as locally included papers and retain only the metadata recorded in the old report.

“Security-related” is used narrowly. Merely controlling a browser, providing a benchmark substrate, or taking consequential actions does **not** make a capability paper a security paper. Security papers are further labeled by role—**attack**, **defense**, **safety/measurement**, **offensive testing**, **deterrence/detection**, or **survey**—to avoid the ambiguous former label “direct security paper.” “Big 4” means a main paper at IEEE S&P, USENIX Security, ACM CCS, or NDSS; workshops are not counted as Big 4 main-conference papers.

## Corpus accounting

| Local location | Required | Accounted for below | Interpretation |
|---|---:|---:|---|
| Repository root | 24 | 24 | Core web-agent papers |
| `Security/` | 17 | 17 | Web/agent security papers |
| `Borderline/` | 7 | 7 | Contextual near-misses |
| **Total local PDFs / summaries** | **48** | **48** | **Exact closed corpus** |
| Historical-search-only items | Not part of local corpus | 3 explicitly inventoried | Not included in 48 |

## 1. Included local core/root papers (24)

All rows in this section have a local PDF and a corresponding summary. None is classified as a security paper merely because the agent can act on a website.

| # | Paper | Local evidence metadata | Primary contribution / audited classification | Security-related? | Locally documented URL(s) |
|---:|---|---|---|---|---|
| C1 | Webscraper: Leverage Multimodal Large Language Models for Index-Content Web Scraping | Guan-Lun Huang; Yuh-Jzer Joung; supplied 2026 arXiv-era paper | Browser-agent scraping across index/content pages, with dedicated parse and merge tools | No | <https://arxiv.org/abs/2603.29161> |
| C2 | WebSailor: Navigating Super-human Reasoning for Web Agent | Kuan Li et al.; 2025 | Long-horizon information-seeking agent training under high uncertainty | No | <https://arxiv.org/abs/2507.02592> |
| C3 | WebDancer: Towards Autonomous Information Seeking Agency | Jialong Wu et al.; arXiv:2505.22648v3, Aug. 10, 2025 | ReAct-style autonomous search/browse training and evaluation | No | <https://arxiv.org/abs/2505.22648> |
| C4 | WebWalker: Benchmarking LLMs in Web Traversal | Jialong Wu et al.; ACL 2025 long paper | Benchmark and agent for vertical traversal within website hierarchies | No | <https://aclanthology.org/2025.acl-long.508.pdf>; <https://arxiv.org/abs/2501.07572> |
| C5 | Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | Boyu Gou et al.; 2025 | Real-time, long-form agentic search benchmark with rubric-based agent judging | No | <https://arxiv.org/abs/2506.21506> |
| C6 | GO-BROWSE: Training Web Agents with Structured Exploration | Apurva Gandhi; Graham Neubig; **ICLR 2026** | Structured graph exploration for collecting web-agent training trajectories | No | <https://openreview.net/forum?id=IpzRWE52yw> |
| C7 | AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation | Wenhao Huang et al.; EMNLP 2024, pp. 2371–2389 | Generates and validates reusable extraction programs rather than repeatedly extracting with an LLM | No | <https://aclanthology.org/2024.emnlp-main.141/>; <https://arxiv.org/abs/2404.12753> |
| C8 | AutoWebGLM: A Large Language Model-based Web Navigating Agent | Hanyu Lai et al.; **KDD 2024** | Compact trained browser agent using simplified HTML, curriculum data, RL, and rejection sampling | No | <https://arxiv.org/abs/2404.03648> |
| C9 | GPT-4V(ision) is a Generalist Web Agent, if Grounded (SeeAct) | Boyuan Zheng et al.; 2024 paper / ICML 2024 as locally documented | Visual reasoning plus grounding for live-site action selection | No | <https://osu-nlp-group.github.io/SeeAct/>; <https://arxiv.org/abs/2401.01614> |
| C10 | WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue | Xing Han Lù; Zdeněk Kasner; Siva Reddy; 2024 / ICML 2024 as locally documented | Dialogue-conditioned navigation demonstrations on real websites | No | <https://mcgill-nlp.github.io/weblinx/>; <https://arxiv.org/abs/2402.05930> |
| C11 | WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | Hongliang He et al.; ACL 2024, pp. 6864–6890 | End-to-end visual/text browser agent evaluated on live sites | No | <https://aclanthology.org/2024.acl-long.371/>; <https://arxiv.org/abs/2401.13919> |
| C12 | LASER: LLM Agent with State-Space Exploration for Web Navigation | Kaixin Ma et al.; 2023 | Backtracking/state-space exploration for navigation rather than forward-only imitation | No | <https://arxiv.org/abs/2309.08172>; <https://openreview.net/pdf?id=sYFFyAILy7> |
| C13 | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao et al.; ICLR 2023 | Foundational interleaving of reasoning and actions, including Wikipedia search and WebShop | No; foundational rather than web-specific | <https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/>; <https://arxiv.org/abs/2210.03629> |
| C14 | WebGPT: Browser-assisted Question-Answering with Human Feedback | Reiichiro Nakano et al.; OpenAI technical report / 2021 preprint | Text-browser search, citation, synthesis, behavior cloning, reward modeling, and human feedback | No | <https://cdn.openai.com/WebGPT.pdf>; <https://arxiv.org/abs/2112.09332> |
| C15 | BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents | Jason Wei et al.; OpenAI benchmark report, 2025 | 1,266 hard-to-find but readily verifiable factual questions | No | <https://openai.com/index/browsecomp/> |
| C16 | BEARCUBS: A Benchmark for Computer-Using Web Agents | Yixiao Song et al.; **COLM 2025** | Human-validated live-web tasks requiring genuine computer use and multimodal interaction | No | <https://arxiv.org/abs/2503.07919> |
| C17 | MMInA: Benchmarking Multihop Multimodal Internet Agents | Shulin Tian et al.; Findings of ACL 2025, pp. 13682–13697 | Multihop multimodal tasks spanning multiple evolving websites | No | <https://aclanthology.org/2025.findings-acl.703/>; <https://arxiv.org/abs/2404.09992> |
| C18 | The BrowserGym Ecosystem for Web Agent Research | Thibault Le Sellier De Chezelles et al.; TMLR, Feb. 2025 | Unified browser environment, benchmark interfaces, and reproducible evaluation infrastructure | No; infrastructure is not itself a security contribution | <https://openreview.net/forum?id=5298fKGmv3>; <https://github.com/servicenow/browsergym> |
| C19 | WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks | Léo Boisvert et al.; NeurIPS 2024 Datasets and Benchmarks | Compositional enterprise browser tasks requiring planning, memory, and infeasibility recognition | No | <https://openreview.net/forum?id=PCjK8dqrWW&noteId=nIdhK4PhIJ>; <https://proceedings.neurips.cc/paper_files/paper/2024/file/0b82662b6c32e887bb252a74d8cb2d5e-Paper-Datasets_and_Benchmarks_Track.pdf> |
| C20 | WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks? | Alexandre Drouin et al.; ICML 2024 | Large executable ServiceNow task environment and BrowserGym-based evaluation | No | <https://servicenow.github.io/WorkArena/>; <https://arxiv.org/abs/2403.07718> |
| C21 | VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks | Jing Yu Koh et al.; ACL 2024, pp. 881–905 | Self-hosted visually grounded tasks whose needed evidence is not reducible to text alone | No | <https://aclanthology.org/2024.acl-long.50/>; <https://arxiv.org/abs/2401.13649> |
| C22 | WebArena: A Realistic Web Environment for Building Autonomous Agents | Shuyan Zhou et al.; ICLR 2024 | Executable self-hosted websites, realistic tasks, and functional outcome evaluators | No; benchmark substrate is not itself a security paper | <https://openreview.net/forum?id=rmiwIL98uQ>; <https://arxiv.org/abs/2307.13854> |
| C23 | Mind2Web: Towards a Generalist Agent for the Web | Xiang Deng et al.; NeurIPS 2023 Datasets and Benchmarks | Cross-website instruction-following dataset and element/action prediction benchmark | No | <https://proceedings.neurips.cc/paper_files/paper/2023/hash/5950bf290a1570ea401bf98882128160-Abstract-Datasets_and_Benchmarks.html>; <https://arxiv.org/abs/2306.06070> |
| C24 | WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents | Shunyu Yao et al.; NeurIPS 2022 | Simulated shopping environment with automatically computed task reward | No | <https://proceedings.neurips.cc/paper_files/paper/2022/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html>; <https://arxiv.org/abs/2207.01206> |

## 2. Included local Security papers (17)

| # | Paper | Local evidence metadata | Audited security role and relevance | Big 4 main paper? | Locally documented URL(s) |
|---:|---|---|---|---|---|
| S1 | WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections | Tri Cao et al.; supplied 2026 paper | **Defense:** trained guard for HTML and visual prompt injection, including adaptive attacks | No | <https://arxiv.org/abs/2605.15030> |
| S2 | Identifying AI Web Scrapers Using Canary Tokens | Steven Seiden et al.; supplied 2026 paper | **Deterrence/detection measurement:** plants canaries in web content and later probes model outputs; not a privacy-leak paper in the victim-agent sense | No | <https://arxiv.org/abs/2605.13706> |
| S3 | When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins | Yigitcan Kaya et al.; accepted IEEE S&P 2026 | **Ecosystem measurement, attack, and prototype defense:** forged roles, scraped untrusted content, tool hijacking, and plugin trust-boundary failures | **IEEE S&P 2026** | <https://sp2026.ieee-security.org/accepted-papers.html>; <https://arxiv.org/abs/2511.05797> |
| S4 | Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems | Hongyan Chang et al.; USENIX Security 2026 as locally documented | **Attack and defense evaluation:** optimizes content for retrieval before testing end-to-end prompt injection in RAG and agent systems | **USENIX Security 2026** | <https://www.usenix.org/conference/usenixsecurity26/presentation/chang> |
| S5 | Prompt Injection Attack to Tool Selection in LLM Agents | Jiawen Shi et al.; NDSS 2026 | **Attack:** poisons retrievable tool documentation so the agent selects an attacker-chosen tool; tests existing defenses | **NDSS 2026** | <https://www.ndss-symposium.org/wp-content/uploads/2026-s675-paper.pdf> |
| S6 | Attention Is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs (RENNERVATE) | Yinan Zhong et al.; NDSS 2026 | **Defense:** token-level attention-derived detection and sanitization for retrieved content; motivates web agents but is not browser-specific | **NDSS 2026** | <https://www.ndss-symposium.org/ndss-paper/attention-is-all-you-need-to-defend-against-indirect-prompt-injection-attacks-in-llms/> |
| S7 | AWE: Adaptive Agents for Dynamic Web Penetration Testing | Akshat Singh Jaswal; Ashish Baghel; **LAST-X workshop, Feb. 27, 2026** | **Offensive security testing:** structured specialist agents, persistent vulnerability-specific memory, adaptive payloads, and browser verification | **No — workshop, not NDSS main conference** | <https://www.ndss-symposium.org/ndss-paper/auto-draft-680/> |
| S8 | ACE: A Security Architecture for LLM-Integrated App Systems | Evan Li et al.; NDSS 2026 | **Defense architecture:** trusted ahead-of-time typed plans, information-flow checks, app matching, and isolated execution | **NDSS 2026** | <https://www.ndss-symposium.org/ndss-paper/ace-a-security-architecture-for-llm-integrated-app-systems/> |
| S9 | Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search | Zeren Luo et al.; USENIX Security 2025 | **Safety measurement and mitigation:** malicious URLs/content in AI-powered search, phishing and documentation case studies, URL/content filters | **USENIX Security 2025** | <https://www.usenix.org/conference/usenixsecurity25/presentation/luo-zeren> |
| S10 | WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks | Ivan Evtimov et al.; **NeurIPS 2025 Datasets and Benchmarks** | **Attack benchmark:** separates diversion from completed attacker goals and measures utility/defense tradeoffs | No | <https://arxiv.org/abs/2504.18575>; <https://arxiv.org/pdf/2504.18575> |
| S11 | SAFEARENA: Evaluating the Safety of Autonomous Web Agents | Ada Defne Tur et al.; ICML 2025, PMLR 267 | **Misuse/safety benchmark:** harmful and benign browser tasks; measures refusal, action, and task completion | No | <https://openreview.net/forum?id=7TrOBcxSvy>; <https://arxiv.org/abs/2503.04957> |
| S12 | YURASCANNER: Leveraging LLMs for Task-driven Web App Scanning | Aleksei Stafeev et al.; NDSS 2025 | **Offensive security testing:** LLM-guided workflow crawling exposes deep forms and supports XSS scanning | **NDSS 2025** | <https://www.ndss-symposium.org/wp-content/uploads/2025-388-paper.pdf> |
| S13 | ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents | Ido Levy et al.; **ICLR 2026** | **Safety/trustworthiness benchmark:** policy compliance, user intent, confidentiality, and task correctness in configurable web tasks | No | <https://arxiv.org/abs/2410.06703> |
| S14 | Formalizing and Benchmarking Prompt Injection Attacks and Defenses | Yupei Liu et al.; USENIX Security 2024 | **Attack/defense framework:** general LLM-integrated applications; relevant when web content is concatenated with trusted instructions, but not web-agent-specific | **USENIX Security 2024** | <https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei> |
| S15 | Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Kai Greshake et al.; ACM AISec 2023 workshop | **Attack/systematization:** webpage, search, email, document, memory, and tool-mediated indirect prompt injection with confidentiality/integrity/availability impacts | No — ACM workshop, not ACM CCS | <https://dl.acm.org/doi/10.1145/3605764.3623985> |
| S16 | How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation (SearchGEO) | Yimeng Chen et al.; supplied 2026 arXiv paper | **Recommendation-integrity measurement:** manipulated evidence, credentials, consensus, and citation structures without explicit injected instructions | No | <https://arxiv.org/abs/2606.16821> |
| S17 | One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders (FORGE) | Minghao Luo; Liang Chen; supplied 2026 arXiv paper | **Recommendation-integrity attack benchmark:** rewrites retrieved product pages to promote fabricated products | No | <https://arxiv.org/abs/2606.13610> |

### Big 4 accounting within the local Security set

| Venue | Local included main papers | Caveat |
|---|---|---|
| IEEE S&P | When AI Meets the Web (2026) | Accepted-paper status is what the local summary records. |
| USENIX Security | Formalizing and Benchmarking Prompt Injection Attacks and Defenses (2024); Unsafe LLM-Based Search (2025); Overcoming the Retrieval Barrier (2026) | The latter’s venue is retained from locally documented metadata. |
| NDSS | YURASCANNER (2025); Prompt Injection Attack to Tool Selection (2026); RENNERVATE (2026); ACE (2026) | AWE is excluded from this count because its summary identifies LAST-X, a workshop. |
| ACM CCS | None in the local corpus | The Greshake et al. paper is ACM AISec 2023, not CCS. |

Thus, **8 of the 17 local Security papers** are locally documented as Big 4 main papers: 1 IEEE S&P, 3 USENIX Security, and 4 NDSS.

## 3. Included local Borderline papers (7)

| # | Paper | Local evidence metadata | Why borderline / use in this review | Security-related? |
|---:|---|---|---|---|
| B1 | Toolformer: Language Models Can Teach Themselves to Use Tools | Timo Schick et al.; NeurIPS 2023 as previously documented | Foundational self-supervised API use, including search-like tools, but no browser traversal or crawling | No |
| B2 | Gorilla: Large Language Model Connected with Massive APIs | Shishir G. Patil et al.; NeurIPS 2024 | API retrieval and invocation rather than website interaction | No |
| B3 | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | Christopher Rawles et al.; **ICLR 2025** | Valuable outcome-based GUI-agent comparison, but mobile apps rather than the web | No |
| B4 | EvoCrawl: Exploring Web Application Code and State using Evolutionary Search | Xiangyu Guo et al.; NDSS 2025 | Highly relevant stateful web crawling, but evolutionary search rather than LLM/agentic AI in the requested sense | Yes — defensive/offensive web-security testing, not LLM-agent security |
| B5 | BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents | Yunhao Feng et al.; Findings of ACL 2026 | General trajectory-level backdoors across planning, memory, tools, web, drive, code, and driving; only partly web-specific | Yes — attack |
| B6 | SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems | Yunhao Feng et al.; ICML 2026, PMLR 306 | Third-party executable-skill supply chain rather than browser navigation; relevant to extensible web-agent deployments | Yes — attack |
| B7 | Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation | Yuchen Ling et al.; **ACM TOSEM, Jan. 2026**, 42 pages | Broad survey of agent systems, not a primary web-agent study; useful framing for authority, state, tool, and multi-agent boundaries | Yes — survey |

## 4. Relevant papers mentioned only in the historical search

These records are retained to preserve the earlier search audit, but **they have no local PDF and no summary in the 48-file evidence set**. Their metadata was not reverified in this no-browse revision, and they are excluded from all local-corpus counts and synthesis statistics.

| Historical item | Previously recorded metadata | Why relevant | Previously recorded URL(s) |
|---|---|---|---|
| Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems | Divya Akkil et al.; OpenReview; 2025; status formerly described as preprint/workshop-style | Hierarchical browser agent, DOM distillation, self-refinement | <https://openreview.net/forum?id=7PQnFTbizU> |
| WebCanvas: Benchmarking Web Agents in Online Environments | Authors not locally verified; OpenReview/arXiv; 2024 | Dynamic online web-agent evaluation | <https://openreview.net/forum?id=wkp57p0uhm>; <https://arxiv.org/abs/2406.12373> |
| Ferret-UI / Ferret-UI Lite | Authors not locally verified; arXiv/Apple research; 2024 | GUI/mobile grounding background, not specifically web traversal | No URL was recorded in the prior inventory |

The old search narrative also named systems, benchmarks, and related work inside queries or prose. A mention in a query is not an inclusion decision and should not be read as evidence that a paper was downloaded, summarized, or verified.

## 5. Evidence-backed synthesis across the 48 local papers

### 5.1 Capability and evaluation trends

The capability literature moves through three overlapping evaluation regimes.

First, early systems test **grounded language action in constrained environments**. WebShop supplies automatic reward in a simulated store; ReAct shows that interleaved reasoning and action can improve interactive behavior; WebGPT turns browsing into text actions and uses demonstrations, preference comparisons, reward modeling, and best-of-*n* selection. These works establish the agent loop but do not reproduce the volatility and visual complexity of the live web.

Second, datasets and self-hosted environments pursue **breadth, realism, and reproducibility**. Mind2Web spans many sites but largely evaluates action/element prediction from recorded interactions. WebArena, VisualWebArena, WorkArena, and WorkArena++ offer executable websites and functional evaluators, while BrowserGym normalizes observation/action APIs and evaluation. The progression also exposes a core measurement lesson: matching a single reference trajectory is weaker than verifying the final state, because multiple action sequences can be valid. AndroidWorld reinforces this point outside the web domain with direct state-based evaluators.

Third, live-web and deep-research benchmarks emphasize **open-world change, multimodality, and long horizons**. WebVoyager and SeeAct combine screenshots with grounding; BEARCUBS deliberately requires video, games, 3D interfaces, and other computer-use skills; MMInA requires multihop multimodal work across sites; WebWalker tests vertical traversal within site hierarchies; BrowseComp, WebDancer, WebSailor, and Mind2Web 2 test protracted information seeking and synthesis. This realism increases ecological validity but reduces reproducibility: pages, rankings, availability, prices, and model/tool backends can change.

Training trends likewise shift from prompting toward **agent-specific data and search**. AutoWebGLM uses curriculum learning, self-sampling RL, and rejection sampling; LASER explicitly explores and backtracks over states; GO-BROWSE treats websites as graphs and gathers diverse feasible trajectories; WebDancer and WebSailor train long-horizon search behavior. Across these studies, stronger base models help, but environment-specific interaction data, observation compression, grounding, memory, and recovery mechanisms remain decisive.

Headline results demonstrate both progress and persistent brittleness:

- WebShop agents achieved roughly **29%** success versus about **60%** for human experts in that environment.
- WebVoyager reported **59.1%** over 643 tasks on 15 sites, versus **40.1%** for its text-only variant and **30.8%** for GPT-4 with integrated tools.
- WebWalker’s best core result was **37.50%**, although combining ordinary RAG with link traversal improved every tested difficulty level.
- WorkArena’s strongest reported model completed about **43%**, and all tested models failed list filtering; WorkArena++ reported about **2%** for GPT-4o versus roughly **94%** for humans, with zero on its more realistic L3 subset.
- BEARCUBS reports about **66%** for the strongest tested agent and about **85%** for humans, while older computer-use agents were roughly **13–23%**.
- AndroidWorld, included only as a GUI-agent comparator, reports **30.6%** for its strongest agent versus **80.0%** for people.

These numbers are **not a leaderboard across papers**. They differ in model generation, scaffolding, observation type, tool access, task set, website state, evaluator, human protocol, maximum steps, and publication time. Some are offline, some self-hosted, some simulated, and some live. Even identically named backbones may be paired with different prompts and agent implementations.

### 5.2 Extraction, scraping, crawling, and traversal

Only a minority of the core corpus directly studies repeatable data extraction. AutoScraper generates executable, reusable extraction rules and progressively narrows pages after failures; on SWDE its GPT-4-Turbo configuration reports **88.69 F1**, **71.56% fully correct**, and **4.06% unexecutable**, with a reported break-even against repeated direct LLM extraction at about **19.5 pages on average**. Its limitations are central rather than incidental: XPath rules are fragile, multiple values remain difficult, golden labels materially affect results, and a scraper can execute while extracting the wrong content.

Webscraper tackles dynamic index-content sites with a browser agent plus dedicated parse and merge tools. Across six news sites and two shopping platforms, the full combination was more consistent than a general agent or prompting alone, especially for pagination and multi-page aggregation. The supplied summary does not justify extrapolating this small-site study to web-scale crawling. Both papers suggest a hybrid architecture: expensive agentic interpretation discovers a procedure, then deterministic code or specialized tools perform repeated extraction.

Traversal papers address a related but different objective. WebWalker follows site hierarchies to answer questions; LASER backtracks through navigation states; GO-BROWSE collects graph-structured trajectories; YURASCANNER pursues task-defined workflows to expose deep application states. Conventional EvoCrawl is an important near-miss: it combines evolutionary search, code coverage, and server-side state but is not LLM-based. Together, these papers show why “search,” “browsing,” “crawling,” and “scraping” should not be collapsed: they optimize respectively for retrieval, task completion, state/coverage exploration, and structured extraction.

### 5.3 Security threat families

The Security and security-relevant Borderline papers cover at least seven distinct threat families:

1. **Indirect prompt injection from untrusted content.** Greshake et al. establish real application attack paths through webpages, search, documents, email, and memory. Formalizing and Benchmarking supplies a general attack/defense framework. WASP places attacks inside functioning web tasks and distinguishes agent diversion from actual malicious state changes. WARD and RENNERVATE focus on detection/sanitization defenses.
2. **Retrieval-layer poisoning.** Overcoming the Retrieval Barrier optimizes malicious content to be retrieved before it can inject the downstream model. Tool-selection injection similarly attacks both retrieval and final selection using poisoned tool descriptions.
3. **Application integration and trust-boundary failure.** When AI Meets the Web finds that forged message roles and indiscriminate webpage scraping undermine the model’s instruction hierarchy. ACE treats app outputs as untrusted data and prevents them from rewriting a plan.
4. **Unsafe or malicious search evidence without explicit instructions.** Unsafe LLM-Based Search studies risky URLs and content. SearchGEO manipulates credibility signals, consensus, and citations; FORGE pollutes product pages to induce recommendation of fabricated products. These are integrity/evidence attacks, not necessarily prompt injection.
5. **Agent misuse and policy noncompliance.** SAFEARENA measures willingness and ability to execute harmful web requests; ST-WebAgentBench evaluates safety and trustworthiness properties alongside task completion. High task capability can increase harm if refusal and authorization controls do not improve with it.
6. **Persistent backdoors and supply-chain compromise.** BackdoorAgent introduces triggers through plans, memory, tools, or observations that persist across trajectories. SkillTrojan targets reusable executable skills. These broaden the web-agent threat model from a malicious page to poisoned persistent state and installed capabilities.
7. **Security testing and scraper accountability.** YURASCANNER and AWE use agents offensively to find vulnerabilities; EvoCrawl supplies a non-LLM coverage comparator. Canary Tokens instead asks whether content was scraped and incorporated into an AI system. These should not be mislabeled as attacks *against* web agents.

### 5.4 Defenses that were actually evaluated

The collection contains more attacks and benchmarks than mature defenses. The following defenses have reported empirical tests in their summaries:

- **WARD** trains guards on HTML and visual injections, then adds prompt-injection-on-guard training and adaptive adversarial training. Under in-domain adaptive attacks, final-cycle attempt success was **0.34%** for WARD-2B and **0.62%** for WARD-0.8B; the corresponding sample success was **3.12%** and **5.62%**. On cross-domain adaptive sets, per-dataset rates were 0–9%, but the study still reports a benign-utility evaluation on 802 WebArena tasks and a real failure case. These figures are specific to its attack budgets, guard placement, models, and judges.
- **RENNERVATE** uses attention patterns to detect token runs associated with injected tasks and sanitizes them. It reduced aggregate FIPI attack success to 0–0.2% across most tested open models, but adaptive PAIR remained **19%** on LLaMA3 and TAP **9%**; cross-task residuals reached **23.9%** in one setting. It is a content defense, not an authorization architecture.
- **ACE** creates a typed plan only from trusted input, checks data flow, selects apps without allowing their text to change the plan, and executes apps in isolated containers. It reports **0% attack success / 100% security** on INJECAGENT and blocks three new attacks, while utility depends on the planning model; GPT-4.1 achieved **85.7%** relational-data accuracy. The fixed-plan design may not cover workflows that genuinely require open-ended replanning from untrusted observations.
- **Unsafe LLM-Based Search** evaluates content refinement plus URL detectors. The paper’s reported reductions must be interpreted with its particular malicious-site corpus, query constructions, labels, and commercial search systems; the defense is filtering, not proof that generated answers are trustworthy.
- **When AI Meets the Web** prototypes UGCBuster to identify user-generated content before scraping and hardens tool instructions. These mitigations directly address observed plugin architecture failures but do not amount to a general prompt-injection solution.
- **WASP** tests defensive system prompts and instruction-hierarchy configurations. Prompting did not reliably stop webpage influence and sometimes reduced benign utility. Across configurations, diversion was about **17–86%**, while complete attacker-goal success was **0–17%**—a gap the paper calls “security through incompetence.”
- **Overcoming the Retrieval Barrier** evaluates query paraphrasing, perplexity filtering, and token masking. None removes the architectural risk that attacker content can win retrieval and then be interpreted as instructions.
- **Formalizing and Benchmarking** evaluates multiple prompt-level and model-level defenses under a general application formulation. Its conclusions should not be treated as browser-agent results because action execution and webpage state are outside its main benchmark.
- **Tool-selection injection** tests StruQ, SecAlign, and detection defenses. SecAlign still leaves **84.6–97.5%** attack success in the reported tool-poisoning settings, showing that defenses tuned to conspicuous foreign instructions can fail on fluent, task-relevant malicious descriptions.

Defenses therefore operate at different layers and are complementary: content detection/sanitization, retrieval filtering, role/data separation, trusted planning, information-flow control, tool authorization, and runtime isolation. No paper in the collection demonstrates a compositional defense that is simultaneously robust to adaptive webpage attacks, poisoned retrieval and tools, persistent memory/skill backdoors, manipulated but non-instructional evidence, and harmful yet correctly executed user requests.

### 5.5 Additional quantitative anchors and non-comparability

Security results are especially easy to miscompare because “attack success” may mean a changed model answer, a diverted intermediate action, a retrieved poisoned item, a selected malicious tool, or a completed external side effect.

- Tool-selection injection reports cross-architecture attack success as high as **96.7%** on MetaTool and **88.2%** on ToolBench for a Llama-3.3-70B shadow model attacking GPT-4o; one malicious document was retrieved in over **96%** of ToolBench cases despite 9,650 benign documents. That is not comparable to WASP’s end-to-end state-change metric.
- YURASCANNER reports about **23%** invalid generated tasks and **61.3%** full or near completion among valid tasks. Across 20 applications, the two scanners found 13 unique previously unknown vulnerabilities; YURASCANNER found 12 and Black Widow three, with overlap. These are scanning outcomes, not general browser-task success.
- AWE solved **54/104** benchmark challenges versus MAPTA’s **80/104**, but achieved **87%** on XSS and **67%** on blind SQL injection in its specialties, with about **98% fewer tokens**, **63% lower cost**, and about **4.4×** faster successful solves. Its specialist scope and workshop evaluation preclude a broad “better pentester” conclusion.
- When AI Meets the Web identifies **8** plugins permitting forged trusted-history roles and **15** scraping page content without separating first-party and user-generated text. These are plugin counts, not prevalence estimates for all web chatbots.
- BackdoorAgent can retain ordinary-task utility while malicious behavior persists, illustrating why clean task success cannot substitute for a security metric.

Every numeric anchor in this report is descriptive of its source paper’s setup. Cross-paper rankings would require harmonized tasks, attack objectives, agent scaffolds, model versions, observation channels, budgets, websites, judges, and final-state evaluators, which this collection does not provide.

### 5.6 Collection-level limitations and open gaps

The audited collection has important limitations:

- **Selection and recency:** it is a curated local collection, not a systematic-review database export. It is weighted toward 2024–2026 work and toward papers already found by the historical search.
- **Evidence level:** this revision relies on local summaries as primary evidence rather than re-extracting every PDF table or checking external records. Summary omissions or transcription errors can propagate. URLs and venue metadata not contradicted locally remain locally documented, not newly verified.
- **Venue heterogeneity:** the corpus mixes peer-reviewed conference/journal papers, workshops, technical reports, benchmarks, and arXiv papers. Publication status should not be inferred from inclusion.
- **Benchmark dependence:** many results reuse WebArena, BrowserGym, commercial model APIs, or LLM judges. Shared substrate does not imply identical configuration, and hosted systems change over time.
- **Live-web instability and contamination:** open-web tasks can disappear, change, become indexed with answers, trigger anti-bot measures, or expose agents to unforeseen content. Static/self-hosted tasks improve repeatability but omit those conditions.
- **Evaluator uncertainty:** action matching penalizes valid alternatives; LLM judges can be biased or wrong; functional evaluators cover only encoded state; human evaluation is costly and inconsistent. Security papers often mix intermediate and end-to-end measures.
- **Scale gap:** most “web agents” complete bounded tasks. Very little local evidence covers continuous web-scale crawling, politeness, robots/terms compliance, scheduling, deduplication, distributed frontier management, or longitudinal scraper maintenance.
- **Safety scope:** privacy leakage during ordinary browsing, least-privilege identity/session management, confirmation for irreversible actions, credential isolation, cross-origin policy, incident recovery, and safe live-site experimentation remain thinly evaluated.
- **Defense composition:** content guards, retrieval defenses, fixed planning, information-flow checks, and sandboxing are usually studied separately. Persistent state, skills, multiple agents, and non-instructional misinformation create cross-layer failure modes.
- **Dual use and ethics:** web penetration testing, large-scale scraping, and live-agent experiments can cause harm or violate site expectations. Results obtained in controlled or authorized settings do not authorize deployment against third-party systems.

The highest-value research gaps are therefore: reproducible long-horizon evaluation under adversarial pages; web-scale agentic crawling and scraper maintenance; security metrics tied to real side effects; provenance and credibility reasoning for retrieved evidence; privacy- and authorization-preserving browser architectures; signed and least-privilege agent skills; persistent-state integrity; and compositional defenses evaluated against adaptive attackers without sacrificing benign task utility.

## 6. Historical search audit trail (preserved, not rerun)

The earlier report recorded searches across arXiv, ACL Anthology, OpenReview, NeurIPS, ICLR, ICML, ACM Digital Library, USENIX Security, NDSS, IEEE S&P, project pages, and indexed scholarly results. Query families covered web agents, browser automation, scraping/crawling, information seeking, benchmarks, prompt injection, malicious webpages, privacy, tool security, safety, defenses, and targeted Big 4 venue searches for 2021–2026.

That trail explains how the collection was assembled; it is **not** a PRISMA-style reproducible review record. The current audit did not browse, rerun queries, inspect search-result counts, or independently confirm the former claim that no directly centered ACM CCS main paper was found. The defensible closed-corpus statement is narrower: **none of the 48 local included papers is an ACM CCS main-conference paper**.

## Conclusion

The local evidence set contains exactly **48 papers: 24 core/root, 17 Security, and 7 Borderline**. The core literature charts a progression from constrained text/tool interaction to executable, visual, live-web, and deep-research agents, but repeatedly shows large reliability gaps, especially for compositional tasks, recovery, multimodal interaction, and deep traversal. Extraction-specific evidence favors hybrid agent-plus-program designs over repeated free-form LLM extraction, while remaining far from web-scale crawling.

The security literature has expanded beyond classic indirect prompt injection to retrieval poisoning, tool-description hijacking, recommendation manipulation, unsafe search, misuse, persistent backdoors, and skill supply chains. Evaluated defenses show meaningful gains in their own settings, but their metrics and threat models are not interchangeable, residual adaptive attacks remain, and no local paper establishes comprehensive end-to-end protection. The central collection-level conclusion is consequently architectural: trustworthy web agents require coordinated controls over content, retrieval, planning, memory, tools, permissions, execution, and evaluation—not a single prompt or detector.
