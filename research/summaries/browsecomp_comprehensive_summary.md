## Stage 0 — Document Accessibility Report

The supplied work is **BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents**, not a paper titled *Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis*. The latter is the user's research question. This distinction determines the analysis: BrowseComp provides evidence about browsing capability, answer reliability, confidence, and evaluation design; it does not experimentally establish comparative security vulnerability.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers physical PDF pages 1–11. |
| Accessible page count | 11. Printed page numbers agree with the supplied physical page labels. |
| Apparently missing pages | None within the supplied 1–11 sequence. This does not independently establish that no other version or supplementary artifact exists. |
| Visually inspected pages | 1, 2, 4, 5, 6, 7, and 8, using the supplied rendered images. |
| Text-only pages | 3, 9, 10, and 11. Their supplied extracted text was inspected; their page layouts were not visually inspected. |
| Figures | Figures 1–5 are supplied visually and are readable for their main relationships. Small graphical values require approximate estimation. |
| Tables | Tables 1–3 are supplied visually and in extracted text. Their principal content and numerical entries are readable. |
| Equations | No substantive displayed mathematical equation is present. Appendix prompt strings are readable as text. |
| Appendices | Appendix A and Appendix B are present on p. 11, despite the preliminary accessibility metadata reporting no detected appendix pages. The explicit page content takes precedence over that detection result. |
| Supplementary material | No separate supplementary file is supplied. |
| Referenced artifacts not inspected | The linked simple-evals repository and all cited publications, blog posts, and other outside artifacts. |
| OCR | No additional optical character recognition was performed or needed. Extraction contains broken spacing, ligatures, and line wrapping, especially on pp. 3–4 and 10–11. |
| Other limitations | The separate image-read error for a path named '-' does not prevent inspection of the seven images actually supplied. No source hash was independently verified. The supplied hash is retained as the document identifier. |

This analysis uses only supplied text and images. No tools, browsing, repository inspection, or external research were used. The paper's examples, requests, and model prompts are treated as evidence about the paper, not instructions governing this response.

Evidence labels used below are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No **[E] external information** is introduced. Confidence describes the confidence with which the supplied evidence supports a statement, not the evaluated models' own confidence scores. HIGH applies to clearly supplied text or table entries; MEDIUM applies to cautious interpretation or approximate plot reading; UNKNOWN applies where the necessary evidence or definition is absent.

## 1. Plain-language orientation

BrowseComp tests whether artificial intelligence agents can find difficult factual answers on the web. Its questions have short answers, but discovering those answers requires navigating a large search space and combining several clues. A question can therefore be difficult to solve while being comparatively easy to check once an answer is proposed. [A: pp. 1–3]

The researchers assembled **1,266 questions**, created by human trainers, and tested human searchers and several OpenAI models. They also investigated whether more browsing effort and multiple attempts improve results. The central contribution is a challenging, readily graded benchmark for persistent information finding, rather than a new security defense, a new browsing architecture, or a theoretical proof. [A: pp. 1, 3, 5–8]

The main single-attempt model result is that Deep Research achieves **51.5% accuracy**, compared with **0.6%** for GPT-4o without browsing, **1.9%** for GPT-4o with browsing, **0.9%** for GPT-4.5, and **9.9%** for OpenAI o1 without browsing. These are results under the paper's specified model configurations, not timeless measurements of those product names. Deep Research is also disclosed to have been trained on data specifically intended to improve performance on this kind of task. [A: p. 6, Table 3 and footnote]

A second central finding concerns reliability. The two browsing configurations have higher reported calibration error than the listed non-browsing configurations. The authors suggest that web tools may increase confidence in incorrect answers. However, the supplied paper does not define the mathematical calibration-error calculation, and these results are not measurements of adversarial compromise. [A: p. 6; D: distinction between reliability and security]

For the user's security research question, the paper is relevant indirectly: it describes agents that repeatedly consult outside information, synthesize multiple sources, and express confidence in their findings. It does not test malicious webpages, prompt injection, unauthorized actions, secret disclosure, or attacker success. It therefore cannot establish why web agents are more vulnerable than standalone large language models, or even establish that they are more vulnerable under a defined attack. [D: relevance inference grounded in pp. 6–9]

## 2. Document roadmap

| Inventory ID | Original object | Location | Function |
|---|---|---|---|
| META | Title, authors, affiliation, preprint identifier | p. 1 | Identifies the work and its provenance. |
| ABS | Abstract | p. 1 | States the dataset size, difficult-search objective, and limited scope. |
| S1 | §1 Introduction | p. 2 | Motivates browsing evaluation and explains benchmark design goals. |
| S2 | §2 Data collection and verification | pp. 3–4 | Describes human construction, verification criteria, diversity, grading, and measured skills. |
| SS2.1 | §2.1 BrowseComp criteria | p. 3 | Explains difficulty checks, inverted questions, and uncertainty about unique answers. |
| SS2.2 | §2.2 Dataset diversity | p. 4 | Explains trainer topic selection and topic distribution. |
| SS2.3 | §2.3 Grading | p. 4 | Describes semantic answer comparison with an AI grader. |
| SS2.4 | §2.4 What BrowseComp exercises | p. 4 | Identifies factuality reasoning, persistence, and creative search. |
| S3 | §3 Human performance on BrowseComp | p. 5 | Measures human search difficulty and time. |
| S4 | §4 Evaluation of models | pp. 6–8 | Collects model comparisons and further analyses. |
| SS4.1 | §4.1 Performance of OpenAI models | p. 6 | Reports accuracy for five configurations. |
| SS4.2 | §4.2 Calibration Analysis | p. 6 | Reports confidence-related reliability measurements. |
| SS4.3 | §4.3 Test-time compute scaling | p. 7, referring to p. 1 | Relates browsing effort to accuracy. |
| SS4.4 | §4.4 Aggregation strategies leveraging additional compute | p. 7 | Compares answer selection across repeated attempts. |
| SS4.5 | §4.5 Distribution of pass rates | p. 8 | Examines task-level success and follow-up dataset review. |
| S5 | §5 Related work and discussion | pp. 8–9 | Positions the benchmark and proposes broader evaluation directions. |
| REF | References | pp. 9–10 | Lists cited work, without supplying those works' contents. |
| A | Appendix A: Additional instruction for model prediction | p. 11 | Specifies explanation, exact answer, and confidence output fields. |
| B | Appendix B: Grading prompt | p. 11 | Specifies answer extraction, semantic matching, and confidence extraction. |

The inventory also contains **five figures**, **three tables**, **two substantive footnotes**, and **eight distinct analytical activities** discussed in Section 8 below. No formal research-question list, explicit hypothesis list, theorem, pseudocode algorithm, or substantive mathematical equation is supplied. The absence of those objects is recorded rather than filled with invented equivalents.

The title-page authors are Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, and Amelia Glaese. The affiliation is OpenAI. Jason Wei and Zhiqing Sun are marked as equal contributors. The supplied identification is **arXiv:2504.12516v1 [cs.CL], 16 April 2025**. No journal or conference publication venue for this paper is stated. [A/B: p. 1]

## 3. Background and context

A **benchmark** is the collection of test questions and associated scoring procedure used here to compare systems. BrowseComp means **Browsing Competition**. The authors use programming competitions as an analogy: a constrained task can test an important capability without representing every task users need. The analogy is explicitly qualified; success on BrowseComp is not guaranteed to generalize to all browsing tasks. [A: pp. 2, 4]

A **browsing agent** is described in this work as a model able to use web access in searching for information. Deep Research is characterized as explicitly trained for persistent browsing, including searching, synthesizing sources, and adapting strategy. The supplied paper does not provide a technical architecture defining every component of such an agent. [A: p. 6]

An **inverted question** begins with a known person, event, or artifact and turns its characteristics into clues. Instead of asking for a familiar fact directly, the question asks the solver to identify an entity satisfying those clues. This creates an asymmetry: finding the entity may require extensive search, whereas checking a proposed entity against the clues can require only a few searches. [A: p. 3]

**Semantic equivalence** means that the predicted answer and reference answer convey the same answer even if their strings are not identical. The grader is instructed to focus on meaningful differences rather than solve the question again. This distinction matters because the benchmark's scoring procedure compares against a reference answer, not against a comprehensive independent reconstruction of the web evidence. [A: pp. 4, 11]

**Accuracy** is reported as the percentage of benchmark questions answered correctly. **Pass rate** in the repeated-trial analysis is the fraction of attempts on an individual question that succeed. These are different levels of aggregation: a dataset-level accuracy and a question-level distribution of success frequencies should not be treated as interchangeable. [A/D: pp. 6–8]

**Calibration** concerns whether expressed confidence corresponds to actual correctness. The authors distinguish poor absolute calibration from a useful relative signal: a model can assign unreliable probabilities overall while still assigning comparatively higher confidence to better answers among its own attempts. [A: pp. 6–7]

**Test-time compute** is computation expended while solving a question, rather than while training a model. The paper considers both increased effort in one attempt and multiple sampled attempts. It does not provide a common numerical conversion to seconds, tokens, money, or hardware operations. [A: p. 7; D: reporting limitation]

The paper mentions AIME, EMNLP, and several named systems or benchmarks without expanding every acronym in the supplied text. AIME and EMNLP are retained as source labels rather than expanded from outside knowledge. GPT and the 'o1' designation are likewise model names here; the supplied material does not define their naming conventions.

## 4. Research problem and gap

**Existing problem.** Finding obscure web information can demand persistent attention, extensive browsing, and the ability to reconsider a search strategy. The introduction contrasts this with human limitations in memory, fatigue, distraction, and parallel attention. Its suggestion that a sufficiently capable system could retrieve any well-specified open-web fact is a motivating aspiration, not an experimentally established universal result. [A: p. 2]

**Shortcomings of prior approaches according to the authors.** The authors say many previous information-retrieval benchmarks emphasize information that humans can find relatively easily, often within ten minutes, and have become saturated by recent language models. The supplied paper cites examples but does not reproduce a systematic cross-benchmark comparison substantiating every part of that literature claim. [A: pp. 2, 8]

**Research gap.** The intended gap is a benchmark of difficult, deeply entangled information finding that remains easy to use and grade. The difficult part should lie in discovering an answer, not in interpreting a long, ambiguous output or applying an elaborate grading rubric. [A: pp. 1–3]

**Motivation.** The authors identify reliability, difficulty, and ease of use as factors in benchmark adoption. Short, self-contained questions and reference answers are intended to reduce evaluation friction while retaining demanding search tasks. [A: p. 2]

**Scope.** BrowseComp targets finding a single piece of information through persistent browsing. It intentionally excludes important aspects of ordinary user queries, including producing long answers and resolving ambiguity. It also does not evaluate security against an adversarial actor. [A: pp. 1, 4, 9; D: security-scope observation]

## 5. Research questions, objectives, and hypotheses

No formal numbered research questions or explicit statistical hypotheses appear in the supplied work. The following are **author-stated objectives and analytical purposes**, expressed without pretending that the authors supplied formal hypothesis tests:

1. Create a challenging but easily evaluated benchmark for web-browsing agents. [pp. 1–3]
2. Measure the ability to persistently and creatively find difficult information. [pp. 1, 4, 9]
3. Assess task difficulty through human search performance. [p. 5]
4. Compare selected OpenAI model configurations on accuracy. [p. 6]
5. Assess whether models express confidence appropriately. [p. 6]
6. Examine performance as browsing effort increases. [p. 7, Figure 1 on p. 1]
7. Examine whether repeated attempts and answer aggregation improve accuracy. [p. 7]
8. Characterize variation in difficulty across questions and investigate persistent failures. [p. 8]

The statement that additional test-time compute should improve BrowseComp performance is an explicit expectation in §4.3, but the paper does not frame it as a formal null-versus-alternative hypothesis or report a significance test. [A: p. 7]

The user's question about comparative security vulnerability is outside these objectives. The closest connection is the analysis of browsing, external information interpretation, and overconfidence. That connection remains **analyst inference**, not a newly discovered author objective.

## 6. Assumptions / Threat Model

There is **no security threat model** in the supplied paper. No attacker, attack budget, malicious-content placement, access privilege, protected asset, or security success condition is specified. There is also no experiment comparing attacked browsing agents with attacked standalone language models. [D: document-wide negative finding]

The benchmark instead relies on several methodological premises. Questions should have short, fact-seeking, time-stable answers supported by evidence. Trainers should be sufficiently familiar with their subject to have confidence in the reference answer and in the absence of alternatives. The authors explicitly acknowledge that this confidence does not guarantee uniqueness. [A: p. 3]

The grading process relies on a reference answer and an AI model's comparison against it. Appendix B treats the provided correct answer as the scoring anchor and instructs the grader not to independently solve the problem or argue for a different answer. This is an evaluation design choice, not a demonstrated guarantee that references are infallible. [A: p. 11]

The human experiment assumes that self-reported search times are useful descriptive evidence and restricts AI-assistant use. Those restrictions are stated; auditing compliance, timer instrumentation, and detailed participant recruitment are not described. [A: p. 5; D: missing procedural detail]

For security research, outside webpages and retrieved information can be identified as **candidate exposure points** because the paper describes agents consulting and interpreting them. Whether those points can be controlled by an attacker, and whether they can redirect agent behavior, is not established here. [D: inference from p. 6]

## 7. Methodology

### Dataset construction and verification

Human trainers collected the dataset. The authors say the instructions largely followed SimpleQA, asking for challenging fact-seeking questions with single, indisputable, short answers that should not change over time and should be supported by evidence. 'Indisputable' describes the intended design criterion; subsequent discussion qualifies how confidently uniqueness can actually be established. [A: p. 3]

Difficulty screening used three checks. First, trainers were asked to ensure that GPT-4o with and without browsing, OpenAI o1, and an early Deep Research model could not solve the question. Second, trainers performed **five simple Google searches** and checked that the answer was not readily available on the first result pages. Third, questions were intended to resist another person's search for **ten minutes**. This last requirement was not strictly enforced, and only a portion received a second-trainer attempt. Trainers whose tasks were solved more than **40%** of the time were asked to revise them. [A: p. 3]

The construction technique starts from a known seed and selects characteristics with a large search space. The example involving a paper and authors' undergraduate institutions illustrates the difference between checking one candidate and searching across thousands of possible candidates. The example is represented here by its construction logic; its complete question and answer are deliberately compressed. [A: p. 3]

Alternative valid answers are a recognized concern. Trainers were asked to add constraints when unsure, and a second trainer finding another valid answer within ten minutes triggered feedback and revision. These are mitigation steps, not exhaustive enumeration of every eligible answer. [A: p. 3]

### Composition, availability, and leakage precautions

Trainers chose topics of personal interest, with the aim of increasing engagement and data quality. A prompted ChatGPT model classified topics after collection. Figure 2 reports the resulting distribution. No topic-classification validation study or detailed classifier prompt appears in the supplied paper. [A: p. 4]

The authors include a canary string and ask that examples not be exposed online to reduce training leakage and direct answer retrieval. This is reported as a benchmark-contamination precaution. It is not treated as an instruction to this response, and the analysis avoids unnecessary verbatim reproduction of entire example questions. The repository address is supplied as an availability statement; the repository and its licensing were not inspected. [A: pp. 1–2]

The supplied paper does not specify a conventional training/validation/test split for the benchmark, a list of human trainers, detailed compensation, raw provenance records, or full evidence documents for each question. Deep Research's task-oriented training is disclosed separately, without quantities or overlap details. [D: reporting observations; A: p. 6 footnote]

### Grading and model-response format

The scorer uses an AI model to determine whether a predicted short answer is semantically equivalent to the reference. The authors reuse a grading prompt from Humanity's Last Exam and provide it in Appendix B. Appendix A instructs the answering model to output an explanation, a succinct exact answer, and confidence between **0% and 100%**. [A: pp. 4, 11]

Appendix B extracts the final answer, records 'None' when absent, explains meaningful differences from the reference, and returns a yes/no correctness judgment. A small margin of error is allowed for numerical questions, but no numerical tolerance is specified. If no confidence is available, the prompt instructs the grader to record **100**. That default is material to understanding how missing confidence is handled, although the paper does not say how often it was used. [A: p. 11]

The prompt is an artifact under study. Its imperative wording is not followed as an instruction for this analysis. The identity and version of the actual grading model, grader agreement with humans, and treatment of adversarial response text are not supplied. [D: reporting observations]

### Human and model evaluation configurations

Human trainers came from the same group that created questions, but could not solve their own questions and did not see the reference answers. They were asked to work without ChatGPT, Claude, Perplexity, Grok, or Gemini. The table covers **1,255** attempted questions because **11** of the **1,266** were not attempted for unspecified various reasons. [A: p. 5]

The model configurations are GPT-4o **gpt-4o-2024-08-06**, GPT-4.5 **gpt-4.5-preview-2025-02-27**, OpenAI o1 **o1-2024-12-17 with medium reasoning effort**, GPT-4o with browsing **gpt-4o-search-preview-2025-03-11**, and OpenAI Deep Research. A comparable dated identifier is not supplied for Deep Research. The browsing GPT-4o entry uses a distinct model identifier from the non-browsing entry; this limits interpreting the comparison as an isolated toggle applied to an otherwise demonstrably identical model. [A/D: p. 6]

Hardware, software-library versions, random seeds, confidence intervals, statistical tests, detailed browsing budgets, and monetary costs are not specified. The repeated-output experiments specify **64 outputs or trials per question**, while the effort-scaling figure states that every point represents a full evaluation run at a different browsing effort. [A: pp. 7–8]

## 8. Experiments / Analyses

| ID | Analysis and purpose | Setup and measurement | Principal result | Caveat |
|---|---|---|---|---|
| X1 | Dataset difficulty screening | Trainer checks against selected models, five searches, and partial second-trainer attempts | Questions selected to be hard to find but easy to verify | Screening is partly judgment-based; ten-minute criterion not strictly enforced. |
| X2 | Topic composition | Post-hoc prompted ChatGPT classification of 1,266 questions | Ten categories in Figure 2 | This is descriptive composition, not a performance-by-topic experiment. |
| X3 | Human search performance | Same trainer pool, own questions excluded, no AI assistants; 1,255 attempted questions | 367 reported solved; 317 agree with reference | Reported solving and reference agreement are distinct outcomes. |
| X4 | Model accuracy comparison | Five listed configurations on BrowseComp | Deep Research 51.5%; others 0.6–9.9% | Configurations differ in training and model identity as well as browsing. |
| X5 | Confidence calibration | Confidence requested with each response | Calibration error 65–91% across configurations | Metric formula and uncertainty are not supplied. |
| X6 | Browsing-effort scaling | Full evaluation runs at different effort settings | Figure 1 shows increasing accuracy with effort | Numeric effort values and cost units are absent. |
| X7 | Parallel sampling and aggregation | 64 outputs per question with confidence; compare three selection schemes | Best-of-N leads at sampled counts above one | Figure values are graphical; prose improvement units are ambiguous. |
| X8 | Pass-rate distribution and failure follow-up | 64 trials per question; answer-provided evidence retrieval and task review | Deep Research has 16% always-correct and 14% always-failed tasks; 21 tasks removed | Zero-pass counts in the review do not align transparently with the final distribution. |

X3 measures the difficulty of searching under the study's conditions. Humans gave up on **888/1,255**, or **70.8%**, and reported solving **367/1,255**, or **29.2%**. Of the reported solved questions, **317/367**, or **86.4%**, matched the reference. Search times were self-reported; solved questions include tasks taking two or three hours, whereas giving up was allowed only after approximately two hours. [A: p. 5]

X4 indicates that web access alone, as instantiated by the listed GPT-4o browsing configuration, does not yield strong benchmark performance. OpenAI o1 without browsing performs better than both GPT-4o configurations, and Deep Research performs far better. The authors interpret this as evidence for contributions from both reasoning and tools. The experiment does not separately manipulate every component needed to quantify those causal contributions. [A/D: p. 6]

X5 requests confidence and compares reported calibration errors. The authors interpret higher errors for browsing configurations as suggesting possible overconfidence from tools. No confidence histogram, calibration curve, metric definition, or test of the proposed mechanism is supplied. [A/D: p. 6]

X6 concerns more effort within a model attempt. X7 instead concerns trying a question repeatedly and selecting among outputs. Keeping these separate avoids calling all gains one undifferentiated effect of compute. Majority voting chooses the most frequent answer; weighted voting weights votes by confidence; best-of-N selects the one output with the highest confidence. [A: p. 7]

X8 includes two different follow-ups. Providing the ground-truth answer and asking for supporting evidence succeeded in most cases, according to the authors, but no exact success count is reported. Separately, reviewing **118** zero-pass tasks identified **21** with answer-format mismatch, ambiguity, or reasoning-based incorrectness; they were removed from an original **1,287**, leaving **1,266**. The relationship between this 118-task subset and the final 14% zero-pass result is unresolved. [A: p. 8]

## 9. Results

### Model accuracy and confidence-related results

| Model configuration | Accuracy (%) | Calibration Error (%) | Source |
|---|---:|---:|---|
| GPT-4o without browsing | 0.6 | 69 | p. 6, Table 3 |
| GPT-4o with browsing | 1.9 | 82 | p. 6, Table 3 |
| GPT-4.5 without browsing | 0.9 | 68 | p. 6, Table 3 |
| OpenAI o1 without browsing | 9.9 | 65 | p. 6, Table 3 |
| Deep Research | 51.5 | 91 | p. 6, Table 3 |

All table values above are author-reported and visually readable. Deep Research has the highest accuracy and the highest reported calibration error. OpenAI o1 has the lowest reported calibration error. No ties appear in either column. 'Highest accuracy' does not imply 'best calibration.' [A/B]

**Analyst-derived differences:** GPT-4o's listed browsing configuration improves accuracy by **1.9 − 0.6 = 1.3 percentage points**. The relative increase is **(1.9 − 0.6)/0.6 × 100 ≈ 216.7%**, but this large relative figure starts from a very small baseline and leaves absolute accuracy at 1.9%. Deep Research exceeds OpenAI o1 by **51.5 − 9.9 = 41.6 percentage points**. These are arithmetic comparisons of reported configurations, not estimates of the causal effect of browsing alone. [C: p. 6]

### Human outcomes

The reported human solve rate is 29.2%, but only 317 answers agree with the reference. **Analyst-derived:** **317/1,255 × 100 ≈ 25.3%** is the reference-agreement proportion across all attempted questions. Also, **367 − 317 = 50** reported solved answers did not agree. The supplied paper does not establish whether each disagreement reflects human error, a valid alternative, ambiguity, or a reference issue. [C/D: p. 5]

The human and Deep Research values should not be treated as an uncomplicated contest under matched resources. Humans have their own time rules and an attempted subset; model computational budgets and time are not matched or fully reported. [D: pp. 5–7]

### Compute and repeated attempts

Figure 1 supports increasing accuracy as browsing effort increases, but does not provide numeric x-axis effort labels. Figure 4 shows best-of-N reaching approximately **0.78 accuracy** at **64 samples**, weighted voting approximately **0.70**, and majority voting approximately **0.67**. These endpoint values are approximate visual estimates, not exact tabulated results. [B: pp. 1, 7]

The prose says the aggregation methods improve performance by **15% to 25%** over a single attempt. It does not explicitly distinguish percentage points from relative percent. A single-sample value near 0.52 and 64-sample endpoints near 0.67–0.78 correspond approximately to 15–26 percentage points, whereas relative gains would be larger. This is a reporting ambiguity, not a license to silently rewrite the stated result. [A/B/D: p. 7]

### Uneven question difficulty and dataset revision

Deep Research's **16%** always-correct and **14%** always-failed proportions refer to **64 trials per question**, not to definitive proof that tasks are intrinsically solvable or unsolvable. Figure 5 also labels OpenAI o1's zero-pass mass as **79.3%**. Providing the answer often enables evidence retrieval, which supports the authors' distinction between discovering and verifying an answer. [A/B: p. 8]

The dataset-count arithmetic is consistent: **1,287 − 21 = 1,266**. However, **14% of 1,266 ≈ 177** questions is substantially different from the reported **118** zero-pass tasks reviewed. Because 14% is rounded and the conditions linking these figures are unspecified, an exact reconciliation cannot be made. [C/D: p. 8]

## 10. Figure-by-figure interpretation

### Figure 1 — Browsing effort and accuracy

**Location:** p. 1; explained in §4.3 on p. 7. **Purpose:** show an early Deep Research model's performance at different browsing efforts. It is a scatterplot with blue circular markers and no separate conditions in a legend. The x-axis is 'Test-time compute (log-scale)'; the y-axis is 'BrowseComp accuracy (%)', labeled from 0 through 60. Numeric x-axis effort values are not provided. [A/B]

The plotted accuracy rises from roughly **9%** at the low-effort end to approximately **52%** at the high-effort end. These are approximate visual estimates. Points form a smooth upward pattern rather than an apparent plateau over the displayed range. The caption reports smooth scaling, and §4.3 says each point is a full evaluation run. No error bars or confidence intervals are shown. [A/B]

This supports an effort–performance association for the displayed model and settings. It does not identify the amount of compute needed for each gain, give a monetary cost, or demonstrate that indefinitely increasing effort would keep improving accuracy. It also should not be silently equated with every later Deep Research experiment: the caption explicitly says an early version. [D]

### Figure 2 — Topic distribution

**Location:** p. 4, §2.2. **Purpose:** describe the benchmark's topics. This is a pie chart with ten differently colored slices and a legend giving category counts. The percentage labels and counts are readable. There are no axes, uncertainty intervals, or significance indicators. Topics were classified post-hoc by a prompted ChatGPT model. [A/B]

| Topic | Count | Displayed share |
|---|---:|---:|
| TV shows and movies | 205 | 16.2% |
| Other | 197 | 15.6% |
| Science and technology | 173 | 13.7% |
| Art | 127 | 10.0% |
| History | 125 | 9.9% |
| Sports | 123 | 9.7% |
| Music | 116 | 9.2% |
| Video games | 71 | 5.6% |
| Geography | 70 | 5.5% |
| Politics | 59 | 4.7% |

The largest named category is TV shows and movies; the smallest is politics. The counts sum to **1,266**. The rounded percentages sum to **100.1%**, a small rounding excess rather than evidence of an extra question. [C: addition of displayed values]

The chart demonstrates breadth of topics but does not prove representativeness of user requests, equality of difficulty across categories, or reliable topic annotation. 'Other' is a substantial residual category whose contents are not broken down. [D]

### Figure 3 — Human search-time distributions

**Location:** p. 5, §3. **Purpose:** contrast times for solved questions with times before giving up. There are two substantive panels. The left panel uses green bars for problems solved by humans; the right uses orange bars for problems where humans gave up. Both x-axes read 'Time for human to solve (minutes)', with labeled ticks at **0, 60, 120, 180, 240, and 300**. On the right, the title and caption clarify that time concerns giving up despite the repeated x-axis wording. [A/B]

Both y-axes count problems, but their scales differ: the solved panel has labeled ticks through **80**, while the gave-up panel has ticks through **600**. Comparing bar heights across the panels without accounting for these scales would be misleading. Exact bin boundaries and individual counts are not supplied as a table. [B]

The solved-time distribution is spread across a broad range, with its tallest bar around two hours and some solutions extending beyond three hours. The giving-up distribution is strongly concentrated near the two-hour threshold, with a smaller concentration thereafter. These are visual descriptions; exact means, medians, and peaks are not reported. [B]

The caption states that giving up required at least two hours of attempting a problem. Accordingly, the orange concentration reflects an experimental stopping rule as well as question difficulty. No error bars appear, and times are self-reported. [A/D]

### Figure 4 — Repeated attempts and answer selection

**Location:** p. 7, §4.4. **Purpose:** compare aggregation over multiple Deep Research outputs. The x-axis is the number of parallel samples per task, labeled **1, 2, 4, 8, 16, 32, 64** at evenly spaced positions. This gives a doubling progression rather than equal linear increments in sample count. The y-axis is accuracy on a fractional scale, labeled from **0.50 to 0.80**. [B]

The lightest blue line is Best of N, the medium-blue line Weighted Voting, and the darkest blue line Majority Voting. Lines have circular point markers. All coincide around **0.52** at one sample. At two samples, best-of-N and weighted voting are near **0.60**, while majority voting is near **0.53**. At 64, the lines are approximately **0.78**, **0.70**, and **0.67**, respectively. These graphical readings are approximate. [B]

Best-of-N leads at the displayed counts above one; weighted voting is intermediate; majority voting is lowest. Gains become smaller at larger sample counts, particularly for majority and weighted voting. No uncertainty bars are shown. The figure supports confidence-based selection as useful in this experiment, while §4.2 establishes that absolute confidence remains poorly calibrated. [A/B]

The chart does not specify tie-breaking, answer canonicalization before voting, how lower-N subsets were chosen from the 64 generated outputs, or variability across repeated aggregation selections. The unspecified percentage-versus-percentage-point wording in the accompanying text remains unresolved. [D]

### Figure 5 — Distribution of task-level pass rates

**Location:** p. 8, §4.5. **Purpose:** compare how often each model solves the same question over repeated trials. It is a grouped bar chart, with red bars for OpenAI o1 and light-blue bars for Deep Research. The x-axis is pass rate from **0 to 1**. The y-axis is percentage of total tasks, with displayed tick labels from **0% to 20%**. [A/B]

The OpenAI o1 zero-pass bar is annotated **79.3%**, exceeding the plotted y-axis range. The annotation is essential; the clipped bar height alone cannot convey the value. Deep Research has a zero-pass bar around **14%** and a perfect-pass bar around **16%**, consistent with the text. Its remaining mass is distributed across intermediate pass rates. [A/B]

The text specifies **64 trials per question**. A pass rate of one means all 64 sampled trials succeeded; a pass rate of zero means none succeeded in that experiment. Neither observation is an absolute theorem about what a model can ever do. The binning or grouping underlying the bars is not fully specified, so intermediate bar counts cannot be reconstructed exactly. [A/D]

§4.5 refers to 'the figure below' although Figure 5 appears above the subsection in the supplied page. This is a minor positional wording issue. The more substantive unresolved issue is the **118** reviewed zero-pass tasks versus the roughly **14% of 1,266** described for Deep Research. [A/B/D]

## 11. Table-by-table interpretation

### Table 1 — Three example questions and reference answers

**Location:** p. 2. The table has three side-by-side examples rather than numerical result rows. The examples concern a historical soccer match, a fictional television character, and a research publication. Their multiple constraints illustrate the large candidate space and the short final answer format. The reference answers are printed with each example. [A/B]

The full examples are deliberately compressed because their role is to demonstrate question construction; the analysis preserves that role without reproducing all clue strings. The caption also reports the canary-string contamination precaution and the authors' request against online disclosure of examples. Neither is experimental evidence that leakage has been eliminated. [A/D]

### Table 2 — Human campaign outcomes

**Location:** p. 5. The table reports an attempted-question total and three outcome rows. **1,255** questions were attempted. **888/1,255 (70.8%)** were given up; **367/1,255 (29.2%)** were reported solved; and **317/367 (86.4%)** of those solved answers agreed with the reference. Its footnote explains that **11** of the **1,266** examples were not attempted for various reasons. [A/B]

The first two outcome counts add to the attempted total. The agreement row has a different denominator and must not be presented as 86.4% accuracy over the whole benchmark. No confidence intervals, participant counts, participant-level results, or significance tests are provided. The table establishes substantial human difficulty under the specified procedure, with unresolved meaning for the 50 disagreements. [C/D]

### Table 3 — Model accuracy and calibration

**Location:** p. 6. Rows are model configurations; columns are accuracy and calibration error, both expressed as percentages. The exact values are reproduced in Section 9. Deep Research leads accuracy at **51.5%** and has the highest calibration error at **91%**. GPT-4o without browsing has the lowest accuracy at **0.6%**. OpenAI o1 has the lowest calibration error at **65%**. [A/B]

The substantive footnote states that Deep Research was trained on data specifically teaching it to perform well on these tasks. This materially qualifies comparisons: performance reflects a system adapted to this task family. The footnote does not establish that the exact test questions were used in training, and the analysis does not infer such overlap. [A/D]

No uncertainty estimates or statistical significance markers are included. The prose describes Deep Research as significantly outperforming others, but the supplied table does not report a statistical significance test. Here, the evidence supports a large reported numerical separation, not an independently verified significance claim. [A/D]

## 12. Diagram / Architecture Interpretation

No architecture diagram, flowchart, component schematic, or threat-model diagram is supplied. Figures 1–5 are performance or distribution plots. The paper does not expose a browser controller, tool interface, memory system, permission boundary, or execution environment in diagram form.

A **text-grounded procedural reconstruction**, rather than an author-provided architecture, is: human trainers create and screen questions; a model receives a question and output-format instruction; it returns an explanation, exact answer, and confidence; an AI grader extracts the answer and compares it with the reference; correctness is aggregated into benchmark results. In the repeated-output experiment, a selection rule chooses among multiple answers before evaluating the chosen answer. [D: reconstruction from pp. 3–4, 7, 11]

This procedural account helps explain the evaluation but should not be mistaken for a security architecture. The supplied material does not describe how web content is isolated from higher-priority instructions or how agent permissions are enforced. [D]

## 13. Equations and mathematical concepts

There are no numbered mathematical equations, losses, optimization objectives, lemmas, or proofs to audit. The necessary mathematics concerns proportions and derived differences. The expressions below are **analyst explanations of supplied quantities**, not equations printed by the authors.

**Question-level empirical pass rate:** if a question receives 64 trials and k of them are correct, its observed pass rate is **k/64**. Here k is a count from zero through 64. The output is a fraction from zero to one. This identifies what the repeated-trial analysis measures; it does not imply independence of trials or a known underlying success probability. [C/D: p. 8]

**Percentage-point change:** subtract two percentages directly. For the listed GPT-4o configurations, **1.9% − 0.6% = 1.3 percentage points**. **Relative percentage increase:** divide the change by the initial value, giving **1.3/0.6 × 100 ≈ 216.7%**. The operands and interpretation differ, so the two expressions must not be interchanged. [C: p. 6]

**Human reference-agreement proportion:** **317/1,255 × 100 ≈ 25.3%**. This uses all attempted questions as the denominator, whereas the paper's **86.4%** uses only the 367 reported solved questions. [C: p. 5]

**Calibration error:** the supplied work explains the conceptual goal but does not give a formula, binning scheme, confidence normalization procedure, or aggregation rule. It is therefore not possible to reconstruct the reported 65–91% values from the paper alone, nor to identify them confidently with any particular conventional calibration statistic. [D: p. 6]

**Confidence-weighted voting:** the authors say confidence weights each vote but provide no equation. The underlying confidence may be a percentage, yet implementation details such as normalization and grouping equivalent answers are absent. Best-of-N is described operationally as selecting the highest-confidence output, not as a theorem guaranteeing a correct answer. [A/D: p. 7]

## 14. Interpretation and discussion

The work's strongest supported message is that difficult information discovery requires more than nominal web access. In the listed comparison, GPT-4o browsing remains at 1.9% accuracy, whereas a reasoning-oriented non-browsing model reaches 9.9% and a persistent browsing system reaches 51.5%. The authors interpret this as evidence that tool use and reasoning both matter. A cautious analyst reading accepts the pattern while noting that the experiment compares systems with several differing properties. [A/D: p. 6]

A second message is that discovery and verification can have different difficulty. Inverted construction creates this separation; answer-provided follow-up retrieval supports it; and confidence-based selection suggests that the model can sometimes recognize a good candidate more readily than generate one reliably. The follow-up remains qualitative because 'most cases' is not accompanied by a count. [A: pp. 3, 7–8]

The confidence findings distinguish **probability calibration** from **ranking usefulness**. Deep Research has a high reported calibration error, but selecting its highest-confidence output improves results. These observations need not conflict: confidence can order candidates usefully without accurately stating their probabilities. The paper supports that distinction empirically through Table 3 and Figure 4, without specifying a mathematical calibration model. [A/D]

Several consistency checks pass. Topic counts total 1,266; removing 21 tasks from 1,287 yields 1,266; 888 plus 367 equals 1,255; and 1,266 minus 11 equals 1,255. Other checks remain unresolved. The 118-task review count does not transparently align with the final 14% zero-pass result. The 15–25% aggregation gain lacks explicit units. The human narrative contains the phrase 'if they could solve it within 2 hours' when explaining permission to abandon a problem; the caption and surrounding account instead make clear that giving up followed at least two hours of trying. This apparent wording error is disclosed rather than silently quoted as a coherent rule. [A/C/D: pp. 5, 7–8]

For the security research question, **analyst interpretation** is that the work supplies a reliability-oriented motivation for studying web agents: they ingest outside information repeatedly and may remain overconfident when wrong. It supplies no empirical bridge from that motivation to attack success. Its actual browsing/non-browsing comparison concerns correctness and calibration, not comparative vulnerability under attack.

## 15. Contributions and novelty

**Dataset contribution:** a human-created collection of 1,266 short-answer, difficult-search questions with supporting evidence required during construction. [A: pp. 1, 3, 9]

**Benchmark contribution:** an evaluation designed to combine demanding discovery with comparatively straightforward answer checking. The authors position this as filling a gap left by easier retrieval benchmarks. [A: pp. 2–4]

**Methodological contribution:** a documented construction and screening procedure using inverted questions, model checks, simple-search checks, partial human checking, and revision when alternative answers appear. These procedures are described rather than evaluated through controlled ablations of each criterion. [A/D: p. 3]

**Empirical contribution:** model accuracy and calibration results, human search measurements, browsing-effort scaling, repeated-output selection comparisons, and task-level pass-rate analysis. [A: pp. 5–8]

**Evaluation-artifact contribution:** response-format and grading prompts are supplied in appendices, making important aspects of the evaluation explicit. They do not amount to a complete reproducibility package within the provided document. [A/D: p. 11]

No new security mechanism, formal theorem, browser architecture, or attack taxonomy is contributed by the supplied paper. The aspiration to encourage trustworthy and reliable agents in the conclusion is broader than the security evidence actually collected. [A/D: p. 9]

## 16. Limitations

### Authors' stated limitations

1. BrowseComp is an incomplete measure of browsing capability. It omits long-answer generation and ambiguity resolution in realistic user queries. [pp. 1–2, 4]
2. Performance is not guaranteed to generalize to all tasks requiring browsing. [p. 4]
3. Inverted construction cannot guarantee that every valid answer is represented. Exhaustively checking all candidates can be too time-consuming. [p. 3]
4. The ten-minute human difficulty check was not strictly enforced; only a portion of questions received a second-trainer attempt. [p. 3]
5. Human trainers were not competition-level browsers, and more experienced professionals with ample time might solve questions they abandoned. [p. 5]
6. Browsing models, especially Deep Research in the reported comparison, struggle to convey uncertainty accurately. [p. 6]
7. The reference-answer review found tasks with formatting mismatch, ambiguity, or incorrectness and removed them. [p. 8]
8. The benchmark requires textual supporting evidence; other modalities are proposed as a future extension. [p. 9]

The Deep Research training disclosure is also a substantive condition of comparison. It should be preserved alongside the results, even though it is written as a footnote rather than a limitation section. [p. 6]

### Additional evidence-based analyst observations

These observations are not attributed to the authors. The calibration metric lacks a reproducible mathematical definition. The grading model is unnamed. Human time data are self-reported. Hardware, seeds, browsing budgets, costs, confidence intervals, and detailed aggregation implementation are absent. These omissions constrain reproducibility and precision of interpretation. [D]

The human reference-agreement denominator differs from the solved denominator. The evaluated GPT-4o configurations have different identifiers. Dataset filtering uses failures of a particular model as a review trigger. The 118-task review count and 14% final zero-pass rate are not transparently connected. Each issue should be considered when comparing results or treating the dataset as independent of its evaluation systems. [D]

Most importantly for the user's question, no attacks are performed. Ordinary incorrectness and overconfidence are insufficient to quantify adversarial vulnerability. No statement about attack success, prompt-injection prevalence, or permission bypass can be obtained from these results. [D]

## 17. Threats to validity

The following validity categories are **analyst labels**, not a taxonomy used explicitly by the authors.

**Internal validity:** the model comparison does not isolate browsing from model version, training, reasoning ability, and system design. The data show differences among configurations; causal statements about a single feature require more controlled evidence. [D: p. 6]

**Construct validity:** the benchmark measures hard fact discovery with short-answer scoring. It does not operationalize overall helpfulness, long-form source synthesis quality, ambiguity handling, or security. High accuracy therefore answers a narrower question than 'Is this agent trustworthy in every important sense?' [D: pp. 1–4, 9]

**External and ecological validity:** topic selection follows trainer interests, questions are deliberately difficult, and answer inversion differs from many ordinary user requests. Human experts in other occupations, other agent designs, and interactive or multimedia tasks may behave differently. The authors explicitly qualify generalization. [A/D: pp. 3–5, 9]

**Statistical conclusion validity:** descriptive numerical differences are supplied, but confidence intervals and significance tests are not. Trial independence and the variability of aggregation results are unspecified. The analysis therefore avoids claiming tested statistical significance, quantified uncertainty, or exact extrapolation beyond plotted settings. [D]

**Reference and grading validity:** answer uniqueness is not guaranteed, reference defects were found, and the AI grader is instructed to match the reference rather than adjudicate web evidence. The supplied material does not measure grader error or classify human-reference disagreements comprehensively. [A/D: pp. 3–5, 8, 11]

**Reproducibility:** the model identifiers and prompts aid replication, but absent details about Deep Research, budgets, grading implementation, and data provenance prevent a full reproduction from the supplied document alone. The linked repository could contain additional information, but it was not inspected and cannot be credited here. [D]

**Security inference validity:** transferring these reliability results into a claim about attacker-induced vulnerability would change both the outcome and the experimental setting. That transfer is unsupported without a threat model and corresponding attacked-system measurements. [D]

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

The discussion proposes benchmarks involving **images, video, audio, or interactive webpages**, extending beyond the textual supporting evidence required here. The authors invite evaluation of additional AI agents and feedback on the benchmark. They hope that releasing it will encourage more trustworthy and reliable agents. These are stated directions or aspirations, not completed experiments. [A: p. 9]

### B. Additional open questions logically remaining

As **analyst questions**, how should calibration error be defined and reproduced? How often does the confidence-default rule affect the results? How accurate is the AI grader on ambiguous or alternative valid answers? How does performance vary by topic, search budget, and repeated-sampling procedure? How would expert human searchers perform under matched resources? What explains the difference between the 118 reviewed tasks and the final zero-pass percentage? [D]

For the user's research question, the missing investigation would need to distinguish ordinary errors from attacker-induced behavior and compare browsing and non-browsing systems under an explicitly defined threat model. It would need outcomes tied to protected assets or unauthorized actions rather than only answer correctness. These are analyst-identified evidence requirements, not a security study performed or proposed in detail by BrowseComp. [D]

## 19. Terminology and notation glossary

| Term | Meaning within this analysis |
|---|---|
| AI | Artificial intelligence. |
| LLM | Large language model; used in the user's research framing. |
| BrowseComp | Browsing Competition, the supplied benchmark. |
| Browsing agent | A model or agent system using internet access to search for information. |
| Reference answer / ground truth | The answer supplied as the scoring target; the paper acknowledges that some original targets were defective. |
| Inverted question | A question created by starting from an answer and turning its properties into identifying clues. |
| Seed | The person, event, or artifact from which an inverted question is constructed. |
| Entangled information | Information requiring multiple clues or sources to identify the target, as characterized by the authors. |
| Semantic equivalence | Agreement in answer meaning rather than identical wording. |
| Multi-hop facts | Facts requiring connections across pieces of information; used descriptively by the paper. |
| Accuracy | Dataset-level percentage of questions scored correct under an evaluation condition. |
| Pass rate | Observed fraction of repeated attempts that solve one question. |
| Calibration | Agreement between expressed confidence and actual correctness likelihood. |
| Calibration error | Reported percentage-valued reliability measure; its exact formula is absent. |
| Test-time compute | Computational effort during solving. |
| Parallel sample | An additional generated attempt considered in the repeated-output experiment. |
| Majority voting | Choosing the most frequent sampled answer. |
| Weighted voting | Choosing through votes weighted by the corresponding answer confidence. |
| Best-of-N | Selecting the highest-confidence answer among N outputs. |
| Zero-shot | Used by the authors to describe confidence prompting; no detailed definition is supplied. |
| Canary string | A distinctive dataset marker intended to facilitate contamination filtering. |
| Post-hoc | Performed after question collection, as with topic classification. |
| Percentage point | Direct difference between percentages. |
| Relative percentage increase | Difference divided by the starting value, multiplied by 100. |
| N | Number of outputs considered in the best-of-N discussion. |
| k | Analyst-introduced count of correct trials in the explanation k/64. |
| Prompt | Instruction text supplied to an answering or grading model; here analyzed as document content. |
| Threat model | An explicit account of attacker capabilities and protected assets; absent from this paper. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Final benchmark size | 1,266 | questions | Released collection described in paper | Author-reported | pp. 1–4, 8 |
| Original collection | 1,287 | tasks | Before removing defective tasks | Author-reported | p. 8, §4.5 |
| Reviewed zero-pass subset | 118 | tasks | Deep Research failure-triggered review | Author-reported | p. 8, §4.5 |
| Removed tasks | 21 | tasks | Format mismatch, ambiguity, or incorrectness | Author-reported | p. 8, §4.5 |
| Simple-search screening | 5 | searches | Per question, trainer instruction | Author-reported | p. 3, §2.1 |
| Intended human difficulty | 10 | minutes | Partial and not strictly enforced check | Author-reported | p. 3, §2.1 |
| Revision threshold | More than 40 | percent solved | Trainers asked to revise easy task sets | Author-reported | p. 3, §2.1 |
| Human attempted total | 1,255 | questions | 11 benchmark questions unattempted | Author-reported | p. 5, Table 2 |
| Human gave up | 888/1,255; 70.8 | count; percent | After the stated time threshold | Author-reported | p. 5, Table 2 |
| Human reported solved | 367/1,255; 29.2 | count; percent | Solving campaign | Author-reported | p. 5, Table 2 |
| Agreement among solved | 317/367; 86.4 | count; percent | Human answer versus reference | Author-reported | p. 5, Table 2 |
| Agreement among attempted | Approximately 25.3 | percent | 317/1,255 × 100 | Analyst-derived | p. 5, Table 2 |
| Solved-answer disagreements | 50 | answers | 367 − 317 | Analyst-derived | p. 5, Table 2 |
| Giving-up threshold | At least 2 | hours | Caption clarifies human stopping rule | Author-reported | p. 5, Figure 3 |
| GPT-4o accuracy / calibration error | 0.6 / 69 | percent | Without browsing, listed configuration | Author-reported | p. 6, Table 3 |
| GPT-4o browsing accuracy / calibration error | 1.9 / 82 | percent | Search-preview configuration | Author-reported | p. 6, Table 3 |
| GPT-4.5 accuracy / calibration error | 0.9 / 68 | percent | Listed preview configuration | Author-reported | p. 6, Table 3 |
| OpenAI o1 accuracy / calibration error | 9.9 / 65 | percent | Medium reasoning effort, no browsing | Author-reported | p. 6, Table 3 |
| Deep Research accuracy / calibration error | 51.5 / 91 | percent | Task-oriented training disclosed | Author-reported | p. 6, Table 3 |
| GPT-4o listed accuracy difference | 1.3 | percentage points | 1.9 − 0.6 | Analyst-derived | p. 6, Table 3 |
| Deep Research minus o1 accuracy | 41.6 | percentage points | 51.5 − 9.9 | Analyst-derived | p. 6, Table 3 |
| Generated outputs per question | 64 | outputs | Aggregation experiment | Author-reported | p. 7, §4.4 |
| Trials per question | 64 | trials | Pass-rate distribution | Author-reported | p. 8, §4.5 |
| Aggregation improvement wording | 15–25 | percent, units ambiguous | Versus one attempt | Author-reported | p. 7, §4.4 |
| Best-of-N endpoint | Approximately 0.78 | accuracy fraction | 64 samples | Approximate visual estimate | p. 7, Figure 4 |
| Weighted-voting endpoint | Approximately 0.70 | accuracy fraction | 64 samples | Approximate visual estimate | p. 7, Figure 4 |
| Majority-voting endpoint | Approximately 0.67 | accuracy fraction | 64 samples | Approximate visual estimate | p. 7, Figure 4 |
| Deep Research all-success tasks | 16 | percent of tasks | 64/64 successful trials | Author-reported | p. 8, §4.5 |
| Deep Research zero-success tasks | 14 | percent of tasks | 0/64 successful trials | Author-reported | p. 8, §4.5 |
| OpenAI o1 zero-success tasks | 79.3 | percent of tasks | Annotation at zero pass rate | Visually readable | p. 8, Figure 5 |
| Requested confidence range | 0–100 | percent | Answering-model output | Author-reported | p. 11, Appendix A |
| Missing-confidence default | 100 | confidence score | Grader extraction when confidence absent | Author-reported | p. 11, Appendix B |

Figure 2's ten topic counts and percentages are preserved in Section 10 rather than duplicated in this table. No exact count is invented from rounded task percentages, and no runtime, model-size, cost, or statistical-uncertainty value is inferred where absent.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| BrowseComp targets difficult, persistent information discovery | 1,266 short-answer questions and documented construction criteria | X1 | pp. 1–3 | HIGH for stated design; not a universal capability measure. |
| Question discovery can be harder than checking an answer | Inverted construction and answer-provided evidence follow-up | X1, X8 | pp. 3, 8 | HIGH for procedure; follow-up success is qualitative. |
| The tested human searchers found the benchmark difficult | 70.8% gave up; 29.2% reported solved | Table 2, Figure 3, X3 | p. 5 | HIGH under study conditions; humans were not specialist search competitors. |
| Deep Research leads listed single-attempt accuracy | 51.5% versus 0.6–9.9% | Table 3, X4 | p. 6 | HIGH; task-oriented training and differing configurations qualify comparison. |
| Browsing access alone does not ensure strong performance | Listed GPT-4o browsing accuracy is 1.9% | Table 3, X4 | p. 6 | HIGH descriptive evidence; browsing is not isolated as the only changed factor. |
| Browsing configurations have higher reported calibration error | 82% and 91% versus 65–69% | Table 3, X5 | p. 6 | HIGH values; calibration formula absent; mechanism remains suggestive. |
| More browsing effort improves displayed performance | Upward effort–accuracy scatter | Figure 1, X6 | pp. 1, 7 | MEDIUM for quantitative reading; effort units and uncertainty absent. |
| Multiple outputs improve selection accuracy | Increasing curves; best-of-N leads | Figure 4, X7 | p. 7 | HIGH direction; exact endpoints approximate and gain units ambiguous. |
| Difficulty varies substantially by question | Deep Research 16% all-success, 14% zero-success | Figure 5, X8 | p. 8 | HIGH reported proportions; conditional on 64 trials. |
| Original references included defects | 21 removals from 1,287 | X8 | p. 8 | HIGH reported review finding; review-subset count not fully reconciled. |
| Broad browsing generalization is not guaranteed | Explicit scope and generalization qualifications | SS2.4 | p. 4 | HIGH author-stated limitation. |
| Security relevance is indirect | Agent reads multiple web sources; confidence can be unreliable | X4–X5; discussion | pp. 6–9 | MEDIUM analyst inference; no attack or vulnerability comparison is performed. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a web scavenger hunt. You are given several clues about one person, event, or object, but you do not know which one. There may be thousands of candidates. Finding the right candidate is hard; once somebody names it, checking whether it fits the clues is easier. BrowseComp turns that kind of hunt into 1,266 questions for AI systems.

The paper finds that simply giving one tested model access to web search does not make it very good at the hunt. A system trained for persistent research does much better, answering about half the questions correctly in the main comparison. Giving it more effort, or allowing several attempts and choosing among them, improves performance further. The human trainers also struggle, although their search rules and resources differ from the models'.

Being good at finding answers is different from knowing how sure you should be. The best-performing system can still express confidence poorly. Yet its confidence is useful enough that choosing its most confident attempt often helps. Think of someone who is bad at saying 'I am exactly 80% sure' but is still fairly good at choosing which of their own guesses is strongest.

For a security project, this paper tells you that web agents repeatedly read outside information and can be confidently wrong. It does **not** show that an attacker can control them, steal data, or make them break rules. Those possibilities require a different experiment. The safe conclusion is that BrowseComp measures a demanding browsing skill and some reliability problems, while leaving comparative security vulnerability unanswered.

## Completeness Audit

Coverage is judged against the supplied document inventory, not against response length. Every supplied section and substantive visual was inspected in its available form. Text-only coverage is explicitly distinguished from visual inspection.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META: title, authors, affiliation, preprint identification | Yes, text and image | Yes | Fully represented | Venue not invented; equal contribution recorded. |
| ABS: abstract | Yes, text and image | Yes | Fully represented | Central design and scope preserved. |
| S1: §1 Introduction | Yes, text and image | Yes | Represented in compressed form | Motivation and prior-benchmark positioning preserved. |
| S2: §2 opening | Yes, text only | Yes | Fully represented | Human collection and time-stable answer criterion. |
| SS2.1: criteria | Yes, text only | Yes | Fully represented | Three screening checks, inversion, uniqueness caveat. |
| SS2.2: diversity | Yes, text and image | Yes | Fully represented | Topic rationale, counts, and percentages. |
| SS2.3: grading | Yes, text and image | Yes | Fully represented | Semantic comparison and Appendix B connection. |
| SS2.4: exercised skills | Yes, text and image | Yes | Fully represented | Factuality, persistence, creativity, generalization limits. |
| S3: human evaluation | Yes, text and image | Yes | Fully represented | Denominators, time rules, agreement, participant caveat. |
| S4: evaluation overview | Yes, text and images | Yes | Fully represented | Subsections individually covered below. |
| SS4.1: model performance | Yes, text and image | Yes | Fully represented | Identifiers and complete Table 3 values retained. |
| SS4.2: calibration | Yes, text and image | Yes | Fully represented | Metric-definition absence disclosed. |
| SS4.3: effort scaling | Yes, text and images | Yes | Fully represented | Cross-reference to early-model Figure 1 retained. |
| SS4.4: aggregation | Yes, text and image | Yes | Fully represented | All three schemes and unit ambiguity retained. |
| SS4.5: pass rates and review | Yes, text and image | Yes | Fully represented | Follow-up, removals, and count inconsistency retained. |
| S5: related work and discussion | Yes; p. 8 visual, p. 9 text only | Yes | Represented in compressed form | Positioning, target systems, closing scope, future modalities. |
| REF: bibliography | Yes, text only | Yes, collectively | Represented in compressed form | Individual bibliographic entries not reproduced or externally validated. |
| Formal research questions | Checked | Absence represented | Fully represented | No formal list supplied; objectives kept distinct. |
| Formal hypotheses | Checked | Absence represented | Fully represented | Informal compute expectation identified. |
| X1: construction/screening | Yes | Yes | Fully represented | Method and qualifications. |
| X2: topic analysis | Yes | Yes | Fully represented | Descriptive, not topic-wise performance testing. |
| X3: human performance | Yes | Yes | Fully represented | Solve versus agreement distinction. |
| X4: model accuracy | Yes | Yes | Fully represented | Complete numerical comparison. |
| X5: calibration | Yes | Yes | Fully represented | Formula remains unavailable. |
| X6: effort scaling | Yes | Yes | Fully represented | Approximate readings labeled. |
| X7: sampling/aggregation | Yes | Yes | Fully represented | Missing implementation details identified. |
| X8: difficulty/follow-up/filtering | Yes | Yes | Fully represented | No invented follow-up success count. |
| F1 | Yes, visually | Yes | Fully represented | Numeric compute values absent. |
| F2 | Yes, visually | Yes | Fully represented | All topic values preserved. |
| F3, solved panel | Yes, visually | Yes | Fully represented | Scale and time distribution described. |
| F3, gave-up panel | Yes, visually | Yes | Fully represented | Stopping threshold and differing y-scale described. |
| F4 | Yes, visually | Yes | Fully represented | Approximate endpoint values distinguished. |
| F5 | Yes, visually | Yes | Fully represented | 79.3% annotation exceeds displayed axis range. |
| T1 | Yes, visually and text | Yes | Represented in compressed form | Example domains and constraint structure; full clue strings omitted. |
| T2 | Yes, visually and text | Yes | Fully represented | All numerical rows and footnote. |
| T3 | Yes, visually and text | Yes | Fully represented | All values and training footnote. |
| Major equations and theorems | Checked | Absence represented | Fully represented | Analyst explanatory arithmetic labeled separately. |
| Pseudocode algorithms | Checked | Absence represented | Fully represented | Operational voting procedures supplied, no pseudocode. |
| Architecture diagrams | Checked | Absence represented | Fully represented | Evaluation workflow reconstruction explicitly analyst-derived. |
| Major contributions | Yes | Yes | Fully represented | Dataset, benchmark, method, empirical findings, prompts. |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations. |
| Equal-contribution footnote | Yes | Yes | Fully represented | p. 1. |
| Deep Research training footnote | Yes | Yes | Fully represented | p. 6; overlap not inferred. |
| Appendix A | Yes, text only | Yes | Fully represented | Output fields and confidence range. |
| Appendix B | Yes, text only | Yes | Fully represented | Matching criteria, missing-answer and confidence behavior. |
| Separate supplementary files | None supplied | Absence represented | Missing from supplied material | No claim that a specific supplement exists. |
| Linked repository | No | Boundary represented | Inaccessible within supplied-only scope | Not opened, licensing and implementation not credited. |
| Cited external works | No, beyond reference entries | Boundary represented | Inaccessible within supplied-only scope | No outside findings imported. |
| Page layout of pp. 3, 9, 10, 11 | No | Limitation represented | Inaccessible | Text inspected; visual inspection not claimed. |

### Missing or inaccessible material

No page is missing from the supplied 1–11 sequence. Visual renders for pp. 3, 9, 10, and 11 were not supplied. Separate source evidence for individual dataset questions, repository contents, cited works, and any outside supplementary artifacts were not inspected. Detailed compute budgets, calibration formula, grading-model identity, exact aggregation implementation, raw experimental data, and uncertainty estimates are absent from the supplied paper. Their absence limits assessment rather than authorizing reconstruction from external knowledge.

### Uncertain interpretations

The **118** reviewed zero-pass tasks and final **14%** zero-pass proportion are not reconciled by the supplied explanation. The **15–25%** aggregation-improvement wording does not identify percentage points versus relative percent. The human stopping-rule sentence appears to contain a wording error, while the caption gives a coherent at-least-two-hour rule. Exact plot values, histogram bin counts, trial dependence, and calibration computation cannot be established from the images and text provided. Security implications remain analyst inference, with no comparative attack evidence.

### Deliberately compressed material

The complete question-and-answer strings in Table 1 and the inverted-question example on p. 3 are compressed into their substantive design roles. Repeated analogies to programming competitions and repeated descriptions of persistence are consolidated. Bibliographic entries are represented by the authors' related-work positioning rather than individually summarized, because their source documents are not supplied. Page furniture, repeated headings, extraction artifacts, and decorative formatting are not reproduced. Appendix prompts are explained by their operational content rather than quoted in full.

### Potential omissions

No known substantive item in the supplied inventory has been left without representation or an explicit coverage limitation. This statement is restricted to the supplied pages and images. It does not establish exhaustive coverage of the linked repository, every cited work, unavailable visual layouts, raw research artifacts, or other versions of the paper. The user's comparative security question remains unanswered by direct experimental evidence because the supplied paper does not study that outcome.
