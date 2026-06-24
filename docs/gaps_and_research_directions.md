# Gap Analysis and Actionable Research Directions

Most work in this collection focuses on web-agent benchmarks and browser task completion. Security work focuses heavily on prompt injection. LLM-guided crawling/scraping, privacy leakage, containment, and live-web adversarial evaluation remain less mature.

## Gap 1: LLM-guided crawling is underdeveloped compared with browser-task benchmarks

- **Observed from papers:** WebArena, Mind2Web, VisualWebArena, WorkArena, and BrowserGym dominate benchmark coverage, while explicit crawling/traversal is mainly WebWalker, Go-Browse, YuraScanner, and borderline EvoCrawl.
- **Why it matters:** Many research, monitoring, and security tasks require systematic site exploration, not just completing a known instruction.
- **Current representative papers:** WebWalker, Go-Browse, LASER, YuraScanner, EvoCrawl, BEARCUBS.
- **What is missing:** A benchmark that measures coverage, efficiency, depth, semantic relevance, state discovery, and safe boundaries for LLM-guided site crawling.
- **Actionable research direction:** Build a benchmark or framework for goal-directed LLM crawling with explicit comparison to BFS, heuristic crawlers, evolutionary crawlers, and search-driven traversal.
- **Possible research questions:**
  - RQ1: How do LLM-guided crawlers compare to BFS, heuristic crawlers, evolutionary crawlers, and search-driven traversal?
  - RQ2: Can agents decide which links or UI states are worth exploring based on a research goal?
  - RQ3: Can crawling policies be made safe with rate limits, robots.txt awareness, and content-safety constraints?
- **Possible methodology:** Create self-hosted and archived websites with known link graphs, hidden states, dynamic UI paths, and goal-relevant/irrelevant pages; evaluate multiple crawl policies under fixed action budgets.
- **Possible evaluation setup:** Metrics for URL/state coverage, goal-relevant recall, duplicate-action rate, depth reached, elapsed requests, policy violations, and unsafe-action attempts.
- **Likely challenges:** Dynamic pages are hard to snapshot, coverage ground truth is expensive, and LLM crawlers may overfit to benchmark site patterns.
- **Potential contribution:** A crawling-focused benchmark that complements WebArena-style task completion and makes exploration quality measurable.

**Possible paper ideas:**
- "SafeCrawler: Policy-Aware LLM-Guided Crawling for Goal-Directed Website Exploration"
- "Prompt Injection in the Crawl Frontier: Adversarial Web Traversal for LLM Agents"
- "Beyond BFS: Measuring Semantic Coverage in LLM-Guided Web Crawling"

## Gap 2: Scraper generation is disconnected from safety, consent, and abuse prevention

- **Observed from papers:** AutoScraper and Webscraper focus on extraction capability; Canary Tokens focuses on detection. Few works connect generation, governance, and abuse resistance.
- **Why it matters:** Better scraper agents can support research and public-interest monitoring, but can also intensify consent, privacy, infrastructure, and attribution harms.
- **Current representative papers:** AutoScraper, Webscraper, Canary Tokens, When AI Meets the Web.
- **What is missing:** Scraper-generation systems that reason about access policies, sensitive data, rate limits, attribution, and site owner preferences.
- **Actionable research direction:** Connect AutoScraper/Webscraper-style capability work with canary-token detection, rate limiting, privacy filters, and policy compliance.
- **Possible research questions:**
  - RQ1: Can LLM-generated scrapers obey site-level access policies?
  - RQ2: Can scraper-generation agents detect and avoid sensitive or private data extraction?
  - RQ3: Can websites reliably distinguish benign research scraping from abusive AI scraping?
- **Possible methodology:** Extend scraper-generation benchmarks with policy files, canary tokens, sensitive fields, and allowed/forbidden extraction goals.
- **Possible evaluation setup:** Score extraction accuracy, scraper reusability, robots/policy compliance, sensitive-data avoidance, request budget, and canary-token leakage.
- **Likely challenges:** Legal norms vary by jurisdiction, robots.txt is not a complete policy language, and defensive measurement can be gamed.
- **Potential contribution:** A responsible scraper-generation benchmark and reference architecture.

**Possible paper ideas:**
- "Consent-Aware Web Scraper Generation with Large Language Models"
- "Can LLM Scrapers Follow Website Policies?"
- "From Extraction to Governance: Auditable AI Scraping Agents"

## Gap 3: Mainstream web-agent benchmarks rarely include adversarial webpages

- **Observed from papers:** WebArena and VisualWebArena are capability benchmarks; WASP and WARD add prompt-injection security layers separately.
- **Why it matters:** Agents optimized only for success may learn to obey malicious webpage content during normal browsing.
- **Current representative papers:** WebArena, VisualWebArena, WASP, WARD, Formalizing Prompt Injection, Not What You've Signed Up For.
- **What is missing:** Paired benign/adversarial variants of mainstream tasks where malicious instructions appear in HTML, rendered text, images, comments, ads, or hidden fields.
- **Actionable research direction:** Combine WebArena / VisualWebArena / WebWalker-style tasks with WASP / WARD-style malicious webpage injections.
- **Possible research questions:**
  - RQ1: How often do agents follow malicious page instructions during normal browsing?
  - RQ2: Are visual prompt injections more effective than hidden HTML injections?
  - RQ3: Can agents complete benign tasks while ignoring malicious webpage content?
- **Possible methodology:** Add controlled adversarial content to self-hosted web tasks and measure both task success and attack success.
- **Possible evaluation setup:** Paired task suites with clean, HTML-injected, visual-injected, and retrieval-injected variants; metrics for benign completion, attack compliance, refusal quality, and false positives.
- **Likely challenges:** Attack realism, benchmark contamination, and separating useful webpage instructions from malicious instructions.
- **Potential contribution:** A bridge between capability benchmarks and web-agent security benchmarks.

**Possible paper ideas:**
- "Adversarial WebArena: Measuring Browser Agents Under Malicious Page Content"
- "Visual vs. Hidden Prompt Injection in Multimodal Web Agents"
- "Task Success Under Attack: Dual-Metric Evaluation for Web Agents"

## Gap 4: Privacy leakage during multi-step browsing is underexplored

- **Observed from papers:** Not What You've Signed Up For, Overcoming the Retrieval Barrier, ACE, and ToolHijacker discuss data exfiltration pathways, but most web-agent benchmarks do not track private-context leakage.
- **Why it matters:** Agents often browse while holding user goals, credentials, enterprise records, documents, conversation history, or memory.
- **Current representative papers:** ACE, Overcoming the Retrieval Barrier, ToolHijacker, ST-WebAgentBench, WebLINX, WebGPT.
- **What is missing:** Benchmarks that track what private context leaks into search queries, forms, tool calls, URLs, citations, screenshots, or final answers.
- **Actionable research direction:** Design privacy-leakage benchmarks for agents browsing with user context, accounts, memory, or private documents.
- **Possible research questions:**
  - RQ1: What private context leaks into search queries, forms, tool calls, or final answers?
  - RQ2: Which agent architectures leak less: ReAct, modular planners, browser-only agents, or policy-gated agents?
  - RQ3: Can privacy budgets or taint tracking reduce leakage?
- **Possible methodology:** Seed tasks with canary secrets, private facts, and decoy instructions, then trace data flow across browser actions and generated text.
- **Possible evaluation setup:** Metrics for secret exposure, query leakage, form leakage, cross-origin leakage, and task success under privacy constraints.
- **Likely challenges:** Defining leakage severity, instrumenting browser/tool actions, and balancing privacy with task completion.
- **Potential contribution:** A benchmark and measurement framework for privacy-preserving web agents.

**Possible paper ideas:**
- "Privacy Budgets for Autonomous Browser Agents"
- "Taint Tracking for LLM Web Agents"
- "Where Did the Secret Go? Measuring Context Leakage in Multi-Step Browsing"

## Gap 5: Containment and sandboxing for browser agents remain immature

- **Observed from papers:** ACE proposes architectural separation and ST-WebAgentBench evaluates policy compliance, but most browser agents rely on prompts and action-space restrictions.
- **Why it matters:** Browser agents can click, type, submit forms, buy goods, send messages, delete data, and change enterprise state.
- **Current representative papers:** ACE, ST-WebAgentBench, ToolHijacker, BrowserGym, WorkArena, WorkArena++.
- **What is missing:** A concrete permission model for browser actions, origins, credentials, forms, downloads, payments, and external tools.
- **Actionable research direction:** Design and evaluate containment models for agents that can browse, click, type, submit forms, and call tools.
- **Possible research questions:**
  - RQ1: What permission model is needed for browser actions?
  - RQ2: Which actions require human approval?
  - RQ3: Can agents be restricted by origin, data sensitivity, or task phase?
- **Possible methodology:** Build a browser-agent sandbox with capability tokens, action gates, origin policies, and human approval hooks.
- **Possible evaluation setup:** Enterprise and public-web tasks with policy-violating temptations; measure completion, blocked hazards, unnecessary approvals, and bypass attempts.
- **Likely challenges:** Overly strict policies harm usability; overly loose policies fail security; UI semantics are hard to classify automatically.
- **Potential contribution:** A browser-agent security architecture analogous to a permissioned operating environment.

**Possible paper ideas:**
- "Capability-Based Sandboxing for Autonomous Browser Agents"
- "Human Approval Gates for High-Risk Web Agent Actions"
- "Origin-Aware Permissions for LLM-Controlled Browsers"

## Gap 6: Live-web evaluation is realistic but hard to reproduce

- **Observed from papers:** BEARCUBS, BrowseComp, MMInA, WebVoyager, and Mind2Web 2 use live or real-world websites; WebArena, VisualWebArena, WebShop, and WorkArena use controlled or self-hosted environments.
- **Why it matters:** Live sites capture real UI diversity and drift, but results can become irreproducible within weeks.
- **Current representative papers:** BEARCUBS, BrowseComp, MMInA, WebVoyager, Mind2Web 2, WebArena, BrowserGym.
- **What is missing:** A systematic comparison of live-web, self-hosted, archived, and hybrid benchmark designs.
- **Actionable research direction:** Compare benchmark designs that balance realism, reproducibility, update cost, and safety.
- **Possible research questions:**
  - RQ1: Which benchmark design best balances realism, reproducibility, and safety?
  - RQ2: Can archived pages preserve enough dynamic behavior?
  - RQ3: How should results be versioned when websites change?
- **Possible methodology:** Run the same tasks across live, archived, and self-hosted versions; record browser traces, DOM snapshots, screenshots, and site versions.
- **Possible evaluation setup:** Metrics for task stability, answer drift, action drift, replay fidelity, benchmark maintenance cost, and safety incidents.
- **Likely challenges:** Capturing dynamic JS behavior, authentication, third-party resources, and legal permission for archiving.
- **Potential contribution:** A practical benchmark design guide for future web-agent evaluations.

**Possible paper ideas:**
- "Live, Archived, or Self-Hosted? Reproducibility Tradeoffs in Web-Agent Benchmarks"
- "Versioned Web Tasks for Longitudinal Browser-Agent Evaluation"
- "Hybrid Benchmarks for Realistic and Repeatable Web Agents"

## Gap 7: Long-horizon multi-site tasks are still weakly covered

- **Observed from papers:** BrowseComp, BEARCUBS, MMInA, WebDancer, WebSailor, and Mind2Web 2 push toward deeper research, but many benchmarks are site-local or short-horizon.
- **Why it matters:** Real research workflows require gathering evidence across many sites, reconciling conflicts, and deciding when enough evidence has been collected.
- **Current representative papers:** WebGPT, BrowseComp, BEARCUBS, MMInA, WebDancer, WebSailor, Mind2Web 2.
- **What is missing:** Tasks requiring cross-site comparison, evidence tracking, source conflict resolution, and synthesis under uncertainty.
- **Actionable research direction:** Create tasks that require multi-site planning, citation management, contradiction handling, and stopping decisions.
- **Possible research questions:**
  - RQ1: How do agents manage state across many websites?
  - RQ2: How do they decide when enough evidence has been collected?
  - RQ3: How do they resolve conflicting sources?
- **Possible methodology:** Build a benchmark of multi-source questions with known evidence graphs and controlled source reliability.
- **Possible evaluation setup:** Score answer correctness, citation quality, evidence coverage, contradiction handling, query efficiency, and unsupported claims.
- **Likely challenges:** Ground-truth evidence graphs are costly, and open-web answers can change.
- **Potential contribution:** A stronger evaluation target for deep-research agents.

**Possible paper ideas:**
- "Evidence Graphs for Long-Horizon Web Research Agents"
- "When Should a Web Agent Stop Searching?"
- "Source Conflict Resolution in Autonomous Browsing Agents"

## Gap 8: Security papers focus heavily on prompt injection, leaving other threats underexplored

- **Observed from papers:** WASP, WARD, RENNERVATE, Formalizing Prompt Injection, Overcoming the Retrieval Barrier, ToolHijacker, and When AI Meets the Web center on injection-like threats.
- **Why it matters:** Prompt injection is critical, but web agents also face phishing, scams, malicious downloads, account misuse, harmful transactions, and denial-of-wallet costs.
- **Current representative papers:** SafeArena, Unsafe LLM-Based Search, ACE, ST-WebAgentBench, ToolHijacker, When AI Meets the Web.
- **What is missing:** A broader taxonomy and benchmark suite for non-injection web-agent threats.
- **Actionable research direction:** Broaden web-agent security evaluation beyond prompt injection.
- **Possible research questions:**
  - RQ1: What are the risks from phishing, scams, malicious downloads, CSRF-like workflows, account misuse, or payment flows?
  - RQ2: Can web agents detect deceptive UI or social engineering?
  - RQ3: What is the equivalent of browser security policy for autonomous agents?
- **Possible methodology:** Build threat scenarios in controlled sites: phishing forms, deceptive checkout flows, fake support pages, malicious downloads, and account-change workflows.
- **Possible evaluation setup:** Measure threat detection, safe refusal, user-confirmation behavior, false positives, and task completion under benign lookalikes.
- **Likely challenges:** Threat simulation must avoid enabling real abuse and must distinguish user intent from harmful requests.
- **Potential contribution:** A web-agent security benchmark that covers the broader browser threat model.

**Possible paper ideas:**
- "Beyond Prompt Injection: A Threat Taxonomy for Autonomous Web Agents"
- "Can Browser Agents Recognize Phishing and Deceptive UI?"
- "Security Policies for Autonomous Agents on the Web"

## Gap 9: Enterprise web agents need auditability, human approval, and compliance models

- **Observed from papers:** WorkArena and WorkArena++ benchmark enterprise workflows; ST-WebAgentBench adds policies; ACE proposes architecture.
- **Why it matters:** Enterprise agents operate over sensitive records, regulated processes, and consequential workflows.
- **Current representative papers:** WorkArena, WorkArena++, ST-WebAgentBench, BrowserGym, ACE.
- **What is missing:** Audit logs, approval workflows, role-based access, compliance checks, and policy explanations built into enterprise web-agent evaluation.
- **Actionable research direction:** Extend WorkArena / ST-WebAgentBench with audit logs, approval workflows, and organization-specific policies.
- **Possible research questions:**
  - RQ1: What actions require approval in enterprise workflows?
  - RQ2: How should agents explain or justify browser actions?
  - RQ3: Can policy violations be detected before the action is executed?
- **Possible methodology:** Instrument enterprise benchmark tasks with policy engines, audit trails, and approval gates.
- **Possible evaluation setup:** Score task success, policy compliance, justification quality, approval burden, and audit completeness.
- **Likely challenges:** Enterprise policies are domain-specific, ambiguous, and often hidden in organizational practice.
- **Potential contribution:** A deployment-oriented evaluation layer for enterprise browser agents.

**Possible paper ideas:**
- "Auditable Web Agents for Enterprise Workflows"
- "Approval-Aware Browser Automation in Regulated Tasks"
- "Policy Explanations for Enterprise LLM Agents"

## Gap 10: There is no unified benchmark combining navigation, traversal, extraction, information seeking, and security

- **Observed from papers:** Navigation, extraction, information seeking, and security are covered in separate clusters: WebArena/Mind2Web, AutoScraper/Webscraper, WebGPT/WebDancer/WebSailor, and WASP/SafeArena/ST-WebAgentBench.
- **Why it matters:** Real agents may need to browse, traverse, extract, cite, and act safely in one session.
- **Current representative papers:** WebArena, VisualWebArena, WebWalker, AutoScraper, Webscraper, Mind2Web 2, WASP, ST-WebAgentBench, SafeArena.
- **What is missing:** Integrated tasks with benign and adversarial variants across multiple agent capabilities.
- **Actionable research direction:** Propose an integrated benchmark with task success, evidence quality, extraction accuracy, safety, privacy, and trajectory-risk metrics.
- **Possible research questions:**
  - RQ1: Can one benchmark evaluate task success, evidence quality, extraction accuracy, safety, and privacy?
  - RQ2: How should scoring balance completion and risk?
  - RQ3: Can the same task have safe and adversarial variants?
- **Possible methodology:** Create scenario families where agents must research a question, traverse sites, extract structured data, and avoid malicious or sensitive content.
- **Possible evaluation setup:** Multi-objective scores for completion, extraction F1, citation quality, policy compliance, privacy leakage, and adversarial robustness.
- **Likely challenges:** Scoring complexity, task authoring cost, and ensuring that safety penalties are fair across agent types.
- **Potential contribution:** A benchmark that evaluates web agents as integrated systems rather than isolated capabilities.

**Possible paper ideas:**
- "WebAgent360: Unified Evaluation of Browsing, Extraction, Research, and Safety"
- "Safe Deep Research Tasks for Browser Agents"
- "Multi-Objective Scoring for Autonomous Web Agents"

## Gap 11: Economic, ethical, and policy dimensions of AI crawlers/scrapers are underdeveloped

- **Observed from papers:** Canary Tokens raises governance questions, and AutoScraper/Webscraper improve scraping capability, but the collection has little policy or economics analysis.
- **Why it matters:** AI crawlers affect publishers, site owners, users, researchers, model providers, and infrastructure operators.
- **Current representative papers:** AutoScraper, Webscraper, Canary Tokens, When AI Meets the Web, Unsafe LLM-Based Search.
- **What is missing:** Technical mechanisms for consent, attribution, auditability, and machine-readable preferences for AI agents.
- **Actionable research direction:** Add a research track connecting technical scraper detection with governance, consent, attribution, and auditability.
- **Possible research questions:**
  - RQ1: How can website preferences be represented in machine-readable form for AI agents?
  - RQ2: Can crawler agents produce audit trails proving compliance?
  - RQ3: What technical controls support responsible academic crawling?
- **Possible methodology:** Design policy descriptors for websites and evaluate whether agents can comply while completing research/extraction goals.
- **Possible evaluation setup:** Measure policy comprehension, compliant coverage, attribution quality, audit-log completeness, and impact on site load.
- **Likely challenges:** No single stakeholder defines legitimate scraping, and machine-readable policies may not map cleanly to law or norms.
- **Potential contribution:** A technical governance layer for responsible AI crawling.

**Possible paper ideas:**
- "Machine-Readable Website Preferences for AI Crawlers"
- "Auditable Academic Crawling with LLM Agents"
- "Responsible AI Scraping: Metrics, Policies, and Enforcement"

## Gap 12: Evaluation often rewards final success but not trajectory quality

- **Observed from papers:** Many benchmarks score final answers or task completion; WebVoyager and Mind2Web 2 introduce judge-based evaluation, while safety benchmarks add policy metrics.
- **Why it matters:** Two agents with the same final answer may differ radically in risk, unnecessary exposure, privacy leakage, cost, and recoverability.
- **Current representative papers:** WebVoyager, Mind2Web 2, BrowserGym, ST-WebAgentBench, SafeArena, WASP.
- **What is missing:** Trajectory-level metrics for action minimality, recoverability, unnecessary exposure, unsafe intermediate states, provenance, and policy margins.
- **Actionable research direction:** Develop metrics for action minimality, recoverability, unnecessary exposure, unsafe intermediate states, and evidence provenance.
- **Possible research questions:**
  - RQ1: Can two agents with the same final answer differ in risk?
  - RQ2: How should benchmark scores penalize dangerous intermediate actions?
  - RQ3: Can trajectory-level judging be made reliable?
- **Possible methodology:** Instrument browser traces and apply rule-based plus model-based judges to classify unnecessary, risky, or unsupported actions.
- **Possible evaluation setup:** Pair final-task scores with trajectory-risk scores, action efficiency, provenance completeness, recovery from errors, and human audit ratings.
- **Likely challenges:** Human agreement on trajectory quality may be low, and model judges can inherit biases or miss subtle risks.
- **Potential contribution:** A richer evaluation standard that rewards safe, efficient, auditable web-agent behavior.

**Possible paper ideas:**
- "Trajectory Quality Metrics for Autonomous Web Agents"
- "Risk-Aware Scoring for Browser-Agent Benchmarks"
- "Auditing the Path, Not Just the Answer: Evaluating Web-Agent Behavior"
