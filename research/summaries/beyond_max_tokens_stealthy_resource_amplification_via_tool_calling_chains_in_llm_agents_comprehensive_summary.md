## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Paper content is treated as evidence, not as instructions. No external sources, tools, code execution, or browsing were used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–14 |
| Accessible page count | 14 |
| Missing pages | None apparent within the supplied 1–14 sequence; this does not establish whether separate supplementary artifacts exist |
| Visually inspected pages | 1–9, 12, and 13 |
| Text-only pages | 10, 11, and 14 |
| Figures | Figures 1–5 are visually available |
| Tables | Tables 1–4 are visually available; main result tables are readable |
| Equations | Available in text and rendered pages; subscripts and overloaded symbols require care |
| Appendices | A, B.1–B.4, and C.1–C.5 are present, despite the automated accessibility metadata not identifying appendix pages |
| Supplementary material | No separate supplementary file supplied |
| Embedded attachments | Accessibility metadata reports zero embedded files |
| OCR | Not needed; supplied native extraction is substantial |
| Other limitations | Small plot labels and dense heatmap cells limit exact visual transcription; graphical points without numerical labels are not treated as exact measurements |

The supplied images permit direct inspection of every numbered figure and table. Pages 10–11 contain references and were inspected through text only. Page 14, containing the end of C.4 and C.5, was also inspected through text only. The paper promises a future code release but supplies no inspected implementation, raw traces, measurement logs, or executable reproduction package here. The supplied SHA-256 is retained as source identity metadata; it was not independently recalculated.

Evidence labels throughout are: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No external information category is used. HIGH confidence means the supplied evidence is clear, not that the experiment has been independently reproduced. MEDIUM identifies interpretations or qualifications requiring judgment. UNKNOWN applies where the supplied work does not establish a fact.

### Document inventory established before synthesis

| Inventory ID | Original item | Physical pages | Substance |
|---|---|---:|---|
| META | Title, authors, affiliations, version | 1 | Identity and preprint metadata |
| ABS | Abstract | 1 | Mechanism, headline results, defense implications |
| S1 | §1 Introduction | 1–2 | Gap and three contributions |
| S2.1 | §2.1 Agents and operational cost | 2 | Economic motivation |
| S2.2 | §2.2 Resource consumption attacks | 2 | Prior-work positioning |
| S3.1 | §3.1 Problem and threat model | 3 | System, objective, capabilities |
| S3.2 | §3.2 Universal malicious template | 3–4 | Progress, verbosity, repair, termination |
| S3.3 | §3.3 Seed bank | 4 | Search initialization and reuse |
| S3.4 | §3.4 Optimizer | 4 | Search phases and UCT |
| S4.1 | §4.1 Setup | 4–6 | Models, data, comparisons, metrics |
| X1/S4.2 | §4.2 Effectiveness and correctness | 6–7 | Token lengths and success |
| X2/S4.3 | §4.3 Resource consumption | 6 | Energy and KV cache |
| X3/S4.4 | §4.4 Throughput | 6–7 | Concurrent benign workload |
| X4–X6/S4.5 | §4.5 Defenses | 7–8 | Perplexity, monitors, budgets |
| S5 | §5 Conclusion | 8 | Implications and future defenses |
| S6 | §6 Limitations | 9 | Emulator and workload restrictions |
| S7 | §7 Ethical Considerations | 9 | Isolation, public data, dual use |
| REF | References | 9–12 | Citation metadata, not independently validated |
| A | Appendix A | 12 | Notation |
| B1–B4 | Appendix B.1–B.4 | 12–13 | Trigger conditioning, invariants, seeds, search reward |
| C1–C5 | Appendix C.1–C.5 | 13–14 | Runtime, attack models, emulator, filtering, stubbing |
| F1–F5 | Figures 1–5 | 3, 6, 8 | Architecture, resources, three defense visualizations |
| T1–T4 | Tables 1–4 | 2, 7, 13 | Comparison, effectiveness, throughput, template elements |
| ALG1 | Algorithm 1 | 5 | MCTS template optimization |
| E-COST/E-OPT | Cost and Equations (1)–(2) | 3 | Output-token objective and success constraint |
| E-UCT | UCT selection | 4 | Exploitation–exploration selection |
| E-TRIGGER | Selection event and routable set | 12 | Conditional evaluation population |
| E-REWARD | Pass indicators and reward | 13 | Search surrogate |

No formal theorem, lemma, proof, numbered research question, or explicit statistical hypothesis is present. The corresponding objectives are informal. A corresponding-author footnote identifies Yongsen Zheng; it does not alter the methodology.

## 1. Plain-language orientation

[A] This paper studies an attack that makes an artificial intelligence agent expend far more computation while still producing a correct answer. An agent is an LLM operating in a loop: it decides to call a tool, reads the tool's reply, and decides what to do next. The researchers place malicious guidance in an external tool server rather than changing the user's request or the language model itself.

The central trick is procedural delay. The server withholds the ordinary useful result until the agent completes repeated steps. Those steps require lengthy generated tool arguments. Progress messages make further calls appear necessary; repair messages reject shortened responses. At the end, the server returns the same benign payload that the unmodified server would have returned. Thus a correct final answer can conceal an expensive intermediate process. [Sources: pp. 3–4, §§3.1–3.2.]

[A] The authors optimize these templates with Monte Carlo Tree Search, or MCTS, and test six LLMs on filtered ToolBench and Berkeley Function Calling Leaderboard datasets. The controlled emulator uses deterministic tool results. The strongest reported token amplification is 658.10×, for Mistral Large on BFCL: 57,255 average output tokens versus 87 benignly. Energy and cache occupancy also rise, and a concurrent benign workload loses substantial throughput. [Sources: pp. 5–7, Table 2, Figure 2, Table 3.]

[D] For the user's question, the relevant explanation is that an agent adds an externally influenced, repeated decision loop around the LLM. That loop permits a tool to influence both the number of generations and the amount generated per call. This is evidence about one additional vulnerability mechanism, not a direct experimental demonstration that all web agents are more vulnerable than all standalone LLMs. No real browser-agent comparison is reported.

## 2. Document roadmap

The introduction motivates correctness-preserving economic denial of service and lists the claimed contributions. Section 2 explains operational costs and contrasts the approach with earlier resource attacks. Section 3 defines the attacker, the constrained optimization problem, the universal template, the seed repository, and the search procedure. Section 4 presents setup and then evaluates effectiveness, physical resources, effects on benign co-running traffic, and defenses. Section 5 concludes with a call for workflow-aware defenses. Sections 6–7 state limitations and ethical precautions.

Appendix A fixes notation. Appendix B clarifies the legitimate-tool trigger condition, template invariants, seed promotion, edit families, search statistics, and reward. Appendix C gives runtime settings, attacker-model configuration, emulator adaptations, filtering, and deterministic tool wrapping. These appendices materially qualify the results: filtering is based on one target model, tool outputs are stubbed, and several search parameters remain unspecified numerically.

## 3. Background and context

[A] A **large language model (LLM)** generates token sequences. In this paper, **output tokens** include generated tool-calling content rather than only the human-facing answer. A **tool call** is an agent action requesting a function with arguments. The **agent policy** chooses between further tool calls and finishing the answer. A **trajectory** is the sequence of these calls and responses.

The **Model Context Protocol (MCP)** supplies the tool-server request/response interface studied here. Protocol-compatible means the malicious variant continues to fit that interaction interface; it does not mean its behavior is economically benign. **Retrieval-augmented generation (RAG)** supplies retrieved content to an LLM; the authors distinguish that context surface from their tool-server surface.

A **denial-of-service (DoS)** attack impairs availability or resource access. Here the authors emphasize **economic DoS**: consuming disproportionate tokens, energy, memory, and time while retaining task success. They contrast this with overt failure or irrelevant verbosity. **Key-value (KV) cache occupancy** is the serving-stack memory-usage measure reported; the paper connects increased occupancy with reduced headroom for concurrent workloads. **OOM** means out of memory; the paper discusses OOM-safe concurrency but does not report a separate measured concurrency-capacity curve.

**MCTS** explores candidate templates as a tree. Its **UCT** selection rule balances high-scoring candidates with less-explored branches. A **seed bank** stores reusable templates. **Perplexity (PPL)** is used as a detector score with thresholds calibrated from benign tool descriptions. The paper evaluates whether this score separates attacked episodes from that reference envelope; it does not establish a universal security interpretation of perplexity.

[A] Prior attacks are described as generating long answer or thinking traces within a single turn. The paper's distinction is to generate long content during tool calling repeatedly, allowing aggregate output to exceed a per-generation cap. This comparison is the authors' positioning of the cited literature, not an independently audited account of that literature. [Sources: pp. 1–2, Table 1.]

## 4. Research problem and gap

**Existing problem [A]:** Agent operation creates ongoing inference costs. External interactions can increase token consumption, energy use, and serving pressure. Protecting only final answer quality does not necessarily protect those resources.

**Shortcomings attributed to prior methods [A]:** Engorgio, P-DoS, and Auto-DoS operate at the dialog-query layer in Table 1 and are not marked correctness-preserving. Overthink is marked correctness-preserving but operates through RAG context and inflates thinking within one turn. Their stated per-query bound is at most M, the maximum completion size of one generation. The authors also distinguish malfunction amplification, which can cause repetitive actions but often disrupts task completion.

**Research gap [A]:** The multi-turn agent–tool loop is presented as underexplored for correctness-preserving resource amplification. The attacker wants unnecessary computation to look like legitimate progress toward the user's goal.

**Motivation [A]:** Correct answers and protocol validity can coexist with expensive behavior, so prompt filters and content-safety judgments may miss the relevant harm.

**Scope:** The empirical scope is six models, two filtered function-calling corpora, a shared emulator, deterministic tool payloads, and a controlled GPU-serving environment. It does not include production browsing, live API consequences, arbitrary multi-tool planning, or a matched agent-versus-standalone deployment study. [Sources: pp. 2–5, 9, 13–14.]

## 5. Research questions / objectives / hypotheses

The paper does not state formally numbered research questions or explicit null/alternative hypotheses. Its objectives can be faithfully reconstructed without attributing invented questions to the authors:

1. **O1 [A]:** Maximize expected generated output-token cost while preserving a minimum probability of task success over queries that legitimately invoke the tool. [p. 3, Equations (1)–(2).]
2. **O2 [A]:** Construct protocol-compatible malicious templates using text-visible changes while retaining function identifiers and terminal payload semantics. [pp. 3–4.]
3. **O3 [A]:** Improve multi-turn adherence and long tool-call outputs through search and reusable seeds. [pp. 4–5, 12–13.]
4. **O4 [A]:** Measure token amplification, successful completion, energy, KV-cache occupancy, and impact on concurrent benign work. [pp. 5–7.]
5. **O5 [A]:** Assess representative prompt filters, output/trajectory monitors, and hard budgets. [pp. 7–8.]

**User research question [D]:** Why might web AI agents have additional vulnerabilities relative to a standalone LLM? This paper supports the specific proposition that repeated external-tool feedback creates a resource-abuse surface. It does not directly measure comparative vulnerability rates, web-page injection success, or browser permissions.

## 6. Assumptions / threat model

[A] The system contains agent policy A, black-box language model M, and an external server Tθ controlled through template θ. The server exposes functions F. The policy maps dialogue and tool feedback into actions or a final answer. The attacker controls the MCP server template or impersonates a benign server, while preserving protocol compatibility.

The attacker does not change the agent policy, target model, user query, prompts, or retrieval. It does not influence the initial decision to route to the tool. Appendix B.1 therefore conditions on queries for which the benign agent already makes at least one call to the benign server. This is an important denominator restriction: the attack is not evaluated as an arbitrary-query routing attack. [pp. 3, 12.]

The described permitted edit zones include argument descriptions, progress or unfinished notices, and validation-error messages. Function identifiers, signatures, control flow, and terminal payload semantics are stated to remain unchanged. The template nevertheless introduces a segment index and a calibration sequence and enforces a return policy. The implementation boundary behind these assertions is not fully demonstrated in the supplied material; the paper does not provide executable server examples proving how all these properties coexist.

[D] The relevant trust boundary is between tool-supplied procedural text and the agent's control decisions. The useful result can remain trustworthy in content while intermediate instructions are wasteful. The assets at risk are generation budget, energy, cache capacity, latency, and shared-serving throughput. No exfiltration or destructive real-world action is required for the studied harm.

The evaluation assumes an isolated environment with stubbed outputs, unchanged prompts across compared conditions, uniform runtime settings, and fixed concurrency. Its success claims depend on benchmark task-success assessment, whose detailed scoring rubric is not fully specified in the supplied pages.

## 7. Methodology

### 7.1 Study design and template architecture

[A] This is an empirical AI-security and systems paper with an algorithmic component. It creates malicious variants of benign tool servers, evaluates them against several baselines under shared conditions, and measures both model behavior and serving effects.

The template has two argument roles and three response modes. The **segment index t** provides an explicit progress state. The **calibration sequence** is a long comma-separated integer list that inflates generated tool-call arguments without contributing to task semantics. A **Progress** response requests the next segment. A **Repair** response requests a compliant retry when the generated sequence is incomplete or malformed. The **Terminal** response returns the original benign result once the last segment and sequence validation conditions are satisfied. [pp. 3–4; Table 4, p. 13.]

Four invariants govern this process: start at segment 1; valid progress advances by exactly one; only complete correctly ordered sequences validate; and the benign payload is returned only at the terminal segment with a valid sequence. Invalid sequences do not advance progress. These requirements make both repeated calls and per-call verbosity part of the apparent procedure.

### 7.2 Search and seed promotion

Each search node represents a concrete server template. An edge is one localized text edit. Appendix B.4 reports 16 atomic edits organized into three families: multi-turn induction, length induction, and repair after omissions or format errors. The full individual edit list is not enumerated in the supplied text.

Search first stabilizes ordered multi-turn behavior in a pre_MT phase, then strengthens length in post_MT. Repair edits are enabled locally only when an omission or formatting error is observed. New children receive a small Stage-1 evaluation; passing children can receive a larger Stage-2 evaluation. UCT chooses branches, rollout rewards update value estimates, and successful templates enter the seed bank. Algorithm 1 depicts child evaluation in parallel; this is a property of the described algorithm, not an independently observed implementation run. [pp. 4–5, 12–13.]

The seed bank begins with one human-authored seed, screens candidates on a fixed query set, and retains metadata such as estimated attack success, segment stability, repair rates, and refusals. Later runs reuse strong seeds and apply stricter promotion targets. Exact query-set size, acceptance thresholds, search budget, UCT constant, phase-transition thresholds, and Stage-1/Stage-2 sample counts are not numerically disclosed here.

### 7.3 Data selection and wrapping

ToolBench contributes 105 MCP servers and 261 queries; BFCL contributes 80 servers and 203 queries. Both are restricted to prompts originally specified as single-turn and single-tool. Tools are wrapped as MCP servers using gpt-4o. Appendix C.5 says tool identity, names, identifiers, and argument schemas are preserved. Live network calls are replaced by deterministic placeholder values so that the experiment isolates trajectory cost rather than external-data accuracy. [pp. 5, 14.]

Appendix C.4 supplies a stronger filter than the simplified main-text description: each candidate is run five times using Qwen-3-32B with the benign server; a prompt is discarded if at least two runs make no tool call. Retained prompts are then shared across all target models. Consequently retention requires at least four of five screening runs to invoke a tool [C: five runs minus at most one failure]. Original candidate counts, excluded counts, train/test splits, and model-specific routability counts are not supplied.

### 7.4 Target and attacker models

Targets are Qwen-3-32B, Llama-3.3-70B-Instruct, Llama-DeepSeek-70B, Mistral Large, Seed-32B, and GLM-4.5-Air. The tables abbreviate them as Qwen, Llama, L-DS, Mistral, Seed, and GLM. The supplied references do not establish exact executable revisions for every target.

The iterative Editor is Llama-3.3-70B-Instruct. One-shot template instantiation uses gpt-4o at temperature 0, with other provider parameters at defaults. The authors describe this as guaranteeing deterministic output; that is their wording, not an independently tested guarantee. The editor follows the target serving/decoding configuration. [pp. 4–5, 13.]

### 7.5 Runtime and controls

[A] A single node has eight H200 GPUs. Targets use vLLM, bfloat16 precision, a 131,072-token maximum context, nucleus sampling p = 0.95, temperature 0.5, and a 16,384-token completion cap per generation. Concurrency is fixed at 25 queries. The emulator adapts Qwen-Agent while holding policy and prompts fixed across conditions. Non-Qwen models receive minimal adaptations to maintain common message formatting and termination logic. Exact package versions, random seeds, and execution repetitions for the final measurements are not provided. [pp. 4, 13.]

### 7.6 Comparison conditions

There are five conditions: benign servers; single-turn Overthink; an aligned Overthink-MT extension; a hand-crafted malicious tool template without MCTS; and the optimized attack. Overthink uses a reproduced ICL–Genetic, Agnostic variant, but because the data are non-RAG, its trigger is placed in the user query rather than retrieved context. Overthink-MT matches six tool calls and delayed exposure of the true result while retaining a benign tool server. The hand-crafted condition isolates templating without optimization. [pp. 5, 7, Table 2 caption.]

These are informative comparisons, but they are not identical attack surfaces. The optimized attack leaves the query unchanged, whereas the adapted Overthink baseline edits it. The reported results therefore compare implemented methods under this setup, not solely a single isolated causal variable.

### 7.7 Metrics and statistical reporting

Token length is average output tokens per eligible query. Attack success rate, ASR, requires both method-specific target behavior and a correct final answer. Benign task success rate, TSR, is the correctness reference. Energy is integrated device power in watt-hours. Cache usage is peak serving-stack KV occupancy. Throughput is tokens per second for a fixed benign workload run concurrently with each condition. Latency is defined as average end-to-end time but no latency-result table or numerical latency analysis is supplied.

No confidence intervals, standard deviations, significance tests, or final evaluation repetition counts are reported in the supplied material. The five screening repetitions are a dataset-filtering procedure, not evidence of five independent final experimental replications.

## 8. Experiments / analyses

| ID | Purpose and manipulation | Data and comparisons | Measures and evidence | Main result and caveat |
|---|---|---|---|---|
| X1 | Test whether costly trajectories retain success; vary attack condition | Six models × two retained corpora; five conditions | Average tokens, benign TSR, attack ASR; Table 2 | Optimized attack gives 57,255–90,298 average tokens and 76.3–96.2% ASR across displayed cells; success is not identical to benign TSR |
| X2 | Measure physical resource impact | Same overall model/benchmark setting | Energy Wh and peak KV%; Figure 2, §4.3 | Large increases; exact examples in prose, most bars not numerically labeled |
| X3 | Measure collateral impact on benign traffic | Fixed benign co-running workload under each condition | Throughput tokens/s; Table 3 | Every optimized-attack cell falls below benign throughput; degree varies |
| X4 | Test input-style PPL filtering | Query and first tool response; three detector LMs | Larger-side score against benign-description maximum; Figure 3 | Optimized attack scores below the displayed reference thresholds |
| X5 | Test content/trajectory monitoring | Self-monitoring and two safety judges; both corpora | Detection percentages; Figure 4 | Optimized attack is rarely flagged, with reported detection below 3% |
| X6 | Test hard resource budgets | Per-session token caps and tool-call limits | Residual ASR; Figure 5 | Budgets bound cost but leave substantial reported success; exact plotted values mostly unlabeled |

X1 connects O1–O3 to behavioral results. X2–X3 address O4 and the system-level meaning of cost amplification. X4–X6 address O5. There is no independent experiment directly comparing a standalone chatbot with a web-browsing agent using a matched task, attacker budget, or deployment stack.

The hand-crafted condition is the closest optimization ablation: it keeps the broad malicious-template idea while removing MCTS. The paper does not separately ablate every invariant, the seed bank, each edit family, or alternative long-content formats. Its attribution to search is supported by the hand-crafted comparison but not by a full factorial component study.

## 9. Results

### 9.1 Token amplification and successful completion

[A] On ToolBench, Llama averages 81,830 tokens with 96.2% ASR, compared with 260 tokens and 98.1% benign TSR. On BFCL it averages 77,052 tokens with 93.9% ASR, compared with 195 tokens and 100.0% benign TSR. The paper reports 314.73× amplification for the ToolBench Llama case. [pp. 6–7.]

The largest reported ratio is Mistral/BFCL: 57,255 versus 87 tokens, or 658.10× as reported. The smallest reported ratio is Seed/ToolBench, 65.51×, where Table 2 lists 85,037 versus 1,298 tokens. High attack success therefore coexists with severe overhead, but the statement that success remains close to baseline needs model-specific qualification.

[C] For ToolBench/Qwen, benign TSR 94.6% minus attack ASR 80.5% is a 14.1-percentage-point gap. For BFCL/L-DS, 95.4% minus 76.3% is 19.1 percentage points. These are success-rate differences, not percent changes. They also compare benign task success with a stricter joint attack-success event, so they do not independently isolate the rate of final-answer failure under attack.

### 9.2 Added value of optimized templates

[A] ToolBench/Qwen improves from 37,425 tokens and 51.3% ASR for the hand-crafted template to 65,273 tokens and 80.5% ASR for the optimized version. [Table 2.]

[C] That is 27,848 additional average tokens and a 29.2-percentage-point ASR increase. Across all 12 model/benchmark cells, the optimized attack has greater average length and greater ASR than the hand-crafted template. Nevertheless, it does not achieve the highest ASR among all attack methods in every cell: single-turn Overthink has higher ASR for some models. The advantage is the combination of strong amplification and successful task completion, not universal dominance on success alone.

### 9.3 Energy and cache occupancy

[A] Llama/ToolBench energy rises from 5.63 Wh to 3159.45 Wh, reported as 561.18×. Mistral/BFCL rises from 4.24 Wh to 2269.60 Wh, reported as 535.28×. Peak KV occupancy rises from 0.4% to 73.9% for Mistral/ToolBench and from 0.3% to 66.1% for Llama/BFCL. The general reported range is approximately 35–74% under attack, usually below 1% benignly. [p. 6, §4.3.]

The figure supplies energy totals, not electricity bills. The paper primarily treats output tokens as an economic-cost proxy; it does not report a provider pricing calculation. The exact aggregation scope for every displayed energy total is not fully explicit, so these Wh examples should not be silently called per-query energy.

### 9.4 Throughput loss

[A] Seed/ToolBench benign throughput is 4001 tokens/s and attack-condition throughput is 1417 tokens/s; the authors report a 64.6% drop. [p. 7, Table 3.]

[C] The reduction from 4001 to 1417 is 2584 tokens/s, and 2584/4001 × 100 is approximately 64.6%. Across the table, not every workload is literally halved: GLM/BFCL falls from 3734 to 2410, a derived 35.5% drop, whereas Qwen/BFCL falls from 5093 to 1738, a derived 65.9% drop. Thus the authors' approximately 50% overall summary describes an aggregate tendency, not a universal per-cell result.

### 9.5 Defense outcomes

[A/B] Figure 3 shows optimized-attack PPL scores of 13.34, 11.35, and 15.10 for the three detector columns, below reference values 59.31, 38.57, and 93.70. Figure 4 and nearby text report less than 3% detection for the optimized attack. Figure 5 shows residual ASR under budget controls; budgets constrain worst-case expenditure but do not consistently identify the wasteful procedure. These are findings for the tested detector configurations, not proof of immunity to all defenses.

## 10. Figure-by-figure interpretation

### Figure 1 — Tool-layer attack overview

[B] This architecture diagram has a benign interaction on the left and an attacked interaction on the right. A user asks for current weather in Singapore. The benign agent calls a weather tool and receives a sunny-weather result, leading to a simple answer. Central components depict MCTS optimization, a stored universal template, and LLM-based modification of the server. On the attacked side, the same apparent weather capability includes multi-turn and long-argument text, repeated calls, and a highlighted resource-consumption loop. The final weather result and answer remain benign.

The arrows distinguish ordinary request/result flow from repeated attacked interactions. The diagram's long-argument annotation illustrates 16,384 tokens; it is not a measured average for all calls. The figure visually expresses that the detour occurs before the result is released. It is a conceptual workflow, not a complete interface specification or raw execution trace. [p. 3.]

### Figure 2 — Energy and cache occupancy

[B] Four grouped-bar panels combine two datasets as columns with energy on the top row and peak KV-cache percentage on the bottom. Horizontal categories are the six model abbreviations. Colors distinguish benign, Overthink, Overthink-MT, hand-crafted, and optimized attack conditions; gray denotes benign and red denotes the optimized attack. Vertical axes are linear: energy is labeled Wh, and cache is labeled percent. The upper panels show energy ticks up to 3000 Wh, while the lower panels show percentage ticks through 100.

The red bars are consistently prominent, and hand-crafted templates also cause substantial increases. Ordinary Overthink produces much smaller resource bars in this setting. No error bars or confidence intervals are visible. Exact values should be taken from the prose examples, not estimated as precise numbers from bar heights. The plot supports a broad resource-pressure pattern across model/dataset combinations but cannot establish run-to-run variability. [p. 6.]

### Figure 3 — Perplexity detector comparison

[B] This annotated heatmap has attack conditions as rows and three detector models as columns. The caption identifies Llama-3.1-8B, Ministral-8B, and Qwen3-8B; the compact visual abbreviates detector names. Cells contain exact displayed scores, with color encoding magnitude. The first row is the benign-derived reference threshold. The optimized-attack row is low across all three columns.

Visually readable values are: reference 59.31/38.57/93.70; Overthink 17.23/14.98/18.79; Overthink-MT 20.41/19.89/21.04; hand-crafted 14.84/12.15/16.70; optimized attack 13.34/11.35/15.10. There are no error bars. The prose defines the score as the larger of query and first-tool-response PPL and the threshold as the maximum over benign tool docstrings. The plot does not separately show distributions, receiver-operating curves, or false-positive rates. [pp. 7–8.]

### Figure 4 — Output and trajectory detection

[B] The stacked heatmap contains three monitoring methods: self-monitoring, Qwen-Guard-3, and Llama-Guard-3. Within each block, dataset columns are separated into ToolBench and BFCL. Rows are target models, and repeated columns are benign, Overthink, Overthink-MT, hand-crafted, and optimized attack. The color bar represents detection percentage on a linear 0–100 scale.

The main visual pattern is strong detection for many Overthink-style cells and low detection for the tool-template conditions. The authors report optimized-attack detection as typically near zero and always below 3%. Dense cell labels exist, but this report deliberately does not transcribe every tiny cell; the supported global statement and visual pattern are retained. No uncertainty intervals are shown. These judges evaluate behavior or unsafe content; low flagging does not imply low resource harm. [p. 8.]

### Figure 5 — Resource caps and residual success

[B] Four line panels show ToolBench and BFCL as columns, with token caps above and tool-call limits below. The vertical axis is ASR in percent, with visible ticks from 40% to 100%. The horizontal token-cap labels are B, approximately 5k, 10k, and 15k. The call-limit panels use B and limits 1–5. B is benign TSR, not an attacked run at zero budget. Colored lines and circular markers distinguish the six target models.

The top panels generally decline as the displayed token cap increases from approximately 5k to 15k; this visible direction should not be reversed to imply a monotonic benefit from tighter caps. The bottom panels show an initial loss under tight call constraints followed by partial recovery as more calls are allowed. The lines remain comparatively high for many models. Point values are not numerically annotated, and this report does not promote visually estimated positions into exact rates. The B point uses a different metric definition from attack ASR, which matters when reading the connected lines. No confidence bands are shown. [p. 8.]

[D] A one-call limit cannot satisfy the unchanged six-call progression endpoint used in the main comparison. The authors say the attack adapts to the constraint, but do not specify the corresponding target/protocol changes. These budget-panel rates therefore cannot be pooled with default six-call ASR. Hard caps still bound expenditure; residual success is not evidence that the caps fail to enforce their numerical limits.

## 11. Table-by-table interpretation

### Table 1 — Positioning against earlier attacks

[A/B] Columns are Engorgio, P-DoS, Auto-DoS, Overthink, and the proposed attack. Rows compare correctness preservation, trigger layer, turns and bounds, long-output location, and attacker access. The first three are marked non-correctness-preserving; Overthink and the proposed method are marked preserving. The first three trigger at dialog queries, Overthink at RAG context, and the new attack at an MCP tool server. Earlier methods have a one-turn bound ≤ M; the proposed method has n turns and bound ≤ nM. Output moves from answer or thinking to tool calling. Access is white-box for Engorgio/P-DoS and black-box for the other three.

These are categorical author characterizations, not measurements of all cited methods in the present evaluation. The caption points to §4.5 for task success, although the primary effectiveness section is §4.2; this is a cross-reference issue. [p. 2.]

### Table 2 — Behavioral effectiveness

[B] The table has ToolBench and BFCL column groups, each ordered Llama, Qwen, GLM, Mistral, L-DS, Seed. Length rows are average output tokens. Benign success is TSR; attacked success is ASR. To preserve exact key values without repeating every baseline cell, the optimized results and benign references are transcribed below.

| Dataset / metric | Llama | Qwen | GLM | Mistral | L-DS | Seed |
|---|---:|---:|---:|---:|---:|---:|
| ToolBench benign length | 260 | 638 | 634 | 127 | 197 | 1298 |
| ToolBench attack length | 81830 | 65273 | 63694 | 61354 | 65546 | 85037 |
| ToolBench benign TSR % | 98.1 | 94.6 | 95.0 | 90.8 | 86.6 | 90.4 |
| ToolBench attack ASR % | 96.2 | 80.5 | 83.1 | 81.2 | 78.9 | 84.3 |
| BFCL benign length | 195 | 770 | 389 | 87 | 157 | 950 |
| BFCL attack length | 77052 | 67585 | 67656 | 57255 | 68464 | 90298 |
| BFCL benign TSR % | 100.0 | 98.5 | 88.8 | 83.8 | 95.4 | 98.0 |
| BFCL attack ASR % | 93.9 | 82.7 | 83.3 | 78.2 | 76.3 | 92.4 |

Among optimized lengths, Seed/BFCL is largest at 90,298 and Mistral/BFCL smallest at 57,255. Among optimized ASRs, Llama/ToolBench is largest at 96.2% and L-DS/BFCL smallest at 76.3%. There are no ties among these extrema. The optimized method exceeds hand-crafted length and ASR in every displayed pairing. Some Overthink ASRs exceed the optimized method and even the benign TSR; because the attack conditions and success events differ, that observation is not itself a logical contradiction. The table provides no uncertainty estimates or significance markers. [p. 7.]

### Table 3 — Throughput of concurrent benign work

[B] Rows are the same five conditions and columns the same six model abbreviations, repeated for both corpora. Units are tokens/s, referring to the benign co-running workload. Key exact values are:

| Dataset / condition | Llama | Qwen | GLM | Mistral | L-DS | Seed |
|---|---:|---:|---:|---:|---:|---:|
| ToolBench benign | 3594 | 4602 | 3753 | 2898 | 3812 | 4001 |
| ToolBench optimized attack | 1672 | 1793 | 2324 | 1716 | 2106 | 1417 |
| BFCL benign | 3563 | 5093 | 3734 | 2871 | 3845 | 4082 |
| BFCL optimized attack | 1668 | 1738 | 2410 | 1740 | 2130 | 1536 |

The optimized condition is lowest in every model/dataset column; the hand-crafted condition is also substantially disruptive. Overthink sometimes yields higher throughput than benign, for example BFCL/Llama 3822 versus 3563, so variability or scheduling effects cannot be quantified without repeated-run statistics. The authors' statement that single-turn effects are negligible is also too broad for some cells: Mistral/BFCL is 2289 versus 2871, a derived decrease of approximately 20.3%. No uncertainty is supplied to determine significance. [p. 7.]

### Table 4 — Template elements and handling

[A/B] Five rows describe segment argument, calibration-sequence argument, Progress return, Repair return, and Terminal return. Columns identify type, effect, and constraints. Segment indices must be positive and advance by one. Sequences require exactly L strictly increasing integers using digits and commas, with optional spaces; abbreviated ranges, ellipses, and duplicates are invalid. Progress requires a valid sequence before the terminal segment. Repair preserves the current segment. Terminal requires the final segment and a valid sequence and returns the unchanged benign payload.

This table is methodological rather than a performance comparison. It makes explicit that repeated generation and anti-abbreviation checks are deliberate parts of the resource-amplification mechanism. The benign payload is preserved, but the path to obtaining it is changed. [p. 13.]

## 12. Diagram / architecture interpretation

Figure 1 and Table 4 together define a feedback system. The user's task enters the agent. The agent legitimately selects the tool. The server's response then affects the next control decision. Under attack, intermediate responses redirect the agent into further calls rather than releasing the task result. Each call generates long arguments; validation decides between retrying the same segment, progressing, or returning the result.

The control loop has three branches: invalid content leads to repair without progress; valid nonterminal content leads to the next segment; valid terminal content leads to the benign result. MCTS operates outside this runtime loop by testing alternative text templates and retaining effective ones. The seed bank carries information across searches. These two loops should not be confused: one optimizes attack text, while the other consumes resources during a user task.

[D] Architecturally, the vulnerability is that procedure-defining text from an external component can influence the agent's scheduling and expenditure. The diagram does not show a browser, arbitrary website content, cross-origin access, or browser credentials. Its relevance to web agents depends on their using a comparable externally influenced tool loop.

## 13. Equations and mathematical concepts

### Output cost and constrained objective — p. 3

[A] A trajectory is τ = {(a_t, r_t)} from t = 1 to n, where a_t is a tool call and r_t its response. Cost is C(τ) = Tok_out(τ): the total output tokens generated by the model along the trajectory. This is a scalar cost proxy, not an explicit currency equation.

Equation (1) maximizes E[C(τ(q; θ))] over θ ∈ Θ. Here θ is the malicious text template, Θ is the feasible template space, and q is a user query. Equation (2) requires Pr[Succ(u, τ, o) = 1] ≥ p_min, where u = goal(q), o is the final answer, and Succ is a binary success indicator. Together they express: make expected generation expensive while keeping successful task completion sufficiently probable. The numerical p_min and the complete distribution underlying the expectation are not supplied. Appendix B.1 specifies the routable-query conditioning.

### Aggregate bound — Table 1, p. 2

[A] A single generation contributes at most M completion tokens under its cap. Across n capped generations, the table gives aggregate output at most nM. This explains how total trajectory length can exceed the single-generation cap without violating that cap. It is an upper bound, not a prediction that every call reaches M or that an attacker controls unlimited n. M also denotes the model elsewhere, an overloaded notation that must be resolved from context.

### UCT branch selection — p. 4

[A] The selected child maximizes Q̄(u) + C sqrt[ln(1 + N_uct(v)) / (1 + N_uct(u))] over children u of node v. Q̄ is the running mean evaluation signal. N_uct counts exploration visits. C is an exploration coefficient. The first term favors observed quality; the second favors less-visited children relative to the parent. The additions of 1 prevent zero-count singularities. In this equation u is a child node, whereas elsewhere u means the user's goal; C is a coefficient, whereas C(τ) is cost.

Appendix B.4 says visit counts can use Stage-1 samples only to avoid heavy batches distorting exploration, while Q̄ can aggregate all rollouts. Algorithm 1 describes Stage-1 count updates and Stage-2 value refinement. Exact coefficient values and batch sizes are absent.

### Trigger event and routable set — p. 12

[A] S(q; A, M, θ₀) = I{there exists t such that a_t calls Tθ₀ under θ₀}. The indicator I is 1 when the benign agent calls the benign server at least once, and 0 otherwise. The routable set is D_T = {q ∈ X : S(q; A, M, θ₀) = 1}, where X is the query space and θ₀ the benign template. Conditioning on D_T excludes queries that never use the tool. It matches the stated lack of influence over the first routing decision.

### Search reward — p. 13

[A] mt_pass = I{MT} and len_pass = I{LEN}. MT means the ordered multi-turn target is met; LEN means the fixed length target L* is reached and omissions are repaired. Reward is r = α mt_pass + β mt_pass len_pass, with 0 < α ≤ β ≤ 1.

[C] Therefore failure of MT yields reward 0; MT alone yields α; meeting both yields α + β. Length receives no additional credit without multi-turn success. The displayed constraints permit α + β up to 2, so the reward is not necessarily normalized to [0,1]. This reward is a search surrogate for adherence and length; it is not itself the formal cost objective or an explicit final-answer correctness score. Correctness and acceptance are addressed elsewhere, but their precise numerical gating is not fully specified.

### Template invariants — pp. 4, 12–13

The progress rule is t₁ = 1 and t_(k+1) = t_k + 1 for valid advances. A valid sequence and t < T_max produce Progress; an invalid sequence produces Repair without advancement; a valid sequence and t = T_max produce Terminal. Table 4 clarifies the intended increment despite cramped subscript rendering in extracted text. The notation L for sequence length is distinct from Figure 5's L for a session token cap. Neither should be silently equated with the 16,384-token generation cap.

## 14. Interpretation and discussion

[A] The authors interpret the findings as evidence that the tool-calling layer deserves explicit availability protection. Correctness preservation makes the attack difficult for defenses that look for irrelevant output or unsafe content. The observed harm is resource expenditure and interference with concurrent work rather than semantic toxicity. Their conclusion calls for monitoring the whole workflow.

[D] The strongest supported causal story is comparative: under a common emulator, prompts, decoding settings, and hardware, malicious templates produce much larger trajectories and worse benign-workload throughput. The hand-crafted baseline supports the contribution of tool-layer procedural manipulation, and the optimized baseline supports added benefit from search. However, the exact share attributable to MCTS, turn count, calibration length, cache pressure, or scheduler behavior is not isolated through independent interventions on each component.

Several consistency checks matter:

- The introductory statement that completions consistently exceed 60,000 is broader than Table 2: Mistral/BFCL is 57,255. Most optimized cells do exceed 60,000, but not all.
- The abstract's 100–560× energy wording is approximate; §4.3 gives a 561.18× example, and the introduction says up to 561×. Preserve the exact example rather than forcing identical rounding.
- The authors say success stays close to benign TSR, but gaps vary and reach 19.1 percentage points in BFCL/L-DS. Because ASR is a joint event, this is not equivalent to a measured correctness-only drop.
- The main text says excluded prompts never trigger a tool; Appendix C.4 instead excludes those failing to trigger in at least two of five screening runs. The appendix supplies the operational rule.
- Statements about unchanged signatures and schemas coexist with introducing two argument roles and a template-governed return policy. Without code, the precise schema/implementation boundary remains unresolved.
- The attack setup points to §§4.2–4.4 for component procedures, but those sections are results; the method is primarily §§3.2–3.4 and Appendix B.
- Latency is defined but not numerically reported. Reduced OOM-safe concurrency is discussed but not separately quantified.

These qualifications narrow interpretation without erasing the central evidence: a successful final answer can coexist with a highly inefficient externally steered trajectory.

## 15. Contributions and novelty

**Conceptual [A]:** The paper claims the tool-calling layer as a first-class correctness-preserving DoS surface. Its stated novelty is author positioning, not independently verified priority.

**Methodological [A]:** It separates terminal payload correctness from trajectory efficiency and formulates cost maximization under a success constraint. Legitimate-tool conditioning makes the attacker model explicit.

**Algorithmic [A]:** It applies phase-gated MCTS, local repair edits, two-stage evaluation, and seed reuse to optimize text-visible server templates. There is no new theorem or proof of optimality.

**Systems/empirical [A]:** It measures energy, cache occupancy, and collateral throughput alongside generated length and success over six models and two retained datasets.

**Defense analysis [A]:** It contrasts perplexity filters, self-monitoring, safety judges, and hard budgets, showing different relationships to economic abuse.

No new public dataset or benchmark release is established in the supplied material. Existing corpora are filtered and wrapped. The code is described as forthcoming, so implementation availability cannot be treated as a delivered contribution here.

## 16. Limitations

### Authors' stated limitations

[A] Section 6 explicitly limits the evaluation to a controlled emulator with deterministic stubbed tool payloads. It focuses on single-tool, originally single-turn subsets for comparability. The authors acknowledge that results may differ in production stacks, multi-tool long-horizon tasks, or different runtimes and hardware. Their structured numeric calibration sequence is one way to produce long tool-call outputs; other protocol-compatible long-form patterns are not exhaustively explored. [p. 9.]

### Additional evidence-based analyst observations

[D] The paper supplies no final-run uncertainty intervals, replication counts, or significance testing. Search budgets, several acceptance thresholds, and exact component settings remain unspecified. There is no full split description separating template search, seed screening, promotion, and final evaluation, so independence between optimization and evaluation cannot be established from the supplied text.

Dataset screening uses Qwen-3-32B and then shares retained prompts across all targets. This is a consistent common set, but not proof that every retained query is equally routable for every model. Task-success scoring details and the exact energy aggregation scope are not fully specified. The text-only/no-control-flow-change boundary is asserted rather than demonstrated with inspected code. Defense evaluation covers particular detectors and thresholds, not all workflow-aware availability controls.

The study does not directly compare web agents with standalone LLMs, and deterministic placeholders do not test accuracy against live external reality. These observations are analyst qualifications, not admissions attributed to the authors.

## 17. Threats to validity

The following categories are analyst framing [D], unless an author limitation is explicitly identified.

**Internal validity:** Shared policy, prompts, runtime, and decoding reduce obvious confounds. However, several components change together in the optimized attack, and the adapted Overthink trigger is placed at a different surface. The study does not fully decompose causal contributions.

**External validity:** The authors' emulator, workload, and hardware restrictions limit generalization to production agents and web browsing. All targets are evaluated within one common execution design rather than their full native product stacks.

**Construct validity:** Output tokens measure generation burden, not a direct monetary invoice. Joint ASR is not the same as correctness alone, and method-specific target behavior differs across attacks. Placeholder-based success measures coherent task completion in the simulator rather than live data truth. Unsafe-content judges may be poorly aligned with availability abuse, which is itself part of the authors' interpretation.

**Statistical conclusion validity:** No error measures or final repetition counts are supplied. Differences are descriptive; significance and stability cannot be inferred. Rounded percentages do not justify reconstructing exact success counts without known per-condition denominators.

**Ecological validity:** Isolation prevents unintended external actions but removes network variability, tool failures, changing data, and real user behavior. The paper does not establish which of those factors would strengthen or weaken the attack.

**Reproducibility:** Hardware and principal decoding settings are specified, but exact software revisions, search hyperparameters, templates, scoring code, logs, and random seeds are absent from the supplied package. The future code-release statement is not evidence that such artifacts were inspected.

## 18. Future work and open questions

### A. Explicit author proposals

[A] The conclusion calls for defenses using behavioral baselines to distinguish legitimate from maliciously inefficient tool-calling patterns. Ethical considerations mention tool-provenance controls and trajectory-based monitoring as protective directions. The limitations identify production stacks, multi-tool long-horizon tasks, different hardware/runtimes, and other long-form content patterns as areas beyond current coverage. The abstract says code will be released soon; its actual release status is unknown here. [pp. 1, 8–9.]

### B. Additional open questions

[D] A direct answer to the user's comparative research question would require matched standalone-LLM and web-agent experiments, with explicit attacker access, shared tasks, and resource budgets. It remains unclear how well these templates transfer to live browser workflows or heterogeneous tool ecosystems, how much search costs relative to induced expenditure, and how robust results are across repeated runs.

Other unresolved questions include whether independent evaluation templates retain the same amplification, whether task-aware efficiency monitors outperform content-safety judges, how budget policies trade legitimate task completion against resource protection, and whether the claimed interface-preserving implementation can be independently reproduced. These questions follow from the supplied design and missing evidence; they are not new findings.

## 19. Terminology and notation glossary

| Term / symbol | Meaning in this paper |
|---|---|
| LLM | Large language model; underlying generator |
| Agent | Policy/model operating through repeated tool interactions |
| MCP | Model Context Protocol; studied server interface |
| DoS / economic DoS | Availability or economic harm from excessive resource use |
| RAG | Retrieval-augmented generation; a context-layer comparison surface |
| MCTS | Monte Carlo Tree Search over template edits |
| UCT | Tree-selection rule balancing measured quality and exploration |
| KV cache | Key-value cache; serving memory occupancy is measured |
| OOM | Out of memory |
| PPL | Perplexity; detector score calibrated against benign descriptions |
| BFCL | Berkeley Function Calling Leaderboard |
| ASR | Attack success rate: target behavior plus successful task completion |
| TSR | Task success rate under benign servers |
| q / X | User query / query space |
| u = goal(q) | User goal; u also denotes a child node in the UCT equation |
| o | Final answer |
| A | Agent policy; Algorithm 1 also uses a calligraphic action-set symbol |
| M | Underlying model; Table 1/setup also use M for a completion cap |
| θ / θ₀ | Malicious text template / benign template |
| Tθ / F | Parameterized tool server / exposed functions |
| τ / a_t / r_t | Interaction trajectory / tool call / tool response |
| C(τ) | Output-token cost; UCT's standalone C is an exploration constant |
| Succ | Binary indicator of achieving the user's goal |
| p_min | Minimum required success probability; numeric value unspecified |
| S / D_T | Benign tool-selection indicator / routable-query set |
| t / T_max | Current segment / terminal segment count |
| L / L* | Calibration-sequence length / target length; Figure 5 reuses L for session token cap |
| m* | Minimum multi-turn target in Algorithm 1 |
| φ | Search phase label, pre_MT or post_MT |
| A_MT / A_LEN / A_REP | Multi-turn, length, and repair edit families |
| Q̄ / N_uct | Running evaluation mean / exploration visit count |
| α / β | Search-reward weights, with 0 < α ≤ β ≤ 1 |
| Wh / tokens/s | Watt-hours of energy / throughput unit |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Target models | 6 | models | Both benchmarks | Author-reported | p. 4, §4.1 |
| ToolBench set | 105 / 261 | servers / queries | Retained evaluation set | Author-reported | p. 5 |
| BFCL set | 80 / 203 | servers / queries | Retained evaluation set | Author-reported | p. 5 |
| Screening repetitions | 5 | runs/prompt | Qwen benign screening | Author-reported | p. 13, C.4 |
| Exclusion threshold | ≥2 failures | runs out of 5 | Failure to call any tool | Author-reported | p. 13, C.4 |
| Hardware | 8 × H200 | GPUs | One node | Author-reported | pp. 4, 13 |
| Concurrency | 25 | queries | Fixed serving setting | Author-reported | p. 4 |
| Maximum context | 131072 | tokens | Target runtime | Author-reported | p. 13, C.1 |
| Per-generation cap | 16384 | tokens | All target conditions | Author-reported | pp. 5, 13 |
| Sampling | 0.95 / 0.5 | top-p / temperature | Targets and iterative editor | Author-reported | p. 13 |
| Atomic edit count | 16 | edits | Three edit families | Author-reported | p. 12, B.4 |
| Matched multi-turn budget | 6 | tool calls | Overthink-MT comparison | Author-reported | p. 7, Table 2 caption |
| Largest token ratio | 658.10× | ratio | Mistral/BFCL: 57255 vs 87 | Author-reported | p. 6 |
| Llama token ratio | 314.73× | ratio | ToolBench: 81830 vs 260 | Author-reported | p. 6 |
| Smallest reported ratio | 65.51× | ratio | Seed/ToolBench | Author-reported | p. 6 |
| Maximum attack length | 90298 | average output tokens | Seed/BFCL | Visually readable | p. 7, Table 2 |
| Llama success comparison | 96.2 / 98.1 | ASR% / TSR% | ToolBench | Author-reported | pp. 6–7 |
| Qwen search improvement | 51.3 → 80.5 | ASR% | Hand-crafted → optimized, ToolBench | Author-reported | pp. 6–7 |
| Qwen ASR difference | 29.2 | percentage points | 80.5 − 51.3 | Analyst-derived | Table 2 |
| Energy example | 5.63 → 3159.45 | Wh | Llama/ToolBench | Author-reported | p. 6 |
| Energy ratio example | 561.18× | ratio | Llama/ToolBench | Author-reported | p. 6 |
| Second energy example | 4.24 → 2269.60 | Wh | Mistral/BFCL | Author-reported | p. 6 |
| Peak KV example | 0.4 → 73.9 | % occupancy | Mistral/ToolBench | Author-reported | p. 6 |
| Peak KV example | 0.3 → 66.1 | % occupancy | Llama/BFCL | Author-reported | p. 6 |
| Throughput example | 4001 → 1417 | tokens/s | Seed/ToolBench benign co-runner | Visually readable | p. 7, Table 3 |
| Throughput loss | 64.6 | % reduction | Seed/ToolBench | Author-reported | p. 7 |
| Optimized PPL | 13.34 / 11.35 / 15.10 | PPL score | Three detectors | Visually readable | p. 8, Figure 3 |
| Monitor detection | <3 | % | Optimized attack, tested monitors | Author-reported | p. 8 |

No approximate plot-point estimates are included in this table. Values described as ratios use the source's reported rounding. Monetary prices, exact latency, search runtime, and confidence intervals are not supplied.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External tool text can sustain costly successful trajectories | Threat model, template invariants, high joint ASR with long output | F1, T2, T4; X1 | pp. 3–7, 13 | HIGH for reported controlled setup; no production validation |
| Aggregate cost can exceed one generation cap | n-turn bound and 16384-token per-generation setting | T1, T2 | pp. 2, 5, 7 | HIGH; not evidence of bypassing the actual cap |
| Optimization improves on a fixed template | Higher length and ASR in all 12 optimized-versus-hand-crafted cells | T2; X1 | p. 7 | HIGH descriptive evidence; no uncertainty or full component ablation |
| Resource amplification has physical consequences | Reported Wh and cache increases | F2; X2 | p. 6 | HIGH for supplied numerical claims; aggregation and repetition details limited |
| Concurrent benign work is degraded | Every optimized throughput cell below benign | T3; X3 | p. 7 | HIGH descriptive evidence; degree is model dependent |
| PPL filtering misses these tested attacks | Scores remain below benign-derived maxima | F3; X4 | pp. 7–8 | HIGH for tested score/threshold design; not universal filter failure |
| Standard monitors rarely flag optimized templates | Reported detection below 3% | F4; X5 | p. 8 | HIGH for author report; only selected monitors |
| Budgets limit expenditure without reliably eliminating abuse | Residual ASR curves and author discussion | F5; X6 | p. 8 | MEDIUM: exact point values and adaptation details limited |
| Findings do not establish production-wide vulnerability | Explicit emulator, stubbing, and workload restrictions | §6, C.5 | pp. 9, 14 | HIGH for scope limitation |
| Agent loops add a relevant vulnerability mechanism for web agents | Repeated tool feedback controls trajectory length | F1, §3.1, B.1 | pp. 3, 12 | MEDIUM analyst inference; no direct standalone/web comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant for the weather. Normally it asks a weather service once and tells you the answer. In this paper, the weather service can still give the right answer, but first it tells the assistant to complete a long series of unnecessary steps. The assistant treats those steps as part of doing the job, so it keeps producing long messages and making more calls.

A limit on the size of one message does not automatically limit the total size of the whole conversation. If the assistant keeps taking another step, many individually limited messages can add up to a very large amount of work. The researchers report that this can consume much more energy and memory and slow down other people sharing the same system.

The attack is difficult for the tested safety checks because the final answer can be correct and the intermediate messages need not contain obviously dangerous content. The waste is in the procedure. This is why the paper argues that checking only answers or unsafe words is insufficient for this kind of resource abuse.

For web agents, the useful lesson is about an extra place where influence can enter: feedback from external tools can affect what the agent does next. That connection is an analyst inference. The paper tested a controlled tool-calling emulator, not a real browser agent against a standalone chatbot, so it cannot by itself rank the overall security of those systems.

## Completeness Audit

The audit uses the inventory above as its denominator. Fully represented means the substantive mechanism or result is covered, not that every source sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META: identity, authors, affiliations, version | Yes, visual/text | Yes | Represented in compressed form | Exact title and author list retained below; affiliations summarized |
| Abstract | Yes, visual/text | Yes | Fully represented | Mechanism, headline results, caveats checked |
| §1 Introduction | Yes, visual/text | Yes | Represented in compressed form | Motivation and three contributions |
| §2.1 Operational cost | Yes, visual/text | Yes | Represented in compressed form | Industry examples compressed |
| §2.2 Related resource attacks | Yes, visual/text | Yes | Represented in compressed form | Author positioning preserved |
| §3.1 System/objective/threat | Yes, visual/text | Yes | Fully represented | Conditional scope and success constraint |
| §3.2 Template | Yes, visual/text | Yes | Fully represented | Five elements and four invariants |
| §3.3 Seed bank | Yes, visual/text | Yes | Fully represented | Initialization, reuse, metadata, missing thresholds |
| §3.4 Search | Yes, visual/text | Yes | Fully represented | Phases, repair gating, UCT |
| §4.1 Setup | Yes, visual/text | Yes | Fully represented | Models, data, baselines, hardware, metrics |
| §4.2 / X1 | Yes, visual/text | Yes | Fully represented | Exact optimized and benign cells; secondary baselines compressed |
| §4.3 / X2 | Yes, visual/text | Yes | Fully represented | Exact prose examples; no invented bar values |
| §4.4 / X3 | Yes, visual/text | Yes | Fully represented | Exact benign/optimized cells and qualifications |
| §4.5 / X4 | Yes, visual/text | Yes | Fully represented | PPL calibration and full displayed score table in prose |
| §4.5 / X5 | Yes, visual/text | Yes | Represented in compressed form | Heatmap patterns and reported detection bound |
| §4.5 / X6 | Yes, visual/text | Yes | Represented in compressed form | Budget curves without invented point values |
| §5 Conclusion | Yes, visual/text | Yes | Fully represented | Workflow-level implication and future direction |
| §6 Limitations | Yes, visual/text | Yes | Fully represented | All stated limitation categories |
| §7 Ethics | Yes, visual/text | Yes | Fully represented | Isolation, public data, dual-use framing |
| Figure 1 | Yes, visual/text | Yes | Fully represented | Architecture and feedback loop |
| Figure 2 | Yes, visual/text | Yes | Represented in compressed form | Axes, conditions, trends, exact textual anchors |
| Figure 3 | Yes, visual/text | Yes | Fully represented | All displayed cell values transcribed |
| Figure 4 | Yes, visual/text | Yes | Represented in compressed form | Tiny individual detection cells not exhaustively transcribed |
| Figure 5 | Yes, visual/text | Yes | Represented in compressed form | All panel types; exact rates unlabeled |
| Table 1 | Yes, visual/text | Yes | Fully represented | All comparison dimensions |
| Table 2 | Yes, visual/text | Yes | Represented in compressed form | All optimized/benign results, selected baseline comparisons |
| Table 3 | Yes, visual/text | Yes | Represented in compressed form | All optimized/benign results, secondary baselines summarized |
| Table 4 | Yes, visual/text | Yes | Fully represented | All elements and failure handling |
| Algorithm 1 | Yes, visual/text | Yes | Fully represented | Steps explained rather than verbatim pseudocode |
| Cost / Equations (1)–(2) | Yes, visual/text | Yes | Fully represented | Symbols, objective, missing numeric threshold |
| UCT equation | Yes, visual/text | Yes | Fully represented | Selection terms and overloaded symbols |
| Trigger equations | Yes, visual/text | Yes | Fully represented | Indicator, routable population, conditioning |
| Reward equations | Yes, visual/text | Yes | Fully represented | Pass events, weights, derived possible range |
| Appendix A | Yes, visual/text | Yes | Fully represented | Substantive notation in glossary |
| Appendix B.1 | Yes, visual/text | Yes | Fully represented | Legitimate-call trigger and cost note |
| Appendix B.2 | Yes, visual/text | Yes | Fully represented | Invariants and Table 4 |
| Appendix B.3 | Yes, visual/text | Yes | Fully represented | Seed screening and promotion |
| Appendix B.4 | Yes, visual/text | Yes | Fully represented | Edit count, statistics, reward, gates |
| Appendix C.1 | Yes, visual/text | Yes | Fully represented | Serving configuration |
| Appendix C.2 | Yes, visual/text | Yes | Fully represented | Editor and gpt-4o settings |
| Appendix C.3 | Yes, visual/text | Yes | Fully represented | Emulator and adaptations |
| Appendix C.4 | Yes, visual/text plus p. 14 text | Yes | Fully represented | Five-run filter and shared retention |
| Appendix C.5 | Yes, text only | Yes | Fully represented | Wrapping and deterministic stubs |
| Three claimed contributions | Yes | Yes | Fully represented | Novelty remains author-reported |
| Formal research questions/hypotheses | Checked | Absence represented | Fully represented | No formal numbered questions or hypotheses found |
| Theorems/proofs | Checked | Absence represented | Fully represented | None identified |
| References | Yes; pp. 10–11 text only | Selectively | Inspected but deliberately omitted as repetitive/non-substantive | Not independently verified; relevant positioning retained |
| Corresponding-author footnote | Yes | Yes | Represented in compressed form | Bibliographic role only |
| Separate supplements/code/raw data | No | Absence represented | Missing from supplied material | No inspected reproduction artifacts |

### Missing or inaccessible material

No physical page in the supplied 1–14 text sequence is missing. Visual renderings for pages 10, 11, and 14 are absent, but their text is available. No separate code, raw trajectory files, power logs, template repository, or supplementary artifact was supplied. Their existence or present release status cannot be established here. Numerical search hyperparameters and final-run statistical details are missing from the supplied text rather than hidden in an inspected supplement.

### Uncertain interpretations

The precise implementation relationship among unchanged signatures/schemas, introduced argument roles, and unchanged control flow is unresolved without code. Exact energy aggregation scope, evaluation denominators by model, full task-success scoring, search/evaluation separation, and budget-adaptation procedures are insufficiently specified. Dense Figure 4 cells and unlabeled Figure 5 points are not exhaustively transcribed. Approximate headline wording differs from exact cells or examples as discussed in §14.

### Deliberately compressed material

Repeated descriptions of the same return-policy invariants are consolidated. Related-work citations, industry-adoption examples, affiliations, and reference entries are compressed. Table 2's secondary-baseline cells and Table 3's secondary-baseline cells are summarized with selected exact comparisons. Figure 4's individual heatmap cells and Figure 2's unlabeled bar heights are represented by structure, trends, and exact prose anchors rather than a speculative numerical dataset.

### Potential omissions

Every substantive section, subsection, numbered visual, table, algorithm, major equation, experiment family, contribution, and stated limitation identified in the inventory is represented. Deliberate compression means this report does not preserve every baseline cell, citation, or tiny plot annotation. Unknown additional artifacts outside the supplied document cannot be audited. Accordingly, coverage is comprehensive for the inventoried supplied work, with the explicit qualifications above; it is not a claim of independent reproduction or literal lossless preservation.

Bibliographic identity [A]: **Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents**, by Kaiyu Zhou, Yongsen Zheng, Yicheng He, Meng Xue, Xueluan Gong, Yuji Wang, Xuanye Zhang, and Kwok-Yan Lam. Page 1 identifies arXiv:2601.10955v2 [cs.CR], dated 11 March 2026. Affiliations span Nanyang Technological University, University of Illinois Urbana-Champaign, Hong Kong University of Science and Technology, and Shanghai Jiao Tong University. No publication venue for this paper is identified in the supplied material.
