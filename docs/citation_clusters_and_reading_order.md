# Citation Clusters and Recommended Reading Order

## Citation Clusters

### 1. Foundational Reasoning/Action and Browsing

- **Papers:** WebGPT; ReAct; WebShop.
- **When to cite:** Use this cluster when introducing the idea that LLMs can interleave reasoning, external actions, browsing, and evidence-backed answering.
- **How they relate:** WebGPT demonstrates browser-assisted question answering with human feedback; ReAct gives the durable reasoning-action loop; WebShop provides an early grounded web interaction environment.
- **Limitation:** These works predate many modern browser-agent safety concerns and do not fully capture live-web adversarial behavior.

### 2. Core Web-Agent Benchmarks

- **Papers:** WebShop; Mind2Web; WebArena; BrowserGym; BEARCUBS; BrowseComp.
- **When to cite:** Use this cluster when discussing standard evaluation environments and task suites for web agents.
- **How they relate:** WebShop is a controlled shopping simulator; Mind2Web broadens to many websites; WebArena provides realistic self-hosted sites; BrowserGym standardizes environments; BEARCUBS and BrowseComp push toward live or difficult browsing tasks.
- **Limitation:** Benchmarks differ in realism, reproducibility, and scoring, making direct comparisons hard.

### 3. Multimodal Browser Agents

- **Papers:** SeeAct; WebVoyager; VisualWebArena; MMInA; BEARCUBS.
- **When to cite:** Use this cluster when arguing that screenshots, visual layout, images, and rendered page state matter for web agents.
- **How they relate:** SeeAct focuses on grounding GPT-4V-style models; WebVoyager builds an end-to-end multimodal agent; VisualWebArena evaluates visual web tasks; MMInA and BEARCUBS add multimodal information-seeking settings.
- **Limitation:** Visual capability does not automatically imply robustness to visual prompt injection or deceptive UI.

### 4. Information Seeking and Deep Research Agents

- **Papers:** WebGPT; WebDancer; WebSailor; Mind2Web 2; BrowseComp; BEARCUBS; MMInA.
- **When to cite:** Use this cluster when framing autonomous browsing for answers, citations, multi-hop research, and deep information seeking.
- **How they relate:** WebGPT is the early browser-assisted QA foundation; WebDancer and WebSailor emphasize training for autonomous information seeking; Mind2Web 2 adds agent-as-a-judge evaluation; BrowseComp, BEARCUBS, and MMInA supply harder browsing tasks.
- **Limitation:** Provenance, source trust, adversarial retrieval, and privacy leakage remain weakly measured.

### 5. Web Traversal and Site Exploration

- **Papers:** WebWalker; Go-Browse; LASER; YuraScanner; EvoCrawl.
- **When to cite:** Use this cluster when the focus is link following, state exploration, crawler policies, or reaching deep website states.
- **How they relate:** LASER introduces state-space exploration for navigation; WebWalker separates vertical site traversal from generic search; Go-Browse uses structured exploration for training data; YuraScanner applies LLM task execution to web app scanning; EvoCrawl is a non-LLM evolutionary crawler reference.
- **Limitation:** This cluster is still smaller than the task-completion benchmark literature and lacks a unified crawling benchmark.

### 6. Web Scraping and Structured Extraction

- **Papers:** AutoScraper; Webscraper; Canary Tokens.
- **When to cite:** Use this cluster for LLM-based scraper generation, dynamic structured extraction, and scraper detection/governance.
- **How they relate:** AutoScraper generates reusable scrapers from HTML understanding; Webscraper uses multimodal navigation for index-content extraction; Canary Tokens studies detection of AI scraping.
- **Limitation:** Capability and governance are mostly separate; few papers evaluate policy-aware or privacy-preserving scraper agents.

### 7. Enterprise Browser Automation

- **Papers:** WorkArena; WorkArena++; BrowserGym; ST-WebAgentBench; ACE.
- **When to cite:** Use this cluster when discussing web agents in enterprise software, knowledge-work automation, and policy-sensitive workflows.
- **How they relate:** WorkArena starts with ServiceNow-style tasks; WorkArena++ adds compositional planning; BrowserGym provides infrastructure; ST-WebAgentBench adds safety/trust policies; ACE contributes security architecture ideas.
- **Limitation:** Real enterprise deployment also requires auditability, approvals, access control, and compliance integration.

### 8. Web-Agent Security Benchmarks

- **Papers:** WASP; SafeArena; ST-WebAgentBench; Unsafe LLM-Based Search.
- **When to cite:** Use this cluster when evaluating web-agent safety, malicious task compliance, prompt-injection robustness, or risky AI search.
- **How they relate:** WASP focuses on prompt injection in web-agent tasks; SafeArena measures harmful-task compliance; ST-WebAgentBench evaluates policy-aware enterprise trust; Unsafe LLM-Based Search studies malicious search results.
- **Limitation:** The benchmarks are complementary but not unified across navigation, privacy, prompt injection, and misuse.

### 9. Prompt-Injection Attacks

- **Papers:** Not What You've Signed Up For; Formalizing and Benchmarking Prompt Injection; Overcoming the Retrieval Barrier; ToolHijacker; When AI Meets the Web; WASP.
- **When to cite:** Use this cluster when describing indirect prompt injection, malicious webpage content, retrieval-optimized attacks, or tool-selection compromise.
- **How they relate:** Not What You've Signed Up For gives early real-world framing; Formalizing Prompt Injection gives a benchmark/formalism; Overcoming the Retrieval Barrier solves retrieval realism; ToolHijacker targets tool selection; When AI Meets the Web studies chatbot plugins and scraped web context; WASP targets web agents.
- **Limitation:** Prompt injection is heavily covered, but other web threats are comparatively thin.

### 10. Prompt-Injection Defenses

- **Papers:** WARD; RENNERVATE; ACE; Formalizing and Benchmarking Prompt Injection; Unsafe LLM-Based Search.
- **When to cite:** Use this cluster when comparing guard models, sanitization, architecture-level separation, and mitigation strategies.
- **How they relate:** WARD is web-agent-specific; RENNERVATE uses attention features; ACE separates trusted planning from untrusted execution; Formalizing Prompt Injection compares defenses; Unsafe LLM-Based Search studies mitigations for malicious search exposure.
- **Limitation:** Defenses still need integration with browser permissions, provenance tracking, human approval, and action-level policy enforcement.

### 11. Tool-Use Security and Containment

- **Papers:** ACE; ToolHijacker; ST-WebAgentBench; Gorilla; Toolformer; ReAct.
- **When to cite:** Use this cluster when arguing that agents need safe tool selection, permissioning, and containment.
- **How they relate:** ReAct and Toolformer motivate tool-using agents; Gorilla covers API invocation; ToolHijacker shows tool-selection attack risk; ACE and ST-WebAgentBench address policy and security controls.
- **Limitation:** The collection lacks a full browser-agent sandboxing benchmark.

### 12. AI Scraper Detection and Crawler Defense

- **Papers:** Canary Tokens; AutoScraper; Webscraper; EvoCrawl; YuraScanner.
- **When to cite:** Use this cluster when discussing AI scraper detection, crawler defense, or the dual-use nature of automated web exploration.
- **How they relate:** AutoScraper and Webscraper improve scraping capability; Canary Tokens detects AI scraping; EvoCrawl and YuraScanner explore web apps for security purposes.
- **Limitation:** Technical detection is not yet connected to a mature policy model for consent, attribution, or acceptable academic crawling.

### 13. Borderline Tool-Use / GUI-Agent Background

- **Papers:** AndroidWorld; Gorilla; Toolformer; EvoCrawl.
- **When to cite:** Use this cluster when comparing browser agents with broader GUI agents, general API/tool-use models, or non-LLM web exploration.
- **How they relate:** AndroidWorld offers mobile GUI-agent benchmarking; Toolformer and Gorilla cover tool/API use; EvoCrawl offers a non-LLM stateful web crawler baseline.
- **Limitation:** These papers are useful context but not all are directly about LLM web browsing.

## Recommended Reading Order

### New Researcher Reading Order

1. WebGPT
2. ReAct
3. WebShop
4. Mind2Web
5. WebArena
6. VisualWebArena
7. WebVoyager
8. BrowserGym
9. WebWalker
10. WASP or SafeArena

### Security-Focused Reading Order

1. Not What You've Signed Up For
2. Formalizing and Benchmarking Prompt Injection
3. WASP
4. WARD
5. RENNERVATE
6. Overcoming the Retrieval Barrier
7. ToolHijacker
8. ACE
9. SafeArena
10. ST-WebAgentBench
11. Unsafe LLM-Based Search
12. When AI Meets the Web

### Crawling/Scraping-Focused Reading Order

1. WebWalker
2. Go-Browse
3. LASER
4. AutoScraper
5. Webscraper
6. Canary Tokens
7. YuraScanner
8. EvoCrawl
9. BEARCUBS
10. MMInA

### Benchmark-Focused Reading Order

1. WebShop
2. Mind2Web
3. WebArena
4. VisualWebArena
5. BrowserGym
6. WorkArena
7. WorkArena++
8. BrowseComp
9. BEARCUBS
10. MMInA
11. WebWalker
12. SafeArena
13. ST-WebAgentBench
14. WASP

## How to Use These Clusters

Use the clusters as citation bundles rather than rigid categories. Many papers belong to multiple clusters: WebWalker is both traversal and information seeking; ST-WebAgentBench is both enterprise and security; BrowserGym is both benchmark infrastructure and a substrate for safety evaluation. When writing a related-work section, cite the cluster that matches the claim being made, then add one or two bridging papers from adjacent clusters to show the gap.
