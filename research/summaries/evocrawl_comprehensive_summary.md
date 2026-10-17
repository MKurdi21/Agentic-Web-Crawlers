## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–17. Images were supplied for pages 1–11, 14, and 16, and these pages were inspected visually as well as textually. Pages 12, 13, 15, and 17 were inspected through their supplied text only. The sequence of extracted pages appears continuous; this establishes coverage of the supplied 17-page document, not independent verification against a publisher copy. No browsing, file access, OCR tool, code execution, repository inspection, or supplementary-artifact execution was performed.

The main text, references, general appendix, and Artifact Appendix A are present. Figures 1–6 and Tables I–V, VII, and VIII are visually available. Table VI is available through extracted text on p. 13, without a supplied page image. Equation (1) is visually readable on p. 6. The search-space expression on p. 2 has a potentially problematic exponent; the image and supplied extraction show n^11, and it is retained as an author expression rather than silently corrected. Some configuration lists on pp. 15–16 have extraction-induced spacing, so their purpose and representative entries are reported rather than presenting the extracted strings as verified executable configuration.

The paper references a GitHub repository, a Zenodo artifact, README files, Dockerfiles, configuration files, and output files. These external artifacts were not supplied or inspected. The artifact badge on p. 1 is visible but does not establish that this analysis reproduced or independently validated the software. No embedded supplementary files are reported in the supplied accessibility metadata. The metadata's appendix-page detection is incomplete as an inventory: the text clearly includes artifact evaluation instructions on p. 17 as well.

Evidence labels used below: [A] author-reported; [B] directly observable in a supplied visual; [C] analyst-derived from supplied numbers; [D] analyst interpretation. No [E] external information is introduced. Confidence concerns fidelity to the supplied evidence, not independent confirmation that the research claims are true. Locators use physical PDF page numbers, which match the displayed page numbers where present.

## 1. Plain-Language Orientation

EvoCrawl studies how to explore a web application thoroughly enough to discover security problems. A web application is more than a collection of addresses. Its available actions change as users create objects, fill forms, click controls, and trigger JavaScript. For example, repository-management code may remain unreachable until someone creates a repository. Merely visiting many pages therefore does not guarantee that a scanner reaches the code or application conditions needed to expose a vulnerability. [A, pp. 1–2]

The researchers build an automated crawler that searches for useful sequences of browser interactions. It learns which actions reveal other controls and uses an evolutionary algorithm to favor sequences that submit forms, fill inputs, upload files, or trigger JavaScript events. A second, simpler crawler rapidly discovers pages. The two components exchange discoveries. Separate detectors look for cross-site scripting, abbreviated XSS, and insecure direct object references, abbreviated IDOR. [A, pp. 3–7]

The headline results are an author-reported average 59% increase in code coverage and fivefold more frequent successful HTML form submission than BlackWidow, the strongest comparison crawler in their evaluation. The evaluation uses ten applications and 24-hour runs. The authors also report eight newly discovered findings: five XSS findings and three implementation-related IDOR findings. These findings have different developer responses and exploitation conditions; they should not be treated as eight equally severe or universally accepted vulnerabilities. [A, pp. 1–2, 9–13]

For the user's research question, this is supporting evidence about the complexity of the web environment, not a direct study of why web AI agents are more vulnerable than standalone large language models. EvoCrawl is an evolutionary crawler, not an LLM agent. The paper does not compare standalone LLMs with browser agents, test prompt injection, or measure model compromise. Its relevant contribution is showing how browser actions, persistent application state, executable input, and access-control boundaries create security-sensitive interaction paths. Connecting these observations to AI agents is explicitly analyst inference. [D]

## 2. Document Roadmap

The inventory is organized around the original numbering. S1, Introduction, pp. 1–2, motivates state-aware exploration and lists three contributions. S2, Motivation, pp. 2–3, explains interaction dependencies and the large sequence-search space. S3, Design, pp. 3–7, contains SS3A Page Collection; SS3B Evolutionary Search, including sequence generation/evaluation, dependency tracking/enforcement, gene elimination, and fitness; and SS3C Vulnerability Detectors, covering XSS and IDOR. S4, Implementation, pp. 7–8, describes TestCafe, rrweb, Kafka, token handling, rrweb replay, and initial setup.

S5, Evaluation, pp. 8–11, contains SS5A Experiment Setup, SS5B Code Coverage and application case studies, SS5C HTML form submissions, and SS5D Benefits of Dependency Tracking. S6, Vulnerabilities, pp. 11–13, contains SS6A known XSS experiments, SS6B zero-day XSS, SS6C IDOR, and SS6D a summary of new findings. S7, Limitations, p. 13, discusses parameter tuning and seed selection. S8, Related Work, pp. 13–14, covers access-control scanners, web crawlers, evolutionary search, and machine learning. S9, Conclusion, p. 14, restates the method's benefits. Acknowledgments and references occupy pp. 14–15.

The general appendix, pp. 15–16, supplies absolute coverage tables, blocked-page keywords, and access-denied phrases. Artifact Appendix A, pp. 16–17, describes access, requirements, benchmarks, installation, workflow, major claims, and three evaluation procedures.

The substantive visual inventory is F1–F6: WordPress interface example, system architecture, mutation example, sitemap, baseline-coverage plot, and dependency-ablation plot. The table inventory is T1–T8, corresponding to Tables I–VIII: fitness weights, applications, p-values, submitted forms, known XSS results, IDOR results, baseline coverage counts, and ablation coverage counts. E1 is Equation (1). No numbered pseudocode algorithm, theorem, lemma, formal hypothesis, or explicit numbered research question is present. The experimental register X1–X6 below separates coverage, forms, ablation, known XSS, new XSS, and IDOR evaluation.

## 3. Background and Context

A crawler automatically navigates and interacts with an application. Code coverage measures which program lines execute during testing. A server-side state is the application's stored condition, such as whether a paper, task, post, or repository exists. A client-side state is the browser interface's current condition, including which controls are visible after JavaScript executes. These distinctions explain why an application may expose different behavior at the same URL. [A, pp. 1–5]

HyperText Markup Language, HTML, supplies forms and elements. JavaScript changes browser behavior and can reveal controls without a page reload. The Document Object Model, DOM, is the page structure that EvoCrawl observes for changes. Asynchronous JavaScript and XML, AJAX, appears in the paper as a mechanism for dynamic requests and interface updates. A Cascading Style Sheets, CSS, selector identifies an element for interaction or replay. A Uniform Resource Locator, URL, identifies a page or request target. [A, pp. 3–8, 14]

XSS occurs in this work when injected script executes in the browser. The detector links an input location, or source, to an execution location, or sink. Stored and reflected XSS are distinguished in the reported findings. IDOR concerns unauthorized access to resources identified through requests, including parameterized endpoints. EvoCrawl's IDOR detector estimates intended accessibility from differences between privileged and less-privileged users' interfaces, then tests direct requests. That estimate is imperfect: missing interface navigation does not prove a resource is intended to be private. [A, pp. 6–7, 12–13]

An evolutionary algorithm generates candidate solutions, scores them, and recombines promising candidates. EvoCrawl's candidates are ordered browser-action sequences, not language-model outputs. A gene is an element–interaction pair, such as a particular input combined with typing text. Crossover combines parts of prior sequences; mutation inserts actions constrained by observed dependencies. [A, pp. 3–5]

## 4. Research Problem and Gap

The existing problem is incomplete dynamic exploration. A vulnerability can remain undiscovered when its code is never reached or when the application is not in the required state. The authors emphasize that these requirements can coexist: executing relevant code alone may still be insufficient. [A, p. 1]

According to the authors, prior systems often treat entire forms as units, fill every field, and enumerate sequences of JavaScript events and forms. This can fail in two ways. First, interactions can occur in the wrong order: cancel may precede save, or a hidden control may be targeted before its prerequisite. Second, a difficult optional field can receive invalid input and prevent the whole form from being accepted. Enumerating combinations also consumes time exploring unrelated actions. [A, pp. 1–3, 10]

The gap is efficient fine-grained search over individual fields and events, coupled to state-changing success rather than page visitation alone. EvoCrawl addresses it with evolutionary search and dependency enforcement while retaining a fast page-collection component. The scope is automated exploration and modular detection of XSS and IDOR in configured applications. The method does not aim to invent sophisticated sanitizer-bypassing XSS payloads or solve arbitrary required-field formats. [A, pp. 2–6, 11, 14]

## 5. Research Questions

The paper gives informal objectives rather than formal research questions. O1 is to reveal unseen links and explore server-side states through useful browser-action sequences. O2 is to reduce wasted sequence search by learning dependencies. O3 is to improve executed-line coverage and successful HTML form submission relative to existing crawlers. O4 is to demonstrate the resulting security-testing value through known and newly discovered XSS and IDOR findings. [A, pp. 2–4, 8–13]

No explicit statistical hypotheses, preregistered questions, or null-hypothesis definitions are supplied. The p-values in Table III therefore should not be retroactively described as tests of a formally stated paper hypothesis.

The user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' is an external organizing question supplied for this reading. The paper does not itself establish the comparative premise. Its evidence can inform a mechanism-level argument about web interaction and authority, with confidence MEDIUM as an indirect conceptual connection and UNKNOWN for any comparative AI vulnerability rate. [D]

## 6. Assumptions / Threat Model

The crawler is configured with login credentials and application users. The IDOR design starts with a privileged crawler and a lower-privileged replay user; its triad response test additionally needs another user at the replay user's privilege level. The evaluation sets the crawler to the highest privilege and the attacker to the second highest. Three users are thus needed for the complete IDOR workflow, even though the initial resource-classification description speaks of two access levels. [A, pp. 6–9]

The key policy assumption is that a resource reachable through a user's interface should be accessible to that user. Resources with no discovered lower-privilege interface path are provisionally private. This is an inferred policy boundary, not a supplied authoritative access-control specification. A direct request by the lower-privileged user then probes whether the server actually protects it. [A, pp. 6–7]

Crawler and replayer must operate on the same application instance in lockstep. Otherwise, object creation/deletion can produce different states and mistaken privacy classification. Response comparison assumes the two lower-privileged users should receive similarly protected content, with differences representing user-specific data. Access-denied phrases are manually collected. [A, p. 7]

The XSS detector assumes its fixed-style injected payload can execute where a suitable injection point is reached. Known-vulnerability selection expressly excludes cases requiring crafted sanitizer bypasses. The tools do not complete some cross-user re-login workflows, producing demonstrated false negatives. [A, pp. 11–12]

The study is a configured testing environment with access to coverage instrumentation and database observations. Browser exploration may be described as black-box relative to source analysis, but the evaluated fitness and success instrumentation use server-side database feedback. Analyst interpretation: deployment conditions requiring such access differ from unrestricted external-only scanning. [D, based on pp. 5, 9, 16–17]

No threat model for malicious web content attacking an LLM, agent tool misuse, instruction hierarchy, or prompt injection is supplied. The paper's XSS and IDOR adversaries should not be relabeled as prompt-injection attackers.

## 7. Methodology

The study is a computer-systems and cybersecurity algorithm paper with empirical evaluation. Its main architecture has a Page Collection Module, PM, an Evolutionary Search Module, ESM, an XSS Vulnerability Detector, XVD, and an IDOR Vulnerability Detector, IVD. PM and ESM exchange discovered URLs; both support detector integration. [A/B, pp. 3–4, Fig. 2]

PM seeks breadth quickly. A seed is a tuple consisting of a URL and an EVENT, where the latter identifies an interaction causing DOM change. Its queue drives three stages. Link crawling opens the seed, performs its event if present, extracts anchor href values, and queues new targets. Event crawling tries interactable elements and records controls whose interactions change the DOM without navigation. Form crawling identifies form tags and sequentially interacts with their elements, dynamically including newly appearing controls such as confirmation dialogs. PM does not construct multi-event seeds; combinations are delegated to ESM. [A, pp. 3–4]

ESM searches more deeply within each page. It extracts interactable elements and constructs element–interaction genes. Candidate sequences come from random combinations and crossover of highly scored prior sequences. The described crossover joins the first half of one selected sequence to the last half of another. Submit buttons are placed at sequence ends to improve submission chances. Candidates execute in the browser and receive feedback from browser behavior and database observations. The intended output is many useful interaction sequences, rather than one globally optimal sequence. [A, pp. 3–5]

Input generation first checks value and placeholder attributes. Otherwise, it searches attributes for URL or email hints and generates a matching-format value. The URL example is www.esm{i}.com; the default experimental text is esm{i}, with i identifying an input. This is heuristic formatting, not semantic understanding of arbitrary input requirements. [A, p. 5]

Dependency tracking observes newly revealed elements after an action and associates them with that triggering gene. Mutation can then insert a newly available action after its prerequisite. If several controls appear, a random subset may be inserted. The authors acknowledge nondeterminism can create false dependencies, described as rare in practice without a supplied quantified rate. [A, p. 5]

ESM initially records a navigation destination, passes it to PM, returns to the prior URL, and continues. Because navigation can reset accumulated JavaScript state, gene elimination removes navigation-causing genes and sequences containing them from subsequent search. This is a locality-preserving heuristic, not full exploration of arbitrary multi-page action histories. [A, p. 5; D for the final characterization]

Fitness is a weighted count of form submissions, filled inputs, uploads, triggered JavaScript events, and invisible-element attempts. Successful submission is detected using uniquely marked input in server-side storage. Inputs and events receive positive scores; attempts to interact with invisible elements receive a penalty. The rationale is to preserve sequences likely to produce useful descendants and to favor accepted forms over filling difficult fields that invalidate submission. [A, pp. 5–6]

XVD replaces PM form inputs and ESM-generated text with payloads. On execution, each payload adds a unique integer to a global browser list inserted in the HTML header. UNIX timestamps generate identifiers. Inspecting the list traces execution back to the source field. The supplied material describes the mechanism but does not reproduce a complete literal payload string or prove identifier collision behavior. [A, p. 6]

IVD records requests and builds a sitemap whose URL nodes are connected by interface actions. It replays actions as a less-privileged user using CSS selectors. If any discovered route is accessible, the destination is public. Remaining URLs are probed directly. The triad test sends requests as userA, the crawler; userB, the replay user; and userC, a user at B's privilege level. First, access-denied phrases identify protected responses. Second, B–C differences identify user-specific content to ignore when comparing B with A. The exact response-normalization algorithm, thresholds, and parser implementation are not specified in the paper text. [A, pp. 6–7]

Implementation uses customized TestCafe browser automation, rrweb recording with MutationObserver for DOM changes, and Kafka as a durable seed queue. PM and ESM run as separate processes with separate cookie sessions and separate consumer groups. Built-in rrweb replay is not used because recorded IDs may identify incorrect elements under another user's dynamic DOM; the authors implement replay themselves. [A, pp. 7–8]

For URL tokens, the modules compare post-login redirect query strings, infer differing parameters to be tokens, and replace values when exchanging seeds. This works only for persistent tokens appearing throughout page URLs; intermittent tokens can produce invalid seeds and slow crawling. Initial setup requires manual user creation and automatic-login configuration. [A, p. 8]

The evaluated environment is a four-CPU virtual machine with 6 GB memory and Intel Xeon Gold 6336Y processors. Applications are reset before sessions. Comparison crawlers receive two parallel processes to match EvoCrawl's two interacting processes. Coverage uses Xdebug and php-code-coverage for PHP and Coverband for Rails production. Detectors are disabled in coverage experiments. Runs last 24 hours; EvoCrawl is repeated five times, and Table III specifies five runs each for EvoCrawl and BlackWidow. Random seeds, actual sequence length, generation count, population size, and statistical-test identity are not reported in the supplied prose. [A, pp. 9–10]

The ten application targets and primary-table versions are given in Table II below. There is no machine-learning training dataset or train/validation/test split. Selection emphasizes functional diversity, active use/maintenance, GitHub stars as a user-base proxy, and prior academic usage. These are author selection criteria, not proof of population representativeness. [A/D, p. 9]

## 8. Experiments / Analyses

X1 — Baseline code coverage. Purpose: test O3's executed-line coverage objective. Conditions: EvoCrawl, BlackWidow, JAK, and CrawlJAX, ten applications, reset initial states, matched process resources, detectors disabled, 24-hour budgets. Metrics: executed lines and pairwise unique/common line sets. Fig. 5 and Table VII report comparisons; Table III supplies EvoCrawl–BlackWidow p-values. JAK and CrawlJAX have no Opencart/phpBB results because their token handling fails. Authors report a 59% average improvement and a 6%–192% application-level range versus BlackWidow. The average's aggregation procedure and the statistical test are not identified. [A, pp. 1–2, 9–10, 16]

X2 — HTML form submission. Purpose: assess successful state-changing interaction. Only BlackWidow is the comparator, because it is considered the strongest and specifically oriented to server-side state. Success requires injected text to appear in database-modifying transactions; forms are represented by their action attributes. BlackWidow is modified to emit unique text per field for this experiment only. Table IV reports distinct successful forms in EvoCrawl-only, common, and BlackWidow-only sets. Non-HTML submissions are excluded because they are difficult to track. The headline fivefold submission claim cannot be assumed to mean fivefold distinct forms in Table IV. [A, pp. 9–11]

X3 — Dependency ablation. Purpose: isolate the benefit of dependency information in sequence generation. EvoCrawl-nodt disables this feature; Fig. 6 and Table VIII compare executed-line sets. Authors describe generally higher total coverage with tracking and explain that differing page queues yield unique lines for either variant. However, Dokuwiki's exact table counts imply a small total decrease with tracking; this contradicts the prose's universal 'always larger' statement. [A/B/C, pp. 11, 16]

X4 — Known XSS detection. Purpose: connect exploration to detection using reproducible known vulnerabilities without specialized sanitizer-bypassing payloads. Each tool runs 24 hours on WordPress 4.7.2, Kanboard 1.2.8, ImpressCMS 1.4.4, and Humhub 1.11.0. Table V gives found/available counts. EvoCrawl finds 2/2, 2/3, 2/2, and 0/1 respectively; BlackWidow finds 1/2, 1/3, 0/2, and 0/1. Both fail on vulnerabilities requiring re-login as another user. Better task creation, optional-field omission, and hidden-form discovery explain some additional detections. [A, pp. 11–12]

X5 — New XSS findings. Purpose: apply the detector to the coverage benchmarks' purported latest versions. Authors report five findings across WordPress, HotCRP, and Kanboard, plus one intentional-script Humhub field conservatively counted as a false positive. Developer trust models exclude the two WordPress findings; the reflected HotCRP finding is admin-visible and CSRF-token protected and is not accepted as a vulnerability by the developer. Patch-status descriptions differ across passages and are preserved as uncertainty. [A, pp. 12–13]

X6 — IDOR evaluation. Purpose: assess URL classification and vulnerable endpoint discovery across ten applications. Table VI records discovered/private/public URLs, false positives, configuration-related Vul-Type1 endpoints, and implementation-related Vul-Type2 endpoints. Three Type2 findings occur in ImpressCMS and GitLab. Public resources without lower-privilege interface links explain many false positives. This is not a benchmark with a supplied exhaustive ground-truth set of all IDORs; recall cannot be established. [A/D, pp. 12–13]

## 9. Results

The principal positive result is greater aggregate executed-line coverage in the reported baseline comparisons. The headline 59% is author-reported, not independently recomputed here. For example, Table VII's WordPress versus BlackWidow counts give EvoCrawl 57,398 unique plus 45,868 common lines and BlackWidow 3,368 unique plus 45,868 common lines. Analyst-derived totals are 103,266 versus 49,236; the relative difference is (103,266−49,236)/49,236 ×100, approximately 109.7%. These are executed-line counts, not percentages of all application code. [C, p. 16]

Coverage case studies tie results to concrete prerequisites: HotCRP requires paper submission before review pages; Kanboard requires task creation before task-management functions; WordPress publication requires an event after input; and Opencart exposes some links only after event combinations. These examples support an interaction-order mechanism but are explanatory case studies rather than isolated controlled tests of each cause. [A/D, p. 10]

Table IV shows higher total distinct submitted forms for EvoCrawl in every application, while BlackWidow still has unique successes in nine rows. Analyst-derived totals across rows are EvoCrawl-only 210, common 55, BlackWidow-only 57; therefore 265 versus 112 distinct successful forms, a ratio 265/112 ≈2.37. This does not numerically reproduce the headline fivefold 'more frequently' claim. Frequency, POST-only scope, repeated submissions, and distinct form-action counts may differ, but the supplied text does not provide the bridge needed to settle the discrepancy. [C/D, pp. 2, 10, 16]

For known XSS, summing Table V gives 6/8 detections for EvoCrawl and 2/8 for BlackWidow, or 75% and 25% within the deliberately selected benchmark. The difference is 50 percentage points; the detection-count ratio is 3. These are analyst-derived and do not estimate prevalence or detection rates across arbitrary XSS vulnerabilities. The two tools tie on Humhub, contrary to the prose saying EvoCrawl outperforms on all tested applications. [C, p. 11]

For IDOR, Table VI reports 492 false positives in total: 9+39+0+4+17+385+4+8+0+27. phpBB contributes 385. The paper attributes 374/385 phpBB false positives and 35/39 HotCRP false positives to resources that are public despite lacking lower-privilege interface paths. These results qualify the early general claim of low false-positive behavior. A precision percentage is not derived because the table does not unambiguously define a complete mutually exclusive prediction accounting. [A/C, pp. 2, 12–13]

The eight new findings are five XSS plus three Type2 IDOR reports. Six are described as acknowledged/confirmed, while the reflected HotCRP report is not acknowledged and one ImpressCMS report remains under inspection. Acknowledgment, fix status, exploitability, and organizational threat-model acceptance are distinct outcomes. [A, pp. 12–13]

## 10. Figure-by-Figure

Figure 1 — Prerequisite interface interaction. [B, p. 3] The upper WordPress Quick Draft panel is collapsed; a red box highlights its expansion arrow. A downward arrow leads to an expanded panel containing Title, Content, and Save Draft controls. It has no numerical axes, units, or panels with separate measurements. The figure demonstrates a visibility dependency: useful form interactions require first opening the component. It illustrates motivation rather than measuring performance.

Figure 2 — EvoCrawl architecture. [B, p. 4] The center contains Page Collection above Evolutionary Search. Internal arrows labeled URL connect their discoveries. At left, XSS Vulnerability Detector connects through Sources and Sinks; at right, IDOR Vulnerability Detector connects through Elements and URLs. The encoding is a block diagram, not a quantitative plot. Together with the text, it shows two complementary searches sharing discoveries and feeding security detectors. The diagram does not depict all implementation infrastructure, database feedback, or the full triad-test workflow.

Figure 3 — Dependency-aware mutation. [B, p. 5] Two vertical blue sequence containers show input2 typing, input1 typing, clicking a2, clicking button1, clicking a1, and typing into a textarea. The mutated sequence inserts a red-outlined a3-click after button1-click. A horizontal arrow and 'Add Dependent Genes' label indicate the transformation. There are no axes or units. The visible sequence places a2 before button1; the running-text execution example on p. 4 reverses these two actions. The figure and prose therefore differ in their incidental ordering example, although the prerequisite button1→a3 relationship is clear.

Figure 4 — WordPress sitemap. [B, p. 6] A central wp-admin/ node points via a1 to both wp-json/wp/v2/settings?_locale=user and wp-admin/site-editor.php; a2 points to wp-admin/edit.php?post_type=page; a3 points to wp-admin/admin-ajax.php. Blank nodes represent page URLs, grey a RESTful API target, and blue an AJAX target. Edges represent triggering elements. Multiple outgoing request destinations can follow an action. The diagram supports replay-based accessibility reasoning; node color denotes request type, not a proven privacy classification.

Figure 5 — Pairwise coverage composition. [B, p. 8] A stacked vertical bar chart compares application–crawler pairs. Horizontal labels identify applications and BW, JAK, or CJ. The vertical scale is linear from 0.0 to 1.0 and each bar fills one unit. Blue denotes EvoCrawl-only lines, orange common lines, red comparator-only lines. The denominator is the pairwise represented line union, not all executable application lines. No uncertainty bars or confidence intervals appear. Blue generally exceeds red, especially for Kanboard comparisons; GitLab versus BlackWidow has a much smaller blue fraction. Exact counts come from Table VII, so no pixel-based estimates are substituted.

Figure 6 — Dependency-tracking coverage composition. [B, p. 11] This stacked bar chart uses application labels on the horizontal axis and a linear 0.0–1.0 vertical scale. Blue is tracking-enabled-only, orange common, red no-tracking-only. It has no error bars. Most bars are dominated by common lines; HotCRP, WordPress, Kanboard, and phpBB show visible blue additions, while WordPress also has substantial red. Exact interpretation uses Table VIII. The near-equality for Dokuwiki hides a small reversal that is clear numerically. The figure supports heterogeneous benefits rather than universal strict improvement.

The artifact badge on p. 1 is inspected but treated as publication metadata, not a substantive experimental figure.

## 11. Table-by-Table

Table I — Fitness weights. [A/B, p. 6] Rows map objective counts to weights: successful form submissions 40; filled inputs 20; uploaded files 20; triggered JavaScript events 15; invisible elements −2. These are scoring coefficients, not measured effect sizes or tuned application-specific optima. The authors say the same weights were used without per-application fine-tuning in their evaluation. No uncertainty estimates apply.

Table II — Application selection. [A/B, p. 9] Columns are functionality, version, GitHub stars, and prior-work usage. WordPress: Blog, 6.4.3, 2.3k, [6]/[7]. HotCRP: Content Management System, v3.0b3, 319, [6]. Dokuwiki: Content Management System, 2022-07-31 Igor, 4k, no cited prior work in its row. Drupal: Content Management System, 9.3.15, 4k, [6]. Humhub: Social Software Platform, 1.12.1, 6.2k. Opencart: eCommerce, 4.0.0, 7.3k. phpBB: Forum, 3.8.8, 1.8k, [6]/[8]/[7]. ImpressCMS: Content Management System, 1.4.4, 27. Kanboard: Project Management System, 1.2.22, 8.2k. Gitlab: DevSecOps Platform, 11.5.1, 23.6k. Stars are author-reported snapshots and selection proxies, not outcomes. WordPress and phpBB versions conflict with the artifact benchmark list.

Table III — Statistical comparisons. [A/B, p. 10] EvoCrawl and BlackWidow each have five runs per application according to the caption. P-values are WordPress 0.00096; HotCRP 0.000007; Dokuwiki 0.00082; Drupal 0.004448; Humhub 0.000031; ImpressCMS 0.000502; Kanboard 0.000719; Opencart 0.000009; phpBB 0.000159; GitLab 0.000120. All are below 0.005 by direct comparison, but the supplied work does not identify the test, assumptions, significance threshold, multiple-testing correction, run-level distribution, or uncertainty intervals. Small p-values do not alone quantify practical benefit.

Table IV — Successful form-set overlap. [A/B, p. 10] Triples are EvoCrawl-only/common/BlackWidow-only distinct forms: WordPress 8/7/2; HotCRP 17/6/3; Humhub 25/3/2; Drupal 70/11/33; Kanboard 17/5/0; phpBB 15/12/10; ImpressCMS 7/2/3; Opencart 15/0/1; Dokuwiki 6/8/2; Gitlab 30/1/1. Derived per-application totals are respectively 15 versus 9, 23 versus 9, 28 versus 5, 81 versus 44, 22 versus 5, 27 versus 22, 9 versus 5, 15 versus 1, 14 versus 10, and 31 versus 2. Drupal has the largest distinct-form total for both tools; Kanboard has no BlackWidow-only form. No variance or per-run aggregation rule is shown.

Table V — Known XSS detections. [A/B, p. 11] Columns are WordPress, Humhub, ImpressCMS, Kanboard. EvoCrawl: 2/2, 0/1, 2/2, 2/3. BlackWidow: 1/2, 0/1, 0/2, 1/3. Denominators are selected known vulnerabilities, not number of applications or runs. EvoCrawl leads on three applications and ties at zero on Humhub. Re-login requirements explain both tools' remaining misses. There are no confidence intervals.

Table VI — IDOR detector accounting. [A, text-only p. 13] Rows below preserve columns URLs/private/public/FP/Type1/Type2: WordPress 1025/379/646/9/106/0; HotCRP 526/415/111/39/3/0; Humhub 10729/9451/1278/0/5/0; Drupal 1908/1242/666/4/55/0; Kanboard 7973/4511/3462/17/0/0; phpBB 1684/1527/158/385/0/0; Opencart 1202/870/332/4/60/0; Dokuwiki 3121/864/2257/8/13/0; ImpressCMS 615/593/22/0/111/2; Gitlab 1382/640/742/27/63/1. Humhub has the most discovered URLs, while phpBB has the most false positives. Type1 means configuration/privilege-setting exposure, Type2 implementation faults. The phpBB private/public sum is 1527+158=1685, exceeding its reported total 1684 by one; the supplied text does not resolve this. Table VI lacks a rendered image here, so this is an extracted-text inconsistency rather than a visually confirmed typesetting error.

Table VII — Absolute baseline coverage. [A/B, p. 16] Every triple is EvoCrawl-only/common/comparator-only executed lines. For BlackWidow: WordPress 57398/45868/3368; HotCRP 10706/17679/331; Dokuwiki 4191/12531/284; Drupal 42460/54691/21437; Humhub 10064/21606/1741; ImpressCMS 6157/16485/622; Kanboard 10130/5246/4; Opencart 8353/14500/672; phpBB 21781/14142/11616; GitLab 10775/172367/617. For JAK: WordPress 58721/44545/1063; HotCRP 14447/13938/131; Dokuwiki 3099/13623/44; Drupal 15843/45460/1195; Humhub 16392/15279/398; ImpressCMS 8418/14224/624; Kanboard 9626/5750/1193; GitLab 19398/163744/419. For CrawlJAX: WordPress 67905/35361/673; HotCRP 11412/16973/250; Dokuwiki 8885/7837/22; Drupal 46545/14758/767; Humhub 22463/9207/290; ImpressCMS 11638/11004/390; Kanboard 10681/4695/488; GitLab 14323/168819/2652. Missing JAK/CrawlJAX entries for Opencart/phpBB are explained failures, not zero coverage. No dispersion or total-application line denominator is given. Drupal's EvoCrawl total differs sharply across comparator blocks: 97151 versus BlackWidow, 61303 versus JAK/CrawlJAX. The table does not explain whether these are distinct runs, aggregation differences, or an error.

Table VIII — Absolute dependency ablation coverage. [A/B, p. 16] Triples are enabled-only/common/disabled-only: WordPress 29676/73590/21738; HotCRP 8578/19807/627; Dokuwiki 91/16631/112; Drupal 2321/58982/1318; Humhub 576/31094/34; ImpressCMS 1039/21603/604; Kanboard 4484/10892/246; Opencart 1151/21675/59; phpBB 8926/17340/3113; GitLab 3034/180108/2131. Tracking's net line benefit is enabled-only minus disabled-only. For Dokuwiki, 91−112=−21; totals are 16722 versus 16743. For HotCRP, 8578−627=7951 additional lines. These derived contrasts expose both substantial application-specific gains and a small exception to the universal prose claim. No ablation run counts or uncertainty intervals are supplied.

## 12. Diagram / Architecture

The operational loop combines breadth and depth. PM consumes seeds, quickly probes links/events/forms, and publishes discovered pages. ESM consumes pages, generates candidate action sequences, executes them, observes browser/database feedback, updates dependency information, selects high-scoring candidates, and generates descendants. Newly found URLs return to the shared discovery process. Kafka implements durable exchange, while separate cookie sessions require token replacement. [A, pp. 3–8]

The dependency loop is local: action → DOM mutation → new element association → sequence mutation → later action execution. Figure 3 illustrates one step of this feedback. It does not establish that all dependencies are learned, that every association is causal, or that arbitrary cross-page workflows are preserved. [A/D]

The XSS data path is source field → substituted payload → application processing → browser execution → unique identifier in the global list → source/sink linkage. The IDOR data path is privileged crawling → sitemap → less-privileged replay → public/private classification → direct triad requests → response analysis → candidate unauthorized endpoint. Figures 2 and 4 show complementary views of these paths; the full detector logic requires the text on pp. 6–7.

## 13. Equations and Mathematical

Equation (1), p. 6, is f = Σ_i o_i·w_i. It is a scalar weighted-sum fitness function. f is a sequence's score; o_i is an objective count; w_i is its associated coefficient. The important operations are multiplying each count by its weight and summing the products. Table I supplies five objective types, although the displayed equation does not explicitly print summation bounds.

Expanding the reported terms gives f = 40·forms + 20·filled_inputs + 20·uploads + 15·JS_events − 2·invisible_elements. Inputs are observed action/result counts from evaluating a sequence; output is a heuristic score used to select sequences for further generations. This is not a probability, a calibrated vulnerability risk, a code-coverage percentage, or a learned neural loss. [A, pp. 5–6]

The authors explain that rewarding accepted submissions helps optional-field omission: a sequence with one extra difficult field can lose the 40-point submission reward while gaining only 20 points for that filled input. This local example does not prove that accepted forms dominate every possible longer sequence; enough other rewarded actions could change the sum. The latter is analyst interpretation of the actual coefficients. [A/D]

The score description mentions an initial uniform score that is dynamically updated, while Equation (1) gives only a weighted sum. Its initial constant is not specified. Likewise, exact counting conventions for multiple database observations are not fully formalized. These details remain unspecified rather than invented.

On p. 2, the paper gives n^11 as a search-space expression for n-interaction sequences with ten JavaScript events and one form. Both supplied visual and extraction support that printed ordering. No derivation or counting convention is supplied. The safe conclusion is the authors' qualitative claim of rapid combinatorial growth; the expression should not be silently repaired or used as a verified complexity bound.

Set notation in Tables VII–VIII has a separate role: A\B means lines executed only by EvoCrawl; A∩B means common executed lines; B\A means comparator-only lines. Therefore |A|=|A\B|+|A∩B| and |B|=|B\A|+|A∩B|. These identities underlie explicitly labeled derived totals. No formal theorem or proof is presented.

## 14. Interpretation and Discussion

The evidence supports the authors' central mechanism: some security-relevant functionality depends on successful prior actions, and coarse form handling can prevent reaching it. Searching individual interactions and preserving visibility prerequisites increases the useful paths found within a fixed budget. The benchmark results connect this mechanism to coverage, distinct form success, and selected vulnerability discovery. [A]

O1 and O3 receive evidence from coverage/form experiments and case studies. O2 receives ablation evidence with heterogeneous effects and a small numerical exception. O4 receives known-XSS results and new-finding reports, qualified by payload selection, cross-user workflow failures, and developer threat-model disagreements. No formal hypothesis is available to mark simply supported or rejected.

Several unresolved consistency points materially affect interpretation. Table II lists WordPress 6.4.3 and phpBB 3.8.8, while Artifact Appendix A lists WordPress 6.1.1 and phpBB 3.3.8. Table VII's Drupal totals vary across baseline columns, and Table VIII's phpBB enabled total is 8926+17340=26266, compared with 21781+14142=35923 in Table VII. These may represent different experimental realizations, but the supplied text does not identify the relevant aggregation/run choices. They prevent treating all tables as one fixed executed-line set.

The headline fivefold submission frequency differs from the approximately 2.37 distinct-form ratio derived from Table IV. Table V ties on Humhub despite a universal outperform statement. Table VIII reverses the universal ablation claim for Dokuwiki. Page 7 says five access-denied sentences are enough per application, whereas the appendix lists varying counts, from one to five. The latter could mean an upper bound rather than exactly five, but this is not clarified.

Parameter discussion also needs care: p. 6 says weights were not fine-tuned per application in the experiments; p. 13 says optimal results currently require manual fitness-parameter adjustments. These can describe fixed evaluation settings versus an aspiration for optimal deployment, but that reconciliation is interpretation, not an explicit resolved statement. Patch descriptions shift between future fixes on p. 12 and fixed findings on p. 13; no timeline is supplied to settle them.

Research relevance [D]: a browser-connected agent participates in sequences that can create durable objects, submit executable content, and cross access-control boundaries. Those environmental affordances add failure pathways beyond producing an isolated text answer. EvoCrawl demonstrates the existence and importance of those web pathways, but does not establish that adding a browser makes an LLM quantitatively more vulnerable or identify an LLM-specific causal mechanism. Its brief Mind2Web discussion concerns autonomous scanning suitability, not an agent-versus-standalone security experiment.

## 15. Contributions and Novelty

Conceptual contribution: the authors identify successful client-side event execution and server-state construction as central impediments to comprehensive vulnerability exploration. Methodological/algorithmic contribution: they combine fine-grained evolutionary interaction search with learned visibility dependencies and a browser/database-informed fitness function. System contribution: PM supplies rapid discovery while ESM supplies deeper sequence search. [A, pp. 2–7]

Detector contribution: a modular XSS integration traces executable payloads, while a custom IDOR detector combines interface-derived public filtering, lockstep replay, and three-user response comparison. Empirical contribution: ten-application evaluation, dependency ablation, selected known-XSS comparisons, and eight new-finding reports. Implementation contribution: an openly referenced artifact with recorded installation/workflow information. [A, pp. 2, 6–13, 16–17]

There is no new LLM, training dataset, formal security theorem, or agent-security benchmark. The related-work novelty claims are the authors' positioning, not independently verified priority claims. Their distinction is evolutionary search over interactions, whereas cited evolutionary and reinforcement-learning XSS systems primarily adapt payloads. [A, p. 14]

## 16. Limitations

Authors' stated limitations: required fields with formats the heuristics cannot infer remain blockers (p. 3). Nondeterministic pages can induce false dependencies (p. 5). Intermittent URL tokens are not captured by the exchange heuristic, producing invalid seeds (p. 8). The 24-hour budget leaves queued pages unexplored, and differing scheduling yields different unique successes (p. 11). Known-XSS tests exclude sanitizer-bypass requirements, and cross-user re-login requirements cause missed detections (pp. 11–12). Public resources absent from a less-privileged interface and incomplete navigation discovery produce IDOR false positives (p. 12). Manual fitness tuning and redundant URL-based seeds are the two dedicated limitations in Section VII (p. 13).

Additional evidence-based analyst observations [D]: database instrumentation narrows applicability relative to an external-only crawler. Form-action counting and database-text matching are imperfect proxies for distinct server states. The selected ten applications and administrative exploration setting do not establish performance for arbitrary sites, unauthenticated users, or modern AI browsing tasks. The detector's trust-policy inference cannot replace an explicit authorization specification. No exhaustive vulnerability ground truth is given for newly found IDORs. Statistical reporting lacks test identity and uncertainty intervals. Several numerical/version/status discrepancies remain unresolved.

Developer acceptance further limits security interpretation: trusted-admin/editor script insertion is not considered a vulnerability by WordPress's reported policy, and the admin-only, token-protected reflected HotCRP report is not accepted by its developer. These are substantive threat-model qualifications, not merely missing patches. [A, pp. 12–13]

## 17. Threats to Validity

The following validity labels are analyst organization [D]; they are not presented as an author-written validity taxonomy.

Internal validity: application resets, equal CPU resources, and disabling detectors in coverage tests are useful controls. Remaining concerns include stochastic schedules, incompletely specified aggregation across runs, and the form-only modification of BlackWidow. Different page queues can explain tool-exclusive successes without demonstrating that the other tool is intrinsically incapable of them.

Construct validity: executed lines approximate exploration, and successful database-bearing HTML forms approximate state exploration. Neither directly counts distinct meaningful states or all exploitable vulnerabilities. Figure 5's normalized pairwise union is not total program coverage. Developer acceptance and actual attacker capability also differ from automatic execution detection.

External/ecological validity: applications span several functions, but selection is not random, some baseline/application pairs fail, high privileges are used, and potentially disruptive configuration/user/plugin/logout areas are excluded. Exclusions improve experimental stability while narrowing tested behavior. The claimed latest-version condition is qualified by contradictory benchmark versions.

Statistical conclusion validity: five-run comparisons are reported with small p-values, but the test, independence assumptions, effect uncertainty, raw runs, and multiple-comparison treatment are absent. The average 59% calculation is not fully reproducible from the described aggregation. Ablation variability is not quantified.

Reproducibility: the artifact identifies dependencies and workflows, but actual repositories, container definitions, configuration defaults, and output files were not inspected. Actual evolutionary settings and random seeds are not supplied in the paper text. Eight-hour artifact demonstrations are expressly partial relative to 24-hour research runs. No independent reproduction is claimed here.

Generalizability to the user's question: the research contains no experiment isolating the security effect of connecting an LLM to the web. It can support discussion of environmental attack surfaces, not an empirical comparative vulnerability conclusion.

## 18. Future Work and Open Questions

A. Author-proposed future work. The authors propose studying the influence of fitness parameters and automatically tuning them for individual applications. They also propose better seed distinction, potentially using DOM comparison rather than URL identity, to reduce redundant crawling. The p. 6 discussion similarly identifies weight tuning as future study. [A, pp. 6, 13]

B. Analyst open questions [D]. How sensitive are gains to weights, population size, sequence length, and random scheduling? Which database-free feedback signals could preserve performance? How often do visibility heuristics infer false dependencies? Can cross-user workflows be explored without sacrificing state consistency? Can policy specifications reduce false positives from interface-derived privacy? How do distinct-state coverage and vulnerability recall change with longer budgets or different privilege levels? What exact aggregation produces the 59% and fivefold claims? Which benchmark versions underlie each table?

For AI-agent research, the remaining question is whether and how an LLM controller changes these interaction risks, including its handling of untrusted page content and authority to take actions. These are proposed research questions, not evaluated mechanisms or results from EvoCrawl.

## 19. Terminology and Notation Glossary

| Term | Meaning within this work |
|---|---|
| EvoCrawl | Combined page discovery, evolutionary interaction search, and detector system. |
| PM | Page Collection Module; rapidly discovers links and simple event/form paths. |
| ESM | Evolutionary Search Module; searches ordered interactions on a page. |
| XVD / XSS | XSS Vulnerability Detector / Cross-Site Scripting; traces injected script execution. |
| IVD / IDOR | IDOR Vulnerability Detector / Insecure Direct Object Reference; probes unauthorized resource access. |
| DOM | Document Object Model; browser page structure observed for mutations. |
| HTML form | Structured input collection submitted through browser interaction. |
| JavaScript event | Client-side behavior triggered by an interaction. |
| AJAX | Asynchronous JavaScript and XML; term used for dynamic application requests. |
| URL / href | Address of a resource / link-target attribute extracted by PM. |
| CSS selector | Element-identifying expression used for interactions and replay. |
| Seed | URL plus optional DOM-changing EVENT used as a crawl target. |
| Gene | Web element paired with an interaction type. |
| Crossover | Recombination of portions of promising sequences. |
| Mutation | Sequence alteration, including inserting dependency-constrained actions. |
| Fitness f | Weighted heuristic score used to select sequence descendants. |
| o_i / w_i | Objective count / coefficient for the corresponding objective. |
| Source / sink | Injection location / observed execution location. |
| Tainted value | Uniquely marked input tracked into database observations. |
| Sitemap | URL/request graph connected by triggering interface elements. |
| Triad test | Response analysis using one privileged and two equally lower-privileged users. |
| FP | False positive; an automatic finding judged not to be a vulnerability under the evaluation. |
| Vul-Type1 / Type2 | Configuration-related endpoint exposure / implementation-related vulnerability. |
| CSRF | Cross-Site Request Forgery; token protection is a condition on the HotCRP finding. |
| A\B, A∩B, B\A | EvoCrawl-only, shared, and comparator-only executed-line sets. |
| LLM | Large Language Model; appears in related work, not in EvoCrawl's controller. |
| SPA | Single-page application; cited as a challenge for older crawlers. |

## 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Primary application set | 10 | applications | Coverage and new-finding evaluation | Author-reported | pp. 2, 9 |
| Comparison crawlers | 3 | tools | BlackWidow, JAK, CrawlJAX | Author-reported | pp. 2, 8 |
| Main testing budget | 24 | hours/run | Configured testing sessions | Author-reported | p. 9 |
| Repetitions | 5 each | runs/application | EvoCrawl and BlackWidow in Table III | Author-reported | p. 10 |
| VM allocation | 4 CPU; 6 GB | resources | Each crawler environment | Author-reported | p. 9 |
| Headline coverage improvement | 59% | relative increase | Author average; aggregation unspecified | Author-reported | pp. 1–2 |
| Coverage improvement range | 6%–192% | relative increase | Compared with BlackWidow | Author-reported | pp. 9–10 |
| Headline HTML submission frequency | 5× | ratio | POST-form claim; distinct-count bridge unspecified | Author-reported | pp. 2, 16 |
| Distinct successful forms | 265 vs 112 | forms | Sum of Table IV totals | Analyst-derived | p. 10 |
| Distinct-form ratio | ≈2.37 | ratio | 265/112; not headline frequency | Analyst-derived | p. 10 |
| Known-XSS detections | 6/8 vs 2/8 | selected vulnerabilities | Sum of Table V; EvoCrawl vs BlackWidow | Analyst-derived | p. 11 |
| Known-XSS rate difference | 50 | percentage points | 75%−25% on selected sample | Analyst-derived | p. 11 |
| New findings | 8 = 5+3 | reports | XSS plus Type2 IDOR | Author-reported | pp. 12–13 |
| Developer-acknowledged findings | 6 | reports | Of eight reported new findings | Author-reported | p. 13 |
| Humhub intentional-script finding | 1 | false positive | XSS field accepts scripts by design | Author-reported | p. 12 |
| Total IVD false positives | 492 | URLs/findings | Sum of Table VI FP column | Analyst-derived | p. 13 |
| Dokuwiki tracking difference | −21 | executed lines | 91 enabled-only minus 112 disabled-only | Analyst-derived | p. 16 |
| Fitness coefficients | 40,20,20,15,−2 | score/count | Forms, inputs, uploads, events, invisible elements | Visually readable | p. 6, T1 |
| Artifact demonstration budget | 8 | compute hours/experiment | Partial E1/E2/E3 demonstrations | Author-reported | p. 17 |
| Artifact setup estimate | 30 | human minutes/experiment | Listed preparation estimate | Author-reported | p. 17 |
| Runtime dependencies | Node 12.22.12; npm 6.14.16 | versions | Linux, Ubuntu preferred | Author-reported | p. 16 |

No approximate plot estimates are needed: available exact tables are preferred. Numbers above preserve conditions and distinguish derived calculations from reported headlines.

## 21. Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| State and code execution jointly matter | Abstract and repository prerequisite example | Framing/O1 | p. 1 | Author explanation; HIGH source fidelity. |
| Fine-grained search can omit difficult optional fields | Sequence design and application case studies | F1/F3, X1/X2 | pp. 2–5, 10 | Does not solve difficult required fields. |
| Evolutionary search uses browser/database feedback | Gene execution, dependency map, weighted score | E1/T1/F2 | pp. 3–6 | Exact evolutionary hyperparameters absent. |
| Coverage exceeds baselines in reported comparisons | Pairwise executed-line counts and p-values | F5/T3/T7/X1 | pp. 8–10, 16 | Baseline failures, aggregation and Drupal inconsistency qualify interpretation. |
| More distinct HTML forms succeed | Unique/common form counts | T4/X2 | pp. 10–11 | Distinct-count ratio differs from headline frequency. |
| Dependencies generally help exploration | Enabled/disabled pairwise counts | F6/T8/X3 | pp. 11, 16 | Dokuwiki is a small numerical exception. |
| Exploration improves selected known-XSS detection | 6 versus 2 summed detections | T5/X4 | pp. 11–12 | Selected easy-payload sample; re-login failures; Humhub tie. |
| IVD uses policy inferred from interface reachability | Sitemap replay and direct triad tests | F4/T6/X6 | pp. 6–7, 12–13 | Missing UI paths can make public resources appear private. |
| Eight new findings have differing acceptance | Finding-by-finding disclosure summary | X5/X6 | pp. 12–13 | Six acknowledged; trust models and status wording differ. |
| Web-agent relevance is indirect | State-changing browser paths and authorization examples | Analyst synthesis | pp. 1, 6–7, 14 | No LLM-versus-agent security comparison; inference only. |

## 22. Very Simple Explanation

Imagine testing a website as if it were a game with locked rooms. Clicking every visible link is not enough. Some rooms appear only after you create an account, submit a paper, make a task, or open a hidden panel. A security bug may sit behind one of those steps. A tester that cannot complete the steps never gets the chance to discover it.

EvoCrawl tries different action sequences and keeps useful ones. It can learn that opening a panel must happen before filling its fields. It can also discover that leaving a troublesome optional field blank makes a form work. One component finds pages quickly; another searches action combinations more carefully. Separate detectors then look for injected scripts or resources that a less-privileged user should not be able to access.

In the authors' selected tests, this explores more code and successfully submits more forms than the comparison tools. It also finds more of a small set of known scripting problems. But it still misses some workflows, produces false alarms, and reports several findings whose developers disagree about whether they violate the intended security rules. The tables also contain some unresolved inconsistencies.

For web AI agents, the useful lesson is about their environment: a browser can change stored information, trigger code, and make requests under a user's permissions. Those are important security boundaries. This paper helps explain those web pathways, but it does not test whether an AI browser agent is more vulnerable than a standalone chatbot, and it does not study malicious instructions hidden in web pages.

## Completeness Audit

The inventory denominator is the supplied 17-page work. 'Fully represented' means the substantive component is explained, not that every sentence is reproduced. Text-only inspection is disclosed separately from visual inspection.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue/abstract | Yes, text+image | Yes | Fully represented | EvoCrawl; Xiangyu Guo, Akshay Kawlay, Eric Liu, David Lie, University of Toronto; NDSS Symposium 2025, 24–28 February, San Diego; DOI 10.14722/ndss.2025.230366. |
| S1 Introduction and contribution bullets | Yes, text+image | Yes | Fully represented | Problem, two conditions, novelty and headlines. |
| S2 Motivation | Yes, text+image | Yes | Fully represented | Dependencies, sequence search, optional/required distinction. |
| SS3A Page Collection | Yes, text+image | Yes | Fully represented | Link, event, and form stages; seed queue. |
| SS3B1 Sequence generation/evaluation | Yes, text+image | Yes | Fully represented | Genes, crossover, execution, input heuristics. |
| SS3B2 Dependency tracking/enforcement | Yes, text+image | Yes | Fully represented | Dynamic map and mutation; false dependency caveat. |
| SS3B3 Gene elimination | Yes, text+image | Yes | Fully represented | Navigation recording and subsequent removal. |
| SS3B4 Fitness | Yes, text+image | Yes | Fully represented | Equation, coefficients, rationale, unspecified initial constant. |
| SS3C1 XVD | Yes, text+image | Yes | Fully represented | Source/sink trace and timestamp identifiers. |
| SS3C2 IVD | Yes, text+image | Yes | Fully represented | UI policy, replay, lockstep, triad test. |
| S4 core implementation | Yes, text+image | Yes | Fully represented | TestCafe, rrweb, Kafka, processes, cookies, tokens. |
| SS4A rrweb / SS4B setup | Yes, text+image | Yes | Fully represented | Custom replay and user configuration. |
| SS5A experiment setup | Yes, text+image | Yes | Fully represented | Resources, controls, exclusions, instrumentation, settings. |
| SS5B coverage and four case studies | Yes, text+image | Yes | Represented in compressed form | HotCRP, Kanboard, WordPress, Opencart mechanisms retained. |
| SS5C form submissions | Yes, text+image | Yes | Fully represented | Success metric, action attributes, excluded non-HTML submissions. |
| SS5D dependency benefits | Yes, text+image | Yes | Fully represented | Ablation and queue/scheduling caveats. |
| SS6A known XSS | Yes; p. 12 text-only | Yes | Fully represented | Selection criteria, versions, all application explanations. |
| SS6B new XSS | Yes, text-only | Yes | Fully represented | Five findings, trust policies, intentional-script false positive. |
| SS6C IDOR | Yes, text-only | Yes | Fully represented | Types, false-positive causes, all table rows. |
| SS6D new-finding summary | Yes, text-only | Yes | Represented in compressed form | Eight reports and endpoint/field details below. |
| S7 parameter tuning / seed selection | Yes, text-only | Yes | Fully represented | Both dedicated limitations and proposed changes. |
| SS8A access-control scanners | Yes; mixed text/image | Yes | Represented in compressed form | Prior-work distinctions summarized below. |
| SS8B web crawlers | Yes, text+image | Yes | Represented in compressed form | Navigation enumeration, JavaScript, DOM state, fuzzing positioning. |
| SS8C evolutionary search | Yes, text+image | Yes | Fully represented | Interaction search versus payload adaptation. |
| SS8D machine learning | Yes, text+image | Yes | Fully represented | Link and Mind2Web are author-positioned comparisons. |
| S9 Conclusion | Yes, text+image | Yes | Fully represented | Evolution plus dependencies and state-changing interactions. |
| Explicit research questions/hypotheses | Yes, absence assessed | Yes | Fully represented | None formally stated; informal objectives retained. |
| X1/X2/X3 | Yes | Yes | Fully represented | Coverage, forms, dependency ablation kept separate. |
| X4/X5/X6 | Yes | Yes | Fully represented | Known XSS, new XSS, IDOR kept separate. |
| F1/F2/F3/F4/F5/F6 | Yes, all visually | Yes | Fully represented | Each interpreted with encoding and caveats. |
| T1/T2/T3/T4/T5 | Yes, all visually | Yes | Fully represented | Exact substantive rows and conditions retained. |
| T6 | Yes, text-only | Yes | Fully represented | No visual verification; phpBB arithmetic flagged. |
| T7/T8 | Yes, visually | Yes | Fully represented | Exact overlap counts preserved. |
| E1 and search-space expression | Yes, visually | Yes | Fully represented | Fitness defined; n^11 uncertainty flagged. |
| Numbered algorithms/theorems | None present | Yes | Fully represented | Procedural algorithm described without invented pseudocode. |
| Major contribution bullets | Yes | Yes | Fully represented | Conceptual, algorithmic, system, empirical, artifact distinctions. |
| Author-stated limitations throughout | Yes | Yes | Fully represented | Includes limitations outside Section VII. |
| General appendix configuration lists | Yes; mixed text/image | Yes | Represented in compressed form | Purpose, examples, variable phrase counts; exact code strings not certified. |
| Artifact Appendix A.A–D | Yes, text+image | Yes | Fully represented | Access, requirements, versions, workflow, major claims. |
| Artifact Appendix A.E / E1–E3 | Yes, text-only | Yes | Fully represented | Procedures summarized below; no execution claimed. |
| Acknowledgments/references | Yes; mixed text/image | Yes | Inspected but deliberately compressed as secondary | Bibliographic entries not independently validated or individually reproduced. |
| Artifact badge | Yes, visually | Yes | Inspected but deliberately compressed as metadata | Does not substitute for reproduction. |
| External repository/Zenodo/README/Dockerfiles | No | Limit disclosed | Inaccessible | Referenced artifacts not supplied or opened. |
| Supplied supplementary files | None identified | Yes | Fully represented | No absent supplement is claimed reviewed. |

Additional inventory details retained for traceability: the two WordPress XSS locations are comment and post-title fields, requiring editor/admin privileges. HotCRP findings concern decision names on settings/decisions and round names on settings/reviews. Kanboard concerns the application URL field on settings/api. ImpressCMS IDOR reports concern userinfo.php?id=1 and /libraries/image-editor/image-edit.php?image_id=1&uniq=. GitLab concerns autocomplete/users.json?search=&active=true&current_user=true, reported to expose user information including avatar URLs, usernames, and states. These are author-described locations, not independently tested endpoints. [A, p. 13]

Compressed related-work accounting: the authors contrast source-language-dependent white-box access-control methods with dynamic exploration; Fuzz-lightyear and RESTler use API specifications; AuthScope uses mobile-app traffic differences and exploration but is criticized for dynamic-resource handling and public/private assumptions. They describe BlackWidow/JAK event enumeration, Enemy of the State's lack of client-side JavaScript coverage, and CrawlJAX's DOM-state approach without their dependency tracking. Deemon and interaction-trace logic testing address other vulnerability classes. Grey-box web fuzzers are positioned as either PHP-specific or dependent on an underlying scanner. Link adapts XSS payloads using reinforcement learning, while EvoCrawl prioritizes exploration. These are author characterizations only; the cited works themselves were not read. [A, pp. 13–15]

Compressed appendix configuration accounting: blocked-page keywords exclude credential/account editing, configuration, plugin, authentication, and logout-related areas; examples include password, maintenance, plugin, logout, signin, and roles. Access-denied lists contain application-specific phrases such as Access denied, Not Allowed, Access Forbidden, not allowed, and Not Found. Their varying lengths qualify the main-text five-sentence statement. Exact extraction-spaced configuration strings are deliberately not presented as executable copies. [A, pp. 15–16]

Artifact Appendix detail: access is reported through Zenodo DOI 10.5281/zenodo.13617803 and an anonymous repository, alongside the main-text GitHub repository reference. Hardware dependencies are listed as none; software requires Linux, preferably Ubuntu, Node 12.22.12 and npm 6.14.16. The benchmark list differs from Table II for WordPress and phpBB as already noted. Workflow is install/configure benchmark, enable coverage/database logging, configure artifact, execute. Artifact E1 is an eight-hour coverage/form demonstration using crawl/monit.py in crawler mode. E2 uses XSS mode and identifies sources.json/sinks.json matched by identifiers. E3 adds two lower-privileged users, uses IDOR mode, and runs detect.sh for endpoint results. Each lists 30 human minutes and eight compute hours. These are documentary instructions, not actions performed in this analysis; authors explicitly say full reproduction needs 24-hour experiments. [A, pp. 16–17]

### Missing or inaccessible material

There are no missing numbered pages within the supplied extracted 1–17 sequence. Images for pp. 12, 13, 15, and 17 were not provided, so typography and Table VI alignment on those pages cannot be visually cross-checked. Referenced code, README files, benchmark Dockerfiles, raw run outputs, logs, configuration defaults, and external disclosure/patch pages were not inspected. No complete literal XSS payload, raw statistical sample, or fully specified evolutionary parameter set is available in the supplied paper text.

### Uncertain interpretations

Unresolved points are the n^11 search-space expression; distinct forms versus fivefold submission frequency; Drupal's changing EvoCrawl coverage totals; differing phpBB totals between baseline and ablation tables; the text-only phpBB URL partition mismatch; WordPress/phpBB benchmark versions; unspecified statistical test and average aggregation; patch-status changes without dates; fixed evaluation weights versus manual optimal tuning; variable access-denied phrase counts; and the minor Fig. 3 versus prose action ordering difference. None is silently reconciled.

### Deliberately compressed material

Repeated motivation, repeated headline claims, repeated per-application success explanations, the full bibliography, acknowledgments/funding identifiers, and extraction-spaced configuration lists are compressed. Their scientific roles, key mechanisms, and qualifications are retained. The table rows necessary for checking numerical outcomes are preserved rather than replaced by plot estimates.

### Potential omissions

Every identified substantive section, subsection, visual, table, equation, experimental condition, contribution, dedicated limitation, and appendix procedure has a representation above. This is an inventory-based account of the supplied material, not a claim of independent scientific verification or literal preservation of every sentence. Repository-dependent implementation details and empirical validation remain outside the accessible evidence.
