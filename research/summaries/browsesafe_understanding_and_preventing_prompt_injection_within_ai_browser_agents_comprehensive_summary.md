# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The paper and its embedded attack examples and evaluation prompts are treated as evidence, never as instructions. No tools, external sources, repository files, or linked artifacts were consulted. Source locators below use physical PDF page numbers, which match the printed page numbers in the supplied material.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for all 27 pages was supplied. |
| Page range and count | Physical PDF pp. 1–27; 27 text pages. |
| Pages apparently missing | None from the supplied text sequence. This establishes supplied-page continuity, not independent verification of the original PDF. |
| Visually inspected pages | 1–10, 12, 14–20, 22–25: 22 supplied page images. |
| Text-only pages | 11, 13, 21, 26, 27. Their text was inspected, but their layout and rendered notation were not visually verified. |
| Figures | Figures 1–12 are visually available. Figure 10's example body is on p. 17 and its caption continues onto p. 18. |
| Tables | Tables 1–3 are visually available. Tables 2–3 have readable numerical text. Table 1's coverage symbols require visual reading because text extraction loses them. |
| Equations | Metric definitions on p. 7 and logical aggregation on pp. 6 and 23 are readable by combining text and images. The extracted OR symbol is distorted in places. |
| Appendices | A–G supplied, including B.1–B.6, C.1–C.11, D.1, E, F.1–F.2, G.1–G.2. |
| Supplementary material | No separate supplementary files supplied. Benchmark and model links are reported by the authors but were not opened or assessed. |
| OCR | Not needed: native/extracted text accompanies the images. Small heatmap cells were checked against extracted text where possible. |
| Other limitations | Prompt templates contain literal ellipses, so their omitted portions cannot be reconstructed. Hardware, exact chunk-window size, detailed annotation checks, and several experimental implementation details are not specified in the supplied paper. |

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. HIGH confidence means the supplied evidence is explicit and readable; MEDIUM indicates interpretation or an unresolved qualification; LOW indicates substantial uncertainty; UNKNOWN indicates missing evidence. Confidence in a reported result is not equivalent to independent replication of that result.

# 1. Plain-language orientation

**[A]** *BrowseSafe: Understanding and Detecting Prompt Injection Within AI Browser Agents* studies how malicious instructions embedded in webpages can redirect an artificial intelligence browser agent away from its user's task. A browser agent repeatedly reads web content and chooses actions such as navigating, searching, or filling forms. The same page may contain useful information and attacker-written instructions. The security problem is keeping those instructions from becoming commands to the agent. The authors emphasize consequences involving real actions and sensitive information, rather than only undesirable text responses. [pp. 1–2, 20–21]

The researchers construct **BrowseSafe-Bench**, a dataset of 14,719 synthesized benign and malicious HTML samples informed by production browser-agent usage. They compare detection models, investigate which content characteristics make attacks harder to detect, and propose **BrowseSafe**, a defense combining explicit trust boundaries, raw-content scanning, a fine-tuned detector, parallel chunk classification, and replacement of dangerous tool outputs. [pp. 2–7]

The principal findings are that realistic benign distractors reduce average balanced accuracy; coherent attacks rewritten into visible content are harder to detect than many hidden HTML injections; indirect and stealth wording is harder than explicit wording; multilingual attacks have the lowest average detection accuracy among the tested attack types; and unseen injection strategies cause the largest generalization decline. BrowseSafe reports F1 0.904, precision 0.978, recall 0.841, balanced accuracy 0.912, no refusals, and latency below one second under the authors' evaluation conditions. These are detector results, not a demonstrated guarantee that every complete browser workflow remains safe. [pp. 4–10]

**Research-question relevance [D; MEDIUM]:** For “Why Are Web AI Agents More Vulnerable Than Standalone LLMs?,” the paper supplies mechanisms that plausibly increase exposure and consequences: repeated encounters with attacker-controlled material, complex HTML, hidden and visible injection locations, transformations that obscure provenance, and the ability to act on manipulated reasoning. It does **not** directly compare otherwise matched standalone large language models and browser agents. It therefore supports an explanation of browser-agent security risks, not a measured comparative vulnerability ratio.

# 2. Document roadmap

**Bibliographic inventory [A]:** Authors are Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, and Ninghui Li. Affiliations are Perplexity, Rutgers University, and Purdue University. Zhang and Tenenholtz are marked equal contributors. The supplied paper identifies itself as a COLM 2026 conference paper; the first-page margin gives arXiv:2511.20597v2, 12 August 2026. The actual title says **Detecting**, even though the provided report identifier contains “preventing.” No keyword list is supplied. [p. 1]

**Document type [D]:** A mixed cybersecurity, machine-learning, benchmark, and systems paper with empirical detector evaluations. It is not a controlled comparison of standalone and agentic LLM deployments, a formal security proof, or a systematic literature review.

| Inventory ID | Original component | Location and purpose |
|---|---|---|
| S0 | Abstract | p. 1: motivation, benchmark, evaluation, defense overview. |
| S1 | §1 Introduction | pp. 1–2: real-world detection gap and three contributions. |
| S2 | §2 Preliminaries | pp. 2–3: attacks, defenses, benchmark categories; Table 1. |
| S3 | §3 Benchmark Design and Empirical Analysis | pp. 3–6: construction, four difficulty analyses, defense design. |
| S4 | §4 Case Studies | pp. 7–10: evaluation setup, metrics, model comparisons, latency, generalization. |
| S5 | §5 Conclusion | p. 10: synthesis and intended community use. |
| S6 | Acknowledgments, ethics, reproducibility | p. 11: funding, synthesized/redacted examples, release statements. |
| S7 | References | pp. 11–15: bibliography, compressed here into the paper's related-work positioning. |
| AA | Appendix A | pp. 15–16: extended attacks, defenses, and benchmarks. |
| AB | Appendix B.1–B.6 | pp. 16–19: attack types, strategies, styles, domains, distractors, generation. |
| AC | Appendix C.1–C.11 | pp. 19–23: agent architecture through intervention design. |
| AD | Appendix D.1 | pp. 23–24: configuration analysis, largely repeating §4.3. |
| AE | Appendix E | p. 24: refusal behavior. |
| AF | Appendix F.1–F.2 | pp. 24–25: attack-type and injection-strategy heatmaps. |
| AG | Appendix G.1–G.2 | pp. 25–27: safeguard and general-purpose evaluation prompts. |

The visual inventory contains F1–F12 and T1–T3. The mathematical inventory contains E1 precision, E2 recall, E3 specificity, E4 F1, E5 balanced accuracy, and E6 document-level OR aggregation. No numbered theorem, lemma, proof, or standalone pseudocode algorithm is supplied. The four-stage benchmark pipeline and defense workflow are procedures described in prose.

# 3. Background and context

**[A] Prompt injection** means malicious instructions enter an AI system through content it is supposed to process, attempting to induce unintended behavior. The paper's example is a forum-summary task redirected by an instruction embedded among legitimate comments. The distinction is between the user's intended task and instructions placed in untrusted material by someone else. [p. 1]

A **large language model (LLM)** processes the contextual information provided to it. A **browser agent** adds an execution loop around a model: receive a user request, select tools, execute browser actions, receive observations, and repeat. A **tool output** is the returned payload from an action, potentially including raw page content, generated summaries, and other annotations. A **trust boundary** marks the point where untrusted external information must be checked before it influences subsequent execution. [pp. 19–21]

**HyperText Markup Language (HTML)** is the page representation used in this benchmark. Some HTML content is displayed to a human reader; other content resides in comments, attributes, hidden elements, or form fields. The paper distinguishes raw HTML from accessibility-tree and screenshot representations used in some prior evaluations. Its taxonomy separates three choices: an attack's **objective**, its **placement**, and its **wording**. Thus, an exfiltration objective can be expressed in different page locations and different linguistic styles. [pp. 3–4, 18]

**Data exfiltration** means directing information to an unauthorized destination. **Typosquatting**, as operationalized here, creates plausible attacker-controlled destinations resembling legitimate domains through substitution, omission, or concatenation. **Hard negatives** are benign examples designed to resemble attacks; they help prevent a detector from treating attack-like formatting or vocabulary as sufficient evidence of malicious intent. [pp. 19, 22]

The paper measures **classification**: whether a sample is marked benign or malicious. This differs from measuring whether an agent actually executes the attack or successfully finishes the user's task. **[D]** Maintaining that distinction is essential when using these findings to discuss practical agent compromise.

# 4. Research problem and gap

**Existing problem [A]:** Browser agents must process untrusted web content while autonomously performing multi-step tasks. An attacker can insert instructions into that content and try to alter the agent's execution flow. Potential harms discussed include click fraud, malware downloads, sensitive-data disclosure, and financial loss. These harms motivate the work; the paper does not report end-to-end rates for each harm. [pp. 1, 20–21]

**Shortcomings of previous approaches, according to the authors [A]:** Simplified injections in clean textual contexts do not reproduce the structural complexity of browser tool outputs. Real outputs contain rich HTML, benign command-like elements, multilingual content, and semantically coherent malicious rewrites. Prior tool/API and GUI benchmarks frequently lack some combination of HTML realism, distractors, injection diversity, and context-aware attack generation. This is the authors' positioning of prior work, not an independently verified judgment of the entire literature. [pp. 2–3]

**Research gap [A]:** The work asks why detection fails under realistic browser-agent content conditions and which benchmark dimensions expose those failures. Its goal is both diagnostic and practical: identify difficult factors and use them to motivate a deployable defense. [pp. 1–4, 10]

**Scope [A]:** Textual content in browser-agent tool outputs; synthesized HTML samples grounded in real usage patterns; binary detection across several model families; and a proposed architecture for intervention. Non-textual attacks, including malicious images and vision-specific inputs, are explicitly excluded from handling and benchmarking. [p. 21]

**Scope boundary [D]:** The paper supports claims about the evaluated detector workload. It does not establish the prevalence of attacks on the live web, a universal security ranking of model architectures, or the magnitude of additional vulnerability relative to a standalone conversational LLM.

# 5. Research questions, objectives, and hypotheses

The paper presents explicit prose questions rather than a numbered hypothesis framework. The following identifiers organize those questions without attributing new formal hypotheses to the authors.

| ID | Explicit question or objective | Evidence location |
|---|---|---|
| RQ0 | Why does detection fail in real-world browser agents? | p. 1, introduction. |
| RQ1 | Do realistic benign HTML elements degrade detection? | p. 4, §3.2. |
| RQ2 | Does hidden versus visible injection placement affect detectability? | p. 5, §3.3. |
| RQ3 | Does linguistic register affect detection? | p. 5, §3.4. |
| RQ4 | Do attack-type semantics affect detectability? | pp. 5–6, §3.5. |
| RQ5 | Are smaller specialized safety classifiers more effective than large general-purpose reasoning models? | p. 8, §4.1. |
| RQ6 | Is specialized fine-tuning worth the effort, and does the comparison hold with a same-data fine-tuned baseline? | p. 8, §4.2. |
| RQ7 | Does inference-time configuration substantially change performance? | p. 9, §4.3. |
| RQ8 | What is the performance–latency deployment tradeoff? | p. 9, §4.4. |
| RQ9 | How does performance generalize to unseen URLs, attack types, and strategies? | p. 10, §4.5. |
| RQ10 | How often do models refuse classification, and what does this imply operationally? | p. 24, Appendix E. |

The objectives are to construct a realistic benchmark, evaluate existing models, characterize detection difficulty, and design a layered defense. No formal preregistered hypotheses, null hypotheses, statistical significance thresholds, or power analysis are supplied. The user's comparative research question is an analytical lens applied here, not an experimental question directly tested by the paper.

## 6. Assumptions / Threat Model

**System model [A]:** Three components are described: a user-facing client; a browsing environment; and an agent service hosting model inference, state, and orchestration. They may share a host or run on separate hosts. At each iteration the agent either returns a result or issues one or more tool calls. Returned observations are fed back into subsequent reasoning. Complex tasks can require dozens or hundreds of calls. Hierarchical agent/subagent execution is discussed as an architectural possibility, not evaluated as a distinct experiment. [pp. 19–20]

**Trusted components [A]:** The authors assume only the AI browser agent itself is trusted. All external inputs, including web content, are untrusted. Their operational design flags tools capable of returning such content; pure-computation tools are generally unflagged. The security requirement is to maintain alignment with the user's high-level task as external data enters execution. [pp. 20–21]

**Attacker capabilities [A]:** First, an attacker may own a malicious website or fully compromise a benign website, gaining control over served content. Second, an attacker may have permission to submit content on an otherwise legitimate site, such as a product description or forum comment. Both can place instructions where an agent may encounter them. Visible rewriting is intended to represent both full-site control and restricted user-content scenarios. [pp. 18, 20]

**Attacker objective [A]:** Induce a sequence of attacker-chosen actions that departs from the user's task. The benchmark's semantic categories include role manipulation, system-prompt extraction, delimiter manipulation, social engineering, hypothetical framing, and multilingual instructions. Appendix C.5 qualifies this breadth: nearly all attacks reduce to data exfiltration or a similar attempt. [pp. 16–17, 22]

**Excluded or untested capabilities [A/D]:** The benchmark principles exclude user-initiated attacks and adversaries given system-prompt access. The system-prompt-exfiltration category is an attempted outcome, not an assumption that the attacker initially knows that prompt. Image-based and vision-specific attacks are excluded. Direct modification of the trusted agent implementation is outside the stated attacker roles. The paper does not supply separate quantified evaluations for every attacker-control regime. [pp. 4, 20–21]

**Research relevance [D]:** The architecture exposes a distinction between encountering adversarial language and allowing it to influence actions. Browser integration creates repeated externally supplied observations and operational consequences. A controlled standalone-versus-agent experiment would still be required to quantify how much these factors increase compromise probability.

# 7. Methodology

## 7.1 Study design and data construction

**[A]** The authors sampled 100,000 anonymized and redacted production browser-agent tool-call outputs after filtering for common domains, quality, and length. These informed HTML scaffolds and axes of variation. The final benchmark comprises 14,719 **constructed** samples, not 14,719 naturally observed successful attacks. Its split is 11,039 training examples and 3,680 test examples. [pp. 2–3]

Four principles guide construction: environmental realism, attack diversity, adversarial robustness through benign lookalikes, and ecological validity based on adversary-embedded web content. Four procedural stages implement them: extract/anonymize website text; wrap it in realistic HTML; add benign distractors; and inject malicious instructions into malicious samples. Eight HTML template styles cover semantic HTML5, attribute-rich layouts, and framework-style structures. [pp. 3–4, 18]

The taxonomy includes 11 attack types, nine nominal injection strategies, three linguistic styles, five distractor types, five application domains, and five context-aware generation components. These are dimensions of variation, not evidence that every possible combination is equally represented. The domains are workspace, education, social media, entertainment, and e-commerce. [pp. 2–4, 18]

Hidden strategies directly insert text into HTML comments, data attributes, CSS-hidden text, hidden form fields, or semantic attributes. Visible strategies rewrite inline paragraphs, list items, footers, or table cells. Context-aware generation extracts the source domain, analyzes branding and terminology, rewrites content, generates plausible attacker domains, and targets suitable elements. Attack and distractor rewriting uses `claude-sonnet-4-5-20250929`. [pp. 18–19]

Distractors mirror features that can also carry attacks, such as comments and hidden fields. Their inclusion in benign and malicious samples aims to break a shortcut in which the detector equates structure with maliciousness. The main pipeline says distractors are added to all samples, whereas Figure 3 includes a zero-distractor group; this remains an unresolved wording issue. [pp. 4, 19]

The supplied work does not detail annotator counts, independent label review, agreement, adjudication, class totals, full filtering thresholds, URL deduplication rules, or contamination checks. The paper calls the samples annotated, but its construction description does not establish human verification of every label.

## 7.2 Detector training and inference

**[A]** BrowseSafe fine-tunes Qwen3-30B-A3B-Instruct-2507, described as having 3 billion active parameters during inference. Training uses one epoch, learning rate 1e-5, and weight decay 0.1. Hard negatives are benign distractors generated with rules resembling attack construction. Their rationale is to discourage memorization of attack vocabulary. No isolated numerical hard-negative ablation is supplied. [pp. 6–8, 22]

At inference, large inputs are tokenized and divided into non-overlapping fixed-window chunks when they exceed a threshold denoted T_w. Each chunk is classified separately and in parallel. A logical OR combines chunk verdicts: one malicious chunk marks the whole document malicious. Chunking is described as inference-only. The numerical value of T_w, overlap alternatives, and concurrency limits are not specified. [pp. 22–23]

The threshold is selected for a 1% false-positive rate. The authors discuss 5% and 10% as possible operational alternatives that could improve recall, not as measured main-table results. The source does not specify a separate calibration set or exactly how threshold selection was separated from final evaluation. [pp. 8, 22]

## 7.3 System integration

Potentially untrusted tools are declaratively flagged. Classification scans raw returned content after removing AI-generated annotations; the rationale is that summaries and relevance assessments may already have omitted or transformed malicious material. Classification is described as asynchronous and parallel to model planning. If malicious content is detected, the system substitutes a placeholder explaining the block without repeating the payload, allowing the agent to change course. [pp. 6, 21–23]

**[D]** The paper's intended ordering is protection before malicious content influences later execution. It does not provide an implementation trace resolving all timing details between parallel planning, classification, and output release. Its architectural claim of end-to-end security guarantees should therefore not be read as a supplied formal proof.

## 7.4 Evaluation configuration

The setup says comparison with 23 frontier models; Table 2 contains 22 non-BrowseSafe configuration rows and one BrowseSafe row. Thus “models” and “configurations” are not used consistently. Inputs are full HTML without truncation, with dataset maximum length stated as 80k tokens. The paper calls Anthropic settings 1K, 8K, and 32K context windows, but their relationship to the full-input protocol is not fully explained. [pp. 7, 9]

Comparators include PromptGuard-2, gpt-oss-safeguard, GPT-5 mini, GPT-5, Haiku 4.5, and Sonnet 4.5. High-reasoning safeguard variants were excluded because of generation errors. Official HuggingFace repositories or APIs are reported as the evaluation interfaces. Hardware, serving configuration, exact benchmark timing setup, software versions, random seeds, repetitions, confidence intervals, and statistical tests are not supplied. [pp. 7–8, 11]

Appendix G gives policy prompts for safeguard models and instruction prompts for general-purpose models. Both bias toward SAFE unless malicious intent is clear. General-purpose models are asked to reason step by step and call a classification tool with a label and explanation. Some prompt content is replaced by ellipses. The supplied text does not provide a complete executable evaluation package. [pp. 25–27]

## 8. Experiments / Analyses

| ID | Purpose and setup | Main results and interpretation | Caveats |
|---|---|---|---|
| X1 | Vary distractor count; average balanced accuracy across models. Figure 3, §3.2. | Zero distractors: 90.5%; three: 81.3%. Authors interpret the decline as reliance on superficial attack-like cues. | Zero group n=44 versus n=340 at three; no intervals or matched-content protocol described. Plot/text range disagreement. |
| X2 | Group detection by injection strategy; average model balanced accuracy. Figure 4, §3.3. | Hidden attributes/fields 91.6%; comments 90.9%; visible paragraph rewrite 74.0%, footer 69.1%, table cell 71.1%. | Footer n=15, table n=2, list n=9. Placement and generation method differ together. |
| X3 | Compare explicit, indirect, stealth styles. Figure 5, §3.4. | 84.6%, 78.1%, 75.3%, respectively. Authors infer increasing evasion with semantic camouflage. | Unequal groups; no statistical tests or fully crossed controls reported. |
| X4 | Compare 11 attack types. Figure 6, §3.5. | Multilanguage lowest at 76.0%; system-prompt exfiltration highest at 85.0%. | Authors' English-feature explanation is an interpretation of performance, not a direct representation analysis. |
| X5 | Compare specialized safety and general-purpose detectors. Table 2, §4.1. | PromptGuard F1 0.350/0.360; safeguard 0.730–0.796; top reasoning configurations about 0.854–0.863. | Training, capacity, prompts, and operating points differ; high-reasoning safeguard excluded. |
| X6 | Compare BrowseSafe fine-tuning with API models. Table 2, §4.2. | BrowseSafe F1 0.904 versus best reported general-purpose F1 0.863. | Different base models and training access; not an architecture-only comparison. |
| X7 | Same-data Qwen3-8B zero-shot versus full fine-tuning. §4.2. | F1 0.559→0.765; recall 0.392→0.626; 11,039 training and all 3,680 test examples, separate thresholds at 1% FPR. | BrowseSafe comparison reuses its paper-reported result; no repeated-run variability. |
| X8 | Vary reasoning/settings. Table 2, §4.3 and D.1. | Haiku F1 0.805–0.810; Sonnet reasoning settings 0.862–0.863 versus no-thinking 0.807. | GPT-5 mini minimal 0.750 versus low 0.854 is a substantial exception to broad stability language. |
| X9 | Plot F1 versus median latency. Figure 7, §4.4. | BrowseSafe <1 s; Sonnet 23–36 s; GPT families around 2 s. | Hardware, workload distribution, concurrency, tail latency, and serving controls unspecified. |
| X10 | Train with held-out characteristics. Table 3, §4.5. | Baseline 0.905; unseen URLs 0.935; unseen attack types 0.863; unseen strategies 0.788. | Holdout identities, sample counts, repetitions, and uncertainty not supplied. |
| X11 | Count classification refusals. Table 2, Appendix E. | Sonnet 419–669; other tabulated families zero. | Refusal definition includes failures; precise scoring treatment remains ambiguous. |
| X12 | Per-model attack and strategy heatmaps. Figures 11–12, Appendix F. | Difficult categories broadly recur across models; visible rewrites are generally harder than hidden placements. | Dense matrix compressed below; small strategy samples explicitly limit conclusions. |

No experiment directly measures standalone-versus-browser-agent compromise, actual exfiltration success, long-horizon task completion after intervention, or all proposed defense layers separately. These absences delimit the use of the results rather than negating the measured detector comparisons.

# 9. Results

**Distractors [A/B]:** Figure 3 labels 90.5% average balanced accuracy for zero distractors and 81.3% for three. **[C]** The decline is 90.5−81.3 = **9.2 percentage points**, not a 9.2% relative decline. The authors summarize it as approximately ten points. Their stronger statement that this reveals absence of genuine semantic understanding is an explanatory interpretation, not something directly established by the aggregate curve. [pp. 4–5]

**Placement [A/B]:** Figure 4 places several hidden strategies around 87–92% and prominent visible rewrites around 69–75%. List-item rewrite is an exception at 81.3%. The headline “nearly twice” evasion claim is not itself a directly measured attack-success ratio: balanced accuracy averages recall and specificity. **[D]** The safe conclusion is that tested visible rewrites have lower average balanced accuracy, with especially weak evidence for the rare footer and table categories. [p. 5; p. 25]

**Language [A/B]:** Explicit, indirect, and stealth styles yield 84.6%, 78.1%, and 75.3%. **[C]** Explicit minus stealth is 84.6−75.3 = **9.3 percentage points**. Multilanguage attacks average 76.0%, versus 85.0% for system-prompt exfiltration. The authors connect this to English-feature dependence; the experiment does not separately isolate language, training coverage, and attack wording. [pp. 5–6]

**Overall model comparison [A/B]:** BrowseSafe leads Table 2 with F1 0.904 and balanced accuracy 0.912. Sonnet's best reported F1 is 0.863. **[C]** The F1 difference is 0.904−0.863 = **0.041**, or 4.1 points when F1 is expressed on a percentage scale. BrowseSafe versus Sonnet 32K has precision difference 0.978−0.935 = 0.043 and recall difference 0.841−0.801 = 0.040. Haiku's recall reaches 0.872, exceeding BrowseSafe's 0.841; BrowseSafe is therefore not the highest-recall configuration in the table. [pp. 7–8]

**Reusable training signal [A]:** Qwen3-8B improves from F1 0.559 to 0.765 and recall 0.392 to 0.626 after same-data fine-tuning at the stated operating point. **[C]** Improvements are 0.206 F1 and 0.234 recall. Using Table 2's BrowseSafe values, its differences from fine-tuned Qwen3-8B are 0.904−0.765 = 0.139 F1 and 0.841−0.626 = 0.215 recall. The authors report these approximately as 0.14 and 0.21. [p. 8]

**Generalization [A/B]:** Relative to Table 3's 0.905 baseline, unseen-URL F1 rises to 0.935, attack-type holdout falls to 0.863, and strategy holdout falls to 0.788. **[C]** Differences are +0.030, −0.042, and −0.117. These support strategy novelty as the largest tested generalization problem. They do not establish that every possible new strategy will produce the same decline. [p. 10]

**Operational availability [A]:** Sonnet refusal counts range from 419 to 669 among 3,680 examples. **[C]** These correspond to 419/3680×100 ≈ 11.39% and 669/3680×100 ≈ 18.18%. These are derived fractions, not source-reported percentages. A high conditional classification score must therefore be considered alongside the availability of a verdict. [pp. 7, 24]

# 10. Figure-by-figure interpretation

## Figure 1 — Overall classifier performance

**[B]** Horizontal bars on p. 2 show F1 on a percentage x-axis, ordered from low-performing PromptGuard variants to BrowseSafe. Colors distinguish groups, but no independent categorical legend is necessary to identify the labeled models. Exact labels include PromptGuard 35.0%/36.0%, safeguard 73.0%–79.6%, GPT-5 mini 75.0% and low reasoning 85.4%, Haiku 81.0%, Sonnet no-thinking 80.7% and reasoning 86.3%, GPT-5 84.9%/85.5%, and BrowseSafe 90.4%. There are no error bars. It is a selected overview rather than every configuration in Table 2. F1 is detection performance, not end-to-end safety.

## Figure 2 — Benchmark taxonomy

**[B]** The colored blocks on p. 4 are a taxonomy rather than a connected architecture diagram. They enumerate attack types, injection strategies, linguistic styles, domains, distractors, context-aware generation components, and metrics. No axes, quantitative areas, arrows, or execution order are encoded. Attack categories progress from five basic types to four advanced and two sophisticated types. The diagram supports the separation of attack objective, placement, and wording; it does not show empirical balance across combinations.

## Figure 3 — Distractor-count sensitivity

**[B]** A connected point plot uses distractor count with sample sizes on the x-axis and average balanced accuracy in percent on the y-axis. Counts are 0 and 3–12; groups 1–2 are not shown. Labeled values in order are 90.5, 81.3, 80.0, 83.1, 81.0, 80.5, 81.6, 81.6, 79.6, 81.1, and 83.0%. Sample sizes are 44, 340, 395, 360, 381, 386, 361, 366, 378, 342, and 338. The initial decline dominates; subsequent values fluctuate rather than decline monotonically. No uncertainty bars are provided. The prose lower-band range of 79.4–82.9% disagrees with plotted labels, whose post-zero minimum and maximum are 79.6 and 83.1%. Neither representation is silently corrected here. [p. 4]

## Figure 4 — Injection-strategy sensitivity

**[B]** Horizontal bars on p. 5 encode average balanced accuracy in percent. Exact values and n are: data attribute 91.6 (276); form hidden field 91.6 (104); HTML comment 90.9 (127); hidden text 87.4 (169); semantic abuse 86.8 (105); list-item rewrite 81.3 (9); inline-paragraph rewrite fallback 75.4 (876); inline-paragraph rewrite 74.0 (152); table-cell rewrite 71.1 (2); footer rewrite 69.1 (15). No error bars or significance markers appear. There are ten plotted labels despite the nominal nine-strategy taxonomy because fallback rewriting is separately displayed. The main pattern supports hidden-versus-visible differences, but the smallest groups cannot sustain precise rankings. Appendix F.2 explicitly warns about rare footer and table results.

## Figure 5 — Linguistic style

**[B]** Three horizontal bars on p. 5 compare average balanced accuracy: explicit 84.6% (n=1109), indirect 78.1% (n=340), stealth 75.3% (n=386). The percent axis is truncated to emphasize differences, not a zero-origin magnitude comparison. No error bars are shown. The trend is lower performance with increasing camouflage. The authors interpret this as keyword dependence; the visual itself establishes an association among these constructed groups.

## Figure 6 — Attack-type sensitivity

**[B]** Horizontal bars on p. 6 show percent average balanced accuracy. From highest to lowest: system-prompt exfiltration 85.0 (n=156); URL segment 84.1 (168); delimiter injection 83.0 (143); ignore previous 82.2 (169); todo 82.1 (168); InjecAgent 82.0 (174); social engineering 81.7 (169); indirect hypothetical 80.5 (183); role manipulation 80.3 (142); important message 80.2 (179); multilanguage 76.0 (184). No error bars appear. The lowest multilingual result is clear, but p. 6 also describes 184 as a training-set count, leaving its relationship to the plotted subgroup count unresolved.

## Figure 7 — Performance and latency

**[B]** A scatter plot on p. 9 places median/P50 latency in seconds on the horizontal axis, labeled log scale, and F1 percentage on the vertical axis. Labeled model markers identify configurations. Dashed reference lines mark 2 seconds and F1 0.85; upper-left positions combine higher F1 and lower delay. BrowseSafe occupies that favorable region. Nearby prose supplies exact qualitative ranges: BrowseSafe below one second, Sonnet 23–36 seconds, GPT families around two seconds. Individual unlabeled point coordinates are not converted into invented exact latency measurements. The displayed x-axis includes a label 0 despite being described as logarithmic, so its precise transform is unclear. No latency intervals or hardware information accompany the plot.

## Figures 8–10 — Attack examples

**[B]** These are syntax-colored HTML/text listings without quantitative axes. Figure 8 on p. 17 instantiates five basic patterns: important-message framing, todo insertion, InjecAgent-style instructions, previous-instruction override, and instructions placed within a URL segment. Figure 9 illustrates role manipulation, system-prompt exfiltration, delimiter injection, and authority/urgency-based social engineering. Figure 10 spans pp. 17–18 and illustrates hypothetical framing and mixed/non-English wording. The examples clarify attack intent and placement. They are illustrative synthesized payloads, not observed exploit traces or proof that a particular live agent obeyed them. Their operational wording is deliberately compressed here; all distinct categories are represented.

## Figure 11 — Attack-type heatmap

**[B]** On p. 24, rows are 11 attack types, columns are 23 displayed model/configuration entries including BrowseSafe, and cell annotations are balanced accuracy on a 0–1 scale. A red-to-green color scale runs approximately 0.5–1.0, with greener cells indicating higher accuracy. BrowseSafe's column ranges from 0.82 for multilanguage to 0.96 for system-prompt exfiltration. PromptGuard columns contain many values near 0.50–0.66. Multilanguage is generally difficult across columns. There are no confidence intervals or significance marks. The 253 annotated cells are inspected but deliberately compressed into trends and selected anchors; Appendix F's claim that reasoning beyond low budgets is not worthwhile is broader than a formal cost-controlled analysis supplied here.

## Figure 12 — Injection-strategy heatmap

**[B]** On p. 25, rows contain ten displayed strategy labels, including paragraph-rewrite fallback; columns match the model/configuration scheme. Annotated balanced accuracies use the same red-to-green 0.5–1.0 scale. BrowseSafe values by displayed row are footer 0.82, table cell 0.74, inline paragraph 0.86, fallback 0.86, list 0.88, semantic abuse 0.94, hidden text 0.98, HTML comment 0.99, hidden form field 0.99, and data attribute 0.99. Hidden strategies are generally greener than visible rewrites. Its caption says nine strategies despite ten displayed rows. The 230 cells are compressed; the rare-category warning materially qualifies the apparent footer/table rankings.

# 11. Table-by-table interpretation

## Table 1 — Benchmark coverage comparison

**[A/B]** On p. 3, rows compare InjecAgent, AgentDojo, Agent Security Bench, WASP, WAInjectBench, and BrowseSafe-Bench. Seven columns cover realistic threat model, attack diversity, distractors, injection diversity, context-aware generation, multimodal images, and end-to-end evaluation. Open circles mean not covered, gray circles partially covered, and black circles fully covered. These are qualitative author-assigned categories, not measured scores or statistical tests.

The BrowseSafe row shows full coverage for the first five dimensions, no image coverage, and partial end-to-end coverage. Prior rows have mixed coverage; several provide full end-to-end evaluation and image support where BrowseSafe does not. **[D]** The table therefore supports a tradeoff in benchmark emphasis, not universal superiority on every evaluation dimension. The small prior-work symbol matrix is compressed rather than used to make detailed independent claims about those external benchmarks.

## Table 2 — Full main numerical comparison

**[A/B]** All metrics below are dimensionless proportions except refusals, which are counts. Configurations reproduce the paper's labels. No standard errors, confidence intervals, significance tests, or per-row sample counts appear. The stated overall test set is 3,680.

| Model | Configuration | F1 | Precision | Recall | Balanced accuracy | Refusals |
|---|---|---:|---:|---:|---:|---:|
| PromptGuard-2 | 22M | 0.350 | 0.975 | 0.213 | 0.606 | 0 |
| PromptGuard-2 | 86M | 0.360 | 0.983 | 0.221 | 0.611 | 0 |
| gpt-oss-safeguard | 20B / Low | 0.790 | 0.986 | 0.658 | 0.826 | 0 |
| gpt-oss-safeguard | 20B / Medium | 0.796 | 0.994 | 0.664 | 0.832 | 0 |
| gpt-oss-safeguard | 120B / Low | 0.730 | 0.994 | 0.577 | 0.788 | 0 |
| gpt-oss-safeguard | 120B / Medium | 0.741 | 0.997 | 0.589 | 0.795 | 0 |
| GPT-5 mini | Minimal | 0.750 | 0.735 | 0.767 | 0.746 | 0 |
| GPT-5 mini | Low | 0.854 | 0.949 | 0.776 | 0.868 | 0 |
| GPT-5 mini | Medium | 0.853 | 0.945 | 0.777 | 0.866 | 0 |
| GPT-5 mini | High | 0.852 | 0.957 | 0.768 | 0.868 | 0 |
| GPT-5 | Minimal | 0.849 | 0.881 | 0.819 | 0.855 | 0 |
| GPT-5 | Low | 0.854 | 0.928 | 0.791 | 0.866 | 0 |
| GPT-5 | Medium | 0.855 | 0.930 | 0.792 | 0.867 | 0 |
| GPT-5 | High | 0.840 | 0.882 | 0.802 | 0.848 | 0 |
| Haiku 4.5 | No Thinking | 0.810 | 0.760 | 0.866 | 0.798 | 0 |
| Haiku 4.5 | 1K | 0.809 | 0.755 | 0.872 | 0.795 | 0 |
| Haiku 4.5 | 8K | 0.805 | 0.751 | 0.868 | 0.792 | 0 |
| Haiku 4.5 | 32K | 0.808 | 0.760 | 0.863 | 0.796 | 0 |
| Sonnet 4.5 | No Thinking | 0.807 | 0.763 | 0.855 | 0.796 | 419 |
| Sonnet 4.5 | 1K | 0.862 | 0.929 | 0.803 | 0.872 | 613 |
| Sonnet 4.5 | 8K | 0.863 | 0.931 | 0.805 | 0.873 | 650 |
| Sonnet 4.5 | 32K | 0.863 | 0.935 | 0.801 | 0.873 | 669 |
| BrowseSafe | Fine-tuned | 0.904 | 0.978 | 0.841 | 0.912 | 0 |

BrowseSafe leads F1 and balanced accuracy. Sonnet 8K and 32K tie at F1 0.863 and balanced accuracy 0.873. Safeguard 120B/Medium has the highest precision, 0.997, but recall only 0.589. Haiku 1K has the highest recall, 0.872, with precision 0.755. PromptGuard 22M has the lowest F1, recall, and balanced accuracy. The 20B safeguard configurations outperform the corresponding 120B configurations in F1; larger parameter count does not imply better performance in these rows. These patterns show different false-positive/false-negative tradeoffs, not a single universal safety ordering.

## Table 3 — Generalization ablations

**[A/B]** On p. 10, rows are baseline standard label stratification, held-out URLs, held-out attack types, and held-out strategies; the single numerical column is F1: 0.905, 0.935, 0.863, and 0.788. No uncertainty estimates, run counts, split sizes, or statistical comparisons are given. The table supports the relative severity of the tested holdout regimes. Its baseline differs from Table 2's 0.904; the supplied work does not explain whether this reflects a different run, rounding, or another condition.

## 12. Diagram / Architecture

Figure 2 is the only substantive taxonomy diagram; the defense architecture is primarily specified in prose. The following reconstruction is **[A] a synthesis of that prose**, not an additional supplied figure.

**User request → agent service → tool selection → browser action → tool output → trust check → raw-content extraction → chunk classification → OR aggregation → permitted observation or replacement placeholder → continued agent reasoning.** [pp. 19–23]

The user-facing client provides the request and possibly metadata. The agent service manages state and forwards actions to the environment. The environment returns observations, the crucial entry point for attacker-controlled content. A declarative flag identifies tools that may return untrusted material; classification decisions then determine whether the returned content is malicious. These are different functions: identifying untrusted provenance does not mean every such output is an attack. [pp. 20–21]

Preprocessing removes generated annotations to scan what the adversary controlled. Large content is split into independently processed chunks. Parallel classification is intended to reduce overhead; OR aggregation sacrifices permissiveness in favor of blocking if any chunk is suspicious. A positive result triggers a type-compatible substitute explaining the interruption without reproducing the attack. This aims to prevent repeated execution of a blocked path and accidental re-exposure while warning the user. [pp. 22–23]

The feedback loop is the next reasoning step after either ordinary content or a placeholder. Proposed boundary-case forwarding to stronger reasoning models and information sharing with tool-argument scanners extend this design, but their performance gains are not benchmarked. Likewise, the supplied paper does not quantitatively isolate the contribution of trust flags, preprocessing, aggregation, and intervention to complete-agent security.

# 13. Equations and mathematical concepts

The paper supplies classification formulas rather than a new optimization objective or theoretical result. The following notation is author-defined on p. 7: TP is true positives, TN true negatives, FP false positives, and FN false negatives. Positive refers to a malicious classification in the evaluation context.

| ID | Formula | Meaning and role |
|---|---|---|
| E1 | Precision = TP / (TP + FP) | Among samples predicted malicious, the fraction actually malicious. High precision reduces unnecessary blocking. |
| E2 | Recall = TP / (TP + FN) | Among malicious samples, the fraction detected. Low recall means attacks are missed. |
| E3 | Specificity = TN / (TN + FP) | Among benign samples, the fraction correctly accepted. |
| E4 | F1 = 2 × Precision × Recall / (Precision + Recall) | Harmonic combination of precision and recall. Used for overall comparison and generalization. |
| E5 | Balanced accuracy = (Recall + Specificity) / 2 | Gives equal weight to detecting malicious samples and accepting benign samples. Used in subgroup figures and heatmaps. |
| E6 | result = OR over i=1,…,n of r_i, with r_i ∈ {0,1} | Any chunk labeled malicious, r_i=1, makes the whole document malicious. Otherwise result=0. |

E1–E5 operate on sample-level confusion counts or their component rates and output proportions, displayed as decimals or percentages. The paper does not specify zero-denominator conventions. E6 operates on n chunk verdicts, not probabilities or an average confidence score. It appears in §3.6 and Appendix C.10; the extracted `W`-like symbol is the visually rendered logical disjunction. [pp. 6–7, 23]

T_w denotes the fixed token-window threshold for inference chunking; its numerical value is unspecified. P50 latency denotes median latency. FPR is expanded as false-positive rate and used for threshold selection, but a separate formula is not printed. The paper's 1% FPR operating point is not interchangeable with 1% of all predictions being wrong. No loss function, calibration equation, theorem, or formal bound connects detector scores to end-to-end security guarantees.

**[D]** A low balanced accuracy cannot directly be converted into attack success, because its two components include behavior on benign content. Likewise, OR aggregation's effects on document-level false positives depend on chunk behavior and number of chunks; the paper provides no numerical derivation of that relationship.

# 14. Interpretation and discussion

The evidence answers RQ1–RQ4 by identifying content dimensions associated with lower detection performance: distractors, visible rewrites, linguistic camouflage, and multilingual wording. These findings motivate hard negatives and realistic training examples. They are strongest as benchmark diagnostics. Claims about exactly what a model internally “understands” remain interpretive because no direct causal mechanism analysis or controlled representation study is supplied. [pp. 4–6]

RQ5–RQ6 show that specialized safety training alone does not ensure strong performance on this workload and that in-domain fine-tuning provides useful signal. The same-data Qwen3-8B comparison strengthens the training-signal claim. The authors explicitly say most benchmarked models might meet or exceed their detector if fine-tuned on this dataset; that is an author expectation, not an experiment on every model. The source therefore supports practical adaptation rather than a universal superiority claim for one architecture. [p. 8]

RQ7–RQ8 reveal that more reasoning is not uniformly beneficial and that latency can constrain use in interactive detection. GPT-5 mini's minimal-to-low change is material; higher settings thereafter offer little F1 improvement. Sonnet reasoning improves F1 but brings both substantial latency and refusals. BrowseSafe's reported favorable position needs hardware and serving information for replication. [pp. 7–9, 24]

RQ9 identifies placement novelty as the strongest tested generalization challenge. The authors describe the benchmark as a diagnostic instrument rather than a deployment pass/fail test. Their statement that any learning-based detector faces the same fundamental challenge is broader than the systems actually evaluated. [p. 10]

### Cross-reference and consistency ledger

| Issue | Both source representations | Assessment |
|---|---|---|
| Baseline F1 | Table 2: 0.904; Table 3: 0.905. | Unexplained; retain each with its condition. |
| Distractor band | §3.2: 79.4–82.9%; Figure 3 labels include 79.6, 83.0, 83.1%. | Text–figure mismatch; cannot resolve. |
| Strategy count | Nine nominal strategies; Figures 4/12 show ten labels including fallback. | A fallback category is separately plotted; caption/taxonomy not fully aligned. |
| Model count | §4 says 23 frontier models; Table 2 shows 22 comparator configurations plus BrowseSafe. | Model/configuration counting is ambiguous. |
| Recall emphasis | §4.2 insight emphasizes higher recall; prose highlights precision and balanced accuracy; Haiku recall exceeds BrowseSafe. | Improvement depends on comparator; no universal recall leadership. |
| Configuration stability | Prose broadly calls GPT settings stable; GPT-5 mini F1 is 0.750 minimal versus 0.854 low. | Important exception visible in Table 2. |
| Multilingual n | Figure 6 gives n=184; prose says training set has only 184 multilingual samples. | Relationship between counts is unclear; do not infer matching train/test counts. |
| Distractor inclusion | Pipeline says distractors added to all samples; Figure 3 contains 44 zero-distractor samples. | Possible control group or probabilistic construction, but not explicitly reconciled. |
| Context setting | Full HTML up to 80k tokens without truncation; 1K/8K/32K settings called context windows. | Setting meaning and compatibility not fully specified. |
| Refusal scoring | Appendix E describes F1 on samples classified, then says refusals can be treated as positives. | Exact scoring implementation is unclear. |
| Log latency axis | Figure 7 called logarithmic, includes 0 label. | Exact transformation is unspecified. |

**Research synthesis [D; MEDIUM]:** The paper suggests that browser-agent risk is a system-level combination of exposure, interpretation, and action. Rich external content creates many instruction-like surfaces; generated summaries can blur provenance; repeated tool loops repeatedly cross trust boundaries; and a manipulated model can issue consequential actions. It does not show that browser use intrinsically makes every underlying model easier to manipulate under matched conditions, nor does it quantify a standalone comparison.

# 15. Contributions and novelty

**Benchmark/data contribution [A]:** BrowseSafe-Bench combines synthesized malicious and benign samples with realistic HTML scaffolding and benign lookalikes, grounded in production-use observations. Its distinctive emphasis is the independent variation of semantic objective, HTML placement, and linguistic style. [pp. 2–4]

**Empirical contribution [A]:** Model comparisons and factor analyses document detection weaknesses across the evaluated families. Generalization holdouts add evidence that new placement strategies are a more difficult axis than the tested new URLs or attack semantics. Same-data Qwen3-8B fine-tuning demonstrates that the dataset supplies reusable training signal. [pp. 4–10]

**Systems contribution [A]:** BrowseSafe combines declarative tool trust flags, raw-content preprocessing, a fine-tuned classifier, parallel inference chunks, conservative aggregation, and context-aware replacement. The authors present this as a multi-layered defense blueprint. [pp. 6, 19–23]

**Implementation/availability contribution [A]:** The authors report releasing the benchmark and model through the links printed on pp. 1 and 11. Availability, licensing, artifact completeness, and reproducibility were not independently checked here.

**Novelty qualification [D]:** The supplied work does not introduce a new formal theorem or a fully specified novel training loss. Its main contribution is the combination of benchmark design, empirical characterization, and defense integration. Appendix B's phrase “four novel attack vectors” is an author claim; the paper itself associates these categories with earlier cited work, so this analysis does not independently certify their historical novelty.

# 16. Limitations

## Authors' stated limitations

**[A]** Non-textual attacks, including malicious images and vision-specialized inputs, are not handled or benchmarked. Multilingual training coverage is limited, with 184 samples reported in the training-set discussion. Unseen injection strategies are the most difficult tested generalization regime. Footer and table-cell rewrite samples are so few that Appendix F.2 says their results are likely not significant. Nearly all attacks reduce to exfiltration or a similar objective. [pp. 6, 10, 21–22, 25]

The authors also acknowledge that their trained detector struggles with some out-of-distribution variations that frontier LLMs handle better; generic frontier outputs are not readily calibrated for a desired precision–recall balance; and high-reasoning safeguard variants were excluded for generation errors. They identify cross-chunk/global context, boundary-case escalation, and tool-scanner integration as areas needing more work. BrowseSafe-Bench is explicitly diagnostic rather than a pass/fail deployment test. [pp. 8, 10, 22–23]

## Additional evidence-based analyst observations

**[D]** Synthesized payloads and template wrapping approximate aspects of production content but do not establish real-world prevalence or attack success. The source gives limited annotation-quality and leakage-prevention detail. Unequal subgroup sizes and missing uncertainty measures constrain rankings, especially among rare visible strategies. Placement comparisons also change rewriting methodology, so placement alone is not isolated.

The main table evaluates a detector, while many architectural protections are described without component ablations or end-to-end task metrics. Latency results lack hardware and load context. Threshold calibration provenance is unclear. Refusal scoring and several text–figure inconsistencies limit exact reproduction. No matched standalone-LLM comparison supports a causal estimate of increased browser-agent vulnerability. These are analyst observations, not claims the authors explicitly admitted.

# 17. Threats to validity

The following methodological categories are **[D] analyst assessments** based only on the supplied design.

**Internal validity:** The factor analyses do not describe fully matched content pairs or adjustment for interactions among type, style, placement, page, and length. A visible rewrite may differ from a hidden injection in coherence and generation procedure as well as position. The performance differences are observable; unique causal attribution is less secure.

**Construct validity:** Binary HTML detection is a proxy for resistance to malicious agent behavior. F1 and balanced accuracy do not directly measure exfiltration prevention, user-task completion, recovery after blocking, or attacker success over multiple steps. “Semantic understanding” and “English-feature reliance” are interpretations of accuracy patterns, not directly measured constructs.

**External and ecological validity:** Real usage informs the scaffolds, but final examples are synthesized across eight templates and five domains. Broad web diversity, non-text inputs, changing attacker strategies, and objectives beyond exfiltration remain incompletely covered. New-URL generalization is encouraging within the authors' construction process, not proof of unrestricted web generalization.

**Statistical conclusion validity:** No intervals, repeated runs, or formal tests accompany most rankings. Sample counts of two, nine, and fifteen make fine-grained strategy conclusions unstable. Model averaging can conceal heterogeneity, partially addressed by the heatmaps. The paper's “likely not significant” warning does not report an actual significance test.

**Reproducibility:** Named base and generator models, training recipe, split totals, metrics, and prompt excerpts are useful. Missing seeds, complete prompts, threshold calibration details, exact split membership, hardware, timing protocol, and chunk size prevent full reconstruction from the paper alone. Reported artifact releases may address some gaps, but those artifacts were not supplied or inspected.

**Comparative validity for the user's question:** Detection performance across model families is not a comparison between standalone and browser-agent use of the same model. The research relevance is mechanistic and architectural, with MEDIUM confidence, rather than a direct empirical answer to comparative vulnerability magnitude.

# 18. Future work and open questions

## A. Explicitly proposed by the authors

Expand multilingual coverage. Forward uncertain or out-of-distribution cases to slower reasoning models, using newly discovered failures as training feedback. Share raw-content detector uncertainty with scanners of subsequent tool-call arguments and benchmark the gains. Develop classifiers that combine chunk hidden states to detect attacks requiring a global view. Consider different false-positive operating points where intervention costs permit. Explore fine-tuning compact models such as PromptGuard for narrow browser-agent scopes. [pp. 6, 8, 22–23]

## B. Additional open questions from this analysis

**[D]** How much does the same underlying model's compromise rate change when given browser tools versus only text interaction under matched attacker content? Which defense layers improve end-to-end security and task completion, and by how much? How should refusal outputs be scored and handled consistently? Can threshold selection be separated transparently from final testing? What are the tail latency and resource costs for long multi-chunk pages? How does blocking affect legitimate workflows over dozens of tool calls? Can larger, balanced strategy groups reproduce the visible-versus-hidden pattern? How do non-exfiltration objectives and non-text modalities alter the results? These are remaining questions, not completed experiments.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| AI | Artificial intelligence; the broad label used for the model-based system. |
| LLM | Large language model; the language-processing component used for reasoning or classification. |
| Browser agent | A model-driven system that repeatedly selects browser tools and processes returned observations. |
| Agent loop | The repeated cycle of reasoning, acting, observing, and deciding the next step. |
| Prompt injection | Attacker-written instructions in content the system is meant to treat as data. |
| HTML | HyperText Markup Language; the structured page representation scanned here. |
| GUI | Graphical user interface; the visual interaction environment discussed in related work. |
| API | Application programming interface; a structured interface used by tools or hosted models. |
| Tool output | Data returned after an action, possibly mixing raw content and generated annotations. |
| Trust boundary | A point where untrusted data requires security handling before influencing trusted execution. |
| Raw-content extraction | Removing generated annotations so detection scans adversary-controlled source material. |
| Attack type | The malicious objective or semantic pattern, such as role manipulation or exfiltration. |
| Injection strategy | Where and how the attack is embedded in HTML. |
| Linguistic style | How directly or covertly the instruction is phrased. |
| Distractor / hard negative | Benign content resembling an attack's surface features. |
| Hidden injection | Instructions in non-rendered markup or attributes still accessible to an agent. |
| Visible rewrite | Instructions blended into ordinary displayed page content. |
| Exfiltration | Unauthorized transfer of information to an attacker destination. |
| Typosquatting | Creating a plausible lookalike domain for malicious redirection. |
| Fine-tuning | Additional training of an existing model on the benchmark's training examples. |
| Zero-shot | Evaluation without the task-specific fine-tuning used in the paired comparison. |
| TP, TN, FP, FN | Correct malicious, correct benign, incorrect malicious, and missed malicious classifications. |
| Precision / recall | Correctness of malicious predictions / coverage of actual malicious examples. |
| Specificity | Correct acceptance rate among benign examples. |
| F1 | Harmonic combination of precision and recall. |
| Balanced accuracy | Mean of recall and specificity. |
| FPR | False-positive rate; used to select the reported threshold. |
| Refusal | Failure or refusal to return a classification response. |
| P50 | Median; half the measured latencies lie on each side. |
| T_w | Fixed inference chunk-window token limit; numeric value not supplied. |
| r_i, n, OR | Verdict for chunk i, number of chunks, and rule that any positive chunk flags the document. |
| Out-of-distribution | Content variations unlike those adequately represented during training. |
| Holdout | A characteristic deliberately excluded during training to test generalization. |

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Production outputs sampled | 100,000 | outputs | Anonymized/redacted; informs scaffolds | Author-reported | p. 3, §3 |
| Benchmark total | 14,719 | samples | Constructed benign and malicious HTML | Author-reported | pp. 2–3 |
| Training/test | 11,039 / 3,680 | samples | Main split | Author-reported | p. 2 |
| HTML styles / domains | 8 / 5 | categories | Template and application diversity | Author-reported | pp. 4, 18 |
| Attack types / nominal strategies / styles | 11 / 9 / 3 | categories | Fallback separately plotted | Author-reported | pp. 2–4 |
| Maximum dataset input | 80k | tokens | Full HTML, no truncation claimed | Author-reported | p. 7 |
| Training recipe | 1; 1e-5; 0.1 | epoch; learning rate; weight decay | BrowseSafe | Author-reported | pp. 6–7 |
| Active inference parameters | 3B | parameters | Qwen3-30B-A3B-Instruct-2507 | Author-reported | pp. 6–7 |
| Threshold operating point | 1% | FPR | Reported detector evaluation | Author-reported | p. 22, C.7 |
| Zero/three distractors | 90.5 / 81.3 | % balanced accuracy | Average over models; n=44/340 | Visually readable | p. 4, F3 |
| Initial distractor decline | 9.2 | percentage points | 90.5−81.3 | Analyst-derived | p. 4, F3 |
| Explicit/indirect/stealth | 84.6 / 78.1 / 75.3 | % balanced accuracy | Average over models | Visually readable | p. 5, F5 |
| Multilanguage | 76.0 | % balanced accuracy | Lowest attack-type mean | Author-reported | p. 6, F6 |
| Hidden field/data attribute | 91.6 / 91.6 | % balanced accuracy | Injection-strategy groups | Visually readable | p. 5, F4 |
| Footer/table rewrite | 69.1 / 71.1 | % balanced accuracy | n=15 / n=2 | Visually readable | p. 5, F4 |
| BrowseSafe | 0.904 / 0.978 / 0.841 / 0.912 | F1 / precision / recall / BA | Main test table | Author-reported | p. 7, T2 |
| Best general-purpose F1 | 0.863 | F1 | Sonnet 8K and 32K | Visually readable | p. 7, T2 |
| F1 lead | 0.041 | F1 | 0.904−0.863 | Analyst-derived | p. 7, T2 |
| Qwen3-8B F1 before/after | 0.559 / 0.765 | F1 | Same-data fine-tuning; 1% FPR | Author-reported | p. 8 |
| Qwen3-8B recall before/after | 0.392 / 0.626 | recall | Same comparison | Author-reported | p. 8 |
| Generalization F1 | 0.905 / 0.935 / 0.863 / 0.788 | F1 | Baseline / URLs / types / strategies | Author-reported | p. 10, T3 |
| Strategy-holdout decline | 0.117 | F1 | 0.905−0.788 | Analyst-derived | p. 10, T3 |
| BrowseSafe latency | <1 | second | Reported inference latency | Author-reported | pp. 2, 9 |
| Sonnet latency | 23–36 | seconds | Family in latency discussion | Author-reported | p. 9 |
| Sonnet refusals | 419–669 | responses | Configuration-dependent, test n=3,680 | Author-reported | pp. 7, 24 |
| Sonnet refusal fractions | ≈11.39–18.18 | % | 419/3680 and 669/3680 | Analyst-derived | pp. 7, 24 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Realistic benign lookalikes challenge detection | 90.5% at zero distractors, 81.3% at three | F3 / X1 | p. 4 | HIGH for labeled means; MEDIUM for causal explanation. |
| Visible coherent rewriting is difficult | Paragraph 74.0%, fallback 75.4%, hidden attributes 91.6% | F4 / X2 | p. 5 | HIGH descriptive; rare footer/table groups and generation differences limit generalization. |
| Camouflage correlates with lower accuracy | Explicit 84.6%, indirect 78.1%, stealth 75.3% | F5 / X3 | p. 5 | HIGH descriptive; semantic-understanding explanation remains interpretive. |
| Multilingual group is hardest on average | 76.0%, lowest of 11 attack-type means | F6 / X4 | p. 6 | HIGH within benchmark; limited coverage and ambiguous n context. |
| Small safety classifiers have low recall | PromptGuard recall 0.213/0.221 | T2 / X5 | pp. 7–8 | HIGH within evaluated configurations; no universal classifier claim. |
| Fine-tuning produces reusable signal | Qwen3-8B F1 0.559→0.765, recall 0.392→0.626 | X7 | p. 8 | HIGH reported; no repeated-run uncertainty. |
| BrowseSafe leads main F1 | 0.904 versus comparator maximum 0.863 | T2 / X6 | p. 7 | HIGH table evidence; comparator training and refusal treatment differ. |
| Strategy novelty is largest tested holdout challenge | 0.788 versus 0.905 baseline | T3 / X10 | p. 10 | HIGH reported; holdout details sparse. |
| Operational utility includes verdict availability | Sonnet 419–669 refusals | T2 / X11 | pp. 7, 24 | HIGH counts; scoring treatment unclear. |
| Layered boundaries address external-content entry | Flagged tools, raw scanning, chunk OR, placeholder | Architecture / E6 | pp. 20–23 | HIGH design description; integrated security effect not isolated. |
| Browser integration creates additional exposure pathways | Repeated tool observations, attacker-controlled pages, action loop | C.1–C.4 | pp. 19–21 | MEDIUM analyst inference; no standalone comparison. |
| Findings do not cover visual attacks | Explicit exclusion of non-text inputs | Limitation | p. 21 | HIGH explicit scope boundary. |

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read a website and help complete a task. Someone who controls part of that website can hide a message telling the assistant to do something else. The message might be obvious, or it might look like a normal customer-service note. A browser agent can be especially exposed because it keeps reading new pages and using tools, and those tools can do things rather than merely produce an answer. This paper explains those pathways, but it does not run a direct contest between browser agents and standalone chatbots.

The researchers built thousands of artificial webpages based on patterns from real browser use. Some contained attacks; others contained harmless material that looked suspicious. Detectors did worse when ordinary page details resembled attacks, when malicious instructions blended into visible writing, and when wording was indirect or multilingual. That means a detector cannot safely assume that hidden code is always dangerous or polished visible text is always harmless.

Their defense checks external content at tool boundaries, scans the raw material, and uses a model trained on realistic examples. If any chunk looks malicious, the system replaces the dangerous output with an explanation of the block. Its reported detector score is better than the tested alternatives and its reported delay is short. But it still misses some attacks, struggles with unfamiliar placement methods, and does not cover malicious images. The practical lesson is that useful browser security requires both good detection and careful control over how outside information reaches the agent's next action.

# Completeness Audit

The inventory denominator is the 27 supplied text pages, 22 supplied page images, sections and subsections listed below, 12 numbered figures, three tables, six mathematical identities, 13 registered analyses including construction, three main contribution groups, and explicit limitations. Coverage means representation of accessible evidence, not verification of the released artifacts or reproduction of experiments.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, version, equal-contribution note | Yes | Yes | Fully represented | §2; title preserved as Detecting. |
| Abstract and §1 | Yes, text and visual | Yes | Fully represented | Framing, gap, contributions. |
| §2 attacks, defenses, benchmark background | Yes | Yes | Represented in compressed form | §§3–4, 11, 15; no independent literature validation. |
| §3 introduction and §3.1 | Yes | Yes | Fully represented | Data origin, four principles, four stages. |
| §3.2 | Yes | Yes | Fully represented | X1, F3, mismatch disclosed. |
| §3.3 | Yes | Yes | Fully represented | X2, F4, rare groups and ratio caveat. |
| §3.4 | Yes | Yes | Fully represented | X3, F5. |
| §3.5 | Yes | Yes | Fully represented | X4, F6, multilingual-count ambiguity. |
| §3.6 | Yes | Yes | Fully represented | Training and defense stages. |
| §4 setup and metrics | Yes | Yes | Fully represented | Table 2 and E1–E5. |
| §4.1 | Yes | Yes | Fully represented | Safety/general-purpose comparison and exclusions. |
| §4.2, including same-data baseline | Yes | Yes | Fully represented | X6–X7, thresholds and qualification. |
| §4.3 | Yes | Yes | Fully represented | Stability with GPT-mini exception. |
| §4.4 | Yes | Yes | Fully represented | Latency and missing serving details. |
| §4.5 | Yes | Yes | Fully represented | Generalization and diagnostic scope. |
| §5 conclusion | Yes | Yes | Represented in compressed form | Synthesis without repeating promotional wording. |
| Ethics and reproducibility | Yes, text-only | Yes | Represented in compressed form | Synthesized/redacted examples; links not inspected. |
| Acknowledgments | Yes, text-only | Yes | Represented in compressed form | NSF/ACTION support noted; grant 2229876 is funding metadata. |
| References pp. 11–15 | Yes, partly visual | Yes | Represented in compressed form | Bibliography not reproduced entry by entry. |
| Appendix A attacks/defenses/benchmarks | Yes | Yes | Represented in compressed form | Categories and author positioning retained. |
| B.1 basic/advanced/sophisticated types | Yes | Yes | Fully represented | All 11 types accounted for in F6 and F8–F10. |
| B.2 hidden/visible strategies | Yes | Yes | Fully represented | Five hidden, four visible, fallback issue. |
| B.3 linguistic styles | Yes | Yes | Fully represented | Explicit, indirect, stealth. |
| B.4 domains/templates | Yes | Yes | Fully represented | Five domains, eight templates. |
| B.5 distractors | Yes | Yes | Fully represented | Purpose and inclusion ambiguity. |
| B.6 generation | Yes | Yes | Fully represented | Five stages and named generator. |
| C.1 browser architecture | Yes | Yes | Fully represented | Three components, repeated loop. |
| C.2 threat model | Yes, p. 21 text-only continuation | Yes | Fully represented | Roles, assets, excluded modalities. |
| C.3 trust boundaries | Yes, text-only | Yes | Fully represented | Flags, tracking, parallel classification. |
| C.4 preprocessing | Yes, mixed text/visual | Yes | Fully represented | Raw extraction and provenance concern. |
| C.5 training | Yes | Yes | Fully represented | Hard negatives; exfiltration concentration. |
| C.6 chunking | Yes | Yes | Fully represented | Inference-only; T_w unknown. |
| C.7 thresholds | Yes | Yes | Fully represented | 1% measured operating point; 5/10% suggestions. |
| C.8 boundary cases | Yes | Yes | Fully represented | Proposed escalation, not measured gain. |
| C.9 tool scanning | Yes | Yes | Fully represented | Future integration. |
| C.10 aggregation | Yes | Yes | Fully represented | OR and global-context future work. |
| C.11 intervention | Yes | Yes | Fully represented | Placeholder, recovery, payload withholding. |
| D.1 repeated configuration results | Yes | Yes | Inspected but compressed as repetitive | Same evidence as §4.3. |
| Appendix E | Yes | Yes | Fully represented | Refusals and scoring uncertainty. |
| F.1 and F.2 | Yes, including visuals | Yes | Represented in compressed form | Heatmap trends and anchors; cells not all transcribed. |
| G.1 safeguard policy | Yes, pp. 26 text-only | Yes | Represented in compressed form | SAFE bias, categories, illustrative example. |
| G.2 general-purpose prompt | Yes, text-only | Yes | Represented in compressed form | Reasoning, classification tool, explanation, SAFE bias. |
| RQ0–RQ10 | Yes | Yes | Fully represented | Explicit questions mapped to analyses. |
| Formal hypotheses | No such items supplied | Yes | Not present | No hypotheses invented. |
| X1–X12 plus benchmark construction | Yes | Yes | Fully represented | Distinct conditions preserved. |
| F1 | Yes visually | Yes | Fully represented | Overview values and selection caveat. |
| F2 | Yes visually | Yes | Fully represented | Taxonomy, no false flow interpretation. |
| F3 | Yes visually | Yes | Fully represented | All labeled points and n retained. |
| F4 | Yes visually | Yes | Fully represented | All bars and n retained. |
| F5 | Yes visually | Yes | Fully represented | All values and n retained. |
| F6 | Yes visually | Yes | Fully represented | All values and n retained. |
| F7 | Yes visually | Yes | Represented in compressed form | Exact prose ranges; unlabeled positions not digitized. |
| F8, F9, F10 | Yes visually | Yes | Represented in compressed form | All attack categories; payload strings compressed. |
| F11 | Yes visually and text | Yes | Represented in compressed form | 253 cells reduced to trends and anchors. |
| F12 | Yes visually and text | Yes | Represented in compressed form | 230 cells reduced to trends and BrowseSafe column. |
| T1 | Yes visually | Yes | Represented in compressed form | Legend, dimensions, focal row; prior-work symbols not fully transcribed. |
| T2 | Yes visually and text | Yes | Fully represented | Every configuration and metric reproduced. |
| T3 | Yes visually and text | Yes | Fully represented | All four rows; baseline discrepancy retained. |
| E1–E6 | Yes | Yes | Fully represented | Definitions, role, symbols, missing conventions. |
| Standalone algorithm/pseudocode/theorems | None supplied | Yes | Not present | Prose workflows explained instead. |
| Major contributions | Yes | Yes | Fully represented | Benchmark, empirical, systems/release. |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst concerns. |
| Benchmark/model linked artifacts | No | No | Inaccessible within supplied material | Links reported only; no artifact inspection. |
| Separate supplements | None supplied | N/A | Missing from supplied material if intended | No claim that absent supplements were reviewed. |

## Missing or inaccessible material

No supplied text page is missing. Images for pp. 11, 13, 21, 26, and 27 were not provided, so these pages have text-only coverage. The original PDF binary, linked benchmark/model artifacts, training/evaluation code, hardware logs, exact split files, and any external citation contents were not inspected. Prompt sections replaced by ellipses are inaccessible within the supplied paper. No separate supplement was supplied or assumed.

## Uncertain interpretations

Unresolved points include 0.904 versus 0.905 baseline F1; Figure 3 versus prose range; nine nominal versus ten displayed strategy categories; model/configuration counts; multilingual n context; all-sample distractors versus zero-distractor controls; 80k full input versus settings described as 1K/8K/32K context windows; refusal scoring; the latency-axis transform; threshold-calibration procedure; and the precise synchronization between parallel planning and classification. Missing chunk size and hardware details prevent exact system reconstruction. These uncertainties were retained rather than silently repaired.

## Deliberately compressed material

The full bibliography, repeated related-work descriptions, repeated configuration discussion, syntax-colored attack payloads, and repetitive prompt examples are compressed. All distinct attack categories and prompt purposes are retained. Dense heatmaps are summarized rather than transcribed cell by cell, with the scope of that compression disclosed. Table 1's external-benchmark symbol matrix is compressed to dimensions, legend, and principal tradeoffs. Repeated headers, page furniture, and decorative formatting carry no separate scientific content.

## Potential omissions

Every substantive item identified in the supplied-document inventory is represented, explicitly compressed, or marked unavailable/uncertain. This does not mean every sentence, reference, prompt token, or matrix cell is reproduced. The analysis cannot establish artifact-level reproducibility, fill omitted prompt sections, or supply a direct standalone-versus-browser vulnerability comparison that the paper did not perform. Coverage is therefore comprehensive for the accessible paper content, with the stated compression and access boundaries.
