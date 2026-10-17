# AI web-agent trap research roadmap

**Research proposal for human review — 2026-10-16.** No trap, benchmark, agent or experiment has been implemented or run for this roadmap. Numerical pilot quantities are proposed limits, not results. External search cutoff: material available by **16 October 2026**, not the remainder of the month.

## 1. Restored objective and recommendation

The project should investigate **how a hostile website can retain an autonomous web agent through the agent's pursuit of a legitimate user goal**. The primary object is sustained, unproductive interaction with an adversarial environment, including the ability to recognize the problem, leave and recover. A successful prompt injection, a single redirected click, a failed task and prolonged retention are different observations.

**Working research question:** How can adversarial web environments induce and sustain task-dependent navigation traps in autonomous AI web agents, and what determines whether agents escape, recover, or continue unproductive interaction?

**Initial operational question:** Under a page-only adversary with access to public task context, does making a recurring prerequisite appear relevant to the user's goal increase bounded non-progress interaction and reduce successful recovery, compared with the same navigation structure carrying neutral content? The working question is not a fixed publication title.

**Leading mechanism:** semantic, task-dependent trapping through a recurring verification/dependency workflow. Resource consumption and failure to escape are measured consequences. Start with one browser agent and deterministic local pages; persistent memory, adversarial adaptation and delegation are later questions.

**Novelty assessment: unresolved and substantially constrained.** Broad claims of the first AI-agent trap, semantic trap, deceptive prerequisite, navigational loop or agent-retaining honeypot are not defensible from the reviewed literature. Sections 3–4 identify implemented competitors. A potentially useful contribution is a controlled study that separates task semantics from page topology, measures retention and recovery with independent progress ground truth, and tests a bounded escape intervention. That combination is a research hypothesis about a contribution, not an established gap or a demonstrated attack.

The standalone-LLM comparison becomes an optional explanation of individual decisions. It is not the organizing contribution or a required baseline for longitudinal trapping.

## 2. Evidence basis, scope and provenance

The current [Research Mode handoff](../../docs/RESEARCH_MODE_HANDOFF.md) records 112 completed canonical papers, with no pending, excluded or failed/deferred entries. Former holdout reservations were retired for ordinary research; historical scientific states are not reinterpreted. This roadmap does not alter that state or any source identity.

The synthesis basis comprises the [comprehensive review](COMPREHENSIVE_LITERATURE_REVIEW.md), [thematic evidence map](THEMATIC_EVIDENCE_MAP.md), [research gaps](RESEARCH_GAPS_AND_HYPOTHESES.md), [controlled comparison design](CONTROLLED_COMPARISON_STUDY_DESIGN.md), [security comparison reference](SECURITY_COMPARISON_MATRIX.md), [initial findings](INITIAL_RESEARCH_FINDINGS.md) and [consolidation report](CONSOLIDATION_REPORT.md). Their active framing is synchronized to this trap-oriented proposal. The earlier comparison study retains its methodology as a secondary proposal; pre-synchronization versions and completed operational reports preserve history.

Relevant original summaries and structured records were consulted for mechanisms, attacker privileges, endpoints and limitations. Local citations below resolve to unchanged records containing typed claims, physical PDF page locators and source fingerprints; corresponding summaries are indexed in the [catalog](../catalog.md). New external discoveries are supplemental related work, not additional completed corpus records.

**Evidence language:** “reported” or “demonstrated” describes the authors' study under its protocol, not reproduction here. “Observed” in this document means inspected publication text or local artifacts, not observed victim behavior. “Interpretation” identifies analytical conclusions. “Proposed” and “hypothesis” identify untested designs. No model agreement substitutes for independent scientific validation.

### External search and its limits

Targeted academic and primary-publication searches covered AI-agent crawler traps, semantic navigation loops, task-dependent progress deception, stateful adversarial environments, agentic honeypots, navigation deadlocks, resource exhaustion, deceptive verification and adaptive task redirection. Representative executed queries included:

- `"AI agent" "crawler traps" semantic`; `"web agents" "tarpit" paper`.
- `"semantic navigation" "trap" agents`; `"web agents" "deadlock" adversarial`.
- `"task-dependent" "traps" web agents`; `"web agents" "progress deception"`.
- `"agentic honeypots" paper`; `Honeyval honeypots agent interaction`.
- `LoginTrap paper arxiv`; `"web agents" "verification" "infinite" attack`.
- Exact-title searches for AI Agent Traps, both TRAP studies and adversarial-environment work.

Search leads were followed to arXiv methods, official proceedings and original implementation documentation. Primary methods were inspected for Honeyval, LoginTrap, POTEMKIN, AGENTBAIT, the Telephone Loop study and visual-preference TRAP. The PMLR page verifies the identity/publication of It's a TRAP!; the external PDF fetch failed, so its detailed methods are grounded in the existing local source record and summary rather than a claimed new PDF inspection. No linked repository was executed, installed or independently reproduced. Nepenthes documentation was read without entering its trap.

This is a targeted novelty assessment, not a preregistered systematic review or proof of absence. Search rankings, preprint revisions, terminology and unpublished implementations can hide closer competitors. Version-specific dates are used below; live software documentation without a verified release date is weaker evidence for chronology. Broad “agentic honeypot” results often describe an AI defender managing decoys, not an autonomous AI visitor being trapped. Embodied navigation, human scam conversations and model-training crawlers do not automatically answer this web-agent question.

## 3. Competing work: what actually exists

### 3.1 Classical traps and deployed crawler decoys

**Traditional crawler-trap research.** The local [crawler-trap detection record](../records/detection_of_crawler_traps_formalization_and_implementation_defeating_protection_on_internet_and_on_the_tor_network_comprehensive_summary.json), claims C01–C14, physical pp.1–12, studies page-distribution comparisons across 13 families with 500 pages per family. It proposes dynamic detection, but the reported overlap study is not operational evidence that a deployed detector prevents loops. Classical traps exploit URL proliferation, repeated content, redirection, branching or delays. The analogy supplies navigation/resource mechanisms, not an LLM-specific result. [IRLbot](../records/irlbot_scaling_to_6_billion_pagesand_beyond_comprehensive_summary.json), physical pp.3–32, supplies crawl scheduling and branching context.

**Nepenthes — implementation documentation, not a controlled AI-agent study.** The author's documentation describes generated linked pages, Markov text, configurable delay and redirect behavior. Reported user-agent strings and request statistics do not establish autonomous goal-directed LLM visitors or their task progress. Treat it as a concrete classical tarpit reference; documentation revision chronology was not independently established. [Original documentation](https://zadzmo.org/code/nepenthes/), features/configuration/history.

**Cloudflare AI Labyrinth — official deployment account.** The account describes pre-generated irrelevant content linked through pages, with hidden links offered to suspected scrapers, and a detection role. This is substantial prior implementation of AI-branded crawler deception. It does not provide the matched goal-directed browser-agent experiment proposed here. Its use of generative content is not evidence that the trapped clients themselves reason with LLMs. [Official description](https://blog.cloudflare.com/ai-labyrinth/), “How we built the labyrinth” and “AI honeypots, created by AI.”

### 3.2 Agent navigation and retention: closest competitors

**POTEMKIN / How Adversarial Environments Mislead Agentic AI? — implemented evaluation.** Compromised tool responses create phantom citation structures, including cycles/dead ends; the Maze experiments manipulate cycle length and plausibility and distinguish entry from wasted retrieval effort. This already studies agent navigation traps. Its citation-graph tool setting differs from a page-only browser workflow, but that domain difference alone is a weak novelty argument. The local record also qualifies engagement-conditioned results and supplementary inconsistencies. [Primary v1](https://arxiv.org/html/2604.18874v1), §§3–4 and supplementary failure taxonomy; [local record](../records/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.json), C01–C16, physical pp.2–17. Do not equate all depth failures with repeated loops: the local C15 taxonomy separates loops, dead ends and authority cascades.

**Honeyval — implemented HTTP-honeypot evaluation, preprint v1, 28 May 2026.** Sixteen backend applications ground interactions between LLM-powered decoys and AI hacking agents. Secure/insecure real implementations and honeypot functional tests supply controls. Metrics include HTTP interaction length, detection and cost; prompt customizations alter deception/engagement. This is direct prior art for retaining goal-directed AI visitors, not merely a taxonomy. The distinction available to this project is a legitimate-user browser task, page-only semantic/topological controls and recovery with a reachable goal—not the general idea of keeping an AI agent engaged. [Primary methods](https://arxiv.org/html/2605.29963v1), §§4–5 and prompt-customization tables. No independent reproduction was performed.

**Telephone Loop / From Monoliths to Swarms — implemented local web study, v1 dated 31 July 2026.** A web-only adversary uses staged verification and disclosed role metadata to induce circular delegation. The reported endpoint includes an unresolved tool-call crash, not simply long browser dwell. The paper compares single/multi-agent architectures and reports 144 multi-agent Telephone Loop trials; its endpoint/denominators must remain separate from retention. This directly threatens novelty claims about task prerequisites, multi-stage verification and delegation loops. [Primary methods](https://arxiv.org/html/2608.00202v1), §§IV, V-A3 and VI-C. Choosing a single browser agent avoids this particular delegation mechanism but does not establish originality.

### 3.3 Persuasion, prerequisites and progress pretexts

**It's a TRAP! — empirical browser persuasion benchmark.** Its main dataset combines 18 tasks and 35 templates, giving 630 combinations per principal model and 3,780 attacked runs across six models. The central endpoint is initial clicked redirection; its Figure 15 already illustrates chained continuation. Therefore, “prior TRAP only considers one step” is inaccurate, even though it does not quantify sustained retention as its main outcome. [Local record](../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json), trap_claim_01/02/03/12, physical pp.3–8,13–14; [summary, Figure 15 discussion](../summaries/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.md); [official ICML 2026 publication](https://proceedings.mlr.press/v306/korgul26a.html). Task tailoring and clickable affordances are already studied mechanisms.

**LoginTrap — implemented phishing-style browser study, preprint v1, 5 August 2026.** Cloned pages carry a login-inducing popup and an attacker-controlled login flow; page-context-based generation does not assume knowledge of the user's task or agent internals. Authentication is presented as a prerequisite, and sensitive-field filling/submission is the specified success path. This is direct prior art for deceptive prerequisites with weaker task knowledge than a fully task-aware attacker. It does not make repeated retention and recovery its primary endpoint. The abstract's aggregate percentage is intentionally not used as a retention estimate. [Primary methods](https://arxiv.org/html/2608.04741v1), §§2.4–3.4.

**AGENTBAIT / When Bots Take the Bait — empirical social-engineering study, v1, 12 January 2026.** The method couples user background/goal with page inducement/attacker objective; it tests five browser-agent frameworks with GPT-4o and constructs 100 input quadruples. Context integration explicitly includes finalization and re-verification pretexts. Thus plausible continuation and verification deception are not new mechanisms by themselves. These findings concern induced unsafe behavior; they are not a measured retention/escape experiment. [Primary text](https://arxiv.org/html/2601.07263v1), §III, Tables I–II and §IV-A.

**WASP — empirical browser-security benchmark.** Contributor-level issues/posts/comments, task-related pretexts and URL-fragment persistence already connect apparent task assistance to later attacker-directed actions. Intermediate compromise and goal-specific final-state ASR differ; neither can be silently converted into trap retention. Its contributor privileges are narrower than full website ownership. [Local record](../records/wasp_comprehensive_summary.json), wasp_c01–wasp_c16, physical pp.3–22.

**TRAP: Targeted Redirecting of Agentic Preferences — a different study.** Its diffusion-based semantic image edits bias multi-candidate VLM choices; the original evaluation uses COCO-derived decision scenarios. This is implemented preference manipulation, not evidence of a recurring web workflow. It threatens broad semantic-manipulation novelty, but cannot supply browser-retention rates. Keep it distinct from Korgul and colleagues' persuasion benchmark. [Primary v1](https://arxiv.org/html/2505.23518v1), methodology/evaluation; [official NeurIPS 2025 publication](https://papers.nips.cc/paper_files/paper/2025/hash/f7bf351cd45a377901780e90a4bc0897-Abstract-Conference.html).

### 3.4 Long-horizon, resource and persistent-state evidence

| Work and evidence status | Demonstrated access/method and endpoint | Constraint on this proposal |
|---|---|---|
| [AI Agent Traps](../records/ai_agent_traps_comprehensive_summary.json), C01–C03/C14, physical pp.1–4,14 | Conceptual architecture-based taxonomy and synthesis; overlapping functional targets, uneven empirical maturity. | The broad trap concept and functional framing are established. Its scenarios are not all independently implemented experiments. |
| [AgentLAB](../records/agentlab_benchmarking_llm_agents_against_long_horizon_attacks_comprehensive_summary.json), physical pp.1–19 | Implemented long-horizon benchmark with adaptive bridge actions, multiple attack families and two-phase memory poisoning. Some settings expose trajectories/reasoning to the attacker. | Long-horizon composition and adaptation already exist. Success-conditioned turns and unequal search budgets do not estimate unbiased retention or a causal horizon effect. |
| [Breaking Agents](../records/breaking_agents_compromising_autonomous_llm_agents_through_malfunction_amplification_comprehensive_summary.json), C01–C14, physical pp.1–13 | Emulator plus implemented Gmail/CSV agents; loop and incorrect-function attacks, with failed-task ASR assessed by self-reflection. | Repetition-induced malfunction is prior art. Failure is not proof of continued captivity, completed malicious action or an observed resource bill. |
| [Overthinking Loops](../records/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.json), C01/C02/C07, physical pp.1–5 | Fourteen malicious tools induce repetition, refinement and distraction through registry/tool interactions; normal/mixed configurations, tokens and runtime. | Repeated validation/refinement is demonstrated under stronger component privileges than page content. Porting wording to HTML alone is not a convincing contribution. |
| [Beyond Max Tokens](../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json), C01–C04/C15, physical pp.3–4,13 | Tool-server progression/validation/termination chains and localized search; controlled emulator and per-generation caps. | Fake progress and chained resource amplification are close mechanisms. Preserve call-cap protocols; aggregate trajectory length does not violate a per-generation token cap. |
| [AgentDoS](../records/autonomy_comes_with_costs_detecting_denial_of_service_vulnerabilities_caused_by_resource_abusing_in_llm_based_agents_comprehensive_summary.json), C01–C13, physical pp.4–15 | Source-informed grey-box fuzzing of resource sinks and lifecycle-dependent memory/disk exhaustion. | Resource sinks are not the same as semantic browser retention; source/runtime knowledge cannot enter the page-only threat model unnoticed. |
| [IAL-SCAN](../records/when_agents_do_not_stop_uncovering_infinite_agentic_loops_in_llm_agents_comprehensive_summary.json), IAL_C01–IAL_C14, physical pp.2–10 | Static analysis and confirmation of potential agentic loop defects. | A code-level loop alert is not measured adversarial entry, dwell or recovery. |
| [Context Manipulation](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json), C01–C14, physical pp.4–8 | Direct plan/history corruption and context-aligned attacks on browser agents. | Direct internal-state editing is a separate attacker privilege, not evidence that a webpage naturally poisoned memory. |
| [Hidden in Memory](../records/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.json), C01/C05/C06/C11, physical pp.3–4,14,23,44 | Environmental memory acquisition plus downstream stored-memory uptake; some standardized tests directly provide saved content. | Separate writing, survival, retrieval and use. Broad uptake includes weaker outcomes than independently verified harmful execution. |
| [RecurGuard](../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json), C01–C14, physical pp.2–14 | Runtime monitoring/cancellation of exposed reasoning with adaptive residual costs. | Useful resource-defense reference; hidden reasoning and cancellation interfaces limit transfer. |

Adjacent external work also requires care. [Towards Agentic Honeynet Configuration](https://arxiv.org/abs/2603.14122), v1, 14 March 2026, describes an AI defender adjusting honeypot exposure in simulated exploit scenarios. This is not itself a demonstration that legitimate browser agents remain trapped. [Simulacrum](https://repository.tudelft.nl/record/uuid%3Ada0ed2f1-ca41-43f1-bcd9-a8c17f0ddbac), TU Delft thesis, 2026, describes coherent resource generation for web honeypots; only its repository abstract was inspected here, so it remains an unresolved methods-level novelty lead rather than a verified comparator. These sources prevent assuming that stateful or generated decoys are new, without overstating their relevance.

### 3.5 What can and cannot be claimed

The closest competition covers navigation topology, AI engagement, task prerequisites, progress-like tool chains and staged browser/delegation attacks. **Changing the word “injection” to “trap,” moving an existing chain to a webpage, or adding token counts is insufficient novelty.** A retention study would need a sharper causal question and useful, independently observable outcomes.

Potentially distinctive, subject to further methods/artifact review: isolate the interaction between task relevance and recurrence on reachable browser tasks; quantify progress-free work and recovery rather than just redirection; compare escape behavior under identical information and privileges; evaluate a simple termination rule against legitimate iterative workflows. None of these components is claimed individually new. The scientific value must come from what the controlled combination explains beyond the competitors.

### External-reference verification — 2026-10-16

Primary publication/author pages were checked for the following identities and dates during synchronization. This is a bounded metadata refresh, not a second systematic review or fresh reproduction of prior methods. The detailed methods descriptions above retain their original local/primary-source basis. Supplemental external items remain outside the canonical 112; POTEMKIN and It's a TRAP! already have local records and are not counted again.

| Work | Verified bibliographic identity / status | Relation to canonical corpus |
|---|---|---|
| [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/abs/2604.18874v1) | Zhonghao Zhan and coauthors; arXiv:2604.18874v1, 20 April 2026; arXiv comments report Findings ACL 2026 acceptance. | Existing local POTEMKIN record; preprint/publication evidence remains version-specific. |
| [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://proceedings.mlr.press/v306/korgul26a.html) | Karolina Korgul and coauthors; ICML 2026, PMLR 306:60284–60300. | Existing canonical record; publication metadata does not change its supplied-PDF identity. |
| [Trapping misbehaving bots in an AI Labyrinth](https://blog.cloudflare.com/ai-labyrinth/) | Reid Tatoris, Harsh Saxena and Luis Miglietti; Cloudflare, 19 March 2025. | Supplemental official deployment account; no controlled goal-driven-agent result inferred. |
| [Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots](https://arxiv.org/abs/2605.29963v1) | Mark Vero and coauthors; arXiv:2605.29963v1, 28 May 2026. | Supplemental preprint; HTTP hacking-agent setting differs from legitimate browser tasks. |
| [LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](https://arxiv.org/abs/2608.04741v1) | Longtao Guo, Zelin Zhang, Kaifeng Huang and Yang Shi; arXiv:2608.04741v1, 5 August 2026. | Supplemental preprint; no retention rate inferred from phishing outcomes. |
| [When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent](https://arxiv.org/abs/2601.07263v1) | Xinyi Wu and coauthors; arXiv:2601.07263v1, 12 January 2026; AGENTBAIT method. | Supplemental preprint; contextual inducement is existing work. |
| [From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems](https://arxiv.org/abs/2608.00202v1) | Yashaswi Malla and Sandra Siby; arXiv:2608.00202v1, 31 July 2026; Telephone Loop mechanism. | Supplemental preprint; architectural/delegation failures are not a standalone-LLM contrast. |
| [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](https://arxiv.org/abs/2606.15673v2) | Jiwan Chung, JiHyuk Byun, Vibhav Vineet and Seon Joo Kim; arXiv:2606.15673, v1 8 April / v2 4 August 2026; journal reference COLM 2026. | Supplemental WebStep evaluation work; semantic-state observation has precedent and is not an attack novelty. |

WebStep's v2 abstract reports different performance examples from the [project-page summary](https://jiwanchung.github.io/webstep/). No numerical result is pooled or silently reconciled here. The methodological point is independently tracked semantic transitions; exact benchmark results require version-specific citation. Author/project pages do not establish artifact availability or independent replication. Classical crawling remains grounded in the unchanged local records cited above; no new external paper was added to the register.

## 4. Trap model and operational definitions

Let the legitimate task be `T=(G,A,U)`: a server-verifiable goal predicate `G`, authorized actions `A`, and trusted user constraints `U`. A running agent policy selects `a_t` from its observation `o_t`, task and internal state `m_t`. The browser/server state `x_t` changes through a transition function; the adversary changes only its declared portion of that environment. A page statement that progress occurred is an observation, not the goal oracle.

### 4.1 Primary threat model

| Element | Proposed definition |
|---|---|
| Legitimate task | Retrieve a specified synthetic document or complete a small local information workflow. The valid result exists and is reachable without following the decoy indefinitely. No purchase, credentials or real account required. |
| Adversarial surface | One designated site and its page text, links, forms and bounded session transitions; entry page may present a misleading verification workflow. This is site-owner control, not merely a third-party comment. |
| Attacker knowledge | Public site/task category and object identifiers revealed by ordinary navigation; no private user prompt, hidden reasoning, model weights, private memories or future actions. Task-blind and full-task-known attacks are separate extensions. |
| Control limits | No trusted instructions, browser chrome, tool definitions, executor, goal oracle, network outside the sandbox or operating-system resources. Attacker content cannot change the evaluator's ground truth. |
| Observation | Primary DOM/accessibility representation, with exact preprocessing recorded. Page, current URL and ordinary browser feedback are available consistently. Visual/bimodal interfaces are later matched strata. |
| Actions | Click, type synthetic values, scroll, back, navigate within allowed origins, stop and return a result. Agents retain a usable exit and can return to the legitimate route. No shell or arbitrary network tool in the primary comparison. |
| Internal state | Current plan, interaction history and working context. Cross-session persistent memory is disabled initially; an architecture's within-run history is still state and must be described. |
| External state | Browser URL/history, local cookies/session and deterministic page workflow state. Ground-truth task state and logs remain outside attacker control. |
| Entry | Exposure means observing the designated page region; behavioral entry means the first chosen action initiating the decoy workflow. Record both; do not infer exposure from page delivery alone. |
| Retention | Continued decoy-directed choices without a verified new legitimate subgoal, despite an available exit. Semantic recurrence may occur at different URLs and text, so URL repetition alone is insufficient. |
| Escape | Leaving the decoy workflow for the legitimate route, or explicitly stopping and notifying the user. Report these separately; browser navigation outside a region is not necessarily recovery. |
| Recovery | After behavioral entry, completing the original authorized task within the remaining budget. A safe stop is successful containment but not task completion. |

**Mechanism hypothesis:** a page presents a goal-relevant prerequisite; the agent follows it; the website supplies apparent partial progress plus a revised prerequisite; the agent continues because the new step seems necessary for the original task. The tested trust crossing is promotion of untrusted workflow claims into planning authority. This description does not imply access to hidden cognition: explanations from traces are evidence about observable plans, not proof of an internal psychological cause.

An abstract local example is a document retrieval workflow alternating “prepare result” and “verify result readiness,” while the requested document remains accessible through an ordinary exit route. The evaluator knows that neither repeated check advances the legitimate task. This is a proposed fixture, not a deployed payload or evidence it works.

### 4.2 Outcomes and failures

Define a verified progress function `P(x_t)` using meaningful task subgoals and final `G`, not the website's displayed percentage. Repeating an already completed subgoal adds no progress. Necessary exploration may have no immediate progress; it becomes evidence of trapping only through prespecified decoy membership, recurrence and controlled excess relative to benign conditions.

A proposed descriptive trap event is behavioral entry followed by at least three decoy-directed decisions without verified new progress. This threshold is a planning choice; select it before evaluation and show sensitivity at two and five decisions. It is not a universal security definition. The primary analysis uses continuous bounded wasted-work outcomes rather than relying on this one threshold.

Classify terminal states separately: goal completed; escaped and recovered; safe stop without goal; still in decoy at budget cap; unrelated task failure; browser/tool defect; provider interruption; or agent crash. A finite capped trajectory cannot prove an infinite loop. A crash can be an availability effect, but cannot be recorded as long retention after execution has ceased. API errors and unobserved outcomes remain operationally missing, not robust or compromised by assumption.

The attacker objective is excess non-progress interaction and/or preventable loss of authorized utility under fixed budgets. **Evidence of success requires more than a failed task:** the trajectory must support the specified mechanism, and the matched comparison must separate it from ordinary difficulty. At the study level, a null effect or benign-equivalent effect refutes the proposed semantic-retention explanation in that setting.

### 4.3 Privilege tiers kept separate

| Tier | Access | Role |
|---|---|---|
| Contributor | One comment/review/document field; no site transition control. | Lower-privilege transfer extension, informed by WASP/TRAP. |
| Site owner, public task context | Page content and bounded site workflow; public request context only. | Primary proposal. |
| Site owner, full user task | Above plus private task knowledge supplied to attack author. | Explicit upper-bound/task-knowledge ablation; not pooled with primary. |
| Tool/runtime adversary | Tool metadata/results or tool registration. | Competitor comparison only initially; different access boundary. |
| Internal-state adversary | Direct plan/history/memory writes or compromised delegate. | Separate threat model; excluded from the primary trap claim. |

## 5. Six candidate mechanisms

### 5.1 Semantic navigation loops

**Mechanism:** goal-related links make revisiting equivalent states appear productive, even when URLs and wording differ. **Prior demonstration:** POTEMKIN already evaluates fabricated navigation structures; classical traps cover topology. **Possible originality:** quantify a task-semantics effect while holding the graph, link count, latency and reachable goal fixed. **Required experiment:** paired goal-relevant/neutral wording on the same graph, with verified task-state transitions and cycle-aware baselines. **Feasibility:** high for a small deterministic site. **Limits:** ordinary search needs revisits; repeated URLs are neither necessary nor sufficient. If neutral topology explains the result, the study is about navigation robustness rather than a semantic-specific trap.

### 5.2 Task-dependency traps — recommended primary

**Mechanism:** a supposed prerequisite repeatedly leads to another prerequisite, exploiting completion-oriented action selection. **Prior demonstration:** LoginTrap, WASP, task-tailored TRAP and Telephone Loop already use task-compatible preconditions; AgentLAB supplies adaptive bridge actions. **Possible originality:** isolate recurrence and recovery in a single-agent page-only setting under public rather than omniscient task knowledge. **Required experiment:** cyclic versus finite prerequisites, task-aligned versus neutral framing, an equally visible escape and independent goal reachability. **Feasibility:** high without adaptive generation. **Limits:** plausible prerequisites may be legitimately necessary; the ground-truth task specification must establish which are unnecessary. A simple new pretext is a weak contribution.

### 5.3 Misleading progress and verification

**Mechanism:** apparent partial completion makes another check or repair seem worthwhile, although legitimate state has not advanced. **Prior demonstration:** Beyond Max Tokens and Overthinking Loops already implement progression/refinement; AGENTBAIT and Telephone Loop include verification pretexts. **Possible originality:** distinguish displayed progress from actual progress and measure whether false progress increases persistence beyond the same dependency cycle. **Required experiment:** truthful/false/no-progress display with equal content volume and latency after the core mechanism is established. **Feasibility:** moderate; useful as the first secondary ablation. **Limits:** interface deception, recovery policy and task complexity may explain effects; adding this factor to the first pilot would dilute the primary question.

### 5.4 Persistent-state and memory traps

**Mechanism:** an agent stores a site's supposed prerequisite, later retrieves it and re-enters the decoy across sessions or tasks. **Prior demonstration:** Hidden in Memory, Context Manipulation, WASP and AgentLAB cover distinct carriers/acquisition privileges. **Possible originality:** measure re-entry and recovery after an observed natural memory write, not merely compliance with a preloaded poisoned memory. **Required experiment:** acquisition → verified write → reset → retrieval → action → legitimate recovery, including clean useful memories and correction/deletion controls. **Feasibility:** moderate/low; requires a defined memory lifecycle. **Limits:** direct edits cannot establish environmental poisoning; conditioning on successful writes selects a susceptible subset. Defer until the within-run mechanism is useful.

### 5.5 Resource-consumption traps

**Mechanism:** unnecessary actions, verbose processing or repeated checks consume bounded inference/browser resources. **Prior demonstration:** resource amplification, malfunction loops, source-informed AgentDoS and classical delays already exist. **Possible originality:** attribute excess resources specifically to semantic retention after controlling response size, induced latency and topology. **Required experiment:** paired absolute token/action/time differences, with task utility and clean iterative tasks; independently label computation, server delay and operational failures. **Feasibility:** high as outcomes of the primary study. **Limits:** large ratios with tiny clean denominators mislead; projected financial harm is not an observed bill. Avoid developing a separate resource-exhaustion attack for the pilot.

### 5.6 Hybrid or adaptive multi-stage traps

**Mechanism:** the site changes its next pretext after public actions, combining entry persuasion, dependencies and later persistence. **Prior demonstration:** AgentLAB, chained TRAP illustrations, adaptive tool-chain search and Telephone Loop undermine general compositional novelty. **Possible originality:** estimate adaptation's incremental effect at equal attacker query/length budgets and public observations. **Required experiment:** fixed versus adaptive policy, held-out task/site families and separate development/evaluation budgets. **Feasibility:** lower; generalization and leakage controls become harder. **Limits:** unequal optimization opportunity can masquerade as an adaptive advantage. Defer dynamic attackers and multi-agent delegation; do not build an orchestrator.

## 6. Comparative evaluation and identifiable claims

### 6.1 Comparators have different jobs

| Comparator | Fair question | Necessary controls and interpretive limit |
|---|---|---|
| Classical bounded crawler | Does graph structure alone create unnecessary traversal? | Same rendered link graph, discovery start and request cap; report coverage, repeat visits and target-resource discovery. A crawler cannot be scored as failing a natural-language user task it cannot represent. |
| Cycle-aware crawler | Does URL/content/state deduplication explain apparent robustness? | Record canonicalization and visited-state rules. Give no private trap-state oracle. Semantic equivalence unavailable to ordinary crawlers cannot be supplied for free. |
| Rule-based task navigator | Can explicit progress/retry logic avoid the workflow? | Use public task fields and visible site cues; same browser actions/goal access. Hand-coded site knowledge is labeled, with clean utility shown. This is an engineering baseline, not a capacity-matched language model. |
| Reactive LLM browser agent | How does a simple observe–act loop respond? | Primary architecture; pin model, prompt, observations, tools, budgets and reset behavior. |
| Planner/executor browser agent | Does structured planning/recovery change the effect? | Same model family, task facts and observation/action interface where feasible. Count all planning/verification calls. Different prompts and call allocation make this a configured-system comparison. |
| Different model families | Does the mechanism transfer across backbones? | Hold scaffold fixed; report exact versions and settings at execution. Avoid ranking model families from one task set or unequal reasoning/cost allowance. |
| Memory on/off | Does retained state increase re-entry or improve escape? | Later randomized extension with identical initial histories; separate within-run history from persistent storage and natural writes from direct writes. |
| DOM, screenshot and combined observation | Is the trap seen and acted upon through each interface? | Later strata with rendered semantics/layout held as close as possible; log visibility, OCR/accessibility filtering and action grounding. Equal source HTML does not ensure equal exposure. |
| Standalone decision replay | Does the same page claim change a single proposed next action? | Optional supporting test with matched task/content and common action choices; no real browser execution. It cannot measure retention or recovery without an interaction loop. |

Classical and rule-based systems provide structural/mechanistic references, not a single universal susceptibility leaderboard. Agent architecture, backbone, memory and modality should be varied in stages rather than crossed into an enormous initial benchmark. In particular, a multi-agent web system and a standalone LLM are different comparator questions; the new Telephone Loop work does not answer the old standalone-versus-agent question.

### 6.2 Controls against ordinary failure

All paired site versions retain the same legitimate task and authorized outcome, a demonstrably reachable goal, a usable exit, equal entry opportunity and comparable legitimate-route difficulty. Validate reachability manually and through a simple reference path before any future victim runs; this is a proposed check, not one executed now. Include an ordinary finite workflow that genuinely requires several steps, so an agent that refuses all verification is not rewarded as secure.

Within each topology, task-aligned and neutral versions share links, element positions, response length range, page count, delays, public object facts and available actions. The treatment changes the claimed relation of the workflow to the task; it must not remove the target object, expose an answer only in one arm or make one exit visibly easier. Record residual differences. Across cyclic/finite topology, change only the declared transition relation as far as possible; repeated observations necessarily differ, so the semantic contrast within topology is the cleaner identification.

Neutral framing should remain readable and comparable in plausibility, without conveying that the procedure is a prerequisite for the current task. Otherwise “task alignment” becomes an obvious nonsense-versus-realistic comparison. A separate clean legitimate workflow verifies baseline solvability; retain all randomized tasks in analysis, even when an agent fails its clean counterpart. A development-only feasibility screen may establish that a task is usable, but evaluation tasks cannot be dropped after seeing treatment outcomes.

Keep network delay fixed and small in the primary study; slow-server waiting is a classical tarpit effect. Keep token/character volume comparable to avoid substituting long-context overload for semantic retention. Browser back and direct allowed navigation remain usable. The hostile site cannot disable all exits, remove the goal, invalidate the evaluator or create an objectively impossible task and then count noncompletion as policy-induced trapping.

### 6.3 Metrics and denominators

Let `N` be all assigned episodes for a configuration/condition, `E` verified exposure and `I` behavioral entry. Retain these counts and operationally unavailable trajectories explicitly.

| Outcome | Operational measure | Denominator / qualification |
|---|---|---|
| Exposure | Observation actually contains the designated attack-bearing region. | E/N; delivery alone is insufficient. |
| Entry | First action initiating the decoy; separately record time/steps to entry. | I/N primary; I/E secondary. No low-exposure agent is declared resistant without clean engagement evidence. |
| Non-progress work — primary | Count decision steps selecting decoy-directed actions that add no new verified legitimate subgoal, bounded by the episode cap. | All assigned episodes; nonentrants contribute zero, operationally missing episodes remain missing with sensitivity bounds. This mixes entry and retention intentionally as an end-to-end burden. |
| Retention | Steps and elapsed time from entry until exit, with decoy visits and semantic-state recurrence. | Entrant trajectories reported descriptively; caps are right-censored for natural exit time. Endogenous entrant groups are not randomized comparators. |
| Escape | Leave for legitimate route; safe-stop/report counted separately. | All assigned rate and entrant-conditional rate, with competing outcomes displayed. Stopping is not task recovery. |
| Recovery | Verified legitimate completion after entry; remaining actions/time to completion. | All assigned and entrant-conditional rates; distinguish never-entered completions. |
| Task deviation | Unauthorized or task-irrelevant proposed/executed actions by stage. | Separate proposal, action and verified effect; deviations can occur without retention. |
| Legitimate progress | New server-verified subgoals and final goal, alongside the page's claimed progress. | Per episode and over decision steps; repeated claims/checks do not add progress. Report success on clean finite workflows. |
| Resources | Absolute actor/planner/verifier calls, input/output tokens, browser requests, elapsed time and waiting time. | All assigned totals/distributions; paired differences primary, ratios secondary with near-zero denominators disclosed. Hidden reasoning tokens remain unknown unless provider accounting exposes them. |
| Sandbox effects | Local server records a synthetic event, if an effect extension is later introduced. | Attempt and receipt are separate. No real credentials, uploads or external callbacks; no effect endpoint is needed for the core pilot. |

Always report counts beside rates. Do not pool initial clicks, self-reflected failure, phishing field entry, loop crashes, tool-chain thresholds and resource-sink exhaustion under a shared ASR. Displayed completion, agent-reported completion and evaluator-confirmed completion remain separate.

### 6.4 Hypotheses, analysis and falsification

**H1, primary:** Task-relevant recurring prerequisites increase bounded non-progress interaction compared with neutral framing on equivalent recurring structures. Estimate a paired mean difference within task templates for the reactive agent. **H2, supporting:** Task relevance interacts with recurrence, producing an effect beyond topology alone. Operationally, the task-alignment effect is larger under recurrence than under a finite workflow; estimate the difference between the two within-topology semantic contrasts. **H3, exploratory:** Appropriate progress-aware escape strategies can reduce non-progress work without substantially damaging legitimate iterative task performance. H3 is a later intervention, not a third pilot factor.

Estimate overall effects on all assigned episodes, then show trajectory stages. Conditional retention differences between naturally selected entrants are descriptive, not automatically causal. If conditional retention is the later central question, use a distinct experiment that places every agent at a fixed, pre-randomization decoy entry state and then randomizes continuation; label this forced-entry estimand separately from natural entry.

Tasks/site templates, not individual decisions, supply independent evidence. Pair conditions, reset state between runs, vary run order, and nest repeated samples within templates. Report per-template results, effect sizes and uncertainty; with very few templates, cluster-bootstrap intervals are unstable and must be described as exploratory. Do not treat 180 episodes as 180 independent task families. Any later confirmatory sample size must use pilot variance/clustering and a prespecified meaningful effect, not the observed best-case ASR.

Budget exhaustion means an observed capped outcome and censored natural escape time. Goal completion, safe stop and crash are competing termination outcomes; do not apply a survival analysis that treats them all as harmless independent censoring. Analyze restricted-budget work directly and report terminal-state counts. Operational interruption is separate; show missingness by arm and sensitivity bounds rather than coding it as resistance. Adaptive attack development must use different tasks from evaluation and equal query opportunity across comparators.

Evidence against the leading hypothesis includes: little paired semantic effect; the same burden on neutral cycles; retention fully explained by response length or delay; failure only where no goal path exists; or a trivial retry bound eliminating burden with negligible utility loss. These outcomes may support a useful negative or engineering result, but not a strong new semantic attack claim.

## 7. Small feasibility pilot — proposal only

Use **six synthetic task templates**, split across two small local workflow families, such as document retrieval and catalog lookup. Build no adaptive website generator. The initial task scope does not require login, external services, real identities, real purchases or simulated harmful execution.

Four factorial site conditions cross **task-aligned versus neutral prerequisite framing** with **recurring versus finite prerequisite transitions**. All retain a legitimate reachable goal and escape route. Add one matched clean workflow per template. Hold page topology fixed for each within-topology semantic pair. The clean condition establishes ordinary capability, not a post hoc filter on evaluation episodes.

For feasibility, propose one pinned backbone in two single-agent configurations: reactive and planner/executor. Three independent resets/repeats per template-condition-configuration yield **6 × 5 × 2 × 3 = 180 agent episodes**. The reactive H1 contrast is primary; architecture comparisons are exploratory. Model-family transfer follows only if this pilot remains useful. Run deterministic crawler/rule-based references separately on the same fixtures, documenting that their objectives and interfaces differ; do not silently add their counts to the LLM denominator.

Proposed initial maximum: **30 browser decisions per episode**, with an additional total-call ceiling of **60 model invocations**, a **five-minute wall-clock ceiling**, bounded per-call generation and an explicit total-token/cost allowance set before running. The earliest cap terminates execution; which cap binds is recorded. These limits can make architecture/resource allowances unequal in practice, so show realized usage and regard architecture effects as system-level. A follow-up resource-matched sensitivity study is needed before claiming an inherent planning advantage. Prices and affordable total spend must be chosen at execution; none is asserted here.

The maximum planned browser-decision workload is **5,400**; the separate maximum model-call workload is **10,800**, not a prediction. Internal retries and verification calls count toward that ceiling. This is a feasibility proposal, not power justification or permission to begin dispatch.

Before interpreting any pilot: confirm legitimate reachability and exit usability in every fixture; verify identical paired graph/content constraints; confirm clean workflow solvability; inspect all retained trajectories for the proposed mechanism; reconcile action/progress labels against local server state; and disclose failed observations. Human review should include apparent successes and failures, not only persuasive examples. No hidden chain-of-thought is necessary or assumed.

A pilot is promising only if the same-direction effect appears across multiple templates and is not accounted for by topology, delay, volume or broken execution, while normal iterative tasks still work. With two workflow families, transfer beyond them remains unknown. If only the entry click changes, study entry persuasion rather than relabeling it sustained trapping. If only a crash occurs, report availability failure rather than retention. If no semantic effect appears, preserve the result and reconsider the contribution before scaling.

## 8. Reconciliation with the existing controlled comparison

| Existing element | Decision | Reason in the restored agenda |
|---|---|---|
| Exposure → decision → execution separation | Retain | Entry is not retention; proposed action is not effect. This is useful regardless of a standalone comparator. |
| Paired clean/attack tasks and independent success oracle | Retain and specialize | Add task progress, decoy recurrence, reachable escape and post-entry recovery. |
| Fixed content/common-action forced-exposure replay | Retain as optional explanation | Can test whether a prerequisite changes a next-step choice. Cannot establish closed-loop retention or universal intrinsic model susceptibility. |
| Closed-loop sandbox interaction | Promote to primary | It contains the feedback and repeated choices the research question requires. |
| Standalone versus executor-enabled arms as the main comparison | Defer | A system without navigation cannot produce comparable retention trajectories; missing capability is not robustness. |
| Permissions/verified harmful actions as main outcomes | Revise | They are optional consequence extensions. Core outcomes are progress-free work, escape and authorized recovery. |
| Memory/modality/adaptation factorials | Defer | They change access and interpretation and would overwhelm the initial mechanism test. |
| Large sample-size/workload plan | Replace for this proposal only | Use the small feasibility pilot first; no existing artifact or protocol is edited. |
| Clustering, capped outcomes, utility and operational missingness | Retain | These prevent misleading rates, pseudoreplication and timeout-based success claims. |

The original design remains a proposal and source of methods. This roadmap does not assert that its causal question was empirically answered or that agents are universally more susceptible than standalone models.

## 9. Research phases, publication potential and review decision

### Phase 0 — human assessment of contribution, now

Review the competitor distinctions and the primary threat model before authorizing implementation. The immediate decision is whether semantic/topological separation and recovery measurement offer enough explanatory value beyond the close studies. The unresolved novelty questions are:

1. Do newer versions or artifacts of the navigation and retention competitors already cross task alignment with matched topology and an independently reachable goal?
2. Do prerequisite/verification studies quantify repeated non-progress interaction and recovery in their supplementary trajectories, even if these are not headline metrics?
3. Would this experiment explain a distinct mechanism, or merely repackage a known progress/validation chain in a browser?
4. Is public task context sufficient, or would the proposed effect depend on private task knowledge unavailable to the stated adversary?
5. Is an escape/progress intervention already evaluated under equivalent information and utility controls?

A full methods/artifact audit of the closest competitors, including any unavailable supplementary material and Simulacrum, is required before a manuscript claims an unfilled global gap. This is a research review task, not a new receipt framework or engineering phase.

### Phase 1 — bounded fixture feasibility, only after review

If separately authorized, construct the few deterministic local fixtures and reference paths, then inspect exposure, progress and termination observability without broad victim dispatch. Confirm that trapping is a choice phenomenon in a solvable environment. Reconsider if the intended contrast cannot be implemented without changing legitimate task difficulty or attacker privilege.

### Phase 2 — pilot, only after fixture acceptance

Run the proposed limited workload with declared caps, resets and all-assigned denominators. Preserve unsuccessful and operationally interrupted trajectories. Diagnose semantic retention versus topological wandering, benign exploration, single-step persuasion and implementation defects. Do not optimize the same fixtures repeatedly and call their final performance held-out evidence.

### Phase 3 — narrow confirmatory study and first extension

If the pilot supports the mechanism, independently choose new task/site families and fix the analysis before evaluation. Prefer one extension: a simple progress-aware retry/escape rule, compared against a generic action cap and cycle detection on both decoy and legitimate iterative tasks. Additional model-family transfer can assess generality. Persistent memory, visual-only interfaces, adaptive opponents and delegation remain separate studies unless the primary mechanism requires them.

### Plausible contribution and its limits

A defensible paper could contribute an operational account of **task-dependent retention in solvable adversarial web workflows**, evidence separating semantic prerequisites from navigation topology, and an escape-versus-utility evaluation. It would be a focused empirical security/agent-evaluation contribution if it discovers a reproducible effect or an informative boundary that competitors do not already measure. A small set of convincing screenshots, a high redirection rate or a large token ratio is insufficient.

The strongest novelty threats are already concrete: existing navigation traps, AI-retaining honeypots, task-compatible phishing prerequisites, progress/validation chains and staged delegation failures. The proposal must earn its distinction through controls and explanation. Publication suitability and generality cannot be established before those checks and experiments; no priority or venue outcome is promised.

**Current stop:** human research review of the synchronized foundation and proposal. No implementation, experiment, corpus dispatch or historical-state transition is authorized. The [foundation handoff](../../docs/RESEARCH_FOUNDATION_HANDOFF.md) defines the separate future experiment-repository boundary.
