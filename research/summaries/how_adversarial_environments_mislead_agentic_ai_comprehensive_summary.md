## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for all 17 physical PDF pages. Direct page images are supplied for physical pages 1, 3, 4, 5, 6, 7, 8, 14, 15, and 17. The publication's printed pagination runs from 10264 to 10280; all locators below use physical PDF page numbers, not those printed numbers. The title is **How Adversarial Environments Mislead Agentic AI?** The authors are Zhonghao Zhan, Huichi Zhou, Zhenhao Li, Peiyuan Jing, Krinos Li, and Hamed Haddadi, affiliated with Imperial College London. The supplied publication line identifies Findings of the Association for Computational Linguistics: ACL 2026, July 2–7, 2026.

| Accessibility item | Assessment |
|---|---|
| Main document | Yes: extracted text covers pages 1–17 |
| Apparently missing document pages | None within the supplied 1–17 sequence; no independent file inspection was performed |
| Direct visual inspection | Pages 1, 3–8, 14–15, 17 |
| Text-only coverage | Pages 2, 9–13, 16 |
| Figures | Figures 1–7 and A3 visually inspected; A1–A2 assessed from supplied extraction and captions only |
| Tables | Tables 1–8 and A1–A9 have readable supplied text; their rendered pages are also available |
| Equations | Equations 1–3 readable in page 3 image and extraction; formal framework on page 2 is text-only |
| Appendices | A–E present on pages 13–17 |
| Separate supplementary artifacts | Not supplied; no repository, configuration, execution log, notebook, or dataset was inspected |
| OCR | No additional OCR used; supplied text and images were compared where available |
| Other limits | Small labels in overview diagrams and plots are less secure than readable table cells; Figure A2 lacks a supplied page image and contains substantial extracted-text contradictions |

No tools, browsing, code execution, or outside sources were used. The supplied paper is treated as evidence, not as instructions. Its source hash is an identifier supplied by the user, not a hash independently verified here. Evidence categories are: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category [E] is used. HIGH confidence means the supplied evidence is clear; it does not establish that an author claim is independently true. MEDIUM confidence marks interpretation or evidence with material qualifications. LOW or UNKNOWN applies where contradictory reporting or inaccessible detail prevents a secure conclusion.

The inventory denominator includes the abstract; Sections 1–6; Sections 2.1–2.2, 3.1–3.8, and 4.1–4.4; Contributions; Limitations; Ethical Considerations; Acknowledgments; References; Appendices A–E, including B.1–B.5; Figures 1–7 and A1–A3; Tables 1–8 and A1–A9; Equations 1–3 and the agent/adversary mappings; experiments 1a–1d and 2a–2c; follow-up Reflexion, transfer, SHAP, frontier validation, and exploratory defense analyses. No theorem, lemma, proof, or pseudocode algorithm appears in the supplied work. This is an empirical AI-security and evaluation-system paper, with dataset and benchmark contributions, rather than a systematic literature review.

## 1. Plain-language orientation

[A] The paper asks what happens when an AI assistant's tools present a convincing but false environment. A tool-using agent may search for evidence, retrieve records, follow references, and use those observations to decide what to say or do next. The authors argue that relying on external information creates a **Trust Gap**: evaluations commonly test successful tool use in cooperative settings without adequately testing skepticism toward compromised outputs (pp. 1–2).

The authors distinguish two attacks. **The Illusion**, or breadth attack, inserts misleading material into retrieved evidence so the agent gives an incorrect verdict. **The Maze**, or depth attack, inserts fabricated papers and reference connections so the agent spends effort navigating a misleading graph. The first attacks what the agent concludes; the second attacks its sequence of actions. A fabricated paper can therefore cause harm even when the agent expresses uncertainty about the information it reads.

[A] The researchers build **POTEMKIN**, a harness that intercepts tool responses and substitutes controlled adversarial versions. They evaluate five original agents, add a five-model follow-up, vary poisoning intensity, writing style, graph cycle length, and fake-paper plausibility, and examine lightweight defenses. Important reported findings include 94.6% and 96.1% trap entry for GPT-4o and Qwen2.5 in the principal depth table; 14.5% versus 6.8% error on hedged versus confident true claims; and cross-dimension transfer areas under the curve of 0.55 and 0.58 (Tables 4–5 and A4).

[D] For the requested question, this paper supports an explanation of **additional vulnerabilities created by tool-mediated observation and navigation**. It does not directly establish that web agents are quantitatively more vulnerable than standalone large language models. There is no matched standalone-model control, and the primary empirical domain is academic citation graphs. The strongest source-grounded answer is therefore mechanistic: agents expose additional environmental trust boundaries and action loops that this study successfully attacks. The comparative magnitude remains unmeasured.

## 2. Document roadmap

The abstract and Introduction frame environmental deception and identify the Trust Gap, Robustness Schism, and Punishment of Honesty (pp. 1–2). Section 2 defines the agent–environment mapping, attacker powers, and breadth/depth taxonomy, then introduces three metrics (pp. 2–3). Section 3 describes interception architecture, agent configurations, engagement-aware reporting, parallel credibility levels, red-team generation, datasets, experimental campaigns, and analysis methods (pp. 3–5).

Section 4 reports breadth results, framing effects, depth susceptibility, engagement and scaffolding effects, feature/transfer analyses, and frontier-model validation (pp. 5–8). Section 5 positions the work against capability benchmarks, retrieval poisoning, prompt injection, and agent-risk research. Section 6 summarizes the contribution and proposes extensions (p. 9). Limitations span pp. 9–10; ethics and acknowledgments appear on p. 10; references occupy pp. 10–12.

Appendix A discusses exploratory defenses and future mitigation directions (p. 13). Appendix B supplies representative behavior traces and a taxonomy (pp. 13–14). Appendix C gives one breadth and one depth attack trace, shown in Figures 6–7 (pp. 14–15). Appendix D describes deployment, reproducibility artifacts, and extensibility (pp. 14–15). Appendix E contains methodology, transfer, defense, failure-mode, policy-collapse, taxonomy, and tool-interface tables, plus supplementary figures (pp. 15–17).

## 3. Background and context

[A] A **large language model (LLM)** produces language; in this paper, an **agent** combines that model with tools and repeated decisions about tool use. **Retrieval-Augmented Generation (RAG)** grounds outputs in retrieved external knowledge. The paper's concern is that grounding can become deception when those retrieved observations are manipulated. Its **Grounding Paradox** describes the tension between reduced hallucination through deference to sources and increased exposure to malicious sources (§2.1, p. 3).

A **citation graph** consists of papers and directed reference connections. Valid papers form legitimate nodes; fabricated **phantom papers** form adversarial nodes. Following references is a structural operation: the agent selects and visits nodes. **Epistemic drift** means an incorrect verdict attributed to poisoned evidence. **Policy collapse** means navigation into fabricated structures that wastes limited tool-use effort. Neither term means a change to model weights in this experiment.

**Prompt injection** is contrasted with environmental deception. According to the authors, prompt injection inserts instructions intended to hijack behavior; their attacks instead present misleading evidence or topology that the agent accepts voluntarily (§5, p. 9). This distinction concerns attack design, not a demonstrated impossibility of overlap between categories.

**Model Context Protocol (MCP)** is the named integration protocol for compatible agents. **Man-in-the-Tool (MitT)** is the authors' name for an adversary controlling what a tool returns. **ReAct** is the standardized reasoning/action harness used for open-source agents; **Reflexion** is the alternative self-correction scaffold tested for Llama-3. These are named and cited by the paper, but their full algorithms are not reproduced. **SHAP** denotes the paper's feature-attribution analysis; its acronym expansion is not provided in the supplied work. **Area under the curve (AUC)** summarizes the transfer-classifier results; the exact curve and evaluation pipeline are insufficiently documented to reconstruct them here.

## 4. Research problem and gap

[A] The existing problem is a mismatch between assumed trustworthy tool outputs and outputs exposed to adversarial manipulation. An agent uses external observations as evidence, but an attacker can arrange those observations into a coherent false environment. The authors call this the Truman Show Problem, using a fictional constructed reality as an analogy (pp. 1–2).

Their attributed shortcoming of capability benchmarks is that benign, cooperative environments test what agents can accomplish rather than what they can withstand. Their attributed shortcoming of content-focused security research is that it emphasizes corrupted belief updates while overlooking navigation through adversarial graph structure. Section 5 discusses AgentBench, GAIA, ToolBench, Gorilla, WebArena, SWE-bench, and ReportBench as capability-oriented comparators, and corpus-poisoning and prompt-injection studies as related security categories. These literature characterizations are author positions, not independently checked assessments.

The research gap is standardized, reproducible testing of both semantic deception and structural traps in tool-using agents. The motivation includes fabricated scholarly sources and the downstream consequences the authors attribute to them. The empirical scope is deliberately citation-oriented because the authors describe citation topology as stable and reproducible. Their broader threat-model claim covers other tool-mediated domains, but they explicitly defer empirical validation on web-search agents, code tools, and database assistants (pp. 9–10).

## 5. Research questions, objectives, and hypotheses

The paper does not present a numbered formal research-question list. The following retain its objectives and hypotheses without inventing author-designated RQs.

| ID | Kind | Source-grounded formulation | Test or evidence |
|---|---|---|---|
| O1 | Objective | Formalize environmental deception through tool outputs | AEI framework, §2 |
| O2 | Objective | Systematically evaluate breadth and depth attacks | Seven principal experiments, Table A3 |
| H1 | Credibility hypothesis | Surface authority cues may predict vulnerability across both dimensions | Parallel credibility levels, SHAP and transfer analyses |
| H2 | Mechanistic hypothesis | Breadth concerns epistemic processing; depth concerns procedural processing | Cross-dimension logistic-regression transfer |
| O3 | Causal objective | Isolate whether hedge/booster framing changes judgment | Minimal-pair experiment 1d |
| O4 | Measurement objective | Separate security resistance from failure to engage with tools | Engagement-conditioned rates, Table 7 |
| O5 | Follow-up objective | Examine whether scaffolding changes engagement and robustness | Llama-3 ReAct versus Reflexion |
| O6 | Replication objective | Test whether dissociation persists in newer agents | Five-model frontier validation, Table 8 |
| O7 | Exploratory objective | Characterize lightweight defenses' safety–utility tradeoff | Appendix A, Table A5, Figure A2 |

[A] The high-authority prediction is not supported by the aggregate breadth style ordering: neutral Wire content has more drift than Professor content. The authors' procedural/epistemic distinction receives support from weak transfer and different reported predictive features. [D] However, weak transfer is more defensible wording than mathematical independence, especially because one transfer confidence interval excludes 0.5 and details of feature construction are sparse.

## 6. Assumptions / Threat Model

[A] The formal agent maps a query and environment state to a response. The environment contains tool observations such as search results and database records. Agents may check consistency or express uncertainty, but in the stated model they lack independent verification channels, alternative sources, or direct ground-truth access (§2.1, p. 2). This is a consequential environmental assumption: it limits recovery by comparing evidence outside the compromised channel.

The adversary controls a transformation of the tool environment and may modify returned content. It cannot access the agent's internal state, system prompt, or weights (§2.1, p. 3). Examples of possible access mechanisms include search-engine optimization, poisoned knowledge bases, attractive third-party tool metadata, and user-contributed RAG content. These examples are feasibility arguments; the experiments implement interception through the authors' proxy rather than demonstrating compromise of live search infrastructure.

[A] The authors rank feasibility as highest for discoverable third-party tools and user-contributed RAG content, moderate for web-search agents, and lower for sandboxed API-only deployments. Trusted evaluation components include frozen authentic records, ground-truth claims, configured transformations, and metric computation. [D] These are operationally trusted by the experiment; the paper does not provide a formal trusted-computing-base analysis.

The attacked assets are answer correctness and productive use of navigation effort. The examined failures are false verdicts, phantom citations, trap entry, repeated traversal, and wasted budget. Data exfiltration, credential theft, privilege escalation, browser exploitation, and destructive external actions are not evaluated. All adversarial experiments are author-reported as conducted on the authors' hardware in a closed local network, disconnected from production systems and third-party infrastructure (p. 10).

## 7. Methodology

### Architecture and procedure

[A] POTEMKIN is a transparent response-channel proxy. An agent issues a tool call; the harness intercepts the returning response, applies an adversarial transformation, and returns compromised content in the expected interface. It supports an MCP server and a Python library (§3.1, p. 4). Table A9 additionally lists HTTP exposure. Frozen snapshots prevent live API content changes from becoming an uncontrolled variable; perturbations are deterministic under a configurable seed. The seed values are not printed.

Breadth tasks use `search` to return poisoned snippets. Depth tasks use `search_papers` to introduce phantom entry points, `get_paper` to retrieve metadata, and `get_references` to construct fabricated citation connections (Table A9, p. 17). A plausible fake paper is not only a statement: it becomes an addressable record with references that influence subsequent actions.

### Agent configuration

The original agents are GPT-4o-2024-08-06, Claude-3.5-Sonnet, Llama-3-70B, Qwen2.5-72B, and DeepSeek-V3. Proprietary agents use vendor interfaces; instruction-tuned open-source agents use a standardized ReAct harness. All victim agents are reported at temperature 0.0 with a limit of 10 tool calls per task (§3.2, p. 4). Llama-3 also receives a Reflexion follow-up, restricted to experiment 2b. Hardware models, operating systems, inference-library versions, full prompts, token limits, and concrete random seeds are not specified in the supplied paper.

### Data and generation

POTEMKIN-S2 contains 9,878 authentic Semantic Scholar papers and 1,797 reference chains. POTEMKIN-PHANTOMS contains 4,281 generated fake-paper items. Of these, 309 are entry papers: 163 Phantom, 75 Signal, and 71 Glitch; the remainder serve as middle/closer nodes. [C] The reported components sum to 163 + 75 + 71 = 309, leaving 4,281 − 309 = 3,972 other nodes. POTEMKIN-CLAIMS uses 150 AVeriTeC claims, described as balanced in Table A2, with 450 adversarial variations across three styles (§3.6; Table A2). The paper does not specify the precise class counts, selection criteria, annotation agreement, or split assignments.

The Gemini 2.5 family supplies adversarial material to avoid generator–victim overlap. Gemini 2.5 Pro generates fact-injection snippets at temperature 1.0 and style variants at 0.7; Gemini 2.5 Flash generates phantom papers at 0.7 (Table A1). [D] Using a separate family reduces the particular overlap the authors target but does not by itself establish absence of shared training information or other generation artifacts.

### Manipulations, metrics, and statistics

Breadth contamination is 10%, 30%, or 50% of a ten-passage retrieval context: one, three, or five poisoned passages. Styles are Professor, Wire, and Rumor. Depth cycle lengths are two, three, or five hops; plausibility levels are Phantom, Signal, and Glitch. Parallel credibility levels are a design device, not evidence that the two manipulations have equivalent strength.

Drift Rate excludes abstentions; Entry Rate records any phantom visit; Budget Waste measures the fraction of counted traversals spent in phantom nodes. Engagement requires at least one retrieval for breadth, and at least one paper retrieval plus one reference traversal for depth. Experiment 1d uses matched framing pairs, identical system prompts, claim/topic preservation, and character counts within ±5%; the authors apply McNemar's paired test and bootstrap confidence intervals. Reported transfer analyses train logistic regression on experiment 1b features and evaluate on 2b, then reverse direction. Train/test partitioning, regularization, feature normalization, bootstrap counts, and many inferential details are absent.

## 8. Experiments / Analyses

| Experiment | Purpose and manipulated condition | Main evidence and qualification |
|---|---|---|
| 1a Contamination | Vary poisoning at 10%, 30%, 50%; measure drift | Table 3: overall 40.2%, 55.8%, 57.9%; model-specific responses are not uniformly monotonic |
| 1b Style | Compare Professor, Wire, Rumor linguistic credibility | Table 3: overall 42.4%, 54.8%, 36.9%; contamination setting for this sweep is not clearly specified |
| 1c Breadth baseline | Clean environment, no injection | Table 3: overall baseline error 7.9%; original agents 4.7–14.7% |
| 1d Causal framing | Matched hedge versus booster wording, separately for true/false claims | Table 4: true errors 14.5% versus 6.8%; false errors 43.1% versus 45.7%; pair counts and test outputs not tabulated |
| 2a Cycle length | Two-, three-, five-hop phantom cycles | Table 5: high entry for several agents and similar within-model waste across cycle lengths |
| 2b Plausibility | Phantom, Signal, Glitch fake papers | Table 5: overall entries 55.4%, 53.5%, 26.4%; Figure A3 supplies conflicting values |
| 2c Depth baseline | Clean graph without phantoms | Tables 1 and 6: 0.0% entry; this does not measure productive task completion |

The principal experiment counts are aggregated rather than fully partitioned by condition. Table 3 reports 5,064 breadth runs; Table 5 reports 5,336 depth runs including the Reflexion row. [C] These total 10,400, which alone does not reconstruct the claimed approximately 11,000 or 11,000+ task runs. Additional framing, defense, or validation runs may contribute, but the supplied accounting does not establish a complete reconciliation.

The engagement analysis reports 448, 447, 441, 443, and 450 runs for GPT-4o, Claude, Qwen, DeepSeek, and Llama respectively (Table 7). Llama has only eight engaged runs and seven engaged trap entries. Conditional vulnerability is therefore important but rests on a small subgroup for that model. Reflexion raises reported engagement from 1.8% to 11.4% and lowers conditional entry from 87.5% to 68.6%; unconditional entry increases to approximately 10.0% (pp. 7–8).

The unified analysis compares predictive features and cross-dimension transfer rather than introducing another poisoning level. Table A4 reports breadth-to-depth AUC 0.55, 95% CI [0.47, 0.67], and depth-to-breadth AUC 0.58, CI [0.53, 0.62]. The authors report less than 5% shared predictive variance, but its computation is not described sufficiently to reproduce.

The frontier validation supplies 100 scenarios per model, excludes API timeouts beyond a three-attempt threshold, and reports separate valid sample counts for breadth and depth. The models are Claude-Sonnet-4.6, GPT-5.2, Qwen3.5-397B-A17B, Kimi-K2.5, and DeepSeek-V3.2. Breadth is evaluated at 50% contamination; depth uses three-hop cycles (Table 8). The exploratory defense analysis, called experiment 3 in Table A5 and 3b in Figure A2, is outside the seven-experiment overview. It compares perplexity filtering, spotlighting, and their combination; its full sample and model composition are not reported.

## 9. Results

### Breadth susceptibility

[A/B] Table 3 reports overall drift increasing from 40.2% at 10% contamination to 55.8% at 30% and 57.9% at 50%. [C] The successive increases are 15.6 and 2.1 percentage points. This supports the authors' aggregate early-saturation description. It does not establish saturation for every model: DeepSeek rises from 50.7% to 66.2% in the final step, while Claude and Llama decrease in that step. Qwen already has 71.1% drift at 10% contamination. Model-specific clean error rates make clear that attacked errors are compared against nonzero baseline errors, not perfect clean performance.

Neutral Wire style has the highest aggregate drift at 54.8%, compared with 42.4% Professor and 36.9% Rumor. [C] Wire exceeds Professor by 12.4 percentage points and Rumor by 17.9 points. [A] The authors interpret this as neutral language being accepted less critically than overt persuasion. [D] The experiments establish a style association under the tested generation procedure, but do not directly identify the training process responsible.

### Framing asymmetry

Table 4 gives true-claim errors of 14.5% with hedging and 6.8% with boosting. [C] The difference is 7.7 percentage points and the ratio is 14.5 / 6.8 ≈ 2.13, consistent with the reported 2.1×. This is not a universal per-model effect: GPT-4o and Claude show zero difference, while Qwen has fewer errors with hedging. Llama and DeepSeek each show a 20.0-point increase. For false claims, aggregate errors are 43.1% hedged and 45.7% boosted, a −2.6-point difference. Per-model effects have mixed directions. The supported aggregate conclusion is asymmetric calibration, not that every agent rejects all uncertain language more often.

### Depth susceptibility and effort

Table 5 reports principal cycle-length entry rates of GPT-4o 94.6%, Claude 25.3%, Llama ReAct 5.6%, Qwen 96.1%, and DeepSeek 74.7%. Table 6, restricted to entered runs for its behavior metrics, reports waste of 44.8%, 51.3%, 98.0%, 50.5%, and 72.8%, respectively. Llama's low unconditional entry coexists with extreme waste among entries and very low proper engagement. The frequently repeated 44–73% waste range therefore does not include the Llama exception.

Overall plausibility entries are Phantom 55.4%, Signal 53.5%, Glitch 26.4%. GPT-4o still enters 52.4% of Glitch traps. Claude's Phantom-to-Glitch relative decline is 68.2%, but Llama ReAct's listed decline is 72.3%. The author's description of Claude as best discriminator is understandable only with the engagement-failure caveat, not as the literal maximum in the column.

### Conditional reporting and newer models

Conditional entries in Table 7 are 99.0% GPT-4o, 50.9% Claude, 98.0% Qwen, 95.6% DeepSeek, and 87.5% Llama. The table's conditional-minus-unconditional gaps are 4.4, 25.6, 1.9, 20.9, and 81.9 percentage points. These comparisons show that overall avoidance can reflect a lack of tool activity. They do not demonstrate that a particular engaged run would have been safe under an alternative scaffold.

Table 8 gives newer-model mean drift 42.5%, mean entry 72.7%, and mean waste 35.9%. Claude-Sonnet-4.6 has the lowest drift, 26.3%, but 58.0% entry. Qwen3.5 has 46.5% drift and 99.0% entry. GPT-5.2 has the lowest listed entry, 51.1%. These results retain substantial depth risk, although the paper's comparison against an original mean drift of 58.4% conflicts with Table 3's 57.9%, and its 'essentially unchanged' mean entry comparison is not straightforward against Table 5's 59.1%.

## 10. Figure-by-figure interpretation

### Figure 1 — Overview of environmental deception, p. 1

[B] This visually inspected conceptual diagram has no quantitative axes. Its upper breadth region shows poisoned information reaching an agent; its middle depth region shows an agent/tool/proxy pathway and a maze-like reference trap; its lower comparison separates corrupted beliefs from corrupted actions and depicts distinct resistance capabilities. Arrows indicate tool observations and navigation rather than model training. Labels summarize drift 36–76%, entry 25–96%, waste 44–73%, transfer AUC 0.55–0.58, and less than 5% shared variance. These are rounded overview claims, not independent measurements. They omit low-engagement Llama exceptions and compress different experimental conditions.

### Figure 2 — Escaped versus trapped navigation, p. 3

[B] Two directed flow diagrams contrast successful routing and phantom cycles. Panel A begins with a search, moves through real records and reference retrieval, encounters a phantom, then skips it and reaches valid papers. Panel B introduces a phantom after search and shows repeated links among fabricated records, ending in failure. Arrows and loops express action sequence; there are no axes, units, or confidence intervals. The diagram illustrates the attack structure but does not quantify its frequency or prove that all successful agents recognize directed citations in the same way.

### Figure 3 — Breadth versus depth vulnerability, p. 5

[B] A grouped bar chart places agents on the horizontal axis and vulnerability rate from 0 to 1 on the vertical axis. Breadth and depth are encoded with two bar styles; labels include breadth 48%, 30%, 45%, 65%, 42% and depth approximately 95%, 25%, 75%, 96%, with Llama annotated for ReAct/Reflexion. No uncertainty bars are visible. Breadth values differ from Table 1's 50%-contamination results and resemble an aggregate across contamination conditions, but the aggregation is not explicitly defined. The chart supports differing vulnerability profiles; it should not be read as a matched standalone-model comparison or as proof of universally inverted agent rankings.

### Figure 4 — Seven-panel experimental synthesis, p. 7

[B] Panel A is a contamination heatmap: models by 10/30/50% conditions, cells labeled with Table 3 drift values. Panel B groups style bars, with drift on a linear 0–0.8 scale and a dashed 7.9% baseline. Panel C compares per-agent hedge/boost true-claim errors on a linear error-rate axis. Panel D groups true/false aggregate errors, labels 14.5%, 6.8%, 43.1%, and 45.7%, and annotates 2.1×. It contains error bars, but their exact widths cannot be recovered confidently from the image; the paper discusses bootstrap intervals without tabulating these values.

Panel E plots entry rate against budget waste, both 0–1, annotating Llama's engagement gap. Panel F groups Phantom/Signal/Glitch entry bars on a 0–1 scale and marks a decreasing quality gradient. Panel G isolates Llama's ReAct/Reflexion plausibility results on a 0–0.2 entry-rate scale. The chart demonstrates why higher unconditional entry under Reflexion can coexist with improved conditional behavior. Its caption says Reflexion 'improves entry'; the direction and meaning require the text's engagement qualification.

### Figure 5 — Features and transfer, p. 8

[B] Panel A is a horizontal breadth feature-importance chart with mean absolute SHAP values; Authority Score is visually largest, followed by Style and Citation Markers. Panel C is the depth analogue, led by Get Paper Calls, Total Steps, and Plausibility, followed by Get References and Search Calls. Exact bar values are not labeled and are not inferred here. Panel B shows transfer distributions or summaries on an AUC axis approximately 0.40–0.75, with 'n.s.' and an asterisk. The statistical test behind those annotations is not defined in the supplied material. Table A4 supplies exact estimates and intervals. The visual feature ranking is not identical to the prose emphasis on hedge density; that distinction is preserved rather than silently harmonized.

### Figure 6 — Breadth attack trace, p. 14

[B] A boxed textual trace contains a claim labeled false by the authors, a neutral-style poisoned snippet, GPT-4o's confident true verdict, and a drift outcome. It has no axes. It shows a local sequence from evidence to verdict. The legal proposition within the attack is treated solely as the paper's adversarial example; no external legal verification is implied. One trace illustrates a mechanism but does not independently establish the aggregate rate.

### Figure 7 — Depth attack trace, p. 15

[B] A boxed trace starts with an Adam-optimizer literature-review query, retrieves a fabricated survey with venue/year/citation metadata, follows references to phantom IDs, and reports a confident citation by Qwen. Labeled metrics are entry yes, three steps in trap, one loop, and 75% waste. The stated 450 citations are fake-paper metadata, not authentic impact evidence. [C] Three phantom traversals would imply four counted traversals if 75% is computed as 3/4; the full denominator is not printed, so this remains a conditional reconstruction, not a recovered execution trace.

### Figure A1 — Failure modes, p. 16; text-only

[A] The supplied extraction and caption identify an overall distribution and per-agent stacked proportions for N = 2,308: 0.9% Loop Trap, 30.6% Dead-end, 27.0% Authority Cascade, and 41.5% Escaped. These values sum to 100.0%. The per-agent plot has a proportion axis from 0 to 1. No direct visual inspection was possible for this page, so colors, tiny annotations, and exact geometric details are not claimed as observed. The caption's 'stopped after one revisit' description of Dead-end is less specific than Table A6's budget-exhaustion definition.

### Figure A2 — Defense threshold frontier, p. 16; text-only

[A] Extracted labels identify a safety–utility plot, thresholds 25–300, point size inversely related to false-positive rate, and a second false-positive-rate curve. Labels claim threshold 100 yields 90% utility and reduces false-positive rate from 100% at threshold 50 to 70%. The caption instead describes the horizontal axis as attack success rate, and claims no defense achieves utility above 70% with ASR below 20%. Appendix A says threshold 100 changes utility from 48% to 58%. These are conflicting descriptions and values. Without a supplied page image or underlying data, the frontier, optimum, and safety definition cannot be reliably reconstructed.

### Figure A3 — Entry versus citation corruption, p. 17

[B] Three grouped bar panels compare Phantom, Signal, and Glitch. The vertical axis is Rate, linear 0–1. Darker bars denote policy failure/entry, lighter bars output corruption/citation. Labeled entry values are Phantom: GPT-4o 85%, Claude 25%, DeepSeek 72%, Qwen 85%, Llama 5.6%; Signal: 80%, 20%, 72%, 80%, 4.0%; Glitch: 75%, 10%, 33%, 70%, 3.0%. These materially differ from Table 5, especially GPT-4o Glitch 75% versus 52.4%. Citation-rate bars are visible but unlabeled; exact values are not invented. The chart supports a qualitative plausibility gradient and distinction between navigation and citation outcomes, while its quantitative inconsistency remains unresolved.

## 11. Table-by-table interpretation

### Table 1 — Preview, p. 4

Five original agents are compared by type, clean breadth error, drift at 50% contamination, clean depth entry, and attacked depth entry. GPT-4o is 4.7/58.0/0.0/94.6%; Claude 8.0/36.2/0.0/25.3%; Llama 5.4/55.3/0.0/5.6%; Qwen 6.8/76.2/0.0/96.1%; DeepSeek 14.7/66.2/0.0/74.7%. Lower is better, with Llama's low entry explicitly marked as engagement failure. No confidence intervals are supplied.

### Table 2 — Parallel credibility, p. 5

Rows are high/medium/low credibility. Professor prose and Phantom venues with h5 > 100 are high-authority cues; Wire and Signal venues with h5 < 50 are medium; Rumor and fabricated Glitch venues are low. The paper does not define the computation of h5-index. This is a manipulation taxonomy, not a result table or proof that style and graph plausibility are quantitatively matched.

### Table 3 — Breadth results, p. 6

Rows include five agents and Overall; columns include N, baseline error, contamination-specific drift, and style-specific drift, all rates in percent. N values are 1,050, 1,048, 1,048, 873, and 1,045, totaling 5,064. The Qwen footnote reports an 82% API error rate without clarifying its denominator. Important less-prominent patterns are nonmonotonic Claude/Llama contamination responses, equal Llama Professor/Rumor rates of 37.3%, and DeepSeek's highest baseline error, 14.7%. No per-cell sample counts or intervals appear.

### Table 4 — Framing, p. 6

Columns split true and false claims into Hedge, Boost, and their difference. True rows: GPT 0.0/0.0; Claude 14.3/14.3; Llama 26.7/6.7; Qwen 0.0/7.1; DeepSeek 26.7/6.7. False rows: GPT 53.3/40.0; Claude 40.0/33.3; Llama 40.0/46.7; Qwen 58.3/70.0; DeepSeek 26.7/46.7. The aggregate asymmetry is clear, but exact paired counts, p-values, and bootstrap intervals are absent despite the methodological discussion.

### Table 5 — Depth conditions, p. 6

Entry and waste are percentages; W2/W3/W5 refer to cycle lengths. GPT waste is 44.5/43.2/46.6; Claude 49.0/52.8/52.0; Llama ReAct 100.0/100.0/95.0; Qwen 51.6/48.5/51.4; DeepSeek 72.5/72.9/73.1. Plausibility entries are GPT 96.7/93.9/52.4; Claude 23.3/26.2/7.4; Llama ReAct 4.7/6.0/1.3; Reflexion 14.7/9.3/6.1; Qwen 97.3/91.8/47.0; DeepSeek 71.8/71.8/33.1. Dashes for Reflexion cycle results mean not evaluated, not zero. Overall N is 5,336. The relative-drop column requires the engagement caveat for Llama and has no uncertainty intervals.

### Table 6 — Entered-run behavior, p. 7

Rows compare clean/attacked entry, retrieval steps, trap calls, waste, and average entry-node revisits. GPT steps/trap/loops are 4.3/2.0/0.44; Claude 2.6/1.2/0.16; Llama 1.3/1.2/0.24; Qwen 4.2/2.1/0.58; DeepSeek 3.3/2.3/0.79. Overall waste is 55.2%. Waste need not equal the ratio of rounded mean trap calls to rounded mean total steps: averaging per-run ratios differs from dividing averages. Metrics are explicitly for entered runs; comparisons with Table A7 require caution.

### Table 7 — Engagement conditioning, p. 8

Rows provide total N, unconditional entry, engaged count, conditional entry, and percentage-point gap. Engaged counts are GPT 201, Claude 110, Qwen 245, DeepSeek 297, Llama 8. [C] Seven of eight Llama engaged runs yield 87.5%. The tiny Llama subgroup makes a single percentage an unstable basis for broad generalization. The table's unconditional rates resemble principal-cycle rates while its sample sizes differ from Table 5; the cohort mapping is not explained.

### Table 8 — Newer cohort, p. 8

Rows report drift at 50% contamination, valid breadth N, entry and waste for three-hop cycles, and valid depth N. Claude: 26.3, 95, 58.0, 18.6, 100. GPT-5.2: 39.1, 92, 51.1, 19.4, 94. Qwen3.5: 46.5, 99, 99.0, 56.9, 100. Kimi: 48.1, 81, 83.9, 31.8, 93. DeepSeek-V3.2: 52.4, 84, 71.4, 52.8, 84. API-timeout exclusions and valid-N denominators are explicit. No uncertainty intervals are shown.

### Tables A1–A3 — Generation, datasets, experiment register, p. 15

A1 gives generator models and temperatures already detailed in §7. A2 distinguishes all phantom items from entry-paper subclasses through a substantive footnote, preventing the mistaken conclusion that 163 + 75 + 71 should equal 4,281. A3 registers seven experiments and their manipulated variables, but excludes defenses and newer-model replication from that principal count.

### Table A4 — Transfer and features, p. 15

The two AUCs and 95% intervals are the paper's most explicit inferential numbers. Breadth-to-depth includes chance 0.5; depth-to-breadth does not. The feature list separates hedge/certainty/style from tool counts/budget/loop detection and reports less than 5% shared predictive variance. [D] These support limited transfer under the chosen representation, with incomplete evidence for the stronger claim of statistical independence.

### Table A5 — Defense ablation, p. 15

Rows None/Perplexity/Spotlighting/Both have breadth ASR 41/22/14/16%, depth ASR 48.5/0.0/0.0/0.0%, and clean utility 83/48/54/58%. Utility losses are −35, −29, −25 percentage points. Spotlighting gives lowest breadth ASR; combined defenses give highest defended utility. ASR differs from abstention-excluding Drift Rate, so these rates should not be directly substituted for Table 3 drift. Sample sizes and precise success criteria are not provided.

### Table A6 — Failure taxonomy, p. 17

N = 2,308. GPT N469 has loop/dead-end/authority/escape 0.0/41.6/51.4/7.0%; Claude N483: 0.0/3.7/20.1/76.2%; Qwen N456: 3.7/50.2/42.3/3.7%; DeepSeek N450: 0.7/57.6/16.4/25.3%; Llama N450: 0.0/1.3/4.2/94.4%. Overall 0.9/30.6/27.0/41.5%. Explicit multiple-revisit loops are rare in this accounting; much of the observed damage comes from dead-ends and accepting phantom authority. This qualifies an undifferentiated 'infinite loops' description.

### Table A7 — Supplementary policy metrics, p. 17

Using the same listed Ns as A6, entry/budget/revisit/mean phantom hits are GPT 93.0/41.9/44.7/2.8; Claude 23.8/12.1/15.7/1.2; Qwen 96.3/49.0/56.0/3.2; DeepSeek 74.7/54.1/78.0/2.9; Llama 5.6/5.4/24.0/0.6. Its engagement box says zero-tool 43%, search-only 49%, proper engagement 8% with 67% vulnerability, conflicting with Table 7's 1.8% engagement and 87.5% conditional entry. Budget percentages differ materially from entered-run Table 6; denominator/cohort explanations are incomplete.

### Tables A8–A9 — Conceptual comparison and interfaces, p. 17

A8 compares belief/content/wrong-answer failures with navigation/structure/wasted-budget failures. Its 'near-total entry' is a headline for vulnerable agents, not every agent. A9 specifies the four tools and makes the engagement criterion concrete: both `get_paper` and `get_references` at least once. These tables connect conceptual taxonomy to an executable test interface without supplying full implementation code.

## 12. Diagram / Architecture Interpretation

The core control path is: query → agent chooses tool → tool response intercepted by POTEMKIN → transformation returns compromised observation → agent updates verdict or chooses another tool. The attacker acts on the response channel, while the agent's system prompt and weights remain outside the stated attacker's control. Frozen legitimate snapshots and configurable attack definitions supply the proxy's inputs. The outputs are observations that look like ordinary tool responses.

For breadth, the observation bundle includes ten passages and the proxy replaces a configured number with misleading text. Subsequent verdict generation is the evaluated endpoint. For depth, search introduces a fake paper ID, paper retrieval returns credible metadata, and reference retrieval supplies more fake IDs. Directed connections create recurrence or unproductive endpoints. The feedback loop is repeated tool selection based on earlier compromised observations. Figures 1–2 show this architecture and path logic; Figures 6–7 instantiate it with concrete traces.

[D] This architecture explains relevance to web-agent security: tool output influences both assertions and future interaction. It does not establish that browser interfaces, arbitrary websites, or every live API can be intercepted with the same ease. The prototype's tested interception power is stronger and more controlled than many deployment-specific attacker positions.

## 13. Equations and mathematical concepts

### Agent and adversary mappings, pp. 2–3

[A] `A: Q × E → R` maps a query q from query space Q and environment e from E to response r from R. The adversary applies `τ: E → E′`, seeking `A(q, τ(e)) ≠ A(q, e)`. This expresses a changed response after environmental manipulation. [D] A changed response alone does not necessarily mean harmful deception; the later metrics and labels define the harmful outcomes. The formal mapping is an abstraction, not an optimization objective or proof.

### Equation 1 — Drift Rate, p. 3

`DR = E[q ~ Q][1[r ≠ y] | r ≠ ⊥]`.

The expectation averages over queries; `1[condition]` is an indicator equal to one when the condition holds; r is the verdict; y is ground truth; ⊥ means abstention. The metric is the probability of an incorrect verdict among non-abstaining outcomes. Inputs are verdicts, labels, and abstention status; output is a rate. It is used for breadth attacks to distinguish incorrect judgment from recognized uncertainty. Although prose says 'confident incorrect verdicts,' the displayed equation includes no numerical confidence threshold. Abstention frequency must be known separately to assess overall usefulness.

### Equation 2 — Entry Rate, p. 3

`ER = E[q ~ Q][1[there exists t such that s_t ∈ P]]`.

Here s_t is the visited node at step t and P is the phantom-node set. The existential operator asks whether any phantom visit occurs. Input is a navigation trace; output is a proportion of runs with at least one visit. It does not measure repetition, answer corruption, or effort lost. An agent may enter once and escape, or enter and remain trapped, with the same ER outcome.

### Equation 3 — Budget Waste, p. 3

`BW(q) = |{t: s_t ∈ P}| / |{t: s_t ∈ V ∪ P}|`.

V contains valid nodes, P phantom nodes, union combines both, and vertical bars count matching steps. The numerator counts phantom traversals; the denominator counts total valid-plus-phantom traversals. Output is a per-query fraction, reported as percentages in tables. The formula does not itself divide by the configured maximum of ten tool calls. It also does not specify handling when no traversal is recorded; this matters for disengaged agents. Tables sometimes use retrieval calls or total tool calls in descriptions, leaving the exact mapping from calls to node traversals insufficiently explicit.

### Other mathematical quantities

Table 5 defines a relative entry decline from high to low plausibility. [C] For GPT-4o, `(96.7 − 52.4) / 96.7 × 100 ≈ 45.8%`, reproducing its listed discrimination value. This relative percentage differs from the 44.3-percentage-point absolute drop. AUC transfer estimates and bootstrap intervals are statistical summaries, not a theorem establishing independence. No loss function, training objective, formal complexity bound, or proof is supplied.

## 14. Interpretation and discussion

[A] The authors' central explanation is that belief formation and action selection expose different vulnerabilities. A model may distrust persuasive claims yet follow references aggressively. DeepSeek's representative medium-confidence trace illustrates that uncertainty in language does not necessarily stop navigation. Claude's traces instead note missing expected sources and fall back to prior knowledge. These examples support the proposed distinction but are representative excerpts, not a controlled causal intervention on navigation aggressiveness.

[D] The requested research question can be addressed in three source-grounded steps. First, adding tools creates an observation boundary at which an attacker can substitute apparent evidence. Second, retrieval lets that evidence influence factual judgments. Third, repeated navigation lets fabricated structure influence actions and consume finite effort. These are additional mechanisms associated with agent operation. A standalone LLM is not evaluated here, so the study cannot quantify relative vulnerability or separate model susceptibility from agent-scaffold susceptibility through a matched control.

Several consistency problems limit strong synthesis. Table 3 gives 57.9% original-cohort drift at 50% contamination, whereas §4.4 uses 58.4%. Table 5 gives overall cycle entry 59.1%, making the newer 72.7% 'essentially unchanged' claim dependent on an unspecified comparison. Figure A3 and Table 5 disagree on plausibility rates. Appendix A, Figure A2 labels, and its caption disagree on utility, horizontal-axis meaning, and threshold performance. Table A7 and Table 7 disagree on Llama engagement and conditional vulnerability. These cannot be repaired from the supplied work.

The statistical claim also deserves qualification. AUC 0.55 with CI [0.47, 0.67] is compatible with chance, but AUC 0.58 with CI [0.53, 0.62] is above chance by its reported interval. The authors nevertheless describe no predictive power and independence. [D] A restrained conclusion is that cross-dimension transfer is weak and far from a strong general-purpose predictor under their setup. The feature analysis supplies complementary descriptive evidence, not an independent causal proof.

## 15. Contributions and novelty

| Contribution category | Author-presented contribution | Boundary |
|---|---|---|
| Conceptual | AEI, Trust Gap, Grounding Paradox, breadth/depth distinction | Framework and terminology rather than a formal security proof |
| Attack-method | Maze structural traps targeting navigational policy | 'First systematic study' is an author novelty claim, not externally verified |
| System | POTEMKIN interception harness with MCP/Python integration | Implementation and interoperability not independently executed |
| Dataset | S2, PHANTOMS, CLAIMS resources | Source sizes reported; actual releases not inspected |
| Evaluation | Controlled poisoning/style/cycle/plausibility sweeps and conditional reporting | Condition-level sample accounting incomplete |
| Empirical | Robustness Schism and Punishment of Honesty | Findings limited by domain, agents, and reporting inconsistencies |
| Reproducibility | Frozen snapshots, hashes, pinned configurations, seeded states, logs/notebooks | Artifacts described but not supplied |
| Exploratory defense | Safety–utility characterization | Not a comprehensive defense benchmark; Figure A2 unresolved |

[A] The release is described as Apache 2.0 with experiment configurations, anonymized logs covering 11,000+ runs, and analysis notebooks (p. 15). This report neither downloads nor verifies those artifacts. There is no standalone theoretical theorem or training algorithm contribution.

## 16. Limitations

Supplemental analyst source check: physical pages15–16 were rendered and visually inspected after generation. Table A5 and Figure A2 genuinely contain differing utility values and axis descriptions; this is not merely a text-extraction error. Preserve both unresolved values. The source SHA-256 was checked against the authorized PDF; a transcription error in the generated top-level fingerprint was corrected to that observed identity without changing the source or baseline.


### Authors' stated limitations

[A] The main evaluation domain is academic citation graphs. Empirical extension to web search, code tools, and database-backed assistants remains future work. Model snapshots cannot anticipate future releases; specialized and multimodal agents may have different profiles. The defense analysis covers two lightweight techniques, not training-time or architectural defense families. Integration with AgentDojo and InjecAgent is planned rather than completed. Appendix A explicitly says the exploratory defenses are not claimed to solve AEI (pp. 9–10, 13).

### Additional evidence-based analyst observations

[D] There is no matched standalone-LLM comparison, so the user's comparative question is only partially answerable. The formal assumption of no independent verification channel may increase reliance on compromised evidence. Proprietary interfaces and open-source ReAct scaffolds differ, making model and scaffold effects hard to isolate. API failures alter valid sample counts; Qwen's 82% error footnote lacks a reconstructible denominator. Sample allocations, paired framing counts, classifier split procedures, and many uncertainty estimates are absent.

Reporting discrepancies create uncertainty beyond ordinary sampling variation: conflicting appendix plausibility rates, incompatible threshold utility claims, different engagement values, and unexplained cohort sizes. The claim of infinite-loop collapse is stronger than the finite-budget setup and the 0.9% repeated-loop taxonomy alone supports. These are analyst observations; they are not presented as limitations the authors explicitly admitted.

## 17. Threats to validity

The following validity labels are analyst organization of the supplied evidence.

**Internal validity:** Controlled snapshots and deterministic perturbations reduce content drift. Minimal pairs hold topics, claim content, prompts, and approximate lengths constant, strengthening the framing comparison. However, generator artifacts, varying interfaces, and incompletely documented exclusions can still influence outcomes. The authors' training-based explanation for neutral-style susceptibility is not experimentally isolated.

**Construct validity:** Drift Rate omits abstentions; Entry Rate treats any phantom visit as entry even without repetition; Budget Waste uses counted traversals rather than necessarily the full ten-call cap. Engagement-conditioned reporting addresses capability/security confounding, but Llama's engaged subgroup is tiny. 'Escape' includes disengagement, so escape rate cannot automatically stand for competent defense.

**External and ecological validity:** Frozen academic citation tasks provide reproducibility but do not measure all features of live browsing, changing websites, multi-tool collaboration, or production safeguards. The threat model offers a general mechanism; real-world attacker reach and comparative web-agent risk remain untested. The newer cohort broadens model coverage without resolving domain restriction.

**Statistical conclusion validity:** Many tables have no uncertainty intervals. Transfer intervals exist, but one contradicts the broad no-predictive-power phrasing. Missing classifier methodology and per-condition sample counts hinder evaluation of overfitting and dependence. Aggregates may pool heterogeneous conditions and exclusion patterns.

**Reproducibility:** The paper describes strong release practices but the separate artifacts are absent from this input. Conflicting figure/table values prevent a unique reconstruction even before code execution. Hardware and full inference settings are not sufficiently specified for independent reruns from the paper alone.

## 18. Future work and open questions

### A. Author-proposed future work

[A] Extend depth attacks to other graph-structured domains; empirically test web-search agents, code tools, and database assistants; pursue AVeriTeC-based fact checking and graph-RAG scenarios; integrate AgentDojo and InjecAgent; investigate utility-preserving layered defenses. Appendix A proposes source cross-checking and provenance tracking, training rewards for appropriate skepticism, risk-selective defense application, and architectural separation of evidence gathering from belief updating. These are proposed directions, not measured solutions.

### B. Analyst-identified open questions

[D] How much extra vulnerability appears when the same model is evaluated with and without tools under matched tasks? Which web-agent attacker positions provide enough control to reproduce MitT effects? Can independent verification channels preserve task utility while reducing both error and wasted navigation? Do loop detection and belief verification have additive benefits? How sensitive are results to larger budgets, alternative scaffolds, multilingual evidence, or longer task horizons? Would correcting the conflicting tables/figures change the strength of the claimed dissociation? These questions logically follow from the study but are not author-reported findings.

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model; language-producing component of an agent |
| Agent | Model plus tools and repeated decisions about tool use |
| RAG | Retrieval-Augmented Generation; use of retrieved evidence to ground output |
| AEI | Adversarial Environmental Injection; deception through compromised observations |
| MitT | Man-in-the-Tool; adversary positioned on returned tool content |
| MCP | Model Context Protocol; harness integration interface |
| SEO | Search Engine Optimization; one discussed route to influence discoverability |
| Trust Gap | Difference between assumed benign tools and actual manipulation exposure |
| Grounding Paradox | Deference to evidence can reduce hallucination yet increase attack exposure |
| Breadth / Illusion | Poisoning immediate retrieved evidence to change judgment |
| Depth / Maze | Fabricated graph structure that redirects navigation |
| Epistemic drift | Incorrect non-abstaining verdict under the drift metric |
| Policy collapse | Unproductive navigation through fabricated structures |
| Phantom node | Fake paper record introduced into the graph |
| Professor / Wire / Rumor | Formal-authoritative, neutral-news, and informal-hedged styles |
| Phantom / Signal / Glitch | High-, medium-, and low-plausibility fake-paper conditions |
| Hedge / Booster | Uncertainty wording versus confident wording |
| ReAct / Reflexion | Named agent scaffolds; full algorithms not supplied |
| DR / ER / BW | Drift Rate / Entry Rate / Budget Waste |
| ASR | Attack Success Rate; separate success metric used in defense analysis |
| Utility | Task completion on clean inputs in the defense table |
| SHAP | Named feature-attribution method; full acronym not expanded by the paper |
| AUC | Area under the curve, used for cross-dimension classifier transfer |
| FPR | False-positive rate, used in threshold-defense discussion |
| pp | Percentage points; difference between percentages |
| A, Q, E, R | Agent mapping, query space, environment space, response space |
| q, e, r, y | Query, environment instance, verdict, ground-truth label |
| τ | Adversarial transformation of the environment |
| ⊥ | Abstention |
| s_t, V, P | Node visited at step t, valid nodes, phantom nodes |
| ρ, ℓ | Contamination fraction and cycle length |
| h5 | Venue authority cue; exact index definition not supplied |
| ∇ | Relative high-to-low plausibility entry decline |

## 20. Key numerical results

All source values below are author-reported; rendered table values are also visually readable where indicated. Derived quantities are explicitly marked.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Original agents | 5 | agents | Main cohort | Author-reported | p. 4, §3.2 |
| Victim temperature | 0.0 | temperature setting | Main evaluation | Author-reported | p. 4 |
| Step limit | 10 | tool calls/task | Main evaluation | Author-reported | p. 4 |
| Authentic papers / chains | 9,878 / 1,797 | records / chains | S2 snapshot | Author-reported | pp. 4, 15 |
| Fake-paper items | 4,281 | items | PHANTOMS | Author-reported | p. 15, A2 |
| Entry-paper subclasses | 163 / 75 / 71 | papers | Phantom / Signal / Glitch | Visually readable | p. 15, A2 |
| Other fake nodes | 3,972 | items | 4,281 − (163 + 75 + 71) | Analyst-derived | p. 15, A2 |
| Claims / variations | 150 / 450 | claims / scenarios | CLAIMS | Author-reported | p. 15, A2 |
| Breadth valid runs | 5,064 | runs | Table 3 aggregate | Visually readable | p. 6 |
| Depth listed runs | 5,336 | runs | Table 5 aggregate including Reflexion | Visually readable | p. 6 |
| Table 3 + Table 5 counts | 10,400 | runs | 5,064 + 5,336; not full run reconciliation | Analyst-derived | p. 6 |
| Overall clean breadth error | 7.9 | % | No attack | Visually readable | p. 6, T3 |
| Overall contamination drift | 40.2 / 55.8 / 57.9 | % | 10 / 30 / 50% poisoning | Visually readable | p. 6, T3 |
| Drift increments | 15.6 / 2.1 | percentage points | 55.8−40.2 / 57.9−55.8 | Analyst-derived | p. 6, T3 |
| Overall style drift | 42.4 / 54.8 / 36.9 | % | Professor / Wire / Rumor | Visually readable | p. 6, T3 |
| True-claim errors | 14.5 / 6.8 | % | Hedge / Boost | Visually readable | p. 6, T4 |
| True-claim framing gap | 7.7 | percentage points | 14.5−6.8 | Author-reported | p. 6, T4 |
| True-claim framing ratio | 2.1 | times | Authors' rounded ratio | Author-reported | p. 6 |
| False-claim errors | 43.1 / 45.7 | % | Hedge / Boost | Visually readable | p. 6, T4 |
| GPT / Qwen trap entry | 94.6 / 96.1 | % | Principal cycle analysis | Visually readable | p. 6, T5 |
| Overall plausibility entry | 55.4 / 53.5 / 26.4 | % | Phantom / Signal / Glitch | Visually readable | p. 6, T5 |
| Llama engaged counts | 8 / 450 | runs | Proper engagement | Author-reported | pp. 7–8 |
| Llama engaged trap entry | 87.5 | % | 7 of 8 engaged runs | Author-reported | p. 8, T7 |
| Reflexion conditional entry | 68.6 | % | Engaged Llama follow-up | Author-reported | p. 8 |
| Transfer B→D | 0.55; [0.47, 0.67] | AUC; 95% CI | Cross-dimension classifier | Visually readable | p. 15, A4 |
| Transfer D→B | 0.58; [0.53, 0.62] | AUC; 95% CI | Reverse transfer | Visually readable | p. 15, A4 |
| Shared predictive variance | <5 | % | Authors' feature-overlap report | Author-reported | pp. 8, 15 |
| New-cohort mean DR / ER / BW | 42.5 / 72.7 / 35.9 | % | 50% contamination / 3-hop cycles | Visually readable | p. 8, T8 |
| Clean utility, no defense | 83 | % | Exploratory defense analysis | Visually readable | p. 15, A5 |
| Defended utility | 48 / 54 / 58 | % | Perplexity / Spotlighting / Both | Visually readable | p. 15, A5 |
| Defended depth ASR | 0.0 | % | All three tested defenses | Visually readable | p. 15, A5 |
| Multiple-revisit loop share | 0.9 | % | N=2,308 taxonomy cohort | Visually readable | p. 17, A6 |

No approximate plot readings are used as exact numerical results. Conflicting Figure A2 and A3 values are discussed separately rather than merged into this reference table.

## 21. Claim–evidence map

| Major claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Environmental outputs are an attack boundary | Explicit MitT transformation and interception implementation | Framework; F1; T A9 | pp. 2–4, 17 | HIGH for author-defined mechanism; live compromise not demonstrated |
| Breadth poisoning changes verdicts | Drift above clean error under contamination/style conditions | T3; X1a–1c; F4A–B | pp. 5–7 | HIGH within setup; exclusions and denominators incompletely detailed |
| Neutral style has greatest aggregate drift | 54.8% Wire vs 42.4% Professor and 36.9% Rumor | T3; X1b | p. 6 | HIGH result; training explanation is interpretation |
| Hedging true claims is penalized overall | 14.5% vs 6.8%; matched-pair design | T4; X1d | pp. 5–6 | HIGH reported aggregate; not universal across agents; test details absent |
| Structural traps induce high entry | GPT 94.6%, Qwen 96.1%; clean entry 0% | T5–6; X2a–2c | pp. 6–7 | HIGH for listed tables; supplementary cohorts differ |
| Low entry can reflect disengagement | Llama 8 engaged of 450, 7 trapped | T7 | pp. 7–8 | HIGH principal evidence; conflicting appendix engagement box |
| Scaffolding affects measured robustness | Engagement 1.8→11.4%; conditional entry 87.5→68.6% | Reflexion follow-up | pp. 7–8 | MEDIUM inference; different engaged subsets and small baseline subgroup |
| Breadth/depth predictors transfer weakly | AUC 0.55 and 0.58 with reported intervals | F5; T A4 | pp. 8, 15 | HIGH numbers; MEDIUM for broad independence conclusion |
| Newer agents retain depth risk | Mean ER 72.7%, Qwen 99.0% | T8 | p. 8 | HIGH within follow-up; original-cohort comparison inconsistent |
| Lightweight defense costs utility | Utility 83→48/54/58 while depth ASR reaches 0% | T A5 | p. 15 | HIGH table reading; threshold figure/prose inconsistent |
| General web-domain validation remains open | Explicit domain limitation | Limitations | pp. 9–10 | HIGH negative finding |
| Agents add tool-mediated failure paths | Observation poisoning plus graph navigation | Framework and experiments | pp. 2–3 | MEDIUM analyst inference; no standalone comparator |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant doing homework with a search tool. If someone replaces some search results with convincing false information, the assistant may repeat it. That is the paper's first attack: changing the evidence so the answer becomes wrong.

Now imagine that the search results point to a fake paper, and that paper points to more fake papers that refer back to each other. The assistant can waste its limited time following those references. It might even say it is uncertain while continuing down the wrong path. That is the second attack: changing the map the assistant follows, rather than only changing the statements it reads.

The researchers found that these two problems need separate attention. Being harder to fool with misleading text does not reliably make an agent good at escaping misleading reference networks. They also found that cautious wording on true claims sometimes made agents reject those claims more often. Defenses reduced attacks in one exploratory test, but also reduced success on ordinary tasks.

For the question about web agents versus standalone language models, the paper shows why tools can create extra opportunities for deception: attackers may control apparent evidence and the links that guide later actions. It does not run the direct comparison needed to say how much more vulnerable web agents are. Its main tests involve academic papers and citation graphs, and several reported numbers disagree across the paper.

## Completeness Audit

This audit compares the explanation against the supplied-object inventory, not against length alone. 'Fully represented' means the substantive content relevant to interpretation is accounted for, not that every sentence or bibliographic entry is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Metadata and abstract | Yes, text and p.1 image | Yes | Fully represented | Original title, authors, venue, central claims |
| §1 Introduction and Contributions | Yes | Yes | Represented in compressed form | Motivation, novelty claims, scope; analogy compressed |
| §2 AEI | Yes | Yes | Fully represented | Environmental feedback threat |
| §2.1 Formal Framework | Yes; p.2 text-only, p.3 visual | Yes | Fully represented | Agent mapping, attacker capabilities, grounding paradox |
| §2.2 Attack Taxonomy | Yes, visual and text | Yes | Fully represented | Parameters, outcomes, equations |
| §3 Setup | Yes | Yes | Fully represented | System/evaluation role |
| §3.1 MitT Architecture | Yes | Yes | Fully represented | Proxy, MCP/Python, snapshots, seed |
| §3.2 Agents | Yes | Yes | Fully represented | Models, interfaces, temperature, budget, scaffolds |
| §3.3 Conditional Reporting | Yes | Yes | Fully represented | Engagement definition and caveats |
| §3.4 Credibility Gradient | Yes | Yes | Fully represented | Hypothesis and parallel manipulation |
| §3.5 Red Team | Yes | Yes | Fully represented | Gemini family and overlap rationale |
| §3.6 Datasets | Yes | Yes | Fully represented | Sizes, origin, subclass footnote |
| §3.7 Experiment Design | Yes | Yes | Fully represented | Seven principal experiments and minimal-pair controls |
| §3.8 Analysis Methods | Yes | Yes | Fully represented | SHAP and transfer; missing configuration identified |
| §4.1 Breadth Results | Yes | Yes | Fully represented | Main rates, model exceptions, framing |
| §4.2 Depth Results | Yes | Yes | Fully represented | Entry, waste, plausibility, traces, engagement, Reflexion |
| §4.3 Unified Analysis | Yes | Yes | Fully represented | AUC, features, strength qualification |
| §4.4 Frontier Validation | Yes | Yes | Fully represented | Conditions, exclusions, all model rows |
| §5 Related Work | Yes, text-only | Yes | Represented in compressed form | All four categories; individual citations not independently checked |
| §6 Conclusion | Yes, text-only | Yes | Fully represented | Main claims with numerical caveats |
| Authors' Limitations | Yes, text-only | Yes | Fully represented | Domain, snapshots, defense scope |
| Ethical Considerations | Yes, text-only | Yes | Represented in compressed form | Closed-network setup and dual-use rationale |
| Acknowledgments | Yes, text-only | Partly | Inspected but deliberately compressed as non-substantive | Funding and thanks do not alter results |
| References | Yes, text-only | Categories represented | Inspected but deliberately compressed as secondary | Bibliographic list not reproduced; no citation validation |
| Objectives and hypotheses O1–O7/H1–H2 | Yes | Yes | Fully represented | Analyst IDs; no invented formal author RQs |
| X1a, X1b, X1c, X1d | Yes | Yes | Fully represented | Distinct conditions retained |
| X2a, X2b, X2c | Yes | Yes | Fully represented | Structure, plausibility, baseline retained |
| Engagement and Reflexion analyses | Yes | Yes | Fully represented | Small subgroup and appendix conflict flagged |
| SHAP and transfer analyses | Yes | Yes | Fully represented | Predictive versus causal distinction |
| Frontier-model replication | Yes | Yes | Fully represented | Domain scope retained |
| Defense X3/X3b | Yes, text and tables; A2 text-only | Yes | Uncertain | Main table represented; threshold contradictions unresolved |
| Figures 1, 2 | Yes, direct images | Yes | Fully represented | Architecture and directed paths |
| Figures 3, 4, 5 | Yes, direct images | Yes | Fully represented | Panels, axes, encodings, approximate/unlabeled values bounded |
| Figures 6, 7 | Yes, direct images | Yes | Fully represented | Representative traces, not aggregate proof |
| Figure A1 | Text/caption only | Yes | Represented in compressed form | No claim of direct visual inspection |
| Figure A2 | Text/caption only | Yes | Uncertain | Axis and performance contradictions |
| Figure A3 | Yes, direct image | Yes | Fully represented | Exact labeled entries and Table 5 disagreement |
| Tables 1–8 | Yes, text and rendered pages | Yes | Fully represented | Main numeric conditions and footnotes retained |
| Tables A1–A4 | Yes, text and image | Yes | Fully represented | Generation, data, experiments, intervals |
| Table A5 | Yes, text and image | Yes | Fully represented | Defense results; sample details absent |
| Tables A6–A9 | Yes, text and image | Yes | Fully represented | Taxonomy, alternate metrics, interfaces, conflicts |
| Equations 1–3 | Yes, direct image and text | Yes | Fully represented | Symbols, denominators, abstention, missing zero handling |
| Agent/adversary mappings | Yes | Yes | Fully represented | No theorem or harmfulness proof inferred |
| Algorithms, proofs, theorems | None identified | Absence stated | Missing from supplied material as artifact types | No pseudocode or formal proof supplied |
| Appendix A | Yes, text-only | Yes | Fully represented | Defenses and proposed mitigation families |
| Appendix B, B.1–B.5 | Yes; partly visual | Yes | Represented in compressed form | All behavior types; long response excerpts compressed |
| Appendix C | Yes, visual and text | Yes | Fully represented | Both attack traces |
| Appendix D | Yes, visual and text | Yes | Fully represented | Release, reproducibility and extensibility claims |
| Appendix E | Yes; p.16 text-only | Yes | Fully represented with uncertainties | All tables/figures accounted for |
| Separate supplementary files | No | Absence disclosed | Missing from supplied material | Code, data, logs, notebooks, pinned configs not inspected |
| Major contribution categories | Yes | Yes | Fully represented | Conceptual, method, system, data, evaluation, empirical |

### Missing or inaccessible material

Direct rendered images are absent for pages 2, 9–13, and 16. Their supplied text was read; Figures A1–A2 were not visually inspected. Referenced repository contents, frozen datasets, cryptographic receipts, model configurations, seeds, execution logs, notebooks, and custom YAML/plugin implementations are absent. The manuscript does not specify full hardware/software details, per-condition run counts, exact framing-pair sample sizes, all p-values/intervals, classifier splits, or a standalone-model baseline. These are missing evidence, not silently completed work.

### Uncertain interpretations

1. Original-cohort 50% drift: Table 3 gives 57.9%; §4.4 uses 58.4%.
2. New-cohort entry described as essentially unchanged: Table 8 mean is 72.7%, while Table 5 overall is 59.1%; reference cohort/conditioning is unclear.
3. Figure A3 plausibility entries conflict with Table 5, including GPT Glitch 75% versus 52.4%.
4. Figure A2 labels say safety and 90% utility at threshold 100; caption describes ASR and no high-utility/low-ASR defense; Appendix A says 58% utility at that threshold.
5. Llama proper engagement and conditional vulnerability: Table 7 gives 1.8% and 87.5%; Table A7 box gives 8% and 67%.
6. Main/appendix depth cohorts and budget denominators differ without a full mapping; these may be different subsets but cannot be automatically reconciled.
7. Table A4's reverse-transfer interval excludes chance despite broad 'no predictive power' wording.
8. Figure 3's breadth aggregation and SHAP shared-variance computation are not fully specified.
9. Exact plot error bars, unlabeled SHAP values, and Figure A3 citation rates cannot be recovered confidently.
10. The approximately 11,000/11,000+ total is not uniquely reconstructed from the principal tables; Qwen's 82% API-error denominator is unclear.

### Deliberately compressed material

Repeated statements of the breadth/depth distinction are synthesized once and cross-referenced. Representative agent-response quotations are paraphrased while preserving all behavioral types and trace metrics. Individual reference entries, author contact details, acknowledgments, and decorative diagram icons are not reproduced. Figures that repeat table values are explained by their encodings and trends without duplicating every cell again. Release promises are represented as promises, not validated artifacts.

### Potential omissions

Every identified substantive supplied section, subsection, experiment, figure, table, equation, appendix, hypothesis/objective, contribution, and author-stated limitation is represented or explicitly marked uncertain. This does not establish completeness of absent supplementary artifacts or correctness of contradictory reporting. Fine visual detail on unrendered pages, undisclosed implementation details, and a quantitative standalone-versus-web-agent comparison remain unavailable. The coverage claim is limited to the supplied inventory.
