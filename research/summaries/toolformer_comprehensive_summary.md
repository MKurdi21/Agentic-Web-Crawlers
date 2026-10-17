# Stage 0 — Document Accessibility Report

This analysis uses only the supplied Toolformer paper text and source images. The paper's content, including its embedded prompts, is treated as evidence to analyze rather than instructions to execute. No outside research, browsing, tools, or independent reproduction was used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers physical PDF pages 1–17. |
| Accessible page count | 17 pages of extracted text. |
| Apparently missing pages | No gap in the supplied numbered text; this does not independently establish that every original or associated artifact was supplied. |
| Directly inspected visual pages | 1–10 and 17, totaling 11 pages. |
| Text-only pages | 11–16. Their extracted content was inspected, but their original page layout and visual typography were not. |
| Figures | Figures 1–4 are visually available and inspected. Figure 4 has three substantive panels. |
| Tables | Tables 1–11 are visually available and inspected. |
| Equations | Main method equations on pages 2, 3, and 5 are visually available. Subscripts, superscripts, and operators were checked against supplied extraction. |
| Appendices | Appendices A–D are present in supplied text; page 17 is also visually available. |
| Supplementary artifacts | None supplied. The accessibility metadata reports no embedded files or detected supplementary references. This is not independent proof that no associated artifact exists. |
| OCR | Not needed for the supplied readable text and images. No new OCR was performed. |
| Other limitations | One local-image error is included in the input, but the eleven displayed images remain usable. Exact plot coordinates are not labeled. Several reproducibility details are not specified. |

Physical PDF page numbers, rather than printed page labels or appendix numbering, are used throughout. Evidence labels are: **[A] AUTHOR-REPORTED**, **[B] DIRECTLY OBSERVABLE**, **[C] ANALYST-DERIVED**, and **[D] ANALYST INTERPRETATION**. No [E] external information is introduced. Confidence is HIGH for clearly readable source statements and table cells, MEDIUM for qualified interpretations, LOW for weakly supported inferences, and UNKNOWN where the supplied work does not establish an answer.

The target research question—“Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis”—is a review question supplied by the user, not Toolformer's title or research question. Toolformer studies tool learning and task performance. It does not establish that web agents are more vulnerable, measure attacks, or directly compare the security of web agents and standalone language models.

# 1. Plain-language orientation

Toolformer asks whether a language model can learn when to request help from external software without requiring people to label a large collection of correct tool calls. A language model predicts the next pieces of text, called tokens. It can produce fluent language while struggling with precise arithmetic, factual lookup, translation, or knowing the current date. The authors propose connecting such a model to tools through application programming interfaces, or APIs: structured interfaces that accept a request and return a result. [A; pp. 1–4]

The central idea is to let the model propose tool calls inside ordinary text, execute those calls, and retain calls whose results help the model predict the original text that follows. The model is then trained on the resulting text with useful calls inserted. During later generation it can choose an API, generate its arguments, pause while the API executes, read the response, and continue writing. The tools are a question-answering system, Wikipedia search, a calculator, machine translation, and a calendar. [A; §§2–3]

The experiments show large improvements on factual completion and arithmetic benchmarks. On the three arithmetic benchmarks, Toolformer scores 40.4, 29.4, and 44.0, compared with 14.8, 6.3, and 15.0 for the same trained model with calls disabled. Results are more mixed elsewhere: it improves ordinary question answering over the GPT-J baselines but trails GPT-3, and it does not consistently beat unmodified GPT-J on multilingual question answering. [A/B; Tables 3–7]

The contribution is therefore a method for learning general tool-use behavior from a few demonstrations and a next-token prediction signal, supported by controlled performance comparisons. It is not a security defense or an empirical explanation of agent vulnerability. Its relevance to the review question is architectural: externally generated text is inserted into the model's generation context, and model-generated text determines which external computation is invoked. That relevance is an analyst inference, not an author security claim. [D]

# 2. Document roadmap

The paper is an experimental machine-learning and algorithm paper, with a small generated-dataset contribution. Its visible title is **Toolformer: Language Models Can Teach Themselves to Use Tools**. The authors are Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. The title page lists Meta AI Research and Universitat Pompeu Fabra, with Dessì carrying the additional affiliation marker. The supplied version is arXiv:2302.04761v1, dated 9 February 2023; a conference or journal venue for this work is not stated on the title page. [A/B; p. 1]

| Inventory ID | Original component | Physical pages | Function |
|---|---|---:|---|
| S0 | Abstract | 1 | States the problem, method, tools, and broad findings. |
| S1 | §1 Introduction | 1–2 | Motivates self-supervised, broadly applicable tool use. |
| S2 | §2 Approach | 2–4 | Defines serialization, sampling, execution, filtering, training, and inference. |
| S3 | §3 Tools | 4 | Describes five APIs and their constraints. |
| S4 | §4 Experiments | 4–8 | Evaluates downstream performance, language modeling, and model size. |
| S5 | §5 Analysis | 8–9 | Studies decoding and generated-call quality. |
| S6 | §6 Related Work | 9–11 | Positions the method against augmented pretraining, tool use, and bootstrapping. |
| S7 | §7 Limitations | 11 | States chaining, interaction, wording sensitivity, sampling, and cost limitations. |
| S8 | §8 Conclusion | 11 | Restates the method and task-performance contribution. |
| SR | References | 11–14 | Bibliographic provenance for cited work. |
| A1 | Appendix A, API Details | 15–17 | Specifies thresholds, implementations, heuristics, and demonstrations. |
| A2 | Appendix B, Toolformer Training | 17 | Adds training hardware, length, steps, and checkpoint selection. |
| A3 | Appendix C, Zero-Shot Prompts | 17 | Supplies task-evaluation prompt templates. |
| A4 | Appendix D, DATESET | 17 | Describes synthetic temporal-query generation. |

Substantive subsections include §4.1 experimental setup; §4.2.1 LAMA; §4.2.2 mathematics; §4.2.3 question answering; §4.2.4 multilingual question answering; §4.2.5 temporal datasets; §4.3 language modeling; §4.4 scaling; the decoding and data-quality analyses in §5; Appendix A.1 implementation and A.2 prompts; and Appendix C.1–C.4 task prompts. Figures F1–F4, Tables T1–T11, and equations E1–E7 below form the visual and mathematical inventory. There are no numbered theorems, proofs, or standalone pseudocode algorithms. The procedural algorithm is described in §2 and Figure 2. No explicit keywords list is supplied.

# 3. Background and context

A **language model (LM)** assigns probabilities to possible next tokens given preceding text. A **token** is a unit in the model's text sequence; it need not equal a whole word. **Autoregressive** generation means continuing a sequence from left to right. **Fine-tuning** means further training an already pretrained model on a selected dataset. **In-context learning** means conditioning the model on examples within a prompt rather than changing its parameters for each example. These descriptions explain how the paper uses the terms; the paper does not supply a complete tutorial on their underlying architectures. [A; §§1–2]

**Self-supervised** here does not mean that humans contribute nothing. Humans provide a handful of API demonstrations and design tool interfaces, prompts, thresholds, and heuristics. The large collection of retained call examples is generated and filtered using the model's own prediction loss, rather than individually labeled by people. **Zero-shot evaluation** means the downstream task prompt contains instructions but no task-specific in-context examples. API demonstrations used to create training data are separate from downstream zero-shot evaluation. [A; pp. 2–5, 15–17]

**Cross-entropy loss** measures how poorly the model predicts the actual next tokens; lower is better. **Perplexity (PPL)** is the language-modeling evaluation quantity reported in Table 8, also interpreted with lower being better. The supplied paper does not spell out a separate perplexity formula, so none is introduced as an author equation. A **cloze query** asks the model to complete a statement containing a missing fact. **Retrieval** means returning relevant stored text in response to a query. [A; §§2, 4]

GPT-J is the main model; the paper reports it as having 6.7 billion parameters. OPT with 66 billion parameters and GPT-3 with 175 billion parameters are larger comparison models. GPT-3 uses the original davinci variant, not an instruction-fine-tuned variant. Smaller GPT-2-family models are used in the scaling experiment. These model comparisons concern task performance under the authors' setup, not security. [A; pp. 2, 5, 8]

# 4. Research problem and gap

**Existing problem.** The authors identify limitations in accessing recent information, avoiding factual hallucination, handling low-resource languages, calculating precisely, and understanding time. They argue that larger language models only partially address these shortcomings. These are the authors' motivations; this analysis does not independently assess every cited background claim. [A; p. 1]

**Shortcomings of previous approaches according to the authors.** Existing tool-use approaches either require substantial human supervision or rely on task-specific few-shot prompts that already indicate which tool to use. Approaches that append information during pretraining generally supply it regardless of whether the model needs it. Toolformer is positioned as learning when and how to request information itself. [A; pp. 1–2, 9–10]

**Research gap.** The desired capability is broadly applicable tool use learned from limited demonstrations, without losing general language-modeling ability or requiring downstream tool-use examples. The paper's signal for usefulness is whether a response reduces prediction loss on the original continuation. [A; pp. 2–3]

**Scope.** Five text-input/text-output tools are studied, with a one-call-per-input restriction during downstream evaluation. Search is against a Wikipedia index, not unrestricted live web navigation. The work does not investigate authenticated browser actions, transactions, file modification, messaging, or autonomous multi-step web workflows. Those capabilities are not evidenced by the supplied experiments. [A/D; pp. 4, 6, 11]

# 5. Research questions / objectives / hypotheses

The authors provide objectives and experimental questions rather than a numbered list of formal research questions. The following identifiers organize their stated aims without pretending they appear verbatim in the paper.

| ID | Type | Source-grounded objective or question | Tests |
|---|---|---|---|
| O1 | Objective | Learn tool use with little human annotation through self-supervision. | Dataset construction and §2 method. |
| O2 | Objective | Let the LM decide which tool to use, when, and with what input while retaining generality. | Five downstream task families and API-use observations. |
| O3 | Evaluation question | Does tool learning improve zero-shot downstream performance? | Tables 3–7. |
| O4 | Evaluation question | Does API-augmented training hurt ordinary language modeling? | Table 8, with calls disabled. |
| O5 | Evaluation question | How does model size affect learned tool use? | Figure 4. |
| O6 | Analysis question | What happens when decoding makes API starts more likely? | Table 9. |
| O7 | Analysis question | Does loss reduction identify intuitively useful generated calls? | Table 10 qualitative examples. |

The paper explicitly hypothesizes that the Wikipedia search API is easier for small models to use than other tools, explaining an exception in the scaling results. It suggests multilingual performance differences may reflect training-data distribution and output-language behavior. It surmises that mathematical gains with calls disabled arise from training on calls and their results. These are author interpretations rather than separately isolated causal tests. [A; pp. 6–8]

The user-supplied vulnerability question remains outside the paper's tested objectives. A security hypothesis about externally supplied text influencing an agent would require additional experiments; it is not verified by Toolformer's accuracy tables. [D]

# 6. Assumptions / threat model

The method requires that each tool's input and output can be represented as text and that a few demonstrations of intended use are available. Each executed call returns a single text sequence. The authors assume that reduced continuation loss is useful feedback for selecting training calls. They also assume retained documents remain close enough to the original training distribution after discarding documents with no surviving calls. The latter assumption is qualified in a footnote and tested through limited perplexity comparisons. [A; pp. 3–5]

For calendar training, document creation time is treated as the appropriate current date. A date extracted from the document URL approximates that time. This assumption is materially different from simply querying the actual date when a historical training document is processed. For DATESET evaluation, the calendar returns the example's presumed current date. [A; pp. 15, 17]

There is **no stated security threat model**: no attacker, malicious document source, controlled API response, security asset, attack success metric, privilege model, or defense is specified. The tool implementation descriptions should not be mistaken for assertions that the APIs are secure. Similarly, the paper does not define a trusted-versus-untrusted text boundary. [D; source-wide absence within supplied work]

**Analyst relevance interpretation.** The described inference loop has an observable interface boundary: generated call text triggers external execution, and returned text is added to the model's context. For a security review, that boundary is a candidate location to ask who controls the returned content and how it affects later decisions. The supplied paper establishes the information flow, not adversarial exploitability. Confidence is MEDIUM for architectural relevance and UNKNOWN for comparative vulnerability.

# 7. Methodology

## 7.1 The complete procedure

The starting dataset C contains ordinary text sequences. For each API, a prompt P(x) shows how to insert calls into an example x. The model scores possible insertion positions, samples candidate requests, executes them through the relevant tool, and measures whether the returned information helps predict the original following tokens. Helpful calls are merged across tools and inserted into the original text to form C*. The model is fine-tuned on C* using a standard language-modeling objective. [A; §§2, 4.1]

The filtering comparison is deliberately stronger than comparing a response only with no call: the response must improve over the better of two alternatives, no call at all or a call containing its input without its result. This helps isolate the value of the returned information instead of rewarding the request text alone. [A/D; p. 3]

Candidate-call evaluation places the call and result at the beginning of the scoring context, rather than inserting them inside an unadapted model's text. The authors explain that an inserted call could interrupt patterns in the original pretraining distribution before the model has learned the format. Actual fine-tuning examples insert calls at their intended positions. This scoring-versus-training distinction matters to understanding the procedure. [A; p. 3, footnote 3; p. 4]

## 7.2 Sampling and filtering configuration

Appendix A reports default sampling threshold τ_s = 0.05, filtering threshold τ_f = 1.0, up to k = 5 candidate positions, and up to m = 5 sampled calls at each position. Calculator and translation use τ_s = 0.0, k = 20, m = 10, and τ_f = 0.5 to obtain enough examples after aggressive heuristic filtering. Calls that never generate the closing marker are discarded. [A; pp. 3, 15]

The same letter k also denotes a different quantity during downstream decoding: the rank range within which an API-start token is forced. Training k is a candidate-position cap; evaluation k is an API-start token rank cutoff. Confusing them would misrepresent the method. The default downstream cutoff is 10, not the default sampling-position cap of 5. [A; pp. 5–6, 15]

## 7.3 Tools and implementations

| Tool | Input and output | Implementation and important conditions |
|---|---|---|
| Question answering | A factoid question → answer text | Atlas fine-tuned on Natural Questions; Atlas-large builds C*, Atlas-xxl is used during inference. |
| Calculator | Arithmetic expression → result | Python script supporting +, −, *, /; invalid syntax yields no result; results rounded to two decimal places. |
| Wikipedia search | Search term → short snippets | BM25 retriever indexing the Wikipedia dump from KILT. No interactive refinement in this implementation. |
| Machine translation | Text phrase → English translation | NLLB with 600M parameters and 200-language support; fastText detects source language; English is always the target. |
| Calendar | No input → date statement | Training date approximated from document URL; evaluation may use a stipulated current date. |

These tools are not interchangeable. The QA system returns a compact answer; search returns material from which the LM must extract the relevant answer. The calculator performs limited arithmetic rather than general program execution. The calendar supplies temporal context but does not itself solve every date-dependent factual question. [A; pp. 4, 15]

## 7.4 Data and preprocessing

The language-modeling corpus is a subset of CCNet. The total starting-document count, exact corpus release, and full composition are not supplied. Documents whose calls all fail filtering are removed, changing the training-example distribution even though retained original text is preserved around inserted calls. [A; pp. 4–5]

Calculator generation considers documents satisfying arithmetic-oriented heuristics: three numbers within 100 tokens where one is an operation result of the other two; selected arithmetic cue strings followed by a number; or at least three numbers, with only 1% retained for documents matching only the final condition. Calendar generation retains documents with extractable URL dates, around 18% of documents. Translation generation uses 10-token chunks, seeking a non-English chunk between English chunks with fastText confidence greater than 0.8, excluding chunks containing only numbers or symbols. [A; p. 15]

Translation calls are additionally removed if their input appears after the call but not before it. During data generation the model can see the full example; at inference it cannot see future text. This filter addresses a specific training-versus-inference lookahead mismatch, not a general proof that all generated calls are free of future-information dependence. [A/D; p. 15]

## 7.5 Training and controls

Fine-tuning uses batch size 128, learning rate 1 × 10^-5, and linear warmup for the first 10% of training. Appendix B reports up to 25,000 examples per API, maximum sequence length 1,024, effective batch size 128, DeepSpeed ZeRO-3, eight NVIDIA A100 GPUs with 40GB each, and BF16 precision. Training lasts up to 2,000 steps. PPL is checked every 500 steps on a 1,000-example CCNet development set, and the best-performing checkpoint is selected. [A; pp. 5, 17]

The main controls are GPT-J without fine-tuning, GPT-J + CC trained on unaugmented C, Toolformer trained on C*, and Toolformer with API calls disabled by setting the API-start probability to zero. OPT 66B and GPT-3 175B provide larger-model comparisons. These controls distinguish corpus fine-tuning, API-augmented training, and active inference-time access, although active toolformer also invokes external models and retrieval. [A/D; p. 5]

No random seeds, repeated-run counts, confidence intervals, significance tests, full optimizer settings, measured tool latency, or execution-cost accounting are reported in the supplied material. Dataset-specific evaluation sample counts are generally absent. They cannot be invented from benchmark names.

## 7.6 Inference

The model writes a call until it emits the response delimiter, at which point decoding pauses. The runtime invokes the corresponding API, inserts its result and the closing marker, and resumes generation. Experiments alter greedy decoding so a call starts whenever the API-start token is within the ten most likely tokens. At most one API call is allowed per input to avoid repeated calls without producing an answer. [A; pp. 4–6]

# 8. Experiments / analyses

| Experiment ID | Purpose and design | Data, metric, and conditions | Main evidence |
|---|---|---|---|
| X1 | Test factual completion with autonomous tools. | LAMA SQuAD, Google-RE, T-REx; retain examples with final-position masks; correct word within first five predicted words; Wikipedia search disabled. | Table 3, p. 6. |
| X2 | Test mathematical problem solving. | ASDiv, SVAMP, MAWPS; inspect first predicted number, or first number after '=' when an equation is generated. | Table 4, p. 6. |
| X3 | Test open-domain question answering. | WebQS, NQ, TriviaQA; correct answer within first 20 words; QA tool disabled because it would make tasks trivial and was trained on NQ. | Table 5, p. 7. |
| X4 | Test multilingual question understanding. | MLQA: English context, question in six languages, English answer; correct answer contained in generation capped at ten words. | Table 6, p. 7. |
| X5a | Test time-varying factual completion. | TEMPLAMA, with facts and answers for 2010–2020; LAMA-style evaluation. | Table 7, pp. 7–8. |
| X5b | Test current-date-dependent questions. | DATESET, 500 sampled current dates and 9,400 template queries; LAMA-style evaluation. | Tables 7 and 11, pp. 8, 17. |
| X6 | Test ordinary language-modeling retention. | WikiText and 10,000 held-out CCNet documents; PPL; API calls disabled. | Table 8, p. 8. |
| X7 | Test model-size effects. | GPT-2 124M, 355M, 775M, 1.6B and GPT-J; only QA, calculator, search tools; average benchmark scores. | Figure 4, pp. 8–9. |
| X8 | Test decoding rank cutoff. | k = 0, 1, 3, 10 on T-REx and WebQS; overall, called and uncalled subsets, call percentage. | Table 9, p. 9. |
| X9 | Inspect generated-call quality. | Ten selected augmented CCNet examples; loss-reduction score and intuitive usefulness annotation. | Table 10, pp. 9–10. |

All downstream comparisons use natural-language task instructions without downstream in-context examples. Appendix C supplies the prompts. Factual completion asks for a factually correct continuation; mathematics appends 'The answer is'; QA prefixes a direct answer request; MLQA explicitly requests an English answer. The experiments use different answer windows and therefore do not share a single interchangeable accuracy definition. [A; pp. 5–7, 17]

X9 is a qualitative illustration, not a measured precision estimate for the entire generated dataset. X7 averages tasks and does not provide every small-model cell numerically. X6 tests ordinary LM behavior with calls disabled, not the full distribution over tool-enabled generation. These boundaries are essential to interpreting the evidence.

# 9. Results

**Factual completion.** Toolformer scores 33.8 on SQuAD, 11.5 on Google-RE, and 53.5 on T-REx, exceeding every listed baseline. The authors report improvements of 11.7, 5.2, and 18.6 points over the best GPT-J-based no-tool baseline. The operands are 33.8−22.1, 11.5−6.3, and 53.5−34.9. These are absolute score-point differences, not relative percentage gains. The model uses the QA tool for 98.1% of examples, another tool for 0.7%, and no tool for 1.2%. [A/B; p. 6]

**Mathematics.** Scores are 40.4, 29.4, and 44.0 for Toolformer versus 14.8, 6.3, and 15.0 with calls disabled. Calculator use occurs on 97.9% of examples across the benchmarks. The authors' claim that active calls more than double performance is supported by each pair. The disabled model also exceeds unmodified GPT-J, but the proposed explanation—learning mathematical capability from call/result examples—is a surmise rather than an isolated mechanism test. [A/B; p. 6]

**Question answering.** Toolformer scores 26.3, 17.7, and 48.8 on WebQS, NQ, and TriviaQA. These exceed the other GPT-J-based rows but fall below GPT-3's 29.0, 22.6, and 65.9. Wikipedia search is used on 99.3% of examples according to the text. Search quality and inability to reformulate or browse results are cited as likely explanations of the remaining gap. [A/B; p. 7]

**Multilingual QA.** Active calls improve every language relative to Toolformer disabled: Spanish 20.6 versus 19.8; German 13.5 versus 11.9; Hindi 1.4 versus 1.2; Vietnamese 10.6 versus 10.1; Chinese 16.8 versus 15.0; Arabic 3.7 versus 3.1. However, unmodified GPT-J remains stronger on German, Chinese, and Arabic. Translation usage ranges from 63.8% to 94.9% for languages other than Hindi; Hindi usage is only 7.3%. The extracted concatenation '1.410.6' is resolved by the visible table as separate Hindi 1.4 and Vietnamese 10.6 cells. [A/B; p. 7]

**Temporal tasks.** Toolformer scores 16.3 on TEMPLAMA and 27.3 on DATESET. Calendar use is only 0.2% for TEMPLAMA, so its improvement cannot reasonably be described as a calendar-driven result. On DATESET, calendar usage is 54.8%, and the authors attribute the improvement to that tool. [A/B; p. 8]

**Language modeling.** GPT-J + CC and Toolformer disabled have identical displayed PPL: 10.3 on WikiText and 10.5 on CCNet. Unmodified GPT-J has 9.9 and 10.6. Thus API-augmented training adds no displayed PPL penalty relative to CCNet-only fine-tuning, while WikiText PPL is worse than unmodified GPT-J. The result supports a narrower preservation claim than 'no performance changes of any kind.' [A/B/D; p. 8]

**Scale and decoding.** The authors place the emergence of useful tool use around 775M parameters, with search as an exception. Increasing decoding k increases calls substantially. T-REx overall scores rise from 34.9 at k=0 to 53.5 at k=10. WebQS rises from 18.9 to 26.3, with the same displayed overall score at k=3 and k=10 despite increased call coverage. [A/B; pp. 8–9]

# 10. Figure-by-figure interpretation

## Figure 1 — Examples of autonomous requests

Figure 1 on page 1 contains four text-completion examples in shaded boxes. Colored spans identify API calls and returned information: pink for QA, blue for calculator, turquoise for translation, and red for Wikipedia search. The examples retrieve a journal publisher, compute 400/1400 as 0.29 before the continuation '29%', translate 'tortuga' into 'turtle', and return a Brown Act description. There are no axes, error bars, or statistical quantities. [B]

The figure demonstrates call placement and the use of returned text in continuation. It does not provide an unbiased sample, a success rate, or evidence that the statements are protected against adversarial content. It also illustrates that calls may occur inside a sentence rather than only before an entire answer. The authors' caption frames these as exemplary predictions, which is the appropriate evidential weight. [A/D]

## Figure 2 — Training-data construction

Figure 2 on page 2 is a left-to-right flowchart. A plain LM dataset feeds stage 1, Sample API Calls; stage 2, Execute API Calls; stage 3, Filter API Calls; and an LM dataset with calls. Arrows show data transformation, not an interactive inference feedback loop. [B]

The Pittsburgh example separates the prefix 'Pittsburgh is also known as' from the target continuation 'the Steel City'. A question about another name returns 'Steel City' and reduces continuation loss; a question about the country returns 'United States' and does not. The retained answer is inserted before the target continuation. The comparison inequalities visually encode helpful-versus-unhelpful responses. [A/B]

This diagram supports the method's central idea: tool calls are selected for relevance to predicting original text. It does not imply that all correct tool answers are useful in every context, or that all retained answers are correct.

## Figure 3 — Demonstration prompt for QA-call generation

Figure 3 on page 3 is a shaded prompt box. It explains the call syntax and contains two input/output demonstrations, one about Joe Biden's birthplace and one about Coca-Cola. Blue spans mark inserted QA calls. The final 'Input: x / Output:' slots indicate where a new document is supplied for annotation. [B]

This is training-data-generation conditioning, not the downstream evaluation prompt. The demonstrations show that several potential calls may be proposed within one document. They are source content and were not executed as instructions during this analysis. No axes, numerical performance, or statistical comparison appears.

## Figure 4 — Performance versus model size

Figure 4 on page 9 has three visually inspected panels, in left-to-right order: LAMA, Math Benchmarks, and QA Benchmarks. The x-axis is Model Parameters (M), with linear ticks at 0, 2000, 4000, and 6000. The plotted models span 124M to the reported 6.7B GPT-J. The y-axis displays average performance but does not print a separate unit label. LAMA and mathematics use a vertical range of 0–30; QA uses 0–40. [B]

Blue solid lines and markers denote Toolformer with calls; coral solid lines and markers denote Toolformer disabled; magenta dotted horizontal lines denote GPT-3. Larger models generally score better, and the blue–coral separation grows substantially in LAMA and mathematics. Search-related QA already shows benefit at smaller sizes. At the largest size, the LAMA and mathematics blue endpoints exceed their GPT-3 reference lines, whereas QA remains below its reference. [B]

Exact intermediate point values are not labeled, so none are reported as exact numerical results. The prose places the broader emergence point around 775M. No error bars or confidence intervals are shown. The lines connect tested sizes and should not be treated as measurements at every intervening parameter count. [A/B/D]

# 11. Table-by-table interpretation

All task-score tables below reproduce displayed point estimates. No significance symbols, confidence intervals, standard deviations, or run counts are supplied for Tables 3–9. Percent-style correctness scores are interpreted under each table's task-specific matching rule, not as a uniform strict exact-match metric.

## Table 1 — API examples, page 5

Rows are the five APIs; columns show name, example input, and output. QA answers where the Knights of Columbus was founded with 'New Haven, Connecticut'. Search returns a fishing-reel snippet. Calculator evaluates 27 + 4 * 2 as 35. Calendar has empty input ε and returns a dated sentence. Translation maps 'sûreté nucléaire' to 'nuclear safety'. This table establishes interface behavior, not benchmark accuracy. Search returns explanatory text while QA returns a concise answer.

## Table 2 — Filtered examples by threshold, page 5

| API | τ_f=0.5 | τ_f=1.0 | τ_f=2.0 |
|---|---:|---:|---:|
| Question answering | 51,987 | 18,526 | 5,135 |
| Wikipedia search | 207,241 | 60,974 | 13,944 |
| Calculator | 3,680 | 994 | 138 |
| Calendar | 61,811 | 20,587 | 3,007 |
| Machine translation | 3,156 | 1,034 | 229 |

The unit is examples with API calls, not necessarily the total number of individual calls. Increasing the required loss reduction reduces every row's yield. Search has the largest counts; translation has the fewest at thresholds 0.5 and 1.0, while calculator has the fewest at 2.0. These counts precede the Appendix B cap of up to 25k training examples per API; they should not be equated automatically with final training consumption. The table does not specify a total count of unique documents across overlapping API rows. [A/B]

## Table 3 — LAMA factual completion, page 6

| Model | SQuAD | Google-RE | T-REx |
|---|---:|---:|---:|
| GPT-J | 17.8 | 4.9 | 31.9 |
| GPT-J + CC | 19.2 | 5.6 | 33.2 |
| Toolformer disabled | 22.1 | 6.3 | 34.9 |
| Toolformer | 33.8 | 11.5 | 53.5 |
| OPT 66B | 21.6 | 2.9 | 30.1 |
| GPT-3 175B | 26.8 | 7.0 | 39.8 |

Toolformer is highest in all columns. The lowest rows differ: GPT-J is lowest on SQuAD, OPT on Google-RE and T-REx. Wikipedia search is prohibited here because the statements come from Wikipedia. QA remains available, so this is not a comparison of unaided internal factual memory alone. The caption says competitive with GPT-3, while the displayed point estimates exceed it on all three subsets; these formulations are compatible rather than contradictory.

## Table 4 — Arithmetic benchmarks, page 6

| Model | ASDiv | SVAMP | MAWPS |
|---|---:|---:|---:|
| GPT-J | 7.5 | 5.2 | 9.9 |
| GPT-J + CC | 9.6 | 5.0 | 9.3 |
| Toolformer disabled | 14.8 | 6.3 | 15.0 |
| Toolformer | 40.4 | 29.4 | 44.0 |
| OPT 66B | 6.0 | 4.9 | 7.9 |
| GPT-3 175B | 14.0 | 10.0 | 19.8 |

Toolformer is highest and OPT lowest in every column. Toolformer disabled exceeds GPT-3 on ASDiv but not SVAMP or MAWPS, an important qualification to broad claims about mathematical gains. Active access to the calculator produces the largest gains. The scoring rule extracts a number rather than requiring a perfectly formatted complete solution.

## Table 5 — Question answering, page 7

| Model | WebQS | NQ | TriviaQA |
|---|---:|---:|---:|
| GPT-J | 18.5 | 12.8 | 43.9 |
| GPT-J + CC | 18.4 | 12.2 | 45.6 |
| Toolformer disabled | 18.9 | 12.6 | 46.7 |
| Toolformer | 26.3 | 17.7 | 48.8 |
| OPT 66B | 18.6 | 11.4 | 45.7 |
| GPT-3 175B | 29.0 | 22.6 | 65.9 |

GPT-3 is highest in all columns; Toolformer is second. Within GPT-J-derived rows, disabled Toolformer is not best on NQ: GPT-J scores 12.8 versus 12.6. The QA API is disabled, leaving search as the dominant retrieval path. The allowed answer window is twenty words, which must accompany any reuse of these numbers.

## Table 6 — MLQA, page 7

| Model | Es | De | Hi | Vi | Zh | Ar |
|---|---:|---:|---:|---:|---:|---:|
| GPT-J | 15.2 | 16.5 | 1.3 | 8.2 | 18.2 | 8.2 |
| GPT-J + CC | 15.7 | 14.9 | 0.5 | 8.3 | 13.7 | 4.6 |
| Toolformer disabled | 19.8 | 11.9 | 1.2 | 10.1 | 15.0 | 3.1 |
| Toolformer | 20.6 | 13.5 | 1.4 | 10.6 | 16.8 | 3.7 |
| OPT 66B | 0.3 | 0.1 | 1.1 | 0.2 | 0.7 | 0.1 |
| GPT-3 175B | 3.4 | 1.1 | 0.1 | 1.7 | 17.7 | 0.1 |
| GPT-J All En | 24.3 | 27.0 | 23.9 | 23.3 | 23.1 | 23.6 |
| GPT-3 All En | 24.7 | 27.2 | 26.1 | 24.9 | 23.6 | 24.0 |

Es, De, Hi, Vi, Zh, and Ar represent Spanish, German, Hindi, Vietnamese, Chinese, and Arabic. Among the multilingual-question conditions, Toolformer leads Spanish, Hindi, and Vietnamese; GPT-J leads German, Chinese, and Arabic. The All En rows change the input condition by making both question and context English, so their higher scores are not same-condition tool-use victories. GPT-3 All En is highest in every column. OPT and GPT-3 tie at 0.1 in Arabic in the multilingual setting. The caption explicitly warns that CCNet fine-tuning can deteriorate multilingual performance.

## Table 7 — Temporal datasets, page 8

| Model | TEMPLAMA | DATESET |
|---|---:|---:|
| GPT-J | 13.7 | 3.9 |
| GPT-J + CC | 12.9 | 2.9 |
| Toolformer disabled | 12.7 | 5.9 |
| Toolformer | 16.3 | 27.3 |
| OPT 66B | 14.5 | 1.3 |
| GPT-3 175B | 15.5 | 0.8 |

Toolformer is highest on both datasets. Toolformer disabled is lowest on TEMPLAMA; GPT-3 is lowest on DATESET. The calendar is scarcely used on TEMPLAMA, while it is important on DATESET. Thus a common temporal-task label hides different mechanisms: retrieving time-sensitive facts versus obtaining the date needed for date arithmetic or calendar reasoning.

## Table 8 — Language-model perplexity, page 8

| Model | WikiText | CCNet |
|---|---:|---:|
| GPT-J | 9.9 | 10.6 |
| GPT-J + CC | 10.3 | 10.5 |
| Toolformer disabled | 10.3 | 10.5 |

Lower is better. GPT-J is best on WikiText; the two fine-tuned rows tie on CCNet and on WikiText. The tie is at the reported one-decimal precision and does not establish numerical identity beyond that precision. The enabled Toolformer row is absent because the authors consider the required marginalization over possible calls intractable. This is an explicit measurement limitation, not a missing result to be estimated.

## Table 9 — API-start rank cutoff, page 9

| k | T-REx All | AC | NC | Calls % | WebQS All | AC | NC | Calls % |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.9 | — | 34.9 | 0.0 | 18.9 | — | 18.9 | 0.0 |
| 1 | 47.8 | 53.0 | 44.3 | 40.3 | 19.3 | 17.1 | 19.9 | 8.5 |
| 3 | 52.9 | 58.0 | 29.0 | 82.8 | 26.3 | 26.5 | 6.6 | 99.3 |
| 10 | 53.5 | 54.0 | 22.5 | 98.1 | 26.3 | 26.4 | — | 100.0 |

All means overall performance; AC means the subset where a call is made; NC means no call. Dashes indicate an unavailable or empty subgroup result, not zero accuracy. T-REx's highest AC score is 58.0 at k=3, even though overall performance is highest at k=10. These subsets change as k changes, so differences in AC are not paired performance changes on a fixed sample. At k=1, uncalled examples have higher performance than the no-call baseline, supporting the authors' limited calibration observation. Greater call frequency is not automatically greater efficiency.

## Table 10 — Qualitative generated-call quality, page 10

The table sorts ten examples by loss reduction L_i^-−L_i^+. Useful-marked examples score 5.49 for a Flodden memorial search, 2.11 for a calendar date before 'March 10', 2.08 for Nile-length QA, 1.59 for 735/499 arithmetic, 0.70 for translating a Jersey schools phrase, and 0.33 for an Easter-event calendar call. Non-useful-marked examples score 0.92 for an irrelevant 'Fast train success' search, −0.02 for 85/23 arithmetic in an unsuitable context, −0.41 for an unrelated calendar insertion, and −1.23 for malformed contextual QA. [A/B]

The high-scoring irrelevant search is a visible counterexample to treating loss reduction as perfect semantic usefulness. The low-scoring useful examples show that a strict threshold can exclude intuitive usefulness. The source prose calls the fast-train case the fourth example, while the visible table puts it fifth. The example's identity and score are clear; the ordinal mismatch is reported rather than silently repaired. The table gives no sampling protocol or dataset-wide noise rate.

## Table 11 — DATESET templates, page 17

Seven template families have sizes 400, 800, 800, 400, 4,000, 1,800, and 1,200, totaling 9,400. They ask elapsed or remaining days to specified dates; past date components from elapsed durations; future components from remaining days; weekdays of dates; components around yesterday/today/tomorrow; holiday date components; and durations to or since holidays. Holiday templates use United States federal holidays. [A/B]

The sum 400+800+800+400+4,000+1,800+1,200=9,400 agrees with the displayed total; this arithmetic check is analyst-derived. The counts do not imply that each of 500 current dates contributes an equal number of questions. The exact template-instantiation and sampling allocation needed to reproduce every example is not supplied.

# 12. Diagram / architecture interpretation

Figure 2 is the explicit training architecture diagram and is represented in §10. Its input is ordinary text; intermediate artifacts are candidate call positions, requests, results, and scored requests; its output is augmented text for fine-tuning. The filter is a decision stage: retain a call only when response-inclusive loss beats the stronger no-response alternative by the specified margin. [A/B]

The inference architecture is described in prose rather than a separate diagram. Its components are the fine-tuned LM, a decoding controller, a selected API implementation, and a text context that receives the response. Control flows from generation to external execution at the response delimiter, then back to generation after insertion. The model chooses call content, while the runtime executes it. Multiple APIs share this general textual interface. [A; p. 4]

There is no visual architecture of a web browser, permissions system, sandbox, security monitor, or chain of dependent tool calls. Such components cannot be imported into the paper's system description. For the user's review question, this architecture can be used to identify interface questions, but not to claim demonstrated compromise. [D]

# 13. Equations and mathematical concepts

The paper's important equations are unnumbered. E1–E7 below are analyst inventory anchors, not original equation numbers.

**E1 — API serialization, p. 2, §2.** A call is c=(a_c,i_c), where a_c is the API name and i_c its input. The request alone is e(c)=<API> a_c(i_c) </API>. With returned text r it becomes e(c,r)=<API> a_c(i_c) → r </API>. These are text representations, not numerical optimization equations. In practice the existing token sequences ' [', ']', and '->' implement the conceptual delimiters, avoiding vocabulary changes. The exact opening sequence includes a leading space. [A; footnote 1]

**E2 — Candidate start probability, p. 3.** p_i=p_M(<API> | P(x),x_{1:i−1}). M is the model; P(x) is the demonstration prompt for full example x; x_{1:i−1} is its prefix before candidate position i; p_i is the probability assigned to starting a call. Positions satisfying p_i>τ_s are retained, limited to the top k when necessary. Up to m request strings are sampled at each position. Inputs are prompt and prefix; output is a candidate set, not a guaranteed useful-call set. [A]

**E3 — Weighted continuation loss, p. 3.** L_i(z)=−Σ_{j=i}^{n} w_{j−i} log p_M(x_j | z,x_{1:j−1}). The sequence x has n tokens, i is the proposed call position, z is additional prefix information, and w weights distances from the call. The negative log probabilities penalize poor predictions of the original remaining text. Summation combines those penalties, emphasizing nearby tokens under the chosen weights. [A]

**E4 — Response and no-response comparators, p. 3.** L_i^+=L_i(e(c_i,r_i)); L_i^−=min(L_i(ε),L_i(e(c_i,ε))). ε is the empty sequence. L_i^+ scores a call with its actual response. L_i^− selects the lower loss between no call and a call with no response. The minimum makes the retained response compete against the better baseline. Superscript '+' does not mean larger loss; it means response-inclusive condition. [A]

**E5 — Retention rule, p. 3.** Keep a call if L_i^−−L_i^+≥τ_f. A positive difference means adding returned information reduces loss. τ_f is a required improvement margin. This is a utility filter for future-token prediction; it is not a factuality, provenance, maliciousness, or security criterion. The latter distinction is analyst interpretation grounded in the equation's measured quantity. [A/D]

**E6 — Augmented sequence, pp. 3–4.** x*=x_{1:i−1},e(c_i,r_i),x_{i:n}. Commas denote concatenated sequence parts. Original prefix and continuation surround the inserted call/result. The procedure extends to documents with several surviving calls. Collecting these sequences produces C*, used for ordinary LM fine-tuning. Calls are generated independently across tools, so this equation does not construct chained tool dependencies. [A]

**E7 — Local weighting, p. 5.** w_t=tilde(w)_t/Σ_{s∈N}tilde(w)_s, with tilde(w)_t=max(0,1−0.2t). The maximum prevents negative weights; normalization rescales them; the decreasing function prioritizes near-future tokens. [C] For nonnegative offsets t, unnormalized weights at 0,1,2,3,4 are 1,0.8,0.6,0.4,0.2 and become zero at 5. These values follow directly from substituting t. The paper uses N without explicitly clarifying its starting index, so a specific normalized denominator should not be attributed to the authors without that convention. The methodological meaning—local emphasis—is clear. [A/D]

There are no theorems or mathematical guarantees that the retained calls are correct, globally optimal, safe, or sufficient to preserve every capability. The equations define a training-data-selection procedure and its rationale.

# 14. Interpretation and discussion

The strongest supported finding is that a prediction-based training signal can teach a pretrained model useful inference-time access to several specialized resources. The tool-disabled condition shows that training effects and active external access both matter. The largest arithmetic gains arise when the calculator is actually available; the largest factual-completion gains use the QA model. [A/B]

The results answer O3 positively for several selected task families, with important exceptions and narrower comparisons. They answer O4 by showing no additional displayed PPL cost relative to unaugmented CCNet fine-tuning on two datasets with tools disabled. O5 shows size-dependent gains in the tested range, not a universal threshold law. O6 reveals that a runtime decoding choice substantially changes call frequency and scores. O7 shows an imperfect but useful association between the filtering signal and intuitive relevance. [D, source-grounded synthesis]

The statement that C* preserves original texts needs to be read together with document filtering and the Appendix A prompts. Retained training text surrounds inserted calls, but documents with no useful call are excluded. Additionally, one calculator demonstration alters original content rather than merely inserting calls. These details limit a literal reading of unchanged-content claims. [A/B/D]

For the user's security review, Toolformer supplies an example of model-selected external execution and returned-text conditioning. It also documents wording-sensitive tool selection and a filtering objective that can retain irrelevant content. These features motivate security questions about influence and trust, but the paper does not establish attackability, prompt-injection success, data leakage, or greater vulnerability than standalone LMs. Calling its task-score comparisons a security comparison would change both the measured construct and the paper's purpose. [D]

# 15. Contributions and novelty

**Conceptual contribution.** Treat helpful tool use as behavior discoverable from the model's own continuation-prediction feedback, while maintaining broadly applicable text generation rather than specializing solely to a downstream task. [A; pp. 1–3]

**Methodological and algorithmic contribution.** Sample candidate call positions and arguments, execute calls, compare response-inclusive loss against no-response alternatives, retain useful calls, and fine-tune on interleaved text. This combines few API demonstrations with large-scale automated annotation. [A; §2]

**System/interface contribution.** A common text serialization and an inference pause-and-resume mechanism connect five different APIs without modifying the existing vocabulary. This is an implementation approach, not a claim of a secure or fully general agent platform. [A; pp. 2, 4]

**Dataset contribution.** DATESET introduces current-date-dependent template questions. Its reported construction uses 500 sampled current dates and 9,400 queries across seven families. The paper supplies templates and a high-level process, but the supplied material does not establish availability of a released dataset artifact. [A; Appendix D]

**Empirical contribution.** Controlled comparisons show benefits across factual completion, arithmetic, question answering, and synthetic temporal reasoning, alongside mixed multilingual results and a model-size study. There is no theoretical security contribution, formal correctness guarantee, or adversarial benchmark in the supplied work. [A/D]

# 16. Limitations

## Authors' stated limitations

1. **No chained tool use.** The output of one call cannot be learned as the input to a later tool because calls are generated independently and chained examples are absent. [A; p. 11]
2. **No interactive tool use.** The model cannot browse many search results or refine a query after seeing an unhelpful result. [A; pp. 7, 11]
3. **Input-wording sensitivity.** Whether to call an API can depend strongly on exact prompt wording. [A; p. 11]
4. **Sample inefficiency.** Processing more than a million documents yields only a few thousand useful calculator examples. [A; p. 11]
5. **No tool-cost-aware selection.** The decision to call an API ignores its tool-dependent computational cost. [A; p. 11]
6. **One-call evaluation restriction.** It prevents loops but also prohibits strategies such as obtaining a date and then querying QA with that date. [A; pp. 6, 8]
7. **Search mismatch.** Retrieved snippets can be poor matches; the model cannot repair that through interaction. [A; p. 7]
8. **Language-modeling measurement limitation.** Enabled-call PPL is not evaluated because marginalization over potential calls is considered intractable. [A; p. 8, footnote 8]
9. **Imperfect filtering.** An irrelevant search can still reduce loss. [A; pp. 9–10]

## Additional evidence-based analyst observations

The task families were selected because the authors expected at least one tool to help, so they do not measure a representative distribution of all user requests. Exact evaluation sample counts, uncertainty estimates, and independent runs are generally unavailable. The effective system includes external QA and translation models; describing its performance solely through the main LM parameter count understates the resources available to active tool use. [D]

The QA tool changes from Atlas-large for dataset creation to Atlas-xxl at inference. Calendar dates extracted from URLs may imperfectly represent document creation time, although that uncertainty is not quantified. DATESET is templated and uses stipulated dates, limiting conclusions about natural temporal requests. The text-based loss filter measures predictive usefulness rather than security or source reliability. None of these observations should be presented as an author-admitted attack vulnerability. [D]

# 17. Threats to validity

The following validity labels are analyst categories, not section headings or claims used by the authors.

**Internal validity.** GPT-J + CC and Toolformer disabled are useful controls for corpus fine-tuning and active tools. However, filtered-document selection, augmented-call training, inference-time API access, and decoding changes jointly shape performance. The enabled comparison measures the complete configuration rather than a single isolated mechanism. [D]

**Construct validity.** Correct-answer containment in five, ten, or twenty words and number extraction are task-specific proxies. They allow more output variation than strict exact match. API call frequency measures use, not correctness, necessity, safety, or efficiency. Perplexity measures predictive behavior, not comprehensive language understanding or security. [D]

**External and ecological validity.** Fixed Wikipedia snippets, basic arithmetic, a date-returning API, and a one-call runtime are narrower than multi-step web agents. Results from these selected benchmarks should not be extended to browsing, authenticated actions, or changing live websites. The synthetic DATESET templates do not establish performance on every natural calendar question. [D]

**Statistical conclusion validity.** The supplied point estimates show substantial differences, but no confidence intervals, significance tests, repeated runs, or benchmark sample denominators are reported. Statistical robustness cannot be assessed from numerical magnitude alone. [D]

**Reproducibility.** Thresholds, heuristics, hardware, prompts, and training limits are disclosed, helping reconstruction. Missing corpus details, seeds, exact benchmark subsets, optimizer configuration, tool versions, retrieval parameters, and artifact availability prevent claiming a fully specified reproduction. No reproduction was attempted in this analysis. [D]

**Security generalizability.** There are no malicious tool responses or agent-versus-standalone attack conditions. Comparative vulnerability has UNKNOWN evidential support in this paper, even though architectural relevance is meaningful. [D]

# 18. Future work and open questions

## A. Future work explicitly proposed by the authors

The authors suggest adding interactive search behavior, including reformulating queries and browsing multiple results. They propose iterative application of their generation-and-filtering approach as a possible response to sample inefficiency. The limitations identify chained use and computational-cost awareness as unresolved capabilities, although the text does not present an implemented solution for them. [A; pp. 7, 11]

## B. Additional open questions logically remaining

How would a model learn dependent calls when the second request must use the first result? How much improvement comes from the main LM versus stronger external models? Which input wordings change tool selection, and how often? How well does filtering identify useful calls across the entire dataset rather than selected illustrations? What is the accuracy-versus-cost tradeoff at different decoding cutoffs? [D]

For the review question, further work would need to specify who can control tool-returned text, which model or runtime decisions it can influence, what assets are at risk, and how attack outcomes compare with a matched standalone model. These are analyst-proposed investigation questions. Toolformer supplies neither attack measurements nor a conclusion that any particular attack succeeds. [D]

# 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this paper |
|---|---|
| LM | Language model predicting text continuations. |
| API | Application programming interface used to request a tool result. |
| QA / Q&A | Question answering; here also an external factoid-answer tool. |
| MT | Machine translation into English. |
| GPT-J, GPT-2, GPT-3, OPT | Model families used in the experiments; names are retained as reported. |
| CCNet | Corpus source for fine-tuning and held-out language-model evaluation. |
| BM25 | Named retrieval method used for Wikipedia search; no formula is supplied. |
| KILT | Named source of the indexed Wikipedia dump; acronym expansion is not supplied. |
| NLLB | Named translation model; its cited work is titled No Language Left Behind. |
| fastText | Classifier used for language detection. |
| LAMA | Named factual-completion benchmark; evaluated through three subsets. |
| SQuAD, Google-RE, T-REx | LAMA subset names; exact expansions are not supplied here. |
| ASDiv, SVAMP, MAWPS | Arithmetic benchmark names; exact acronym expansions are not supplied. |
| WebQS | Table abbreviation for Web Questions. |
| NQ | Natural Questions. |
| MLQA | Multilingual question-answering benchmark. |
| TEMPLAMA | Temporal cloze dataset covering changing facts. |
| DATESET | Authors' generated date-dependent question dataset. |
| PPL | Perplexity, reported language-model prediction measure. |
| BF16 | Training precision designation; detailed representation is not defined in the paper. |
| ZeRO-3 | DeepSpeed training configuration named in Appendix B; mechanics are not explained. |
| Zero-shot | Downstream instruction without in-context task examples. |
| Greedy decoding | Selecting the most likely next token, modified here for API starts. |
| C / C* | Original text dataset / dataset augmented with retained API calls. |
| M / p_M | Language model / its next-token probability function. |
| x, x_j, n | Text sequence, its jth token, and its length. |
| P(x) | Prompt showing how to annotate example x with calls. |
| c=(a_c,i_c) | Call comprising API name and input. |
| r / e(c,r) | Returned text / serialized call with returned text. |
| ε | Empty sequence. |
| τ_s / τ_f | Call-start sampling threshold / minimum loss reduction for retention. |
| k | Sampling-position cap in data generation; API-start rank cutoff in decoding. |
| m | Maximum sampled calls per candidate position. |
| L_i(z) | Weighted prediction loss after adding prefix z. |
| L_i^+ / L_i^- | Response-inclusive loss / better no-response alternative loss. |
| w_t | Weight on a token at offset t after the proposed call. |
| AC / NC / All | Called subset / uncalled subset / complete evaluated set. |

Names whose expansions are absent are preserved rather than filled with outside knowledge. This keeps the glossary source-bounded.

# 20. Key numerical results

The complete displayed benchmark cells are preserved in §11. This compact ledger emphasizes configuration, usage, and major outcomes; it does not replace the table-specific conditions.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main model size | 6.7B | parameters | GPT-J as described by authors | Author-reported | pp. 2, 11 |
| Larger baselines | 66B; 175B | parameters | OPT; GPT-3 | Author-reported | p. 5 |
| Translation model | 600M; 200 | parameters; languages | NLLB | Author-reported | pp. 4, 15 |
| Default generation thresholds | 0.05; 1.0 | probability; loss margin | τ_s; τ_f | Author-reported | p. 15 |
| Default candidate limits | 5; 5 | positions; calls per position | k; m | Author-reported | p. 15 |
| Calculator/MT thresholds | 0.0; 0.5 | probability; loss margin | Special generation settings | Author-reported | p. 15 |
| Calculator/MT candidate limits | 20; 10 | positions; calls per position | Special generation settings | Author-reported | p. 15 |
| Fine-tuning learning rate | 1 × 10^-5 | learning rate | Linear warmup first 10% | Author-reported | p. 5 |
| Training limits | 25k; 1,024; 2k | examples/API; tokens; steps | Upper limits | Author-reported | p. 17 |
| Hardware | 8 × A100, 40GB each | GPUs; memory/GPU | BF16, ZeRO-3 | Author-reported | p. 17 |
| Development evaluation | 1,000; every 500 | examples; steps | Best-PPL checkpoint selection | Author-reported | p. 17 |
| Default decoding | 10; 1 | rank cutoff; calls/input | Modified greedy generation | Author-reported | p. 6 |
| LAMA Toolformer scores | 33.8; 11.5; 53.5 | correctness score | SQuAD; Google-RE; T-REx | Visually readable | Table 3, p. 6 |
| LAMA gain over best GPT-J no-call row | 11.7; 5.2; 18.6 | score points | Matching three subsets | Author-reported | p. 6 |
| Arithmetic Toolformer scores | 40.4; 29.4; 44.0 | correctness score | ASDiv; SVAMP; MAWPS | Visually readable | Table 4, p. 6 |
| QA Toolformer scores | 26.3; 17.7; 48.8 | correctness score | WebQS; NQ; TriviaQA | Visually readable | Table 5, p. 7 |
| Temporal Toolformer scores | 16.3; 27.3 | correctness score | TEMPLAMA; DATESET | Visually readable | Table 7, p. 8 |
| QA-tool usage | 98.1 | % examples | LAMA | Author-reported | p. 6 |
| Calculator usage | 97.9 | % examples | Arithmetic benchmarks | Author-reported | p. 6 |
| Wikipedia-search usage | 99.3 | % examples | QA benchmarks, prose report | Author-reported | p. 7 |
| Translation usage | 63.8–94.9; Hindi 7.3 | % examples | MLQA | Author-reported | p. 7 |
| Calendar usage | 0.2; 54.8 | % examples | TEMPLAMA; DATESET | Author-reported | p. 8 |
| Toolformer-disabled PPL | 10.3; 10.5 | perplexity | WikiText; held-out CCNet | Visually readable | Table 8, p. 8 |
| Held-out CCNet | 10,000 | documents | Language-model evaluation | Author-reported | p. 8 |
| Smaller model sizes | 124M; 355M; 775M; 1.6B | parameters | GPT-2 scaling series | Author-reported | p. 8 |
| DATESET construction | 500; 9,400 | current dates; questions | Seven template families | Author-reported | p. 17 |
| DATESET active-minus-disabled score | 27.3−5.9=21.4 | score points | Same displayed evaluation | Analyst-derived | Table 7, p. 8 |
| DATESET template total check | 400+800+800+400+4,000+1,800+1,200=9,400 | questions | Sum of displayed families | Analyst-derived | Table 11, p. 17 |

Derived differences are absolute score-point differences. No relative percentage improvement is implied. Figure 4's unlabeled point coordinates are deliberately excluded from this exact-number ledger.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Useful calls can be selected with model prediction feedback. | Response-inclusive loss must improve over the stronger no-response baseline. | E3–E5, X9 | p. 3; Table 10 | HIGH for method; qualitative usefulness is imperfect. |
| Toolformer learns several tool interfaces. | Five implementations and task-dependent usage patterns. | Table 1, X1–X5 | pp. 4–8 | HIGH for studied configuration; no unrestricted agent generality. |
| Active tools improve factual completion. | 33.8/11.5/53.5 versus best GPT-J no-call 22.1/6.3/34.9. | Table 3, X1 | p. 6 | HIGH for displayed scores; search disabled, QA available. |
| Active calculator access strongly improves arithmetic. | 40.4/29.4/44.0 versus disabled 14.8/6.3/15.0. | Table 4, X2 | p. 6 | HIGH; task-specific number extraction, no uncertainty estimates. |
| Ordinary QA improvements do not surpass GPT-3. | Toolformer below GPT-3 on all three QA columns. | Table 5, X3 | p. 7 | HIGH; QA API disabled, search available. |
| Multilingual benefit depends on comparison. | Active exceeds disabled in six languages but not vanilla GPT-J in all. | Table 6, X4 | p. 7 | HIGH; English context and answer, mixed-language questions. |
| DATESET benefit is associated with calendar use. | 27.3 score, 54.8% use; author attribution. | Tables 7, 11, X5b | pp. 8, 17 | HIGH for reports; not a general temporal-agent result. |
| API augmentation adds no displayed PPL penalty against CC fine-tuning. | Both rows 10.3/10.5. | Table 8, X6 | p. 8 | HIGH; disabled inference only, reported precision. |
| More permissive decoding changes behavior. | Calls rise sharply with k; overall scores improve or plateau. | Table 9, X8 | p. 9 | HIGH; called subsets change across conditions. |
| Current method lacks chained/interactive use and cost-aware decisions. | Explicit limitations. | S7 | p. 11 | HIGH; limits current implementation. |
| Toolformer is relevant to external-content influence questions. | Runtime inserts API response before continued generation. | Inference architecture | p. 4 | MEDIUM analyst inference; no attack demonstrated. |
| Comparative web-agent vulnerability is not established. | Experiments measure correctness and PPL, with no adversarial conditions. | Entire experiment register | pp. 4–11 | HIGH about the supplied study's scope; vulnerability itself UNKNOWN. |

## Cross-reference and consistency findings

1. **Content-preservation claim versus calculator demonstration.** Page 4 states that augmented data retain the exact original texts apart from calls. On page 16, a calculator demonstration changes 'three times less than the 2169 goals last year' into 'twenty goals more than the ... 703 goals last year'. This is a prompt-example inconsistency, not proof that the final generated corpus systematically changes original documents. Its downstream effect is unknown.
2. **Filtering inequality wording.** Page 3 defines sampling with p_i>τ_s; page 15 describes it as probability 'at least 5%'. Strict greater-than and greater-than-or-equal differ at the exact boundary. The supplied work does not specify how implementation resolves exact equality.
3. **Fast-train example ordinal.** Page 9 calls it the fourth example; Table 10 on page 10 places it fifth. The content and score 0.92 are unambiguous.
4. **API usage percentages require matching meanings.** Page 7 reports 99.3% Wikipedia-search use for QA; Table 9 reports 100.0% any-API calls for WebQS at k=10. These differ in tool definition and aggregation scope, so they are not automatically contradictory. The remaining allocation cannot be recovered exactly.
5. **Rounded subgroup numbers.** Some Table 9 overall and subgroup point estimates do not permit exact reconstruction at displayed precision. Raw numerators and denominators are absent. No stronger reconciliation is claimed.
6. **Model-size naming.** The main prose reports 6.7B parameters, while the reference title calls GPT-J a '6 Billion Parameter' model. This analysis preserves the paper's explicit experimental size rather than deriving a replacement from the bibliographic title.
7. **DATESET allocation.** The 9,400-template total is internally additive, but Appendix D's 500 current dates do not disclose a fully specified per-date instantiation count. This is missing reconstruction detail, not evidence of a false total.

# 22. Very simple explanation — Explain Like I'm 15

Imagine a text-writing model that is good at finishing sentences but sometimes bad at arithmetic or remembering facts. The researchers give it access to a calculator, a search service, a translator, a question-answering system, and a date service. They show it a few examples of how to ask each service for help.

Then the model tries adding requests inside many existing texts. The researchers run those requests and ask a simple question: did the result make it easier for the model to predict the words that were already supposed to come next? Useful examples become training material. Later, the model can ask a tool for help while writing an answer.

This works especially well for arithmetic and filling in facts in the tested setup. It helps other tasks too, but it does not always beat a much larger model. It also cannot learn a full chain such as 'get the date, then use that date in another search', and the tests allow only one request per input.

For your security question, the important connection is that information from another service becomes part of what the model reads before continuing. That gives a security researcher a place to investigate unwanted influence. But this paper does not test malicious information or show that web agents are more vulnerable than standalone models. It explains a capability and its limits, not an attack result.

# Completeness Audit

The inventory denominator is the supplied 17-page text and eleven rendered pages, not unspecified material outside the input. 'Fully represented' below means the substantive available content is explained, not that every original sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliations, version | Yes, text and image | Yes | Fully represented | §2; no venue invented. |
| Abstract S0 | Yes, text and image | Yes | Represented in compressed form | Main aims and findings integrated. |
| §1 Introduction S1 | Yes, text and images | Yes | Fully represented | Motivation, prior-work gap, desiderata. |
| §2 Approach S2 | Yes, text and images | Yes | Fully represented | Sampling, execution, filtering, training, inference. |
| Sampling subsection | Yes | Yes | Fully represented | Thresholds, caps, closing-marker rejection. |
| Execution subsection | Yes | Yes | Fully represented | One text response per call. |
| Filtering subsection | Yes | Yes | Fully represented | Equations and prefix-scoring caveat. |
| Fine-tuning and inference subsections | Yes | Yes | Fully represented | Insertion and runtime execution distinctions. |
| §3 five tool subsections S3 | Yes | Yes | Fully represented | Implementations, constraints, different output types. |
| §4.1 generation/training/baselines | Yes | Yes | Fully represented | Tables 1–2, controls, configuration. |
| §4.2 downstream setup | Yes | Yes | Fully represented | Zero-shot, modified greedy, one-call limit. |
| §4.2.1 LAMA / X1 | Yes | Yes | Fully represented | Metric, exclusions, every Table 3 cell. |
| §4.2.2 Math / X2 | Yes | Yes | Fully represented | Number extraction exception, every Table 4 cell. |
| §4.2.3 QA / X3 | Yes | Yes | Fully represented | QA disabled, search limits, every Table 5 cell. |
| §4.2.4 MLQA / X4 | Yes | Yes | Fully represented | Six languages, All En conditions, every Table 6 cell. |
| §4.2.5 Temporal / X5a–b | Yes | Yes | Fully represented | Different mechanisms and usage percentages. |
| §4.3 LM / X6 | Yes | Yes | Fully represented | Held-out corpus, disabled PPL, footnote limitation. |
| §4.4 Scaling / X7 | Yes | Yes | Fully represented | Model sizes, tool subset, visual-only numerical limits. |
| §5 Decoding / X8 | Yes | Yes | Fully represented | Every Table 9 cell and changing subgroup caution. |
| §5 Data quality / X9 | Yes | Yes | Fully represented | All ten scores and usefulness markings summarized. |
| §6 Related Work S6 | Yes, partly text-only | Yes | Represented in compressed form | Three categories and TALM distinction; citations not independently validated. |
| §7 Limitations S7 | Yes, text-only | Yes | Fully represented | All five core limitations preserved. |
| §8 Conclusion S8 | Yes, text-only | Yes | Represented in compressed form | Integrated into findings and contributions. |
| References SR | Yes, text-only | Partly | Represented in compressed form | Role and relevant cited methods preserved; full bibliography not repeated. |
| Objectives O1–O7 | Yes | Yes | Fully represented | Analyst identifiers for informal author objectives. |
| Author hypotheses/surmises | Yes | Yes | Fully represented | Scaling ease, multilingual shift, disabled math gains qualified. |
| F1 examples | Yes, visually | Yes | Fully represented | Four tool examples and evidential scope. |
| F2 process diagram | Yes, visually | Yes | Fully represented | Inputs, arrows, stages, decisions. |
| F3 prompt box | Yes, visually | Yes | Represented in compressed form | Syntax and two-example role; duplicate Appendix A text compressed. |
| F4 LAMA panel | Yes, visually | Yes | Fully represented | Axes, range, encoding, trend; no fabricated coordinates. |
| F4 Math panel | Yes, visually | Yes | Fully represented | Same visual audit, distinct trend. |
| F4 QA panel | Yes, visually | Yes | Fully represented | Search exception and GPT-3 gap. |
| T1 API examples | Yes, visually | Yes | Fully represented | All five rows summarized. |
| T2 threshold counts | Yes, visually | Yes | Fully represented | Every cell preserved. |
| T3–T9 results | Yes, visually | Yes | Fully represented | Every displayed cell preserved with conditions. |
| T10 quality examples | Yes, visually | Yes | Represented in compressed form | All scores/labels and substantive examples; long snippets shortened. |
| T11 DATESET templates | Yes, visually | Yes | Represented in compressed form | Seven families, every count, holiday scope. |
| E1–E7 equations | Yes, visually | Yes | Fully represented | Symbols, inputs, meaning, and indexing uncertainty. |
| Procedural algorithm | Yes | Yes | Fully represented | §7 and §12; no numbered pseudocode exists. |
| Theorems/proofs | Not present | Accounted for | Not applicable | None supplied. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, method, interface, dataset, empirical. |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst observations. |
| Appendix A.1 implementation | Yes, text-only | Yes | Fully represented | All tool-specific details and heuristics. |
| Appendix A.2 prompts | Yes, text-only plus partial image | Yes | Represented in compressed form | All five prompt families; altered calculator example flagged. |
| Appendix B training | Yes, text and image | Yes | Fully represented | Hardware, caps, checkpoints. |
| Appendix C.1–C.4 prompts | Yes, text and image | Yes | Represented in compressed form | Four task prompt patterns and output-language requirement. |
| Appendix D DATESET | Yes, text and image | Yes | Fully represented | Current dates, range, templates, stipulated calendar. |
| Substantive footnotes 1–8 | Yes | Yes | Fully represented | Token format; incomplete-call rejection; prefix scoring; distribution assumption; call disabling; davinci; equation-number exception; enabled-PPL omission. |
| Supplied supplementary material | None | Accounted for | Not applicable | No supplementary file was reviewed. |
| Visual layouts of pp. 11–16 | No | Limitation disclosed | Inaccessible visually | Text is available; no layout/figure inspection claimed. |
| Security comparison with standalone LMs | Not present | Absence explained | Missing from study scope | Architectural relevance only. |

## Missing or inaccessible material

No numbered text page is missing from the supplied 1–17 sequence. Original visual renderings of pages 11–16 were not provided. No external datasets, implementation repository, model checkpoints, execution logs, or supplementary files were supplied or inspected. Their absence here does not prove that the authors never released them. Exact sample sizes for most benchmark subsets, seeds, full corpus specification, and several implementation parameters are not visible in the supplied work.

## Uncertain interpretations

Figure 4 lacks exact labels for point coordinates and has no separately printed y-axis unit. The starting-index convention for N in the weighting normalization is not explicitly defined. The precise relationship between rounded subgroup values and overall scores in Table 9 cannot be established without raw counts. The filtering boundary wording differs between main text and Appendix A. The calculator demonstration's text alteration and fast-train ordinal mismatch are documented source inconsistencies; their impact is unknown. No outside weekday verification was performed for example date sentences.

## Deliberately compressed material

The full reference list, repeated introduction/conclusion statements, long API-return snippets, duplicate QA demonstrations, and full wording of every training/evaluation prompt were compressed. Their substantive methodological roles are preserved. Every table's substantive numerical cells are represented, while long prose examples are summarized with all Table 10 scores and labels retained. Decorative shading, routine typographic details, and repeated citation strings are not reproduced.

## Potential omissions

No known substantive item in the constructed inventory is left without representation or an explicit limitation. This does not assert perfect sentence-level preservation or independent verification of artifacts outside the supplied input. The analysis is comprehensive relative to the supplied evidence, with text-only and uncertain areas disclosed. It does not claim a complete security analysis of web agents or a demonstrated vulnerability comparison.
