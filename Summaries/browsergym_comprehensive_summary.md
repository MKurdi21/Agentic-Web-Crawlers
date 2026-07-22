# The BrowserGym Ecosystem for Web Agent Research

**Authors:** Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Lacoste, with core contributors Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, and Sahar Omidi Shayegan; benchmark contributors Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, and Frank F. Xu; and affiliated advisors Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, and Nicolas Chapados.

**Publication:** *Transactions on Machine Learning Research*, February 2025.

## 1. Background and Context

Large language models (LLMs) and vision-language models (VLMs) have expanded conversational assistants beyond chat. They can search the web, read documents, execute sandboxed code, generate images, and directly operate browser interfaces.

Browser-operating assistants could automate repetitive, multi-step work such as filling forms, comparing products, synchronizing calendars, retrieving information, and performing enterprise workflows. This could:

- Free users to focus on higher-level decisions.
- Improve accessibility for people who find websites difficult to navigate.
- Make agent behavior visually inspectable because users can watch the interface.
- Work with existing software through its user interface without requiring a custom API.

Web-agent research, however, has become fragmented. Numerous benchmarks use different installation procedures, data formats, agent APIs, action spaces, evaluation rules, and experimental practices. An agent designed for one benchmark often cannot be evaluated on another without substantial re-engineering. This obstructs fair comparison, reproducibility, statistical testing, and development of general-purpose agents.

Earlier benchmarks progressed from controlled tasks to increasingly realistic settings:

- **MiniWoB/MiniWoB++** test basic interactions such as clicking and filling forms.
- **WebShop** adds constrained product search.
- **Mind2Web** contains more than 2,000 human traces from open-ended tasks on 137 real websites.
- **WebVoyager** evaluates live tasks on 15 popular websites.
- **Mind2Web-Live** converts static demonstrations into an online benchmark.
- **WebArena** and **VisualWebArena** use functional website replicas; the latter adds visual search, product-image comparison, and spatial reasoning.
- **WebLINX** contains more than 100,000 human interactions across 155 websites.
- **AssistantBench** contains 214 realistic, often multi-website information-gathering tasks.
- **MMInA** contains 1,050 multimodal, multi-website tasks.
- **GAIA** evaluates question answering that combines information from diverse web sources.
- **WorkArena/WorkArena++** test realistic enterprise knowledge-work workflows.
- **CRMArena** contains nine CRM tasks across service-agent, analyst, and manager roles.
- Other frameworks evaluate broader mobile, desktop, and operating-system interaction, while ST-WebAgentBench focuses on policy compliance and safety.

Web agents themselves also differ. Some act through HTML elements; others ground screenshots to interface elements or interact directly with pixels. Their reasoning may use specialized prompts, planning, search, fine-tuning, chain-of-thought, tree-of-thought, ReAct, or iterative reasoning. The paper argues that this diversity makes a common research framework essential.

The proposed ecosystem is explicitly a **research framework, not a consumer product**.

## 2. Research Goal and Objectives

The paper introduces an expanded **BrowserGym ecosystem** intended to standardize and accelerate web-agent research.

Its three practical goals are to support:

1. Designing a new web agent and evaluating it easily across many existing benchmarks.
2. Designing a new benchmark and evaluating existing agents on it.
3. Comparing LLMs and VLMs by changing the backbone model inside a common agent implementation.

The work has three central objectives:

- Extend BrowserGym and expose diverse benchmarks through one observation/action interface.
- Introduce AgentLab for agent construction, parallel evaluation, reproducibility, trace inspection, and model integration.
- Demonstrate the ecosystem through the first large-scale, unified experiment comparing six contemporary models across the available benchmark suite.

## 3. Methods (Approach/Design)

### 3.1 Overall ecosystem

**Figure 1** presents the architecture. BrowserGym is the common environment layer surrounding benchmarks such as MiniWoB, WebArena, VisualWebArena, WorkArena, WebLINX, AssistantBench, and Mind2Web-Live. A user-defined agent sits above it. AgentLab supplies dynamic prompting, a unified LLM API, parallel experiments, reproducibility support, a leaderboard, AgentXRay trace analysis, and facilities for sharing traces as a dataset.

The paper adds WebLINX, VisualWebArena, and AssistantBench to BrowserGym, bringing the supported collection to six benchmark families, with WorkArena represented at multiple difficulty levels.

### 3.2 BrowserGym interaction model

BrowserGym represents a browser-using conversational assistant. The user and agent exchange messages in a chat, while the agent can navigate pages, type, click, open tabs, extract information, and reply.

**Figure 2** shows the rendered interface: chat appears on the left and the live browser on the right.

The interaction is modeled as a **Partially Observable Markov Decision Process**:

- The environment supplies an observation and reward.
- The agent chooses an action.
- The environment executes it and returns the next observation.

“Partially observable” means the agent acts from the information exposed at the current step rather than from complete access to every hidden state of the website.

BrowserGym follows the Gym/Gymnasium API. Internally it uses Chromium and Playwright.

**Figure 3** connects the abstract loop—agent action followed by environment observation and reward—to concrete Python operations: create an environment with `gym.make`, call `reset`, repeatedly call `step(action)`, and stop when the episode is terminated or truncated.

### 3.3 Observation space

BrowserGym observations include:

- Task goal and/or chat history.
- Open tabs and pop-up windows.
- Current-page content.
- Raw DOM.
- Accessibility tree, or AXTree.
- A screenshot.
- Element properties.
- Error feedback from the preceding action.

**Figure 4** compares four views of the same page:

- A raw screenshot.
- A Set-of-Marks screenshot with element identifiers overlaid.
- HTML/DOM containing unique BrowserGym identifiers.
- A simplified AXTree identifying semantic elements such as the Upvote and Downvote buttons.

The DOM and AXTree are obtained through the Chrome Developer Protocol. BrowserGym makes minimally altered raw objects available and supplies utilities for converting them into basic text. Agents may filter irrelevant elements or attributes before prompting an LLM.

Every page element can receive:

- A unique **BrowserGym ID (`bid`)**, shared across the DOM and AXTree.
- A bounding box `(left, top, width, height)`.
- A visibility ratio between 0 and 1.
- A Set-of-Marks flag specifying whether its box should appear in an annotated screenshot.

Bounding boxes align exactly with screenshot pixel coordinates.

BrowserGym also exposes the URLs and titles of all open pages and an index for the active page. Instructions may be read from a separate goal object or from chat messages. Both can include text and images. Non-interactive goals are placed into the chat for compatibility, although later chat messages are not copied back into the goal. The authors recommend chat-based implementations because these can support and record interactive demonstrations.

Errors are retained in `last_action_error` instead of breaking the episode. **Figure 5** shows an attempted click on a Google Search button hidden by autocomplete. Playwright reports that another element intercepted pointer events, allowing the agent to react at the next step.

### 3.4 Action space

BrowserGym’s unrestricted action space is executable Python. An agent receives a Playwright page object and functions to communicate with the user or report that a task is infeasible. This is expressive but creates security risks because arbitrary code may be executed.

An optional **action mapping** converts a safer structured action—such as JSON or a command-like function call—into trusted Python. Parsing or conversion errors are returned to the agent.

The default `HighLevelActionSet` maps function-like primitives to Playwright operations. **Figure 6** contrasts raw Playwright or JavaScript with high-level actions such as clicking by `bid`, pressing Enter, or clicking screen coordinates. Raw code is more flexible; high-level primitives offer tighter control and require less knowledge of page structure.

**Table 3** lists the high-level primitives:

- Element actions: fill, click, double-click, hover, press, focus, clear, select options, drag and drop, and upload files.
- Coordinate actions: mouse movement, button down/up, click, double-click, drag-and-drop, and file upload.
- Keyboard actions: key down/up, key combinations, typing, and text insertion.
- Tab actions: open, close, or focus a tab.
- Navigation: back, forward, and go to a URL.
- Miscellaneous: send a message, report infeasibility, scroll, or wait.

**Figure 10** shows how the action set is described to an agent, including typed signatures, explanations, examples, scrolling direction conventions, and the rule that only one action is allowed at a time.

### 3.5 Creating new tasks

A new BrowserGym task requires two principal methods:

- `setup()` prepares the browser and returns the goal. Preparation can include logging in, creating records, or navigating to a starting URL. The goal may be plain text or multimodal messages.
- `validate()` runs after each action and checks the page, backend records, or chat for task completion. It returns a scalar reward, a termination flag, and optionally a user-facing message.

**Figure 7** illustrates a small task that opens Google, asks for Einstein’s birth year, and awards success if the assistant replies with “1879.”

### 3.6 Unified benchmarks

**Table 1** describes the supported benchmarks:

| Benchmark | Task templates | Seed diversity | Maximum steps | Multi-tab | Backend |
|---|---:|---|---:|---|---|
| MiniWoB(++) | 125 | Medium | 10 | No | Self-hosted pages |
| WebArena | 812 | None | 30 | Yes | Self-hosted Docker |
| VisualWebArena | 910 | None | 30 | Yes | Self-hosted Docker |
| WorkArena L1 | 33 | High | 30 | No | ServiceNow demo instance |
| WorkArena L2 | 341 | High | 50 | Yes | ServiceNow demo instance |
| WorkArena L3 | 341 | High | 50 | Yes | ServiceNow demo instance |
| WebLINX | 31,586 | None | 1 | No | Static dataset; no web backend |
| AssistantBench | 214 | None | 30 | Yes | Open web |

All tasks are accessed through the same Gymnasium interface. **Figure 8** demonstrates that a synthetic MiniWoB checkbox task and a realistic WebArena forum task can be created through corresponding `gym.make(...)` calls and handled through the same API.

The unification is intended to:

- Break research silos and encourage general-purpose agents.
- Make new benchmarks immediately compatible with existing agents.
- Reduce noise by testing hypotheses across benchmarks instead of relying on one benchmark’s biases.

Coverage ranges from synthetic interfaces and website replicas to enterprise workflows, open-web searches, and imitation of recorded human actions. GAIA, WebVoyager, WebShop, and Mind2Web-Live were being considered for later integration.

Each benchmark supplies metadata, default train/test splits, suggested action sets, seed counts, step limits, and, where needed, task dependency graphs. BrowserGym’s `prepare_backend()` can check configuration and reset WebArena or VisualWebArena Docker services between evaluations.

Appendix B adds benchmark-specific details:

- MiniWoB uses self-contained JavaScript pages and supports collision-free parallelism.
- WebArena contains six self-hosted domains. Validation uses HTML, URLs, messages, exact matching, or semantic matching with GPT-3.5.
- VisualWebArena retains two WebArena domains and adds another. It includes image-conditioned goals and uses an open-source `blip2-flan-t5-xl` model for some visual validation.
- WorkArena requires a ServiceNow Personal Developer Instance. It validates through database queries and injected JavaScript and avoids trajectory collisions by design.
- AssistantBench’s 214 tasks involve more than 525 pages across 258 websites. It has 33 development and 181 test tasks. Test answers are hidden and predictions are submitted through an evaluation API.
- WebLINX converts recorded human interactions into single-step action-prediction tasks and gives partial-match scalar rewards.

### 3.7 AgentLab

AgentLab organizes experiments with a disk-backed **Study** object. A study configures agents and benchmarks, runs episodes, saves results and reproducibility information, and relaunches failed jobs. Automatic execution retries failed tasks up to three times; incomplete runs can also be found and relaunched manually.

Experiments use multiprocessing with Joblib or Ray. Because most computation occurs on external LLM or web servers, the authors report that a laptop can launch up to 20 tasks concurrently and a large server can launch 50–100. API rate limits often become the bottleneck. Ray can distribute workers across machines.

Task dependencies constrain WebArena and VisualWebArena to roughly 2–4 concurrent tasks in the dependency-aware configuration. The paper later also notes that database collisions can require one agent at a time in some deployments.

### 3.8 AgentXRay and reproducibility

**Figure 9** shows AgentXRay, a Gradio-based trace-analysis interface. It includes:

- Agent and task selection.
- Task and seed statistics.
- Goal and episode information.
- Chosen action, reasoning, and error.
- A step-by-step profiling timeline.
- Tabs for screenshots, prompts, DOM, AXTree, chat, logs, statistics, and agent information.

Its purpose is to identify the precise step where an agent made an incorrect or suboptimal decision.

Sources of non-reproducibility include:

- Package and Playwright versions.
- Silent changes to API-served models.
- Changing live websites, layouts, content, language, or regional defaults.
- LLM stochasticity.
- Residual task stochasticity even under a fixed seed.

AgentLab mitigates these through standardized representations, benchmark-default action spaces, and saved metadata including benchmark and package versions, commit hashes, operating system, and timestamps.

A reproducibility journal records agent identity, BrowserGym and AgentLab versions, benchmark metadata, and results. The leaderboard can display reproduced scores as a range alongside an original result.

A `ReproducibilityAgent` replays an existing GenericAgent action sequence on the same seeds. AgentXRay then displays prompt differences between runs. Episodes may diverge quickly, but early-step differences can reveal changes in a live benchmark.

### 3.9 Creating agents and integrating models

A minimal agent defines an action set and implements `get_action(observation)`, which returns an action string and optional `AgentInfo` for later inspection.

An `AgentArgs` data structure records configuration and makes agents reliably serializable across processes. It may also apply benchmark-specific settings.

AgentLab provides a unified model interface through `BaseModelArgs` and `AbstractChatModel`; only a callable query method is required. Implementations are supplied for OpenAI, Azure OpenAI, and OpenRouter models, with automatic cost and token tracking.

### 3.10 Dynamic prompting and GenericAgent

Raw HTML may exceed 1,000,000 tokens, and AXTree representations may exceed 100,000. Some open models support only about 8,000 tokens. AgentLab therefore builds prompts from configurable components and shrinks them recursively to a target length rather than simply cutting off the end. Shrinking may remove older history or truncate the lower portion of the page while preserving crucial instructions and examples.

**Figure 11** shows an example agent that constructs a prompt from the goal, observation, action description, and example; fits it to 40,000 tokens; calls a chosen chat model; parses the answer; and returns trace information. Flags control HTML, AXTree, tabs, focused elements, errors, histories, screenshots, Set-of-Marks, coordinate extraction, visibility filtering, and action descriptions.

The accompanying WorkArena prompt demonstrates a task to find duplicated expense lines and retain only the most expensive duplicate. It includes the current AXTree, interaction history, the 20-action set, operational tips, and required `<think>`/`<action>` formatting.

**Table 4** gives the experimental GenericAgent configuration:

- Uses AXTree, focused-element information, current error logs, action history, full reasoning history, visibility/clickability tags, chain-of-thought, and abstract and concrete examples.
- Does not use HTML, old-error history, coordinates, a continuously refined plan, self-criticism, multi-action output, long action descriptions, or per-action examples.
- Screenshots are disabled except for VisualWebArena; Set-of-Marks is not used in the reported configuration.

GenericAgent can also use memory, screenshots, Set-of-Marks, self-criticism, and examples under other settings. Parsing failures trigger reprompting, with up to four attempts; four consecutive failures terminate the task.

### 3.11 Experimental design

The experiment evaluates GenericAgent with six models:

- Claude 3.5 Sonnet, checkpoint 2024-10-22.
- GPT-4o, checkpoint 2024-08-06.
- GPT-4o Mini, checkpoint 2024-07-18.
- o1 Mini, checkpoint 2024-09-12.
- Llama 3.1 70B.
- Llama 3.1 405B.

GPT models use Azure OpenAI; o1 Mini, Claude, and the Llama models use OpenRouter.

The primary metric is **task success rate**, with standard error calculated as the sample standard deviation divided by the square root of the number of episodes.

The agent uses the WorkArena++ configuration plus full chain-of-thought history. Visual input is used only on VisualWebArena and only for multimodal models. For most WorkArena L3 model combinations, prior results from a closely related agent were reused to reduce resource use; Claude was evaluated directly. Some least-promising WorkArena L3 runs were skipped for budget reasons and displayed as zero.

**Table 5** reports evaluation sizes:

| Benchmark | Templates/tasks | Seeds or split | Maximum steps | Episodes |
|---|---:|---|---:|---:|
| MiniWoB | 125 | 5 seeds | 10 | 625 |
| WebArena | 812 | Entire benchmark | 30 | 812 |
| VisualWebArena | 910 | Entire benchmark | 30 | 910 |
| WorkArena L1 | 33 | 10 seeds | 30 | 330 |
| WorkArena L2 | 341 | Preset curriculum | 50 | 235 |
| WorkArena L3 | 341 | Preset curriculum | 50 | 235 |
| WebLINX | 31,586 | Test split | 1 | 2,650 |
| AssistantBench | 214 | Test set | 30 | 181 |

## 4. Results and Findings

### 4.1 Main benchmark results

**Table 2** reports success rate in percent, with standard error:

| Benchmark | Episodes | Claude 3.5 | GPT-4o | GPT-4o Mini | Llama 70B | Llama 405B | o1 Mini |
|---|---:|---:|---:|---:|---:|---:|---:|
| MiniWoB | 625 | **69.8 ± 1.8** | 63.8 ± 1.9 | 56.6 ± 2.0 | 57.6 ± 2.0 | 64.6 ± 1.9 | 67.8 ± 1.9 |
| WorkArena L1 | 330 | 56.4 ± 2.7 | 45.5 ± 2.7 | 27.0 ± 2.4 | 27.9 ± 2.5 | 43.3 ± 2.7 | **56.7 ± 2.7** |
| WorkArena L2 | 235 | **39.1 ± 3.2** | 8.5 ± 1.8 | 1.3 ± 0.7 | 2.1 ± 0.9 | 7.2 ± 1.7 | 14.9 ± 2.3 |
| WorkArena L3 | 235 | **0.4 ± 0.4** | 0.0 ± 0.0 | 0.0 ± 0.0 | 0.0 ± 0.0 | 0.0 ± 0.0 | 0.0 ± 0.0 |
| WebLINX | 2,650 | **13.7 ± 0.6** | 12.5 ± 0.6 | 11.6 ± 0.6 | 8.9 ± 0.5 | 7.9 ± 0.5 | 12.5 ± 0.6 |
| WebArena | 812 | **36.2 ± 1.7** | 31.4 ± 1.6 | 17.4 ± 1.3 | 18.4 ± 1.4 | 24.0 ± 1.5 | 28.6 ± 1.6 |
| VisualWebArena | 910 | 21.0 ± 1.3 | **26.7 ± 1.5** | 16.9 ± 1.2 | Not evaluated | Not evaluated | Not evaluated |
| AssistantBench | 181 | 5.2 ± 1.5 | 4.8 ± 2.4 | 2.1 ± 1.0 | 2.8 ± 1.1 | 3.9 ± 1.0 | **6.9 ± 2.2** |

Principal patterns were:

- Claude 3.5 Sonnet led most benchmarks.
- GPT-4o was best on VisualWebArena, the explicitly visual benchmark.
- o1 Mini narrowly led WorkArena L1 and had the best AssistantBench score.
- WorkArena L2 showed the largest separation: Claude reached 39.1%, compared with 14.9% for o1 Mini and 8.5% for GPT-4o.
- WorkArena L3 remained almost entirely unsolved; Claude completed only 0.4%, and all displayed alternatives were zero.
- Llama 3.1 70B was often close to GPT-4o Mini.
- Llama 3.1 405B substantially exceeded GPT-4o Mini on several benchmarks, including MiniWoB, WorkArena L1/L2, WebArena, and AssistantBench, although not WebLINX.
- No statistical hypothesis-test p-values were reported; uncertainty is expressed as standard errors.

GPT-4o improved over an earlier closely related evaluation:

- WebArena increased from 23.5% to 31.4%.
- WorkArena L2 increased from 3.8% to 8.5%.

Because the agent implementations were similar but the model checkpoint was newer, the authors suggest improved model reasoning as one explanation. They also acknowledge the possibility that public benchmark material entered model training data.

AssistantBench remained particularly weak. The best score in this experiment was o1 Mini’s 6.9%, compared with a reported 27% leaderboard high score. The authors attribute the gap to GenericAgent being general-purpose rather than specialized for information retrieval.

### 4.2 Claude cost and episode length by benchmark

Table 2 also reports Claude’s API cost and mean steps:

| Benchmark | Claude cost | Mean steps |
|---|---:|---:|
| MiniWoB | $23.11 | 3.7 |
| WorkArena L1 | $100.03 | 9.0 |
| WorkArena L2 | $299.44 | 33.8 |
| WorkArena L3 | $191.50 | 25.0 |
| WebLINX | $104.62 | 1.0 |
| WebArena | $138.76 | 6.8 |
| VisualWebArena | $134.69 | 4.7 |
| AssistantBench | $37.33 | 7.5 |

WorkArena L2 was both successful relative to other models and expensive, with the longest average trajectory.

### 4.3 Overall model costs

**Table 6** sums costs and tokens over all benchmarks except VisualWebArena:

| Model | Total cost | Input tokens | Output tokens | Input price per million | Output price per million |
|---|---:|---:|---:|---:|---:|
| Claude | $894.80 | 276.20M | 4.41M | $3.00 | $15.00 |
| GPT-4o | $720.72 | 277.25M | 2.76M | $2.50 | $10.00 |
| GPT-4o Mini | $75.73 | 479.72M | 6.29M | $0.15 | $0.60 |
| Llama 3.1 405B | $849.63 | 359.89M | 8.13M | $2.30 | $2.30 |
| Llama 3.1 70B | $78.79 | 221.23M | 5.02M | $0.35 | $0.35 |
| o1 Mini | $971.12 | 171.25M | 38.11M | $3.00 | $12.00 |

o1 Mini was the most expensive overall and produced far more output tokens than the other models. GPT-4o Mini and Llama 70B were much cheaper. The paper cautions that OpenRouter’s Llama pricing may have changed since the experiment.

### 4.4 Runtime

**Table 7** reports Claude 3.5 Sonnet runtime without crediting parallel execution:

| Benchmark | Cumulative experiment hours | Mean step seconds | Environment hours | Environment seconds/step | Steps |
|---|---:|---:|---:|---:|---:|
| AssistantBench | 4.0 | 9.1 | 2.0 | 4.5 | 1,590 |
| MiniWoB | 3.1 | 5.0 | 0.7 | 1.1 | 2,282 |
| WebArena | 18.6 | 12.2 | 11.6 | 7.6 | 5,493 |
| WebLINX | 4.5 | 6.1 | 0.1 | 0.2 | 2,649 |
| WorkArena L1 | 8.2 | 9.9 | 4.4 | 5.3 | 2,985 |
| WorkArena L2 | 23.6 | 10.7 | 10.9 | 4.9 | 7,947 |
| WorkArena L3 | 16.1 | 9.8 | 7.4 | 4.5 | 5,884 |
| VisualWebArena | 16.9 | 14.1 | 10.5 | 8.8 | 4,319 |

WorkArena L2 had the greatest cumulative workload. VisualWebArena had the slowest average steps. Differences between total and environment time largely reflect model/API processing.

Runs used up to 20 parallel jobs where possible. Experiments ran on clusters with Intel Xeon Gold 6126 2.60 GHz CPUs and effectively unlimited RAM, although the authors state that the core workload can run on ordinary laptops. WebArena used Azure virtual machines with 8 CPUs and 32 GB RAM, limiting throughput.

### 4.5 Error analysis

The paper groups failures into:

- Navigation errors.
- Form-handling errors.
- Task-understanding errors.
- Repeated or stuck behavior.
- Information-extraction failures.
- External API, network, or system errors.

The analysis is qualitative rather than a counted error taxonomy. Full traces are released for inspection in AgentXRay.

**Figures 12 and 13** compare Claude and GPT-4o on the same WorkArena L2 task: ordering six Standard Laptops with Salesforce, Microsoft Office 365, Asana, HubSpot, Adobe Acrobat, and Adobe Photoshop.

- **Figure 12:** Claude opens the All menu, enters the catalog, navigates to hardware, selects Standard Laptop, completes the fields, and submits the order. When clicking a checkbox fails because its label intercepts pointer events, Claude reads the AXTree, identifies the label’s `bid`, clicks the label instead, and recovers.
- **Figure 13:** GPT-4o attempts to select quantity six by clicking menu item `a243` rather than using `select_option`. The action fails, but GPT-4o’s subsequent reasoning incorrectly assumes the quantity was set to six. It completes an order for one laptop and fails the task.

The example illustrates two contrasting behaviors: Claude uses error and structural feedback to revise its strategy, while GPT-4o preserves an incorrect belief from its previous reasoning history.

## 5. Analysis and Interpretation

The study demonstrates that a single agent implementation can be evaluated across substantially different environments without separate benchmark-specific code. This supports the paper’s main claim that BrowserGym and AgentLab reduce experimental fragmentation.

Claude’s broad lead suggests that model choice strongly influences web-agent ability even when the agent scaffold, prompting strategy, and action interface are held constant. The authors propose that Claude’s computer-use-oriented training may help explain its 39.1% WorkArena L2 result.

GPT-4o’s win on VisualWebArena shows a different strength: it performed best where visual interpretation was essential. Thus, Claude’s overall advantage did not extend to the primary vision-focused benchmark.

The open-weight results were mixed but encouraging. Llama 405B remained behind leading proprietary models on difficult reasoning benchmarks, yet often exceeded GPT-4o Mini. This indicates that open-weight models could be competitive on a meaningful subset of web tasks.

The low scores on WorkArena L3 show that complex compositional enterprise workflows remain largely beyond all evaluated agents. AssistantBench likewise reveals that a general interface and agent do not automatically match a specialized retrieval system.

The case study explains one source of performance differences: reliable agents must not merely generate plausible plans; they must use environment feedback to verify whether actions actually succeeded. Preserving reasoning history can aid consistency, but it can also propagate false assumptions, as seen with GPT-4o.

The authors emphasize that BrowserGym’s value is broader than a leaderboard. Cross-benchmark evaluation provides a stronger basis for testing whether a model, screenshot representation, prompting strategy, or action space truly helps, rather than fitting conclusions to one benchmark’s peculiarities.

## 6. Contributions and Novelty

The paper’s main contributions are:

- An expanded **BrowserGym**, exposing heterogeneous web-agent benchmarks through a common Gymnasium interface.
- Integration of WebLINX, VisualWebArena, and AssistantBench alongside MiniWoB, WebArena, and WorkArena.
- Standardized, configurable observations combining chat, goals, tabs, DOM, AXTree, screenshots, semantic identifiers, geometry, visibility, and action errors.
- A flexible action system ranging from unrestricted Python to restricted high-level primitives.
- A minimal interface for adding new benchmarks through `setup` and `validate`.
- **AgentLab**, covering agent construction, dynamic prompting, model-provider abstraction, parallel studies, retries, logging, cost tracking, and benchmark-specific configuration.
- **AgentXRay**, a visual tool for inspecting complete step-by-step traces.
- Reproducibility mechanisms including metadata logging, journals, replay agents, visual prompt diffs, and reproduced-score ranges on a leaderboard.
- The first unified large-scale comparison of six current LLMs/VLMs across the BrowserGym benchmark ecosystem.
- A then-unprecedented 39.1% success rate by Claude 3.5 Sonnet on WorkArena L2, versus 8.5% for GPT-4o.
- Public trace data and an online leaderboard intended to support follow-up analysis and evolving comparisons.

## 7. Limitations and Caveats

### Experimental limitations

- VisualWebArena was evaluated only with multimodal models.
- Visual inputs were deliberately withheld on other benchmarks, so the experiment does not test whether vision could improve those tasks.
- Many non-Claude WorkArena L3 values came from prior closely related evaluations or were skipped for budget reasons. Displayed zeroes therefore do not always mean a fresh full run.
- Error analysis was qualitative; the experiment did not quantify the prevalence of each failure category.
- API prices and hosted model behavior can change.
- Public benchmark availability creates a possible contamination concern.
- GenericAgent was not specialized for retrieval, which limits interpretation of its AssistantBench performance.
- Success rate and standard error were reported, but no formal significance tests or p-values were supplied.

### Reproducibility limitations

Even with logging and replay, results can change because of:

- LLM and software updates.
- Operating-system and browser differences.
- Time zones, language defaults, geographic settings, and localization.
- Dynamic pages, advertisements, and changing content.
- Stochastic models and tasks.

### Safety and operational risks

- Unrestricted Python actions can execute arbitrary untrusted code.
- Open-web agents may take consequential actions on a user’s behalf. BrowserGym mitigates this through URL protection on closed benchmarks and warning notices, but open-web tasks remain risky.
- CAPTCHA, IP rate limits, and automated-behavior detection can block agents. AssistantBench is the benchmark currently most affected.
- Concurrent agents may modify the same database records or shopping carts. This causes collisions and can force serial evaluation.
- Task dependency graphs reduce WebArena/VisualWebArena parallelism.
- The synchronous interaction loop may create delays when a task requires several rapid actions.
- BrowserGym is not yet a consumer-ready automation system.

### Broader societal caveats

The authors warn that capable UI agents could automate work quickly and cheaply, producing economic benefits but also rapid job displacement. Prompt-injection and related attacks could eventually leak private information, authorize unwanted transactions, or cause other harms.

Autonomous agents may also disrupt online advertising. Their browsing behavior, ad filtering, and limited likelihood of engaging like humans could alter impressions, clicks, conversions, and publisher revenue. The paper calls for standardized approaches that balance automation with sustainable advertising models.

## 8. Future Work or Open Questions

The authors identify several directions:

- Build stronger safety benchmarks and mechanisms covering privacy-policy compliance, malicious interactions, and prompt injection.
- Develop secure environments suitable for enterprise or sensitive use.
- Create real-time agents whose latency and decision speed approach human interaction.
- Improve smaller models so they retain complex web reasoning with lower computation and deployment cost.
- Use stronger computer-level VLMs to understand complex layouts and graphical information.
- Adapt inference-time scaling and self-reflection specifically to web tasks.
- Improve agents’ ability to react to failed actions instead of repeating errors or trusting incorrect prior reasoning.
- Conduct deeper, preferably automated, error analysis over the released traces.
- Use BrowserGym’s complete logs as training or fine-tuning data.
- Continue integrating benchmarks such as GAIA, WebVoyager, WebShop, and Mind2Web-Live.
- Improve solutions for live-site change, localization, robot detection, agent collisions, and synchronous interaction bottlenecks.
- Establish social policies and technical frameworks before UI agents are deployed widely.

## 9. High-Level Takeaway (Plain Language)

BrowserGym gives researchers one common way to test AI systems that operate websites, while AgentLab provides the tools needed to build those systems, run many trials, inspect mistakes, and record enough information to repeat experiments. Testing six models showed that Claude 3.5 Sonnet was strongest overall and dramatically better on difficult enterprise tasks, while GPT-4o was better on the visual benchmark. Yet even the best model failed most complex tasks—and almost all WorkArena L3 tasks—showing that reliable, safe browser automation remains far from solved.