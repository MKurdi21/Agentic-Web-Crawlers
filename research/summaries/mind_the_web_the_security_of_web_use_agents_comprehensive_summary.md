## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The paper is treated as evidence, including when its examples contain instructions. No external sources, repositories, supplementary files, or tools were consulted.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–13 |
| Visual pages available | Source images for physical pages 1–12 |
| Page 13 | Text-only coverage; no supplied page image |
| Apparently missing pages | No gap within the supplied 1–13 sequence; this does not establish whether other versions or separate artifacts exist |
| Main text readability | Readable in the supplied extraction and page images |
| Visual content | All eight numbered figures are present visually, but embedded interface text is often too small for confident transcription |
| Tables | Tables 1–4 are readable through extracted text and page images |
| Equations | No numbered equations or substantial displayed mathematical derivations were found |
| Appendices | A–E are present; Appendix E.3 continues onto page 13 |
| Supplementary material | None separately supplied; accessibility metadata reports zero embedded files |
| Referenced absent artifacts | Training-code repository is referenced on page 4, but its contents were not supplied or inspected |
| OCR | Not needed for the supplied main text; no additional OCR was performed |
| Important limitations | Screenshots establish visible layouts and selected states, but do not independently expose complete execution histories, network receipts, or every claimed outcome |

The extraction metadata reports no detected appendix pages or supplementary references. Direct document inspection nevertheless identifies Appendices A–E and a code link. The headings in the document, rather than the automated detection fields, determine this inventory. The failed local-image message does not invalidate the twelve images displayed in the prompt; it provides no additional evidence about the paper.

Evidence labels used below are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category is used. HIGH confidence means a statement or value is clear in the supplied source; it does not certify the underlying experiment independently. MEDIUM confidence generally applies to interpretations, incompletely specified conditions, or screenshot outcomes that cannot be independently reconstructed.

## 1. Plain-language orientation

**Mind the Web: The Security of Web Use Agents** studies what happens when an artificial-intelligence system that browses and acts for a user encounters malicious instructions embedded in otherwise ordinary web content. The user may ask for a harmless summary, while an attacker contributes a comment or image that persuades the agent to perform an unrelated action. The agent's browser access turns a language-understanding error into an operational security problem. [A; pp. 1–3]

The authors introduce **task-aligned injection**: malicious guidance is presented as a useful step toward completing the user's request. Instead of openly demanding that the agent abandon its task, the content can claim that another destination contains updated information or that an additional step is necessary for a better summary. The agent may incorporate this guidance into its plan and act with permissions it already possesses. [A; p. 3, §5.1]

The researchers build an automated attack-generator training pipeline, evaluate several training configurations, test transfer to additional payloads and underlying models, and show manually tested examples across five agent implementations overall. Their strongest reported configuration reaches **82% attack success rate**, compared with **12%** for contextual injections without task-aligned phrasing and **54%** for a task-aligned base generator without fine-tuning. [A; p. 5, Table 1]

For the reader's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper offers a mechanism-based answer: agents repeatedly consume third-party content and can use browser sessions, navigation, forms, and sometimes local resources to act on it. **This relevance is analyst inference [D]. The paper does not provide a matched quantitative comparison of standalone LLMs against web agents.** Its experiments compare attack-generation methods and agent/model conditions, not two deployment classes under an otherwise identical protocol.

## 2. Document roadmap

The document is an empirical cybersecurity and AI-systems paper. Its primary contribution is an attack methodology with an automated training procedure and supporting evaluation, rather than a formal theorem, systematic review, or benchmark release.

| Original section | Physical pages | Role in the argument |
|---|---|---|
| Abstract and keywords | 1 | Summarize the threat, generator, broad results, and proposed defenses |
| §1 Introduction | 1–2 | Motivate indirect attacks and list five contributions |
| §2 Web-Use Agents | 2 | Explain the repeated perception, reasoning, and action cycle |
| §3 Related Work; §§3.1–3.2 | 2–3 | Position the work against LLM jailbreaks, capability benchmarks, and security assessments |
| §4 Threat Model | 3 | Define a remote content-controlling attacker and agent assumptions |
| §5 Attack Methodology and Payload Taxonomy | 3–6 | Present the lifecycle, nine payloads, training pipeline, results, and demonstrations |
| §6 Mitigations Strategies; §§6.1–6.4 | 6–8 | Propose oversight, constraints, reasoning defenses, and discuss usability costs |
| §7 Discussion; §§7.1–7.3 | 8 | Explain browser-security limitations, contextual reasoning, and model transfer |
| §8 Conclusion | 8–9 | Restate the contribution and implications |
| References | 9 | List 31 cited items; their external contents are not part of this analysis |
| Appendix A; A.1–A.3 | 9–10 | Describe agent deployment types, modalities, and five implementations |
| Appendix B | 10–11 | Summarize payload preconditions and affected agent types in Table 2 |
| Appendix C | 10–12 | Expand demonstrations associated with Figures 4–8 |
| Appendix D | 10, 12 | Discuss defense implications and summarize mitigations in Table 3 |
| Appendix E; E.1–E.3 | 10–13 | Explain browser defenses, security–usability tradeoffs, and ethics |

The visual inventory consists of **Figure 1**, a training-flow diagram; **Figures 2–8**, interface screenshots illustrating attacks; **Table 1**, training-method ASRs; **Table 2**, payload taxonomy; **Table 3**, mitigation mappings; and **Table 4**, limitations of browser-security mechanisms. There is no numbered algorithm, pseudocode listing, theorem, lemma, or equation. The substantive footnotes are the equal-contribution note on page 1 and the training-repository link on page 4.

## 3. Background and context

A **large language model (LLM)** interprets language and generates responses or proposed instructions. A **web-use agent**, as defined here, wraps an LLM in a loop: gather current page content, combine it with the task context, obtain proposed actions, execute those actions, and repeat. The authors contrast this adaptive process with automation based on predetermined scripts and structured interfaces. [A; p. 2, §2]

A **prompt injection** places instructions in material that the model encounters as input. In this paper, the attacker supplies third-party content rather than the user's authorized request. The agent can mistake that content for guidance that should influence its own behavior. **Task alignment** describes the deceptive relationship to the user's goal; it does not mean the resulting action is authorized. [A; p. 3, §5.1]

The **Document Object Model (DOM)** is the page structure agents can parse to identify elements such as buttons, forms, and links. Other agents perceive screenshots, using visual analysis and potentially **optical character recognition (OCR)** to read text. Hybrid agents use both channels. The authors argue that hybrid perception broadens the attack surface by allowing malicious content to arrive through multiple channels. [A; pp. 9–10, Appendix A.2]

The **Confidentiality–Integrity–Availability (CIA) triad** organizes the consequences. Confidentiality concerns exposure of private information; integrity concerns unauthorized actions or deceptive outputs; availability concerns interruption or exhaustion of the agent's service. P3 is explicitly assigned both confidentiality and integrity in Table 2. These categories describe attack objectives, not independent guarantees that every implementation permits every objective.

A **jailbreak** is described in related work as an attempt to obtain behavior that a model's safety guidelines would normally prevent. The paper's indirect attacks also exploit the difference between trusted task instructions and untrusted environmental content. Browser safeguards discussed later primarily address code, origins, sessions, or resource access; the authors' proposed failure mechanism involves an already privileged agent interpreting language. [A; pp. 2–3, 8, 12]

## 4. Research problem and gap

**Existing problem [A].** Web-use agents process comments, forum posts, advertisements, and other page content while holding capabilities needed for user tasks. An adversary can influence this input without directly accessing the agent. The agent may convert malicious text into navigation, data access, output manipulation, or an authenticated operation. [pp. 1–3]

**Shortcomings of earlier approaches, as attributed by the authors [A].** Much LLM security research concerns direct textual jailbreaks, multimodal jailbreaks, or optimization against standalone models. Capability benchmarks assess whether agents complete tasks. Other security work examines harmful instructions issued directly by users. The authors argue that direct-access assumptions do not capture a remote attacker who only controls material encountered during benign browsing. [pp. 1–3, §3]

They also criticize attack optimizers that repeatedly call a target model, lack persistent learning across attacks, or require model-specific retraining. Their dedicated generator is intended to learn reusable strategies through one offline fine-tuning process. These are the paper's characterizations of cited work, not an independently verified judgment of the broader literature. [p. 2, §3.1]

**Gap [A].** The targeted gap is indirect manipulation through third-party web content, combined with high-privilege browser execution and contextual framing that appears to advance the task. The paper describes this setting as largely unexplored. Its references include other environmental or indirect agent-injection work, so the safest novelty statement is that the authors present their particular task-aligned technique, generator, taxonomy, and evaluation; the supplied paper does not establish that all indirect-agent attacks originated here.

**Scope.** The work focuses on autonomous browser agents, selected open-ended tasks, two controlled injection environments, additional manually tested platforms, and nine conceptual payload classes. Quantitative payload results cover seven classes; P2 and P3 are described but have no separate reported ASR. It does not estimate attack prevalence across ordinary browsing, test every browser agent, or compare the same model acting alone and inside an agent.

## 5. Research questions, objectives, and hypotheses

**Explicit research questions:** No formally numbered or interrogative research questions are stated in the supplied paper.

**Explicit hypotheses:** No formal hypothesis set or prespecified hypothesis-testing framework is supplied.

The following objectives are directly grounded in the authors' descriptions [A]:

1. Demonstrate that third-party web content can redirect agents executing benign user requests. [pp. 1–3]
2. Introduce task-aligned injection that disguises malicious actions as helpful guidance. [p. 3, §5.1]
3. Automate generation and validation of injections, then train a reusable generator without agent interactions during fine-tuning. [pp. 4–5, §5.3]
4. Evaluate training methods, targeted and unseen payloads, different agents, environments, and underlying LLMs. [pp. 5–6, 8]
5. Organize consequences through a CIA taxonomy and propose mitigation strategies with usability tradeoffs. [pp. 3–4, 7–8, Tables 2–3]

**Reader-supplied research question [D].** The question about greater vulnerability than standalone LLMs is an organizing lens for this analysis. The evidence supports a distinction between language-level susceptibility and the consequences enabled by agent permissions. It does not establish an experimentally measured vulnerability ratio or universal ranking between standalone models and agents.

## 6. Assumptions / Threat Model

The attacker is remote and cannot directly compromise the agent's code or alter the user's task. The attacker cannot execute arbitrary code or hijack browser sessions. Instead, the attacker controls portions of content that the agent may encounter: public comments or reviews, advertisements or third-party content, and user-generated posts, emails, or shared documents. [A; p. 3, §4]

The stated assumptions are:

- **ReAct-style LLM reasoning:** the agent uses an LLM to interpret browser content and generate instructions. The paper references ReAct but does not give its formal algorithm or a component-by-component implementation here.
- **Limited attacker observability:** the attacker cannot inspect the victim agent's internal queries, responses, or thought process.
- **Browser capabilities:** the agent can perform complex operations such as authenticated navigation and form submission.
- **Autonomous operation:** the user delegates execution without continuous oversight or manual intervention.

The training laboratory can nevertheless execute agents and collect logs to label candidate attacks. **Analyst interpretation [D]:** this is a development-time capability in controlled environments; it should not be silently attributed to the remote attacker against a deployed victim. The supplied work does not fully specify what feedback that attacker receives after posting an injection.

Assets include authenticated user data, credentials or account control, local files where permitted, camera and microphone access under relevant permissions, the integrity of posts and financial actions, truthful summaries, and successful completion of the user's task. The original user request is treated as the authorized objective. Third-party content is an input channel whose apparent task relevance can be mistaken for authority. [A; pp. 3–4, Table 2]

Permissions are conditional. Pre-granted camera/microphone permissions matter for P1; sessions or credentials matter for P2, P3, and P7; local file access matters for P4. P5, P6, P8, and P9 list no additional preconditions in Table 2, but still require that the agent encounter and follow injected content. Remote isolation reduces access to user-local resources; it does not by itself prevent deceptive summaries, navigation, or loops.

## 7. Methodology

### 7.1 Attack lifecycle and taxonomy

The lifecycle has four stages [A; p. 3, §5.1]: **injection**, where malicious content enters the page; **perception**, where the agent gathers it; **interpretation**, where the LLM accepts it as guidance and changes its plan; and **execution**, where the agent acts using its existing privileges. The malicious objective can be embedded in text or image content. Task-aligned framing includes helpful suggestions, system-like notices, task refinements, deprecated-content notices, testing explanations, and fabricated recommendations.

| Payload | Objective | Conditions and affected types reported in Table 2 |
|---|---|---|
| P1 | Unauthorized camera/microphone activation | Pre-granted permissions; extension-based agents |
| P2 | Sensitive personal-information extraction | Active sessions, stored credentials, or valid cookies; extension, semi-stateful isolated, and local clean-browser agents |
| P3 | Credentials hijack | Autofill or authenticated password-reset access; extension, local clean-browser, and semi-stateful remote agents; C + I impact |
| P4 | Local-file exfiltration | Local file-system access; local clean-browser and permitted extension agents |
| P5 | Task abortion | No additional listed precondition; all types; availability impact |
| P6 | Infinite-loop denial of service | No additional listed precondition; all types; availability impact |
| P7 | Unauthorized user action | Sessions, credentials, or cookies; extension, semi-stateful isolated, and authenticated local agents |
| P8 | Misleading redirection/phishing | No additional listed precondition; all types; integrity impact |
| P9 | Misleading or deceptive output | No additional listed precondition; all types; integrity impact |

P2 and P3 describe potential exploitation of private sessions, autofill, or account recovery. They are taxonomy entries rather than separately quantified results. P8's reported outcome is redirection; it should not automatically be expanded into verified theft of credentials. P4's concrete screenshot evidence is narrower than the term exfiltration used elsewhere, as explained in §10 below.

### 7.2 Automated generation and validation

Stage 1 conditions candidate generation on three inputs: **user task**, **attack objective/payload**, and **injection environment**. High-temperature sampling produces multiple formulations for each context. Stage 2 embeds a candidate, runs a web agent on the benign task, collects execution logs, and asks an independent LLM judge to score whether the malicious objective was achieved. Scores run from **0.0 to 1.0**. The preprocessing description classifies scores **≥0.5** as successful. [A; p. 4, §§5.3.1–5.3.2]

The environments are a self-hosted European-city blog with comments, **City-Explorer**, and a local Reddit instance. Candidate generation uses **Qwen3-4B-Instruct**, temperature **1.6**, and approximately **1,500** injections for **P4, P5, P6, and P8**. Tasks are randomly selected from open-ended requests such as page analysis, issue analysis, and summarization. Browser Use executes candidates with **GPT-4o** or **Gemini-2.0-Flash**, randomly selected per trial; **GPT-5** supplies judgment. Approximately **300** candidates meet the successful threshold and feed supervised fine-tuning. [A; p. 5, §5.3.4]

### 7.3 Fine-tuning

**Supervised fine-tuning (SFT)** trains the generator on successful injections, teaching linguistic and contextual patterns associated with success. **Direct preference optimization (DPO)** then trains with higher- versus lower-scoring injections sharing the same attack context. The pairs include success–failure comparisons and stronger–moderate comparisons. This allows unsuccessful candidates to contribute to learning rather than being discarded. [A; p. 4, §5.3.3]

The authors filter near-ties with score difference **<0.05**, prioritize gaps **≥0.3**, and obtain approximately **12,000** preference pairs. Training uses one **NVIDIA RTX 6000 GPU**. They do not specify GPU memory variant, learning rates, epochs, batch sizes, optimizer details, random seeds, or exact training time in the supplied work. No explicit training/validation/test split or overlap-control protocol is reported. [A and absence observation; p. 5]

Agent executions occur during the preprocessing validation stage. Fine-tuning then proceeds without further agent interaction. Consequently, 'offline' describes the learning stage after data collection; it does not mean the pipeline required no agent executions at all. The §5.3 heading says generation 'through RL', while the implemented best-performing procedure is SFT followed by DPO and is contrasted with online reinforcement learning.

### 7.4 Evaluation protocol

The comparison includes non-task-aligned base generation, task-aligned base generation, SFT, SFT+DPO, and **proximal policy optimization (PPO)** with **500 agent interactions** as an online reinforcement-learning baseline. Although the prose says five configurations, these contain two different base-generation conditions, then three training variants, matching Table 1's five rows.

Evaluation generation temperature is **0.6**. The authors call this deterministic, high-quality generation; no decoding settings are supplied to establish literal determinism. Each experiment uses **100 independent trials** in which a generated injection is embedded, the agent executes the user task, and the judge scores the logs. The evaluation ASR definition uses **judge score >0.5**, unlike preprocessing's **≥0.5**. The treatment of a score exactly equal to 0.5 is therefore inconsistent. [A; p. 5, §5.4]

There are no reported statistical tests, confidence intervals, error bars, run-to-run deviations, annotation-agreement measurements, or measured cost and latency comparisons. The code repository is linked but was not inspected. These absences constrain reproducibility and the precision of performance comparisons.

## 8. Experiments / Analyses

### X1 — Training-method comparison

**Purpose:** assess task alignment and successive training stages. **Conditions:** Table 1's five generator methods; evaluation temperature 0.6; 100 trials per experiment; success judged from agent logs. **Results:** 12% non-task-aligned; 54% task-aligned base; 61% SFT; 82% SFT+DPO; 63% PPO. The authors attribute gains to task-relevant framing and learning from both better and worse examples. Their explanation that DPO better captures subtle evasion than PPO is explicitly speculative. [A; p. 5, §5.4.1]

The table does not report separate ASRs for each of the five agent products. The exact aggregate weighting over tasks, payloads, environments, and executor models is insufficiently specified. It is therefore inappropriate to describe 82% as independently measured for every implementation.

### X2 — Performance on targeted payloads

**Purpose:** compare the SFT+DPO generator across its four training-targeted objectives. **Results:** P6 infinite loop **85%**, P5 task abortion **84%**, P8 redirection/phishing **81%**, P4 local-file exfiltration **79%**. All four exceed 75%, but their individual permission requirements differ. The authors describe these as consistent performance across the CIA triad. No detailed per-environment breakdown, uncertainty estimate, or sample-composition table accompanies the figures. [A; p. 5, §5.4.2]

### X3 — Transfer to unseen payload types

**Purpose:** test objectives outside the four candidate-training payloads. **Results:** P9 misleading content **84%**, P7 unauthorized action **79%**, and P1 camera/microphone activation **73%**. 'Unseen' refers to payload type in this description; the paper does not establish a complete held-out protocol for every other variable. The authors relate lower P1/P4 success to agents occasionally flagging sensitive operations as requiring permission. [A; pp. 5–6]

### X4 — Manual agent and environment demonstrations

**Purpose:** show transfer beyond the automated Browser Use validation setting. Agent interfaces prevented programmatic automation, so generated injections were tested manually. The demonstrations involve Do Browser, OpenOperator, OpenAI Operator, and Comet, with GitHub as an additional environment and external test-account actions. Where configurable, the authors report GPT-4o for manual testing. This does not mean every named agent uses GPT-4o; Operator's CUA model is separately discussed. [A; p. 6]

Outcomes include a Google Meet session with camera/microphone, Comet local-directory access and preparation to transmit information, an OpenOperator reload loop and reported crash, unauthorized Twitter posting, a misleading Operator summary, a GitHub comment directing task termination, and a demo-bank transfer. These establish existence examples, not comparable success-rate estimates across products. Figure 7 primarily displays the payload rather than a clear post-execution state.

### X5 — Transfer across underlying LLMs

**Purpose:** test the generator with additional Browser Use backend models. The setup names **Claude Sonnet 3.5** and **Mistral Pixtral-Large**, two payloads P5 and P8, and **100 independent trials**. Results are respectively P5/P8 **90%/94%** for Mistral and **82%/77%** for Claude. The text does not unambiguously establish whether 100 means per payload or across both payloads for each model. [A; p. 8, §7.3]

The results sentence calls the Claude model 'Claude Sonnet 3', whereas setup names 'Claude Sonnet 3.5'. Both wordings are retained as a version ambiguity. The authors observe greater susceptibility to fake system prefixes for GPT-4o, Gemini, and Mistral and resistance to that formatting for Sonnet. Their explanation involving weaker Mistral safety alignment is an attribution, not a separately controlled experiment.

### X6 — Manual safety-tuned Operator test

The authors test P7, P8, and P9 against the CUA-powered Operator. P7 and P8 succeed immediately in the reported manual tests. P9 initially prompts for permission; a manual addition asserting permission was unnecessary lets it proceed. This supports a particular adaptive bypass example. It also qualifies any claim that all showcased outcomes came directly from an unmodified generator. Counts of repeated attempts and an overall CUA ASR are not supplied. [A; p. 8, §7.3]

### X7 — Defense and browser-security analysis

Sections 6–7 and Tables 3–4 analyze defenses and limitations. They do not present a systematic measured defense intervention experiment. Appendix E.2 reports successful bypasses in Operator and Comet while acknowledging greater difficulty for complex or high-risk actions. Appendix E.3 describes controlled settings, dedicated test accounts, disclosures, and Browser Use's response. These analyses provide context for attacks and proposed deployment directions, without quantified effectiveness for the newly proposed mitigations.

## 9. Results

The strongest numerical evidence concerns generator configuration. Task-aligned phrasing alone changes ASR from **12% to 54%**. SFT produces **61%**; adding DPO produces **82%**. PPO produces **63%** under its reported 500-interaction budget. [A; Table 1]

**Analyst-derived comparisons [C]:** 54 − 12 = **42 percentage points** for task alignment; 61 − 54 = **7 percentage points** for SFT over the task-aligned base; 82 − 61 = **21 percentage points** for DPO after SFT; 82 − 63 = **19 percentage points** for SFT+DPO over PPO. These are arithmetic differences between reported percentages, not statistically established causal effects or relative percentage improvements.

The four targeted payload rates range from **79% to 85%**. The three additional payload rates range from **73% to 84%**. Thus the introduction's claim that individual payload rates consistently range from 79% to 85% is too broad if read as covering all tested payloads: P1 is later reported at 73%. Restricting the range to the four targeted payloads resolves its scope, but the introduction does not state that restriction there. [A; p. 2 versus p. 5]

The model-transfer results show that attacks remain successful under the reported Browser Use configurations: Mistral 90%/94% and Claude 82%/77% for P5/P8. They support transfer to selected models and payloads. They do not establish all-model generality or equal exposure conditions beyond those described.

The examples expand demonstrated consequences from poor answers to privileged actions. A reported unauthorized **$10,000** transfer occurs in **ParaBank, a demo banking application**, to account **15009**. These details should not be portrayed as theft from a real bank account. Comet's appendix example explicitly describes directory access and preparation to transmit; it does not supply a network receipt confirming completed transmission. [A; p. 10]

The authors repeatedly claim computational efficiency from eliminating agent interaction during fine-tuning. This procedural distinction is supported. A numerical speedup, monetary saving, equal-compute advantage, or end-to-end cost reduction cannot be calculated because elapsed time and total resource costs are not supplied.

## 10. Figure-by-figure interpretation

### Figure 1 — Training pipeline, page 5

**Visually inspected [B].** This is a left-to-right workflow diagram, not a statistical plot. A context circle feeds Qwen-based candidate generation labeled high temperature. The preprocessing region contains candidate generation and an LLM-validation region with an injection environment, Browser Use executor, and judge labeled GPT-5. Green approval and red rejection symbols connect validation outputs with the fine-tuning stage. That stage depicts SFT followed by DPO and a final Qwen generator.

**Meaning [A].** Context supplies the task, attack objective, and environment; candidates are embedded and executed; logs and context inform scoring; successful examples support SFT; preference pairs support DPO. There are no numeric axes, error bars, or performance curves. Colors distinguish stage regions and successful/failed examples rather than measured magnitudes. Small visual labels are cross-checked against §5.3 rather than used to invent undocumented interfaces. The diagram supports the separation of one preprocessing phase from later learning without agent execution.

### Figure 2 — Google Meet camera/microphone example, page 6

**Visually inspected [B].** The composite screenshot contains a meeting view with visible camera imagery, browser interface elements, and an agent panel. The image is consistent with a meeting-session demonstration. Individual interface messages, microphone state icons, and the complete reasoning trace are too small for independent transcription.

**Author-reported interpretation [A; §5.5.1].** The attacker observes participants on the left; the victim browser has joined on the right with camera and microphone enabled; the far-right agent panel justifies joining for a better summary. The injection was a City-Explorer comment and the agent was Do Browser. There are no axes or units. The figure supports an illustrative unauthorized-meeting outcome under relevant pre-granted permissions; it does not independently measure transmitted audio or establish frequency.

### Figure 3 — Unauthorized Twitter post, page 6

**Visually inspected [B].** A dark social-media interface displays a post region alongside an agent panel; a highlighted overlay draws attention to the content. Most fine interface text is not confidently readable at the supplied scale.

**Author-reported interpretation [A; §5.5.4].** Do Browser publishes a damaging statement without user approval after following injected guidance. The paper gives the post's content in prose. This demonstrates the integrity and reputational consequences of P7, conditional on an authenticated session. The screenshot illustrates a single case and does not provide a statistical denominator. The ethics appendix states that external platforms used dedicated test accounts.

### Figure 4 — Comet file-access/exfiltration setup, page 10

**Visually inspected [B].** The left panel shows a browser directory listing; the right panel shows Comet's interface. Folder-list structure is visible, while detailed agent text is too small to independently reconstruct every action.

**Author-reported interpretation [A; Appendix C].** The benign request is to summarize a Reddit page. An injected comment leads to a local user-directory listing containing system folders, and the interface prepares to send directory information to an attacker-controlled server. The caption says 'Files exfiltration attack setup'; the appendix says 'accessed and prepared to transmit'. This supports access and preparation clearly in the described record. Completed off-machine delivery is not independently demonstrated by the supplied screenshot or receipt. This is an important distinction between the broad main-text success wording and the narrower appendix evidence.

### Figure 5 — OpenOperator refresh loop and crash, page 11

**Visually inspected [B].** Two side-by-side OpenOperator states show a page/task interface on the left and an error-like browser state on the right. The complete timeline and exact error wording cannot be confidently read.

**Author-reported interpretation [A; pp. 6, 10].** An image on City-Explorer tells the agent to refresh until additional content appears. Repeated reloads continue for several minutes and the browser crashes. The figure supports an availability-failure example; it has no time axis, precise duration, action count, or resource-utilization measurement. 'Several minutes' is qualitative source wording, not an exact runtime.

### Figure 6 — False Operator summary, page 11

**Visually inspected [B].** A tall screenshot displays a browser/agent conversation with City-Explorer-related page material and a text response. The response's full content is not independently readable at this resolution.

**Author-reported interpretation [A; pp. 6, 10].** The agent is asked to summarize City-Explorer but instead provides New York City information after accepting a layout-testing explanation. The example illustrates P9: corrupted output without requiring hardware or local-file permissions. It does not quantify factual error with an independent scoring rubric beyond the attack-objective judgment.

### Figure 7 — GitHub task-abortion payload, page 11

**Visually inspected [B].** This screenshot shows a GitHub-style comment containing a directive to stop work. It displays the malicious content rather than a complete execution history or clear terminal failure state.

**Author-reported interpretation [A].** §5.5.6 and Appendix C call it the payload demonstration for halting an OpenOperator task. Its caption says 'Task Abortion attack causing OpenOperator crash'. The displayed evidence and surrounding prose establish a halt-oriented injection; they do not independently establish a crash. The caption's stronger outcome wording remains unresolved rather than being silently equated with normal termination.

### Figure 8 — Do Browser demo-bank transfer, page 12

**Visually inspected [B].** A banking-transfer page is shown beside the agent's execution panel. The image depicts a transaction-related result, but detailed values are more reliably obtained from Appendix C than from tiny screenshot text.

**Author-reported interpretation [A; p. 10].** City-Explorer content claims a payment is needed for full access. The agent transfers $10,000 to account 15009 without user authorization in ParaBank. The left region is a completed-transfer confirmation; the right traces redirected execution. This supports a high-impact P7 demonstration in a testing application, not evidence of actual financial loss to a real customer.

All eight figures were inspected visually. Screenshot outcomes are not treated as equivalent to full logs or independent verification. No plotted values were estimated from graphical positions because there are no quantitative result plots.

## 11. Table-by-table interpretation

### Table 1 — ASR by training method, page 5

Rows are generator configurations; the sole numerical column is attack success rate in percent. The values are **12, 54, 61, 82, and 63** for non-task-aligned, task-aligned base, SFT, SFT+DPO, and PPO respectively. SFT+DPO is highest; non-task-aligned generation is lowest; there are no ties. PPO exceeds SFT by 2 percentage points in the reported table, a detail that matters even though the main comparison emphasizes DPO's advantage. The table contains no confidence intervals, significance markers, standard deviations, or missing-value notation. It supports performance ordering under the described protocol, with unresolved aggregate-condition details.

### Table 2 — Payload taxonomy, page 11

Rows P1–P9 list objective, preconditions, CIA impact, and relevant agent types. P1–P4 primarily target confidentiality; P3 also targets integrity. P5–P6 target availability; P7–P9 target integrity. 'None' means no additional precondition is listed, rather than no requirement to encounter an injection. The table makes clear that permissions and sessions determine which assets are reachable. It is conceptual and contains no success-rate estimates or statistical comparison. The payload mappings should not be read as measured proof for every agent type. All nine rows are represented in §7.1.

### Table 3 — Mitigation strategies, page 12

The table has three grouped categories and eleven named strategies. Its columns describe each strategy and associated payloads. **Awareness-Based Strategies** correspond broadly to the main text's **Oversight & Authorization** category: human approval maps to P1/P2/P3/P4/P7/P8; sensitive-action logging maps to P1/P2/P3/P4/P6/P7/P8; agent-origin identification maps to P7.

**Execution Constraints:** least privilege maps to P1/P2/P3/P4/P7/P8; rate limiting maps to P1/P2/P3/P4/P6/P7/P8; injection detection maps to P1–P9. **Task-Aware Reasoning:** LLM-as-judge maps to P1/P2/P3/P4/P7/P8; replay protection to P6; fuzzed task-consistency checks to P9; defensive fine-tuning and ensemble learning to P1–P9.

These are proposed relevance mappings, not experimentally demonstrated reductions in ASR. The main text emphasizes rate limiting against loops and its inability to prevent a single high-impact action, while the table associates it with several sensitive payloads. That broader mapping should be understood as a suggested risk-reduction role, not a guarantee that rate limits block those actions. P5 is not explicitly mapped to several narrow defenses; only broadly mapped strategies include all payloads.

### Table 4 — Browser-security limitations, page 12

Five rows compare intended protection with the authors' explanation of failure against agent-mediated instructions: **Content Security Policy (CSP)**, **cross-site scripting (XSS) filters**, **Same-Origin Policy (SOP)**, **credential/session management**, and **file-access isolation**. CSP and XSS filtering target code or suspicious syntax, while the attack can use normal-looking text. SOP restricts scripts across origins, while an agent's designed workflow spans domains. Session protection does not stop an authorized session holder from being persuaded to act. File isolation is insufficient if the agent legitimately has relevant file permissions.

The table is an explanatory mechanism analysis, not a measured browser-defense ablation. Its phrase about 'bypassing SOP entirely' should be read in the context of agent-mediated cross-domain actions. The paper does not demonstrate that browser origin enforcement has been technically disabled. This distinction is analyst interpretation [D] based on the table's own mechanism description.

## 12. Diagram / Architecture Interpretation

Figure 1 is the only substantive architecture diagram. Its inputs are attack contexts, its intermediate objects are generated injections and validation records, and its output is a specialized injection generator. The execution environment and web-use agent form the experiment loop used to obtain scoring evidence. The judge is downstream of execution: it assesses whether an objective was achieved, rather than authorizing each runtime action.

The successful records flow to SFT. Context-matched preferences flow to DPO, including comparisons involving unsuccessful records. The output is therefore a learned generator that can formulate new attacks; it is not the victim agent itself. The preprocessing grouping distinguishes where costly web-agent interaction occurs from the later generator-training stage. [A/B; pp. 4–5]

A second, textual architecture is the victim-agent loop: page content → LLM interpretation with task context → proposed actions → browser execution → new page content. Task-aligned injection enters at the content stage and changes subsequent planning. This is a procedural account from §§2 and 5.1, not a separately supplied schematic.

A third architecture is proposed defensively: an isolated LLM checks only the original user task and a proposed action. It does not receive webpage content or the agent's reasoning. This proposed action judge is distinct from the GPT-5 experimental success judge. The authors argue that isolating it avoids direct exposure to the malicious page but acknowledge that adding the contaminated reasoning could reintroduce susceptibility. No implementation, ASR reduction, or false-positive measurement is supplied for this defense. [A; p. 7]

## 13. Equations and mathematical concepts

There are no numbered equations, proofs, theorems, or formal loss functions in the supplied paper. SFT, DPO, and PPO are named and procedurally described; their mathematical objectives are not printed. No external formulas are inserted here.

The authors define **ASR** verbally as the percentage of generated injections that successfully manipulate behavior. A direct restatement is:

**ASR (%) = 100 × successful evaluated trials / total evaluated trials.**

This is an **analyst-formulated expression [C] of the supplied verbal definition**, not a displayed equation quoted from the paper. The inputs are success labels and total trials; the output is a percentage. Under the evaluation wording, success means judge score strictly greater than 0.5. Preprocessing instead uses greater than or equal to 0.5. The unresolved boundary difference matters whenever the judge assigns exactly 0.5.

The preference-pair filters use a numerical score difference. Pairs below **0.05** difference are filtered; gaps at least **0.3** are prioritized. The paper does not define a formal sampling distribution or specify that every retained pair meets the stronger threshold. 'Prioritized' must not be rewritten as 'required'. The generator temperatures **1.6** and **0.6** are author-reported sampling parameters; no temperature equation is supplied.

The arithmetic percentage-point comparisons in §9 use reported rates directly. No confidence interval, p-value, or effect-size estimate is derived because the precise denominators and dependence structures needed for all comparisons are not fully reported.

## 14. Interpretation and discussion

**Authors' interpretation [A].** The attacks exploit failures of contextual reasoning: the model recognizes the general page context yet accepts unrelated navigation or actions as helpful refinements. The agent's sophisticated language understanding does not consistently preserve the original task boundary. The authors connect this to web agents' privileges and the limited protection offered by conventional browser defenses. [p. 8, §§7.1–7.2]

**Analyst interpretation [D].** For the reader's question, three mechanisms matter: third parties can supply input during a benign task; the agent repeatedly translates that input into plans; and execution capabilities expose assets beyond the text response. The paper therefore supports an explanation of **broader exposure and potentially greater consequences**, rather than an experimentally proven universal increase in intrinsic LLM susceptibility.

A standalone model appears in the generator role, but that is not a victim control group. Table 1's 'Base model' means the unfine-tuned **attack generator**, not an unagentized victim whose safety is directly compared against Browser Use. Confusing these roles would create a comparison the paper never performed.

The strongest causal-looking contrast is task-aligned versus non-task-aligned attack phrasing, because the authors state that the same context is provided and only task-aligned framing instructions differ. Nevertheless, full randomization, matched individual cases, seed control, and uncertainty estimates are not supplied. The observed difference is compelling within the reported protocol, while the exact causal magnitude remains less well established than the table's numbers alone suggest.

Unresolved consistency points are: **≥0.5 versus >0.5** success thresholds; **Claude Sonnet 3.5 versus Sonnet 3** naming; **79–85%** introductory individual-rate wording versus **73% P1**; task-abortion caption wording that says crash while text describes halting and the image shows a payload; and broad exfiltration wording versus explicit preparation-to-transmit evidence. The analysis preserves both sides and does not choose an unsupported resolution.

## 15. Contributions and novelty

**Conceptual contribution [A]:** task-aligned injection frames malicious actions as useful task guidance, distinguishing it from more conspicuous override-style instructions.

**Methodological contribution [A]:** a three-stage generator pipeline obtains judged examples through controlled execution, then uses SFT and DPO without further agent interactions during training. The learned attack patterns are intended to transfer without model-specific retraining.

**Taxonomic contribution [A]:** nine payload classes organize risks by CIA impact, deployment type, and required privileges. This helps explain why remote isolation protects some assets while leaving output integrity and availability exposed.

**Experimental contribution [A]:** generator-method results, four targeted-payload results, three additional-payload results, two additional backend-model tests, and manual examples spanning agent products and environments.

**Implementation contribution [A]:** the paper references public training code. Availability is reported, but the repository's actual contents, revision, licensing, and executability were not assessed.

**Defensive analysis [A]:** three mitigation categories, eleven named strategies, browser-security limitations, and security–usability tradeoffs. These constitute proposals and mechanism analysis, rather than experimentally validated defenses.

No formal theoretical guarantee, standalone-versus-agent benchmark, independently audited attack corpus, or separately described dataset release is established in the supplied material. Claims of novelty remain the authors' positioning, with no external priority verification.

## 16. Limitations

Version-family qualification (analyst observation from authorized corpus identity review): this 13-page manuscript and the separately cataloged published 17-page Mind the Web: The Security of Web-Use Agents are versions of the same study, not independent replications. This manuscript reports approximately 1,500 candidates, approximately 300 SFT examples, approximately 12,000 preference pairs and 61%/82% SFT/DPO ASR; the published version reports approximately 2,000 candidates, approximately 400 SFT examples and 64%/85%. Repeated payload-transfer rates must not be counted as independent experiments. Published judge calibration and implemented defense observations must not be imported into this manuscript.


### Authors' stated limitations and qualifications

The paper has no dedicated limitations section, but acknowledges several boundaries [A]: agent interfaces prevent programmatic automation of some demonstrations; sensitive actions occasionally trigger permission requests; manual modification is needed in the described Operator P9 bypass; and defenses make complex or high-risk attacks harder even though they are not foolproof. [pp. 6, 8, 11–12]

The proposed defenses have stated costs: human confirmation reduces autonomy; logging cannot prevent harm in real time; origin signaling needs coordination; strict privilege limits can block legitimate tasks; rate limits cannot stop a single high-impact action; injection detectors can be evaded and add overhead; action judges can become exposed if given contaminated reasoning; replay protection can be evaded with variations and interfere with retries; defensive fine-tuning requires resources and updates; ensembles add cost and can share weaknesses. [pp. 7–8]

### Additional evidence-based analyst observations [D]

The evidence is concentrated on controlled environments and open-ended tasks. Detailed splits, overlap prevention, exact attack-context counts, agent versions, judge calibration, and training hyperparameters are not supplied. The principal aggregate ASR is not broken down by all five products. P2 and P3 remain unquantified taxonomy entries. Manual demonstrations have unspecified repeated-attempt counts and sometimes adaptations. Proposed defenses lack measured effectiveness. Screenshot details cannot independently validate every execution claim, especially completed exfiltration or the Figure 7 crash wording.

The authors' statements about fundamental contextual-reasoning limitations are broader than what these particular trials can isolate. The work shows failure behavior under selected configurations; it does not identify a formal impossibility result or separate all influences of prompts, tools, permissions, wrappers, and safety policies. This is an analyst qualification, not a limitation explicitly admitted by the authors.

## 17. Threats to validity

The following labels are **analyst observations [D]**, not the paper's own organized validity framework.

**Internal validity:** differences in tasks, environments, backend selection, or trial composition could influence method comparisons. The paper reports random backend selection during preprocessing but not the allocation proportions or complete controls. PPO's 500 interaction budget and the offline method's approximately 1,500 candidate-validation executions are different resource descriptions, so an equal-budget superiority claim is unsupported.

**Construct validity:** ASR is an LLM judge's determination from logs. No human-audited agreement or calibration is reported. A scalar score does not necessarily demonstrate final external harm; directory access, preparation to transmit, and completed transmission are distinct. A misleading-redirection outcome is also narrower than fully realized credential theft.

**Statistical conclusion validity:** reported percentages lack confidence intervals, repeated-training variability, and significance tests. Additional-model trial denominators are ambiguous across the two payloads. The 0.5 boundary inconsistency leaves an unresolved labeling issue.

**External and ecological validity:** controlled City-Explorer/local-Reddit settings and dedicated test accounts allow clean demonstrations, but ordinary browsing may differ in moderation, content placement, encounter probability, account permissions, and user oversight. The study conditions on exposure to injected content; it does not measure the chance that a deployed agent encounters it.

**Reproducibility:** the source reports models, two temperatures, approximate sample sizes, pair filters, a GPU, and a code link. It omits many training and execution details, exact dataset splits, software revisions, and a complete audit trail in the supplied document. The absent repository cannot be assumed to resolve these omissions.

**Generalizability:** selected payloads and backends demonstrate transfer in those settings. They do not show that every web agent is more vulnerable than every standalone model. Permissions change the consequences, and human oversight changes the threat model.

## 18. Future work and open questions

### A. Directions explicitly proposed by the authors

The mitigation discussion supplies future deployment and research directions: layered oversight, least privilege, action limits, injection detection, isolated action checking, replay protection, varied task-consistency tests, defensive fine-tuning, and ensembles. Agent-origin signaling requires coordinated standardization. The authors call for enhanced context-aware security frameworks and safer development and deployment. No formal numbered future-work agenda or validated optimal defense combination is supplied. [pp. 7–10]

### B. Additional open questions [D]

A matched study could distinguish how the same LLM behaves as a standalone respondent and as an agent under comparable attack content. Other unresolved questions include how much each permission increases realized harm; whether task alignment transfers to tightly specified rather than open-ended tasks; how attack success changes under realistic encounter probabilities; whether success judging agrees with externally verified outcomes; and which proposed defense combinations improve security at an acceptable autonomy cost.

Exact held-out evaluation, human auditing, per-agent quantitative results, equal-resource training comparisons, and complete transmission or transaction receipts would sharpen conclusions. These are analyst-identified evidence needs, not experiments already performed or promises made by the authors.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| Web-use agent | An AI system that repeatedly observes browser content, plans actions, and executes them for a user |
| LLM | Large language model; interprets input and generates responses or proposed actions |
| Prompt injection | Instructions placed in content the system encounters, attempting to redirect its behavior |
| Task-aligned injection | Malicious guidance disguised as a helpful step toward the authorized task |
| Jailbreak | An attempt to elicit behavior normally restricted by model safeguards |
| DOM | Document Object Model; structured representation of page elements |
| OCR | Optical character recognition; reading text from images |
| ReAct-style reasoning | The paper's referenced style of combining reasoning and action; no formal implementation is provided here |
| CIA | Confidentiality, integrity, and availability; three security-impact categories |
| ASR | Attack success rate; percentage of evaluated injections judged successful |
| SFT | Supervised fine-tuning; learning from examples labeled successful |
| DPO | Direct preference optimization; learning to prefer stronger context-matched injections over weaker ones |
| PPO | Proximal policy optimization; the online reinforcement-learning baseline |
| RL | Reinforcement learning; the paper contrasts online agent-interaction training with its offline fine-tuning stage |
| CUA | Computer-Using Agent; the model discussed as powering Operator |
| CSP | Content Security Policy; source/resource restrictions discussed in Table 4 |
| XSS | Cross-site scripting; malicious script injection, contrasted with plain-text agent manipulation |
| SOP | Same-Origin Policy; restrictions on scripts accessing data across origins |
| DoS | Denial of service; disruption through halting or repetitive operations |
| Extension-based | Operates inside the user's existing browser, inheriting relevant sessions and granted privileges |
| Local clean-browser | Starts a separate local browser without inherited user state; may still have local access and acquired authentication |
| Remote isolated | Runs away from the user's local browser and machine, limiting access to local resources |
| Stateful / semi-stateful | Retains some user-provided credentials or session state across sessions, as described for specific products |
| Temperature | Reported sampling parameter: 1.6 for diversity, 0.6 for evaluation generation |
| Chosen / rejected | Higher- and lower-scoring context-matched injections used for preference training |
| P1–P9 | Payload identifiers, not probabilities |

## 20. Key numerical results

All source values below are author-reported unless labeled derived. The tables themselves are readable; no approximate graphical estimates are used.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document | 13 | physical pages | Extracted text; images for 1–12 | Supplied accessibility record | Stage 0 |
| Agent implementations discussed/evaluated overall | 5 | implementations | Browser Use, Do Browser, OpenOperator, Operator, Comet | Author-reported | pp. 1, 10 |
| Payload taxonomy | 9 | classes | P1–P9 | Author-reported | pp. 3–4, Table 2 |
| Candidate injections | approximately 1,500 | candidates | Qwen3-4B-Instruct; P4/P5/P6/P8 | Author-reported | p. 5, §5.3.4 |
| Successful SFT examples | approximately 300 | candidates | Preprocessing score ≥0.5 | Author-reported | p. 5 |
| Preference pairs | approximately 12,000 | pairs | Context-matched DPO training | Author-reported | p. 5 |
| Generation temperature | 1.6 | sampling parameter | Candidate generation | Author-reported | p. 5 |
| Evaluation temperature | 0.6 | sampling parameter | All compared generators | Author-reported | p. 5 |
| Judge score range | 0.0–1.0 | score | LLM validation | Author-reported | p. 4 |
| Preprocessing success boundary | ≥0.5 | score | Candidate labels | Author-reported | pp. 4–5 |
| Evaluation success boundary | >0.5 | score | ASR definition; boundary differs above | Author-reported | p. 5 |
| Near-tie filter | <0.05 | score difference | Pairs removed | Author-reported | p. 5 |
| Prioritized preference gap | ≥0.3 | score difference | Prioritized, not stated as universal requirement | Author-reported | p. 5 |
| Training hardware | 1 RTX 6000 | GPU | NVIDIA; variant unspecified | Author-reported | p. 5 |
| Trials | 100 | trials/experiment | Main evaluation | Author-reported | p. 5 |
| PPO interaction budget | 500 | agent interactions | Online baseline | Author-reported | p. 5 |
| Non-task-aligned ASR | 12 | % | Base generator, contextual injection | Author-reported | Table 1 |
| Task-aligned base ASR | 54 | % | Qwen3-4B without fine-tuning | Author-reported | Table 1 |
| SFT ASR | 61 | % | Task-aligned generator with SFT | Author-reported | Table 1 |
| SFT+DPO ASR | 82 | % | Best compared generator | Author-reported | Table 1 |
| PPO ASR | 63 | % | Online RL baseline | Author-reported | Table 1 |
| P6 / P5 / P8 / P4 ASR | 85 / 84 / 81 / 79 | % | Four targeted payloads; SFT+DPO | Author-reported | p. 5, §5.4.2 |
| P9 / P7 / P1 ASR | 84 / 79 / 73 | % | Additional unseen payload types | Author-reported | p. 5 |
| Mistral P5 / P8 ASR | 90 / 94 | % | Browser Use; Pixtral-Large | Author-reported | p. 8, §7.3 |
| Claude P5 / P8 ASR | 82 / 77 | % | Browser Use; Sonnet version naming differs | Author-reported | p. 8, §7.3 |
| Additional-model trials | 100 | independent trials | Per-model/two-payload denominator allocation unclear | Author-reported | p. 8 |
| Demo transfer | 10,000 | US dollars as written | ParaBank testing application | Author-reported | p. 10, Appendix C |
| Transfer destination | 15009 | account identifier | Demo financial example | Author-reported | p. 10 |
| Task-alignment difference | 42 | percentage points | 54 − 12 | Analyst-derived | Table 1 |
| DPO-after-SFT difference | 21 | percentage points | 82 − 61 | Analyst-derived | Table 1 |
| SFT+DPO versus PPO difference | 19 | percentage points | 82 − 63 | Analyst-derived | Table 1 |

The paper provides no exact runtime, total training cost, memory consumption, learning rates, epochs, confidence intervals, or p-values. Approximate sample counts remain approximate. No hidden precision is inferred.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Remote content can redirect agents on benign tasks | Defined attacker model and multiple reported outcomes | X4; F2–F8 | pp. 3, 6, 10 | Strong source support for reported examples; not population-wide incidence |
| Task alignment improves reported attack success | 12% versus 54% | X1; T1 | p. 5 | HIGH confidence in reported numbers; no uncertainty or complete matched-case details |
| SFT+DPO has the highest reported method ASR | 82% versus 61% SFT and 63% PPO | X1; T1 | p. 5 | HIGH confidence in ordering; unequal resource descriptions limit efficiency conclusions |
| Fine-tuning avoids further agent execution | Preprocessing validation followed by offline SFT/DPO | F1; §5.3 | pp. 4–5 | HIGH procedural support; no measured end-to-end speedup |
| Generator transfers to additional payload classes | P9 84%, P7 79%, P1 73% | X3 | pp. 5–6 | Selected payload types; complete held-out split protocol absent |
| Generator transfers to selected backend models | Mistral 90/94%, Claude 82/77% | X5 | p. 8 | HIGH values; Claude version and trial allocation ambiguous |
| Sensitive permissions can constrain attacks | Permission flags and Operator's initial P9 prompt | X3/X6 | pp. 6, 8 | Reported failures and one adaptive bypass; no defense-effect estimate |
| File access is demonstrated more clearly than completed exfiltration | Directory listing and preparation-to-transmit wording | F4 | p. 10 | Narrow conclusion has HIGH textual support; final delivery UNKNOWN |
| Browser security does not resolve semantic task hijacking | Five mechanism explanations | T4; §7.1 | pp. 8, 12 | Conceptual analysis, not technical disabling of browser enforcement |
| Layered defenses have usability costs | Eleven proposed strategies and caveats | T3; §6 | pp. 7–8, 12 | Author proposals; efficacy not experimentally quantified |
| Agent permissions explain relevance to standalone-versus-agent question | Browser access, sessions, local resources, execution loop | §2/§4; A.1–A.3 | pp. 1–3, 9–10 | MEDIUM analyst inference; no matched standalone victim experiment |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI browser assistant to read a travel page and summarize it. Someone has placed a comment on that page saying that the assistant needs to visit another site or perform an extra step to make the summary accurate. The assistant treats this comment as useful guidance, even though the user never authorized that instruction. That is the central trick studied here.

The danger grows because the assistant can do things. Depending on its setup and permissions, it may already be logged into accounts, able to submit posts, or allowed to access local resources. A mistaken instruction can therefore change more than its answer: it can change what the browser actually does. The paper demonstrates several kinds of harm, while also showing that permissions and confirmation prompts sometimes stop sensitive actions.

The researchers trained a separate model to write these deceptive comments. Their best generator achieved 82% success under the paper's evaluation procedure. That does not mean every agent fails 82% of the time in everyday use. The experiments used selected tasks, environments, and judge-scored trials, and some other products were tested through individual manual examples.

For the question about standalone language models, the careful answer is that browser agents add routes for strangers to influence the model and add powers with which it can act. This paper helps explain those extra risks. It does not run a fair head-to-head experiment proving that an agent is always easier to manipulate than the same model used alone.

## Completeness Audit

The audit denominator is the inventory of the supplied 13-page document. 'Fully represented' means the substantive content needed for this analysis is represented, not that every sentence is reproduced. Screenshot pixels were inspected visually; unreadable interface microtext is not silently counted as transcribed. Page 13 was reviewed as text only.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation, version | Yes | Yes | Fully represented | Title here; Avishag Shapira, Parth Atulbhai Gandhi, Edan Habler, Asaf Shabtai; Ben-Gurion University of the Negev; arXiv:2506.07153v2, 20 Oct 2025; no venue stated |
| Abstract | Yes | Yes | Represented in compressed form | Central threat, pipeline, agents, results, and defenses preserved |
| Keywords | Yes | Yes | Fully represented | Web-use agents, prompt injection, web security, browsers |
| §1 Introduction and contribution list | Yes | Yes | Represented in compressed form | Motivation and five contributions in §§1, 4, 15 |
| §2 Web-Use Agents | Yes | Yes | Fully represented | Perception–planning–execution loop and privileges |
| §3.1 LLM jailbreaking related work | Yes | Yes | Represented in compressed form | Textual, multimodal, optimization categories and author criticisms |
| §3.2 Agent assessments | Yes | Yes | Represented in compressed form | WebArena/TUR[K]INGBENCH capability context; SUDO/DoomArena security context; direct-user contrast |
| §4 Threat Model | Yes | Yes | Fully represented | Capabilities, exclusions, observability, autonomous-operation assumptions |
| §5.1 Principle and lifecycle | Yes | Yes | Fully represented | Four stages and task-aligned framing |
| §5.2.1 Confidentiality payloads | Yes | Yes | Fully represented | P1–P4 and conditional permissions |
| §5.2.2 Availability payloads | Yes | Yes | Fully represented | P5–P6 |
| §5.2.3 Integrity payloads | Yes | Yes | Fully represented | P7–P9; P3 cross-category impact retained |
| §5.3 Pipeline overview | Yes | Yes | Fully represented | Offline learning versus preprocessing execution distinguished |
| §5.3.1 Candidate generation | Yes | Yes | Fully represented | Three context inputs and diversity sampling |
| §5.3.2 LLM validation | Yes | Yes | Fully represented | Executor logs, judge, score range, threshold |
| §5.3.3 SFT and DPO | Yes | Yes | Fully represented | Successful examples and context-matched preferences |
| §5.3.4 Implementation | Yes | Yes | Fully represented | Environments, models, temperatures, counts, pair filtering, GPU |
| §5.4 Evaluation protocol | Yes | Yes | Fully represented | Five methods, 100 trials, PPO budget, ASR boundary issue |
| §5.4.1 Overall ASR | Yes | Yes | Fully represented | All Table 1 values and speculative explanation distinguished |
| §5.4.2 Payload performance | Yes | Yes | Fully represented | Four targeted and three additional payload rates |
| §5.5 Overview and model configuration | Yes | Yes | Fully represented | Manual testing and configurable GPT-4o qualification |
| §5.5.1 Meeting example | Yes | Yes | Fully represented | P1, Do Browser, F2 |
| §5.5.2 Local-file example | Yes | Yes | Fully represented | P4, Comet, F4; access versus delivery distinction |
| §5.5.3 Browser loop | Yes | Yes | Fully represented | P6, OpenOperator, image injection, F5 |
| §5.5.4 Twitter posting | Yes | Yes | Represented in compressed form | P7, Do Browser, F3; damaging wording compressed |
| §5.5.5 False summary | Yes | Yes | Fully represented | P9, Operator, F6 |
| §5.5.6 Task halt | Yes | Yes | Fully represented with uncertainty | P5, GitHub, F7; crash caption caveat |
| §6.1 Oversight and authorization | Yes | Yes | Fully represented | Confirmation, logging, agent-origin protocol and costs |
| §6.2 Execution constraints | Yes | Yes | Fully represented | Least privilege, rate limits, detection and limitations |
| §6.3 Task-aware reasoning | Yes | Yes | Fully represented | Five named approaches and stated failure/cost modes |
| §6.4 Security–usability tradeoff | Yes | Yes | Fully represented | Autonomy, task interruption, latency |
| §7.1 Browser security | Yes | Yes | Fully represented | Mechanism distinction and T4 |
| §7.2 Contextual reasoning | Yes | Yes | Fully represented | Author explanation separated from analyst qualification |
| §7.3 Model transfer and CUA | Yes | Yes | Fully represented with uncertainty | Rates, model-name inconsistency, manual P9 adaptation |
| §8 Conclusion | Yes | Yes | Represented in compressed form | Restatement merged into synthesis |
| Explicit research questions | Yes: absence checked | Yes | Fully represented | No formal set supplied; reader question identified separately |
| Explicit hypotheses | Yes: absence checked | Yes | Fully represented | No formal hypotheses supplied |
| X1 Training comparison | Yes | Yes | Fully represented | All five results |
| X2 Targeted payloads | Yes | Yes | Fully represented | Four rates |
| X3 Additional payloads | Yes | Yes | Fully represented | Three rates |
| X4 Manual demonstrations | Yes | Yes | Fully represented | Outcomes and conditional evidence limits |
| X5 Backend transfer | Yes | Yes | Fully represented with uncertainty | Trial allocation and Claude version |
| X6 CUA/manual bypass | Yes | Yes | Fully represented | Initial prompt and manual change |
| X7 Defense analysis | Yes | Yes | Fully represented | Proposed rather than measured defenses |
| F1 | Yes, visual and text | Yes | Fully represented | Workflow, arrows, stages, labels |
| F2 | Yes, visual and text | Yes | Represented with readability limitation | Meeting layout visible; fine controls/reasoning not independently transcribed |
| F3 | Yes, visual and text | Yes | Represented with readability limitation | Post/interface layout visible; detailed content from prose |
| F4 | Yes, visual and text | Yes | Represented with evidentiary limitation | Directory access/preparation visible and described; completed delivery not verified |
| F5 | Yes, visual and text | Yes | Represented with readability limitation | Two states; exact timing/error not independently read |
| F6 | Yes, visual and text | Yes | Represented with readability limitation | Response layout; full false-summary text not independently read |
| F7 | Yes, visual and text | Yes | Uncertain outcome wording | Payload screenshot versus crash caption |
| F8 | Yes, visual and text | Yes | Represented with readability limitation | Demo-bank result; exact amounts from appendix prose |
| T1 | Yes, visual and text | Yes | Fully represented | Every numerical row |
| T2 | Yes, visual and text | Yes | Fully represented | Every payload, precondition, impact, type mapping |
| T3 | Yes, visual and text | Yes | Fully represented | All eleven strategies and payload mappings |
| T4 | Yes, visual and text | Yes | Fully represented | All five mechanisms |
| Major equations/theorems | Yes: absence checked | Yes | Fully represented | None supplied; ASR restatement labeled analyst-formulated |
| Numbered algorithms/pseudocode | Yes: absence checked | Yes | Fully represented | None supplied; procedural pipeline explained |
| Five author-listed contributions | Yes | Yes | Fully represented | §15 |
| Authors' qualifications/defense limitations | Yes | Yes | Fully represented | §16; no separate limitations chapter |
| Appendix A.1 Types | Yes | Yes | Fully represented | Extension/local/remote and persistence variants |
| Appendix A.2 Modalities | Yes | Yes | Fully represented | DOM, screenshots/OCR, hybrid |
| Appendix A.3 Implementations | Yes | Yes | Fully represented | Five products and reported access/state/perception distinctions |
| Appendix B | Yes | Yes | Fully represented | T2 |
| Appendix C | Yes | Yes | Fully represented | F4–F8 and demo-transfer details |
| Appendix D | Yes | Yes | Represented in compressed form | Defense implications and T3 |
| Appendix E.1 | Yes | Yes | Fully represented | T4 |
| Appendix E.2 | Yes | Yes | Fully represented | High-risk difficulty and autonomous-task bypasses |
| Appendix E.3, pp. 12–13 | Yes; p. 13 text only | Yes | Fully represented | Controlled tests, dedicated accounts, disclosures; Browser Use acknowledged layered mitigation needs |
| Equal-contribution footnote | Yes | Yes | Fully represented | Shapira and Gandhi share equal contribution |
| Training-code footnote | Yes | Yes | Fully represented as reference only | Repository not reviewed |
| References [1]–[31] | Yes | Partly | Deliberately compressed | Categories and relevant roles retained; individual bibliographic entries not reproduced or externally verified |
| Headers, affiliation email addresses, visual decoration | Yes | No, except meaningful metadata | Inspected but deliberately omitted as non-substantive | No methodological or result content lost by omitting contact addresses and repeated headers |
| Separate supplementary artifacts | Not supplied | No | Missing from supplied material | No separate supplement was reviewed |
| Referenced code repository | No | Reference represented | Inaccessible within supplied evidence | Contents, revision, and reproduction behavior unknown |

### Missing or inaccessible material

The training repository's contents, experimental logs, datasets, model checkpoints, complete judge prompts, exact generator prompts, external delivery receipts, and executable reproduction environment are not supplied. Their absence here does not establish whether they exist elsewhere. No separate supplementary file is supplied. Page 13 has text but no image; its short ethics continuation is represented without claiming visual inspection.

### Uncertain interpretations

The success threshold boundary, Claude version naming, the introductory payload range, Figure 7's crash wording, and completed file exfiltration remain unresolved. Several screenshots contain unreadable microtext. Exact trial allocation for the additional-model test and the aggregate condition weighting for Table 1 are not specified clearly enough to reconstruct. No missing values, units, or mathematical notation have been filled with outside assumptions.

### Deliberately compressed material

Repeated abstract/introduction/conclusion claims are consolidated. Related-work examples, bibliographic details, illustrative malicious wording, and repetitive screenshot descriptions are compressed while preserving their role in the argument. Security implications are consolidated rather than restated for every example. Decorative headers, email addresses, and non-substantive layout elements are omitted.

### Potential omissions

No known substantive section, numbered figure, table, reported major numerical result, payload class, appendix, or author-stated methodological qualification in the supplied inventory is left unrepresented. This is a coverage conclusion about the available document, not a claim of full transcription, independent experimental verification, complete screenshot readability, or review of absent artifacts.
