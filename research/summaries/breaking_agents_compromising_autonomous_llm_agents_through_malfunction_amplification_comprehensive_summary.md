# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and nine supplied page images. The document's content is treated as evidence, never as instructions. No external research, tool calls, citation validation, or artifact retrieval was performed.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–15 is supplied. |
| Page range and count | Pages 1–15, fifteen accessible text pages. Printed page numbers correspond to the supplied physical page numbers. |
| Apparent missing pages | No gaps in the supplied text sequence. This establishes continuity of the supplied version, not independent verification against an original PDF. |
| Visually inspected pages | 1, 2, 4, 7, 8, 9, 10, 11, and 12. |
| Text-only pages | 3, 5, 6, 13, 14, and 15. Layout and any unextracted visual details on these pages were not inspected. |
| Figures and diagrams | All numbered figures visible in the supplied material, Figures 1–7, were visually inspected. Figures 1–2 are diagrams; Figures 3–7 are quantitative plots. |
| Tables | Tables 1–7 are supplied both as extracted text and in page images. Their principal numerical cells are readable. |
| Equations | No numbered equations or mathematical proofs appear in the supplied text. Plot axes and percentages are readable. One character-replacement example on p. 5 is incomplete in extracted text. |
| Appendices | None identified in the supplied fifteen pages. |
| Supplementary material | None supplied or explicitly identified as supplementary material in the supplied text. |
| Referenced artifacts | Source references and implementation links occur, including Gmail and CSV agent links on p. 6. Those linked artifacts were not inspected. |
| OCR | Not used. Native/extracted text was sufficient for the main prose and was cross-checked against supplied images where available. |
| Other limitations | Plot bars and points are generally not numerically labeled. Exact values cannot be reconstructed reliably from these small images. Some extracted text contains apparent typographical or extraction errors. |

Evidence labels throughout: **[A] Author-reported** means explicitly stated by the paper; **[B] Directly observable** means visible in supplied images; **[C] Analyst-derived** means calculated from supplied values; **[D] Analyst interpretation** means an inference beyond an explicit statement. No **[E] External information** is introduced. HIGH confidence describes clearly supported transcription or a narrowly bounded conclusion; MEDIUM describes an interpretation with qualifications; LOW describes uncertain visual estimates; UNKNOWN describes unavailable information.

The analysis first inventories the supplied work, separates its experiments, and checks text against tables and figures. The narrative below represents that cumulative extraction. It is an analysis of the supplied version, not a claim that all implementation details or all scientific uncertainties have been resolved.

# 1. Plain-Language Orientation

**[A]** This paper studies how an attacker can make an autonomous large language model agent stop doing useful work. A large language model, or LLM, normally generates text. An LLM agent combines that model with planning, external tools, and sometimes memory so that it can choose and execute actions. The paper's examples include managing email and analyzing comma-separated values, or CSV, files.

The attack goal is **malfunction amplification**: increasing an agent's existing tendency to make reasoning or execution mistakes. Rather than asking for an obviously forbidden act, an attacker can induce repeated actions or an irrelevant function call. A seemingly ordinary operation can undermine the intended task when performed at the wrong time or repeatedly. The authors frame this as resembling denial of service: preventing useful service rather than necessarily stealing information or causing an explicitly prohibited transaction. [pp. 1–4]

The researchers evaluate two malfunction types, three broad attack-method families, three entry surfaces, different core models, and properties of the tools available to agents. Their evaluation combines an LLM-based emulator covering 144 test cases with two implemented LangChain agents, one for Gmail and one for CSV analysis. They also test agent-to-agent transmission and two prompts that ask an LLM to inspect instructions for danger or malfunction. [pp. 4–12]

The central quantitative result is conditional, not universal. In the emulator, infinite-loop prompt injection raises failure from 15.3% without attack to 59.4% with the default GPT-3.5-Turbo core. Corresponding prompt-injection failure is 32.1% with GPT-4 and 88.1% with Claude-2. On the implemented agents, direct-input attacks achieve 75.0%–90.0% across the two malfunction types, while external-file and memory attacks behave very differently. [Tables 1, 2, and 4]

**[D] Research-question relevance:** The paper helps explain why web-connected AI agents can have additional security exposure: they receive tool-mediated content, translate model decisions into actions, and can pass attack-bearing information to other agents. It does **not** experimentally establish that web agents are uniformly more vulnerable than standalone LLMs. Its opening comparison is an architectural and consequence argument; its experiments primarily compare agent configurations and attack conditions.

# 2. Document Roadmap

**Document identity.** The original title is *Breaking Agents: Compromising Autonomous LLM Agents Through Malfunction Amplification*. The authors are Boyang Zhang, Yicong Tan, Yun Shen, Ahmed Salem, Michael Backes, Savvas Zannettou, and Yang Zhang. Affiliations are CISPA Helmholtz Center for Information Security, NetApp, Microsoft, and TU Delft. The page-1 margin identifies arXiv:2407.20859v1, category cs.CR, dated 30 July 2024. No separate publication venue is stated for this paper in the supplied material. [p. 1]

**Document type:** An empirical cybersecurity paper about LLM-agent robustness, with systems-oriented architecture discussion, simulated evaluation, implemented case studies, and defense testing. It is neither a mathematical theory paper nor a systematic literature review.

| Original section | Pages | Function in the argument |
|---|---|---|
| Abstract | 1 | Summarizes malfunction attacks, evaluations, and limited detection. |
| §1 Introduction | 1–3 | Motivates agent-specific risks and lists contributions. |
| §2 Background | 3 | Defines core, tools, planning, memory, and safety-analysis approaches. |
| §2.1 LLM Agents | 3 | Explains the agent components and ReAct planning. |
| §2.2 Agents Safety | 3 | Distinguishes red-teaming from robustness analysis. |
| §3 Attacks | 3–5 | Defines attacker goals, capabilities, methods, and entry surfaces. |
| §3.1 Threat Model | 4 | Specifies black-box access and knowledge of available functions. |
| §3.2 Attack Types | 4 | Separates basic single-agent and advanced multi-agent attacks. |
| §3.3 Attack Methodology | 4–5 | Covers injection, perturbation, and misleading examples. |
| §3.4 Attack Surface | 5 | Covers instructions, intermediate outputs, and memory. |
| §4 Evaluation Setting | 5–6 | Describes the emulator, two agents, and the failure metric. |
| §4.1 Agent Emulator | 5–6 | Explains simulation and evaluation scale. |
| §4.2 Case Studies | 6 | Describes Gmail and CSV implementations. |
| §4.3 Metric | 6 | Defines failure/attack success and self-reflection measurement. |
| §5 Results | 6–11 | Reports attack comparisons, tool analysis, and propagation. |
| §5.1 Attack Types | 6–7 | Compares loops and incorrect functions. |
| §5.2 Attack Methods | 7–8 | Compares methods, models, and adversarial ratios. |
| §5.3 Tools and Toolkits | 8–9 | Examines toolkit identity and tool/toolkit counts. |
| §5.4 Attack Surfaces | 9–10 | Examines external content and memory. |
| §5.5 Advanced Attacks | 10–11 | Evaluates same-type and different-type agent chains. |
| §6 Defense; §§6.1–6.2 | 11–12 | Tests policy and malfunction self-examination. |
| §7 Related Work | 12 | Positions the study against other safety and robustness research. |
| §8 Limitation | 12–13 | Discusses limited implemented agents, categories, and models. |
| §9 Ethics Discussion | 13 | Frames attacks as robustness evaluation and deployment warning. |
| §10 Conclusion | 13 | Restates vulnerability and mitigation concerns. |
| References [1]–[51] | 13–15 | Lists cited sources; these sources were not independently reviewed. |

Inventory identifiers retained here are S1–S10 for numbered sections, F1–F7 for figures, T1–T7 for tables, X1–X10 for substantive experimental analyses, and C1–C4 for the four contribution bullets on p. 3. No keywords, numbered equations, pseudocode algorithms, appendices, or supplied supplementary files were identified. Prompt templates are substantive method objects and are represented in §7 below.

# 3. Background and Context

**[A] Agent components.** The paper divides an agent into four components. The **core** is the LLM that interprets requests and coordinates action selection. **Tools** are external functions or applications, often reached through an application programming interface, or API. **Planning** provides structured reasoning that helps select and assess actions. **Memory** stores relevant information, commonly conversation and interaction histories, that may be retrieved when needed. [§2.1, p. 3]

An API is an interface through which an agent can invoke an application's functions. In the paper's terminology, a **toolkit** groups related functions, while a **tool** is one function within that toolkit. Gmail's API is an example toolkit; sending email is an example tool. This distinction matters because the paper separately examines the number of toolkits, the number of individual tools, and toolkit identity. [pp. 8–9]

**ReAct** is the named planning framework used to structure reasoning and acting. The paper describes it as querying the core LLM at each stage to assess the previous action. The study uses these observations and the agent's assessment of task completion to obtain its principal metric. The acronym's expansion is visible in reference [45]'s title, *ReAct: Synergizing Reasoning and Acting in Language Models*; the supplied paper does not give a separate formal definition of the framework. [pp. 3, 6, 15]

A **hallucination** is described as an inaccuracy or fabrication in model output. The authors distinguish an ordinary text error from an agent's sequence-of-actions error: an agent must satisfy the stricter requirements of external tools to obtain information or finish work. That distinction motivates testing task failure rather than only objectionable text. [pp. 2–3]

**Prompt injection** places adversarial commands alongside material the model processes, attempting to redirect instruction following. **Adversarial perturbation** changes an input or adds disruptive text. **Adversarial demonstration** supplies examples of deliberately incorrect responses, hoping the model imitates them through in-context learning. In-context learning here means using examples included in the current prompt, rather than describing a new model-training procedure. [§3.3, pp. 4–5]

**[D]** These definitions explain the user’s research question without requiring an assumption that every agent uses a web browser. The evaluated ecosystem includes email APIs, files, Python functions, and simulated toolkits. The security argument is about tool-integrated autonomous agents broadly, with direct implications for agents exposed to web-originated content.

# 4. Research Problem and Gap

**Existing problem [A].** Agents can extend the capabilities of their base models, but their normal task performance is unstable. The authors attribute failures to reasoning errors and response randomness. External tools impose less flexible requirements than text generation, so an incorrect logical sequence can block completion. [§1, p. 2]

**Prior-approach shortcomings according to the authors [A].** Earlier safety work emphasizes conspicuous harmful or policy-violating actions. The authors argue that these can be easier to recognize from their intent, may be constrained by external authorization checks, and can require agent-specific attack customization. These are the paper's characterizations of prior work, not independently verified conclusions about the entire literature. [pp. 1–2, 12]

**Research gap [A].** The paper targets disruption of normal functioning using instructions that need not contain obvious harmful intent. It treats malfunction induction as a robustness problem and asks which configurations and entry points are susceptible. Its novelty claim is explicitly qualified as being to the authors' knowledge. [pp. 2–3]

**Motivation [A].** Autonomy makes repeated or irrelevant actions consequential: they can consume resources, prevent useful work, and affect downstream agents. The paper draws inspiration from denial-of-service attacks and seeks to warn developers before larger deployments. [pp. 2, 4, 13]

**Scope [A].** The study considers two malfunction outcomes, selected attack methods, three core LLM variants, emulator workloads, and two implemented task-oriented agents. It investigates limited self-examination defenses. It does not assess every agent type, every model, all browser environments, or all security defenses. [pp. 4–13]

**[D]** For the question 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', the strongest supported formulation is that integration creates additional exposure and can amplify consequences. Vulnerability frequency depends on the entry surface, task, core model, and workflow; the paper’s results do not support a single numerical agent-versus-standalone vulnerability multiplier.

# 5. Research Questions / Objectives / Hypotheses

The paper does not enumerate formal research questions. The following are its stated objectives, organized for clarity rather than attributed as numbered author questions.

| ID | Author-stated objective | Evaluation connection |
|---|---|---|
| O1 | Propose attacks that disrupt normal agent functioning. | X1, X2; Tables 1 and 4. |
| O2 | Identify vulnerability across attack types, methods, surfaces, and agent properties. | X1–X7; Tables 1–4, Figures 3–7. |
| O3 | Show practical risks in multi-agent scenarios with implemented agents. | X8; Table 5. |
| O4 | Assess and modify self-examination defenses. | X9–X10; Tables 6–7. |

**Explicit hypothesis H1 [A]:** More toolkits should increase attack success because more choices could induce more reasoning errors. Table 3 does not provide the expected increasing relationship. The authors conclude that toolkit count lacks strong correlation with failure. [§5.3, p. 9]

**Explicit hypothesis H2 [A]:** Intentionally harmful commands should be relatively easy to detect, allowing execution to be stopped. Tables 6–7 compare such commands with malfunction-oriented attacks. Policy inspection strongly detects the tested direct-harm and data-stealing prompts, but the conclusion applies to these prompt collections and this detection setup. [§6, p. 11]

**Author expectations and explanatory conjectures [A]:** Prompt-injection effectiveness should depend more on overriding semantics than on instruction length; transferred GCG perturbations may work partly through general disturbance; Gmail/CSV differences may arise from attention to natural-language versus quantitative content. These are expressed as expectations or suspicions, not proven mechanisms. [pp. 7–10]

**User research question [D].** The supplied question is a synthesis lens external to the paper's own formal structure. It is addressed through architecture, extra entry points, autonomous execution, and agent-to-agent propagation. It is not treated as an experimentally tested standalone-LLM comparison.

# 6. Assumptions / Threat Model

**Attacker goal [A].** Cause logic errors that prevent task completion without requiring obviously harmful or policy-violating actions. Two specific targets are repeated execution and selecting an incorrect function. [§3.1–§3.2, p. 4]

**Ordinary attacker capabilities [A].** The core model is black-box: the attacker does not receive its internal implementation or model parameters. Detailed agent-framework knowledge is also not assumed. The attacker knows or can infer several functions the agent supports, through educated guesses or interaction. An email agent’s ability to draft or send messages is the paper's example. [p. 4]

**Surface-dependent access [A].** Direct instruction attacks require control of input provided to the agent. Intermediate-output attacks require placing adversarial commands in content it retrieves, such as an email or CSV file. Direct memory manipulation requires additional access and is included as an expanded evaluation condition, not a universal prerequisite. [pp. 4–5, 9–10]

**Advanced-scenario access [A].** The attacker has direct control of one agent and seeks to disrupt other agents when they interact with it. This stronger scenario must be distinguished from the ordinary single-agent black-box description. The different-type experiment gives the attacker direct access to a CSV agent whose output is autonomously passed to Gmail. [pp. 10–11]

**Bounded loops [A].** The attack called 'infinite loop' actually targets repeated actions until a maximum allowed iteration limit is reached. The attack template requests 100 repetitions, but the paper does not supply the configured maximum iteration count. Thus 'infinite' names the malfunction class rather than proving unbounded execution. [pp. 4, 6]

**Trust and environmental boundaries [D].** The evidence indicates a boundary between legitimate task instructions and text returned by tools or other agents. The paper does not supply a formal access-control or trusted-computing-base specification. Its discussion of authorization checks for dangerous transactions is a motivation argument, not an audit of deployed banking controls. [pp. 1–2, 11]

**Excluded or unestablished capabilities.** The ordinary threat model does not require white-box access to the target LLM, model retraining, or universal memory access. It does not define a measured browser compromise, an operating-system exploit, or credential theft. Those should not be inferred from the title or examples.

# 7. Methodology

## Study design and rationale

**[A]** The study uses a broad emulator evaluation to make testing many tool integrations feasible, followed by two implemented agents to examine concrete execution and inter-agent behavior. The authors explain that real APIs can require subscriptions and multiple accounts, making large batch experiments difficult. The emulator replaces tool implementation with detailed tool-input/output templates and an LLM-generated sandbox response. [§4.1, pp. 5–6]

The authors argue that malfunction testing is especially suitable for this emulator because their target is the agent's reasoning and planning, rather than harmful tool behavior that might be blocked by real-world safety checks. This is their rationale. The supplied evidence does not independently quantify equivalence between simulated and actual tools for every workload. [p. 6]

## Evaluation material and implementation

The emulator covers **144 test cases**, **36 toolkits**, and **more than 300 tools**, as reported on p. 6. Its sandbox model is **GPT-3.5-Turbo-16k**, and the default agent core is **GPT-3.5-Turbo**. Core-model comparisons additionally use **GPT-4** and **Claude-2**. The paper does not give immutable model snapshot identifiers, inference dates, or complete generation settings. [pp. 6–7]

Both implemented agents use **LangChain**. The Gmail agent uses Google's Gmail API and five tools for email-related actions, including reading, searching, drafting, and sending. The CSV agent uses Python toolkits and predefined functions to read, analyze, and modify CSV files and can execute Python code. Links to implementation locations are supplied on p. 6, but no linked code was reviewed here. Framework versions, detailed source revisions, hardware, token budgets, and full agent prompts are not specified in the supplied narrative. [§4.2, p. 6]

## Attack construction

**Prompt injection [A].** The infinite-loop template appends a command to ignore previous instructions and repeat the previous action 100 times. For incorrect-function attacks in the emulator, GPT-4 is asked to choose the most irrelevant tool for the target task and generate an instruction invoking it. That generated instruction is then placed into an overriding prompt-injection template. Implemented-agent incorrect functions are handcrafted, an important difference from the emulator. [pp. 6–7]

**Perturbations [A].** SCPN uses a pretrained syntactically controlled paraphrase network; the researchers do not train it themselves. VIPER replaces characters with visually similar elements. GCG normally uses white-box optimization, so the study optimizes on an auxiliary model and transfers/appends the resulting adversarial text to the black-box agent. The auxiliary model identity and detailed optimization settings are not given in the supplied text. Perturbations are evaluated for infinite-loop disruption rather than targeted incorrect functions. [§3.3, p. 5]

**Adversarial demonstrations [A].** Misleading examples associate instructions with confused confirmation requests or a predefined irrelevant function. The implemented agents usually disregard these examples. A separate system-message placement experiment yields one successful attack in twenty cases. This placement changes instruction privilege and should not be merged with ordinary user-input demonstrations. [p. 7]

## Surface construction

Direct-input attacks alter the user instruction. Intermediate-output attacks insert commands into Gmail email content or CSV file content. CSV placements include headers, early entries, final entries, and a file containing only the injected prompt. Memory experiments separately test residual effects of past successful attacks and direct fabrication of interaction/reasoning records. [pp. 9–10]

For Gmail intermediate-output testing, the paper describes twenty email templates combined with twenty target functions. It does not explicitly state how many unique trials, repetitions, or successfully executed combinations produced every Table 4 cell. Therefore the resulting denominator is not reconstructed as an established sample size. [p. 9]

## Metric and checking

**[A]** The metric is the percentage of tasks not completed. Without attack it is the baseline failure rate; under attack the authors call it attack success rate, or **ASR**, and use these terms interchangeably. They obtain completion judgments from agent self-reflection in the ReAct chain. Random sampling and human inspection are used to check that incorrect judgments occur minimally, but the sample size and disagreement rate are not reported. [§4.3, p. 6]

No train/validation/test split, participant sample, annotation protocol, random seed, repeated-run count, confidence interval, hypothesis test, p-value, runtime measurement, or resource-consumption measurement is supplied for the main comparisons. These are unavailable details, not evidence that such quantities would necessarily be relevant or that no internal settings existed.

# 8. Experiments / Analyses

| ID | Purpose and setup | Main evidence | Important boundary |
|---|---|---|---|
| X1 Attack-type comparison | Emulator, direct-input prompt injection; no attack versus loops versus irrelevant functions. | T1: 15.3%, 59.4%, 26.4%. | Irrelevant actions generated with GPT-4; ASR is task failure. |
| X2 Implemented-agent method/type comparison | Gmail and CSV, direct input; injections, perturbations, demonstrations. | T4: injection produces 75.0%–90.0%; other methods much lower. | Two implementations; handcrafted incorrect functions. |
| X3 Core-model/method comparison | Emulator infinite-loop attack across GPT-3.5-Turbo, GPT-4, Claude-2. | T2: injection 59.4%, 32.1%, 88.1%. | Compares agents with different cores, not agents versus standalone models. |
| X4 Adversarial-ratio analysis | Plot failure against attack text's share of the instruction; injection and GCG, two cores. | F3–F4. | No correlation coefficients or bin sample counts given. |
| X5 Toolkit/tool analysis | Group emulator results by toolkit count, toolkit identity, and tool count. | T3, F5–F7. | Overlapping toolkit groups and unequal representation complicate attribution. |
| X6 Intermediate-output attacks | Commands in email or CSV content. | T4: Gmail 20.0% loops, 60.0% incorrect functions; CSV 0.0%. | External text/file effects differ from direct-input effects. |
| X7 Memory analysis | Past attacks retained in history; fabricated memory records; misleading examples in memory. | T4 and p. 10: zero listed ASR; ten subsequent instructions complete normally. | Tasks often bypass memory; footnote checks basic recall. |
| X8 Advanced agent-chain attacks | Same-type Gmail network and different-type CSV-to-Gmail workflow. | T5: 30.0%/50.0% and 80.0%/75.0%. | Stronger attacker control of the upstream agent; network scale unspecified. |
| X9 Policy self-examination | LLM judges whether an instruction is harmful or violates policy. | T6: harmful attacks detected well; listed malfunction attacks 0.0%. | Detection metric, not end-to-end prevented failures. |
| X10 Malfunction self-examination | Modified judge prompt asks whether instruction deliberately causes malfunction. | T7: full-prompt loop 20.0%, GCG 30.0%; incorrect function 0.0%. | Better detection in some rows, still limited; benign false-positive results not quantified. |

A supplementary analysis within X2 tests misleading examples in the system message: **1/20 successful attacks**, as distinct from Table 4's ordinary demonstration rows. A supplementary analysis within X7 checks that memory can recall information available only there; this supports functioning recall but does not establish robustness for all memory-dependent workflows. [pp. 7, 10]

The manipulated variables include attack objective, method, entry surface, model, prompt ratio, and tool configuration. The common dependent measure in X1–X8 is task failure/ASR; X9–X10 measure anomaly detection. Controls include clean instructions and, for detection, inspection of benign instruction segments. No separate statistical testing procedure is reported.

# 9. Results

**R1 — Loops outperform irrelevant actions in the emulator [A].** Table 1 reports 59.4% failure for loops and 26.4% for incorrect functions, against 15.3% clean failure. **[C]** The loop increase is 59.4 − 15.3 = **44.1 percentage points**; the failure-rate ratio is 59.4 / 15.3 ≈ **3.88**. Incorrect functions increase failure by 26.4 − 15.3 = **11.1 percentage points**. These quantify observed workload failure, not the probability that a specific tool operation was malicious. [p. 7]

**R2 — Prompt injection is the strongest tested method [A].** Across Table 2's models, injection exceeds the corresponding baseline substantially. For GPT-4, **[C]** 32.1 − 9.1 = **23.0 percentage points**; for Claude-2, 88.1 − 10.5 = **77.6 percentage points**. GCG is weaker, while SCPN and VIPER are close to or sometimes below baseline. Results below baseline do not prove a protective effect without variability information. [p. 7]

**R3 — Core capability helps conditionally [A/D].** GPT-4 agents have lower baseline and injection failure than GPT-3.5-Turbo agents in this evaluation. Nonetheless, GPT-4 injection failure remains 32.1%. The authors interpret this as improved reasoning mitigating attacks. **[D]** Model choice is associated with different outcomes here; the experiments do not isolate which internal capability causes the differences or establish a ranking of all possible models. [pp. 7–8]

**R4 — Implemented agents show strong direct-input susceptibility [A].** Gmail's loop and incorrect-function injection rates are 90.0% and 75.0%; CSV's are 85.0% and 90.0%. Clean rates are 0.0% in the listed conditions. The incorrect-function ordering differs from the emulator, plausibly because the implemented targets are handcrafted. The paper presents that explanation as likely, not as a controlled ablation. [Tables 1 and 4; p. 7]

**R5 — Extra surfaces are unequal [A].** External-input injection produces 20.0% loop and 60.0% incorrect-function failure for Gmail, but 0.0% for CSV. Thus external content creates an actionable attack path in one tested implementation, while another remains robust under the tested placements. This is stronger evidence for conditional exposure than for universal agent susceptibility. [pp. 9–10, T4]

**R6 — Memory attacks are unsuccessful in the examined conditions [A].** Table 4 reports 0.0% for listed memory injection and demonstration rows. After prior successful attacks, ten normal instructions produce no observed residual failure. The authors suggest agents avoid memory when not needed; that condition limits extrapolation to tasks that necessarily retrieve and act on memory. [p. 10]

**R7 — Tool counts do not yield a simple increasing relationship [A].** Table 3 gives injection ASR of 60.0%, 60.0%, and 50.0% for one, two, and three toolkits. Figure 7 shows scattered rates across tool counts. Toolkit identity appears more informative in this workload; all five Twilio-using agents are reported successfully attacked. This is an association within overlapping configurations, not proof of a defect in Twilio itself. [pp. 8–9]

**R8 — Agent-to-agent transmission is demonstrated [A].** Same-type networks produce 30.0% loop and 50.0% incorrect-function ASR. Different-type CSV-to-Gmail chains produce 80.0% and 75.0%. **[D]** This demonstrates a path from an upstream agent to downstream malfunction under the evaluated controls. It does not measure exponential growth, widespread deployment impact, or a reproduction number for propagation. [pp. 10–11, T5]

**R9 — Simple inspection misses many malfunction attacks [A].** Policy inspection detects none of the listed loop, incorrect-function, or GCG attacks. Modified inspection detects 20.0% of complete loop prompts and 30.0% of complete GCG prompts, but 0.0% of incorrect-function prompts. Harmful-content recognition is therefore insufficient for these availability-oriented failures in this setup. [Tables 6–7]

# 10. Figure-by-Figure Interpretation

## Figure 1 — Agent architecture and attack locations [p. 2]

**[B]** This conceptual diagram places a core LLM inside a reasoning/planning framework. User instructions enter from above. External tools are at left, with a blue leftward tool-selection arrow and a rightward intermediate-output arrow. Agent memory is at right, with opposing fetch and record arrows. A red/orange box lists prompt injection, adversarial perturbation, and adversarial demonstration. Red dotted arrows associate attack-bearing content with instruction processing, tool return content, and memory.

There are no numerical axes or measured performance values. Tool-service logos illustrate external integrations rather than experimentally establishing vulnerabilities in each depicted service. The diagram supports the architecture and surface taxonomy; actual effectiveness comes from later experiments. The distinction between selecting an action and receiving external output is central to why agents can encounter attack text beyond their initial user prompt.

## Figure 2 — Downstream agent disruption [p. 4]

**[B]** An attacker icon sends an embedded attack to a blue agent. Dotted connections branch toward three colored downstream agent boxes, with small red attack symbols along the paths and an ellipsis indicating additional agents. The figure depicts indirect influence through communication. It does not specify a network topology, count of experimental agents, time scale, measured bandwidth, or propagation probability. The adjacent text supplies the proposed mechanism; Table 5 supplies the reported case-study outcomes.

## Figure 3 — Adversarial ratio with GPT-3.5-Turbo [p. 8]

Two light-blue bar-chart panels compare **(a) prompt injection** and **(b) GCG adversarial perturbation**. The x-axis is adversarial ratio, visibly spanning approximately 0.2–0.8; the y-axis is failure rate/ASR, spanning 0.0–1.0 on a linear scale. A plotted rate of 1.0 corresponds to 100%, but bars are not labeled with exact percentages. No confidence intervals, error bars, or sample-count labels are shown.

**[B, approximate]** Injection bars vary across ratios, with intermediate bins around one-half to two-thirds failure and a higher-ratio bar reaching near 1.0. GCG's lower-ratio bars are comparatively small, followed by larger bars at higher ratios, including a bar near 1.0. These are graphical estimates, not transcribed exact results. **[A]** The text concludes that injection has no strong ratio correlation, while larger GCG perturbation ratios show a stronger effect. **[D]** The high endpoint alone does not establish a general monotonic law; bin sizes and numerical correlation measures are missing.

## Figure 4 — Adversarial ratio with GPT-4 [p. 8]

The layout, axes, linear scales, and colors match Figure 3. Panel (a) shows injection, panel (b) GCG. **[B, approximate]** Injection bars around ratios 0.3–0.5 vary from roughly 0.2 to 0.6; GCG bars in the middle range are below roughly 0.4. Exact bin centers and values should not be reconstructed from the image as definitive numbers.

The text interprets the pattern as reduced overall attack effectiveness for the stronger core and a weaker ratio relationship for GCG. Neither plot contains uncertainty intervals or a fitted trend. Figure 4 illustrates heterogeneity within conditions rather than replacing Table 2's aggregate model comparison.

## Figure 5 — Toolkit-associated injection failure [p. 8]

This horizontal blue bar chart shows average infinite-loop prompt-injection success for cases using each named toolkit. The x-axis is failure rate/ASR from 0.0 to 1.0; the y-axis lists toolkit names. No error bars or exact bar annotations appear. Several upper bars reach 1.0, whereas several lower listed toolkits have no discernible positive bar. Intermediate toolkits show a broad range of rates.

**[A]** The adjacent discussion explicitly singles out Twilio: all five agents using it were successfully attacked. **[D]** A toolkit-associated rate is not a toolkit-isolated causal effect, because tasks and other available toolkits can differ. Figure 6 supplies representation counts but does not eliminate confounding or overlapping group membership. The figure's label list also requires caution relative to the prose's reported 36-toolkit scope; that issue is discussed in §14.

## Figure 6 — Toolkit representation [p. 9]

A horizontal purple bar chart shows the number of emulator agents using each listed toolkit. The x-axis is count, with ticks from 0 through 30. The y-axis repeats toolkit identities. **[B]** Representation is unequal: Terminal and Gmail have conspicuously longer bars than many other toolkits. **[B, approximate]** Their bars reach about 30 and about 25 respectively; these are visual estimates and are not treated as exact dataset counts. Twilio's count of five is reported in prose on the same page.

This plot qualifies Figure 5: toolkit rates arise from very different group sizes. It does not provide disjoint groups, per-task breakdowns, or statistical uncertainty. The authors use multiple agents per toolkit to argue that findings need not concern just one agent, but small groups can still produce unstable rate estimates.

## Figure 7 — Number of tools versus ASR [p. 9]

A light-blue scatter plot places number of tools on the x-axis, with visible ticks 1–22, and average failure rate/ASR on the y-axis, visibly around 0.3–1.0. Unlike the bar plots, its y-axis is truncated above zero. Points at similar or larger tool counts have differing failure rates; several are near 1.0, while other high-count conditions are lower.

The plot shows no regression line, correlation coefficient, confidence band, or per-point denominator. **[A]** The authors conclude that tool count is not strongly correlated with success, although some agents with many tools have high rates. **[D]** The visible scatter supports rejecting a simple monotonic interpretation; it does not establish that tool count is irrelevant under all workloads or designs.

# 11. Table-by-Table Interpretation

All table values below are **[A] author-reported** and cross-checked visually **[B]** on the supplied page images. They are percentages. No table provides confidence intervals, standard deviations, or significance markers.

## Table 1 — Emulator attack types [p. 7]

| Condition | Baseline | Infinite loop | Incorrect function |
|---|---:|---:|---:|
| Failure / ASR | 15.3% | 59.4% | 26.4% |

The comparison uses prompt injection for both attacks to make their deployment methods similar. The highest failure is infinite loop; the lowest is clean baseline. The table supports amplification of existing failure, with the caveat that incorrect commands are LLM-generated and task completion is self-assessed.

## Table 2 — Methods and core models [p. 7]

| Method | GPT-3.5-Turbo | GPT-4 | Claude-2 |
|---|---:|---:|---:|
| Baseline | 15.3% | 9.1% | 10.5% |
| GCG | 15.5% | 13.2% | 20.0% |
| SCPN | 14.2% | 9.3% | 10.2% |
| VIPER | 15.1% | 10.1% | 8.2% |
| Prompt injection | 59.4% | 32.1% | 88.1% |

Rows compare clean prompts and infinite-loop attack methods; columns identify agent cores. Injection is the highest row in each model column. GCG is the strongest perturbation method in each column, but its GPT-3.5-Turbo rate is just 0.2 percentage points above baseline. Some perturbation rates fall below clean failure. Without repeated-run variability, small differences should not be interpreted as reliable improvements or degradations.

## Table 3 — Toolkit count [p. 9]

| Number of toolkits | Baseline | Prompt injection | GCG |
|---|---:|---:|---:|
| 1 | 15.8% | 60.0% | 14.8% |
| 2 | 17.1% | 60.0% | 16.7% |
| 3 | 0.0% | 50.0% | 12.5% |
| Total | 15.3% | 59.4% | 15.5% |

The rows are toolkit-count groups, not individual toolkit identities. Two-toolkit agents have the highest baseline and GCG rates, but injection ties at 60.0% for one and two toolkits. The table contradicts any assertion that the two-toolkit injection rate is strictly highest. Group denominators are absent; the total is reported, not reconstructed as an unweighted average.

## Table 4 — Implemented-agent types, methods, and surfaces [p. 10]

| Attack / method | User Gmail | User CSV | External Gmail | External CSV | Memory Gmail | Memory CSV |
|---|---:|---:|---:|---:|---:|---:|
| No attack | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| Loop / injection | 90.0% | 85.0% | 20.0% | 0.0% | 0.0% | 0.0% |
| Loop / demonstration | 0.0% | 0.0% | — | — | 0.0% | 0.0% |
| Loop / GCG | 9.0% | 3.0% | — | — | — | — |
| Loop / VIPER | 0.0% | 0.0% | — | — | — | — |
| Loop / SCPN | 0.0% | 0.0% | — | — | — | — |
| Incorrect function / injection | 75.0% | 90.0% | 60.0% | 0.0% | 0.0% | 0.0% |
| Incorrect function / demonstration | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

A dash is preserved as an unavailable/not-reported combination, not converted to zero. The highest direct-input values are 90.0%, reached by Gmail loops and CSV incorrect functions. External Gmail incorrect functions outperform external Gmail loops. Every reported CSV external-input value is zero, even though direct-input injection strongly affects CSV. Memory rows are also zero. The table supports a distinction among control of instructions, control of task data, and control of retained history.

## Table 5 — Advanced scenarios [p. 10]

| Scenario | Infinite loop | Incorrect function |
|---|---:|---:|
| Same type | 30.0% | 50.0% |
| Different type | 80.0% | 75.0% |

Same type means interacting Gmail agents; different type means a CSV-to-Gmail chain. These are different workflows, not a controlled manipulation of agent heterogeneity alone. Different-type ASR is higher in both columns. Incorrect functions outperform loops in the same-type case, while loops are slightly higher in the different-type case. Trial denominators and network sizes are not shown.

## Table 6 — Policy-violation inspection [p. 11]

| Attack | Attack segment | Complete prompt |
|---|---:|---:|
| Direct harm / injection | 90.0% | 83.7% |
| Data stealing / injection | 100.0% | 100.0% |
| Infinite loop / injection | 0.0% | 0.0% |
| Incorrect function / injection | 0.0% | 0.0% |
| GCG / perturbation | 0.0% | 0.0% |
| VIPER / perturbation | N/A | 0.0% |
| SCPN / perturbation | N/A | 0.0% |

The metric is anomaly detection, so higher is better for defense, unlike attack ASR. Attack segment means adversarial content separated from the benign request; complete prompt includes both. N/A must remain distinct from failed detection. Data stealing is perfectly detected in this tested collection; malfunction-oriented attacks are not detected by this inspection criterion.

## Table 7 — Malfunction-oriented inspection [p. 12]

| Attack | Attack segment | Complete prompt |
|---|---:|---:|
| Direct harm / injection | 40.0% | 42.7% |
| Data stealing / injection | 78.1% | 69.3% |
| Infinite loop / injection | 0.0% | 20.0% |
| Incorrect function / injection | 0.0% | 0.0% |
| GCG / perturbation | 0.0% | 30.0% |
| VIPER / perturbation | N/A | 0.0% |
| SCPN / perturbation | N/A | 0.0% |

Changing the inspection question improves detection of complete loop and GCG prompts, but does not detect incorrect-function attacks. Direct-harm and data-stealing detection is lower than with policy inspection. **[D]** This indicates a criterion-dependent tradeoff in the reported results, not a demonstrated optimal combined defense. The paper says benign segments are checked for false positives but does not provide their numerical results in these tables.

# 12. Diagram / Architecture Interpretation

Figures 1 and 2 are already audited individually; this section connects their information flow to the method.

**[A/B] Single-agent workflow:** A request reaches the LLM/planning component; the agent selects a tool; the external tool produces an intermediate output; that output informs a later action; relevant history may be recorded or fetched. The workflow is iterative because tool observations can lead to additional tool choices. This gives attackers opportunities to affect not only the starting request but later evidence used in planning. [F1; §§2.1 and 3.4]

**[D] Boundary interpretation:** A malicious email is nominally task data. If its embedded wording controls the next action, retrieved content has influenced the command path. The Gmail external-input results provide an empirical instance of this risk, while CSV’s zero external-input results show that encountering adversarial text does not inevitably cause that promotion. [T4]

**[A/B] Multi-agent workflow:** An attacker-controlled upstream agent communicates attack-bearing information to another agent, which may execute repetitive or incorrect actions. Same-type experiments use Gmail interactions; different-type experiments use CSV-generated analysis passed to Gmail for reporting. The downstream material is autonomously generated, rather than manually edited by the attacker between the two agents. [F2; pp. 10–11]

**[D] Consequence interpretation:** Agent integration can couple a local reasoning error to a real action and couple one agent's output to another agent's behavior. The paper demonstrates these paths. It does not measure a production network cascade or establish that every repeated action has a particular monetary or bandwidth cost.

# 13. Equations and Mathematical Concepts

No numbered equation, loss function, theorem, lemma, proof, or pseudocode algorithm is present in the supplied work. It would be misleading to invent a mathematical optimization specification for the attacks. GCG is described verbally as optimization on an auxiliary white-box model; the paper does not provide its objective, update rule, or hyperparameters here.

Three quantitative concepts are necessary:

1. **Failure rate / ASR [A]:** The percentage of tasks the agent cannot complete. Without attack this is baseline failure; under attack the paper calls it ASR. **[C, explanatory formalization]** For a condition with N evaluated tasks and F judged failures, the natural expression is 100 × F/N percent. This formalizes the prose definition; it is not a printed paper equation. Exact F and N for each table cell are unavailable.
2. **Adversarial ratio [A]:** The attack prompt's share of the overall instruction prompt. The supplied material does not specify whether length is measured in characters, words, or tokens. A conceptual expression is attack-text length / complete-prompt length, provided both lengths use the same unit. That expression does not establish the omitted unit.
3. **Anomaly detection rate [A]:** Tables 6–7 quantify how often the inspection prompt recognizes attack prompts as anomalous. A higher rate is interpreted as better detection. This is distinct from task failure and does not directly measure the full protected agent's success.

**[C] Difference conventions:** Subtracting two percentages gives percentage points: 59.4% − 15.3% = 44.1 percentage points. Dividing rates gives a ratio: 59.4/15.3 ≈ 3.88. A relative increase, if desired, is (59.4 − 15.3)/15.3 × 100 ≈ 288.2%. These are three different descriptions of the same comparison and must not be interchanged.

# 14. Interpretation and Discussion

**[D] Answer to the user’s question:** The paper supports four mechanisms for increased agent exposure or consequences. First, tools and memory create additional entry points beyond a direct prompt. Second, tool use turns language-model decisions into executable actions. Third, autonomous planning can repeatedly follow a mistaken path until an iteration cap is reached. Fourth, communication allows one agent's output to influence another agent. The experiments substantiate selected manifestations of these mechanisms, especially direct injection, Gmail external-input injection, and CSV-to-Gmail propagation.

The distinction between **vulnerability** and **impact** is important. Page 1 says additional components introduce attack surfaces and that consequential actions can make compromise more damaging. These do not imply that every agent has a higher measured attack success rate than the same model used alone. A matched standalone baseline is not provided. Nor is the number of tools a reliable predictor in this workload. Memory and CSV external-input attacks yield negative findings.

The authors' toolkit-count hypothesis is not supported by a monotonic pattern. Their harmful-command-detection hypothesis is supported for policy inspection of the tested comparison prompts, but the modified malfunction inspector has lower detection of those harmful prompts. Their expectation that injection length matters less than overriding meaning is consistent with the reported plots, though no numeric correlation analysis is given.

## Cross-reference and consistency findings

- **Text–table discrepancy, toolkit tie:** Page 9 says two-toolkit agents have the highest failure rates in all three cases. Table 3's injection column ties one and two toolkits at 60.0%. The evidence supports 'joint highest' for injection, not uniquely highest.
- **Text–table reference discrepancy, defense:** Page 12 attributes perfect detection of data-stealing prompts to Table 7 while discussing the original inspection defense. Perfect 100.0% detection appears in Table 6; Table 7 reports 78.1% and 69.3%. Both tables are preserved rather than merged.
- **Terminology discrepancy, ratio analysis:** Page 8 starts a sentence about 'adversarial demonstrations' but proceeds to explain GCG and 'adversarial perturbation attacks.' Figures 3–4 label their second panels GCG perturbation. The likely interpretation is perturbations, but the wording discrepancy remains disclosed.
- **Potential toolkit inventory discrepancy:** Page 6 reports 36 toolkits. Figures 5–6 visibly list a broader-looking set of toolkit labels, including both Venmo and FacebookManager endpoints and numerous intervening categories. The figure-label inventory is not reconciled by the supplied text. The reported scope is retained as 36 without silently treating every plotted label as a separately verified member of that count.
- **Approximation in advanced results:** Page 11 describes both different-type outcomes as around 80%. Table 5 gives 80.0% and 75.0%. This is broad prose rounding, not an exact shared value.
- **Claim versus measurement, propagation:** The introduction suggests exponentially increasing multi-agent damage. Table 5 reports success rates for two scenarios, not scaling curves or exponential-growth measurements. That broader consequence remains an author motivation claim.
- **Extraction-sensitive example:** Page 5's VIPER character replacement gives a clear s-to-$ example but an incomplete a replacement. The missing glyph is not repaired from outside knowledge.

The paper's strongest supported conclusion is that disruption can be induced without an obviously dangerous command and that a harmfulness-focused inspector can miss it. A stronger conclusion that simple LLM inspection proves all LLM-based defenses inadequate would exceed the tested defense family.

# 15. Contributions and Novelty

The four explicit contribution bullets on p. 3 are represented as follows:

| ID | Contribution category | Authors' claim and evidence boundary |
|---|---|---|
| C1 | Conceptual/security | To their knowledge, the first attack targeting compromise of normal agent functioning. Novelty is an author claim, not independently verified here. |
| C2 | Methodological/empirical | Use malfunction attacks as a platform to identify susceptible agent properties and surfaces. Tables 1–4 and Figures 3–7 implement this analysis. |
| C3 | Systems/experimental | Present implemented and deployable multi-agent scenarios to demonstrate risks. Table 5 covers two workflows using Gmail and CSV agents. |
| C4 | Defensive evaluation | Show limited self-examination effectiveness. Tables 6–7 separate policy and malfunction inspection. |

The attack mechanisms reuse or modify existing injection, perturbation, and demonstration methods. The principal novelty is the malfunction-oriented objective and its evaluation, rather than a wholly new text-optimization algorithm. No new dataset release, mathematical theorem, general-purpose defense implementation, or independently validated benchmark standard is established by the supplied material.

**[D]** The study contributes a useful distinction between recognizing objectionable content and preserving correct autonomous behavior. That distinction is particularly relevant to web agents because external content may be ordinary-looking and the intended action sequence can be disrupted without an explicit request for theft or violence.

# 16. Limitations

## Authors' stated limitations

1. **Only two implemented agents [A].** Implementing real tool integrations is difficult; more case studies could give broader results. The emulator is used to extend coverage efficiently. [§8, p. 12]
2. **Limited agent categories [A].** The study focuses on real-world task-oriented agents. Other categories, including non-player characters in games, are not evaluated. The authors defer category effects to future work. [p. 12]
3. **Only three core model variants [A].** The models are selected for practical popularity and framework support. More models, including open-source models with greater control, could support broader or worst-case perturbation evaluation. [p. 13]
4. **Completion-metric uncertainty [A].** The authors acknowledge that self-reflection can make incorrect decisions because of hallucinations. They use random human inspection but leave alternative metrics outside the paper's scope. [§4.3, p. 6]
5. **Emulator limitation for advanced scenarios [A].** Simulated tool output cannot guarantee actual tool reactions. Advanced attacks are therefore evaluated only with implemented agents. [§5.5, p. 10]
6. **Scale qualifier in ethics discussion [A].** The paper says practical advanced attacks presently require large-scale deployment to pose significant threats. It does not report measured large-scale operational damage. [§9, p. 13]

## Additional evidence-based analyst observations

- **[D]** No matched standalone-LLM experimental comparison supports a universal relative-vulnerability claim.
- **[D]** ASR counts failed tasks, including natural failure, rather than necessarily confirming the intended malfunction in every failed trial.
- **[D]** Sample counts per result cell, repetitions, confidence intervals, and significance tests are absent, limiting comparison of small differences.
- **[D]** Toolkit groups have unequal and possibly overlapping membership; causal effects of toolkit identity are not isolated.
- **[D]** The failed memory attacks often concern tasks that can bypass memory, leaving mandatory retrieval workflows untested.
- **[D]** Model snapshots, inference settings, framework versions, full prompts, and GCG optimization parameters are insufficiently specified for exact reproduction from the paper alone.
- **[D]** Detection percentages do not establish protected end-to-end task success, latency, false-positive cost, or robust prevention under adaptive attack.
- **[D]** No measured runtime, billable cost, bandwidth consumption, or propagation scaling converts malfunction success into a quantified denial-of-service impact.

# 17. Threats to Validity

These methodological labels are **analyst interpretations**, not labels the authors necessarily use.

**Internal validity [D].** Clean baselines help separate ordinary instability from failures under attack. However, stochastic model behavior, unreported repetitions, and differing incorrect-function construction make exact causal comparisons uncertain. Handcrafted case-study targets and GPT-4-generated emulator targets differ in more than implementation realism. Toolkit identity is also mixed with task and configuration differences.

**Construct validity [D].** The main metric operationalizes attack success as task failure. This fits availability-oriented disruption, but task failure alone does not establish that the attacker’s exact requested behavior occurred. Likewise, anomaly detection is not identical to successful mitigation. The absence of harmful intent in a command does not by itself establish that the command is harmless in an operational context.

**Statistical conclusion validity [D].** Reported percentages have no uncertainty intervals or repeated-run variation. Large injection-versus-baseline gaps are descriptively striking, whereas near-baseline perturbation differences are difficult to interpret. Zero observed successes or failures do not establish zero underlying probability. Plot correlations are described qualitatively without coefficients or formal tests.

**External validity [D].** Emulator breadth does not replace real integration breadth. Two implemented agents and three model variants restrict generalization across browsers, enterprise workflows, memory systems, agent frameworks, and deployment controls. The article’s dated model configuration should be understood as the evaluated setup rather than assumed current behavior.

**Ecological validity [D].** Gmail API execution and Python CSV processing are more concrete than simulated tool calls, but the supplied text does not specify production workloads, independent users, security policies, account privileges, or real service-load effects. Multi-agent scenarios demonstrate feasible interactions without measuring a deployed network incident.

**Reproducibility [D].** The article supplies architecture, templates, model names, workloads at a high level, and implementation links. It omits enough runtime and prompt details that an exact independent replication cannot be specified solely from the supplied text. Linked code, datasets, and referenced papers were not inspected in this closed-document analysis.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Expand implemented agents beyond Gmail and CSV. [p. 12]
- Investigate whether agent category changes attack performance, including agents outside real-world task assistance. [p. 12]
- Evaluate more core models and open-source models offering greater control. [p. 13]
- Use controllable models to examine more severe or worst-case adversarial perturbations. [p. 13]
- Improve robustness and devise more effective safeguards before broader adoption. [§§9–10, p. 13]

## B. Additional open questions from this analysis

**[D]** How would the same model perform as a standalone assistant and as an agent under matched tasks and attacks? Which portion of the observed difference would arise from extra exposure, action autonomy, or evaluation definitions?

**[D]** How do attacks behave when memory is necessary for the task, rather than optional? Do different memory retrieval policies change persistence or susceptibility?

**[D]** Would toolkit-associated patterns persist after matching tasks, tool sets, and group sizes? How much uncertainty surrounds the apparent zero and 100% toolkit rates?

**[D]** How often do failed tasks actually exhibit the intended loop or irrelevant function? What would independent execution-log adjudication reveal compared with agent self-reflection?

**[D]** How much compute, money, time, or bandwidth do attacks consume before iteration limits stop them? How does propagation behave across larger networks and multiple interaction rounds?

**[D]** Can inspection be combined with action verification while maintaining normal task completion? The supplied paper does not evaluate such a combined system, so these remain questions rather than endorsed solutions.

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning within this paper |
|---|---|
| LLM | Large language model: the text-processing model at an agent's core. |
| Autonomous LLM agent | A system that uses an LLM to plan and act through tools with reduced need for further human input. |
| Core | The coordinating LLM that interprets requests and selects actions. |
| Planning | Structured reasoning used to choose and assess steps toward a task. |
| ReAct | The named reasoning-and-acting framework that uses observations to assess preceding actions. |
| Tool | An individual external function the agent can call. |
| Toolkit | A collection of related tools, such as functions exposed by an API. |
| API | Application programming interface: an interface for using external software functions. |
| Memory | Stored information or interaction history retrieved for ongoing tasks. |
| CSV | Comma-separated values: the file format analyzed by the second implemented agent. |
| Prompt injection | Adversarial commands embedded in input to redirect instruction following. |
| Intermediate output | Tool-returned information or retrieved file/email content processed between agent actions. |
| Adversarial perturbation | Input alteration or added disruptive text intended to impair the agent's behavior. |
| Adversarial demonstration | Misleading examples intended to teach an incorrect response within the current prompt. |
| In-context learning | Using examples included in the prompt to influence current behavior. |
| SCPN | Syntactically controlled paraphrase networks, used here through a pretrained paraphrasing model. |
| VIPER | A named character-perturbation method; the supplied paper does not expand the acronym. |
| GCG | A named optimization-based perturbation method; the supplied paper does not expand the acronym. |
| Black-box access | Interaction without access to target model internals or parameters. |
| White-box access | Access sufficient for model-based optimization, contrasted with the target's black-box setting. |
| Auxiliary model | A separate model used to construct transferable perturbations. |
| Infinite-loop attack | Repeated execution until the agent's allowed iteration limit; not established as literally unbounded. |
| Incorrect-function attack | Calling an irrelevant or wrong tool instead of the function needed for the legitimate task. |
| Malfunction amplification | Increasing existing reasoning/action failures rather than requiring explicitly forbidden actions. |
| ASR | Attack success rate; operationalized here as failed-task percentage under attack. |
| Baseline | The corresponding no-attack condition. |
| Adversarial ratio | Attack prompt length relative to the complete instruction; length unit unspecified. |
| Self-reflection | The agent's assessment of whether observations indicate task completion. |
| Self-examination | Asking an LLM to classify a prompt as harmful or malfunction-inducing before execution. |
| Anomaly detection rate | Percentage of attacks detected by an inspection prompt; higher is better for the tested defense. |
| Denial of service | Preventing useful service; used as inspiration for malfunction-oriented disruption. |
| Hallucination | Incorrect or fabricated model output. |
| NPC | Non-player character, an agent category mentioned as outside the evaluated scope. |
| Percentage point | The subtraction of two percentages, distinct from a relative percentage change. |

No further mathematical notation is defined or required in the supplied work. Acronym expansions not supplied by the paper have not been imported from external sources.

# 20. Key Numerical Results

The following table consolidates principal quantities; complete method and defense matrices remain in §11. Author-reported values in rendered tables were also visually cross-checked. Approximate graph estimates are intentionally excluded from this exact-number reference.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Emulator test cases | 144 | cases | Broad agent evaluation | Author-reported | p. 6, §4.1 |
| Emulator toolkit scope | 36 | toolkits | Reported scope; plotted-label reconciliation unresolved | Author-reported | p. 6, §4.1 |
| Emulator tools | >300 | tools | Reported scope | Author-reported | p. 6, §4.1 |
| Implemented agents | 2 | agents | Gmail and CSV | Author-reported | p. 6, §4.2 |
| Gmail tools | 5 | tools | API-backed implementation | Author-reported | p. 6 |
| Requested repetitions | 100 | actions | Loop injection template; not configured iteration cap | Author-reported | p. 6, §5.1 |
| Default clean failure | 15.3 | % | GPT-3.5-Turbo emulator | Author-reported | p. 7, T1–T2 |
| Default loop injection | 59.4 | % | Same default emulator | Author-reported | p. 7, T1–T2 |
| Default incorrect function | 26.4 | % | Emulator prompt injection | Author-reported | p. 7, T1 |
| Loop increase over baseline | 44.1 | percentage points | 59.4 − 15.3 | Analyst-derived | p. 7, T1 |
| Loop/baseline ratio | ≈3.88 | ratio | 59.4 / 15.3 | Analyst-derived | p. 7, T1 |
| GPT-4 clean failure | 9.1 | % | Emulator | Author-reported | p. 7, T2 |
| GPT-4 loop injection | 32.1 | % | Emulator | Author-reported | p. 7, T2 |
| GPT-4 injection increase | 23.0 | percentage points | 32.1 − 9.1 | Analyst-derived | p. 7, T2 |
| Claude-2 clean failure | 10.5 | % | Emulator | Author-reported | p. 7, T2 |
| Claude-2 loop injection | 88.1 | % | Emulator | Author-reported | p. 7, T2 |
| Claude-2 injection increase | 77.6 | percentage points | 88.1 − 10.5 | Analyst-derived | p. 7, T2 |
| System-message demonstration | 1/20 | successful attacks / cases | Separate demonstration placement | Author-reported | p. 7 |
| System-message success proportion | 5.0 | % | 1 / 20 × 100 | Analyst-derived | p. 7 |
| One/two/three-toolkit injection | 60.0 / 60.0 / 50.0 | % | Toolkit-count groups | Author-reported | p. 9, T3 |
| Twilio-using agents successfully attacked | 5 of 5 | agents | Infinite-loop injection | Author-reported | p. 9 |
| Gmail email templates | 20 | templates | Intermediate-output setup | Author-reported | p. 9 |
| Gmail target functions | 20 | functions | Combined with email templates; trial total unstated | Author-reported | p. 9 |
| Gmail direct loop / incorrect function | 90.0 / 75.0 | % | User-input injection | Author-reported | p. 10, T4 |
| CSV direct loop / incorrect function | 85.0 / 90.0 | % | User-input injection | Author-reported | p. 10, T4 |
| Gmail external loop / incorrect function | 20.0 / 60.0 | % | Email-content injection | Author-reported | p. 10, T4 |
| CSV external injection | 0.0 | % | Both malfunction types | Author-reported | p. 10, T4 |
| Listed memory injection | 0.0 | % | Both agents and types | Author-reported | p. 10, T4 |
| Post-attack normal instructions | 10 | instructions | No residual failure observed | Author-reported | p. 10 |
| Same-type loop / incorrect function | 30.0 / 50.0 | % | Gmail multi-agent scenario | Author-reported | p. 10, T5 |
| Different-type loop / incorrect function | 80.0 / 75.0 | % | CSV-to-Gmail scenario | Author-reported | p. 10, T5 |
| Policy inspection: direct harm | 90.0 / 83.7 | % detected | Attack segment / complete prompt | Author-reported | p. 11, T6 |
| Policy inspection: data stealing | 100.0 / 100.0 | % detected | Attack segment / complete prompt | Author-reported | p. 11, T6 |
| Policy inspection: loop / incorrect function | 0.0 / 0.0 | % detected | Both prompt scopes for both attacks | Author-reported | p. 11, T6 |
| Modified inspection: complete loop | 20.0 | % detected | Malfunction criterion | Author-reported | p. 12, T7 |
| Modified inspection: complete GCG | 30.0 | % detected | Malfunction criterion | Author-reported | p. 12, T7 |
| Modified inspection: incorrect function | 0.0 | % detected | Both prompt scopes | Author-reported | p. 12, T7 |

The earlier 'around 14%' task-success statement on p. 2 is a cited prior-work motivation claim, not a result of this study. It is not used as a baseline for the paper's measured attack effects.

# 21. Claim–Evidence Map

| Major claim | Evidence | Figure/Table/Experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Additional components create entry points and actions increase potential consequences. | Architectural description and introduction comparison. | F1; threat/surface taxonomy | pp. 1–5 | Author argument; no matched standalone experiment. |
| Malfunction attacks can markedly raise emulator failure. | 15.3% baseline versus 59.4% loops and 26.4% incorrect functions. | T1, X1 | p. 7 | Strong descriptive difference in this workload; self-assessed completion. |
| Prompt injection outperforms tested perturbations. | Injection is the highest method row across three cores. | T2, X3 | p. 7 | Bounded to tested methods and transfer setup. |
| GPT-4 mitigates but does not remove injection failure. | 32.1% versus its 9.1% baseline; lower than GPT-3.5-Turbo's injection result. | T2, F4, X3–X4 | pp. 7–8 | Capability explanation is interpretive; no internal causal isolation. |
| Direct input and external data have different effects. | Gmail external 20.0%/60.0%; CSV external 0.0%; direct-input rates much higher. | T4, X2/X6 | pp. 9–10 | Two agents with distinct task designs. |
| Tested memory attacks have no observed effect. | Zero listed memory ASR; ten normal follow-up instructions. | T4, X7 | p. 10 | Does not establish safety for mandatory memory retrieval. |
| More tools/toolkits do not guarantee higher ASR. | Nonmonotonic toolkit rows and scattered tool-count points. | T3, F7, X5 | p. 9 | No numerical correlation statistic; group sizes unstated. |
| Attack-bearing outputs can disrupt another agent. | Same- and different-type multi-agent success rates. | F2, T5, X8 | pp. 10–11 | Upstream control assumed; no measured large-network cascade. |
| Policy inspection misses tested malfunction attacks. | Zero detection for loops, incorrect functions, and GCG. | T6, X9 | p. 11 | Applies to this simple inspection prompt. |
| Malfunction inspection improves selected rows but remains limited. | Full-loop 20.0%, full-GCG 30.0%, incorrect-function 0.0%. | T7, X10 | p. 12 | Detection only; false-positive outcomes not tabulated. |
| Implementation breadth limits generalization. | Two real agents; three core model variants. | §8 | pp. 12–13 | Explicit author limitation. |
| Web-agent relevance is through exposure and consequence amplification. | Extra surfaces, executed actions, and agent communication. | F1–F2, T4–T5 | pp. 1–5, 9–11 | Analyst inference; not a direct empirical agent-versus-LLM ranking. |

# 22. Very Simple Explanation

An ordinary language model mainly gives you words. An agent uses those words to decide what to do next: read an email, run a function, analyze a file, or send a message. The paper argues that this creates more places where misleading text can enter and more ways an error can matter. The researchers do not directly test the same system as both a standalone chatbot and an agent, so they cannot give a general number for how much more vulnerable agents are.

The attacks here try to make an agent waste its effort or take the wrong next step. They do not need to say something obviously dangerous. Asking an agent to repeat an action, or to use an irrelevant function, can stop the legitimate job from being finished. In the simulated default setup, failed tasks rise from 15.3% without attack to 59.4% with the repeating-action injection.

The details matter. Both implemented agents are vulnerable when their direct instructions are manipulated. But malicious email content affects the Gmail agent more than malicious CSV content affects the CSV agent. The memory attacks tested here do not succeed. An agent that resists one kind of input can still pass information to a more susceptible downstream agent, as the CSV-to-Gmail experiment shows.

Finally, asking the model 'Is this harmful?' misses the tested malfunction attacks. Asking specifically about malfunction catches some, but still misses many. The lesson supported by this paper is that checking for scary or forbidden wording does not fully protect an autonomous workflow. Correctly completing the intended task is a separate security concern.

# Completeness Audit

The coverage denominator is the supplied document inventory, not the narrative's length. All fifteen pages were read through supplied extracted text; only the nine listed images were visually inspected. All numbered figures and tables visible in this version are represented. Where methods lack detail or prose conflicts with tables, the uncertainty is retained.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliations, arXiv marker | Yes; p. 1 image/text | Yes | Fully represented | No separate venue inferred. |
| Abstract | Yes; p. 1 image/text | Yes | Represented in compressed form | Central objective and findings integrated in §§1 and 9. |
| S1 Introduction and contribution overview | Yes; pp. 1–3, p. 3 text-only | Yes | Represented in compressed form | Motivation separated from empirical standalone comparison. |
| S2 / §2.1 LLM Agents | Yes; p. 3 text-only | Yes | Fully represented | Core, tools, planning, memory, ReAct. |
| §2.2 Red-Teaming | Yes; p. 3 text-only | Yes | Represented in compressed form | Prior-work characterization preserved. |
| §2.2 Robustness Analysis | Yes; p. 3 text-only | Yes | Represented in compressed form | Evasion analogy and adapted attacks. |
| S3 / §3.1 Goal and Access | Yes; p. 4 image/text | Yes | Fully represented | Black-box and expanded access distinguished. |
| §3.2 Basic Attack | Yes | Yes | Fully represented | Loops and incorrect functions. |
| §3.2 Advanced Attack | Yes | Yes | Fully represented | Indirect downstream influence and scale claim qualified. |
| §3.3 Prompt Injection | Yes | Yes | Fully represented | Templates and placement explained without treating them as instructions. |
| §3.3 Perturbation / SCPN / VIPER / GCG | Yes; pp. 4–5, p. 5 text-only | Yes | Fully represented with uncertainty | Missing replacement glyph and optimization details disclosed. |
| §3.3 Adversarial Demonstration | Yes; p. 5 text-only | Yes | Fully represented | Ordinary and system-message placements separated. |
| §3.4 Input Instructions | Yes; p. 5 text-only | Yes | Fully represented | Direct-input access condition. |
| §3.4 Intermediate Outputs | Yes | Yes | Fully represented | Email/API/file return content. |
| §3.4 Agent Memory | Yes | Yes | Fully represented | Persistence and direct manipulation separated. |
| S4 / §4.1 Emulator | Yes; pp. 5–6 text-only | Yes | Fully represented with missing details | Scope, models, rationale, simulation limits. |
| §4.2 Gmail and CSV case studies | Yes; p. 6 text-only | Yes | Fully represented | Implementation links not followed. |
| §4.3 Metric | Yes; p. 6 text-only | Yes | Fully represented | Self-reflection and human spot-check limitation. |
| S5 / §5.1 Attack Types | Yes; pp. 6–7 | Yes | Fully represented | X1 and X2. |
| §5.2 Attack Methods | Yes | Yes | Fully represented | Injection, perturbation, demonstrations. |
| §5.2 Core Model Variants | Yes | Yes | Fully represented | Three core models; no standalone baseline. |
| §5.2 Adversarial Ratio | Yes | Yes | Fully represented with uncertainty | Undefined length unit; wording inconsistency. |
| §5.3 Toolkit count | Yes | Yes | Fully represented | H1 and Table 3 tie disclosed. |
| §5.3 Toolkit identity | Yes | Yes | Represented in compressed form | All categories visible; exact unlabeled bar values not reconstructed. |
| §5.3 Individual tool count | Yes | Yes | Fully represented | Scatter and missing correlation statistic. |
| §5.4 Intermediate Outputs | Yes | Yes | Fully represented | Placement and agent differences. |
| §5.4 Memory | Yes | Yes | Fully represented | Zero findings, ten instructions, recall footnote. |
| §5.5 Same-type agents | Yes | Yes | Fully represented | Gmail interactions, Table 5. |
| §5.5 Various-type agents | Yes | Yes | Fully represented | CSV-to-Gmail, autonomous output. |
| S6 / §6.1 Self Examination | Yes | Yes | Fully represented | Policy and malfunction criteria. |
| §6.2 Defense Comparison | Yes | Yes | Fully represented with uncertainty | Table-reference discrepancy and absent false-positive numbers. |
| S7 Related Work | Yes; p. 12 image/text | Yes | Represented in compressed form | Categories and positioning; outside sources not read. |
| S8 Implemented Agents limitation | Yes | Yes | Fully represented | Only two implementations. |
| S8 Categorization limitation | Yes | Yes | Fully represented | Other categories deferred. |
| S8 Models limitation | Yes; p. 13 text-only | Yes | Fully represented | Three cores; open-source future work. |
| S9 Ethics Discussion | Yes; p. 13 text-only | Yes | Represented in compressed form | Evaluation intent and scale qualifier preserved. |
| S10 Conclusion | Yes; p. 13 text-only | Yes | Represented in compressed form | Restatement integrated with supported findings. |
| Explicit formal research questions | Assessed | Yes | Not present | Informal objectives O1–O4 distinguished. |
| H1 toolkit-count hypothesis | Yes | Yes | Fully represented | No monotonic support. |
| H2 harmful-command detection hypothesis | Yes | Yes | Fully represented | Criterion- and prompt-dependent support. |
| X1–X10 experiments/analyses | Yes | Yes | Fully represented | Separate conditions in §8. |
| F1 architecture diagram | Visually | Yes | Fully represented | Arrows and attack locations explained. |
| F2 propagation diagram | Visually | Yes | Fully represented | Schematic scale not treated as measurement. |
| F3a/F3b ratio panels | Visually | Yes | Fully represented with uncertainty | Approximate bars, no exact reconstruction. |
| F4a/F4b ratio panels | Visually | Yes | Fully represented with uncertainty | Approximate bars, no uncertainty intervals. |
| F5 toolkit rates | Visually | Yes | Represented in compressed form | Trends and explicit Twilio result; per-bar estimates omitted. |
| F6 toolkit counts | Visually | Yes | Represented in compressed form | Unequal representation; exact unlabeled counts unavailable. |
| F7 tool-count scatter | Visually | Yes | Fully represented | Truncated y-axis and qualitative trend. |
| T1–T7 | Visually and text | Yes | Fully represented | Numerical cells preserved in §11. |
| Prompt templates | Yes | Yes | Represented in compressed form | Operational meaning preserved; not every template re-quoted. |
| Major equations/theorems | Assessed | Yes | Not present | Explanatory formulas explicitly analyst-derived. |
| Numbered algorithms/pseudocode | Assessed | Yes | Not present | Procedures reconstructed from prose only. |
| C1–C4 contributions | Yes | Yes | Fully represented | Novelty remains author-reported. |
| Substantive footnote 4 | Yes; p. 10 image/text | Yes | Fully represented | Memory recall functioning check. |
| Footnotes 1–3 / implementation links | Text inspected | Yes | Represented in compressed form | Linked artifacts not inspected. |
| References [1]–[51] | Text inspected, pp. 13–15 | Yes | Represented in compressed form | Bibliographic entries not reproduced individually or validated. |
| Decorative logos, attacker icons, repeated headers | Visually | Accounted for | Inspected but deliberately omitted as non-substantive | No performance conclusions inferred from decoration. |
| Appendices | Assessed | Accounted for | Not present in supplied material | No appendix claimed reviewed. |
| Supplementary material | Assessed | Accounted for | Not supplied | No supplementary review claimed. |

## Missing or Inaccessible Material

No numbered page in the supplied text sequence is missing. Visual rendering is absent for pages 3, 5, 6, 13, 14, and 15, so layout and any details excluded by extraction on those pages cannot be visually verified. The underlying PDF file, linked code, external references, and any unsupplied artifacts were not opened. No appendices or supplementary files are provided. Exact per-cell denominators, model snapshots, runtime settings, hardware, iteration caps, complete prompts, optimization settings, and statistical uncertainty are not supplied sufficiently for reconstruction.

## Uncertain Interpretations

The VIPER replacement glyph is incomplete. Adversarial-ratio length units are undefined. Plot values are unlabeled and only approximate at the supplied image scale. The toolkit label inventory is not reconciled with the prose’s 36-toolkit count. Page 9's unique-highest wording conflicts with Table 3's injection tie. Page 12's reference to perfect detection in Table 7 conflicts with that table's values and instead matches Table 6. The ratio discussion apparently switches 'demonstrations' and 'perturbations.' These points are not silently repaired.

## Deliberately Compressed Material

Repeated denial-of-service motivation, repeated statements about authorization checks, repeated conclusion language, bibliographic entries, tool-service logos, and multiple illustrative attack examples are compressed. Figure 5–6 category-by-category unlabeled values are not estimated exhaustively: their purpose, axes, patterns, representation issue, and explicit Twilio example are preserved. Attack and inspection templates are explained without duplicating all wording. This compression does not omit any numbered figure, table, main experiment, contribution, or stated limitation identified in the inventory.

## Potential Omissions

No identified substantive inventory object is left wholly unrepresented. However, inaccessible visual details on text-only pages and unavailable linked artifacts cannot be audited. Missing experimental configuration and unresolved consistency issues prevent calling the analysis a fully reproducible account or claiming that the study conclusively answers a universal agent-versus-standalone comparison. Coverage is comprehensive for the supplied evidence at the disclosed level of compression, with those limits retained.
