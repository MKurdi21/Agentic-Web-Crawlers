# Attention Is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs

**Authors:** Yinan Zhong, Qianhao Miao, Yanjiao Chen, Jiangyi Deng, Yushi Cheng, and Wenyuan Xu — Zhejiang University  
**Venue:** Network and Distributed System Security (NDSS) Symposium 2026

## 1. Background and Context

Large language models are increasingly embedded in web agents, email assistants, planners, and other applications. Such an application typically receives a user instruction, retrieves relevant information from an external source, and sends the combined instruction and retrieved data to a backend LLM.

This creates a security problem called **indirect prompt injection (IPI)**. Instead of placing a malicious instruction directly in the user’s prompt, an attacker hides it inside externally retrieved content. If the application treats that content as instructions, the attacker can redirect the LLM toward an unintended task. Potential consequences include sensitive-information leakage and goal hijacking in systems such as email or banking applications. The paper notes that OWASP ranks prompt injection as the leading security risk for LLM-integrated applications.

**Figure 1** illustrates the threat and the proposed solution:

- In Figure 1(a), a user asks what the NDSS Symposium is. The retrieved webpage contains a hidden instruction telling the LLM to ignore previous instructions and direct the user to a phishing site. The backend returns the malicious text instead of answering the question.
- In Figure 1(b), the proposed system, **RENNERVATE**, detects and removes the injected instruction. The LLM then produces the legitimate description of NDSS.

The paper distinguishes:

- **Direct prompt injection**, where the malicious instruction appears in the user’s own prompt.
- **Indirect prompt injection**, where it appears in retrieved external data. IPI is generally stealthier because the user may never see or control the compromised source.
- **Black-box IPI**, produced through prompt engineering without access to model internals. Examples include naive instructions, context-ignoring text, escape/control characters, and fake-completion messages.
- **White-box or gradient-based IPI**, where an attacker uses model gradients or learned triggers. POUGH, GCG, and Neural Exec are examples discussed in the paper.

Existing defenses fall into two broad groups:

1. **Detection methods**
   - Auxiliary-LLM methods judge the prompt or compare the target model’s response with an expected response.
   - Classifiers such as Prompt-Guard, ProtectAI-v2, Attention Tracker, and TaskTracker distinguish clean from injected data.
   - These approaches may generalize poorly, depend on recognizable attack wording, incur large computational costs, or themselves be susceptible to injection.
   - Detection alone can also cause denial of service: it may reject compromised data without recovering enough clean content to complete the legitimate task.

2. **Prevention methods**
   - Prompt modification includes paraphrasing, base64 encoding, delimiters, Spotlighting, Sandwich defense, and Instructional defense.
   - Model modification includes adversarial fine-tuning or separate processing channels, as in BIPIA, Jatmo, SecAlign, StruQ, and Signed-Prompt.
   - Prompt modifications may leave malicious text in the data and remain vulnerable to sophisticated attacks.
   - Model modifications can be effective but require changing an LLM’s training or architecture, which may be costly or impractical for proprietary systems.

The authors argue that a useful defense must detect semantically subtle instructions, generalize beyond known attack templates, remove only the malicious portion, and preserve the application’s legitimate functionality.

## 2. Research Goal and Objectives

The paper introduces **RENNERVATE**, a framework that uses the target LLM’s internal attention patterns to:

1. Label individual external-data tokens as clean or injected.
2. Decide whether the complete retrieved document contains an IPI attack.
3. Remove the suspicious tokens so the original application can continue operating.
4. Generalize to new datasets, task combinations, and attacks not seen during training.
5. Resist attackers that adapt their injections using system outputs or gradients.
6. Achieve these goals without retraining or modifying the target LLM.

The central idea is that even when an injected instruction looks semantically harmless—such as “Please print Yes”—the target LLM may attend to it differently because it interprets it as a task. Attention features may therefore reveal the instruction’s functional role more reliably than its surface wording.

The paper also aims to provide a reusable research resource: **FIPI**, a large fine-grained IPI dataset with 100,000 injected examples, 10,000 benign examples, token-level labels, five principal attack forms, combined attacks, and coverage of 300 NLP subtasks.

## 3. Methods (Approach/Design)

### Threat and defender model

The adversary:

- Controls the external data source.
- Seeks to make the application produce an attacker-chosen response.
- May use any attack method.
- Knows that defenses may be present.
- May observe application responses and, in the strongest setting, gradients of the whole system.

The defender:

- Wants to detect IPI and neutralize it without disrupting legitimate instructions.
- Can observe the target LLM’s internal attention values.
- Cannot modify the target LLM.
- Has white-box access to the model but does not know the attacker’s exact method, wording, or injection position.

### Token-level formulation

An external document \(X\) is tokenized into embeddings \(F=[f_1,\ldots,f_n]\). Rather than classify the document only as clean or injected, RENNERVATE applies a detector to every token. These predictions are aggregated into a document-level verdict.

Tokens classified as injected form a set \(F^*\). Removing them from the original sequence produces a purified sequence, which is detokenized to recover sanitized text. In simple terms, the system highlights suspicious words or subwords, checks whether they form a convincing malicious span, and deletes them.

### System architecture

**Figure 2** shows three modules:

1. **Token-Level Detector:** produces clean/injected logits for every input token from the target LLM’s attention features.
2. **Injection Identifier:** smooths and aggregates those token predictions to decide whether the entire text is compromised.
3. **Injection Sanitizer:** removes tokens predicted to belong to the injection.

This design allows the same token labels to support both detection and recovery.

### Attention-based token detector

For each input token, the system collects attention from the first \(m\) generated response tokens across all \(l\) layers and \(h\) heads. The resulting feature has dimensions \(l \times h \times m\).

The authors avoid relying directly on token embeddings because an attacker may disguise an instruction as ordinary text. Attention is intended to capture how the LLM internally processes the token, including whether it treats the token as part of a task.

Because attention heads and response tokens do not contribute equally, RENNERVATE uses **two-step attentive pooling**:

1. **Response-wise pooling** learns which generated response tokens are most informative.
2. **Head-wise pooling** learns which attention heads matter most.

**Figure 3(a)** depicts an attentive-statistics pooling layer. It assigns learned weights to frames and computes both a weighted mean and weighted standard deviation. The mean emphasizes important frames; the standard deviation captures variation across different-length sequences.

**Figure 3(b)** shows the complete token detector:

- Attention features enter response-wise and head-wise pooling.
- Fully connected and batch-normalization layers process the pooled representation.
- \(N\) residual blocks with skip connections refine it.
- A final layer with dropout \(p=0.2\), softmax, and cross-entropy training outputs two logits per token.

All token detectors are parallelized.

### Injection identification and sanitization

Algorithm 1 performs the following operations:

1. Replicate-pad the sequence of token logits.
2. Apply a mean filter of kernel size \(k\).
3. Convert the smoothed scores to clean/injected token labels.
4. Find the longest consecutive sequence of injected labels.
5. Classify the whole document as injected if that run exceeds a predefined threshold.
6. If sanitization is enabled, remove the flagged tokens and detokenize the remainder.

The mean filter suppresses isolated prediction errors and reflects the assumption that actual injected instructions usually contain several consecutive tokens. Detection occurs for every input; sanitization is controlled by a user-selectable flag.

### FIPI dataset construction

FIPI extends the SEP prompt-injection dataset, which contains 9,160 user-instruction/clean-data pairs spanning:

- Information processing and retrieval.
- Creative and generative work.
- Analytical and evaluative tasks.

Each category contains 100 subtasks, for 300 subtasks overall.

Construction followed five stages:

1. **Benign examples:** GPT-3.5-Turbo rewrote repetitive SEP instructions, expanding the data to 10,000 distinct benign pairs.
2. **Probe–witness pairs:** The researchers manually created 100 simple questions with deterministic answers. For example, the probe “Name the first month of a year” has the witness “January.” If the target outputs the witness, the injected task likely succeeded. All five target LLMs were verified to answer the probes correctly when directly instructed.
3. **Attack generation:** Probes were inserted through Naive, Escape Character, Context Ignoring, and Fake Completion attacks, plus three pairwise combined attacks. Their distribution ratio was \(1:1:1:1:2:2:2\).
4. **Token labeling:** Attacks were placed at randomized positions in clean content. Character-level start and end positions were converted into model-specific token labels. Examples whose clean text already contained the witness were removed to avoid false success measurements.
5. **Splitting and quality checks:** The final data contains 100,000 injected and 10,000 benign instances. The authors manually inspected 1,000 randomly selected instances for attack deployment and label accuracy. The test set contains 5,000 injected and 5,000 benign examples; the remaining 100,000 examples are used for training. Train and test examples come from different instruction/data pairs and different attack-prompt generation methods.

The Appendix gives a detailed FIPI example: a fake-completion attack is inserted into a named-entity-recognition passage, with character positions 182–266 and token positions 39–66.

### Prototype and hyperparameters

The PyTorch prototype was trained using two NVIDIA A100 GPUs.

- Training response-token limit: \(m=32\), using trimming or zero-padding.
- Evaluation: truncate to 32 but do not pad.
- Two residual blocks, each with hidden dimension 512.
- Adam optimizer.
- Learning rate \(10^{-3}\).
- Annealing rate 0.3.
- Batch size 128.
- Mean-filter kernel \(k=5\).
- Consecutive-token threshold 5.

### Target models

The five target LLMs were deliberately varied:

- **ChatGLM-6B:** bilingual prefix decoder, multi-query attention, SwiGLU, 28 layers and 32 heads per layer.
- **Dolly-7B:** Pythia-6.9B derivative trained on about 15,000 instruction examples; causal decoder, sparse attention, GeLU, 32 layers and 32 heads.
- **Falcon-7B:** causal decoder, multi-query attention, GeLU, 32 layers and 71 heads.
- **LLaMA2-7B:** causal decoder, SwiGLU, 32 layers and 32 heads.
- **LLaMA3-8B:** grouped-query attention and scaled-corpus training, 32 layers and 32 heads.

### Baselines and metrics

Detection baselines included Prompt-Guard, ProtectAI-v2, Attention Tracker, TaskTracker, GPT/DeepSeek naive detection, GPT/DeepSeek response-based detection, and Known-Answer Detection.

Sanitization baselines included Sandwich, Spotlighting, Instructional defense, GPT-Loc, DeepSeek-Loc, and StruQ on LLaMA2.

Metrics were:

- **Accuracy:** overall detection correctness.
- **False-positive rate:** clean examples incorrectly flagged.
- **False-negative rate:** attacks incorrectly labeled clean.
- **Attack success rate:** fraction of attacks that compromise the target.
- **Win rate:** AlpacaEval2.0 preference for sanitized output over the corresponding benign output; 50% means parity.
- **Jaccard similarity:** shared words divided by the total unique words across sanitized and original clean text.

## 4. Results and Findings

### Overall IPI detection

**Table I** reports that RENNERVATE achieved:

| Model | Accuracy | FPR | FNR |
|---|---:|---:|---:|
| ChatGLM | 99.05% | 1.20% | 0.70% |
| Dolly | 97.88% | 2.42% | 1.82% |
| Falcon | 99.58% | 0.54% | 0.30% |
| LLaMA2 | 99.43% | 0.46% | 0.68% |
| LLaMA3 | 99.37% | 0.84% | 0.42% |

It outperformed every evaluated detector. On LLaMA3, Attention Tracker reached 83.23% and TaskTracker 95.07%, so RENNERVATE led them by 16.14 and 4.30 percentage points. GPT-Resp and DeepSeek-Resp reached 82.55% and 91.71%. Compared with the second-best LLaMA3 method, RENNERVATE improved FPR by 2.90 points and FNR by 5.70 points.

Other baselines exposed different failure patterns:

- Prompt-Guard had 64.43% accuracy and a 69.94% FPR.
- ProtectAI-v2 had 75.48% accuracy and a 46.52% FNR.
- GPT-Naive reached 84.40%; DeepSeek-Naive reached 81.14%.
- Known-Answer Detection varied severely by model, including 50.24% accuracy and 99.52% FNR on LLaMA3.
- DeepSeek response-based detection was the strongest broadly evaluated baseline, reaching 91.52% on Dolly and 91.71% on LLaMA3.

### IPI sanitization on FIPI

Without defense, total attack-success rates were:

- ChatGLM: 85.90%.
- Dolly: 72.10%.
- Falcon: 84.90%.
- LLaMA2: 67.10%.
- LLaMA3: 60.80%.

**Tables II and III** show that RENNERVATE reduced total ASR to:

- ChatGLM: 0.10%.
- Dolly: 0%.
- Falcon: 0%.
- LLaMA2: 0.20%.
- LLaMA3: 0.20%.

Thus the reductions were 85.80, 72.10, 84.90, 66.90, and 60.60 percentage points.

Across individual attacks, RENNERVATE usually reduced ASR to exactly zero. The nonzero cases were 0.90% for Context Ignoring on ChatGLM; 0.93% for Naive and 0.89% for Fake Completion on LLaMA2; and 0.93% for Naive and 0.18% for combined attacks on LLaMA3.

Prompt-modification defenses helped but were substantially weaker. For example, Spotlighting reduced Falcon’s total ASR from 84.90% to 35.10%. GPT-Loc was the strongest LLM-based sanitizer, reducing ASR by 75.60, 63.90, 75.10, 57.40, and 51.50 points across the five models. On LLaMA2, StruQ achieved 0.30% total ASR, close to RENNERVATE’s 0.20%, but StruQ requires model modification.

**Figures 4 and 5** present Jaccard-similarity boxplots for FIPI and five unseen cross-task datasets. FIPI similarities are predominantly 0.9–1.0, meaning sanitization generally preserves the original wording.

**Table IV** reports FIPI win rates of 46.37%, 44.34%, 44.59%, 43.60%, and 46.78% for ChatGLM, Dolly, Falcon, LLaMA2, and LLaMA3. These are close to the 50% parity point, supporting the claim that sanitization preserves legitimate task performance.

### Unseen datasets and cross-task scenarios

Five datasets were paired to form unseen task/injected-task combinations:

- MRPC–HSOL.
- Jfleg–RTE.
- SST2–MRPC.
- MRPC–SST2.
- RTE–Jfleg.

Each scenario contained 1,000 injected and 1,000 benign examples. Unlike FIPI’s probe attacks, these injections also included task-specific content, such as sentence pairs for an injected duplicate-detection task.

**Table V** shows high but uneven transfer performance. Accuracy ranges across the five scenarios were:

- ChatGLM: 96.90–100.00%.
- Dolly: 93.05–96.65%.
- Falcon: 82.20–99.55%.
- LLaMA2: 93.75–96.00%.
- LLaMA3: 80.20–99.95%.

The weakest cases were Falcon on RTE–Jfleg at 82.20% accuracy, with 21.50% FPR and 14.10% FNR, and LLaMA3 on MRPC–SST2 at 80.20%, with 35.30% FNR. Several combinations nevertheless approached perfect detection, including ChatGLM on SST2–MRPC at 100% and LLaMA3 on SST2–MRPC at 99.95%.

For sanitization, DeepSeek judged whether responses followed the injected task. A manual check of 200 balanced positive/negative cases found the judge 94.50% accurate.

**Table VI** shows large ASR reductions. In MRPC–HSOL, for example:

- ChatGLM: 98.10% to 0.20%.
- Dolly: 32.60% to 2.90%.
- Falcon: 64.10% to 0.20%.
- LLaMA2: 7.70% to 0%.
- LLaMA3: 76.10% to 2.20%.

Across all scenarios, most defended ASRs were low, though notable residual values included Falcon at 14.50% on Jfleg–RTE, Dolly at 10.90% on RTE–Jfleg, and LLaMA3 at 23.90% on MRPC–SST2.

Jaccard scores in Figures 4 and 5 were generally above 0.8. Utility win rates in Table IV, however, varied substantially:

| Scenario | ChatGLM | Dolly | Falcon | LLaMA2 | LLaMA3 |
|---|---:|---:|---:|---:|---:|
| MRPC–HSOL | 40.36 | 38.61 | 52.93 | 9.84 | 38.88 |
| Jfleg–RTE | 5.07 | 16.57 | 1.90 | 5.03 | 12.33 |
| SST2–MRPC | 29.79 | 29.66 | 23.56 | 8.05 | 14.84 |
| MRPC–SST2 | 53.68 | 42.22 | 53.03 | 44.35 | 33.45 |
| RTE–Jfleg | 35.08 | 39.41 | 35.61 | 43.73 | 42.68 |

The authors attribute low values to injected-task-specific content that may remain after the explicit instruction is deleted.

**Table XII** tests injections containing only instructions. Utility improves markedly:

- MRPC–HSOL: 40.26–54.40%, except LLaMA2 at 10.55%.
- Jfleg–RTE: 17.28–35.33%.
- SST2–MRPC: 37.43–43.71%, improving by more than 10 points for every model.
- MRPC–SST2: 43.03–52.17%.
- RTE–Jfleg: 44.77–51.76%.

Jfleg–RTE remained near 20% for several models because grammar correction requires exact text; one wrongly removed token can hurt the evaluation.

### Transfer to unseen gradient-based attacks

GCG and Neural Exec were not included in RENNERVATE’s training. The evaluation used LLaMA2, five datasets, 200 examples per dataset, 500 GCG iterations, and 250 Neural Exec iterations.

**Table VII** reports:

- GCG detection accuracy: 92.50–100%.
- Neural Exec detection accuracy: 100% on every dataset.
- GCG ASR without defense: 94.00–100%.
- GCG ASR after sanitization: 0–7.00%.
- Neural Exec ASR without defense: 83.00–97.50%.
- Neural Exec ASR after sanitization: 0% everywhere.

**Figure 6** shows GCG Jaccard scores generally around 0.90–0.95. Neural Exec produces lower similarity because its learned suffixes contain more meaningful words, which are harder to distinguish precisely from legitimate text than GCG’s more punctuation-like suffixes.

### Adaptive adversaries

PAIR and TAP dynamically refine attacks using target responses. DeepSeek served as attacker and judge. PAIR could make up to 20 queries; TAP used depth 7, width 10, branching factor 4, and at most 70 queries. Each produced 100 FIPI attacks.

**Table VIII** shows that undefended PAIR reached 94–100% ASR and TAP reached 95–100%. With RENNERVATE:

- PAIR: 0% ChatGLM, 1% Dolly, 1% Falcon, 0% LLaMA2, 19% LLaMA3.
- TAP: 0% ChatGLM, 2% Dolly, 2% Falcon, 0% LLaMA2, 9% LLaMA3.

The defense reduced ASR by more than 75 points in every setting.

For a white-box adaptive GCG attack, the attacker added a loss explicitly designed to make token-level injections appear clean. Using 500 iterations, **Table IX** reports undefended ASRs of 98.50%, 98.50%, 99.50%, 98.00%, and 93.00% across FIPI, MRPC, Jfleg, SST2, and RTE. RENNERVATE reduced them to 3%, 2%, 2%, 0%, and 5%.

### Ablation findings

**Table X** evaluates components on Dolly across six datasets.

- Replacing two-step pooling with one response-token pooling layer improved FIPI from 97.88% to 99.53% and MRPC–SST2 from 93.10% to 94.20%, but reduced transfer accuracy by 1.30 points on MRPC–HSOL, 11.60 on Jfleg–RTE, 12.65 on SST2–MRPC, and 3.65 on RTE–Jfleg. Two-step pooling therefore mainly improves generalization.
- Replacing the token-level detector with a Transformer classifier gave broadly comparable accuracy, sometimes higher, but required about 12.5 times as many parameters. RENNERVATE used only 8% of its parameters and retained the ability to localize and sanitize tokens.
- Removing the mean filter lowered accuracy by 0.62, 6.55, 8.90, 7.15, 3.75, and 0.40 points across the six datasets.

### Hyperparameter effects

**Table XI** shows:

- Increasing kernel size from 2 to 6 generally improved accuracy, though gains diminished. Relative to \(k=2\), \(k=5\) changed the six accuracies by −0.05, +2.65, +5.25, +0.40, +0.30, and 0 points.
- One response token produced accuracies of only 73.10–92.00%. With two tokens, results rose to 89.45–94.45% on five datasets and 92.96% on FIPI. Performance generally improved further through 16 tokens, showing that only a few response tokens can already be informative.
- More residual blocks improved FIPI somewhat, from 97.65% at one block to 98.18% at 16. Excessive depth hurt transfer: moving from 2 to 16 blocks reduced Jfleg–RTE accuracy by 9.95 points and RTE–Jfleg by 7.00 points.

### Error examples and workflow visuals

**Figure 7** explains two errors:

- A benign role-playing instruction was classified as malicious because it resembled an embedded task, causing a false positive.
- A naive injected instruction was missed because ChatGLM treated it as ordinary text rather than executing it. Only two words were flagged, fewer than the threshold needed for document-level detection.

**Figure 8** visualizes the full workflow. A fake-completion-style instruction is inserted into an electric-vehicle market passage. Token-level detection highlights the malicious span, the consecutive-token criterion classifies the document as injected, and sanitization strikes out the detected text while retaining the surrounding clean passage.

### Parameter size

**Table XIII** compares model sizes:

- Prompt-Guard: 86M.
- ProtectAI-v2: 98M.
- GPT-3.5 detection methods: at least 175B.
- DeepSeek-v2.5 methods: 236B.
- Known-Answer: the 6B–7B target LLM.
- TaskTracker: 4K.
- RENNERVATE: 0.5–0.8M.

Attention Tracker is statistical and has no listed learned-model size. RENNERVATE is much smaller than neural classifier and auxiliary-LLM baselines while also supporting sanitization.

## 5. Analysis and Interpretation

The results support the paper’s main hypothesis: the way an LLM attends to a token provides a transferable signal about whether the model interprets that token as an instruction.

The strongest evidence is that a detector trained on black-box FIPI attacks continued to recognize unseen cross-task injections, GCG, Neural Exec, PAIR, TAP, and even a GCG variant explicitly optimized to evade it. This suggests that RENNERVATE captures a property of model processing rather than merely memorizing obvious words such as “ignore.”

The two-step pooling mechanism is particularly important for transfer. It learns which response tokens and attention heads contribute to injection analysis, while weighted standard deviations accommodate variable-length responses. Its benefit is less visible on the training-like FIPI distribution than on new task combinations.

Fine-grained token localization addresses a service-availability problem in prior binary detectors. Instead of rejecting the entire retrieved document, RENNERVATE can retain most clean content. High Jaccard scores and near-parity FIPI win rates show that this often succeeds.

The authors nevertheless distinguish removal of explicit adversarial instructions from removal of accompanying task content. RENNERVATE is better at the former. If an injection includes ordinary-looking content needed by the attacker’s task, some of that content may survive and interfere with the legitimate task. Table XII’s utility improvements after excluding such content support this explanation.

The consecutive-token threshold improves robustness to isolated false labels but introduces a trade-off. It prevents a few accidental token errors from triggering alarms, yet can miss a short or weakly recognized injection, as Figure 7 demonstrates.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **RENNERVATE:** a unified system for both detecting and sanitizing indirect prompt injection without retraining the target LLM.
- **Attention-based token classification:** it uses the target model’s internal attention behavior rather than relying only on attack wording, document embeddings, or an auxiliary LLM.
- **Two-step attentive-statistics pooling:** response-token and attention-head information is weighted and aggregated into stable token-level features.
- **Fine-grained recovery:** malicious tokens can be removed while clean portions of retrieved data remain available to the application.
- **FIPI:** a dataset with 100,000 injected examples, 10,000 benign examples, 100 probe–witness pairs, 300 subtasks, randomized attack positions, and character- and token-level labels.
- **Broad evaluation:** 15 commercial and academic baselines, five structurally different LLMs, FIPI and five unseen task combinations, unseen gradient attacks, and adaptive black- and white-box adversaries.
- **Compactness:** the learned component contains approximately 0.5–0.8M parameters.

The Appendix also documents the exact prompt formats used for naive LLM detection, response-based detection, Known-Answer Detection, LLM sanitization, and DeepSeek judging, improving reproducibility.

## 7. Limitations and Caveats

- RENNERVATE requires access to internal attention weights. Users of closed API-only models cannot deploy it directly unless the provider exposes or integrates it.
- A proposed workaround is to run a local shadow model, such as ChatGLM-6B, with RENNERVATE. The paper states that the shadow system can operate on one NVIDIA RTX 3090, but its empirical results primarily concern defenses attached to the evaluated target models.
- The defender assumes white-box model knowledge even though it does not know the attack.
- Sanitization may fail to remove injected-task-specific content that resembles normal data, producing substantial utility losses on some unseen task combinations.
- Exact-output tasks such as grammar correction are especially sensitive to a single misclassified or deleted token.
- Neural Exec’s meaningful lexical suffixes reduce post-sanitization textual similarity compared with GCG.
- The consecutive-run threshold can miss attacks when only a few malicious tokens are detected.
- Legitimate role-playing or task-like text can be falsely flagged because it resembles an embedded instruction.
- Some transfer settings remain difficult: LLaMA3 reached only 80.20% detection accuracy on MRPC–SST2, and Falcon reached 82.20% on RTE–Jfleg.
- Residual adaptive vulnerability remains, particularly PAIR on LLaMA3 at 19% ASR and TAP on LLaMA3 at 9%.
- DeepSeek-based judging of cross-task attack success was 94.50% accurate rather than perfect.
- StruQ was evaluated only on LLaMA2 because its official model availability was limited.
- Increasing detector capacity does not uniformly improve generalization; excessive residual depth reduced accuracy on unseen datasets.
- The present work addresses textual IPI. Image- and audio-based attacks are outside its evaluated scope.

## 8. Future Work or Open Questions

The authors identify two main directions:

1. **Better recovery from IPI:** Token-level sanitization is presented as an initial recovery mechanism, but more work is needed to reconstruct clean data accurately, especially when malicious instructions are intertwined with injected-task-specific content.
2. **Multimodal IPI defense:** Future LLM applications may retrieve images and audio as well as text. The authors propose exploring unified representations across modalities so that malicious content can be detected and sanitized consistently.

Other open technical issues exposed by the results include improving short-injection detection without raising false positives, distinguishing legitimate embedded instructions from attacks, preserving exact-output tasks, and defending closed-model API users without direct attention access.

## 9. High-Level Takeaway (Plain Language)

Indirect prompt injection happens when a webpage or other external source secretly tells an AI agent to ignore the user and do something else. RENNERVATE watches how the AI’s attention system reacts to every token, identifies stretches that behave like hidden instructions, and removes them. Across five LLMs, it achieved roughly 98–99.6% detection accuracy and usually reduced successful attacks to near zero, including attacks it had never seen. Its main unresolved problem is that malicious task-related content can look like ordinary data, so removing the explicit command does not always preserve the original task perfectly.