# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available page range | Pages 1–16, corresponding to proceedings pages 10290–10305 |
| Pages apparently missing | None |
| Native text | Available for all 16 pages; no page is identified as scanned or unusually text-poor |
| Visual inspection | Partial: rendered pages were supplied for pages 1–9, 11, and 13–16 |
| Pages not visually rendered | Pages 10 and 12; these contain references rather than substantive figures, tables, or methods |
| Figures | Figures 1–11 are present in the extracted text; all substantive figure pages were visually supplied |
| Tables | Tables 1–6 are available in extracted text and rendered pages; most values are readable |
| Equations | No separately numbered equations. Inline mathematical notation is available, though some subscripts, superscripts, and interval boundaries are OCR-sensitive |
| Algorithms/pseudocode | No formal algorithm block; the explorer/critic workflow and prompts serve as operational specifications |
| Appendices | Appendices A–F are present on pages 13–16 |
| Supplementary material supplied | No separate supplementary files, code repository, dataset archive, API configurations, or training data |
| Referenced but absent artifacts | GitHub codebase, Hugging Face dataset, API configurations, approximately 14,000 silver QA pairs, and external webpages cited in case studies |
| OCR needed | Not generally; native extraction is available. OCR-sensitive mathematical notation and table alignment were checked against rendered pages where possible |
| Important accessibility caveat | The analysis can assess what the paper reports about its code, data, APIs, and live websites, but cannot inspect those external artifacts in closed-document mode |

The complete 16-page paper is therefore textually accessible, while visual inspection is complete for its substantive figures and tables but not literally for every reference page.

# 1. Plain-Language Orientation

This paper studies whether a large language model (LLM) can begin at a website’s home page, follow links into increasingly deep subpages, collect the right pieces of information, and answer a question. The authors call this task **web traversal**.

The motivating problem is that ordinary retrieval-augmented generation (RAG) normally searches broadly across the web and retrieves documents that rank highly for a query. That “horizontal” search may miss authoritative information buried several clicks inside an official website. Some questions also require combining information from two different subpages rather than finding one ready-made answer.

The paper contributes two closely connected artifacts:

1. **WebWalkerQA**, a bilingual benchmark containing 680 question–answer pairs derived from more than 1,373 webpages in four website domains.
2. **WebWalker**, a prompted two-agent baseline in which:

   - an **explorer** chooses links using a Thought–Action–Observation loop; and
   - a **critic** extracts useful evidence into memory and decides when enough information has been gathered.

The benchmark separates questions by whether they require one source or multiple sources and by how deeply the relevant pages occur. The main evaluation shows that it is difficult: the best overall WebWalker result in Table 3 is 37.50% accuracy with GPT-4o, while the best searched-enhanced RAG system in Table 4 reaches 40.73% overall. Accuracy generally declines for deeper and multi-source questions.

The paper’s central empirical argument is that conventional search and vertical traversal are complementary. In Figures 8–9, adding WebWalker-derived memory to a naïve RAG pipeline improves every reported difficulty category, and allowing more traversal actions improves performance up to a plateau in the tested range.

Unless otherwise marked, statements below are **[A] author-reported**. Statements explicitly read from diagrams and plots are **[B] directly observable**; calculations made from reported values are **[C] analyst-derived**; and critical inferences are labeled **[D] analyst interpretation**.

# 2. Document Roadmap

The document is an AI benchmark, dataset, and agent-systems paper organized as follows:

| Section | Role in the argument |
|---|---|
| Abstract and §1, Introduction, pp. 1–2 | Defines the shallow-retrieval problem, proposes web traversal, introduces WebWalkerQA and WebWalker, and states three contributions |
| §2, Related Work, pp. 2–3 | Positions the work against web-action benchmarks, multi-page QA benchmarks, trained web agents, prompted agents, and visual agents |
| §3, WebWalkerQA, pp. 3–4 | Describes dataset creation, dataset composition, the web-traversal task, and evaluation metrics |
| §4, WebWalker, pp. 5–6 | Defines the explorer–critic architecture, observations, actions, histories, and memory |
| §5, Experiment, pp. 6–7 | Specifies baselines and backbones, then reports main performance, domain/language analysis, and error categories |
| §6, Discussion, pp. 7–9 | Evaluates closed-book and RAG systems, integrates WebWalker with RAG, and scales the action budget |
| §7, Conclusion, p. 9 | Restates the benchmark, method, and vertical-exploration conclusion |
| Limitations and Discussion, p. 9 | Discusses dataset size, lack of visual interaction, lack of agent tuning, and incomplete RAG integration |
| References, pp. 10–12 | Cited literature; inspected in compressed form |
| Appendix A, p. 13 | Implementation details |
| Appendix B, p. 13 | Commercial and open-source RAG configurations |
| Appendix C, p. 13 | Dataset example and availability |
| Appendix D, pp. 13–15 | Root-page selection, annotation prompts, and agent prompts |
| Appendix E, p. 15 | LLM evaluator prompt |
| Appendix F, pp. 15–16 | Reasoning-error and temporal-cutoff case studies |

Document inventory:

- Figures: F1–F11, corresponding to original Figures 1–11.
- Tables: T1–T6, corresponding to original Tables 1–6.
- Formal algorithms: none.
- Numbered equations or theorems: none.
- Operational mathematical definitions: task inputs, observation/action/history notation, memory, action budget, and difficulty-depth rules.
- Distinct empirical analyses:

  - X1: agent framework/backbone comparison, Table 3 and Figure 5;
  - X2: domain and language comparison, Figure 6;
  - X3: error distribution, Figure 7;
  - X4: closed-book and RAG comparison, Table 4;
  - X5: RAG plus WebWalker integration, Figure 8;
  - X6: action-budget scaling, Figure 9;
  - X7–X8: appendix case studies, Tables 5–6.

# 3. Background and Context

## Retrieval-augmented generation

**Retrieval-augmented generation (RAG)** retrieves external documents and supplies them to a language model before it generates an answer. In the authors’ framing, ordinary RAG performs **horizontal search**: it searches across documents or websites that appear relevant to a query (§1, pp. 1–2; §6.2, p. 8).

The weakness addressed here is that the needed fact may be several links below a root page. A search engine may return the home page or another shallow page without reaching the deeper page that contains the answer.

## Web agents and web traversal

A **web agent** is an LLM-based system that observes a web environment and chooses actions. Existing benchmarks often measure whether agents can execute tasks such as clicking, filling forms, or completing workflows. WebWalkerQA instead asks whether an agent can find and reason over authoritative information inside a website (§2, pp. 2–3).

The paper restricts the relevant action to **clicking a sublink**. This narrows the benchmark to navigation and information seeking rather than general computer control (§1, p. 2).

**Depth** means how far below the root website a relevant page lies.  
**Width** means whether multiple source pages are required.  
**Hop** indicates that multiple interaction steps are needed (Table 1, p. 3).

## Single-source and multi-source questions

A **single-source** question ultimately depends on one target subpage, although reaching that page may require several link selections.

A **multi-source** question requires evidence from two pages. Its depth index is the sum of the depths of those pages (§3.2, pp. 3–4). For example, the authors state that a multi-source depth of 6 could combine two third-level pages or a second-level and a fourth-level page (footnote 3, p. 4).

## ReAct and Reflexion

**ReAct** is used here as a baseline and as the explorer’s interaction pattern. It alternates internal reasoning, action selection, and environment observation.

**Reflexion** is a single-agent baseline that introduces feedback or reflection. WebWalker differs by separating exploration from critique and persistent evidence management (§4, pp. 5–6).

## Chain-of-thought evaluator

Exact string matching is unsuitable when a correct answer may be phrased in different ways. The paper therefore uses GPT-4 with a **chain-of-thought (CoT)** grading prompt to classify each answer as correct or incorrect (§3.4, pp. 4–5; Appendix E, p. 15).

# 4. Research Problem and Gap

## Existing problem

LLMs contain static pretrained knowledge. Search-enhanced systems can obtain fresher information, but ordinary search may retrieve shallow or incomplete material. Relevant evidence may be buried behind several website links or divided across pages (§1, pp. 1–2).

## Shortcomings attributed to previous approaches

According to the authors:

- HTML/action benchmarks such as Mind2Web and WebArena expose agents to noisy, long page content and focus on instruction execution rather than deeply buried information.
- Existing multi-page benchmarks cover width and multiple hops but do not explicitly evaluate depth from a root website (Table 1, p. 3).
- Search engines conduct horizontal retrieval and may fail to reach deeply nested pages (§1, p. 1; §6.1, p. 8).
- Multi-source questions may not be solvable through a single search shortcut because all required evidence may not be returned together (§3.1, p. 3).

## Research gap

The stated gap is a benchmark specifically testing whether an LLM agent can begin from a root URL, traverse a structured official website, find deeply nested authoritative information, combine evidence where necessary, and answer a concise QA item.

## Motivation

The authors argue that official conference, organization, education, and game websites contain structured link paths and dynamically updated facts. These make them useful environments for evaluating realistic information seeking (§1, pp. 1–2; §3.2, p. 4).

## Scope

The scope is deliberately narrower than unrestricted web automation:

- inputs are a root URL and query;
- interaction is through HTML/Document Object Model content and clickable links;
- no form filling, scrolling-based visual grounding, or general GUI actions are evaluated;
- answers are short entities or judgments;
- the benchmark covers Chinese and English root webpages and four domains.

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or hypotheses. Its objectives can be reconstructed without presenting them as formal author-written RQs:

1. **Benchmark objective:** Construct a dataset that measures deep, multi-step, single- and multi-source website navigation (§1, pp. 1–2).
2. **Agent objective:** Test whether an explorer–critic framework with external memory can serve as a strong baseline for this task (§4, pp. 5–6).
3. **Evaluation objective:** Compare WebWalker, ReAct, and Reflexion across closed- and open-source backbones (§5, pp. 6–7).
4. **RAG objective:** Determine whether existing closed-book and searched-enhanced RAG systems can answer WebWalkerQA (§6.1, pp. 7–8).
5. **Integration objective:** Test whether vertical traversal complements horizontal RAG (§6.2, pp. 8–9).
6. **Scaling objective:** Examine whether increasing the maximum number of link actions improves inference-time performance (§6.3, p. 9).

No statistical null hypotheses, confidence intervals, or significance tests are specified.

# 6. Assumptions / Threat Model

This is not a cybersecurity study, so there is no attacker-oriented threat model. The relevant system and environmental assumptions are:

- A correct root URL is supplied to the agent (§3.3, p. 4; §6.2 limitation, p. 9).
- Relevant information is accessible through links or buttons discoverable from the website hierarchy.
- Pages can be represented using Markdown-like page text plus extracted HTML buttons and their URLs (§4.1, p. 5; Appendix A, p. 13).
- Official websites are treated as authoritative sources for benchmark construction (§3.1–3.2, pp. 3–4).
- The live page structure remains sufficiently compatible with the recorded task and golden path.
- The agent does not answer during an explorer action; it selects a URL, while the critic decides when an answer can be produced (§4.1–4.2, pp. 5–6).
- Successful performance requires both navigation and reasoning. Finding the golden page alone may be insufficient (Figure 7 discussion, p. 7; Appendix F.1, pp. 15–16).
- GPT-4 grading is treated as the operational measure of semantic answer correctness (§3.4 and Appendix E).
- The default explorer action limit is \(K=15\) (§5.1, pp. 6–7).

Trusted components implicitly include link extraction, page-to-Markdown conversion, the root URLs, benchmark annotations, and the GPT-4 evaluator. The paper does not test adversarial webpages, malicious instructions, inaccessible pages, authentication barriers, or hostile HTML.

# 7. Methodology

## 7.1 Overall study design

The work combines:

- benchmark and dataset construction;
- implementation of a prompted multi-agent baseline;
- comparative evaluation across agent methods and LLM backbones;
- evaluation of existing RAG systems;
- integration and inference-scaling experiments.

## 7.2 WebWalkerQA construction

The dataset uses a two-stage funnel (§3.1, pp. 3–4; Figure 2):

1. Official root websites are located.
2. The sites are traversed recursively and accessible sublinks/pages collected.
3. GPT-4o generates candidate QA pairs under predefined single- or multi-source roles.
4. An LLM-based verification prompt filters candidates.
5. Crowd-sourced human annotators rewrite, calibrate, verify, and filter the candidates.

Appendix D.1 adds that root sites were initially located using Google queries such as “conference official website” and “game official website,” followed by manual filtering. University computer-science department sites were used for the education domain (p. 13).

### Annotation criteria

The multi-source generation prompt requires:

- at least two intrinsically connected sublinks;
- information from both pages;
- a complex but natural multi-step question;
- a concise entity-like answer;
- rejection if one page alone suffices.

The single-source verifier treats one document as known context and a second as the current/deeper page. It accepts a question only if the current page is necessary and the answer is concise and correct (Appendix D.2, pp. 13–14).

### Dataset size and classes

WebWalkerQA contains 680 QA pairs (§3.2, p. 3), distributed evenly between:

- 340 single-source questions;
- 340 multi-source questions.

For each type, Table 2 reports:

- easy: 80;
- medium: 140;
- hard: 120.

The total is \(2(80+140+120)=680\), an **[C] analyst-derived consistency check**.

### Difficulty rules

- Single-source:

  - depth 2 → easy;
  - depth 3 → medium;
  - depth 4 → hard.

- Multi-source:

  - summed depth 2–4 → easy;
  - summed depth 4–6 → medium;
  - summed depth 6–8 → hard.

The extracted notation produces overlapping boundaries at 4 and 6. The supplied text does not state whether these intervals are half-open or otherwise disambiguated; this is an uncertainty.

## 7.3 Web-traversal task

Given root URL \(U_{\text{root}}\) and question \(Q\), the agent navigates the site until it has enough information to answer \(Q\) (§3.3, p. 4).

The principal metrics are:

- **accuracy (acc.)**: percentage of answers graded correct;
- **action count (A.C.)**: number of link actions for successful/correct executions only (§3.4, pp. 4–5; §5.4, p. 7).

Because A.C. excludes unsuccessful runs, it is not a measure of average computational cost over all attempts.

## 7.4 WebWalker architecture

### Explorer

At step \(t\), the explorer receives:

\[
O_t=(p_t,l_t),
\]

where:

- \(p_t\) is the current page’s Markdown-like content;
- \(l_t=\{\text{button}_i\}_{i=1}^{K}\) is the set of clickable buttons/sublinks shown in the notation;
- each button has descriptive HTML information and a URL.

It chooses:

\[
A_t \sim \pi(A_t\mid H_t),
\]

where \(A_t\) is a subpage URL and \(H_t\) is the accumulated interaction history (§4.1, p. 5).

The explorer’s prompt follows Question → Thought → Action → Action Input → Observation and may repeat that cycle (Appendix D.3, p. 14).

### Critic

After each explorer action, the critic:

1. checks whether the new observation is relevant;
2. returns JSON with `usefulness: true/false`;
3. appends extracted evidence to memory \(M\) if useful;
4. judges whether accumulated information is sufficient;
5. returns either `judge: false` or `judge: true` with an answer.

This separates the large navigation history from a more selective memory of relevant evidence (§4.2, pp. 5–6; Appendix D.3, pp. 14–15).

## 7.5 Experimental configuration

### Agent methods

- ReAct
- Reflexion
- WebWalker

### Backbones reported in Table 3

- GPT-4o
- Qwen-Plus
- Qwen2.5-7B-Instruct
- Qwen2.5-14B-Instruct
- Qwen2.5-32B-Instruct
- Qwen2.5-72B-Instruct

The paper says it validates “nine models” (§5.1, p. 6), but only six agent backbones are subsequently named and reported in Table 3. This is an unresolved text–table inconsistency.

### Selection rules and inference settings

- minimum context window: 128K;
- minimum model size for open models: 7 billion parameters;
- zero-shot operation;
- default maximum action count: \(K=15\);
- generation hyperparameter: `top_p = 0.8`;
- Qwen-Agent as foundational codebase;
- `crawl4ai` for Markdown-like webpage extraction (Appendix A, p. 13).

Hardware, temperature, random seeds, number of repeated runs, runtime, token cost, and exact API versions are not supplied.

## 7.6 RAG systems

Table 4 evaluates:

- closed-book Gemini-1.5-Pro and o1-preview;
- commercial Doubao, Gemini-Search, ERNIE-4.0-8K, Kimi, and Tongyi;
- open-source Naive RAG and MindSearch.

Naive RAG uses Google, concatenates information from the top 10 returned links with the query, and asks Qwen-Plus to answer (Appendix B.2, p. 13).

For RAG plus WebWalker, the critic’s accumulated memory is appended to the conventionally retrieved documents before generation (§6.2, pp. 8–9).

# 8. Experiments / Analyses

## X1 — Agent framework and backbone comparison

**Purpose:** Compare ReAct, Reflexion, and WebWalker across six backbones.

**Data:** All 680 benchmark questions, divided into six type/difficulty cells.

**Metrics:** Accuracy and successful-run action count.

**Evidence:** Table 3 and Figure 5, p. 6.

Major overall results:

| Backbone | ReAct acc. | Reflexion acc. | WebWalker acc. |
|---|---:|---:|---:|
| GPT-4o | 33.82 | 35.29 | **37.50** |
| Qwen-Plus | 33.08 | 33.23 | **33.82** |
| Qwen2.5-7B | 16.02 | 19.11 | **19.85** |
| Qwen2.5-14B | 22.35 | 25.14 | **27.50** |
| Qwen2.5-32B | 25.44 | 23.26 | **26.02** |
| Qwen2.5-72B | 30.73 | 32.50 | **33.26** |

WebWalker is best overall for each listed backbone, but Reflexion does not uniformly beat ReAct: Qwen2.5-32B ReAct scores 25.44 versus Reflexion’s 23.26. Thus the prose ordering “WebWalker … outperforms Reflexion, which in turn outperforms ReAct” (§5.2, p. 7) is a broad trend, not a universal row-by-row result.

The hardest multi-source cell is consistently difficult: every Table 3 accuracy is between 4.17% and 16.67%.

## X2 — Domains and languages

**Purpose:** Compare WebWalker with Qwen-Plus and Qwen-14B across four domains and two languages.

**Evidence:** Figure 6 and §5.3, p. 7.

The radar plots show conference as the strongest domain for both backbones. The authors attribute this to explicit, directive button labels. They report similar Chinese and English performance and attribute this to bilingual pretraining and supervised fine-tuning.

Exact values are not labeled clearly enough in the supplied radar plots for reliable transcription; the plots support relative patterns rather than exact numerical claims.

## X3 — Error assessment

**Purpose:** Determine why agent attempts fail.

**Error categories:**

- refusal or wrong location;
- exceeding \(K\);
- reasoning error after navigation.

**Evidence:** Figure 7 and §5.4, p. 7.

The authors argue that smaller ReAct systems often terminate after a few actions without locating sufficient evidence. Larger models and WebWalker’s memory reduce this behavior. Figure 7 also shows that some failures persist as reasoning errors even when the relevant page was visited.

Approximate visual reading suggests WebWalker reduces the “refusal or locating wrongly” share substantially for Qwen-14B relative to ReAct, while no configuration eliminates reasoning errors.

## X4 — Closed-book and RAG evaluation

**Purpose:** Determine whether static model knowledge or standard searched-enhanced RAG can answer the benchmark.

**Evidence:** Table 4, p. 8.

Overall accuracy ranges from:

- 8.08% for closed-book Gemini-1.5-Pro;
- 9.85% for closed-book o1-preview;
- 11.32% for MindSearch;
- up to 40.73% for Tongyi.

Tongyi is strongest overall and in five of the six type/difficulty cells, but Kimi is best on single-source easy questions at 77.50%.

The average row reports a monotonic decline from 37.50% for single-source easy to 16.48% for multi-source hard. The paper does not specify exactly which systems enter this average; it appears associated with searched-enhanced systems rather than the closed-book rows, but that cannot be confirmed from the supplied text.

## X5 — Adding WebWalker to RAG

**Purpose:** Test horizontal plus vertical retrieval.

**Setup:** Add WebWalker’s critic memory to the documents returned by Naive RAG; use Qwen-Plus.

**Evidence:** Figure 8 and §6.2, pp. 8–9.

The figure reports higher performance for RAG plus WebWalker in every one of the six cells. Approximate visual estimates are:

| Cell | RAG | RAG + WebWalker |
|---|---:|---:|
| Single-source easy | 0.38 | 0.56 |
| Single-source medium | 0.26 | 0.53 |
| Single-source hard | 0.24 | 0.37 |
| Multi-source easy | 0.20 | 0.43 |
| Multi-source medium | 0.14 | 0.32 |
| Multi-source hard | 0.13 | 0.21 |

These are **approximate visual estimates**, not labeled exact values.

## X6 — Action-budget scaling

**Purpose:** Test whether more allowed clicks improve inference-time performance.

**Conditions:** \(K\in\{5,10,15,20,25\}\), Qwen-Plus backbone.

**Evidence:** Figure 9 and §6.3, p. 9.

Both WebWalker alone and RAG plus WebWalker improve as \(K\) increases through most of the range, then flatten. Approximate WebWalker values are 0.27, 0.29, 0.34, 0.35, and 0.35 for \(K=5,10,15,20,25\). Approximate RAG-plus-WebWalker bars are 0.36, 0.40, 0.39, 0.42, and 0.41.

The authors describe this as evidence for vertical inference scaling “within a certain range,” appropriately acknowledging the plateau.

## X7 — Reasoning case

Table 5 asks for the total duration of six daily “Inclusive Connections Lounge” schedules. The reported answer is 66 hours (Appendix F.1, pp. 15–16).

**[C] Analyst-derived verification:** The displayed schedule contains five 11.5-hour days (7:30 a.m.–6:30 p.m.) plus one 8.5-hour day (7:30 a.m.–3 p.m.):

\[
5(11)+8.5=63.5\text{ hours},
\]

not 66 hours, if elapsed clock time is calculated literally and no omitted activity interval exists. The image’s line breaks and endpoints are small, so this discrepancy should be treated cautiously. Nevertheless, the displayed schedule does not transparently reproduce the stated 66-hour answer. This is a potentially important source–answer inconsistency.

## X8 — Knowledge-cutoff case

Table 6 asks where and when the 2025 MRS Fall Meeting will occur. The ground truth is Boston, Massachusetts, November 30–December 5, 2025. The o1 prediction says that its October 2023 knowledge cutoff prevents it from knowing the answer.

The example supports the authors’ argument that static, closed-book knowledge cannot reliably answer questions about later website updates (Appendix F.2, pp. 15–16).

# 9. Results

## Finding 1 — The benchmark is difficult

The highest Table 3 overall agent accuracy is 37.50% for GPT-4o WebWalker. The best searched-enhanced RAG result is 40.73% for Tongyi (Table 4). Closed-book systems remain below 10%.

Qualification: the evaluation uses an LLM grader and no confidence intervals or repeated-run variability are reported.

## Finding 2 — WebWalker gives the best overall accuracy for each listed agent backbone

Across all six Table 3 backbones, WebWalker has the highest overall accuracy.

Examples:

- GPT-4o: 37.50 versus 35.29 Reflexion and 33.82 ReAct.
- Qwen2.5-14B: 27.50 versus 25.14 and 22.35.
- Qwen2.5-72B: 33.26 versus 32.50 and 30.73.

**[C] Analyst-derived:** For GPT-4o, WebWalker improves over ReAct by 3.68 percentage points:

\[
37.50-33.82=3.68.
\]

Relative to ReAct, this is approximately:

\[
3.68/33.82\approx10.9\%.
\]

The larger action count—4.67 versus 3.83—means it also takes more successful-run traversal actions.

## Finding 3 — Greater depth and multiple sources reduce accuracy

For GPT-4o WebWalker, accuracy declines from:

- 55.00% single-source easy;
- to 50.00% medium;
- to 30.00% hard.

For multi-source questions it is:

- 47.50% easy;
- 34.29% medium;
- 15.83% hard.

This pattern appears broadly across models and methods, though individual local reversals occur.

## Finding 4 — Model scale usually helps, but not monotonically in every comparison

Among WebWalker’s open-source backbones, overall accuracy is:

- 7B: 19.85%;
- 14B: 27.50%;
- 32B: 26.02%;
- 72B: 33.26%.

The 32B result is lower than 14B, so the prose claim that performance improves as model size increases (§5.2) is a general tendency rather than a strict monotonic relationship.

## Finding 5 — Conventional retrieval remains weak on deeply nested evidence

Table 4’s average row declines from 37.50% for single-source easy to 16.48% for multi-source hard. Tongyi reaches 40.73% overall, and Kimi 37.35%; the other searched systems score below 29%.

The paper interprets this as evidence that horizontal search often fails to retrieve all deep or distributed evidence.

## Finding 6 — Vertical traversal complements RAG

Figure 8 shows improvement in all six difficulty cells after WebWalker memory is appended to RAG documents. The largest visually apparent gains occur for single-source medium and multi-source easy/medium questions.

Because Figure 8 does not label exact bar values and no corresponding numerical table is supplied, exact improvements cannot be stated confidently.

## Finding 7 — More actions help until gains flatten

Figure 9 shows performance improving as the action limit rises, with relatively little additional gain after approximately \(K=15\)–20. The evidence supports bounded improvement, not indefinite scaling.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Example multi-source question

- **Location:** p. 1.
- **Contents:** An ACL 2025 root webpage, two navigation paths, selected evidence pages, and a question asking for both a submission deadline and venue address.
- **Flow:** Root page → click “Calls” → click “Industry Track”; separately click “Venue”; combine the two answers.
- **Purpose:** Demonstrates why one question may require two distinct pages.
- **Conclusion supported:** Web traversal can require both depth and width.
- **Caveat:** The screenshot text is illustrative and small; Appendix Figure 10 supplies the corresponding structured example more readably.

## Figure 2 — Dataset-generation pipeline

- **Location:** p. 4.
- **Panels:** (a) root official website; (b) URL tree with single- and multi-source page selection; (c) synthetic QA generation; (d) manual verification.
- **Encoding:** Colored nodes denote root, second-, third-, and fourth-level pages.
- **Flow:** Website discovery → recursive traversal → source-page selection → GPT-4o QA generation → human annotation.
- **Method relationship:** Visual counterpart of §3.1.
- **Caveat:** It summarizes the funnel but does not report rejection rates, annotator counts, or agreement.

## Figure 3 — Language and domain distributions

- **Location:** p. 4.
- **Plot type:** Two pie charts.
- **Language chart:** Labels 60.5% and 39.5%.
- **Domain chart:** Labels 24.0%, 46.3%, 7.9%, and 21.9%.
- **Important inconsistency:** Nearby prose says conference, organization, education, and game are 24.0%, 7.9%, 46.3%, and 24.0%. These sum to 102.2% and conflict with the visible 21.9% slice. The figure suggests game is 21.9%, not 24.0%.
- **Language inconsistency:** The visible legend/color mapping appears to assign 60.5% to English and 39.5% to Chinese, while the prose states Chinese 60.5% and English 39.5%. The supplied work is internally inconsistent, so the correct mapping cannot be determined with confidence.

## Figure 4 — WebWalker architecture

- **Location:** p. 5.
- **Components:** Explorer agent, critic agent, accumulated memory, visited webpages, and a multi-source worked trajectory.
- **Control loop:** Explorer reasons and clicks; critic examines each observation, extracts useful evidence, updates memory, and decides whether to continue or answer.
- **Feedback:** The critic’s decision controls whether another exploration step occurs.
- **Data flow:** Page observation → critic extraction → memory → final answer.
- **Conclusion supported:** Navigation history and answer evidence are managed by distinct roles.

## Figure 5 — Accuracy versus action count

- **Location:** p. 6.
- **Plot type:** Scatter plot.
- **X-axis:** successful-run action count, approximately 2.75–4.75.
- **Y-axis:** accuracy, approximately 0–40%.
- **Markers:** triangles = WebWalker; squares = Reflexion; circles = ReAct.
- **Observation:** Closed-source backbones occupy the upper/right region. Larger Qwen models generally move upward; reflective or critic-based methods often move right because they conduct longer successful traversals.
- **Caveat:** Higher action count is not automatically better efficiency. The paper calls A.C. an efficiency metric, but Figure 5 interprets movement to the right as more prolonged traversal rather than lower cost.

## Figure 6 — Domain/language radar charts

- **Location:** p. 7.
- **Panels:** Accuracy and action count for Qwen-Plus versus Qwen-14B.
- **Axes:** conference, organization, education, game, English, and Chinese.
- **Observation:** Conference accuracy is relatively high. Chinese and English appear broadly similar.
- **Uncertainty:** Radial tick labels and polygon positions do not support confident exact transcription.

## Figure 7 — Prediction distribution

- **Location:** p. 7.
- **Plot type:** 100% stacked horizontal bars.
- **Systems:** WebWalker and ReAct with Qwen-Plus and Qwen-14B.
- **Segments:** correct; refusal/wrong location; exceeding \(K\); reasoning error.
- **Observation:** WebWalker generally enlarges the correct segment and changes failure composition; wrong-location/refusal remains substantial, while reasoning errors persist.
- **Caveat:** Exact percentages are not printed and should not be inferred as exact.

## Figure 8 — RAG versus RAG plus WebWalker

- **Location:** p. 8.
- **Plot type:** Grouped bars.
- **X-axis:** six type/difficulty categories.
- **Y-axis:** performance from 0 to 0.6.
- **Encoding:** pink = RAG; blue = RAG with WebWalker.
- **Observation:** The blue bar is higher in every category, with conspicuous gains for single-source medium and multi-source easy/medium.
- **Numbers:** Only approximate visual estimates are available; see §8/X5.
- **Conclusion:** Vertical site traversal supplies evidence missed by horizontal retrieval.

## Figure 9 — Scaling action limit \(K\)

- **Location:** p. 9.
- **Plot type:** Bars plus a line.
- **X-axis:** action limit, \(K=0,5,10,15,20,25\).
- **Y-axis:** performance, 0–approximately 0.45.
- **Encoding:** bars = RAG plus WebWalker; orange line = WebWalker.
- **Observation:** Both configurations improve rapidly at small-to-moderate \(K\), then plateau.
- **Caveat:** The \(K=0\) bar appears to represent RAG alone, while WebWalker is zero/inapplicable there; the text does not explain this plotting convention explicitly.

## Figure 10 — Annotated JSON example

- **Location:** Appendix C/D, p. 13.
- **Contents:** Question, answer, root URL, hop type, domain, language, difficulty, source webpages, and golden paths.
- **Example answer:** March 21, 2025 and Brune-Kreisky-Platz 1.
- **Purpose:** Documents the released record schema.
- **Visual/text issue:** One golden path contains `student_research_workshop` for an Industry Track source, which appears semantically mismatched. The supplied work does not explain whether this is a display error or actual annotation.

## Figure 11 — Evaluator prompt

- **Location:** Appendix E, p. 15.
- **Contents:** A prompt instructing GPT-4 to grade factual correctness as `CORRECT` or `INCORRECT`, while tolerating punctuation and phrasing differences and allowing extra non-conflicting information.
- **Purpose:** Operational definition of accuracy.
- **Caveat:** No evaluator validation, inter-grader reliability, or comparison with human judgments is supplied.

# 11. Table-by-Table Interpretation

## Table 1 — Benchmark comparison

- **Location:** p. 3.
- **Rows:** Mind2Web, WebArena, AssistantBench, MMInA, GAIA, WebWalkerQA.
- **Columns:** language, format, depth, width, hop, number of pages.
- **Main result:** WebWalkerQA is the only listed benchmark marked as covering depth, width, and multiple hops, and the only bilingual one.
- **Page counts:** 100, 6, 525, 100, unspecified, and 1,373 respectively.
- **Cross-reference inconsistency:** §2.1 on p. 2 says the comparison appears in “Table 2,” but it is captioned Table 1.

## Table 2 — Dataset counts by type and difficulty

- **Location:** p. 4.
- **Counts:** 80 easy, 140 medium, and 120 hard for each of single-source and multi-source questions.
- **Totals:** 340 per type and 680 overall.
- **Class proportions [C]:** easy 23.53%, medium 41.18%, hard 35.29% overall.
- **No statistical information:** No uncertainty, sampling error, or annotation reliability is provided.

## Table 3 — Agent-method results

- **Location:** p. 6.
- **Structure:** Six backbones × three methods; accuracy and successful-run A.C. for six subsets plus overall values.
- **Best overall:** GPT-4o WebWalker, 37.50% accuracy.
- **Worst overall:** Qwen2.5-7B ReAct, 16.02%.
- **Highest listed overall A.C.:** GPT-4o WebWalker, 4.67.
- **Best subset values:**

  - single-source easy: Qwen2.5-72B WebWalker, 58.75%;
  - single-source medium: GPT-4o Reflexion, 51.43%;
  - single-source hard: GPT-4o Reflexion, 30.83%;
  - multi-source easy: GPT-4o WebWalker and Qwen-Plus Reflexion, 47.50%;
  - multi-source medium: GPT-4o WebWalker, 34.29%;
  - multi-source hard: GPT-4o Reflexion, 16.67%.

- **Important qualification:** WebWalker is best overall for every backbone but not best in every subset.
- **Statistical limitation:** No error bars, repeated runs, or significance tests.

## Table 4 — Closed-book and searched-enhanced RAG

- **Location:** p. 8.
- **Best overall:** Tongyi, 40.73%.
- **Best single-source easy:** Kimi, 77.50%.
- **Best multi-source hard:** Tongyi, 34.17%.
- **Closed-book:** 8.08% Gemini-1.5-Pro; 9.85% o1-preview.
- **Open-source:** 20.73% Naive RAG; 11.32% MindSearch.
- **Trend:** Accuracy generally declines with depth and multi-source requirements.
- **Terminology issue:** The caption says “Commercial and Open-sourced Searched-enhanced RAG systems,” but the table also contains closed-book rows.

## Table 5 — Reasoning case

- **Location:** p. 16.
- **Question:** Total time attending the Inclusive Connections Lounge, December 1–6, 2024.
- **Reported answer:** 66 hours.
- **Purpose:** Shows that locating the page does not guarantee correct arithmetic.
- **Potential discrepancy:** Literal calculation from the displayed schedule appears not to yield 66 hours; see X7.

## Table 6 — Temporal-cutoff case

- **Location:** p. 16.
- **Ground truth:** Boston, Massachusetts; November 30–December 5, 2025.
- **Prediction:** The model says this information was not announced as of its October 2023 cutoff.
- **Purpose:** Illustrates why dynamic web retrieval matters.
- **Caveat:** It is a single illustrative case, not a controlled analysis of cutoff failures.

# 12. Diagram / Architecture Interpretation

WebWalker’s architecture can be represented as:

```text
Question + root URL
        |
        v
Explorer observes current page text and available links
        |
        v
Explorer reasons and selects one link
        |
        v
New page observation
        |
        v
Critic asks: Is this observation useful?
        |
   +----+----+
   |         |
  No        Yes
   |         |
discard   extract evidence
             |
             v
       append to memory M
             |
             v
Critic asks: Is memory sufficient to answer?
        |
   +----+----+
   |         |
  No        Yes
   |         |
next click  return answer
   |
stop if maximum K is reached
```

The explorer’s full interaction history \(H_t\) can grow large and noisy. The critic functions as a lossy evidence compressor: it retains observations judged relevant to \(Q\) and omits others. This is the practical meaning of the paper’s “effective memory management” claim (§1, p. 2; §4.2, pp. 5–6).

For RAG integration, the critic’s memory is appended to horizontally retrieved documents:

```text
Search-engine documents ----+
                             +--> answer generator
WebWalker critic memory -----+
```

Thus WebWalker does not replace search in §6.2; it adds deeper, root-site-specific evidence.

# 13. Equations and Mathematical Concepts

There are no numbered equations, losses, optimization objectives, theorems, or proofs. The necessary formal concepts are:

## Task definition

\[
(U_{\text{root}},Q)\longrightarrow \text{website traversal}\longrightarrow \text{answer}.
\]

- \(U_{\text{root}}\): supplied initial website.
- \(Q\): question.
- Output: answer supported by information found during traversal.

## Observation

\[
O_t=(p_t,l_t).
\]

- \(O_t\): observation at step \(t\).
- \(p_t\): current page content.
- \(l_t\): clickable sublinks/buttons.

## Link set

\[
l_t=\{\text{button}_i\}_{i=1}^{K}.
\]

In §4.1 this \(K\) denotes the number of buttons in the current observation. Elsewhere \(K\) denotes the maximum number of actions. The paper reuses the same symbol for two related but distinct quantities, creating notation ambiguity.

## Action policy

\[
\pi(A_t\mid H_t).
\]

This is an implicit policy that chooses action \(A_t\) given history \(H_t\). It is not trained or explicitly parameterized in the paper; it is realized through prompting.

## History

The extracted text gives:

\[
H_t=(T_1,A_1,O_1,\ldots,O_{t-1},T_t,A_t,O_t).
\]

Here \(T\), \(A\), and \(O\) mean thought, action, and observation. The indexing is unusual because a policy choosing \(A_t\) would conventionally condition on information available before \(A_t\); the displayed \(H_t\) includes \(A_t\) and \(O_t\). The paper does not resolve this formal timing ambiguity.

## Memory

\[
M_t \leftarrow M_{t-1} + \text{relevant information extracted from }(Q,O_t,A_t).
\]

This update is expressed procedurally rather than as an equation. The critic then evaluates whether \(M_t\) is sufficient.

## Metrics

\[
\text{Accuracy} =
\frac{\text{number graded correct}}
{\text{number attempted}}.
\]

The exact formula is not printed but is the ordinary operational interpretation of the reported percentage.

A.C. is the action count only among correct executions. The aggregation method—mean, median, or another statistic—is not explicitly defined, although decimal values strongly suggest an average.

# 14. Interpretation and Discussion

The evidence supports three levels of conclusion.

First, the benchmark captures a real distinction between possessing information, retrieving a shallow page, and navigating to a deep page. Closed-book models perform poorly, and searched-enhanced systems lose accuracy as page depth and source count rise.

Second, WebWalker’s critic memory appears useful. It produces the best overall Table 3 accuracy for every listed backbone, although its advantage is modest and not uniform across individual categories. The method commonly performs more successful-run actions, so its gain is coupled to longer traversal.

Third, the Figure 8 integration experiment supports complementarity between horizontal search and vertical traversal. The strongest part of the argument is not that WebWalker alone solves the benchmark—it does not—but that its selected evidence improves an existing retrieval pipeline.

Several conclusions need qualification:

- “WebWalker outperforms Reflexion, which outperforms ReAct” is not universal across rows or subsets.
- “Performance improves as model size increases” has exceptions, notably Qwen2.5-32B WebWalker versus 14B.
- A.C. is conditioned on success and therefore cannot directly establish overall efficiency.
- Figures 8–9 are promising but lack tabulated exact values, uncertainty estimates, and repeated-run analysis.
- The benchmark’s dynamic live-web basis improves realism but may also make future reproduction sensitive to page changes.

# 15. Contributions and Novelty

## Conceptual contribution

The paper distinguishes **horizontal retrieval** from **vertical exploration** and frames them as complementary dimensions of information seeking.

## Dataset and benchmark contribution

WebWalkerQA contributes:

- 680 human-verified QA pairs;
- more than 1,373 webpages;
- single- and multi-source tasks;
- depth-based difficulty;
- Chinese and English root websites;
- conference, organization, education, and game domains.

## Task contribution

The paper formalizes web traversal as answering a query by navigating downward from a supplied root URL through clickable subpages.

## System contribution

WebWalker separates navigation and evidence management into explorer and critic agents.

## Implementation contribution

The authors report releasing code and data, although those artifacts were not supplied for inspection.

## Experimental contribution

The study compares agent frameworks and model scales, tests commercial and open-source RAG systems, integrates WebWalker with Naive RAG, and varies the inference-time action budget.

# 16. Limitations

## Authors’ stated limitations

From “Limitations and Discussion,” p. 9:

1. **Dataset size:** 680 verified QA pairs is modest; approximately 14,000 additional silver pairs exist but have not been carefully human-verified.
2. **Multimodal environment:** The method uses HTML/DOM button data but not screenshots or other visual modalities.
3. **Agent tuning:** WebWalker is prompt-driven and receives no trajectory-based fine-tuning.
4. **RAG integration:** The experiment supplies WebWalker with the root URL. A fuller system would need to rewrite or route the query to an appropriate official website before vertical traversal.

## Additional evidence-based analyst observations

These are **[D] analyst observations**, not author-admitted limitations:

- The paper supplies no annotator count, qualifications, compensation details, agreement measure, rejection rate, or audit sample.
- Accuracy depends on an LLM evaluator whose reliability is not validated against human judgments.
- No repeated-run variance, confidence intervals, or statistical significance tests are reported.
- Live websites can change, threatening exact reproducibility.
- Only four domains and two webpage languages are represented.
- The supplied root URL removes a major discovery problem from the traversal task.
- Action count excludes failed runs and therefore may underrepresent the cost of weak methods.
- Exact commercial API configurations are deferred to an absent codebase.
- The main text contains numerical and labeling inconsistencies in Figure 3’s distribution description.
- The “nine models” statement does not match the six backbones enumerated in Table 3.
- Table 5’s reported 66-hour answer is not transparently reproducible from the visible schedule.

# 17. Threats to Validity

## Internal validity

Differences may reflect model/API behavior, prompt sensitivity, page availability, or nondeterminism rather than only the framework. Random seeds, repetitions, and decoding details beyond `top_p` are absent.

## Construct validity

Accuracy captures final answer correctness but not evidence faithfulness. The benchmark also conflates navigation, evidence extraction, arithmetic, temporal reasoning, and answer generation.

A.C. is labeled an efficiency measure, but because it includes only successful runs, it does not capture total resource consumption or failure cost.

## Statistical conclusion validity

No error estimates or hypothesis tests are reported. Small percentage differences should therefore not be treated as demonstrated statistically reliable advantages.

## External validity

Generalization is uncertain beyond:

- official, openly accessible websites;
- structured link navigation;
- four selected domains;
- Chinese and English;
- concise entity/judgment answers.

## Ecological validity

Use of live official sites is realistic, but supplying the root URL and restricting actions to clicks simplifies real-world research, where an agent must also identify the correct site, interpret visual layouts, handle search, scrolling, downloads, scripts, and access restrictions.

## Reproducibility

Code and data are reportedly released, but were not supplied. Exact commercial system configurations are in the external codebase, and live webpages may change. Hardware, API snapshots, evaluation dates, and complete decoding configurations are missing.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Use the approximately 14,000 silver QA pairs for training.
- Add screenshot and visual-modal interaction.
- Fine-tune agents on golden navigation trajectories.
- Improve RAG integration by rewriting/routing queries to relevant official sites before traversal.
- Combine horizontally retrieved knowledge and vertically mined evidence.
- Continue investigating action-budget scaling for vertical inference.

## B. Additional open questions

- How stable are results across repeated stochastic runs?
- How accurate and consistent is the GPT-4 evaluator relative to human grading?
- Does critic memory improve evidence quality, or mainly allow more actions?
- How much performance comes from receiving the correct root URL?
- How does the system behave when pages move, disappear, or contain misleading instructions?
- What is the token, latency, and monetary cost per correct answer?
- Can evidence provenance be returned with the answer?
- How would the benchmark handle more than two source pages?
- Are the Figure 3 distribution inconsistencies typographical or data-generation errors?
- Can the Table 5 answer be independently reconciled with its displayed schedule?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model: a model that generates and interprets text |
| RAG | Retrieval-augmented generation: retrieving external documents before answering |
| Web traversal | Following links from a root site to find information |
| Horizontal search | Searching broadly across documents or websites |
| Vertical exploration | Following links deeper into one website |
| Root URL, \(U_{\text{root}}\) | Starting website address supplied to the agent |
| QA pair | A question paired with its ground-truth answer |
| Single-source | A question whose answer depends on one target page |
| Multi-source | A question requiring evidence from multiple pages |
| Depth | Number/level of link transitions needed to reach information |
| Width | Whether multiple sources must be combined |
| Hop | One stage in a multi-step retrieval or reasoning chain |
| DOM | Document Object Model: structured representation of webpage elements |
| ReAct | A pattern alternating reasoning, acting, and observing |
| Reflexion | An agent framework using feedback/reflection |
| Explorer | WebWalker component that selects links |
| Critic | Component that filters evidence, manages memory, and decides when to answer |
| \(T_t\) | Explorer thought at step \(t\) |
| \(A_t\) | Selected link/action at step \(t\) |
| \(O_t\) | Page observation at step \(t\) |
| \(p_t\) | Current page content |
| \(l_t\) | Set of available links/buttons |
| \(H_t\) | Interaction history |
| \(M\) | Critic’s accumulated relevant-information memory |
| \(K\) | Usually maximum action budget; also reused for link-set size in §4.1 |
| acc. | Answer accuracy |
| A.C. | Action count for successful executions |
| Closed-book | Answering without external retrieval |
| Zero-shot | Applying a model without task-specific training examples |
| `top_p` | Nucleus-sampling parameter controlling the probability mass considered during generation |
| Golden path | Annotated link sequence leading to relevant source pages |
| Silver data | Automatically generated data not yet fully human-verified |
| CoT | Chain of thought; here, a step-by-step evaluator prompt |
| Qwen-Agent | Reported foundational agent codebase |
| `crawl4ai` | Reported tool for converting webpages to Markdown-like content |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 680 | QA pairs | Verified WebWalkerQA | Author-reported | p. 2, §1; p. 3, §3.2 |
| Webpages | >1,373 | pages | Dataset coverage | Author-reported | p. 2; Table 1, p. 3 |
| Single-source total | 340 | QA pairs | 80 + 140 + 120 | Analyst-derived | Table 2, p. 4 |
| Multi-source total | 340 | QA pairs | 80 + 140 + 120 | Analyst-derived | Table 2, p. 4 |
| Easy per source type | 80 | QA pairs | Single and multi separately | Author-reported | Table 2 |
| Medium per source type | 140 | QA pairs | Single and multi separately | Author-reported | Table 2 |
| Hard per source type | 120 | QA pairs | Single and multi separately | Author-reported | Table 2 |
| Extra silver data | ~14,000 | QA pairs | Not carefully human-verified | Author-reported | Limitations, p. 9 |
| Default action limit | 15 | actions | Agent experiments | Author-reported | §5.1, pp. 6–7 |
| Context requirement | ≥128K | tokens/context positions | Backbone selection | Author-reported | §5.1, p. 6 |
| Generation `top_p` | 0.8 | probability mass | Implementation | Author-reported | Appendix A, p. 13 |
| Best Table 3 overall | 37.50 | % accuracy | GPT-4o WebWalker | Author-reported | Table 3 |
| GPT-4o WebWalker A.C. | 4.67 | actions | Correct executions only | Author-reported | Table 3 |
| WebWalker gain over GPT-4o ReAct | 3.68 | percentage points | 37.50 − 33.82 | Analyst-derived | Table 3 |
| Closed-book Gemini | 8.08 | % accuracy | Gemini-1.5-Pro | Author-reported | Table 4 |
| Closed-book o1 | 9.85 | % accuracy | o1-preview | Author-reported | Table 4 |
| Best Table 4 overall | 40.73 | % accuracy | Tongyi | Author-reported | Table 4 |
| Kimi single-source easy | 77.50 | % accuracy | Best SS-easy Table 4 cell | Author-reported | Table 4 |
| Naive RAG overall | 20.73 | % accuracy | Google top-10 + Qwen-Plus | Author-reported | Table 4; Appendix B |
| MindSearch overall | 11.32 | % accuracy | Open-source system | Author-reported | Table 4 |
| Language shares | 60.5/39.5 | % | English/Chinese mapping uncertain | Visually readable; mapping disputed | Figure 3, p. 4 |
| Domain shares | 24.0, 46.3, 7.9, 21.9 | % | Figure slices | Visually readable | Figure 3 |
| RAG + WebWalker SS easy | ~0.56 | proportion accuracy | Qwen-Plus integration | Approximate visual estimate | Figure 8 |
| RAG + WebWalker MS hard | ~0.21 | proportion accuracy | Qwen-Plus integration | Approximate visual estimate | Figure 8 |
| WebWalker at \(K=15\) | ~0.34 | proportion accuracy | Qwen-Plus | Approximate visual estimate | Figure 9 |
| WebWalker at \(K=25\) | ~0.35 | proportion accuracy | Qwen-Plus | Approximate visual estimate | Figure 9 |
| MRS case answer | 66 | hours | Inclusive Connections Lounge | Author-reported | Table 5 |
| MRS Fall Meeting | Nov. 30–Dec. 5, 2025 | dates | Boston, Massachusetts | Author-reported | Table 6 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WebWalkerQA is difficult | Best agent result 37.50%; best searched system 40.73% | T3/X1; T4/X4 | pp. 6–8 | Strong descriptive evidence; no uncertainty estimates |
| WebWalker improves overall agent accuracy | Highest overall score for every listed backbone | T3/X1 | p. 6 | Strong within-table pattern; not best in every subset |
| Greater depth makes questions harder | Accuracy generally falls from easy to hard | T3, T4 | pp. 6, 8 | Strong broad trend with local exceptions |
| Multi-source questions are harder | Multi-source averages and hard cells are generally lower | T3, T4 | pp. 6, 8 | Supported descriptively; source count and depth are partly coupled |
| Closed-book knowledge is inadequate | 8.08% and 9.85% overall | T4/X4; T6/X8 | pp. 8, 16 | Strong for tested models, not all possible models |
| Search alone misses deep evidence | Searched systems remain mostly below 41%; performance declines with depth | T4/X4 | p. 8 | Supports difficulty, but does not directly inspect retrieved-document recall |
| Vertical traversal complements RAG | All six Figure 8 categories improve | F8/X5 | pp. 8–9 | Promising; exact values and variance absent |
| More actions can improve performance | Rising curves/bars through moderate \(K\) | F9/X6 | p. 9 | Supports improvement only within tested range; plateau visible |
| Critic memory mitigates noisy long context | WebWalker performance and altered error distribution | T3, F7 | pp. 6–7 | Plausible author interpretation; no isolated memory ablation |
| Conference pages are easier | Radar plot and textual interpretation | F6/X2 | p. 7 | Relative evidence only; exact values unreadable |
| Chinese and English performance are similar | Figure 6 polygons and prose | F6/X2 | p. 7 | Approximate; Figure 3 language-share mapping is inconsistent |
| Finding the page is not sufficient | Reasoning-error category and MRS duration case | F7, T5 | pp. 7, 15–16 | Conceptually supported; Table 5 answer itself may be inconsistent |

# 22. Very Simple Explanation

Imagine asking a person a question whose answer is hidden on a university or conference website. A normal search engine might show the home page, but the person may need to click “Events,” then “Annual Meeting,” then a particular activity page. Sometimes the person must also visit a second page and combine two facts.

WebWalkerQA is a test of whether AI systems can do that. It contains 680 questions, including easy and hard questions and questions needing one or two source pages. Most systems answer fewer than half correctly, so the task remains difficult.

WebWalker divides the job between two AI roles. One role explores links. The other keeps only useful facts and decides when enough information has been collected. This generally works better than the comparison agent methods, but it still solves only about 38% of the complete benchmark with its strongest tested backbone.

The most important idea is that web search and website exploration are different. Search finds likely documents across the web; traversal follows links deeper inside a site. The experiments suggest that using both together works better than search alone, although the paper does not yet show a complete, highly reliable solution.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue | Yes | Yes | Fully represented | ACL 2025 long paper, pp. 10290–10305 |
| Abstract | Yes | Yes | Represented in compressed form | Core problem, benchmark, system, and findings retained |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, scope, task, and contributions covered |
| §2.1 Web-Oriented Benchmark | Yes | Yes | Represented in compressed form | Main categories and Table 1 positioning retained |
| §2.2 Agents on Web-Navigation | Yes | Yes | Represented in compressed form | Trained, prompted, and visual agent lines retained |
| §3.1 Data Collection | Yes | Yes | Fully represented | LLM generation, verification, and human annotation covered |
| §3.2 Data Statistics | Yes | Yes | Fully represented | Counts, types, depth rules, languages, domains, inconsistencies covered |
| §3.3 Web Traversal Task | Yes | Yes | Fully represented | Inputs and objective covered |
| §3.4 Evaluation | Yes | Yes | Fully represented | Accuracy, successful-only A.C., and GPT-4 grading covered |
| §4 WebWalker | Yes | Yes | Fully represented | Explorer–critic architecture covered |
| §4.1 Think then Explore | Yes | Yes | Fully represented | Observation, actions, links, history, and stopping covered |
| §4.2 Think then Critique | Yes | Yes | Fully represented | Memory extraction and sufficiency judgment covered |
| §5.1 Experimental Setting | Yes | Yes | Fully represented | Baselines, models, selection criteria, and settings covered |
| §5.2 Main Results | Yes | Yes | Fully represented | Table 3 results and qualifications covered |
| §5.3 Domains and Languages | Yes | Yes | Fully represented | Relative findings covered; exact radar values uncertain |
| §5.4 Error Assessment | Yes | Yes | Fully represented | All three error categories covered |
| §6.1 RAG Performance | Yes | Yes | Fully represented | Closed-book, commercial, and open-source systems covered |
| §6.2 WebWalker + RAG | Yes | Yes | Fully represented | Integration mechanism and Figure 8 covered |
| §6.3 Action Scaling | Yes | Yes | Fully represented | Tested \(K\) values, trend, and plateau covered |
| §7 Conclusion | Yes | Yes | Represented in compressed form | No separate new evidence |
| Authors’ limitations | Yes | Yes | Fully represented | All four stated categories covered |
| Acknowledgement | Yes | No substantive analysis | Deliberately omitted as non-substantive | Funding and thanks do not change method/results |
| References | Yes textually | Compressed | Deliberately compressed | Bibliographic list not repeated; related-work roles summarized |
| Appendix A | Yes | Yes | Fully represented | Codebase, `top_p`, webpage tool, release claim |
| Appendix B | Yes | Yes | Fully represented | All named RAG systems and Naive RAG procedure |
| Appendix C | Yes | Yes | Fully represented | Availability and Figure 10 |
| Appendix D.1 | Yes | Yes | Fully represented | Root-page search and filtering |
| Appendix D.2 | Yes | Yes | Represented in compressed form | Prompt criteria retained; repetitive wording compressed |
| Appendix D.3 | Yes | Yes | Fully represented | Explorer and critic prompt logic |
| Appendix E | Yes | Yes | Fully represented | Evaluator behavior and limitations |
| Appendix F.1 | Yes | Yes | Fully represented | Reasoning case and numerical discrepancy |
| Appendix F.2 | Yes | Yes | Fully represented | Temporal-cutoff case |
| Figure 1 | Visually inspected | Yes | Fully represented | Multi-source traversal example |
| Figure 2 | Visually inspected | Yes | Fully represented | Dataset pipeline |
| Figure 3 | Visually inspected | Yes | Fully represented | Both distribution inconsistencies noted |
| Figure 4 | Visually inspected | Yes | Fully represented | Architecture and control loop |
| Figure 5 | Visually inspected | Yes | Fully represented | Axes, markers, trend, caveat |
| Figure 6 | Visually inspected | Yes | Fully represented | Exact values uncertain |
| Figure 7 | Visually inspected | Yes | Fully represented | Error segments and qualitative pattern |
| Figure 8 | Visually inspected | Yes | Fully represented | Approximate values explicitly labeled |
| Figure 9 | Visually inspected | Yes | Fully represented | Approximate values and plateau |
| Figure 10 | Visually inspected | Yes | Fully represented | JSON schema and golden-path issue |
| Figure 11 | Visually inspected | Yes | Fully represented | Evaluation prompt |
| Table 1 | Visually/textually inspected | Yes | Fully represented | Cross-reference error noted |
| Table 2 | Visually/textually inspected | Yes | Fully represented | Counts and derived totals |
| Table 3 | Visually/textually inspected | Yes | Fully represented | Main values, best cells, exceptions |
| Table 4 | Visually/textually inspected | Yes | Fully represented | All systems and central values |
| Table 5 | Visually/textually inspected | Yes | Fully represented | Potential arithmetic inconsistency |
| Table 6 | Visually/textually inspected | Yes | Fully represented | Ground truth and prediction |
| Formal research questions | Yes | Yes | Not present | Informal objectives distinguished |
| Formal hypotheses | Yes | Yes | Not present | None manufactured |
| Formal algorithms | Yes | Yes | Not present | Prompt workflow treated as operational specification |
| Numbered equations | Yes | Yes | Not present | All relevant inline notation audited |
| Statistical tests/error bars | Yes | Yes | Missing from paper | Identified as validity limitation |
| Supplementary artifacts | No | Yes | Missing from supplied material | Code, data archive, API configurations, silver set |

## Missing or inaccessible material

- The external GitHub codebase was not supplied.
- The Hugging Face dataset was not supplied.
- The approximately 14,000 silver QA pairs were not supplied.
- Detailed commercial API configurations were deferred to the absent codebase.
- The external live webpages and complete traversal traces were not supplied.
- Hardware specifications, random seeds, repeated-run results, costs, latency, annotation workforce details, and evaluator-validation data are not reported.
- Pages 10 and 12 were not visually rendered, but their supplied text contains references rather than substantive experimental objects.

## Uncertain interpretations

- Figure 3 conflicts with its surrounding prose about language and domain percentages.
- Multi-source difficulty intervals overlap at depths 4 and 6 in the extracted notation.
- \(K\) is reused for link-set size and maximum action budget.
- The formal history \(H_t\) appears to include the current action/observation despite being used to condition that action.
- The “nine models” claim conflicts with the six backbones named and tabulated.
- Figure 6’s exact radar values are not confidently readable.
- Figures 7–9 do not print all exact plotted values.
- Table 4 does not clearly define which rows contribute to its “Avg.” row.
- Figure 10’s Industry Track example contains a seemingly mismatched `student_research_workshop` golden-path component.
- Table 5’s 66-hour answer is not transparently reproducible from the visible schedule.

## Deliberately compressed material

- The reference list was inspected but not reproduced citation by citation.
- Repetitive wording in the annotation verification prompts was compressed into its acceptance and rejection rules.
- The acknowledgements were classified as non-substantive to the scientific contribution.
- Related work was summarized by methodological category rather than by every cited paper.
- Table 3’s complete 108 condition-level numbers remain available in the supplied table; the analysis preserves all overall scores, major extrema, representative subset values, and exceptions rather than duplicating every cell.

## Potential omissions

No known major section, substantive subsection, experiment, figure, table, mathematical definition, contribution, author-stated limitation, or supplied appendix has been omitted. The principal unrepresented materials are external artifacts that were referenced but not supplied, plus bibliographic and repetitive prompt language deliberately compressed as documented above.