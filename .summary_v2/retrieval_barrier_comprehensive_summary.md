# Stage 0 - Document Accessibility Report

| Accessibility item | Finding |
|---|---|
| Main document available | Yes: supplied page-labeled text covers pp. 1–20. |
| Pages apparently missing | No gaps in the supplied page sequence. However, the paper explicitly refers to a longer version containing material absent from these 20 pages. |
| Directly inspected page images | pp. 1, 2, 4–14, 19, and 20: 15 rendered pages. |
| Text-only pages | pp. 3 and 15–18. Their supplied text was inspected; their original visual layout was not. |
| Figures available | Figures 1–10 are visually available. Figure 1 includes embedded icons and a system diagram. |
| Tables available | Tables 1–3 are available as text and rendered images. Their values are readable, although Table 2 is compact. |
| Equations available | Equations (1)–(7), Algorithm 1, and Theorem 1 are visually available. The cosine-similarity definition on p. 3 is available in text only. Mathematical inconsistencies are identified below. |
| Appendices present | Appendix A begins on p. 19; §A.1 covers additional metrics and §A.2 covers hyperparameters. The mechanical record’s detection of p. 11 as an appendix page does not match the document headings. |
| Supplementary files supplied | None. The mechanical record reports no embedded files. |
| Referenced but absent material | Detailed proofs; the full-version NP-hardness statement and proof; Appendix A.2.1 examples and knowledge-poisoning results; Appendix A.3 queries, prompts, payloads, and logs; Appendix B defense results and ablations, including Figure 12; Appendix C multimodal experiments; the code repository and its evaluation scripts. |
| OCR needed | No additional OCR was needed. Supplied native text and page images were used together. |
| Other limitations | A failed attachment entry for `-` is reported, but the 15 listed page images are visible. It does not establish an additional missing paper page. Small plot points without numerical labels support trends and approximate estimates, not exact values. |

**Document identity.** *Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems*, by Hongyan Chang, Ergute Bao, Xinjian Luo, and Ting Yu, Mohamed bin Zayed University of Artificial Intelligence. Xinjian Luo is marked as corresponding author. The supplied first page displays a USENIX “Artifact Evaluated—Available” badge, and the ethics section mentions USENIX guidelines. An explicit publication venue, publication date, or proceedings citation for this paper is not supplied. (p. 1; p. 14.)

**Document type.** A cybersecurity and artificial-intelligence paper combining an algorithm, a conditional theoretical result, retrieval benchmarks, and experiments on retrieval-augmented generation and agentic systems.

**Source convention.**

- **[A] Author-reported:** stated in the supplied paper.
- **[B] Directly observable:** readable in a supplied figure or table.
- **[C] Analyst-derived:** calculated or reasoned directly from supplied information, with the derivation given.
- **[D] Analyst interpretation:** an explicitly identified interpretation.
- **[E] External information:** none used.

Unless otherwise labeled, descriptions below report the authors’ work. Numerical tables transcribe supplied evidence. Claims of novelty, practical significance, or generality remain the authors’ claims unless expressly evaluated as analyst observations.

# 1. Plain-Language Orientation

This paper studies a security problem in systems that search external information before answering a question or performing a task.

A user might ask an assistant to summarize relevant emails. The assistant searches an email collection, reads the retrieved messages, and then answers or uses tools. An attacker can place instructions inside an external message, hoping the assistant will follow them. This is **indirect prompt injection**: the instructions arrive through material the system reads rather than through the user’s direct request. (pp. 1–3.)

The paper focuses on an often-overlooked obstacle: **the malicious message must first be retrieved**. Instructions that would influence a model if placed directly in its context may never appear among the documents returned by a realistic search. The authors report that their unmodified attack text was never retrieved in the evaluated benchmark settings. (pp. 2, 6–7.)

Their solution separates the malicious document into:

1. an **attack fragment**, containing the unwanted instructions; and
2. a **trigger fragment**, a short token sequence optimized to make the whole document resemble the target query in the retriever’s numerical representation.

They adapt the **Cross-Entropy Method (CEM)**, an existing probabilistic optimization method, to find these trigger fragments using access to an embedding model’s outputs, without access to its internal parameters or the clean corpus. (pp. 3–5.)

The experiments show substantial retrieval vulnerability in the tested settings. Table 3 reports average malicious-document Recall@5 of **94.1% with a 10-token trigger**, although nearby appendix prose reports a conflicting **95.6%**. In a GPT-4o multi-agent email workflow, the combined “Fusion” variant achieves code-execution-and-exfiltration success of **0.80 ± 0.07**, compared with **0.02 ± 0.04** for that variant in the single-agent setting. These are controlled experiments, not attacks against live deployments. (pp. 11–14, 19–20.)

The central contribution is the treatment of retrieval as a distinct security stage and the demonstration that optimizing this stage can enable downstream attacks. However, **retrieval success is not the same as instruction execution**: several Table 2 conditions retrieve malicious content almost perfectly while producing little or no targeted-answer success.

# 2. Document Roadmap

The paper progresses from the retrieval problem, through its optimization method, to increasingly complex evaluations.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| S0 | Abstract | p. 1 | States the problem, method, headline results, and defense claims. |
| S1 | §1 Introduction | pp. 1–3 | Motivates the retrieval barrier, positions prior work, and lists contributions. |
| S2 | §2 Problem Formulation | p. 3 | Defines the corpus, embedding model, similarity ranking, and system pipeline. |
| S2.1 | §2.1 Threat Model | p. 3 | Specifies attacker access, one-item injection, the attack objective, and scope. |
| S3 | §3 Prefix Construction Attack | pp. 3–5 | Turns retrieval manipulation into prefix optimization. |
| S3.1 | §3.1 Similarity Search for Prefix | pp. 3–4 | Defines the objective, token budget, query budget, and optimization problem. |
| S3.2 | §3.2 Our Algorithm: CEM Attack | pp. 4–5 | Explains sampling, elite selection, distribution updates, and the conditional theorem. |
| S4 | §4 Evaluation on Trigger Fragment | pp. 5–9 | Introduces datasets, metrics, embedding models, baselines, and configuration. |
| S4.1 | §4.1 Effectiveness in Retrieval | pp. 6–8 | Tests length, corpus competition, model variation, cost, and multimodal extension. |
| S4.2 | §4.2 Transferability of Our Attack | pp. 8–9 | Tests transfer across models, positions, dispersed tokens, and attack fragments. |
| S5 | §5 End-to-end Evaluations | pp. 9–12 | Connects retrieval manipulation to downstream behavior. |
| S5.1 | §5.1 Case Study: RAG | pp. 9–10 | Tests fixed-answer generation and a knowledge-poisoning extension. |
| S5.2 | §5.2 Case Study: Agentic Systems | pp. 10–12 | Tests email agents, tool misuse, worm propagation, and code execution. |
| S6 | §6 Evaluation on Defense | pp. 12–13 | Discusses paraphrasing, perplexity filtering, and token masking. |
| S7 | §7 Related Work | p. 13 | Separates prior injection, RAG poisoning, retrieval optimization, and content defenses. |
| S8 | §8 Limitations | p. 13 | Restricts scope and transferability claims and acknowledges CEM’s prior origin. |
| S9 | §9 Conclusion | p. 13 | Calls for security evaluation and defenses spanning retrieval and downstream systems. |
| S10 | Ethical Considerations | p. 14 | Describes stakeholders, controlled scope, possible harms, and intended use. |
| S11 | Open Science | p. 14 | Reports code and evaluation scripts on Zenodo; the artifact itself is absent. |
| REF | References [1]–[104] | pp. 15–19 | Provides bibliographic context; cited works were not independently inspected. |
| A | Appendix A: Additional Experiments and Details | pp. 19–20 | Introduces the supplied additional material. |
| A.1 | Different Metrics | pp. 19–20 | Defines retrieval metrics and discusses Table 3. |
| A.2 | Impact of hyper-parameters in CEM | p. 20 | Discusses Figure 10. |

**Visual and mathematical inventory:** Figures F1–F10; Tables T1–T3; Algorithm ALG1; numbered equations E1–E7; the cosine-similarity definition; the unnumbered retrieval-threshold condition; Problem Definitions 1–2; Theorem 1; and the three appendix metric definitions.

**Other substantive objects:** Prompt 1 specifies the fixed-answer attack used in the main retrieval evaluation. The corresponding-author footnote is bibliographic. The artifact badge is metadata, not experimental evidence.

# 3. Background and Context

A **large language model (LLM)** generates responses from its input context. In this paper, the context can include documents returned from an external collection.

**Retrieval-augmented generation (RAG)** uses retrieved documents to support answer generation. An **agentic system** additionally plans tasks or invokes tools. The paper’s agents can retrieve emails, send emails, list contacts, and execute Python. A multi-agent system divides work among several interacting agents. (pp. 1, 9–10.)

An **embedding model** maps a token sequence into a numerical vector. The retriever compares the query vector with document vectors using **cosine similarity**, a score defined here in the range −1 to 1. It returns the **top-K** highest-ranked documents. Most experiments use \(K=5\). (pp. 3–4.)

A **token** is an element of the model’s vocabulary. The paper distinguishes trigger length in tokens from dataset query and document lengths, which Table 1 measures in words. These units should not be interchanged.

**Direct prompt injection** acts through the direct user–model interface. **Indirect prompt injection (IPI)** places instructions in an external source that the model later reads. The paper’s attack exploits two stages:

- **Retrieval:** make the malicious document enter the returned results.
- **Downstream behavior:** induce the model or agent to act on its instructions.

The authors’ main optimization targets the first stage. Their end-to-end experiments measure whether the second stage also succeeds. (pp. 3, 9, 11.)

**Black-box access** means the attacker can submit text to the embedding model and obtain vectors but cannot inspect model parameters or gradients. **White-box access** exposes internal information useful for optimization; attacks requiring it are excluded from the paper’s threat model. (p. 3.)

**Corpus competition** is the cosine similarity of the \(K\)-th highest-ranked clean document to the query. It expresses how high a malicious item’s score must be to compete with the retrieved clean documents, subject to the ranking-definition issues discussed in Section 13 below. (p. 7.)

# 4. Research Problem and Gap

| Element | Authors’ position | Source |
|---|---|---|
| Existing problem | External retrieved content can carry instructions that redirect an LLM’s answers or actions. | pp. 1–3 |
| Shortcoming of prior evaluations | Many ensure exposure by placing malicious material directly in context, forcing a tool to return it, selecting a “latest email,” constraining the corpus, or modifying the user query. | pp. 1–2, 13 |
| Consequence | Such experiments test behavior after exposure but do not establish that malicious text would be retrieved under ordinary queries and competing documents. | pp. 1–2 |
| White-box limitation | Gradient-based retrieval attacks require access inconsistent with proprietary embedding services. | pp. 2–4 |
| Black-box baseline limitation | Simply prepending the query can improve similarity but may not retrieve the malicious item reliably. | pp. 2, 6, 11 |
| Research gap | End-to-end evidence combining realistic retrieval competition with downstream injection effects across RAG and agents. | pp. 2–3, 9 |
| Motivation | Retrieval may be the missing stage that determines whether otherwise effective injected instructions can reach a deployed-style pipeline. | pp. 1–3 |
| Scope | Embedding-based retrieval, one malicious insertion per target query, black-box embedding access, and controlled evaluations. | pp. 3, 13–14 |

These are the authors’ characterizations of prior work. The supplied references permit tracing their citations, but do not independently establish that this is the first such study or that all earlier approaches share the described limitations.

# 5. Research Questions / Objectives / Hypotheses

The paper does not present a numbered hypothesis list or formal statistical hypothesis tests. It poses several explicit questions and states corresponding objectives.

| ID | Question or objective | Status in paper | Evidence addressing it |
|---|---|---|---|
| RQ1 | Under realistic corpora and natural queries, will malicious text be retrieved? | Explicit central question, p. 2 | Vanilla and optimized-prefix results, Figure 2 and Table 3. |
| RQ2 | Can retrieval be guaranteed? | Explicit question, p. 2 | Formalization, Algorithm 1, conditional theorem, and retrieval experiments. |
| RQ3 | What makes retrieval vulnerable? | Explicit question, p. 6 | Corpus-competition analysis, Figure 3. |
| RQ4 | Are stronger embedding models safer? | Explicit question, p. 7 | Eight-model FiQA evaluation, Figure 4. |
| RQ5 | Does effectiveness persist when the model, placement, or attack fragment changes? | Explicit questions across §4.2 | Figures 5–8. |
| RQ6 | Does retrieving the malicious document change downstream system behavior? | Explicit uncertainty motivating §5 | Figure 9 and Table 2. |
| RQ7 | Can potential countermeasures neutralize the attack? | Explicit question, p. 12 | Three defense discussions; detailed results absent. |
| O1 | Construct a compact trigger through limited black-box access. | Methodological objective | Equations (1)–(7), Algorithm 1, runtime and cost reports. |
| O2 | Evaluate across retrieval datasets, embedding models, and downstream attack families. | Experimental objective | §§4–5. |
| O3 | Examine adaptive attacks against existing defenses. | Stated contribution | §6; absent full-version Appendix B. |

**Informal conjecture:** attack difficulty depends primarily on query–corpus similarity rather than corpus size or document length. Figure 3 provides an observational comparison supporting this conjecture; it is not a controlled causal test. (pp. 6–7.)

# 6. Assumptions / Threat Model

## System and attacker assumptions

| Component | Supplied specification |
|---|---|
| External corpus | \(\mathcal D=\{D_1,\ldots,D_m\}\), with each item a token sequence. |
| Retriever | A predefined embedding model \(E\), cosine similarity, and top-\(K\) selection. |
| Input limit | \(E\) supports sequences up to some \(n^*\); Contriever is given as an example supporting 512 tokens. |
| Target query | The optimization is formulated for a given natural query \(q\). |
| Attacker write access | Can inject exactly one malicious item into the corpus for the target query. |
| Corpus knowledge | Cannot inspect the clean corpus contents. |
| Model knowledge | Cannot access retriever or LLM parameters. |
| Available access | Can query the embedding model through an application programming interface (API) and obtain vectors. |
| Attack fragment | Supplied to the optimization; its creation is not the main research contribution. |
| Attacker-controlled modification | A short trigger \(x\), initially prepended to the attack fragment. |
| Resource restrictions | Finite trigger-token budget \(n\) and scoring-query budget \(B\). |
| Downstream goals | Targeted answers, phishing/self-replication, tool misuse, and code execution with exfiltration. |

Source: p. 3, §§2–2.1; pp. 4–5.

The attacked trust boundary lies between **external information** and **instructions governing the model or its tools**. Figure 1 shows an external item entering retrieval results and influencing subsequent actions.

**[D] Important interpretation:** “black-box” does not mean the attacker lacks all useful knowledge. The formal problem assumes a target query is available and that an embedding model can be queried. Section 4.2 separately examines imperfect knowledge of the deployed embedding model. The paper does not demonstrate a universal trigger that succeeds for every unknown future query.

Theoretical assumptions are stronger than the deployment assumptions. Theorem 1 requires the score to decompose additively across token positions. The authors motivate this through pooling behavior, but do not establish exact additivity for the evaluated models. (p. 5.)

The study excludes hybrid retrieval, reranking, and defenses requiring model fine-tuning. Its ethics statement explicitly limits the experiments to controlled settings. (pp. 13–14.)

# 7. Methodology

## 7.1 Overall design

The study has four connected layers:

1. **Formalization:** express malicious-document retrieval as similarity optimization.
2. **Algorithm:** adapt CEM to discrete trigger-token sequences.
3. **Retrieval experiments:** test whether optimized documents enter top-5 results.
4. **End-to-end and defense experiments:** measure downstream behavior and resilience to selected countermeasures.

The study does not train a new retriever or base LLM.

## 7.2 CEM prefix optimization

The score for a candidate trigger is

\[
f(x)=\operatorname{sim}\big(E(q),E(x\parallel D_{\mathrm{adv}})\big).
\]

The attack fragment stays fixed while the trigger changes.

The algorithm maintains a probability distribution over possible tokens at each trigger position. Initially, each position has a uniform distribution. It repeatedly:

1. samples a batch of candidate triggers;
2. evaluates each candidate’s similarity score;
3. selects high-scoring candidates;
4. increases the probability of tokens that appear in those selected candidates;
5. returns the best sequence found.

A factorized distribution allows storage as an \(n\times|\mathcal V|\) matrix rather than a separate probability for every full sequence. The rationale is to search a large discrete space while using a bounded number of black-box evaluations. (pp. 4–5.)

This is an adaptation of an existing method. The authors explicitly disclaim invention of CEM itself. (p. 13.)

## 7.3 Retrieval datasets

The authors report using test splits from 11 BEIR datasets, subsampling **100 target queries per dataset**, and generating one malicious item for each query’s evaluation. The document labels identify which clean items are relevant to particular queries. (pp. 5–6.)

Table 1 is reproduced in Section 11. The reported corpora span passage retrieval, biomedical retrieval, question answering, argument retrieval, entity retrieval, citation prediction, and fact checking.

The supplied paper does not specify the query-subsampling seed, whether the same selected queries are reused across every experiment, or the detailed preprocessing and truncation procedure.

## 7.4 Embedding models

| Model label | Reported model | Parameters | Output dimensions |
|---|---|---:|---:|
| GTE | `gte-modernbert-base` | 139M | 768 |
| Contriever | `contriever-msmarco` | 110M | 768 |
| Q3-0.6B | Qwen3-Embedding-0.6B | 0.6B | 1,024 |
| Q3-4B | Qwen3-Embedding-4B | 4B | 2,560 |
| Q3-8B | Qwen3-Embedding-8B | 8B | 4,096 |
| OpenAI | `text-embedding-3-small` | Not specified | Not specified |
| Voyage | `voyage-3.5-lite` | Not specified | Not specified |
| Qwen-v4 | Alibaba Cloud `text-embedding-v4` | Not specified | Not specified |

GTE is the default. The eight-model direct and transfer comparisons are reported on FiQA. Thus, “11 datasets and 8 models” should not be read as evidence that every dataset–model combination was tested. (pp. 6–8.)

## 7.5 Baselines

| Method | Construction or evaluation condition |
|---|---|
| Vanilla | Attack fragment alone, without a trigger. |
| Query+ | Original user query prepended to the attack fragment; called “repeat query” in the paper. |
| CEM | Learned trigger prepended to the same attack fragment. |
| Fusion | Learned trigger, then original user query, then attack fragment. |
| Ideal | Attack fragment assumed to be in context, bypassing the retrieval obstacle. |

The retrieval comparisons keep the attack fragment fixed and vary the prefix. White-box attacks are excluded because they violate the specified access model. Claims that Query+ resembles a white-box baseline’s performance are attributed to cited work rather than newly tested here. (pp. 6, 11.)

The exact implementation of Query+ across all prefix lengths in Figure 2 is not described sufficiently to reconstruct its repetition or truncation schedule.

## 7.6 Configuration and resources

| Parameter | Default |
|---|---:|
| Retrieved documents \(K\) | 5 |
| Trigger length \(n\) | 10 tokens |
| Samples per iteration \(N\) | 5,000 |
| Iterations \(T\) | 30 |
| Elite fraction \(\lambda\) | 0.2 |
| Smoothing \(\alpha\) | 0.55 |
| Scoring accesses | At most 150,000 |
| Hardware | Server with an H100 GPU |
| Retrieval implementation | BEIR framework and FAISS vector database |

Sources: pp. 4–8.

**[C] Budget check:** \(5{,}000\times30=150{,}000\) candidate-score evaluations. The paper reports this same maximum. It does not fully itemize any additional embedding calls, batching behavior, or caching.

## 7.7 Metrics and statistics

- **Recall@5:** whether the one malicious item enters the five returned items, averaged across queries. This is an attacker-oriented retrieval metric, not clean-task answer quality.
- **Mean Reciprocal Rank at K (MRR@K):** averages a score of \(1/r\) when the malicious item is at rank \(r\le K\), otherwise zero.
- **Normalized Discounted Cumulative Gain at K (nDCG@K):** rewards higher placement using the supplied single-item discount formula; its cutoff notation is incomplete.
- **SIM:** cosine similarity between the query and malicious text.
- **RAG attack success rate (ASR):** fraction of eligible queries changed to the target response by poisoning. Queries already producing that response in the clean system are excluded.
- **Agent ASR:** fraction of queries producing the specified downstream effect.

RAG results are averaged over **five random seeds**. Agent experiments are repeated **five times**, and Table 2 reports **mean ± standard deviation**. Table 3 displays uncertainty terms, but its exact run count and error-summary definition are not clearly specified in the supplied appendix. No confidence intervals or significance tests are reported. (pp. 10–11, 19–20.)

## 7.8 Agent setup

The email experiments use an Enron mailbox described as having at least **50 sent and received emails**. Claude Sonnet 4 generates **10 frequently asked questions** from that history. Each query receives a separate single malicious insertion. The exact mailbox size and questions are absent. (p. 10.)

The single-agent system uses AutoGen with retrieval, email sending, contact-list access, and Python execution, implemented through the **Model Context Protocol (MCP)**. The multi-agent system uses Magentic-One within AutoGen, with an orchestrator, FileSurfer, Coder, Computer Terminal, and an added retriever agent. GPT-4o and GPT-4o-mini are evaluated. (p. 10.)

# 8. Experiments / Analyses

| ID | Experiment | Design and purpose | Evidence, result, and caveat |
|---|---|---|---|
| X1 | Trigger length and retrieval | Compare CEM, Query+, and Vanilla across 11 corpora; vary prefix length; measure Recall@5. | Figure 2; Table 3. CEM generally improves with length and outperforms the baselines. Table 3 reports 94.1% average at 10 tokens, with lower results on MS MARCO and ArguAna. |
| X2 | Corpus competition | Group successful and failed queries by similarity of their fifth-ranked clean document. | Figure 3. Failure groups often have higher competition. This is an association, not an isolated manipulation of corpus density. |
| X3 | Embedding-model variation | Evaluate eight embedding models on FiQA. | Figure 4: seven models show 100% Recall@5; OpenAI shows 90%. This is a FiQA comparison, not the full dataset–model grid. |
| X4 | Cost and runtime | Report API cost and local runtime for trigger generation. | pp. 7–8: $0.21 for Voyage/OpenAI, up to $0.76 for Qwen-v4; 1.6–7.6 minutes for selected local models. Timing distributions and cost accounting are absent. |
| X5 | Image-to-text extension | Use MS COCO and OpenCLIP embeddings. | p. 8 reports near-perfect recall with few tokens. Detailed setup and results are in absent Appendix C. |
| X6 | Cross-model transfer | Optimize on one embedding model and evaluate on another using FiQA. | Figure 5 shows substantial asymmetry. Same-family transfer is often high; some cross-family cells are low or zero. Prose misidentifies one cell. |
| X7 | Position transfer | Optimize at position 0, move the contiguous trigger elsewhere. | Figure 6. Most models retain considerable recall; OpenAI falls toward zero around position 20. Direct optimization at the end reportedly restores 60%, but that result is not separately plotted here. |
| X8 | Token dispersion | Randomly scatter trigger tokens through the attack text; average over 10 dispersions. | Figure 7. Recall ranges from 6% to 91%, depending on model. This qualifies claims of position independence. |
| X9 | Attack-fragment transfer | Reuse a trigger optimized on one attack fragment with other randomly sampled fragments of varying lengths. | Figure 8 shows similarity increases. Sample count and length distribution are absent; similarity improvement is not itself an end-to-end ASR measurement. |
| X10 | RAG fixed-answer attack | Insert one malicious document and measure changed output to “Yes”; exclude clean “Yes” cases. | Figure 9, five seeds. Broad susceptibility, but considerable variation and model-count inconsistencies. |
| X11 | Knowledge poisoning | NQ, LLaMA-2-7B, one malicious document; compare short triggers with query prepending. | p. 10 reports ASR 0.58 with two tokens and 0.50 with one, versus 0.58 for the query baseline. Detailed results absent. |
| X12 | Single-agent answer manipulation | Compare Ideal, Query+, CEM, Fusion for GPT-4o and GPT-4o-mini. | Table 2. High retrieval does not ensure target-answer success: CEM ASR is 0.02 and 0.00, respectively. |
| X13 | Single-agent phishing worm | Separately measure phishing-link inclusion and replication-instruction propagation. | Table 2. GPT-4o Fusion yields 0.84 phishing and 0.18 worm; GPT-4o-mini yields 0.74 and 0.64. |
| X14 | Single-agent tool misuse | Measure broadcasting to contacts and phishing-link inclusion. | Table 2. GPT-4o results are generally high; GPT-4o-mini Fusion improves over its other tested variants. |
| X15 | Single-agent code execution | Measure execution and data exfiltration. | Table 2. GPT-4o remains at 0.02–0.04; GPT-4o-mini CEM reaches 0.26. |
| X16 | Multi-agent code execution | Adapt the attack fragment to the multi-agent setup and compare methods. | Table 2. GPT-4o CEM/Fusion reach 0.72/0.80; GPT-4o-mini reaches 0.42/0.36. Payload adaptation complicates causal attribution to orchestration alone. |
| X17 | Query paraphrasing defense | Alter query wording; test adaptive optimization over multiple paraphrases. | §6 reports a drop below 10% on most datasets before adaptation, followed by recovery. Exact per-dataset results absent. |
| X18 | Perplexity filtering defense | Examine whether unnatural text can be detected; test repetition as adaptation. | §6 reports reduced perplexity while maintaining effectiveness. Figure 12 and thresholds are absent. |
| X19 | Token masking defense | Randomly mask token positions. | §6 reports weak protection, especially for longer triggers. Masking rates and detailed results absent. |
| X20 | Additional retrieval metrics | Vary \(n=3,5,10\); report Recall@5, MRR@5, nDCG@5. | Table 3. Metrics improve in every displayed dataset; appendix prose conflicts with several table values. |
| X21 | Hyperparameter sensitivity | On MS MARCO with \(n=10\), vary \(T,N,\lambda,\alpha\). | Figure 10. More search generally improves similarity; smaller elite fractions are favorable; smoothing has modest effects. No numerical data table or error bars is supplied. |

# 9. Results

The strongest supported findings are conditional on the tested systems and should be separated from the paper’s broader language.

| Finding | Evidence | Qualification |
|---|---|---|
| Prefix optimization substantially improves malicious-document retrieval. | Figure 2; Table 3 average Recall@5: 28.4%, 63.0%, 94.1% for 3, 5, 10 tokens. | These are Table 3 values; nearby prose reports different averages. |
| A short trigger can suffice, but not uniformly. | At 10 tokens: NFCorpus, HotpotQA, DBPedia, SCIDOCS, SciFact reach 100.0%; MS MARCO reaches 74.0%; ArguAna 77.5%. | “Guarantees retrieval” is stronger than the finite empirical results. |
| Different embedding models remain vulnerable when directly optimized. | Figure 4: 100% on seven FiQA model conditions and 90% on OpenAI. | Does not establish universal vulnerability across all retrieval systems or workloads. |
| Transfer depends on the source and target model. | Figure 5 contains values from 0% to 100%. | Direct optimization and cross-model transfer are different conditions. |
| Placement robustness varies sharply. | Figure 7: GTE 90%, Contriever 22%, OpenAI 6%. | Robustness observed in some models cannot be generalized to every embedding architecture. |
| Retrieval and downstream execution can diverge. | GPT-4o CEM targeted answer: R@5 1.00, ASR 0.02 ± 0.04. | Retrieval success alone is insufficient evidence of behavioral compromise. |
| Multi-agent GPT-4o code-execution risk is high in the tested setup. | Fusion: 0.80 ± 0.07; CEM: 0.72 ± 0.16. | One email setting, 10 generated questions, five repetitions, and adapted multi-agent payloads. |
| Fusion does not dominate every condition. | GPT-4o-mini multi-agent ASR: Query+ 0.56, CEM 0.42, Fusion 0.36. | The prose’s broad “highest success” description needs task- and model-specific qualification. |
| The evaluated retrieval defenses are reported to be bypassable. | §6 qualitative summaries. | Detailed experiments, parameters, and uncertainty estimates are not supplied. |

**[C] Derived retrieval improvement:** Table 3’s reported averages increase from 28.4% at three tokens to 94.1% at ten tokens: \(94.1-28.4=65.7\) **percentage points**. This is not a 65.7% relative increase.

**[C] Derived multi-agent comparison:** for GPT-4o Fusion, \(0.80-0.02=0.78\), a **78-percentage-point** difference between the reported multi-agent and single-agent means. Their ratio is \(0.80/0.02=40\). This descriptive ratio does not isolate the effect of adding agents because the attack fragment is adapted for the multi-agent setting. (pp. 11–12.)

# 10. Figure-by-Figure Interpretation

## Figure 1 — Retrieval-to-action attack pipeline

**Location:** p. 2.

This diagram connects three stages:

1. the user submits a query;
2. an embedding-based retriever selects external documents;
3. agents and a base LLM generate an answer or take an action.

The attacker supplies an attack fragment and uses the proposed algorithm to generate a trigger. Their concatenation enters the corpus as one malicious item. An embedding-space inset distinguishes query, clean-document, attack-fragment, and combined-malicious-text vectors.

The geometry illustrates the intended change: the attack fragment alone is poorly aligned with the query, while the combined item is moved closer to it. The diagram then shows potential downstream categories: incorrect answers or denial of service, spam, and code execution.

**Caveat:** this is a conceptual diagram, not a measured embedding visualization. The distances and positions are illustrative.

## Figure 2 — Retrieval success versus trigger length

**Location:** p. 7; discussion pp. 6–7.

- **Panels:** MS MARCO, NFCorpus, Natural Questions, ArguAna, SciFact, HotpotQA, TREC-COVID, FiQA, DBPedia, SciDocs, FEVER.
- **Horizontal axis:** trigger length, labeled at 1, 5, 10, 15, 20; linear scale.
- **Vertical axis:** Recall@5 (%), ticks from 0 to 100; linear scale.
- **Encoding:** pink/red circles for CEM; blue squares for Query+; green dashed line for Vanilla.
- **Uncertainty:** no visible error bars.

**[B] Observations:** CEM generally rises faster than Query+ and often reaches a high plateau with fewer tokens. Vanilla remains at the bottom throughout. MS MARCO and ArguAna are harder than several other datasets.

The authors report that approximately 15 tokens often yield above 80% and sometimes 90% recall on the harder corpora, while Query+ remains around 20% on ArguAna. These are prose descriptions, not exact labeled plot values. (p. 6.)

**Caveat:** numerical plot estimates should not replace the differently summarized Table 3 results. The figure does not identify the exact Query+ construction at every tested length.

## Figure 3 — Corpus competition and attack outcome

**Location:** p. 7.

- **Plot:** grouped bars, one group per dataset.
- **Horizontal axis:** dataset.
- **Vertical axis:** competition level, shown roughly from 0.6 to 0.9.
- **Encoding:** light blue for CEM success, pink for CEM failure.
- **Definition:** average cosine similarity of the fifth-ranked clean document, calculated separately for successful and unsuccessful queries.
- **Missing bars:** indicate no failed group where all attacks succeed, according to the caption.
- **Uncertainty:** no error bars or group sample counts.

The authors highlight NFCorpus at approximately 0.64 with no failures and MS MARCO at approximately 0.75 for successful attacks versus 0.82 for failed attacks. (p. 7.)

**[D] Interpretation:** stronger clean-document competition is associated with failure. Because the outcome groups are formed after observing success, this does not by itself establish that corpus competition is the sole or primary causal factor.

## Figure 4 — Direct optimization across embedding models

**Location:** p. 7.

- **Plot:** bars for eight models on FiQA.
- **Vertical axis:** Recall@5 (%), linear 0–100.
- **Exact labels:** GTE 100; Contriever 100; Q3-0.6B 100; Q3-4B 100; Q3-8B 100; Voyage 100; OpenAI 90; Qwen-v4 100.
- **Uncertainty:** no error bars.

This supports vulnerability across the tested model architectures and access types. It does not demonstrate that model size never affects security or that every embedding-based system behaves similarly.

## Figure 5 — Cross-model transfer matrix

**Location:** p. 8.

- **Horizontal axis:** reference model used to optimize the trigger.
- **Vertical axis:** target model used for retrieval.
- **Cells:** Recall@5 (%), explicitly labeled.
- **Color scale:** white to dark blue, 0–100.
- **Dataset:** FiQA.

The following transcription reorders rows from GTE through Qwen-v4 for readability while preserving the axis meaning.

| Target \ Reference | GTE | Contriever | Q3-0.6B | Q3-4B | Q3-8B | Voyage | OpenAI | Qwen-v4 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GTE | 100 | 40 | 40 | 40 | 40 | 60 | 60 | 40 |
| Contriever | 40 | 100 | 30 | 30 | 40 | 40 | 20 | 40 |
| Q3-0.6B | 90 | 90 | 100 | 90 | 90 | 90 | 100 | 90 |
| Q3-4B | 90 | 90 | 90 | 100 | 90 | 70 | 90 | 90 |
| Q3-8B | 80 | 70 | 80 | 100 | 100 | 70 | 80 | 90 |
| Voyage | 60 | 40 | 40 | 30 | 60 | 100 | 60 | 60 |
| OpenAI | 20 | 0 | 30 | 30 | 10 | 30 | 90 | 20 |
| Qwen-v4 | 70 | 60 | 100 | 90 | 90 | 70 | 90 | 100 |

**[B] Findings:** transfer is asymmetric. OpenAI-target retrieval is especially low for several foreign reference models. Qwen-family targets frequently retain high recall.

**Cross-check discrepancies:**

- The text says Q3-0.6B → OpenAI yields 10%; the matrix shows **30%**. The **10%** cell is Q3-8B → OpenAI.
- The text says OpenAI-generated triggers exceed 60% on seven models. The column shows seven models at **60% or higher**, with two exactly 60%.
- **[C] Recalculation:** OpenAI’s reference column sums to \(60+20+100+90+80+60+90+90=590\); \(590/8=73.75\%\), consistent with the rounded reported average of 74%.

No error bars or condition-specific sample counts accompany this matrix.

## Figure 6 — Moving a trigger away from its optimized position

**Location:** p. 9; interpretation p. 8.

- **Panels:** eight embedding models.
- **Horizontal axis:** token position, labeled at 0, 20, 40, 60.
- **Vertical axis:** Recall@5 (%), linear 0–100.
- **Condition:** trigger optimized at position 0, then inserted elsewhere.
- **Encoding:** blue line; no uncertainty bands.

Most panels retain substantial success across positions. OpenAI declines sharply and approaches zero near position 20. Some other models show meaningful fluctuations rather than flat position independence.

The p. 8 text separately reports that optimizing directly at the end achieves 60% Recall@5 on OpenAI. That is not a curve shown in this figure.

**Caveat:** the curves demonstrate positional behavior, not direct measurements of internal positional encoding. The authors’ explanation in terms of how models encode position is an interpretation.

## Figure 7 — Random dispersion of trigger tokens

**Location:** p. 9.

- **Plot:** eight bars.
- **Horizontal axis:** model.
- **Vertical axis:** Recall@5 (%), linear 0–100.
- **Condition:** tokens from a prefix optimized at position 0 are scattered through the text.
- **Aggregation:** average of 10 random dispersions.
- **Uncertainty:** no error bars.

| Model | Exact displayed Recall@5 |
|---|---:|
| GTE | 90% |
| Contriever | 22% |
| Q3-0.6B | 68% |
| Q3-4B | 91% |
| Q3-8B | 80% |
| Voyage | 88% |
| OpenAI | 6% |
| Qwen-v4 | 86% |

The figure supports strong dispersion tolerance for several models, with clear exceptions. The prose says GTE is “above 90%” and Q3-8B “exceed[s] 80%”; the labels show exactly 90% and 80%.

## Figure 8 — Reusing a trigger with other attack fragments

**Location:** p. 9.

- **Plot:** scatterplot.
- **Horizontal axis:** query similarity of the attack fragment alone, with ticks from −0.2 to 0.8.
- **Vertical axis:** query similarity after adding a trigger optimized on another attack fragment, with ticks around 0.75–0.90.
- **Encoding:** blue points are random fragments; pink is the originally targeted fragment.
- **Scales:** linear, with a restricted vertical range.
- **Uncertainty:** no error bars.

**[B] Observation:** many low-similarity fragments cluster near approximately 0.76 after trigger addition; fragments with higher original similarity often appear higher, approaching approximately 0.89.

The text’s example of moving from around −0.1 to 0.76 describes a portion of the plot, not its maximum vertical value.

**Caveats:** exact point coordinates, fragment counts, lengths, and sampling rules are not supplied. The plot measures similarity, not Recall@5 or successful execution of each alternate attack fragment.

## Figure 9 — Fixed-answer attack across RAG models and datasets

**Location:** p. 10.

- **Plot:** heatmap.
- **Horizontal axis:** 11 datasets.
- **Vertical axis:** model labels.
- **Metric:** attack success rate, linear color scale 0–1.
- **Condition:** a single malicious document attempts to induce “Yes.”
- **Averaging:** five random seeds, according to the setup.
- **Uncertainty:** no error terms in the figure.

The visual contains **12 model rows**, despite the caption and prose saying 11 LLMs.

| Model as labeled | MS MARCO | COVID | NFCorpus | NQ | HotpotQA | FiQA | ArguAna | DBPedia | SciDocs | FEVER | SciFact |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen3-0.6B | .8 | .8 | 1 | 1 | .8 | .8 | .7 | 1 | .9 | .6 | .7 |
| Qwen3-1.7B | .6 | .7 | .9 | .8 | .8 | .6 | .7 | 1 | .9 | .4 | .6 |
| Qwen3-4B | .8 | .6 | 1 | .9 | .6 | .7 | .7 | 1 | 1 | .5 | .5 |
| Qwen3-8B | .7 | .7 | .9 | .7 | .6 | .7 | .7 | 1 | 1 | .1 | .5 |
| Qwen3-11B | .7 | .7 | .9 | .8 | .6 | .8 | .8 | .9 | 1 | .6 | .5 |
| Qwen3-32B | .7 | .7 | .9 | .7 | .7 | .7 | .7 | 1 | .9 | .4 | .5 |
| Llama3-3B | .2 | .1 | .3 | .2 | .5 | .3 | .3 | .7 | .3 | .6 | .4 |
| Llama3-3B-Ins | .3 | .5 | .7 | .3 | .1 | .4 | .7 | 1 | .9 | .4 | .5 |
| Llama3-8B | .5 | .3 | .5 | .5 | .3 | .6 | .6 | .7 | .6 | .8 | .8 |
| Llama3-8B-Ins | .3 | .8 | .7 | .6 | .5 | .7 | .7 | 1 | .9 | .6 | .8 |
| Vicuna-7B | .4 | .6 | .4 | .4 | .1 | .4 | .5 | .8 | .8 | .4 | .8 |
| Vicuna-13B | .6 | .6 | .6 | .8 | .7 | .6 | .7 | 1 | .8 | .4 | .5 |

**[B] Observations:** DBPedia has high displayed success across all rows. The Qwen rows are frequently high, but include lower conditions such as 0.1 for Qwen3-8B on FEVER. Instruction tuning and model size do not improve or worsen every cell uniformly.

**Caveats:** the setup describes Qwen3 as “0.8B–32B,” while the visual begins at 0.6B. The unusual “Qwen3-11B” label is reproduced as printed and cannot be independently resolved from the supplied material. Retained sample counts after excluding clean “Yes” outputs are absent.

## Figure 10 — Sensitivity to CEM hyperparameters

**Location:** p. 20, §A.2.

Four line plots vary:

1. iterations \(T\), with labeled ticks 20, 60, 100;
2. batch size \(N\), with labeled ticks 2k, 6k, 10k;
3. elite fraction \(\lambda\), labeled 0.1, 0.3, 0.5;
4. smoothing \(\alpha\), labeled 0.5, 0.8, 1.

The vertical axis is similarity, approximately 0.70–0.90. The dataset is MS MARCO and trigger length is fixed at 10.

**[B] Observations:** similarity rises quickly and then fluctuates as \(T\) increases; rises with \(N\); generally falls as \(\lambda\) increases; and changes modestly with \(\alpha\).

**Caveats:** exact point values, error bars, and repeated-run details are absent. The prose’s “consistently enhances” wording is best interpreted as an overall tendency, because the iteration curve is not strictly monotonic.

# 11. Table-by-Table Interpretation

## Table 1 — Dataset characteristics

**Location:** p. 6.

The table describes corpus sizes and average lengths. “M” means millions of documents; both length columns are in **words**.

| Task | Dataset | Documents, millions | Mean query words | Mean document words |
|---|---|---:|---:|---:|
| Passage retrieval | MSMARCO | 8.8 | 6.0 | 56.0 |
| Biomedical retrieval | TREC-COVID | 0.171 | 10.6 | 160.8 |
| Biomedical retrieval | NFCorpus | 0.036 | 3.3 | 232.3 |
| Question answering | Natural Questions | 2.7 | 9.2 | 78.9 |
| Question answering | HotpotQA | 5.2 | 17.6 | 46.3 |
| Question answering | FiQA-2018 | 0.058 | 10.8 | 132.3 |
| Argument retrieval | ArguAna | 0.087 | 193.0 | 166.8 |
| Entity retrieval | DBPedia | 4.6 | 5.4 | 49.7 |
| Citation prediction | SCIDOCS | 0.026 | 9.4 | 176.2 |
| Fact checking | FEVER | 5.4 | 8.1 | 84.8 |
| Fact checking | SciFact | 0.052 | 12.4 | 213.6 |

**Interpretation:** the datasets differ substantially in corpus size and query length. ArguAna’s mean query is especially long; NFCorpus has the shortest mean query and longest mean document.

**Caveats and checks:**

- The table reports characteristics, not experiment-specific retained sample counts.
- The prose gives a document-length range of 56–232, but the table includes 46.3 for HotpotQA and 49.7 for DBPedia.
- The MS MARCO row cites [46], while reference [46] is titled *Natural Questions*. This is an internal citation mismatch, not an externally verified correction.

## Table 2 — Agent retrieval and downstream effects

**Location:** p. 11; explanations pp. 10–12.

All displayed success values are fractions. Multiplication by 100 converts them to percentages. ASR terms are **mean ± standard deviation** across five repetitions. R@5 and SIM have no displayed uncertainty. A dash means the quantity is not reported or not applicable to the Ideal condition, not zero.

### Targeted-answer task

| Model | Method | R@5 | SIM | ASR |
|---|---|---:|---:|---:|
| GPT-4o | Ideal | — | — | .04 ± .05 |
| GPT-4o | Query+ | 1 | .76 | .14 ± .05 |
| GPT-4o | CEM | 1 | .85 | .02 ± .04 |
| GPT-4o | Fusion | 1 | .88 | .16 ± .11 |
| GPT-4o-mini | Ideal | — | — | .00 ± .00 |
| GPT-4o-mini | Query+ | 1 | .76 | .00 ± .00 |
| GPT-4o-mini | CEM | .98 | .85 | .00 ± .00 |
| GPT-4o-mini | Fusion | 1 | .89 | .04 ± .05 |

Fusion has the highest mean in each model group, but targeted-answer success remains low despite near-perfect retrieval.

### Phishing-worm task

| Model | Method | R@5 | SIM | Phishing | Worm |
|---|---|---:|---:|---:|---:|
| GPT-4o | Ideal | — | — | .77 ± .11 | .01 ± .03 |
| GPT-4o | Query+ | .56 | .70 | .38 ± .14 | .08 ± .06 |
| GPT-4o | CEM | 1 | .77 | .66 ± .17 | .00 ± .00 |
| GPT-4o | Fusion | 1 | .81 | .84 ± .11 | .18 ± .13 |
| GPT-4o-mini | Ideal | — | — | .87 ± .08 | .83 ± .13 |
| GPT-4o-mini | Query+ | .63 | .70 | .51 ± .11 | .46 ± .10 |
| GPT-4o-mini | CEM | 1 | .77 | .64 ± .17 | .46 ± .11 |
| GPT-4o-mini | Fusion | 1 | .81 | .74 ± .09 | .64 ± .11 |

“Phishing” and “Worm” are separate outcomes. A phishing link being sent does not imply the replication instructions were also propagated.

Fusion is strongest among the three retrieval-based variants here. However, the GPT-4o-mini Ideal condition has higher means than Fusion for both outcomes. GPT-4o CEM improves retrieval and phishing over Query+ but has lower worm success.

### Tool-misuse task

| Model | Method | R@5 | SIM | Sent to contacts | Phishing |
|---|---|---:|---:|---:|---:|
| GPT-4o | Ideal | — | — | 1 ± .00 | 1 ± .00 |
| GPT-4o | Query+ | 1 | .78 | .99 ± .04 | .99 ± .04 |
| GPT-4o | CEM | 1 | .83 | .92 ± .08 | .92 ± .08 |
| GPT-4o | Fusion | .98 | .87 | .98 ± .04 | .98 ± .04 |
| GPT-4o-mini | Ideal | — | — | .47 ± .19 | .44 ± .18 |
| GPT-4o-mini | Query+ | 1 | .78 | .64 ± .13 | .63 ± .13 |
| GPT-4o-mini | CEM | 1 | .83 | .58 ± .18 | .58 ± .18 |
| GPT-4o-mini | Fusion | 1 | .87 | .84 ± .05 | .84 ± .05 |

For GPT-4o, the Ideal and Query+ means exceed the optimized variants. For GPT-4o-mini, Fusion has the highest means. Thus, increased similarity is not accompanied by a uniform increase in tool-misuse success.

### Code execution and exfiltration

| Model | Setting | Method | R@5 | SIM | ASR |
|---|---|---|---:|---:|---:|
| GPT-4o | Single agent | Ideal | — | — | .02 ± .04 |
| GPT-4o | Single agent | Query+ | 1 | .73 | .02 ± .04 |
| GPT-4o | Single agent | CEM | 1 | .79 | .04 ± .05 |
| GPT-4o | Single agent | Fusion | 1 | .85 | .02 ± .04 |
| GPT-4o | Multi-agent | Ideal | — | — | .58 ± .18 |
| GPT-4o | Multi-agent | Query+ | 1 | .76 | .56 ± .05 |
| GPT-4o | Multi-agent | CEM | 1 | .78 | .72 ± .16 |
| GPT-4o | Multi-agent | Fusion | 1 | .85 | .80 ± .07 |
| GPT-4o-mini | Single agent | Ideal | — | — | .04 ± .05 |
| GPT-4o-mini | Single agent | Query+ | 1 | .73 | .18 ± .08 |
| GPT-4o-mini | Single agent | CEM | 1 | .79 | .26 ± .09 |
| GPT-4o-mini | Single agent | Fusion | 1 | .85 | .22 ± .04 |
| GPT-4o-mini | Multi-agent | Ideal | — | — | .54 ± .23 |
| GPT-4o-mini | Multi-agent | Query+ | 1 | .75 | .56 ± .21 |
| GPT-4o-mini | Multi-agent | CEM | 1 | .78 | .42 ± .08 |
| GPT-4o-mini | Multi-agent | Fusion | 1 | .83 | .36 ± .09 |

The standout result is GPT-4o Fusion in the multi-agent setup. The reverse ranking for GPT-4o-mini is equally important: Query+ has a higher mean than CEM or Fusion in its multi-agent condition.

**Statistical caveat:** the table supplies standard deviations, not significance tests. Ranking means does not establish that each difference is statistically reliable.

## Table 3 — Prefix length and three retrieval metrics

**Location:** p. 20, §A.1 discussion on p. 19.

The table compares \(n=3,5,10\) tokens across the same 11 datasets. Higher values indicate stronger attacker retrieval performance.

### Recall@5, in percent

| Dataset | \(n=3\) | \(n=5\) | \(n=10\) |
|---|---:|---:|---:|
| MSMARCO | 7.9 ± 3.8 | 35.3 ± 3.4 | 74.0 ± 13.6 |
| TREC-COVID | 0.4 ± 0.8 | 7.6 ± 3.2 | 87.6 ± 11.8 |
| NFCorpus | 94.0 ± 3.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| NQ | 7.0 ± 1.1 | 48.8 ± 3.1 | 98.6 ± 2.8 |
| HotpotQA | 11.4 ± 2.2 | 80.4 ± 2.4 | 100.0 ± 0.0 |
| FiQA-2018 | 31.6 ± 3.4 | 73.4 ± 2.4 | 97.8 ± 3.9 |
| ArguAna | 1.8 ± 0.7 | 16.6 ± 0.8 | 77.5 ± 8.0 |
| DBPedia | 45.8 ± 8.3 | 91.4 ± 5.9 | 100.0 ± 0.0 |
| SCIDOCS | 24.0 ± 3.0 | 78.2 ± 2.5 | 100.0 ± 0.0 |
| FEVER | 10.2 ± 1.6 | 62.4 ± 4.2 | 99.8 ± 0.4 |
| SciFact | 77.8 ± 3.0 | 98.6 ± 0.8 | 100.0 ± 0.0 |
| **Reported average** | **28.4** | **63.0** | **94.1** |

### MRR@5

| Dataset | \(n=3\) | \(n=5\) | \(n=10\) |
|---|---:|---:|---:|
| MSMARCO | .04 ± .02 | .22 ± .04 | .55 ± .10 |
| TREC-COVID | .00 ± .00 | .03 ± .01 | .69 ± .12 |
| NFCorpus | .71 ± .06 | .93 ± .01 | .97 ± .02 |
| NQ | .03 ± .01 | .31 ± .02 | .83 ± .03 |
| HotpotQA | .05 ± .01 | .45 ± .03 | .90 ± .04 |
| FiQA-2018 | .17 ± .02 | .53 ± .02 | .87 ± .01 |
| ArguAna | .01 ± .00 | .06 ± .01 | .40 ± .03 |
| DBPedia | .33 ± .03 | .79 ± .06 | .97 ± .03 |
| SCIDOCS | .12 ± .02 | .55 ± .02 | .88 ± .02 |
| FEVER | .04 ± .01 | .28 ± .02 | .63 ± .03 |
| SciFact | .43 ± .02 | .75 ± .05 | .92 ± .01 |
| **Reported average** | **.18** | **.45** | **.78** |

### nDCG@5

| Dataset | \(n=3\) | \(n=5\) | \(n=10\) |
|---|---:|---:|---:|
| MSMARCO | .05 ± .02 | .26 ± .04 | .60 ± .10 |
| TREC-COVID | .00 ± .00 | .04 ± .02 | .74 ± .12 |
| NFCorpus | .77 ± .04 | .95 ± .01 | .98 ± .02 |
| NQ | .04 ± .01 | .35 ± .02 | .87 ± .02 |
| HotpotQA | .06 ± .01 | .54 ± .02 | .93 ± .03 |
| FiQA-2018 | .20 ± .02 | .58 ± .02 | .90 ± .02 |
| ArguAna | .01 ± .00 | .09 ± .01 | .49 ± .04 |
| DBPedia | .37 ± .04 | .82 ± .06 | .98 ± .02 |
| SCIDOCS | .15 ± .02 | .61 ± .02 | .91 ± .02 |
| FEVER | .06 ± .01 | .36 ± .03 | .72 ± .02 |
| SciFact | .52 ± .02 | .81 ± .04 | .94 ± .01 |
| **Reported average** | **.20** | **.49** | **.82** |

**Interpretation:** all displayed dataset means improve or remain at their maximum as trigger length increases. At ten tokens, NFCorpus and DBPedia tie for the highest MRR and nDCG, while ArguAna has the lowest values for those rank-sensitive metrics. MS MARCO has the lowest Recall@5.

A document can be retrieved almost every time without usually ranking first. FEVER illustrates this: Recall@5 is 99.8%, but MRR@5 is 0.63.

**Uncertainty caveat:** the appendix mentions variation across seeds, but does not clearly define every displayed ± term or give the number of repetitions. It calls a ± range “variance,” although no variance calculation is supplied.

**Direct contradictions with p. 19 prose:**

| Quantity | Appendix prose | Table 3 |
|---|---:|---:|
| Average Recall@5, \(n=3\) | 29.5% | 28.4% |
| Average Recall@5, \(n=10\) | 95.6% | 94.1% |
| Average MRR@5, \(n=10\) | .79 | .78 |
| NQ Recall@5, \(n=10\) | 100% | 98.6 ± 2.8% |
| FEVER Recall@5, \(n=10\) | 100% | 99.8 ± 0.4% |

**[C] Check from displayed rows:** the ten-token recall means sum to 1,035.3; \(1{,}035.3/11\approx94.118\%\), matching the table’s rounded 94.1%. This confirms the table’s internal arithmetic, but does not establish why the prose differs.

# 12. Diagram / Architecture Interpretation

Figure 1 is the only substantive architecture diagram. It combines two interacting paths.

**Normal information path:** user query → embedding model → similarity search over corpus vectors → retrieved documents → LLM/agents → answer or action.

**Attacker path:** chosen attack fragment + target query/model access → trigger-construction algorithm → combined malicious item → corpus insertion → possible retrieval → possible downstream instruction following.

The trigger changes the **retrieval representation** of the item, while the attack fragment changes what the model is asked to do after reading it. The diagram’s embedding inset makes this separation visible.

The agent architecture described in §5.2 adds further control flow:

- An orchestrator delegates work.
- A retriever agent searches emails and can access email/contact tools.
- FileSurfer handles files.
- Coder produces code.
- Computer Terminal executes code.

The authors suggest that an execution agent may receive code from a teammate without seeing the original malicious source or user request. They offer this as a possible explanation for multi-agent amplification. It is not established through a dedicated information-flow ablation in the supplied material. (pp. 10, 12.)

# 13. Equations and Mathematical Concepts

## 13.1 Core notation

| Symbol | Meaning in the paper |
|---|---|
| \(\mathcal D\) | Clean external corpus. |
| \(D_i\) | A corpus item. |
| \(m\) | Number of corpus items. |
| \(\mathcal V\) | Token vocabulary. |
| \(n^*\) | Maximum supported input length for the embedding model. |
| \(d\) | Embedding dimension. |
| \(E\) | Embedding model. |
| \(q\) | Target user query. |
| \(D_{\mathrm{adv}}\) | Attack fragment. |
| \(x\) | Trigger fragment. |
| \(\parallel\) | Sequence concatenation. |
| \(K\) | Number of retrieved items. |
| \(n\) | Trigger length or token budget. |
| \(B\) | Black-box scoring-query budget. |
| \(\varepsilon\) | Allowed suboptimality in similarity. |
| \(\delta\) | Failure-probability parameter in Theorem 1. |
| \(N,T\) | Batch size and number of iterations. |
| \(\lambda,\alpha\) | Elite fraction and smoothing weight. |

## 13.2 Cosine similarity

**Location:** p. 3, §3.1.

\[
\operatorname{sim}(u,v)=
\frac{u^\top v}{\|u\|_2\|v\|_2},
\qquad u,v\in\mathbb R^d.
\]

This scalar score compares the directions of two vectors. The numerator is their dot product; the denominator uses their Euclidean lengths.

**Inputs:** query and document embeddings.  
**Output:** similarity used to rank documents.  
**Role:** supplies the optimization objective.

**[C] Mathematical boundary:** the displayed formula requires nonzero vector norms. The paper does not discuss zero-vector handling.

## 13.3 Equation (1): trigger score

**Location:** p. 4.

\[
f(x)=\operatorname{sim}\big(E(q),E(x\parallel D_{\mathrm{adv}})\big).
\]

This function scores a trigger by the similarity of the **entire combined malicious item**, not the trigger alone, to the query.

For fixed \(q\), \(D_{\mathrm{adv}}\), and \(E\), the variable is \(x\). A higher value is intended to improve retrieval ranking.

## 13.4 Problem Definition 1: overall attack objective

**Location:** p. 3, §2.1.

The attacker seeks an \(x\) such that \(x\parallel D_{\mathrm{adv}}\) ranks in the top-\(K\) of the augmented corpus.

The definition then says this ensures execution. **[D] Qualification:** that implication is too strong as a general statement. Section 5 explicitly separates retrieval from downstream behavior, and Table 2 supplies counterexamples to equating them.

## 13.5 Unnumbered retrieval-threshold condition

**Location:** p. 4.

The paper writes:

\[
f(x)>
\min\left\{
\tau:
\left|\left\{
D\in\mathcal D:
\operatorname{sim}(E(D),E(q))>\tau
\right\}\right|
\le K
\right\}.
\]

The intended meaning is that the malicious item must exceed the clean-document competition threshold.

**[C] Indexing problem:** this formula does not generally express the stated top-\(K\) condition.

For an illustrative clean corpus with scores 0.9 and 0.8 and \(K=1\), the displayed minimum is 0.8: only one clean score exceeds 0.8. A malicious score of 0.85 satisfies the formula, yet ranks second and is not top-1. The paper’s next sentence instead says the \(K=1\) threshold is the maximum clean score, which is 0.9 in this illustration.

For distinct scores, the intended strict comparison is against the \(K\)-th highest clean score. Equivalently, a successfully retrieved malicious item can have at most \(K-1\) clean items strictly above it. Tie handling needs a separate rule, which is not supplied.

## 13.6 Equation (2): approximately optimal prefix

**Location:** p. 4.

The paper seeks \(x\in\mathcal V^n\) with

\[
f(x)>f(x^*)-\varepsilon.
\]

The displayed definition of \(x^*\) is

\[
x^*:=\arg\max_{x\in\mathcal V^n}f(x^*).
\]

**Notation issue:** the maximand is printed as \(f(x^*)\), which does not vary with the optimization variable \(x\). The surrounding prose indicates the intended expression is likely

\[
x^*\in\arg\max_{x\in\mathcal V^n}f(x),
\]

but this is an **analyst interpretation of an apparent typo**, not a silent correction.

The objective seeks a prefix whose score is within \(\varepsilon\) of the best feasible score. It does not itself guarantee that the best feasible score exceeds the unknown corpus threshold.

**[C] Feasible-set qualification:** the authors say increasing \(n\) expands the solution space and improves the optimum. For exact-length sets \(\mathcal V^n\), the shorter set is not literally contained in the longer one. Monotonicity would require an at-most-length formulation or an extension that preserves scores, neither of which is specified. The empirical results nevertheless support an overall benefit from longer triggers.

## 13.7 Equation (3): factorized distribution

**Location:** p. 4.

\[
p(x)=\prod_{i=1}^{n}p_i(x[i]).
\]

Here \(p_i(v)\) is the probability of token \(v\) at position \(i\). Multiplication forms a joint sequence probability under independent position sampling.

**Purpose:** reduce representation from \(|\mathcal V|^n\) sequence probabilities to \(n|\mathcal V|\) token-position probabilities.

**Limitation:** the sampling model does not explicitly represent dependencies between token positions. This is a modeling choice, distinct from proving the true score is additive.

## 13.8 Equation (4): iteration-specific sampling

**Location:** p. 5.

\[
p^{(t)}(x_j)=\prod_{i=1}^{n}p_i^{(t)}(x_j[i]).
\]

At iteration \(t\), candidate \(j\) is sampled from the current distribution. The algorithm generates \(N\) independent candidates and evaluates their scores.

The stated budget constraint is \(NT\le B\).

## 13.9 Equation (5): elite selection

**Location:** p. 5.

\[
S=
\left\{
x_j:
\left|
\left\{
x_k:k\ne j,\ f(x_k)\ge f(x_j)
\right\}
\right|
\le\lambda N
\right\}.
\]

This is intended to identify the highest-scoring \(\lambda\) fraction of candidates.

**[C] Boundary issue:** with distinct scores and integer \(\lambda N\), the candidate ranked \(\lambda N+1\) has exactly \(\lambda N\) candidates above it and also satisfies the displayed condition. The formula can therefore select one more candidate than the pseudocode’s “\(\lambda N\) highest-scoring samples.” Ties introduce further ambiguity. Rounding and tie rules are not supplied.

## 13.10 Equations (6) and (7): probability update

**Location:** p. 5.

\[
p_i^{(t+1)}(v)=(1-\alpha)p_i(v)+\alpha\widehat p_i(v),
\tag{6}
\]

\[
\widehat p_i(v)=
\frac{
\sum_{j=1}^{N}
\mathbf 1\{v=x_j[i]\land x_j\in S\}
}{
|S|
}.
\tag{7}
\]

Equation (7) counts how often token \(v\) appears at position \(i\) among selected candidates, then divides by the number selected. The indicator \(\mathbf 1\) equals one when its condition is true and zero otherwise.

Equation (6) blends that empirical frequency with the prior distribution. The paper constrains \(\alpha\in(0,1)\).

**Notation caveat:** \(p_i(v)\) on the right side omits the iteration superscript. Context suggests \(p_i^{(t)}(v)\), but the printed expression is incomplete.

## 13.11 Algorithm 1

**Location:** p. 5.

The pseudocode takes the attack fragment, embedding model, target query, token length, batch size, elite fraction, smoothing, and iteration count. It initializes distributions, constructs \(f\), loops through sampling/scoring/selection/update, and outputs the best sequence.

The initialization writes \(p_i^{(t)}\) rather than a clearly designated initial iteration. The prose clarifies uniform initialization. Exact tie-breaking and whether “best” refers to all sampled candidates or only the final batch are not fully specified.

## 13.12 Theorem 1: conditional utility guarantee

**Location:** p. 5.

Assume

\[
f(x_1,\ldots,x_n)=\sum_{i=1}^{n}f_i(x_i).
\]

The authors state that with

\[
T=O(\log|\mathcal V|),\qquad
N=O\!\left(\log\frac1\delta\right),
\]

the algorithm returns an \(x\) satisfying

\[
f(x)\ge f(x^*)-\varepsilon
\]

with probability at least \(1-\delta\).

The proof sketch says elite selection repeatedly amplifies probabilities of good tokens from an initial \(1/|\mathcal V|\).

The claimed scoring cost is

\[
O\!\left(\log|\mathcal V|\log\frac1\delta\right),
\]

compared with \(n|\mathcal V|\) greedy evaluations and \(O(|\mathcal V|^n)\) brute-force sampling.

**Limits of verification:**

- The detailed proof is absent.
- Dependence hidden in the big-\(O\) notation on \(n,\varepsilon,\lambda,\alpha\), and score separation is unspecified.
- Exact additive structure is not demonstrated for the evaluated embedding scores.
- Approximate similarity optimality does not imply retrieval against every unknown corpus.
- The theorem uses a non-strict \(\ge\), while Equation (2) uses \(>\).
- The separate NP-hardness claim is also deferred to absent material.

Thus, the supplied theorem can be accurately reported, but its correctness and applicability cannot be fully verified here.

## 13.13 Appendix metric equations

**Location:** p. 19, §A.1.

\[
\operatorname{Recall@K}
=
\frac{\text{number of relevant items in top-}K}
{\text{number of all relevant items}}.
\]

The authors designate the single malicious item as the relevant item for this attack metric, reducing each query’s value to zero or one.

\[
\operatorname{RR@K}=
\begin{cases}
1/r,&r\le K,\\
0,&r>K.
\end{cases}
\]

MRR is the mean of these reciprocal ranks across queries. High values indicate early ranking.

The supplied single-item nDCG expression is

\[
\operatorname{nDCG@K}=\frac1{\log_2(i+1)}.
\]

The rank is \(i\), and rank one gives one.

**Notation limitation:** the printed nDCG expression does not state its value when the malicious item lies outside top-\(K\), although the metric is labeled “@K.” The intended cutoff treatment cannot be confirmed from this equation alone.

# 14. Interpretation and Discussion

The paper demonstrates why retrieval and downstream model behavior should be evaluated together. A malicious item can fail because it is never seen, or it can be seen without producing the attacker’s desired action. The experiments measure both cases.

For RQ1–RQ2, the evidence supports **high retrieval rates after optimization in the tested settings**, not an unconditional guarantee. The mathematical guarantee is conditional, and Table 3 includes failures.

For RQ3, corpus competition is a useful descriptive quantity associated with attack outcome. The claim that it “governs” difficulty is stronger than the observational design alone establishes.

For RQ4–RQ5, the results show broad vulnerability under direct optimization and uneven transfer. Model choice changes transfer and placement behavior even where direct optimization succeeds.

For RQ6, the downstream findings are task-dependent. The multi-agent GPT-4o result is substantial, but it coexists with low targeted-answer ASR and weak single-agent code-execution results. The study therefore supports evaluating entire workflows rather than inferring system safety from a single model response or retrieval score.

For RQ7, the authors report adaptive bypasses of three retrieval defenses. The missing detailed appendix limits independent assessment of their strength, utility tradeoffs, and experimental coverage.

## Consistency register

| Issue | Conflicting or incomplete evidence | Assessment |
|---|---|---|
| Headline exfiltration rate | Abstract: “over 80%”; introduction: “up to 80%”; Table 2 maximum displayed mean: .80. | The supplied table supports 80% mean, not a mean exceeding 80%. |
| Retrieval averages | p. 19: 29.5%, 95.6%, MRR .79; Table 3: 28.4%, 94.1%, .78. | Unresolved text–table discrepancies. |
| Perfect-recall datasets | p. 19 includes NQ and FEVER at 100%; Table 3 gives 98.6% and 99.8%. | Report both; do not silently round to perfect. |
| Transfer cell | p. 8 assigns 10% to Q3-0.6B → OpenAI; Figure 5 shows 30%. | The 10% cell belongs to Q3-8B → OpenAI. |
| Transfer threshold wording | p. 8 says seven models above 60%; two relevant cells are exactly 60%. | “At least 60%” matches the figure. |
| Dispersion wording | p. 8 says GTE above 90% and Q3-8B above 80%; Figure 7 labels 90 and 80. | Minor text–figure overstatements. |
| RAG model count | Caption/setup: 11 LLMs; Figure 9: 12 rows. | Exact evaluated inventory is unresolved. |
| RAG model size | Setup: Qwen3 0.8B–32B; figure starts 0.6B and includes 11B. | Preserve printed labels; no external correction. |
| Dataset length range | p. 6 says document lengths 56–232; Table 1 includes 46.3 and 49.7. | Prose range excludes displayed rows. |
| Query length unit | Table 1: NQ 9.2 words; p. 10: 9.2 tokens. | Unit discrepancy affects the short-trigger comparison. |
| Enron characterization | §5.2 calls it real-world; ethics section calls Enron a synthetic-corpus example. | Whether and how the mailbox was transformed is unclear. |
| Extra-metric pointer | p. 6 points to Appendix A.2; metrics are in supplied A.1. | Internal cross-reference mismatch. |
| Missing appendix references | Proofs, A.2.1, A.3, B, C, and Figure 12 are cited but absent. | Cannot verify those materials. |
| Mathematical definitions | Retrieval threshold, argmax, elite selection, update notation, cutoff handling. | Detailed in Section 13; cannot be silently repaired. |
| Fusion superiority | Broad prose claim; Table 2 contains multiple conditions where Fusion is not best. | Must qualify by task and model. |
| Causal explanation | Orchestration, positional encoding, and similarity are invoked to explain outcomes. | Plausible author interpretations; dedicated causal tests are absent. |

# 15. Contributions and Novelty

| Contribution type | What the paper contributes | Qualification |
|---|---|---|
| Conceptual | Separates the retrieval-attracting trigger from the instruction-bearing attack fragment. | A useful formal decomposition; it does not make downstream execution automatic. |
| Methodological | Treats successful retrieval as an explicit requirement in end-to-end IPI evaluation. | The authors’ “first” claim is not externally verified. |
| Algorithmic | Adapts CEM to short discrete prefixes under black-box embedding access. | CEM itself is prior art, explicitly acknowledged in §8. |
| Theoretical | States an approximate-optimization guarantee under additive scores and a query-complexity comparison. | Proof absent; assumptions are not established for actual embedding scores. |
| Empirical | Tests retrieval across 11 datasets and model variation across eight embeddings, plus transfer and sensitivity. | Not evidence of a complete 11-by-8 experiment grid. |
| Systems/security | Demonstrates downstream effects in RAG, single-agent, and multi-agent workflows. | Agent evidence comes from a limited email setting. |
| Defense evaluation | Examines adaptive behavior against three retrieval-stage defenses. | Detailed results absent. |
| Implementation/open science | Reports an available algorithm and evaluation-script repository. | Repository contents were not supplied or inspected. |

The paper does not introduce a new dataset or claim a newly invented family of instruction payloads. Its emphasis is making existing kinds of malicious instructions retrievable. (pp. 2–3, 13–14.)

# 16. Limitations

## Authors’ stated limitations

1. **Embedding-based retrieval only.** Hybrid retrieval and reranking are not evaluated. (p. 13, §8.)
2. **Defense scope is limited to retrieval.** The work does not evaluate all system-level protections. (p. 13.)
3. **Cross-model transfer is not guaranteed.** Architecture differences can substantially reduce success. (pp. 8, 13.)
4. **CEM is not original to this work.** The contribution is its adaptation. (p. 13.)
5. **Agent scenarios are limited to email.** Other agent settings are deferred. (p. 10.)
6. **Fine-tuning-based defenses are excluded.** The stated setting assumes proprietary models whose parameters cannot be modified. (p. 13.)
7. **Controlled benchmarks do not represent attacks on deployed systems.** The ethics statement explicitly distinguishes the study from live targeting. (p. 14.)
8. **Detailed material is omitted because of page limits.** The supplied appendix points to a fuller technical report. (p. 19.)
9. **The study addresses one security risk, not overall LLM safety.** The ethics statement cautions against treating it as resolving broader harms. (p. 14.)

## Additional evidence-based analyst observations

The following are **[D] analyst observations**, not author admissions.

- The optimization is target-query-specific; effectiveness against unknown future queries is not established.
- The main agent evaluation uses only ten generated questions from one described mailbox.
- The exact email corpus size, preprocessing, prompts, model configurations, and complete logs are absent.
- Table 2 demonstrates that retrieval is not sufficient for downstream compromise.
- Similarity gains do not uniformly translate to higher ASR.
- Theorem 1’s proof and applicability to nonlinear embedding scores remain unverified.
- Several numerical and mathematical inconsistencies materially limit precision.
- Defensive utility costs—such as the effect of masking on legitimate retrieval—are not quantified here.
- The “stealth” benefit of short triggers is not evaluated through human detection, automated detection, or realistic ingestion controls.
- Large clean corpora do not by themselves establish broad generalization when only 100 queries per corpus are sampled.
- Reported uncertainty is incomplete for several experiments, and no statistical significance testing is supplied.

# 17. Threats to Validity

These labels are **analyst classifications** of the supplied design.

| Validity dimension | Evidence-based concern |
|---|---|
| Internal validity | Within a task, keeping the attack fragment and clean corpus fixed helps isolate prefix changes. However, the multi-agent attack fragment is adapted, so the large single-to-multi-agent difference does not isolate orchestration alone. |
| Construct validity | Recall@5 measures malicious-item exposure, not clean retrieval utility or behavioral compromise. Figure 8 measures similarity, not actual retrieval or ASR. Worm and phishing outcomes must remain separate. |
| Statistical conclusion validity | Five agent repetitions and ten questions provide a limited basis for precise generalization. Standard deviations are supplied, but no confidence intervals, tests, or paired comparisons. Table 3’s uncertainty definition is unclear. |
| External validity | Evaluations omit hybrid search, reranking, other agent domains, and varied production ingestion environments. Cross-model transfer varies. |
| Ecological validity | Queries are described as natural, but the email questions are model-generated and the environment is controlled. The title’s “in the wild” must be read alongside the explicit statement that no live deployments were attacked. |
| Reproducibility | Defaults, model names, frameworks, and hardware are reported. Exact versions, all prompts, seed values, detailed mailbox preparation, proofs, and code are absent from the supplied material. |
| Generalizability | Eight embedding models on FiQA do not establish identical behavior across all models and datasets. One-item-per-query optimization does not establish universal attack success across queries. |
| Interpretation validity | Associations with corpus competition and explanations involving position encoding or agent trust are not separately established as causal mechanisms. |

No claim in this table requires outside evidence; each follows from the paper’s stated design and missing details.

# 18. Future Work and Open Questions

## A. Explicitly proposed or identified by the authors

- Evaluate hybrid retrieval and reranking. (p. 13.)
- Improve transfer between different embedding architectures. (pp. 8, 13.)
- Investigate the attacker’s need for knowledge or a good guess of the target embedding model. (p. 8.)
- Extend agent evaluations beyond email. (p. 10.)
- Develop defenses addressing both retrieval and downstream system behavior. (p. 13.)
- Consider potential misuse of embedding optimization in search or recommendation systems; this is raised as an ethical consideration, not a completed experiment. (p. 14.)

## B. Additional questions remaining from the supplied evidence

These are **[D] analyst questions**.

- How effective is the method when the attacker cannot predict the user query?
- How does one optimized insertion perform across many different queries without further optimization?
- How much of multi-agent amplification is due to orchestration, payload adaptation, or differences in context passed between agents?
- Which factors explain high similarity and retrieval but low downstream success?
- What are the legitimate-task costs of the evaluated defenses?
- How do truncation, document chunking, and tokenization affect trigger effectiveness?
- Which theorem assumptions hold approximately in the tested models, and how does approximation affect the guarantee?
- Which reported numbers and model labels are intended where prose and visuals disagree?
- How sensitive are results to mailbox selection, query-generation procedure, and model settings?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning grounded in the paper |
|---|---|
| LLM | Large language model; the component that generates answers or instructions for actions. |
| RAG | Retrieval-augmented generation; supplying retrieved documents to a model before it answers. |
| IPI | Indirect prompt injection; instructions embedded in external material later read by the system. |
| PI | Prompt injection, the broader term used in the related-work discussion. |
| Agent | A model-driven component that plans or uses tools. |
| MAS | Multi-agent system; interacting agents divide tasks and pass information. |
| Corpus | The collection of external documents or emails searched by the retriever. |
| Embedding | A vector representation of text, or another query modality in the reported extension. |
| Embedding model | The function producing those vectors. |
| Cosine similarity | The vector-comparison score used for ranking in this study. |
| Top-\(K\) | The \(K\) highest-ranked retrieval results. |
| Attack fragment | The part of the inserted item carrying the unwanted instructions. |
| Trigger fragment | Tokens optimized to increase the whole item’s retrieval similarity. |
| Prefix | A token sequence placed before another sequence. |
| Token budget | The allowed trigger length \(n\). |
| Query budget | The allowed number \(B\) of score evaluations. |
| Black-box access | Ability to query a model without inspecting its parameters or gradients. |
| White-box access | Access to internal model information used by some competing optimization methods. |
| CEM | Cross-Entropy Method; iterative sampling and updating toward high-scoring candidates. |
| Monte Carlo | The probabilistic sampling approach used to generate candidate sequences. |
| Elite set | The selected high-scoring candidates used to update the distribution. |
| Factorized distribution | A sequence probability formed by multiplying separate probabilities for each position. |
| Smoothing | Blending old probabilities with frequencies from the elite set. |
| Query+ | Baseline that prepends the user query to the attack fragment. |
| Vanilla | Attack fragment without an optimized or query-based prefix. |
| Fusion | CEM trigger plus user query plus attack fragment. |
| Ideal baseline | A condition assuming the attack fragment is already available in model context. |
| Recall@5 / R@5 | Fraction of queries for which the malicious item is among five retrieved items. |
| MRR@K | Mean reciprocal rank at \(K\); rewards placing the malicious item near the top. |
| nDCG@K | Normalized discounted cumulative gain at \(K\); another rank-sensitive score. |
| ASR | Attack success rate, defined separately for the downstream task. |
| SIM | Cosine similarity in Table 2 and the similarity-transfer analysis. |
| Corpus competition | Similarity of the \(K\)-th ranked clean item to the query. |
| Transferability | Effectiveness after changing the model, trigger placement, or attack fragment. |
| Token dispersion | Scattering trigger tokens throughout the text. |
| Perplexity filtering | Screening text using a measure treated by the authors as a proxy for unnaturalness. |
| Token masking | Replacing selected tokens with a mask symbol. |
| Query paraphrasing | Rewriting the query while retaining its intended meaning. |
| Phishing worm | In this evaluation, an email payload involving a phishing link and self-replication instructions, measured separately. |
| Exfiltration | Sending data out of the intended environment; the code-execution task targets SSH key files. |
| SSH | The acronym used for the targeted key files; the supplied paper does not expand it. |
| DoS | Denial of service; named among attack categories, without a standalone quantitative service-availability experiment here. |
| MCP | Model Context Protocol; the tool interface used in the agent setup. |
| BEIR | The heterogeneous information-retrieval benchmark collection identified in reference [77]. |
| FAISS | The vector-search library used by the implementation; the supplied paper does not expand the name. |
| FAQ | Frequently asked question; ten are generated for the email evaluation. |
| NP-hard | A computational-hardness classification claimed for the stated search problem; its precise proof is absent. |
| \(O(\cdot)\) | Asymptotic scaling notation used in the theoretical query-cost statements; constants and some parameter dependencies are not specified. |

# 20. Key Numerical Results

This table is a compact index. Full figure matrices and table values appear in Sections 10–11.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Supplied document length | 20 | pages | Page-labeled text | Directly observable | pp. 1–20 |
| Retrieval datasets | 11 | datasets | BEIR evaluation | Author-reported | pp. 5–6 |
| Queries per dataset | 100 | queries | Retrieval subsample | Author-reported | p. 5 |
| Malicious insertions | 1 | item per target-query evaluation | Retrieval and email tests | Author-reported | pp. 5, 10 |
| Default retrieved count | 5 | documents | Top-\(K\) | Author-reported | p. 4 |
| Default trigger length | 10 | tokens | CEM | Author-reported | p. 6 |
| Default samples and iterations | 5,000; 30 | samples; iterations | CEM | Author-reported | p. 6 |
| Elite and smoothing parameters | .2; .55 | fractions | CEM defaults | Author-reported | p. 6 |
| Maximum score evaluations | 150,000 | accesses | Default search | Author-reported | pp. 7–8 |
| Trigger-generation API cost | .21 | US dollars | Voyage/OpenAI, paper’s reported conditions | Author-reported | p. 8 |
| Trigger-generation API cost | .76 | US dollars | Qwen-v4 maximum reported | Author-reported | p. 8 |
| Contriever/GTE/Q3-0.6B runtime | 1.6 / 2.3 / 7.6 | minutes | One H100 | Author-reported | p. 8 |
| Mean Recall@5, 3/5/10 tokens | 28.4 / 63.0 / 94.1 | % | Table averages | Visually readable | Table 3, p. 20 |
| Conflicting prose recall averages | 29.5 / 95.6 | % | 3/10 tokens | Author-reported; inconsistent | §A.1, p. 19 |
| Mean MRR@5, 10 tokens | .78 | fraction | Table average; prose says .79 | Visually readable | Table 3, p. 20 |
| Mean nDCG@5, 10 tokens | .82 | fraction | Table average | Visually readable | Table 3, p. 20 |
| MS MARCO Recall@5 | 74.0 ± 13.6 | % | 10 tokens | Visually readable | Table 3 |
| ArguAna Recall@5 | 77.5 ± 8.0 | % | 10 tokens | Visually readable | Table 3 |
| Eight-model direct retrieval | 100 for seven; 90 for OpenAI | % | FiQA | Visually readable | Figure 4 |
| Competition, NFCorpus | About .64 | similarity | Successful group | Author-reported approximation | p. 7; Figure 3 |
| Competition, MS MARCO | About .75 / .82 | similarity | Success/failure groups | Author-reported approximation | p. 7; Figure 3 |
| OpenAI-reference transfer mean | 73.75 | % | Eight target models; \(590/8\) | Analyst-derived | Figure 5 |
| OpenAI dispersed-trigger recall | 6 | % | Ten random dispersions | Visually readable | Figure 7 |
| GTE / Q3-4B dispersed recall | 90 / 91 | % | FiQA | Visually readable | Figure 7 |
| Post-trigger scatter values | Roughly .75–.89 | similarity | Alternate attack fragments | Approximate visual estimate | Figure 8 |
| Knowledge-poisoning ASR | .58 / .50 | fraction | Two/one trigger tokens | Author-reported | p. 10 |
| Email questions | 10 | questions | Model-generated from mailbox | Author-reported | p. 10 |
| Mailbox history threshold | ≥50 | emails | Sent and received history | Author-reported | p. 10 |
| Agent repetitions | 5 | runs | Different random seeds | Author-reported | p. 11 |
| GPT-4o CEM targeted answer | .02 ± .04 | ASR | R@5 = 1 | Visually readable | Table 2 |
| GPT-4o Fusion multi-agent exfiltration | .80 ± .07 | ASR | Code-execution task | Visually readable | Table 2 |
| GPT-4o CEM multi-agent exfiltration | .72 ± .16 | ASR | Code-execution task | Visually readable | Table 2 |
| GPT-4o-mini CEM single-agent exfiltration | .26 ± .09 | ASR | Code-execution task | Visually readable | Table 2 |
| GPT-4o Fusion worm propagation | .18 ± .13 | fraction | Separate from phishing .84 ± .11 | Visually readable | Table 2 |
| GPT-4o-mini Fusion worm propagation | .64 ± .11 | fraction | Separate from phishing .74 ± .09 | Visually readable | Table 2 |
| Fusion GPT-4o multi/single ratio | 40 | ratio of means | \(.80/.02\) | Analyst-derived | Table 2 |
| Initial paraphrasing degradation | <10 | % drop, as written | Most datasets; percentage-point meaning unspecified | Author-reported | p. 12 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Retrieval is an important barrier for the tested injection text. | Vanilla stays at zero while optimized triggers retrieve frequently. | Figure 2; X1 | pp. 6–7 | Strong for this payload and evaluated retrieval setup; not proof that all unoptimized malicious documents fail. |
| Compact black-box optimization can overcome that barrier. | High recall with 5–10 tokens and 94.1% ten-token table average. | Algorithm 1; Figures 2, 4; Table 3 | pp. 5–8, 20 | Substantial empirical support; universal guarantees are not established. |
| Corpus competition helps explain difficulty. | Failure groups often have higher fifth-clean-document similarity. | Figure 3; X2 | p. 7 | Observational support; no causal isolation or significance testing. |
| Larger/proprietary embeddings are not automatically resistant. | Direct optimization succeeds on all eight tested FiQA model conditions, with 90–100% recall. | Figure 4; X3 | p. 7 | Strong within this comparison; broader universality is unsupported. |
| Trigger transfer varies by architecture. | Cross-model matrix ranges from 0–100%. | Figure 5; X6 | p. 8 | Direct visual support; one prose cell attribution is incorrect. |
| Triggers can tolerate placement changes. | Many position curves remain high; several dispersion bars are 80–91%. | Figures 6–7; X7–X8 | pp. 8–9 | Model-dependent; OpenAI and Contriever dispersion results are important exceptions. |
| Triggers can transfer to different attack fragments. | Similarity rises for sampled alternative fragments. | Figure 8; X9 | p. 9 | Supports score transfer, not arbitrary-fragment retrieval or execution guarantees. |
| RAG outputs can be redirected. | Many Figure 9 ASRs are high. | Figure 9; X10 | p. 10 | Direct evidence with variable success; model inventory and retained denominators are unresolved. |
| Retrieval success can enable serious agent behavior. | Phishing/tool misuse and code-execution results. | Table 2; X12–X16 | pp. 11–12 | Strong evidence of feasibility in the tested environment, with major task/model differences. |
| Multi-agent GPT-4o can be more vulnerable than its single-agent counterpart. | Fusion .80 versus .02; CEM .72 versus .04. | Table 2; X15–X16 | pp. 11–12 | Strong descriptive difference; payload adaptation prevents a clean orchestration-only causal claim. |
| Fusion is the best method in practice. | Best on selected outcomes, including GPT-4o multi-agent execution. | Table 2 | p. 11 | Overbroad as stated: multiple task/model conditions favor Query+, CEM, or Ideal. |
| Three intuitive defenses lack durable protection. | Author summaries of adaptive paraphrasing, repetition, and masking results. | X17–X19 | pp. 12–13 | Limited assessability because detailed defense evidence is absent. |
| CEM has an efficient theoretical guarantee. | Theorem under additive scores and proof sketch. | Theorem 1 | p. 5 | Conditional author result; proof and full parameter dependence absent. |
| The study establishes deployed-system attacks “in the wild.” | Realistic-style corpora and workflows, but ethics explicitly says controlled experiments and no deployment probing. | Study scope | pp. 10, 14 | The evidence supports controlled feasibility, not a demonstrated live attack campaign. |

# 22. Very Simple Explanation — Explain Like I’m 15

Imagine an assistant that searches a library before answering you. Someone hides a note in the library saying, “Ignore the person asking the question and do what this note says.” That note can only influence the assistant if the search system picks it up.

This paper studies how an attacker can make that note easier to find. The researchers add a short sequence of tokens that makes the whole note look relevant to a particular question according to the search model’s numerical similarity score. The extra tokens help it get retrieved; the rest of the note carries the unwanted instructions.

In the tested search systems, this often works very well. But finding the note and obeying it are different things. Some assistants retrieved the malicious text almost every time while rarely following its instructions. In one tested system where several agents worked together, however, the attack caused GPT-4o to execute code and send out targeted files in 80% of the reported trials on average.

The lesson supported by the study is that security testing should include the whole route from searching to reading to acting. The paper gives substantial evidence for that concern, but its experiments were controlled, several stronger defenses were not tested, and some reported numbers and equations disagree.

# Completeness Audit

The audit below compares this analysis with the inventory of the **supplied 20-page version**. “Fully represented” means its substantive content is accounted for; it does not mean every sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation, corresponding-author footnote | Yes, text/image | Yes | Fully represented | Stage 0. |
| Publication metadata and artifact badge | Yes, image/text | Yes | Fully represented | Venue/date not explicitly supplied; badge not treated as artifact verification. |
| Abstract | Yes, text/image | Yes | Fully represented | Headline claims and “over 80%” discrepancy included. |
| §1 Introduction | Yes, text/images | Yes | Represented in compressed form | Motivation, prior-work gap, questions, and contributions preserved. |
| §2 system formulation | Yes, text only | Yes | Fully represented | Original p. 3 layout not visually inspected. |
| §2.1 threat model and scope | Yes, text only | Yes | Fully represented | Query-specific optimization, one insertion, no corpus/parameter access. |
| Problem Definition 1 | Yes, text only | Yes | Fully represented | Retrieval-to-execution implication qualified. |
| §3.1 similarity optimization | Yes, text/image | Yes | Fully represented | Objectives, budgets, hardness claim, and notation issues. |
| Problem Definition 2 | Yes, text/image | Yes | Fully represented | Apparent argmax typo retained and explained. |
| §3.2 CEM method | Yes, text/images | Yes | Fully represented | Factorization, sampling, selection, update, rationale. |
| Algorithm 1 | Yes, text/image | Yes | Fully represented | Boundary and initialization ambiguities disclosed. |
| Cosine-similarity definition | Yes, text only | Yes | Fully represented | Symbols, role, and nonzero-norm boundary. |
| Retrieval-threshold inequality | Yes, text/image | Yes | Fully represented | Reproducible counterexample to printed indexing. |
| Equations (1), (2) | Yes, text/image | Yes | Fully represented | Objective and approximation condition. |
| Equations (3), (4) | Yes, text/images | Yes | Fully represented | Factorization and sampling. |
| Equation (5) | Yes, text/image | Yes | Fully represented | Elite-selection boundary issue. |
| Equations (6), (7) | Yes, text/image | Yes | Fully represented | Smoothing and empirical token frequencies. |
| Theorem 1 and proof sketch | Yes, text/image | Yes | Fully represented | Conditional statement and verification limits. |
| Detailed theorem proof | No | Absence represented | Missing from supplied material | Referenced but not present. |
| NP-hardness technical statement/proof | No | Absence represented | Missing from supplied material | Deferred to full version. |
| §4 experimental setup | Yes, text/images | Yes | Fully represented | Datasets, models, defaults, baselines, metrics, hardware. |
| Prompt 1 | Yes, text/image | Yes | Represented in compressed form | Fixed “Yes” target and claimed-authority mechanism summarized; exact repetitive payload wording not reproduced. |
| §4.1 retrieval effectiveness | Yes, text/images | Yes | Fully represented | Includes length, competition, model comparison, and cost. |
| §4.2 transferability | Yes, text/images | Yes | Fully represented | All four transfer conditions distinguished. |
| §5 end-to-end framing | Yes, text/image | Yes | Fully represented | Retrieval and execution kept separate. |
| §5.1 RAG | Yes, text/image | Yes | Fully represented | Setup, exclusions, five seeds, figure, knowledge extension. |
| §5.2 agents | Yes, text/images | Yes | Fully represented | Architecture, tasks, methods, metrics, and model effects. |
| §6 query paraphrasing | Yes, text/image | Yes | Fully represented for available content | Detailed experiment absent. |
| §6 perplexity filtering | Yes, text/image | Yes | Fully represented for available content | Figure 12 and thresholds absent. |
| §6 token masking and defense scope | Yes, text/images | Yes | Fully represented for available content | Masking rates and full ablations absent. |
| §7 indirect-injection related work | Yes, text/image | Yes | Represented in compressed form | Author positioning preserved, external claims not verified. |
| §7 RAG poisoning | Yes, text/image | Yes | Represented in compressed form | Scope distinction retained. |
| §7 retrieval optimization and content defenses | Yes, text/image | Yes | Represented in compressed form | Baseline rationale and orthogonal defense scope retained. |
| §8 scope limitation | Yes, text/image | Yes | Fully represented | Embedding-only; no hybrid/reranking. |
| §8 transfer limitation | Yes, text/image | Yes | Fully represented | Architecture-dependent transfer. |
| §8 novelty limitation | Yes, text/image | Yes | Fully represented | CEM prior origin. |
| §9 conclusion | Yes, text/image | Yes | Represented in compressed form | End-to-end evaluation and defense implications. |
| Ethics: stakeholders and principles | Yes, text/image | Yes | Represented in compressed form | Researchers/developers/users; controlled and public/synthetic-data claims. |
| Ethics: harms, controlled scope, second-order effects | Yes, text/image | Yes | Represented in compressed form | No live deployments; misuse and broader-safety cautions retained. |
| Open Science | Yes, text/image | Yes | Fully represented | Repository reported, not inspected. |
| References [1]–[104] | Yes, supplied text | Yes, as bibliographic inventory | Represented in compressed form | Not reproduced entry by entry or externally validated; internal mismatch noted. |
| RQ1–RQ7 and O1–O3 | Yes | Yes | Fully represented | Section 5 and experiment register. |
| Formal hypotheses | None identified | Yes | Fully represented as absent | Informal conjecture distinguished from formal hypothesis tests. |
| X1–X4: retrieval, competition, models, efficiency | Yes | Yes | Fully represented | Figures 2–4 and reported resource values. |
| X5: multimodal extension | Summary only | Yes | Represented in compressed form | Full setup and Appendix C missing. |
| X6–X9: transfer experiments | Yes | Yes | Fully represented | Figures 5–8; score versus ASR distinction retained. |
| X10: RAG fixed-answer experiment | Yes | Yes | Fully represented | Full displayed heatmap transcribed. |
| X11: knowledge poisoning | Summary only | Yes | Fully represented for available content | Detailed example and results missing. |
| X12–X16: agent experiments | Yes | Yes | Fully represented | All Table 2 values preserved. |
| X17–X19: defenses | Summary only | Yes | Fully represented for available content | Missing detailed evidence explicitly identified. |
| X20: additional metrics | Yes | Yes | Fully represented | Full Table 3 values preserved. |
| X21: hyperparameters | Yes | Yes | Fully represented | Four Figure 10 panels and caveats. |
| Figure 1 | Yes, visual | Yes | Fully represented | Conceptual diagram distinguished from measured geometry. |
| Figure 2 | Yes, visual | Yes | Fully represented | All 11 panels accounted for; unlabeled points not digitized. |
| Figure 3 | Yes, visual | Yes | Fully represented | Grouping and observational limitation. |
| Figure 4 | Yes, visual | Yes | Fully represented | All eight labeled values. |
| Figure 5 | Yes, visual | Yes | Fully represented | All 64 matrix values and transfer discrepancy. |
| Figure 6 | Yes, visual | Yes | Fully represented | All eight panels; exact unlabeled coordinates unavailable. |
| Figure 7 | Yes, visual | Yes | Fully represented | All eight labeled values. |
| Figure 8 | Yes, visual | Yes | Fully represented | Encodings, trend, approximate range, sample-detail limits. |
| Figure 9 | Yes, visual | Yes | Fully represented | All 132 displayed cells; count/label inconsistencies. |
| Figure 10 | Yes, visual | Yes | Fully represented | Four parameter panels; approximate trend interpretation. |
| Table 1 | Yes, visual/text | Yes | Fully represented | All data rows and values. |
| Table 2 | Yes, visual/text | Yes | Fully represented | All task/model/method values and error terms. |
| Table 3 | Yes, visual/text | Yes | Fully represented | All three metrics, lengths, datasets, and error terms. |
| Appendix A introduction | Yes, text/image | Yes | Represented in compressed form | Longer technical report explicitly absent. |
| Appendix A.1 | Yes, text/images | Yes | Fully represented | Metric definitions, results, discrepancies. |
| Appendix A.2 | Yes, text/image | Yes | Fully represented | Hyperparameters. |
| Referenced A.2.1 and A.3 | No | Absence represented | Missing from supplied material | Examples, complete prompts, queries, payloads, and logs. |
| Referenced Appendix B, B.1, B.2, Figure 12 | No | Absence represented | Missing from supplied material | Detailed defense results. |
| Referenced Appendix C | No | Absence represented | Missing from supplied material | Multimodal details. |
| Supplied supplementary files | None | Yes | No supplementary files supplied | No artifact contents inspected. |
| Decorative icons and repeated prose | Yes where rendered | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | Icons explained by diagram role; repeated headline language consolidated. |

## Missing or inaccessible material

- Visual renderings of pp. 3 and 15–18; their text was available.
- The fuller technical report and its detailed theoretical proofs.
- Full-version RAG examples and knowledge-poisoning details.
- Agent queries, complete prompts and attack fragments, and execution logs.
- Detailed defense results, thresholds, dataset breakdowns, and additional ablations.
- Full multimodal experiment setup and results.
- Repository contents, executable code, and evaluation scripts.
- Exact point-level data for plots without numerical labels.

## Uncertain interpretations

- Which retrieval averages and perfect-recall statements were intended where p. 19 conflicts with Table 3.
- The intended RAG model count and some model-size labels.
- Whether Enron was used directly or transformed into a synthetic evaluation corpus.
- The exact definition and repetition count behind Table 3 uncertainty terms.
- Tie handling, elite-set boundaries, the printed argmax, and the retrieval-threshold formula.
- The cutoff treatment in the displayed nDCG equation.
- The theorem’s full assumptions, constants, proof, and applicability to actual embedding scores.
- Whether changes in similarity, positional behavior, or agent context are causal explanations for the observed outcomes.
- Whether “<10% drop” in the paraphrasing discussion means relative percent or percentage points.

## Deliberately compressed material

- Repeated motivation, novelty claims, and conclusions.
- Bibliography entries, while retaining their role and relevant internal citation inconsistency.
- Exact wording of Prompt 1 and illustrative harmful instructions; their scientific purpose and measured outcomes are represented.
- Ethics prose, consolidated into stakeholders, stated principles, controlled scope, misuse concerns, and broader-safety cautions.
- Unlabeled plot coordinates, represented through trends and explicitly approximate observations rather than fabricated precision.

## Potential omissions

Every substantive component identified in the supplied-document inventory is represented or explicitly marked as missing, uncertain, or compressed. This does **not** establish completeness for the referenced full version, validate the absent proofs or code, or resolve the paper’s internal inconsistencies.