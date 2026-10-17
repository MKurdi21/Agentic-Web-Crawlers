## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and the supplied page images. No outside sources, browsing, code execution, OCR tools, or supplementary downloads were used. Statements embedded in the paper's prompts are treated as research evidence, never as instructions to this analyst.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text identifies 18 physical PDF pages. This establishes access to the supplied 18-page document, not to every version or supplement. |
| Text pages accessible | Physical PDF pp. 1–18. |
| Visually inspected pages | pp. 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18: 14 supplied page images. |
| Text-only pages | pp. 4, 13, 14, 15. Their extracted text was inspected; their page layout was not visually inspected. |
| Apparently missing main-document pages | None within the supplied 1–18 sequence. Completeness relative to another paper version is not established. |
| Figures | Figures 1–12 have supplied visual renderings and were inspected. Small plot coordinates do not support exact transcription of every point. |
| Tables | Tables I–XVII are available in text and supplied renderings; their main numerical cells are readable. Table X uses visually shared false-positive-rate cells, requiring care about row alignment. |
| Equations | Equations (1)–(16) are available. Equation (5) is text-only; the other numbered equations have corresponding supplied rendered pages. Some notation and pseudocode are internally inconsistent. |
| Appendices | Appendix A begins on p. 15; Appendix B and Appendix C material appear on pp. 16–18. |
| Supplementary material | Supplementary experiments inside this PDF were supplied and reviewed. The complete appendix of the separately cited technical-report version [35] was not supplied. |
| Referenced but absent material | The attacker LLM's complete system prompt, the detailed target-task list, and baseline malicious-document examples identified as Figure 16 in [35]. Code and data are discussed but were not supplied. |
| OCR | Not performed. Supplied extracted text was sufficient when checked against available images. Garbled plot-label extraction on several pages was resolved only where the supplied image was readable. |
| Other limitations | Small plots permit trends and labeled-axis readings, not reliable exact values for every point. No source-file hash was independently computed; the supplied SHA-256 is preserved as provenance metadata. |

Evidence labels used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No [E] external information is introduced. Confidence is HIGH for clear text and table readings, MEDIUM for qualified methodological interpretation or small-plot trends, and UNKNOWN where required material is absent. Page references always mean physical PDF pages.

## 1. Plain-language orientation

The paper studies how an artificial-intelligence agent chooses a tool. A large language model, or LLM, supplies the language reasoning, but an agent also connects that model to external services. Before calling a service, it may search a library of tool descriptions and ask the LLM which retrieved tool best fits the user's request.

The attack, called **ToolHijacker**, puts a malicious tool description into that library. The description has two jobs: make the tool look relevant enough to be retrieved, and influence the LLM to choose it. The researchers optimize these jobs separately and concatenate the resulting text. They study both a method that uses only outputs from accessible models and a method that uses gradients from accessible substitute models. Neither method requires querying the actual target system under the stated threat model. [A; pp. 1–7]

The main findings are high rates of malicious-tool selection across two benchmark tool libraries, eight target LLMs, and several retrieval models. For GPT-4o, the gradient-free method reports attack success rates of 96.7% on MetaTool and 88.2% on ToolBench; the gradient-based method reports 92.2% and 83.9%. These are tool-selection outcomes averaged over ten target tasks per dataset, not measured rates of data theft or harmful tool execution. [A; Table I, p. 7; p. 8]

The central contribution is an automated attack designed for the **entire retrieval-and-selection pipeline** rather than just the final LLM decision. Its empirical contribution includes transfer experiments, component ablations, and tests of six defenses. The supplied results show substantial residual vulnerability under the tested defenses, with important qualifications and several reporting inconsistencies described below.

For the user's research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper provides mechanism-level evidence about an additional external-input and action-selection surface. It does **not** directly compare a web agent with a standalone LLM, and it does not establish a quantitative vulnerability gap between them. That relevance is an analyst inference, not the paper's experimental finding.

## 2. Document roadmap

The original title is **Prompt Injection Attack to Tool Selection in LLM Agents**. The authors are Jiawen Shi, Zenghui Yuan, Guiyao Tie, Pan Zhou, Neil Zhenqiang Gong, and Lichao Sun. The affiliations are Huazhong University of Science and Technology, Duke University, and Lehigh University. The first page identifies the Network and Distributed System Security Symposium, NDSS 2026, February 23–27, San Diego, and DOI 10.14722/ndss.2026.230675. These are supplied publication details, not externally verified facts. [A; p. 1]

This is a mixed cybersecurity, algorithm, and empirical machine-learning paper. It introduces an attack, formalizes its objective, gives optimization procedures, and evaluates attacks and defenses. It is not a systematic review, dataset paper, or theorem-and-proof paper.

| Inventory ID | Original component | Location and role |
|---|---|---|
| S0 | Abstract | p. 1; problem, proposed attack, results, defenses. |
| S1 | I. Introduction | pp. 1–2; motivation, prior-method gap, contributions. |
| S2 | II. Problem Formulation | pp. 3–4; tool-selection model and threat model. |
| S3 | III. ToolHijacker | pp. 4–6; overview, optimization objective, retrieval and selection optimization. |
| S4 | IV. Evaluation | pp. 6–11; setup, main results, ablations. |
| S5 | V. Defenses | pp. 11–12; prevention and detection experiments. |
| S6 | VI. Related Work | pp. 12–13; tool selection, attacks, defenses. |
| S7 | VII. Conclusion and Future Work | pp. 13–14; findings and proposed extensions. |
| S8 | Ethics Considerations | p. 14; controlled experiments, access plans, participant consent. |
| S9 | References | pp. 14–15; 75 numbered entries. |
| A1 | Appendix A. List of Symbols | pp. 15–16; Table XI. |
| A2 | Appendix B. Supplementary Experimental Results | pp. 16–17; utility, attacker models, branching, losses, library size, humans, cost. |
| A3 | Appendix C. Details of Prompts and Datasets | pp. 17–18; generation templates and initialization. |

Visual inventory: Figures F1–F12 correspond to original Figures 1–12. Tables T1–T17 correspond to original Tables I–XVII. ALG1 is Algorithm 1. E1–E16 correspond to Equations (1)–(16). There are no supplied theorems, lemmas, propositions, formal hypothesis tests, or separately numbered research questions. The experiment register below distinguishes the substantive studies rather than merging them into a single result.

The paper moves from system definition to attack construction, then to effectiveness, transfer, ablation, and defense testing. The appendices materially qualify the main findings, particularly target specificity, human detection, computation cost, and the dynamic-library results.

## 3. Background and context

**Tool selection** is choosing an external function or service suitable for a user's request. **Tool calling** is subsequently invoking that service. The paper separates task planning, tool selection, and tool calling; its measured attack centers on selection. [A; p. 1]

A **tool document** describes a tool's name, functionality, invocation methods, parameters, and application programming interface, or API. Although the general system includes API specifications, this attack concentrates on the name and description because the authors say these primarily drive selection. The name is manually chosen, while most optimization concerns the description. [A; pp. 3–4]

A **retriever** shortlists likely relevant documents. Here, a dual encoder maps the request and documents to numerical vectors called embeddings. A similarity function ranks them, and **top-k** means the k highest-ranked documents. The LLM then sees the request and that shortlist in a structured prompt and returns the selected tool name. [A; p. 3]

**Prompt injection** means instructions placed in external data attempt to redirect the LLM away from its intended instructions. The crucial distinction in this paper is that a description ostensibly serving as evidence about a tool can also contain text influencing which tool should be selected. Figure 1 visibly combines relevant gift-service language with a preference instruction for the attacker's tool. [A/B; pp. 2–3]

**No-box** is the paper's name for an attacker who cannot inspect the target library, obtain the target retrieval setting or shortlist, inspect target model parameters, or directly query the target retriever or LLM. The attacker can nevertheless build a **shadow pipeline**, meaning a locally accessible substitute system used to develop the attack. No-box therefore does not mean no resources or no knowledge: the attacker knows the target task category and can use substitute models and synthetic documents. [A; pp. 3–4]

**Gradient-free** optimization evaluates or rewrites text without accessing model gradients. **Gradient-based** optimization uses gradients from shadow models to guide changes to discrete tokens. **Transferability** means a document optimized against substitute components remains effective against different target components.

**Retrieval-augmented generation**, or RAG, retrieves external material before generating an answer. PoisonedRAG is a comparison attack originally aimed at this setting. The authors distinguish changing generated answers from changing which external tool an agent selects. Descriptions of cited methods here report the paper's account only; their original publications were not independently examined.

## 4. Research problem and gap

**Existing problem.** An agent's tool-selection prompt includes information originating outside the trusted instruction source. An attacker-controlled document may enter the retrieved shortlist and influence the LLM's choice. The authors connect this to possible harmful execution because their system model assumes selection is followed by execution without further verification. [A; pp. 1, 3]

**Shortcomings of previous approaches according to the authors.** Manual attacks and JudgeDeceiver mainly optimize the selection stage. Instructions that strongly influence an LLM may have insufficient semantic relevance to survive retrieval. PoisonedRAG incorporates retrieval but targets answer generation and, in the authors' comparison, optimizes for a single task description rather than multiple descriptions of the same task. [A; pp. 1, 8]

**Research gap.** The paper seeks an automated, transferable attack on both retrieval and selection under severe restrictions on target access. The attacker needs one document to work across semantically different requests about a chosen task, rather than only one exact prompt. [A; pp. 2, 4]

**Motivation.** Agents increasingly integrate external tools and services, so their action choices depend on externally supplied documentation. The authors argue this can threaten system integrity and user safety. These security consequences motivate the experiment but are not themselves measured as deployed harms. [A; pp. 1, 3, 14]

**Scope.** The evaluated target is a two-stage tool-selection pipeline. The default attack inserts one malicious document per target-task attack into a benign tool library. The paper also tests two malicious documents, alternative retrieval settings, different shadow and target models, and selected defenses. It does not evaluate every agent architecture, a general web-browsing workflow, or a matched standalone-LLM baseline.

## 5. Research questions, objectives, and hypotheses

No explicit numbered research questions or formal statistical hypotheses appear in the supplied document. The following are author-stated objectives or faithful descriptions of the tested objectives, not manufactured quotations of formal research questions:

1. Construct a malicious tool document that is retrieved and selected for varied descriptions of an attacker-chosen task. [pp. 3–5]
2. Develop attacks without access to or direct queries of the target retriever and LLM. [pp. 3–4]
3. Solve the attack through separate retrieval and selection objectives, with gradient-free and gradient-based alternatives. [pp. 4–6]
4. Evaluate effectiveness across datasets, target LLMs, and retrievers, including transfer between different shadow and target models. [pp. 6–10]
5. Determine how attack components and configuration affect effectiveness. [pp. 9–11, 16–17]
6. Assess prevention, automated detection, human detection, target specificity, and optimization cost. [pp. 11–12, 16–17]

The user's broader comparative question is distinct. **[D; HIGH confidence in this boundary]** This work helps explain why adding external tool documentation to an LLM-based system creates another opportunity for attacker influence. It cannot determine how much more vulnerable web agents are than standalone LLMs because that comparison is absent.

## 6. Assumptions / Threat Model

The system consists of a tool library D, a retriever, and a selection LLM E. A request q retrieves D_k, and E chooses a tool from that set. Tool documentation is mixed with a header instruction and a trailer instruction. The intended behavior is exactly one valid tool name in a parsable JavaScript Object Notation, or JSON, response. [A/B; Figure 2 and Equations (1)–(4), p. 3]

The attacker knows the target task, such as a category of requests about weather or space images, but not the actual target descriptions Q. The attacker can generate substitute descriptions Q′ and documents D′, operate a shadow retriever and LLM, and publish a malicious tool through a third-party tool platform. The paper explicitly assumes Q and Q′ do not overlap. It does not supply the complete target descriptions needed to independently inspect that separation. [A; pp. 3–4]

Excluded capabilities are: reading target-library documents, learning k or the actual retrieved shortlist, accessing target-model parameters, and directly querying target retrieval or selection. Public development templates and interface specifications remain available to the attacker. Gradients used by the gradient-based method come from shadow components, so they do not contradict the target-access restriction. [A; p. 4]

The attacker controls a malicious tool's documentation, especially its description. The goal is preferential selection of that tool whenever a user submits one of the target task's descriptions. The experiments measure this selection, not the tool's implementation or its malicious side effects. The ethics statement expressly says no real malicious tools were developed or deployed online. [A; pp. 3, 14]

**[D] Trust-boundary interpretation.** The legitimate instruction tells the model how to select; the external document should describe a candidate. The attack succeeds when candidate content gains influence over the selection policy. The retriever's relevance score is not a security validation step: being semantically relevant makes an attack more likely to be read.

**[D] Environmental qualification.** Publishing a tool is an assumed route to potential integration. The experiments inject documents into controlled libraries; they do not measure the probability that a real platform accepts, distributes, or installs an attacker submission. Actual authorization, tool approval, and execution checks may change the consequence of selection.

## 7. Methodology

### 7.1 Study design and attack architecture

The study constructs an attack on a shadow pipeline and evaluates the optimized document on target pipelines. The overall objective is the average indicator that the shadow LLM selects the malicious tool after retrieval across shadow queries. Because retrieval ranking, discrete text, and the final selection decision make this objective discontinuous and non-differentiable, the authors decompose the description into **R ⊕ S**: R supports retrieval, and S supports selection. The symbol ⊕ means string concatenation. [A; Equation (5), p. 4]

The malicious name is manually crafted for semantic clarity and limited token length. R and S are optimized sequentially, so this is a practical decomposition, not a proof that each component's influence is isolated. Table V shows that S can itself be highly retrievable, especially after gradient-based optimization. [A/B; pp. 4, 9–10]

### 7.2 Shadow data

An accessible LLM produces diverse shadow descriptions of the known target task. Another generation prompt creates shadow tool documents describing relevant functionality; the main method also says D′ contains task-relevant and task-irrelevant documents. Appendix C identifies GPT-3.5-turbo as the generator used with Figures 10 and 11. The complete target-task list and full attacker system prompt are deferred to technical report [35]. [A; pp. 4, 17–18]

The generation templates specify task alignment, varying complexity, contextual diversity, practical requests, variable description lengths, and JSON formatting. Numerical values for all template placeholders, such as maximum words and the approximate length of R, are not given in the supplied material. These prompts document desired generation properties; they do not by themselves establish measured diversity or realism.

### 7.3 Retrieval optimization

The gradient-free R procedure asks an LLM to synthesize a general functionality description that covers the shadow requests. Its rationale is semantic overlap: descriptions of what a tool does should resemble descriptions of tasks the tool can solve. The gradient-based procedure starts from that generated R and uses HotFlip to optimize tokens for average shadow-retriever similarity between shadow queries and R ⊕ S, with S initially fixed. [A; pp. 4–5; Equation (6)]

The authors attribute transfer across retrievers to overlapping learned semantic patterns. This is their explanation; the paper does not separately measure those internal representations or experimentally isolate that explanation from alternative causes.

### 7.4 Selection optimization without gradients

For each shadow request, selection optimization uses k′−1 shadow documents plus the malicious document, making k′ candidates in total. The attacker LLM E_A generates B variants of the current S. The shadow LLM E′ evaluates every candidate variant across the shadow requests. Matching the malicious output increments a success count. A candidate succeeding on all m′ requests terminates the search; otherwise, the highest-scoring candidates survive pruning to width W, and their outputs and scores provide feedback for another generation round. [A; Algorithm 1, pp. 5–6]

The tree's root is the initial S; child nodes are rewrites. The method searches through variations rather than requiring access to target gradients. Its feedback loop is confined to shadow evaluations. Algorithm 1 contains indexing and final-return ambiguities described in Section 14; the prose supplies a clearer conceptual procedure than literal execution of every printed line.

### 7.5 Selection optimization with gradients

The gradient-based method increases the probability that E′ emits the malicious tool's desired output. It optimizes S at token level using three losses: L1 for the full desired response, L2 for the malicious tool name, and L3 for the readability of the injected sequence. The combined loss is L1 + αL2 + βL3. [A; Equations (8)–(14), p. 6]

Position-adaptive optimization changes where the malicious document is placed among shadow candidates. Step-wise optimization progressively adds task–candidate-set pairs instead of optimizing every pair immediately. The authors say this stabilizes optimization. The underlying optimization procedure is adopted from JudgeDeceiver; the supplied text does not expose every implementation detail of that procedure.

### 7.6 Datasets and evaluation sample

| Dataset | Original benchmark description | Evaluated benign library | Evaluation requests |
|---|---|---:|---:|
| MetaTool | 21,127 instances; tool documents from OpenAI Plugins | 199 documents | 10 target tasks × 100 descriptions = 1,000 |
| ToolBench | 126,486 instruction-tuning samples; originally 16,464 tool documents from RapidAPI | 9,650 after duplicate-tool and empty-description removal | 10 target tasks × 100 descriptions = 1,000 |

These benchmark corpus counts must not be mistaken for the number of attack trials. The authors design ten tasks per dataset and generate or evaluate their descriptions using LLM-based and human evaluations. The supplied text does not give detailed annotation criteria, evaluator agreement, exact task lists, benchmark split identifiers, class distributions, or random seeds. The no-overlap statement concerns target versus shadow descriptions, not a fully documented benchmark train/test leakage audit. [A; pp. 4, 6]

### 7.7 Models and parameters

Target LLMs: Llama-2-7B-chat, Llama-3-8B-Instruct, Llama-3-70B-Instruct, Llama-3.3-70B-Instruct, Claude-3-Haiku, Claude-3.5-Sonnet, GPT-3.5, and GPT-4o. Target retrievers: text-embedding-ada-002, Contriever, Contriever-ms, and Sentence-BERT-tb. The latter two are described as fine-tuned on MS MARCO and ToolBench respectively. [A; p. 7]

Default shadow setup uses m′ = 5 queries and k′ = 5 total candidates, comprising four shadow documents and the malicious document. Gradient-free selection uses Llama-3.3-70B as both attacker and shadow LLM, T_iter = 10, B = 2, and W = 10. Gradient-based optimization uses Contriever and Llama-3-8B, α = 2.0, β = 0.1, three R iterations, and 400 S iterations. Default target retrieval is k = 5. Unless otherwise specified, ablations use MetaTool task 1, GPT-4o, and text-embedding-ada-002. [A; pp. 7–8]

Appendix C gives natural-language initial R and S for a space-image task. Both begin with a description of access to space-related images. The gradient-based initial S includes five repetitions of the word Correct before the initial selection instruction. The evidence is an initialization example, not a full optimized-payload listing. [A/B; Figure 12, p. 18]

### 7.8 Metrics, statistics, hardware, and access

ACC is correct selection without attack. ASR is malicious-tool selection with the injected document. HR is retrieval of at least one correct tool. AHR is retrieval of the malicious document. ACC-a is correct selection during attack. False negative rate, FNR, is malicious documents mislabeled benign; false positive rate, FPR, is benign documents mislabeled malicious. AUC is area under the receiver operating characteristic curve; the paper reports two AUC scores but does not display the curves or fully specify their aggregation. [A; pp. 7, 11–12]

Rates for a target task use 100 target descriptions. Main Table I results are averages across ten tasks. The supplied work does not report confidence intervals, significance tests, repeated optimization-run variability, or seed sensitivity. Hardware is specified for the gradient-based cost estimate: one NVIDIA A800 graphics processing unit, or GPU. Software versions, exact closed-model snapshots, decoding settings, and a complete reproducibility package are not supplied. The authors plan restricted access to code and data rather than providing them in this input. [A; pp. 8, 14, 17]

## 8. Experiments / Analyses

| ID | Purpose and setup | Measures and evidence | Results and qualification |
|---|---|---|---|
| X1 | Main effectiveness: two datasets, ten tasks each, eight target LLMs, default pipeline | ACC and ASR; Table I, pp. 7–8 | All reported ASRs are at least 74.3%; performance varies by model, method, and dataset. Averages do not describe every individual request. |
| X2 | Retrieval effectiveness in the main libraries | HR and AHR; Table II, p. 7 | No-attack HR 100% for both datasets; AHR 99.9%/100% on MetaTool and 96.1%/97.8% on ToolBench for gradient-free/based. |
| X3 | Compare seven adapted attacks on GPT-4o | ASR; Table III, p. 8 | ToolHijacker exceeds every listed baseline on both datasets; this is the supplied adaptation and configuration of those methods. |
| X4 | Compare performance across ten target tasks and document lengths | Figures 3–4, p. 8 | Radar plots show high but nonidentical task rates; length plots show overlap between benign and ToolHijacker descriptions. No exact point dataset or length-classifier test is supplied. |
| X5 | Change target retriever under default ablation conditions | AHR/ASR; Table IV, p. 9 | All AHRs 100%; gradient-free ASR 99% for every retriever; gradient-based 95% for ada-002 and 100% for the three open-source retrievers. |
| X6 | Vary target k from 1–10 and shadow k′ across 2, 3, 5, 7 | AHR/ASR; Figure 5, pp. 9–10 | Larger shadow candidate sets improve robustness to target candidate count. Small k can block retrieval; larger k can introduce stronger benign competition. |
| X7 | Vary shadow-query count from 1–10 | Figure 6, pp. 9–10 | AHR remains 100%; gradient-based ASR rises from 32% with one query to 98% with seven. Gradient-free minimum is reported as 92%. |
| X8 | Remove R or S | Table V, pp. 9–10 | Retrieval alone gives 100% AHR but only 5%/0% ASR; full descriptions give 99%/95% ASR. Components interact rather than being perfectly independent. |
| X9 | Change shadow selection LLM | Tables VI–VII, p. 10 | Gradient-free averages 94.75–99.50%; gradient-based 81.38% with Llama-2-7B versus 96.50% with Llama-3-8B. Single-task ablation, not Table I averages. |
| X10 | Cosine similarity versus dot product | Table VIII, p. 10 | AHR remains 100%; gradient-free ASR 99% for both; gradient-based rises from 95% to 97%. |
| X11 | One versus two malicious documents, with k′ = 2 | Figure 7, pp. 10–11 | Two documents pointing to one tool produce curves near 100% over much of k; separate targets improve ASR but retain competition. |
| X12 | Test StruQ and SecAlign fine-tuned selection models | ACC-a/AHR/ASR; Table IX, Figure 8, pp. 11–12 | Residual ASR 84.6–99.6%; SecAlign has lower ASR than StruQ in corresponding rows. Model refusals affect complementarity of rates. |
| X13 | Test four automated detectors with ten malicious documents per dataset | FNR/FPR; Table X, p. 12 | All gradient-free FNRs 100%; gradient-based PPL-W FNR 50% on MetaTool and 80% on ToolBench. Some prose conflicts with the table. |
| X14 | Optimize for task 1 and test other nine tasks | Table XII, p. 16 | Non-target ASR 0%/0.11%; non-target AHR 0.22%/4%. This measures malicious choice, not full non-target accuracy. |
| X15 | Change attacker rewriting LLM, separately from shadow selector | Table XIII, pp. 16–17 | Average ASR 69.00% with Llama-2-7B versus 99.00% with GPT-4o; Claude-derived attacks have weak Claude-3-Haiku cells. |
| X16 | Vary generated variants B from 1–5 | Table XIV, pp. 16–17 | AHR 100%, ASR 99–100%, queries 12–30. More variants do not monotonically reduce queries. |
| X17 | Vary α and β; remove loss terms | Figure 9, Table XV, pp. 16–17 | Loss removal leaves retrieval high but reduces ASR; removing readability loss gives 5% versus 95% with all losses. |
| X18 | Expand library sizes | Table XVI, p. 17 | High rates persist, with declining ASR across displayed sizes; prose reverses two method/dataset lower bounds. |
| X19 | Human identification of malicious descriptions | Six participants; seven malicious tools; Table XVII, p. 17 | FNR 71.43–100%; FPR 5.60–30.35%. Participant aggregation and uncertainty are not specified. |
| X20 | Optimization resource cost | p. 17 | Gradient-free R: one query; S: about 18 queries. Gradient-based R: about one GPU-minute; S: about eight GPU-hours on one A800. Not an equal-unit cost comparison. |

There are no formal research hypotheses to mark supported or rejected. These experiments address attack feasibility, transfer, mechanism, and defenses; they do not supply a controlled web-agent-versus-standalone-LLM experiment.

## 9. Results

### 9.1 Main model results

The following compact transcription preserves all Table I conditions. Model order is Llama-2-7B, Llama-3-8B, Llama-3-70B, Llama-3.3-70B, Claude-3-Haiku, Claude-3.5-Sonnet, GPT-3.5, GPT-4o. Every entry is a percentage. [A/B; p. 7]

| Dataset and metric | Values in model order |
|---|---|
| MetaTool, no-attack ACC | 96.7, 98.9, 98.2, 99.6, 99.2, 98.9, 98.8, 99.6 |
| MetaTool, gradient-free ASR | 98.2, 94.0, 97.0, 99.6, 85.4, 92.1, 91.0, 96.7 |
| MetaTool, gradient-based ASR | 99.8, 100, 97.2, 99.4, 82.6, 92.0, 92.8, 92.2 |
| ToolBench, no-attack ACC | 97.1, 90.5, 97.2, 97.2, 97.2, 97.8, 97.3, 98.4 |
| ToolBench, gradient-free ASR | 91.7, 80.6, 82.1, 90.8, 82.8, 93.6, 77.7, 88.2 |
| ToolBench, gradient-based ASR | 95.2, 96.6, 89.2, 94.8, 74.3, 85.2, 84.6, 83.9 |

High clean accuracy coexists with high attacked selection rates. This demonstrates that ordinary task competence does not ensure resistance in the tested pipeline. **[D]** It does not imply that clean accuracy and malicious selection are measurements of the same outcome: ACC scores legitimate correctness, while ASR scores the attacker's chosen outcome.

### 9.2 Baseline comparison and derived differences

On GPT-4o, PoisonedRAG is the best listed baseline: 39.3% on MetaTool and 58.3% on ToolBench. Gradient-free ToolHijacker obtains 96.7% and 88.2%. **[C]** Absolute advantages are 96.7−39.3 = **57.4 percentage points** and 88.2−58.3 = **29.9 percentage points**. These are not relative percent improvements. The gradient-based method also exceeds that baseline, by 92.2−39.3 = **52.9 points** and 83.9−58.3 = **25.6 points**. [Table III, p. 8]

The paper sometimes describes percentage-point differences using percent signs. For example, 96.7% versus 92.2% is a 4.5-point difference, not a 4.5% relative improvement. Likewise, 96.6% versus 80.6% is a 16-point difference. This analysis preserves the source rates and labels the arithmetic correctly.

### 9.3 Mechanism evidence

Table V is particularly informative. With gradient-free R alone, AHR is 100% but ASR is only 5%; with gradient-based R alone, AHR is 100% but ASR is 0%. Retrieval is therefore insufficient for malicious selection. Full R ⊕ S restores ASR to 99% and 95%. S alone gives gradient-free AHR/ASR 65%/63%, and gradient-based 99%/16%. [A/B; p. 9]

These results support the usefulness of both phases. **[D]** They also show that retrieval and selection effects overlap: gradient-based S retains task information and is nearly always retrieved, yet generally loses the selection competition without R. AHR should not be used as a substitute for ASR.

### 9.4 Defense and specificity results

StruQ residual ASR ranges from 90.8% to 99.6%; SecAlign ranges from 84.6% to 97.5%. These are different fine-tuned target-model conditions, not necessarily the GPT-4o conditions of Table III. Detection evaluates documents rather than complete tool-selection runs; its sample is ten malicious documents per dataset. Human detection uses seven malicious tools and six participants. These distinct denominators should not be blended. [A; pp. 11–12, 17]

The non-target experiment is narrower than a complete utility evaluation. Its 0% and 0.11% non-target ASRs show very little selection of the attacker's tool on the other nine tasks. They do not report whether the correct benign tool was always selected, whether some other incorrect tool was selected, or whether the model refused. [A/D; Table XII, p. 16]

## 10. Figure-by-figure interpretation

### Figure 1 — How documentation redirects selection

Two horizontal pipelines contrast no attack and attack. The input is the same gift-related user request. A tool library feeds retrieval; retrieved names and descriptions feed selection; the selected output is shown at the right. In the benign panel, ProductSearch is selected. In the attacked panel, a malicious GiftAdvisorPro document enters the library and shortlist, and GiftAdvisorPro becomes the output. Red arrows and text mark attacker influence. The attack description combines gift-related capabilities with a preferential-selection instruction. [B; p. 2]

This is a conceptual example, not an experimental rate or proof that every depicted tool exists. There are no numerical axes or uncertainty intervals. Its substantive point is that the attacker must influence both what reaches the LLM and what the LLM chooses.

### Figure 2 — Structured selection prompt

A prompt box contains a user question, candidate names/descriptions, and final constraints requiring exactly one listed tool and a parsable JSON output. An output box contains the chosen tool name. Dashed outlines distinguish the displayed prompt and output. There are no numerical axes. [B; p. 3]

The ordering shows the instruction–data–instruction structure that the authors later identify as sandwich prevention. It exposes the location where external descriptions share an LLM input with legitimate rules. The supplied diagram demonstrates prompt construction, not reliable enforcement of those rules.

### Figure 3 — Ten-task effectiveness

Two radar panels represent MetaTool and ToolBench. Angular axes are Task1–Task10; radial values are percentages with labeled rings roughly spanning 40–100. The legend identifies gradient-free AHR and ASR and gradient-based AHR and ASR. Blue and orange distinguish methods, while line styles distinguish retrieval from selection. [B; p. 8]

Most curves lie near the outer region, with visible task variation and more separation in ToolBench. The nearby prose says these are averages across target LLMs. Exact values for every task are not labeled and are not reconstructed here. The figures show breadth across the chosen tasks; they do not show confidence intervals or the distribution across individual models.

### Figure 4 — Document token lengths

Two panels compare benign documents, manual attacks, JudgeDeceiver, PoisonedRAG, and the two ToolHijacker variants. The y-axis is Token Length; labeled ticks include 10, 100, 500, 1,000, and 2,000. Their spacing is not uniform, so the image should not be treated as a simple linear scale; the exact transformation is not specified. Category labels form the x-axis. Colored point distributions and summary-like marks show spread. [B; p. 8]

Benign documents span a broad range, especially in ToolBench. ToolHijacker lengths overlap portions of that range; manual attacks extend higher than the ToolHijacker clusters in the visible plot. The authors infer that length alone cannot distinguish their attacks. No fitted length detector, threshold, or classification error is supplied. Exact medians and ranges are therefore not invented.

### Figure 5 — Target k versus shadow k′

Eight line panels form a two-by-four arrangement. The top row is gradient-free and the bottom row gradient-based. Columns use k′ = 2, 3, 5, and 7. Each x-axis is target k from 1–10; each y-axis is Percentage (%) from 0–100. Red solid lines denote ASR, and green dashed lines AHR. No uncertainty bands are shown. [B; p. 9]

At small k′, increasing target k can retrieve more benign competitors and reduce selection success even while malicious retrieval improves. In the lower-left panel, ASR visibly drops to approximately the mid-20% range around k = 3–5; that is an approximate visual reading, not an exact reported cell. With k′ = 5 or 7, curves are much nearer 100% and more stable. Reported anchors include gradient-based AHR rising from 74% to 99% as k goes from 1 to 3 at k′ = 2. The prose's single k = 1 statement is not sufficiently method-specific to assign its 89% value to both methods.

### Figure 6 — Number of shadow descriptions

Two panels show gradient-free and gradient-based results. The x-axis is m′ from 1–10; the y-axis is percentage from 0–100. Red ASR and green dashed AHR follow the same encoding as Figure 5. AHR remains at 100%. Gradient-based ASR starts much lower and improves markedly; gradient-free is high throughout. [B; p. 9]

The prose supplies exact anchors: gradient-based ASR 32% at one shadow description and 98% at seven; gradient-free minimum 92%. No repeated-run variability is shown. This supports the value of query diversity in the tested optimization, especially for gradients.

### Figure 7 — Number and coordination of malicious documents

Six panels contrast one document, two individually targeting themselves, and two targeting a shared tool. Rows distinguish attack methods. Axes and colors match Figure 5: target k from 1–10, percentage from 0–100, red ASR, green dashed AHR. This experiment deliberately uses the weak-shadow setting k′ = 2. [A/B; pp. 10–11]

Two individually directed documents improve ASR but retain a lower-selection region. Two coordinated documents produce curves close to 100% after the lowest k values. The unified gradient-free panel begins visibly below its later plateau, so the phrase close to 100% should not be read as every point being nearly 100%. The authors report a 24% ASR increase at k = 5 but do not explicitly distinguish relative percent from points; this analysis does not reinterpret that statement as a new exact derived result.

### Figure 8 — ASR change after prevention defenses

A grouped bar chart compares StruQ–MetaTool, StruQ–ToolBench, SecAlign–MetaTool, and SecAlign–ToolBench. The y-axis is ΔASR (%) from 0–10; blue and orange outline bars distinguish gradient-free and gradient-based attacks. The metric is defined as pre-fine-tuning ASR minus defended ASR. [A/B; p. 12]

SecAlign bars are larger than corresponding StruQ bars, and ToolBench bars are generally larger than MetaTool bars. Exact values are not printed on bars. The figure supports relative defense reductions, while Table IX supplies residual attacked rates. The pre-defense comparison values are not fully tabulated here, so exact bar heights are not reverse-engineered.

### Figure 9 — Weights on name consistency and readability

Two line panels vary α and β in Equation (13). The y-axis is Percentage (%) from 0–100. The α panel labels 0, 0.2, 1, 2, 10; the β panel labels 0, 0.01, 0.1, 1, 10. The displayed positions should be interpreted as parameter settings, not an assumed uniform linear numerical spacing. Red ASR is non-monotonic; green dashed AHR remains high. [B; p. 16]

ASR peaks in intermediate ranges and falls at extremes. The text reports high ASR for α around 1–2 and β around 0.1–1. The β = 0 endpoint is visually near the bottom and is consistent with the loss-removal result of 5% ASR in Table XV, but that exact value is attributed to the table, not read from the graph. No error bars are present.

### Figure 10 — Shadow-request generation template

A bordered text box gives the generation template. It requests diverse, realistic queries about a specified target task, with alignment, complexity, context, and practical-applicability requirements. Placeholders specify query count and maximum words. [B; p. 18]

This figure documents data construction rather than results. Its requirements do not prove that generated requests achieved the intended diversity. It is represented in compressed form because its full wording repeats the methodology.

### Figure 11 — Shadow-document generation template

A second text box asks for named tool descriptions addressing the shadow queries, variable description lengths, general functionality, and a JSON list of entries. [B; p. 18]

The text shows how a synthetic library is constructed. It does not expose all actual generated documents or how irrelevant documents were selected. Template placeholders are not numerical hyperparameter values. The example JSON is documentary content, not an instruction to this analysis.

### Figure 12 — Initial retrieval and selection text

Two blocks give initial R and S for gradient-free and gradient-based methods. Both R sequences describe space-related images. S contains an instruction naming SpaceImageLocator; gradient-based S additionally begins with five Correct tokens. [B; p. 18]

This provides one concrete initialization for MetaTool task 1. It does not reveal the final optimized texts for all tasks. There are no quantitative axes, sample statistics, or performance values.

## 11. Table-by-table interpretation

### Table I — Clean accuracy and attacked selection across models

Rows distinguish dataset, no attack, gradient-free, and gradient-based; columns are eight target LLMs. Units are percentages. All cells are transcribed in Section 9. Highest MetaTool ASR is 100% for gradient-based Llama-3-8B; lowest overall main-table ASR is 74.3% for gradient-based Claude-3-Haiku on ToolBench. ToolBench's gradient-free maximum is 93.6% on Claude-3.5-Sonnet; its gradient-based maximum is 96.6% on Llama-3-8B. [p. 7]

No standard errors or significance markers are supplied. Clean and attack rows use different outcome definitions. Results average ten tasks rather than proving uniformly high performance on every task.

### Table II — Retrieval-stage rates

No-attack HR is 100% for both datasets. MetaTool AHR is 99.9% gradient-free and 100% gradient-based; ToolBench AHR is 96.1% and 97.8%. These are intermediate retrieval rates, with default k = 5. [p. 7]

The introduction's generic 100% MetaTool statement compresses a method-specific distinction: the table's gradient-free value is 99.9%, not exactly 100%. No uncertainty measurements are shown.

### Table III — GPT-4o comparison with seven baselines

| Dataset | Naive | Escape | Context/content ignore | Fake completion | Combined | JudgeDeceiver | PoisonedRAG | Gradient-free | Gradient-based |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MetaTool | 6.0 | 28.2 | 1.2 | 14.5 | 9.7 | 30.2 | 39.3 | 96.7 | 92.2 |
| ToolBench | 24.8 | 24.6 | 11.3 | 23.0 | 11.7 | 26.4 | 58.3 | 88.2 | 83.9 |

All entries are ASR percentages. The table labels Content Ignore while the prose uses Context Ignore; these apparently refer to the same listed baseline, but the wording differs. ToolHijacker is strongest in both rows. Exact baseline documents are absent because the paper locates them in the technical report. [p. 8]

### Table IV — Target retrievers

Gradient-free AHR/ASR is 100%/99% for all four retrievers. Gradient-based AHR is 100% throughout, with ASR 95% for text-embedding-ada-002 and 100% for Contriever, Contriever-ms, and Sentence-BERT-tb. The reported gradient-based average is 98.75%. [p. 9]

This is the default single-task ablation, not a four-retriever average of the full main experiment. The authors attribute the lower ada-002 ASR to ranking; corresponding rank distributions are not supplied.

### Table V — R and S components

Gradient-free R ⊕ S, R only, and S only give AHR/ASR 100/99, 100/5, and 65/63. Gradient-based values are 100/95, 100/0, and 99/16. All units are percent. [p. 9]

The key contrast is that perfect malicious retrieval can coexist with negligible malicious selection. No statistical variability is reported. This table supports the decomposition while showing cross-component effects.

### Table VI — Gradient-free shadow-selector transfer

Eight rows change the shadow LLM and eight columns change the target LLM. Reported row-average ASRs, in the model order used earlier, are 95.13%, 95.25%, 94.75%, 97.25%, 97.25%, 99.50%, 97.38%, and 97.75%. Claude-3.5-Sonnet has the highest average; Llama-3-70B the lowest. The lowest cell is 70% for Llama-2-7B shadow to Claude-3-Haiku target. [p. 10]

Many cells tie at 100%, but those ties have no uncertainty estimates. The full 64-cell matrix is deliberately compressed to averages, extrema, and meaningful transfer exceptions. Row averages do not establish monotonically improving performance with every presumed increase in model capability.

### Table VII — Gradient-based shadow-selector transfer

The Llama-2-7B shadow row is 100, 100, 34, 95, 55, 82, 98, 87%; average 81.38%. The Llama-3-8B row is 100, 100, 100, 100, 98, 97, 82, 95%; average 96.50%. [p. 10]

**[C]** The displayed average difference is 96.50−81.38 = 15.12 percentage points. Transfer is not uniformly improved for every target: GPT-3.5 falls from 98% to 82%. The average conclusion needs that qualification.

### Table VIII — Similarity function

Cosine and dot-product retrieval both produce 100% AHR. Gradient-free ASR is 99% under both; gradient-based ASR is 95% under cosine and 97% under dot product. [p. 10]

**[C]** The latter difference is two percentage points. It does not mean dot product helps every attack method or every dataset. This is one default ablation condition.

### Table IX — Prevention defenses

| Defense/dataset | Gradient-free ACC-a/AHR/ASR (%) | Gradient-based ACC-a/AHR/ASR (%) |
|---|---|---|
| StruQ/MetaTool | 0.3 / 99.9 / 99.6 | 2.1 / 100 / 97.9 |
| StruQ/ToolBench | 5.7 / 96.1 / 90.8 | 4.1 / 97.8 / 92.1 |
| SecAlign/MetaTool | 2.5 / 99.9 / 97.5 | 7.4 / 100 / 92.1 |
| SecAlign/ToolBench | 8.2 / 96.1 / 86.9 | 11.3 / 97.8 / 84.6 |

SecAlign has lower corresponding ASR than StruQ. Residual rates remain high. ACC-a and ASR need not sum to 100% because refusals or invalid responses can be outside both categories. The supplied evaluation uses the defenses' fine-tuned target models; it does not establish universal failure of all possible deployments of these defense ideas. [pp. 11–12]

### Table X — Automated detection

Gradient-free FNR is 100% for all four detectors on both datasets. Gradient-based FNRs, in order known-answer, DataSentinel, PPL, PPL-W, are MetaTool 100%, 90%, 80%, 50%; ToolBench 100%, 90%, 90%, 80%. [p. 12]

Shared FPR cells are MetaTool 0%, 0%, 1.01%, 0%; ToolBench 0.01%, 2.61%, 0.85%, 2.99%, in the same detector order. The visual groups these rates by dataset and detector rather than giving separate clearly distinct FPR values for every attack row. This reflects benign-document testing, but no unstated per-attack variation is invented.

Table X conflicts with prose saying known-answer and DataSentinel FNRs exceed 90%: DataSentinel's gradient-based entries equal 90%. Its MetaTool gradient-based PPL FNR is 80%, while the introduction gives an unqualified 90% example. The threshold discussion gives approximately 1% as an example calibration limit, not a guarantee that every reported evaluation FPR stays below 1%.

### Table XI — Symbols

This is a notation reference, not a results comparison. It defines E, E′, E_A, D, D_k, D′, selected and malicious documents, target and shadow query sets, R, S, the losses, encoders, optimization parameters, and tree lists. [p. 16]

The description of d_t(S) is circular unless read with the method: it is the malicious document treated as a function of the variable S while the name and R are fixed. The table does not resolve the E versus E′ issue in Equation (12).

### Table XII — Target and non-target requests

For 100 target descriptions, gradient-free AHR/ASR is 100%/99% and gradient-based 100%/95%. For 900 descriptions of the other nine tasks, the values are 0.22%/0% and 4%/0.11%. [p. 16]

The attack is task-specific in this experiment. Full non-target correct-selection accuracy is not reported, so low attack success is incomplete evidence about preserved overall utility.

### Table XIII — Attacker rewriting LLM

Eight attacker-model rows have average ASRs 69.00%, 95.63%, 97.13%, 97.25%, 92.88%, 93.00%, 94.38%, and 99.00%, in the earlier model order. GPT-4o has the highest average and Llama-2-7B the lowest. [p. 17]

For Claude-3-Haiku and Claude-3.5-Sonnet attackers, the Claude-3-Haiku target cells are only 43% and 44%; all other target cells in those two rows are 100%. This notable exception qualifies the prose's universality claim. The Llama-2-7B attacker row ranges from 45% on GPT-3.5 to 98% on Llama-2-7B. The remaining full matrix is compressed; attacker generation and shadow evaluation are separate experimental roles.

### Table XIV — Branching and queries

B = 1, 2, 3, 4, 5 yields AHR 100% throughout; ASR 100%, 99%, 100%, 100%, 100%; and total queries 30, 12, 18, 24, 30. [p. 17]

B = 2 minimizes the displayed query total, while B = 1 requires more iterations. These are observed query counts in an ablation, not a guarantee of optimization cost for every target task. No dispersion is supplied.

### Table XV — Loss removal

Without L1: AHR 100%, ASR 54%. Without L2: 100%, 56%. Without L3: 100%, 5%. All losses: 100%, 95%. [p. 17]

**[C]** ASR decreases are 41, 39, and 90 percentage points, respectively, calculated from 95−54, 95−56, and 95−5. The readability term has the largest displayed effect. Retrieval remains unchanged, so this ablation localizes the observed loss to selection outcomes. It does not directly measure the internal reason the LLM rejected or ignored an unnatural sequence.

### Table XVI — Library expansion

MetaTool sizes 50, 100, 150: gradient-free AHR is always 100%, ASR 98.8%, 98.0%, 96.7%; gradient-based AHR always 100%, ASR 98.0%, 95.1%, 93.3%. ToolBench sizes 2,500, 5,000, 7,500: gradient-free AHR 99.6%, 97.5%, 97.6%, ASR 95.8%, 94.9%, 92.8%; gradient-based AHR 99.6%, 99.0%, 98.2%, ASR 88.7%, 88.4%, 84.8%. [p. 17]

The prose assigns ≥93.3% to gradient-free ToolBench and ≥92.8% to gradient-based MetaTool. The table instead gives gradient-free ToolBench minimum 92.8% and gradient-based MetaTool minimum 93.3%. Both are preserved as an unresolved text–table mismatch; this analysis uses the explicit cells when describing the table.

### Table XVII — Human detection

For libraries of 200, 400, 600 tools, gradient-free FNR is 85.71% throughout; FPR 12.44%, 5.60%, 18.38%. Gradient-based FNR is 85.71%, 100%, 71.43%; FPR 7.77%, 9.67%, 30.35%. [p. 17]

There are six participants and seven malicious tools. High false negatives coexist with nontrivial false positives. No confidence intervals, participant-level outcomes, expertise description, or aggregation formula is supplied. The experiment supports difficulty for these participants under these conditions, not a population-wide human detection rate.

## 12. Diagram / Architecture Interpretation

Figures 1 and 2 are the substantive system diagrams. Figure 1 has a data path from request and library to retrieval, from retrieved documents to selection, and from selection to a tool name. The attacker adds a document upstream of retrieval; the effect travels through the shortlist into the LLM decision. The diagram's control change is the final chosen tool, not a demonstrated downstream exploit.

Figure 2 specifies the selection interface: the LLM receives the request and candidate documents inside legitimate constraints, and returns one name. The trailer attempts to constrain output format and membership. The attack does not require adding an out-of-library output when its own tool is already in the shortlist. **[D]** A well-formed, permitted-name response can therefore still be attacker-directed.

Algorithm 1 is the optimization-control architecture. Candidate text flows from attacker LLM to shadow selector; selector outputs flow into matching, scoring, pruning, and feedback; retained text and feedback return to the attacker LLM. Early stopping occurs when one variant succeeds on all shadow requests. This feedback loop is different from the target agent's tool-selection flow and should not be mistaken for querying the victim.

Figures 10–12 are documentation boxes rather than system architectures. They provide generation constraints and initialization. No separate implementation diagram, API call graph, deployed-platform integration diagram, or measured execution trace is supplied.

## 13. Equations and mathematical concepts

The mathematics defines the pipeline and optimization; it does not provide a theorem guaranteeing transfer or global optimality. Below, averages and probabilities refer to the supplied finite request sets and models.

| Equation | Mathematical identity and plain-language role |
|---|---|
| (1), p. 3 | D_k = Top-k(q; D) = {d_1, …, d_k}. The output is a set of retrieved candidates. The notation locally labels retrieved documents; it does not imply they are always the first k entries of the original library. |
| (2), p. 3 | Top-k ranks d_j in D by Sim(f_q(q), f_d(d_j)). Inputs are the request, documents, their encoders, similarity function, and k. Output is the highest-similarity shortlist. Cosine similarity and dot product are examples. |
| (3), p. 3 | E(q, D_k) = d*. The selection LLM maps the request and shortlist to the selected tool. |
| (4), p. 3 | E(p_header ⊕ q ⊕ d_1 ⊕ … ⊕ d_k ⊕ p_trailer) = o_d*. The abstract selection is implemented as one concatenated prompt producing an output containing the chosen name. |
| (5), p. 4 | Maximize over d_t: (1/m′) Σ_i I[E′(q′_i, Top-k′(q′_i; D′ ∪ {d_t})) = o_t]. I is 1 for malicious selection and 0 otherwise. This is average shadow end-to-end success, with retrieval inside the objective. |
| (6), p. 5 | Maximize over R: (1/m′) Σ_i Sim(f′(q′_i), f′(R ⊕ S)). This surrogate raises semantic retrieval similarity across shadow queries. S is its initial sequence during this phase; R is changed. |
| (7), p. 5 | Maximize over S: (1/m′) Σ_i I[E′(q′_i, D-tilde^(i) ∪ {d_t(S)}) = o_t]. The candidate set explicitly contains the malicious document plus k′−1 shadow documents. This isolates selection optimization from target retrieval. |
| (8), p. 6 | Maximize over S the product over i of E′(o_t | p_header ⊕ q′_i ⊕ candidate documents ⊕ d_t(S) ⊕ p_trailer). Instead of a binary decision, optimize the probability of the target output. |
| (9), p. 6 | L1(x^(i), S) = −log E′(o_t | x^(i), S). Lower negative log probability means the desired response is more likely. x^(i) represents the rest of the prompt around S. |
| (10), p. 6 | E′(o_t | x^(i), S) is the product, j = 1…ρ, of next-token probabilities for τ_j conditioned on the surrounding prompt and previous target-output tokens. This is the autoregressive factorization of the desired output sequence. |
| (11), p. 6 | L2(x^(i), S) = −log E′(d_t_name | x^(i), S). This adds emphasis specifically on the malicious name rather than only the full response format. |
| (12), p. 6 | L3(x^(i), S) = −(1/γ) Σ_j log E(T_j | x^(i)_1:h_i, T_1, …, T_(j−1)). This is average negative log probability of S's own tokens, encouraging readability. The printed model symbol is E, although surrounding optimization uses E′. That discrepancy is not silently repaired. |
| (13), p. 6 | L_all = L1 + αL2 + βL3. α and β weight name consistency and readability relative to alignment. They are hyperparameters, not learned quantities in the supplied description. |
| (14), p. 6 | Minimize over S: Σ_i L_all(x^(i), S). The same S should work across multiple shadow request–candidate pairs. This is a summed loss, unlike the average indicator objectives above. |
| (15), p. 7 | HR@k = (1/m) Σ_i hit(q_i, k). The indicator is one when at least one correct tool is in the retrieved shortlist. This measures legitimate retrieval availability. |
| (16), p. 7 | AHR@k = (1/m) Σ_i a-hit(q_i, k). The indicator is one when the malicious document is retrieved. This measures attacker access to the selection prompt, not final malicious choice. |

Symbols in token-level equations: S = (T_1, …, T_γ) is the optimized injected token sequence; o_t = (τ_1, …, τ_ρ) is the desired output token sequence. h_i denotes insertion position; n_i is input length. The surrounding x segments represent text before and after the inserted sequence. The indexing in Equation (10) is compressed and potentially confusing because x is described as excluding S while suffix indices account for its length; the intended before/after-prompt role is clear, but a literal tensor-index implementation is not fully specified.

The logarithmic losses transform high desired probabilities into low costs. L3 is called a perplexity loss, but its displayed form is average negative log-likelihood, not an explicitly exponentiated perplexity value. The authors use it to promote plausible text. The loss-removal experiment tests its practical contribution.

Two additional formulas matter. Prevention reduction is ΔASR = ASR_none − ASR_d, with the models' fine-tuning state defining the comparison. The appendix query formula is (B + B × m′) × iter, where iter is the actual iteration count. **[D]** This formula matches a simplified case with one active candidate parent per iteration; the printed tree algorithm can retain multiple parents, so the formula alone does not fully specify cost accounting for all tree widths.

## 14. Interpretation and discussion

The strongest supported finding is that an attacker-controlled tool description can be optimized to cross both stages of a selection pipeline. Table V connects the mechanism to results: being found is not enough, and being persuasive without relevance can be insufficient. Transfer tables show that the attacker need not use the exact target selector or retriever for substantial success in the tested settings.

The authors explain transfer through shared alignment objectives, overlapping training data, and similar semantic patterns. These explanations are author interpretations rather than independently isolated causal results. The experiments demonstrate transfer; they do not directly measure training overlap or prove why transfer occurs. [A/D boundary; pp. 5, 8]

The relevance to web-agent security is precise. **[D]** An agent can consume third-party text while deciding which service will act for the user. This creates a chain from untrusted content to model decision to potentially consequential action. In a web context, the paper's introduction and related work mention browser agents and webpage-based injection, but ToolHijacker's own evaluated surface is tool documentation. It should not be reclassified as an experimental webpage attack.

### Cross-reference and consistency checks

1. **Retrieval-rate precision:** pp. 1–2 broadly describe 100% MetaTool attack hit rate; Table II reports gradient-free 99.9% and gradient-based 100%. The method-specific table is more precise.
2. **PPL detection mismatch:** p. 2 describes PPL missing 90% of gradient-based documents with below-1% false positives. Table X, p. 12, gives MetaTool PPL FNR 80% and FPR 1.01%; ToolBench gives 90% and 0.85%. The introductory statement fits ToolBench better, but its condition is not stated there.
3. **Strict versus non-strict language:** p. 12 says known-answer and DataSentinel FNRs exceed 90%; Table X has DataSentinel gradient-based FNR equal to 90%. Both should not be described as strictly above 90% in every condition.
4. **Majority language:** p. 12 says both perplexity methods fail to identify the majority. MetaTool gradient-based PPL-W FNR is exactly 50%, so that individual cell is half, not strictly a majority.
5. **Dynamic-library text–table mismatch:** p. 17 reverses the 92.8% and 93.3% method/dataset lower bounds relative to Table XVI. The discrepancy cannot be resolved from supplied evidence.
6. **Percent versus points:** several prose comparisons use percent signs for differences between percentage rates. Derived comparisons in this analysis explicitly use percentage points.
7. **Algorithm vector indexing:** Algorithm 1 initializes FLAG with m′ entries but indexes it by candidate node S_l. The number of candidate nodes need not equal m′. The prose treats FLAG as candidate success counts, which is conceptually clear, but printed dimensions are ambiguous.
8. **Algorithm termination:** the final return references Leaf_next after the loop resets that list. A literal implementation may not return the intended best candidate. The supplied code is absent, so this cannot be checked against implementation.
9. **Algorithm iteration notation:** the input names T_iter, while the printed loop uses T. Their intended relationship is apparent but not explicitly repaired here.
10. **Model notation:** Equation (12) prints E, the target LLM symbol, in a shadow-optimization discussion. Whether this is a typographical error or a different scoring model is unspecified.
11. **Output versus tool-name notation:** o_t is defined as the shadow output selecting the malicious document, while Algorithm 1 calls it the malicious tool name. Matching and complete-response probability may depend on that distinction; the exact implementation is absent.
12. **Baseline naming:** Context Ignore in prose appears as Content Ignore in Table III. This is a terminology variation, not evidence of a separately evaluated eighth baseline.

These issues do not erase clear table results, but they limit literal reproducibility and require condition-specific reporting. No discrepancy has been automatically reconciled using external information.

## 15. Contributions and novelty

**Conceptual contribution [A]:** the authors identify retrieval plus selection as the attack path and emphasize a no-box tool-selection threat. Their claim of being first is a literature-positioning claim; closed-document analysis cannot independently establish priority.

**Methodological and algorithmic contribution [A]:** malicious documentation is divided into retrieval-oriented R and selection-oriented S, with sequential optimization, a shadow pipeline, and gradient-free and gradient-based alternatives. The gradient-free selection procedure uses generation, evaluation, pruning, and feedback; the gradient-based procedure balances output alignment, name consistency, and readability.

**Empirical contribution [A/B]:** experiments across two datasets and eight LLMs, retriever transfer, configuration ablations, six automated defenses, human detection, non-target outcomes, dynamic libraries, and cost estimates provide evidence about feasibility and sensitivity.

There is no supplied theorem proving attack success, no new standalone benchmark introduced as the principal contribution, and no deployed malicious-tool system demonstrated. The paper adapts existing benchmark libraries and established optimization ideas while presenting its integrated attack framework as novel.

## 16. Limitations

### Authors' stated limitations and boundaries

The authors acknowledge that direct optimization is discrete, discontinuous, non-differentiable, and vulnerable to local optima. They use decomposition and surrogate objectives rather than claim an exact global solution. [p. 4]

They acknowledge incomplete material in this version: the full appendix, including E_A's system prompt and target tasks, is available in technical report [35]. [p. 17, footnote]

They bound the experiment ethically: controlled environments, no development or online deployment of real malicious tools, and restricted-access plans for code and data. Their conclusion proposes joint selection-and-calling attacks as future work, consistent with the present focus on selection. [p. 14]

The supplied work contains no dedicated comprehensive limitations section. Low-performance cells and defense detection rates are observed results, not automatically author-admitted limitations of the whole study.

### Additional evidence-based analyst observations [D]

The study does not directly compare standalone LLMs with agents, or web agents with other agents. It also does not measure downstream harm. Generalizing from malicious selection to data theft requires additional execution and permission assumptions.

Each dataset uses ten researcher-designed target tasks. The complete list, exact descriptions, generation checks, and annotation agreement are not available. This constrains assessment of representativeness and query diversity.

Most ablations use one MetaTool task. They are informative about mechanism but narrower than the main ten-task averages. One-task findings about model choice or loss weights should not be treated as universal settings.

Repeated-run variability, seeds, intervals, model-version identifiers, and significance tests are missing. Many ablation rates use only 100 queries, and detector testing uses only ten malicious documents per dataset. Apparent small differences may be unstable even though no supplied uncertainty permits quantifying that instability.

The utility experiment reports malicious retrieval and selection on non-target tasks rather than correct-selection accuracy. The human experiment has six participants and limited description of their expertise and outcome aggregation.

The dynamic-library study changes library size but does not fully document realistic timing, update order, document composition, or attacker reoptimization. It demonstrates robustness across displayed library conditions, not every live ecosystem update process.

Several internal reporting and pseudocode inconsistencies remain unresolved. These are reproducibility and interpretation concerns, separately documented rather than silently corrected.

## 17. Threats to validity

These validity labels are analyst framing, not headings used by the authors.

**Internal validity [D]:** component ablations support the role of R and S, but the components influence each other. Different shadow LLMs, generators, and optimization procedures can change more than one property of a payload. Explanations invoking security, semantic integrity, or training overlap are not independently isolated by mechanistic controls.

**Construct validity [D]:** ASR measures malicious-tool selection, not successful harmful execution. AHR measures access to the shortlist, not persuasion. Low non-target ASR does not measure complete legitimate utility. Detector FNR measures document classification, and is not directly comparable with request-level ASR.

**External validity [D]:** two libraries and eight target LLMs give useful breadth, but the system model is specifically retrieval followed by one-tool selection. Tool approval policies, different architectures, multiple-step plans, restricted tool sets, and execution verification are outside the evaluated comparison.

**Statistical conclusion validity [D]:** point estimates are supplied without confidence intervals, repeated runs, or formal tests. The paper's ten-task means, one-task ablations, and ten-document detector samples have different uncertainty structures. The analysis cannot supply missing significance judgments.

**Ecological validity [D]:** controlled injection bypasses the question of whether a real tool ecosystem would admit and integrate the document. The ethics statement confirms no online deployment of actual malicious tools. Human detection conditions are limited and do not establish behavior of professional reviewers in production workflows.

**Reproducibility [D]:** parameters, prompts, and mathematical objectives provide substantial methodological information, but the complete attacker prompt, target tasks, final payloads, implementation, random seeds, and exact service versions are absent. Algorithm and notation inconsistencies further complicate faithful replication.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

The conclusion proposes joint attacks on tool selection and tool calling, and new defense strategies against ToolHijacker. The ethics discussion also motivates more rigorous tool validation and safer agent architectures, but it does not evaluate such mechanisms. [A; p. 14]

### B. Additional open questions [D]

How large is the vulnerability difference between a matched standalone LLM and an agent given the same untrusted content? How does web browsing change exposure relative to tool-library ingestion? These are necessary comparative studies for the user's broader question and remain unanswered here.

How often would real platforms admit and agents install the malicious tool? What fraction of malicious selections would survive user authorization, permission restrictions, or execution verification? Can defense performance be improved without losing legitimate tool-selection accuracy?

How stable are optimized documents across repeated runs, model updates, different languages, more diverse tasks, and genuinely changing libraries? Would a complete non-target accuracy evaluation reveal benign-task degradation that low malicious ASR misses? Can documentation provenance or semantic validation distinguish relevant descriptions from relevant-looking policy manipulation?

These are logical gaps in the supplied evidence, not claims that the paper evaluated or endorsed a particular solution.

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning |
|---|---|
| LLM | Large language model; the language-processing component used to choose among candidates. |
| LLM agent | An LLM-based system connected to external environments and tools. |
| API | Application programming interface; a specified way to call a service or function. |
| Tool library D | Collection of available tool documents. |
| Tool document d_j | A named tool's description and associated interface information. |
| Retriever | Component selecting a shortlist by relevance. |
| Embedding | Numerical representation used for similarity comparison. |
| Dual encoder | Separate encoding of queries and documents before comparing their vectors. |
| f_q, f_d | Query encoder and document encoder. |
| Sim | Similarity function, such as cosine similarity or dot product. |
| k, D_k | Number of target retrieved documents and the resulting shortlist. |
| q, Q, m | One target request, the set of target descriptions, and its size. |
| E, d*, o_d* | Target selection model, selected tool, and output naming it. |
| E′, f′, D′, Q′ | Shadow selector, retriever, library, and descriptions. |
| m′, k′ | Number of shadow queries and number of shadow candidates. |
| E_A | Attacker LLM that proposes rewritten selection text. |
| d_t, d_t_name, d_t_des | Malicious document, its name, and its description. |
| d_t(S) | Malicious document viewed as changing with S while other parts are fixed. |
| R | Description subsequence primarily optimized for retrieval. |
| S, S0 | Selection-oriented subsequence and its initialization. |
| ⊕ | Concatenation: join strings in sequence. |
| I | Indicator: one when a condition is true, zero otherwise. |
| o_t | Desired output selecting the malicious tool; exact name-versus-response use varies in the paper. |
| D-tilde^(i) | Shadow benign candidates paired with shadow query i during selection optimization. |
| L1, L2, L3 | Full-output alignment, malicious-name consistency, and readability losses. |
| α, β | Weights on consistency and readability. |
| T_j, γ | Tokens of S and its token length. |
| τ_j, ρ | Tokens of the desired response and its length. |
| B, W, T_iter | Variants per parent, retained tree width, and iteration limit. |
| Leaf_curr, Leaf_next, Feed | Current candidates, next candidates, and optimization feedback. |
| EM | Output matching function; exact matching implementation is not supplied. |
| ACC, ACC-a | Correct selection without attack and with attack. |
| ASR | Attack success rate: malicious tool selected. |
| HR, AHR | Legitimate-tool retrieval rate and malicious-document retrieval rate. |
| PPL, PPL-W | Perplexity and windowed-perplexity detection. |
| FNR, FPR | Malicious documents missed and benign documents falsely flagged. |
| AUC | Area under a receiver operating characteristic curve; aggregate discrimination score. |
| GPU | Graphics processing unit used for gradient-based computation. |
| MCP | Model context protocol, mentioned as a tool-document attack context; not a separately evaluated MCP deployment here. |
| RAG | Retrieval-augmented generation; retrieve external material before generating an answer. |
| No-box | No target inspection or direct target queries under this paper's threat model. |
| Transfer attack | Attack developed using substitute components and evaluated on different target components. |

## 20. Key numerical results

All source rates below retain their reported precision. Visually readable means a supplied table or figure supports the value; it does not imply independent experimental verification.

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document | 18 | pages | Supplied physical PDF sequence | Author-reported/input metadata | pp. 1–18 |
| Main evaluation requests | 1,000 | descriptions per dataset | 10 tasks × 100 | Author-reported | p. 6 |
| MetaTool library | 199 | benign documents | Main evaluation | Author-reported | p. 6 |
| ToolBench library | 9,650 | benign documents | After filtering | Author-reported | p. 6 |
| Shadow query/candidate counts | 5 / 5 | queries/candidates | Defaults; four benign plus malicious | Author-reported | p. 7 |
| Target retrieval count | 5 | candidates | Default | Author-reported | p. 8 |
| Gradient-free GPT-4o ASR | 96.7 / 88.2 | % | MetaTool / ToolBench | Author-reported; visually readable | Table I, p. 7 |
| Gradient-based GPT-4o ASR | 92.2 / 83.9 | % | MetaTool / ToolBench | Author-reported; visually readable | Table I, p. 7 |
| ToolBench AHR | 96.1 / 97.8 | % | Gradient-free / based | Author-reported; visually readable | Table II, p. 7 |
| Best baseline ASR | 39.3 / 58.3 | % | PoisonedRAG; MetaTool / ToolBench; GPT-4o | Author-reported; visually readable | Table III, p. 8 |
| Gradient-free advantage over best baseline | 57.4 / 29.9 | percentage points | 96.7−39.3 / 88.2−58.3 | Analyst-derived | Table III, p. 8 |
| R-only ASR | 5 / 0 | % | Gradient-free / based default ablation | Author-reported; visually readable | Table V, p. 9 |
| Gradient-based shadow-query sensitivity | 32 → 98 | % ASR | m′ = 1 → 7 | Author-reported | p. 10; Figure 6 |
| Gradient-based shadow-model averages | 81.38 / 96.50 | % ASR | Llama-2-7B / Llama-3-8B | Author-reported; visually readable | Table VII, p. 10 |
| Residual prevention ASR | 84.6–99.6 | % | All Table IX conditions | Analyst-derived range from reported cells | Table IX, p. 11 |
| Gradient-free detector FNR | 100 | % | All four detectors, both datasets | Author-reported; visually readable | Table X, p. 12 |
| Gradient-based PPL-W FNR | 50 / 80 | % | MetaTool / ToolBench | Author-reported; visually readable | Table X, p. 12 |
| PPL / PPL-W AUC | 0.64 / 0.74 | score | Aggregation condition unspecified | Author-reported | p. 12 |
| Non-target ASR | 0 / 0.11 | % | Gradient-free / based; 900 descriptions | Author-reported; visually readable | Table XII, p. 16 |
| Best displayed B query count | 12 | queries | B = 2; ASR 99% | Author-reported; visually readable | Table XIV, p. 17 |
| ASR without readability loss | 5 | % | Versus 95% with all losses | Author-reported; visually readable | Table XV, p. 17 |
| Human study | 6 / 7 | participants/malicious tools | Libraries of 200, 400, 600 | Author-reported | p. 17 |
| Human FNR range | 71.43–100 | % | Table XVII conditions | Analyst-derived range from reported cells | Table XVII, p. 17 |
| Gradient-free construction cost | 1 + approximately 18 | LLM queries | R plus S | Author-reported | p. 17 |
| Gradient-based construction cost | approximately 1 / 8 | GPU-minute / GPU-hours | R / S; one NVIDIA A800 | Author-reported | p. 17 |

No exact numerical result is assigned to an unlabeled plot point. Approximate visual trends are explicitly described in Section 10 and are not promoted into this reference table as precise measurements.

## 21. Claim–evidence map

| Major claim | Evidence | Experiment/object | Source | Qualification/evidence strength |
|---|---|---|---|---|
| Tool documentation can manipulate both retrieval and selection | High main AHR and ASR; component removal contrasts | X1, X2, X8; Tables I, II, V | pp. 7–9 | Strong evidence within the controlled two-stage pipeline; no downstream harmful execution measured. |
| Attack can transfer without target queries | No-box restrictions plus different shadow/target results | X1, X5, X9 | pp. 4, 7, 9–10 | Author-reported protocol; independent enforcement of no target access cannot be checked from supplied artifacts. |
| Two-part construction is useful | R alone retrieves but seldom wins; full R ⊕ S wins frequently | X8; Table V | p. 9 | Strong ablation evidence for default task; components are not causally independent. |
| ToolHijacker exceeds listed adapted baselines | GPT-4o ASRs exceed seven comparisons | X3; Table III | p. 8 | Clear numerical comparison; full baseline payloads and implementation absent. |
| Tested prevention defenses leave substantial risk | Residual ASR 84.6–99.6% | X12; Table IX | pp. 11–12 | Specific fine-tuned models and settings; no universal claim about all prevention approaches. |
| Tested detectors miss many malicious documents | FNRs 50–100%, depending on method and condition | X13; Table X | p. 12 | Ten malicious documents per dataset; prose contains strictness and value mismatches. |
| Attack is targeted in the displayed utility test | Non-target ASR 0%/0.11% | X14; Table XII | p. 16 | One optimized target task; legitimate non-target ACC not supplied. |
| Readability term supports selection | ASR 95% with all losses versus 5% without L3 | X17; Table XV | p. 17 | Strong default-condition contrast; explanation about perceived anomaly is not directly measured. |
| Library-size robustness is demonstrated over displayed sizes | High Table XVI rates at increasing sizes | X18; Table XVI | p. 17 | Table/prose mismatch; simplified size changes, not comprehensive live-update evaluation. |
| Human review is difficult under tested conditions | High FNR with nontrivial FPR | X19; Table XVII | p. 17 | Six participants, seven malicious tools; aggregation and uncertainty unavailable. |
| Agent integration creates a relevant extra attack surface | External-document ingestion, selection, and assumed execution link | Threat model; Figures 1–2 | pp. 1–4 | Analyst inference relevant to web-agent research; no standalone-versus-agent comparison. |
| Real-world harm was not demonstrated | Controlled experiments; no actual malicious tools deployed | Ethics statement | p. 14 | Explicit study boundary, not evidence that deployment would be harmless. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an AI assistant looking through a directory of apps to find one that can help you. First it searches for descriptions related to your request. Then it reads a few descriptions and chooses an app. An attacker can write an app description that looks useful but also nudges the assistant to pick the attacker's app.

ToolHijacker separates those jobs. One part of the description helps it appear in search results. Another part helps it win the assistant's choice. The researchers practice with substitute models and made-up examples, then test whether the description also works on other models. In their tests, it often does—even when the actual target model was different from the practice model.

The tested defenses did not reliably stop this. Some descriptions looked normal enough that automatic detectors and human participants missed them. But the researchers mainly measured which tool the assistant chose. They did not deploy real harmful tools, and choosing a malicious tool is not the same measurement as successfully stealing information.

This helps explain a risk of giving an AI assistant access to outside services: text written by someone else can influence a decision about what the assistant will use. However, this paper does not test whether web agents are more vulnerable than ordinary standalone chat models. It gives evidence about one additional route for attacks, not a numerical comparison between those two kinds of systems.

## Completeness Audit

The denominator is the supplied inventory: 18 text pages, 14 rendered pages, eight substantive main sections including ethics, references, three appendix components, 12 supplied figures, 17 supplied tables, 16 numbered equations, one algorithm, and 20 distinct experiment/analysis entries. Coverage concerns representation of those supplied items, not completeness of an absent technical-report appendix.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract | Yes, text and image | Yes | Represented in compressed form | Claims connected to detailed evidence and qualifications. |
| S1 Introduction and contributions | Yes, text and images | Yes | Fully represented | Motivation, gap, novelty claim, and comparative boundary retained. |
| S2 Tool selection | Yes, text and image | Yes | Fully represented | Library, dual encoder, shortlist, structured prompt, Equations 1–4. |
| S2 Threat model | Yes; p. 4 text-only | Yes | Fully represented | Goal, knowledge, capabilities, exclusions, execution assumption. |
| S3 Overview and optimization formulation | Yes; p. 4 text-only | Yes | Fully represented | Shadow pipeline, Equation 5, decomposition, discrete-search rationale. |
| S3 Retrieval optimization | Yes, text and relevant image | Yes | Fully represented | Both variants, Equation 6, generation template, HotFlip, rationale. |
| S3 Selection optimization | Yes, text and images | Yes | Fully represented | Both variants, losses, position and step-wise optimization. |
| S4 Setup | Yes, text and images | Yes | Fully represented | Datasets, samples, models, retrievers, baselines, parameters, metrics. |
| S4 Main results | Yes, text and images | Yes | Fully represented | Tables I–III and task/length figures retained. |
| S4 Ablations | Yes, text and images | Yes | Represented in compressed form | Every distinct manipulation represented; repetitive matrix cells compressed. |
| S5 Prevention defenses | Yes, text and images | Yes | Fully represented | Models, ACC-a, AHR, ASR, refusals, reduction plot. |
| S5 Detection defenses | Yes, text and image | Yes | Fully represented | Detector logic, thresholds, windows, sample sizes, all FNR/FPR conditions. |
| S6 Tool-selection related work | Yes; p. 13 text-only | Yes | Represented in compressed form | Integration, retrieval, training, reranking, feedback, tool generation categories. |
| S6 Attack related work | Yes; p. 13 text-only | Yes | Represented in compressed form | Manual/optimized, tool-calling, web, multimodal, multi-agent positioning. |
| S6 Defense related work | Yes; p. 13 text-only | Yes | Represented in compressed form | Preprocessing, training, policy enforcement, detection; no original-source verification. |
| S7 Conclusion/future work | Yes, text-only on pp. 13–14 | Yes | Fully represented | Joint selection/calling and new defenses. |
| S8 Ethics | Yes, text-only | Yes | Represented in compressed form | Controlled testing, no real tools, restricted release, consent, no unnecessary personal data. |
| S9 References 1–75 | Yes, text-only | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries not individually restated; relevant categories and method positioning preserved. |
| Explicit research questions | Assessed | Yes | Fully represented | None formally numbered; objectives distinguished from user's question. |
| Formal hypotheses | Assessed | Yes | Fully represented | None supplied; no tests invented. |
| X1–X4 main, retrieval, baseline, task/length analyses | Yes | Yes | Fully represented | Register and detailed objects cover each. |
| X5–X11 main ablations | Yes | Yes | Represented in compressed form | All conditions explained; exact unlabeled plot points not invented. |
| X12–X13 defense experiments | Yes | Yes | Fully represented | Condition-specific rates and inconsistencies retained. |
| X14–X20 appendix analyses | Yes | Yes | Fully represented | Specificity, attacker model, B, losses, libraries, humans, cost. |
| F1 | Yes, visually | Yes | Fully represented | Both pipelines and attack route. |
| F2 | Yes, visually | Yes | Fully represented | Prompt structure and output. |
| F3 | Yes, visually | Yes | Represented in compressed form | Both radar panels; exact unlabeled task rates unavailable. |
| F4 | Yes, visually | Yes | Represented in compressed form | Both length distributions; exact scale transform and summaries uncertain. |
| F5 | Yes, visually | Yes | Represented in compressed form | All eight panels; trends and reported anchors. |
| F6 | Yes, visually | Yes | Fully represented | Both methods and reported query-count effects. |
| F7 | Yes, visually | Yes | Represented in compressed form | All six panels and individual/unified distinction. |
| F8 | Yes, visually | Yes | Represented in compressed form | Four grouped conditions; exact bar heights not printed. |
| F9 | Yes, visually | Yes | Represented in compressed form | Both parameter panels; no invented exact coordinates. |
| F10 | Yes, visually | Yes | Represented in compressed form | All substantive generation requirements retained. |
| F11 | Yes, visually | Yes | Represented in compressed form | Format, relevance, length variation, JSON output. |
| F12 | Yes, visually | Yes | Fully represented | Both initializations and repeated tokens. |
| T1–T5 | Yes, visually and textually | Yes | Fully represented | Main rates, baseline rates, retrievers, component values. |
| T6 | Yes, visually and textually | Yes | Represented in compressed form | Eight row means, extremes, transfer exception; not all 64 cells repeated. |
| T7–T10 | Yes, visually and textually | Yes | Fully represented | All rates and defense distinctions retained. |
| T11 | Yes, visually and textually | Yes | Represented in compressed form | Definitions distributed between equations and glossary. |
| T12 | Yes, visually and textually | Yes | Fully represented | Target/non-target denominators and rates. |
| T13 | Yes, visually and textually | Yes | Represented in compressed form | Eight means, critical exception rows, weak-attacker range. |
| T14–T17 | Yes, visually and textually | Yes | Fully represented | All displayed numerical conditions retained. |
| E1–E4 | Yes, visually and textually | Yes | Fully represented | Retrieval, selection, prompt concatenation. |
| E5 | Yes, text-only | Yes | Fully represented | Overall objective; no visual-inspection claim. |
| E6–E8 | Yes, visually and textually | Yes | Fully represented | Retrieval surrogate and selection objectives. |
| E9–E14 | Yes, visually and textually | Yes | Fully represented | All loss terms, tokens, weights, notation uncertainty. |
| E15–E16 | Yes, visually and textually | Yes | Fully represented | Legitimate and malicious retrieval indicators. |
| ALG1 | Yes, visually and textually | Yes | Fully represented | Conceptual procedure and literal pseudocode ambiguities. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, algorithmic, empirical; priority not externally validated. |
| Authors' stated boundaries | Yes | Yes | Fully represented | Optimization difficulty, absent full appendix, controlled deployment scope. |
| A1 Symbols | Yes; opening text-only, table visual | Yes | Represented in compressed form | Symbol meanings preserved. |
| A2 Supplementary experiments | Yes, text and images | Yes | Fully represented | Every displayed experiment included. |
| A3 Prompt/dataset details | Yes, text and images | Yes | Represented in compressed form | Supplied templates included; absent detailed tasks flagged. |
| Footnote on corresponding authors | Yes | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Authorship and affiliations retained; contact formatting omitted. |
| Footnote on complete appendix | Yes | Yes | Fully represented | Missing technical-report material explicitly disclosed. |
| Technical report full appendix | No | No | Missing from supplied material | Attacker system prompt, full tasks, baseline Figure 16 examples. |
| Code, data, final payload collection | No | No | Missing from supplied material | Access plan described; files not supplied. |

### Missing or inaccessible material

The complete appendix of technical report [35], including the attacker model's full system prompt and target-task list, was not supplied. Baseline malicious-document examples referred to as Figure 16 of that report were not supplied. Code, raw experimental outputs, full optimized documents, and data-release files were not supplied. Page images for pp. 4, 13, 14, and 15 were not provided; those pages were read through extracted text only. There are no known missing pages within this supplied 18-page sequence.

### Uncertain interpretations

Small plots do not support exact transcription of every point, distribution summary, or bar height. Figure 4's precise axis transformation is unspecified. Table X's shared FPR formatting must not be expanded into invented separate rates. Equation (12), Equation (10)'s indexing, Algorithm 1's FLAG dimension, iteration variable, and final return contain ambiguities. Text–table mismatches concern detection rates and dynamic-library minima. The paper's 24% multiple-document increase is not explicitly classified as relative percent or percentage points. Exact implementation of output matching and AUC aggregation is absent.

### Deliberately compressed material

Repeated motivation and contribution statements are consolidated. Related work is summarized by methodological category rather than retelling every cited paper. The 75 references are accounted for but not individually reproduced. Tables VI and XIII are compressed to row means, extrema, and substantively important exceptions. Generation prompts are summarized rather than copied in full. Unlabeled plot coordinates and decorative icons are not transcribed as if they were numerical observations.

### Potential omissions

Every identified substantive section, subsection category, supplied figure, table, numbered equation, algorithm, experiment, contribution, and appendix component has a corresponding representation or explicit coverage limitation above. Exact matrix cells and plot coordinates deliberately compressed are not claimed to be individually preserved. Missing technical-report material could contain further substantive details that cannot be inventoried or assessed from this input. The analysis therefore provides comprehensive coverage of the supplied work without claiming complete coverage of its unavailable supplements or full experimental implementation.
