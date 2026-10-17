# Stage 0 — Document Accessibility Report

The supplied work is **Mind2Web: Towards a Generalist Agent for the Web**, a dataset and benchmark paper with an exploratory language-model agent. It is not a paper titled 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis.' That phrase is the user's research question. Security relevance below is explicitly separated from the paper's own research objectives.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pages 1–24. |
| Accessible page count | 24; all numbered pages in this supplied document are represented. |
| Apparently missing pages | None within the supplied 1–24 sequence. This does not establish that every externally distributed artifact is present. |
| Directly inspected page images | Pages 1, 2, 4, 5, 6, 7, 8, 13, 17, 18, 19, 20, 21, 22, 23, 24. |
| Text-only page coverage | Pages 3, 9, 10, 11, 12, 14, 15, 16. Their supplied text was inspected; their page layouts were not visually inspected. |
| Figures | All numbered Figures 1–11 have supplied rendered pages and were visually inspected. Small screenshot text and individual plot labels have limited readability. |
| Tables | All numbered Tables 1–8 were inspected using supplied text and rendered pages. Table 8 continues onto page 24. The unnumbered artifact table on page 16 is text-only. |
| Equations | No numbered mathematical equations appear in the supplied work. Relevant mathematical operations and notation occur in prose. |
| Appendices | Appendix A Overview; B Data Collection Details; C Experiment Details; D Additional Results are present on pages 16–24. |
| Supplementary material | The in-document supplementary appendices are available. Linked dataset files, code, trained models, annotation training documents, video tutorial, and individual captured browser artifacts are not supplied. |
| OCR | Not performed. Supplied extracted text and direct image reading were sufficient for substantive analysis. |
| Other limitations | The source hash is user-supplied and was not independently recomputed. No tools, browsing, external citation validation, code execution, or reproduction was performed. |

The rendered images and extracted text agree on the principal tables, figures, and findings, with several source inconsistencies documented below. Extraction sometimes separates letters in Mind2Web or loses subscript formatting; the rendered title establishes the readable title used here. The failed local-image message for a path named '-' does not erase the sixteen images visibly supplied in the conversation.

**Evidence labels:** [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived from supplied quantities; [D] analyst interpretation. No [E] external information is introduced. Confidence is HIGH for clearly readable source statements, MEDIUM for bounded interpretations, LOW for weakly supported interpretations, and UNKNOWN where the work supplies no evidence.

# 1. Plain-language orientation

[A; pp. 1–3] This paper asks how to build a computer assistant that can receive an ordinary-language goal, open a website, and perform the necessary interactions. A user might ask it to find flights, locate a service, browse a collection of films, or open an appointment page. The challenge is to make one agent work across many websites, including websites it did not encounter during training.

The authors contribute **Mind2Web**, a collection of 2,350 human-demonstrated tasks from 137 real websites spanning 31 secondary domains. Each task contains a high-level description, a sequence of element-and-operation actions, and snapshots of the pages encountered. The authors also propose **MindAct**, a two-stage agent: a smaller language model ranks webpage elements, and a larger model chooses a promising element and predicts what operation to perform on it.

[A; pp. 7–8] The strongest reported Flan-T5 variant achieves 52.0% step success on new tasks associated with familiar websites, 38.9% on unseen websites, and 39.6% on held-out domains. These are per-step results, not rates of completing entire user requests. Whole-task success remains much lower: the corresponding Flan-T5 XL rates are 5.2%, 5.1%, and 2.9%. The best whole-task model also differs by condition; higher step success does not guarantee the best task success.

[D; security relevance, pp. 4, 10, 19, 23–24] For the user's security question, the important architectural observation is that a web agent combines language interpretation with externally supplied webpage content and executable operations. The authors explicitly discuss sensitive transactions, user control, CAPTCHA-related concerns, and possible malicious uses. However, they do not run attacks, define an adversary, measure prompt injection, or compare security vulnerability against standalone large language models. This work provides a grounded description of agent capabilities and deployment concerns, not proof of a comparative vulnerability claim.

# 2. Document roadmap

The paper has seven main numbered sections, references, and four supplementary appendices.

| Inventory ID | Original section | Pages | Role |
|---|---|---|---|
| S1 | 1 Introduction | 1–3 | Motivates generalist agents, states desiderata, introduces contributions and the explicit research question. |
| S2 | 2 Mind2Web Dataset | 3–5 | Explains dataset principles, task definition, collection, comparison with existing datasets, and research challenges. |
| S3 | 3 Method: MindAct | 5–6 | Describes candidate ranking and language-model action prediction. |
| S4 | 4 Experiments | 7–8 | Specifies generalization splits, preprocessing, metrics, baselines, and main findings. |
| S5 | 5 Related Work | 8–9 | Positions the work relative to web/mobile agents, automation, language models, grounded understanding, and tool learning. |
| S6 | 6 Limitations and Potential Societal Impact | 9–10 | Discusses representation, multimodality, dynamics, user interaction, evaluation, and safety. |
| S7 | 7 Conclusion | 10 | Restates dataset and method contributions and future directions. |
| A1 | A Overview | 16 | Maps supplementary sections and lists artifact links and licenses. |
| A2 | B Data Collection Details | 17–20 | Provides worker requirements, proposal procedures, demonstration controls, and verification. |
| A3 | C Experiment Details | 20–21 | Explains equivalent elements, model implementations, training hardware, and hyperparameters. |
| A4 | D Additional Results | 21–24 | Reports grouping variation, zero-shot results, matched GPT-4 subsets, and the example GPT prompt. |

References occupy pages 11–15. Acknowledgements begin on page 10 and continue on page 11. No keywords, formal hypotheses, theorem statements, or separately numbered algorithms are supplied. Figures 1–11, Tables 1–8, and the unnumbered artifact table form the visual and tabular inventory. All are accounted for later in this report.

# 3. Background and context

[A; pp. 1–6, 9] A **web agent** performs actions within a website rather than merely returning a written answer. A **large language model**, or LLM, processes language and is used here to interpret task descriptions and predict actions. A smaller **language model**, or LM, first reduces the number of webpage elements that the larger model must consider.

A webpage is represented partly by **HyperText Markup Language**, or HTML, which describes elements such as buttons, links, text fields, and selection controls. The **Document Object Model**, or DOM, organizes these elements into a tree. An element can contain other elements: a button, for example, may contain a text span. This creates an evaluation complication because selecting different nested elements can sometimes cause the same interaction.

**Grounding** means connecting a language instruction to a concrete element and operation in the environment. Knowing that a user needs to select a date is different from identifying the correct date control on an unfamiliar page. The paper distinguishes this environment-specific grounding difficulty from high-level task understanding.

A **high-level goal** describes the desired outcome without specifying each click. **Fine-tuning** trains a model on task-specific examples. **In-context learning** supplies examples within the input prompt without explicitly retraining the model. **Zero-shot** evaluation supplies no task demonstrations of that kind. **Out-of-distribution** evaluation tests environments that differ from the training coverage, operationalized here as unseen websites or held-out top-level domains.

[A; pp. 3–4] The agent receives the task description, the current webpage, and previous actions. Its output is a target element and operation, plus an argument when typing or selecting an option. The benchmark supports Click, Type, and Select Option. Hover and Press Enter are folded into Click in the final data.

The paper provides MHTML files containing webpage HTML, DOM snapshots with layout and style information, HAR files containing network traffic, and complete interaction traces. The paper names these formats and describes their roles; it does not expand MHTML or HAR in the supplied prose. Those external acronyms are therefore retained without importing definitions.

# 4. Research problem and gap

**Existing problem [A; pp. 1–3].** Generalist agents must work across a web too large for exhaustive training coverage. Real websites are complex, dynamic, and noisy, and useful tasks can require many interactions. A system restricted to simple commands on a small known website set does not meet the authors' goal.

**Shortcomings attributed to prior approaches [A; pp. 2, 5, 8–9].** The authors describe prior work as restricted to predefined websites, simplified simulated environments, narrow task types, or detailed user-provided action instructions. They also distinguish their setting from mobile applications, structured database or knowledge-base environments, and short-term tool invocation. These are the authors' literature characterizations, not an independently verified assessment of every cited system.

**Research gap [A; pp. 2–3].** The authors identify the lack of a suitable dataset for developing and evaluating agents that generalize across real websites and domains. A second practical gap is how to process large HTML documents without feeding every element into an expensive or capacity-limited LLM.

**Motivation [A; pp. 1, 9–10].** The proposed capability could make complex websites easier to use and let language models acquire information and carry out actions through website interfaces. Accessibility benefits are particularly emphasized for users unfamiliar with information technology or users with disabilities.

**Scope [A; pp. 3–10].** The study constructs an offline dataset from real websites and evaluates next-action prediction with recorded states and ground-truth histories. It explores language-model architectures and generalization, rather than online autonomous deployment or adversarial security. Real-world source websites do not imply unrestricted real-world evaluation.

# 5. Research questions, objectives, and hypotheses

**RQ1, explicit author research question [A; p. 1].** How can a generalist web agent, given any website, follow language instructions and carry out the corresponding tasks?

**O1, dataset objective [A; pp. 2–4].** Provide diverse real-world websites, realistic high-level goals, action demonstrations, snapshots, and interaction traces suitable for developing and evaluating such agents.

**O2, modeling objective [A; pp. 3, 5–6].** Explore whether a small ranking model followed by a larger action-prediction model can handle large webpage representations effectively.

**O3, experimental objective [A; p. 7].** Determine how well models generalize across tasks, websites, and domains.

**O4, auxiliary objectives [A; pp. 21–22].** Examine sensitivity to random candidate grouping, compare zero-shot and fine-tuned Flan-T5 XL behavior, and contextualize GPT-4 results using the same 50-task subsets.

No formal statistical hypotheses are stated. Expected advantages of diverse data and multiple-choice prediction are methodological motivations, not pre-registered hypotheses.

**User research question [D].** Why are web AI agents more vulnerable than standalone LLMs? This paper can inform the capability and deployment side of that question. It cannot establish that they are more vulnerable, quantify a difference, or identify an empirically validated attack mechanism. A comparative security answer remains outside the supplied evidence.

# 6. Assumptions / Threat Model

[A; pp. 1, 3–4] The authors treat websites as partially observable: current page content and action history are available, but complete future states are not assumed known in advance. The dataset is built around a user giving one task description at the start. MindAct processes the current page independently at each step with previous actions as context.

[A; pp. 7, 10] Evaluation assumes recorded webpage states and a ground-truth action history. Every step is evaluated independently. A full-task success score requires every recorded step to be correct, but this does not constitute a free-running live rollout with model-generated histories.

[A; pp. 18–19] Collection deliberately prepares websites by resolving pop-ups and CAPTCHAs, supplies anonymous accounts, resets altered values before recording, and avoids actual execution of selected consequential clicks. These choices support clean demonstrations and reduce disruption. They also define a narrower interaction environment than the full web experience.

**Security threat model: not specified.** The work does not define attacker capabilities, malicious webpage control, trusted prompt boundaries, secret-bearing components, attack success criteria, or a defense evaluation. It does not establish that its HTML pruning is a security sanitizer.

[D; pp. 4, 6, 19, 23–24] A security-oriented reading can identify places where website-derived content enters ranking and action-prediction inputs, and where predicted actions may affect a website. That is an architectural inference. The paper does not test whether an attacker can control those inputs or redirect the model. No attacker powers should be assumed from this source alone.

# 7. Methodology

## 7.1 Dataset design and instance structure

[A; pp. 3–4] Each instance has three components: a high-level task description, the demonstrated action sequence, and webpage snapshots. Each action is a pair consisting of Target Element and Operation. Type and Select Option require an additional value. Sequences can span multiple webpages.

The collection principles are direct engagement with real websites, diverse realistic tasks, and comprehensive snapshots and traces intended to support offline replay. Figure 2 illustrates a ten-action auto-repair review task, including location entry, search, filters, sorting, business selection, and opening reviews. Red actions identify transitions to new webpages; they do not mark attacks or model failures.

## 7.2 Website selection

[A; p. 4] The authors choose five top-level categories: Travel, Shopping, Service, Entertainment, and Information. These are divided into 31 secondary domains. Websites are selected for U.S. popularity using a ranking source named in the paper, followed by manual selection of approximately 3–5 representative websites per secondary domain, producing 137 websites. The ranking source was not independently accessed here.

## 7.3 Task proposal

[A; pp. 4, 17–18] Annotators receive a website description and sample tasks, and propose diverse realistic goals requiring multiple interactions. The authors generate 50 ChatGPT seed tasks per website and show ten randomly selected seeds to the annotator. Seeds serve as inspiration: copying or highly similar proposals are rejected. Table 3 requests concrete goals and mock information rather than low-level instructions.

For each proposal human intelligence task, or HIT, annotators may propose up to five additional tasks. The nominal proposal payment is $0.05, regardless of acceptance; successful demonstration of an accepted task receives the stated $0.80 reward. Websites stop being offered after approximately 20 collected tasks, aiming for balance and diversity. This is an approximate stopping target, not an exact count for every site.

## 7.4 Workers and ethics procedures

[A; p. 17] Workers must have at least 1,000 approved HITs and an approval rate exceeding 98%. Compensation is designed around an estimated hourly rate of $10.10. The paper reports consent, training documents, a video tutorial, qualification questionnaires and demonstrations, a secure remote sandbox, and instructions against entering private or sensitive information. It states that the study meets Institutional Review Board, or IRB, exemption criteria at the authors' institution. Actual worker counts, demographic distributions, measured hourly earnings, and qualification pass rates are not reported in the supplied material.

## 7.5 Demonstration and consequential actions

[A; pp. 18–19] A Playwright-based tool has a dialogue control window and a browser window. Workers first explore and practice without recording, close pop-ups, use anonymous accounts where needed, and then reset the website before demonstration. During recording, selecting an element highlights it while blocking the actual browser click. The worker separately chooses an operation, which the tool executes.

The interface supports Click, Type, Hover, Press Enter, Click (Fake), and Ignore. A click on an HTML select element is converted to Select Option, and the annotator chooses the value. Hover and Press Enter become Click in the final dataset. Ignore discards an accidental element selection.

Click (Fake) records a normal Click label without executing it. It is intended for actions with real-world side effects, such as posting comments or scheduling appointments. The authors suggest that a deployed model might request user confirmation before such actions. However, they also state that fake clicks are recorded like normal clicks; the supplied material does not explain how a model trained on those normalized labels would reliably recover the fake distinction at deployment.

## 7.6 Verification and retained data

[A; pp. 5, 17, 19–20] Authors screen proposed tasks, check demonstrations, discard low-quality tasks, remove extraneous actions, align task descriptions with actions, and standardize start/end conventions. Each demonstration is initially reviewed by an author; uncertain cases are re-evaluated by the first author. From 2,411 tasks, 61 are discarded, leaving 2,350. Among retained tasks, 390 descriptions are refined and 187 instances have extraneous steps removed. These revision groups may overlap; their sum is not the reported count of distinct modified tasks.

## 7.7 HTML preprocessing and candidate ranking

[A; pp. 6–7, 20] Heuristics retain visible elements with substantial semantic information based on attributes, text, and neighboring elements. Average element count falls from 1,135 to 580, with 94.7% training-data recall of target elements after this cleaning.

Candidate generation concatenates the task description and previous actions into a query. Each candidate representation includes its tag, text, salient attributes, and parent/child context. A cross-encoder jointly processes a query–element pair and produces a relevance score. The model uses DeBERTa-v3-base through Sentence-Transformers' Cross-Encoder implementation. The paper describes its base candidate model as having 86 million parameters.

Training uses positive target elements and randomly sampled negative webpage elements, a sigmoid-transformed score, and binary cross-entropy. Appendix C.1 clarifies that all acceptable equivalent elements are treated as positives in training and evaluation. Inference ranks webpage elements and keeps the top candidates. The ordinary candidate pool is top-50; GPT-4 uses top-10 under its stated budget restriction.

## 7.8 Action prediction

[A; pp. 5–6] The retained candidates and their neighbors form a pruned HTML snippet. MindAct casts element selection as multiple-choice question answering, or QA. Each input has up to five candidate elements and a None option. The model chooses an element and generates the operation and any value.

During training, ground-truth actions form output sequences for a left-to-right language-modeling objective. During inference, candidates are divided into groups of five. Selected candidates from different groups are regrouped until one remains or all groups select None. This is repeated elimination, not a single choice among all 50 elements in one prompt.

The direct-generation baseline generates the element itself from the snippet, together with operation and value. The classification baseline uses the candidate model for element selection and does not predict operations.

## 7.9 Splits, implementation, and metrics

[A; pp. 7, 20–21] Training contains 1,009 tasks from 73 websites. Cross-Task contains 252 tasks from 69 websites, formed by randomly taking 20% of remaining data after other holdouts. Cross-Website contains 177 tasks; its website-count wording is ambiguous and is examined in Section 14. Cross-Domain holds out Information and Service, containing 912 tasks from 73 websites.

Flan-T5 base, large, and XL use the Transformers sequence-to-sequence implementation. Candidate ranking trains for five epochs with batch size 32 and learning rate 3e−5. Flan-T5 generation and MindAct train for five epochs with batch size 32 and learning rate 5e−5. GPT-3.5-turbo and GPT-4 use temperature 0 and three demonstrations. Flan-T5 large and XL train on servers with four A100 80GB cards; other trained models use a single A6000 48GB card. Library versions, exact API snapshots, optimizer details, and numerical seed identities are not supplied.

Element Accuracy accepts equivalent elements. Operation F1 is token-level F1 and reduces to accuracy for Click; for Type and Select Option it also reflects argument correctness. Step Success Rate requires both the element and operation to be correct. Success Rate requires all steps of a task to succeed. Step-wise metrics are macro-averaged across tasks, giving each task equal weight in that average.

# 8. Experiments / Analyses

| ID | Experiment | Setup and purpose | Evidence and outcome | Important caveat |
|---|---|---|---|---|
| X1 | Candidate generation | DeBERTa base ranks elements across the three test splits; assess Recall@50. | p. 7: 88.9%, 85.3%, 85.7% for Cross-Task, Cross-Website, Cross-Domain. | Candidate recall is not final action correctness; it creates an upstream limitation. |
| X2 | Action formulation comparison | Classification, direct generation, and multiple-choice MindAct; Table 2. | MindAct with Flan-T5 base exceeds direct generation in every reported element and step comparison. | Classification reports no operation or success metrics. |
| X3 | Flan-T5 model variants | Base, large, XL trained with the task data; Table 2. | XL has highest step success among these variants in all three splits. | Large has higher Cross-Task and Cross-Domain whole-task success than XL. |
| X4 | Three generalization levels | Familiar-site new tasks, unseen sites, held-out domains; Table 2 and Fig. 6. | Cross-Task is strongest overall; unseen-site and unseen-domain performance are similar for several models. | GPT-3.5's highest step success is actually Cross-Domain, an exception to the prose's 'all models' claim. |
| X5 | GPT in-context learning | Three demonstrations; GPT-3.5-turbo and GPT-4. | GPT-4 improves substantially over GPT-3.5 in reported step success. | GPT-4 uses only 50 tasks per split and top-10 candidates; training regimes also differ from Flan-T5. |
| X6 | Random grouping sensitivity | Five runs with different random seeds for element grouping; Table 5. | All reported standard deviations are below one percentage point. | This is grouping sensitivity, not demonstrated variation across five independent full training runs. |
| X7 | Zero-shot Flan-T5 XL | Compare zero-shot with fine-tuned counterpart; Table 6. | Zero-shot row: 10.8, 7.8, 11.7; fine-tuned row: 52.0, 38.9, 39.6. | Caption labels element selection, but fine-tuned numbers match Table 2 step success rather than element accuracy. |
| X8 | Matched GPT-4 subsets | Other methods evaluated on the same 50 tasks per split; Table 7. | GPT-4 step success: 36.2%, 30.1%, 26.4%. | Matching tasks does not establish matching candidate budgets; subset ordering has exceptions to the prose claim. |

No attack experiment, defense ablation, standalone-LLM security baseline, significance test, or measured transaction-safety outcome appears in this register. Those absences matter for the user's research question.

# 9. Results

[A; Table 2, p. 7] MindAct with Flan-T5 base achieves element accuracies of 43.6%, 32.1%, and 33.9%, compared with 20.2%, 13.9%, and 14.2% for the direct-generation baseline. Corresponding step success is 41.0%, 29.5%, and 31.6%, compared with 17.5%, 11.0%, and 11.9%.

[C] The Cross-Task step-success difference between these base-model formulations is **23.5 percentage points**, calculated as 41.0 − 17.5. This is an absolute metric difference, not a 23.5% relative improvement. The evidence supports the multiple-choice formulation within the reported system; it does not isolate every implementation choice as a separate causal factor.

[A] Flan-T5 XL produces the strongest step success in Table 2: 52.0%, 38.9%, and 39.6%. Its element accuracies are 55.1%, 42.0%, and 42.1%. Its operation F1 scores are 75.7%, 65.2%, and 66.5%. Higher operation F1 than joint step success indicates that these metrics assess different requirements; a correct-looking operation is insufficient if the selected element is wrong.

[C] XL's Cross-Task to Cross-Website step-success gap is 52.0 − 38.9 = **13.1 percentage points**. Its Cross-Task to Cross-Domain gap is 52.0 − 39.6 = **12.4 percentage points**. Cross-Domain exceeds Cross-Website by only 39.6 − 38.9 = **0.7 percentage points** for this model. This narrow difference is consistent with, but does not prove, the authors' interpretation about website-specific grounding challenges.

[A] Whole-task success is low. Flan-T5 large scores 7.1%, 1.1%, and 2.7%; XL scores 5.2%, 5.1%, and 2.9%. Base scores 4.0%, 1.7%, and 1.6%. GPT-4 scores 2.0% in each 50-task subset. Because a task succeeds only when every step is correct, step-level performance should not be presented as practical end-to-end reliability.

[A; pp. 7–8, 22] GPT-4's Table 2 step-success scores are 36.2%, 30.1%, and 26.4%. GPT-3.5's full-set scores are 17.4%, 16.2%, and 18.6%. For the matched 50-task subsets, GPT-3.5 scores 15.2%, 15.1%, and 16.7%. Comparisons must preserve these different denominators and GPT-4's top-10 condition.

[A; p. 8] The authors interpret GPT-3.5's tendency to choose None as one possible failure mechanism. They suggest that a model may judge that a whole task cannot be completed on the current page when it should instead identify an intermediate action. This is a qualitative author analysis, without a reported count or frequency of that failure category.

[D] None of these success or failure rates is an attack success rate. They quantify benchmark task prediction under the paper's evaluation procedure, not adversarial susceptibility.

# 10. Figure-by-figure interpretation

## Figure 1 — Task and domain diversity, p. 2

[B] Six screenshot panels show flight-search tasks, a social-media task, movie browsing, and an appointment-page task. Panels a and b illustrate different tasks on the same website; a and c illustrate similar tasks on different websites; d–f illustrate more disparate tasks and environments. The lower portion is a colored treemap of domain coverage, not a performance plot.

The top-level shares are Travel 27.4%, Information 20.4%, Service 18.3%, Shopping 17.5%, and Entertainment 16.1%. Their displayed sum is 99.7%, calculated as 27.4 + 20.4 + 18.3 + 17.5 + 16.1; this is compatible with rounded displayed shares, but the source does not explicitly explain the rounding. Rectangular area visually encodes category share and color groups top-level domains. The denominator is not explicitly specified in the caption, so these are reported as domain-coverage percentages rather than independently asserted exact task fractions.

Readable secondary categories include airlines, restaurants, hotels, jobs, housing, social media, health, government, shipping, specialty shopping, music, sports, movies, and games. No axes or error bars are applicable. Tiny website screenshot content is not fully transcribed. The figure supports coverage diversity, not representative sampling of every web activity.

## Figure 2 — A dataset instance, p. 4

[B] The left column gives a task description and ten action pairs. The right column shows six selected page snapshots for Actions 1, 2, 5, 6, 9, and 10, with target HTML fragments. The task is to show reviews for the auto-repair business closest to location 10002.

The visible sequence enters 'auto repair', chooses Auto Repair, enters 10002, selects the location, searches, interacts with an accreditation switch and an SVG element, opens sorting, selects a business, and opens reviews. Actions 5 and 9 are red and the caption identifies red as a transition to a new webpage. This directly illustrates the three-component data structure and the need to predict intermediate actions. There are no quantitative axes, and the screenshot panels do not constitute an agent execution result.

## Figure 3 — MindAct pipeline, p. 6

[B] An HTML document yields candidate elements; the ranking LM selects top-k elements; these form an HTML snippet; the prediction LLM outputs Target Element and Operation. Task description and previous actions supply context. Arrows show the flow through ranking and prediction. The key architectural feature is the reduction of a large element space before final action selection. No confidence intervals or experimental values appear.

## Figure 4 — Candidate scoring, p. 6

[B] A candidate representation contains ancestor context and a target button associated with Boston. The task query contains the pickup-restaurant goal and prior actions. Both enter the ranking LM, followed by a classifier and a score shown in [0, 1]. This depicts pairwise query–candidate scoring. The score range is a classifier output range, not measured accuracy. Some small source text is clearer in supplied extraction than in the rendered image.

## Figure 5 — Direct generation versus multiple choice, p. 6

[B] A shared HTML snippet and pillow-protector task feed a prediction LLM. The direct-generation branch emits the selected element plus SELECT and Queen. The multiple-choice branch selects option C and emits SELECT and Queen. Its list includes None and five candidates. The figure clarifies that multiple choice constrains element selection while the operation and value are still generated. It is an illustrative output, not a measured trial.

## Figure 6 — Per-website step success, p. 8

[B] This is a vertical bar chart grouped left-to-right by Cross-Task, Cross-Website, and Cross-Domain. The y-axis is a fractional step-success scale; the x-axis contains individual websites. Colors indicate Travel, Shopping, Entertainment, Information, and Service. Only websites with more than three test tasks are shown. There are no visible error bars.

The chart visually shows considerable variation across sites and overlapping performance ranges for unseen-site and held-out-domain groups. Individual site names and exact bar heights are too small to read confidently. No exact per-site values are extracted, and the caption does not clearly identify the plotted model. The plot is used qualitatively, alongside the readable aggregate table, without inventing individual values or assigning an unstated model.

## Figure 7 — Annotation interface, p. 18

[B] A left dialogue/control pane sits beside a right browser pane displaying a flight website. The left pane contains task and operation controls; the right pane supports webpage navigation and element selection. The figure demonstrates the separation of annotation control from browser interaction, not a fully autonomous agent interface. Fine-grained screenshot text is compressed.

## Figure 8 — Demonstration workflow, p. 18

[B] Boxes flow from selecting website/task to exploring and preparing the website, task demonstration, operation selection, and task confirmation. A return connection depicts repeated element selection during demonstration. A completion route leads to confirming the task. The diagram makes preparation and recording distinct stages and depicts the repeated select-element/select-operation cycle.

## Figure 9 — Type operation dialogue, p. 19

[B] The dialogue identifies a selected destination element and asks for text to enter. 'New York' is visible as the value. This shows why Type requires an argument in addition to the operation label. It has no axes or performance interpretation.

## Figure 10 — Select Option dialogue, p. 19

[B] The dialogue identifies a selected Make combobox and presents vehicle-manufacturer options. One option is highlighted. The substantive point is selection of a permissible option rather than unrestricted typed text. The complete list is secondary interface detail and is compressed.

## Figure 11 — Verification tool, p. 20

[B] A left pane contains the task, action sequence, review controls, and comment area. A right pane shows a webpage with a red target highlight. Visible controls support keeping/removing actions and task-level review. The prose explains the 'unsure' route for re-evaluation. The figure demonstrates author review infrastructure; it does not independently measure reviewer agreement or error detection.

# 11. Table-by-table interpretation

## Table 1 — Dataset comparison, p. 5

[A/B] Columns give domain count, environment count and type, average elements, task quantity, instruction level, and average actions. Mind2Web reports 5/31 domains, 137 real-world websites, 1,135 average elements, 2,350 high-level tasks, and 7.3 average actions.

| Dataset | Domains | Environments | Average elements | Task quantity as printed | Average actions |
|---|---:|---:|---:|---|---:|
| MiniWoB++ | — | 100 | 28 | 100 | 3.6 |
| WebShop | 1 | 1 | 38 | 12,000 products | 11.3 |
| RUSS | — | 22 | 801 | 80 | 5.4 |
| PixelHelp | 4 | 4 | — | 187 | — |
| META-GUI | 6 | 11 | 79 | 1,125 dialogues | 4.3 |
| MoTIF | 15 | 125 | 188 | 756 | 4.4 |
| Mind2Web | 5/31 | 137 | 1,135 | 2,350 | 7.3 |

Dashes indicate unavailable or inapplicable entries, without further source clarification. Environment types and instruction types vary: this is not a uniformly controlled dataset ranking. In particular, products and dialogues should not be silently converted into comparable task counts. Mind2Web has the largest reported average element count in this table, but WebShop has a larger reported average action count.

## Table 2 — Main performance results, p. 7

[A/B] Each split reports Element Accuracy, Operation F1, Step Success Rate, and whole-task Success Rate. Values below are percentages or percentage-scaled metric scores as reported. Each cell follows that four-value order.

| Model | Cross-Task | Cross-Website | Cross-Domain |
|---|---|---|---|
| Classification | 26.8 / — / — / — | 21.6 / — / — / — | 24.5 / — / — / — |
| Generation | 20.2 / 52.0 / 17.5 / 0.0 | 13.9 / 44.7 / 11.0 / 0.0 | 14.2 / 44.7 / 11.9 / 0.4 |
| MindAct Flan-T5 base | 43.6 / 76.8 / 41.0 / 4.0 | 32.1 / 67.6 / 29.5 / 1.7 | 33.9 / 67.3 / 31.6 / 1.6 |
| MindAct Flan-T5 large | 53.4 / 75.7 / 50.3 / 7.1 | 39.2 / 67.1 / 35.3 / 1.1 | 39.7 / 67.2 / 37.3 / 2.7 |
| MindAct Flan-T5 XL | 55.1 / 75.7 / 52.0 / 5.2 | 42.0 / 65.2 / 38.9 / 5.1 | 42.1 / 66.5 / 39.6 / 2.9 |
| MindAct GPT-3.5 | 20.3 / 56.6 / 17.4 / 0.8 | 19.3 / 48.8 / 16.2 / 0.6 | 21.6 / 52.8 / 18.6 / 1.0 |
| MindAct GPT-4 | 41.6 / 60.6 / 36.2 / 2.0 | 35.8 / 51.1 / 30.1 / 2.0 | 37.1 / 46.5 / 26.4 / 2.0 |

GPT-4's row uses 50 tasks per split and top-10 candidates. Other ordinary experiments use the top-50 pool. Classification cannot predict actions, so its missing operation and success entries are not zero. XL has the highest element accuracy and step success in all three conditions. Base has the highest operation F1 in all three. Large has the highest Cross-Task whole-task success. XL has the highest Cross-Website and Cross-Domain whole-task success. No significance markers, confidence intervals, or run variability are reported here.

## Table 3 — Seed-task prompt, p. 17

[A/B] The table contains an airline website description, instructions for generating five varied practical goals, and sample responses. It asks for one-sentence tasks with concrete constraints and mock information, without step-by-step instructions or explicit target-element directions. The table documents a data-collection aid, not an evaluated agent prompt.

One sample calls a flight 'one-way' while also specifying a return date. That internal wording tension is preserved as an example-quality issue; it is not evidence that the contradictory sample was retained as a human-demonstrated dataset task. Sample responses are deliberately compressed rather than all repeated verbatim.

## Table 4 — Hyperparameters, p. 21

[A/B] DeBERTa-v3-base: batch size 32, five epochs, learning rate 3e−5. Flan-T5 base generation and MindAct base/large/XL: batch size 32, five epochs, learning rate 5e−5. GPT-3.5-turbo and GPT-4: temperature 0, three demonstrations. These rows specify reported settings; they do not provide complete reproducibility details such as optimizer, software versions, exact seeds, or dated API model revisions.

## Table 5 — Random grouping variation, p. 21

[A/B] The table gives mean ± standard deviation over five random-seed grouping runs.

| Model | Cross-Task step SR | Cross-Website step SR | Cross-Domain step SR |
|---|---:|---:|---:|
| Flan-T5 base | 41.5 ± 0.7 | 30.0 ± 0.8 | 31.3 ± 0.5 |
| Flan-T5 large | 49.9 ± 0.2 | 35.7 ± 0.5 | 36.7 ± 0.3 |
| Flan-T5 XL | 51.9 ± 0.8 | 39.5 ± 0.2 | 39.6 ± 0.2 |

All standard deviations are below one percentage point. XL has the largest mean in each condition. These are standard deviations, not standard errors or confidence intervals. Small grouping variation does not establish low uncertainty from dataset sampling, model training, or API changes.

## Table 6 — Zero-shot versus fine-tuned XL, p. 21

[A/B] The zero-shot row reports 10.8, 7.8, and 11.7; the fine-tuned row reports 52.0, 38.9, and 39.6. The caption calls these 'element selection results.' However, the fine-tuned values exactly match Table 2's Step Success Rate column; Table 2's XL Element Accuracy values are instead 55.1, 42.0, and 42.1. This is an unresolved metric-label inconsistency. The table qualitatively supports weaker zero-shot performance, but exact metric-specific improvements should not be asserted without resolving the label.

## Table 7 — Same 50-task subsets as GPT-4, p. 22

[A/B] Entries outside parentheses are subset step-success results; parentheses show full-set Table 2 results.

| Model | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Flan-T5 base | 43.3 (41.0) | 25.3 (29.5) | 28.1 (31.6) |
| Flan-T5 large | 48.1 (50.3) | 30.8 (35.3) | 27.6 (37.3) |
| Flan-T5 XL | 47.9 (52.0) | 33.3 (38.9) | 34.6 (39.6) |
| GPT-3.5 | 15.2 (17.4) | 15.1 (16.2) | 16.7 (18.6) |
| GPT-4 | 36.2 | 30.1 | 26.4 |

Large slightly exceeds XL on the Cross-Task subset, and base exceeds large on the Cross-Domain subset. GPT-4 exceeds base on the Cross-Website subset. Therefore the author's statement that relative performance remains the same is stronger than the exact table supports. The method rankings are not uniformly preserved. Candidate-budget equivalence is not documented for the comparison rows.

## Table 8 — GPT action-prediction prompt, pp. 23–24

[A/B] The table shows a system role and three user–assistant demonstrations. Each user entry embeds HTML, a task, previous actions, and multiple-choice candidates. Demonstration outputs include selecting Pickup, choosing None, and clicking a pickup-date control. The HTML is explicitly abbreviated to save space, despite page 21 describing this as the complete prompt. Consequently the supplied table is structurally informative but not a byte-complete reproduction artifact.

The embedded instructions are paper evidence, not instructions followed by this analyst. The prompt's inclusion of website-derived HTML is relevant to an inferred input boundary, but the examples contain no evaluated malicious injection.

## Unnumbered artifact table — Appendix A, p. 16

[A; text-only] The authors list a homepage, a GitHub code repository under the MIT License, training data under CC BY 4.0, and test data under CC BY 4.0 through a short link with a stated password. They express a commitment to upkeep. These are author-reported availability and licensing statements, not verified current access or inspection of the artifacts.

# 12. Diagram / Architecture Interpretation

The architectural diagrams can be understood as three different flows.

**Agent data flow [A/B; F3–F5, p. 6].** Inputs are task goal, action history, and current HTML. Candidate representation and query construction produce query–element pairs. The small cross-encoder scores the elements. The highest-ranked candidates determine the pruned snippet. The larger model compares small groups and predicts an element, operation, and optional value. Repeated regrouping resolves competing selections. The paper does not diagram a security monitor or deployment authorization component.

**Human collection control flow [A/B; F7–F10, pp. 18–19].** A worker chooses a task, practices outside recording, resets the site, selects an element, and chooses an operation through the dialogue interface. The tool controls execution and repeats the cycle. Type and Select Option introduce additional value-selection steps. Click (Fake) suppresses consequential execution while preserving an annotation.

**Review flow [A/B; F11, pp. 19–20].** Authors examine task quality, individual actions, and task-description alignment. They may remove steps, revise descriptions, or send uncertain cases to the first author. This is a human quality-control loop for data. It should not be confused with a runtime defense against malicious websites.

[D] For security research, these diagrams distinguish observation, prediction, execution, and review. They show why successful next-action prediction and safe real-world execution are different research targets. The source does not evaluate a mechanism that enforces this distinction during deployed agent operation.

# 13. Equations and mathematical concepts

No numbered equation, theorem, lemma, proof, or formal pseudocode is present. The following mathematical concepts are necessary to understand the method and evaluation, but their full formulas are not supplied and are not reconstructed as author equations.

**Step index t [A; pp. 5–6].** The current webpage is observed at step t, and context includes actions from the preceding t−1 steps. This describes sequential context, not a guarantee that the model predicts future page states.

**Top-k ranking [A; p. 6].** k is the number of highest-scoring candidates retained for action prediction. The ordinary experiments use 50; GPT-4 uses 10. A high-ranking error can remove the correct element before the larger model sees it.

**Sigmoid and binary cross-entropy [A; p. 6].** The relevance score is passed through a sigmoid activation and optimized against positive and negative candidate labels. The paper does not provide explicit symbols, loss weights, negative-sample counts, or a displayed loss equation.

**Left-to-right language-modeling objective [A; p. 6].** The action model learns to generate an output sequence using preceding output tokens. The paper specifies the objective family rather than an explicit mathematical expression.

**Recall@50 [A; p. 7].** Reported candidate recall assesses whether the relevant target survives within the top-50 set. Exact handling of multiple acceptable candidates for this calculation is not separately formalized in the supplied prose.

**Token-level Operation F1 [A; p. 7].** The metric evaluates operation-related tokens and values; Click reduces to accuracy. Exact tokenization and aggregation details beyond macro-averaging across tasks are not supplied.

**Joint step success [A; p. 7].** A step is successful only when its element and operation are both correct. **Whole-task success** requires all steps to be successful. The logical conjunction is stated, but no probabilistic independence assumption is given. Multiplying an average step success raised to 7.3 would therefore not be a justified estimate of actual task success.

**Mean ± standard deviation [A; p. 21].** Table 5 describes five grouping runs. Its uncertainty terms quantify that experiment's variability, not statistical significance.

**Derived consistency check [C].** Split counts sum to 1,009 + 252 + 177 + 912 = 2,350, matching the retained task count. Website counts should not be summed the same way because familiar websites can occur in both training and Cross-Task evaluation.

# 14. Interpretation and discussion

[A; pp. 7–9] The central empirical finding is that environment-specific grounding remains difficult even when language models can understand broad goals. Multiple-choice selection improves the evaluated agent over direct element generation, and unfamiliar websites lower performance relative to the familiar-site task condition. The authors interpret similar Cross-Website and Cross-Domain scores as suggesting that interface design and interaction logic matter more than domain-specific subject matter.

[D] That interpretation is plausible within the benchmark, but the design does not independently manipulate domain and website design while holding other factors constant. Only Information and Service are held out as entire top-level categories. Similar aggregate scores do not establish a general causal ranking of all sources of difficulty.

Several source consistency issues deserve explicit treatment:

| Issue | Source statements | Assessment |
|---|---|---|
| Cross-Website site count | p. 7 says '10 websites from each remaining top-level domain'; Cross-Domain uses 73 websites, training uses 73, and total coverage is 137. | The phrasing is difficult to reconcile with other counts under disjoint held-out-site assumptions. Do not silently rewrite it to ten total websites. |
| 'All models' strongest on Cross-Task | p. 8 prose; Table 2 GPT-3.5 step SR is 17.4 / 16.2 / 18.6. | GPT-3.5's Cross-Domain step score exceeds Cross-Task. The universal wording is unsupported by that row. |
| Zero-shot metric label | Table 6 calls results element selection, but fine-tuned values match Table 2 step SR. | Metric identity is unresolved. |
| Subset rankings | p. 22 says relative performance remains the same; Table 7 contains ordering changes. | Broad trends are similar, but exact ordering is not preserved. |
| Prompt completeness | p. 21 calls Table 8 the complete prompt; Table 8 says only part of the HTML is shown. | Prompt structure is available; full HTML content is not. |
| Fake-click distinction | p. 19 says fake clicks are recorded like Click, then discusses predicting Click (Fake). | The mechanism retaining or recovering this distinction is not explained. |

[C/D] If the 73 training websites and 73 Cross-Domain websites were disjoint, their sum would be 146, exceeding 137 before adding unseen-site websites. This arithmetic identifies a count tension; it does not determine the correct split membership. The supplied paper does not provide enough detailed website lists to resolve it.

[D; security synthesis] A web agent's described responsibilities extend from interpreting text to choosing actions in an outside environment. That can increase the consequences of an incorrect decision, especially for transactions or publication. It does not by itself establish greater likelihood of adversarial compromise than a standalone model. Comparative exposure, exploitation probability, and harm require separate evidence.

# 15. Contributions and novelty

**Dataset contribution [A; pp. 1–5].** Mind2Web combines real websites, broad domain coverage, high-level goals, and human action traces. The authors claim it is the first dataset for developing and evaluating generalist web agents. This priority claim is reported, not externally verified.

**Benchmark contribution [A; pp. 3, 7].** Three generalization settings distinguish new tasks, unseen websites, and unseen top-level domains. Metrics distinguish element selection, operation prediction, step success, and task success.

**Methodological and algorithmic contribution [A; pp. 5–6].** MindAct combines a small relevance ranker with larger-model action prediction and a multiple-choice formulation. The iterative grouping procedure permits selection from a larger pool through small choice sets.

**System and implementation contribution [A; pp. 4, 16, 18–20].** The work supplies an annotation approach, recorded webpage representations, quality-review infrastructure, and reported code/model availability.

**Empirical contribution [A; pp. 7–8, 21–22].** The paper reports comparisons of model formulation, model variant, generalization level, in-context learning, grouping variability, zero-shot behavior, and matched task subsets.

**Security contribution: limited [D; pp. 10, 19].** The work raises deployment safety concerns and uses fake clicks to avoid collection-time side effects. It does not contribute a formal threat model, attack benchmark, security theorem, or validated runtime defense. Its value for the user's project is architectural and contextual rather than direct comparative security evidence.

# 16. Limitations

## Authors' stated limitations

[A; pp. 9–10, 19] The dataset predominantly contains English-language websites used in the United States. MTurk annotators may be more proficient web users than the broader population, and the tasks represent only a subset of possible activities. The authors propose expanding countries, languages, demographics, accessibility needs, and professional domains.

MindAct uses textual webpage context even though visual information may be useful. It independently encodes each current page with previous actions rather than explicitly modeling environmental changes such as newly appearing menus. The user supplies a single initial goal; ongoing user corrections and agent clarification are not modeled.

Offline cached evaluation may produce false negatives when an alternative valid action was not recorded. Equivalent-element normalization addresses some within-page alternatives, but not arbitrary alternative task paths. The authors propose replay and eventual live evaluation, rather than reporting that these issues have already been solved.

Pop-ups and CAPTCHAs are intentionally omitted or cleared, although the authors acknowledge that they are significant parts of real web dynamics. Whole-task performance remains low, and GPT-4 operational cost is identified as a concern. Deployment safety requires attention to sensitive transactions, interpretability, transparency, user control, possible CAPTCHA circumvention, and misuse.

## Additional evidence-based analyst observations

[D] Ground-truth histories and independent step scoring limit what can be inferred about recovery from an agent's own mistakes. The dataset does not directly test adversarial content or standalone-model security. GPT-4 comparisons differ in task sample and candidate budget. Exact model snapshots, library versions, optimizer details, and numerical seed values are unavailable.

[D] Collection-time fake execution means recorded consequential actions are not direct demonstrations of successful real-world completion. Task descriptions may be adjusted to match demonstrations, so benchmark alignment partly reflects author revision. Neither point proves bias or invalidity; each narrows the meaning of the reported evidence.

[D] Source count tensions and metric-label inconsistencies limit precise reconstruction of particular results. The visually unreadable individual labels in Figure 6 prevent a trustworthy site-by-site numerical audit. No missing linked artifact is represented as reviewed.

# 17. Threats to validity

The validity categories below are analyst-organized [D]; the authors do not present this taxonomy as such.

**Internal validity.** MindAct and direct generation differ in output formulation, while GPT and Flan-T5 comparisons also differ in adaptation strategy. GPT-4 has a smaller candidate pool and task sample. Observed differences cannot all be attributed to model intelligence alone.

**External validity and generalizability.** Real websites provide broader environmental realism than the simplified alternatives described by the authors, but English/U.S. selection, MTurk participation, selected accessible sites, and only two held-out top-level domains constrain population-level conclusions.

**Construct validity.** Element Accuracy and Operation F1 measure components of action prediction. Strict recorded-path task success is different from live user-goal completion, and neither metric measures security vulnerability. Treating low task success as an attack rate would substitute a different construct without evidence.

**Ecological validity.** Pop-up preparation, CAPTCHA clearance, anonymous accounts, offline snapshots, and fake consequential clicks remove some deployment conditions. The data originate from real sites but the evaluated interactions remain curated and cached.

**Statistical conclusion validity.** Main results lack confidence intervals or significance tests. Five-run grouping standard deviations address a specific randomness source. Fifty tasks per GPT-4 setting provide limited evidence about stable rankings, and Table 7 already shows ordering changes.

**Reproducibility.** The paper names models, libraries, hardware, hyperparameters, and artifact licenses. Missing software versions, exact API snapshots, detailed candidate-budget parity, and split-count ambiguities remain. Linked resources were not accessed, so practical reproducibility was not tested.

**Security inference validity.** The architecture supports an exposure-and-consequence hypothesis, but no adversarial evaluation tests it. Attacker control, exploitability, secret access, and comparative vulnerability remain UNKNOWN from this paper.

# 18. Future work and open questions

## A. Explicit author proposals

[A; pp. 3, 9–10, 19] Integrate multimodal webpage information; use reinforcement learning with feedback from real websites; develop smaller specialized models for web understanding and action taking; model interaction dynamics; permit conversational user–agent interaction; expand language, country, demographic, and professional coverage; improve robustness to pop-ups and CAPTCHAs; explore cached replay and end-to-end live evaluation with human assistance; and develop protective measures for deployment risks and misuse.

## B. Analyst open questions

[D] How much does performance change when the agent receives its own mistaken action history rather than ground truth? Can it recover from an incorrect intermediate action? How should recorded-path evaluation credit alternate successful paths? Which component most limits performance when the correct element is removed by preprocessing or ranking?

[D; security relevance] How would malicious webpage content affect ranking, element choice, operation choice, or argument generation? What authorization boundary should govern transactions and publication? Can collection-time fake-click safeguards be translated into reliable runtime controls? How would matched standalone and tool-enabled models differ under the same adversarial inputs, permissions, and harm criteria? These questions are motivated by the paper's architecture and safety discussion, but are not answered or tested by it.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within this work |
|---|---|
| Mind2Web | Dataset of high-level goals, demonstrated actions, and captured real webpages. |
| MindAct | Two-stage agent that ranks elements and then predicts an action. |
| LLM / LM | Large language model / language model; models used for language-conditioned ranking or prediction. |
| HTML | HyperText Markup Language; webpage element representation. |
| DOM | Document Object Model; hierarchical webpage element structure. |
| Target Element | The webpage component selected for an interaction. |
| Operation | Click, Type, or Select Option in the final benchmark representation. |
| Value | Additional argument, such as typed text or a chosen option. |
| Grounding | Mapping a language goal to concrete actions in the current environment. |
| Cross-encoder | Model jointly processing a task query and a candidate element to score their match. |
| Logit | Pre-activation ranking score; the paper selects candidates with highest logits. |
| Sigmoid | Activation used to map candidate scores into the classifier range. |
| Binary cross-entropy | Reported training-loss family for positive/negative candidate matching. |
| Top-k | The k highest-ranked candidate elements; ordinarily 50, or 10 for GPT-4. |
| QA | Question answering; here a multiple-choice element-selection formulation. |
| None option | Choice indicating that the current candidate group contains no selected element. |
| Fine-tuning | Training model parameters using the task data. |
| In-context learning | Providing examples inside the prompt without task-specific parameter training. |
| Zero-shot | Evaluation without the corresponding demonstrations or task fine-tuning. |
| Recall@50 | Candidate-retention metric for the top-50 pool. |
| Element Accuracy | Correctness of choosing one of the acceptable elements. |
| Operation F1 | Token-level agreement for predicted operation and relevant value. |
| Step SR | Step Success Rate: correct element and operation together. |
| SR | Whole-task Success Rate: every evaluated step succeeds. |
| Macro average | Average giving each task equal weight for step-wise metrics. |
| Click (Fake) | Annotation-time recorded click that is not executed on the real website. |
| MTurk / HIT | Mechanical Turk / human intelligence task; platform and work unit for collection. |
| IRB | Institutional Review Board; paper reports exemption criteria compliance. |
| CAPTCHA | Security mechanism named by the paper; its acronym is not expanded in the supplied work. |
| t, t−1 | Current step index and number of preceding steps. |
| SD | Standard deviation; Table 5's measure of grouping-run variation. |
| MHTML / HAR | Named snapshot/network formats; acronym expansions are not supplied. |

# 20. Key numerical results

All page numbers below are physical PDF pages. Table-derived values were cross-checked against supplied rendered pages where available.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Retained tasks | 2,350 | tasks | After author verification | Author-reported | p. 5, T1 and verification |
| Initial tasks / discarded | 2,411 / 61 | tasks | Collection cleanup | Author-reported | p. 5 |
| Websites / secondary domains | 137 / 31 | counts | Full dataset | Author-reported | pp. 4–5 |
| Top-level domains | 5 | categories | Travel, Shopping, Service, Entertainment, Information | Author-reported | p. 4 |
| Average elements | 1,135 | elements/page | Before stated preprocessing | Author-reported | pp. 5, 7 |
| Average actions | 7.3 | actions/task | Dataset comparison | Author-reported | p. 5, T1 |
| Refined descriptions / cleaned instances | 390 / 187 | instances | Retained tasks; overlap unspecified | Author-reported | p. 5 |
| Training | 1,009 | tasks | 73 websites reported | Author-reported | p. 7 |
| Cross-Task | 252 | tasks | 69 websites reported | Author-reported | p. 7 |
| Cross-Website | 177 | tasks | Site-count phrasing unresolved | Author-reported | p. 7 |
| Cross-Domain | 912 | tasks | Information and Service; 73 websites reported | Author-reported | p. 7 |
| Split total | 2,350 | tasks | 1,009 + 252 + 177 + 912 | Analyst-derived | p. 7 |
| Post-cleaning average elements | 580 | elements/page | Heuristic HTML cleaning | Author-reported | p. 7 |
| Target recall after cleaning | 94.7 | % | Training data | Author-reported | p. 7 |
| Candidate model size | 86 | million parameters | DeBERTa base | Author-reported | p. 7 |
| Generation baseline model size | 220 | million parameters | Flan-T5 base | Author-reported | p. 8 |
| Recall@50 | 88.9 / 85.3 / 85.7 | % | Task / Website / Domain | Author-reported | p. 7 |
| XL step success | 52.0 / 38.9 / 39.6 | % | Task / Website / Domain | Visually readable | p. 7, T2 |
| XL whole-task success | 5.2 / 5.1 / 2.9 | % | Task / Website / Domain | Visually readable | p. 7, T2 |
| Large whole-task success | 7.1 / 1.1 / 2.7 | % | Task / Website / Domain | Visually readable | p. 7, T2 |
| Base versus generation step gap | 23.5 | percentage points | Cross-Task: 41.0 − 17.5 | Analyst-derived | p. 7, T2 |
| XL task-to-website gap | 13.1 | percentage points | 52.0 − 38.9 | Analyst-derived | p. 7, T2 |
| GPT-4 step success | 36.2 / 30.1 / 26.4 | % | 50 tasks/split, top-10 | Author-reported | pp. 7, 22 |
| GPT-4 whole-task success | 2.0 / 2.0 / 2.0 | % | Same restricted setting | Visually readable | p. 7, T2 |
| GPT demonstrations / temperature | 3 / 0 | examples / setting | In-context models | Author-reported | p. 21, T4 |
| Grouping experiment repetitions | 5 | runs | Different grouping seeds | Author-reported | p. 21, T5 |
| XL grouping mean ± SD | 51.9±0.8 / 39.5±0.2 / 39.6±0.2 | % / percentage points | Task / Website / Domain | Visually readable | p. 21, T5 |
| Zero-shot row | 10.8 / 7.8 / 11.7 | percentage-scaled score | Metric identity caveat | Visually readable | p. 21, T6 |
| Candidate learning rate | 3e−5 | training setting | Batch 32, five epochs | Author-reported | p. 21, T4 |
| Flan-T5 learning rate | 5e−5 | training setting | Batch 32, five epochs | Author-reported | p. 21, T4 |
| Worker threshold | ≥1,000 and >98 | approved HITs / % approval | Eligibility | Author-reported | p. 17 |
| Compensation target | 10.10 | USD/hour | Estimated design rate | Author-reported | p. 17 |
| Approved-task payment | 0.80 | USD/task | Successful final demonstration | Author-reported | pp. 17–18 |
| Proposal payment | 0.05 | USD/HIT | Regardless of acceptance | Author-reported | p. 18 |
| Equivalent-element manual check | 100 | instances | Cases with differing top-level element | Author-reported | p. 20 |

No approximate plot values are inserted into this numerical ledger. Full Table 2, Table 5, and Table 7 values appear in Section 11 rather than being redundantly repeated here.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Dataset covers diverse real web tasks. | 2,350 tasks, 137 websites, 31 secondary domains. | F1, T1; collection | pp. 2, 4–5 | HIGH for reported scope; not a claim of full web representativeness. |
| Agent actions require element grounding and operation choice. | Target Element–Operation pairs; values for Type/Select. | F2; task definition | pp. 3–4 | HIGH; concrete task structure. |
| Small ranking precedes larger-model prediction. | Candidate scoring, top-k pruning, multiple-choice action prediction. | F3–F5; X1–X2 | pp. 5–7 | HIGH for design; no security sanitation claim. |
| Multiple choice improves evaluated action prediction. | Base MindAct step SR 41.0/29.5/31.6 versus generation 17.5/11.0/11.9. | T2; X2 | p. 7 | HIGH within reported configurations; no significance test. |
| Unseen environments remain challenging. | XL step SR 52.0 versus 38.9 and 39.6. | T2, F6; X4 | pp. 7–8 | HIGH for metrics; causal interpretation MEDIUM. |
| Good step scores do not imply reliable full completion. | XL whole-task SR 5.2/5.1/2.9. | T2 | p. 7 | HIGH under strict offline recorded-step metric. |
| GPT-4 comparisons have restricted conditions. | Fifty tasks per setting and top-10 candidates. | T2, T7; X5/X8 | pp. 7, 22 | HIGH; cannot treat as full-set matched-budget comparison. |
| Random grouping has modest reported variation. | Five-run SD values all below one. | T5; X6 | p. 21 | HIGH for grouping variation; not global statistical certainty. |
| Offline evaluation can reject valid alternative paths. | Authors explicitly discuss uncached-action false negatives. | Evaluation limitation | p. 10 | HIGH as acknowledged limitation. |
| Consequential annotation clicks can be suppressed. | Click (Fake) records without executing. | B.3; collection | p. 19 | HIGH for collection mechanism; runtime mechanism unresolved. |
| Deployment creates safety concerns. | Transactions, user control, CAPTCHA concerns, malicious uses. | S6 | p. 10 | HIGH as author discussion; no measured exploit. |
| Architecture is relevant to agent security. | Webpage HTML enters prediction, and outputs specify actions. | F3–F5, T8 | pp. 6, 23–24 | MEDIUM analyst inference; comparative vulnerability UNKNOWN. |
| Standalone-model vulnerability comparison is absent. | Experiment inventory concerns task prediction/generalization only. | X1–X8 | pp. 7–8, 21–22 | HIGH within supplied document; no external extrapolation. |

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking a computer to find the right flight or appointment on a website without telling it every button to press. Different websites arrange their controls differently, so understanding your sentence is only part of the problem. The computer must also work out which button, field, or menu matches the next step.

The researchers collected thousands of examples of people doing tasks on real websites. Their agent first uses a smaller model to narrow down the possible controls. A larger model then chooses among those controls and decides whether to click, type, or select something. This works better in their tests than asking the model to generate the target element directly.

The agent still makes many mistakes. Its strongest reported model gets about half the evaluated steps right on familiar websites, and fewer on unfamiliar ones. Completing an entire task is much harder because every step must work. The tests also provide the correct previous actions, so they do not fully show what happens after an agent makes its own mistake.

For security, a web agent has responsibilities beyond writing an answer: it can interact with outside pages and potentially perform consequential actions. The paper discusses those concerns and avoids actually executing some sensitive clicks while collecting examples. But it does not test attacks or compare agents against standalone language models. It helps explain where security questions arise; it does not prove which system is more vulnerable.

# Completeness Audit

The denominator for coverage is the supplied 24-page document, its seven main sections, substantive subsections, four appendices, eleven figures, eight numbered tables, unnumbered artifact table, and eight distinct experimental analyses. 'Fully represented' means the substantive contribution of an item is explained, not that every word or screenshot pixel is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes, text and p. 1 image | Yes | Fully represented | Metadata below; abstract integrated into orientation and contributions. |
| S1 Introduction; RQ1 and desiderata | Yes, pp. 1–3 | Yes | Fully represented | Any website, real-world complexity, sophisticated interaction. |
| S2 Dataset principles | Yes, pp. 3–5 | Yes | Fully represented | Real sites, diverse tasks, snapshots/traces. |
| §2.1 Task Definition | Yes | Yes | Fully represented | Goal, action pairs, values, snapshots, history. |
| §2.2 Website Selection | Yes | Yes | Fully represented | Five/31 categories, popularity/manual selection. |
| §2.2 Task Proposal | Yes | Yes | Fully represented | Seed generation and human proposals. |
| §2.2 Task Demonstration | Yes | Yes | Fully represented | Two-stage interaction and tool. |
| §2.2 Task Verification | Yes | Yes | Fully represented | Discards, revisions, cleanup counts. |
| §2.3 Comparison and Challenges | Yes | Yes | Fully represented | Complexity, high-level planning, grounding. |
| S3; §3.1 Candidate Generation | Yes | Yes | Fully represented | Query, element context, ranking, training loss. |
| §3.2 Action Prediction | Yes | Yes | Fully represented | Choice groups, None, iterative selection, generation baseline. |
| S4; §4.1 Experimental Setup | Yes | Yes | Uncertain | Task counts preserved; website-count tensions disclosed. |
| §4.2 Preprocessing and Evaluation | Yes | Yes | Fully represented | Cleaning, recall, metrics, ground-truth histories. |
| §4.3 Candidate Generation Results | Yes | Yes | Fully represented | Recall@50 and model size. |
| §4.3 Action Prediction Results | Yes | Yes | Fully represented | Full main table and caveats. |
| §4.3 Three Generalization Levels | Yes | Yes | Fully represented | Universal prose exception disclosed. |
| §4.3 In-context Learning | Yes | Yes | Fully represented | GPT conditions and qualitative None behavior. |
| S5 Related Work: web/mobile agents and automation | Yes | Yes | Represented in compressed form | Literature categories and author positioning, not external validation. |
| S5 LLMs, grounded understanding, tool learning | Yes | Yes | Represented in compressed form | Principal distinctions retained. |
| S6 Data Diversity and Representation | Yes, text-only | Yes | Fully represented | Geography, language, annotator proficiency. |
| S6 Multimodal Information | Yes, text-only | Yes | Fully represented | Text-only agent versus available visual snapshots. |
| S6 Interaction Dynamics | Yes, text-only | Yes | Fully represented | Independent page encoding. |
| S6 Human–Agent Interaction | Yes, text-only | Yes | Fully represented | Single initial instruction limitation. |
| S6 Offline/Online Evaluation | Yes, text-only | Yes | Fully represented | Alternative-path false negatives and future live evaluation. |
| S6 Safety in Deployment | Yes, text-only | Yes | Fully represented | Safety discussion separated from attacks. |
| S7 Conclusion | Yes, text-only | Yes | Fully represented | Contributions and future directions. |
| Acknowledgements | Yes, text-only | Briefly | Represented in compressed form | Funding and thanks do not support empirical claims. |
| References [1]–[45] | Yes, supplied text; p. 13 image | Categories only | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries not independently checked or reproduced. |
| Appendix A Overview and artifact table | Yes, text-only | Yes | Fully represented | Licenses reported; artifacts unreviewed. |
| Appendix B.1 Crowdsourcing | Yes | Yes | Fully represented | Eligibility, payments, consent, qualification, review. |
| Appendix B.2 Task Proposal | Yes | Yes | Fully represented | HIT limits, reward, approximate per-site target. |
| Appendix B.3 Demonstration | Yes | Yes | Fully represented | Preparation, six interface operations, normalization, fake clicks. |
| B.3 Pop-ups and CAPTCHAs | Yes | Yes | Fully represented | Exclusions and author future direction. |
| B.3 Mitigating Disruptions | Yes | Yes | Fully represented | Non-executing consequential annotations. |
| Appendix B.4 Verification | Yes | Yes | Fully represented | Task/action/description review and uncertainty escalation. |
| Appendix C.1 Evaluation | Yes | Yes | Fully represented | Clickable ancestor/descendant equivalence; 100 manual checks. |
| Appendix C.2 Candidate and Action implementations | Yes | Yes | Fully represented | Named libraries and models. |
| C.2 GPT learning and training hardware | Yes | Yes | Fully represented | Three examples, GPU setups, missing versions. |
| Appendix D.1 Grouping | Yes | Yes | Fully represented | Five runs and complete Table 5. |
| Appendix D.2 Zero-shot | Yes | Yes | Uncertain | Metric discrepancy preserved. |
| Appendix D.3 Matched subsets | Yes | Yes | Fully represented | Complete Table 7 and ordering caveats. |
| F1 | Yes, visually | Yes | Represented in compressed form | Panels/top-level shares retained; full secondary treemap transcription compressed. |
| F2 | Yes, visually | Yes | Fully represented | Task, sequence, snapshots, red transitions. |
| F3, F4, F5 | Yes, visually | Yes | Fully represented | Architecture, candidate score, output formulations. |
| F6 | Yes, visually | Yes | Uncertain | Qualitative plot reading only; tiny labels/model attribution unresolved. |
| F7, F8 | Yes, visually | Yes | Fully represented | Interface and workflow. |
| F9, F10 | Yes, visually | Yes | Represented in compressed form | Operation/value purpose retained; repetitive interface text compressed. |
| F11 | Yes, visually | Yes | Fully represented | Verification interface and purpose. |
| T1, T2 | Yes, text and visually | Yes | Fully represented | Full quantitative rows retained. |
| T3 | Yes, text and visually | Yes | Represented in compressed form | Prompt criteria and sample contradiction preserved. |
| T4, T5 | Yes, text and visually | Yes | Fully represented | Settings and mean/SD values retained. |
| T6 | Yes, text and visually | Yes | Uncertain | Metric label not repaired. |
| T7 | Yes, text and visually | Yes | Fully represented | Subset/full-set values preserved. |
| T8 | Yes, text and visually | Yes | Represented in compressed form | Roles, three demonstrations, outputs and HTML truncation retained. |
| RQ1; objectives O1–O4 | Yes | Yes | Fully represented | Explicit question distinguished from inferred experimental organization. |
| Formal hypotheses | None found | Absence stated | Fully represented | No manufactured hypotheses. |
| X1–X8 | Yes | Yes | Fully represented | Separate experiment register and table interpretations. |
| Major equations/theorems | None found | Absence stated | Fully represented | Relevant mathematical concepts explained without invented equations. |
| Numbered algorithms/pseudocode | None found | Absence stated | Fully represented | Prose algorithm represented. |
| Dataset, benchmark, method, implementation, empirical contributions | Yes | Yes | Fully represented | Novelty claims attributed to authors. |
| Author-stated limitations | Yes | Yes | Fully represented | All identified limitation categories represented. |
| In-document supplementary appendices | Yes | Yes | Fully represented | A–D covered, with uncertainties above. |
| Linked datasets, code, models, browser artifacts | No | Availability only | Missing from supplied material | No file contents or execution reviewed. |
| Worker training document/video and detailed sandbox materials | No | Mentioned | Missing from supplied material | Referenced but not provided. |
| Attack experiments and standalone security comparison | Not present | Absence stated | Missing from supplied material | Not part of this paper's reported study. |

**Bibliographic metadata [A/B; p. 1].** Authors: Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su; affiliation: The Ohio State University. Venue: 37th Conference on Neural Information Processing Systems, NeurIPS 2023, Track on Datasets and Benchmarks. No separately supplied keywords are visible.

## Missing or inaccessible material

External dataset downloads, repository contents, trained model files, individual MHTML/DOM/HAR/trace files, annotation training documents, and the video tutorial were not supplied or accessed. Pages 3, 9–12, and 14–16 were read through supplied text only. Individual small plot labels and screenshot contents are not fully legible. There are no missing numbered pages in the provided text sequence.

## Uncertain interpretations

Unresolved points are the Cross-Website wording and website-count arithmetic; Table 6's metric identity; Table 7's claims of preserved rankings; the runtime interpretation of normalized fake clicks; Figure 6's individual values and plotted model; and the precise denominator of Figure 1's percentages. None is silently repaired.

## Deliberately compressed material

The bibliography, acknowledgements, repeated task examples, full seed-task response wording, tiny screenshot text, secondary treemap details, and abbreviated HTML prompts are compressed. Their roles are represented, while important quantitative tables, methodological conditions, limitations, and disagreements are retained. URLs in the artifact inventory are described as reported resources rather than treated as verified evidence of current availability.

## Potential omissions

No identified substantive section, numbered visual, numbered table, experiment category, or author-stated limitation in the supplied inventory is left entirely unrepresented. Exact secondary-domain percentages, individual website plot values, and full interface/prompt text are not all reproduced; those omissions are disclosed. The analysis is comprehensive for the supplied evidence at the stated level of compression, not a claim that every fact in every linked artifact has been preserved or verified.
