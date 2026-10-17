## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–21, together with rendered images for pages 1–9, 11, and 13–21. All 21 page texts were inspected. The 19 supplied page images were visually inspected, including the substantive figures and tables appearing on those pages. Pages 10 and 12 received text-only inspection because their rendered images were not supplied. The isolated image-loading error does not establish that a numbered paper page is missing: the corresponding numbered text and the other attached images remain available.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes, as supplied page text and partial page rendering |
| Accessible physical PDF pages | 1–21; 21 page texts and 19 page images |
| Apparently missing numbered pages | None within the supplied 1–21 sequence |
| Visual content | Available for every numbered substantive figure, Figures 1–11 |
| Tables | Tables 1–10 available in text and rendered pages; small type requires cross-checking against extracted text |
| Equations | No numbered mathematical equations identified in the supplied work |
| Appendices | Appendix A, §§A.1–A.3, and Appendix B, §§B.1–B.2, are present |
| Supplementary files | No supplementary files supplied; no embedded file is reported in the accessibility metadata |
| Referenced external artifacts | WorkArena, BrowserGym, and AgentLab repositories; ServiceNow developer instances; cited papers and documentation were not inspected |
| OCR | Not needed for the supplied text; no additional OCR performed |
| Remaining limitations | Fine screenshot text and Figure 4's exact distribution statistics cannot all be read confidently; no repository implementation or raw experimental data was reviewed |

The metadata's empty appendix-detection list is contradicted by plainly supplied headings on pages 13 and 20. The document itself establishes that appendices are present. The supplied checksum is retained as an identifier; it was not independently recomputed. No tools, external browsing, execution, or outside information were used.

Evidence categories throughout this report are: [A] AUTHOR-REPORTED, [B] DIRECTLY OBSERVABLE, [C] ANALYST-DERIVED, and [D] ANALYST INTERPRETATION. Confidence is HIGH, MEDIUM, LOW, or UNKNOWN. There is no [E] external evidence in this analysis. Page references mean physical PDF page numbers, which agree with the printed page numbers here.

## 1. Plain-language orientation

[A; HIGH] This paper asks how well language-model-based agents can perform ordinary workplace tasks through a web browser. A web agent reads information about a page, decides what to do, and clicks, types, navigates, or sends an answer. Its job is more demanding than producing a plausible paragraph: it must successfully manipulate an actual software interface and reach a verifiable outcome.

The researchers introduce two different contributions. **WorkArena** is a benchmark: a collection of tasks used to measure performance. It contains 33 task types and 19,912 parameterized instances on ServiceNow, an enterprise software platform. **BrowserGym** is an execution and evaluation environment: it supplies page observations, browser actions, a chat interface, and task validation. The paper also evaluates agents built around GPT-4o, GPT-3.5, and Llama3-70B, including a screenshot-augmented GPT-4o condition. [pp. 1–7]

The central finding is that realistic enterprise interfaces remain difficult. In the final evaluation, WorkArena success was 42.7% ± 1.5 for GPT-4o, 41.8% ± 1.7 for screenshot-augmented GPT-4o, 6.1% ± 1.3 for GPT-3.5, and 17.9% ± 1.5 for Llama3. These are success rates with reported standard errors, not confidence intervals. Every agent scored 0.0% on the list-filter category, while other categories were substantially easier. [p. 7, Table 2]

The work is a benchmark, systems, and empirical AI paper. It is **not a comparative security experiment** between web agents and standalone large language models. For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', its relevance is [D; MEDIUM]: it documents how language models become connected to external observations, executable actions, enterprise records, and user identities. Those connections identify possible security-relevant boundaries. The paper does not measure attack success, establish greater vulnerability, or isolate a causal mechanism for such a comparison.

## 2. Document roadmap

The original title is **WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?** The authors are Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, and Alexandre Lacoste. Drouin and Gasse are marked as equal contributors; Caccia and Lacoste as core contributors. Affiliations include ServiceNow Research, Mila, Polytechnique Montréal, McGill University, and Université de Montréal. The first page identifies the Proceedings of the 41st International Conference on Machine Learning, Vienna, PMLR 235, 2024, and arXiv:2403.07718v5, dated 23 July 2024. These are supplied bibliographic statements, not externally verified metadata.

| Inventory ID | Original component | Pages | Function |
|---|---|---:|---|
| S0 | Abstract | 1 | Problem, benchmark, environment, performance gap |
| S1 | §1 Introduction | 1–2 | Motivation for enterprise UI assistants |
| S2 | §2 Related Works | 2–3 | Benchmark and agent positioning |
| S3 | §3 WorkArena – An Enterprise Benchmark | 3–5 | Benchmark scope and task design |
| SS3.1 | §3.1 WorkArena Tasks | 3–4 | Six task categories, goals, validation, oracles |
| SS3.2 | §3.2 Challenges: the World Wild Web of Work | 4–5 | Dynamic interfaces, unusual HTML, large observations |
| SS3.3 | §3.3 Availability | 5 | Open-source benchmark and cloud deployment |
| S4 | §4 BrowserGym | 5–6 | Browser environment and implementation |
| SS4.1 | §4.1 Capabilities | 5–6 | Chat, observations, actions, navigation |
| SS4.2 | §4.2 An Ideal Experimental Framework | 6 | Agent flexibility and task lifecycle |
| S5 | §5 Experiments | 6–9 | Performance and feature evaluation |
| SS5.1 | §5.1 Agent Design | 6–7 | Prompting, features, models, truncation |
| SS5.2 | §5.2 Experimental Protocol | 7 | Seeds, bootstrap, steps, model selection |
| SS5.3 | §5.3 Results | 7–8 | Benchmark comparisons and author conclusions |
| SS5.4 | §5.4 Ablation Study | 8–9 | Feature changes and interpretations |
| S6 | §6 Conclusion | 9 | Contributions and future development |
| S7 | Impact Statement | 10 | Productivity, accessibility, labor, security, privacy, energy |
| S8 | References | 10–12 | Bibliographic support; not independent evidence reviewed here |
| A1 | Appendix A, §A.1 Tasks | 13 | All 33 task names, instance counts, oracle actions |
| A2 | Appendix A, §A.2 Task User Interface Examples | 13–17 | Annotated task screenshots |
| A3 | Appendix A, §A.3 Knowledge Base Tasks – Additional Details | 18–19 | Synthetic articles, questions, acceptable answers |
| B1 | Appendix B, §B.1 Action Space | 20 | Full BrowserGym primitive inventory |
| B2 | Appendix B, §B.2 MiniWoB | 20–21 | Benchmark port and illustrated task |

The visual inventory is Figures F1–F11 and Tables T1–T10, retaining original numbering. There are no numbered algorithms, proofs, theorems, or equations. There is no supplied keyword list. The experimental register contains X1 final benchmark comparison, X2 GPT-4o ablations, X3 GPT-3.5 ablations, X4 Llama3 ablations, X5 screenshot augmentation, and X6 observation-size comparison. Random configuration search is a model-selection procedure, not a fully reported standalone search experiment. Preliminary Llama2 failure is a secondary observation with limited setup detail.

## 3. Background and context

[A; HIGH] A **large language model (LLM)** supplies the reasoning and action-generation component. A **user interface (UI)** is the visible software surface containing forms, menus, lists, buttons, and charts. An **application programming interface (API)** permits programmatic interaction with software. The authors favor studying direct UI interaction because it can expose the assistant's activity to the user and allow the user to regain control. This is an argument about possible transparency and oversight, not a measured safety guarantee. [p. 1]

A **Document Object Model (DOM)** represents the page's structure. Here, its rendered HTML can be converted to text and passed to the agent. An **accessibility tree (AXTree)** is another structured page representation offered by BrowserGym. The paper uses AXTrees instead of HTML on WorkArena and WebArena because their HTML is too large. On MiniWoB the agents use both HTML and AXTree. [pp. 5–6]

BrowserGym augments elements with **bid**, a unique identifier, bounding-box coordinates, and visible/clickable flags. The identifier allows an action to target a specific element without deciding pixel coordinates. A **coordinate action** instead specifies an x,y location. A screenshot supplies the rendered pixels. These are different descriptions of the same active page; availability in the environment does not mean every experimental agent used all of them. [pp. 5–6]

**Chain-of-thought prompting**, as used by the authors, asks the model to generate reasoning before its next action. **Action history** adds earlier actions to the current prompt; **error history** adds earlier error messages; **thought history** adds earlier reasoning outputs. These are prompt construction choices, not separately trained memory systems. The report describes them at the methodological level without reproducing private model reasoning. [pp. 6–7]

A **zero-shot agent** here has no task-specific worked examples, although it receives one generic output-format example and may receive individual action-call examples. Thus zero-shot does not mean the absence of instructions or all examples. [p. 7]

A **task type** differs from an **instance**. For example, creating a user is one task type, while distinct names and field values produce multiple instances. The 19,912 available instances are not the number of evaluated episodes. A **benchmark** measures defined outcomes; an **oracle** is a hand-written solution demonstrating feasibility; a **validator** checks the resulting state or answer. [pp. 3–4, 13]

## 4. Research problem and gap

[A; HIGH] The practical problem is that everyday enterprise software work can be repetitive, difficult to learn, and cumbersome even when its individual goals sound simple. The authors also motivate assistance for users with visual impairments. Enterprise interfaces may favor functionality over ease of use. [p. 1]

According to the authors, earlier benchmarks cover toy interfaces, shopping, consumer information retrieval, and realistic web applications such as forums or collaborative software development. WorkArena fills their identified gap in enterprise software tasks. It aims to complement those benchmarks rather than replace them. [pp. 2–3]

The technical gap is not merely the ability to understand an instruction such as 'create a user.' An agent must find the right widget, expose hidden fields, satisfy dependencies, handle auto-completion, interpret charts, and distinguish repeated menu labels. WorkArena combines non-standard interfaces with large page descriptions and real cloud-hosted ServiceNow instances. [pp. 3–5]

The authors position BrowserGym as a unified environment combining multimodal observations, code and higher-level actions, chat interaction, and support for several benchmarks. Their claim to novelty in chat-based agent-user interaction is an author claim about prior work; this closed-document analysis does not independently establish priority. [pp. 2–3, 5]

The scope of the empirical contribution is agents relying on language models for reasoning. It is not an evaluation of every possible browser automation architecture, every enterprise platform, or all modalities supported by the environment. No dedicated security benchmark or adversarial workload is introduced.

## 5. Research questions, objectives, and hypotheses

The title poses the broad capability question: how capable are web agents at solving common knowledge work tasks? The paper does not enumerate formal research questions or preregistered hypotheses.

[A; HIGH] Its explicit experimental objectives are:

1. Situate WorkArena's difficulty by comparing models and benchmarks. [p. 6, §5]
2. Quantify the impact of BrowserGym features through ablations. [p. 6, §5]

Its broader development objectives are to provide a realistic enterprise benchmark, support flexible agent evaluation, and help study automation's potential effects on accessibility, user experience, and productivity. Those effects are motivations; worker productivity and accessibility improvements are not measured outcomes in this paper.

[A; MEDIUM] The authors hypothesize that added prompt content may distract weaker models because the AXTree is already large, and note that extra content also causes more truncation. They suggest limited screen-related training data as a possible explanation for weak multimodal improvements. These are explanatory hypotheses, not directly tested causal conclusions. [pp. 8–9]

[D; MEDIUM] The user's security research question can use the paper to formulate questions about observation-to-action boundaries, authorization, identity changes, and sensitive-data handling. It cannot use the reported capability scores as measurements of vulnerability or as a standalone-LLM comparison.

## 6. Assumptions / Threat Model

[A; HIGH] BrowserGym follows a **Partially-Observable Markov Decision Process (POMDP)** paradigm. At each step it extracts observations from the current page view. The authors explicitly state that the agent must implement its own memory mechanism; BrowserGym does not supply that memory. The observation also includes chat, open-page URLs, and available error information. Partial observability therefore does not mean the agent receives only an image. [p. 5 and footnote continuing to p. 6]

WorkArena goals are generated from human-designed templates populated with predefined values and are intended to provide all information needed to solve the task. This design minimizes instruction ambiguity. Tasks are executed on real ServiceNow Personal Developer Instances. Validation and oracle functions are benchmark-controlled components; the study assumes they can correctly assess task success and feasibility. [pp. 3–6]

No formal attacker, malicious website, adversarial instruction, credential compromise, privilege model, or security trust boundary is specified. The paper does not define an attack success metric. The impact statement acknowledges cybersecurity and privacy concerns but does not supply a threat-model experiment. [p. 10]

[D; MEDIUM] For security analysis, one can distinguish the benchmark's intended user goal, external page content, model-generated action, execution environment, and resulting enterprise state. This separation is an analyst's reading of the architecture, not an author-specified adversarial model. The paper leaves unknown who can control each observation source, how permissions are limited, and how potentially conflicting instructions would be handled.

## 7. Methodology

### 7.1 Benchmark construction and validation

[A; HIGH] WorkArena contains six categories:

| Category | Task types | Available instances | Work performed | Success check |
|---|---:|---:|---|---|
| Lists | 12 | 6,900 | Six filtering tasks and six sorting tasks | Client-side check that list conditions are satisfied |
| Forms | 5 | 5,000 | Create a record with 1–26 fields | Query created database records and verify field values |
| Knowledge bases | 1 | 1,000 | Search articles and answer a factual question | Membership in a set of acceptable answers |
| Service catalogs | 9 | 3,550 | Select and configure products, then order quantities | Query orders for correct items, amounts, specifications |
| Dashboards | 4 | 1,862 | Read chart values or minima/maxima | Verify key numbers and chart labels in the answer |
| Menus | 2 | 1,600 | Navigate the All menu or impersonate a user | Expected location or expected logged-in user |

Source: pp. 3–4, §3.1; p. 13, Table 6. [C; HIGH] The category totals sum to 6,900 + 5,000 + 1,000 + 3,550 + 1,862 + 1,600 = 19,912, matching the reported total. The task counts sum to 12 + 5 + 1 + 9 + 4 + 2 = 33.

Filtering uses 1–5 conditions. Sorting can use up to three columns. Form difficulty depends on both field count and interface behavior. Catalog difficulty depends on configuration options. Dashboard difficulty depends on the number of charts and required reasoning. Menu navigation requires disambiguating applications and modules; impersonation changes the active user for an IT-support-style task. [pp. 3–4]

For combinatorially large list and form pools, the authors randomly cap instances at 1,000 per task where applicable. Available instance counts are uneven, with some catalog tasks containing only ten instances. The paper reports no train/validation/test split for this benchmark evaluation; configuration selection and later evaluation use different seeds. [pp. 7, 13]

### 7.2 Knowledge-base generation

[A; HIGH] The knowledge base contains 100 GPT-4-generated HTML articles built from 100 facts. Each fact is described as an item/value pair. GPT-4 generates ten alternative question wordings and formatting instructions. GPT-3.5 is then asked to answer each question from the article. Failed questions are revised by GPT-4 and retested. The stated rationale is to avoid GPT-4 generating ambiguous questions that it can nevertheless answer itself. [p. 18, §A.3]

GPT-4 also generates ten alternative answer formats; examples are supplied in the prompt and the results are inspected for coherence. This supports tolerance for superficial formatting differences. It is not described as unrestricted semantic answer evaluation. [pp. 18–19]

The text describing an inserted article string uses 'the {fact} is {item}', whereas the surrounding prose describes item/value pairs and Table 7 labels columns Fact/Item. The intended idea is a factual description paired with its answer, but the placeholder naming is inconsistent. This report does not silently rewrite that sentence into a verified generation template.

### 7.3 Environment and task lifecycle

[A; HIGH] BrowserGym is implemented as an OpenAI Gym environment using Chromium, the Chrome DevTools Protocol, and Playwright. Its observation includes chat messages, URLs of open pages, the last action's error stack trace, an HTML DOM snapshot, an AXTree, and a viewport screenshot. DOM and AXTree observations can be enriched with element identifiers, coordinates, and visibility/clickability attributes. [p. 5]

Its action space can be restricted to predefined primitives or permit arbitrary Python with the Playwright API. It supports multiple tabs, popups, nested iFrames, and shadow DOMs. Support for a capability is different from use in the selected experimental configuration: Table 1 uses bid actions and disables multiple actions per step for all three base agents. [pp. 5–6]

Tasks implement setup(), teardown(), validate(), and optionally cheat(). Setup creates required state, authenticates, and navigates. Teardown cleans task-created resources. Validate checks state, page content, URL, or chat and returns a reward, optional chat message, and completion flag. Cheat is an optional hard-coded oracle. WorkArena's oracle functions demonstrate feasibility and help identify tasks affected by platform updates. They are not necessarily optimal solutions. [pp. 3, 6, 13]

### 7.4 Agent configuration

[A; HIGH] The common agent codebase varies the LLM and feature flags. WorkArena and WebArena use AXTree alone; MiniWoB uses AXTree plus HTML. The current goal is provided, and flags determine inclusion of focused element, last error, coordinates, visibility tags, clickability tags, history, descriptions, and action examples. [pp. 6–7]

The agents receive one generic formatting example, with no task-specific few-shot examples. A parsing loop can reprompt up to four times to correct malformed output before execution. This loop addresses output parsing, not a demonstrated security or semantic correctness check. [p. 7]

Model identifiers and conditions are GPT-3.5: gpt-3.5-turbo-1106, reported 16K context; GPT-4o: gpt-4o-2024-05-13, reported 128K context; Llama3: meta-llama-3-70B-instruct, reported 8K context. Llama3 runs through Hugging Face Text Generation Inference on four A100 GPUs. Maximum agent prompt lengths are 15K, 40K, and 8K tokens respectively. When prompts exceed their limits, HTML and AXTree are progressively truncated from the end. [p. 7]

Experiments use BrowserGym v0.3.5 and WorkArena v0.3.0. AgentLab is linked as code, but no repository was inspected. Temperature, sampling parameters, exact random-search trial count, search ranges, API execution hardware, runtime, inference cost, and exact seed identifiers are not specified in the supplied account. [pp. 6–7]

### 7.5 Evaluation and statistics

[A; HIGH] There are ten seeds per task for WorkArena and MiniWoB, and one per WebArena task. The authors use stratified bootstrap to generate 1,000 samples of the mean, reporting the average and standard deviation of those means as success rate and standard error. The stratification details are not fully described. No formal hypothesis test or p-value is reported. [p. 7]

Each episode permits at most 15 steps. Some WorkArena tasks may need more steps unless multiple actions are permitted per step. The selected final configurations do not enable multi-action execution. Model configuration is selected by random search on MiniWoB and WorkArena, fixed per model, and then evaluated again using a different seed. WebArena is not used for tuning because it is described as deterministic. Ablations use a different seed from Table 2. [pp. 7–8]

[C; HIGH] The stated protocol implies 33 × 10 = 330 WorkArena task-seed episodes and 125 × 10 = 1,250 MiniWoB episodes per full configuration, if every stated task-seed pair is run once. Table 2's 812 WebArena tasks at one seed imply 812 episodes. These are protocol-derived counts, not separately reported execution receipts.

## 8. Experiments / Analyses

| Experiment | Purpose and manipulated condition | Evidence | Results and caveats |
|---|---|---|---|
| X1 Final benchmark comparison | Compare underlying LLMs using selected configurations on WorkArena, MiniWoB, WebArena | Table 1 configuration; Table 2 performance | GPT-4o leads the three base models; model and feature configuration vary together; no standalone-LLM baseline |
| X2 GPT-4o ablations | Modify one displayed row's features relative to its initial condition | Table 3 | Coordinates improve MiniWoB but reduce WorkArena; baseline differs from final evaluation seed |
| X3 GPT-3.5 ablations | Remove thinking/history/examples or add observations/actions/descriptions | Table 4 | Thinking and action history help; thought history hurts; most small effects are not tested for significance |
| X4 Llama3 ablations | Change thinking, histories, multiple actions, descriptions, last error, visibility tags | Table 5 | Removing thinking or action history strongly reduces scores; thought-history pattern differs from GPT agents |
| X5 Screenshot augmentation | Add Set-of-Mark screenshot to GPT-4o while preserving its other selected flags | Table 2; §5.4 | Slight gains on MiniWoB/WebArena; lower aggregate WorkArena score; category-level effects vary |
| X6 Observation-size comparison | Compare pruned HTML and AXTree sizes across three benchmarks | Figure 4 | Enterprise and realistic-page observations are larger; exact distribution summaries not provided |

X1 answers the objective of situating benchmark difficulty. It evaluates task completion, not reasoning quality in isolation. X2–X4 answer the feature-impact objective but several rows change two coupled aspects, such as coordinate observations and coordinate actions. These rows cannot separately establish which component caused the change.

X5 tests screenshot augmentation in one particular agent configuration. It does not test a screenshot-only agent or retrain the underlying model for screen understanding. X6 motivates context-management choices but does not experimentally isolate prompt length as the sole reason for failure.

[A; MEDIUM] A secondary preliminary result states that a Llama2 model achieved flat 0% on WorkArena and WebArena. No comparable full protocol, model identifier, or result table is supplied for that preliminary observation. It should not carry the same evidentiary weight as Table 2.

## 9. Results

### 9.1 Final benchmark performance

[A; HIGH] Table 2 gives the following exact aggregate success rates, in percent ± standard error:

| Benchmark | GPT-4o | GPT-4o-V | GPT-3.5 | Llama3 |
|---|---:|---:|---:|---:|
| WorkArena, 33 tasks | 42.7 ± 1.5 | 41.8 ± 1.7 | 6.1 ± 1.3 | 17.9 ± 1.5 |
| MiniWoB, 125 tasks | 66.1 ± 1.0 | 67.7 ± 1.0 | 38.9 ± 1.1 | 62.6 ± 0.6 |
| WebGum subset, 56 tasks | 82.9 ± 1.5 | 83.2 ± 1.5 | 53.6 ± 1.4 | 80.5 ± 1.0 |
| WebArena, 812 tasks | 23.5 ± 0.7 | 24.0 ± 0.6 | 6.7 ± 0.6 | 11.0 ± 0.6 |

[C; HIGH] On WorkArena, GPT-4o exceeds GPT-3.5 by 42.7 − 6.1 = 36.6 percentage points, and Llama3 by 42.7 − 17.9 = 24.8 percentage points. On MiniWoB the GPT-4o/Llama3 gap is 66.1 − 62.6 = 3.5 points. These operands support the authors' observation that the model gap is larger on WorkArena; they do not identify why it is larger.

### 9.2 Task-category differences

The most important category finding is **0.0% list-filter success for every evaluated agent**. The knowledge category is comparatively strong for GPT-4o at 80.0% ± 12.2, while the service catalog category reaches 77.8% ± 3.2. Vision augmentation improves dashboards from 62.5% to 72.5% and menus from 60.0% to 90.0%, but reduces forms, knowledge retrieval, and service catalogs. The aggregate vision result therefore conceals mixed category behavior. [p. 7, Table 2]

[C; HIGH] GPT-4o-V minus GPT-4o is −0.9 percentage points on WorkArena, +1.6 on MiniWoB, and +0.5 on WebArena. These are observed differences in reported point estimates, not demonstrated statistically significant effects.

### 9.3 Ablation findings

Removing thinking lowers GPT-3.5 from 41.3 to 30.2 on MiniWoB and from 8.5 to 6.1 on WorkArena; Llama3 falls from 59.8 to 48.6 and from 20.0 to 8.5. Adding thought history lowers GPT-4o from 68.2 to 66.7 and from 45.5 to 42.4; GPT-3.5 falls from 41.3 to 36.2 and from 8.5 to 3.0. In contrast, removing Llama3's existing thought history lowers its MiniWoB score from 59.8 to 52.2 and WorkArena from 20.0 to 18.8. Thus the claim that memory can hurt is conditional, not a universal recommendation to remove history. [p. 8, Tables 3–5]

GPT-4o's combined bounding-box and coordinate-action addition raises MiniWoB from 68.2 to 72.6, but lowers WorkArena from 45.5 to 41.2. [C; HIGH] The changes are +4.4 and −4.3 percentage points. The setup jointly changes observation information and available actions. [p. 8, Table 3]

### 9.4 Consistency checks and unresolved issues

1. **25.4% versus 23.5% WebArena:** p. 2's contribution paragraph claims a GPT-4 score of 25.4%; p. 7 Table 2 and p. 8 report GPT-4o at 23.5%. The supplied text does not explain whether this is a different model, experiment, or stale statement. Both are preserved; final evaluation discussion uses Table 2.
2. **190 versus 812 WebArena tasks:** §2 on p. 2 describes 190 tasks, while Table 2 reports 812 and category totals 411 + 325 + 76 = 812. The supplied document does not explain the change in task inventory.
3. **List tasks wording:** p. 8 describes list-based tasks as having 0% success, but Table 2 distinguishes filtering at 0.0% from sorting with nonzero results. The zero-success finding is therefore represented specifically as list filtering.
4. **Thinking evidence:** p. 8 says removing chain-of-thought is clearly detrimental for all three models. Displayed Table 3 contains no GPT-4o '-use thinking' row. The visible numerical support directly establishes the effect for GPT-3.5 and Llama3; the GPT-4o extension remains an author assertion without a displayed matching row.
5. **Description/example explanation:** prose groups long descriptions and individual examples as potentially harmful for weaker models. Table 4 shows removing individual examples worsens GPT-3.5's MiniWoB score, while Table 5 does not report an individual-example ablation. The broad wording is not a consistent result for every feature/model.
6. **Different baselines:** Table 2 and Tables 3–5 have different scores; footnote 8 explicitly attributes this to a different seed. These conditions are not silently pooled.
7. **Zero success with nonzero standard error:** Table 2 reports nonzero SE alongside several 0.0% rates. The bootstrap description does not fully explain how these particular pairs arise. They are transcribed as reported without inventing a correction.
8. **Oracle action counts and episode steps:** Table 6 reports Playwright oracle actions; §5.2 uses them to motivate the 15-step caveat. They are not necessarily equal to agent steps or minimal required action counts.

## 10. Figure-by-figure interpretation

### Figure 1 — Contributions and browser-agent interaction [p. 2]

[B; HIGH] Panel a is a montage of ServiceNow interfaces labeled Workspace, List, Form, Dashboard, Knowledge Base, and Service Catalog. It establishes task diversity, not quantitative performance. Panel b places a browser and web agent in an observation/action loop, with a separate chat interaction. Observations are depicted as HTML, AXTree, and screenshot; action examples include Python/Playwright, coordinate-based clicks, and bid-based clicks. The arrows indicate browser information flowing to the agent and actions returning to the browser. The caption reports 33 tasks and 19,912 instances. There are no experimental axes or error bars. Small screenshot contents are illustrative and are not exhaustively transcribed.

### Figure 2 — Example goal for each category [p. 3]

[B; HIGH] Six colored boxes show natural-language requests for lists, forms, knowledge bases, service catalogs, dashboards, and menus. Examples include filtering for high priority, creating John Smith, ordering an iPad with specified color/storage, reading a manufacturer's chart percentage, and navigating a named module. Colors separate categories and do not encode scores. The knowledge example asks about room A-651; Appendix A.3 later uses A-561 as a different example. The figure demonstrates explicit goal wording and parameterized templates. It is not evidence that agents completed these goals.

### Figure 3 — A complex form [p. 4]

[B; HIGH] A chat goal requests a hardware asset with model category Computer, model Lenovo ThinkStation S20, vendor Lenovo, installation date 2024-01-01, and serial SN-456-789. The main form and enlarged details show three interaction problems: auto-completion, tabs hiding fields, and a date picker. Red numbered callouts connect these problems to interface regions. The screenshot directly illustrates complexity while the caption supplies the interpretation. No timing or success measurement is shown.

### Figure 4 — Observation-size distributions [p. 9]

[B; MEDIUM] This is a violin-style distribution plot comparing pruned HTML on the left with AXTree on the right. Blue denotes MiniWoB, orange WorkArena, and green WebArena. The vertical axis represents token count and uses a logarithmic scale, with powers-of-ten tick labels. WorkArena and WebArena page representations occupy higher ranges than MiniWoB; AXTree distributions are generally lower than the corresponding HTML distributions. Distribution marks appear within the violins, but their exact statistical definitions are not explained in the supplied caption. Exact medians, quantiles, sample counts, and extrema are not provided in readable numerical form, so none are estimated as exact values here. The visual supports the context-size concern; p. 5 separately reports a 40k–500k HTML-token range for ServiceNow pages.

### Figure 5 — Building an incident filter [p. 14]

[B; HIGH] The top view contains the incident list and the instruction to filter Priority = '1 - Critical' and Category = 'Hardware'. A lower view displays the condition-building UI and filtered results. Callouts show opening the filter menu, adding/filling conditions, and pressing Run. This is a multi-stage interaction, not a simple text search. Its relationship to Table 2 is important: the list-filter category fails for all agents despite explicit goals. It does not establish which individual widget behavior causes failure.

### Figure 6 — Knowledge-base search and answer [p. 15]

[B; HIGH] The composite shows an initial chat request for the CEO's full phone number, the knowledge-base landing page, search results, an article, and a returned answer. Callouts identify search, browsing results, reading the article, and replying in chat. The displayed example answer is +1 (555) 101-2020. It is an illustrative task answer, not a performance statistic or externally verified contact. Fine article prose is not independently transcribed. The figure shows information moving from page content into a user-facing answer.

### Figure 7 — Catalog configuration and order submission [p. 16]

[B; HIGH] Three interface states show the catalog, the product listing, and the selected Developer Laptop (Mac). The goal asks for five units, Adobe Acrobat enabled, Eclipse IDE disabled, Adobe Photoshop enabled, and additional software Zoom. Callouts trace item navigation, configuration, quantity, and Order Now submission. The figure demonstrates that success includes state-changing order creation. No actual financial amount or transaction security result is inferred.

### Figure 8 — Reading a dashboard percentage [p. 16]

[B; HIGH] The dashboard has a pie chart and a horizontal manufacturer bar chart. The task selects Hewlett-Packard in 'Configuration Item by Manufacturer' and asks for a percentage. A highlighted tooltip and chat answer provide the exact example value 4.72%. Other tiny chart labels are not needed for the demonstrated task and are compressed. This is a retrieval illustration, not a benchmark score; the agent must locate the right chart, label, unit, and response format.

### Figure 9 — Disambiguating a menu destination [p. 17]

[B; HIGH] The composite shows the All menu, an 'Open' search, and multiple candidate modules. The instruction is to navigate to the Open module under Problem. Callouts identify opening the menu, searching or alternatively scrolling, and selecting the correct application/module. Repeated 'Open' labels show why literal label matching alone may be inadequate. This illustrates semantic disambiguation without reporting failure frequencies.

### Figure 10 — Generated factual article [p. 18]

[B; HIGH] An HTML article titled 'Enhancing Your Conference Room Experience' embeds the highlighted fact that room A-561's password is roo918k. Surrounding prose describes room access, features, booking, and etiquette. The purpose is to demonstrate a factual answer embedded in a larger article. The password is synthetic benchmark content, not evidence of a real credential leak. The visual aligns with Table 7 and §A.3; not every surrounding sentence is reproduced.

### Figure 11 — A geometric MiniWoB task [p. 21]

[B; HIGH] A chat instruction asks the agent to draw a line bisecting an angle and submit it. The browser panel shows two rays, points, a drawing area, and a Submit button. It illustrates why some toy tasks require spatial coordinates even though many enterprise tasks can use identifiers. The figure does not provide an angle measurement, geometric accuracy score, or success result. No numerical angle is inferred.

## 11. Table-by-table interpretation

### Table 1 — Selected feature configurations [p. 6]

[A/B; HIGH] Rows are agent, observation, and action-space flags; columns are GPT-4o, GPT-3.5, and Llama3. Checkmarks mean enabled and crosses disabled. All three enable thinking, action history, visibility extraction, and individual action examples. All disable error history, coordinates, visible-only filtering, and multiple actions per step; all use bid actions. Only Llama3 enables thought history and focused-element information. GPT-4o and GPT-3.5 enable last-error information; Llama3 does not. Only GPT-4o enables clickability extraction and long action descriptions. These are selected configurations following random search, not universal recommendations or an exhaustive factorial design.

### Table 2 — Main success results [p. 7]

[A/B; HIGH] All values below are SR% ± SE. The table reports uncertainty, but no significance stars, p-values, or confidence intervals. Benchmark aggregates are distinguished from subsets.

| Task/category | GPT-4o | GPT-4o-V | GPT-3.5 | Llama3 |
|---|---:|---:|---:|---:|
| Dashboard, 4 | 62.5 ± 6.8 | 72.5 ± 6.0 | 20.0 ± 4.8 | 37.5 ± 6.0 |
| Form, 5 | 40.0 ± 5.9 | 34.0 ± 4.8 | 2.0 ± 2.5 | 32.0 ± 4.6 |
| Knowledge, 1 | 80.0 ± 12.2 | 70.0 ± 13.9 | 0.0 ± 4.3 | 30.0 ± 12.3 |
| List-filter, 6 | 0.0 ± 1.6 | 0.0 ± 1.7 | 0.0 ± 1.6 | 0.0 ± 1.8 |
| List-sort, 6 | 10.0 ± 3.8 | 13.3 ± 4.0 | 8.3 ± 3.7 | 1.7 ± 2.5 |
| Menu, 2 | 60.0 ± 8.0 | 90.0 ± 6.0 | 5.0 ± 4.7 | 0.0 ± 2.9 |
| Service catalog, 9 | 77.8 ± 3.2 | 65.6 ± 3.6 | 5.6 ± 2.3 | 26.7 ± 3.4 |
| WebArena content-and-config, 411 | 25.8 ± 1.0 | 26.8 ± 0.9 | 8.8 ± 0.8 | 12.7 ± 0.9 |
| WebArena information-seeking, 325 | 22.5 ± 1.0 | 22.5 ± 0.9 | 4.3 ± 0.9 | 9.8 ± 1.1 |
| WebArena navigation, 76 | 15.8 ± 2.2 | 15.8 ± 1.8 | 5.3 ± 1.9 | 6.6 ± 1.9 |

Aggregate and WebGum subset values are reproduced in §9. The vision agent is best on dashboards and menus, ties the base GPT-4o on the displayed WebArena information-seeking and navigation point estimates, and performs worse on several WorkArena categories. List-filter has a four-way zero tie. Knowledge uncertainty is large because this category contains one task type and only ten task seeds under the stated protocol. That explanation of limited sampling is [D], while the uncertainty numbers themselves are reported.

### Table 3 — GPT-4o ablations [p. 8]

[A/B; HIGH] Each row modifies the initial configuration. Values are MiniWoB/WorkArena SR% ± SE, not changes from the baseline.

| Configuration | MiniWoB | WorkArena |
|---|---:|---:|
| Initial | 68.2 ± 1.0 | 45.5 ± 2.2 |
| +multi actions | 68.5 ± 1.0 | 40.6 ± 2.0 |
| +coords=box, action_set=bid+coord | 72.6 ± 1.0 | 41.2 ± 1.8 |
| +use think history | 66.7 ± 0.9 | 42.4 ± 2.3 |
| +use error history | 67.2 ± 0.9 | 43.6 ± 2.1 |
| -extract visible tag | 68.8 ± 1.0 | 43.0 ± 2.2 |

The coordinate condition is the highest displayed MiniWoB result; the initial configuration is highest on WorkArena. No row removes thinking. Multiple actions help the MiniWoB point estimate only slightly and lower WorkArena. These observations do not prove that more allowed actions necessarily harm every agent or task.

### Table 4 — GPT-3.5 ablations [p. 8]

| Configuration | MiniWoB SR% ± SE | WorkArena SR% ± SE |
|---|---:|---:|
| Initial | 41.3 ± 1.1 | 8.5 ± 1.3 |
| -use thinking | 30.2 ± 1.0 | 6.1 ± 1.2 |
| -use action history | 34.1 ± 1.1 | 5.2 ± 1.3 |
| +use think history | 36.2 ± 1.2 | 3.0 ± 1.0 |
| +use error history | 37.9 ± 1.0 | 7.0 ± 1.4 |
| +multi actions | 41.4 ± 1.1 | 9.4 ± 1.5 |
| +only visible elements | 38.1 ± 1.0 | 5.8 ± 1.3 |
| +long description | 39.5 ± 1.0 | 6.4 ± 1.2 |
| -individual examples | 34.4 ± 1.0 | 8.2 ± 1.3 |
| +coords=center, action_set=bid+coord | 40.8 ± 1.1 | 4.5 ± 1.1 |
| +coords=box, action_set=bid+coord | 40.5 ± 1.2 | 6.1 ± 1.4 |
| +use focused element | 40.3 ± 1.1 | 9.4 ± 1.5 |
| -extract visible tag | 37.8 ± 1.0 | 6.7 ± 1.3 |
| +extract clickable tag | 37.9 ± 1.1 | 7.6 ± 1.2 |

[A/B; HIGH] The highest displayed WorkArena point estimate is a tie at 9.4 for multiple actions and focused-element information; thought history gives the lowest at 3.0. MiniWoB's highest displayed point estimate is 41.4 with multiple actions, barely above 41.3 initial. Large effects from removing thinking or action history are more persuasive than ranking small differences without hypothesis tests. The example-removal row demonstrates that individual action examples can help GPT-3.5, qualifying the prose's broad 'more is not always better' discussion.

### Table 5 — Llama3 ablations [p. 8]

| Configuration | MiniWoB SR% ± SE | WorkArena SR% ± SE |
|---|---:|---:|
| Initial | 59.8 ± 1.0 | 20.0 ± 2.3 |
| -use thinking | 48.6 ± 1.1 | 8.5 ± 1.7 |
| -use action history | 49.9 ± 1.1 | 8.5 ± 1.7 |
| -use think history | 52.2 ± 1.1 | 18.8 ± 2.1 |
| +multi actions | 63.0 ± 1.0 | 17.6 ± 2.1 |
| +long description | 55.5 ± 1.0 | 17.6 ± 2.0 |
| +use last error | 60.2 ± 1.1 | 19.4 ± 1.8 |
| -extract visible tag | 61.3 ± 0.9 | 15.8 ± 2.0 |

[A/B; HIGH] Multiple actions produce the highest displayed MiniWoB score; the initial configuration leads WorkArena. Removing thinking and action history ties at the lowest WorkArena score, 8.5. [C; HIGH] Thinking removal changes MiniWoB by 48.6 − 59.8 = −11.2 percentage points and WorkArena by 8.5 − 20.0 = −11.5 points. The prose's '10 points' is an approximate characterization, not the exact table difference. Table 5 shows that retaining thought history helps this Llama3 configuration, unlike the GPT additions.

### Table 6 — All tasks and oracle complexity [p. 13]

[A/B; HIGH] Instances are parameter combinations, not measured episodes. Oracle Actions are mean Playwright action counts ± standard deviation over ten randomly sampled instances. Their uncertainty is SD, unlike Tables 2–5's SE. Human-coded oracles may be nonoptimal.

| Task | Instances | Oracle actions, mean ± SD |
|---|---:|---:|
| FilterAssetList | 1,000 | 17.3 ± 6.5 |
| FilterChangeRequestList | 1,000 | 18.7 ± 4.7 |
| FilterHardwareList | 1,000 | 18.4 ± 5.6 |
| FilterIncidentList | 1,000 | 16.2 ± 4.2 |
| FilterServiceCatalogItemList | 1,000 | 19.9 ± 5.9 |
| FilterUserList | 1,000 | 12.7 ± 3.2 |
| SortAssetList | 150 | 7.4 ± 2.3 |
| SortChangeRequestList | 150 | 7.7 ± 1.6 |
| SortHardwareList | 150 | 8 ± 2.3 |
| SortIncidentList | 150 | 8 ± 2.7 |
| SortServiceCatalogItemList | 150 | 8.3 ± 2.5 |
| SortUserList | 150 | 7.7 ± 2.1 |
| CreateChangeRequest | 1,000 | 21.5 ± 6.2 |
| CreateIncident | 1,000 | 23 ± 7.9 |
| CreateHardwareAsset | 1,000 | 47.1 ± 10.9 |
| CreateProblem | 1,000 | 10 ± 3.4 |
| CreateUser | 1,000 | 17.9 ± 5.2 |
| KnowledgeBaseSearch | 1,000 | 4.0 ± 0.0 |
| OrderDeveloperLaptopMac | 1,000 | 8.7 ± 0.9 |
| OrderIpadMini | 80 | 6.0 ± 0.0 |
| OrderIpadPro | 60 | 6.0 ± 0.0 |
| OrderSalesLaptop | 1,000 | 9.0 ± 0.8 |
| OrderStandardLaptop | 1,000 | 8.0 ± 0.6 |
| OrderAppleWatch | 10 | 4.0 ± 0.0 |
| OrderAppleMacBookPro15 | 10 | 4.0 ± 0.0 |
| OrderDevelopmentLaptopPC | 40 | 6.0 ± 0.0 |
| OrderLoanerLaptop | 350 | 8.0 ± 0.0 |
| AllMenu | 1,000 | 3.0 ± 0.0 |
| Impersonation | 600 | 7.0 ± 0.0 |
| SingleChartValueRetrieval | 1,000 | 1.0 ± 0.0 |
| SingleChartMinMaxRetrieval | 346 | 1.0 ± 0.0 |
| MultiChartValueRetrieval | 444 | 2.0 ± 0.0 |
| MultiChartMinMaxRetrieval | 72 | 2.0 ± 0.0 |
| Total | 19,912 | Not supplied |

CreateHardwareAsset has the largest reported mean oracle action count, 47.1; single-chart retrieval has the smallest, 1.0. Several form and filtering means exceed the 15-step agent budget. This motivates a confounding concern but is not proof that no shorter solution exists.

### Table 7 — Example knowledge facts [p. 18]

[A/B; HIGH] Three rows pair a factual description with an answer: room A-561 password → roo918k; office #456 address → 42, Pizza street, New York, USA; CEO name → Alex Johnson. The column names Fact and Item differ from nearby item/value terminology. These are synthetic examples showing benchmark content, not verified facts about an actual company.

### Table 8 — Question wording and format constraints [p. 19]

[A/B; HIGH] Four sample questions ask for office #456's address, with instructions to include number, street, city, and country. They illustrate variation in language while preserving the requested fact and answer structure. The examples are compressed because the rows repeat the same informational target. They are not a quantitative diversity assessment.

### Table 9 — Alternative accepted answers [p. 19]

[A/B; HIGH] Four sample formats include '42 Pizza Street, New York, USA', abbreviations such as 'Pizza St.' and 'NY', '#42', and 'United States of America'. The table demonstrates tolerance to surface formatting and wording. It does not show an algorithm for recognizing every correct paraphrase or a false-positive/false-negative validation study.

### Table 10 — BrowserGym action space [p. 20]

[A/B; HIGH] The categories are bid, coord, tab, nav, misc, and python. Bid actions include fill, click, double-click, hover, press, focus, clear, select options, and element-to-element drag/drop. Coordinate actions include mouse movement, mouse-button down/up, click/double-click, coordinate drag/drop, keyboard down/up/press/type/insert. Tab actions open, close, and focus tabs. Navigation actions go back, forward, or to a URL. Miscellaneous actions scroll, send a user message, and do nothing. The Python row permits arbitrary Python with Playwright, the active page, and a user-message primitive, explicitly labeled 'UNSAFE!'.

These are capability descriptions, not attack results. Exact function-name spacing in extracted text sometimes loses underscores; the visual confirms code-like primitive naming, but this report does not offer a runnable API reference. Table 1's evaluated bid-only agents should not be described as agents experimentally using unrestricted Python merely because the environment can support it.

## 12. Diagram / Architecture Interpretation

[A/B; HIGH] Figure 1b provides the main architecture. The browser contains the current external software state. BrowserGym exposes representations of that state to the web agent. The user supplies a goal through chat. The agent consumes selected observations and generates an action; the action execution changes the browser state, after which another observation can be produced. The chat also supports returning a retrieved answer.

The methodological text adds validation to this loop. Setup creates initial conditions; an action produces a new state or error; validate checks whether the goal is satisfied and may return reward, feedback, and a done flag; teardown cleans resources. An oracle is a separate hard-coded solution path used for feasibility and maintenance, not the LLM's decision procedure. [pp. 3, 5–6]

[D; MEDIUM] The security-relevant architectural sequence is external content → agent input → generated action → browser execution → enterprise state or outgoing message. It identifies points where integrity, authorization, or privacy questions could be investigated. The supplied study does not implement or test an attack against that sequence.

The remaining composite screenshots are procedural diagrams in a loose sense: numbered callouts show steps through forms, filtering, retrieval, ordering, and menus. Their sequence is explained in §10. They should not be mistaken for complete implementation flowcharts or proof that all allowable paths are safe.

## 13. Equations and mathematical concepts

There are no numbered equations, loss functions, optimization objectives, formal policy definitions, or proofs requiring transcription. This is primarily a benchmark and empirical systems paper.

[A; HIGH] The notation SR% ± SE means success rate expressed as a percentage, together with standard error. Table 6 instead uses oracle-action mean ± standard deviation. Standard error describes uncertainty in an estimated mean; standard deviation in Table 6 describes variation in action counts across sampled task instances. This distinction is necessary to interpret the supplied tables.

[C; HIGH] A percentage-point comparison subtracts reported percentages: 42.7% − 6.1% = 36.6 percentage points. A relative improvement would divide that difference by the baseline; this report does not substitute a relative percentage for the point difference. Derived comparisons in §§9 and 11 identify their operands.

[A; HIGH] The bootstrap procedure resamples to obtain 1,000 means; the reported standard error is the standard deviation of those bootstrap means. The paper does not give a formal bootstrap equation, exact stratification specification, or confidence-interval construction. No missing mathematical detail is filled with an assumed conventional formula.

The POMDP term expresses incomplete state visibility over time. The paper does not enumerate a formal state set, transition distribution, reward equation, or observation probability model. Its operational consequence here is that agents may need history or memory beyond the current page observation. [p. 5]

## 14. Interpretation and discussion

[A; HIGH] WorkArena supports the authors' capability conclusion: enterprise UI automation is far from solved under the tested protocol. Strong performance in one category does not imply broad reliability. GPT-4o's 77.8% catalog score coexists with 0.0% filter success, and its aggregate remains below half of evaluated episodes. [Table 2]

[D; MEDIUM] The study also shows why agent performance cannot be reduced to model identity. Observation representation, prompt truncation, action grounding, history, examples, and episode budget all shape the task. Because each model has a separately selected configuration and different prompt budget, Table 2 estimates performance of model-agent packages rather than a perfectly isolated model effect.

[A; MEDIUM] The authors attribute much of the difficulty to non-standard UI interaction and long contexts. Figure 4 and the 40k–500k HTML-token statement support the existence of context pressure. The data do not partition failures into exact percentages caused by truncation, widget incompatibility, reasoning error, parsing error, or step exhaustion.

[A; MEDIUM] The authors describe earlier erroneous decisions persisting when thought history is retained, reducing self-correction. This is a qualitative observation, supported by GPT ablation score decreases but without an error taxonomy or systematic trajectory count. Llama3's opposite pattern reinforces the need for conditional interpretation.

For the security research question, [D; MEDIUM] this paper contributes a concrete description of **expanded operational reach**. An agent can read enterprise pages, create records, submit orders, change the logged-in identity in an impersonation task, and send information through chat. These capabilities make errors or malicious redirection potentially consequential in ways not assessed by text-only output quality. The paper also explicitly notes transmission of sensitive information as a privacy concern. However, consequential capability is not itself evidence of exploitation or greater vulnerability.

The supplied paper does not compare standalone and browser-connected versions under the same attacks. It does not show malicious instructions inside pages, measure secret extraction, test unauthorized purchases, or evaluate defensive controls. Therefore the appropriate security conclusion is that WorkArena/BrowserGym helps characterize environments and interfaces for a future security analysis, while leaving the user's comparative hypothesis unresolved.

## 15. Contributions and novelty

| Contribution category | Paper contribution | Evidence and boundary |
|---|---|---|
| Benchmark | WorkArena's 33 enterprise task types and 19,912 instances | §§3, A.1; one platform, not all workplaces |
| Dataset/content | Parameterized goals and generated knowledge articles/questions/answers | §3.1, §A.3; synthetic knowledge content |
| System | BrowserGym observation/action/chat environment | §4; capability availability differs from evaluation use |
| Methodological | Unified agent feature flags, common codebase, validation and oracle support | §§4–5; not a formal causal isolation of every feature |
| Implementation | Chromium/CDP/Playwright environment and open-source repository links | pp. 5–6; code not reviewed here |
| Empirical | Model comparisons, category results, feature ablations, vision condition | Tables 1–5; bounded task/seed/step protocol |
| Conceptual | Enterprise UI complexity as a capability-testing domain | §§1–3, 6; author positioning |
| Security research relevance | Observation/action/data/identity pathways usable for security questions | Analyst interpretation; no security experiment contribution |

The paper does not supply a new theorem, mathematical learning objective, trained foundation model, demonstrated attack, or experimentally validated defense. Its major novelty claims concern benchmark coverage and evaluation infrastructure rather than a new security mechanism.

## 16. Limitations

### Authors' stated limitations and qualifications

[A; HIGH] Some WorkArena tasks may need more than 15 steps unless multi-action mode is used. HTML is too large for the selected WorkArena/WebArena agents, motivating AXTree-only observations. Prompts are truncated from the end when too long. BrowserGym provides no memory mechanism. Oracle solutions may be correct without being optimal. These qualifications materially constrain interpretation. [pp. 5–7, 13]

[A; HIGH] Screenshot augmentation produces limited gains in the tested configuration. The authors describe memory persistence and extra prompt content as potentially harmful. They report a considerable gap to full automation and propose harder compositional workflows as future work. [pp. 8–9]

[A; HIGH] The impact statement acknowledges labor disruption, potential elaborate cyberattacks from human-like agents, privacy concerns from sensitive-information transmission, and inference energy consumption. It suggests constrained language models as a security measure but provides no operational definition or defense evaluation. These are prospective impacts, not quantified experimental limitations. [p. 10; text-only inspection]

### Additional evidence-based analyst observations

[D; MEDIUM] Model capability, configuration, context budget, and access modality vary together. Configuration selection uses the same benchmark families later evaluated, with different seeds rather than a clearly described held-out task split. Ten seeds per task limit category-level precision, particularly the one-task knowledge category. The step cap can interact with task length. The absence of raw trajectories prevents independent failure attribution.

[D; MEDIUM] Knowledge articles and answer formats are generated by models, and question quality is checked using another model. This establishes a useful controlled dataset but may not represent the diversity and ambiguity of real corporate documentation. Validators use different success constructs across categories, and no validator accuracy study is supplied.

[D; HIGH] For security purposes, the strongest limitation is construct mismatch: task completion measures capability, not adversarial robustness, authorization correctness, confidentiality, or vulnerability relative to standalone LLMs. There is no security control comparison, attacker workload, or standalone baseline.

## 17. Threats to validity

The following validity categories are analyst labels, not headings used by the authors.

**Internal validity [D; MEDIUM]:** Model-specific tuning and unequal prompt limits complicate attribution of score differences exclusively to the underlying LLM. The coordinate ablations jointly change information and action availability. The 15-step limit can interact with task length. Different ablation seeds explain baseline changes but reduce direct comparability with final scores.

**Construct validity [D; HIGH]:** Success is defined by benchmark validators, which differ across categories. A task may be counted correct by its state or answer without measuring user satisfaction, privacy, permission compliance, or safe intermediate behavior. Conversely, inability to finish within the budget need not mean the model cannot understand the task. Security vulnerability is not the construct being measured.

**External validity [D; MEDIUM]:** WorkArena concentrates on ServiceNow developer instances and particular software versions. The results do not establish behavior on every enterprise product, production deployment, organization, or contemporary model. The authors' 2024 claims of state-of-the-art performance are historical claims within the supplied paper, not current leaderboard assertions.

**Ecological validity [D; MEDIUM]:** Real cloud interfaces provide more realistic widgets than toy pages, but goals are intentionally explicit and many evaluated tasks are individual interactions rather than longer workplace workflows. Synthetic articles and known answer sets simplify some information-retrieval conditions. No study of actual employees, accessibility users, or organizational deployment outcomes is reported.

**Statistical conclusion validity [D; MEDIUM]:** Standard errors provide uncertainty information, but no significance tests are supplied. Small point-estimate changes should not be treated as established effects. Some reported zero-success/nonzero-SE pairs are insufficiently explained. Search breadth, exact seeds, and bootstrap implementation details are unavailable.

**Reproducibility [D; MEDIUM]:** Version numbers, model identifiers, configurations, episode limits, and repository links are helpful. This inspection has not reviewed code, exact prompts, raw runs, search records, or service state. Publicly linked artifacts are referenced evidence, not inspected supplements. ServiceNow evolution is explicitly anticipated by the oracle-maintenance rationale.

## 18. Future work and open questions

### A. Authors' proposed future work

[A; HIGH] Integrate additional benchmarks into BrowserGym, specifically WebShop and WebVoyager. Expand WorkArena with compositional tasks joining existing interactions into complex workflows requiring retrieval, memorization, visual perception, and advanced reasoning. Improve multimodal agents' use of screenshots and continue studying emerging capabilities through browser-based tasks. [p. 9]

The text's compatibility/support language is not entirely uniform: p. 2 names WebShop among compatible benchmarks, while pp. 6 and 9 list current supported benchmarks as MiniWoB, WebArena, and WorkArena and propose adding WebShop later. The safe reading is that current integrated support explicitly established in the implementation discussion is the latter three; WebShop's precise integration status remains unclear from the supplied account.

### B. Additional open questions

[D; MEDIUM] Would more steps, different truncation, or alternative grounding remove the list-filter bottleneck? Which failures originate in omitted observations versus reasoning or execution? How much do synthetic articles differ from actual enterprise retrieval demands? How accurate are validators under unusual but correct answers? Does thought history help once workflows genuinely require cross-page memory?

For security, unresolved questions include: what content can an attacker control; which actions require authorization; whether page-derived text can improperly influence execution; whether retrieval output can expose sensitive information; how impersonation is permission-limited; and whether restricted primitives change attack outcomes compared with arbitrary code. These are research questions suggested by the architecture, not attacks or vulnerabilities demonstrated by this paper.

A direct answer to the user's comparative question would require a study that actually compares specified standalone and web-agent systems under defined threats. No such comparison is supplied, so its outcome remains UNKNOWN here.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| LLM | Large language model used to reason and generate actions |
| Web agent | Model-driven system acting through a browser |
| UI | User interface: software controls and information presented to a user |
| API | Application programming interface for programmatic access |
| WorkArena | Enterprise-task benchmark built on ServiceNow |
| BrowserGym | Browser interaction and evaluation environment |
| AgentLab | Linked code artifact for the experimental agents; not inspected |
| DOM | Document Object Model, the structural representation of a page |
| HTML | Page markup whose textual representation can become very large |
| AXTree | Accessibility tree, a structured page observation |
| bid | BrowserGym's unique identifier for an element |
| Bounding box | Left/top/right/bottom coordinates locating an element |
| coord | Coordinate-based observations or actions using screen positions |
| CDP | Chrome DevTools Protocol, used to obtain browser information and control |
| Playwright | Browser automation library used by the environment and oracles |
| POMDP | Partially-Observable Markov Decision Process; current observations do not fully represent all relevant state |
| iFrame | Embedded frame; the paper notes nesting as an interaction challenge |
| Shadow DOM | Encapsulated page structure supported by BrowserGym |
| Oracle / cheat() | Hand-coded task solution, not necessarily optimal |
| validate() | Task outcome check returning reward, feedback, and completion flag |
| setup() / teardown() | Initialize task state / clean resources |
| Episode | One task attempt consisting of successive agent steps |
| Seed | Randomization setting used for task/evaluation variation |
| Zero-shot | No task-specific worked examples; generic format/action examples may remain |
| Chain-of-thought | Author's prompting method requesting reasoning before an action |
| Thought history | Earlier reasoning outputs reinserted into the current prompt |
| Set-of-Mark | Screenshot augmentation used for GPT-4o-V; detailed construction not supplied |
| SR | Success rate |
| SE | Standard error of the estimated mean success rate |
| SD | Standard deviation; used for sampled oracle action counts |
| Stratified bootstrap | Resampling procedure used to estimate benchmark mean uncertainty; strata not fully specified |
| Token | Unit of model input length used in context and truncation budgets |
| TGI | Text Generation Inference library used to serve Llama3 |
| Impersonation | Task that logs in as a specified user for support-style diagnosis |

## 20. Key numerical results

The detailed table ledgers above retain all displayed main and ablation scores. This compact reference selects the values most important for interpreting methods and findings.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| WorkArena task inventory | 33 | task types | Six categories | Author-reported | pp. 2–3, T6 p. 13 |
| WorkArena available instances | 19,912 | instances | Parameterized inventory, not evaluated episodes | Author-reported | T6 p. 13 |
| GPT-4o WorkArena | 42.7 ± 1.5 | SR% ± SE | Final selected configuration | Author-reported | T2 p. 7 |
| GPT-4o-V WorkArena | 41.8 ± 1.7 | SR% ± SE | Added Set-of-Mark screenshot | Author-reported | T2 p. 7 |
| GPT-3.5 WorkArena | 6.1 ± 1.3 | SR% ± SE | Final selected configuration | Author-reported | T2 p. 7 |
| Llama3 WorkArena | 17.9 ± 1.5 | SR% ± SE | Final selected configuration | Author-reported | T2 p. 7 |
| List-filter success | 0.0 | SR% | All four agents; differing reported SEs | Author-reported | T2 p. 7 |
| GPT-4o MiniWoB | 66.1 ± 1.0 | SR% ± SE | Full 125-task benchmark | Author-reported | T2 p. 7 |
| GPT-4o WebGum subset | 82.9 ± 1.5 | SR% ± SE | 56 tasks, subset of MiniWoB | Author-reported | T2 p. 7 |
| GPT-4o WebArena | 23.5 ± 0.7 | SR% ± SE | Final 812-task evaluation | Author-reported | T2 p. 7 |
| Earlier contribution-paragraph score | 25.4 | % | GPT-4/WebArena; relation to T2 unexplained | Author-reported | p. 2 |
| Prior WebArena GPT-4 score | 14.4 | % | Authors' account of original study; not independently checked | Author-reported | pp. 2, 8 |
| ServiceNow cleaned HTML size | 40k–500k | tokens | Reported page-text range | Author-reported | p. 5 |
| Agent prompt caps | 40K / 15K / 8K | tokens | GPT-4o / GPT-3.5 / Llama3 | Author-reported | p. 7 |
| Seeds per task | 10 / 10 / 1 | seeds | WorkArena / MiniWoB / WebArena | Author-reported | p. 7 |
| Bootstrap means | 1,000 | samples | Stratified bootstrap | Author-reported | p. 7 |
| Episode limit | 15 | steps | All tasks; some WorkArena tasks may need more | Author-reported | p. 7 |
| Parser reprompts | Up to 4 | retries | Correct output parsing mistakes | Author-reported | p. 7 |
| Llama3 hardware | 4 | A100 GPUs | TGI deployment | Author-reported | p. 7 |
| Generated articles/facts | 100 / 100 | articles / facts | Knowledge-base construction | Author-reported | p. 18 |
| Alternative question wordings | 10 | per fact | GPT-4 generation and GPT-3.5 check | Author-reported | p. 18 |
| Alternative answer formats | 10 | requested formats | GPT-4 generation and inspection | Author-reported | p. 18 |
| Hardware-asset oracle actions | 47.1 ± 10.9 | mean actions ± SD | Ten sampled instances | Author-reported | T6 p. 13 |
| Dashboard example answer | 4.72 | % | Hewlett-Packard example, not benchmark score | Visually readable | F8 p. 16 |
| GPT-4o minus GPT-3.5 | 36.6 | percentage points | 42.7 − 6.1, WorkArena final evaluation | Analyst-derived | T2 p. 7 |
| GPT-4o minus Llama3 | 24.8 | percentage points | 42.7 − 17.9, WorkArena final evaluation | Analyst-derived | T2 p. 7 |
| Coordinate-condition MiniWoB change | +4.4 | percentage points | 72.6 − 68.2, GPT-4o ablation | Analyst-derived | T3 p. 8 |
| Coordinate-condition WorkArena change | −4.3 | percentage points | 41.2 − 45.5, GPT-4o ablation | Analyst-derived | T3 p. 8 |

No approximate visual estimate is used as an exact numerical result. Background reach figures—over 7,000 companies, 85% of Fortune 500, over 12 million individuals, and 500,000 daily help-center users—are author-cited motivational claims on pp. 1–2. They are not benchmark sample sizes or measured impacts of these agents.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| WorkArena covers diverse enterprise interactions | Six categories, 33 types, 19,912 instances | F1, F2, T6 | pp. 2–4, 13 | HIGH for supplied inventory; representativeness is author positioning |
| BrowserGym exposes rich observations and executable actions | DOM, AXTree, screenshots, identifiers, coordinates, primitives, optional Python | F1b, T10 | pp. 5–6, 20 | HIGH for described capability; code not reviewed |
| GPT-4o leads base-model final scores | 42.7/66.1/23.5 versus GPT-3.5 and Llama3 | T2, X1 | p. 7 | HIGH within the selected agent/model conditions |
| Enterprise task completion remains difficult | Aggregate below half and filter scores at zero | T2, X1 | pp. 7–8 | HIGH for scores; causes not quantitatively isolated |
| Screenshot augmentation has small aggregate gains elsewhere | MiniWoB 67.7 vs 66.1; WebArena 24.0 vs 23.5 | T2, X5 | pp. 7, 9 | HIGH point estimates; no significance test; WorkArena decreases |
| Thinking helps displayed weaker-model ablations | GPT-3.5 and Llama3 removal rows | T4–T5, X3–X4 | p. 8 | HIGH for these conditions; matching GPT-4o row absent |
| Coordinate support is task dependent | GPT-4o 72.6/41.2 versus 68.2/45.5 | T3, X2; F11 | pp. 8, 21 | HIGH for combined ablation; components not isolated |
| Thought history can hurt | GPT additions reduce scores; Llama removal also reduces scores | T3–T5 | pp. 8–9 | HIGH conditional pattern; persistence explanation qualitative |
| Step budget can constrain completion | 15-step cap and long oracle solutions | T6; §5.2 | pp. 7, 13 | HIGH stated caveat; oracles not minimal solutions |
| Privacy and cybersecurity warrant attention | Impact statement flags attacks and sensitive transmission | Impact Statement | p. 10 | HIGH as author concern; no quantified security evidence |
| Agent architecture is relevant to security boundaries | Read pages, execute actions, create orders/records, change user context | F1b, F7, T10; task descriptions | pp. 4–5, 16, 20 | MEDIUM analyst inference; does not prove greater vulnerability |
| Comparative standalone-LLM vulnerability remains unanswered | No such baseline, attack workload, or metric appears in the supplied study | Whole-document inventory | pp. 1–21 | HIGH negative finding about this document's scope |

Source-grounded checking preserved dataset/model conditions, exact main table values, SE versus SD, ablation seed differences, and author-versus-analyst attribution. Visuals were cross-checked with their captions and supplied extracted text. Conflicting claims remain explicitly unresolved rather than repaired.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to help with office software. Answering 'here is how you create a user' is easier than actually opening the right menu, finding the right form, entering all the fields, and making sure the new user really exists. This paper tests the second kind of work.

The researchers made WorkArena, a collection of office-style tasks, and BrowserGym, the environment that lets an AI see and control the browser. They tested several language models. The strongest main agent, GPT-4o, completed 42.7% of the WorkArena evaluation. Every tested agent failed the list-filter category, even though its goals were clearly written. Screenshots helped some task categories but did not improve the overall WorkArena score.

A major difficulty is that office web pages can be huge and complicated. Information may be hidden behind tabs, fields may depend on other fields, and several menu items can have the same name. Giving the AI more information or more memory did not always help. Sometimes the extra material made the task harder under the tested setup.

For your security question, the useful idea is that a browser AI can do more than talk: it can read information, create records, place orders, and interact with user identities. That makes its connections to software important to investigate. But this paper did not attack the agents or compare them with standalone chat models. It shows what these agents can attempt and where they struggle; it does not prove that web agents are more vulnerable.

## Completeness Audit

The denominator for this audit is the supplied inventory: 21 page texts, 19 page images, the main sections and substantive subsections listed in §2, Figures 1–11, Tables 1–10, six registered analyses, the major contributions, and author-stated caveats. 'Fully represented' means the substantive purpose, method, or finding is included; it does not mean every sentence or screenshot pixel is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract | Yes, text and image | Yes | Fully represented | Problem, benchmark, system, automation gap |
| S1 Introduction | Yes, text and images | Yes | Represented in compressed form | Motivation retained; reach figures separated from sample sizes |
| S2 Related Works: benchmarks | Yes, text and images | Yes | Represented in compressed form | Toy, shopping, realistic web, retrieval, mobile categories |
| S2 Related Works: LLM-based agents | Yes, text and image | Yes | Represented in compressed form | Text, multimodal, generated-code approaches |
| S3 WorkArena overview | Yes | Yes | Fully represented | Scope, daily-work trajectory, categories |
| SS3.1 goals, validators, oracles | Yes | Yes | Fully represented | Purpose and differences explained |
| SS3.1 Lists | Yes | Yes | Fully represented | Conditions, columns, counts, validation |
| SS3.1 Forms | Yes | Yes | Fully represented | Field range, dynamic UI, database checks |
| SS3.1 Knowledge bases | Yes | Yes | Fully represented | Retrieval, acceptable answers, appendix detail |
| SS3.1 Service catalogs | Yes | Yes | Fully represented | Configuration, quantities, database checks |
| SS3.1 Dashboards | Yes | Yes | Fully represented | Chart retrieval/reasoning and answer checks |
| SS3.1 Menus | Yes | Yes | Fully represented | Navigation and impersonation |
| SS3.2 UI, HTML, observation-size challenges | Yes | Yes | Fully represented | All three challenges and range retained |
| SS3.3 Availability | Yes | Yes | Represented in compressed form | Open source and developer instances; code not inspected |
| S4 BrowserGym/POMDP | Yes | Yes | Fully represented | Implementation and memory caveat |
| SS4.1 Chat | Yes | Yes | Fully represented | Goal input, replies, sequential-interaction capability |
| SS4.1 Augmented attributes | Yes | Yes | Fully represented | bid, bounding box, visible/clickable |
| SS4.1 Observation space | Yes | Yes | Fully represented | Page, chat, URLs, errors, modalities |
| SS4.1 Action space | Yes | Yes | Fully represented | Restricted primitives versus optional arbitrary code |
| SS4.1 Multi-page navigation | Yes | Yes | Fully represented | Tabs, popups, nested structures |
| SS4.2 Flexible agent design | Yes | Yes | Fully represented | Agent chooses representation/history/actions |
| SS4.2 Task lifecycle | Yes | Yes | Fully represented | setup, teardown, validate, cheat |
| SS4.2 Extensibility | Yes | Yes | Represented in compressed form | Support lists and WebShop ambiguity retained |
| S5 Experimental objectives | Yes | Yes | Fully represented | Two explicit objectives |
| SS5.1 Observation/action flags | Yes | Yes | Fully represented | Methods and Table 1 |
| SS5.1 Histories and examples | Yes | Yes | Fully represented | Distinct histories and zero-shot qualification |
| SS5.1 Parsing/models/truncation | Yes | Yes | Fully represented | Identifiers, hardware, caps, retries |
| SS5.2 Protocol | Yes | Yes | Fully represented | Seeds, bootstrap, steps, search, seed caveats |
| SS5.3 Results | Yes | Yes | Fully represented | All T2 values and major conclusions |
| SS5.4 Thinking/features/history | Yes | Yes | Fully represented | Tables and conditional interpretations |
| SS5.4 Vision and 2D actions | Yes | Yes | Fully represented | Aggregate/category effects and coupled ablation |
| S6 Conclusion | Yes | Yes | Represented in compressed form | Contributions and future plans |
| S7 Impact Statement | Yes, text only | Yes | Fully represented | Positive/negative impact categories and security limits |
| S8 References | Yes; p. 11 also image | Yes | Inspected but deliberately compressed as secondary | Bibliographic entries not individually annotated or externally verified |
| Title capability question | Yes | Yes | Fully represented | Distinguished from formal enumerated RQs |
| Explicit objectives | Yes | Yes | Fully represented | Difficulty comparison and feature impact |
| Formal hypotheses | Assessed | Yes | Not present | Explanatory hypotheses distinguished from formal tests |
| X1 Main benchmark comparison | Yes | Yes | Fully represented | Configurations and all final scores |
| X2 GPT-4o ablations | Yes | Yes | Fully represented | Every displayed row |
| X3 GPT-3.5 ablations | Yes | Yes | Fully represented | Every displayed row |
| X4 Llama3 ablations | Yes | Yes | Fully represented | Every displayed row |
| X5 Vision augmentation | Yes | Yes | Fully represented | Fixed-other-flags condition and caveats |
| X6 Observation-size comparison | Yes, visually | Yes | Represented in compressed form | Distribution pattern retained; exact statistics unavailable |
| Preliminary Llama2 observation | Yes | Yes | Represented in compressed form | Setup incomplete, evidentiary weight limited |
| F1a benchmark montage | Yes, visually | Yes | Represented in compressed form | Categories retained; tiny screenshot contents compressed |
| F1b architecture | Yes, visually | Yes | Fully represented | Observation/action/chat loop |
| F2 goals | Yes, visually | Yes | Represented in compressed form | Six categories and examples |
| F3 form | Yes, visually | Yes | Fully represented | Autocomplete, tabs, date-picker callouts |
| F4 distributions | Yes, visually | Yes | Uncertain for exact statistics | Log scale and trend retained; no invented medians |
| F5 filter | Yes, visually | Yes | Fully represented | Three-step procedure and conditions |
| F6 retrieval | Yes, visually | Yes | Fully represented | Search/read/reply flow and example answer |
| F7 catalog | Yes, visually | Yes | Fully represented | Configuration, quantity, order submission |
| F8 dashboard | Yes, visually | Yes | Fully represented | Exact 4.72% example; background chart details compressed |
| F9 menu | Yes, visually | Yes | Fully represented | Repeated-label disambiguation |
| F10 article | Yes, visually | Yes | Represented in compressed form | Highlighted fact retained; repetitive article prose compressed |
| F11 geometry | Yes, visually | Yes | Fully represented | Spatial task, no inferred angle |
| T1 configurations | Yes, text and image | Yes | Fully represented | All flags summarized without losing model differences |
| T2 final scores | Yes, text and image | Yes | Fully represented | All aggregate/category/subset rows retained |
| T3 GPT-4o ablations | Yes, text and image | Yes | Fully represented | All rows and uncertainties |
| T4 GPT-3.5 ablations | Yes, text and image | Yes | Fully represented | All rows and uncertainties |
| T5 Llama3 ablations | Yes, text and image | Yes | Fully represented | All rows and uncertainties |
| T6 task inventory | Yes, text and image | Yes | Fully represented | All 33 names/counts/action means and SDs |
| T7 fact examples | Yes, text and image | Yes | Fully represented | Three pairs and terminology ambiguity |
| T8 question examples | Yes, text and image | Yes | Represented in compressed form | Four variants grouped by shared target |
| T9 answer variants | Yes, text and image | Yes | Represented in compressed form | Formatting distinctions retained |
| T10 primitives | Yes, text and image | Yes | Represented in compressed form | Every action family and operation accounted for; no runnable API reconstruction |
| A1 task details | Yes | Yes | Fully represented | Instance cap and oracle-sampling caveat |
| A2 UI examples | Yes, visually | Yes | Fully represented | Figures 5–9 interpreted individually |
| A3 knowledge generation | Yes | Yes | Fully represented | Generation, checking, revisions, formats |
| B1 action-space details | Yes | Yes | Fully represented | Restricted/unsafe distinction |
| B2 MiniWoB port | Yes | Yes | Represented in compressed form | Goal moved from HTML to chat; hard time limit removed |
| Major equations/theorems | Assessed | Yes | Not present | Statistical notation discussed instead |
| Numbered algorithms/pseudocode | Assessed | Yes | Not present | Lifecycle and agent loop explained from prose |
| Major contributions | Yes | Yes | Fully represented | Benchmark, system, empirical study separated |
| Author-stated methodological caveats | Yes | Yes | Fully represented | Memory, truncation, steps, oracle optimality, vision |
| Author-stated impact concerns | Yes, text only | Yes | Fully represented | Labor, cybersecurity, privacy, energy |
| Supplied supplementary material | None supplied | Accounted for | Not present | No claim of supplementary review |
| Referenced repositories/raw outputs | No | Availability boundary represented | Not supplied as inspected evidence | WorkArena, BrowserGym, AgentLab, raw runs |

### Missing or inaccessible material

Rendered images for pages 10 and 12 are absent; their supplied text was inspected. Repository code, raw experimental records, exact prompts, configuration-search logs, and developer-instance state were not supplied as inspectable artifacts. No standalone supplementary document was provided. Figure 4 lacks readable exact distribution summary values. Some fine screenshot prose is too small for reliable full transcription, although task structure, captions, callouts, and central example values are visible.

### Uncertain interpretations

The relationship between the 25.4% contribution-paragraph WebArena result and the 23.5% final table result remains unresolved. The 190/812 WebArena task counts are unreconciled. Nonzero SE accompanying reported 0.0% success is insufficiently explained. GPT-4o thinking-removal evidence is asserted in prose but absent from Table 3. Knowledge-generation placeholders and Fact/Item labels are inconsistent. Current versus prospective WebShop integration is unclear. Exact Figure 4 statistics and some fine screenshot labels are unreadable. None of these uncertainties is repaired using external evidence.

### Deliberately compressed material

Related-work citations are grouped by their role rather than recounted paper by paper. For traceability, the authors describe MiniWoB's 125 tasks; WebShop shopping; WebArena's earlier 190-task description and 14% agent/78% human background results; Mind2Web, spelled 'Min2Web' in the supplied body, with 2,000 interactions and 137 websites; WebLINX with 2,337 demonstrations, 155 websites, and average 43 interactions; and WebVoyager's 300 retrieval tasks across 15 websites. These are author accounts of other studies, not results independently checked here. Mobile benchmark citations, author affiliations, correspondence details, repeated screenshot greetings, the full reference list, decorative UI chrome, and repetitive article prose are compressed. Tables 8–9 are summarized by their formatting function. The complete major experimental numerical tables and all 33 Table 6 task rows are retained.

Appendix B.2's port detail is also condensed: a minimal JavaScript snippet in setup extracts MiniWoB's goal from page HTML into separate chat, and the hard time limit per episode is removed. This change matters when interpreting cross-framework comparisons; the paper does not quantify its isolated effect.

### Potential omissions

No known major section, numbered substantive figure, numbered table, registered analysis, major contribution, or author-stated caveat from the supplied inventory is left unaccounted for. This is an inventory-bounded representation, not a claim to preserve every source fact or every fine visual detail. Exact plot distributions, unavailable implementation artifacts, unresolved textual conflicts, and compressed secondary examples remain explicit limitations. The paper's relevance to comparative security is represented as analyst inference, and the absence of a direct standalone-LLM vulnerability comparison is preserved.
