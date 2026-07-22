# *Gorilla: Large Language Model Connected with Massive APIs*

**Authors:** Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez  
**Affiliations:** UC Berkeley and Microsoft Research  
**Venue:** NeurIPS 2024

## 1. Background and Context

Large language models (LLMs) have become capable at reasoning, conversation, and code generation, but reliably using external tools through application programming interfaces (APIs) remains difficult. An API is a standardized way for software to invoke another program, model, database, or service. Correct API use requires knowing which tools exist, choosing one that satisfies the user’s needs, and generating the exact function name and arguments expected by that tool.

This problem is challenging because:

- Millions of APIs may be available, often with overlapping functions but different constraints.
- API documentation, model names, repositories, versions, and arguments change more quickly than LLMs can be retrained.
- An LLM may invent a nonexistent API or argument—an API “hallucination”—even when its response looks plausible.
- Merely retrieving documentation does not guarantee success. A retriever may return an irrelevant document, and an LLM may follow it uncritically.
- Several APIs may be functionally suitable, making conventional unit-test evaluation inadequate.
- Real requests frequently include constraints such as minimum accuracy, maximum parameter count, latency, memory use, or cost.

Prior tool-using systems connected LLMs to particular tools such as web search, calculators, translation systems, Python interpreters, or robotics functions. Other work improved program synthesis through prompting, decomposition, self-debugging, code pretraining, and retrieved documentation. The authors distinguish Gorilla from these approaches by targeting an open-ended collection of APIs, systematically training and evaluating the model, including detailed API constraints, and introducing a structural metric for API correctness and hallucination.

The closest comparison discussed is DocPrompting, which retrieves documentation for code generation. Gorilla differs by collecting model-specific information such as arguments, performance, and efficiency; using Abstract Syntax Tree (AST) subtree matching; instruction-tuning a conversational model; and allowing the model to interact with users rather than serving solely as an NLP-to-code generator.

## 2. Research Goal and Objectives

The paper aims to make LLMs reliable interfaces to large, changing collections of APIs. It introduces **Gorilla**, a fine-tuned LLaMA-7B model designed to translate natural-language requests into appropriate API calls.

The evaluation asks three central questions:

1. How does Gorilla compare with open- and closed-source LLMs on held-out APIBench examples?
2. Can it adapt at test time when API documentation, model versions, or repositories change?
3. Can it select an API while respecting user-defined constraints?

The work also examines:

- Whether retrieval-aware fine-tuning is better than ordinary fine-tuning or prompting.
- How BM25, embedding-based, and oracle retrieval affect accuracy and hallucination.
- Whether AST subtree matching is a valid offline evaluation method.
- Whether the training recipe transfers to different underlying pretrained models.

## 3. Methods (Approach/Design)

### 3.1 APIBench construction

The authors created **APIBench**, a benchmark assembled from model cards in three machine-learning API hubs:

- Torch Hub
- TensorFlow Hub
- HuggingFace

The main methodology reports **1,645 APIs**:

- 95 Torch Hub models are stated in the text, although Figure 3 says 94.
- TensorFlow Hub v2 originally contained 801 models; after removing poorly documented cards, 626 remained.
- HuggingFace hosted approximately 203,681 models. The authors retained the top 20 models in each considered domain, producing 925 models.

There are minor internal numerical inconsistencies in the paper. Appendix A.1 says Tensor Hub contains 696 APIs, while the methodology and Figure 3 say 626; it also alternates between 94 and 95 Torch Hub APIs. The stated total of 1,645 agrees with 94 + 626 + 925, not with all of the appendix counts.

Each model card was converted into a JSON record containing:

- Domain
- Framework
- Functionality
- API name and call
- API arguments
- Environment requirements
- Example code
- Performance
- Description

The schema was deliberately designed to be extensible beyond machine-learning APIs to areas such as REST and SQL APIs.

### 3.2 Domains represented

The methodology groups HuggingFace models into 7 multimodal, 8 computer-vision, 12 NLP, 5 audio, 2 tabular, and 2 reinforcement-learning categories. Appendix Figure 7 reports:

- 6 Torch Hub domains
- 57 Tensor Hub domains
- 37 HuggingFace domains

Torch Hub covers classification, semantic segmentation, object detection, audio separation, video classification, and text-to-speech.

Tensor Hub spans text, image, video, and audio tasks, including classification, generation, question answering, retrieval, segmentation, object detection, pose estimation, image enhancement, speech-to-text, speech synthesis, and audio-event classification.

HuggingFace includes multimodal tasks, computer vision, NLP, audio, tabular learning, and reinforcement learning. Examples include text-to-image, image-to-text, document question answering, depth estimation, object detection, translation, summarization, conversational generation, automatic speech recognition, tabular regression, and robotics.

The caption of Figure 7 says Tensor Hub is the smallest dataset, although the numerical counts in the text make Torch Hub the smallest. This is another source inconsistency.

### 3.3 Synthetic instruction generation

The authors used GPT-4 and the self-instruct paradigm to create realistic natural-language requests for each API. GPT-4 received:

- Three in-context examples
- The reference API documentation
- Instructions to invent realistic use cases without mentioning the API’s name or giving obvious hints

The researchers manually created six instruction–API examples for each of the three hubs, for **18 manually produced examples total**. For every API, they generated 10 instruction–API pairs, sampling three of the six relevant demonstrations for each generation. Figure 3 consequently reports **16,450 instruction–API pairs** from 1,645 APIs.

Each training example was converted into a one-round user–assistant conversation. The expected response could include the domain, API provider, API call, explanation, and supporting code.

Figure 8 illustrates two records:

- A zero-shot TensorFlow Hub request about detecting animal movement at a zoo, answered using an SSD MobileNet V2 object detector from the Open Images v4 collection.
- A retrieval-assisted Torch Hub request for detecting pedestrians and cars, accompanied by documentation for HybridNets. The answer uses `torch.hub.load` with `datvuthanh/hybridnets` and explains its object-detection role. The reference record also includes performance on BDD100K: 92.8% detection recall, 77.3% mAP@0.5, 90.5% drivable-area mIoU, 85.4% lane-line accuracy, and 31.6% lane-line IoU.

### 3.4 Constraint-aware instructions

Training examples also included requests with numerical or operational constraints. One example asks for an image classifier with fewer than 10 million parameters and at least 70% ImageNet accuracy.

The premise is that selecting an API is often a trade-off among accuracy, parameter count, disk size, peak memory, FLOPs, latency, or invocation cost. The model must therefore understand both the requested function and the restrictions governing the choice.

### 3.5 Gorilla and Retriever-Aware Training

Gorilla is a LLaMA-7B model instruction-fine-tuned specifically for API invocation. Two versions were trained:

- A model trained without retrieval.
- A model trained with **Retriever-Aware Training (RAT)**.

For RAT, retrieved documentation is appended to the user prompt in approximately this form:

`Use this API documentation for reference: <retrieved_API_doc_JSON>`

The training response still contains the correct ground-truth API. Because the retrieved item may be wrong, this teaches Gorilla to judge rather than automatically obey the retriever:

- If the document is relevant, Gorilla can use its up-to-date names, arguments, and details.
- If it is irrelevant, Gorilla should ignore it and rely on knowledge learned during fine-tuning.

RAT is intended to improve in-context use of documentation, reduce hallucination, and support test-time API changes.

### 3.6 Inference and retrieval conditions

At inference time, Gorilla supports:

- **Zero-shot mode:** Only the natural-language request is supplied.
- **Retrieval mode:** The request is combined with the top-ranked API document.

Three retrieval conditions were tested:

- **BM25:** A lexical retriever treating every API as a separate document.
- **GPT-Index:** An embedding retriever using 1,536-dimensional `text-embedding-ada-002-v2` representations.
- **Oracle:** A perfect-recall retriever that supplies the correct document, estimating the upper bound from ideal retrieval.

Only the top-ranked document is appended. No additional prompt tuning is performed. The authors built an API execution system but state that execution is not the paper’s main focus.

### 3.7 Data splits and training configuration

The appendix reports:

- HuggingFace: 90% training and 10% evaluation.
- Torch Hub and Tensor Hub: 80% training and 20% testing.
- Five training epochs
- Learning rate: \(2 \times 10^{-5}\)
- Cosine learning-rate decay
- Batch size: 64
- Warmup ratio: 0.03
- Weight decay: 0
- Maximum sequence length: 2,048
- Hardware: eight A100 GPUs with 40 GB memory each

The model, code, dataset, and demo were released, and the checklist states that the assets are under the Apache 2.0 license.

### 3.8 AST-based evaluation

Ordinary unit tests are poorly suited to the task because multiple APIs may correctly solve the same problem. Even within a family such as DenseNet, several valid configurations may exist.

The authors instead parse generated Python calls into an **Abstract Syntax Tree**, a structural representation of the code. They identify whether the generated API call matches a subtree belonging to a known API in the benchmark.

Figure 4 demonstrates this for:

`torch.hub.load('pytorch/vision:v0.10.0', 'densenet121', pretrained=True)`

The evaluator matches the structural path through `torch.hub.load`, the `pytorch/vision` repository, and the `densenet121` model. It does not require `pretrained=True` because that argument is optional.

The evaluator supports configurable required arguments:

- Torch Hub: `torch.hub.load`, checking `repo_or_dir` and `model`.
- Tensor Hub: `hub.KerasLayer` or `hub.load`, checking `handle`.
- HuggingFace: required API-specific function information and normally `pretrained_model_name_or_path`; `pipeline` is exempt because it may choose a model automatically once the task is specified.

Three mutually exclusive outcomes are defined:

- **Accuracy:** The correct API structure is generated.
- **Error:** A real API is invoked incorrectly or the wrong real API is chosen.
- **Hallucination:** The call is not a subtree of any API in the database, meaning the model invented a tool.

Accuracy, error, and hallucination sum to 100%.

### 3.9 Baselines

Gorilla was compared with:

- LLaMA-7B
- GPT-3.5 Turbo, checkpoint `gpt-3.5-turbo-0301`
- GPT-4, checkpoint `gpt-4-0314`
- Claude, checkpoint `claude-v1`
- DocPrompting in a separate matched comparison

The main evaluations include zero-shot, BM25, GPT-Index, and oracle-retrieval conditions. A further experiment compares zero-shot Gorilla with GPT-3.5 and GPT-4 using three in-context examples.

For HuggingFace, the benchmark is not exhaustive. Except for Gorilla, models were therefore evaluated mainly on whether they selected the correct domain, reducing that evaluation to a multiple-choice-like problem. Torch Hub and Tensor Hub use full AST matching for all models, so HuggingFace results are not completely equivalent across systems.

## 4. Results and Findings

### 4.1 Illustrative API-call behavior

**Figure 1** compares answers to a request for a Torch Hub speech-to-text API:

- Gorilla correctly identifies the speech-to-text task and generates a fully qualified call to the `snakers4/silero-models` repository.
- GPT-4 supplies a nonexistent model or argument combination, classified as an argument hallucination.
- Claude chooses an incorrect library and labels the task as audio translation.

This example illustrates the distinction between inventing API components and selecting a real but functionally inappropriate tool.

### 4.2 Overall zero-shot results

Gorilla’s zero-shot accuracy was:

- **Torch Hub:** 59.13%, with 6.98% hallucination and 33.87% other error.
- **HuggingFace:** 71.68%, with 10.95% hallucination and 17.36% error.
- **TensorFlow Hub:** 83.79%, with 5.40% hallucination and 10.80% error.

Zero-shot baseline results were:

| Model | Torch accuracy / hallucination | HuggingFace accuracy / hallucination | TensorFlow accuracy / hallucination |
|---|---:|---:|---:|
| LLaMA | 0 / 100 | 0 / 97.57 | 0 / 100 |
| GPT-3.5 | 48.38 / 18.81 | 16.81 / 35.73 | 41.75 / 47.88 |
| GPT-4 | 38.70 / 36.55 | 19.80 / 37.16 | 18.20 / 78.65 |
| Claude | 18.81 / 65.59 | 6.19 / 77.65 | 9.19 / 88.46 |
| Gorilla | **59.13 / 6.98** | **71.68 / 10.95** | **83.79 / 5.40** |

The paper reports Gorilla as 20.43 percentage points better than GPT-4 and 10.75 points better than GPT-3.5 in the zero-shot comparison discussed in Section 4.1. Relative to base LLaMA, improvement was as large as 83 percentage points.

Figure 10 presents the same accuracies as bar charts across all 12 combinations of dataset and retrieval condition. It emphasizes Gorilla’s especially large advantage without retrieval.

### 4.3 BM25 retrieval

With BM25, Gorilla achieved:

- Torch Hub: 40.32% accuracy, 4.30% hallucination, 55.37% error.
- HuggingFace: 17.03% accuracy, 6.42% hallucination, 76.55% error.
- TensorFlow Hub: 41.89% accuracy, 2.77% hallucination, 55.32% error.

The best BM25 accuracies among the evaluated models were:

- Torch Hub: Gorilla at 40.32%, narrowly above Claude at 39.78%.
- HuggingFace: GPT-3.5 at 17.26%, narrowly above Gorilla at 17.03%.
- TensorFlow Hub: GPT-3.5 at 54.16%, above Gorilla at 41.89%.

Thus, retrieval greatly reduced hallucination in several cases but frequently increased wrong-API errors. BM25 was particularly damaging to HuggingFace accuracy.

### 4.4 GPT-Index retrieval

With GPT-Index, the accuracies were:

| Model | Torch Hub | HuggingFace | TensorFlow Hub |
|---|---:|---:|---:|
| LLaMA | 14.51 | 10.18 | 15.62 |
| GPT-3.5 | 60.21 | 29.08 | **65.59** |
| GPT-4 | 59.13 | 44.58 | 43.94 |
| Claude | 60.21 | 41.37 | 55.62 |
| Gorilla | **61.82** | **47.46** | 64.96 |

Gorilla’s corresponding hallucination rates were:

- Torch Hub: **0%**
- HuggingFace: 8.19%
- TensorFlow Hub: 2.33%

Figure 5 visualizes these results. Gorilla leads on Torch Hub and HuggingFace and essentially matches the strongest result on TensorFlow Hub, where GPT-3.5 is 0.63 percentage points higher.

Gorilla’s non-hallucination error remained substantial—38.17%, 44.36%, and 32.70% across the three hubs—showing that avoiding invented APIs does not ensure selection of the correct real API.

### 4.5 Oracle retrieval

With the correct documentation supplied, Gorilla reached:

- Torch Hub: **67.20%** accuracy, 0% hallucination, 32.79% error.
- HuggingFace: **91.26%** accuracy, 7.08% hallucination, 1.66% error.
- TensorFlow Hub: 94.16% accuracy, 1.89% hallucination, 3.94% error.

Other oracle accuracies were:

| Model | Torch Hub | HuggingFace | TensorFlow Hub |
|---|---:|---:|---:|
| LLaMA | 16.12 | 17.70 | 12.55 |
| GPT-3.5 | 66.31 | 89.71 | **95.03** |
| GPT-4 | 66.12 | 85.07 | 55.91 |
| Claude | 63.44 | 77.21 | 74.74 |
| Gorilla | **67.20** | **91.26** | 94.16 |

Gorilla leads on Torch Hub and HuggingFace. On TensorFlow Hub it is 0.87 points below GPT-3.5.

The gap between ordinary retrieval and oracle retrieval indicates that retrieval quality is a major bottleneck. Figure 10’s caption says Gorilla remains best even with the oracle answer, although the numerical TensorFlow Hub result is slightly higher for GPT-3.5.

### 4.6 Effect of Retriever-Aware Training

Table 2 compares Gorilla trained without retrieval against Gorilla trained with oracle documentation during fine-tuning.

For the RAT-trained model:

- Without test-time retrieval, accuracy was 0% on all three hubs, with hallucination of 100%, 99.67%, and 100%.
- With BM25, accuracy was 40.32%, 17.04%, and 41.89%.
- With GPT-Index, accuracy was 61.82%, 47.46%, and 64.96%.
- With oracle retrieval, accuracy reached 67.20%, 91.26%, and 94.16%.

For Gorilla trained without retrieval:

- Zero-shot accuracy was 59.13%, 71.68%, and 83.79%.
- BM25 accuracy was 37.63%, 11.28%, and 34.30%.
- GPT-Index accuracy was 60.21%, 28.10%, and 52.40%.
- Oracle-document accuracy was 54.83%, 45.58%, and 82.91%.

According to the paper, incorporating ground-truth retrieval during fine-tuning produced:

- A **12.37-point** improvement on Torch Hub relative to training without retrieval.
- A **23.46-point** improvement on HuggingFace.

At evaluation, however, current retrievers remained far below the oracle:

- GPT-Index caused a reported 29.20% accuracy degradation.
- BM25 caused a reported 52.27% degradation.

The striking 0% zero-shot performance of the RAT-trained model shows that it is dependent on receiving documentation in the expected prompt format. RAT is beneficial when retrieval is available and sufficiently good, not as an unconditional replacement for ordinary zero-shot fine-tuning.

### 4.7 Accuracy versus hallucination

Figures 2 and 11 plot accuracy vertically and hallucination horizontally, so the ideal position is the upper-left corner. They cover zero-shot, BM25, GPT-Index, and oracle settings across the three hubs.

The plots show that:

- Gorilla is particularly strong in zero-shot mode, combining high accuracy with substantially lower hallucination than most baselines.
- GPT-Index and oracle retrieval move most systems toward lower hallucination and higher accuracy, although not uniformly.
- LLaMA remains low-accuracy and high-hallucination under most conditions.
- Gorilla generally stays close to the desirable upper-left region.
- Retrieval can lower hallucination while producing more wrong-API errors, especially when the retrieved document is irrelevant.

The paper unexpectedly finds that GPT-3.5 hallucinates less than GPT-4 across the hubs and across zero-shot, BM25, GPT-Index, and oracle settings. It suggests that differences associated with reinforcement learning from human feedback may influence truthfulness, although it does not establish a causal explanation.

### 4.8 Hallucination examples

Figure 9 shows GPT-4 generating questionable HuggingFace calls such as:

- A text-to-video pipeline with the placeholder `your_model_name`.
- A visual-question-answering model named `microsoft/clip-vqa-base`.
- A depth-estimation pipeline using `intel-isl/MiDaS` as both model and tokenizer.

The authors report that GPT-4 sometimes inserts arbitrary GitHub repository names into HuggingFace’s `pretrained_model_name_or_path` field or assumes that the user has a local model path. Gorilla substantially reduces this behavior.

### 4.9 Validation of the AST metric

The authors manually reviewed and attempted to execute **100 randomly selected Gorilla generations**.

Results were:

- AST subtree accuracy: **78%**
- Human judgment of correct API selection: **78%**
- End-to-end executable supporting code: **72%**

Every generation marked incorrect by AST was also marked incorrect manually. The six-point gap between API correctness and end-to-end execution arose from supporting code rather than semantic API-selection errors.

Figure 12 gives an example: Gorilla loads a correct HuggingFace sentiment-analysis model, but later calls `zip(sentiments, scores)` when `scores` is a single floating-point value rather than an iterable. The API call is correct, yet the surrounding program fails. This supports AST matching as an efficient metric for API selection while also showing that it does not guarantee bug-free complete programs.

### 4.10 Adaptation to changed documentation

Figure 6 tests whether RAT lets Gorilla follow new documentation at inference time for background removal:

- Its default learned response uses an FCN model with a ResNet-50 backbone.
- When retrieval supplies an FCN with ResNet-101, Gorilla changes the call to `fcn_resnet101`, even though that exact combination was unseen in training. It had encountered ResNet-101 in other architectures and treats the new document as plausible.
- If supplied an unfamiliar FCN ResNet-60 document, the paper reports that Gorilla assigns it low confidence and falls back to the known ResNet-50 configuration.
- When the documentation moves the model from `pytorch/vision` to `NVIDIA/DeepLearningExamples:torchhub`, Gorilla changes the repository in its call.

The experiment shows adaptation to both model-version changes and repository migration without retraining the LLM.

### 4.11 Constraint-aware API selection

The constraint experiment retains the **65.26% of Torch Hub examples** whose model cards include an accuracy measurement on at least one dataset. The model must choose an API satisfying a requested threshold. The paper’s example contrasts ResNeXt-101 32×16d at 84.2% top-1 ImageNet accuracy with MobileNetV2 at 71.88%; for a threshold of at least 80%, only the former is appropriate.

Table 4 distinguishes ordinary API correctness from **constraint accuracy**, meaning that the chosen API also satisfies the user’s numerical requirement.

Constraint accuracies were:

| Model | Zero-shot | BM25 | GPT-Index | Oracle |
|---|---:|---:|---:|---:|
| LLaMA | 0 | 6.33 | 3.52 | 17.60 |
| GPT-3.5 | 43.66 | **33.80** | **33.09** | 69.01 |
| GPT-4 | 43.66 | 29.57 | 29.57 | 59.15 |
| Claude | 17.25 | 29.57 | 31.69 | **69.71** |
| Gorilla | **47.88** | 30.28 | 26.76 | 67.60 |

Gorilla has the best zero-shot constraint accuracy. With BM25 and GPT-Index, it is broadly competitive but below GPT-3.5 and, for GPT-Index, Claude. Under oracle retrieval, Claude is highest, followed by GPT-3.5 and Gorilla.

Gorilla’s overall API accuracies—not necessarily satisfying the constraint—were 71.83%, 57.04%, 71.83%, and 78.16% across zero-shot, BM25, GPT-Index, and oracle conditions. Its hallucination rates were 19.71%, 39.43%, 26.05%, and 16.90%.

All models’ constraint accuracy was lower than their general API accuracy. This confirms that finding a functionally relevant API is easier than finding one that also meets a quantitative condition.

### 4.12 Fine-tuning versus three-shot prompting

Table 5 compares zero-shot Gorilla with GPT-3.5 and GPT-4 prompted with three examples.

| Model | HF acc. / hall. | Torch acc. / hall. | TensorFlow acc. / hall. |
|---|---:|---:|---:|
| GPT-3.5, zero-shot | 16.81 / 35.73 | 41.93 / 10.75 | 41.75 / 47.88 |
| GPT-4, zero-shot | 19.80 / 37.16 | 54.30 / 34.40 | 18.20 / 78.65 |
| GPT-3.5, three-shot | 25.77 / 32.30 | 73.11 / 72.58 | 71.82 / 11.09 |
| GPT-4, three-shot | 26.32 / 35.84 | **75.80** / 13.44 | 77.37 / 11.97 |
| Gorilla, zero-shot | **58.05** / 28.32 | **75.80** / 16.12 | **83.79** / **5.40** |

Three-shot prompting improves the GPT models’ syntactic/API accuracy and lets GPT-4 match Gorilla on Torch Hub. Gorilla nevertheless performs best on average without demonstrations, especially on HuggingFace and TensorFlow Hub.

Some figures differ slightly from Table 1—for example, Table 5 reports Gorilla HuggingFace accuracy/hallucination of 58.05/28.32 rather than 71.68/10.95, and Torch values for GPT-3.5 and GPT-4 also differ. The paper does not explicitly reconcile these evaluation-number differences.

### 4.13 Comparison with DocPrompting

On HuggingFace, with both 7B systems trained for the same number of epochs and with the same learning rate:

- DocPrompting: 61.72% accuracy and 17.36% hallucination.
- Gorilla: **71.68% accuracy** and **10.95% hallucination**.

Thus, Gorilla improves accuracy by 9.96 percentage points and reduces hallucination by 6.41 points.

### 4.14 Robustness to the base model

Figure 13 applies the same RAT recipe to LLaMA-, MPT-, and Falcon-based Gorilla models on HuggingFace zero-shot evaluation. The visual shows the LLaMA and MPT variants at roughly 71–72% accuracy and Falcon at roughly 65%. The authors conclude that all three converge within a few percentage points, though the plotted Falcon gap appears somewhat larger than that description. Exact labels are not printed on the bars, so these values are approximate.

## 5. Analysis and Interpretation

The results support the authors’ central argument that specialized fine-tuning is more reliable for API invocation than asking a general-purpose LLM to generate calls from its pretrained knowledge.

Several mechanisms explain Gorilla’s gains:

- Instruction fine-tuning teaches the exact syntax and structure of API calls.
- Rich API records teach the model about functionality, performance, arguments, and constraints.
- RAT exposes the model to retrieved documentation during training and teaches it to decide whether that information is relevant.
- Current documentation can override stale model knowledge at test time.
- The model retains enough learned domain knowledge to reject some implausible retrieved documents.

The experiments also show that retrieval is not automatically beneficial. When a top-1 retriever returns the wrong document, models often stop hallucinating but invoke the retrieved wrong API. This shifts failures from invented tools to selection errors. Oracle results reveal substantial room for improving retrieval.

The test-time update examples directly answer the second research question: RAT permits changes in model architecture and repository source to be incorporated through documentation rather than retraining.

The constraint experiment partially answers the third question. Gorilla is strongest in zero-shot constraint satisfaction and remains competitive with retrieval, but constraint accuracy is still modest—47.88% zero-shot and 67.60% with an oracle. Reliable numerical trade-off reasoning is therefore improved but not solved.

AST matching closely reproduces human API-selection judgments on the 100-example sample. It is useful because executing every generated model call would require numerous libraries, compatible CUDA and kernel combinations, and expensive hardware. However, the 78% API correctness versus 72% complete-code execution demonstrates that API evaluation and whole-program correctness are distinct.

The paper interprets Gorilla as an initial step toward turning LLMs from static knowledge stores into interfaces that can act on a changing digital environment.

## 6. Contributions and Novelty

The paper claims three main contributions:

1. **Gorilla:** A large-scale API-calling LLM that generates calls across thousands of functions and libraries and outperforms the evaluated general-purpose open- and closed-source models in many settings.

2. **Retriever-Aware Training:** A training method that teaches an LLM to use relevant retrieved documentation while resisting irrelevant documentation. It improves adaptation to API changes, retrieval-based accuracy, and hallucination behavior.

3. **APIBench and AST evaluation:** A benchmark of approximately 1,600 machine-learning APIs, paired with synthetic natural-language instructions, detailed metadata, constraint information, and AST-based metrics separating correct calls, wrong real calls, and invented calls.

Additional contributions include:

- A test of API selection under numerical constraints.
- Evidence that fine-tuning generally outperforms few-shot prompting for this task.
- A matched comparison showing gains over DocPrompting.
- An empirical validation of AST matching against manual evaluation.
- Evidence that the training approach can transfer across LLaMA, MPT, and Falcon base models.
- Public release of the model, data, code, and demo.

## 7. Limitations and Caveats

The paper and its evidence establish several limitations:

- **Dataset scope:** APIBench covers machine-learning APIs from only three hubs. Claims about REST, SQL, or millions of arbitrary tools are prospective rather than experimentally demonstrated.
- **Internal count inconsistencies:** The paper alternates between 94 and 95 Torch Hub APIs and between 626 and 696 Tensor Hub APIs. Figure 7’s statement about the smallest dataset also conflicts with the reported counts.
- **Non-exhaustive HuggingFace evaluation:** HuggingFace hosts far more models than APIBench contains. Baselines other than Gorilla are evaluated mainly on domain selection rather than the same detailed AST criterion, limiting direct comparability.
- **Top-1 retrieval:** Only one document is retrieved. A single poor retrieval can strongly mislead the model.
- **Retriever dependence:** RAT-trained Gorilla scores approximately zero without the expected retrieval context, so the method relies on documentation being supplied in the trained format.
- **Retrieval quality:** BM25 frequently harms accuracy, and even GPT-Index remains far below the oracle.
- **Residual errors:** Gorilla can avoid hallucination yet still choose the wrong real API. For example, its GPT-Index error rates remain 38.17% on Torch Hub, 44.36% on HuggingFace, and 32.70% on TensorFlow Hub.
- **Constraint reasoning remains difficult:** Even the best constraint-aware results leave many cases unresolved.
- **Single-call evaluation:** The AST method evaluates one API call rather than multi-step plans or workflows.
- **AST is not execution:** Structurally correct calls can be surrounded by broken code. Only 72% of manually tested complete generations executed successfully.
- **Limited manual validation:** AST validation used 100 randomly sampled Gorilla outputs, not every system and condition.
- **Execution complexity:** Full testing requires dependency installation, compatible framework/CUDA combinations, and sometimes A100-class hardware.
- **Supporting code was deprioritized:** The dataset includes code examples, but the authors did not make full program execution a primary evaluation target.
- **No statistical uncertainty:** LLM experiments were performed once because of GPU cost, and the paper reports no error bars or significance tests.
- **Compute requirements:** Fine-tuning used eight 40-GB A100 GPUs.
- **Temporal robustness demonstrated through selected examples:** The documentation-change section shows convincing cases but does not provide a large quantitative benchmark of API evolution.
- **Execution system out of scope:** Although an API executor was implemented, the paper evaluates selection and invocation more than reliable completion of users’ end-to-end goals.
- **Broader-impact discussion is predominantly positive:** The checklist mentions customer service, real-time content generation, and data analysis, but does not describe concrete technical safeguards. It marks safeguards as not applicable because APIs are intended for distribution.

## 8. Future Work or Open Questions

The paper explicitly presents Gorilla as a first step toward LLMs that act as flexible interfaces to the digital world. Remaining directions include:

- Extending the benchmark and training method beyond machine-learning hubs to REST, SQL, and other API ecosystems.
- Improving retrievers so practical performance approaches the oracle results.
- Supporting more than one API call and evaluating multi-step tool workflows.
- Testing complete generated programs, not only the core API-call structure.
- Improving supporting-code reliability, including dependency installation, environment configuration, and output processing.
- Conducting broader quantitative evaluations of test-time API version and repository changes.
- Improving reasoning over multiple simultaneous constraints such as accuracy, cost, latency, memory, model size, and FLOPs.
- Evaluating whether RAT remains robust across a wider variety of base models and scales.
- Resolving the gap between correct API selection and successful end-to-end execution.
- Expanding manual or executable validation beyond the 100-generation sample.

The appendix specifically leaves systematic execution testing of the dataset’s code examples to future work.

## 9. High-Level Takeaway (Plain Language)

Gorilla is a language model trained to turn ordinary requests into precise calls to software tools. Instead of relying only on memorized knowledge, it can read current API documentation, decide whether that documentation is relevant, and use it to produce a call. Across the paper’s machine-learning API benchmark, this generally makes Gorilla more accurate and less likely to invent nonexistent tools than GPT-4, GPT-3.5, Claude, or unmodified LLaMA. The work also shows, however, that retrieval quality, numerical constraints, and bugs in surrounding code remain important unsolved problems.