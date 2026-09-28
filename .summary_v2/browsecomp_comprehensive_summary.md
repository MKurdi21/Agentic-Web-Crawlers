# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–11 |
| Apparently missing pages | None |
| Native text | Available for all 11 pages |
| Visually rendered pages | Pages 1, 2, 4, 5, 6, 7, and 8 |
| Pages not visually rendered | Pages 3, 9, 10, and 11; assessed from supplied extracted text only |
| Figures | Figures 1–5 are visually available and readable |
| Tables | Tables 1–3 are visually available and readable |
| Equations | No substantive mathematical equations appear |
| Algorithms/pseudocode | None |
| Appendices | Appendices A and B are present on p. 11, despite the mechanical record’s failure to detect appendix pages |
| Supplementary material | None supplied or clearly referenced as a separate supplement |
| External artifacts | The dataset/code repository is referenced but was not supplied or inspected |
| OCR needed | No; native text was supplied. Some extraction on pp. 3–4 and 10–11 contains broken spacing, but the intended prose remains mostly recoverable |
| Important visual limitation | Figures were directly inspected only on the seven rendered pages. Appendices and the methodology prose on p. 3 were not visually cross-checked against their source-page layouts |
| Other limitation | The paper reports using prompts and model procedures but does not provide many implementation details, statistical uncertainty measures, or monetary/compute costs |

The supplied material is sufficient to analyze the complete 11-page paper, including its five figures, three tables, two appendices, and substantive footnote. No outside sources are used below. Information is treated as **author-reported [A]**, **directly observable [B]**, **analyst-derived [C]**, or **analyst interpretation [D]** where distinction matters.

# 1. Plain-Language Orientation

BrowseComp is a benchmark for testing whether an artificial-intelligence agent can persistently search the web for facts that are deliberately difficult to locate. Its 1,266 questions are not ordinary fact lookups. Each combines multiple clues so that the answer may require exploring many pages, reformulating searches, following indirect connections, and rejecting plausible but incorrect candidates (pp. 1–4).

The authors argue that many older information-retrieval benchmarks have become too easy for modern language models. BrowseComp targets a harder capability: finding a particular, obscure answer in a large search space. At the same time, each expected answer is a short string, making the final response comparatively easy to check (§§1–2.4).

The researchers:

- commissioned human trainers to construct and verify difficult, stable, fact-seeking questions;
- evaluated how often other human trainers could solve them;
- tested several OpenAI models with and without web browsing;
- measured confidence calibration;
- varied browsing effort and the number of independent attempts;
- tested three ways of aggregating multiple answers; and
- analyzed per-question pass-rate distributions (§§2–4.5).

The central results are that humans solved only 29.2% of attempted questions under the campaign procedure, while the tested single-run Deep Research system reached 51.5% accuracy. Other evaluated models ranged from 0.6% to 9.9%. More test-time computation improved performance, and selecting the most confident answer from multiple attempts performed best among the tested aggregation methods (Tables 2–3; Figs. 1, 3–5).

The paper’s central contribution is therefore a difficult but operationally simple benchmark for one narrow, important part of browsing-agent competence: persistent and creative retrieval of hard-to-find information.

# 2. Document Roadmap

The paper is organized as follows:

1. **Abstract and Figure 1 (p. 1):** Introduce BrowseComp and preview the relationship between browsing effort and accuracy.
2. **§1 Introduction (p. 2):** Motivate machine web browsing, distinguish BrowseComp from easier retrieval benchmarks, show three protected examples in Table 1, and state the benchmark’s design goals.
3. **§2 Data collection and verification (pp. 3–4):**
   - §2.1 defines question-construction and difficulty criteria.
   - §2.2 reports topic diversity in Figure 2.
   - §2.3 describes model-based answer grading.
   - §2.4 explains the capabilities BrowseComp is intended to exercise.
4. **§3 Human performance (p. 5):** Reports the human campaign in Table 2 and time distributions in Figure 3.
5. **§4 Model evaluation (pp. 6–8):**
   - §4.1 compares five model configurations.
   - §4.2 examines confidence calibration.
   - §4.3 examines test-time compute scaling.
   - §4.4 evaluates multi-sample aggregation.
   - §4.5 examines per-task pass rates and documents dataset cleaning.
6. **§5 Related work and discussion (pp. 8–9):** Positions the benchmark relative to prior retrieval and agent work and states its intended scope.
7. **References (pp. 9–10).**
8. **Appendix A (p. 11):** Gives the exact-answer and confidence-output instruction.
9. **Appendix B (p. 11):** Gives the model-grading prompt.

# 3. Background and Context

A **benchmark** is a standardized collection of tasks used to compare systems. BrowseComp is specifically a browsing-agent benchmark: the system is expected to use the open web rather than merely answer from its stored model knowledge.

A **browsing agent** is a model-driven system that can issue searches, visit pages, interpret material, and adjust its search strategy. The authors distinguish this from a chatbot answering from internal knowledge and from systems that make only a small number of tool calls (§§1, 5).

The benchmark focuses on **multi-constraint fact seeking**. A question supplies several attributes whose intersection points to a short answer. The authors call the construction process **inverted question creation**: trainers begin with a known person, event, or artifact and then formulate indirect identifying clues around it (§2.1).

Two difficulty notions recur:

- **Finding difficulty:** discovering the target among many possible candidates.
- **Verification simplicity:** once a candidate is proposed, comparing it with the short reference answer is intended to be easy (§§1–2.3).

**Test-time compute** means computation spent while answering, rather than during training. Here it includes greater browsing effort within an attempt and running multiple attempts per question (§§4.3–4.4).

**Calibration** concerns whether stated confidence corresponds to actual correctness. A well-calibrated system should, for example, be correct about as often as its stated probability implies across comparable predictions. The paper reports a calibration-error percentage but does not supply its formula (§4.2, Table 3).

A **pass rate** is the fraction of repeated trials on a particular question that produce a correct answer. Section 4.5 uses 64 trials per question.

# 4. Research Problem and Gap

## Existing problem

Finding complicated factual information through ordinary human browsing can be slow and cognitively demanding. Humans have limited attention, memory, and stamina; they also cannot naturally conduct many searches in parallel (§1).

## Shortcomings of prior approaches, as characterized by the authors

The paper says most earlier information-retrieval benchmarks concentrate on information a human can find relatively easily, often within about ten minutes. Recent language models have saturated many such benchmarks (§§1, 5).

The authors also suggest that early web agents with limited tool calls and weak backtracking would struggle on harder, deeply entangled retrieval tasks (§5). This is their positioning of the literature, not an independently verified survey conclusion.

## Research gap

The authors identify a need for a benchmark that is simultaneously:

- hard enough to require persistent, strategic browsing;
- reliable enough for evaluation;
- simple to use and grade; and
- focused on obscure, multi-hop information rather than routine lookup (§1).

## Motivation

A sufficiently capable agent might search much more broadly and persistently than a person, potentially recovering a well-specified item even when thousands of pages must be considered. A benchmark is needed to measure progress toward that capability (§1).

## Scope

BrowseComp measures retrieval of one short, targeted answer. It does not attempt to represent common user-query distributions, long-form answer quality, interaction ergonomics, or ambiguity resolution (§§1, 2.4, 5).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper does not enumerate formal research questions.

## Author-stated or clearly expressed objectives

- Create a benchmark of extremely difficult but easily graded browsing questions (§§1–2).
- Measure persistence, search creativity, factual reasoning, and depth of browsing (§2.4).
- Establish task difficulty through human and model performance (§§3–4.1).
- Assess whether browsing capability and reasoning both contribute to success (§4.1).
- Evaluate confidence calibration (§4.2).
- Test whether performance scales with additional test-time compute (§4.3).
- Test whether repeated attempts and aggregation improve performance (§4.4).
- Characterize variation in question difficulty using per-task pass rates (§4.5).

## Hypotheses or expectations

No formal null/alternative hypotheses are declared. The authors express an expectation that additional test-time compute should improve accuracy because the questions require searching many sites (§4.3). Figure 1 and Figure 4 are presented as supporting this expectation.

# 6. Assumptions / Threat Model

This is a benchmark paper, not a cybersecurity study, so it has no attacker threat model. Its operative assumptions are:

- Questions have single, short, stable answers supported by evidence (§2).
- Reference answers are correct, although uniqueness cannot be guaranteed (§2.1).
- A system may use the open web when evaluated as a browsing agent.
- Semantic-equivalence grading by an AI model adequately determines whether a predicted short answer matches the reference (§2.3; Appendix B).
- More search effort and multiple independent trials are meaningful forms of test-time computation (§§4.3–4.4).
- Model-assigned confidence may be used both to evaluate calibration and to rank or weight repeated responses (§§4.2, 4.4).

For the human comparison, participants could not answer their own questions and were prohibited from using named AI assistants. The paper does not report a standardized search interface, browser environment, or formal control over human search skill (§3).

The benchmark’s data-integrity assumptions include limiting leakage. Table 1 asks readers not to repost its examples, and the dataset includes a canary string intended to facilitate filtering from training corpora (§1, Table 1). This analysis therefore does not reproduce the protected examples and answers.

# 7. Methodology

## Study design

This is a mixed **benchmark-construction and empirical evaluation study**. It includes human-authored data collection, human validation, model-based grading, human difficulty measurement, model comparisons, compute-scaling experiments, aggregation experiments, and dataset-quality review.

## Dataset construction

Human trainers created difficult fact-seeking questions with a single short answer expected not to change over time and with supporting evidence. The instructions largely followed SimpleQA (§2).

The construction procedure was usually inverted:

1. Select a seed fact, person, event, or artifact.
2. Find several identifying characteristics.
3. Create a question whose combined constraints imply the seed.
4. Add more criteria if multiple answers appear plausible (§2.1).

## Difficulty controls

Three checks were used (§2.1):

1. GPT-4o with and without browsing, OpenAI o1, and an early Deep Research version had to fail the proposed problem.
2. Trainers performed five simple Google searches and verified that the answer was not readily available on the first result pages.
3. Questions were intended to resist another human for ten minutes. This was not strictly enforced for every item; where second-trainer testing occurred, authors whose questions were solved more than 40% of the time were asked to revise them.

The exact amount of second-trainer testing is not reported.

## Answer uniqueness and validation

The authors explicitly acknowledge that inverted construction establishes that the reference answer fits, but cannot prove that no other answer fits. Trainers were asked to know the topic well enough to be fairly confident about uniqueness and to add constraints when uncertain. If a second trainer found a different valid answer within ten minutes, the question was revised (§2.1).

## Dataset size and composition

The released benchmark contains 1,266 questions. It originally contained 1,287, but 21 of 118 questions on which Deep Research scored 0% across repeated trials were removed after review (§4.5).

Topic classification was performed after collection by prompting ChatGPT. Figure 2 reports ten categories totaling 1,266 items (§2.2).

## Grading

A predicted response is evaluated for semantic equivalence to the short reference answer using an AI judge and the Humanity’s Last Exam grading prompt (§2.3; Appendix B). The judge extracts the final answer, explains match or mismatch, produces a yes/no correctness judgment, and extracts confidence. If no confidence is supplied, it assigns 100 (Appendix B).

No judge model/version, human validation rate, inter-rater analysis, or grading-error estimate is reported.

## Human evaluation

Human trainers came from the same trainer pool that created the questions, but they could not solve items they themselves had authored. They had no reference answer and could not use ChatGPT, Claude, Perplexity, Grok, or Gemini. They could give up after attempting a question for approximately two hours and self-reported elapsed time (§3).

Of 1,266 questions, 11 were not attempted, leaving 1,255 in the human campaign (Table 2).

The text contains a likely wording error: “we allowed trainers … if they could solve it within 2 hours” (p. 5). Context, Table 2, and Figure 3 indicate that the intended condition was inability to solve within roughly two hours.

## Model configurations

The tested configurations were (§4.1):

- GPT-4o: `gpt-4o-2024-08-06`
- GPT-4o with browsing: `gpt-4o-search-preview-2025-03-11`
- GPT-4.5: `gpt-4.5-preview-2025-02-27`
- OpenAI o1: `o1-2024-12-17-medium reasoning effort`
- OpenAI Deep Research

The paper does not report temperature, decoding settings, browser restrictions, search-provider details, timeouts, token budgets, exact per-model sample counts for Table 3, random seeds, hardware, software libraries, or monetary cost.

The substantive footnote on p. 6 states that Deep Research was trained on data specifically intended to make it good at “BrowsingComp” tasks. “BrowsingComp” appears to be a naming inconsistency with “BrowseComp”; the exact degree of train–test overlap is not specified.

## Confidence and calibration

Models were instructed to provide an explanation, exact answer, and confidence from 0% to 100% (Appendix A). Table 3 reports calibration error, but neither its equation nor binning/estimation procedure is supplied.

## Compute-scaling and aggregation

Figure 1 varies browsing effort within an early Deep Research version. The exact compute units are not labeled; only a log-scaled test-time-compute axis is shown (§4.3).

For parallel sampling, the authors generated 64 outputs per question, each with model-assigned confidence, then examined prefixes of 1, 2, 4, 8, 16, 32, and 64 samples (Figure 4). The three aggregators were:

- **Majority voting:** select the most frequent answer.
- **Weighted voting:** weight each answer vote by its assigned confidence.
- **Best-of-N:** select the individual response with the highest confidence (§4.4).

## Statistics

The paper reports percentages and distributions but no confidence intervals, hypothesis tests, standard errors, or statistical-significance tests. The word “significantly” in §4.1 appears colloquial; no inferential test is presented.

# 8. Experiments / Analyses

## X1 — Human difficulty study

- **Purpose:** Estimate how difficult BrowseComp is for experienced trainers.
- **Sample:** 1,255 attempted questions; 11 of 1,266 were unattempted.
- **Conditions:** No named AI assistants; no one answered their own authored item; giving up permitted after roughly two hours.
- **Metrics:** Solved fraction, agreement with the reference among solved items, and self-reported time.
- **Results:** 367/1,255 solved (29.2%); 888/1,255 abandoned (70.8%); 317/367 solved responses matched the reference (86.4%) (Table 2).
- **Caveat:** Participants were not described as elite investigators, and time was self-reported (§3).

**Analyst-derived [C]:** 50 solved submissions did not agree with the reference: \(367-317=50\). This could reflect participant errors, alternative answers, or reference/format issues; the supplied study does not adjudicate those 50 cases.

## X2 — Single-model performance comparison

- **Purpose:** Compare reasoning-only, browsing-enabled, and persistent-browsing systems.
- **Data:** BrowseComp’s 1,266 questions.
- **Metric:** Accuracy.
- **Results:** GPT-4o 0.6%; GPT-4o with browsing 1.9%; GPT-4.5 0.9%; OpenAI o1 9.9%; Deep Research 51.5% (Table 3).
- **Interpretation:** The authors argue that browsing alone is insufficient and that reasoning plus persistent tool use matters.
- **Caveat:** Only OpenAI model configurations are evaluated, and several procedural details are absent.

**Analyst-derived [C]:**

- Browsing GPT-4o gains 1.3 percentage points over GPT-4o: \(1.9-0.6=1.3\).
- Relative to 0.6%, that is approximately a 216.7% increase: \(1.3/0.6\times100\), although both absolute accuracies remain very low.
- Deep Research exceeds o1 by 41.6 percentage points: \(51.5-9.9=41.6\).

## X3 — Confidence-calibration analysis

- **Purpose:** Determine whether confidence reflects correctness.
- **Procedure:** Each response contains a 0%–100% confidence value.
- **Metric:** Calibration error, whose formula is not specified.
- **Results:** GPT-4o 69%; browsing GPT-4o 82%; GPT-4.5 68%; o1 65%; Deep Research 91% (Table 3).
- **Interpretation:** Browsing-capable systems have particularly high reported calibration errors and may be overconfident when wrong (§4.2).
- **Caveat:** Without a metric definition or uncertainty estimates, the magnitude is hard to interpret precisely.

## X4 — Within-attempt test-time compute scaling

- **Purpose:** Test whether more browsing effort improves Deep Research.
- **Independent variable:** Test-time compute/browsing effort on a log scale.
- **Dependent variable:** BrowseComp accuracy.
- **Evidence:** Figure 1.
- **Result:** Accuracy rises smoothly from approximately 9% at the lowest displayed effort to approximately 52% at the highest.
- **Caveat:** These are visual estimates; compute values and run settings are not numerically labeled.

## X5 — Parallel sampling and aggregation

- **Purpose:** Determine whether repeated attempts and confidence-based selection improve accuracy.
- **Procedure:** Generate 64 outputs per question and aggregate at N = 1, 2, 4, 8, 16, 32, and 64.
- **Methods:** Majority vote, confidence-weighted vote, and best-of-N.
- **Result:** All improve with N; best-of-N is consistently highest after the one-sample point and reaches approximately 0.78 accuracy at N=64 (Figure 4).
- **Author characterization:** The approaches improve performance by 15%–25% over a single attempt.
- **Caveat:** The paper does not clarify whether 15%–25% means relative percent or percentage points. The graph suggests approximately 15–26 percentage points, depending on the method.

## X6 — Per-task pass-rate distribution

- **Purpose:** Characterize heterogeneity in question difficulty.
- **Procedure:** Run 64 trials per question for Deep Research and o1 across 1,266 tasks.
- **Metric:** Per-question fraction of successful trials.
- **Results:** Deep Research succeeds in all 64 trials for 16% of tasks and in none for 14%. o1 has a very large 0-pass-rate mass labeled 79.3% (Figure 5; §4.5).
- **Interpretation:** Difficulty varies substantially by task structure or domain.

## X7 — Guided evidence-retrieval follow-up

- **Purpose:** Determine whether questions never solved by Deep Research were impossible or merely hard to discover.
- **Procedure:** Supply the ground-truth answer and ask Deep Research to retrieve supporting web evidence.
- **Result:** The model succeeded “in most cases”; no exact numerator or percentage is supplied (§4.5).
- **Interpretation:** Many failures concern search strategy and discovery rather than inability to recognize evidence once guided.

## X8 — Dataset-quality review

- **Purpose:** Audit tasks with 0% Deep Research pass rate.
- **Initial dataset:** 1,287 tasks.
- **Reviewed subset:** 118 tasks with 0% pass rate.
- **Removed:** 21 tasks with mismatched answer format, ambiguous phrasing, or an incorrect reference based on reasoning.
- **Final dataset:** 1,266 tasks (§4.5).
- **Analyst-derived [C]:** The removal rate among reviewed zero-pass tasks was approximately 17.8%: \(21/118\times100\). The overall dataset removal rate was approximately 1.63%: \(21/1,287\times100\).

# 9. Results

| Finding | Evidence and condition | Supported interpretation | Qualification |
|---|---|---|---|
| BrowseComp is difficult for the tested humans | 29.2% solved; 70.8% gave up (Table 2) | Questions often demand prolonged search | Trainer population and interface were not fully characterized |
| Human “solved” responses did not always match references | 86.4% agreement among 367 solved items | Solving claims and exact reference matching differ | Causes of the 50 disagreements were not analyzed |
| Ordinary tested models perform near zero | GPT-4o 0.6%; GPT-4.5 0.9% (Table 3) | Internal knowledge alone is usually insufficient for this benchmark | Only selected OpenAI models were studied |
| Basic browsing adds little without stronger strategy | GPT-4o rises from 0.6% to 1.9% | Tool access by itself is insufficient | Different model configurations may differ beyond browsing access |
| Reasoning-only o1 performs better than GPT-4o variants | 9.9% versus ≤1.9% | Some answers can be inferred from internal knowledge and reasoning | No causal isolation of “reasoning strength” is provided |
| Deep Research is strongest | 51.5% accuracy | Persistent web search plus reasoning is useful | Footnote says it was trained for this task type |
| Calibration is poor, especially for Deep Research | Calibration error 91% for Deep Research | High accuracy does not imply reliable uncertainty estimates | Metric definition is missing |
| Greater browsing effort improves accuracy | Figure 1 rises approximately 9%→52% | Test-time compute scales performance | Exact compute values are absent |
| Repeated attempts improve performance | Figure 4; roughly 0.52 at N=1 to 0.67–0.78 at N=64 | Diverse attempts uncover additional correct answers | Compute and cost grow substantially but are not quantified |
| Best-of-N performs best | Approximately 0.78 at N=64 | Confidence contains useful ranking information | Useful ranking confidence coexists with poor probability calibration |
| Difficulty varies by question | Deep Research: 16% always solved and 14% never solved | Tasks are not uniformly difficult | Domain-stratified results are absent |
| Dataset auditing found label issues | 21 of 118 reviewed zero-pass items removed | Extreme failures can expose benchmark defects | Review focused on one failure-defined subset |

# 10. Figure-by-Figure Interpretation

## Figure 1 — Accuracy versus browsing effort

- **Location:** p. 1; discussed in §4.3, p. 7.
- **Purpose:** Show performance scaling for an early version of Deep Research.
- **Plot:** Scatter plot.
- **X-axis:** “Test-time compute (log-scale)”; numeric tick labels are absent.
- **Y-axis:** BrowseComp accuracy (%), visually spanning 0–60%.
- **Encoding:** Blue circular markers connected implicitly by their ordered placement; no error bars.
- **Direct observation [B]:** Approximately 13 plotted runs form a largely smooth increasing curve.
- **Approximate visual values [B]:** The series begins near 9%, then rises through roughly 14%, 17%, 19%, 23%, 27%, 31%, 35%, 39%, 42%, 46%, 49%, and 52%.
- **Conclusion supported:** Greater test-time browsing effort is associated with higher accuracy.
- **Caveats:** Exact compute, uncertainty, costs, and point values are not shown. The graph establishes an empirical association across configurations, not a general scaling law.

## Figure 2 — Topic distribution

- **Location:** p. 4, §2.2.
- **Purpose:** Show topical breadth across all 1,266 questions.
- **Plot:** Pie chart.
- **Encoding:** Ten colored wedges linked to a legend containing counts.
- **Values [A/B]:**
  - TV shows & movies: 205 (16.2%)
  - Other: 197 (15.6%)
  - Science & technology: 173 (13.7%)
  - Art: 127 (10.0%)
  - History: 125 (9.9%)
  - Sports: 123 (9.7%)
  - Music: 116 (9.2%)
  - Video games: 71 (5.6%)
  - Geography: 70 (5.5%)
  - Politics: 59 (4.7%)
- **Cross-check:** Counts sum exactly to 1,266 [C].
- **Conclusion supported:** The dataset covers multiple broad topics, with entertainment-related material particularly prominent.
- **Caveat:** Categories were assigned post hoc by a prompted ChatGPT model; no validation, taxonomy instructions, or classification accuracy is reported.

## Figure 3 — Human search-time histograms

- **Location:** p. 5, §3.
- **Panels:** Two.
- **Left panel:** Questions humans reported solving.
- **Right panel:** Questions on which humans gave up.
- **X-axis:** Time in minutes, shown from 0 to 300.
- **Y-axis:** Number of problems; left reaches about 80, right about 600.
- **Encoding:** Green bars for solved tasks; orange bars for abandoned tasks.
- **Direct observations [B]:**
  - Solved times are broadly distributed, with a visible peak near 120–135 minutes and smaller counts before and after.
  - Give-up times cluster strongly around 120 minutes, with a second concentration around 150 minutes and few much later observations.
- **Conclusion supported:** Even successful searches often took substantial time; abandonment mostly occurred around the permitted two-hour threshold.
- **Caveats:** Times were self-reported. Exact bin widths and counts are not tabulated. Some apparent post-two-hour abandonments are unexplained.

## Figure 4 — Aggregation performance by sample count

- **Location:** p. 7, §§4.3–4.4.
- **Plot:** Three line series.
- **X-axis:** Number of parallel samples per task: 1, 2, 4, 8, 16, 32, 64.
- **Y-axis:** Accuracy from 0.50 to 0.80.
- **Series:** Best-of-N, weighted voting, and majority voting.
- **Approximate visual estimates [B]:**

| N | Best-of-N | Weighted voting | Majority voting |
|---:|---:|---:|---:|
| 1 | 0.52 | 0.52 | 0.52 |
| 2 | 0.60 | 0.60 | 0.53 |
| 4 | 0.67 | 0.65 | 0.58 |
| 8 | 0.71 | 0.67 | 0.63 |
| 16 | 0.74 | 0.69 | 0.66 |
| 32 | 0.76 | 0.69 | 0.67 |
| 64 | 0.78 | 0.70 | 0.67 |

- **Observations:** Best-of-N continues improving through 64 samples. Weighted and majority voting flatten earlier.
- **Conclusion supported:** Repeated sampling improves accuracy, and confidence is more useful for choosing the strongest individual answer than for calibrated probability reporting.
- **Caveats:** No confidence intervals or repeated-run variation are shown. “Parallel” describes independent samples but hardware parallelism is not documented.

## Figure 5 — Distribution of per-question pass rates

- **Location:** p. 8, §4.5.
- **Plot:** Overlaid/grouped histogram-like bars.
- **X-axis:** Pass rate from 0 to 1.
- **Y-axis:** Percentage of all tasks, 0–20% on the displayed scale.
- **Encoding:** Red for o1 and light blue for Deep Research.
- **Exact labeled or text-reported values:**
  - o1: 79.3% of tasks at 0 pass rate [B].
  - Deep Research: 16% of tasks at 100% pass rate [A].
  - Deep Research: 14% at 0% pass rate [A].
- **Direct observation [B]:** Deep Research is distributed across the full range and has its largest displayed mass at pass rate 1. o1 is dominated by the off-scale zero-pass bar, with relatively small mass elsewhere.
- **Conclusion supported:** Deep Research succeeds reliably on some tasks, never succeeds on others, and has varying success on the remainder.
- **Caveat:** Exact intermediate-bin percentages and bin definitions are not tabulated. The 79.3% annotation exceeds the plotted y-axis and is indicated above a truncated red bar.

# 11. Table-by-Table Interpretation

## Table 1 — Protected example questions

- **Location:** p. 2, §1.
- **Purpose:** Illustrate multi-constraint questions across different subject areas and show that expected answers are short.
- **Structure:** Three columns, each containing one question and its reference answer.
- **What it demonstrates:** Solving requires intersecting several indirect clues rather than retrieving a plainly worded fact.
- **Data-integrity note:** The authors explicitly request that these examples not be revealed in plain text or images online to reduce benchmark leakage. Accordingly, they are not reproduced here.
- **Canary:** The caption supplies a unique canary string to assist filtering the benchmark from training corpora.
- **Caveat:** Three examples cannot establish the character of all 1,266 items.

## Table 2 — Human performance

- **Location:** p. 5, §3.
- **Rows and values:**
  - Total attempted in campaign: 1,255.
  - Gave up after two hours: 888/1,255 (70.8%).
  - Solved by human: 367/1,255 (29.2%).
  - Agreement among solved items: 317/367 (86.4%).
- **Footnote:** Eleven of the 1,266 dataset questions were not attempted.
- **Cross-check:** 888 + 367 = 1,255 [C].
- **What it demonstrates:** Most attempted questions were not solved within the campaign procedure.
- **Caveat:** “Solved” is self-assessed before comparison with the reference; 50 such answers failed the reference match [C].

## Table 3 — Model accuracy and calibration

- **Location:** p. 6, §§4.1–4.2.
- **Columns:** Model, accuracy (%), calibration error (%).
- **Values:**

| Model | Accuracy | Calibration error |
|---|---:|---:|
| GPT-4o | 0.6% | 69% |
| GPT-4o with browsing | 1.9% | 82% |
| GPT-4.5 | 0.9% | 68% |
| OpenAI o1 | 9.9% | 65% |
| Deep Research | 51.5% | 91% |

- **Best accuracy:** Deep Research, 51.5%.
- **Lowest calibration error:** o1, 65%, though every reported value is large.
- **Worst accuracy:** GPT-4o, 0.6%.
- **Largest calibration error:** Deep Research, 91%.
- **Footnote:** Deep Research was trained on data specifically designed for this task type.
- **What it demonstrates:** High task accuracy and good calibration do not coincide here.
- **Missing statistical information:** No confidence intervals, standard errors, significance tests, or calibration definition.

# 12. Diagram / Architecture Interpretation

The paper contains no substantive architecture diagram, flowchart, or system-component diagram. Its methodology is described through prose, tables, and plots.

A conceptual workflow can be reconstructed from author-reported procedures, but this is not a supplied diagram:

1. Human trainer chooses a seed.
2. Trainer constructs an indirect multi-constraint question.
3. Trainer performs model and search difficulty checks.
4. Another trainer may attempt validation.
5. A model or human produces an answer.
6. An AI judge compares the extracted short answer with the reference.
7. Accuracy, confidence calibration, or repeated-trial pass rate is calculated.

This reconstruction is **analyst-organized [D]**, though each component is reported in §§2–4 and Appendices A–B.

# 13. Equations and Mathematical Concepts

No numbered equations, theorems, lemmas, or formal optimization objectives appear.

The main mathematical concepts are:

- **Accuracy:** the percentage of benchmark questions judged correct. The paper does not explicitly print a formula, but its use is conventional and recoverable as correct answers divided by evaluated questions.
- **Per-task pass rate:** correct trials divided by 64 repeated trials for that question (§4.5).
- **Majority vote:** choose the answer with the largest raw sample count (§4.4).
- **Confidence-weighted vote:** sum confidence weights associated with each answer and choose the answer with greatest total weight (§4.4).
- **Best-of-N:** select the single sampled response having the highest model-assigned confidence (§4.4).
- **Calibration error:** a discrepancy between confidence and empirical correctness (§4.2). Its exact mathematical definition is absent, so no formula should be inferred.
- **Logarithmic scale:** equal visual distances on Figure 1 represent multiplicative rather than additive changes in compute. The compute unit and tick values are missing.

The exact model-response template in Appendix A requires:

- an explanation;
- a succinct final answer; and
- a confidence score from 0% to 100%.

Appendix B specifies a structured judging result with extracted answer, reasoning, yes/no correctness, and extracted confidence.

# 14. Interpretation and Discussion

The evidence supports the paper’s core contention that BrowseComp is difficult for the evaluated participants and models. Human trainers familiar with the benchmark process solved fewer than one-third of attempted items under the campaign rules, and ordinary tested language models achieved below 2% except for o1. Deep Research’s 51.5% establishes that specialized persistent browsing can make large gains without saturating the benchmark.

The comparison between GPT-4o, browsing GPT-4o, and o1 motivates the authors’ view that neither browsing access nor reasoning alone is enough. However, this should be read as suggestive rather than a controlled causal decomposition: the configurations differ in model design and possibly other unreported respects.

The confidence results reveal two distinct properties:

- **Probability calibration:** whether a stated confidence value accurately estimates correctness.
- **Within-set ranking:** whether confidence can help identify the best answer among several attempts.

Deep Research performs poorly on the first but usefully on the second. Its 91% calibration error is the worst reported, yet best-of-N selection substantially improves accuracy. Therefore, a confidence signal can be mis-scaled as a probability while still ordering candidate answers productively.

Figure 5 and the guided follow-up suggest that failures are heterogeneous. Some questions are consistently solvable; some resist every unguided trial; others are solved intermittently. When given the correct answer, Deep Research could usually retrieve support, indicating that discovering the candidate—not merely verifying evidence—is often the hard part. Because “most cases” is not quantified, the strength of that conclusion cannot be measured precisely.

## Consistency findings

- Final dataset counts are consistent: Figure 2 categories total 1,266.
- Human campaign counts are consistent: 888 + 367 = 1,255, with 11 unattempted.
- Dataset revision is consistent: 1,287 − 21 = 1,266.
- Deep Research’s single-attempt performance is approximately 51.5% in Table 3 and approximately 0.52 at N=1 in Figure 4.
- Figure 1’s high endpoint is approximately consistent with the 51.5% result, though it concerns an “early version” and exact equivalence is not stated.
- Figure 5 says Deep Research has 14% zero-pass tasks, while §4.5 says 118 tasks were reviewed as zero-pass from the original 1,287-task set. These are not necessarily contradictory because the review concerns the pre-removal dataset, whereas the distribution concerns the final benchmark.
- “BrowsingComp” in the p. 6 footnote is inconsistent with the benchmark name “BrowseComp.”
- The p. 5 sentence about giving up contains a probable omitted negation; surrounding evidence indicates giving up after failure to solve within two hours.
- §4.4’s “15% to 25%” improvement is ambiguous between relative percentages and percentage points.
- The paper refers to Deep Research as “significantly” outperforming other models but reports no inferential statistical test.

# 15. Contributions and Novelty

## Conceptual contribution

The paper frames persistent, creative web search for obscure multi-constraint answers as a distinct capability worth evaluating.

## Dataset contribution

It releases 1,266 human-authored, fact-seeking questions with short reference answers, supporting evidence during creation, broad topic coverage, and explicit difficulty-screening procedures.

## Benchmark-design contribution

BrowseComp combines high discovery difficulty with simple output and grading. The authors present this as analogous to programming competitions: intentionally incomplete as a representation of real work but useful for measuring a core capability.

## Methodological contribution

The construction procedure uses inverted questions, model-failure screening, simple-search screening, limited second-trainer validation, confidence-bearing responses, and semantic-equivalence grading.

## Empirical contribution

The paper supplies:

- human difficulty measurements;
- five model accuracy/calibration results;
- within-attempt compute scaling;
- multi-attempt aggregation comparisons;
- per-task pass-rate distributions; and
- a guided retrieval follow-up on persistent failures.

## Implementation/resource contribution

The paper states that BrowseComp is available through the `simple-evals` repository. The repository itself was outside the supplied document and was not inspected.

# 16. Limitations

## Authors’ stated limitations

1. **Incomplete proxy for browsing ability:** BrowseComp covers an important but limited subset of browsing competence (§§1, 2.4).
2. **Not a true user-query distribution:** It avoids long answers and ambiguity resolution (§§1, 2.4).
3. **Answer uniqueness is not guaranteed:** Inverted construction confirms one correct answer but cannot exhaustively eliminate alternatives (§2.1).
4. **Generalization is not guaranteed:** High BrowseComp performance need not transfer to every browsing task (§2.4).
5. **Human comparison is not an expert ceiling:** Trainers were not competition-level browsers; detectives or investigative journalists with ample time might solve more (§3).
6. **Deep Research confidence is poorly calibrated:** It often fails to communicate uncertainty accurately (§4.2).
7. **Current modality is textual:** Future benchmarks could require images, video, audio, or interactive webpages (§5).

## Additional evidence-based analyst observations

These are **analyst observations [D]**, not author admissions:

- The benchmark and baseline systems are produced by the same organization, creating a possible benchmark–system coupling concern.
- The Deep Research footnote reports task-specific training, but the nature of that training and separation from benchmark test items are not described.
- Only OpenAI systems are evaluated, limiting cross-provider conclusions.
- The question-authoring population, compensation, demographics, expertise, and number of trainers are not reported.
- “Personally interesting” topic selection is not a controlled sampling strategy and yields a distribution with substantial entertainment content.
- Post-hoc topic labels come from a prompted ChatGPT model without reported validation.
- The AI judge is not named or validated in the paper.
- Human times are self-reported, and the human search environment is not standardized in the reported methodology.
- Statistical uncertainty is absent.
- Compute, monetary cost, latency, and environmental resource use are not quantified.
- Reviewing only persistent Deep Research failures may not detect ambiguous or incorrect labels among easier items.
- Removing items after observing model behavior can make dataset quality better but also couples benchmark composition to one evaluated system.
- Short-answer equivalence is simpler than long-form grading but still permits judge disagreement, format sensitivity, aliases, and multiple-valid-answer problems.

# 17. Threats to Validity

These categories are analyst-applied unless otherwise noted.

## Internal validity

The model comparison does not isolate browsing, reasoning, training, and model scale as independent variables. Therefore, causal claims that a particular capability produced the differences should remain cautious.

The Deep Research training footnote raises uncertainty about how much performance comes from broadly useful browsing competence versus task-specific preparation.

## Construct validity

BrowseComp operationalizes browsing skill as finding a single short answer under artificially inverted clues. This captures persistence and search strategy but omits long-form synthesis, clarification, interactive navigation, multimodal evidence, and common user needs.

Calibration error lacks a formula, making the measured construct difficult to reproduce.

## External validity

The topic distribution is trainer-interest-driven rather than population-derived. Results may not generalize to common web queries, professional research, multilingual browsing, changing information, or other agents.

## Statistical conclusion validity

No error bars, confidence intervals, significance tests, or repeated evaluation estimates are reported. Accuracy differences are often large, but their uncertainty cannot be assessed from the paper.

## Ecological validity

Real users may provide ambiguous requests, revise their goals, require source-quality judgments, or want a narrative answer. BrowseComp deliberately removes many of those complications.

## Reproducibility

The questions, reference answers, prompts, and model identifiers are partially documented, but key inference settings, browse budgets, tool interfaces, calibration formula, judge model, hardware, and compute measures are missing. Appendix prompts improve reproducibility but do not fully specify the evaluation.

## Data validity

Question uniqueness is probabilistic rather than exhaustive. The review found 21 defective tasks among 118 persistent failures, confirming that label and phrasing errors occurred during construction.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Develop benchmarks requiring interaction with images, video, audio, or interactive webpages (§5).
- Use the released benchmark to encourage more trustworthy and reliable agents.
- Evaluate additional AI agents on BrowseComp.
- Collect feedback from researchers (§5).

## B. Additional open questions

- How does performance break down by topic, clue count, source type, or required search depth?
- How reproducible are results under standardized time, query, page-visit, token, or dollar budgets?
- How accurately does the AI judge agree with careful human grading?
- How many questions have valid answers other than the designated reference?
- What is the exact nature of Deep Research’s task-specific training?
- Do gains persist for non-OpenAI agents?
- How stable are results as the web changes?
- Does best-of-N remain beneficial once compute cost and latency are considered?
- Can confidence be recalibrated without destroying its useful candidate-ranking signal?
- Would systematic auditing of all questions reveal defects beyond those found among zero-pass tasks?
- How do expert investigators compare with trainers and browsing agents under identical resources?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| BrowseComp | “Browsing Competition,” a benchmark for difficult web-search agents |
| Agent | A model-based system able to take actions such as searching and visiting pages |
| Benchmark | A standardized test set used to measure and compare systems |
| Browsing effort | Amount of search work or compute used during an answer attempt |
| Calibration | Agreement between stated confidence and actual probability of correctness |
| Calibration error | A measure of mismatch between confidence and correctness; exact formula not specified here |
| Canary string | A distinctive sequence inserted to help detect or filter benchmark material in training data |
| Deep Research | The paper’s specialized agent for persistent web browsing |
| Ground truth / reference answer | The answer designated correct by the benchmark creators |
| Inverted question | A question constructed by starting from a known answer and turning its characteristics into clues |
| Multi-hop | Requiring multiple pieces or stages of information gathering |
| Pass rate | Fraction of repeated attempts on one question that are correct |
| Post hoc classification | Categorization performed after the data were collected |
| Semantic equivalence | Matching in meaning even when wording is not identical |
| Test-time compute | Computation spent while producing an answer |
| Majority voting | Choosing the answer occurring most often among samples |
| Weighted voting | Choosing using confidence-weighted sample votes |
| Best-of-N | Choosing the most confident single answer from N attempts |
| N | Number of sampled attempts considered |
| GPT-4o, GPT-4.5, o1 | Specific model configurations evaluated in the paper |
| AI judge/grader | A model that decides whether the submitted answer matches the reference |
| 0% pass rate | None of the 64 trials solved a particular question |
| 100% pass rate | All 64 trials solved a particular question |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Final benchmark size | 1,266 | questions | Released BrowseComp | Author-reported | p. 1; §§1, 4.5 |
| Original dataset size | 1,287 | questions | Before failure review | Author-reported | p. 8, §4.5 |
| Removed tasks | 21 | questions | Defective among 118 reviewed | Author-reported | p. 8, §4.5 |
| Removal rate among reviewed tasks | 17.8 | % | \(21/118\) | Analyst-derived | p. 8, §4.5 |
| Overall original-set removal rate | 1.63 | % | \(21/1,287\) | Analyst-derived | p. 8, §4.5 |
| Human-attempted tasks | 1,255 | questions | 11 were unattempted | Author-reported | p. 5, Table 2 |
| Human give-ups | 888/1,255 (70.8%) | questions / % | Roughly two-hour threshold | Author-reported | p. 5, Table 2 |
| Human solved | 367/1,255 (29.2%) | questions / % | Campaign procedure | Author-reported | p. 5, Table 2 |
| Reference agreement among solved | 317/367 (86.4%) | questions / % | Human answer vs. reference | Author-reported | p. 5, Table 2 |
| Solved/reference disagreements | 50 | questions | \(367-317\) | Analyst-derived | p. 5, Table 2 |
| GPT-4o accuracy | 0.6 | % | No browsing | Author-reported | p. 6, Table 3 |
| GPT-4o browsing accuracy | 1.9 | % | Search-preview model | Author-reported | p. 6, Table 3 |
| GPT-4.5 accuracy | 0.9 | % | No browsing | Author-reported | p. 6, Table 3 |
| o1 accuracy | 9.9 | % | Medium reasoning effort, no browsing | Author-reported | p. 6, Table 3 |
| Deep Research accuracy | 51.5 | % | Single model evaluation | Author-reported | p. 6, Table 3 |
| Browsing GPT-4o absolute gain | 1.3 | percentage points | \(1.9-0.6\) | Analyst-derived | p. 6, Table 3 |
| Deep Research advantage over o1 | 41.6 | percentage points | \(51.5-9.9\) | Analyst-derived | p. 6, Table 3 |
| GPT-4o calibration error | 69 | % | Confidence evaluation | Author-reported | p. 6, Table 3 |
| GPT-4o browsing calibration error | 82 | % | Confidence evaluation | Author-reported | p. 6, Table 3 |
| GPT-4.5 calibration error | 68 | % | Confidence evaluation | Author-reported | p. 6, Table 3 |
| o1 calibration error | 65 | % | Confidence evaluation | Author-reported | p. 6, Table 3 |
| Deep Research calibration error | 91 | % | Confidence evaluation | Author-reported | p. 6, Table 3 |
| Repeated outputs | 64 | outputs/question | Aggregation study | Author-reported | p. 7, §4.4 |
| Best-of-N at N=64 | ≈0.78 | accuracy | Figure reading | Approximate visual estimate | p. 7, Fig. 4 |
| Weighted vote at N=64 | ≈0.70 | accuracy | Figure reading | Approximate visual estimate | p. 7, Fig. 4 |
| Majority vote at N=64 | ≈0.67 | accuracy | Figure reading | Approximate visual estimate | p. 7, Fig. 4 |
| Reported aggregation improvement | 15–25 | % (ambiguous) | Versus one attempt | Author-reported | p. 7, §4.4 |
| Deep Research always-solved tasks | 16 | % of tasks | 100% pass rate over 64 trials | Author-reported | p. 8, §4.5 |
| Deep Research never-solved tasks | 14 | % of tasks | 0% pass rate over 64 trials | Author-reported | p. 8, §4.5 |
| o1 never-solved tasks | 79.3 | % of tasks | 0% pass-rate bin | Visually readable | p. 8, Fig. 5 |
| Largest topic category | 205 (16.2%) | questions / % | TV shows & movies | Author-reported/visually readable | p. 4, Fig. 2 |
| Smallest topic category | 59 (4.7%) | questions / % | Politics | Author-reported/visually readable | p. 4, Fig. 2 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| BrowseComp is difficult for tested humans | 70.8% gave up; 29.2% solved | X1; Table 2; Figure 3 | p. 5, §3 | Strong for this trainer campaign; not a general human ceiling |
| Simple browsing access is insufficient | GPT-4o rises only 0.6%→1.9% | X2; Table 3 | p. 6, §4.1 | Suggestive; not a fully controlled comparison |
| Reasoning contributes to performance | o1 without browsing reaches 9.9% | X2; Table 3 | p. 6, §4.1 | Suggestive; model differences are not isolated |
| Persistent browsing plus reasoning is effective | Deep Research reaches 51.5% | X2; Table 3 | p. 6, §4.1 | Strong within tested systems; task-specific training is a caveat |
| Deep Research confidence is poorly calibrated | 91% calibration error | X3; Table 3 | p. 6, §4.2 | Numerically clear but metric definition missing |
| More browsing effort improves accuracy | Smooth increasing curve | X4; Figure 1 | pp. 1, 7 | Strong descriptive evidence; exact compute is absent |
| Repeated attempts improve accuracy | All three Figure 4 curves rise with N | X5; Figure 4 | p. 7 | Strong descriptive evidence; no uncertainty estimates |
| Best-of-N is the best tested aggregation rule | Highest curve across N>1 | X5; Figure 4 | p. 7 | Strong within the plotted settings |
| Confidence retains useful ranking information | Best-of-N outperforms voting despite poor calibration | X3/X5; Table 3, Fig. 4 | pp. 6–7 | Reasonable author interpretation, not direct proof of mechanism |
| Task difficulty is heterogeneous | 14% never and 16% always solved by Deep Research | X6; Figure 5 | p. 8 | Strong distributional evidence |
| Many zero-pass failures concern discovery rather than evidence retrieval | Guided model succeeds in “most cases” | X7 | p. 8, §4.5 | Qualitative; exact count absent |
| Dataset auditing improves label quality | 21 defective tasks removed | X8 | p. 8, §4.5 | Direct evidence for the reviewed subset |
| Benchmark measures a useful but incomplete capability | Design scope and empirical results | §§1–5 | pp. 1–9 | Conceptual claim; authors explicitly qualify generalization |

# 22. Very Simple Explanation

Imagine someone gives an AI a riddle whose answer is somewhere on the internet. The clues may refer to several different facts, and no search result directly states the answer. The AI must search, follow leads, combine clues, and keep trying. BrowseComp contains 1,266 such riddles, each designed to have a short final answer.

These questions were genuinely hard under the reported tests. Human trainers solved 29.2% of the questions they attempted. Ordinary models scored from 0.6% to 9.9%, while a specialized Deep Research browsing agent scored 51.5%.

Giving the agent more time and more attempts helped. Running 64 searches and selecting the answer with the highest self-reported confidence produced about 78% accuracy in the plotted experiment. Interestingly, the agent’s confidence was bad as an exact probability, but still useful for deciding which of its own answers looked best.

The benchmark is valuable because it tests persistence and clever searching in a simple format. It is not a complete test of whether an AI is good at helping people on the web: it does not test ordinary questions, conversations, long reports, ambiguous requests, or most non-textual interaction.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation, arXiv metadata | Yes | Yes | Fully represented | Title metadata appears on p. 1 |
| Abstract | Yes | Yes | Fully represented | Integrated into orientation and contributions |
| §1 Introduction | Yes, visual and text | Yes | Fully represented | Includes motivation, scope, design goals, Table 1 |
| §2 Data collection and verification | Yes, text | Yes | Fully represented | p. 3 was not visually rendered |
| §2.1 BrowseComp criteria | Yes, text | Yes | Fully represented | All three difficulty checks and uniqueness caveat covered |
| §2.2 Dataset diversity | Yes, visual and text | Yes | Fully represented | All ten categories covered |
| §2.3 Grading | Yes, visual and text | Yes | Fully represented | Appendix B connected to methodology |
| §2.4 What BrowseComp exercises | Yes, visual and text | Yes | Fully represented | Factuality, persistence, creativity, scope |
| §3 Human performance | Yes, visual and text | Yes | Fully represented | Table 2 and both Figure 3 panels covered |
| §4 Evaluation of models | Yes, visual and text | Yes | Fully represented | All five subsections covered |
| §4.1 Model performance | Yes | Yes | Fully represented | All models and values covered |
| §4.2 Calibration | Yes | Yes | Fully represented | Metric-definition absence noted |
| §4.3 Test-time compute | Yes | Yes | Fully represented | Figure 1 cross-referenced |
| §4.4 Aggregation | Yes | Yes | Fully represented | All three rules and plotted results covered |
| §4.5 Pass-rate distribution | Yes | Yes | Fully represented | Follow-up and data cleaning covered |
| §5 Related work and discussion | Yes, text | Yes | Represented in compressed form | Literature citations grouped by role |
| References | Yes, text | Partly | Deliberately compressed | Bibliographic entries not repeated individually |
| Figure 1 | Yes, visual | Yes | Fully represented | Exact point values unavailable |
| Figure 2 | Yes, visual | Yes | Fully represented | Counts and percentages transcribed |
| Figure 3, both panels | Yes, visual | Yes | Fully represented | Bin counts treated as approximate/unlabeled |
| Figure 4 | Yes, visual | Yes | Fully represented | Approximate point values explicitly labeled |
| Figure 5 | Yes, visual | Yes | Fully represented | Intermediate-bin values not estimated individually |
| Table 1 | Yes, visual | Yes | Represented in compressed form | Examples withheld to honor authors’ anti-leakage request |
| Table 2 | Yes, visual | Yes | Fully represented | Counts cross-checked |
| Table 3 | Yes, visual | Yes | Fully represented | All values and footnote covered |
| Appendix A | Yes, text | Yes | Fully represented | Page not visually rendered |
| Appendix B | Yes, text | Yes | Fully represented | Page not visually rendered |
| Footnote on equal contribution | Yes | No substantive analysis needed | Inspected but non-substantive | Jason Wei and Zhiqing Sun marked equal contributors |
| Deep Research training footnote | Yes | Yes | Fully represented | Naming inconsistency noted |
| Explicit research questions | Yes | Yes | Fully represented | None formally enumerated |
| Hypotheses | Yes | Yes | Fully represented | No formal hypotheses; expectation identified |
| Experiments/analyses X1–X8 | Yes | Yes | Fully represented | Individually registered |
| Major equations | Yes | Yes | Fully represented | None present |
| Algorithms/pseudocode | Yes | Yes | Fully represented | None present |
| Architecture diagrams | Yes | Yes | Fully represented | None present |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations |
| Supplementary material | N/A | Yes | Missing from supplied material | None supplied or explicitly referenced as a separate supplement |
| Dataset/code repository | No | Yes | Inaccessible external artifact | Referenced but excluded by closed-document mode |

## Missing or inaccessible material

- Pages 3, 9, 10, and 11 were not visually rendered; only their supplied native/extracted text was inspected.
- The linked dataset and `simple-evals` repository were not supplied and were not accessed.
- Supporting web evidence collected for individual questions was not included.
- Raw human-response data, raw model outputs, per-question results, and grader outputs were not supplied.
- Exact compute budgets, costs, search traces, and implementation configuration were not supplied.
- No separate supplementary material was provided.

## Uncertain interpretations

- The exact definition of calibration error is absent.
- Figure 1 lacks numeric compute values and exact labels for individual accuracies.
- Figure 3 does not tabulate bin widths or exact bar counts.
- Figure 4 values other than the authors’ broad improvement statement are visual estimates.
- Figure 5’s intermediate bins are visually readable only approximately.
- “15% to 25%” in §4.4 is ambiguous between relative improvement and percentage-point improvement.
- The degree and nature of Deep Research’s task-specific training are unspecified.
- The human give-up sentence on p. 5 appears to omit “not”; this interpretation is based on Table 2, Figure 3, and surrounding prose.
- “BrowsingComp” in the p. 6 footnote appears to refer to BrowseComp but is not silently corrected in the analysis.
- “Most cases” in the guided-retrieval follow-up is unquantified.
- It is unclear whether Figure 1’s early Deep Research version is identical to the Table 3 system.

## Deliberately compressed material

- The individual bibliography entries were not reproduced; the related-work categories and author positioning were summarized.
- Table 1’s protected questions and answers were not repeated because the authors explicitly request that they not be redistributed.
- Routine prose repeating the benchmark’s “hard to find, easy to verify” framing was consolidated.
- Figure 5’s many unlabeled intermediate bins were summarized as a distribution rather than assigned unreliable numeric estimates.
- Appendix prompts were explained structurally instead of copied verbatim.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, appendix, major numerical result, contribution, or author-stated limitation in the supplied 11-page document is absent from this analysis. The principal coverage limitation is visual: four pages were available only as extracted text, and external artifacts referenced by the paper were not supplied or inspected.