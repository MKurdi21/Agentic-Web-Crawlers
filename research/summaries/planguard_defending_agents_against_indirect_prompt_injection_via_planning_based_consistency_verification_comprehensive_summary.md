# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and six supplied page images. The paper is treated as evidence, including when it contains example malicious instructions. No tools, browsing, external references, repository inspection, or independent experimental verification were used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pages 1–7. |
| Page range and count | Seven text pages; six rendered images covering pages 1–6. |
| Apparent completeness | The available sequence contains the title, abstract, Sections I–VII, acknowledgements, and references [1]–[22]. No obvious interrupted main-text passage is visible. This establishes coverage of the supplied sequence, not independent proof that no other artifact exists. |
| Visual inspection | Pages 1–6 were directly inspected as supplied images. Page 7 was inspected through supplied text only. |
| Figures | Figure 1 on page 2 and Figure 2 on page 5 are visually available. Figure 2 is small; the important results are also explicitly printed in nearby prose. |
| Tables | No numbered substantive tables occur in the supplied work. Algorithm 1 is a pseudocode block, not an experimental table. |
| Equations | Equations (1)–(7) are available in both text and rendered pages. Their principal notation is readable. They formalize the system rather than provide a security proof. |
| Appendices | None present in the supplied sequence. |
| Supplementary material | No supplementary files supplied; no explicit supplementary-file reference identified in the supplied paper. |
| Other referenced artifacts | The source-code repository and InjecAgent benchmark are referenced but not supplied or inspected. Cited papers were not inspected. |
| OCR | Not used. Supplied native/extracted text and direct visual reading were sufficient for substantive analysis. |
| Extraction limitations | Multi-column ordering and mathematical typography require care. Figure 1 contains labels absent from the extracted text; these are recovered by visual inspection. Small plot typography limits confident transcription of every tick and annotation. |
| Page 7 limitation | Bibliographic entries [17]–[22] are text-only coverage; no claim is made to have visually inspected that page. |

Evidence labels used below are **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No **[E] External information** is introduced. Confidence describes how securely a statement follows from the supplied evidence, rather than certifying the real-world truth of every author assertion. Page numbers always mean physical PDF pages.

## Inventory established before synthesis

| ID | Supplied object | Location |
|---|---|---|
| META | Title, two authors, affiliations, arXiv identifier/version/date | p. 1 |
| ABS | Abstract and four index terms | p. 1 |
| S1 | I. Introduction | pp. 1–2 |
| C1–C3 | Three explicit contribution bullets | p. 2 |
| S2 | II. Related Work: classifiers, perplexity, instruction tuning, execution monitoring | p. 2 |
| S3 | III. Preliminaries and Threat Model | pp. 2–3 |
| S3A1 | Scope: Actionable IPI | p. 2 |
| S3A2 | Agent Modeling | p. 3 |
| S3B1 | Attacker Capabilities | p. 3 |
| S3B2 | Attack Goals: Type I and Type II | p. 3 |
| S4 | IV. Methodology | pp. 3–4 |
| S4A1 | Overview: architecture | p. 3 |
| S4A2 | Overview: four-step workflow | p. 3 |
| S4B | The Isolated Planner | p. 4 |
| S4C1 | Stage I: Deterministic Constraint Matching | p. 4 |
| S4C2 | Stage II: Tool Intent Verification | p. 4 |
| ALG1 | Algorithm 1: Hierarchical Verification Process | p. 4 |
| E1–E5 | Agent, effective instructions, attack definitions, success condition | p. 3 |
| E6–E7 | Reference-set generation and intent-verifier mapping | p. 4 |
| F1 | Figure 1: architecture and injected product-information example | p. 2 |
| S5 | V. Experiments | pp. 4–5 |
| S5A1–S5A4 | Dataset/scenarios, backbone, baselines, evaluation metrics | pp. 4–5 |
| X1 | Direct Harm comparison across three system variants | p. 5, Fig. 2 left |
| X2 | Data Stealing comparison across three system variants | p. 5, Fig. 2 right |
| X3 | Stage-II ablation interpretation through FPR comparison | p. 5 |
| S5B1–S5B3 | Baseline performance, zero-ASR claim, FPR reduction | p. 5 |
| S5C1–S5C2 | Failure and success mechanism discussion | p. 5 |
| F2 | Figure 2: two-panel ASR/FPR comparison | p. 5 |
| S6 | VI. Discussion | pp. 5–6 |
| S6A | Performance and Cost Analysis | p. 5 |
| S6B | Robustness Against Adaptive Attacks | p. 6 |
| L1 | Added inference/token cost | p. 5 |
| L2 | Context-dependent argument hijacking | p. 6 |
| FW1–FW2 | Smaller verifier/planner models; rule-based information extraction | pp. 5–6 |
| S7 | VII. Conclusion | p. 6 |
| ACK | Acknowledgements and corresponding-author note | pp. 1, 6 |
| REF | References [1]–[22] | pp. 6–7 |

There are no explicitly numbered research questions, hypotheses, theorems, lemmas, propositions, appendices, or experimental tables. The experiment register distinguishes DH, DS, and the Stage-II ablation, while recognizing that they belong to one benchmark evaluation rather than three independent studies.

# 1. Plain-language orientation

**[A]** PlanGuard addresses a problem that arises when a language-model agent can both read outside information and perform actions through tools. An attacker can place instructions inside material the agent retrieves, such as a webpage or email. The agent may then follow those instructions even though the real user never authorized them. The paper calls this **Indirect Prompt Injection (IPI)**. Its particular concern is an injected instruction causing a tool execution, such as sending data or transferring funds, rather than merely producing an undesirable sentence. Sources: p. 1, abstract and Introduction; pp. 2–3, §III.

The proposed solution separates planning from potentially contaminated execution. A protected planner receives the user's instruction and tool definitions, but does not receive retrieved external content. It generates a reference set of permitted tool actions. When the ordinary agent proposes a tool call, PlanGuard checks it before execution. Exact matches pass; calls to unapproved tools are blocked; calls using an approved tool with different arguments receive an additional language-model intent check. Sources: pp. 3–4, §IV and Algorithm 1.

**[A]** On the InjecAgent benchmark, both the strict first-stage version and full PlanGuard reportedly achieve 0.0% Attack Success Rate (ASR) in Direct Harm and Data Stealing scenarios. Adding the second stage reduces False Positive Rate (FPR), meaning fewer benign actions are incorrectly rejected: from 27.00% to 0.97% for Direct Harm, and from 38.01% to 3.28% for Data Stealing. These findings use DeepSeek-V3.2 and an intentionally compliance-inducing system prompt for the victim agent. They are not results from an unchanged ordinary agent deployment. Sources: pp. 4–5, §V.

**[D] Research relevance:** The paper helps explain how web-connected agents acquire an additional attacker-controlled input route and how tool access turns instruction confusion into consequential action. It does not directly compare a standalone language model with a web agent. Its strongest contribution to the user's research question is therefore a mechanism-level account of exposure and consequences, accompanied by a defense evaluation under specified conditions—not a measured agent-versus-standalone vulnerability gap.

# 2. Document roadmap

The title is **PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification**. The authors are Guangyu Gong and Zizhuang Deng, both affiliated with the School of Cyber Science and Technology at Shandong University; Deng also lists the Suzhou Research Institute of Shandong University. The supplied first page identifies **arXiv:2604.10134v1 [cs.CR], 11 Apr 2026**. No publication venue for this paper is supplied. This is a cybersecurity and AI-agent systems paper with an algorithmic defense and an empirical benchmark evaluation.

Section I establishes the problem of context mixing and introduces the defense. Section II organizes prior defenses into four categories. Section III narrows the target to actionable injection, defines the agent and attacker, and distinguishes unauthorized tools from malicious arguments. Section IV describes the isolated planner and two-stage verifier, with seven equations distributed across Sections III–IV and one algorithm. Section V gives the benchmark setup, results, and mechanism interpretation. Section VI discusses overhead, adaptive attacks, and an acknowledged limitation. Section VII restates the main conclusions. Acknowledgements and 22 references follow.

Figure 1 is the architecture overview; Figure 2 is the only quantitative results figure. There is no detailed experimental appendix, prompt appendix, case-level results table, or supplied software artifact. The references are evidence of what the authors cite, not evidence that this analysis reviewed those referenced works.

# 3. Background and context

**Large Language Model (LLM):** In this paper, the language-based decision-making component used by the agent. **Agent:** A system that can generate a sequence of tool calls rather than only conversational output. **Tool:** An external function or interface used to act on the world; each call has a tool name and arguments. **Application Programming Interface (API):** The external interface mentioned in the Introduction through which such actions can occur. These meanings are drawn from pp. 1 and 3 rather than supplemented with an external taxonomy.

**Indirect Prompt Injection:** An adversary places a malicious instruction in retrieved content rather than directly changing the user's trusted request. **Context mixing:** The authors' explanation that trusted instructions and untrusted external data coexist in a context window, allowing the model to treat malicious data as instructions. **Actionable IPI:** The subset that triggers unauthorized tool execution. These definitions matter because a toxic answer and an unauthorized funds transfer are different evaluated outcomes; the paper restricts itself to the latter class.

**Context isolation / instruction-data decoupling:** Keeping the planner's input away from retrieved content. **Reference Action Set:** The planner's proposed allowable action tuples for the current request. **Hard constraints:** Exact matching and tool-membership checks applied before any intent model is consulted. **Intent verification:** A model judgment about whether a changed parameter is consistent with the user's intent.

**Stochastic variation:** The paper uses this term to describe benign differences between planner and agent outputs. Its example is the date strings `last_week` and `lastweek`. The authors treat them as functionally equivalent. **[D]** That example explains the intended role of semantic tolerance, but the paper does not give a tool-specific schema establishing that both strings are valid for a particular deployed tool.

**Direct Harm (DH)** covers damaging or high-stakes actions. **Data Stealing (DS)** covers unauthorized information extraction or transmission. **Attack Success Rate (ASR)** is the proportion of adversarial inputs inducing the target malicious behavior. **False Positive Rate (FPR)** measures false alarms in benign scenarios. Lower values are preferred for both, but they address different things: attack prevention and unnecessary rejection, respectively.

# 4. Research problem and gap

**Existing problem [A]:** External information can carry an attacker instruction that changes an agent's control flow. The authors identify emails, webpages, and retrieved documents as potential carriers, and identify unauthorized transactions and data stealing as consequences. The paper attributes the underlying failure to context mixing. Source: p. 1, §I.

**Shortcomings of previous approaches, according to the authors [A]:** Classifier-based filters can generalize poorly to new or adaptive attacks. Perplexity-based filters can flag benign complex content and still have inadequate efficacy. Instruction tuning requires computational effort and can be difficult to interpret. Execution guardrails can be rigid, while a contaminated model's own intent analysis may be manipulated along with its reasoning. Sources: pp. 1–2, §§I–II. These are the paper's positioning claims; this analysis has not independently assessed the cited literature.

**Research gap [A]:** The authors argue that defenses need an architectural boundary protecting the source of action authorization, rather than relying only on detecting dangerous input or changing the victim model's behavior. Their proposed reference planner is independent of retrieved content, and execution monitoring compares actual proposed actions against this clean reference.

**Motivation [A]:** Unauthorized tool execution can connect digital instructions to damaging digital or physical outcomes. The authors therefore regard it as higher risk than textual deviation. Source: p. 2, §III-A1. This is their scope rationale, not a comparative harm measurement.

**Scope [A]:** The paper studies malicious actions induced through external context when the original user instruction remains trusted. It does not claim to solve every attack on an agent, every unsafe user request, or every harmful generated answer. **[D]** Its method is especially straightforward when the user instruction already contains enough detail to authorize both the tool and its arguments; the acknowledged context-dependent-argument limitation marks an important boundary.

# 5. Research questions / objectives / hypotheses

**Explicit research questions:** None are formally stated as questions in the supplied paper. The user's question, “Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,” is an analysis lens supplied outside the paper and must not be attributed to the authors.

**Explicit objectives [A]:** The methodology aims to defend against Type I unauthorized tool invocation and Type II intent deviation. The introduction and contributions also aim to preserve usability by distinguishing benign parameter variation from malicious changes, and to evaluate the proposed defense on InjecAgent. Sources: pp. 1–3.

**Hypotheses:** No formally named hypotheses or hypothesis tests are supplied. **[D]** The method implies the expectation that a clean reference plan constrains malicious tool calls and that a semantic verifier lowers unnecessary blocking. These are useful descriptions of the design expectations, but they are not author-labeled statistical hypotheses.

**Relation to the research lens [D]:** The evidence supports asking how retrieved attacker content enters the action-selection process, what tools make that exposure consequential, and how separating planning changes the attack path. It does not establish how much more vulnerable a web agent is than a standalone model, because no such comparison group appears in the experiment.

# 6. Assumptions / threat model

The protected asset is faithful execution of the user's intended tool actions. **[A]** The user instruction `I` is the absolute root of trust and reflects the user's true intent. External context `C`, including webpages, is untrusted. The agent can invoke a tool set `T`. The attacker cannot modify `I`; instead, the attacker injects payload `p_adv` into `C`. Direct jailbreaking through the user instruction is explicitly distinguished from this threat model. Source: p. 3, §III.

Two attack goals are defined. **Type I / function hijacking:** The agent calls a tool unrelated to the user instruction. The paper's example is a request to summarize an email leading to `SendEmail()`. **Type II / argument hijacking:** The agent calls the appropriate tool but substitutes malicious parameters. The example is a request to delete a temporary folder leading to `DeleteFile("/system/root")`. These are illustrative author examples, not separately reported benchmark outcomes.

The planner receives `I` and tool definitions `T`, while retrieved external context is excluded. The verifier receives the user instruction, reference set, proposed action, and agent reasoning. **[D]** This creates different trust positions: the planner's reference has no direct retrieved-content input, but the proposed action and its accompanying reasoning originate from the potentially compromised agent. The latter are evaluated, not independently established as trustworthy.

**[A]** Section VI-B considers a white-box attacker who knows the architecture and might place adversarial prompts in tool parameters to deceive Stage II. The authors argue this is difficult because the victim must generate a suitably embedded payload and structured tool schemas may reject it. They do not provide a separate adaptive-attack experiment or a measured success rate for that scenario.

**Important boundary [A]:** If the instruction is “Pay the bill in the email,” the planner can identify the payment action but lacks retrieved information needed to establish correct argument values. The paper explicitly acknowledges this information asymmetry. **[D]** Thus, isolation protects the reference from direct contamination while also withholding facts needed for some legitimate contextual decisions. The paper does not describe a completed solution to that trade-off.

# 7. Methodology

## 7.1 Study design and architecture

**[A]** PlanGuard is described as training-free: the proposed defense does not require training a replacement victim model in the reported method. It adds planning and verification around an agent's attempted tool execution. The isolated planner `P` creates a set `S_ref` of action tuples based on the original instruction and tool definitions. A hierarchical verifier decides whether each captured action can execute. Sources: pp. 1, 3–4.

The workflow has four steps: generate the reference set; capture each proposed tool name, arguments, and reasoning; apply hierarchical verification; enforce pass or block. It monitors proposed behavior rather than only inspecting retrieved text. No replanning policy, reference-update protocol, blocked-action recovery procedure, or full deployment interface is specified in the supplied description.

## 7.2 Stage I: deterministic checks

For a proposed action `a_act = (t_act, v_act)`, exact membership in `S_ref` yields an immediate pass. If the tool name does not occur in any reference action, the call is immediately blocked as Type I. If the tool name is permitted but its arguments do not match a corresponding reference tuple, the action is forwarded to Stage II. Source: p. 4, §IV-C1.

The first stage therefore distinguishes three outcomes, not merely safe versus unsafe. Its computational rule is clear at the conceptual level: exact action match, tool exclusion, or argument-review referral. The paper calls the comparison exact string matching, but does not specify canonicalization, argument ordering, serialization, or normalization rules.

## 7.3 Stage II: model-based intent checking

The verifier model evaluates `M_verify(I, S_ref, a_act, r_act)` and returns a Boolean decision. A true result permits the action; false blocks it. Its stated purpose is to allow benign formatting changes while rejecting malicious argument shifts. Source: p. 4, §IV-C2 and Eq. (7).

**[D]** Stage II is a semantic decision boundary, not an exact equality test. Calling the entire full system deterministic is therefore stronger than describing Stage I alone as deterministic. A Boolean output does not establish that the language model producing it is infallible or deterministic across executions. The paper supplies neither the verifier's full prompt nor a formal correctness proof.

## 7.4 Algorithm 1

Algorithm 1 takes `I`, `S_ref`, `a_act`, and `r_act`; extracts tool and parameters; passes an exact action match; blocks a non-reference tool; otherwise calls the intent verifier and returns pass or block. The branch order agrees with the prose. Parameter extraction appears explicitly, but schema validation does not appear as an algorithm step even though it is discussed later as a hurdle for adaptive attacks. Source: pp. 4 and 6.

## 7.5 Dataset and models

The InjecAgent dataset is reported to contain **1,054 test cases**, **17 user tools**, and **62 attacker tools**. The paper evaluates DH and DS scenarios. DeepSeek-V3.2 is the backbone for both the victim and PlanGuard components. No per-subset counts, attack-category counts, selection log, filtering protocol, or benign-case denominator is provided. Source: p. 4, §V-A.

The victim's system prompt is modified with a compliance-inducing directive requiring it to execute a command in a tool return. The authors explain that this partially lifts intrinsic safety restrictions so that those restrictions do not mask the defense's contribution. **[D]** This is an experimental control intended to increase exposure to injection; it also limits direct interpretation as ordinary deployment behavior.

## 7.6 Baselines, metrics, and missing configuration

The comparisons are: Vanilla Agent under the compliance-inducing prompt; Stage-I Only, retaining the planner and hard matching but removing the intent verifier; full PlanGuard with both stages. No implemented classifier, perplexity, tuning, or other published-defense baseline is evaluated in the supplied results.

ASR and FPR are the reported metrics. Their exact sample denominators and aggregation procedures are not supplied. Hardware, operating environment, libraries, API configuration, temperature, random seeds, repetitions, confidence intervals, significance tests, exact prompts beyond the quoted victim directive, latency measurements, and monetary costs are not reported. No train/validation/test split for a newly trained PlanGuard model is given; the method is presented as training-free, and the benchmark cases are described as test cases.

# 8. Experiments / analyses

## X1 — Direct Harm benchmark comparison

**Purpose [A]:** Evaluate prevention of damaging or high-stakes injected actions and benign-action rejection. **Setup:** InjecAgent DH subset; DeepSeek-V3.2; compliance-inducing victim prompt; Vanilla, Stage-I Only, and full PlanGuard. **Manipulated condition [D]:** Defense configuration. **Outcomes:** ASR and FPR. **Source:** p. 5, §V-B and Figure 2 left.

Vanilla ASR is **56.90%** in prose, shown as **56.9%** in the plot. Both defense versions have **0.0% ASR** according to the prose. Stage-I Only FPR is **27.00%**, while full PlanGuard FPR is **0.97%**. The authors attribute the lower baseline vulnerability relative to DS to heightened safety sensitivity around high-stakes tools. No individual-tool breakdown or intervention isolates that explanation.

**Caveats [D]:** DH sample counts and benign-case counts are absent. There are no error bars or reported repeated runs. The evidence establishes a reported benchmark outcome under this setup, not universal protection for every damaging action.

## X2 — Data Stealing benchmark comparison

**Purpose [A]:** Evaluate unauthorized information extraction/transmission attacks under the same defense conditions. **Data:** InjecAgent DS subset, with no separately reported count. **Source:** p. 5, §V-B and Figure 2 right.

Vanilla ASR is **88.67%**. Stage-I Only and full PlanGuard each reportedly achieve **0.0% ASR**. Stage-I Only FPR is **38.01%**, and full PlanGuard FPR is **3.28%**. The authors explain the higher vanilla susceptibility by describing DS attack tools as mostly query-based and perceived as having limited direct harm. The DS definition, however, concerns unauthorized data exfiltration. These descriptions address the attack category and the authors' interpretation of involved tools, respectively; no full attack-chain inventory is supplied to reconcile them at case level.

**Caveats [D]:** The explanation for the DH–DS difference is interpretive rather than separately tested. The DS results do not prove a general property of all data-stealing attacks, tools, or models.

## X3 — Stage-II ablation and utility interpretation

The ablation removes semantic intent verification while retaining the clean planner and strict matching. Since both variants already report zero ASR, the observed benefit of Stage II in these results is reduced false positives rather than an additional measured ASR reduction. Sources: p. 5, §V-B2–B3.

**[C] Analyst-derived:** DH FPR decreases by `27.00 − 0.97 = 26.03` percentage points. DS FPR decreases by `38.01 − 3.28 = 34.73` percentage points. These are absolute rate differences, not percentages of all tasks completed. Relative FPR reductions are approximately `26.03 / 27.00 × 100 = 96.41%` and `34.73 / 38.01 × 100 = 91.37%`, respectively. These derived percentages describe fewer false positives relative to the strict variant; they do not measure general agent utility.

## X4 — Qualitative reliability and adaptive-attack discussion

Section V-C interprets vanilla failure through context mixing and defense success through planner isolation plus semantic tolerance. Section VI-B argues that adaptive verifier attacks face generation and schema obstacles. These are qualitative mechanism analyses, not separately documented experiments with attack budgets, sample counts, success rates, or controls. Treating them as additional empirical validation would overstate the supplied evidence.

# 9. Results

| Condition | Vanilla ASR | Stage-I Only ASR | Full PlanGuard ASR | Stage-I Only FPR | Full PlanGuard FPR |
|---|---:|---:|---:|---:|---:|
| Direct Harm | 56.90% | 0.0% | 0.0% | 27.00% | 0.97% |
| Data Stealing | 88.67% | 0.0% | 0.0% | 38.01% | 3.28% |

All entries are **[A] author-reported**, p. 5, §V-B, with Figure 2 providing the visual comparison. A vanilla FPR value is not supplied and is not invented here. The shared experimental condition is the DeepSeek-V3.2 setup with a compliance-inducing victim prompt described on p. 4.

**[C] Analyst-derived ASR differences:** Relative to Vanilla, reported ASR decreases by **56.90 percentage points** for DH and **88.67 percentage points** for DS. These are comparisons against two different subset baselines. Neither should be replaced by the abstract's overall baseline number when describing a particular subset.

The abstract reports an ASR reduction from **72.8% to 0%** and an FPR of **1.49%**. The main results provide the subset values above but do not state how the abstract's aggregate values are formed. **[C]** The equal-weight mean of the two subset baseline ASRs is `(56.90 + 88.67) / 2 = 72.785%`, which rounds to 72.8% at one decimal place. This numerical agreement does not establish the authors' actual weighting or denominators.

**[C]** The equal-weight mean of the full-system subset FPRs is `(0.97 + 3.28) / 2 = 2.125%`, which is not 1.49%. **[D]** Different weights or benign-case populations could produce a different aggregate, so this is an unresolved aggregation issue rather than a demonstrated contradiction. Without subset denominators, the 1.49% value cannot be reconstructed from the supplied report.

The strongest directly reported comparative conclusion is that, within this setup, both defenses prevent the measured target attacks while the second stage substantially reduces unnecessary rejections. The broader language of guaranteed security, negligible impact, and real-world viability requires qualification because the paper also acknowledges context-dependent arguments and reports no deployment or overhead measurements.

# 10. Figure-by-figure interpretation

## Figure 1 — Architecture and malicious product-information example

**Location:** p. 2. **Inspection:** Direct visual inspection plus caption and method cross-check. **Type:** Architecture/flow diagram; no axes, numerical scale, or statistical markers.

**[B]** A User Task requests product information for ID `XXX-001`. The upper blue path leads to a Planner, whose box identifies `GetProductDetails` as required, and a Trusted Reference box records `GetProductDetails` with the product ID. A separate path supplies the task to an Agent. A red Attacker box presents product information with an injected instruction to transfer **$500** to Amy. The Agent box depicts retrieval followed by the injected transfer. A Candidate Action box lists the legitimate product-details action and `TransferTool` with Amy. The rightmost yellow Verifier contains Hard Rules and Intent Verifier, with a green pass/check branch and red block/cross branch.

The color scheme distinguishes trusted planning flow, contaminated input/candidate behavior, and enforcement. The attack example shows function hijacking: a funds-transfer tool is outside a product-information request. The amount is an illustrative figure value, not an experimental cost or attack-success statistic.

The caption says the framework decouples instruction processing into two paths: isolated planning and execution. The prose and Algorithm 1 clarify details the diagram compresses: hard rules can pass exact matches or block unauthorized tools without calling the intent verifier; only parameter mismatches require Stage II. The stacked verifier boxes therefore should not be read as proof that every action always traverses both model and hard-rule checks.

**Caveat [D]:** The displayed example emphasizes an easily separable unauthorized tool. It does not itself demonstrate successful verification of context-dependent payment arguments, the limitation later acknowledged on p. 6.

## Figure 2 — DH and DS performance comparison

**Location:** p. 5. **Inspection:** Direct visual inspection, supplied extracted labels, and adjacent prose. **Panels:** Left DH; right DS. **Plot type:** Bars for ASR with a blue line for FPR, using separate vertical axes. **Horizontal categories:** Vanilla Agent; Single Rule (Stage I); PlanGuard (Stage I+II).

**[B]** The left ASR axis is percentage-scaled from 0 to 100; the right FPR axis is percentage-scaled from 0 to 50. The axes are linear as displayed. Pink/red ASR bars make the large vanilla attack rate visible; blue FPR markers/lines compare strict matching with the full system. The displayed line joins categorical configurations and should not be interpreted as a continuous time trajectory.

The visible important labels correspond to DH baseline ASR **56.9%**, DS baseline ASR **88.67%**, and FPR changes **27.0% → 0.97%** and **38.01% → 3.28%**. The nearby text explicitly supplies defended ASR **0.0%** for both variants and subsets. No nonzero defended bar is visible. No error bars, confidence bands, significance stars, or individual-case distributions appear.

**Meaning:** The figure visually separates two outcomes: preventing attacks and avoiding false alarms. Both defended configurations suppress reported ASR, while the full configuration has substantially lower FPR. **Caveats:** The caption names Vanilla Agent and PlanGuard but the visual also contains the Single Rule ablation. Small typography limits confident reading of every graphical detail; important exact results are grounded in the prose, not estimated from bar heights. The dual axes require care: a blue line height cannot be compared numerically with a pink bar height without using its own axis.

# 11. Table-by-table interpretation

There are **no substantive numbered tables** in the supplied paper. Figure 2 carries quantitative comparisons, while Algorithm 1 contains pseudocode. Tables in this analysis are analyst-created organizational aids and must not be mistaken for original paper tables.

Accordingly, there are no original table rows, missing-value symbols, table footnotes, uncertainty columns, or table-specific significance results to audit. This absence matters because per-case outcomes, subgroup denominators, and aggregate construction are not available through a hidden supplied table.

# 12. Diagram / architecture interpretation

Figure 1 represents two information paths that meet at authorization. The user's task supplies both the planner and the agent. The planner's protected input creates a trusted reference; the agent's wider input includes attacker-controlled retrieved material. The agent proposes actions, and the verifier compares them with the reference before permitting execution.

The information boundary is central: the planner does not read the attacker-controlled product description. This prevents that description from directly asking the planner to add `TransferTool`. The agent may still produce the malicious call; protection depends on enforcement stopping it. Thus, the method need not make the victim immune to contaminated instructions internally to prevent the corresponding action from executing.

Algorithm 1 adds the precise control path. First, exact reference membership returns Pass. Second, a missing tool name returns Block. Third, remaining calls go to the intent model. There is no depicted feedback loop from a rejected action to replanning, no reference-set update from tool results, and no supplied workflow for recovering from a block. Their absence from the description is a reporting boundary, not proof that an implementation lacks all such mechanisms.

**[D]** The architecture is best understood as an authorization check relative to a protected plan. Its security depends on the reference capturing the user's legitimate scope and on the semantic review handling exceptions safely. Excluding external information addresses direct planner contamination, but it does not by itself supply missing factual ground truth or prove the correctness of every planned action.

# 13. Equations and mathematical concepts

The paper uses seven equations as formal descriptions. It supplies no theorem proving all accepted actions safe, and no probabilistic bound on verifier error. Subscripts below are rendered in readable text notation; the identities preserve the source meaning.

## Equation (1), p. 3 — Agent action sequence

`a = A(I, T) = (a_1, a_2, …, a_m), where m ≥ 0`.

This maps user instruction `I` and tool set `T` through agent `A` to a sequence `a`. The integer `m` is sequence length, including the possibility of no action. Each `a_i = (t_k, v_k)` pairs a tool `t_k ∈ T` with its arguments `v_k`. The equation defines the basic unit the defense later checks. It is not an optimization objective, loss function, or empirical estimator.

**Notation boundary [D]:** The surrounding system discusses external context `C`, but Eq. (1) does not include `C` as an explicit input. The equation presents an ideal instruction-to-action model; it does not fully specify the runtime influence of retrieved information.

## Equation (2), p. 3 — Effective instruction mixture

`I_effective = I ∪ p_adv`.

The authors use union to represent the trusted instruction combined with an injected payload. `p_adv` is attacker content placed in external context; `I_effective` is what drives compromised behavior. In plain language, the model acts as if the malicious retrieved instruction joins the legitimate request. **[D]** The union notation is a conceptual representation: no operational parsing rule, ordering semantics, or conflict-resolution algorithm is defined for it.

## Equation (3), p. 3 — Unauthorized tool invocation

`a_adv = (t_adv, v_adv)`.

This defines a malicious action using tool `t_adv` and arguments `v_adv`. The critical condition is stated in prose: the tool is not implied by the semantics of `I`. The formula alone does not determine that relationship; the protected reference is used later to operationalize tool eligibility.

## Equation (4), p. 3 — Argument hijacking

`a_adv = (t_correct, v_adv)`.

Here the tool is the one required by the legitimate instruction, but the arguments conflict with its constraints or intent. This distinguishes tool-name correctness from action correctness. Calling a permitted deletion tool can still be malicious if it targets the wrong path. No formal semantic predicate for argument conflict is given.

## Equation (5), p. 3 — Attack-success condition

`ã = A(I_effective, T), subject to a_adv ∈ ã`.

The tilde marks the actual execution sequence under the effective mixed instruction. Success means that the target malicious action occurs in that sequence. Membership means occurrence, even though the sequence is ordered. The equation defines the event counted conceptually by ASR; it does not specify the benchmark's implementation of outcome checking or its denominators.

## Equation (6), p. 4 — Isolated reference generation

`S_ref = P(I, T) = {a_1, a_2, …, a_k}, where k ≥ 0`.

Planner `P` maps the user instruction and tool definitions to a set of zero or more reference actions. Excluding `C` and `p_adv` expresses the isolation boundary. The output is a set, unlike the agent's sequence. **[D]** Algorithm 1 checks individual membership but does not describe enforcement of order, repetition counts, or sequence-wide constraints. A clean set and a safe complete execution are related concepts, but not identical mathematical objects.

The authors say isolation ensures only necessary user-intended actions occur in the set. **[D]** Independence from attacker input supports absence of direct contamination; necessity and correctness additionally depend on the planner's ability to interpret the instruction and tools. No proof of that ability is provided.

## Equation (7), p. 4 — Intent-verifier judgment

`V_res = M_verify(I, S_ref, a_act, r_act) → {T, F}`.

`M_verify` is the verifier model; `a_act` is the captured action; `r_act` is the agent's preceding reasoning or Thought; `V_res` is the verification result. Here `T` in `{T, F}` denotes True, whereas `T` elsewhere denotes the tool set—a contextual overloading of notation. The result permits or blocks a parameter-mismatched call. The arrow indicates a Boolean-valued judgment rather than a trained objective or calibrated probability.

No decision threshold, confidence score, formal semantics of benign equivalence, or reliability guarantee is supplied. The equation connects to Algorithm 1's final branch and the measured reduction in false positives, but it does not establish that all accepted deviations are safe.

# 14. Interpretation and discussion

**Authors' interpretation [A]:** Vanilla failure arises because malicious external content reaches the agent's instruction-following process. PlanGuard succeeds by separating reference generation from that content, and semantic tolerance preserves legitimate actions that differ textually from the reference. Source: p. 5, §V-C.

**Supported experimental reading [D]:** The benchmark comparison supports the claim that this architecture prevented the measured malicious behavior in the reported setup and that Stage II reduced false alarms relative to exact matching. Because the strict variant also achieved zero ASR, the results do not show that Stage II was necessary to improve attack prevention on this benchmark. Its demonstrated advantage is usability as represented by FPR.

**Unresolved strengthening [D]:** The paper describes the defense as a deterministic firewall and argues that actions cannot deviate from intent. Its own Stage II uses an LLM judgment, and its limitation admits missing ground truth for contextual argument values. A protected reference generator is narrower than an unconditional guarantee about every accepted action. The results and discussion should therefore be retained together, rather than repeating only the strongest claim.

**Research-question interpretation [D]:** Relative to a standalone text interaction, the agent architecture described here adds external retrieval and an execution interface. The authors directly identify those two features as enabling injection and real-world consequences. However, the relative comparison itself remains an analyst inference: the experiment contains three agent-defense configurations, not standalone and agent groups. The paper cannot quantify the independent contributions of browsing, tool permissions, autonomous sequencing, or model behavior to a comparative vulnerability gap.

**Consistency audit:** The DH numeric formatting 56.9% versus 56.90%, and 27.0% versus 27.00%, agrees in value. The abstract aggregate ASR is compatible with an equal-subset average, but the calculation method is unstated. The aggregate FPR is not that equal-subset average. The white-box robustness discussion has no accompanying adaptive evaluation. Schema validation is discussed but omitted from Algorithm 1. The text also describes a planner using sanitized instructions without supplying a sanitization procedure. These are preserved as unresolved reporting boundaries rather than silently repaired.

# 15. Contributions and novelty

**Conceptual contribution [A]:** Instruction-data isolation shifts authorization toward a reference formed independently of retrieved content. **System contribution [A]:** The isolated planner and execution-time interception organize planning, proposal, verification, and enforcement as separate roles. **Algorithmic contribution [A]:** Hierarchical checking combines exact action matching, unauthorized-tool rejection, and semantic argument review. Sources: pp. 2–4.

**Empirical contribution [A]:** The paper reports InjecAgent results with zero ASR in both categories and substantially reduced FPR after adding Stage II. **Implementation availability claim [A]:** A GitHub source-code URL is printed on p. 2. This analysis has not inspected that repository, verified its availability, or checked whether it reproduces the paper.

No new dataset or benchmark is introduced; InjecAgent is reused. No formal theorem or security proof is supplied. No measured scalability or latency contribution is presented. The abstract calls the method model-agnostic and highly compatible, but only DeepSeek-V3.2 is identified in the reported evaluation. **[D]** Those attributes are design claims rather than demonstrated cross-model results within the supplied evidence.

Novelty is described here as the authors' proposed combination and framing, not independently verified priority over the external literature. The related-work section provides positioning but does not substitute for an inspected comparative literature review.

# 16. Limitations

## Authors' stated limitations

**L1 — Additional cost [A]:** PlanGuard adds planner and Stage-II verifier inference, producing computational overhead and token costs relative to Vanilla. The authors regard this as a security trade-off and propose smaller specialized models. No numerical overhead measurement accompanies the acknowledgement. Source: p. 5, §VI-A.

**L2 — Context-dependent argument hijacking [A]:** Planner isolation creates information asymmetry. A user may authorize an action whose correct parameters exist only in external content. The planner can identify the action type while lacking the truth needed to check specific values. The payment-from-email example makes this boundary explicit. Source: p. 6, §VI-B.

## Additional evidence-based analyst observations

**[D] Reporting and generalization:** One named backbone and one benchmark do not demonstrate model-agnostic empirical performance or all open-world tasks. The compliance-inducing prompt changes the victim's behavior and limits direct transfer to ordinary configurations. Benign-case counts, subset counts, randomization, repetitions, and confidence intervals are not supplied.

**[D] Verification boundary:** The intent verifier consumes proposed action data and victim reasoning, both potentially influenced by injection. The paper discusses an adaptive attack through parameters but reports no dedicated test of that route. Structured fields may constrain a payload, yet the supplied material does not inventory every schema or establish that all fields reject free text.

**[D] Reference adequacy:** A set of allowable actions does not explicitly capture order, frequency, or cumulative effects. The paper does not explain handling of repeated approved calls, dynamic tool-dependent discoveries, changing user instructions, or an empty reference in a task that legitimately needs action. These are questions raised by the formal description, not demonstrated implementation failures.

**[D] Utility measurement:** FPR captures one form of usability loss. It is not a complete task-success, correctness, latency, or user-effort evaluation. A passed action may still be unhelpful or factually wrong without being a malicious intent shift. The supplied evidence cannot assess those dimensions.

# 17. Threats to validity

The labels in this section are analyst methodology categories, not headings the authors themselves use.

**Internal validity [D]:** The Stage-I/full comparison makes the role of semantic review visible, but the supplied report gives limited details about identical case handling, stochastic sampling, and repetitions. The authors' explanation that intrinsic safety causes the DH–DS baseline difference is not tested by a separate safety-policy intervention beyond the shared compliance directive.

**Construct validity [D]:** ASR measures induced target malicious behavior, and FPR measures benign false alarms. Neither alone measures all unsafe output, all agent failures, or complete useful-task performance. The paper's actionable scope deliberately excludes misinformation and toxic text. The operational test for target success and the benign-case denominator are insufficiently specified for independent reconstruction.

**Statistical conclusion validity [D]:** No confidence intervals, standard errors, significance tests, or run counts are reported. Zero observed ASR is a finite reported outcome; without group counts and repetition details, its sampling uncertainty cannot be quantified from this paper. Rounded rates must not be converted into invented integer event counts.

**External validity and generalizability [D]:** Evidence is concentrated in InjecAgent, DeepSeek-V3.2, and a deliberately receptive victim prompt. Cross-model deployment, novel attacks, longer task chains, and context-dependent arguments remain insufficiently established. A benchmark's tool categories are not equivalent to an evaluated live web-browsing workflow.

**Ecological validity [D]:** The setup simulates tool-return attacks and is motivated by real-world agents. The supplied paper reports no live deployment study showing its behavior under ordinary permissions, recovery workflows, or realistic cost constraints.

**Reproducibility [D]:** A source-code link is promising as an availability statement, but the artifact was not supplied. Missing full planner/verifier prompts, runtime settings, denominators, and aggregation rules prevent this closed-document analysis from independently reconstructing all results.

# 18. Future work and open questions

## A. Future work explicitly proposed by the authors

**[A]** Train specialized **Small Language Models (SLMs)** to replace the current general-purpose planner/verifier models, with the stated aim of reducing inference latency and operational cost while preserving effectiveness. Source: p. 5, §VI-A. The reduction is prospective, not measured.

**[A]** Address context-dependent argument hijacking through rule-based information extraction. Source: p. 6, §VI-B. The supplied paper does not provide the completed extraction algorithm, trust rule, or evaluation.

## B. Additional open questions from the supplied evidence

**[D]** How should external facts be admitted without converting attacker instructions into authorization? How reliably does Stage II resist malicious parameter content and misleading victim reasoning? What happens when approved actions are repeated or executed in a harmful order? Can a reference represent constraints and dependencies rather than only enumerated tuples?

**[D]** How do outcomes change with ordinary victim prompts, other backbones, different tool schemas, and longer tasks? What are actual planner latency, verifier latency, token consumption, task completion, and recovery costs? What benign populations and weights produce the reported aggregate FPR? A direct comparison with standalone LLMs would additionally require a defined common outcome and comparable task/attack conditions; this study does not provide that experiment.

# 19. Terminology and notation glossary

| Term / symbol | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large Language Model; the language-based component driving agent decisions. |
| Agent `A` | System generating tool-action sequences. |
| API | Application Programming Interface used to interact with external functions. |
| IPI | Indirect Prompt Injection: malicious instructions placed in retrieved content. |
| Actionable IPI | Injection resulting in unauthorized tool execution. |
| Context mixing | Failure to separate trusted instructions from untrusted data. |
| Context isolation | Restricting protected planning to the user instruction and tools. |
| `I` | Trusted user instruction; assumed root of trust. |
| `C` | Untrusted external context, such as a webpage. |
| `T` | Tool set `{t_1, …, t_n}`; also overloaded as True in Eq. (7). |
| `t`, `v` | Tool name and its argument/parameter values. |
| `a_i` | One action tuple `(t_k, v_k)`. |
| `a`, `ã` | Ordinary modeled action sequence and actual sequence under mixed instructions. |
| `m`, `k` | Number of sequence actions and number of reference-set actions; each may be zero. |
| `p_adv` | Adversarial payload injected into external context. |
| `I_effective` | Combined instruction influence under an injection. |
| `a_adv` | Target malicious action. |
| Type I | Function hijacking: unauthorized tool selection. |
| Type II | Argument hijacking: malicious parameters for the right tool. |
| `P`, `S_ref` | Isolated planner and its Reference Action Set. |
| `V` | Hierarchical verifier component. |
| `a_act`, `r_act` | Captured proposed action and preceding victim-agent reasoning. |
| `M_verify`, `V_res` | Intent-verifier model and its Boolean result. |
| Hard rules / Stage I | Exact action match and tool-membership checks. |
| Stage II | Semantic review of parameter mismatches. |
| ASR | Attack Success Rate; fraction of adversarial inputs inducing target behavior. |
| FPR | False Positive Rate; false alarms in benign scenarios. |
| DH / DS | Direct Harm / Data Stealing benchmark categories. |
| PPL | Perplexity, used by a related-work detection category; no calculation supplied. |
| White-box attacker | Attacker assumed to know the defense architecture. |
| Schema validation | Checking tool arguments against permitted types and formats. |
| SLM | Small Language Model proposed for future cost reduction. |

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| InjecAgent test cases | 1,054 | cases | Dataset described for evaluation | Author-reported | p. 4, §V-A1 |
| User tools | 17 | tools | Dataset description | Author-reported | p. 4, §V-A1 |
| Attacker tools | 62 | tools | Dataset description | Author-reported | p. 4, §V-A1 |
| Abstract baseline ASR | 72.8 | % | Aggregate interpretation unspecified | Author-reported | p. 1, abstract |
| Abstract defended ASR | 0 | % | PlanGuard | Author-reported | p. 1, abstract |
| Abstract full-system FPR | 1.49 | % | Aggregate denominator/weighting unspecified | Author-reported | p. 1, abstract |
| Vanilla DH ASR | 56.90 | % | DeepSeek-V3.2; compliance-inducing prompt | Author-reported | p. 5, §V-B1 |
| Vanilla DS ASR | 88.67 | % | Same shared setup | Author-reported | p. 5, §V-B1 |
| Stage-I Only ASR | 0.0 | % | Both DH and DS | Author-reported | p. 5, §V-B2 |
| Full PlanGuard ASR | 0.0 | % | Both DH and DS | Author-reported | p. 5, §V-B2 |
| Strict DH FPR | 27.00 | % | Stage-I Only; benign scenarios | Author-reported | p. 5, §V-B3 |
| Full DH FPR | 0.97 | % | PlanGuard; benign scenarios | Author-reported | p. 5, §V-B3 |
| Strict DS FPR | 38.01 | % | Stage-I Only; benign scenarios | Author-reported | p. 5, §V-B3 |
| Full DS FPR | 3.28 | % | PlanGuard; benign scenarios | Author-reported | p. 5, §V-B3 |
| DH FPR decrease | 26.03 | percentage points | 27.00 − 0.97 | Analyst-derived | p. 5 operands |
| DS FPR decrease | 34.73 | percentage points | 38.01 − 3.28 | Analyst-derived | p. 5 operands |
| Relative DH FPR decrease | approximately 96.41 | % | 26.03 / 27.00 × 100 | Analyst-derived | p. 5 operands |
| Relative DS FPR decrease | approximately 91.37 | % | 34.73 / 38.01 × 100 | Analyst-derived | p. 5 operands |
| Equal-subset baseline ASR mean | 72.785 | % | (56.90 + 88.67) / 2; actual weights unknown | Analyst-derived | p. 5 operands |
| Equal-subset full FPR mean | 2.125 | % | (0.97 + 3.28) / 2; not the abstract aggregate | Analyst-derived | p. 5 operands |
| Architecture example transfer | 500 | dollars | Illustrative attacker instruction; not a result | Visually readable | p. 2, Fig. 1 |
| Workflow stages | 4 | steps | Reference, capture, verify, enforce | Author-reported | p. 3, §IV-A2 |
| Verification stages | 2 | stages | Hard rules and intent verification | Author-reported | p. 4, §IV-C |

No plotted quantity in this table is inferred solely from graphical height. Important result values are explicitly reported in prose. No per-subset sample count, exact event count, confidence interval, latency, token total, dollar operating cost, or adaptive-attack success rate is supplied.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External content can carry instructions that redirect agents | Explicit context-mixing and injection account | Problem framing | p. 1, §I | Author account; no standalone comparison. |
| Scope is unauthorized tool execution | Explicit actionable-IPI restriction | Threat-model scope | p. 2, §III-A1 | Strong textual evidence; excludes textual-only failures. |
| User instruction is trusted; attacker targets external context | Explicit attacker capability and trust statements | Threat model | p. 3, §III | Assumption of the study, not empirically tested user authenticity. |
| Planner excludes retrieved context | Input mapping uses only `I` and `T` | Eq. (6), Fig. 1 | pp. 2, 4 | Strong method evidence; planner correctness is a separate issue. |
| Unauthorized tools are blocked before semantic review | Tool-membership branch | Algorithm 1 | p. 4 | Clear specified behavior; implementation not inspected. |
| Parameter mismatches receive model review | Boolean intent mapping and final branch | Eq. (7), Algorithm 1 | p. 4 | Model-based judgment; no formal correctness guarantee. |
| Both defended variants achieve zero reported ASR | Main-results statement | X1–X2, Fig. 2 | p. 5 | One named backbone and modified victim prompt; no uncertainty reported. |
| Stage II reduces benign rejection | DH and DS FPR comparisons | X3, Fig. 2 | p. 5 | Large rate differences; benign denominators unavailable. |
| Adaptive attacks face generation/schema hurdles | Two qualitative constraints | Discussion only | p. 6, §VI-B | Argument, not a supplied adaptive-attack experiment. |
| Isolation limits checking of context-derived parameters | Explicit payment-email example | Limitation L2 | p. 6, §VI-B | Direct acknowledged boundary to general security claims. |
| Additional inference incurs overhead | Explicit cost acknowledgement | Discussion L1 | p. 5, §VI-A | Qualitative; no measured cost or latency. |
| Agent connectivity and tools are relevant to comparative vulnerability | External-input route plus execution consequences | Research synthesis | pp. 1–3 | Analyst inference; no measured standalone-versus-agent effect. |

Confidence is HIGH for clear reporting of method, numerical statements, and explicit limitations. Confidence in universal security or general comparative vulnerability is lower because the supplied evaluation does not establish those propositions. The distinction avoids treating fidelity to an author sentence as confirmation of an unlimited guarantee.

# 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant that can read an email and also use buttons that send messages, delete files, or pay bills. An attacker puts a sentence inside the email telling the assistant to press a different button. The problem is that the assistant may mistake a sentence it is supposed to read for an instruction it is supposed to obey.

PlanGuard adds a separate planner that reads your request but never reads that email. The planner writes down which actions fit your request. Before the assistant presses a button, a checker compares the proposed action with that protected list. An entirely different button is blocked. If the button is right but the details look different, another model checks whether the difference is harmless or changes what you wanted.

In the paper's test, the protected systems stopped all measured target attacks. The extra meaning-based check also prevented many harmless actions from being rejected. But the test made the ordinary assistant unusually willing to obey commands in tool responses, and it used one named model. The results therefore describe that test, rather than proving that every possible agent attack is solved.

There is also a difficult case: if you say “pay the bill in the email,” the planner needs information from the email to know the right amount and recipient. Keeping it away from the email protects it from malicious instructions, but also keeps it away from useful facts. The authors acknowledge this problem. For your question about web agents, the paper shows why reading attacker-controlled material while holding action permissions can be dangerous; it does not measure a direct comparison with a standalone chatbot.

# Completeness Audit

The audit compares the representation above with the supplied-document inventory. “Fully represented” means the substantive supplied content is accounted for; it does not mean every sentence is reproduced or every author claim is independently verified.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META: title/authors/affiliations/version | Yes, text and p. 1 image | Yes | Fully represented | §2; contact details compressed. |
| ABS: abstract/index terms | Yes | Yes | Fully represented | Claims and aggregate numbers retained; keywords reflected in glossary/context. |
| S1: Introduction | Yes | Yes | Represented in compressed form | Problem, motivation, architecture and claims retained. |
| C1–C3: contribution bullets | Yes | Yes | Fully represented | §15 and claim map. |
| Source-code availability statement | Yes | Yes | Fully represented | Link's existence reported; repository not reviewed. |
| S2: Related Work | Yes | Yes | Represented in compressed form | All four paradigms and attributed shortcomings covered. |
| S3A1: Actionable IPI scope | Yes | Yes | Fully represented | Textual-only deviations excluded. |
| S3A2: Agent Modeling | Yes | Yes | Fully represented | Trust entities and tuple/sequence model explained. |
| S3B1: Attacker Capabilities | Yes | Yes | Fully represented | Cannot modify user instruction; injects external context. |
| S3B2: Attack Goals | Yes | Yes | Fully represented | Type I/II definitions and examples covered. |
| S4A1: Architecture | Yes | Yes | Fully represented | Components and input boundaries described. |
| S4A2: Workflow | Yes | Yes | Fully represented | All four steps retained. |
| S4B: Isolated Planner | Yes | Yes | Fully represented | Clean input and ground-truth boundary explained. |
| S4C1: Hard Rules | Yes | Yes | Fully represented | All three cases represented. |
| S4C2: Intent Verification | Yes | Yes | Fully represented | Inputs, Boolean result and formatting example covered. |
| ALG1: Algorithm 1 | Yes, text and image | Yes | Fully represented | Branch order and missing schema step noted. |
| E1: action sequence | Yes | Yes | Fully represented | Symbols and omitted explicit context discussed. |
| E2: effective instructions | Yes | Yes | Fully represented | Union treated as conceptual model. |
| E3: unauthorized tool | Yes | Yes | Fully represented | Semantic condition preserved. |
| E4: malicious arguments | Yes | Yes | Fully represented | Tool correctness separated from argument correctness. |
| E5: attack success | Yes | Yes | Fully represented | Target occurrence explained. |
| E6: reference set | Yes | Yes | Fully represented | Set/sequence distinction and zero-action case covered. |
| E7: intent result | Yes | Yes | Fully represented | All inputs and overloaded True notation covered. |
| S5A1: Dataset/scenarios | Yes | Yes | Fully represented | 1,054 cases, 17/62 tools, DH/DS retained. |
| S5A2: Backbone/prompt condition | Yes | Yes | Fully represented | DeepSeek-V3.2 and deliberately increased compliance retained. |
| S5A3: Baselines | Yes | Yes | Fully represented | All three configurations identified. |
| S5A4: Metrics | Yes | Yes | Fully represented | ASR/FPR and absent denominator detail covered. |
| X1: DH comparison | Yes | Yes | Fully represented | All reported DH values and caveats covered. |
| X2: DS comparison | Yes | Yes | Fully represented | All reported DS values and caveats covered. |
| X3: Stage-II ablation | Yes | Yes | Fully represented | Utility benefit distinguished from unchanged zero ASR. |
| S5B1: baseline interpretation | Yes | Yes | Fully represented | Safety-sensitivity explanation attributed to authors. |
| S5B2: zero-ASR interpretation | Yes | Yes | Fully represented | Structural claim retained and qualified. |
| S5B3: FPR interpretation | Yes | Yes | Fully represented | Exact rates and derived differences distinguished. |
| S5C1–C2: reliability analysis | Yes | Yes | Represented in compressed form | Context mixing, isolation and tolerance covered. |
| F1: architecture diagram | Yes, directly visual | Yes | Fully represented | Visual-only example details and flow retained. |
| F2: both result panels | Yes, directly visual | Yes | Fully represented | Axes, encodings, numbers and dual-axis caveat covered. |
| All substantive tables | No tables present | Not applicable | Fully accounted for | Analyst tables are not source tables. |
| S6A/L1: performance and cost | Yes | Yes | Fully represented | Qualitative overhead; no invented measurements. |
| S6B: adaptive robustness | Yes | Yes | Fully represented | Both hurdles and absence of empirical adaptive test covered. |
| L2: contextual arguments | Yes | Yes | Fully represented | Author limitation and example retained. |
| FW1–FW2: future work | Yes | Yes | Fully represented | Smaller models and extraction proposal covered. |
| S7: Conclusion | Yes | Yes | Represented in compressed form | Repeated central claims retained without duplicate prose. |
| Explicit research questions | None present | Absence stated | Fully accounted for | User research question separately labeled. |
| Explicit hypotheses | None present | Absence stated | Fully accounted for | No formal tests invented. |
| Theorems/lemmas/propositions | None present | Absence stated | Fully accounted for | Equations are definitions/mappings, not proofs. |
| ACK: acknowledgements/note | Yes | Yes, compressed | Inspected but deliberately compressed as secondary | Funding bodies and correspondence noted below. |
| REF: bibliography | Yes; p. 7 text only | Yes, compressed | Represented in compressed form | 22 entries identified; cited works not reviewed. |
| Appendices | None supplied | Absence stated | Fully accounted for | No hidden appendix content assumed. |
| Supplied supplements | None supplied | Absence stated | Fully accounted for | No supplement reviewed. |
| External code/benchmark artifacts | No | Availability/reference only | Missing from supplied material | No implementation or raw-data audit. |
| Page 7 visual rendering | No | Text content represented | Inaccessible as a visual | Only supplied text assessed. |

## Missing or inaccessible material

The code repository, underlying benchmark artifact, raw outcomes, complete runtime prompts, and any additional implementation files were not supplied. The paper cites them or leaves relevant details unspecified; they were not inspected. Page 7 lacks a supplied rendered image, although its reference text is accessible. No appendix or supplementary package is supplied, and no explicit missing supplementary-file reference was identified. The analysis cannot independently certify the source hash against a file because tools were prohibited; it preserves the user-provided identifier.

## Uncertain interpretations

The aggregate FPR of 1.49% cannot be reproduced from the subset rates without missing denominators or weights. The aggregate ASR is numerically compatible with an equal-subset mean, but its calculation remains unstated. The practical extent of schema protection, the sanitization procedure, and the reliability of the semantic verifier are unspecified. The source does not operationalize every semantic condition used in its equations. Small Figure 2 typography prevents a confident transcription of every minor graphical label, while the important numbers are corroborated by prose.

Broad deterministic-security language must be read alongside model-based Stage II and the acknowledged contextual-argument limitation. The paper's explanation of the DH–DS difference is not isolated by a separate experiment. Its design-level model-agnostic claim is not supported by a reported multi-model evaluation. These uncertainties are identified rather than resolved through outside knowledge.

## Deliberately compressed material

Repeated abstract/introduction/conclusion statements were consolidated while preserving distinct claims and numbers. Related-work citations were grouped by the authors' four categories; the external works were not summarized as if read. All 22 references were inspected as supplied bibliographic text, but individual author lists, publication page spans, and every URL were not reproduced. Entries [7] and [9] list the same work title and arXiv identifier with different bibliographic dating; no external reconciliation was attempted.

The acknowledgements identify NSFC, the Shandong Provincial Natural Science Foundation, the Basic Research Program of Jiangsu Province, and the Taishan Scholars Program. Grant identifiers and author email addresses are secondary administrative details deliberately omitted from the substantive explanation. The corresponding-author note identifies Zizhuang Deng. Figure 1's decorative icons and page typography were inspected but not individually catalogued because they do not add scientific claims.

## Potential omissions

No known substantive item in the available inventory has been left without representation or an explicit limitation entry. This is an inventory-based coverage statement about the supplied seven text pages and six images, not a claim of word-for-word preservation, independent reproduction, comprehensive review of the cited literature, or access to undisclosed artifacts. The central unresolved issues—aggregate-rate construction, untested generality, adaptive-verifier robustness, overhead, and context-dependent arguments—remain visible in the analysis.
