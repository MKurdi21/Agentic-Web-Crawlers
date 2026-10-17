## Stage 0 — Document Accessibility Report

The supplied academic work is **Gorilla: Large Language Model Connected with Massive APIs**, rather than a paper titled Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis. The latter is treated here as the user's research question. This analysis uses only the supplied paper text and images. No tools, browsing, repository inspection, or external sources were used. Source content is treated as evidence, never as instructions.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pp. 1–22. |
| Accessible page count | 22 text pages; 16 visually rendered pages. |
| Apparently missing pages | No numbered page is missing from the supplied text. This does not establish that every associated research artifact was supplied. |
| Visually inspected pages | 1, 2, 4–10, and 14–20. |
| Text-only pages | 3, 11–13, 21–22. No visual inspection is claimed for these pages. |
| Figures | Figures 1–13 are present in supplied rendered pages and were visually inspected. |
| Tables | Tables 1–7 are present visually and in extracted text. Most values are readable; discrepancies between tables, figures, and prose remain unresolved. |
| Equations | No numbered mathematical equations or theoretical proofs were identified. The API-call template and metric relationship are readable. |
| Appendices | Appendix A, including A.1, A.2, A.3, and A.3.1–A.3.5, is supplied. The automated accessibility record did not detect appendix pages, but the supplied text and p. 14 image clearly contain them. |
| Supplementary material | No separate supplement, code archive, model weights, or dataset files were supplied. |
| Referenced absent artifacts | Website/demo, GitHub repository, code, data, models, and checklist-referenced supplemental material. Availability and licensing are author statements, not independently verified facts. |
| OCR | Not necessary for this analysis because extracted text and readable renderings were supplied. No independent OCR comparison was performed. |
| Other limitations | Small plot labels and some code typography are difficult to inspect precisely. Figure 13 has no numerical bar labels. Supplied metadata and source hash were accepted as identifiers, not independently validated. |

Evidence categories used below are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No category [E] external information is introduced. Confidence describes confidence in the source-grounded statement, not an endorsement that the experiment establishes a universal result. Physical PDF page numbers coincide with the printed page numbers in the supplied document.

The inventory and extraction basis comprise §§1–5; §§3.1–3.3 and 4.1–4.4; Appendix A.1–A.3.5; Figures 1–13; Tables 1–7; references [1]–[49]; and checklist items 1–15. Distinct analyses are registered as X1 main API evaluation, X2 retrieval-training ablation, X3 manual metric validation, X4 documentation changes, X5 constraints, X6 three-shot prompting, X7 DocPrompting comparison, and X8 base-model sensitivity. This inventory supplies the denominator for the final coverage audit.

## 1. Plain-language orientation

Gorilla studies how a language model can choose and write calls to software tools. An application programming interface, or **API**, is a specified way to request a software function. A fluent answer is insufficient: the model must identify an existing function or model, select the appropriate provider, and supply the necessary arguments. The authors emphasize that tool catalogs are large, overlapping, and frequently updated. A model's stored training knowledge can therefore be incomplete or outdated. [A: pp. 1–2]

The researchers build **APIBench**, a collection of machine-learning API documentation and generated user instructions, and fine-tune a seven-billion-parameter LLaMA model into Gorilla. They train variants with and without reference documentation. Their **Retriever-Aware Training**, or **RAT**, is intended to help the model use relevant retrieved documentation while resisting irrelevant documentation. At inference, a retriever can attach one API document to the user's request. Gorilla then generates an API call. [A: §§3.1–3.2, pp. 4–5]

The strongest consistently supported result is improved API-call performance for the specialized Gorilla model in several evaluated conditions, especially without retrieval. Table 1 reports Gorilla zero-shot accuracy of 59.13% on Torch Hub, 71.68% on HuggingFace, and 83.79% on TensorFlow Hub. However, real retrieval can substantially reduce its accuracy, and Gorilla is not best in every table cell. The paper also demonstrates documentation-driven changes, tests accuracy constraints, and proposes structural API checking. [A/B: pp. 8–10]

Its central contribution is a combined training, dataset, and evaluation pipeline for API invocation. Its relevance to agent security is indirect: retrieved material can influence executable API choices, and correct API selection does not guarantee working surrounding code. **Analyst interpretation:** these are useful components of a security analysis, but the paper neither measures adversarial attacks nor directly compares web agents with standalone language models.

## 2. Document roadmap

The abstract and §1 introduce the problem and three main contributions. Figure 1 illustrates different API mistakes; Figure 2 previews the accuracy–hallucination tradeoff. Section 2 groups related work into language models, tool use, and program synthesis, then positions Gorilla against DocPrompting. Section 3 introduces the dataset, training/inference workflow, and structural API verification. [A: pp. 1–6]

Section 4 contains the evaluation. Section 4.1 compares models and retrievers and discusses training with retrieval; §4.2 gives documentation-change examples; §4.3 evaluates API selection subject to an accuracy constraint; §4.4 compares fine-tuning with three-example prompting. Section 5 concludes. References occupy pp. 11–13. [A: pp. 6–13]

Appendix A.1 expands dataset details; A.2 gives splits, hardware, and hyperparameters; A.3 and A.3.1–A.3.5 provide fuller performance plots, argument-checking rules, hallucination examples, manual validation, DocPrompting results, and base-model sensitivity. The NeurIPS checklist on pp. 21–22 adds important information: language-model experiments were performed once, artifacts are claimed to be open source, and no specific misuse safeguard is described. These checklist statements are part of the evidence rather than independent verification.

## 3. Background and context

A **large language model**, or **LLM**, generates language and code from a prompt. In this paper, the relevant output is a software invocation. An API call has a function name and arguments: for example, the supplied Torch Hub example identifies a repository and a model through `torch.hub.load`. Choosing a familiar-looking but nonexistent model counts differently from choosing an existing but unsuitable one. [A: pp. 5–6, 17]

**Fine-tuning** means additional training of a pretrained model using task-specific examples. **Instruction tuning** uses user-request/answer pairs. **Self-instruct** is the paper's process of generating additional instructions with a language model from a small set of examples. **In-context learning** supplies examples inside the prompt rather than updating model weights. Here, three-shot prompting means three examples in the input. [A: pp. 3–5, 10]

**Retrieval** finds documentation to accompany a request. BM25 is a named retrieval baseline; the supplied work does not explain its scoring formula. GPT-Index uses the named OpenAI embedding model with 1,536-dimensional document representations. An **oracle retriever** supplies the correct reference document and is used as an idealized condition. The paper calls inference without a retriever **zero-shot**; this does not mean Gorilla lacked task-specific training. [A: pp. 6–7]

An **abstract syntax tree**, or **AST**, represents the structure of code. Gorilla's evaluator checks selected API names and arguments against a database. Its hallucination metric concerns API calls absent from that database, rather than every possible factual, semantic, runtime, or security failure. **Reinforcement learning from human feedback**, or **RLHF**, is mentioned in characterizing conversational baselines and speculating about hallucination differences; its causal contribution is not experimentally isolated. [A: pp. 6–8]

Related-work claims remain attributed to the authors. They describe earlier tool systems as often focused on particular tools or prompting, whereas Gorilla targets systematic training and evaluation across many API entries. They distinguish DocPrompting by dataset content, constraint-related metadata, structural evaluation, and instruction tuning. The cited works themselves were not supplied and were not independently reviewed. [A: §2, p. 3]

## 4. Research problem and gap

**Existing problem:** LLMs may not know which APIs exist or how current versions should be invoked. Many APIs overlap in purpose but differ in arguments, performance, and other restrictions. [A: pp. 1, 4–5]

**Shortcomings attributed to previous approaches:** prompting general models can produce nonexistent tools or wrong arguments; limited-tool demonstrations do not establish a broad API training/evaluation pipeline; conventional testing is difficult when multiple API choices can satisfy a task; and text-oriented metrics may fail to capture the API structure the authors care about. [A: pp. 2–3, 5–6]

**Research gap:** the authors seek a scalable connection between natural-language instructions, API documentation, specialized training, and API-specific evaluation. They also want adaptation to changed documentation without having to retrain whenever an API changes. [A: §§1–3]

**Motivation:** improve practical reliability when translating user goals into software calls. **Scope:** the actual benchmark centers on machine-learning model hubs and individual API calls. References to millions of tools, RESTful APIs, SQL, and flexible interfaces describe motivation or potential extension; they are not demonstrations over those broader environments. [A: pp. 1–5, 10]

**Research-question relevance [D]:** a security review can use this paper to identify documentation-to-action dependencies and evaluation gaps. It cannot use Gorilla's accuracy numbers as attack-success rates or as proof that web agents are more vulnerable than standalone LLMs.

## 5. Research questions / objectives / hypotheses

The paper explicitly lists three evaluation questions on p. 6:

- **RQ1:** How does Gorilla compare to other LLMs on the APIBench test set? Addressed primarily by X1, Table 1, and Figures 5, 10, and 11.
- **RQ2:** How well does Gorilla adapt to test-time changes in API documentation? Addressed by X4, Figure 6, and §4.2.
- **RQ3:** How well can Gorilla handle questions with constraints? Addressed by X5, Table 4, and §4.3.

Additional explicit experimental objectives are understanding retrieval during training, comparing fine-tuning with three-shot prompting, validating the AST metric against human judgments/execution, comparing with DocPrompting, and checking sensitivity to the pretrained base model. [A: pp. 7–10, 17–20]

No formal null hypotheses, preregistered hypotheses, statistical power targets, or significance thresholds are supplied. Statements that RAT improves adaptation and hallucination are author claims evaluated through the listed analyses, not formal statistical hypotheses. The requested web-agent security question is an external organizing question supplied by the user, not an experimental question posed by this paper.

## 6. Assumptions / threat model

There is **no explicit adversarial threat model**. The paper specifies no attacker, attacker-controlled website, injection strategy, secret asset, privilege boundary, or attack-success metric. It evaluates routine API invocation rather than malicious manipulation. [D: assessment of supplied methods and experiments]

Operationally, the system assumes an API database, reference documentation, a natural-language request, and a model that can map the request to an API call. Retrieval can be inaccurate. RAT is intended to teach the model to judge relevance and use stored domain knowledge when the retrieved document is irrelevant. Relevant documentation can legitimately change the selected API. [A: p. 5]

The evaluator assumes that checking designated API arguments against the collected database is an appropriate proxy for the desired API behavior. Optional arguments can be ignored. HuggingFace coverage is explicitly nonexhaustive, and most non-Gorilla models receive domain-level evaluation there. These assumptions limit the interpretation of cross-model comparisons and of the term hallucination. [A: pp. 6–7, 17]

**Security interpretation [D]:** documentation appended to a model input is an influence channel, while generated API calls are a potential action interface. This architecture suggests a place to investigate malicious influence, but no evidence here establishes exploitation. Irrelevant benign documents and adversarial instructions are different experimental conditions. An oracle document is correct by construction; it is not a security assurance about a real retrieval source.

## 7. Methodology

### Dataset construction

The authors collect model cards from HuggingFace, PyTorch/Torch Hub, and TensorFlow Hub. HuggingFace reportedly hosted about 203,681 models. The authors select top models by domain to reduce poorly documented entries, describing 7 multimodal, 8 computer-vision, 12 natural-language, 5 audio, 2 tabular, and 2 reinforcement-learning domains, and report 925 retained models. TensorFlow Hub v2 reportedly contains 801 models before filtering and 626 afterward. The main prose reports 95 Torch Hub models. [A: §3.1, p. 4]

Important inconsistencies are preserved. Figure 3 gives 94 Torch Hub entries and a total of 1,645 API calls. Main-text components 95 + 626 + 925 equal 1,646 [C], whereas 94 + 626 + 925 equal 1,645 [C]. Appendix A.1 gives 696 Tensor Hub APIs, alongside 95 Torch Hub and 925 HuggingFace APIs. These cannot all describe the same exact collection without additional explanation, which is absent. [A/B/C: pp. 4, 14]

Each API card is converted to fields for domain, framework, functionality, API name, call, arguments, environment requirements, example code, performance, and description. These metadata are intended to support selection beyond simple function naming, including parameter and accuracy restrictions. The study does not demonstrate the claimed generalization of this representation to all other API domains. [A: p. 4]

### Instruction generation and formatting

GPT-4 generates instructions from reference API documentation and three in-context examples. The authors instruct it not to include API names or hints in user instructions. There are six manually constructed instruction–API examples per hub, eighteen total, described as the only hand-generated or modified data for this generation process. Ten instruction–API pairs are generated for each of the reported 1,645 APIs; Figure 3 labels 16,450 pairs. Later manual dataset cleanup for evaluation is also disclosed, so the eighteen-example statement should not be extended to mean no manual processing anywhere. [A: pp. 4, 17]

Training uses one user turn and one assistant turn per example. Gorilla is based on LLaMA-7B. Variants are trained without retrieval and with reference documentation. RAT appends documentation to the prompt while preserving the correct answer as the target. The general explanation allows imperfect or irrelevant documents, but the specific Table 2 training experiment uses a ground-truth oracle document. This distinction matters: the paper does not fully enumerate the corruption/relevance distribution for every training condition. [A: pp. 5, 7–8]

### Inference and retrieval

Without retrieval, only the request is supplied. With retrieval, BM25 or GPT-Index returns the top-one API document, which is concatenated with the request using a reference-document instruction. GPT-Index uses `text-embedding-ada-002-v2` and 1,536-dimensional embeddings. Oracle retrieval supplies the relevant document. No further prompt tuning is reported beyond the concatenation. An API execution system was implemented, but execution is explicitly outside the paper's main focus. [A: pp. 5–7]

### Splits, training, and hardware

Appendix A.2 reports a 90%/10% training/evaluation split for HuggingFace and 80%/20% training/test splits for Torch Hub and Tensor Hub. Page 7 says the generated instruction–API pairs are divided into training and test sets. The supplied material does not establish API-disjoint splitting, exact example counts after each split, or whether all instructions for an API stay together. Training uses five epochs, learning rate 2e-5 with cosine decay, batch size 64, warmup ratio 0.03, weight decay 0, maximum sequence length 2,048, and eight A100 GPUs with 40 GB memory each. [A: pp. 7, 14–15]

### Baselines and metrics

Baselines are LLaMA-7B, GPT-4 checkpoint `gpt-4-0314`, GPT-3.5-turbo checkpoint `gpt-3.5-turbo-0301`, and Claude checkpoint `claude-v1`. Three-shot comparisons involve GPT-3.5 and GPT-4. A separate DocPrompting comparison uses 7B models with the same epochs and learning rate. [A: pp. 6, 10, 18]

AST matching checks API identities and selected arguments. Torch Hub checks `torch.hub.load`, `repo_or_dir`, and `model`; Tensor Hub checks `hub.KerasLayer` or `hub.load` with `handle`. HuggingFace generally requires `pretrained_model_name_or_path`, except for `pipeline`, where the task may select a model automatically. A nonexistent database API is hallucination; a real but wrong API is an error. Accuracy, hallucination, and error are intended to partition outcomes. [A: pp. 6, 17]

For HuggingFace, §4.1 says non-Gorilla models are checked only for correct domain names, unlike Gorilla. This is a major comparability qualification. Statistical tests, confidence intervals, error bars, and multiple training runs are not reported; checklist item 7 states LLM experiments were performed once because of GPU costs. [A: pp. 7, 21]

## 8. Experiments / analyses

### X1 — Main model and retriever comparison

Purpose: answer RQ1. Manipulated conditions are model and retrieval setting: none, BM25, GPT-Index, or oracle. Outcomes are accuracy, hallucination, and wrong-API error across three hubs. Table 1 contains twenty model/setting rows and nine metric columns. Gorilla without retrieval records 59.13/71.68/83.79% accuracy for Torch/HuggingFace/TensorFlow and 6.98/10.95/5.40% hallucination. Corresponding GPT-4 accuracies are 38.70/19.80/18.20%; GPT-3.5 accuracies are 48.38/16.81/41.75%. [A/B: p. 8]

The retrieval story is conditional. Gorilla BM25 accuracies are 40.32/17.03/41.89%, all below its no-retrieval values. GPT-Index gives 61.82/47.46/64.96%; oracle gives 67.20/91.26/94.16%. GPT-3.5 exceeds Gorilla on TensorFlow under GPT-Index, 65.59 versus 64.96%, and oracle, 95.03 versus 94.16%. Under HuggingFace BM25, GPT-3.5 scores 17.26% versus Gorilla's 17.03%. Thus universal superiority is not supported. [A/B: Table 1]

### X2 — Retrieval-aware training ablation

Purpose: separate training with documentation from merely attaching documentation at test time. Table 2 crosses two Gorilla training variants with four inference settings. For the no-retriever-trained model, Torch accuracies are 59.13, 37.63, 60.21, and 54.83%; HuggingFace 71.68, 11.28, 28.10, and 45.58%; TensorHub 83.79, 34.30, 52.40, and 82.91%. Columns are none, BM25, GPT-Index, oracle. [A/B: p. 8]

For the oracle-retriever-trained model, the same sequences are Torch 0, 40.32, 61.82, 67.20%; HuggingFace 0, 17.04, 47.46, 91.26%; TensorHub 0, 41.89, 64.96, 94.16%. No-document evaluation of this model yields 100%, 99.67%, and 100% hallucination, respectively. This is strong evidence of dependence on the training/inference input condition. It does not show a malicious attack. The paper's improvement claims of 12.37 and 23.46 correspond to particular oracle-to-oracle differences, detailed below. [A/B/C: pp. 7–8]

### X3 — Manual validation of the AST metric

One hundred randomly selected Gorilla generations are checked. AST API accuracy and human API judgment both equal 78%; 72% of complete generated programs execute successfully. The authors report that AST-incorrect cases match manually incorrect cases. They attribute the six-point gap between API correctness and execution to surrounding code or other factors outside the API call. Figure 12 illustrates an invalid `zip` over a scalar score. No confidence interval or detailed sampling distribution is supplied. [A: pp. 8–9, 17, 19]

### X4 — Documentation changes

Purpose: answer RQ2. Figure 6 changes documentation for background-removal calls from FCN ResNet-50 to ResNet-101, and from one model repository to another. Outputs change accordingly. The text says an unfamiliar ResNet-60 reference is rejected in favor of the familiar ResNet-50. This is qualitative evidence of selective documentation responsiveness, not a quantified benchmark of arbitrary API changes. Counts, success rates, and calibration measures are absent. [A/B: p. 9]

### X5 — Constraint-aware API selection

Purpose: answer RQ3. The authors retain Torch Hub models with an accuracy metric for at least one dataset, reporting 65.26% of the original Torch Hub dataset. They test requests with an accuracy constraint. Their illustration requests at least 80% ImageNet top-one accuracy: ResNeXt-101 32x16d is reported at 84.2%, whereas MobileNetV2 is 71.88%. The study's outcome is selection satisfying the constraint; those are model-card values, not newly measured classification performance. [A: p. 10]

Table 4 distinguishes ordinary overall API selection from `Accuracy const`. Gorilla constraint accuracies are 47.88, 30.28, 26.76, and 67.60% across none/BM25/GPT-Index/oracle. GPT-3.5 scores 43.66, 33.80, 33.09, and 69.01%; GPT-4 scores 43.66, 29.57, 29.57, and 59.15%; Claude scores 17.25, 29.57, 31.69, and 69.71%; LLaMA scores 0, 6.33, 3.52, and 17.60%. Gorilla leads without retrieval but not under every retrieval condition. [A/B: p. 9]

### X6 — Fine-tuning versus three-shot prompting

Table 5 compares Gorilla without examples to GPT models with zero or three examples. Three-shot GPT-4 accuracy is 26.32% HuggingFace, 75.80% Torch, and 77.37% TensorFlow; the Gorilla row is 58.05, 75.80, and 83.79%. Gorilla ties GPT-4 on Torch accuracy and leads in the other two columns. Its Torch hallucination, 16.12%, exceeds GPT-4 three-shot's 13.44%. Table 5 differs materially from Table 1, and one GPT-3.5 row is internally problematic; those discrepancies are not repaired here. [A/B: p. 10]

### X7 — DocPrompting comparison

Table 7 reports HuggingFace accuracy 61.72% for DocPrompting and 71.68% for Gorilla; hallucination 17.36% and 10.95%, respectively. The comparison controls model size at 7B, epoch count, and learning rate according to the text. Further implementation and run-variance details are not supplied. [A: p. 18]

### X8 — Base-model sensitivity

Figure 13 compares Gorilla-LLaMA, Gorilla-MPT, and Gorilla-Falcon on the same HuggingFace training/evaluation dataset. The first two bars are visually near 71–72%, and Falcon near 64–65%; these are approximate visual estimates, not exact reported values. The authors claim convergence within a few percentage points. The plot suggests some base-model dependence remains, and no numeric labels or error bars support a precise gap calculation. [A/B: pp. 18, 20]

## 9. Results

The main positive result is specialized fine-tuning's strong no-retriever performance in Table 1. For Torch Hub, Gorilla's 59.13% minus GPT-4's 38.70% equals **20.43 percentage points** [C]; relative to GPT-3.5, 59.13 − 48.38 equals **10.75 points** [C]. The prose calls these percentages, but the arithmetic is an absolute point difference. They are not relative percentage improvements. The claimed improvement as large as 83% over LLaMA appears consistent with an approximately 83.79-point TensorFlow gap over zero, but the prose does not specify its exact aggregation. [A/C: pp. 7–8]

Retrieval reduces some hallucination rates while increasing wrong-API errors. For Gorilla on Torch, moving from no retrieval to BM25 changes accuracy from 59.13 to 40.32%, hallucination from 6.98 to 4.30%, and wrong-API error from 33.87 to 55.37%. Fewer imagined APIs therefore do not imply more useful API selection. [A/B: Table 1]

Oracle-trained Gorilla benefits substantially from correct documentation: Table 2's oracle-inference Torch values are 54.83% without retriever-aware training versus 67.20% with it, a **12.37-point** difference [C]. HuggingFace gives 91.26 − 45.58 = **45.68 points** [C], whereas the prose's 23.46 figure equals 91.26 − 71.68, comparing oracle-trained/oracle-tested with no-retriever-trained/no-retriever-tested. The two reported improvement examples therefore do not use a uniform baseline. [A/C: pp. 7–8]

The prose's 29.20% GPT-Index degradation and 52.27% BM25 degradation can be reproduced on oracle-trained TensorHub as 94.16 − 64.96 = 29.20 points and 94.16 − 41.89 = 52.27 points [C]. They should not be generalized into a benchmark-wide relative degradation. Oracle-trained HuggingFace gives other gaps, so the conditions matter. [A/C: Table 2]

Manual validation supports AST as a limited API-identity proxy: 78% AST accuracy matches 78% human API accuracy on 100 sampled outputs, while end-to-end execution reaches 72%. The result does not show that AST certifies a complete program, user-goal completion, absence of vulnerabilities, or safe execution. [A/D: pp. 8–9, 17]

Constraint handling is partial. Gorilla's 47.88% no-retriever constraint accuracy leads the listed no-retriever baselines, but oracle Claude reaches 69.71%, exceeding Gorilla's oracle 67.60%. On ordinary overall API selection in Table 4, Claude's GPT-Index 82.39% exceeds Gorilla's 71.83%; overall and constraint accuracy must remain separate. [A/B: p. 9]

## 10. Figure-by-figure interpretation

### Figure 1 — Contrasting API responses, p. 2

Three vertically arranged code examples answer a speech-to-text request using Torch Hub. Gorilla is labeled correct; GPT-4 is labeled API argument hallucination; Claude is labeled incorrect API call. Colored code and a yellow highlight draw attention to arguments, especially `source='local'`. There are no axes, units, statistical samples, or uncertainty bars. The figure illustrates the authors' failure categories, but it is one curated example, not a frequency estimate. The caption says GPT-4 presents a nonexistent model and Claude selects an incorrect library. The code examples were inspected, not executed. [A/B]

### Figure 2 — Accuracy versus hallucination overview, p. 2

Four scatterplot panels represent no retriever, BM25, GPT retrieval, and oracle retrieval. Horizontal position is hallucination; vertical position is accuracy, on percentage-like 0–100 scales. Named colored points distinguish LLaMA, GPT-3.5, GPT-4, Claude, and Gorilla. A directional annotation indicates that moving upward and leftward is better. Gorilla generally occupies a favorable region, especially without retrieval, but no exact per-hub attribution should be inferred from this compact preview alone. Table 1 and Figure 11 provide the more explicit conditions. No error bars are visible. [B]

### Figure 3 — Training and inference architecture, p. 4

The upper flow moves from model-card collections to JSON records, then self-instruct generation of 16,450 instruction–API pairs, and Gorilla-7B training. The lower flow takes a user image-generation request, queries an API database through a retriever, and supplies a reference API to Gorilla; the output leads to a generated image. A separate zero-shot path bypasses retrieval. Arrows convey data flow, not a measured feedback loop. The diagram includes 94 Torch Hub entries, conflicting with the prose's 95. The execution image illustrates capability; it does not establish a broad execution benchmark. [A/B]

### Figure 4 — API subtree matching, p. 6

The left side decomposes a Torch Hub DenseNet call. The right side branches through API namespaces, repositories, model names, and optional pretrained settings. Green nodes highlight the matching path. The set-membership-style symbol visually links candidate structure to the database. The match depends on `torch.hub.load`, repository, and model; `pretrained=True` is optional and not checked in the example. This diagram explains selective structural validation, not validation of all program behavior. [A/B]

### Figure 5 — GPT-retriever accuracy, p. 7

Three bar panels show Torch Hub, HuggingFace, and TensorFlow Hub. The vertical axis is accuracy in percent, extending to 100; horizontal categories are GPT-3.5, GPT-4, Claude, LLaMA, and Gorilla. Blue/orange/purple/red/green distinguish models; a dotted separator marks the closed-source grouping. Torch values are 60.21, 59.13, 60.21, 14.51, 61.82. HuggingFace labels are 47.34, 44.57, 41.37, 10.17, 47.45. TensorFlow values are 65.59, 43.94, 55.62, 15.62, 64.96. These show a small Torch lead for Gorilla and a TensorFlow lead for GPT-3.5. HuggingFace numbers differ from Table 1 for several models. No statistical equivalence test supports the caption's language of matching performance. [A/B]

### Figure 6 — Documentation-driven API changes, p. 9

Three side-by-side rounded text panels show default response, updated model, and updated repository. The requested task stays background removal while retrieved references and output calls change. ResNet-50 becomes ResNet-101 in the middle; the right panel changes repository while using ResNet-50. There are no quantitative axes. This is direct visual evidence that reference material can alter generated API identity, not proof of arbitrary update generalization or adversarial robustness. [A/B]

### Figure 7 — Domain lists, p. 15

Three bordered blocks list task domains for Torch Hub, Tensor Hub, and HuggingFace. Torch's six visible categories include classification, segmentation, detection, audio separation, video classification, and text-to-speech. The other lists cover image, text, audio, video, tabular, and reinforcement-learning tasks. Their purpose is dataset breadth, not a distribution plot: no counts per domain are shown. The caption calls Tensor Hub the smallest dataset, conflicting with the supplied API counts, which make Torch Hub smallest. Exhaustive domain-name transcription is compressed; category breadth and this conflict are retained. [A/B]

### Figure 8 — Dataset records, p. 16

Two large text boxes show a no-retriever TensorFlow object-detection example and a Torch Hub example with a detailed HybridNets reference document. Fields include domain, API call, provider, explanation, and code. The reference contains environment and performance metadata. The examples show how user language and structured documentation enter the training format. Performance values inside the HybridNets card are metadata about that referenced model, not Gorilla benchmark results. The examples do not establish that every supplied code fragment was executed. [A/B]

### Figure 9 — HuggingFace hallucination examples, p. 17

Three code boxes show a placeholder model identifier and two other model/task combinations presented as GPT-4 hallucination examples. No rates, axes, or comparisons are plotted. The figure supports the authors' qualitative description of invalid API/model arguments. Whether every call is invalid under every external library version was not checked, because this is closed-document analysis. [A/B]

### Figure 10 — Full accuracy grid, p. 18

Twelve bar panels cross three hubs with four retriever settings. Horizontal categories are the five models; vertical axes show accuracy, generally from 0 to 100. Colors remain model-specific. The grid makes Gorilla's no-retriever advantage clear and shows that oracle retrieval helps several models strongly. It also shows GPT-3.5 above Gorilla in TensorFlow oracle accuracy, 95.03 versus 94.16%, contradicting the caption's unqualified statement that Gorilla remains best with the oracle. Minor numerical differences from Table 1 are preserved in the consistency discussion. No error bars appear. [A/B]

### Figure 11 — Full accuracy–hallucination grid, p. 19

Twelve scatterplots use the same hub-by-retriever organization. Horizontal axes are hallucination, vertical axes accuracy, with linear 0–100 scales. Colored labeled points identify models. Gorilla's no-retriever points are high and far left relative to most baselines. Real retrievers can move points toward lower hallucination without maximizing accuracy. The panels largely repeat Table 1, so their exact coordinates are not separately estimated from pixels. No confidence intervals or significance markers are visible. [B]

### Figure 12 — Correct API, broken supporting code, p. 19

A code listing loads a sentiment-analysis pipeline, extracts a label and scalar score, then attempts to iterate with `zip(sentiments, scores)`. The paper identifies the scalar score as noniterable. The API call can be correct while this surrounding operation fails. There are no axes or numerical outcomes in the listing. Its importance is conceptual: API-identity success and end-to-end program success are different outcomes. [A/B]

### Figure 13 — Base-model sensitivity, p. 20

Three bars show Gorilla-LLaMA, Gorilla-MPT, and Gorilla-Falcon for zero-shot HuggingFace accuracy. The vertical axis is accuracy with ticks at intervals of ten; the horizontal axis names pretrained models. Purple and green bars are near 71–72%, the blue bar near 64–65%. These are **approximate visual estimates**. Values are not printed above bars, and no error bars are shown. The plot supports performance on multiple bases, but not exact equality or a statistically characterized robustness margin. [A/B]

## 11. Table-by-table interpretation

### Table 1 — Model/retriever comparison, p. 8

Rows are five models crossed with four retrieval conditions. Each hub has overall accuracy, hallucination, and wrong-API error, all percentage values. Arrows indicate higher accuracy and lower errors are preferred. Gorilla's accuracy sequences across none/BM25/GPT-Index/oracle are Torch 59.13/40.32/61.82/67.20; HuggingFace 71.68/17.03/47.46/91.26; TensorFlow 83.79/41.89/64.96/94.16. LLaMA is weakest in many conditions, including zero accuracy without retrieval. Gorilla has zero Torch hallucination under GPT-Index and oracle, but still has wrong-API errors of 38.17 and 32.79%. Thus zero hallucination is not perfect accuracy. HuggingFace evaluation differs across models. Values are point estimates without significance notation or error measures. All 180 metric cells were considered as the comparison grid; repetitive cells are not reproduced individually.

### Table 2 — Training/inference retrieval interaction, p. 8

Two training blocks each have four inference columns. Rows give accuracy and hallucination for all three hubs. The strongest methodological lesson is distribution dependence: oracle-trained Gorilla performs at zero accuracy without documentation, while no-retriever-trained Gorilla can perform well without it. Properly matched oracle training and testing improves outcomes, but realistic retrieval remains a bottleneck. The HuggingFace BM25 value 17.04 differs from Table 1's 17.03. The table has no error bars or run variance. Full accuracy sequences appear in X2; hallucination patterns are compressed after preserving the catastrophic no-document condition and key comparisons.

### Table 3 — AST, human judgment, execution, p. 9

Three rows report 0.78 AST accuracy, 0.78 human API accuracy, and 0.72 executable-code rate on the sampled generations. These are proportions, equivalent to 78%, 78%, and 72%. The caption describes strong correlation, but no correlation coefficient is given; matching aggregate accuracies alone should not be mistaken for a reported statistical correlation coefficient. The accompanying prose adds matching incorrect cases. The sample is 100, and no uncertainty interval appears.

### Table 4 — Constraint-aware invocation, p. 9

Models are grouped across no retrieval, BM25, GPT-Index, and oracle. Rows distinguish overall API accuracy, hallucination, wrong-API error, and accuracy satisfying the constraint. Units are percentages. Gorilla's no-retriever constraint score, 47.88%, exceeds GPT-3.5 and GPT-4 at 43.66%. The highest listed constraint value is Claude oracle at 69.71%, followed by GPT-3.5 oracle 69.01% and Gorilla oracle 67.60%. BM25 and GPT-Index do not consistently improve constraint compliance. Ordinary API accuracy must not substitute for the constraint metric. No statistical information is supplied.

### Table 5 — Zero-shot fine-tuning versus three-shot prompting, p. 10

Rows compare GPT-3.5/GPT-4 without examples, the same models with three examples, and Gorilla without examples. Columns pair accuracy and hallucination for each hub. Gorilla ties three-shot GPT-4 at 75.80% Torch accuracy; GPT-4 has lower Torch hallucination, 13.44 versus 16.12%. Gorilla leads the listed three-shot models in HuggingFace and TensorFlow accuracy. However, the Gorilla HuggingFace and Torch values differ from Table 1. GPT-3.5 three-shot Torch accuracy 73.11 and hallucination 72.58 sum to 145.69% [C], incompatible with the paper's mutually exclusive outcome definition if both use the same denominator. No correction is inferred.

### Table 6 — Training hyperparameters, p. 15

This two-column table reports learning rate 2e-5, batch size 64, five epochs, warmup ratio 0.03, weight decay 0, and maximum sequence length 2,048. The text adds cosine decay and eight A100 40 GB GPUs. Optimizer identity, random seeds, elapsed training time, and a hyperparameter search procedure are not specified in the supplied table or accompanying training paragraph. The checklist's broad reproducibility assertion does not supply those details.

### Table 7 — DocPrompting comparison, p. 18

The table compares accuracy and hallucination on HuggingFace. Gorilla improves accuracy from 61.72 to 71.68% and lowers hallucination from 17.36 to 10.95%. Derived differences are +9.96 and −6.41 percentage points. The comparison text reports equal model scale, epochs, and learning rate. It does not provide repeated-run uncertainty or a full reproduction recipe within this small comparison. These results establish a reported advantage in this condition, not universal superiority over every documentation-based coding approach.

## 12. Diagram / architecture interpretation

Figure 3 is the main system diagram. Its training path begins with documentation from three hubs, converts it into structured records, uses self-instruct to pair user requests with API answers, and fine-tunes Gorilla. Its inference path begins with a user goal. In retrieval mode, a retriever queries the API database, and one reference document joins the user prompt. The model outputs the API call. The illustration continues to execution, but the paper separates that execution capability from its main evaluation. [A/B: pp. 4–5]

The zero-shot path bypasses the retrieval component. This architectural choice produces two forms of dependency: knowledge stored in model parameters and knowledge supplied in the current prompt. Table 2 shows that a model trained to expect the second source may fail when it is removed. **Analyst interpretation:** training and deployment input formats therefore matter as much as simply deciding to add a retriever.

Figure 4 is an evaluation diagram rather than a runtime planner. It maps an output call into a path through allowable API structure and checks selected nodes. It does not represent an agent loop, authorization process, sandbox, or security policy. Figure 6 is a controlled input/output comparison showing changes in selected call components; it contains no feedback loop or iterative learning. These distinctions prevent interpreting simple data-flow arrows as evidence of a fully autonomous web agent.

## 13. Equations and mathematical concepts

No numbered optimization objective, loss equation, theorem, lemma, or proof is provided in the supplied work. Standard instruction fine-tuning is named, but its exact training loss is not written out. No missing formula is supplied from outside knowledge.

The principal metric relationship is stated verbally on p. 6:

`accuracy + hallucination + error = 1`

This means the authors intend each evaluated API output to belong to one of three mutually exclusive categories: correct API, imagined/database-absent API, or existing but wrong API. With percentage units, the corresponding sum is 100%. Small deviations can result from displayed rounding; large violations require explanation. The Table 5 GPT-3.5 example is a large violation if the columns share this definition and denominator. [A/C]

Appendix A.3.1 gives the call template `API_name(API_arg1, API_arg2, ..., API_argk)`. Here `API_name` identifies a callable, the argument placeholders denote its inputs, and `k` indexes the last shown argument. This is structural notation, not a numerical model. The evaluator can choose which arguments to check. Ignoring an optional argument narrows what a successful match establishes. [A: p. 17]

Derived comparisons in this report use percentage-point subtraction. For example, 71.68% − 61.72% = 9.96 percentage points for Gorilla versus DocPrompting. Relative improvement would divide that difference by the baseline, but no such extra relative figure is needed here. The sample-based execution gap is 78% − 72% = 6 percentage points; it is not a six-percent relative drop. [C]

## 14. Interpretation and discussion

RQ1 receives substantial empirical evidence within the selected benchmark: specialized fine-tuning can outperform the specified general-model checkpoints on API selection. However, retrieval condition, hub, and scoring rule change the answer. The evidence supports conditional performance advantages rather than a universal model ranking. HuggingFace's asymmetric scoring and internal numerical discrepancies reduce confidence in broad cross-model magnitude claims. [A/D]

RQ2 receives qualitative support. Gorilla changes an API component or source when given a relevant updated reference, while the text describes rejecting an unfamiliar backbone. The work does not quantify the boundary between helpful novelty and rejected novelty. Its language about remaining reliable irrespective of documentation changes is stronger than the demonstrated case set. [A/D: p. 9]

RQ3 receives evidence of partial constraint handling. Gorilla leads no-retriever constraint accuracy, but more than half of those requests still fail the constraint metric, and several oracle baselines exceed it. Selection under a metadata threshold is demonstrated; general multi-constraint optimization, live resource measurement, and guaranteed compliance are not. [A/D: pp. 9–10]

Several consistency problems materially affect interpretation:

| Issue | Conflicting evidence | Assessment |
|---|---|---|
| API counts | Figure 3: 94 Torch; prose/A.1: 95. Main TensorFlow: 626; A.1: 696. | Exact dataset size unresolved. |
| Domain totals | Main HuggingFace category counts sum to 36 [C]; A.1 says 37. | Domain taxonomy/version not reconciled. |
| Smallest hub | Figure 7 caption says Tensor Hub smallest; reported API counts make Torch smallest. | Caption conflicts with counts. |
| Main versus prompting table | Gorilla HF accuracy 71.68 in T1 versus 58.05 in T5; Torch 59.13 versus 75.80. | Conditions/version differences not adequately explained. |
| T5 outcome partition | GPT-3.5 three-shot Torch 73.11 accuracy and 72.58 hallucination. | Cannot both be exclusive percentages of the same outcomes. |
| Figure 5 versus T1 | GPT-3.5 HF 47.34 versus 29.08; Gorilla 47.45 versus 47.46. | Major and minor differences coexist; no silent selection. |
| Oracle superiority | Figure 10 caption says Gorilla best; TensorFlow GPT-3.5 95.03 exceeds 94.16. | Universal caption claim contradicted. |
| Training description | General RAT allows irrelevant references; X2 uses oracle documents. | General mechanism and tested training condition must remain distinct. |

The authors speculate that RLHF could explain GPT-3.5's hallucination behavior. Table 1 does not establish a causal RLHF effect, and even the asserted all-settings ordering has exceptions: Torch oracle GPT-4 hallucination is 0.53% versus GPT-3.5's 1.60%. This speculation should not be promoted into a demonstrated explanation. [A/B/D: p. 8]

## 15. Contributions and novelty

**System contribution [A]:** Gorilla connects natural-language requests, API metadata, retrieval, and specialized generation. The authors call it the first system for large-scale API integration; priority is an author claim, not externally verified here. [p. 2]

**Methodological contribution [A]:** RAT trains with documentation in the prompt and is intended to help judge its relevance and accommodate test-time changes. The training/inference cross-condition experiment is particularly informative because it exposes both gains and strong input dependence. [pp. 5, 7–8]

**Dataset/benchmark contribution [A]:** APIBench collects documentation from three hubs, enriches records with metadata, and generates instruction–API pairs. The reported exact counts conflict, but the three-source structure and synthetic-instruction strategy are clear. [pp. 4, 14–16]

**Evaluation contribution [A]:** selected-argument AST matching separates database-absent API hallucination from existing-but-wrong API selection. The 100-output manual check provides limited validation of API identification, not full execution correctness. [pp. 6, 8–9, 17]

**Empirical contribution [A]:** model/retriever comparisons, training ablation, prompting comparison, constraint study, documentation-change examples, DocPrompting comparison, and base-model plot. There is no new theorem, formal security proof, or measured web-agent vulnerability contribution in the supplied work.

## 16. Limitations

### Authors' stated limitations

The authors explicitly report that retrieval can hurt performance. They acknowledge imperfect retrieval, nonexhaustive HuggingFace coverage, and the difficulty of executing every generated program given dependency, software-kernel, and hardware requirements. They focus on one API call and state that API execution is not the paper's focus. Appendix A.1 deprioritizes testing execution of the dataset's example code and leaves that for future work. These statements coexist with the narrower 100-generation manual execution study; neither should erase the other. [A: pp. 5, 7–8, 14, 17]

Checklist item 7 states that language-model experiments were run once because of GPU cost. The paper therefore does not characterize run-to-run variation. The checklist marks limitations discussed but does not provide a separate extensive limitations section. [A: p. 21]

### Additional evidence-based analyst observations

[D] Dataset counts, results, captions, and metric columns contain unresolved inconsistencies. Exact reproducibility and uniform ranking claims are consequently less secure than the broad pipeline description. Generated instructions and GPT-4-produced targets may not represent independently authored user workloads. The disclosed split does not establish API-disjoint generalization. HuggingFace scores use different criteria for Gorilla and other models. Documentation adaptation is illustrated rather than evaluated through a clearly sized challenge set. AST success cannot certify dependency integrity, authorization, security, or correct surrounding code. None of these observations is presented as an author-admitted security result.

## 17. Threats to validity

These validity categories are analyst labels, not headings used by the authors.

**Internal validity [D]:** comparisons depend on training format, retrieval quality, scoring rules, and potentially inconsistent result versions. The oracle-trained model's failure without documentation shows an input-distribution effect that must be separated from claims about general model competence.

**Construct validity [D]:** AST accuracy measures selected API structure; hallucination means database absence. Neither equals user-goal success or secure behavior. The demonstrated 78% API accuracy versus 72% execution rate makes this distinction concrete. Constraint success is based on supplied model-card metadata rather than fresh evaluation of the selected model.

**External/ecological validity [D]:** three ML model hubs, synthetic requests, top-one retrieval, and single-call generation do not establish performance on open-web browsing, multi-step autonomous workflows, authenticated applications, or adversarial pages. The evaluated historical checkpoints should be identified precisely rather than generalized to all LLMs.

**Statistical conclusion validity [D]:** single runs, no error bars, and no confidence intervals make small gaps such as 47.46 versus 44.58% or 65.59 versus 64.96% difficult to characterize statistically. The report preserves point values without declaring significance or equivalence.

**Reproducibility [D]:** several hyperparameters and hardware details are supplied, but exact cleaned counts, seeds, split grouping, full prompt details, optimizer identity, and some condition mappings remain unclear. Repository and license claims were not checked. The checklist's affirmative reproducibility answer is evidence of the authors' position, not a substitute for absent details.

## 18. Future work and open questions

**A. Explicit author future work:** Appendix A.1 leaves systematic execution testing of example code to future work and makes data available for others to build on. The conclusion frames Gorilla as an initial step toward LLM interfaces that interact with the digital world. Broader API domains are discussed as a possible use of the representation, not as completed evaluations. [A: pp. 4, 10, 14]

**B. Analyst open questions [D]:** How would performance change under API-disjoint or time-separated splits? Which training references are irrelevant, incorrect, or updated, and in what proportions? Can the contradictory counts and tables be resolved through durable experiment records? How stable are small model differences across runs? Can AST checks be combined with full execution and goal-level checks? What causes oracle-trained Gorilla's zero-document collapse? How should the system decide whether an unfamiliar API update is legitimate?

For the security research question, further questions remain entirely untested here: can malicious documentation redirect tool selection; which parties control the retrieved text; what actions the generated calls are authorized to perform; and whether adding retrieval and execution changes attack success relative to an otherwise comparable standalone LLM. Gorilla identifies architectural components relevant to asking these questions, but supplies no attack measurements answering them.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| API | Application programming interface: a specified callable software entry point. |
| APIBench | The authors' API documentation/instruction benchmark from three ML hubs. |
| LLM | Large language model that generates text or code from an input. |
| Gorilla | The API-specialized fine-tuned model and associated pipeline. |
| LLaMA-7B | Main pretrained base model, described as having seven billion parameters. |
| RAT | Retriever-Aware Training: training with API documentation alongside requests. |
| Retriever | Component selecting documentation to append to a request. |
| BM25 | Named retrieval baseline; its formula is not supplied. |
| GPT-Index | Retrieval condition using the specified embedding model. |
| Embedding | A numerical document representation; 1,536 dimensions are reported here. |
| Oracle | Idealized condition providing the correct reference document. |
| Zero-shot / 0-shot | In the main retrieval comparison, inference with no retrieved document. |
| Three-shot | Prompting with three worked examples. |
| Self-instruct | Generation of instructions using a model and a small seed-example set. |
| Fine-tuning | Additional training of pretrained weights for a particular task. |
| AST | Abstract syntax tree: structural representation of code. |
| Hallucination | Here, an API call absent from the evaluator's API database. |
| Error / err | Existing API selected incorrectly, distinguished from hallucination. |
| Overall / Acc | Reported API-call accuracy under the table's scoring condition. |
| Accuracy const | Table 4's accuracy satisfying an additional stated constraint. |
| HF / TH / TF | HuggingFace / Torch Hub / TensorFlow Hub in Table 5. |
| Model card | Documentation describing a model and its use/metadata. |
| Top-one accuracy | Fraction whose highest-ranked class is correct, used as model-card metadata. |
| RLHF | Reinforcement learning from human feedback; mentioned, not causally tested. |
| FLOPS | A computational-cost term mentioned among possible constraints; not operationalized in the reported constraint study. |
| `repo_or_dir`, `model`, `handle` | API argument names used by the structural evaluator. |
| `k` | Final argument index in the generic API-call template. |
| Percentage point | Absolute difference between percentages, distinct from relative percent change. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main reported API total | 1,645 | APIs | Main methodology/Figure 3; component conflict retained | Author-reported | p. 4 |
| Torch entries | 94 / 95 | APIs | Figure 3 / prose and A.1 | Author-reported | pp. 4, 14 |
| Tensor entries | 626 / 696 | APIs | Main filtering / A.1 | Author-reported | pp. 4, 14 |
| HuggingFace entries | 925 | models/APIs | After filtering | Author-reported | p. 4 |
| TensorFlow before filtering | 801 | models | v2 source | Author-reported | p. 4 |
| HuggingFace source size | about 203,681 | models | Reported platform catalog | Author-reported | p. 4 |
| Generated pairs | 16,450 | pairs | Ten per reported 1,645 APIs | Author-reported | p. 4 |
| Manual seed examples | 18 | examples | Six per hub | Author-reported | p. 4 |
| HF split | 90 / 10 | % | Train/evaluation | Author-reported | p. 14 |
| Torch/Tensor split | 80 / 20 | % | Train/test | Author-reported | p. 14 |
| Training epochs / batch | 5 / 64 | epochs / examples | Main training configuration | Author-reported | pp. 14–15 |
| Learning rate | 2e-5 | rate | Cosine decay | Author-reported | pp. 14–15 |
| Warmup / weight decay | 0.03 / 0 | ratio / coefficient | Table 6 | Author-reported | p. 15 |
| Maximum sequence length | 2,048 | sequence positions | Table 6; tokenizer unit not elaborated | Author-reported | p. 15 |
| Training hardware | 8 × A100, 40 GB each | GPUs / memory | Fine-tuning | Author-reported | p. 14 |
| Retrieved documents | 1 | document/query | BM25 and GPT-Index | Author-reported | p. 7 |
| Embedding dimensions | 1,536 | dimensions | GPT-Index | Author-reported | p. 7 |
| Gorilla no-retriever accuracy | 59.13 / 71.68 / 83.79 | % | Torch / HF / Tensor, T1 | Author-reported | p. 8 |
| Gorilla no-retriever hallucination | 6.98 / 10.95 / 5.40 | % | Torch / HF / Tensor, T1 | Author-reported | p. 8 |
| Gorilla BM25 accuracy | 40.32 / 17.03 / 41.89 | % | T1; T2 HF is 17.04 | Author-reported | p. 8 |
| Gorilla GPT-Index accuracy | 61.82 / 47.46 / 64.96 | % | Torch / HF / Tensor, T1 | Author-reported | p. 8 |
| Gorilla oracle accuracy | 67.20 / 91.26 / 94.16 | % | Torch / HF / Tensor, T1 | Author-reported | p. 8 |
| GPT-3.5 Tensor oracle accuracy | 95.03 | % | Exceeds Gorilla's 94.16 | Author-reported | p. 8 |
| Torch advantage over GPT-4 | 20.43 | percentage points | 59.13 − 38.70, no retriever | Analyst-derived | p. 8 |
| Manual validation sample | 100 | generations | Random Gorilla evaluation sample | Author-reported | pp. 8, 17 |
| AST / human / execution | 78 / 78 / 72 | % | Same reported sample | Author-reported | pp. 8–9 |
| Execution gap | 6 | percentage points | 78 − 72 | Analyst-derived | pp. 8–9 |
| Constraint subset retained | 65.26 | % | Torch entries with accuracy metadata | Author-reported | p. 10 |
| Gorilla constraint accuracy | 47.88 / 30.28 / 26.76 / 67.60 | % | None / BM25 / GPT-Index / oracle | Author-reported | p. 9 |
| Best listed constraint score | 69.71 | % | Claude oracle | Author-reported | p. 9 |
| DocPrompting / Gorilla accuracy | 61.72 / 71.68 | % | HF, 7B comparison | Author-reported | p. 18 |
| DocPrompting / Gorilla hallucination | 17.36 / 10.95 | % | Same comparison | Author-reported | p. 18 |
| DocPrompting accuracy improvement | 9.96 | percentage points | 71.68 − 61.72 | Analyst-derived | p. 18 |
| Base-model plot | about 71–72 / 71–72 / 64–65 | % | LLaMA / MPT / Falcon | Approximate visual estimate | p. 20 |
| LLM repetitions | 1 | run | Checklist cost explanation | Author-reported | p. 21 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Specialized Gorilla improves no-retriever API performance in T1 | 59.13/71.68/83.79% accuracy, higher than listed baselines | T1, X1 | p. 8 | HIGH for table contents; HF scoring differs by model. |
| Retrieval is not uniformly beneficial | Gorilla BM25 below no retrieval on all three hubs | T1–T2, X1–X2 | pp. 7–8 | HIGH; not a security attack result. |
| Training/input format matters | Oracle-trained Gorilla has zero accuracy without documents | T2, X2 | p. 8 | HIGH within this ablation; mechanism not isolated further. |
| Correct documentation can improve oracle-trained output | Oracle accuracies 67.20/91.26/94.16% | T2, X2 | p. 8 | HIGH; idealized retriever condition. |
| AST captures API identity better than full execution | 78% API judgments versus 72% executable programs | T3, F12, X3 | pp. 8–9, 17, 19 | HIGH for reported sample; only 100 generations. |
| Gorilla responds to changed API references | ResNet and repository substitutions | F6, X4 | p. 9 | MEDIUM for generalization; qualitative examples. |
| Gorilla can satisfy some accuracy constraints | 47.88% zero-shot constraint score | T4, X5 | pp. 9–10 | HIGH for value; no universal compliance. |
| Three-shot GPT prompting can match one Gorilla accuracy | Torch 75.80% tie with GPT-4 | T5, X6 | p. 10 | MEDIUM due table inconsistencies. |
| Gorilla beats the reported DocPrompting configuration | Accuracy +9.96 points; hallucination −6.41 points | T7, X7 | p. 18 | HIGH for reported comparison; no run variation. |
| Multiple base models can be fine-tuned | Three nonzero bars, Falcon visibly lower | F13, X8 | pp. 18, 20 | MEDIUM; values approximate. |
| Agent security relevance is architectural | Retrieved text conditions an API output; execution is separate | F3, §3.2, F12 | pp. 4–5, 19 | Analyst interpretation; no attack or standalone comparison. |
| Statistical uncertainty is uncharacterized | LLM experiments performed once | Checklist item 7 | p. 21 | HIGH for disclosure. |

## 22. Very simple explanation

Imagine asking a computer assistant to choose a tool from a very large toolbox. A normal language model might name a tool that does not exist, choose the wrong one, or give it the wrong settings. Gorilla trains a model specifically to read requests and produce calls to real machine-learning tools. It can also receive a page of tool documentation before answering.

The documentation can help, but it can also point the assistant in the wrong direction. The experiments show that attaching a retrieved page sometimes lowers accuracy. A model trained to expect documentation can fail badly when no documentation is supplied. The result depends on how the model was trained, which document it receives, and what counts as a correct answer.

The researchers also build a checker that looks at the structure of the tool call. In a sample of 100 outputs, that checker and human reviewers both judged 78% of the API choices correct. Only 72% of the complete programs ran successfully, because the code around a correct tool call could still be broken. Choosing the right tool is therefore only one part of getting a task done.

For the question about web-agent security, the useful lesson is a limited one: an assistant that reads outside material and produces software actions has more components whose behavior needs examination. This paper shows that documents can affect API choices and that API correctness does not guarantee complete program correctness. It does **not** show a malicious website attacking an agent, measure security vulnerability, or prove that web agents are more vulnerable than standalone language models.

## Completeness Audit

The audit distinguishes coverage of supplied objects from strength of their evidence. All supplied text pages were read; only the sixteen supplied renderings were visually inspected. Repetitive results are compressed openly rather than described as absent.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes, text/visual | Yes | Fully represented | Title retained; authors are Shishir G. Patil, Tianjun Zhang, Xin Wang, Joseph E. Gonzalez; NeurIPS 2024 footer. First two authors carry equal-contribution marks. |
| Keywords | No separate list found | Yes | Missing from supplied material | No keyword section identified. |
| §1 Introduction | Yes | Yes | Fully represented | Problem, motivation, scope, contributions. |
| §2 Related Work | Yes, text only | Yes | Represented in compressed form | Categories and DocPrompting positioning; individual cited works not independently reviewed. |
| §3 Methodology overview | Yes | Yes | Fully represented | Dataset, training, evaluation pipeline. |
| §3.1 Dataset Curation | Yes | Yes | Fully represented | Documentation, instructions, constraints, count conflicts. |
| §3.2 Gorilla | Yes | Yes | Fully represented | Training, RAT, inference, execution boundary. |
| §3.3 Verifying APIs | Yes | Yes | Fully represented | Single-call scope and AST rationale. |
| §4 Evaluation setup | Yes | Yes | Fully represented | RQs, baselines, retrievers, scoring. |
| §4.1 AST Accuracy | Yes | Yes | Fully represented | X1–X3, asymmetric HF scoring. |
| §4.2 Documentation Change | Yes | Yes | Fully represented | X4; qualitative scope preserved. |
| §4.3 Constraints | Yes | Yes | Fully represented | X5, subset, metric distinction. |
| §4.4 Fine-tuning versus Prompting | Yes | Yes | Fully represented | X6 and T5 inconsistencies. |
| §5 Conclusion | Yes | Yes | Represented in compressed form | Main contributions and aspirational scope. |
| References [1]–[49] | Yes, text only | Yes | Represented in compressed form | Bibliographic list not individually reproduced or validated. |
| A.1 Dataset Details | Yes | Yes | Fully represented | Counts, fields, code-execution limitation. |
| A.2 Gorilla Details | Yes | Yes | Fully represented | Splits, hyperparameters, hardware. |
| A.3 Performance Comparison | Yes | Yes | Fully represented | Full-plot purpose and claims. |
| A.3.1 Evaluation | Yes | Yes | Fully represented | API-specific argument matching. |
| A.3.2 Hallucination | Yes | Yes | Fully represented | Qualitative examples and database-relative meaning. |
| A.3.3 AST Metric | Yes | Yes | Fully represented | Manual sample and broken supporting code. |
| A.3.4 DocPrompting | Yes | Yes | Fully represented | X7 and exact T7 values. |
| A.3.5 Pretraining Sensitivity | Yes | Yes | Fully represented | X8; approximate values labeled. |
| RQ1, RQ2, RQ3 | Yes | Yes | Fully represented | Separately linked to experiments. |
| Formal hypotheses | None identified | Yes | Missing from supplied material | No formal hypotheses invented. |
| X1–X8 | Yes | Yes | Fully represented | Separate setup, outcomes, caveats provided. |
| F1 API examples | Yes, visual/text | Yes | Fully represented | Curated examples, not execution verification. |
| F2 overview scatterplots | Yes, visual/text | Yes | Represented in compressed form | Four panels; exact points not pixel-estimated. |
| F3 architecture | Yes, visual/text | Yes | Fully represented | Training and inference paths. |
| F4 AST diagram | Yes, visual/text | Yes | Fully represented | Selected-node matching and optional argument. |
| F5 GPT-retriever bars | Yes, visual/text | Yes | Fully represented | Values and T1 disagreement. |
| F6 documentation changes | Yes, visual/text | Yes | Fully represented | All three conditions. |
| F7 domain lists | Yes, visual/text | Yes | Represented in compressed form | Full list omitted; breadth and count/caption conflicts preserved. |
| F8 dataset examples | Yes, visual/text | Yes | Represented in compressed form | Fields and two formats; metadata not relabeled as Gorilla results. |
| F9 hallucination examples | Yes, visual/text | Yes | Represented in compressed form | Example role and limits retained. |
| F10 twelve accuracy panels | Yes, visual/text | Yes | Represented in compressed form | Major patterns, repeated values, caption contradiction. |
| F11 twelve scatter panels | Yes, visual/text | Yes | Represented in compressed form | Axes, encoding, trends; repeats T1. |
| F12 supporting-code bug | Yes, visual/text | Yes | Fully represented | API correctness separated from program execution. |
| F13 base models | Yes, visual/text | Yes | Uncertain | Exact values unlabeled; approximate estimates only. |
| T1 main grid | Yes, visual/text | Yes | Represented in compressed form | Key values, exceptions, scoring caveat; not every cell transcribed. |
| T2 retrieval ablation | Yes, visual/text | Yes | Represented in compressed form | Full accuracy sequences, critical hallucination conditions. |
| T3 validation | Yes, visual/text | Yes | Fully represented | All three values and sample context. |
| T4 constraints | Yes, visual/text | Yes | Represented in compressed form | Full constraint sequences, key overall comparisons. |
| T5 prompting | Yes, visual/text | Yes | Fully represented | Core comparisons and contradictions. |
| T6 hyperparameters | Yes, visual/text | Yes | Fully represented | All six entries. |
| T7 DocPrompting | Yes, visual/text | Yes | Fully represented | All four values. |
| Major equations | None numbered | Yes | Fully represented | Metric relationship and API template discussed. |
| Algorithms/pseudocode | No numbered algorithm | Yes | Fully represented | Procedural training/inference and example code explained. |
| Three primary contributions | Yes | Yes | Fully represented | Gorilla, RAT, APIBench/AST. |
| Author-stated limitations | Yes | Yes | Fully represented | Retrieval harm, coverage, execution, single call, single runs. |
| Checklist 1–8 | Yes, text only | Yes | Represented in compressed form | Claims, limitations, theory NA, reproducibility, artifacts, settings, single runs, compute. |
| Checklist 9–15 | Yes, text only | Yes | Represented in compressed form | Ethics yes; impacts emphasize benefits; safeguards NA; licensing/new assets yes; human-subject/IRB items NA. |
| Author affiliations/contact | Yes | Yes | Represented in compressed form | UC Berkeley and Microsoft Research; email not needed for scientific explanation. |
| Substantive footnotes | Yes where supplied | Yes | Represented in compressed form | Venue and author markers accounted for; no additional scientific footnote identified. |
| Separate supplementary material | No | No | Missing from supplied material | Checklist reference does not establish access. |
| Repository, models, data, demo | No | Claims only | Inaccessible | No artifact inspection permitted or performed. |

### Missing or inaccessible material

No page is missing from the supplied text, but separate supplemental files, dataset records, experiment logs, repository contents, model weights, and demo behavior were not supplied. Original cited papers were not reviewed. Pages 3, 11–13, 21–22 have text-only coverage. The API execution system is described but not inspected. No claim is made that absent artifacts, licenses, or reproduction instructions were validated.

### Uncertain interpretations

Exact dataset counts remain unresolved: 94 versus 95 Torch entries, 626 versus 696 Tensor entries, and the resulting total. Domain counts and the smallest-hub caption also conflict. Table 1, Table 5, and several figure labels disagree. Table 5 contains a major outcome-partition problem. Figure 13 lacks exact values. The distribution of incorrect training references, grouping of split examples by API, and the extent of genuinely unseen API evaluation are not fully specified. The paper's discussion of model confidence on unfamiliar documentation is qualitative and does not define a calibrated confidence measure.

### Deliberately compressed material

The 49 references, exhaustive domain names, long dataset example records, repeated bar/scatter results, and every noncritical cell in Tables 1, 2, and 4 are compressed. Figure 8's detailed HybridNets metrics are identified as source-model metadata rather than copied as Gorilla outcomes. Decorative logos, generated-image illustration details, author email, and routine checklist wording are not exhaustively reproduced. Compression preserves method, conditions, important numbers, exceptions, and substantive contradictions.

### Potential omissions

No known major section, substantive subsection, listed research question, distinct experiment, figure, table, principal contribution, or explicit methodological limitation from the supplied inventory is left unrepresented. This is an inventory-based coverage statement, not a claim that every word or numerical cell has been reproduced. Unavailable artifacts, unlabeled values, unresolved contradictions, and compressed repetitions prevent a claim of fully verified scientific completeness.
