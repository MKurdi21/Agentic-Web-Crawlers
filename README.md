# Agentic Web Agents, Web Crawling, Web Browsing, and Web-Agent Security Literature

This repository is a local literature collection on agentic AI systems that interact with the web: LLM and multimodal agents for autonomous browsing, browser automation, website traversal, information seeking, web scraping, scraper generation, and web-agent safety/security.

## Executive Summary

- **Core area:** autonomous LLM and multimodal agents that browse, traverse, scrape, search, and interact with websites.
- **Dominant literature:** benchmark construction, browser-control systems, visual web agents, and information-seeking agents.
- **Dominant security focus:** prompt injection, malicious webpages, unsafe tool use, data exfiltration, and web-agent safety benchmarks.
- **Weakest-covered areas:** LLM-guided crawling at scale, scraping governance, privacy leakage during browsing, containment/sandboxing, and live-web adversarial evaluation.
- **Best starting papers:** WebGPT, ReAct, WebShop, Mind2Web, WebArena, VisualWebArena, WebVoyager, BrowserGym, WASP, SafeArena, WARD.

## Repository Map

| File | Purpose |
|---|---|
| [docs/papers.md](docs/papers.md) | Full paper inventory and detailed summaries |
| [docs/problem_approach_matrix.md](docs/problem_approach_matrix.md) | Research problems mapped to solution approaches |
| [docs/gaps_and_research_directions.md](docs/gaps_and_research_directions.md) | Gap analysis and actionable research ideas |
| [docs/citation_clusters_and_reading_order.md](docs/citation_clusters_and_reading_order.md) | Citation clusters and recommended reading order |
| [docs/metadata_verification.md](docs/metadata_verification.md) | Venue/source verification notes and uncertainty |

## Short Area Overview

Agentic web agents are AI systems that do more than answer questions from a static corpus. They observe webpages, decide what to do next, issue browser or tool actions, read the results, and continue over multiple steps until a task is complete. Their actions may include search queries, link traversal, clicking, typing, form submission, scrolling, UI-element selection, tool calls, citation collection, structured extraction, or manipulation of enterprise web applications.

They differ from traditional web crawlers because their unit of behavior is not simply URL discovery and page fetching. A crawler usually follows links, fetches documents, and indexes or extracts content according to fixed policies. A web agent may reason about a natural-language goal, inspect dynamic UI state, use screenshots or accessibility trees, authenticate into a task environment, recover from mistakes, and decide that a page is not useful. This makes web-agent research closer to interactive decision-making than to batch crawling.

They also differ from classic web scraping. Traditional scraping often relies on manually written wrappers, CSS selectors, APIs, or extraction rules. Agentic scraping papers ask whether an LLM or multimodal model can understand a target expressed in natural language, navigate dynamic pages, generate reusable scraper code, or extract index-content records from interactive websites. That adds flexibility, but it also raises governance questions: which data may be collected, how site preferences are honored, and how to distinguish benign research scraping from abusive automation.

They differ from search engines and generic RAG systems because they do not only retrieve a ranked list of documents or chunks. Web agents may perform multi-hop browsing, vertical traversal within a website, visual inspection, account-bound interaction, evidence tracking, and final synthesis. WebGPT and later deep-research-style systems are important because they treat browsing as an iterative action loop with source use, not only as retrieval.

LLMs and multimodal models changed this area by making it plausible to combine task understanding, planning, page interpretation, visual grounding, and tool use in one loop. ReAct provided a durable reasoning-action pattern. WebShop, Mind2Web, WebArena, VisualWebArena, WorkArena, BrowserGym, BEARCUBS, BrowseComp, WebWalker, and MMInA then made evaluation more realistic and harder. Architectures explored DOM and HTML simplification, screenshot grounding, state-space search, self-generated exploration data, trajectory training, agent-as-a-judge evaluation, and specialized information-seeking training.

Web-agent evaluation is difficult because web tasks are long-horizon, interactive, dynamic, partially observable, and often visually grounded. A final answer or task-completion score can hide brittle trajectories, unnecessary actions, privacy leakage, reliance on unstable live content, or unsafe intermediate states. Reproducible self-hosted environments improve comparability, but they can miss live-web drift and adversarial content. Live-web benchmarks are more realistic, but they are harder to maintain, version, and audit.

Web-agent security is difficult because agents consume untrusted web content while holding privileges. A browser agent may browse with accounts, fill forms, read private context, call tools, produce citations, or take external actions. Webpages, retrieved snippets, PDFs, tool descriptions, screenshots, and scraped content become possible instruction channels. The current security literature is strong on indirect prompt injection and malicious webpage content, but thinner on privacy leakage, permissioning, containment, economic abuse, crawler governance, and full-stack browser-agent security architecture.

## Paper Categories

- **Core web-agent architectures:** ReAct, AutoWebGLM, SeeAct, LASER, WebLINX, WebVoyager.
- **Benchmarks and environments:** WebShop, Mind2Web, WebArena, VisualWebArena, BrowserGym, WorkArena, WorkArena++, BEARCUBS, BrowseComp, MMInA.
- **Information-seeking / deep research agents:** WebGPT, WebDancer, WebSailor, Mind2Web 2, WebWalker.
- **Web traversal / site exploration:** WebWalker, Go-Browse, LASER, YuraScanner, EvoCrawl.
- **Web scraping / structured extraction:** AutoScraper, Webscraper.
- **Enterprise browser automation:** WorkArena, WorkArena++, BrowserGym, ST-WebAgentBench.
- **Security and safety:** WASP, WARD, SafeArena, ST-WebAgentBench, ACE, RENNERVATE, ToolHijacker, Unsafe LLM-Based Search, Canary Tokens, When AI Meets the Web, Overcoming the Retrieval Barrier, Formalizing Prompt Injection, Not What You've Signed Up For, AWE, YuraScanner.
- **Borderline but useful background:** AndroidWorld, EvoCrawl, Gorilla, Toolformer.

## Top Research Gaps

1. LLM-guided crawling is underdeveloped compared with browser-task benchmarks.
2. Scraper generation is disconnected from safety, consent, and abuse prevention.
3. Mainstream web-agent benchmarks rarely include adversarial webpages.
4. Privacy leakage during multi-step browsing is underexplored.
5. Containment and sandboxing for browser agents remain immature.
6. Live-web evaluation is realistic but hard to reproduce.
7. Long-horizon multi-site tasks are still weakly covered.
8. Security papers focus heavily on prompt injection, leaving other threats underexplored.
9. Enterprise web agents need auditability, human approval, and compliance models.
10. Evaluation often rewards final success but not trajectory quality.

See [docs/gaps_and_research_directions.md](docs/gaps_and_research_directions.md) for detailed discussion and actionable project ideas.

## Quick Reading Order

1. WebGPT and ReAct for early browsing and reasoning-action foundations.
2. WebShop, Mind2Web, and WebArena for core web-agent benchmarks.
3. SeeAct, WebVoyager, and VisualWebArena for multimodal browser agents.
4. WebLINX, BrowserGym, WorkArena, and WorkArena++ for demonstrations, standardized evaluation, and enterprise workflows.
5. AutoScraper and Webscraper for LLM-assisted scraper generation and extraction.
6. WebWalker, Go-Browse, WebDancer, WebSailor, BrowseComp, BEARCUBS, Mind2Web 2, and MMInA for traversal and deep information seeking.
7. Not What You've Signed Up For, Formalizing Prompt Injection, WASP, WARD, SafeArena, ST-WebAgentBench, ACE, and ToolHijacker for security and safety.
8. AndroidWorld, EvoCrawl, Toolformer, and Gorilla for adjacent GUI, crawling, and tool-use background.

See [docs/citation_clusters_and_reading_order.md](docs/citation_clusters_and_reading_order.md) for expanded citation clusters and specialized reading paths.

## Maintenance Notes

- PDFs are stored locally in the repository root, `Security/`, and `Borderline/`.
- Some PDFs are preprints or have venue metadata that may change after download.
- Metadata should be periodically re-verified against official proceedings, OpenReview, ACL Anthology, USENIX, NDSS, IEEE S&P, ACM, NeurIPS, ICML, ICLR, or arXiv pages.
- The problem-approach matrix is a synthesis of this local collection and should be updated whenever new papers are added.
