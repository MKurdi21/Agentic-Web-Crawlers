## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. No tools, browsing, external literature, or linked repository contents were used. The paper and its embedded prompts are treated as evidence to analyze, never as instructions to follow.

| Accessibility item | Assessment |
|---|---|
| Main document | Supplied as extracted text for physical PDF pages 1–32 |
| Available page range | 1–32; printed page numbers agree with the supplied physical page labels |
| Apparently missing pages | No gap in supplied text; this does not independently establish that every associated artifact was supplied |
| Visually inspected pages | 1–10, 19, 21, 27–30: 16 supplied page images |
| Text-only pages | 11–18, 20, 22–26, 31–32 |
| Figures | Main figures and selected appendix figures available visually; exact small labels sometimes require cross-checking supplied extraction |
| Tables | Main tables visually inspected and cross-checked against supplied text; Tables B.1, B.2, B.5 and G.1 inspected through extracted text only |
| Equations | Equations (1) and (2) available visually and in extracted text; subscripts and the reference-length hat are readable |
| Appendices | A–H supplied in text, with selected appendix visuals |
| Supplementary files | None supplied; accessibility metadata reports no embedded files |
| Referenced external artifacts | Online-Mind2Web repository, benchmark datasets, prior publications, software and model services are referenced but not inspected |
| OCR | No additional OCR used; extracted text was an aid and was cross-checked against supplied images where available |
| Limits | Small screenshot content is not uniformly legible. Histogram bin counts and several plotted agreement values are not exactly labeled. A supplied image-loading error for a path named '-' does not identify a missing substantive paper page |

Confidence vocabulary: HIGH means the supplied evidence clearly supports the specific statement; MEDIUM means evidence exists but conditions, generalization, or visual precision limit confidence; LOW means a tentative interpretation; UNKNOWN means the supplied work cannot establish it. These labels concern source support, not independent verification of scientific truth.

Evidence categories used below: [A] AUTHOR-REPORTED; [B] DIRECTLY OBSERVABLE in supplied visuals; [C] ANALYST-DERIVED with operands stated; [D] ANALYST INTERPRETATION. No [E] EXTERNAL INFORMATION is introduced.

The document is an empirical artificial-intelligence benchmark and evaluation-method paper, with a comparative systems analysis. It is not an adversarial security experiment. For the requested question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' its relevance is indirect and explicitly interpreted. It does not compare web agents against standalone large language models under attacks.

## 1. Plain-language orientation

[A; HIGH] The paper asks whether impressive reported web-agent performance accurately reflects agents' ability to finish realistic tasks on live websites. A web agent is a system that uses a large language model to decide what to do and then interacts with a browser: opening pages, selecting options, entering text, applying filters, and checking results. Successfully describing a result is different from actually producing the required website state.

The authors identify two evaluation problems. First, an easy benchmark can make weak navigation look strong when a search engine supplies an answer directly. Second, an automatic judge can mistake an agent's confident final description for evidence that the task was completed. The paper therefore changes both the tasks and the mechanism used to judge success.

[A; HIGH] Online-Mind2Web contains 300 tasks across 136 websites. Six agents are evaluated against human judgments. Four achieve approximately 28–31% success; Claude Computer Use 3.7 achieves 56.3%, and OpenAI Operator achieves 61.3% in Table 2. These results describe the paper's particular configurations and restrictions, including a starting website and an instruction against Google Search. They are not universal capability estimates for every deployment.

[A; HIGH] WebJudge is the proposed automatic evaluator. It extracts task requirements, identifies screenshots that matter, and judges success from those requirements, selected screenshots, and action history. Its o4-mini version averages 85.7% agreement with humans; WebJudge-7B averages 87.0%. Both remain imperfect. Their respective mean success-rate gaps are 3.8 and 3.9 percentage points in Table 2.

[D; MEDIUM] For security analysis, the useful lesson is that a web agent has several places where a user's intent can fail to become a correct action: requirement interpretation, visual grounding, navigation, filtering, confirmation, and assessment of success. The paper documents reliability failures at these places. It does not show that an attacker exploited them or that they make agents more attack-vulnerable than standalone language models.

## 2. Document roadmap and inventory

Title: *An Illusion of Progress? Assessing the Current State of Web Agents*. Authors: Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, and Yu Su. The affiliations shown on p. 1 are The Ohio State University and University of California, Berkeley. Weijian Qi and Tianneng Shi have equal-contribution markers; Huan Sun and Yu Su have corresponding-author markers. The supplied header identifies the work as a conference paper at COLM 2025; the acronym is not expanded in the supplied work.

The narrative follows this inventory. Original numbering is retained, and the following identifiers are also used in the coverage audit.

| ID | Original component | Pages | Function |
|---|---|---:|---|
| S0 | Abstract and title information | 1 | Overall motivation, benchmark and evaluator claims |
| S1 | §1 Introduction | 2 | Evaluation gap and three contributions |
| S2.1 | §2.1 Why Introduce a New Benchmark? | 3 | Critique of offline, sandbox and online benchmarks |
| S2.2 | §2.2 Dataset Construction | 3–4 | Filtering, task sources and difficulty |
| S3 | §3 WebJudge | 4–6 | Three-stage evaluator, inputs and cost |
| S4.1 | §4.1 Experimental Setup | 6 | Six agents, restrictions and annotation |
| S4.2 | §4.2 Main Results | 6–7 | Success, agreement, difficulty and robustness |
| S4.3 | §4.3 Comparison against Existing Evaluation Methods | 7–8 | Judge comparisons and trajectory-length analysis |
| S4.4 | §4.4 The Generalization of WebJudge | 8–9 | AgentRewardBench evaluation |
| S5.1 | §5.1 Agent Efficiency | 9 | Step-normalized efficiency |
| S5.2 | §5.2 Error Analysis and More Discussion | 9–10 | Error taxonomy and agent limitations |
| S6 | §6 Conclusions | 10 | Main synthesis and proposed uses |
| S7 | §7 Acknowledgments | 10 | Funding and resources |
| REF | References | 10–15 | Bibliographic provenance, not independent evidence checking |
| TOC | Appendix contents | 16 | Appendix inventory |
| A.A1–A.A2 | Appendix A Related Work | 17 | Agents, benchmarks and evaluators |
| A.B1–A.B5 | Appendix B Experimental Details | 17–20 | Granularity, search restriction, threshold, repeatability and detailed metrics |
| A.C1–A.C2 | Appendix C Task Construction | 20–21 | Website selection and distributions |
| A.D1–A.D2 | Appendix D Prompts | 22–25 | Benchmark-specific and general-purpose evaluator criteria |
| A.E | Appendix E Implementation Details | 26 | Models, interfaces, limits and training |
| A.F1.1–A.F1.4 | Appendix F Operator cases | 27–29 | Structured search, navigation, correction and constraint failures |
| A.F2–A.F3 | Appendix F Other agents and hallucinations | 28–30 | Search behavior and unsupported final claims |
| A.G | Appendix G Task Examples | 31 | Twenty task examples |
| A.H | Appendix H WebJudge Example | 32 | Requirement extraction, screenshot relevance and judgment |

Substantive visual inventory: Figures 1–7; Figure B.1; Figures C.1–C.2; Figures F.1–F.8. Figure 3 is also the sole architecture/workflow diagram. Figure C.1 has two distinct histogram panels, Figure 6 has bars and a second-axis efficiency line, and Figure F.6 has three agent panels. Tables: 1–5, B.1–B.5, and G.1. Equations: (1) and (2). There is no numbered algorithm or pseudocode block, theorem, lemma, or proposition. Appendix D contains operational prompts, and Appendix E contains implementation procedures.

Footnotes account for equal contributions and corresponding authors, the origin/difficulty of Mind2Web-Live tasks, and SimilarWeb as the website-popularity source. Recurring publication headers, page numbers, affiliation symbols, and acknowledgments are compressed as non-methodological context. No keywords are supplied. No formal numbered research questions or hypotheses appear.

## 3. Background and context

[A] A large language model, abbreviated LLM, supplies language-based reasoning and communication. A multimodal LLM, called MLLM in Appendix A, can also process images. In this paper, browser screenshots are especially important because the evidence for success often exists in the page interface rather than in an answer sentence.

A trajectory is the sequence of an agent's actions and observed screenshots while attempting a task. A reference trajectory is the human demonstration or annotated path associated with a task. Reference length is the number of steps a human annotator needs. A cached or offline benchmark saves website material for later evaluation; a sandbox benchmark recreates websites in a controlled environment; an online benchmark uses live websites. These are the paper's distinctions, not claims that any one design is best for every purpose.

LLM-as-a-judge means asking an LLM to classify or assess another system's output or behavior. Here the central decision is binary: success or failure. Human judgments are the reference standard used to measure agreement. Agreement rate is the fraction of matching binary decisions. Success rate is the fraction of attempted tasks judged successful. Agreement can be high even when some individual successes are missed or some failures are accepted; the paper consequently also reports success-rate gaps and, on AgentRewardBench, precision and recall.

[D; HIGH as a metric explanation] Precision concerns the reliability of positive success judgments; recall concerns how many human-positive successes the evaluator recovers. These meanings are consistent with the reported precision/recall/F1 comparisons, although the paper does not display their mathematical definitions. F1 is reported as a combined classification measure; no additional formula is attributed to the authors.

Grounding means connecting an intended action to the actual interface object. Appendix F.1.3 explicitly identifies selecting BLUE instead of BLACK as a grounding error. Exploration means inspecting alternative pages or interface features; exploitation or a greedy strategy means committing more directly to a selected course of action. The paper connects these behaviors to completion and step cost.

## 4. Research problem and gap

[A; HIGH] The existing problem is measurement: reported success may overstate realistic browser-task competence. The authors seek a smaller simulation-to-reality gap and an evaluator that preserves enough interaction evidence to make reliable judgments.

According to §2.1 and Appendix A, offline snapshots cannot fully represent dynamic websites and limit exploration beyond the stored trajectory. Sandboxes permit interaction but have limited website diversity because building full replicas is difficult. AssistantBench restricts tasks to time-invariant answer strings to enable automatic checking, excluding some current-information and procedural tasks. Mind2Web-Live has around 100 tasks and a key-node evaluator that can be disrupted by website changes.

The authors particularly scrutinize WebVoyager. They report only 15 websites, tasks synthesized from modified Mind2Web seeds, many relatively simple interactions, and automatic evaluation weaknesses. Their two-step search agent solves 51% of 100 sampled WebVoyager tasks, suggesting that substantial success need not require deep navigation. This is an experiment about shortcut susceptibility of that sample, not proof that every WebVoyager task is trivial.

The gap has two linked parts: a diverse, realistic live-web task collection and a scalable evaluator aligned with human judgments. The proposed scope is ordinary task completion and its evaluation. The paper does not define an attack model, inject malicious instructions, test data theft, or evaluate unauthorized actions.

## 5. Research questions, objectives and hypotheses

[A] Explicit objectives are: rigorously assess current web-agent competence; construct realistic tasks across many live websites; develop more reliable automatic evaluation; and compare agent strengths, limitations, and efficiency. The three contributions in §1 map to benchmark construction, WebJudge, and comparative analysis.

No formal hypotheses or named research questions are supplied. For organizing the evidence only, the following are analyst-formulated questions, not author quotations:

- O1: How do six agents perform on the new live-web benchmark under controlled website-navigation conditions?
- O2: Does selecting relevant intermediate screenshots improve automatic judgment relative to existing evaluators?
- O3: How do task difficulty, trajectory length, evaluator granularity, screenshot threshold, and search access affect results?
- O4: How well does WebJudge transfer to other benchmark trajectories?
- O5: Which efficiency patterns and error types help explain observed performance?

[D] The user's security question is a separate research lens: which observed interaction and evaluation weaknesses could matter when analyzing security? The supplied experiments answer O1–O5 much more directly than this security question. A direct comparative vulnerability conclusion remains unsupported.

## 6. Assumptions / Threat Model

There is no author-defined security threat model. Attacker capabilities, attacker-controlled pages, malicious tools, credential exposure, authorization boundaries, and security-specific success criteria are not specified or tested. Their absence is a scope boundary, not a negative result showing safety.

[A] The evaluation assumes task descriptions, action records, screenshots, and human annotation can establish whether required actions occurred. Tasks are initialized at a start URL. Agents are prompted not to use Google Search so that alternative websites and search shortcuts do not confound navigation comparisons. Strong CAPTCHA-protected websites are filtered out; the acronym is not expanded by the supplied paper. Consequently, results do not measure agents' ability to operate across all real-world access barriers.

[A] Human judgment is the reference standard: at least two annotators label each task trajectory, with a third resolving conflicts. The paper does not report an inter-annotator agreement statistic or establish that every adjudicated label is indisputable.

[A] WebJudge assumes an LLM can identify necessary requirements and score screenshot relevance. Appendix B.1 acknowledges that generated key points may be inaccurate or unnecessary. The screenshot threshold therefore controls an evidence trade-off rather than guaranteeing preservation of every decisive state.

[D; MEDIUM] The task description, observation stream, action representation, and outcome judge are candidate components to inspect in a future security model. Calling them candidate surfaces is an analyst interpretation based on the workflow. Their resistance to manipulation is UNKNOWN in this study.

## 7. Methodology

### Dataset construction

[A; HIGH] The authors randomly select 650 original Mind2Web tasks for viability assessment. They report that 47% are invalid or have outdated ground-truth trajectories. They filter ambiguous instructions, obsolete or unexecutable tasks, and tasks on strongly CAPTCHA-protected websites. This is a combined invalidity/outdated-reference statistic; it should not be paraphrased as 47% malicious or 47% impossible solely because of bot protection.

The final sources are 167 selected Mind2Web tasks, 24 rewritten Mind2Web tasks, 34 Mind2Web-Live tasks, and 75 manually created tasks. [C] The stated source counts reconcile: 167 + 24 + 34 + 75 = 300. Rewriting primarily changes requirements for solvability or clarifies ambiguous descriptions. Website selection prioritizes traffic reported by SimilarWeb, chooses different websites where possible, adds previously unrepresented popular websites, and includes 14 tasks from niche websites plus some regional sites such as UK sites. The 14 niche tasks are part of the constructed set, not an additional 14 beyond 300.

Difficulty uses human reference length: easy has at most five steps; medium has six through ten; hard has at least eleven. Counts are 83 easy, 143 medium, and 74 hard. [C] These sum to 300; their shares are approximately 27.7%, 47.7%, and 24.7%, respectively, calculated by dividing each count by 300. The dataset has 136 unique websites and 12 domains. No benchmark train/validation/test partition is specified for these 300 evaluation tasks. Separate training/held-out agent groups are reported for the screenshot model, not a standard task-level split of the benchmark.

### WebJudge procedure

[A] Input consists of task T, actions A, and screenshots I. Stage 1 extracts explicit task requirements K. Stage 2 describes each screenshot and assigns relevance from 1 to 5, selecting scores at least 3. Stage 3 judges success using the task, key points, selected screenshots, relevance explanations, and action history. The default outcome mode uses chain-of-thought, abbreviated CoT in Appendix B, meaning a reasoning-based final judgment. The alternative keypoint-wise mode judges each requirement separately and requires all to pass.

The evaluator does not depend on intermediate agent thoughts or the final agent response. This permits agents that do not expose these outputs and avoids treating potentially hallucinated final claims as decisive evidence. The authors suggest reduced self-preference bias because the principal evaluated content is environment observation rather than generated answer prose. They do not provide a dedicated self-preference-bias experiment.

### Operational success criteria

[A] Appendix D matters to what success means. Filters must visibly take effect; exact numerical ranges must match; keyword searches alone cannot guarantee all requested constraints; some tasks require submission or visible results. The benchmark-specific prompt allows success after a correctly performed action returns no matches and permits selecting qualifying items without applying a filter when the full available set is already shown. The general-purpose prompt instead explicitly condemns repeated actions and loops with no visible progress; those benchmark-specific exceptions are not included in its listed criteria.

Thus, the two prompt variants are substantively similar but not identical. Strict filter-use expectations can classify a seemingly plausible answer as failure. Appendix H illustrates an allowed full-list exception: a male senior Boxer is selected from the complete visible set despite no sex-filter toggle.

### Agents and implementation

[A; HIGH] SeeAct, Browser Use, and Agent-E use Playwright, with maximum 25 steps and GPT-4o model version gpt-4o-2024-08-06. Claude Computer Use uses the Computer Use OOTB Tool with local Chrome. The paper names claude-3-5-sonnet-20241022 for Claude Computer Use and separately says Claude 3.7 has a 50-step limit and thinking mode disabled; it does not give an equally explicit Claude 3.7 model identifier. A Claude 3.5 step limit is not separately specified. Operator uses OpenAI's remote browser and web interface because the authors report no API access; they collect its actions and screenshots there.

SeeAct and Agent-E capture extended full-page screenshots. Browser Use, Claude, and Operator capture visible-screen portions. Action histories are normalized using element attributes and actions for the open-source agents; Claude histories include coordinates; Operator uses supplied action descriptions. These representations differ, which is relevant to comparability.

Automatic evaluators use gpt-4o-2024-08-06 or o4-mini-2025-04-16. GPT-4o temperature is zero; o4-mini reasoning effort is medium. AgentRewardBench uses gpt-4o-2024-11-20 for compatibility with prior results, the general-purpose prompt, screenshots instead of accessibility trees, and action histories concatenated with their reasoning. This latter condition qualifies the broad claim that no agent reasoning is needed: it is not required by the architecture, but some external-benchmark action inputs include reasoning.

### WebJudge-7B training

[A] The lightweight model is based on Qwen2.5-VL-7B and replaces screenshot description/relevance scoring, not the entire evaluator. Synthetic training labels come from GPT-4o, GPT-4.1-mini, Claude 3.7, and Qwen2.5-VL-72B. Training trajectories are from SeeAct, Browser Use, and Claude 3.5; Agent-E, Claude 3.7, and Operator are held-out agent groups. The supplied text does not give training-example counts or establish task-level separation.

Training uses four H100 GPUs with 80 GB each, bfloat16 precision, batch size 256, sequence length 4096, five epochs, learning rate 5e-6, cosine scheduling, and 10% warmup. Inference still uses an LLM for key-point identification and outcome judgment, producing two API calls per trajectory. On Online-Mind2Web these stages are described as o4-mini; the AgentRewardBench description specifies GPT-4o-2024-11-20 for consistency. The two-call claim concerns remote API calls, not elimination of local screenshot-processing computation.

## 8. Experiments / Analyses

| ID | Purpose and conditions | Evidence and result | Main qualification |
|---|---|---|---|
| X1 | Test shortcut solutions on 100 randomly sampled, website-stratified WebVoyager tasks | Two-step search agent achieves 51%; Fig. 2, p. 3 | Only sampled tasks; per-site denominators absent |
| X2 | Apply the search agent to 100 Online-Mind2Web tasks: 33 easy, 34 medium, 33 hard | Overall 22%; nearly 50%, 18%, 3% by difficulty; p. 4 | Difficulty-balanced sample differs from full benchmark distribution |
| X3 | Assess viability of 650 original Mind2Web tasks | 47% invalid or outdated references; p. 4 | No category breakdown or uncertainty interval |
| X4 | Evaluate six agents on the 300-task benchmark and compare judge outputs | Human success 28.0–61.3%; Table 2 | Model/interface/step-budget conditions differ |
| X5 | Compare performance by reference-length difficulty | Easy-to-medium and medium-to-hard declines; Fig. 4 | Difficulty is human step count, not an independently validated complexity scale |
| X6 | Compare automatic judges with human binary labels | Tables 2–3; WebJudge averages 83.6%, 85.7%, 87.0% agreement | Missing cells and different supported inputs affect averages |
| X7 | Study Operator trajectory length | Fig. 5; WebJudge remains relatively aligned up to 80 steps | Bin counts and exact points not supplied |
| X8 | Transfer to AgentRewardBench's 1,302 trajectories across five benchmarks | Tables 4–5 and B.5; precision/recall and success-rate gaps | Distinct datasets, prompts, model version and metric |
| X9 | Compare outcome granularity | Tables B.1–B.2; CoT 83.7%, keypoint-wise 81.7%, combined 84.6% overall agreement | Study sample and combined-mode selection rule incompletely specified |
| X10 | Allow Browser Use Google Search | Tables B.3: 26% without, 31% with | Baseline does not match Table 2's 30.0%; unresolved |
| X11 | Vary screenshot threshold on Operator trajectories | Table B.4: 79.3%, 81.8%, 77.0% for thresholds 2, 3, 4 | One agent's ablation motivates threshold used everywhere |
| X12 | Repeat GPT-4o judge evaluation three times | Average success-rate SD 1.1%, maximum 1.8%; Fig. B.1 | Evaluator repeatability, not repeated agent trials |
| X13 | Analyze steps and efficiency | Eq. 2 and Fig. 6; Operator efficiency ratio 2.6 | Efficiency uses successful tasks only |
| X14 | Classify errors and illustrate behaviors | Fig. 7 and F.1–F.8 | Error-category sample/counts and case-selection procedure absent |

No named statistical significance test, p-value, confidence interval for main agent performance, or systematic adversarial experiment is supplied. Statements using 'significantly' therefore should not be converted into claims of demonstrated statistical significance.

## 9. Results

[A; HIGH] Table 2 gives human success rates: SeeAct 30.7%, Agent-E 28.0%, Browser Use 30.0%, Claude 3.5 29.0%, Claude 3.7 56.3%, and Operator 61.3%. The descriptive ranking puts Operator first and Claude 3.7 second. [C] Operator exceeds Claude 3.7 by 61.3 − 56.3 = 5.0 percentage points. This arithmetic does not establish significance or comparative security.

[A] Figure 4 reports easy/medium/hard success percentages, respectively: SeeAct 60.2/25.2/8.1; Claude 3.7 90.4/49.0/32.4; Claude 3.5 56.6/20.3/14.9; Browser Use 55.4/26.6/8.1; Agent-E 49.4/26.6/6.8; Operator 83.1/58.0/43.2. Claude 3.7 leads on easy tasks, whereas Operator leads on medium and hard tasks. All agents deteriorate with longer reference trajectories.

[C] Using those plotted values, mean easy success is 65.85%, mean medium success 34.283%, and mean hard success 18.917%. Their differences are approximately 31.6 and 15.4 percentage points. The prose calls these drops '31.6%' and '15.4%'; the values correspond to absolute rate differences, not relative percent reductions.

[A] On Online-Mind2Web, GPT-4o WebJudge has 83.6% average agreement and 7.8-point average gap; o4-mini has 85.7% and 3.8 points; WebJudge-7B has 87.0% and 3.9 points. A small average success-rate gap is not the same as nearly perfect task-level agreement. The authors' ranking-alignment statement is also approximate: o4-mini gives Browser Use 26.0% versus SeeAct 30.0%, reversing their human ordering, while WebJudge-7B reverses Browser Use and Claude 3.5.

[A] On AgentRewardBench, WebJudge-o4-mini's 82.0% overall precision accompanies 47.8% recall and 60.4% F1. GPT-4o WebJudge has lower precision, 73.7%, but higher recall, 71.2%, and F1, 72.4%. WebJudge-7B reports 75.7/58.0/65.6. Thus, highest precision among WebJudge variants does not mean strongest overall recovery of human-positive trajectories.

[A] Operator's error distribution is dominated by filter/sorting errors, 57.7%, followed by navigation errors, 19.6%, misunderstanding, 11.3%, incomplete steps, 6.2%, and others, 5.2%. These percentages describe categorized errors, not percentages of all 300 tasks. The underlying category counts are not given.

## 10. Figure-by-figure interpretation

### Figure 1 — Reported performance versus new manual evaluation, p. 1

[B] A grouped bar chart compares blue WebVoyager self-reported rates and salmon Online-Mind2Web manually evaluated rates. The x-axis lists agents; the y-axis is success rate in percent from 0 to 100 on a linear scale. Exact displayed comparisons are Claude 3.5: 52 versus 29; Agent-E: 61 versus 28; Browser Use: 89 versus 30; Operator: 87 versus 61. Red annotations show drops of 23, 33, 59, and 26. SeeAct has 31 and Claude 3.7 has 56 for the new benchmark, without paired older bars.

[C] Those paired drops are percentage-point differences. Figure values are rounded relative to Table 2. [D] The figure supports a warning about evaluation-dependent performance, but benchmark, judge, and configuration changes are entangled; it is not an isolated causal estimate of benchmark inflation.

### Figure 2 — Search-agent shortcuts, p. 3

[B plus supplied extraction] Blue per-website WebVoyager bars and a salmon Online-Mind2Web bar use a 0–100% success axis. The plotted WebVoyager sites have labeled rates: Cambridge Dictionary 86, Amazon 83, Coursera 83, Google Search 83, ESPN 75, GitHub 71, arXiv 57, Allrecipes 57, Apple 43, BBC 43, Hugging Face 33, WolframAlpha 17, Booking 0, Google Maps 0, Google Flights 0. Overall WebVoyager is 51 and Online-Mind2Web 22.

The same simple search procedure succeeds much less on the new sample. Site-specific sample sizes are absent, so 86 versus 83 should not be treated as a robust ranking of site difficulty. The overall samples are 100 tasks each, with different stratification/difficulty composition.

### Figure 3 — WebJudge workflow, p. 5

[B] This is a directed workflow diagram, not a performance plot. A top task box requests the newest refrigerator, 34–36 inches wide, priced $1,000–$2,000, rated at least four stars. A blue requirement box lists four conditions. The screenshot box contains selected and discarded frames, indicated by green checks and red exclusion symbols. Arrows carry task requirements and relevant visual evidence to a green outcome-judgment box, yielding success or failure. The pictured example demonstrates the structure of evidence selection, not a measured success rate.

### Figure 4 — Difficulty breakdown, p. 7

[B plus extraction] Grouped bars encode overall in red, easy in very pale gray, medium in light blue, and hard in dark blue. The y-axis is linear success percentage, 0–100; the x-axis lists six agents. Exact values are reproduced in §9. Operator's medium/hard rates are 58.0/43.2, compared with Claude 3.7's 49.0/32.4. Claude 3.5's hard rate of 14.9 exceeds the three open-source agents but remains low. No uncertainty bars appear.

### Figure 5 — Agreement versus Operator action steps, p. 7

[B] The x-axis is number of steps, roughly 10–80; the y-axis is agreement percentage, 0–100. Red squares represent WebJudge, dark blue dashed markers Autonomous Evaluation, and teal markers WebVoyager. Values fluctuate rather than declining monotonically. At the longest plotted trajectories, the red series remains high while the alternatives fall sharply; the dark blue series approaches the bottom of the chart.

Exact point values and bin sizes are not labeled, so this report does not invent numerical coordinates. [A] The authors attribute the pattern to missing intermediate evidence for final-screenshot judging and excess screenshots for WebVoyager. [D] The visual alone does not isolate those mechanisms from other properties of long tasks.

### Figure 6 — Steps and normalized efficiency, p. 9

[B] Green bars show average steps for successful tasks, pink bars failed tasks, against the left axis from 0 to 50. A teal line uses the right efficiency axis. Labeled ratios in plotted order are SeeAct 2.0, Claude 3.7 2.1, Claude 3.5 1.3, Agent-E 1.0, Browser Use 1.1, Operator 2.6. Lower ratios indicate fewer steps relative to the human reference, conditional on success. Failure bars generally exceed success bars, particularly for Claude 3.7, Browser Use, and Operator. Exact bar heights are not labeled; no exact step means are asserted here.

### Figure 7 — Operator error composition, p. 9

[B] A pie chart labels filter/sorting 57.7%, navigation 19.6%, misunderstanding 11.3%, incomplete step 6.2%, and others 5.2%. There are no axes or intervals. [C] The percentages sum to 100.0%. It supports prioritizing filter/sorting failures within the analyzed error set, not a statement that 57.7% of every Operator attempt fails this way.

### Figure B.1 — Judge repeatability, p. 19

[B] A point/error-bar plot shows WebJudge success rate percentages by agent; error bars represent standard deviation across three runs, not confidence intervals. Visible annotations in plotted order are SeeAct 39.8 ± 1.2, Claude 3.7 59.7 ± 1.2, Claude 3.5 34.7 ± 1.0, Agent-E 40.1 ± 0.8, Browser Use 35.8 ± 1.8, Operator 71.8 ± 0.8.

These labels conflict with Table 2 for Claude 3.5, Agent-E, and Browser Use; the values 34.7, 40.1, and 35.8 correspond to different agents there. The visual was inspected, and its apparent mapping is reported without repair. The supplied evidence cannot determine whether the figure labels or table assignments are responsible.

### Figure C.1 — Popularity and reference-length distributions, p. 21

[B] Two histograms show task counts. Left: website popularity, with logarithmically spaced x-axis labels from about 10^5 to 10^11; popularity is author-defined as monthly user clicks according to SimilarWeb. Right: reference length, roughly 0–30 steps on a linear axis. Both show a count y-axis. Most tasks visually occupy middle popularity ranges and relatively short-to-medium reference lengths. Exact bin edges/counts are not confidently readable and are not reconstructed. Website popularity is not the same as task-use frequency.

### Figure C.2 — Website-domain composition, p. 21

[B] A multicolor donut chart has 136 total websites and 12 categories at its center. It describes websites by domain, despite prose/caption language referring to tasks or task domains. Shopping/e-commerce is the largest visible segment, labeled 17.6%; entertainment/media and travel/transportation are each 11.8%; education is 11.0%. Small labels are not all confidently readable, so the complete exact category-percentage distribution is not asserted. All 12 domain names are listed in §19.

### Figures F.1 and F.2 — Operator's useful interaction strategies, p. 27

[B] F.1 shows a sequence of retailer interfaces for selecting 8K Samsung open-box televisions. It illustrates structured filtering, with no plot axes or measured effect. F.2 shows browser page search for 'Compare' and the 'Compare Side by Side' feature for the Audi comparison task. The supporting text reports Ctrl+F use. The screenshots illustrate navigation mechanisms; they are selected cases rather than controlled tests of how often the strategies succeed.

### Figure F.3 — Correction of a grounding mistake, p. 28

[B] Two clothing-site screenshots are connected by a verification/self-correction arrow. The first action intends BLACK but selects BLUE; the next deselects BLUE and selects BLACK. This is direct visual evidence of a state-changing correction sequence, accompanied by author explanation. It does not establish correction reliability over all grounding mistakes.

### Figures F.4 and F.5 — Numeric and temporal failures, pp. 28–29

[B/A] F.4 displays the used-car interface for a task requiring model years 2004–2012, while the applied range is 2001–2012. F.5 presents three flight-interface states for an arrival window of 8:00–11:00 PM. The authors report an incorrectly adjusted slider. The latter small screenshot labels are not uniformly legible; the exact erroneous final time bounds are therefore not asserted. Both illustrate failures to translate explicit ranges into interface settings.

### Figure F.6 — Keyword-search behavior across three agents, p. 29

[B] Three panels show Browser Use, Agent-E, and SeeAct issuing shopping queries for 27–32-inch Samsung or LG monitors with 4K IPS displays and lowest price. The images support observing loosely structured search approaches. The nearby p. 28 text mistakenly references Figure F.2 for this three-agent example; F.6 is the matching visual. Precise query strings are small and are deliberately not transcribed as reliable exact text.

### Figures F.7 and F.8 — Unsupported final-response assertions, p. 30

[B/A] F.7 shows a CarMax results interface; the accompanying Browser Use response claims cars near Kentwood while naming locations in Kenosha and Murrieta. F.8 shows a jobs page; the accompanying response claims the most recent jobs despite no use of the sort function. These are examples of a mismatch between claimed satisfaction and visible interaction evidence. Neither case involves an attacker, malicious page instruction, or proven data fabrication beyond the specific unsupported constraint claims described.

## 11. Table-by-table interpretation

### Table 1 — Evaluator input requirements, p. 6

Rows are Autonomous Evaluation, AgentTrek, WebVoyager, and WebJudge. Columns indicate screenshots, action history, ability to operate without intermediate thoughts, and ability to operate without final response. All use screenshots. Autonomous Evaluation and WebJudge support action history and both omissions. AgentTrek uses actions but requires intermediate thoughts. WebVoyager has no action-history check and requires the final response. The two 'w/o' columns indicate independence from those outputs, not consumption of absent data.

### Table 2 — Success and agreement, p. 6

All numerical entries are percentages. For compact precision, each judge pair below is success rate/agreement rate:

| Agent | Human SR | GPT-4o pair | o4-mini pair | 7B pair |
|---|---:|---:|---:|---:|
| SeeAct | 30.7 | 39.8/86.7 | 30.0/85.3 | 28.0/86.0 |
| Agent-E | 28.0 | 34.7/86.0 | 27.0/86.3 | 26.0/87.3 |
| Browser Use | 30.0 | 40.1/81.4 | 26.0/89.3 | 24.3/88.3 |
| Claude 3.5 | 29.0 | 35.8/86.3 | 24.0/87.0 | 26.0/89.7 |
| Claude 3.7 | 56.3 | 59.7/79.1 | 47.3/82.3 | 48.7/84.3 |
| Operator | 61.3 | 71.8/81.8 | 58.3/83.7 | 59.0/86.3 |
| Average gap/AR | — | 7.8/83.6 | 3.8/85.7 | 3.9/87.0 |

The average row combines a gap statistic with agreement, not an average success rate. [C] For o4-mini, the absolute differences from human rates are 0.7, 1.0, 4.0, 5.0, 9.0, and 3.0 points; their mean is 22.7/6 = 3.783 points, consistent with 3.8 after rounding. No statistical significance symbols appear.

### Table 3 — Agreement among evaluators, p. 7

GPT-4o averages: Autonomous Evaluation 79.4%, AgentTrek 66.9%, WebVoyager 73.9%, WebJudge 83.6%. o4-mini averages: Autonomous Evaluation 79.5%, WebVoyager 78.7%, WebJudge 85.7%. WebJudge-7B averages 87.0%. AgentTrek has missing entries for the Claude agents and Operator; WebVoyager lacks SeeAct because the required final response is unavailable. A dash is unavailable/not evaluated, not zero. Average comparisons therefore do not always use identical agent sets.

WebJudge's complete agent-level agreement values are in Table 2. A notable non-uniform result is that GPT-4o WebJudge agrees only 79.1% for Claude 3.7, despite its strong agent success; evaluator difficulty varies by trajectory group.

### Table 4 — Out-of-domain precision, p. 8

Column order is AssistantBench, VisualWebArena, WebArena, WorkArena, WorkArena++, overall. Row values are:

- Rule-based: 25.0, 85.2, 79.0, 100.0, 83.3, 83.8.
- Autonomous Evaluation: 83.3, 61.2, 67.6, 96.4, 59.3, 67.6.
- GPT-4o accessibility tree: 77.8, 63.0, 70.2, 94.6, 63.0, 69.8.
- WebJudge-GPT-4o: 66.7, 69.8, 72.6, 92.3, 75.0, 73.7.
- WebJudge-7B: 80.0, 66.7, 77.5, 100.0, 70.0, 75.7.
- WebJudge-o4-mini: 100.0, 74.5, 81.2, 100.0, 90.0, 82.0.

Stars indicate results imported from the cited AgentRewardBench paper, not newly reproduced baselines verified independently here. GPT-4o version is controlled to 2024-11-20. The rule-based overall precision of 83.8 exceeds all WebJudge variants, qualifying language about outperforming 'existing methods': WebJudge improves upon the listed LLM baselines overall, not every method on every metric. WorkArena has three 100% ties. Overall values should not be assumed to be unweighted means of the five columns.

### Table 5 — Success-rate estimates across external benchmarks, p. 9

Rows are Claude 3.7, GPT-4o, Llama 3.3, and Qwen2.5-VL agents. Each evaluator has columns for VisualWebArena, WebArena, and WorkArena++. Llama's VisualWebArena cells are missing. Human rates include Claude 28.3/55.1/18.4, GPT-4o 35.9/42.3/18.4, Llama —/22.4/9.2, and Qwen 21.7/33.3/13.8.

Average absolute gaps are accessibility-tree GPT-4o 8.1, rule-based 9.8, WebJudge-GPT-4o 5.9, WebJudge-o4-mini 10.5, and WebJudge-7B 6.0 percentage points. Benchmark-specific gaps in the same order are 10.5/10.3/3.4; 9.1/12.2/8.0; 5.4/6.5/5.7; 8.7/10.9/12.0; and 4.4/4.5/9.2. The 7B variant is closest on VisualWebArena and WebArena among these gap rows; GPT-4o WebJudge is closer on WorkArena++ than 7B.

A concrete example shows conservatism: Claude 3.7 on WebArena has 55.1% human success but only 33.3% under o4-mini WebJudge. [C] The difference is 21.8 points. Full individual cells beyond these examples are deliberately compressed; the supplied table is inspected but not exhaustively duplicated.

### Tables B.1 and B.2 — Judgment granularity and tokens, p. 18, text-only

B.1 reports CoT versus keypoint-wise agreement: 86.1 versus 87.9 when key points are at most three; 81.4 versus 76.3 when there are more than three; overall 83.7 versus 81.7. Combined mode reaches 84.6 overall, with no subgroup entries. Mean key-point count is 3.6, reported on p. 17. The default CoT is chosen for cost and performance.

B.2 gives per-task token counts by key-point identification, screenshot identification, outcome judgment, and total. CoT: 241, 47k, 20k, 67k. Keypoint-wise: 241, 47k, 73k, 120k. These are rounded token quantities, not dollar costs. [C] 120k/67k is approximately 1.79, so the table supports a substantial cost difference; it does not precisely establish a factor of two in tokens. The text describes CoT as approximately half the total cost.

### Tables B.3 and B.4 — Search and threshold ablations, p. 19

B.3 reports Browser Use 26% without search and 31% with search. [C] This is a five-percentage-point increase, or approximately 19.2% relative to 26%; the point difference is the more direct comparison. The unresolved mismatch with Table 2 is retained.

B.4 gives Operator judge agreement for threshold 2: 79.3%; threshold 3: 81.8%; threshold 4: 77.0%. Threshold 3 wins among these three conditions. It does not establish a universal optimum over every possible scoring policy.

### Table B.5 — Precision, recall and F1, p. 20, text-only

Overall triples are rule-based 83.8/55.9/67.1; o4-mini 82.0/47.8/60.4; GPT-4o 73.7/71.2/72.4; WebJudge-7B 75.7/58.0/65.6. Benchmark-specific triples are retained here because they materially qualify transfer claims:

| Benchmark | Rule-based P/R/F1 | o4-mini P/R/F1 | GPT-4o P/R/F1 | 7B P/R/F1 |
|---|---|---|---|---|
| AssistantBench | 25.0/12.5/16.7 | 100.0/25.0/40.0 | 66.7/50.0/57.1 | 80.0/50.0/61.5 |
| VisualWebArena | 85.2/58.2/69.2 | 74.5/51.9/61.2 | 69.8/75.9/72.7 | 66.7/58.2/62.2 |
| WebArena | 79.0/53.8/64.0 | 81.2/58.0/67.6 | 72.6/82.4/77.2 | 77.5/72.3/74.8 |
| WorkArena | 100.0/91.9/95.8 | 100.0/54.1/70.2 | 92.3/64.9/76.2 | 100.0/56.8/72.4 |
| WorkArena++ | 83.3/38.5/52.6 | 90.0/17.3/29.0 | 75.0/46.2/57.1 | 70.0/26.9/38.9 |

High precision can coincide with very low recall: o4-mini's WorkArena++ recall is 17.3%. The caption names GPT-4o and o4-mini but the table also includes rule-based and 7B rows. This is caption compression, not grounds to discard those rows.

### Table G.1 — Task examples, p. 31, text-only

Twenty examples are grouped as five Mind2Web-Live, five Mind2Web, and ten newly constructed tasks. They include car browsing, baggage information, lost-item information, shipping-rate calculation, clothing price constraints, insurance/distance filtering, housing amenities, a music-chart repost, a trending-repository issue, a conference video, movie availability, hotel/transit planning, a tax calculator, meme creation, chess, a driver download, and class schedules. These examples show task variety; they are not additional evaluation results or proof of representativeness. All twenty were inspected, with repeated task wording deliberately compressed.

## 12. Diagram / Architecture Interpretation

Figure 3 expresses two converging evidence paths. The task provides the conditions to check and also supplies context for the final judge. The requirement extractor produces key points. Those points condition screenshot relevance assessment so the selector can retain states showing filters, actions, results, or other decisive evidence. Selected frames and action history then feed the outcome judge, which returns a binary label.

[A] The workflow preserves intermediate evidence while reducing the amount submitted to final judgment. A final screenshot alone can hide earlier completed steps; every screenshot can overwhelm the context. Selection is intended to balance these failures.

[D] The diagram contains no explicit adversarial-input validation, independent browser-state attestation, or permission-checking component. This is an observation about what the supplied architecture depicts, not proof that deployments lack such controls. WebJudge-7B changes the implementation of screenshot selection while leaving the two other stages dependent on an LLM.

Appendix H provides a text-only worked example. A blank page is scored 1, while a relevant pet-search result screenshot is scored 4 despite an unchecked sex filter. The final judgment accepts selecting a qualifying male from the complete visible list. The intermediate screenshots represented by ellipses are unavailable within the example; no reconstruction of the complete trajectory is attempted.

## 13. Equations and mathematical concepts

### Equation (1), p. 5

`O = Evaluator(T, A, I)`.

[A] This is a functional description of binary outcome classification. T is the task description; A = (a1, …, an) is the action sequence; I = (i1, …, in) is the screenshot sequence; O is Success or Failure. The evaluator's internal steps produce key requirements K = (k1, …, km), score screenshots, retain selected evidence, and judge the outcome. The equation is not a training loss, optimization objective, or probability model. It does not quantify uncertainty or require a particular implementation.

Screenshot relevance ranges from 1 to 5 and uses an inclusive threshold: score at least 3 is retained. §3 calls the threshold δ; Appendix B.3 calls it θ. Their descriptions imply the same role, but this notation change is disclosed rather than silently ignored.

### Equation (2), p. 9

`E = (1 / |T_succ|) Σ_{i in T_succ} (S_i / Ŝ_i)`.

[A] S_i is the agent's step count for task i; Ŝ_i is that task's human reference length; T_succ is the set of tasks the agent completes successfully; |T_succ| is its size; Σ adds the ratios. E is dimensionless. Each successful task contributes its agent-to-human step ratio equally. Lower E means fewer normalized steps, not higher task success. E = 1 corresponds to matching the human reference on average; Operator's 2.6 indicates 2.6 times reference steps under this definition.

[D] The metric is conditional on success. Different agents may succeed on different task subsets, so their E values do not automatically compare identical workloads. The equation requires a nonempty success set and nonzero reference lengths; the paper does not discuss undefined cases. It is a mean of ratios, not the ratio of summed steps, and no conversion to elapsed time follows without additional measurements.

No theorem, formal proof, optimization convergence analysis, or security-bound equation is supplied.

## 14. Interpretation and Discussion

[A] The authors conclude that current agents remain weaker on realistic live navigation than headline WebVoyager rates imply. Their evidence is a combination of benchmark redesign, manual evaluation, shortcut testing, and evaluator comparisons. They position intermediate-screenshot selection as the central reason WebJudge better aligns with human judgments.

[D] The strongest supported interpretation is conditional: these six configurations struggle on this collection under these constraints. The design does not isolate the causal share of task difficulty, different model versions, search restrictions, judgment criteria, or interfaces in the cross-benchmark performance drop. It also does not establish a population-level failure rate for all real users.

Important source inconsistencies and qualifications are retained:

1. Browser Use has 30.0% human success in Table 2, but 26% without search in Table B.3 and §B.2. The ablation's sample/model/run differences are not specified sufficiently to reconcile them.
2. Figure B.1 appears to assign 34.7 to Claude 3.5, 40.1 to Agent-E, and 35.8 to Browser Use, while Table 2 assigns 35.8, 34.7, and 40.1 respectively. The three-run means might differ, but the permutation remains unexplained.
3. Table B.1 CoT overall agreement is 83.7, while the main GPT-4o average is 83.6. The ablation's sample or aggregation is not fully specified, so neither number replaces the other.
4. The p. 28 three-agent keyword-search paragraph cites F.2, whereas Figure F.6 on p. 29 matches its content.
5. Difficulty declines written as percentages correspond to percentage-point differences when reconstructed from Fig. 4.
6. Table 4's rule-based 83.8% precision exceeds WebJudge-o4-mini's 82.0%. Claims of superiority depend on the selected comparator and metric.
7. Ranking alignment is approximate; lower-performing agent orderings sometimes change under automatic evaluation.
8. 'No intermediate thoughts required' describes compatibility, while the AgentRewardBench procedure concatenates available reasoning with actions.
9. Figure C.2 describes domain composition of 136 websites, not an exact task-domain distribution.
10. Appendix B.5 calls RFT 'reinforcement tuning,' whereas §4.4 calls it 'Rejection Sampling Fine-Tuning.' The supplied terminology is inconsistent.

For the security research question, [D; MEDIUM] the documented failures suggest mechanisms to investigate: constraints can be mistranslated into actions; long interaction histories complicate verification; repeated or exploratory actions create more opportunities for mistakes; and unsupported final claims can fool weak judges. [UNKNOWN] Whether an adversary can exploit these mechanisms, whether such exploitation is more frequent than with standalone LLMs, and what defenses work are not established.

## 15. Contributions and novelty

[A] Dataset/benchmark contribution: Online-Mind2Web updates and diversifies live tasks across 136 websites, with validity filtering and reference-step difficulty labels.

[A] Methodological contribution: WebJudge combines explicit requirement extraction, relevance-based intermediate-screenshot selection, and final judgment. Its core contribution is evidence selection for evaluation, not a new web-agent navigation policy.

[A] Implementation contribution: WebJudge-7B uses a fine-tuned local vision-language model for screenshot selection, reducing remote API calls to two per trajectory while retaining LLM stages.

[A] Empirical contribution: the paper manually compares six agents, tests judge agreement and external transfer, studies difficulty and efficiency, and categorizes failures. The authors describe the comparative analysis as the first comprehensive one; this priority claim is author-reported and was not externally checked.

No theoretical security contribution, vulnerability exploit, verified defense, or direct standalone-LLM comparison is supplied. [D] Its security contribution for this literature review is evidence about operational reliability and outcome verification, which should remain distinct from measured adversarial robustness.

## 16. Limitations

### Authors' stated limitations

[A] WebJudge's cost and latency scale with screenshot count before the lightweight selector is introduced; long Operator trajectories are costly. Generated key points can be inaccurate or unnecessary, making all-keypoints-required judgment overly strict. Even temperature-zero GPT-4o remains somewhat random. WebJudge-o4-mini is conservative on AgentRewardBench, causing low recall and larger success-rate gaps. Live websites change, requiring benchmark maintenance. Search is a natural strategy for some tasks even though prohibited in the main comparison. Some agents lack final responses or reasoning traces, motivating broader evaluator compatibility.

[A] Operator fails numeric and temporal constraints and sometimes misses niche features. Other agents neglect requirements, hallucinate satisfaction, terminate prematurely, repeat actions, explore poorly, and overuse keywords. These are agent limitations, separate from limitations of the study's design.

### Additional evidence-based analyst observations

[D] Agent step budgets and interfaces are unequal; disabling Claude 3.7 thinking affects the meaning of its result. Full-page versus viewport screenshots change available evidence. Strong bot-protection exclusions limit realism for some environments. Popularity-oriented website selection does not demonstrate representative task-use sampling. The authors do not report annotation agreement, main-result confidence intervals, attack experiments, or multiple independent agent-run distributions.

[D] The screenshot model's held-out groups are agent identities; task-level non-overlap is not specified. Some reported improvements compare averages over different available agents. Strict sorting/filtering criteria can encode a particular operational definition of success rather than every acceptable user solution. The identified table/figure disagreements limit exact reproduction of selected findings.

## 17. Threats to validity

The following categories are analyst-applied, not a claim that the authors use this taxonomy.

- Internal validity [D; MEDIUM]: different browser environments, model versions, action representations, step caps, and screenshot viewpoints can influence comparative outcomes. Website changes during evaluation are another uncontrolled possibility; a synchronized evaluation schedule is not supplied.
- Construct validity [D; MEDIUM]: reference length operationalizes task difficulty, and strict prompt criteria operationalize success. Neither automatically measures every dimension of useful assistance. Reliability failure is not equivalent to security vulnerability.
- External/ecological validity [D; MEDIUM]: real websites increase realism, but bot-protection filtering, no Google Search, popular-site selection, and limited agent configurations restrict generalization.
- Statistical conclusion validity [D; MEDIUM]: descriptive percentages are informative, but absence of significance testing, agent-repeat distributions, and bin counts limits fine ranking and trajectory-length conclusions. Judge-repeat standard deviations do not quantify all uncertainty.
- Reproducibility [D; MEDIUM]: model identifiers, thresholds, prompts, and training hyperparameters are supplied, but some agent settings, dates, training counts, and artifact contents remain unverified. Operator's non-API interface complicates reproducible collection.
- Generalizability [A/D]: transfer across five benchmarks supplies useful positive evidence, but varying precision/recall and prompt/model changes show the result is not uniform.
- Security validity [D; HIGH for scope]: no attacker or standalone-model baseline is tested. This paper cannot answer the requested comparative vulnerability question as a causal or quantitative security conclusion.

## 18. Future work and open questions

### A. Explicit author-proposed future work

[A] Maintain the benchmark by replacing outdated tasks with similarly difficult ones. Explore dynamic adjustment of key points as agents learn more about the website. Use evaluator feedback for rejection sampling fine-tuning, reinforcement learning, and reflection; the paper identifies these as prospective uses, not completed training experiments. Develop or use lightweight screenshot identification to lower evaluation cost; Appendix E reports the concrete 7B implementation alongside the forward-looking discussion.

### B. Additional questions remaining from the evidence

[D] How do results change under matched budgets and interfaces? How stable are agent rankings across repeated attempts and website changes? Does training on overlapping tasks influence screenshot-model transfer? Which success definitions best match users' judgments when exact filters are unavailable? Can improved requirement extraction preserve recall without accepting unsupported claims?

[D] For security, a future study would need explicit attacker control, malicious-input conditions, outcomes such as unauthorized behavior, and matched standalone-LLM baselines. It would need to separate ordinary task failure from adversarially induced deviation. This is a proposal for missing evidence, not a reported result or an externally grounded claim.

## 19. Terminology and notation glossary

| Term | Meaning within this analysis |
|---|---|
| LLM | Large language model; language-based reasoning/communication component |
| MLLM | Multimodal large language model; model that can use image evidence |
| Web agent | System that uses model decisions to interact with websites |
| Online-Mind2Web | Proposed 300-task live-web benchmark |
| WebJudge | Three-stage automatic trajectory evaluator |
| WebJudge-7B | Qwen2.5-VL-7B-based screenshot selector combined with LLM stages |
| Trajectory | Ordered actions and screenshots from one task attempt |
| Reference length | Human annotator's step count used for difficulty and efficiency |
| Key point | Explicit requirement extracted from the task |
| Grounding | Connecting intended action to the correct interface target |
| CoT | Chain-of-thought; reasoning-based outcome mode |
| SR | Success rate, percentage of tasks judged successful |
| AR | Agreement rate, percentage of judge/human binary decisions matching |
| Precision/recall/F1 | Complementary classification measures reported for transfer |
| API | Application programming interface; remote model calls counted for cost |
| GPU | Graphics processing unit; hardware used for fine-tuning |
| A11y tree | Accessibility-tree representation used by an external comparator |
| RFT | Rejection Sampling Fine-Tuning in §4.4; inconsistent expansion in Appendix B.5 |
| RL | Reinforcement learning; prospective downstream use |
| WA/VWA/AB/Work/Wk++ | WebArena/VisualWebArena/AssistantBench/WorkArena/WorkArena++ |
| T, A, I, O | Task, action sequence, screenshots, outcome |
| K, k_j | Requirement list and an individual requirement |
| δ or θ | Screenshot relevance threshold, set to 3 |
| S_i, Ŝ_i | Agent steps and human reference steps for task i |
| T_succ, E | Successful-task set and mean normalized step ratio |
| bfloat16 | Training precision named by authors; no further definition supplied |
| OOTB, CAPTCHA, COLM | Acronyms appearing in the paper without supplied expansions |

The twelve domains are Shopping & E-Commerce; Food & Recipes; Housing & Real Estate; Finance & Investment; Health & Medical; Travel & Transportation; Entertainment & Media; Technology; Education; Government & Services; Jobs & Careers; and Other.

## 20. Key numerical results

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| New benchmark size | 300 | tasks | Online-Mind2Web | Author-reported | p. 4 §2.2 |
| Website coverage | 136 | websites | Same benchmark | Author-reported | p. 4 |
| Original tasks checked | 650 | tasks | Viability assessment | Author-reported | p. 4 |
| Invalid/outdated references | 47 | % | Of sampled original tasks | Author-reported | p. 4 |
| Source counts | 167/24/34/75 | tasks | Selected/rewritten/live/new | Author-reported | p. 4 |
| Difficulty counts | 83/143/74 | tasks | Easy/medium/hard | Author-reported | p. 4 |
| WebVoyager website coverage | 15 | websites | Authors' benchmark critique | Author-reported | p. 3 |
| Search-agent success | 51 versus 22 | % | Separate 100-task samples | Author-reported | pp. 3–4 |
| Human agent success | 30.7/28.0/30.0/29.0/56.3/61.3 | % | SeeAct/Agent-E/Browser/Claude 3.5/3.7/Operator | Author-reported | p. 6 T2 |
| Operator minus Claude 3.7 | 5.0 | percentage points | 61.3 − 56.3 | Analyst-derived | p. 6 T2 |
| Average judge agreement | 83.6/85.7/87.0 | % | GPT-4o/o4-mini/7B | Author-reported | p. 6 T2 |
| Average success-rate gaps | 7.8/3.8/3.9 | percentage points | Same judge variants | Author-reported values; clarified units | p. 6 T2 |
| Difficulty mean declines | 31.6/15.4 | percentage points | Easy→medium→hard | Analyst-derived, matching reported magnitudes | p. 7 F4 |
| AgentRewardBench sample | 1,302 | trajectories | Five benchmarks | Author-reported | p. 8 |
| Transfer precision | 73.7/82.0/75.7 | % | GPT-4o/o4-mini/7B | Author-reported | p. 8 T4 |
| Transfer recall | 71.2/47.8/58.0 | % | Same variants | Author-reported | p. 20 B5 |
| Transfer average gaps | 5.9/10.5/6.0 | percentage points | Same variants, Table 5 conditions | Author-reported values; clarified units | p. 9 T5 |
| Threshold agreement | 79.3/81.8/77.0 | % | Operator; θ = 2/3/4 | Author-reported | p. 19 B4 |
| Judge repeated runs | 3 | runs | GPT-4o pipeline | Author-reported | p. 7 |
| Average/maximum repeat SD | 1.1/1.8 | percentage points | Judge-estimated success rates | Author-reported | pp. 7, 19 |
| Open-source step cap | 25 | steps | SeeAct, Browser Use, Agent-E | Author-reported | p. 26 |
| Claude 3.7 cap | 50 | steps | Thinking disabled | Author-reported | p. 26 |
| Operator normalized steps | 2.6 | ratio | Successful-task reference normalization | Visually readable and author-reported | p. 9 F6 |
| Challenging Operator task time | up to 44 | minutes | Selected challenging tasks | Author-reported | p. 9 |
| Filter/sorting share | 57.7 | % of categorized errors | Operator | Visually readable | p. 9 F7 |
| Lightweight API calls | 2 | calls/trajectory | Local screenshot processing plus two LLM stages | Author-reported | pp. 7, 26 |
| Fine-tuning hardware | 4 × 80 | GPUs × GB/GPU | H100 | Author-reported | p. 26 |
| Training configuration | 256; 4096; 5; 5e-6; 10 | batch; tokens; epochs; learning rate; % warmup | 7B model | Author-reported | p. 26 |

No approximate visual estimates are needed for these key results. Unlabeled chart coordinates are discussed qualitatively and excluded from this numerical reference table.

## 21. Claim–evidence map

| Claim | Evidence | Object/experiment | Source | Qualification/evidence strength |
|---|---|---|---|---|
| Live-web competence is lower than some headline results suggest | Manual success 28.0–61.3%; rounded paired benchmark bars | T2/F1/X4 | pp. 1, 6 | HIGH for reported rates; MEDIUM for generalization; conditions differ |
| WebVoyager permits many shortcut solutions | Search agent solves 51% of sampled tasks | F2/X1 | p. 3 | HIGH within 100-task sample |
| New tasks are harder for the search agent | 22% versus 51% | F2/X2 | pp. 3–4 | HIGH for samples; distributions differ |
| Relevant intermediate evidence improves judge agreement | WebJudge outperforms listed LLM judge averages | T3/F5/X6–X7 | pp. 7–8 | HIGH descriptive support; causal mechanism not fully isolated |
| Lightweight selection reduces remote calls | Local screenshot model replaces per-frame API stage | Appendix E/X8 | p. 26 | HIGH for architecture; full latency/cost not quantified |
| Hard tasks remain difficult | Hard-task rates 6.8–43.2% | F4/X5 | p. 7 | HIGH for reported configurations |
| Precision alone overstates transfer quality | o4-mini 82.0 precision, 47.8 recall, 60.4 F1 | B5/X8 | p. 20 | HIGH; metric trade-off directly reported |
| Constraint application is a major failure source | 57.7% filter/sorting share and numeric-range cases | F7/F.4–F.5/X14 | pp. 9, 28–29 | HIGH for observed errors; category denominator unspecified |
| Final descriptions can misrepresent success | Car-location and job-recency examples | F.7–F.8/X14 | p. 30 | HIGH for selected examples; frequency not quantified |
| Paper informs security mechanism hypotheses | Interaction errors and verification failures | §§3, 5 and Appendix F | pp. 5, 9–10, 30 | MEDIUM analyst inference; no attacks tested |
| Paper does not establish greater vulnerability than standalone LLMs | Experimental groups are web agents/evaluators | §4.1/Appendix E | pp. 6, 26 | HIGH scope observation; comparative vulnerability UNKNOWN |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an AI that can use a website for you. Asking it to find a car from particular years is not finished just because it says, 'I found the right cars.' It must actually set the right years, show the right results, and avoid quietly missing a requirement.

This paper argues that some previous tests made these agents look better than they were. Many tasks could be answered by a simple search, and some automatic graders trusted weak evidence. The researchers built a more varied test on real websites. Four agents completed about three tasks out of ten, and the strongest completed about six out of ten under the study's conditions.

Their new grader checks important requirements and keeps screenshots that show what happened. It avoids relying on the agent's final boast. That improves agreement with people, but the grader still makes mistakes. A strict grader can also reject real successes, which is why the paper reports both precision and recall.

For your security question, this shows places where an agent can go wrong while turning words into website actions. It does not show an attacker causing those failures, and it does not compare attacks on agents with attacks on ordinary chat models. The safe conclusion is that the paper gives useful reliability evidence for planning a security analysis, while leaving the actual vulnerability comparison unanswered.

## Completeness Audit

The denominator is the supplied inventory: main text and all appendix text, 18 substantive numbered figures including the diagram, 11 tables, two equations, 14 experiment/analysis groups, three principal contributions, and the explicit limitations identified above. 'Fully represented' means its substantive role and accessible evidence are explained; it does not mean every original sentence or table cell is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 title/abstract | Yes, text + visual | Yes | Fully represented | Authorship, venue, scope and claims |
| S1 Introduction | Yes, text + visual | Yes | Fully represented | Three objectives/contributions and evaluation gap |
| S2.1 benchmark rationale | Yes, text + visual | Yes | Fully represented | Prior benchmark categories and shortcut critique |
| S2.2 dataset construction | Yes, text + visual | Yes | Fully represented | Filtering, counts, difficulty and maintenance |
| S3 WebJudge | Yes, text + visual | Yes | Fully represented | Stages, inputs, bias rationale and cost |
| S4.1 setup | Yes, text + visual | Yes | Fully represented | Agents, website constraint, annotators |
| S4.2 main results | Yes, text + visual | Yes | Fully represented | Success, judge gaps, difficulty and repeats |
| S4.3 evaluator comparison | Yes, text + visual | Yes | Fully represented | Missing cells, disagreement mechanisms |
| S4.4 generalization | Yes, text + visual | Yes | Fully represented | Transfer setting and metric trade-offs |
| S5.1 efficiency | Yes, text + visual | Yes | Fully represented | Equation and success-conditioned caveat |
| S5.2 errors | Yes, text + visual | Yes | Fully represented | Taxonomy, shares and stated limitations |
| S6 conclusions | Yes, text + visual | Yes | Represented in compressed form | Repeated claims connected to earlier evidence |
| S7 acknowledgments | Yes, text + visual | Yes | Represented in compressed form | Funding/resources noted; full legal wording omitted |
| REF references | Yes, text; p. 10 visual | Yes | Represented in compressed form | Categories/provenance retained; no citation validation |
| TOC appendix contents | Yes, text-only | Yes | Fully represented | Used to establish appendix denominator |
| A.A1 web agents/benchmarks | Yes, text-only | Yes | Represented in compressed form | Prior-work categories integrated in §§3–4 |
| A.A2 automatic evaluation | Yes, text-only | Yes | Fully represented | Methods, limitations and input distinctions |
| A.B1 granularity | Yes, text-only | Yes | Fully represented | B1/B2 rates, tokens, rationale and sample uncertainty |
| A.B2 search constraint | Yes, text-only; B3 visual | Yes | Fully represented | Reasons, natural-search caveat, inconsistency |
| A.B3 threshold | Yes, text + partial visual | Yes | Fully represented | Threshold trade-off and values |
| A.B4 robustness | Yes, text + visual | Yes | Fully represented | Three runs, SD and figure-table mismatch |
| A.B5 transfer details | Yes, text-only | Yes | Fully represented | Precision/recall/F1 table retained |
| A.C1 website selection | Yes, text-only | Yes | Fully represented | Popularity, niche and regional sites |
| A.C2 distributions | Yes, text + visual | Yes | Represented in compressed form | Small histogram/domain values uncertain |
| A.D1 specific prompts | Yes, text-only | Yes | Fully represented | Operative criteria and exceptions; prompt wording compressed |
| A.D2 general prompts | Yes, text-only | Yes | Fully represented | Differences and non-progress criteria |
| A.E implementation | Yes, text-only | Yes | Fully represented | Versions, limits, interfaces, training and held-out groups |
| A.F1.1 structured search | Yes, text + visual | Yes | Fully represented | F.1 example |
| A.F1.2 tool navigation | Yes, text + visual | Yes | Fully represented | F.2 example |
| A.F1.3 self-correction | Yes, text + visual | Yes | Fully represented | F.3 action correction |
| A.F1.4 range failures | Yes, text + visual | Yes | Fully represented | F.4/F.5; exact slider endpoints unreadable |
| A.F2 other agents | Yes, text + visual | Yes | Fully represented | Three panels and mistaken cross-reference |
| A.F3 hallucinations | Yes, text + visual | Yes | Fully represented | Two unsupported constraint claims |
| A.G task examples | Yes, text-only | Yes | Represented in compressed form | All 20 inspected; domains/procedures summarized |
| A.H evaluator example | Yes, text-only | Yes | Fully represented | Scores, full-list exception and ellipses |
| Explicit research questions/hypotheses | Assessed | Yes | Fully represented | None formal; analyst questions labeled |
| X1–X3 shortcut/viability studies | Yes | Yes | Fully represented | Samples and qualification preserved |
| X4–X8 performance/judges/transfer | Yes | Yes | Fully represented | Distinct conditions and metrics maintained |
| X9–X12 ablations/repeatability | Yes | Yes | Fully represented | Sample uncertainties and conflicts retained |
| X13–X14 efficiency/errors | Yes | Yes | Fully represented | Conditional metric and selected-case limits |
| F1 | Yes, visual + text | Yes | Fully represented | Rounded cross-benchmark comparison |
| F2 | Yes, visual + text | Yes | Fully represented | Site labels cross-checked with extraction |
| F3 diagram | Yes, visual + text | Yes | Fully represented | Flow explained in §§10 and 12 |
| F4 | Yes, visual + text | Yes | Fully represented | All difficulty values retained |
| F5 | Yes, visual + text | Yes | Represented in compressed form | Exact unlabeled points not invented |
| F6 | Yes, visual + text | Yes | Represented in compressed form | Labeled ratios retained; exact bar means unavailable |
| F7 | Yes, visual + text | Yes | Fully represented | All error shares |
| F.B1 | Yes, visual + text | Yes | Fully represented | Error bars and contradictory mappings |
| F.C1, both panels | Yes, visual + text | Yes | Represented in compressed form | Exact bin counts unreadable |
| F.C2 | Yes, visual + text | Yes | Represented in compressed form | Website denominator and small-label uncertainty |
| F.F1–F.F3 | Yes, visual + text | Yes | Fully represented | Three distinct strategies |
| F.F4–F.F5 | Yes, visual + text | Yes | Fully represented | Range failures; small time values uncertain |
| F.F6, all three panels | Yes, visual + text | Yes | Represented in compressed form | Query wording not confidently transcribed |
| F.F7–F.F8 | Yes, visual + text | Yes | Fully represented | Response/evidence mismatch |
| T1–T4 | Yes, visual + text | Yes | Fully represented | All substantive metric/input comparisons |
| T5 | Yes, visual + text | Yes | Represented in compressed form | Human values, gaps and illustrative cells retained |
| T.B1–T.B2 | Yes, text-only | Yes | Fully represented | No claim of visual inspection |
| T.B3–T.B4 | Yes, visual + text | Yes | Fully represented | Both ablations |
| T.B5 | Yes, text-only | Yes | Fully represented | Detailed triples retained |
| T.G1 | Yes, text-only | Yes | Represented in compressed form | Twenty examples grouped |
| E1–E2 | Yes, visual + text | Yes | Fully represented | Symbols, function and metric limitations |
| Algorithms/pseudocode | Assessed | Yes | Fully represented | None numbered; procedures/prompts analyzed |
| Contributions C1–C3 | Yes | Yes | Fully represented | Benchmark, evaluator, comparative analysis |
| Author-stated limitations | Yes | Yes | Fully represented | Cost, key-point errors, conservatism, randomness, drift, agent failures |
| Supplied supplementary files | None | N/A | Missing from supplied material | No separate files supplied or reviewed |
| Linked repository/data/software | No | Boundary disclosed | Inaccessible under closed-document scope | References are not artifact inspection |
| Standalone-LLM attack comparison | No such experiment | Absence represented | Missing from supplied material | Requested security inference remains indirect |

### Missing or inaccessible material

No supplied text page is missing. Unprovided materials include the linked repository, raw benchmark records, complete collected trajectories, annotation records, model training examples, execution logs, and source code. Pages not among the 16 images have text-only coverage. Appendix H deliberately omits intermediate screenshots with ellipses. No separate supplementary artifact was supplied, and no absent supplement is claimed to have been reviewed.

### Uncertain interpretations

Exact Figure 5 points and sample bins; Figure 6 bar means; Figure C.1 bin counts; all small Figure C.2 labels; some browser screenshot text and flight-slider settings are not confidently recoverable. Browser Use's 26% versus 30.0%, Figure B.1 agent/value assignments, and the granularity study's 83.7% versus 83.6% remain unresolved. Task-level separation for screenshot-model training is unspecified. Security attack vulnerability and its comparison to standalone LLMs are UNKNOWN.

### Deliberately compressed material

Bibliographic entries, recurring headers, author contact details, acknowledgments, repeated motivation/conclusion prose, near-duplicate prompt wording, the full set of Table 5 individual cells, and repeated task descriptions were compressed. Distinct prompt exceptions, model settings, key numerical findings, all visual objects, and all experimental groups were retained. The selected screenshot examples are explained without transcribing every tiny interface label.

### Potential omissions

No known inventoried substantive component is left wholly unrepresented. Representation is limited by the explicitly listed unreadable details, unresolved inconsistencies, and absent external artifacts. This is a comprehensive account of supplied evidence with disclosed compression, not a claim that the entire research package was independently verified or that every original fact survives verbatim.
