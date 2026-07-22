# Problem–Approach Matrix

## Scope and assignment rule

This matrix is an evidence map of the **48 comprehensive summaries in `Summaries/`**, not a keyword map. A paper is placed in a cell only when the summary says that the paper (a) proposes or implements that row's approach and (b) applies or evaluates it on that column's problem. A benchmark paper is credited with benchmark/evaluation design, not with every method run as a baseline. A paper that discusses, recommends, or lists a defense is not credited with evaluating that defense. Attack benchmarks remain attacks/evaluations; they are never relabeled as defenses. A defense with poor or mixed results is included only in the evaluated-defense table and is marked accordingly.

Short names identify papers. `—` means no supported assignment in this 48-paper corpus. Parenthetical text narrows the supported claim; it is not a general endorsement. “Environment” means a reusable task/evaluation environment; “agent” means a proposed system; and “data” means a collected or generated training resource.

## 1. Capability and control

| Implemented approach | General browser tasks | DOM / accessibility-tree control | Visual / coordinate grounding | Conversational or enterprise workflow | Mobile / API-adjacent control |
|---|---|---|---|---|---|
| Interleaved reasoning and action | ReAct; WebArena baseline; BrowserGym GenericAgent | ReAct; WebArena; BrowserGym | WebVoyager | WorkArena agent | AndroidWorld M3A |
| Simplified HTML or ranked markup | AutoWebGLM | AutoWebGLM; WebLINX (Dense Markup Ranking) | — | WebLINX | — |
| Screenshot plus element grounding | SeeAct; WebVoyager | SeeAct (grounding stage) | SeeAct; WebVoyager | WorkArena (vision ablation) | AndroidWorld (Set-of-Marks M3A; SeeAct transfer) |
| High-level grounded action policy | WebShop | WebShop (text observations) | WebShop (multimodal choice model) | — | — |
| Modular / multi-agent planning | WebWalker (explorer–critic); LASER | LASER | SeeAct (planning/grounding/execution) | — | — |
| Unified environment and instrumentation | BrowserGym; WebArena | BrowserGym; WebArena | BrowserGym | WorkArena | AndroidWorld |
| API selection / tool-use model | — | — | — | — | Toolformer; Gorilla |

**Boundary:** VisualWebArena, Mind2Web, WebLINX, WorkArena++, and AndroidWorld contribute datasets or evaluations even when they also implement baselines. They are not assigned as new visual-control or planning methods unless the summary identifies a proposed agent or control component. Toolformer and Gorilla concern tool/API use rather than browser control and are retained only as adjacent capability evidence.

## 2. Training and data construction

| Training/data approach | Browser action learning | Information-seeking learning | Enterprise / dialogue traces | Tool / API learning | No agent training contribution |
|---|---|---|---|---|---|
| Human demonstrations / behavior cloning | WebShop; AutoWebGLM | WebGPT | WebLINX | — | Mind2Web (demonstration dataset) |
| Supervised fine-tuning on filtered trajectories | AutoWebGLM | WebDancer; WebSailor | WebLINX | — | — |
| Reinforcement learning or reward optimization | WebShop; AutoWebGLM (self-sampling RL) | WebGPT; WebDancer; WebSailor (DUPO) | — | — | — |
| Rejection sampling / best-of-*n* | AutoWebGLM | WebGPT; WebSailor (RFT cold start) | — | — | — |
| Structured exploration for data generation | Go-Browse | — | WorkArena++ (oracle ground-truth traces, not a trained model) | — | — |
| Synthetic questions / trajectories | — | WebDancer (CRAWLQA/E2HQA); WebSailor (SailorFog-QA) | — | Gorilla (synthetic API instructions) | — |
| Self-supervised tool-use insertion | — | — | — | Toolformer | — |
| Retriever-aware API fine-tuning | — | — | — | Gorilla | — |

**Boundary:** WorkArena++ supplies oracle traces intended to support future fine-tuning but does not report training an agent on them. Mind2Web is a human-demonstration dataset and evaluation, not evidence that its paper trained a new browser agent. Benchmark construction alone is not “training.”

## 3. Evaluation and benchmark contribution

| Evaluation contribution | General interaction / navigation | Live-web search / traversal | Visual or multimodal interaction | Enterprise / dialogue | Safety / security | Adjacent platform |
|---|---|---|---|---|---|---|
| Dataset or benchmark | Mind2Web; WebShop; WebArena; AutoWebBench | BrowseComp; WebWalkerQA; Mind2Web 2; BEARCUBS; MMInA | VisualWebArena; WebVoyager task set; BEARCUBS; MMInA | WebLINX; WorkArena; WorkArena++ | SafeArena; ST-WebAgentBench; WASP; FORGE; SearchGEO; BackdoorAgent; Formalizing Prompt Injection | AndroidWorld; APIBench (Gorilla) |
| Reusable environment / evaluation infrastructure | WebShop; WebArena; BrowserGym | BrowserGym (unified access to included suites) | VisualWebArena; BrowserGym | WorkArena via BrowserGym | WASP (self-hosted full-stack web environments) | AndroidWorld |
| Outcome / state-based automatic scoring | WebShop; WebArena | — | VisualWebArena | WorkArena; WorkArena++ | WASP (intermediate and end-to-end state); ST-WebAgentBench (task plus policy) | AndroidWorld |
| LLM or agent as judge | WebVoyager (GPT-4V trajectory/outcome judge) | Mind2Web 2 (agent-as-a-judge); WebWalkerQA (LLM evaluation caveat); BEARCUBS (automatic evaluator) | WebVoyager | — | WASP (intermediate-state judge); SafeArena (ARIA/refusal judging) | — |
| Human comparison / validation | WebShop; WebArena; Mind2Web | BrowseComp; BEARCUBS | WebVoyager; BEARCUBS | WebLINX; WorkArena++ | SafeArena (subset validation) | AndroidWorld |

**Boundary:** The safety/security entries in this table are evaluation artifacts, not defenses. WebVoyager's automatic judge was checked against humans but is not a safety judge. SearchGEO and FORGE evaluate evidence manipulation; neither is a general information-seeking benchmark.

## 4. Extraction, information seeking, and exploration

| Implemented approach | Structured extraction / scraper generation | Broad web research | Deep within-site traversal | Exploration for training data | Security-oriented state exploration |
|---|---|---|---|---|---|
| Executable scraper synthesis | AutoScraper (progressive generation plus cross-page synthesis) | — | — | — | — |
| Multimodal index-to-content extraction | Webscraper (parse/merge tools and staged procedure) | — | — | — | — |
| Browser-assisted evidence collection | — | WebGPT | — | — | — |
| Long-horizon search reasoning | — | WebDancer; WebSailor | — | — | — |
| Explorer–critic vertical navigation | — | WebWalker (QA) | WebWalker | — | — |
| State-space search / explicit planning | — | LASER | LASER | — | — |
| Structured graph exploration | — | — | Go-Browse | Go-Browse | — |
| Evolutionary interaction-sequence search | — | — | — | — | EvoCrawl |
| Task-driven goal-based crawling | — | — | — | — | YuraScanner |
| Memory-guided specialist exploitation | — | — | — | — | AWE |

**Boundary:** AutoScraper and Webscraper generate or perform scraping; they do **not** defend against scrapers. EvoCrawl and YuraScanner crawl web applications to expose states for security testing, not to answer information-seeking questions. AWE is a penetration-testing framework, not a general navigation agent.

## 5. Security attacks and adversarial evaluations

| Attack/evaluation approach | Indirect prompt injection in retrieved/web content | Retrieval manipulation or content pollution | Tool selection / app control | Persistent backdoor / skill supply chain | Harmful user intent / policy violation |
|---|---|---|---|---|---|
| Real-system attack study | Not What You've Signed Up For; When AI Meets the Web | Unsafe LLM-Based Search | When AI Meets the Web | — | — |
| Formal or controlled attack suite | Formalizing Prompt Injection; WASP | — | ACE (three attacks on IsolateGPT) | BackdoorAgent | SafeArena |
| Adaptive / optimized attack generation | Overcoming the Retrieval Barrier (retrieval trigger optimization) | SearchGEO; FORGE (controlled polluted evidence) | ToolHijacker (optimized tool description) | SkillTrojan (composed encrypted fragments) | — |
| End-to-end full-stack web attack evaluation | WASP | — | — | — | — |
| Safety-and-utility policy evaluation | — | — | — | — | ST-WebAgentBench |

**Boundary:** Unsafe LLM-Based Search measures malicious or harmful retrieved pages and also evaluates a detector-based defense; it is not a prompt-injection paper. SearchGEO and FORGE manipulate claims, consensus, or recommendations without relying on embedded instructions. ToolHijacker attacks retrieval and selection of a tool description, not demonstrated malicious tool execution. BackdoorAgent and SkillTrojan are attack frameworks; their ordinary-task accuracy does not make them defenses.

## 6. Safety evaluation (what is measured)

| Evaluation target | Harmful-request acceptance | Indirect environmental hijacking | Policy compliance during benign work | Malicious-source endorsement | Persistent / composed compromise |
|---|---|---|---|---|---|
| Task-level completion and refusal | SafeArena | — | — | — | — |
| Intermediate and final harmful state | — | WASP | — | — | — |
| Functional success plus policy compliance | — | — | ST-WebAgentBench | — | — |
| Risky citation / recommendation outcome | — | — | — | Unsafe LLM-Based Search; FORGE; SearchGEO | — |
| Attack success with clean utility | — | Formalizing Prompt Injection; WARD evaluation; RENNERVATE evaluation | — | — | BackdoorAgent; SkillTrojan |

SafeArena's paired tasks and normalized safety score attempt to separate refusal from mere inability. WASP explicitly distinguishes diversion from completion: this prevents “security through incompetence” from being counted as robust defense. ST-WebAgentBench penalizes successful tasks that violate consent, privacy, reliability, or other policies; it proposes future controller ideas but does not evaluate such a controller.

## 7. Evaluated defenses only

| Evaluated defense | Prompt injection | Malicious retrieval / polluted evidence | Tool/app compromise | Backdoors / malicious skills | Result qualification |
|---|---|---|---|---|---|
| Prevention/detection baselines | Formalizing Prompt Injection (10 defenses) | — | — | — | None solved the benchmark reliably; security–utility trade-offs remained. |
| Attention-based token detection and sanitization | RENNERVATE | — | — | — | Strong text-only results; requires internal attention access and has residual adaptive/utility failures. |
| Multimodal guard model | WARD | — | — | — | Near-complete reported detection and zero attack success in tested live-agent tasks; task-aligned visual camouflage remains a failure mode. |
| Fixed typed plan, isolation, and static information-flow verification | ACE | — | ACE | — | Blocked all three new IsolateGPT attacks and all tested INJECAGENT attacks while retaining substantial tool utility. |
| Defensive prompt / instruction hierarchy | WASP | SearchGEO (simple defensive prompts) | — | — | Reduced some attacks but was inconsistent and/or reduced utility; not a complete defense. |
| URL/HTML detector plus response refinement | — | Unsafe LLM-Based Search | — | — | HtmlLLM: 0.822 F1 and 78.3% response-level defense success; XGBoost caught all malicious URLs but had many false positives. |
| Skepticism / prior-consensus / cross-document checks | — | FORGE | — | — | Evaluated, with cross-document corroboration strongest among the reported defenses; not established as general protection. |
| Plugin trust-boundary prototypes | When AI Meets the Web (UGCBuster for user content) | — | When AI Meets the Web (tool-instruction hardening) | — | Prototype evaluations only; no broad deployment guarantee. |
| Existing detectors, scanners, or human review tested against a new attack | — | ToolHijacker | ToolHijacker | BackdoorAgent (probability signal); SkillTrojan (two lightweight scanners) | Mostly weak or bypassed; inclusion records a negative defense evaluation, not an effective defense. |

**Not assigned as evaluated defenses:** Not What You've Signed Up For and Overcoming the Retrieval Barrier discuss possible mitigations but do not establish an effective evaluated defense in the supplied summaries. Toward Secure LLM Agents synthesizes defense families but is a systematic review. SafeArena and ST-WebAgentBench motivate defenses but primarily evaluate agents. SearchGEO's provenance checks are future work, not an implemented defense.

## 8. Provenance, containment, and scraper accountability

| Implemented or evidenced mechanism | Source / content provenance | Capability and information-flow control | Execution isolation / containment | Scraper attribution or publisher control |
|---|---|---|---|---|
| Typed planning and static flow checks | ACE (trusted request separated from app descriptions/outputs) | ACE (restricted plan and clearance checks) | ACE (isolated execution containers) | — |
| Role and content-boundary preservation | When AI Meets the Web (plugin analysis and prototypes) | When AI Meets the Web (authenticated histories/tool-role separation as tested design guidance) | — | — |
| Canary-token attribution | — | — | — | Canary Tokens (User-Agent/ASN linkage) |
| Lifecycle security synthesis | Toward Secure LLM Agents (identifies provenance gap) | Toward Secure LLM Agents (maps access control and information-flow work) | Toward Secure LLM Agents (maps sandboxing/containment) | — |

The survey row records **systematization**, not an evaluated implementation. Canary Tokens evaluates attribution and post-scraping controls: it does not claim to prevent scraping, and its evidence shows that taking sites offline or adding `robots.txt` after collection usually failed to stop chatbot reuse. No paper in the corpus evaluates a complete provenance chain that establishes independence of web sources, signed skill provenance, revocation, and runtime containment together.

## 9. Web-security testing

| Implemented system | Exploration strategy | Vulnerability testing / verification | Evaluation scope | Supported limitation |
|---|---|---|---|---|
| YuraScanner | LLM task generation and goal-directed workflow execution | XSS testing; manually reviewed findings | 20 applications; comparison with Black Widow and BFS variants | Generated invalid tasks and incomplete executions; complements rather than replaces conventional crawling. |
| EvoCrawl | Evolutionary sequences with dependency tracking and coverage fitness | Modular XSS and IDOR detectors; known and new findings | Seven web applications | Black-box coverage and detector limitations; not an LLM web-agent method. |
| AWE | Orchestrated vulnerability specialists, persistent memory, reconnaissance | Browser-backed exploit verification; adaptive payload mutation | DVWA and 104 XBOW challenges | Strong on XSS/blind SQLi and efficient, but lower total coverage than broader MAPTA. |

These systems are assigned only to security testing. Their crawling, planning, or browser use does not make them evidence for ordinary web QA, scraper defense, or safety-policy compliance.

## Concise evidence key

Representative exact findings anchor the assignments and show their limits:

- **AutoScraper:** GPT-4-Turbo reached **88.69 F1**, **71.56% fully correct**, and **4.06% unexecutable** on SWDE; XPath fragility and layout change remain limitations.
- **WebVoyager:** completed **59.1% of 643 live-site tasks**, versus **40.1%** for its text-only variant; its evaluator is a GPT-4V outcome judge validated against humans, not ground truth for every case.
- **WorkArena++:** humans solved about **94%**, GPT-4o about **2%**, and all tested models scored zero on L3; oracle traces were generated, but no trace-trained model was evaluated.
- **BrowseComp:** Deep Research scored **51.5%** and best-of-64 selection about **78%**; this is an information-seeking benchmark, not a new browser-control method.
- **WASP:** intermediate attack success ranged about **17–86%**, while end-to-end success was **0–17%**; defensive prompting sometimes lowered utility.
- **SafeArena:** every initially refused harmful task could be completed through decomposition for the safest tested agent; the sites are controlled simulations and judge-based measures have bounded human validation.
- **ST-WebAgentBench:** mean task success fell from **24.3%** to **15.0%** when policy compliance counted; it evaluates policy-aware safety but does not demonstrate the proposed centralized controller.
- **WARD:** reported false-positive rates around **0.2–0.35%** and reduced tested live-agent attack success to zero; highly task-aligned visual camouflage and pixel-level attacks remain outside complete coverage.
- **RENNERVATE:** reported roughly **98–99.6% detection accuracy** across five LLMs; it needs white-box attention access and covers textual, not image/audio, injection.
- **Formalizing Prompt Injection:** the strongest Combined Attack reached **0.75 average success on GPT-4**; none of ten tested defenses was reliably satisfactory.
- **Unsafe LLM-Based Search:** **47%** of responses were risky and **34%** directly cited harmful content; HtmlLLM achieved **0.822 F1** and **78.3%** defense success, whereas a perfect-recall XGBoost detector produced many false positives.
- **FORGE:** evaluates fake-product recommendation from polluted pages and reports cross-document corroboration as the strongest tested defense family; it is evidence manipulation, not instruction injection.
- **SearchGEO:** explicit attack success ranged from **0%** for Claude-Sonnet-4.6 to **31.4%** for Gemini-3-Flash; provenance and source-independence checks are proposed future work, not evaluated mechanisms.
- **Overcoming the Retrieval Barrier:** ten optimized tokens placed a poisoned item in the top five about **94%** of the time; one poisoned email produced **80% SSH-key exfiltration** in a GPT-4o workflow, while simple defenses failed after adaptation.
- **ACE:** blocked all tested INJECAGENT attacks and all three newly demonstrated IsolateGPT attacks; its guarantee is scoped to the architecture, planning language, policies, and benchmarks evaluated.
- **SkillTrojan:** reached up to **97.2% attack success** with **89.3% clean accuracy** and largely evaded two lightweight scanners; signed provenance and sandboxing are recommendations, not evaluated contributions of that paper.
- **Canary Tokens:** obtained attributable evidence for **18 of 22 chatbots**; **12 of 18** continued returning content in both offline and `robots.txt` conditions, so the method supports attribution rather than reliable deletion or prevention.
- **YuraScanner:** only **61.3%** of valid tasks were fully or nearly completed and about **23%** of generated tasks were invalid, yet it found 12 of 13 unique previously unknown vulnerabilities found by the two compared scanners.
- **AWE:** solved **54/104** XBOW challenges versus MAPTA's **80/104**, but reached **87% XSS** and **67% blind-SQLi** success with about **98% fewer tokens**; it is a specialist with narrower breadth.

## Coverage and accounting

All **48/48** summary files were reviewed and are accounted for below. “Primary role” prevents a paper from appearing to contribute a method merely because it evaluates one; papers can still have supported secondary assignments in the tables.

| Primary role | Papers | Count |
|---|---|---:|
| Browser capability agents / control methods | ReAct; WebShop; AutoWebGLM; SeeAct; WebVoyager; LASER; WebWalker | 7 |
| Training/data methods for web information seeking or navigation | WebGPT; WebLINX; Go-Browse; WebDancer; WebSailor | 5 |
| Extraction systems | AutoScraper; Webscraper | 2 |
| Capability benchmarks / environments | Mind2Web; WebArena; VisualWebArena; BrowserGym; WorkArena; WorkArena++; BrowseComp; BEARCUBS; MMInA; Mind2Web 2 | 10 |
| Security/safety attacks, measurements, or benchmarks | Not What You've Signed Up For; Formalizing Prompt Injection; WASP; Overcoming the Retrieval Barrier; ToolHijacker; When AI Meets the Web; Unsafe LLM-Based Search; FORGE; SearchGEO; BackdoorAgent; SkillTrojan; SafeArena; ST-WebAgentBench | 13 |
| Security defense architecture / guard | ACE; WARD; RENNERVATE | 3 |
| Provenance/accountability or security synthesis | Canary Tokens; Toward Secure LLM Agents | 2 |
| Web-application security testing | YuraScanner; EvoCrawl; AWE | 3 |
| Adjacent mobile or general tool/API work | AndroidWorld; Toolformer; Gorilla | 3 |
| **Total** |  | **48** |

The accounting intentionally includes adjacent papers while bounding their claims. AndroidWorld is a mobile benchmark with a transferred web-agent baseline; Toolformer and Gorilla train general tool/API use; Toward Secure LLM Agents is a systematic synthesis. None is silently treated as evidence for a web-specific method it did not implement or evaluate.
