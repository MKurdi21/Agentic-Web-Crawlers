# Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–56, together with rendered images for 51 pages. All 56 pages have supplied text records; therefore no physical page is apparently absent from the text sequence. Images are not supplied for pp. 9, 10, 12, 47, and 51. Those five pages were inspected through supplied text only. The remaining pages were available for direct visual inspection. This distinction matters particularly for Appendix F: its examples span both visually inspected and text-only pages.

The main document, references, and Appendices A–G are present. All three numbered tables and Algorithm 1 are accessible. No numbered theorem, lemma, or substantive displayed mathematical equation appears in the supplied work. Mathematical notation occurs in the sampling algorithm, task-count arithmetic, statistical reporting, and an informal optimization example. Small text embedded in screenshots is less readable than surrounding prose. Pages 27–36 and 38 contain substantive screenshot content despite having almost no native extracted text; their visual content was inspected directly. The ten application-theme illustrations on pp. 39–44 were also inspected visually. Individual tiny interface labels, consent-form paragraphs, and training-slide text cannot all be transcribed confidently at the supplied resolution.

No supplementary file or executable repository snapshot is supplied. The paper references its codebase, GitHub Wiki, exact curricula, human-evaluation software, task implementations, and external publications. These artifacts were not opened or independently checked. The supplied accessibility metadata reports zero embedded files; that does not establish that every artifact associated with the publication is present. OCR would be useful for exhaustive screenshot transcription, but no OCR tool was called. Direct visual reading supplements the supplied extraction. No native-text/OCR comparison was performed.

Evidence labels used below are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information is introduced. Confidence is HIGH for clear text and table entries, MEDIUM for interpretation or small visual content, and UNKNOWN where the supplied work cannot resolve an issue. The supplied source hash is retained as an identifier; it was not independently recomputed.

# 1. Plain-language orientation

WorkArena++ studies whether an artificial-intelligence system can carry out realistic office work through a web browser. It is a benchmark paper with systems contributions and an empirical evaluation, rather than a security experiment. Its central distinction is between answering a question and completing a sequence of actions in software: a useful agent must read the right information, remember it, choose an appropriate action, operate the interface, and verify that the intended change actually happened.

[A] The researchers introduce 682 tasks built from 341 workflows, each presented at two difficulty levels. Examples include restocking inventory, assigning work, scheduling requests, removing duplicate expenses, choosing investments under a budget, and onboarding employees. The environment is the ServiceNow enterprise platform, accessed through BrowserGym, a framework for browser-agent interaction and evaluation. The benchmark also includes impossible requests that agents should recognize rather than blindly execute. Sources: pp. 1–6, §§1–3.

[A] The tested agents perform poorly on these workflows. On the standardized agent curriculum, every tested agent obtains 0.0% success on L3, where instructions are distributed between an assigned ticket and a knowledge base. On L2, where the user supplies explicit procedural instructions, GPT-4o obtains 3.0% and its vision-enabled version obtains 3.8%; the other tested agents obtain 0.0%. Human participants perform much better on a smaller curriculum. These results apply to the particular agents, prompts, context budgets, environments, and stopping conditions reported in this paper. They do not establish an immutable limit on web agents. Sources: pp. 7–8, Table 2.

[D] For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' the paper supplies relevant mechanisms and failure examples, but no direct vulnerability comparison. It shows an agent translating page content into actions that can change enterprise records. It also shows failures in interpreting instructions, choosing targets, remembering state, and assessing consequences. These are useful reliability observations for motivating a security analysis. They are not measured attacks, prompt-injection results, or evidence that web agents have a quantified vulnerability advantage over standalone large language models.

# 2. Document roadmap and inventory

The original title is **WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks**. The authors are Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, and Alexandre Drouin. Affiliations are ServiceNow Research, Mila, Polytechnique Montréal, and Chandar Research Lab. Boisvert and Thakkar are marked as equal contributors; Gasse, Caccia, and Le Sellier De Chezelles as core contributors; Lacoste and Drouin as equal supervisors. The supplied venue is the NeurIPS 2024 Track on Datasets and Benchmarks. No keyword list is supplied. Source: p. 1.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| S0 | Abstract | p. 1 | Benchmark motivation, scope, and contributions |
| S1 | §1 Introduction | pp. 1–2 | Office-work motivation and contribution list |
| S2 | §2 Background; §§2.1–2.2 | p. 3–4 | BrowserGym, WorkArena, certifiability, hosting |
| S3 | §3 WorkArena++ | pp. 4–6 | Composition, L2/L3, skill categories, technical features |
| S4 | §4 Experiments; §§4.1–4.5 | pp. 6–9 | Curriculum, agents, results, humans, errors |
| S5 | §5 Related Work | p. 9 | Position relative to other benchmarks and datasets |
| S6 | §6 Conclusion and Future Work | pp. 9–10 | Findings and proposed extensions |
| S7 | §7 Limitations and Potential Societal Impacts | p. 10 | Scope, safety omission, benefits and harms |
| REF | Acknowledgments and References | pp. 10–12 | Attribution and cited literature |
| A | Appendix A, §§A.1–A.5 | pp. 13–17 | Human sample, protocol, platform, limitations |
| B | Appendix B | pp. 18–20 | Detailed agent implementation and prompt example |
| C | Appendix C, §§C.1–C.6 | pp. 21–36 | Task families, examples, knowledge-base protocols |
| D | Appendix D | pp. 37–38 | Sampling algorithm and configuration |
| E | Appendix E, §§E.1–E.2 | pp. 39–46 | Themes, trace extraction, workflow extension |
| F | Appendix F | pp. 47–55 | Qualitative execution-error examples |
| G | Appendix G, §§G.1–G.3 | pp. 55–56 | Transfer arguments, expansion, context ablation |
| F1–F53 | Figures 1–53 | pp. 2–55 | Architecture, tasks, protocols, examples, themes |
| T1–T3 | Tables 1–3 | pp. 5, 8, 56 | Benchmark comparison, results, context ablation |
| ALG1 | Algorithm 1 | p. 37 | Reproducible curriculum construction |

The extraction ledger underlying this synthesis tracks framing, configuration, numerical results, visual objects, claims, limitations, and inconsistencies by the page and original section references used throughout. The inventory includes three main empirical analyses—agent benchmarking, human comparison, and qualitative error analysis—plus the oracle-length characterization and context-size ablation. The figure-level inventory is expanded in §10 and the coverage audit.

# 3. Background and context

[A] A **large language model (LLM)** produces language-based outputs; this study embeds such a model in a loop that observes a browser and selects the next action. A **vision-language model (VLM)** additionally receives an image of the page. The paper's GPT-4o-v label denotes its vision-enabled GPT-4o agent. A **web agent** is the overall system that uses these outputs to interact with websites. These agent evaluations should not be confused with tests of the same model answering questions without browser interaction. Sources: pp. 2–3, 7, 18.

[A] BrowserGym supplies observations, chat, and standardized actions. An **accessibility tree (AXTree)** is described as a compressed representation of the page's HyperText Markup Language (HTML). A screenshot provides visual appearance; **set-of-marks** overlays element identifiers so that visible objects can be matched to action targets. A **bid** is BrowserGym's identifier for an element. An element inside iframe a can have an identifier such as a324. Losing the iframe prefix can target the wrong element or produce an error. Sources: pp. 3, 18–20, 47.

[A] The original WorkArena tasks become **L1**, meaning level 1. They primarily exercise basic interface operations, such as filling forms and sorting lists. WorkArena++ composes these operations into workflows. An **atomic task** is a simpler building block; a **compositional task** combines several such blocks into a larger goal. Some newly implemented atomic tasks extend beyond the original L1 collection. Sources: pp. 3–4 and footnote 4.

[A] An **oracle** is a human-coded browser-automation solution, not an LLM judge. A **validator** checks whether a task succeeded, using database state and/or current-page state, and returns a binary reward of 0 or 1. **Playwright** is the browser-automation tool used by the oracles. A **Personal Developer Instance** is the remote-hosted ServiceNow environment used for evaluation. These definitions explain how the researchers can separate an agent's statement that it succeeded from externally checked task completion. Source: p. 3, §2.2.

# 4. Research problem and gap

**Existing problem [A].** Autonomous assistants could reduce repetitive office work, but their ability to turn apparent planning and reasoning competence into successful software use remains underexplored. The paper focuses on knowledge workers using enterprise software, rather than general conversation or unrestricted computer use. Sources: pp. 1–2.

**Previous shortcomings according to the authors [A].** Earlier synthetic environments emphasize low-level interactions. WebArena introduces realistic website tasks; WorkArena introduces enterprise interfaces, but its original 33 tasks remain predominantly atomic. Merely succeeding at a single form or explicit navigation goal does not adequately test multi-step reasoning, constraint satisfaction, cross-page memory, or application of retrieved rules. Sources: pp. 2–5, 9.

**Research gap [A].** The authors seek a benchmark that combines realistic enterprise interfaces with workflows requiring planning, mathematical or logical reasoning, retrieval, memory, and contextual understanding. They also seek standardized evaluation, reusable validation, and a practical route to generating demonstration traces. Their statement that this is the first web-agent benchmark requiring such complex skills is a novelty claim reported from the paper, not independently verified here. Source: p. 2.

**Scope [A].** WorkArena++ operates within ServiceNow. Its visual themes diversify branding and colors, while the underlying platform remains the same. It does not exhaustively represent occupations, all knowledge-work tasks, or interactions with external software. Most importantly for the user's research question, it does not evaluate safety or robustness against malicious behaviors. Sources: pp. 6, 10, 55.

# 5. Research questions, objectives, and hypotheses

The paper does not introduce a formal numbered hypothesis-testing framework. Its objectives should therefore remain objectives rather than invented hypotheses.

| ID | Status | Question or objective | Evidence used |
|---|---|---|---|
| O1 | Author objective | Construct realistic compositional enterprise tasks requiring complex skills | §§3, C; task and protocol inventory |
| O2 | Author objective | Standardize feasible, reproducible evaluation across skill categories | §§4.1, D; Algorithm 1 |
| O3 | Author objective | Measure contemporary baseline-agent performance | §4.3; Table 2 |
| RQ1 | Explicit author question | Are these tasks actually solvable? | p. 8; human evaluation |
| RQ2 | Explicit author question | Why do the agents fail? | p. 8; §§4.5, F |
| RQ3 | Explicit discussion question | Do insights generalize beyond ServiceNow? | §G.1; reasoned argument, no transfer experiment |
| RQ4 | Explicit discussion question | Would additional software environments improve representativeness? | §G.1; authors answer affirmatively |
| X5Q | Experiment purpose | How does context length affect Llama3-agent performance on L1? | §G.3; Table 3 |

[A] Appendix A hypothesizes that increasing human efficiency during the study mainly reflects growing interface familiarity. This is an explanatory hypothesis about a learning effect, not a separately controlled experimental test. Source: p. 14.

[D] The user's security question is an external analytical lens applied to this supplied work. The paper can inform it by identifying observation-to-action dependencies and failures. It cannot answer the comparative proposition that browser agents are more vulnerable than standalone LLMs, because no such comparison is performed.

## 6. Assumptions / Threat Model

[A] The evaluated system consists of a model-driven agent, BrowserGym, a browser, and a remote ServiceNow instance. Task setup and teardown configure the environment; the agent acts through the frontend; validation uses frontend JavaScript and backend Representational State Transfer (REST) interfaces. The tested agents use restricted high-level actions rather than every action mode depicted in BrowserGym's general overview. Sources: pp. 3, 7, 18.

[A] Evaluation assumes the supplied task configuration, oracle, and validator define the intended outcome. Each task runs under a newly created user account, later deleted, to reduce interference between tasks. The installer standardizes parameters, themes, knowledge bases, and layouts. These measures support reproducibility and task isolation. They are not reported as defenses validated against a malicious attacker. Source: p. 6.

**Security boundary [A/D].** No attacker, adversarial objective, attacker-controlled field, trust-boundary policy, exploit success criterion, or defensive comparison is specified. Tickets and knowledge-base articles supply legitimate benchmark instructions. [D] Their role illustrates how an agent can rely on page-resident content to decide what to do; it does not demonstrate malicious content being promoted into authority. Likewise, the general BrowserGym diagram includes an unsafe-Python action option, but the actual baseline configuration is limited to chat, infeasibility reporting, and bid-based interaction. Treating that diagram as proof that these agents executed arbitrary Python would misrepresent the method.

[A] The practical resource assumption is a maximum of 50 agent time steps. The authors argue from oracle action lengths that most sampled tasks can be completed within this budget. Humans have no explicit action limit. These are material comparison conditions. Sources: pp. 7, 17.

# 7. Methodology

## 7.1 Benchmark construction

[A] The benchmark contains 341 underlying workflows presented in two ways, yielding 2 × 341 = 682 tasks. **L2** provides detailed instructions in the chat. **L3** places the assignment in a ticket, includes task-specific details, and directs the agent toward company knowledge-base rules when needed. The underlying workflow remains the same, but L3 requires discovering and integrating instructions across sources, remembering details, acting, and properly closing the ticket. Sources: pp. 4–5.

[A] The five skill categories in the main text are planning/problem solving, 66 × 2; information retrieval, 39 × 2; data-driven decision-making/reasoning, 156 × 2; sophisticated memorization, 28 × 2; and contextual understanding through infeasible tasks, 52 × 2. [C] Their workflow counts sum to 66 + 39 + 156 + 28 + 52 = 341. Appendix C's memorization heading instead states 29 × 2; that inconsistency is retained rather than repaired. Sources: pp. 5–6, 13, 25.

[A] Planning tasks include balancing workload, assigning work by expertise and priority, scheduling requests under time and risk constraints, and deduplicating problems. Retrieval tasks require reading charts, lists, or forms and then acting on what was found. Reasoning tasks include hierarchical expense rules, budget-constrained investment selection, and mean/median/mode calculations. Memory tasks connect navigation and data entry or user management. Infeasible tasks require recognizing unavailable fields or invalid configurations, sometimes with an explanation naming the obstacle. Sources: pp. 21–26.

## 7.2 Curriculum and sampling

[A] Task types have many possible seeded configurations. To avoid evaluating every possible instance, the researchers create skill categories and buckets of task types requiring similar abilities. They sample without replacement within buckets, using specified bucket weights and different seed counts across categories. A meta-seed makes the resulting collection reproducible. The curriculum yields 235 instances per difficulty level, or 470 L2/L3 instances together. Meta-seeds 0–9 are reserved for evaluation; other seeds may be used for tuning. Sources: pp. 7, 37–38.

[D] 'Uniform across skills' should be read as the design goal of balanced skill coverage, not exact equality of category counts. Table 2 reports 32, 55, 44, 56, and 48 instances per level. The difference between a task type, a configured instance, an underlying workflow, and a curriculum is essential to understanding the counts.

## 7.3 Agent configuration

[A] The closed-model baselines are gpt-3.5-turbo-1106 and gpt-4o-2024-05-13, including GPT-4o with screenshots and set-of-marks. Open-model baselines are meta-llama-3-70B-instruct and open-mixtral-8x22b, served through Hugging Face Text Generation Inference on four A100 graphics processing units. The supplied material does not specify GPU memory capacity, library versions, sampling temperature, or a complete inference-cost accounting. Sources: pp. 7, 18.

[A] Observations include the goal, AXTree, focused element, previous-action error, and clickable/visible properties. The vision agent also receives a marked screenshot. On WorkArena and WebArena, only AXTree is used because HTML is too large; MiniWoB uses both. Previous actions and generated thoughts are reinserted into the prompt as a simple memory mechanism. The model emits a single next action. A generic example explains output formatting; task-specific demonstrations are not provided in this baseline design. Source: p. 18 and footnote 7.

[A] The allowed action families are chat messages, infeasibility reporting, and interactions with bid-identified elements. A parser can re-prompt up to four times after formatting errors. Effective prompt limits are 40K tokens for GPT-4o, 15K for GPT-3.5, 8K for Llama3, and 32K for Mixtral. HTML/AXTree content is progressively truncated from the end when needed. These limits differ from the model context capacities listed in Appendix B: 128K, 16K, 8K, and 64K respectively. Source: p. 18.

## 7.4 Human study and evaluation

[A] Fifteen unpaid, consenting volunteers were recruited from ServiceNow research and local academic institutions. They watched a 15-minute presentation and spent 15 minutes exploring the platform, then individually attempted up to seven tasks without discussing them. The human curriculum contains 49 configured tasks at both levels, giving 98 instances. The BrowserGym-like interface adds a movable human console with Validate and Give up controls and automatic completion checking. Participants see whether a task is incomplete or solved, rather than detailed corrective feedback. Sources: pp. 8, 13–17.

[A] The main metric is binary validated task success, aggregated as success rate in percent with standard error. The work does not report a formal significance-test procedure, confidence intervals, or error-category frequencies. Time to resolution was recorded for humans according to the protocol, but no aggregate completion-time results are supplied. The exact human task list and evaluation software are referenced in the repository, which was not reviewed.

## 8. Experiments / Analyses

## X1 — Oracle action-length characterization

[A/B] Figure 4b compares oracle action counts for 470 L2/L3 curriculum instances against 33 L1 tasks at five seeds. The horizontal axis is number of actions; the vertical axis is count. Skill-colored distributions show many tasks at shorter lengths and a long tail toward roughly 130–140 actions. Exact histogram bin counts are not labeled. The authors use this characterization to justify a 50-step agent budget for most tasks. Sources: pp. 4, 7. [D] An oracle is an efficient coded solution; its length does not measure how many exploratory steps a model will require.

## X2 — Agent benchmark evaluation

[A] Five agent variants are evaluated on 235 L2 and 235 L3 instances: GPT-3.5, GPT-4o, GPT-4o-v, Llama3, and Mixtral. The manipulated conditions include model choice, input modality for GPT-4o, and task presentation level. The outcome is validated success rate. Every variant gets 0.0 ± 0.0% on L3. L2 totals are 0.0 ± 0.0%, 3.0 ± 1.1%, 3.8 ± 1.3%, 0.0 ± 0.0%, and 0.0 ± 0.0%, respectively. Source: p. 8, Table 2.

[A] The successful L2 categories are concentrated: both GPT-4o variants obtain 14.6 ± 5.1% on 48 memorization instances; only GPT-4o-v obtains 3.6 ± 2.5% on 56 retrieval instances. All other L2 category entries are zero. The prior-benchmark rows are taken from earlier work, not newly executed comparisons established by this report. The agents face a 50-step cap and model-specific context budgets. Sources: pp. 7–8.

## X3 — Human feasibility and matched-subset comparison

[A] Humans solve the smaller 98-instance curriculum with reported 93.9% overall success. Table 2 separately lists 93.9 ± 3.4% for L2 and L3 human rows. GPT-4o obtains 2.1 ± 2.0% on the L2 human-subset row and 0.0 ± 0.0% on L3. The prose reports a human-versus-GPT-4o comparison of 93.9% versus 2.1%, but the table does not clearly support reading 2.1% as pooled over both levels. Source: p. 8, Table 2 and §4.4.

[A] Human category results vary despite high totals: L3 contextual understanding and planning are each 87.5 ± 11.7%; L3 memorization is 91.7 ± 8.0%; L3 retrieval and data-driven decision-making are 100.0 ± 0.0%. L2 data-driven decision-making is 84.6 ± 10.0%; memorization is 91.7 ± 8.0%; the other L2 categories are 100.0 ± 0.0%. The agent-curriculum counts printed at left are not human-category denominators. Human familiarity, training, feedback controls, and absence of an action cap qualify the comparison.

## X4 — Qualitative error analysis

[A] The authors inspect traces from GPT-4o and Llama3 to identify information-retrieval, exploration, hallucination, goal-understanding, and action-consequence errors. Examples include dropping an iframe prefix, clicking an already sorted column, failing to expand menus or switch tabs, inventing unavailable calls, ordering a case instead of a tablet, treating instructions in a ticket as completed work, overwriting a serial number, and repeating an ineffective click. Sources: pp. 8–9, 47–55.

[D] This is mechanism-oriented qualitative evidence, not a statistical decomposition of failure causes. No coded sample size, annotation reliability, prevalence distribution, or causal intervention is supplied. The examples establish that these failures occurred; they do not establish which is most frequent or how much each explains the overall success rate.

## X5 — Context-size ablation

[A] Appendix G.3 varies a Llama3-based agent's context on WorkArena L1: 130k gives 17.9 ± 2.1%, 64k gives 14.8 ± 2.0%, 32k gives 17.6 ± 2.1%, and 13k gives 18.2 ± 2.1%. The authors describe performance as similar and caution that this should not be expected for more complex tasks. Source: p. 56, Table 3.

[D] This is not an L2/L3 memory ablation. The exact model/configuration responsible for the 130k setting is not reconciled with Appendix B's 8K Llama3 description. No equivalence test is reported; overlapping uncertainty and similar point estimates should not be promoted into proof that context never matters.

# 9. Results and numerical interpretation

[A] The strongest result is the L3 floor: all five tested variants have zero observed successes under the reported curriculum and execution limits. Zero observed success is a sample result, not proof that the underlying probability of success is exactly zero. Source: p. 8, Table 2.

[A/C] GPT-4o-v improves the L2 point estimate from GPT-4o's 3.0% to 3.8%. The analyst-derived absolute difference is 3.8 − 3.0 = **0.8 percentage points**. Because the paper does not supply a corresponding significance test, the evidence supports a limited observation that vision enabled some chart-retrieval successes, rather than a firm general advantage across task families. Sources: pp. 7–8.

[A] Compared with L2/L3, the same table reports substantially higher L1 and MiniWoB success for several variants. For GPT-4o, the displayed figures are 42.7 ± 2.7% on L1, 71.3 ± 1.5% on MiniWoB, and 23.5 ± 1.5% on WebArena. These support the authors' argument that the new workflows are challenging, but different task populations and imported prior results limit a tightly controlled causal interpretation. Source: Table 2.

[A/D] Human success demonstrates feasibility for the sampled participants and sampled tasks. It does not establish that every one of the 682 task types is easy for arbitrary users. The paper's validator/oracle design gives additional constructive evidence of intended solvability, while intentionally infeasible tasks are 'solved' through correctly recognizing infeasibility rather than completing impossible actions.

[A] Qualitative results reveal a gap between verbal progress claims and actual software state. A model can claim it correctly filled a serial-number field after overwriting that field; another can close a ticket because its description looks like completed work. Sources: pp. 52–54. [D] These are particularly relevant to security-oriented reasoning because action execution can affect records, yet the study establishes ordinary task failure rather than adversarial exploitation.

# 10. Figure-by-figure interpretation

Unless specified below, the figures are screenshots or workflow diagrams rather than quantitative plots: they have no numerical axes, error bars, or statistical markers. Small example names, identifiers, and arbitrary field strings are intentionally compressed; they are task-instance details rather than estimated benchmark outcomes.

### Figure 1 — Restocking workflow, p. 2

[B] Four numbered interface panels show receiving a ticket, reading inventory from a chart, ordering from the service catalog, and closing the ticket. The sequence makes the composition concrete: information obtained in one interface must guide an action elsewhere. The chart's exact bar values are too small for confident transcription. [A] The caption specifies restocking below-threshold items to a minimum stock quantity. The figure illustrates a task; it does not report an evaluated trajectory's success rate.

### Figure 2 — WorkArena and BrowserGym, p. 3

[B] Panel a groups six interface components: workspace, list, form, dashboard, knowledge base, and service catalog. Panel b places a browser between a user-facing goal and an agent, with observations flowing to the agent and actions back to the browser. HTML, AXTree, and screenshot represent observation modes; code-, coordinate-, and identifier-based examples illustrate general action options. [A] The diagram is reproduced from prior work. The current baselines use only the subset specified in §4.2 and Appendix B.

### Figure 3 — Environment and validation, p. 3

[B] A web agent has a perception/action loop with the ServiceNow frontend. Setup/teardown and validation connect to the backend, while validation also reaches the frontend. [A] Backend REST and frontend JavaScript inspect database and page state. The distinction explains why a ticket appearing closed is not automatically equivalent to successful completion of its underlying work.

### Figure 4 — Skill distribution and oracle lengths, p. 4

[B] Panel a is a pie chart with labeled counts: planning/problem solving 132, contextual understanding 104, information retrieval 78, data-driven decision-making/reasoning 312, and sophisticated memorization 56. These are exact visible labels, not estimates. Panel b uses number of actions on a linear horizontal axis from 0 to about 140 and count on a linear vertical axis extending above 100. The legend colors encode five skill groups plus L1. The distribution is concentrated toward fewer actions with a long right tail. Exact unlabeled bin heights are not inferred. The caption distinguishes all 682 task types in panel a from 470 L2/L3 instances and 33 × 5 L1 instances in panel b.

### Figure 5 — Consent form, p. 14

[B] A multi-panel consent form is shown. [A] The caption says all evaluators signed it. This supports documented consent, but its tiny embedded paragraphs cannot all be independently transcribed from the image. Recruitment, compensation, and procedure are taken from readable surrounding text, not guessed from the form.

### Figure 6 — Participant demographics, p. 15

[B] Eleven small charts cover gender, country, main language, occupation, daily computer use, programming comfort, age, education, ServiceNow familiarity, ServiceNow employment, and prior evaluation participation. Each is based on 15 responses. Clearly readable examples include 80% male/20% female; countries Canada 9, France 1, India 5; English main language 40% yes/60% no; programming comfort 86.7% yes; first-time ServiceNow use 46.7%; and ServiceNow employment 73.3%. The surrounding discussion confirms 11/15 employed there and 86.7% using the product at most a few times monthly. Remaining small demographic slices are compressed rather than treated as necessary explanatory variables. These charts describe the sample; they do not demonstrate representativeness.

### Figure 7 — Human training slides, p. 16

[B] A grid of presentation slides introduces agents, the browser, chat, evaluation controls, lists, forms, dashboards, knowledge bases, and catalog use. The visual grid establishes broad interface-oriented training content. Full text within every thumbnail is unreadable at this scale. [A] The talk lasted 15 minutes and is followed by exploration. The figure is not evidence that participants received a worked solution for every task.

### Figure 8 — Human evaluation platform, p. 16

[B] Chat appears on the left, the ServiceNow browser on the right, and a movable evaluation console at bottom right. [A] Validate, Give up, and auto-validation support completion checking. The console is an explicit procedural difference from the agent interface, despite otherwise matched browser access.

### Figure 9 — Example agent prompt, p. 19

[B] A long boxed prompt contains instructions, an L1 laptop-ordering goal, AXTree, focused element, interaction history, action descriptions, and a generic response-format example. Its example goal orders six Sales Laptops with specified options. These numbers are illustrative input values, not performance results. Ellipses explicitly omit portions. Embedded instructions are analyzed as paper content and were not followed as instructions for this report.

### Figure 10 — Set-of-marks screenshot, p. 20

[B] Boxes and element identifiers overlay catalog regions. The caption connects a252 and a261 to the textual observation in Figure 9. This illustrates grounding the same page element across text, image, and action target. Dense overlapping labels limit exhaustive visual transcription.

### Figure 11 — Workload balancing, p. 21

[B] Panel a supplies an explicit L2 instruction list; panel b gives an L3 ticket. [A] The task redistributes problems from heavily loaded users to less loaded users; three task variants occur per level. This figure connects chart/report retrieval to a record reassignment.

### Figure 12 — Work assignment, p. 22

[B] Paired L2/L3 panels show assignment based on category experts and priority. [A] Six variants occur per level. The protocol in Figure 24 clarifies role selection. Exact personal names and incident identifiers are example configuration values, deliberately compressed.

### Figure 13 — Scheduling requests, p. 22

[B] Explicit instructions and a ticket describe scheduling change requests within a permitted interval. Risk-dependent durations and impact order impose constraints. [A] There are 48 scheduling variants per level. The concrete dates are illustrative; this is not a scheduling-runtime experiment.

### Figure 14 — Deduplicating problems, p. 22

[B] Paired panels show filtering related problem statements and marking duplicates. [A] Nine variants per level incorporate priority-sensitive handling. Figure 26 supplies the detailed rules; simply deleting every duplicate would not accurately describe the task.

### Figure 15 — Dashboard retrieval, p. 23

[B] Paired goals connect a chart-derived value to ordering low-stock items. [A] Twenty-nine variants per level use values or labels from bar/pie charts for follow-up actions. The task tests the consequence of retrieval as well as reading itself.

### Figure 16 — List/form retrieval, p. 23

[B] The example asks for a named user's laptop warranty expiration, using an asset list and field lookup. [A] Ten variants per level belong to this family. The final answer can be a chat response rather than a database mutation.

### Figure 17 — Expense management, p. 24

[B] The L2 example filters expenses and keeps the most expensive among duplicate descriptions; the L3 counterpart conveys the assignment through a ticket. [A] Twelve variants per level apply date, amount, or other hierarchical rules. Figure 29 shows that the full protocol is richer than this single example.

### Figure 18 — Investment selection, p. 24

[B] The paired panels describe maximizing investment returns under a budget, including removal of unselected entries in the illustrated variant. [A] Fifty-seven variants per level can require IDs, total return, or deletion actions. The displayed budget is an example task input, not a universal benchmark constant.

### Figure 19 — Chart-based computation, p. 25

[B] L2/L3 examples require using employee-performance statistics to identify below-median workers and create subsequent records. [A] Eighty-seven variants per level involve calculations over plots. The figure illustrates reasoning followed by action; it supplies no measured numerical accuracy for arithmetic alone.

### Figure 20 — Navigation plus operation, p. 25

[B] The example requires reaching the incidents list and sorting by category ascending. [A] Twenty-six navigation-and-do variants per level combine destination memory with action details. Success requires both navigation and the final operation.

### Figure 21 — Offboarding, p. 26

[B] Paired panels show a named user, clearing the user's asset assignment, and deleting the user record. These operations align with Figure 32 but differ from the nearby §C.4.2 prose description of deleting hardware and marking the user inactive. The inconsistency is substantive because the resulting database states differ.

### Figure 22 — Infeasible task, p. 26

[B] The example includes an unavailable filtering requirement among otherwise ordinary instructions. [A] The benchmark checks recognition of impossibility, sometimes requiring a reason. This is not a demonstration of malicious instructions or a measured safety refusal.

### Figure 23 — Workload-balancing protocol, p. 27

[B] The knowledge-base screenshot directs the worker to identify the busiest and least busy users for hashtag-associated problems, choose a low-priority problem, and reassign it. The visual's priority-5 example differs from the priority-4 condition visible in Figure 11's L2 instance; the supplied work does not explain that specific difference. The general transfer-from-busy-to-less-busy workflow remains clear.

### Figure 24 — Assignment protocol, p. 28

[B] The article instructs locating an incident, reading category and priority, and selecting the assigned role: priority 1 Critical maps to expert, priority 3 Moderate to supporter, and priority 5 Planning to planner. These exact labeled values are rules, not experimental outcomes. Category expertise and priority jointly determine the action.

### Figure 25 — Scheduling protocol, p. 29

[B] The rules require fitting requests within a time window, avoiding overlap, ordering higher-impact requests first, limiting gaps to one day or one hour for tight schedules, and assigning durations of three days for high risk, two for moderate, and one for low risk. Planned dates are used; actual dates are left empty. These constraints explain the planning burden.

### Figure 26 — Problem-deduplication protocol, p. 30

[B] Identify matching problem statements, retain the higher-priority problem when priorities differ, and use Mark Duplicate on the other. Priority 1 is highest and 5 lowest. Equal-priority duplicates permit either choice. A special rule changes the description to Duplicate when a critical-priority problem is marked duplicate. This exception materially changes correct execution.

### Figure 27 — Dashboard retrieval protocol, p. 31

[B] Locate a chart by hashtag, extract the requested value or statistic, and perform form creation, filtering, or ordering. The text specifies rounding upward to the next highest integer and selecting the greatest value for ambiguous modes. These conventions are benchmark rules; they should not be replaced by an analyst's preferred arithmetic convention.

### Figure 28 — Warranty protocol, p. 32

[B] Find the laptop through Assigned to in the hardware asset list and read its warranty expiration on the detail page. This compact article illustrates lookup across records. No statistical plot is present.

### Figure 29 — Expense protocol, p. 33

[B] Filter by hashtag and duplicate short description. Prefer entries linked to tasks; if all or none are linked, keep the oldest; if dates match, keep the most expensive; if costs also match, any entry may be retained. This is a hierarchy of decisions rather than a single maximum-cost rule.

### Figure 30 — Investment protocol, p. 34

[B] Returns are in descriptions and costs in Amount fields. Select within budget, then report total return, selected record numbers, both, or delete unselected investments according to the task. The screenshot demonstrates why retrieving one field is insufficient: multiple records and an objective must be combined.

### Figure 31 — Onboarding protocol, p. 35

[B] Create and save a user account, order an Apple MacBook Pro 15-inch laptop, create a hardware asset, and assign it to that user. This article connects identity creation, purchasing, and asset records. The model must preserve the same user identity across steps.

### Figure 32 — Offboarding protocol, p. 36

[B] Find the user's laptop, erase Assigned to, then locate and delete the user account. This directly visible protocol supports unassignment plus account deletion. It does not say to delete the hardware record, reinforcing the unresolved discrepancy with §C.4.2.

### Figure 33 — Curriculum configuration, p. 38

[B] A code screenshot lists skill categories, task buckets, weights, and seed counts. Readable seed-count values are 2 for planning, 7 for retrieval, 1 for data-driven reasoning, 8 for memory, and 4 for infeasibility. The structure is visually clear; every long constant name is not transcribed. Table 2 and Appendix D provide the more reliable final curriculum counts.

### Figures 34–43 — Ten application themes, pp. 39–44

[B] Each figure has a landing-page panel and list-view panel. Figure 34 is Astranova; 35 Charlie's Cookies; 36 Great Pasta; 37 Mighty Capital; 38 Skyward; 39 SpeedyTires; 40 TurboBots; 41 UltraShoes; 42 VitaSphere; 43 WorkArena. Colors, header branding, logos, and list-striping vary while the basic layout is similar. These ten figures are individually accounted for but grouped because their methodological meaning repeats. They demonstrate cosmetic/interface diversity within ServiceNow, not ten independent software platforms. No per-theme performance results are reported.

### Figure 44 — Trace extraction, p. 45

[B] Screenshots along the top connect through a lower sequence of BrowserGym observations, oracle actions, catalog navigation, ordering, and completion. Arrows show repeated observation/action recording. [A] Screenshot, AXTree, Document Object Model, optional marks, and Playwright code are saved together. This is the mechanism for generating demonstration data, not an experiment showing fine-tuning gains.

### Figure 45 — Composed onboarding, p. 45

[B] Three connected stages create a user, order a laptop, and assign it to the user. Small boxes preserve cross-step data such as identity and model. [A] Individual stages can be validated sequentially. The diagram abstracts from the detailed forms.

### Figure 46 — Extended onboarding, p. 46

[B] A fourth stage creates a new task assigned to the user. This demonstrates extending the workflow by appending a task with its own validation. No result shows whether this extension improves agent performance or changes evaluation difficulty by a measured amount.

### Figure 47 — Folded and unfolded menus, p. 48

[B] Panel a hides Asset submenu links; panel b exposes them after expansion. [A] Hidden links are absent from AXTree, requiring search or expansion. This is a concrete observability problem: a missing target may require an exploratory action rather than repeated attempts to click it.

### Figures 48–49 — Wrong form field, p. 50

[B] Two screenshots show a change-request form before and after text intended for Close notes is placed in another field. [A] Close notes is on a different tab, and the agent submits the incorrect form believing it is finished. The pair supports the progression from incomplete exploration to overwriting to false completion assessment.

### Figure 50 — L3 ticket misunderstanding, p. 52

[B] A ticket describes a hardware-asset task. [A] The agent mistakes the populated assignment description for evidence that the underlying work is done, then attempts to close the ticket. This is an instruction-versus-state confusion; no adversarial ticket is introduced.

### Figures 51–52 — Serial-number overwrite, p. 54

[B] The first screenshot contains the intended serial number; the second contains IT in that field. [A] IT belongs in Cost center on another tab. The agent's accompanying statement incorrectly preserves its belief that the serial number remains correct. These paired images directly corroborate the prose error account.

### Figure 53 — Ineffective repeated action, p. 55

[B] The catalog page shows the context for a navigation loop. [A] The trace repeatedly clicks search element 113 without typing or changing the page until the episode ends. The still image alone cannot establish repetition; that temporal claim comes from the supplied trace description on p. 54.

# 11. Table-by-table interpretation

## Table 1 — Benchmark design comparison, p. 5

[A] Columns compare MiniWoB, WebArena, WorkArena L1, and WorkArena++. Rows cover task count, environment, task nature, required abilities, and backend. Counts are 125, 190, 33, and 682. MiniWoB uses custom interfaces and basic interactions; WebArena uses diverse realistic websites; WorkArena uses basic ServiceNow tasks; WorkArena++ uses complex enterprise workflows. Backend descriptions distinguish Selenium, Docker-based setup, and BrowserGym-based access.

[D] This is a descriptive positioning table. Its ability labels do not constitute isolated measurements of each cognitive skill. The WebArena count of 190 here and 812 instances in Table 2 are different reported evaluation quantities; the supplied work does not fully derive their relationship. Do not silently replace one with the other.

## Table 2 — Success rate and standard error, p. 8

[A] Units are percentages. The left block contains the full agent curriculum; the right block contains the human subset and GPT-4o evaluated on that subset. Each L2/L3 agent curriculum has 235 instances. Category counts are 32 contextual, 55 data-driven, 44 planning, 56 retrieval, and 48 memory. The human counts are not those left-column category counts.

| Agent | L3 | L2 | L1 | MiniWoB | WebArena |
|---|---|---|---|---|---|
| GPT-3.5 | 0.0 ± 0.0 | 0.0 ± 0.0 | 6.1 ± 1.3 | 43.4 ± 1.6 | 6.7 ± 0.9 |
| GPT-4o | 0.0 ± 0.0 | 3.0 ± 1.1 | 42.7 ± 2.7 | 71.3 ± 1.5 | 23.5 ± 1.5 |
| GPT-4o-v | 0.0 ± 0.0 | 3.8 ± 1.3 | 41.8 ± 2.7 | 72.5 ± 1.5 | 24.0 ± 1.5 |
| Llama3 | 0.0 ± 0.0 | 0.0 ± 0.0 | 17.9 ± 2.1 | 68.2 ± 1.2 | 11.0 ± 1.1 |
| Mixtral | 0.0 ± 0.0 | 0.0 ± 0.0 | 12.4 ± 1.8 | 62.4 ± 1.6 | 12.6 ± 0.5 |

[A] L1 uses 33 × 10 seeds; MiniWoB uses 125 × 5 seeds; WebArena reports 812 instances. Human comparison values imported for MiniWoB and WebArena are 93.5% and 78.2%, without displayed standard errors. Dashes mean no corresponding value is reported, not zero success. Boldface identifies overall benchmark rows, not statistical significance. All L3 agents tie at the floor; GPT-4o-v has the largest L2 point estimate. The supplied work does not describe a test supporting each rank difference.

## Table 3 — Context ablation, p. 56

[A] The four columns are 130k, 64k, 32k, and 13k tokens, with L1 success rates 17.9 ± 2.1%, 14.8 ± 2.0%, 17.6 ± 2.1%, and 18.2 ± 2.1%. The largest point estimate is at 13k and smallest at 64k, but the table supports neither monotonic improvement nor a causal claim that shorter context is better. The authors explicitly limit the lesson to this simpler setting and caution against transferring it to more complex tasks.

## 12. Diagram / Architecture

The architecture has three distinct paths. **Interaction:** the agent receives a goal and page observation, generates one allowed action, and changes the browser/frontend. **Evaluation:** validators inspect the current page and database through separate APIs. **Lifecycle:** setup and teardown create controlled task state and remove the task user. Figure 3 separates these paths; Figures 2, 9, and 10 explain the observation/action interface. [D] Keeping these paths distinct prevents confusing a model's self-report, a frontend label, and a validated backend outcome.

[A] The execution loop repeatedly reinserts history and current observations into the prompt, parses the output, optionally retries malformed output, and executes the action. Page errors then become information for the next step. This feedback is incomplete when an incorrect action is valid but semantically wrong: clicking a search field repeatedly can generate no error while making no progress. Sources: pp. 18, 54.

[A] Trace generation follows a related but different loop: a coded oracle chooses actions; BrowserGym records observations and intercepts automation code. This can provide ground-truth demonstrations. Workflow composition chains atomic oracles and checks either sequential subtasks or a global database condition. Figures 44–46 illustrate extension without requiring a new end-to-end solution from scratch.

[D] From a security-analysis perspective, the frontend supplies information and the same agent can cause state changes. This identifies a place where a future threat model would need to specify which content is trusted and which actions require safeguards. The present paper does not define or test such a policy, so no trust-boundary defense effectiveness can be inferred.

# 13. Equations and mathematical concepts

No numbered equation or theorem is necessary to explain the contribution. The key mathematical objects are counts, constrained selection, sampling, and success-rate summaries.

**Task arithmetic [A/C].** The paper explicitly gives 2 × 341 = 682: two presentation levels times 341 workflows. The analyst check of the main-text categories is 66 + 39 + 156 + 28 + 52 = 341. If the Appendix C heading's 29 replaces 28, the sum becomes 342 and doubling gives 684. This calculation exposes an unresolved count discrepancy; it does not determine which implementation is correct.

**Success metric [A/C].** Validators return rᵢ ∈ {0,1}. A reproducible analyst expression for the reported success-rate concept is SR = 100 × (Σᵢ rᵢ)/n, where n is the number of evaluated instances. This expression is explanatory, not a numbered author equation. The paper labels uncertainty as standard error but does not provide its exact estimation formula or an adjustment for participant/task clustering. No such formula is silently supplied here.

**Investment problem [A/D].** The authors describe maximizing return within a budget as a small knapsack instance. An analyst formalization is maximize Σᵢ vᵢxᵢ subject to Σᵢ cᵢxᵢ ≤ B and xᵢ ∈ {0,1}, where vᵢ is return, cᵢ cost, B budget, and xᵢ selection. This compact identity translates the described objective; the paper does not display this formulation or establish a solver's optimality proof.

**Algorithm 1 [A].** CATEGORIES holds buckets, sampling weights, and num_seeds. The meta-seed m initializes a random generator. Each category receives task seeds; each seed initializes a bucket generator; tasks are sampled without replacement according to the bucket's requested count; each selected task and seed is appended to tuple T. T is the returned curriculum. Here 'weight' functions as a specified within-bucket sample count in the pseudocode, rather than an unexplained continuous optimization coefficient. Source: p. 37.

**Chart computations [A/B].** Mean, median, and mode are task operations, not separately evaluated mathematical theories. The visible protocol specifies upward rounding and a greatest-value rule for ambiguous modes. The supplied work gives no independent arithmetic-accuracy breakdown. Source: Figure 27, p. 31.

## 14. Interpretation and Discussion

[A] The authors interpret the low agent scores alongside high human scores as evidence of a useful benchmark gap: the workflows are feasible but challenging for these baselines. The error examples suggest problems extending beyond button manipulation to goal understanding, exploration, reasoning, and state assessment. [D] Because the analysis is qualitative and multiple factors vary, the paper does not isolate reasoning capability from observation truncation, interface grounding, prompt design, and action budgets.

The following cross-checks remain unresolved:

| Issue | First report | Other report | Assessment |
|---|---|---|---|
| Memorization task count | 28 × 2, p. 6; 56 in Fig. 4 | 29 × 2, pp. 13 and 25 heading | Unresolved; listed subfamilies 26 + 2 support 28 |
| Offboarding operation | Delete assigned hardware and mark user inactive, p. 25 | Clear asset assignment and delete user, Figs. 21/32, pp. 26/36 | Different state changes; cannot reconcile |
| Llama3 context | 8K capacity/effective limit, p. 18 | 130k full-context ablation, p. 56 | Exact ablation configuration unexplained |
| Human-subset GPT-4o total | Prose contrasts 93.9% with 2.1%, p. 8 | Table gives 2.1% L2, 0.0% L3 | Do not treat 2.1% as unambiguous pooled result |
| Skill uniformity | Uniform sampling language, p. 7 | Category counts range 32–56, Table 2 | Balanced intent, not equal final counts |
| Work assignment terminology | Problems, p. 21 | Incidents in Figs. 12/24 | Terminological mismatch in examples |
| List/form retrieval name | §C.2.2 | Its prose calls the ten tasks dashboard retrieval, p. 23 | Likely labeling inconsistency; not silently corrected |
| Workload priority example | Priority 4 in Fig. 11 | Priority 5 in Fig. 23 protocol | Example/protocol difference unexplained |

[A] Appendix G argues transfer is plausible because lists, forms, and dashboards are common and many failures concern general planning or goals. [D] These are reasoned generalization arguments, not empirical transfer results. The benchmark's single-platform design remains an external-validity boundary.

[D] For security, the most defensible conclusion is that reliable agency requires maintaining the relationship between instruction, observation, action target, and actual state. WorkArena++ documents failures in that relationship. It does not establish how attackers exploit them, whether malicious inputs increase their frequency, or whether a standalone LLM would be more resistant on a matched task.

# 15. Contributions and novelty

| Contribution category | Author-reported contribution | Qualification |
|---|---|---|
| Benchmark | 682 L2/L3 tasks representing 341 workflows | Count discrepancy in memorization heading retained |
| Conceptual | Evaluate combinations of planning, reasoning, retrieval, memory, and infeasibility recognition | Skill names are design categories, not isolated latent measurements |
| Systems | BrowserGym integration, remote ServiceNow instances, lifecycle and validation mechanisms | Built upon WorkArena infrastructure |
| Evaluation methodology | Seeded curriculum with bucketed skill coverage | Exact configuration supplied as code screenshot/repository reference |
| Implementation | Ten brands, standardized installer, per-task user isolation | No measured per-theme robustness or adversarial isolation test |
| Data generation | Compose coded oracles and extract observation/action traces | No training-benefit experiment in supplied work |
| Empirical | Baseline-agent results, human comparison, error cases, context ablation | Historical models and specific budgets; no security comparison |

[A] The main novelty claim is adding realistic compositional workflows requiring more complex skills than atomic tasks. [D] The supplied work supports a benchmark and infrastructure contribution more strongly than an algorithmic advance in agent reasoning: the evaluated agent largely follows a prior design.

# 16. Limitations

## Authors' stated limitations

[A] The task set does not exhaustively cover knowledge-work tasks or personas; thousands more tasks would be needed for broad coverage. Safety and robustness against malicious behaviors are not assessed. Tasks do not interact with external software. Additional open/closed models and very long-context models could have been included. Visual diversity could be expanded. Sources: pp. 6, 10.

[A] The human sample is small and not representative: 11/15 have ServiceNow employment history, all have undergraduate degrees, and many have advanced degrees. The authors discuss possible UI learning, a general announcement about saving closed tickets with Update, and the absence of an explicit human action cap. They argue that these factors do not explain the enormous gap, but the study does not experimentally remove them. Sources: pp. 14–17.

[A] The authors caution that the L1 context-size result should not be generalized to more complex tasks. They acknowledge that adding environments would improve workflow representativeness. Sources: pp. 55–56.

## Additional evidence-based analyst observations

[D] A 50-step cap can disadvantage exploratory agents even when an oracle finishes within 50 actions. Different effective context lengths complicate attributing model differences solely to reasoning quality. Truncating from the end may remove task-relevant page information. The zero-success L3 floor limits discrimination among the tested agents. Qualitative error cases do not reveal prevalence. No adversarial task, standalone-model comparison, defense evaluation, or security metric supports a comparative vulnerability claim.

[D] Internal inconsistencies prevent exact reconciliation of some task counts and operations. Repository-dependent details were not inspected, and no claim of executable reproducibility is made. None of these observations invalidates the displayed results; each narrows what can be concluded from them.

# 17. Threats to validity

These validity labels are analyst classifications, not headings used by the authors.

**Internal validity [D].** Model, modality, context capacity, prompt budget, and task difficulty are not all independently controlled. The vision comparison is closer to a paired design, but the paper supplies no detailed statistical test. Human training, console functions, public announcement, and action-budget differences complicate causal attribution of the human-agent gap.

**Construct validity [D].** End-to-end validated success combines reading, navigation, planning, memory, grounding, and execution. A category labeled reasoning does not establish that a failure is purely mathematical reasoning. Conversely, correctly declaring infeasibility is a benchmark success even though no requested database modification occurs. Task completion is not a measure of adversarial security.

**External and ecological validity [A/D].** ServiceNow offers realistic enterprise interfaces, but the sample covers one platform with synthetic configured tasks and fictitious branding. Human volunteers are not a representative workforce sample. The authors' transfer arguments are plausible interpretations rather than demonstrated cross-platform effects.

**Statistical conclusion validity [D].** Standard errors are displayed, but confidence intervals, test procedures, repeated-agent-run details, and dependence adjustments are not fully described. Zero standard error at observed zero or perfect success should not be interpreted as absence of uncertainty about future populations. Sparse human categories have large reported errors.

**Reproducibility [A/D].** Seeds, model identifiers, prompts, algorithm, and repository references help reproduction. However, the exact code revision, complete software versions, all decoding settings, and reconciliation of the context ablation are unavailable here. No replication was executed.

# 18. Future work and open questions

## A. Explicit author proposals

[A] Add ServiceNow tasks, especially safety and cybersecurity tasks; develop a hidden competition test set; use generated traces to train more robust agents; increase visual diversity; add longer and more complex workflows; draw occupational inspiration from O*NET; include collaboration and delegation; and interact with multiple external applications. Sources: pp. 6, 10, 55–56.

[A] The authors suggest a possible L4 involving multiple environments, such as replacing the internal knowledge base with an external one. Delegation could be implemented by executing an oracle for a delegated subtask, with excessive delegation penalized. New atomic tasks require setup, teardown, oracle, and validation functions. These are proposed extensions rather than evaluated capabilities. Sources: pp. 55–56.

## B. Additional analyst open questions

[D] How much failure is attributable to observation truncation versus planning? Would stronger state verification prevent false completion? How do results change with equalized action budgets or a larger representative human sample? Can the task categories discriminate stronger agents beyond the current floor? Would oracle traces improve performance on held-out workflows rather than familiar instances?

[D] For the security research question, a subsequent study would need a defined attacker, specified controllable content, legitimate task objectives, measurable harmful outcomes, and matched standalone-model conditions. This paper leaves open whether its observed goal/state confusions are exploitable, how exposure changes with browser access, and which safeguards reduce risk. These are questions motivated by the paper, not findings reported by it.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used to select language-formatted next actions |
| VLM | Vision-language model receiving visual input as well as text |
| Web agent | Model plus browser observations, action interface, memory/history, and execution loop |
| UI | User interface: visible controls, pages, forms, menus, and lists |
| API | Application programming interface used by software components |
| HTML | HyperText Markup Language representing a web page |
| AXTree | Accessibility tree, a compressed structured page representation |
| DOM | Document Object Model, another structured representation recorded in traces |
| bid | BrowserGym identifier for an actionable or observed page element |
| iframe | Embedded page context whose identifier prefix matters for targeting |
| Set-of-marks | Visual overlay connecting page regions to element identifiers |
| BrowserGym | Framework providing browser observations, actions, chat, and evaluation integration |
| WorkArena L1 | Original atomic enterprise-interface task set |
| L2 | Explicit procedural instructions supplied through chat |
| L3 | Assignment supplied through a ticket with knowledge-base guidance |
| Atomic task | Reusable simpler task building block |
| Compositional workflow | Several linked operations forming a larger office-work goal |
| Oracle | Human-coded automation solution used for solving and trace generation |
| Validator | Function checking real task completion and returning 0 or 1 |
| Curriculum | Seeded collection of configured task instances for evaluation |
| Task seed | Random seed controlling one task's concrete configuration |
| Meta-seed m | Seed controlling curriculum construction |
| T | Tuple of selected task/seed pairs in Algorithm 1 |
| SR ± SE | Success rate plus/minus standard error, reported in percent |
| TGI | Text Generation Inference, used to serve open-model baselines |
| REST / JS | Backend interface style / JavaScript frontend mechanisms used for validation |
| Knapsack | Selecting a valuable subset while staying within a limited budget |
| Infeasible task | Request that cannot be completed as specified and must be recognized |
| Zero-shot baseline | Agent without task-specific solved demonstrations in its prompt; generic formatting example remains |

# 20. Key numerical results

All uncertainties below are reported standard errors unless explicitly stated otherwise.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Underlying workflows | 341 | workflows | Same workflows presented at L2/L3 | Author-reported | p. 4, §3.1 |
| New task total | 682 | tasks | 2 × 341 | Author-reported | p. 4 |
| Planning | 66 × 2 | tasks | Across L2/L3 | Author-reported | p. 5 |
| Retrieval | 39 × 2 | tasks | Across L2/L3 | Author-reported | p. 6 |
| Data-driven reasoning | 156 × 2 | tasks | Across L2/L3 | Author-reported | p. 6 |
| Memory | 28 × 2 | tasks | Appendix heading instead says 29 × 2 | Author-reported | pp. 6, 25 |
| Infeasibility/context | 52 × 2 | tasks | Includes declaration/reason variants | Author-reported | p. 6 |
| Agent curriculum | 235 per level | instances | 470 combined | Author-reported | p. 37 |
| Agent category counts | 32, 55, 44, 56, 48 | instances | Context, data, planning, retrieval, memory | Author-reported | p. 8, T2 |
| Agent action cap | 50 | time steps | All baseline agents | Author-reported | p. 7 |
| Parse retries | Up to 4 | retries | Output parsing failure | Author-reported | p. 18 |
| Effective prompt limits | 40K / 15K / 8K / 32K | tokens | GPT-4o / GPT-3.5 / Llama3 / Mixtral | Author-reported | p. 18 |
| Open-model hardware | 4 A100 | GPUs | TGI serving | Author-reported | p. 18 |
| Reserved evaluation meta-seeds | 0–9 | seed identifiers | Other seeds available for tuning | Author-reported | p. 37 |
| Themes | 10 | brands | Randomly sampled per task | Author-reported | p. 6 |
| Human sample | 15 | participants | Unpaid volunteers | Author-reported | pp. 8, 13 |
| Human curriculum | 98 | instances | 49 × 2 levels | Author-reported | p. 14 |
| Human preparation | 15 + 15 | minutes | Presentation + exploration | Author-reported | p. 14 |
| Prior ServiceNow employment | 11/15 | participants | Sample bias | Author-reported | p. 16 |
| First-time users | 46.7 | percent | Human sample self-report | Author-reported | p. 16 |
| All baseline L3 success | 0.0 ± 0.0 | percent | Each of five variants, 235 instances | Author-reported | p. 8, T2 |
| GPT-4o L2 | 3.0 ± 1.1 | percent | Full agent curriculum | Author-reported | p. 8, T2 |
| GPT-4o-v L2 | 3.8 ± 1.3 | percent | Full agent curriculum | Author-reported | p. 8, T2 |
| GPT-4o variants, L2 memory | 14.6 ± 5.1 | percent | Each variant; 48 instances | Author-reported | p. 8, T2 |
| GPT-4o-v L2 retrieval | 3.6 ± 2.5 | percent | 56 instances | Author-reported | p. 8, T2 |
| Human L2 / L3 | 93.9 ± 3.4 each | percent | Human subset, separate level rows | Author-reported | p. 8, T2 |
| GPT-4o human-subset L2 / L3 | 2.1 ± 2.0 / 0.0 ± 0.0 | percent | Separate level rows | Author-reported | p. 8, T2 |
| Vision L2 point difference | 0.8 | percentage points | 3.8 − 3.0 | Analyst-derived | p. 8, T2 |
| L1 context ablation | 17.9 / 14.8 / 17.6 / 18.2 | percent | 130k / 64k / 32k / 13k | Author-reported | p. 56, T3 |
| Figure 4 skill labels | 132 / 104 / 78 / 312 / 56 | tasks | Planning/context/retrieval/data/memory | Visually readable | p. 4, F4a |

No exact numerical result in this report is derived from an unlabeled histogram height. Approximate graphical interpretation is limited to the action-length distribution's broad shape and tail.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| WorkArena++ evaluates compositional enterprise work | 341 workflows × two presentations | Task inventory; F1, F11–F32 | pp. 4–6, 21–36 | Strong design evidence; memory-count typo unresolved |
| L3 adds instruction discovery and integration | Ticket plus knowledge base instead of explicit chat steps | Paired examples | pp. 4–5 | Strong method evidence; not an adversarial condition |
| Tested agents struggle | Near-zero L2 and zero L3 success | T2, X2 | pp. 7–8 | Strong within reported configuration |
| Humans can solve sampled tasks | High success on 98-instance subset | T2, X3, Appendix A | pp. 8, 13–17 | Strong sample evidence; cohort/protocol caveats |
| Vision helps some chart retrieval | Nonzero GPT-4o-v retrieval score versus zero text counterpart | T2 | p. 8 | Limited category evidence; no broad causal proof |
| Self-assessed progress can diverge from state | Wrong-field overwrite and premature closure | F48–F52, X4 | pp. 49–54 | Concrete qualitative examples; prevalence unknown |
| Workflow demonstrations can be generated | Coded oracles with recorded observations/actions | F44–F46 | pp. 45–46 | Mechanism described; no training-gain experiment |
| Context result is limited to simpler L1 tasks | Similar displayed rates across four contexts | T3, X5 | p. 56 | Model/context configuration inconsistency remains |
| Safety robustness is not established | Authors explicitly exclude malicious-behavior assessment | §7 | p. 10 | Strong negative scope evidence |
| Paper informs security through action/state dependencies | Browser observations guide record-changing actions and can be misunderstood | F3, F50–F52 | pp. 3, 52–54 | Analyst inference; no attack or standalone-model comparison |

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to help in an office. Answering 'How do I order a laptop?' is only the beginning. Actually doing the job means finding the right page, choosing the correct laptop, entering the right person's details, saving the order, and checking that everything worked. WorkArena++ creates hundreds of tasks like that inside an enterprise website.

The researchers give AI agents either clear step-by-step messages or a more realistic ticket that requires reading company instructions. The tested agents almost always fail on the harder version, while the human volunteers usually succeed on the smaller set they try. Sometimes the AI clicks the wrong thing, misses a hidden tab, buys the wrong product, or thinks a change happened when it did not.

That matters for security because software actions can change real records. An agent that confuses a description of work with proof that the work is done may make consequential mistakes. But this paper does not test hackers tricking agents, and it does not compare agents against standalone chat models. Its lesson is that these browser agents have important reliability problems. A separate security study would be needed to show exactly how attackers could exploit them and whether browser access makes them more vulnerable.

# Completeness Audit

The denominator is the inventory in §2, expanded to all numbered figures, tables, algorithm, empirical analyses, substantive appendix subsections, explicit questions, contributions, and acknowledged limitations. 'Represented in compressed form' means the substantive role and findings are included while repetitive interface strings or secondary details are condensed. Inspection does not imply executable verification.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract; §1 | Yes, text and image | Yes | Fully represented | Framing, authors, venue, contributions |
| §2.1 BrowserGym | Yes, text and image | Yes | Fully represented | Observations/actions and actual restricted baseline |
| §2.2 WorkArena | Yes, text and image | Yes | Fully represented | Atomic tasks, oracle, validator, hosting |
| §3 introduction; §3.1 | Yes, text and image | Yes | Fully represented | Composition and L2/L3 |
| §3.2 all five categories | Yes, text and image | Yes | Fully represented | Counts, definitions, inconsistency |
| §3.3 all three feature groups | Yes, text and image | Yes | Fully represented | Themes, isolation, extension/traces |
| §§4.1–4.2 | Yes, text and image | Yes | Fully represented | Curriculum/configuration |
| §§4.3–4.4 | Yes, text and image | Yes | Fully represented | Agent/human outcomes and conditions |
| §4.5 | Yes; p. 9 text-only | Yes | Fully represented | Five error families |
| §5 Related Work | Yes, text-only | Yes | Represented in compressed form | Categories and positioning; no independent citation validation |
| §6 Conclusion/Future Work | Yes, text-only | Yes | Fully represented | Benchmark conclusions and proposed safety tasks |
| §7 Limitations/Societal Impacts | Yes, text-only | Yes | Represented in compressed form | Scope limits; societal effects below |
| Acknowledgments | Yes, text-only | Yes | Inspected but deliberately omitted as non-substantive | Personal thanks do not alter methods/results |
| References pp. 10–12 | Yes; pp. 10/12 text-only | Yes | Represented in compressed form | Citations treated as author context, not read works |
| Appendix A.1 Participants | Yes | Yes | Fully represented | Sample, recruitment, consent |
| A.2 Protocol | Yes | Yes | Fully represented | Training, exploration, individual work |
| A.3 Curriculum | Yes | Yes | Fully represented | 49 × 2 instances |
| A.4 Platform | Yes | Yes | Fully represented | Console and completion feedback |
| A.5 Limitations | Yes | Yes | Fully represented | Learning, announcement, cohort, action cap |
| Appendix B all design paragraphs | Yes | Yes | Fully represented | Models, observations, history, retries, tuning, truncation |
| C.1.1–C.1.4 | Yes | Yes | Fully represented | Four planning families and counts |
| C.2.1–C.2.2 | Yes | Yes | Fully represented | Chart and form retrieval |
| C.3.1–C.3.3 | Yes | Yes | Fully represented | Expenses, investments, calculations |
| C.4.1–C.4.2 | Yes | Yes | Fully represented | Navigation/user management; discrepancies |
| C.5 Infeasibility | Yes | Yes | Fully represented | Declaration and reason |
| C.6 protocols | Yes, mainly direct vision | Yes | Represented in compressed form | Every protocol's decision rules included |
| Appendix D | Yes | Yes | Fully represented | Sampling and counts |
| E.1 Themes | Yes, direct vision | Yes | Represented in compressed form | All ten figures named |
| E.2 Traces/composition | Yes | Yes | Fully represented | Mechanism and lack of training evaluation |
| Appendix F all error examples | Yes; pp. 47/51 text-only | Yes | Represented in compressed form | Every error type and substantive example accounted for |
| G.1 Transfer/platform scope | Yes | Yes | Fully represented | Arguments distinguished from experiments |
| G.2 Expansion | Yes | Yes | Fully represented | Longer tasks, collaboration, external software |
| G.3 Context sensitivity | Yes | Yes | Fully represented | Results and model-context uncertainty |
| RQ1 solvability; RQ2 failure causes | Yes | Yes | Fully represented | Human study and qualitative traces |
| RQ3/RQ4 transfer/representativeness | Yes | Yes | Fully represented | Discussion arguments only |
| Formal hypotheses | No formal framework present | Yes | Fully represented | No formal hypotheses invented |
| Human learning-effect hypothesis | Yes | Yes | Fully represented | Not experimentally isolated |
| X1 oracle lengths | Yes | Yes | Represented in compressed form | No invented bin counts |
| X2 agent evaluation | Yes | Yes | Fully represented | All overall baseline values and nonzero L2 categories |
| X3 human comparison | Yes | Yes | Fully represented | All human category values and asymmetries |
| X4 qualitative errors | Yes | Yes | Fully represented | No invented prevalence |
| X5 context ablation | Yes | Yes | Fully represented | Four conditions and uncertainty |
| F1 | Yes, visual | Yes | Fully represented | Restocking sequence |
| F2–F3 | Yes, visual | Yes | Fully represented | Architecture and validation |
| F4a/F4b | Yes, visual | Yes | Fully represented | Exact labels versus approximate distribution |
| F5 | Yes, visual | Yes | Represented in compressed form | Tiny consent text uncertain |
| F6 | Yes, visual | Yes | Represented in compressed form | All question topics; selected clear values |
| F7 | Yes, visual | Yes | Represented in compressed form | Thumbnail slide text partly unreadable |
| F8 | Yes, visual | Yes | Fully represented | Human console |
| F9–F10 | Yes, visual | Yes | Represented in compressed form | Prompt/marks; illustrative strings condensed |
| F11–F14 | Yes, visual | Yes | Fully represented | Each planning family discussed separately |
| F15–F16 | Yes, visual | Yes | Fully represented | Each retrieval family discussed separately |
| F17–F19 | Yes, visual | Yes | Fully represented | Each reasoning family discussed separately |
| F20–F22 | Yes, visual | Yes | Fully represented | Memory, offboarding, infeasibility |
| F23–F32 | Yes, visual | Yes | Represented in compressed form | All ten protocols separately explained |
| F33 | Yes, visual | Yes | Represented in compressed form | Structure and seed counts; long constants condensed |
| F34/F35/F36/F37/F38 | Yes, visual | Yes | Represented in compressed form | Each named in theme group |
| F39/F40/F41/F42/F43 | Yes, visual | Yes | Represented in compressed form | Each named in theme group |
| F44–F46 | Yes, visual | Yes | Fully represented | Trace and workflow diagrams |
| F47 | Yes, visual | Yes | Fully represented | Folded/unfolded menu |
| F48–F49 | Yes, visual | Yes | Fully represented | Wrong-field sequence |
| F50 | Yes, visual | Yes | Fully represented | Ticket/state confusion |
| F51–F52 | Yes, visual | Yes | Fully represented | Serial-number overwrite |
| F53 | Yes, visual | Yes | Fully represented | Still image plus textual temporal evidence |
| T1 | Yes, text and visual | Yes | Fully represented | Design comparison and count distinction |
| T2 | Yes, text and visual | Yes | Fully represented | Baseline, category, human, imported comparison results |
| T3 | Yes, text and visual | Yes | Fully represented | All four estimates and SEs |
| ALG1 | Yes, text and visual | Yes | Fully represented | Inputs, loops, sampling, output |
| Major equations/theorems | None present | Yes | Fully represented | Analyst formulas explicitly labeled |
| Main contributions | Yes | Yes | Fully represented | Seven categories in §15 |
| Author-stated limitations | Yes | Yes | Fully represented | Scope, models, humans, context, visual diversity |
| Supplied supplementary files | None supplied | Not applicable | Missing from supplied material | No claim of supplementary review |
| Repository/wiki/exact implementation | Referenced only | Scope stated | Inaccessible under source boundary | No tools or browsing used |

## Missing or inaccessible material

There are no missing pages in the supplied extracted-text sequence. Visual renderings of pp. 9, 10, 12, 47, and 51 are absent. Full-resolution transcriptions of tiny interface screenshots, every training-slide sentence, and consent-form paragraphs are not available confidently. The code repository, Wiki instructions, exact curricula as executable data, raw execution traces beyond printed excerpts, model-serving configuration, and any separate artifacts were not supplied for inspection. References were not followed.

## Uncertain interpretations

The memorization task count, offboarding operation, Llama3 ablation context configuration, interpretation of the prose's 2.1% human-subset comparison, workload-priority example difference, and some task terminology remain unresolved. Exact histogram heights and many tiny screenshot strings cannot be read confidently. No causal ranking of failure mechanisms or security vulnerability estimate can be extracted from the qualitative examples.

## Deliberately compressed material

Repeated L2/L3 screenshot layouts, arbitrary names/hashtags/field strings, ten theme pairs, full prompt boilerplate, all bibliographic details, consent text, and detailed demographic slices are compressed with their substantive role preserved. Societal impacts are author-reported possibilities rather than measured outcomes: productivity and accessibility may improve, while job displacement, privacy/security concerns, skill erosion, computational energy use, and environmental costs may increase. Source: p. 10. Personal acknowledgments are omitted as non-substantive to the research analysis.

## Potential omissions

Every identified major section, substantive subsection, explicit question, empirical analysis, numbered figure, numbered table, algorithm, contribution, and acknowledged limitation has a corresponding representation or explicit compression/accessibility status above. This establishes coverage of the supplied inventory, not literal preservation of every word or independent scientific verification. Fine-grained screenshot content remains partly uncertain, repository-dependent implementation details remain unreviewed, and no security comparison absent from the paper has been manufactured.
