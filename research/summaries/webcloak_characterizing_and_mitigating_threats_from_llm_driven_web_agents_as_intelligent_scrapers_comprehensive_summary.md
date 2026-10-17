## Stage 0 — Document Accessibility Report

The supplied main document contains extracted text for physical PDF pages 1–20. All 20 pages can therefore be assessed textually. Seventeen page images are supplied: pp. 1, 2, 5–16, and 18–20. These images were directly inspected; pp. 3, 4, and 17 have text-only coverage. The supplied accessibility metadata reports native text on every page, no low-text pages, and no embedded supplementary files. This report does not independently verify the PDF file or its hash; the supplied source identifier is retained as provenance.

The available sequence reaches the conclusion, references, and Appendices A–E, with no apparent gap in the extracted page sequence. That supports coverage of this supplied 20-page version, but does not establish that every associated artifact or publication supplement is present. Figures 1–9 and Tables 1–15 are available on rendered pages. Their principal structures and values are readable. Figure 3 has dense small labels, so its 160 individual agent-by-website bar segments are not all independently transcribed. Figure 6 has extraction artifacts and stray text in its extracted representation; interpretation follows the visible diagram and surrounding method description rather than treating those artifacts as substantive content. Equations are sparse: the recall fraction is readable, while some diagram notation is less reliable.

Appendices A–E are included. Appendix C provides experimental platforms and prompts, not an executable implementation. The project website, cited repositories, actual benchmark snapshots, annotation records, restoration code, defense-generation prompts, and experimental logs are not supplied or inspected. No browsing, tools, external verification, or OCR was used. Native text was compared with supplied visuals where possible; remaining discrepancies are reported below.

Evidence labels throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. HIGH confidence means clear supplied support, not independent replication. MEDIUM means support exists but reporting or interpretation limits precision. LOW means a material uncertainty remains. UNKNOWN means the supplied work cannot answer the point.

## 1. Plain-Language Orientation

WebCloak studies how large language model (LLM) technology can help people collect website content automatically, especially image URLs. A URL is an address from which a resource can be retrieved. The paper treats a malicious user operating an AI scraper as the attacker and the website owner as the defender. This differs from studying a legitimate assistant tricked by a malicious website: here, the assistant is deliberately being used to scrape a benign site. [A; pp. 1–4]

The researchers built LLMCrawlBench from 237 offline webpage snapshots, drawn from 50 high-traffic websites across five categories, with 10,895 annotated image assets. They first evaluated 32 scraper variants and then examined three leading representatives in more detail: Gemini-2.5-pro generating scraping scripts, Crawl4AI integrating LLMs into extraction, and Browser-Use controlling a browser. Their central architectural observation is that agents usually cannot economically process an entire large webpage directly. Instead, software first parses and reduces its structure; the LLM then interprets the reduced content. [A; pp. 2, 5–7]

WebCloak attacks both dependencies. Its structural layer changes image tags, attribute names, and resource representations, while JavaScript restores their visible appearance for people. Its semantic layer places hidden, optimized text around assets to confuse extraction-oriented LLM interpretation. In the ordinary tested configurations, the paper reports zero image-scraping recall with the full defense. Under some adaptive conditions, however, small nonzero recall remains. The headline reduction from 88.7% to 0% refers to a selected high-vulnerability comparison subset; other whole-benchmark baselines are reported separately and inconsistently. [A; pp. 8–12]

The central contribution is a combined benchmark, measurement study, and website-owner defense. It is not a direct experiment comparing standalone LLM security with web-agent security. For the requested research question, its relevance is **analyst inference**: connecting a model to webpage parsing and browser workflows adds structural dependencies and channels through which untrusted page content can influence behavior. The paper demonstrates those dependencies in scraping systems, but does not establish how much more vulnerable an agent is than the same model used alone. [D; pp. 3–4, 7–9]

## 2. Document Roadmap

**Document identity.** The original title is *WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers*. Authors are Xinfeng Li, Tianze Qiu, Yingbin Jin, Lixu Wang, Hanqing Guo, Xiaojun Jia, XiaoFeng Wang, and Wei Dong. The title page lists Nanyang Technological University, Hong Kong Polytechnic University, and University of Hawaii at Manoa; Wei Dong is marked corresponding author. Appendix D identifies a meta-review for the 2026 IEEE Symposium on Security and Privacy. This is supplied publication-process information, not externally verified publication status. Three artifact badges appear on p. 1: available, functional, and reproduced. Their presence does not substitute for inspecting those artifacts. [A/B]

**Type.** This is a mixed cybersecurity, computer-systems, empirical measurement, and benchmark paper. It includes a defense-generation procedure and two user studies. It is neither a systematic literature review nor a theoretical proof paper.

**Inventory.** S1 Introduction and abstract, pp. 1–3; S2 Background and Related Work, §§2.1–2.3, pp. 3–4; S3 Threat Model, §§3.1–3.3, p. 4; S4 LLMCrawlBench Construction, p. 5; S5 Large-Scale LLM Crawler Measurement, §§5.1–5.3, pp. 5–8; S6 WebCloak: Dual-Layer Protection, §§6.1–6.3, pp. 8–9; S7 Evaluation, §§7.1–7.5, pp. 9–13; S8 Discussion, including limitations and ethical practices, pp. 13–14; S9 Conclusion, p. 14. Acknowledgments and 67 references occupy pp. 14–16.

Appendix A has A.1 website curation, A.2 snapshot preprocessing, and A.3 image annotation. Appendix B describes measurement supplementary details and points to a standardized script-generation prompt. Appendix C contains C.1 platforms, C.2 task prompts, C.3 adaptive-adversary prompts, C.4 audio/text generalization, and C.5 usability study. Appendix D includes D.1 summary, D.2 contributions, D.3 acceptance reasons, and D.4 concerns. Appendix E responds to those concerns. Figures F1–F9 and Tables T1–T15 retain original numbering below. E1 identifies the recall fraction on p. 10. ALG1 identifies the described iterative semantic-defense procedure, which is prose rather than numbered pseudocode. No theorem, lemma, formal hypothesis, or keyword list is supplied.

The logical sequence is: characterize misuse → build a repeatable testbed → identify operational dependencies → construct a two-layer defense → test extraction, adaptation, usability, and cost → discuss boundaries. Appendix D supplies independent review concerns within the document, and Appendix E supplies the authors' response; both materially qualify the novelty and effectiveness discussion.

## 3. Background and Context

**Web scraping** means automatically extracting website content. The paper distinguishes simple Hypertext Transfer Protocol (HTTP) requests with parsing libraries from browser automation capable of executing JavaScript. Hypertext Markup Language (HTML) describes webpage elements; the Document Object Model (DOM) is their structured representation used by browser and automation software. Tags such as `<img>` identify images, while `src` and `srcset` identify image resources or alternatives. Cascading Style Sheets (CSS) control presentation. [A; pp. 3, 8, 16]

Three paradigms matter. **LLM-to-Script (L2S)** uses natural-language requests to generate code, usually Python; that code performs scraping and may require correction. **LLM-Native Crawlers (LNCs)** integrate LLMs into extraction pipelines and commonly use simplified HTML. **LLM-based Web Agents (LWAs)** operate browsers using DOM or accessibility information, screenshots, or both. LWA is a category, not a guarantee that every tested agent sees the same inputs. [A; p. 3]

A **context window** limits how much model input can be processed at once. The paper reports average raw HTML length of 332,079 tokens and cites example limits of 128k and 200k tokens. Those are author-provided contextual comparisons; they were not checked against current product specifications. **Markdown conversion** turns HTML into a shorter textual format. **Parse-then-interpret** names the dependency between non-LLM structural preprocessing and subsequent LLM semantic processing. L2S differs: it commonly generates a parser from general web knowledge instead of itself reading the whole page. [A; pp. 2, 7]

**Prompt injection** in this paper is page-carried text that attempts to redirect the model away from the user's extraction objective. WebCloak uses it defensively. The same text is untrusted evidence for this analysis: none of the supplied example instructions were followed. **Polymorphic** structural protection means the representation changes between sessions. A **cryptographically secure pseudorandom number generator (CSPRNG)** produces randomized structural identifiers. **Shadow DOM** is the named restoration mechanism in which the authors say recovered URLs are stored with reduced visibility to agent automation. No browser-level impossibility guarantee is proved. [A; pp. 8–9]

## 4. Research Problem and Gap

**Existing problem.** Valuable public-facing content can be harvested without the owner's authorization. The authors emphasize images, intellectual-property concerns, unauthorized aggregation, and the ability of natural-language-controlled tools to lower the technical barrier. Their examples of real-world abuse are literature/background claims, not incidents experimentally investigated here. [A; pp. 1, 3]

**Shortcomings of prior approaches, according to the authors.** Traditional scripts require site-specific maintenance. Internet Protocol (IP) and User-Agent checks can be spoofed; CAPTCHAs face multimodal-model challenges; behavioral analysis has per-request costs. Static code obfuscation can fail once a browser renders a readable DOM. Existing agent benchmarks emphasize benign task success and generally lack image-scraping ground truth. Prior agent-security studies mostly consider the agent as victim rather than as an attacker-operated scraper. [A; pp. 1, 3–5]

**Research gap.** The paper seeks systematic measurement across scraper paradigms and a defense grounded in their common operational mechanisms. Its claim to be the first such systematic characterization is an author novelty claim; the supplied paper alone cannot verify priority across all literature. [A; pp. 2, 4]

**Motivation and scope.** The intended intervention is lightweight protection inside the page rather than expensive centralized detection. The target is scalable misuse by novice-to-intermediate operators, not every possible extraction method or expert attacker. The defender should retain the human-visible content. This creates a deliberate asymmetry: humans are intended to see the same page while automated structural and semantic extraction becomes harder. [A; p. 4]

## 5. Research Questions / Objectives / Hypotheses

The introduction states three questions: **RQ1:** how feasible current LLM-driven agents are for illicit extraction from real-world websites; **RQ2:** their underlying mechanisms, failure modes, and exploitable dependencies; **RQ3:** how owners can defend effectively, robustly, and lightly while preserving user experience. These are answered by the measurement, mechanism analysis, and defense evaluation respectively. [A; p. 1]

Section 7 reuses question labels differently: §7.2 is RQ1 effectiveness, §7.3 RQ2 robustness, §7.4 RQ3 usability, and §7.5 RQ4 overhead. These are evaluation dimensions, not the same numbering as the introductory questions. Both systems are preserved rather than silently merged. [A; pp. 10–13]

Explicit objectives include comparing 32 variants, selecting representative strong scrapers, quantifying effort and resource costs, constructing an image-specific reproducible benchmark, and assessing a dual-layer defense against adaptation and across environments. No formal null or alternative hypotheses, preregistered decision rules, or significance thresholds are specified. The requested question about agents versus standalone LLMs is an external analytical framing supplied by the user, not an experimental question tested by this paper.

## 6. Assumptions / Threat Model

The **attacker** is a malicious operator seeking automated, unauthorized extraction of images, audio, or text with little manual effort and low cost. The attacker can use L2S, LNC, or LWA systems, configure prompts, inspect source and DOM, and understand HTML, CSS, and JavaScript. Knowledge-guided adaptation may provide a protected page and restoration script to an LLM for reverse engineering. [A; §3, p. 4]

The assumed operator is novice-to-intermediate and prioritizes scale. The model excludes sustained expensive per-session manual code repair, modification of core closed-source agent logic, and intensive per-site jailbreak optimization. Highly resourced bespoke attackers fall outside the intended protection claim. Thus low measured recall does not imply that resources are cryptographically inaccessible or that all methods of copying a human-visible asset have been eliminated. The latter is an analyst interpretation of the stated scope. [A/D]

The **defender** controls the webpage representation and can insert transformations, restoration JavaScript, and optimized semantic cues. Legitimate users are expected to execute JavaScript. The defense aims for visual transparency, extraction reduction, adaptive robustness, and practical integration. The page's appearance is trusted for usability purposes; its hidden text is deliberately adversarial to scraper interpretation. The supplied design does not formalize a comprehensive trusted-computing base or access-control proof. [A; pp. 4, 8–9]

An important scope distinction is that the experiments run on local snapshots, despite frequent wording about threats to live websites. The live-web origin supplies realistic content and layout, but local execution does not directly test continuous production behavior, authenticated interactions, or changing server responses. [A/D; pp. 5, 14, 16]

## 7. Methodology

### Benchmark and annotation

LLMCrawlBench contains 237 distinct pages from 50 sites in marketplaces, lifestyle, design, travel, and entertainment. Selection favors high traffic, complex layouts, and dense valuable visual assets. The authors report 10,895 unique image assets and mean HTML length 332,079 tokens. There is no model-training dataset or train/validation/test split described: this is an evaluation benchmark. [A; pp. 5, 16]

To freeze changing content, the authors saved offline HTML and local assets. They neutralized nonessential or problematic scripts, localized CSS/fonts/images, rewrote resource paths, and simplified responsive `srcset` to a high-resolution local `src`. Each page was compared visually with a timestamped screenshot of the live counterpart. The purpose was repeatable rendering with minimal necessary intervention. The supplied work does not quantify fidelity verification error or provide the screenshots used for all 237 comparisons. [A; Appendix A.2]

Candidate images came from `<img>` tags and CSS `background-image` properties. Filters removed images smaller than 64×64 pixels, filenames containing logo/icon/avatar/spinner indicators, and non-content locations such as navigation, headers, and footers. Trained annotators then selected semantically relevant main-content images. Annotator count, agreement statistics, adjudication rules, and a per-category page allocation are not supplied. The benchmark target is therefore main-content extraction, which is narrower than literally every visible image. [A/D; Appendix A.3]

### Scraper measurement

Phase 1 tests 19 L2S models, five LNC tools, and eight LWAs on five pages, one per category. Phase 2 tests Gemini-2.5-pro, Crawl4AI, and Browser-Use on all 237 pages. Default requests ask for image URLs. Appendix C includes more specific requests and an L2S prompt that asks for Python code, URL JSON output, downloads, and an image count, while suggesting browser automation for dynamic content. These are reported experimental inputs, not instructions for this analysis. [A; pp. 6–7, 17]

The expert/novice comparison uses five experts and five novices. Experts manually implement scraping; novices use the three representative tools. Perceived difficulty and manual effort use five-point scales. The usability study is separate: 35 participants inspect randomized pairs of original/protected versions of five pages and answer five questions on a seven-point scale. Participant selection, demographic distributions, and formal statistical tests are not reported. [A; pp. 6–7, 18]

### Structural protection

Part 1 first normalizes nonstandard source attributes, then changes structural representations per session. Random attributes replace conventional resource cues; image tags may become `<div>` elements; encoded or encrypted resource values and honeypot `src` values may be inserted. A separate JavaScript snippet restores the display after DOM loading. The authors describe preserving obfuscated attributes and storing recovered URLs in Shadow DOM, with CSS-background presentation mentioned as an alternative to direct image `src` representation. [A; pp. 2, 8]

The paper calls critical URLs encrypted but does not specify a cryptographic algorithm, key handling, or a formal secrecy property. The experimentally supported goal is confusing the tested parsing pipelines while retaining display, not proving resource confidentiality against arbitrary client instrumentation. [A/D]

### Semantic protection: ALG1

Part 2 identifies three zones per target image: **pre**, hidden text before it; **intra**, its `alt` attribute; and **post**, hidden text after it. Random tags and CSS styles hide added elements from people. Content strategies include misleading asset descriptions, safety/policy warnings, and attention diversion or honeypots. The authors optimize these cues to survive the simplified representation consumed by agents. [A; p. 9]

A Defend LLM, exemplified by GPT-4o-mini, generates candidate triples of snippets for a small template group. An Attack LLM, exemplified by GPT-4o, attempts extraction from simplified minimal HTML containing those targets. Candidate protection rates are scored; top-performing strategies are refined, including combinations of effective ideas. Iteration stops at a maximum depth or when enough variants perfectly block targets. The winning template is adapted to other images and inserted into the full page. `branchfactor`, `top_k`, depth, and success-count stopping parameters are named but their numerical settings are not supplied. [A]

Construction order matters: semantic optimization and insertion occur first on the original page context; structural obfuscation follows. Figure 4's conceptual pairing should not be read as overriding this explicit implementation sequence. [A; §6.3]

### Platforms, comparisons, and reporting

Default execution uses Ubuntu 22.04, Intel Xeon Gold at 2.8 GHz, 128 GB RAM, and Chrome. Additional platforms are macOS 14.1 on a MacBook M1 Pro with 16 GB RAM and Windows 11 on AMD Ryzen 7 7735HS with 16 GB RAM. Browser robustness includes Chrome, Firefox, Brave, Edge, and Safari. Exact tool releases, browser versions, API snapshots, decoding settings, random seeds, run counts, and confidence intervals are not specified. [A; pp. 6, 16]

Baselines are original snapshots, full-code obfuscation, dynamic JavaScript loading, static target-tag replacement, and naive unoptimized semantic interference. Original snapshots retain existing site complexity and anti-scraping measures. Metrics include recall, precision, minimal viable recall, execution time, token consumption, CPU/memory percentages, Lighthouse loading measures, visual similarity, and subjective ratings. Reporting inconsistencies in definitions and aggregates are retained in Sections 13–14.

## 8. Experiments / Analyses

**X1 — Broad feasibility, introductory RQ1.** Thirty-two variants operate on five category-representative pages. Table 1 and Figure 3 assess operational status and extraction. The authors report 84.4% can extract multiple correct images, while 30 of 32 are runnable. Top-performing recall entries are 84.2% L2S, 98.0% LNC, and 99.3% LWA. Minimal viable recall is separately 73.7%, 76.0%, and 25.0%. Five pages are a screening sample, not the full benchmark. [A; p. 6]

**X2 — Expert/novice effort.** Five experts and five novices compare manual development with tool assistance. Manual coding takes 31:31, Gemini L2S 01:27 or 04:01 on dynamic pages, Crawl4AI 02:03, and Browser-Use 04:09. Experts report difficulty 4.8, reduced to 3.2 when LLM queries are allowed; novice difficulty is 2.3, 1.3, and 1.5. The small study supports lower reported effort; exact comparative extraction-success scores are not included in Table 2. [A; pp. 6–7]

**X3 — Full-benchmark scraper profiles, RQ1/RQ2.** Three selected agents run across 237 pages. Table 4 gives recall/precision of 65.0/78.5 for Gemini, 71.0/81.7 for Crawl4AI, and 60.4/88.8 for Browser-Use. Token overhead is 9,998, 32,518, and 15,053. Table 3 gives category variation. Strong representatives demonstrate feasibility but are not an unbiased estimate of every available agent. [A/D; p. 7]

**X4 — Mechanism analysis, introductory RQ2.** Figures 1 and 9 and §5.3 connect large HTML inputs with simplification and code-generated parsing. The authors identify predictable structural representations and LLM interpretation as distinct intervention points. The supplied work describes this as empirical investigation but does not present instrumented traces or a formal frequency count for every pipeline. [A/D; pp. 2, 7–8, 19]

**X5 — Full-benchmark defense, evaluation effectiveness.** §7.2 reports initial recall 57.5%, 62.5%, and 54.4%, then 0.0% for all three with WebCloak. Those baseline values differ from Table 4's whole-benchmark scraper characterization. No explanation or separate whole-benchmark result table resolves the difference. [A; p. 10]

**X6 — Defense-baseline comparison.** Twenty-seven deliberately difficult pages from Walmart, Allrecipes, Behance, Booking.com, and Eventbrite are selected for high baseline recall. Table 5 compares four alternatives with WebCloak. The latter has zero recall and precision for all agents; original recall is 93.1%, 95.3%, and 77.7%. The selected sample explains the headline 88.7% average and should not be equated with the entire benchmark. [A; pp. 10–11]

**X7 — Instruction variation.** Default, targeted, conditional, and adversarial extraction requests yield varying unprotected performance in Table 6, but all reported protected recall/precision entries are zero. Exact sample allocation per prompt type is not restated. Targeted descriptions differ between the generic main-product-image example and the recipe-image template; these are distinct reported examples. [A; pp. 11, 17]

**X8 — Audio/text generalization.** Ten supplementary evaluation pages comprise five music pages and five news pages. Audio extraction targets `.mp3` URLs; text tasks target content snippets, with the supplied template requesting paragraphs containing specified text. Table 7 reports all protected values as zero. Its text aggregate and the adjacent description conflict with per-agent values, limiting confidence in the aggregate. [A; pp. 11, 18]

**X9 — Backend switching.** Crawl4AI is evaluated with four LLM backends. Table 8 reports zero protected recall throughout. Nearby prose reports a DeepSeek-V3 outlier producing 2.9% recall. The disagreement is unresolved. This experiment supports broad backend coverage, but not an unequivocal all-backends-zero conclusion. [A; p. 11]

**X10 — Part 1 adaptation.** Static target replacement is compared with dynamic structural obfuscation under naive and adaptive attempts. L2S recall rises from 0 to 52.3% for the static baseline, versus 0 to 0.13% for Part 1. Crawl4AI rises to 2.7% versus 0.22%; Browser-Use remains zero in both. These are layer-isolation results, not the full-defense ordinary configuration. [A; pp. 11–12]

**X11 — Part 2 removal.** Crawl4AI and Browser-Use operate against the semantic layer alone while increasing proportions of its cues are removed. At 90% removal, recall is 30.5% and 21.2%; Figure 7 shows substantial recovery at complete removal. L2S is excluded because the layer primarily targets interpretation-oriented agents. The prose incorrectly refers to isolating Part 1's resilience although the stated setup isolates Part 2. [A/B; p. 12]

**X12 — Full-defense adaptive adversaries.** Refined, knowledgeable, and multi-turn knowledgeable attacks test increasing information and refinement. Table 10 gives refined recall 0/0.22/0; knowledgeable 0.20/1.58/0; and multi-turn L2S 0.30%. The latter is not applicable to the tested sessionless Crawl4AI/Browser-Use configurations. This evaluates two to three refinement turns, not unrestricted adaptation. [A; pp. 12, 17–18]

**X13 — Environment robustness.** Browser-Use with WebCloak has reported recall 0.0% across five macOS browsers and Chrome on Windows/Ubuntu. No per-environment detailed result table is supplied. [A; p. 12]

**X14 — Human usability.** Five randomly selected pages are assessed with loading metrics, visual similarity, and 35 participants. Ratings are 1.42–1.77 on the seven-point negative-impact scale; Figure 8 gives disagreement rates 89.1–99.4%. No uncertainty or significance tests accompany these values. Loading prose conflicts with Table 11. [A/B; pp. 13, 18–19]

**X15 — Overhead and dynamic-content simulation.** Tables 14–15 assess size/tokens and generation/restoration time. Average file-size increase is reported as 20.8%, token increase 6.4%, server generation 179.7 s, and client restoration 0.052 s. Part 1 alone averages 13.0 ms/page; Part 2 dominates generation. A preliminary content-update simulation is described favorably without sample size, update regime, or numerical outcomes. [A; pp. 13, 19]

## 9. Results

The strongest supported findings are conditional. First, many tested tools can extract assets with simple requests, but operational maturity varies: ScrapeGraphAI has JSON parsing failures, Proxy Lite returns hallucinatory URLs, SeeAct omits source attributes, and UI-only tools struggle with multi-step saving. These are observed author-reported failures in tested configurations, not inherent impossibility results. [A; p. 6]

Second, extraction quality differs: Crawl4AI leads Table 4 recall at 71.0%; Browser-Use leads precision at 88.8%; Gemini script generation is comparatively flexible but may require debugging or Selenium. Category dependence is substantial: Crawl4AI marketplace recall is 45.4%, versus lifestyle 82.5%; Browser-Use travel precision is 99.8%. A single mean hides those differences. [A; p. 7]

Third, ordinary full-defense evaluations report zero recall, whereas full-defense knowledgeable adaptation produces up to 1.58% for Crawl4AI in Table 10. The conclusion should therefore be 'zero in the reported ordinary conditions and very low in the modeled adaptive conditions,' rather than universal prevention. [A/D; pp. 10–12]

Fourth, static structural defenses can look strong before adaptation. Table 5's static replacement already blocks Crawl4AI and Browser-Use in the initial condition. The added value of dynamic protection is clearer in the adaptive comparisons and its L2S protection, not merely in an initial all-agents average. [A/D; pp. 10–12]

**Derived numerical distinction.** Table 5 original recalls average to (93.1 + 95.3 + 77.7)/3 = 88.7%. Moving from that average to zero is an 88.7-percentage-point reduction, or a 100% relative reduction within that specific experiment. It is not an 88.7% relative reduction. Table 4's recalls average to (65.0 + 71.0 + 60.4)/3 = 65.4667%, while §7.2's whole-benchmark baselines average to (57.5 + 62.5 + 54.4)/3 = 58.1333%. These derived averages expose different conditions/reporting; they do not reconcile the discrepancy. [C]

Usability findings indicate small perceived impact for the sampled users and pages, with close rendered similarity. They do not establish perfect accessibility or functionality across every application. The loading table contains larger delays than the narrative's illustrative claim. Generation is roughly three minutes per page, whereas client restoration is roughly 52 milliseconds; calling both simply 'low overhead' obscures this deployment distinction. [A/D]

## 10. Figure-by-Figure Interpretation

### Figure 1 — Parse-then-interpret mechanism, p. 2

A diagram shows dense webpage input → Agent Parse → simplified content → Agent Interpret. Attacker-prompt guidance enters interpretation, with a feedback-style arrow suggesting guidance around that stage. The dense input is labeled averaged 332k tokens; reduced content can be about 1k tokens. These are diagram labels, not a reported universal compression ratio. No axes or statistical uncertainty apply. It supports the two dependency points used by WebCloak. [A/B]

### Figure 2 — Benchmark construction, p. 5

Panel (a) displays the five content categories and challenges from dynamic content, A/B testing, and personalization. Panel (b) flows from selection of 50 websites through offline snapshots to preprocessing of 237 pages, then annotation with automated asset statistics and manual verification. Panel (c) lists five categories, 50 websites, 237 pages, 10,895 images, and 332,079 mean tokens. A lower strip groups reproducibility, image-specific ground truth, and systematic evaluation contributions. This is a pipeline, not a statistical plot; the token count is an average per page. [A/B]

### Figure 3 — Thirty-two screening variants, p. 6

Horizontal stacked bars list scraper variants vertically and sum recall across five websites horizontally, reaching up to 500%. Website categories use different fills; agent names are blue for L2S, green for LNC, and red for LWA. The x-axis total is a sum of five percentages, not recall above 100% on a single page. Individual segment labels are percentages. High totals for leading tools contrast with zero/low bars for several agents. Small segment labels are not all confidently transcribed; Table 1 and prose provide the main numerical findings. No error bars or run variability are shown. [B]

### Figure 4 — Two-layer architecture, p. 8

An original page feeds Dynamic Structural Obfuscation and Optimized Semantic Labyrinth, which combine into a WebCloak page. The plus/combination symbol communicates complementary protection. Actual construction order is semantic insertion first, structural transformation second according to §6.3. The figure is conceptual and does not specify an API, timing budget, or execution schedule. [A/B]

### Figure 5 — Structural transformation and restoration, p. 8

The diagram contrasts standard image markup with nonstandard randomized representation. A central flow labels CSPRNG, obfuscation, honeypot, and keep-as-is operations. A lower user-side path connects original and protected pages that look identical, with post-loading de-obfuscation and a de-obfuscator, and identifies Shadow DOM in the resulting representation. The exact code strings are examples; no particular random identifier is a required system constant. The key separation is visible rendering versus the structural cues encountered by automation. [A/B]

### Figure 6 — Semantic-defense optimization, p. 9

The left portion initializes pre/intra/post injection points and illustrates repeated Defend-LLM/Attack-LLM interaction, simplification, and final selection. The right portion contrasts original image markup with added hidden warnings and altered descriptive attributes. Arrows represent candidate construction, attack evaluation, and iterative refinement. There are no quantitative axes. Extracted diagram text contains duplicated content, notation corruption, and an apparent editorial comment; those are not used as method claims. The visible figure and §6.2 support the interpretation. [A/B]

### Figure 7 — Semantic-layer removal stress test, p. 12

The x-axis is percentage of defensive prompts removed, 0–100%; the y-axis is recall, 0–100%. Blue circles represent Crawl4AI and orange squares Browser-Use. Both stay low over earlier removal levels and rise sharply near complete removal. Reported 90%-removal values are 30.5% and 21.2%; final visible labels at 100% removal are 97.1% and 85.0%. Other visible annotations include 12.8%, 11.8%, and 20.1%, but not all are assigned to exact removal positions here because small-label association is less certain. No error bars appear. This tests Part 2 alone, not combined protection. [A/B]

### Figure 8 — User ratings and disagreement, p. 13

Five paired bar groups correspond to Q1–Q5. Blue bars use the left axis, average rating on a 1–7 scale, lower better. Orange bars use the right axis, disagreement percentage, higher better, because statements describe negative effects. Exact means are 1.67, 1.42, 1.55, 1.77, 1.55; percentages are 90.00%, 99.40%, 89.70%, 89.10%, 91.40%. A disagreement threshold of ≤3.0 appears in the caption. The percentage denominator is unclear because percentages do not correspond to simple single-response counts out of 35. No error bars or significance markings appear. [A/B/D]

### Figure 9 — HTML token distribution, p. 19

A histogram places token count on the horizontal axis with a ×10^6 multiplier and webpage count vertically, approximately 0–25. The horizontal display reaches about 1.6 million tokens. Many pages cluster toward the lower end, with a long tail and occasional very large pages. The caption says most exceed 200,000 tokens and argues direct full-HTML LLM processing is impractical. Exact bin boundaries, tokenization method, and per-bin counts are not supplied, so no independent median or percentile is calculated. This supports large-input motivation without proving every current model incapable of reading each page. [A/B/D]

## 11. Table-by-Table Interpretation

### Table 1 — Paradigm screening, p. 6

Rows L2S/LNC/LWA contain 19/5/8 variants, with 19/4/7 runnable. The No.1 recall column is 84.2/98.0/99.3%; the separate minimal viable recall (MVR) column is 73.7/76.0/25.0%. Its note defines MVR as the ratio of crawlers extracting at least one image URL on each website. Prose labels the top-performing numbers as MVR, conflicting with the column distinction. The operational results show that runnable and successful are different concepts.

### Table 2 — Human effort, p. 7

Manual experts N=5: 31:31, difficulty 4.8→3.2, manual level 5.0. Novices N=5: Gemini 01:27/04:01, difficulty 2.3, manual level 3.1; Crawl4AI 02:03, 1.3, 1.2; Browser-Use 04:09, 1.5, 1.2. The expert arrow means allowing LLM queries while core logic remains self-implemented; 04:01 denotes dynamic pages requiring Selenium. The difficulty heading has an upward arrow despite prose treating lower difficulty favorably. There is no uncertainty or extraction-success column.

### Table 3 — Category performance, p. 7

Entries below are recall/precision percentages in marketplace, lifestyle, design, travel, entertainment order. Gemini: 53.8/77.6; 71.9/82.0; 71.5/83.0; 74.1/84.5; 62.2/68.5. Crawl4AI: 45.4/78.7; 82.5/86.2; 76.8/85.0; 61.6/69.1; 82.7/80.9. Browser-Use: 54.5/86.8; 58.0/84.7; 58.1/91.1; 70.5/99.8; 60.9/82.0. Crawl4AI has top recall in lifestyle/design/entertainment; Gemini in travel; Browser-Use in marketplaces. Browser-Use has strongest precision in most categories, but Crawl4AI leads lifestyle. No confidence intervals are given.

### Table 4 — Overall quality and resources, p. 7

Gemini has recall 65.0%, precision 78.5%, 9,998 tokens, CPU 2.61%, memory 0.11%; Crawl4AI 71.0%, 81.7%, 32,518, 2.48%, 0.24%; Browser-Use 60.4%, 88.8%, 15,053, 2.66%, 0.39%. CPU/memory are fractions of total system resources during scraping, not monetary costs or peak-memory bytes. The aggregation and token-accounting rules are not fully specified.

### Table 5 — Baseline defenses, p. 10

Pairs are recall/precision percentages, Gemini; Crawl4AI; Browser-Use. Original: 93.1/84.1; 95.3/84.5; 77.7/92.3. Full-code obfuscation: 0/0; 95.3/84.5; 74.6/91.0. Dynamic JS loading: 0/0; 89.8/87.0; 74.3/91.7. Static target obfuscation: 9.8/62.3; 0/0; 0/0. Naive semantic interference: 81.8/81.8; 80.5/82.6; 57.8/86.1. WebCloak: 0/0 for all. Lower values favor the defender. Sample: 27 selected vulnerable pages. The static baseline's strong initial results qualify blanket statements that all structural alternatives fail immediately.

### Table 6 — Task instructions, p. 11

Unprotected recall/precision in default, targeted, conditional, adversarial order: Gemini 93.7/84.1, 44.8/67.5, 24.3/41.3, 92.3/82.7; Crawl4AI 95.3/84.5, 99.0/94.4, 74.3/99.1, 93.4/83.8; Browser-Use 77.7/92.3, 93.9/92.3, 81.4/98.8, 85.1/100.0. All protected entries are zero. Gemini's default 93.7 differs from Table 5's 93.1; the supplied material does not explain the condition or measurement difference.

### Table 7 — Other assets, p. 11

Audio unprotected recall/precision: Gemini 71.4/70.0; Crawl4AI 85.7/78.3; Browser-Use 95.2/90.0; average 84.1/79.4. Text: Gemini 100.0/26.6; Crawl4AI 80.3/83.6; Browser-Use 88.2/94.4; printed average 60.4/37.0. Every protected number is zero. The printed text average cannot be an ordinary arithmetic mean of the listed agents. Adjacent prose also associates aggregate numbers with Gemini. Preserve row values and mark the aggregate unresolved.

### Table 8 — Crawl4AI backends, p. 11

Unprotected category recalls, marketplace/lifestyle/design/travel/entertainment, then printed average: ChatGPT-4o 69.9/99.7/87.1/98.7/54.1, 88.9; Claude-3.7 41.8/14.9/59.6/77.1/39.3, 41.6; DeepSeek-V3 82.5/70.2/85.9/98.0/96.7, 81.9; Gemini-2.5 84.8/99.0/94.5/100/100, 95.3. All protected entries are zero. Printed averages are not generally simple means of categories, and weighting is unspecified. Prose reports 2.9% residual DeepSeek recall and identifies Gemini-2.5 Flash, while the table label is less specific.

### Table 9 — Structural adaptation, p. 11

Naive→adaptive recall: static baseline L2S 0→52.3%, Crawl4AI 0→2.7%, Browser-Use 0→0%; WebCloak Part 1 L2S 0→0.13%, Crawl4AI 0→0.22%, Browser-Use 0→0%. The dynamic layer has lower adaptive extraction for L2S/LNC. Appendix E pairs 52.3% with 0.22%, crossing agent rows; the like-for-like L2S comparison is 52.3% versus 0.13%.

### Table 10 — Full-defense adaptation, p. 12

Refined attacks: L2S 0.0%, Crawl4AI 0.22%, Browser-Use 0.0%. Knowledgeable: 0.20%, 1.58%, 0.0%. Multi-turn knowledgeable: L2S 0.30%, remaining entries N/A. N/A means not applicable, not zero. Multi-turn uses two to three refinements and is evaluated only for L2S. Prose gives Crawl4AI knowledgeable recall as 1.5%, which is less precise than the table's 1.58%.

### Table 11 — Protected loading, p. 13

Rows list protected FCP/LCP/TTI seconds and performance score, with change from original: Mac Chrome 8.3(+0.88), 17.0(+4.52), 17.4(+4.79), 53.8(−5.20); Mac Edge 8.2(+0.85), 12.5(+2.33), 12.8(+2.50), 53.9(−5.46); Win Chrome 10.4(+0.82), 12.6(+1.07), 12.7(+1.09), 56.2(−0.67); Win Edge 10.5(+0.69), 12.6(+1.00), 12.7(+1.04), 56.2(−0.31). Prose says Mac Chrome LCP increases 0.88 s, but that is the FCP change in the table. The LCP change shown is 4.52 s. No error estimates appear.

### Table 12 — Site coverage, p. 19

Five rows enumerate sites and owner-risk rationales. Marketplaces include Alibaba, Amazon, Autotrader, Craigslist, eBay, Flipkart, JD.com, Lazada, MercadoLivre, Rakuten, Walmart. Lifestyle includes Allrecipes, Bon Appétit, Cup of Jo, Epicurious, Martha Stewart, Poshmark, PureWow, The Kitchn, The Pioneer Woman. Design includes 99designs, Adobe Portfolio, Behance, Canva, Coroflot, Dribbble, Havenly, Houzz, Pinterest, Squarespace, Wix. Travel includes Agoda, Airbnb, Booking.com, Explore, Google Travel, Kayak, TripAdvisor, Trip.com, Trivago. Entertainment includes Bleacher Report, CBS Sports, Ditto Music, Eventbrite, IMDb, Meetup, Rotten Tomatoes, Spotify, Ticketmaster, Yahoo Sports. The table does not provide page counts by category. Appendix A's examples include IGN and Bandcamp, which are not in this table; the discrepancy is unresolved.

### Table 13 — Rendered similarity, p. 19

Five scores are 0.0014, 0.0015, 0.0021, 0.0099, and 0.0016, versus unrelated-page reference 0.5261. Lower means more similar. The prose names Jelinek-Chelba Divergence (JCD), but no calculation or implementation definition is supplied. Close scores support visual similarity for five pages, not proof of identical behavior or accessibility.

### Table 14 — Size/token growth, p. 19

In marketplace/lifestyle/design/travel/entertainment order, MB original→protected: 0.56→0.71, 1.17→1.33, 0.56→0.59, 0.65→0.87, 0.43→0.58; reported increments 26.8/14.3/5.4/32.7/34.6%, average 20.8%. Average sizes are 0.69→0.83 MB. Thousand-token pairs: 209→237, 394→408, 247→252, 273→301, 143→168; increments 13.8/3.6/2.1/10.4/17.5%, average 6.4%; average counts 257→273k. Display rounding can affect recomputed percentages. The 257k baseline differs materially from the benchmark's 332,079-token mean, without an explained denominator or preprocessing distinction.

### Table 15 — Generation/restoration time, p. 19

Server seconds across the five categories: 146.6, 266.9, 233.2, 109.5, 142.1; average 179.7. Client seconds: 0.054, 0.089, 0.062, 0.017, 0.038; average 0.052. Server means generation of the protected HTML; client means restoration execution. Lifestyle has the largest reported costs and travel the smallest. No error bars, repetition counts, or model-price costs are supplied.

## 12. Diagram / Architecture Interpretation

Figures 1, 2, 4, 5, and 6 are the architecture and workflow diagrams; their individual coverage appears above. Together they describe two interacting data paths. The normal scraping path takes source/rendered page structure, reduces it using parsers, and sends selected information to an LLM that decides what to extract. L2S instead has an LLM generate code whose assumptions determine which structures are found. [A]

The protected path starts with original page context. A generation-time optimization loop creates contextual pre/intra/post cues. Those cues and asset elements are then structurally transformed. The delivered page contains nonstandard structure plus restoration code. In the human path, JavaScript reconstructs the intended visual assets. In the agent path, standard parsing may miss true assets or follow honeypots; surviving contextual text can redirect interpretation. [A/D]

The optimizer's feedback is an Attack-LLM extraction result returned to the Defend LLM for refinement. That loop is a preparation procedure rather than a required fresh attack simulation during every human page load. The paper distinguishes expensive generation from lightweight restoration. It does not specify production interfaces, caching invalidation, encryption parameters, or a complete browser observability boundary. [A/D]

## 13. Equations and Mathematical Concepts

**E1 — Recall, p. 10, §7.1:** `R = |C_extract ∩ C_target| / |C_target|`. `C_extract` is the extracted-item set, `C_target` the ground-truth target set, intersection selects correctly retrieved targets, and vertical bars denote set cardinality. Recall measures how much of the desired content was retrieved. Lower recall favors defense. Multiplying the fraction by 100 expresses a percentage. A zero-target convention is not supplied. [A]

Precision is verbally defined as the proportion of extracted items that are correct targets. Its corresponding explanatory identity is `P = |C_extract ∩ C_target| / |C_extract|`; this is a direct formalization of the supplied definition, not a separately numbered author equation. If nothing is extracted, the denominator is zero. Tables report 0.0 precision in blocked conditions, but the implementation convention is not explained. Zero precision could also accompany extraction of incorrect honeypots, so it should not automatically be read as zero output items. [A/D]

On p. 6, recall is described instead as correctly extracted URLs among all extractions, which corresponds to precision under §7.1. This is a definition inconsistency. The p. 10 explicit target-denominator formula is the clearest available recall definition; the p. 6 wording remains flagged rather than silently corrected. [A]

`D_LLM` and `A_LLM` denote defense-generation and attack-simulation models. `p_pre`, `p_intra`, and `p_post` are text snippets for three insertion zones. `branchfactor` denotes candidate-set generation breadth; `top_k` denotes retained strategies; depth denotes iterative refinement level. Values are unspecified. `t_part1`, `t_part2`, and `t_full` denote generation times, not objective functions. [A; pp. 9, 13]

No numbered optimization loss, theorem, proof, or executable pseudocode is supplied. The 'optimization' is scored candidate search and refinement using extraction outcomes. JCD's mathematical definition, tokenization procedure, and exact aggregation formulas for most means are absent. Diagram notation for full DOM and simplified text/Markdown is explanatory; corrupt extracted superscripts are not promoted into equations.

## 14. Interpretation and Discussion

**Introductory RQ1:** The screening, strong representative results, and effort study support the claim that tested LLM-assisted systems can lower the barrier to image extraction. They do not quantify real-world unauthorized scraping prevalence or total economic harm. **RQ2:** The paper identifies structural preprocessing and semantic interpretation as dependencies. The defense's observed effects are consistent with this explanation, although layer-specific traces and broader causal measurements would strengthen it. **RQ3:** The combined defense is effective under the tested threat model and mostly well-rated by sampled users, with significant generation costs and some adaptive residual extraction. [A/D]

For the user's research question, the architecture adds a useful mechanism-level explanation: agents consume untrusted page content through parsers, descriptions, and browser representations, and can act on the model's resulting interpretation. Hidden text can survive simplification and compete with extraction instructions. Structural transformations can also cause failures before the model receives useful evidence. These are different mechanisms: prompt susceptibility is semantic, while missed assets may be parser failure. Treating both as one generic 'LLM vulnerability' would obscure the findings. [D; pp. 7–9]

The paper's cited discussion says some prior agents execute harmful instructions they would refuse in chat, and reference [15] has the user's research-question title. Those are reported literature positions, not this paper's controlled standalone comparison. The actual supplied experiment is agents versus protected/unprotected pages, not agents versus isolated LLMs. Thus comparative vulnerability magnitude remains UNKNOWN from this work. [A/D; pp. 4, 14]

**Unresolved consistency ledger:** (1) Table 4 whole-benchmark recalls 65.0/71.0/60.4 differ from §7.2's 57.5/62.5/54.4. (2) Table 1 distinguishes No.1 recall from MVR, while prose confuses the labels. (3) The p. 6 recall description uses an extraction denominator rather than a target denominator. (4) Table 5 Gemini default recall 93.1 differs from Table 6's 93.7. (5) Table 7 text average 60.4/37.0 conflicts with its rows; the adjacent prose misattributes aggregates. (6) Table 8 zero protected DeepSeek recall conflicts with prose 2.9%; category-to-average weighting is unspecified. (7) Table 10 1.58 becomes 1.5 in prose. (8) Table 11 Mac Chrome LCP change 4.52 s conflicts with prose 0.88 s. (9) Benchmark mean 332,079 tokens differs from Table 14's 257k baseline. (10) Appendix A site examples differ from Table 12. (11) §7 research-question numbering differs from introduction numbering. (12) Appendix B points to Listing C.1 while C.1 is headed Experimental Platforms and the script template follows on p. 17. (13) Part 2-removal prose says it isolates Part 1. (14) Appendix E compares static L2S 52.3 with dynamic Crawl4AI 0.22 instead of like-for-like rows. These cannot all be explained as rounding. [A/B]

## 15. Contributions and Novelty

**Conceptual:** A website-owner-centered agent-as-attacker framing, separating deliberate malicious use from compromise of an otherwise legitimate agent. **Empirical:** A 32-variant screening, three-paradigm detailed comparison, effort observations, and identified operational dependencies. **Dataset/benchmark:** Offline image-rich pages with main-content ground truth and repeatable extraction tasks. **System/methodological:** Two complementary layers combining dynamic representation changes with optimized hidden contextual cues. **Experimental:** Baseline, instruction, backend, adaptation, removal, cross-environment, usability, and overhead studies. [A; pp. 2–14]

No new theorem, standalone model architecture, or model-training algorithm is claimed. The semantic search adapts an iterative adversarial-generation approach cited by the paper. The authors claim first systematic characterization and benchmark priority; those remain unverified author claims in closed-document mode.

Appendix D recognizes a dataset, tool, and useful advance, but questions the extra advantage over standard defenses, absence of social media, and novelty of defensive prompt injection. Appendix E argues that rendered-DOM resilience and adaptive robustness supply the extra advantage. A balanced reading locates novelty primarily in the combined system, threat characterization, benchmark, and dynamic defense evaluation rather than claiming defensive prompt injection itself is new. The latter assessment is analyst interpretation informed by the included review. [A/D; p. 20]

## 16. Limitations

### Authors' stated limitations

JavaScript is required for visual restoration; disabling it can break the intended display. The cited under-0.2% prevalence claim is author-reported background, not verified current prevalence. A determined expert could reverse-engineer a single randomized session, although the authors argue scaling this is expensive. Large-scale evidence is image-centric; audio/text protection is tested on a smaller supplementary set, and a comprehensive multimodal benchmark is needed. Approximately three-minute semantic generation may challenge rapidly changing sites such as social media. Protection is deliberately scoped to novice/intermediate scalable misuse rather than all expert attacks. [A; pp. 4, 13–14]

### Additional evidence-based analyst observations

The supplied work has inconsistent metrics/aggregates and incomplete experimental settings. Two small human studies lack uncertainty reporting. The 27-page comparison subset is selected for vulnerability and cannot estimate average production-site performance. Offline preprocessing can alter dynamic behavior even when visual appearance is preserved. Exact randomization, resource encoding, restoration code, and generation hyperparameters are absent. Browser and backend tests cover selected systems, not all possible models or extraction routes. Similar visuals do not by themselves establish assistive-technology compatibility, identical semantics, or full interaction fidelity. These are analyst observations, not author admissions. [D]

## 17. Threats to Validity

**Internal validity [D]:** Layer effects are supported by isolated adaptation/removal studies, but a complete factorial ablation across the full benchmark is absent. Unresolved baseline differences and recall wording make some cross-experiment comparisons uncertain. Repetition counts and stochastic variability are not reported.

**Construct validity [D]:** URL extraction is used as the main success proxy. It measures retrieval of annotated addresses, not necessarily successful downloads, downstream misuse, or economic loss. Main-content annotation excludes decorative and small assets; a broader extraction objective could yield different judgments. High visual similarity and low negative ratings are narrower than perfect user transparency.

**External/ecological validity [D]:** Fifty source sites and five categories improve diversity, but local frozen pages omit live change, authentication, request traffic, and many interactive conditions. Social media is explicitly identified as absent in the meta-review. Audio/text has only five pages per modality. Five usability pages and 35 participants cannot establish all-platform experience.

**Statistical conclusion validity [D]:** No standard errors, confidence intervals, significance tests, or variability across repeated model calls are shown. A reported 0.0% is an observed outcome at available precision, not a statistical guarantee. User-study disagreement percentages need an explicit response denominator. Weighted versus unweighted category and page aggregation is often unclear.

**Reproducibility [D]:** Snapshots, standardized tasks, platforms, and annotation procedures help, and artifact badges are visible. Nevertheless the supplied package lacks code, dataset files, detailed versioning, seeds, optimization values, and logs. Reproducibility is described and partially supported, not independently demonstrated by this analysis.

## 18. Future Work and Open Questions

**A. Explicit author directions:** Build a comprehensive multimodal benchmark to substantiate broader asset protection; devote more effort to trustworthy and resilient AI agents. The authors also suggest batch transformation and caching as practical ways to manage generation overhead for low-update-frequency content. Their dynamic-image update simulation is preliminary rather than a fully reported future deployment solution. [A; pp. 13–14]

**B. Analyst-derived open questions:** What happens with continuously changing pages or social-media interaction? How does performance vary across repeated model calls and new tool releases? Can the same model be compared directly in standalone and agent configurations with matched malicious content? What fraction of failures comes from parsing versus semantic redirection? Does page protection preserve accessibility semantics and all user interactions? How much operator time and cost is required for adaptive bypass at scale? Which aggregation rules resolve the inconsistent means? Can audio/text findings replicate on a larger benchmark? These are remaining questions, not additional author experiments or demonstrated failures. [D]

## 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model; processes instructions/text and may generate code |
| L2S | LLM-to-Script; model generates a scraping program |
| LNC | LLM-Native Crawler; LLM integrated into extraction pipeline |
| LWA | LLM-based Web Agent; browser actions guided by model input |
| HTML / DOM | Page markup / structured representation of page elements |
| CSS / JS | Presentation rules / JavaScript used for rendering and restoration |
| UI | User interface; visible and interactive webpage components |
| URL | Address identifying a retrievable resource |
| HTTP | Request protocol discussed for conventional scraping |
| IP / User-Agent | Network address / request identifying string used in bot checks |
| CAPTCHA | Human-versus-bot challenge discussed as an existing defense |
| CORS | Cross-Origin Resource Sharing; resource-access constraint relevant to snapshots |
| `img`, `src`, `srcset`, `alt` | Image tag, source address, responsive alternatives, descriptive attribute |
| Parse-then-interpret | Structural simplification followed by LLM understanding |
| Polymorphic cloaking | Session-varying transformation of asset representations |
| CSPRNG | Cryptographically secure pseudorandom number generator for identifiers |
| Shadow DOM | Named client-side representation used in restoration |
| Honeypot | Misleading apparent asset or cue intended to divert extraction |
| Semantic labyrinth | Optimized contextual text that confounds LLM extraction |
| MVR | Minimal viable recall; agents extracting an image on each tested website |
| Rec / Prec | Recall / precision; target coverage versus extracted-item correctness |
| OH | Overhead; resource/time increase or consumption |
| RA / KA / MKA | Refined / knowledgeable / multi-turn knowledgeable attacker |
| N/A | Not applicable; not a successful zero-recall result |
| FCP / LCP / TTI | First Contentful Paint / Largest Contentful Paint / Time to Interactive; conventional name expansions used for the paper's loading abbreviations, whose formal definitions are not supplied |
| JCD | Paper's named Jelinek-Chelba Divergence visual-similarity measure; formula absent |
| IRB | Institutional Review Board; author-reported research approval |
| `C_extract`, `C_target` | Extracted set and annotated target set in recall formula |
| `D_LLM`, `A_LLM` | Defense-generating and attack-simulating models |
| `p_pre`, `p_intra`, `p_post` | Defensive text before, within, and after image markup |
| `branchfactor`, `top_k`, depth | Search breadth, retained candidates, refinement level; values absent |

## 20. Key Numerical Results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark pages / sites | 237 / 50 | counts | Five categories | Author-reported | p. 5, Fig. 2 |
| Annotated image assets | 10,895 | images | Main-content ground truth | Author-reported | pp. 5, 16 |
| Mean HTML length | 332,079 | tokens/page | Benchmark description | Author-reported | pp. 5, 16 |
| Small-image exclusion | <64×64 | pixels | Annotation heuristic | Author-reported | p. 16, A.3 |
| Variant allocation | 19 / 5 / 8 | variants | L2S / LNC / LWA | Author-reported | p. 6, T1 |
| Successful variants | 84.4 | % | Extract multiple correct images in screening | Author-reported | p. 6 |
| Full-benchmark recall | 65.0 / 71.0 / 60.4 | % | Gemini / Crawl4AI / Browser-Use | Author-reported | p. 7, T4 |
| Alternative full-benchmark baseline | 57.5 / 62.5 / 54.4 | % | §7.2; conflicts with T4 | Author-reported | p. 10 |
| Selected-subset mean baseline | 88.7 | % | 27-page T5 comparison | Author-reported | pp. 10–11 |
| T5 mean verification | (93.1+95.3+77.7)/3 = 88.7 | % | Equal mean of agent recalls | Analyst-derived | p. 10, T5 |
| Ordinary protected recall | 0.0 | % | Three representative agents | Author-reported | pp. 10–11 |
| Static vs dynamic adaptive L2S | 52.3 vs 0.13 | % recall | Part 1 isolation | Author-reported | pp. 11–12, T9 |
| Knowledgeable full-defense attack | 0.20 / 1.58 / 0.0 | % recall | L2S / Crawl4AI / Browser-Use | Author-reported | p. 12, T10 |
| Multi-turn L2S | 0.30 | % recall | Two to three refinements | Author-reported | p. 12, T10 |
| Part 2 at 90% removal | 30.5 / 21.2 | % recall | Crawl4AI / Browser-Use | Author-reported | p. 12, F7 |
| Audio/text pages | 5 / 5 | pages | Small generalization study | Author-reported | p. 18, C.4 |
| Expert / novice sample | 5 / 5 | participants | Effort study | Author-reported | p. 7, T2 |
| Manual coding time | 31:31 | MM:SS | Experts | Author-reported | p. 7, T2 |
| Assisted tool times | 01:27 or 04:01 / 02:03 / 04:09 | MM:SS | L2S / Crawl4AI / Browser-Use | Author-reported | p. 7, T2 |
| Usability sample | 35 | participants | Five page pairs | Author-reported | pp. 13, 18 |
| User ratings | 1.67 / 1.42 / 1.55 / 1.77 / 1.55 | 1–7 scale | Q1–Q5 negative impact | Visually readable | p. 13, F8 |
| Mac Chrome LCP increase | 4.52 | seconds | Table contradicts prose 0.88 | Visually readable | p. 13, T11 |
| Similarity scores | 0.0014–0.0099 | score | Five render comparisons | Author-reported | p. 19, T13 |
| HTML size increase | 20.8 | % | Reported average | Author-reported | p. 19, T14 |
| Token increase | 6.4 | % | Reported 257k→273k | Author-reported | p. 19, T14 |
| Part 1 generation | 13.0 | milliseconds/page | Structural layer | Author-reported | p. 13 |
| Full generation / restoration | 179.7 / 0.052 | seconds/page | Server / client | Author-reported | p. 19, T15 |

## 21. Claim–Evidence Map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| LLM-assisted scraping is feasible | 32 variants; 84.4% extract multiple correct images | X1, F3, T1 | p. 6 | HIGH for tested five pages; broader prevalence unmeasured |
| Assistance lowers reported effort | Expert 31:31 versus tool times of roughly 1–4 min | X2, T2 | pp. 6–7 | MEDIUM; small groups, no uncertainty |
| Paradigms trade coverage for precision/cost | T4 quality and tokens differ | X3, T3–T4 | p. 7 | HIGH table support; aggregation details limited |
| Predictable preprocessing is a dependency | Structural simplification and script-generation account | X4, F1/F9 | pp. 2, 7–8, 19 | MEDIUM causal strength; traces absent |
| Full defense blocks ordinary selected tests | Zero protected recall in T5/T6 | X5–X7 | pp. 10–11 | HIGH conditional support, not universal guarantee |
| Dynamic structure resists modeled adaptation | L2S 52.3% static versus 0.13% dynamic | X10, T9 | pp. 11–12 | HIGH for those conditions |
| Semantic layer tolerates partial cue removal | 90% removal leaves 30.5/21.2% recall | X11, F7 | p. 12 | HIGH; layer alone, no uncertainty |
| Full defense permits small adaptive residuals | KA 0.20/1.58/0; MKA L2S 0.30 | X12, T10 | p. 12 | HIGH; limited adaptation budget |
| Broader assets show preliminary protection | Ten pages; protected audio/text zero | X8, T7 | pp. 11, 18 | MEDIUM; text aggregates conflict |
| Sampled users perceive little negative impact | Ratings below 1.8; similarity near zero | X14, F8/T13 | pp. 13, 18–19 | MEDIUM; loading inconsistency and denominator limits |
| Deployment costs differ server versus client | 179.7 s generation, 0.052 s restoration | X15, T15 | pp. 13, 19 | HIGH reported means; variability absent |
| Web-agent versus standalone comparison is untested | Agent-as-attacker distinction and page-processing experiments | S2/S3/S5 | pp. 3–4, 7–9 | HIGH scope assessment; relevance is analyst inference |

## 22. Very Simple Explanation — Explain Like I'm 15

Imagine asking an AI to collect all the useful pictures from a website. Some AI tools write a program to do it; others read a simplified page; others control a browser. The researchers found that many such tools work, and using them can save people a lot of coding effort. That is useful for legitimate tasks, but it also makes unauthorized copying easier.

WebCloak changes how a page is represented without intentionally changing what a person sees. One layer replaces familiar image labels and resource clues with changing, unusual ones. A small browser script still displays the pictures for people. Another layer adds hidden text designed to distract or mislead the AI reading the page. The important idea is that the computer's simplified map of the page can differ from the page a human sees.

The defense stopped extraction in many ordinary tests. More informed attackers sometimes recovered a small amount, and the researchers do not claim protection against every expert method. There are also contradictory numbers in the paper, and the tests mostly use saved pages rather than running websites. Preparing a protected page takes about three minutes on average; displaying it adds about 52 milliseconds of restoration work, although some loading measures show larger effects.

For the question about why web agents might be more vulnerable than standalone chat models, this paper suggests an extra source of weakness: an agent must trust enough information from webpage software and content to do its job. That creates opportunities to confuse its parser or influence its model. But this study never directly tests the same model alone against the same model acting as a web agent, so it cannot tell us the size of that difference.

## Completeness Audit

Coverage is assessed against the supplied inventory, not response length. All physical pages have textual coverage, all supplied rendered pages were visually inspected, and all identified figures and tables are represented. 'Compressed' means the core method/results are preserved while repeated language or secondary examples are reduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, abstract | Yes, text/visual | Yes | Fully represented | Identity and central claims |
| S1 Introduction | Yes | Yes | Represented in compressed form | Motivation, three questions, contributions |
| S2.1 threats/paradigms | Yes, text only | Yes | Fully represented | Three types and attributed prior-defense limits |
| S2.2 operation/research focus | Yes, text only | Yes | Represented in compressed form | Preprocessing and benchmark positioning |
| S2.3 victim/attacker distinction | Yes, text only | Yes | Fully represented | Includes p. 4 continuation |
| S3.1 parties/goals | Yes, text only | Yes | Fully represented | Attacker and owner |
| S3.2 capabilities | Yes, text only | Yes | Fully represented | Adaptation and exclusions |
| S3.3 principles/scope | Yes, text only | Yes | Fully represented | Four principles and operator boundary |
| S4 benchmark construction | Yes, text/visual | Yes | Fully represented | Counts, pipeline, rationale |
| S5.1 broad assessment | Yes | Yes | Fully represented | X1/X2, operational failures |
| S5.2 representative assessment | Yes | Yes | Fully represented | X3, T3/T4 |
| S5.3 mechanism | Yes | Yes | Fully represented | LNC/LWA versus L2S distinction |
| S6.1 structural layer | Yes | Yes | Fully represented | Randomization/restoration; missing crypto specifics |
| S6.2 semantic layer | Yes | Yes | Fully represented | ALG1 and three insertion zones |
| S6.3 synergy | Yes | Yes | Fully represented | Preparation order preserved |
| S7.1 setup | Yes | Yes | Fully represented | Metrics, models, dataset, platforms |
| S7.2 effectiveness | Yes | Yes | Fully represented | X5–X8 and condition distinctions |
| S7.3 robustness | Yes | Yes | Fully represented | X9–X13, residuals and conflict |
| S7.4 usability | Yes | Yes | Fully represented | X14, loading/survey/similarity |
| S7.5 overhead | Yes | Yes | Fully represented | X15, dynamic simulation limits |
| S8 discussion/ethics | Yes | Yes | Represented in compressed form | Scope, limitations, local experiments, IRB |
| S9 conclusion | Yes | Yes | Represented in compressed form | Claims qualified by evidence |
| Introductory RQ1/RQ2/RQ3 | Yes | Yes | Fully represented | Mapping preserved |
| Evaluation RQ1–RQ4 | Yes | Yes | Fully represented | Renumbering discrepancy disclosed |
| Formal hypotheses | None identified | Yes, absence noted | Fully represented | None manufactured |
| X1/X2/X3/X4/X5 | Yes | Yes | Fully represented | Feasibility, effort, profiles, mechanism, defense |
| X6/X7/X8/X9/X10 | Yes | Yes | Fully represented | Baselines, tasks, assets, backends, structure |
| X11/X12/X13/X14/X15 | Yes | Yes | Fully represented | Removal, adaptation, environments, users, cost |
| F1/F2/F4/F5 | Yes, visual | Yes | Fully represented | Diagram flows explained |
| F3 | Yes, visual | Yes | Represented in compressed form | Not every dense bar label transcribed |
| F6 | Yes, visual | Yes | Uncertain | Core method readable; extraction artifacts excluded |
| F7/F8/F9 | Yes, visual | Yes | Represented in compressed form | Main axes, labels, trends; no invented bin values |
| T1/T2/T3/T4/T5 | Yes, text/visual | Yes | Fully represented | Main values and footnotes |
| T6/T7/T8/T9/T10 | Yes, text/visual | Yes | Fully represented | Conflicts and N/A retained |
| T11/T12/T13/T14/T15 | Yes, text/visual | Yes | Fully represented | Values, lists, conditions, caveats |
| E1 recall | Yes | Yes | Fully represented | Denominator inconsistency disclosed |
| Precision and optimization notation | Yes | Yes | Fully represented | Definitions and missing settings |
| ALG1 semantic refinement | Yes | Yes | Fully represented | Prose algorithm; no numbered pseudocode |
| Major contributions | Yes | Yes | Fully represented | Claims separated from review concerns |
| Author limitations 1–3 | Yes | Yes | Fully represented | JS, experts, image-centric evidence |
| Rapid-update latency limitation | Yes | Yes | Fully represented | Preliminary simulation not overclaimed |
| A.1/A.2/A.3 | Yes | Yes | Fully represented | Curation, preprocessing, annotation |
| Appendix B | Yes | Yes | Represented in compressed form | Listing cross-reference issue |
| C.1 platforms | Yes | Yes | Fully represented | p. 16 text/visual |
| C.2 task prompts | Yes, p. 17 text only | Yes | Represented in compressed form | Objectives retained; templates not reproduced verbatim |
| C.3 adaptive prompts | Yes, mixed coverage | Yes | Represented in compressed form | Levels and knowledge retained |
| C.4 modality study | Yes | Yes | Fully represented | Ten pages and task/template mismatch |
| C.5 survey | Yes | Yes | Fully represented | All five questions/ratings summarized |
| D.1–D.4 meta-review | Yes | Yes | Represented in compressed form | Acceptance reasons and all three concerns |
| Appendix E response | Yes | Yes | Fully represented | Arguments and mixed-row comparison flagged |
| Corresponding-author/project footnotes | Yes | Yes | Represented in compressed form | Website not visited |
| Artifact badges | Yes, visual | Yes | Fully represented | Displayed status only |
| Acknowledgments/funding | Yes | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | Funding names/award numbers not expanded |
| References [1]–[67] | Yes | Accounted for | Represented in compressed form | Positions used only as author-reported background; no citation validation |
| External supplementary files/artifacts | No | Absence disclosed | Missing from supplied material | Dataset/code/logs not provided |

### Missing or Inaccessible Material

No missing page is apparent within the supplied 1–20 text sequence. Direct visuals for pp. 3, 4, and 17 are absent; their text was assessed. Benchmark files, annotation records, exact implementation, optimization configuration, complete experimental logs, source snapshots/screenshots, cited project/repository material, and any separate supplementary artifact are absent. The supplementary descriptions inside Appendices A–C are present; the underlying smaller dataset is not.

### Uncertain Interpretations

The consistency ledger in Section 14 remains unresolved. Figure 3's tiny segment labels, Figure 6's corrupted extracted notation, unspecified aggregate weighting, zero-output precision conventions, exact survey denominator, and missing statistical variability prevent stronger conclusions. The supplied evidence does not establish a direct agent-versus-standalone security comparison. Confidence in that requested comparative conclusion is UNKNOWN; confidence in the paper's relevance as architectural evidence is MEDIUM.

### Deliberately Compressed Material

Repeated introductory/concluding claims, examples of prior research, the 67-entry bibliography, funding details, repeated prompt formatting requirements, every individual Figure 3 segment, unlabeled Figure 9 bin counts, and duplicate diagram extraction strings are compressed. Their roles and coverage boundaries are explicitly accounted for. Core task conditions, all numbered visuals/tables, all major experiments, limitations, and review concerns are retained.

### Potential Omissions

No known substantive section, numbered figure/table, major method, research question, experiment, or stated limitation from the supplied inventory is wholly unrepresented. That is an inventory-based coverage statement, not a claim of verbatim preservation or independently verified scientific completeness. Unavailable artifacts and unresolved reporting conflicts remain substantive assessment limits.
