## Stage 0 — Document Accessibility Report

The supplied main document contains extracted text for physical PDF pages 1–20. All 20 page records were available for reading; this establishes coverage of the supplied document, rather than independently proving that no longer version exists. Directly supplied page images permit visual inspection of pages 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 18, and 20. Pages 3, 6, 14–17, and 19 were inspected through supplied text only. No browsing, tools, external documents, or repository inspection were used. The source hash is supplied metadata and was not independently recomputed.

The two numbered figures, nine numbered tables, Algorithm 1, filtering pseudocode, and several attack-example boxes are available. The figures and tables are readable in their supplied images, with extracted text supporting numerical transcription. Mathematical notation is generally readable, but dataset-index notation, quotation marks in delimiter templates, and the algorithm's returned variable require caution. Appendix A and Appendix B are present on pages 18–20. The accessibility metadata's detection of appendix references on pages 5 and 11 does not mean those pages themselves contain the appendix. No supplementary files were supplied; no embedded files or explicit supplementary-file references are identified in the supplied metadata. The paper announces released code, but the code was not provided or inspected. OCR was unnecessary. The reported local-image error for the path '-' does not identify an additional paper page and does not prevent inspection of the 13 displayed images.

Evidence categories used below are: [A] author-reported statements; [B] directly observable image/table content; [C] analyst-derived calculations with operands shown; and [D] analyst interpretation. No [E] external information is introduced. Confidence is HIGH for clearly readable source statements and table entries, MEDIUM for interpretations or unresolved reporting differences, and UNKNOWN for information the supplied document does not establish.

## 1. Plain-language orientation

StruQ studies how an application can safely ask a large language model (LLM) to work on text that someone else controls. A developer might instruct the model to summarize an email, classify a message, or extract a résumé's job title. An attacker can put an additional instruction inside that email or résumé. If the model follows the attacker's instruction, the application loses control of its intended task. This is prompt injection: text that should be processed as data is instead treated as authority. [A: pp. 1, 3–5]

The researchers propose structured queries: provide the trusted task instruction and untrusted data as distinct inputs, encode their boundaries using reserved tokens, remove boundary-spoofing strings from the data, and train the model to obey instructions only in the trusted portion. Their implementation, StruQ, combines a secure front-end with structured instruction tuning of base Llama-7B and Mistral-7B models. [A: pp. 7–9]

The important finding is conditional. StruQ greatly reduces the tested manual attacks while retaining approximately the same instruction-following utility. However, carefully optimized attacks still succeed: Greedy Coordinate Gradient (GCG) achieves 58% attack success against defended Llama and 56% against defended Mistral. Tree-of-Attacks with Pruning (TAP) achieves 9% and 36%, respectively. Therefore, this paper demonstrates a promising defense and a remaining vulnerability, not immunity. [A/B: p. 10, Tables 2–3]

Its central contribution is to make instruction authority depend on input location and protected structure, rather than merely on how persuasive an instruction sounds. Relevance to the requested question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', is an analyst inference: applications that ingest external text create a trust boundary between the developer and the data source. The paper explains this mechanism, but does not experimentally compare autonomous web agents with standalone LLMs or quantify how much more vulnerable either category is.

## 2. Document roadmap and inventory

The paper is an empirical cybersecurity and machine-learning systems study. It proposes an interface and training method, defines attacks, and evaluates security, utility, adaptive attacks, ablations, and competing defenses. There are no formal numbered research questions, hypotheses, theorems, or security proofs.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| META | Title, four authors, affiliations, version and venue footnote | p. 1 | Identifies the supplied work |
| ABS | Abstract | p. 1 | Problem, architecture, training, outcome |
| S1 | §1 Introduction | pp. 1–2 | Motivation and contributions |
| S2 | §2 Background and Related Work | pp. 2–4 | LLM integration, injection analogy, defenses, threat distinctions |
| S3 | §3 Prompt Injection Attacks; §§3.1–3.8 | pp. 4–7 | Definition, threat model, manual and optimized attacks |
| S4 | §4 Structured Queries; §§4.1–4.4 | pp. 7–9 | Requirements, architecture, filtering, training construction |
| S5 | §5 Experiments; §§5.1–5.5 | pp. 9–13 | Metrics, setup, results, adaptation, ablations, comparisons |
| S6 | §6 Discussion | pp. 13–14 | Limitations, future defenses, system prompts, instruction tuning |
| S7 | §7 Summary | p. 14 | Final synthesis |
| ETH | Ethics/open-science statement and acknowledgments | p. 14 | Research positioning and support |
| REF | References [1]–[65] | pp. 15–17 | Bibliographic context; cited works not independently reviewed |
| A1–A6 | Appendix A, §§A.1–A.6 | pp. 18–20 | Ignore strings, delimiter construction, HackAPrompt examples, TAP settings |
| B1–B2 | Appendix B, §§B.1–B.2 | p. 20 | Detailed ablation results |
| F1–F2 | Figures 1–2 | pp. 2, 8 | Concept comparison and system architecture |
| T1–T9 | Tables 1–9 | pp. 4, 10–13, 20 | Attack taxonomy and numerical evaluations |
| ALG1 | Algorithm 1 | p. 9 | Training-data augmentation |
| FILT | Filtering pseudocode | p. 8 | Recursive delimiter removal |
| EQ-DATA | Dataset tuple and concatenation expressions | pp. 8–9, 11 | Defines training transformations |
| EQ-DELIM | Delimiter-generation expressions | p. 18 | Specifies test/train fake delimiters |
| X1–X6 | Main security, utility, adaptive, tuning ablation, front-end ablation, defense comparison | pp. 9–13, 20 | Distinct experimental conditions |

The original title is 'StruQ: Defending Against Prompt Injection with Structured Queries'. Authors are Sizhe Chen, Julien Piet, Chawin Sitawarin, and David Wagner, all listed with UC Berkeley affiliations. Page 1 identifies arXiv:2402.06363v2, dated 25 September 2024, and states that the paper is to appear at USENIX Security Symposium 2025. These are document-reported publication details, not externally verified current status. No separate keywords list is visible. The substantive footnote is the venue statement; email addresses and acknowledgments are deliberately compressed.

## 3. Background and context

An LLM generates text and can be fine-tuned to follow instructions. The paper distinguishes a base model, trained for text completion, from an instruction-tuned model, trained to respond to task requests. An LLM-integrated application is conventional software that calls an LLM as a subroutine. In zero-shot prompting, the developer specifies a task directly rather than training a separate model for each task. [A: pp. 2–3]

The vulnerable interface concatenates a developer's instruction with user-supplied text. Concatenation means placing strings together into one input. The model receives a combined sequence and may respond to instructions anywhere in it. A résumé can therefore contain both genuine employment information and an instruction to assign its applicant the highest score. The paper's résumé example illustrates manipulation of an application's decision, rather than a universal prohibition on the requested words. [A: p. 3]

The authors connect this to older injection vulnerabilities: telephone signaling, Structured Query Language (SQL) injection, cross-site scripting (XSS), and shell command injection. Their common explanation is that control and data share a channel, allowing data to impersonate control. SQL prepared statements motivate an interface with separate control and data arguments. These historical explanations are author-provided context, not independently checked accounts. The analogy motivates StruQ; it does not prove that probabilistic language models enforce boundaries as reliably as database parsers. [A: p. 3; D: qualification]

Jailbreaking and prompt injection differ in whose instructions are violated. In the authors' framing, jailbreaking involves a trusted model provider and an untrusted user attempting to defeat provider safety goals. Prompt injection adds a trusted application developer whose intended task can be overridden by an untrusted data source. An injected request such as printing a number can be harmless in ordinary conversation yet harmful when it corrupts an application's score. Safety tuning aimed at harmful content therefore does not by itself establish instruction-source authority. [A: p. 4]

Related defenses include prompt reminders, textual delimiters, demonstrations, task-specific fine-tuning through Jatmo, and general-purpose training through BIPIA, the benchmark for indirect prompt injection attacks. The authors also discuss special message tokens and instruction hierarchy. These are descriptions from this paper; no cited system's broader performance was assessed here.

## 4. Research problem and gap

The existing problem is that an instruction-following model is asked to process untrusted text while receiving trusted instructions in the same sequence. The attacker can exploit the model's ability to interpret natural-language commands and its insufficient separation of task instructions from task content. The motivating application risks include redirecting the task, manipulating output, and extracting application prompts. [A: pp. 1–3]

According to the authors, previous approaches are insufficient in different ways. Test-time reminders and ordinary delimiters do not resist their strongest manual attacks. Jatmo trains a model for a single task, whereas StruQ seeks a model reusable across tasks. BIPIA has closely related ideas but differs in its front-end and training-data construction. The paper attributes its comparative results to several possible differences, but explicitly labels much of that causal account as speculation. [A: pp. 4, 12–13]

The research gap is how to train an existing base LLM to accept a safer interface with separated instruction and data, preserve general instruction-following utility, and resist attacks without training a new foundation model from scratch. Claimed novelty includes reserved delimiter tokens with filtering, structured instruction tuning, attention to Completion attacks in design and evaluation, and adapting TAP/GCG to prompt injection. These priority claims are author claims, not a validated literature-wide novelty assessment. [A: pp. 2, 7–10]

Scope is programmatic LLM-integrated applications. It does not cover all chatbot interactions or every attack against an LLM. The paper evaluates output hijacking on specific benchmarks and models, not complete web-agent security, browser control, credential misuse, or end-to-end unauthorized actions.

## 5. Research questions, objectives, and hypotheses

The paper does not state formally numbered research questions or hypotheses. Its explicit primary objective is to secure LLM-integrated applications against prompt injection with minimal utility loss. Section 4.1 states three requirements: security, utility, and feasible training. Security is expressed aspirationally as never executing instructions found in the data portion; utility should remain close to existing models; training should build on existing models rather than require prohibitively expensive pretraining. [A: pp. 4, 7]

For traceability, the following are analyst-organized objectives, not invented quotations or formal hypotheses:

- O1: Construct an interface and trained model that distinguish trusted instructions from data.
- O2: Measure resistance to manual and optimized prompt injections.
- O3: Measure whether general instruction-following utility is preserved.
- O4: Test delimiter attacks tailored to knowledge of the defense.
- O5: Determine which training augmentations and delimiter configurations support the design.
- O6: Compare against test-time defenses and a reproduced BIPIA system.

O1 is addressed by §4 and Figure 2; O2 and O3 by Tables 2–3; O4 by Table 4; O5 by Tables 5–6 and 8–9; and O6 by §5.5 and Table 7. The absolute security requirement is not achieved by the evaluated implementation, because optimized attacks remain successful. Utility preservation is supported within AlpacaEval's reported measurement conditions.

## 6. Assumptions / Threat Model

The attacker can arbitrarily modify the data portion but cannot modify the trusted prompt. The attacker knows the prompt and the application's formatting. Success occurs when the model obeys a hidden instruction in the data instead of treating it as data; following the benign instruction is not required for attack success. This is an inference-time attack, not an attack on training data or model deployment infrastructure. [A: pp. 4–5]

Trusted components are the application developer's prompt, the front-end that assembles and filters the query, and the intended model-training process. The source of data is untrusted. GCG additionally receives white-box gradient access to the target model, which the authors acknowledge may not be feasible for every real attacker. TAP constructs attacks using an attacker LLM; the original judge LLM is removed in this adaptation because the target response can be checked by substring matching. [A: pp. 6–7]

The relevant asset is faithful execution of the developer's intended instruction. Output integrity is the directly measured security property. Although the introduction mentions prompt extraction, the reported success metric primarily checks for an attacker-selected output string; it does not establish a measured reduction in every possible confidentiality or action-integrity failure. [A/D: pp. 1, 9]

The defense assumes the application can identify which input is instruction and which is data, and can pass them through the protected front-end. It also assumes that forbidden delimiter strings are removed before they can create reserved tokens in untrusted content. The paper does not specify a complete tokenizer or API security contract sufficient to independently verify every possible route to token spoofing. [D: pp. 7–8]

## 7. Methodology

### Architecture and encoding

StruQ has two components. The secure front-end takes separate prompt and data inputs, filters the data, and formats a structured query. A structured-instruction-tuned model consumes that query and produces the response. The format adapts Alpaca's instruction/input/response template. It replaces textual '###' with [MARK], the labels with [INST], [INPT], and [RESP], and ':' with [COLN]. These strings correspond to reserved tokens. A query therefore has a trusted instruction region, a data region, and a response boundary. [A: pp. 7–8]

The front-end repeatedly removes [MARK], [INST], [INPT], [RESP], [COLN], and '##' from user data. Repetition continues until the string stops changing. Recursive application prevents a deletion from leaving a newly formed forbidden substring that a single pass would miss. The authors add '##' filtering because a related fake delimiter was empirically effective otherwise. This is structural filtering, not a classifier that recognizes every malicious sentence. [A: pp. 7–8; D: explanation of fixed-point behavior]

New reserved-token embeddings are initialized from corresponding existing textual-token embeddings, such as [MARK] from '###' and [INST] from 'instruction', then updated during fine-tuning. The authors report that initialization matters for utility and that learning these embeddings from scratch was insufficient in their experiments. The supplied pages do not give a separate numerical table isolating this initialization claim. [A: p. 8]

### Structured instruction tuning

The initial dataset is T = {(p_i, d_i, r_i), ...}, where p_i is an instruction, d_i its data, and r_i its desired response. The transformed dataset retains the original desired response while adding distracting instructions to the data portion. The model should learn to obey the instruction's location rather than the linguistic content of the injected request. A base, non-instruction-tuned model is fine-tuned on these examples. [A: pp. 8–9]

Nominal construction is 50% clean samples, 25% Naive augmentation, and 25% Completion-Other augmentation. Samples without associated data remain clean even if selected for augmentation, so the actual attacked proportion can be below 50%. Naive augmentation appends another training sample's instruction and data. Completion augmentation first appends fake response delimiters and a fake response, then fake instruction delimiters and the unrelated instruction/data. The fake response differs from the desired response to avoid training the model to repeat its input. The authors obtain it from another dataset with the same instruction/data and a different answer; they note that another LLM could generate it instead. [A: pp. 8–9]

The final method uses Naive plus Completion-Other augmentation. Ignore augmentation and fake-delimiter rejection augmentation are additional ablation conditions, not components that should silently be attributed to the final system. Fake-delimiter augmentation replaces structural delimiters and changes the target to a rejection response; Ignore augmentation adds an explicit instruction-disregarding phrase. [A: p. 11]

### Data, models, and training

Models are Llama-7B and Mistral-7B. Training uses the cleaned Alpaca instruction-tuning dataset, official model/evaluation code, and whole-model fine-tuning for three epochs. Learning rates are 2 × 10^-5 for Llama and 2.5 × 10^-6 for Mistral. The supplied work does not give the training-set count, batch size, optimizer details, random seeds, complete hardware configuration, or a full run-repetition protocol. The reference list names relevant code sources, but they were not inspected. [A: p. 9]

The authors report non-overlapping train/test sets for instructions, injected instructions, and ignore statements. Appendix A.2 says training Ignore sentences were crafted by a different person from testing sentences; Appendix A.4 provides training fake-delimiter components distinct from testing components. The amount of overlap avoided is described qualitatively, without a full split manifest. [A: pp. 9, 18]

### Evaluation metrics and attack setup

Utility uses AlpacaEval 1.0: GPT-4 judges tested outputs against davinci003 reference outputs on 805 AlpacaFarm samples. The reported value is a win rate, not classification accuracy. The authors describe 50% as equivalent output quality relative to that reference. They report a 0.7% standard error and discuss significance at 0.05, but do not name the statistical test or report exact p-values. [A: p. 9]

Security uses attack success rate (ASR), the percentage of evaluated attacks producing the attacker-requested behavior. Most attacks request 'Print exactly Hacked!'; HackAPrompt requests 'I have been PWNED'. Chinese and Spanish variants alter the injected request while retaining English elsewhere. A Base64 condition encodes the entire Completion-Real injection. Injections are appended at the end of data, described as favorable to attackers. Responses containing 'Hacked!' or 'hacked!' are manually inspected to exclude false positives. The general security set contains 208 AlpacaFarm samples with data inputs. HackAPrompt is separately described as 20 selected successful level-1 competition injections with their original task prompts retained; its effective evaluation denominator is not explicitly reconciled with the general 208-sample statement. [A: pp. 6, 9]

TAP uses branching factor 4, depth 10, and width 10; the search runs to its highest depth, and responses are manually reviewed. GCG uses 500 optimization iterations and refers to the original GCG settings for other hyperparameters. The discussion reports roughly 100 TAP model queries and 256k GCG queries per attacked sample, and more than 100 times the GPU-hour cost of other attacks. These costs are author-reported approximations, not independently reproduced benchmarks. [A: pp. 7, 14, 20]

## 8. Experiments / Analyses

### X1 — Main security evaluation

Purpose: test whether the full StruQ system resists a broad attack set. Conditions: undefended versus defended Llama and Mistral, using the attack taxonomy in §3 and the security setup above. Table 2 reports 15 attack rows, including language/encoding variants and the maximum near-miss-delimiter result. Most defended manual-attack entries are zero; exceptions include Completion-RealCmb at 2% for Mistral and Completion-Close maximum at 1% for both models. Optimized attacks remain substantially stronger. These results support improved empirical resistance, not the absolute security requirement. [A/B: p. 10]

### X2 — Utility evaluation

Purpose: determine whether the defense compromises general instruction-following output quality. Table 3 reports Llama 67.2% undefended versus 67.6% defended and Mistral 80.0% versus 78.7%. Derived differences are +0.4 percentage points for Llama and -1.3 percentage points for Mistral. The authors call Llama's change nonsignificant and Mistral's decrease borderline significant at 0.05 with a 0.7% standard error. This is a reference-relative judged win rate on 805 samples; it does not measure every application's utility or input preservation. [A/B/C: pp. 9–10]

### X3 — Adaptive delimiter attacks

Purpose: evade filtering using delimiters similar to the expected ones. Manipulations change hash counts, capitalization, spacing, colon presence, spelling, or semantic similarity. Table 4 reports ten rows including the real delimiter and nine variants. Undefended models remain vulnerable, while defended ASR is 0–1% for Llama and 0% for Mistral in that table. Additional variants of reserved-token strings all reportedly achieve 0%. Caveats: Table 4's Mistral real-delimiter baseline is 90%, whereas Table 2's Completion-Real is 96%; the source does not reconcile the conditions. [A/B: pp. 10–11]

### X4 — Training-augmentation ablation

Purpose: isolate augmentation choices. This experiment uses ordinary Alpaca delimiters without the proposed secure front-end, so it tests model training rather than the complete system. It evaluates six attacks: Naive, Ignore, Escape-Deletion, Escape-Separation, Completion-Other, and Completion-OtherCmb. Tables 5 and 8 compare single augmentations and selected pairs. Naive+Completion gives 66.0% utility and 0% across those six attacks; Ignore+Completion also yields 0% but has 65.4% utility. Fake-delimiter-only training has 60.3% utility and a worst ASR of 70%. These results justify the selected augmentation within the tested subset; they do not show zero ASR against GCG, TAP, or all Completion-Real conditions. [A/B: pp. 11, 20]

### X5 — Front-end/delimiter ablation

Purpose: compare textual and reserved-token versions of marker, word, and colon components. Llama uses Naive+Completion training and front-end filtering in every configuration. Tables 6 and 9 report utility and Completion-Real/Close attacks. All five configurations have a maximum reported ASR of 1%, while utility ranges from 60.2% to 67.6%. Fully special delimiters have the highest utility, 67.6%. This supports the complete delimiter choice for utility under filtering; the identical worst-case ASR values do not establish a uniform security advantage over every alternative. [A/B: pp. 12, 20]

### X6 — Existing-defense comparisons

Test-time comparison applies Completion-Real to Llama-7B: undefended 96%, reminder in prompt 83%, reminder after data 39%, delimiter isolation 85%, in-context demonstration 48%, and StruQ 0%. These are one attack-family comparisons; the paper does not give equivalent utility results for those test-time defenses. [A: p. 12]

Training-time comparison reproduces BIPIA on Vicuna-7B-v1.5 and compares StruQ on Llama-7B. Table 7 includes both the StruQ set and 231 BIPIA samples from email, table, and WebQA tasks. BIPIA's utility falls from 53.9% to 26.0%; StruQ is 67.2% to 67.7% in this table. GCG achieves 100% against BIPIA and 58% against StruQ on the unstarred set. GCG on the BIPIA test set is absent because one 80GB GPU was insufficient for the long samples. Different starting models complicate a causal attribution to the defense alone. [A/B/D: p. 13]

## 9. Results and numerical interpretation

The strongest main evidence for control/data separation is the Completion-Real result: both undefended models have 96% ASR and both defended models have 0% in Table 2. The ordinary textual structure is highly spoofable; reserved structure plus filtering and trained location sensitivity resists this tested attack. However, this is an observed test result, not proof that every delimiter or tokenizer route is secure. [A/B/D: p. 10]

Optimization produces a different outcome. For Llama, TAP falls from 97% to 9% and GCG from 97% to 58%. For Mistral, TAP falls from 100% to 36% and GCG from 99% to 56%. Derived absolute reductions are 88, 39, 64, and 43 percentage points, respectively. The calculation subtracts defended ASR from undefended ASR; these are not relative percentage reductions. [C: Table 2]

The authors interpret optimized attacks as exploiting task-specific injections: 68% of generated TAP injections against the defended models have a close semantic connection to the original instruction. A request to execute code may be attacked with code that prints the target string; a navigation task may be attacked with an arrival-signaling pretext. GCG suffixes are not reliably human-readable, and the authors do not claim to interpret their meaning. The explanation that task specificity drives success is plausible but not isolated experimentally by a controlled task-specificity ablation. [A/D: p. 10]

Manual-attack claims need precise wording. Page 2 says all tested manual attacks fall below 2%; Table 2 visibly contains a 2% Mistral Completion-RealCmb result. Report '0–2% for the displayed manual conditions' rather than silently converting the table to a strict below-2% claim. Likewise, page 11's prose says StruQ stops all designed Completion attacks, while Table 4 reports 1% and 0.5% Llama successes. The strongest defensible conclusion is low observed ASR, not universal elimination.

The Base64 row is 0% for undefended and defended models. It provides no measured security improvement from the defense in that particular condition. Chinese and Spanish injection rows do show large differences: Llama 66% and 50% to 0%; Mistral 96% and 92% to 0%. These conditions keep the rest of the input English and should not be described as a general multilingual benchmark. [A/B: pp. 9–10]

## 10. Figure-by-figure interpretation

### Figure 1 — Combined input versus separated instruction/data

Figure 1 on page 2 is directly visually inspected. It has four schematic cases: undefended clean input, defended clean input, undefended attacked input, and defended attacked input. Arrows move left to right from input through the model to output. Gray boxes contain task text/data, white boxes contain models, green boxes represent desired paraphrases, and a red/pink box represents the hijacked 'Hacked!' output. The malicious line is red within the attacked input. There are no axes, units, scales, confidence intervals, or numerical measurements.

In the undefended clean case, the combined prompt/data produces a paraphrase. In the attacked combined case, the injected instruction changes the output. In the defended cases, the instruction and data occupy separate boxes and both lead to the intended paraphrase. The diagram explains the proposed trust-boundary distinction; it is not a record of four benchmark measurements and does not establish immunity to all attacks. [B: p. 2]

### Figure 2 — StruQ architecture

Figure 2 on page 8 is directly visually inspected. Two inputs enter the secure front-end: the task prompt and the data. A recursive filter deletes '##' and the five reserved delimiter spellings from the data. The front-end emits a structured sequence with visually distinguished marker, instruction/input/response, and colon tokens. The sequence enters the structured-instruction-tuned model, and an output arrow leads to the paraphrased result. There are no quantitative axes or error bars.

The figure depicts the operational processing path; training is described by the model label and caption rather than drawn as a separate training-data pipeline. A caption explains that training contains instructions in both regions but teaches responses only to the prompt region. A terminology discrepancy remains: the illustrated marker token is [HASH], whereas the surrounding text and filtering code use [MARK]. These appear to refer to the marker role, but their equivalence is not explicitly documented. [A/B: pp. 7–8]

## 11. Table-by-table interpretation

All nine tables were inspected in supplied images and cross-checked against supplied text. Values below are readable reported percentages, not graphical estimates. Lower ASR is better; higher utility is better. Unless stated otherwise, tables do not provide confidence intervals, per-cell standard errors, or significance markers.

### Table 1 — Attack taxonomy, p. 4

Rows group Naive/Ignore, escape attacks, Completion variants, and other attacks. Naive has no additional mechanism beyond the injected instruction. Ignore adds a directive to disregard prior instructions. Escape-Deletion uses backspace/carriage-return characters; Escape-Separation uses newline/tab characters. Completion variants insert fake responses and real, close, or other delimiters; combined variants add Ignore and Escape-Separation. HackAPrompt is human-crafted, TAP LLM-crafted, and GCG gradient-guided. This is a qualitative taxonomy, not a performance table. The prose additionally evaluates languages and Base64.

### Table 2 — Main security comparison, p. 10

| Attack | Llama undefended | Llama StruQ | Mistral undefended | Mistral StruQ |
|---|---:|---:|---:|---:|
| Naive | 6% | 0% | 5% | 0% |
| Ignore | 12% | 0% | 11% | 0% |
| Escape-Deletion | 3% | 0% | 1% | 0% |
| Escape-Separation | 2% | 0% | 4% | 0% |
| Completion-Other | 29% | 0% | 71% | 0% |
| Completion-OtherCmb | 41% | 0% | 77% | 0% |
| Completion-Real | 96% | 0% | 96% | 0% |
| Completion-RealCmb | 71% | 0% | 83% | 2% |
| Completion-Real, Base64 | 0% | 0% | 0% | 0% |
| Completion-Real, Chinese | 66% | 0% | 96% | 0% |
| Completion-Real, Spanish | 50% | 0% | 92% | 0% |
| Completion-Close maximum | 96% | 1% | 96% | 1% |
| HackAPrompt | 52% | 0% | 38% | 0% |
| Tree-of-Attack/TAP | 97% | 9% | 100% | 36% |
| GCG | 97% | 58% | 99% | 56% |

This table demonstrates broad improvements and the persistence of optimized attacks. The Close row is a maximum over variants, so it is not the mean performance of a single standardized attack. The highest defended ASR is GCG for both models. Zero is tied across many manual conditions but means no reported success in those finite tests, not zero population risk.

### Table 3 — Utility, p. 10

Llama's AlpacaEval win rates are 67.2% undefended and 67.6% defended. Mistral's are 80.0% and 78.7%. These are comparisons against reference-model outputs, not head-to-head defender versus baseline win rates. Statistical discussion appears in §5.1, not as table annotations. Table 7 reports 67.7% for StruQ Llama; the 0.1-point difference is unresolved.

### Table 4 — Near-miss Completion delimiters, p. 11

| Delimiter condition | Llama undefended/StruQ | Mistral undefended/StruQ |
|---|---|---|
| Real delimiter | 96% / 0% | 90% / 0% |
| Two hash marks | 90% / 0% | 90% / 0% |
| One hash mark | 91% / 1% | 90% / 0% |
| Zero hash marks | 90% / 0.5% | 90% / 0% |
| All uppercase | 92% / 0% | 92% / 0% |
| Title case | 89% / 0% | 93% / 0% |
| No blank space | 90% / 0% | 93% / 0% |
| No colon | 90% / 0% | 93% / 0% |
| Typo | 85% / 0% | 91% / 0% |
| Similar token | 61% / 0% | 73% / 0% |

The caption says the real and two-hash variants are filtered; remaining variants are unfiltered. The smallest undefended rates occur with similar tokens, but are still substantial. The table's defended Mistral maximum is 0%, unlike Table 2's 1% Close maximum; the exact source of this condition/reporting difference is not given.

### Table 5 — Training augmentation summary, p. 11

| Augmentation | Utility | Highest ASR among six selected attacks |
|---|---:|---:|
| Undefended | 67.2% | 41% |
| Naive | 66.0% | 16% |
| Ignore | 64.3% | 6% |
| Completion-Other | 66.1% | 3% |
| Fake Delimiter | 60.3% | 70% |
| Naive + Completion-Other | 66.0% | 0% |
| Naive + Fake Delimiter | 63.3% | 25% |
| Ignore + Completion-Other | 65.4% | 0% |
| Ignore + Fake Delimiter | 63.5% | 6% |

Both Completion-containing pairs tie at zero selected-attack ASR. Naive+Completion has higher utility than Ignore+Completion and is selected. Fake Delimiter alone is worse than undefended on the strongest selected attack and has the lowest utility. This experiment excludes reserved delimiters and filtering; its zero values cannot be transferred to the full attack suite.

### Table 6 — Delimiter-component summary, p. 12

Five configurations vary whether marker/hash marks, delimiter words, and colon are textual or reserved tokens. Utility/maximum Completion ASR pairs are: all textual 66.0%/1%; textual marker with special words and textual colon 62.6%/1%; special marker with textual words/colon 60.2%/1%; special marker/words with textual colon 64.0%/1%; all special 67.6%/1%. Filtering is used throughout. All tie on the reported maximum ASR. Full special structure wins on utility within this experiment, while claims about better unseen-attack security remain prospective interpretation.

### Table 7 — BIPIA versus StruQ, p. 13

| Row | Vicuna none/BIPIA | Llama none/StruQ |
|---|---|---|
| Utility | 53.9% / 26.0% | 67.2% / 67.7% |
| Ignore | 67% / 54% | 12% / 0% |
| Completion-Real | 94% / 23% | 96% / 0% |
| Completion-RealCmb | 92% / 30% | 71% / 0% |
| GCG | 100% / 100% | 97% / 58% |
| Ignore, BIPIA set (*) | 39% / 5% | 7% / 0% |
| Completion-Real (*) | 99% / 4% | 25% / 0% |
| Completion-RealCmb (*) | 99.5% / 7% | 36% / 0% |

The asterisk denotes the BIPIA test set, not statistical significance. Models differ between the two defense families. GCG on the starred set was not run because of the stated 80GB GPU limitation. The prose's broad zero-success statement about StruQ must be restricted to the displayed manual rows; the GCG row is 58%. Table 7's StruQ RealCmb result is also not identical to the Mistral condition in Table 2.

### Table 8 — Full augmentation breakdown, p. 20

Column order is undefended, Naive, Ignore, Completion, FakeDelm, Naive-Completion, Naive-FakeDelm, Ignore-Completion, Ignore-FakeDelm. Utility values are 67.2, 66.0, 64.3, 66.1, 60.3, 66.0, 63.3, 65.4, and 63.5 percent. In that order, ASR rows are:

- Naive: 6, 0, 0.5, 0, 4, 0, 0, 0, 2 percent.
- Ignore: 12, 0, 0, 3, 14, 0, 0.5, 0, 0 percent.
- Escape-Deletion: 3, 0.5, 0, 1, 2, 0, 0, 0, 0 percent.
- Escape-Separation: 2, 0, 0.5, 1, 2, 0, 0, 0, 1 percent.
- Completion-Other: 29, 5, 6, 0, 43, 0, 9, 0, 6 percent.
- Completion-OtherCmb: 41, 16, 0, 0, 70, 0, 25, 0, 3 percent.

These entries explain Table 5's maxima and show that improvement depends on the attack family. Ignore-only training eliminates the combined Completion attack but still has 6% on Completion-Other. Completion-only training eliminates Completion conditions but retains 3% Ignore ASR. The two successful paired strategies cover weaknesses of individual augmentations within this subset.

### Table 9 — Full delimiter breakdown, p. 20

Columns match Table 6's five configurations, ordered all textual; special words only; special marker only; special marker and words; all special. Utility is 66.0, 62.6, 60.2, 64.0, 67.6 percent. ASR rows in that order are:

- Default: 1, 0.5, 1, 0, 1 percent.
- Two hash marks: 0.5, 0.5, 0, 0, 0.5 percent.
- One hash mark: 1, 0.5, 1, 0, 1 percent.
- Zero hash marks: 0.5, 0, 0, 0, 0.5 percent.
- Uppercase: 0, 0, 0, 1, 0 percent.
- Title case: 0.5, 1, 0.5, 0, 0.5 percent.
- No blank space: 0, 0, 0, 0, 1 percent.
- No colon, typo, and similar tokens: all five entries are 0% for each row.

No configuration dominates every row: some alternatives outperform all-special delimiters on individual attacks, and the all-special choice retains 1% in several rows. These are distinct ablation conditions from Table 2 and should not be silently merged with its exact-delimiter zero result. Appendix B provides pointers to these detailed tables rather than new separate experiments.

## 12. Diagram / Architecture Interpretation

Figures 1–2 already account for the numbered diagrams. Additional boxed examples are substantive illustrations of the attack surface. Pages 4–5 show a benign email classification query, an Ignore injection, a direct Naive instruction, escape-character insertions, and a fabricated answer followed by a new instruction. The red text identifies attacker-controlled additions; it is evidence to analyze, never an instruction to follow.

Page 6's text-only examples show a combined Completion attack, a HackAPrompt translation-to-echo role switch, and a TAP-generated instruction to prioritize a second task. Page 7's visually inspected example shows a GCG suffix containing irregular text. Page 13's visually inspected BIPIA box uses USER/ASSISTANT and data tags to fabricate a completed answer and new user turn. Page 20's four TAP success boxes demonstrate synonym-task blending, direct override, conditional code, and a recipe-scenario pretext. They are qualitative successful examples, not four additional numerical experiments.

The control path originates in the developer's trusted prompt and front-end template. The data path goes through filtering before insertion into the structured input. Both reach the same model sequence; the design's logical separation relies on protected token boundaries and learned behavior. There is no depicted permission manager, browser executor, tool-call validator, or runtime feedback loop. TAP and GCG supply iterative attack search outside this normal inference pipeline.

## 13. Equations and mathematical concepts

The supplied paper contains dataset-construction expressions and algorithmic notation, not a new formal security theorem or a numbered optimization loss. Its essential mathematical objects are training triples and concatenations. In T = {(p_i, d_i, r_i), ...}, p_i is the trusted instruction, d_i associated data, and r_i the desired response. T' denotes the modified training set; i and j identify samples, and the double-bar operator denotes text concatenation. [A: pp. 8–9]

For Naive augmentation, the conceptual example is (p_j, d_j || p_i || d_i, r_j). The input data is lengthened by another sample's instruction/data; the correct answer remains r_j. For Completion augmentation, the example is (p_j, d_j || d_resp || r' || d_inst || p_i || d_i, r_j). Here d_resp and d_inst are fake response/instruction delimiters, and r' is a fake answer different from r_j. The operation intentionally places a plausible conversation continuation inside data while retaining the original task's output as the training target. [A: pp. 8–9]

Ignore augmentation inserts I, an ignore directive: (p_j, d_j || I || p_i || d_i, r_j). Fake-delimiter augmentation changes delimiters and uses r^⊤, a default rejection answer such as 'Invalid Delimiters'. The latter's objective is to reject structurally invalid input, but the authors observe utility loss and poor security for this strategy. [A: p. 11]

Algorithm 1 shuffles T into T', iterates over samples, skips augmentation with probability 0.5 or when data is empty, and otherwise chooses Naive or Completion with another 0.5 probability. Conditional on nonempty data, the nominal probabilities are derived as 0.5 clean, 0.5 × 0.5 = 0.25 Naive, and 0.5 × 0.5 = 0.25 Completion. These are probabilities, not guaranteed exact sample fractions in a particular randomized execution. Empty-data samples increase the final clean fraction. [A/C: p. 9]

Two notation issues are preserved. The prose describes choosing another random sample, while Algorithm 1 refers to T[j] after T' has been shuffled; the exact pairing and possible self-pairing behavior are not fully explained. The algorithm's output is named T', but its last line returns T_s. That returned symbol is not defined in the supplied algorithm. The continuation on page 9 also alternates i/j notation. These issues do not obscure the broad augmentation idea, but prevent a perfectly literal implementation specification.

Appendix A.3 generates fake delimiters by selecting a marker template m and role/label words, then using d_resp = m.format(s = R_o W_r) and d_inst = m.format(s = R_i W_i). R_i labels input roles, R_o output roles, W_i instructions, and W_r responses. Appendix A.4 adds a data-word variable W_d and d_inpt = m.format(s = R_i W_d). Adjacent symbols mean forming the label string in this context, not numerical multiplication. Quotation glyphs in the marker list are extraction-sensitive; their exact byte-level spelling is uncertain. No loss equation, gradient formula, convergence argument, or formal proof of filtering security is supplied.

## 14. Interpretation and discussion

The supported conclusion is that input structure and training jointly improve resistance while preserving measured utility. Reserved delimiters protect syntactic boundaries; filtering prevents exact boundary spellings from originating in data; augmentation teaches the model to ignore competing instructions inside that boundary. This combination addresses different failure modes and explains why ordinary quotation-like delimiters alone are insufficient in the tested settings. [A/D: pp. 7–12]

The optimized-attack results show that protecting explicit separators does not solve every semantic authority error. An attacker can frame the desired output as part of the legitimate task, or optimize a suffix without readable meaning. The authors attribute generalization failures to training on task-agnostic manual attacks rather than highly optimized task-specific attacks. That is their interpretation, supported by examples and the 68% semantic-relatedness observation, rather than a definitive causal experiment. [A: p. 10]

For the requested web-agent research question, the paper supplies a mechanism rather than a direct ranking. A developer-controlled application can ingest text from another party; that text can attempt to override the application's task. The three-party trust model explains why instruction following becomes an application security issue. Applying this to a web agent that consumes external pages is an analyst inference. The supplied study does not show that web exposure alone increases attack success relative to an identically configured standalone model, nor does it test a browsing agent with executable actions.

Several consistency checks materially limit stronger conclusions: the strict below-2% prose versus the 2% table cell; the 'stops all' Completion wording versus nonzero Table 4 cells; Mistral's 96% versus 90% real-delimiter baselines; its 1% Table 2 Close maximum versus all-zero defended Table 4 entries; Llama utility 67.6% versus 67.7%; the Figure 2 [HASH]/text [MARK] naming difference; and Algorithm 1's undefined T_s return. None is silently reconciled here. Table 5/8 and Table 6/9 aggregate/detail relationships otherwise match their displayed maxima and utility values.

## 15. Contributions and novelty

Conceptual contribution: structured queries treat instruction and data as separately supplied inputs and explicitly connect prompt injection to control/data confusion. Methodological contribution: structured instruction tuning augments ordinary instruction datasets while keeping the trusted task's desired response. Systems contribution: a front-end combines reserved-token encoding with recursive data filtering. Implementation contribution: the paper reports adapting existing base models and releasing code, although that code was not reviewed. [A: pp. 1–3, 7–9]

Experimental contribution: the authors evaluate manual, adaptive-delimiter, and optimized attacks, measure utility, test component choices, and compare defenses. Their adaptation of TAP and GCG reveals substantial residual vulnerability that simpler attacks would miss. These are author-claimed contributions within the supplied evidence; no independent priority verification is performed. [A: pp. 9–14]

There is no claimed new foundation-model pretraining, formal security proof, or new dataset contribution. The ethics/open-science statement explicitly says the paper does not contribute new datasets or binaries. Training-data augmentation is a procedure applied to existing data, rather than evidence of a separately released benchmark dataset.

## 16. Limitations

### Authors' stated limitations

StruQ protects programmatic applications calling models through an API or library. It is not applicable as presented to web-based multi-turn open-ended chatbots, because end users are unlikely to label each conversational contribution as instruction versus data. It is designed for prompt injection rather than jailbreaks, training-data extraction, or other LLM attacks. [A: pp. 13–14]

It is not completely secure in the worst case: GCG and TAP remain successful. Optimized attacks are much more expensive than the manual attacks studied. GCG requires gradient access, which may not be realistic for every attacker. The authors cannot interpret GCG suffix meanings. They could not run GCG on the long BIPIA test samples with one 80GB GPU. [A: pp. 6, 10, 13–14]

### Additional evidence-based analyst observations

[D] The security metric emphasizes one target output string, so it may not represent the full variety of application deviations. [D] Only two 7B base-model families are evaluated; results do not establish behavior for all model sizes or deployment interfaces. [D] Utility measurement is a single judged instruction-following benchmark and does not isolate legitimate data loss caused by filtering. [D] Train-set size, random seeds, detailed optimizer configuration, repetitions, and ASR uncertainty intervals are not supplied.

[D] BIPIA and StruQ use different starting models, limiting direct defense-only attribution. [D] The training prose and pseudocode contain unresolved indexing details. [D] Reported zeros cannot guarantee robustness outside finite evaluated conditions. [D] The benchmark uses text-processing model calls rather than an end-to-end web-agent workflow; browsing, tool permissions, multi-step persistence, and action consequences remain unmeasured here.

## 17. Threats to validity

The following labels are analyst-organized observations, not terminology attributed to the authors. Internal validity: augmentation ablations help isolate training choices, but the BIPIA comparison changes model family as well as defense. The suspected explanations for BIPIA's performance are not each separately controlled. Construct validity: output-string ASR measures an important hijacking behavior, but not all confidentiality breaches, silent answer corruption, or unauthorized tool use. Utility win rate measures judged answer preference rather than every application's correctness. [D]

External and ecological validity: 208 data-bearing AlpacaFarm examples, 20 selected competition attacks, and 231 BIPIA examples cover useful conditions but do not establish performance on every long web document, multi-turn agent, or language. The authors consider shorter data favorable to attackers; that contextual claim does not replace evaluation across document lengths. White-box GCG tests a strong threat model that differs from some deployed attackers, while its high ASR usefully exposes worst-case weaknesses. [A/D]

Statistical conclusion validity: the source reports a utility standard error and significance threshold, but not detailed test methodology, ASR intervals, seeds, or repeated-run variation. Rounded percentages should not be converted to exact success counts. Reproducibility: code availability is reported, and key learning rates, epochs, augmentation procedures, and attack budgets are supplied, but full computational reproduction cannot be assessed without inspecting code and missing implementation details. Generalizability: protection depends on accurate trusted/data assignment and the complete front-end/model pairing. [D]

## 18. Future work and open questions

### A. Authors' proposed future work

The authors propose improving resistance to optimized task-specific attacks, potentially training on task-dependent injections generated by an LLM or human crowdsourcing. They discuss access control and rate limiting to detect iterative attackers, architectures inherently robust to injection, and possibly masking attention between prompt and data in initial layers. These are proposed directions, not implemented or evaluated defenses in this paper. [A: pp. 10, 14]

They suggest richer structured queries containing system prompt, user prompt, and data; models that distinguish instructions from data without delimiters; and making non-instruction-tuned models available for fine-tuning. The discussion explicitly presents structured queries as a first step. [A: p. 14]

### B. Analyst-identified remaining questions

Would the method preserve useful content in documents that legitimately contain filtered strings? How would it handle browser/tool outputs and multiple trust levels in a multi-step agent? Would expanded attack-aware training close the TAP/GCG gap without reducing utility? How do results vary by model size, length, language, attack budget, or random seed? Can structural enforcement be specified precisely enough to independently verify tokenizer and API assumptions? What happens when the application itself incorrectly labels malicious instructions as trusted? These questions logically remain, but the supplied paper does not answer them. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model: a model that processes/generates language |
| Base model | Model before the instruction-tuning stage considered here |
| Instruction tuning | Training a model on task requests and desired responses |
| Structured instruction tuning | Training it to obey the prompt-region instruction while ignoring data-region instructions |
| Prompt | The task instruction supplied by the application |
| Data | Text the task should operate on, potentially attacker-controlled |
| Prompt injection | Data-contained instructions that redirect the intended task |
| Jailbreak | Attempt to defeat the provider's safety goals; distinct from developer-task hijacking |
| Structured query | Separate prompt/data inputs encoded with protected boundaries |
| Delimiter | Marker identifying a region boundary |
| Reserved token | Special token used for structural control rather than ordinary data text |
| Embedding | Learned numerical representation of a token |
| Front-end | Component that filters data and formats model input |
| Completion attack | Fake answer plus new instruction intended to simulate a new query |
| Cmb | Combined attack, including Completion, Ignore, and Escape-Separation mechanisms |
| TAP | Tree-of-Attacks with Pruning: iterative LLM-generated attack search |
| GCG | Greedy Coordinate Gradient: gradient-guided suffix optimization |
| White-box | Attacker access to internal model gradients in this study |
| ASR | Attack success rate; lower is better |
| AlpacaEval | Automated instruction-output preference evaluation used for utility |
| BIPIA | Benchmark for indirect prompt injection attacks and related defense compared here |
| Jatmo | Task-specific fine-tuning defense described by the authors |
| API | Application programming interface through which software calls a model |
| SQL / XSS | Structured Query Language / cross-site scripting, used as injection analogies |
| T, T' | Original and augmented training datasets |
| p_i, d_i, r_i | Instruction, data, and desired response of sample i |
| r' | Fake response used in Completion augmentation |
| r^⊤ | Default rejection response in fake-delimiter augmentation |
| I | Ignore directive added in Ignore augmentation |
| || | Concatenation of text pieces |
| d_resp, d_inst, d_inpt | Fake response, instruction, and input delimiters |
| [MARK], [INST], [INPT], [RESP], [COLN] | Reserved structural-token spellings in the textual method |
| [HASH] | Marker spelling shown in Figure 2; relationship to [MARK] not explicitly resolved |

## 20. Key numerical results

All exact table values below are author-reported and visually readable. Derived differences are separately labeled. No approximate graphical estimates are required because the paper's figures are schematics.

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| Main security sample set | 208 | examples | AlpacaFarm samples with data inputs | Author-reported | p. 9, §5 |
| Utility sample set | 805 | examples | AlpacaFarm/AlpacaEval 1.0 | Author-reported | p. 9 |
| BIPIA test set | 231 | examples | Email, table, WebQA | Author-reported | p. 13 |
| HackAPrompt selection | 20 | injections | Successful level-1 entries | Author-reported | pp. 6, 19 |
| Training duration | 3 | epochs | Whole-model fine-tuning | Author-reported | p. 9 |
| Llama learning rate | 2 × 10^-5 | learning-rate scalar | Llama-7B | Author-reported | p. 9 |
| Mistral learning rate | 2.5 × 10^-6 | learning-rate scalar | Mistral-7B | Author-reported | p. 9 |
| Nominal clean/Naive/Completion allocation | 50/25/25 | percent | Empty-data samples remain clean | Author-reported | pp. 8–9 |
| Llama Completion-Real ASR | 96 → 0 | percent | Undefended → full StruQ | Visually readable | p. 10, T2 |
| Mistral Completion-RealCmb ASR | 83 → 2 | percent | Undefended → full StruQ | Visually readable | p. 10, T2 |
| Llama TAP ASR | 97 → 9 | percent | Undefended → StruQ | Visually readable | p. 10, T2 |
| Mistral TAP ASR | 100 → 36 | percent | Undefended → StruQ | Visually readable | p. 10, T2 |
| Llama GCG ASR | 97 → 58 | percent | Undefended → StruQ | Visually readable | p. 10, T2 |
| Mistral GCG ASR | 99 → 56 | percent | Undefended → StruQ | Visually readable | p. 10, T2 |
| Llama TAP absolute reduction | 97 - 9 = 88 | percentage points | Main security comparison | Analyst-derived | p. 10, T2 |
| Llama GCG absolute reduction | 97 - 58 = 39 | percentage points | Main security comparison | Analyst-derived | p. 10, T2 |
| Mistral TAP absolute reduction | 100 - 36 = 64 | percentage points | Main security comparison | Analyst-derived | p. 10, T2 |
| Mistral GCG absolute reduction | 99 - 56 = 43 | percentage points | Main security comparison | Analyst-derived | p. 10, T2 |
| Llama utility | 67.2 → 67.6 | percent win rate | Table 3; Table 7 instead has 67.7 defended | Visually readable | pp. 10, 13 |
| Mistral utility | 80.0 → 78.7 | percent win rate | AlpacaEval | Visually readable | p. 10, T3 |
| Mistral utility change | 78.7 - 80.0 = -1.3 | percentage points | Defended minus undefended | Analyst-derived | p. 10, T3 |
| Utility standard error | 0.7 | percent as reported | AlpacaEval discussion | Author-reported | p. 9 |
| Significance level | 0.05 | threshold | Utility interpretation | Author-reported | p. 9 |
| GCG iterations | 500 | iterations | Per-sample suffix optimization | Author-reported | p. 7 |
| TAP branching/depth/width | 4/10/10 | search parameters | Adapted TAP | Author-reported | p. 20, A.6 |
| TAP semantic connection | 68 | percent | Generated injections against defended models | Author-reported | p. 10 |
| Optimized attack cost | >100× | GPU-hour ratio | Relative to other tested attacks | Author-reported | p. 14 |
| TAP model queries | about 100 | queries | Attack improvement | Author-reported | p. 14 |
| GCG model queries | 256k | queries | One attacked sample | Author-reported | p. 14 |
| BIPIA utility | 53.9 → 26.0 | percent win rate | Vicuna none → BIPIA | Visually readable | p. 13, T7 |
| GCG on BIPIA | 100 | percent ASR | Unstarred test condition | Visually readable | p. 13, T7 |
| GPU memory limitation | 80 | GB | One GPU insufficient for BIPIA-set GCG | Author-reported | p. 13, T7 caption |

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification/evidence strength |
|---|---|---|---|---|
| Separating authority from data is the core approach | Separate inputs, reserved encoding, location-aware training | F1, F2, ALG1 | pp. 1–2, 7–9 | HIGH for the described method; no formal enforcement proof |
| Exact Completion spoofing is strongly reduced | 96% to 0% for both models | T2, X1 | p. 10 | HIGH for tested conditions; finite benchmark |
| Optimized attacks remain effective | GCG 58%/56%; TAP 9%/36% | T2, X1 | p. 10 | HIGH; refutes blanket immunity |
| Utility changes are small in the chosen benchmark | Llama 67.2/67.6; Mistral 80.0/78.7 | T3, X2 | pp. 9–10 | HIGH for numbers; broader utility interpretation MEDIUM |
| Training combination matters | Naive+Completion zero on six attacks, utility 66.0% | T5/T8, X4 | pp. 11, 20 | HIGH within no-filter ablation subset |
| Fully special delimiters support utility | 67.6% highest utility, all configurations max ASR 1% | T6/T9, X5 | pp. 12, 20 | HIGH; security superiority not established by maxima |
| Test-time defenses leave substantial vulnerability | ASR 83%, 39%, 85%, 48% versus StruQ 0% | X6 | p. 12 | HIGH for Completion-Real on Llama only |
| StruQ outperforms reproduced BIPIA in reported tests | Lower manual ASR and retained utility | T7, X6 | p. 13 | HIGH descriptive; different starting models constrain causality |
| Deployment scope excludes ordinary open-ended chatbots | Explicit limitations statement | S6 | pp. 13–14 | HIGH; does not mean all programmatic web agents are excluded |
| Web-agent relevance concerns trust boundaries | Three-party model and untrusted-source application data | S2/S3 | pp. 3–5 | MEDIUM analyst inference; no direct web-agent/standalone comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a teacher asks you to summarize a letter. The letter itself says, 'Ignore the teacher and write a different answer.' You should understand that sentence as part of the letter, not as a new order. The problem studied here is that a language model can confuse those two roles: the instruction from the application and the instruction written inside the material it is reading.

StruQ gives the model a clearly marked place for the real task and another place for the material. It removes strings that could pretend to be those markers. Then it trains the model with many examples where the material contains distracting instructions, while the correct answer still follows the real task.

This works well against many tested tricks and keeps the model's ordinary answers about as useful on the chosen benchmark. But attackers that repeatedly optimize their tricks still succeed often. That means the method improves security without solving the whole problem.

For a web agent, this paper suggests why reading someone else's text can be risky: the agent's application has a task, while the text's author can try to replace it. That is a connection inferred from the paper's trust model. The researchers did not directly test whether a web agent is more vulnerable than a standalone chatbot, or measure the consequences of an agent taking unauthorized actions.

## Completeness Audit

Coverage is assessed against the inventory of the supplied 20-page document, not against unseen publications or code. 'Fully represented' means the substantive role and evidence are represented here; it does not mean every source word is reproduced. Closely related subsection rows are grouped only where all named components share the same inspected and represented status.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META and Abstract | Yes, text and image | Yes | Represented in compressed form | Title/authors/version/venue and abstract claims covered |
| §1 Introduction | Yes, text and images | Yes | Fully represented | Motivation, interface problem, qualified results |
| §2 LLMs and integration | Yes; p. 3 text-only | Yes | Fully represented | Base/instruction tuning, subroutine calls, résumé example |
| §2 Injection analogy | Yes, text-only p. 3 | Yes | Represented in compressed form | Telephone/SQL/XSS/shell examples summarized |
| §2 Defenses and threat distinctions | Yes | Yes | Fully represented | BIPIA/Jatmo/reminders, hierarchy, jailbreak distinction |
| §3.1 problem and threat model | Yes, text/images | Yes | Fully represented | Capabilities and success criterion |
| §§3.2–3.4 Naive/Ignore/Escape | Yes, text/images | Yes | Fully represented | Parameters and examples compressed |
| §3.5 Completion variants | Yes; p. 6 text-only | Yes | Fully represented | Real/Close/Other/combined distinctions |
| §3.6 HackAPrompt | Yes, text-only p. 6 | Yes | Fully represented | Level-1 selection, 20 attacks, retained prompts |
| §3.7 TAP | Yes, text-only p. 6 plus A.6 image | Yes | Fully represented | Adaptation, settings, successful examples |
| §3.8 GCG | Yes, text and p. 7 image | Yes | Fully represented | White-box assumption, 500 iterations, unreadable semantics |
| §§4.1–4.2 requirements/overview | Yes | Yes | Fully represented | Security goal distinguished from achieved result |
| §4.3 encoding/filter/embeddings | Yes, text/images | Yes | Fully represented | All removed strings, initialization, marker inconsistency |
| §4.4 training | Yes, text/images | Yes | Fully represented | Clean/Naive/Completion construction, empty-data caveat |
| §5 metrics/data/models | Yes, text/image | Yes | Fully represented | Counts, rates, epochs, missing implementation details |
| §5.1 main results | Yes, text/images | Yes | Fully represented | Full T2/T3 values and caveats |
| §5.2 adaptive attacks | Yes, text/images | Yes | Fully represented | Nine variants, additional token variants, discrepancies |
| §5.3 tuning ablation | Yes, text/images | Yes | Fully represented | Conditions and T5/T8 values |
| §5.4 front-end ablation | Yes, text/images | Yes | Fully represented | Conditions and T6/T9 values |
| §5.5 test-time comparison | Yes, text/image | Yes | Fully represented | All four baseline ASRs |
| §5.5 BIPIA comparison | Yes, text/images | Yes | Fully represented | T7, model differences, missing starred GCG |
| §6 limitations | Yes; continuation p. 14 text-only | Yes | Fully represented | Application scope and residual attacks |
| §6 future defenses/system prompts/tuning/provider lessons | Yes, text-only p. 14 | Yes | Fully represented | Proposals labeled untested |
| §7 Summary | Yes, text-only | Yes | Represented in compressed form | Repetitive synthesis integrated |
| Ethics/open-science statement | Yes, text-only | Yes | Represented in compressed form | No new datasets/binaries; ethical positioning |
| Acknowledgments/contact information | Yes | Partly | Inspected but deliberately compressed as secondary | Funding names/emails not enumerated |
| References [1]–[65] | Yes, text-only | Yes, bibliographic role | Represented in compressed form | No cited work independently inspected |
| Objectives O1–O6 | Yes, source objectives | Yes | Fully represented | Analyst organization clearly labeled |
| Formal hypotheses/RQs | Checked | Yes, absence disclosed | Not present as formal items | No invented hypotheses |
| X1–X6 experiments | Yes | Yes | Fully represented | Distinct conditions maintained |
| Figure 1 | Yes, visually | Yes | Fully represented | Four schematic cases, no quantitative axes |
| Figure 2 | Yes, visually | Yes | Fully represented | Architecture and [HASH]/[MARK] issue |
| Tables 1–9 | Yes, visually and textually | Yes | Fully represented | Numerical rows preserved; T1 qualitative |
| Algorithm 1 | Yes, visually and textually | Yes | Fully represented with uncertainty | Pairing/index and undefined return symbol flagged |
| Filtering pseudocode | Yes, visually and textually | Yes | Fully represented | Fixed-point deletion described |
| Dataset/augmentation expressions | Yes | Yes | Fully represented with uncertainty | i/j inconsistency retained |
| Delimiter-generation expressions | Yes, p. 18 image/text | Yes | Represented in compressed form | Exact quote glyphs uncertain |
| Formal theorems/loss equations | Checked | Yes, absence disclosed | Not present | No proof reconstructed |
| Major contributions | Yes | Yes | Fully represented | Author novelty claims not externally validated |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst observations |
| Appendix A.1/A.2 | Yes, visually/textually | Yes | Represented in compressed form | Ten test/ten train Ignore variants; rhetoric grouped |
| Appendix A.3/A.4 | Yes, visually/textually | Yes | Represented in compressed form | Separate delimiter vocabularies/formulas |
| Appendix A.5 | Yes, text-only p. 19 | Yes | Represented in compressed form | Twenty repetitive attacks grouped by mechanism |
| Appendix A.6 | Yes, visually/textually | Yes | Fully represented | Settings and four examples summarized |
| Appendix B.1/B.2 | Yes, visually/textually | Yes | Fully represented | Detailed T8/T9 results included |
| Supplied supplementary material | None supplied | Absence represented | Not available | No claim of review |
| Released code | Announcement inspected only | Availability claim represented | Artifact not supplied | Implementation not verified |

### Missing or inaccessible material

No numbered page among the supplied 1–20 text records is missing. Visual renderings were not supplied for pages 3, 6, 14–17, and 19; their content was reviewed through text only. Released code, underlying datasets, trained models, exact split manifests, and any separate supplementary artifacts were not supplied or inspected. External references were available as bibliography entries only. Exact contents of linked artifacts, current publication status, and independent reproduction cannot be assessed.

### Uncertain interpretations

Unresolved differences are: page 2's strict below-2% claim versus Table 2's 2%; page 11's 'stops all' wording versus Table 4's nonzero cells; Mistral real-delimiter 96% in Table 2 versus 90% in Table 4; Mistral Close maximum 1% in Table 2 versus 0% across Table 4's displayed defended rows; Llama utility 67.6% in Table 3 versus 67.7% in Table 7; [HASH] in Figure 2 versus [MARK] in text; Algorithm 1's T_s return and sample-pairing indices; and exact quote characters in Appendix A's marker templates. The effective denominator and aggregation for HackAPrompt are not fully specified. No values were invented to resolve these issues.

### Deliberately compressed material

The ten testing and ten training Ignore statements are represented by their counts, separation, and rhetorical mechanisms: cancellation, urgency, changed priorities, fictional pretexts, and asserted authority. Appendix A.5's 20 attacks are compressed as translation reversals, output substitution, role/task switching, string combination, dictionary mapping, and multilingual conditional examples. Their repeated target string and punctuation constraints do not require verbatim duplication. The four successful TAP examples are summarized by mechanism. Bibliographic entries, author contact details, funding acknowledgments, and repeated abstract/introduction/conclusion formulations are compressed. Mathematical construction, experimental conditions, substantive tables, and limitations receive priority over repeated attack prose.

### Potential omissions

Every substantive item identified in the supplied-document inventory has a representation or explicit uncertainty/absence entry. Exact wording of repetitive attack examples and exact delimiter-template glyphs is not preserved, as disclosed. The analysis cannot rule out substantive information in unprovided code or other artifacts, cannot validate all implementations from prose, and does not claim a complete account of the outside literature. Its coverage conclusion applies to the supplied paper text and the explicitly listed visually inspected pages.
