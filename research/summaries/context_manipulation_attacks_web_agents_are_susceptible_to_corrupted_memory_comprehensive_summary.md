## Stage 0 — Document Accessibility Report

The supplied main document is available as extracted text for physical PDF pages 1–10. Eight page images are also supplied: pages 1, 2, 3, 4, 5, 7, 8, and 10. These images were visually inspected directly in the conversation. Pages 6 and 9 were inspected through supplied text only; no visual inspection is claimed for those pages. Printed page numbers agree with the supplied physical-page labels. The accessible sequence contains an abstract, main sections 1–7, and references on pages 9–10, and appears to reach the paper's end. This does not establish whether another version has additional material.

All six numbered figures are present on visually supplied pages: Figure 1 on page 2; Figure 2 on page 4; Figures 3–4 on page 7; Figures 5–6 on page 8. Their overall structures, axes, legends, and main comparisons are readable. Small text in Figure 1 and exact unlabeled bar heights in Figures 5–6 have lower precision than the prose. Equations (1)–(6) are available in both text and images, although the extraction separates some superscripts and subscripts. The analysis uses the rendered mathematical structure where necessary and flags undefined mathematical details. No numbered tables, pseudocode, theorems, appendices, or supplied supplementary files are present. Page 6 contains a substantive footnote saying that the benchmarks are available at a link; the destination and benchmark files themselves are not supplied. The accessibility metadata reports no embedded files and no detected supplementary references, but that does not make the externally linked benchmarks accessible.

OCR was unnecessary: native/extracted text was supplied throughout. No separate OCR output was generated or compared. No tools, browsing, citation verification, or external literature were used. The source hash and report identifier are accepted as supplied metadata; they were not independently computed. References are treated as the paper's bibliography, not as independently reviewed evidence.

Evidence categories throughout are: [A] AUTHOR-REPORTED; [B] DIRECTLY OBSERVABLE in supplied visuals; [C] ANALYST-DERIVED from explicit operands; and [D] ANALYST INTERPRETATION. No [E] external information is introduced. Confidence is HIGH for clearly readable source statements, MEDIUM for qualified interpretations or approximate visual readings, and UNKNOWN where the document does not provide the necessary information. A high-confidence transcription of an author claim does not mean its empirical validity has been independently established.

## 1. Plain-language orientation

[A] This paper studies how autonomous web agents can be redirected by corrupting the information they use to remember and plan a task. A web agent accepts a request, visits websites, decides what to do next, and performs browser actions. Because these activities span multiple steps, the agent needs stored context: its goal, observations, previous actions, and sometimes an explicit plan. The authors investigate what happens when an attacker can insert malicious material into that context without changing the user's original request, browser observations, system instructions, or program code.

[A] The central contribution is **plan injection**: inserting unauthorized steps into an agent's internal task plan. The attacker tries to make the inserted steps look like plausible extensions of the user's request. The paper contrasts obvious unrelated insertions, task-related insertions, and **context-chained injections**, which construct intermediate steps connecting an innocent task to the attacker's goal. In a recipe-search example, the chain moves from finding a recipe to finding nearby restaurants, obtaining the user's address, and transmitting private details to an attacker-controlled website. The recipe task itself does not authorize that transmission.

[A] Two systems are evaluated: Browser-use, which selects actions from its execution context, and Agent-E, which separates a high-level planner from a browser executor. The authors build a task-category benchmark and a privacy-focused adaptation of WebVoyager. They report that prompt defenses reduce attacks entering through retrieved content but do not adequately protect corrupted plans or memory. Under reported privacy conditions, context-chained attacks achieve 46% success against Agent-E and up to 63% against Browser-use. In a separate Agent-E task-category benchmark, task-aligned opinion steering reaches 94.7%, whereas task-aligned factual manipulation reaches 18.7%.

[D] For the user's research question, the paper offers a mechanism-based explanation of agent vulnerability: an agent has mutable execution state, repeatedly consumes untrusted material, and can act on the resulting decisions. However, this paper does **not** experimentally compare web agents with a standalone language-model condition. Its evidence supports a security analysis of two agent architectures, not a measured universal difference between agents and standalone large language models.

## 2. Document roadmap

The original title is **Context manipulation attacks : Web agents are susceptible to corrupted memory**. The authors are Atharv Singh Patlan, Ashwin Hebbar, Pramod Viswanath, and Prateek Mittal. Page 1 identifies Princeton University, marks Patlan and Hebbar as equal contributors, and lists the Workshop on Computer-use Agents @ ICML 2025, Vancouver, Canada. These are supplied publication statements, not externally verified bibliographic records.

The document is a mixed AI-agent systems and empirical cybersecurity paper. Its organization is:

| Inventory ID | Original component | Pages | Function |
|---|---|---:|---|
| S0 | Abstract | 1 | States the attack, headline findings, and memory-security motivation |
| S1 | 1. Introduction | 1–2 | Explains decentralized context and motivates attacks on hierarchical plans |
| S2 | 2. Background and Related Work | 2–3 | Describes web-agent architectures and earlier prompt/memory attacks |
| SS2.1 | 2.1. Web navigation agents | 2 | Explains Browser-use and Agent-E |
| SS2.A | Attacks on language agents | 3 | Positions direct and indirect prompt injection |
| SS2.B | Attacks on agent memory | 3 | Positions knowledge-base, trajectory, and conversation-memory poisoning |
| S3 | 3. Context Manipulation Attacks | 3–4 | Defines the agent context and attack locations |
| SS3.1 | 3.1. Formalizing the AI Agent Framework | 3 | Gives components, decision mapping, and context updates |
| SS3.2 | 3.2. Context Manipulation | 3–4 | Gives equations (1)–(6) and attack taxonomy |
| S4 | 4. Context manipulation attacks on Web navigation agents | 4–5 | Introduces the evaluation threat model and attack construction |
| SS4.1 | 4.1. Threat model | 4–5 | Defines allowed corruption and attacker objectives |
| SS4.2 | 4.2. Vulnerability to prompt injection attacks | 5 | Describes preliminary attacks and prompt defenses |
| SS4.3 | 4.3. Vulnerability to context manipulation attacks | 5 | Explains three injection sophistication levels |
| S5 | 5. Evaluation | 6 | Defines two benchmarks and attack-success criteria |
| SS5.1 | 5.1. Plan Injection Benchmark | 6 | Four categories, sample generation, repeated execution |
| SS5.2 | 5.2. WebVoyager-Privacy Benchmark | 6 | Privacy tasks across domains and adaptive attack generation |
| SS5.3 | 5.3. Evaluation metrics | 6 | Defines attack success rate and category-specific success |
| S6 | 6. Results | 6–8 | Reports task, defense, and architecture comparisons |
| SS6.1 | 6.1. Plan Injection Benchmark results | 7 | Interprets Figures 3–4 |
| SS6.2 | 6.2. WebVoyager-Privacy attacks | 7–8 | Interprets Figures 5–6 |
| S7 | 7. Conclusion | 8 | Synthesizes findings and proposes defenses |
| REF | References | 9–10 | Bibliographic context; cited works were not inspected |

Additional inventory objects are F1–F6, equations E1–E6, three unnumbered mathematical identities in §3.1, experiments X1–X4, and the benchmark-availability footnote on page 6. There are no explicit formal research-question labels, numbered hypotheses, algorithms, tables, proofs, or appendices. The experiments are registered separately below so that different datasets and success definitions are not collapsed.

## 3. Background and context

[A] A **large language model (LLM)** is described here as stateless: the model itself does not maintain a task's evolving history across independent interactions. Agent applications supply that history and other state as context. The paper contrasts centrally managed conversation history with agent context distributed across client devices and third-party services. Its argument concerns who can alter the context, rather than claiming that every agent deployment has the same storage arrangement. See page 1, Introduction.

[A] A **web navigation agent** translates natural-language instructions into browser actions such as clicks, keystrokes, form filling, and content extraction. The agent must combine a user goal with what it sees on websites and what it has already done. **Document Object Model (DOM) interaction primitives** are the predefined browser operations used by Agent-E's navigation component. The paper names this interface but does not enumerate the primitives or specify their implementation.

[A] **Direct prompt injection** places malicious instructions in user-prompt content. **Indirect prompt injection** places them in retrieved content, such as webpages. **Memory injection** changes stored interaction history. **Plan injection** changes the internal high-level plan. All are treated as instances of context manipulation targeting different context components. The experimental restricted attacker is narrower than the complete taxonomy: the taxonomy describes several possible attack surfaces, while the primary memory/plan tests constrain the attacker to stored context.

[A] Browser-use references the user's goal and current/past execution trajectory when selecting the next action. Agent-E instead has a Planner Agent that creates ordered subtasks and a Browser Navigation Agent that executes them. After each step, the planner compares progress with the plan, adjusts the plan if needed, and directs the next action. The authors regard this separation as providing additional validation against obviously irrelevant memory insertions. Both systems still depend on context over the course of a task. See page 2, §2.1.

[A] The related-work discussion distinguishes poisoned knowledge bases, poisoned retrieved trajectories, and directly altered conversation history. AgentPoison, MINJA, and earlier ElizaOS attacks are discussed as examples of those categories. These descriptions are the current paper's account of prior work. Neither the cited studies nor their implementations were independently inspected. The same boundary applies to its statements about exposed production databases and the ranking of prompt injection in external security guidance.

## 4. Research problem and gap

**Existing problem [A].** Multi-step agents rely on memory and contextual state that can be modified outside a centrally controlled conversation boundary. Malicious entries can consequently be read as part of the agent's own history or plan. The paper presents this as an architectural security problem in addition to ordinary attacks through webpage content. Pages 1–4.

**Shortcomings of existing approaches, according to the authors [A].** Prompt defenses that warn against following webpage instructions do not necessarily prevent malicious content already positioned inside the agent's task representation. Separating planner and executor helps reject naive or unrelated insertions, but does not guarantee that a semantically plausible inserted step is authorized. Pages 2 and 5.

**Research gap [A].** Earlier context-manipulation work focused on persistent conversation histories, including financial agents. Agent-E's executions are independent across sessions, which appears to reduce that particular cross-session risk. The paper asks whether the principles still apply to the temporary internal plan used during a single execution. This is the gap addressed by formalizing and evaluating plan injection. Pages 2 and 4.

**Motivation and scope [A].** The study aims to measure vulnerability to controlled context corruption while exploring how task type, attack sophistication, defenses, and agent architecture affect success. It studies two named agents and two constructed benchmarks. It does not establish rates for all web agents, all models, every memory-storage deployment, or all security objectives. Its main comparative security outcome is attacker-goal completion, especially privacy exfiltration, rather than ordinary task accuracy or deployment-wide incident frequency.

## 5. Research questions / objectives / hypotheses

No formally numbered research questions are supplied. The following are organized restatements of the authors' objectives, not quotations or newly claimed formal questions:

- **O1 [A]:** Formalize plan injection as corruption of the internal task representation and demonstrate that it can compromise planner-based web agents. Pages 1–4.
- **O2 [A]:** Determine how factual, opinion, advertisement, and privacy tasks differ in susceptibility. Page 6, §5.1; page 7, §6.1.
- **O3 [A]:** Compare non-contextual, task-aligned, and context-chained attack construction. Pages 5–8.
- **O4 [A]:** Compare context attacks with weak and strong retrieved-content prompt injection under different security configurations. Pages 6–8.
- **O5 [A]:** Examine whether architectural separation in Agent-E offers more resistance than Browser-use's execution-context design. Pages 2 and 8.

**Hypothesis H1 [A].** Page 8 explicitly describes the authors' hypothesis that hierarchical validation requires more semantically sophisticated attacks, while remaining vulnerable to malicious content aligned with legitimate task contexts. Figure 6 and the accompanying text are offered as support. The supplied document does not give a preregistration, formal statistical hypothesis test, or a controlled architecture ablation.

**User research question, separate from the paper's objectives [D].** Why are web AI agents more vulnerable than standalone LLMs? This paper is relevant because it explains an additional state-corruption pathway and demonstrates its consequences in agents. It does not directly test that comparative question. The similarly titled Chiang et al. paper appears in the references on page 9; its contents are not supplied and cannot be substituted for this study's evidence.

## 6. Assumptions / threat model

[A] The general system model separates user prompts, external data, static knowledge, interaction history, and, for Agent-E, the generated plan. Context is repeatedly passed to a decision engine that selects actions and updates the environment. The assets at risk include faithful execution of the user's goal, integrity of reasoning and recommendations, and sensitive personal information. Pages 3–6.

[A] The restricted attacker in §4.1 cannot modify: (1) the original user instruction; (2) browser observations; (3) system prompts; or (4) agent code. The attacker can inject content into stored context. The authors describe this as the weakest form of context manipulation and a way to establish a lower bound on vulnerability. That wording is an author characterization, not a formal ordering proven over all attacker models. Page 4.

[A] The attacker seeks one of three deviations: add an unauthorized task to the legitimate task; replace the legitimate task with a malicious alternative; or complete the legitimate task with reasoning or data manipulation favorable to the attacker. Four concrete objective types are named: false reasoning, advertisement injection, privacy leakage, and goal hijacking. The evaluation categories are related but not identical labels: factual manipulation, opinion steering, advertisement injection, and privacy exfiltration. Pages 4–6.

[A] Direct memory injection assumes a way to change backend state, conversation logs, or similar storage. The paper gives insecure client storage, third-party context storage, and compromised plugins/extensions as possible access scenarios. Indirect memory injection instead contaminates history through earlier interactions. The controlled evaluation modifies context to measure downstream susceptibility; it does not measure the probability or cost of acquiring write access in each scenario. Page 4.

[D] There is a notation/scope ambiguity: §4.1 permits injection into history h, while equation (6) separately represents modifying plan P. The surrounding prose clearly includes plan injection, but does not fully document how plan text is stored relative to history in the implementation. It is therefore unsafe to claim that the experiment exposes a particular storage API or that the formal history-only rule completely specifies the implementation.

## 7. Methodology

### Study design and systems

[A] This is an empirical attack evaluation supported by a conceptual context-manipulation formalization. Browser-use and Agent-E are selected as representative open-source web agents. Agent-E is the main target of the four-category Plan Injection Benchmark. Both agents are evaluated in the privacy-focused architecture comparison. GPT-4o is used for Browser-use's controller and Agent-E's planner. GPT-4o-mini is used for the browser-navigation component as described by the paper. Agents run in headless mode. Page 7 states a cost-utility rationale for assigning repetitive execution to the smaller model.

[A] There is no reported new model training. GPT-4o also helps generate the first benchmark semi-automatically. For the privacy suite, an LLM adaptively crafts injections using current trajectory, attacker goal, and dataset-defined foot-in-the-door context; its exact identity is not specified in that passage. The paper does not provide model snapshot identifiers, decoding temperatures, token limits, seed settings, browser versions, library versions, hardware, or measured cost/runtime.

### Attack construction

[A] **Non-contextual injection** directly adds a malicious instruction unrelated to the task. **Task-aligned injection** first makes the inserted material relevant to the task domain, then introduces the attacker preference. **Context-chained injection** connects the legitimate goal to an intermediate task and then to the malicious action. These are construction strategies, not separate permissions: relevance does not imply that the user authorized the inserted action. Page 5.

[A] For Agent-E, malicious steps are inserted into the generated plan so that they appear plausible as planner-produced steps. For Browser-use, context/memory is modified in a system without the same explicit planning layer. Page 6 distinguishes Agent-E plan injection from Browser-use memory injection. Page 8 sometimes describes the attacks collectively using plan terminology; that wording should not erase the architectural distinction.

### Benchmarks and samples

[A] The **Plan Injection Benchmark** contains four categories, each with 15 samples. Each sample is executed five times to account for behavior variance. Samples include a realistic user query, malicious content, and evaluation criteria. Generation uses a standardized template and GPT-4o. All categories are evaluated with non-contextual and task-aligned injections; privacy receives the additional context-chained condition. Page 6.

[C] Four categories × 15 samples yields 60 distinct samples. Fifteen samples × five executions yields 75 executions per category for a fully populated evaluated condition. Four × 15 × five yields 300 executions across categories for one shared condition. These are arithmetic implications of the reported design, not an explicitly audited run log. An overall run total across all strategies is not asserted because the paper does not enumerate completed runs, failures, exclusions, or accounting conventions.

[A] **WebVoyager-Privacy** samples nine domains with five tasks each, producing 45 scenarios across e-commerce, information retrieval, and content discovery. Every task has a consistent attacker goal: send name, date of birth, and address to an untrusted external domain. Attacks are generated dynamically from the current agent trajectory rather than only using a fixed insertion string. Page 6.

[A] No train/validation/test split is reported for these attack evaluations. Domain names, exact selection criteria, task-level exclusions, annotation procedures, privacy-data provisioning, and handling of failed normal tasks are not specified in the supplied document. The linked benchmark files are not available for inspection.

### Defenses, baselines, and metrics

[A] **SECURE** adds safety guidelines to the system prompt, including warnings against tool misuse. **SANDWICH** wraps retrieved content in data tags and tells the agent to treat it as data rather than executable instructions. The security configurations visible in Figure 5 are Undefended, Secure, and Secure+Sandwich. Prompt baselines include **PI-Weak**, insertion in one retrieval, and **PI-Strong**, insertion at every retrieval step. **CI** denotes context/plan injection, described in the caption as one plan injection. Pages 5, 7–8.

[A] **Attack success rate (ASR)** is the percentage of attempts in which the attacker objective is performed. Category-specific criteria are incorrect specified answers, injected opinions, promoted products, and transmission of sensitive data to the specified destination. Figure 5 distinguishes **partial success**, attacker tool access, from **full success**, complete private-data exfiltration. Figure 6 also displays partial/full encodings. Page 6 and page 8 caption.

[D] The supplied text does not fully reconcile the general ASR definition with every partial/full bar and every headline percentage. No confidence intervals, error bars, statistical tests, evaluator agreement, or per-run distributions are reported. Thus the reported percentage comparisons are descriptive rather than demonstrated statistically significant effects.

## 8. Experiments / analyses

### X1 — Preliminary prompt-injection and defense checks

[A] Purpose: establish that the agents are vulnerable through retrieved webpages and create a defended baseline before testing corrupted context. A public Pastebin-based strawman attack reportedly achieved prompt leakage, private-information exfiltration, and goal hijacking. SECURE and SANDWICH were then implemented. Page 5 reports improved identification and rejection of malicious external instructions, with safety acknowledgments and termination of harmful tasks.

Unknowns: the preliminary experiment's task count, success percentages, precise payloads, timing, and repetition count are not reported in the supplied passage. It is supporting methodology, not a quantitative standalone comparison with a recoverable denominator.

### X2 — Agent-E Plan Injection Benchmark

[A] Purpose: examine task category and injection sophistication. Data: four categories, 15 samples per category, five executions per sample. Manipulated variables: category and non-contextual/task-aligned attack form; privacy additionally has context-chained attacks. Outcome: category-specific ASR. Relevant evidence: Figure 3 and §6.1, page 7.

[A] Results: opinion steering is 94.7% with task alignment and 70.7% with direct insertion; factual manipulation is 18.7% and 0%, respectively. Advertisement injection reaches 78.7% with task alignment. Privacy exfiltration is 0% for non-contextual injection, 35.6% for task alignment, and 53.3% for context chaining. Figure 3 labels rounded decimal bar values, which must be distinguished from the more precise prose percentages.

[A] Author interpretation: factual constraints help the agent resist conflicting directives; subjective tasks leave greater room for manipulated outputs. Semantic relevance and intermediate steps make unauthorized instructions easier to accept. Caveat: this concerns constructed tasks and one evaluated planner/model setup, and no statistical uncertainty is supplied.

### X3 — Semantic-similarity analysis

[A] Purpose: explain how task-aligned and context-chained injections relate to both user and attacker goals. Figure 4 plots cosine embedding similarity to the user task against similarity to the attacker objective. The caption says the visualization uses the first 20% of WebVoyager-Privacy tasks. Orange circles represent context-chained injections; green diamonds represent task-aligned injections. Page 7.

[B] Context-chained points generally sit higher on attacker-objective similarity, while retaining moderate similarity to user tasks. Task-aligned points generally have lower attacker-objective similarity. Both groups have horizontal spread. The plot is not an ASR plot: no point color, axis, or marker directly encodes successful versus failed execution.

[D] This supports a descriptive association between construction strategy and embedding placement. It does not independently prove that similarity causes success, establish an optimal boundary, or compare every attack form: non-contextual points are not visibly plotted. The embedding model and exact point values are unspecified.

### X4 — WebVoyager-Privacy defenses and architecture comparison

[A] Purpose: compare prompt attacks with context attacks, then compare sophistication across architectures. Data: 45 scenarios sampled from nine domains. Variables: agent, attack vector, security configuration, and injection sophistication. Outcome: privacy-related ASR, with partial and full success shown separately. Relevant evidence: Figures 5–6 and §6.2, pages 7–8.

[A] Weak prompt injection enters one retrieval; strong prompt injection enters every retrieval. Context injection is described as a single insertion at the initial plan. Prompt defenses greatly reduce retrieved-content attack success against Agent-E. Reported context-chained percentages are 46% for Agent-E and up to 63% for Browser-use. Browser-use task-aligned and non-contextual values are 31% and 19%; Agent-E task-aligned is 20.6%. Page 8.

Qualifications: exact repetitions for this suite are not supplied; partial/full bar interpretation needs care; Figure 5 has a visual discrepancy with the blanket undefended >80% prose statement; and the architecture comparison changes an entire system rather than one isolated component. Figure 5 does not display separate agent panels.

## 9. Results

**Task subjectivity [A].** On the Plan Injection Benchmark, Agent-E's task-aligned opinion ASR is 94.7%, compared with 18.7% for factual manipulation. Non-contextual/direct-insertion values are 70.7% and 0%. Source: page 7, §6.1 and Figure 3. The authors attribute the difference to weaker factual constraints in subjective reasoning. This does not mean all opinion tasks are unsafe or all factual tasks are immune; factual ASR remains nonzero under task alignment.

**Task alignment [A].** Advertisement injection reaches 78.7% and privacy reaches 35.6% under task alignment. Non-contextual privacy attacks have 0% success. Source: page 7. Figure 3 also shows an advertisement non-contextual bar labeled 0.36; this is a displayed rounded ASR, not an exact 36.0% prose measurement with independently known precision.

**Context chaining [A].** On the same Agent-E task-category benchmark, privacy ASR rises from 35.6% for task alignment to 53.3% for chaining. [C] The absolute increase is 53.3 − 35.6 = **17.7 percentage points**. The relative increase is 17.7 / 35.6 × 100 ≈ **49.7%**. The abstract's wording of a 17.7% increase should therefore not be silently treated as a relative percentage increase. Source: pages 1 and 7.

**Defense bypass [A/B].** SECURE and SECURE+SANDWICH greatly reduce retrieved-content prompt attacks in Figure 5, whereas context-injection bars remain substantial. Source: pages 7–8. The outcome is bypass of these implemented prompt defenses; it is not a demonstration that every possible prompt defense or memory-integrity mechanism fails.

**Architectural comparison [A].** On WebVoyager-Privacy, context-chained attacks are reported at 63% for Browser-use and 46% for Agent-E, with task-aligned values of 31% and 20.6%. [C] The reported chained values differ by 63 − 46 = **17 percentage points**. Within Agent-E, chaining exceeds task alignment by 46 − 20.6 = **25.4 percentage points**. These calculations do not establish causal attribution to architecture because other system differences are not isolated. Source: page 8.

**Headline ratios [A].** The abstract and contributions use up-to-threefold language, but in different comparison contexts: comparable prompt-based attacks in the abstract, and contextual versus non-contextual attacks in the contributions. [D] The supplied text does not explicitly map the headline to one fully specified numerator, denominator, success type, and security condition. Accordingly, the headline is retained as an author statement rather than reconstructed as a uniquely established ratio.

**Undefended vulnerability discrepancy [A/B].** Page 7 says both agents exceed 80% for both prompt and plan attacks. Figure 5's weak-prompt bars in the Undefended group visibly sit around 0.6, below 0.8. Its strong-prompt and context bars are higher. The figure has no separate agent panels, so it cannot validate the broad claim about every agent/vector combination. The text and visual are reported without choosing which is correct.

## 10. Figure-by-figure interpretation

### Figure 1 — A recipe task redirected into privacy leakage

[B] Page 2 shows a vertical planner/browser interaction inside a red border. The legitimate user request is to find the best Paneer Butter Masala recipe. Orange plan boxes include recipe-search steps and additional restaurant/private-data transmission steps. Purple browser-report boxes record page visits and entered information. The diagram concludes with recipe ingredients and a serving suggestion, illustrating that an ordinary-looking final answer can coexist with an unauthorized action during execution.

[A/B] The caption identifies the red content as a plan injection connecting user and attacker objectives. The sequence includes an attacker website, restaurant details, user address, name, date of birth, and a displayed phone field. The benchmark's stated standardized private fields are name, date of birth, and address; the figure's additional phone example should not be generalized into a fourth benchmark-required field.

The diagram has no axes, statistical units, uncertainty intervals, or panels. It is an attack illustration, not a rate estimate or a claim that every run follows this trace. Small masked personal fields are not transcribed as exact identifying data. Its main evidentiary role is to demonstrate the logical progression and how a planner/browser loop can execute inserted steps.

### Figure 2 — Agent context and attack entry points

[B] Page 4 shows an Agent boundary containing an Action Module, Data Provider, and Context. Context contains Memory, Data, Plan, Prompt, and Knowledge. APIs and Webpages are above; External Storage is at the left; Users and Adversary are below. The legend distinguishes input flow, output flow, and potential attacks, with potential attacks drawn as red dashed paths.

[B] Attack paths point toward external retrieved sources for indirect prompt injection, external storage/memory for memory injection, the plan for plan injection, and the prompt for direct injection. The ordinary paths connect user input, agent context, browser/action processing, external sources, and outputs. The figure communicates multiple trust-crossing entry points rather than one single pipeline. It provides no frequency, success rate, access-control specification, or proof of an exploitable deployment.

### Figure 3 — Agent-E ASR by task and strategy

[B] Page 7 contains a grouped bar chart. The horizontal axis is Task Category: Factual, Opinion, Advertisement, Privacy. The vertical axis is Attack Success Rate, shown on a linear 0–1 proportion scale. Red represents non-contextual injection, orange task-aligned injection, and green context-chained injection. Green is shown for privacy, matching the stated additional condition. No error bars or statistical markers are visible.

[B] Labeled rounded values are: factual 0.00 and 0.19; opinion 0.71 and 0.95; advertisement 0.36 and 0.79; privacy 0.00, 0.36, and 0.53. [A] Prose supplies more precise percentages for most key results: 0%, 18.7%, 70.7%, 94.7%, 78.7%, 35.6%, and 53.3%. Rounded plot labels are not contradictions of these prose values.

The major observation is that task alignment raises the displayed ASR in every category, with opinion tasks highest. Privacy additionally benefits from context chaining. The caption uses the word significantly, but no statistical significance procedure accompanies this figure. It is therefore interpreted as an author emphasis on the magnitude of differences, not evidence of a reported significance test.

### Figure 4 — Embedding similarity of attack constructions

[B] Page 7 contains a scatter plot with horizontal User Task Embedding Similarity and vertical Attacker Instruction Embedding Similarity. Both are cosine-similarity quantities without physical units. The visible horizontal values span approximately 0.35–0.85 and vertical values approximately 0.20–0.49; these are approximate displayed ranges, not stated theoretical bounds. Orange circles denote context-chained injection and green diamonds task-aligned injection. No fitted line, uncertainty interval, significance marker, or success/failure encoding is shown.

[B] Orange points generally have greater vertical similarity, while retaining overlap with green points horizontally. Some orange points have relatively low user-task similarity, so the plot should not be simplified into a claim that chaining raises both similarities for every task. [A] The caption calls this an optimal balance and attributes improved success to it. [D] The visual alone establishes group placement, not optimization or causal mediation. It is based on the first 20% of the privacy dataset; representativeness and embedding-model details are not reported. Non-contextual injections are discussed in the caption/prose but do not appear as a plotted legend category.

### Figure 5 — Attack vectors under prompt defenses

[B] Page 8's upper chart is a grouped bar plot. The horizontal axis is Defense Type: Undefended, Secure, Secure+Sandwich. The vertical axis is Attack Success Rate, linear 0–1. Blue denotes weak prompt injection, orange strong prompt injection, and green context injection. The legend includes partial and full versions of each; full-success bars are visibly hatched and partial-success bars are plain. No numeric labels or error bars are visible.

[A] The caption defines weak injection as one retrieval, strong injection as every retrieval, and CI as one plan injection. Partial success means attacker tool access; full success means complete private-data exfiltration. [B] Blue and orange bars decline greatly with stronger defense configurations, while green remains substantially higher. Exact unlabeled heights are not asserted as author-reported values. The undefended blue bars visibly remain below 0.8, which conflicts with the broad prose claim noted above.

The figure supports the narrower conclusion that these prompt defenses leave appreciable context-attack vulnerability. Its caption names WebVoyager; the main text calls the privacy suite WebVoyager-Privacy, derived from WebVoyager. This naming compression is noted rather than treated as proof of a different dataset. Although the prose discusses both agents, the chart does not visibly separate them.

### Figure 6 — Sophistication and architecture

[B] Page 8's lower chart compares Agent-E and Browser-Use on the horizontal Agent axis. The vertical axis is linear ASR from 0 to 1. Blue, orange, and green denote no-context, task-aligned, and context-chained injection. Each has partial/full forms, with hatching distinguishing full success. There are no error bars, exact labels, or statistical markers.

[B] Green exceeds orange in both systems; Browser-use has taller displayed attack bars than Agent-E for comparable strategies. Agent-E's no-context result is at or near zero; the paper explicitly states zero for non-contextual privacy in the earlier benchmark, but does not provide a separate precise WebVoyager prose percentage for that bar. [A] The nearby text reports Agent-E task-aligned 20.6%, chained 46%; Browser-use no-context 19%, task-aligned 31%, chained 63%.

The text percentages need not be read as exact values for both plain and hatched bars: the figure distinguishes two success outcomes, and the prose does not consistently specify which outcome each headline percentage denotes. The strongest supported comparison is the ordering and the reported condition-specific values with this qualification preserved.

## 11. Table-by-table interpretation

No substantive numbered or unnumbered source tables are supplied. Consequently, there are no original table rows, columns, footnotes, missing-value codes, or statistical table results to audit. Tables in this analysis are analyst-organized representations of supplied content, not tables authored by the paper.

Results that might ordinarily appear in tables are instead located in prose and Figures 3–6. The key-number table in section 20 preserves that distinction by marking author-reported values separately from directly readable plot labels and derived arithmetic. No table is inferred from extracted text merely because the text contains aligned numbers.

## 12. Diagram / architecture interpretation

[A/B] The architecture is an iterative decision-and-action loop. The user supplies a goal. Perception supplies external data from webpages or APIs. Memory/context retains the goal, history, and other information. A decision component chooses an action. The action component changes the external environment or obtains more data. The next context includes new observations and newly appended interaction history. Page 3 formalizes that loop; Figure 2 visualizes components and attack points.

[A] In Agent-E, the Planner Agent maps to the Decision Engine, the Browser Navigation Agent to the Action Module, and context storage to the Memory System. The planner decomposes a task, receives execution feedback, checks progress, revises the plan if necessary, and issues the next subtask. This creates a separation between high-level intentions and low-level browser operations. In Browser-use, the controller directly references current and previous execution context to choose a next step. Page 2.

[D] Figure 1 illustrates the failure mode of a corrupted control representation: the executor can follow a subtask that appears internally legitimate because the malicious content has entered the plan. The same final user-facing recipe answer does not reveal every intermediate browser action. This is an interpretation of the supplied trace, not a measured detection rate or proof that users never notice attacks.

The paper does not document exact message schemas, component permissions, state serialization, plan-validation code, browser sandbox boundaries, or storage-integrity enforcement. Therefore, its conceptual diagram cannot be used to reconstruct a deployable secure architecture or reproduce the precise injection interface.

## 13. Equations and mathematical concepts

### Agent context and action loop — page 3, §3.1

[A] The unnumbered context identity is **c_t = (p_t, d_t, k, h_t)**. It is a tuple describing what the agent uses at timestep t. The components are user prompts p_t; external data d_t, such as webpage content/API responses; static knowledge k; and interaction history h_t. The tuple is a conceptual representation, not an explicit vector encoding with specified dimensions.

[A] The decision mapping is **M: C → Δ(A)**. It maps contexts in C to a probability distribution over possible actions/action sequences in A. The paper then selects **a_t = arg max_{a∈A} P(a | c_t)**: choose an action with maximum conditional probability given the current context. The notation P here denotes probability; later P_i denotes a plan. Those meanings must be separated by their arguments and subscripts.

[A] The update is **c_{t+1} = F(c_t, a_t)**. F represents the combined context/environment update after the selected action. New conversation can be appended to history and new observations can enter external data. The supplied work does not specify F as executable pseudocode, address tied maxima, or prove that every actual system uses deterministic maximum-probability selection.

### E1 — Equation (1): bounded context injection

[A] **c_t* = c_t ⊕ δ, with ||δ|| ≤ β.** This defines corrupted context by injecting perturbation δ. The operator ⊕ means injection into selected components; it is not stated to be numeric addition or exclusive OR. β is a bound on manipulation size. The paper says δ belongs to Δ, but does not fully define that perturbation set, the norm, the measurement units, or an experimental β. Δ(A) earlier denotes action distributions; the separate Δ notation should not be silently assigned the same meaning.

The equation provides a general attack model. It does not give an optimization algorithm or tested numerical constraint. Its input is original context and an allowed perturbation; its output is corrupted context. The main assumption is that some context component can be modified within the stated bound.

### E2 — Equation (2): direct prompt injection

[A] **c* = (p_t ⊕ δ_p, d_t, k, h_t).** Only the prompt component is injected. δ_p denotes malicious prompt material. The other displayed components are unchanged. This establishes a taxonomy location, not the primary experimental attacker permission in §4.1, which excludes modifying the original user instruction.

### E3 — Equation (3): indirect prompt injection

[A] **c* = (p_t, d_t ⊕ δ_d, k, h_t).** The injected component is external data. In web-agent terms, a malicious webpage can be retrieved and processed as content. Weak/strong prompt baselines differ in whether this occurs once or at every retrieval. The equation itself does not specify frequency, payload size, or the retrieved-data processing pipeline.

### E4 — Equation (4): memory injection

[A] **c* = (p_t, d_t, k, h_t ⊕ δ_h).** The corrupted component is stored interaction history. Prompts, external data, and static knowledge remain as displayed. The important distinction is that an attacker changes information represented as prior context, rather than placing an instruction only in a newly retrieved page.

### E5 — Equation (5): indirect memory contamination

[A] **c* = (p_t, d_t, k, h_{t−1} ⊕ c*_{t−1}).** The authors represent earlier corrupted context being incorporated into history used later. This describes persistence of prior manipulation. The injection operator and storage process are not formally specified, so the expression should be read as a conceptual contamination relation rather than a dimensionally defined vector operation. The equation does not establish that Agent-E carries poisoned state across independent sessions; the following text explicitly distinguishes its session model.

### E6 — Equation (6): plan injection

[A] For session i and timestep t, the expanded context is **c_{i,t} = (p_i, d_{i,t}, k, h_{i,t}, P_i)**, where p_i is the user's task and P_i the generated plan. The attack is **c* = (p_i, d_{i,t}, k, h_{i,t}, P_i ⊕ δ_P)**. Only the displayed plan component is modified. δ_P is inserted plan content. It is the equation most directly tied to the conceptual contribution and Agent-E attack evaluation.

[D] Across-session history and within-session plan persistence are different concepts. Page 2 calls the planner representation ephemeral while a contribution bullet calls the task plan persistent; page 4 explains independent sessions. A reasonable reading is that the plan persists during execution but not across executions. Because the paper does not explicitly resolve the wording, this is marked interpretation rather than a silently repaired definition.

No equation reports ASR computation as a numbered formula, an attack loss, a semantic-similarity objective, a learned defense, or a theorem. The formalization organizes attack surfaces; the empirical findings come from execution experiments rather than mathematical proof.

## 14. Interpretation and discussion

[A] The authors interpret the findings as showing that secure memory handling must be part of agent design. An agent may reject malicious instructions in a webpage yet follow similar instructions when they appear as plausible internal plan steps. The reported task-category difference supports their view that factual constraints can help expose a conflicting instruction, whereas subjective answers and recommendations provide more room for steering. Pages 7–8.

[D] The connection to the user question has three layers. First, multi-step agents need application-managed state, creating a place where information can be altered. Second, planners and controllers reuse that state when deciding subsequent actions, allowing corruption to influence a sequence rather than only one response. Third, browser/tool execution can turn an accepted instruction into data transmission. These mechanisms follow from the paper's model and attack trace. They do not quantify how much more vulnerable agents are than standalone LLMs.

[A/D] The findings descriptively support O1–O5 and the stated hierarchical-validation hypothesis: plan corruption succeeds, task categories differ, context chaining performs better, tested prompt defenses leave context vulnerability, and Agent-E is more resistant in the reported architecture comparison. However, experimental design does not isolate architecture as the only cause, and Figure 4 does not itself prove a causal explanation based on embedding similarity.

Several unresolved consistency points matter. The abstract's 17.7% wording corresponds to a 17.7-percentage-point difference between privacy rates. The undefended >80% blanket statement is not borne out by every visible Figure 5 bar. The claimed up-to-threefold improvement is not mapped to one precisely documented ratio. Page 8 uses direct-prompt language when discussing defenses evaluated mainly against retrieved-content prompt attacks; that sentence does not establish a separate direct-user-prompt experiment. These distinctions keep the explanation from becoming stronger than the source evidence.

## 15. Contributions and novelty

**Conceptual contribution [A].** The paper identifies plan injection as context manipulation of the agent's internal task representation, including a plan used only within a single execution. It extends the authors' memory-security framing beyond cross-session conversation histories. Pages 2–4.

**Methodological contribution [A].** It distinguishes non-contextual, task-aligned, and context-chained attack construction, explaining the latter as a bridge from legitimate goal through intermediate objective to unauthorized action. Page 5.

**Benchmark contribution [A].** It constructs a four-category Plan Injection Benchmark and a 45-scenario WebVoyager-Privacy suite. A link to benchmarks is mentioned, but the actual benchmark artifacts were not inspected. Page 6.

**Empirical contribution [A].** It reports differences by task type, demonstrates residual vulnerability under SECURE/SANDWICH defenses, and compares two agent architectures. Pages 7–8.

**Formal contribution [A].** Equations organize prompt, external-data, memory, and plan attacks within a common context representation. This is a modeling contribution, not a theorem or quantitative security guarantee.

The paper does not present a trained defense system, a new browser implementation, an attack-generation optimization algorithm with complete pseudocode, or a controlled proof that hierarchy alone causes improved security. Novelty claims are the authors' positioning within their cited literature; no external novelty verification was performed.

## 16. Limitations

### Authors' stated limitations

[A] Page 5 explicitly says the implemented prompt defenses cannot guarantee complete protection. Page 8 says initial experiments suggest stronger reasoning models may reduce success, but comprehensive evaluation remains future work. The conclusion lists potential defenses rather than demonstrating that context-integrity fine-tuning or principled memory management has been implemented and validated.

[A] The paper deliberately restricts attacker capabilities to evaluate a lower-bound-style vulnerability scenario. That is a stated scope choice rather than an admission that the attack is unrealistic. The text also states that Agent-E sessions are independent, making manipulation of previous execution history infeasible in that particular setting; the plan attack targets within-session context instead.

There is no dedicated limitations section or comprehensive author-authored threats-to-validity inventory. Missing experimental details below are analyst observations, not author admissions.

### Additional evidence-based analyst observations

[D] The study covers two systems using one reported controller/planner model family and a smaller browser model. It does not include a standalone-LLM baseline, a large agent population, or a controlled architectural ablation. The Plan Injection Benchmark is small in distinct examples, although examples are repeated. The privacy suite has 45 scenarios, with repetitions unspecified.

[D] Exact prompts, dynamic attack-generator settings, model versions, task selections, denominators by success condition, grading implementation, and storage-injection interfaces are unavailable in the supplied material. These gaps limit independent reproduction. Unknown details must not be assumed to have been absent from the authors' actual workflow; they are simply not disclosed here.

[D] No confidence intervals, variance estimates, formal statistical tests, failed-run accounting, or evaluator agreement are supplied. Repetition alone does not reveal statistical uncertainty. The similarity figure uses only an initial dataset subset and lacks success labels, so its causal explanation remains limited. The paper also does not measure benign task completion under defenses or quantify the tradeoff between refusing malicious actions and completing authorized tasks.

## 17. Threats to validity

These labels are analyst-organized observations [D], not categories explicitly used by the authors.

**Internal validity.** Comparing Agent-E with Browser-use changes full systems, not just the presence of a planning layer. Tool interfaces, prompting, execution policies, and context handling may also differ. The evidence supports a system-level difference; isolating hierarchy would require additional controls not supplied.

**Construct validity.** ASR operationalizes several different attacker goals, from expressing a view to transmitting private data. Partial attacker tool access differs from completed exfiltration. Without a complete evaluation implementation, it is unclear how ambiguous output, incomplete data transmission, or mistaken fields were scored. These questions affect what a reported success percentage means.

**Statistical conclusion validity.** Five repetitions are reported for the first benchmark, but uncertainty and dependence across repeated examples are not quantified. The paper's words significantly and optimal are stronger than the specific statistical evidence supplied. They should not be read as a reported hypothesis-test result or solved optimization problem.

**External and ecological validity.** Constructed queries, semi-automatic generation, controlled context writes, and adaptively generated payloads represent important attack conditions, but do not establish real-world prevalence. The chance of obtaining storage write access, encountering authentic private data, or succeeding across different websites and model releases is not measured. Dynamic websites may also change results over time, but no temporal robustness study is supplied.

**Reproducibility.** Benchmark links are referenced without accessible payloads here, and implementation/model settings are incomplete. The available document supports understanding and evaluating the reported argument, not a fully specified reproduction protocol.

**Generalizability to the user question.** The work demonstrates an additional agent attack surface. It does not measure the same attacks under matched standalone-model and agent conditions, so a quantitative claim of greater vulnerability relative to standalone LLMs remains unsupported by this paper alone.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

[A] Comprehensively evaluate stronger reasoning models, following initial indications of reduced attack success. Develop more robust models able to detect semantic inconsistencies and malicious manipulations, potentially through specialized fine-tuning for context integrity. Build principled memory-management systems with strict isolation and integrity guarantees. These proposals appear on page 8; their effectiveness is not established by the reported experiments.

### B. Additional open questions logically remaining

[D] Would a matched standalone-LLM condition resist the same malicious content more often, and how would success be defined when no browser actions are available? How much of Agent-E's reported advantage comes from hierarchy rather than other implementation differences? Which plan-validation rules reject unauthorized but task-related steps without obstructing useful task decomposition?

[D] How do full-exfiltration rates differ from attacker tool-access rates under each configuration? How robust are the results across more tasks, model snapshots, repeated privacy-suite runs, and independent attack generation? Can memory integrity prevent injection while maintaining usability, and what overhead would it impose? The supplied study leaves these questions unresolved; they are not additional author-reported experiments.

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this paper |
|---|---|
| AI agent | A system that uses model decisions and tools to pursue a task over multiple steps |
| LLM | Large language model; supplied context carries task state between model interactions |
| Web navigation agent | Agent that reads websites and performs browser actions |
| DOM | Document Object Model; the page structure targeted by browser interaction primitives |
| Context | The information supplied to the decision engine, including goal, observations, knowledge, history, and possibly plan |
| Planner–executor hierarchy | A component plans subtasks while another executes browser operations |
| DPI | Direct prompt injection: malicious content in prompt input |
| IPI | Indirect prompt injection: malicious instructions embedded in external retrieved data |
| MI | Memory injection: alteration or contamination of stored interaction history |
| Plan injection | Alteration of the high-level plan used to direct execution |
| PI-Weak | Prompt attack inserted into one retrieval |
| PI-Strong | Prompt attack inserted at every retrieval step |
| CI | Context/plan injection in the privacy comparison; caption describes one plan insertion |
| Non-contextual injection | Malicious step with no plausible connection to the user's task |
| Task-aligned injection | Attack content framed as relevant to the task domain |
| Context-chained injection | Intermediate steps connect the legitimate task to the malicious goal |
| Foot-in-the-door | The paper's name for first establishing relevance before introducing the malicious objective |
| ASR | Attack success rate: fraction/percentage of attempts completing the defined attacker outcome |
| Partial success | In Figure 5, attacker tool access |
| Full success | In Figure 5, completed private-data exfiltration |
| SECURE | System-prompt safety guidelines against misuse |
| SANDWICH | Retrieved-content delimiters and instructions to treat enclosed material as data |
| Exfiltration | Sending private information to an unauthorized destination |
| Cosine similarity | The embedding comparison used in Figure 4; model and detailed procedure are unspecified |
| t, i | Timestep and session index |
| c_t, c* | Original context and corrupted context |
| p_t or p_i | User prompt or session task |
| d_t | External observations/data |
| k | Static knowledge, with system prompts/code included in the threat-model discussion |
| h_t | Stored interaction history |
| P_i | Generated session plan; distinct from probability P(a given c) |
| M, C, A | Decision engine, context space, and action/action-sequence space |
| Δ(A) | Probability distributions over actions in the formal decision mapping |
| F | Context/environment update after an action |
| δ | Injected perturbation; subscripts indicate the attacked component |
| ⊕ | Context injection operator, not fully specified as an algebraic operation |
| β, ||δ|| | Manipulation-size bound and its norm; no concrete norm, unit, or tested bound is supplied |
| T_v, T_a | Victim's legitimate task and attacker's unauthorized task |

## 20. Key numerical results

The table separates prose percentages from rounded plot labels. Percentages belong to their stated dataset and condition; similarly named privacy conditions across benchmarks are not interchangeable.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible main-document pages | 10 | pages | Supplied extracted text | Supplied input metadata | Pages 1–10 |
| Visually inspected pages | 8 | pages | 1–5, 7–8, 10 | Directly observable | Supplied images |
| Plan benchmark categories | 4 | categories | Factual, opinion, advertisement, privacy | Author-reported | p. 6, §5.1 |
| Samples per category | 15 | samples | Plan Injection Benchmark | Author-reported | p. 6, §5.1 |
| Executions per sample | 5 | executions | Plan Injection Benchmark | Author-reported | p. 6, §5.1 |
| Distinct plan-benchmark samples | 60 | samples | 4 × 15 | Analyst-derived | p. 6 operands |
| Executions per category/condition | 75 | executions | 15 × 5, if fully executed | Analyst-derived | p. 6 operands |
| Privacy-suite domains | 9 | domains | WebVoyager-derived suite | Author-reported | p. 6, §5.2 |
| Tasks per privacy domain | 5 | tasks | WebVoyager-derived suite | Author-reported | p. 6, §5.2 |
| Privacy scenarios | 45 | scenarios | 9 domains × 5 tasks | Author-reported | p. 6, §5.2 |
| Opinion task-aligned ASR | 94.7 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Opinion direct-insertion ASR | 70.7 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Factual task-aligned ASR | 18.7 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Factual direct-insertion ASR | 0 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Advertisement task-aligned ASR | 78.7 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Advertisement non-contextual ASR label | 0.36 | proportion | Rounded bar label | Visually readable | p. 7, Fig. 3 |
| Privacy non-contextual ASR | 0 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Privacy task-aligned ASR | 35.6 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Privacy chained ASR | 53.3 | % | Agent-E, Plan Injection Benchmark | Author-reported | p. 7, §6.1 |
| Privacy chaining absolute increase | 17.7 | percentage points | 53.3 − 35.6 | Analyst-derived | p. 7 operands |
| Privacy chaining relative increase | ≈49.7 | % | (53.3 − 35.6) / 35.6 × 100 | Analyst-derived | p. 7 operands |
| Similarity-analysis subset | 20 | % of tasks | First portion of WebVoyager-Privacy | Author-reported | p. 7, Fig. 4 caption |
| Agent-E task-aligned privacy ASR | 20.6 | % | WebVoyager-Privacy comparison | Author-reported | p. 8, §6.2 |
| Agent-E chained privacy ASR | 46 | % | WebVoyager-Privacy comparison | Author-reported | p. 8, §6.2 |
| Browser-use non-contextual privacy ASR | 19 | % | WebVoyager-Privacy comparison | Author-reported | p. 8, §6.2 |
| Browser-use task-aligned privacy ASR | 31 | % | WebVoyager-Privacy comparison | Author-reported | p. 8, §6.2 |
| Browser-use chained privacy ASR | 63 | % | WebVoyager-Privacy comparison; also stated as up to 63% | Author-reported | p. 8, §6.2 |
| Chained cross-agent difference | 17 | percentage points | 63 − 46 | Analyst-derived | p. 8 operands |
| Agent-E chaining versus alignment | 25.4 | percentage points | 46 − 20.6 | Analyst-derived | p. 8 operands |
| Undefended ASR headline | >80 | % | Prose claims both agents and prompt/plan attacks; visually qualified | Author-reported | p. 7, §6.2 |
| Undefended weak-PI bars | Around 0.6 | proportion | Figure 5, partial/full bars; exact values unlabeled | Approximate visual estimate | p. 8, Fig. 5 |
| Headline relative effectiveness | Up to 3× | ratio | Comparison wording differs across abstract/contributions | Author-reported | pp. 1–2 |

The 53.3% Plan Injection Benchmark privacy result and the 46% WebVoyager-Privacy Agent-E result are different experiment conditions, not contradictory estimates of one identical quantity. Likewise, 35.6% and 20.6% task-aligned values belong to different benchmark descriptions. Exact values for every partial/full bar cannot be recovered confidently from the images.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Internal plans are an attackable context component | Expanded context and direct plan modification | E6; F1–F2 | p. 4, Eq. (6); p. 2 | HIGH for author formalization; implementation interface unspecified |
| Restricted context corruption can redirect agent behavior | Threat model plus attack outcomes | X2–X4 | pp. 4–8 | HIGH for reported scope/results; obtaining write access is not measured |
| Task nature affects susceptibility | Opinion 94.7% versus factual 18.7% under alignment | X2; F3 | p. 7 | HIGH transcription; generalization beyond constructed tasks is limited |
| Alignment helps compared with unrelated insertion | All Figure 3 category comparisons | X2; F3 | p. 7 | HIGH for displayed direction; no statistical test supplied |
| Chaining improves Agent-E privacy attacks | 53.3% versus 35.6% | X2; F3 | p. 7 | HIGH for reported percentages; +17.7 points is derived |
| Prompt defenses leave context vulnerability | PI bars fall while CI bars remain substantial | X4; F5 | pp. 7–8 | HIGH qualitative visual support; not all possible defenses tested |
| Agent-E is more resistant than Browser-use in reported privacy conditions | 46% versus 63% chained ASR | X4; F6 | p. 8 | HIGH for report; architecture is not isolated causally |
| Semantic construction changes embedding placement | Orange/green scatter distributions | X3; F4 | p. 7 | MEDIUM explanatory strength; no causal test or success labels |
| Every undefended agent/vector exceeds 80% | Broad prose statement | X4; F5 | pp. 7–8 | Qualified: weak-PI figure bars are below 0.8 |
| Stronger reasoning models might help | Preliminary observation and future-work statement | Unreported preliminary analysis | p. 8 | LOW empirical specificity; no detailed results supplied |
| Agent state adds a relevant vulnerability mechanism | Context-management discussion and successful corruption | S1; SS4.3; X2–X4 | pp. 1, 5, 7–8 | MEDIUM analyst inference; no standalone-model comparison |

The map deliberately separates evidence for a reported result from evidence for the proposed explanation. For example, an architecture difference can be measured descriptively while the cause remains only partly established. Each machine-readable claim below has a short exact supporting quotation and a physical PAGE_RANGE locator.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to find a recipe. To finish the job, it keeps a to-do list and notes about the websites it has visited. If someone can secretly edit that list, they might add steps such as finding your address and entering it on their website. The assistant could still give you the recipe afterward, even though it also did something you never requested.

The paper tests attacks like that against two web assistants. An obvious unrelated instruction is easier for the more structured assistant to reject. A deceptive sequence that starts with something relevant to the recipe and gradually moves toward sharing personal data works more often. The important distinction is that a step can sound related to your task without being authorized by you.

The researchers also add warnings that help the assistants ignore malicious instructions found on webpages. Those warnings help with webpage attacks, but they do less to protect an already-corrupted plan. In one privacy comparison, the paper reports context-chained attack success of 46% for Agent-E and up to 63% for Browser-use. These are results for the tested setup, not predictions for every assistant.

This helps explain why a web agent can have extra security problems: it keeps changing notes and can use a browser to act on them. But this paper does not run the same experiment against a standalone language model, so it cannot tell us exactly how much more vulnerable the web agents are. Its strongest message is that protecting what an agent remembers and plans is necessary alongside protecting what it reads.

## Completeness Audit

The inventory is the denominator for this audit. All supplied main-text sections were inspected; all numbered figures were visually inspected; page 6 and page 9 remain text-only. Fully represented means the substantive role and available evidence are explained, not that every sentence or plot coordinate has been reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract | Yes, text and image | Yes | Represented in compressed form | Headline attack, threefold claim, and ambiguous 17.7% wording preserved |
| S1 Introduction | Yes, text and images | Yes | Represented in compressed form | State-management rationale and hierarchical-plan gap retained |
| S2 Background/related work | Yes, text and images | Yes | Represented in compressed form | Prior-work categories retained without independent citation review |
| SS2.1 Web navigation agents | Yes | Yes | Fully represented | Browser-use and Agent-E workflows explained |
| SS2.A Attacks on language agents | Yes | Yes | Represented in compressed form | Direct/indirect taxonomy and source boundary retained |
| SS2.B Attacks on agent memory | Yes | Yes | Represented in compressed form | Knowledge, trajectory, and conversation poisoning retained |
| S3 Context Manipulation Attacks | Yes | Yes | Fully represented | Model and attack locations covered |
| SS3.1 Agent framework | Yes | Yes | Fully represented | Components, action mapping, and update identities explained |
| SS3.2 Context manipulation | Yes | Yes | Fully represented | Six equations and notation uncertainty covered |
| S4 Web-agent attacks | Yes | Yes | Fully represented | Controlled context corruption and objectives covered |
| SS4.1 Threat model | Yes | Yes | Fully represented | Allowed/excluded capabilities and history/plan ambiguity retained |
| SS4.2 Prompt attacks/defenses | Yes | Yes | Fully represented | Preliminary attack, SECURE, SANDWICH, and limits covered |
| SS4.3 Context attacks | Yes | Yes | Fully represented | Three sophistication levels and mechanisms explained |
| S5 Evaluation | Yes, text only on p. 6 | Yes | Fully represented | Benchmarks and metrics extracted without visual-page claim |
| SS5.1 Plan benchmark | Yes, text only | Yes | Fully represented | Categories, 15 samples, five runs, generation, success criteria |
| SS5.2 Privacy benchmark | Yes, text only | Yes | Fully represented | Nine domains, 45 tasks, adaptive attack generation |
| SS5.3 Metrics | Yes, text only | Yes | Fully represented | Category outcomes and partial/full qualification |
| S6 Results | Yes | Yes | Fully represented | Results separated by benchmark and condition |
| SS6.1 Plan results | Yes, text and image | Yes | Fully represented | Exact prose percentages and rounded plot labels distinguished |
| SS6.2 Privacy results | Yes, text and images | Yes | Fully represented | Defense/architecture comparisons and discrepancies retained |
| S7 Conclusion | Yes, text and image | Yes | Fully represented | Claims and proposed defenses covered with limits |
| REF References | Yes; p. 9 text only, p. 10 text/image | Yes | Represented in compressed form | Bibliographic role and relevant cited categories accounted for |
| Explicit research questions | No formal list exists | Yes | Not present as formal objects | O1–O5 labeled as organized objective restatements |
| H1 Hierarchical-validation hypothesis | Yes | Yes | Fully represented | Page 8 statement and descriptive support covered |
| X1 Preliminary prompt checks | Yes | Yes | Fully represented within available detail | Missing denominators and rates disclosed |
| X2 Plan benchmark | Yes | Yes | Fully represented | Main outcomes and design retained |
| X3 Similarity analysis | Yes | Yes | Fully represented | Subset, axes, groups, and causal limits retained |
| X4 Privacy comparisons | Yes | Yes | Fully represented | Defense and architecture conditions separated |
| F1 Attack trace | Yes, visually | Yes | Fully represented | Sequence and data-flow purpose; tiny masked fields compressed |
| F2 Architecture/attack diagram | Yes, visually | Yes | Fully represented | Components, arrow categories, attack locations |
| F3 Category bar chart | Yes, visually | Yes | Fully represented | All displayed category/strategy combinations covered |
| F4 Similarity scatter | Yes, visually | Yes | Fully represented | Axes, encodings, trends; individual coordinates not transcribed |
| F5 Defense chart | Yes, visually | Yes | Represented with uncertainty | Exact unlabeled heights and agent allocation unresolved |
| F6 Architecture chart | Yes, visually | Yes | Represented with uncertainty | Partial/full precise values not fully recoverable |
| E1 Bounded manipulation | Yes | Yes | Fully represented | Norm/set/bound unspecified |
| E2 Direct prompt injection | Yes | Yes | Fully represented | Taxonomy versus restricted threat model distinguished |
| E3 Indirect prompt injection | Yes | Yes | Fully represented | External-data attack location explained |
| E4 Memory injection | Yes | Yes | Fully represented | History modification explained |
| E5 Indirect memory injection | Yes | Yes | Fully represented with notation caveat | Conceptual contamination, not invented storage algebra |
| E6 Plan injection | Yes | Yes | Fully represented | Session-specific context and modified plan explained |
| Unnumbered context/action/update identities | Yes | Yes | Fully represented | Tuple, decision mapping, argmax, update |
| Tables | None supplied | Accounted for | Not present | Analysis tables are not source tables |
| Algorithms/pseudocode | None supplied | Accounted for | Not present | Narrative procedure is available, executable algorithm is not |
| Theorems/proofs | None supplied | Accounted for | Not present | Formalization does not establish a security proof |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, benchmark, formal, empirical |
| Author-stated defense limitations | Yes | Yes | Fully represented | No complete protection; stronger-model evaluation pending |
| Author future-work proposals | Yes | Yes | Fully represented | Model robustness and memory integrity |
| Page 1 affiliation/equal-contribution/venue footnote | Yes | Yes | Represented in compressed form | Relevant publication metadata retained; contact details omitted |
| Page 6 benchmark footnote | Yes, text only | Yes | Represented; linked artifact inaccessible | Link destination and benchmark files not supplied |
| Appendices | None supplied/detected | Accounted for | Not present in supplied document | No appendix inspection claimed |
| Supplementary files | None supplied | Accounted for | Missing from supplied material if linked artifacts are counted | No supplied external benchmark artifact reviewed |
| Headers/page numbers | Yes on supplied images/text | Accounted for | Inspected but omitted as repetitive/non-substantive | Used for physical-page traceability |

### Missing or inaccessible material

The externally linked benchmark files and their link destination are unavailable. Exact attack prompts, detailed run logs, evaluation code, storage-injection interfaces, model snapshots, and hyperparameters are not provided in the supplied text. Page images for pages 6 and 9 are absent, although their text is supplied. No appendix or supplement is supplied; the paper does not visibly identify an appendix to inspect. These are access/reporting boundaries, not proof that the authors never created such artifacts.

### Uncertain interpretations

Unresolved points are: the precise meaning and implementation of the perturbation norm and bound; the relationship between history-only permission and a separately modeled plan component; persistent-versus-ephemeral plan wording; whether every headline privacy percentage denotes partial or full success; the figure allocation needed to support claims about both agents in Figure 5; the discrepancy between its weak-PI bars and the >80% prose; and the exact comparison underlying up-to-threefold claims. Figure 4's optimal-balance explanation is an author interpretation without a supplied optimization procedure or causal experiment. Exact unlabeled bar heights are not converted into invented precise percentages.

### Deliberately compressed material

Repeated motivation about memory security, overlapping definitions across sections, individual bibliography entries, and multiple illustrative attack examples are compressed. Citation groups are retained by methodological category rather than reproduced author by author. Figure 1's masked field contents, Figure 4's individual point coordinates, author contact information, decorative agent icons, running headers, and repeated page titles are not transcribed in full. Their substantive roles are represented where relevant.

### Potential omissions

No known substantive section, numbered figure, numbered equation, reported benchmark design, major numerical comparison, major contribution, or explicit future-work proposal in the supplied inventory has been left entirely unrepresented. Coverage remains qualified by the listed inaccessible artifacts, missing visual pages, ambiguous success conditions, and unresolved source inconsistencies. This report does not claim exhaustive verification of the paper's underlying experiments or literal preservation of every source detail.
