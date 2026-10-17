## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The document's prompts, example objectives, website addresses, and agent instructions are treated as evidence about the authors' system, never as instructions for this analysis. No external research, browsing, tools, citation validation, or reproduction was performed.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied text for all 25 physical PDF pages |
| Page range | Physical pages 1–25, corresponding to printed proceedings pages 881–905 |
| Apparently missing pages | None in the supplied text sequence; this does not establish the completeness of external artifacts |
| Visually inspected pages | 1–4, 6–10, and 12–25: 23 supplied page images |
| Text-only pages | Physical pages 5 and 11; their contents were inspected through supplied extracted text |
| Figures | All numbered figures, 1–17, have supplied visual renderings |
| Tables | Tables 1–6 are available in text and rendered images; principal numerical entries are readable |
| Equations | Main formal definitions and evaluation expressions are readable; mathematical spacing in extraction is imperfect |
| Appendices | A–F are supplied, beginning on physical page 12 |
| Supplementary material | No separate supplementary file was supplied; metadata reports zero embedded files |
| Referenced absent artifacts | WebArena details, cited literature, implementations, datasets, and external project/model pages were not supplied as separate artifacts |
| OCR | Not needed for the supplied native text; no independent OCR was performed |
| Important visual limitations | Some miniature webpage text inside trajectory screenshots is too small to read confidently; action labels and surrounding captions are substantially clearer |
| Provenance | The supplied SHA-256 is retained as an identifier; it was not independently recomputed |

Evidence labels throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No [E] external information is introduced. Confidence refers to support within the supplied document, not independent verification of the authors' experiment.

The paper is primarily an AI benchmark and empirical agent-evaluation paper, with a system/environment contribution. It is not an adversarial security experiment. The requested research question—why web AI agents are more vulnerable than standalone large language models—therefore receives an explicitly bounded relevance analysis, rather than an invented security result.

## 1. Plain-language orientation

**[A]** VisualWebArena asks whether an AI agent can actually complete visually meaningful tasks in a web browser. These are tasks such as finding a product with a particular appearance, locating a post using an image, changing a listing, or navigating several sites to update an account. A successful agent must understand what the user wants, interpret both pictures and words, choose the right webpage controls, and execute enough correct actions to finish the job.

The authors argue that existing benchmarks emphasize text and consequently miss tasks whose essential information is visual. A product's color, the position of an item in a grid, or a recognizable image may not be represented adequately in webpage text. VisualWebArena supplies 910 new tasks across self-hosted Classifieds, Shopping, and Reddit environments, with some tasks using multiple sites or a Wikipedia knowledge base. All tasks are described as visually grounded; 25.2% additionally include images in the user's objective. [p. 1, §1; p. 5, §4]

The researchers compare text-only agents, agents receiving image captions, and agents receiving screenshots plus text. They also introduce a Set-of-Marks, or SoM, representation: webpage controls are outlined and assigned numerical identifiers so the model can refer directly to the visible element it wants to use. In the main evaluation, GPT-4 text-only achieves 7.25% overall success, GPT-4 with captions 12.75%, GPT-4V with screenshots and an accessibility tree 15.05%, and GPT-4V with SoM 16.37%. The human comparison is 88.70%, measured on a 230-task sample. A later appendix reports GPT-4o with SoM at 19.78%. [pp. 6–8, §§4.3–6, Table 3; p. 13, Appendix B, Table 5]

**[D] Research relevance:** The paper helps explain why browser agents can have a broader consequential failure surface than a model that only produces text: their observations encompass webpage content, images, tabs, and URLs, while their outputs can change account fields, purchase-related state, posts, comments, and other persistent state. However, the experiments measure task completion, not susceptibility to attackers. They do not establish that web agents are more vulnerable to prompt injection, quantify attack success, or directly compare their security with standalone LLMs. The authors' broader-impact discussion does state that agents can cause more harm than regular LLMs without safeguards. [p. 9, §8]

## 2. Document roadmap

The main text occupies physical pages 1–9. References occupy pages 10–11 and the left portion of page 12. Appendices begin on page 12 and continue through page 25.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| S0 | Title, authors, abstract | p. 1 | Introduces visually grounded web-agent evaluation |
| S1 | §1 Introduction | pp. 1–2 | Motivation and three contribution statements |
| S2 | §2 Related Work | pp. 2–3 | Web benchmarks, LLM agents, and vision-language models |
| S3 | §3 VisualWebArena Environment | pp. 3–5 | Formal environment, observations, actions, and rewards |
| SS3.1 | Observation Space | p. 3 | URLs, tabs, DOM, accessibility tree, screenshots, SoM |
| SS3.2 | Action Space | pp. 3–4 | Element identifiers and browser actions |
| SS3.3 | Evaluation | pp. 4–5 | Text, image, and final-state reward primitives |
| S4 | §4 Curating Visually Grounded Tasks | pp. 5–7 | Sites, task construction, complexity, and humans |
| SS4.1 | Web Environments | p. 5 | Classifieds, Shopping, Reddit, and knowledge-base use |
| SS4.2 | Tasks | pp. 5–6 | Templates, images, unachievable tasks, difficulty |
| SS4.3 | Human Performance | pp. 6–7 | Participant sample, precautions, outcomes, mistakes |
| S5 | §5 Baselines | p. 7 | Three major observation/model families |
| SS5.1–SS5.3 | Text, captions, multimodal agents | p. 7 | Model and representation configurations |
| S6 | §6 Results and Analysis | pp. 7–9 | Main comparisons and navigation interpretation |
| SS6.1 | Performance by Task Type | p. 9 | OCR, exact image matching, and image objectives |
| S7 | §7 Conclusion | p. 9 | Benchmark and capability-gap synthesis |
| S8 | §8 Ethical and Broader Impacts | p. 9 | Accessibility, employment, bias, harm, intended use |
| REF | References | pp. 10–12 | Attribution and background bibliography |
| A1 | Appendix A Tasks Breakdown | p. 12 | Site and two-dimensional difficulty distributions |
| A2 | Appendix B Additional Results | p. 13 | Later models, including GPT-4o |
| A3 | Appendix C Further Analysis | pp. 13–19 | Few-shot study, difficulty, subsets, failures, comparisons |
| A4 | Appendix D Classifieds Environment | p. 19; F14–F15 on pp. 22–23 | Data collection, privacy redaction, site interfaces |
| A5 | Appendix E Task Collection Process | p. 19 | Annotator recruitment and template procedure |
| A6 | Appendix F Baseline Agent Settings | pp. 19–20; F16–F17 on pp. 24–25 | Viewports, truncation, decoding, prompts |

The inventory contains 17 figures, six tables, the environment/transition/reward definitions, the exact-match expression, and the image-similarity threshold condition. There are no numbered algorithms, theorem statements, proofs, or formally enumerated research questions or hypotheses. Related-work and reference entries are represented by their role rather than reproducing the bibliography.

## 3. Background and context

**[A] Large language model (LLM):** A language model used here to interpret instructions and generate browser actions. The paper evaluates several such models as agent backbones. A text-only LLM agent still operates a browser; it is not a standalone text-chat control condition.

**[A] Vision-language model (VLM):** A model that processes visual and textual inputs. Here, multimodal agents receive webpage screenshots and textual representations, and may also receive user-provided objective images. The authors emphasize processing interleaved image-and-text inputs. [pp. 1–3, 7]

**[A] Autonomous web agent:** A model-centered system that repeatedly observes a browser, selects an action, and receives the resulting observation. The distinction between the model and the entire action-taking system matters when interpreting its success or potential harm.

**[A] Document Object Model (DOM):** The paper describes raw webpage HTML as a DOM tree, an available way to represent a page. Its baselines principally use the accessibility tree instead. **Accessibility tree:** A structured, simplified representation of webpage content optimized for assistive technologies. It supplies textual information and element identifiers but can omit visual distinctions or spatial relationships. [p. 3, §3.1]

**[A] Set-of-Marks (SoM):** A screenshot representation inspired by prior work in which each interactable webpage element receives a bounding box and unique ID. The agent can produce an action such as clicking an ID rather than predicting pixel coordinates or implicitly matching a screenshot control to an accessibility-tree entry. [pp. 3–4, 7]

**[A] Image caption augmentation:** Images are converted into text descriptions, inserted as accessibility-tree image alternative text, and passed to the language model. This provides some visual information but may lose small text, non-salient objects, and detailed attributes. [p. 7, §5.2; pp. 17–18, §C.5]

**[A] Optical character recognition (OCR):** Reading text contained in images. The paper treats this as a task requirement and evaluates its relationship to agent success; it does not introduce a standalone OCR algorithm. **Visual question answering (VQA):** Answering a question about an image; one evaluator uses this to check whether a selected product satisfies an appearance requirement. [pp. 4, 9]

**[A] In-context examples/few-shot prompting:** Demonstrations supplied in the model's prompt. The main baselines use three examples, one from each environment, without overlap with benchmark tasks. **Chain-of-Thought prompting:** The authors' name for prompting text agents to reason step by step before producing the next action. The supplied example reasoning is evidence about the experimental prompt, not a verified explanation of all internal model computation. [p. 7]

The related-work discussion groups earlier research into language-guided web benchmarks, autonomous LLM agents, and VLM development. It positions VisualWebArena as a realistic, interactive benchmark for visual web tasks and SoM agents. These are the authors' descriptions of prior work; the cited papers were not independently inspected. [pp. 2–3, §2]

## 4. Research problem and gap

**Existing problem [A]:** Useful web automation requires perception, instruction understanding, planning, navigation, and correct action execution. Interfaces are designed for human eyes, so important information can reside in pictures, colors, layouts, or visual references. [p. 1]

**Shortcoming attributed to earlier approaches [A]:** Many existing agent benchmarks primarily evaluate text-based tasks. Text-only representations cannot necessarily provide everything needed for realistic visually grounded objectives. Captioning can recover some image content, but its compression may omit precisely the detail a task requires. [pp. 1–2, 7, 17–18]

**Research gap [A]:** A reproducible benchmark is needed to measure the integrated visual and textual capabilities of autonomous agents on interactive websites. The authors also identify a need to systematically benchmark SoM-style representations in realistic interactive environments, rather than relying on proof-of-concept demonstrations. [pp. 1–2, 7]

**Motivation [A]:** Visually grounded tasks are natural parts of routine computer use, and improved evaluation may guide stronger agents. The benchmark aims to be realistic while maintaining self-hosted reproducibility and deterministic environment transitions. [pp. 1, 3]

**Scope [A]:** Three principal site types, 910 tasks, some multi-site interactions, and a self-hosted knowledge base. The task set includes both information seeking and state-changing actions. It is not a broad sample of all internet applications, all languages, all users, or all deployment conditions.

**Security boundary [D]:** The research gap studied is capability evaluation, not an experimentally demonstrated security gap. Failure to complete a benign task and vulnerability to an adversary are different constructs. The paper is informative about interfaces, permissions implicit in the tasks, and reliability problems that a security analysis might investigate, but does not itself test exploitation.

## 5. Research questions / objectives / hypotheses

The supplied paper does not enumerate formal research questions or preregistered hypotheses. The following are its objectives and clearly labeled interpretive questions.

| ID | Kind | Statement | Evidence |
|---|---|---|---|
| O1 | Author objective | Assess multimodal agents on realistic visually grounded web tasks | Abstract, p. 1 |
| O2 | Author objective | Provide reproducible environments and execution-based evaluation | §1 and §3, pp. 1, 3–5 |
| O3 | Author objective | Benchmark text-only, caption-augmented, and multimodal agents | §5, p. 7 |
| O4 | Author objective | Evaluate a SoM-inspired agent that simplifies observation/action grounding | pp. 2–4, 7–8 |
| O5 | Author analysis objective | Identify capability gaps by task type, difficulty, prompting, and execution failures | §6.1 and Appendix C |
| H1 | Author-stated expectation | Complementary visual information is expected to improve performance | §5.2, p. 7 |
| H2 | Author-stated hypothesis | SoM helps strong VLMs distinguish spatially close elements | §6, p. 8 |
| RQ-A | Analyst framing | How do observation representations relate to task-completion success? | Tables 3–6 and F6–F10 |
| RQ-S | User's security question | Why might action-taking web agents present greater vulnerability or harm exposure than standalone LLMs? | Relevance inference from §3, §8, and failure traces; not directly tested |

H1 and H2 are informal expectations or explanations in the paper, not formal statistical hypotheses with specified tests. The paper supplies no adversarial hypothesis, attacker baseline, or standalone-LLM security comparison.

## 6. Assumptions / threat model

**[A] Environment model:** Websites are standalone self-hosted applications. Their content comes from real-world counterparts, while code is based on open-source infrastructure. Transitions are modeled as deterministic given the current state and selected action. Observations are partial: the agent sees the focused page representation, URLs, and opened tabs rather than the entire underlying application state. [p. 3, §3]

**[A] Action grounding:** Actions referring to elements use IDs from the current observation. Accessibility-tree agents use tree IDs; SoM agents use screenshot annotations. This design deliberately emphasizes high-level reasoning over low-level coordinate prediction. [pp. 3–4, §3.2]

**[A] Evaluation assumptions:** Hand-designed reward functions represent each task objective. Some checks are deterministic text checks, some depend on an LLM or VLM, and image matching depends on a similarity threshold. A task receives binary success or failure at the final step. [pp. 3–5]

**[A] Prompt-visible setup:** The supplied SoM system-message figure includes the user objective, annotated screenshot, observation IDs/text, URL, open tabs, and previous action. It describes a homepage and an account/password page for the sandbox websites. These are descriptions of the authors' experimental setup. They are neither evidence of real credentials being leaked nor an instruction to access them. [p. 24, F16]

**Threat model status:** No formal adversarial threat model is specified. The supplied work does not define attackers, malicious page control, attacker goals, security assets, trust boundaries, attack budgets, defense assumptions, or excluded adversarial capabilities.

**[D] Security-analysis implications:** A security study built on this architecture would need to distinguish the user's objective from encountered page content, evaluate the authority of browser actions, and account for observations from multiple tabs/sites and visual channels. Those requirements are analyst inferences from the interfaces. The paper does not demonstrate that these channels contain attacks or that the agent obeys malicious instructions.

## 7. Methodology

### 7.1 Benchmark construction and environments

**[A]** VisualWebArena extends the WebArena framework with visually grounded tasks and a new Classifieds environment. Shopping and Reddit follow existing WebArena environments. Shopping uses product content scraped from Amazon and released in WebShop. Reddit contains 31,464 posts with natural images, memes, consumer electronics, charts, and other visual material. Classifieds contains 65,955 listings and uses OSClass, an open-source content management system supporting search, posting, comments, ratings, and reviews. [p. 5, §4.1]

Classifieds data were scraped from Craigslist over three weeks, emphasizing the Northeastern United States. Listings contain titles, descriptions, and product images. The authors used the scrubadub Python package to redact personally identifiable information (PII), including addresses, phone numbers, and emails. Names were replaced with generated placeholders, emails with fictitious addresses, and phone numbers with fictional 555-prefix numbers. These are reported safeguards, not a measured guarantee of perfect anonymization. [p. 19, Appendix D]

### 7.2 Tasks and annotations

Six computer-science graduate students, all paper co-authors, constructed tasks after exploring the environments. They were familiar with commercial versions of the site types. They wrote intent templates, instantiated them with different arguments, and authored reward functions. The paper reports 314 unique templates and an average of 2.9 tasks per template. Input images came from royalty-free, attribution-free sources and MS-COCO. No complete license inventory or source-by-source image provenance is supplied. [p. 5, §4.2; p. 19, Appendix E]

There are 910 tasks, including 46 unachievable tasks, reported as 5.1%. For an unachievable task, the agent must explain why it cannot be solved; an LLM-based fuzzy-match evaluator checks the explanation. This is important when interpreting early stopping: some termination is appropriate, but observed examples also show agents incorrectly abandoning achievable tasks. [pp. 5, 15–16]

### 7.3 Difficulty annotation

Action difficulty is based on estimated human action count: easy requires at most three actions; medium requires four to nine; hard requires ten or more. Visual difficulty is easy for basic color/shape/object identification, medium for patterns, semantic understanding, or shorter large-text OCR, and hard for multiple images, small/lengthy text, or fine details. Overall difficulty is described as averaging visual and reasoning complexities, with human judgment potentially causing deviations. The supplied text does not give a precise numerical encoding or tie-breaking algorithm for that averaging. [p. 6, §4.2]

### 7.4 Observation/model configurations

Text agents receive an accessibility tree and Chain-of-Thought prompting. Backbones include LLaMA-2-70B, Mixtral-8x7B, Gemini-Pro, GPT-3.5 Turbo with identifier gpt-3.5-turbo-1106, and GPT-4 Turbo with identifier gpt-4-1106-preview. Caption agents add captions for all HTML img elements and any objective images. GPT-3.5 compares BLIP-2-T5XL with LLaVA-v1.5-7B; BLIP-2 is used elsewhere because its performance is slightly higher and the authors describe it as smaller and less demanding of GPU video memory. [p. 7, §§5.1–5.2]

Multimodal agents include IDEFICS-80B-Instruct, CogVLM, Gemini-Pro, and GPT-4V, identified as gpt-4-1106-vision-preview. One condition receives screenshot + captions + accessibility tree. The other receives screenshot + captions + SoM. JavaScript annotates interactable elements with bounding boxes and IDs, and a textual SoM representation accompanies the annotated screenshot. Both conditions still receive captions; therefore this is not a clean comparison of screenshots against captions with every other component absent. [p. 7, §5.3]

### 7.5 Evaluation

Success is binary and execution based. Information-seeking tasks evaluate a returned string. State-changing tasks inspect the final webpage using a URL and a locator, then apply text/image reward primitives to retrieved content. The URL can be fixed or computed, such as the latest page or order. Locators select objects such as image elements or product-image classes. [pp. 4–6, §3.3, Table 2]

Reward primitives are exact_match, must_include, fuzzy_match, must_exclude, eval_vqa, and eval_fuzzy_image_match. GPT-4-Turbo judges semantic equivalence for fuzzy_match; BLIP-2-T5XL supplies VQA judgments. Image matching uses structural similarity index measure (SSIM) exceeding a threshold t in [0,1]; its concrete task-specific threshold values are not provided in the supplied prose. [pp. 4–5]

### 7.6 Human comparison

Seven college students completed a sample described as one task per template, totaling 230 tasks. Some also helped create tasks, but they were not assigned their own creations. Humans achieved 88.7% overall success. The paper elsewhere reports 314 unique templates, so the relationship between the 230-task sample and all templates is unresolved. The human result should not be described as measured over all 910 tasks. [pp. 5–6]

### 7.7 Experimental settings and reporting gaps

The default viewport is 1280 × 2048, with text observations truncated to 3840 tokens or 15360 characters for Gemini. Shorter-context models such as LLaMA, IDEFICS, and CogVLM instead use 1280 × 720 and 640 tokens. GPT-3.5/GPT-4 use temperature 1.0 and top-p 0.9; Gemini uses 0.9 and 1.0; other models use 0.6 and 0.95. Nucleus sampling is used throughout. Main baselines receive three non-overlapping demonstrations. Multimodal demonstrations include screenshots; text conditions use text/captions as applicable. [pp. 19–20, Appendix F]

Hardware models, exact GPU memory consumption, full software versions, random seeds, repeated-run counts, confidence intervals, and formal significance tests are not reported in the supplied material. The work is prompt-based; it does not report a newly trained agent or benchmark train/validation/test partition. Few-shot example separation is stated, but this is not equivalent to demonstrating the absence of all pretraining contamination.

## 8. Experiments / analyses

| ID | Analysis | Purpose and conditions | Evidence | Main outcome and caveat |
|---|---|---|---|---|
| X1 | Main baseline comparison | Compare text, captions, screenshots/accessibility tree, screenshots/SoM on the benchmark | Table 3, pp. 7–8 | Strongest main agent 16.37%; open models often much lower; viewport/truncation differ across models |
| X2 | Caption-backbone comparison | GPT-3.5 with LLaVA versus BLIP-2 captions | Table 3, §5.2 | 2.75% versus 2.97% overall; no uncertainty interval |
| X3 | Human benchmark | Seven students, 230 sampled tasks, avoid assigning self-created tasks | §4.3, Table 3 | 88.70%; human sample differs from full agent task set |
| X4 | Main task-subset analysis | GPT-4V + SoM on OCR, exact-match, and image-input subsets | Table 4, p. 9 | OCR 13.4%, exact match 18.9%, image inputs 19.0%; subsets are observational groupings |
| X5 | Later-model comparison | GPT-4o, Gemini 1.5 variants with SoM; captioned Llama-3 | Table 5, Appendix B | GPT-4o 19.78%; added after submission deadline |
| X6 | Few-shot prompting | Multimodal Gemini-Pro, accessibility tree + captions + image, 0/1/3 examples | Table 6, Appendix C.1 | Overall 2.86/3.63/6.04%; Table 6 has site values inconsistent with Table 3 |
| X7 | Difficulty analysis | GPT-4 text, GPT-4 captions, GPT-4V SoM across visual/action difficulty | F6, Appendix C.2 | Hard-visual aggregate 4.8/8.0/12.4%; not every cell follows a monotonic trend |
| X8 | Extended subset comparison | Four representation conditions each for Gemini and GPT families | F7–F9, Appendix C.3 | Family-dependent OCR/exact-match/image-input trends; unlabeled bars permit approximate reading only |
| X9 | Trajectory length | GPT-4V SoM completion outcomes grouped by trajectory length | F10, Appendix C.3 | Many short trajectories; longer execution does not consistently raise success |
| X10 | Qualitative failure analysis | Selected shopping/classifieds examples and phone-number trace | Appendix C.4, F11–F12 | Undoing work, wrong spatial selection, premature stopping, loops, input append errors |
| X11 | Qualitative agent comparison | Keyboard post, Pittsburgh image, Pixel-phone comment | Appendix C.5, F13 | Visual detail and direct grounding explain selected differences; cases do not quantify prevalence |

The manipulated variables in X1/X2/X5/X6 are model, representation, caption backbone, or demonstration count. Task difficulty, OCR requirements, exact-match requirements, input-image presence, and realized trajectory length are grouping variables, not randomized interventions. All success comparisons lack reported uncertainty measures in the supplied tables. Qualitative cases illustrate mechanisms but are not an exhaustive statistical taxonomy of failures.

## 9. Results

**[A] Visual information helps strong agents under these configurations.** GPT-4 improves from 7.25% with text to 12.75% with captions; GPT-4V with screenshots reaches 15.05%. **[C]** The differences are 12.75 − 7.25 = **5.50 percentage points**, and 15.05 − 12.75 = **2.30 percentage points**. These are benchmark-success differences, not security-risk reductions. [pp. 7–8, Table 3]

**[A] SoM improves GPT-4V overall, but not uniformly across environments or models.** GPT-4V increases from 15.05% to 16.37%, a **[C] 1.32 percentage-point** gain. Classifieds increases from 8.12% to 9.83%, Reddit from 12.38% to 17.14%, and Shopping decreases from 19.74% to 19.31%. Their **[C]** changes are +1.71, +4.76, and −0.43 percentage points. Gemini-Pro decreases overall from 6.04% to 5.71%; CogVLM is unchanged at 0.33%; IDEFICS rises from 0.77% to 0.99%. The prose on page 8 reverses the site associations of the two GPT-4V gains; Table 3 identifies the conditions explicitly. [p. 8]

**[A] The human gap remains large.** Main GPT-4V SoM scores 16.37% versus humans at 88.70%. **[C]** The difference is 88.70 − 16.37 = **72.33 percentage points**, subject to the different human sample. GPT-4o's later result is 19.78%, leaving **[C] 68.92 percentage points** to the reported human value, again not a matched-task statistical comparison. [pp. 6, 8, 13]

**[A] OCR is relatively difficult for GPT-4V SoM.** OCR-required tasks score 13.4% versus 16.9% without OCR. **[C]** Difference: 13.4 − 16.9 = −3.5 percentage points. Multimodal GPT-4 improves OCR success over caption-only input from 6.4% to 12.2% in the appendix. These findings concern completion on OCR-associated tasks, not isolated character-recognition accuracy. [pp. 9, 14]

**[A] Exact-match and image-input tasks are not the hardest subsets for GPT-4V SoM.** Exact-image-match tasks score 18.9% versus 16.2%; image-input tasks score 19.0% versus 14.9%. **[C]** Differences are +2.7 and +4.1 percentage points. The authors suggest exact image matching is not a primary bottleneck and that some image-input tasks become tractable once understood. This does not establish that image input itself causally makes a task easier. [p. 9, Table 4]

**[A] Newer appendix models improve results.** GPT-4o reaches 19.78%; Gemini-Pro-1.5 11.98%; Gemini-Flash-1.5 6.59%; caption-augmented Llama-3-70B-Instruct 9.78%. **[C]** GPT-4o exceeds main GPT-4V SoM by 19.78 − 16.37 = **3.41 percentage points**. Thus the introduction's approximately 16.4% best-agent statement must be read as the main experiment, not the best result anywhere in the final supplied paper. [p. 13, Table 5]

**[A] Increased demonstrations improve Gemini's overall reported score.** Zero, one, and three examples yield 2.86%, 3.63%, and 6.04%. **[C]** Zero-to-three gain: 6.04 − 2.86 = **3.18 percentage points**. Reddit does not improve monotonically: 2.38%, 1.43%, 4.29%. The experiment does not test fine-tuning, despite the authors suggesting it as future work. [p. 13, Table 6]

**[A/B] Important mistakes occur even on apparently easy tasks and after partial success.** Agents select the wrong row/color, abandon tasks when a control merely requires scrolling, alternate between tabs, append text instead of replacing it, and undo a correct wishlist action. These show fragile end-to-end execution. **[D]** They are relevant to security assurance because operational errors can affect persistent state, but none is evidence of an adversarial attack. [pp. 15–19]

## 10. Figure-by-figure interpretation

### Figure 1 — Benchmark overview, p. 2

**[B]** A left block depicts the three sites and knowledge/resources/tools. A central block pairs webpages with three natural-language task specifications, two containing image references. Arrows lead to an LLM/VLM agent and an example click action. There are no axes, quantitative scale, or error bars. The diagram connects website observations and task specifications to action generation. **[A]** The caption identifies 910 realistic visually grounded tasks. It does not depict an attacker or a security boundary.

### Figure 2 — SoM observation and action grounding, p. 4

**[B]** The original Reddit-style page becomes an annotated screenshot with colored boxes and IDs. A text block lists element IDs, tags, and content; the agent receives this plus a target-image objective and produces click [31]. Arrows indicate preprocessing followed by action selection. The visual supports the mechanism of explicit element grounding, not an isolated quantitative proof of improvement. Miniature page details are compressed; the annotation structure and action are readable.

### Figure 3 — Successful Reddit blocking trajectory, p. 8

**[A/B]** The task is to block the author of a specified image from hot posts in /f/memes. The panels show the homepage, an initial search, the forum list, the correct forum, the author's profile, the block button, and confirmation. Red commands mark the selected actions. This is a multi-step successful example involving exact image matching and a persistent user-account action. No axes or rates are present. The authors describe recovery after the initial search fails. It demonstrates one trace, not the frequency of successful recovery.

### Figure 4 — Site distribution, p. 12

**[B]** A pie chart uses labeled slices: Shopping 50.9%, Classifieds 25.5%, Reddit 18.7%, Multi-Site 4.9%. Colors distinguish slices; no axes or uncertainty intervals are shown. These are task-set shares, not per-site success rates. **[C]** The displayed percentages sum to 100.0%. The multi-site category means these shares should not be directly substituted for the evaluation-column denominators in Table 3.

### Figure 5 — Joint difficulty distribution, p. 12

**[B]** A bubble matrix places visual difficulty on the horizontal axis and action difficulty on the vertical axis, each with easy/medium/hard categories. Circle size and color visually distinguish cells; exact percentages are labeled. For action easy, the visual easy/medium/hard shares are 15.7/12.9/4.2%; for action medium, 13.7/12.6/8.5%; for action hard, 7.0/10.5/14.8%. Units are percentages of all tasks. No confidence intervals are shown. **[C]** Their sum is 99.9%, consistent with rounded display values, without proving exact underlying counts.

### Figure 6 — Difficulty and trajectory heatmaps, p. 14

**[B]** Panels a–c are success-rate matrices for GPT-4 text, GPT-4 captions, and GPT-4V SoM. Rows are action difficulty; columns are visual difficulty; aggregate rows/columns are included. Panel d shows trajectory lengths for GPT-4V SoM rather than percentages. Green shading in success panels encodes larger rates; numerical labels carry the exact displayed values. No error bars or tests are shown.

The visual-difficulty aggregate rates, easy/medium/hard, are 9.0/7.3/4.8% for text; 16.9/12.2/8.0% for captions; and 21.4/14.3/12.4% for SoM. Action-difficulty aggregates are 14.8/4.7/2.4%, 20.1/10.4/7.8%, and 25.8/12.9/10.5%, respectively. SoM trajectory averages by action difficulty are 6.9, 10.0, and 12.1, with 9.6 overall. Individual cells are not uniformly monotonic; the paper's statement concerns general trends. Full cell values are preserved below in the numerical reference section.

### Figure 7 — OCR subset bars, p. 15

**[B]** Grouped bars compare eight agent conditions: Gemini-Pro and GPT-family text-only, captions, multimodal, and SoM. The horizontal axis names conditions; the vertical axis is success rate with percentage ticks on a linear scale. Coral indicates no OCR, turquoise OCR. GPT-family OCR bars are lower than their no-OCR partners; Gemini multimodal and SoM show the opposite relation. No error bars are visible. Exact bar values are mostly unlabeled, so numerical interpretation is restricted to Table 4 and the appendix prose rather than invented decimals.

### Figure 8 — Exact-image-match subset bars, p. 16

**[B]** The same eight conditions are grouped by exact-match requirement. Coral means exact match, turquoise no match; the vertical axis is linear percentage success. Gemini exact-match bars are visibly lower than no-match bars. GPT-4V SoM's exact-match bar is higher; GPT-4V multimodal bars are nearly equal visually. The text generalizes that other GPT variants are relatively worse on exact match, so the near-equal multimodal pair should not be overinterpreted. Unlabeled bar heights are not exact source numbers.

### Figure 9 — Image-input subset bars, p. 17

**[B]** Coral bars represent at least one objective image; turquoise bars represent no input image. Axes and model conditions parallel Figures 7–8. GPT captions, multimodal, and SoM perform better on image-input tasks; GPT text-only does worse. Gemini generally does worse with objective images. This supports the authors' discussion of interleaved image/text handling but does not experimentally isolate the cause. Exact values for GPT-4V SoM are 19.0% and 14.9% in Table 4; other bars are not assigned precise values here.

### Figure 10 — Trajectory length and outcomes, p. 18

**[B]** The upper panel is a grouped count histogram: horizontal trajectory length runs from 0 to 35, vertical count from 0 to roughly 250 with the tallest failure bar above that tick. Orange indicates pass and blue fail. Exact count labels are absent. The lower panel is a 100% stacked outcome plot with the same length axis and percentage vertical axis. Seven consecutive bins display pass shares 22.0%, 11.4%, 16.0%, 14.7%, 10.8%, 21.1%, and 9.9%; corresponding fail shares are 78.0%, 88.6%, 84.0%, 85.3%, 89.2%, 78.9%, and 90.1%.

The count panel shows many short executions; the share panel shows no monotonic success improvement with length. Exact bin-boundary inclusion conventions and underlying counts are not specified. The authors' inference that agents assume tasks can be completed quickly is stronger than the directly observable fact that they often terminate quickly; it is retained as their interpretation. [p. 15]

### Figure 11 — Easy spatial-selection task, p. 18

**[B]** A shopping grid supplies the starting page for selecting the red item in the second row. The image shows products distributed across rows and columns. There are no analytical axes or rates. **[A]** The surrounding text reports that GPT-4V multimodal and SoM instead selected a blue tablecloth in the first row, and none of the benchmarked agents completed the task. This links spatial/visual grounding to a concrete failure. Tiny product text is not confidently readable and is not reconstructed.

### Figure 12 — Failed account-phone update, p. 19

**[A/B]** Two starting tabs contain Shopping and a Wikipedia country-code map. The trace moves through account/address editing, creates an unused blank tab, switches to the map and back, types into the phone field, and repeatedly submits/retakes an action. Red commands and black step labels encode the sequence and loop. The task is to prepend South Korea's country code. A step label says +816505551212, while the adjacent red command says +826505551212; both are visible and are not silently reconciled. Appendix C.4 attributes failure to appending rather than replacing text and repeated actions. The diagram also uses page_focus where Table 1 describes tab_focus. These inconsistencies limit command-level reconstruction.

### Figure 13 — Successful Classifieds comment, p. 21

**[A/B]** The agent searches for a white Google Pixel phone, filters to cell phones, changes to list view, selects a listing, types a comment title and an offer of $250, and posts it. The objective requires an offer $10 below the asking price. The title action appears twice, at steps 5 and 6. Thus a successful trace can include redundant actions; the caption's more-efficient-navigation interpretation is not a proof of minimal execution. Small listing details are not used to independently reconstruct all search/order decisions.

### Figure 14 — Classifieds homepage, p. 22

**[B]** The interface contains a keyword search box, category selection, search button, latest-listing image grid, category icons, location links, and account/publishing controls. It illustrates why pictures, layout, and text jointly matter. This is an interface screenshot, not an evaluation plot. Individual sample listing prices are incidental interface content and are deliberately not transcribed as research results.

### Figure 15 — Classifieds listing detail, p. 23

**[B]** A Nintendo Switch example includes an image, displayed 270.00 $ price, publication/location metadata, publisher contact panel, related listings, and comment/review fields with a submission button. It shows the interface's state-changing affordances. The sample price is illustrative page content, not agent performance. No security effectiveness is measured by this screenshot.

### Figure 16 — SoM system message, p. 24

**[A/B]** The boxed prompt lists the objective, screenshot with ID/color correspondence, textual observation, URL, tabs, and prior action. It specifies page operations, tab management, URL navigation, and stopping. Typing normally presses Enter; an additional argument can disable this. Instructions request one valid action per step and an explicit action format. It includes sandbox homepage/password-page information. The figure is inspected as an experimental artifact only. Table 1's tab_close and this figure's close_tab differ, an unresolved naming inconsistency.

### Figure 17 — Three in-context examples, p. 25

**[A/B]** Examples demonstrate answering a fax-machine price ($279.49), entering a Reddit comments page, and searching Classifieds for guitars. The page contains observation IDs, objectives, prior actions, model reasoning, and actions. The caption says screenshots are appended to each example-user turn, but those actual demonstration screenshots are not shown separately here; the text identifies their intended presence. A substantive inconsistency occurs in the Reddit example: the requested croissant post's comments are ID [16], but the assistant emits click [11], associated with the other post's comments. This is visible in both text and image and cannot be treated as a correct demonstration without qualification.

## 11. Table-by-table interpretation

### Table 1 — Action vocabulary, p. 3

The table lists 12 action types: click [elem], hover [elem], type [elem] [text], press [key_comb], new_tab, tab_focus [index], tab_close, goto [url], go_back, go_forward, scroll [up|down], and stop [answer]. Rows define browser operations; there are no units, baselines, or statistical measures. The table is central to understanding why this is an action-taking system: model outputs can manipulate the browser or provide the final answer. Naming differs in later prompt/trajectory figures as disclosed above.

### Table 2 — Execution-reward examples, p. 6

Four rows pair task examples with evaluation code. Buying the least expensive red blanket checks a latest-order URL and inclusion of product ID B0983XCYK6 and Red. Adding clothing like an objective image checks the wishlist image using VQA questions for polo shirt and green. Posting provided images uses fuzzy image matching. Changing a white-car listing checks inclusion of $25000 or $25,000 and exclusion of $30000 or $30,000 at a specified listing URL. These examples explain how visual and textual criteria become binary rewards. They are not observed model outcomes, and the displayed primitives alone should not be assumed to document every logical check in the complete task implementation.

### Table 3 — Main baseline success, p. 8

Rows represent backbone/representation combinations; columns are Classifieds, Reddit, Shopping, and Overall success percentages. Higher is better. The table has no confidence intervals, p-values, or repeated-run dispersion. Dashes in backbone fields mean no listed component, not zero success. Model-family grouping and the merged visual-backbone column require reading the headers with §5; multimodal configurations still include captions. All rows are preserved here:

| Type / Backbone | Classifieds % | Reddit % | Shopping % | Overall % |
|---|---:|---:|---:|---:|
| Text / LLaMA-2-70B | 0.43 | 1.43 | 1.29 | 1.10 |
| Text / Mixtral-8x7B | 1.71 | 2.86 | 1.29 | 1.76 |
| Text / Gemini-Pro | 0.85 | 0.95 | 3.43 | 2.20 |
| Text / GPT-3.5 | 0.43 | 0.95 | 3.65 | 2.20 |
| Text / GPT-4 | 5.56 | 4.76 | 9.23 | 7.25 |
| Captions BLIP-2 / LLaMA-2-70B | 0.00 | 0.95 | 0.86 | 0.66 |
| Captions BLIP-2 / Mixtral-8x7B | 1.28 | 0.48 | 2.79 | 1.87 |
| Captions LLaVA / GPT-3.5 | 1.28 | 1.43 | 4.08 | 2.75 |
| Captions BLIP-2 / GPT-3.5 | 0.85 | 1.43 | 4.72 | 2.97 |
| Captions BLIP-2 / Gemini-Pro | 1.71 | 1.43 | 6.01 | 3.85 |
| Captions BLIP-2 / GPT-4 | 8.55 | 8.57 | 16.74 | 12.75 |
| Multimodal / IDEFICS-80B-Instruct | 0.43 | 0.95 | 0.86 | 0.77 |
| Multimodal / CogVLM | 0.00 | 0.48 | 0.43 | 0.33 |
| Multimodal / Gemini-Pro | 3.42 | 4.29 | 8.15 | 6.04 |
| Multimodal / GPT-4V | 8.12 | 12.38 | 19.74 | 15.05 |
| SoM / IDEFICS-80B-Instruct | 0.85 | 0.95 | 1.07 | 0.99 |
| SoM / CogVLM | 0.00 | 0.48 | 0.43 | 0.33 |
| SoM / Gemini-Pro | 3.42 | 3.81 | 7.73 | 5.71 |
| SoM / GPT-4V | 9.83 | 17.14 | 19.31 | 16.37 |
| Human sample | 91.07 | 87.10 | 88.39 | 88.70 |

Among agents, GPT-4V SoM has the highest overall, Classifieds, and Reddit main-table results, while GPT-4V without SoM has the highest Shopping result. CogVLM's two conditions tie for the lowest overall value, 0.33%. Captions reduce LLaMA-2 overall success from 1.10% to 0.66%, so visual augmentation does not universally improve every model. Human values exceed all agent rows but are based on a different sampled evaluation.

### Table 4 — GPT-4V SoM task subsets, p. 9

| Subset | Share of tasks % | Success % |
|---|---:|---:|
| OCR required | 17.1 | 13.4 |
| No OCR required | 82.9 | 16.9 |
| Exact image match | 8.7 | 18.9 |
| No exact image match | 91.3 | 16.2 |
| Image inputs | 25.2 | 19.0 |
| No image inputs | 74.8 | 14.9 |

Each pair partitions tasks along a different attribute; the three positive subsets are not stated to be mutually exclusive. No interval or significance measure is supplied. Differences can reflect task composition as well as the named capability.

### Table 5 — Later backbones, p. 13

| Backbone / Condition | Classifieds % | Reddit % | Shopping % | Overall % |
|---|---:|---:|---:|---:|
| Llama-3-70B-Instruct / captions | 7.69 | 5.24 | 12.88 | 9.78 |
| Gemini-Flash-1.5 / SoM | 3.85 | 4.76 | 8.80 | 6.59 |
| Gemini-Pro-1.5 / SoM | 5.98 | 12.86 | 14.59 | 11.98 |
| GPT-4o / SoM | 20.51 | 16.67 | 20.82 | 19.78 |

GPT-4o leads all columns within this table. Its Reddit score, 16.67%, is lower than main-table GPT-4V SoM's 17.14%, despite the higher overall result. The appendix provides Gemini preview identifiers ending in 0514. It does not give statistical uncertainty or a matched standalone-model test.

### Table 6 — Number of demonstrations, p. 13

| Examples | Classifieds % | Reddit % | Shopping % | Overall % |
|---:|---:|---:|---:|---:|
| 0 | 4.29 | 2.38 | 0.43 | 2.86 |
| 1 | 5.36 | 1.43 | 2.14 | 3.63 |
| 3 | 8.15 | 4.29 | 3.42 | 6.04 |

This uses multimodal Gemini-Pro with image + captions + accessibility tree. One-shot uses the demonstration from the corresponding environment. GPT-4V is excluded because the authors describe it as prohibitively expensive. The three-shot overall matches Table 3, but Classifieds and Shopping values are swapped between the two tables: Table 3 gives 3.42/8.15, Table 6 gives 8.15/3.42. The supplied work does not establish which site-specific reporting is correct.

## 12. Diagram / architecture interpretation

The operational architecture has three linked flows. **[A/B] Observation flow:** user objective and optional images combine with the current browser's URL, tab list, and focused-page representation. Depending on condition, that representation is an accessibility tree, captions added to the tree, a screenshot plus the tree, or an annotated screenshot plus textual SoM. Figures 1–2 show this flow; Figure 16 specifies the prompt fields.

**[A/B] Control flow:** the model emits one browser action, such as click, type, scroll, change tab, or navigate. The browser environment transitions to a new state; a new partial observation is returned; the process repeats until stopping or another stopping condition. Table 1 defines the action vocabulary. Figures 3, 12, and 13 show concrete sequences, including recovery, loops, and redundant steps.

**[A] Evaluation flow:** after task execution, the evaluator checks a final answer or extracts relevant final-page state using URLs and locators. Text checks, semantic judgments, visual questions, or image similarity determine binary reward. Table 2 shows example evaluators. The evaluator is a separate correctness mechanism, not merely the agent's declaration that it succeeded.

**[D] Security interpretation:** This architecture connects perception to consequential browser actions through a repeated feedback loop. A standalone response-generating model comparison would need to account for those additional interfaces and effects. The paper supplies the architectural ingredients for such analysis, but no malicious input path, attack diagram, defense module, or measured trust-boundary violation.

## 13. Equations and mathematical concepts

### E1 — Environment tuple, p. 3, §3

The paper writes **E = (S, A, Ω, T)** and describes it as a partially observable Markov decision process (POMDP). S is the set of environment states; A the set of allowed actions; Ω the set of observations; T the state-transition function. In ordinary language, the environment has an underlying condition, the agent sees only part of it, and the chosen action changes that condition. The tuple is reproduced as supplied; no additional conventional POMDP components are silently inserted.

### E2 — Deterministic transition, p. 3

**T: S × A → S.** The Cartesian product S × A means a state/action pair is the input; the output is a resulting state. At time t, action a_t ∈ A is conditioned on observation o_t ∈ Ω and produces state s_(t+1) ∈ S and observation o_(t+1) ∈ Ω. Determinism describes the environment transition conditional on a state and action; it does not imply deterministic model outputs, particularly because the settings use sampling.

### E3 — Binary task reward, pp. 3–6

**R: S × A → {0,1}.** The final task receives 1 if state transitions align with the task objective, otherwise 0. S and A retain their meanings; R is the reward function. The paper alternates R and r(s,a) in table notation. Its prose describes checking final state or final output with task-specific functions. It does not fully formalize how every possible trace property is encoded within a state/action pair, so no stronger mathematical equivalence is assumed.

### E4 — Exact match, p. 4

**exact_match = 1{â = a*}.** Here â is the model's returned answer and a* the ground-truth answer. The indicator is 1 when the strings exactly match and 0 otherwise. It suits exact numerical or textual responses. This is an evaluation rule, not a training loss or optimization objective.

### E5 — Inclusion/exclusion and semantic checking, p. 4

must_include returns 1 when every required element in a* occurs in â. must_exclude returns 0 if any prohibited element occurs, otherwise 1. For fuzzy_match, a judging LLM labels semantic equivalence correct, incorrect, or partially correct; only correct receives reward 1. The paper's footnote explicitly excludes non-binary rewards. These functions distinguish exact equality from containment and judged equivalence.

### E6 — Visual-question evaluation, p. 4

A VLM receives an image and question; reward is 1 if its output contains the required ground-truth answer. The supplied example checks whether clothing is a green polo shirt. This is an evaluator-mediated operational definition of visual correctness, not a proof that every image property is recognized accurately.

### E7 — Fuzzy image similarity, p. 5

**SSIM(query image, ground-truth image) > t**, with **t ∈ [0,1]**, yields reward 1. SSIM is expanded as structural similarity index measure. The work names the measure but does not supply its internal equation, parameterization, preprocessing, or concrete thresholds in the available description. Those details cannot be filled from outside knowledge.

No optimization equation, trained loss, theorem, lemma, or proof is presented. The mathematical contribution is an environment/evaluation formalization rather than a new theoretical result.

## 14. Interpretation and discussion

The strongest supported conclusion is about integrated capability: visual information and direct grounding improve certain strong models, yet end-to-end web tasks remain difficult. Merely interpreting an image is insufficient if the agent then selects the wrong control, stops early, loops, or reverses a correct action. Conversely, some exact-image-match tasks score higher than non-match tasks, demonstrating that a task attribute should not automatically be equated with overall difficulty. [Tables 3–4; Appendix C]

For O1–O3, the benchmark and baseline tables provide direct evidence of a capability gap and representation-sensitive outcomes. For O4, GPT-4V's overall SoM improvement supports the approach under the reported configuration, but Shopping decreases slightly and other backbones do not reliably improve. The authors' spatial-disambiguation explanation is plausible and illustrated, but not isolated by a controlled ablation of visual density. For O5, subset analyses and qualitative traces expose several bottlenecks, with causal explanations remaining tentative.

### Cross-reference and consistency findings

1. **Site-gain reversal:** Page 8 prose associates 12.38→17.14 with Classifieds and 8.12→9.83 with Reddit; Table 3 places these under Reddit and Classifieds respectively. Both are reported; numerical explanations here use the table's explicit headers.
2. **Human/template counts:** Page 5 reports 314 unique templates; page 6 says one task per template gives a 230-task human set. The template subset or sampling change is not explained.
3. **Few-shot site values:** Table 6's three-shot Gemini Classifieds/Shopping values are 8.15/3.42, while Table 3 gives 3.42/8.15. Overall is 6.04 in both. No reconciliation is invented.
4. **Prompt demonstration mismatch:** Figure 17's croissant objective points to comments ID [16], but its example action clicks [11], which belongs to the other post.
5. **Phone trace mismatch:** Figure 12's step description contains +81 while adjacent action text contains +82. The action labels and step captions disagree.
6. **Command naming:** Table 1 uses tab_close; Figure 16 uses close_tab; Figure 12 displays page_focus whereas the formal action vocabulary uses tab_focus. Their implementation equivalence is not established.
7. **Precision changes:** Main-table GPT-4V SoM 16.37% becomes 16.4% in Figure 6/introduction; humans 88.70% become 88.7%. These are disclosed display precision changes. Figure 6's caption-agent overall is 12.7%, whereas Table 3 is 12.75%; the rounding convention is not supplied.
8. **Main versus appendix best result:** The main claim of 16.4% is superseded as an all-document maximum by Appendix B's 19.78% GPT-4o result. These are different experiment cohorts, not evidence of a contradiction in the same run.

### Relevance to the user's security question

**[D]** Four mechanisms are relevant hypotheses: broader observation channels; action authority over persistent state; cross-page/tab execution with memory requirements; and compounding errors over multiple steps. The paper visibly instantiates all four architectural features and illustrates operational mistakes involving them. **[A]** Its ethical discussion acknowledges potential for greater harm than regular LLMs without safeguards. Nevertheless, harm potential is not identical to attack susceptibility, and operational unreliability is not a measured attack success rate. No security ranking between agent and standalone LLM is established.

## 15. Contributions and novelty

**Benchmark/dataset [A]:** 910 newly curated visually grounded tasks with 314 intent templates, including image objectives and unachievable cases.

**System/environment [A]:** A new Classifieds site with 65,955 listings, integrated with inherited Shopping/Reddit environments and knowledge-base access in some tasks.

**Methodological [A]:** Execution-based visually grounded evaluation, including visual question answering, fuzzy image matching, and prohibited-output exclusion, alongside existing text-checking ideas.

**Agent/interface [A]:** A SoM-inspired observation/action representation generated with JavaScript, connecting numbered visible elements to browser actions. The paper credits prior SoM work; it does not claim to invent the general prompting idea.

**Experimental/empirical [A]:** Comparisons across agent families, human performance, later models, prompting counts, difficulty, task subsets, trajectory lengths, and qualitative failures.

**Novelty qualification [A]:** The authors state that, to their knowledge, they are first to systematically benchmark similar representations in a realistic interactive web environment. That priority claim is not externally verified here. No new security attack, defense, adversarial benchmark, mathematical theorem, or agent-training algorithm is demonstrated.

## 16. Limitations

### Authors' stated limitations and caveats

- Current agents perform far below humans, and the paper describes their capabilities as insufficient even for simple tasks. [pp. 7–9]
- Text-only inputs and captions can fail to preserve essential visual details, including fine text or non-salient information. [pp. 7–8, 17–18]
- SoM does not substantially improve every tested VLM; the authors tie this to differences in grounding capability. [p. 8]
- OCR can be a bottleneck for GPT-4V SoM; handling interleaved inputs remains a requirement for stronger agents. [pp. 9, 14]
- Difficulty annotation can deviate because of human judgment and varying emphasis on visual versus reasoning challenges. [p. 6]
- Rewards are binary; non-binary reward scales are left to future work. [p. 4, footnote 2]
- More advanced text-agent prompting is left for future work. [p. 7]
- GPT-4V cost prevents its use in the few-shot example-count analysis. [p. 13]
- Qualitative executions reveal undoing correct work, premature stopping, easy-task errors, loops, and repeated text appending. [pp. 15–17]
- Models are research prototypes intended for a sandbox, not practical deployment in their current state, particularly high-risk domains. Bias, harmful behavior, employment, and safeguards need further investigation. [p. 9]

### Additional evidence-based analyst observations [D]

- Human and agent results are not reported on the same full task set, limiting direct comparison.
- Co-author task creators and a narrow set of site types may shape task selection; template instantiations are not all independent task designs.
- Viewport and truncation differ across backbones, so model-capability differences are mixed with available-observation differences.
- Model-mediated semantic/VQA rewards may introduce evaluation error; judge agreement with human correctness is not reported.
- No confidence intervals, repeated-run variation, significance tests, or random seeds are supplied, despite sampling-based decoding.
- The paper contains the specific text/table/prompt inconsistencies listed in §14.
- No adversarial condition, security outcome, standalone-model control, or protection mechanism is measured.
- All figures are inspected, but tiny webpage details cannot be fully transcribed; missing external implementations prevent source-level reconstruction.

These are observations from the supplied evidence, not limitations the authors necessarily named.

## 17. Threats to validity

The following validity labels are analyst framing [D]. **Internal validity:** Model, observation representation, viewport, context truncation, and decoding vary across comparisons. This limits attributing every difference exclusively to multimodality or model architecture. The few-shot study holds a narrower configuration fixed, but site-specific reporting inconsistencies remain.

**Construct validity:** Binary task completion operationalizes successful web interaction, not general intelligence, isolated visual perception, or adversarial security. A semantically correct action sequence that misses one required final detail can fail, while a successful trace may contain redundant actions. LLM/VLM evaluators and string containment provide practical checks but are not independently validated in the supplied work.

**Statistical conclusion validity:** Rounded rates without uncertainty or repeated-run information limit conclusions about small differences. Words such as significantly in the paper should not be interpreted as evidence of a reported statistical significance test. Template-derived tasks may share structure, and subset comparisons are observational.

**External/ecological validity:** Real-world-derived content and familiar site interfaces support realism, but three self-hosted applications with deterministic transitions do not represent the full changing internet or live commercial deployment. Regional Classifieds data and student annotators/participants further bound generalization. Realism of benign workflows does not establish realism of an attacker model.

**Reproducibility:** Self-hosting, prompts, model identifiers, viewports, and decoding settings aid reconstruction. Missing implementation inspection, SSIM thresholds, seeds, hardware/software detail, exact trajectory stopping limit, and judge-validation detail prevent a complete reproduction from this document alone.

**Security validity:** The study cannot support a claim that browser agents suffer a particular attack more often than standalone LLMs. Such a conclusion would require a defined attack, matched conditions, security metrics, and appropriate controls that are absent here.

## 18. Future work and open questions

### A. Explicitly proposed by the authors

The authors propose improving reasoning, visual understanding, and planning; exploring non-binary rewards; using more advanced prompting; fine-tuning on web trajectories; better tracking past states and execution history to reduce loops; testing stronger models for OCR and interleaved inputs; and expanding error analysis. They suggest the easy subset can provide development signal for weaker models, conditional on correlations with stronger-agent performance. Their ethical section calls for research on bias, harmful behavior, safeguards, and broader social effects. [pp. 4, 6–7, 9, 13–16]

### B. Additional open questions [D]

How much of SoM's gain comes from direct visual grounding versus the accompanying textual representation? Would matched viewport/context budgets change rankings? How reliable are model-mediated evaluators against human judgments? How variable are outcomes across decoding runs? How should the 230-task human sample be reconciled with 314 templates? Can demonstrations be corrected and their effect measured? Which memory mechanisms prevent undoing completed work or repeated appending?

For the user's research question, a further study would need to measure whether encountered text or images can redirect actions away from the user's objective, what persistent effects result, and how those outcomes differ from a standalone-model control. Those are proposed research questions, not attack results in this paper.

## 19. Terminology and notation glossary

| Term / Symbol | Beginner-friendly meaning in this paper |
|---|---|
| Visual grounding | Connecting instructions/actions to visual information on a page |
| LLM | Large language model used to generate reasoning text and actions |
| VLM | Vision-language model processing pictures and text |
| Multimodal | Using more than one input modality, principally images and text |
| SoM | Set-of-Marks: boxes and IDs on webpage elements |
| DOM | Document Object Model: tree representation of webpage HTML |
| Accessibility tree | Simplified structured page representation for assistive technologies |
| HTML | Webpage markup referenced by the paper; img identifies image elements |
| Caption | Text description generated from an image |
| Alt-text | Image-associated text field enriched with generated captions here |
| OCR | Optical character recognition: reading text in images |
| VQA | Visual question answering: checking an image through a question/answer |
| SSIM | Structural similarity index measure used for image comparison |
| POMDP | Partially observable Markov decision process: acting with incomplete observation of state |
| E | Environment tuple (S, A, Ω, T) |
| S, s_t | State set and current underlying state |
| A, a_t | Action set and action at step t |
| Ω, o_t | Observation set and observation at step t |
| T | Deterministic state-transition function |
| R or r(s,a) | Binary task reward |
| â, a* | Model answer and ground-truth answer/required content |
| 1{condition} | Indicator: one if the condition holds, zero otherwise |
| t in SSIM threshold | Similarity threshold; distinct from the time-step index by context |
| Locator | Rule selecting page content for evaluation |
| Trajectory | Sequence of observations/actions during task execution |
| In-context example | Demonstration included in a model prompt |
| Top-p / nucleus sampling | Decoding setting named in the paper; its algorithm is not derived there |
| Temperature | Model-output sampling setting; concrete values appear in Appendix F |
| Viewport | Browser image dimensions available to the agent |
| PII | Personally identifiable information redacted from collected listings |
| CMS | Content management system; OSClass supports the Classifieds site |
| Success rate / SR | Percentage of evaluated tasks awarded successful completion |
| Percentage point | Difference between two percentage-valued rates |
| Unachievable task | Task for which appropriate behavior is to stop and explain impossibility |

## 20. Key numerical results

Values below are exact reported/displayed values unless explicitly labeled derived. Complete baseline rows appear in §11; plot estimates are deliberately not converted into exact results.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark tasks | 910 | tasks | All curated tasks | Author-reported | p. 1; p. 5 |
| Unique templates | 314 | templates | Task creation | Author-reported | p. 5 |
| Tasks per template | 2.9 | tasks/template | Reported average | Author-reported | p. 5 |
| Task creators | 6 | people | Graduate-student co-authors | Author-reported | pp. 5, 19 |
| Unachievable tasks | 46; 5.1 | tasks; % | Explain inability using fuzzy_match | Author-reported | p. 5 |
| Image-input tasks | 229; 25.2 | tasks; % | Objective includes images | Author-reported | p. 14 |
| Classifieds listings | 65,955 | listings | New environment | Author-reported | pp. 5, 19 |
| Reddit posts | 31,464 | posts | Forum environment | Author-reported | p. 5 |
| Classifieds collection | 3 | weeks | Craigslist scraping | Author-reported | p. 19 |
| Human participants | 7 | people | College students | Author-reported | p. 6 |
| Human task sample | 230 | tasks | Template-sampling description unresolved | Author-reported | p. 6 |
| Human overall success | 88.70 | % | Sampled human evaluation | Author-reported | Table 3, p. 8 |
| GPT-4 text success | 7.25 | % | Accessibility tree | Author-reported | Table 3 |
| GPT-4 caption success | 12.75 | % | BLIP-2 + accessibility tree | Author-reported | Table 3 |
| GPT-4V multimodal success | 15.05 | % | Image + captions + accessibility tree | Author-reported | Table 3 |
| GPT-4V SoM success | 16.37 | % | Image + captions + SoM | Author-reported | Table 3 |
| GPT-4o success | 19.78 | % | Later appendix SoM evaluation | Author-reported | Table 5 |
| Caption gain for GPT-4 | 5.50 | percentage points | 12.75 − 7.25 | Analyst-derived | Table 3 |
| SoM gain for GPT-4V | 1.32 | percentage points | 16.37 − 15.05 | Analyst-derived | Table 3 |
| Later GPT-4o gain | 3.41 | percentage points | 19.78 − 16.37 | Analyst-derived | Tables 3, 5 |
| Main human-agent gap | 72.33 | percentage points | 88.70 − 16.37; different sample | Analyst-derived | Table 3; §4.3 |
| OCR subset performance | 13.4 / 16.9 | % | OCR / no OCR, GPT-4V SoM | Author-reported | Table 4 |
| Exact-match performance | 18.9 / 16.2 | % | Exact / non-exact, GPT-4V SoM | Author-reported | Table 4 |
| Image-input performance | 19.0 / 14.9 | % | Input image / no image, GPT-4V SoM | Author-reported | Table 4 |
| Few-shot overall | 2.86 / 3.63 / 6.04 | % | Gemini-Pro, 0 / 1 / 3 examples | Author-reported | Table 6 |
| Default viewport | 1280 × 2048 | pixels | Main settings | Author-reported | pp. 19–20 |
| Short-context viewport | 1280 × 720 | pixels | Selected shorter-context models | Author-reported | p. 20 |
| Text limits | 3840 / 640 | tokens | Default / shorter-context | Author-reported | pp. 19–20 |
| Gemini text limit | 15360 | characters | Default Gemini observation | Author-reported | p. 20 |
| GPT temperature / top-p | 1.0 / 0.9 | setting | GPT-3.5 and GPT-4 | Author-reported | p. 20 |
| Gemini temperature / top-p | 0.9 / 1.0 | setting | Gemini models | Author-reported | p. 20 |
| Other temperature / top-p | 0.6 / 0.95 | setting | Remaining models | Author-reported | p. 20 |
| Easy / medium / hard action difficulty | ≤3 / 4–9 / ≥10 | human actions | Estimated completion requirement | Author-reported | p. 6 |

For exact Figure 6 coverage, each row below lists visual easy, medium, hard, and overall, in that order. Success rows are percentages; trajectory rows are average lengths as labeled by the figure.

| Figure 6 panel | Action easy | Action medium | Action hard | Overall row |
|---|---|---|---|---|
| a: GPT-4 text success | 18.9, 11.1, 10.5, 14.8 | 1.6, 6.1, 7.8, 4.7 | 1.6, 4.2, 1.5, 2.4 | 9.0, 7.3, 4.8, 7.3 |
| b: GPT-4 caption success | 23.1, 18.8, 13.2, 20.1 | 14.4, 9.6, 5.2, 10.4 | 7.8, 7.3, 8.1, 7.8 | 16.9, 12.2, 8.0, 12.7 |
| c: GPT-4V SoM success | 30.1, 20.5, 26.3, 25.8 | 15.2, 11.3, 11.7, 12.9 | 14.1, 10.4, 8.9, 10.5 | 21.4, 14.3, 12.4, 16.4 |
| d: GPT-4V SoM trajectory | 6.0, 7.7, 6.1, 6.9 | 10.4, 10.6, 7.2, 10.0 | 14.1, 9.2, 12.5, 12.1 | 9.5, 9.4, 10.2, 9.6 |

These values are visually readable and cross-supported by the supplied extraction. They are not uncertainty estimates. Numeric task-example prices, product IDs, telephone strings, and demonstration IDs are explanatory artifacts, not additional benchmark performance observations.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| VisualWebArena evaluates visually grounded web tasks | 910 tasks; three environments; 25.2% image objectives | F1, X1 | pp. 1, 5 | HIGH for what authors constructed/reported |
| Environment supports consequential browser actions | Click/type/navigation plus state inspection | T1–T2, F12–F15 | pp. 3–6, 19, 21–23 | HIGH for supplied interface; no attack established |
| Captions improve GPT-4 completion | 7.25% to 12.75% | T3, X1 | pp. 7–8 | HIGH reported comparison; causal attribution bounded |
| SoM improves main GPT-4V overall | 15.05% to 16.37% | T3, F2, X1 | p. 8 | HIGH rates; no reported significance test |
| SoM is not uniformly beneficial | Shopping decreases; Gemini decreases; CogVLM ties | T3 | p. 8 | HIGH; contradicts an unconditional improvement claim |
| Humans outperform evaluated agents | 88.70% versus 16.37% main / 19.78% later | T3, T5, X3/X5 | pp. 6, 8, 13 | HIGH reported values; unmatched sample limits inference |
| OCR-associated tasks challenge GPT-4V SoM | 13.4% versus 16.9% | T4, F7, X4/X8 | pp. 9, 14–15 | HIGH association; no isolated OCR accuracy test |
| Newer models improve best reported overall score | GPT-4o 19.78% | T5, X5 | p. 13 | HIGH; later cohort, still far below human sample |
| More demonstrations improve Gemini overall | 2.86/3.63/6.04% | T6, X6 | p. 13 | HIGH overall; site values inconsistent with T3 |
| Execution reliability is fragile | Undoing, early stopping, loops, append errors | F11–F13, X10 | pp. 15–21 | HIGH examples; prevalence unquantified |
| Agents may cause greater harm without safeguards | Explicit broader-impact statement | §8 | p. 9 | HIGH author caution; not experimental security evidence |
| Broader security exposure is plausible | Multiple input channels connected to state-changing actions | T1, F1–F2, F12, F16 | pp. 2–4, 19, 24 | MEDIUM analyst inference; vulnerability comparison UNKNOWN |

Verification was source grounded: key model conditions and values were rechecked against the supplied tables and rendered pages; figure interpretations distinguish visible content from captions and author explanations. Inconsistencies were preserved rather than repaired. This is document checking, not independent experimental verification.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to use a browser for you: find a green shirt, identify a picture, or change something in your account. Reading webpage words is only part of the job. The AI also needs to understand pictures, know which button belongs to which item, and remember what it has already done.

This paper builds a test with 910 tasks to measure those abilities. Giving strong AI models pictures helps. Putting numbered boxes around webpage controls helps one of the strongest tested models choose actions more accurately. But even the later best model succeeds on only 19.78% of tasks, while people succeed on 88.70% in a smaller sampled test. The AI sometimes picks the wrong item, quits too early, repeats actions, or undoes something it already did correctly.

For security, the useful lesson is that a browser agent can do things that affect websites and accounts. A mistake can become a changed phone field or an unwanted action, rather than just an incorrect sentence. The authors warn that agents can cause more harm than regular language models without safeguards. However, this paper never tests hackers or compares attacks on browser agents with attacks on standalone models. It gives evidence about capability and mistakes, plus ingredients for a future security study; it does not prove an attack-vulnerability ranking.

## Completeness Audit

The denominator is the inventory in §2 plus all six tables, seventeen figures, formal expressions, experimental analyses, contributions, and limitations identified above. Coverage means substantive representation, not preservation of every sentence or every tiny screenshot label.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 title/authors/venue/abstract | Yes, text and visual | Yes | Represented in compressed form | Title and framing preserved; bibliographic details below |
| S1 Introduction | Yes | Yes | Fully represented substantively | Motivation, task count, contribution claims |
| S2 Related Work | Yes | Yes | Represented in compressed form | Three categories and positioning; citations not independently validated |
| S3 environment formalization | Yes | Yes | Fully represented | E1–E3 and assumptions |
| SS3.1 observations | Yes | Yes | Fully represented | DOM/tree/screenshots/SoM, URLs, tabs, image objectives |
| SS3.2 actions | Yes | Yes | Fully represented | All 12 action types, grounding rationale |
| SS3.3 information-seeking evaluation | Yes | Yes | Fully represented | Equality, inclusion, exclusion, semantic judgment |
| SS3.3 visual evaluation | Yes; p. 5 text-only | Yes | Fully represented with missing implementation detail | VQA/SSIM; thresholds unspecified |
| SS3.3 navigation/state evaluation | Yes; p. 5 text-only | Yes | Fully represented | URLs, locators, final-state checks |
| SS4.1 environments | Yes; p. 5 text-only | Yes | Fully represented | Three principal sites and knowledge base |
| SS4.2 creation/visual grounding | Yes | Yes | Fully represented | Templates, creators, image sources, impossibility cases |
| SS4.2 complexity | Yes | Yes | Fully represented | Action/visual categories, judgment caveat |
| SS4.3 humans | Yes | Yes | Fully represented with uncertainty | Seven participants, 230 tasks, leakage precaution, errors |
| SS5.1 text agents | Yes | Yes | Fully represented | Models, tree, prompting |
| SS5.2 caption agents | Yes | Yes | Fully represented | Caption process and two caption backbones |
| SS5.3 multimodal agents | Yes | Yes | Fully represented | Both input representations, captions, JavaScript |
| S6 main results | Yes | Yes | Fully represented | All T3 rows and model-dependent SoM outcomes |
| SS6.1 task subsets | Yes | Yes | Fully represented | All T4 values |
| S7 conclusion | Yes | Yes | Represented in compressed form | Capability gap and proposed directions |
| S8 Real World Impacts | Yes | Yes | Represented in compressed form | Accessibility, routine work, employment |
| S8 Bias and Safety | Yes | Yes | Fully represented | Bias, safeguards, greater harm caution |
| S8 Intended Uses | Yes | Yes | Fully represented | Sandbox and prototype limits |
| REF bibliography | Yes; p. 11 text-only | Yes, role only | Inspected but deliberately compressed | Individual bibliography entries not reproduced |
| A1 Tasks Breakdown | Yes | Yes | Fully represented | F4 site shares and F5 nine difficulty cells |
| A2 Additional Results | Yes | Yes | Fully represented | All T5 rows and later cohort distinction |
| A3 C.1 Few-shot | Yes | Yes | Fully represented with inconsistency | All T6 values and configuration |
| A3 C.2 Difficulty | Yes | Yes | Fully represented | All F6 cells, panel units, nonmonotonic cells |
| A3 C.3 OCR/exact/image subsets | Yes | Yes | Represented in compressed form | Trends, exact textual values, no invented bar decimals |
| A3 C.3 trajectory analysis | Yes | Yes | Fully represented substantively | F10 shares; exact counts unavailable |
| A3 C.4 longer-horizon failures | Yes | Yes | Represented in compressed form | Wishlist undoing and banana-cart case |
| A3 C.4 easy-task failure | Yes | Yes | Fully represented | Wrong row/color and F11 |
| A3 C.4 early stopping | Yes | Yes | Represented in compressed form | Scrolling/search examples |
| A3 C.4 loops | Yes | Yes | Represented in compressed form | Makeup tabs and phone-field loop |
| A3 C.4 phone-number trace | Yes | Yes | Fully represented with uncertainty | F12, three error categories, label mismatch |
| A3 C.5 agent comparisons | Yes | Yes | Represented in compressed form | Keyboard, Pittsburgh, Pixel-phone cases |
| A4 Classifieds Environment | Yes | Yes | Fully represented substantively | Collection, redaction, functionality |
| A5 Task Collection Process | Yes | Yes | Fully represented substantively | Exploration, familiarity, templates, repetition control |
| A6 Baseline Agent Settings | Yes | Yes | Fully represented | Viewports, truncation, decoding, examples |
| O1–O5 objectives | Yes | Yes | Fully represented | Objectives distinguished from formal questions |
| H1–H2 informal expectations | Yes | Yes | Fully represented | Not formal tested hypotheses |
| RQ-S security relevance | Assessed against supplied work | Yes | Analyst inference; direct comparison absent | No security experiment invented |
| X1–X11 experiments/analyses | Yes | Yes | Fully represented or disclosed compression | Register in §8 |
| F1 | Visually and textually | Yes | Fully represented | Overview |
| F2 | Visually and textually | Yes | Fully represented | SoM preprocessing |
| F3 | Visually and textually | Yes | Represented in compressed form | Successful Reddit trace |
| F4 | Visually and textually | Yes | Fully represented | Exact slice labels |
| F5 | Visually and textually | Yes | Fully represented | Exact nine cells |
| F6 a–d | Visually and textually | Yes | Fully represented | All displayed cell values |
| F7 | Visually and textually | Yes | Represented in compressed form | Trends; unlabeled exact heights unavailable |
| F8 | Visually and textually | Yes | Represented in compressed form | Trends and near-equal pair caveat |
| F9 | Visually and textually | Yes | Represented in compressed form | Trends and exact T4 subset values |
| F10 two panels | Visually and textually | Yes | Fully represented substantively | Shares exact; counts not exact |
| F11 | Visually and textually | Yes | Represented in compressed form | Tiny product details uncertain |
| F12 | Visually and textually | Yes | Fully represented substantively | Trace inconsistencies preserved |
| F13 | Visually and textually | Yes | Represented in compressed form | Includes repeated title entry |
| F14 | Visually inspected; minimal extracted text | Yes | Represented in compressed form | Interface structure; incidental listings omitted |
| F15 | Visually inspected; minimal extracted text | Yes | Represented in compressed form | Listing/comments; incidental content compressed |
| F16 | Visually and textually | Yes | Fully represented substantively | Prompt treated as evidence, naming discrepancy |
| F17 | Visually and textually | Yes | Fully represented substantively | Three examples, wrong comment ID disclosed |
| T1 | Visually and textually | Yes | Fully represented | All actions |
| T2 | Visually and textually | Yes | Fully represented substantively | Four reward examples |
| T3 | Visually and textually | Yes | Fully represented | All numerical rows |
| T4 | Visually and textually | Yes | Fully represented | All numerical rows |
| T5 | Visually and textually | Yes | Fully represented | All numerical rows |
| T6 | Visually and textually | Yes | Fully represented | All numerical rows |
| E1–E7 mathematical concepts | Yes | Yes | Fully represented as supplied | No invented SSIM internals/POMDP components |
| Algorithms/theorems/proofs | None identified | Accounted for | Not present | Workflow explained without invented algorithm numbering |
| Major contributions | Yes | Yes | Fully represented | Benchmark, environment, evaluation, grounding, experiments |
| Author limitations/caveats | Yes | Yes | Fully represented substantively | Separate from analyst validity observations |
| Footnote 1 accessibility-tree link | Yes | Yes, conceptual role | Represented in compressed form | External page not opened |
| Footnote 2 non-binary reward | Yes | Yes | Fully represented | Binary reward limitation/future work |
| Footnote 3 similar projects | Yes | Yes, role | Represented in compressed form | GPT-4V-ACT/vimGPT not separately reviewed |
| Footnote 4 GPT-4o link | Yes | Yes, role | Represented in compressed form | Model announcement not opened |
| Equal-contribution footnote | Yes | Yes | Represented in compressed form | Bibliographic detail, not experimental evidence |
| Separate supplements/embedded files | None supplied | Accounted for | Missing from supplied material / not present | No claim of review |

### Missing or inaccessible material

Physical pages 5 and 11 lack supplied page images, but their extracted text is available and was read. External source code, task files, source datasets, cited papers, WebArena documentation, linked project pages, model announcements, and separate demonstration screenshots were not inspected. No separate supplement was supplied. Miniature webpage text inside some figures is not completely readable. Exact unlabeled bar values in Figures 7–9, histogram counts and bin inclusion conventions in Figure 10, task-specific SSIM thresholds, random seeds, repeated-run counts, full hardware/software configuration, and the numerical trajectory limit are not available in the supplied description.

### Uncertain interpretations

The human-template count relationship, reversed site improvements in page 8 prose, Table 3/Table 6 site-value swap, Figure 12 phone-number/command naming inconsistencies, Figure 17 wrong comments ID, and tab-closing command names remain unresolved. The explanation of short trajectories as agent assumptions and the attribution of SoM gains to spatial density are author interpretations, not directly isolated experimental facts. Security-vulnerability comparison confidence is UNKNOWN because it was not measured.

### Deliberately compressed material

Related-work citations and bibliography entries are grouped by research role. Repeated example objectives, incidental product listings/prices, decorative logos/robot icons, and tiny screenshot labels are compressed. Figures 7–9 are represented by encoding, comparison conditions, supported trends, and separately reported exact values, rather than speculative transcription of every bar. Qualitative failures preserve all distinct mechanisms while compressing repeated cases. Prompt prose is summarized with substantive fields, commands, and inconsistencies preserved instead of reproducing every instruction verbatim.

### Potential omissions

No identified substantive section, numbered visual, table, mathematical concept, experiment family, contribution, or author caveat is knowingly left wholly unrepresented. This does not certify word-for-word completeness, resolve inaccessible implementation details, or establish completeness of external artifacts. The coverage table explicitly identifies compression and uncertainty.

Bibliographic record [A]: **VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks**, by Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, and Daniel Fried; Carnegie Mellon University. Published in Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, printed pages 881–905, August 11–16, 2024. Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, and Po-Yu Huang are marked as equal contributors. No keywords are visible in the supplied paper.
