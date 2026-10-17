## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–12 and as rendered images for pages 1, 2, 3, 4, 6, 8, 10, 11, and 12. All twelve supplied text pages were inspected. The nine supplied images were also inspected directly, including the state-transition diagram, trajectory plots, product examples, result tables, and prompt tables. Pages 5, 7, and 9 have text-only coverage; their page layouts were not visually inspected. The reported twelve-page extent is consistent with the supplied material, but it does not independently establish that every artifact associated with the original publication is present.

The main text, Limitations, References, and Appendices A–E are present. The accessibility metadata did not detect appendix pages, but the actual supplied text explicitly contains Appendix A, Related Works; Appendix B, Experimental Details; Appendix C, Case Studies; Appendix D, Prompts used in our experiments; and Appendix E, Licenses. Content takes precedence over this detection result. Tables 1–8 and Figures 1–4 are supplied. Their substantive contents are readable, although small product-screen text and unlabeled bar heights cannot support exact numerical transcription. No separate supplementary files or embedded attachments are supplied. A referenced transfer-code repository and external function-calling guidelines were not inspected. No tools, browsing, or additional OCR were used.

The stray message about failure to read an image at '-' does not prevent inspection of the nine images actually supplied. No scientific content is attributed to that error message. The source digest is accepted as user-provided provenance; it was not independently recomputed.

Evidence labels throughout this report are: [A] AUTHOR-REPORTED, [B] DIRECTLY OBSERVABLE, [C] ANALYST-DERIVED, and [D] ANALYST INTERPRETATION. No [E] external information is introduced. Confidence describes fidelity to the supplied evidence, rather than certainty that the underlying scientific claim is universally true. HIGH applies to clearly readable statements and table entries; MEDIUM applies to qualified interpretations or incomplete methodological descriptions; UNKNOWN applies where the supplied work does not establish an answer. Source references use physical PDF page numbers.

## 1. Plain-language orientation

LASER: LLM Agent with State-Space Exploration for Web Navigation studies how a large language model, or LLM, can operate a shopping website to find an item matching a user's request. Unlike a model that only returns an answer, this agent repeatedly observes a web environment and chooses actions such as searching, opening an item, checking its details, returning to results, and selecting an item to buy. The central problem is recovering from imperfect choices while avoiding actions that do not exist on the current page. [A; pp. 1–3]

The researchers organize navigation into four states: Search, Results, Item, and Finish. Each active state has its own instructions and permitted actions. Rather than supplying example shopping journeys, the standard system supplies general instructions about what to do in each state. The agent generates a rationale, selects an action, observes the result, and repeats. It can backtrack and can retain previously inspected items as fallback choices. [A; pp. 2–3]

On 500 WebShop test instructions, LASER reports a 50.0 success rate and 75.6 reward, compared with 34.0 and 59.7 for the authors' GPT-4 ReAct rerun. Human-expert figures in the table are 59.6 and 82.1. On 100 instructions transferred to Amazon.com, LASER reports 62.0 success rate and 85.4 reward, compared with human figures of 65.0 and 88.2. These are task-performance results, not security measurements. Real purchases were prevented: the Amazon agent stopped when it decided to buy. [A; pp. 3, 5, 7–8]

The central contribution is an explicit state-and-action organization for an LLM shopping agent. It improves reported navigation performance and provides a clearer structure for recovery. It does not establish that actions are safe simply because they are permitted. For the research question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' the paper offers indirect architectural and deployment-risk evidence. It does not directly compare the security of agents and standalone LLMs, test adversaries, or measure attacks. [D; grounded in pp. 2, 5, 10–12]

## 2. Document roadmap

The paper is an empirical artificial-intelligence agent paper with a systems-oriented method and benchmark evaluation. It is neither a security experiment nor a theoretical proof paper. The title, authors, affiliation, abstract, introduction, and Figure 1 occupy p. 1. The authors are Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Wenhao Yu, and Dong Yu, affiliated with Tencent AI Lab, Bellevue, Washington. The visible version identifier is arXiv:2309.08172v2, dated 21 February 2024. No publication venue for this paper is established by the supplied title page. [A/B; p. 1]

Section 1 motivates recovery and state-dependent action constraints. Section 2, Methods, contains §2.1 Problem Formulation, §2.2 LLM Agent, §2.3 State Description, and §2.4 Action Space. Section 3 describes experiments. Section 4 gives results; §4.1 examines examples, function calling, trajectory length, and a different model. Section 5 concludes. The separate Limitations section on p. 5 materially qualifies deployment and generalization claims.

Appendix A positions LASER against prompting, planning, and multimodal agents. Appendix B supplies dataset size, reward details, action budget, and Amazon conversion/evaluation procedures. Appendix C classifies 30 development-set errors. Appendix D supplies Tables 4–8 containing prompts and action descriptions. Appendix E states licensing. References span pp. 5–7 and are compressed here to their role in the authors' argument; their cited works were not independently reviewed.

Inventory identifiers used for coverage are S1–S5 for the numbered sections; SS2.1–SS2.4 and SS4.1 for substantive numbered subsections; L1 for Limitations; A1–A5 for Appendices A–E; F1–F4 for Figures 1–4; T1–T8 for Tables 1–8; X1–X7 for distinct experiments or analyses; N1 for problem-formulation notation; C1–C5 for major contribution groups; and H1–H3 for informal hypotheses. There are no supplied numbered equations, theorems, lemmas, or formal pseudocode algorithms. A procedural reconstruction is given below and is explicitly an analyst organization of the authors' method.

## 3. Background and context

An LLM is the language model used to interpret observations and choose behavior. The paper's standard backbone is GPT-4-0613. A web agent surrounds that model with an environment, observations, permitted operations, navigation state, and execution history. The paper evaluates the whole arrangement rather than language generation in isolation. [A; pp. 2–3]

An observation is the representation of the current website situation presented to the agent. In the supplied prompts it includes the user's instruction, buttons, product names and prices, and, when relevant, options and product details. A state is a high-level category distinguished by observation structure. Different products can therefore share the Item state; the state is not a unique identifier for every page or product. [A; pp. 2, 10–11]

An action space is the set of operations available to the agent. A global action space makes all operations conceptually available at every stage; LASER instead exposes operations associated with the current state. Backtracking means returning to a previous stage, for example leaving an unsuitable product and revisiting search results. It does not mean undoing every real-world consequence. [A; pp. 1–2; D for the consequence distinction, p. 5]

In-context examples are examples placed in a prompt to demonstrate desired behavior without changing model parameters. Zero-shot LASER uses no such examples, but it still uses substantial human-authored instructions. One-shot LASER adds one example input-output pair to each prompt. Thus 'zero-shot' does not mean unconfigured, unassisted by human knowledge, or instruction-free. [A; pp. 4, 8]

Function calling is the action-selection interface used by the standard system: permitted actions are supplied as described functions, and the model selects a function with arguments. The alternative interface asks for JavaScript Object Notation, or JSON, text representing the selected action. The paper also uses Python dictionaries to describe available actions in this alternative. [A; pp. 3–4, 7]

A trajectory is the sequence of steps taken during a task. A backup strategy retains previously examined items and chooses one when the exploration budget is nearly exhausted. Sim-to-real transfer here means moving from the simulated WebShop environment to Amazon pages converted into the same observation format. It is not evidence that an arbitrary website can be handled without adaptation. [A; pp. 3, 7]

## 4. Research problem and gap

Existing problem: an agent can select a product that fails to match the request, encounter inadequate search results, repeat unhelpful actions, or attempt an operation unavailable on the current page. These errors prevent completion or reduce matching quality. [A; pp. 1–3]

Shortcomings attributed to previous approaches: the authors argue that example trajectories often show only correct forward progress. They therefore give little explicit guidance for unexpected mistakes or recovery. Providing enough trajectories to cover every situation may be costly or unrealistic. They also argue that a global action space increases difficulty and allows invalid choices. These are the authors' characterization of prior work, not an independently established account of the entire field. [A; p. 1]

Research gap: the authors seek an agent organization that explicitly tracks the kind of environment it is in, supplies relevant guidance, supports recovery, and narrows the current action set. Their approach provides high-level scenario knowledge directly rather than expecting the model to infer it from many low-level demonstrations. [A; pp. 2, 8]

Motivation: shopping requires comparing candidates and revising decisions, so a recoverable navigation process is preferable to treating every task as a single ideal path. Scope: finding a target item in shopping, primarily WebShop with a small Amazon transfer study. Order tracking, order history, arbitrary open-web tasks, and adversarial behavior are outside the evaluated scope. [A; pp. 3, 5]

Security relevance is analyst interpretation: observing website content and converting judgments into executable operations creates a consequential interaction loop. The paper explicitly recognizes that some real-world operations are difficult to recover from. It supplies evidence for consequences and control requirements, but not evidence that malicious web content successfully exploits the loop. [D; pp. 2, 5, 10–12]

## 5. Research questions, objectives, and hypotheses

The paper does not enumerate formal research questions. Its explicit objectives are to handle novel situations and mistakes, enable backtracking, prevent invalid state-specific actions, complete shopping instructions without in-context examples, and evaluate performance on WebShop and Amazon. [A; pp. 1–3]

The analysis asks informal experimental questions: whether adding examples helps; whether function calling improves action selection; how trajectory length relates to performance; whether the framework works with text-davinci-003; and what kinds of errors remain. These correspond to X3–X7 below. They are descriptive objectives rather than preregistered hypotheses. [A; pp. 4, 8]

H1: the authors hypothesize that adding an example can distract an agent that already understands the task through state-specific instructions. H2: they suggest that Amazon's stronger search engine likely explains its higher performance. H3: they hypothesize that a more effective retriever could address retrieval failures. These explanations are not separately controlled causal experiments. [A; pp. 3–4, 8]

The user's security research question is separate from the paper's objectives. The supplied work cannot answer whether web agents are more vulnerable than standalone LLMs, how much more vulnerable they are, or which attack classes explain a difference. It can inform a security analysis of state-dependent capabilities, external observations, histories, model judgments, and consequential actions. This relevance is [D], with MEDIUM confidence as an architectural inference and UNKNOWN confidence for any comparative vulnerability conclusion.

## 6. Assumptions / Threat Model

The operational system assumes a web environment E, a user instruction I, an initial observation, actionable observations, and a stopping state. It assumes that useful page structures can be manually grouped into a small collection of states and that each state can be given a suitable instruction and action set. The four-state shopping design is the concrete evaluated case. [A; p. 2]

The method assumes usable environmental controls and an observation representation that exposes relevant buttons and product information. Amazon transfer specifically converts pages into the WebShop format. The supplied paper does not explain every conversion rule, state-detection rule, argument validator, or execution wrapper. Those implementation details cannot be reconstructed from Tables 4–8 alone. [A; pp. 7, 10–12; D for the reconstruction boundary]

There is no explicit adversarial threat model. No attacker, protected secret, malicious page, trust boundary, credential attack, prompt-injection attack, or data-exfiltration experiment is specified. The evaluation treats observations as task information and judges whether the selected item matches the user's request. This absence concerns the supplied paper; it is not a claim that the system has no attack surface. [D; scope audit]

The authors do identify deployment risk: simulated actions are allowed, whereas real actions can have hard-to-recover consequences. Amazon trials therefore stop at a purchase decision. Additional human verification may be needed before high-stakes actions because success is imperfect. This is an explicit operational limitation, not a measured security defense. [A; p. 5]

Analyst distinction: an available action is executable in the current interface; an appropriate action satisfies the request; a safe or authorized action satisfies additional requirements. The paper measures the first two aspects in shopping and warns about consequences. It does not show that state-based availability establishes safety or authorization. [D; pp. 2, 5, 11–12]

## 7. Methodology

The study combines a manually structured agent, benchmark comparisons, transfer evaluation, ablations, trajectory analysis, and error annotation. No new model training is reported for standard LASER. Its core engineering choice is to put domain structure and guidance around an existing LLM. [A; pp. 2–4]

State construction: the authors manually categorize environments according to observation structure. Each state receives a generic layout with placeholders, a high-level goal, and detailed guidance. Search generates a query. Results assesses candidate relevance, pages forward, or returns to search. Item checks attributes, options, and detail views before buying or rejecting. Finish terminates the task. [A; pp. 2, 10–12]

Step inputs: state-specific system instructions, current observation, permitted actions, and past thoughts/actions. The user instruction supplies the overall goal. The agent first generates a thought or rationale, then selects an action based on it. The action can change the state or keep the same state. Execution repeats until Finish or a maximum budget. Table 7 documents the rationale-to-function stage. [A; pp. 2–3, 12]

Procedural reconstruction, labeled [D]: initialize Search; obtain an observation; choose the appropriate state prompt and actions; generate a rationale; select and execute an allowed action; update state, history, and inspected-item memory; continue until completion or invoke backup as the budget approaches exhaustion. This reconstruction organizes statements distributed across pp. 2–3 and 7. It is not supplied pseudocode and does not fill in missing code-level details.

Search guidance uses the instruction to generate relevant keywords. Results guidance encourages inspecting partial matches because item customization may resolve a mismatch. It discourages reopening already clicked items. Item guidance compares requirements with available options, checks Description, Features, or Reviews when useful, and discourages reopening information already supplied. These are human-authored behavioral instructions; the paper does not isolate their individual effects. [A; pp. 10–11]

Action implementation: standard LASER uses GPT-4-0613 function calling. Appendix B says the authors write a short description for each action and pass a list through the function-call argument. Table 8 omits additional function parameters. The alternative interface puts action dictionaries in the prompt and requests JSON output. text-davinci-003 uses that alternative because it does not support function calling in the reported setup. [A; pp. 4, 7, 12]

Backup memory stores items examined but judged non-matching. When the agent must stop, it selects one of these intermediate results. Appendix B sets a maximum of 15 state transitions and begins forced history selection if Finish has not been reached after 13 transitions, to remain within budget. The supplied material does not specify how fallback candidates are ranked or exactly how the remaining transitions are allocated. [A; pp. 3, 7]

Data: WebShop contains 1,181,436 items collected from Amazon shopping sites and human-annotated purchasing instructions with target items. The principal test uses 500 instructions. Ablations use 200 instructions because of limited computing budget. Amazon uses the first 100 WebShop test instructions. The error study uses 30 development-set error cases. These populations must remain separate. [A; pp. 3–4, 7–8]

Metrics: success means the selected/purchased item perfectly matches the target under the benchmark evaluation. Partial reward ranges from 0 to 100 and uses price, product category, hidden attributes, and customization options. The full reward formula is not supplied. Amazon selections are manually annotated for attribute, option, category, and price matches, then scored with the same WebShop functions. Price matches are 100% for both LASER and humans and therefore omitted from Table 2. [A; pp. 7–8]

Baselines: ReAct uses observations, thoughts/actions, and example trajectories; the original entry uses PaLM, whereas the authors rerun ReAct with GPT-4-0613. ASH adds observation summarization to ReAct. WebGUM fine-tunes FlanT5-XL on 1K human demonstrations. Human results are attributed to the WebShop authors. ReAct's original Table 1 entry is marked as a simplified setting. These are not fully matched training and prompting conditions. [A; pp. 3, 8]

Unreported configuration: hardware, temperature, random seeds, repeated-run counts, confidence intervals, significance tests, detailed instruction-selection rules, annotation agreement, and a complete execution implementation. No leakage control or exhaustive split construction is described in the supplied text beyond use of established test and development sets. [D; reporting audit]

## 8. Experiments / Analyses

X1 — Main WebShop comparison. Purpose: test whether the complete state-based agent performs better than reported navigation baselines. Setup: 500 test instructions, GPT-4-0613 LASER, state-specific instructions, function calls, and backup. Outcomes: success rate and reward. Table 1 reports LASER 50.0/75.6, no-backup LASER 48.4/71.2, GPT-4 ReAct rerun 34.0/59.7, original simplified-setting ReAct 40.0/66.6, ASH 30.2/56.7, WebGUM 45.0/67.5, and human expert 59.6/82.1. LASER leads the listed automated methods; humans remain ahead. No statistical uncertainty is reported. [A; p. 3]

X2 — Amazon transfer. Purpose: assess transfer to a live shopping environment. Setup: first 100 WebShop test instructions, Amazon pages converted to WebShop format, agent used as is within that interface, manual matching annotations, and stopping at the buy decision. Table 2 gives LASER/human success 62.0/65.0, reward 85.4/88.2, attributes 85.5/86.2, options 75.0/76.3, and type/category 97.0/99.0. Both achieve 100% price matches. The study evaluates item selection, not completed real purchasing. Conversion is a material condition on 'without modification.' [A; pp. 3, 5, 7–8]

X3 — Zero-shot versus one-shot. Purpose: see whether demonstrations improve the state-instruction design. Setup: 200 instructions; add one example input-output pair between instructions and current inputs for every prompt; otherwise preserve the agent. Table 3 gives zero-shot 52.0 success/77.6 reward and one-shot 50.0/74.9. The authors hypothesize distraction, but the experiment establishes a lower observed score in this setting rather than the cause or universal harm of examples. [A; pp. 3–4]

X4 — Function-calling ablation. Purpose: isolate the action-selection interface. Setup: the 200-instruction ablation setting; replace function-list selection with action descriptions as Python dictionaries and JSON text output. Table 3 gives 50.0/76.2 without function calls versus 52.0/77.6 standard LASER. The observed improvement is modest; no error decomposition or repeated-run uncertainty is supplied. [A; pp. 3–4]

X5 — Trajectory length. Purpose: characterize how many transitions tasks use and how performance varies across length groups. Figure 2 uses bins 3, 4–6, 7–9, 10–13, and 15. The pie labels show 75%, 9%, 5%, 2%, and 9%, respectively. The authors say the shortest common sequence is search-select-buy. Performance generally decreases for longer trajectories; the budget-exhausted 15-step group performs much worse but has non-zero success. Length is observed, not randomized, so the analysis does not establish that extra steps themselves cause failure. [A/B; p. 4]

X6 — Alternative model. Purpose: test adaptation to a less powerful non-chat LLM. Setup: text-davinci-003 with JSON action generation in the 200-instruction ablation study. Table 3 gives 38.5 success and 70.2 reward. The authors describe a large performance drop but conclude that the design can adapt to another model. Changing both the backbone and its interface complicates attribution. The statement that it still beats baselines also needs qualification because its success is below WebGUM's 45.0 and original ReAct's 40.0 in Table 1, and the tables use different evaluation sample sizes. [A/D; pp. 3–4]

X7 — Development-set error study. Purpose: understand residual failures. Setup: manual annotation of 30 development-set error cases. Categories: Item good enough, 9; Retrieval failure, 12; Missing details, 9. Figures 3 and 4 illustrate the first and third categories. The sample is composed of errors; these proportions cannot be interpreted as failure probabilities over all tasks. Sampling procedures and annotator agreement are unspecified. [A; p. 8]

## 9. Results

The principal supported result is stronger reported benchmark performance for LASER's combined design. On the main 500-instruction evaluation, LASER exceeds the GPT-4 ReAct rerun by 16.0 success-rate percentage points, calculated as 50.0 − 34.0, and 15.9 reward points, calculated as 75.6 − 59.7. Relative success improvement would be 16.0/34.0 × 100 ≈ 47.1%, a different quantity from 16.0 percentage points. These comparisons are [C], derived from Table 1, and do not isolate state tracking from all other design differences.

Against WebGUM, LASER gains 5.0 success-rate points, 50.0 − 45.0, and 8.1 reward points, 75.6 − 67.5. Against the original simplified-setting ReAct entry, the differences are 10.0 and 9.0. Because the original ReAct setting is explicitly different and model/training conditions vary, these are descriptive table comparisons, not perfectly controlled causal estimates. [C; p. 3]

Removing backup reduces success by 1.6 points, 50.0 − 48.4, and reward by 4.4 points, 75.6 − 71.2. Thus backup contributes to the observed overall result, while the no-backup system still exceeds every listed automated baseline on both Table 1 metrics. The no-backup condition gives zero score when budget runs out. [A/C; p. 3]

The WebShop human gap remains 9.6 success-rate points, 59.6 − 50.0, and 6.5 reward points, 82.1 − 75.6. The Amazon human gap is smaller: 3.0 and 2.8, from 65.0 − 62.0 and 88.2 − 85.4. These separate gaps support the authors' description of approaching human performance, especially in the transfer study, but do not establish equivalence or a statistical comparison between environments. [C; p. 3]

In the 200-instruction ablations, adding an example lowers success by 2.0 points and reward by 2.7; replacing function calling lowers them by 2.0 and 1.4. Switching to text-davinci-003 lowers them by 13.5 and 7.4. Operands are 52.0/77.6 versus 50.0/74.9, 50.0/76.2, and 38.5/70.2, respectively. These are [C], not author-supplied effect estimates with uncertainty.

The authors report 100% valid actions in the analysis discussion. This is a claim about action validity in their evaluated setup, not 100% task success, perfect product judgment, universal website support, or security. The 50.0 main success rate and remaining error categories make that distinction essential. [A; pp. 3–4, 8]

## 10. Figure-by-figure interpretation

### Figure 1 — State transitions and recovery

The directly inspected diagram on p. 1 contains four colored state circles: Search in orange, Results in blue, Item in turquoise, and Finish in green. Active states contain an 'LLM Agent' box. Arrows show search queries moving Search to Results, item selection moving Results to Item, and buying moving Item to Finish. Results has a next-page loop; Item has a detail-checking loop. Reverse routes include returning from Results to Search and rejecting an item to return to Results. [B]

A browsing-history component is shown below the Search/Results area, with a budget-related backup route associated with item selection. The exact low-resolution wording of the threshold annotation is not used to determine the budget; Appendix B supplies 13 and 15 transitions. The diagram's role is to make recovery paths and state-local decisions explicit. It is a conceptual control-flow diagram, not a measured graph, so axes, units, confidence intervals, and statistical markers do not apply. [B/A; pp. 1, 7]

The caption says the formulation enables backtracking and handling unfamiliar scenarios. That is an author interpretation of the architecture. The arrows directly demonstrate available recovery routes, but they cannot show how reliably the agent chooses them or whether a recovery action reverses an irreversible real operation. [A/B/D; pp. 1, 5]

### Figure 2 — Performance and trajectory-length distribution

The left panel is a grouped bar chart. Its horizontal categories are 3, 4–6, 7–9, 10–13, and 15 steps. Blue bars represent Rewards and green bars Success Rate. The vertical scale is linear, with visible ticks from 0 to 80. The figure does not label every bar with an exact value or provide error bars. Reward follows the benchmark's 0–100 scale; success rate is interpreted as a percentage. [B; p. 4]

Direct visual observations: blue reward bars exceed green success bars within each bin; shorter bins generally perform better; the 15-step group is distinctly lower on both measures. The shortest categories do not establish a perfectly monotonic relationship for every metric. Exact bar values are deliberately not reconstructed from graphical positions. Any such reading would be an approximate visual estimate, not a reported number. [B]

The right panel is a pie chart with the same trajectory bins. The visually readable labels are 75% for 3, 9% for 4–6, 5% for 7–9, 2% for 10–13, and 9% for 15. Color encodes category: blue, green, yellow-orange, red-orange, and magenta. The percentages sum to 100%, calculated as 75 + 9 + 5 + 2 + 9. Counts and rounding procedures are not printed. [B/C]

The authors connect the dominant three-step group to search-select-buy and the 15-step group to forced backup selection. They interpret non-zero success in that final group as evidence that some acceptable items were found but not recognized initially. The figure supports descriptive length-performance association. It does not include ReAct or ASH curves, so the claimed smaller degradation relative to those methods is not directly demonstrated by this visual alone. [A/D; p. 4]

### Figure 3 — Item good enough example

The inspected screenshot on p. 8 shows an instruction for a green table lamp for a living room, priced below 60 dollars, and a selected green lamp. The authors say it satisfies the instruction from their perspective but does not receive full benchmark credit. The caption reports reward 0.666. The exact tiny product details are not needed or confidently transcribed here. [A/B]

This is an illustrative case, not a distribution plot; no axes or statistical uncertainty apply. It supports the existence of disagreement between the authors' judgment of task satisfaction and benchmark scoring. It does not establish which hidden scoring component causes the disagreement or prove that every example in this category is acceptable to the user. The figure's 0.666 notation also differs from the 0–100 scale used for aggregate reward. [A/D; pp. 7–8]

### Figure 4 — Missing details example

The inspected screenshot on p. 8 shows a request for pink, closed-toe, size-nine women's high-heel shoes below 40 dollars. The selected footwear matches some requested details, but the authors state that it is not high-heel footwear. The caption reports reward 0.8. [A/B]

The example demonstrates partial matching despite a missed essential condition. It supports the authors' warning that many matching details can coexist with an important mismatch. The screenshot is not used to infer a failure frequency; the 9-of-30 category count comes from the case-study text. Tiny option labels and price fields are compressed rather than guessed. No axes, confidence intervals, or statistical comparisons apply.

## 11. Table-by-table interpretation

### Table 1 — Main WebShop comparison

Rows compare automated methods and a human expert. Columns are Success Rate and Reward. Values are: ASH 30.2/56.7; original ReAct 40.0/66.6; authors' ReAct rerun 34.0/59.7; WebGUM 45.0/67.5; LASER without backup 48.4/71.2; LASER 50.0/75.6; human expert 59.6/82.1. The original ReAct row has an asterisk indicating a simplified setting. [A/B; p. 3]

Humans are best overall, LASER best among listed automated systems, and ASH lowest on both columns. There are no ties, uncertainty intervals, missing entries, or significance markers. Boldface emphasizes LASER's values. 'LASER - backup' means removal of the backup strategy, not the backup strategy itself. Differences in models, training, and baseline settings limit causal comparability.

### Table 2 — Amazon transfer and human comparison

Columns are SR, Reward, Att., Opt., and Type. Appendix B/C text establishes attribute, option, and category matching as evaluation components; Type is interpreted as product type/category. LASER values are 62.0, 85.4, 85.5, 75.0, and 97.0. Human values are 65.0, 88.2, 86.2, 76.3, and 99.0. [A/B; pp. 3, 8]

Human figures exceed LASER in every displayed column. The derived gaps are 3.0 success points, 2.8 reward points, 0.7 attribute points, 1.3 option points, and 2.0 type points. Price is omitted because both attain 100% price matches. The table does not identify new human trial counts, annotation agreement, or uncertainty. It must be read with the 100-instruction conversion and no-real-purchase conditions.

### Table 3 — Ablations and another model

Rows are standard LASER, LASER + One-shot, LASER - function call, and LASER with text-davinci-003. Success/reward are 52.0/77.6, 50.0/74.9, 50.0/76.2, and 38.5/70.2. The caption identifies standard LASER as GPT-4 under zero-shot conditions. [A/B; p. 3]

The standard condition is best on both metrics. One-shot and no-function-call conditions tie at 50.0 success, but no-function-call has higher reward. text-davinci-003 is lowest. These are 200-instruction results, explaining why the standard row differs from Table 1's 500-instruction result. No statistical information establishes whether the small differences exceed run-to-run variability.

### Table 4 — Search-state prompt

The table contains a system instruction, observation template, user-instruction placeholder, and Search button. It asks the model to generate a rationale about its next action and use past rationale/action history when available. It demonstrates the form of explicit state guidance, not measured performance. Quoted prompt commands are treated as paper evidence, never instructions to this analysis. [A/B; p. 10]

### Table 5 — Results-state prompt

The observation template lists Back to Search, page counts, Next, item buttons, names, and prices. Guidance encourages inspecting potentially customizable partial matches and avoiding already clicked items. The output template ties the user's keywords to a candidate's matching keywords. Repeated item placeholders are deliberately compressed; the substantive behavioral rules are preserved. [A/B; p. 10]

### Table 6 — Item-state prompt

The prompt contains Back to Search, Prev, customization options, product details, Description, Features, Reviews, Buy Now, and target keywords/max_price. Guidance compares requirements and options, checks further information, rejects unsuitable items, and avoids repeat checks of information already present. The rationale template explicitly considers whether customization covers the requirements. [A/B; p. 11]

The layout exposes more capabilities than Table 8 fully enumerates: customization buttons and Back to Search are visible here, whereas Table 8's Item action row lists only five named functions. The function parameters are explicitly omitted, but the supplied paper does not fully explain this mapping. This discrepancy is retained as an unresolved implementation detail.

### Table 7 — Rationale-to-action prompt

The inputs are a current observation and next-action rationale. The instruction asks for one function call based on that rationale. It documents a separation between producing reasoning text and selecting an executable operation. It does not provide the complete function schema, parser, or validation behavior. [A/B; p. 12]

### Table 8 — State/action mapping

Search lists Search. Result lists select_item, Next, and Back_to_Search. Item lists Description, Features, Reviews, Buy_Now, and Prev. Finish has no listed action row. Each operation has a natural-language purpose or condition. Additional function-call parameters are omitted for brevity. [A/B; p. 12]

The table shows how state-specific action exposure supports executable navigation. It does not establish enforcement details or the correctness of argument values. Some descriptive conditions, such as buying only a perfectly matching item, still require model judgment. Its cited external implementation guidelines were not inspected. No performance units or statistical information apply to Tables 4–8.

## 12. Diagram / Architecture Interpretation

Figure 1 and Tables 4–8 together describe a feedback system with five conceptual components: environment observations, state identification, state-specific instructions, an LLM rationale/action stage, and execution/history management. A user instruction enters as the persistent goal. The current page representation enters as changing task evidence. The output is an action and ultimately a selected item. [A/B; pp. 1–3, 10–12]

Control flow follows the state graph. Search obtains results. Results can open a product, continue paging, or revise the search. Item can inspect additional details, return to Results, or finish via buying. Detail checks and pagination can keep the agent within a high-level state while changing its observation. Thus a state transition is not necessarily movement to a different named state. [A; p. 2; B; p. 1]

Information flow includes past thoughts/actions and a memory of inspected items. That history helps discourage repeated choices and supplies fallback candidates. The budget mechanism adds another decision path: if normal completion has not occurred by 13 transitions, the system forces history-based selection within the 15-transition cap. [A; pp. 3, 7]

The security-related architectural interpretation is that observations, history, rationale generation, function selection, and execution are distinct places where correctness matters. The supplied paper does not establish which component authenticates content, enforces permissions, or guards irreversible effects. Those are unanswered questions, not discovered vulnerabilities. The paper's explicit Amazon stopping rule is the only directly described intervention preventing a consequential real purchase. [D/A; p. 5]

## 13. Equations and mathematical concepts

There are no numbered equations, optimization objectives, proofs, or formal guarantees in the supplied paper. The mathematical content needed to understand the method is the notation in §2.1 and the arithmetic behind metrics and comparisons. [A; p. 2]

E denotes the web environment; I the user instruction; O0 the initial observation; {a0, a1, …, an} the action series; ai an individual action; Oi an observation produced when an action executes; and S the stopping state. The text uses S specifically for stopping, rather than defining it as the set of all states. No probability model or transition function is supplied. [A; p. 2]

The observation indexing is informal: the text says each ai produces Oi while also calling O0 the initial observation. A precise implementation might use a different index convention, but this report does not repair the source or invent a formally defined transition equation. The practical meaning is an alternating observation/action process ending in an output that is compared with a target. [D; p. 2]

Conceptually, success is a perfect benchmark match and reward grants partial credit based on price, category, hidden attributes, and options. The work does not supply weights or a full mathematical reward expression, so the aggregate scores cannot be independently recalculated from the report alone. [A; p. 7]

Analyst-derived comparison rules: absolute success difference equals one reported rate minus another and is expressed in percentage points. Relative improvement divides that difference by the baseline rate. Reward differences are reward points. For example, 50.0 − 34.0 = 16.0 percentage points, whereas (50.0 − 34.0)/34.0 × 100 ≈ 47.1% relative improvement. Neither computation is a significance test. [C; Table 1]

The figure captions report individual rewards as 0.666 and 0.8 while Appendix B specifies a 0–100 partial-reward scale. Multiplying those caption values by 100 gives 66.6 and 80.0, but that is only a possible [C] rescaling. The paper does not explicitly explain the scale conversion, so the original representations are preserved rather than silently substituted.

## 14. Interpretation and discussion

The evidence supports the practical usefulness of combining state guidance, state-local action sets, rationale-driven execution, and backup in the evaluated shopping environment. It does not isolate one component as the sole cause of the improvement. The principal comparison is between complete systems with multiple differences. [D; pp. 2–4]

The results address the objectives in different ways. Better Table 1 outcomes support improved task completion. Figure 1 establishes designed recovery routes, while the no-backup comparison quantifies one recovery-related mechanism. The reported 100% valid actions supports action feasibility in this setup. Table 3 shows that example-free instructions can outperform the tested one-example variation. Amazon transfer supports limited reuse across a normalized shopping interface. None of these tests proves handling of every novel situation. [A/D]

Consistency check: Table 1's LASER 50.0/75.6 and Table 3's 52.0/77.6 are different sample conditions, 500 versus 200 instructions, not an unexplained numerical contradiction. Appendix B's 13-transition trigger and 15-transition cap are also compatible: backup is initiated before the cap. Real Amazon purchase prevention qualifies language elsewhere about applying LASER 'without modification.' The navigation agent is reused, but page conversion and stopping at the buy decision are material evaluation conditions. [A/D; pp. 3–5, 7]

An unresolved claim is that text-davinci-003 LASER still achieves better results than baselines. Its reward 70.2 exceeds the automated Table 1 rewards, but its success 38.5 is below original ReAct 40.0 and WebGUM 45.0. Furthermore, sample sizes differ. Consequently, a blanket superiority claim on both metrics is not justified by these tables. [A/D; pp. 3–4]

Another qualification concerns 'significantly outperforms': the wording appears in the abstract and main text, but no statistical tests, p-values, confidence intervals, or repeated-run summaries are supplied. The report therefore treats this as the authors' description of substantial observed differences, not demonstrated statistical significance. [A/D; pp. 1–4]

The trajectory analysis is descriptive. Harder tasks may both require longer exploration and yield lower scores. The study does not randomize length. The suggestion that Amazon's stronger search explains higher scores is likewise plausible author interpretation, not a controlled comparison of search engines. [A/D; pp. 3–4]

For security research, the most useful distinction is between invalid operations, incorrect decisions, and consequential operations. LASER can constrain available actions while still choosing a mismatching product. A real purchase could turn that incorrect decision into a difficult-to-reverse outcome. This is a grounded risk pathway, but no adversary or standalone-model comparison is present. [D; pp. 4–5, 8]

## 15. Contributions and novelty

C1 — Conceptual contribution: represent interactive shopping as exploration among high-level observation-structure states, allowing backward as well as forward navigation. [A; pp. 1–2]

C2 — Methodological contribution: combine state-specific instructions with state-specific permissible actions, using generic observation templates instead of demonstration trajectories in standard LASER. [A; pp. 2, 10–12]

C3 — Agent implementation contribution: a thought/action process with GPT-4 function calling, execution history, intermediate-item memory, and budget-triggered backup. Some elements are adapted from existing approaches; the paper explicitly credits ReAct for the thought/action inspiration. [A; pp. 3, 7]

C4 — Empirical contribution: benchmark comparison, live-site transfer under converted observations, example and interface ablations, and an alternative-model result. [A; pp. 3–4]

C5 — Diagnostic contribution: trajectory distribution/performance analysis and a three-category annotation of 30 development errors. [A; pp. 4, 8]

No new dataset, benchmark, theoretical theorem, or security evaluation is introduced. Appendix A identifies Synapse as especially similar because it also uses state-conditional prompts, while distinguishing LASER's instruction-only approach from decomposition of few-shot examples. Planning and multimodal approaches are positioned as potentially compatible. These are the authors' novelty claims and literature relationships, not independently verified priority judgments. [A; p. 7]

## 16. Limitations

### Authors' stated limitations

Only target-item finding in shopping is evaluated. Common e-commerce activities such as tracking orders and checking order history are not covered. More complex instructions may require tools such as a knowledge retriever or calculator. [A; p. 5]

Possible states and descriptions require manual annotation. The authors therefore say the method may suit specific domains with a handful of states rather than open-world web agents. They suggest a hierarchy in which domain agents cooperate with a general agent. [A; p. 5]

Real-world deployment requires caution and testing because some actions have hard-to-recover consequences. Amazon trials stop when buying is chosen. Imperfect success may require human verification before high-stakes operations. [A; p. 5]

The ablation sample is restricted to 200 instructions because of computing budget. The error study identifies retrieval failures, overlooked details, and disagreements between benchmark credit and the authors' view of acceptable items. The latter are acknowledged failure-analysis findings rather than a formal general limitations theorem. [A; pp. 4, 8]

### Additional evidence-based analyst observations

No adversarial tests establish security robustness. No uncertainty estimates establish the reliability of small ablation differences. Reward definitions are described but not fully specified mathematically. Amazon evaluation depends on conversion and manual matching annotations, with no reported inter-annotator agreement. No completed purchase evaluation establishes end-to-end transaction reliability. [D]

The prompts contain substantial domain guidance, so the result should not be described as eliminating human expertise. The manual-state dependency and limited tasks constrain generalization. The alternative-model analysis changes the backbone and action interface, while comparisons to baselines cross sample conditions. Table 8 omits parameters and does not fully reconcile its Item actions with all Table 6 buttons. These observations concern evidential limits, not experimentally demonstrated failures. [D]

## 17. Threats to validity

The following labels are analyst classifications; the paper does not present a formal validity taxonomy.

Internal validity: the full LASER-versus-baseline comparison changes multiple components. It cannot assign all improvement specifically to state tracking or action restriction. Ablations more narrowly address examples and function calling, but run variability and matching details are not fully documented. [D; pp. 3–4]

Construct validity: benchmark perfect matching is not always identical to the authors' judgment of satisfying a user's request. Item good enough cases illustrate this discrepancy. Conversely, partial reward can credit a product that misses an essential requested property, as in the footwear example. Reward, success, action validity, and safety measure different constructs. [D; pp. 7–8]

External validity: four manually designed shopping states and normalized Amazon pages do not establish general open-web applicability. The first 100 test instructions are not described as a random sample, and live purchasing is excluded. [D; pp. 5, 7]

Statistical conclusion validity: no repeated runs, uncertainty intervals, significance procedures, or power analysis are supplied. The 200-case ablation differences should remain descriptive. The 30-error sample cannot establish population-wide category rates. [D; pp. 3–4, 8]

Ecological validity: Amazon provides a real website context, but observations are converted and the consequential transaction is stopped. The simulated benchmark permits actions that would require stronger controls in deployment. [A/D; pp. 5, 7]

Reproducibility: model identifiers, prompts, budget, sample sizes, and broad metrics are documented. Full function parameters, execution code, configuration, conversion behavior, and annotation protocols are not reproduced in the supplied paper. The external transfer repository is only a reference, not reviewed evidence. [D; pp. 7, 10–12]

Security validity: there is no measured comparison to a standalone LLM and no malicious-input condition. Therefore security superiority, vulnerability rates, or attack effectiveness cannot be inferred from task-performance scores. [D; document-wide scope audit]

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

Expand shopping capabilities to order tracking and order history; add a knowledge retriever or calculator for more complex instructions; develop hierarchical collaboration between domain-specific agents and a general open-world agent; combine LASER with planning/refinement approaches; integrate state-transition ideas into multimodal agents; investigate more effective retrieval; and examine self-feedback or verification for missed details. The authors also speculate that stronger future models could surpass human task performance. These are proposals, not implemented results. [A; pp. 4–5, 7–8]

### B. Additional open questions

How much of the benefit comes from action restriction, state descriptions, anti-repetition guidance, or the rationale/action separation? Does the benefit persist under repeated runs and matched baseline settings? How expensive is manual state construction? How are unexpected page structures handled? What causes the benchmark/author disagreement in Item good enough cases? [D]

For the user's security question: what occurs when observations contain deliberately misleading or instruction-like content? Which components enforce permissions independently of the LLM? Can permissible actions still violate the user's intent? How are high-stakes operations reviewed? Does history preserve misleading content across steps? How does a matched standalone LLM behave under the same adversarial inputs? These are analyst-generated research questions, not claims that the paper studied or demonstrated these mechanisms. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model used to interpret observations and select behavior. |
| LASER | LLM Agent with State-Space ExploRation, the proposed shopping agent. |
| NLU | Natural language understanding, mentioned as a broader model capability. |
| State | High-level category defined by observation structure, such as Search or Item. |
| State space | The set of categories through which navigation is organized. |
| Action space | Operations exposed to the agent in a particular state. |
| Observation | Current environment representation supplied to the model. |
| Backtracking | Returning to an earlier navigation stage to revise a choice. |
| Trajectory | Sequence of reasoning/action steps or transitions during a task. |
| Oracle trajectory | Demonstration in which correct actions are selected at every step. |
| In-context example | Prompt example demonstrating behavior without reported parameter training. |
| Zero-shot | No example input-output pairs; manual instructions are still present. |
| One-shot | One example input-output pair added for every prompt. |
| Function calling | Selecting an operation through a described function interface. |
| JSON | JavaScript Object Notation, used to represent actions in the text-output alternative. |
| Backup strategy | Choosing from previously examined items when the budget runs out. |
| WebShop | Simulated shopping environment and benchmark used for the main study. |
| Sim-to-real transfer | Applying the agent to Amazon pages converted to the benchmark format. |
| Success rate / SR | Rate of perfect target matching under the evaluation. |
| Reward | Partial-match score based on price, category, attributes, and options. |
| Att. / Opt. / Type. | Attribute, option, and product-type/category matching columns. |
| ReAct | Baseline that combines reasoning and acting; original and GPT-4 rerun entries differ. |
| ASH | Named summarization-based baseline; its acronym expansion is not supplied. |
| WebGUM | Named supervised baseline fine-tuned on human trajectories; expansion is not supplied. |
| UI | User interface, the controls through which an agent interacts. |
| Dev set | Development set from which the 30 annotated errors were selected. |
| E, I | Web environment and user instruction in §2.1. |
| O0, Oi | Initial observation and observations associated with action execution. |
| ai, n | Individual action and index delimiting the displayed action sequence. |
| S | Stopping state, as explicitly defined in §2.1. |

Names of referenced systems are preserved without inventing expansions or importing their external descriptions. 'Valid action' means an available state-appropriate operation in this paper; it must not be equated with a correct item choice or secure execution.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| WebShop inventory | 1,181,436 | items | Collected from Amazon shopping sites | Author-reported | p. 7, Appendix B |
| Main test sample | 500 | instructions | WebShop principal evaluation | Author-reported | pp. 3, 7 |
| Ablation sample | 200 | instructions | Limited computing budget | Author-reported | p. 4 |
| Transfer sample | 100 | instructions | First 100 WebShop test instructions | Author-reported | p. 7 |
| WebGUM demonstrations | 1K | trajectories | Human training demonstrations | Author-reported | pp. 3, 8 |
| State count | 4 | states | WebShop design | Author-reported | p. 2 |
| Maximum budget | 15 | state transitions | LASER | Author-reported | p. 7 |
| Backup trigger | 13 | completed transitions | If Finish has not been reached | Author-reported | p. 7 |
| ASH success / reward | 30.2 / 56.7 | % / reward points | Table 1 | Visually readable | p. 3 |
| Original ReAct success / reward | 40.0 / 66.6 | % / reward points | Simplified setting | Visually readable | p. 3 |
| GPT-4 ReAct rerun | 34.0 / 59.7 | % / reward points | Table 1 | Visually readable | p. 3 |
| WebGUM success / reward | 45.0 / 67.5 | % / reward points | Table 1 | Visually readable | p. 3 |
| LASER without backup | 48.4 / 71.2 | % / reward points | Main evaluation | Visually readable | p. 3 |
| LASER success / reward | 50.0 / 75.6 | % / reward points | Main 500 instructions | Visually readable | p. 3 |
| Human expert | 59.6 / 82.1 | % / reward points | WebShop comparison | Visually readable | p. 3 |
| Amazon LASER | 62.0 / 85.4 | % / reward points | Converted observations, no purchase execution | Visually readable | p. 3 |
| Amazon human | 65.0 / 88.2 | % / reward points | Cited human comparison | Visually readable | p. 3 |
| Amazon LASER attribute / option / type | 85.5 / 75.0 / 97.0 | matching scores | Manual matching evaluation | Visually readable | pp. 3, 8 |
| Amazon human attribute / option / type | 86.2 / 76.3 / 99.0 | matching scores | Human comparison | Visually readable | p. 3 |
| Amazon price matches | 100 | % | Both human and LASER | Author-reported | p. 8 |
| Standard ablation LASER | 52.0 / 77.6 | % / reward points | GPT-4 zero-shot, 200 instructions | Visually readable | p. 3 |
| One-shot LASER | 50.0 / 74.9 | % / reward points | 200 instructions | Visually readable | p. 3 |
| No-function-call LASER | 50.0 / 76.2 | % / reward points | 200 instructions | Visually readable | p. 3 |
| text-davinci-003 LASER | 38.5 / 70.2 | % / reward points | JSON interface, ablation setting | Visually readable | p. 3 |
| Valid actions | 100 | % of actions, as stated | Reported LASER setup | Author-reported | p. 4 |
| Length distribution | 75 / 9 / 5 / 2 / 9 | % | Bins 3 / 4–6 / 7–9 / 10–13 / 15 | Visually readable | p. 4, F2 |
| Error-study sample | 30 | error cases | Development set | Author-reported | p. 8 |
| Good enough / retrieval / missing details | 9 / 12 / 9 | cases | Within selected 30 errors | Author-reported | p. 8 |
| Error-category proportions | 30 / 40 / 30 | % of selected errors | 9/30, 12/30, 9/30 × 100 | Analyst-derived | p. 8 |
| Figure 3 reward | 0.666 | caption-scale reward | Lamp example | Author-reported | p. 8 |
| Figure 4 reward | 0.8 | caption-scale reward | Footwear example | Author-reported | p. 8 |
| LASER minus GPT-4 ReAct success | 16.0 | percentage points | 50.0 − 34.0 | Analyst-derived | p. 3, T1 |
| LASER minus GPT-4 ReAct reward | 15.9 | reward points | 75.6 − 59.7 | Analyst-derived | p. 3, T1 |
| Backup success / reward gain | 1.6 / 4.4 | percentage points / reward points | 50.0 − 48.4; 75.6 − 71.2 | Analyst-derived | p. 3, T1 |
| Amazon human success gap | 3.0 | percentage points | 65.0 − 62.0 | Analyst-derived | p. 3, T2 |

No exact bar-height estimates are included. Table 2's component headings do not explicitly print units; they are preserved as matching scores rather than silently assigned a more specific aggregation formula. Overall success is treated as a percentage, consistent with the task's success-rate reporting.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| State-based exploration supports designed recovery paths | Reverse transitions and state-local instructions | F1, T4–T8 | pp. 1–2, 10–12 | HIGH for architecture; no universal recovery guarantee |
| LASER leads listed automated WebShop methods | 50.0 success, 75.6 reward | T1, X1 | p. 3 | HIGH for reported values; unmatched baseline conditions |
| Backup contributes to scores | 50.0/75.6 versus 48.4/71.2 | T1, X1 | p. 3 | HIGH for comparison; uncertainty absent |
| Amazon item selection approaches cited human scores | 62.0/85.4 versus 65.0/88.2 | T2, X2 | pp. 3, 5, 7–8 | Converted observations, 100 instructions, no real buying |
| One example does not improve this ablation | 50.0/74.9 versus 52.0/77.6 | T3, X3 | pp. 3–4 | HIGH for scores; distraction mechanism untested |
| Function calling gives a modest observed benefit | 52.0/77.6 versus 50.0/76.2 | T3, X4 | pp. 3–4 | No repeated-run uncertainty |
| Another model can run the design with lower scores | text-davinci-003 38.5/70.2 | T3, X6 | pp. 3–4 | Success does not exceed every T1 baseline |
| Long trajectories associate with poorer performance | Length-group bars and distribution | F2, X5 | p. 4 | Descriptive, not causal; bars lack exact values |
| Retrieval and detail checking remain failure sources | 12 and 9 cases in selected 30 errors | F4, X7 | p. 8 | Error sample cannot give overall prevalence |
| Benchmark scoring may disagree with author judgment | 9 good-enough cases; lamp example | F3, X7 | p. 8 | Authors' assessment; hidden scoring cause unspecified |
| Manual states limit open-world applicability | Explicit domain-specific limitation | L1 | p. 5 | HIGH as an author-stated limitation |
| Real action consequences require deployment controls | Stop at buy decision; human verification warning | L1, X2 | p. 5 | Explicit caution; no security experiment |
| Architecture is relevant to agent security research | Observation-to-rationale-to-action loop | T6–T8, L1 | pp. 5, 11–12 | MEDIUM analyst inference; no attack evidence |
| Comparative standalone-LLM vulnerability is unestablished | No standalone-model security condition in evaluation | X1–X7 | pp. 3–5, 7–8 | HIGH confidence in scope boundary; comparative result UNKNOWN |

Source-grounded verification consisted of comparing the synthesis back against supplied page text and visible tables/captions: model and sample conditions were retained; the two LASER score sets were separated; reward scales were not silently merged; real purchasing was excluded; and the alternative-model claim was qualified against the table entries. This is an evidence cross-check, not an independently executed reproduction.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking a helper to find a very specific pair of shoes online. The helper searches, looks at several choices, opens a product, checks sizes and colors, and decides whether it fits your request. If it opens the wrong product, it needs to go back and try again. A language model that has only seen examples of perfect shopping trips may not know what to do when something goes wrong.

LASER gives the helper a small set of situations: searching, looking at results, examining a product, and finishing. Each situation has its own instructions and buttons. It also remembers products it has already looked at. This makes the process more organized and gives it a fallback when it runs out of steps. In the main shopping test it succeeds on 50.0% of instructions, better than the listed automated alternatives, but below the reported human score of 59.6%.

Being allowed to press a button does not mean pressing it is the right decision. LASER can still overlook an important detail, such as whether shoes actually have high heels. The researchers also recognize that a real purchase can have consequences, so their Amazon experiment stops when the helper decides to buy. It tests choosing an item rather than completing a real payment.

For your security question, this paper helps explain why an agent's mistakes can matter beyond the words it produces: it connects observations and judgments to actions in a website. But it does not test attackers or compare agent security with an ordinary language model. It gives useful ingredients for a security analysis, not proof that web agents are more vulnerable.

## Completeness Audit

Coverage is assessed against the supplied inventory, not against response length. All twelve extracted pages and all nine supplied rendered pages were inspected. Every supplied substantive section, figure, table, experimental analysis, contribution group, and explicit limitation is represented below. Missing implementation detail and external references remain unavailable rather than filled in.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/version/affiliation, p. 1 | Yes, text and image | Yes | Fully represented | Venue not established |
| Abstract, p. 1 | Yes | Yes | Represented in compressed form | Core contribution and claims preserved |
| S1 Introduction | Yes | Yes | Represented in compressed form | Motivation and prior-work criticism preserved |
| S2 Methods | Yes | Yes | Fully represented | Core agent design |
| SS2.1 Problem Formulation | Yes | Yes | Fully represented | N1 notation and indexing qualification |
| SS2.2 LLM Agent | Yes | Yes | Fully represented | Inputs, loop, rationale, stopping |
| SS2.3 State Description | Yes | Yes | Fully represented | Manual structural categories and prompts |
| SS2.4 Action Space | Yes | Yes | Fully represented | State-local actions and heuristic possibility |
| Thought/action and backup continuation, p. 3 | Yes | Yes | Fully represented | Distributed method content retained |
| S3 Experiments | Yes | Yes | Fully represented | Samples, models, baselines, transfer |
| S4 Results | Yes | Yes | Fully represented | Invalid-action examples and scores |
| SS4.1 Analysis | Yes | Yes | Fully represented | All four named analyses retained |
| S5 Conclusions | Yes | Yes | Represented in compressed form | Broad claims qualified against results |
| L1 Limitations, p. 5 | Yes, text only | Yes | Fully represented | Task scope, manual states, real consequences |
| A1 Appendix A Related Works | Yes, text only | Yes | Represented in compressed form | Taxonomy and closest comparison retained |
| A2 Appendix B Experimental Details | Yes; p. 7 text-only, p. 8 visual | Yes | Fully represented | Dataset, metric, budget, transfer, annotation |
| A3 Appendix C Case Studies | Yes | Yes | Fully represented | Counts, examples, proposed remedies |
| A4 Appendix D Prompts | Yes | Yes | Represented in compressed form | All T4–T8, repeated placeholders compressed |
| A5 Appendix E Licenses | Yes, text only | Yes | Fully represented | WebShop and ReAct reported MIT; research usage stated |
| References, pp. 5–7 | Yes; p. 6 visual | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries compressed to methodological roles; no validation |
| F1 State diagram | Yes, visually | Yes | Fully represented | Components, loops, recovery, history |
| F2 Left performance panel | Yes, visually | Yes | Represented in compressed form | Trends and axes; exact unlabeled heights uncertain |
| F2 Right distribution panel | Yes, visually | Yes | Fully represented | Five labeled proportions preserved |
| F3 Lamp example | Yes, visually | Yes | Represented in compressed form | Instruction, mismatch issue, caption reward |
| F4 Footwear example | Yes, visually | Yes | Represented in compressed form | Missing high-heel condition and reward |
| T1 WebShop results | Yes, visually and textually | Yes | Fully represented | Every row and footnote |
| T2 Amazon results | Yes, visually and textually | Yes | Fully represented | Every displayed value; omitted price explained |
| T3 Ablations | Yes, visually and textually | Yes | Fully represented | Every row; 200-case condition |
| T4 Search prompt | Yes, visually and textually | Yes | Represented in compressed form | Behavioral purpose and history |
| T5 Results prompt | Yes, visually and textually | Yes | Represented in compressed form | Customization and anti-repeat guidance |
| T6 Item prompt | Yes, visually and textually | Yes | Represented in compressed form | Options, detail checks, decision guidance |
| T7 Action prompt | Yes, visually and textually | Yes | Fully represented | Rationale-to-function interface |
| T8 State/action table | Yes, visually and textually | Yes | Fully represented | All named functions; omitted parameters flagged |
| X1 Main comparison and backup removal | Yes | Yes | Fully represented | 500 instructions |
| X2 Amazon transfer | Yes | Yes | Fully represented | First 100; conversion and stopping condition |
| X3 Example ablation | Yes | Yes | Fully represented | 200 instructions |
| X4 Function-call ablation | Yes | Yes | Fully represented | JSON alternative |
| X5 Trajectory analysis | Yes | Yes | Fully represented | Association and chart limits |
| X6 Alternative LLM | Yes | Yes | Fully represented | Backbone/interface and baseline qualifications |
| X7 Error annotation | Yes | Yes | Fully represented | 30 selected development errors |
| Explicit formal research questions | Not present | Absence represented | Missing from supplied material | Informal objectives preserved instead |
| H1–H3 informal hypotheses | Yes | Yes | Fully represented | Distraction, search strength, retrieval improvement |
| C1–C5 contribution groups | Yes | Yes | Fully represented | Conceptual, method, implementation, empirical, diagnostic |
| N1 notation | Yes | Yes | Fully represented | No invented transition equation |
| Numbered equations/theorems | Not present | Absence represented | Missing from supplied material | No mathematical proof objects supplied |
| Formal algorithm/pseudocode | Not present | Absence represented | Missing from supplied material | Analyst reconstruction explicitly labeled |
| Transfer-code footnote | Yes, reference text | Yes | Represented in compressed form | Repository not inspected |
| Function-guideline footnote marker | Yes | Yes | Uncertain | External contents not supplied; p. 12 marker visible |
| Separate supplementary material | Not supplied | Absence represented | Missing from supplied material | No attachments reviewed |
| Decorative formatting/contact details | Yes where supplied | No detailed transcription | Inspected but deliberately omitted as repetitive/non-substantive | No substantive argument depends on typography or email addresses |

### Missing or inaccessible material

There are no missing physical pages within the supplied 1–12 text sequence. Rendered images for pages 5, 7, and 9 are absent, so those pages have text-only coverage. The original PDF binary, referenced transfer repository contents, external function-calling guidelines, full function parameters, runtime implementation, and any separately hosted artifacts were not inspected. No separate supplementary files were supplied. No claim is made that such files do or do not exist elsewhere.

### Uncertain interpretations

Exact Figure 2 bar values are unlabeled. The small Figure 1 budget annotation is not used for exact threshold extraction. Fine print in product screenshots is not fully transcribed. Figure-caption rewards use a different representation from the aggregate scale without explicit explanation. The exact mapping of customization controls and Item-state Back to Search to Table 8 functions is unresolved. Observation indexing in §2.1 is informal. Type/category scoring is inferred from the supplied annotation description, but its complete aggregation is absent. The comparison asserting alternative-model superiority requires the qualifications described above.

### Deliberately compressed material

Repeated prompt openings, placeholder item lists, rationale-template syntax, bibliography entries, and tiny illustrative product fields are compressed. Related work is grouped into training, prompting, planning/refinement, and multimodal approaches. All eight tables retain their substantive purpose; all result-table values are retained. No referenced paper is summarized as if independently read. Appendix E states that WebShop and ReAct are released under the MIT License for research purposes and that the authors consider their experiments consistent with that intended usage; this is author-reported licensing information, not external verification.

### Potential omissions

No known substantive item in the supplied inventory has been left unaccounted for: each is represented, explicitly compressed, absent, or uncertain in this audit. This is a coverage statement about the supplied evidence. It does not establish completeness of unavailable code, undisclosed implementation details, external artifacts, or the original publication package. Comparative vulnerability of web agents and standalone LLMs remains unanswered by this paper.
