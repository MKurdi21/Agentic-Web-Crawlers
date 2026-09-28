# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible page range | pp. 1–24 |
| Apparently missing pages | None |
| Native/extracted text | Available for all pages; p. 24 contains little text because it is primarily the end of Figure 8 |
| Pages visually supplied | pp. 1–10, 18–22, and 24 |
| Pages not visually supplied | pp. 11–17 and 23 |
| Figures visually inspected | Figures 1–7 in full; Figure 8 on pp. 21–22 and 24, but its intervening p. 23 was available only as extracted text |
| Tables visually inspected | Tables 1–4 |
| Equations | Equations (1)–(5) are readable in extracted text; Equations (2)–(4) contain layout- and OCR-sensitive subscripts, indices, and normalization terms |
| Appendices | Appendices A–F are present on pp. 17–24 |
| Supplementary material | No separate supplementary file supplied |
| Referenced but absent artifacts | The GitHub repository, external datasets, model/system cards, benchmark sources, Qwen-Agent implementation, and cited papers were referenced but not supplied as independent artifacts |
| OCR required | Partially. Extracted text was needed for the non-rendered pages and for some small visual labels |
| Main limitations of inspection | References on pp. 12–16 were text-only; Appendix A–B on p. 17 was text-only; the middle of Figure 8 on p. 23 was text-only. Fine-grained plotted values in Figures 3–5 are not all explicitly labeled and therefore cannot all be reported exactly. |

The analysis below remains in closed-document mode. Labels are used as follows: **[A]** author-reported, **[B]** directly observable, **[C]** analyst-derived, and **[D]** analyst interpretation. No external information is introduced.

# 1. Plain-Language Orientation

WebDancer is a recipe for training an open-source language model to behave like an autonomous web researcher. Instead of answering solely from what it memorized, the model repeatedly:

1. reasons about what it needs;
2. issues a web-search or page-visit action;
3. reads the resulting observation;
4. revises its plan; and
5. eventually returns an answer.

The paper addresses two linked problems. First, difficult web-research questions are scarce as training data. Second, directly training a model with reinforcement learning (RL) can be inefficient because the model must simultaneously learn tool syntax, multi-step behavior, and which decisions produce correct answers.

The authors’ solution has four stages [A, pp. 1–2]:

1. synthesize difficult question–answer pairs;
2. sample and filter complete reasoning/tool-use trajectories;
3. use supervised fine-tuning (SFT) as a behavioral “cold start”;
4. apply on-policy RL using DAPO—Decoupled Clip and Dynamic Sampling Policy Optimization.

Two synthetic datasets support the pipeline:

- **CRAWLQA:** questions generated from information gathered by recursively browsing websites.
- **E2HQA:** initially easy questions rewritten into progressively harder multi-hop questions without changing their answers.

The strongest reported WebDancer configuration, built on QwQ-32B, reaches **51.5 on GAIA Pass@1** and **47.9 on WebWalkerQA Pass@1** [A, Table 1, p. 7]. It improves substantially over the corresponding vanilla ReAct agent—by **13.7 percentage points on GAIA** and **23.8 points on WebWalkerQA** [C: 51.5−37.8 and 47.9−24.1]. OpenAI Deep Research remains substantially stronger on GAIA at 67.4, but no WebWalkerQA result is supplied [A, Table 1].

The central contribution is therefore not a new web tool or a single isolated RL algorithm. It is an end-to-end, data-to-training pipeline showing how synthetic questions, filtered demonstrations, SFT, and on-policy RL can be assembled into a native ReAct web agent [A, pp. 2, 5–7, 18].

# 2. Document Roadmap

The paper is a mixed **machine-learning/AI systems and empirical study**:

| Document part | Role |
|---|---|
| Abstract and §1, pp. 1–2 | Motivation, gap, four-stage contribution |
| §2, pp. 3–5 | CRAWLQA/E2HQA construction and trajectory rejection sampling |
| §3, pp. 5–7 | SFT and DAPO-based RL objectives |
| §4, pp. 7–8 | Main benchmark setup and results |
| §5, pp. 8–10 | Data, SFT/RL, reasoning-transfer, and stability analyses |
| §6–7, pp. 10–11 | Related work and conclusion |
| References, pp. 12–16 | Cited literature |
| Appendix A, p. 17 | Author-stated limitations |
| Appendix B, p. 17 | Broader impacts |
| Appendix C, pp. 17–18 | Concurrent-work comparisons and post-trained agentic models |
| Appendix D, pp. 18–19 | Training-data counts, filtering, and open-only datasets |
| Appendix E, pp. 19–21 | Benchmarks, baselines, implementation, prompts |
| Appendix F, pp. 21–24 | Qualitative case study |

Inventory of substantive objects:

- **Figures:** F1 data generation; F2 training framework; F3 data efficiency; F4 SFT-versus-RL metrics; F5a–c training/stability analyses; F6 LLM prompt; F7 LRM prompt; F8 case trajectory.
- **Tables:** T1 main benchmarks; T2 BrowseComp; T3 chain-of-thought transfer; T4 training-data statistics.
- **Major equations:** E1 trajectory history; E2 masked SFT loss; E3 DAPO objective and sampling constraint; E4 importance ratio and group-normalized advantage; E5 reward.
- **Algorithms/pseudocode:** No separately numbered algorithm. Procedural algorithms are described in prose and diagrams.
- **Explicit hypotheses/research questions:** None formally enumerated.
- **Experiments/analyses:** main benchmarks, BrowseComp, data ablation, SFT/RL comparison, training-step analysis, chain-of-thought transfer, emergent behavior, decoding temperature, and memorization stress test.

# 3. Background and Context

A **large language model (LLM)** generates text token by token. A **large reasoning model (LRM)** is the paper’s term for a model oriented toward extended intermediate reasoning.

A conventional model may answer from internal knowledge. A **web agent** can also call tools. Here, the main tools are:

- `search`: receives a query and optional year filter, then returns the top ten titles and snippets;
- `visit`: receives a goal and URL, then returns evidence and a model-generated summary;
- `answer`: terminates the trajectory with a final answer [A, §2.2, p. 4].

**ReAct** means interleaving reasoning and acting. Each round has a **Thought**, **Action**, and **Observation**. The observation is external feedback, not text independently produced by the policy model.

**Chain of thought (CoT)** is the model’s intermediate reasoning. The paper distinguishes:

- **Short-CoT**, sampled with GPT-4o;
- **Long-CoT**, sampled with QwQ-Plus, an LRM [A, §2.2, p. 4].

**Supervised fine-tuning (SFT)** trains the policy to imitate accepted trajectories. It supplies a cold start: the model first learns the structure of alternating reasoning and tool use.

**Reinforcement learning (RL)** subsequently improves the policy using rewards for outcomes. WebDancer uses **DAPO**, an on-policy optimization method that compares newly sampled behavior with an older policy while clipping excessively large updates [A, §3.2, pp. 6–7].

Key evaluation concepts:

- **Pass@1:** success using one attempt.
- **Pass@3:** success within three attempts.
- **Cons@3:** the fraction of three attempts that are correct: 1/3, 2/3, or 1 [A, §5, p. 8].
- **LLM-as-Judge:** a language model evaluates whether the output is correct, rather than exact string matching.

# 4. Research Problem and Gap

## Existing problem

Difficult real-world questions may require long sequences of searching, visiting, comparing, and revising. A useful agent must perceive a changing web environment, choose actions, decompose goals, and continue until enough evidence is gathered [A, pp. 1–2].

## Shortcomings attributed to prior approaches

The authors divide earlier approaches into two broad categories [A, §1, pp. 1–2]:

- prompting an LLM/LRM without agent-specific training;
- incorporating search or browsing through SFT or RL.

They argue that prompting alone does not fully exploit reasoning models’ capabilities. Existing training approaches allegedly use relatively simple data, learn tool following inefficiently, or generalize poorly to complex web environments. Frequently used training questions may be solvable in only a few searches, while hard evaluation sets are small: the paper cites 466 GAIA items, 680 WebWalkerQA items, and 1,266 BrowseComp items [A, p. 2].

## Research gap

The missing capability is a scalable route from realistic training-question construction through trajectory generation to stable post-training of multi-turn, multi-tool agents [A, pp. 1–2].

## Motivation

The stated goal is to “unlock” autonomous multi-turn information seeking and provide a systematic recipe for constructing a Deep-Research-like agent from scratch [A, p. 2].

## Scope

The implemented agent is limited to short-answer web information seeking and two fundamental retrieval operations. It is not evaluated on long-form research reports, arbitrary browser manipulation, code execution, or broad API interaction [A, Appendix A, p. 17].

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

No questions are formally labeled as research questions.

## Author-stated objectives

The paper seeks to [A, pp. 1–2]:

1. construct diverse, deep information-seeking questions at scale;
2. sample reliable short- and long-reasoning trajectories;
3. teach models the ReAct interaction format through SFT;
4. improve decision-making and generalization through on-policy RL;
5. evaluate the resulting agent on deep web-retrieval benchmarks;
6. derive practical lessons about data quality, reasoning transfer, RL, and environmental instability.

## Hypotheses

No formal statistical hypotheses or null hypotheses are supplied. The experiments implicitly examine whether:

- synthetic and filtered trajectories improve SFT;
- SFT is necessary before RL;
- RL improves success and consistency;
- long-CoT transfers differently to reasoning and instruction models;
- trained WebDancer policies outperform their base or vanilla-ReAct counterparts.

These are analytical reconstructions [D], not author-enumerated hypotheses.

# 6. Assumptions / Threat Model

This is not a cybersecurity paper, so no attacker threat model is defined.

The operational model assumes [A, §§2.2–3.2]:

- questions have short reference answers;
- a policy can interact through `search`, `visit`, and terminal `answer` actions;
- search returns ten titles/snippets;
- visited pages can be summarized by a separate model, \(M_s\);
- a judge model, \(M_j\), can assess correctness adequately;
- synthetically generated data contain some invalid/noisy cases, which filtering and dynamic sampling should suppress;
- tool responses are external context and should not contribute directly to the model-token training loss;
- web interaction is dynamic and partially observable;
- reward can be represented primarily by binary judged correctness, plus a smaller formatting reward.

Trusted components include the search environment, summarizer, reference answers, filtering judges, and RL judge. Their independent accuracy is not evaluated in the supplied work.

# 7. Methodology

## 7.1 Overall design

The four-stage pipeline is [A, pp. 2–7]:

```text
Synthetic QA construction
        ↓
Trajectory sampling and rejection/filtering
        ↓
SFT cold start on accepted ReAct trajectories
        ↓
On-policy DAPO RL on unused QA pairs
```

## 7.2 CRAWLQA construction

The system collects root URLs from official or knowledge-oriented sites such as arXiv, GitHub, and wikis. It recursively follows hyperlinks, collects page content, and uses GPT-4o to generate question–answer pairs. Prompts request question types including **COUNT**, **MULTI-HOP**, and **INTERSECTION** [A, §2.1 and Fig. 1, p. 3].

The intended benefit is scalable acquisition of questions that genuinely require page traversal.

## 7.3 E2HQA construction

E2HQA begins with a concise fact-seeking question. At iteration \(n\):

1. select an entity \(E_n\) in question \(Q_n\);
2. search for related information \(C_n\);
3. have a model rewrite that content into a new query fragment \(R_n\);
4. replace the original entity with \(R_n\), producing \(Q_{n+1}\).

The rewriting relation is stated as \(R_n=\pi(S(C_n))\) [A, pp. 3–4]. Repeated rewriting increases the number of subproblems while preserving the final answer.

## 7.4 Trajectory sampling

Each trajectory alternates Thought, Action, and Observation. Short trajectories are sampled with GPT-4o. Long trajectories are generated with QwQ-Plus using prior actions and observations—but not prior thoughts—as input to the next reasoning step. The generated thoughts are nevertheless retained as SFT targets [A, p. 4].

Each QA instance can undergo rejection sampling up to **\(N=5\)** times [A, Appendix E.3, p. 19].

## 7.5 Filtering

A three-stage funnel is used [A, pp. 4–5]:

1. **Validity control:** discard malformed/noncompliant ReAct outputs.
2. **Correctness verification:** retain only answers judged correct, using GPT-4o during trajectory selection.
3. **Quality assessment:** reject hallucinated, severely repetitive, redundant, misaligned, or logically deficient trajectories.

Appendix D adds an explicit repetition rule: maximum occurrences of any 10-gram are constrained to **4** [A, p. 18].

There is an apparent wording problem: p. 5 says the authors “filter out trajectories with more than two actions,” yet Table 4 reports mean action counts of **4.56** and **2.31**. This is a **text–table inconsistency**. The most plausible editorial possibilities cannot be resolved from the supplied document.

## 7.6 Training data

The authors collect [A, Appendix D, p. 18]:

- **40,000 E2HQA** samples;
- **60,000 CRAWLQA** samples.

Accepted SFT trajectories comprise:

- **7,678 Short-CoT** examples;
- **6,550 Long-CoT** examples.

The paper does not give a complete accounting from 100,000 QA pairs to all intermediate accepted/rejected pools, nor does it fully specify the exact RL subset for every model. Appendix A says only a small subset, “e.g., 5,000 pairs,” can be used in RL [A, p. 17].

## 7.7 SFT

The serialized trajectory uses:

- `<think>…</think>`;
- `<tool_call>…</tool_call>`;
- `<tool_response>…</tool_response>`;
- `<answer>…</answer>` [A, p. 5].

During training, loss is masked on observation tokens so that the model learns only its own thoughts and actions, not the external tool’s reply [A, Eq. (2), pp. 5–6].

## 7.8 RL

RL operates on QA pairs not used in SFT. For each prompt, DAPO samples **16 rollouts** [A, Appendix E.3, p. 19], computes judged rewards, normalizes rewards within the sampled group, and updates only model-generated tokens.

Dynamic sampling rejects groups in which all candidate answers are correct or all are incorrect. Such groups provide no within-group comparative signal [A, Eq. (3), p. 6].

## 7.9 Reward

The total reward is:

\[
R(\hat y_i,y)=0.1\,score_{\text{format}}+0.9\,score_{\text{answer}}.
\]

Both components are binary. Correctness therefore dominates formatting [A, Eq. (5), p. 7].

## 7.10 Models and implementation

| Function | Model/system |
|---|---|
| Short-CoT trajectory generator | GPT-4o |
| Long-CoT trajectory generator | QwQ-Plus |
| Visit summarizer \(M_s\) | Qwen-2.5-72B |
| Judge \(M_j\) | Qwen-72B-Instruct |
| Agent framework | ReAct on Qwen-Agent |
| RL implementation | verl |
| Main policy backbones | Qwen-2.5-7B, Qwen-2.5-32B, QwQ-32B |

Training/inference parameters [A, Appendix E.3, p. 19]:

- evaluation inference: temperature 0.6, top-\(p\) 0.95;
- LRM repetition penalty: 1.1;
- LLM repetition penalty: 1.0;
- RL rollout: temperature 1.0, top-\(p\) 1.0.

Hardware is reported as **32 nodes with 8 NVIDIA H20 96-GB GPUs**. The wording does not explicitly clarify whether this means eight GPUs per node or eight total; the natural reading is eight per node, but that is not stated unambiguously.

## 7.11 Benchmarks and metrics

The primary evaluation uses [A, §4.1 and Appendix E.1]:

- **103 questions** from GAIA’s text-only validation split;
- **680 questions** from the WebWalkerQA test set;
- Pass@1 evaluated by LLM-as-Judge.

Additional tests use BrowseComp English and Chinese with Pass@1/Pass@3 [A, Table 2, p. 8].

No confidence intervals, conventional significance tests, random seeds, or repeated-run variance estimates are reported.

# 8. Experiments / Analyses

## X1 — Main GAIA and WebWalkerQA comparison

**Purpose:** determine whether WebDancer improves different backbones and how it compares with non-agentic and agentic baselines.

**Setup:** 103 GAIA text-only validation questions and 680 WebWalkerQA test questions; Pass@1; model-based judging [A, pp. 7, 19].

**Result:** every WebDancer row improves on its corresponding vanilla ReAct row in average score, with the largest reported WebWalkerQA gain for QwQ-32B [A, Table 1].

**Caveats:** small GAIA sample; dynamic web; missing results for several baselines; no uncertainty estimates.

## X2 — BrowseComp and BrowseComp-zh

**Purpose:** test more difficult and multilingual browsing tasks.

**Result:** WebDancer reports 3.8/7.9 on English BrowseComp and 18.0/31.5 on Chinese BrowseComp, interpreted as Pass@1/Pass@3 [A, Table 2, p. 8].

**Caveats:** the table does not state the tested WebDancer backbone, sample counts, or enough procedural detail to reproduce this comparison.

## X3 — Data-efficiency/data-source ablation

**Purpose:** compare Open-only, Crawl-only, E2H-only, All, and Final filtered data on GAIA.

**Data labels:** 1,308; 9,662; 2,485; 17,764; and 6,550 examples respectively [B, Fig. 3, p. 8].

**Metrics:** Pass@3 and consistency.

**Result:** Final performs best despite containing fewer examples than All, supporting the authors’ claim that filtering quality matters more than raw volume [A/B, pp. 8–9].

**Caveat:** bar values are not numerically labeled and the small figure prevents confident exact extraction.

## X4 — Detailed SFT versus RL evaluation

**Purpose:** quantify RL’s change in Pass@1, Pass@3, and Cons@3 for 7B, 32B, and QwQ models.

**Reported improvements:** Figure 4 annotates gains of:

- Pass@1: +7.70, +5.80, +1.95;
- Pass@3: +2.90, +5.80, +0.97;
- Cons@3: +2.67, +8.68, +1.74,

for 7B, 32B, and QwQ respectively [B, Fig. 4, p. 9].

**Interpretation:** RL has larger effects for non-reasoning instruction models than for QwQ, although QwQ still gains consistency [A, pp. 8–9].

## X5 — RL without SFT cold start

**Purpose:** test whether RL alone can teach the required behavior.

**Result:** QwQ trained in a single RL setting achieves only **5% Pass@3 on GAIA** [A, p. 9].

**Interpretation:** the authors conclude SFT cold start is essential.

**Caveat:** the exact control configuration and training budget are not fully described.

## X6 — Performance across DAPO training steps

**Purpose:** examine whether additional RL steps improve success and consistency.

**Result:** Figure 5a shows Pass@3 and Consistency@3 generally rising over the plotted 40–60 step interval [A/B, pp. 9–10].

**Caveat:** exact point values are visually approximate; no error bars or repeated-run variance are provided.

## X7 — CoT transfer analysis

**Purpose:** compare Short-CoT with Long-CoT training for instruction and reasoning models.

**Result:** Long-CoT raises Pass@3 for all three models, but sharply raises invalid output rates, particularly for Qwen2.5-7B [A, Table 3, p. 9].

For Qwen2.5-7B, Long-CoT increases Pass@3 by **1.94 points** but invalid rate by **20.71 points** [C: 35.92−33.98; 21.36−0.65]. For QwQ-32B, it increases Pass@3 by **13.59 points**, Cons@3 by **11.33 points**, and invalid rate by **12.30 points** [C].

## X8 — Emergent action count and reasoning length

**Purpose:** compare base, SFT, and RL behavior.

**Result:** Figure 5b shows action count and reasoning length increasing from Base to SFT and again to RL. Approximate endpoints are roughly 3.5 to 6.5 actions and 380 to about 500 reasoning tokens [B, approximate visual estimates].

**Caveat:** the paper’s prose identifies Qwen-32B, but exact plotted values are not labeled.

## X9 — Temperature sensitivity

**Purpose:** test whether decoding randomness explains unstable performance.

**Result:** Figure 5c shows similar Pass@1 and Pass@3 across temperatures 0.5, 0.6, and 0.7 [A/B, p. 10].

**Interpretation:** the authors attribute more instability to changes in the web environment than to decoding temperature.

**Caveat:** no variance estimates are shown, so “minimal impact” is descriptive, not a formal equivalence finding.

## X10 — Memorization stress test

**Purpose:** assess whether even memorizing training trajectories stabilizes performance.

**Setup:** Qwen-7B fine-tuned for **10 epochs** on **69 correctly sampled trajectories** from GAIA’s development set, then evaluated on the same set with greedy decoding [A, p. 10].

**Result:** only **37.4%** success.

**Interpretation:** the authors take this as evidence that open-web agent execution is difficult to stabilize.

**Caveat:** because tool/environment variation can affect an otherwise memorized task, this is not a conventional test of parameter memorization alone [D].

## X11 — Qualitative case study

**Purpose:** illustrate decomposition, hypothesis testing, gap handling, and reflection.

The agent identifies the fish as *Amphiprion ocellaris*, visits USGS occurrence records, discovers a 2018 Fred Howard Park occurrence, notices the missing postal code, performs another search, and answers **34689** [A/B, Fig. 8, pp. 21–24].

A serious anomaly appears in Step 2: its thought suddenly discusses chinstrap-penguin populations, unrelated to the clownfish task [A/B, p. 22]. The later trajectory returns to the correct question. This directly observable contamination conflicts with the figure’s presentation as an example of sophisticated coherent reasoning.

# 9. Results

## Main benchmark findings

| Backbone | Benchmark | Vanilla ReAct | WebDancer | Absolute gain [C] |
|---|---:|---:|---:|---:|
| Qwen-2.5-7B | GAIA Avg. | 18.4 | 31.0 | +12.6 points |
| Qwen-2.5-7B | WebWalkerQA Avg. | 24.2 | 36.0 | +11.8 points |
| Qwen-2.5-32B | GAIA Avg. | 31.0 | 40.7 | +9.7 points |
| Qwen-2.5-32B | WebWalkerQA Avg. | 31.9 | 38.4 | +6.5 points |
| QwQ-32B | GAIA Avg. | 37.8 | 51.5 | +13.7 points |
| QwQ-32B | WebWalkerQA Avg. | 24.1 | 47.9 | +23.8 points |

All gains are analyst-derived subtraction from Table 1. They are percentage-point-style score differences, not relative percentages.

The strongest WebDancer result is QwQ-32B. It exceeds GPT-4o vanilla ReAct by **16.9 points on GAIA** and **14.1 points on WebWalkerQA** [C: 51.5−34.6 and 47.9−33.8]. This supports the paper’s narrower claim that trained open models can outperform GPT-4o under this ReAct evaluation. It does not show superiority to every closed system: OpenAI Deep Research scores **67.4 on GAIA**, 15.9 points above QwQ-WebDancer [C].

## Difficulty-level behavior

QwQ-32B WebDancer reports [A, Table 1]:

- GAIA: Level 1 61.5, Level 2 50.0, Level 3 25.0;
- WebWalkerQA: Easy 52.5, Medium 59.6, Hard 35.4.

Performance generally drops on the hardest categories. WebWalkerQA Medium exceeds Easy, showing the named levels do not produce a perfectly monotonic empirical ordering for this model.

Qwen-2.5-7B WebDancer remains at **0.0 on GAIA Level 3**, despite substantial gains at Levels 1 and 2. Training therefore does not eliminate the smallest model’s hardest-level failure [A, Table 1].

## Pass@3

The paper reports its best model achieving **64.1% Pass@3 on GAIA** and **62.0% on WebWalkerQA** [A, §5, p. 8]. The exact model is described only as “our best-performing model” in that sentence; context suggests QwQ-32B, but the document does not explicitly attach the backbone there.

## Data and training findings

- Final filtered data outperform larger unfiltered combinations under the Figure 3 comparison [A/B, pp. 8–9].
- RL alone yields only 5% GAIA Pass@3, supporting the cold-start stage [A, p. 9].
- RL improvements are largest for some non-reasoning models and smaller for QwQ [A/B, Fig. 4].
- Long-CoT is especially beneficial to QwQ but creates elevated invalid rates for all reported models [A, Table 3].
- More RL steps improve Pass@3 and consistency over the plotted range [A/B, Fig. 5a].
- SFT and RL both lengthen reasoning and increase tool actions [A/B, Fig. 5b].
- Temperature 0.5–0.7 has little visible effect [A/B, Fig. 5c].
- Same-set memorization remains low at 37.4% [A, p. 10].

No inferential statistics establish whether numerical differences are statistically significant.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Two web-data generation pipelines

- **Type:** process diagram.
- **Top panel:** CRAWLQA follows a website tree from root to deeper subpages, then generates a question and answer from gathered content.
- **Bottom panel:** E2HQA iteratively transforms \(Q_1\) through \(Q_n\) by retrieving new evidence and replacing entities with descriptions.
- **Visual examples:** a Godot game question for CRAWLQA and an IEEE award question expanded into a more elaborate fuzzy-logic query for E2HQA.
- **Conclusion supported:** question difficulty can be synthesized either by browsing depth or iterative semantic rewriting.
- **Caveat:** the figure illustrates workflows, not measured validity or difficulty.

## Figure 2 — Training framework

- **Panel I, SFT:** a base model is trained on Short- and Long-CoT ReAct trajectories from CRAWLQA/E2HQA.
- **Panel II, RL:** unused QA pairs drive rollouts; the policy calls tools, receives rewards, compares grouped candidates, and computes advantages under a KL/reference-model structure.
- **Flow:** task → policy → repeated tool interaction → candidate rollouts → reward → group computation → advantage → policy update.
- **Conclusion supported:** SFT and RL consume related but distinct forms of data.
- **Caveat:** the diagram abstracts away dataset partition rules, optimizer settings, and detailed computational costs.

## Figure 3 — Data-efficiency ablation

- **Plot:** grouped bars.
- **X-axis:** Open-only (1,308), Crawl-only (9,662), E2H-only (2,485), All (17,764), Final (6,550).
- **Y-axis:** score, approximately 0–60.
- **Legend:** Pass@3 and consistency.
- **Observation:** Final is tallest for both metrics; All is second; Open-only is weakest.
- **Exact versus approximate:** dataset counts are readable; bar heights are approximate because labels are absent.
- **Supported claim:** filtering is more valuable than simply retaining all data.

## Figure 4 — SFT versus RL across metrics and backbones

- **Plot:** paired, hatched bars grouped by model and metric.
- **X grouping:** 7B, 32B, QwQ repeated for Pass@1, Pass@3, and Cons@3.
- **Y-axis:** score percentage.
- **Annotations:** exact displayed gains of +7.70/+5.80/+1.95, +2.90/+5.80/+0.97, and +2.67/+8.68/+1.74.
- **Observation:** RL improves every shown combination, but gains vary considerably.
- **Supported claim:** RL adds value after SFT, particularly for instruction models.
- **Caveat:** no confidence intervals and exact base/final values are not all labeled.

## Figure 5a — DAPO training progression

- **X-axis:** training step, visually spanning about 40–60.
- **Left y-axis:** Pass@3; right y-axis: Consistency@3.
- **Observation:** both series generally increase, with some flattening.
- **Conclusion:** additional on-policy training improves success and consistency over this interval.
- **Caveat:** small figure, exact points not labeled, no error bars.

## Figure 5b — Action count and reasoning length

- **X-axis:** Base, SFT, RL.
- **Left y-axis:** action count.
- **Right y-axis:** reasoning length.
- **Observation:** both increase monotonically across the three stages.
- **Approximate values:** actions about 3.5→6.2→6.5; length about 380→430→500.
- **Caveat:** estimates are graphical, not exact reported values.

## Figure 5c — Temperature sensitivity

- **X-axis:** temperature 0.5, 0.6, 0.7.
- **Y-axis:** performance.
- **Bars:** Pass@1 and Pass@3.
- **Observation:** scores are visually similar across temperatures.
- **Conclusion:** temperature variation in this narrow range does not explain most observed instability.
- **Caveat:** the visual cannot establish statistical equivalence.

## Figure 6 — Traditional ReAct prompt for LLMs

The prompt explicitly demands:

- evidence-chain completeness assessment;
- tool-selection rationale;
- alternating Thought/Action/Observation;
- JSON action parameters;
- a final answer only when confidence is sufficient.

It is a prompt artifact rather than a quantitative figure. It shows that the Short-CoT generator receives substantial procedural scaffolding.

## Figure 7 — Modified ReAct prompt for LRMs

This prompt is shorter and emphasizes action formatting, mandatory tool use before the final answer, and valid JSON. Unlike Figure 6, it does not explicitly request a visible Thought field. This aligns with the method in which the LRM supplies its own internal reasoning content while the external prompt focuses on actions.

The figure heading says “Case Trajectory in GAIA,” although its caption calls it an LRM prompt. This appears to be a labeling/layout inconsistency.

## Figure 8 — GAIA case study

- **Content:** a five-step ReAct trajectory spanning pp. 21–24.
- **Flow:** identify likely species → search USGS → visit occurrence record → notice missing ZIP code → search address → answer 34689.
- **Observed strengths:** goal decomposition, hypothesis checking, recovery from missing information, and an additional search to bridge location to postal code.
- **Observed anomaly:** Step 2 contains unrelated chinstrap-penguin reasoning [B, p. 22].
- **Conclusion:** the final action sequence demonstrates recovery and tool use, but the trajectory is not a clean demonstration of coherent reasoning throughout.
- **Visual limitation:** p. 23 was supplied only as extracted text.

# 11. Table-by-Table Interpretation

## Table 1 — Main GAIA and WebWalkerQA results

Rows are grouped into:

- No Agency;
- closed-source agentic frameworks;
- open-source agentic frameworks;
- ReAct frameworks.

Columns report GAIA Levels 1–3 and average, then WebWalkerQA Easy/Medium/Hard and average. A dash means unreported or unreproducible.

Key observations:

- OpenAI Deep Research is best on GAIA average at 67.4.
- QwQ-32B WebDancer is the best reported WebDancer: 51.5 GAIA and 47.9 WebWalkerQA.
- WebDancer improves every matched vanilla-ReAct average.
- WebThinker-RL scores 48.5/46.5, so QwQ-WebDancer is 3.0 points higher on GAIA and 1.4 higher on WebWalkerQA [C].
- Qwen-2.5-7B WebDancer still scores 0.0 on GAIA Level 3.
- Statistical uncertainty is absent.

The caption says the best results “among all frameworks” are bold, but the visual bolding emphasizes WebDancer values even where OpenAI Deep Research is numerically higher on GAIA. This is a caption–format ambiguity.

## Table 2 — BrowseComp results

Columns are framework, browsing availability, English, and Chinese scores. WebDancer’s slash-separated results are Pass@1/Pass@3.

- GPT-4o without browsing: 0.6 English, 6.2 Chinese.
- GPT-4o with browsing: 1.9 English; Chinese absent.
- QwQ-32B without browsing: Chinese 11.1.
- WebDancer with browsing: 3.8/7.9 English and 18.0/31.5 Chinese.

Missing values are denoted by dashes. The table lacks the WebDancer backbone and sample sizes.

## Table 3 — CoT knowledge transfer

Columns compare Short-CoT and Long-CoT for Pass@3, Cons@3, and invalid rate.

| Model | Short Pass@3 | Long Pass@3 | Short invalid | Long invalid |
|---|---:|---:|---:|---:|
| Qwen2.5-7B | 33.98 | 35.92 | 0.65% | 21.36% |
| Qwen2.5-32B | 42.72 | 45.63 | 4.20% | 13.59% |
| QwQ-32B | 44.66 | 58.25 | 0.97% | 13.27% |

Long-CoT substantially helps the reasoning model but also raises invalidity. For Qwen2.5-7B, Cons@3 actually falls from 22.33 to 21.00 despite the small Pass@3 increase.

No uncertainty or sample denominator is supplied.

## Table 4 — Training dataset statistics

| CoT type | Number | Mean action count | Mean tokenized thought length |
|---|---:|---:|---:|
| Short | 7,678 | 4.56 | 510.03 |
| Long | 6,550 | 2.31 | 1,599.39 |

Long-CoT examples have roughly **3.14 times** the average thought length [C: 1599.39/510.03], but about **half the action count** [C: 2.31/4.56 ≈ 0.51]. This distinction matters: “long” refers to reasoning-token length, not more tool interactions.

The mean action count conflicts with the p. 5 statement about filtering out trajectories with more than two actions.

# 12. Diagram / Architecture Interpretation

The architecture has three interacting layers:

1. **Data layer:** CRAWLQA and E2HQA generate questions at scale.
2. **Trajectory layer:** strong models solve these questions through ReAct; the system filters trajectories for format, correctness, and quality.
3. **Learning layer:** SFT teaches the interaction grammar; RL improves outcome-directed behavior.

During inference:

```text
Question
  ↓
Policy generates thought
  ↓
Policy emits search or visit call
  ↓
External tool executes
  ↓
Summarizer returns an observation
  ↓
Observation is appended to context
  ↺ repeat until answer
```

During SFT, observations are context but not prediction targets. During RL, candidate trajectories are judged as groups, and model-token likelihoods—not tool-response tokens—are optimized. This symmetry is intentional [A, pp. 5–6].

A separate reference/old policy supplies the denominator for importance sampling and constrains updates. The reward system evaluates both protocol correctness and answer correctness, weighted 0.1 and 0.9 respectively.

# 13. Equations and Mathematical Concepts

## Equation (1) — Trajectory history

\[
H_t=(\tau_0,\alpha_0,o_0,\tau_1,\ldots,\tau_{t-1},\alpha_{t-1},o_{t-1}).
\]

- \(\tau_t\): thought at step \(t\).
- \(\alpha_t\): action.
- \(o_t\): observation.
- \(H_t\): everything observed/generated before the next decision.

The policy is described as producing thought and action conditional on this history, \(\pi(\tau_t,\alpha_t\mid H_t)\) [A, p. 4].

## Equation (2) — Observation-masked SFT loss

\[
L=
-\frac{1}{\sum_{i=1}^{|H|}\mathbb{I}[x_i\neq o]}
\sum_{i=1}^{|H|}
\mathbb{I}[x_i\neq o]\log \pi_\theta(x_i\mid tc,x_{<i}).
\]

This is normalized negative log-likelihood over model-controlled tokens only.

- \(tc\): task context.
- \(x_i\): a trajectory element/token belonging to thought, action, or observation.
- \(\mathbb I[x_i\neq o]\): indicator excluding observations.
- \(\pi_\theta\): trainable policy.

Plain meaning: teach the model what it should think and do, while letting tool outputs serve only as context.

## Equation (3) — DAPO objective

The objective averages a clipped policy-gradient contribution across \(G\) sampled executions and their generated tokens:

\[
J_{\text{DAPO}}(\theta)
=
\mathbb E\left[
\frac{1}{\sum_i|o_i|}
\sum_{i=1}^{G}\sum_{t=1}^{|o_i|}
\min\left(
r_{i,t}(\theta)\hat A_{i,t},
\operatorname{clip}(r_{i,t}(\theta),1-\epsilon_{\rm low},1+\epsilon_{\rm high})\hat A_{i,t}
\right)
\right].
\]

The accompanying constraint retains prompts whose sampled group contains at least one—but not all—correct-equivalent outputs:

\[
0<|\{o_i:\operatorname{is\_equivalent}(y,o_i)\}|<G.
\]

Plain meaning: learn only from mixed-outcome groups, and prevent any one policy update from changing probability ratios too aggressively.

The OCR/extraction makes some \(o_i\), \(q_i\), and time indices uncertain, but the objective’s role is clear.

## Equation (4) — Importance ratio and advantage

\[
r_{i,t}(\theta)=
\frac{\pi_\theta(o_i\mid q_i,o_{i,<t})}
{\pi_{\theta_{\rm old}}(o_i\mid q_i,o_{i,<t})},
\qquad
\hat A_{i,t}=
\frac{R_i-\operatorname{mean}(\{R_i\})}
{\operatorname{std}(\{R_i\})}.
\]

The first term compares how likely the current and old policies consider a sampled output. The second standardizes its reward within the rollout group. The extracted paper alternates \(j\) and \(t\) subscripts around Eq. (4), an apparent notation inconsistency.

## Equation (5) — Reward

\[
R(\hat y_i,y)=0.1\,score_{\rm format}+0.9\,score_{\rm answer}.
\]

A perfectly formatted but incorrect response receives 0.1; a correct but format-invalid response would receive 0.9 under the literal formula; a response satisfying both receives 1.0 [C from the binary definition]. The document does not clarify whether malformed responses can still receive an answer score in implementation.

# 14. Interpretation and Discussion

The evidence supports the authors’ principal empirical claim: the full training pipeline improves matched vanilla ReAct agents across three backbone scales and two primary benchmarks. The comparison is especially strong for QwQ-32B.

The analyses refine that conclusion:

- **Data quality matters:** a filtered 6,550-example set outperforms a larger 17,764-example combination in Figure 3.
- **SFT and RL have different functions:** RL alone performs poorly, while SFT supplies the interaction grammar and RL later improves outcomes.
- **Reasoning transfer is architecture-dependent:** Long-CoT substantially helps QwQ but creates invalid-output problems, particularly for the 7B instruction model.
- **More reasoning is not automatically cleaner reasoning:** the agent produces longer thought and more actions after training, yet the Figure 8 trajectory contains unrelated reasoning.
- **Web evaluation is unstable:** temperature barely changes performance, while even same-set training produces only 37.4% success. The authors infer that environmental non-stationarity contributes to variability.

Several conclusions should be kept narrow:

- Table 1 supports performance gains under the supplied judge and benchmark setup, not universal agent quality.
- The paper does not isolate the causal contribution of every pipeline component with a complete factorial ablation.
- The claim that the web environment causes instability is plausible but not directly separated from search-engine variation, summarizer behavior, judge noise, stochastic tool results, or implementation failures.
- “Generalization” is inferred from held-out benchmark performance and extra BrowseComp tests, not demonstrated across all web-agent task families.

# 15. Contributions and Novelty

## Conceptual contribution

A four-stage abstraction for constructing trained information-seeking agents from data generation through RL [A, pp. 1–2].

## Dataset contribution

Two synthetic-data procedures:

- CRAWLQA for page-traversal-grounded questions;
- E2HQA for answer-preserving easy-to-hard transformation.

The paper reports 100,000 collected QA samples before trajectory filtering [A, Appendix D].

## Methodological contribution

A three-stage rejection/filtering pipeline and a separation between accepted SFT trajectories and unused QA pairs recoverable for RL.

## Training contribution

A native ReAct post-training design combining observation-masked SFT and on-policy DAPO.

## Empirical contribution

Evaluation across GAIA, WebWalkerQA, BrowseComp, and BrowseComp-zh, plus analyses of data quality, cold starts, reasoning transfer, training progression, trajectory length, temperature, and memorization.

## Systems contribution

Integration of search, page visiting, summarization, structured tool calls, group rollouts, model judging, and distributed training.

The authors do not claim to invent ReAct or DAPO; novelty lies chiefly in the end-to-end assembly, synthetic-data strategies, and application to open-source web agents [A, Appendix C.1, p. 18].

# 16. Limitations

## Authors' stated limitations

Appendix A identifies six limitations [A, p. 17]:

1. **Tool number and type:** only two basic information-seeking tools are integrated.
2. **Task generalization:** evaluation focuses on short-answer tasks rather than document-level research and long-form generation.
3. **Data utilization:** only a small RL subset—e.g., 5,000 pairs—can be used because of computational and stability constraints.
4. **High rollout cost:** repeated tool calls and model completions make RL expensive and slow.
5. **Hybrid thinking:** models are trained on one CoT type; dynamic reasoning-length control is future work.
6. **Thinking-pattern failures:** nonexistent-tool hallucination and redundant over-action may occur.

The authors also acknowledge elsewhere that [A]:

- GAIA has a relatively small and variable test set (p. 8);
- Long-CoT may hallucinate simulated observations (p. 9);
- long trajectories may yield sparse reward (p. 8);
- real web environments are dynamic and resist stabilization (pp. 9–10);
- long-CoT transfer can cause repetition and context overflow (p. 9).

## Additional evidence-based analyst observations

These are [D], not author admissions:

- **Judge dependence:** trajectory filtering, RL rewards, and final evaluation all rely on model judgments, creating correlated sources of error.
- **No judge-agreement study:** no human validation, inter-rater agreement, calibration, or sensitivity to alternate judges is supplied.
- **Limited statistical reporting:** no confidence intervals, significance tests, seeds, or repeated-run dispersion.
- **Incomplete data accounting:** the path from 100,000 synthesized QA pairs to SFT/RL subsets is only partially reported.
- **Unresolved action-count inconsistency:** the “more than two actions” rule conflicts with Table 4’s averages.
- **Case-study contamination:** Figure 8 contains an unrelated penguin passage.
- **Dynamic external services:** reproducibility may depend on changing search results and web pages.
- **Potential benchmark exposure:** the supplied paper does not report checks for benchmark leakage into foundation models or synthetic-data sources.
- **Resource accessibility:** the reported distributed hardware requirement may impede independent reproduction.
- **BrowseComp underspecification:** backbone, sample sizes, and evaluation details are not adequately stated near Table 2.

# 17. Threats to Validity

## Internal validity

The design does not fully isolate the effects of question synthesis, generator model, filtering, SFT, DAPO, reward design, and backbone. Differences may reflect several components simultaneously.

## Construct validity

Pass@1/3 and Cons@3 capture answer success but do not directly measure source faithfulness, search efficiency, reasoning correctness, safety, or research-report quality. Binary LLM judging may not perfectly operationalize correctness.

## Statistical conclusion validity

GAIA uses only 103 questions, and no uncertainty intervals or hypothesis tests are shown. Small score changes—especially QwQ’s +0.97 Pass@3 gain—cannot be interpreted confidently as stable improvements without run variability.

## External validity

Primary tests are short-answer tasks using two web tools. Results may not transfer to long-form synthesis, authenticated sites, GUI browsing, coding, transactional workflows, or rapidly changing domains.

## Ecological validity

Live-web interaction is more realistic than static retrieval, but the environment includes a specific search engine, summarizer, tool schema, and judge. This is one operational ecology rather than the full web.

## Reproducibility

Implementation pointers and many hyperparameters are provided, but exact dataset instances, splits, checkpoint details, optimization schedules, clipping parameters, and complete evaluation prompts are not all present in the supplied document. Live-web drift further complicates exact reproduction.

## Generalizability

Results span three model scales and both instruction/reasoning backbones, which strengthens within-family evidence. However, all trained backbones are from the Qwen/QwQ family, limiting cross-family conclusions.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- add modular browser functions and a Python sandbox;
- support external APIs and more human-like interaction;
- extend from short answers to document-level research and generation;
- design better rewards for open-ended long-form output;
- improve RL data efficiency beyond small subsets;
- reduce rollout cost;
- scale the high-quality dataset;
- create hybrid agents that dynamically choose reasoning length;
- reduce nonexistent-tool hallucinations and over-action [A, pp. 17–18].

## B. Additional open questions

- How accurate are the synthetic QA answers and the model-based filters under human review?
- Which pipeline stage contributes most after controlling for backbone and training compute?
- Would an independent judge materially change the rankings?
- How often does reasoning contamination like Figure 8 occur?
- Can source citation and evidence faithfulness be rewarded directly?
- What fraction of performance variance comes from policy sampling versus live-web drift?
- Does Long-CoT remain beneficial after controlling for token budget and number of actions?
- How does performance scale with SFT/RL data under fixed compute?
- Can the same pipeline transfer to non-Qwen model families?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Agent | A model that selects actions and interacts with an environment |
| CRAWLQA | Synthetic QA generated from recursively crawled web pages |
| E2HQA | Easy-to-hard QA generated through answer-preserving rewrites |
| CoT | Chain of thought; intermediate reasoning |
| Short-CoT / Long-CoT | Relatively short or extended reasoning trajectories |
| ReAct | A framework alternating reasoning, action, and observation |
| LLM | Large language model |
| LRM | Large reasoning model |
| SFT | Supervised fine-tuning by imitation of accepted examples |
| RFT | Rejection-sampling fine-tuning; train only on accepted sampled trajectories |
| RL | Reinforcement learning from outcome rewards |
| DAPO | Decoupled Clip and Dynamic Sampling Policy Optimization |
| RAG | Retrieval-augmented generation |
| Pass@1 | Whether one attempt succeeds |
| Pass@3 | Whether at least one of three attempts succeeds |
| Cons@3 | Fraction of three attempts that are correct |
| Rollout | One sampled agent execution |
| Policy | The model’s conditional behavior for generating thoughts/actions |
| Advantage | Relative quality of a rollout compared with its sampled group |
| Importance ratio | Current-policy likelihood divided by old-policy likelihood |
| Dynamic sampling | Keeping prompts whose rollout groups contain mixed outcomes |
| \(\tau_t\) | Thought at step \(t\) |
| \(\alpha_t\) | Action at step \(t\) |
| \(o_t\) | Observation at step \(t\) |
| \(H_t\) | Interaction history before step \(t\) |
| \(\pi_\theta\) | Trainable policy |
| \(M_s\) | Visit-result summarizer |
| \(M_j\) | Correctness judge |
| \(G\) | Number of sampled candidate rollouts |
| \(\hat A\) | Estimated, group-normalized advantage |
| \(\epsilon_{\rm low/high}\) | Lower and upper clipping bounds; values not supplied |
| top-\(p\) | Nucleus-sampling threshold |
| Invalid rate | Percentage of outputs failing required validity criteria |
| Non-stationary environment | An environment whose content/behavior changes over time |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| CRAWLQA collected | 60,000 | QA samples | Before trajectory filtering | Author-reported | p. 18, App. D |
| E2HQA collected | 40,000 | QA samples | Before trajectory filtering | Author-reported | p. 18, App. D |
| Short-CoT SFT data | 7,678 | trajectories | Mean 4.56 actions, 510.03 thought tokens | Author-reported | Table 4, p. 18 |
| Long-CoT SFT data | 6,550 | trajectories | Mean 2.31 actions, 1599.39 thought tokens | Author-reported | Table 4, p. 18 |
| Long/short thought-length ratio | 3.14 | ratio | 1599.39 ÷ 510.03 | Analyst-derived | Table 4 |
| Rejection samples per QA | 5 | attempts | \(N=5\) | Author-reported | App. E.3, p. 19 |
| RL rollout count | 16 | rollouts/prompt | Training | Author-reported | App. E.3, p. 19 |
| GAIA evaluation sample | 103 | questions | Text-only validation | Author-reported | App. E.1, p. 19 |
| WebWalkerQA sample | 680 | questions | Test set | Author-reported | App. E.1, p. 19 |
| QwQ-WebDancer GAIA | 51.5 | Pass@1 score | Average | Author-reported | Table 1, p. 7 |
| QwQ-WebDancer WebWalkerQA | 47.9 | Pass@1 score | Average | Author-reported | Table 1, p. 7 |
| QwQ WebDancer gain over vanilla | +13.7 | points | GAIA, 51.5−37.8 | Analyst-derived | Table 1 |
| QwQ WebDancer gain over vanilla | +23.8 | points | WebWalkerQA, 47.9−24.1 | Analyst-derived | Table 1 |
| Best reported Pass@3 | 64.1 | percent | GAIA | Author-reported | §5, p. 8 |
| Best reported Pass@3 | 62.0 | percent | WebWalkerQA | Author-reported | §5, p. 8 |
| RL-only cold-start test | 5 | percent Pass@3 | QwQ on GAIA | Author-reported | p. 9 |
| Long-CoT QwQ Pass@3 | 58.25 | score | Versus 44.66 Short-CoT | Author-reported | Table 3, p. 9 |
| Long-CoT Qwen-7B invalid rate | 21.36 | percent | Versus 0.65% Short-CoT | Author-reported | Table 3 |
| BrowseComp English | 3.8/7.9 | Pass@1/Pass@3 | WebDancer | Author-reported | Table 2, p. 8 |
| BrowseComp Chinese | 18.0/31.5 | Pass@1/Pass@3 | WebDancer | Author-reported | Table 2, p. 8 |
| Memorization stress test | 37.4 | percent | 69 trajectories, 10 epochs, same-set greedy evaluation | Author-reported | p. 10 |
| Reward weights | 0.1 / 0.9 | proportion | Format / answer | Author-reported | Eq. (5), p. 7 |
| Evaluation temperature/top-\(p\) | 0.6 / 0.95 | parameters | Inference | Author-reported | App. E.3, p. 19 |
| Training hardware | 32 × 8 H20 | GPUs/nodes, wording ambiguous | H20 has reported 96 GB | Author-reported | App. E.3, p. 19 |
| Figure 5b actions | ~3.5→~6.5 | actions | Base→RL | Approximate visual estimate | Fig. 5b, p. 10 |
| Figure 8 answer | 34689 | ZIP code | Fred Howard Park case | Visually readable | Fig. 8, p. 24 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WebDancer improves vanilla ReAct | Higher averages for every matched backbone | T1 / X1 | p. 7 | Strong within reported setup; no uncertainty estimates |
| Reasoning backbones benefit most in absolute top-line performance | QwQ-WebDancer reaches 51.5/47.9 | T1 | p. 7 | Supported among tested backbones only |
| SFT is necessary for cold start | RL-only QwQ obtains 5% Pass@3 | X5 | p. 9 | Suggestive; control details limited |
| RL improves SFT policies | All nine annotated Fig. 4 changes are positive | F4 / X4 | p. 9 | Supported descriptively; small gains lack uncertainty |
| Filtering quality matters | Final 6,550-example set exceeds larger All set | F3 / X3 | pp. 8–9 | Strong ablation pattern; exact scores unlabeled |
| Long-CoT transfers best to reasoning models | QwQ Pass@3 44.66→58.25 | T3 / X7 | p. 9 | Supported, but invalid rate also rises |
| Long-CoT can harm validity | Invalid rates rise for all models | T3 | p. 9 | Strong table evidence |
| RL produces longer, more agentic trajectories | More actions and reasoning length after SFT/RL | F5b / X8 | pp. 9–10 | Descriptive behavioral proxy |
| Temperature is not the main instability source | Similar scores at 0.5–0.7 | F5c / X9 | p. 10 | Narrow range; no variance analysis |
| Web environments resist stabilization | 37.4% same-set stress-test result | X10 | p. 10 | Suggestive, not causal proof |
| Agent demonstrates iterative reflection | It searches for a ZIP code after USGS lacks one | F8 / X11 | pp. 21–24 | Supported, but unrelated Step 2 weakens trajectory quality |
| Pipeline generalizes to harder benchmarks | BrowseComp results exceed shown nonbrowsing rows | T2 / X2 | p. 8 | Limited by missing backbone/sample details |

# 22. Very Simple Explanation

Imagine training someone to solve hard internet questions. Giving them a search box is not enough: they must learn what to search for, which result to open, what information is missing, and when they have enough evidence to answer.

WebDancer teaches this in stages. It first manufactures many difficult questions. It then has strong models demonstrate how to solve them, discards bad demonstrations, and trains a smaller model to copy the good behavior. Finally, reinforcement learning rewards the model when its complete search process leads to a correct, properly formatted answer.

The method improves all three tested model backbones over ordinary ReAct agents. Its strongest version performs well among open-source systems, although it remains behind OpenAI Deep Research on GAIA. The experiments also show that good filtering matters, supervised training is important before RL, and very long reasoning can improve answers while also causing repetition or invalid outputs.

The main lesson is that a good web agent is not created merely by attaching search. It needs suitable questions, clean examples of tool use, a careful training sequence, and a way to learn from successful complete searches. The paper also shows that this remains difficult: the web changes, rollouts are costly, model judges can be imperfect, and even the showcased trajectory contains an unrelated reasoning fragment.

# Completeness Audit

## Inventory coverage

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text and rendered p. 1 | Yes | Fully represented | Orientation and contribution |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, objectives, contributions |
| §2 Dataset synthesis | Yes | Yes | Fully represented | CRAWLQA, E2HQA |
| §2.2 Trajectory sampling | Yes | Yes | Fully represented | ReAct, CoT generation, filtering |
| §3 Agent learning | Yes | Yes | Fully represented | SFT, RL, rollout, reward |
| §4 Experiments | Yes | Yes | Fully represented | Primary and extra benchmarks |
| §5 Analysis | Yes | Yes | Fully represented | All identified analyses X3–X10 |
| §6 Related work | Yes | Yes | Represented in compressed form | Categories and claimed distinctions preserved |
| §7 Conclusion | Yes, text-only p. 11 | Yes | Represented in compressed form | Repeats central contribution |
| References | Yes, text-only pp. 12–16 | Indirectly | Deliberately compressed | Bibliographic entries not individually restated |
| Appendix A Limitations | Yes, text-only | Yes | Fully represented | Six stated categories |
| Appendix B Broader impacts | Yes, text-only | Yes | Represented in compressed form | Benefits, misinformation, extraction/surveillance, responsible deployment |
| Appendix C Discussions | Yes | Yes | Fully represented | Concurrent work and agentic-model framing |
| Appendix D Training dataset | Yes | Yes | Fully represented | Counts, means, n-gram rule, open-only sources |
| Appendix E Experimental details | Yes | Yes | Fully represented | Benchmarks, baselines, implementation, prompts |
| Appendix F Case study | Yes; p. 23 text-only | Yes | Fully represented with limitation | Contamination anomaly recorded |
| Explicit research questions | Yes | Yes | Fully represented | None formally stated |
| Formal hypotheses | Yes | Yes | Fully represented | None formally stated |
| Figure 1 | Yes, visual | Yes | Fully represented | Both pipelines |
| Figure 2 | Yes, visual | Yes | Fully represented | SFT and RL panels |
| Figure 3 | Yes, visual | Yes | Fully represented with approximate bars | Exact bar heights unlabeled |
| Figure 4 | Yes, visual | Yes | Fully represented | Annotated gains preserved |
| Figure 5a | Yes, visual | Yes | Fully represented with estimates | No exact point labels |
| Figure 5b | Yes, visual | Yes | Fully represented with estimates | Dual axes |
| Figure 5c | Yes, visual | Yes | Fully represented | Narrow temperature range |
| Figure 6 | Yes, visual/text | Yes | Fully represented | LLM prompt |
| Figure 7 | Yes, visual/text | Yes | Fully represented | LRM prompt; header inconsistency noted |
| Figure 8 | Partial visual plus complete extracted text | Yes | Fully represented with limitation | p. 23 not visually supplied |
| Table 1 | Yes, visual/text | Yes | Fully represented | Main benchmark results |
| Table 2 | Yes, visual/text | Yes | Fully represented | Missing setup details noted |
| Table 3 | Yes, visual/text | Yes | Fully represented | Exact values and derived differences |
| Table 4 | Yes, visual/text | Yes | Fully represented | Exact statistics |
| Equation (1) | Yes | Yes | Fully represented | History definition |
| Equation (2) | Yes | Yes | Fully represented | OCR-sensitive notation noted |
| Equation (3) | Yes | Yes | Fully represented | Objective and constraint |
| Equation (4) | Yes | Yes | Fully represented | Subscript inconsistency noted |
| Equation (5) | Yes | Yes | Fully represented | Reward interpretation |
| Algorithms | Yes | Yes | Represented in prose | No numbered pseudocode algorithm exists |
| Major contributions | Yes | Yes | Fully represented | Conceptual through empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Appendix A plus relevant main-text caveats |
| Broader impacts | Yes | Yes | Represented in compressed form | No independent external assessment |
| Supplied supplementary material | N/A | N/A | Missing from supplied material | No separate supplementary artifact supplied |

## Missing or inaccessible material

- No pages are missing from the extracted main document.
- Pages 11–17 and 23 were not visually rendered; their content was inspected through supplied extracted text.
- Fine bibliographic typography on pp. 12–16 was not visually checked.
- The Qwen-Agent repository and the paper’s WebAgent repository were referenced but not supplied.
- External datasets, source webpages, checkpoints, training logs, evaluation outputs, and cited papers were not supplied and were not independently checked.
- No separate supplementary material was provided.
- Exact values for every bar/point in Figures 3 and 5 are unavailable because the plots do not label them sufficiently.

## Uncertain interpretations

- Equation (3)–(4) indices contain extraction-sensitive \(i,j,t\) notation and appear internally inconsistent.
- “Filter out trajectories with more than two actions” conflicts with Table 4’s mean action counts of 4.56 and 2.31.
- The hardware statement “32 nodes with 8 NVIDIA H20” does not explicitly clarify whether eight GPUs are installed per node.
- Table 1’s caption says globally best values are bold, while the visible emphasis does not straightforwardly match OpenAI Deep Research’s higher GAIA results.
- Table 2 does not identify the tested WebDancer backbone.
- Figure 7 carries the internal header “Case Trajectory in GAIA” although its caption identifies it as an LRM prompt.
- Figure 8’s unrelated penguin reasoning may be accidental data contamination, a layout error, or an actual model failure; the supplied work does not resolve which.
- The “best-performing model” associated with 64.1%/62.0% Pass@3 is not named in the relevant sentence.

## Deliberately compressed material

- The individual reference entries on pp. 12–16 were not reproduced.
- Related-work citations were summarized by methodological category rather than paper by paper.
- Prompt text in Figures 6 and 7 was explained structurally rather than copied verbatim.
- Figure 8’s full tool-response text was compressed while preserving its sequence, final answer, and anomalous passage.
- Appendix B’s broader-impact discussion was condensed because it is brief and not part of the empirical method.

## Potential omissions

No substantive section, subsection, experiment, figure, table, major equation, contribution, or author-stated limitation identified in the inventory is knowingly absent from this analysis. Exact unlabeled graphical coordinates, full bibliography entries, and repetitive prompt/case-study wording were deliberately compressed or marked unavailable rather than silently reconstructed.