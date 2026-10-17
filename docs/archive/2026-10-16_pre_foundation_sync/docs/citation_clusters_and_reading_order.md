# Citation Clusters and Recommended Reading Order

This guide is based on the 48 papers represented in `Summaries/`. Clusters are claim-specific citation bundles, not leaderboards or mutually exclusive categories. In particular, keep these roles distinct in prose:

- **Capability system:** proposes or trains an agent (for example, WebVoyager or WebSailor).
- **Benchmark/environment:** defines tasks, infrastructure, or evaluation (for example, WebArena or BrowseComp).
- **Attack:** demonstrates an adversarial mechanism (for example, ToolHijacker).
- **Safety evaluation:** measures unsafe behavior without necessarily introducing an attack or defense (for example, SafeArena).
- **Evaluated defense:** proposes a mitigation and measures both security and utility (for example, WARD or ACE).

Scores should be compared only within the same benchmark version, task split, agent scaffold, model, observation/action space, and evaluator. Live-web results are time-dependent; self-hosted, simulated, and frozen-retrieval results trade ecological validity for repeatability.

## Citation Clusters

### 1. Foundations: Grounded Reasoning, Browsing, and Tool Use

- **Claim scope:** Cite this cluster for the transition from language-only generation to systems that interleave reasoning, observations, browser actions, evidence collection, and calls to external tools.
- **Paper roles:** **ReAct** supplies the general reasoning/action/observation pattern; **WebGPT** is a trained browser-assisted, citation-producing QA system using demonstrations, reward modeling, and human feedback; **WebShop** is both a grounded shopping environment and an early learned interaction system; **Toolformer** teaches a model when and how to make mostly single-step API calls; **Gorilla** trains documentation-grounded API invocation.
- **Evidence anchors:** WebShop's learned agents reached about 29% success versus 59.6% for expert humans. WebGPT answers were preferred slightly more often than contractor answers under the same text browser, but its summaries stress source selection, perceived-authority, bias, and synthesis risks.
- **Boundaries/non-comparability:** ReAct is a prompting paradigm, not a browser benchmark; Toolformer and Gorilla primarily address tool/API invocation, not long-horizon GUI control. WebGPT's text browser and answer-preference evaluation are not comparable to WebShop's state-based shopping success.
- **Bridging citations:** Bridge to **Mind2Web** for broad website action data, **SeeAct** for visual grounding, **WebDancer/WebSailor** for search-agent training, and **Toward Secure LLM Agents** when moving from capability to authority and risk.

### 2. General Web Navigation Systems and Interaction Data

- **Claim scope:** Use for systems and datasets aimed at operating unfamiliar websites, choosing page elements, maintaining action histories, and generalizing beyond a single site.
- **Paper roles:** **Mind2Web** contributes a large cross-website instruction/action corpus and the MindAct candidate-generation/ranking system; **WebLINX** contributes 2,337 conversational demonstrations across 155 sites plus HTML reduction and action-sensitive metrics; **SeeAct** separates visual next-action planning from grounding; **WebVoyager** is an end-to-end live-web multimodal agent; **AutoWebGLM** is a trained 6B bilingual navigating agent using curriculum, error correction, and simulated practice.
- **Evidence anchors:** SeeAct completed 51.1% of live tasks when humans performed grounding, isolating grounding as the bottleneck. WebVoyager reached 59.1% on 643 tasks across 15 sites versus 40.1% for its text-only version. WebLINX's best trained system reached only about 65% of human agreement in its sampled comparison and degraded out of domain.
- **Boundaries/non-comparability:** Mind2Web largely evaluates action prediction from recorded states, whereas WebVoyager and SeeAct execute on live sites. Human-assisted SeeAct is an oracle-grounding diagnostic, not autonomous end-to-end success. AutoWebGLM results mix several benchmarks and an author-created bilingual benchmark; do not treat its best historical scores as current cross-paper rankings.
- **Bridging citations:** Use **WebArena/BrowserGym** for reproducible execution, **VisualWebArena/MMInA** for visual and cross-site demands, and **Go-Browse** for exploration-derived training data.

### 3. Reproducible Task-Completion Benchmarks and Infrastructure

- **Claim scope:** Cite when defining realistic, executable web-agent evaluation and the difference between trajectory imitation and checking the resulting site state.
- **Paper roles:** **WebShop** provides a controlled shopping simulator; **WebArena** provides 812 state-verified tasks over self-hosted replicas; **BrowserGym** unifies interfaces and benchmarks while AgentLab supports experiments and reproducibility; **Mind2Web** provides offline cross-domain action data; **AndroidWorld** supplies a dynamic, state-verified mobile-GUI analogue useful as methodological background.
- **Evidence anchors:** The original best WebArena GPT-4 setup solved 14.41% versus 78.24% for humans. AndroidWorld's strongest tested agent solved 30.6% of 116 tasks across 20 apps versus 80.0% for humans, illustrating why dynamically instantiated tasks and state-based graders matter.
- **Boundaries/non-comparability:** WebArena and WebShop are controlled web environments; Mind2Web is primarily offline; BrowserGym is infrastructure/ecosystem rather than one task distribution; AndroidWorld is mobile, not web. Scores reported through BrowserGym may use different agents or updated benchmark integrations from original papers.
- **Bridging citations:** Bridge to **WorkArena/WorkArena++** for enterprise complexity, **VisualWebArena** for visual state, and **ST-WebAgentBench** for policy-compliant rather than outcome-only success.

### 4. Visual, Multimodal, and Cross-Website Interaction

- **Claim scope:** Use to support claims that rendered layout, images, spatial grounding, cross-site memory, and interaction with media-rich pages add difficulty beyond DOM/text access.
- **Paper roles:** **VisualWebArena** is a self-hosted visual benchmark; **MMInA** benchmarks multihop, multimodal tasks spanning websites; **BEARCUBS** tests real-web computer use across text and interactive/multimodal questions; **SeeAct** diagnoses planning versus grounding; **WebVoyager** demonstrates an end-to-end multimodal system; **AndroidWorld** is a GUI benchmark bridge.
- **Evidence anchors:** VisualWebArena's strongest reported agent completed about one-fifth of tasks versus nearly nine-tenths for humans. MMInA reports 21.8% for GPT-4V versus about 96% human success. BEARCUBS reports 65.8% for ChatGPT Agent versus 84.7% for humans, with a pronounced gap on videos, games, and 3D/interactive content.
- **Boundaries/non-comparability:** These figures come from different eras, sites, models, graders, and notions of completion. BEARCUBS is live-web answer seeking; MMInA is cross-website task execution; VisualWebArena is reproducible and self-hosted. Visual access can help grounding but is not evidence of resilience to visual prompt injection or deceptive UI.
- **Bridging citations:** Bridge to **WebLINX** for conversational control, **Mind2Web 2** for cited research outputs, and **WASP/WARD** for adversarial webpage content.

### 5. Information Seeking, Deep Research, and Evidence-Based Answers

- **Claim scope:** Use for agents that search, traverse, synthesize, cite, or answer difficult questions rather than primarily modifying website state.
- **Paper roles:** **WebGPT** is the early trained browser-assisted QA system; **WebWalker** adds a traversal benchmark and a memory/answer agent; **BrowseComp** is a 1,266-question hard fact-finding benchmark; **Mind2Web 2** evaluates long-form research with task-specific agent judges and citation checks; **BEARCUBS** and **MMInA** test interactive/multimodal information access; **WebDancer** and **WebSailor** are trained search/reasoning systems.
- **Evidence anchors:** BrowseComp reports 51.5% for Deep Research and roughly 78% with best-of-64 selection, while humans solved 29.2% of attempted questions under a two-hour constraint—an effort-sensitive comparison, not evidence of general superhuman browsing. Mind2Web 2 reports 28% full completion for the best AI versus 54% for humans and 99.03% agreement for its detailed judge audit. WebWalker's best core result was 37.50%, and combining traversal with ordinary RAG improved every tested difficulty level.
- **Boundaries/non-comparability:** Short-answer accuracy, long-form requirement satisfaction, citation support, interactive task completion, and model-judged success measure different constructs. Live search changes over time, and parallel sampling/test-time compute can dominate results. WebDancer/WebSailor are systems evaluated on multiple datasets, not benchmark definitions.
- **Bridging citations:** Use **SearchGEO/FORGE** to question evidence independence, **Unsafe LLM-Based Search** for malicious-source exposure, and **Overcoming the Retrieval Barrier** for targeted retrieval poisoning.

### 6. Training Web Agents and Search Agents

- **Claim scope:** Cite for supervision, curriculum, exploration, synthetic task generation, reflection/error data, reinforcement learning, and test-time search as distinct ways to improve web agents.
- **Paper roles:** **WebGPT** uses demonstrations, reward modeling, RL, and best-of-*n*; **WebShop** compares imitation learning and RL; **AutoWebGLM** uses staged curriculum and simulated practice; **Go-Browse** performs structured site exploration to produce grounded tasks and trajectories; **WebDancer** uses synthetic data, supervised fine-tuning, and RL; **WebSailor** uses difficult synthetic research tasks, concise demonstrations, and RL; **LASER** constrains exploration with a manually defined state space.
- **Evidence anchors:** Go-Browse trains a 7B model to 21.7% on WebArena. WebDancer's strongest reported result reached 51.5 Pass@1 and 64.1% Pass@3 on GAIA. AutoWebGLM's error analysis attributes 44% of errors to hallucination and 28% to graphical recognition, showing that training gains do not erase perception failures.
- **Boundaries/non-comparability:** Training recipes are entangled with base models, tools, prompts, data filtering, and inference budgets. LASER's explicit state machine is not learned open-ended exploration. WebSailor and WebDancer target information seeking; Go-Browse and AutoWebGLM target website interaction. Do not compare their headline numbers across benchmarks.
- **Bridging citations:** Bridge to **Mind2Web/WebLINX** for human demonstrations, **BrowseComp** for effort scaling, and **BrowserGym** for controlled training/evaluation infrastructure.

### 7. Traversal, Stateful Crawling, and Web Security Scanning

- **Claim scope:** Use for reaching deep states, discovering workflows, or expanding attack-surface coverage—not for generic search alone.
- **Paper roles:** **WebWalker** studies vertical link traversal for QA; **Go-Browse** explores site graphs to collect training data; **LASER** is state-space-guided shopping navigation; **EvoCrawl** is a non-LLM evolutionary stateful security crawler; **YURASCANNER** is an LLM task-driven scanner; **AWE** is a procedure-guided adaptive penetration-testing agent.
- **Evidence anchors:** YURASCANNER generated 77.0% valid tasks and fully or partially completed 61.3% of those; it found 12 of 13 unique previously unknown vulnerabilities found across it and Black Widow, while also showing that traditional crawlers reached substantial unique surface. EvoCrawl found eight previously unknown XSS/access-control vulnerabilities on 10 applications. AWE solved 54/104 XBOW challenges versus MAPTA's 80/104, but reached 87% on XSS and 67% on blind SQL injection while using about 98% fewer tokens.
- **Boundaries/non-comparability:** WebWalker is answer-oriented traversal, Go-Browse is data collection, LASER is shopping navigation, and the other three are authorized security-testing systems. Form/URL/code coverage, vulnerability yield, QA accuracy, and challenge solve rate are not interchangeable. AWE's specialist efficiency does not imply broader coverage; YURASCANNER and conventional crawling are complementary, not a winner/loser pair.
- **Bridging citations:** Bridge to **AutoScraper/Webscraper** for extraction after discovery, **Canary Tokens** for crawler observability, and **Toward Secure LLM Agents** for dual-use and containment concerns.

### 8. Scraper Generation, Structured Extraction, and Crawler Observability

- **Claim scope:** Cite for turning pages into structured records, compiling reusable extraction logic, or measuring which crawlers feed AI answers.
- **Paper roles:** **AutoScraper** synthesizes and tests reusable extraction programs/XPaths; **Webscraper** equips a multimodal browser agent with parsing and merge tools for index-content scraping; **Canary Tokens** is an observational measurement study using per-crawler content variants, not a scraper capability or blocking defense.
- **Evidence anchors:** AutoScraper with GPT-4-Turbo reached 88.69 F1, 71.56% fully correct, and 4.06% unexecutable on SWDE, with average break-even against repeated direct LLM extraction at about 19.5 pages. Canary Tokens studied 22 chatbots and found indirect collection through advertised bots, browser-like clients, and search crawlers; removal or later `robots.txt` blocking usually did not retract already collected content.
- **Boundaries/non-comparability:** AutoScraper targets repeated template-like pages; Webscraper targets interactive index/detail workflows and does not yet automatically compile successful runs into dependable programs. Canary Tokens attributes content pathways but does not establish legal consent, prove model-training use, or offer a robust prevention mechanism.
- **Bridging citations:** Use **EvoCrawl/YURASCANNER** for state discovery, **When AI Meets the Web** for risks in scraped untrusted content, and **Toward Secure LLM Agents** for governance and least-privilege framing.

### 9. Enterprise and Conversational Browser Automation

- **Claim scope:** Use for knowledge-work interfaces, multi-turn user collaboration, compositional office tasks, and evaluation that includes organizational policies.
- **Paper roles:** **WorkArena** defines nearly 20,000 ServiceNow task instances and introduced BrowserGym; **WorkArena++** adds compositional L2/L3 tasks and infeasibility reasoning; **BrowserGym** standardizes execution; **WebLINX** studies conversational control across ordinary sites; **ST-WebAgentBench** is a safety-and-trust benchmark for policy-governed enterprise tasks; **ACE** is a general LLM-integrated app security architecture relevant to enterprise deployment.
- **Evidence anchors:** WorkArena's strongest reported GPT-4o result was 42.7%, with 0% for every model on list filtering. WorkArena++ reports 0% for all tested agents on 235 L3 instances versus 93.9% for humans. In ST-WebAgentBench, average apparent task success fell from 24.3% to 15.0% when policy compliance was required.
- **Boundaries/non-comparability:** ST-WebAgentBench evaluates whether behavior is both useful and compliant; it is not a prompt-injection benchmark. ACE evaluates a typed-plan, isolated tool/app architecture, not browser navigation quality. WorkArena and WorkArena++ differ sharply in compositional depth, so their percentages should not be placed in one trend line.
- **Bridging citations:** Bridge to **SafeArena** for malicious-user requests, **Toward Secure LLM Agents** for deployment controls, and **AndroidWorld** for dynamic state-based GUI evaluation outside the browser.

### 10. Indirect Prompt Injection: Threat Definition and Web Realism

- **Claim scope:** Use for attacker instructions embedded in untrusted content that an agent reads, retrieves, or receives through a plugin/tool.
- **Paper roles:** **Not What You've Signed Up For** (the real-world indirect-prompt-injection paper) establishes practical attacks and consequences across data sources and tools; **Formalizing and Benchmarking Prompt Injection** supplies a formalism, five attacks, ten models, seven tasks, and a defense comparison; **When AI Meets the Web** measures vulnerable third-party chatbot-plugin architectures and controlled direct/indirect attacks; **WASP** is an end-to-end web-agent injection benchmark; **Overcoming the Retrieval Barrier** optimizes triggers that cause poisoned content to be retrieved.
- **Evidence anchors:** The formalization paper's Combined Attack averaged 0.75 success value on GPT-4 and none of ten tested defenses was reliably sufficient. WASP observed intermediate compromise up to about 86%, but end-to-end attacker-task success topped out around 17%. The retrieval-barrier attack placed poisoned items in the top five about 94% of the time with ten optimized tokens and produced 80% SSH-key exfiltration in one GPT-4o multi-agent email workflow.
- **Boundaries/non-comparability:** Intermediate instruction following, completed attacker goals, retrieval rank, and data exfiltration are different endpoints. When AI Meets the Web concerns embedded website chatbots/plugins, not autonomous browser agents in general. Retrieval optimization is an attack enabler and includes limited defense tests; it is not itself a defense paper.
- **Bridging citations:** Bridge to **WARD/RENNERVATE/ACE** for evaluated defenses, **ToolHijacker** for malicious tool metadata, and **SearchGEO/FORGE** for manipulation without explicit injected commands.

### 11. Evaluated Prompt-Injection Defenses and Security Architectures

- **Claim scope:** Use when comparing mitigations that were explicitly evaluated for attack reduction and benign utility.
- **Paper roles:** **WARD** is a web-observation guard trained with adaptive adversarial data; **RENNERVATE** detects and removes instruction-like spans using attention features; **ACE** creates typed plans from trusted input, constrains app selection/data flow, and isolates execution; **Formalizing and Benchmarking Prompt Injection** evaluates ten earlier defenses; **When AI Meets the Web** evaluates prototype input/tool hardening in its plugin setting. **Overcoming the Retrieval Barrier** and **Unsafe LLM-Based Search** contain defense experiments but are primarily an attack paper and a risk/mitigation study, respectively.
- **Evidence anchors:** WARD reduced attack success to zero on its tested live-agent tasks with about 0.2–0.35% benign-step false alarms and strong adaptive-attack results. RENNERVATE reports roughly 98–99.6% detection accuracy across five LLMs and usually near-zero attack success. ACE reports 100% security on 1,054 INJECAGENT cases with a strongest average utility of 85.3%, plus at least 86% utility on ASB.
- **Boundaries/non-comparability:** WARD filters observations, RENNERVATE edits content, and ACE changes architecture and execution authority; each assumes different access and threat models. Detection accuracy, attack success, task utility, and false-positive rate must all be reported. No summary supports claiming universal protection: WARD excludes imperceptible pixel attacks, RENNERVATE struggles when malicious content resembles task data, and ACE depends on plan completeness, matching, and supported app semantics.
- **Bridging citations:** Pair with **WASP** for end-to-end web attacks, **ST-WebAgentBench** for policy compliance, and **Toward Secure LLM Agents** for defense-in-depth gaps.

### 12. Harmful Requests and Action-Level Safety Evaluation

- **Claim scope:** Use for whether agents comply with malicious users or violate operational policies even without poisoned webpage content.
- **Paper roles:** **SafeArena** evaluates harmful web tasks and multi-step jailbreak decomposition; **ST-WebAgentBench** evaluates enterprise policies, consent, data handling, and escalation; **Unsafe LLM-Based Search** measures exposure to malicious results/URLs and downstream risky answers; **BEARCUBS**, **WebArena**, and **WorkArena++** are capability benchmarks that reveal reliability gaps but are not safety benchmarks.
- **Evidence anchors:** SafeArena found broad harmful-task compliance and showed that every initially refused task could be completed by the safest tested agent after decomposition into benign-looking steps. ST-WebAgentBench's compliance-aware success was 15.0% versus 24.3% outcome-only. Unsafe LLM-Based Search found eight model configurations reproducing malicious code or treating a simulated phishing site as official; its combined answer/content checks mitigated most high-risk outputs but did not achieve perfect safety and utility.
- **Boundaries/non-comparability:** Malicious-user compliance, policy violation, unsafe information exposure, and ordinary task failure are different failure modes. SafeArena is not an indirect-injection benchmark; ST-WebAgentBench is not evidence-pollution evaluation; Unsafe LLM-Based Search evaluates AI search responses rather than arbitrary browser action sequences.
- **Bridging citations:** Use **ACE** for enforcement architecture, **SearchGEO/FORGE** for manipulated recommendations, and **Toward Secure LLM Agents** for privilege and human-approval controls.

### 13. Search Pollution, Recommendation Manipulation, and Source Trust

- **Claim scope:** Use when attacker-controlled web evidence changes answers or recommendations without necessarily containing an explicit instruction to the model.
- **Paper roles:** **SearchGEO** measures fabricated consensus/endorsement shifts across search agents; **FORGE** rewrites highly ranked product evidence and measures fake-product recommendation; **Unsafe LLM-Based Search** measures retrieval and repetition of malicious sites; **Overcoming the Retrieval Barrier** manipulates retrieval relevance and then injects payloads.
- **Evidence anchors:** SearchGEO's explicit attack success ranged from 0% for Claude-Sonnet-4.6 to 31.4% for Gemini-3-Flash, while subtler answer shifts occurred even without explicit success. FORGE shows that altering one high-ranked page can induce fake recommendations and repeated pages can push some models toward near-routine endorsement. The retrieval-barrier paper reports about 94% top-five retrieval for ten-token triggers.
- **Boundaries/non-comparability:** SearchGEO and FORGE primarily exploit evidence/trust aggregation; the retrieval-barrier attack optimizes retrievability for an instruction-bearing poison; Unsafe LLM-Based Search studies naturally or deliberately malicious web sources plus mitigations. Frozen/controlled retrieval, live search, rewritten documents, and simulated sites have different external validity. Recommendation rate is not prompt-injection ASR.
- **Bridging citations:** Bridge backward to **WebGPT/Mind2Web 2** for citation-based answering and forward to **WARD/ACE** only with the caveat that instruction defenses do not by themselves establish source truth or independence.

### 14. Malicious Tools, Skills, Backdoors, and Agent Supply Chains

- **Claim scope:** Use for compromise introduced through tool descriptions, installed executable skills, poisoned agent components, memory, or triggers that persist across a trajectory.
- **Paper roles:** **ToolHijacker** attacks retrieval and selection using optimized malicious tool documentation; **SkillTrojan** distributes an encrypted payload across cooperating installed skills; **BackdoorAgent** unifies trigger insertion across planning, memory, tools, and observations and benchmarks trajectory-level compromise; **Gorilla/Toolformer** are capability antecedents, not security evaluations.
- **Evidence anchors:** SkillTrojan reached up to 97.2% attack success while retaining 89.3% clean accuracy and largely evaded two lightweight scanners. BackdoorAgent shows high attack success can coexist with strong ordinary accuracy; in its Agent Web setting, effects were attack/model-specific (for example, Claude Sonnet 4.5 BadChain ASR 97.39 with 98.35 attacked accuracy, while many other combinations were near zero). ToolHijacker transferred across models, libraries, retrievers, and user wording and evaded several detector/reviewer baselines.
- **Boundaries/non-comparability:** Tool selection hijacking, executable multi-skill payloads, training/trajectory backdoors, and webpage prompt injection require different controls. BackdoorAgent spans code, QA, web, and driving; only part is web-specific. Clean task accuracy is not a security metric and may conceal compromise.
- **Bridging citations:** Use **ACE** for constrained app selection/execution, **Toward Secure LLM Agents** for provenance and lifecycle controls, and **Overcoming the Retrieval Barrier** where retrieval is the common attack surface.

### 15. System-Level Agent Security, Containment, and Lifecycle

- **Claim scope:** Cite for the argument that secure agents require bounded authority, trust separation, provenance, memory integrity, information-flow controls, monitoring, revocation, sandboxing, and human escalation—not only prompt filtering.
- **Paper roles:** **Toward Secure LLM Agents** synthesizes 247 papers into a threat/defense/lifecycle view; **ACE** implements trusted typed planning, data-flow checks, and isolated execution; **ST-WebAgentBench** evaluates policy-aware behavior and escalation; **WARD/RENNERVATE** cover observation-layer defenses; **SkillTrojan/BackdoorAgent/ToolHijacker** motivate supply-chain and trajectory monitoring.
- **Evidence anchors:** ACE blocked all reported INJECAGENT and three new architecture attacks while retaining substantial utility, but its app abstraction differs from open-ended browsers. The survey finds prompt injection dominant while memory poisoning and multi-agent propagation are growing, and identifies fragmented benchmarks that rarely combine long-term effects, utility, cost, and deployment consequences.
- **Boundaries/non-comparability:** The survey is synthesis, not a new benchmark; ACE is an architecture under specified app semantics; ST-WebAgentBench measures behavior rather than implementing a complete enforcement stack. No paper in the collection evaluates signed skill provenance, static analysis, runtime sandboxing, revocation, memory integrity, and policy-compliant browser actions together.
- **Bridging citations:** Pair with **Canary Tokens** for data-path observability and **SafeArena** for misuse, while keeping crawler governance, content provenance, and runtime containment as separate control layers.

### 16. Adjacent Baselines and Scope Boundaries

- **Claim scope:** Use sparingly to position web agents relative to general tool use, mobile GUI control, classical crawling, and specialized penetration testing.
- **Paper roles:** **Toolformer** and **Gorilla** are API/tool-use foundations; **AndroidWorld** is a dynamic mobile-GUI benchmark; **EvoCrawl** is a non-LLM evolutionary crawler; **AWE** is a specialized web penetration-testing system; **Toward Secure LLM Agents** supplies cross-domain security context.
- **Evidence anchors:** AndroidWorld's 30.6% best-agent versus 80.0% human result demonstrates a GUI reliability gap, not web-browser performance. EvoCrawl's stateful search and AWE's procedure-guided specialization provide meaningful design contrasts to open-ended LLM navigation.
- **Boundaries/non-comparability:** These papers should not be described as general browser-agent benchmarks. Their relevance is methodological: state-based verification, structured actions, documentation retrieval, stateful exploration, specialization, and containment.
- **Bridging citations:** Cite the specific web-native counterpart: **BrowserGym/WebArena** for AndroidWorld, **YURASCANNER** for EvoCrawl/AWE, and **ReAct** for Toolformer/Gorilla.

## Recommended Reading Paths

Each path moves from framing to representative systems, then evaluation and limitations. Read the cited summaries alongside the papers; ordering does not imply chronology or quality.

### General Web-Agent Path

1. **ReAct** — the reasoning/action loop.
2. **WebGPT** — browsing, evidence, human feedback, and citation risks.
3. **WebShop** — grounded interactive tasks and state-based success.
4. **Mind2Web** — cross-website data and candidate-based action selection.
5. **WebArena** — reproducible realistic execution and the human-agent gap.
6. **SeeAct** — planning-versus-grounding diagnosis.
7. **WebVoyager** — end-to-end multimodal live-web operation.
8. **VisualWebArena** — controlled visual evaluation.
9. **BrowserGym** — unified infrastructure and reproducibility.
10. **WebLINX** — conversational assistance and supervised specialization.
11. **MMInA** — multihop, multimodal, cross-site tasks.
12. **BEARCUBS** — current real-web computer-use breadth.
13. **Toward Secure LLM Agents** — authority, lifecycle, and unresolved safety stack.

### Security Path

1. **Not What You've Signed Up For** — practical indirect-injection threat model.
2. **Formalizing and Benchmarking Prompt Injection** — formalism, attacks, and defense baselines.
3. **WASP** — web-agent intermediate versus end-to-end compromise.
4. **Overcoming the Retrieval Barrier** — getting poisoned content retrieved.
5. **When AI Meets the Web** — plugin trust-boundary failures in deployed ecosystems.
6. **WARD** — evaluated web-observation guard and adaptive attacks.
7. **RENNERVATE** — attention-based span detection/removal.
8. **ACE** — architectural trust separation and containment.
9. **SafeArena** — malicious-user action requests and decomposition.
10. **ST-WebAgentBench** — enterprise policy compliance and escalation.
11. **Unsafe LLM-Based Search** — malicious source exposure and mitigation.
12. **SearchGEO**, then **FORGE** — consensus and recommendation manipulation without conflating them with instruction injection.
13. **ToolHijacker**, then **SkillTrojan**, then **BackdoorAgent** — tool metadata, executable skills, and trajectory backdoors.
14. **Toward Secure LLM Agents** — synthesize the layers into a lifecycle/security-stack agenda.

### Crawling and Extraction Path

1. **EvoCrawl** — non-LLM stateful exploration baseline.
2. **LASER** — explicit state-space constraints for navigation.
3. **WebWalker** — vertical traversal and the search/traversal distinction.
4. **Go-Browse** — structured exploration for data generation.
5. **YURASCANNER** — task-driven security crawling and complementary coverage.
6. **AWE** — specialized adaptive penetration testing and efficiency/coverage tradeoffs.
7. **AutoScraper** — reusable extractor synthesis.
8. **Webscraper** — interactive index-content extraction with parsing/merge tools.
9. **Canary Tokens** — crawler attribution, indirect collection, and limits of post-collection control.
10. **When AI Meets the Web** — security consequences of ingesting untrusted scraped content.

### Benchmark and Evaluation Path

1. **WebShop** — controlled environment and graded shopping success.
2. **Mind2Web** — offline action data and cross-domain splits.
3. **WebArena** — self-hosted, state-verified realistic tasks.
4. **VisualWebArena** — visual extensions under controlled hosting.
5. **BrowserGym** — common interfaces, experiment tooling, and integrated suites.
6. **WorkArena**, then **WorkArena++** — simple enterprise tasks to compositional L3 tasks.
7. **MMInA** — cross-site multimodal execution.
8. **WebWalker** — depth/source-controlled traversal.
9. **BrowseComp** — difficult short-answer browsing and test-time compute.
10. **Mind2Web 2** — long-form requirements and citation-aware agent judging.
11. **BEARCUBS** — live interactive and multimedia web use.
12. **AndroidWorld** — adjacent dynamic instantiation and state verification.
13. **WASP**, **SafeArena**, and **ST-WebAgentBench** — respectively injection, harmful requests, and policy compliance.
14. **SearchGEO** and **FORGE** — evidence pollution and endorsement/recommendation endpoints.
15. **BackdoorAgent** and **SkillTrojan** — trajectory and supply-chain endpoints; do not merge their metrics with web-task success.

### Training-Focused Path

1. **ReAct** — prompted reasoning/action baseline.
2. **WebShop** — imitation learning versus RL in a controlled environment.
3. **WebGPT** — demonstrations, reward modeling, RL, and rejection sampling.
4. **Mind2Web** and **WebLINX** — offline supervision at different interaction granularity.
5. **AutoWebGLM** — curriculum, error correction, and simulated environment practice.
6. **Go-Browse** — exploration-generated grounded tasks and successful trajectories.
7. **WebDancer** — synthetic data, supervised cold start, and RL for information seeking.
8. **WebSailor** — uncertainty-oriented task construction and RL.
9. **LASER** — structured state priors as an alternative/complement to more data.
10. **BrowseComp** — inference-time browsing effort and parallel sampling as a separate scaling axis.

### Enterprise Deployment Path

1. **WorkArena** — baseline enterprise UI capability and failure modes.
2. **BrowserGym** — reproducible execution and experiment operations.
3. **WorkArena++** — compositional workflows, memory, constraints, and infeasibility.
4. **WebLINX** — multi-turn human-agent interaction.
5. **ST-WebAgentBench** — policy-aware success, consent, and escalation.
6. **SafeArena** — malicious-user and request-decomposition risk.
7. **When AI Meets the Web** — third-party integration and message-role boundaries.
8. **ACE** — typed trusted planning, app selection, data-flow checks, and isolation.
9. **ToolHijacker** and **SkillTrojan** — third-party tool/skill supply-chain risk.
10. **BackdoorAgent** — persistent compromise across memory, planning, tools, and observations.
11. **WARD** and **RENNERVATE** — complementary observation-layer controls.
12. **Toward Secure LLM Agents** — defense-in-depth, auditability, revocation, least privilege, and remaining gaps.

## Complete Coverage Map (48/48)

The map gives each paper a primary home and selected bridges. Repeated membership is intentional; every citation should still match the sentence-level claim.

| # | Paper | Primary cluster | Important bridges |
|---:|---|---:|---|
| 1 | ACE | 11 | 9, 12, 15 |
| 2 | AndroidWorld | 3 | 4, 16 |
| 3 | AutoScraper | 8 | 7 |
| 4 | AutoWebGLM | 2 | 6 |
| 5 | AWE | 7 | 16 |
| 6 | BackdoorAgent | 14 | 15 |
| 7 | BEARCUBS | 4 | 5, 12 |
| 8 | BrowseComp | 5 | 6 |
| 9 | BrowserGym | 3 | 9 |
| 10 | Canary Tokens | 8 | 15 |
| 11 | EvoCrawl | 7 | 16 |
| 12 | FORGE | 13 | 5 |
| 13 | Formalizing and Benchmarking Prompt Injection | 10 | 11 |
| 14 | Go-Browse | 6 | 7 |
| 15 | Gorilla | 1 | 14, 16 |
| 16 | Not What You've Signed Up For (indirect prompt injection in the real world) | 10 | 15 |
| 17 | LASER | 6 | 7 |
| 18 | Mind2Web 2 | 5 | 4 |
| 19 | Mind2Web | 2 | 3, 6 |
| 20 | MMInA | 4 | 5 |
| 21 | Overcoming the Retrieval Barrier | 10 | 11, 13, 14 |
| 22 | ReAct | 1 | 2, 6 |
| 23 | RENNERVATE | 11 | 15 |
| 24 | SafeArena | 12 | 9, 15 |
| 25 | SearchGEO | 13 | 5 |
| 26 | SeeAct | 2 | 4 |
| 27 | SkillTrojan | 14 | 15 |
| 28 | ST-WebAgentBench | 9 | 12, 15 |
| 29 | Toolformer | 1 | 14, 16 |
| 30 | ToolHijacker | 14 | 10, 15 |
| 31 | Toward Secure LLM Agents | 15 | 10–14, 16 |
| 32 | Unsafe LLM-Based Search | 12 | 11, 13 |
| 33 | VisualWebArena | 4 | 3 |
| 34 | WARD | 11 | 10, 15 |
| 35 | WASP | 10 | 11 |
| 36 | WebArena | 3 | 2, 9, 12 |
| 37 | WebDancer | 6 | 5 |
| 38 | WebGPT | 1 | 5, 6, 13 |
| 39 | WebLINX | 2 | 6, 9 |
| 40 | WebSailor | 6 | 5 |
| 41 | Webscraper | 8 | 7 |
| 42 | WebShop | 1 | 3, 6 |
| 43 | WebVoyager | 2 | 4 |
| 44 | WebWalker | 5 | 7 |
| 45 | When AI Meets the Web | 10 | 8, 11, 15 |
| 46 | WorkArena | 9 | 3 |
| 47 | WorkArena++ | 9 | 3, 12 |
| 48 | YURASCANNER | 7 | 16 |

## Using the Clusters in Related Work

Start each paragraph with the claim, then cite papers by role. A useful pattern is: one foundational or capability paper, one benchmark that operationalizes the claim, one evidence anchor, one boundary sentence, and one bridging citation that exposes the gap. Avoid bundles that silently imply equivalence—for example, do not group SafeArena, WASP, WARD, and SearchGEO as four versions of the same “security benchmark.” They respectively evaluate malicious-user compliance, indirect prompt injection, an evaluated injection defense, and source-consensus manipulation.

When reporting a number, name its benchmark and endpoint (for example, task success, ASR-intermediate, ASR-end-to-end, policy-compliant success, retrieval top-*k*, recommendation rate, or detection accuracy). When discussing live-web systems, state that sites and retrieval results are mutable. When discussing a defense, report utility and threat-model exclusions alongside attack reduction. These practices preserve the distinctions needed for a defensible related-work narrative.
