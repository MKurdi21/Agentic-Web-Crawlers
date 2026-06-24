# Agentic Web Agents, Web Crawling, Web Browsing, and Web-Agent Security Literature

This repository is a local literature collection on agentic AI systems that interact with the web. It covers LLM and multimodal agents for autonomous browsing, browser automation, website navigation, web traversal, web information seeking, web scraping and scraper generation, web-agent benchmark environments, and safety/security issues such as prompt injection, unsafe tool use, privacy leakage, and defenses. It also includes a small `Borderline` folder for broader tool-use, GUI-agent, and web-security-scanning work that is useful context but not always directly about LLM web agents.

The README synthesizes the local PDFs and the existing search report. PDF text extraction was successful for all 43 PDFs, but venue metadata is sometimes absent from the local PDF or appears only as preprint metadata; those cases are marked cautiously.

## Repository Overview

The collection is organized into three groups:

- `Root`: core web-agent, browsing, traversal, information-seeking, web-scraping, benchmark, and enterprise-browser papers.
- `Security`: papers about prompt injection, malicious or unsafe web content, web-agent misuse, trustworthiness, scraper detection, security architectures, and LLM-assisted web application security testing.
- `Borderline`: related work on mobile/GUI agents, evolutionary web crawling, and general LLM tool/API use.

The repository is intended as an onboarding map for researchers asking: what has been studied, what methods dominate, how evaluation is done, which papers belong together, and where the open gaps are.

## Area Overview

Agentic web agents are AI systems that do more than answer a query from a static document collection. They observe webpages, decide what to do next, issue browser or tool actions, read the results, and continue over multiple steps until a user task is complete. Their actions may include search queries, link traversal, clicking, typing, form submission, scrolling, selecting UI elements, calling tools, collecting citations, extracting structured records, or manipulating enterprise web applications.

They differ from traditional web crawlers because the unit of behavior is not simply URL discovery and page fetching. An agent may reason about a goal, inspect dynamic UI state, use screenshots or accessibility trees, authenticate into a task environment, recover from mistakes, or decide that a page is not useful. They differ from classic web scraping because the extraction target may be expressed in natural language, the website may be dynamic or interactive, and the agent may need to generate a reusable scraper rather than manually configured wrappers. They differ from search engines and generic RAG because the agent may perform multi-hop browsing, vertical site traversal, visual grounding, and task-specific interaction instead of retrieving a ranked list of documents.

LLMs and multimodal models changed the area by making it plausible to combine natural-language task understanding, planning, visual perception, DOM or accessibility-tree interpretation, and tool use in one loop. Early systems such as WebGPT and ReAct showed the value of interleaving reasoning and action. Later benchmarks such as WebShop, Mind2Web, WebArena, VisualWebArena, WorkArena, BrowserGym, BEARCUBS, BrowseComp, WebWalkerQA, and MMInA made the evaluation problem more realistic and harder. Agent architectures then explored HTML simplification, state-space search, multimodal grounding, self-generated exploration data, trajectory training, agent-as-a-judge evaluation, and specialized information-seeking training.

The main capability categories in this collection are:

- Browsing and navigation: completing user tasks by controlling a browser or browser-like environment.
- Web task completion: shopping, account management, form filling, forum/wiki/git tasks, and enterprise workflows.
- Web traversal and information seeking: finding information buried across pages, sites, modalities, and search results.
- Scraper generation and structured extraction: producing reusable scrapers or extracting index-content records from dynamic websites.
- Benchmark environments: reproducible websites, live-web QA, browser gyms, multimodal tasks, and enterprise task suites.
- Visual web grounding: using screenshots, element candidates, and multimodal models to act on visually meaningful webpages.
- Enterprise/browser automation: ServiceNow-style knowledge-work tasks and compositional workflows.
- Safety and security: prompt injection, tool hijacking, malicious webpages, unsafe search results, misuse tasks, trust policies, canary-token scraper detection, and LLM-guided web app security scanning.

The central evaluation challenge is that web tasks are long-horizon, interactive, dynamic, partially observable, and often visually grounded. A final answer or task-completion score may hide brittle trajectories, unsafe intermediate actions, privacy leakage, or reliance on unstable live content. The central security challenge is that web agents consume untrusted web content while holding privileges: they may browse with accounts, fill forms, use tools, retrieve private context, cite URLs, or take external actions. This turns webpages, retrieved documents, tool descriptions, and scraped snippets into possible instruction channels.

## Paper Inventory

| # | Paper | Folder | Year | Venue / Source | Type | Security-related? | Main contribution | Local PDF |
|---:|---|---|---:|---|---|---|---|---|
| 1 | [AutoScraper](<AutoScraper_A_Progressive_Understanding_Web_Agent_for_Web_Scraper_Generation.pdf>) | Root | 2024 | EMNLP 2024 | Web scraping / extraction | No | LLM framework for generating reusable web scrapers using progressive HTML understanding and an executability metric. | [PDF](<AutoScraper_A_Progressive_Understanding_Web_Agent_for_Web_Scraper_Generation.pdf>) |
| 2 | [AutoWebGLM](<AutoWebGLM_A_Large_Language_Model-based_Web_Navigating_Agent.pdf>) | Root | 2024 | KDD 2024 / arXiv | Agent architecture | No | Open web-navigation agent based on HTML simplification, human-AI browsing traces, curriculum learning, and RL bootstrapping. | [PDF](<AutoWebGLM_A_Large_Language_Model-based_Web_Navigating_Agent.pdf>) |
| 3 | [BEARCUBS](<BEARCUBS_A_benchmark_for_computer-using_web_agents.pdf>) | Root | 2025 | COLM 2025 | Benchmark / environment | No | Live-web benchmark of 111 computer-use information-seeking questions with human-validated trajectories. | [PDF](<BEARCUBS_A_benchmark_for_computer-using_web_agents.pdf>) |
| 4 | [BrowseComp](<BrowseComp_A_Simple_Yet_Challenging_Benchmark_for_Browsing_Agents.pdf>) | Root | 2025 | arXiv / OpenAI | Benchmark / environment | No | 1,266 hard-to-find browsing questions with short verifiable answers for measuring deep browsing ability. | [PDF](<BrowseComp_A_Simple_Yet_Challenging_Benchmark_for_Browsing_Agents.pdf>) |
| 5 | [Go-Browse](<Go-Browse_Training_Web_Agents_with_Structured_Exploration.pdf>) | Root | 2026 | ICLR 2026 | Training / data generation | No | Structured web exploration as graph search for collecting diverse browser-agent trajectories at scale. | [PDF](<Go-Browse_Training_Web_Agents_with_Structured_Exploration.pdf>) |
| 6 | [SeeAct / GPT-4V is a Generalist Web Agent](<GPT-4V(ision)_is_a_Generalist_Web_Agent_if_Grounded.pdf>) | Root | 2024 | ICML 2024 | Agent architecture | No | Uses multimodal models for visual website grounding and element selection across arbitrary websites. | [PDF](<GPT-4V(ision)_is_a_Generalist_Web_Agent_if_Grounded.pdf>) |
| 7 | [LASER](<LASER_LLM_Agent_with_State-Space_Exploration_for_Web_Navigation.pdf>) | Root | 2023 | arXiv / OpenReview | Agent architecture | No | Adds state-space exploration to LLM web navigation to recover from mistakes and reason beyond forward-only demonstrations. | [PDF](<LASER_LLM_Agent_with_State-Space_Exploration_for_Web_Navigation.pdf>) |
| 8 | [Mind2Web 2](<Mind2Web_2_Evaluating_Agentic_Search_with_Agent-as-a-Judge.pdf>) | Root | 2025 | arXiv | Information seeking | No | Evaluates agentic search and deep-research-style browsing with an agent-as-a-judge methodology. | [PDF](<Mind2Web_2_Evaluating_Agentic_Search_with_Agent-as-a-Judge.pdf>) |
| 9 | [Mind2Web](<Mind2Web_Towards_a_Generalist_Agent_for_the_Web.pdf>) | Root | 2023 | NeurIPS 2023 Datasets and Benchmarks | Benchmark / environment | No | Large generalist web-agent dataset with over 2,000 tasks from 137 websites and 31 domains. | [PDF](<Mind2Web_Towards_a_Generalist_Agent_for_the_Web.pdf>) |
| 10 | [MMInA](<MMInA_Benchmarking_Multihop_Multimodal_Internet_Agents.pdf>) | Root | 2025 | Findings of ACL 2025 | Benchmark / environment | No | Multihop multimodal internet-agent benchmark over evolving real-world websites. | [PDF](<MMInA_Benchmarking_Multihop_Multimodal_Internet_Agents.pdf>) |
| 11 | [ReAct](<ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf>) | Root | 2023 | ICLR 2023 | Tool-use / general agent background | Yes — security-relevant | Foundational reasoning-action prompting method evaluated on QA and interactive tasks including WebShop. | [PDF](<ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf>) |
| 12 | [BrowserGym](<The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf>) | Root | 2025 | TMLR / OpenReview | Benchmark / environment | Yes — security-relevant | Unified gym-like ecosystem for web-agent environments and reproducible browser-agent evaluation. | [PDF](<The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf>) |
| 13 | [VisualWebArena](<VisualWebArena_Evaluating_Multimodal_Agents_on_Realistic_Visual_Web_Tasks.pdf>) | Root | 2024 | ACL 2024 | Benchmark / environment | No | Realistic visually grounded web tasks requiring screenshots and web actions. | [PDF](<VisualWebArena_Evaluating_Multimodal_Agents_on_Realistic_Visual_Web_Tasks.pdf>) |
| 14 | [WebArena](<WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf>) | Root | 2024 | ICLR 2024 | Benchmark / environment | Yes — security-relevant | Reproducible self-hosted realistic web environment for autonomous agents. | [PDF](<WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf>) |
| 15 | [WebDancer](<WebDancer_Towards_Autonomous_Information_Seeking_Agency.pdf>) | Root | 2025 | arXiv | Information seeking | No | Data-centric training pipeline for autonomous information-seeking agents. | [PDF](<WebDancer_Towards_Autonomous_Information_Seeking_Agency.pdf>) |
| 16 | [WebGPT](<WebGPT_Browser-assisted_question-answering_with_human_feedback.pdf>) | Root | 2021 | arXiv / OpenAI | Information seeking | Yes — security-relevant | Browser-assisted long-form QA trained with imitation learning and human feedback. | [PDF](<WebGPT_Browser-assisted_question-answering_with_human_feedback.pdf>) |
| 17 | [WebLINX](<WebLINX_Real-World_Website_Navigation_with_Multi-Turn_Dialogue.pdf>) | Root | 2024 | ICML 2024 | Training / data generation | No | 100K interactions from 2,300 demonstrations for multi-turn conversational web navigation. | [PDF](<WebLINX_Real-World_Website_Navigation_with_Multi-Turn_Dialogue.pdf>) |
| 18 | [WebSailor](<WebSailor_Navigating_Super-human_Reasoning_for_Web_Agent.pdf>) | Root | 2025 | arXiv | Information seeking | No | Training recipe for uncertainty reduction and superhuman reasoning on difficult web information-seeking tasks. | [PDF](<WebSailor_Navigating_Super-human_Reasoning_for_Web_Agent.pdf>) |
| 19 | [Webscraper](<Webscraper_Leverage_Multimodal_Large_Language_Models_for_Index-Content_Web_Scraping.pdf>) | Root | 2026 | arXiv | Web scraping / extraction | No | MLLM-based framework for dynamic index-content web scraping with navigation and specialized tools. | [PDF](<Webscraper_Leverage_Multimodal_Large_Language_Models_for_Index-Content_Web_Scraping.pdf>) |
| 20 | [WebShop](<WebShop_Towards_Scalable_Real-World_Web_Interaction_with_Grounded_Language_Agents.pdf>) | Root | 2022 | NeurIPS 2022 | Benchmark / environment | No | Simulated e-commerce environment with 1.18M products and 12,087 natural-language shopping instructions. | [PDF](<WebShop_Towards_Scalable_Real-World_Web_Interaction_with_Grounded_Language_Agents.pdf>) |
| 21 | [WebVoyager](<WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models.pdf>) | Root | 2024 | ACL 2024 | Agent architecture | No | End-to-end multimodal web agent evaluated on real websites with GPT-4V-based trajectory judging. | [PDF](<WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models.pdf>) |
| 22 | [WebWalker](<WebWalker_Benchmarking_LLMs_in_Web_Traversal.pdf>) | Root | 2025 | ACL 2025 | Information seeking | No | WebWalkerQA benchmark and explore-critic framework for vertical site traversal. | [PDF](<WebWalker_Benchmarking_LLMs_in_Web_Traversal.pdf>) |
| 23 | [WorkArena](<WorkArena_How_Capable_are_WebAgents_at_Solving_Common_Knowledge_Work_Tasks.pdf>) | Root | 2024 | ICML 2024 | Benchmark / environment | No | Enterprise browser benchmark with 33 ServiceNow-based knowledge-work tasks and BrowserGym support. | [PDF](<WorkArena_How_Capable_are_WebAgents_at_Solving_Common_Knowledge_Work_Tasks.pdf>) |
| 24 | [WorkArena++](<WorkArena_Towards_Compositional_Planning_and_Reasoning-based_Common_Knowledge_Work_Tasks.pdf>) | Root | 2024 | NeurIPS 2024 | Benchmark / environment | No | 682 compositional enterprise tasks evaluating planning, reasoning, retrieval, and contextual understanding. | [PDF](<WorkArena_Towards_Compositional_Planning_and_Reasoning-based_Common_Knowledge_Work_Tasks.pdf>) |
| 25 | [ACE](<Security/ACE_A_Security_Architecture_for_LLM-Integrated_App_Systems.pdf>) | Security | 2026 | NDSS 2026 | Security defense | Yes — direct security paper | Security architecture for LLM-integrated app systems separating trusted planning from untrusted execution. | [PDF](<Security/ACE_A_Security_Architecture_for_LLM-Integrated_App_Systems.pdf>) |
| 26 | [RENNERVATE](<Security/Attention_is_All_You_Need_to_Defend_Against_Indirect_Prompt_Injection_Attacks_in_LLMs.pdf>) | Security | 2026 | NDSS 2026 | Security defense | Yes — direct security paper | Attention-feature defense for token-level detection and sanitization of indirect prompt injection. | [PDF](<Security/Attention_is_All_You_Need_to_Defend_Against_Indirect_Prompt_Injection_Attacks_in_LLMs.pdf>) |
| 27 | [AWE](<Security/AWE_Adaptive_Agents_for_Dynamic_Web_Penetration_Testing.pdf>) | Security | 2026 | Unclear from local PDF | Agent architecture | Yes — direct security paper | Memory-augmented multi-agent framework for dynamic web penetration testing. | [PDF](<Security/AWE_Adaptive_Agents_for_Dynamic_Web_Penetration_Testing.pdf>) |
| 28 | [Formalizing and Benchmarking Prompt Injection](<Security/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf>) | Security | 2024 | USENIX Security 2024 | Security attack | Yes — direct security paper | Formal framework and benchmark comparing prompt-injection attacks and defenses across tasks and LLMs. | [PDF](<Security/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf>) |
| 29 | [Canary Tokens for AI Web Scrapers](<Security/Identifying_AI_Web_Scrapers_Using_Canary_Tokens.pdf>) | Security | 2026 | arXiv | Security defense | Yes — direct security paper | Detects AI web scrapers by planting canary tokens and querying LLM-backed systems for leakage. | [PDF](<Security/Identifying_AI_Web_Scrapers_Using_Canary_Tokens.pdf>) |
| 30 | [Not What You've Signed Up For](<Security/Not_What_You've_Signed_Up_For_Compromising_Real-World_LLM-Integrated_Applications_with_Indirect_Prompt_Injection.pdf>) | Security | 2023 | ACM AISec 2023 | Security attack | Yes — direct security paper | Early taxonomy and demonstrations of indirect prompt injection against LLM-integrated applications. | [PDF](<Security/Not_What_You've_Signed_Up_For_Compromising_Real-World_LLM-Integrated_Applications_with_Indirect_Prompt_Injection.pdf>) |
| 31 | [Overcoming the Retrieval Barrier](<Security/Overcoming_the_Retrieval_Barrier_Indirect_Prompt_Injection_in_the_Wild_for_LLM_Systems.pdf>) | Security | 2026 | USENIX Security 2026 | Security attack | Yes — direct security paper | Black-box retrieval-optimized indirect prompt injection against RAG and agentic systems. | [PDF](<Security/Overcoming_the_Retrieval_Barrier_Indirect_Prompt_Injection_in_the_Wild_for_LLM_Systems.pdf>) |
| 32 | [ToolHijacker](<Security/Prompt_Injection_Attack_to_Tool_Selection_in_LLM_Agents.pdf>) | Security | 2026 | NDSS 2026 | Security attack | Yes — direct security paper | Prompt-injection attack against LLM-agent tool selection via malicious tool documents. | [PDF](<Security/Prompt_Injection_Attack_to_Tool_Selection_in_LLM_Agents.pdf>) |
| 33 | [SafeArena](<Security/SafeArena_Evaluating_the_Safety_of_Autonomous_Web_Agents.pdf>) | Security | 2025 | ICML 2025 / OpenReview | Safety / trustworthiness benchmark | Yes — direct security paper | Benchmark of 250 benign and 250 harmful web-agent tasks across misuse categories. | [PDF](<Security/SafeArena_Evaluating_the_Safety_of_Autonomous_Web_Agents.pdf>) |
| 34 | [ST-WebAgentBench](<Security/ST-WebAgentBench_A_Benchmark_for_Evaluating_Safety_and_Trustworthiness_in_Web_Agents.pdf>) | Security | 2026 | ICLR 2026 | Safety / trustworthiness benchmark | Yes — direct security paper | Policy-aware enterprise-grade benchmark with 375 tasks and 3,057 safety/trust policies. | [PDF](<Security/ST-WebAgentBench_A_Benchmark_for_Evaluating_Safety_and_Trustworthiness_in_Web_Agents.pdf>) |
| 35 | [Unsafe LLM-Based Search](<Security/Unsafe_LLM-Based_Search_Quantitative_Analysis_and_Mitigation_of_Safety_Risks_in_AI_Web_Search.pdf>) | Security | 2025 | USENIX Security 2025 | Safety / trustworthiness benchmark | Yes — direct security paper | Quantifies malicious URL/content risks in production AI-powered search engines and studies mitigation. | [PDF](<Security/Unsafe_LLM-Based_Search_Quantitative_Analysis_and_Mitigation_of_Safety_Risks_in_AI_Web_Search.pdf>) |
| 36 | [WARD](<Security/WARD_Adversarially_Robust_Defense_of_Web_Agents_Against_Prompt_Injections.pdf>) | Security | 2026 | arXiv | Security defense | Yes — direct security paper | Robust web-agent prompt-injection guard model trained on large-scale benign and attack data. | [PDF](<Security/WARD_Adversarially_Robust_Defense_of_Web_Agents_Against_Prompt_Injections.pdf>) |
| 37 | [WASP](<Security/WASP_Benchmarking_Web_Agent_Security_Against_Prompt_Injection_Attacks.pdf>) | Security | 2025 | arXiv / OpenReview | Safety / trustworthiness benchmark | Yes — direct security paper | End-to-end web-agent prompt-injection benchmark over realistic multi-step UI tasks. | [PDF](<Security/WASP_Benchmarking_Web_Agent_Security_Against_Prompt_Injection_Attacks.pdf>) |
| 38 | [When AI Meets the Web](<Security/When_AI_Meets_the_Web_Prompt_Injection_Risks_in_Third-Party_AI_Chatbot_Plugins.pdf>) | Security | 2026 | IEEE S&P 2026 | Security attack | Yes — direct security paper | Large-scale study of third-party chatbot plugins and prompt injection via public websites and scraped context. | [PDF](<Security/When_AI_Meets_the_Web_Prompt_Injection_Risks_in_Third-Party_AI_Chatbot_Plugins.pdf>) |
| 39 | [YuraScanner](<Security/YURASCANNER_Leveraging_LLMs_for_Task-driven_Web_App_Scanning.pdf>) | Security | 2025 | NDSS 2025 | Agent architecture | Yes — direct security paper | LLM-driven task-oriented web application scanner for reaching deeper application states. | [PDF](<Security/YURASCANNER_Leveraging_LLMs_for_Task-driven_Web_App_Scanning.pdf>) |
| 40 | [AndroidWorld](<Borderline/AndroidWorld_A_Dynamic_Benchmarking_Environment_for_Autonomous_Agents.pdf>) | Borderline | 2025 | ICLR 2025 | Borderline related | Borderline | Dynamic Android GUI-agent benchmark with 116 programmatic tasks over 20 apps. | [PDF](<Borderline/AndroidWorld_A_Dynamic_Benchmarking_Environment_for_Autonomous_Agents.pdf>) |
| 41 | [EvoCrawl](<Borderline/EvoCrawl_Exploring_Web_Application_Code_and_State_using_Evolutionary_Search.pdf>) | Borderline | 2025 | Unclear from local PDF | Borderline related | Borderline | Evolutionary web crawler for exploring web app code paths and server-side states. | [PDF](<Borderline/EvoCrawl_Exploring_Web_Application_Code_and_State_using_Evolutionary_Search.pdf>) |
| 42 | [Gorilla](<Borderline/Gorilla_Large_Language_Model_Connected_with_Massive_APIs.pdf>) | Borderline | 2024 | NeurIPS 2024 | Tool-use / general agent background | Borderline | LLM fine-tuning and retrieval framework for robust API call generation. | [PDF](<Borderline/Gorilla_Large_Language_Model_Connected_with_Massive_APIs.pdf>) |
| 43 | [Toolformer](<Borderline/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools.pdf>) | Borderline | 2023 | NeurIPS 2023 | Tool-use / general agent background | Borderline | Self-supervised method for teaching language models when and how to call tools. | [PDF](<Borderline/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools.pdf>) |

## Detailed Paper Summaries

### Core Web-Agent Papers

#### AutoWebGLM: A Large Language Model-based Web Navigating Agent

- **Local file:** [PDF](<AutoWebGLM_A_Large_Language_Model-based_Web_Navigating_Agent.pdf>)
- **Year / venue:** 2024, KDD 2024 / arXiv.
- **Problem addressed:** Real-world web navigation is difficult because HTML is verbose, actions are diverse, and open-domain tasks require multi-step decomposition.
- **Core idea / approach:** AutoWebGLM builds on ChatGLM3-6B, simplifies HTML while preserving important information, trains on hybrid human-AI browsing traces, and bootstraps with reinforcement learning and rejection sampling.
- **Evaluation setting:** AutoWebBench, a bilingual English/Chinese benchmark, plus other web-navigation benchmarks.
- **Main findings / contribution:** The paper shows that a relatively small open model can become a capable navigation agent when representation, data, and RL are tailored to web browsing.
- **Security relevance:** Security-relevant because it studies agents that take external browser actions, but security is not the focus.
- **Limitations / open questions:** The approach still depends on curated data, task distributions, and reliable HTML simplification; generalization to adversarial or safety-critical sites is not the main evaluation target.

#### SeeAct / GPT-4V(ision) is a Generalist Web Agent, if Grounded

- **Local file:** [PDF](<GPT-4V(ision)_is_a_Generalist_Web_Agent_if_Grounded.pdf>)
- **Year / venue:** 2024, ICML 2024.
- **Problem addressed:** Multimodal models can understand screenshots, but web agents also need to ground intentions into concrete UI elements and actions.
- **Core idea / approach:** SeeAct separates high-level reasoning from grounding: an LMM interprets the page visually and instructionally, while candidate elements and action choices connect model output to executable browser operations.
- **Evaluation setting:** Web navigation tasks on real websites and Mind2Web-style settings.
- **Main findings / contribution:** The paper establishes that GPT-4V-like models can serve as generalist web agents when visual reasoning is paired with explicit grounding.
- **Security relevance:** Mostly capability-oriented, but the same visual grounding surface can expose agents to visual prompt injection and deceptive UI.
- **Limitations / open questions:** Robust element grounding, ambiguous screenshots, accessibility gaps, and adversarial visual content remain open.

#### LASER: LLM Agent with State-Space Exploration for Web Navigation

- **Local file:** [PDF](<LASER_LLM_Agent_with_State-Space_Exploration_for_Web_Navigation.pdf>)
- **Year / venue:** 2023, arXiv / OpenReview.
- **Problem addressed:** Many LLM web agents act in a forward-only manner and struggle when trajectories deviate from demonstrations.
- **Core idea / approach:** LASER treats navigation as state-space exploration, allowing the agent to branch, backtrack, and evaluate alternative states instead of committing to a single action path.
- **Evaluation setting:** WebShop and Amazon-like web tasks.
- **Main findings / contribution:** State exploration improves robustness for scenarios where single-trajectory prompting is brittle.
- **Security relevance:** Indirect; exploration can increase reach into websites but may also increase the need for action constraints.
- **Limitations / open questions:** Search can be costly, and the paper does not primarily evaluate live-web volatility or adversarial pages.

#### ReAct: Synergizing Reasoning and Acting in Language Models

- **Local file:** [PDF](<ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf>)
- **Year / venue:** 2023, ICLR 2023.
- **Problem addressed:** Reasoning-only prompting lacks environmental feedback, while action-only policies can be opaque and error-prone.
- **Core idea / approach:** ReAct interleaves natural-language reasoning traces with actions, letting models decide, act, observe, and revise.
- **Evaluation setting:** Question answering, fact verification, text games, and WebShop-style interactive decision making.
- **Main findings / contribution:** ReAct became a foundational pattern for tool-using and browsing agents because it makes multi-step behavior inspectable and adaptive.
- **Security relevance:** Security-relevant because reasoning-action loops can be manipulated by untrusted observations.
- **Limitations / open questions:** ReAct alone does not define memory, verification, permissions, or robust handling of malicious observations.

#### WebLINX: Real-World Website Navigation with Multi-Turn Dialogue

- **Local file:** [PDF](<WebLINX_Real-World_Website_Navigation_with_Multi-Turn_Dialogue.pdf>)
- **Year / venue:** 2024, ICML 2024.
- **Problem addressed:** Many web-agent datasets use single-turn instructions, simulated sites, or limited websites, leaving dialogue-conditioned navigation underrepresented.
- **Core idea / approach:** WebLINX introduces conversational web navigation with 100K interactions from 2,300 expert demonstrations across more than 150 websites.
- **Evaluation setting:** Models predict browser actions in multi-turn dialogue contexts with large webpages and diverse website patterns.
- **Main findings / contribution:** The dataset supplies large-scale, real-world demonstrations for training and evaluating agents that interact with users over multiple turns.
- **Security relevance:** Mostly indirect; multi-turn agents may accumulate user context and therefore create privacy and instruction-conflict risks.
- **Limitations / open questions:** Demonstration learning does not solve live-site drift, safe action policies, or long-horizon recovery.

#### WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

- **Local file:** [PDF](<WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models.pdf>)
- **Year / venue:** 2024, ACL 2024.
- **Problem addressed:** Text-only agents and simplified simulators miss the visual, dynamic nature of real websites.
- **Core idea / approach:** WebVoyager uses a large multimodal model to observe screenshots, reason about instructions, and choose browser actions end to end.
- **Evaluation setting:** Real-world tasks collected from 15 popular websites, with automatic trajectory evaluation using GPT-4V and human agreement checks.
- **Main findings / contribution:** The paper shows strong gains from multimodal observation and proposes an evaluator for open-ended web-agent trajectories.
- **Security relevance:** Security-relevant because live visual browsing expands the attack surface to webpage content and UI manipulation.
- **Limitations / open questions:** Automatic judging can be imperfect; live websites change; safety and prompt-injection resistance are outside the main contribution.

### Benchmark and Environment Papers

#### BEARCUBS: A Benchmark for Computer-Using Web Agents

- **Local file:** [PDF](<BEARCUBS_A_benchmark_for_computer-using_web_agents.pdf>)
- **Year / venue:** 2025, COLM 2025.
- **Problem addressed:** Computer-use agents need live-web tasks that require actual browsing, multimodal interaction, and factual answer extraction.
- **Core idea / approach:** BEARCUBS provides 111 information-seeking questions with short answers and human-validated trajectories.
- **Evaluation setting:** Live web content, including tasks involving video, 3D navigation, and interactions that cannot be bypassed with text snippets.
- **Main findings / contribution:** The benchmark is small but deliberately difficult and transparent, exposing gaps between human and agent browsing.
- **Security relevance:** Indirect; live-web evaluation must manage contamination, drift, and exposure to untrusted content.
- **Limitations / open questions:** Maintaining live-web validity is labor-intensive, and the benchmark focuses on answer finding rather than safe action.

#### BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

- **Local file:** [PDF](<BrowseComp_A_Simple_Yet_Challenging_Benchmark_for_Browsing_Agents.pdf>)
- **Year / venue:** 2025, arXiv / OpenAI.
- **Problem addressed:** Existing QA benchmarks often under-measure persistent browsing and hard-to-find information retrieval.
- **Core idea / approach:** BrowseComp uses 1,266 questions whose answers are short and verifiable but require sustained web navigation.
- **Evaluation setting:** Browsing agents search the open web for entangled information.
- **Main findings / contribution:** The benchmark targets deep-browsing competence in a simple scoring format.
- **Security relevance:** Indirect; browsing open web content creates exposure to malicious or misleading sources.
- **Limitations / open questions:** It evaluates final answer accuracy more than provenance quality, safety, or the internal browsing path.

#### Mind2Web: Towards a Generalist Agent for the Web

- **Local file:** [PDF](<Mind2Web_Towards_a_Generalist_Agent_for_the_Web.pdf>)
- **Year / venue:** 2023, NeurIPS 2023 Datasets and Benchmarks.
- **Problem addressed:** Generalist web agents require diverse websites, domains, tasks, and human action traces.
- **Core idea / approach:** Mind2Web collects more than 2,000 open-ended tasks from 137 websites across 31 domains, with crowdsourced action sequences.
- **Evaluation setting:** Offline action prediction and generalization across tasks, websites, and domains.
- **Main findings / contribution:** The paper became a central dataset for evaluating whether agents can generalize beyond one site or synthetic environment.
- **Security relevance:** Not directly security-focused.
- **Limitations / open questions:** Offline snapshots simplify live interaction; visual, safety, and adversarial factors are limited compared with later benchmarks.

#### MMInA: Benchmarking Multihop Multimodal Internet Agents

- **Local file:** [PDF](<MMInA_Benchmarking_Multihop_Multimodal_Internet_Agents.pdf>)
- **Year / venue:** 2025, Findings of ACL 2025.
- **Problem addressed:** Agents must hop across evolving, multimedia websites for tasks that require more than text retrieval.
- **Core idea / approach:** MMInA defines multihop multimodal internet tasks across real-world websites and evaluates embodied internet agents.
- **Evaluation setting:** Domains include evolving sites where agents must combine multimodal observation, navigation, and reasoning.
- **Main findings / contribution:** The benchmark emphasizes compositional internet tasks and the gap between static multimodal QA and active web use.
- **Security relevance:** Indirect; multimedia web content is an untrusted input channel.
- **Limitations / open questions:** Live-web variability and benchmark maintenance remain challenging.

#### BrowserGym: The BrowserGym Ecosystem for Web Agent Research

- **Local file:** [PDF](<The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf>)
- **Year / venue:** 2025, TMLR / OpenReview.
- **Problem addressed:** Web-agent benchmarks are fragmented, making reproducibility and fair comparison difficult.
- **Core idea / approach:** BrowserGym provides a unified gym-like interface, browser control layer, action spaces, observations, and integrated tasks from multiple benchmarks.
- **Evaluation setting:** Standardized web-agent environments, including WorkArena and other browser tasks.
- **Main findings / contribution:** The ecosystem turns web-agent research into a more reproducible experimental practice.
- **Security relevance:** Security-relevant because standardized environments can support safety and attack evaluation.
- **Limitations / open questions:** A common interface does not by itself solve live-web drift, privacy, permissions, or adversarial evaluation.

#### VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks

- **Local file:** [PDF](<VisualWebArena_Evaluating_Multimodal_Agents_on_Realistic_Visual_Web_Tasks.pdf>)
- **Year / venue:** 2024, ACL 2024.
- **Problem addressed:** Text-based web benchmarks neglect tasks where visual layout, images, or rendered page state are essential.
- **Core idea / approach:** VisualWebArena extends realistic web-agent evaluation to visually grounded tasks using rendered webpages.
- **Evaluation setting:** Self-hosted realistic web environments with tasks requiring screenshot interpretation and browser actions.
- **Main findings / contribution:** The paper shows that visual grounding is necessary for many realistic tasks and that existing agents remain limited.
- **Security relevance:** Indirect, but later security papers such as WASP and WARD build on visual/HTML prompt-injection risks.
- **Limitations / open questions:** It is primarily a capability benchmark, not a robust safety benchmark.

#### WebArena: A Realistic Web Environment for Building Autonomous Agents

- **Local file:** [PDF](<WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf>)
- **Year / venue:** 2024, ICLR 2024.
- **Problem addressed:** Synthetic or simplified browser tasks do not capture realistic websites, accounts, and cross-site workflows.
- **Core idea / approach:** WebArena provides reproducible self-hosted websites, realistic user tasks, and evaluation scripts.
- **Evaluation setting:** Sites such as shopping, forums, maps, GitLab-like workflows, and administrative tasks.
- **Main findings / contribution:** WebArena is a foundational benchmark for autonomous web agents because it balances realism and reproducibility.
- **Security relevance:** Security-relevant substrate; agents act in realistic websites, but adversarial content is not the core focus.
- **Limitations / open questions:** Static self-hosted sites improve reproducibility but underrepresent live-web change and adversarial pages.

#### WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents

- **Local file:** [PDF](<WebShop_Towards_Scalable_Real-World_Web_Interaction_with_Grounded_Language_Agents.pdf>)
- **Year / venue:** 2022, NeurIPS 2022.
- **Problem addressed:** Language agents need scalable, grounded interactive environments with realistic language and reward signals.
- **Core idea / approach:** WebShop simulates an e-commerce website with 1.18 million products and 12,087 crowdsourced shopping instructions.
- **Evaluation setting:** Agents search, navigate, compare, customize, and choose products.
- **Main findings / contribution:** It provided an early, scalable benchmark for grounded web interaction and supported imitation/RL-style agent training.
- **Security relevance:** Not directly security-focused.
- **Limitations / open questions:** It is a controlled shopping simulator, not an arbitrary live website.

#### WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?

- **Local file:** [PDF](<WorkArena_How_Capable_are_WebAgents_at_Solving_Common_Knowledge_Work_Tasks.pdf>)
- **Year / venue:** 2024, ICML 2024.
- **Problem addressed:** Enterprise browser workflows differ from public web tasks and require structured interaction with complex business software.
- **Core idea / approach:** WorkArena evaluates agents on 33 ServiceNow-based tasks and introduces BrowserGym support.
- **Evaluation setting:** Remote-hosted enterprise tasks with multimodal observations and rich action spaces.
- **Main findings / contribution:** The paper shows that web agents can solve some knowledge-work tasks but remain far from full automation.
- **Security relevance:** Indirect; enterprise automation raises permission, audit, privacy, and safe-action requirements.
- **Limitations / open questions:** The task set is focused on one platform family and emphasizes capability more than governance.

#### WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks

- **Local file:** [PDF](<WorkArena_Towards_Compositional_Planning_and_Reasoning-based_Common_Knowledge_Work_Tasks.pdf>)
- **Year / venue:** 2024, NeurIPS 2024.
- **Problem addressed:** Enterprise agents need compositional planning, arithmetic/logical reasoning, retrieval, and contextual understanding.
- **Core idea / approach:** WorkArena++ expands to 682 realistic tasks and provides a mechanism for generating ground-truth observation/action traces.
- **Evaluation setting:** State-of-the-art LLMs, VLMs, and human workers on ServiceNow-style workflows.
- **Main findings / contribution:** The benchmark reveals failures in information retrieval, exploration, hallucinated actions, and long-horizon planning.
- **Security relevance:** Indirect but important for enterprise trustworthiness.
- **Limitations / open questions:** Safety policies, access control, and privacy are separate concerns handled more directly by ST-WebAgentBench.

### Web Scraping / Extraction Papers

#### AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation

- **Local file:** [PDF](<AutoScraper_A_Progressive_Understanding_Web_Agent_for_Web_Scraper_Generation.pdf>)
- **Year / venue:** 2024, EMNLP 2024.
- **Problem addressed:** Wrapper-based scraping is brittle across websites, while direct LLM extraction lacks reusability.
- **Core idea / approach:** AutoScraper introduces scraper generation with LLMs, using progressive understanding of HTML hierarchy and synthesis across similar pages.
- **Evaluation setting:** Multiple LLMs on web scraper generation tasks, with an executability metric measuring whether generated scrapers run successfully across pages.
- **Main findings / contribution:** The paper reframes LLMs as generators of reusable extraction programs rather than one-off extractors.
- **Security relevance:** Mostly non-security, though scraper automation is relevant to abuse and governance.
- **Limitations / open questions:** The paper discusses efficiency and limitations, but not adversarial anti-scraping defenses, privacy, or legal/ethical controls.

#### Webscraper: Leverage Multimodal Large Language Models for Index-Content Web Scraping

- **Local file:** [PDF](<Webscraper_Leverage_Multimodal_Large_Language_Models_for_Index-Content_Web_Scraping.pdf>)
- **Year / venue:** 2026, arXiv.
- **Problem addressed:** Dynamic interactive websites are difficult for static HTML parsers and manually customized scrapers.
- **Core idea / approach:** Webscraper uses an MLLM to navigate interactive interfaces, invoke specialized tools, and extract structured index-content records.
- **Evaluation setting:** Dynamic sites such as news and e-commerce pages.
- **Main findings / contribution:** It connects browser-agent interaction with structured extraction, showing how multimodal perception can support scraping beyond static DOM parsing.
- **Security relevance:** Security-relevant as a capability that could be used for large-scale scraping, but the paper itself is not a security paper.
- **Limitations / open questions:** The collection contains little work connecting this capability to consent, rate limits, privacy leakage, or detection.

### Information-Seeking Papers

#### Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge

- **Local file:** [PDF](<Mind2Web_2_Evaluating_Agentic_Search_with_Agent-as-a-Judge.pdf>)
- **Year / venue:** 2025, arXiv.
- **Problem addressed:** Deep-research-style agentic search is open-ended, long-horizon, and hard to evaluate with fixed short answers.
- **Core idea / approach:** Mind2Web 2 evaluates browsing agents that synthesize citation-backed answers and uses an agent-as-a-judge method for richer assessment.
- **Evaluation setting:** Agentic search tasks requiring autonomous browsing, synthesis, and answer evaluation.
- **Main findings / contribution:** The paper extends the Mind2Web line from action prediction toward open-ended agentic search.
- **Security relevance:** Indirect; citation-backed browsing can still retrieve unsafe or injected content.
- **Limitations / open questions:** LLM judging introduces calibration and bias questions, and safety is not the primary dimension.

#### WebDancer: Towards Autonomous Information Seeking Agency

- **Local file:** [PDF](<WebDancer_Towards_Autonomous_Information_Seeking_Agency.pdf>)
- **Year / venue:** 2025, arXiv.
- **Problem addressed:** Autonomous information seeking requires agents that can plan, browse, collect evidence, and reason over many steps.
- **Core idea / approach:** WebDancer proposes a data-centric and training-stage pipeline: browsing data construction, trajectory sampling, reasoning-oriented training, and evaluation for information seeking.
- **Evaluation setting:** Deep-research and browsing tasks, compared against agentic information-seeking baselines.
- **Main findings / contribution:** The paper treats information seeking as an end-to-end agency problem rather than only retrieval or QA.
- **Security relevance:** Indirect; open-web research agents face source trust and prompt-injection risks.
- **Limitations / open questions:** It emphasizes capability training more than provenance verification, safety, or live-web containment.

#### WebGPT: Browser-assisted Question-Answering with Human Feedback

- **Local file:** [PDF](<WebGPT_Browser-assisted_question-answering_with_human_feedback.pdf>)
- **Year / venue:** 2021, arXiv / OpenAI.
- **Problem addressed:** LMs need current external information and transparent evidence for long-form QA.
- **Core idea / approach:** WebGPT fine-tunes GPT-3 in a text-based browsing environment using imitation learning and human feedback, requiring the model to collect references.
- **Evaluation setting:** ELI5-style long-form answers with human evaluation of factual quality.
- **Main findings / contribution:** It is an early template for search-browse-read-cite agents trained from human browsing behavior.
- **Security relevance:** Security-relevant because retrieved web content enters the model context, although prompt injection was not the central framing.
- **Limitations / open questions:** The text browser is limited compared with modern visual websites, and safety against malicious sources is not central.

#### WebSailor: Navigating Super-human Reasoning for Web Agent

- **Local file:** [PDF](<WebSailor_Navigating_Super-human_Reasoning_for_Web_Agent.pdf>)
- **Year / venue:** 2025, arXiv.
- **Problem addressed:** Difficult web information-seeking tasks require systematic uncertainty reduction across vast information landscapes.
- **Core idea / approach:** WebSailor trains agents to reason through uncertainty and navigate complex open-web information spaces, motivated by Deep Research-style systems.
- **Evaluation setting:** Challenging information-seeking benchmarks including BrowseComp-like tasks.
- **Main findings / contribution:** The paper argues that advanced web agents need explicit reasoning patterns for reducing uncertainty, not just stronger retrieval.
- **Security relevance:** Indirect; deeper browsing increases exposure to untrusted sources.
- **Limitations / open questions:** The paper focuses on reasoning capability more than source trust, privacy, or adversarial content.

#### WebWalker: Benchmarking LLMs in Web Traversal

- **Local file:** [PDF](<WebWalker_Benchmarking_LLMs_in_Web_Traversal.pdf>)
- **Year / venue:** 2025, ACL 2025.
- **Problem addressed:** Traditional search/RAG often retrieves shallow pages and misses information buried inside site subpages.
- **Core idea / approach:** WebWalkerQA evaluates vertical traversal from an initial website, and WebWalker uses an explore-critic multi-agent framework.
- **Evaluation setting:** Question-answering over website subpage traversal with horizontal and vertical integration.
- **Main findings / contribution:** The paper separates web traversal from general search and shows that site-internal exploration remains challenging.
- **Security relevance:** Indirect; traversal agents may encounter hidden or malicious content deeper in sites.
- **Limitations / open questions:** Text-focused traversal does not fully cover dynamic visual interaction or action safety.

### Security and Safety Papers

#### ACE: A Security Architecture for LLM-Integrated App Systems

- **Local file:** [PDF](<Security/ACE_A_Security_Architecture_for_LLM-Integrated_App_Systems.pdf>)
- **Year / venue:** 2026, NDSS 2026.
- **Problem addressed:** LLM-integrated apps can be compromised when untrusted app outputs influence planning or execution.
- **Core idea / approach:** ACE separates trusted planning from untrusted execution and uses static enforcement of security policies over plans.
- **Evaluation setting:** Attacks against LLM-integrated app systems, including integrity, availability, and privacy failures.
- **Main findings / contribution:** The paper offers a principled architecture for reducing indirect prompt-injection and tool-use risks.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Applying such architecture to messy browser agents with arbitrary websites, accounts, and UI actions remains an open systems problem.

#### Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs

- **Local file:** [PDF](<Security/Attention_is_All_You_Need_to_Defend_Against_Indirect_Prompt_Injection_Attacks_in_LLMs.pdf>)
- **Year / venue:** 2026, NDSS 2026.
- **Problem addressed:** LLM applications and web agents are vulnerable to indirect prompt injections embedded in untrusted external data.
- **Core idea / approach:** RENNERVATE uses attention features for token-level detection and sanitization of injected instructions.
- **Evaluation setting:** Experiments on IPI detection, transferability, robustness, and preservation of useful functionality.
- **Main findings / contribution:** The paper demonstrates a compact detector/sanitizer strategy based on internal attention signals.
- **Security relevance:** Direct defense paper.
- **Limitations / open questions:** It is a model-level mitigation; full web-agent safety also needs permissions, provenance, UI constraints, and action auditing.

#### AWE: Adaptive Agents for Dynamic Web Penetration Testing

- **Local file:** [PDF](<Security/AWE_Adaptive_Agents_for_Dynamic_Web_Penetration_Testing.pdf>)
- **Year / venue:** 2026, venue unclear from local PDF.
- **Problem addressed:** Pattern-based web scanners struggle with novel contexts and deep workflows; unconstrained LLM pentesters can be costly and unstable.
- **Core idea / approach:** AWE uses a memory-augmented multi-agent framework with vulnerability-specific analysis pipelines, payload mutation, and browser-backed verification.
- **Evaluation setting:** Web penetration-testing challenges measured by solve rate, time-to-solve, token usage, and API cost.
- **Main findings / contribution:** The paper adapts agentic web interaction to security testing with more structure than open-ended exploration.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Reproducibility, legal deployment boundaries, and coverage of real production apps require caution.

#### Formalizing and Benchmarking Prompt Injection Attacks and Defenses

- **Local file:** [PDF](<Security/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf>)
- **Year / venue:** 2024, USENIX Security 2024.
- **Problem addressed:** Prompt-injection work lacked a common formalism and systematic benchmark across attacks, defenses, LLMs, and tasks.
- **Core idea / approach:** The paper formalizes prompt injection, unifies existing attacks, designs combined attacks, and evaluates 5 attacks and 10 defenses with 10 LLMs and 7 tasks.
- **Evaluation setting:** Multiple LLM-integrated application tasks rather than only web agents.
- **Main findings / contribution:** It supplies a foundational security benchmark and vocabulary for later web-agent prompt-injection work.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** It is broader than web agents and does not fully model long-horizon browser action.

#### Identifying AI Web Scrapers Using Canary Tokens

- **Local file:** [PDF](<Security/Identifying_AI_Web_Scrapers_Using_Canary_Tokens.pdf>)
- **Year / venue:** 2026, arXiv.
- **Problem addressed:** Site owners lack reliable ways to identify AI-related scraping infrastructures and enforce access preferences.
- **Core idea / approach:** The paper places canary tokens on websites and later queries LLM-backed systems to detect whether scraped content appears.
- **Evaluation setting:** Measurements over a small set of websites and queries from one vantage point.
- **Main findings / contribution:** It connects AI web scraping to empirical detection and governance.
- **Security relevance:** Direct scraper-defense paper.
- **Limitations / open questions:** The authors note limited site coverage and vantage points; adaptive scrapers, geography, and provider-specific infrastructure remain open.

#### Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

- **Local file:** [PDF](<Security/Not_What_You've_Signed_Up_For_Compromising_Real-World_LLM-Integrated_Applications_with_Indirect_Prompt_Injection.pdf>)
- **Year / venue:** 2023, ACM AISec 2023.
- **Problem addressed:** LLM applications blur data and instructions when they retrieve untrusted content.
- **Core idea / approach:** The paper introduces indirect prompt injection, develops a threat taxonomy, and demonstrates practical attacks including data theft and manipulation.
- **Evaluation setting:** Real-world and synthetic LLM-integrated applications.
- **Main findings / contribution:** It is an early security foundation for understanding webpages and retrieved documents as remote instruction vectors.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** It predates many modern browser-agent benchmarks and does not provide a full web-agent evaluation harness.

#### Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems

- **Local file:** [PDF](<Security/Overcoming_the_Retrieval_Barrier_Indirect_Prompt_Injection_in_the_Wild_for_LLM_Systems.pdf>)
- **Year / venue:** 2026, USENIX Security 2026.
- **Problem addressed:** Many IPI demonstrations assume malicious content is retrieved; in practice retrieval itself is a barrier.
- **Core idea / approach:** The paper splits attack content into a trigger fragment that ensures retrieval and an attack fragment that encodes the objective, using a black-box construction.
- **Evaluation setting:** RAG and agentic systems under natural user queries, including single- and multi-agent workflows.
- **Main findings / contribution:** It makes IPI more realistic by solving the retrieval step rather than assuming it.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Defense against adaptive retrieval-optimized attacks remains difficult, especially for open-web agents.

#### Prompt Injection Attack to Tool Selection in LLM Agents

- **Local file:** [PDF](<Security/Prompt_Injection_Attack_to_Tool_Selection_in_LLM_Agents.pdf>)
- **Year / venue:** 2026, NDSS 2026.
- **Problem addressed:** LLM agents often retrieve and select tools from tool libraries, creating an attack surface in tool descriptions.
- **Core idea / approach:** ToolHijacker injects a malicious tool document to manipulate retrieval and selection so the agent chooses an attacker-controlled tool.
- **Evaluation setting:** Multiple LLMs and benchmark datasets, plus prevention and detection defenses.
- **Main findings / contribution:** The paper extends prompt injection from webpage content to the tool-selection pipeline itself.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Web agents need defenses that combine tool provenance, permissioning, and content-level injection filtering.

#### SafeArena: Evaluating the Safety of Autonomous Web Agents

- **Local file:** [PDF](<Security/SafeArena_Evaluating_the_Safety_of_Autonomous_Web_Agents.pdf>)
- **Year / venue:** 2025, ICML 2025 / OpenReview.
- **Problem addressed:** Capable web agents may deliberately complete harmful tasks, not just fail benign ones.
- **Core idea / approach:** SafeArena contains 250 safe and 250 harmful tasks across four websites, categorized by misinformation, illegal activity, harassment, cybercrime, and social bias.
- **Evaluation setting:** Leading LLM-based web agents are measured for both task completion and harmful compliance.
- **Main findings / contribution:** It reframes web-agent safety as a dual-use and misuse benchmark rather than only robustness.
- **Security relevance:** Direct safety benchmark.
- **Limitations / open questions:** It does not cover every enterprise policy, privacy boundary, or prompt-injection threat.

#### ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents

- **Local file:** [PDF](<Security/ST-WebAgentBench_A_Benchmark_for_Evaluating_Safety_and_Trustworthiness_in_Web_Agents.pdf>)
- **Year / venue:** 2026, ICLR 2026.
- **Problem addressed:** Enterprise deployment requires more than task completion; agents must obey safety and trust policies.
- **Core idea / approach:** ST-WebAgentBench attaches 3,057 policies to 375 tasks and scores agents on dimensions such as consent, robustness, and policy adherence.
- **Evaluation setting:** Configurable web tasks with policy-aware metrics such as CuP, pCuP, and Risk Ratio.
- **Main findings / contribution:** The paper provides a more enterprise-oriented safety/trustworthiness benchmark than general web-agent tasks.
- **Security relevance:** Direct safety and trustworthiness benchmark.
- **Limitations / open questions:** Policy taxonomies and real organizational controls will need continual updating.

#### Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search

- **Local file:** [PDF](<Security/Unsafe_LLM-Based_Search_Quantitative_Analysis_and_Mitigation_of_Safety_Risks_in_AI_Web_Search.pdf>)
- **Year / venue:** 2025, USENIX Security 2025.
- **Problem addressed:** AI-powered search engines may surface malicious URLs or harmful content in generated answers.
- **Core idea / approach:** The paper defines a threat model and risk categories, evaluates seven production AI-powered search engines, and studies mitigations.
- **Evaluation setting:** Queries and malicious-content data from sources such as PhishTank, ThreatBook, and LevelBlue.
- **Main findings / contribution:** It quantifies safety risks in AI search, a neighboring capability to browsing and research agents.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Search-answer risk is not identical to browser-agent action risk; multi-step agent behavior remains broader.

#### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections

- **Local file:** [PDF](<Security/WARD_Adversarially_Robust_Defense_of_Web_Agents_Against_Prompt_Injections.pdf>)
- **Year / venue:** 2026, arXiv.
- **Problem addressed:** Web agents face prompt injections embedded in HTML and visual interfaces, while existing guards can be slow, brittle, or high false-positive.
- **Core idea / approach:** WARD trains a practical guard model on WARD-Base, a dataset with about 177K samples from high-traffic websites, with adversarial robustness in mind.
- **Evaluation setting:** WebArena-style tasks and prompt-injection scenarios, measuring false positives and protection.
- **Main findings / contribution:** WARD is one of the most directly web-agent-specific defenses in the collection.
- **Security relevance:** Direct defense paper.
- **Limitations / open questions:** Guard models still need integration with permissions, provenance, and action-level policy enforcement.

#### WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks

- **Local file:** [PDF](<Security/WASP_Benchmarking_Web_Agent_Security_Against_Prompt_Injection_Attacks.pdf>)
- **Year / venue:** 2025, arXiv / OpenReview.
- **Problem addressed:** Prompt-injection tests for web agents are often single-step or unrealistic.
- **Core idea / approach:** WASP provides end-to-end web-agent security tasks where malicious instructions appear in realistic UI settings and agents must complete benign goals safely.
- **Evaluation setting:** Web-agent prompt-injection attacks against systems such as VisualWebArena-style agents, Claude Computer Use, and Operator-like agents.
- **Main findings / contribution:** The benchmark exposes security failures in advanced agents during realistic multi-step browsing.
- **Security relevance:** Direct security benchmark.
- **Limitations / open questions:** It focuses on prompt injection; broader threats such as privacy leakage, economic abuse, and account misuse need more coverage.

#### When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins

- **Local file:** [PDF](<Security/When_AI_Meets_the_Web_Prompt_Injection_Risks_in_Third-Party_AI_Chatbot_Plugins.pdf>)
- **Year / venue:** 2026, IEEE S&P 2026.
- **Problem addressed:** Public websites increasingly deploy third-party chatbot plugins, but their prompt-injection exposure is poorly understood.
- **Core idea / approach:** The paper studies 17 chatbot plugins used by over 10,000 websites, analyzing direct and indirect prompt injection via plugin configurations and scraped web content.
- **Evaluation setting:** Large-scale measurement of public website deployments and systematic security tests.
- **Main findings / contribution:** It shows that prompt-injection risk is already present in ordinary website chatbots, not only advanced agents.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** Chatbot plugins are adjacent to, but not identical with, autonomous browser agents.

#### YuraScanner: Leveraging LLMs for Task-driven Web App Scanning

- **Local file:** [PDF](<Security/YURASCANNER_Leveraging_LLMs_for_Task-driven_Web_App_Scanning.pdf>)
- **Year / venue:** 2025, NDSS 2025.
- **Problem addressed:** Traditional web application scanners fail to discover deeper states that require understanding workflows.
- **Core idea / approach:** YuraScanner is a goal-driven LLM agent that generates and executes multi-step tasks to explore web applications for security scanning.
- **Evaluation setting:** 20 real web applications and manual review of generated/executed tasks.
- **Main findings / contribution:** It demonstrates that LLM-guided task execution can improve web app scanning beyond pattern-driven crawling.
- **Security relevance:** Direct security paper.
- **Limitations / open questions:** The technique raises questions about safe deployment, authorization, reproducibility, and coverage guarantees.

### Borderline but Useful Papers

#### AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents

- **Local file:** [PDF](<Borderline/AndroidWorld_A_Dynamic_Benchmarking_Environment_for_Autonomous_Agents.pdf>)
- **Year / venue:** 2025, ICLR 2025.
- **Problem addressed:** Autonomous computer-use agents need realistic, reproducible GUI benchmarks beyond the browser.
- **Core idea / approach:** AndroidWorld provides 116 programmatic tasks across 20 real Android apps, with dynamic task instantiation.
- **Evaluation setting:** Mobile-app control with reward signals and robustness analysis.
- **Main findings / contribution:** Useful comparison point for cross-platform agents and dynamic task generation.
- **Security relevance:** Borderline; GUI action risks resemble web-agent risks.
- **Limitations / open questions:** It is mobile-app-focused rather than web-focused.

#### EvoCrawl: Exploring Web Application Code and State using Evolutionary Search

- **Local file:** [PDF](<Borderline/EvoCrawl_Exploring_Web_Application_Code_and_State_using_Evolutionary_Search.pdf>)
- **Year / venue:** 2025, venue unclear from local PDF.
- **Problem addressed:** Web vulnerabilities may require specific server-side states and input sequences to trigger.
- **Core idea / approach:** EvoCrawl uses evolutionary search to generate sequences of web interactions that improve code and state coverage.
- **Evaluation setting:** Ten web applications compared with web vulnerability scanners.
- **Main findings / contribution:** It is a strong non-LLM reference for stateful web exploration.
- **Security relevance:** Borderline security; useful for comparing LLM-guided scanning against evolutionary crawling.
- **Limitations / open questions:** It is not primarily an LLM or agentic-AI paper.

#### Gorilla: Large Language Model Connected with Massive APIs

- **Local file:** [PDF](<Borderline/Gorilla_Large_Language_Model_Connected_with_Massive_APIs.pdf>)
- **Year / venue:** 2024, NeurIPS 2024.
- **Problem addressed:** LLMs need reliable API call generation over large and changing tool sets.
- **Core idea / approach:** Gorilla fine-tunes an LLaMA model and uses retrieval over API documentation to improve tool invocation.
- **Evaluation setting:** API call generation benchmarks.
- **Main findings / contribution:** It is background for agents that combine browsing with external APIs.
- **Security relevance:** Borderline; tool invocation creates security and permission risks.
- **Limitations / open questions:** It is not web-navigation-specific.

#### Toolformer: Language Models Can Teach Themselves to Use Tools

- **Local file:** [PDF](<Borderline/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools.pdf>)
- **Year / venue:** 2023, NeurIPS 2023.
- **Problem addressed:** Language models struggle with tasks such as arithmetic and factual lookup that external tools can handle.
- **Core idea / approach:** Toolformer self-supervises API-call use by deciding which calls to insert, when to call, and how to use results.
- **Evaluation setting:** Language modeling tasks augmented with tools.
- **Main findings / contribution:** It is foundational background for tool-using agents, including web agents.
- **Security relevance:** Borderline; tool use becomes risky when tools can act externally.
- **Limitations / open questions:** It does not study browsers, webpages, or web security.

## Research Problems Identified in the Literature

### Problem: General Web Task Completion

- **Research question:** How can agents follow natural-language instructions and complete tasks on websites?
- **Why it matters:** This is the central automation promise behind browser agents.
- **Representative papers:** WebShop, Mind2Web, WebArena, AutoWebGLM, WebVoyager, SeeAct, WebLINX.
- **Common approaches:** ReAct loops, DOM/HTML observations, screenshots, action prediction, demonstrations, and environment-specific benchmarks.
- **What remains unresolved:** Robustness to live-site change, task ambiguity, recovery from errors, safe action policies, and evaluation beyond final success.

### Problem: Multi-step Web Information Seeking

- **Research question:** How can agents search, browse, synthesize, and cite information over many steps?
- **Why it matters:** Deep research systems require more than top-k retrieval.
- **Representative papers:** WebGPT, WebDancer, WebSailor, Mind2Web 2, BrowseComp, BEARCUBS, MMInA.
- **Common approaches:** Browser-assisted QA, trajectory training, uncertainty reduction, agent-as-a-judge evaluation, and short-answer benchmarks.
- **What remains unresolved:** Source trust, adversarial retrieval, provenance evaluation, and long-horizon multi-site reliability.

### Problem: Web Traversal and Site Exploration

- **Research question:** How can agents explore a website's internal structure to find information or reach deep states?
- **Why it matters:** Many useful pages are not available from shallow search snippets.
- **Representative papers:** WebWalker, Go-Browse, LASER, YuraScanner, EvoCrawl.
- **Common approaches:** Explore-critic frameworks, graph search, state-space exploration, evolutionary search, and task-driven scanning.
- **What remains unresolved:** Coverage guarantees, efficient exploration of dynamic pages, and safe traversal boundaries.

### Problem: Visual Web Grounding

- **Research question:** How can agents map visual webpage understanding to executable UI actions?
- **Why it matters:** Many webpages encode meaning in layout, images, icons, and rendered state.
- **Representative papers:** SeeAct, WebVoyager, VisualWebArena, MMInA, BEARCUBS.
- **Common approaches:** Screenshots, multimodal models, candidate element grounding, and visual trajectory judging.
- **What remains unresolved:** Adversarial visual instructions, ambiguous UI elements, accessibility mismatches, and cross-device layout variation.

### Problem: Web Scraping and Structured Extraction

- **Research question:** Can LLM agents generate reusable scrapers or extract structured records from dynamic websites?
- **Why it matters:** Research, monitoring, and data integration often require structured web data rather than task completion.
- **Representative papers:** AutoScraper, Webscraper.
- **Common approaches:** HTML hierarchy analysis, progressive scraper generation, MLLM navigation, and extraction-specific tools.
- **What remains unresolved:** Safety, consent, anti-abuse controls, extraction quality on adversarial sites, and scraper detection.

### Problem: Realistic and Reproducible Web-Agent Benchmarks

- **Research question:** How can the field evaluate agents fairly when websites are interactive, dynamic, and expensive to maintain?
- **Why it matters:** Without reproducible benchmarks, claims about web agents are hard to compare.
- **Representative papers:** WebShop, Mind2Web, WebArena, VisualWebArena, WorkArena, WorkArena++, BrowserGym, BEARCUBS, BrowseComp, MMInA.
- **Common approaches:** Simulators, self-hosted sites, live-web QA, standardized browser environments, and human-validated trajectories.
- **What remains unresolved:** Live-web validity versus reproducibility, benchmark contamination, safety scoring, and maintenance burden.

### Problem: Learning from Demonstrations, Self-Exploration, and Synthetic Trajectories

- **Research question:** What data and training procedures make web agents more capable than prompted general LLMs?
- **Why it matters:** Browser behavior is long-horizon and difficult to learn from final answers alone.
- **Representative papers:** WebGPT, WebLINX, AutoWebGLM, Go-Browse, WorkArena++, WebDancer, WebSailor.
- **Common approaches:** Imitation learning, human feedback, human-AI trajectories, graph-search exploration, synthetic traces, and RL bootstrapping.
- **What remains unresolved:** Data quality, safe exploration, transfer to unseen websites, and avoiding learned unsafe behaviors.

### Problem: Enterprise and Knowledge-Work Browser Automation

- **Research question:** Can web agents perform realistic enterprise workflows that require planning, retrieval, and reasoning?
- **Why it matters:** Enterprise automation is high-value but safety-critical.
- **Representative papers:** WorkArena, WorkArena++, BrowserGym, ST-WebAgentBench.
- **Common approaches:** ServiceNow-style environments, compositional tasks, policy-aware scoring, and standardized action spaces.
- **What remains unresolved:** Permissions, auditability, human approval, privacy, and organization-specific policy adaptation.

### Problem: Prompt Injection and Malicious Webpage Attacks

- **Research question:** How can agents remain aligned with user intent when webpages or retrieved content contain adversarial instructions?
- **Why it matters:** The web is untrusted, yet agents place web content into the model context and may act on it.
- **Representative papers:** Not What You've Signed Up For, Formalizing and Benchmarking Prompt Injection, WASP, WARD, RENNERVATE, Overcoming the Retrieval Barrier, When AI Meets the Web.
- **Common approaches:** Attack taxonomies, benchmark construction, retrieval-optimized attacks, guard models, token-level sanitization, and adversarial training.
- **What remains unresolved:** End-to-end defenses that combine content filtering, policy enforcement, provenance, UI grounding, and tool permissions.

### Problem: Unsafe Tool Use, Data Exfiltration, and Trustworthy Action

- **Research question:** How can agents avoid choosing malicious tools, leaking private data, or performing unauthorized actions?
- **Why it matters:** Agents are dangerous when they connect untrusted inputs to privileged tools.
- **Representative papers:** ACE, ToolHijacker, ST-WebAgentBench, SafeArena, Overcoming the Retrieval Barrier.
- **Common approaches:** Security architectures, tool-selection attack models, policy-aware metrics, and harmful-task benchmarks.
- **What remains unresolved:** Fine-grained permission models for browser actions, cross-tool data flow control, and usable human approval.

### Problem: AI Scraper Detection and Crawler Defense

- **Research question:** How can websites detect, regulate, or defend against AI-related scraping?
- **Why it matters:** LLM training and query-time scraping affect site stability, privacy, and consent.
- **Representative papers:** Identifying AI Web Scrapers Using Canary Tokens, AutoScraper, Webscraper.
- **Common approaches:** Canary tokens, query-time leakage checks, and scraper-generation analysis.
- **What remains unresolved:** Robust attribution, provider transparency, adaptive scraper behavior, and policy enforcement.

### Problem: LLM-guided Web App Security Testing

- **Research question:** Can LLM agents improve vulnerability scanning by understanding workflows and reaching deeper states?
- **Why it matters:** Modern web apps are stateful and UI-driven, defeating many pattern-based scanners.
- **Representative papers:** YuraScanner, AWE, EvoCrawl.
- **Common approaches:** Goal-driven task generation, multi-agent pentesting, memory, payload mutation, browser-backed verification, and evolutionary exploration.
- **What remains unresolved:** Soundness, authorization, reproducibility, cost, and safe containment for autonomous testing.

## Problem-Approach Matrix

| Approach | General web task completion | Web navigation / browser automation | Web traversal and site exploration | Web information seeking / deep research | Web scraping / structured extraction | Multimodal visual web interaction | Enterprise web workflows | Benchmarking and reproducible evaluation | Learning / training web agents | Prompt injection and malicious webpage attacks | Unsafe tool use / data exfiltration | Web-agent safety and trustworthiness | AI scraper detection or crawler defense | Web app security testing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prompting / ReAct-style reasoning-action loops | ReAct; WebShop; WebArena; WebVoyager | ReAct; AutoWebGLM; WebVoyager | WebWalker; LASER | WebGPT; WebDancer; WebSailor | Webscraper | WebVoyager; SeeAct | WorkArena | WebShop; WebArena | WebGPT | — | — | SafeArena | — | AWE |
| DOM / HTML-based browser control | Mind2Web; AutoWebGLM; WebArena | AutoWebGLM; WebLINX; BrowserGym | WebWalker; Go-Browse | Mind2Web 2 | AutoScraper | SeeAct | WorkArena; WorkArena++ | Mind2Web; WebArena; BrowserGym | WebLINX; AutoWebGLM | WASP; WARD | ACE | ST-WebAgentBench | — | YuraScanner |
| Visual grounding with screenshots or multimodal models | SeeAct; WebVoyager | WebVoyager; SeeAct | BEARCUBS; MMInA | BEARCUBS; MMInA | Webscraper | SeeAct; WebVoyager; VisualWebArena; MMInA | WorkArena++ | VisualWebArena; MMInA; BEARCUBS | — | WASP; WARD | — | ST-WebAgentBench | — | — |
| State-space exploration / planning | LASER; WebArena | LASER | LASER; WebWalker | WebSailor | — | — | WorkArena++ | — | — | — | — | — | — | AWE |
| Demonstration learning / imitation learning | WebGPT; Mind2Web; WebLINX | WebLINX; AutoWebGLM | — | WebGPT | — | — | WorkArena++ | Mind2Web; WebLINX | WebGPT; WebLINX; AutoWebGLM | — | — | — | — | — |
| Reinforcement learning / self-improvement | WebShop; AutoWebGLM | AutoWebGLM | — | WebDancer; WebSailor | — | — | — | WebShop | WebShop; AutoWebGLM; WebDancer | — | — | — | — | — |
| Synthetic data generation / trajectory generation | Go-Browse; WorkArena++ | Go-Browse | Go-Browse | WebDancer; WebSailor | — | — | WorkArena++ | WorkArena++ | Go-Browse; WorkArena++; WebDancer; WebSailor | WARD | — | ST-WebAgentBench | — | AWE |
| Benchmark construction / environment design | WebShop; Mind2Web; WebArena | BrowserGym; WebArena | WebWalker | BrowseComp; BEARCUBS; Mind2Web 2; MMInA | — | VisualWebArena; MMInA | WorkArena; WorkArena++ | WebShop; Mind2Web; WebArena; VisualWebArena; BrowserGym; WorkArena; BEARCUBS; BrowseComp | — | WASP; Formalizing Prompt Injection | ToolHijacker | SafeArena; ST-WebAgentBench | — | YuraScanner |
| Agent-as-a-judge evaluation | WebVoyager | WebVoyager | — | Mind2Web 2 | — | WebVoyager | — | Mind2Web 2; WebVoyager | — | — | — | — | — | — |
| Hierarchical planning / modular agents | AutoWebGLM; LASER | AutoWebGLM; LASER | WebWalker | WebDancer; WebSailor | Webscraper | SeeAct | WorkArena++ | — | AutoWebGLM; WebDancer | — | ACE | ST-WebAgentBench | — | AWE; YuraScanner |
| Tool-use and API orchestration | ReAct | BrowserGym | — | WebGPT | Webscraper | — | WorkArena | — | Toolformer; Gorilla | ToolHijacker | ACE; ToolHijacker | ST-WebAgentBench | — | AWE |
| Web traversal / link-following policies | — | LASER | WebWalker; Go-Browse; EvoCrawl | WebWalker; BEARCUBS | — | MMInA | — | WebWalker; BEARCUBS | Go-Browse | — | — | — | — | YuraScanner; EvoCrawl |
| Scraper-generation pipelines | — | — | — | — | AutoScraper; Webscraper | Webscraper | — | — | AutoScraper | — | — | — | AutoScraper; Webscraper | — |
| Safety benchmark design | — | — | — | Unsafe LLM-Based Search | — | — | ST-WebAgentBench | SafeArena; ST-WebAgentBench; WASP | — | WASP | ST-WebAgentBench | SafeArena; ST-WebAgentBench | — | — |
| Prompt-injection attack generation | — | — | — | Overcoming the Retrieval Barrier | — | — | — | Formalizing Prompt Injection; WASP | — | Not What You've Signed Up For; Formalizing Prompt Injection; WASP; Overcoming the Retrieval Barrier; When AI Meets the Web | ToolHijacker | WASP | — | — |
| Prompt-injection defenses / guard models | — | — | — | Unsafe LLM-Based Search | — | — | — | Formalizing Prompt Injection | WARD | WARD; RENNERVATE; Formalizing Prompt Injection | ACE | ST-WebAgentBench | — | — |
| Permissioning / security architecture | — | — | — | — | — | — | ST-WebAgentBench | — | — | ACE | ACE; ToolHijacker | ST-WebAgentBench | — | — |
| Canary-token or detection-based scraper defense | — | — | — | — | — | — | — | — | — | — | — | — | Identifying AI Web Scrapers Using Canary Tokens | — |
| LLM-guided web app security scanning | — | — | YuraScanner; AWE; EvoCrawl | — | — | — | — | — | — | — | — | — | — | YuraScanner; AWE |

The densest part of the matrix is general web task completion, browser automation, and benchmarking: many papers build environments or agents for navigation, and the dominant approaches are ReAct-style loops, DOM/HTML control, visual grounding, and demonstration data. Information seeking is also well represented, but it is split between browsing QA benchmarks and newer deep-research training recipes. Web traversal is emerging as its own problem, with WebWalker and Go-Browse separating exploration from generic search.

Security coverage is strong for prompt injection, especially attacks, benchmarks, and guard models. It is thinner for privacy leakage during ordinary browsing, permission models for browser actions, scraper governance, and unified benchmarks that combine navigation, extraction, information seeking, and safety. Scraper-generation work is capability-rich but relatively disconnected from the security and policy papers.

## Gap Analysis

### Gap 1: LLM-guided crawling is underdeveloped compared with browser-task benchmarks

- **Observed from papers:** WebArena, Mind2Web, VisualWebArena, WorkArena, and BrowserGym dominate the benchmark landscape, while explicit crawling/traversal is mainly WebWalker, Go-Browse, YuraScanner, and the borderline EvoCrawl.
- **Why it matters:** Many research and security tasks require systematic site exploration, not just completing a known instruction.
- **Potential research direction:** Develop LLM-guided crawling benchmarks with coverage metrics, state discovery, change handling, and safety constraints.

### Gap 2: Scraping/extraction is weakly connected to safety, abuse, and defenses

- **Observed from papers:** AutoScraper and Webscraper focus on extraction capability; Identifying AI Web Scrapers Using Canary Tokens focuses on detection. Few works connect the two sides.
- **Why it matters:** Better scraper agents can support research and monitoring, but also intensify consent, privacy, and infrastructure concerns.
- **Potential research direction:** Study scraper agents under robots policies, rate limits, privacy-preserving extraction, canary-token defenses, and adversarial anti-scraping settings.

### Gap 3: Live-web evaluation remains hard to reconcile with reproducibility

- **Observed from papers:** BEARCUBS, BrowseComp, MMInA, WebVoyager, and Mind2Web 2 use live or real-world websites; WebArena, VisualWebArena, WebShop, and WorkArena use controlled or self-hosted environments.
- **Why it matters:** Live websites are realistic but unstable; self-hosted sites are reproducible but may miss drift, adversaries, and real UI diversity.
- **Potential research direction:** Hybrid benchmarks with archived interaction states, live refresh protocols, contamination controls, and replayable browser traces.

### Gap 4: Mainstream capability benchmarks rarely include adversarial webpages

- **Observed from papers:** WebArena and VisualWebArena are capability benchmarks; WASP and WARD add prompt-injection security layers separately.
- **Why it matters:** Agents trained only for success may learn to obey malicious webpage content.
- **Potential research direction:** Add adversarial webpage variants, visual prompt injections, and policy-aware scoring to mainstream navigation benchmarks.

### Gap 5: Few unified benchmarks combine navigation, information seeking, extraction, and security

- **Observed from papers:** Information seeking appears in WebGPT, WebDancer, WebSailor, BrowseComp, BEARCUBS, and Mind2Web 2; extraction appears in AutoScraper and Webscraper; security appears in WASP, SafeArena, ST-WebAgentBench, and WARD.
- **Why it matters:** Real agents may need to browse, extract, cite, and act safely in the same session.
- **Potential research direction:** Build tasks where agents must gather evidence, extract structured data, obey policies, and resist malicious content.

### Gap 6: Privacy leakage during browsing sessions is not deeply evaluated

- **Observed from papers:** Not What You've Signed Up For, Overcoming the Retrieval Barrier, ACE, and ToolHijacker discuss data exfiltration pathways, but most web-agent benchmarks do not track private-context leakage.
- **Why it matters:** Agents often browse while holding user goals, credentials, history, documents, or enterprise context.
- **Potential research direction:** Create privacy-aware browsing tasks with canary secrets, data-flow tracking, and exfiltration scoring.

### Gap 7: Containment and permissioning models for browser agents remain immature

- **Observed from papers:** ACE proposes an architecture for LLM-integrated apps, and ST-WebAgentBench evaluates policies, but most browser agents rely on prompt instructions and action spaces.
- **Why it matters:** Browser agents can click, type, submit forms, buy goods, send messages, or change enterprise state.
- **Potential research direction:** Combine browser sandboxes, capability-based permissions, human approval gates, static policy checking, and runtime monitors.

### Gap 8: Long-horizon multi-site tasks are still sparse

- **Observed from papers:** BrowseComp, BEARCUBS, MMInA, WebDancer, and WebSailor push toward deeper research, but many benchmarks are site-local or short-horizon.
- **Why it matters:** Research workflows often require reconciling evidence across many sites and modalities.
- **Potential research direction:** Evaluate multi-site plans, contradiction handling, source reliability, and recovery after dead ends.

### Gap 9: Security papers focus heavily on prompt injection

- **Observed from papers:** WASP, WARD, RENNERVATE, Formalizing Prompt Injection, Overcoming the Retrieval Barrier, ToolHijacker, and When AI Meets the Web all center on injection-like threats.
- **Why it matters:** Prompt injection is critical, but web agents also face phishing, fraud, malware links, account misuse, privacy inference, economic abuse, and denial-of-wallet costs.
- **Potential research direction:** Broaden web-agent security benchmarks to include deception, harmful transactions, credential handling, resource abuse, and social engineering.

### Gap 10: Economic, ethical, and policy dimensions of AI crawlers and scrapers are thin

- **Observed from papers:** Canary-token detection raises governance questions, and AutoScraper/Webscraper improve scraping capability, but the collection has little policy analysis.
- **Why it matters:** AI crawlers affect publishers, site owners, users, and model providers.
- **Potential research direction:** Study technical enforcement of consent, attribution, audit logs, compensation signals, and crawler transparency mechanisms.

## Suggested Citation Clusters

### Foundational web-agent benchmarks

Cite these when introducing standard web-agent task environments and evaluation: WebShop, Mind2Web, WebArena, VisualWebArena, BrowserGym, WorkArena, WorkArena++.

### Multimodal browser agents

Cite these for screenshot-based interaction, visual grounding, or LMM-controlled browsing: SeeAct, WebVoyager, VisualWebArena, MMInA, BEARCUBS.

### Information seeking / deep research agents

Cite these when framing autonomous browsing for answers, citations, and multi-hop research: WebGPT, ReAct, WebDancer, WebSailor, WebWalker, Mind2Web 2, BrowseComp, BEARCUBS.

### Web scraping / extraction

Cite these for LLM-based scraper generation or dynamic structured extraction: AutoScraper, Webscraper. Add Identifying AI Web Scrapers Using Canary Tokens when discussing scraper detection or governance.

### Web traversal and exploration

Cite these when the focus is site exploration, graph search, or reaching deep web states: WebWalker, Go-Browse, LASER, YuraScanner, EvoCrawl.

### Enterprise browser automation

Cite these for knowledge-work and enterprise workflows: WorkArena, WorkArena++, BrowserGym, ST-WebAgentBench.

### Security and safety

Cite these for web-agent prompt injection, unsafe actions, or trustworthiness: WASP, WARD, SafeArena, ST-WebAgentBench, Unsafe LLM-Based Search, When AI Meets the Web, Not What You've Signed Up For, Overcoming the Retrieval Barrier, Formalizing and Benchmarking Prompt Injection, ToolHijacker, RENNERVATE, ACE.

### General tool-use background

Cite these when motivating LLMs that decide when to call tools or APIs: ReAct, Toolformer, Gorilla.

## Recommended Reading Order

1. WebGPT and ReAct - early foundations for search/action agents and reasoning-action loops.
2. WebShop, Mind2Web, and WebArena - core web-agent datasets and environments.
3. SeeAct, WebVoyager, and VisualWebArena - multimodal and visually grounded web interaction.
4. WebLINX, BrowserGym, WorkArena, and WorkArena++ - demonstrations, standardized browser environments, and enterprise workflows.
5. AutoScraper and Webscraper - scraper generation and structured extraction.
6. WebWalker, Go-Browse, WebDancer, WebSailor, BrowseComp, BEARCUBS, Mind2Web 2, and MMInA - traversal, deep research, and live multimodal information seeking.
7. Not What You've Signed Up For, Formalizing Prompt Injection, WASP, WARD, RENNERVATE, Overcoming the Retrieval Barrier, SafeArena, ST-WebAgentBench, Unsafe LLM-Based Search, When AI Meets the Web, ACE, ToolHijacker, Canary Tokens, YuraScanner, and AWE - security, safety, defenses, and web-security scanning.
8. AndroidWorld, EvoCrawl, Toolformer, and Gorilla - useful adjacent context for GUI agents, non-LLM web exploration, and general tool/API use.

## Limitations of this Repository

- Some papers are preprints or have final venue metadata that may have changed after the local PDF was downloaded.
- Some venue metadata is not explicit in the local PDF; those cases are marked as unclear rather than inferred.
- PDF extraction can introduce spacing errors, missing ligatures, or heading-detection noise.
- The collection is strong but not exhaustive; related papers such as Agent-E, WebCanvas, OSWorld-style GUI benchmarks, and newer security work may be absent.
- The problem-approach matrix is a synthesis of this local collection, not a universal taxonomy. It should be updated whenever papers are added.
- The summaries emphasize research positioning and open gaps rather than exhaustive experimental details.
