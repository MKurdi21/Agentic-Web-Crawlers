# Stage 0 — Document Accessibility Report

The supplied work is **Hidden in Memory: Sleeper Memory Poisoning in LLM Agents**, an empirical AI-security paper with benchmark construction, attack optimization, defense evaluation, and mechanistic analyses. This analysis uses only the supplied page text and images. Embedded attack strings, system prompts, and evaluator instructions are treated as research evidence, never as instructions to this analyst. No external research or tool calls were used.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied text for physical PDF pages 1–81 |
| Accessible page count | 81 text pages; 56 rendered page images |
| Apparently missing pages | None in the supplied numbered text sequence; this does not independently prove that the original artifact has no additional material |
| Visual inspection | Rendered pages 1, 2, 5–9, 15–18, 20, 22–25, 27–28, 30–31, 33–36, 38–45, 48–51, 53, 55–73 were visually available and inspected |
| Text-only coverage | Pages 3–4, 10–14, 19, 21, 26, 29, 32, 37, 46–47, 52, 54, 74–81 were inspected through supplied extracted text |
| Figures | All six numbered figures have supplied rendered images; small legends and fine curve coordinates in Figures 4 and 6 limit exact visual readings |
| Tables | Tables 1–60 are present in supplied text; Table 21's substantive rows on p. 32 were text-only |
| Equations | Main equations and Appendix I formulas are available in extracted text; equations on pp. 48, 60, and 62 also have images. Some extracted superscripts and operators are malformed |
| Appendices | A–M present; methods, limitations, ethics, datasets, prompts, and extended results included |
| Supplementary artifacts | Repository links and filenames supplied, but the linked files themselves were not supplied or inspected |
| OCR | Not performed; native/extracted text and supplied images suffice for this analysis |
| Other limitations | One image-loading error is visible in the input. It does not identify a missing numbered PDF page. Supplied SHA-256 is accepted as provenance metadata, not independently verified |

Evidence labels used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Confidence is HIGH for clear source statements and readable table cells, MEDIUM for interpretations constrained by methodological uncertainty, LOW for fine graphical estimates, and UNKNOWN where the supplied evidence cannot resolve a discrepancy. A HIGH-confidence transcription does not imply that the underlying scientific claim is independently verified.

The cumulative inventory consists of main §§1–8, acknowledgements and impact statement, references, Appendices A–M, Figures F1–F6, Tables T1–T60, Equations E1–E8 plus Appendix I and K formulas, and the experiment register X1–X15 below. The narrative represents every substantive inventory family, with repetitive examples and large matrices compressed explicitly.

# 1. Plain-language orientation

[A] This paper studies an assistant that remembers information between conversations. An attacker changes a document, webpage, email, repository, or similar material that the assistant reads. The malicious text persuades the assistant to record a false statement about the user. Later, the original document is gone, but the false memory may return and affect the assistant's answers or actions. The authors call this **sleeper memory poisoning**: the attack can lie dormant until a suitable future task activates it (pp. 1–4).

The key difference from an immediate prompt injection is persistence. A malicious page need not make the assistant misbehave immediately. It can instead change the assistant's stored understanding of the user, making future misuse look like personalization or compliance with a remembered workflow. The authors describe a one-to-many effect across future conversations, but the experiments primarily measure specified later-session evaluations rather than a longitudinal count of repeated harms.

The researchers construct a reusable attack template, optionally rewrite its target memory to improve retrieval, and evaluate three separate stages: writing the memory, retrieving it, and using it adversarially. They test six target models, two writing architectures, three retrieval configurations, conversational tasks, and simulated tool-using agent tasks. They also evaluate defenses, production-interface transfer, and internal model signals.

[A] In the no-defense tool-based condition, behavior-memory injection reaches 99.4% for GPT-5.4 and 99.8% for GPT-5.5. In standardized downstream agent evaluations, goal-adjacent adversarial usage ranges from 60% to 89%, conditional on the malicious memory being available in context. These are different stages and denominators: neither number alone is the full attack-chain success probability (Tables 1–2, p. 7).

[D] For the user's research question, the paper supplies a specific explanation for increased agent risk: external content can corrupt durable state, and tools can turn a later interpretation of that state into action. It does **not** provide a controlled standalone-LLM-versus-web-agent experiment establishing a general vulnerability ratio.

# 2. Document roadmap

Main §1 motivates cross-session attacks; §2 positions them relative to prompt injection, tool attacks, and memory poisoning. §3 defines the memory system and threat model. §4 explains reusable payload optimization and retrieval-aware rewriting. §5 specifies datasets, memory regimes, retrieval mechanisms, and metrics. §6 presents injection, activation, end-to-end, production-validation, and defense results. §7 summarizes activation and attention analyses. §8 concludes with memory-governance implications (pp. 1–9).

Pages 10–13 contain acknowledgements, an impact statement, and references. Appendix A states limitations; B discusses ethics and disclosure; C details attack generation; D documents dataset construction; E describes provider rendering and the external writer; F expands injection results and failure traces; G compares retrieval; H analyzes post-injection behavior; I defines coupled end-to-end estimates; J details defenses; K develops mechanistic analyses; L reports ablations and production validation; M documents prompt structures and judge rubrics (pp. 14–81).

The appendices materially qualify the main claims. Appendix D shows that the principal downstream experiment uses standardized, directly saved paraphrases with cross-model fallback. Appendix I gives actual-injection-conditioned compositions. Appendix E explains reconstructed prompts and synthetic memory interfaces. Appendix M reveals that an agent-action YES can mean an attempt or acceptance, not necessarily completed harm.

# 3. Background and context

[A] A **large language model (LLM)** generates responses from its input context. A **stateful assistant** additionally retains information across sessions. Its **memory bank** contains user facts, preferences, habits, or workflow instructions. **Memory writing** selects information to retain; **memory retrieval** selects retained information for a later request; **generation** uses that information to answer or act (p. 3).

**Prompt injection** means untrusted content is interpreted as instructions that compete with the user's or system's intent. **Indirect prompt injection** arrives through material the assistant processes, such as an uploaded document or retrieved webpage. The paper's attack uses indirect delivery to contaminate persistent memory rather than merely changing the current response (pp. 2–3).

A **tool-based memory writer** lets the target LLM invoke a save/edit interface. An **external memory manager** is a separate model that extracts memories after the target responds. These writing architectures must be distinguished from an **external retrieval manager**, which selects stored memories for a future query. The paper uses different models for these jobs: Gemini-3.1-Flash-Lite for the main external writer, GPT-OSS-20B for the retrieval agent (pp. 29, 39).

An **embedding** represents text numerically. **Cosine similarity** compares embedding directions. **Top-k retrieval** returns the k highest-ranked memories; here it does so without a minimum relevance threshold. **Goal-adjacent** queries concern the malicious memory's topic without directly requesting its objective; **goal-distant** queries concern other topics.

[A] The authors position their study against ordinary prompt injection, agent/tool-selection attacks, direct memory-store or retrieval-corpus poisoning, and multi-turn query attacks. Their claimed distinction is the combination of delayed activation, reusable templates, and external delivery without direct memory access. These are the authors' literature characterizations, not an independent assessment of all cited work.

# 4. Research problem and gap

[A] Existing problem: useful long-term personalization can preserve an adversary's fabricated understanding of the user. Once stored, malicious content may outlive its external source and regain influence when a later request makes it relevant (pp. 1–3).

According to the authors, previous approaches often examine immediate prompt-injection harm, direct poisoning of memory/knowledge stores, multiple attacker interactions, or white-box optimization. Such assumptions fit their single-document, black-box, external-content setting less closely. They therefore investigate whether one reusable template can write many different malicious memories through ordinary document processing (pp. 3–6).

The research gap is the complete **write → retrieve → use** pipeline under delayed activation. A memory-write success is insufficient if retrieval suppresses it; retrieval is insufficient if the assistant declines to use it. Conversely, an assistant may resist writing dangerous memories yet remain vulnerable if a future attack succeeds in placing one.

The scope includes behavior manipulation and operational agent goals, several document sources, two writing regimes, three retrieval configurations, and model-specific harnesses. It excludes a systematic evaluation of deletion, correction, user review, provenance-aware editing, repeated exposure, or multiple poisoned documents in one session (Appendix A, p. 14).

# 5. Research questions / objectives / hypotheses

[A] The paper does not introduce a formally numbered hypothesis list. Its explicit objectives are to measure whether external adversarial content produces a fabricated memory, whether that memory is retrieved later, and whether it influences behavior. It seeks a universal injection template and a meaning-preserving retrieval-oriented rewrite (pp. 3–5).

For traceability, the following are **analyst-assigned objective identifiers**, not invented quotations of author research questions:

- O1: Can an external document induce a semantically correct adversarial memory write?
- O2: Can a reusable template transfer across documents, goals, models, and writing regimes?
- O3: How does future-query proximity affect retrieval and usage?
- O4: How do conversational effects differ from tool-using agent effects within the paper's respective tasks?
- O5: How effective are prompting and detection defenses, including adaptive attacks?
- O6: Do injection examples have detectable activation and attention signatures?
- O7: How much do provider setup, memory-manager choice, wording, position, and language affect results?

[A] Appendix H.1 explicitly asks how often models show goal influence, whether semantic proximity changes susceptibility, and which goal types influence behavior (p. 41). Mechanistic sections investigate separability and transferability. They do not establish a preregistered causal hypothesis that attention necessarily causes compromise.

[D] The user's broader question—why web AI agents are more vulnerable than standalone LLMs—is addressed through mechanisms and task-specific evidence, not directly tested as a general comparative hypothesis.

# 6. Assumptions / threat model

[A] The attacker is black-box and controls external context d in user input U=(q,d). The attacker cannot access model weights, system prompt, memory-writing system, retrieval mechanism, or existing memory bank. It cannot directly read or write memory and is absent from future sessions. It supplies a target malicious memory and an instruction template that attempts to make the assistant store that memory as legitimate user information (p. 3).

The benign query q remains part of the interaction; the adversary changes the accompanying document through d_adv=d⊕P_adv(m_adv). The symbol ⊕ denotes combining benign content with the payload; the supplied text describes embedding/appending rather than specifying a general mathematical algebra for this operation.

Success requires injection, future retrieval, and attacker-aligned usage. The original poisoned document is removed before downstream sessions. This establishes a memory-mediated channel rather than continued exposure to the same source (pp. 3–5).

[A] The main attack is single-shot and document-only. Retrieval rewriting assumes a plausible set of future goal-relevant queries, not access to the actual future conversation. Adaptive defense evaluation allows optimization against the defended prompt format. This is a stronger defense-aware optimization condition than the base attack's no-defense search; its relationship to the strict attacker exclusion of deployed system-prompt access should be kept explicit (pp. 3, 15).

[D] Trust boundaries at issue include external text versus direct user instruction, an assistant completion versus trustworthy user facts, stored memories versus authorized preferences, and contextual information versus authority to use tools. The external writer's blindness to the document prevents direct ingestion of its payload, but not laundering of the malicious claim through the target assistant's reply (pp. 29–30, 75–76).

# 7. Methodology

## 7.1 Study design and attack search

[A] The attack has two optimization stages. The first searches for a reusable memory-write template. The second optionally rewrites the target memory to improve expected retrieval. Downstream usage is measured afterward rather than directly optimized in attack generation (p. 4).

Appendix C uses Kimi-K2.5 as both actor and critic, GLM-4.7-Flash as shadow target, a disjoint development set of 125 document–goal pairs of the behavior type, batches of three documents, up to ten refinements per batch, and approximately 200 overall shadow iterations. Thirty candidates survive initial generation; Claude-Haiku-4.5 tests them on 30 development samples, retaining ten; Claude-Sonnet-4.5 selects the strongest on another 30-document subset (pp. 14–15). The figure simplifies this into iterative refinement followed by frontier validation.

The critic receives truncated current documents, attack text, and outputs; historical raw documents are removed while critiques remain. The actor retains attack/feedback history. This reduces what the authors call context rot. The optimization critic accepts structural tool evidence or a statement of intent to save, whereas final IR requires a persisted semantic match. Search success and evaluation success are therefore not identical constructs (pp. 14, 77–78).

[A] Goal rewriting uses text-embedding-3-small, five iterations, twenty gpt-5.4-mini paraphrases per iteration, and up to 100 raw candidates before parsing, filtering, and deduplication. An LLM same-meaning judge rejects semantic drift; the highest-scoring accepted rewrite is selected, or the original goal remains. Strategies include synonyms, workflow expansion, and first-person phrasing (pp. 15–16).

## 7.2 Datasets and isolation

[A] The injection dataset contains 700 document–goal pairs: 500 behavior and 200 agent-action samples from fifteen sources. Behavior documents are evenly divided into 250 with and 250 without benign prior memories; agent documents into 100 and 100. Sources span books, code, emails, encyclopedia entries, finance transcripts, government reports, legal material, mathematics, news, patents, science, SEC filings, tweets, and two HTML sources (Tables 6–7).

A pool of 700 behavior goals covers promotion, competitor smear, opposing-view discredit, belief alignment, and personal-attribute fabrication. Claude-Sonnet-4.5 generates goals using twenty seeds per subcategory and fourteen goals per seed, with automated format, duplicate, and balance checks. The final 500 behavior pairs do not imply that all 700 generated behavior goals were evaluated as injection samples (pp. 18–19).

Agent goals are generated through Gemini-3.1-Pro-Preview category/domain/constraint tuples and Kimi-K2.5 synthesis. Forty-three constraints across twenty-two domain allocations produce 200 goals: exfiltration 45, system hijacking/resource exploitation 50, brute-force execution 10, sabotage 50, and propagation 45. Table 8 combines the first two hijacking-related groups as 60; Table 9 separates them (pp. 20–22).

[A] The principal downstream dataset contains 200 behavior conversations and 200 agent workspaces, each split into 100 adjacent and 100 distant samples. Behavior conversations have 3–6 turns, generated by Kimi-K2.5. Distant seeds come from WildChat; adjacent conversations use the target goal but are audited by GPT-OSS-20B to reject queries that reveal or execute it trivially (pp. 23–24).

Agent workspaces contain a query, task files, USER.md, IDENTITY.md, and MEMORY.md. Kimi-K2.5 generates tasks/files; Gemma-4-26B-4B generates personas and identities. Foundational memories come from PersistBench. An auditor rejects memory leakage into USER.md. Distant tasks are produced by shuffling query/file tuples while keeping persona and memory consistent (p. 25). These are simulated environments, not demonstrated compromises of live infrastructure.

## 7.3 Crucial distinction: standardized versus coupled downstream evaluation

[A] For the main downstream analysis, the authors directly ask target models to save adversarial goals so that natural paraphrases are available. When a target refuses, a more compliant model's saved paraphrase substitutes. This keeps every downstream sample populated and balanced. Table 10 reports direct-save success, not indirect-document injection (p. 23).

Consequently, the main AUR asks what happens **if a plausible poisoned memory is available**, including some goals the target would otherwise refuse to store. Appendix I separately carries actual injection outputs into later evaluation and composes injection, retrieval, and usage. Its rates cannot be obtained by blindly multiplying Table 1 and Table 2 because the evaluated memories and conditioned samples differ.

## 7.4 Provider harness and external writer

[A] Six target models are GPT-5.4, GPT-5.5, Claude-Sonnet-4.6, Gemini-3.1-Pro, Kimi-K2.6, and DeepSeek-V4-Pro. Main experiments state default settings; Appendix H labels GPT behavior runs medium, while production ChatGPT validation uses Thinking/extended thinking. Exact API revisions, decoding settings, and run dates are not comprehensively supplied (pp. 6, 41, 71).

Prompts are reconstructed from circulated extractions and available official documentation. Claude uses structured memory_user_edits; GPT uses bio; Gemini receives an evaluation-added save_memory interface because available extracts lack a comparable native tool; Kimi and DeepSeek use a generic GPT-derived scaffold. Memory placement differs across configurations (pp. 27–29, 73–74).

Eight file types were probed twice per provider to infer upload representation. Claude uses antml XML; GPT raw text with PDF markers; Gemini a JSON envelope. Main evaluation excludes CSV, XLSX, and XML and applies a shared 16,000-character long-document threshold. These exclusions concern injection rendering; agent task files can include CSV (pp. 25, 28–29).

The external writer uses a Mem0-derived additive extraction prompt, not the Mem0 SDK. It sees only the user's direct query and target completion, not the uploaded document or target system prompt. Gemini-3.1-Flash-Lite Preview high is the default writer. Any saved memory is tested for semantic alignment, with first matching memory sufficient for success (pp. 29–30).

## 7.5 Retrieval, baseline, metrics, and statistics

[A] Retrieval configurations are full context, GPT-OSS-20B relevance selection, and Qwen-3-Embedding-8B top-k retrieval with k=15 or 5 from pools of 40–60 memories. Full context assumes retrieval probability one. The User Review baseline hides a fabricated user preference in a purported review appended to the document (pp. 6, 39–40, 75).

IR is semantic target-memory writing; RR is subsequent selection of poisoned memory; AUR is influence/use given its availability. Behavior AUR counts ratings 2–4 on a four-level rubric. Agent AUR counts pursuit, attempt, claim, acceptance, or relevant movement toward the malicious goal under the supplied judge rules; it is not restricted to completed malicious execution (pp. 79–80).

Behavior judging uses Kimi-K2.5 calibrated on fifty human ratings from five annotators, quadratic weighted kappa 0.7288. Agent judging uses Gemma-4-26B, with two false positives in eighty audited predictions, reported accuracy 97.5%. Semantic-save judging and no-write classification are separate functions (pp. 77–80).

[A] Appendix F reports percentile bootstrap confidence intervals with 1,000 resamples at prompt-entry level and 2.5th/97.5th percentiles. Tables 19–20 display half-widths. No comprehensive multiple-testing procedure, significance-test register, hardware specification, end-to-end runtime, or operational cost analysis is supplied. A fixed seed is mentioned for benign-save sampling, but its numeric value is absent (pp. 31, 57).

# 8. Experiments / analyses

| ID | Purpose and setup | Main results and caveats |
|---|---|---|
| X1 | Universal indirect injection: six targets, two writers, 500 behavior and 200 action pairs, AC versus User Review | Table 1: near-ceiling GPT behavior writing under tools; much lower Claude action writing. No-defense condition |
| X2 | Direct-save standardization: all goals saved explicitly, fallback on refusal | Table 10: behavior average 90.3%, action 88.1%; enables controlled downstream tests rather than representing attack success |
| X3 | Standardized downstream behavior/action, adjacent versus distant | Tables 2, 29–35: strong semantic-proximity effect; action usage includes attempts and acceptance |
| X4 | Retrieval configurations: full context, relevance agent, top-k embeddings | Tables 27–28: distant action retrieval remains 98–99% even at k=5; exact main/appendix RR disagreement unresolved |
| X5 | Fixed-attack and attack-family coupled compositions | Tables 36–37: five models, actual injection-conditioned components; semantic E2E borrows external-manager usage |
| X6 | Four prompt defenses versus AC and defense-aware AC+ | Tables 3, 19–20: protection uneven; Kimi GEPA behavior IR rises 6.2% to 64.6% with adaptation |
| X7 | GEPA development/transfer | Table 38: GPT-5.4 attack write rate 0.86→0.01; Kimi-K2.5 0.94→0.38; benign save 1.00 |
| X8 | LLM document scanner: 900 source documents, twenty template variants, random sentence insertion | Tables 39–41: strong detection/localization for larger scanners; zero reported benign FPR; no integrated attack-chain reduction reported |
| X9 | Benign memory functionality under naive/GEPA defense | Table 42: 840 generations, overall write 0.999, semantic match 0.951; no uploaded document |
| X10 | Activation probes across six open-weight models, 125 unique development examples | Table 43/Figure 4: several AUROC values above 0.98; document-group split details insufficient to exclude sibling-example leakage |
| X11 | Cross-model representation alignment and transfer | Table 44/Figure 5: shared PCA near chance, Procrustes 0.74–0.85; not a proprietary-model demonstration |
| X12 | Attention outcome analysis: 125 examples/model/position, end versus random | Tables 45–47/Figure 6: success-associated attention patterns; observational, not causal intervention |
| X13 | Position and wording ablations | Tables 48, 53–55: internal placement matters for defended Kimi; explicit save/urgent wording dominates in a separate no-defense study |
| X14 | Multilingual context: 200 documents, twenty languages, English payloads | Tables 49–52: high no-defense IR persists; not a translated-payload evaluation |
| X15 | Production transfer and provider-setup swap | Tables 56–59: selected successful attack transfer; full setup strongly changes IR, so model-only rankings are insufficient |

Additional stratifications include goal-category aggregates, benign-memory conditions, and no-write failure types (Tables 21–26). They are diagnostic analyses with denominators distinct from single no-defense AC results.

# 9. Results

[A] **Injection is highly condition-dependent.** Under tool-based AC, behavior IR across GPT-5.4, GPT-5.5, Sonnet, Gemini, Kimi, and DeepSeek is 99.4, 99.8, 64.2, 88.6, 95.0, and 96.2%. Agent-action IR is 97.0, 91.5, 6.5, 67.0, 81.0, and 88.5%. External-writer AC behavior IR is 80.4, 75.0, 13.6, 54.2, 78.8, and 86.4%; action IR is 61.5, 46.5, 5.5, 59.0, 65.0, and 82.5% (Table 1, p. 7).

[C] GPT-5.5 behavior improvement over User Review under tools is 99.8−4.2=95.6 **percentage points**, not a 95.6% relative improvement. Claude's corresponding action IR is only 6.5%, showing why downstream conditional vulnerability must not be equated with whole-chain vulnerability.

[A] **Semantic proximity drives activation.** Standardized behavior AUR is 42–85% adjacent versus 0–6% distant. Action AUR is 60–89% adjacent versus 6–17% distant. These differences are reported as 42–79 percentage points for behavior and 54–72 points for action (Tables 30, 34). The paper interprets this as contextual assimilation: poisoned preferences or workflow constraints resemble useful context (pp. 8, 46).

[A] **Hard-to-write does not imply harmless once stored.** Data-exfiltration goals are relatively difficult to inject in category aggregates, but their downstream agent AUR ranges from 44.4% to 66.7%. This is a stage-specific reversal, not a contradiction: avoiding storage and avoiding action after storage are different defenses (Tables 21–22, 33).

[A] **Retrieval design matters.** The relevance agent retrieves distant behavior poison only 3–8% of the time; semantic k=15 retrieval yields 34–44%. Reducing k to five brings distant behavior RR to 3–6%, but distant agent-action RR remains 98–99%. A broad operational vocabulary can remain similar to otherwise unrelated agent tasks (Tables 27–28).

[A] **Full-chain rates are lower and differently conditioned.** Fixed-attack external-retrieval E2E for adjacent behavior is 41.0–73.9%; adjacent action is 3.0–66.0%. Distant external-retrieval E2E is 0–1.0% behavior and 0–5.0% action. Semantic action estimates reach 27.5% distant because retrieval is effectively complete in that experiment (Table 36).

[A] **Prompt defenses resist some attacks but do not transfer uniformly.** GEPA gives near-zero IR for Sonnet and Gemini in the principal tables, but Kimi adaptive behavior reaches 64.6%, and DeepSeek reaches 25.2% in Tables 3/20. The main prose says 21.8% for that DeepSeek result; the discrepancy remains unresolved. Adaptive attack performance can also decrease, so adaptation is not uniformly beneficial (pp. 8–9, 31).

[A] **Harness effects are large.** GPT-5.5 overall IR on a fixed 100-sample swap set is 97% under GPT-style, 3% under Claude-style, and 1% under Gemini-style. The swap changes tools, prompt family, identity, memory placement, and document representation together; it cannot identify which individual component explains the difference (Tables 57–59).

[A] **Detection is promising but not a demonstrated complete defense.** Gemma-4-26B scanner localization is 0.955/0.958/0.985 across behavior/action/multilingual corpora. Activation PCA64 diagonal QDA achieves 0.9329–0.9888 across the six models. These are detection measures, not observed elimination of the full sleeper pipeline (Tables 39, 43).

# 10. Figure-by-figure interpretation

## Figure 1 — Three-stage threat model (p. 2)

[B] The left panel shows an attacker modifying a document; a red dashed arrow carries malicious text to a writer assistant. A blue memory-writing path stores entries in a central user-memory bank, one highlighted red. The rightward retrieval path leads to an assistant in a later/new chat, supplied a benign query and retrieved context. The final right panels depict agentic harm and behavioral manipulation without a contemporaneous attacker.

There are no numerical axes. Red denotes malicious input/state and warning points; blue depicts memory writing/retrieval; green identifies the later benign query; purple distinguishes behavioral manipulation. The important diagrammatic claim is that the malicious source disappears while its derived state remains. The illustrated harmful endpoints are examples, not experimentally measured values in the figure.

## Figure 2 — Universal-template optimization (p. 15)

[B] Phase 1 contains an attacker LLM, one adversarial template, multiple document–goal pairs processed by shadow LLMs, a critic, and a candidate pool. Critic feedback loops back to the attacker over K iterations. Phase 2 sends candidates to a frontier model and ranks them by injection rate to select the universal template. The diagram compresses the intermediate Haiku filtering described in text. Blue arrows represent refinement/data flow; orange marks final validation. No axes, units, or uncertainty bars appear.

## Figure 3 — Retrieval-aware goal rewriting (p. 17)

[B] A query set becomes query embeddings. Seed goals pass through a paraphraser, yielding candidate goal embeddings. Mean similarity scores rank candidates; an LLM checks meaning preservation before a selected paraphrase or original goal enters the optimized bank. Red/blue short bars encode candidate rankings, not a readable numeric scale. The diagram supports the constrained retrieval objective, not a quantified improvement attributable to rewriting alone.

## Figure 4 — Layer-wise activation-probe AUROC (p. 59)

[B] Six panels cover Gemma-4-26B, E2B, E4B, GPT-OSS-20B, Qwen-3.5-9B, and Qwen-3.6-35B-A3B. Horizontal axes are decoder-layer indices; vertical axes are AUROC from 0 to 1 on linear scales. Colored lines distinguish single-layer and fused classifiers/projections. Layer spans differ by model, so matching horizontal positions do not mean matching absolute layers.

Broadly, several single-layer curves rise from early layers toward strong middle/later discrimination, while fused methods remain high and comparatively flat. Some curves decline near final layers. No visible error bars establish curve uncertainty. Small legends prevent confident color-by-method mapping for every curve; exact method scores come from Table 43, not graph interpolation. The caption's phrase linear separability is broader than warranted for every plotted nonlinear method.

## Figure 5 — Cross-model transfer heatmaps (p. 61)

[B] Three panels display source-model rows versus target-model columns: top-left Procrustes, top-right shared PCA, bottom target-self reference. Annotated cells give AUROC; color bars span 0–1. The shared-PCA panel centers near 0.5, while Procrustes is visibly warmer and annotated approximately 0.74–0.85; native-reference values are approximately 0.77–0.88. Diagonal entries are blank and are not zero observations.

The visual supports improved transfer after orthogonal alignment. Native-reference values repeat across source rows because they are reference evaluations, not ordinary source-trained transfer cells. Exact readable annotations agree with the reported ranges; no heatmap confidence intervals are shown.

## Figure 6 — Attack-to-context attention ratios (p. 64)

[B] Six panels plot layer index against attack/(attack+document) attention ratio, with linear ratio axes. Red solid/dashed curves distinguish successful end/random attacks; blue dashed/dotted curves distinguish failures by placement. Gemma E2B/E4B and GPT-OSS panels show periodic sharp peaks, while Qwen panels are smoother. Success and failure curves often separate, although fine numerical differences are not reliably readable.

A consequential discrepancy is visible: GPT-OSS's blue failure peaks reach roughly the middle of its displayed ratio range, whereas p. 63 states a ratio below 0.05 across layers. This is an **approximate visual observation**, not an exact peak estimate, but it conflicts with that textual upper bound. The graph also shows sawtooth structure in E2B, not emphasized in the prose's alternating-attention grouping. Causal necessity of attention is not established by these plotted correlations.

# 11. Table-by-table interpretation

All results below are [A] unless explicitly marked derived or visually uncertain. Percentages and proportions are preserved in their source units. Long matrices are compressed by retaining their purpose, conditions, important extrema, and qualifications; this is not a cell-for-cell transcription.

| Table | Interpretation, values, and qualifications |
|---|---|
| T1, p. 7 | Six models × two writing regimes × two attacks × two subsets; IR %, 95% bootstrap intervals. Tool AC behavior best GPT-5.5 99.8±0.3, lowest Sonnet 64.2±4.2; action best GPT-5.4 97.0±2.5, lowest Sonnet 6.5±3.5. User Review is much weaker for GPT/Sonnet, but already high for Gemini/Kimi/DeepSeek. External-writer results remain substantial but lower for all AC cells in this table |
| T2, p. 7 | RR and conditional AUR by proximity. Adjacent behavior RR 90–95%, AUR 42–85%; adjacent action RR 94–98%, AUR 60–89%. Distant values much lower. Agent RR for GPT columns disagrees with T27 |
| T3, p. 9 | Four defenses, AC/AC+, tool regime, IR %. Naive defense leaves GPT behavior near 90–97%; GEPA is strong against base attacks but adaptive Kimi behavior reaches 64.6. DeepSeek adaptive GEPA behavior 25.2 conflicts with main prose 21.8 |
| T4, p. 9 | Mechanistic synthesis: single-layer AUROC 0.93–0.99; fused often >0.95; shared-PCA 0.48–0.54; Procrustes 0.74–0.85; native 0.77–0.88. Summary ranges are rounded and do not replace detailed model conditions |
| T5, p. 16 | Four original/rewritten memories illustrating vocabulary expansion and workflow phrasing. No control result measures rewriting's causal retrieval benefit; examples are malicious benchmark goals, not true user facts |
| T6, p. 17 | Fifteen behavior document sources totaling 500; code/email/government/legal each 40, Wikipedia HTML 42, random HTML 10. Source diversity is real within the curated sample, not evidence of all web workloads |
| T7, p. 18 | Same source families totaling 200 action documents; legal 26 is largest, tweets 4 smallest; HTML entries 5 and 15 |
| T8, p. 18 | Behavior goal pool: promotion 151, opposing-view discredit 140, smear 139, fabrication 138, alignment 132, totaling 700. Action categories total 200, with hijacking 60 including the ten brute-force goals separated later |
| T9, p. 22 | Agent taxonomy: 9×5=45 exfiltration, 10×5=50 hijacking, 5×2=10 brute-force, 10×5=50 sabotage, 9×5=45 propagation; forty-three distinct constraints. Domain/constraint products determine sample allocation |
| T10, p. 23 | Explicit direct-save success, not indirect injection: Gemini behavior/action 100/99%, Sonnet 93/56.5%, DeepSeek 68/99.5%; overall averages 90.3/88.1. Refusal fallback supplies downstream memories |
| T11, p. 24 | Conversation lengths 3/4/5/6 turns have 48/54/46/52 samples; shares 24/27/23/26%. Total 200 |
| T12, p. 24 | Distant behavior category counts 44 commercial, 37 political, 19 fabrication; adjacent 40/40/20. Category mix differs slightly across splits |
| T13, p. 25 | Seven query styles. Distant curious/checklist 33/24 versus adjacent 19/10; adjacent formal/direct 18/16 versus distant 6/2. Proximity comparisons also involve different style distributions |
| T14, p. 27 | Prompt provenance: circulated extracts plus cross-checks; generic GPT-derived setup for Kimi/DeepSeek. This documents reconstruction sources, not exact deployment equivalence |
| T15, p. 28 | Memory tools, placement, and safeguards differ: Claude structured edits and malicious-memory warning; GPT bio in separate system context; Gemini/generic save-only stub at prompt end |
| T16, p. 28 | Upload formats: Claude XML, GPT raw text, Gemini JSON snippets; filename/MIME/index visibility differs. Inferred from repeated assistant descriptions, not independent provider internals |
| T17, p. 30 | Six subjects × five writers, seventy samples/cell, 2,100 scores. Gemini writer cells range 15.7–82.9%; Haiku 4.3–40.0. Two timeout entries retain failed samples in denominators |
| T18, p. 30 | Writer pooled IR over 420 samples each: GPT-nano 36.0%, Haiku 24.3%, Gemini-lite 63.8%, DeepSeek-flash 26.0%, Qwen-flash 55.5%. Authors report 2.6× extreme ratio; this is a pipeline-composition result |
| T19, p. 31 | Base-defense IR and 95% interval half-widths. GEPA behavior Kimi 6.2±2.1, DeepSeek 0.4±0.6; hybrid behavior DeepSeek 68.2±4.1 shows substantial residual risk |
| T20, p. 31 | Adaptive-defense intervals. GEPA behavior Kimi 64.6±4.2, DeepSeek 25.2±3.8; action Kimi 37.5±6.3. Sonnet/Gemini mostly zero observed successes; zero bootstrap spread is not proof of population zero |
| T21, pp. 31–32 | Goal-category IR aggregates three attacks × five defense settings, denominator unique goals×15. Behavior fabrication is lowest for every model; action sabotage/hijacking high. Sonnet exfiltration 1/675=0.1%, brute-force 0/150. Not no-defense AC-only rates |
| T22, p. 33 | External-writing goal categories aggregate two attack variants, no defense, denominator goals×2. Sonnet fabrication 9.1% exceeds its other behavior categories; GPT-5.5 exfiltration 7/90=7.8%. Category order is not universal |
| T23, p. 34 | Tool-memory condition aggregates attacks/defenses. Effects mixed: Kimi behavior 37.7→34.5% with memories; GPT-5.4 action 31.1→33.5%. Prior benign memories are not consistently protective |
| T24, p. 35 | External-writing memory condition, two variants. Gemini behavior 19.0→39.0% is notable; Sonnet action 1.0→4.5%. Authors lack evidence to isolate the mechanism |
| T25, p. 36 | No-write failure types, pooled baseline/AC, no defense. Sonnet refusals 41.9% behavior, 61.2% action; GPT behavior failures overwhelmingly ignored. Denominator is no-write cases, excluding wrong-memory writes |
| T26, p. 36 | External no-write types. Sonnet refusals 17.2% behavior, 33.3% action; most other rows are 84–100% ignored. These small no-write counts do not measure total semantic injection failure |
| T27, p. 39 | GPT-OSS retrieval RR. Behavior matches T2; action GPT-5.4/GPT-5.5 adjacent 96/98 and distant 13/19 differ from T2's 98/96 and 13/13. Unresolved |
| T28, p. 40 | Semantic RR, entries k15/k5. Distant behavior 34–44%/3–6%; adjacent action 100/100 all models; distant action 99%/98–99%. Top-k always returns memories; no hard relevance threshold |
| T29, p. 41 | Behavior rating distribution over 200/model. Any influence GPT-5.4 21.0%, DeepSeek 45.5%; strong influence 16.0–38.0%; means 1.38–1.95. Ordinal means should not be read as calibrated harm magnitudes |
| T30, p. 41 | Behavior split n100/model: adjacent 42–85%, distant 0–6%; amplification +42 to +79 percentage points |
| T31, p. 42 | Five behavior payload families; mean promotion 41.5%, fabricated attribute 40.0%, belief alignment 28.0%. DeepSeek fabrication 54% highest; category denominators are not shown here |
| T32, p. 43 | Agent n200/model: used goal 106 Gemini, 97 GPT-5.4, 94 Kimi, 92 GPT-5.5, 91 DeepSeek, 66 Sonnet. Ignored/refused columns do not exhaust non-use for several rows; residual outcomes are not labeled |
| T33, p. 43 | Agent categories combine brute-force and hijacking. Exfiltration highest for every model, 44.4–66.7%; Gemini highest/tied in all four columns. Caption says category sizes are in headers, but they are absent |
| T34, p. 44 | Agent split n100/model: adjacent 82/60/89/80/79/83%, distant 12/6/17/11/13/14% in Kimi/Sonnet/Gemini/DeepSeek/GPT5.5/GPT5.4 order. Four exceed 80%; DeepSeek equals 80% |
| T35, p. 45 | Domain pooled usage: server administration 27/30=90.0%, research 34/54=63.0%; social-media brand work 5/54=9.3%, HPC 17/60=28.3%. Different domain denominators and task types limit clean causal comparison |
| T36, p. 50 | Five-model fixed-attack components/E2E %, actual-injection-conditioned. Adjacent behavior external E2E 41.0–73.9; action 3.0–66.0. Sonnet action 100% conditional usage rests on only 3% injection. Semantic distant Sonnet action n/a because borrowed usage is undefined |
| T37, p. 51 | Best-of-family E2E, denominator dataset samples. Adjacent behavior external max74.0%, action70.0%; semantic action max72.7. Kimi distant behavior external1.1% conflicts with displayed component product near1.0%; caption uses IR instead of IR_any for ctx |
| T38, p. 53 | GEPA transfer reports write rate, not semantic IR. GPT-5.4 attack0.86→0.01; Kimi-K2.5 0.94→0.38; benign1.00. Different Kimi version from main K2.6 |
| T39, p. 55 | Scanner localization proportions: Gemma26B0.955/0.958/0.985, Qwen0.921/0.945/0.968; E2B0.342/0.470/0.365. Fuzzy boundary-anchor criterion differs from exact character recovery |
| T40, p. 55 | Scanner TPR proportions; Gemma0.999/1/1; all reported FPR0.000. Benign denominator and uncertainty are not given here |
| T41, p. 56 | Scanner localization by template bank. GPT-OSS memory0.782/0.830/0.815 exceeds classic0.494/0.600/0.675, contrary to nearby prose claiming GPT-OSS localizes classic better. Small Gemma pattern varies by corpus |
| T42, p. 57 | Benign save six models×two defenses×70=840. Write≥0.986, match0.871–1.000; overall0.999/0.951. One no-write plus forty semantic mismatches; direct-save-only functionality test |
| T43, p. 58 | Ten probe methods×six open-weight models; AUROC. PCA64 single-layer0.9486/0.9329/0.9544/0.9834/0.9768/0.9888; top-four ridge0.9620/0.9187/0.9490/0.9860/0.9903/0.9513. Several fused scores remain below0.95 |
| T44, p. 60 | Best model-pair representational similarities: Qwen pair CKA0.9516, SVCCA0.8760, PA-sim0.6378. Similarity is not detection-transfer performance; Figure5 separately tests transfer |
| T45, p. 62 | End/random attack outcomes125 each. GemmaE4B success83/70, GPT-OSS0/0, Qwen35B58/48. Finite development subset; does not establish universal GPT-OSS immunity |
| T46, p. 63 | Total attention mass×1000. Gemma26B end success/fail0.8/0.5; Qwen35B1.4/0.8. E4B rounds both to0.1, so displayed values cannot establish strict higher success mean there. Zero-success GPT-OSS success0.0 is not an observed success mean |
| T47, p. 64 | Top three outcome-discriminative heads/model. Qwen35B L1H4 Δ0.2592; E2B L14H5 Δ0.2786; E4B L11H6 Δ0.2011. No GPT-OSS ranking because no successful cases; no held-out prediction accuracy supplied |
| T48, p. 66 | Defended adaptive position IR %. Kimi behavior beginning6, quarter61, middle58, three-quarter53, end3; GPT5.5 3/8/8/7/4. Sample allocation description is ambiguous because 100 samples and separate subset percentages are reported |
| T49, p. 67 | Multilingual source counts188 XL-Sum BBC,12 Wikipedia HTML, total200 |
| T50, p. 67 | Twenty languages, ten documents each; ten author-classified low-resource and ten mid/high. Language-resource classification is source-specific, not independently validated |
| T51, p. 67 | English payloads in non-English context, no defense/tool regime. AC GPT5.4 99%, GPT5.5 99.5%, Sonnet66%, Gemini90%, Kimi87.5%, DeepSeek95.5%; baseline GPT1%, Sonnet0% |
| T52, p. 68 | Multilingual defenses. GEPA adaptive Kimi55.5%, DeepSeek17%; GPT5.4 hybrid13→49.5% AC/AC+. Similar model-dependent brittleness, not results for non-English payloads |
| T53, p. 70 | Twenty wording/structure variants, thirty samples/model each. Save/urgent reaches100% in some Kimi/GPT cells; note/indirect mostly0–13.3%. Every tool call matched goal in this ablation, making call rate equal IR here only |
| T54, p. 70 | Structural means: Kimi48.7–52.7%, GPT54.7–58.0%, Haiku10.7–15.3%. [C] Haiku spread15.3−10.7=4.6pp, exceeding prose's approximate3.3pp generalized statement |
| T55, p. 70 | Wording means: save95.8/97.5/24.2%, urgent94.2/97.5/14.2%, remember56.7/72.5/23.3%, note4.2/2.5/0%, indirect3.3/8.3/0% for Kimi/GPT/Haiku. Wording dominates these no-defense variants |
| T56, p. 71 | Selected-success production transfer: ChatGPT24/25, Claude24/25, Kimi22/25, Gemini16/25. Behavior/action splits differ for Claude19/6 versus others13/12. Not random population IR |
| T57, p. 71 | Full provider-swap overall IR on100 samples: GPT5.5 97/3/1%, Sonnet77/36/9%, Gemini98/46/80% under GPT/Claude/Gemini styles |
| T58, p. 71 | Swap behavior n50: GPT5.5 100/4/2%, Sonnet98/66/18%, Gemini96/68/86%; demonstrates interaction with goal type |
| T59, p. 72 | Swap action n50: GPT5.5 94/2/0%, Sonnet56/6/0%, Gemini100/24/74%. Bundled setup change cannot isolate rendering from prompt/tool effects |
| T60, p. 73 | Approximate prompt tokens Claude6.2k, GPT7.0k, Gemini4.5k, generic5.8k, using about4 characters/token. Summarizes safeguards and framing; sizes are estimates, not tokenizer measurements |

# 12. Diagram / architecture interpretation

Figures 1–3 are the substantive architecture diagrams; their content is accounted for above. Their combined information flow is: attacker-controlled source → memory-writing decision → durable memory bank → later selection → response or tool action. The actor–critic loop optimizes the first transition; embedding-oriented rewriting optimizes the later selection transition; downstream usage is separately measured.

[A] Tool-based architecture has one target model making both the document interpretation and save decision. External writing introduces a second gate: the target must place adversarial user information into its completion, then a separate extractor must persist it. The manager's input restriction makes this a response-laundering attack rather than direct document ingestion by that manager (pp. 29–30).

[A] Conversational memory is placed in provider-specific system context; agent memory is in a workspace file. The agent also has persona documents and task files. Information about the actual malicious objective is intended to reside exclusively in memory, preventing task/persona contamination from explaining the measured behavior (pp. 25, 39).

[D] The prospective layered defense architecture is source identification and prompt safeguards plus scanner/probe detection before writing, followed by memory governance. Only its component evaluations are demonstrated; the integrated governance pipeline remains future work (p. 65).

# 13. Equations and mathematical concepts

## E1–E6: Memory system and attack stages (p. 3)

[A] E1: **M′=M∪W(U,M)**. M is existing memory, W is the writing mechanism, U the current input, and M′ the updated bank. Union expresses adding generated memories. The abstraction does not fully model deletion, replacement, ordering, or contradictions among entries.

E2: **y=G(U′,R(U′,M′))**. U′ is a later input, R selects memories, and G generates response y. The equation expresses conditioning on retrieved state, not a guarantee that every selected memory is followed.

E3: **U*=(q,d_adv)=(q,d⊕P_adv(m_adv))**. The attacker combines benign document d with a reusable payload instantiated with target malicious memory m_adv. The user query q is retained.

E4: **m_adv∈W(q,d_adv,M)** describes successful writing. E5: **m_adv∈R(U′,M′)** describes retrieval. E6 repeats generation conditioned on retrieved memories, accompanied by the adversarial-usage requirement. Semantic equivalence, rather than literal membership of an unchanged string, is used operationally by the judge.

## E7: Universal attack objective (p. 4)

[A] **max over P_adv E[I_inj·I_ret·I_use]**, with d sampled from document distribution D, m from goal distribution G_adv, and U′ from a goal-associated future-query distribution Q(m). Each indicator is binary. The product is one only when all three stages succeed. The expectation is an average over conditions, not the largest observed model-specific IR. The actor–critic optimizer targets injection and rewriting targets retrieval; the full product is evaluated afterward.

## E8: Meaning-preserving retrieval rewrite (p. 4)

[A] **m̃*=argmax over m̃∈C(m_adv) (1/|Q|)Σq∈Q sim(e(m̃),e(q))**. C restricts rewrites to meaning-preserving candidates; e embeds text; sim is cosine similarity; Q is the plausible target-query set. The output is a selected rewrite, not a probability. A semantic judge operationalizes the constraint. Notice that Q denotes a query distribution in E7 but a finite query set in E8; their roles differ.

## Appendix I: Coupled success and denominators (pp. 47–51)

[A] For N samples, IR=ΣI_inj/N; RR_R=ΣI_inj I_ret/ΣI_inj; UR_R=ΣI_inj I_ret I_use/ΣI_inj I_ret. Therefore E2E_R=IR×RR_R×UR_R=ΣI_inj I_ret I_use/N. This is conditional decomposition on the same samples, not an independence assumption. Failed injections remain in the full denominator.

The attack-family indicator is a logical OR over template-specific injection indicators: any successful template counts the example once. This changes attacker opportunity and is distinct from one fixed attack. Full-context RR=1, giving E2E_ctx=IR×UR_ctx. Semantic E2E is **approximately** IR×RR_sem×UR_emm because the semantic setting borrows usage from the external retrieval-manager setting.

[C] Using rounded Table 36 GPT-5.4 adjacent behavior components gives 0.94×0.957×0.456=0.41019168, approximately41.0%. This reproduces the reported value approximately; authors use unrounded counts. If a conditioning denominator is zero, UR is undefined, explaining n/a entries rather than a zero usage estimate.

## Appendix K: Representation alignment and attention (pp. 60–64)

[A] Procrustes alignment minimizes **||X_s R−X_t||_F subject to RᵀR=I**. X_s/X_t are source/target feature matrices; R is an orthogonal mapping; the Frobenius norm measures total squared-matrix discrepancy before square root. The notation R here is an alignment matrix, unlike memory retrieval R earlier. Feature-dimension reconciliation is not fully specified in the supplied prose.

The layer attention ratio is **ρ_l=A_l/(A_l+D_l)**: average attention assigned to attack tokens divided by attack plus benign-document attention. It excludes other attention buckets, so it is not the fraction of all model attention allocated to the attack. The per-head outcome difference is **Δ_l,h=meanρ_success−meanρ_failure**. Positive values associate that head with greater relative payload attention in successful cases. Ranking by |Δ| selects strongly separating heads; it does not establish causation or a validated deployment detector.

Table 46 reports aggregate attack mass multiplied by1000. Thus displayed0.8 corresponds to underlying0.0008, not80% attention. The paper's relative increases60% and75% use (0.8−0.5)/0.5 and (1.4−0.8)/0.8 respectively. Superscripts in extracted text are checked against rendered equations where available; no formal theorem/proof contribution is present.

# 14. Interpretation and discussion

[A] The authors interpret the central failure as **contextual assimilation**: malicious memory resembles a useful preference, constraint, or workflow requirement, allowing harmful behavior while apparently fulfilling a benign task. Tools make that assimilation operationally consequential. Memory selection mitigates distant-query activation, but embedding top-k selection can still surface broadly related operational instructions (pp. 40, 46).

[D] O1–O2 are supported by high semantic injection rates and transfer across varied source material, with substantial model/harness differences. O3 is strongly supported by split results. O4 is supported as a difference in observed consequences across separately constructed behavior and action tasks, not a matched causal demonstration that tools increase per-input compromise probability. O5 receives mixed defense evidence; O6 receives strong within-sample detection evidence and observational attention evidence; O7 is supported by ablations that reveal major configuration dependence.

The following consistency ledger preserves unresolved source disagreements:

| Issue | Evidence and implication |
|---|---|
| DeepSeek no-defense behavior IR | T1 p.7 tool96.2%, external86.4%; F.3 p.38 instead uses tool82.2%, claims external is higher, and uses82.2 to explain an action/behavior exception. The table and prose cannot both describe the same cells |
| Adaptive DeepSeek GEPA | Main p.8 says21.8%; T3 p.9 and T20 p.31 say25.2%. Report table result with explicit disagreement |
| Action retrieval RR | T2 p.7 GPT5.4/GPT5.5 adjacent98/96, distant13/13; T27 p.39 adjacent96/98, distant13/19. Condition/version difference not documented |
| Claude injection count | pp.5/23 say fifteen action injections, while T1 action6.5% of200 implies13 [C:0.065×200]. Different variant/count scope could explain it, but is not identified |
| Scanner bank ordering | p.56 says GPT-OSS and small Gemma localize classic better; T41 shows GPT-OSS memory higher in all corpora, E2B memory higher in behavior/action, E4B mixed |
| Scanner headline | p.8 says best localization above0.96; T39 behavior0.955 and action0.958 are below0.96, multilingual0.985 above. Statement needs corpus qualification |
| Attention ratio | p.63 claims GPT-OSS ratio<0.05 across layers; F6 p.64 visibly has substantially higher failure peaks. The metric/plot mismatch is unresolved |
| Strict attention gap | T46 E4B rounded success/failure both0.1; strict greater-than requires unrounded values, which are absent |
| Non-use subcounts | T32 p.43 Gemini ignored91+refused1=92 versus non-use94; GPT5.4 94+6=100 versus103; Kimi98+7=105 versus106; GPT5.5 94+12=106 versus108; DeepSeek96+11=107 versus109. Sonnet85+49=134 matches. Residual categories not labeled |
| E2E family formula/value | T37 caption uses IR rather than IR_any for ctx, although preceding formulation uses IR_any. Kimi distant external1.1 is not reproduced by100%×7.9%×14.3%≈1.1297%, whereas visible retrieval percentage and sample-denominator interpretation also differ from a simple integer100-sample count. Raw counts needed |
| Structural spread | p.69 says clustered within≈3.3pp; T54 gives Kimi4.0pp and Haiku4.6pp [C]. Small overall effect is plausible, but universal3.3 bound is unsupported |
| Template identity | p.69 calls its displayed quick-note wording the original main variant; M.3 pp.75–76 assigns an actually/add-something wording to AC and quick-note wording to AC+. Exact experiment-template mapping is uncertain |
| Reference/editorial errors | J.6 p.55 references Table??; K.3 p.65 assigns prompt defenses to Section7 although they are§6.3. T25 mentions TBD rows although displayed rows have values; T33 promises header sample sizes not shown |

[C] The displayed Table37 Kimi distant product is approximately1.13%, which rounds1.1; this arithmetic explains the displayed value but does not resolve the sample-count issue. The disagreement should therefore be treated as denominator/aggregation uncertainty rather than declared a simple multiplication error. Likewise, the authors' claim that manager choice dominates subject choice is not cleanly supported by the stated narrower within-column spreads: Gemini's writer column spans15.7–82.9%, a67.2-point range, versus39.5 points across pooled writer means. Their2.6× writer comparison is supported; the stronger dominance wording requires a defined comparison model.

# 15. Contributions and novelty

[A] **Conceptual:** delayed externally delivered memory poisoning without direct memory-store access; framing success as writing, retrieval, and usage.

**Methodological/algorithmic:** actor–critic search for reusable injection templates; meaning-preserving retrieval rewriting; separating standardized downstream susceptibility from actual-injection-conditioned end-to-end risk.

**Dataset/benchmark:** curated document–goal pairs, behavior conversations, simulated agent workspaces, goal taxonomies, language variation, and benign-memory conditions.

**Empirical:** six-model, multi-regime injection and downstream results; defense-aware evaluation; scanner and benign-functionality measurements; manager and provider-harness ablations; selected production transfer.

**Mechanistic:** activation separability, alignment-dependent cross-model transfer, and architecture-dependent attention associations.

[D] The material supports these as contributions of the paper. It does not establish an exhaustive first-ever claim against independently examined literature, a proven causal attention mechanism, a complete deployed defense, or a general web-agent/standalone vulnerability ranking.

# 16. Limitations

## Authors' stated limitations

[A] Appendix A lists LLM-judge disagreement, especially borderline indirect influence; partially observable provider memory pipelines relying on leaked/reconstructed/inferred prompts; one adversarial document per session rather than compound or repeated exposure; and lack of systematic deletion, correction, user review, and provenance-aware editing defense evaluation (p.14).

[A] Further author qualifications include small downstream samples when coupling low-IR models; direct-save/refusal fallback in standardized evaluation; semantic E2E as an estimate borrowing usage; insufficient evidence to explain Gemini's prior-memory effect; production Gemini claims of saving without visible memory; and open-weight-only transfer findings that may not extend to proprietary internals (pp.23,38,48,65,71).

## Additional evidence-based analyst observations

[D] The main conditional AUR includes memories obtained through a more compliant model after target refusal, so it measures a forward-looking susceptibility rather than current end-to-end exploitability. Production validation selects previously successful attacks, creating selection bias if interpreted as general population IR. Harness swaps alter multiple components together, preventing component-level attribution.

[D] Agent YES includes claiming, attempting, accepting, asking for details, or reading/editing relevant files. It is broader than completed harmful execution. Behavioral AUR includes mild rating2 cues; rating3–4 provides a stronger but still judge-defined threshold. Different task sets, goals, query styles, and metrics prevent a direct numerical causal comparison of agent and conversational vulnerability.

[D] Detection studies omit deployment overhead and integrated prevention outcomes. Probe samples include benign and two injected variants of the same125 documents; grouping in cross-validation is not described. Without document-level grouping details, leakage through related examples remains unresolved. High AUROC does not specify performance at an operational false-positive threshold.

# 17. Threats to validity

These are [D] analyst-applied validity categories unless the authors explicitly discuss the underlying issue.

**Internal validity:** removal of the original document, memory-only placement, persona auditing, and held-out attack development strengthen attribution to memory. Standardization/fallback and generated adjacent tasks complicate claims about natural attack frequency. Simultaneous harness changes make component causality unresolved.

**Construct validity:** semantic IR measures desired meaning, not every memory write. Behavior ratings capture influence rather than objective factual error alone. Agent AUR measures broad uptake/pursuit rather than guaranteed execution. Scanner localization uses fuzzy anchor similarity≥0.5, so reported success is not exact byte-level boundary recovery.

**Statistical conclusion validity:** bootstrap intervals provide uncertainty for selected rate tables, but clustering by repeated goals/documents and many comparisons are not fully addressed. Eighty judge-audit predictions and fifty human ratings are limited calibration samples. Zero-success cells yield zero empirical bootstrap width without proving zero future risk. Some coupled Sonnet action usage percentages have very small conditioning denominators.

**Ecological/external validity:** provider-specific rendering and production transfer help, but prompts are reconstructed, Gemini/generic tools synthetic, long documents truncated, tasks generated, and agent environments simulated. Selected successful production examples validate transfer rather than estimate field prevalence. English payloads in non-English text test context variation, not fully multilingual attacks.

**Reproducibility:** many prompts are summarized and repository paths supplied, but linked artifacts were not reviewed here. Exact software revisions, random seeds, API settings, raw counts, splits, and timing are incomplete in the supplied document. Discrepancies across tables/prose add uncertainty that raw experiment receipts could resolve.

**Generalizability:** results apply to evaluated models, harnesses, goal distributions, and retrieval policies. They do not establish every agent's vulnerability, every standalone LLM's comparative safety, or persistent recurrence over arbitrary long periods.

# 18. Future work and open questions

## A. Explicit author proposals

[A] Develop safeguards for what assistants write, retain, retrieve, and use; evaluate deletion, correction, user review, and provenance-aware editing; detect/remove/quarantine hidden goals rather than silently ignore them; combine prompt defenses with scanners and activation-based detection; integrate probing into memory-write governance; explore efficient monitoring using selected attention heads (pp.9,14,46,65).

## B. Additional open questions

[D] How much added risk comes independently from persistence, external-content exposure, and tool authority in matched tasks? Which individual harness component explains setup effects? How do multiple exposures, memory conflicts, corrections, and long delays change attack success? Can source provenance remain attached through paraphrasing and extraction? What operational false-positive rate and latency would integrated detection achieve? Do probes generalize to unseen attack families under document-group splits? How often does an accepted agent goal produce completed harmful effects? Can the reported main/appendix discrepancies be resolved through raw counts and versioned configurations?

These are questions motivated by the supplied evidence, not additional experiments performed in this analysis.

# 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model, the response-generating component |
| Agent | LLM-based system operating through tools and task workspaces |
| Persistent memory | Stored information reused across sessions |
| Sleeper memory poisoning | External content induces false memory that affects a later session |
| Universal template | Reusable attack wording instantiated with different target goals |
| AC / AC+ | Base actor–critic attack / defense-aware adaptive variant |
| Actor / critic / shadow | Candidate proposer / feedback evaluator / proxy target |
| IR | Injection Rate: semantic target-memory persistence |
| RR | Retrieval Rate: poisoned-memory selection in later context |
| AUR / UR | Adversarial Usage Rate / usage component; context-dependent influence or pursuit |
| E2E / ASR | End-to-end success / attack success rate; stage meaning must be specified |
| Goal-adjacent / distant | Topically related / unrelated future task relative to poison |
| Contextual assimilation | Poison treated as useful preference, constraint, or workflow context |
| GEPA | Genetic-Pareto textual optimization as described by the authors |
| Spotlighting | Marking document boundaries and identifying content as untrusted |
| TPR / FPR | True-positive / false-positive scanner rate |
| AUROC | Area under the receiver operating characteristic curve, a discrimination measure |
| PCA / RP | Principal component analysis / random projection for feature reduction |
| LDA / QDA | Linear / quadratic discriminant analysis classifiers |
| SVM / RBF | Support vector machine / radial basis function kernel |
| CKA / SVCCA / PA-sim | Centered kernel alignment / singular vector canonical correlation analysis / principal-angle similarity |
| QWK | Quadratic weighted kappa, agreement statistic for ordinal ratings |
| M, M′ | Memory bank before/after writing |
| U, U′, U* | Current input, future input, adversarially modified current input |
| q, d, d_adv | User query, benign document, adversarial document |
| W, R, G | Memory writer, retriever, response generator; R also denotes an alignment matrix locally |
| m_adv, P_adv | Target malicious memory, reusable payload template |
| C(m_adv) | Allowed meaning-preserving candidate rewrites |
| I_inj, I_ret, I_use | Binary stage-success indicators |
| emm / sem / ctx | External retrieval manager / semantic retrieval / full context |
| ρ_l, Δ_l,h | Layer attack-to-document ratio / per-head success-minus-failure difference |

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Injection pairs | 700 | pairs | 500 behavior +200 action | Author-reported | p.5,§5.2 |
| Standardized downstream samples | 400 | samples | 200/subset,100/proximity | Author-reported | pp.23–25 |
| Attack development | 125 | unique pairs | Disjoint behavior development set | Author-reported | p.14,C.1 |
| GPT5.5 behavior IR | 99.8±0.3 | % | Tool AC,95% bootstrap interval | Author-reported | p.7,T1 |
| Sonnet action IR | 6.5±3.5 | % | Tool AC,200 pairs | Author-reported | p.7,T1 |
| GPT5.5 AC baseline gain | 95.6 | percentage points | 99.8−4.2, tool behavior | Analyst-derived | p.7,T1 |
| Adjacent behavior AUR | 42–85 | % | Standardized poison in context | Author-reported | p.7,T2 |
| Adjacent action AUR | 60–89 | % | Standardized poison, broad pursuit criterion | Author-reported | pp.7,44,T2/T34 |
| Overall action uptake | 546/1200=45.5 | % | Six models,200 traces each | Author-reported | p.43,H.2 |
| Fixed adjacent behavior E2E | 41.0–73.9 | % | Five models,external retrieval | Author-reported | p.50,T36 |
| Fixed adjacent action E2E | 3.0–66.0 | % | Actual injection-conditioned chain | Author-reported | p.50,T36 |
| Kimi adaptive GEPA IR | 64.6±4.2 | % | Behavior,tool regime | Author-reported | p.31,T20 |
| Writer pooled IR extremes | 24.3 /63.8 | % | Haiku/Gemini-lite,420 samples each | Author-reported | p.30,T18 |
| GPT5.5 setup swap | 97 /3 /1 | % | GPT/Claude/Gemini full setups | Author-reported | p.71,T57 |
| Gemma scanner localization | 0.955 /0.958 /0.985 | proportion | Behavior/action/multilingual | Author-reported | p.55,T39 |
| Benign semantic match | 0.951 | proportion | 840 defended direct-save samples | Author-reported | p.57,T42 |
| PCA64 single-layer probe | 0.9329–0.9888 | AUROC | Six open-weight models | Author-reported | p.58,T43 |
| Transfer Procrustes /PCA | 0.74–0.85 /0.48–0.54 | AUROC | Aligned cross-model probes | Author-reported | pp.60–61 |
| Human/judge agreement | 0.7288 | QWK | Fifty behavior ratings | Author-reported | p.79,M.5.4 |
| Agent judge audit | 78/80=97.5 | % accuracy | Two audited false positives | Author-reported | p.80,M.5.4 |
| Production ChatGPT/Claude | 24/25 each | successes | Selected prior-success samples | Author-reported | p.71,T56 |
| Production Gemini | 16/25=64 | % | 10+6 successes; selected sample | Analyst-derived | p.71,T56 |
| Haiku structural spread | 4.6 | percentage points | 15.3−10.7 | Analyst-derived | p.70,T54 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External sources can poison future memory | Three-stage model; indirect writing and later activation | F1,T1–2,X1/X3 | pp.2–7 | Strong within evaluated harnesses; not direct memory access |
| Reusable template improves injection | AC versus User Review across conditions | T1,X1 | p.7 | Strong empirical comparison for chosen baseline |
| Proximity increases activation | Adjacent/distant RR and AUR | T2,T27–30,T34 | pp.7,39–44 | Strong association; synthetic tasks and styles differ |
| Agent memory can motivate operations | Goal uptake in546/1200 traces | T32–35,X3 | pp.43–45 | Includes attempts/acceptance, not completed harm only |
| Stage-wise rates overstate full-chain probability if treated as E2E | Coupled conditional decomposition and low Sonnet injection | T36–37,X5 | pp.47–51 | Directly supported; semantic branch estimated |
| Prompt protection is adaptation/model dependent | Kimi/DeepSeek GEPA increases; near-zero Sonnet/Gemini | T3,T19–20,X6 | pp.9,31 | Strong for tested attacks; exact DeepSeek prose mismatch |
| Pipeline setup matters independently of model name | Manager and full-provider swaps | T17–18,T57–59 | pp.30,71–72 | Strong setup dependence; bundled causes not isolated |
| Poisoned input is detectable in representations | High AUROC probes and alignment transfer | T43–44,F4–5 | pp.58–61 | Detection evidence, not integrated defense proof |
| Attention relates to successful injection | Outcome-conditioned means and curves | T45–47,F6 | pp.62–64 | Observational; rounding/plot inconsistency limits strong causal claims |
| Web-agent relevance involves persistence plus tools | External-context threat, memory carryover, agent action | F1,T34,H.3 | pp.2–3,44,46 | Analyst inference; no matched standalone-versus-web-agent comparison |

# 22. Very simple explanation

Imagine an assistant keeps a notebook about you. You ask it to read a document, and that document secretly says something false such as that you always want a particular extra step in your workflow. The assistant may mistake that statement for a real request from you and put it in its notebook. When you return later, the document is gone, but the notebook still contains the false instruction.

The researchers tested three questions separately: does the false note get written, does it get brought back later, and does the assistant follow it? A note related to your new task is much more likely to influence the assistant than an unrelated note. If the assistant has tools, following the note can mean changing files or pursuing another operation, not just giving a biased answer. The reported action rates include attempts and acceptance, so they do not all mean a harmful operation was completed.

Some protective instructions worked well for some models, but adaptive attacks and different memory setups changed the results substantially. Detectors could often recognize malicious text or its internal model signature, although the paper did not demonstrate a finished defense that reliably protects the whole process.

For the question about web agents, the paper helps explain a plausible added danger: an agent can encounter hostile external text, remember it, and later act on it. It does not prove that every web agent is more vulnerable than every standalone language model. That broader comparison would require matched experiments that this paper does not provide.

# Completeness Audit

The denominator is the supplied document inventory, not response length. All81 supplied text pages were inspected; all56 supplied rendered pages were visually considered. Every numbered figure and table is represented. Large tables, prompt examples, references, and repeated explanations are deliberately compressed; no claim is made to preserve every cell or word.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue/abstract,p.1 | Yes,text+image | Yes | Represented in compressed form | Authors: Sidharth Pulipaka, Stanislau Hlebik, Leonidas Raghav, Sahar Abdelnabi, Vyas Raina, Ivaxi Sheth, Mario Fritz; Hlebik/Raghav equal contribution; AIWILD at ICML2026 |
| §1 Introduction | Yes | Yes | Fully represented at substantive level | Persistence, delayed influence, motivation |
| §2 Related Work | Yes | Yes | Represented in compressed form | Prompt, tools, memory categories; citations not externally validated |
| §3.1 Memory /§3.2 threat and objective | Yes,text-only p.3 | Yes | Fully represented | E1–E7 and capability exclusions |
| §4.1 payload /§4.2 rewrite | Yes,text-only p.4 | Yes | Fully represented | Search, constraints, E8 |
| §5.1 setup /§5.2 datasets | Yes | Yes | Fully represented | Regimes and standardized/coupled distinction |
| §5.3 retrieval /§5.4 metrics | Yes | Yes | Fully represented | Three retrievers,conditional metrics |
| §6.1 configuration /§6.2 results /§6.3 defenses | Yes | Yes | Fully represented | Principal result conditions and discrepancies retained |
| §7 mechanistic /§8 conclusion | Yes | Yes | Fully represented | Detection and interpretation separated |
| Acknowledgements/impact | Yes,text-only p.10 | Yes | Represented in compressed form | Funding/support and defensive purpose; personal acknowledgements compressed |
| References,pp.10–13 | Yes,text-only | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliography not individually reproduced or validated |
| Appendix A limitations | Yes,text-only p.14 | Yes | Fully represented | All four principal limitations |
| Appendix B ethics/disclosure | Yes,text-only p.14 | Yes | Represented in compressed form | Dual use,controlled research,authors report contacting support channels |
| C.1 actor–critic/context/filter/adaptation | Yes | Yes | Fully represented | Development sizes,models,filtering,critic criterion |
| C.2 goal rewriting/strategies | Yes | Yes | Fully represented | Candidate counts and meaning check |
| D.1.1 documents | Yes | Yes | Represented in compressed form | T6–7 source matrices compressed |
| D.1.2–D.1.3 behavior taxonomy/seeds/examples | Yes | Yes | Represented in compressed form | Five categories,generation/validation; individual seeds/examples compressed |
| D.1.4–D.1.5 agent synthesis/constraints/examples | Yes | Yes | Represented in compressed form | All five threat categories and43-constraint design; operational examples compressed |
| D.2 standardization/refusal handling | Yes | Yes | Fully represented | Crucial cross-model fallback disclosed |
| D.2.1 conversation cohesion/splits/audit | Yes | Yes | Fully represented | T11–13 and generated style differences |
| D.2.2 workspace/splits/profiles | Yes | Yes | Represented in compressed form | Profile prose decorative example compressed |
| E.1.1 prompt provenance/truncation | Yes | Yes | Represented in compressed form | Paired50 test: full64%,truncated62%; reconstructed proxy qualification |
| E.1.2 tools /E.1.3 uploads /E.1.4 transcripts | Yes | Yes | Fully represented | Format,placement,exclusions,truncation |
| E.2 writer/scoping/scoring /E.2.1 ablation | Yes | Yes | Fully represented | Writer versus retrieval-manager distinction |
| F.1 results /F.1.1 categories /F.1.2 prior memory | Yes | Yes | Represented in compressed form | Full matrices summarized with exact selected cells |
| F.1.3 no-write /F.2 traces /F.3 discussion | Yes | Yes | Represented in compressed form | Refusal versus silent ignoring; text/table disagreements |
| G.1 full context /G.2 manager /G.3 embeddings /G.4 discussion | Yes | Yes | Fully represented | Top-k and RR inconsistencies |
| H.1 behavior /H.2 action /H.3 discussion | Yes | Yes | Fully represented | Severity,proximity,categories,domains,contextual assimilation |
| I definitions/decomposition /I.1 fixed /I.2 family /I.2.1 discussion | Yes | Yes | Fully represented | Conditional denominator and estimated branch |
| J.1 naive /J.2 GEPA /J.3 spotlight /J.4 hybrid | Yes | Yes | Represented in compressed form | Defense policy and two-stage training; exact suffix not duplicated |
| J.5 scanner setup/metrics /J.6 results /J.7 benign saves | Yes | Yes | Fully represented | Localization criterion,FPR limits,functionality |
| K.1.1 extraction /K.1.2 probes /K.1.3 transfer | Yes | Yes | Fully represented | Unique-document count and grouping uncertainty |
| K.2.1 attention methods /K.2.2 means | Yes | Yes | Fully represented | Scaling and outcome conditions |
| K.2.3 profiles /K.2.4 heads /K.2.5 findings | Yes | Yes | Fully represented | F6 conflict and causality caveat |
| K.3 synthesis | Yes | Yes | Fully represented | Open-weight boundary,prospective integrated defense |
| L.1 position /L.2 languages /L.3 variants | Yes | Yes | Fully represented | Condition-specific ablations,not merged |
| L.4 production /L.5 setup swap | Yes | Yes | Fully represented | Selection and bundled setup changes |
| M.1.1 tools /M.1.2 background writing /M.2 extractor | Yes,text+text-only continuation | Yes | Represented in compressed form | Input scope,attribution,integrity rules; linked full prompts absent |
| M.3 payloads /M.4.1 actor /M.4.2 critic /M.4.3 rewrite | Yes,text-only pp.75–77 | Yes | Represented in compressed form | Attack functional design,search/evaluation mismatch,template identity uncertainty |
| M.5.1 semantic /M.5.2 benign /M.5.3 no-write /M.5.4 usage | Yes,text-only pp.77–80 | Yes | Fully represented | Ambiguous outputs scored incorrect; judge calibration and broad YES criterion |
| M.6 scanner prompt | Yes,text-only p.81 | Yes | Represented in compressed form | Conservative source-only detection; full file not inspected |
| Objectives O1–O7 | Yes | Yes | Fully represented | Analyst identifiers; no formal hypothesis register supplied |
| Explicit H.1 questions | Yes | Yes | Fully represented | Influence,proximity,goal type |
| Hypotheses/theorems | No formal register present | Accounted for | Missing from supplied material as formal objects | No invented hypotheses/proofs |
| Experiments X1–X15 | Yes | Yes | Fully represented | Register in§8; secondary stratifications included |
| F1–F3 diagrams | Yes,visually | Yes | Fully represented | Components/arrows/feedback explained |
| F4–F6 plots | Yes,visually | Yes | Represented in compressed form | Fine curve coordinates not transcribed; F6 disagreement preserved |
| T1–T20 | Yes | Yes | Represented in compressed form | Individual entries in table audit |
| T21–T40 | Yes,T21 substantive rows text-only | Yes | Represented in compressed form | Individual entries,denominators and missing labels |
| T41–T60 | Yes | Yes | Represented in compressed form | Individual entries,condition changes and conflicts |
| E1–E8 | Yes,text | Yes | Fully represented | Core symbols and objectives explained |
| Appendix I conditional/OR/full-context formulas | Yes,text+partial images | Yes | Fully represented | Undefined conditional denominator disclosed |
| K Procrustes/attention/head equations | Yes,text+images | Yes | Fully represented | Operator roles and scaling |
| Algorithms/pseudocode | Procedures present; no separate numbered algorithm | Yes | Represented in compressed form | Search,rewrite,GEPA,scanner workflows |
| Major contributions | Yes | Yes | Fully represented | Concept,method,dataset,empirical,mechanistic |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Equal contribution,T17 timeout handling,CI/caption notes |
| Supplementary repository files | No | No | Inaccessible | Links supplied but files not provided; no browsing authorized |

## Missing or inaccessible material

The referenced repository, complete provider/attack/defense/judge/scanner prompt files, raw evaluation traces, detailed experiment receipts, and any separate anonymous supplementary artifact were not supplied as inspectable artifacts. Summaries and excerpts of them in Appendix M were inspected; that is not equivalent to reviewing the full files. Pages outside the56 rendered images were text-only, although their extracted content was available. Exact fine visual values in dense multi-curve plots were not confidently readable.

## Uncertain interpretations

The consistency ledger in§14 lists unresolved main/appendix numbers, template identity, incomplete non-use subcategories, attention plotting contradictions, and editor references. Precise cross-validation grouping, feature alignment dimensions, some sample allocations, operational scanner denominators, and raw unrounded counts cannot be determined from the supplied work. The formal claim that attention is necessary is an author interpretation beyond the observational design's causal identification.

## Deliberately compressed material

The60 tables are individually covered but large matrices are summarized rather than reproduced. Dataset source counts, all43 operational constraints, full seed lists, repeated malicious examples, persona examples, verbatim payloads/defense suffixes, prompt summaries, and references are compressed. Their function, major category structure, key settings, and consequential caveats remain represented. Table5 examples illustrate rewriting rather than establishing separate attack outcomes. Headers,page numbers,rules,decorative icons,and repeated title lines are non-substantive layout elements.

## Potential omissions

No numbered figure, table, major section, substantive appendix family, principal equation, explicit limitation, or registered experiment from the supplied inventory is knowingly left unrepresented. This is a comprehensive representation of substantive available content with disclosed compression, **not** an assertion that every numerical cell, example, or word is preserved. Full supplementary-artifact and independent reproduction verification remain outside the accessible evidence.
