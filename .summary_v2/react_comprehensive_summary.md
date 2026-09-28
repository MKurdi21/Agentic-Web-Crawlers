# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available extent | All 33 numbered pages |
| Apparently missing pages | None |
| Native text | Available on every page; no page was mechanically classified as scanned or low-text |
| Visually inspected pages | 1–9, 14–15, 22–25, and 31 |
| Pages not visually rendered | 10–13, 16–21, 26–30, and 32–33; these were available only through supplied page-labeled text |
| Figures visually available | All five numbered figures: Figures 1–3, 4, and 5 |
| Tables visually available | Tables 1–10 were rendered except Table 5’s placement within p. 14 and Tables 6–10 on rendered pages; all tables were also available as supplied text |
| Table readability | Main numerical tables are readable. Long prompt/trajectory tables are readable chiefly through the supplied native text; small typography limits reliable character-by-character visual reading |
| Equations | The paper contains a short formal definition of the agent and augmented action space, not a large equation system. The supplied text has extraction artifacts such as `7→` for a mapping arrow, but the meaning is recoverable from context |
| Appendices | Present: Appendices A–E, pp. 14–33 |
| Supplementary material | No separate supplementary file was supplied |
| External artifacts referenced but not supplied | Project/code websites and the underlying models, datasets, environments, and executable code |
| OCR required | No. Native text was supplied. Some rendered display text is encoded poorly in extraction, so visual and native-text evidence were cross-checked where possible |
| Principal limitation | Only 16 of 33 pages were visually rendered. Consequently, figures and the main tables were visually inspected, while substantial portions of references, prompts, and trajectories were inspected from supplied text rather than page images |

Evidence labels used below:

- **[A] Author-reported:** stated in the paper.
- **[B] Directly observable:** visible in a supplied page rendering.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** a clearly marked inference rather than an author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

ReAct—short for **Reasoning and Acting**—is a prompting method for large language models (LLMs). Instead of asking a model only to think through a problem or only to execute actions, ReAct makes it alternate between:

1. a language-based thought;
2. an action in an external environment; and
3. the environment’s observation.

For example, a model answering a multi-hop question can state what it needs to find, search Wikipedia, inspect the returned text, revise its plan, search again, and finally answer. In a text game, it can reason that it must find an object, clean it, and place it somewhere, then track those subgoals while acting. [A: pp. 2–4, §§1–2; B: Fig. 1]

The addressed problem is that **reasoning-only** methods such as chain-of-thought (CoT) can invent facts and propagate mistakes, while **action-only** agents may act without understanding the goal, lose track of state, or repeat invalid commands. ReAct attempts to make reasoning grounded by external feedback and action purposeful through explicit planning. [A: pp. 2–3]

The authors evaluate it on four benchmarks:

- HotpotQA multi-hop question answering;
- FEVER fact verification;
- ALFWorld text-based household tasks;
- WebShop simulated online shopping. [A: pp. 3–8]

Main findings include:

- ReAct beats action-only prompting on all four evaluated benchmarks. [A: Tables 1, 3, and 4]
- Plain ReAct is better than plain CoT on FEVER but slightly worse on HotpotQA. [A: Table 1]
- Hybrid ReAct/CoT-self-consistency methods produce the best prompt-based results in Table 1. [A: pp. 5–6]
- ReAct’s best ALFWorld prompt obtains 71% success, versus 45% for Act and 37% for BUTLER. [A: Table 3]
- ReAct obtains 40.0% WebShop success, versus 30.1% for Act and 28.7–29.1% for the learned baselines. [A: Table 4]
- Manual trajectory analysis suggests ReAct reduces factual hallucination relative to CoT, but suffers more reasoning/search failures and occasional loops. [A: Table 2, p. 6]

The central contribution is therefore a general, prompt-based control format in which language reasoning and environmental interaction continuously inform one another.

# 2. Document Roadmap

## Document inventory

| ID | Original component | Pages | Role |
|---|---|---:|---|
| S1 | Abstract | 1 | Problem, method, headline results |
| S2 | §1 Introduction | 1–3 | Motivation, gap, contributions |
| S3 | §2 ReAct: Synergizing Reasoning + Acting | 3–4 | Formal framework and design |
| S4 | §3 Knowledge-Intensive Reasoning Tasks | 4–7 | HotpotQA and FEVER methodology/results |
| S5 | §4 Decision Making Tasks | 7–8 | ALFWorld and WebShop methodology/results |
| S6 | §5 Related Work | 9 | Positioning against reasoning and decision-making research |
| S7 | §6 Conclusion | 9–10 | Conclusions, limitations, future directions |
| S8 | Reproducibility and Ethics statements | 10 | Access limitations and interaction risks |
| S9 | References | 10–13 | Bibliography |
| A1 | Appendix A: Additional Results | 14–15 | GPT-3, current knowledge, human editing |
| A2 | Appendix B: Experiment Details | 15 | Fine-tuning and ReAct-IM details |
| A3 | Appendix C: Prompts | 16–25 | Full prompt examples for all tasks |
| A4 | Appendix D: Trajectories | 25–31 | FEVER, ALFWorld, and WebShop examples |
| A5 | Appendix E: More Analysis | 32–33 | Success/failure examples |

### Visual and formal inventory

- Figures: F1–F5.
- Tables: T1–T10.
- Formal expressions: agent policy/context and augmented action space in §2, p. 3.
- Algorithms/pseudocode: none presented as a numbered algorithm.
- Explicit hypotheses or formally numbered research questions: none.
- Distinct analyses: knowledge-task prompting, hybrid methods, failure-mode labeling, fine-tuning, ALFWorld, WebShop, ReAct-IM ablation, GPT-3 transfer, current-information example, human thought editing, and appendix trajectory analyses.

The main paper first motivates and defines ReAct, then tests it in two broad regimes: knowledge-intensive reasoning (§3) and long-horizon interactive decision-making (§4). The appendices supply robustness experiments, training details, actual prompts, and qualitative trajectories that materially clarify the main claims.

# 3. Background and Context

An **LLM** is the paper’s policy-generating model. The main experiments use frozen PaLM-540B with a small number of examples placed in the prompt; additional experiments use GPT-3 (`text-davinci-002`) and fine-tuned PaLM-8B/62B. [A: pp. 3, 5–7, 14–15]

**In-context or few-shot prompting** means demonstrating a task within the input rather than updating the model’s parameters. ReAct demonstrations contain thoughts, actions, and observations. [A: pp. 3–4]

**Chain-of-thought (CoT)** elicits intermediate verbal reasoning but does not retrieve external observations during that reasoning. **Self-consistency (CoT-SC)** samples several CoT trajectories and selects their majority answer. [A: p. 5]

An **action-only (Act)** prompt retains environmental actions and observations but removes the thoughts from a ReAct trajectory. This is the paper’s controlled test of whether explicit reasoning helps acting. [A: p. 5]

A **trajectory** is the ordered history of thoughts, actions, and observations for one task. An **observation** is feedback returned by Wikipedia, ALFWorld, or WebShop.

The paper distinguishes:

- **internal knowledge:** information encoded in model parameters and expressed through reasoning;
- **external knowledge/feedback:** information obtained by acting in an environment. [A: pp. 5–6, 8]

**Exact match (EM)** credits an answer only when it matches the reference answer under the benchmark’s criterion. **Accuracy** is used for FEVER; **success rate (SR)** is used for ALFWorld and WebShop. WebShop additionally uses a partial-credit score: the percentage of requested attributes satisfied, averaged across episodes. [A: pp. 5, 7]

# 4. Research Problem and Gap

## Existing problem

LLMs had shown reasoning ability and action generation, but these capabilities were mainly studied separately. [A: Abstract, p. 1]

## Shortcomings attributed to prior approaches

- Reasoning-only CoT is not externally grounded and can hallucinate facts or propagate an early error. [A: p. 2]
- Action-generation methods often map observations directly to actions without abstract goal decomposition or working memory. [A: p. 2]
- Inner Monologue supplies dense environmental feedback but, in the authors’ account, does not offer ReAct’s flexible internal reasoning. [A: pp. 8–9]
- Learned interactive agents may require many human trajectories, task instances, or reinforcement-learning feedback. [A: pp. 7–9]

## Research gap

The authors identify a lack of systematic study of whether free-form reasoning and environmental action can be combined synergistically across both reasoning and interactive decision tasks. [A: p. 2]

## Motivation

Reasoning can decide what action to take, maintain plans, and recover from exceptions; actions can acquire information that corrects or extends reasoning. The human cooking analogy illustrates this two-way relationship. [A: pp. 1–2]

## Scope

The empirical scope is four language-based benchmarks and primarily frozen PaLM-540B few-shot prompting. It does not evaluate unrestricted physical-world action or a general web browser. [A: pp. 3–8, 10]

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or hypotheses. Its explicit and implicit objectives are:

- Determine whether interleaving thoughts, actions, and observations improves over reasoning-only and action-only prompting.
- Test generality across question answering, fact verification, text games, and shopping navigation.
- Determine how internal model knowledge and externally retrieved information complement each other.
- Analyze ReAct’s success and failure modes, including hallucination, search failure, and reasoning loops.
- Test whether ReAct benefits from fine-tuning and transfers across LLMs.
- Explore interpretability and human correction through editable reasoning traces. [A: pp. 2–4, 6, 14–15]

No preregistered or statistical null hypotheses are supplied.

# 6. Assumptions / Threat Model

This is not a security paper and defines no conventional attacker threat model.

## System and environmental assumptions

- At each step, the environment returns an observation and accepts an action from a permitted action space. [A: p. 3]
- Thoughts update the model’s context but do not directly affect the external environment. [A: p. 3]
- The LLM possesses sufficiently strong language priors to use an effectively unbounded thought space. [A: p. 3]
- Wikipedia retrieval depends on exact page names or lookup strings and is intentionally weaker than state-of-the-art retrievers. [A: p. 4]
- ALFWorld and WebShop expose textual observations and constrained actions.
- Few demonstrations are assumed to fit within the model input length, although the conclusion acknowledges this can fail for large action spaces. [A: pp. 4, 9–10]

## Safety boundary

The experiments restrict interaction to Wikipedia, the WebShop research environment, and simulated ALFWorld. Models cannot edit Wikipedia, make real purchases, or execute dangerous physical actions. The authors nevertheless warn that more capable agents could retrieve private/inappropriate information or take harmful actions. [A: Ethics Statement, p. 10]

# 7. Methodology

## Core framework

At time \(t\), the agent observes \(o_t\), chooses \(a_t\) using policy \(\pi(a_t\mid c_t)\), and conditions on the trajectory context

\[
c_t=(o_1,a_1,\ldots,o_{t-1},a_{t-1},o_t).
\]

ReAct augments the environmental action space \(A\) with a language space \(L\):

\[
\hat A=A\cup L.
\]

A language action \(\hat a_t\in L\) is a thought. It changes the next context to \(c_{t+1}=(c_t,\hat a_t)\) but yields no environmental observation. [A: §2, p. 3]

For knowledge tasks, thoughts and actions alternate densely. For long-horizon decision tasks, thoughts occur sparsely at positions chosen by the model. [A: pp. 3–4]

## Models and decoding

- Main prompting model: frozen PaLM-540B.
- CoT-SC: 21 sampled CoT trajectories, temperature 0.7, majority answer.
- Most reported prompting uses greedy decoding.
- Table 3 notes that all compared ALFWorld methods use greedy decoding except BUTLER, which uses beam search.
- GPT-3 appendix model: `text-davinci-002`, greedy decoding. [A: pp. 3, 5, 8, 14]

No hardware, random seed, software version, confidence interval, or significance-test procedure is reported in the supplied paper.

## HotpotQA and FEVER

Both use a question-only setup: no gold supporting passages are given. [A: p. 4]

Wikipedia API actions:

- `search[entity]`: first five sentences of the page, or five similar entity suggestions;
- `lookup[string]`: next matching sentence on the current page;
- `finish[answer]`: terminate with an answer. [A: p. 4]

Demonstrations:

- HotpotQA: six manually written ReAct trajectories.
- FEVER: three manually written trajectories.
- The authors report that more demonstrations did not help. [A: pp. 4–5 and footnote 2]

Baselines are Standard, CoT, CoT-SC, and Act. Hybrid methods switch between ReAct and CoT-SC:

- **ReAct → CoT-SC:** fall back when ReAct fails to answer within seven HotpotQA steps or five FEVER steps.
- **CoT-SC → ReAct:** switch when the CoT majority appears fewer than \(n/2\) times. [A: p. 5]

## Fine-tuning

The authors bootstrap 3,000 correctly answered ReAct-generated trajectories to fine-tune PaLM-8B and PaLM-62B. Batch size is 64. [A: pp. 5, 15]

- PaLM-8B: ReAct/Act for 4,000 steps; Standard/CoT for 2,000.
- PaLM-62B: ReAct/Act for 4,000 steps; Standard/CoT for 1,000.

The target is to decode complete trajectories from questions or claims. [A: Appendix B.1, p. 15]

## ALFWorld

- Six task types.
- 134 unseen evaluation games.
- Three annotated training trajectories per type.
- Each prompt uses two trajectories; all six permutations of two among the three form six prompt trials.
- Thoughts support goal decomposition, progress tracking, next-subgoal selection, and commonsense search.
- Act uses the same trajectories with thoughts removed.
- Principal learned baseline: BUTLER, trained on \(10^5\) expert trajectories per task type. [A: p. 7]

## WebShop

- Environment: 1.18 million products and 12,000 human instructions.
- Evaluation: 500 test instructions.
- Conditions: one-shot Act and ReAct.
- Baselines: imitation learning (IL) trained on 1,012 human trajectories and IL+reinforcement learning (RL) additionally trained on 10,587 instructions.
- Metrics: average attribute score and exact success rate. [A: pp. 7–8]

## Qualitative and diagnostic analyses

- Four groups of 50 HotpotQA trajectories—correct and incorrect trajectories from each of ReAct and CoT—give 200 manually labeled examples. [A: p. 6]
- ReAct-IM substitutes dense, restricted feedback-like thoughts for flexible reasoning.
- Appendices provide cross-model, current-information, human-editing, and trajectory examples.

# 8. Experiments / Analyses

## X1 — Knowledge-task prompting

Purpose: compare ReAct with Standard, CoT, CoT-SC, Act, and supervised state-of-the-art references.

Results: see Table 1. ReAct beats Act on both datasets; plain ReAct beats CoT on FEVER but not HotpotQA. Hybrid approaches are best among prompting methods. [A: pp. 5–6]

Caveat: supervised systems remain much stronger: 67.5 HotpotQA EM and 89.5 FEVER accuracy. [A: Table 1]

## X2 — Hybrid internal/external reasoning

The two switching rules combine CoT-SC’s flexible internal reasoning with ReAct’s grounded retrieval. Figure 2 reports that the hybrids reach 21-sample CoT-SC performance with roughly 3–5 CoT samples and remain stronger across the displayed sample counts. Exact intermediate curve values are not labeled. [A: pp. 5–6; B: Fig. 2]

## X3 — HotpotQA error analysis

Sample: 200 trajectories. ReAct has fewer hallucinated successful traces and no hallucination-coded failures in this sample, but substantially more reasoning-error failures and a distinct search-error category. [A: Table 2]

This analysis describes error composition within manually selected groups, not population-wide error rates.

## X4 — Fine-tuning scale analysis

PaLM-8B/62B prompting and fine-tuning are compared with PaLM-540B prompting. ReAct performs poorly as a small-model prompt but best after 3,000-example fine-tuning. Exact bar heights other than textual comparisons are not labeled and should not be treated as exact. [A: p. 6; B: Fig. 3]

## X5 — ALFWorld

Across six prompt variants, ReAct’s best overall success is 71%, versus 45% for Act and 37% for BUTLER. Average ReAct is 57%. Its best trial is strongest in five of the six task columns; BUTLER reaches 100% on Cool. [A/B: Table 3]

## X6 — ReAct-IM ablation

Best ReAct reaches 71% overall versus 53% for best ReAct-IM, with ReAct better in five of six task types. The proposed explanation is that restricted dense feedback lacks subgoal-transition and commonsense-location reasoning. [A: pp. 8, 15]

## X7 — WebShop

ReAct: score 66.6, success 40.0%. Act: 62.3 and 30.1%. Learned baselines have lower success, while humans obtain 82.1 and 59.6%. [A/B: Table 4]

The appendix’s example yields 1.0 for ReAct versus 0.125 for Act because ReAct checks flavor, pack size, and price rather than buying the first superficially related item. [A/B: Table 10]

## X8 — Cross-model GPT-3 analysis

On a 500-question HotpotQA subset, GPT-3 ReAct scores 30.8 EM versus PaLM-540B’s 29.4. Across all 134 ALFWorld instances, GPT-3 scores 78.4% versus 70.9%. [A/B: Table 5]

The authors infer cross-model generality but note no repeated-run uncertainty.

## X9 — Up-to-date retrieval case

Figure 4 presents a HotpotQA label of 2,664 rooms. ReAct retrieves 2,884 rooms plus 220 suites and returns 3,104. [A/B: Fig. 4]

**[C] Arithmetic check:** \(2{,}884+220=3{,}104\).

This is a single illustrative case, not a systematic temporal-validity evaluation.

## X10 — Human thought editing

In Figure 5, removing a false belief from thought 17 and adding likely search locations in thought 23 redirects the agent from a failed drawer lookup to the dresser and successful completion. [A/B: Fig. 5]

The experiment is a demonstration, not a controlled user study.

# 9. Results

| Finding | Evidence and condition | Qualification |
|---|---|---|
| Reasoning improves acting on knowledge tasks | HotpotQA: ReAct 27.4 vs Act 25.7 EM; FEVER: 60.9 vs 58.9 accuracy (T1) | Gains are 1.7 and 2.0 percentage points [C] |
| Plain ReAct does not dominate plain CoT | HotpotQA: 27.4 vs 29.4; FEVER: 60.9 vs 56.3 (T1) | Task-dependent trade-off |
| Hybrid prompting is strongest | HotpotQA best: ReAct→CoT-SC 35.1; FEVER best: CoT-SC→ReAct 64.6 (T1) | Still far below supervised references |
| ReAct is more grounded in the manual sample | False-positive success traces: 6% vs 14%; hallucination failures: 0% vs 56% (T2) | Human-coded subsample; definitions are paper-specific |
| ReAct has more reasoning failures | 47% of sampled ReAct failure cases vs 16% for CoT (T2) | Includes repetition/failure to recover |
| Search quality is critical | Search-result error is 23% of ReAct failure cases (T2) | CoT has no comparable search category |
| ReAct improves ALFWorld success | Best: 71% vs Act 45% and BUTLER 37% (T3) | Best-of-prompt reporting differs from averages |
| ReAct improves WebShop success | 40.0% vs previous-best listed 30.1% (Act) (T4) | 9.9 percentage points from displayed values [C], described as 10% absolute |
| ReAct-IM is weaker | Best overall 53% vs ReAct 71% (T3) | Supports flexible internal reasoning, within one environment |
| ReAct transfers to GPT-3 | 30.8 vs 29.4 HotpotQA; 78.4 vs 70.9 ALFWorld (T5) | Model comparison is not controlled for training history |

### Important derived distinctions

- **[C] ALFWorld best ReAct vs Act:** \(71-45=26\) percentage points, not 34. The abstract’s “absolute success rate of 34%” corresponds to ReAct versus BUTLER: \(71-37=34\) points.
- **[C] WebShop ReAct vs Act:** \(40.0-30.1=9.9\) points, conventionally rounded to the paper’s 10-point claim.
- **[C] HotpotQA best prompting vs CoT-SC:** \(35.1-33.4=1.7\) points.
- **[C] FEVER best prompting vs CoT-SC:** \(64.6-60.4=4.2\) points.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Why thoughts and actions must be interleaved

- **Contents:** HotpotQA comparison of Standard, CoT, Act, and ReAct; ALFWorld comparison of Act and ReAct.
- **Visual form:** annotated trajectory panels, not an axis-based plot.
- **Flow:** question/state → thought or action → external observation → revised thought/action → answer/completion.
- **Observation:** CoT invents an overbroad Apple Remote answer; Act retrieves information but cannot synthesize the required final answer; ReAct searches, handles an entity-resolution failure, and answers “keyboard function keys.”
- **ALFWorld panel:** Act repeatedly tries to take a nonexistent pepper shaker from a sink basin; ReAct searches likely locations, updates its subgoal after finding the object, opens the drawer, and places it.
- **Support:** qualitative mechanism for “reason to act” and “act to reason.”
- **Caveat:** curated examples demonstrate possibility, not frequency. [A/B: p. 2]

### Figure 2 — Performance versus number of CoT-SC trials

- **Panels:** HotpotQA EM and FEVER accuracy.
- **X-axis:** number of CoT-SC trials, 0–20.
- **Y-axes:** approximately 26–35 HotpotQA EM and 47.5–65 FEVER accuracy.
- **Encoding:** lines for CoT-SC→ReAct, ReAct→CoT-SC, CoT-SC, ReAct, and CoT.
- **Main observation:** hybrid curves rise quickly and generally remain above plain CoT-SC; the paper states they match 21-sample CoT-SC with 3–5 samples.
- **Exactness:** endpoints corresponding to Table 1 are reported; intermediate values are approximate visual positions.
- **Caveat:** no error bars or run variability are shown. [A/B: pp. 5–6]

### Figure 3 — Model scale and prompting versus fine-tuning

- **Plot type:** grouped bar chart.
- **X-axis:** PaLM size—8B, 62B, 540B where available.
- **Y-axis:** HotpotQA EM, approximately 0–30+.
- **Panels:** `learning = prompt` and `learning = finetune`.
- **Legend:** Standard, CoT, Act, ReAct.
- **Main observation:** small-model prompted ReAct is weak, while fine-tuned ReAct becomes strongest at 8B and 62B.
- **Textual claims:** fine-tuned 8B ReAct exceeds all 62B prompting methods; fine-tuned 62B ReAct exceeds all 540B prompting methods.
- **Exactness:** individual bar heights are not numerically labeled and are therefore only visually approximate.
- **Caveat:** methods receive different numbers of fine-tuning steps because Standard/CoT degrade earlier. [A/B: pp. 6–7, 15]

### Figure 4 — ReAct obtains current information

- **Contents:** Standard, CoT, Act, and ReAct trajectories for a hotel-room question.
- **Dataset label:** 2,664.
- **Model outputs:** Standard 3,000; CoT 2,885; Act gives no answer; ReAct retrieves 2,884 rooms and 220 suites and answers 3,104.
- **Meaning:** reasoning guides retrieval, while retrieval updates an obsolete static answer.
- **Caveat:** whether “rooms” should include suites is not independently adjudicated within the paper; the authors call 3,104 reasonable and current. [A/B: p. 14]

### Figure 5 — Human-in-the-loop thought correction

- **Panels:** original failed ReAct trajectory and trajectory after two thought edits.
- **Original failure:** it hallucinates that a second keychain is in drawer 4.
- **Edit:** delete that belief and add likely locations, including the dresser.
- **Outcome:** the agent finds keychain 2 in dresser 1 and places it in the safe.
- **Meaning:** editing a small amount of explicit reasoning can redirect later actions.
- **Caveat:** one hand-selected example; no usability, time, or success-distribution study is reported. [A/B: pp. 14–15]

# 11. Table-by-Table Interpretation

### Table 1 — PaLM-540B on HotpotQA and FEVER

Rows are prompting methods; columns are HotpotQA EM and FEVER accuracy.

- HotpotQA prompting best: ReAct→CoT-SC, 35.1.
- FEVER prompting best: CoT-SC→ReAct, 64.6.
- Plain ReAct: 27.4/60.9.
- Plain Act: 25.7/58.9.
- Supervised references: 67.5/89.5.
- Footnote: previously reported HotpotQA values for Standard/CoT/CoT-SC are 27.1/28.9/33.8, slightly different from 28.7/29.4/33.4 here.
- No uncertainties or significance statistics are supplied. [A/B: p. 5]

### Table 2 — HotpotQA success and failure modes

Percentages are compositions of manually sampled correct/incorrect trajectories.

- Successful ReAct traces: 94% true-positive, 6% false-positive.
- Successful CoT traces: 86%/14%.
- ReAct failures: 47% reasoning, 23% search, 0% hallucination, 29% label ambiguity.
- CoT failures: 16% reasoning, 56% hallucination, 28% label ambiguity.
- ReAct failure percentages sum to 99%, presumably due to displayed integer rounding; the paper does not explain this explicitly.
- Categories are not symmetric because CoT cannot incur retrieval failure. [A/B: p. 6]

### Table 3 — ALFWorld success rates

Columns are Pick, Clean, Heat, Cool, Look, Pick 2, and overall (`All`), in percent.

- Best ReAct: 92, 58, 96, 86, 78, 41; overall 71.
- ReAct average: overall 57.
- Best Act: overall 45.
- Best ReAct-IM: 53.
- Best BUTLER: 37; BUTLER achieves the table maximum of 100 on Cool.
- ReAct and ReAct-IM are reported as average and best-of-six; Act only as best-of-six.
- BUTLER results are best-of-eight and one variant uses beam search, complicating direct procedural equivalence. [A/B: p. 8]

### Table 4 — WebShop score and success

- ReAct: 66.6 score, 40.0% SR.
- Act: 62.3, 30.1%.
- IL: 59.9, 29.1%.
- IL+RL: 62.4, 28.7%.
- Human expert: 82.1, 59.6%.
- ReAct leads machine methods but remains 19.6 percentage points below humans in success. [C: \(59.6-40.0\)] [A/B: p. 8]

### Table 5 — PaLM-540B versus GPT-3 ReAct

- HotpotQA: 29.4 vs 30.8 EM on 500 sampled validation questions.
- ALFWorld: 70.9% vs 78.4% on 134 unseen instances.
- Uses greedy decoding and the prompt selected using PaLM performance.
- This demonstrates success on another model, but prompt selection is not independent of PaLM. [A/B: p. 14]

### Table 6 — WebShop Act and ReAct demonstrations

Both sides navigate the same deodorant task. ReAct adds two thoughts: shortlist plausible products, then verify scent and size before buying. It makes explicit how sparse reasoning bridges unstructured search text and structured options. This is prompt documentation, not a result table. [A/B: p. 22]

### Table 7 — ALFWorld Act prompt

Despite the caption “No thoughts are provided,” the displayed trajectory includes a late `think:` line after cleaning the lettuce. This is a **caption–content inconsistency** visible in both supplied text and rendering. The prompt otherwise lacks the early planning and progress thoughts seen in Table 8. [A/B: p. 23]

### Table 8 — ALFWorld ReAct prompt

Adds explicit goal decomposition, likely-location search, object acquisition, cleaning, and final placement tracking. It demonstrates sparse thoughts at subgoal boundaries rather than a thought before every action. [A/B: p. 24]

### Table 9 — ReAct-IM prompt

Uses dense repetitive statements of the current goal/subgoal. It omits likely-location reasoning and richer progress transitions. This operationalizes the restricted Inner-Monologue-style ablation. [A/B: p. 25]

### Table 10 — WebShop predicted trajectories

Act buys a $85, 100-pack strawberry-banana product and scores 0.125. ReAct inspects a $12.99 product, selects apple-cinnamon and pack-of-16 options, and scores 1.0. This illustrates attribute-level reasoning, but is a single selected example. [A/B: p. 31]

# 12. Diagram / Architecture Interpretation

The paper has no conventional block architecture diagram. Figure 1 supplies the effective process architecture:

```text
Task/question
    ↓
Current trajectory context
    ↓
LLM policy chooses either:
    ├─ Thought → appended to context, no environment change
    └─ Action  → environment/API executes it
                    ↓
               Observation
                    ↓
             Updated context
                    ↺
```

The key feedback loop is bidirectional:

- **Reason to act:** thoughts decompose the goal, choose searches/actions, track state, and revise plans.
- **Act to reason:** observations supply evidence that changes subsequent thoughts.

For reasoning tasks, the loop generally follows Thought → Action → Observation repeatedly. For decision tasks, several physical/interface actions may occur between sparse thoughts. [A: §§1–2; B: Fig. 1]

# 13. Equations and Mathematical Concepts

## Agent policy and context

\[
a_t\sim\pi(a_t\mid c_t),\qquad
c_t=(o_1,a_1,\ldots,o_{t-1},a_{t-1},o_t).
\]

- \(t\): current time step.
- \(o_t\in O\): current environmental observation.
- \(a_t\in A\): environmental action.
- \(c_t\): full interaction history available to the model.
- \(\pi\): policy mapping context to an action distribution.

Plainly: the next action depends on everything the model has observed and done so far. [A: §2, p. 3]

## Augmented action space

\[
\hat A=A\cup L.
\]

- \(A\): environment-changing actions.
- \(L\): free-form language thoughts.
- \(\hat A\): combined choice space.

If \(\hat a_t\in L\), then:

\[
c_{t+1}=(c_t,\hat a_t).
\]

The thought changes the information available for the next decision but not the external world. No learned loss function, theorem, convergence result, or optimization objective is introduced.

## Hybrid switching threshold

CoT-SC→ReAct switches when the majority answer occurs fewer than \(n/2\) times among \(n\) samples. This treats weak voting agreement as a heuristic indication that internal knowledge may be unreliable. [A: p. 5]

# 14. Interpretation and Discussion

The evidence supports a **complementarity**, not universal dominance, claim. ReAct grounds answers through retrieval and makes plans visible, but its rigid interaction pattern can impede reasoning. CoT is flexible and performs slightly better on HotpotQA, yet its ungrounded facts lead to more hallucination in the sampled analysis. The hybrids are therefore central: they exploit CoT when internal reasoning is confident and ReAct when external evidence is needed. [A: pp. 5–6]

In interactive environments, thoughts function as working memory. The ALFWorld trajectories show that an agent must remember whether it has found, taken, cleaned, or placed an object. Action-only behavior can lose this state and repeat invalid commands. [A: pp. 27–30]

WebShop shows a related but distinct benefit: thoughts translate a natural-language request into a checklist of attributes and compare that checklist with noisy product titles and options. [A: pp. 7–8, 31]

**[D] Analyst interpretation:** The experiments collectively isolate two roles for reasoning: a state-management role in ALFWorld and a constraint-matching role in WebShop. That distinction is consistent with the supplied trajectories but is not explicitly formalized by the authors.

Notable unresolved points include:

- Table 7’s “No thoughts” caption conflicts with its late thought line.
- The abstract’s 34-point ALFWorld improvement refers to ReAct versus BUTLER, whereas the most controlled same-prompt comparison with Act is 26 points.
- “Significantly” is used descriptively, but no inferential tests, confidence intervals, or repeated-run uncertainty are supplied.
- Prompt selection and best-of-\(k\) reporting make some comparisons less direct.

# 15. Contributions and Novelty

## Conceptual

A unified view of language thoughts and environment actions as choices within one augmented action space. [A: §2]

## Methodological

A prompt format that interleaves thought, action, and observation without modifying the base model. [A: pp. 2–4]

## Algorithmic

Heuristic switching between ReAct and CoT-SC based on interaction failure or voting uncertainty. [A: p. 5]

## Experimental

Evaluation across four benchmarks spanning retrieval-based reasoning and long-horizon decision-making. [A: pp. 3–8]

## Analytical

Manual failure taxonomy contrasting groundedness, hallucination, search failure, reasoning error, and label ambiguity. [A: Table 2]

## Human-interaction contribution

An initial demonstration that users can redirect behavior by editing thoughts rather than issuing many replacement actions. [A: Fig. 5]

There is no new dataset, theorem, or standalone trained architecture claimed.

# 16. Limitations

## Authors' stated limitations

- ReAct’s structured alternation can reduce reasoning flexibility and induce repetitive loops. [A: p. 6]
- Retrieval failures account for a meaningful share of errors and are difficult to recover from. [A: p. 6]
- Small models struggle to learn both reasoning and acting from few in-context examples. [A: p. 6]
- Complex, large-action-space tasks may require more demonstrations than fit within the context window. [A: pp. 9–10]
- Prompting results remain far below domain-specific supervised systems. [A: pp. 6, 8]
- WebShop agents remain substantially below human performance and conduct fewer product explorations/query reformulations. [A: p. 8]
- PaLM is not openly accessible, limiting reproducibility. [A: p. 10]
- Larger-scale human editing/alignment evaluation is left for future study. [A: p. 15]
- Environment-connected models may retrieve inappropriate/private information or execute harmful actions. [A: p. 10]

## Additional evidence-based analyst observations

- **[D]** No confidence intervals, statistical tests, or random-seed variability are reported.
- **[D]** Best-of-six and best-of-eight comparisons may overstate performance relative to single-prompt deployment.
- **[D]** Hand-written demonstrations and qualitative examples permit selection effects.
- **[D]** The 200-trajectory taxonomy is balanced by correctness and method rather than sampled in natural outcome proportions, so its percentages should not be read as overall incident prevalence.
- **[D]** The four benchmarks use constrained textual interfaces; this limits conclusions about open-web or physical-world autonomy.
- **[D]** Exposed thoughts may improve inspection without necessarily being faithful causal explanations of the model’s internal computation; the paper does not test faithfulness directly.

# 17. Threats to Validity

## Internal validity

The Act comparison is strong where prompts derive from identical trajectories with thoughts removed. However, differing decoding methods, training resources, fine-tuning schedules, and best-of-trial selection complicate some baseline comparisons.

## Construct validity

EM can classify a reasonable current answer as wrong when a dataset label is obsolete. Table 2 also shows label-format ambiguity. WebShop’s score and SR operationalize attribute satisfaction but may not capture all real shopping concerns.

## Statistical conclusion validity

No uncertainty estimates or formal significance analyses are reported. “Significant” should therefore be read as the authors’ characterization of performance gaps, not proof from a stated hypothesis test.

## External and ecological validity

Wikipedia search, ALFWorld, and WebShop are bounded environments. Real web browsing and physical action introduce broader ambiguity, safety risks, interface failures, and irreversible consequences.

## Reproducibility

Prompts and some GPT-3 code are provided, but PaLM-540B was not openly available. Exact software stack, hardware, random seeds, and full evaluation code configuration are not documented in the supplied text.

## Generalizability

Appendix A.1 supports transfer across two large model families and two tasks, but this is limited evidence for the stronger notion of broad model/task generality.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Train ReAct using more high-quality human annotations.
- Scale to multitask training and additional tasks.
- Combine ReAct with reinforcement learning.
- Improve decoding, potentially with beam search, to reduce loops.
- Combine human feedback with the method.
- Study human thought editing and alignment more systematically.
- Extend interactive agents cautiously while addressing safety risks. [A: pp. 3, 6, 9–10, 15]

## B. Additional open questions

- **[D]** Are displayed thoughts faithful explanations or merely useful intermediate text?
- **[D]** How robust is ReAct to adversarial, misleading, stale, or conflicting observations?
- **[D]** What switching policy outperforms the paper’s fixed heuristics?
- **[D]** How do latency, token cost, and environment-call cost compare with CoT-SC or trained agents?
- **[D]** Can automated verification detect contradictions between thoughts and observations?
- **[D]** Does human editing remain efficient and safe across many users and long trajectories?
- **[D]** How much performance comes from prompt content versus the interleaving format itself?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| ReAct | Interleaved reasoning and acting |
| LLM | Large language model |
| CoT | Chain-of-thought: reasoning text without external actions |
| CoT-SC | CoT with self-consistency voting over sampled trajectories |
| Act | Action-and-observation prompting with thoughts removed |
| ReAct-IM | Restricted Inner-Monologue-style ablation |
| Thought/reasoning trace | Language action appended to context without changing the environment |
| Action | Command that queries or changes the external environment |
| Observation | Environment feedback following an action |
| Trajectory | Ordered sequence of thoughts, actions, and observations |
| Few-shot/in-context learning | Learning task behavior from demonstrations in the prompt |
| Dense thought | Thought-action-observation alternation used in reasoning tasks |
| Sparse thought | Thoughts inserted mainly at important subgoal boundaries |
| Groundedness | Reasoning tied to externally retrieved or observed evidence |
| Hallucination | Unsupported or invented fact/reasoning content |
| HotpotQA | Multi-hop question-answering benchmark |
| FEVER | Fact-verification benchmark with SUPPORTS, REFUTES, and NOT ENOUGH INFO labels |
| ALFWorld | Text-based simulated household task environment |
| WebShop | Simulated shopping website benchmark |
| EM | Exact-match answer metric |
| SR | Success rate |
| IL / RL | Imitation learning / reinforcement learning |
| \(o_t\) | Observation at time \(t\) |
| \(a_t\) | Environmental action at time \(t\) |
| \(c_t\) | Interaction context/history |
| \(A\) | Environmental action space |
| \(L\) | Language/thought space |
| \(\hat A\) | Union of environmental and language action spaces |
| \(\pi(a_t\mid c_t)\) | Policy for selecting an action from context |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| ReAct HotpotQA | 27.4 | EM | PaLM-540B prompting | Author-reported | p. 5, T1 |
| CoT HotpotQA | 29.4 | EM | PaLM-540B prompting | Author-reported | p. 5, T1 |
| Best prompt HotpotQA | 35.1 | EM | ReAct→CoT-SC | Author-reported | p. 5, T1 |
| ReAct FEVER | 60.9 | accuracy | PaLM-540B prompting | Author-reported | p. 5, T1 |
| Best prompt FEVER | 64.6 | accuracy | CoT-SC→ReAct | Author-reported | p. 5, T1 |
| Supervised HotpotQA/FEVER | 67.5 / 89.5 | EM / accuracy | Reference systems | Author-reported | p. 5, T1 |
| Manual analysis sample | 200 | trajectories | 50 correct and 50 incorrect per method | Author-reported | p. 6 |
| ReAct/CoT false-positive successes | 6 / 14 | % | Manual HotpotQA sample | Author-reported | p. 6, T2 |
| ReAct/CoT reasoning failures | 47 / 16 | % | Manual failure samples | Author-reported | p. 6, T2 |
| ReAct/CoT hallucination failures | 0 / 56 | % | Manual failure samples | Author-reported | p. 6, T2 |
| ReAct search failures | 23 | % | Manual ReAct failure sample | Author-reported | p. 6, T2 |
| Fine-tuning trajectories | 3,000 | trajectories | Correct generated examples | Author-reported | p. 5 |
| Fine-tuning batch size | 64 | examples | PaLM-8B/62B | Author-reported | p. 15 |
| ALFWorld evaluation size | 134 | games | Unseen evaluation games | Author-reported | p. 7 |
| Best ReAct ALFWorld | 71 | % success | Best of six prompts | Author-reported | p. 8, T3 |
| Best Act ALFWorld | 45 | % success | Best of six prompts | Author-reported | p. 8, T3 |
| Best BUTLER ALFWorld | 37 | % success | Best of eight | Author-reported | p. 8, T3 |
| ReAct–Act ALFWorld gap | 26 | percentage points | \(71-45\) | Analyst-derived | p. 8, T3 |
| ReAct–BUTLER gap | 34 | percentage points | \(71-37\) | Analyst-derived | p. 8, T3 |
| WebShop product/instruction pool | 1.18M / 12k | products/instructions | Environment | Author-reported | p. 7 |
| WebShop test size | 500 | instructions | Evaluation | Author-reported | p. 7 |
| ReAct WebShop | 66.6 / 40.0 | score / % SR | One-shot prompt | Author-reported | p. 8, T4 |
| Act WebShop | 62.3 / 30.1 | score / % SR | One-shot prompt | Author-reported | p. 8, T4 |
| ReAct–Act WebShop SR gap | 9.9 | percentage points | \(40.0-30.1\) | Analyst-derived | p. 8, T4 |
| Human WebShop | 82.1 / 59.6 | score / % SR | Human expert | Author-reported | p. 8, T4 |
| GPT-3 HotpotQA | 30.8 | EM | 500-question subset | Author-reported | p. 14, T5 |
| GPT-3 ALFWorld | 78.4 | % success | 134 instances | Author-reported | p. 14, T5 |
| Figure 4 current total | 3,104 | rooms+suites | \(2,884+220\) | Analyst-derived | p. 14, F4 |
| Table 10 scores | 0.125 / 1.0 | score | Act / ReAct example | Visually readable | p. 31, T10 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Interleaved reasoning helps action selection | ReAct exceeds Act on all four benchmarks | T1, T3, T4; X1, X5, X7 | pp. 5–8 | Strong within supplied benchmarks |
| External retrieval reduces hallucination | 6% vs 14% false-positive successes; 0% vs 56% hallucination failures | T2; X3 | p. 6 | Moderate; manually labeled subsample |
| ReAct trades flexibility for groundedness | ReAct has 47% reasoning-error share vs CoT’s 16% | T2 | p. 6 | Moderate; category definitions and selected sample constrain inference |
| Internal and external knowledge are complementary | Hybrid methods lead Table 1 and Figure 2 | T1, F2; X2 | pp. 5–6 | Strong comparative evidence, no uncertainty estimates |
| Sparse reasoning aids long-horizon control | ReAct 71% vs Act 45% and ReAct-IM 53% | T3; X5–X6 | p. 8 | Strong in ALFWorld; best-prompt selection matters |
| ReAct aids noisy attribute matching | 40.0% WebShop SR and successful appendix example | T4, T10 | pp. 8, 31 | Quantitative benchmark plus qualitative illustration |
| Fine-tuning teaches transferable interaction skills | Fine-tuned ReAct leads the compared small-model methods | F3; X4 | pp. 6–7 | Supported directionally; exact bar values and uncertainty absent |
| ReAct works across model families | GPT-3 exceeds PaLM in two ReAct tests | T5; X8 | p. 14 | Limited cross-model evidence |
| ReAct enables human correction | Two thought edits redirect one failed trajectory | F5; X10 | pp. 14–15 | Proof of concept, not systematic evidence |
| ReAct is more interpretable/trustworthy | Thoughts separate internal reasoning from observations | F1, trajectories, T2 | pp. 2–8 | Interpretability is demonstrated qualitatively; no user study |

# 22. Very Simple Explanation

Imagine an AI trying to answer a tricky question or complete a task in a virtual kitchen. One option is to let it “think” without checking anything. It may reason well, but it can also confidently invent facts. Another option is to let it click, search, or move objects without explaining its plan. Then it may wander around, forget what it has done, or repeat mistakes.

ReAct combines the two. The AI might say, “First I need to find the knife,” search likely places, observe where the knife actually is, then say, “Now I must clean it,” and continue. Its thoughts help organize its actions, while the results of its actions keep its thoughts connected to reality.

Across four tests, this generally worked better than acting without thoughts. It was especially helpful in long tasks and shopping tasks with many requirements. It was not perfect: searches could fail, the AI could get stuck repeating itself, and ordinary chain-of-thought was still slightly better on one question-answering benchmark. The best results often came from combining ReAct with chain-of-thought voting.

The big idea is simple: an AI agent should not only think and should not only act. It should think about what to do, act to obtain evidence, and then use that evidence to think again.

# Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract and §1 Introduction | Yes, text and rendered pp. 1–3 | Yes | Fully represented | Problem, motivation, gap, claims |
| §2 ReAct framework | Yes, text and rendered pp. 3–4 | Yes | Fully represented | Formal policy/action-space definition included |
| §3.1 Setup | Yes | Yes | Fully represented | Datasets and API |
| §3.2 Methods | Yes | Yes | Fully represented | Prompts, baselines, hybrids, fine-tuning |
| §3.3 Results | Yes | Yes | Fully represented | T1–T3 and error analysis |
| §4 Decision Making Tasks | Yes | Yes | Fully represented | ALFWorld, WebShop, ReAct-IM |
| §5 Related Work | Yes | Yes | Represented in compressed form | Categories and positioning retained; individual citations compressed |
| §6 Conclusion | Yes | Yes | Fully represented | Claims, limitations, future work |
| Reproducibility statement | Yes | Yes | Fully represented | PaLM access and supplied prompt/code references |
| Ethics statement | Yes | Yes | Fully represented | Safety boundaries and risks |
| References | Yes, text only | Yes | Inspected but deliberately compressed | Bibliographic entries not individually restated |
| Explicit research questions | Yes | Yes | Fully represented | None formally stated; objectives reconstructed without manufacturing formal RQs |
| Formal hypotheses | Yes | Yes | Fully represented | None stated |
| Formal framework/equations | Yes | Yes | Fully represented | No additional major equations |
| Algorithms | Yes | Yes | Fully represented | No numbered algorithm/pseudocode |
| Figure 1 | Yes, visually | Yes | Fully represented | All task/method panels |
| Figure 2 | Yes, visually | Yes | Fully represented | Intermediate curve values marked non-exact |
| Figure 3 | Yes, visually | Yes | Fully represented | Bar values not invented |
| Figure 4 | Yes, visually | Yes | Fully represented | Arithmetic and label caveat included |
| Figure 5 | Yes, visually | Yes | Fully represented | Both original and edited paths |
| Tables 1–5 | Yes | Yes | Fully represented | Numerical conditions and caveats included |
| Tables 6–10 | Yes | Yes | Fully represented | Long trajectories compressed to their substantive contrasts |
| Appendix A.1 | Yes | Yes | Fully represented | GPT-3 comparison |
| Appendix A.2 | Yes | Yes | Fully represented | Current-information example |
| Appendix A.3 | Yes | Yes | Fully represented | Human thought editing |
| Appendix B.1–B.2 | Yes | Yes | Fully represented | Fine-tuning and IM setup |
| Appendix C.1–C.4 | Yes, mainly text | Yes | Represented in compressed form | Repetitive full prompt wording omitted |
| Appendix D.1 | Yes, text only | Yes | Represented in compressed form | FEVER examples summarized through their error patterns |
| Appendix D.2 | Yes, text only | Yes | Represented in compressed form | ReAct/Act/ReAct-IM knife trajectories compared |
| Appendix D.3 | Yes, text and rendered T10 | Yes | Fully represented | Scores and attribute reasoning retained |
| Appendix E.1 | Yes, text only | Yes | Represented in compressed form | Each success/failure category accounted for |
| Supplementary files | No separate files supplied | Yes | Missing from supplied material | No embedded or separate supplement was provided |

### Missing or inaccessible material

- No page of the 33-page paper is missing in text.
- Pages 10–13, 16–21, 26–30, and 32–33 were not supplied as rendered images; their typography and layout could not be visually audited.
- The linked project pages, code repositories, executable environments, models, and source datasets were referenced but not supplied and were not inspected.
- No independent supplementary file was supplied.
- Hardware, random seeds, full software versions, run-level outputs, confidence intervals, and statistical-test details are not specified in the supplied paper.

### Uncertain interpretations

- Figure 2’s intermediate curve values and Figure 3’s bar heights are not numerically labeled; only trends and author-stated comparisons are reported confidently.
- Table 2’s ReAct failure percentages total 99%, likely from rounding, but the paper does not explicitly confirm this.
- Table 7’s caption says no thoughts are provided, while its content contains one `think:` step.
- Figure 4 treats suites as part of the requested hotel-room total; the paper presents this as reasonable but supplies no independent label-adjudication rule.
- “Significantly” cannot be mapped to a reported statistical test because none is supplied.

### Deliberately compressed material

- The complete bibliography was reduced to the prior-work categories that affect the paper’s positioning.
- Full word-for-word prompts in Appendix C were compressed into their formats, demonstration counts, and substantive distinctions.
- Repetitive action sequences in Appendices D and E were compressed while preserving each reported success/failure mechanism.
- Administrative acknowledgments were not reproduced beyond noting funding and the reproducibility/ethics statements; they do not alter the method or results.

### Potential omissions

No substantive numbered section, figure, table, formal expression, experiment, contribution, author-stated limitation, or appendix identified in the inventory is knowingly absent from this analysis. Non-rendered pages were analyzed from supplied native text, and that difference in inspection mode has been disclosed.