## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–29 and as 22 rendered page images: pp. 1–10, 12, 15, 17, 18, 20–23, and 26–29. All 29 pages therefore have readable textual coverage, but only those 22 pages have direct visual coverage. Pages 11, 13, 14, 16, 19, 24, and 25 were inspected through their supplied text only. The separate error concerning a local image named '-' does not prevent reading the images and text actually included in the prompt.

The main article, references, ethics statement, and Appendix A.1–A.12 are present. No page is apparently missing from the supplied 1–29 sequence. This establishes coverage of the supplied document, not independent verification that no other version or supplement exists. No supplementary files, executable benchmark artifacts, raw trajectories, participant histories, dataset files, or evaluation code were supplied. The paper advertises a project website and links an OSWorld repository; neither was accessed. No tools, browsing, external sources, or OCR were used.

Tables 1–5 are readable. Equation (1) is readable in the page image and extracted text. All numbered figures, 1–12, have supplied visual renderings. Their overall arrangements, plotted trends, annotations, and captions are inspectable. Small browser screenshots and interface text within montage figures are less readable than the surrounding captions and annotations. Consequently, this report distinguishes visually observed arrangements from details established by author-provided captions or extracted text. It does not claim independent verification of every pixel-level browser state.

The accessibility metadata's entry 'appendix_pages_detected: [3]' is not a reliable appendix inventory: the actual Appendix A begins on physical p. 15. Physical PDF page numbers are used throughout; they coincide with the printed page numbers here. Confidence is HIGH for readable textual statements and table entries, MEDIUM for qualitative visual interpretation where small embedded screenshots limit inspection, and UNKNOWN for unavailable execution artifacts or unresolved contradictions.

Source categories used below are [A] AUTHOR-REPORTED, [B] DIRECTLY OBSERVABLE, [C] ANALYST-DERIVED, and [D] ANALYST INTERPRETATION. No [E] EXTERNAL INFORMATION is introduced. Unless otherwise identified, descriptions of the study are [A]. All security relevance to the user's research question is explicitly [D] unless the paper's ethics discussion itself makes the claim.

## 1. Plain-language orientation

**Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks** studies whether artificial intelligence systems can carry out extended, realistic work across websites. The authors are Lawrence Keunho Jang, Jing Yu Koh, Daniel Fried, and Ruslan Salakhutdinov, from Carnegie Mellon University. Jang and Koh contributed equally. The supplied version identifies itself as arXiv:2604.24964v1, dated 27 April 2026; no publication venue for this paper is supplied on its title page.

A web agent does more than answer a question. It observes a computer screen, chooses actions, clicks, types, opens tabs, gathers information, and may create a document or spreadsheet. The paper asks how to evaluate this behavior when work spans many pages, multiple sites, and potentially hours. An example is planning a trip that combines flights, driving, hotels, restaurants, and a final itinerary.

The researchers construct 200 tasks using participant browsing histories as source material, author-written requests, and language-model-assisted expansion. They evaluate eight general computer-use models in virtual Ubuntu environments, primarily through Google Chrome. Instead of awarding only one overall pass/fail grade, they break each task into independently checked requirements called rubric items.

Under the main 100-step condition, Opus 4.6 achieves the highest perfect-task success, 44.5%, while GPT-5.4 achieves the highest reported Trajectory Efficiency, 1.15%. These refer to different outcomes: completing every required item versus obtaining rubric credit per model interaction step. Rubric-based automated evaluation agrees more closely with human annotations than the tested holistic trajectory judge. An appendix experiment materially qualifies the main result: giving Opus 200 steps raises reported perfect success to 76.5%.

The central contribution is a benchmark and evaluation method for extended computer-mediated work. This is not an adversarial security experiment. It does not directly compare web agents with standalone large language models, measure prompt-injection susceptibility, or estimate compromise rates. Its relevance to 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?' is indirect: it documents action capabilities, heterogeneous information sources, long execution chains, and unexpected browser/system strategies that a security analysis would need to consider.

## 2. Document roadmap

The inventory below is the denominator for the coverage audit, rather than a claim that length alone establishes completeness.

| Inventory ID | Original component | Location | Function |
|---|---|---|---|
| S0 | Abstract | p. 1 | Benchmark, rubric evaluation, headline success and efficiency |
| S1 | 1 Introduction | pp. 1–2 | Motivation and contribution framing |
| S2 | 2 Related Work | pp. 2–3 | Computer-use benchmarks and long-horizon agents |
| S3 | 3 The Odysseys Dataset | pp. 3–5 | Dataset construction and characteristics |
| SS3.1 | Collection Process | p. 3 | Participants and browsing journeys |
| SS3.2 | From Journeys to Odysseys | pp. 3–4 | Refinement, composition, task sources, difficulty |
| SS3.3 | Rubrics | p. 5 | Requirements, verification descriptions, judge |
| SS3.4 | Final Review | p. 5 | Conversational rewriting, privacy, two-pass QA |
| SS3.5 | Dataset Statistics | p. 5 | Task, rubric, length, and category counts |
| S4 | 4 Experiments | pp. 6–10 | Model evaluation and analysis |
| SS4.1 | Evaluation | pp. 6–8 | Human agreement and Trajectory Efficiency |
| SS4.2 | Results | p. 8 | Main 100-step comparison |
| SS4.3 | Analysis | pp. 8–10 | Difficulty, scaling, failures, surprising capabilities |
| S5 | 5 Conclusion | p. 10 | Implications and future directions |
| SE | Ethics Statement | p. 11 | Intended use, misuse, social impact, privacy |
| SR | References | pp. 11–14 | Cited literature; not independently validated |
| A1–A12 | Appendix A.1–A.12 | pp. 15–29 | Disclosures, construction details, prompts, scaling, interfaces, examples |

The numbered visual inventory is Figures 1–12, Tables 1–5, and Equation (1). There are no numbered algorithms, theorems, lemmas, or proofs. The composition and hard-task generation prompts function as procedural specifications, not mathematical algorithms with formal guarantees. No explicitly numbered research questions or hypotheses appear.

## 3. Background and context

A **large language model**, or LLM, is the model component that interprets instructions and selects responses or actions. A **computer-use agent**, or CUA, uses a model inside an observation/action loop to operate human-facing software. A **graphical user interface**, or GUI, consists of visible controls such as pages, buttons, tabs, and menus. These terms describe the paper's evaluated setting; they do not imply that all models have identical scaffolds or tools.

A **trajectory** is the sequence of observations and actions during a task. A **long-horizon task** requires sustained work over many steps and often across sites. The paper contrasts these with short, tightly scoped tasks, but does not provide a universally applicable duration threshold defining long-horizon capability.

A **rubric item** is one verifiable requirement plus instructions for checking it. A task might require an itinerary document, a particular comparison, and several supporting pages left open. **Averaged rubric score** gives partial credit across the task's items. **Perfect rubric score** is one only when every item passes. The distinction matters because substantial research can still leave a required deliverable unfinished.

An **LLM-as-a-judge** is an automated evaluator that reads the task and execution evidence. The tested Online-Mind2Web judge gives a holistic binary trajectory judgment. Odysseys instead issues a separate judgment for each rubric. A **step** in reported efficiency is a model call in the runner's observation/action loop, not necessarily a single mouse click or keyboard action.

The related-work discussion groups earlier work into synthetic interface tasks; operating-system, mobile, and enterprise environments; live-web trajectory evaluation; visual grounding; deep-research information synthesis; and long-horizon tool or workplace tasks. The authors position Odysseys as combining realistic multi-site workflows with GUI-level interaction and process evidence. These are the authors' characterizations of prior work, not an independently verified survey of the field.

## 4. Research problem and gap

**Existing problem [A]:** real browsing involves maintaining context, coordinating information across websites, decomposing goals, and deciding when to stop gathering information and produce an output. Short benchmark episodes do not adequately expose these demands (§1, pp. 1–2).

**Attributed shortcomings of previous approaches [A]:** the authors argue that many web benchmarks emphasize short-answer or single-site tasks; deep-research benchmarks often focus on final answers through text or application programming interface access; execution-based grading requires task-specific rules; and holistic LLM grading becomes unreliable as trajectories lengthen (§2–§3.3, pp. 2–5).

**Research gap [A]:** a realistic, live-web evaluation of extended, multi-site computer-use behavior, with informative partial-progress grading and explicit attention to efficiency.

**Motivation [A]:** an agent that eventually succeeds after an excessive number of interactions may still provide poor practical value. The authors report roughly 30 minutes for a 100-step Opus trajectory and use this to motivate measuring efficiency (§4.1, p. 7).

**Scope [A]:** 200 public-web-oriented tasks, general computer-use models, virtual Ubuntu environments, primarily Chrome, and automated rubric evaluation. Login-dependent source tasks are filtered. The ethics statement describes the intended actions as read-only or low impact rather than purchase completion or form submission (p. 11).

**Security boundary [D]:** operational difficulty and security vulnerability are different constructs. Failure to finish a spreadsheet is evidence of task unreliability, not evidence of an attacker gaining control. Browser source inspection and archive retrieval establish capabilities and alternative information routes, but do not by themselves demonstrate unauthorized exploitation.

## 5. Research questions / objectives / hypotheses

The paper does not state formal, numbered research questions or testable hypotheses. Its explicit objectives can be organized without inventing such declarations:

1. Construct realistic long-horizon, multi-site web tasks grounded in browsing behavior (§3).
2. Evaluate whether rubric decomposition provides more informative grading and greater human agreement than holistic trajectory judgment (§4.1).
3. Compare frontier API-based and open-weight computer-use models under a shared task environment and nominal step cap (§4.2).
4. Measure the relationship between success and interaction cost using Trajectory Efficiency (§4.1).
5. Analyze difficulty, step-budget scaling, characteristic failures, and unexpected successful strategies (§4.3; A.9).

The user's security research question is external to the paper's stated objectives. **Analyst framing [D]:** this source can inform what agents can observe and do, what environments they traverse, and where task-control failures occur. It cannot establish the comparative proposition that web agents are more vulnerable than standalone LLMs because it has neither a standalone-LLM control group nor adversarial conditions.

## 6. Assumptions / threat model

There is no formal attacker model, security asset inventory, exploit objective, trust-boundary specification, or adversarial evaluation protocol. Attacker capabilities and excluded attacks are therefore unspecified, not implicitly tested.

The operational environment gives models the full Chrome interface and the capabilities supported by the virtual machine. They may open tabs, save files, and sometimes use applications such as LibreOffice (§4, p. 6; §4.2, p. 8). Examples also show Python actions, clipboard use, terminal/API attempts, source viewing, and archive navigation. These capabilities should be attributed to the evaluated model/runner setting, not assumed for every possible web agent.

Construction assumes source browsing journeys can be transformed into coherent benchmark tasks while preserving useful real-user intent. It also relies on author review, LLM screening, live-site feasibility checks, and rubric verification. These are quality-control procedures, not proofs that every task remains feasible indefinitely.

Evaluation assumes screenshots and action histories contain sufficient evidence to judge requirements. The judge is instructed to avoid inventing state, require visible confirmation of filtering or sorting, and count blocking conditions as failure (A.8, p. 21). These instructions establish intended judging behavior; the human-agreement study provides empirical evidence about its performance.

**Security relevance [D]:** the environment joins external web information to consequential computer actions. The paper illustrates this connection, but does not measure whether malicious page content can override user instructions, cross permissions, steal data, or induce unauthorized actions. Those questions remain untested.

## 7. Methodology

### 7.1 Study design and source data

This is a mixed dataset/benchmark and empirical AI evaluation paper. It is not a training-method paper or security attack paper. The authors recruit 248 consenting participants in the United States and United Kingdom through Prolific. A desktop application reads Chrome history, segments activity using Chrome's Journey algorithm, and lets participants annotate their own journeys (§3.1, p. 3).

The annotation workflow asks participants to select a success-state URL, indicate an automation preference, write a task label as an AI request, and judge feasibility (A.2, p. 15; Figure 6). Collection yields 2,380 labeled journeys.

### 7.2 Refinement

An LLM screens label accuracy, feasibility without credentials or extra personal context, login requirements, and overall quality. It also proposes a refined label anchored to URL evidence. The screening judges 71.8% of original labels inaccurate relative to URLs. This is not a claim that 71.8% of participants lied: the authors explain that intentions, mixed goals, or underspecified descriptions may not match visible URL evidence (A.3, p. 16).

Authors manually review URL selections and feasibility, choosing an original, refined, or custom label. After exclusions, 696 usable journeys remain, reported as 29.2% of the original collection. Login-gated flows and low-quality or infeasible tasks are removed.

### 7.3 Composed tasks

Journey labels are embedded using text-embedding-3-small, reduced to 15 dimensions with UMAP, and clustered using HDBSCAN. The authors describe UMAP as preserving local/global structure and HDBSCAN as accommodating variable-density clusters and noise. Cluster centroids are connected by cosine similarity within a fixed but numerically unspecified range (A.4, p. 17).

For composition, a random seed cluster is selected; a one- or two-hop breadth-first search collects three to six related clusters; three to four journeys per cluster provide 12–24 candidate journeys. GPT-5.4 selects and orders a subset and generates the prompt, steps, transitions, rubrics, verification procedures, and coherence score.

The composition specification requires a unified goal, logical sequence, geographic consistency, at least two websites, and at least 30% of steps depending on earlier outputs. It requests exactly the target number of steps and permits rejecting incoherent combinations. These are generation requirements, not independently measured compliance rates.

Each source journey is used at most three times. Tasks are deduplicated and rejected if they span fewer than two sites, have incomplete rubrics, or score below 2/5 coherence. The final sources are 90 composed tasks, 30 author-written tasks based on personal queries, and 80 LLM-generated hard tasks. **Analyst-derived [C]:** 90 + 30 + 80 = 200.

### 7.4 Hard-task expansion

A.5 describes GPT-5.4 expanding source journeys into plausible multi-hour workflows, rejecting artificial complexity and preserving the broader decision goal rather than literal URLs. A GPT-5.4 judge filters candidates for artificiality, brevity, vagueness, staleness, and rubric mismatch; salvageable rejections receive one retry. It reports 567 viable candidates and a human-reviewed shortlist of 80 (pp. 18–19).

There is an unresolved source-count issue: A.5 calls its input '2,380 refined journeys,' whereas A.3 reports only 696 usable journeys after refinement. The supplied material does not establish whether A.5 intentionally uses a broader label-refined pool, uses all raw seeds, or contains a terminology error.

The hard-task prompt requires five to seven rubric items, weights summing to 1.0, both substantive output and browser evidence, no hidden deliverables, exact matching of requested quantities, and durable future-relative wording for time-sensitive requests. These specifications are compressed here rather than reproduced in full.

### 7.5 Final rewriting and review

Prompts are 'CUAfied': rewritten as natural user requests with concrete sites and parameters, first-person motivation, connected steps, and visible browser evidence such as open tabs or comparisons. Rubrics, dependencies, steps, and deliverables are regenerated to match (§3.4, p. 5).

Two-pass review checks coherence, journey provenance, unambiguous actionable rubrics, and privacy; then an LLM-assisted web check examines accessibility and feasibility, with human adjudication of flagged issues. Prompts exposing personally identifiable information are rewritten or removed. No raw browsing histories are released (p. 11).

### 7.6 Dataset and evaluation configuration

The final set contains 45 easy, 46 medium, and 109 hard tasks. Instructions average 272.3 words, median 277.5, range 76–387. There are 1,225 rubric items, mean 6.1 per task, median six, range three to twelve. The paper reports 22 top-level domains and 88 fine-grained SimilarWeb categories, averaging 1.9 categories per task, up to three. In this statistics context, 'domains' appears alongside topical categories and should not automatically be treated as a count of website hostnames.

Models use their recommended computer-use settings and official OSWorld implementations, which vary by model. The common environment is virtual Ubuntu, primarily Chrome, with maximum reasoning effort where available and a main cap of 100 model-loop steps. A.7 says runs start at google.com; §4.2 allows a provided task starting URL if any. No hardware specifications, full package versions, random seeds, repeated-run protocol, or full per-model hyperparameters are supplied.

The rubric judge is gemini-3.1-flash-lite-preview. Each call receives one rubric, its verification description, the task for context, the full action history, and chronological screenshots. It produces a rationale and binary verdict. The paper reports averaged and all-items-perfect task scores. Weight fields appear in interfaces and prompts, but the precise relationship between weights and the reported averaged metric is not explicitly formulated.

## 8. Experiments / analyses

| ID | Purpose and conditions | Evidence and principal outcome | Important qualification |
|---|---|---|---|
| X1 | Compare automated grading with human annotation | 120 Opus 4.6 trajectories; Table 3; rubric-average κ 0.788 versus holistic κ 0.508 | Rubric-pair denominator is unclear; only Opus trajectories are identified |
| X2 | Compare eight models on the benchmark | Main 100-step setting; Table 2; Opus perfect 44.5%, GPT-5.4 33.5% | Model-specific scaffolds vary; not a pure architecture-only comparison |
| X3 | Examine success versus interaction efficiency | Equation (1), Figure 3; GPT-5.4 efficiency 1.15% | Steps count calls, and action batching differs |
| X4 | Compare task difficulty | Figure 5 and Table 4; Opus perfect 97.8/71.7/11.0% across easy/medium/hard | Difficulty groups differ in content as well as nominal complexity |
| X5 | Examine success achieved over 0–100 steps | Figure 4; little perfect success in first approximately 15 steps, gains thereafter | Caption wording mixes perfect rate and mean rubric score |
| X6 | Identify failures and emergent strategies | §4.3; Figures 2, 10–12 | Qualitative examples and reported counts, not causal interventions |
| X7 | Increase budget to 200 steps | A.9; Figure 8; Opus 76.5% full-set success, Qwen 1/76 on matched hard subset | Different subsets and several arithmetic/reporting inconsistencies |

X1 uses Cohen's κ, precision, recall, F1, and accuracy. The supplied text does not report annotator overlap, inter-human agreement, a sampling protocol for the 120 trajectories, or uncertainty intervals for these metrics.

X2 evaluates general computer-use models rather than web-navigation-only models because tasks can require capabilities such as maintaining multiple tabs. The main comparison includes four API models and four open-weight models. No standalone question-answering LLM baseline is evaluated.

X5 is best read as progress within available trajectories at different step budgets; the paper does not clearly establish that each plotted x-coordinate comes from a separate independently rerun experiment. X7 is explicitly an increased-budget experiment and should not be merged with the main 100-step table.

## 9. Results

**Model performance under 100 steps [A].** Opus 4.6 leads averaged rubric score at 68.9% and perfect success at 44.5%. GPT-5.4 reaches 55.4% and 33.5%; Sonnet 4.6 reaches 49.8% and 31.0%. GPT-5.4-mini achieves 38.4% averaged but only 10.5% perfect. Partial progress and complete success therefore differ substantially (Table 2, p. 6).

**Analyst-derived comparison [C]:** Opus exceeds GPT-5.4 by 44.5 − 33.5 = 11.0 percentage points in perfect success, and by 68.9 − 55.4 = 13.5 percentage points in averaged score. These are absolute percentage-point differences, not relative percentage improvements.

**Open-weight results [A].** Qwen-3.5-9B has the highest reported perfect rate among the tested open-weight models, 13.5%. Qwen-3.5-4B has a slightly higher averaged score, 42.9% versus 42.6%, but lower perfect success, 10.7%. Thus the prose statement that 9B performs best is metric-dependent. UI-TARS-1.5-7B has 1.0% perfect success and 10.0% averaged score.

**Human agreement [A].** Rubric-average evaluation obtains κ 0.788, F1 0.949, accuracy 0.923. Perfect-task rubric evaluation obtains κ 0.849, F1 0.934, accuracy 0.926. The holistic judge obtains κ 0.508, F1 0.762, accuracy 0.752. The perfect metric has higher κ and accuracy than the averaged-item evaluation, but lower precision and F1; no single metric improves in every comparison (Table 3).

**Difficulty [A].** Opus perfect success falls from 97.8% on easy tasks to 71.7% on medium and 11.0% on hard. GPT-5.4 falls from 80.0% to 58.7% to 3.7%. On hard tasks, Opus's averaged score is 53.2%, versus GPT-5.4's 33.8% (§4.3, p. 8). The large difference between averaged and perfect hard-task scores indicates unfinished requirements despite partial work, without identifying why each item failed.

**Efficiency [A].** GPT-5.4 averages 64.4 steps versus Opus's 81.3 and achieves efficiency 1.15% versus 1.06%. GPT-5.4 averages 2.03 actions per call; 49.1% of calls contain two or more actions, with up to 24 actions in one turn. Opus returns exactly one action per call in the reported tasks (p. 8). This makes step counts informative about model round trips but not equivalent to raw action counts.

**Longer budgets [A].** Opus's reported full-set perfect rate increases from 44.5% to 76.5% with a 200-step budget. **Analyst-derived [C]:** 76.5 − 44.5 = 32.0 percentage points. Efficiency remains similar, 1.08% versus 1.06%. On a matched 76-task hard subset, Opus reaches 64.5%, while Qwen-3.5-9B remains at one perfect task, reported as 1.3% (A.9, pp. 22–23). Reporting errors in associated counts and upper bounds are discussed in §14.

## 10. Figure-by-figure interpretation

### Figure 1 — A task, trajectory, and partial-credit example

On p. 2, a task banner describes Palm Springs wedding-trip planning. Five thumbnail stages show flight search, drive-time checking, hotel search, car rental, and itinerary writing. Eight rubric rows use green checks and one red failure. The figure reports 88%, seven of eight rubrics satisfied; the unmet item concerns restaurant-detour feasibility. Seven divided by eight is 87.5% [C], consistent with a whole-percent display of 88%. This illustrates decomposition and partial credit, not a representative success rate. Small browser contents are only partially readable; task labels, rubric annotations, and caption carry the detailed evidence.

### Figure 2 — Bulk spreadsheet entry

On p. 7, a montage follows GPT-5.4 on a ten-surgeon research task. It reports 100% score in 93 steps and six rubric requirements. Eight selected snapshots show research, tab opening, spreadsheet paste, formatting, and completion; omitted steps are indicated. The caption explains encoding a table as base64 in a Python action, decoding it, and copying/pasting with preserved tabs and newlines. There are no statistical axes or uncertainty bars. It supports the existence of a flexible system-assisted strategy, not its prevalence beyond the eight runs reported separately in §4.3. Medical content is task material, not clinical advice from this report.

### Figure 3 — Success/step trade-off

On p. 8, a scatter plot places average steps per task on the horizontal linear axis and perfect rubric score in percent on the vertical linear axis. Points are labeled by model; colors distinguish model families/variants. A dashed frontier marks the tested Pareto-optimal trade-off: GPT-5.4 Mini, GPT-5.4, and Opus 4.6 offer increasing success at increasing average step cost. Visible ticks span approximately 50–80 steps and 0–40% success, with points extending beyond some outer ticks. Exact values come from Table 2, not coordinate estimation. No confidence intervals appear. Pareto optimality here applies only to the tested points and chosen metrics.

### Figure 4 — Perfect success within 100 steps

On p. 9, eight colored/marked curves show step budget, 0–100, against perfect score rate in percent. Visible y ticks run through 40%, with the highest endpoint above 40%. Opus and GPT-5.4 rise above the weaker-model curves; Opus overtakes GPT-5.4 late in the plotted trajectory. The authors describe a broadly sigmoidal pattern: near-zero perfect success for roughly the first 15 steps, growth through 20–70, and tapering after about 80. These phase boundaries are approximate descriptions. No uncertainty bands are shown. The caption calls the plot perfect rubric rate but also says 'mean rubrics score'; the axis and surrounding text favor perfect success, and the inconsistent wording remains flagged.

### Figure 5 — Difficulty and step consumption

On p. 9, the left grouped bar panel plots perfect rubric score (%) for easy, medium, and hard tasks. The right plots average steps per task for the same categories. Model colors are shared across panels. Both use linear 0–100 scales. Black capped error bars are visible, but their statistical definition is not supplied in the caption or nearby text; they must not be called confidence intervals or standard errors without evidence. The left-panel values correspond to Table 4's perfect-rate comparison. The panels show sharply lower hard-task success and generally substantial step use on harder tasks. Exact right-panel bar heights are not transcribed because they are not numerically labeled.

### Figure 6 — Participant annotation application

On p. 15, a screenshot shows a list of journey URLs and the four-step annotation workflow: select a key success URL, indicate automation preference, write the task, and judge feasibility. It documents the participant-facing collection mechanism, not a quantitative validation result. Some fine text is small; the surrounding explanation and caption establish the workflow.

### Figure 7 — Author task QA interface

On p. 20, an expandable list presents task difficulty, rubric count, and score. An expanded task shows its prompt and weighted rubric requirements and verification descriptions. The diagram is an interface screenshot, not a data-flow chart. It supports traceability of manual review procedures, but does not establish how consistently reviewers applied them or quantify reviewer agreement.

### Figure 8 — Scaling beyond 100 steps

On p. 22, step budget runs from 0 to 200 and perfect score rate from 0 to 80%. A vertical dashed line marks the original 100-step cap. The solid red curve represents Opus on all 200 tasks; a lighter red dotted curve represents Opus on the matched 76-task hard subset; a green curve represents Qwen-3.5-9B on that subset. The full-set Opus curve continues rising to 76.5%; subset Opus reaches 64.5%; Qwen remains near 1.3%. Values are reported in the caption/text, not merely estimated. No uncertainty bands appear. The full-set and subset curves must not be treated as the same population.

### Figure 9 — Human annotation viewer

On p. 26, the left panel selects runs and steps, the center shows screenshots/action details, and the right marks rubric pass/fail. Ambiguous cases can be flagged. This visually documents how humans inspect evidence. It does not independently establish the number of annotators per trajectory or inter-human consistency.

### Figure 10 — Source inspection after rendering failure

On p. 27, six selected snapshots follow a shopping/outfit task with four rubrics, 100% score, and 74 steps. The caption reports that GPT-5.4 used view-source: when a product page rendered blank, searched raw HTML for variant and stock terms, read embedded JSON-LD, and reconstructed a variant URL. The search terms include 40.5, while the described decoded size mapping is EU 40.0 = US 9.5; these are reported textual details, not independently resolved product facts. The figure shows an alternate information route, not a demonstrated security compromise.

### Figure 11 — Keyword absence as a relevance probe

On p. 28, eight snapshots show Opus completing seven requirements in 69 steps. An annotation highlights a browser find operation for 'Chromebook' yielding 0/0 matches and a pivot away from a page. The authors interpret this as hypothesis falsification about page relevance. **Analyst qualification [D]:** absence of an exact string does not logically prove absence of relevant content; the figure establishes the agent's heuristic, not universal validity of that inference. The task's 100% rubric score is a reported evaluator outcome.

### Figure 12 — Archive fallback after 403 responses

On p. 29, six snapshots illustrate Opus using archived yoga-studio pages after both target sites return 403 Forbidden. It reports five rubrics satisfied, 100%, in 50 steps. The caption identifies June 2024 archived pages, while the task requests upcoming classes. **Analyst observation [D]:** successful retrieval of historical schedules does not establish their current validity. The figure therefore illustrates both resourceful access and a temporal-evidence concern that the reported perfect score does not resolve.

## 11. Table-by-table interpretation

### Table 1 — Representative tasks

On p. 4, six rows pair task summaries with example rubric criteria: kitchen setup and weather risk at easy difficulty; Canadian passport/Japan-trip planning and Tesla lease comparison at medium; a 30-stadium baseball trip and ten-recipe banana-bread synthesis at hard. Columns are level, task summary, and example rubric criteria. These are condensed examples, not all rubric items or population statistics. Appendix A.10 supplies full prompts. The table demonstrates diversity, cross-site requirements, concrete quantities, and observable deliverables. The substantive constraints are retained here; conversational wording is compressed.

### Table 2 — Eight-model main results

All scores below are author-reported on p. 6. O-M2W is the holistic Online-Mind2Web judge; rubric columns and efficiency are percentages; steps are mean runner steps.

| Model | O-M2W | Rubric average | Perfect | Steps | Trajectory Efficiency |
|---|---:|---:|---:|---:|---:|
| Opus 4.6 | 37.0 | 68.9 | 44.5 | 81.3 | 1.06 |
| GPT-5.4 | 21.5 | 55.4 | 33.5 | 64.4 | 1.15 |
| Sonnet 4.6 | 25.0 | 49.8 | 31.0 | 80.4 | 0.79 |
| GPT-5.4-mini | 15.5 | 38.4 | 10.5 | 41.7 | 1.12 |
| Qwen-3.5-9B | 18.0 | 42.6 | 13.5 | 78.3 | 0.75 |
| Qwen-3.5-4B | 18.3 | 42.9 | 10.7 | 86.4 | 0.69 |
| Qwen-3.5-35B-A3B | 9.5 | 28.5 | 6.5 | 86.1 | 0.42 |
| UI-TARS-1.5-7B | 2.0 | 10.0 | 1.0 | 76.6 | 0.23 |

Opus leads the three success columns; GPT-5.4 leads efficiency; Mini uses the fewest steps. No statistical significance markers, error intervals, or missing-value notes are supplied. Qwen-4B's 10.7% is not an exact possible perfect-task fraction of 200 binary outcomes, suggesting an unreported denominator or aggregation detail; the table alone does not explain it.

### Table 3 — Automated versus human judgments

| Metric | Cohen's κ | Precision | Recall | F1 | Accuracy |
|---|---:|---:|---:|---:|---:|
| O-M2W judge | 0.508 | 0.842 | 0.696 | 0.762 | 0.752 |
| Rubrics, averaged/item level | 0.788 | 0.939 | 0.960 | 0.949 | 0.923 |
| Rubrics, perfect/task level | 0.849 | 0.901 | 0.970 | 0.934 | 0.926 |

The rubric metrics outperform the holistic judge on every listed measure. Between the two rubric granularities, averaged/item-level grading has higher precision and F1, while perfect/task-level grading has higher κ, recall, and accuracy. These are different observation units, so the comparison should not imply interchangeable denominators. No uncertainty estimates or significance tests are reported.

### Table 4 — Perfect rates by difficulty

| Model | Easy, n=45 | Medium, n=46 | Hard, n=109 | Overall, n=200 |
|---|---:|---:|---:|---:|
| Opus 4.6 | 97.8 | 71.7 | 11.0 | 44.5 |
| Sonnet 4.6 | 82.2 | 50.0 | 1.8 | 31.0 |
| GPT-5.4 | 80.0 | 58.7 | 3.7 | 33.5 |
| GPT-5.4 Mini | 22.2 | 19.6 | 1.8 | 10.5 |
| Qwen3.5-35B-A3B | 24.4 | 4.3 | 0.0 | 6.5 |
| Qwen3.5-9B | 31.1 | 17.4 | 4.6 | 13.5 |
| Qwen3.5-4B | 28.9 | 8.7 | 3.8 | 10.7 |
| UI-TARS-1.5-7B | 4.4 | 0.0 | 0.0 | 1.0 |

All entries are percentages. Opus leads every column. UI-TARS and Qwen-35B-A3B tie at zero on hard tasks; UI-TARS is also zero on medium. There are no statistical significance annotations. The Qwen-4B hard value, 3.8%, also does not correspond to a one-decimal rounded integer success count out of 109, reinforcing uncertainty about its effective denominator.

### Table 5 — Qwen final-summary prompt

On p. 23, the table instructs Qwen to summarize information gathered during the task, use plain text, and avoid tool calls or action descriptions. It embeds the date 29 April 2026. This is a model-specific evaluation accommodation, not a results table. The date is later than the title-page arXiv date, 27 April 2026; the supplied work does not explain this chronology. The prompt's behavioral requirements are represented, while its full wording is deliberately compressed.

## 12. Diagram / architecture interpretation

There is no separate formal architecture diagram. Figure 1 is a conceptual workflow montage, Figures 2 and 10–12 are execution-story montages, and Figures 6, 7, and 9 show interfaces.

The construction pipeline can be reconstructed from the supplied methods: participant history → segmented journeys and labels → LLM screening → author refinement → embedding/reduction/clustering → related-cluster graph → GPT-5.4 composition → prompt/rubric rewriting → two-pass review → final tasks. A parallel hard-task route expands seeds, applies LLM judging with limited retry, and uses human shortlisting. Author-written tasks provide a third source. The uncertainty over 2,380 versus 696 seeds prevents treating all branches as sharing a proven identical input pool.

The evaluation flow is task → model/runner observation-action loop → screenshots and action history → one judge call per rubric → binary item verdicts → averaged and perfect scores. Human annotations provide a comparison layer for automated judging. Trajectory Efficiency adds the per-task step count to the score calculation. These descriptions are analyst-organized renderings of the methods, not additional author-provided diagrams.

## 13. Equations and mathematical concepts

Equation (1), on p. 7, defines:

**Trajectory Efficiency = (1/N) Σᵢ₌₁ᴺ (sᵢ / nᵢ).**

Here N is the number of tasks, sᵢ is the averaged rubric score on task i, and nᵢ is the number of runner/model steps taken on that task. The summation adds each task's score-per-step ratio, and division by N gives equal weight to each task's ratio. Higher values indicate more rubric credit per interaction step. The table expresses the result as a percentage.

The metric is an average of ratios, not the ratio of average score to average steps. **Analyst mathematical clarification [C]:** in general, (1/N)Σ(sᵢ/nᵢ) differs from [(1/N)Σsᵢ]/[(1/N)Σnᵢ], because each task has its own denominator. Thus Table 2's efficiency should not be reconstructed by simply dividing its aggregate score column by its aggregate step column.

The authors explicitly lack the oracle minimum number of steps required for each task. They therefore do not normalize against an optimal trajectory, unlike the referenced success-weighted path-length concept. The metric measures observed efficiency under this runner, not distance from a known optimum. A positive step count is required for the ratio; handling of a zero-step run is not specified.

Perfect task success corresponds to every binary rubric verdict being one. The text describes averaged rubric scoring, but supplies no separate equation clarifying whether or how stored weights are used. Cohen's κ, precision, recall, F1, and accuracy are named agreement measures; their formulas and class conventions are not provided. No additional mathematical derivations, optimization objectives, or formal proofs appear.

## 14. Interpretation and discussion

The strongest supported conclusion is conditional: under the main 100-step setup, even the leading tested agent leaves many tasks incomplete, and granular grading detects substantially more partial progress than holistic pass/fail. The appendix shows that some incompleteness is budget-dependent: Opus continues improving at 200 steps. Qwen's matched-subset stagnation indicates that this particular model's failures are not remedied simply by doubling the available steps.

Several consistency issues prevent stronger numerical conclusions:

| Issue | Source statements | Assessment |
|---|---|---|
| 100-step Opus count | 44.5% of 200; A.9 also writes 86/200 | 44.5% × 200 = 89 [C], whereas 86/200 = 43.0% [C]. Both cannot describe the same exact condition. |
| Optimistic Opus upper bound | 153 successes, 29 capped runs, upper bound 86.0% | If all 29 capped runs are additional successes, (153+29)/200 = 91.0% [C]. Overlap or another rule is not explained; 86.0% cannot be reproduced from the stated operands. |
| Non-budget failure floor | A.9 says at least approximately 14% fail for other reasons | This depends on the unresolved 86.0% upper-bound calculation and should not be treated as established. |
| Human-agreement denominator | 120 Opus trajectories; agreement across all 1,225 rubric pairs | 1,225 is also the full 200-task rubric inventory. The actual annotated pair count and mapping are not clear. |
| Hard-generation seeds | 696 usable refined journeys in A.3; 2,380 refined journeys in A.5 | Terminology or source-pool mismatch; unresolved. |
| Hard-task comparison population | p. 23 says 80 hard tasks but reports 1/76; Figure 8 uses 76 | Only 76 matched runs are quantitatively evidenced; four omitted cases are unexplained. |
| Qwen-4B denominators | Overall 10.7% for n=200; hard 3.8% for n=109 | Neither is reproduced by integer perfect-success counts at stated denominators and displayed precision. |
| Figure 4 metric wording | Perfect-rate title/axis versus 'mean rubrics score' caption sentence | Most context supports perfect rate, but wording is inconsistent. |
| Figure 12 temporal evidence | Upcoming classes requested; June 2024 archives used; 100% score | Historical retrieval and current schedule validity are not equivalent. |
| Difficulty illustration | A.4 example says six steps, hard; §3.2 calls medium six–eight steps or four-plus domains, hard exceeding both | Example label and simplified taxonomy do not transparently align. |

These discrepancies do not erase the observed model rankings or rubric-agreement comparison, but reduce confidence in precise secondary calculations and some generalizations. The abstract's 1.15% efficiency is the highest table value, achieved by GPT-5.4; it should not be attributed to the highest-success model, Opus, whose main efficiency is 1.06%.

**Security interpretation [D]:** the paper supports studying an expanded interaction surface involving websites, tabs, raw source, archives, clipboard operations, files, and sometimes programmatic execution. It also illustrates imperfect stopping, completion, and evidence-selection behavior. It does not establish that these mechanisms cause more security failures than a standalone LLM, nor that its observed agents encountered malicious instructions. A defensible use in the user's research is as capability and environment evidence, supplemented elsewhere by actual adversarial comparisons—not as direct proof of comparative vulnerability.

## 15. Contributions and novelty

**Dataset/benchmark contribution [A]:** 200 extended multi-site tasks with browsing-history grounding, author contributions, and model-assisted hard-task generation; 1,225 rubric items; multiple difficulty levels and topic categories.

**Methodological contribution [A]:** per-requirement trajectory judging, including verification descriptions and observable browser evidence, tested against human annotations.

**Measurement contribution [A]:** Trajectory Efficiency, which combines partial task achievement with runner-step cost.

**Empirical contribution [A]:** eight-model results, difficulty breakdowns, 100-step progress curves, and a 200-step budget analysis.

**Qualitative contribution [A]:** characteristic incomplete-deliverable failures and adaptive techniques such as batched actions, base64-assisted spreadsheet paste, raw-source extraction, archive fallback, and keyword-based relevance probes.

There is no new trained model, formal security defense, exploit algorithm, theorem, or demonstrated standalone-LLM/web-agent vulnerability comparison. **Analyst interpretation [D]:** for security research, the novel value of this source is operational detail about realistic agents rather than a security effect estimate.

## 16. Limitations

### Authors' stated limitations

The authors acknowledge that holistic evaluation is noisy and task-specific rule-based rewards are difficult to scale (§3.3). They do not know optimal trajectory lengths (§4.1). They explicitly note low complete-task success, poor hard-task performance, inefficiency, research without deliverable production, inaction despite planning, and difficulty covering many parallel subtasks (§4.3; A.9). The ethics statement says the models/scaffolds are research prototypes and the results do not endorse present practical deployment (p. 11).

They describe both misuse possibilities and unintended reuse of browser primitives. They acknowledge that extra steps alone do not solve Qwen's hard-task failures. These are author statements about observed limitations and risks, not a quantified security evaluation.

### Additional evidence-based analyst observations

[D] Geographic recruitment is limited to the US and UK; public-page feasibility filtering excludes authenticated workflows. Real browsing grounding does not mean every final task is an unmodified natural user session: 80 hard tasks are generated expansions and 30 are author-written.

[D] The benchmark is imbalanced toward hard tasks, with 109 of 200. Model implementations vary, Qwen receives a special summary prompt, and batching changes the meaning of a step across systems. These conditions complicate causal attribution to underlying models alone.

[D] Human agreement is reported for Opus trajectories only, without clear annotation overlap or uncertainty estimates. Live-site changes and historical archive use can complicate what counts as correct evidence. Numeric inconsistencies limit confidence in some appendix bounds and denominators.

[D] The supplied code, dataset, full trajectories, and model configurations are absent, so this report cannot reproduce scores or inspect every claimed behavior independently. These are access limitations of this analysis, not claims that the authors failed to release artifacts.

## 17. Threats to validity

The following categories are analyst-applied [D]; the authors do not present this exact taxonomy.

**Internal validity:** shared virtual environments improve comparability, but model-specific implementations, recommended settings, action batching, and final-summary prompting vary. No controlled intervention isolates which component causes performance differences. Qualitative failure labels are descriptive rather than experimentally established causal mechanisms.

**Construct validity:** rubric agreement supports the intended measurement of task satisfaction, but perfect scores depend on rubric coverage and judge interpretation. A completed rubric set may not guarantee current factual validity, as the archived-schedule example illustrates. Efficiency is defined per model call, so it is not a universal measure of mouse actions, latency, cost, or optimality. Task success is not security robustness.

**External validity/generalizability:** English-language-style requests, US/UK participants, public web pages, selected models, and a specific runner constrain generalization. Authenticated enterprise work, harmful adversarial pages, real financial actions, and standalone LLM operation are outside the demonstrated comparison.

**Statistical conclusion validity:** tables lack confidence intervals and significance tests; repeated-run variability is not described. Figure 5 has undefined error bars. Several denominators and appendix counts are unresolved. The report therefore preserves descriptive differences without asserting statistically proven superiority.

**Ecological validity:** live websites and human-history seeds improve realism, while generated expansion, forced browser-evidence requirements, and finite caps shape tasks differently from unconstrained personal assistance. The ethics statement intentionally limits real-world side effects.

**Reproducibility:** the paper names core tools, judge model, prompts, and runner, but full hardware/software versions, seeds, exact graph thresholds, all scaffold settings, and inaccessible artifacts prevent reproduction from the supplied document alone.

## 18. Future work and open questions

### A. Author-proposed future work

The authors propose rubric-based reward signals for reinforcement learning, multi-action batching through training or prompting, inference-time search, and better efficiency. They suggest subagents or multi-agent arrangements for high-fanout tasks and explicit step-aware planning for persistent failures. The ethics statement calls for safeguards that account for agent capabilities, including respecting site terms and robots.txt policies. These proposals are not implemented defenses evaluated in this paper.

### B. Additional open questions [D]

Would rubric-judge agreement generalize to weaker models, other languages, or adversarial trajectories? How much of the ranking comes from model capability versus scaffold design? How should historical evidence be scored when a task asks for current information? What are the correct denominators for Qwen-4B and the matched hard-task subset? How do results vary across repeated runs and changing sites?

For the user's security question, the next necessary evidence would be an explicit threat model, a defined standalone-LLM comparator, matched tasks and malicious content, and separate measurements of attack success and benign task success. The present source motivates those questions but cannot answer them experimentally. Another unresolved question is whether additional autonomous steps increase harmful exposure, improve recovery, or both; the paper measures completion scaling, not this security trade-off.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within this report |
|---|---|
| LLM | Large language model; the component generating language, reasoning, or action choices |
| CUA | Computer-use agent; a model-driven system operating software interfaces |
| GUI | Graphical user interface; visible computer controls and displays |
| API | Application programming interface; a programmatic way to access a service |
| Trajectory | Recorded sequence of task observations and actions |
| Horizon | Extent of sequential work and dependencies needed to complete a task |
| Rubric | A requirement/checkpoint used for grading |
| Verification description | Instructions describing evidence needed to pass a rubric |
| Averaged rubric score | Partial-credit aggregation of item outcomes; exact weighting is underexplained |
| Perfect rubric score | Binary task success requiring all rubric items to pass |
| LLM-as-a-judge | A language model evaluating task-execution evidence |
| O-M2W | The paper's abbreviation for the Online-Mind2Web trajectory judge |
| OSWorld runner | Execution framework used to operate virtual computer environments |
| Step | One model call in the runner observation/action loop |
| Action batching | Returning multiple interface actions in one call |
| Trajectory Efficiency | Mean across tasks of rubric score divided by step count |
| N, i, sᵢ, nᵢ | Task count, task index, task rubric score, and task step count |
| Embedding | Numerical representation used to compare journey-label similarity |
| UMAP | Named dimensionality-reduction method; used to reduce embeddings to 15 dimensions |
| HDBSCAN | Named clustering method; used to form groups and identify noise |
| BFS | Breadth-first search; graph traversal used to collect related clusters |
| Cosine similarity | The specified similarity measure for cluster centroids; thresholds are unspecified |
| QA | Quality assurance; author and LLM-assisted checking |
| PII | Personally identifiable information; prompts exposing it are rewritten or removed |
| High fanout | Many related parallel items/subtasks requiring coverage |
| Pareto frontier | Tested options for which no other plotted option has both fewer steps and greater success |
| Base64 | Encoding used in the reported table-paste strategy |
| HTML / JSON-LD | Page source and embedded structured-data formats used in a qualitative example |
| 403 Forbidden | Website response that blocked direct access in the reported example |
| Cohen's κ | Reported chance-adjusted agreement measure; formula not supplied |
| F1 | Reported precision/recall summary measure; formula not supplied |
| pp | Percentage points; absolute difference between percentages |

The paper names UMAP and HDBSCAN without expanding their acronyms in the supplied methods. Their names are retained rather than importing external definitions. ACL and MLB appear in example tasks as anterior cruciate ligament and Major League Baseball contexts; they are not central evaluation concepts.

## 20. Key numerical results

All values are exact reported representations unless labeled otherwise. Main model-table values are already fully transcribed in §11.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Participants | 248 | people | US/UK recruitment | Author-reported | p. 3, §3.1 |
| Collected journeys | 2,380 | journeys | Participant labels | Author-reported | p. 3, §3.1 |
| Labels judged inaccurate | 71.8 | % | LLM comparison with URL evidence | Author-reported | p. 16, A.3 |
| Retained usable journeys | 696; 29.2 | journeys; % | After filtering | Author-reported | pp. 3, 16 |
| Final tasks | 200 | tasks | 90 composed + 30 authored + 80 generated hard | Author-reported | pp. 4–5 |
| Difficulty counts | 45 / 46 / 109 | tasks | Easy / medium / hard | Author-reported | p. 5 |
| Total rubric items | 1,225 | items | Full task inventory | Author-reported | p. 5 |
| Rubrics per task | mean 6.1; median 6; range 3–12 | items | Full benchmark | Author-reported | p. 5 |
| Instruction length | mean 272.3; median 277.5; range 76–387 | words | Task prompts | Author-reported | p. 5 |
| Category coverage | 22; 88 | top-level domains; categories | SimilarWeb-based description | Author-reported | p. 5 |
| Categories per task | mean 1.9; up to 3 | categories | Topic coverage | Author-reported | p. 5 |
| Main topic counts | 43 / 38 / 37 / 34 | tasks | Shopping / travel / science-education / computing-technology | Author-reported | p. 5 |
| Other listed topics | 21 / 21 / 20 / 19 / 18 | tasks | Lifestyle / health / community / arts / food | Author-reported | p. 5 |
| Embedding reduction | 15 | dimensions | UMAP pipeline | Author-reported | p. 17 |
| Cluster traversal | 1–2; 3–6; 12–24 | hops; clusters; candidate journeys | Task composition | Author-reported | p. 17 |
| Source reuse cap | 3 | uses per journey | Composed tasks | Author-reported | p. 4 |
| Dependency requirement | at least 30 | % of steps | Composition prompt | Author-reported | p. 17 |
| Hard candidates / shortlist | 567 / 80 | tasks | Generated pipeline | Author-reported | p. 18 |
| Human comparison subset | 120 | trajectories | Opus 4.6 only identified | Author-reported | p. 6 |
| Best main perfect success | 44.5 | % | Opus, 100-step cap | Author-reported | p. 6, Table 2 |
| Highest main efficiency | 1.15 | % | GPT-5.4, 100-step cap | Author-reported | p. 6, Table 2 |
| Rubric versus holistic κ | 0.788 versus 0.508 | coefficient | Item-level rubric vs trajectory judge | Author-reported | p. 6, Table 3 |
| Opus hard average / perfect | 53.2 / 11.0 | % | Main budget, hard tasks | Author-reported | p. 8 |
| GPT-5.4 hard average / perfect | 33.8 / 3.7 | % | Main budget, hard tasks | Author-reported | p. 8 |
| GPT actions per call | 2.03 | actions | GPT-5.4 | Author-reported | p. 8 |
| Batched GPT calls | 49.1; max 24 | %; actions/turn | Two or more actions; maximum batch | Author-reported | p. 8 |
| Opus cost/time | approximately 30; 2.5 | minutes; dollars | 100-step run per task | Author-reported | p. 8, footnote 1 |
| Opus research-only zero runs | 6 of 12 | runs | Qualitative failure analysis | Author-reported | p. 9 |
| GPT inaction zero runs | 4 of 7 | runs | Qualitative failure analysis | Author-reported | p. 9 |
| Opus main cap / partial steps | 39; 97.4 | % of tasks; mean steps | 100-step cap; partial-credit runs | Author-reported | p. 9 |
| Base64 / source-inspection occurrence | 8 / 23 | runs | GPT strategies | Author-reported | p. 10 |
| Middle-click uses | 131 versus 7 | interactions | Opus versus GPT-5.4 | Author-reported | p. 10 |
| Opus extended perfect success | 76.5 | % | Full 200-task set, 200 steps | Author-reported | p. 22 |
| Opus extended progress | 50.5 / 59.5 / 67.0 | % | At 120 / 150 / 180 steps | Author-reported | p. 22 |
| Opus extended capped runs | 29/200; 14.5 | runs; % | 200-step condition | Author-reported | p. 22 |
| Opus extended efficiency | 1.08 | % | 200-step condition | Author-reported | p. 22 |
| Matched hard-set final success | 64.5 versus 1.3 | % | Opus versus Qwen, 76 tasks | Author-reported | p. 22, Figure 8 |
| Qwen perfect tasks | 1/76 | tasks | No additional perfect task from steps 100–200 | Author-reported | p. 23 |
| Opus budget improvement | 76.5 − 44.5 = 32.0 | percentage points | Reported full-set rates | Analyst-derived | p. 22 |
| Opus/GPT main success gap | 44.5 − 33.5 = 11.0 | percentage points | Table 2 perfect rates | Analyst-derived | p. 6 |
| Opus 44.5% count check | 0.445 × 200 = 89 | tasks | Contradicts 86/200 parenthetical | Analyst-derived | p. 22 |
| Upper-bound arithmetic check | (153+29)/200 = 91.0 | % | Conditional disjoint-addition calculation | Analyst-derived | p. 22 |

The last row is an arithmetic diagnostic, not a replacement author result: capped-run overlap is unspecified. The source's 86.0% upper bound and approximate 14% non-budget failure floor remain unresolved.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Benchmark targets extended multi-site work | 200 tasks, constructed from journeys and additional sources | X2; Table 1 | pp. 3–5 | HIGH for documented design; realism is a methodological claim |
| Rubric grading agrees better with humans | κ, F1, accuracy, precision, recall all exceed holistic comparator | X1; Table 3 | p. 6 | HIGH for reported numbers; denominator/generalization caveats |
| Main complete-task performance remains limited | Best perfect rate 44.5% | X2; Table 2 | p. 6 | HIGH under 100-step condition only |
| Hard tasks are much less often completed | Opus 97.8/71.7/11.0% | X4; Table 4 | p. 10 | HIGH descriptive evidence; content and difficulty covary |
| Efficiency and success rankings differ | GPT 1.15% efficiency; Opus highest perfect score | X3; Table 2; Figure 3 | pp. 6–8 | HIGH; step/action distinction matters |
| Extra budget helps Opus substantially | 76.5% at 200 steps | X7; Figure 8 | p. 22 | HIGH reported rate; associated counts/bounds inconsistent |
| Extra budget does not rescue tested Qwen subset | 1/76 perfect by 100 and still 1/76 by 200 | X7 | p. 23 | HIGH for stated matched subset; 80/76 discrepancy |
| Agents use unexpected information routes | Raw source, clipboard/Python, archives | X6; Figures 2, 10, 12 | pp. 7, 10, 27, 29 | HIGH author reports; MEDIUM independent screenshot verification |
| Browser primitives can have misuse implications | Ethics discussion names scraping, phishing, access-control circumvention | Ethics analysis | p. 11 | HIGH as author concern; no attack rates measured |
| Agent interaction surfaces matter to security | External sources connect to browser/system actions | Analyst synthesis | pp. 8, 11, 27, 29 | MEDIUM inference; no standalone-LLM comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to plan an entire trip, not just tell you a city's name. It has to compare flights, check hotels, look up places to eat, remember what it found, and leave you a useful itinerary. Odysseys tests that kind of extended computer work with 200 tasks.

The researchers grade each task with a checklist. That matters because an AI might do most of the research but forget the final document. A single pass/fail grade hides that difference. The checklist-based grader agreed with human judgments better than the tested all-at-once grader.

With a limit of 100 model steps, the best tested system completed every requirement on 44.5% of tasks. Giving that system 200 steps raised its reported success to 76.5%. A smaller tested model barely improved on a matched difficult subset. More time can help a capable agent, but it does not automatically fix every problem.

For security, the useful lesson is that these agents can interact with much more than a conversation: websites, page source, archived pages, files, and computer actions. That makes their behavior important to study carefully. But this paper did not put malicious instructions on websites or compare attacks against ordinary chat models, so it cannot prove that web agents are more vulnerable. It shows capabilities and reliability problems that help define the security questions still needing direct tests.

## Completeness Audit

Coverage is assessed against the supplied inventory. 'Represented in compressed form' means the substantive method, result, or example is explained while repetitive wording or fine-grained interface text is shortened. It does not mean every original sentence is retained.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/version/abstract | Yes, text + visual | Yes | Fully represented | Venue not supplied |
| §1 Introduction | Yes, text + visual | Yes | Represented in compressed form | Motivation and contributions retained |
| §2 Computer-Use Agents | Yes, text + visual | Yes | Represented in compressed form | Prior-work categories retained; individual citation descriptions shortened |
| §2 Long-Horizon LLM Agents | Yes, text + visual | Yes | Represented in compressed form | Positioning retained; no external validation |
| §3 dataset overview | Yes, text + visual | Yes | Fully represented | 200 tasks and search-based setting |
| §3.1 collection | Yes, text + visual | Yes | Fully represented | Participants, app, journeys |
| §3.2 transformation/difficulty | Yes, text + visual | Yes | Fully represented | Sources, thresholds, reuse, taxonomy caveat |
| §3.3 rubrics | Yes, text + visual | Yes | Fully represented | Judge and verification details |
| §3.4 final review | Yes, text + visual | Yes | Fully represented | Rewriting, two passes, privacy |
| §3.5 statistics | Yes, text + visual | Yes | Fully represented | Key distribution and length values |
| §4 setup | Yes, text + visual | Yes | Fully represented | Shared environment and varying implementations |
| §4.1 rubric agreement | Yes, text + visual | Yes | Fully represented | All Table 3 metrics; denominator caveat |
| §4.1 efficiency | Yes, text + visual | Yes | Fully represented | Equation and call/action distinction |
| §4.2 results | Yes, text + visual | Yes | Fully represented | Entire main table |
| §4.3 difficulty | Yes, text + visual | Yes | Fully represented | Entire difficulty table |
| §4.3 step scaling | Yes, text + visual | Yes | Fully represented | Conditions and approximate trend boundaries |
| §4.3 failure modes | Yes, text + visual | Yes | Represented in compressed form | Counts and main mechanisms retained |
| §4.3 surprising capabilities | Yes, text + visual | Yes | Fully represented | Strategies and occurrence counts |
| §5 conclusion | Yes, text + visual | Yes | Represented in compressed form | Appendix qualification preserved |
| Acknowledgments | Yes, text only | Partly | Inspected but deliberately omitted as non-substantive | Contributor names not repeated; no methodological findings omitted |
| Ethics: intended use | Yes, text only | Yes | Fully represented | Controlled prototypes, low-impact scope |
| Ethics: misuse | Yes, text only | Yes | Fully represented | Risks distinguished from measured attacks |
| Ethics: broader impacts | Yes, text only | Yes | Represented in compressed form | Accessibility, automation, employment concerns |
| Ethics: privacy | Yes, text only | Yes | Fully represented | Consent, de-identification, no raw-history release |
| References pp. 11–14 | Yes, text; p. 12 also visual | Yes | Represented in compressed form | Bibliography not reproduced or validated |
| A.1 LLM disclosure | Yes, text + visual | Yes | Represented in compressed form | Claude Code assisted plots, example selection/descriptions, manuscript checks; human review reported |
| A.2 collection interface | Yes, text + visual | Yes | Fully represented | Four annotation stages |
| A.3 journey refinement | Yes, text only | Yes | Fully represented | 71.8%, screening dimensions, manual review |
| A.4 composition pipeline | Yes, text + visual | Yes | Fully represented | Embeddings, graph, traversal, prompt constraints |
| A.5 hard-task pipeline | Yes; p. 18 visual, p. 19 text only | Yes | Represented in compressed form | Counts, filtering, retry, weights, time policy, no-hidden-work rule retained |
| A.6 QA interface | Yes, text + visual | Yes | Fully represented | Weighted rubric display |
| A.7 evaluation details | Yes, text + visual | Yes | Fully represented | Start URL, official implementations, Qwen accommodation |
| A.8 judge prompt | Yes, text + visual | Yes | Represented in compressed form | Inputs, binary output, visible-evidence and blocking rules |
| A.9 200-step analysis | Yes, text + visual | Yes | Fully represented | Full/subset distinction, failures, numerical issues |
| A.10 six full task prompts | Yes; pp. 24–25 text only | Yes | Represented in compressed form | All six examples and core constraints retained, conversational wording shortened |
| A.11 annotation interface | Yes, text + visual | Yes | Fully represented | Evidence layout and ambiguity flagging |
| A.12 qualitative results | Yes, text + visual | Yes | Fully represented | All three additional montages |
| Figure 1 | Yes, visual + text | Yes | Fully represented | Fine browser text partly unreadable |
| Figure 2 | Yes, visual + text | Yes | Fully represented | Selected steps, not full trajectory |
| Figure 3 | Yes, visual + text | Yes | Fully represented | Exact coordinates taken from table |
| Figure 4 | Yes, visual + text | Yes | Fully represented | Caption metric inconsistency flagged |
| Figure 5, both panels | Yes, visual + text | Yes | Represented in compressed form | Undefined error bars and unlabeled step heights flagged |
| Figure 6 | Yes, visual + text | Yes | Fully represented | Interface structure; tiny text qualified |
| Figure 7 | Yes, visual + text | Yes | Fully represented | Interface structure; not reviewer-reliability evidence |
| Figure 8 | Yes, visual + text | Yes | Fully represented | Three populations/curves distinguished |
| Figure 9 | Yes, visual + text | Yes | Fully represented | Human annotation workflow |
| Figure 10 | Yes, visual + text | Yes | Fully represented | Source-view strategy and size-text caveat |
| Figure 11 | Yes, visual + text | Yes | Fully represented | Keyword-absence inference qualified |
| Figure 12 | Yes, visual + text | Yes | Fully represented | Historical/current mismatch flagged |
| Tables 1–5 | Yes, visual + text | Yes | Fully represented | Numeric tables fully transcribed; prose prompts compressed |
| Equation (1) | Yes, visual + text | Yes | Fully represented | Symbols, aggregation, normalization caveats |
| X1–X7 analyses | Yes | Yes | Fully represented | Separate conditions retained |
| Explicit RQs/hypotheses | Searched supplied content | Yes | Not present as formal declarations | Objectives distinguished from invented formal questions |
| Numbered algorithms/theorems | Searched supplied content | Yes | Not present | Procedural prompts represented |
| Major contributions | Yes | Yes | Fully represented | Benchmark, rubric method, metric, empirical/qualitative results |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst observations |
| Footnotes | Yes | Yes | Represented in compressed form | Equal contribution, cost/time, runner link accounted for |
| Supplied supplementary files | None | Not applicable | No separate files supplied | Website/code not inspected |
| Prompt examples omitted by authors | No | No | Missing from supplied material | A.4/A.5 explicitly abbreviate in-context examples |

### Missing or inaccessible material

No physical page in the supplied 1–29 sequence is missing. Visual renderings are absent for pp. 11, 13, 14, 16, 19, 24, and 25, which have text-only coverage. Full-resolution embedded browser states, complete raw trajectories, benchmark task files, code, configuration files, and live release contents were not supplied or accessed. Some in-context examples are explicitly omitted in the paper itself. No separate supplement was supplied; absence of embedded files does not prove absence of all externally hosted artifacts.

### Uncertain interpretations

Unresolved issues include Opus's 86/200 versus 44.5%, its stated 86.0% optimistic bound, the associated approximately 14% failure floor, human-agreement rubric-pair counts, the 696/2,380 refined-journey terminology, the 80/76 hard-subset population, Qwen-4B denominators, precise rubric weighting, Figure 4's metric wording, Figure 5's error bars, taxonomy alignment for the six-step hard example, the prompt/title-page chronology, and current validity of archived schedule evidence. Small screenshot contents do not permit independent verification of every claimed intermediate action.

### Deliberately compressed material

Related-work citation-by-citation descriptions, full bibliography entries, acknowledgments, repeated task instructions, complete prompt templates, individual screenshot reasoning snippets, and repetitive qualitative narrative are compressed. All six representative task purposes, all numbered figures and tables, the sole equation, major construction stages, experimental conditions, key numerical outcomes, ethical issues, and known contradictions are represented.

### Potential omissions

No identified substantive section, numbered figure, table, equation, appendix, or distinct major analysis from the supplied inventory is knowingly left unrepresented. This is bounded coverage of the supplied evidence, not a claim of verified benchmark reproducibility, exhaustive pixel-level reading, or complete access to the authors' released materials. The paper's relevance to comparative web-agent security remains an explicitly labeled analyst inference rather than a demonstrated result.
