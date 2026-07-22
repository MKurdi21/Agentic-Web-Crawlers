# Prompt Injection Attack to Tool Selection in LLM Agents

**Authors:** Jiawen Shi, Zenghui Yuan, Guiyao Tie, Pan Zhou, Neil Zhenqiang Gong, and Lichao Sun  
**Venue:** Network and Distributed System Security Symposium (NDSS) 2026

## 1. Background and Context

Large language model agents do more than generate text: they can plan tasks, choose external tools, and call those tools to act in external environments. Such agents are used for web interaction, software development, API access, and other complex tasks.

Tool selection is especially important because choosing the wrong tool can directly affect an agent’s behavior and safety. The paper studies a common two-stage selection pipeline:

1. **Retrieval:** A retriever compares a user’s task with tool documents and returns the top \(k\) candidates.
2. **Selection:** An LLM reads the task and retrieved tool documents, then chooses one tool to execute.

A tool document normally contains a tool’s name, description, API specifications, functionality, invocation method, and parameters. Retrieval commonly uses two encoders: one maps the task description to an embedding, and another maps each tool document to an embedding. Cosine similarity or dot product is then used to rank the tools. During selection, the LLM receives a structured prompt containing the user query and the names and descriptions of the retrieved tools, surrounded by header and trailer instructions.

This architecture creates a security problem because tool documents may come from untrusted external sources or third-party tool hubs. A malicious developer could publish a tool whose description contains language designed to manipulate the LLM. If the agent selects and immediately executes that tool without further verification, the tool could cause unauthorized data access, privacy breaches, or other harmful behavior.

Earlier prompt-injection attacks fall into two broad groups:

- **Manual attacks:** naive instructions, escape characters, context-ignoring text, fake completions, and combinations of these techniques.
- **Automated attacks:** optimization-based methods such as JudgeDeceiver and PoisonedRAG.

The authors argue that these approaches are not well suited to end-to-end tool selection. Manual attacks and JudgeDeceiver mainly manipulate the final LLM selection stage and may never be retrieved. PoisonedRAG considers retrieval, but it targets answer generation in retrieval-augmented generation and typically injects multiple entries optimized for one query. Tool selection requires one malicious document to survive retrieval and then defeat competing legitimate tools during selection.

**Figure 1** illustrates this distinction. Without an attack, a Father’s Day gift query retrieves ordinary tools such as `GiftTool`, `ProductSearch`, and `ProductComparison`, and the LLM selects `ProductSearch`. Under attack, the library contains a malicious `GiftAdvisorPro` document. Its description appears relevant to personalized gifts, reviews, comparisons, quality, and cost, while also steering the model to prefer that tool. It is retrieved and then selected instead of the benign alternatives.

**Figure 2** shows the selection prompt. The LLM is told to choose exactly one of the retrieved tools and return only its name in parseable JSON. The attack therefore has to make the malicious tool win within this constrained, structured prompt.

## 2. Research Goal and Objectives

The paper introduces **ToolHijacker**, described as the first prompt-injection attack designed specifically to manipulate tool selection in LLM agents under a **no-box** threat model.

Its main objective is to generate one malicious tool document that:

- Is retrieved for many semantically different descriptions of an attacker-chosen target task.
- Is selected by the LLM over legitimate tools after retrieval.
- Transfers to unknown retrievers, LLMs, task phrasings, tool libraries, and top-\(k\) settings.
- Has little effect on unrelated tasks, making the attack targeted.
- Remains effective against existing prevention and detection defenses.

The paper also investigates:

- Gradient-free and gradient-based ways to construct the document.
- Transfer across eight target LLMs and four retrievers.
- Sensitivity to optimization parameters, tool-library size, and the number of malicious documents.
- Whether humans or automated defenses can recognize the malicious descriptions.

## 3. Methods (Approach/Design)

### Threat model

The attacker knows the general target task but does not know the actual user phrasings. If the target is weather information, for example, unknown users might ask “What is the weather today?”, “How is tomorrow’s weather?”, or “Will it rain later?”

The attacker cannot:

- Inspect the target tool library.
- Learn the target value of \(k\) or see the retrieved top-\(k\) tools.
- Access the target retriever or target LLM parameters.
- Query the target retriever or target LLM directly.

The attacker can:

- Use an accessible LLM to create a disjoint set of shadow task descriptions.
- Create a shadow tool library containing relevant and irrelevant tools.
- Operate a shadow retriever and shadow LLM.
- Follow standardized tool-document templates.
- Publish a malicious tool through a third-party tool platform.

The true and shadow task-description sets do not overlap.

### ToolHijacker’s two-part malicious description

A malicious tool document contains a manually chosen, semantically meaningful tool name and an optimized description. Because tool names contain relatively few tokens, optimization focuses on the description.

The description is split into two concatenated subsequences:

- **\(R\): retrieval component.** Makes the document semantically similar to many descriptions of the target task, increasing its chance of appearing in the retrieved top-\(k\).
- **\(S\): selection component.** Makes the LLM choose the malicious tool once it appears among the candidates.

The complete malicious description is \(R \oplus S\). This decomposition mirrors the retrieval–selection architecture and turns one difficult discrete, discontinuous, non-differentiable optimization problem into two coordinated subproblems.

The overall attack objective is the fraction of shadow task descriptions for which the shadow pipeline retrieves and selects the malicious tool.

### Constructing the shadow environment

An accessible LLM generates:

- A shadow task set \(Q'\), containing varied but realistic formulations of the target task.
- A shadow tool set \(D'\), containing task-relevant and task-irrelevant documents.

**Figure 10** gives the task-generation prompt. It asks for realistic queries that:

- Directly match the target task.
- Span simple, moderate, and complex requests.
- Use varied sentence structures.
- Cover different contexts, use cases, and user backgrounds.
- Reflect practical real-world requests.

**Figure 11** gives the shadow-tool-generation prompt. It asks for JSON-formatted tool entries with names and descriptions, emphasizing general functionality across multiple related queries and varying description lengths.

GPT-3.5-turbo was used to generate these shadow tasks and tools.

### Optimizing \(R\) for retrieval

#### Gradient-free method

An LLM synthesizes a general functional description by extracting the common capabilities implied by the shadow task descriptions. The reasoning is that task requests and descriptions of tools capable of fulfilling them naturally share semantic content.

The prompt asks for a general functionality description applicable across the supplied shadow queries, constrained to an approximate word count.

#### Gradient-based method

The method maximizes the average similarity between the malicious description and all shadow tasks under the shadow retriever. It begins with the gradient-free \(R\), then uses HotFlip for token-level adversarial optimization.

The paper expects transfer because different retrieval models learn overlapping semantic patterns.

### Optimizing \(S\) for selection

For every shadow task, the researchers create a candidate set containing the malicious tool plus \(k'-1\) shadow tools. They optimize \(S\) so that the shadow LLM chooses the malicious tool across all task–candidate-set pairs.

#### Gradient-free method

This method uses an attacker LLM and a shadow LLM in a tree-search process:

1. Start with an initial \(S\).
2. The attacker LLM generates \(B\) variants of each current candidate.
3. The shadow LLM tests every variant against every shadow task and associated candidate set.
4. A regularized matching procedure counts how often the malicious tool is selected.
5. If a variant succeeds for all shadow tasks, optimization stops.
6. Otherwise, retain the top \(W\) variants, provide their results as feedback, and continue.
7. Iterate up to \(T_{\text{iter}}\) times per shadow task.

This resembles a tree-of-attacks search, with pruning to control the search width.

#### Gradient-based method

This method uses the shadow LLM’s gradients to maximize the probability of generating the malicious tool name. Its loss has three parts:

- **Alignment loss \(L_1\):** raises the probability of the complete desired output.
- **Consistency loss \(L_2\):** specifically reinforces generation of the malicious tool name.
- **Perplexity loss \(L_3\):** encourages readable, coherent language by penalizing improbable token sequences.

The total loss is \(L_1+\alpha L_2+\beta L_3\), summed across shadow task–retrieval pairs.

Optimization follows JudgeDeceiver’s position-adaptive and step-wise strategies:

- The malicious document is tested at different positions in the retrieved list.
- Task–retrieval pairs are progressively added rather than optimized simultaneously, improving stability.

### Initial sequences

**Figure 12** shows an example for a MetaTool space-image task:

- Initial \(R\): a natural description providing access to space-related images for educational and creative projects.
- Gradient-free initial \(S\): an instruction to output `SpaceImageLocator`.
- Gradient-based initial \(S\): repeated “Correct” tokens followed by the same output instruction.

### Datasets and task construction

Two benchmarks were used:

- **MetaTool:** 21,127 instances and 199 benign tool documents sourced from OpenAI Plugins.
- **ToolBench:** 126,486 instruction-tuning samples and 16,464 RapidAPI tool documents. After removing duplicates and empty descriptions, 9,650 benign documents remained.

For each dataset, the researchers designed 10 diverse, real-world target tasks. Each task had 100 target descriptions produced through LLM-based generation and human evaluation, yielding 1,000 target descriptions per dataset.

### Models and retrievers

Eight target LLMs were evaluated:

- Llama-2-7B-chat
- Llama-3-8B-Instruct
- Llama-3-70B-Instruct
- Llama-3.3-70B-Instruct
- Claude-3-Haiku
- Claude-3.5-Sonnet
- GPT-3.5
- GPT-4o

Four target retrievers were tested:

- text-embedding-ada-002
- Contriever
- Contriever-ms, fine-tuned on MS MARCO
- Sentence-BERT-tb, fine-tuned on ToolBench

### Default attack settings

Each malicious document was optimized using:

- Five shadow task descriptions: \(m'=5\).
- Four shadow benign documents per candidate set.
- Shadow retrieval depth \(k'=5\).

For the gradient-free attack:

- Llama-3.3-70B served as attacker and shadow LLM.
- \(T_{\text{iter}}=10\), \(B=2\), and \(W=10\).

For the gradient-based attack:

- Contriever was the shadow retriever.
- Llama-3-8B was the shadow LLM.
- \(\alpha=2.0\), \(\beta=0.1\).
- \(R\) was optimized for 3 iterations and \(S\) for 400 iterations.

Unless otherwise stated, ablations used MetaTool task 1, GPT-4o, and text-embedding-ada-002.

### Baselines

Seven attacks were compared:

- Naive instruction.
- Escape-character separation.
- Context-ignoring instruction.
- Fake completion.
- Combined manual attack.
- JudgeDeceiver.
- PoisonedRAG.

### Metrics

- **Accuracy (ACC):** probability of selecting the correct legitimate tool without attack.
- **Attack success rate (ASR):** probability of selecting the malicious tool after injection.
- **Hit rate (HR):** fraction of tasks for which at least one correct legitimate tool appears in the top-\(k\).
- **Attack hit rate (AHR):** fraction for which the malicious document appears in the top-\(k\).

ACC and ASR evaluate the complete pipeline; HR and AHR isolate retrieval. The default was \(k=5\).

## 4. Results and Findings

### Attack success across models and datasets

**Table I** reports average results across 10 target tasks.

| Dataset and metric | Llama-2 7B | Llama-3 8B | Llama-3 70B | Llama-3.3 70B | Claude-3 Haiku | Claude-3.5 Sonnet | GPT-3.5 | GPT-4o |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MetaTool, no-attack ACC | 96.7% | 98.9% | 98.2% | 99.6% | 99.2% | 98.9% | 98.8% | 99.6% |
| MetaTool, gradient-free ASR | 98.2% | 94.0% | 97.0% | 99.6% | 85.4% | 92.1% | 91.0% | 96.7% |
| MetaTool, gradient-based ASR | 99.8% | 100% | 97.2% | 99.4% | 82.6% | 92.0% | 92.8% | 92.2% |
| ToolBench, no-attack ACC | 97.1% | 90.5% | 97.2% | 97.2% | 97.2% | 97.8% | 97.3% | 98.4% |
| ToolBench, gradient-free ASR | 91.7% | 80.6% | 82.1% | 90.8% | 82.8% | 93.6% | 77.7% | 88.2% |
| ToolBench, gradient-based ASR | 95.2% | 96.6% | 89.2% | 94.8% | 74.3% | 85.2% | 84.6% | 83.9% |

The attacks transferred even when shadow and target models had different architectures. With Llama-3.3-70B as the shadow LLM and GPT-4o as the target, the gradient-free attack reached 96.7% ASR on MetaTool and 88.2% on ToolBench.

The gradient-free version generally did better on closed-source models; the gradient-based version often performed better on open-source models. Examples include:

- Gradient-free was 4.5 percentage points higher than gradient-based on GPT-4o/MetaTool.
- Gradient-free was 8.4 points higher on Claude-3.5-Sonnet/ToolBench.
- Gradient-based was 16 points higher on Llama-3-8B/ToolBench.

Claude-3-Haiku was the least sensitive model, but the lowest reported ASR was still 74.3% in the main table.

### Retrieval success

**Table II** shows:

- MetaTool: ordinary HR was 100%; gradient-free AHR was 99.9%; gradient-based AHR was 100%.
- ToolBench: ordinary HR was 100%; gradient-free AHR was 96.1%; gradient-based AHR was 97.8%.

Thus, one malicious document was retrieved in more than 96% of ToolBench cases despite competing with 9,650 benign documents.

**Figure 3** presents radar plots over the 10 target tasks in both datasets. Both attacks have high AHR and ASR across tasks rather than succeeding only on a small subset. The exact task-by-task values are not labeled clearly enough to enumerate, but the plots support the reported cross-task consistency.

### Comparison with other attacks

**Table III** reports GPT-4o ASRs:

| Attack | MetaTool | ToolBench |
|---|---:|---:|
| Naive | 6.0% | 24.8% |
| Escape characters | 28.2% | 24.6% |
| Context ignore | 1.2% | 11.3% |
| Fake completion | 14.5% | 23.0% |
| Combined attack | 9.7% | 11.7% |
| JudgeDeceiver | 30.2% | 26.4% |
| PoisonedRAG | 39.3% | 58.3% |
| ToolHijacker gradient-free | 96.7% | 88.2% |
| ToolHijacker gradient-based | 92.2% | 83.9% |

Manual attacks often failed because irrelevant or conspicuous instructions had low retrieval relevance. JudgeDeceiver optimized selection but did not adequately solve retrieval. PoisonedRAG was the strongest baseline, but it optimized for one task description rather than multiple semantic formulations.

**Figure 4** plots document token lengths on a logarithmic axis. Benign and malicious documents vary substantially, but ToolHijacker’s documents occupy length ranges overlapping normal documents. Token length alone therefore does not distinguish them. The figure does not provide exact numeric summaries for each category.

### Retriever transfer

**Table IV** shows that the gradient-free attack achieved 100% AHR and 99% ASR with every retriever.

For the gradient-based attack:

- text-embedding-ada-002: 100% AHR, 95% ASR.
- Contriever: 100% AHR, 100% ASR.
- Contriever-ms: 100% AHR, 100% ASR.
- Sentence-BERT-tb: 100% AHR, 100% ASR.
- Average: 100% AHR and 98.75% ASR.

The paper attributes the slightly lower ASR on text-embedding-ada-002 to stronger retrieval ranking: the malicious document was retrieved but sometimes ranked lower, making final selection less likely.

### Effect of target and shadow top-\(k\)

**Figure 5** varies target \(k\) from 1 to 10 and shadow \(k'\) over 2, 3, 5, and 7.

Under the default configuration:

- At \(k=1\), gradient-free AHR and ASR were both 89%.
- Once \(k>3\), AHR stabilized at 100% for both attacks.
- Gradient-free ASR stabilized near 99%.
- Gradient-based ASR fluctuated around 96%.

With small \(k'\), performance was less stable. At \(k'=2\):

- Gradient-based AHR increased from 74% at \(k=1\) to 99% at \(k=3\).
- As target \(k\) increased, ASR fell by about 16 points for gradient-free and 50 points for gradient-based.

The dataset has five ground-truth tools. When \(k'<5\), optimization sees too few competitors; increasing target \(k\) then introduces more legitimate tools and can reduce malicious selection. At \(k'\ge5\), performance improves and stabilizes.

### Number of shadow task descriptions

**Figure 6** varies \(m'\) from 1 to 10:

- AHR remained 100% for both attacks.
- Gradient-based ASR rose from 32% with one shadow description to 98% with seven.
- Gradient-free ASR remained at least 92% even with only one.

Multiple paraphrases mainly improve robustness during the LLM selection phase.

### Contributions of \(R\) and \(S\)

**Table V** confirms that both components are necessary:

| Attack | Description | AHR | ASR |
|---|---|---:|---:|
| Gradient-free | \(R\oplus S\) | 100% | 99% |
| Gradient-free | \(R\) only | 100% | 5% |
| Gradient-free | \(S\) only | 65% | 63% |
| Gradient-based | \(R\oplus S\) | 100% | 95% |
| Gradient-based | \(R\) only | 100% | 0% |
| Gradient-based | \(S\) only | 99% | 16% |

Removing \(R\) badly harmed gradient-free retrieval. Removing \(S\) almost eliminated final selection. Gradient-based \(S\) retained 99% AHR because token-level optimization caused it to include target-task information, but its ASR was only 16%.

### Choice of shadow LLM

**Table VI** evaluates eight shadow LLMs for the gradient-free attack.

Average ASRs ranged from:

- 94.75% with Llama-3-70B,
- 95.13% with Llama-2-7B,
- 95.25% with Llama-3-8B,
- 97.25% with Llama-3.3-70B or Claude-3-Haiku,
- 97.38% with GPT-3.5,
- 97.75% with GPT-4o,
- to 99.50% with Claude-3.5-Sonnet.

Claude-3.5-Sonnet improved average ASR by 4.37 points over Llama-2-7B. Cross-model transfer was usually very high. The lowest gradient-free entry was 70% when Llama-2-7B optimized an attack tested against Claude-3-Haiku.

**Table VII** compares two shadow LLMs for the gradient-based attack:

- Llama-2-7B average ASR: 81.38%.
- Llama-3-8B average ASR: 96.50%.

The improvement was 15.12 points. With Llama-2-7B, target-specific values ranged from 34% on Llama-3-70B to 100% on Llama-2-7B and Llama-3-8B. With Llama-3-8B, values ranged from 82% on GPT-3.5 to 100% on the four Llama targets.

Gradient-free optimization was therefore less sensitive to the shadow model.

### Similarity metric

**Table VIII** finds no effect on retrieval:

- Both cosine similarity and dot product produced 100% AHR.
- Gradient-free ASR was 99% with either metric.
- Gradient-based ASR rose from 95% with cosine similarity to 97% with dot product.

### Multiple malicious tools

**Figure 7** compares one malicious document with two documents under \(k'=2\):

- In the **individual** condition, each document promoted itself.
- In the **unified** condition, both promoted the same malicious tool.

The individual condition followed the same shape as the one-document condition but improved ASR. At \(k=5\), both attack types gained 24 percentage points. In the unified condition, AHR and ASR stayed close to 100% as \(k\) increased. Multiple documents therefore compensate when the shadow candidate set is too small.

### Impact on unrelated tasks

**Table XII** evaluates a malicious document optimized for one target task on 900 descriptions of nine other tasks:

| Attack | Target AHR | Target ASR | Non-target AHR | Non-target ASR |
|---|---:|---:|---:|---:|
| Gradient-free | 100% | 99% | 0.22% | 0% |
| Gradient-based | 100% | 95% | 4% | 0.11% |

The attack was highly targeted and had minimal measured effect on unrelated tool-selection utility.

### Attacker LLM in gradient-free optimization

**Table XIII** shows average ASRs for eight attacker LLMs:

- Llama-2-7B: 69.00%.
- Llama-3-8B: 95.63%.
- Llama-3-70B: 97.13%.
- Llama-3.3-70B: 97.25%.
- Claude-3-Haiku: 92.88%.
- Claude-3.5-Sonnet: 93.00%.
- GPT-3.5: 94.38%.
- GPT-4o: 99.00%.

More capable attacker models generally generated stronger \(S\). Claude-generated sequences transferred at 100% to most other target models but achieved only 43% or 44% against Claude-3-Haiku. The authors associate this with Claude-3-Haiku’s stronger resistance.

### Number of generated variants

**Table XIV** varies \(B\):

| \(B\) | AHR | ASR | Total queries |
|---:|---:|---:|---:|
| 1 | 100% | 100% | 30 |
| 2 | 100% | 99% | 12 |
| 3 | 100% | 100% | 18 |
| 4 | 100% | 100% | 24 |
| 5 | 100% | 100% | 30 |

Every setting was effective. \(B=1\) needed more iterations, while large \(B\) generated more candidates that each had to be checked against all shadow tasks. The default \(B=2\) required the fewest queries in this experiment.

### Hyperparameters and loss ablation

**Figure 9** varies \(\alpha\) and \(\beta\):

- AHR stayed around 100%, with a small decrease when \(\alpha\) reached 10.
- ASR first rose and then fell as either parameter increased.
- ASR remained above 95% as \(\alpha\) moved from 1 to 2.
- ASR remained above 95% for \(\beta\) from 0.1 to 1.

**Table XV** removes one loss at a time:

| Loss setting | AHR | ASR |
|---|---:|---:|
| Without alignment loss \(L_1\) | 100% | 54% |
| Without consistency loss \(L_2\) | 100% | 56% |
| Without perplexity loss \(L_3\) | 100% | 5% |
| Full loss | 100% | 95% |

Every loss contributed at least 39 ASR points. Perplexity loss was most important: without it, \(S\) became unnatural or nonsensical and was less likely to manipulate the target LLM.

### Dynamic tool libraries

**Table XVI** tests growing libraries.

For MetaTool:

| Number of tools | Gradient-free AHR/ASR | Gradient-based AHR/ASR |
|---:|---:|---:|
| 50 | 100% / 98.8% | 100% / 98.0% |
| 100 | 100% / 98.0% | 100% / 95.1% |
| 150 | 100% / 96.7% | 100% / 93.3% |

For ToolBench:

| Number of tools | Gradient-free AHR/ASR | Gradient-based AHR/ASR |
|---:|---:|---:|
| 2,500 | 99.6% / 95.8% | 99.6% / 88.7% |
| 5,000 | 97.5% / 94.9% | 99.0% / 88.4% |
| 7,500 | 97.6% / 92.8% | 98.2% / 84.8% |

Performance declined as libraries grew but remained high, suggesting robustness to library expansion and updates.

### Prevention-based defenses

The study tested:

- **StruQ:** separates secure instructions from user data and trains the model to follow only the secure channel.
- **SecAlign:** fine-tunes on prompt-injected examples paired with secure and insecure responses.

**Table IX** reports ACC under attack, AHR, and ASR:

| Defense | Dataset | Attack | ACC under attack | AHR | ASR |
|---|---|---|---:|---:|---:|
| StruQ | MetaTool | Gradient-free | 0.3% | 99.9% | 99.6% |
| StruQ | MetaTool | Gradient-based | 2.1% | 100% | 97.9% |
| StruQ | ToolBench | Gradient-free | 5.7% | 96.1% | 90.8% |
| StruQ | ToolBench | Gradient-based | 4.1% | 97.8% | 92.1% |
| SecAlign | MetaTool | Gradient-free | 2.5% | 99.9% | 97.5% |
| SecAlign | MetaTool | Gradient-based | 7.4% | 100% | 92.1% |
| SecAlign | ToolBench | Gradient-free | 8.2% | 96.1% | 86.9% |
| SecAlign | ToolBench | Gradient-based | 11.3% | 97.8% | 84.6% |

SecAlign reduced ASR more than StruQ but still left ASRs between 84.6% and 97.5%. The attacks evade these defenses because their descriptions remain relevant and coherent rather than containing conspicuous foreign instructions.

ACC and ASR do not always sum to 100%, because models sometimes refuse or fail to produce a valid answer.

**Figure 8** plots the reduction in ASR relative to undefended models. SecAlign consistently produced larger reductions than StruQ, and reductions were generally larger on ToolBench, suggesting greater defensive benefit with a larger library. The approximate reductions visible in the figure range from around 0–2.5 points for StruQ to roughly 2–9.5 points for SecAlign, depending on dataset and attack type.

### Detection-based defenses

The tested detectors were:

- **Known-answer detection:** prepends an instruction to output “Hello World!”; failure indicates possible injection.
- **DataSentinel:** a game-theoretically fine-tuned extension of known-answer detection.
- **PPL:** flags documents with perplexity above a dataset-adaptive threshold.
- **PPL-W:** applies perplexity detection over sliding windows; window size was 5 for MetaTool and 10 for ToolBench.

Thresholds were calibrated using 100 clean documents so that false positives would remain near a specified limit.

Experiments used 199 MetaTool or 9,650 ToolBench benign documents and 10 injected malicious documents. False negative rate measures malicious documents missed; false positive rate measures benign documents wrongly flagged.

**Table X** shows:

- Known-answer detection had 100% FNR for both attacks on both datasets, with FPR of 0% on MetaTool and 0.01% on ToolBench.
- DataSentinel had 100% FNR for gradient-free attacks. Its listed FPR was 0% on MetaTool and 2.61% on ToolBench.
- For gradient-based attacks, DataSentinel’s FNR was 90% on both datasets.
- Standard PPL had 100% FNR for gradient-free attacks, with FPR of 1.01% on MetaTool and 0.85% on ToolBench. Gradient-based FNR was 80% on MetaTool and 90% on ToolBench.
- PPL-W had 100% FNR for gradient-free attacks, with FPR of 0% on MetaTool and 2.99% on ToolBench. Gradient-based FNR was 50% on MetaTool and 80% on ToolBench.

The table displays FPR once per dataset/detector rather than separately for both attack rows because FPR is evaluated on benign documents.

PPL and PPL-W achieved AUCs of only 0.64 and 0.74. Gradient-based descriptions were somewhat easier to detect because token-level optimization could reduce readability. Gradient-free descriptions preserved sentence-level coherence and were missed entirely in these tests.

### Human detection

**Table XVII** reports a study with six participants. They inspected ToolBench subsets containing 200, 400, or 600 tools, including seven malicious documents.

| Dataset size | Gradient-free FNR/FPR | Gradient-based FNR/FPR |
|---:|---:|---:|
| 200 | 85.71% / 12.44% | 85.71% / 7.77% |
| 400 | 85.71% / 5.60% | 100% / 9.67% |
| 600 | 85.71% / 18.38% | 71.43% / 30.35% |

Participants missed at least 71% of malicious documents while wrongly flagging 5.60–30.35% of benign ones. Human review was therefore unreliable.

### Computational cost

- Gradient-free \(R\): one LLM query.
- Gradient-free \(S\): approximately 18 LLM queries.
- Gradient-based \(R\): approximately one GPU-minute.
- Gradient-based \(S\): approximately eight GPU-hours on one NVIDIA A800 GPU.

## 5. Analysis and Interpretation

The experiments answer the central research question affirmatively: a single optimized tool document can manipulate both stages of an unknown tool-selection pipeline.

The authors attribute transfer across models to shared alignment objectives, similar training practices, and overlapping training data, which can make different LLMs respond similarly to injected language. Retrieval transfer is attributed to semantic features shared across embedding models.

The main reason ToolHijacker outperforms prior attacks is its explicit separation of objectives:

- \(R\) makes the document look like a genuinely useful tool for the target task.
- \(S\) steers the LLM toward the malicious tool after retrieval.

Manual attacks and JudgeDeceiver do not reliably solve retrieval. PoisonedRAG addresses retrieval but is optimized for a different generation problem and typically for one query rather than a set of semantic variants.

The attack’s coherence also explains why defenses fail. Existing detectors often assume prompt injection introduces irrelevant instructions, foreign tasks, unusual token patterns, or high perplexity. ToolHijacker instead aligns the malicious document with the target task and normal tool functionality. The gradient-free version is particularly difficult to identify because it operates at sentence level and produces natural text.

The loss ablation reinforces this interpretation. Retrieval was unaffected by removing individual selection losses, but final ASR collapsed when descriptions became less aligned, less consistent, or less fluent. Surprisingly, readability-related perplexity loss had the largest effect: a semantically awkward adversarial sequence was less successful even when mathematically optimized toward the malicious output.

The attack was also narrowly targeted. Near-zero ASR on unrelated tasks means it can strongly redirect one intended category of requests without broadly disrupting the tool-selection system, potentially making the problem less visible through general utility monitoring.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It introduces **ToolHijacker**, presented as the first prompt-injection attack specifically targeting the complete tool-selection process in LLM agents.
- It formulates malicious tool-document creation as an optimization problem under a restrictive no-box threat model.
- It decomposes the attack into retrieval and selection objectives, implemented through the \(R\) and \(S\) subsequences.
- It develops both gradient-free and gradient-based optimization methods.
- It systematically evaluates transfer across two datasets, eight LLMs, four retrievers, 20 target tasks, and many task phrasings.
- It shows that one malicious tool document can compete successfully in libraries containing thousands of benign tools.
- It provides extensive ablations covering retrieval depth, shadow-task count, shadow and attacker models, similarity metrics, loss functions, multiple malicious tools, dynamic libraries, and optimization cost.
- It evaluates prevention, automated detection, and human detection, finding all insufficient.
- It demonstrates that the attack is targeted and minimally affects unrelated tasks.

## 7. Limitations and Caveats

The paper’s findings should be interpreted within several constraints:

- Experiments were conducted in controlled environments. No real malicious tools were developed or deployed online.
- The attack was evaluated on two tool-selection benchmarks, 20 designed target tasks, eight target LLMs, and four retrievers. This is broad but does not cover every agent architecture or tool ecosystem.
- The work attacks tool selection, not the later tool-calling and execution stages.
- The threat model assumes the attacker can publish a tool that becomes available to the agent and can construct a shadow pipeline.
- The tool name is manually chosen rather than fully optimized.
- Gradient-based optimization is computationally expensive, especially the approximately eight GPU-hours required for \(S\).
- Gradient-based descriptions may become less readable, although perplexity loss reduces this problem.
- Performance can decline with larger tool libraries, small target \(k\), insufficient shadow candidates, weaker shadow models, or more resistant targets such as Claude-3-Haiku.
- Detection experiments injected only 10 malicious documents per dataset.
- The human study involved six participants and seven malicious documents, so it was limited in scale.
- The complete attacker-LLM system prompt, target-task list, and some baseline malicious documents are available only in the separately referenced technical-report appendix, not in the supplied paper pages.
- No statistical significance tests, confidence intervals, or standard deviations are reported; results are percentages over tasks and descriptions.
- The defenses tested were not designed specifically for semantically aligned tool-document attacks, and the results do not establish that every possible defense will fail.

## 8. Future Work or Open Questions

The authors identify two main next steps:

1. Extend the attack surface from tool selection alone to **joint attacks on tool selection and tool calling**.
2. Develop new defenses specifically capable of mitigating ToolHijacker.

The results point to unresolved defensive questions: how to validate third-party tool documents, separate legitimate functionality descriptions from semantically aligned manipulation, verify selected tools before execution, and preserve ordinary tool-selection utility without relying on conspicuous prompt-injection markers.

The authors intend to release code and data only under restricted access. Requesters must disclose their intended use. They also notified OpenAI, Anthropic, and LangChain, although responses were still pending when the paper was written.

All experiments and malicious documents remained local, participants gave informed consent, no harmful content was involved in annotation or the user study, and no personally identifiable information beyond what was necessary was collected.

## 9. High-Level Takeaway (Plain Language)

LLM agents often choose tools by first retrieving a few promising candidates and then asking an LLM to pick one. This paper shows that a malicious developer can write one carefully optimized tool description that looks relevant enough to be retrieved and is persuasive enough to be selected, even without knowing the target agent, retriever, library, user wording, or retrieval settings.

ToolHijacker succeeded at very high rates across many models and libraries, substantially outperforming earlier attacks. Existing fine-tuning defenses, prompt-injection detectors, perplexity checks, and human reviewers missed most malicious documents. The central security lesson is that selecting a tool should not be treated as sufficient evidence that the tool is trustworthy or safe to execute.