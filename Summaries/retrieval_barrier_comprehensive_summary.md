# *Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems*

**Authors:** Hongyan Chang, Ergute Bao, Xinjian Luo, and Ting Yu  
**Affiliation:** Mohamed bin Zayed University of Artificial Intelligence

## 1. Background and Context

Modern large language model systems often retrieve information from external sources because an LLM’s training-time knowledge may be outdated or too general. Retrieval supports systems such as web-enabled assistants, document-question-answering tools, coding assistants, research copilots, and agents that inspect operational logs.

A typical retrieval-based system has three stages:

1. The user’s query is converted into an embedding vector.
2. Documents with embeddings most similar to the query are retrieved from an external corpus.
3. An LLM uses the query and retrieved documents to answer or take actions, potentially through tools or other agents.

This creates an attack surface called **indirect prompt injection (IPI)**. Instead of directly entering malicious instructions as the user’s prompt, an attacker places them in an external source—such as a webpage, document, or email—hoping that the system retrieves and follows them. Such instructions can manipulate answers, send phishing messages, misuse tools, or execute code without the user realizing why.

Previous IPI studies usually assumed that the poisoned material was already in the model’s context. Typical artificial setups made the system retrieve the “latest email,” used a corpus containing only one malicious item, required special trigger words in the user’s query, fine-tuned a retriever with a backdoor, or fixed tools so that they always returned the malicious item. These experiments showed what could happen **after retrieval**, but did not establish whether poisoned content would surface under ordinary queries in realistic corpora.

The authors identify retrieval as the key unresolved barrier. In their initial experiments, an unoptimized malicious document was never retrieved for natural queries across 11 information-retrieval benchmarks, regardless of corpus or query size. If malicious content never reaches the LLM, its embedded instructions cannot affect the system.

Existing ways to improve retrieval are inadequate for the paper’s threat model:

- White-box attacks optimize against the embedding model’s gradients, but deployed embedding services are commonly accessible only through APIs.
- The strongest practical black-box heuristic, **Query+**, simply prepends or repeats the target query in the poisoned document. It improves similarity only modestly and does not reliably defeat realistic benign corpora.
- Prior email-worm work prepended benign company descriptions, but the authors report that this heuristic had effectively zero retrieval in their setting.

The paper therefore distinguishes two components of poisoned content:

- The **attack fragment** contains the actual malicious instructions.
- The **trigger fragment** is a short sequence whose sole purpose is to make the complete malicious item rank among the retrieved documents.

### Figure 1: Attack pipeline

Figure 1 illustrates this decomposition and the complete attack path. A user asks agents to check and summarize reimbursement emails. An attacker inserts a malicious item consisting of an optimized trigger fragment plus an attack fragment containing instructions such as denial of service, spamming, or code execution. The retrieval system embeds the query and corpus items; the trigger moves the malicious item close to the query in embedding space. Once retrieved, the agents or base LLM may give a wrong answer, send spam, or run a destructive command. The diagram emphasizes that a successful IPI must first cross the retrieval stage before it can affect downstream behavior.

## 2. Research Goal and Objectives

The central question is:

> Can a single malicious document be reliably retrieved—and then cause real downstream harm—under natural user queries, realistic corpora, and black-box access to the embedding model?

The study has four main objectives:

1. Determine whether retrieval is the decisive bottleneck in realistic IPI attacks.
2. Construct a compact trigger fragment that makes an arbitrary attack fragment appear in the top retrieval results without access to the corpus, retriever parameters, or LLM parameters.
3. Test the method across diverse datasets, embedding models, RAG systems, and single- and multi-agent systems.
4. evaluate simple retrieval-stage defenses and determine whether adaptive attacks can bypass them.

The authors seek to demonstrate the first end-to-end IPI attacks under natural queries across both RAG and agentic systems.

## 3. Methods (Approach/Design)

### 3.1 Retrieval system and threat model

The external corpus is represented as documents \(D_1,\ldots,D_m\). An embedding model \(E\) maps each document and user query \(q\) into a \(d\)-dimensional vector. Documents are ranked using cosine similarity, which ranges from −1 to 1; larger values mean greater embedding similarity. The system returns the top \(K\) items, with the experiments primarily using \(K=5\).

The adversary chooses an arbitrary attack fragment \(D_{\text{adv}}\), such as instructions to provide misinformation, propagate phishing, or execute a Python command. The attacker prepends a trigger fragment \(x\), producing \(x\Vert D_{\text{adv}}\).

The attacker is deliberately restricted:

- They may inject only **one malicious item**.
- They cannot inspect the benign corpus.
- They do not know the retriever or LLM parameters.
- They have no embedding-model gradients.
- They can only submit sequences to the embedding model’s normal API and obtain their embedding vectors.
- The paper assumes the attack fragment already exists and studies how to retrieve it, not how to design its downstream malicious instructions.

The goal is to make \(x\Vert D_{\text{adv}}\) rank in the top \(K\) for a natural query.

### 3.2 Prefix-search objective

The score for a candidate trigger \(x\) is the cosine similarity

\[
f(x)=\operatorname{sim}\big(E(q),E(x\Vert D_{\text{adv}})\big).
\]

A successful trigger must exceed the similarity of all but at most \(K\) benign documents. Because the attacker cannot inspect the corpus, that threshold is unknown. The authors state that finding a prefix guaranteed to cross it is NP-hard in this setting; the technical statement and proof are deferred to the full arXiv version.

They instead define an **\(\varepsilon\)-optimal prefix search**: within the set of sequences of a fixed length \(n\), find a trigger whose score is within \(\varepsilon\) of the best possible trigger. The length \(n\) is the **token budget**. Increasing it enlarges the search space and may improve the maximum achievable similarity, but long prefixes are less stealthy and embedding models have finite input limits.

A naive greedy search would evaluate every vocabulary token at every position, requiring as many as \(n|V|\) evaluations. Brute-force sequence sampling could require \(O(|V|^n)\) evaluations. Both are impractical under API-query and computation limits.

### 3.3 Cross-Entropy Method attack

The proposed attack adapts the existing **Cross-Entropy Method (CEM)**, a Monte Carlo optimization method, to black-box trigger construction.

The algorithm maintains a separate probability distribution over vocabulary tokens for every one of the \(n\) trigger positions. The joint distribution is factorized:

\[
p(x)=\prod_{i=1}^{n}p_i(x[i]).
\]

This requires an \(n\times|V|\) representation rather than explicitly representing all \(|V|^n\) possible sequences.

Each iteration performs four steps:

1. **Sample:** Draw \(N\) candidate trigger sequences from the current distributions.
2. **Evaluate:** Compute \(f(x)\) for every candidate using the embedding API.
3. **Select:** Retain the highest-scoring fraction \(\lambda\), called the elite set.
4. **Update:** Increase the probability of tokens that occur in elite candidates. A smoothing parameter \(\alpha\) controls how much the new distribution moves toward the elite-token frequencies.

After \(T\) iterations, the best-scoring candidate is returned.

The default configuration is:

- Trigger length \(n=10\)
- 5,000 candidates per iteration
- \(T=30\) iterations
- Elite fraction \(\lambda=0.2\)
- Smoothing \(\alpha=0.55\)
- At most 150,000 black-box embedding evaluations

The paper proves a conditional utility guarantee. If the score decomposes linearly across token positions, then with \(T=O(\log |V|)\) iterations and \(N=O(\log(1/\delta))\) samples per iteration, the algorithm returns an \(\varepsilon\)-optimal trigger with probability at least \(1-\delta\). The intuition is that each iteration increases the probability of sampling useful tokens. The authors motivate the factorization and approximate linearity by noting that modern sentence embeddings often pool token representations and can be relatively insensitive to token order.

### 3.4 Retrieval datasets

The authors use 100 target queries from the test split of each of 11 BEIR datasets. Exactly one malicious document is constructed and injected for each query.

**Table 1: Dataset characteristics**

| Task | Dataset | Documents | Mean query length | Mean document length |
|---|---:|---:|---:|---:|
| Passage retrieval | MSMARCO | 8.8M | 6.0 words | 56.0 words |
| Biomedical retrieval | TREC-COVID | 0.171M | 10.6 | 160.8 |
| Biomedical retrieval | NFCorpus | 0.036M | 3.3 | 232.3 |
| Question answering | Natural Questions | 2.7M | 9.2 | 78.9 |
| Question answering | HotpotQA | 5.2M | 17.6 | 46.3 |
| Question answering | FiQA-2018 | 0.058M | 10.8 | 132.3 |
| Argument retrieval | ArguAna | 0.087M | 193.0 | 166.8 |
| Entity retrieval | DBPedia | 4.6M | 5.4 | 49.7 |
| Citation prediction | SCIDOCS | 0.026M | 9.4 | 176.2 |
| Fact checking | FEVER | 5.4M | 8.1 | 84.8 |
| Fact checking | SciFact | 0.052M | 12.4 | 213.6 |

These datasets span approximately 26,000 to 8.8 million documents, queries averaging 3.3–193 words, and documents averaging 46.3–232.3 words.

### 3.5 Embedding models

The default model is **gte-modernbert-base**, with 139 million parameters and 768 embedding dimensions. Seven additional models are tested:

- Contriever-MSMARCO: 110M parameters, 768 dimensions
- Qwen3-Embedding-0.6B: 1,024 dimensions
- Qwen3-Embedding-4B: 2,560 dimensions
- Qwen3-Embedding-8B: 4,096 dimensions
- OpenAI text-embedding-3-small
- Voyage AI voyage-3.5-lite
- Alibaba Cloud text-embedding-v4, called Qwen-v4

The experiments use BEIR, FAISS, and an H100 GPU.

### 3.6 Retrieval baselines and measures

The attack is compared with:

- **Vanilla:** Inject only the attack fragment, with no trigger.
- **Query+:** Prepend the original user query.
- **CEM:** Prepend the optimized trigger.

All methods use the same attack fragment. For initial retrieval experiments, that fragment instructs the LLM to disregard other information and respond only with “Yes.”

The principal measure is **Recall@5**: whether the single malicious document appears among the five retrieved items. Because there is one malicious item, the score for a query is either 0 or 1 and is averaged across 100 queries.

Appendix experiments also report:

- **MRR@5:** Rewards placing the malicious item near the top; it is the reciprocal of its rank when ranked 1–5 and zero otherwise.
- **nDCG@5:** Also gives more credit to higher positions using a logarithmic rank discount.

### 3.7 End-to-end RAG evaluation

For RAG, the malicious document tells the LLM to answer “Yes” regardless of the query. Attack success rate (ASR) is the fraction of queries for which the clean system did not answer “Yes,” but the poisoned system did. Queries where the clean model already gave the target answer are excluded.

The paper tests 11 datasets and 11 LLMs, including:

- Qwen3 models from 0.8B to 32B
- LLaMA-3 3B and 8B, including base and instruction-tuned variants
- Vicuna 7B and 13B

The figure itself displays 12 model rows because it separately shows six Qwen3 sizes, four LLaMA base/instruction variants, and two Vicuna sizes; the surrounding text nevertheless describes the experiment as covering 11 LLMs. Results are averaged over five random seeds.

### 3.8 Agentic-system evaluation

The authors use the Enron email corpus and select a user with at least 50 sent and received emails. Claude Sonnet 4 generates ten frequently asked questions from this user’s history. For every question, the attacker inserts one malicious email.

Two systems are evaluated:

- **Single-agent AutoGen:** Round-robin access to email retrieval, send-email, contact-list, and Python-execution tools.
- **Multi-agent Magentic-One:** An Orchestrator delegates to FileSurfer, Coder, and Computer Terminal agents. A retriever agent can search email, send email, and access contacts.

GPT-4o and GPT-4o-mini serve as base models. Tools use MCP.

Four attack objectives are tested:

1. **Targeted answer manipulation**
2. **Phishing-worm propagation**, measuring both inclusion of a phishing link and forwarding of self-replication instructions
3. **Tool misuse**, measuring whether the agent emails every contact and includes a phishing link
4. **Code execution**, where malicious Python exfiltrates SSH keys from `~/.ssh`

The methods are:

- **Ideal:** The attack fragment is assumed already retrieved.
- **Query+:** User query plus attack fragment.
- **CEM:** A learned 10-token trigger plus attack fragment.
- **Fusion:** CEM trigger plus user query plus attack fragment.

Each experiment is repeated with five random seeds. The paper reports Recall@5, query–malicious-document cosine similarity, and ASR with standard deviations.

## 4. Results and Findings

### 4.1 Retrieval effectiveness

#### Figure 2: Recall as trigger length increases

Figure 2 plots Recall@5 against trigger lengths from approximately 1 to 20 for all 11 datasets. CEM is the red curve, Query+ the blue dashed curve, and Vanilla the green dashed line.

The main patterns are:

- Vanilla remains near zero on every dataset.
- CEM consistently outperforms Query+ at the same trigger length.
- On NFCorpus, Natural Questions, SciFact, HotpotQA, DBPedia, SCIDOCS, and FEVER, only 5–10 optimized tokens produce near-perfect recall.
- MS MARCO and ArguAna are more difficult, but CEM generally exceeds 80% and sometimes 90% around 15 tokens.
- Query+ improves much more slowly; on ArguAna it remains near 20% even as length increases.
- CEM therefore achieves better retrieval using shorter, potentially less conspicuous triggers.

#### Table 3: Exact retrieval results

The supplied table gives the following Recall@5 percentages:

| Dataset | \(n=3\) | \(n=5\) | \(n=10\) |
|---|---:|---:|---:|
| MSMARCO | 7.9±3.8 | 35.3±3.4 | 74.0±13.6 |
| TREC-COVID | 0.4±0.8 | 7.6±3.2 | 87.6±11.8 |
| NFCorpus | 94.0±3.6 | 100.0±0.0 | 100.0±0.0 |
| Natural Questions | 7.0±1.1 | 48.8±3.1 | 98.6±2.8 |
| HotpotQA | 11.4±2.2 | 80.4±2.4 | 100.0±0.0 |
| FiQA-2018 | 31.6±3.4 | 73.4±2.4 | 97.8±3.9 |
| ArguAna | 1.8±0.7 | 16.6±0.8 | 77.5±8.0 |
| DBPedia | 45.8±8.3 | 91.4±5.9 | 100.0±0.0 |
| SCIDOCS | 24.0±3.0 | 78.2±2.5 | 100.0±0.0 |
| FEVER | 10.2±1.6 | 62.4±4.2 | 99.8±0.4 |
| SciFact | 77.8±3.0 | 98.6±0.8 | 100.0±0.0 |
| **Average** | **28.4** | **63.0** | **94.1** |

At \(n=10\), seven datasets reach exactly 100% recall and FEVER reaches 99.8%. MS MARCO is the weakest at 74.0%, followed by ArguAna at 77.5%.

The corresponding average MRR@5 values are 0.18, 0.45, and 0.78 for lengths 3, 5, and 10; average nDCG@5 values are 0.20, 0.49, and 0.82. Exact \(n=10\) MRR@5 values range from 0.40 on ArguAna to 0.97 on NFCorpus and DBPedia. Exact \(n=10\) nDCG@5 ranges from 0.49 on ArguAna to 0.98 on NFCorpus and DBPedia.

The prose immediately preceding Table 3 reports averages of 29.5% Recall@5 at \(n=3\), 95.6% at \(n=10\), and 0.79 MRR@5 at \(n=10\). These do not exactly match the supplied table’s 28.4%, 94.1%, and 0.78. The table values are reported above without attempting to reconcile the discrepancy.

Variation across seeds is generally limited, although the most difficult datasets show larger uncertainty, such as ±13.6 on MS MARCO and ±11.8 on TREC-COVID at \(n=10\).

### 4.2 What determines retrieval difficulty?

Corpus size and document length do not explain vulnerability. Large datasets such as MS MARCO with 8.8 million documents and FEVER with 5.4 million are vulnerable alongside NFCorpus with only 36,000 documents.

The authors instead define **corpus competition level** as the similarity between the query and the fifth-ranked clean document. A high value means that several benign documents are strongly relevant, so a malicious item must achieve a higher similarity to enter the top five.

#### Figure 3: Competition versus success

Figure 3 compares average competition levels for queries where CEM succeeds and fails.

- NFCorpus has a low competition level of about 0.64 and no failed attacks.
- In MS MARCO, failed attacks have competition around 0.82, versus about 0.75 for successful attacks.
- Across datasets, failures tend to occur when clean documents are more similar to the query.

Thus, dense semantic relevance—not merely the number or length of documents—is the primary obstacle.

### 4.3 Robustness across embedding models

#### Figure 4: Eight models on FiQA

On FiQA, CEM obtains:

- GTE: 100% Recall@5
- Contriever: 100%
- Qwen3-0.6B: 100%
- Qwen3-4B: 100%
- Qwen3-8B: 100%
- Voyage: 100%
- OpenAI: 90%
- Qwen-v4: 100%

Larger, newer, or proprietary embedding models therefore provide no general protection. The vulnerability occurs across BERT, ModernBERT, Qwen3, open-source models, and commercial APIs.

### 4.4 Cost and speed

At the default 150,000 embedding calls:

- A trigger costs **$0.21** using Voyage 3.5 Lite or OpenAI text-embedding-3-small.
- It costs at most **$0.76** with Qwen text-embedding-v4.
- On one H100 GPU, optimization takes 1.6 minutes for Contriever, 2.3 minutes for GTE, and 7.6 minutes for Qwen3-0.6B.
- Nearly all runtime comes from embedding computation; the CEM update itself has negligible overhead.

The paper also reports an image-to-text experiment on MS COCO using OpenCLIP embeddings. Even a few adversarial tokens produced near-perfect recall, suggesting that the vulnerability arises from shared vector embedding spaces rather than being limited to text queries. Detailed multimodal results are deferred to Appendix C of the full version and were not supplied.

### 4.5 Hyperparameter effects

#### Figure 10: CEM hyperparameters on MS MARCO

With trigger length fixed at ten, Figure 10 varies:

- Number of iterations \(T\)
- Candidates per iteration \(N\)
- Elite fraction \(\lambda\)
- Smoothing \(\alpha\)

More iterations and larger candidate batches consistently raise query–malicious-document similarity. Smaller elite fractions, which retain fewer but better candidates, generally improve similarity, with diminishing returns when the elite set becomes extremely small. Smoothing has relatively little effect, producing only minor fluctuations.

### 4.6 Transfer across embedding models

#### Figure 5: Cross-model transfer matrix

Figure 5 applies each trigger optimized on a reference model to all eight target models.

The exact matrix, with rows as target models and columns ordered GTE, Contriever, Qwen3-0.6B, Qwen3-4B, Qwen3-8B, Voyage, OpenAI, and Qwen-v4, is:

- **GTE target:** 100, 40, 40, 40, 40, 60, 60, 40
- **Contriever:** 40, 100, 30, 30, 40, 40, 20, 40
- **Qwen3-0.6B:** 90, 90, 100, 90, 90, 90, 100, 90
- **Qwen3-4B:** 90, 90, 90, 100, 90, 70, 90, 90
- **Qwen3-8B:** 80, 70, 80, 100, 100, 70, 80, 90
- **Voyage:** 60, 40, 40, 30, 60, 100, 60, 60
- **OpenAI:** 20, 0, 30, 30, 10, 30, 90, 20
- **Qwen-v4:** 70, 60, 100, 90, 90, 70, 90, 100

Triggers transfer particularly well within the Qwen family. Cross-architecture transfer is less reliable: a Qwen3-0.6B trigger achieves only 10% on OpenAI. Conversely, a trigger optimized on OpenAI averages 74% across target models and exceeds 60% on seven of eight, with Contriever as the exception. The results suggest that attackers may need to know or correctly guess the target architecture.

### 4.7 Transfer across positions and token dispersion

#### Figure 6: Moving a prefix away from position zero

For most models, a trigger optimized at the beginning of the document remains above 50% Recall@5 when moved through positions up to about 60, with moderate fluctuations. Qwen3-4B and Qwen-v4 remain near perfect across positions, while GTE, Qwen3-8B, and Voyage fluctuate but remain substantially effective.

OpenAI is the major exception: a trigger giving about 80% recall at position zero falls to nearly 0% around position 20. This indicates stronger location sensitivity. Nevertheless, optimizing directly at the end still produces 60% recall, so positional encoding is not a complete defense.

#### Figure 7: Randomly scattering trigger tokens

When the ten trigger tokens are randomly dispersed through the document rather than kept together, average FiQA Recall@5 over ten dispersions is:

- GTE: 90%
- Contriever: 22%
- Qwen3-0.6B: 68%
- Qwen3-4B: 91%
- Qwen3-8B: 80%
- Voyage: 88%
- OpenAI: 6%
- Qwen-v4: 86%

Several models evidently aggregate token information globally. This lets attackers hide trigger tokens throughout an otherwise normal-looking document. OpenAI’s location sensitivity sharply weakens naive dispersion, although attackers could optimize directly over the intended scattered positions.

### 4.8 Transfer across attack fragments

#### Figure 8: A trigger reused with other payloads

Figure 8 compares query similarity for attack fragments alone against similarity after adding a trigger optimized with a different attack fragment. The blue points represent randomly sampled attack fragments of varying lengths; the pink point is the original targeted fragment.

Across all tested fragments, the transferred trigger raises similarity. Values starting around −0.1 can rise as high as 0.76. The points form a clear upward relationship, indicating that the trigger carries a broadly reusable retrieval signal rather than being tightly tied to one payload. This reduces the need to rerun optimization for every malicious objective.

### 4.9 End-to-end RAG results

#### Figure 9: Targeted-answer ASR

Figure 9 is a heat map covering 11 datasets and the displayed LLM variants. A single poisoned document attempts to force the answer “Yes.”

Most cells show substantial vulnerability, frequently between 0.7 and 1.0. Several Qwen models reach 1.0 on particular datasets, and many model–dataset combinations are at or above 0.8. MS MARCO is generally weaker, matching its lower retrieval recall.

The authors’ main observations are:

- Nearly every tested model and dataset is vulnerable once the malicious document is retrieved.
- Without the optimized prefix, the attack fragment alone is never retrieved, so ASR is zero.
- Instruction-tuned models are usually more vulnerable because they follow the injected instruction more faithfully.
- Greater model size does not protect the system; Vicuna-13B can be more vulnerable than Vicuna-7B.
- Qwen models behave similarly across scales.
- Retrieval is the common failure point: once the poisoned item enters the top \(K\), model family, size, and tuning offer little dependable protection.

For a knowledge-poisoning comparison on Natural Questions with LLaMA-2-7B, prior Query+ work obtained 0.58 ASR by prepending the full query, whose average length was 9.2 tokens. CEM matches 0.58 with only a two-token trigger and still obtains 0.50 with one token.

### 4.10 Single- and multi-agent results

Agent-generated retrieval queries sometimes differ substantially from the original user query. This reduces the usefulness of Query+, which repeats the original wording. In the worm task, Query+ retrieval recall falls to 56%. CEM generally attains near-perfect retrieval with ten tokens despite Query+ using approximately 11–20 tokens. Fusion improves similarity and stabilizes retrieval further.

#### Table 2: GPT-4o

Key results include:

- **Targeted answer:** Query+ and CEM both have R@5=1, but CEM raises similarity from 0.76 to 0.85. ASR remains low: 0.14±0.05 for Query+, 0.02±0.04 for CEM, and 0.16±0.11 for Fusion.
- **Phishing worm:** Ideal-context success is 0.77±0.11 for including the phishing content but only 0.01±0.03 for self-replication. Query+ has R@5=0.56, similarity 0.70, phishing success 0.38±0.14, and worm success 0.08±0.06. CEM reaches R@5=1 and similarity 0.77, with phishing success 0.66±0.17 but worm success 0.00. Fusion reaches R@5=1, similarity 0.81, phishing success 0.84±0.11, and worm success 0.18±0.13.
- **Tool misuse:** The ideal baseline emails all contacts and includes phishing at 1.00±0.00. Query+ reaches R@5=1, similarity 0.78, and 0.99±0.04 for both sending and phishing. CEM reaches R@5=1, similarity 0.83, and 0.92±0.08 for both. Fusion records R@5=0.98, similarity 0.87, and 0.98±0.04 for both.
- **Single-agent code execution:** Ideal ASR is 0.02±0.04. Query+ has R@5=1, similarity 0.73, and ASR 0.02±0.04. CEM has R@5=1, similarity 0.79, and ASR 0.04±0.05. Fusion has R@5=1, similarity 0.85, and ASR 0.02±0.04.
- **Multi-agent code execution:** Ideal ASR is 0.58±0.18. Query+ has R@5=1, similarity 0.76, and ASR 0.56±0.05. CEM reaches R@5=1, similarity 0.78, and ASR **0.72±0.16**. Fusion reaches R@5=1, similarity 0.85, and ASR **0.80±0.07**.

#### Table 2: GPT-4o-mini

- **Targeted answer:** Ideal and Query+ ASR are 0.00. CEM has R@5=0.98 and similarity 0.85 but ASR 0.00; Fusion has R@5=1, similarity 0.89, and ASR 0.04±0.05.
- **Phishing worm:** Ideal produces phishing at 0.87±0.08 and worm propagation at 0.83±0.13. Query+ has R@5=0.63, similarity 0.70, phishing 0.51±0.11, and worm 0.46±0.10. CEM has R@5=1, similarity 0.77, phishing 0.64±0.17, and worm 0.46±0.11. Fusion has R@5=1, similarity 0.81, phishing 0.74±0.09, and worm 0.64±0.11.
- **Tool misuse:** Ideal sends to all contacts at 0.47±0.19 and includes phishing at 0.44±0.18. Query+ has R@5=1, similarity 0.78, sent 0.64±0.13, and phishing 0.63±0.13. CEM has R@5=1, similarity 0.83, and 0.58±0.18 for both. Fusion has R@5=1, similarity 0.87, and 0.84±0.05 for both.
- **Single-agent code execution:** Ideal ASR is 0.04±0.05. Query+ has R@5=1, similarity 0.73, and ASR 0.18±0.08. CEM has R@5=1, similarity 0.79, and ASR **0.26±0.09**. Fusion has R@5=1, similarity 0.85, and ASR 0.22±0.04.
- **Multi-agent code execution:** Ideal ASR is 0.54±0.23. Query+ has R@5=1, similarity 0.75, and ASR 0.56±0.21. CEM has R@5=1, similarity 0.78, and ASR 0.42±0.08. Fusion has R@5=1, similarity 0.83, and ASR 0.36±0.09.

The table’s formatting is compact, but these values follow its displayed column groupings and the accompanying interpretation.

### 4.11 Model and orchestration effects

GPT-4o is more conservative than GPT-4o-mini around conspicuously harmful instructions such as worms and Python payloads. This reduces GPT-4o’s single-agent worm and code-execution success. However, GPT-4o is more willing to complete routine email workflows, producing higher tool-misuse success.

This single-agent caution does not carry over to multi-agent workflows. GPT-4o’s code-execution ASR rises from only 2–4% in the single-agent setting to 72% with CEM and 80% with Fusion in the multi-agent system—roughly a 40-fold increase. Eight of ten Fusion runs exfiltrate a private file.

The authors attribute this amplification to divided context: the code-execution agent receives Python from an apparently trusted teammate but may not see either the original query or malicious source. It is therefore more likely to execute the code as a legitimate delegated task. GPT-4o-mini has lower multi-agent ASR than GPT-4o, which the authors attribute to less consistent instruction following.

The “ideal” assumption can either underestimate or overestimate realistic risk. For example, the ideal single-agent code-execution ASR is only 2% for GPT-4o and 4% for GPT-4o-mini, whereas realistic CEM retrieval reaches 26% on GPT-4o-mini. In the multi-agent GPT-4o experiment, the ideal baseline reaches 58%, while Fusion reaches 80%.

### 4.12 Defense evaluation

The paper tests three retrieval-stage defenses.

#### Query paraphrasing

Changing the wording of user queries reduces Recall@5 by less than 10% on most datasets. If the attacker optimizes jointly over multiple paraphrases, performance fully recovers and sometimes exceeds the original baseline. Paraphrasing therefore offers little durable protection.

#### Perplexity filtering

Optimized malicious text initially has higher perplexity than clean content, suggesting it might look less natural. However, simply repeating the malicious text lowers perplexity while preserving attack effectiveness. The paper states that adaptive repetition can make perplexity lower than that of clean documents. Figure 12 is referenced for this result, but it was not provided, so its dataset-level values cannot be summarized.

#### Token masking

Randomly masking tokens has little effect as the trigger grows longer, because eliminating enough useful tokens becomes unlikely. Partial deletion is also insufficient: Figure 2 shows that as few as five optimized tokens can already produce high recall. Identifying the trigger tokens is difficult because they may occur anywhere and can look harmless; the most common FiQA trigger token is reported as “business.” Token masking is consequently ineffective.

Position-based defenses are also considered unsuitable because most triggers are position-agnostic. Defenses requiring model fine-tuning, such as SecAlign, DataSentinel, and StruQ, are outside the study’s closed-source-model scope.

## 5. Analysis and Interpretation

The findings answer the central question affirmatively: realistic IPI attacks can succeed, but only if the retrieval barrier is overcome.

The authors interpret the results as evidence that retrieval is the system-wide failure point:

- Unoptimized malicious instructions are effectively harmless in these experiments because they are not retrieved.
- A short optimized trigger converts the same attack fragment into one of the most relevant items for a natural query.
- Once retrieved, the malicious document frequently overrides RAG answers and can cause agents to send messages, propagate phishing, misuse tools, or execute code.
- Model scale and stronger embedding quality do not reliably confer security.
- The danger comes from semantic-vector manipulation rather than from corpus size or query modality.
- The strength of competing benign documents is the main factor that determines attack difficulty.

The trigger/attack decomposition also explains transferability. A trigger is optimized to move an entire document’s embedding toward the query. Its effect is often reusable across payloads and positions because many embedding models pool token information globally. Cross-model transfer is weaker when architectures differ, particularly for OpenAI’s more location-sensitive embeddings.

The downstream results show that component-level safety does not guarantee system-level safety. GPT-4o resists direct-looking code in a single-agent context, yet becomes more vulnerable when a teammate agent passes the same code as a delegated task. The authors therefore argue that evaluating prompts “already in context,” or testing an isolated model, can substantially misstate the risk of a complete retrieval-and-tool-use pipeline.

The work also distinguishes itself from narrower RAG knowledge poisoning. Knowledge poisoning primarily corrupts answers in a single-model setting. The general IPI framework can additionally redirect tool calls, spread self-replicating instructions, and cause multi-agent code execution.

The ethical discussion identifies three stakeholder groups:

- Researchers gain a realistic basis for studying retrieval-stage security.
- Developers need principled retrieval-aware defenses rather than ad hoc filters.
- Users face harms such as phishing sent to their contacts or exposure of SSH keys.

The study used public benchmarks and controlled Enron-based experiments rather than probing live deployments or using private user data. The authors caution that the method might also manipulate other embedding-based search or recommendation systems. They also warn that progress on IPI should not be portrayed as resolving broader LLM harms, including environmental, cognitive, and intellectual-property concerns.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It provides the first reported end-to-end IPI evaluation under natural queries and realistic retrieval corpora across RAG, single-agent, and multi-agent systems.
- It identifies retrieval—not merely malicious instruction design—as the decisive bottleneck.
- It formally decomposes poisoned content into a reusable retrieval-oriented **trigger fragment** and an arbitrary objective-oriented **attack fragment**.
- It adapts CEM into a practical black-box prefix-optimization method requiring only embedding API access.
- It supplies a theoretical \((\varepsilon,\delta)\)-utility result under a position-wise linear scoring assumption.
- It evaluates one-item poisoning across 11 retrieval datasets and eight embedding models, including commercial services.
- It demonstrates near-perfect retrieval using approximately ten tokens, with average Recall@5 of 94.1% in Table 3.
- It shows that the attack is inexpensive—as little as $0.21 per target query—and computationally practical.
- It establishes partial transfer across payloads, token locations, and some model families.
- It demonstrates severe downstream effects, including up to 80% GPT-4o SSH-key exfiltration in a multi-agent workflow without further user interaction.
- It shows that query paraphrasing, perplexity filtering, and token masking fail under adaptive attacks.
- It extends the evidence beyond text-to-text retrieval through a reported MS COCO/OpenCLIP image-to-text experiment.
- It releases source code and evaluation scripts through the stated Zenodo repository for controlled defensive testing.

The authors explicitly do not claim to have invented CEM itself; their novelty lies in adapting the established method to realistic IPI retrieval.

## 7. Limitations and Caveats

- The evaluation is restricted to **embedding-based retrieval**. Hybrid lexical/vector search and reranking systems were not tested.
- Defense evaluation addresses only the retrieval stage. It does not evaluate all defenses that act after malicious content enters the LLM context.
- Fine-tuning-based defenses are outside scope because the study targets closed-source and proprietary models.
- Cross-architecture trigger transfer is inconsistent. Strong attacks may require knowledge or a good guess of the target embedding architecture.
- Most detailed experiments are text-based. The multimodal result is summarized briefly, with fuller results deferred to an unavailable appendix.
- Agentic testing focuses on one Enron email scenario, ten generated FAQs, two base models, and particular AutoGen/Magentic-One configurations. Other agent workflows were not tested.
- Exactly one malicious document is injected per query. This is intentionally stealthy, but it does not describe attacks using multiple coordinated documents.
- The theoretical guarantee assumes a linearly separable score across token positions. Real embedding models are not proven to satisfy that structure exactly.
- The proof of NP-hardness and detailed CEM utility proof are deferred to the full arXiv version and are not present in the supplied material.
- Several appendices and visuals referenced by the paper—such as complete FAQs, raw agent logs, payloads, dataset-level defense results, Figure 12, and fuller multimodal results—were not supplied.
- The experiments use public or synthetic controlled corpora and do not demonstrate compromise of deployed organizations or live infrastructure.
- The paper’s Appendix A.1 prose reports slightly different retrieval averages from Table 3; this internal numerical discrepancy should be kept in mind.
- The work focuses on retrieving already-designed attack fragments and does not study the construction or inherent strength of those payloads.
- The authors caution that the attack technique could potentially be misused to manipulate embedding-based search and recommendation systems outside LLM agents.

## 8. Future Work or Open Questions

The paper identifies several unresolved directions:

- Evaluate the attack against hybrid retrieval systems and rerankers.
- Improve transfer between embedding models with different architectures.
- Develop defenses that remain effective after the attacker adapts, rather than relying on paraphrasing, perplexity, masking, or token position.
- Secure both retrieval and downstream system components instead of treating them independently.
- Extend end-to-end testing beyond the studied email workflow to other agentic applications.
- Investigate broader multimodal retrieval risks beyond the reported MS COCO/OpenCLIP experiment.
- Determine how to protect multi-agent systems when agents receive narrow, delegated context and trust outputs from other agents.
- Study whether theoretical insights from trigger optimization can support stronger retrieval-aware mitigation.
- Consider analogous manipulation risks in other embedding-dependent search and recommendation systems.

## 9. High-Level Takeaway (Plain Language)

A malicious instruction hidden in a document or email usually cannot hurt an AI assistant if the system never retrieves it. This paper shows that an attacker can add a very short, automatically optimized sequence of words or tokens that makes one poisoned item look highly relevant to an ordinary user question. Across many datasets and embedding systems, ten such tokens put the poisoned item into the top five results about 94% of the time.

Once retrieved, the item can force wrong answers, spread phishing messages, misuse tools, or induce code execution. In the most severe reported experiment, one poisoned email led a GPT-4o multi-agent workflow to exfiltrate SSH keys in 80% of trials. Simple defenses did not hold up after adaptation. The central message is that securing the LLM alone is insufficient: systems must protect the retrieval step and the full chain of agents and tools that follows it.