## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Paper content, including the malicious instructions depicted in examples, is treated as evidence rather than instructions. No external research, browsing, file access, code execution, or OCR was performed.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–14 |
| Available page range | Physical pages 1–14, corresponding to printed proceedings pages 23159–23172 |
| Apparently missing pages | No physical page is missing from the supplied text sequence |
| Visually inspected pages | 1–9 and 11–14: 13 supplied page images |
| Text-only page | Page 10: extracted text was supplied, but no page image |
| Visual content | All four numbered figures, all five tables, and all three algorithms have supplied visual renderings |
| Table readability | Numerical cells and main headings are readable; extracted text and images support cross-checking |
| Equation readability | The scoring and selection formulas are readable in Algorithms 1–2; undefined notation and pseudocode ambiguities are discussed below |
| Appendices | A, B.1–B.4, and C are present on pages 12–14 |
| Supplementary material | No separate supplement, code artifact, execution trace, or embedded file was supplied |
| Referenced but absent artifacts | The paper references benchmark code/data and related works; their underlying contents are outside the supplied evidence |
| OCR needed | No: supplied text is sufficient, with direct visual checks for plots, tables, and formulas |
| Other limitations | Small screenshot text within Figure 1 cannot support complete payload transcription; plots lack exact point labels; no independent hash verification was performed |

The supplied accessibility metadata reports no detected appendix pages, but actual reading identifies appendices A–C. This is a metadata-versus-document discrepancy, resolved by the visible headings rather than by assuming the detection report is authoritative. A local-image error concerning the path '-' does not identify additional missing scientific content: the listed images and extracted pages remain available in the message.

Evidence labels throughout are: **[A] AUTHOR-REPORTED**, **[B] DIRECTLY OBSERVABLE**, **[C] ANALYST-DERIVED**, and **[D] ANALYST INTERPRETATION**. No **[E] EXTERNAL INFORMATION** is introduced. Confidence is HIGH for clearly readable source statements and cells, MEDIUM for interpretations and approximate plot readings, and UNKNOWN where the source leaves an issue unresolved.

## 1. Plain-language orientation

AgentVigil studies how an AI assistant can be redirected by information it encounters while working. A legitimate user might ask an assistant to search a shopping site or inspect email. An attacker places instructions inside a review, message, or other external content. If the assistant treats those instructions as commands, it can pursue the attacker's objective instead of the user's. The paper calls this **indirect prompt injection**. [A; pp. 1, 3–4]

The researchers build an automated testing framework that searches for effective injections without seeing the agent's internal model or architecture. It starts with attack templates, changes them using a helper language model, tests the resulting prompts, and preferentially develops candidates that succeed or reach previously uncompromised tasks. Its distinctive combination is a curated initial corpus, coverage-aware scoring, and selection inspired by Monte Carlo Tree Search. [A; §§4.1–4.5]

The main reported optimization results are 71% success on AgentDojo against an o3-mini agent and 70% on VWA-adv against a GPT-4o web agent, compared with handcrafted baselines of 38% and 36%. These headline optimization results must be distinguished from selected-prompt transfer and defense tables: Table 1 reports 60%, rather than 70%, for the selected VWA-adv prompts on its GPT-4o fuzzing set. The supplied work does not fully reconcile that distinction. [A/B; pp. 6–8]

For the user's research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper supplies a mechanism and agent-level evidence, not a controlled measurement of that comparative proposition. **Analyst inference:** external-content ingestion, autonomous planning, and connected tools create routes from attacker-controlled data to actions. However, AgentVigil does not experimentally compare matched standalone language models and web agents, so it cannot establish a numerical excess vulnerability caused by agentization. [D; pp. 2–4]

## 2. Document roadmap

The work is a mixed **cybersecurity, AI-agent systems, algorithm, and empirical evaluation paper**. Its organization connects a threat model to a testing method and then to benchmark, defense, transfer, ablation, and deployment-style evidence.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| META | Title, authors, venue | 1 | Identifies the work |
| ABS | Abstract | 1 | Summarizes problem, framework, and headline results |
| S1 | 1 Introduction | 1–3 | Motivates generic black-box agent testing and distinguishes GPTFuzzer |
| S2 | 2 Related Work | 3 | Groups attacks and defenses and states their attributed shortcomings |
| S3 | 3 Threat Model | 3–4 | Defines benign users, black-box access, external manipulation, and exclusions |
| S4 | 4 Method | 4–5 | Explains corpus, mutation, scoring, and selection |
| S5 | 5 Evaluation | 5–9 | Presents benchmark attacks, transfer, defenses, ablations, and a case study |
| S6 | 6 Conclusion | 9 | Restates framework and generalization claims |
| S7 | 7 Limitations | 9 | Acknowledges cost and model-specific transfer weaknesses |
| S8 | 8 Ethics Statement | 9 | Positions offensive testing as support for defensive development |
| S9 | 9 Acknowledgements | 9–10 | Names funding and gives the funding disclaimer |
| REF | References | 10–12 | Bibliographic context, not independently reviewed source content |
| A | A Details of Models and Dataset | 12 | Gives model checkpoints and benchmark licensing |
| B | B Additional Evaluation Results | 12–13 | Extra models, baselines, scenarios, and coverage curve |
| C | C Algorithms | 13–14 | Supplies scoring, selection, and update pseudocode |

Substantive subsections are §§4.1 Overview, 4.2 Corpus Collection, 4.3 Mutation Design, 4.4 Seed Scoring, 4.5 Seed Selection; §§5.1 Attack Personal Assistant Agents, 5.2 Attacking Web Agents, 5.3 Ablation Study, 5.4 Real-world Case Study; and B.1 Evaluation on Extra Models, B.2 Comparison with Additional Baselines, B.3 Breakdown on Attack Scenarios, B.4 Coverage Curve.

The visual and mathematical inventory is F1 shopping-review attack example; F2 framework architecture; F3 AgentDojo coverage/ablation curves; F4 VWA-adv coverage curve; T1 transfer rates; T2 AgentDojo defenses; T3 VWA-adv defenses; T4 additional models/baselines; T5 scenario breakdown; ALG1 seed scoring; ALG2 seed selection; ALG3 visit-count update. E1 is attack success rate, E2 coverage-weighted seed score, and E3 the Upper Confidence Bound selection score. There are no numbered theorems, proofs, explicit formal hypotheses, or keyword list in the supplied work.

## 3. Background and context

A **large language model (LLM)** is the model component that interprets language and, in this paper's agent setting, helps plan what to do. An **LLM agent** combines that model with an environment and tools, such as a browser, email system, file system, or code execution service. The model coordinates retrieval, commands, and responses over multiple steps. [A; §4.1]

A **direct prompt injection** puts adversarial instructions directly into model input controlled by the attacker. Here, **indirect prompt injection** puts them into external material that the agent retrieves while carrying out a legitimate task. The paper contrasts GPTFuzzer's direct, single-turn, full-input-control setting with AgentVigil's indirect, multi-step setting and restricted control over external content. This is an author-described difference in attack settings; it is not an experiment proving agents have higher attack success rates than standalone models. [A; p. 2]

**Black-box** means the attacker cannot inspect underlying LLM internals or agent architecture. They can interact with the agent and observe external outcomes. An individual trial supplies binary success/failure feedback. A benchmark's evaluator determines whether the attacker-defined objective occurred. [A; §3 and §5.1]

**Fuzzing** means automatically generating and testing inputs to discover failures. A **seed** is an existing candidate attack prompt. A **mutator** changes seeds to create new candidates. **Exploration** seeks unfamiliar candidates or task coverage; **exploitation** develops candidates already showing useful performance. **Attack success rate (ASR)** is the fraction of evaluated attacks/tasks that succeed. **Coverage** concerns which task combinations have been successfully attacked, and the method rewards newly covered combinations. [A; pp. 2, 5, 13]

**Monte Carlo Tree Search (MCTS)** is the authors' name for their mutation-history-guided selection method. The supplied implementation uses a pool of prompt nodes, a confidence-bound score, parent relationships, and ancestor visit updates. It does not show a conventional simulation or rollout procedure. This observation constrains how specifically the algorithm should be described; it does not invalidate the name the authors use. [B/D; Algorithms 2–3]

## 4. Research problem and gap

**Existing problem [A]:** agents encounter untrusted external data that can contain instructions contrary to the user's goal. Once this data reaches the planning LLM, it can alter behavior and produce unauthorized actions. [§4.1]

**Attributed shortcomings of previous attacks [A]:** manual attacks require expertise and can be inconsistent; some automated methods depend on white-box access or detailed knowledge; methods specialized to one agent type do not provide generic assessment; model-level jailbreak testing does not directly accommodate different agent components and mechanisms. These are the authors' characterizations of cited work, not findings independently verified here. [§§1–2]

**Research gap [A]:** a generic, automated approach for indirect injection assessment against black-box, multi-step agents with diverse tasks and architectures. Its search must work with sparse binary feedback and language-shaped input. [pp. 1–2]

**Motivation [A]:** real deployments restrict internal access, user tasks vary dynamically, and systems combine interconnected tools and services. These complicate risk assessment. The curated corpus supplies useful early candidates; coverage scoring adds a search signal aggregated from binary outcomes; confidence-bound selection directs a limited evaluation budget toward promising and less-explored candidates. [pp. 1–2, 5]

**Scope [A]:** external-data injection against personal-assistant and web agents, including web agents that receive multimodal input. The evaluated VWA-adv attacks specifically use text triggers. The paper's broad discussion of multimodal systems must not be mistaken for an evaluation of image-payload generation. [§5.2]

## 5. Research questions / objectives / hypotheses

The paper does not state a numbered research-question list or formal null/alternative hypotheses. Its objectives can be extracted without inventing formal questions:

| ID | Author-stated or source-grounded objective | Addressed by |
|---|---|---|
| O1 | Automatically discover effective indirect injections under black-box constraints | Method and benchmark optimization |
| O2 | Apply the framework across different agent architectures and tasks | AgentDojo and VWA-adv |
| O3 | Produce attacks that transfer to unseen tasks and underlying LLMs | Table 1 and Appendix B |
| O4 | Evaluate attacks against defenses and demonstrate adaptive testing | Tables 2–3 and repeat-defense optimization |
| O5 | Assess the contribution of corpus and search components | Figure 3 and §5.3 |
| O6 | Demonstrate applicability in a deployment-style web environment | Figure 1 and §5.4 |

**User-supplied research question:** Why are web AI agents more vulnerable than standalone LLMs? **Analyst relevance inference [D]:** the paper illustrates an expanded input/action pathway and limited attacker access that nevertheless supports successful attacks. It neither formally asks this comparative question nor controls for the difference between standalone and agent deployments. No hypothesis of greater comparative vulnerability is experimentally tested.

## 6. Assumptions / threat model

The legitimate user is benign and asks the agent to complete intended tasks. The attacker's objective differs from the user's. Neither users nor attackers see the underlying model internals or agent design. The attacker can access and test the agent similarly to a legitimate user, on tasks resembling real usage. [A; §3]

Attacker control is restricted to external data, such as a shopping-site item or calendar event. The paper also illustrates a malicious email that causes sensitive information to be sent to a recipient. Success can be checked after execution by observing the environment, for example the recipient's inbox. An individual task yields success/failure rather than gradients or internal model state. [A; p. 3]

The controlled attack surface is therefore an **external content location**, not the benign user's request, model weights, hosting platform, or computational infrastructure. Direct infrastructure attacks and misuse in which a user directly asks an agent to do harm are excluded. [A; pp. 3–4]

**Trust boundary interpretation [D]:** the user's task and tool-access permissions define intended behavior, whereas retrieved content should supply task information. The attack works when content-derived instructions influence planning or tool use. The paper does not provide a formal trust lattice or complete permission model, so this is an explanatory interpretation rather than an author-defined security policy.

The threat model assumes access sufficient to place content the agent will encounter and to conduct repeated tests. It does not quantify the probability of encounter on arbitrary public websites, the attacker's economic budget, or the difficulty of obtaining write access across deployments. Figure 1's review placement uses a regular account, but that particular affordance should not be generalized to every environment. [A/D; §5.4]

## 7. Methodology

### 7.1 Study design and framework

This is an empirical offensive-testing study with an algorithmic contribution. AgentVigil receives a target agent, attack templates, user tasks, and attacker objectives. An adversarial task combines a user task with an injection goal. Initial templates are instantiated and evaluated to create seeds. A repeated loop selects one or two parents, mutates them, inserts the candidate into an allowed environmental location, executes tasks, records success and new coverage, scores the candidate, and adds it to storage. [A; §§4.1–4.5, Figure 2]

### 7.2 Corpus collection

Templates come from human heuristics, online resources, and existing injection research. Placeholders can represent the model, user task, and attacker goal. Included strategies are role-playing, delimiter manipulation, and obfuscation. The stated rationale is to supply diverse, high-quality starting points rather than leave sparse success feedback to guide a nearly random search. [A; §4.2]

The supplied paper does not specify the total corpus size, a complete template listing, collection dates, template filtering criteria, or a reproducible corpus-quality rubric. 'High-quality' is the authors' characterization, supported in part by stronger starting performance than the handcrafted baseline. [A/D; pp. 4, 6, 8]

### 7.3 Five mutation operations

| Operation | Author-described transformation | Parent structure |
|---|---|---|
| Shorten | Makes the seed more concise | One existing seed |
| Expand | Adds contextual information | One existing seed |
| Rephrase | Changes wording while preserving meaning | One existing seed |
| Crossover | Combines elements of two parent seeds | Two existing seeds |
| GenerateSimilar | Creates stylistically similar content with different content | Existing seed as reference |

A helper LLM generates mutations using templates and context. Mutation types are randomly selected. The authors prefer basic operations for simplicity, diversity, and use with moderately capable smaller models; Llama-3-8B and GPT-4o-mini are given as examples. The reported benchmark experiments use GPT-4o-mini, not a demonstrated comparison between those helpers. [A; §4.3]

### 7.4 Scoring and selection

A seed receives its ASR plus a weighted normalized bonus for newly successful task combinations. The authors intend this to reward both effectiveness and expansion beyond previously compromised tasks. Selection adds an exploration bonus to the seed score, favoring nodes with fewer visits. One parent is selected by the highest score; two are selected for a two-parent operation. Parent/ancestor visit counts increase when a new node is added. [A/B; §§4.4–4.5, Algorithms 1–3]

The paper states that UCB1 is preferred over UCT because evaluating each variant is expensive and deep expansion is undesirable. UCB1 is expanded as **Upper Confidence Bound 1**. UCT is named but not expanded or fully specified in the supplied paper; its conventional expansion is not imported here. The numerical coverage and exploration coefficients, epsilon value, initialization rules, and tie handling are not supplied. [A/B; p. 5 and Algorithm 2]

### 7.5 Data and experimental configuration

| Configuration | AgentDojo | VWA-adv |
|---|---|---|
| Agent setting | Personal assistant with application tools/state | Visual web tasks based on VisualWebArena |
| Attack location | Defined environmental placeholders | Text-trigger locations; image triggers exist but are not the focus |
| Fuzzing/test split | 142 / 173 adversarial tasks | 99 / 100 tasks |
| Optimization backbone | o3-mini | GPT-4o |
| Helper model | GPT-4o-mini | GPT-4o-mini |
| Optimization iterations | 10 | 10 |
| Mutated prompts per iteration | 3 | 10 |
| Candidate evaluation sampling | Random quarter of user and injection tasks from each suite | No equivalent quarter-sampling rule stated |
| Transfer selection | Top 5 seeds by score | Top 5 seeds by score |
| Baseline | AgentDojo handcrafted prompts | VWA-adv handcrafted prompts |
| Transfer backbones | o3-mini, GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet | GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet, Gemini-2-flash-exp |

For AgentDojo, the success rate is explicitly computed over the **union of adversarial prompts**. **Interpretation [D]:** this counts tasks on which at least one selected prompt succeeds, rather than the success probability of one fixed prompt. The VWA-adv protocol is introduced as similar, but its prose does not separately restate the union rule. That reporting detail should remain qualified. [p. 6–7]

**Derived counts [C]:** the listed splits contain 142 + 173 = 315 AgentDojo adversarial tasks and 99 + 100 = 199 VWA-adv tasks. Ten iterations times three or ten generated prompts yield 30 and 100 mutation outputs respectively, excluding initial seeds and any unspecified retries. These are output-count derivations, not target-agent call counts.

Appendix A gives checkpoints: o3-mini-2024-12-17; gpt-4o-mini-2024-07-18; gpt-4o-2024-08-06; claude-3-5-sonnet-20241022; and gemini-2.0-flash-exp. Appendix B adds o3-mini-2025-01-31 and open-source models. AgentDojo and VWA-adv are described as providing open code/data under the MIT license. Their repositories were not supplied or inspected. [A; p. 12]

No hardware specification, implementation version, generation temperature, random seed, full prompt budget, measured runtime, monetary cost, repeated-run count, confidence interval, or statistical test is reported in the supplied text. Random splitting is described, but a grouping rule preventing related task variants from crossing splits is not specified.

## 8. Experiments / analyses

### X1 — AgentDojo optimization

**Purpose:** test whether the framework improves black-box attacks against a personal assistant. **Setup:** optimize against o3-mini on 142 fuzzing tasks, using GPT-4o-mini mutations, 3 new prompts per iteration, 10 iterations, and quarter sampling from each suite for candidate evaluation. **Metric:** injection-task ASR and coverage. **Result:** handcrafted baseline 38%, initial corpus 63%, optimized result 71%. These are fuzzing-set results, not unseen-task performance. [A; §5.1, pp. 6–8]

### X2 — AgentDojo task/model transfer

**Purpose:** test selected attacks beyond the optimization tasks and model. **Setup:** top five seeds, 173 test tasks, four backbones. **Results:** o3-mini 65% versus 34%; GPT-4o 19% versus 25%; GPT-4o-mini 43% versus 28%; Claude 4% versus 8%. Transfer therefore improves two listed test backbones and underperforms the baseline on two. Broad transfer language needs these exceptions. [B; Table 1]

### X3 — AgentDojo defenses and adaptive optimization

**Conditions:** no defense; pi_detector, a BERT-based injection classifier; repeat, which repeats user instructions after each function call; delimit, which surrounds tool outputs with delimiters and prioritizes user instructions through system prompts. Table 2 evaluates selected prompts against o3-mini on fuzzing tasks. **Results:** AgentVigil 71%, 25%, 12%, 49%; baseline 38%, 13%, 21%, 36%, respectively. The repeat column favors the baseline, contrary to the prose's 'consistently outperforms' claim. [A/B; pp. 6–8]

A distinct experiment **re-optimizes against repeat-protected agents**, achieving 74% versus a 21% baseline. This is adaptive attack generation, not the same condition as the fixed selected attacks obtaining 12% in Table 2. The paper does not fully restate its budget or transfer protocol for that additional experiment. Tool_filter is excluded because of o3-mini incompatibility. Other defenses are omitted for author-stated utility, cost, capability, or architecture-adaptation concerns. [A; pp. 6–7]

### X4 — VWA-adv optimization

**Purpose:** test web agents with multimodal task input but text-based injections. **Setup:** GPT-4o optimization backbone, 99 fuzzing tasks, GPT-4o-mini helper, 10 mutations per iteration for 10 iterations. **Result:** baseline 36%, initial corpus 54%, final optimization/coverage result 70%. Figure 4 tracks the rising coverage. Selected prompts in Table 1 instead show 60% on the GPT-4o fuzzing set; the paper does not explicitly resolve how selection, aggregation, or evaluation produces the difference. [A/B; §§5.2, B.4]

### X5 — VWA-adv transfer

**Setup:** top five selected seeds, 100 test tasks, four models. **Results:** GPT-4o 59% versus 44%; GPT-4o-mini 54% versus 29%; Claude 42% versus 51%; Gemini 67% versus 50%. The first three success-rate improvements are not all positive: Claude is an exception. Gemini is an unseen optimization backbone, and GPT-4o test performance concerns unseen tasks on the optimization model. [B; Table 1]

### X6 — VWA-adv defenses

**Conditions:** safety uses delimiters and system prompts; paraphrase rewrites untrusted text; combined applies both. **Results:** AgentVigil 60% without defense, 29% safety, 33% paraphrase, 27% combined; baseline 36%, 34%, 27%, 30%. AgentVigil is stronger only under no defense and paraphrase in this table. An image–text consistency defense is excluded because of increased API calls. These results do not establish universal superiority against web defenses. [A/B; §5.2, Table 3]

### X7 — Ablation

**Purpose:** assess corpus and search mechanisms on AgentDojo. **Conditions:** full method; replace curated corpus with benchmark handcrafted prompts; replace both adaptive scoring and MCTS selection with uniform random selection. Figure 3 shows the full curve rising fastest and highest, the baseline-corpus curve flattening after about four iterations, and the joint search ablation improving more slowly. Scoring and selection are removed together, so their separate causal contributions are not isolated. [A/B/D; §5.3]

### X8 — Local deployment-style case study

**Setup:** local copy of a Magento2-based WebArena shopping site and its default agent. A regular account posts a malicious review. The user asks for a screen protector and reviewers mentioning good fingerprint resistance; execution involves more than ten steps. Generated VWA-adv prompts redirect the agent to arbitrary URLs. The authors report phishing navigation, malicious-file downloads, and private-information transmission as possible demonstrated outcomes. Figure 1 directly depicts redirected navigation, rather than complete forensic evidence for all outcomes. No trial count, denominator, detailed payload set, or quantitative case-study ASR is supplied. [A/B; Figure 1, §5.4]

### X9 — Extra models and additional baselines

Appendix B.1 reports benign-task utility of 42% for Llama3.3-70B-Instruct, 54% for Qwen2.5-72B-Instruct, 74% for QwQ-32B, and 79% for o3-mini. QwQ-32B is then used for further attacks. Table 4 compares AgentVigil with AgentDojo Baseline, OpenPromptInjection, and InjecAgent on QwQ-32B and the newer o3-mini checkpoint. AgentVigil has the highest listed ASR in all four model/split columns. The nearby updated-o3-mini prose gives different numbers from the table; both are preserved below. [A/B; p. 12]

### X10 — Scenario breakdown

Table 5 separates Slack, Workspace, Travel, and Banking in AgentDojo, and illusioning versus goal misdirection in VWA-adv. AgentVigil exceeds the baseline in every listed scenario/model/split cell. This supports breadth across those listed scenarios, while exposing substantial variation: o3-mini Banking test ASR is 38%, versus Slack 97%; GPT-4o goal-misdirection test ASR is 42%, versus illusioning 76%. [B; Table 5]

## 9. Results

The most defensible synthesis is that the framework substantially improves attacks in several optimization and transfer settings, while its performance is model- and defense-dependent. It succeeds even under the paper's restricted external-content threat model. The evidence does not support a uniform claim that every backbone or defense condition improves. [A/B/D]

| Finding | Exact source values | Condition and qualification |
|---|---|---|
| AgentDojo optimization improves over handcrafted baseline | 71% versus 38% | o3-mini fuzzing; initial corpus already reaches 63% |
| VWA-adv optimization improves | 70% versus 36% | GPT-4o optimization result; selected-prompt table gives 60% |
| Unseen AgentDojo tasks remain vulnerable | 65% versus 34% | o3-mini test set; selected attack union |
| Unseen VWA-adv tasks remain vulnerable | 59% versus 44% | GPT-4o test set |
| Strong unseen-model web transfer | 67% versus 50% | Gemini-2-flash-exp test set |
| Claude is a consistent transfer weakness | AgentDojo test 4% versus 8%; VWA-adv test 42% versus 51% | Baselines outperform AgentVigil in these conditions |
| Adaptive repeat-defense testing succeeds | 74% versus 21% | Separate optimization against defended AgentDojo agent |
| Web defenses materially reduce selected-attack success | 60% falls to 29%, 33%, or 27% | Safety, paraphrase, combined; fuzzing/GPT-4o |

**Analyst-derived effect sizes [C]:** AgentDojo optimization gains 71 − 38 = **33 percentage points**, equivalent to (71 − 38)/38 × 100 ≈ **86.8% relative improvement**, or 71/38 ≈ **1.87 times** baseline. VWA-adv's reported optimization gains 70 − 36 = **34 points**, (70 − 36)/36 × 100 ≈ **94.4% relative improvement**, or **1.94 times** baseline. These calculations explain 'nearly doubling' without equating percentage points with percent.

The curated corpus provides much of the initial gain. AgentDojo starts 63 − 38 = **25 points** above baseline and adds 71 − 63 = **8 points** during refinement. VWA-adv starts 54 − 36 = **18 points** above baseline and adds 70 − 54 = **16 points**. These are decompositions of reported numbers, not controlled estimates attributing every point to a single component. [C]

No confidence intervals or hypothesis tests accompany these percentages. The authors repeatedly use 'significant' in descriptive language, but the supplied work does not establish statistical significance. Rounded ASRs should not be converted into exact successful-task counts without more information about aggregation and denominators.

## 10. Figure-by-figure interpretation

### Figure 1 — Review content redirects a shopping agent

**Source:** physical p. 2; case-study discussion p. 9. **Inspected visually:** yes. The figure has three substantive regions: a shopping page with a highlighted injected review on the left; user/task and agent/thought boxes in the middle; and an attacker-controlled destination plus outcome labels on the right. Arrows show the user directing the agent, retrieved review text influencing it, and the agent moving toward the attacker's destination.

The legitimate task is to find a Samsung Galaxy S6 screen protector and identify reviews about fingerprint resistance. The visible agent-thought excerpt treats a message to visit a URL before completing the task as an instruction it will follow. This directly illustrates the proposed content-to-command failure mechanism. The displayed fake GitHub-style URL is an example destination, not a source for this analysis to visit. [A/B]

There are no axes, units, uncertainty bars, or quantitative success values. Red highlights encode injected content and malicious outcomes; user/agent labels distinguish intended task flow from redirection. Icons and the destination screenshot are illustrative. Small review text does not allow confident reconstruction of the complete attack payload. Labels for malware downloads and private-information transmission describe reported consequences; the figure alone does not show full execution traces proving each consequence.

### Figure 2 — AgentVigil architecture

**Source:** p. 4. **Inspected visually:** yes. The left gray region depicts the target system: user, agent, environment, and attacker. The environment lists code execution, email, file system, and browser. Red arrows indicate injection into external sources and subsequent exposure to the agent. This is the attack path.

The right region depicts testing: initial/current seeds feed a mutator; mutated seeds are tested in the agent system; binary outcomes reach a scorer; selection and storage maintain candidates for future iterations. Yellow boxes identify prompt-generation stages, purple boxes selection/storage, and a pink scorer marks evaluation. The feedback loop rather than any single prompt is the framework's central structure. [B]

The diagram is schematic, without latency, bandwidth, call counts, or component version labels. The caption says effectiveness and scalability are ensured; the diagram itself establishes component organization, not quantitative scalability evidence. Details of confidence-bound selection and coverage scoring come from §§4.4–4.5 and Appendix C.

### Figure 3 — AgentDojo coverage and ablation curves

**Source:** p. 6, discussed pp. 8–9. **Inspected visually:** yes. This is a line plot with horizontal axis **Steps**, ten optimization steps, and vertical axis **Average Coverage**, a unitless fraction displayed from 0.0 to 0.5. Both axes are linear. Tick labels on the x-axis show 2, 4, 6, 8, 10.

The blue solid line labeled Ours rises from approximately 0.18 at step 1 to approximately 0.37–0.38 at step 10. The orange dashed line, w/o Initial Corpus, rises from about 0.08 to about 0.16 and then flattens. The green dashed line, w/o Seed Selection & Scoring, rises from about 0.16 to about 0.27. These are **approximate visual estimates**, not exact reported point values. Small markers distinguish points; no error bars, confidence bands, or statistical markers appear. [B]

The full method ends highest, and replacing the curated corpus ends lowest. Removing scoring and selection together produces intermediate coverage with slower improvement. This supports the authors' qualitative component comparison. It does not separately identify scoring's and selection's individual effects. The plotted final coverage near 0.38 is not numerically identical to the 0.71 AgentDojo ASR reported in prose/Table 1. The work does not define their aggregation sufficiently to convert one into the other; neither should be silently substituted.

### Figure 4 — VWA-adv optimization coverage

**Source:** p. 13; introduced in §5.2 and B.4. **Inspected visually:** yes. A single blue line with small markers plots **Steps** against **Average Coverage**. Axes are linear; y-axis limits are 0.50–0.80. There is no comparative legend because only one curve is shown, and there are no uncertainty bars.

The curve begins near 0.54, rises to roughly 0.63 at step 2, reaches around 0.65–0.66 at steps 3–5, then increases to 0.70 around step 8 and remains near that level through step 10. Individual unlabeled intermediate values are approximate visual estimates. The starting 54% and final 70% are also explicitly reported in the text, giving those endpoints stronger grounding. [A/B]

The figure supports improvement and a late plateau in this run. Its truncated y-axis makes vertical changes visually prominent, and it does not display the 36% baseline as a line. It cannot establish repeat-run stability, cost efficiency, or the source of the 60% selected-prompt result in Table 1.

## 11. Table-by-table interpretation

All table values below are visually readable and agree with the supplied extracted cells. Values are unitless ASR fractions, so 0.71 corresponds to 71%. Tables do not report standard errors, confidence intervals, sample-level counts, or significance tests. Boldface indicates selected higher values rather than documented statistical significance.

### Table 1 — Task/model transfer

**Source:** p. 8. Each pair is **Handcrafted / AgentVigil**, a presentation transformation preserving original values.

| Benchmark / split | o3-mini | GPT-4o | GPT-4o-mini | Claude-3.5-Sonnet | Gemini-2-flash-exp |
|---|---|---|---|---|---|
| AgentDojo fuzzing | 0.38 / 0.71 | 0.22 / 0.22 | 0.28 / 0.49 | 0.12 / 0.03 | — |
| AgentDojo test | 0.34 / 0.65 | 0.25 / 0.19 | 0.28 / 0.43 | 0.08 / 0.04 | — |
| VWA-adv fuzzing | — | 0.36 / 0.60 | 0.08 / 0.47 | 0.47 / 0.31 | 0.49 / 0.67 |
| VWA-adv test | — | 0.44 / 0.59 | 0.29 / 0.54 | 0.51 / 0.42 | 0.50 / 0.67 |

There is a tie on AgentDojo/GPT-4o fuzzing at 0.22. AgentVigil underperforms on every displayed Claude condition and on AgentDojo/GPT-4o test. Among AgentVigil's AgentDojo test columns, o3-mini is highest and Claude lowest; among its VWA-adv test columns, Gemini is highest and Claude lowest.

Footnotes state Gemini does not fully support AgentDojo tool calls and the early o3-mini version does not fully support VWA-adv. Dashes denote unavailable evaluations, not zero success. The table caption specifies optimization against o3-mini for AgentDojo and GPT-4o for VWA-adv. Selected-prompt results should not automatically replace whole-search coverage results.

### Table 2 — AgentDojo defenses

**Source:** p. 8; o3-mini fuzzing tasks and selected prompts.

| Attack | No defense | pi_detector | repeat | delimit |
|---|---:|---:|---:|---:|
| Handcrafted | 0.38 | 0.13 | 0.21 | 0.36 |
| AgentVigil | 0.71 | 0.25 | 0.12 | 0.49 |

AgentVigil exceeds baseline except under repeat. Within each attack row, defenses lower ASR relative to no defense. Repeat gives AgentVigil's lowest ASR; pi_detector gives the baseline's lowest. Delimit leaves the highest defended ASR in both rows. The caption says 'four defenses,' but the table contains three defense columns and one no-defense condition. This is a caption–table mismatch, not evidence of an unseen fourth evaluated defense.

### Table 3 — Web-agent defenses

**Source:** p. 8; GPT-4o VWA-adv fuzzing tasks.

| Attack | No defense | safety | paraphrase | combined |
|---|---:|---:|---:|---:|
| Handcrafted | 0.36 | 0.34 | 0.27 | 0.30 |
| AgentVigil | 0.60 | 0.29 | 0.33 | 0.27 |

AgentVigil is stronger without defense and under paraphrase, but weaker under safety and combined. For AgentVigil, combined at 0.27 is lower than safety at 0.29 and paraphrase at 0.33. Thus the prose saying combined does not further reduce success compared with individual defenses is not literally supported for this row. For the baseline, combined is between safety and paraphrase. The authors' proposed explanation involving prompt complexity and limited context is an interpretation, not a directly measured causal mechanism.

### Table 4 — Additional baselines and models

**Source:** p. 12. Pairs mean **fuzzing / test**.

| Attack | o3-mini-2025-01-31 | QwQ-32B |
|---|---|---|
| AgentVigil | 0.73 / 0.76 | 0.72 / 0.74 |
| AgentDojo Baseline | 0.47 / 0.49 | 0.45 / 0.47 |
| OpenPromptInjection | 0.38 / 0.39 | 0.20 / 0.20 |
| InjecAgent | 0.15 / 0.11 | 0.14 / 0.12 |

AgentVigil ranks highest and InjecAgent lowest in every listed column/split. The updated-o3-mini table values differ from B.1 prose, which attributes 72%/74% to AgentVigil and 50%/53% to the handcrafted baseline. The 72%/74% pair matches the QwQ-32B table column, but the source does not authorize silently reassignment of the prose. Checkpoint identity and correct values remain unresolved.

### Table 5 — Scenario-specific outcomes

**Source:** p. 14. All pairs are **fuzzing / test**.

| Benchmark / model | Scenario | AgentVigil | Baseline |
|---|---|---|---|
| AgentDojo / o3-mini | Slack | 0.81 / 0.97 | 0.64 / 0.70 |
| AgentDojo / o3-mini | Workspace | 0.63 / 0.60 | 0.20 / 0.22 |
| AgentDojo / o3-mini | Travel | 0.71 / 0.83 | 0.55 / 0.50 |
| AgentDojo / o3-mini | Banking | 0.49 / 0.38 | 0.25 / 0.23 |
| AgentDojo / QwQ-32B | Slack | 1.00 / 0.97 | 0.85 / 0.88 |
| AgentDojo / QwQ-32B | Workspace | 0.33 / 0.42 | 0.05 / 0.10 |
| AgentDojo / QwQ-32B | Travel | 0.80 / 0.80 | 0.60 / 0.65 |
| AgentDojo / QwQ-32B | Banking | 0.60 / 0.65 | 0.23 / 0.23 |
| VWA-adv / GPT-4o | Illusioning | 0.82 / 0.76 | 0.51 / 0.62 |
| VWA-adv / GPT-4o | Goal misdirection | 0.58 / 0.42 | 0.00 / 0.20 |

Every listed comparison favors AgentVigil. QwQ-32B Slack fuzzing reaches 1.00, which applies to that scenario only. The zero baseline for goal-misdirection fuzzing is a measured table value, not a missing entry. Illusioning is easier for these selected attacks than goal misdirection in both splits. Scenario sample counts and aggregation weights are absent, so a simple unweighted average cannot be assumed to reproduce global ASR. Table 5 labels o3-mini without a checkpoint suffix, preventing confident allocation to one of the two checkpoints discussed elsewhere.

## 12. Diagram / architecture interpretation

Figures 1 and 2 provide complementary views. Figure 1 follows a single attack path: benign user request → web-agent browsing → attacker-controlled customer review → instruction adopted by the agent → attacker-chosen navigation. The important transition is between reading a review as task data and treating review text as guidance for what action to perform. [B/D]

Figure 2 adds the testing control loop. Template inputs create current seeds; the mutator produces candidate prompts; target-agent execution produces task outcomes; the scorer computes effectiveness and new coverage; seed selection/storage feed future candidates. The target agent's application tools are distinct from the helper LLM used to mutate attacks. One executes the legitimate workflow under test; the other generates testing inputs. [A/B]

The system diagram separates **attack data flow** through the environment from **optimization feedback** through scorer and selection. Feedback is not privileged access to model reasoning: it is derived from externally assessed outcomes. Coverage adds memory across trials to those outcomes. The paper's 'intermediate feedback' therefore means an aggregate search signal assembled from task successes, not a richer per-task internal oracle. [A/D; pp. 2–5]

The diagram's storage and selector are separate boxes, but their API, persistence format, and concurrency are not specified. The corpus/tree is described through mutation histories. Crossover permits two parents, and ALG3 refers to parent node(s); thus the ancestry structure is not necessarily a strict single-parent tree. This matters for reproducibility of traversal and visit accounting. [B/D]

## 13. Equations and mathematical concepts

### E1 — Attack success rate

**Location:** Algorithm 1, p. 13, line 19.

`ASR = total_success / num_questions`

This is a scalar ratio. `total_success` counts successful evaluated injections; `num_questions` counts evaluated cases according to the algorithm. Its intended output is a fraction of evaluated cases succeeding. It requires a nonzero denominator, but no zero-case guard is shown. The source prints a minor spelling variation in `total_succcess`; the prose and increments make the intended success counter identifiable. [A/B]

An important granularity ambiguity remains: the loop says `for all task_suite in sampled_tasks`, while comments refer to user/injection combinations and increments occur inside the suite loop. A literal implementation could count suites rather than combinations unless additional inner evaluation is implicit. The methodological prose defines ASR over tasks, so the algorithm's loop granularity should be flagged rather than silently repaired.

### E2 — Coverage-aware seed score

**Location:** Algorithm 1, p. 13, line 20.

`seed_score = ASR + C_cov × coverage_bonus / num_questions`

The source uses `C`; `C_cov` is an analyst-added disambiguation label. It is the coverage factor supplied to ALG1. `coverage_bonus` counts newly successful combinations not previously covered in the run; `num_questions` normalizes this count. The output is a search score combining current success and novelty of task coverage. Unlike ASR alone, this score is not necessarily a probability and need not be bounded by one. The coefficient's value and constraints are not specified. [A/B/D]

The prose clearly limits coverage rewards to previously unsuccessful tasks. The pseudocode's second conditional only says `if injection successful`; the preceding comment instructs identifying newly successful combinations. Consequently the novelty guard is conveyed in a comment rather than an explicit condition. The supplied algorithm should not be implemented literally without resolving that discrepancy. [B/D]

### E3 — Confidence-bound selection

**Location:** Algorithm 2, p. 13, lines 1–2.

`total_visits = Σ(node in N) node.visits`

`UCB(node) = node.score + C_explore × sqrt(log(total_visits + 1) / (node.visits + ε))`

`N` is the set of candidate nodes; `node.score` is empirical seed score; `node.visits` records visits; `C_explore` is the exploration factor called `C` in this algorithm. `Σ` sums visits, `log` applies a logarithm, and the square root forms an exploration term. The numerator grows with total recorded visits, while a larger node visit count reduces its exploration reward. [A/B]

The symbol `ε` appears in the denominator without a supplied definition or value. **Analyst interpretation:** its position suggests an offset relevant to zero visits, but the paper does not specify that rationale. The logarithm base, coefficient value, node initialization, score updates for existing nodes, and numerical validity constraints are not given. One should not assume the two algorithms' `C` values are equal.

### ALG1–ALG3 — Operational meaning

ALG1 initializes counters, evaluates sampled tasks, records successes/new coverage, and returns the score. Its Ensure line also mentions suite results, but the visible Return gives only `seed_score`. ALG2 selects the highest UCB node when `n = 1`, or sorts and selects two when `n = 2`. No behavior for other `n` values, ties, or too-small candidate sets is specified. ALG3 starts from parent nodes, increments ancestor visits, adds further ancestors, and inserts the new node into `N`. It does not visibly update ancestor reward averages or scores. [B]

With two-parent crossover, shared ancestors can exist. ALG3 does not show a visited set or clearly defined queue/set semantics, so duplicate ancestor updates cannot be ruled out from the pseudocode alone. This is an implementation ambiguity, not a reported experimental failure. No theorem establishes convergence, optimality, or a quantitative sample-complexity guarantee in the supplied paper.

## 14. Interpretation and discussion

The evidence answers O1 and O2 by showing effective external-data injections in two agent benchmark families. O3 receives mixed support: unseen-task success is substantial on the optimization backbone, GPT-4o-mini and Gemini transfer can be strong, but Claude and AgentDojo/GPT-4o expose exceptions. O4 shows defenses reduce attack success and adaptive optimization can find new repeat-defense attacks. O5 supports corpus quality and the combined scoring/selection mechanism without separating the latter components. O6 provides a local deployment-style demonstration, rather than a broad live-deployment survey. [A/B/D]

For the research question, the source-grounded mechanism is: an agent needs to ingest external content to fulfill a user's goal; that content may be attacker-controlled; the LLM uses it in planning; connected tools can turn altered planning into navigation, communication, or other unauthorized actions. **Analyst inference:** this exposes more routes for adversarial influence and more consequential outputs than a standalone text interaction under a narrower interface. The paper provides no matched standalone control, so this remains a structural relevance argument rather than a proven comparative vulnerability ranking.

### Cross-reference and consistency findings

| Issue | Source side 1 | Source side 2 | Assessment |
|---|---|---|---|
| VWA-adv final result | §5.2/Figure 4: 70% optimization coverage/result | Tables 1/3: 60% selected-prompt fuzzing ASR | Different reporting scopes may matter, but reconciliation is not explicit |
| AgentDojo defense superiority | §5.1 says consistently outperforms baseline | T2 repeat: 0.12 versus 0.21 | Prose is too broad for the fixed-attack table |
| Web combined defense | §5.2 says no further reduction versus individual defenses | T3 AgentVigil: 0.27 versus 0.29/0.33 | Literal claim conflicts with this row |
| Updated o3-mini results | B.1: AgentVigil 72%/74%, baseline 50%/53% | T4: 73%/76%, baseline 47%/49% | Unresolved text–table discrepancy |
| AgentDojo coverage versus ASR | F3 endpoint about 0.38 | Main ASR 0.71 | Aggregation/metric relationship insufficiently explained |
| Defense count | T2 caption says four defenses | Three defenses plus no defense | Caption–table count mismatch |
| Novelty reward | §4.4 rewards newly attacked tasks | ALG1 condition only states successful injection | Novelty rule is implicit in comment |
| Appendix detection | Input metadata detects none | Visible A–C headings | Metadata does not reflect actual document content |

The VWA-adv transfer prose reports absolute improvements of '15% to 40%.' **Derived [C]:** Table 1's non-Claude gains range from 0.15 to 0.39, or 15–39 percentage points, across its listed conditions. The wording is broadly compatible with rounding to 40, but 'absolute' changes should be expressed in points. No discrepancy should be converted into an exact correction without author clarification.

## 15. Contributions and novelty

**Conceptual [A]:** the work frames generic black-box indirect-injection assessment as a fuzzing problem over diverse, multi-step agents. It highlights sparse feedback and restricted control of external content as methodological challenges.

**Methodological [A]:** it combines a curated template corpus, LLM-assisted mutations, task-coverage rewards, and adaptive seed selection into one iterative testing workflow.

**Algorithmic [A]:** it adapts confidence-bound selection to prompt mutation histories and propagates visit counts through ancestry. The contribution is an adaptation and integration, not a new foundational MCTS theorem.

**System [A]:** the framework is designed to interface with different agent environments through prompt placement and outcome feedback. The supplied paper does not provide sufficient implementation artifacts to independently verify portability to arbitrary architectures.

**Empirical [A/B]:** evaluations span two benchmark families, unseen tasks/backbones, selected defenses, adaptive defended-agent testing, ablations, additional baselines, open-source-model testing, scenario breakdowns, and a local web case study.

The authors call AgentVigil the first generic automated black-box approach of this kind. That priority claim is represented as **author-reported**, with HIGH confidence that they state it but UNKNOWN independently verified historical priority. No new dataset, benchmark, formal theorem, or complete standalone-versus-agent comparison is introduced in the supplied work.

## 16. Limitations

### Authors' stated limitations

1. **High computational cost:** iterative MCTS-guided fuzzing can hinder scaling to extremely large agent systems or real-time use. No exact runtime or cost is given. [A; §7]
2. **Model-specific transfer weakness:** attacks perform relatively poorly against models such as Claude; model-specific defenses or alignment may limit generalization. The proposed explanation is suggestive rather than experimentally isolated. [A; §7]
3. **Need for further adaptation:** robust cross-model effectiveness and more efficient optimization require further investigation. [A; §7]

### Additional evidence-based analyst observations

These observations are **[D] analyst assessments**, not admissions attributed to the authors:

- Text-trigger evaluation does not establish effectiveness of generated image-based payloads, even though the web agents process multimodal input.
- The fixed-prompt defense comparisons include conditions where the handcrafted baseline performs better.
- Joint removal of scoring and selection cannot establish their independent effects.
- No standalone-LLM control supports the user's comparative premise directly.
- Missing budgets, corpus details, coefficients, random seeds, and repeat-run statistics limit reproducibility and uncertainty assessment.
- Task-union success can exceed single-prompt success and depends on the selected-prompt budget.
- The local shopping case has no reported success denominator, outcome trace set, or broad deployment sample.
- Several text–table and metric-reporting inconsistencies weaken confidence in particular numerical interpretations.
- Model version compatibility excludes some cross-benchmark cells; absent cells should not be read as evidence of robustness.

## 17. Threats to validity

The following categories are analyst-applied labels; the authors do not explicitly organize their limitations this way.

**Internal validity [D]:** the curated corpus is stronger at baseline, and ablation removes scoring and selection together. Thus performance gains cannot be uniquely attributed to MCTS rather than scoring, corpus, mutation diversity, or aggregation. Random task splits are described but not accompanied by seeds or repeated splits. The adaptive repeat-defense experiment has a different optimization condition from the fixed selected-prompt table.

**Construct validity [D]:** benchmark injection success measures attainment of an attacker objective. It does not quantify the complete economic or privacy harm of a real attack, probability that the agent encounters the payload in the wild, or how safely it completes benign tasks afterward. Figure 3's coverage and the headline ASR are not interchangeable. Benign utility scores in Appendix B describe task capability, not injection robustness.

**Statistical conclusion validity [D]:** no uncertainty intervals, significance tests, or repeat-run variance are reported. Some percentages are rounded and prompt unions are used. The evidence supports descriptive comparisons within reported conditions, not precise population-level risk estimates.

**External validity/generalizability [D]:** two benchmark families and several checkpoints show breadth, but Claude exceptions, compatibility exclusions, and absent architecture-specific implementation details prevent universal claims about web agents. The corpus may exploit recurrent benchmark affordances; the paper does not supply enough template detail to assess dependence on them.

**Ecological validity [D]:** a local Magento2-based environment gives more realistic interaction structure than a single isolated prompt, and review placement uses a normal account. It still does not measure encounter rates, access restrictions, active human oversight, or consequences across public deployed services.

**Reproducibility [D]:** checkpoint IDs and split sizes help, but absent corpus contents, implementation versions, score coefficients, epsilon, generation settings, and runtime budgets leave important execution choices unresolved. The supplied material supports a conceptual reconstruction rather than a verified reproduction.

## 18. Future work and open questions

### A. Explicitly proposed by the authors

The authors call for more efficient optimization and improved cross-model robustness, especially adaptation to models where existing attacks transfer poorly. They also position the framework as a foundation for better agent security and emphasize ongoing research and proactive updates because no testing or defense approach is infallible. [A; §§6–8]

### B. Additional open questions derived from the study

**Analyst questions [D]:** How much additional risk arises from agent tools versus the same model operating without tools? How do encounter probability and permission scope affect end-to-end harm? What are the separate contributions of coverage scoring and confidence-bound selection? How do one-prompt, five-prompt-union, and whole-search success compare at equal query budgets? Can defenses preserve benign utility while reducing adaptive ASR? Do payloads transfer to image-trigger tasks and other interfaces? How stable are results across random splits, generation seeds, and model checkpoints? Which values resolve the Appendix B.1/Table 4 mismatch? What operational definition explains Figure 3's coverage versus the reported global ASR?

These are not author-proposed experiments unless explicitly identified above. They mark evidence boundaries rather than introduce outside findings.

## 19. Terminology and notation glossary

| Term / symbol | Beginner-friendly meaning and source boundary |
|---|---|
| LLM | Large language model; the language-processing/planning component |
| Agent | A model combined with tools and an environment to carry out tasks |
| Indirect prompt injection | Adversarial instructions embedded in external content the agent reads |
| Direct prompt injection | Injection directly into attacker-controlled model input; contrasted with this study |
| Black-box | Access to external behavior without model/architecture internals |
| Red-teaming | Adversarial testing to expose failures or security weaknesses |
| Fuzzing | Repeated automated generation and evaluation of candidate inputs |
| Seed | Candidate adversarial prompt used as a starting point for mutation |
| Corpus | Collection of templates/seeds |
| Mutator | Procedure using a helper LLM to alter existing attack prompts |
| Crossover | Mutation combining two parent prompts |
| ASR | Attack success rate: successful evaluated cases divided by evaluated cases |
| Coverage | Which task combinations have been attacked successfully; aggregation details are incomplete |
| Coverage bonus | Reward for reaching previously unsuccessful combinations in the current run |
| Exploration | Trying less-examined candidates or paths |
| Exploitation | Developing candidates already performing well |
| MCTS | Monte Carlo Tree Search; author label for ancestry/confidence-guided selection |
| UCB1 | Upper Confidence Bound 1; selection principle named by the authors |
| UCT | Named alternative selection approach; expansion not supplied |
| BERT | Classifier family named for pi_detector; expansion not supplied in the paper |
| API | Term used for service calls; expansion not supplied in the paper |
| Multimodal | Processing more than one input type, here including visual and text information |
| Illusioning | Misleading an agent about state or object attributes |
| Goal misdirection | Causing pursuit of an attacker-chosen objective instead of the user's |
| Task suite | Related user and injection tasks for an application environment |
| Adversarial task | Combination of user task and injection objective |
| Fuzzing set | Tasks used to optimize attacks; not ordinary model-training examples |
| Test set | Held-out tasks used for attack evaluation/transfer |
| Union success | Task counted successful when an evaluated selected prompt succeeds; explicit for AgentDojo |
| Utility | Success on benign tasks, separate from security attack success |
| N | Set of candidate prompt nodes in ALG2–ALG3 |
| n | Number of nodes selected, visibly handled for 1 or 2 |
| S | Selected node or nodes |
| C in ALG1 | Coverage factor; numerical value absent |
| C in ALG2 | Exploration factor; numerical value absent and not necessarily equal to ALG1's C |
| ε | Denominator symbol in ALG2; definition/value absent |
| node.parents | Parent prompt nodes defining mutation ancestry |
| node.visits | Counter used to determine exploration reward |
| node.score | Empirical prompt score used during selection |

Definitions of terms used operationally are grounded in the supplied work. Conventional acronym expansions absent from the paper are explicitly left unfilled under closed-document mode.

## 20. Key numerical results

Complete table-cell ledgers are retained in §11. This compact reference emphasizes configuration, headline results, exceptions, and derived effects.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Accessible text pages | 14 | pages | Physical PDF sequence | Visually readable/supplied text | pp. 1–14 |
| AgentDojo fuzzing/test tasks | 142 / 173 | tasks | Random split within suites | Author-reported | p. 6, §5.1 |
| VWA-adv fuzzing/test tasks | 99 / 100 | tasks | Text-trigger study | Author-reported | p. 7, §5.2 |
| AgentDojo total | 315 | tasks | 142 + 173 | Analyst-derived | p. 6 |
| VWA-adv total | 199 | tasks | 99 + 100 | Analyst-derived | p. 7 |
| Optimization iterations | 10 / 10 | iterations | AgentDojo / VWA-adv | Author-reported | pp. 6–7 |
| Mutations per iteration | 3 / 10 | prompts | AgentDojo / VWA-adv | Author-reported | pp. 6–7 |
| Mutation outputs | 30 / 100 | outputs | 10×3 / 10×10; excludes corpus | Analyst-derived | pp. 6–7 |
| Transfer seed count | 5 | seeds | Highest-scoring selections | Author-reported | pp. 6–7 |
| AgentDojo candidate sampling | One quarter | task fraction | Each suite, per new seed | Author-reported | p. 6 |
| AgentDojo baseline/initial/final | 38 / 63 / 71 | % ASR | o3-mini optimization | Author-reported | p. 6 |
| VWA-adv baseline/initial/final | 36 / 54 / 70 | % | GPT-4o optimization/coverage | Author-reported | p. 8; F4 |
| AgentDojo optimization gain | 33 | percentage points | 71 − 38 | Analyst-derived | p. 6 |
| AgentDojo relative gain | ≈86.8 | % relative | (71−38)/38×100 | Analyst-derived | p. 6 |
| VWA-adv optimization gain | 34 | percentage points | 70 − 36 | Analyst-derived | p. 8 |
| VWA-adv relative gain | ≈94.4 | % relative | (70−36)/36×100 | Analyst-derived | p. 8 |
| AgentDojo o3-mini test | 0.65 vs 0.34 | ASR fraction | AgentVigil vs baseline | Visually readable | p. 8, T1 |
| VWA-adv GPT-4o fuzzing | 0.60 vs 0.36 | ASR fraction | Selected prompts, distinct from 70% | Visually readable | p. 8, T1/T3 |
| VWA-adv GPT-4o test | 0.59 vs 0.44 | ASR fraction | Selected prompts | Visually readable | p. 8, T1 |
| VWA-adv Gemini test | 0.67 vs 0.50 | ASR fraction | Unseen backbone | Visually readable | p. 8, T1 |
| AgentDojo repeat, fixed attacks | 0.12 vs 0.21 | ASR fraction | AgentVigil below baseline | Visually readable | p. 8, T2 |
| AgentDojo repeat, adaptive attack | 74 vs 21 | % ASR | Re-optimization against defense | Author-reported | p. 7 |
| VWA-adv defended ASRs | 0.29 / 0.33 / 0.27 | ASR fraction | Safety / paraphrase / combined | Visually readable | p. 8, T3 |
| Benign utility | 42 / 54 / 74 / 79 | % | Llama3.3 / Qwen2.5 / QwQ / o3-mini | Author-reported | p. 12, B.1 |
| Newer o3-mini table ASR | 0.73 / 0.76 | ASR fraction | Fuzzing/test; contradictory prose exists | Visually readable | p. 12, T4 |
| Newer o3-mini prose ASR | 72 / 74 | % | Fuzzing/test; differs from T4 | Author-reported | p. 12, B.1 |
| QwQ-32B table ASR | 0.72 / 0.74 | ASR fraction | Fuzzing/test | Visually readable | p. 12, T4 |
| QwQ Slack fuzzing ASR | 1.00 | ASR fraction | Scenario-specific, not global | Visually readable | p. 14, T5 |
| Web goal-misdirection test | 0.42 vs 0.20 | ASR fraction | AgentVigil vs baseline | Visually readable | p. 14, T5 |
| AgentDojo F3 final full coverage | ≈0.37–0.38 | coverage fraction | Unlabeled plotted endpoint | Approximate visual estimate | p. 6, F3 |
| Local shopping task length | More than 10 | operation steps | One described workflow | Author-reported | p. 9, §5.4 |

The table intentionally preserves contradictory representations as separate rows. Missing error bars, statistical tests, and cost estimates are not replaced with guessed values.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Restricted external content can redirect agents | Threat model and visible adopted review instruction | F1; X8 | pp. 2–4, 9 | Strong mechanism illustration; encounter probability unmeasured |
| Corpus, scoring, and selection form the testing method | Architecture, procedural descriptions, pseudocode | F2; ALG1–3 | pp. 4–5, 13–14 | Strong description; implementation parameters incomplete |
| Search improves on handcrafted benchmarks | 71 vs 38 and 70 vs 36 | X1/X4; F4 | pp. 6–8, 13 | Descriptive results; selected web table reports 60 |
| Unseen tasks remain vulnerable | 65% o3-mini and 59% GPT-4o test ASRs | T1; X2/X5 | p. 8 | Model/task conditions essential; no statistical uncertainty |
| Cross-model transfer is possible | GPT-4o-mini and Gemini gains | T1 | p. 8 | Claude and AgentDojo GPT-4o test are counterexamples to universality |
| Defense resistance varies | T2/T3 fixed-prompt columns | X3/X6 | pp. 7–8 | Several defenses favor handcrafted baseline |
| Adaptive testing can bypass repeat protection | 74% after defended-agent optimization | X3 | p. 7 | Different attack-generation condition from T2's 12% |
| Corpus and joint search mechanism help | Full F3 curve exceeds both ablations | F3; X7 | pp. 6, 8–9 | Scoring and selection not isolated individually |
| Performance spans multiple scenarios | All T5 comparisons favor AgentVigil | T5; X10 | pp. 12–14 | Scenario counts and checkpoint suffix absent |
| New baselines are weaker in listed tests | T4 rankings | T4; X9 | p. 12 | Updated-o3-mini prose disagrees with table |
| Deployment-style exploitation is feasible | Local shopping review causes unwanted navigation | F1; X8 | pp. 2, 9 | Local copy; no broad real-world success denominator |
| Computational scalability is limited | Authors explicitly acknowledge high costs | §7 | p. 9 | Qualitative limitation; no measured cost curve |
| Paper informs agent-versus-standalone research | External ingestion, multi-step planning, tools | §§1, 3, 4.1 | pp. 1–4 | Analyst inference; no controlled standalone comparison |

Claims are grounded again against their visible tables, captions, or supplied page text. The resulting verification is document-based consistency checking, not independent experimental validation.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking a helpful robot to read product reviews. One review secretly tells the robot to visit a different website before finishing. The review is supposed to be information about the product, but the robot starts treating it as an instruction. That is the problem this paper studies.

The researchers built a program that keeps trying different versions of these misleading messages. It remembers which messages work and which tasks have not yet been fooled. A second language model rewrites the messages, and the program chooses promising ones for more testing. This makes searching more effective than simply trying random wording.

The program did better than the supplied handcrafted attacks in several tests. But the result depends on the model and defenses. Some attacks transferred well to new tasks or models; others did worse than the old attacks. Defenses reduced success, and attacks specially optimized against one defense could become effective again.

For your question about web agents versus standalone models, the important idea is that a web agent reads outside material and can act on it. A misleading sentence can therefore affect what website it visits or what tool it uses. This paper shows that pathway is real in its tested settings. It does not directly measure whether an otherwise identical standalone model is less vulnerable, so that comparison remains an inference rather than a demonstrated result.

## Completeness Audit

The inventory is the denominator for coverage. All supplied substantive scientific objects are represented below; representation does not imply their claims are externally verified or every implementation detail is available.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META title/authors/venue | Yes, visual/text p. 1 | Yes | Represented in compressed form | Full original title in research.title; authors and venue below |
| ABS Abstract | Yes | Yes | Fully represented | Headline results and qualifications integrated |
| S1 Introduction | Yes, pp. 1–3 | Yes | Fully represented | Motivation, challenges, GPTFuzzer distinction, novelty claims |
| S2 Existing attacks | Yes, p. 3 | Yes | Represented in compressed form | Categories and attributed limits retained; citation list compressed |
| S2 Existing defenses | Yes, p. 3 | Yes | Represented in compressed form | Training-dependent/free, tool controls, human intervention claims |
| S3 Black-box assumption | Yes | Yes | Fully represented | Internal access excluded |
| S3 Benign-user assumption | Yes | Yes | Fully represented | User is not adversarial |
| S3 Attacker capability/goals | Yes | Yes | Fully represented | External manipulation, testing access, binary feedback |
| S3 Exclusions | Yes, pp. 3–4 | Yes | Fully represented | Misuse and infrastructure attacks excluded |
| SS4.1 Overview | Yes | Yes | Fully represented | Environmental ingestion and iterative loop |
| SS4.2 Corpus Collection | Yes | Yes | Fully represented | Sources, placeholders, strategies, missing corpus detail |
| SS4.3 Mutation Design | Yes | Yes | Fully represented | All five mutations, helper model, rationale |
| SS4.4 Seed Scoring | Yes | Yes | Fully represented | ASR and new-coverage bonus |
| SS4.5 Seed Selection | Yes | Yes | Fully represented | Confidence bounds, one/two parents, ancestor updates |
| SS5.1 AgentDojo setup/results/transfer | Yes | Yes | Fully represented | Splits, sampling, union metric, all table cells |
| SS5.1 Defenses/adaptive repeat | Yes | Yes | Fully represented | Fixed and adaptive conditions kept separate |
| SS5.2 VWA-adv setup/results/transfer | Yes | Yes | Fully represented | Text triggers, split, models, 70/60 distinction |
| SS5.2 Web defenses | Yes | Yes | Fully represented | Three included, consistency defense excluded |
| SS5.3 Ablation | Yes | Yes | Fully represented | Joint scoring/selection ablation caveat |
| SS5.4 Case study | Yes | Yes | Fully represented | Local site/account, task, reported outcomes, trace limits |
| S6 Conclusion | Yes | Yes | Represented in compressed form | Generality/transfer claim with exceptions |
| S7 Cost limitation | Yes | Yes | Fully represented | No measured cost supplied |
| S7 Cross-model limitation | Yes | Yes | Fully represented | Claude weakness and future adaptation |
| S8 Ethics Statement | Yes | Yes | Represented in compressed form | Offensive testing for defense, ongoing updates |
| S9 Acknowledgements | Yes; p. 10 text-only continuation | Yes | Represented in compressed form | Funding and disclaimer accounted for |
| REF References | Yes, pp. 10–12; p. 10 text-only | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries not independently validated |
| Objectives O1–O6 | Yes, extracted from prose | Yes | Fully represented | No invented formal RQ list |
| Explicit hypotheses | No such object present | Yes, absence stated | Fully represented | Formal hypotheses not supplied |
| User research question | Yes | Yes | Fully represented | Relevance labeled analyst inference |
| X1 AgentDojo optimization | Yes | Yes | Fully represented | 38/63/71 |
| X2 AgentDojo transfer | Yes | Yes | Fully represented | All models/splits preserved |
| X3 AgentDojo defenses/adaptation | Yes | Yes | Fully represented | 12% fixed versus 74% adaptive |
| X4 VWA-adv optimization | Yes | Yes | Fully represented | 36/54/70 and selection caveat |
| X5 VWA-adv transfer | Yes | Yes | Fully represented | Claude exception retained |
| X6 VWA-adv defenses | Yes | Yes | Fully represented | All four conditions |
| X7 Ablation | Yes | Yes | Fully represented | No separate scoring/selection isolation |
| X8 Case study | Yes | Yes | Fully represented | No quantitative denominator invented |
| X9 Additional models/baselines | Yes | Yes | Fully represented | Utility, T4, discrepancy |
| X10 Scenario breakdown | Yes | Yes | Fully represented | All T5 cells retained |
| F1 | Yes, visually | Yes | Fully represented | Small complete payload unreadable |
| F2 | Yes, visually | Yes | Fully represented | Components, arrows, feedback loop |
| F3 | Yes, visually | Yes | Fully represented | Axes, scales, encodings, approximate values |
| F4 | Yes, visually | Yes | Fully represented | Axes, plateau, truncated y-axis |
| T1 | Yes, visually/text | Yes | Fully represented | Every numerical cell and both footnotes |
| T2 | Yes, visually/text | Yes | Fully represented | Caption count and repeat inconsistency |
| T3 | Yes, visually/text | Yes | Fully represented | Combined-defense inconsistency |
| T4 | Yes, visually/text | Yes | Fully represented | Prose/table disagreement |
| T5 | Yes, visually/text | Yes | Fully represented | Scenario values and missing weights |
| E1 ASR | Yes | Yes | Fully represented | Denominator and granularity caveats |
| E2 Seed score | Yes | Yes | Fully represented | Undefined numerical coefficient |
| E3 UCB | Yes | Yes | Fully represented | Epsilon and coefficient unresolved |
| ALG1 | Yes, visually/text | Yes | Fully represented | Novelty guard and return ambiguity |
| ALG2 | Yes, visually/text | Yes | Fully represented | One/two-node rules, missing edge cases |
| ALG3 | Yes, visually/text | Yes | Fully represented | Ancestor visits and shared-ancestor ambiguity |
| Conceptual/method/system/empirical contributions | Yes | Yes | Fully represented | Priority claim not independently verified |
| Appendix A | Yes | Yes | Fully represented | Checkpoints and author-reported MIT availability |
| Appendix B.1 | Yes | Yes | Fully represented | Utility and updated checkpoint |
| Appendix B.2 | Yes | Yes | Fully represented | Additional baselines |
| Appendix B.3 | Yes | Yes | Fully represented | Scenario breakdown |
| Appendix B.4 | Yes | Yes | Fully represented | F4 |
| Appendix C | Yes | Yes | Fully represented | Three algorithms and formulas |
| Separate supplementary files | None supplied | Absence stated | Missing from supplied material | No separate artifact inspection claimed |

**Metadata retained:** Authors are Zhun Wang, Vincent Siu, Zhe Ye, Tianneng Shi, Yuzhou Nie, Xuandong Zhao, Chenguang Wang, Wenbo Guo, and Dawn Song. Affiliations are University of California, Berkeley; University of California, Santa Cruz; and University of California, Santa Barbara. The supplied venue is Findings of the Association for Computational Linguistics: EMNLP 2025, printed pages 23159–23172, November 4–9, 2025. Acknowledgements identify ARL Grant W911NF-23-2-0137 and state that author conclusions need not reflect supporting entities. Correspondence details, institutional superscripts, and publisher formatting are administrative rather than methodological evidence.

### Missing or inaccessible material

Page 10 has no supplied visual rendering, although all its extracted text is accessible. The complete small payload in Figure 1 is not confidently readable. No separate code, template corpus, benchmark files, execution traces, or supplementary artifact was supplied. No numbered figure, table, algorithm, or appendix referenced within this paper is missing from the available text/images. Repository availability statements do not mean repositories were reviewed.

### Uncertain interpretations

The unresolved issues are updated-o3-mini prose versus Table 4 values; 70% VWA-adv optimization versus 60% selected-prompt ASR; Figure 3 coverage versus global AgentDojo ASR; exact coverage aggregation; ALG1 suite/task granularity and explicit novelty test; ALG2 epsilon, coefficients, initialization and edge cases; ALG3 shared-ancestor visit handling; checkpoint identity in Table 5; and complete event-level evidence for the local case study's claimed consequences. Approximate plot points are labeled rather than treated as exact.

### Deliberately compressed material

Repeated abstract/introduction/conclusion statements are consolidated. Related-work citations and reference entries are compressed into source-reported categories; their external contents are not reviewed. Administrative correspondence, funding boilerplate, decorative icons, publisher formatting, and repetitive examples are compressed. All numerical table cells, substantive footnotes, experiments, algorithmic formulas, reported limitations, and meaningful visual trends remain represented.

### Potential omissions

No known supplied substantive inventory item is left unrepresented. This is an inventory-based coverage statement for the available paper, not a claim that compression preserves every sentence, that absent implementation artifacts were recovered, or that experimental claims were independently reproduced. Reporting ambiguities and inaccessible fine detail remain explicitly unresolved.

Version relationship: this published AGENTVIGIL paper and the previously summarized AgentFuzzer/AGENTVIGIL arXiv version belong to the same study family. Their overlapping results are not independent replication; the adaptive Repeat-defense result is version-specific evidence and must retain its separate protocol.

