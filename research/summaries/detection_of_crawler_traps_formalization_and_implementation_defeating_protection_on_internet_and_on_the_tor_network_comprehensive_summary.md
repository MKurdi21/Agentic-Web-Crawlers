## Stage 0 — Document Accessibility Report

The supplied main document is available as extracted text for all 14 physical PDF pages. Its printed journal pagination is 185–198; physical PDF page 1 corresponds to printed page 185, and physical page 14 corresponds to printed page 198. All locators below use physical PDF page numbers unless explicitly described otherwise. The supplied sequence contains the title, abstract, main sections, conclusion, complete-looking numbered bibliography, and publisher's note. No gap is apparent in this supplied sequence, although the original file and its hash were not independently checked.

Direct visual inspection is possible for physical pages 1, 3, 6, 7, 8, 9, 10, 11, and 12 through the supplied source images. Pages 2, 4, 5, 13, and 14 are assessed from the supplied extracted text only. All five substantive figures are visible: Figure 1 on page 6, Figure 2 on page 7, Figure 3 on page 10, and Figures 4–5 on page 11. Their general structures and plotted trends are readable. Small legends require care, and exact curve values are usually not labeled. Numerical results explicitly stated in prose are therefore distinguished from approximate graphical readings.

No substantive tables, numbered algorithms, appendices, or supplied supplementary files are present. The authors identify a dataset repository on page 7 and cite external trap software and prior work. Those artifacts were not supplied or opened. A repository link and a statement of intended availability do not establish that the dataset or implementation was inspected. The supplied accessibility metadata reports no embedded supplementary files and no detected appendix pages.

Equations on visually supplied pages 8, 9, and 12 can be cross-checked against their rendering. Equations on pages 4–5 are available only through extraction containing mathematical encoding artifacts. Their main structures are recoverable, but unusual notation and missing aggregation operators are preserved as uncertainties rather than silently repaired. The page-4 threshold statement, the Handfish and Dhufish formulas, and the overlap-index normalization require particular caution. No OCR, browsing, code execution, or external research was used. The standalone image-loading error in the input does not prevent inspection of the nine images actually displayed.

Evidence labels throughout are: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No external-information category [E] is used. HIGH confidence indicates a clearly stated or clearly visible source fact; MEDIUM indicates a bounded interpretation or partially specified method; LOW indicates substantial ambiguity; UNKNOWN indicates absent information. Confidence in accurately reporting a claim is separate from confidence that the claim is scientifically established.

## 1. Plain-language orientation

This paper studies how an automated website crawler can recognize that a website has started feeding it trap pages. A crawler is a program that downloads a page, extracts links, follows them, and repeats. A crawler trap exploits that repeated interaction: it supplies endless pages, loops, changing identifiers, or randomly generated text so that the crawler continues collecting useless material. The intended consequences are wasted time, wasted computational resources, and misleading collected information. [A; pp. 1–3]

The authors focus on the difficult case in which pages remain superficially plausible while their text changes randomly. Remembering previously visited addresses is insufficient because each new address or generated page can appear different. Instead, they compare the statistical content of pages. Their central idea is that pages from one genuine website should exhibit a recognizable pattern of change, whereas trap-generated pages should exhibit a different pattern. A useful comparison measure should produce different typical values for different page families and relatively little variation within each family. [A; pp. 3–5]

They construct a dataset containing 13 page families, with 500 pages per family, and evaluate three established information-comparison measures against five proposed measures. Their principal measurements concern overlap between intervals formed from the means and standard deviations of page-comparison values. Lower overlap is treated as indicating clearer separation. The strongest method depends on the evaluation condition: Dottyback performs especially well when regular and trapped families are merged into two groups, while Shark has the lowest explicitly reported overlap impact in the unmerged cross-group analysis. [A; pp. 6–10]

The paper also describes a future-facing or partially specified online detection model using unsupervised clustering and robust statistics. However, page 6 explicitly reserves implementation, classifier selection, and operational tests for future work. Consequently, the most firmly demonstrated contribution is an evaluation of comparison measures and an overlap index, accompanied by a detection-model proposal. It should not be summarized as a fully validated deployed crawler-defense system. [A/D; pp. 6, 10–12]

For the user's research question about web AI agents versus standalone large language models, this paper offers evidence about hazards introduced by repeated interaction with externally controlled web content. That connection is an analyst inference. The paper does not study large language models, prompt injection, or a direct web-agent-versus-standalone-model comparison. [D; pp. 1–3, 6, 10–12]

## 2. Document roadmap

The original title is **Detection of crawler traps: formalization and implementation—defeating protection on internet and on the TOR network**. The authors are Baptiste David, Maxence Delong, and Eric Filiol. The venue is *Journal of Computer Virology and Hacking Techniques*, volume 17, pages 185–198, published in 2021. The supplied first page reports receipt on 7 September 2020, acceptance on 16 March 2021, and online publication on 1 April 2021. The DOI is 10.1007/s11416-021-00380-4. [A; p. 1]

This is a mixed cybersecurity, mathematical-method, and empirical distance-evaluation paper. It is neither a systematic review nor an LLM-security experiment. Its conceptual progression is threat taxonomy → comparison measures → dataset and overlap-based experiments → online clustering proposal → conclusions.

| Inventory ID | Original component | Physical pages | Function |
|---|---|---:|---|
| S0 | Abstract and keywords | 1 | Summarize problem, information-distance approach, and broad claims |
| S1 | §1 Introduction | 1–2 | Explain crawler motivations and anti-bot countermeasures |
| S2 | §2 State of art | 2–3 | Position traps among website protections |
| SS2.1 | Involuntarily crawler traps | 2 | Calendars and parameterized-page loops |
| SS2.2 | Infinite depth or infinite loop | 2 | Deliberately recurring paths/pages |
| SS2.3 | Identifiers | 3 | Changing session identifiers and revisits |
| SS2.4 | Random texts | 3 | Main target: dynamically generated deceptive content |
| S3 | §3 The use of distances | 3–5 | Formalize page families and introduce eight measures |
| SS3.1 | Approach to resolve the problem | 3–4 | Within-family stability and incremental comparison |
| SS3.2 | Distances evaluated, §§3.2.1–3.2.6 | 4–5 | Established and custom formulas |
| S4 | §4 Experiments | 5–10 | Describe evaluation scope and dataset |
| SS4.1 | Experimental dataset | 6–8 | Sources, collection, and page representations |
| SS4.1.1 | Websites | 6–7 | Thirteen families and trap generators |
| SS4.1.2 | Relevant data in a webpage | 7–8 | Four extracted feature representations |
| SS4.2 | Experimental evaluation | 8–9 | Distribution intervals and overlap index |
| SS4.3 | Experimental results | 9–10 | Family, merged-group, and unmerged-group results |
| S5 | §5 Detection model to use | 10–12 | Dynamic clustering, outliers, and trimmed k-means |
| S6 | §6 Conclusion | 12 | Claimed contributions, avoidance, and broader applicability |
| R | References 1–61 and publisher's note | 12–14 | Attribution and bibliographic context |

The keywords are Crawler trap, Information distance, Bots, and TOR network. The five figures are inventoried as F1 pipeline, F2 dataset hierarchy, F3 family overlap, F4 merged-group overlap, and F5 individual-family cross-group overlap. The major mathematical objects are inventoried in Section 13 below. No explicit numbered research questions, formal hypothesis list, theorem/proof sequence, substantive table, or algorithm listing appears.

## 3. Background and context

A **bot**, in this paper, is an automatic program that browses websites. Its purposes may include indexing, archiving, search engine optimization, retrieving content, collecting user information, and gathering intelligence for attacks. The authors describe both legitimate and unwanted uses. Website protection is therefore presented from two opposing operational perspectives: a site owner tries to impede bots, while the authors' crawler tries to detect and bypass the impediment. [A; pp. 1–2]

**Search Engine Optimization (SEO)** is named in the discussion of useful bots. **Internet Protocol (IP) banishment** means denying access based on a client's network address; the authors emphasize possible frustration when legitimate users are blocked. A **captcha**, as described here, is a challenge intended to require a human. Its full acronym expansion is not supplied, so none is introduced as source-derived information. [A; p. 2]

The paper calls the declarative crawler-control file “robot.txt.” This spelling is preserved as the authors' wording; the analysis does not silently correct it using outside knowledge. Their argument is that the file expresses an agreement rather than enforcing access denial and may reveal sensitive locations. [A; p. 2]

A **crawler trap**, also called a **spider trap**, is a region or mechanism that leads automated browsing into endless false or repeated information. Some traps are accidental, such as indefinitely generated calendar pages. Others deliberately generate deep paths, repeatedly changing URL identifiers, or random text. **URL** means Uniform Resource Locator in ordinary technical usage, but the supplied paper does not spell out that expansion; the operational meaning here is simply a page address. **HTML** is the page markup discussed through tags such as `<body>` and `<head>`; **CSS** is named as a page-background setting. Their formal expansions are not needed to reconstruct the reported method. [A; pp. 2–3, 7–8]

The **TOR network** is named as an environment containing notEvil. The paper also uses “Darkweb” when introducing its experiments. No detailed network architecture, anonymity threat model, or TOR-specific protocol analysis is provided. This analysis therefore treats TOR as the authors' stated collection context, not as an independently explained or verified system. [A; pp. 2, 7]

For statistical comparison, a page becomes a distribution of word or word-pair frequencies. A **bigram** is a pair of adjacent words. With overlapping bigrams, the sequence “one two three” yields the pairs “one two” and “two three.” This is an illustration of the described transformation, not a quotation or an experimental example. **Entropy** is the numerical information quantity used in the proposed Shark measure. **Clustering** groups observations by a comparison criterion without requiring the paper's proposed model to begin with a comprehensive labeled training corpus. [A/D; pp. 4–5, 9–12]

## 4. Research problem and gap

**Existing problem.** A crawler can encounter an effectively endless source of fake pages. Each page can contain new text and new links, making continued exploration appear productive even when it is not. The authors emphasize both misleading information and resource waste. [A; pp. 1–3]

**Shortcomings of simpler approaches, according to the authors.** Accidental traps can be handled by recognizing problematic objects. URL-based traps can be addressed through visited-page management and content hashes. Random-text traps cannot be handled in the same way because their pages continue changing. Avoiding detection by the website is also rejected as the principal strategy because slowing or disguising crawling would reduce its operational performance. [A; p. 3]

**Claimed research gap.** Pages 1–2 make strong claims that suitable bots, research, and public operational solutions were unavailable. These are statements about the authors' perceived landscape, not independently verified findings from a systematic search. No database search protocol, inclusion criteria, or quantified literature-screening process is supplied. [A/D; pp. 1–2]

**Methodological gap.** The authors argue that established probability-distribution measures are awkward when the vocabulary is discovered incrementally and the two pages contain different words. They describe removing exclusive words or otherwise altering distributions as losing useful information. Their custom measures are motivated by retaining or exploiting distinctions between page contents. This explanation is reported faithfully, but the paper's general assertions about what established measures mathematically require are not independently established here. [A; pp. 4–5]

**Scope.** The primary target is content-changing crawler traps encountered during page-by-page browsing, using only previously observed pages and newly encountered pages. The empirical scope is the selected 13 families. The broader claims about arbitrary clustering problems and generic avoidance of any trap exceed the directly evaluated scope. [A/D; pp. 3, 6–7, 12]

## 5. Research questions / objectives / hypotheses

The paper does not present a numbered research-question list or a formal hypothesis-testing plan. The following are source-grounded objectives, not invented author research questions:

| ID | Objective or assumption | Status | Source |
|---|---|---|---|
| O1 | Detect when a website begins trapping a crawler and enable avoidance | Explicit objective | 1–3 |
| O2 | Design a page-comparison measure with distinct family means and small within-family variation | Explicit methodological objective | 3–4 |
| O3 | Compare established and proposed measures on regular and trap-generated page families | Explicit evaluation objective | 4–10 |
| O4 | Evaluate interval overlap as the confidence-width multiplier increases | Explicit evaluation objective | 8–10 |
| O5 | Describe a dynamic detector requiring little initial data and robust handling of atypical observations | Explicit model objective | 10–12 |
| H1 | Pages within one family have approximately stable pairwise distances | Author assumption | 3–4 |
| H2 | Typical differences between linked pages from one website should be reasonably stable | Author design hypothesis | 5 |

The user's question—why web AI agents might be more vulnerable than standalone LLMs—is separate from these objectives. The paper supplies neither a standalone LLM condition nor an AI-agent condition. Its relevance is an inferred mechanism: external websites can shape the material and traversal sequence consumed by an automated system. [D; pp. 1–3]

## 6. Assumptions / threat model

The actors are a website capable of serving anti-bot content and a crawler attempting to continue useful collection. From the website's perspective, a trap is protective; from the crawler's perspective, it is an adversarial environment. The paper does not assume that all crawlers are benign or that all site protections are attacks. That role distinction matters when applying the work to security research. [A/D; pp. 1–3]

The website can generate pages dynamically, change page identifiers, create repeated relative-link structures, and choose when to begin returning trap content. The authors suggest triggering factors such as visitation speed, number of visits, and link-following order. They do not implement or evaluate a formal trigger policy in the reported distance experiments. [A; pp. 2–3]

The crawler observes pages sequentially and cannot know the complete vocabulary or complete page population beforehand. It is assumed that pages from one family have sufficiently stable distance behavior for their mean to be useful. A family is a source-specific group; the larger regular-versus-trap grouping combines several such families. [A; pp. 3–4, 6–7]

The proposed detector uses two clusters, k = 2, corresponding to regular and trapped pages. It must operate with limited initial regular-page data and tolerate outliers and changing populations. The authors state that 10 pages are enough in practice for a regular website, but no dedicated learning-curve or repeated cold-start experiment is shown. [A; pp. 10–11]

No formal trusted-component list, credential-access model, tool-permission model, code-execution threat, or LLM instruction hierarchy appears. The paper's malicious or deceptive material is website content and navigation structure, not natural-language instructions aimed at a model. Any analogy to web AI-agent security must preserve that boundary. [D; whole document]

## 7. Methodology

### 7.1 Study design and processing architecture

The empirical study compares eight measures on distributions extracted from collected pages. Figure 1 shows source collections entering feature extraction and preprocessing, then multiple distance branches, then result aggregation, a classifier, classification of new files, and final results. It illustrates an intended full workflow rather than documenting every implemented component. Page 6 explicitly states that classifier choice, implementation, and operational testing are future work. [A/B; pp. 5–6]

The eight named measures are Jensen–Shannon, Hellinger, Bhattacharyya, Shark, Archerfish, Handfish, Dottyback, and Dhufish. The first three are attributed to prior literature. The five fish-named measures are proposed by the authors. Figure legends sometimes display abbreviated or slightly altered names, including “JensenShannon” and “ArcherFish”; these are treated as corresponding to the textual methods. [A/B; pp. 4–5, 10–11]

### 7.2 Dataset and collection

The dataset has 13 families: nine regular families and four trap families, with 500 pages in each. **[C] Analyst-derived:** 13 × 500 = 6,500 total pages; 9 × 500 = 4,500 regular pages; 4 × 500 = 2,000 trap pages. The family counts are therefore unequal across the two broad categories even though each individual family has the same reported size. These derived totals describe the stated corpus, not an independently counted repository. [A/C; pp. 6–7]

| Family | Source | Reported characterization | Pages |
|---|---|---|---:|
| F1 | CPAN | English Perl-library documentation, ranging from prose to code | 500 |
| F2 | Jeuxvideo.com | French gaming news/discussion, including informal forum language | 500 |
| F3 | Stack Exchange | Broad topical questions, described as requiring proper English | 500 |
| F4 | Stack Overflow | Programming content with relatively more source code | 500 |
| F5 | Wikipedia German | Language-specific encyclopedia collection | 500 |
| F6 | Wikipedia English | Language-specific encyclopedia collection | 500 |
| F7 | Wikipedia French | Language-specific encyclopedia collection | 500 |
| F8 | Wikipedia Italian | Language-specific encyclopedia collection | 500 |
| F9 | Wikipedia mixed | Combination of the four preceding languages | 500 |
| F10 | notEvil | Rapid collection within the same minute | 500 |
| F11 | notEvil | Long-duration collection, one page per hour | 500 |
| F12 | Poison | Locally generated random dictionary-based pages | 500 |
| F13 | Tarantula | Locally generated PHP trap pages | 500 |

The authors use a simplified crawler. Wikipedia's random-article control provides varied subjects. They describe pages as consecutive and one click away from the previous and next pages. This should not be expanded into a fully specified traversal algorithm: the paper supplies no exhaustive link-selection policy, crawl date, timeout configuration, or request schedule for all sources. [A; p. 6]

notEvil contains an embedded Zork game with three new-game links. A crawler following them can continue playing indefinitely. A separate “Recent Public Channels” area changes over time. F10 and F11 are intended to capture the possible effect of that temporal difference. The paper does not separately report a timing-condition ablation result for those two families. [A; p. 7]

Poison uses an operating-system dictionary. The authors report settings of 1–10 paragraphs, a binary 0–1 CSS-background option, 25–75 minimum words per paragraph, and 25–100 additional words. They describe uncommon and common dictionary words as equally likely. The exact parameter-sampling procedure and operating-system dictionary version are not supplied. [A; p. 7]

Tarantula generates 1–10 new links and 100–999 words from 1,000 predefined words. Of its 500 pages, 250 are generated from the root address and 250 by following a random link. It is run on a local web server. No server configuration, PHP version, random seed, or precise software revision is reported. [A; p. 7]

The dataset size is reported as 514.3 MiB uncompressed. The stated repository is https://github.com/MaxenceD-ConfData/ForSe-2020. The text says the dataset “will be made available”; availability and contents were not verified. [A; p. 7]

### 7.3 Page representations and preprocessing

Four representations are described: body words; body HTML architecture; head metadata; and body words combined with HTML architecture. Words are normalized to lowercase. Body-architecture processing removes text between tags, comments, and link material identified through `src` and `href`. Head processing removes comments and text between tags. The regex strings in the supplied extraction are imperfectly rendered, so they should not be treated as executable specifications. [A/B; pp. 7–8]

The authors say HTML structure provides efficient discrimination but choose textual content for the reported results to support a more general method. The principal experiments use overlapping word bigrams. Thus, the reported curves concern content distributions, not a demonstrated combined-feature classifier or a measured metadata-only detector. [A; pp. 8–9]

### 7.4 Evaluation procedure and missing configuration

For each family, page-comparison outputs are summarized through a mean μ and standard deviation σ, creating intervals [μ − tσ, μ + tσ]. Increasing t widens those intervals and tests whether separation persists. An overlap index aggregates pairwise interval relationships. The three analyses differ in how families are grouped or merged. [A; pp. 8–10]

The authors prefer this evaluation to repeated cross-validation because their intended population changes as pages arrive. No train/validation/test split, held-out classification table, confusion matrix, accuracy, precision, recall, or area-under-curve result is supplied. No hardware, runtime, memory use, library versions, experiment repetitions, random seeds, or exact pair-sampling counts are reported. These omissions limit reproducibility and the interpretation of operational claims. [A/D; pp. 6–12]

## 8. Experiments / analyses

### X1 — Separation among individual families

Purpose: determine whether measures distinguish source-specific families, regardless of whether they belong to the regular or trap category. Input: the content-based overlapping-bigram representation of the selected families. Variable: interval multiplier t. Outcome: overlap rate among family intervals. Baselines: Jensen–Shannon, Hellinger, and Bhattacharyya. Custom comparisons: all five proposed measures. Figure: F3. [A; pp. 9–10]

At t = 3, the authors report Handfish 19.95%, Dottyback 12.73%, Bhattacharyya 47.61%, Hellinger 48.48%, and Jensen–Shannon 55.11%. Lower is preferable under their criterion. Exact terminal values for Shark, Archerfish, and Dhufish are not given in the prose. The graph supports the general ordering but should not be mined for falsely precise values. The authors interpret reduced overlap as strong discrimination and low false-positive potential; no observed false-positive count is reported. [A/B/D; pp. 9–10]

### X2 — Separation after merging families into two groups

Purpose: examine regular-versus-trapped separation. Setup: families within each category are merged before the same overlap framework is applied. Variable: t. Outcome: overlap between the resulting category interval sets. Figure: F4. [A; p. 10]

Dottyback is reported at 0.57% when t = 3. The authors characterize this as near-perfect detection with only an infinitesimal possible false-negative residue. However, the directly reported measurement is an overlap quantity; the paper supplies no counted false negatives or labeled predictions that would identify it as an empirical false-negative rate. The authors also acknowledge that interval merging can disrupt monotonicity. [A/D; pp. 10–11]

### X3 — Unmerged family impact across categories

Purpose: evaluate how regular-family intervals overlap trap-family intervals without merging them first. Setup: preserve source-specific intervals while comparing the two categories. Outcome: cross-category overlap impact. Figure: F5. [A; p. 10]

Reported values are Shark 3.4%, Dottyback 7.28%, Hellinger 17.31%, Bhattacharyya 20.44%, and Jensen–Shannon 28.08. The final number appears without a percent sign in that sentence but is clearly presented within an overlap-rate comparison. The prose does not repeat t = 3 for this list; associating these values with the terminal plotted condition near t = 3 is supported by the figure and context, but should be labeled as contextual interpretation rather than an independently explicit condition. [A/B/D; pp. 10–11]

The notEvil timing collections, multilingual Wikipedia families, and two Tarantula collection modes contribute dataset diversity. They are not separately demonstrated controlled experiments with their own result tables. The online clustering model in §5 is likewise not accompanied by a separate end-to-end operational evaluation. [D; pp. 6–12]

## 9. Results

The principal finding is that the proposed measures produce less interval overlap than the three established comparisons under the selected dataset and evaluation framework. The broad statement is author-reported; the clearest exact evidence is the five endpoint values for X1, the Dottyback value for X2, and the five impact values for X3. [A; pp. 9–10]

For X1 at t = 3, Dottyback's 12.73% is below Handfish's 19.95% and the three reported baselines. **[C] Analyst-derived:** compared with Jensen–Shannon, the absolute overlap difference is 55.11 − 12.73 = 42.38 percentage points. Compared with Hellinger it is 48.48 − 12.73 = 35.75 percentage points, and compared with Bhattacharyya it is 47.61 − 12.73 = 34.88 percentage points. These are differences in the paper's overlap metric, not improvements in measured classifier accuracy. [A/C; pp. 9–10]

For X2, the 0.57% Dottyback result pertains to merged regular and trap groups. It cannot be substituted for the 12.73% individual-family result because the evaluated objects and aggregation procedure differ. Nor should 100 − 0.57 = 99.43 be reported as validated accuracy: the paper does not establish that conversion through counted predictions. [A/D; p. 10]

For X3, Shark's 3.4% is lower than Dottyback's 7.28%. **[C] Analyst-derived:** the difference is 7.28 − 3.4 = 3.88 percentage points. This condition-dependent reversal matters: the work does not identify one measure as unconditionally best for every task. The abstract's singular “our new distance” compresses a body of work that actually introduces multiple measures with different comparative behavior. [A/C/D; pp. 1, 5, 10]

No exact family means or standard deviations are tabulated. No uncertainty bands around the reported overlap curves, significance tests comparing methods, repeated-run variation, or measured detection latency are provided. Conclusions about deployment, universal applicability, or near-zero error therefore need stronger evidence than the supplied interval-separation analysis alone. [D; pp. 8–12]

## 10. Figure-by-figure interpretation

### Figure 1 — Full process to determine a page family

This grayscale flowchart on page 6 contains sample sources such as CPAN, Stack Overflow, and notEvil, followed by feature extraction and preprocessing. Arrows branch into Jensen–Shannon, Hellinger, a custom-distance block, and additional placeholder branches. The branches converge into aggregation of results, then a classifier, then classification, then results. A “New Files” input enters the classification stage from below. [B]

There are no quantitative axes, units, confidence bars, or measured performance values. The distinction between classifier construction and application to new files is visually explicit. The diagram supports an architecture proposal, not evidence that every stage was implemented or operationally tested. The nearby future-work statement is essential to its interpretation. [A/B; p. 6]

### Figure 2 — Summary of data

This nested-box diagram on page 7 has a top-level grouping labeled “Ethnicity” with two categories. The crawler-trap box contains four 500-sample entries: NotEvil, NotEvil_Fast, Poison, and Tarantula. The regular box contains nine 500-sample entries: CPAN, Exchange, JeuxVideo, StackOverflow, Wikipedia, and four language-labeled Wikipedia entries. The shortened diagram labels should be read alongside the prose, which explicitly specifies four single-language collections and one mixed collection. [A/B]

The figure has no numerical axes or statistical uncertainty. It confirms the family-count structure and per-family sample count. It does not show train/test allocation, labels assigned to individual pages, or collection chronology. The two notEvil entries correspond to different collection rates, not necessarily two independent trap implementations. [A/B/D; pp. 6–7]

### Figure 3 — Overlapping of families

The plot on page 10 is titled “Overlapping of families.” The horizontal axis spans 0 to 3 and is marked with a sigma-related symbol; the caption and text identify the swept quantity as t in [μ ± tσ]. The vertical axis is overlap rate, displayed from approximately 0 to 0.7, although the prose defines the metric's general range as 0 to 1. Both axes are linear. Values such as 0.2 represent 20% overlap. [A/B]

Eight colored curves correspond to the eight measures. The legend uses a magenta/purple encoding for Dhufish, a pale gray/yellow encoding for Bhattacharyya, yellow for Shark, dark green for Handfish, bright green for Dottyback, cyan for Archerfish, blue-violet for Jensen–Shannon, and red for Hellinger. Some pale legend strokes are difficult to distinguish; exact method association should be cross-checked against the textual endpoint results. There are no markers, error bars, or significance annotations. [B]

The curves generally rise as intervals widen. At t near 3, the highest curve is near 0.55 and the lowest near 0.13. These visual estimates agree with the reported Jensen–Shannon 55.11% and Dottyback 12.73% endpoints. Handfish is reported at 19.95%, while Hellinger and Bhattacharyya are near 0.48. The curve mapping must therefore not be inferred from color alone when a small rendered legend is ambiguous. [A/B]

The figure supports lower overlap for custom measures in family separation. It does not directly show a classifier's false-positive or false-negative rates, despite the nearby prose connecting overlap to detection efficiency. [D; pp. 9–10]

### Figure 4 — Overlapping of clusters, merged

The upper plot on page 11 is titled “Overlapping of clusters (merged).” Its x-axis again spans 0–3 for the interval-width multiplier, and its y-axis spans 0–1 in rate units. It uses the same eight-method legend structure as Figure 3. No error bars or prediction counts are shown. [B]

The blue-violet curve rises sharply near t ≈ 1.6 and remains around 0.82–0.84. A magenta curve rises sharply near t ≈ 0.9 and plateaus around 0.65. Several other curves remain below approximately 0.15, with the lowest curve close to zero. These are approximate visual observations; the supplied text gives only Dottyback's exact 0.57% value at t = 3 for this condition. [A/B]

Some curves flatten, dip, or change discontinuously. The authors explain that merging intervals can affect monotonicity. Consequently, the plot should not be interpreted as a smooth ordinary classification-accuracy curve. Its purpose is comparison under merged category intervals. [A/D; p. 10]

### Figure 5 — Overlapping of clusters, individual

The lower plot on page 11 is titled “Overlapping of clusters (individual).” The x-axis spans 0–3 and the y-axis approximately 0–0.4. The methods use the same legend scheme. The eight curves increase and generally flatten toward the right; there are no error bars or statistical markers. [B]

The top curve approaches approximately 0.28, consistent with the prose's Jensen–Shannon 28.08 value. Another baseline is around 0.20, and Hellinger is reported at 17.31%. Dottyback is reported at 7.28% and Shark at 3.4%, with Shark the lowest explicitly reported method in this analysis. The graph is compressed vertically, so prose numbers are preferable to exact visual digit extraction. [A/B; p. 10]

This figure concerns unmerged regular-family impact on trap-family intervals. It is not simply Figure 4 redrawn on a smaller scale. The different aggregation makes the results and rankings substantively different. [A/D]

**Visual cross-validation caution.** Some legend colors are small and pale, and the extracted prose gives baseline rankings that cannot safely be reconstructed solely from a cursory color reading. The exact reported numbers are retained as author statements. Potential curve-to-method ambiguity is disclosed rather than resolved by guessing. All five figures were directly inspected; no figure is represented from caption alone.

## 11. Table-by-table interpretation

No substantive tables appear in the supplied paper. The dataset and result tables in this analysis are analyst-organized representations of prose and figures, not original paper tables. There are therefore no source-table row footnotes, significance stars, missing-value codes, or table-only results to extract. Figure 2 is a dataset hierarchy diagram, not a tabular benchmark. [B/D; pp. 1–14]

## 12. Diagram / architecture interpretation

Figure 1 separates source data, feature construction, distance calculation, aggregation, classifier construction, classification of new inputs, and final outputs. Data flow is left to right. Multiple distance branches imply that the pipeline can compare alternative measures or potentially aggregate their outputs, but the paper does not specify an ensemble formula, learned aggregation weights, or a classifier implementation. Those should not be invented from the arrows. [A/B/D; p. 6]

The “New Files” arrow enters classification rather than the initial source collection. This suggests a distinction between existing material used to construct a model and incoming pages to assign, but the exact online update and feedback path is not drawn. There is no visible feedback arrow from classification to retraining. Section 5 supplies the dynamic-model discussion separately. [B/D; pp. 6, 10–12]

Figure 2 organizes the dataset into two broad categories and 13 families. Its role is to clarify what is grouped in the later experiments. X1 compares individual families; X2 merges within broad categories; X3 preserves individual families while evaluating cross-category impact. This relationship between hierarchy and experiment is necessary to understand why the three overlap results are not interchangeable. [A/B; pp. 7, 9–10]

## 13. Equations and mathematical concepts

The equations are mostly unnumbered. Stable analyst IDs below identify their location and role without implying original equation numbering.

### E1 — Within-family page-distance assumption, pp. 3–4

The authors write X = D(s_i, s_j) for a random page-pair comparison and assume D(s_i, s_j) ≈ D(s_i, s_k) within a family. Here D is a comparison measure, s_i is a page sample, and the family contains n samples. This expresses the desired stability of distances among pages from the same source. They attribute it to transitivity of a distance. **[D] Analyst observation:** the supplied argument does not prove that a generic distance enforces approximately equal pairwise distances. It is a modeling assumption about the selected page families.

The page-4 extraction also contains D(s_i, s_j) ≤ ε with ε ≤ 0, embedded in a discussion of a new sample and family mean. The sign and the connection between mean comparison and page-pair comparison are not confidently resolved from the text-only page. This statement is preserved as uncertain and is not converted into an executable threshold rule.

### E2 — Shannon entropy, p. 4

H(X) = −Σ_{x∈𝒳} p(x) log₂ p(x).

H is the entropy function; p(x) is an occurrence probability for a word or word group; 𝒳 is the possible-value space. The sum combines each probability with its base-2 logarithm and negates the result. It supplies the information quantity used in Jensen–Shannon and Shark. The paper does not specify implementation conventions for zero-probability terms or degenerate zero-entropy pages.

### E3 — Jensen–Shannon divergence and square-root distance, p. 4

JS_π(P,Q) = H(π₁P + π₂Q) − π₁H(P) − π₂H(Q), with π₁, π₂ ≥ 0 and π₁ + π₂ = 1.

D_JSπ(p₁,p₂) = √JS_π(p₁,p₂).

P and Q are distributions for two pages; π₁ and π₂ weight them. The divergence compares the entropy of their mixture with their weighted individual entropies. The authors take a square root to obtain a metric. The actual experimental weights are not reported, and the p₁,p₂ notation in the final expression should not be confused with a single token probability elsewhere.

### E4 — Normalized Hellinger distance, p. 4

D_H(P,Q) = (1/√2) √[Σ_{i=1}^{n}(√p_i − √q_i)²].

p_i and q_i are corresponding probabilities; n is the number of compared categories in this expression. The formula compares square-root probabilities, squares their differences, sums them, and rescales. The authors state that the normalized output lies between 0 and 1. Exact support alignment and vocabulary handling in their implementation remain unspecified.

### E5 — Bhattacharyya coefficient and metric variant, p. 4

cos θ₁ = Σ_{i=1}^{n} √(p_i q_i), followed by D_C(P,Q) = √[1 − ρ(P,Q)].

θ₁ is an angle between probability-derived vectors, and ρ is called the Bhattacharyya or affinity coefficient. The authors discuss a nonmetric Bhattacharyya measure and a metric variant attributed to prior work. The plotted legend says Bhattacharyya, but the supplied account does not unambiguously identify which exact displayed expression produced every baseline result. That is a reproducibility uncertainty, not a reason to silently substitute a conventional alternative formula.

### E6 — Shark, p. 5

D_s(P,Q) = [H(P\Q) + H(Q\P)] / [H(P) + H(Q)].

The backslash denotes exclusive content: words present on one side but absent on the other. The numerator represents information associated with exclusive words; the denominator represents information in both page distributions. The intended output is a comparison emphasizing vocabulary differences that may be lost when supports are restricted. The supplied paper does not fully specify renormalization of restricted distributions, how overlapping bigrams are handled in this restriction, or what happens when the denominator is zero.

### E7 — Arcsine distribution and Archerfish, p. 5

F(x) = (2/π) arcsin(√x), and f(x) = 1/[π√(x(1−x))] for x∈[0,1].

D_a(P,Q) = (4/π²) Σ_{i=1}^{n} arcsin(√p_i) arcsin(√q_i).

F is the reported cumulative distribution function and f its density. The authors use their shape as motivation for Archerfish. The summation pairs transformed probabilities from two pages. The displayed expression is a product-based comparison rather than an explicitly stated difference-from-self construction; the paper does not provide a full metric proof or a detailed explanation of its identity behavior. The density expression is singular at endpoints, and implementation handling is absent.

### E8 — Handfish, p. 5

D_h(P,Q) = (1/π) |1/√[p_i(1−p_i)] − 1/√[q_i(1−q_i)]|.

This is the recoverable extracted form. It compares reciprocal density-related terms. The index i appears, but no sum, average, or other vector-level aggregation operator is visible in the supplied text. It is therefore not possible to reconstruct the full page-distribution computation with HIGH confidence. Endpoint handling at probabilities 0 or 1 is also not specified. The text's stated intention is to use arcsine-density behavior for discriminating page families.

### E9 — Dottyback, p. 5

D_o(P,Q) = Σ_{i=1}^{n} √p_i arctan(√p_i) √q_i arctan(√q_i).

The expression sums products of arctangent-transformed probability terms. It is motivated by the arctangent function rather than by the separately cited arctangent distribution. It produces a scalar comparison for two probability distributions. The paper calls it a distance but supplies no complete proof of metric properties or explicit self-distance analysis. The reported results evaluate its practical interval separation, not a fully established general metric theorem.

### E10 — Dhufish, p. 5

D_u(P,Q) = |1/[1 + p_i(1−p_i)] − 1/[1 + q_i(1−q_i)]|.

The authors connect this measure to the derivative of arctangent. As with Handfish, the recoverable expression is indexed by i without an explicit visible aggregation across tokens. A complete implementation cannot be inferred confidently. No missing sum is inserted in this analysis.

### E11 — Family intervals and distributional approximation, p. 8

I_D0 = [E[D(x,y)] − tσ_D, E[D(x,y)] + tσ_D].

E denotes expectation; σ_D is the standard deviation of comparison values; t is the width multiplier. The authors regard values outside the family's interval as evidence of another family and seek separated means μ₀ and μ₁. They invoke the central limit theorem to motivate approximate normal behavior and report coverage of 68% at one standard deviation, 95% at 1.96 standard deviations, and 99% at three standard deviations.

These percentages are the paper's reported values. **[D] Analyst observation:** the interval uses a standard deviation of distances, while the text also discusses average distances and calls the intervals confidence intervals. The paper does not make the sampling distribution, effective sample size, or distinction between population spread and uncertainty in an estimated mean fully explicit. The reader should not interpret these bands as conventional estimated-mean confidence intervals without additional specification.

### E12 — Similarity properties and widening condition, p. 9

The paper lists boundedness 0≤S(A,B)≤1, symmetry S(A,B)=S(B,A), reflexivity S(A,B)=1 iff A=B, and an inclusion-based property: if A⊆B⊆C, then S(A,B)≥S(A,C). It additionally proposes S(I_i,I_j,t)≤S(I_i,I_j,t′) when t≤t′. These properties articulate desired similarity and nondecreasing overlap under interval widening. No complete proof for every proposed use case is supplied, and the authors explicitly allow merging to disturb monotonicity in X2.

### E13 — Multiple-interval overlap index, p. 9

For intervals I_i=[a_i,b_i], the displayed expression aggregates pairwise intersection-to-union quantities and expands them through medians:

τ = [2/(n(n+1))] Σ_{i=1}^{n} Σ_{j=i+1}^{n} R_ij,

R_ij = [Med(a_i,b_i,b_j) − Med(a_i,b_i,a_j)] / [Max(b_i,b_j) − Min(a_i,a_j)] when the denominator is nonzero; otherwise R_ij = 1.

Med means median, Max maximum, and Min minimum. The numerator computes the shared length through endpoint medians; the denominator measures the enclosing span. The symbol Δ in the earlier expression is used for an interval-size quantity, but its exact formal definition is not supplied. The initial coefficient c_n is replaced by the displayed 2/[n(n+1)] factor without a separate detailed definition.

**[C/D] Analyst-derived consistency check:** the sum has n(n−1)/2 unordered pairs. If all nondegenerate intervals are identical, every R_ij equals 1, so the displayed normalization gives τ = [2/(n(n+1))] × [n(n−1)/2] = (n−1)/(n+1), rather than 1. Thus, the displayed factor does not directly produce reflexivity at the aggregate level under that interpretation. This is an unresolved formula/property mismatch; the analysis does not replace n(n+1) with another denominator or recompute the paper's results. The distinction also cautions against interpreting τ automatically as the literal fraction of all covered space shared by intervals.

### E14 — k-means objective, p. 12

min_{T₁,…,T_k} Σ_{i=1}^{n} inf_{1≤j≤k} ||x_i−T_j||².

x_i is an observation in p-dimensional real space; T_j is a cluster center; k is the number of clusters. For each observation, the inner operation chooses its nearest center. The outer sum adds squared distances, and minimization chooses centers that make that sum small. The proposed application uses k=2. The paper does not fully specify the feature vector connecting its custom distribution comparisons to this Euclidean objective.

### E15 — Trimmed k-means, p. 12

min_{x_{nα}} min_{T₁,…,T_k} Σ_{x_i∈x_{nα}} inf_{1≤j≤k} ||x_i−T_j||²,

where x_{nα} contains n−⌊nα⌋ observations. α controls the fraction removed, and the floor operator selects an integer number to discard. The goal is robustness against atypical observations while selecting centers. No numerical α, online update schedule, convergence rule, or trimming sensitivity result is given. TCLUST is mentioned as another procedure that can produce ellipsoidal clusters, but no full algorithm or experimental comparison is supplied.

## 14. Interpretation and discussion

The results answer O2–O4 most directly: certain proposed comparison functions create less overlap among the selected distributions than the baselines under the authors' interval criterion. O1 and O5 are addressed through motivation and a detector proposal rather than a complete operational test. The distinction between separability and deployed detection is essential. [A/D; pp. 6, 9–12]

The three analyses test different notions of separation. X1 asks whether different source families remain distinct. X2 asks whether their merged regular/trap groupings remain distinct. X3 asks how source-specific intervals interfere across those groupings without merging. Dottyback's particularly low X2 value and Shark's X3 advantage are therefore compatible findings rather than necessarily contradictory rankings. [A/D; pp. 9–11]

The paper's conclusion states broad applicability to other statistical and clustering problems. That is an author extrapolation, not a demonstrated cross-domain benchmark. Likewise, the abstract's claim of escaping any trap is broader than the evaluated random-content and selected-source conditions. [A/D; pp. 1, 12]

Several unresolved points matter: page 6 defers implementation and operational testing while later passages describe a created model; interval overlap is rhetorically translated into detection error without counted predictions; the displayed overlap normalization has an aggregate self-similarity issue; and some custom formulas are incompletely specified for vector aggregation. These do not erase the reported measurements, but they limit the strength and reproducibility of downstream claims. [D; pp. 5–6, 8–12]

For web AI-agent research, the supported connection is that vulnerability can arise from the external browsing process itself: repeated actions and observations can be manipulated by an environment that controls pages and links. Whether that creates greater vulnerability than a standalone LLM, and by how much, remains unanswered here. [D]

## 15. Contributions and novelty

**Conceptual contribution:** a source-family view of crawler-trap detection that focuses on changes in page content rather than only addresses or duplicate pages. The security goal is to recognize deception after site-side countermeasures activate. [A; pp. 2–4]

**Methodological contribution:** an overlap-based framework for comparing distance-output distributions while varying interval width. It separates individual-family, merged-group, and unmerged cross-group analyses. [A; pp. 8–10]

**Comparison-function contribution:** five custom functions—Shark, Archerfish, Handfish, Dottyback, and Dhufish—motivated by exclusive vocabulary, arcsine behavior, and arctangent transformations. Their naming as distances does not by itself establish that every function satisfies metric axioms. [A/D; pp. 4–5]

**Dataset contribution:** 13 families with linguistic, source, timing, and trap-generator variation, each reported to contain 500 pages. Dataset sharing is announced, not independently confirmed. [A; pp. 6–7]

**Empirical contribution:** lower reported overlap values for selected custom measures under the supplied corpus and evaluation conditions. **Model contribution:** a proposed dynamic, robust unsupervised clustering protocol using small initial samples and outlier removal. No formal theorem sequence, complete implementation release, runtime benchmark, or operational detector experiment is established in the supplied material. [A/D; pp. 6, 9–12]

## 16. Limitations

### Authors' stated limitations

The authors explicitly state that only creation of a more discriminating distance is presented at that stage, and that implementation, classifier selection, and operational tests remain future work. They acknowledge few identified content-changing crawler traps, incomplete advance knowledge of pages and vocabulary, difficulty detecting traps from only two consecutive pages, and limited initial regular-page data. They recognize atypical observations as a source of model pollution and interval overlap as a source of possible misdetection. They also state that interval merging can affect monotonicity. [A; pp. 3, 5–8, 10–12]

### Additional evidence-based analyst observations

The corpus has four trap families but only three named trap sources because notEvil contributes two timing variants. Poison and Tarantula are locally generated. Generalization to independently developed, adaptively adversarial, or more diverse real-world traps is therefore not established by the listed families alone. [D; pp. 6–7]

The study does not report prediction-level accuracy or error counts, detector runtime, detection delay, repeated trials, seeds, held-out sources, or a complete implementation specification. Custom-function aggregation, probability-support handling, trimming fraction, and the exact mapping to Euclidean clustering remain insufficiently specified. [D; pp. 4–12]

A legitimate page can be atypical, while a trap can preserve site style; the authors themselves motivate both possibilities. The extent to which text separability remains reliable under those cases is not isolated experimentally. The dataset's linguistic variation helps demonstrate diversity but does not establish that differences are caused specifically by malicious trapping rather than language, source, or generator characteristics. [D; pp. 3, 6–8]

No LLM-specific conclusion is supported. There is no direct evidence about prompt injection, model alignment, instruction following, agent tool misuse, credential compromise, or a standalone-model comparison. [D; whole document]

## 17. Threats to validity

The labels in this section are analyst categories, not headings used by the authors.

**Internal validity:** the supplied work does not fully specify page-pair selection, repetitions, or all preprocessing and comparison-function details. This makes it difficult to attribute each numerical advantage to a particular reproducible implementation choice. [D; pp. 4–10]

**Construct validity:** interval overlap measures distributional interference. It is not automatically a measured classification error rate. The paper's use of “confidence interval,” its normal-approximation argument, and its conversion of low overlap into near-perfect detection require clearer definitions and prediction-level validation. [D; pp. 8–10]

**External validity:** the selected regular sources, multilingual collections, notEvil behavior, and two local generators do not exhaust possible web environments. Broad claims about all traps or all clustering problems are not demonstrated by this dataset. [D; pp. 6–7, 12]

**Statistical conclusion validity:** no uncertainty around overlap estimates, repeated-run distributions, or formal comparative significance analysis is shown. The overlap-index normalization ambiguity further limits interpretation of its absolute scale. [D; pp. 8–11]

**Ecological validity:** two trap datasets are generated locally, and the main evaluation is a corpus-based comparison rather than a running crawler transitioning into a trap under live conditions. Resource savings and escape behavior are proposed outcomes, not measured operational results. [D; pp. 6–7, 12]

**Reproducibility:** a repository address and uncompressed dataset size improve traceability, but no supplied repository snapshot, code revision, environment, seed, or full algorithm configuration allows this analysis to reproduce results. **Research-question validity:** transferring these findings to web AI agents is a mechanism-level analogy, not a measured comparative conclusion. [D]

## 18. Future work and open questions

### A. Explicitly proposed by the authors

Page 6 identifies implementation, choice of a classification algorithm, and operational tests as future work. Section 5 discusses robustness through trimmed k-means and possible TCLUST use. The conclusion proposes avoiding pages too far from a subset of previously visited pages and applying the method beyond webpage classification. These are stated directions or proposed uses, not additional completed experiments. [A; pp. 6, 12]

### B. Additional open questions inferred from the study

How accurately does the full detector classify held-out pages and previously unseen trap sources? How many pages are required before a stable decision, and what happens when the first observed pages are already trap pages? How should the model preserve genuinely unusual pages while removing harmful outliers? Which measure is preferable under different group-aggregation conditions? What computational cost and resource savings occur during live crawling? [D; pp. 6–12]

How are exclusive-token probabilities normalized? How are Handfish and Dhufish aggregated? Which Bhattacharyya variant is actually evaluated? What overlap normalization was used in code? How are the custom comparison values represented for Euclidean trimmed k-means? These questions follow directly from specification gaps. [D; pp. 4–5, 9, 12]

For the user's research question, additional experiments would be needed to determine whether web AI agents inherit this browsing hazard, whether language-model capabilities mitigate or amplify it, and how they compare with standalone LLMs under a matched task. The supplied paper provides no results for those questions. [D]

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning and boundary |
|---|---|
| Bot / crawler | Program that automatically visits pages and follows links |
| Crawler trap / spider trap | Mechanism that induces endless, repeated, or fake browsing |
| Involuntary trap | An accidental navigation structure with effectively unlimited pages |
| Session ID | Identifier associated with a visitor, potentially changed to induce revisits |
| Family F | Pages from one website/source or one defined collection condition |
| Regular/trap group | Larger category combining several families |
| Bigram | Two adjacent words treated as one comparison token |
| Overlapping bigrams | Adjacent pairs sharing one word between consecutive pairs |
| Probability distribution P,Q | Relative occurrence frequencies for page tokens |
| Support / vocabulary | Tokens represented by a distribution; exact handling is incompletely specified |
| Entropy H | Information quantity computed from probabilities and logarithms |
| D | Generic page-comparison function called a distance by the paper |
| μ | Mean comparison value for a population or family |
| σ, σ_D | Standard deviation, describing spread in comparison values |
| t | Multiplier used to widen [μ−tσ, μ+tσ] |
| I_i=[a_i,b_i] | Interval with lower endpoint a_i and upper endpoint b_i |
| τ | Proposed aggregate overlap index |
| Med, Max, Min | Median, maximum, and minimum operations |
| P\Q | Content represented on the P side but absent on the Q side |
| π₁,π₂ | Mixture weights in Jensen–Shannon, summing to one |
| ρ | Bhattacharyya/affinity coefficient |
| k | Number of clusters; the proposed detector uses 2 |
| T_j | Center of cluster j |
| x_i∈R^p | Observation represented by p numerical coordinates |
| ||x_i−T_j||² | Squared Euclidean distance from observation to center |
| α | Fraction used for trimming atypical observations; value not supplied |
| ⌊nα⌋ | Integer number removed under the displayed trimming formula |
| Outlier | Observation atypical enough to disrupt a fitted model |
| Robust statistics | Methods intended to reduce sensitivity to atypical observations |
| Silhouette method | Named clustering method; the paper describes average-distance assignment but gives no full silhouette formula |
| TCLUST | Named robust clustering procedure; acronym expansion and implementation are not supplied |
| MiB | Dataset-size unit reported by the authors; no conversion is performed |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Document length | 14 | physical pages | Supplied text sequence | Visually readable / supplied text | 1–14 |
| Families | 13 | families | Whole dataset | Author-reported | 6 |
| Regular families | 9 | families | Regular category | Author-reported | 6 |
| Trap families | 4 | families | Trap category | Author-reported | 6 |
| Pages per family | 500 | pages | Each source family | Author-reported | 6 |
| Total corpus | 6,500 | pages | 13×500 | Analyst-derived | 6–7 |
| Regular corpus | 4,500 | pages | 9×500 | Analyst-derived | 6–7 |
| Trap corpus | 2,000 | pages | 4×500 | Analyst-derived | 6–7 |
| Dataset size | 514.3 | MiB uncompressed | Announced dataset | Author-reported | 7 |
| Rapid notEvil collection | Same minute | collection interval | F10 | Author-reported | 7 |
| Slow notEvil collection | 1 | page/hour | F11 | Author-reported | 7 |
| Poison paragraphs | 1–10 | paragraphs | Generator setting | Author-reported | 7 |
| Poison minimum words | 25–75 | words/paragraph | Generator setting | Author-reported | 7 |
| Poison added words | 25–100 | words/paragraph | Generator setting | Author-reported | 7 |
| Poison background | 0–1 | binary setting | CSS-background choice | Author-reported | 7 |
| Tarantula links | 1–10 | links/page | Local generator | Author-reported | 7 |
| Tarantula text | 100–999 | words/page | Local generator | Author-reported | 7 |
| Tarantula vocabulary | 1,000 | predefined words | Local generator | Author-reported | 7 |
| Tarantula root/link split | 250 / 250 | pages | Root address / random link | Author-reported | 7 |
| Distribution-band coverage | 68 / 95 / 99 | percent | t=1 / 1.96 / 3, as stated | Author-reported | 8 |
| X1 Handfish overlap | 19.95 | percent | Individual families, t=3 | Author-reported | 9 |
| X1 Dottyback overlap | 12.73 | percent | Individual families, t=3 | Author-reported | 9 |
| X1 Bhattacharyya overlap | 47.61 | percent | Individual families, t=3 | Author-reported | 9–10 |
| X1 Hellinger overlap | 48.48 | percent | Individual families, t=3 | Author-reported | 9–10 |
| X1 Jensen–Shannon overlap | 55.11 | percent | Individual families, t=3 | Author-reported | 10 |
| X2 Dottyback overlap | 0.57 | percent | Merged groups, t=3 | Author-reported | 10 |
| X3 Shark impact | 3.4 | percent | Unmerged regular-to-trap impact; terminal t condition inferred from context | Author-reported | 10 |
| X3 Dottyback impact | 7.28 | percent | Same X3 condition | Author-reported | 10 |
| X3 Hellinger impact | 17.31 | percent | Same X3 condition | Author-reported | 10 |
| X3 Bhattacharyya impact | 20.44 | percent | Same X3 condition | Author-reported | 10 |
| X3 Jensen–Shannon impact | 28.08 | rate expressed as percent in context | Sentence omits percent sign for this entry | Author-reported | 10 |
| Proposed clusters | 2 | clusters | Regular versus trapped | Author-reported | 10–12 |
| Initial regular-page sufficiency | 10 | pages | Practical assertion, no dedicated curve | Author-reported | 11 |
| X1 JS–Dottyback difference | 42.38 | percentage points | 55.11−12.73 | Analyst-derived | 9–10 |
| X3 Dottyback–Shark difference | 3.88 | percentage points | 7.28−3.4 | Analyst-derived | 10 |

Other plotted method values are deliberately not converted into exact numbers. Approximate visual observations are included only where useful in Section 10, with their approximate status stated.

## 21. Claim–evidence map

| Claim | Evidence | Figure / Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Traps can waste crawler resources through fake or repeated material | Abstract and taxonomy | Framing | 1–3 | Explicit author description; no resource-cost measurement |
| Random-content traps require more than simple visited-address management | Discussion of changing text and links | O1 | 3 | Author operational argument |
| The study evaluates page-content comparisons on 13 families | Dataset description and hierarchy | F2 | 6–7 | Clearly reported design; repository not inspected |
| Reported results use overlapping word bigrams | Experimental-results preprocessing description | X1–X3 | 9 | Explicit; complete tokenizer details absent |
| Dottyback improves individual-family overlap relative to reported baselines | 12.73% versus 47.61%, 48.48%, 55.11% at t=3 | F3 / X1 | 9–10 | Exact reported overlap values; not accuracy |
| Dottyback has very low merged-group overlap | 0.57% at t=3 | F4 / X2 | 10 | Explicit number; error-rate interpretation is stronger than direct measurement |
| Shark is best among explicitly reported X3 values | 3.4% versus Dottyback 7.28% and larger baseline values | F5 / X3 | 10 | Aggregation differs from X1/X2; endpoint condition contextual |
| Dynamic robust clustering is proposed | k=2, small initial set, outlier removal, trimmed objective | S5 | 10–12 | Model description without separate operational results |
| Implementation and operational testing are not established by the main experiments | Explicit future-work statement | F1 context | 6 | Strong source basis; later created-model wording remains unresolved |
| Absolute overlap-index interpretation is uncertain | Displayed coefficient versus number of unordered pairs | E13 | 9 | Analyst-derived mathematical consistency check |
| Web interaction can expose automated systems to environment-controlled deception | Dynamic pages and repeated navigation | Framing / relevance | 1–3 | Analyst inference for web AI agents; no LLM comparison |
| Universal clustering applicability is not demonstrated | Broad conclusion versus one page corpus | S6 | 12 | Analyst qualification of an author extrapolation |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a program that explores a website by opening a page, following its links, and doing the same thing again. A website can trick that program by continually creating new-looking pages that contain random or useless material. The program keeps working, but it is no longer getting useful information.

The researchers try to notice this by comparing the words in pages. Real pages from one site may change in a recognizable way. Trap pages may be strangely similar, strangely different, or follow a different statistical pattern. The researchers test several ways of measuring these differences on a collection of regular pages and trap pages.

Some of their new measurements separate the collected groups better than the older measurements under their chosen test. But their main numbers describe how much statistical ranges overlap. They are not the same thing as counting how often a complete live detector makes the right decision. The paper also describes how a detector might learn while browsing and avoid being confused by unusual pages, but the complete operational system still needs stronger testing.

For web AI agents, the useful lesson is that trouble can come from the websites an automated system interacts with, even without a direct attack on its language model. A website can control the pages and links the system encounters. This paper does not show that web AI agents are more vulnerable than standalone LLMs; it gives one reason why adding web interaction creates security questions that a standalone model comparison would need to examine.

## Completeness Audit

The denominator is the inventory of the supplied 14-page paper: abstract, six major sections, all visible substantive subsections, eight named comparison measures, five figures, three overlap analyses, major mathematical objects, model proposal, author limitations, and bibliography. Coverage below distinguishes representation from validation. “Fully represented” means the available substantive content is explained; it does not mean the scientific claim has been proven.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, dates, keywords | Yes | Yes | Fully represented | Page 1 visually and textually inspected |
| Abstract | Yes | Yes | Fully represented | Broad claims qualified against body evidence |
| §1 Introduction | Yes | Yes | Represented in compressed form | Bot-use examples grouped |
| §2 State of art | Yes | Yes | Represented in compressed form | Protection mechanisms and author positioning retained |
| §2.1 Involuntary traps | Yes, text | Yes | Fully represented | Calendar and parameter-loop examples retained |
| §2.2 Infinite depth/loop | Yes, text | Yes | Represented in compressed form | Exact illustrative URL omitted as secondary |
| §2.3 Identifiers | Yes | Yes | Fully represented | Changing session ID and countermeasures retained |
| §2.4 Random texts | Yes | Yes | Fully represented | Main threat and sequential setting retained |
| §3 opening and §3.1 | Yes | Yes | Fully represented with uncertainty | Stable-distance assumption and threshold ambiguity disclosed |
| §3.2.1 Jensen–Shannon | Yes, text only | Yes | Fully represented with configuration gaps | Weights not supplied |
| §3.2.2 Hellinger | Yes, text only | Yes | Fully represented | Formula and normalization explained |
| §3.2.3 Bhattacharyya | Yes, text only | Yes | Fully represented with uncertainty | Baseline variant not fully identified |
| §3.2.4 Shark | Yes, text only | Yes | Fully represented with uncertainty | Restricted-distribution normalization unspecified |
| §3.2.5 Archerfish and Handfish | Yes, text only | Yes | Fully represented with uncertainty | Handfish aggregation and endpoints unresolved |
| §3.2.6 Dottyback and Dhufish | Yes, text only | Yes | Fully represented with uncertainty | Dhufish aggregation unresolved |
| §4 experiment framing | Yes | Yes | Fully represented | Future-work boundary explicitly retained |
| §4.1 dataset | Yes | Yes | Fully represented | Family counts, size, and collection distinctions retained |
| §4.1.1 all regular sources | Yes | Yes | Fully represented | Language/style details compressed into dataset table |
| §4.1.1 notEvil | Yes | Yes | Fully represented | Game and timing variants retained |
| §4.1.1 Poison | Yes | Yes | Fully represented | Generator settings retained |
| §4.1.1 Tarantula | Yes | Yes | Fully represented | Vocabulary, links, word counts, and 250/250 split retained |
| §4.1.2 page features | Yes | Yes | Fully represented with uncertainty | Regex extraction not treated as executable code |
| §4.2 evaluation | Yes | Yes | Fully represented | Interval construction, normal argument, and overlap index retained |
| §4.3 results | Yes | Yes | Fully represented | Distinct conditions and exact prose numbers retained |
| §5 detection model | Yes | Yes | Fully represented with gaps | k=2, 10-page assertion, trimming, and TCLUST retained |
| §6 conclusion | Yes | Yes | Fully represented | Generic-use claims identified as extrapolation |
| Explicit research questions | Entire document checked | Yes | Not present as formal list | Objectives represented without invented author questions |
| Explicit formal hypotheses | Entire document checked | Yes | Not present as formal list | Design assumptions H1/H2 identified separately |
| X1 family analysis | Yes | Yes | Fully represented | Figure 3 and endpoint comparisons |
| X2 merged-group analysis | Yes | Yes | Fully represented | Figure 4, 0.57%, and merging caveat |
| X3 unmerged impact analysis | Yes | Yes | Fully represented | Figure 5 and contextual t qualification |
| F1 pipeline | Yes, visually | Yes | Fully represented | Inputs, branches, aggregation, new-file input |
| F2 hierarchy | Yes, visually | Yes | Fully represented | Two groups and 13 families |
| F3 family plot | Yes, visually | Yes | Fully represented with legend caution | Exact prose and approximate visual evidence separated |
| F4 merged plot | Yes, visually | Yes | Fully represented | Jumps and nonmonotonicity accounted for |
| F5 individual plot | Yes, visually | Yes | Fully represented | Separate grouping condition retained |
| Substantive tables | Entire document checked | Yes | None present | Analyst tables are not source tables |
| E1 family/threshold assumptions | Yes | Yes | Uncertain in part | Page-4 threshold sign not confidently resolved |
| E2 entropy | Yes, text | Yes | Fully represented | Zero-term conventions absent |
| E3 Jensen–Shannon | Yes, text | Yes | Fully represented | Experimental weights absent |
| E4 Hellinger | Yes, text | Yes | Fully represented | Support handling absent |
| E5 Bhattacharyya forms | Yes, text | Yes | Fully represented with uncertainty | Evaluated variant unclear |
| E6 Shark | Yes, text | Yes | Fully represented with uncertainty | Renormalization and zero denominator absent |
| E7 arcsine/Archerfish | Yes, text | Yes | Fully represented | No full metric proof supplied |
| E8 Handfish | Yes, text | Yes | Uncertain | Vector aggregation not visible |
| E9 Dottyback | Yes, text | Yes | Fully represented | Metric properties not fully established |
| E10 Dhufish | Yes, text | Yes | Uncertain | Vector aggregation not visible |
| E11 intervals/normal approximation | Yes, visually and textually | Yes | Fully represented with qualification | Population spread versus mean uncertainty distinguished |
| E12 similarity properties | Yes | Yes | Fully represented | Monotonicity and merging caveat retained |
| E13 overlap index | Yes, visually | Yes | Fully represented with consistency concern | Displayed normalization preserved |
| E14 k-means | Yes, visually | Yes | Fully represented | Feature mapping unspecified |
| E15 trimmed k-means | Yes, visually | Yes | Fully represented | α and update procedure absent |
| Named TCLUST procedure | Yes | Yes | Represented in compressed form | Mention only; no supplied detailed algorithm |
| Numbered algorithms/pseudocode | Entire document checked | Yes | None present | No implementation inferred |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, dataset, empirical, model |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst concerns |
| Appendices | Entire supplied sequence checked | Yes | None present | No detected appendix content |
| Supplied supplements | Input checked | Yes | None supplied | No external artifact reviewed |
| Dataset repository and trap software | References inspected only | Yes, as absent artifacts | Missing from supplied material | Links not accessed |
| References 1–61 | Yes, extracted text | Yes | Represented in compressed form | Categories and relevant method attributions retained; bibliography not reproduced |
| Author contact/affiliation footnotes | Yes | Partly | Inspected but deliberately compressed | Authors identified; contact addresses and full affiliations secondary |
| Logos, running headers, page footers, publisher note | Yes where supplied | Accounted for | Inspected but deliberately omitted as non-substantive | Not scientific findings |

### Missing or inaccessible material

No main-text page is apparently missing from the supplied 1–14 sequence. Direct visual renderings are absent for pages 2, 4, 5, 13, and 14; those pages were assessed through extracted text only. The dataset repository, trap-program source files, any experiment code, and the cited ForSE 2020 version were not supplied for inspection. No appendix or separate supplementary artifact was supplied. The source hash is user-provided metadata and was not independently verified.

### Uncertain interpretations

The page-4 ε threshold sign and wording are uncertain. Handfish and Dhufish do not visibly specify distribution-level aggregation in the extracted formulas. Exact probability normalization, exclusive-token handling, and zero/one endpoint handling are unspecified. The exact Bhattacharyya baseline variant is not fully resolved. The overlap formula's 2/[n(n+1)] normalization creates a mismatch with an aggregate reflexivity interpretation. The authors' intervals mix language about spread and mean estimation. The X3 prose does not explicitly repeat the terminal t condition. Small legend colors should not override exact textual values. Later created-model wording does not resolve page 6's future-work boundary.

### Deliberately compressed material

Repeated motivation about bots and website protections, long illustrative addresses, dictionary-word examples, routine bibliographic details, author contact information, publisher branding, and the analogy about measuring people's changing heights are compressed. Their substantive roles—navigation loops, vocabulary diversity, provenance, and changing populations—are retained. No exact numerical result from the principal reported overlap comparisons was deliberately omitted.

### Potential omissions

Every substantive section, subsection, figure, named comparison measure, major mathematical object, distinct reported overlap analysis, contribution category, and identified author limitation in the inventory is represented. Important uncertainty remains in the supplied mathematical specifications and absent operational artifacts. This is an inventory-based account of the available paper, not a claim of independently reproduced results or complete understanding of an unavailable implementation.
