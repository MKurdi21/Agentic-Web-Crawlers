## Stage 0 — Document Accessibility Report

The supplied main document contains extracted text for physical PDF pages 1–20. Fifteen page images are supplied: pp. 1, 2, 4–14, 19, and 20. I inspected those images visually and used the supplied extracted text throughout. Pages 3 and 15–18 were inspected as text only. Therefore, textual page coverage is 20/20, while direct visual page coverage is 15/20. The failed local-image message for `-` does not prevent inspection of the fifteen images embedded in the request. No tools, browsing, external references, or repository files were used.

The supplied 20-page version appears internally continuous: title and abstract, numbered main sections, ethics and availability statements, references, and a short Appendix A. This does not establish completeness relative to the repeatedly referenced full technical report. Appendix A begins on physical p. 19, not p. 11; the supplied automated appendix-detection metadata is inconsistent with the visible document. Tables 1–3, Figures 1–10, Algorithm 1, and the principal equations are accessible. Small plot coordinates and some dense mathematical notation require caution. Exact numerical labels and readable table cells are distinguished below from qualitative visual trends. No OCR was performed or needed for the supplied text; extraction artifacts are checked against images where possible.

Missing referenced material includes the full arXiv/technical-report version; the NP-hardness statement and proof; the detailed proof of Theorem 1; Appendix A.2.1 examples and knowledge-poisoning details; Appendix A.3 FAQs, payloads, prompts, and logs; Appendix B and its defense breakdowns and ablations, including Figure 12; Appendix C and detailed image-to-text experiments; and the linked code repository. These are references to absent material, even though the automated accessibility record reports no supplementary references. No embedded supplementary files were supplied. I cannot assess absent artifacts, verify the supplied SHA-256 against a PDF, or independently reproduce results.

Evidence labels used throughout: [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived, with operands shown; [D] analyst interpretation. No [E] external information is introduced. HIGH confidence means the supplied evidence is clear, not that the result has been independently replicated. MEDIUM indicates inferential or condition-dependent conclusions. UNKNOWN applies to absent details.

## 1. Plain-language orientation

This paper studies how an attacker can place instructions inside an external document that an artificial-intelligence system retrieves while doing an ordinary task. A large language model (LLM) may search an email collection, scientific database, or other corpus before answering. An agent may additionally use tools or delegate tasks to other agents. The problem is indirect prompt injection (IPI): instructions arrive through retrieved material rather than through an authorized user request. [A: pp. 1–3]

The researchers focus on a neglected prerequisite: the malicious document must actually appear in the retrieved results. A harmful instruction sitting somewhere in a database has no effect if the system never reads it. They divide the document into an attack fragment, which states the malicious objective, and a short trigger fragment, which makes the combined document resemble the target query in the retriever's numerical representation. They adapt the Cross-Entropy Method (CEM), an existing probabilistic optimization technique, to find the trigger using embedding-model API access. [A: pp. 2–5]

Across eleven retrieval datasets, optimized documents are retrieved much more frequently than unmodified attack fragments. Across eight embedding models on FiQA, independently optimized attacks obtain 90–100% Recall@5. Downstream experiments include forcing an irrelevant fixed answer, propagating phishing content, misusing email tools, and executing code in controlled agent workflows. A central result is GPT-4o multi-agent code-execution success of 0.80 ± 0.07 for the Fusion variant, compared with 0.02 ± 0.04 in the corresponding single-agent Fusion column. [A/B: pp. 7, 11–12]

For the user's question, the relevant explanation is that retrieval introduces an additional entry point for attacker-controlled content; tools create consequences beyond a wrong answer; and agent handoffs may obscure the original source of instructions. This is an analyst synthesis, not a direct experiment comparing web agents with standalone LLMs. The paper studies retrieval-augmented generation and email-based agents. It does not establish a universal vulnerability ranking for all web agents and standalone models. [D: pp. 3, 9–12]

## 2. Document roadmap

The document combines a cybersecurity study, an algorithm paper, an empirical AI-systems evaluation, and a conditional mathematical analysis. Its organization follows the attack's causal chain.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| S0 | Abstract | 1 | Problem, method, headline outcomes |
| S1 | §1 Introduction | 1–3 | Retrieval gap and four contributions |
| S2 | §2 Problem Formulation; §2.1 Threat Model | 3 | System, attacker, and scope |
| S3 | §3 Prefix Construction Attack; §3.1 Similarity Search for Prefix | 3–4 | Optimization objective and budgets |
| S3.2 | §3.2 Our Algorithm: CEM Attack | 4–5 | Factorization, updates, Algorithm 1, Theorem 1 |
| S4 | §4 Evaluation on Trigger Fragment | 5–6 | Data, models, baselines, defaults |
| S4.1 | §4.1 Effectiveness in Retrieval | 6–8 | Retrieval, corpus competition, model breadth, cost, multimodality |
| S4.2 | §4.2 Transferability of Our Attack | 8–9 | Models, positions, dispersion, attack fragments |
| S5 | §5 End-to-end Evaluations | 9 | Transition from retrieval to downstream effects |
| S5.1 | §5.1 Case Study: RAG | 9–10 | Fixed-answer attack and knowledge poisoning |
| S5.2 | §5.2 Case Study: Agentic Systems | 10–12 | Email agents, four objectives, multi-agent amplification |
| S6 | §6 Evaluation on Defense | 12–13 | Paraphrasing, perplexity filtering, token masking |
| S7 | §7 Related Work | 13 | Three literature categories and contextual defenses |
| S8 | §8 Limitations | 13 | Retrieval scope, transferability, algorithm originality |
| S9 | §9 Conclusion | 13 | Retrieval and system-level security implications |
| ETH/OPEN | Ethical Considerations; Open Science | 14 | Controlled experiments, risks, code availability |
| REF | References [1]–[104] | 15–19 | Bibliographic apparatus; no external validation |
| A | Appendix A: Additional Experiments and Details | 19–20 | Additional metrics and hyperparameters |
| A.1 | Different Metrics | 19–20 | Recall, reciprocal rank, nDCG; Table 3 |
| A.2 | Impact of hyper-parameters in CEM | 20 | Figure 10 and parameter trends |

Visual inventory: F1 is the attack-flow diagram; F2 retrieval-versus-length panels; F3 corpus-competition bars; F4 embedding-model bars; F5 transfer heatmap; F6 position curves; F7 dispersion bars; F8 payload-transfer scatter; F9 RAG success heatmap; F10 hyperparameter curves. Tables T1–T3 cover dataset characteristics, agent outcomes, and detailed retrieval metrics. ALG1 is the CEM pseudocode. E1–E7 are numbered method equations; additional mathematical objects are cosine similarity, the retrieval threshold, and three appendix metric definitions. TH1 is the conditional utility theorem. The corresponding-author footnote on p. 1 is administrative. No keyword list, definitive venue/year line, formal hypotheses, or separate supplied supplement is visible. The artifact badge and ethics wording reference USENIX, but do not by themselves specify a publication venue and year.

## 3. Background and context

An embedding model converts a token sequence into a numerical vector. The paper's retriever represents a query and each document as vectors, compares their cosine similarity, and returns the K highest-scoring items. Cosine similarity measures directional agreement and ranges from −1 to 1 in the paper's definition. The downstream LLM then answers or calls tools. [A: p. 3]

Retrieval-Augmented Generation (RAG) means that retrieved documents are added to the LLM's input context to support answer generation. An agentic system extends this arrangement with planning, tool invocation, or coordination among agents. The examples here use email retrieval, email sending, contact listing, file handling, and Python execution. A multi-agent system distributes these responsibilities among interacting agents. [A: pp. 9–10]

Direct prompt injection or a jailbreak targets the user–model interface. Indirect prompt injection arrives through external data that the system later consumes. The security issue is whether text supplied as information can redirect behavior as if it were an instruction. The authors describe prior evaluations that ensured the harmful item was already in context; their objection is that this bypasses the retrieval barrier. [A: pp. 1, 13]

A trigger fragment is a short token sequence selected to increase retrieval similarity. An attack fragment is the instruction-bearing remainder. The symbol x∥D_adv means their concatenation. A trigger need not be a readable explanation of the query; it is evaluated by its effect on the embedding score. Query+ is the baseline that prepends the user's query itself. Vanilla supplies the attack fragment without a prefix. [A: pp. 3, 6]

Black-box access here is specific: the attacker can submit text to the embedding model and receive vectors, but cannot inspect model parameters, obtain gradients, or read the clean corpus. It does not mean the attacker has no information: optimization assumes a target query and a provided attack fragment. The distinction matters when considering deployment relevance. [A/D: pp. 3–4]

## 4. Research problem and gap

**Existing problem.** Retrieved external content may contain instructions that cause undesired answers, phishing, tool abuse, or code execution. The authors argue that external retrieval is an important attack surface in modern LLM applications. [A: pp. 1–2]

**Shortcomings attributed to previous approaches.** Evaluations may designate the latest email as malicious and explicitly request that email, use a corpus containing only the malicious item, require optimized tokens in the user's query, force tool responses to return the payload, or modify the retriever through a backdoor. The authors say these conditions demonstrate post-retrieval effects without establishing whether natural retrieval would expose the content. These are the paper's characterizations of prior work, not independently verified judgments. [A: pp. 1, 13]

**Research gap.** Can a single malicious item be retrieved among legitimate documents for a natural query, using a practical black-box attacker, and then produce an end-to-end effect? The work connects retrieval manipulation to downstream security outcomes. [A: pp. 2–3]

**Motivation.** In the authors' experiments, Vanilla attack fragments are not retrieved on the eleven benchmark datasets. Merely writing harmful instructions is therefore insufficient in those conditions. White-box optimization violates the chosen threat model, while query repetition is an imperfect black-box baseline. [A: pp. 2, 6]

**Scope.** The empirical core is embedding-based top-K retrieval, predominantly text-to-text retrieval. The controlled downstream cases are RAG and email agents. Hybrid search, reranking, full web browsing, and arbitrary deployed products are not evaluated. The full-version multimodal claim is reported in the supplied text, but its detailed experiment is absent. [A: pp. 8, 10, 13–14]

## 5. Research questions / objectives / hypotheses

The paper supplies explicit prose questions rather than a numbered hypothesis-testing framework.

| ID | Question/objective | Source | Associated evidence |
|---|---|---|---|
| RQ1 | Under realistic corpora and natural queries, will malicious text be retrieved? | p. 2 | Vanilla versus optimized retrieval, F2/T3 |
| RQ2 | Can retrieval be guaranteed or made reliable through a compact black-box prefix? | pp. 2–4 | Optimization formulation, ALG1, F2/T3 |
| RQ3 | What makes retrieval vulnerable or difficult to attack? | pp. 6–7 | Competition level, F3 |
| RQ4 | Are larger, newer, or proprietary embedding models safer? | p. 7 | Eight-model FiQA comparison, F4 |
| RQ5 | Does an optimized trigger retain effectiveness when conditions change? | pp. 8–9 | F5–F8 |
| RQ6 | Does successful retrieval cause downstream compromise? | p. 9 | RAG F9; agent T2 |
| RQ7 | Can the examined countermeasures neutralize the attack? | p. 12 | §6 qualitative defense findings |

The objectives are to formalize a trigger/attack decomposition, adapt CEM to discrete prefix search, provide a conditional utility analysis, and evaluate retrieval and downstream outcomes. There are no explicit null/alternative hypotheses or predeclared statistical significance tests in the supplied version. The conjecture that corpus similarity governs attack difficulty is discussed and examined through grouped averages, rather than established by a formal causal test. [A/D: pp. 2–7]

## 6. Assumptions / threat model

The external corpus is D = {D₁,…,D_m}; each item is a token sequence. Vocabulary V contains the available tokens. Embedding model E accepts sequences up to a maximum length n* and produces d-dimensional vectors. The paper gives Contriever's 512-token limit as an example. A query q is embedded, cosine scores determine top-K retrieval, and the base LLM acts on the query and retrieved content. Experiments focus on K = 5. [A: pp. 3–4]

The attacker provides D_adv and knows the target q for optimization. They may inject exactly one malicious item into the corpus for the query under evaluation. They cannot inspect the clean corpus or the parameters of the retriever or LLM; they have embedding API access. Their construction changes the injected item, not the legitimate user query. The corpus must admit attacker-written material, such as the paper's examples of online sources or email systems. [A: p. 3]

The attack has two distinct success requirements: retrieval exposure and downstream compliance. Problem Definition 1 describes a prefix that puts the attack fragment in top-K and frames this as fulfilling the objective. Later experiments clarify that retrieval alone does not ensure execution: agents sometimes retrieve perfectly while rarely following a particular malicious request. The analysis therefore preserves these as separate events. [A/B: pp. 3, 11]

The empirical evaluation does not assume gradient access, corpus-reading privileges, control over every document, or an already-retrieved malicious item for the realistic attack variants. The Ideal baseline deliberately assumes the last condition for comparison. Payload construction itself is excluded from the core optimization research problem, although selected payload effects are evaluated downstream. [A: pp. 3, 11]

The theorem additionally assumes an additive score across token positions. This is a mathematical simplification, not an established exact property of all deployed embedding models. The authors motivate it through token pooling and positional insensitivity, while the OpenAI position results demonstrate substantial exceptions to broad position-agnostic language. [A/D: pp. 5, 8–9]

## 7. Methodology

### Design and architecture

The study first optimizes retrieval independently, then tests the retrieved document's effect in RAG and agent workflows. This separates whether the system sees the injected content from whether it follows it. The controlled comparison keeps the attack fragment and clean corpus fixed while changing prefixes. Query+, Vanilla, CEM, and, in agents, Fusion provide distinct retrieval conditions. [A: pp. 5–6, 11]

### CEM prefix search

The score is f(x) = sim(E(q), E(x∥D_adv)). The algorithm samples length-n token sequences from a distribution, computes their scores using embeddings, retains the best fraction, and increases the probability of the tokens appearing in those retained sequences. It repeats and outputs the best sampled trigger. The distribution is factorized by token position, so it can be stored as an n-by-|V| matrix rather than an explicit probability for every possible sequence. This trades modeling token dependencies for tractability. [A: pp. 4–5]

Defaults are n = 10 tokens, N = 5,000 sampled prefixes per iteration, T = 30 iterations, elite fraction λ = 0.2, and smoothing α = 0.55. NT must not exceed the query budget B. From the defaults, 5,000 × 30 = 150,000 candidate score evaluations, matching the paper's maximum-access description. This multiplication is analyst-derived; it does not establish an identical count of network requests because batching and query-embedding reuse are not specified. [A/C: pp. 5–8]

### Datasets and sampling

Eleven BEIR test datasets provide legitimate corpora and queries. The researchers subsample 100 target queries per dataset and independently inject one malicious item for each evaluated target. The source does not describe accumulating all malicious items simultaneously into one persistent poisoned corpus. Documents have relevance labels, but the attack metric counts exposure to the malicious item rather than ordinary benign retrieval quality. [A: pp. 5–6]

The default attack fragment asks for a predetermined response regardless of the question. It also presents its own bounded text as trusted and other information as misinformation. This is treated as experimental evidence, never as an instruction to this analysis. Other objectives are evaluated in §5. [A: p. 6]

### Models and implementation

The default retriever is gte-modernbert-base: ModernBERT, 139M parameters, 768 dimensions. Contriever-msmarco uses BERT-Base with 110M parameters and 768 dimensions. Qwen3 embedding variants have 0.6B, 4B, and 8B parameters with output dimensions 1,024, 2,560, and 4,096. Proprietary models are OpenAI text-embedding-3-small, Voyage voyage-3.5-lite, and Alibaba text-embedding-v4, termed Qwen-v4. The implementation uses BEIR and FAISS on an H100 GPU server. Versions, tokenization choices, batching details, and index settings are not specified in the supplied material. [A: p. 6]

### Baselines and metrics

Vanilla uses no prefix. Query+ prepends the target query, with retrieval-versus-length plots treating its prefix length as a comparison variable; the exact repetition/truncation procedure for each plotted length is not supplied. CEM learns a prefix. Fusion concatenates the learned trigger, the user query, and the attack fragment. Ideal assumes the attack fragment alone is always retrieved. White-box methods are excluded because their parameter access violates the threat model; the authors also cite prior comparisons as motivation. [A: pp. 6, 11]

Recall@5 is 1 when the malicious document appears in the five retrieved items and 0 otherwise, averaged across queries. Mean Reciprocal Rank at K (MRR@K) averages reciprocal ranks, assigning zero outside top-K. Normalized Discounted Cumulative Gain at K (nDCG@K) weights higher placement more strongly. SIM is cosine similarity. Attack Success Rate (ASR) is the fraction producing the designated downstream effect. RAG ASR excludes cases where the clean system already answers with the target phrase. [A: pp. 6, 10–11, 19]

### Downstream configurations and statistics

The agent study uses an Enron email history for one user with at least 50 sent and received emails. Claude Sonnet 4 generates ten FAQs from that history. Each query receives one injected email. AutoGen provides the single-agent setting with email retrieval, send-email, contact-list, and Python execution tools; the authors describe round-robin scheduling. Tools use Model Context Protocol (MCP). GPT-4o and GPT-4o-mini are tested. Magentic-One within AutoGen provides orchestration, FileSurfer, Coder, Computer Terminal, and an added retriever agent with email tools. [A: p. 10]

RAG results are averaged over five random seeds. Agent experiments repeat five times with different seeds and report mean ± standard deviation of ASR. Token dispersion averages ten random placements. Appendix retrieval tables show ± values and discuss seed variation, but the exact number of retrieval seed repetitions is not clearly specified in the supplied version. There are no reported p-values, confidence intervals, or significance tests. A standard deviation is not a confidence interval. [A: pp. 8, 10–11, 19–20]

## 8. Experiments / analyses

| ID | Distinct analysis | Setup and manipulated condition | Outcome and caveat |
|---|---|---|---|
| X1 | Retrieval effectiveness | Eleven datasets, 100 queries each, one injection per target, prefix lengths varied, CEM/Query+/Vanilla | F2 and T3 show strong length-dependent gains; Vanilla remains unretrieved in reported conditions |
| X2 | Corpus competition | Group success/failure by similarity of fifth-ranked clean item | F3 associates failures with stronger clean competition; descriptive association |
| X3 | Embedding-model breadth | Eight separately optimized models on FiQA | F4: seven at 100%, OpenAI at 90%; not an eleven-dataset-by-eight-model full grid |
| X4 | Runtime and API cost | Default optimization budget; selected providers/models | Reported $0.21–$0.76 and 1.6–7.6 minutes; costing details absent |
| X5 | Image-to-text retrieval | MS COCO and OpenCLIP, reported in prose | Near-perfect recall claimed; details absent in Appendix C of full version |
| X6 | Cross-model transfer | Trigger built on one FiQA embedding model, evaluated on another | F5 strongly heterogeneous; reference-model knowledge matters |
| X7 | Position transfer | Trigger optimized at position 0, moved through attack text | F6 usually sustained recall; OpenAI nearly collapses around position 20 |
| X8 | Token dispersion | Scatter optimized trigger tokens; ten random dispersions on FiQA | F7: 6–91% across models; broad prose claims exceed some exact labels |
| X9 | Cross-fragment transfer | Reuse one optimized trigger with randomly sampled fragments of varying lengths | F8 raises cosine similarity; sample count and retrieval-success distribution absent |
| X10 | RAG answer manipulation | Eleven datasets; displayed model rows; fixed target answer; five seeds | F9 contains ASR 0.1–1.0; caption/model-count inconsistencies |
| X11 | Knowledge poisoning | NQ, LLaMA-2-7B, single malicious document | ASR 0.58 with two trigger tokens, 0.50 with one; detailed comparison absent |
| X12 | Agent answer manipulation | Ten Enron-history FAQs; two GPT models; four variants | T2: CEM can retrieve nearly perfectly yet produce 0–2% targeted-answer ASR |
| X13 | Phishing/worm propagation | Same query framework; phishing and replication recorded separately | T2 separates transmission of a link from transmission of self-replication instructions |
| X14 | Tool misuse | Enumerate contacts and send phishing content | T2: substantial success; execution does not require overtly harmful code |
| X15 | Single-agent code execution | Retrieved email redirects summarization toward script execution/exfiltration | T2: GPT-4o 2–4%; GPT-4o-mini 4–26%, depending on variant |
| X16 | Multi-agent code execution | Magentic-One handoffs with adapted attack fragment | T2: GPT-4o Fusion 80%; mini Fusion 36%; setup differs from single-agent |
| X17 | Query paraphrasing defense | Rephrase queries; adaptive multi-paraphrase optimization | Small initial degradation reportedly restored; exact breakdown absent |
| X18 | Perplexity defense | Detect unusual text; attacker repeats malicious text | Claimed detection signal reversal; absent F12 prevents numerical verification |
| X19 | Token masking defense | Random token replacement/removal | Claimed limited protection; rates and utility trade-offs absent |
| X20 | Additional retrieval metrics | T3 at n = 3, 5, 10 | Exact Recall/MRR/nDCG values; prose averages conflict with table |
| X21 | Hyperparameter sensitivity | MSMARCO, n = 10; vary T, N, λ, α | F10: more sampling generally improves similarity; no exact optimal settings established |

These experiments address different endpoints. Retrieval success, similarity, phishing-link transmission, worm replication, and file exfiltration cannot be merged into one generic success rate. The distinction is especially important for RQ6: seeing the text and executing its request are empirically separable. [A/B: pp. 9–12]

## 9. Results

**Retrieval barrier.** The authors report that Vanilla is never retrieved across the eleven benchmark datasets. CEM performs better than Query+ at matched plotted lengths, with compact triggers approaching perfect recall on several datasets. At n = 10, Table 3 reports 74.0 ± 13.6% for MSMARCO, 77.5 ± 8.0% for ArguAna, and 100.0 ± 0.0% for five datasets. The table average is 94.1%; prose elsewhere gives a different average. Therefore, the supported conclusion is strong but nonuniform retrieval effectiveness, not an unconditional guarantee for every corpus. [A/B: pp. 6–7, 19–20]

**Competition rather than size alone.** NFCorpus has an average competition level around 0.64 and no failures in the described analysis. MSMARCO failures have competition around 0.82 versus around 0.75 for successes. These approximate author-reported descriptions support an association between the query's strongest clean competitors and attack difficulty. They do not demonstrate that corpus size has no causal effect in every setting. [A: p. 7]

**Model breadth.** Figure 4 labels FiQA Recall@5 as 100% for GTE, Contriever, Q3-0.6B, Q3-4B, Q3-8B, Voyage, and Qwen-v4, and 90% for OpenAI. Larger parameter counts and proprietary access do not eliminate vulnerability in this experiment. This is a restricted empirical result, not proof of universality over all embedding architectures. [B/A: p. 7]

**Transferability.** The Qwen-family block in Figure 5 is strong, while some cross-family cells are weak. A trigger constructed on Q3-0.6B obtains only 10% retrieval on OpenAI. OpenAI-reference triggers have a reported average of 74% across targets. Reusing a trigger is therefore plausible under some conditions but not reliable across arbitrary models. [A/B: p. 8]

**Dispersion.** Figure 7 labels GTE 90%, Contriever 22%, Q3-0.6B 68%, Q3-4B 91%, Q3-8B 80%, Voyage 88%, OpenAI 6%, and Qwen-v4 86%. These values show striking heterogeneity. The prose's strict 'above 90%' and 'exceed 80%' wording does not exactly match GTE's 90 or Q3-8B's 80 labels. [B: pp. 8–9]

**Downstream effects are conditional.** In GPT-4o CEM targeted-answer attacks, retrieval is 1.00 and SIM is 0.85, but ASR is only 0.02 ± 0.04. Conversely, GPT-4o Fusion tool misuse achieves 0.98 ± 0.04 for both sending and phishing. This demonstrates that attack objective and workflow substantially influence harm after exposure. [B: p. 11]

**Multi-agent amplification.** GPT-4o CEM code execution increases from 0.04 ± 0.05 in the single-agent setting to 0.72 ± 0.16 in the multi-agent setting. Fusion increases from 0.02 ± 0.04 to 0.80 ± 0.07. Analyst-derived contrasts are 68 and 78 percentage points, respectively: (0.72−0.04)×100 and (0.80−0.02)×100. The Fusion ratio is 0.80/0.02 = 40, but its small denominator and differing adapted workflows limit interpretation. These are descriptive contrasts, not statistically tested causal effects. [B/C/D: pp. 11–12]

**Defenses.** The authors report that paraphrasing, perplexity filtering, and masking fail to provide durable protection against adaptive variants. The supplied version contains qualitative findings and a '<10%' degradation statement, not the full defense tables. The percentage-drop wording does not specify relative percent versus percentage points, so it is preserved without converting units. [A: pp. 12–13]

## 10. Figure-by-figure interpretation

### Figure 1 — Retrieval-to-action attack flow, p. 2

This is a diagram, not a quantitative chart. A benign user query travels to an agent or base LLM, which retrieves from a corpus using an embedding model. The attacker supplies x∥D_adv: a trigger plus instruction-bearing fragment. Colored points in a schematic vector space distinguish the query, clean documents, attack fragment, and combined malicious text. The visual places the combined text closer to the query than the attack fragment alone. This is explanatory geometry, not measured experimental coordinates. The final branch shows wrong answers/denial of service, spamming, and running code as possible effects. Arrows explain that the attacker acts through corpus content, while legitimate query and tool flows carry the item into the system. [B: p. 2]

### Figure 2 — Retrieval as trigger length increases, p. 7

Eleven panels correspond to the datasets. The x-axis is trigger-fragment length, with labeled ticks 1, 5, 10, 15, 20; the y-axis is Recall@5 (%) from 0 to 100. Red/pink curves represent CEM, blue dashed curves Query+, and green dashed curves Vanilla. Point markers identify sampled lengths. No confidence intervals or significance markers are displayed. Axes appear linear. CEM generally rises earlier and reaches higher recall at a given length; Vanilla stays at zero. MSMARCO and ArguAna remain more difficult, with ArguAna's Query+ curve notably low. Exact coordinates for every point are not labeled; Table 3 supplies exact values for selected CEM lengths but cannot be assumed to resolve every plotted seed condition. [B: p. 7]

### Figure 3 — Clean-corpus competition and attack outcome, p. 7

Grouped bars show average cosine similarity of the fifth-ranked clean document, separated into CEM succeeds and CEM fails. Dataset labels run along x; y is Competition Level with ticks approximately 0.6–0.9. Blue bars indicate success groups and pink bars failure groups. Datasets without failures have only one bar. Failure bars generally stand higher where both groups exist. The nearby text reports about 0.64 for NFCorpus and MSMARCO about 0.82 for failures versus 0.75 for successes. These are author-reported approximate descriptions, not exact extracted bar heights. The truncated lower axis range visually enlarges differences. There are no error bars or correlation coefficients. The figure supports a descriptive ranking-competition explanation. [A/B: p. 7]

### Figure 4 — Eight independently optimized embedding models, p. 7

The x-axis lists GTE, Contriever, three Qwen3 sizes, Voyage, OpenAI, and Qwen-v4. The y-axis is Recall@5 (%) with a 0–100 scale. Pink bars have exact labels: 100, 100, 100, 100, 100, 100, 90, 100. The condition is FiQA, not all eleven corpora. There are no error bars. The figure demonstrates that each tested model can be attacked effectively when optimization targets it; it does not measure cross-model transfer. [B: p. 7]

### Figure 5 — Cross-model transfer heatmap, p. 8

Columns are reference embedding models on which triggers are optimized; rows are target models where they are evaluated. The colorbar is Recall@5 (%) from 0 to 100, with darker blue for larger values. The physical arrangement places Qwen-v4 at the top row and GTE at the bottom; overlooking that reversal would invert conclusions. The displayed diagonal is 100 except OpenAI's 90. Strong Qwen-to-Qwen cells contrast with weaker cross-family transfers. In the OpenAI target row, the Q3-0.6B reference column is 10. In the OpenAI reference column, target recalls, in GTE-to-Qwen-v4 order, are 60, 20, 100, 90, 80, 60, 90, 90. Their sum is 590, so their unweighted mean is 590/8 = 73.75%, an analyst-derived check consistent with the rounded 74% prose. Exactly seven cells are at least 60%; only five are strictly above 60%, so the prose's '7 out of 8 ... above 60%' appears to use 'above' loosely. No seed uncertainties are shown. [A/B/C: p. 8]

### Figure 6 — Moving a trigger optimized at the beginning, p. 9

Eight panels plot insertion position on x, approximately 0–60, and Recall@5 (%) on y, 0–100. Blue lines represent the same initially optimized trigger moved elsewhere. Most models retain substantial recall, though GTE and Voyage fluctuate and Q3-0.6B dips. OpenAI begins near the reported 80% and falls toward zero by around position 20. No exact value is labeled at each position and no error bands appear. The prose reports 60% when directly optimizing at the end; that is a separate condition from merely moving the beginning-optimized trigger. The figure does not justify a universal position-agnostic claim. [A/B: pp. 8–9]

### Figure 7 — Randomly dispersing trigger tokens, p. 9

Eight pink bars show FiQA Recall@5 (%) averaged over ten random dispersions. Exact labels are 90, 22, 68, 91, 80, 88, 6, and 86 in the model order used above. No dispersion variability is drawn. GTE and Q3-4B retain roughly 90%; OpenAI and Contriever fall substantially. This supports robustness to token scattering for several models, while demonstrating important exceptions. It measures retrieval after scattering, not the effectiveness of a detector or downstream harm. [B: p. 9]

### Figure 8 — Trigger reuse across attack fragments, p. 9

The scatter plot uses cosine similarity between query and attack fragment alone on x, approximately −0.2 to 0.8, and similarity after adding a trigger optimized on another fragment on y, approximately 0.7–0.9. Blue points represent random fragments and a pink point the fixed targeted fragment. Low initial similarities cluster near elevated final similarity around 0.75; more query-aligned fragments reach higher y-values. The text gives an example rising from around −0.1 to as high as 0.76. Points are not individually labeled. The y-axis is truncated, and no diagonal equality line is shown; axes must be read rather than judging apparent vertical displacement alone. The experiment supports similarity transfer, while exact sample counts, fragment lengths, and corresponding top-5 success rates are absent. [A/B: p. 9]

### Figure 9 — RAG fixed-answer success heatmap, p. 10

Columns are eleven datasets; rows are twelve visibly labeled LLM configurations. Blue shading encodes ASR on a 0–1 scale and each cell carries a one-decimal label. The attack seeks the fixed answer 'Yes' using one malicious document. Models ending in -Ins are instruction-tuned. Visible rows include six Qwen3 labels, four Llama3 configurations, and two Vicuna models. The caption and prose say eleven LLMs, creating a count discrepancy. DBPedia has high values across rows, whereas some lower-performing rows have 0.1 on particular datasets. Qwen3-8B's FEVER cell is 0.1, which complicates the assertion that Qwen scales behave almost identically. Values span 0.1–1.0, so 'often close to 1' must not be restated as uniformly near-perfect. No uncertainty overlay is given despite the five-seed averaging statement. [A/B: p. 10]

### Figure 10 — Hyperparameter sensitivity, p. 20

Four small line panels vary T, N, λ, and α on MSMARCO with n = 10. Shared y-axis is cosine similarity, approximately 0.7–0.9. T has labeled ticks 20, 60, 100; N 2k, 6k, 10k; λ 0.1, 0.3, 0.5; α 0.5, 0.8, 1. More iterations and samples generally raise the score, with small local fluctuations. Larger elite fractions reduce scores in the displayed range; smoothing changes are comparatively mild. Values are not printed point by point, and there are no uncertainty bars. The plotted endpoint α = 1 sits at the boundary of the earlier stated α ∈ (0,1); the supplied version does not explain that change. Similarity improvements should not be converted into exact recall improvements without further evidence. [A/B: pp. 5, 20]

## 11. Table-by-table interpretation

### Table 1 — Dataset characteristics, p. 6

Rows are eleven datasets grouped by retrieval task. Corpus sizes are in millions of documents; Q-Len and D-Len are average word counts. These are corpus statistics, not the 100-query evaluation sample sizes.

| Dataset | Documents, millions | Query words | Document words |
|---|---:|---:|---:|
| MSMARCO | 8.8 | 6.0 | 56.0 |
| TREC-COVID | 0.171 | 10.6 | 160.8 |
| NFCorpus | 0.036 | 3.3 | 232.3 |
| Natural Questions | 2.7 | 9.2 | 78.9 |
| HotpotQA | 5.2 | 17.6 | 46.3 |
| FiQA-2018 | 0.058 | 10.8 | 132.3 |
| ArguAna | 0.087 | 193.0 | 166.8 |
| DBPedia | 4.6 | 5.4 | 49.7 |
| SCIDOCS | 0.026 | 9.4 | 176.2 |
| FEVER | 5.4 | 8.1 | 84.8 |
| SciFact | 0.052 | 12.4 | 213.6 |

[A/B: p. 6] The smallest listed corpus is SCIDOCS and the largest MSMARCO; ArguAna has unusually long queries. The nearby p. 6 prose describes document lengths as '56 to 232', but the table includes 46.3 and 49.7 and a maximum of 232.3. This is an imprecise prose range, not grounds to change the table. On p. 10, NQ's 9.2 is called tokens, whereas Table 1 says words. That unit inconsistency remains unresolved.

### Table 2 — Agent retrieval and downstream harm, p. 11

Rows compare Ideal, Query+, CEM, and Fusion for GPT-4o and GPT-4o-mini. Columns separate single-agent targeted answers, phishing/worm propagation, tool misuse, single-agent code execution, and multi-agent code execution. R@5 and SIM accompany each task. Ideal has dashes for retrieval and similarity, not numerical zeros. Phishing and Worm are separate outcomes; Sent and Phishing in tool misuse are also separate outcomes. The ± terms on outcome rates are reported standard deviations across five repetitions. Bold and shading are emphasis, not declared significance.

The following transcription retains all downstream means and standard deviations while deliberately compressing repeated R@5/SIM cells into a separate description. Every rate is on a 0–1 scale.

| Model / Method | Targeted answer | Worm: phishing | Worm: replication | Tool: sent | Tool: phishing | Single code | Multi code |
|---|---|---|---|---|---|---|---|
| GPT-4o Ideal | .04±.05 | .77±.11 | .01±.03 | 1±.00 | 1±.00 | .02±.04 | .58±.18 |
| GPT-4o Query+ | .14±.05 | .38±.14 | .08±.06 | .99±.04 | .99±.04 | .02±.04 | .56±.05 |
| GPT-4o CEM | .02±.04 | .66±.17 | .00±.00 | .92±.08 | .92±.08 | .04±.05 | .72±.16 |
| GPT-4o Fusion | .16±.11 | .84±.11 | .18±.13 | .98±.04 | .98±.04 | .02±.04 | .80±.07 |
| GPT-4o-mini Ideal | .00±.00 | .87±.08 | .83±.13 | .47±.19 | .44±.18 | .04±.05 | .54±.23 |
| GPT-4o-mini Query+ | .00±.00 | .51±.11 | .46±.10 | .64±.13 | .63±.13 | .18±.08 | .56±.21 |
| GPT-4o-mini CEM | .00±.00 | .64±.17 | .46±.11 | .58±.18 | .58±.18 | .26±.09 | .42±.08 |
| GPT-4o-mini Fusion | .04±.05 | .74±.09 | .64±.11 | .84±.05 | .84±.05 | .22±.04 | .36±.09 |

[B: p. 11] Retrieval is usually 1.00. The notable exceptions are Query+ worm retrieval at .56 for GPT-4o and .63 for mini, CEM mini targeted-answer retrieval at .98, and Fusion GPT-4o tool retrieval at .98. CEM SIM values for the five task groups are .85/.77/.83/.79/.78 for both models. Fusion values are .88/.81/.87/.85/.85 for GPT-4o and .89/.81/.87/.85/.83 for mini. Query+ values are .76/.70/.78/.73/.76 for GPT-4o and .76/.70/.78/.73/.75 for mini.

The table does not show Fusion winning every endpoint. GPT-4o CEM single-agent code execution is .04 versus Fusion .02; mini CEM code execution is .26 versus Fusion .22; mini multi-agent Query+ is .56 versus Fusion .36. Ideal is strongest for mini worm replication at .83. These counterexamples materially qualify the prose's generalized strongest-ASR language. Perfect retrieval can coexist with near-zero compliance.

### Table 3 — Prefix length and three retrieval metrics, p. 20

Rows are datasets plus averages; columns group Recall@5 (%), MRR@5, and nDCG@5 at n = 3, 5, 10. Higher values mean stronger malicious-document exposure or placement, not better benign security. The following preserves every dataset's Recall values and all n = 10 ranking metrics; n = 3 and 5 ranking cells are deliberately compressed.

| Dataset | Recall n=3, % | Recall n=5, % | Recall n=10, % | MRR n=10 | nDCG n=10 |
|---|---|---|---|---|---|
| MSMARCO | 7.9±3.8 | 35.3±3.4 | 74.0±13.6 | .55±.10 | .60±.10 |
| TREC-COVID | .4±.8 | 7.6±3.2 | 87.6±11.8 | .69±.12 | .74±.12 |
| NFCorpus | 94.0±3.6 | 100.0±.0 | 100.0±.0 | .97±.02 | .98±.02 |
| NQ | 7.0±1.1 | 48.8±3.1 | 98.6±2.8 | .83±.03 | .87±.02 |
| HotpotQA | 11.4±2.2 | 80.4±2.4 | 100.0±.0 | .90±.04 | .93±.03 |
| FiQA-2018 | 31.6±3.4 | 73.4±2.4 | 97.8±3.9 | .87±.01 | .90±.02 |
| ArguAna | 1.8±.7 | 16.6±.8 | 77.5±8.0 | .40±.03 | .49±.04 |
| DBPedia | 45.8±8.3 | 91.4±5.9 | 100.0±.0 | .97±.03 | .98±.02 |
| SCIDOCS | 24.0±3.0 | 78.2±2.5 | 100.0±.0 | .88±.02 | .91±.02 |
| FEVER | 10.2±1.6 | 62.4±4.2 | 99.8±.4 | .63±.03 | .72±.02 |
| SciFact | 77.8±3.0 | 98.6±.8 | 100.0±.0 | .92±.01 | .94±.01 |
| Reported Average | 28.4 | 63.0 | 94.1 | .78 | .82 |

[B: p. 20] The reported average MRR values across lengths are .18, .45, .78; nDCG averages .20, .49, .82. All displayed dataset mean metrics increase with length. At n = 3, NFCorpus is already strong while TREC-COVID is near zero. At n = 10, five datasets tie at exact displayed 100%; NQ is 98.6 and FEVER 99.8. MRR shows that top-five retrieval does not always mean first place: FEVER has nearly complete exposure but MRR .63, lower than NFCorpus and DBPedia .97.

The appendix prose on p. 19 reports n = 3 average Recall 29.5%, n = 10 Recall 95.6%, and MRR .79. Table 3 reports 28.4%, 94.1%, and .78. The prose also lists NQ and FEVER among 100% datasets, contrary to the table. I cannot determine which experimental aggregation the prose intended. The table is transcribed as displayed, without silently replacing either source.

## 12. Diagram / architecture interpretation

Figure 1 separates three stages: the user submits a benign query; the retriever exposes external documents; the base model or agents act on the combined input. The attacker changes the data path by inserting a document into the corpus. The trigger alters its ranking; the attack fragment attempts to redirect the action path. The colored vector-space sketch illustrates how adding the trigger can move the combined representation toward the query. It does not depict changing the embedding model's parameters. [B/A: pp. 2–3]

The single-agent implementation joins retrieval and other tools within AutoGen. The multi-agent implementation delegates file access, code writing, and code execution among specialized components. An additional retrieval agent supplies email-related capabilities. The authors suggest that a code executor may receive Python from a teammate without seeing the original malicious text or user request. That explanation is explicitly tentative in the paper and cannot be validated against the missing logs. [A: pp. 10, 12]

Analyst interpretation: the architecture can transform external content into an apparently internal instruction through intermediate messages. This is a useful explanation of the reported multi-agent amplification, but no standalone-versus-agent architecture diagram or controlled provenance-isolation ablation is supplied. The concrete evidence is the differing code-execution outcomes in the tested workflows. [D: pp. 10–12]

## 13. Equations and mathematical concepts

**Cosine similarity, §3.1, p. 3.** sim(u,v) = uᵀv / (||u||₂ ||v||₂), for vectors u,v in Rᵈ. The numerator is a dot product; the denominator normalizes vector lengths. The output expresses directional alignment. The supplied paper does not specify handling of zero-length vectors. E(q) and E(document) supply its inputs.

**Equation (1), p. 4.** f(x) = sim(E(q), E(x∥D_adv)). This maps a candidate prefix to one score while q, D_adv, and E remain fixed. Its role is the black-box optimization objective. Increasing f increases the injected document's competitiveness, but the unknown clean-corpus threshold prevents a unconditional empirical guarantee.

**Retrieval condition, p. 4.** The displayed threshold is f(x) > min{τ : |{D∈D ∧ sim(E(D),E(q))>τ}|≤K}. The intended meaning is to exceed the relevant clean-document ranking threshold. The paper then states that K=1 gives the maximum clean similarity, and later defines competition by the K-th-ranked clean document. There is a potential indexing/tie ambiguity: allowing up to K clean scores strictly greater than τ appears different from allowing only K−1 documents ahead of the injected item. Equal-score handling is unspecified. I report the displayed condition and the authors' interpretation without repairing it. [D: pp. 4, 7]

**Equation (2), p. 4.** The ε-optimal objective is f(x) > f(x*)−ε for x∈Vⁿ. Here n bounds prefix tokens, Vⁿ is the finite sequence search space, x* denotes an optimal sequence, and ε>0 allows an optimization error. The printed argmax expression uses f(x*) inside the maximization rather than f(x), which appears self-referential. Its contextual intent is clear enough to describe, but the literal notation is flagged. A near-optimal score is not itself a guarantee of defeating every clean corpus.

**Equation (3), p. 4.** p(x)=∏ᵢ₌₁ⁿ pᵢ(x[i]). This is a factorized probability distribution. pᵢ(v) is the probability of token v at position i. Multiplication represents independent positional choices. The n-by-|V| storage avoids an explicit |V|ⁿ joint table. Token interactions in the real embedding score may remain, even though sampling ignores dependencies.

**Equation (4), p. 5.** p⁽ᵗ⁾(xⱼ)=∏ᵢ₌₁ⁿ pᵢ⁽ᵗ⁾(xⱼ[i]). This applies the factorization at iteration t to sampled candidate j. Inputs are the current token probabilities; output is that candidate's sampling probability. N candidates are sampled independently.

**Equation (5), p. 5.** S={xⱼ : |{xₖ : k≠j, f(xₖ)≥f(xⱼ)}|≤λN}. S is the elite set: high-scoring candidates used for the next update. λ∈(0,1) determines the retained fraction. Algorithm 1 describes exactly λN highest-scoring samples; the set formula can behave differently at ties or integer boundaries. Rounding and tie-breaking are not supplied.

**Equation (6), p. 5.** pᵢ⁽ᵗ⁺¹⁾(v)=(1−α)pᵢ(v)+α p̂ᵢ(v). This blends the existing distribution and the elite empirical distribution. α controls how strongly selection changes sampling. The right-side pᵢ lacks an iteration superscript in the displayed equation; nearby text identifies it as the current distribution. Smaller α preserves more previous mass; larger α follows elite counts more strongly. That explanation follows directly from the formula.

**Equation (7), p. 5.** p̂ᵢ(v)=[Σⱼ₌₁ᴺ 1{v=xⱼ[i] ∧ xⱼ∈S}]/|S|. The indicator contributes one when an elite sequence has v at position i. Dividing by elite-set size converts counts into frequencies. These frequencies feed equation (6).

**Algorithm 1, p. 5.** Initialize uniform positional distributions, construct f, repeat sampling/evaluation/selection/update for T iterations, and output the best sequence. The budget condition is NT≤B. Naive greedy search is described as n|V| score evaluations; brute-force sequence search as O(|V|ⁿ). These are the authors' method comparisons, not measured timing baselines in the supplied version.

**Theorem 1, p. 5.** If f((x₁,…,x_n))=Σᵢ fᵢ(xᵢ), then the authors state T=O(log|V|) and N=O(log(1/δ)) suffice for f(x)≥f(x*)−ε with probability at least 1−δ, for δ∈(0,1). Their proof sketch says elite updates amplify good-token probability. The detailed proof is absent, and dependencies hidden in the big-O constants are not assessable. The theorem's non-strict ≥ also differs from equation (2)'s >. It supports a conditional optimization claim, not a proven corpus-independent retrieval or execution guarantee.

**Appendix metrics, p. 19.** Recall@K = number of relevant items retrieved / total relevant items. Here there is exactly one malicious item, so per-query Recall is binary. Reciprocal Rank@K is 1/rank when rank≤K and zero otherwise; MRR averages it. nDCG@K is displayed as 1/log₂(i+1), where i is malicious-document rank and the maximum at i=1 is 1. The displayed nDCG equation omits an explicit zero case outside top-K, so truncation handling is not fully specified by that formula alone. These metrics distinguish exposure from how early the injected item is encountered.

## 14. Interpretation and discussion

The experiments answer the main retrieval question with a conditional yes: under the tested embedding-based settings, a single optimized item can repeatedly surface for ordinary benchmark queries. They also show that unoptimized payloads can substantially underestimate risk. Query+ partly addresses exposure, but CEM searches a broader discrete space and usually reaches higher similarity with fewer trigger tokens. [A/B: pp. 4–7]

Downstream evidence changes the meaning of 'success'. Retrieval is a necessary entry point for these attacks, while instruction following depends on payload and agent behavior. Table 2 makes this visible: targeted-answer attacks can fail despite perfect exposure, and routine email-tool workflows can succeed at high rates. Therefore, a strong retrieval result should not be described as automatic execution of arbitrary instructions. [B/D: p. 11]

For the user's research question, this paper supports three possible mechanisms: external-data exposure, action capabilities, and coordination across agents. The first is measured directly through retrieval manipulation; the second through email and code endpoints; the third through multi-agent code-execution outcomes. The broader claim that web AI agents are more vulnerable than standalone LLMs remains analyst inference because neither a web-agent study nor a matched standalone control is supplied. [D: pp. 3, 9–12]

Important source inconsistencies remain unresolved:

| Issue | First source | Conflicting or qualifying source | Treatment |
|---|---|---|---|
| Appendix averages | p. 19: 29.5%, 95.6%, MRR .79 | T3 p. 20: 28.4%, 94.1%, .78 | Preserve both |
| Perfect-recall datasets | p. 19 includes NQ and FEVER at 100% | T3: NQ 98.6%, FEVER 99.8% | Use table for tabulated condition |
| RAG model count | p. 10 prose/caption: 11 | F9 visibly has 12 rows | Flag count discrepancy |
| Qwen size range | p. 10 prose: 0.8B–32B | F9 labels start at 0.6B | Do not infer intended model roster |
| Dispersion thresholds | p. 8: GTE above 90%, Q3-8B exceeds 80% | F7: 90 and 80 | Preserve exact labels |
| OpenAI transfer threshold | p. 8: seven targets above 60% | F5: seven at least 60%, five strictly above | Explain threshold wording |
| Fusion superiority | p. 11 generalized highest-ASR wording | T2 has multiple contrary endpoints | Limit to supported tasks |
| Enron characterization | p. 10 real-world corpus | p. 14 synthetic-corpora example | Dataset provenance wording unresolved |
| Query length unit | T1 p. 6: NQ 9.2 words | p. 10: 9.2 tokens | Preserve source units |
| Mathematical notation | E2 self-reference; threshold/ties | Context suggests intended optimization | Flag rather than silently repair |

These inconsistencies do not erase the central pattern of vulnerability. They reduce confidence in exact aggregation, broad universal wording, and some formal details. Missing logs and proofs prevent adjudication beyond the supplied source.

## 15. Contributions and novelty

The **conceptual contribution** is treating retrieval as a separate bottleneck and distinguishing the trigger's ranking function from the attack fragment's behavioral function. This makes end-to-end evaluation more explicit. [A: pp. 2–3]

The **methodological/algorithmic contribution** is adapting CEM to black-box token-prefix search with a factorized distribution and fixed evaluation batches. The authors explicitly disclaim inventing CEM. The contribution is its application and adaptation to this IPI problem. [A: pp. 4–5, 13]

The **theoretical contribution** is the conditional utility theorem under an additive score assumption, plus an asserted NP-hardness result whose proof is outside the supplied version. Their validity cannot be independently established here. [A: pp. 4–5]

The **empirical contribution** combines eleven retrieval datasets, eight embedding models in the FiQA breadth test, multiple transfer dimensions, costs, RAG answer manipulation, and agent workflows with several harm objectives. These are complementary evaluations rather than a demonstrated exhaustive cross-product of all models and corpora. [A/B: pp. 5–12]

The **systems/security contribution** is showing how retrieval manipulation can lead to tool misuse and multi-agent code execution under natural email queries. The authors claim first end-to-end coverage of this kind; novelty relative to all prior literature is not independently verified in closed-document mode. [A: pp. 2, 9–12]

The **implementation contribution** is a reported release of attack and end-to-end evaluation scripts on Zenodo. No new dataset or benchmark is claimed in the supplied work, and the repository contents were not inspected. [A: p. 14]

## 16. Limitations

### Authors' stated limitations

The evaluation is restricted to embedding-based retrieval. Defense experiments address the retrieval stage. Hybrid pipelines and reranking are not evaluated and are explicitly future work. Cross-architecture transfer is not guaranteed. The core CEM algorithm is prior art. Payload construction is outside the central problem. Email is selected for in-depth agent analysis while other setups remain future directions. Fine-tuning defenses are excluded because the targeted proprietary models cannot be modified in the assumed setting. [A: pp. 3, 10, 13]

The authors also emphasize controlled scope: experiments are not attacks on deployed organizations or live infrastructure. They warn against reading the work as resolving the larger safety problems of LLM deployment. [A: p. 14]

### Additional evidence-based analyst observations

The known-query assumption is substantial: constructing a trigger for q does not demonstrate success against unknown future user queries. The single-user, ten-FAQ agent evaluation is a narrow sample for claims about broad populations or web tasks. Five repetitions produce descriptive variability but do not establish significance. Absent exact prompts, logs, model versions, selection rules, and proof details limit reproducibility from this version. [D: pp. 3, 10–12]

Several main claims use stronger language than detailed evidence supports. Table 3 is strong but nonperfect; F4 covers FiQA; F7 has major model exceptions; T2 demonstrates retrieval without compliance. The adapted multi-agent payload and changed architecture prevent attributing the whole difference solely to number of agents. Defense efficacy cannot be independently assessed without missing breakdowns and benign-utility measurements. [D: pp. 7–13, 19–20]

## 17. Threats to validity

The following are analyst classifications based on the supplied evidence, not section labels adopted by the authors.

**Internal validity.** Fixed corpora and attack fragments help isolate prefix differences within a given task. However, the multi-agent versus single-agent comparison changes workflow and adapts the attack fragment, so architecture, payload, and delegation effects are not separated. The suggested limited-context mechanism lacks a supplied ablation. [D: pp. 11–12]

**Construct validity.** Recall@5 measures malicious-item exposure, not malicious obedience or overall user harm. SIM measures vector alignment, not trustworthiness. The targeted answer 'Yes' is an answer-redirection endpoint; it is not a complete measurement of misinformation quality or denial of service. Phishing-link inclusion and worm propagation are properly distinguished in T2 and should remain distinct. [D: pp. 6, 9–11]

**External and ecological validity.** Diverse benchmark corpora improve domain breadth, but agent tests use a controlled email scenario rather than production web browsing. The attacker knows the query and embedding interface. Systems using hybrid retrieval, rerankers, different tool permissions, or different delegation policies may behave differently; those conditions are untested here. [D/A: pp. 3, 10, 13–14]

**Statistical conclusion validity.** Reported means and standard deviations characterize variation over limited repetitions. No significance tests or intervals are provided, and ± notation in T3 is less fully documented than T2. Prose/table aggregate conflicts weaken exact numerical conclusions. A zero displayed standard deviation does not prove zero uncertainty outside the evaluated sample. [D: pp. 11, 19–20]

**Reproducibility.** Default CEM parameters, datasets, frameworks, and hardware are supplied, but full payloads, agent logs, seed identifiers, model snapshots, and detailed defense settings are absent. Code is said to be available, but availability is an author report rather than a verified artifact in this analysis. [A/D: pp. 6, 10–14]

**Theoretical generalizability.** The theorem depends on an additive f. Real cosine scores of embedded concatenations are not shown to satisfy that exact assumption. The missing proof and notation ambiguities preclude asserting a general mathematical guarantee for modern retrievers. [D: pp. 4–5]

## 18. Future work and open questions

### A. Explicitly proposed by the authors

Evaluate hybrid retrieval and reranking; improve transfer across embedding architectures; investigate how much knowledge of the target embedding model is necessary; extend agent evaluation beyond the email setup; and develop defenses covering retrieval and system-level behavior. These directions are grounded in the limitations, transfer discussion, and conclusion. [A: pp. 8, 10, 13]

### B. Additional questions remaining from the evidence

For the user's research question, a matched study would need to compare the same base model under standalone, RAG, single-agent, and multi-agent conditions while specifying attack access and endpoints. How much additional risk arises from each stage? Can source provenance be retained through delegation? Do unknown or shifting user queries defeat query-specific triggers? How do benign retrieval quality and task success change under defenses? How sensitive are results to corpus ingestion, indexing, truncation, model updates, and agent permission policies? [D: pp. 3, 10–13]

These are open questions inferred from study boundaries, not results supplied by the paper. The present work provides mechanisms and selected measurements that motivate them, but does not answer them quantitatively.

## 19. Terminology and notation glossary

| Term / Symbol | Meaning in this paper |
|---|---|
| LLM | Large language model; generates responses or supports tool calls |
| IPI | Indirect prompt injection; instruction-bearing external content enters through retrieval |
| PI | Prompt injection; broader instruction-redirection category |
| RAG | Retrieval-Augmented Generation; retrieved content informs an LLM answer |
| Agentic system | LLM-based workflow involving planning, tools, or other agents |
| MAS | Multi-agent system; interacting specialized agents |
| CEM | Cross-Entropy Method; iterative sampling, elite selection, and distribution update |
| API | Application programming interface; black-box route to embedding outputs |
| MCP | Model Context Protocol; the interface used for the study's agent tools |
| BEIR | Named heterogeneous information-retrieval benchmark used in the paper; its acronym expansion is not supplied |
| FAISS | Named vector-database/library component; expansion is not supplied |
| FAQ | Frequently asked question; generated from the selected email history |
| DoS | Denial of service; discussed among possible downstream objectives |
| SSH keys | Sensitive key files targeted for exfiltration; the acronym is not expanded in the supplied paper |
| Corpus D | Collection of legitimate documents/items |
| D_adv | Attack fragment containing the attacker-specified behavioral objective |
| x | Trigger fragment selected to improve retrieval |
| ∥ | Concatenation of token sequences |
| q | Target user query |
| V, |V| | Token vocabulary and its size |
| Vⁿ | All length-n token sequences |
| n / n* | Prefix token budget / maximum embedding input length |
| E / d | Embedding model / vector dimensionality |
| sim | Cosine similarity between embeddings |
| f(x) | Similarity score of a candidate-trigger document against q |
| K | Number of retrieved items; usually 5 |
| B | Budget of black-box score accesses |
| N / T | Samples per iteration / iteration count |
| pᵢ(v) | Probability of token v at position i |
| λ | Elite fraction selected for distribution updates |
| α | Smoothing/update weight |
| ε | Allowed difference from optimal objective value |
| δ | Allowed failure probability in the conditional theorem |
| Recall@5 / R@5 | Fraction of queries exposing the single malicious item among five results |
| MRR@K | Mean Reciprocal Rank at K; averages inverse malicious-item rank, with cutoff |
| nDCG@K | Normalized Discounted Cumulative Gain at K; rewards earlier placement |
| ASR | Attack Success Rate; fraction achieving a specified downstream effect |
| SIM | Table 2's cosine-similarity field |
| Competition level | Similarity of the K-th-ranked clean document to q |
| Query+ / Vanilla | Query-prefix baseline / no-prefix baseline |
| Fusion / Ideal | Learned trigger plus query / assumed exposure of fragment alone |
| Black-box / white-box | API-output access / access to parameters or gradients |
| Perplexity filtering | Screening text by the language-model unusualness signal discussed in §6 |
| Token masking | Replacing selected tokens with a mask or removing their effect |

Undefined acronym expansions are deliberately not supplied from outside knowledge. Mathematical symbols whose intended meaning is inferable but whose printed expression is inconsistent are discussed in §13.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Retrieval datasets | 11 | datasets | BEIR test splits | Author-reported | pp. 5–6 |
| Target sample | 100 | queries per dataset | One injected item per evaluated target | Author-reported | p. 5 |
| Default prefix | 10 | tokens | CEM | Author-reported | p. 6 |
| Batch / iterations | 5,000 / 30 | candidates / iterations | Default CEM | Author-reported | p. 6 |
| Elite / smoothing | .2 / .55 | fractions | Default CEM | Author-reported | p. 6 |
| Candidate evaluations | 150,000 | score evaluations | 5,000×30 | Analyst-derived | pp. 6–7 |
| API cost | .21 | US dollars | Voyage or OpenAI, reported trigger generation | Author-reported | p. 8 |
| Higher API cost | .76 | US dollars | Qwen-v4, reported upper cost | Author-reported | p. 8 |
| Runtime | 1.6 / 2.3 / 7.6 | minutes | Contriever / GTE / Qwen3-0.6B, H100 | Author-reported | p. 8 |
| FiQA model breadth | 100 for seven; 90 for OpenAI | Recall@5 % | Independently targeted models | Visually readable | F4, p. 7 |
| OpenAI-reference mean | 73.75 | Recall@5 % | 590/8 across target cells; prose rounds to 74 | Analyst-derived | F5, p. 8 |
| Weak transfer example | 10 | Recall@5 % | Q3-0.6B reference to OpenAI target | Author-reported | p. 8 |
| Dispersion recalls | 90,22,68,91,80,88,6,86 | % | Eight models, ten dispersions | Visually readable | F7, p. 9 |
| Agent queries | 10 | FAQs | One user's Enron history | Author-reported | p. 10 |
| History criterion | ≥50 | sent/received emails | Selected user | Author-reported | p. 10 |
| Agent repetitions | 5 | seed repetitions | Mean and standard deviation | Author-reported | p. 11 |
| GPT-4o Fusion multi code | .80±.07 | ASR fraction | Multi-agent exfiltration endpoint | Visually readable | T2, p. 11 |
| GPT-4o Fusion single code | .02±.04 | ASR fraction | Single-agent code endpoint | Visually readable | T2, p. 11 |
| Fusion descriptive contrast | 78 | percentage points | (.80−.02)×100 | Analyst-derived | T2, p. 11 |
| Fusion descriptive ratio | 40 | ratio | .80/.02; differing workflows | Analyst-derived | T2, p. 11 |
| Mini CEM single code | .26±.09 | ASR fraction | Single-agent code endpoint | Visually readable | T2, p. 11 |
| GPT-4o Fusion tool misuse | .98±.04 | fraction | Both Sent and Phishing | Visually readable | T2, p. 11 |
| Recall average, n=3/5/10 | 28.4 / 63.0 / 94.1 | % | Table averages | Visually readable | T3, p. 20 |
| Conflicting prose averages | 29.5 / 95.6 | Recall % | n=3 / n=10 | Author-reported | p. 19 |
| MRR average, n=10 | .78 | reciprocal-rank mean | T3; prose says .79 | Visually readable | pp. 19–20 |
| NQ / FEVER, n=10 | 98.6±2.8 / 99.8±.4 | Recall % | Prose calls them 100% | Visually readable | T3, p. 20 |
| Knowledge poisoning | .58 / .50 | ASR fraction | Two / one trigger tokens, NQ, LLaMA-2-7B | Author-reported | p. 10 |

No exact values have been invented from unlabeled curves. The full condition and endpoint accompany each central result; rates are not silently converted between fractions and percentages.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Retrieval is an important attack prerequisite | Vanilla unretrieved; optimized prefixes exposed | F2, T3, X1 | pp. 6–7, 20 | HIGH within tested setups; not the only downstream failure condition |
| Compact black-box optimization is effective | CEM defaults and higher recall than baselines | ALG1, F2 | pp. 4–7 | HIGH for method description; performance nonuniform |
| Clean competition is associated with failures | Higher fifth-clean-item similarity for failures | F3, X2 | p. 7 | MEDIUM; descriptive association, not isolated causality |
| Larger/proprietary embedders remain attackable | FiQA recalls 90–100% | F4, X3 | p. 7 | HIGH for eight-model FiQA comparison |
| Transfer is conditional | Strong within-family and weak cross-family cells | F5, X6 | p. 8 | HIGH for matrix; broad generalization limited |
| Trigger scattering can retain effectiveness | Exact dispersion labels vary 6–91% | F7, X8 | p. 9 | HIGH; important OpenAI/Contriever exceptions |
| Retrieval does not ensure compliance | CEM targeted-answer R@5=1, ASR=.02 for GPT-4o | T2, X12 | p. 11 | HIGH counterexample to an unconditional guarantee |
| Tools support harms beyond wrong answers | Email misuse and code-exfiltration endpoints | T2, X13–X16 | pp. 10–12 | HIGH within controlled email setup |
| GPT-4o multi-agent workflow has higher code ASR | .72/.80 versus .04/.02 for CEM/Fusion | T2, X15–X16 | pp. 11–12 | HIGH descriptive evidence; MEDIUM causal interpretation |
| Three lightweight defenses lack adaptive durability | Qualitative §6 findings | X17–X19 | pp. 12–13 | MEDIUM; detailed appendix absent |
| Hybrid/reranking robustness is unknown | Explicit non-evaluation statement | §8 | p. 13 | HIGH as a scope boundary |
| Agent exposure helps explain the user's question | Retrieval, tools, delegation mechanisms | F1/T2, synthesis | pp. 3, 9–12 | MEDIUM analyst inference; no standalone or web-agent control |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant searching a large pile of emails to answer an ordinary question. Someone slips one malicious email into the pile. The email tells the assistant to do something else, but that instruction will not matter unless the assistant finds and reads it.

The researchers' main idea is to add a short piece of text that makes the search system rank the malicious email as relevant. That short piece is the trigger. The rest of the email contains the unwanted instruction. They use repeated trial-and-selection to find triggers that work well according to the search system's own numerical scores. In many of their tests, a single inserted document becomes one of the five results.

An assistant that can only answer questions might give a bad answer after reading the document. An assistant connected to email or code tools can cause different harms. In the paper's controlled multi-agent experiment, GPT-4o followed the code-execution attack much more often than in its single-agent experiment. The authors suggest that one agent may trust code sent by another without seeing where the request originally came from.

This helps explain why connecting a model to outside information and tools can create additional security problems. It does not prove that every web agent is less secure than every standalone model. The paper tests particular retrieval and email-agent systems, and some models, tasks, and conditions resist better than others. Its strongest lesson is to evaluate the whole path: what gets retrieved, what gets treated as an instruction, and what actions the system is allowed to take.

## Completeness Audit

Coverage is judged against the inventory of this supplied version, not by response length. 'Fully represented' means the substantive purpose, mechanism, evidence, and qualifications are covered; it does not mean every sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract | Yes, text and image | Yes | Represented in compressed form | Headline retrieval and agent claims qualified by detailed results |
| S1 Introduction and contributions | Yes | Yes | Fully represented | Gap, motivation, contribution categories |
| S2 Problem Formulation | Yes, text only on p. 3 | Yes | Fully represented | Corpus, embeddings, top-K system |
| S2.1 Threat Model | Yes, text only | Yes | Fully represented | One insertion, API access, known target, exclusions |
| S3.1 Similarity Search | Yes | Yes | Fully represented | Budgets, threshold, optimization, notation concerns |
| S3.2 CEM method | Yes | Yes | Fully represented | Distribution, elite selection, update |
| S4 Evaluation setup | Yes | Yes | Fully represented | Datasets, samples, models, defaults, framework |
| S4.1 Retrieval effectiveness | Yes | Yes | Fully represented | Baselines, competition, model breadth, runtime |
| S4.1 Multimodal extension | Prose only | Yes | Represented in compressed form | Detailed full-version experiment inaccessible |
| S4.2 Model transfer | Yes | Yes | Fully represented | Heatmap direction, strong/weak conditions |
| S4.2 Position transfer | Yes | Yes | Fully represented | OpenAI exception retained |
| S4.2 Dispersion | Yes | Yes | Fully represented | All labeled values and prose mismatch |
| S4.2 Fragment transfer | Yes | Yes | Fully represented | Similarity endpoint and absent sample details |
| S5 End-to-end framing | Yes | Yes | Fully represented | Retrieval versus execution distinction |
| S5.1 RAG | Yes | Yes | Fully represented | Endpoint, exclusions, seeds, heatmap discrepancies |
| S5.1 Knowledge poisoning | Prose only | Yes | Represented in compressed form | Exact reported numbers; absent full details |
| S5.2 Agent setup/objectives | Yes | Yes | Fully represented | Single/multi components and four objectives |
| S5.2 Agent baseline/metrics | Yes | Yes | Fully represented | Ideal, Query+, CEM, Fusion, distinct outcomes |
| S5.2 Retrieval/model effects | Yes | Yes | Fully represented | Query rewriting and task dependence |
| S5.2 Multi-agent amplification | Yes | Yes | Fully represented | Exact rates, tentative mechanism, confounding |
| S6 Paraphrasing | Main text only | Yes | Represented in compressed form | Full Appendix B.1 absent |
| S6 Perplexity filtering | Main text only | Yes | Represented in compressed form | F12 and full Appendix B.2 absent |
| S6 Token masking/scope | Main text only | Yes | Represented in compressed form | No supplied quantitative breakdown |
| S7 Related Work | Yes | Yes | Represented in compressed form | Three categories and orthogonal contextual defenses |
| S8 Limitations | Yes | Yes | Fully represented | All three explicit limitations plus scope restrictions |
| S9 Conclusion | Yes | Yes | Represented in compressed form | End-to-end evaluation and defense implications |
| ETH Stakeholders/principles | Yes | Yes | Represented in compressed form | Controlled scope and benefits; not every principle sentence repeated |
| ETH Potential harms/second-order effects | Yes | Yes | Represented in compressed form | Misuse and overinterpretation cautions |
| OPEN Code availability | Statement only | Yes | Fully represented | Repository not accessed |
| REF [1]–[104] | Yes, pp. 15–18 text only | Yes, as apparatus | Inspected but deliberately omitted as repetitive/non-substantive | Full bibliography not reproduced or externally verified |
| RQ1–RQ7 | Yes | Yes | Fully represented | Questions mapped to experiments; no invented formal hypotheses |
| Formal hypotheses | None identified | Yes, absence stated | Fully represented | No hypothesis-test framework supplied |
| X1–X21 | Yes where supplied | Yes | Represented in compressed form | Register covers each distinct analysis and endpoint |
| F1 | Yes, visually | Yes | Fully represented | Diagram interpreted separately |
| F2 | Yes, visually | Yes | Fully represented | Eleven panels; exact unlabeled points not transcribed |
| F3 | Yes, visually | Yes | Fully represented | Encoding, truncated axis, association caveat |
| F4 | Yes, visually | Yes | Fully represented | All eight exact labels |
| F5 | Yes, visually | Yes | Represented in compressed form | Direction, key cells, OpenAI column check; not all 64 cells reproduced |
| F6 | Yes, visually | Yes | Fully represented | Eight panels, position condition, exception |
| F7 | Yes, visually | Yes | Fully represented | All eight exact labels |
| F8 | Yes, visually | Yes | Fully represented | Axes, cluster trends, limits |
| F9 | Yes, visually | Yes | Represented in compressed form | Model rows/count issue and major patterns; not all 132 cells reproduced |
| F10 | Yes, visually | Yes | Fully represented | Four parameter panels; approximate trends only |
| T1 | Yes, visually | Yes | Fully represented | All dataset statistics transcribed |
| T2 | Yes, visually | Yes | Fully represented | All outcome means/SDs; retrieval/SIM compressed in prose |
| T3 | Yes, visually | Yes | Represented in compressed form | All Recall cells, n=10 rank metrics, averages; earlier rank cells compressed |
| E1–E7 | Yes, visually | Yes | Fully represented | Roles, symbols, constraints, ambiguities |
| Cosine/threshold/metric definitions | Yes | Yes | Fully represented | Cutoff and indexing issues flagged |
| ALG1 | Yes, visually | Yes | Fully represented | All substantive algorithm stages |
| TH1 | Statement/sketch only | Yes | Fully represented as supplied | Detailed proof absent |
| NP-hardness assertion | Statement only | Yes | Represented in compressed form | Formal result/proof absent |
| A.1 Different Metrics | Yes | Yes | Fully represented | Definitions, table, main-text conflicts |
| A.2 Hyperparameters | Yes | Yes | Fully represented | Defaults and sensitivity trends |
| A.2.1/A.3 full-version details | No | Absence represented | Missing from supplied material | Examples, FAQs, payloads, prompts, logs |
| Appendix B and F12 | No | Absence represented | Missing from supplied material | Defense evidence not independently inspectable |
| Appendix C | No | Absence represented | Missing from supplied material | Multimodal details |
| Supplied supplementary files | None | Absence represented | Missing from supplied material | No separate files or embedded artifacts provided |
| Administrative footnote/artifact badge | Yes | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | Corresponding-author marker and availability decoration |

### Missing or inaccessible material

The full technical report/arXiv version, formal NP-hardness proof, detailed Theorem 1 proof, full-version A.2.1 and A.3, defense Appendix B and F12, multimodal Appendix C, and Zenodo code were not supplied or accessed. Their absence prevents verification of exact payload construction, complete agent traces, defense thresholds, sample-level outputs, and theoretical derivations. Images for pp. 3 and 15–18 were not supplied, although their extracted text was available.

### Uncertain interpretations

Unresolved points include appendix prose/table numerical conflicts; the RAG model count and size labels; NQ word/token units; Enron real-world/synthetic wording; strict threshold wording in dispersion and transfer claims; the optimization argmax typo; ranking-threshold indexing and ties; elite-set tie handling; theorem assumptions and hidden constants; nDCG cutoff handling; and α = 1 in the parameter plot despite an earlier open-interval definition. Plot values without labels remain qualitative or approximate rather than exact.

### Deliberately compressed material

Repeated motivation, examples of prior work, the full bibliography, repeated ethical principle wording, individual coordinates in line plots, all nonessential cells of transfer and RAG heatmaps, and n = 3/5 MRR/nDCG cells were compressed. The central conditions, endpoint definitions, numerical outcomes, negative findings, and contradictory evidence were preserved. The malicious prompt is described rather than repeated in full because its instruction wording is secondary to understanding the retrieval mechanism.

### Potential omissions

No known major section, substantive subsection, supplied figure, supplied table, numbered equation, algorithm, explicit question, contribution category, or stated limitation is absent from this representation. Individual secondary numerical cells have been deliberately compressed as disclosed. Important referenced material remains inaccessible, so this analysis is comprehensive for the supplied version and cannot be called complete for the full research artifact. The user's standalone-LLM comparison remains an explicitly qualified research inference.
