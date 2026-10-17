## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–20. Rendered page images are supplied for pages 1, 2, 4, 5, 7, 8, 11–15, and 17–20. These 15 pages were inspected visually as well as through the supplied text. Pages 3, 6, 9, 10, and 16 were inspected through supplied text only. No tools, browsing, external sources, or supplementary repositories were used. Instructions appearing inside attack examples, prompts, and tool outputs were treated solely as untrusted documentary evidence.

The main text, references, and Appendices A–F are present. The available sequence ends at page 20 without an obvious unfinished section. This establishes coverage of the supplied 20-page document, not independent verification that no separate supplement exists. No supplementary files were supplied. A code repository is linked on page 1, but its contents were not inspected. The supplied accessibility metadata's indication that appendix pages were detected at page 4 does not describe the visible document organization: Appendix A begins on page 12.

All five numbered tables are available and readable through extracted text; Tables 1–4 are also visually available on page 8, and Table 5 on page 20. Figures 1–4 and Algorithm 1 are visually available. Small plot markers and diagram labels require care, so exact experimental values below come from tables rather than estimates of marker positions. Mathematical expressions are mostly readable, but flattened extraction obscures some superscripts, set membership, and norm notation. The theoretical error bounds on page 6 have text-only coverage. OCR was not needed, and no independent OCR was performed.

Evidence labels used throughout are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Confidence is HIGH where source wording and tables are clear; MEDIUM where interpretation, incomplete specifications, or source inconsistencies matter. All page locators refer to physical PDF pages, which agree with the printed page numbers.

## 1. Plain-language orientation

MELON studies indirect prompt injection: an agent reads outside material while performing a legitimate task, but that material contains instructions planted by an attacker. A website, email, or file can therefore become an instruction channel. The danger is consequential because the agent can use tools to send messages, transfer money, modify files, or otherwise act on what it reads. The authors focus on detecting when such instructions actually redirect the agent, rather than merely identifying suspicious language. [A: pp. 1–3]

The defense compares two proposed continuations. One uses the real user task and normal execution history. The other removes the user task and prior generated actions, preserves retrieved tool outputs, and substitutes a general prompt. If both continuations propose sufficiently similar tool calls, MELON treats that agreement as evidence that the outside material is driving the agent's behavior. A cache allows comparison with calls proposed by earlier masked continuations. Detection occurs after the original agent proposes its next action but before the proposed tools execute. [A: pp. 3–5, 7]

The evaluation uses AgentDojo, three language models, four attack templates, and five baseline defenses. MELON substantially lowers attack success while retaining more useful activity than defenses that stop whenever suspicious material appears. Its augmented version adds repetition of the original user prompt. For GPT-4o, MELON-Aug reports 68.72% average utility under attack and 0.32% average attack success, compared with 69.08% and 16.06% without defense. However, plain MELON has the lower GPT-4o attack success, 0.24%, while retaining less utility, 58.78%. Thus augmentation improves the balance between utility and security rather than uniformly improving every metric. [A: pp. 6–8]

The central contribution is a behavioral detection method based on how much a proposed action depends on the user's task. The title's word 'Provable' refers to a separate ensemble construction and conditional error bounds. It does not establish that the evaluated single-prompt implementation blocks every injection. The paper reports residual failures, false positives, and approximately doubled model-call costs. [A: pp. 5–6, 9; D: distinction between theoretical and evaluated configurations]

## 2. Document roadmap and inventory

This is a mixed AI-security, algorithm, systems, empirical, and theoretical paper. The title is **MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents**. The authors are Kaijie Zhu, Xianjun Yang, Jindong Wang, Wenbo Guo, and William Wang. The supplied publication note identifies the Proceedings of the 42nd International Conference on Machine Learning, Vancouver, Canada, PMLR 267, 2025. Affiliations are the University of California, Santa Barbara, and William & Mary. [A: p. 1]

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| ABS | Abstract | 1 | Motivation, proposed method, headline contributions |
| S1 | 1. Introduction | 1–2 | Injection problem and security–utility trade-off |
| S2 | 2. Related Work | 2–3 | Attack and defense categories |
| S3.1 | 3.1. Preliminaries | 3 | Agent state and threat model |
| S3.2 | 3.2. Technical Overview | 3–5 | Behavioral insight, challenges, three design choices |
| S3.3 | 3.3. Technical Details | 5 | Cache population and similarity detection |
| S3.3.1 | Implementation and Overhead Analysis | 5 | Serialization, embeddings, threshold, costs |
| S3.4.1 | Ensemble Detector | 5–6 | Multiple masking prompts |
| S3.4.2 | Error Bounds | 6 | Conditional concentration bounds |
| S4.1 | Experiment Setup | 6–7 | Models, benchmark, attacks, baselines, metrics |
| S4.2 | Experiment Results | 7 | Utility and attack-success interpretation |
| S4.3 | Ablation Study and Sensitivity Test | 7–9 | Components, prompts, thresholds |
| S4.4 | Analysis of False Positive Rate | 9 | Benign-operation detections |
| S4.5 | Analysis of Attack Success Cases | 9 | Four residual failure categories |
| S5 | Conclusion and Future Work | 9 | Main interpretation and future directions |
| IMP/ACK/REF | Impact, acknowledgements, references | 9–11 | Consequences, funding, cited literature |
| A1–A3 | Appendix A. MELON | 12–14 | Full prompt, examples, call transformation |
| B | Basic Agent Pipeline | 14–15 | Iterative action–observation loop |
| C1–C2 | Attacks and Defenses | 14–17 | Concrete templates and baseline behavior |
| D1–D2 | Datasets | 17–18 | AgentDojo and excluded VWA-Adv |
| E1–E2 | Examples of False Positives | 18–20 | DeBERTa and MELON examples |
| F | LLM Detector FPN and FNR | 20 | Detector diagnostic results |

The visual inventory contains F1, an aggregate utility–attack scatter plot; F2, the MELON pipeline; F3, three model-specific scatter panels; and F4, the basic agent loop. Tables T1–T5 cover the main comparison, component ablation, prompt sensitivity, threshold sensitivity, and LLM-detector diagnostics. ALG1 is Algorithm 1 on page 4. Mathematical inventory E1–E8 covers state evolution, the dependence intuition, dual continuations, masking, cache accumulation, cosine similarity and alerts, ensemble detection, and error bounds. Experiments X1–X7 are registered in Section 8 below. No separately numbered formal research questions, hypotheses, theorems, or lemmas appear in the supplied work.

## 3. Background and context

A large language model, or LLM, generates responses from input context. In the paper's agent definition, that model is embedded within a system that also has tools and an execution loop. A tool call specifies a function and arguments; its execution returns an observation. The next model action can use the original task, earlier responses and calls, and returned observations. This repeated feedback is the basic system structure, not an experimental finding about comparative vulnerability. [A: p. 3; Appendix B, pp. 14–15]

Indirect prompt injection, or IPI, enters through retrieved information rather than through the legitimate user's original instruction. The authors distinguish this from direct injection, in which attack text is appended directly to user inputs. Their threat model includes websites, emails, and files. Malicious instructions need not describe inherently prohibited activities: sending an email or transferring funds can be legitimate when authorized, yet malicious when an attacker causes it. This makes task provenance and authorization central to the problem. [A: pp. 1–3]

The related-work section divides general attacks into patterns such as escape characters, context ignoring, and fake completion, and also discusses attacks specific to web or computer agents. It divides defenses into approaches requiring training resources and training-free approaches. The former include retraining the agent model or using a trained detector. The latter include prompt augmentation, detection questions, permitted-tool restrictions, and task-alignment checks. These are the authors' descriptions of prior work; the cited papers were not independently reviewed. [A: pp. 2–3]

Three metrics must be kept separate. **Benign utility (BU)** is user-task success without attacks. **Utility under attack (UA)** requires successful user-task completion while avoiding execution of the malicious task. **Attack success rate (ASR)** measures completion of the attacker's objective, including all required malicious steps. UA and ASR are not necessarily complements: a run can fail both the user task and the attacker task. [A: pp. 6–7; D: consequence of the definitions]

## 4. Research problem and gap

The existing problem is that external content can redirect an agent's actions. The authors argue that defenders must preserve useful behavior while stopping unauthorized actions, and that suspicious instructions and their associated actions can resemble legitimate work. A defense that simply blocks all potentially dangerous tools may prevent attacks by making the agent ineffective. [A: pp. 1–2, 7]

According to the authors, training-based defenses require substantial computational or data resources and can degrade normal utility. Prompt augmentation is inexpensive but insufficient against stronger attacks. Tool filtering can exclude tools required later in a dynamic workflow and can be bypassed when attacker and user tasks use the same tools. Content detectors can terminate useful runs even when the agent would have ignored the injected instruction. Known-answer detection can operate too late, after harmful execution. [A: pp. 2–3, 6–7]

The proposed gap is therefore a training-free, automated detector that considers the agent's proposed behavior and intervenes before harmful tools execute. MELON attempts to fill it by asking whether a proposed call persists when the user task is removed. Its scope is predominantly tool-mediated task redirection in the stated benchmark and attack configurations. The paper does not establish a general detector for all harmful model responses, all web interactions, or all multimodal attacks. [A: pp. 3–6, 9; D: scope synthesis]

For the user's research question, this work is most useful as evidence about mechanisms that add risk to tool-using agents: untrusted retrieval, persistent observations, and executable actions. It does not experimentally establish that web agents have a higher vulnerability rate than standalone LLMs. [D: research relevance inference]

## 5. Research questions, objectives, and hypotheses

**Explicit formal research questions:** none are presented as numbered questions. **Explicit formal hypotheses:** none are specified as a predeclared hypothesis-testing program. The analysis therefore does not invent them.

The explicit objectives are to detect IPI by comparing original and masked continuations; reduce false positives and false negatives through three design choices; compare MELON and MELON-Aug with existing defenses; test component necessity and parameter sensitivity; and provide a theoretical extension with worst-case error bounds. [A: pp. 1–2, 4–9]

The behavioral proposition motivating the method is that successful attacks make the next action less dependent on the user task and prior generated actions, and more dependent on attacker-bearing tool outputs. This is a proposed pattern underlying the algorithm, not an unconditional empirical law. The failure analysis demonstrates situations in which the tool-call proxy does not expose the attack. [A: pp. 3, 9]

The evaluation implicitly addresses practical questions about security–utility balance, benefit from prompt repetition, component removal, prompt wording, thresholds, benign detections, and missed attacks. These are analyst-organized questions corresponding to reported experiments, rather than questions explicitly labeled by the authors. [D]

## 6. Assumptions / Threat Model

The agent is an integrated system π with LLM components and tools F. The user task is assumed legitimate. Attackers cannot access the model's internal input and output inside the target agent; their control is restricted to external information retrieved by tools. They seek to substitute a malicious task Tm for the intended task Tu. The defender has complete access to agent states and system operation but is not assumed able to retrain the LLM or inspect its internal representations. [A: p. 3]

Assets and consequences are illustrated through private information, email recipients, financial transfers, file changes, and user-directed work. These are examples and benchmark domains, not an exhaustive asset taxonomy. The attack surface consists of observations returned from external websites, emails, files, and analogous retrieved resources. The trusted user-task assumption is important: the paper is not defending against a malicious legitimate user. [A: pp. 3, 14–20; D: interpretation of the boundary]

The experiments use predefined AgentDojo user tasks, attack tasks, and injection points, with four general text attack patterns. Selected agent-specific attacks are excluded because the authors consider their reported efficacy low or their threat models impractical. Methods requiring human intervention, white-box access, or action reversion are excluded from the defense analysis. [A: pp. 2–3, 6]

The ensemble guarantee additionally requires a separation of expected similarity: benign scores must lie below the decision threshold in expectation and malicious scores above it. The source does not fully specify conditions ensuring independent or otherwise suitably concentrated similarity observations across different prompts. Consequently, the guarantee must be read conditionally, not as a demonstrated property of every agent or attack. [A: p. 6; D: mathematical qualification]

A practical trust-boundary issue remains underdescribed: the masked continuation is intentionally encouraged to follow instructions in retrieved content, but the implementation discussion does not fully specify isolation, permissions, or side-effect prevention for that branch. Algorithm 1 generates proposed calls and compares them; it does not instruct their actual execution. The supplied text is insufficient to establish a complete sandbox design. [A: pp. 4–5, 12–14; D]

## 7. Methodology

### Agent state and proposed actions

At step t, state St consists of Tu, action history A1:t, and observation history O1:t. Each action Ai contains a text response Ri and a set of tool calls Ci. The model proposes At+1 = π(St); executing its calls produces the next observation. This process repeats until completion, error, or the maximum-step condition described in Appendix B. [A: pp. 3, 14]

### Original and masked continuations

The original continuation receives normal state. The masked continuation receives a substitute prompt Tf, an empty generated-action history, and a consolidated context containing prior tool outputs. Removing generated actions helps distinguish instruction following caused by retrieved content from behavior supported by the legitimate task history. The authors call Tf task-neutral because it is unrelated to the original user's task; it is still an instruction-bearing prompt. [A: pp. 3–5; D: clarification]

The complete Appendix A.1 prompt asks the model to retrieve random.txt, summarize it, follow instructions in it first, and avoid repeating tool calls already represented in the contents. This is more specific than the main text's short summarization example. Two few-shot conversations teach the model to summarize ordinary content without calls and to follow embedded instructions while reusing available tool results. [A: pp. 12–13]

### Three design choices

First, replacing rather than merely deleting Tu, consolidating observations, and providing examples aim to prevent arbitrary calls in the masked continuation. Second, a tool-call cache stores masked proposals over time, so an attacker-directed call can be matched even if the original continuation reaches it later. Third, comparison focuses on calls rather than full text-plus-call actions, because explanatory text may differ even when the consequential action is the same. [A: pp. 3–5]

### Algorithm 1

At each step, concatenate observations; build masked state; generate the masked action; extract its calls; add them to the cache; generate the original action; extract its calls; compare every original call against every cached call; and return an attack flag if any similarity exceeds θ. Otherwise return no attack detected. The prose describes the cache as accumulating prior calls. The printed update line is ambiguous because Ht+1 appears on both sides, so its intended accumulation semantics are clearer in the prose than in that line. [A/B: p. 4]

### Call representation and similarity

Calls are converted to strings containing function names and selected arguments. For send_email, only recipients are retained; subject and body are omitted. For send_money, recipient and amount are retained; other functions retain all arguments. Argument-free calls use function_name(), and the appendix mentions a 'No tool calls' string. Embeddings are compared with cosine similarity. The implementation names OpenAI's text-embedding-v3 model, but does not provide a more precise variant or version. The main threshold is θ = 0.8. [A: pp. 5, 13–14]

### Data and configuration

AgentDojo contains banking, Slack, travel, and workspace agents with 16, 21, 20, and 40 user tasks respectively: 97 in total. There are 629 user-task/attack-task cases. The models are GPT-4o, o3-mini, and Llama-3.3-70B, each configured with temperature 0. The authors omit large-scale Claude-3.5-Sonnet experiments for budget reasons and mention unstable DeepSeek tool calling as a reason not to use it. These are author-reported selection rationales. [A: p. 6, footnote; p. 17]

The four attacks are Direct, Ignore Previous Instructions, System Message, and Important Messages. The last is described as enhanced with user-name and model-version context. Baselines are DeBERTa Detector, a GPT-4o LLM Detector, Delimiting, Repeat Prompt, and Tool Filter. MELON-Aug combines MELON with Repeat Prompt. Detection-based approaches terminate the whole run on detection, but MELON acts on a proposed action whereas the content detectors inspect observations before action generation. [A: pp. 6–7]

No new training procedure, dataset split, random-seed list, repeated-run count, hardware profile, latency benchmark, confidence interval, or significance test is specified. The study is primarily an inference-time benchmark comparison. Approximately doubled model calls and API costs are reported; parallel execution and key–value caching are discussed as latency optimizations, without measured timing results. [A: pp. 5–9]

## 8. Experiments / Analyses

| ID | Purpose and configuration | Manipulated conditions | Outcomes and evidence |
|---|---|---|---|
| X1 | Main AgentDojo comparison, three models, four attacks | No defense, five baselines, MELON, MELON-Aug | BU, UA, ASR; T1, F1, F3 |
| X2 | Component ablation, GPT-4o, Important Messages | Original, Basic, No Cache, Full Comp. | BU/BN, UA, ASR; T2 |
| X3 | Prompt sensitivity, same restricted setup | Original, paraphrase, sentiment, grammar, translation | BU, UA, ASR; T3 |
| X4 | Threshold sensitivity, same restricted setup | θ = 0.5, 0.6, 0.7, 0.8, 0.9 | BU, UA, ASR; T4 |
| X5 | Benign false-positive analysis, GPT-4o AgentDojo | MELON, DeBERTa, LLM Detector | FPR and examples; §4.4, Appendix E |
| X6 | Missed-attack analysis, Important Messages, three models | Categorization of 66 evasions | Four failure shares; §4.5 |
| X7 | Additional detector diagnostics | Important Messages, Ignore Previous, System Message | Accuracy, FPR, FNR; T5 |

X1 uses the same benchmark framework to compare defense settings; no uncertainty estimates or statistical tests accompany the reported percentages. The 629 cases are benchmark combinations, not 629 independent users. The paper does not enumerate all task-pairing rules or per-domain result counts in Table 1. [A: pp. 6–8; D: sampling caution]

X2 tests the three proposed improvements one at a time. Relative to original ASR 0.95%, deleting Tu without Tf raises ASR to 2.70%; removing the cache raises it to 1.75%; comparing whole actions raises it to 17.33%. Higher utility in an ablated setting must be interpreted alongside its weaker attack prevention. [A: pp. 7–8]

X3 and X4 support limited robustness under one model–attack combination. They do not establish invariance across all models, languages, applications, or adaptive attacks. X5 examines the tension between faithful completion of delegated external instructions and conservative security intervention. X6 identifies important failure mechanisms, particularly attacks carried through text responses. X7 evaluates detection labels rather than end-to-end user utility, and therefore cannot be substituted for X1. [A: pp. 8–9, 18–20; D: scope interpretation]

The VWA-Adv discussion is a benchmark-selection analysis, not a full MELON evaluation. The authors report that pure image-based goal misdirection reaches only 1% ASR on GPT-4o and exclude the dataset. Its 200 adversarial tasks are therefore not additional evaluated MELON test cases. [A: pp. 6, 17–18]

## 9. Results

### Main average outcomes

The following entries reproduce Table 1 as BU / average UA / average ASR, all in percent. Average UA and ASR summarize the four attack types; BU is a separate no-attack measure. [A/B: p. 8]

| Defense | GPT-4o | o3-mini | Llama-3.3-70B |
|---|---|---|---|
| No Defense | 80.41 / 69.08 / 16.06 | 57.73 / 46.50 / 15.78 | 74.88 / 54.65 / 28.50 |
| Delimiting | 82.47 / 69.75 / 13.39 | 55.67 / 51.59 / 13.16 | 75.26 / 55.76 / 26.59 |
| Repeat Prompt | 83.51 / 77.86 / 9.18 | 53.61 / 46.38 / 6.72 | 72.16 / 62.56 / 18.32 |
| Tool Filter | 65.98 / 65.54 / 2.34 | 4.12 / 5.72 / 0.00 | 4.12 / 6.20 / 0.00 |
| DeBERTa Detector | 38.14 / 21.34 / 2.58 | 38.14 / 21.14 / 2.23 | 35.05 / 12.92 / 2.66 |
| LLM Detector | 81.44 / 0.00 / 0.00 | 81.44 / 0.00 / 0.00 | 81.44 / 0.00 / 0.00 |
| MELON | 68.04 / 58.78 / 0.24 | 50.52 / 36.29 / 0.95 | 63.92 / 46.30 / 1.27 |
| MELON-Aug | 76.29 / 68.72 / 0.32 | 55.67 / 37.28 / 0.56 | 67.01 / 52.94 / 0.72 |

MELON-Aug greatly reduces average attack success compared with no defense across all three models, but UA decreases in each comparison. For GPT-4o the decrease is small; for o3-mini it is substantial. The source's language about maintaining utility should therefore be read as retaining useful performance alongside low ASR, not as preserving every undefended metric. [A: pp. 7–8; D]

**Analyst-derived differences:** GPT-4o MELON-Aug reduces ASR by 16.06 − 0.32 = 15.74 percentage points, a relative reduction of 15.74 / 16.06 × 100 ≈ 98.01%. UA decreases by 69.08 − 68.72 = 0.36 percentage points. For o3-mini, ASR falls by 15.78 − 0.56 = 15.22 points while UA falls by 46.50 − 37.28 = 9.22 points. For Llama, ASR falls by 28.50 − 0.72 = 27.78 points while UA falls by 54.65 − 52.94 = 1.71 points. [C: T1, p. 8]

### Conditions hidden by averages

Attack behavior differs sharply by model. GPT-4o without defense has 51.03% ASR under Important Messages but only 3.50% under Direct. Llama without defense has 63.43% under Direct and only 6.20% under Important Messages. Thus the prose statement that Important Messages is most successful and Direct least successful is not universally supported across models. [A/B: pp. 7–8]

For GPT-4o, MELON and MELON-Aug both report 0.00% ASR for Direct, Ignore Previous, and System Message. Important Messages remains at 0.95% for MELON and 1.27% for MELON-Aug, explaining why augmentation slightly raises average ASR despite improving UA. For o3-mini, MELON-Aug's Direct UA is 26.55%, below plain MELON's 49.60%, even though its average UA is slightly higher. For Llama, MELON-Aug's Direct ASR remains 2.07%, versus 0.16% for both System Message and Important Messages. [A/B: p. 8]

A detector can achieve zero successful attacks while accomplishing no attacked user tasks. The LLM Detector does exactly that in Table 1: 0.00% UA and 0.00% ASR. Tool Filter likewise reaches zero ASR for o3-mini and Llama while leaving UA at 5.72% and 6.20%. These results support the need to inspect security and functionality jointly. [A: p. 7; B: p. 8]

## 10. Figure-by-figure interpretation

### Figure 1 — Aggregate security and utility

This is a scatter plot on page 1. The horizontal axis is UA in percent, approximately 0–100; the vertical axis is ASR in percent, approximately 0–25. Both are linear. The caption reports averaging over GPT-4o, o3-mini, and Llama-3.3-70B. Gray markers distinguish No Defense, Delimiting, Repeat Prompt, Tool Filter, DeBERTa Detector, and LLM Detector. Green markers represent MELON and MELON-Aug. A black star and arrow identify ideal performance near 100% UA and 0% ASR. [A/B]

The visible pattern places the proposed methods close to the bottom while retaining appreciable horizontal position; the LLM Detector is near the origin, illustrating complete loss of attacked utility. There are no error bars or uncertainty bands. Exact pooled coordinates are not labeled, so none are asserted here. The figure summarizes a trade-off, but its aggregate view hides model and attack variation shown in Table 1.

### Figure 2 — Original and masking paths

The page-4 diagram contains a benign example on the left and an injected example on the right. Original execution occupies the upper path, masking the lower. Rounded boxes separate agent generation and tool execution; arrows show observation copying and proposed-call comparison. The masked path uses the substitute prompt and accumulated external outputs. Its calls enter a cache. Green visual cues indicate benign continuation; red cues indicate attacker-directed behavior. [B]

In the benign example, the user requests agenda-related work and the masked branch produces no matching consequential calls. In the injected example, both paths propose attacker-related money transfer behavior, causing detection. The diagram explains the method rather than reporting measured success rates. Some text is small, so the nearby prose and Algorithm 1 provide the precise procedural account.

### Figure 3 — Separate model panels

The page-7 figure has three scatter panels: GPT-4o, o3-mini, and Llama-3.3-70B. UA (%) is horizontal and ASR (%) vertical. Scales are linear but differ: visible horizontal ticks reach 75 for GPT-4o, 40 for o3-mini, and 60 for Llama; vertical ticks reach 20, 15, and 30 respectively. These tick extents are not asserted as exact axis boundaries. Marker conventions follow Figure 1. [B]

The proposed methods sit near low ASR in all panels. Tool Filter and LLM Detector also achieve low ASR but often occupy low-UA positions. Repeat Prompt tends to retain substantial UA while leaving more attack success. No error bars are shown. The caption's broad statement that all other defenses exhibit a trade-off should not be interpreted as proving MELON has no cost: Table 1 shows its own BU and UA reductions. [A/B; D]

### Figure 4 — Basic agent feedback loop

On page 15, the user prompt feeds the agent system. The agent sends tool calls to tool execution; outputs return to the agent. A separate arrow reaches task completion when no calls remain. Icons illustrate people, an agent, and tools. This is an explanatory architecture diagram without numeric axes, measurements, or uncertainty. Its feedback arrow is important to the research question because external outputs repeatedly re-enter the decision process. [B; D: relevance inference]

## 11. Table-by-table interpretation

### Table 1 — Full defense comparison

Rows are grouped by model and defense. Columns distinguish no-attack BU from UA and ASR for Direct, Ignore Previous, System Message, and Important Messages, followed by averages. All values are percentages. Gray, yellow, blue, red, and green backgrounds identify undefended, prompt-based, tool-filtering, detector, and proposed-method categories. Arrows indicate higher utility and lower attack success are preferable. [A/B: p. 8]

The main averaged rows are reproduced in Section 9. Additional substantive conditions are: MELON's o3-mini System Message UA is 23.05%, despite ASR 0.79%; MELON-Aug raises that UA to 43.08% at the same ASR. Llama Repeat Prompt reaches UA 69.48% for System Message and 69.16% for Important Messages, with ASR 4.61% and 3.18%. Thus strong utility and strong security do not necessarily coincide. No significance marks, confidence intervals, or missing-value codes appear.

The LLM Detector BU is exactly 81.44% in all three model groups, including groups whose undefended BU differs. The supplied methods do not explain this identical value. It should be preserved as reported rather than silently corrected or used to infer an unreported execution configuration. The caption calls ASR 'average success rate,' while the main text defines 'Attack Success Rate'; the latter definition is used here.

### Table 2 — Component removal

For Original / Basic / No Cache / Full Comp., the first utility row is 68.04 / 69.07 / 67.01 / 78.35; UA is 32.91 / 32.43 / 29.41 / 39.27; ASR is 0.95 / 2.70 / 1.75 / 17.33, all percentages. The first row is visibly labeled BN rather than the paper's usual BU. Context suggests benign utility, but that interpretation is flagged rather than treated as a corrected source label. [A/B: p. 8]

Full-action comparison has the largest attack-success deterioration. Basic and No Cache also worsen ASR. These results support the three choices within GPT-4o under Important Messages, without establishing their universal necessity.

### Table 3 — Substitute-prompt variation

Original / Para. / Senti. / Grammar / Tran. have BU 68.04 / 68.04 / 69.07 / 67.01 / 70.10; UA 32.91 / 30.37 / 31.40 / 31.79 / 33.07; ASR 0.95 / 1.11 / 1.11 / 0.95 / 1.43. All are percentages. Original and Grammar tie for the lowest ASR; Translation has the highest BU and UA but also the highest ASR. [A/B: p. 8]

The range is relatively narrow in this setting, supporting reduced dependence on one exact prompt. The actual full texts of all four variants are not supplied, limiting exact reproduction. The weather values inside the few-shot example are demonstration content, not additional evaluation measurements.

### Table 4 — Similarity threshold

For thresholds 0.5 / 0.6 / 0.7 / 0.8 / 0.9, BU is 68.04 / 67.01 / 68.04 / 68.04 / 67.01; UA is 30.21 / 31.32 / 30.84 / 32.91 / 33.07; ASR is 0.95 / 1.11 / 0.95 / 0.95 / 0.95. Thresholds are unitless and results percentages. [A/B: p. 8]

Higher thresholds generally retain more UA, but the sequence is not strictly monotonic. The prose mentions minimal standard deviations without tabulating standard-deviation estimates. These rows are parameter settings, not error bars from repeated experiments.

### Table 5 — LLM-detector diagnostics

Important Messages reports accuracy 99.87%, FPR 0.00%, FNR 0.78%. Ignore Previous reports 99.74%, 0.31%, 0.00%. System Message reports 100.00%, 0.00%, 0.00%. Direct is absent. No counts, uncertainty estimates, or full aggregation procedure are supplied. [A/B: p. 20]

The following paragraph instead gives near-perfect Important-related performance as 99.98%. That conflicts with the table's 99.87%; neither is silently substituted for the other. The table describes classification performance, while Table 1 describes completed agent runs. Their percentages measure different outcomes.

## 12. Diagram / Architecture

Figure 4 supplies the underlying control loop: task → action proposal → tool execution → observation → revised action. Figure 2 adds a diagnostic branch at the proposal stage. Original observations are copied into a consolidated masked context. The masking branch produces hypothetical calls, the cache retains them, and a similarity check gates the original proposal. [A/B: pp. 4, 14–15]

The distinction between data and control is central. Retrieved outputs begin as data returned by tools. A successful injection causes their embedded directives to control the next proposal. MELON tests for this by deliberately asking another continuation to follow those directives and checking whether the actual proposal resembles its result. This is an interpretation of the architecture, not a verified causal identification theorem. [D]

The cache addresses temporal displacement: the original agent may complete legitimate work before attempting the malicious step, while the masked branch attempts it immediately. Comparison against historical masked proposals avoids requiring both branches to arrive at the same call at the same moment. Call-focused comparison removes differences in explanatory prose. These two mechanisms improve alignment between what is compared, but cannot help when the original harm appears only as text or when calls genuinely differ. [A: pp. 4–5, 9]

## 13. Equations and mathematical concepts

### E1 — State evolution, page 3 and Appendix B

St = (Tu, A1:t, O1:t), At+1 = π(St), and Ot+1 = Exec(Ct+1). Tu is the legitimate task; A1:t is prior generated actions; O1:t is prior tool outputs; π is the agent; Ct+1 is the next set of calls. This is a state-transition description, not an optimization objective. Appendix B initializes S0 = (Tu, ∅, ∅). Its execution expression uses Exec(At+1), whereas the main definition uses Exec(Ct+1). The intended pipeline executes calls, but the notation differs. [A: pp. 3, 14]

### E2 — Dependence intuition, page 3

For a successful attack, the authors write Pπ(At+1 | Tu, A1:t, O′1:t) ≈ Pπ(At+1 | O′1:t). Primes indicate attacker-modified observations. In plain language, removing the user task and earlier actions is expected to change little when the attacker-bearing outputs dominate the next action. For benign execution the source uses a much-greater-than comparison between analogous conditional probabilities. This is an informal motivation: it does not specify an action event, a distributional distance, or a measured test of conditional independence. [A; D: qualification]

### E3 — Two continuations, page 3

Ao_t+1 = π(St) and Am_t+1 = π(M(St)). Superscripts o and m distinguish original and masked actions. Each action includes a response R and calls C. M maps a full state to a masked state. These continuations operationalize the behavioral proposition using concrete model outputs.

### E4 — Masked state, page 4

M(Tu, A1:t, O1:t) = (Tf, ∅, O¹_t), where the final symbol denotes the consolidated sequence of tool outputs; the source's superscript/subscript layout is easier to understand through its explicit concat(O1:t) operation. The input is full state; the output retains observations while substituting Tf and deleting prior generated actions. [A/B]

### E5 — Cache and existential match, pages 4–5

Ht+1 accumulates masked call sets through the current step. Detection asks whether there exists an original call c and cached call h with sim(c,h) > θ. The existential operator means a single sufficiently similar pair is enough; all calls need not match. The strict inequality matters at the boundary. The cache stores proposed call information, not proof that a corresponding malicious task was completed. [A; D: distinction]

### E6 — Cosine similarity and alert, page 5

sim(c,h) = φ(c)·φ(h) / (||φ(c)|| ||φ(h)||). φ maps a serialized call to an embedding vector; the dot product measures alignment, normalized by vector lengths. Alertt+1 is true when any original/cached pair exceeds θ, normally 0.8. The paper does not specify zero-vector handling or every embedding-service option. It also does not prove that this score perfectly distinguishes authorization. [A; D]

### E7 — Ensemble detector, pages 5–6

H(Ao) = 1[(1/n) Σi d(Ao, Am_i) > θ]. Here H is a binary detector, distinct from the call-cache symbol Ht; n is the number of masking prompts; Am_i is the action using prompt Ti; d is a similarity measure; and 1[·] is an indicator returning 1 when its condition holds. The theoretical threshold is typically 0.5, separate from the implementation's 0.8 pairwise-call threshold. The ensemble averages scores rather than using Algorithm 1's any-pair rule. [A]

### E8 — Error bounds, page 6

For benign actions, P[(1/n)Σi d(Ao,Am_i) > θ] ≤ exp(−2n(θ−μB)²). For malicious actions, P[(1/n)Σi d(Ao,Am_i) < θ] ≤ exp(−2n(μV−θ)²). μB and μV are expected benign and malicious similarities. The stated separation condition is μB < θ < μV. The authors attribute these bounds to Hoeffding's inequality. [A]

The numeric example sets μB = 0.3, μV = 0.7, θ = 0.5, and n = 100, reporting approximately 1.8 × 10⁻⁴. Direct substitution gives exp(−2 × 100 × 0.2²) = exp(−8) ≈ 3.35 × 10⁻⁴. This is an analyst-derived discrepancy. The displayed false-negative event also uses < θ, whereas the binary rule returns benign at equality, so boundary handling is not fully aligned. [C/D]

The paper does not empirically establish the required expectation separation, report an n = 100 ensemble evaluation, or detail independence conditions across prompt-generated scores. The bounds therefore support a conditional ensemble argument; they should not be transferred automatically to the main cached, single-prompt detector. [D: evidence-based mathematical assessment]

## 14. Interpretation and discussion

The strongest supported empirical message is that evaluating a proposed action can preserve useful runs that a content detector would stop. If suspicious content appears but the original agent ignores it, a masked branch may propose an attacker call while the original does not. MELON then allows continuation. This explains why a detector can have high content-label accuracy yet zero attacked utility under a termination policy. [A: pp. 5, 7, 20]

The method's useful proxy is also its limitation. Similar calls do not necessarily mean unauthorized behavior: a user can legitimately ask an agent to follow a retrieved bill or task list. Conversely, dissimilar calls or absent calls do not establish safety: attacks may affect text responses or exploit state hallucination. The paper documents both directions of mismatch. [A: pp. 9, 18–20; D]

Several consistency issues limit broad claims. Important Messages is not strongest for every model; MELON-Aug does not always lower ASR relative to MELON; Appendix E's false-positive counts total eight while §4.4 reports nine; Table 5's accuracy conflicts with its prose; and the theoretical numerical example does not match direct substitution. These issues do not erase the large Table 1 differences, but they require qualified interpretation. [A/B/C]

For **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper supports a mechanism-focused analyst inference: retrieving attacker-controlled material introduces additional opportunities for instructions to enter, and tool permissions can convert a changed response into an external action. Repeated action–observation cycles can carry those instructions forward. However, the paper does not run a standalone-LLM control, measure a web-agent versus standalone risk ratio, or establish that every web agent is more vulnerable. The relevance is explanatory and architectural, not a direct comparative causal result. [D]

## 15. Contributions and novelty

**Conceptual:** the authors propose user-task independence of attacker-driven behavior as a detection signal. **Algorithmic:** they implement masked re-execution, a historical masked-call cache, and focused semantic call comparison. **Implementation:** they specify substitute prompts, few-shot examples, selected-argument serialization, embeddings, and an inference-time threshold. [A: pp. 2–5, 12–14]

**Theoretical:** they extend the idea to multiple masking prompts and present conditional exponential error bounds. **Empirical:** they compare three models, four attacks, five defenses, two proposed configurations, and targeted ablation and diagnostic analyses. [A: pp. 5–9]

There is no claimed new dataset: AgentDojo and VWA-Adv are existing resources. The page-1 repository link is an availability statement, not evidence that the implementation was reproduced here. The authors' claim to be the first detector using the independence property is reported as their novelty claim; priority was not externally verified. [A: pp. 1–2; D]

## 16. Limitations

### Authors' stated limitations

The paper explicitly identifies response-based attacks, redundant tool calls, state hallucination, and nonexistent-function calls as evasion mechanisms. Across 66 Important Messages evasions, their reported shares are 72.73%, 15.15%, 6.06%, and 6.06%. Response-only harms are particularly consequential because the detector focuses on calls. [A: p. 9]

The masking branch approximately doubles model calls and API costs. Embedding-service response time contributes latency; proposed parallelization and caching do not come with measured latency improvements. Benign utility decreases in some cases, especially where users ask the agent to execute external instructions. The impact statement acknowledges imperfect security and evolving attacks. Budget limits restrict model coverage, and the multimodal benchmark is excluded. [A: pp. 5–6, 9, 17–18]

### Additional evidence-based analyst observations

[D] The conditional ensemble bounds require independent bounded similarity variables and the stated separation of benign and malicious means. The implemented single masked continuation is not this multi-prompt ensemble. Raw cosine similarity can range from -1 to 1; the paper does not specify a rescaling or dependence analysis sufficient to transfer the displayed Hoeffding constants to correlated LLM responses. This is a limitation of applying the conditional argument, not an empirical refutation of Table 1.

[D] The 66 Important Messages evasions in Section 4.5 do not have a reconciled sampling denominator. Under a single 629-case pass, the displayed MELON rates in Table 1 correspond approximately to 6 GPT-4o, 11 o3-mini, and 5 Llama successes, or 22 in total. No three-repetition protocol is stated that would justify multiplying this to 66. Moreover, nonexistent-function calls and hallucinated state are not automatically completed harmful actions, despite the earlier all-required-steps ASR criterion. Retain the reported taxonomy and counts as author-reported diagnostic evidence; do not convert all 66 into verified executed compromises. [Sources: pp. 6–9, Table 1.]


The main evaluation does not establish security against an attacker optimizing specifically against MELON. No uncertainty estimates, repeated-run protocol, or significance tests are provided. Ablation and sensitivity tests are restricted to GPT-4o under Important Messages. Serialization deliberately discards email subject and body, so distinct content-related intentions can share a representation; the paper does not isolate that trade-off experimentally. [D]

The actual few-shot construction and full prompt are more operationally specific than the phrase task-neutral suggests. Precise embedding version, cache initialization and reset policy, maximum-step values, baseline thresholds, and masked-branch isolation are insufficiently specified for exact reproduction. The theoretical ensemble is not the same decision procedure as the evaluated cache detector. These are limitations of the supplied evidence, not author admissions. [D]

## 17. Threats to validity

**Internal validity — analyst assessment:** defenses differ in intervention timing and termination consequences. Those differences are part of their real behavior, but they mean content-classification accuracy and completed-task utility answer different questions. The identical LLM Detector BU across model groups is unexplained. The study does not isolate every implementation choice or report repeated-run variation. [D: pp. 6–8, 20]

**Construct validity — analyst assessment:** similarity of proposed calls is a proxy for attacker control. Legitimate delegated instructions can satisfy the proxy, while response-based harms can avoid it. Benchmark success requires all malicious steps to be executed; attempted or partial harms may therefore be absent from ASR. [A: pp. 6–7, 9; D]

**External and ecological validity — analyst assessment:** results concern four AgentDojo domains and chosen text templates. They do not cover unrestricted production browsing, the full diversity of web interfaces, all multimodal attacks, or every model. VWA-Adv exclusion narrows conclusions about visual web-agent security. [D: pp. 6, 17–18]

**Statistical conclusion validity — analyst assessment:** results are point percentages without confidence intervals, significance tests, or reported independent repetitions. Temperature 0 is a configuration choice, not a demonstrated guarantee of invariant executions. Benchmark cases can share tasks and templates, so independence should not be presumed. [D]

**Reproducibility — analyst assessment:** prompts and pseudocode improve transparency, but the uninspected code link cannot fill missing runtime configuration. Classification denominators, complete prompt variants, model snapshots, software versions, and measured computational costs remain incompletely documented in the supplied paper. [D]

## 18. Future work and open questions

### A. Explicit author proposals

The authors propose extending detection beyond direct task manipulation, improving masked re-execution efficiency through key–value caching and selective state masking, and combining behavioral detection with other defenses. They also anticipate more effective image-based attacks that could make the excluded visual benchmark more informative. [A: pp. 9, 17–18]

### B. Additional open questions

Analyst questions include how to detect harmful text without losing the benefit of call-focused comparison; how to distinguish authorized delegation from attacker-driven instructions; whether prompt ensembles actually satisfy the separation and concentration assumptions; how an adaptive attacker would respond; and how cache growth affects cost and spurious matches. Further questions concern recipient/body serialization trade-offs and how to isolate a branch deliberately prompted to follow untrusted instructions. [D]

For the user's comparative research question, a direct experiment remains open: use matched tasks, adversarial content, models, permissions, and outcome definitions to compare standalone and agent configurations. This is a proposed study design inferred from the evidence gap, not an experiment reported by MELON. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model, the text-generating component |
| Agent π | Model plus tools and execution logic |
| IPI | Indirect prompt injection through retrieved material |
| MELON | Masked re-Execution and TooL comparisON |
| MELON-Aug | MELON combined with Repeat Prompt |
| Tu / Tm | Legitimate user task / attacker task |
| Tf / Ti | Substitute masking prompt / an ensemble prompt |
| St | Current task, generated-action history, and observations |
| At = (Rt,Ct) | Action containing response text and tool calls |
| Ot / O′t | Tool output / attacker-modified tool output |
| M | State-masking function |
| Ht | Cache of masked proposed calls |
| φ | Call-to-embedding mapping |
| sim / d | Similarity score used in detection |
| θ | Decision threshold; implementation and ensemble use different settings |
| Ao / Am | Original / masked proposed action |
| BU | Benign utility without attacks |
| UA | Successful legitimate work while avoiding malicious execution under attack |
| ASR | Fraction of attacks completing their malicious objective |
| FPR / FNR | False-positive rate / false-negative rate |
| μB / μV | Expected benign / malicious ensemble similarity |
| n | Number of masking prompts in the theoretical ensemble |
| Few-shot examples | Demonstrations included in context to guide behavior |
| Embedding | Vector representation used for semantic comparison |
| KV cache | Key–value cache, discussed as a latency optimization |
| SOTA | State of the art, the authors' characterization of comparators |

DeBERTa is supplied as a model name; the paper does not expand that name. Appendix F's heading uses FPN, whereas the table reports FPR. FPN is not separately defined and is not assigned a new meaning here.

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| AgentDojo legitimate tasks | 97 | tasks | 16 banking + 21 Slack + 20 travel + 40 workspace | Author-reported | 6, 17 |
| Security cases | 629 | cases | Benchmark task/attack combinations | Author-reported | 6, 17 |
| Models / attacks / baseline defenses | 3 / 4 / 5 | counts | Main comparison | Author-reported | 6 |
| Temperature | 0 | setting | All evaluated agent models | Author-reported | 6 |
| Main similarity threshold | 0.8 | unitless | Pairwise embedding comparison | Author-reported | 5 |
| Model-call/API-cost increase | approximately 2× | multiplier | Compared with undefended execution | Author-reported | 5 |
| GPT-4o no-defense UA / ASR | 69.08 / 16.06 | % | Four-attack average | Visually readable | 8, T1 |
| GPT-4o MELON UA / ASR | 58.78 / 0.24 | % | Four-attack average | Visually readable | 8, T1 |
| GPT-4o MELON-Aug UA / ASR | 68.72 / 0.32 | % | Four-attack average | Visually readable | 8, T1 |
| o3-mini MELON-Aug UA / ASR | 37.28 / 0.56 | % | Four-attack average | Visually readable | 8, T1 |
| Llama MELON-Aug UA / ASR | 52.94 / 0.72 | % | Four-attack average | Visually readable | 8, T1 |
| GPT-4o augmented ASR reduction | 15.74 | percentage points | 16.06 − 0.32 | Analyst-derived | 8, T1 |
| GPT-4o augmented relative ASR reduction | approximately 98.01 | % | (16.06 − 0.32) / 16.06 × 100 | Analyst-derived | 8, T1 |
| MELON / DeBERTa / LLM FPR | 9.28 / 61.86 / 0.00 | % | GPT-4o benign-operation analysis | Author-reported | 9 |
| Missed attacks analyzed | 66 | cases | Important Messages, three models | Author-reported | 9 |
| Response-based failure share | 72.73 | % | Of 66 evasions | Author-reported | 9 |
| Redundancy / state / function failure shares | 15.15 / 6.06 / 6.06 | % | Same evasion analysis | Author-reported | 9 |
| Image-only goal-misdirection ASR | 1 | % | GPT-4o VWA-Adv selection discussion | Author-reported | 17 |
| Illustrative ensemble bound | approximately 1.8 × 10⁻⁴ | probability | Authors' n = 100 example | Author-reported | 6 |
| Substitution into displayed bound | approximately 3.35 × 10⁻⁴ | probability | exp(−8), same example | Analyst-derived | 6 |

All table values retain their reported precision. Percentages are not converted to counts unless explicitly derived. For example, Appendix E's domain counts sum to 3 + 3 + 0 + 2 = 8, which conflicts with the nine cases reported in §4.4; no replacement count is asserted.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / strength |
|---|---|---|---|---|
| Retrieved content can redirect agents | Threat model and concrete file/web/email examples | F4, Appendix C | 1, 3, 14–17 | Strong support for the studied mechanism |
| Masked comparison operationalizes task-dependence testing | State masking, cache, call similarity | ALG1, F2 | 3–5 | Strong method documentation; proxy is imperfect |
| Proposed methods reduce average ASR | Three-model results against four attacks | T1, X1 | 8 | Strong within benchmark; no uncertainty estimates |
| Augmentation improves utility–security balance | GPT-4o 68.72% UA, 0.32% ASR | T1, X1 | 7–8 | Plain MELON has lower ASR, 0.24% |
| Three design choices improve detection | Component-removal ASR increases | T2, X2 | 7–8 | One model and attack condition |
| Prompt/threshold changes have modest effects | Restricted sensitivity tables | T3–T4, X3–X4 | 8–9 | Does not establish universal robustness |
| Tool-only comparison misses response harms | 72.73% of analyzed evasions | X6 | 9 | Share of failures, not all attacks |
| Benign delegation can trigger MELON | FPR and bill/task-list examples | X5, Appendix E | 9, 18–20 | Authors call these risky; benchmark still counts false positives |
| Ensemble error decreases under separation assumptions | Displayed concentration bounds | E7–E8 | 5–6 | Conditional, distinct from main implementation |
| Agents expose a retrieval-to-action risk path | External observations feed executable calls | F2, F4 | 3–4, 14–15 | Analyst relevance inference, not standalone comparison |

Source-grounded checks preserve several unresolved discrepancies: page 3 calls the embedding quantity a distance while the operational rule uses high similarity; page 4's cache update notation is self-referential; Table 2 uses BN; the ensemble example's arithmetic differs from its formula; false-positive counts disagree; and Table 5 accuracy disagrees with nearby prose. Appendix C templates also do not exactly reproduce the attack names/prefixes described in §4.1. These discrepancies are reported rather than silently repaired.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read your schedule. A malicious note hidden in the schedule says to send money to someone else. The assistant has two problems: recognizing that the note is an instruction from an untrusted source, and avoiding using its tools to carry it out.

MELON makes a second proposed continuation that does not know your original request. It sees the retrieved material and is prompted to follow instructions there. If your real assistant proposes essentially the same tool action as this second continuation, MELON treats that match as a warning and stops the original action before execution. It remembers earlier proposals because the real assistant might reach a malicious step later.

This worked well against the paper's selected attacks, but it has costs. It needs extra model calls, can stop legitimate work that involves following a bill or task list, and can miss harmful answers that do not use tools. The mathematical guarantee also depends on assumptions about how an ensemble of prompts behaves.

For web-agent security, the important lesson is that outside text can influence something capable of taking actions. That helps explain a source of agent risk. This paper does not directly test whether agents are more vulnerable than standalone chat models, so it cannot supply that comparative conclusion by itself.

## Completeness Audit

The denominator is the supplied 20-page inventory, including main sections, substantive subsections, four figures, five tables, Algorithm 1, eight mathematical groups, seven analysis groups, and Appendices A–F. Coverage is of the supplied material; it is not a claim of external reproduction or verified completeness of separate artifacts.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, affiliations | Yes, text and image | Yes | Fully represented | Section 2 |
| Abstract | Yes, text and image | Yes | Represented in compressed form | Orientation and contributions |
| S1 Introduction | Yes, text and images | Yes | Fully represented | Problem and gap |
| S2 Related Work | Yes; p. 3 text only | Yes | Represented in compressed form | Categories and selected contrasts |
| S3.1 Preliminaries/threat model | Yes, text only | Yes | Fully represented | Sections 6, 13 |
| S3.2 Technical overview/challenges | Yes, text and images | Yes | Fully represented | Three design choices and failure rationale |
| S3.3 Technical details | Yes, text and image | Yes | Fully represented | Algorithm and similarity |
| S3.3.1 Implementation/overhead | Yes, text and image | Yes | Fully represented | Missing specifications disclosed |
| S3.4.1 Ensemble | Yes; p. 6 text only | Yes | Fully represented | Distinguished from main detector |
| S3.4.2 Error bounds | Yes, text only | Yes | Fully represented with uncertainty | Assumptions and arithmetic flagged |
| S4.1 Setup and model-selection footnote | Yes, text only on p. 6 | Yes | Fully represented | Model, benchmark, exclusions, metrics |
| S4.2 Results | Yes, text and image | Yes | Fully represented in synthesis | All averaged rows; selective per-attack values |
| S4.3 Ablation and sensitivity | Yes, text and images | Yes | Fully represented | Tables 2–4 transcribed |
| S4.4 False positives | Yes, text only | Yes | Fully represented | Count discrepancy retained |
| S4.5 Attack successes | Yes, text only | Yes | Fully represented | Four shares and mechanisms |
| S5 Conclusion/future work | Yes, text only | Yes | Fully represented | No universal-security claim adopted |
| Impact statement | Yes, text only | Yes | Represented in compressed form | Cost and imperfect security |
| Acknowledgements | Yes, text only | Yes | Represented in compressed form | Funding provenance noted below |
| References, pp. 9–11 | Yes; p. 11 also visual | Yes | Inspected but compressed as bibliographic material | No citation validation |
| Formal research questions/hypotheses | Checked | Yes | Absence represented | Informal objectives kept separate |
| X1 Main comparison | Yes | Yes | Represented in compressed form | Full averages, selected attack-specific rows |
| X2–X4 Ablation/prompt/threshold | Yes | Yes | Fully represented | All table cells reproduced |
| X5 False positives | Yes | Yes | Fully represented | Counts, FPR, example patterns |
| X6 Evasion analysis | Yes | Yes | Fully represented | All categories and shares |
| X7 LLM diagnostics | Yes | Yes | Fully represented | All T5 values and inconsistency |
| F1 Aggregate scatter | Yes, visually | Yes | Fully represented | No invented exact coordinates |
| F2 MELON pipeline | Yes, visually | Yes | Fully represented | Method diagram, not performance evidence |
| F3 Three model panels | Yes, visually | Yes | Fully represented | Different scales and no error bars |
| F4 Basic agent loop | Yes, visually | Yes | Fully represented | Control and observation feedback |
| T1 Main results | Yes, visually and text | Yes | Represented in compressed form | All averages; not all 288 numeric cells repeated |
| T2 Component ablation | Yes, visually and text | Yes | Fully represented | BN label flagged |
| T3 Prompt sensitivity | Yes, visually and text | Yes | Fully represented | Variant text unavailable |
| T4 Threshold sensitivity | Yes, visually and text | Yes | Fully represented | No reported error estimates |
| T5 Detector diagnostics | Yes, visually and text | Yes | Fully represented | Direct attack absent |
| ALG1 | Yes, visually and text | Yes | Fully represented | Cache update ambiguity disclosed |
| E1–E6 Operational equations | Yes; p. 3 text only | Yes | Fully represented | Notational differences flagged |
| E7–E8 Ensemble and bounds | Yes; p. 6 text only | Yes | Fully represented with qualifications | No full independence specification |
| A.1 Complete masking prompt | Yes, visually and text | Yes | Represented in compressed form | File read, follow-first, avoid-repeat clauses |
| A.2 Few-shot examples | Yes, visually and text | Yes | Represented in compressed form | Benign summary and reused weather results |
| A.3 Serialization | Yes, visually and text | Yes | Fully represented | All function-specific rules |
| B Agent pipeline | Yes, visually and text | Yes | Fully represented | Exit conditions and notation |
| C.1.1–C.1.4 Attack examples | Yes; p. 16 text only | Yes | Represented in compressed form | Common financial-transfer objective |
| C.2.1–C.2.5 Defenses | Yes; p. 16 text only | Yes | Fully represented in synthesis | Detector, delimiters, repeats, whitelist |
| D.1 AgentDojo | Yes, visually and text | Yes | Fully represented | 97 tasks, 629 cases |
| D.2 VWA-Adv | Yes, visually and text | Yes | Fully represented | Exclusion, 200 tasks, 1% ASR |
| E.1 DeBERTa example | Yes, visually and text | Yes | Represented in compressed form | Benign hotel rating/reviews |
| E.2 MELON examples | Yes, visually and text | Yes | Represented in compressed form | Bill, web task list, embedded email |
| F Detector analysis | Yes, visually and text | Yes | Fully represented | T5 and prose discrepancy |
| Major contributions | Yes | Yes | Fully represented | Conceptual through empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Failures, cost, imperfect security, scope |
| Supplied supplementary files | None supplied | Yes | Absence represented | Linked repository not reviewed |

### Missing or inaccessible material

No physical page is missing from the supplied 1–20 sequence. Visual renderings of pages 3, 6, 9, 10, and 16 were not supplied; those pages have text-only coverage. The code repository, exact execution environment, raw trajectories, complete per-case outcomes, full alternative masking prompts, and independent supplementary files were not supplied or inspected. Their availability elsewhere is not assumed. Exact model snapshots, seed/repetition protocols, baseline tuning settings, and measured timing data cannot be recovered from the supplied paper alone.

### Uncertain interpretations

The theoretical score assumptions and applicability of the concentration bound are incompletely specified. The displayed bound and numerical example disagree. False-positive totals differ between §4.4 and Appendix E. Table 5 and its paragraph disagree on accuracy. Identical LLM Detector BU across model groups is unexplained. Table 2's BN label likely refers to BU, but remains a source-label uncertainty. The meaning of distance versus similarity on page 3, the cache update line, no-call string handling versus empty-set iteration, and the precise correspondence between Appendix C examples and §4.1 attack prefixes remain unresolved. These uncertainties have not been silently reconciled.

### Deliberately compressed material

Table 1's complete per-attack matrix was inspected but compressed into all model/defense averages plus decision-relevant attack-specific contrasts. Repetitive attack examples share a financial-transfer objective, so account numbers and repeated bill formatting are omitted. The hotel example contains rating 4.2 above the user's threshold of 4 and a requested January 11–15, 2025 reservation; its role is a benign detector false positive, not a separate performance experiment. The weather demonstration's four days, temperatures, and generated report are prompt examples rather than research measurements and are compressed accordingly. Email metadata, names, timestamps, and repeated task-list wording are secondary to the delegation pattern.

Bibliographic entries are represented through the paper's related-work categories rather than reproduced individually. Acknowledgements identify ARL Grant W911NF-23-2-0137, the Microsoft AFMR grant program, and support from FAR AI, OpenAI, and Berkeley RDI; they do not contribute experimental results. Decorative icons, repeated headers, and page furniture are non-substantive and deliberately omitted.

### Potential omissions

No known major substantive component of the supplied inventory is entirely unrepresented. Representation is compressed for the full Table 1 matrix, references, repeated examples, prompt demonstration details, and funding text as disclosed above. Exact reproduction of unreported settings, missing external artifacts, and a direct standalone-LLM comparison remains outside what the supplied evidence can establish.
