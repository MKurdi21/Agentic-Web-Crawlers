# Problem-Approach Matrix

## Purpose

This matrix maps the local literature collection across two dimensions:

- **Columns:** research problems or questions.
- **Rows:** solution approaches.
- **Cells:** papers in this repository that use the approach for the problem.

The matrix is a synthesis, not a formal taxonomy. Empty cells use `-`, and populated cells use short paper names rather than full citations. See [papers.md](papers.md) for detailed summaries and [gaps_and_research_directions.md](gaps_and_research_directions.md) for research opportunities implied by sparse cells.

## A. Compact Matrix

| Approach | General tasks | Navigation | Traversal | Info seeking | Extraction | Visual | Enterprise | Benchmarks | Training | Prompt injection | Tool / exfiltration | Safety / trust | Scraper defense | Web app security |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prompting / ReAct loops | ReAct; WebShop; WebArena; WebVoyager | ReAct; AutoWebGLM; WebVoyager | WebWalker; LASER | WebGPT; WebDancer; WebSailor | Webscraper | WebVoyager; SeeAct | WorkArena | WebShop; WebArena | WebGPT | - | - | SafeArena | - | AWE |
| DOM / HTML browser control | Mind2Web; AutoWebGLM; WebArena | AutoWebGLM; WebLINX; BrowserGym | WebWalker; Go-Browse | Mind2Web 2 | AutoScraper | SeeAct | WorkArena; WorkArena++ | Mind2Web; WebArena; BrowserGym | WebLINX; AutoWebGLM | WASP; WARD | ACE | ST-WebAgentBench | - | YuraScanner |
| Visual grounding | SeeAct; WebVoyager | WebVoyager; SeeAct | BEARCUBS; MMInA | BEARCUBS; MMInA | Webscraper | SeeAct; WebVoyager; VisualWebArena; MMInA | WorkArena++ | VisualWebArena; MMInA; BEARCUBS | - | WASP; WARD | - | ST-WebAgentBench | - | - |
| State-space exploration / planning | LASER; WebArena | LASER | LASER; WebWalker | WebSailor | - | - | WorkArena++ | - | - | - | - | - | - | AWE |
| Demonstration / imitation learning | WebGPT; Mind2Web; WebLINX | WebLINX; AutoWebGLM | - | WebGPT | - | - | WorkArena++ | Mind2Web; WebLINX | WebGPT; WebLINX; AutoWebGLM | - | - | - | - | - |
| RL / self-improvement | WebShop; AutoWebGLM | AutoWebGLM | - | WebDancer; WebSailor | - | - | - | WebShop | WebShop; AutoWebGLM; WebDancer | - | - | - | - | - |
| Synthetic trajectory generation | Go-Browse; WorkArena++ | Go-Browse | Go-Browse | WebDancer; WebSailor | - | - | WorkArena++ | WorkArena++ | Go-Browse; WorkArena++; WebDancer; WebSailor | WARD | - | ST-WebAgentBench | - | AWE |
| Benchmark / environment design | WebShop; Mind2Web; WebArena | BrowserGym; WebArena | WebWalker | BrowseComp; BEARCUBS; Mind2Web 2; MMInA | - | VisualWebArena; MMInA | WorkArena; WorkArena++ | WebShop; Mind2Web; WebArena; VisualWebArena; BrowserGym; WorkArena; BEARCUBS; BrowseComp | - | WASP; Formalizing Prompt Injection | ToolHijacker | SafeArena; ST-WebAgentBench | - | YuraScanner |
| Agent-as-a-judge evaluation | WebVoyager | WebVoyager | - | Mind2Web 2 | - | WebVoyager | - | Mind2Web 2; WebVoyager | - | - | - | - | - | - |
| Hierarchical / modular agents | AutoWebGLM; LASER | AutoWebGLM; LASER | WebWalker | WebDancer; WebSailor | Webscraper | SeeAct | WorkArena++ | - | AutoWebGLM; WebDancer | - | ACE | ST-WebAgentBench | - | AWE; YuraScanner |
| Tool-use / API orchestration | ReAct | BrowserGym | - | WebGPT | Webscraper | - | WorkArena | - | Toolformer; Gorilla | ToolHijacker | ACE; ToolHijacker | ST-WebAgentBench | - | AWE |
| Link-following / traversal policies | - | LASER | WebWalker; Go-Browse; EvoCrawl | WebWalker; BEARCUBS | - | MMInA | - | WebWalker; BEARCUBS | Go-Browse | - | - | - | - | YuraScanner; EvoCrawl |
| Scraper-generation pipelines | - | - | - | - | AutoScraper; Webscraper | Webscraper | - | - | AutoScraper | - | - | - | AutoScraper; Webscraper | - |
| Safety benchmark design | - | - | - | Unsafe LLM-Based Search | - | - | ST-WebAgentBench | SafeArena; ST-WebAgentBench; WASP | - | WASP | ST-WebAgentBench | SafeArena; ST-WebAgentBench | - | - |
| Prompt-injection attack generation | - | - | - | Overcoming the Retrieval Barrier | - | - | - | Formalizing Prompt Injection; WASP | - | Not What You've Signed Up For; Formalizing Prompt Injection; WASP; Overcoming the Retrieval Barrier; When AI Meets the Web | ToolHijacker | WASP | - | - |
| Prompt-injection defenses | - | - | - | Unsafe LLM-Based Search | - | - | - | Formalizing Prompt Injection | WARD | WARD; RENNERVATE; Formalizing Prompt Injection | ACE | ST-WebAgentBench | - | - |
| Permissioning / security architecture | - | - | - | - | - | - | ST-WebAgentBench | - | - | ACE | ACE; ToolHijacker | ST-WebAgentBench | - | - |
| Canary-token / scraper defense | - | - | - | - | - | - | - | - | - | - | - | - | Canary Tokens | - |
| LLM-guided web app scanning | - | - | YuraScanner; AWE; EvoCrawl | - | - | - | - | - | - | - | - | - | - | YuraScanner; AWE |

## B. Split Matrices

### Capability and Navigation Matrix

| Approach | General web task completion | Web navigation / browser automation | Multimodal visual interaction | Enterprise web workflows |
|---|---|---|---|---|
| Prompting / ReAct loops | ReAct; WebShop; WebArena; WebVoyager | ReAct; AutoWebGLM; WebVoyager | WebVoyager; SeeAct | WorkArena |
| DOM / HTML browser control | Mind2Web; AutoWebGLM; WebArena | AutoWebGLM; WebLINX; BrowserGym | SeeAct | WorkArena; WorkArena++ |
| Visual grounding | SeeAct; WebVoyager | WebVoyager; SeeAct | SeeAct; WebVoyager; VisualWebArena; MMInA | WorkArena++ |
| State-space exploration / planning | LASER; WebArena | LASER | - | WorkArena++ |
| Demonstration learning | WebGPT; Mind2Web; WebLINX | WebLINX; AutoWebGLM | - | WorkArena++ |
| Hierarchical / modular agents | AutoWebGLM; LASER | AutoWebGLM; LASER | SeeAct | WorkArena++ |
| Tool-use orchestration | ReAct | BrowserGym | - | WorkArena |

### Information Seeking, Traversal, and Scraping Matrix

| Approach | Web traversal / site exploration | Web information seeking / deep research | Web scraping / structured extraction | AI scraper detection or crawler defense |
|---|---|---|---|---|
| Prompting / ReAct loops | WebWalker; LASER | WebGPT; WebDancer; WebSailor | Webscraper | - |
| DOM / HTML browser control | WebWalker; Go-Browse | Mind2Web 2 | AutoScraper | - |
| Visual grounding | BEARCUBS; MMInA | BEARCUBS; MMInA | Webscraper | - |
| State-space exploration | LASER; WebWalker | WebSailor | - | - |
| Synthetic trajectory generation | Go-Browse | WebDancer; WebSailor | - | - |
| Link-following policies | WebWalker; Go-Browse; EvoCrawl | WebWalker; BEARCUBS | - | - |
| Scraper-generation pipelines | - | - | AutoScraper; Webscraper | AutoScraper; Webscraper |
| Canary-token defense | - | - | - | Canary Tokens |

### Benchmarking and Training Matrix

| Approach | Benchmarking and reproducible evaluation | Learning / training web agents | Agent-as-a-judge evaluation |
|---|---|---|---|
| Benchmark / environment design | WebShop; Mind2Web; WebArena; VisualWebArena; BrowserGym; WorkArena; BEARCUBS; BrowseComp; WebWalker; MMInA | - | - |
| Demonstration learning | Mind2Web; WebLINX | WebGPT; WebLINX; AutoWebGLM | - |
| Reinforcement learning / self-improvement | WebShop | WebShop; AutoWebGLM; WebDancer | - |
| Synthetic trajectory generation | WorkArena++ | Go-Browse; WorkArena++; WebDancer; WebSailor | - |
| Agent-as-a-judge evaluation | Mind2Web 2; WebVoyager | - | Mind2Web 2; WebVoyager |
| Safety benchmark design | SafeArena; ST-WebAgentBench; WASP | - | - |

### Security and Safety Matrix

| Approach | Prompt injection / malicious webpages | Unsafe tool use / data exfiltration | Web-agent safety and trustworthiness | Web app security testing |
|---|---|---|---|---|
| Safety benchmark design | WASP | ST-WebAgentBench | SafeArena; ST-WebAgentBench | - |
| Prompt-injection attack generation | Not What You've Signed Up For; Formalizing Prompt Injection; WASP; Overcoming the Retrieval Barrier; When AI Meets the Web | ToolHijacker | WASP | - |
| Prompt-injection defenses | WARD; RENNERVATE; Formalizing Prompt Injection | ACE | ST-WebAgentBench | - |
| Permissioning / security architecture | ACE | ACE; ToolHijacker | ST-WebAgentBench | - |
| DOM / HTML control | WASP; WARD | ACE | ST-WebAgentBench | YuraScanner |
| Visual grounding | WASP; WARD | - | ST-WebAgentBench | - |
| LLM-guided web app scanning | - | - | - | YuraScanner; AWE |
| Stateful web exploration | - | - | - | YuraScanner; AWE; EvoCrawl |

## Matrix Interpretation

The densest coverage is in **general web task completion**, **browser automation**, and **benchmarking**. WebShop, Mind2Web, WebArena, VisualWebArena, BrowserGym, WorkArena, WorkArena++, BEARCUBS, BrowseComp, MMInA, and WebWalker show that the field has invested heavily in defining tasks and environments. This is healthy, but it also means many papers diagnose capability gaps more than they solve deployment problems.

The dominant approaches are **ReAct-style reasoning-action loops**, **DOM/HTML browser control**, **visual grounding**, **demonstration learning**, and **benchmark construction**. Most core systems still use an observe-think-act loop, either over HTML/DOM representations, screenshots, accessibility trees, or some combination. Multimodal systems are now central because many real webpages cannot be understood reliably from text alone.

Several areas are mostly benchmarked but not solved. **Live-web information seeking** has BrowseComp, BEARCUBS, Mind2Web 2, MMInA, WebDancer, and WebSailor, but open questions remain around source trust, adversarial pages, citation provenance, and stopping criteria. **Enterprise automation** has WorkArena and WorkArena++, but auditability, approval, and compliance are only beginning to appear through ST-WebAgentBench.

Security coverage is strongest for **prompt injection**. Not What You've Signed Up For, Formalizing Prompt Injection, WASP, WARD, RENNERVATE, Overcoming the Retrieval Barrier, ToolHijacker, When AI Meets the Web, and ACE create a dense attack/defense cluster. The field has credible benchmarks and defenses here, although integration with real browser permissions and enterprise policy is still incomplete.

Sparse but promising problem-approach combinations include **LLM-guided crawling plus safety policies**, **scraper generation plus consent/privacy constraints**, **live-web benchmarks plus adversarial webpage variants**, **trajectory-quality scoring plus security risk**, and **browser-agent containment plus human approval**. These combinations look especially actionable because there are enough nearby papers to cite, but not enough direct work to make the problem saturated.

The largest structural gap is that the collection has separate islands: navigation benchmarks, information-seeking benchmarks, scraping systems, prompt-injection security, and web app scanning. A mature research agenda would connect these islands into evaluation suites where the same agent must browse, traverse, extract, cite, obey policy, preserve privacy, and resist malicious content in one coherent task setting.
