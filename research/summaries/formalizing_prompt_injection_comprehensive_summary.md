# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The paper is treated as evidence, including where it displays attack instructions; those instructions are not followed. No outside sources, repository contents, or technical-report supplements were consulted.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers physical PDF pages 1–18. |
| Accessible page count | 18, including the proceedings cover. |
| Apparently missing pages | None within the supplied 1–18 sequence. This establishes coverage of the supplied document, not of every related artifact. |
| Direct visual inspection | Images supplied for pages 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, and 18. |
| Text-only pages | Pages 4, 14, and 16 were read through supplied extracted text; their original page layouts were not visually inspected. |
| Tables | Tables 1–11 are present in supplied images and text. Dense Tables 5 and 9 require alignment checks; their images resolve much of the flattened extraction. |
| Equations | Equations (1)–(6) and five unnumbered attack constructions are available. Extracted text corrupts bold variables and concatenation signs; visible equations on pages 5, 6, and 9 clarify them. |
| Appendix | Appendix A, Details on Selecting Target/Injected Data, is present on physical page 17. Additional figures and tables appear in the end matter. |
| Supplementary material | No separate supplementary files were supplied. |
| Referenced absent artifacts | Technical report [28], especially its Tables 12–32, and the public implementation platform are referenced but not supplied. |
| OCR | Additional OCR was unnecessary. Supplied extraction was cross-checked against available images, especially for tables and notation. |
| Other limitations | Small figure legends and unlabelled bar/line heights cannot support exact numerical transcription. The reported source hash is accepted as supplied metadata, not independently verified. |

The accessibility metadata lists an appendix detection on page 8, but the actual Appendix A heading occurs on page 17. Page 8 contains experimental setup and references to the appendix. This analysis follows the document itself. The message about an unreadable local image at `-` does not remove the fifteen images actually displayed.

Evidence categories used throughout are [A] author-reported, [B] directly observable, [C] analyst-derived, and [D] analyst interpretation. No [E] external information is introduced. HIGH confidence means the supplied evidence clearly supports the particular statement; it does not certify the authors' broader scientific conclusions. MEDIUM confidence applies to qualified inferences or visual trends. LOW or UNKNOWN applies where necessary information is absent or ambiguous. All page locators below are physical PDF pages, not proceedings page numbers; physical pages 2–18 carry printed pages 1831–1847.

# 1. Plain-language orientation

This paper studies what happens when an application asks a large language model, or LLM, to process material supplied by someone else. The intended instruction might be to summarize a webpage, screen a résumé, or classify a message. An attacker places a competing instruction inside that material. If the model follows the embedded instruction, the application performs the attacker's task rather than the user's task. The authors call this a prompt injection attack.

The central security problem is the boundary between instructions and data. The application legitimately needs to read external content, but the content may contain language that looks like a command. The paper's résumé example makes this concrete: an applicant adds text telling the model to print an affirmative answer, potentially defeating automated qualification screening. A footnote observes that white text on a white background could be invisible to a human while still appearing in PDF-to-text conversion. This is a supplied example, not an experimentally measured attack in the benchmark (p. 2).

The researchers formalize the attack as replacing legitimate task data with compromised data assembled from the original data, an injected instruction, and injected data. They compare five attacks, including a Combined Attack that joins three existing strategies. Their experimental program covers ten LLMs and seven language tasks, and evaluates five prevention defenses and five detection defenses (pp. 2–3, 5–9).

The strongest average attack in the displayed GPT-4 comparison is Combined Attack: its average Attack Success Value, or ASV, is 0.75 across 49 target/injected task combinations, compared with 0.62 for Naive Attack. The corresponding PaLM 2 averages are 0.71 and 0.62. Across ten LLMs and the 49 combinations, the authors report Combined Attack averages of 0.62 ASV and 0.78 Matching Rate, or MR. These are task-score averages, not a universal probability that any deployed agent will be compromised (pp. 10, 17).

Their defense findings emphasize tradeoffs. Some defenses reduce attack scores but damage legitimate task performance. Some detectors miss attacks; others reject large amounts of clean content. Known-answer detection performs well against Combined Attack in these experiments but is bypassed by other constructions in several conditions (pp. 11–14).

Relevance to the research question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', is [D] analyst inference. The paper identifies externally sourced data, including webpages, as an attacker-controlled entry point into LLM-integrated applications. It does not directly compare web agents against standalone LLMs, measure browsing or tool-use risk, or establish a numerical vulnerability difference between those populations.

# 2. Document roadmap

The original title is **Formalizing and Benchmarking Prompt Injection Attacks and Defenses**. Authors are Yupei Liu, Yuqi Jia, Runpeng Geng, Jinyuan Jia, and Neil Zhenqiang Gong. The supplied affiliations are The Pennsylvania State University and Duke University. The proceedings cover identifies the 33rd USENIX Security Symposium, August 14–16, 2024, Philadelphia, Pennsylvania, USA (pp. 1–2). This is a mixed security, AI, formalization, and empirical benchmark paper.

The document inventory provides the denominator for the final audit:

| ID | Original item | Physical pages | Function |
|---|---|---|---|
| FRONT | Cover, title, authors, affiliations, abstract | 1–2 | Publication identity and overview |
| S1 | §1 Introduction | 2–3 | Motivation, gap, contributions |
| S2 | §2 LLM-Integrated Applications | 3–4 | Application and prompt model |
| S3 | §3 Threat Model | 4 | Attacker goal, knowledge, capabilities |
| S4 | §4 Our Attack Framework | 4–6 | Formal attack definition and construction |
| SS4.1 | §4.1 Defining Prompt Injection Attacks | 4–5 | Target/injected tasks; Definition 1 |
| SS4.2 | §4.2 Formalizing an Attack Framework | 5–6 | General framework and five attacks |
| S5 | §5 Defenses | 6–8 | Prevention/detection taxonomy |
| SS5.1 | §5.1 Prevention-based Defenses | 6–7 | Five prevention methods |
| SS5.2 | §5.2 Detection-based Defenses | 7–8 | Five detection methods |
| S6 | §6 Evaluation | 8–13 | Experimental configuration and results |
| SS6.1 | §6.1 Experimental Setup | 8–9 | Models, datasets, sampling, metrics |
| SS6.2 | §6.2 Benchmarking Attacks | 9–11 | Attack, model, task, demonstration comparisons |
| SS6.3 | §6.3 Benchmarking Defenses | 11–13 | Utility, detection, and bypass results |
| S7 | §7 Related Work | 14 | Scope distinctions and concurrent defenses |
| S8 | §8 Discussion and Limitations | 14 | Heuristics, fine-tuning, recovery, detector scope |
| S9 | §9 Conclusion and Future Work | 14 | Synthesis and proposed directions |
| A1 | Appendix A | 17 | Data splits, labels, overlap precautions |
| REF | Acknowledgements and References [1]–[57] | 15–17 | Funding and cited sources |
| F1–F6 | Figures 1–6 | 3, 10, 10, 12, 15, 18 | Architecture, attack plots, size trend, demonstrations, defense examples |
| T1–T11 | Tables 1–11 | 5, 6, 8, 10, 11, 11, 12, 13, 13, 17, 18 | Methods, models, results, task prompts |
| E1–E6 | Equations (1)–(6) | 5, 9 | Attack construction and evaluation metrics |
| U1–U5 | Five unnumbered attack formulas | 5–6 | Concrete concatenation strategies |
| DEF1 | Definition 1 | 5 | Formal meaning of prompt injection |
| X1–X6 | Six experimental analyses | 9–13, 17–18 | Registered in Section 8 below |

No separate keywords, formal research-question list, named hypotheses, theorem/lemma/proposition sequence, or algorithm pseudocode block is present. The formulas specify constructions rather than optimization algorithms. Tables 12–32 belong to referenced technical report [28], not to the supplied eighteen-page paper.

# 3. Background and context

An LLM is modeled here as a text-to-text neural network: it receives prompt p and produces response f(p), where f denotes the model (p. 3). An **LLM-Integrated Application** surrounds that model with a user-facing service. The service chooses or receives instructions, obtains data, submits both to the model, and returns a possibly post-processed response (pp. 3–4).

The **instruction prompt** specifies the operation. The **data context**, shortened to data, is the material on which the operation should be performed. The paper writes an ordinary request as instruction concatenated with data. In its GPT-4 experiments, however, the instruction and data are also assigned separate API roles: system and user, respectively. The distinction between conceptual concatenation and API packaging matters; these results were not obtained solely by placing everything into one undifferentiated message (pp. 4, 8).

**Target task** means the legitimate operation chosen by the user or application. **Injected task** means the operation chosen by the attacker. These can be different kinds of tasks, such as replacing spam classification with summarization, or the same task type applied to different data, such as replacing classification of a spam message with classification of a non-spam message. Identical task types do not imply identical intended outputs (pp. 4–5, 8).

**In-context learning** means including example inputs and their correct outputs in the instruction prompt. The model is not reported as being retrained for these examples; they are supplied as demonstrations during prompting. The experiment varies their number from zero to five (pp. 4, 11–12).

The authors distinguish injection from **jailbreaking**. Jailbreaking seeks to make an LLM perform a refused, unsafe target task. Injection seeks to make it perform a different, attacker-injected task; that task may be safe or unsafe. Therefore, harmless-looking sentiment analysis can serve as the injected task in a security failure. The failure concerns unauthorized task substitution, not necessarily harmful content generation (p. 14).

**Perplexity**, abbreviated PPL, is used by the evaluated detectors as a model-dependent text-quality signal: high values are treated as evidence of compromised content. This is the defense's rationale, not proof that malicious text must have high perplexity. The authors explain the detectors' poor results by observing that compromised text can remain fluent (pp. 7, 13).

# 4. Research problem and gap

**Existing problem [A].** External content can influence the behavior of an application that relies on an instruction-following LLM. The attacker can exploit an input that the application needs to process, even when the attacker cannot edit the application's legitimate instruction (pp. 2, 4).

**Authors' assessment of previous approaches [A].** Prior research papers and blog posts were largely case studies. According to the authors, they lacked both a framework for formalizing attacks and defenses and a comprehensive evaluation. Consequently, the severity of attacks and effectiveness of defenses were difficult to compare systematically (pp. 2–3).

**Research gap [A].** A reusable definition, construction framework, and quantitative benchmark were needed to compare task substitution across models, task types, attacks, and defenses. This is the authors' characterization of the gap; the supplied paper is not an independent systematic review of all prior literature.

**Motivation [A].** Applications integrate external material such as résumés and webpages into prompts. An adversary who controls that material can potentially induce an attacker-desired response. The introduction also cites application compromises and a security-risk ranking, but those citations were not independently verified here (p. 2).

**Scope.** The benchmark uses language-processing datasets and prompt-level constructions. It does not present a browser-agent implementation, a benchmark of autonomous multi-step workflows, tool execution, or measured exfiltration from a running web agent. Web search and translation are motivating application examples, while the seven evaluated tasks are specified separately (pp. 4, 8).

# 5. Research questions / objectives / hypotheses

The authors do not enumerate formal research questions or hypotheses. Their explicit objectives and contributions can be preserved without inventing such a list:

| Objective ID | Author-stated objective | Evidence used to address it |
|---|---|---|
| O1 | Formalize prompt injection attacks | Definition 1, Equation (1), and task notation |
| O2 | Develop attacks within a general construction framework | Existing attacks represented as special cases; Combined Attack |
| O3 | Quantitatively benchmark attacks | Five attacks, ten LLMs, seven tasks; Tables 4–6 and 10; Figures 2–4 and 6 |
| O4 | Evaluate candidate defenses | Five prevention and five detection defenses; Tables 7–9 |
| O5 | Facilitate further research | Author-reported public platform and suggested future directions |

The claims that larger models are more vulnerable because they follow instructions more effectively, and that sentiment analysis is easier to inject than summarization because it is less challenging, are explicitly expressed as suspicions in the results discussion. They are explanatory conjectures, not preregistered hypotheses tested in isolation (pp. 10–11).

The user's research question about web agents versus standalone LLMs is an additional analytical question. It is not O1–O5 and is not directly tested by the paper. The supported contribution to that question is a mechanism: attacker-controlled external data can become a competing instruction inside an integrated application.

# 6. Assumptions / threat model

The threat model is explicit on page 4 and further delimited on page 14.

**Asset and attacker goal [A].** The application should accomplish the user's target task. The attacker seeks an attacker-desired response, either a limited change, such as spam becoming non-spam, or an arbitrary task replacement, such as a classifier producing a document summary.

**Attacker knowledge [A].** The attacker knows the service is LLM-integrated. Although applications might reveal internal details in general, the benchmark assumes the attacker does not know the instruction prompt, whether in-context examples are used, or which LLM is the backend. These are properties of the modeled attacker; evaluators know the experimental configuration.

**Attacker capabilities [A].** The attacker can inject arbitrary instruction/data into content consumed by the application. Examples include the attacker's résumé, social-media post, or hosted webpage. The attacker cannot manipulate the target instruction, which is determined by the user/application. The backend LLM is assumed to maintain integrity.

**Access assumptions [A].** The benchmarked attacks do not require even black-box access to the victim application while crafting compromised data. This differs from attacks by malicious application users who can repeatedly query a service to extract its private information (p. 14).

**Boundary interpretation [D].** The trusted instruction and intact backend do not eliminate risk if the model treats external data as an instruction. For web-agent research, the relevant additional exposure is the ability of a third party to place text on a resource that the application later reads. The paper demonstrates this class of task-substitution failure in controlled tasks; it does not quantify how often web agents encounter attacker-controlled pages.

**Excluded or unmeasured capabilities.** Direct model-parameter modification and instruction-prompt modification are outside this threat model. Adaptive query-based attack optimization is not used in the evaluated heuristics. Tool permissions, authentication, browser state, and action execution are not specified components of the benchmark, so conclusions about them would exceed the evidence.

# 7. Methodology

## 7.1 Formal construction and attacks

A task consists of an instruction and data. Let t be the target task, s^t its instruction, and x^t its data. Let e be the injected task, s^e its instruction, and x^e its data. The attacker constructs compromised data x̃ = A(x^t, s^e, x^e). The legitimate instruction s^t remains in place. The model is queried with s^t combined with x̃ (pp. 4–5).

The five attacks differ in inserted text and ordering:

| Attack | Construction, using ⊕ for concatenation | Intended mechanism |
|---|---|---|
| Naive Attack | x^t ⊕ s^e ⊕ x^e | Append the injected task directly |
| Escape Characters | x^t ⊕ c ⊕ s^e ⊕ x^e | Special character suggests a context change |
| Context Ignoring | x^t ⊕ i ⊕ s^e ⊕ x^e | Explicitly tell the model to ignore prior instructions |
| Fake Completion | x^t ⊕ r ⊕ s^e ⊕ x^e | Suggest the target task has already been completed |
| Combined Attack | x^t ⊕ c ⊕ r ⊕ c ⊕ i ⊕ s^e ⊕ x^e | Combine separation, fake completion, and context ignoring |

Here c is a special character such as a newline, i is task-ignoring text, and r is a fake response. The experiments use the generic fake response 'Answer: task complete', which avoids needing to know the target task. The two occurrences of c in Combined Attack separate the fake response and task-ignoring text. The formulas describe heuristic assembly, not learned or optimized payload search (pp. 5–6).

## 7.2 Models and execution

Ten backends are listed: GPT-4; PaLM 2 text-bison-001; GPT-3.5-Turbo; Bard; Vicuna-33b-v1.3; Flan-UL2; Vicuna-13b-v1.3; Llama-2-13b-chat; Llama-2-7b-chat; and InternLM-Chat-7B. Table 3 reports parameter counts and providers. These counts are paper-reported metadata, not independently confirmed facts about proprietary models (p. 8).

GPT-4 is the default because the authors report good task performance. They access it through Azure OpenAI Studio and send the target instruction as a system-role message and the data as a user-role message. Open-source model runs fix a random-generator seed; the seed value is not supplied. Closed-source models use temperature 0.1. The authors say nondeterminism has a small impact, but the supplied paper does not show repeated-run uncertainty estimates substantiating that statement (p. 8).

Hardware, runtime, memory, total API cost, exact API snapshot dates, maximum output lengths, and a complete set of generation settings are not supplied. These omissions restrict independent reproduction from the paper alone.

## 7.3 Tasks, datasets, and sampling

| Task | Abbreviation | Dataset | Target/injected source split | Demonstration source split | Task metric |
|---|---|---|---|---|---|
| Duplicate sentence detection | DSD | MRPC | Testing | Training | Accuracy |
| Grammar correction | GC | Jfleg | Validation | Testing | GLEU |
| Hate detection | HD | HSOL | Training | Training, with no overlap | Accuracy |
| Natural language inference | NLI | RTE | Training | Validation | Accuracy |
| Sentiment analysis | SA | SST2 | Validation | Training | Accuracy |
| Spam detection | SD | SMS Spam | Training | Training, with no overlap | Accuracy |
| Text summarization | Summ | Gigaword | Validation | Training | Rouge-1 |

Each of seven tasks can be target or injected, yielding 7 × 7 = 49 combinations [A]. For each task dataset, 100 examples are sampled uniformly without replacement as target data and another 100 as injected data, with no overlap. The Cartesian product has 100 × 100 = 10,000 pairs per combination [A]; the experiments randomly sample 100 pairs for ASV, MR, and FNR to reduce computation cost (pp. 8–9).

When target and injected tasks are the same classification task, examples are selected to have different ground-truth labels. Otherwise a correct-looking output might not reveal which task the model followed. In the same-task spam and hate cases, target content is restricted to spam or hateful examples and injected content to non-spam or non-hateful examples. This makes the tested direction of manipulation especially relevant to evasion, but changes the class distribution relative to unconstrained sampling (pp. 8, 17).

Appendix A specifies label mapping: SST2 0/1 means negative/positive; SMS Spam 0/1 means non-spam/spam; HSOL label 2 is not hateful and other labels are hateful; MRPC 0/1 is not equivalent/equivalent; RTE 0/1 is entailment/not entailment. Jfleg and Gigaword use original reference outputs. Demonstration examples do not overlap sampled target/injected examples. PPL calibration records are also kept separate from target/injected data (p. 17).

## 7.4 Prevention defenses

Paraphrasing asks the backend LLM to paraphrase the data before performing the target task. Retokenization uses BPE-dropout to split rare words into smaller tokens while maintaining frequent words. Delimiters surround data, using three single quotes by default; XML tags and random strings are illustrated but their alternative results are in absent report tables. Sandwich prevention appends a reminder of the target task after the data. Instructional prevention modifies the instruction to resist instructions embedded in data (pp. 6–7).

The rationale is either to disrupt attack structure or reinforce the distinction between instruction and data. No defense is assumed intrinsically safe: legitimate task performance is separately evaluated.

## 7.5 Detection defenses

PPL detection rejects data with perplexity above a threshold. Windowed PPL detection rejects if any contiguous window exceeds a threshold. Naive LLM-based detection asks the backend whether the content should be sent to another AI chatbot; a 'no' response denotes compromised content. Response-based detection checks whether the application output is valid for the target task. Known-answer detection gives a separate instruction to repeat a secret key while ignoring the data; absence of the key denotes compromised content (pp. 7–8).

Known-answer detection uses a seven-random-character key. It tests behavior on its detection instruction, rather than directly verifying whether the original application task will be preserved. That distinction is central to the bypass experiment.

For PPL-based methods, GPT-4 cannot provide the required perplexity in this setup, so Llama-2-13b-chat is used. Each task contributes 100 clean calibration examples, and the threshold is selected for calibration FPR at most 1%. The supplied material does not give actual thresholds or numerical window sizes (pp. 12–13, 17).

## 7.6 Evaluation and statistics

PNA measures task performance without an attack; PNA-T refers to the target task and PNA-I to the injected task. ASV scores attacked outputs against injected-task ground truth. MR scores attacked outputs against the model's output when directly performing the injected task. FPR measures false alarms on clean content; FNR measures missed compromised content. All lie in [0,1] (pp. 8–9).

Five classification tasks use accuracy; grammar correction uses GLEU; summarization uses Rouge-1. GLEU and Rouge-1 implementations, tokenization settings, and response normalization are not detailed. Averaging these different metrics gives a broad benchmark aggregate, not one uniformly interpretable event rate.

The reported statistical association is Pearson correlation between model size and attack metrics: 0.63 for ASV and 0.64 for MR. No confidence intervals, significance tests, repeated-run error bars, or causal design for model size appear in the supplied paper. Graphs show point estimates and trends.

# 8. Experiments / analyses

| ID | Purpose and conditions | Comparisons and outcomes | Caveats |
|---|---|---|---|
| X1 | Compare five attacks across 49 task combinations | GPT-4 Figure 2/Table 4 and PaLM 2 Figure 6/Table 10; ASV | Detailed five-attack grids are displayed for two models, not all ten |
| X2 | Evaluate Combined Attack across ten models | Figure 3, Tables 5–6; ASV, MR, PNA-I | Nine model-specific matrices are only in absent report [28] |
| X3 | Test target-task demonstrations | GPT-4, zero to five examples, Figure 4; ASV | Small graphical changes, no numerical uncertainty estimates |
| X4 | Compare prevention with no defense | GPT-4, Combined Attack, seven target tasks; Table 7 ASV/MR and clean PNA-T | Aggregated across injected tasks; task-specific tradeoffs matter |
| X5 | Compare five detectors | Combined Attack FNR and clean FPR; Table 8 | GPT-4 for three detectors, Llama-2-13b-chat for PPL methods |
| X6 | Probe known-answer bypasses | GPT-4, injected sentiment analysis, four other attacks; Table 9 | ASV/MR conditional on bypass; one detection prompt |

**X1 — Attack strategy comparison.** The manipulated variable is construction strategy; target and injected tasks form the grid. GPT-4 averages are 0.62, 0.66, 0.65, 0.70, and 0.75 for Naive, Escape, Context Ignoring, Fake Completion, and Combined, respectively. PaLM 2 values are 0.62, 0.64, 0.65, 0.66, and 0.71. Combined wins the averages, but the authors explicitly identify exceptions in individual task combinations. For GPT-4, Fake Completion slightly exceeds Combined when target is grammar correction and injected task is duplicate sentence detection (pp. 9–10, 17–18).

**X2 — Model/task breadth.** Combined Attack averages 0.62 ASV and 0.78 MR over ten models and 49 combinations. Table 6 aggregates by target and injected task across models. Target-task ASV ranges from 0.59 to 0.64, while injected-task ASV ranges from 0.34 for summarization to 0.89 for sentiment analysis. The authors infer differing injected-task difficulty as a possible explanation, but do not isolate that mechanism experimentally. Model-size correlations are positive but observational (pp. 10–11).

**X3 — Demonstrations.** Figure 4 varies the number of target-task examples from 0 through 5 for GPT-4. Seven panels correspond to injected tasks; each contains seven target-task curves. Curves remain comparatively flat. The authors conclude examples have a small impact on Combined Attack effectiveness. Exact per-point values are not labelled, so this analysis preserves the reported qualitative conclusion rather than inventing a numerical effect size (pp. 11–12).

**X4 — Prevention/utility.** Table 7a compares attack scores under defenses; Table 7b evaluates clean utility. For duplicate sentence detection, paraphrasing lowers ASV from 0.76 to 0.06 while clean PNA-T changes from 0.73 to 0.77. For grammar correction, the same defense changes clean PNA-T from 0.48 to 0.01. Thus a defense can look effective in an attack average yet be unsuitable for a different legitimate task. Instructional prevention leaves summarization-target ASV at 0.73 compared with 0.75 without defense (p. 12).

**X5 — Detection tradeoffs.** PPL methods often miss nearly all compromised samples. Naive LLM-based detection has FNR 0.00 in every displayed row but clean FPR as high as 0.93 for hate detection and 0.83 for spam detection. Known-answer detection has low FNR against Combined Attack, ranging from 0.00 to 0.12, and FPR 0.00 except hate detection at 0.07. This is strong performance under that particular attack/prompt configuration, not proof of general protection (p. 13).

**X6 — Known-answer failure conditions.** Table 9 fixes injected sentiment analysis and evaluates Naive, Escape, Context Ignoring, and Fake Completion. With grammar correction as target, Context Ignoring has FNR 0.76 and bypass-conditional ASV/MR 0.92/0.93; Fake Completion has FNR 0.86 and conditional ASV/MR 0.88/0.93. Escape Characters has all-zero displayed values across targets. The zero scores when there are no bypasses require care: the paper does not specify a convention for an empty conditional evaluation set (p. 13).

# 9. Results

**Combined Attack improves the displayed averages [A/B].** For GPT-4, it scores 0.75 against Fake Completion's 0.70 and Naive Attack's 0.62. For PaLM 2, it scores 0.71 against 0.66 and 0.62. [C] Analyst-derived absolute differences are 0.75 − 0.62 = 0.13 for GPT-4 and 0.71 − 0.62 = 0.09 for PaLM 2. These are differences in mixed task-score averages; describing them as percentage-point gains in universal attack probability would be misleading (Tables 4 and 10).

**Results extend across task types and models [A].** The ten-model aggregate ASV/MR is 0.62/0.78. Table 6a gives target-task ASV/MR: DSD 0.64/0.80; GC 0.59/0.76; HD 0.63/0.78; NLI 0.64/0.77; SA 0.64/0.80; SD 0.59/0.76; Summ 0.62/0.80. Table 6b gives injected-task values: DSD 0.65/0.75; GC 0.41/0.78; HD 0.70/0.77; NLI 0.69/0.81; SA 0.89/0.90; SD 0.66/0.78; Summ 0.34/0.67 (pp. 10–11).

**ASV and MR answer different questions.** Table 5's GPT-4 grammar-correction injected column has baseline PNA-I 0.54, attack ASV roughly 0.52–0.57, and MR roughly 0.91–0.96. Matching the model's own injected-task response can be strong even when the reference-based score is moderate. Conversely, a binary task can receive a correct injected label without uniquely demonstrating an entire internal task-switching process. The label-selection precautions help distinguish outputs but do not reveal hidden reasoning (pp. 8–11).

**Prevention does not offer a uniformly acceptable tradeoff [A].** Average clean PNA-T changes reported in Table 7b are −0.14 for paraphrasing, −0.06 retokenization, −0.08 delimiters, −0.06 sandwich prevention, and −0.02 instructional prevention. The smallest average utility loss does not identify the strongest attack reduction. For example, instructional prevention leaves summarization-target ASV/MR at 0.73/0.85. Delimiters reduce grammar-correction-target ASV to 0.29 but clean grammar-correction PNA-T becomes 0.00 (p. 12).

**Detection performance depends strongly on method and attack [A/B].** Known-answer detection is strongest against Combined Attack in Table 8, but Table 9 demonstrates failure against other strategies. This reverses a simplistic assumption that success against the strongest average attack implies success against every weaker-average attack. The detection instruction and the application instruction can respond differently to the same payload (p. 13).

**The model-size result is an association [A, qualification D].** Pearson correlations are 0.63 and 0.64. The authors suspect larger models follow injected instructions more effectively. Architecture, provider, training, and parameter counts vary simultaneously, and no intervention isolates size. Therefore the supplied evidence supports positive association in this model collection, not a causal law that increasing parameters necessarily reduces security (p. 10).

# 10. Figure-by-figure interpretation

## Figure 1 — Application and attack data flow

Directly visually inspected on page 3. This is a component diagram, not a statistical plot. The external-resource icon connects to the application through arrow 2, Data. The user optionally supplies an instruction through arrow 1. The application sends Prompt p to the LLM through arrow 3; the LLM returns its response through arrow 4; the application returns a response to the user through arrow 5. A red attacker icon sends red Instruction/data into external resources. Red distinguishes attacker influence from ordinary black information flow. There are no axes, units, numeric outcome values, error bars, or feedback loops. The figure locates the intrusion upstream of prompt assembly and supports the threat model's data-control assumption.

## Figure 2 — Five attack strategies with GPT-4

Directly visually inspected on page 10. Seven grouped-bar panels correspond to injected tasks: (a) DSD, (b) GC, (c) HD, (d) NLI, (e) SA, (f) SD, and (g) Summ. Each x-axis lists the seven target tasks. The y-axis is ASV on a linear 0–1 scale. Blue denotes Naive Attack, orange Escape Characters, green Context Ignoring, red Fake Completion, and purple Combined Attack. Each target category contains five bars; there are no displayed error bars or significance markers.

The visual shows high values in injected NLI and sentiment panels, lower reference scores in injected grammar correction and summarization, and generally strong purple bars. The prose supplies a specific exception: target GC/injected DSD slightly favors Fake Completion. Exact individual bar heights are not labelled; Table 4 supplies exact aggregate values. Differences across panels partly reflect different task metrics, so summarization bars should not be read as binary attack probabilities. Confidence is HIGH for axes/panel meaning and MEDIUM for unlabelled visual comparisons.

## Figure 3 — Combined Attack across models

Directly visually inspected on page 10. Two line series show average ASV and MR across 49 task combinations. The x-axis lists ten models in descending reported size order; it is a categorical axis, not a continuous parameter-count axis. The y-axis is ASV/MR, linear 0–1. The red dashed line is ASV; the blue solid line is MR. MR stays above ASV, GPT-4 appears highest, and the trend generally declines toward smaller models but is not strictly monotonic. No exact point labels, uncertainty bands, or significance markers are displayed. The final axis label uses a variant of the InternLM name. Exact correlations 0.63/0.64 are supplied by nearby prose, not derived from visual coordinates.

## Figure 4 — Number of in-context examples

Directly visually inspected on page 12. Seven line-chart panels again represent injected tasks (a) DSD through (g) Summ. The x-axis is number of target-task in-context examples, integer values 0–5. The y-axis is ASV, linear 0–1. Seven curves represent target tasks, distinguished by colors and line styles. Legends repeat the task names; some small legend details are difficult to resolve, but panel roles and the text explanation are clear.

Curves are nearly horizontal, with small fluctuations. Their vertical levels differ substantially by injected task, while adding target-task demonstrations changes them much less. There are no error bars, point labels, or tests supporting a precise equivalence claim. The supported conclusion is the authors' qualitative finding of a small impact within this zero-to-five range for GPT-4 and Combined Attack.

## Figure 5 — Example prevention prompts

Directly visually inspected on page 15. Five rounded blue boxes show three delimiter variants, sandwich prevention, and instructional prevention. The examples all use summarization as the target task. Delimiter boxes enclose [data] in quotation-style marks, an XML-like tag pair, or a repeated random string. Sandwich prevention places a reminder after the data; instructional prevention places an ignore-embedded-instructions qualifier before it. This is a prompt-layout illustration with no axes or measured outcomes.

There is a source discrepancy: prose calls the default delimiter three single quotes, while the figure's prompt text visibly uses backtick-like marks and its label still says Three single quotes. The extracted XML closing tag is also unconventional. These literal details are reported rather than silently corrected. The figure communicates boundary marking and reminder placement; it does not prove effectiveness. Alternative delimiter performance tables are absent.

## Figure 6 — Five attack strategies with PaLM 2

Directly visually inspected on page 18. The panel organization, target-task categories, five attack colors, and linear ASV scale match Figure 2. Panels (a)–(g) correspond to injected DSD, GC, HD, NLI, SA, SD, and Summ. Combined Attack is generally competitive or strongest, sentiment/NLI injected tasks have high bars, and summarization remains lower. Some grammar-correction conditions show conspicuous separation between attack strategies. Exact bar values are unlabelled; Table 10 gives the aggregate ordering and values. No error bars or statistical markers appear. This provides a second model's detailed comparison, not detailed evidence for all ten backends.

# 11. Table-by-table interpretation

## Table 1 — Attack examples

Page 5; visually inspected. Rows are the five attacks; columns give description and compromised-data example. The caption fixes automated screening, a three-year PyTorch qualification question, résumé data, injected instruction Print, and injected data yes. Every example appends material to the résumé. The table demonstrates construction differences, not measured success. Full repeated résumé prefixes are compressed here because the formulas in Section 7 preserve the substantive differences.

## Table 2 — Defense taxonomy

Page 6; visually inspected. Ten rows are divided into prevention and detection categories. Prevention rows are paraphrasing, retokenization, delimiters, sandwich prevention, and instructional prevention. Detection rows are PPL, windowed PPL, naive LLM-based, response-based, and known-answer. Descriptions state the intended mechanism. Citations identify prior sources without importing their contents. The table supports breadth of evaluated strategies, not a completeness claim about every available defense.

## Table 3 — Models and reported parameter counts

Page 8; visually inspected. Columns are model, number of parameters, and provider. Reported values are GPT-4 1.5T/OpenAI; PaLM 2 text-bison-001 340B/Google; GPT-3.5-Turbo 154B/OpenAI; Bard 137B/Google; Vicuna-33b-v1.3 33B/LM-SYS; Flan-UL-2 20B/Google; Vicuna-13b-v1.3 13B/LM-SYS; Llama-2-13b-chat 13B/Meta; Llama-2-7b-chat 7B/Meta; InternLM-Chat-7B 7B/InternLM. B and T denote billion and trillion in the table's parameter notation. These values underpin Figure 3's ordering. Their accuracy is not independently verified, and uncertainty is not supplied.

## Table 4 — GPT-4 attack averages

Page 10; visually inspected. Five attack columns report ASV averaged over 49 combinations: 0.62, 0.66, 0.65, 0.70, 0.75 in Naive/Escape/Context/Fake/Combined order. Combined is highest; Naive lowest; there are no ties. No uncertainty or significance information accompanies the differences. It is an aggregate over multiple task metrics.

## Table 5 — GPT-4 Combined Attack matrix

Page 11; visually inspected against flattened text. Rows are target tasks and seven column groups are injected tasks. Each group includes baseline PNA-I and attack ASV/MR; PNA-I cells are visually merged across target rows, so missing repeated text is not missing baseline data. Baselines by injected task are DSD 0.77, GC 0.54, HD 0.78, NLI 0.93, SA 0.94, SD 0.96, and Summ 0.41.

Selected exact results preserve the main comparisons and important qualifications. Target DSD/injected DSD gives ASV/MR 0.77/0.78; target DSD/injected GC 0.54/0.96; target DSD/injected NLI 0.95/0.96; target SA/injected SA 0.97/0.97; target NLI/injected SD 0.98/0.96; target GC/injected Summ 0.38/0.76. Across target rows, injected Summ ASV ranges 0.38–0.42 and MR 0.76–0.83, while injected GC ASV ranges 0.52–0.57 and MR 0.91–0.96 [C: ranges selected from the displayed cells].

The table also exposes a qualification to the stated PNA-I upper-bound claim: injected NLI has baseline 0.93 but an ASV cell 0.95; injected SA baseline 0.94 but an ASV cell 0.97; injected SD baseline 0.96 but an ASV cell 0.98. These are different estimated scores and do not establish a strict empirical upper bound. The paper does not reconcile these observations. The full 49-cell ASV/MR matrix is deliberately compressed, with its structure, baselines, representative values, and important exception preserved. Other nine-model matrices are absent report tables.

## Table 6 — Task-wise ten-model aggregates

Page 11; visually inspected. Part (a) rows are target tasks, averaged over seven injected tasks and ten models. Part (b) rows are injected tasks, averaged over seven targets and ten models. Every exact ASV/MR pair is reproduced in Section 9. Target-task averages are comparatively similar; injected sentiment has the highest ASV/MR at 0.89/0.90, summarization the lowest at 0.34/0.67. Target ASV has three-way highest tie DSD/NLI/SA at 0.64 and lowest tie GC/SD at 0.59. No uncertainty estimates are supplied.

## Table 7 — Prevention and clean utility

Page 12; visually inspected. Part (a) has seven target rows and six conditions: no defense plus five prevention defenses, each with ASV/MR averaged over seven injected tasks. Part (b) has clean PNA-T for the same target tasks and defense conditions. The final row is the average change from the no-defense baseline. Lower attack scores and higher clean scores are desirable, making both halves necessary.

Important attack contrasts include DSD paraphrasing 0.06/0.12 versus baseline 0.76/0.88; GC delimiters 0.29/0.30 versus 0.73/0.85; NLI sandwich 0.65/0.76 versus 0.75/0.88; Summ instructional 0.73/0.85 versus 0.75/0.88. Important utility contrasts include GC paraphrasing 0.01 and delimiters 0.00 versus 0.48; SD retokenization 0.71 versus 0.92; HD delimiters/sandwich/instructional each 0.88 versus 0.79; Summ all defense scores 0.22–0.24 versus 0.38. No defense is uniformly best across attack reduction and utility.

The complete clean utility rows are: DSD 0.73/0.77/0.74/0.75/0.77/0.76; GC 0.48/0.01/0.54/0.00/0.53/0.52; HD 0.79/0.50/0.71/0.88/0.88/0.88; NLI 0.86/0.80/0.84/0.85/0.86/0.84; SA 0.96/0.93/0.94/0.92/0.92/0.95; SD 0.92/0.90/0.71/0.92/0.86/0.92; Summ 0.38/0.22/0.22/0.22/0.24/0.23. Order is no defense/paraphrasing/retokenization/delimiters/sandwich/instructional. Remaining attack cells are compressed; no uncertainty or significance marks are displayed.

## Table 8 — Detector errors

Page 13; visually inspected. Part (a) reports Combined Attack FNR averaged over seven injected tasks; part (b) reports clean FPR. The same five method columns appear in both. Lower is better for each, but low FNR alone can be achieved by excessive rejection.

Exact row vectors in method order PPL/windowed PPL/naive LLM/response/known-answer are:

| Target | FNR vector | FPR vector |
|---|---|---|
| DSD | 0.77 / 0.40 / 0.00 / 0.16 / 0.00 | 0.02 / 0.04 / 0.21 / 0.00 / 0.00 |
| GC | 1.00 / 0.99 / 0.00 / 1.00 / 0.12 | 0.00 / 0.00 / 0.23 / 0.00 / 0.00 |
| HD | 1.00 / 0.99 / 0.00 / 0.15 / 0.03 | 0.01 / 0.02 / 0.93 / 0.13 / 0.07 |
| NLI | 0.83 / 0.57 / 0.00 / 0.16 / 0.02 | 0.01 / 0.01 / 0.16 / 0.00 / 0.00 |
| SA | 1.00 / 0.94 / 0.00 / 0.16 / 0.01 | 0.03 / 0.03 / 0.15 / 0.03 / 0.00 |
| SD | 1.00 / 0.99 / 0.00 / 0.17 / 0.05 | 0.02 / 0.02 / 0.83 / 0.06 / 0.00 |
| Summ | 0.97 / 0.75 / 0.00 / 1.00 / 0.03 | 0.02 / 0.02 / 0.38 / 0.00 / 0.00 |

Observed PPL FPR can exceed the 1% calibration target; calibration data and evaluation data are distinct. Thus 1% is a calibration constraint, not a guaranteed test-set ceiling. No sample uncertainty is shown.

## Table 9 — Known-answer bypasses

Page 13; visually inspected. Rows are target tasks; column groups are four attacks. Each group gives ASV, MR, and FNR. GPT-4 and injected sentiment analysis are fixed. ASV/MR use only compromised samples that bypass detection, so these are conditional scores.

Grammar-correction target has Naive 0.75/0.79/0.53, Escape 0.00/0.00/0.00, Context Ignoring 0.92/0.93/0.76, and Fake Completion 0.88/0.93/0.86. Sentiment target has Naive 0.85/0.85/0.13, Context 0.90/0.90/0.77, and Fake 0.85/0.92/0.13. Summarization target has Naive 0.83/0.97/0.29 and Context 0.90/0.95/0.40. DSD rows and all Escape groups display zero triples. Fake Completion under spam target has conditional ASV/MR 1.00/1.00 but FNR 0.07, illustrating why perfect conditional scores do not mean every sample bypasses. Secondary row triples are compressed; empty-bypass zero handling remains unspecified.

## Table 10 — PaLM 2 attack averages

Page 17; visually inspected. Identical aggregation to Table 4 but PaLM 2 backend: Naive 0.62, Escape 0.64, Context 0.65, Fake 0.66, Combined 0.71. Combined highest and Naive lowest. Context slightly exceeds Escape, reversing GPT-4's ordering. No uncertainty estimates or tests accompany the 0.01 difference.

## Table 11 — Task instructions

Page 18; visually inspected. Seven task groups each contain target and injected instruction text. DSD outputs equivalent/not equivalent; NLI entailment/not entailment; sentiment positive/negative; hate yes/no; spam spam/not spam. Grammar correction requests correcting grammatical errors while preserving text structure. Summarization requests a short summary of no more than ten words. Target and injected instructions generally paraphrase the same operation; the attacked data and task placement cause the substitution. The full repeated prompt wording is compressed, while output vocabularies and the ten-word constraint are preserved.

# 12. Diagram / architecture interpretation

Figure 1's architecture contains four normal components: user, application, external resources, and backend LLM. The attacker is an additional influence on resources, not a legitimate recipient in the normal response path. The application mediates both user control and data acquisition. Its outgoing prompt joins those sources before inference; its incoming model response is then delivered to the user (pp. 3–4).

The important sequence is: user defines a task; external data is obtained; application assembles the prompt; backend performs inference; application returns the result. Attacker insertion occurs before the external data reaches prompt assembly. The diagram does not include a detector, recovery stage, explicit permission check, or multiple autonomous iterations.

[D] For the web-agent research question, the diagram supports a trust-boundary explanation: visiting or reading externally authored material supplies another party with influence over model input, even if that party cannot edit the user's request. It does not itself demonstrate additional attack consequences from an agent's tools or autonomy. Figure 5 supplies layouts for possible prompt-level prevention, not a redesigned application architecture or guaranteed enforcement boundary.

# 13. Equations and mathematical concepts

Notation is normalized from the visual equations because extracted text repeats bold letters and replaces the concatenation symbol with control-like characters. Here ⊕ means string concatenation, not addition or exclusive-or. |D| denotes number of examples; sums range over dataset examples or pairs. The notation below preserves equation identity while using readable variables.

**Definition 1, page 5.** Given an application with target instruction s^t and target data x^t, prompt injection modifies x^t so that the application accomplishes an injected task instead of the target task. This is a behavioral definition. It imposes no requirement that the injected task be unsafe, and supplies no theorem guaranteeing that any construction succeeds.

**Equation (1), page 5: x̃ = A(x^t, s^e, x^e).** This is a data-construction function. Inputs are original target data, injected instruction, and injected data. Output is compromised data. The target instruction is not an attack-function input in this formulation, consistent with unknown internal instructions. Applying f to s^t ⊕ x̃ produces the attacked response. The equation organizes possible attacks rather than optimizing them.

**Unnumbered constructions, pages 5–6.** U1–U5 are the five formulas in Section 7. Naive appends the injected instruction/data. Escape inserts c; Context inserts i; Fake inserts r; Combined inserts c, r, c, and i in that order. These are string-valued expressions. c, i, and r are supplied attack components, not probabilities or learned parameters. Their placement explains Table 1's examples and the independent variable in X1.

**Equation (2), page 9: PNA = (1/|D|) Σ_(x,y)∈D M[f(s ⊕ x), y].** This arithmetic average evaluates normal task outputs against reference labels or texts. D is the relevant example set, s the task instruction, x input data, y reference output, and M the task's scoring function. Output is average task score in [0,1]. With s=s^t and D=D^t it is PNA-T; with s=s^e and D=D^e it is PNA-I. PNA-T measures whether a defense damages ordinary utility, and PNA-I checks the model's baseline ability to perform an injected task directly.

**Equation (3), page 9: ASV = (1/(|D^t||D^e|)) Σ_((x^t,y^t),(x^e,y^e)) M^e[f(s^t ⊕ A(x^t,s^e,x^e)), y^e].** This averages attacked output quality relative to the injected task's reference. M^e is the injected-task score. y^t is part of the paired target example but is not the comparison reference in this formula. Higher scores mean stronger attacker-task performance. The theoretical sum covers the product of sets; implementation estimates it with 100 sampled pairs rather than all 10,000. For classification it is a fraction of correct injected labels; for generative tasks it is an average overlap/quality score.

**Equation (4), page 9: MR = (1/(|D^t||D^e|)) Σ M^e[f(s^t ⊕ A(x^t,s^e,x^e)), f(s^e ⊕ x^e)].** The construction matches Equation (3), but the reference is the model's own direct response to the injected task, not ground truth. For classification this is response agreement; for grammar correction and summarization it is scored similarity. It helps detect task following even when direct task quality is limited. It does not validate the correctness of the direct response. Again, the empirical implementation uses 100 sampled pairs.

**Equation (5), page 9: FPR = (1/|D^t|) Σ_(x^t,y^t)∈D^t h(x^t).** h returns 1 when the detector calls data compromised and 0 otherwise. Inputs are clean target examples; output is the fraction incorrectly rejected. Lower is better. A clean spam or hateful example can legitimately be part of this evaluation: compromised status concerns injected task instructions, not merely the subject matter or target label.

**Equation (6), page 9: FNR = 1 − (1/(|D^t||D^e|)) Σ h(A(x^t,s^e,x^e)).** The sum measures detected compromised pairs; subtracting from one gives the missed fraction. Lower is better. It does not measure whether a missed sample actually succeeds at task substitution; Table 9 separately scores bypassed samples. Empirical FNR uses 100 sampled pairs.

The authors state that PNA-I would upper-bound ASV, but neither the formulas nor finite-sample estimates enforce that inequality. Table 5 shows some ASV cells above their displayed PNA-I baseline. This analysis reports the statement and conflicting observations without replacing them with an invented proof or explanation. No optimization objective, loss minimization, theorem, or proof is supplied.

# 14. Interpretation and discussion

The results address O1–O4 through a connected chain: the definition identifies unauthorized task substitution; the framework makes constructions comparable; the benchmark shows substantial injected-task performance across configurations; and the defense experiments show that reducing one error measure is insufficient. O5 is supported by an availability statement, but the platform itself was not inspected.

The paper's distinction between prevention and detection is substantive. Prevention should preserve legitimate task completion despite compromised data. Detection only identifies suspect content. A detector with low FNR can still be operationally poor if it rejects much clean content, while a preprocessing defense can reduce ASV by destroying text needed for the original task. Tables 7 and 8 make these tradeoffs visible.

Known-answer detection reveals a second boundary problem: obedience to an auxiliary test instruction is not equivalent to obedience to the application's actual instruction. The paper reports payloads that leave the detection prompt intact, allowing the secret key to be produced, yet redirect the application. Thus one test of instruction adherence can be an incomplete proxy for another (p. 13).

For web-agent vulnerability, [D] the supported explanation is that integration supplies a route from third-party content to model behavior. The attacker need not be the authorized user. A standalone model considered without such ingestion has no corresponding attacker-controlled resource in this paper's architecture. However, that is an architectural comparison inferred by the analyst, not a measured comparison in the study. Standalone LLMs are the computational backends in the benchmark; the paper does not establish that they are intrinsically immune to injection or quantify a relative risk ratio.

Source consistency checks identify several unresolved points. First, the PNA-I upper-bound statement conflicts with larger ASV cells in Table 5. Second, retokenization is described in §5.1 as splitting tokens with BPE-dropout, while §6.3 describes randomly dropping tokens; these are different descriptions and cannot be reconciled without implementation evidence. Third, default delimiters are described as single quotes while Figure 5 displays backtick-like characters. Fourth, 1% calibration FPR and larger evaluated PPL FPR are not necessarily contradictory because different records are used. Fifth, spam output wording varies between non-spam and not spam across prose, appendix, and prompts, and exact response normalization is unspecified. References [6] and [7] also show mismatches between their 7B/13B labels and displayed URLs; this does not change the named models but weakens citation precision.

# 15. Contributions and novelty

**Conceptual contribution [A].** A formal definition frames injection as target-data modification causing an attacker-selected task to replace the legitimate task. This extends beyond simply seeking a wrong classification label.

**Methodological contribution [A].** A(x^t,s^e,x^e) provides a common representation for attack construction and links it to metrics for injected-task performance and model-response matching.

**Attack contribution [A].** Combined Attack joins escape characters, fake completion, and context ignoring. It is a simple heuristic composition; the novelty claim should not be inflated into a new learned optimization method.

**Benchmark and empirical contribution [A].** The authors evaluate five attacks, ten models, seven tasks, and ten candidate defenses. The supplied main paper displays detailed five-attack comparisons for GPT-4 and PaLM 2, aggregated ten-model results, and default-model defense analyses.

**Implementation contribution [A].** The authors report an open-source platform, Open-Prompt-Injection. Availability is author-reported; installation, tests, code correctness, and current access were not checked.

No new pretraining dataset, trained foundation model, formal security guarantee, browser-agent system, or theorem is claimed in the supplied contribution list. The benchmark samples established language datasets. The authors call their framework the first such formalization; that priority claim is retained as their claim, not independently validated against the external literature.

# 16. Limitations

## Authors' stated limitations

The following are explicitly acknowledged or delimited in the supplied text:

- The evaluated constructions are heuristic; optimization-based attacks remain future work (§8, p. 14).
- Experiments use standard LLMs; security fine-tuning is not evaluated as part of this study (§8, p. 14).
- Fine-tuning against known attacks may leave vulnerability to attacks absent from that training data (§8, p. 14).
- Known-answer detection evaluation uses a specific detection prompt; other prompts and adaptive attacks remain open (§8, p. 14).
- Detection without recovery can prevent the target task from being completed, creating denial-of-service consequences (§8, p. 14).
- Concurrent defenses, including task-specific fine-tuning approaches, are discussed but not evaluated (§7, p. 14).
- Response-based detection fails when target/injected tasks share a type and when valid outputs are difficult to check (§5.2 and §6.3, pp. 8, 13).
- Black-box GPT-4 cannot supply perplexity for the implemented PPL detector evaluation, requiring a different model (pp. 12–13).
- Pair sampling is reduced to 100 to save computation cost (§6.1, p. 9).

The paper's conclusion that existing defenses are insufficient must therefore be interpreted as referring to the evaluated candidate defenses and reported conditions, rather than every possible defense.

## Additional evidence-based analyst observations

[D] The study does not directly establish comparative vulnerability of web agents and standalone LLMs. It does not evaluate live browsing, multi-step agent planning, external actions, tool permission boundaries, or resource encounter frequencies.

[D] Seven language tasks provide controlled breadth but are not a census of deployed application workflows. Label restrictions in same-task experiments deliberately select consequential evasion directions and affect generalization to natural class distributions.

[D] Aggregate ASV combines accuracy, GLEU, and Rouge-1, which measure different constructs. A single mean therefore provides comparative benchmark utility but lacks one universal probability interpretation.

[D] The supplied paper omits uncertainty intervals, seed values, actual PPL thresholds/window lengths, complete API settings, and exact output-normalization logic. These gaps limit confidence about small differences and exact independent reproduction.

[D] Proprietary model parameter metadata and cross-model training differences complicate model-size interpretation. The supplied study does not identify a causal size effect.

[D] Missing technical-report tables limit verification of nine model-specific matrices and detailed per-combination defense outcomes. Author-reported aggregates remain accessible, but their underlying cells are not all available.

# 17. Threats to validity

The categories below are analyst-organized [D]; they should not be mistaken for headings the authors used.

**Internal validity.** Controlled payload formulas and disjoint target/injected samples help attribute output differences to attack placement. However, response parsing is underspecified, and nondeterminism is not quantified through visible repeated-run results. Different detector backends also mean detector comparisons include model differences as well as method differences.

**Construct validity.** ASV measures injected-task performance, while MR measures similarity to a directly prompted injected response. Neither is a comprehensive measure of end-to-end security harm. Known-answer detection measures a proxy behavior, and its bypasses demonstrate that the proxy can disagree with the behavior of interest. Mixed-task aggregates combine different scoring systems.

**External validity and generalizability.** Ten named models and seven tasks broaden coverage, but the configuration uses specific model versions and prompt templates. The paper does not test every deployment, every language, a live web distribution, or every adversarial objective. The reported heuristic attacks do not require victim queries, whereas adaptive adversaries may operate differently.

**Statistical conclusion validity.** One hundred sampled pairs per score and no displayed confidence intervals make small differences difficult to assess. Averaging across combinations also hides individual failures and improvements. Reported correlations have no supplied significance or uncertainty estimates and should remain associations.

**Ecological validity.** Résumé and webpage examples connect the threat model to practical input channels, but experiments use established NLP datasets. Browser state, access control, external-tool consequences, and long interaction trajectories are not measured.

**Reproducibility.** Dataset splits, task prompts, overlap precautions, model names, temperature, and formulas are useful. Missing implementation details and absent extended tables prevent full reconstruction solely from these pages. An author-reported repository may help in principle, but it was not reviewed here.

# 18. Future work and open questions

## A. Explicit author-proposed future work

The authors propose optimization-based construction of compromised data, including optimizing special characters, task-ignoring text, or fake responses. They suggest studying security fine-tuning, training on target instructions paired with compromised data, and task-specific models that do not follow arbitrary instructions. They warn that unseen attacks may remain effective (p. 14).

They also propose recovery mechanisms that reconstruct clean data after detection, additional prevention and detection defenses, alternative known-answer prompts, and adaptive attacks against a detector if a more generally effective detection instruction is found. These are proposed directions, not demonstrated results.

## B. Additional open questions from this analysis

[D] How much does external-resource ingestion change vulnerability relative to a comparable standalone interaction when model, task, prompt, and attacker knowledge are held constant? This would directly address the user's comparative research question, but the present paper does not perform that experiment.

[D] Which parts of a web-agent workflow amplify the task-substitution mechanism shown here: resource selection, repeated reads, state accumulation, or action execution? The supplied evidence does not answer those questions.

[D] Can a detector distinguish benign task-like language from competing instructions without rejecting legitimate spam/hate examples or rewriting away needed task information? Tables 7–9 show why this is a substantive problem.

[D] How stable are the displayed rankings under repeated pair sampling, alternative prompts, other known-answer tests, and accurately documented model configurations? Addressing these uncertainties would strengthen conclusions about small score gaps and generalization.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model; the paper's text-input/text-output backend |
| LLM-Integrated Application | A service that combines task instructions and data and uses an LLM to return a result |
| Prompt | Input text or instruction-plus-data sent to the LLM; usage depends on context |
| Instruction prompt | The legitimate description of what the model should do |
| Data context | Material the model should analyze, rather than obey as a new task |
| Prompt injection | Modification of task data intended to redirect the application to an attacker-chosen task |
| Target task t | The user's legitimate task |
| Injected task e | The attacker's substituted task |
| s^t, x^t | Target instruction and target data |
| s^e, x^e | Injected instruction and injected data |
| x̃ | Compromised data after attack construction |
| A | Function/strategy that constructs compromised data |
| f, p, f(p) | LLM, its input prompt, and its output response |
| ⊕ | Concatenation: putting strings next to one another |
| c, i, r | Special character, task-ignoring text, and fake response |
| D^t, D^e | Sets of target-task and injected-task examples |
| x, y | Example text and ground-truth label/reference |
| M, M^e | Task scoring function; superscript e selects the injected-task metric |
| PNA | Performance under No Attacks |
| PNA-T / PNA-I | No-attack performance on target/injected tasks |
| ASV | Attack Success Value; attacked output scored against injected-task reference |
| MR | Matching Rate; attacked output scored against direct injected-task response |
| h | Detector returning 1 for compromised and 0 for clean |
| FPR | False Positive Rate; clean inputs incorrectly flagged |
| FNR | False Negative Rate; compromised inputs incorrectly accepted |
| PPL | Perplexity; model-dependent signal used by two detectors |
| BPE-dropout | Retokenization technique described as splitting rare words into smaller tokens |
| In-context examples | Demonstrations included in the prompt, without reported model retraining |
| GLEU / Rouge-1 | Named grammar-correction and summarization metrics; detailed algorithms are not defined in the paper |
| Black-box access | Ability to query a system without access to its internals |
| Denial-of-service | Failure to provide the legitimate service; here detection without usable recovered data can leave the task uncompleted |

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Evaluated attack strategies | 5 | strategies | Four prior constructions plus Combined | Author-reported | p. 2 abstract |
| Candidate defenses | 10 | defenses | Five prevention, five detection | Author-reported | pp. 3, 6 T2 |
| Evaluated models | 10 | LLMs | Named backends in T3 | Author-reported | p. 8 |
| Evaluated task types | 7 | tasks | DSD, GC, HD, NLI, SA, SD, Summ | Author-reported | p. 8 |
| Target/injected combinations | 49 | combinations | 7 × 7 | Author-reported | p. 8 |
| Examples selected | 100 + 100 | examples/task | Disjoint target and injected pools | Author-reported | p. 8 |
| Candidate pairs | 10,000 | pairs/combination | Product of the two pools | Author-reported | p. 9 |
| Pairs evaluated for ASV/MR/FNR | 100 | sampled pairs | Computation-saving estimate | Author-reported | p. 9 |
| Closed-model temperature | 0.1 | generation setting | Closed-source backends | Author-reported | p. 8 |
| Known-answer key length | 7 | random characters | Specific evaluated detector | Author-reported | p. 8 |
| PPL calibration data | 100 | clean examples/task | Separate calibration pool | Author-reported | p. 13 |
| Calibration FPR ceiling | 1% | fraction constraint | Calibration, not guarantee on evaluation set | Author-reported | p. 13 |
| GPT-4 five-attack ASV | 0.62 / 0.66 / 0.65 / 0.70 / 0.75 | average task score | Naive/Escape/Context/Fake/Combined over 49 combinations | Visually readable | p. 10 T4 |
| PaLM 2 five-attack ASV | 0.62 / 0.64 / 0.65 / 0.66 / 0.71 | average task score | Same ordering and aggregation | Visually readable | p. 17 T10 |
| Combined ten-model average | 0.62 ASV; 0.78 MR | average scores | Ten LLMs and 49 combinations | Author-reported | p. 10 |
| Size correlation | 0.63 ASV; 0.64 MR | Pearson coefficient | Ten-model association | Author-reported | p. 10 |
| Injected sentiment average | 0.89 ASV; 0.90 MR | average scores | Combined, ten models, seven targets | Visually readable | p. 11 T6b |
| Injected summarization average | 0.34 ASV; 0.67 MR | average scores | Same aggregation | Visually readable | p. 11 T6b |
| Paraphrasing clean utility change | −0.14 | average score difference | Seven GPT-4 target tasks | Author-reported | pp. 11–12 T7b |
| Grammar correction utility | 0.48 → 0.01 | GLEU-based PNA-T | No defense → paraphrasing | Visually readable | p. 12 T7b |
| Grammar correction utility | 0.48 → 0.00 | GLEU-based PNA-T | No defense → delimiters | Visually readable | p. 12 T7b |
| Summarization utility | 0.38 → 0.24 | Rouge-1-based PNA-T | No defense → sandwich | Author-reported | pp. 11–12 |
| Naive detector HD FPR | 0.93 | false-positive fraction | Clean hate-task data, GPT-4 detector | Visually readable | p. 13 T8b |
| Naive detector SD FPR | 0.83 | false-positive fraction | Clean spam-task data, GPT-4 detector | Visually readable | p. 13 T8b |
| Known-answer GC FNR | 0.12 | missed fraction | Combined averaged over injected tasks | Visually readable | p. 13 T8a |
| Known-answer GC/Fake FNR | 0.86 | missed fraction | Injected sentiment, GPT-4 | Visually readable | p. 13 T9 |
| Bypass-conditional GC/Fake scores | 0.88 ASV; 0.93 MR | conditional scores | Only bypassed samples | Visually readable | p. 13 T9 |
| GPT-4 Combined minus Naive | 0.13 | absolute score difference | 0.75 − 0.62 | Analyst-derived | p. 10 T4 |
| PaLM 2 Combined minus Naive | 0.09 | absolute score difference | 0.71 − 0.62 | Analyst-derived | p. 17 T10 |

No approximate graphical values are placed in this numerical reference table. All exact values come from readable tables or explicit prose; derived differences show their operands.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External data provides an injection entry point | Threat model allows arbitrary instruction/data insertion into resources | F1, threat model | pp. 3–4 | HIGH for modeled capability; not encounter prevalence |
| Formal framework represents existing attacks | x̃=A(x^t,s^e,x^e) and five constructions | E1, T1, U1–U5 | pp. 5–6 | HIGH; priority claim not independently checked |
| Combined has highest displayed average ASV | GPT-4 0.75; PaLM 2 0.71 | T4/T10, X1 | pp. 10, 17 | HIGH; individual exceptions exist |
| Combined transfers across model/task conditions | Author-reported ten-model mean 0.62/0.78 | F3, T5/T6, X2 | pp. 10–11 | HIGH for report; underlying nine matrices absent |
| Larger reported models show higher average vulnerability | Correlations 0.63/0.64 | F3, X2 | p. 10 | HIGH for reported association; causal explanation tentative |
| Target demonstrations offer little protection here | Mostly flat 0–5 example curves | F4, X3 | pp. 11–12 | MEDIUM for size of effect; no uncertainty tests |
| Prevention has security/utility tradeoffs | Reduced ASV alongside clean-score losses | T7, X4 | pp. 11–12 | HIGH within GPT-4/Combined setup |
| Naive detector rejects much legitimate material | HD FPR 0.93; SD FPR 0.83 despite zero displayed FNR | T8, X5 | p. 13 | HIGH; content and prompt dependent |
| Known-answer protection is attack-dependent | Low Combined FNR but GC/Fake FNR 0.86 | T8/T9, X5/X6 | p. 13 | HIGH; specific detection prompt |
| Known-answer findings have limited prompt scope | Authors explicitly acknowledge one detection prompt | §8 | p. 14 | HIGH |
| Web-agent relevance is an external-content trust-boundary mechanism | Hosted webpages can carry injected instructions | F1, §3 | pp. 3–4 | MEDIUM analyst inference; no standalone comparison |
| General defense sufficiency is not established | Concurrent defenses not evaluated; recovery unresolved | §§7–9 | p. 14 | HIGH for stated exclusions; broad extrapolation unwarranted |

# 22. Very simple explanation

Imagine asking an assistant to read a résumé and answer whether the applicant qualifies. The résumé contains a sentence saying, in effect, 'Your earlier job is finished; do this other job instead.' The résumé is supposed to be evidence, but the assistant may treat part of it as an instruction. That is the failure this paper studies.

The researchers made a precise way to describe the user's job, the attacker's job, and the text that tries to switch between them. They tested five ways of arranging that text. Combining several tricks usually worked best on average, though not in every individual case. Their tests use ordinary language tasks and several models; the scores depend on which task and metric are being used.

Defenses had tradeoffs. Rewriting the input sometimes weakened the attack but also ruined information needed for the real job. Asking a model to detect suspicious input sometimes made it reject harmless input too. A test that asks the model to repeat a secret key worked against some attacks but missed others, because passing that test did not guarantee the model would obey the real application's instruction.

For a web agent, the relevant lesson is that somebody else's webpage can become part of the agent's input. That gives the page author a route to influence the model. This is an analyst inference from the paper's application model. The paper does not run a direct contest showing that web agents are a particular amount more vulnerable than standalone LLMs, and it does not measure browsing tools or autonomous actions.

# Completeness Audit

The inventory was checked against the supplied text, visible objects, and analysis above. Coverage refers to the supplied work, not absent extended artifacts. Repeated results are compressed openly rather than presented as a complete cell-by-cell transcription.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| FRONT: title/authors/venue/abstract | Yes, text and images | Yes | Fully represented | Decorative cover artwork omitted |
| S1 §1 Introduction | Yes, text and images | Yes | Represented in compressed form | Motivation, gap, résumé example, footnote, contributions |
| S2 §2 Applications | Yes; p. 4 text only | Yes | Fully represented substantively | Instruction/data, response flow, demonstrations |
| S3 §3 Threat Model | Yes, text only | Yes | Fully represented | Goal, unknown internals, content control, intact backend |
| SS4.1 target/injected tasks and DEF1 | Yes | Yes | Fully represented | Definition and task relationship |
| SS4.2 general framework | Yes | Yes | Fully represented | E1 and all constructions |
| SS5.1 prevention methods | Yes | Yes | Fully represented substantively | Retokenization inconsistency disclosed |
| SS5.2 detection methods | Yes | Yes | Fully represented substantively | Prompts compressed; key and thresholds retained |
| SS6.1 setup | Yes | Yes | Fully represented substantively | Missing execution settings explicitly identified |
| SS6.2 attack results | Yes | Yes | Represented in compressed form | Full repeated matrix values not transcribed |
| SS6.3 defense results | Yes | Yes | Represented in compressed form | Key conditions and tradeoffs retained |
| S7 related work | Yes, text only | Yes | Represented in compressed form | Malicious-user scope, concurrent defenses, jailbreak distinction |
| S8 limitations/discussion | Yes, text only | Yes | Fully represented substantively | Four discussion topics and caveats |
| S9 conclusion/future work | Yes, text only | Yes | Fully represented substantively | Claims kept within evaluated scope |
| Explicit research questions | Checked | Yes, absence recorded | Fully represented | Objectives used without inventing RQs |
| Explicit hypotheses | Checked | Yes, absence recorded | Fully represented | Authors' suspicions distinguished |
| X1 attack comparison | Yes | Yes | Fully represented substantively | Two displayed model grids |
| X2 model/task breadth | Yes | Yes | Represented in compressed form | Missing extended matrices flagged |
| X3 demonstrations | Yes | Yes | Fully represented substantively | Exact line values unavailable |
| X4 prevention/utility | Yes | Yes | Represented in compressed form | Selected attack cells; all clean rows retained |
| X5 detector comparison | Yes | Yes | Fully represented | All T8 row vectors retained |
| X6 known-answer bypass | Yes | Yes | Represented in compressed form | Conditional denominator and zero ambiguity retained |
| F1 architecture | Yes, visually | Yes | Fully represented | Every numbered arrow and attacker path |
| F2 panels a–g | Yes, visually | Yes | Represented in compressed form | Shared axes/legend and panel distinctions; no guessed exact bars |
| F3 model lines | Yes, visually | Yes | Fully represented substantively | Categorical size order and correlation caveat |
| F4 panels a–g | Yes, visually | Yes | Represented in compressed form | All injected panel roles; curves compressed |
| F5 five prompt boxes | Yes, visually | Yes | Fully represented substantively | Quote/backtick discrepancy noted |
| F6 panels a–g | Yes, visually | Yes | Represented in compressed form | Shared encoding and model distinction |
| T1 attack examples | Yes, visually | Yes | Represented in compressed form | Repeated résumé strings omitted |
| T2 defense taxonomy | Yes, visually | Yes | Fully represented | All ten methods |
| T3 model metadata | Yes, visually | Yes | Fully represented | Counts attributed to paper |
| T4 GPT-4 averages | Yes, visually | Yes | Fully represented | All five values |
| T5 GPT-4 task matrix | Yes, visually | Yes | Represented in compressed form | Baselines, examples, ranges, upper-bound discrepancy |
| T6a/b task aggregates | Yes, visually | Yes | Fully represented | Every ASV/MR pair |
| T7a/b prevention | Yes, visually | Yes | Represented in compressed form | All clean utility rows; selected attack cells |
| T8a/b detection | Yes, visually | Yes | Fully represented | All error-rate vectors |
| T9 bypass matrix | Yes, visually | Yes | Represented in compressed form | Secondary triples omitted openly |
| T10 PaLM 2 averages | Yes, visually | Yes | Fully represented | All five values |
| T11 task prompts | Yes, visually | Yes | Represented in compressed form | Output labels, task operations, ten-word limit |
| E1 general attack | Yes, visually | Yes | Fully represented | Inputs/output and scope |
| E2 PNA | Yes, visually | Yes | Fully represented | Both baseline meanings |
| E3 ASV | Yes, visually | Yes | Fully represented | Population formula versus sampled estimator |
| E4 MR | Yes, visually | Yes | Fully represented | Own-response comparison |
| E5 FPR | Yes, visually | Yes | Fully represented | Clean false alarms |
| E6 FNR | Yes, visually | Yes | Fully represented | Missed compromised inputs |
| U1–U5 constructions | Yes, visually | Yes | Fully represented | All five string formulas |
| Algorithms/pseudocode | Checked | Absence recorded | Fully represented | No separate blocks supplied |
| Theorems/lemmas/proofs | Checked | Absence recorded | Fully represented | Definition is not a theorem |
| Major contributions O1–O5 | Yes | Yes | Fully represented | Availability separated from code inspection |
| Author-stated limitations | Yes | Yes | Fully represented substantively | Separated from analyst observations |
| A1 Appendix A | Yes, text and image | Yes | Fully represented substantively | Splits, mappings, restrictions, overlap precautions |
| Acknowledgements | Yes | Yes | Inspected but compressed as secondary | NSF/ARO support and Azure credits; grant numbers not repeated |
| References [1]–[57] | Yes; p. 16 text only | Yes | Represented in compressed form | Relevant categories and [28] dependency; no citation verification |
| Separate supplementary material | Not supplied | Absence recorded | Missing from supplied material | Technical-report tables and code not reviewed |

## Missing or inaccessible material

The extended technical report [28] is not supplied as a separate artifact. Its Tables 12–20 contain nine additional model-specific matrices; Tables 21–27 contain detailed prevention results, including alternative delimiter results; Tables 28–32 contain detailed detection results. Statements about these tables are references made by the main paper, not claims of having inspected them. The public platform is likewise referenced but unreviewed. Pages 4, 14, and 16 have supplied text but no displayed image, so their layouts have text-only coverage. No essential supplied page is missing.

## Uncertain interpretations

Exact bar/line coordinates in Figures 2, 3, 4, and 6 are not labelled and are not promoted to exact results. Tiny legend style details are less certain than caption-defined series roles. The default delimiter's literal characters differ between prose and Figure 5. Retokenization has inconsistent descriptions. PNA-I is described as an upper bound despite higher Table 5 ASV estimates. Table 9 does not define how conditional scores are handled when no samples bypass. Response normalization for alternative label wordings, actual PPL thresholds/window sizes, and full generation settings are unspecified. None of these points was silently repaired.

## Deliberately compressed material

The full Table 5 and Table 9 cell matrices, remaining Table 7a cells, all individual graph heights, repeated task-prompt wording, repeated attack-example prefixes, and full reference/funding transcription are compressed. Their structures, experimental conditions, main results, exceptions, and consequential caveats are represented. Decorative red cover graphics, page furniture, and author contact emails are accounted for as non-substantive to the research analysis.

## Potential omissions

Every substantive inventory object is represented either directly, in disclosed compressed form, or as unavailable/uncertain. This is not a claim that every number or every sentence has been reproduced. In particular, secondary matrix cells and literal prompt wording are intentionally not all repeated, and absent extended results cannot be assessed. The analysis supports an external-content mechanism relevant to web-agent security while leaving the user's direct comparative question unresolved by this paper's experimental design.
