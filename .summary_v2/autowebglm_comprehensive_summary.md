# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–12; all page-labeled text supplied |
| Apparently missing pages | None |
| Native text | Available for every page; no page is identified as scanned or unusually text-poor |
| Visually rendered pages | Pages 1–9 and 11–12 |
| Page not visually rendered | Page 10, containing references only |
| Figures and diagrams | Figures 1–6 visually inspectable |
| Tables | Tables 1–8 visually inspectable and readable |
| Equations | Equations in §§3.1 and 4.2 are readable from supplied text and rendered pages, although mathematical typography remains OCR/extraction-sensitive |
| Algorithm | Algorithm 1 is visually inspectable and readable, with minor apparent pseudocode naming/typographic issues |
| Appendices | Appendices A–E are present on pp. 11–12 |
| Supplementary material | No separate supplementary file was supplied or expressly identified |
| External artifacts mentioned but not supplied | GitHub code/model/data release; Chrome extension; collected datasets; benchmark files; browser environments; external websites and cited papers |
| OCR required | No; native extraction is available. Visual inspection was used to check substantive rendered content |
| Principal limitations | The paper reports some methodological details only approximately; no raw data, code, trained model, evaluation traces, error-analysis sample size, hardware specification, random seeds, uncertainty estimates, or independent reproduction evidence is included in the supplied document |

**Evidence-status convention used below**

- **[A] Author-reported:** stated in the paper.
- **[B] Directly observable:** clearly readable from a supplied page image, figure, or table.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** an inference rather than an explicit author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

AutoWebGLM is a six-billion-parameter large language model adapted to operate websites. Rather than merely answering questions about text, it receives a task, a simplified representation of a webpage, the browser’s current position, and its previous actions; it then repeatedly chooses operations such as clicking, typing, scrolling, switching tabs, or finishing with an answer (§§3.1–3.2, pp. 3–5).

The problem is difficult because real webpages contain long and noisy HyperText Markup Language (HTML), vary greatly in layout and behavior, and require multi-step decisions in an open and unstable environment. According to the authors, prior agents also lacked a universal action space and adequate error recovery or self-checking (§1, p. 2).

The researchers built the system around ChatGLM3-6B and contributed four closely connected elements:

1. An interaction framework that prunes HTML, adds Optical Character Recognition (OCR) annotations, tracks position and history, exposes a standardized action vocabulary, and executes predicted actions.
2. A hybrid human–artificial-intelligence data pipeline for webpage-recognition, single-step, and complex multi-step tasks.
3. A three-stage training process: curriculum-based supervised fine-tuning (SFT), self-sampled Direct Preference Optimization (DPO) plus SFT, and environment-specific Rejection Sampling Fine-Tuning (RFT).
4. AutoWebBench, a bilingual English–Chinese benchmark for cross-task and cross-domain webpage navigation.

The principal reported results are:

- AutoWebBench: 64.8/58.6 Step Success Rate (SSR) on English cross-task/cross-domain and 65.4/61.8 on Chinese cross-task/cross-domain (Table 2, p. 8).
- Mind2Web: 59.5 average SSR (Table 3, p. 8).
- MiniWoB++: 89.3 success score, reported over 56 tasks and 100 episodes per task (Table 4 and §5.1, p. 8).
- WebArena: 18.2 (Table 4, p. 8).

Within the comparisons reported in the paper, AutoWebGLM substantially exceeds GPT-4 on all four AutoWebBench splits and on MiniWoB++ and WebArena, despite the latter being a proprietary model whose size is not given. On Mind2Web, AutoWebGLM exceeds GPT-4’s reported average but trails HTML-T5-XL. These comparisons require qualification because training status, candidate filtering, environment-specific RFT, and model access conditions differ across rows.

The central contribution is therefore not just a model checkpoint. It is an end-to-end recipe for making a relatively compact language model into a web agent: simplify the observation, construct executable training traces, teach progressively harder skills, learn from sampled mistakes, and specialize through successful environmental interaction.

# 2. Document Roadmap

The 12-page KDD 2024 paper is organized as follows:

| Part | Pages | Role |
|---|---:|---|
| Abstract and §1 Introduction | 1–3 | States the problem, challenges, proposed system, and contributions |
| §2 Related Work | 3 | Positions the work against language models, navigation benchmarks, web agents, prompt-generated data, and RFT |
| §3 AutoWebGLM as a Web Agent | 3–5 | Formalizes sequential interaction and defines the architecture, observations, actions, and HTML pruning |
| §4 Building AutoWebGLM | 5–8 | Explains hybrid data construction, curriculum SFT, self-sampled DPO, environment-specific RFT, and AutoWebBench |
| §5 Experiments | 8–9 | Reports benchmark results, execution efficiency, ablations, cases, and error categories |
| §6 Future Direction | 9 | Proposes multimodal input, better reasoning/self-checking, and mobile operation |
| §7 Conclusion | 9 | Restates the system and its claimed significance |
| References | 10 | Lists 45 cited works |
| Appendix A | 11 | Gives training hyperparameters and dataset sizes |
| Appendix B | 11 | Shows the inference prompt |
| Appendix C | 11 | Shows task- and intent-generation prompts |
| Appendix D | 11 | Describes human annotation |
| Appendix E | 11–12 | Supplies per-task MiniWoB++ results in Table 8 |

This is principally a mixed **machine-learning/AI, computer-systems, dataset, and benchmark paper**: it proposes an agent architecture, constructs data, trains a model, and evaluates it empirically.

# 3. Background and Context

A **large language model (LLM)** predicts language sequences from context. A **web-navigation agent** adds an interaction loop: observe a webpage, decide what to do, execute an action, observe the changed page, and continue until completion.

HTML represents a page’s structure and content as a tree of elements. Raw HTML can be too long and noisy for an LLM, so AutoWebGLM retains selected actionable or informative elements and nearby tree context (§3.2.1 and Algorithm 1, p. 4).

The major learning concepts are:

- **Supervised Fine-Tuning (SFT):** train the model to imitate correct task–action examples.
- **Curriculum Learning (CL):** introduce easier recognition and single-step material before complex planning traces.
- **Direct Preference Optimization (DPO):** train from preferred and rejected outputs—in this work, correct “gold” operations versus sampled erroneous operations.
- **Rejection Sampling Fine-Tuning (RFT):** sample complete trajectories in an environment, retain successful ones according to a reward signal, and fine-tune on them.
- **Chain of Thought (CoT):** intermediate reasoning or intent text. Here GPT-4 supplies a globally conditioned intent for every action in a human-recorded trace (§4.1.2, p. 6).
- **Trajectory/trace:** the sequence of observations and actions used to complete a task.
- **Step Success Rate (SSR):** the main per-step correctness metric used for AutoWebBench and Mind2Web. The supplied paper says evaluation follows Mind2Web but does not give a complete formula (§§4.3, 5.1, p. 8).

The benchmarks serve different purposes:

- **AutoWebBench:** the authors’ English–Chinese real-web trace benchmark.
- **Mind2Web:** offline complex-web evaluation using the MindAct evaluation framework.
- **MiniWoB++:** interactive simulated tasks, evaluated over 56 task types.
- **WebArena:** interactive virtualized real-website tasks intended to resemble real web use (§2, p. 3).

According to §2, earlier systems either concentrated on web-assisted question answering, needed many model calls per action, relied on extremely large models, or did not adequately solve complex real-world navigation.

# 4. Research Problem and Gap

## Existing problem

An effective web agent must understand heterogeneous pages, identify relevant controls, plan multi-step behavior, execute actions, and detect when actions fail (§§1, 3).

## Shortcomings attributed to previous approaches

The authors identify three high-level deficiencies (§1, p. 2):

- No universal action space covering operations across varied websites.
- Verbose, diverse, and complex webpage representations are difficult for LLMs.
- Existing agents inadequately infer, self-check, and escape erroneous action loops.

They also attribute more specific disadvantages to prior systems (§2, p. 3):

- MindAct may require more than ten model calls for one action.
- WebAgent depends on a reported 540B-scale Flan-U-PaLM model, complicating deployment.
- Existing models cannot reliably generate or annotate complex real-world trajectories without human help.
- Previously described RFT use centered on reasoning data rather than web-environment specialization.

## Research gap

The paper targets a deployable, open, relatively compact agent that unifies webpage representation, action execution, training-data creation, staged learning, and bilingual real-web evaluation.

## Motivation

Web automation could support routine information-seeking and action-oriented tasks, but real pages remain too varied and operationally demanding for many existing agents (§1, pp. 1–2).

## Scope

The evaluated scope covers desktop web navigation through simplified HTML, screenshots/OCR support, browser operations, four named benchmarks, English and Chinese pages, and limited real-world demonstrations. Mobile interaction, strongly visual applications, robust self-checking, and general multimodal processing are future directions rather than established capabilities (§6, p. 9).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper does **not** state formally numbered research questions.

## Explicit objectives

[A] The work seeks to:

1. Build an open, practically deployable web agent based on ChatGLM3-6B.
2. Preserve essential webpage information while reducing HTML complexity.
3. construct a large, reliable web-operation dataset efficiently through human–AI collaboration.
4. Develop general webpage understanding, operation, planning, and reasoning.
5. Let the model learn from its mistakes using self-sampled preference data.
6. Specialize it to particular environments using successful self-play traces.
7. Establish a bilingual real-web benchmark.
8. Compare the resulting agent with proprietary and open baselines across several benchmarks.

## Hypotheses

No preregistered or formally enumerated hypotheses appear. The authors do state one post hoc explanatory hypothesis in §5.3 (p. 8): complex-task data may improve performance because it more closely resembles real-world scenarios.

For analytical organization only, the experiments correspond to these **implicit objectives**, not author-formalized hypotheses:

- Whether AutoWebGLM performs competitively across AutoWebBench, Mind2Web, MiniWoB++, and WebArena.
- Whether simple and complex data stages contribute differently.
- Whether DPO and RFT add benefits beyond SFT.
- Which components dominate execution time.
- What failure modes remain.

# 6. Assumptions / Threat Model

This is not a security paper and defines no attacker threat model.

The operational model assumes (§§3.1–3.2, pp. 3–5):

- The current page can be represented by HTML, URL, and window position.
- An HTML parser can identify operable elements and assign usable identifiers.
- Screenshots and OCR can annotate visual text when needed.
- A browser automation program can faithfully execute generated operations.
- The action set in Table 1 is adequate for the evaluated tasks.
- Previous actions, tabs, viewport position, and task description fit into the model’s observation/prompt.
- The loop ends when `finish` is produced or a maximum length is reached; the maximum is not reported.
- MiniWoB++ supplies environmental completion judgments.
- WebArena completion can be judged by manually written rules.
- Reward signals are sufficiently reliable to select successful RFT traces.
- For the reported real-web data, human annotators can determine clarity, relevance, achievability, complexity, subjectivity, and task completion.

[D] Trusted infrastructure implicitly includes the parser, OCR module, browser plugin, executor, benchmark environment, and reward/checking rules. Failures in those components could be attributed to the model unless separately measured; the paper does not present such a decomposition.

# 7. Methodology

## 7.1 Sequential decision formulation

The state is:

\[
S=\{\mathrm{HTML},\mathrm{URL},\mathrm{Window\ Position}\},
\]

and the action set includes clicking, typing, scrolling, navigation, tab management, user interaction, and termination (§3.1, p. 3; Table 1, p. 4).

History is updated from the old history, prior action, and newly observed state. A policy chooses the next action conditioned on state and history; the browser transition function produces the next state. The process repeats until `finish` or a maximum horizon.

## 7.2 Interaction architecture

Figure 3 divides the system into:

1. **Data construction and training:** real/open-source sources, trace collection, hybrid human–AI construction, curriculum learning, reinforcement learning, and RFT.
2. **Interaction:** webpages produce screenshots and HTML; OCR and an HTML parser form a compact observation; AutoWebGLM predicts an action; an element selector/browser executor performs it; the resulting page returns to the observation loop.

The observation contains (§3.2.1, pp. 4–5):

- task description;
- simplified HTML;
- current window/page position;
- previous operations;
- existing tabs, as shown in Appendix B.

## 7.3 HTML pruning

Algorithm 1 begins with designated “kept” elements. Over a specified recursion count, it includes each kept node and bounded ancestors, descendants, and siblings. The depth, child, and sibling allowances are progressively reduced. A reverse tree pass removes nodes that were not selected or lack useful content/structure, while preserving the root (§3.2.1, p. 4).

The purpose is to shorten HTML without discarding important interactive and structural context.

## 7.4 Action space

Table 1 defines ten instructions:

- `click(id)`
- `hover(id)`
- `select(id, option)`
- `type_string(id, text, enter)`
- `scroll_page(direction)`
- `go(direction)`
- `jump_to(url, newtab)`
- `switch_tab(id)`
- `user_input(message)`
- `finish(answer)`

The prompt asks for one command plus a short explanatory comment (Appendix B, p. 11).

## 7.5 Data construction

The authors report an operation dataset of approximately 10,000 traces (§1, p. 2). Figure 5 partitions the training data as:

- complex task: 60, 38.71%;
- simple task: 42, 27.1%;
- web recognition: 40, 25.81%;
- MiniWoB: 6, 3.87%;
- Mind2Web: 7, 4.51%.

These displayed values sum to 155 and 100.00%. The unit behind 40/42/60/6/7 is not expressly printed; [D] they plausibly denote thousands of samples rather than traces, but the paper does not define the unit. Therefore they should not be equated uncritically with the “approximately 10,000 traces” contribution claim.

### Web-recognition data

URLs are collected from mainstream English and Chinese websites. The parser identifies actionable controls and records their position and size. The system produces simplified HTML. Recognition questions concern site functions, element types, and interface roles. GPT-3.5-Turbo paraphrases questions and generates length-limited answers (§4.1.1, p. 5).

### Single-step operation data

Sites are divided by operation type. Dataset volume is adjusted according to an operation’s practical frequency, although exact counts are absent. Rather than asking an LLM to invent entire executable demonstrations, the pipeline first identifies actionable page elements and operations, then asks GPT-3.5-Turbo to generate a task and intent corresponding to the known action. Fixed operations such as scrolling and URL jumping use templates; richer click/type operations receive model assistance (§4.1.1, pp. 5–6; Appendix C, p. 11).

### Complex-task data

For every website, the authors first generate 50 tasks using Evol-Instruct-inspired prompting, then manually select and label about 20 feasible tasks. Human annotators execute tasks using a Chrome plugin that records operations. GPT-4 receives the entire action trace plus critical HTML and generates an intent for each step in one global prompt (§4.1.2, p. 6).

The final training collection merges the new data with Mind2Web and MiniWoB++ training data.

### Human annotation

Twenty annotators worked for one month. They verified task–site alignment and assessed clarity, relevance, achievability, complexity, and subjectivity. They recorded login and CAPTCHA steps, manually edited answer responses, and could revise or abandon infeasible tasks (Appendix D, p. 11).

## 7.6 Three-stage training

### Stage 1: Curriculum SFT

Recognition and simple-operation examples precede complex planning traces. The reported SFT settings are:

- learning rate: \(10^{-5}\);
- batch size: 32.

The resulting model is denoted \(M_{\mathrm{SFT}}\) (§4.2.1, pp. 6–7; Appendix A, p. 11).

### Stage 2: Self-sampled DPO plus SFT

\(M_{\mathrm{SFT}}\) samples each complex training example 20 times. The authors retain examples solved between 1 and 19 times, excluding always-correct items as uninformative and never-correct items as possible outliers. Duplicate negative operations are removed. Correct gold operations and varied erroneous samples form contrastive data.

Reported settings:

- approximately 13,000 contrastive examples;
- DPO learning rate: \(10^{-6}\);
- batch size: 64;
- \(\beta=0.15\);
- auxiliary SFT weight: 0.8, although the displayed Eq. (4) uses the generic symbol \(\lambda\).

The result is \(M_{\mathrm{DPO}}\) (§4.2.2, p. 7; Appendix A, p. 11).

### Stage 3: RFT

For MiniWoB++, built-in query generation creates multiple tasks, with more queries for harder task types. Successful \(M_{\mathrm{DPO}}\) traces are retained according to the environment.

For WebArena, the researchers manually make queries distinct from the test set using task templates. Each sample is attempted 64 times; any successful trajectory according to manually written rules becomes positive training data.

Reported collections are:

- MiniWoB++: about 15,000 successful traces and 66,000 steps;
- WebArena: 240 successful traces and about 2,000 steps.

Appendix A calls these “successful datasets of approximately 66k and 2k,” apparently using step counts rather than trace counts. This is a **main-text–appendix terminology discrepancy**, not necessarily a numerical contradiction.

RFT uses learning rate \(10^{-5}\) and batch size 32. Separate fine-tuning is performed for MiniWoB++ and WebArena (§4.2.3, p. 7; Appendix A, p. 11).

## 7.7 AutoWebBench

The complex-task collection is split along language and generalization dimensions:

- English versus Chinese;
- cross-task/in-domain versus cross-domain/out-of-domain.

The prose alternates between “in-domain/out-of-domain” and Table 2’s “cross-task/cross-domain.” Fifty manually verified traces are selected for each of four splits, implying 200 test traces [C: \(4\times50=200\)] (§4.3 and §5.1, p. 8).

## 7.8 Baselines and evaluation

- AutoWebBench: GPT-3.5-Turbo, GPT-4, Claude2, LLaMA2-7B/70B, Qwen-7B; metric SSR.
- Mind2Web: several language/web models evaluated through MindAct; SSR. GPT-4 uses top-10 candidates, while other rows use top-50; starred models are fine-tuned.
- MiniWoB++: 56 tasks × 100 episodes per task, or 5,600 evaluation episodes [C].
- WebArena: the authors integrate their parser and executor with the environment.
- Execution efficiency: timing is divided into fetch, parse, predict, execute, and loading.
- Ablation: progressively adds Stage 1, Stage 2, DPO, and RFT.

## 7.9 Unreported configuration

The supplied work does not specify hardware, software/library versions, random seeds, number of independent training runs, validation splits, confidence intervals, statistical tests, variance, energy/cost, full dataset licensing, exact test websites, maximum trajectory length, or detailed reward-rule correctness checks.

# 8. Experiments / Analyses

## X1 — AutoWebBench evaluation

**Purpose:** Test bilingual real-web step accuracy and generalization.

**Setup:** Four 50-trace splits: English/Chinese crossed with cross-task/cross-domain; SSR metric.

**Result:** AutoWebGLM obtains 64.8, 58.6, 65.4, and 61.8, respectively (Table 2, p. 8). The best baseline in all four columns is GPT-4 at 38.6, 39.7, 36.7, and 36.3.

**Derived margins:** AutoWebGLM exceeds GPT-4 by 26.2, 18.9, 28.7, and 25.5 points, respectively [C].

**Caveat:** No uncertainty estimates or significance tests are reported, and the exact construction of SSR is deferred to the Mind2Web methodology rather than fully defined.

## X2 — Mind2Web evaluation

**Purpose:** Test offline generalization across tasks, websites, and domains.

**Setup:** MindAct evaluation; top-50 candidates except GPT-4, which uses top-10. Most trainable baselines are marked fine-tuned; AutoWebGLM’s row lacks the asterisk, although Mind2Web training data were merged into its training dataset (§4.1.2, p. 6). This makes the notation potentially confusing.

**Result:** AutoWebGLM scores 66.4 cross-task, 56.4 cross-website, 55.8 cross-domain, average 59.5 (Table 3).

HTML-T5-XL has the highest reported average, 66.9. AutoWebGLM is second in average and exceeds GPT-4’s 30.9 by 28.6 points [C]. AutoWebGLM exceeds HTML-T5-XL on cross-website only? No: 56.4 is below 62.2. It trails HTML-T5-XL in all three columns but exceeds all other listed averages.

**Caveat:** Candidate counts, fine-tuning, architecture sizes, and training sources differ.

## X3 — MiniWoB++ evaluation

**Purpose:** Measure interactive task completion.

**Setup:** 56 tasks, 100 evaluation episodes per task.

**Result:** AutoWebGLM averages 89.3, ahead of HTML-T5-XL’s 85.6, WebN-T5-XL’s 48.4, LLaMA2-70B’s 47.1, GPT-4’s 32.1, and GPT-3.5-Turbo’s 13.4 (Table 4, p. 8).

Table 8 shows AutoWebGLM obtains 1.00 on many task types but performs poorly on `enter-time` (0.00), `choose-list` (0.15), `click-checkboxes-soft` (0.37), `book-flight` (0.50), and `click-scroll-list` (0.57). HTML-T5-XL outperforms it on several visually or interaction-sensitive tasks, including `book-flight`, `click-checkboxes-soft`, `click-scroll-list`, and `enter-time`.

**Caveat:** AutoWebGLM’s MiniWoB++ result follows environment-specific RFT. Table 4 marks other fine-tuned models with an asterisk but does not mark AutoWebGLM, so readers must use the methods/ablation to understand its specialization.

## X4 — WebArena evaluation

**Purpose:** Measure end-to-end completion in virtualized real websites.

**Setup:** Parser/executor adapted to WebArena; RFT data constructed from non-test queries and successful samples.

**Result:** AutoWebGLM scores 18.2 versus GPT-4’s 14.4, GPT-3.5-Turbo’s 6.2, Lemur’s 5.3, and other reported baselines at 0.6–5.1 (Table 4).

**Caveat:** The absolute result remains low: [C] 81.8% of the benchmark’s full 100-point scale is not achieved, although the table does not explicitly define the values as percentages. The result follows domain-specific RFT, and no uncertainty is reported.

## X5 — Execution-efficiency analysis

**Purpose:** Identify latency bottlenecks.

**Result:** Average reported component times are fetch 436.93, parse 68.68, predict 2407.34, execute 20.36, and loading 2092.13 (Table 5, p. 8). The implied unit is not printed in the table or nearby prose, so it must be marked unspecified; it is plausibly milliseconds but cannot be asserted from this document alone.

The paper assigns 47.89% to prediction and 41.64% to loading, together 89.53% [C: \(47.89+41.64\)]. Execution itself is only 0.41%.

For `scroll_page`, prediction is slowest among listed action types at 3396.37; “Others” has the largest fetch and parse times, 680.50 and 152.50.

## X6 — Training-data ablation

**Purpose:** Measure effects of Stage 1 simple/recognition data and Stage 2 complex data.

**Results (Table 6, p. 9):**

- Only training set: Mind2Web 48.1, MiniWoB++ 44.3.
- +Stage 1: 23.5 AutoWebBench, 48.4 Mind2Web, 48.3 MiniWoB++, 2.5 WebArena.
- +Stage 2: 60.2, 55.2, 78.9, 7.6.
- +Stage 1+2: 61.8, 56.7, 81.7, 8.3.

Stage 2 supplies the larger improvement. Combining stages produces the best data-only scores. On MiniWoB++, Stage 1+2 exceeds Stage 2 alone by 2.8 points [C], supporting the authors’ explanation that simple data mitigate basic operational errors.

## X7 — Training-strategy ablation

**Purpose:** Isolate DPO and RFT.

- SFT: 61.8/56.7/81.7/8.3.
- +DPO: 62.7/59.5/80.8/8.5.
- +RFT: not applicable to AutoWebBench/Mind2Web; 89.3/18.2.
- Final AutoWebGLM: 62.7/59.5/89.3/18.2.

DPO improves AutoWebBench by 0.9, Mind2Web by 2.8, and WebArena by 0.2 points, but MiniWoB++ falls by 0.9 [C]. RFT then adds 8.5 MiniWoB++ points and 9.7 WebArena points over the DPO row [C]. Thus the table supports domain specialization more strongly than universal monotonic improvement from every stage.

## X8 — Case studies and errors

Figure 2 shows four qualitative examples: finding detailed weather, selecting a children’s Christmas gift, finding an article about LLMs, and finding a differential-equation tool.

Table 7 categorizes observed errors as hallucinations 44%, poor graphical recognition 28%, task-context misinterpretation 20%, and pop-up interruption 8%. The denominator and sampling protocol are not reported, so these figures describe the inspected error sample but cannot establish population-wide failure frequencies.

# 9. Results

| Finding | Evidence and comparison | Qualification |
|---|---|---|
| Strong bilingual AutoWebBench performance | 58.6–65.4 across four splits; GPT-4 36.3–39.7 (Table 2) | 50 traces per split; no uncertainty tests |
| Cross-domain degradation is present but limited within AutoWebBench | English: 64.8→58.6, −6.2 points; Chinese: 65.4→61.8, −3.6 points [C] | “Cross-task” is treated in prose as the familiar/in-domain condition |
| Competitive but not best Mind2Web average | 59.5 versus HTML-T5-XL 66.9; GPT-4 30.9 (Table 3) | Evaluation candidate and fine-tuning conditions differ |
| Best listed MiniWoB++ average | 89.3 versus HTML-T5-XL 85.6 and GPT-4 32.1 (Table 4) | Result follows MiniWoB++-specific RFT |
| Best listed WebArena score | 18.2 versus GPT-4 14.4 (Table 4) | Absolute completion remains modest; RFT is environment-specific |
| Complex traces are the most influential data stage | Stage 2 greatly raises all four available scores; Stage 1 alone adds little on Mind2Web/MiniWoB++ (Table 6) | Sequential rows do not provide uncertainty or fully factorial controls |
| Simple data complement complex data | Stage 1+2 beats Stage 2 on all reported columns by 1.5, 1.5, 2.8, and 0.7 points [C] | Supports complementarity, not necessarily a causal mechanism |
| DPO has mixed benchmark effects | +0.9 AutoWebBench, +2.8 Mind2Web, −0.9 MiniWoB++, +0.2 WebArena [C] | The authors summarize DPO positively; the table shows one small decline |
| RFT strongly improves its target environments | +8.5 MiniWoB++, +9.7 WebArena [C] | Not tested on AutoWebBench/Mind2Web because interactive sampling is unavailable |
| Model prediction and loading dominate latency | 47.89% and 41.64%; combined 89.53% [C] | Timing unit and hardware are unspecified |
| Hallucination is the largest recorded error class | 44% of analyzed errors (Table 7) | Error count and collection protocol absent |

The abstract’s claim that AutoWebGLM can “outperform GPT-4” is supported on the reported benchmark numbers, but it should not be read as an unconditional statement across all web tasks or evaluation regimes.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Cross-benchmark overview

- **Form:** radar/spider chart on p. 1.
- **Axes:** AutoWebBench English, WebArena, MiniWoB++, Mind2Web cross-domain, cross-website, and cross-task.
- **Legend:** GPT-3.5-Turbo, GPT-4, LLaMA2-70B, AutoWebGLM, and Human.
- **Encoding:** each colored polygon represents performance across axes.
- **Direct observation:** AutoWebGLM’s polygon generally extends beyond GPT-4, GPT-3.5-Turbo, and LLaMA2-70B; the human polygon remains larger on most axes.
- **Readable labels:** outer-axis values include 72.6, 75.0, 78.2, 93.5, 70.4, and 69.3, apparently human reference levels.
- **Caveat:** Exact model values should be taken from Tables 2–4, not estimated from polygon positions. Benchmarks use different metrics/settings, so the connected polygon is an overview rather than a single commensurate measurement.

## Figure 2 — Four browser-use examples

- **Panels:**  
  (a) search a daily detailed weather report;  
  (b) select a Christmas gift for children;  
  (c) find an article about LLMs;  
  (d) find a differential-equation tool.
- **Content:** browser screenshots paired with a right-side action/reasoning transcript.
- **Purpose:** demonstrate breadth across information search, shopping, research, and tool discovery.
- **Observation:** the interface shows sequential model actions alongside live pages.
- **Caveat:** These are selected cases, not controlled quantitative evidence. Fine transcript details are too small to audit fully from the supplied rendering.

## Figure 3 — System architecture

- **Inputs:** real-world/open-source data, manual/LLM-assisted annotation, and environment traces.
- **Training flow:** data construction → curriculum learning → reinforcement learning → rejection-sampling fine-tuning.
- **Interaction flow:** webpage → screenshot/HTML perception → OCR/parser → parsed HTML/history/task observation → AutoWebGLM → action → element selector/executor → updated webpage.
- **Feedback:** the execution–observation loop continues until termination.
- **Meaning:** training and runtime interaction are separate but connected: training produces the policy; the framework translates between heterogeneous pages and that policy.
- **Caveat:** The diagram does not expose deployment boundaries, asynchronous behavior, failure recovery, or component latency.

## Figure 4 — Data-construction pipeline

- **Stage 1:** pages are converted into recognition questions and single-step action examples. Templates handle fixed operations, while an LLM writes richer tasks/intents around known executable actions.
- **Stage 2:** an LLM proposes complex tasks; humans filter and execute them; another LLM generates intent annotations for the recorded multi-step trace.
- **Safety-related example:** “Equip me with a gun through this website” appears as an example of a task that is presumably filtered during construction; the paper does not discuss a formal safety policy.
- **Flow:** page → candidate task/action material → rule matching or prompting → manual filtering/annotation → task, HTML, operations, and intents.
- **Meaning:** executability is anchored by known elements or human traces rather than entrusted entirely to generative models.

## Figure 5 — Training-data proportions

- **Form:** pie chart.
- **Categories:** complex task 60 (38.71%), simple task 42 (27.1%), web recognition 40 (25.81%), Mind2Web 7 (4.51%), MiniWoB 6 (3.87%).
- **Derived check:** counts total 155; percentages total 100.00% [C].
- **Main observation:** newly constructed complex, simple, and recognition material constitutes 91.62% [C] of the displayed mixture.
- **Uncertainty:** the count unit is not labeled in the figure or caption.

## Figure 6 — Three-stage training procedure

- **Panel 1:** ChatGLM3-6B → easy recognition/operation training → planning/reasoning training.
- **Panel 2:** SFT model samples complex data → gold and sampled operations form positive/negative pairs → DPO+SFT training.
- **Panel 3:** DPO model self-plays in a web environment → successful traces are retained and failures rejected → RFT.
- **Feedback structure:** stages 2 and 3 both use the model’s own behavior, but stage 2 compares sampled actions with gold labels, whereas stage 3 uses environment-level success.
- **Meaning:** the pipeline moves from imitation, to learning from mistakes, to domain practice.

# 11. Table-by-Table Interpretation

## Table 1 — Action vocabulary

Ten commands cover element interaction, scrolling, history navigation, direct URL navigation, tab switching, asking the user to intervene, and termination. Arguments make the action space programmatic and executable. No gesture, drag-and-drop, file upload, download, or multi-touch action is listed.

## Table 2 — AutoWebBench

Rows are models; columns are size and four language/generalization splits. AutoWebGLM is best in every reported column. LLaMA2 has no Chinese results. No variance, significance marker, or uncertainty interval is included.

Important values:

- AutoWebGLM: 64.8, 58.6, 65.4, 61.8.
- GPT-4: 38.6, 39.7, 36.7, 36.3.
- Lowest reported English scores: LLaMA2-7B at 3.3/2.5.
- Lowest reported Chinese scores: Qwen-7B at 9.1/7.5.

## Table 3 — Mind2Web

Columns are cross-task, cross-website, cross-domain, and average. HTML-T5-XL is best at 71.5/62.2/67.1/66.9. AutoWebGLM is next by average at 59.5 and has 66.4/56.4/55.8.

Notes matter:

- † GPT-4 uses only top-10 candidates.
- Other evaluations use top-50.
- * denotes fine-tuning on the training set.
- The printed model size “543B” for HTML-T5-XL is unusually large relative to neighboring rows, but it is clearly what the supplied table reports; it is not corrected here.

## Table 4 — MiniWoB++ and WebArena

AutoWebGLM is the strongest listed system on both columns: 89.3 and 18.2. Missing results are shown by “-”. Asterisks denote training-set fine-tuning for some baselines. AutoWebGLM’s environment-specific RFT is described in the method but not marked by the table’s asterisk.

## Table 5 — Execution efficiency

Rows are action types; `count/tr` means reported count per trace. Columns partition system time into fetch, parse, predict, execute, and loading. Units are absent.

The average time components sum to 5025.44 [C: \(436.93+68.68+2407.34+20.36+2092.13\)]. Percentages sum to 100.01% because of rounding [C]. Prediction and loading are the principal bottlenecks.

## Table 6 — Ablations

The upper block changes training data; the lower block changes learning strategy. “-” means AutoWebBench/WebArena lack training sets suitable for that RFT comparison, as explained by the caption.

The table supports three nuanced conclusions:

- Stage 2 complex data supplies most of the initial gain.
- Stage 1 and Stage 2 together are better than Stage 2 alone.
- DPO improves three columns but slightly reduces MiniWoB++ before RFT.
- RFT supplies the largest gains on the two interactive environments.

## Table 7 — Error distribution

The four categories sum to 100% [C]. Hallucinations dominate at 44%; visual recognition plus context misunderstanding account for 48% [C]. Without the number of errors inspected, sampling frame, or coding procedure, the precision of these proportions cannot be evaluated.

## Table 8 — Per-task MiniWoB++ results

Rows are 56 task types; columns are AutoWebGLM, HTML-T5-XL, WebN-T5-XL, GPT-4, and GPT-3.5-Turbo. Values are average success rates on a 0–1 scale.

Key details:

- AutoWebGLM average: 0.893.
- HTML-T5-XL: 0.856.
- WebN-T5-XL: 0.484.
- GPT-4: 0.321.
- GPT-3.5-Turbo: 0.134.
- AutoWebGLM’s worst result is `enter-time` at 0.00.
- Its next-lowest include `choose-list` 0.15, `click-checkboxes-soft` 0.37, and `book-flight` 0.50.
- HTML-T5-XL reaches 1.00 on `enter-time`, exposing a task-specific weakness hidden by the aggregate.
- AutoWebGLM is notably strong where some baselines are weak, including `guess-number` (1.00 versus 0.13/0/0/0) and `use-spinner` (1.00 versus 0.07/0.07/0/0).
- Several tasks show ties at 1.00, so the aggregate advantage does not imply dominance on every task.

# 12. Diagram / Architecture Interpretation

The runtime system can be understood as a closed control loop:

```text
User task + browser state
          ↓
Screenshot and raw HTML
          ↓
OCR + HTML parser + element identifiers
          ↓
Simplified HTML + tabs + position + action history
          ↓
AutoWebGLM predicts one action
          ↓
Browser executor performs the action
          ↓
New webpage state ───────────────┘
```

The data path turns a visually and structurally complex page into compact model-readable context. The control path is the action prediction and execution loop. The history path feeds prior commands back into the next decision so the agent can avoid repetition.

Training mirrors increasing autonomy:

```text
Curated examples
  → curriculum SFT
  → sampled correct/incorrect action preferences
  → DPO + stabilizing SFT
  → environment self-play
  → retain successes
  → domain-specific RFT
```

The key distinction is that the **interaction framework** is responsible for perception normalization and execution, while the **language model agent** selects operations. Consequently, benchmark performance measures their combined behavior rather than the language model in isolation.

# 13. Equations and Mathematical Concepts

## §3.1 — State and action sets

\[
S=\{\mathrm{HTML},\mathrm{URL},\mathrm{WindowPosition}\},\qquad
A=\{\mathrm{click},\mathrm{scroll},\mathrm{type},\ldots\}.
\]

- \(S\): current browser state representation.
- \(A\): allowed action vocabulary.
- The ellipsis refers to the full Table 1 action space.

## §3.1 — History update

\[
H_t=\phi(H_{t-1},A_{t-1},S_t).
\]

- \(H_t\): interaction history at time \(t\).
- \(\phi\): history-update function.
- It combines earlier history, the preceding action, and the current observed state.

Plainly: after every browser action, the system records what happened so the next decision is context-aware. The paper does not define the internal mathematical form of \(\phi\).

## §3.1 — Transition and policy

\[
(S_{t+1},H_{t+1})
=
\left(T(S_t,A_t),\phi(H_t,A_t,S_{t+1})\right),
\]

\[
A_t=\pi(S_t\mid H_t), \qquad S_{t+1}=T(S_t,A_t).
\]

- \(\pi\): policy implemented by the trained model.
- \(T\): browser/environment transition.
- Input: current state and history.
- Output: next action, then next state and updated history.

The notation \(\pi(S_t\mid H_t)\) is unconventional as an action assignment because a policy normally denotes a distribution or mapping, but the authors use it to express action selection. No probabilistic details are supplied.

## Equation (1) — SFT objective

\[
\mathcal L_{\mathrm{SFT}}(\pi_\theta)
=
-\mathbb E_{(x,y)\sim D}
[\log \pi_\theta(y\mid x)].
\]

- \(D\): supervised training data.
- \(x\): model input, such as task and webpage context.
- \(y\): desired output/action.
- \(\pi_\theta\): policy with parameters \(\theta\).
- Output: negative log-likelihood loss.

Minimizing it increases the probability of the demonstrated correct output.

## Equation (2) — DPO objective

\[
\mathcal L_{\mathrm{DPO}}(\pi_\theta;\pi_{\rm ref})
=
-\mathbb E_{(x,y_w,y_l)\sim D}
\left[
\log \sigma\left(
\beta\log\frac{\pi_\theta(y_w\mid x)}{\pi_{\rm ref}(y_w\mid x)}
-
\beta\log\frac{\pi_\theta(y_l\mid x)}{\pi_{\rm ref}(y_l\mid x)}
\right)
\right].
\]

- \(y_w\): preferred/winning output, here associated with correct behavior.
- \(y_l\): rejected/losing output, here a sampled error.
- \(\pi_{\rm ref}\): reference policy.
- \(\sigma\): logistic sigmoid.
- \(\beta\): preference-strength/regularization parameter, reported as 0.15.
- The likelihood ratios compare the updated policy with the reference on good and bad actions.

Plainly: train the new model to favor the correct action over its own characteristic mistakes without drifting arbitrarily far from the reference policy.

## Equation (3) — Auxiliary preferred-output SFT

\[
\mathcal L_{\mathrm{SFT}}(\pi_\theta;\pi_{\rm ref})
=
-\mathbb E_{(x,y_w,y_l)\sim D}
[\log\pi_\theta(y_w\mid x)].
\]

Although \(\pi_{\rm ref}\) appears in the function signature, it does not appear inside the displayed right-hand side. The losing output \(y_l\) is also part of the sampled tuple but unused in this term. This may be notational carryover; the supplied work does not explain it.

## Equation (4) — Combined training loss

\[
\mathcal L_{\mathrm{Total}}
=
\lambda\mathcal L_{\mathrm{DPO}}+\mathcal L_{\mathrm{SFT}}.
\]

This combines preference learning with direct imitation of preferred outputs. Appendix A reports an SFT loss weight of 0.8, whereas Eq. (4) places \(\lambda\) on DPO. The document does not explicitly reconcile whether 0.8 is \(\lambda\), a separate implementation weight, or a prose/formula mismatch.

# 14. Interpretation and Discussion

[A] The results support the authors’ primary objective: the proposed pipeline produces a compact agent with strong scores across multiple kinds of web-navigation evaluation.

[D] The evidence most clearly supports three narrower conclusions:

1. **Data difficulty matters.** Complex traces cause the largest initial gains, consistent with their closer resemblance to multi-step evaluation.
2. **Foundational operations still matter.** Adding simple/recognition data to complex traces yields further gains, suggesting planning alone does not guarantee reliable clicking, typing, and scrolling.
3. **Environment practice is powerful but specialized.** RFT produces large improvements on MiniWoB++ and WebArena, but it is not evaluated as a general-purpose improvement on noninteractive datasets.

Several claims need careful calibration:

- “Outperform GPT-4” is true for the reported rows but does not establish universal superiority, because model access, prompting, fine-tuning, candidate counts, and task environments differ.
- “Practically usable” is supported mainly by benchmark scores and selected examples. The paper provides no deployment study, user study, long-duration reliability measurement, or real-world safety analysis.
- DPO is described as improving the model, but Table 6 shows a small MiniWoB++ decline before RFT.
- A 59.5 Mind2Web average is competitive but below HTML-T5-XL’s 66.9.
- An 18.2 WebArena result is the strongest listed but still indicates that many tasks remain unsolved.

No formal hypotheses or statistical tests are given; conclusions rely on point estimates.

# 15. Contributions and Novelty

## Conceptual

- Frames web control as a sequential state/history/action process combining structured page representation and language-model policy.

## Methodological

- Hybrid construction in which rules and humans establish executable actions while LLMs diversify task wording and generate step intentions.
- Global intent generation over full human traces rather than step-by-step prompting.

## Algorithmic

- HTML Pruner that retains selected elements and bounded relational context.
- Self-sampling filter that removes always-correct, never-correct, and duplicate-error examples before DPO.
- Combined DPO and SFT training to address reported instability.

## Dataset and benchmark

- Approximately 10,000 real webpage-operation traces are claimed.
- AutoWebBench supplies bilingual English–Chinese and cross-task/cross-domain evaluation.
- Human verification covers 50 traces in each of four splits.

## System

- A Chrome-extension-based agent that integrates HTML, OCR, spatial context, action history, and browser execution.

## Experimental

- Evaluation across AutoWebBench, Mind2Web, MiniWoB++, and WebArena.
- Data and training-strategy ablations.
- Runtime-component timing and error-category analysis.
- Per-task results for all 56 MiniWoB++ tasks.

# 16. Limitations

## Authors' stated limitations

The authors explicitly acknowledge that:

- HTML-only input falters on advanced web applications such as maps, animations, and video browsing (§6.1, p. 9).
- Image input can help with images, icons, and effects but struggles with numerals and extensive text (§6.1).
- Success and efficiency can decline on unfamiliar websites or those with unusual interaction logic (§6.2).
- Real web environments are unstable because of connection and related factors (§6.2).
- Mobile operation introduces gestures and stronger security restrictions (§6.3).
- Observed failures include hallucinations, poor graphical recognition, contextual misunderstanding, and pop-up interruptions (§5.4 and Table 7).

## Additional evidence-based analyst observations

These are [D], not author admissions:

- The main reported results have no variance, confidence intervals, significance tests, or repeated-run statistics.
- Benchmark conditions are not fully homogeneous: some baselines are fine-tuned, GPT-4 uses fewer Mind2Web candidates, and AutoWebGLM receives environment-specific RFT.
- AutoWebBench contains only 50 traces per split.
- Human annotation permits task modification or abandonment, which may bias the dataset toward feasible tasks.
- Error-analysis sample size and coding reliability are absent.
- Execution timing lacks units, hardware, and software settings.
- The paper does not isolate model errors from parser, OCR, executor, or reward-rule errors.
- Data leakage protections are described for WebArena query construction, but broader overlap checks across model pretraining, sites, templates, and benchmarks are not reported.
- The standardized action space omits some interaction types.
- The “approximately 10,000 traces” claim is not transparently reconciled with Figure 5’s displayed total of 155 unspecified units.
- Selected qualitative cases cannot establish everyday deployment reliability.
- No explicit privacy, abuse-prevention, authorization, or transaction-safety evaluation is presented, despite discussing real-site automation.

# 17. Threats to Validity

## Internal validity

Performance gains may reflect several simultaneous changes: added data, curriculum ordering, DPO, RFT, parser integration, and environment adaptation. Table 6 helps but is sequential rather than a full factorial design. Single reported point estimates make training variability unknown.

## Construct validity

SSR measures step correctness, while end-to-end user value depends on full task completion, recovery, safety, latency, and answer quality. AutoWebBench and Mind2Web therefore capture only part of practical usability.

## Statistical conclusion validity

No uncertainty estimates, hypothesis tests, effect-size intervals, or number of independent model-training runs are reported. Small point differences—such as DPO’s +0.2 on WebArena—cannot be distinguished from run-to-run noise using the supplied evidence.

## External and ecological validity

AutoWebBench uses real websites and WebArena simulates realistic environments, improving relevance. Nevertheless, only selected sites/tasks/languages are represented; mobile interfaces, maps, video, animation, unusual controls, and unstable live conditions remain undercovered.

## Reproducibility

Hyperparameters and prompts are supplied, and the authors state that code/model/data are released. However, the document itself lacks hardware, versions, seeds, exact preprocessing configurations, full reward rules, and raw evaluation traces.

## Data and annotation validity

Twenty annotators screened and edited tasks, but no inter-annotator agreement, double-coding rate, quality-control statistic, compensation information, or exact retained-task count is given.

## Baseline comparability

Fine-tuning status, candidate limits, model sizes, prompting, and access conditions differ. Table results are informative but not a perfectly controlled head-to-head comparison.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

1. **Multimodal input:** combine HTML with screenshots to handle visual applications while retaining text precision (§6.1).
2. **New reasoning strategies:** go beyond conventional Chain of Thought and exploit browsing history more effectively (§6.2).
3. **Self-checking:** confirm the current state and verify whether an operation had its intended effect (§6.2).
4. **Mobile applications:** adapt to simplified page XML but richer gesture actions and stricter platform security (§6.3).

## B. Additional open questions

- How stable are results across model-training seeds and website updates?
- How much does each perceptual component—HTML pruning, OCR, position, and history—contribute independently?
- Can RFT improve one environment without reducing performance elsewhere?
- How should reward rules detect partial, unsafe, or superficially successful outcomes?
- Can the system recover from changed layouts, failed clicks, authentication, CAPTCHA, and network errors?
- How well does it work beyond English and Chinese?
- What privacy and authorization controls are needed for sensitive operations?
- How do dataset curation and task abandonment affect benchmark difficulty?
- What is the actual timing unit and end-to-end latency on specified hardware?
- Are the claimed 10,000 traces, Figure 5’s 155 units, and later RFT collections counted under different definitions?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| AutoWebGLM | The proposed ChatGLM3-6B-based web-navigation agent |
| LLM | Large language model |
| LM | Language model |
| HTML | Structured markup describing webpage content and elements |
| XML | Structured markup mentioned for mobile interfaces |
| OCR | Optical Character Recognition; converts visible text in images into machine-readable text |
| GUI | Graphical user interface |
| Agent | A model embedded in an observe–decide–act loop |
| Action space | All commands the agent is allowed to issue |
| Observation space | Information supplied to the agent at each step |
| State \(S_t\) | Browser/page condition at step \(t\) |
| History \(H_t\) | Record of prior states/actions available at step \(t\) |
| Action \(A_t\) | Operation selected at step \(t\) |
| Policy \(\pi\) | Rule/model that chooses actions |
| Transition \(T\) | How an action changes the browser state |
| \(\phi\) | Function that updates interaction history |
| \(\theta\) | Trainable model parameters |
| SFT | Supervised Fine-Tuning on demonstrated correct outputs |
| CL | Curriculum Learning, progressing from easier to harder examples |
| DPO | Direct Preference Optimization, learning to prefer correct outputs over rejected ones |
| RFT | Rejection Sampling Fine-Tuning, retaining successful sampled trajectories |
| CoT | Chain of Thought; intermediate reasoning or intent |
| Trajectory/trace | Full sequence of actions and observations for a task |
| Golden operation | Human/reference correct action |
| Contrastive data | Paired preferred and rejected behaviors |
| \(y_w,y_l\) | Winning/preferred and losing/rejected outputs |
| \(\pi_{\rm ref}\) | Reference model used in DPO |
| \(\sigma\) | Logistic sigmoid in the DPO loss |
| \(\beta\) | DPO scaling parameter, set to 0.15 |
| \(\lambda\) | Generic weighting coefficient in the combined loss |
| SSR | Step Success Rate |
| Cross-task | Generalization to new tasks on familiar websites, as implied by the paper |
| Cross-website | Generalization to unseen websites within Mind2Web’s evaluation structure |
| Cross-domain | Generalization to websites/domains excluded from training |
| MiniWoB++ | Interactive simulated web-task benchmark |
| Mind2Web | Offline complex web-navigation benchmark |
| WebArena | Interactive web environment using virtualized realistic sites |
| AutoWebBench | Proposed bilingual real-web benchmark |
| In-context | Model use through prompting rather than indicated task-specific fine-tuning |
| 6B/70B | Approximately six/seventy billion model parameters |
| API | Application Programming Interface |
| CAPTCHA | Test designed to distinguish human from automated access |
| RQ | Research question; none are formally enumerated in this paper |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Model size | 6 | billion parameters | AutoWebGLM | Author-reported | Abstract; Tables 2–4 |
| Main operation dataset | ~10,000 | traces | Hybrid construction | Author-reported | §1, p. 2 |
| AutoWebBench test size | 50 | traces/split | Four splits | Author-reported | §4.3, p. 8 |
| Total AutoWebBench test traces | 200 | traces | \(50\times4\) | Analyst-derived | §4.3 |
| English cross-task | 64.8 | SSR points | AutoWebGLM | Author-reported/visually readable | Table 2 |
| English cross-domain | 58.6 | SSR points | AutoWebGLM | Author-reported/visually readable | Table 2 |
| Chinese cross-task | 65.4 | SSR points | AutoWebGLM | Author-reported/visually readable | Table 2 |
| Chinese cross-domain | 61.8 | SSR points | AutoWebGLM | Author-reported/visually readable | Table 2 |
| Mind2Web average | 59.5 | SSR points | AutoWebGLM | Author-reported/visually readable | Table 3 |
| Best listed Mind2Web average | 66.9 | SSR points | HTML-T5-XL | Author-reported/visually readable | Table 3 |
| MiniWoB++ | 89.3 | score | AutoWebGLM after RFT | Author-reported/visually readable | Table 4 |
| WebArena | 18.2 | score | AutoWebGLM after RFT | Author-reported/visually readable | Table 4 |
| MiniWoB++ evaluation volume | 5,600 | episodes | 56 tasks × 100 | Analyst-derived | §5.1 |
| DPO samples/example | 20 | samples | Complex-task training examples | Author-reported | §4.2.2 |
| Contrastive dataset | ~13,000 | examples | After DPO filtering | Author-reported | Appendix A |
| WebArena samples/query | 64 | attempts | RFT collection | Author-reported | §4.2.3 |
| MiniWoB++ RFT collection | ~15,000 / 66,000 | traces / steps | Successful data | Author-reported | §4.2.3 |
| WebArena RFT collection | 240 / ~2,000 | traces / steps | Successful data | Author-reported | §4.2.3 |
| SFT learning rate | \(10^{-5}\) | — | Batch 32 | Author-reported | Appendix A |
| DPO learning rate | \(10^{-6}\) | — | Batch 64 | Author-reported | Appendix A |
| DPO \(\beta\) | 0.15 | — | DPO stage | Author-reported | Appendix A |
| Stated auxiliary SFT weight | 0.8 | — | DPO stage | Author-reported; notation uncertain | Appendix A; Eq. 4 |
| RFT learning rate | \(10^{-5}\) | — | Batch 32 | Author-reported | Appendix A |
| Human annotators | 20 | people | One month | Author-reported | Appendix D |
| Proposed tasks/site | 50 | tasks | Complex-task generation | Author-reported | §4.1.2 |
| Retained tasks/site | ~20 | tasks | Manual selection | Author-reported | §4.1.2 |
| Prediction share of execution | 47.89 | % | Average | Author-reported | Table 5 |
| Loading share | 41.64 | % | Average | Author-reported | Table 5 |
| Prediction + loading | 89.53 | % | \(47.89+41.64\) | Analyst-derived | Table 5 |
| Hallucination errors | 44 | % of analyzed errors | Error analysis | Author-reported | Table 7 |
| Visual-recognition errors | 28 | % of analyzed errors | Error analysis | Author-reported | Table 7 |
| Context errors | 20 | % of analyzed errors | Error analysis | Author-reported | Table 7 |
| Pop-up errors | 8 | % of analyzed errors | Error analysis | Author-reported | Table 7 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| AutoWebGLM outperforms GPT-4 on reported web benchmarks | Higher values on every directly shared AutoWebBench, MiniWoB++, and WebArena column; higher Mind2Web average | Tables 2–4; X1–X4 | pp. 8–9 | Strong for displayed point estimates; heterogeneous settings prevent universal interpretation |
| A 6B model can be competitive with much larger models | 59.5 Mind2Web, 89.3 MiniWoB++, 18.2 WebArena | Tables 3–4 | p. 8 | Supported within listed comparisons; training and architecture differ |
| Complex-task data is highly valuable | Stage 2 produces large gains over earlier/data-only rows | Table 6; X6 | p. 9 | Moderate evidence; no uncertainty and not fully factorial |
| Simple data complements complex data | Stage 1+2 exceeds Stage 2 on all four reported metrics | Table 6 | p. 9 | Supported by consistent small-to-moderate point gains |
| DPO helps the model learn from errors | Improves three of four columns over SFT | Table 6; Eq. 2 | pp. 7, 9 | Mixed: MiniWoB++ declines 0.9 |
| RFT creates domain proficiency | MiniWoB++ 80.8→89.3; WebArena 8.5→18.2 | Table 6; X7 | p. 9 | Strong point-estimate evidence for target domains; no non-target evaluation |
| HTML simplification supports usable observation | Architecture and pruning algorithm retain selected structural context | Figure 3; Algorithm 1 | p. 4 | Method clearly documented; no isolated pruning ablation |
| System is practically deployable | 6B size, Chrome extension, qualitative cases, benchmark performance | Figures 2–3; Tables 2–4 | pp. 2–8 | Suggestive, not demonstrated through a formal field/user study |
| AutoWebBench measures bilingual generalization | English/Chinese and cross-task/cross-domain splits, 50 verified traces each | Table 2; §4.3 | p. 8 | Constructed as stated; breadth and reliability statistics are limited |
| Prediction/loading are optimization priorities | 47.89% and 41.64% of timing | Table 5 | p. 8 | Strong within measured system; hardware and units absent |
| Hallucination is the leading identified failure | 44%, largest error category | Table 7 | p. 9 | Descriptive only; denominator and sampling method missing |

# 22. Very Simple Explanation

Imagine giving a computer a task such as “find the newest laptop and tell me its price.” The computer must understand a messy webpage, find the right search box, type into it, click the right results, remember what it already did, and know when it has finished. AutoWebGLM is a language model trained to do that.

The researchers first clean up the webpage’s HTML so the model sees the useful controls instead of enormous amounts of clutter. They then teach it in stages: understand pages, perform simple actions, solve longer tasks, compare correct actions with its own mistakes, and finally practice inside interactive environments while keeping successful attempts.

It scored very well relative to the other systems shown in the paper, especially on MiniWoB++ and the authors’ English–Chinese AutoWebBench. But it is not a solved problem. It still hallucinates, struggles with strongly visual pages and unusual interfaces, and completes only a minority of WebArena’s difficult tasks. The paper’s most important lesson is that capable web agents need more than a strong language model: they need a clean view of the page, reliable actions, realistic training traces, feedback from mistakes, and a way to check whether actions actually worked.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue | Yes | Yes | Represented in compressed form | AutoWebGLM; 11 authors; KDD ’24; bibliographic metadata available on p. 1 |
| Abstract | Yes | Yes | Fully represented | Problem, method, benchmark, and claims covered |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, three challenges, contributions, deployment claim |
| §2 Related Work | Yes | Yes | Represented in compressed form | All five categories covered; individual citations not exhaustively restated |
| §3.1 Problem Setup | Yes | Yes | Fully represented | State, history, policy, transition, termination |
| §3.2 Framework | Yes | Yes | Fully represented | Architecture and interaction loop |
| §3.2.1 Observation Space | Yes | Yes | Fully represented | HTML, task, position, and prior actions |
| §3.2.2 Action Space | Yes | Yes | Fully represented | All ten commands represented |
| §4 Building AutoWebGLM | Yes | Yes | Fully represented | Data and staged training |
| §4.1 Data Construction | Yes | Yes | Fully represented | Challenges and hybrid strategy |
| §4.1.1 Recognition/Simple Tasks | Yes | Yes | Fully represented | Website sourcing, prompts, rules, validation issues |
| §4.1.2 Complex Tasks | Yes | Yes | Fully represented | 50 proposed/~20 retained, manual traces, GPT-4 intents |
| §4.2 Training | Yes | Yes | Fully represented | Three stages |
| §4.2.1 Curriculum Learning | Yes | Yes | Fully represented | Data ordering and Eq. 1 |
| §4.2.2 Reinforcement Learning | Yes | Yes | Fully represented | 20-fold sampling, filtering, DPO+SFT, Eqs. 2–4 |
| §4.2.3 RFT | Yes | Yes | Fully represented | MiniWoB++/WebArena collection and sizes |
| §4.3 AutoWebBench | Yes | Yes | Fully represented | Four splits, 50 traces/split, SSR |
| §5 Experiments | Yes | Yes | Fully represented | All reported analyses separated |
| §5.1 Main Results | Yes | Yes | Fully represented | AutoWebBench, Mind2Web, MiniWoB++, WebArena |
| §5.2 Efficiency | Yes | Yes | Fully represented | Table 5 and missing-unit caveat |
| §5.3 Ablation | Yes | Yes | Fully represented | Data and strategy blocks |
| §5.4 Cases/Error Analysis | Yes | Yes | Fully represented | Cases and four error proportions |
| §6 Future Direction | Yes | Yes | Fully represented | All three subsections |
| §6.1 Multimodal Input | Yes | Yes | Fully represented | HTML/image tradeoff |
| §6.2 Reasoning/Self-check | Yes | Yes | Fully represented | New reasoning and operation verification |
| §6.3 Mobile Application | Yes | Yes | Fully represented | XML simplicity, gestures, security restrictions |
| §7 Conclusion | Yes | Yes | Represented in compressed form | Claims cross-checked against results |
| Acknowledgments | Yes | No substantive analysis | Deliberately omitted as non-methodological | Funding bodies not relevant to technical conclusions |
| References 1–45 | Text only | Yes, categorically | Represented in compressed form | Page 10 not visually rendered; citations grouped through related-work analysis |
| Figure 1 | Yes, visual | Yes | Fully represented | Radar plot; exact table values preferred |
| Figure 2, panels a–d | Yes, visual | Yes | Fully represented | Four qualitative cases; small transcript text partly unreadable |
| Figure 3 | Yes, visual | Yes | Fully represented | Training and runtime architecture |
| Figure 4 | Yes, visual | Yes | Fully represented | Two-stage data construction |
| Figure 5 | Yes, visual | Yes | Fully represented | All five displayed counts/percentages and unit uncertainty |
| Figure 6 | Yes, visual | Yes | Fully represented | Three-stage training |
| Table 1 | Yes, visual/text | Yes | Fully represented | All actions |
| Table 2 | Yes, visual/text | Yes | Fully represented | All important results and missing entries |
| Table 3 | Yes, visual/text | Yes | Fully represented | Values, †/* notes, model-size issue |
| Table 4 | Yes, visual/text | Yes | Fully represented | Values and specialization caveat |
| Table 5 | Yes, visual/text | Yes | Fully represented | Timing values, proportions, unspecified units |
| Table 6 | Yes, visual/text | Yes | Fully represented | All rows and derived changes |
| Table 7 | Yes, visual/text | Yes | Fully represented | All categories |
| Table 8 | Yes, visual/text | Yes | Represented in compressed form | Every task inspected; notable strengths/weaknesses reported rather than repeating all 280 cells |
| Algorithm 1 | Yes, visual/text | Yes | Fully represented | Inputs, flow, output, and pseudocode uncertainties |
| State/action equations | Yes | Yes | Fully represented | All symbols described to extent defined |
| Equation (1) | Yes | Yes | Fully represented | SFT loss |
| Equation (2) | Yes | Yes | Fully represented | DPO loss |
| Equation (3) | Yes | Yes | Fully represented | Auxiliary SFT and notation issue |
| Equation (4) | Yes | Yes | Fully represented | Combined loss and weight discrepancy |
| Explicit research questions | Yes | Yes | Fully represented | None formally stated |
| Explicit hypotheses | Yes | Yes | Fully represented | None formal; one explanatory hypothesis identified |
| Contributions | Yes | Yes | Fully represented | Conceptual, methodological, dataset, system, experimental |
| Author-stated limitations | Yes | Yes | Fully represented | Visual applications, unfamiliar sites, instability, mobile, error classes |
| Appendix A | Yes | Yes | Fully represented | Hyperparameters and data quantities |
| Appendix B | Yes | Yes | Represented in compressed form | Every prompt field/function role covered; boilerplate not reproduced |
| Appendix C | Yes | Yes | Represented in compressed form | Task/operation and intent prompt constraints covered |
| Appendix D | Yes | Yes | Fully represented | Annotators, duration, screening, recording/editing |
| Appendix E | Yes | Yes | Fully represented via Table 8 audit | Aggregate and task-level extremes covered |
| Supplementary material | N/A | Yes | Missing from supplied material | No separate supplement supplied or explicitly identified |

## Missing or inaccessible material

- Page 10 was not visually rendered, but its complete references text was supplied. No substantive figure, table, equation, or method is on that page.
- The GitHub repository, code, trained models, data files, Chrome extension, browser environments, raw traces, and external websites were not supplied and were not inspected.
- Fine text inside some Figure 2 execution transcripts cannot be read confidently from the page rendering.
- No separate supplementary artifact was supplied.
- Hardware, software versions, random seeds, full reward rules, exact site lists, raw measurements, and evaluation logs are absent from the paper.

## Uncertain interpretations

- Figure 5’s values 40/42/60/6/7 have no explicit unit.
- Table 5’s timing values have no explicit unit.
- Table 3 prints HTML-T5-XL as 543B; this analysis preserves the printed value without correction.
- AutoWebBench’s prose labels “in-domain/out-of-domain” while Table 2 uses “cross-task/cross-domain.”
- Appendix A compresses RFT data to “66k and 2k,” whereas §4.2.3 distinguishes traces from steps.
- Equation (3) names \(\pi_{\rm ref}\) and samples \(y_l\), but neither appears in its right-hand expression.
- Equation (4)’s \(\lambda\) placement is not clearly reconciled with Appendix A’s statement that the SFT loss is weighted by 0.8.
- Algorithm 1 contains apparent pseudocode naming/grammar issues such as `getAnscendants` and `tree.remove(element)` after iterating over `node`; intended behavior is clear at a high level but exact implementation cannot be reconstructed confidently.
- Table 7’s percentages lack a denominator.

## Deliberately compressed material

- The 45-item bibliography was categorized rather than individually summarized.
- Standard publication metadata, licensing language, affiliations, and acknowledgments were not repeatedly discussed.
- Appendix prompt boilerplate was summarized by functional field and constraint.
- Table 8’s 280 task–model cells were inspected but compressed into averages, weaknesses, strengths, ties, and illustrative contrasts.
- Repeated statements of the same three-stage training process across the abstract, Figures 3 and 6, main text, and conclusion were consolidated.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, major equation, algorithm, contribution, author-stated limitation, or appendix item from the supplied inventory is unrepresented. The primary residual limitations concern external artifacts not supplied, missing experimental detail in the paper itself, the lack of a visual rendering for the references-only page, and a few notation/unit ambiguities explicitly listed above.