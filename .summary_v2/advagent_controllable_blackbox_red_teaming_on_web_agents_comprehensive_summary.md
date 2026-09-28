# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available extent | All 13 pages, page-labeled native/extracted text |
| Apparently missing pages | None |
| Visually rendered pages supplied | pp. 1, 2, 4–9, 12–13 |
| Pages not visually rendered | pp. 3, 10, 11 |
| Figures | Figures 1–5 were visually supplied and inspected |
| Tables | Tables 1–6 were visually supplied and readable |
| Algorithms | Algorithms 1–2 were visually supplied and readable |
| Equations | Equations (2)–(3) were visually supplied; Equation (1) was available only through extracted text because p. 3 was not rendered |
| Appendices | Appendices A–D are present on pp. 12–13 |
| References | Present on pp. 10–11; text available, but those pages were not visually inspected |
| Supplementary material | None supplied or clearly referenced as a separate supplement |
| Embedded files | None |
| OCR needed | No general OCR was needed. Extracted mathematical notation and text embedded in figures remain OCR-sensitive |
| Material limitations | The paper does not report hardware, random seeds, validation splits, exact per-domain test counts, numbers of positive/negative prompts after feedback, DPO coefficient \(\beta\), or repetition counts. These cannot be reconstructed from the supplied work |

All substantive figures, tables, and algorithms can be inspected directly. The mathematical structure of Equations (2)–(3) is readable, although line breaking and typesetting make their expectation and summation scopes mildly ambiguous. The analysis therefore preserves the equations’ substantive optimization roles without silently repairing their notation.

Evidence labels used below:

- **[A] Author-reported:** explicitly stated by the paper.
- **[B] Directly observable:** visible in a supplied page image.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** a source-grounded inference, not an author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

AdvAgent is a security-testing framework for web agents: artificial-intelligence systems that read websites and take actions for users. The paper asks whether a malicious webpage can invisibly alter what such an agent does—for example, turning “buy Microsoft” into “buy NVIDIA”—without changing the webpage as seen by the human user.

The central vulnerability is an **indirect prompt injection**. The attacker puts a malicious natural-language instruction inside a non-rendered HTML attribute such as `aria-label`. The user does not see it, but a web agent processing the HTML may interpret it as an instruction. AdvAgent automatically learns which wording is most effective.

The method has two training stages:

1. **Supervised fine-tuning (SFT):** learn from prompts that already succeeded.
2. **Direct Preference Optimization (DPO):** learn the difference between successful and unsuccessful prompts using feedback from the attacked black-box agent.

The authors test AdvAgent against the SeeAct web-agent framework using GPT-4V and Gemini 1.5 backends on 200 test tasks drawn from finance, medical, housing, and cooking domains. [A: pp. 2, 5–6, §§4–5.1]

The main results are:

- 97.5% mean step-based attack success rate (ASR) against GPT-4V SeeAct.
- 99.8% against Gemini 1.5 SeeAct.
- The best baseline obtained 64.3% against GPT-4V and 28.0% against Gemini.
- Adding DPO raised GPT-4V mean ASR from 69.5% to 97.5%.
- Simple prompt-based defenses reduced Gemini mean ASR only to 88.8–89.8%.
- Successful prompts could usually be retargeted by replacing the malicious target string, reaching 98.5% ASR for GPT-4V and 100.0% for Gemini. [A/B: pp. 6–8, 12, Tables 1–6; Fig. 3]

The contribution is therefore not a defense but a black-box red-teaming method that exposes how readily current web agents can be redirected by hidden website content.

# 2. Document Roadmap

The 13-page paper is organized as follows:

1. **Abstract and Introduction** (pp. 1–2): motivates the security problem, introduces AdvAgent, previews results, and lists four contributions.
2. **Related Work** (pp. 2–3): covers web agents and attacks on them.
3. **Targeted Black-box Attack on Web Agents** (pp. 3–4): formalizes web-agent actions, the threat model, attack constraints, and technical challenges.
4. **AdvAgent** (pp. 4–5): explains hidden HTML injections, automated feedback collection, SFT, and DPO.
5. **Experiments** (pp. 6–8): gives the setup, headline comparison, ablations, adaptability and controllability tests, cross-model transfer analysis, and case studies.
6. **Mitigation Strategies and Blue-teaming** (pp. 8–9): evaluates three prompt-based defenses.
7. **Conclusion, acknowledgements, and impact statement** (p. 9).
8. **References** (pp. 10–11).
9. **Appendices A–D** (pp. 12–13): Gemini controllability results, additional qualitative examples, additional related work, and limitations.

The progression is coherent: threat model → attack design → training method → empirical evaluation → defenses and limitations.

# 3. Background and Context

A **web agent** is an AI system that receives a user request, observes a webpage, and produces executable actions. In the paper’s formulation, the observation includes both the page’s HTML and its rendered screenshot. [A: p. 3, §3.1]

A **large language model (LLM)** processes language. A **vision-language model (VLM)** processes language and images. SeeAct uses a proprietary VLM backend to reason over screenshots and maps its proposed action to an HTML element. [A: pp. 3, 6]

An HTML page has visible text and metadata. An attribute such as `aria-label` can describe an element for software without necessarily appearing visually. AdvAgent places the adversarial prompt in such a non-rendered attribute. The paper’s intended security property is:

\[
I(h)=I(h_{\mathrm{adv}}),
\]

meaning that rendering original HTML \(h\) and adversarial HTML \(h_{\mathrm{adv}}\) produces the same visible image. [A: pp. 3–4, §3.2–4.1]

A **black-box attack** observes outputs but has no access to the victim model’s parameters, logits, or gradients. A **white-box attack** has internal access useful for gradient optimization.

**Red-teaming** deliberately attacks a system to discover weaknesses. Here the goal is a **targeted attack**: make the agent perform one particular wrong action, not merely cause any failure.

**Attack success rate (ASR)** is defined at an individual action step. Success requires an exact match to the malicious action triplet: correct operation, malicious argument, and target HTML element. It is not an end-to-end task-completion metric. [A: p. 6, §5.1; p. 12, Appendix D]

**Reinforcement learning from AI feedback (RLAIF)** here means that another AI system—the victim web agent—provides success/failure signals used to improve the attack generator. The paper implements this through SFT followed by DPO rather than through a separately learned scalar reward model. [A: pp. 4–5]

# 4. Research Problem and Gap

## Existing problem

Web agents may act on finance, healthcare, e-commerce, and other sensitive systems. Because they interpret webpage content and can autonomously act, malicious content can produce consequential unintended actions. [A: p. 1, Introduction]

## Shortcomings attributed to previous approaches

The authors identify three families of shortcomings:

- Some automated attacks require white-box model access and gradients.
- Manual or heuristic prompt injections require substantial human effort and do not scale well.
- Prompts optimized against one model often transfer poorly to different black-box backends. [A: pp. 1, 3–4]

Existing LLM jailbreak methods are also characterized as concentrating on comparatively simple objectives, such as eliciting harmful responses, rather than multi-part actions grounded in webpages. [A: p. 12, Appendix C]

## Research gap

The stated gap is an efficient, automated, adaptable, and controllable method for targeted attacks on multimodal web agents using only black-box feedback. [A: pp. 1, 3–4]

## Motivation

An attacker who controls or contaminates webpage HTML could invisibly redirect consequential actions. The authors mention malicious website developers and contaminated dependencies as possible scenarios. [A: p. 3, §3.2]

## Scope

The empirical scope is SeeAct with GPT-4V and Gemini 1.5 Flash backends, using 440 selected Mind2Web tasks from four domains. The work attacks individual action steps by altering the action argument while retaining its operation and HTML target. [A: pp. 3, 6]

# 5. Research Questions / Objectives / Hypotheses

The paper gives no formally numbered research questions or hypotheses.

Its explicit and implicit objectives are:

- **O1:** Develop a targeted black-box red-teaming framework for web agents.
- **O2:** Generate hidden and controllable HTML prompt injections automatically.
- **O3:** use victim-agent feedback to improve the adversarial prompter.
- **O4:** measure effectiveness against different proprietary backends and domains.
- **O5:** test the contribution of DPO, robustness to HTML variations, controllability, cross-model transfer, and resistance to common prompt defenses. [A: pp. 1–2, 4, 7–9]

The experimental propositions tested, without being formal hypotheses, are that feedback-guided training improves ASR, target placeholders allow inexpensive retargeting, HTML-field changes preserve effectiveness better than position changes, direct model-specific optimization outperforms transfer, and common defenses remain insufficient.

# 6. Assumptions / Threat Model

## System model

At step \(t\), the agent observes:

- user task \(T\);
- action history \(A_t\);
- HTML \(h_t\);
- rendered screenshot \(i_t=I(h_t)\).

Its backend policy \(\Pi\) outputs action \(a_t\). [A: p. 3, Eq. (1)]

## Action representation

\[
a=(o,r,e),
\]

where:

- \(o\): operation, such as typing;
- \(r\): operation argument, such as “Microsoft”;
- \(e\): target HTML element.

The attack changes only the argument:

\[
a_{\mathrm{adv}}=(o,r_{\mathrm{adv}},e).
\]

[A: p. 3, §§3.1–3.2]

## Attacker capabilities

The attacker may:

- modify webpage HTML \(h\) into \(h_{\mathrm{adv}}\);
- insert natural-language adversarial prompts into hidden attributes;
- query the victim agent offline and observe whether attacks succeed;
- substitute a new target argument into an already successful prompt. [A: pp. 3–5]

## Excluded capabilities

The attacker has no access to:

- victim-agent framework internals;
- backend weights;
- logits;
- gradients. [A: p. 3, §3.2]

## Constraints

- **Stealthiness:** the malicious modification must not alter the rendered webpage, expressed as \(I(h)=I(h_{\mathrm{adv}})\).
- **Controllability:** a successful prompt should be retargetable through deterministic replacement \(D(h_{\mathrm{adv}},r_{\mathrm{adv}},r'_{\mathrm{adv}})\), without another optimization cycle. [A: pp. 3–4]

## Trusted or assumed components

The evaluation assumes that:

- the attacker can obtain and modify the relevant HTML;
- the agent processes the chosen non-rendered attribute;
- the agent’s expected target element is known so the injection can be placed near it;
- exact step-level matching is an adequate test of targeted manipulation.

The first three are elements of the described attack design. The last is the evaluation construct and is explicitly qualified in Appendix D.

# 7. Methodology

## Study design

This is a cybersecurity and machine-learning systems experiment. The researchers train an adversarial prompt generator, attack black-box web agents, compare it with three baselines, and conduct ablations and transfer/defense tests.

## Structured adversarial HTML

The adversarial string \(q\):

1. is placed in a non-rendered HTML attribute, principally `aria-label`;
2. contains a placeholder such as `{target argument}`;
3. is injected at the HTML element the agent is expected to select.

This reduces the otherwise enormous discrete search space and directly enforces the intended stealthiness and target replacement mechanism. [A: pp. 4–5, §4.1]

## Initial data generation

Algorithm 1 asks a large language model to generate varied malicious prompts from the original HTML. For every training task, GPT-4 produces ten candidates at temperature 1.0. Each candidate is tested on the victim agent and labeled positive or negative according to whether the target action occurs. [A: pp. 5–6]

The paper does not report:

- total retained prompt count;
- numbers \(n_1\) and \(n_2\) of positive and negative instances;
- rejection or deduplication procedures;
- per-domain composition of those partitions.

## Two-stage training

Algorithm 2 initializes a prompter from Mistral-7B-Instruct-v0.2.

- Stage 1 uses SFT on positive prompts.
- Stage 2 fixes the SFT model as reference policy and applies DPO to positive–negative prompt pairs.

The stated rationale is that initial SFT stabilizes the subsequent preference-learning stage, while DPO learns subtle distinctions from both successful and failed attempts. [A: p. 5, §4.2]

## Dataset and split

Mind2Web contains 2,350 tasks from 137 websites and 31 domains. The authors select 440 tasks involving “critical events” across four domains:

- Finance
- Medical
- Housing
- Cooking

The split is 240 training tasks and 200 test tasks. [A: p. 6, §5.1]

No validation split, precise selection rule, per-domain counts, or class distribution is supplied.

## Victim agents

SeeAct is evaluated with:

- `gpt-4-vision-preview`;
- `gemini-1.5-flash`.

SeeAct first creates an action description from the user task and screenshot, then grounds that description to HTML. [A: p. 6]

## Implementation details

| Component | Reported setting |
|---|---|
| Initial attack-prompt generator | GPT-4 |
| Candidate prompts | 10 per task |
| Sampling temperature | 1.0 |
| Learned prompter initialization | Mistral-7B-Instruct-v0.2 |
| SFT learning rate | \(1\times10^{-4}\) |
| SFT batch size | 32 |
| DPO learning rate | \(1\times10^{-4}\) |
| DPO batch size | 16 |

[A: p. 6, §5.1]

Hardware, training duration, optimizer, sequence length, random seeds, DPO \(\beta\), decoding parameters for the trained model, and software versions are not specified.

## Baselines

- **GCG:** optimized against the open-source LLaVA-NeXT VLM and transferred to the black-box agent.
- **Agent-Attack:** manually curated injection prompts adapted to the tasks.
- **InjecAgent:** GPT-4-generated injection prompts adapted to the evaluated websites. [A: p. 6]

## Metric

Step-based ASR is the proportion of evaluated attack steps at which the agent exactly outputs \(a_{\mathrm{adv}}=(o,r_{\mathrm{adv}},e)\). The paper reports domain rates and a mean ± standard deviation across four domains. It reports no confidence intervals or significance tests. [A: p. 6]

# 8. Experiments / Analyses

## X1 — Primary effectiveness and baseline comparison

**Purpose:** Determine whether AdvAgent can redirect SeeAct and whether it outperforms prior attacks.

**Setup:** Four domains; GPT-4V and Gemini 1.5 backends; GCG, Agent-Attack, InjecAgent, and AdvAgent; step-based ASR.

**Result:** AdvAgent reached 97.5% ± 2.0 across domains for GPT-4V and 99.8% ± 0.3 for Gemini. The strongest baselines were InjecAgent at 64.3% ± 16.7 on GPT-4V and 28.0% ± 23.0 on Gemini. [A/B: p. 6, Table 1]

**Caveat:** The number of test steps represented by each domain percentage is not specified.

## X2 — Training-stage ablation

**Purpose:** Test whether DPO feedback learning adds value beyond SFT.

**Conditions:** SFT only versus SFT+DPO on GPT-4V SeeAct.

**Results:** Means were 69.5% and 97.5%. Domain improvements were:

- Finance: 94.8 → 100.0
- Medical: 59.2 → 94.4
- Housing: 74.8 → 97.6
- Cooking: 49.2 → 98.0

[A/B: p. 7, Fig. 3]

**Analyst-derived differences:** +5.2, +35.2, +22.8, and +48.8 percentage points; mean +28.0 points.

**Caveat:** This ablation changes the training objective/stage but does not isolate other possible consequences such as extra training computation.

## X3 — Adaptability to injection position and HTML field

**Purpose:** Test whether successful standard-setting attacks remain effective after structural HTML changes.

**Conditions:**

- move the injection from after to before expected element \(e\);
- replace `aria-label` with `id`.

**Results:**

- Different position: 26.0, 82.0, 88.0, 88.0; mean 71.0% ± 26.1.
- Different HTML field: 98.0, 94.0, 98.0, 98.0; mean 97.0% ± 1.7.

[A/B: p. 7, Table 2]

**Interpretation:** Field transfer is consistently strong; position transfer is highly domain-dependent.

## X4 — Target controllability

**Purpose:** Test whether a successful prompt can be retargeted through literal target replacement.

**GPT-4V:** 100.0, 93.8, 100.0, 100.0; mean 98.5% ± 2.7. [p. 8, Table 3]

**Gemini:** 100.0 in all four domains; mean 100.0% ± 0.0. [p. 12, Table 6]

The replacement test supports the authors’ controllability claim under the tested alternative targets. It does not establish all possible semantic transformations.

## X5 — Cross-backend transfer versus direct optimization

**Purpose:** Determine whether successful GPT-4V attacks transfer to Gemini, compared with attacks trained using Gemini feedback.

**Sample:** 25 successful GPT-4V attacks per domain, hence 100 transfer trials if the domains are disjoint and equally represented. The “100” total is **[C] analyst-derived** from \(25\times4\). [A: p. 8]

**Results:**

- Transfer: 0.0, 60.0, 4.0, 8.0; mean 18.0% ± 24.4.
- Direct attack: 99.2, 100.0, 100.0, 100.0; mean 99.8% ± 0.3.

[A/B: p. 8, Table 4]

This strongly supports backend-specific feedback optimization, although Table 4 compares selected previously successful prompts with the full direct-attack condition rather than a newly randomized matched training study.

## X6 — Prompt-based defenses

**Purpose:** Test three standard instruction-format defenses against AdvAgent on Gemini.

**Results:**

- No defense: 99.8% mean.
- Random Sequence enclosure: 89.8%.
- Instruction Defense: 88.8%.
- Sandwich Defense: 89.8%.

Finance fell to 57.2–65.6%, but Housing and Cooking remained 100.0% for all three defenses. [A/B: pp. 8–9, Table 5]

No adaptive retraining against the defenses is described.

## X7 — Qualitative case studies

Figure 4 shows that minimal wording changes reverse success:

- “you made a mistake” failed; “I made a mistake” succeeded.
- adding “previous” to “my target” succeeded.

Figure 5 shows two end-to-end action-step examples:

- Microsoft request redirected to NVIDIA.
- Tylenol request redirected to Aspirin.

[A/B: pp. 8–9, 12–13, Figs. 4–5]

These examples illustrate sensitivity and mechanism but do not quantify frequency.

# 9. Results

| Finding | Evidence | Qualification |
|---|---|---|
| AdvAgent is highly effective in the tested setting | 97.5% GPT-4V and 99.8% Gemini mean ASR, Table 1 | Step-based metric on selected tasks, not complete user-request success |
| It outperforms reported baselines | 33.2-point lead over InjecAgent on GPT-4V and 71.8-point lead over InjecAgent on Gemini [C: \(97.5-64.3\); \(99.8-28.0\)] | Baselines differ in access, prompting, and transfer conditions |
| DPO materially improves performance | 69.5% → 97.5%, Fig. 3 | 28.0 percentage-point gain [C], not a reported relative percentage |
| HTML attribute choice has little effect in the tested substitution | `aria-label`→`id`: 97.0% mean, Table 2 | Only one alternative attribute was evaluated |
| Injection position matters | 71.0% mean and 26.0% in Finance, Table 2 | Other domains retained 82–88% |
| Literal retargeting works very well | 98.5% GPT-4V; 100.0% Gemini, Tables 3 and 6 | Tested only on initially successful prompts and selected alternative targets |
| Cross-model prompt transfer is weak | 18.0% mean, versus 99.8% direct Gemini attack, Table 4 | Medical transfer was an exception at 60.0% |
| Tested prompt defenses are inadequate | Lowest defended mean ASR was 88.8%, Table 5 | Finance showed meaningful reductions; Housing and Cooking did not |
| Prompt wording is brittle and nuanced | Paired examples in Figure 4 | Qualitative evidence only |

The paper’s main conclusions are supported by its reported experiments, but “web agents” should be read as the tested SeeAct configuration rather than every possible agent architecture.

# 10. Figure-by-Figure Interpretation

### Figure 1 — AdvAgent attack overview

- **Type:** architecture/scenario diagram.
- **Content:** a stock website, adversarial prompter, hidden HTML injection, web agent, and redirected stock action.
- **Flow:** webpage → prompter-generated malicious string → invisible HTML attribute → web agent → malicious target action.
- **Example:** user asks for Microsoft; injection says to type NVIDIA; agent buys NVIDIA.
- **Axes/units:** none.
- **Visual encoding:** peach region represents malicious website/injection; blue region represents user–agent action; arrows show processing flow.
- **Conclusion supported:** an unchanged rendered page may contain machine-readable instructions that redirect the agent.
- **Status:** scenario and labels are visually readable; it is explanatory, not quantitative. [B: p. 2]

### Figure 2 — Prompter-model training pipeline

- **Type:** process/feedback-flow diagram.
- **Stages:** generate candidate adversarial prompts; collect victim feedback; form positive/negative data; perform SFT on positives; perform DPO on both classes.
- **Feedback loop:** black-box victim responses produce the preference information used for training.
- **Outputs:** first an SFT prompter, then the final adversarial prompter.
- **Conclusion supported:** AdvAgent converts binary attack outcomes into a two-stage learning signal.
- **Uncertainty:** the caption says data are collected using “Algorithm 1 in ??,” an unresolved cross-reference. The diagram itself says “using Algorithm 2,” which conflicts with both the method and Algorithm 2’s role. Candidate generation is actually described in Algorithm 1; training is Algorithm 2. [A/B: p. 4]

### Figure 3 — SFT versus SFT+DPO

- **Type:** grouped bar chart.
- **X-axis:** Finance, Medical, Housing, Cooking, Average.
- **Y-axis:** ASR, apparently 0–100%.
- **Legend:** light blue = SFT only; dark blue = SFT+DPO.
- **Exact labeled values:** 94.8/100.0, 59.2/94.4, 74.8/97.6, 49.2/98.0, 69.5/97.5.
- **Main observation:** DPO improves every domain; the largest absolute gain is Cooking, +48.8 percentage points [C].
- **Error bars:** none displayed.
- **Caveat:** “significant improvement” is ordinary-language usage; no statistical significance test is reported. [A/B: p. 7]

### Figure 4 — Minimal wording changes and attack outcome

- **Type:** paired qualitative examples.
- **Pair 1:** “you” produces the legitimate Microsoft action; “I” produces malicious Apple.
- **Pair 2:** without “previous,” the agent searches Tylenol; with “previous,” it searches Aspirin.
- **Conclusion supported:** tiny linguistic differences can determine success.
- **Caveat:** two chosen examples cannot measure prevalence or causal generality.
- **Text issue:** the visual/extraction displays `arial-label`, apparently a misspelling or rendering/extraction issue for `aria-label`. [B: p. 9]

### Figure 5 — Additional qualitative attacks

- **Type:** two workflow examples.
- **Example 1:** portfolio request for Microsoft is redirected to NVIDIA.
- **Example 2:** Tylenol side-effect search is redirected to Aspirin.
- **Components:** user request, webpage screenshot, generated hidden prompt, and agent’s selected operation.
- **Conclusion supported:** attacks operate in two different domains and preserve the intended element/operation while altering the argument.
- **Inconsistency:** the prompt text says “optimized by AdvWeb,” although the system is called AdvAgent throughout. This appears in the supplied visual and text and is not explained. [B: p. 13]

# 11. Table-by-Table Interpretation

### Table 1 — Main attack comparison

Rows are four attacks; columns are ASR percentages for D1–D4 and mean ± cross-domain standard deviation.

- GPT-4V: AdvAgent is best in all domains, 94.4–100.0%.
- Gemini: AdvAgent is best in all domains, 99.2–100.0%.
- GCG is 0.0 everywhere.
- InjecAgent is the strongest GPT-4V baseline; Agent-Attack is slightly stronger than InjecAgent in mean Gemini ASR only? No: InjecAgent mean is 28.0 versus Agent-Attack 25.0, so InjecAgent remains marginally higher, although domain behavior varies.
- No inferential statistics are included. [A/B: p. 6]

### Table 2 — Structural variations

Two rows test changed position and changed HTML attribute.

- Position change is weakest and most variable: 71.0% ± 26.1.
- Field change is strong and uniform: 97.0% ± 1.7.
- Finance accounts for most position sensitivity at 26.0%.
- These are transferability tests of successful standard attacks, not independently optimized attacks. [A/B: p. 7]

### Table 3 — GPT-4V controllability

The malicious argument is replaced with an alternative.

- D1/D3/D4: 100.0%.
- D2: 93.8%.
- Mean: 98.5% ± 2.7.

The table supports literal target substitution with no reported re-optimization. [A/B: p. 8]

### Table 4 — Cross-model transfer

- GPT-4V→Gemini transfer mean: 18.0% ± 24.4.
- Direct Gemini optimization: 99.8% ± 0.3.
- Medical transfer reaches 60.0%, while the other domains are 0–8%.
- Analyst-derived absolute mean gap: \(99.8-18.0=81.8\) percentage points. [A/B/C: p. 8]

### Table 5 — Defense evaluation

The columns report domain ASR percentages and an unqualified mean; unlike other tables, no standard deviation is shown.

- Instruction Defense has the lowest mean ASR, 88.8%.
- Sequence and Sandwich both yield 89.8%.
- Every defense leaves D3 and D4 at 100.0%.
- Finance sees the largest reductions.
- The table supports “limited protection,” but also shows domain-specific effectiveness that the overall mean obscures. [A/B: p. 8]

### Table 6 — Gemini controllability

All domain ASRs and the mean are 100.0%; reported standard deviation is 0.0. This is the strongest controllability result, but it remains conditioned on attacks that were successful before replacement. [A/B: p. 12]

# 12. Diagram / Architecture Interpretation

AdvAgent has three functional layers:

1. **Attack-surface layer:** the attacker inserts \(q\) into a hidden attribute at the anticipated target HTML element.
2. **Feedback collection layer:** multiple candidate prompts are executed against the black-box agent and labeled by exact attack success.
3. **Learning layer:** positives train an initial SFT policy; positive–negative pairs train a DPO policy.

At inference, the trained prompter maps HTML context \(h\) to a malicious instruction \(q\). A placeholder provides the malicious argument, allowing later replacement without re-running training.

The system has no gradient path into the victim. Its only connection to the victim is behavioral feedback. That separation is why the authors classify it as black-box. [A/B: pp. 4–5, Fig. 2, Algorithms 1–2]

# 13. Equations and Mathematical Concepts

## Equation (1): web-agent policy

\[
a_t=\Pi(s_t,T,A_t)=\Pi(\{i_t,h_t\},T,A_t).
\]

- **Location:** p. 3, §3.1.
- **Object:** policy/function mapping observations and history to an action.
- \(a_t\): action at time \(t\).
- \(\Pi\): backend agent policy.
- \(s_t\): current environment observation.
- \(T\): user task.
- \(A_t=\{a_1,\ldots,a_{t-1}\}\): prior actions.
- \(h_t\): current HTML.
- \(i_t=I(h_t)\): rendered screenshot.

Plainly: the agent chooses its next action from what the page looks like, what its HTML says, the user’s request, and what it already did.

Equation (1) was read from supplied text, not a page image.

## Stealthiness constraint

\[
I(h)=I(h_{\mathrm{adv}}).
\]

- **Location:** p. 3, §3.2.
- **Meaning:** original and attacked HTML should render identically.
- **Role:** formalizes invisibility to a human viewing the webpage.
- **Caveat:** the paper demonstrates use of non-rendered attributes but reports no independent perceptual or accessibility-tool test of this equality.

## Controllability transformation

\[
h'_{\mathrm{adv}}
=D(h_{\mathrm{adv}},r_{\mathrm{adv}},r'_{\mathrm{adv}}).
\]

- **Location:** pp. 3–4, §3.2.
- **Meaning:** replace the original malicious target with a new one inside a successful attacked page.
- **Role:** enables target changes without optimizing a new prompt.

## Equation (2): SFT loss

The displayed objective is substantively:

\[
\mathcal L_{\mathrm{SFT}}(\theta)
=-\mathbb E_h\sum_{i=1}^{n_1}
\log \pi_\theta(q_i^{(p)}\mid h).
\]

- **Location:** p. 5, Eq. (2).
- \(\theta\): prompter parameters.
- \(\pi_\theta\): learned prompt-generating policy.
- \(h\): HTML context.
- \(q_i^{(p)}\): successful/positive adversarial prompt.
- \(n_1\): number of positive prompts.

Minimizing the negative log-likelihood makes successful prompts more probable. The supplied work does not specify how the expectation over \(h\) is sampled or normalized.

## Equation (3): DPO loss

The objective compares the learned policy’s relative preference for a positive prompt against a negative prompt, measured relative to a fixed SFT reference policy:

\[
\mathcal L_{\mathrm{DPO}}(\theta)
=-\mathbb E_h
\sum_{i,j}
\log \sigma\!\left[
\beta\log
\frac{\pi_\theta(q_i^{(p)}\mid h)}
{\pi_{\mathrm{ref}}(q_i^{(p)}\mid h)}
-
\beta\log
\frac{\pi_\theta(q_j^{(n)}\mid h)}
{\pi_{\mathrm{ref}}(q_j^{(n)}\mid h)}
\right].
\]

- **Location:** p. 5, Eq. (3).
- \(q_i^{(p)}\): successful prompt.
- \(q_j^{(n)}\): failed prompt.
- \(\sigma\): logistic function.
- \(\beta\): deviation-control parameter.
- \(\pi_{\mathrm{ref}}=\pi_{\mathrm{SFT}}\): fixed reference policy.

Plainly: reward the new model for preferring successful prompts to failed prompts, while anchoring it to the SFT model. The numerical value of \(\beta\) is not supplied.

# 14. Interpretation and Discussion

The results answer the paper’s objectives as follows:

- **Automated black-box attack:** supported by high ASR on two proprietary backends without reported weight or gradient access.
- **Value of feedback:** supported by the 28.0-point SFT-to-DPO mean improvement and weak GPT-4V→Gemini transfer.
- **Controllability:** supported strongly for literal target replacement.
- **Stealth-oriented structure:** supported procedurally by hidden-attribute placement and high transfer from `aria-label` to `id`; human detectability itself is not empirically measured.
- **Defense weakness:** supported for the three tested prompt-format defenses, all leaving mean ASR at least 88.8%.

The domain results reveal more nuance than the headline averages. Finance is highly vulnerable in the standard setting but comparatively sensitive to changed injection position and defenses. Medical is the one domain with substantial GPT-4V→Gemini transfer, at 60%. Housing and Cooking remain at 100% under every tested defense.

The work also shows that natural-language attacks are not smoothly predictable: changing one pronoun or adding one word can reverse the outcome. The authors interpret this as motivation for learning from both positive and negative feedback rather than manually designing prompts.

“Incorporating DPO leads to a significant improvement” is empirically plausible in the ordinary sense, but the supplied paper reports no statistical hypothesis test. Likewise, claims of “real-world attacks” refer to tasks built from real-world website data; the document does not describe unauthorized live transactions.

# 15. Contributions and Novelty

## Conceptual

A threat model for targeted web-agent action manipulation that separates operation, argument, and target element and attacks the argument while preserving the others.

## Methodological

A structured hidden-HTML design intended to satisfy invisibility and target substitutability.

## Algorithmic

A two-stage SFT+DPO adversarial prompter trained from binary black-box agent feedback.

## Systems/security

A red-teaming workflow that attacks screenshot-and-HTML-based agents without victim weights, logits, or gradients.

## Experimental

Evaluation on 440 selected tasks, including baseline comparisons, model backends, training ablation, HTML variations, target changes, cross-model transfer, defenses, and qualitative cases.

## Empirical

Evidence that the tested SeeAct configurations are highly susceptible and that simple prompt-format defenses do not reduce mean ASR below 88.8%.

No new dataset or theorem is contributed. The authors release code, but the code artifact was not supplied and cannot be assessed here. [A: pp. 1–2]

# 16. Limitations

## Authors' stated limitations

Appendix D identifies two principal limitations:

1. Victim feedback must be collected before optimization and used offline; the system does not adapt in real time.
2. Evaluation uses step-based ASR because current agents have relatively low complete-task success. This does not fully measure risk across an entire user request or task flow.

The authors propose online feedback and end-to-end interactive evaluation as remedies. [A: pp. 9, 12]

## Additional evidence-based analyst observations

These are analyst observations, not author-admitted limitations:

- Only one web-agent framework, SeeAct, is tested, although it has two backends.
- The four domains are a selected 440-task subset of a much broader dataset; the exact task-selection criteria and per-domain counts are absent.
- The metric requires exact malicious action matching but gives no denominator counts or uncertainty based on trials.
- Means and standard deviations across four domains do not establish statistical generalization.
- No confidence intervals, statistical tests, repeated-run variation, or random seeds are reported.
- “Stealthiness” is principally guaranteed by construction; no user study, accessibility audit, browser-variation test, or detector evaluation is described.
- Controllability is tested only by replacing target arguments in already successful attacks, which conditions the analysis on prior success.
- Only one alternative HTML field and one position change are tested.
- Baselines do not have identical access and adaptation conditions, complicating a pure algorithmic comparison.
- Hardware, training cost, query cost, and positive/negative dataset sizes are missing.
- The supplied paper contains several presentation inconsistencies: “Algorithm 1 in ??,” conflicting Figure 2 algorithm labeling, `arial-label`, and “AdvWeb.”

# 17. Threats to Validity

## Internal validity

Observed improvements are consistent with DPO’s addition, but DPO also adds another training phase. The design does not separately control for training duration or extra optimization. Candidate-generation and feedback-partition details are incomplete.

## Construct validity

Step-based exact-triplet ASR measures targeted local manipulation well, but not whether an entire harmful task completes. Conversely, it may count a dangerous step even if a later safeguard reverses it.

## External validity

Generalization is limited by one agent framework, two backends, four domains, and selected tasks. The paper states applicability to other screenshot/HTML agents but does not test that claim here.

## Statistical conclusion validity

No inferential statistics, confidence intervals, or trial-level variance are supplied. “Mean ± Std” is across four domain rates rather than an explicitly described repeated-sampling distribution.

## Ecological validity

Mind2Web uses real-world website data, but the supplied description does not establish live deployment, real financial execution, or full interactive task completion.

## Reproducibility

Core model names, learning rates, batch sizes, and split sizes are supplied. Reproduction is hindered by missing seeds, optimizer and decoding details, \(\beta\), hardware, per-domain counts, generated dataset sizes, and uninspected released code.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Develop a prompter that learns from online black-box feedback.
- Evaluate end-to-end attacks in real-time interactive web environments.
- Monitor ASR across the entire task flow.
- Explore more sophisticated controllability transformations, including hashing-based mappings.
- Develop proactive detection and stronger mitigation strategies. [A: pp. 4, 9, 12]

## B. Additional open questions

- Do the attacks transfer to web-agent architectures other than SeeAct?
- How detectable are hidden attributes to security scanners, accessibility pipelines, or anomaly detectors?
- How many victim queries and how much computation are required per task/backend?
- Would defenses that separate trusted user instructions from untrusted webpage text outperform prompt-only warnings?
- How often does a successful malicious step produce actual end-to-end harm?
- Does adversarial training on AdvAgent prompts create robust defense or only prompt-specific resistance?
- How stable are results across random seeds, webpage updates, browsers, and model-version changes?
- Can attacks alter operations or elements, rather than only arguments, while preserving controllability?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| AdvAgent | The paper’s learned framework for generating hidden targeted attacks on web agents |
| ASR | Attack success rate: percentage of tested steps producing the exact malicious action |
| Black-box | The attacker sees behavior but not model weights, logits, or gradients |
| DPO | Direct Preference Optimization; trains a model to prefer successful prompts over unsuccessful ones |
| HTML | Structured source representation of a webpage |
| Indirect prompt injection | Malicious instruction supplied through external content rather than directly by the user |
| LLM | Large language model |
| VLM | Vision-language model |
| RLAIF | Reinforcement learning from AI feedback |
| SFT | Supervised fine-tuning on examples treated as correct |
| SeeAct | The victim web-agent framework used in the experiments |
| Stealthiness | Requirement that attacked HTML leave the visible page unchanged |
| Controllability | Ability to replace the malicious target without re-optimization |
| \(T\) | User task |
| \(h_t\) | HTML at step \(t\) |
| \(h_{\mathrm{adv}}\) | Adversarially modified HTML |
| \(i_t=I(h_t)\) | Rendered screenshot |
| \(A_t\) | Prior action sequence |
| \(\Pi\) | Victim agent policy/backend |
| \(a_t\) | Agent action at step \(t\) |
| \(a=(o,r,e)\) | Action triplet: operation, argument, HTML element |
| \(r_{\mathrm{adv}}\) | Maliciously substituted argument |
| \(q\) | Generated adversarial prompt |
| \(q^{(p)},q^{(n)}\) | Successful and failed prompts |
| \(\pi_\theta\) | Learned adversarial prompter |
| \(\pi_{\mathrm{ref}}\) | Fixed SFT reference policy in DPO |
| \(\beta\) | DPO reference-deviation parameter; value not reported |
| \(\sigma\) | Logistic function |
| \(D\) | Deterministic target-replacement function |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Full Mind2Web size | 2,350 | tasks | 137 sites, 31 domains | Author-reported | p. 6, §5.1 |
| Selected evaluation corpus | 440 | tasks | Four critical-event domains | Author-reported | pp. 2, 6 |
| Training split | 240 | tasks | Selected subset | Author-reported | p. 6 |
| Test split | 200 | tasks | Selected subset | Author-reported | p. 6 |
| Candidate prompts | 10 | per task | GPT-4 generator | Author-reported | p. 6 |
| Sampling temperature | 1.0 | — | Initial prompt generation | Author-reported | p. 6 |
| SFT learning rate | \(10^{-4}\) | — | Mistral-7B prompter | Author-reported | p. 6 |
| SFT batch size | 32 | instances | Training stage 1 | Author-reported | p. 6 |
| DPO learning rate | \(10^{-4}\) | — | Training stage 2 | Author-reported | p. 6 |
| DPO batch size | 16 | instances | Training stage 2 | Author-reported | p. 6 |
| AdvAgent GPT-4V mean ASR | 97.5 ± 2.0 | % | Four domains | Author-reported / visually readable | Table 1, p. 6 |
| Best GPT-4V baseline | 64.3 ± 16.7 | % | InjecAgent | Author-reported / visually readable | Table 1 |
| AdvAgent Gemini mean ASR | 99.8 ± 0.3 | % | Four domains | Author-reported / visually readable | Table 1 |
| Best Gemini baseline | 28.0 ± 23.0 | % | InjecAgent | Author-reported / visually readable | Table 1 |
| SFT-only mean ASR | 69.5 | % | GPT-4V | Visually readable | Fig. 3, p. 7 |
| SFT+DPO mean ASR | 97.5 | % | GPT-4V | Visually readable | Fig. 3 |
| DPO absolute gain | 28.0 | percentage points | \(97.5-69.5\) | Analyst-derived | Fig. 3 |
| Different-position mean ASR | 71.0 ± 26.1 | % | GPT-4V | Author-reported / visually readable | Table 2 |
| Different-field mean ASR | 97.0 ± 1.7 | % | `aria-label`→`id` | Author-reported / visually readable | Table 2 |
| GPT-4V controllability | 98.5 ± 2.7 | % | New target replacement | Author-reported / visually readable | Table 3 |
| Gemini transfer ASR | 18.0 ± 24.4 | % | Prompts transferred from GPT-4V | Author-reported / visually readable | Table 4 |
| Direct Gemini ASR | 99.8 ± 0.3 | % | Feedback-guided direct attack | Author-reported / visually readable | Table 4 |
| Direct-vs-transfer gap | 81.8 | percentage points | \(99.8-18.0\) | Analyst-derived | Table 4 |
| Lowest defended mean ASR | 88.8 | % | Instruction Defense | Author-reported / visually readable | Table 5 |
| Gemini controllability | 100.0 ± 0.0 | % | All four domains | Author-reported / visually readable | Table 6 |
| Transfer-test sample | 100 | attacks | \(25\) per domain × \(4\) domains | Analyst-derived | p. 8, §5.3 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| AdvAgent effectively attacks tested web agents | 97.5% GPT-4V; 99.8% Gemini | X1, Table 1 | p. 6 | Strong within tested step-level setting |
| AdvAgent outperforms baselines | All domain means exceed all reported baselines | X1, Table 1 | p. 6 | Strong descriptive evidence; no significance tests |
| Victim feedback improves attack quality | 69.5% SFT → 97.5% SFT+DPO | X2, Fig. 3 | p. 7 | Strong ablation evidence, but added training is not separately controlled |
| Prompts tolerate HTML-field changes | 97.0% mean after field replacement | X3, Table 2 | p. 7 | Strong for one tested alternative field |
| Position affects success | Mean falls to 71.0%; Finance to 26.0% | X3, Table 2 | p. 7 | Strong descriptive evidence |
| Successful prompts are controllable | 98.5% GPT-4V; 100% Gemini after target replacement | X4, Tables 3, 6 | pp. 8, 12 | Strong but conditional on initially successful attacks |
| Cross-model transfer is poor | 18.0% transfer versus 99.8% direct | X5, Table 4 | p. 8 | Strong for GPT-4V→Gemini direction |
| Prompt defenses offer limited protection | All defended means remain 88.8–89.8% | X6, Table 5 | pp. 8–9 | Strong for these three defenses and Gemini |
| Small wording changes can determine success | Two paired examples | X7, Fig. 4 | pp. 8–9 | Illustrative, not population-level evidence |
| Hidden prompts can alter action arguments | Microsoft→NVIDIA; Tylenol→Aspirin | Figs. 1 and 5 | pp. 2, 13 | Direct qualitative demonstrations |
| The attack is stealthy | Prompt placed in non-rendered attribute; unchanged-rendering constraint | Method, Fig. 1 | pp. 2–4 | Design-based support; no empirical human/detector test |

# 22. Very Simple Explanation

Imagine asking a computer assistant to buy Microsoft stock. The assistant looks at the website, but the website contains a hidden note that says, in effect, “Ignore the real request and type NVIDIA.” You cannot see that note on the screen, but the assistant reads the website’s underlying code and follows it.

AdvAgent learns how to write hidden notes that work reliably. It first studies notes that succeeded, then compares successful and failed notes to learn tiny wording differences. In one example, changing only “you” to “I” changed a failed attack into a successful one.

In the tests, these hidden instructions redirected the agent roughly 98–100% of the time. Three simple defenses reduced the attacks somewhat, but even the best one still left an 88.8% average success rate. The paper’s warning is that web agents should not treat arbitrary webpage text as trusted instructions merely because it appears near a relevant form field.

The result does not show that every web agent will always fail, and it measures individual action steps rather than complete harmful transactions. It does show a serious weakness in the particular agent framework and backends tested.

# Completeness Audit

## Inventory

| ID | Original item | Location |
|---|---|---|
| S1 | Abstract | p. 1 |
| S2 | Introduction | pp. 1–2 |
| S3 | Related Work | pp. 2–3 |
| S4 | Targeted Black-box Attack on Web Agents | pp. 3–4 |
| SS4.1 | Web-agent formulation | p. 3 |
| SS4.2 | Threat model | pp. 3–4 |
| SS4.3 | Attack challenges | p. 4 |
| S5 | AdvAgent framework | pp. 4–5 |
| SS5.1 | Automatic attack and feedback collection | pp. 4–5 |
| SS5.2 | Prompter-model training | p. 5 |
| S6 | Experiments | pp. 6–8 |
| SS6.1 | Experimental settings | p. 6 |
| SS6.2 | Effectiveness | pp. 6–7 |
| SS6.3 | In-depth analysis | pp. 7–8 |
| SS6.4 | Case studies | pp. 8–9 |
| S7 | Mitigation and blue-teaming | pp. 8–9 |
| S8 | Conclusion | p. 9 |
| S9 | Acknowledgements and impact statement | p. 9 |
| S10 | References | pp. 10–11 |
| A1–A4 | Appendices A–D | pp. 12–13 |
| F1–F5 | Figures 1–5 | pp. 2, 4, 7, 9, 13 |
| T1–T6 | Tables 1–6 | pp. 6–8, 12 |
| ALG1–ALG2 | Algorithms 1–2 | p. 5 |
| E1–E3 | Equations (1)–(3) | pp. 3, 5 |
| X1–X7 | Main comparison, ablation, structural transfer, controllability, backend transfer, defenses, cases | pp. 6–13 |

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Orientation and results |
| Introduction | Yes | Yes | Fully represented | Problem, gap, contributions |
| Related Work | Yes | Yes | Represented in compressed form | Categories and claimed shortcomings retained |
| §3.1 formulation | Yes, text only | Yes | Fully represented | Page 3 was not visually rendered |
| §3.2 threat model | Yes, text only | Yes | Fully represented | Objectives, capabilities, constraints |
| §3.3 challenges | Yes | Yes | Fully represented | Discreteness, black-box access, scalability |
| §4 framework overview | Yes | Yes | Fully represented | Architecture and design |
| §4.1 data collection | Yes | Yes | Fully represented | Candidate generation and feedback partition |
| §4.2 training | Yes | Yes | Fully represented | SFT and DPO |
| §5.1 settings | Yes | Yes | Fully represented | Dataset, splits, models, hyperparameters, baselines, metric |
| §5.2 effectiveness | Yes | Yes | Fully represented | Main comparison |
| §5.3 in-depth analysis | Yes | Yes | Fully represented | All four analyses separated |
| §5.4 case studies | Yes | Yes | Fully represented | Both prompt pairs |
| §6 defenses | Yes | Yes | Fully represented | All three defenses |
| §7 conclusion | Yes | Yes | Fully represented | Claims and caveats |
| Acknowledgements | Yes | Minimally | Deliberately compressed | Funding is non-methodological |
| Impact statement | Yes | Yes | Represented in compressed form | Defensive intent and risk domains retained |
| References | Yes, text only | Categorically | Represented in compressed form | Individual bibliographic entries not repeated |
| Appendix A | Yes | Yes | Fully represented | Table 6 |
| Appendix B | Yes | Yes | Fully represented | Figure 5 cases |
| Appendix C | Yes | Yes | Represented in compressed form | Additional LLM red-teaming categories retained |
| Appendix D | Yes | Yes | Fully represented | Both stated limitations |
| Figure 1 | Visually inspected | Yes | Fully represented | Scenario diagram |
| Figure 2 | Visually inspected | Yes | Fully represented | Cross-reference inconsistency recorded |
| Figure 3 | Visually inspected | Yes | Fully represented | All plotted values recorded |
| Figure 4 | Visually inspected | Yes | Fully represented | Both paired cases |
| Figure 5 | Visually inspected | Yes | Fully represented | Both examples; “AdvWeb” discrepancy recorded |
| Tables 1–6 | Visually inspected | Yes | Fully represented | Important cells and all domain patterns covered |
| Algorithm 1 | Visually inspected | Yes | Fully represented | Inputs, messages, output described |
| Algorithm 2 | Visually inspected | Yes | Fully represented | Collection, partition, SFT, DPO described |
| Equation (1) | Text inspected | Yes | Fully represented with limitation | No direct page image |
| Equations (2)–(3) | Visually/textually inspected | Yes | Fully represented | OCR/typesetting sensitivity disclosed |
| X1–X7 | Yes | Yes | Fully represented | Separate experiment register supplied |
| Explicit research questions | Yes | Yes | Not present | Objectives were not converted into claimed formal RQs |
| Formal hypotheses | Yes | Yes | Not present | Tested propositions distinguished from hypotheses |
| Supplementary material | N/A | Yes | Missing from supplied material | None referenced as a separate artifact |
| Released code | No | Yes | Inaccessible | Link stated, artifact not supplied |

## Missing or inaccessible material

- Pages 3, 10, and 11 were not supplied as rendered images; their native/extracted text was available.
- The released code repository was not supplied and was not inspected.
- No separate supplementary files were supplied.
- Hardware, random seeds, optimizer details, \(\beta\), training duration, query cost, trial denominators, per-domain sample counts, and positive/negative training-set sizes are absent from the paper.

## Uncertain interpretations

- Equation (3)’s extracted line layout makes the exact typography of expectation and summation scopes mildly uncertain, though its DPO comparison is clear.
- Figure 2 contains the unresolved phrase “Algorithm 1 in ??” and conflicting algorithm labeling.
- `arial-label` appears in qualitative visuals/text where the method says `aria-label`.
- Figure 5 calls the optimizer “AdvWeb,” inconsistent with “AdvAgent.”
- “Significant improvement” is not accompanied by a statistical test.
- The precise operational verification of \(I(h)=I(h_{\mathrm{adv}})\) is not described.

## Deliberately compressed material

- Individual reference entries on pp. 10–11 were not reproduced; their substantive categories and methodological positioning were summarized.
- Acknowledged funding sources were not itemized because they do not affect the reported method or findings.
- Repeated statements of the headline 97.5%, 99.8%, and 88.8% results were consolidated into traceable tables.
- Appendix C’s citation-by-citation history was compressed into its methodological categories and author-stated gap.

## Potential omissions

Every major section, substantive subsection, experiment, figure, table, algorithm, equation, contribution, author-stated limitation, and appendix identified in the inventory is represented. The only uninspected artifacts are the externally hosted code and any implementation details not contained in the supplied paper.