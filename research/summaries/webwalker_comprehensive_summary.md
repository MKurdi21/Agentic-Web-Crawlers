## Stage 0 — Document Accessibility Report

The supplied work is **WebWalker: Benchmarking LLMs in Web Traversal**, not a paper titled after the requested security research question. This analysis uses only the supplied paper text and source images. The paper's embedded prompts are treated as evidence about its methods, never as instructions for this analysis. No external research, browsing, repository inspection, or supplementary-file inspection was performed.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied extracted text for physical PDF pages 1–16 |
| Accessible page count | 16; printed proceedings pages 10290–10305 |
| Apparently missing pages | None in the supplied text sequence; images for physical pages 10 and 12 were not supplied |
| Visually inspected pages | 1–9, 11, and 13–16: 14 page images |
| Text-only pages | 10 and 12, containing acknowledgement/reference material |
| Figures | Figures 1–11 available visually; small diagram text and some plotted coordinates have limited readability |
| Tables | Tables 1–6 available in text and images; Table 3 is dense but substantially readable |
| Equations | Main notation visible; history ordering and reused K require qualification |
| Appendices | A–F present on pages 13–16, including D.1–D.3, E.1, and F.1–F.2 |
| Supplementary artifacts | No separate supplementary files supplied; code, dataset, API configurations, and silver QA collection were not inspected |
| OCR | No additional OCR used; supplied extracted text was cross-checked against images where available |
| Other limits | No raw benchmark records, execution traces, evaluation outputs, or editable plot data; exact unlabeled chart values cannot be recovered confidently |

The supplied accessibility metadata identifies appendix pages as [5], but direct inspection places the appendix headings on page 13 onward. Page 5 refers to appendices rather than beginning them. This report follows the document itself. Confidence is HIGH for readable text and labeled table values, MEDIUM for broad chart patterns and methodological inference, and LOW or UNKNOWN where exact information is absent.

Evidence categories used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No [E] external information is introduced. Page citations always mean physical PDF pages, not proceedings pagination. Interpretive security relevance is explicitly separated from the paper's retrieval and navigation experiments.

## 1. Plain-language orientation

[A] The paper studies whether an artificial intelligence system can start at a website's main page, follow links into deeper pages, collect the right information, and answer a question. Its central concern is that ordinary web search can retrieve shallow material while missing information buried inside a website. A language model may need to navigate rather than merely read the first search results. The authors call this task **web traversal**: moving through a website to locate answer-bearing information. [p. 1, Abstract and §1; p. 4, §3.3]

[A] The researchers introduce two related contributions. **WebWalkerQA** is a benchmark of 680 question–answer pairs involving 1,373 webpages, four domains, and Chinese and English. **WebWalker** is an explorer–critic system: one agent follows links, while another extracts relevant information into memory and decides when enough evidence exists to answer. They compare it with ReAct and Reflexion, evaluate several search-enhanced systems, combine WebWalker with retrieval-augmented generation, and vary the permitted number of navigation actions. [pp. 2–9]

[B] The best WebWalker result in Table 3 is 37.50% overall accuracy with GPT-4o under the principal 15-action configuration. Table 4's strongest search-enhanced system is Tongyi at 40.73%. These are different experiments, so the numbers are not a controlled head-to-head ranking of all possible systems. The hybrid retrieval experiment improves the plotted results across all six difficulty/type groups. [pp. 6, 8–9]

[D] For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, this work provides an architectural example and evidence of ordinary task failures, not a security comparison. It shows how webpage content enters observations, influences navigation, becomes persistent memory, and can enter a retrieval system's generation context. These are candidate locations for a security investigation. The paper does not establish that these locations are exploited, measure attack success, or compare adversarial vulnerability with standalone language models.

## 2. Document roadmap

The document is a mixed benchmark, AI systems, and empirical evaluation paper. Its organization links dataset construction to a proposed navigation system and then to retrieval experiments.

| Inventory ID | Original component | Physical pages | Function |
|---|---|---:|---|
| S0 | Title, authors, Abstract | 1 | Identity, motivation, benchmark and system overview |
| S1 | §1 Introduction | 1–2 | Gap, task, three contributions |
| S2 | §2 Related Work; §2.1 Web-Oriented Benchmark; §2.2 Agents on Web-Navigation | 2–3 | Benchmark positioning and agent approaches |
| S3 | §3 WebWalkerQA; §§3.1–3.4 | 3–5 | Collection, statistics, traversal task, evaluation |
| S4 | §4 WebWalker; §§4.1–4.2 | 5–6 | Explorer policy, observation/history, critic memory |
| S5 | §5 Experiment; §§5.1–5.4 | 6–7 | Setup, main results, domain/language analysis, errors |
| S6 | §6 Discussion; §§6.1–6.3 | 7–9 | Search systems, retrieval integration, action scaling |
| S7 | §7 Conclusion | 9 | Synthesis of contributions |
| SL | Limitations and Discussion | 9 | Dataset size, modality, tuning, retrieval integration |
| SR | Acknowledgement and References | 10–12 | Funding and cited literature |
| AA–AF | Appendices A–F | 13–16 | Implementation, retrieval systems, example record, prompts, evaluator, cases |

The substantive visual inventory contains Figures 1–11 and Tables 1–6. Figures 1, 2, 4, and 10 are examples or diagrams; Figures 3 and 5–9 visualize distributions or experiments; Figure 11 reproduces the evaluator prompt. There are no numbered algorithm listings, formal theorems, lemmas, proofs, or explicitly enumerated hypotheses. Mathematical content is unnumbered task and agent notation. The main experiments are registered below as X1–X6, with appendix cases X7–X8.

## 3. Background and context

[A] A **large language model (LLM)** supplies the reasoning and language generation used by the agents. The authors describe its trained knowledge as static, motivating access to dynamically updated webpages. **Question answering (QA)** means returning an answer to a supplied question. **Retrieval-augmented generation (RAG)** adds retrieved information to the material used to generate that answer. [p. 1]

[A] The paper distinguishes **horizontal search**, finding relevant documents through a search engine, from **vertical exploration**, following links deeper into a selected website. Neither term is a spatial measurement: they distinguish search across retrieved sources from navigation within a site's linked structure. A **root URL**, or starting web address, is given to the traversal agent. A **subpage** is a page reached within that structure. [pp. 1, 4, 8–9]

[A] **Single-source QA** requires answer information from one relevant page; **multi-source QA** requires information from distinct pages. The dataset construction describes the latter in terms of two associated pages. **Depth** is how deeply the answer page lies in the site structure. **Width** in Table 1 indicates multiple information sources. **Hop** there indicates multiple required task steps. These labels describe different properties and should not be substituted for one another. [pp. 1, 3–4]

[A] **HTML**, the page markup referred to by the paper, and the **Document Object Model (DOM)** supply structured web elements. WebWalker observes Markdown-like page content plus clickable HTML button descriptions and their URLs. It reasons over this extracted representation rather than using screenshots as its agent input. Figures containing screenshots illustrate the work; they do not make the evaluated agent multimodal. [pp. 5, 9, 13]

[A] **ReAct** interleaves thought, action, and observation. **Reflexion** is described as a single-agent framework using feedback. WebWalker uses an explorer based on ReAct and a separate critic for relevance extraction, memory, and answering. **Zero-shot** is the reported experimental setting; the paper separately states that WebWalker uses prompting without additional training. **Chain-of-thought (CoT)** prompting is used in the answer evaluator to request an explanation before a correctness grade. These descriptions are restricted to how this paper uses the terms. [pp. 2, 5–6, 9, 15]

## 4. Research problem and gap

[A] The existing problem is incomplete access to answer-bearing web information. Search engines can return relevant-looking pages without exposing the deeper subpages needed for a query. Dynamic information also limits answers drawn only from a model's stored knowledge. [p. 1; pp. 8–9]

[A] The authors attribute several shortcomings to previous web benchmarks and agents: emphasis on instruction–action tasks, noisy HTML, long inputs, limited long-context understanding, and insufficient attention to deep information-seeking. They position their work around QA over official sites, using restricted click actions and both single-source and multi-source questions. Related benchmarks are discussed as prior work, not independently reevaluated in this analysis. [pp. 1–3]

[A] The claimed gap is a benchmark focused on traversal depth and information gathering, paired with a memory-managing baseline. The scope covers conference, organization, education, and game websites, chosen for authoritative information and rich clickable structure. The benchmark does not cover all browser tasks, unrestricted tool use, or every kind of website. [pp. 2–4]

[D] The security research gap remains open in this paper. Ordinary errors under benign task conditions cannot by themselves show adversarial susceptibility. A website's official status is a collection criterion here, not a demonstrated security guarantee. The supplied work does not test manipulated links, malicious text, authentication boundaries, or instructions conflicting with the user's objective.

## 5. Research questions / objectives / hypotheses

The authors do not present formally numbered research questions or statistical hypotheses. The following are labeled **objectives reconstructed from explicit descriptions**, not quotations of formal RQs.

| ID | Author-grounded objective | Evidence and analysis |
|---|---|---|
| O1 | Assess LLM agents' ability to traverse websites for answers | WebWalkerQA task and Table 3, pp. 3–7 |
| O2 | Evaluate an explorer–critic framework with memory | §4 and main method comparisons, pp. 5–7 |
| O3 | Examine differences by depth, source count, model, domain, and language | Tables 2–3 and Figures 5–7, pp. 4, 6–7 |
| O4 | Test whether existing search-enhanced systems obtain deep information | §6.1 and Table 4, pp. 7–8 |
| O5 | Test integration of vertical traversal with horizontal retrieval | §6.2 and Figure 8, pp. 8–9 |
| O6 | Explore increasing navigation actions during inference | §6.3 and Figure 9, p. 9 |

No formal null hypothesis, alternative hypothesis, significance threshold, or preregistered analysis is visible. The requested security question is an external analytical lens supplied by the user, not O1–O6. Its relevance is addressed as [D] inference in §§14, 17, and 18; an actual security comparison is absent.

## 6. Assumptions / threat model

[A] The task starts with a given root website and query. Answer-bearing material must be accessible through page traversal. Actions are constrained to clicks, represented as selecting a subpage URL. The main configuration allows at most 15 explorer actions. The critic decides whether accumulated information suffices to answer; otherwise exploration continues until the budget is reached. [pp. 2, 4–7]

[A] Observations contain extracted page information and clickable elements. Dataset construction uses official websites, and evaluation uses a model-based judge against the reference answer. The main study is text-based and uses no additional agent training. Root discovery is a separate future-integration issue: the authors acknowledge that the root URL is supplied in §6.2. [pp. 5, 9, 13–15]

[D] These are functional assumptions, not a stated adversarial threat model. The paper specifies no attacker, attacker-controlled fields, protected secrets, trust hierarchy, malicious site population, exploit objective, or defense guarantee. It does not explain whether untrusted page text is isolated from agent instructions or whether extracted memory retains provenance sufficient for security decisions. These matters are unreported, rather than proven absent from the released implementation.

[D] Candidate boundaries for future security analysis are webpage-to-observation, observation-to-action, observation-to-memory, memory-to-answer, and memory-to-RAG-context. The architecture establishes these information flows; it does not establish that malicious content crosses them successfully. Click-only actions narrow this benchmark's action scope and cannot support conclusions about transactions, file access, email, or other tools not evaluated here.

## 7. Methodology

### Dataset construction

[A] The authors use a two-stage funnel: GPT-4o initially constructs QA pairs, followed by crowdsourced human quality control and filtering. Official websites are recursively traversed to collect accessible links and page information. Questions are generated for a single page or for combined information from pages. Verification favors natural questions with concise answers containing entities; humans can rewrite and calibrate both questions and answers. [p. 3, §3.1]

[A] Appendix D.1 explains root selection: Google searches using phrases such as conference official website or game official website, followed by manual filtering. Education sites are official university computer science department sites. Appendix D.2's multi-source prompt requires information from at least two sublinks with an intrinsic connection. Its verifier rejects questions answerable from one document, documents contributing only background, incorrect or long answers, and unnatural phrasing. The single-source verifier distinguishes known information in doc1 from current information in doc2 and requires dependence on doc2. [pp. 13–14]

[B] The single-source prompt block shows a Question Generate heading without a substantive generation template underneath it. The multi-source generator and both verification templates are represented, but a complete single-source generation prompt cannot be reconstructed from the supplied page. [p. 14]

### Dataset structure and difficulty

[A/B] There are 680 QA pairs. Table 2 has six cells: single-source easy/medium/hard contain 80/140/120, and multi-source easy/medium/hard also contain 80/140/120. [C] Each source type therefore contains 80 + 140 + 120 = 340 questions; the complete count is 2 × 340 = 680. Combined difficulty totals are 160 easy, 280 medium, and 240 hard. [pp. 3–4]

[A] Single-source labels use page depths 2, 3, and 4 for easy, medium, and hard. Multi-source labels use the sum of two page depths, with stated ranges 2–4, 4–6, and 6–8. The shared endpoints 4 and 6 make exact boundary assignment unclear. A footnote explains that total depth 6 can arise from two third-level pages or a second-level plus a fourth-level page. Difficulty therefore encodes structural depth, not a measured psychological or computational difficulty score. [p. 4]

[A/B] Chinese accounts for 60.5% and English for 39.5%; language is classified from the root webpage. Domain proportions contain an inconsistency: prose gives conference 24.0%, organization 7.9%, education 46.3%, and game 24.0%, whereas Figure 3 labels the game-colored slice 21.9%. Both are preserved below. No train/validation/test split, unique-root count, collection dates, annotator count, inter-annotator agreement, filtering totals, or licensing terms are specified in the supplied material. [p. 4]

### Architecture and execution

[A] The explorer receives page Markdown-like content and clickable HTML buttons with URLs, extracted using Beautiful Soup. Its role is to choose a subpage to visit, not to answer the question. It maintains an interaction history represented by thought/action/observation components. The critic operates after explorer execution, extracts useful information, updates memory, checks sufficiency, and generates the answer when appropriate. [pp. 5–6]

[A/B] Appendix D.3 divides the critic behavior into two JSON-output tasks. Relevance extraction returns usefulness and information when useful. Answer checking returns judge and answer when sufficient, or judge false otherwise. The templates make the intended information compression and stopping decision explicit, but they are not an implementation-level specification of memory storage, provenance, or error handling. The explorer template includes placeholders for tool descriptions and names without supplying a full concrete tool schema. [pp. 14–15]

### Configuration, baselines, and metrics

[A] The main backbones are GPT-4o, Qwen-Plus, and Qwen2.5-7B/14B/32B/72B-Instruct. Models are selected with at least 128K context windows and at least 7B parameters. ReAct and Reflexion are baselines. All three methods operate zero-shot with an explorer action limit of 15. Appendix A reports top-p = 0.8, Qwen-Agent as the foundational codebase, and a crawling tool for Markdown-like pages. Its prose names ai4crawl while the footnote links crawl4ai; this naming discrepancy is preserved. Hardware, versions, temperatures, seeds, run counts, and detailed API configurations are not supplied. [pp. 6–7, 13]

[A] Accuracy measures answer correctness using GPT-4 with a CoT evaluator comparing prediction and ground truth. Action count, A.C., is computed only for correct executions. It is consequently a success-conditioned navigation measure, not total action cost over all attempted questions. Runtime, token cost, critic-call cost, and failed-execution cost are not reported. Appendix E's evaluator allows extra information if it does not conflict with the answer and ignores punctuation and phrasing differences. [pp. 4–7, 15]

[A] Appendix B evaluates five commercial retrieval systems and two open-source systems. Naive RAG searches Google and concatenates information from the top 10 returned links with the query for Qwen-Plus. MindSearch is described as a WebPlanner/WebSearcher multi-agent system. Commercial systems are accessed through business-oriented APIs; configurations are delegated to the unsupplied codebase. [p. 13]

## 8. Experiments / analyses

| ID | Purpose and setup | Outcomes and evidence | Qualifications |
|---|---|---|---|
| X1 | Compare ReAct, Reflexion, and WebWalker on six backbones using WebWalkerQA; zero-shot, principal action budget 15 | Table 3 accuracy and correct-run A.C.; WebWalker highest overall accuracy within each backbone | No repeats, uncertainty estimates, or significance tests reported |
| X2 | Examine domain and language performance for WebWalker with Qwen-Plus and Qwen-14B | Figure 6 radar plots; authors emphasize conference performance and similar bilingual performance | Exact per-domain and per-language values are not tabulated |
| X3 | Classify outcomes for ReAct and WebWalker with Qwen-Plus and Qwen-14B | Figure 7: correct, refusal/locating wrongly, exceeding K, reasoning error | Category assignment procedure and annotator reliability unspecified |
| X4 | Assess no-retrieval and search-enhanced systems on the same six QA groups | Table 4; no-retrieval overall 8.08% and 9.85%; search-system maximum 40.73% | Different products/configurations; no controlled retrieval-only causal isolation |
| X5 | Add WebWalker critic memory to Naive RAG's retrieved documents | Figure 8; improvements across all six plotted groups | Given root URL; exact hybrid values not printed; backbone naming varies |
| X6 | Vary K over 5, 10, 15, 20, 25 using Qwen-Plus | Figure 9; improved performance with increasing budget and visible flattening | No cost, latency, or security outcomes; K = 0 RAG baseline also drawn |
| X7 | Illustrate reasoning after finding the relevant page | Table 5 and Appendix F.1; lounge schedule, reference answer 66 hours | No full failed prediction or trajectory supplied |
| X8 | Illustrate outdated stored knowledge | Table 6 and Appendix F.2; o1 prediction invokes October 2023 cutoff | One case; cutoff statement is author/model-output evidence, not independently verified |

X1–X6 address the paper's traversal and retrieval objectives. X7–X8 illustrate error mechanisms rather than constitute controlled experiments. Every principal comparison uses the benchmark's source/difficulty grouping, but exact denominators for Figure 6's domain/language subgroups are not provided. No experiment addresses adversarial instruction following or attack resistance.

## 9. Results

### Main overall results

[B] Table 3 reports the following overall pairs, where accuracy is percent and A.C. is the reported action-count measure restricted to successful executions.

| Backbone | ReAct acc. / A.C. | Reflexion acc. / A.C. | WebWalker acc. / A.C. |
|---|---:|---:|---:|
| GPT-4o | 33.82 / 3.83 | 35.29 / 4.27 | 37.50 / 4.67 |
| Qwen-Plus | 33.08 / 3.03 | 33.23 / 4.32 | 33.82 / 4.36 |
| Qwen2.5-7B | 16.02 / 2.99 | 19.11 / 4.07 | 19.85 / 3.94 |
| Qwen2.5-14B | 22.35 / 2.76 | 25.14 / 3.01 | 27.50 / 3.60 |
| Qwen2.5-32B | 25.44 / 2.93 | 23.26 / 3.00 | 26.02 / 3.90 |
| Qwen2.5-72B | 30.73 / 2.86 | 32.50 / 4.09 | 33.26 / 4.32 |

[C] GPT-4o WebWalker improves over ReAct by 37.50 − 33.82 = **3.68 percentage points**, and over Reflexion by 37.50 − 35.29 = **2.21 percentage points**. These are not relative percentage improvements. Qwen-Plus gains over ReAct by only 33.82 − 33.08 = **0.74 percentage points**; Qwen2.5-14B gains 27.50 − 22.35 = **5.15 percentage points**. The benefit depends on backbone. [p. 6, Table 3]

[B] WebWalker wins every backbone's overall accuracy comparison, but not every subgroup. GPT-4o Reflexion is higher on single-source easy/medium/hard: 56.25/51.43/30.83 versus WebWalker's 55.00/50.00/30.00. WebWalker's GPT-4o multi-source easy accuracy is substantially higher: 47.50 versus 35.00 for Reflexion and 32.50 for ReAct. For Qwen-Plus, Reflexion's multi-source easy score is 47.50 versus WebWalker's 35.00. These exceptions prevent an across-the-board superiority claim. [p. 6]

[B] Increasing source depth generally reduces accuracy, but not monotonically in every row. GPT-4o WebWalker decreases from 55.00 to 50.00 to 30.00 across single-source difficulty and from 47.50 to 34.29 to 15.83 across multi-source difficulty. Qwen2.5-14B WebWalker is 41.25 then 41.43 then 23.33 for single-source difficulty, a small easy-to-medium increase. [p. 6]

### Search systems and integration

[B] In Table 4, Gemini-1.5-Pro and o1-preview without retrieval obtain 8.08% and 9.85%. Commercial systems range from Doubao's 16.76% to Tongyi's 40.73%; Naive RAG obtains 20.73% and MindSearch 11.32%. Tongyi's exact number is above 40%, while nearby prose describes it as only reaching 40%. This is a rounded textual characterization, unlike Table 3's best WebWalker result of 37.50%. [p. 8]

[A/B] Figure 8 and accompanying text report gains after integrating WebWalker with RAG across difficulty levels, especially multi-source. [B] Approximate bars are 0.38→0.56, 0.26→0.52, 0.24→0.36, 0.20→0.34, 0.14→0.32, and 0.13→0.20 for single-source easy/medium/hard then multi-source easy/medium/hard. These are **approximate visual estimates**, not exact results. Table 4 provides exact Naive RAG baseline values but no exact hybrid table. [pp. 8–9]

[A/B] Figure 9 supports improved performance with larger action budgets in the tested range. The WebWalker line rises from roughly 0.24 at K = 5 to roughly 0.34–0.35 at K = 20–25. The hybrid RAG bars rise to roughly 0.42. The nearly level rightmost results qualify any claim of indefinitely increasing returns. [p. 9]

## 10. Figure-by-figure interpretation

### Figure 1 — Multi-source question example

[B] A compact composite on page 1 connects a conference website, clicked subpages, an explorer/critic icon pair, and an answer about an industry-track submission deadline and conference venue address. Its purpose is to show why two pieces of information can require traversing different branches of one site. There are no quantitative axes or uncertainty markers. [A] The caption explicitly identifies a multi-source WebWalkerQA example. Tiny embedded text is not needed to infer the architecture; the readable example is repeated more clearly in Figures 4 and 10. This is an illustration, not a measured success rate.

### Figure 2 — Data generation pipeline

[B] Four stages run left to right: (a) official root website, (b) sublinks/subpages as a URL tree, (c) synthetic QA pairs, and (d) manually verified QA pairs. Colored tree nodes represent root, second-, third-, and fourth-level pages. Dashed selections contrast multi-source node combinations with a single-source target. Arrows label traversal, query generation, and manual annotation. [A] The caption names the four domains and GPT-4o generation followed by manual verification. This supports the collection workflow, but reports no attrition counts or annotation reliability. [p. 4]

### Figure 3 — Language and domain distributions

[B] Two pie charts use percentage-labeled slices. Language is English 39.5% and Chinese 60.5%. Domain colors map to conference 24.0%, education 46.3%, organization 7.9%, and game 21.9%. There are no axes or confidence intervals. [C] The displayed domain percentages total 24.0 + 46.3 + 7.9 + 21.9 = 100.1%, consistent with a possible rounding total, while the prose percentages total 102.2%. The game discrepancy cannot be resolved from supplied evidence. These proportions should not be converted into exact integer sample counts. [p. 4]

### Figure 4 — Explorer–critic worked flow

[B] The left panel separates explorer Thought/Action/Observation from critic Thought/Memory/Judge. The central panel shows three steps, and the right panel shows visited conference pages. Example clicks include Calls, Industry Track Papers, and Venue. Page observations feed critic extraction, useful information accumulates, and the final answer combines deadline and venue. Arrows trace the click-to-page and page-to-processing paths. No accuracy metric or elapsed time is displayed. [D] It illustrates information movement into memory, useful for identifying prospective trust boundaries, but does not depict an adversarial payload. [p. 5]

### Figure 5 — Accuracy against successful action count

[B] This scatterplot has linear x-axis Action Count, with ticks about 2.75–4.75, and y-axis Accuracy, with visible ticks 5–35. Red triangles encode WebWalker, blue squares Reflexion, and green dots ReAct; labels identify backbones. Higher points indicate better accuracy; farther-right points indicate more actions among successful runs. GPT-4o WebWalker occupies the upper-right area, whereas smaller Qwen models occupy lower regions. Exact values are available in Table 3. No error bars are shown. [A] The authors interpret upper-right movement as effective, prolonged traversal. [D] Rightward movement alone is not proof of lower cost or better efficiency. [pp. 6–7]

### Figure 6 — Domain and language comparisons

[B] Two radar panels compare Qwen-Plus and Qwen-14B WebWalker. Spokes are Conference, Organization, Education, Game, English, and Chinese. The left panel is accuracy, the right A.C.; blue and orange polygons distinguish the models. Accuracy is drawn as fractions, while A.C. is action count. Radial label presentation is sparse, especially in the A.C. panel, so exact values and scale interpretation should not be reconstructed confidently. [A] Authors highlight conference performance and similar Chinese/English performance, attributing the former to clearer buttons and the latter to bilingual training. These explanations are not experimentally isolated. [p. 7]

### Figure 7 — Outcome distribution

[B] Four horizontal stacked bars compare WebWalker and ReAct for Qwen-Plus and Qwen-14B. The x-axis runs 0–100%, with categories correct in orange-red, refusal or locating wrongly in pale blue, exceeding K in blue-green, and reasoning error in pink. Each bar partitions outcomes rather than showing an accuracy confidence interval. ReAct with Qwen-14B has the largest visible refusal/locating segment; WebWalker reduces that segment while often expanding budget-exceeding outcomes. Reasoning errors are a small segment. Exact error percentages are unlabeled, so only broad comparisons are represented. [p. 7]

### Figure 8 — RAG with and without WebWalker

[B] Six groups on the x-axis represent single-source and multi-source easy/medium/hard. Pink bars denote RAG and blue bars RAG with WebWalker. The linear y-axis Performance runs 0.0–0.6. All blue bars exceed paired pink bars. Approximate values are listed in §9 and remain estimates. No error bars, numeric bar labels, or statistical markers are visible. [A] The associated method appends critic memory to retrieved documents. The figure supports benchmark improvements, not a security benefit or an isolated proof that memory alone caused them. [p. 8]

### Figure 9 — Action-budget scaling

[B] The linear x-axis Number of Action K shows 0, 5, 10, 15, 20, 25; the y-axis Performance is fraction-scaled with visible ticks 0.0–0.4. An orange-red WebWalker line with point markers and pale-blue RAG bars compare conditions. The caption describes the bars as RAG combined with WebWalker; at K = 0 the bar visually supplies a retrieval baseline near 0.21, while the line starts at zero. Both series increase then flatten. Text states the tested traversal budgets as {5,10,15,20,25}. No uncertainty or cost information appears. [p. 9]

### Figure 10 — Annotated JSON record

[B] A blue-bordered code panel shows Question, Answer, Root_Url, and Info, with Hop, Domain, Language, Difficulty_Level, Source_Website, and Golden_Path. The example is an English, medium, multi-source conference question combining March 21, 2025 and Brune-Kreisky-Platz 1. A material inconsistency is visible: the source page points to industry_track, but the illustrated golden path includes student_research_workshop. This may be an example-record error, but it cannot be repaired without the underlying data. The figure is a schema/example, not evidence of dataset-wide error prevalence. [p. 13]

### Figure 11 — Answer evaluator prompt

[B] A bordered prompt requests step-by-step explanation and CORRECT/INCORRECT grading. It supplies question, reference answer as context, and model result as student answer. It accepts phrasing differences and nonconflicting extra information. No visual scale applies. [A] This operationalizes the model-based evaluation described in §3.4. [D] It shows that the evaluator judges factual agreement with a reference answer, not safe navigation, justified provenance, or adversarial robustness. [p. 15]

## 11. Table-by-table interpretation

### Table 1 — Benchmark positioning

[A/B] Rows are Mind2Web, WebArena, AssistantBench, MMInA, GAIA, and WebWalkerQA. Columns compare language, task format, Depth/Width/Hop checkmarks, and webpage counts. The reported counts are 100, 6, 525, 100, an unspecified dash for GAIA, and 1,373 for WebWalkerQA. WebWalkerQA alone receives a Depth checkmark and supports English and Chinese; all comparison rows are English. Width and Hop are checked for AssistantBench, MMInA, GAIA, and WebWalkerQA. These are the authors' characterizations of prior benchmarks, not independently verified claims. §2.1 refers to the comparison as Table 2 although it is actually Table 1. [pp. 2–3]

### Table 2 — Question counts by difficulty

[B] Six cells show 80, 140, 120 for each source type. The small trees visually distinguish source number and depth. There is no statistical test, missing-data notation, or uncertainty measure. The table verifies the total 680 by summation and shows that medium questions are more common than easy questions. It does not report domain-by-difficulty or language-by-difficulty cross-tabulations. [p. 4]

### Table 3 — Main agent results

[B] Eighteen method/backbone rows are grouped into closed- and open-source backbones. Each has accuracy and A.C. for six strata plus overall. Accuracy is interpreted as percent from the values and plotting conventions; A.C. is success-conditioned action count. Overall entries are fully reproduced in §9. WebWalker has each backbone's highest overall accuracy, with 37.50% the overall maximum and 16.02% Qwen-7B ReAct the minimum. Subgroup exceptions matter: Reflexion sometimes wins, and smaller model increases are not uniformly monotonic. No confidence intervals, tests, or significance notation accompany results. [p. 6]

[B] The minimum subgroup accuracy is Qwen-7B Reflexion's 4.17% on multi-source hard, while Qwen-72B WebWalker reaches 58.75% on single-source easy. Increasing successful-run actions can accompany better accuracy but does not account for unsuccessful runs or all model calls. The supplied text extraction separates one value as 18.5 7; the rendered table supports reading it as 18.57 for Qwen-7B ReAct single-source medium. Detailed subgroup A.C. values and most subgroup accuracy cells are deliberately compressed rather than fully transcribed.

### Table 4 — No-retrieval and search-enhanced systems

[B] Rows include two close-book systems, five commercial search systems, two open-source systems, and Avg. Columns are six source/difficulty accuracy percentages and overall.

| System | SS easy | SS medium | SS hard | MS easy | MS medium | MS hard | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini-1.5-Pro, no retrieval | 12.50 | 7.86 | 8.33 | 11.25 | 6.43 | 5.00 | 8.08 |
| o1-preview, no retrieval | 16.25 | 10.00 | 9.17 | 7.50 | 10.71 | 6.67 | 9.85 |
| Doubao | 45.00 | 15.00 | 18.33 | 13.75 | 8.57 | 10.00 | 16.76 |
| Gemini-Search | 40.00 | 32.14 | 29.17 | 30.00 | 23.57 | 17.50 | 27.94 |
| ERNIE-4.0-8K | 52.50 | 30.00 | 28.33 | 21.25 | 18.57 | 30.00 | 28.97 |
| Kimi | 77.50 | 41.43 | 40.83 | 26.25 | 26.43 | 22.50 | 37.35 |
| Tongyi | 41.25 | 45.00 | 41.67 | 40.00 | 41.43 | 34.17 | 40.73 |
| Naive RAG | 37.50 | 25.71 | 24.17 | 20.00 | 14.29 | 12.50 | 20.73 |
| MindSearch | 15.00 | 11.43 | 10.83 | 8.75 | 12.14 | 10.00 | 11.32 |
| Avg. | 37.50 | 24.29 | 23.42 | 19.86 | 18.02 | 16.48 | — |

SS and MS mean single-source and multi-source. Tongyi leads overall and each multi-source group; Kimi leads single-source easy at 77.50%, and Tongyi leads single-source medium/hard at 45.00/41.67. The Avg. row's inclusion rule is not explained. It should not be described as a benchmark-wide weighted accuracy or silently recomputed. Individual rows contain nonmonotonic depth patterns, including ERNIE multi-source hard exceeding its easier multi-source scores. [p. 8]

### Table 5 — Reasoning case

[A/B] The question asks total attendance time for Inclusive Connections Lounge activities from December 1–6, 2024. Reference answer: 66 hours. The embedded schedule visibly gives Sunday 7:30 am–6:30 pm, Monday 7:30 am–6:30 pm, Tuesday 7:30 am–6:30 pm, Wednesday 7:30 am–6:30 pm, Thursday 7:30 am–6:30 pm, and Friday 7:30 am–6:30 pm. [C] Each is 11 hours; 6 × 11 = 66 hours. This visually supports the reference answer. Appendix F.1 explains that finding the right page is insufficient if the system processes time incorrectly. No actual failed calculation is shown in this table. [pp. 15–16]

### Table 6 — Time-cutoff case

[A/B] The reference answer for the 2025 MRS Fall Meeting is Boston, Massachusetts, November 30–December 5, 2025. The displayed prediction states that, as of its October 2023 cutoff, exact dates/location had not been announced. The table illustrates an answer failing to supply current information. It is not independent confirmation of every version of o1's cutoff or an attack example. The body calls the model o1 while Table 4 labels its no-retrieval system o1-preview; no version reconciliation is supplied. [pp. 15–16]

## 12. Diagram / architecture interpretation

Figures 1, 2, 4, and 10 serve different architectural roles and should not be conflated.

[A/B] **Collection path, Figure 2:** official roots → traversal of accessible links → gathered page content → GPT-4o-generated QA pairs → manual correction/filtering → final verified dataset. Source-depth selections determine single- versus multi-source construction. The diagram does not show counts discarded between stages or a training/evaluation split.

[A/B] **Execution path, Figure 4:** query plus current extracted page → explorer thought and click selection → new page observation → critic relevance extraction → accumulated memory → critic sufficiency judgment. A false sufficiency decision allows further exploration; a true judgment produces an answer. The action budget provides another termination condition. The memory path is persistent across steps; the explorer's history is a separate context representation. [pp. 5–6, 14–15]

[A/B] **Retrieval integration, §6.2:** ordinary retrieved documents and WebWalker critic memory are combined as generation input. The paper does not show a complete implementation diagram for routing, deduplication, provenance resolution, or the treatment of contradictions between retrieved documents and memory. A supplied root URL is necessary in the evaluated hybrid configuration. [pp. 8–9]

[D] **Security relevance:** these flows expand the number of transformations between a webpage and an answer. They provide specific objects for future inspection—button descriptions, URLs, page Markdown, history, extracted memory, and the final retrieval context. Calling them candidate attack surfaces is an analyst interpretation. The source does not show instructions being laundered through memory, hostile URL selection, or exploit propagation.

## 13. Equations and mathematical concepts

The paper uses unnumbered notation rather than a formal optimization objective. There is no loss function, theorem, or proved security property.

| ID | Form and location | Meaning and limits |
|---|---|---|
| E1 | Given U_root and Q, §3.3, p. 4 | Input is a starting website URL and a question; desired output is an answer supported by traversed information |
| E2 | O_t = (p_t, l_t), §4.1, p. 5 | Observation at step t combines current page information p_t with clickable sublinks l_t |
| E3 | l_t = {button_i}_{i=1}^{K}, §4.1, p. 5 | Set of clickable button descriptions with associated URLs; K here is the number of listed links |
| E4 | π(A_t | H_t), §§4.1–4.2, p. 5 | Explorer action-selection policy conditioned on interaction history; its internal mathematical form is not specified |
| E5 | H_t = (T_1, A_1, O_1, …, O_{t−1}, T_t, A_t, O_t), §4.1, p. 5 | Printed history contains thought, action, observation components; the ellipsis is compressed and ordering is problematic for a pre-action condition |
| E6 | Memory M, §4.2, pp. 5–6 | Critic's accumulated useful information; no formal update equation or storage specification supplied |
| E7 | Single-source_i, i ∈ [2,4], §§3.2, pp. 3–4 | Label i is answer-page depth; depths 2/3/4 map to easy/medium/hard |
| E8 | Multi-source_i, i ∈ [2,8], §3.2, p. 4 | Label i is the sum of two page depths; stated difficulty ranges share endpoints |
| E9 | K ∈ {5,10,15,20,25}, §6.3, p. 9 | Experimental maximum-action budgets used in scaling analysis |

[A] T denotes thought, A action, O observation, t step index, Q query, and U_root starting URL. Selecting A_t means choosing a subpage URL, while answering is assigned to the critic. π is called a policy but is not parameterized, optimized, or explicitly trained in this paper. [p. 5]

[D] Two notation issues remain. First, K denotes clickable-link count in E3 and maximum-action budget in E9; context must disambiguate them. Second, the printed H_t includes A_t and O_t even though π(A_t | H_t) describes choosing A_t based on H_t. The source does not resolve whether this is post-step notation or a temporal indexing error. This report preserves the published form instead of silently replacing it with a conventional pre-action history.

[C] Arithmetic used in this report is limited to reproducible sums and differences: 680 questions from six counts, percentage-point gains from Table 3, domain-percentage totals, and 66 hours from the visible schedule. These are descriptive derivations, not significance tests or new author results.

## 14. Interpretation and discussion

[A/B] The benchmark is difficult for the evaluated agents and retrieval systems. O1 is supported by low overall accuracy and especially low hard multi-source results. O2 receives descriptive support because WebWalker improves overall accuracy within all six backbones. That support is qualified by subgroup reversals and the absence of isolated memory/explorer/critic ablations. [pp. 6–7]

[A/B] O3 is addressed through depth/type tables and domain/language charts. Larger Qwen backbones generally perform better, but Qwen-32B Reflexion at 23.26% is below Qwen-14B Reflexion at 25.14%. The authors' broad statement that Reflexion outperforms ReAct also has an overall exception: Qwen-32B ReAct reaches 25.44%. Longer successful trajectories are compatible with deeper information gathering, but A.C. does not establish better resource efficiency. [pp. 6–7]

[A/B] O4 shows that search-enhanced systems still leave many questions unanswered. O5 shows improved plotted performance when critic memory augments retrieval documents. O6 supports action-budget scaling within the tested range, with diminishing visible gains at high K. None of these results identifies whether retrieval, planning, extraction, evaluator error, or final reasoning is the dominant cause across every failure. [pp. 8–9]

[D] For the security question, the useful inference is architectural: the agent repeatedly incorporates external observations and uses them to select further actions, store information, and generate answers. A standalone no-retrieval condition lacks those particular live webpage flows in the reported setup. However, the paper's close-book comparison measures factual QA performance using different systems, not adversarial vulnerability of matched standalone and agentic models. It therefore supports **where to investigate potential exposure**, not **why agents are empirically more vulnerable**.

The consistency audit identifies: (1) game-domain 24.0% in prose versus 21.9% in Figure 3; (2) nine claimed validated models in §5.1 versus six listed/main-result backbones; (3) §2.1's Table 2 reference versus the actual comparison Table 1; (4) generalized method-ranking and scaling statements with numerical exceptions; (5) K symbol reuse and history timing ambiguity; (6) Figure 10's industry-track source versus workshop golden path; (7) Qwen-Plus versus Qwen-2.5-Plus naming in hybrid discussion; and (8) ai4crawl prose versus crawl4ai footnote. These are preserved as unresolved or qualified rather than automatically reconciled.

[D, MEDIUM confidence, source inconsistency flagged for review] Table 3 reports Qwen2.5-7B ReAct overall A.C. 2.99, below every displayed subgroup A.C. (minimum 3.36). If overall A.C. is a weighted mean of those successful-execution subgroup means under the same protocol, this is not reconstructible. A differing aggregation or reporting error could explain it, but neither is established by the supplied source. Retain published values without guessing a corrected action count. [Physical pp. 6–7]

## 15. Contributions and novelty

[A] **Dataset/benchmark:** WebWalkerQA provides 680 bilingual QA pairs emphasizing deep single-source and combined multi-source information from official websites, with 1,373 webpages reported. The authors position this depth emphasis as distinguishing it from earlier benchmarks. [pp. 2–4]

[A] **Task framing:** Web Traversal starts from a provided root URL and query, evaluating information-seeking through click actions. This isolates navigation and answering from broader action-based browser workflows. [pp. 1–4]

[A] **System/method:** WebWalker pairs a ReAct-based explorer with a critic that extracts useful information, maintains memory, judges sufficiency, and answers. Its claimed memory-management advantage addresses long, noisy context. [pp. 2, 5–6]

[A] **Empirical contributions:** comparisons across backbones, source/depth groups, domains/languages, outcome categories, retrieval systems, hybrid integration, and action budgets show remaining challenges and potential gains from vertical exploration. [pp. 6–9]

[A] **Implementation availability:** the paper states code and data availability through a GitHub project and dataset hosting. These artifacts were not supplied or accessed here, so availability is author-reported and implementation claims are not independently reproduced. [pp. 1, 13]

[D] **Security relevance is not an author-claimed contribution.** The system provides a concrete architecture that could be used to study external-content exposure. The paper contains no security benchmark, attack algorithm, defense, formal security model, or adversarial comparison demonstrating novelty on the user's security question.

## 16. Limitations

### Authors' stated limitations

[A] **Dataset size:** 680 verified QA pairs are relatively limited; approximately 14,000 additional silver QA pairs have not been carefully human-verified and are proposed as supplementary training material. They are not equivalent to the evaluated benchmark and were not inspected here. [p. 9]

[A] **Multimodal environment:** the evaluated approach only parses clickable buttons through HTML-DOM. Screenshot-based visual information is left for future work. [p. 9]

[A] **Agent tuning:** WebWalker uses prompting without additional training. Fine-tuning with golden trajectories is proposed to improve effective action selection. [p. 9]

[A] **Better retrieval integration:** the root URL is provided. The authors propose query rewriting and searching for suitable official websites before applying WebWalker, then combining ordinary retrieval and traversed information. [p. 9]

### Additional evidence-based analyst observations

[D] The supplied report lacks run-to-run uncertainty, significance tests, evaluator calibration against humans, annotation agreement, raw trajectories, complete product configuration, and timing or monetary cost. These omissions limit reproducibility and causal interpretation; they are not claims that the underlying implementation necessarily omitted them.

[D] Success-conditioned A.C. can hide costs of failed attempts and critic calls. Depth-based difficulty bins do not isolate reasoning complexity from navigation complexity. Official sites and click-only tasks bound generalization. The hybrid's supplied root omits root-discovery mistakes from the tested pipeline. Figure 10 and domain distribution discrepancies warrant record-level checking but cannot establish dataset-wide error rates.

[D] Security outcomes are entirely unmeasured. Non-adversarial refusal, wrong location, or reasoning mistakes should not be renamed attacks. Increasing K increases opportunities for traversal in the reported system, but no relation between K and exploit probability is established.

## 17. Threats to validity

These validity categories are **analyst observations**, not terminology or admissions attributed to the authors.

| Category | Source-grounded concern | Consequence |
|---|---|---|
| Internal validity | Architecture comparisons do not isolate memory, additional critic processing, prompt differences, or stopping policy | Overall gains cannot be causally assigned to memory alone |
| Construct validity | Model-judged QA accuracy and successful-run action count operationalize only parts of task performance | Neither measures security, total cost, or provenance quality |
| Statistical conclusion validity | No repeats, confidence intervals, or tests reported | Small descriptive gains cannot be called statistically reliable |
| External validity | Four official-site domains, two languages, structured buttons, supplied roots | Findings need not transfer to arbitrary sites or unrestricted agents |
| Ecological validity | Live information motivates the benchmark, but snapshot/collection dates and product versions are unspecified | Changing websites and services may change outcomes |
| Reproducibility | API details and artifacts are referred to externally; no inspection here | Exact independent execution cannot be established from this report alone |
| Measurement validity | GPT-4 judge accepts paraphrases and extra nonconflicting content, without reported human agreement | Judge error is not quantified |
| Security validity | No adversary, attack manipulation, protected asset, or matched security baseline | No evidence that web agents are more vulnerable than standalone LLMs |

[D] The authors' error explanation attributes failures to long noisy contexts and model capability. Figure 7 makes this plausible but does not independently manipulate context noise while holding other factors fixed. The security implication is therefore a hypothesis to investigate, not a demonstrated causal bridge from noisy context to adversarial exploitation.

## 18. Future work and open questions

### A. Author-proposed future work

[A] Expand or use the roughly 14k silver QA collection for training, after recognizing its limited human verification. Add screenshot/visual modalities. Tune agents using golden trajectories. Improve RAG integration through query rewriting, official-site discovery, and combined retrieved/traversed knowledge. Explore larger inference-time traversal budgets within useful ranges. [p. 9]

### B. Additional analyst open questions

[D] Can the same model be compared as a standalone answerer, standard retrieval answerer, and WebWalker agent under matched benign and adversarial tasks? Which externally supplied elements can alter navigation or contaminate critic memory? Does relevance extraction retain source attribution and distinguish page data from instructions? Can stored content influence later steps after its originating page is no longer visible? What happens when retrieved documents conflict with memory? These questions arise from documented information flows; the paper supplies no attack results answering them.

[D] Other unresolved questions concern cost-normalized improvements, failure-inclusive action counts, evaluator agreement, repeatability across dates and roots, exact depth-bin boundaries, benchmark-record consistency, and whether gains persist after isolating memory and critic-call effects. More actions might improve benign accuracy while changing exposure, but the direction and magnitude of any security tradeoff are UNKNOWN from this source.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used for reasoning, action selection, or answering |
| QA | Question–answer task or paired benchmark record |
| RAG | Retrieval-augmented generation: using retrieved information during answer generation |
| Web traversal | Starting at a root site and navigating its linked pages to gather an answer |
| Horizontal search | Search-engine retrieval of relevant documents |
| Vertical exploration | Following links deeper within a website |
| Root URL / U_root | Supplied starting web address |
| Single-source | Answer-bearing information from one relevant page |
| Multi-source | Required information from distinct pages; construction discusses two associated pages |
| Depth | Structural level of an answer page |
| Width | Table 1's multiple-source requirement |
| Hop | Table 1's multiple-step requirement; Figure 10 uses Hop as a source-type field |
| HTML / DOM | Page markup / Document Object Model used to identify clickable content |
| Markdown-like content | Textual page representation supplied to the explorer |
| Explorer | Agent choosing which clickable subpage URL to visit |
| Critic | Agent extracting useful information and deciding whether to answer |
| ReAct | Reasoning and acting through repeated thought/action/observation steps |
| Reflexion | Feedback-based single-agent baseline described by the authors |
| CoT | Chain-of-thought prompting; evaluator requests reasoning before grading |
| acc. | Answer accuracy, reported as percentages in result tables |
| A.C. | Action count calculated only for correct executions |
| Q | Query/question |
| t | Navigation step index |
| T_t, A_t, O_t | Thought, action, and observation at a step |
| p_t, l_t | Current page information and clickable link set |
| H_t | Printed interaction-history representation |
| π(A_t\u007cH_t) | Explorer policy selecting action conditional on history |
| M | Critic's accumulated useful-information memory |
| K | Link-set size in §4.1; action budget in experiments, requiring contextual disambiguation |
| top-p | Reported generation hyperparameter, set to 0.8; its implementation details are not supplied |
| Golden path / trajectory | Reference navigation route; full construction/validation procedure unspecified |
| Silver QA | Additional machine-produced QA material not carefully human-verified |
| Close book | No-retrieval answering condition |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Verified benchmark | 680 | QA pairs | WebWalkerQA | Author-reported | pp. 2–3 |
| Webpages | 1,373 | pages | Benchmark comparison | Visually readable | p. 3, T1 |
| Domains | 4 | domains | Conference, organization, education, game | Author-reported | p. 4 |
| Languages | 2 | languages | Chinese and English | Author-reported | p. 4 |
| SS counts | 80 / 140 / 120 | questions | Easy / medium / hard | Visually readable | p. 4, T2 |
| MS counts | 80 / 140 / 120 | questions | Easy / medium / hard | Visually readable | p. 4, T2 |
| Source-type total | 340 each | questions | 80 + 140 + 120 | Analyst-derived | p. 4, T2 |
| Combined difficulty totals | 160 / 280 / 240 | questions | Twice each source-type count | Analyst-derived | p. 4, T2 |
| Language distribution | 60.5 / 39.5 | % | Chinese / English | Author-reported | p. 4, F3 |
| Game distribution | 24.0 versus 21.9 | % | Prose versus chart | Author-reported / visually readable; inconsistent | p. 4 |
| Context selection threshold | At least 128K | context-window size | Reported model selection | Author-reported | p. 6 |
| Parameter threshold | At least 7B | parameters | Reported model selection | Author-reported | p. 6 |
| Main backbones | 6 listed, 9 claimed | models | Main table versus §5.1 prose | Visually readable / author-reported; inconsistent | pp. 6–7 |
| Main action budget | 15 | actions | Explorer maximum | Author-reported | pp. 6–7 |
| Generation top-p | 0.8 | hyperparameter | Appendix A | Author-reported | p. 13 |
| Naive RAG retrieved links | 10 | links | Google top results | Author-reported | p. 13 |
| Best main WebWalker | 37.50 | % accuracy | GPT-4o, zero-shot, 15-action setup | Visually readable | p. 6, T3 |
| Associated A.C. | 4.67 | action-count measure | Correct GPT-4o WebWalker executions | Visually readable | p. 6, T3 |
| GPT-4o WebWalker gain | 3.68 | percentage points | 37.50 − 33.82, versus ReAct | Analyst-derived | p. 6, T3 |
| Qwen-14B WebWalker gain | 5.15 | percentage points | 27.50 − 22.35, versus ReAct | Analyst-derived | p. 6, T3 |
| Best T4 overall | 40.73 | % accuracy | Tongyi search-enhanced | Visually readable | p. 8, T4 |
| No-retrieval results | 8.08 / 9.85 | % accuracy | Gemini-1.5-Pro / o1-preview | Visually readable | p. 8, T4 |
| Open-source search results | 20.73 / 11.32 | % accuracy | Naive RAG / MindSearch | Visually readable | p. 8, T4 |
| Hybrid SS easy | About 0.56 | performance fraction | Blue Figure 8 bar | Approximate visual estimate | p. 8, F8 |
| Scaling budgets | 5, 10, 15, 20, 25 | actions | Qwen-Plus inference sweep | Author-reported | p. 9 |
| Additional silver collection | Approximately 14k | QA pairs | Not carefully human-verified | Author-reported | p. 9 |
| Lounge duration | 66 | hours | Six days at 11 hours/day | Author-reported; visually supported derivation | p. 16, T5 |
| Conference reference dates | Nov. 30–Dec. 5, 2025 | dates | MRS Fall Meeting, Boston | Author-reported | p. 16, T6 |

All numerical conditions are retained: accuracy, action count, performance fractions, question counts, and action budgets are different quantities. Chart estimates are not substituted for exact table values. No attack-rate number exists in the supplied work.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Benchmark targets deep web information gathering | Given root/query, click actions, source/depth definitions | T1–T2, F2, O1 | pp. 2–4 | HIGH for design; claimed superiority to prior benchmarks is author positioning |
| Collection combines LLM and human annotation | GPT-4o generation and manual verification | F2, Appendix D | pp. 3, 13–14 | HIGH for reported procedure; reliability statistics absent |
| Explorer and critic have separate roles | Navigation versus relevance/memory/sufficiency/answer | F4, Appendix D.3 | pp. 5–6, 14–15 | HIGH for architecture; exact memory implementation unavailable |
| WebWalker improves overall accuracy within each tested backbone | Six overall method comparisons | T3, X1 | p. 6 | HIGH descriptively; subgroup reversals and no significance tests |
| Benchmark remains difficult | Best main agent 37.50%; best T4 search system 40.73% | T3–T4, X1/X4 | pp. 6, 8 | HIGH for displayed conditions; not a universal model capability bound |
| Increased depth/source requirements generally reduce accuracy | Six-stratum results | T3–T4 | pp. 6, 8 | MEDIUM for generalization; explicit nonmonotonic exceptions |
| Retrieval integration improves plotted groups | Blue bars exceed pink bars in all six groups | F8, X5 | pp. 8–9 | HIGH for direction; exact hybrid values and variability absent |
| Larger K improves tested performance | Budget sweep and plotted rising/flattening curves | F9, X6 | p. 9 | MEDIUM; limited range, no cost-normalized result |
| Finding a page need not ensure correct reasoning | Schedule calculation case | T5, X7 | pp. 15–16 | HIGH for illustrative distinction; no error prevalence established |
| External observations enter memory and generation | Architecture and hybrid method description | F4/F8, §6.2 | pp. 5–6, 8–9 | HIGH for flow; security exploitation is untested |
| Candidate agent security boundaries can be identified | Page→observation→action/memory→answer/RAG | Analyst interpretation of method | pp. 5–6, 8–9 | MEDIUM as architectural inference; no attack evidence |
| Paper establishes greater vulnerability than standalone LLMs | No supporting adversarial experiment | Negative finding across supplied document | pp. 1–16 | It does not establish this claim; confidence HIGH about scope, UNKNOWN about actual vulnerability |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a question whose answer is hidden several clicks inside a website. A search engine might find the website but miss the useful page. This paper builds a test of that problem: sometimes one deep page contains the answer, and sometimes two pages must be combined.

WebWalker gives the AI two jobs. An explorer chooses links to click. A critic writes down useful facts and checks whether those facts are enough to answer. This helps on the paper's test, but the strongest main WebWalker setup still answers only 37.50% correctly. Adding its collected information to a search-based answer system improves the plotted results, and allowing more clicks helps within the tested range.

For your security question, the important clue is the route information takes: website text can affect what the AI reads next, what it remembers, and what it eventually says. Those are sensible places to investigate malicious influence. But this paper never puts an attacker there or tests whether an attacker succeeds. Its no-search models do badly at finding current facts; that does not mean they are more secure or less secure.

The faithful takeaway is that web agents have a more elaborate interaction and memory pipeline than the paper's no-retrieval answering conditions. WebWalker gives us a concrete pipeline to study. It does not answer whether web agents are more vulnerable than standalone language models, or quantify how much more vulnerable they might be.

## Completeness Audit

The inventory is the coverage denominator. Available substantive sections, figures, tables, notation, experiments, contributions, and author limitations have been represented either directly or with disclosed compression. Visual inspection covers 14 supplied images; acknowledgement/reference pages 10 and 12 are text-only. This is an inventory-based representation of the supplied document, not independent reproduction or validation of the research.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue/Abstract | Yes | Yes | Represented in compressed form | Identity recorded below; affiliation/contact details compressed |
| §1 Introduction | Yes | Yes | Fully represented substantively | Motivation, gap, scope, contributions |
| §2.1 benchmarks | Yes | Yes | Represented in compressed form | Categories and T1; individual citations compressed |
| §2.2 navigation agents | Yes | Yes | Represented in compressed form | Training/filtering versus prompting; screenshot approaches |
| §3.1 collection | Yes | Yes | Fully represented substantively | GPT-4o, humans, recursive collection, filtering |
| §3.2 statistics | Yes | Yes | Fully represented with uncertainty | Counts, types, languages, domain discrepancy, bin ambiguity |
| §3.3 task | Yes | Yes | Fully represented | Given root/query and traversal goal |
| §3.4 evaluation | Yes | Yes | Fully represented | GPT-4 judge, accuracy, success-conditioned A.C. |
| §4.1 explorer | Yes | Yes | Fully represented with notation caveat | Observation, actions, history, page extraction |
| §4.2 critic | Yes | Yes | Fully represented substantively | Memory and sufficient-information answering |
| §5.1 setup | Yes | Yes | Fully represented with inconsistency | Six listed versus nine claimed; model selection and K |
| §5.2 main results | Yes | Yes | Represented in compressed form | Full overall results; selected strata and exceptions |
| §5.3 domain/language | Yes | Yes | Represented with uncertainty | Exact radar values unavailable |
| §5.4 errors | Yes | Yes | Fully represented substantively | Categories and unisolated causal explanation |
| §§6.1–6.3 | Yes | Yes | Fully represented substantively | X4–X6, T4, F8–F9 and qualifications |
| §7 conclusion | Yes | Yes | Represented in compressed form | Core synthesis preserved |
| Limitations: dataset | Yes | Yes | Fully represented | 680 and approximately 14k silver pairs |
| Limitations: multimodal | Yes | Yes | Fully represented | HTML-DOM only; screenshots future work |
| Limitations: tuning | Yes | Yes | Fully represented | Prompt-driven; golden trajectories proposed |
| Limitations: RAG integration | Yes | Yes | Fully represented | Root supplied; discovery/rewrite proposed |
| Explicit RQs/hypotheses | Yes, searched in supplied content | Absence recorded | No formal items present | O1–O6 are labeled objectives, not invented formal RQs |
| X1 main comparison | Yes | Yes | Represented in compressed form | Overall matrix complete; detailed cells selective |
| X2 domain/language | Yes | Yes | Represented with uncertainty | Unlabeled coordinates not made exact |
| X3 error analysis | Yes | Yes | Represented in compressed form | No exact error-share transcription |
| X4 search systems | Yes | Yes | Fully represented | T4 transcribed |
| X5 hybrid integration | Yes | Yes | Represented with uncertainty | All conditions; approximate bars |
| X6 K scaling | Yes | Yes | Represented with uncertainty | Budgets and flattening; approximate curves |
| X7–X8 cases | Yes | Yes | Fully represented substantively | Schedule and cutoff distinction |
| F1 | Yes, visually | Yes | Represented in compressed form | Tiny example labels compressed |
| F2 | Yes, visually | Yes | Fully represented substantively | Four stages and depth selections |
| F3 | Yes, visually | Yes | Fully represented with discrepancy | Game percentage unresolved |
| F4 | Yes, visually | Yes | Fully represented substantively | Agent roles, click/example flow |
| F5 | Yes, visually | Yes | Fully represented substantively | Exact points grounded in T3 |
| F6 | Yes, visually | Yes | Uncertain exact values | Radar patterns and author interpretation preserved |
| F7 | Yes, visually | Yes | Represented in compressed form | Categories and trends; unlabeled percentages omitted |
| F8 | Yes, visually | Yes | Approximate visual estimates | Six paired bars; uncertainty disclosed |
| F9 | Yes, visually | Yes | Approximate visual estimates | K range, baseline, improvement, plateau |
| F10 | Yes, visually | Yes | Fully represented substantively | Schema/example and golden-path mismatch |
| F11 | Yes, visually | Yes | Fully represented substantively | Grading rules and inputs |
| T1 | Yes | Yes | Fully represented substantively | All benchmarks/features/counts discussed |
| T2 | Yes | Yes | Fully represented | All six counts |
| T3 | Yes | Yes | Represented in compressed form | All overall cells; subgroup results selective |
| T4 | Yes | Yes | Fully represented | All numerical rows and conditions |
| T5 | Yes, including screenshot | Yes | Fully represented substantively | Schedule and 66-hour derivation |
| T6 | Yes | Yes | Fully represented substantively | Reference and prediction; version caution |
| E1–E9 | Yes | Yes | Fully represented with caveats | Unnumbered notation; K/history issues |
| Algorithms/pseudocode | No formal listing present | Absence recorded | Not applicable | Prompt/workflow procedures represented |
| Theorems/proofs | None present | Absence recorded | Not applicable | No formal security guarantee |
| Contributions: dataset/task/system/experiments | Yes | Yes | Fully represented substantively | Security novelty explicitly not attributed |
| Appendix A | Yes | Yes | Fully represented substantively | top-p, codebase, crawling-tool naming |
| Appendix B.1–B.2 | Yes | Yes | Fully represented substantively | Commercial APIs and open-source setup |
| Appendix C | Yes | Yes | Fully represented substantively | F10 and dataset availability statement |
| Appendix D.1 | Yes | Yes | Fully represented substantively | Root collection and education selection |
| Appendix D.2 | Yes | Yes | Represented in compressed form | Generation/verification logic; missing single-source generator body |
| Appendix D.3 | Yes | Yes | Represented in compressed form | Explorer and two critic templates |
| Appendix E.1 | Yes | Yes | Fully represented substantively | Model-based factual judge |
| Appendix F.1–F.2 | Yes | Yes | Fully represented substantively | Cases and their limited evidential scope |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Multi-source meaning, depth example, root-language classification, successful-run metric, LLaMA preliminary limitation, artifact/API references |
| References/acknowledgement | Yes; pp. 10/12 text-only | Yes | Deliberately compressed as secondary | Bibliography is not external-source verification |
| Separate supplementary files | Not supplied | Absence recorded | Missing from supplied material | No code/data/API config/silver-pair inspection |

**Document identity retained:** authors are Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Linhai Zhang, Yulan He, Deyu Zhou, Pengjun Xie, and Fei Huang. The supplied venue is Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp. 10290–10305, July 27–August 1, 2025. Affiliations include Southeast University, King's College London, The Alan Turing Institute, and Tongyi Lab, Alibaba Group. The acknowledgement names National Natural Science Foundation of China grant 62176053. Internship/correspondence notes are administrative and compressed. [pp. 1, 10]

### Missing or inaccessible material

No physical text page is missing from 1–16. Images for pages 10 and 12 are absent, so those pages were assessed only through supplied text. Released repositories, hosted dataset, detailed commercial API configurations, approximately 14k silver QA pairs, raw execution traces, editable figures, and evaluator outputs were not supplied or reviewed. The standalone single-source generation template's body is not visible despite its heading. No separate supplement was provided; references to code and datasets do not imply that those artifacts were inspected.

### Uncertain interpretations

Exact radar values in Figure 6, exact error shares in Figure 7, and exact hybrid/scaling values in Figures 8–9 cannot be asserted from unlabeled graphics. Domain game percentage, multi-source bin endpoints, nine-versus-six model count, history timing, K reuse, Figure 10's path mismatch, Qwen backbone naming, and crawling-tool naming remain unresolved. The Table 4 Avg. inclusion rule is unspecified. The source cannot determine adversarial vulnerability, matched standalone-versus-agent security differences, or the exploitability of the identified architectural boundaries.

### Deliberately compressed material

Table 3's extensive subgroup accuracy/action-count matrix is represented through every overall row, major strata, extrema, and exceptions rather than every cell. Repeated conference examples in Figures 1/4/10 are consolidated while preserving each object's role. Prompt templates are explained by inputs, outputs, and acceptance rules rather than fully quoted. Related-work citations, bibliography entries, decorative icons, contact information, and administrative notes are compressed. These choices preserve substantive methods and findings while avoiding repetitive transcription.

### Potential omissions

No known substantive inventory object is wholly unrepresented. Some detailed Table 3 cells and unlabeled chart coordinates are deliberately not reproduced; raw artifacts and unspecified methodological details remain inaccessible or unreported. Coverage is therefore comprehensive at the level of supplied substantive components, with disclosed numerical compression and uncertainty. It is not a claim to preserve every word or to establish scientific correctness, reproduction, or security conclusions beyond this paper.
