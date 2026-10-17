## Stage 0 — Document Accessibility Report

The supplied main document consists of extracted text for physical PDF pages 1–14 and directly visible renderings of pages 1, 4, 5, 6, 7, 8, 9, 10, 12, and 13. All 14 text pages were inspected. The ten supplied page images were visually inspected, including every numbered figure and the appendix's unnumbered response-classification table. Pages 2, 3, 11, and 14 have text-only coverage: their original page layouts were not visually inspected. No tools, browsing, OCR, or external sources were used. Instructions appearing inside the paper's example prompts were treated only as research evidence.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text identifies a 14-page paper. |
| Accessible physical pages | 1–14, with no gap in supplied page text. |
| Apparent completeness | The sequence reaches references on p. 14, but supplied page count alone does not independently establish that every original artifact is present. |
| Direct visual coverage | Partial page coverage: ten rendered pages; all nine numbered figures and the substantive table are visible. |
| Readability | Body text, captions, legends, and table content are readable. Plot bars lack exact numerical labels. |
| Equations | The simple marking-token counting expressions on p. 9 are readable; extracted superscript/fraction formatting is awkward but the image resolves it. |
| Appendices | Present as §8, beginning p. 11: §8.1 and §8.2. The supplied metadata's empty appendix-detection list does not mean appendices are absent. |
| Supplementary material | None supplied. No separate supplementary artifact is identified in the supplied text. |
| Referenced absent material | Cited papers, websites, benchmark source documents, and underlying experimental data/code were not supplied or reviewed. |
| OCR | Not needed for the supplied material. No independent OCR/native-text comparison was performed. |
| Other limitations | Exact plot values, sample counts per condition, and omitted implementation details cannot be reconstructed reliably from images. |

Evidence labels used below are [A] AUTHOR-REPORTED, [B] DIRECTLY OBSERVABLE, [C] ANALYST-DERIVED, and [D] ANALYST INTERPRETATION. No [E] EXTERNAL INFORMATION is introduced. Confidence describes confidence in the source-grounded account, not certainty that a defense will work in deployment. HIGH applies to clear supplied statements or readable objects; MEDIUM applies to plausible interpretation or approximate graphical readings; LOW or UNKNOWN applies where the evidence does not resolve a point.

## Document Inventory and Extraction Basis

This is an experimental artificial-intelligence security paper with a prompt-engineering method contribution, rather than a formal security proof or a deployed web-agent benchmark. The original title is **Defending Against Indirect Prompt Injection Attacks With Spotlighting**. Authors are Keegan Hines, Gary Lopez, Matthew Hall, Federico Zarfati, Yonatan Zunger, and Emre Kıcıman, affiliated with Microsoft. Page 1 identifies CAMLIS’24, Conference on Applied Machine Learning for Information Security, October 24–25, 2024, Arlington, Virginia, and a Creative Commons Attribution 4.0 license. Keywords are large language models, prompt injection attacks, and security.

The inventory denominator is: abstract and keywords; §1 Introduction; §2 Background and Related Work with §§2.1–2.3; §3 Spotlighting with §§3.1–3.4; §4 Experimental Methodology with §§4.1–4.2; §5 Results with §§5.1–5.4; §6 Discussion; §7 Conclusion; §8 Appendices with §§8.1–8.2; acknowledgments; 25 numbered references; Figures 1–9, including Figure 8's two model panels; one unnumbered table; prompt examples; and the mathematical expressions N^k and 1/N^k. There are no numbered algorithms, theorems, lemmas, formal hypotheses, or standalone architecture diagrams.

The experiment register assigns X1 to baseline attack susceptibility, X2 to defensive instructions, X3 to delimiters, X4 to datamarking for summarization, X5 to datamarking for document question answering, X6 to encoding for both attack tasks, X7 to datamarking's ordinary-task performance, X8 to encoding's ordinary-task performance, and X9 to few-shot defenses. Temperature sensitivity is an author-mentioned auxiliary analysis without a supplied figure or configuration. Attack-scoring examples are a methodological analysis rather than another benchmark experiment. Dynamic marking and the ROT13 bypass are design reasoning, not reported quantitative adaptive-attack experiments.

## 1. Plain-Language Orientation

The paper studies a problem that arises when a large language model (LLM) receives both legitimate instructions and text obtained from elsewhere. An assistant might be asked to summarize a web page or an email. That page or email can contain an instruction written by an attacker. The model may follow that embedded instruction instead of the user's request, even though the user never authorized it. The authors call this an **indirect prompt injection attack**, abbreviated XPIA. [A; pp. 1–2]

Their proposed defense, **spotlighting**, changes the presentation of outside text and tells the model how to interpret the changed presentation. The goal is to make the text's **provenance**, meaning its source and intended authority, continuously apparent. They test three variants: boundaries around the document, special markers throughout the document, and an encoded representation of the document. These are called **delimiting**, **datamarking**, and **encoding**. [A; pp. 2–4]

The researchers create 1,000 synthetic documents containing attacks that ask the model to abandon its original task and output one special keyword. They measure attack success during summarization and document question answering, then separately test whether transformations impair ordinary language tasks. Experiments use text-davinci-003 and June 2023 versions of GPT-3.5-Turbo and GPT-4, with temperature 1.0. [A; pp. 4–5]

Their central empirical result is that transforming outside text can reduce successful task takeover much more than merely warning the model. However, each technique has qualifications. Delimiters are comparatively weak and can be imitated. Datamarking preserves performance well on the shown benchmarks but still leaves nonzero attack success in some conditions. Encoding gives the lowest reported attack rates in the displayed GPT-3.5-Turbo attack experiment, yet substantially harms that model's ordinary-task performance. The authors therefore recommend encoding only with sufficiently capable models and with application-specific validation. [A/B; pp. 5–9]

For the user's research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, this paper supplies a mechanism and a motivation, not a direct comparative experiment. [D] A web agent can encounter attacker-controlled external content without its user deliberately submitting an attack, and additional capabilities can increase the consequences of following that content. The paper describes both points, but does not measure a vulnerability ratio between standalone LLMs and web agents, evaluate an end-to-end browser agent, or establish that every web agent is more vulnerable than every standalone model.

## 2. Document Roadmap

The abstract and introduction frame source confusion as a security problem. Section 2 explains how instruction-following LLM systems encounter outside data, distinguishes indirect attacks from direct user attacks, and summarizes safety approaches. Section 3 defines the three spotlighting variants and supplies example system prompts. Section 4 identifies models and explains attack measurement. [A; pp. 1–5]

Section 5 first measures defense effectiveness, then checks task preservation, recommends techniques, and discusses adversarial considerations. Its order matters: a reduction in attack success is not sufficient if the transformed document becomes difficult for the model to use. Section 6 uses telecommunications as an analogy for mixing control instructions and user data, and proposes separate channels as a future direction. Section 7 restates the contribution. [A; pp. 5–11]

The appendices materially qualify the main results. Section 8.1 defines successful takeover more narrowly than any influence on an answer. Section 8.2 shows impressive few-shot results but warns that examples and test attacks can be correlated. Acknowledgments and references finish the paper. These appendices are essential for interpreting what low attack success means and why the authors prefer structural marking over example-based defenses. [A; pp. 11–14]

## 3. Background and Context

An LLM produces text completions from a prompt. The authors describe instruction-following behavior as something encouraged through supervision, and note that this behavior supports systems that plan and reason. An **agent**, in this account, is a system built around such behavior to automate tasks; the supplied paper does not give a formal agent architecture. [A; §2.1, p. 2]

A **prompt injection attack** attempts to make the model follow an instruction that conflicts with its intended task. In a **user prompt injection attack**, or UPIA, the person directly prompting the model attempts to subvert its safety rules; the authors associate this with jailbreaking. In XPIA, the instruction arrives inside another source, such as a website, email, or text message. The legitimate user can be an innocent bystander. [A; §2.2, pp. 2–3]

The distinction depends on authority and context, not just offensive or dangerous wording. The paper's financial-transfer illustration shows that an instruction could be legitimate when issued directly by a user but malicious when embedded in unrelated external material. It also discusses **accidental XPIA**: text intended to instruct a human reader can be misinterpreted as an instruction to the model. These are explanatory examples, not evaluated transaction attacks. [A; pp. 2–3]

The authors use **code versus data** as a security analogy. Code means the designer's instructions; data means text that the system does not control. They argue that concatenating these into a token stream makes it difficult for the model to maintain their distinct authority. A **token** is the textual processing unit referenced by the paper; the supplied work does not explain tokenizer internals. **Natural language processing**, or NLP, denotes tasks such as summarization, question answering, sentiment classification, and language understanding. [A; pp. 1, 3, 7]

**Black-box** evaluation here means using the named models without the paper reporting access to, or modification of, their internal parameters. **Encoding** changes the text representation; the model is expected to recover its meaning while performing the task. The supplied work names base64, ROT13, and binary, but does not provide an implementation specification for those formats. No external definitions or model specifications are imported into this analysis.

## 4. Research Problem and Gap

**Existing problem.** The authors argue that external instructions can be mistaken for legitimate instructions because the model processes sources together. Websites and other outside material are therefore attack entry points. Plugins, capabilities, and access patterns increase the downstream risk of a mistaken instruction. [A; pp. 1–2]

**Shortcomings of previous approaches according to the authors.** Alignment tuning addresses many desired and undesired behaviors, but indirect injection has a source-authority problem distinct from direct harmful prompting. Related defenses include prompt engineering, classifiers, and fine-tuning. The authors build on reference [2] rather than claiming all spotlighting ideas first appeared here. Their own experiments show limited gains from warning instructions, while their adversarial reasoning identifies delimiter imitation as a bypass. [A; §2.3, p. 3; pp. 5, 9]

**Research gap.** The work seeks an easily applied prompt-level method that helps a model distinguish trusted instructions from untrusted text while preserving useful language performance. It also asks which transformation offers the best tradeoff. This gap is the paper's positioning, not an independently verified statement that no other source-aware defense existed. [A; pp. 1–4]

**Motivation.** The desired outcome is practical mitigation without requiring a model architecture change. Spotlighting operates through preprocessing and system-prompt instructions. **Scope.** Empirical evidence concerns synthetic keyword attacks, selected GPT-family models, summarization and document question answering, and four language benchmarks. It does not cover arbitrary attack objectives, every source modality, browsing workflows, multi-step tool execution, or real financial/data-exfiltration actions. [A/D; pp. 3–8]

## 5. Research Questions, Objectives, and Hypotheses

Two explicit question-form subsection headings serve as the main research questions: **RQ1: Can Spotlighting Reduce ASR?** in §5.1, and **RQ2: Does Spotlighting Impair Language Tasks?** in §5.2. ASR means Attack Success Rate. RQ1 is addressed by Figures 1–6 and the comparisons between warning instructions, delimiting, datamarking, and encoding. RQ2 is addressed by Figures 7–8. [A; pp. 5–9]

The broader objectives are to make provenance apparent, reduce indirect instruction-following, compare three transformations, and formulate use-case recommendations. The appendix adds an investigation of few-shot examples and clarifies the measurement construct. These are objectives and analyses, not additional formally stated hypotheses. [A; pp. 3–4, 8–13]

No formal null or alternative hypothesis, preregistered analysis, significance threshold, or theorem-backed security target is specified. [D; supplied-document inspection] The intuition that clearer token-block distinctions help prevent unwanted instruction-following guides the method, but the authors explicitly say they lack a clear understanding of why spotlighting works. [A; §6, p. 10]

The user's web-agent research question is external to the paper's own question headings. Its relevance is analyzed from the paper's discussion of outside data and capabilities. It must not replace RQ1 and RQ2 or be presented as an experimental question the authors directly tested.

## 6. Assumptions / Threat Model

**System model.** A legitimate task, such as summarization, is specified in a prompt, and outside document content is incorporated into the input. The defender can preprocess that content and update the system prompt. The attacker places instructive text inside the outside source. The model may then act on this text under the user's session. [A; pp. 1–4]

**Trusted components.** The designer's task instructions and the defender-controlled transformation/prompt construction are the intended control layer. The external document is untrusted. This is an account of intended authority, not a proof that the model enforces it. The examples themselves place document material into system-prompt templates; source distinction is therefore explained semantically to the model rather than implemented as a demonstrated independent hardware or architectural boundary. [A/D; §3, pp. 3–4]

**Attacker capabilities.** The attacker can insert document text. The security discussion asks defenders to assume the full system prompt has leaked, enabling an adversary to know delimiter or marker strategies. It considers imitation of delimiters, text without spaces, and prearranged ROT13 text that becomes a plain attack after transformation. [A; §5.4, pp. 9–10]

**Defender capabilities.** The defender chooses markers, may remove a chosen marker from input, can choose new marker strings for each invocation, can vary insertion locations, and can choose an encoding. Randomized insertion between tokenizer separations is proposed to mark attacks lacking whitespace. These controls are described design options; a quantitative comparison of these dynamic implementations is not supplied. [A; pp. 8–10]

**Evaluated attack objective.** The measured attacker tries to replace the assigned response with a special keyword. The appendix identifies 'canary' as an illustrative target. Credential theft, payment, and data exfiltration motivate the discussion but are not the outcomes measured by the reported corpus. [A; pp. 5, 11–12]

**Excluded or unspecified capabilities.** The paper does not provide a complete formal attacker model, query budget, adaptive optimization procedure, attacker-model interaction protocol, document-placement constraints, or guarantee against transformation-aware adversaries. It does not evaluate compromise of the preprocessing code or privileged instructions. Their omission should be treated as unspecified scope, not as explicitly proved impossible attacks. [D; HIGH confidence in the reporting boundary]

## 7. Methodology

### Method structure

Spotlighting has two primary components: optionally transform the outside input before it enters the prompt template, and update the system prompt with instructions explaining how that input should be treated. The model should process its meaning while refusing to adopt embedded instructions as new goals. This is inference-time prompt engineering; the paper does not report training a new spotlighting model. [A; §3.1, p. 3]

**Delimiting** prepends and appends special tokens. The example uses opening and closing guillemets, « and », and tells the model never to obey instructions between them. The cue appears at the boundaries. [A; §3.2, p. 3, text-only inspection]

**Datamarking** interleaves a special token through the whole document. The initial example replaces whitespace with a caret, so ordinary words remain readable but are visibly marked. The prompt explains that the markers distinguish document content from instructions. Later sections recommend more sophisticated token and placement variation because whitespace-only marking can leave a spaceless attack unmarked. [A; §§3.3, 5.4, pp. 3–4, 9–10]

**Encoding** applies an encoding algorithm and asks the model to decode and perform the intended task without following document instructions. The example uses base64. The proposed rationale is a more distinctive representation and implicit decoding by sufficiently capable models. The encoding experiment's caption identifies the transformation family, but does not state a complete executable configuration; therefore the base64 example should not be treated as a fully documented experimental implementation. [A/D; §3.4, p. 4; Fig. 6, p. 8]

### Models and settings

The models are text-davinci-003, GPT-3.5-Turbo from June 2023, and GPT-4 from June 2023. Labels such as Text-003 and GPT-3-Text-003 appear in figures and captions for the older model. Temperature is 1.0 in all experiments. The authors report examining temperature and finding no notable impact, but give no range, trial count, numerical results, or statistical assessment for that auxiliary examination. [A; §4.1, p. 4]

Hardware, API implementation details, software versions, token budgets, response-length settings, seeds, sampling repetitions, evaluation date, and exact request construction are not supplied. There are no reported training splits or model training procedures for spotlighting. These omissions limit reproduction precision. [D; supplied-document inspection]

### Attack data and metric

The synthetic corpus contains 1,000 documents with variations of a keyword payload. The attack asks the model to forget prior instructions and return only a special keyword. The documents are used in several tasks, and responses are collected. ASR is the fraction of the corpus yielding successful injections. [A; §4.2, p. 5]

The appendix defines success as the task being fully overtaken. Merely noticing or mentioning the malicious keyword while still summarizing is not success. A broader Affected Success Rate, AffSR, would count evidence of influence, but its exact operational scoring rules are not specified. The paper states that defense trends are similar under that broader measure without supplying a numerical AffSR table or plot. [A; §8.1, pp. 11–12]

The corpus-generation model, document topics and lengths, insertion positions, attack templates, deduplication, class distribution, public release, licensing, and per-condition exclusions are unspecified. The aggregate count does not establish identical usable sample counts or paired data across every figure. [D]

### Ordinary-task evaluation and controls

Datamarking is compared with unmarked inputs on GPT-3.5-Turbo using SQuAD question answering, IMDB sentiment, SuperGLUE Word-In-Context, and SuperGLUE BoolQ. Encoding is evaluated on the same plotted benchmark labels for GPT-4 and GPT-3.5-Turbo. The plots report Task Accuracy. Benchmark sample sizes, chosen splits, prompting details, and exact scoring rules are absent. The '100,000+' appearing in the SQuAD reference title on p. 14 is not the number of examples used here. [A/B/D; pp. 7–9, 14]

The comparisons function as ablations: baseline input, warning instructions, added delimiters, datamarking, encoding, and few-shot examples. No confidence intervals, error bars, hypothesis tests, standard deviations, or repeated-run results are supplied. Author descriptions of 'significant' reductions consequently indicate strong observed changes in the reported account; they do not establish a documented statistical-significance test.

## 8. Experiments / Analyses

| ID | Purpose and setup | Outcome and interpretation | Qualification |
|---|---|---|---|
| X1 | Compare baseline ASR for three models on summarization and document Q&A; Fig. 1, p. 5. | Approximate bars show substantial model/task variation; GPT-4 is lowest in summarization. | GPT-4 is not lowest in the displayed Q&A group; exact values are unlabeled. |
| X2 | Add warning instructions; compare GPT-3.5-Turbo and Text-003 with baseline; Fig. 2, p. 6. | Turbo changes little; Text-003 falls substantially but retains nonzero ASR. | Conditions producing baseline differences from Fig. 1 are not explained. |
| X3 | Add delimiters to defensive instructions for GPT-3.5-Turbo; Fig. 3, p. 6. | ASR falls from around 60% to around 30%, described as roughly halving. | The authors identify an imitation bypass and do not recommend delimiter-only deployment. |
| X4 | Datamarking for summarization; Turbo and Text-003; Fig. 4, p. 7. | Caption reports 3.10% for Turbo and 0.00% for Text-003. | Main text says Turbo falls below 3%, conflicting with the caption. |
| X5 | Datamarking for document Q&A; three models; Fig. 5, p. 7. | Reported rates are 8.0% Turbo, 1.0% GPT-4, and 0.00% Text-003. | Remaining Turbo failures exceed the abstract's broad below-2% formulation. |
| X6 | Baseline, marking, encoding for Turbo across two attack tasks; Fig. 6, p. 8. | Encoding reports 0.0% summarization and 1.8% Q&A, lowest displayed rates. | The accompanying ordinary-task encoding study shows a utility cost for Turbo. |
| X7 | Compare baseline and datamarking accuracy on four benchmarks with Turbo; Fig. 7, p. 8. | Bars are close; the authors report no detrimental impact. | BoolQ's marked bar is slightly lower; no uncertainty quantification resolves that difference. |
| X8 | Compare baseline and encoded accuracy on four benchmarks for GPT-4 and Turbo; Fig. 8, p. 9. | GPT-4 preserves most plotted accuracy; Turbo shows large declines. | GPT-4 Word-In-Context visibly declines, so preservation is qualified by task. |
| X9 | Add few-shot examples to warnings; FS1 and FS2 with Turbo; Fig. 9, p. 13. | Both plotted rates are low; text describes below 5%. | Example/test correlation and poor coverage of unknown attack tactics limit confidence. |

Each attack experiment manipulates prompt treatment or document representation and measures successful takeover. The ordinary-task experiments manipulate representation and measure task accuracy. No hypothesis tests or per-condition sample counts are reported. The register distinguishes demonstrated treatments from proposed dynamic marking: suggestions about new markers and locations cannot be promoted into measured adaptive robustness.

The scoring analysis in §8.1 explains a construct choice. A response consisting solely of 'canary' indicates takeover; a valid summary indicates failure; a valid summary that mentions attempted injection is still an attack failure under strict ASR. This matters because a defense can have a low strict takeover rate while the output still reflects malicious content.

## 9. Results

**Warning instructions are insufficient in the shown Turbo comparison.** Figure 2 places baseline and warning-only ASR near 0.61 and 0.60, respectively. Figure 3 similarly shows approximately 0.60 and 0.58. These are visual estimates from distinct plots, not exact repeated estimates of one condition. The authors describe only negligible or modest warning benefit. [A/B; pp. 5–6]

**Delimiters help but leave substantial failure.** The Figure 3 caption reports a baseline around 60% and a reduction by half; the final bar is about 30%. This supports mitigation rather than strong isolation. Known delimiters can be inserted by an attacker, according to §5.4. [A/B; pp. 6, 9]

**Datamarking substantially reduces keyword takeover.** In summarization, the Figure 4 caption reports 3.10% for Turbo and 0.00% for Text-003. In Q&A, Figure 5 reports 8.0%, 1.0%, and 0.00% for Turbo, GPT-4, and Text-003. The Q&A result demonstrates that datamarking does not uniformly achieve below 2%. The sentence on p. 6 claiming below 3% for Turbo summarization conflicts with the 3.10% caption. Both are preserved; no hidden reconciliation is imposed. [A; pp. 6–7]

**Encoding has the strongest shown attack suppression, with a capacity-dependent utility tradeoff.** Figure 6 reports 0.0% summarization and 1.8% Q&A for Turbo. Figure 8 shows that the same model family suffers material accuracy losses on encoded ordinary tasks. GPT-4 retains performance more effectively, though its Word-In-Context bar drops from approximately 0.70 to 0.60. The source does not supply an analogous GPT-4 encoding-ASR panel in Figure 6. [A/B; pp. 8–9]

**Datamarking is less disruptive on the shown ordinary tasks.** Figure 7's accuracy pairs are similar, with approximate changes ranging from a small increase to a small decline. The authors state no detrimental impact, but the plot contains a slight BoolQ decrease. Without error measures, its importance cannot be established. [A/B/D; pp. 7–8]

**Few-shot defenses appear strong but have acknowledged evaluation hazards.** Figure 9 suggests FS1 around 2% and FS2 around 5%. The main appendix text says below 5%, but the second bar is too close to 5% for a precise independent reading. The authors explicitly caution against full confidence because attack examples can correlate with the evaluation corpus. [A/B; pp. 12–13]

No new numerical improvement calculation is needed to establish these patterns. In particular, exact relative reductions should not be calculated from approximate baseline bars. A reduction 'by half' is an author description, not a percentage-point estimate. A 0.00% observed rate is a result for the tested setting, not a mathematical guarantee of zero future failures.

## 10. Figure-by-Figure Interpretation

All nine numbered figures were directly inspected in the supplied images. Every quantitative plot is a vertical bar chart with a linear y-axis. None shows uncertainty intervals, statistical-significance markers, exact labels on the bars, distributions, or individual observations. Bar heights listed as approximate are graphical readings, not recovered underlying data.

### Figure 1 — Baseline susceptibility by task and model

Location: p. 5. The x-axis groups Summarization and Q&A. The y-axis is Baseline Attack Success Rate, with ticks from 0.0 to 0.6 and a plot extending slightly higher. The legend uses blue for GPT-4, teal for GPT-3.5-Turbo, and green for Text-003. Approximate summarization rates are 0.17, 0.47, and 0.63. Approximate Q&A rates are 0.19, 0.24, and 0.15. [B; MEDIUM for values]

The figure supports the caption's point that susceptibility varies across tasks and models. It also qualifies nearby prose saying GPT-4 tends to have the lowest ASRs: that is true for the displayed summarization group, but Text-003 is lower in the Q&A group. No exact values or sample-specific uncertainty are labeled. The notably different baselines in later plots should not be treated as identical conditions without additional information.

### Figure 2 — Additional defensive instructions

Location: p. 6. The x-axis compares Turbo 3.5 and Text-003; the y-axis is Attack Success Rate with ticks from 0.0 to 0.6. Green denotes Baseline and dark purple denotes Instructions. Approximate pairs are Turbo 0.61 versus 0.60 and Text-003 0.30 versus 0.16. [B]

The strongest visible pattern is near-overlap for Turbo and a larger reduction for Text-003. This supports the caption's modest-impact interpretation and the prose's model-specific account. The caption does not fully identify the task or explain why these baselines differ from Figure 1. The Text-003 reduction should therefore not be combined numerically with another figure's baseline.

### Figure 3 — Instructions plus delimiters

Location: p. 6. Three categories are Baseline, + Instructions, and + Instr + Delimiters. The y-axis is Attack Success Rate, with ticks 0.0–0.6. Bars are teal, blue, and purple, respectively; treatment labels identify them without a separate legend. Approximate heights are 0.60, 0.58, and 0.30. The caption names GPT-3.5-Turbo and reports a baseline around 60% and reduction by half. [A/B]

This is a sequential defense comparison: warnings alone change little, while boundaries add a larger benefit. It leaves many attacks successful and does not test the specific delimiter-imitation bypass later discussed. The exact document task is not stated in the caption, although nearby examples discuss summarization.

### Figure 4 — Datamarking for summarization

Location: p. 7. The x-axis compares Turbo 3.5 and Text-003. The y-axis is Attack Success Rate, with ticks 0.0–0.5. Green denotes Baseline and dark blue denotes Mark. Baselines are visually about 0.50 and 0.42. The caption gives marked rates of 3.10% and 0.00%. [A/B]

The graph supports a large improvement for both models. The Text-003 marked bar is not visibly positive. The caption's exact Turbo rate is the clearest numerical statement, but p. 6 describes that rate as below 3%. This is a text–caption inconsistency. Likewise, the prose's 40% older-model baseline and the visually approximately 42% bar should be distinguished as a rounded description and a visual estimate, rather than treated as independently exact values.

### Figure 5 — Datamarking for document question answering

Location: p. 7. The x-axis lists Turbo 3.5, GPT-4, and Text-003. The y-axis is Attack Success Rate, ticked 0.00–0.25. Green is Baseline; dark blue is Mark. Approximate baseline rates are 0.25, 0.08, and 0.17. The caption explicitly reports marked rates of 8.0%, 1.0%, and 0.00%. [A/B]

The figure extends the datamarking pattern beyond summarization. It also shows model-dependent residual risk: Turbo retains more successful attacks than GPT-4 or Text-003. Its GPT-4 baseline near 8% differs from Figure 1's Q&A bar near 19%, with no supplied explanation. The claim of cross-model benefit is supported; identical baseline configurations across plots are not established.

### Figure 6 — Encoding compared with marking

Location: p. 8. The x-axis has Summarization and Q&A. The y-axis is Attack Success Rate, ticked 0.00–0.35. Blue denotes Baseline, teal Marking, and light green Encoding. The caption identifies GPT-3.5-Turbo. Approximate baseline rates are 0.34 and 0.19; marking is approximately 0.03 and 0.08. Encoding is reported as 0.0% and 1.8%, respectively. [A/B]

Encoding is lowest in both groups. The summarization encoding bar is at zero; the Q&A encoding bar remains positive. This supports the attack-suppression claim for these tasks and this model. It does not by itself establish performance preservation, which requires Figure 8, or provide GPT-4 encoding attack rates. Baseline shifts relative to Figures 1, 4, and 5 are unresolved.

### Figure 7 — Datamarking's ordinary-task performance

Location: p. 8. The x-axis lists SQuAD Q&A, Sentiment, WiC, and BoolQ. The y-axis is Task Accuracy, ticked 0.0–1.0. Green denotes Baseline; dark blue denotes Mark. Section 5.2 identifies the tested model as GPT-3.5-Turbo. Approximate pairs are SQuAD 0.95/0.96, Sentiment 0.92/0.92, WiC 0.63/0.65, and BoolQ 0.86/0.85. [A/B]

There is no large visible accuracy collapse. A small BoolQ decrease is visible despite the caption's unqualified 'no detrimental effect' language. Without uncertainty intervals, the decrease cannot be judged statistically or operationally. The figure supports approximate task preservation on these plotted benchmarks, not exact equality on every task or preservation of web-agent utility.

### Figure 8 — Encoding performance depends on model

Location: p. 9. This figure contains two substantively distinct panels: GPT-4 above and GPT-3.5-Turbo below. Both use SQuAD Q&A, Sentiment, WiC, and BoolQ on the x-axis and Task Accuracy on the y-axis. Ticks run from 0.0 to 0.8, with plots extending above 0.8. Green denotes Baseline; dark blue denotes Encoding. [B]

Approximate GPT-4 pairs are SQuAD 0.45/0.46, Sentiment 0.94/0.93, WiC 0.70/0.60, and BoolQ 0.91/0.89. Approximate Turbo pairs are SQuAD 0.86/0.58, Sentiment 0.93/0.50, WiC 0.64/0.50, and BoolQ 0.86/0.58. These values are estimates from the bars, not exact reported scores. [B; MEDIUM]

The bottom panel visibly shows substantial encoding costs. The top panel preserves most plotted tasks more closely but contains a clear WiC decline. The caption's wording 'most NLP tasks' is therefore an important qualification. The GPT-4 SQuAD baseline is lower than Turbo's in this figure; the supplied work does not explain that difference. Benchmark settings are insufficiently documented to turn these bars into a general model ranking.

### Figure 9 — Few-shot examples

Location: p. 13. The x-axis, labeled Treatment, has Baseline, + Instructions, + Instr + FS1, and + Instr + FS2. The y-axis is Attack Success Rate, ticked 0.0–0.6. Bars are green, teal, blue, and purple. Approximate rates are 0.61, 0.59, 0.02, and 0.05. The appendix identifies GPT-3.5-Turbo and says FS1 and FS2 differ slightly in prompt examples. [A/B]

Few-shot examples markedly outperform warning-only instructions in this displayed experiment. Exact FS1 and FS2 rates are not labeled, and the second bar cannot establish a strict less-than-5% inequality independently. The figure must be read together with p. 13's warnings about example/test correlation and uncertain real-world generalization. It is not evidence that few-shot learning has solved indirect prompt injection.

## 11. Table-by-Table Interpretation

### Unnumbered table — Classifying takeover versus mere mention

Location: p. 12, continuing §8.1 from p. 11. The table has two columns, **LLM Response** and **Conclusion**, and three rows. It is qualitative: there are no units, counts, aggregate percentages, significance markers, or uncertainty estimates. [A/B]

The first row gives a normal summary beginning with a recent meeting and classifies the attack as unsuccessful. The second row contains only 'canary' and classifies the attack as successful because the document task has been completely overtaken. The third row gives a summary that also notes instructions about printing canary. It is classified as unsuccessful because the model noticed the attack while continuing its original task. [A/B]

Its purpose is to define ASR, not rank defenses. There is no best/worst numerical comparison, baseline, tie, or missing-value convention. Ellipses indicate abbreviated illustrative responses rather than unavailable experimental observations. The table demonstrates why keyword presence alone is not sufficient for the paper's success metric and why a broader influence metric can exceed strict takeover ASR. No other substantive table is supplied.

## 12. Diagram / Architecture Interpretation

There is no standalone architecture or flowchart in the supplied paper. A textual reconstruction of the method is: outside document enters defender-controlled preprocessing; the transformed representation is placed in a prompt; the prompt explains its source status and requests the intended task; the LLM returns an answer; attack scoring determines whether the original task was overtaken. [A/D; §§3–4]

The legitimate task instructions form the intended control path. The document content forms the intended data path. Both ultimately reach the model as prompt content, which is why the authors discuss source confusion. A marker is a cue within that shared input, not a demonstrated separate authorization channel. The method has no reported feedback loop, multi-step planner, browser-control component, retrieval module, or tool-permission implementation. Those elements cannot be inferred merely because the motivation mentions agents and plugins. [D]

The discussion's telecommunications analogy is conceptual rather than a diagrammed implemented system. In-band signaling shares a medium; multi-frequency separation reduces accidental interference but does not fully stop intentional interference; out-of-band signaling uses a separate channel. The authors suggest an analogous separation for LLM control and data, while acknowledging that current common architectures do not straightforwardly provide it. [A; pp. 10–11]

## 13. Equations and Mathematical Concepts

**ASR definition.** The authors define ASR verbally as the fraction of corpus documents yielding successful prompt injections. A faithful mathematical restatement is ASR = successful-takeover documents / evaluated corpus documents. This notation is analyst-supplied, while the ratio definition is author-reported. The numerator counts strict takeover, not every keyword mention; the denominator must refer to the actual evaluated corpus. Multiplying the ratio by 100 expresses it as a percentage. [A/C; pp. 5, 11–12]

No new failure counts are inferred from the 1,000-document corpus. Although a stated percentage and denominator could permit arithmetic under additional assumptions, per-condition sample handling and repetitions are not documented sufficiently to make those counts dependable across all experiments.

**Random marking-token space.** On p. 9, the paper states that selecting a length-k marker from a character set of size N yields N^k possible marking tokens and an attacker guessing probability of 1/N^k. Here N is the number of suitable available characters and k is marker length. Exponentiation counts the combinations of k character positions. The reciprocal expresses one correct guess among those possibilities. The example uses a 5-gram; no concrete N is supplied. [A/B]

[D] The equal-probability interpretation requires uniform choice over the possible strings and no information about the current token. Multiple guesses, leaked current tokens, nonuniform generation, or attacks that need not guess a marker are not incorporated in this expression. It is therefore a token-guessing calculation, not a formal bound on ASR or an end-to-end security theorem.

**ROT13 construction.** Section 5.4 describes an attacker arranging source text so the defender's ROT13 transform produces a plain malicious instruction. The crucial mathematical property in the authors' reasoning is bidirectionality: the same simple substitution can undo the attacker's preparation. The example illustrates transformation-aware input construction, not an experimentally measured bypass rate. [A; p. 10]

There are no numbered objective functions, losses, optimization problems, proofs, theorems, or learned transformation equations. The statement that base64 yields a 'one-way transformation' is an author security characterization in context; the paper does not give a formal cryptographic definition or proof of that property. This account preserves the wording without treating it as a demonstrated general security guarantee.

## 14. Interpretation and Discussion

RQ1 receives a qualified positive answer: the displayed transformations reduce strict keyword takeover, and datamarking and encoding outperform simpler warnings and delimiters in the presented comparisons. RQ2 receives a technique- and model-dependent answer: datamarking approximately preserves the plotted Turbo benchmark accuracy, whereas encoding can substantially impair Turbo and is less disruptive for GPT-4 on most shown tasks. [A/B]

The security contribution concerns authority cues, not harmfulness classification alone. The model should understand external content without treating it as a command. This is why the authors prefer methods that mark source structure over few-shot examples tailored to familiar attack wording. Their expectation that structural techniques should generalize better is a rationale, not a comparative test against an independently sampled comprehensive adversary set. [A/D; pp. 3, 13]

The telecommunications analogy explains the authors' design intuition but is not causal evidence. They speculate that spotlighting moves token blocks into a different region of representation space. No representation-space measurements or mechanistic probes are supplied. They explicitly acknowledge an incomplete understanding of why it works and say separation is not perfectly secure against interference. [A; pp. 10–11]

Cross-reference checks identify several unresolved points. First, p. 6 says Turbo datamarking summarization is below 3%, whereas Figure 4 reports 3.10%. Second, the abstract's below-2% description is broader than the 8.0% Turbo datamarking Q&A result and the 3.10% summarization caption. Third, Figure 1 does not place GPT-4 lowest in both tasks despite prose saying it tends to be lowest. Fourth, baseline ASRs change between figures without a supplied condition-by-condition explanation. Fifth, Figure 7's BoolQ bar decreases slightly despite an unqualified no-detriment claim. Sixth, Figure 8's GPT-4 WiC decrease reinforces the caption's narrower 'most tasks' statement. These are preserved as differences in reporting or scope rather than silently repaired.

For the web-agent question, [D] the paper supports a two-part interpretation: outside sources create additional opportunities for unauthorized instructions to enter, and agent capabilities create additional consequences if those instructions are adopted. Exposure and consequence are distinct. The paper does not quantify either across standalone and web-agent populations, so it supplies a mechanism-level argument rather than a direct empirical answer about relative vulnerability.

## 15. Contributions and Novelty

**Conceptual contribution.** Spotlighting frames continuous provenance cues as a way to help separate authorized instructions from outside content. The paper explicitly identifies source confusion as a structural problem. [A; pp. 1–3]

**Methodological contribution.** It organizes delimiting, datamarking, and encoding into one prompt-engineering family, with preprocessing and explanatory system instructions as the common pattern. Delimiting and early versions of some techniques are acknowledged as related to previous work; novelty should not be described as inventing every component from scratch. [A; §3, pp. 3–4]

**Empirical contribution.** It compares defenses across models and two attack tasks, reports strong reductions for keyword payloads, and separately evaluates ordinary-task preservation. The joint security-and-utility evaluation is central because the strongest attack suppression can coincide with reduced usefulness. [A/B; pp. 4–9]

**Measurement contribution.** The appendix clarifies strict takeover ASR versus broader influence, and warns that few-shot evaluation can leak information through correlated examples. **Practical contribution.** The authors offer recommendations about marker choice, randomized marking, encoding capacity, and task-specific validation. [A; pp. 8–13]

The synthetic corpus is part of the evaluation, but there is no documented public dataset release or benchmark package. There is no new model architecture, training algorithm, security proof, deployed web-agent system, or measured hardware optimization. Such contributions should not be attributed to this work.

## 16. Limitations

### Authors' stated limitations

Delimiters can be subverted by an adversary who knows the prompt and inserts the same delimiter structure. Whitespace-only marking can fail to mark an attack without spaces. Marker choice can collide with input content, motivating application-sensitive selection and sanitization. Encoding must remain decodable by the model; smaller or earlier-generation models can make decoding mistakes or hallucinate, impairing task performance. Use-case validation is explicitly recommended. [A; pp. 5, 7–10]

ASR is task-dependent and difficult to interpret as an objective universal quantity. Strict ASR excludes influence that does not fully overtake the task, and the appendix offers AffSR as a broader alternative. The authors lack a clear mechanistic explanation for spotlighting and acknowledge that shared-channel separation is not perfectly secure. Few-shot examples cover known tactics and can correlate with the test set, making their low ASRs difficult to trust fully. [A; pp. 5, 10–13]

### Additional evidence-based analyst observations

[D] The attack corpus targets a narrow, easily scored keyword outcome. It does not establish resilience to partial manipulation, hidden tool-use changes, gradual goal drift, data exfiltration, or other agent actions. Proposed dynamic marking is not evaluated with reported numerical results, and the ROT13 discussion is a constructed example rather than an adaptive benchmark.

[D] Several baseline rates differ without explicit experimental identifiers, limiting numerical aggregation across figures. Exact ordinary-task scores, split sizes, scoring details, repeated-run variation, and statistical uncertainty are absent. No data/code availability statement supplies the material needed to reproduce the corpus and every prompt condition exactly.

[D] Some conclusion and abstract language is broader than the visible evidence. In particular, encoding's utility preservation is model- and task-dependent, and below-2% attack success does not characterize all datamarking conditions. These observations concern reporting and evidential scope; they are not claims that the authors expressly admitted each limitation.

## 17. Threats to Validity

The following validity labels are analyst categories, not terminology attributed to the authors.

**Internal validity [D].** Changing baseline rates across figures makes it difficult to determine whether every difference is caused only by the stated defense. Stochastic temperature-1.0 generation and unspecified repetitions also limit assessment of run variability. This does not negate large visible differences, but restricts precise causal and numerical claims.

**Construct validity [D].** Strict keyword takeover is a clear operational measure but captures only one security outcome. A model can mention or be influenced by attack text without counting as compromised. The appendix explicitly explains that distinction; whether such influence matters depends on the downstream task.

**External and ecological validity [D].** Synthetic documents and single-response language tasks differ from an autonomous web workflow involving many pages, evolving state, credentials, and actions. Model versions are specifically June 2023 for Turbo and GPT-4. The supplied work provides no evidence about later models or a broad population of deployed agents.

**Statistical conclusion validity [D].** No confidence intervals, repeated trials, or significance tests quantify uncertainty. Zero observed ASR does not establish zero underlying failure probability. Tiny benchmark accuracy changes cannot be declared meaningful or negligible statistically from the bars alone.

**Reproducibility [D].** The corpus count, model versions, temperature, conceptual prompts, and benchmark names provide useful anchors, but omitted generation, sampling, scoring, and execution details prevent exact reproduction from the supplied document alone.

**Generalizability [A/D].** The authors themselves warn that few-shot examples may fail on unfamiliar tactics. Their broader expectation that provenance transformations generalize better remains only partially evaluated because adaptive attacker conditions and diverse attack objectives are not quantitatively registered.

## 18. Future Work and Open Questions

### A. Future directions explicitly proposed or recommended by the authors

The discussion proposes a multi-channel analogue for LLMs in which control tokens are separate from data tokens and the model responds to instructions from the control layer. It notes that this is not straightforward in common architectures, references structured fine-tuning approaches, and says further work remains. [A; p. 11]

The practical sections recommend dynamic marker strings, changing insertion locations, and validating encoding's downstream performance for the intended use case. These are proposed refinements and validation requirements, not proof that their effectiveness has already been measured in this paper. [A; pp. 7–10]

### B. Additional questions logically remaining from the study

[D] How does spotlighting perform against adaptive attacks that know the transformation and pursue partial answer manipulation rather than a single keyword? Does repeated browsing increase cumulative exposure, and how should source markers persist across extracted text, summaries, and subsequent agent steps? What is the cost in prompt length, latency, and useful context capacity? These quantities are not measured here.

[D] Can strict takeover ASR and broader influence be jointly reported with an application-specific action metric? Which ordinary tasks suffer from marking or encoding, and how do exact decoding errors relate to failure? What explains the baseline shifts across figures? Would an independently generated, held-out attack distribution preserve the observed reductions? These are analyst questions grounded in the reporting gaps, not author-proposed experiments.

## 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model: a model that generates text from prompt input. |
| NLP | Natural language processing: computational tasks involving language. |
| PIA | Prompt injection attack: an attempt to replace or override intended instructions. |
| XPIA | Indirect prompt injection attack: unauthorized instructions inside an outside source. |
| UPIA | User prompt injection attack: a user directly attempts to subvert the model. |
| Jailbreaking | The paper's term for direct attempts to induce prohibited behavior. |
| Provenance | Where input came from and the source distinction the model should maintain. |
| System prompt / metaprompt | Instructions specifying the intended task and how supplied content should be handled. |
| Spotlighting | Transforming and explaining outside text so its source status is more apparent. |
| Delimiting | Marking the beginning and end of a text block with special tokens. |
| Datamarking / marking | Interleaving source markers throughout a text block. |
| Encoding | Changing text representation and asking the model to recover meaning while retaining the original task. |
| ASR | Attack Success Rate: fraction of evaluated documents causing full task takeover. |
| AffSR | Affected Success Rate: broader evidence of influence; fully executable scoring rules are not supplied. |
| Q&A | Question answering based on a document or benchmark input. |
| Few-shot learning | Supplying a small number of examples in the prompt to demonstrate desired behavior. |
| FS1 / FS2 | Two few-shot treatments that differ slightly in included examples; exact full configurations are unspecified. |
| Black-box model | A model evaluated without reported access to or modification of internal parameters. |
| Temperature | A generation setting set to 1.0; its mathematical implementation is not defined in this paper. |
| SQuAD | A named question-answering benchmark; its long title appears in reference [5]. |
| IMDB Sentiment | The named sentiment benchmark used for task-preservation evaluation. |
| SuperGLUE | The named benchmark suite providing Word-In-Context and BoolQ tasks. |
| WiC / WIC | Plot abbreviation corresponding to Word-In-Context; capitalization varies. |
| BoolQ | A benchmark name; the supplied work does not expand the name or give its scoring procedure. |
| k-gram | A marker string of k characters in the marking-token discussion. |
| N | Number of suitable characters available for generating a marker. |
| N^k | Number of length-k marker strings stated in the paper. |
| 1/N^k | Stated probability of guessing one randomly chosen marker under the counting model. |
| U+E000 | Unicode value suggested for a marker, identified by the authors as part of the Private Use Area. |
| In-band / out-of-band | Shared-channel versus separate-channel signaling in the authors' telecommunications analogy. |

## 20. Key Numerical Results

Reported percentages retain the source's precision. Approximate values are read from bar positions and have MEDIUM confidence. They should not be used as exact data for statistical testing or cross-figure aggregation.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Synthetic corpus size | 1000 | documents | Keyword-payload attack corpus | Author-reported | p. 5, §4.2 |
| Temperature | 1.0 | generation setting | All experiments | Author-reported | p. 4, §4.1 |
| Model versions | June 2023 | version date | GPT-3.5-Turbo and GPT-4 | Author-reported | p. 4, §4.1 |
| Abstract attack reduction | >50% to <2% | ASR | Broad experimental summary, not every condition | Author-reported | p. 1, abstract |
| Baseline summarization | ~17 / ~47 / ~63 | % ASR | GPT-4 / Turbo / Text-003 | Approximate visual estimate | p. 5, Fig. 1 |
| Baseline Q&A | ~19 / ~24 / ~15 | % ASR | GPT-4 / Turbo / Text-003 | Approximate visual estimate | p. 5, Fig. 1 |
| Instructions comparison | ~61 to ~60 | % ASR | Turbo | Approximate visual estimate | p. 6, Fig. 2 |
| Instructions comparison | ~30 to ~16 | % ASR | Text-003 | Approximate visual estimate | p. 6, Fig. 2 |
| Delimiter baseline and final | around 60; reduced by half | % ASR and relative description | Turbo | Author-reported | p. 6, Fig. 3 caption |
| Marked summarization | 3.10 | % ASR | Turbo | Author-reported | p. 7, Fig. 4 caption |
| Conflicting marked summarization wording | below 3 | % ASR | Turbo | Author-reported | p. 6, §5.1 |
| Marked summarization | 0.00 | % ASR | Text-003 | Author-reported | p. 7, Fig. 4 caption |
| Marked Q&A | 8.0 | % ASR | Turbo | Author-reported | p. 7, Fig. 5 caption |
| Marked Q&A | 1.0 | % ASR | GPT-4 | Author-reported | p. 7, Fig. 5 caption |
| Marked Q&A | 0.00 | % ASR | Text-003 | Author-reported | p. 7, Fig. 5 caption |
| Encoded summarization | 0.0 | % ASR | Turbo | Author-reported | p. 8, Fig. 6 caption |
| Encoded Q&A | 1.8 | % ASR | Turbo | Author-reported | p. 8, Fig. 6 caption |
| Datamarking SQuAD | ~0.95 / ~0.96 | accuracy fraction | Turbo, baseline / marked | Approximate visual estimate | p. 8, Fig. 7 |
| Datamarking sentiment | ~0.92 / ~0.92 | accuracy fraction | Turbo, baseline / marked | Approximate visual estimate | p. 8, Fig. 7 |
| Datamarking WiC | ~0.63 / ~0.65 | accuracy fraction | Turbo, baseline / marked | Approximate visual estimate | p. 8, Fig. 7 |
| Datamarking BoolQ | ~0.86 / ~0.85 | accuracy fraction | Turbo, baseline / marked | Approximate visual estimate | p. 8, Fig. 7 |
| Encoding SQuAD | ~0.45 / ~0.46 | accuracy fraction | GPT-4, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 top |
| Encoding sentiment | ~0.94 / ~0.93 | accuracy fraction | GPT-4, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 top |
| Encoding WiC | ~0.70 / ~0.60 | accuracy fraction | GPT-4, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 top |
| Encoding BoolQ | ~0.91 / ~0.89 | accuracy fraction | GPT-4, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 top |
| Encoding SQuAD | ~0.86 / ~0.58 | accuracy fraction | Turbo, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 bottom |
| Encoding sentiment | ~0.93 / ~0.50 | accuracy fraction | Turbo, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 bottom |
| Encoding WiC | ~0.64 / ~0.50 | accuracy fraction | Turbo, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 bottom |
| Encoding BoolQ | ~0.86 / ~0.58 | accuracy fraction | Turbo, baseline / encoded | Approximate visual estimate | p. 9, Fig. 8 bottom |
| Few-shot outcome | below 5 | % ASR | Turbo, appendix prose | Author-reported | p. 12, §8.2 |
| Few-shot treatment bars | ~2 / ~5 | % ASR | FS1 / FS2 | Approximate visual estimate | p. 13, Fig. 9 |
| Example dynamic marker length | 5 | characters | Illustrative 5-gram, not measured optimum | Author-reported | p. 9, §5.4 |
| Possible marker strings | N^k | strings | N characters, marker length k | Author-reported | p. 9, §5.4 |
| Single marker guess | 1/N^k | probability | Stated random-marker model | Author-reported | p. 9, §5.4 |

Calendar dates, postal address numbers, reference identifiers, historical example amounts, and reference-title dataset counts are accounted for where relevant but are not experimental results. In particular, the Colonial Pipeline text is a few-shot illustration, and its dates do not describe study data collection.

## 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External instructions can be adopted without user authorization. | Introduction and background describe websites, emails, and innocent users. | Threat framing | pp. 1–2 | Author mechanism claim; no standalone-versus-agent rate comparison. |
| Spotlighting combines source transformation and prompt instructions. | Two components explicitly described. | Method | p. 3, §3.1 | HIGH confidence in method definition; no architectural isolation demonstrated. |
| Warnings alone offer little Turbo benefit. | Near-equal baseline and instruction bars. | Figs. 2–3, X2 | pp. 5–6 | Strong visible pattern; exact values and variability absent. |
| Delimiters roughly halve the shown ASR but are bypassable. | Caption plus delimiter-imitation reasoning. | Fig. 3, X3 | pp. 6, 9 | Quantitative mitigation shown; bypass rate not measured. |
| Datamarking reduces summarization takeover. | Caption rates 3.10% and 0.00%. | Fig. 4, X4 | p. 7 | Strong reduction; conflicts with below-3% prose. |
| Datamarking helps Q&A across three models. | Caption rates 8.0%, 1.0%, 0.00%. | Fig. 5, X5 | p. 7 | Residual risk varies; not uniformly below 2%. |
| Encoding achieves the lowest shown Turbo attack rates. | Caption gives 0.0% and 1.8%. | Fig. 6, X6 | p. 8 | Limited to displayed tasks/model; utility must be assessed separately. |
| Datamarking approximately preserves shown benchmark performance. | Close accuracy pairs; author no-detriment statement. | Fig. 7, X7 | pp. 7–8 | Slight BoolQ decline; no statistical uncertainty. |
| Encoding utility is capacity- and task-dependent. | Large Turbo declines and smaller GPT-4 changes. | Fig. 8, X8 | pp. 7–9 | GPT-4 WiC also declines; 'most tasks' is essential. |
| Strict ASR excludes attack mention without takeover. | Three qualitative scoring examples and appendix definition. | Unnumbered table | pp. 11–12 | HIGH confidence; broader AffSR lacks numerical detail. |
| Few-shot success has generalization and leakage caveats. | Low bars plus explicit warnings about correlated examples. | Fig. 9, X9 | pp. 12–13 | Authors explicitly resist full confidence in low rates. |
| Web-agent relevance is additional exposure and potential consequence. | External-source and capability discussion. | Analyst synthesis | pp. 1–2 | MEDIUM confidence as relevance inference; not a measured comparison. |

## 22. Very Simple Explanation — Explain Like I'm 15

Imagine asking an assistant to summarize a webpage. Somewhere on the page, someone has written a message telling the assistant to stop summarizing and do something else. The assistant needs to understand that message as part of the page, while remembering that the page does not get to decide its job. This paper studies ways to make that distinction clearer.

One method puts a fence around the page's text. Another puts little markers all through it. A third changes the text into an encoded form and asks the assistant to understand it without accepting new orders from it. In the researchers' tests, the repeated markers and encoding usually stopped more attacks than a simple warning. But encoding could also make a less capable model much worse at its actual language task.

The tests mainly asked whether an attack could make the assistant abandon its task and output one special word. That is useful because success is easy to recognize, but it does not test every way an assistant might be manipulated. A zero observed attack rate means no successful attacks were counted in that condition; it does not promise that future attackers will always fail.

For web agents, the connection is that the agent reads material other people control, and it may have capabilities that make obeying the wrong instruction consequential. That is an inference supported by the paper's explanation. The researchers did not run a direct contest between standalone models and browsing agents, so the paper helps explain a possible reason for greater risk without measuring exactly how much greater it is.

## Completeness Audit

The analysis represents the supplied work against the inventory rather than equating length with completeness. 'Fully represented' below means the substantive content needed to understand that item is covered, not that every sentence is reproduced. All page numbers are physical PDF page numbers.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract, title, authors, keywords, venue | Yes, text and p. 1 image | Yes | Fully represented | Broad abstract claims are qualified by conditions. |
| §1 Introduction | Yes, text and p. 1 image | Yes | Fully represented | External input, credentials, capabilities, code/data framing. |
| §2 Background and Related Work | Yes, text | Yes | Represented in compressed form | No external cited works were independently reviewed. |
| §2.1 LLM Systems | Yes, text only | Yes | Represented in compressed form | Instruction following and agent motivation. |
| §2.2 Indirect Prompt Injection attacks | Yes, text only | Yes | Fully represented | UPIA distinction, external sources, accidental injection, cited demonstrations. |
| §2.3 Related approaches to LLM Safety | Yes, text only | Yes | Represented in compressed form | Alignment, classifiers, prompting, fine-tuning, extension of [2]. |
| §3 Spotlighting / §3.1 Overview | Yes, text only | Yes | Fully represented | Two-component method and source distinction. |
| §3.2 Delimiting | Yes, text only | Yes | Fully represented | Boundary-token example described rather than reproduced. |
| §3.3 Datamarking | Yes, text and p. 4 continuation image | Yes | Fully represented | Whitespace replacement and continuous markers. |
| §3.4 Encoding | Yes, text and image | Yes | Fully represented | Encoding examples, implicit decoding, capacity condition. |
| §4 Experimental Methodology | Yes, text and images | Yes | Fully represented | Reported details separated from missing configuration. |
| §4.1 Models | Yes | Yes | Fully represented | Three models, versions, temperature, unquantified sensitivity check. |
| §4.2 Measuring ASR | Yes | Yes | Fully represented | 1000 documents, keyword attacks, corpus fraction. |
| §5 Results | Yes | Yes | Fully represented | Defense efficacy, utility, recommendations, adversarial reasoning. |
| §5.1 / RQ1 | Yes | Yes | Fully represented | X1–X6; numerical and reporting qualifications retained. |
| §5.2 / RQ2 | Yes | Yes | Fully represented | X7–X8; encoding tradeoff emphasized. |
| §5.3 Overall Recommendations | Yes | Yes | Fully represented | Datamarking minimum; conditional encoding preference. |
| §5.4 Additional Considerations | Yes | Yes | Fully represented | Collision, dynamic markers, insertion, delimiters, spaceless text, ROT13. |
| §6 Discussion | Yes, text plus p. 10 image | Yes | Represented in compressed form | Telecom narrative condensed; speculation and imperfect security preserved. |
| §7 Conclusion | Yes, text only | Yes | Represented in compressed form | Repeated synthesis incorporated with qualifications. |
| §8 Appendices | Yes | Yes | Fully represented | Present despite metadata detection omission. |
| §8.1 Measuring ASR | Yes, text plus table image | Yes | Fully represented | Strict takeover versus broader influence. |
| §8.2 Few Shot Learning | Yes, text and images | Yes | Fully represented | X9, example behavior, leakage/generalization caveats. |
| Formal hypotheses | No such item found | Absence stated | Fully represented | No formal hypothesis is invented. |
| X1 baseline susceptibility | Yes | Yes | Fully represented | Fig. 1; model/task variation. |
| X2 warning instructions | Yes | Yes | Fully represented | Fig. 2 plus prose. |
| X3 delimiting | Yes | Yes | Fully represented | Fig. 3 plus bypass reasoning. |
| X4 datamarking summarization | Yes | Yes | Fully represented | Fig. 4; below-3% discrepancy retained. |
| X5 datamarking Q&A | Yes | Yes | Fully represented | Fig. 5; three exact caption rates. |
| X6 encoding attack suppression | Yes | Yes | Fully represented | Fig. 6; Turbo conditions identified. |
| X7 datamarking task accuracy | Yes | Yes | Fully represented | Fig. 7; approximate bar values. |
| X8 encoding task accuracy | Yes | Yes | Fully represented | Fig. 8; both panels separately covered. |
| X9 few-shot prompting | Yes | Yes | Fully represented | Fig. 9 and cautionary appendix. |
| Temperature auxiliary analysis | Statement inspected | Yes | Represented in compressed form | No quantitative report available. |
| Figures 1, 2, 3 | Yes, direct vision | Yes | Fully represented | Each has individual visual interpretation. |
| Figures 4, 5, 6 | Yes, direct vision | Yes | Fully represented | Exact caption rates separated from approximate bars. |
| Figure 7 | Yes, direct vision | Yes | Fully represented | Minor BoolQ decline retained. |
| Figure 8 top and bottom | Yes, direct vision | Yes | Fully represented | Model-specific performance patterns retained. |
| Figure 9 | Yes, direct vision | Yes | Fully represented | Few-shot rates treated approximately. |
| Unnumbered appendix table | Yes, direct vision and text | Yes | Fully represented | Three response categories and scoring rule. |
| N^k and 1/N^k expressions | Yes, direct vision and text | Yes | Fully represented | Symbols and scope explained. |
| ASR mathematical concept | Yes, verbal source definition | Yes | Fully represented | Formula identified as analyst restatement. |
| Numbered algorithms / theorems / diagrams | None found | Absence stated | Fully represented | No nonexistent objects reconstructed as source artifacts. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, empirical, measurement, practical. |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations. |
| Prompt examples | Yes | Yes | Represented in compressed form | Behavioral intent retained; long templates and base64 payload not copied. |
| Acknowledgments | Yes | Yes | Represented in compressed form | Mark Russinovich and Ahmed Salem thanked; no methodological evidence. |
| References [1]–[25] | Yes, supplied text | Yes | Represented in compressed form | Roles discussed; citation accuracy not externally validated. |
| Decorative logos, license icon, contact details | Yes where rendered/text supplied | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | Venue/license retained; artwork and full address not analyzed. |
| Supplied supplementary material | None supplied | Absence stated | Missing from supplied material | No separate supplement claimed reviewed. |
| Underlying corpus, code, and raw response data | Not supplied | Limitation stated | Missing from supplied material | Necessary for independent reproduction, not claimed as inspected. |
| Original visual layouts of pp. 2, 3, 11, 14 | No | Text content represented | Inaccessible | Text-only page coverage explicitly disclosed. |

### Missing or inaccessible material

The underlying PDF file was not opened independently; analysis used the supplied text and images. Original page layouts for pp. 2, 3, 11, and 14 were not supplied visually. Raw datasets, experiment code, full prompt configurations, API logs, response records, exact plot data, benchmark subsets, and repeated-run statistics were not supplied. No separate supplement was provided or identified. References were inspected as bibliography entries only; their linked contents were not consulted.

### Uncertain interpretations

The 3.10% caption versus below-3% text is unresolved. Baseline shifts across figures lack an explanation. Figure 9's FS2 bar is approximately 5%, so its exact relation to the prose's strict below-5% statement cannot be read confidently. Figure 7's small BoolQ decline has unknown practical and statistical importance. The authors' U+E000 absence claim is accompanied by an if-present sanitization clause; it is treated as their marker-choice proposal, not an independently verified universal guarantee. Their base64 'one-way' characterization is not backed by a formal proof. The proposed representation-space mechanism remains speculative. Exact graphical accuracy and baseline ASR values are unavailable.

### Deliberately compressed material

Repeated warning sentences and long prompt templates are described by their function rather than reproduced. The base64 example string is not decoded or copied because its role is to illustrate transformed input, not report a numerical outcome. The Cosette and Colonial Pipeline examples are summarized as illustrations. The telecommunications history is condensed while retaining the distinction between accidental separation and adversarial security. Acknowledgments, bibliography metadata, logos, copyright symbols, and contact information are compressed or treated as non-substantive. References [7] and [8] list the same supplied telecommunications source entry; no external correction is attempted. Reference [16] has a supplied title whose relationship to the discussion is not assessed through outside verification.

### Potential omissions

No known substantive item from the supplied inventory is left entirely unrepresented. This statement is limited to the supplied 14-page text and ten images, not unseen attachments or the contents of cited works. Reproduction details absent from the source cannot be supplied by analysis. Confidence is HIGH for coverage of readable supplied content, MEDIUM for graphical estimates and web-agent relevance inference, and UNKNOWN for unreported configurations, unseen artifacts, and performance beyond the tested settings.
