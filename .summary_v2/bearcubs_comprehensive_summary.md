# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes. Complete page-labeled text for pp. 1–20 was supplied. |
| Available page range | pp. 1–20 |
| Apparently missing pages | None |
| Native text | Available for every page; no page was flagged as scanned or unusually low-text. |
| Visually rendered pages inspected | pp. 1–4, 6–10, and 15–20 |
| Pages not visually rendered | pp. 5 and 11–14. Page 5 contains prose; pp. 11–14 contain acknowledgments, references, and the beginning of Appendix A. These pages were inspected through supplied native text, not page images. |
| Figures | Figures 1–4 were visually available. Figures 1–3 were clearly readable. Figure 4’s labeled stacked bars were readable on p. 20. |
| Tables | Tables 1–10 were available through extracted text; Tables 1–10 also appear on rendered pages except Table 2’s extended interpretation depends partly on prose. Fine text in Table 9 is dense but recoverable from the supplied page text. |
| Equations | No substantive mathematical equations appear in the paper. Percentages, averages, and evaluator classifications are reported, but no numbered mathematical formulation is introduced. |
| Algorithms/pseudocode | None. Figure 3 is a workflow diagram, not executable pseudocode. |
| Appendices | Appendices A–K are present on pp. 14–20. |
| Supplementary material | No supplementary file was supplied. The dataset, leaderboard, full evaluator prompt, and evaluator code are referenced as available on the project website but are not part of the supplied document. |
| OCR needed | No. Native text was supplied. OCR-sensitive items—especially symbols, table alignment, and duplicated percent signs in Table 9—were checked against rendered pages where available. |
| Material limitations | The individual benchmark questions, gold answers, complete trajectories, raw screen recordings, full 17-example evaluator prompt, evaluator code, and per-question results are not included. Table 6 says it concerns six error causes but visually presents only three examples, with multiple causes combined in the first. |
| Analysis boundary | Closed-document mode. No external facts or verification are introduced. |

# 1. Plain-Language Orientation

BEARCUBS—“BEnchmark for Agents with Real-world Computer Use and Browsing Skills”—tests whether artificial-intelligence agents can use the live web to find precise factual answers. These agents do more than retrieve text: some can inspect pixels and operate a virtual mouse and keyboard. The benchmark therefore asks whether they can locate the right website, navigate it, interpret its content, and return a short, definite answer.

The problem matters because success on simulated websites or familiar benchmark environments may not transfer to the changing, messy public web. A real website may require clicking through a scanned document, manipulating an interactive database, watching a video, navigating a three-dimensional tour, playing a web game, or dealing with access restrictions. A search engine may also expose an unintended textual shortcut that defeats the purpose of testing those interactions.

The authors construct 111 live-web question–answer pairs:

- 56 text-based questions;
- 55 multimodal questions;
- 108 distinct top-level URLs across the human-validated routes;
- one short, unique answer and one viable browsing trajectory for each question.

They compare humans, five simple or search-augmented baselines, three web-research agents without full computer use, and four agents with computer-use capabilities. Humans reach 84.7% accuracy. The strongest tested computer-using system, ChatGPT Agent, reaches 65.8%; the next-best computer-use system, Operator, reaches 23.4%. ChatGPT Agent performs much better than earlier agents, but still trails humans—especially on multimodal tasks, interactive filtering, fine cursor control, and execution speed (pp. 6–8, Tables 2 and 9).

The central contribution is therefore not a new agent. It is a curated, evolving benchmark and an accompanying empirical diagnosis of where contemporary web agents fail: multimodal interaction, credible sourcing, efficient planning, trajectory transparency, and avoiding textual workarounds.

# 2. Document Roadmap

| Location | Content and role |
|---|---|
| Abstract and §1, pp. 1–2 | Introduce BEARCUBS, motivate live-web and multimodal evaluation, and summarize the main results. |
| §2, pp. 2–3 | Defines four benchmark-construction problems: contamination, workarounds, interaction diversity, and slow evaluation. |
| §3, pp. 3–5 | Describes the benchmark, question criteria, collection, validation, and dataset statistics. |
| §4, pp. 5–6 | Defines the human study, agent groups, baselines, execution protocol, and answer-scoring rule. |
| §5, pp. 6–8 | Reports human and agent performance and interprets major failure patterns. |
| §6, pp. 8–10 | Discusses trajectory transparency, source credibility, multimodal interaction, and planning. |
| §7, p. 10 | Positions the benchmark relative to low-level web skills, web-agent evaluation, and non-web agent benchmarks. |
| §8, p. 10 | Restates the contributions and principal findings. |
| pp. 11–14 | Acknowledgments and references; Appendix A begins on p. 14. |
| Appendix A, pp. 14–15 | Authors’ stated benchmark limitations. |
| Appendix B, p. 15 | Detailed question criteria and creation/validation workflow. |
| Appendix C, p. 15 | Human-annotator recruitment and compensation. |
| Appendix D, p. 16 | Baseline models, hyperparameters, and search-augmented prompt. |
| Appendix E, p. 16 | Detailed human-performance statistics. |
| Appendix F, pp. 16–17 | Examples and categories of human error. |
| Appendix G, pp. 16–19 | Automatic answer-evaluator prompt, configuration, and validation. |
| Appendix H, pp. 17–19 | Detailed agent results by question modality. |
| Appendix I, pp. 17–20 | Defense of the benchmark’s size and four-run variance analysis. |
| Appendix J, pp. 18–20 | Source attribution of agents’ correct answers. |
| Appendix K, pp. 19–20 | Agent-specific behaviors. |

# 3. Background and Context

A **large language model (LLM)** produces and reasons over language. A conventional text-only browsing agent may receive webpage text or search snippets. A **computer-using web agent** instead perceives the displayed interface and can issue mouse and keyboard actions.

A **live-web benchmark** uses currently accessible public websites. This improves realism but makes the evaluation unstable: pages can change, links can break, and answers can leak into search results.

A **trajectory** is the recorded route and action sequence used to solve a task—for example, searches, opened pages, clicks, keystrokes, and navigation decisions. BEARCUBS includes a human-validated viable trajectory for each question, although the complete trajectories are not printed in the paper.

The paper distinguishes:

- **Text-based questions:** require reading or navigating textual content, sometimes in complex databases.
- **Multimodal questions:** require interpreting or interacting with images, videos, audio, virtual tours, games, or other non-text interfaces.
- **Workaround:** an unintended route that answers a supposedly multimodal question using searchable text rather than the target interaction.
- **Contamination:** benchmark information becoming available to a model through training data or online indexing. On the live web, publishing a question can itself lead to searchable answers.
- **Primary source:** in Table 9, a reliable source or the source specified by the question.
- **Secondary source:** an unreliable source or one not specified by the question.
- **Ungrounded answer:** an answer based on the agent’s internal knowledge or reasoning rather than an identified source.
- **Abstention/uncertain response:** no direct, definite answer.
- **None/no answer:** either an explicit “No answer found” from a baseline or a loop/stall that yields no response.

# 4. Research Problem and Gap

## Existing problem

Computer-using agents could potentially perform any operation visible on a screen, yet evaluating them on realistic public websites is difficult (§1, pp. 1–2).

## Shortcomings attributed to prior benchmarks

The authors identify three major shortcomings:

1. **Synthetic or simulated environments.** WebArena and WebShop are cited as examples whose controlled environments do not fully capture dynamic live-web behavior (§1, pp. 1–2).
2. **Performance saturation.** The paper reports Operator at 87% on WebVoyager and 58% on WebArena, while reporting 78% human performance on WebArena (p. 2).
3. **Restricted interaction coverage.** Some benchmarks can be solved from HTML, while others focus on narrower modalities such as maps or images rather than video browsing, real-time games, and 3D navigation (p. 2).

## Research gap

According to the authors, a benchmark was needed that jointly offered:

- interaction with unpredictable live websites;
- broad text and multimodal task diversity;
- resistance to search-snippet and text-only shortcuts;
- concise, objective answers;
- human-validated trajectories suitable for examining agent behavior.

## Motivation

Benchmark scores on controlled environments may obscure failures in finding reliable information on actual websites. The authors also argue that correctness alone hides whether an answer came from the requested source, an unreliable secondary source, or unsupported guessing (§6, p. 9).

## Scope

BEARCUBS evaluates factual information seeking. Every retained question has a single concise answer and a publicly accessible solution path. It does not principally test open-ended generation, questions with no answer, multiple valid answers, or long-form responses (Appendix A, pp. 14–15).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper states one direct question in §1:

- **RQ1:** “How well do [computer-using agents] actually perform in real-world web browsing scenarios?” (p. 1)

Section 4.1 states a second direct question:

- **RQ2:** “How well do humans perform on BEARCUBS?” (p. 5)

## Objectives

The authors aim to:

1. Construct a live-web benchmark of diverse information-seeking tasks.
2. Ensure that multimodal tasks genuinely require multimodal interaction.
3. Establish human performance and identify human error sources.
4. compare baseline language models, search agents, and computer-use agents.
5. analyze trajectories, source use, execution time, and agent-specific failures.
6. maintain the benchmark by replacing invalid or contaminated questions.

## Hypotheses

No formal statistical hypotheses are declared. The design implicitly tests two author expectations, but these should not be treated as formally preregistered hypotheses:

- zero-shot language models and simple search-snippet augmentation should not solve the benchmark well (§4.2, p. 5);
- current agents should exhibit meaningful shortcomings on diverse live-web and multimodal tasks.

No null-hypothesis significance tests, confidence intervals, or p-values are reported.

# 6. Assumptions / Threat Model

This is not a security paper and contains no attacker threat model. Its relevant evaluation assumptions are:

- Each retained question has a correct, unique, concise answer (Appendix B, p. 15).
- Each answer is publicly accessible without payment, account creation, or login.
- A valid solution requires interaction with the live web.
- Multimodal questions must not be answerable by text-only systems.
- At least two authors verify each question, answer, viable trajectory, and relevant links.
- A response is correct only if it directly and unambiguously entails the gold answer.
- Hedged guesses are not accepted as correct.
- Agents should work autonomously. One extra directive is allowed if an agent requests assistance; a repeated request terminates the session (§4.2, p. 6).
- Computer-use agents normally receive 15 minutes, while ChatGPT Agent receives 45 minutes because it can solve questions after the standard limit (footnote 3, p. 3).
- Humans may abandon after 15 minutes (§4.1, p. 5).
- Public release creates contamination risk, which the authors propose mitigating through periodic replacement rather than secrecy (footnote 2, p. 2).

The supplied paper does not define a frozen website snapshot, deterministic browser environment, common hardware configuration, or uniform commercial-agent backend version beyond the named products and evaluation dates.

# 7. Methodology

## 7.1 Study design

The work combines:

- benchmark construction and validation;
- a human performance study;
- evaluation of model baselines and commercial web agents;
- qualitative trajectory/error analysis;
- automatic evaluator validation;
- a four-run stability check for DeepSeek R1.

## 7.2 Dataset construction

BEARCUBS contains 111 questions: 65 authored by the research team and 46 accepted from freelancers (pp. 3–4). The freelancer count is **analyst-derived** as \(111-65=46\).

Only 58.2% of freelancer-created questions were accepted (p. 3). Freelancers received $4 per accepted question (footnote 4, p. 4).

Every question includes:

- question text;
- short gold answer;
- viable human-written trajectory;
- visited-websites list.

The four acceptance criteria are:

1. short but sufficiently informative question;
2. correct, unique, concise answer;
3. resistance to Google Search snippets/top results;
4. public availability without paywall or login.

Multimodal questions undergo additional checks against text-only systems. Thirteen candidate questions were removed, mostly because Deep Research found textual workarounds (p. 3).

## 7.3 Dataset composition

Table 1 (p. 4) reports:

| Split | Questions | Distinct top-level URLs | Mean steps | Step range | Mean webpages | Webpage range |
|---|---:|---:|---:|---:|---:|---:|
| Text-based | 56 | 61 | 6.5 | 3–12 | 3.8 | 1–8 |
| Multimodal | 55 | 47 | 5.8 | 3–14 | 3.0 | 1–6 |
| All | 111 | 108 | 6.1 | 3–14 | 3.4 | 1–8 |

Google Search visits are excluded from the URL counts.

## 7.4 Human study

People who had not previously seen a given question used a web browser without prescribed navigation restrictions. They recorded:

1. elapsed time;
2. answer;
3. number of dead ends;
4. free-form difficulty comments;
5. perceived difficulty label.

A dead end means leaving the current page to backtrack or restarting the search (footnote 7, p. 5).

Recruitment was matched to language needs:

- volunteers for Arabic and Mandarin Chinese;
- three Upwork annotators for Hindi, German, and Finnish;
- annotators and authors who had neither written nor validated the relevant questions for the English-only set.

Paid human annotators received $2.50 per question plus a $1 bonus for each correct answer (Appendix C, p. 15). The paper does not report the total number of distinct human participants.

## 7.5 Evaluated systems

### Baselines

- GPT-4o (`gpt-4o-2024-11-20`), zero-shot;
- DeepSeek R1, zero-shot;
- GPT-4o plus Google Search snippets;
- DeepSeek R1 plus Google Search snippets;
- Perplexity sonar-pro.

For search augmentation, each question retrieves up to ten results through Serper. Titles and snippets are concatenated with the question (pp. 5–6).

Appendix D reports:

- GPT-4o: maximum 518 tokens, temperature 0;
- DeepSeek R1: maximum 8,000 tokens, temperature 0;
- prompt instructing the model to rely on supplied context and return “No answer found” if it lacks a direct answer.

The markedly different token limits are reported but not justified.

### Web agents without computer use

- Grok 3 DeepSearch;
- OpenAI Deep Research;
- Google Deep Research.

### Web agents with computer use

- Convergence AI Proxy;
- Anthropic Computer Use;
- OpenAI Operator;
- OpenAI ChatGPT Agent.

## 7.6 Execution protocol

Because the agents lacked suitable APIs, the authors manually entered each question into each web interface, screen-recorded sessions, and denied normal requests for user help. Computer-use agents received an autonomy prompt, and an agent requesting assistance received one extra directive to solve the task independently. A second request ended the session (pp. 3 and 6).

Recorded outcomes were:

- final response;
- time per question;
- trajectory.

Sessions ended at an answer, abstention, or non-progress loop.

Evaluation dates were February 23–March 1, 2025 for most agents; late May for Google Deep Research; and July 18–20, 2025 for ChatGPT Agent (footnote 13, p. 6).

## 7.7 Answer evaluation

A response counted as correct only if it unambiguously entailed the gold answer. Modal or hedged statements were not concrete answers (§4.2, p. 6).

The authors also built a GPT-4o-based evaluator with four labels:

- no answer;
- no direct answer;
- correct;
- wrong.

It used temperature 0 and 17 in-context examples, although only the first two are printed. Evaluating 111 responses took about 1 minute 30 seconds and cost approximately $0.80 (Appendix G, pp. 16–18).

The automatic evaluator was applied to five agents, not to every baseline or agent. Its main validation metric was agreement accuracy against the manually assigned labels.

## 7.8 Statistical methodology

The main analyses are descriptive:

- accuracy;
- counts of response labels;
- mean completion times;
- human dead ends;
- perceived difficulty;
- source-attribution proportions;
- standard deviation across four DeepSeek R1 trials.

No confidence intervals, formal significance tests, corrections for multiple comparisons, or inferential effect estimates are reported. Although the prose sometimes says one model “significantly” outperforms another, the supplied paper does not report a corresponding statistical test.

## 7.9 Hardware, software, and reproducibility details

No browser version, operating system, hardware, display resolution, network conditions, or detailed website-state controls are reported. The paper identifies Fireworks AI and later OpenRouter for DeepSeek R1 trials and Serper for Google Search results. Commercial systems were manually operated through their web interfaces.

# 8. Experiments / Analyses

## X1 — Human performance study

**Purpose:** Establish whether the questions are solvable and non-trivial, and diagnose human difficulties.

**Data:** All 111 questions, divided into 56 text and 55 multimodal questions.

**Metrics:** Accuracy, answer status, elapsed time, number of dead ends, and perceived difficulty.

**Results:** Humans achieve 94 correct, 14 wrong, and 3 abandoned answers: 84.7% accuracy (Tables 2 and 5). Multimodal accuracy is 85.7%, slightly above 83.6% for text questions. Average overall time is 4:46, with 1.50 dead ends.

**Caveat:** The paper does not state the number of participants or per-participant workload, preventing assessment of participant-level variation or dependence among observations.

## X2 — Zero-shot and simple search baselines

**Purpose:** Determine whether model memory or search snippets make BEARCUBS trivial.

**Conditions:** GPT-4o and DeepSeek R1 in zero-shot and Serper-augmented settings; Perplexity sonar-pro as an answer-engine baseline.

**Metric:** Exact task accuracy under the direct-answer rule.

**Results:** DeepSeek R1 zero-shot is best among the two zero-shot models at 8.1%. Perplexity sonar-pro reaches 5.4%. GPT-4o plus search scores 0.0%, and DeepSeek R1 plus search scores 1.8% (Table 2).

**Authors’ interpretation:** Correct answers are not easily recoverable from search snippets, and zero-shot success is largely guessing.

**Caveat:** Search-augmented GPT-4o returns “None” on 107 of 111 questions because the prompt explicitly requires “No answer found” without direct snippet evidence. This is a stringent retrieval test, but it is not equivalent to an interactive browsing agent.

## X3 — Non-computer-use web-agent evaluation

**Purpose:** Measure advanced web search and reasoning without broad direct interface manipulation.

**Systems:** Grok 3 DeepSearch, OpenAI Deep Research, and Google Deep Research.

**Results:** Overall accuracies are 11.7%, 36.0%, and 23.4%, respectively. OpenAI Deep Research reaches 60.7% on text questions but only 10.9% on multimodal questions (Tables 2 and 9).

**Interpretation:** Strong search/reasoning can solve many text questions but does not replace reliable multimodal interaction.

**Caveat:** The authors report that Deep Research’s multimodal successes were often guesses, determined through trajectory inspection rather than a separately quantified causal test.

## X4 — Computer-use agent evaluation

**Purpose:** Evaluate systems that can manipulate live interfaces.

**Systems:** Proxy, Anthropic Computer Use, Operator, and ChatGPT Agent.

**Results:** Overall accuracies are 12.6%, 14.4%, 23.4%, and 65.8%. ChatGPT Agent reaches 76.8% on text and 54.5% on multimodal questions.

**Interpretation:** ChatGPT Agent represents a large capability improvement, including game, CAPTCHA, video, and 3D-navigation tasks, yet remains below humans.

**Caveat:** ChatGPT Agent had a 45-minute limit versus 15 minutes for the other computer-use agents. Its mean correct-answer time was also much longer: 9:16 overall and 13:15 on multimodal questions (Tables 2 and 9).

## X5 — Human error analysis

**Purpose:** Identify why verified, answerable questions still defeat people.

**Evidence:** Free-form comments and Table 6 examples.

**Reported causes:** Missing or overlooking details, lack of topic knowledge, suboptimal source selection, obvious oversight, and task complexity. The prose says Table 6 lists six causes, but the caption says “five key reasons”; the supplied table visually shows several combined labels and three examples. The sixth category cannot be confidently reconstructed.

## X6 — Agent trajectory and failure analysis

**Purpose:** Diagnose behavior not captured by final-answer accuracy.

**Evidence:** Figure 1, Table 3, trajectory recordings, action counts, and qualitative inspection.

**Findings:** Agents may stop before a critical click, abandon the requested source, choose irrelevant pages, avoid multimodal interactions, repeat failed actions, or provide trajectories too granular or too vague to audit.

**Caveat:** Step definitions differ by agent: sources, saved HTML activity records, visible “Tool Use” actions, or provider-displayed steps are counted depending on the system (footnote 19, p. 8). Counts are therefore not directly standardized.

## X7 — Source-credibility analysis

**Purpose:** Determine whether correct answers are grounded in the requested or reliable source.

**Evidence:** Figure 4 and Table 9.

**Results:** Most correct answers from computer-use agents are primary-sourced. OpenAI Deep Research is an exception: 25 of 40 correct answers are primary, 10 secondary, and 5 ungrounded. Thus 15/40 = 37.5% are non-primary.

**Inconsistency:** §6 says 38.5% (p. 9), while §5.2 says 37.5% (p. 8), Table 9 gives 15/40 = 37.5%, and Figure 4 visually labels the two non-primary portions 25.64% and 12.82%, summing to 38.46%. This likely reflects a denominator mismatch, but the supplied paper does not explain it.

## X8 — Automatic evaluator validation

**Purpose:** Test whether GPT-4o can reproduce manual response labels.

**Data:** Outputs from five agents.

**Metrics:** Four-way and binary classification accuracy.

**Results:** Four-way accuracy ranges from 96.4% to 99.1%; binary accuracy ranges from 96.4% to 100% (Table 8). Three repeated runs on Anthropic and Proxy outputs give identical results.

**Caveat:** The paper does not report classwise metrics, confusion matrices, uncertainty, or a held-out design for the 17 in-context examples.

## X9 — Four-run stability analysis

**Purpose:** Argue that the 111-item benchmark is meaningful despite its small size.

**Conditions:** DeepSeek R1 with and without Serper over four trials.

**Results:** Without Serper: 7.2%, 5.4%, 5.4%, 5.4%, reported standard deviation 0.8%. With Serper: 1.8%, 0.9%, 2.7%, 2.7%, reported standard deviation 0.7% (Table 10).

**Interpretation:** The authors view these as low run-to-run variances.

**Caveat:** Stability is shown for one model family at very low accuracy; it does not establish stability for all agents or per-category estimates.

## X10 — Agent-specific behavior

Appendix K reports that Grok 3 may produce its trajectory in a non-English input language and never abstains. Computer Use sometimes declares a task impossible without attempting it. The authors regard these as questions for user-centered evaluation rather than automatically desirable or undesirable behaviors.

# 9. Results

## 9.1 Human–agent gap

Humans score 84.7%; ChatGPT Agent scores 65.8% (Table 2).

**Analyst-derived:** the absolute gap is:

\[
84.7-65.8=18.9\text{ percentage points}.
\]

This is a percentage-point difference, not a 18.9% relative reduction.

## 9.2 ChatGPT Agent versus Operator

ChatGPT Agent scores 65.8%; Operator scores 23.4%.

**Analyst-derived from displayed rounded percentages:** \(65.8-23.4=42.4\) percentage points, matching the prose on p. 6.

For multimodal questions, the displayed scores are 54.5% versus 12.7%, a 41.8-point difference, matching p. 8.

## 9.3 Humans are comparatively strong on multimodal tasks

Humans score 85.7% multimodal and 83.6% text-based (Tables 2 and 5).

**Analyst-derived:** multimodal performance is 2.1 percentage points higher. The result contradicts the pattern for every tested agent, all of which perform worse on multimodal questions.

## 9.4 ChatGPT Agent narrows but does not close the modality gap

ChatGPT Agent reaches:

- 76.8% on text questions;
- 54.5% on multimodal questions.

**Analyst-derived:** its modality gap is 22.3 percentage points.

The authors connect failures to fine interaction, interactive database filtering, long runtimes, and access restrictions (§5.2 and §6).

## 9.5 Search-only strength is concentrated in text tasks

OpenAI Deep Research scores:

- 36.0% overall;
- 60.7% text;
- 10.9% multimodal.

Its 34 correct text answers constitute most of its 40 total correct answers (Table 9). The authors say its six multimodal successes are largely guesses based on trajectory inspection.

## 9.6 Earlier computer-use agents perform poorly

Proxy and Anthropic Computer Use both score 9.1% on multimodal questions, below Deep Research’s 10.9%. Operator reaches 12.7%. The paper interprets this as evidence that merely having computer-control tools does not guarantee effective multimodal reasoning.

## 9.7 Correctness and speed trade off

For ChatGPT Agent, mean times are:

- correct: 9:16;
- wrong: 16:14;
- uncertain: 25:55.

For Operator:

- correct: 2:59;
- wrong: 3:58;
- uncertain: 8:06.

The authors summarize the pattern as “agents succeed quickly and fail slowly” (p. 8). Proxy and Operator reportedly spend averages of 11:08 and 14:37, respectively, before looping and returning no answer (footnote 18).

## 9.8 Human efficiency depends on perceived difficulty

Humans spend an average:

- 2:14 on questions perceived as easy;
- 5:32 on medium questions;
- 10:52 on hard questions (§5.1, p. 7).

Table 5 reports 55 easy, 36 medium, and 20 hard judgments, totaling all 111 questions.

## 9.9 Simple snippet augmentation does not help

GPT-4o plus search scores 0.0%; DeepSeek R1 plus search scores 1.8%; both underperform their zero-shot variants (2.7% and 8.1%). This supports the narrower claim that the benchmark’s answers are generally absent from the supplied top-result titles and snippets under the authors’ prompt.

## 9.10 Source grounding differs markedly

From Table 9:

- ChatGPT Agent: 72 primary, 0 secondary, 1 ungrounded among 73 correct;
- Operator: 24 primary, 1 secondary, 1 ungrounded among 26;
- Anthropic Computer Use: 14 primary, 2 secondary among 16;
- Proxy: 13 primary, 1 secondary among 14;
- OpenAI Deep Research: 25 primary, 10 secondary, 5 ungrounded among 40.

Correctness alone therefore conceals source-quality differences.

# 10. Figure-by-Figure Interpretation

## Figure 1 — One question, human and agent trajectories

**Location:** p. 3.

The figure presents a question about reading exact text beneath a horizontal line in a historical document displayed through the olmOCR website’s interactive comparison tool.

It is a qualitative workflow comparison rather than an axis-based plot:

- **Human:** finds the correct document and zooms into the answer in 43 seconds.
- **ChatGPT Agent:** obtains the answer but takes 18 minutes.
- **Operator:** reaches the correct section but fails to click the necessary link.
- **Proxy:** does not fully explore the correct webpage.
- **Anthropic Computer Use:** fails to find the correct webpage.

Green boxes encode successful outcomes; red/pink boxes encode failures. The figure supports the claim that a task easy for a person can require a fragile chain of navigation and visual inspection for an agent. No error bars or statistical aggregation are involved; it is one illustrative case.

## Figure 2 — Textual workaround for a multimodal video task

**Location:** p. 4.

The question asks how many times a player takes damage in a *Phantom Blade Zero* trailer. The intended path is:

`find trailer → watch video → count health-bar reductions → answer`.

A human uses that path. Deep Research instead finds a forum comment—“Dude’s health bar didn’t drop the whole time…”—infers that “Dude” means the player, and returns “0 times.”

The diagram uses a green upper branch for the intended multimodal path and a red dashed lower branch for the textual workaround. It explains why this candidate was removed: retaining it would test indirect text retrieval rather than video understanding.

## Figure 3 — Benchmark creation and validation workflow

**Location:** p. 15.

The flow has three numbered stages:

1. **Question writing:** an author or freelancer supplies the question, viable approach, and visited links.
2. **Quality verification:** at least two authors check the approach and links, enforce clarity and unambiguity, and discard unqualified questions.
3. **Workaround prevention:** reviewers search for snippet-level answers, test whether ChatGPT can answer directly, and reject multimodal questions solvable by Deep Research through text.

The diagram’s arrows express a sequential curation pipeline. It operationalizes the criteria in Appendix B and connects directly to the reported rejection of 13 multimodal candidates.

## Figure 4 — Sources behind correct answers

**Location:** p. 20; introduced in Appendix J, p. 18.

This is a horizontal 100% stacked-bar chart. The horizontal axis runs from 0 to 100 percent. Colors represent:

- green: primary source;
- blue: secondary source;
- pink: ungrounded.

Visually labeled proportions are:

| Agent | Primary | Secondary | Ungrounded |
|---|---:|---:|---:|
| Grok 3 DeepSearch | 61.54% | 15.38% | 23.08% |
| OpenAI Deep Research | 61.54% | 25.64% | 12.82% |
| Convergence AI Proxy | 92.86% | 7.14% | 0% |
| Anthropic Computer Use | 87.5% | 12.5% | 0% |
| OpenAI Operator | 89.29% | 7.14% | 3.57% |

These percentages agree with Table 9 for Grok, Proxy, Anthropic, and Operator. For OpenAI Deep Research, however, Table 9 reports 25 primary, 10 secondary, and 5 ungrounded among 40 correct answers, which equals 62.5%, 25%, and 12.5%. The plotted 61.54/25.64/12.82 percentages correspond to a denominator of 39. The paper does not resolve this discrepancy.

ChatGPT Agent and Google Deep Research are absent from the plotted figure even though Table 9 supplies source-attribution counts for them. The supplied text does not explain the omission.

# 11. Table-by-Table Interpretation

## Table 1 — Benchmark composition

**Location:** p. 4.

It compares text and multimodal splits by question count, distinct top-level URLs, human-trajectory steps, and webpages. The dataset is almost evenly divided: 56 versus 55. Text tasks average more steps and webpages, while multimodal tasks have the larger maximum step count, 14. No variability measures accompany the means.

## Table 2 — Main human and agent results

**Location:** p. 7.

Rows group baselines, non-computer-use agents, computer-use agents, and humans. Columns report overall/text/multimodal accuracy, answer-label counts, and mean time conditional on correct, wrong, or unknown responses.

Best overall: human, 84.7%.  
Best agent: ChatGPT Agent, 65.8%.  
Worst displayed overall: GPT-4o plus Google Search, 0.0%.

The em dash means no value is provided or applicable. “Unk.” is an uncertain/no-direct answer; “None” is explicit failure/no answer or a loop. Timing is not directly comparable across all systems because baselines lack timing entries and ChatGPT Agent has a longer maximum allowance.

## Table 3 — Agent error examples

**Location:** p. 9.

Three qualitative cases demonstrate:

1. inefficient search and opaque top-level URLs;
2. abandoning the required source and giving a wrong answer from an alternative site;
3. failure to interact with a keyboard-driven game.

The table supports the discussion of transparency, source credibility, multimodal avoidance, and planning. It is illustrative, not a frequency distribution.

## Table 4 — Baseline prompt and hyperparameters

**Location:** p. 16.

GPT-4o uses 518 maximum tokens; DeepSeek R1 uses 8,000; both use temperature 0. The search prompt tells models not to use internal knowledge and to return “No answer found” unless the supplied snippets contain a clear answer. This helps explain the large “None” counts for search augmentation.

## Table 5 — Detailed human performance

**Location:** p. 16.

Humans score 83.6% text and 85.7% multimodal. They average 1.83 dead ends for text tasks and 1.22 for multimodal tasks. Mean completion time is 5:19 for text and 4:23 for multimodal. Multimodal questions also receive more “easy” ratings: 32 of 55 versus 23 of 56 text questions.

A discrepancy exists:

- Table 5 reports text outcomes as 46 correct, 9 wrong, 1 none.
- Table 9 reports 46 correct, 8 wrong, 1 none for humans on text tasks, totaling only 55 rather than 56.

Table 2 agrees with the overall total of 14 wrong but does not expose the split counts. Table 5 is internally consistent; Table 9 appears to omit one text error, but the paper does not explicitly correct it.

## Table 6 — Human error examples

**Location:** p. 17.

The table shows three cases:

- a Wingspan question involving missing details, topic knowledge, and source selection;
- an overlooked answer on a magazine page;
- abandonment of a map-marker calculation task.

The caption reports 14 incorrect and 3 abandoned questions. It says errors were primarily due to five reasons; nearby prose says “six key causes.” Only the displayed combined labels can be verified.

## Table 7 — Automatic evaluator prompt

**Location:** p. 18.

It defines four labels and emphasizes strict semantic equivalence: near numbers are not equivalent, rejected premises are wrong, and hedged answers are “no direct answer.” It contains two displayed examples; examples 3–17 are omitted. Consequently, the complete evaluator cannot be reconstructed from the paper alone.

## Table 8 — Evaluator agreement

**Location:** p. 19.

Four-way accuracy is:

- Grok: 99.1%;
- OpenAI Deep Research: 96.4%;
- Anthropic: 99.1%;
- Proxy: 99.1%;
- Operator: 97.3%.

Binary accuracy is 99.1%, 96.4%, 100%, 100%, and 98.2%, respectively. OpenAI Deep Research is lowest in both settings. No confidence intervals or error-type breakdowns are supplied.

## Table 9 — Detailed performance and source attribution

**Location:** p. 19.

This expands Table 2 into overall, text, and multimodal blocks and adds source categories. It contains nearly all per-system aggregate results.

Notable points not fully visible in the main prose include:

- Google Deep Research returns 46 uncertain answers overall.
- Anthropic Computer Use returns 73 uncertain answers but zero “None.”
- Operator returns 29 “None” outcomes, including 19 on multimodal questions.
- ChatGPT Agent returns 72 of its 73 correct answers from primary sources.
- Deep Research has 15 non-primary correct answers according to the counts.

The repeated `%%` after ChatGPT Agent’s percentages is a visible typesetting error; it should not be interpreted as a different unit. The multimodal ChatGPT “uncertain” time appears in extracted text as `16.58`; the rendered table appears to intend a time value, likely `16:58`, but this is OCR/typesetting-sensitive and should be treated as uncertain.

## Table 10 — DeepSeek R1 run-to-run stability

**Location:** p. 20.

It reports four runs in two settings. Performance is consistently low, with standard deviations of 0.8 and 0.7 percentage points. This supports repeatability of these particular low scores but does not by itself validate all benchmark rankings.

# 12. Diagram / Architecture Interpretation

The paper contains no software architecture diagram. Its substantive diagrams are process diagrams:

- **Figure 1:** parallel human/agent routes from the same question to success or distinct failure points.
- **Figure 2:** a branch between the intended multimodal solution and an unintended text-based shortcut.
- **Figure 3:** a sequential creation pipeline from drafting through quality verification to shortcut prevention.

Collectively, they show that BEARCUBS treats the **path to the answer** as important, not just the final string. A correct answer can still reveal benchmark failure if it was obtained through a shortcut, and an incorrect answer can be diagnosed through the exact stage at which navigation failed.

# 13. Equations and Mathematical Concepts

No numbered equations, optimization objectives, theorems, or formal algorithms are present.

The principal quantitative definition is accuracy:

\[
\text{Accuracy}=\frac{\text{number of correct answers}}{\text{number of benchmark questions}}\times100\%.
\]

This formula is not explicitly printed but is directly recoverable from the tables. For example:

\[
\frac{73}{111}\times100\%=65.77\%\approx65.8\%
\]

for ChatGPT Agent.

Other relevant concepts are:

- **Percentage-point difference:** subtraction of two percentages. ChatGPT Agent versus Operator is \(65.8-23.4=42.4\) points.
- **Standard deviation across runs:** Table 10’s measure of run-to-run score dispersion. The paper provides the values but not the exact sample-versus-population convention.
- **Conditional mean time:** timing columns in Tables 2 and 9 are means within response categories, not a single unconditional runtime average.
- **Four-way versus binary classification:** Table 8 collapses correct/incorrect-style outcomes into a two-class judgment, but the exact label mapping beyond “correct versus incorrect” is described only generally.

# 14. Interpretation and Discussion

## Answers to the research questions

**RQ1: How well do computer-using agents perform on real-world browsing?**  
The strongest tested system reaches 65.8%, but other computer-use agents score 12.6%–23.4%. Performance is especially weak on multimodal tasks. The evidence therefore supports the authors’ conclusion that substantial progress has occurred without reaching human reliability.

**RQ2: How well do humans perform?**  
Humans achieve 84.7%, with 1.5 dead ends and 4:46 mean completion time. They find multimodal questions slightly easier and solve them more accurately than text questions, suggesting that benchmark difficulty is not simply intrinsic question difficulty; it depends strongly on whether the solver can manipulate the interface effectively.

## Meaning of the findings

The study separates several capabilities often conflated under “web browsing”:

1. locating the correct page;
2. navigating the interface;
3. interpreting text or media;
4. applying precise filters or controls;
5. selecting credible sources;
6. returning a direct answer;
7. doing so efficiently;
8. exposing a useful trajectory.

ChatGPT Agent’s strong improvement does not eliminate bottlenecks. Its failures cluster around complex filtering, fine control, access restrictions, and long execution. Earlier computer-use agents sometimes fail even when text-only Deep Research can guess the answer.

## Relationship to prior work

The authors position BEARCUBS between realistic web benchmarks and multimodal computer-use benchmarks. They distinguish it through live-web content, diverse modalities, and deliberate removal of text-only shortcuts. They describe AssistantBench as closest in realism but less focused on video and other multimodal interactions (§7, p. 10).

## Internal inconsistencies and unresolved points

- Deep Research non-primary sourcing is reported as 37.5% in §5.2, 38.5% in §6, 37.5% from Table 9 counts, and approximately 38.46% in Figure 4.
- Table 5 reports nine wrong text answers for humans; Table 9 reports eight, leaving one question unaccounted for in that block.
- The human prose reports 4:46 overall task time, while Table 2’s 4:24 and 5:44 are conditional means for correct and wrong responses, respectively. These are compatible but easy to confuse.
- The paper describes Table 6 as listing six causes in one place and five key reasons in its caption.
- “Significantly outperforms” is used without a reported inferential test.
- Figure 4 omits ChatGPT Agent and Google Deep Research despite Table 9 containing their attribution data.

# 15. Contributions and Novelty

## Dataset and benchmark contribution

- A 111-question live-web benchmark split nearly evenly between text and multimodal tasks.
- Human-validated answers, routes, and website lists.
- Coverage of 108 distinct top-level URLs and varied interaction types.

## Methodological contribution

- Explicit filtering of multimodal tasks for text-only workarounds.
- Question criteria designed for concise, objective grading.
- A proposal for periodic replacement of contaminated or invalid items.

## Experimental contribution

- Side-by-side evaluation of humans, language-model baselines, research agents, and computer-use agents.
- Modality-specific performance and timing.
- Qualitative trajectory and error analysis.
- Source-credibility categorization.

## Implementation contribution

- A GPT-4o automatic answer evaluator with reported 96.4%–99.1% four-way agreement across five agents.
- Publicly referenced dataset, leaderboard, prompt, and evaluator code, although these artifacts were not supplied here.

## Empirical contribution

- Evidence of a sizeable human–agent gap.
- Evidence that simple search snippets do not solve the retained questions.
- Evidence that humans find many multimodal tasks easier than agents do.
- Evidence that correct answers differ in source quality and grounding.

# 16. Limitations

## Authors’ stated limitations

Appendix A identifies three principal limitations:

1. **Restricted answer format.** Every question has one short answer, unlike realistic questions that may have no answer, multiple answers, or long-form responses.
2. **Limited multilingual scope.** The benchmark contains multilingual questions, but its small size does not support systematic cultural or cross-language evaluation.
3. **Non-comparable trajectory detail.** Agents expose action traces at inconsistent levels of granularity, complicating direct behavioral comparison.

Elsewhere, the authors also acknowledge:

- public release cannot fully prevent contamination (footnote 2, p. 2);
- live-web validity requires continuing maintenance;
- manual evaluation is slow and expensive;
- the dataset is small;
- agents’ missing APIs impede scalable and reproducible evaluation;
- brief or obscured trajectories may reflect provider anti-distillation choices (footnote 20, p. 9).

## Additional evidence-based analyst observations

These are not presented as author admissions:

- ChatGPT Agent receives three times the nominal time allowance of other computer-use agents, complicating direct capability comparisons.
- Commercial systems were evaluated in different months, so model and website states may differ.
- The number of human participants and assignment structure are unspecified.
- There is no participant-level uncertainty analysis or adjustment for repeated measures.
- No formal uncertainty intervals accompany accuracy differences.
- The benchmark’s 55-question multimodal subset yields coarse percentage resolution.
- Website changes could alter difficulty even without answer contamination.
- Hardware, browser, network, and display conditions are not documented.
- Some qualitative claims—such as “guessing” or avoiding interactions—depend on human trajectory interpretation without a reported annotation protocol or inter-rater agreement.
- The automatic evaluator is validated on outputs from five agents only and uses an incompletely disclosed prompt in the paper.
- Source categories combine “reliable” and “question-specified” into primary, and “unreliable” and “not specified” into secondary; these are conceptually different properties.
- Aggregate accuracy treats every question equally despite substantial differences in interaction type and runtime.

# 17. Threats to Validity

## Internal validity

Different evaluation dates, agent time limits, interfaces, and trajectory formats may affect observed differences. Manual operation can introduce operator variability. The authors’ one-time intervention prompt may affect products differently.

## Construct validity

A single exact answer makes grading clear but represents only one portion of useful web-agent behavior. Accuracy does not fully measure source quality, calibration, robustness, efficiency, or quality of explanation. Conversely, labeling a multimodal answer as a “guess” from trajectory review depends on how completely the provider exposes its process.

## Statistical conclusion validity

Results are primarily descriptive. No uncertainty intervals or hypothesis tests establish whether close differences—such as 12.6% versus 14.4%—are stable. The strongest differences are large, but the paper’s use of “significantly” is not backed by a reported statistical procedure.

## External validity

The benchmark spans many websites but only 111 questions. Findings may not generalize to transactional work, long-form research, private/authenticated sites, questions with multiple answers, or later agent versions.

## Ecological validity

Use of live websites improves realism. However, the strict no-help protocol, source-specified questions, concise-answer format, and termination rules differ from many real human–agent collaborations.

## Reproducibility

The public dataset and code are referenced, but not supplied here. Reproducing the exact study would additionally require historical commercial model versions, website states, browser conditions, prompts, trajectories, and screen recordings. Some providers do not expose standardized APIs or logs.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Periodically replace invalid or contaminated questions.
- Add new examples to keep the benchmark current.
- Improve release and standardization of structured trajectories.
- Evaluate source credibility more thoroughly.
- Improve fine mouse/keyboard control and multimodal interaction.
- Develop strategies for restricted-content access.
- Build more structured planning mechanisms to reduce repetition.
- Combine computer-use capabilities with stronger search/reasoning agents.
- Study performance systematically across languages and cultures.
- Expand to questions with absent, multiple, or long-form answers.
- Improve transparency so trajectories can be compared meaningfully.

## B. Additional open questions

- How much of ChatGPT Agent’s advantage remains under the same 15-minute limit?
- How stable are rankings across repeated runs of all agents?
- Which modalities—video, audio, 3D navigation, games, scanned documents—account for most failures?
- How should source reliability be separated from compliance with a question’s requested source?
- Can benchmark maintenance be audited without making answers searchable?
- What trajectory representation is both transparent and resistant to proprietary-information leakage?
- How should partial progress or a well-calibrated abstention be rewarded?
- How much performance variation comes from changing websites rather than changing agents?
- Would participant-level modeling change the human baseline?
- Does the evaluator generalize to new answer styles and later agents?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| BEARCUBS | Benchmark for Agents with Real-world Computer Use and Browsing Skills. |
| LLM | Large language model; a model trained to process and produce language. |
| Web agent | A system that searches, browses, reasons, and returns information from websites. |
| Computer-use agent | A web agent that can perceive the displayed interface and issue mouse/keyboard actions. |
| Live web | Public websites in their current, changing state rather than a frozen simulation. |
| QA pair | A question and its gold answer. |
| Gold answer | The benchmark’s verified correct answer. |
| Trajectory | The sequence of searches, pages, clicks, and other actions used to solve a task. |
| Viable trajectory | A human-validated route known to reach the answer. |
| Text-based task | A task solvable through textual reading and navigation. |
| Multimodal task | A task requiring non-text information or interaction, such as video, audio, images, games, or 3D tours. |
| Workaround | An unintended shortcut that avoids the skill the task was designed to test. |
| Contamination | Benchmark information leaking into training data or searchable web content. |
| Zero-shot | Answering without task-specific examples or retrieved context. |
| Search augmentation | Adding search-result titles and snippets to a model’s input. |
| Parametric knowledge | Information stored in a model’s learned parameters rather than retrieved during the task. |
| CAPTCHA | A challenge intended to distinguish human users from automated systems. |
| Dead end | A path that requires backtracking or restarting. |
| Abstention | Declining to give a definite answer. |
| Primary source | Here, a reliable source or the specific source requested in the question. |
| Secondary source | Here, an unreliable source or one not requested in the question. |
| Ungrounded | Unsupported by an identified external source. |
| Percentage point | The arithmetic difference between two percentages. |
| Standard deviation | A measure of variation across repeated results. |
| Serper | The search-results API used in the paper’s Google-search augmentation. |
| Unk./Uncertain | The agent gives no definite, concrete answer. |
| None | The baseline says no answer was found, or the agent loops/stalls without answering. |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Total benchmark size | 111 | questions | Entire dataset | Author-reported | p. 4, Table 1 |
| Text split | 56 | questions | Text-based | Author-reported | p. 4, Table 1 |
| Multimodal split | 55 | questions | Multimodal | Author-reported | p. 4, Table 1 |
| Distinct top-level URLs | 108 | URLs | Human trajectories; Google excluded | Author-reported | pp. 4–5, Table 1 |
| Mean trajectory length | 6.1 | steps/question | All questions | Author-reported | p. 4, Table 1 |
| Mean webpages visited | 3.4 | webpages/question | All questions | Author-reported | p. 4, Table 1 |
| Author-written questions | 65 | QA pairs | Dataset construction | Author-reported | p. 4, §3 |
| Accepted freelancer questions | 46 | QA pairs | \(111-65\) | Analyst-derived | p. 4, §3 |
| Freelancer acceptance rate | 58.2 | % | Submitted candidate questions | Author-reported | p. 3, §2 |
| Removed workaround questions | 13 | questions | Mostly found by Deep Research | Author-reported | p. 3, §2 |
| Human accuracy | 84.7 | % | All questions | Author-reported | p. 7, Table 2 |
| Human text accuracy | 83.6 | % | Text split | Author-reported | p. 16, Table 5 |
| Human multimodal accuracy | 85.7 | % | Multimodal split | Author-reported | p. 16, Table 5 |
| Human mean time | 4:46 | min:sec | All questions | Author-reported | p. 16, Table 5 |
| Human mean dead ends | 1.50 | dead ends/question | All questions | Author-reported | p. 16, Table 5 |
| ChatGPT Agent accuracy | 65.8 | % | All questions | Author-reported | p. 7, Table 2 |
| ChatGPT Agent text accuracy | 76.8 | % | Text split | Author-reported | p. 7, Table 2 |
| ChatGPT Agent multimodal accuracy | 54.5 | % | Multimodal split | Author-reported | p. 7, Table 2 |
| Operator accuracy | 23.4 | % | All questions | Author-reported | p. 7, Table 2 |
| OpenAI Deep Research accuracy | 36.0 | % | All questions | Author-reported | p. 7, Table 2 |
| Google Deep Research accuracy | 23.4 | % | All questions | Author-reported | p. 7, Table 2 |
| Human–ChatGPT Agent gap | 18.9 | percentage points | \(84.7-65.8\) | Analyst-derived | p. 7, Table 2 |
| ChatGPT Agent–Operator gap | 42.4 | percentage points | Overall | Author-reported and arithmetically reproducible | p. 6, §5; Table 2 |
| ChatGPT Agent modality gap | 22.3 | percentage points | \(76.8-54.5\) | Analyst-derived | p. 7, Table 2 |
| DeepSeek R1 zero-shot | 8.1 | % | Overall | Author-reported | p. 7, Table 2 |
| Best listed search-augmented baseline | 5.4 | % | Perplexity sonar-pro | Author-reported | p. 7, Table 2 |
| ChatGPT correct-answer mean time | 9:16 | min:sec | All correct responses | Author-reported | p. 7, Table 2 |
| ChatGPT multimodal correct time | 13:15 | min:sec | Correct multimodal responses | Author-reported | p. 19, Table 9 |
| Standard agent time limit | 15 | minutes | Computer-use agents except ChatGPT | Author-reported | p. 3, footnote 3 |
| ChatGPT Agent time limit | 45 | minutes | ChatGPT Agent | Author-reported | p. 3, footnote 3 |
| Automatic evaluator four-way range | 96.4–99.1 | % accuracy | Five evaluated agents | Author-reported | p. 19, Table 8 |
| Automatic evaluator binary range | 96.4–100 | % accuracy | Five evaluated agents | Author-reported | p. 19, Table 8 |
| Evaluator runtime | ~1:30 | min:sec | 111 answers | Author-reported | p. 16, Appendix G |
| Evaluator cost | ~$0.80 | USD | 111 answers | Author-reported | p. 16, Appendix G |
| DeepSeek no-Serper variability | 0.8 | percentage-point SD | Four runs | Author-reported | p. 20, Table 10 |
| DeepSeek with-Serper variability | 0.7 | percentage-point SD | Four runs | Author-reported | p. 20, Table 10 |
| Deep Research non-primary correct answers | 15/40 = 37.5 | % | Table 9 counts | Analyst-derived | p. 19, Table 9 |
| Deep Research non-primary proportion | 38.46 | % | Figure labels sum | Visually readable | p. 20, Figure 4 |
| Paid annotator compensation | $2.50 + $1 correct bonus | USD/question | Human study | Author-reported | p. 15, Appendix C |
| Freelancer compensation | $4 | USD/accepted question | Dataset writing | Author-reported | p. 4, footnote 4 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Current agents remain below humans | Human 84.7%; best agent 65.8% | X1/X4, Table 2 | pp. 6–7 | Strong descriptive evidence on this benchmark; no confidence intervals. |
| ChatGPT Agent is the strongest tested computer-use agent | 65.8% versus 23.4%, 14.4%, and 12.6% | X4, Tables 2 and 9 | pp. 7, 19 | Strong within tested systems; unequal time limits and different evaluation dates qualify comparison. |
| Multimodal interaction is a major bottleneck | Best agent 54.5% versus human 85.7%; all agents decline relative to text | X1–X4, Table 2 | pp. 7–8 | Strong aggregate evidence; modality subtypes are not separately quantified. |
| Humans find multimodal questions comparatively manageable | 85.7% accuracy, 4:23 mean time, 1.22 dead ends, 32 easy ratings | X1, Table 5 | p. 16 | Strong descriptive evidence; participant design details are missing. |
| Search snippets do not make BEARCUBS easy | Search-augmented scores 0.0%, 1.8%, and 5.4% | X2, Table 2 | p. 7 | Supports resistance to the tested search setup, not every possible search method. |
| Text-only workarounds threaten multimodal validity | 13 questions removed; Figure 2 gives a concrete case | X2/construction, Figure 2 | pp. 3–4 | Direct construction evidence; full rejected set is not supplied. |
| Correctness alone hides source quality | Deep Research has 10 secondary and 5 ungrounded correct answers | X7, Table 9/Figure 4 | pp. 19–20 | Strong in principle; exact percentage conflicts across text, table, and figure. |
| Agents often fail slowly | Longer mean times for wrong/uncertain than correct outcomes | X3/X4, Tables 2 and 9 | pp. 7–8 | Descriptive association, not causal proof. |
| Agent trajectories need standardization | Step reports vary from granular to brief/obscured | X6, Table 3 | pp. 8–9 | Qualitative evidence; step definitions differ between agents. |
| The small benchmark gives stable DeepSeek scores | Four-run SDs of 0.8 and 0.7 points | X9, Table 10 | p. 20 | Limited to one model family and low-accuracy conditions. |
| Automatic grading can approximate manual labels | 96.4%–99.1% four-way agreement | X8, Table 8 | p. 19 | High reported accuracy; incomplete prompt and no classwise evaluation. |
| Planning failures impede agents | Repeated failed actions and irrelevant navigation in trajectories | X6, Table 3 | pp. 9–10 | Qualitative, evidence-based author interpretation; frequency not quantified. |

# 22. Very Simple Explanation

Imagine giving a person and several AI assistants the same web scavenger hunt. Some clues are in ordinary text, but others require watching a video, moving through a virtual building, playing a small web game, reading a scanned book, or adjusting controls in a database. The answer is always short, but getting to it may require several careful actions.

People answered about 85 out of every 100 questions correctly. The best AI, ChatGPT Agent, answered about 66 out of 100 correctly. That is much better than the other tested computer-control agents, but it still missed many tasks—especially ones needing precise interaction with videos, games, menus, maps, and databases.

The paper also shows why checking only the final answer is insufficient. An AI may guess correctly, use an unreliable webpage, avoid the requested source, or waste time repeating failed actions. BEARCUBS therefore records not just the answer but also a known human route, making it possible to inspect how an agent searched.

The main lesson is that modern agents have improved dramatically, but reliable web use requires more than language ability. They need better mouse and keyboard control, better planning, trustworthy sourcing, clearer records of what they did, and stronger handling of non-text information.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue | Yes | Yes | Fully represented | *BEARCUBS*, Song et al., COLM 2025; metadata visible on p. 1. |
| Abstract | Yes | Yes | Fully represented | Core problem, method, and headline results incorporated. |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, and contributions covered. |
| §2 Evaluation challenges | Yes | Yes | Fully represented | Contamination, workarounds, diversity, and slow evaluation covered. |
| §3 Benchmark construction | Yes | Yes | Fully represented | Criteria, collection, validation, and statistics covered. |
| §4 Experiments | Yes | Yes | Fully represented | Human and agent protocols covered. |
| §4.1 Human evaluation | Yes | Yes | Fully represented | Tasks, recruitment pointers, measures, and time limit covered. |
| §4.2 Agent benchmarking | Yes | Yes | Fully represented | Agents, baselines, prompts, scoring, and dates covered. |
| §5 Results | Yes | Yes | Fully represented | Principal numeric and qualitative findings covered. |
| §5.1 Human analysis | Yes | Yes | Fully represented | Accuracy, timing, difficulty, dead ends, and errors covered. |
| §5.2 Agent analysis | Yes | Yes | Fully represented | Model comparisons, modality gap, time, and sourcing covered. |
| §6 Discussion | Yes | Yes | Fully represented | Transparency, credibility, multimodality, planning covered. |
| §7 Related work | Yes | Yes | Represented in compressed form | Categories and claimed positioning retained; individual citations not enumerated. |
| §8 Conclusion | Yes | Yes | Fully represented | Its substantive claims are integrated into synthesis. |
| Acknowledgments | Yes, text only | No substantive analysis | Inspected but deliberately omitted as non-substantive | Funding and acknowledgments do not change methods or findings. |
| References | Yes, text only | Compressed | Inspected but deliberately compressed | Related-work categories represented; full bibliography not reproduced. |
| Appendix A | Yes | Yes | Fully represented | All three stated limitations covered. |
| Appendix B | Yes, visually | Yes | Fully represented | All criteria and workflow covered. |
| Appendix C | Yes, visually | Yes | Fully represented | Recruitment and compensation covered. |
| Appendix D | Yes, visually | Yes | Fully represented | Prompt and hyperparameters covered. |
| Appendix E | Yes, visually | Yes | Fully represented | All Table 5 statistics relevant to conclusions covered. |
| Appendix F | Yes, visually | Yes | Fully represented with uncertainty | Three visible examples covered; cause-count inconsistency flagged. |
| Appendix G | Yes, visually | Yes | Fully represented | Evaluator design and validation covered. |
| Appendix H | Yes, visually | Yes | Fully represented | Detailed result groups covered through Table 9. |
| Appendix I | Yes, visually | Yes | Fully represented | Size rationale and stability experiment covered. |
| Appendix J | Yes, visually | Yes | Fully represented | Figure 4 and source-count discrepancy covered. |
| Appendix K | Yes, visually | Yes | Fully represented | Grok and Computer Use behaviors covered. |
| RQ1 | Yes | Yes | Fully represented | Answered explicitly. |
| RQ2 | Yes | Yes | Fully represented | Answered explicitly. |
| Formal hypotheses | Yes | Yes | Not present | Informal expectations distinguished from formal hypotheses. |
| X1 Human study | Yes | Yes | Fully represented | Setup, results, and caveats covered. |
| X2 Baseline evaluation | Yes | Yes | Fully represented | Five settings covered. |
| X3 Non-computer agents | Yes | Yes | Fully represented | Three systems covered. |
| X4 Computer-use agents | Yes | Yes | Fully represented | Four systems covered. |
| X5 Human error analysis | Yes | Yes | Fully represented with uncertainty | Visible examples and inconsistent category count noted. |
| X6 Trajectory analysis | Yes | Yes | Fully represented | Transparency and failure patterns covered. |
| X7 Source analysis | Yes | Yes | Fully represented with discrepancy | Text/table/figure mismatch preserved. |
| X8 Evaluator validation | Yes | Yes | Fully represented | Table 8 results and missing diagnostics covered. |
| X9 Stability analysis | Yes | Yes | Fully represented | All Table 10 values covered. |
| X10 Agent-specific analysis | Yes | Yes | Fully represented | Appendix K covered. |
| Figure 1 | Yes, visually | Yes | Fully represented | Contents and success/failure paths explained. |
| Figure 2 | Yes, visually | Yes | Fully represented | Intended and shortcut paths explained. |
| Figure 3 | Yes, visually | Yes | Fully represented | Three-stage workflow explained. |
| Figure 4 | Yes, visually | Yes | Fully represented with discrepancy | All displayed percentages transcribed and checked against Table 9. |
| Table 1 | Yes | Yes | Fully represented | All aggregate values covered. |
| Table 2 | Yes | Yes | Fully represented | Main values and labels covered. |
| Table 3 | Yes | Yes | Fully represented | All three examples covered. |
| Table 4 | Yes | Yes | Fully represented | Models, token limits, temperature, and prompt covered. |
| Table 5 | Yes | Yes | Fully represented | Results and Table 9 conflict covered. |
| Table 6 | Yes | Yes | Fully represented with uncertainty | All visible rows covered. |
| Table 7 | Yes | Yes | Represented in compressed form | Rules and visible examples represented; full prompt absent from paper. |
| Table 8 | Yes | Yes | Fully represented | All accuracy values covered. |
| Table 9 | Yes | Yes | Represented in compressed form | All major results and unusual counts covered; not every cell repeated. |
| Table 10 | Yes | Yes | Fully represented | Every value covered. |
| Major equations | Yes | Yes | Not present | Only derived accuracy/difference expressions added and labeled. |
| Algorithms/pseudocode | Yes | Yes | Not present | Figure 3 is treated as a workflow. |
| Major contributions | Yes | Yes | Fully represented | Dataset, method, implementation, and empirical contributions separated. |
| Author-stated limitations | Yes | Yes | Fully represented | Appendix A and related admissions covered. |
| Footnotes 1–21 | Yes | Yes | Represented in compressed form | Substantive details—name, release, limits, payments, dates, prompts, evaluator, timing, and trajectory counting—integrated. |
| Supplementary material | No | Yes as missing | Missing from supplied material | Project website artifacts were referenced but not supplied. |

## Missing or inaccessible material

- The project website, downloadable dataset, leaderboard, and evaluator code were not supplied.
- The complete 17-example automatic-evaluator prompt was not printed; only examples 1–2 were supplied.
- Individual questions, gold answers, complete viable trajectories, agent trajectories, screen recordings, and per-question predictions were not supplied.
- Pages 5 and 11–14 were not visually rendered. Their supplied native text was readable; no substantive figure or table on those pages was indicated except prose and references.
- Exact historical website states and commercial-agent versions cannot be recovered from the paper alone.
- The paper does not supply the number of distinct human participants.

## Uncertain interpretations

- Deep Research’s non-primary-source share conflicts across §5.2, §6, Figure 4, and Table 9.
- The human text-error count differs between Tables 5 and 9.
- Table 6 is described as containing either five or six error causes; only the displayed categories can be verified.
- ChatGPT Agent’s multimodal uncertain-response time in Table 9 is rendered/extracted ambiguously as `16.58`, likely a time separator issue.
- The exact convention used for Table 10’s standard deviations is unspecified.
- “Significantly” is used without a reported statistical test.
- Figure 4 omits two agents that have attribution counts in Table 9, without explanation.

## Deliberately compressed material

- The full reference list was not reproduced; only its conceptual role in §7 was summarized.
- Table 9 contains many cells. All principal comparisons, answer distributions, source-attribution counts, and anomalies were analyzed, but routine duplicate values already present in Table 2 were not repeated cell by cell.
- Acknowledgments and decorative page headers were inspected but omitted because they do not affect the scientific argument.
- Repetitions of the same headline accuracies across the abstract, introduction, results, conclusion, and tables were consolidated.

## Potential omissions

No known substantive section, experiment, figure, table, appendix, contribution, or author-stated limitation from the supplied inventory is unrepresented. The remaining omissions are either explicitly identified missing artifacts, bibliographic repetition, acknowledgments, or individual cells compressed from Table 9.