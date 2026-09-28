# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–56 |
| Apparently missing pages | None |
| Main text readability | Generally readable from complete page-labeled extraction |
| Visual inspection | Partial: 51 candidate visual pages were rendered; pages 9, 10, 12, 47, and 51 were not rendered, although their extracted text/captions are available |
| Figures | Figures 1–53 are represented by rendered pages, captions, or extracted descriptions. Figures on unrendered pages 47 and 51 were not directly inspected |
| Tables | Tables 1–3 are readable from extracted text; Tables 1–2 were also rendered. Table 3 was visible on rendered page 56 |
| Equations | No substantive mathematical equations are presented. Arithmetic task examples and pseudocode occur, but no numbered equation system |
| Algorithms | Algorithm 1 is readable on p. 37; its configuration dictionary is shown visually in Figure 33 |
| Appendices | Present, pp. 13–56: Appendices A–G |
| Supplementary material | No separate supplementary file was supplied |
| Referenced external artifacts | Benchmark codebase, GitHub Wiki, Personal Developer Instances, and external datasets/websites are referenced but were not supplied or inspected |
| OCR requirement | Needed particularly for image-dominant pp. 27–36, 38–44. Renderings make their broad content readable, but tiny interface text is sometimes uncertain |
| Important limitation | The prompt says the page-labeled paper text is complete, but several pages contain screenshot-only details absent from native extraction. Those screenshots were inspected where rendered, without treating tiny illegible text as exact evidence |

Source-status convention used below:

- **[A] Author-reported**: stated in the paper.
- **[B] Directly observable**: visible in a supplied rendering.
- **[C] Analyst-derived**: calculated directly from supplied values.
- **[D] Analyst interpretation**: a clearly identified inference.
- No external information is introduced.

# 1. Plain-Language Orientation

WorkArena++ is a benchmark for testing whether an artificial-intelligence agent can operate business software and complete realistic office workflows—not merely click a specified button or fill one explicitly described form.

The benchmark uses ServiceNow, an enterprise software platform containing lists, forms, dashboards, catalogs, tickets, and knowledge-base articles. An agent interacts with it through BrowserGym. The agent sees a goal and a representation of the current web page, chooses one browser action at a time, and receives a success signal only when the resulting page and database state satisfy an automated validator (pp. 3, 7, 18).

The problem is that existing web-agent benchmarks often emphasize comparatively atomic interactions. WorkArena++ instead asks agents to combine several operations and cognitive skills: planning, retrieving data, reasoning over it, remembering information across pages, and recognizing impossible requests (pp. 2, 4–6).

The authors created 341 workflows, each expressed at two difficulty levels:

- **L2** gives explicit procedural instructions.
- **L3** supplies a work ticket with task-specific facts but requires the agent to locate and remember a knowledge-base protocol.

This produces **682 tasks** in five skill categories (pp. 4–6).

The principal empirical finding is a large human–agent gap. On a matched 98-instance human curriculum, humans achieved **93.9% ± 3.4 percentage points**, while GPT-4o achieved **2.1% ± 2.0**. On the full 235-instance L3 agent curriculum, every evaluated model achieved **0%** (Table 2, p. 8).

The central contribution is therefore not a new agent algorithm. It is a reproducible, extensible benchmark and task-generation framework that exposes limitations hidden by simpler benchmarks while also producing oracle observation–action traces that could support future model training (pp. 2, 6, 45–46).

# 2. Document Roadmap

The paper is a mixed **benchmark, systems, and empirical evaluation paper** published in the NeurIPS 2024 Datasets and Benchmarks track (p. 1).

- **Abstract and §1, pp. 1–2:** problem, motivation, benchmark, and contributions.
- **§2, pp. 3–4:** BrowserGym and the original WorkArena.
- **§3, pp. 4–6:** WorkArena++ levels, skill taxonomy, isolation, visual diversity, task composition, and trace extraction.
- **§4, pp. 6–9:** evaluation curriculum, agent design, quantitative results, human study, and error analysis.
- **§5, p. 9:** related benchmarks and datasets.
- **§6, pp. 9–10:** conclusions and future work.
- **§7, p. 10:** limitations and societal impacts.
- **References, pp. 10–12.**
- **Appendix A, pp. 13–17:** human-evaluation details.
- **Appendix B, pp. 18–20:** agent prompt, observations, actions, and model setup.
- **Appendix C, pp. 21–36:** task families and L3 knowledge-base protocols.
- **Appendix D, pp. 37–38:** reproducible curriculum algorithm.
- **Appendix E, pp. 39–46:** interface themes, trace extraction, and compositional task construction.
- **Appendix F, pp. 47–54:** concrete error cases.
- **Appendix G, pp. 55–56:** ServiceNow scope, expansion directions, and a context-length ablation.

# 3. Background and Context

A **web agent** is a program that interprets a goal, observes a website, and takes actions such as clicking, typing, selecting options, or sending a message.

An **LLM** is a large language model. A **VLM** is a vision-language model that can also inspect screenshots.

**BrowserGym** standardizes the interaction loop. The agent receives chat instructions and multimodal observations, then issues an action from a fixed action vocabulary (Figure 2b; pp. 3, 18).

**WorkArena L1** is the predecessor benchmark. Its 33 task types focus on atomic enterprise-software interactions such as sorting a list or filling a form. Each task has:

- an **oracle**: human-written Playwright automation that completes it;
- a **validator**: code that checks the page and/or database and returns reward 0 or 1;
- setup and teardown mechanisms around a ServiceNow Personal Developer Instance (pp. 3–4).

An **accessibility tree (AXTree)** is a structured textual representation of page elements. BrowserGym assigns each interactable element a unique **bid** identifier. Elements inside an iframe combine the iframe identifier with an element number, such as `a324` (pp. 18, 47).

**Set-of-marks** overlays these identifiers on screenshots so a visual model can connect visible components to callable actions (Figures 9–10, pp. 19–20).

A **compositional task** chains atomic operations into a workflow. For example, onboarding requires creating a user, ordering a laptop, creating an asset, and assigning it to that user (pp. 4, 35, 45).

A **task seed** instantiates a template with reproducibly generated details. A separate **meta-seed** controls curriculum sampling (pp. 7, 37).

# 4. Research Problem and Gap

## Existing problem

Knowledge workers spend time navigating awkward software, retrieving information, coordinating schedules, and completing administrative workflows. Agents might automate such work, but success requires sustained reasoning and reliable interaction rather than isolated clicks (p. 1).

## Shortcomings of prior approaches, according to the authors

The original WorkArena remained predominantly atomic. MiniWoB used synthetic interfaces and toy interactions. WebArena offered realistic websites and complex instruction following but, in the authors’ comparison, did not target the same compositional enterprise skills (Table 1, p. 5; §5, p. 9).

## Research gap

The effectiveness of contemporary LLM/VLM agents at applying planning and reasoning autonomously in realistic enterprise workflows had not been adequately measured (abstract, p. 1).

## Motivation

A benchmark should reveal whether agents can:

1. organize multi-step work;
2. retrieve and combine information across pages;
3. reason under constraints;
4. remember task details;
5. avoid acting when requests are infeasible;
6. produce certifiably correct changes to an enterprise system.

## Scope

The benchmark is confined to ServiceNow and common web-interface primitives. It evaluates task completion, not safety, malicious robustness, or cross-software workflows (§7, p. 10; Appendix G.1, p. 55).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The prose explicitly poses two empirical questions after the primary agent results (p. 8):

- **RQ1:** Are WorkArena++ tasks actually solvable?
- **RQ2:** Why do contemporary agents fail?

Appendix G.1 poses two scope questions (p. 55):

- **RQ3:** Should insights from WorkArena++ generalize to other enterprise software?
- **RQ4:** Would including more software environments make the benchmark more representative?

## Objectives

- Construct realistic compositional enterprise workflows.
- distinguish explicit L2 instructions from implicit, ticket-and-knowledge-base L3 tasks.
- standardize evaluation while retaining large configuration diversity.
- evaluate closed- and open-source LLM/VLM agents.
- establish feasibility through human evaluation.
- diagnose failures through execution traces.
- enable task extension and oracle-trace extraction.

## Hypotheses

The paper does not state formal preregistered hypotheses. It anticipates that WorkArena++ will be difficult for current agents and comparatively straightforward for humans (§4, pp. 6–7), but this is presented as an expectation, not a formal hypothesis.

# 6. Assumptions / Threat Model

This is not a cybersecurity study, so no attacker threat model is defined.

The operational system assumptions are:

- A configured remote ServiceNow Personal Developer Instance is available (pp. 3–4).
- BrowserGym mediates observations and actions.
- Backend REST and frontend JavaScript APIs can set up, tear down, and validate tasks (Figure 3, p. 3).
- Oracle and validator implementations correctly encode intended solutions and success conditions.
- Each agent action is drawn from the provided high-level action space, one action per step (pp. 7, 18).
- AI episodes terminate after at most 50 steps; humans have no explicit action limit (pp. 7, 17).
- Task accounts are created and deleted per episode to isolate state (p. 6).
- Evaluation seeds 0–9 are reserved; tuning should use other seeds (p. 7).
- L2 and L3 share the same underlying workflows, but differ in instruction delivery (pp. 4–5).
- The authors treat oracle action count as a practical proxy for task length (Figure 4b).

A consequential evaluation assumption is that binary validation adequately represents successful workflow completion. The paper provides examples of database- and page-state checks but not a formal proof that every validator captures every intended semantic outcome.

# 7. Methodology

## 7.1 Benchmark construction

The authors compose WorkArena-style atomic setup, oracle, validation, and teardown functions into larger workflows. Sequential workflows may validate every constituent step; others may use global database validation (pp. 45–46).

The benchmark contains **341 workflows × 2 presentation levels = 682 tasks** (p. 4).

## 7.2 Difficulty levels

- **L2:** Complete steps are supplied through chat. Navigation mechanics may still be implicit.
- **L3:** A ticket provides task-specific details, while a knowledge-base article provides the general procedure. The agent must infer that the ticket is an assignment, retrieve the article, retain both sources, execute the workflow, and close the ticket (pp. 4–5).

## 7.3 Skill taxonomy

The main text reports (pp. 5–6):

- Planning/problem solving: **66 × 2**
- Information retrieval: **39 × 2**
- Data-driven decision-making/reasoning: **156 × 2**
- Sophisticated memorization: **28 × 2**
- Contextual understanding/infeasibility: **52 × 2**

These per-level values sum to 341. Appendix C instead labels memorization as **29 × 2** (pp. 13, 25), creating a documented inconsistency; see §14.

## 7.4 Curriculum sampling

The full task collection permits thousands of configurations. Algorithm 1 groups tasks into skill categories and within-category buckets representing similar abilities. For each category, it:

1. generates task seeds from a meta-seed;
2. initializes a random generator per seed;
3. samples a weighted number of tasks from every bucket without replacement;
4. records `(task, seed)` pairs.

The resulting agent curriculum contains **235 L2 + 235 L3 = 470 instances** (p. 37). Figure 4b also compares these with **33 L1 tasks × 5 seeds** for oracle lengths, whereas Table 2 reports L1 agent results over **33 × 10 seeds**.

## 7.5 Agent architecture

At each step the model receives:

- goal;
- current AXTree and, depending on benchmark, HTML;
- focused element;
- prior-action error;
- complete preceding thoughts/actions;
- for GPT-4o-v, a marked screenshot.

It emits a chain-of-thought section and one action (pp. 7, 18–19).

Available action families are:

- `chat`, including `send_msg_to_user`;
- `infeas`, including `report_infeasible(reason)`;
- bid-based browser operations such as click, fill, type, and option selection.

A parser may re-prompt up to four times after malformed output (pp. 7, 18).

## 7.6 Models, contexts, and implementation

| Agent | Reported model | Nominal model context in Appendix B | Maximum prompt used |
|---|---|---:|---:|
| GPT-3.5 | `gpt-3.5-turbo-1106` | 16K | 15K |
| GPT-4o / GPT-4o-v | `gpt-4o-2024-05-13` | 128K | 40K |
| Llama3 | `meta-llama-3-70B-instruct` | 8K | 8K |
| Mixtral | `open-mixtral-8x22b` | 64K | 32K |

Open models were served through Hugging Face Text Generation Inference on **4 A100 GPUs** (pp. 7, 18). When prompts exceeded limits, the HTML/AXTree was progressively truncated from the end. Prompts were tuned following the cited WorkArena methodology (p. 18).

## 7.7 Human study

Fifteen uncompensated volunteers attended an in-person session at ServiceNow’s Montreal office. They received:

- a 15-minute recorded introduction;
- 15 minutes of self-exploration;
- up to seven individually solved tasks;
- no discussion with other participants.

The curriculum contained **98 instances: 49 workflows × L2/L3**, sampled uniformly across skills (pp. 8, 14).

The interface matched BrowserGym but added a movable evaluation console with validation and give-up controls. Automatic validation checked completion continuously, but participants received only incomplete/solved status, not procedural feedback (p. 14).

The paper reports success rate and standard error. It does not report significance tests, confidence intervals, completion-time statistics, or per-participant task allocations.

# 8. Experiments / Analyses

## X1 — Main agent benchmark

**Purpose:** Measure contemporary agent success on L2/L3 and compare with established benchmarks.

**Sample:** 235 instances per WorkArena++ level; L1, MiniWoB, and WebArena comparison sets are listed in Table 2.

**Models:** GPT-3.5, GPT-4o, GPT-4o-v, Llama3-70B, Mixtral-8x22B.

**Metric:** Success rate (%) ± standard error.

**Result:** All models scored 0% on L3. Only GPT-4o and GPT-4o-v achieved nonzero L2 success, concentrated in memorization; GPT-4o-v also solved some information-retrieval tasks (Table 2, p. 8).

**Caveat:** The 50-step limit could terminate long unsuccessful trajectories, although the authors state oracle lengths show most curriculum tasks are solvable within that budget (p. 7; Figure 4b).

## X2 — Human feasibility study

**Purpose:** Address RQ1 and quantify the human–agent gap.

**Sample:** 15 people, 98 total curriculum instances; participants solved subsets.

**Comparison:** Humans versus GPT-4o on the same task subset.

**Result:** Humans achieved 93.9% ± 3.4 overall on both L2 and L3; GPT-4o achieved 2.1% ± 2.0 on L2 and 0% on L3 (Table 2; pp. 8, 14).

**[C] Derived matched-curriculum gap:**  
\(93.9 - 2.1 = 91.8\) percentage points on L2;  
\(93.9 - 0 = 93.9\) percentage points on L3.

**Caveats:** Small, nonrepresentative cohort; 11/15 had worked at ServiceNow; all held undergraduate degrees and half advanced degrees; participants had training, self-exploration, no action cap, and one general interface announcement (pp. 14–17).

## X3 — Qualitative execution-trace error analysis

**Purpose:** Address RQ2.

**Models examined:** Best-performing closed and open models, GPT-4o and Llama3 (p. 8).

**Method:** In-depth inspection of execution traces; no error frequencies or inter-rater procedures are reported.

**Categories:** information retrieval, exploration, hallucination, goal understanding, and action-consequence assessment (pp. 8–9, 47–54).

**Result:** Failures include malformed bids, misunderstanding current sort state, failure to expand hidden menus/tabs, invented actions/buttons, asking the user for help, thought/action disagreement, treating an L3 ticket as completed work, imagining progress, overwriting fields, and repeating ineffective actions.

## X4 — Context-size sensitivity

**Purpose:** Test Llama3 performance on WorkArena L1 under four context budgets.

**Conditions:** 130K, 64K, 32K, and 13K.

**Results:** 17.9 ± 2.1, 14.8 ± 2.0, 17.6 ± 2.1, and 18.2 ± 2.1%, respectively (Table 3, p. 56).

**Interpretation:** Performance was similar within the reported standard errors. The authors explicitly caution against extrapolating this to more complex WorkArena++ tasks.

**Unresolved inconsistency:** Appendix B identifies the evaluated Llama3 model as having an 8K context, whereas Appendix G reports Llama3 L1 conditions up to 130K. The supplied paper does not explain this discrepancy.

# 9. Results

## 9.1 Full L3 curriculum

Every evaluated model scored **0.0 ± 0.0%** across all five categories and overall (235 instances). This is the strongest evidence that implicit ticket-plus-knowledge-base tasks defeated the evaluated agent configuration (Table 2).

Humans scored **93.9 ± 3.4%** overall on their L3 subset. Category results ranged from **87.5 ± 11.7%** in contextual understanding and planning to **100.0 ± 0.0%** in data-driven reasoning and information retrieval.

## 9.2 Full L2 curriculum

- GPT-3.5: **0.0 ± 0.0**
- GPT-4o: **3.0 ± 1.1**
- GPT-4o-v: **3.8 ± 1.3**
- Llama3: **0.0 ± 0.0**
- Mixtral: **0.0 ± 0.0**

The only nonzero category results were:

- GPT-4o memorization: **14.6 ± 5.1**
- GPT-4o-v memorization: **14.6 ± 5.1**
- GPT-4o-v information retrieval: **3.6 ± 2.5**

On the matched human subset, GPT-4o reached **8.3 ± 8.0%** for memorization and 0% elsewhere, producing **2.1 ± 2.0%** overall.

## 9.3 Existing benchmarks

The same agent family performed materially better on simpler or established benchmarks:

- WorkArena L1: best **42.7 ± 2.7%** for GPT-4o.
- MiniWoB: best **72.5 ± 1.5%** for GPT-4o-v.
- WebArena: best **24.0 ± 1.5%** for GPT-4o-v.

These comparisons support the authors’ claim that WorkArena++ reveals difficulties not apparent from established benchmark scores. Because task distributions differ, these are not controlled measures of the isolated effect of compositional complexity.

## 9.4 Visual input

GPT-4o-v exceeded text-only GPT-4o overall on L2 by **0.8 percentage points** [C: 3.8 − 3.0], and uniquely obtained **3.6 ± 2.5%** on information retrieval. The authors interpret this as evidence that vision can help with chart-reading tasks (pp. 7–8). This evidence is limited because both rates remain very low and no significance test is supplied.

# 10. Figure-by-Figure Interpretation

## Figures 1–4 — Motivation, architecture, and benchmark overview

### Figure 1 — Restocking workflow

Four ServiceNow screenshots show a ticket, dashboard/chart, catalog item, and ticket closure. The numbered sequence demonstrates ticket interpretation → data retrieval → calculated purchasing → workflow completion. It supports the compositional-task claim (p. 2).

### Figure 2 — WorkArena and BrowserGym

Panel (a) presents WorkArena interface categories: workspace, list, form, dashboard, knowledge base, and service catalog. Panel (b) depicts a user goal entering an agent/browser loop, with HTML, AXTree, and screenshot observations flowing to the agent and actions returning to the browser (p. 3).

### Figure 3 — System architecture

The web agent exchanges perceptions and actions with the ServiceNow frontend through BrowserGym. Setup/teardown and validation use backend and frontend ServiceNow APIs. The loop separates agent-visible interaction from benchmark-controlled initialization and correctness checking (p. 3).

### Figure 4 — Task composition and oracle lengths

Panel (a) is a pie chart of five task categories. Labels visibly correspond to 132 planning tasks, 78 retrieval, 312 data-driven reasoning, 56 sophisticated memorization, and 104 contextual-understanding tasks, totaling 682. This visual supports **28 workflows × 2** for memorization, not Appendix C’s 29 × 2.

Panel (b) is a stacked histogram of oracle action counts. L2/L3 tasks extend much farther to the right than L1, with most density below roughly 50 actions but a sparse tail approaching 140. Exact bin counts are not labeled; only qualitative distributional comparison is justified.

## Figures 5–10 — Human study and agent interface

### Figure 5

Rendered consent-form screenshots document informed consent; the small legal text is not confidently readable. Substantively, it supports the reported consent procedure (p. 14).

### Figure 6

Eleven demographic charts summarize 15 participants. Clearly reported accompanying values include 11/15 having worked at ServiceNow, 46.7% first-time users, and 86.7% using ServiceNow no more than a few times monthly (pp. 15–16). The remaining tiny chart labels were not transcribed because exact reading is uncertain.

### Figure 7

A montage of training slides covers the agent concept, BrowserGym chat/browser, console controls, interface components, and a complex-task example. It supports the characterization of training as brief and high-level (p. 16).

### Figure 8

The evaluation UI places chat at left, ServiceNow at right, and a movable human-evaluation console at bottom right. It demonstrates broad interface equivalence between humans and agents plus the human-only control overlay (p. 16).

### Figure 9

A formatted prompt includes instructions, goal, AXTree, focused element, interaction history, action definitions, and a single generic output example. It documents the actual agent input structure (p. 19).

### Figure 10

A marked screenshot maps visible interface elements to identifiers also present in Figure 9. The page itself was rendered; identifiers `a252` and `a261` are called out in the caption (p. 20).

## Figures 11–22 — Task-family examples

Each figure contrasts explicit L2 chat instructions in panel (a) with an L3 ticket in panel (b):

- **Figure 11:** workload balancing using reports and reassignment.
- **Figure 12:** assignment by category expertise and priority.
- **Figure 13:** scheduling change requests under time, overlap, impact, and duration constraints.
- **Figure 14:** identifying duplicate problems and applying priority rules.
- **Figure 15:** retrieving low-stock information from a dashboard and ordering items.
- **Figure 16:** retrieving a laptop warranty date from a list/form.
- **Figure 17:** removing duplicate expenses under hierarchical rules.
- **Figure 18:** selecting investments under a budget, a small knapsack-style problem.
- **Figure 19:** calculating statistics from charts and acting on workers above/below a threshold.
- **Figure 20:** navigating and then sorting/filtering a target list.
- **Figure 21:** offboarding through asset unassignment and user deletion/deactivation.
- **Figure 22:** identifying an infeasible filter involving nonexistent or impossible values.

The consistent visual contrast is the important result: L2 discloses concrete steps, while L3 supplies facts and points to a protocol without spelling out the workflow (pp. 21–26).

## Figures 23–32 — L3 knowledge-base protocols

These full-page screenshots were directly rendered. They encode reusable business rules rather than individual task values:

- **Figure 23:** move a low-priority problem from the busiest to least-busy user.
- **Figure 24:** assign incidents to category experts, with priority determining expert/seniority tier.
- **Figure 25:** schedule change requests within allowed windows, without overlap, by impact and risk-dependent duration.
- **Figure 26:** mark duplicate problems, retaining higher-priority items and applying special handling to critical items.
- **Figure 27:** retrieve dashboard statistics and use them in form, filter, or catalog tasks.
- **Figure 28:** locate a user’s laptop and read its warranty expiration.
- **Figure 29:** identify duplicate expenses and retain records according to linked-task, date, or amount rules.
- **Figure 30:** choose investments maximizing return within budget and report or preserve the selected subset.
- **Figure 31:** create a user, order a laptop, create an asset, and assign it.
- **Figure 32:** unassign assets and remove/deactivate the user.

The screenshots’ broad instructions are readable, but some small hyperlink and metadata text is OCR-sensitive.

## Figures 33–46 — Curriculum, themes, traces, and composition

### Figure 33

A code screenshot shows the category dictionary: task buckets, number of seeds, and bucket weights. It is the configuration input to Algorithm 1. Exact identifiers are visually dense, so the conceptual role is more reliable than a character-perfect transcription (p. 38).

### Figures 34–43

Ten pairs of screenshots show landing and list views for:

1. Astranova,
2. Charlie’s Cookies,
3. Great Pasta,
4. Mighty Capital,
5. Skyward,
6. SpeedyTires,
7. TurboBots,
8. UltraShoes,
9. VitaSphere,
10. WorkArena.

The content and layout remain largely constant while logos and color palettes vary. These figures support visual diversity through branding, but not deep structural UI diversity (pp. 39–44).

### Figure 44

A trace-extraction flow shows repeated cycles of screenshot/AXTree capture and oracle Playwright actions, ending in successful task completion. Stored observations and actions form ground-truth trajectories (p. 45).

### Figure 45

A three-stage onboarding flow: create user → order laptop → assign laptop to user. It illustrates sequential composition and validation (p. 45).

### Figure 46

The same workflow gains a fourth “new task” stage, showing that workflows can be extended by appending an atomic task and validator (p. 46).

## Figures 47–53 — Error evidence

### Figure 47

Folded and expanded all-menu screenshots show why navigation requires exploration: links may be absent from the AXTree until a submenu is expanded (p. 48). The page was not rendered in the supplied selection, so this description relies on extracted text/caption rather than direct visual inspection.

### Figures 48–49

Figure 48 shows a multi-tab request form nearly completed. Figure 49 shows the agent putting the remaining “Close notes” value into the wrong visible field instead of opening the Closure Information tab. The rendered screenshots substantiate exploration and state-tracking failures (pp. 49–50).

### Figure 50

An L3 ticket displays instructions to create a hardware asset. The agent wrongly interprets the ticket text as evidence that the asset already exists and closes the ticket (p. 52).

### Figures 51–52

Figure 51 reportedly shows a correctly populated serial-number field; Figure 52 shows it overwritten with cost-center text. These pages were not rendered, so the specific visual comparison is caption/text-inspected only (pp. 53–54).

### Figure 53

The catalog page is the state in which the model repeatedly clicks the search bar without entering a query or changing strategy. It supports the repeated-action failure category (p. 55).

# 11. Table-by-Table Interpretation

## Table 1 — Benchmark comparison

Columns compare MiniWoB, WebArena, WorkArena L1, and WorkArena++ across task count, environment, task nature, required abilities, and backend (p. 5).

Key values:

- MiniWoB: 125 tasks.
- WebArena: 190.
- WorkArena L1: 33.
- WorkArena++: 682.

The authors position WorkArena++ as combining an out-of-the-box BrowserGym backend with complex enterprise workflows requiring planning, arithmetic/logical reasoning, long-context memory, and retrieval. The comparison is qualitative and author-constructed; it is not an empirical head-to-head measurement of task complexity.

## Table 2 — Principal success rates

Rows divide WorkArena L3 and L2 into five categories, followed by L1, MiniWoB, and WebArena. Columns contain five agent variants plus human and matched-subset GPT-4o results. Units are percent success rate ± standard error (p. 8).

Important observations:

- All L3 agent cells are zero.
- GPT-4o-v is best overall on L2 at 3.8 ± 1.3%.
- GPT-4o and GPT-4o-v tie on L2 memorization at 14.6 ± 5.1%.
- Human overall success is 93.9 ± 3.4% on both levels.
- Human category minima are 84.6 ± 10.0% for L2 data-driven decision-making and 87.5 ± 11.7% for two L3 categories.
- Human maxima are 100% in multiple categories.
- Dashes indicate results not supplied, not zero.
- Existing-benchmark results come from cited prior studies rather than newly rerunning every human baseline.

## Table 3 — Context-size ablation

This one-row table compares Llama3 WorkArena-L1 success under 130K, 64K, 32K, and 13K context limits (p. 56).

The observed range is only **3.4 percentage points** [C: 18.2 − 14.8]. Because all standard errors are about 2 points and no formal test is reported, the evidence supports “similar measured performance,” not proven equivalence.

# 12. Diagram / Architecture Interpretation

The core architecture spans Figures 2, 3, and 44:

1. A natural-language goal enters through chat.
2. The browser exposes HTML/AXTree and optionally a marked screenshot.
3. The model reviews the current observation plus complete action/thought history.
4. It chooses one high-level BrowserGym action.
5. BrowserGym executes that operation.
6. Errors return in the next observation.
7. The loop continues for at most 50 agent steps.
8. Independent validators inspect frontend and database state.
9. Setup/teardown isolates each task.
10. The oracle can replace the model in this loop to generate correct demonstration traces.

This design separates three paths:

- **Control path:** model → browser action.
- **Observation path:** browser → structured/textual/visual state.
- **Evaluation path:** hidden validator → binary reward.

Task composition adds another layer: multiple atomic setup/oracle/validation components are chained into a workflow (Figures 45–46).

# 13. Equations and Mathematical Concepts

The paper contains no numbered mathematical equations or theorems. Three mathematical concepts are important.

## Binary success reward

The validator returns **0 or 1** depending on whether the task was completed correctly (p. 3). The benchmark-level success rate is the percentage of evaluated instances returning success.

## Success rate with standard error

Tables 2–3 report:

\[
\text{SR} \pm \text{SE}
\]

where SR is success rate in percent and SE is the reported standard error. The paper does not provide the explicit estimator formula, clustering assumptions, or confidence-interval conversion.

## Knapsack-style optimization

Investment tasks ask for a subset maximizing total return while keeping total cost within a budget (pp. 6, 24). In plain language: choose the most valuable feasible combination, not merely the individually highest-return item. The paper gives no formal symbolic objective.

## Algorithm 1

Let \(T\) be a tuple/list of `(task, seed)` pairs. A meta-seed initializes reproducible sampling. For each skill category and generated seed, tasks are sampled from weighted buckets without replacement and appended to \(T\) (p. 37). The algorithm is procedural pseudocode rather than a learned optimization algorithm.

# 14. Interpretation and Discussion

## Answer to RQ1: Are the tasks solvable?

Yes, for the sampled human cohort: human success was 93.9% on both L2 and L3 subsets. This establishes practical feasibility for trained human users under the study conditions, not universal ease for every knowledge worker.

## Answer to RQ2: Why do agents fail?

The trace analysis attributes failure to interconnected weaknesses:

- inaccurate grounding of identifiers and page information;
- insufficient exploration of menus and tabs;
- invented actions or controls;
- failure to translate correct reasoning into the corresponding action;
- misunderstanding tickets and workflow state;
- failure to verify consequences;
- behavioral loops after ineffective actions.

These failures occur before sophisticated business reasoning in many examples, so benchmark difficulty arises from the combination of navigation, grounding, memory, planning, and verification.

## Answer to RQ3: Expected generalization

The authors expect some findings to generalize because lists, forms, and dashboards are common elsewhere and many errors are not ServiceNow-specific (p. 55). This is an argument, not an empirical cross-platform result.

## Answer to RQ4: Broader representativeness

The authors agree that multiple environments would improve representativeness but prioritize ServiceNow because it integrates with BrowserGym, is comparatively easy to provision, and supports modular compositional tasks (pp. 55–56).

## Internal inconsistencies and unresolved points

1. **Memorization count:** Main text and Figure 4 report **28 × 2 = 56** memorization tasks (pp. 4, 6). Appendix contents and §C.4 report **29 × 2** (pp. 13, 25). The detailed subtypes in §C.4 list 26 navigation tasks plus 2 user-management tasks, totaling 28. Thus 28 is internally consistent with the 682 total; the appendix heading appears inconsistent, but the paper does not issue a correction.

2. **Context-size ablation versus model specification:** Appendix B reports Llama3-70B with an 8K model context, but Table 3 tests “Llama3” at 13K–130K. The supplied text does not explain whether this used a different context extension, implementation, or model configuration.

3. **Curriculum counts:** Figure 4b uses 33 L1 tasks × 5 seeds for oracle-length comparison, while Table 2 evaluates L1 over 33 × 10 seeds. These address different analyses and are not necessarily contradictory, but the distinction matters.

4. **“Significantly outperforms”:** The prose says GPT-4o-based agents significantly outperform GPT-3.5 (p. 8), but no hypothesis test is supplied. The numerical differences are large, yet “significantly” cannot be interpreted as a documented statistical-significance result.

# 15. Contributions and Novelty

## Benchmark contribution

A collection of 682 L2/L3 tasks representing 341 compositional knowledge-work workflows.

## Conceptual contribution

A hierarchy separating atomic L1 tasks from explicit compositional L2 tasks and implicit ticket-plus-protocol L3 tasks.

## Methodological contribution

Five skill categories intended to probe planning, retrieval, data-driven reasoning, memorization, and infeasibility recognition.

## Systems contribution

Standardized ServiceNow installation, per-task user isolation, setup/teardown machinery, frontend/database validation, and BrowserGym integration.

## Data contribution

Oracle-based generation of screenshots, AXTree/DOM observations, and correct action traces suitable for future fine-tuning.

## Experimental contribution

Evaluation of five agent configurations and a matched human study demonstrating a very large observed performance gap.

## Diagnostic contribution

A qualitative taxonomy with detailed examples of grounding, exploration, hallucination, goal-understanding, and consequence-assessment failures.

# 16. Limitations

## Authors’ stated limitations

- The 682 tasks do not exhaustively cover knowledge-work tasks or personas; thousands more would be needed (§7, p. 10).
- Safety and robustness against malicious behavior are not evaluated (§7).
- Tasks do not cross beyond ServiceNow (§7; Appendix G.1).
- More open and closed models, especially very-long-context models, could have been included (§7).
- Visual diversity is limited mainly to ten brands and color/logo changes; more could be added (§3.3, p. 6).
- Human participants showed a learning effect not directly controlled (Appendix A.5, p. 14).
- A general announcement helped participants remember to save L3 ticket-state changes (pp. 14–15).
- The human cohort was small and unrepresentative: many were ServiceNow-affiliated and highly educated (pp. 16–17).
- Humans had no action cap, whereas agents had 50 steps (p. 17).

## Additional evidence-based analyst observations

- **[D] Validator dependence:** Benchmark validity relies on the correctness and completeness of many hand-written setup/oracle/validator functions.
- **[D] Limited statistical characterization:** Results use success rate and standard error without significance tests, confidence intervals, time-to-completion distributions, or hierarchical modeling of participants/tasks.
- **[D] Error-analysis reproducibility:** No sampling protocol, annotation rubric, category frequency, or independent coding agreement is reported.
- **[D] Prompt dependence:** Prompt tuning was performed, but the supplied paper does not quantify tuning sensitivity or provide an ablation.
- **[D] Interface diversity:** The ten themes visibly alter branding and colors while preserving similar layouts; this tests appearance variation more than structural site diversity.
- **[D] Long-task truncation:** Removing the AXTree/HTML tail may systematically hide late-listed elements, potentially confounding reasoning ability with observation truncation.
- **[D] Human comparison:** Training, self-exploration, unlimited actions, and institutional familiarity mean the human–agent comparison measures complete systems under different resource constraints, not purely cognitive capacity.

# 17. Threats to Validity

## Internal validity

The 50-step agent limit, prompt truncation, prompt tuning, and human-only announcement could affect success independently of the targeted reasoning skills. Binary validators may also misrepresent partial progress.

## Construct validity

Task categories are plausible but not empirically validated as isolated cognitive constructs. A “planning” failure may actually arise from grounding or navigation, while a “memorization” failure may arise from truncated observations.

## External validity

All workflows use one platform. The authors argue that common UI elements and non-platform-specific errors should transfer, but no cross-software WorkArena++ experiment tests this.

## Statistical conclusion validity

Standard errors are supplied, but the paper gives no formal comparisons or corrections. Some category estimates have wide SEs because the human subset is small.

## Ecological validity

Tickets, dashboards, knowledge bases, and enterprise forms resemble real work. However, generated values, constrained workflows, binary validation, and isolated accounts simplify organizational practice.

## Reproducibility

Strengths include reserved seeds, curriculum pseudocode, reported model identifiers, prompt limits, an open codebase, and automated setup/validation. Remaining uncertainty concerns exact model-serving parameters, prompt-tuning decisions, validator coverage, and the unexplained context-length configuration.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Add more ServiceNow tasks.
- Develop safety and cybersecurity evaluations.
- Create a hidden test set for competitions.
- use oracle traces to fine-tune stronger LLM/VLM agents.
- build longer workflows inspired by occupational task databases.
- add human–agent or agent–agent collaboration and delegation.
- incorporate multiple external software environments.
- introduce an L4-style cross-environment level.
- expand task and visual diversity through community contributions (pp. 10, 55–56).

## B. Additional open questions

- Which failure category accounts for the most lost success?
- How much improvement comes from better perception versus planning versus memory?
- Would explicit state tracking prevent overwritten fields and imagined progress?
- How does performance change without thought-history reinjection?
- What is the isolated effect of screenshots when chart-reading tasks are evaluated at adequate scale?
- How often do the 50-step limit and prompt truncation directly cause failure?
- How robust are validators to alternative correct workflows?
- Would a larger, demographically representative human study reproduce 93.9%?
- Can agents trained on oracle traces generalize to unseen task templates rather than memorizing interface routines?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| Agent | Software that observes a web page and autonomously selects actions |
| LLM | Large language model |
| VLM | Vision-language model |
| Web agent | Agent designed to operate websites or web applications |
| BrowserGym | Standard interaction and evaluation environment for browser agents |
| WorkArena L1 | Original 33-task enterprise benchmark emphasizing atomic interactions |
| WorkArena++ | New 682-task compositional benchmark |
| L2 | Explicit chat instructions for a compositional workflow |
| L3 | Task ticket plus separately retrieved knowledge-base protocol |
| Atomic task | A small primitive workflow, such as filling one form |
| Compositional task | A workflow formed by chaining atomic tasks |
| Oracle | Human-authored automation that correctly solves a task |
| Validator | Program that checks whether page/database state satisfies the goal |
| AXTree | Accessibility tree: structured textual representation of web elements |
| HTML | HyperText Markup Language, the document structure of a webpage |
| DOM | Document Object Model, the browser’s structured page representation |
| bid | BrowserGym’s unique identifier for an element |
| iframe | Embedded document whose element IDs may have a prefix such as `a` |
| Set-of-marks | Visual overlay associating screenshot elements with identifiers |
| Playwright | Browser-automation mechanism used by the oracle |
| REST API | Programmatic interface used here for backend setup/validation |
| Chain-of-thought prompting | Prompt format requesting intermediate reasoning before an action |
| Seed | Number controlling reproducible task configuration |
| Meta-seed | Number controlling reproducible curriculum sampling |
| Curriculum | Standard sampled set of task instances |
| SR | Success rate |
| SE | Standard error |
| Infeasible task | Request impossible under the available fields, records, or configurations |
| Knapsack problem | Selection problem maximizing value under a limited budget |
| TGI | Text Generation Inference, used to serve open models |
| `T` | Algorithm 1’s collection of `(task, seed)` pairs |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Workflows | 341 | workflows | Each appears as L2 and L3 | Author-reported | p. 4, §3.1 |
| Total tasks | 682 | tasks | 341 × 2 levels | Author-reported | pp. 1, 4 |
| Planning tasks | 132 | tasks | 66 × 2 | Author-reported | p. 5 |
| Retrieval tasks | 78 | tasks | 39 × 2 | Author-reported | p. 6 |
| Data-driven tasks | 312 | tasks | 156 × 2 | Author-reported | p. 6 |
| Memorization tasks | 56 | tasks | 28 × 2; appendix heading conflicts | Author-reported / visually readable | pp. 4, 6, Fig. 4 |
| Infeasibility tasks | 104 | tasks | 52 × 2 | Author-reported | p. 6 |
| Agent curriculum | 470 | instances | 235 L2 + 235 L3 | Author-reported | p. 37 |
| Human curriculum | 98 | instances | 49 workflows × 2 levels | Author-reported | p. 14 |
| Human participants | 15 | people | In-person study | Author-reported | pp. 8, 13 |
| Human overall L2 | 93.9 ± 3.4 | % SR ± SE | Human subset | Author-reported | Table 2, p. 8 |
| GPT-4o matched L2 | 2.1 ± 2.0 | % SR ± SE | Same subset | Author-reported | Table 2 |
| Human–GPT-4o L2 gap | 91.8 | percentage points | 93.9 − 2.1 | Analyst-derived | Table 2 |
| Human overall L3 | 93.9 ± 3.4 | % SR ± SE | Human subset | Author-reported | Table 2 |
| All agents L3 | 0.0 ± 0.0 | % SR ± SE | Full 235-instance curriculum | Author-reported | Table 2 |
| GPT-4o full L2 | 3.0 ± 1.1 | % SR ± SE | 235 instances | Author-reported | Table 2 |
| GPT-4o-v full L2 | 3.8 ± 1.3 | % SR ± SE | 235 instances | Author-reported | Table 2 |
| Vision–text L2 difference | 0.8 | percentage points | 3.8 − 3.0 | Analyst-derived | Table 2 |
| GPT-4o-v L2 retrieval | 3.6 ± 2.5 | % SR ± SE | 56 instances | Author-reported | Table 2 |
| GPT-4o(-v) L2 memorization | 14.6 ± 5.1 | % SR ± SE | 48 instances | Author-reported | Table 2 |
| GPT-4o WorkArena L1 | 42.7 ± 2.7 | % SR ± SE | 33 × 10 seeds | Author-reported | Table 2 |
| GPT-4o-v MiniWoB | 72.5 ± 1.5 | % SR ± SE | 125 × 5 seeds | Author-reported | Table 2 |
| GPT-4o-v WebArena | 24.0 ± 1.5 | % SR ± SE | 812 instances | Author-reported | Table 2 |
| Maximum agent steps | 50 | actions/time-steps | Per episode | Author-reported | p. 7 |
| Parse retries | Up to 4 | retries | Malformed model output | Author-reported | pp. 7, 18 |
| Evaluation seeds | 0–9 | seeds | Reserved for evaluation | Author-reported | pp. 7, 37 |
| Interface themes | 10 | themes | Fictitious brands | Author-reported | pp. 6, 39–44 |
| Training | 15 + 15 | minutes | Video + exploration | Author-reported | pp. 8, 14 |
| ServiceNow-employed participants | 11/15 | people | Cohort characteristic | Author-reported | p. 16 |
| First-time users | 46.7 | % | Human cohort | Author-reported | p. 16 |
| Llama3 context-ablation range | 14.8–18.2 | % SR | WorkArena L1 | Author-reported | Table 3, p. 56 |
| Ablation spread | 3.4 | percentage points | 18.2 − 14.8 | Analyst-derived | Table 3 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WorkArena++ is much harder for evaluated agents than L1/MiniWoB/WebArena | L2 ≤3.8%; L3 0%; substantially higher prior-benchmark scores | Table 2, X1 | pp. 7–8 | Strong descriptive evidence; benchmarks differ structurally |
| Tasks are feasible for humans | 93.9% overall human success | Table 2, X2 | p. 8 | Strong for sampled cohort; limited representativeness |
| L3 instruction delivery is especially difficult | All five agents scored 0% across every L3 category | Table 2 | p. 8 | Strong for evaluated agents/configuration |
| Visual observations can help retrieval | GPT-4o-v obtained 3.6% where text GPT-4o obtained 0% | Table 2 | pp. 7–8 | Suggestive; very small absolute success and no significance test |
| Memorization is the only L2 category with notable agent success | GPT-4o and GPT-4o-v both 14.6% | Table 2 | p. 8 | Descriptive, still low |
| Current failures extend beyond UI manipulation | Trace examples show goal, consequence, hallucination, and looping errors | X3, Figs. 47–53 | pp. 47–54 | Rich qualitative evidence; no prevalence counts |
| Benchmark tasks are genuinely compositional | Workflow/task examples chain retrieval, decision, catalog, form, and ticket operations | Figs. 1, 11–22, 45–46 | pp. 2, 21–26, 45–46 | Strong design evidence |
| Evaluation is reproducible | Reserved seeds, curriculum algorithm, validators, isolated accounts | Algorithm 1, Fig. 3 | pp. 6–7, 37 | Strong procedural support; code not supplied here |
| Oracle traces can generate fine-tuning data | Oracle actions and browser observations are intercepted and saved | Fig. 44 | p. 45 | Mechanism described; no downstream fine-tuning experiment |
| L1 performance is insensitive to tested context sizes | 14.8–18.2% across four conditions | Table 3, X4 | p. 56 | Limited to L1; context/model inconsistency unresolved |
| Findings should generalize beyond ServiceNow | Common UI primitives and non-specific error types | Appendix G.1 | p. 55 | Author argument, not empirically tested |

# 22. Very Simple Explanation

Imagine testing a robot office assistant. Easy tests might say, “Click this button” or “put this name in this box.” WorkArena++ gives it a whole job instead: read a ticket, find instructions elsewhere, inspect a chart, make a decision, fill several forms, buy the correct item, and then close the ticket.

The researchers made 682 such tests inside a ServiceNow environment. In the easier L2 version, the assistant gets explicit steps. In the harder L3 version, it gets a realistic ticket and must find the company procedure itself.

Humans completed about 94% of the sampled tasks. The tested AI agents completed almost none; every agent scored zero on L3. The agents often knew pieces of what to do but clicked the wrong element, failed to open hidden menus, invented nonexistent controls, misunderstood whether work was already done, or repeated useless actions.

So the paper’s message is not simply “AI is bad at clicking websites.” It is that reliable office automation requires perception, memory, planning, reasoning, exploration, and self-checking to work together. WorkArena++ is designed to measure that complete combination.

# Completeness Audit

## Inventory and coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract and §1 | Yes | Yes | Fully represented | Motivation and contributions covered |
| §2 Background | Yes | Yes | Fully represented | BrowserGym, WorkArena, oracle/validator |
| §3 WorkArena++ | Yes | Yes | Fully represented | Levels, skills, technical features |
| §4 Experiments | Yes | Yes | Fully represented | Curriculum, agents, results, humans, errors |
| §5 Related Work | Yes | Yes | Represented in compressed form | Prior systems/datasets grouped; no external verification |
| §6 Conclusion/Future Work | Yes | Yes | Fully represented | Included in findings and future work |
| §7 Limitations/Societal Impacts | Yes | Partly | Represented in compressed form | Limitations fully covered; societal impacts summarized below |
| References | Yes | No individual enumeration | Deliberately compressed | Bibliographic list is supporting material rather than a substantive experiment |
| Appendix A | Yes | Yes | Fully represented | Participants, protocol, curriculum, platform, limitations |
| Appendix B | Yes | Yes | Fully represented | Agent design and prompt |
| Appendix C | Yes | Yes | Fully represented | All task families and protocols |
| Appendix D | Yes | Yes | Fully represented | Algorithm and curriculum |
| Appendix E | Yes | Yes | Fully represented | Themes, traces, compositional extension |
| Appendix F | Yes | Yes | Fully represented | All named error categories/examples |
| Appendix G | Yes | Yes | Fully represented | Scope, expansion, context ablation |
| Explicit RQ1–RQ4 | Yes | Yes | Fully represented | No formal hypotheses found |
| X1 agent evaluation | Yes | Yes | Fully represented | Table 2 |
| X2 human study | Yes | Yes | Fully represented | Table 2 and Appendix A |
| X3 error analysis | Yes | Yes | Fully represented | Qualitative only |
| X4 context ablation | Yes | Yes | Fully represented | Table 3 |
| Figures 1–4 | Yes | Yes | Fully represented | Directly rendered |
| Figures 5–10 | Partial | Yes | Fully/compressed | Figs. 5–8 rendered; 9–10 supplied visually |
| Figures 11–22 | Yes | Yes | Represented in compressed form | Repeated L2/L3 paired structure |
| Figures 23–32 | Yes | Yes | Represented in compressed form | Screenshot protocols summarized individually |
| Figure 33 | Yes | Yes | Represented in compressed form | Dense code screenshot |
| Figures 34–43 | Yes | Yes | Deliberately compressed | Repetitive theme demonstrations |
| Figures 44–46 | Yes | Yes | Fully represented | Trace and task-composition diagrams |
| Figure 47 | Caption/text only | Yes | Partial visual accessibility | Page 47 not rendered |
| Figures 48–50 | Yes | Yes | Fully represented | Rendered |
| Figures 51–52 | Caption/text only | Yes | Partial visual accessibility | Page 51 not rendered |
| Figure 53 | Yes | Yes | Fully represented | Rendered |
| Table 1 | Yes | Yes | Fully represented | Rendered and extracted |
| Table 2 | Yes | Yes | Fully represented | All major values preserved |
| Table 3 | Yes | Yes | Fully represented | Rendered and extracted |
| Algorithm 1 | Yes | Yes | Fully represented | Pseudocode summarized faithfully |
| Major equations | Not applicable | Yes | No equations present | Mathematical concepts covered |
| Contributions | Yes | Yes | Fully represented | Seven contribution types separated |
| Author-stated limitations | Yes | Yes | Fully represented | Main text and Appendix A/G |
| Supplementary files | No | Yes | Missing from supplied material | No separate supplement supplied |

## Societal-impact coverage

The authors anticipate productivity and accessibility benefits, including assistance for impaired users and possible creation of new work opportunities. They also identify job displacement, privacy/security risks, erosion of human skills and decision-making, and computational energy use as possible harms (§7, p. 10). This material was inspected and deliberately compressed here because it does not alter the benchmark methodology or numerical conclusions.

## Missing or inaccessible material

- No separate supplementary artifacts were provided.
- The benchmark repository, exact curriculum file, GitHub Wiki, source code, validators, and trace dataset were referenced but not supplied.
- Pages 9, 10, 12, 47, and 51 were not visually rendered in the supplied image set. Their extracted text was available; consequently Figures 47, 51, and 52 were not directly visually inspected.
- Tiny text in screenshot-heavy Figures 5–8, 11–43, and 48–53 is not uniformly legible. Their captions, nearby text, and clearly visible structure were used without inventing unreadable details.
- Exact task-completion times were reportedly recorded in the human study but are not reported in the supplied paper.

## Uncertain interpretations

- The correct memorization-task count is inconsistent: 28 × 2 in the main text/Figure 4 versus 29 × 2 in Appendix C’s headings.
- The Llama3 context-ablation settings up to 130K conflict with the 8K model context stated in Appendix B.
- “Significantly outperforms” is not accompanied by a reported statistical test.
- Exact frequencies of error categories cannot be determined from the qualitative examples.
- The standard-error computation and dependency treatment across seeded tasks are not specified.

## Deliberately compressed material

- Individual bibliography entries.
- Repetitive visual-theme screenshots in Figures 34–43.
- Repeated visual formatting of the L2/L3 pairs in Figures 11–22.
- Screenshot-level typography and hyperlinks in the ten knowledge-base protocols.
- Decorative interface branding and incidental screenshot metadata.
- Acknowledgments and author-role footnotes, except publication and contribution information relevant to provenance.

## Potential omissions

No known substantive main section, appendix, experiment, table, algorithm, contribution, or author-stated limitation from the document inventory is absent. Some figures were necessarily represented through captions/text rather than direct visual inspection, and repetitive visual material was explicitly compressed as recorded above.