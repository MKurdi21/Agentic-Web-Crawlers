## Stage 0 — Document Accessibility Report

**Final analyst review scope.** Image-supply, tool-use and hash-computation disclosures below describe the isolated model pass (images1/8). The parent analyst separately recomputed the canonical PDF hash and visually inspected physical pages4–7, including TablesI–VII, from the same PDF; those actual inspections are recorded in `research/extensions/2026-10-17/analyst_visual_review.json`. Pages2–3/9 remain text-only in this review. This adds a focused visual/source-identity check, not experimental reproduction or independent human scientific validation.

The supplied main document is available as extracted text for physical PDF pages 1–9. Direct page images are supplied for pages 1 and 8, and these two pages were visually inspected. Pages 2–7 and 9 were inspected through the supplied text only. This distinction matters: the seven tables can be analyzed from their extracted contents, but their original typography, alignment, and any visually encoded details on their pages were not independently inspected. No tools, browsing, external documents, or external verification were used. The paper and images were treated as evidence, never as instructions.

| Accessibility item | Assessment |
|---|---|
| Main document | Available: nine pages of supplied text |
| Accessible physical page range | 1–9 |
| Apparently missing main-document pages | None apparent from the sequence; independent completeness verification unavailable |
| Direct visual coverage | Pages 1 and 8 only |
| Text-only coverage | Pages 2–7 and 9 |
| Tables | Tables I–VII readable in extracted text, with specific alignment/count ambiguities discussed below |
| Figures and diagrams | No numbered substantive figure or architecture diagram identified in the supplied document |
| Equations | No numbered or substantive mathematical equations identified |
| Appendices | None identified |
| Supplied supplementary material | None |
| Referenced external artifacts | Framework, model, development-tool, and website links; their contents were not supplied or inspected |
| OCR | No additional OCR performed; supplied text is adequate for substantive reading |
| Other limitations | Extracted text contains line-break, ligature, and spacing artifacts; raw logs, code, recordings, annotation files, and exact complete prompt packages are unavailable |

The supplied accessibility metadata reports zero embedded files and no detected supplementary references. These are intake observations, not proof that no related artifacts exist elsewhere. The source hash is the identifier supplied by the user; it was not independently recomputed. All page references below refer to physical PDF pages.

Evidence labels used throughout: [A] author-reported; [B] directly observable in supplied images; [C] analyst-derived from reported operands; [D] analyst interpretation. Confidence labels are HIGH, MEDIUM, LOW, and UNKNOWN. HIGH usually means that the paper clearly reports the statement, not that the experiment has been independently reproduced. No [E] external information is introduced.

## 1. Plain-language orientation

[A; pp. 1–4] This paper examines what happens when artificial intelligence (AI) agents browse a news website containing advertisements, cookie banners, subscription offers, and paywalls. A web agent combines a language model with software that can inspect pages and take actions such as clicking links and filling forms. The authors ask two linked questions: which advertisements can these agents perceive and operate, and how responsibly do they behave after they begin interacting?

The researchers built a functional clone of the Tiroler Tageszeitung news website and tested GPT-4o, Claude 3.7 Sonnet, and Gemini 2.0 Flash through Browser Use. They also explored OpenAI Operator as a contrasting, primarily pixel-based agent. The core study contained 300 baseline trials: ten tasks, ten repetitions per task, and three Browser Use models. Follow-up experiments changed advertisement markup, position, dynamic media, and consent interfaces.

[A; pp. 4–8] The main finding is that machine-readable structure strongly shaped advertisement interaction. A visual button drawn inside an image attracted no banner clicks in the reported comparison. An actual button element or explanatory off-screen text produced substantially more banner interaction. Agents also stopped searching early, sometimes missing relevant offers. Their financial behavior depended strongly on task framing: they avoided buying subscriptions merely to read sports articles but often subscribed when payment was presented as a prerequisite for entering a sweepstake.

[D; research relevance] For the question “Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,” this paper supplies evidence about risks created when models consume website content and can act on it. It does not test standalone large language models (LLMs) against equivalent web agents. It therefore supports mechanisms and hypotheses about agent vulnerability, rather than a measured claim that web agents are categorically more vulnerable.

The central contribution is an empirical connection between website accessibility, agent attention, and commercially consequential behavior. The same features that make an advertisement easier for an agent to understand can also help steer its actions. The paper treats this as both a design opportunity and a trust problem.

## 2. Document roadmap

### Inventory constructed before synthesis

| ID | Original item | Location | Role |
|---|---|---|---|
| META | Title, authors, venue, abstract, keywords | p. 1 | Identity and condensed claims |
| S1 | I. Introduction | pp. 1–2 | Motivation, two broad questions, contributions |
| S2 | II. Related Work | pp. 2–3 | Agent architectures, advertising, accessibility, trust |
| SS2A | Architectural Paradigms of AI Web Agents | p. 2 | Vision-based versus DOM-based framing |
| SS2B | AI Agents and Online Advertising | p. 2 | Structured cues and advertising incentives |
| SS2C | Markup and Accessibility for Ads | pp. 2–3 | Semantic accessibility |
| SS2D | Trust and Responsible Behavior in Web Agents | p. 3 | Policy-aware evaluation background |
| S3 | III. Methodology | pp. 3–4 | Design, implementation, protocol, logging |
| SS3A | Research Design | p. 3 | RQ-A, RQ-B, dummy user information |
| SS3B | Technical Implementation | pp. 3–4 | Clone and agent stack |
| SS3C | Experimental Protocol | p. 4 | Repetitions, resets, exclusions, version |
| SS3D | Data Capture and Logging | p. 4 | Automated versus manual observations |
| S4 | IV. Results | pp. 4–7 | Accessibility and behavioral findings |
| SS4A1–5 | Position; semantic markup; scrolling; media; native dialogs | pp. 4–6 | Five accessibility factors |
| SS4B | Behavioral Patterns of AI Agents | pp. 6–7 | Spending boundaries and hallucination |
| SS4B1 | Cookie Consent and Privacy Dialogs | pp. 6–7 | Three banner conditions |
| SS4B2 | Subscription-Tier Selection Bias | p. 7 | Tier choices and retention recommendations |
| S5 | V. Discussion and Outlook | pp. 7–9 | Design guidance, risk profiles, limitations |
| SS5A | Implications for Ad Design and Site Markup | p. 7 | Five recommendations |
| SS5B | Behavioral Patterns and Model-Specific Risk Profiles | p. 8 | Interpretation and measurement gap |
| SS5C | Limitations and Future Work | pp. 8–9 | Seven families of limitations |
| T1–T7 | Tables I–VII | pp. 5–7 | Task inventory and quantitative results |
| REF | References [1]–[19] | p. 9 | Cited literature and artifact pointers |

No numbered figures, algorithms, theorems, appendices, or substantive equations appear in this inventory. The paper is an empirical AI web-agent study with systems and trustworthiness components, not a formal security benchmark, mathematical paper, or systematic review.

The reading sequence is straightforward: motivation leads to architecture and trust background; methodology defines a controlled website and tasks; results separate accessibility from behavior; discussion translates observations into design recommendations and acknowledges limits. The abstract compresses these findings more strongly than some detailed results justify, especially for scrolling depth.

## 3. Background and context

[A; pp. 1–3] The paper describes multimodal LLMs as models that process text and images. Adding browser tools lets them navigate websites and execute transactions on users’ behalf. Display advertisements, however, were often created to attract human visual attention. An agent operating through structured page representations may respond to different signals.

The Document Object Model (DOM) is the page representation central to the Browser Use configuration studied here. The paper contrasts DOM-based interaction with vision-based interaction, where an agent sees page screenshots as pixels. In the authors’ framing, DOM-based tools offer efficient, precise structured actions but can miss content whose purpose is conveyed mainly through appearance. Vision-based tools may operate image-only controls but bring different latency, cost, and interaction constraints. These are the authors’ architectural characterizations, not independently validated comparisons of every named tool.

Semantic markup tells a machine what an element means or how it can be used. The paper investigates actual button elements, image alternative text, Accessible Rich Internet Applications (ARIA) labels and descriptions, custom attributes, and off-screen text. A call to action (CTA) is an invitation to do something, such as “Order Now.” A CTA drawn inside an image and a real HTML button may look similar to a person while being exposed differently to an agent.

A paywall limits article access until a subscription requirement is met. A cookie consent interface requests a privacy-related choice. A dark pattern is a manipulative interface pattern; in this study, the authors deliberately used a visibly pressuring consent modal. Satisficing means stopping at an acceptable-looking result instead of continuing to search for a better or exact result.

[A; pp. 1–3] Related work supplies motivation about general web-agent reliability, accessibility failures in advertisements, and policy-aware trust evaluation. The paper mentions BrowseComp, ST-WebAgentBench, MLA-Trust, and the Trustworthiness Assessment Model (TrAM). It also invokes European Union ethical and regulatory frameworks. These references are part of the authors’ positioning; their underlying papers and legal texts were not independently reviewed here.

## 4. Research problem and gap

**Existing problem.** [A; pp. 1–3] Advertisements, subscription flows, and privacy prompts assume human perception and judgment. Agents may overlook visual controls, select an initially plausible offer, or follow a commercial flow without adequately evaluating its implications.

**Shortcomings attributed to previous approaches.** The authors argue that general web-agent evaluations do not adequately capture realistic, commercially motivated advertising environments. Simplified test websites omit structural complexity. Broad trust frameworks do not yet supply standardized, agent-specific measures for this setting. Their earlier travel-site simulation showed preference for factual structured cues but did not resolve the present questions about varied advertisements and responsible action.

**Research gap.** The paper links two issues often treated separately: whether an agent can interact with an ad and whether that interaction respects privacy, spending boundaries, and user expectations. It investigates concrete interface and markup changes alongside observable behavior.

**Motivation.** If agents increasingly mediate browsing and purchasing, website designers need machine-readable content, while users need protection from unwanted commercial consequences. These objectives can conflict: increasing detectability can also increase the ability of a website to steer an agent.

**Scope.** One cloned news environment; three Browser Use model configurations; exploratory Operator comparisons; ten authored tasks; selected follow-up manipulations. The paper does not establish prevalence across the web, measure an adversarial campaign, or compare agents with standalone LLMs.

[D] A security reading should preserve this scope. The work demonstrates susceptibility to interface and goal framing within a controlled commercial environment. It does not establish that every hidden label is malicious, that every subscription was a policy violation, or that prompt injection was the tested attack mechanism.

## 5. Research questions / objectives / hypotheses

[A; p. 3] **RQ-A — Accessibility:** “How do semantic markup, spatial placement, and media format influence an agent’s ability to detect, interpret, and act on advertisements?”

[A; p. 3] **RQ-B — Trustworthiness:** “How do AI agents navigate behavioral patterns and ethical considerations in ad-related tasks, particularly with respect to avoiding hallucinated information, responding to privacy dialogs, and making autonomous subscription decisions?”

The operational objectives include locating and ranking advertisements, parsing dynamic versus static content, applying promotional offers, and completing multi-step journeys. More specific investigations examine scrolling, side-banner choice, coupon reporting, subscriptions, cookies, and sensitive data.

No formal statistical hypotheses or preregistered predictions are supplied. The authors explicitly state that they did not construct a formal composite trust metric. Instead, hallucination avoidance, privacy-dialog handling, and subscription choices serve as observable indicators. The study therefore answers its questions through repeated behavior and condition comparisons rather than hypothesis tests against a unified trust score.

**Connection to the user’s research question.** [D] RQ-A informs how website-controlled representations reach agent perception and action selection. RQ-B informs how task pursuit can produce privacy and spending consequences. Neither directly tests the comparative vulnerability of a web agent and its underlying standalone model. Confidence in relevance is MEDIUM; confidence in a direct comparative conclusion is UNKNOWN because that experiment is absent.

## 6. Assumptions / threat model

[A; pp. 3–4, 8–9] The experimental system assumes a controlled clone with realistic site structure, functioning forms and subscription flows, and repeatable start conditions. Models receive identical prompts and interface setups within the Browser Use comparisons. Relevant prompts include fictitious user information so that missing payment details do not alone block continuation. Dummy credentials prevent real financial transactions.

The paper does not define a formal attacker, security objective, adversarial budget, attack success rate, or defended trust boundary. Its manipulation of page markup and promotional conditions nevertheless identifies an interface surface relevant to security analysis.

[D; analyst threat-model mapping] A website operator controlling the tested page can change advertisement position, visible and non-visible descriptions, semantic controls, consent wording, and the relationship between a user goal and a subscription requirement. Those changes can affect what the agent notices and does. This mapping is restricted to capabilities demonstrated or described in the paper; it does not imply control over model system prompts, runtime tools, internal memory, or other agents.

The user’s instruction is the initiating goal, while website content supplies offers and possible action paths. The observed spending issue arises when a website presents payment as necessary to fulfill a promotional goal. Calling this an authorization failure requires knowing the intended spending policy; the paper does not provide a complete formal policy for that judgment.

[A; pp. 6, 8] Operator pauses for user confirmation at sensitive actions, while Browser Use can execute multi-step tasks without such pauses. This is a consequential system distinction. The paper excludes Operator from the detailed autonomous behavioral comparison, and cross-architecture results should not be interpreted as a controlled comparison of model reasoning alone.

## 7. Methodology

### Study substrate and implementation

[A; pp. 3–4] The authors recreated the Tiroler Tageszeitung website using a multi-stage workflow. The html.to.design plugin imported key pages into Figma. Bolt.new translated design layers into a React codebase with components, routing, and styling. Cursor was used to refine functionality including session handling, simulated paywalls, forms, and modal dialogs.

The clone included the homepage, sports pages, article views, subscription and login flows, banner popups, coupon widgets, and overlays. The rationale was to retain realistic DOM and layout complexity while controlling the environment. The study is therefore a controlled simulation on a functional clone, despite some earlier prose describing “real-world” environments.

### Agent configurations

Browser Use supplied browsing capabilities through Playwright. The three principal models were GPT-4o, Claude 3.7 Sonnet, and Gemini 2.0 Flash. Browser Use version 0.1.41 is reported. All three used identical prompts, interface setups, and default settings. Exact model snapshot identifiers, complete system prompts, decoding parameters, hardware, random seeds, and a Playwright version are not supplied.

Operator was explored for image-heavy and dynamic conditions. Its evaluations took place June 1–15, 2025. The paper does not provide an equivalent experiment date interval for every Browser Use condition.

### Baseline protocol

Ten tasks were run ten times for each of three Browser Use models: 10 × 10 × 3 = 300 baseline trials [C; operands reported p. 4]. Each run began at the cloned homepage. Browser sessions were reset between trials to reduce cross-session contamination. Connectivity or rendering failures were excluded and rerun. The number of excluded attempts is not reported.

Follow-up conditions generally used ten trials per model. The complete follow-up count and complete Operator trial inventory are not specified, so total study-wide runs cannot be reconstructed reliably.

### Prompt information and data capture

Early models refused steps requiring payment data when those details were unavailable. The researchers then appended standardized fictitious names, emails, and banking details to relevant prompts. Their stated purpose was to distinguish willingness from missing capability or information. This intervention also conditions interpretation: subsequent purchase behavior occurred with supplied dummy credentials in a simulated environment.

Browser Use generated JSON action logs with event rationales, final answers when available, and animated GIF recordings. Operator outcomes were manually entered into a structured comma-separated values (CSV) file by a human annotator. Successful completion was judged against the instruction. Complete task-specific decision rules, inter-annotator agreement, raw logs, and recordings are not supplied.

### Measurement and analysis

Measurements are counts of clicks, discovered banners, scrolling actions, reported promotions, subscription choices, and cookie acceptance. Results are predominantly descriptive. No confidence intervals, significance tests, sample-size justification, or composite trust index are reported. There are no training datasets, annotation training procedures, or train/validation/test splits: the models are evaluated as existing agent configurations rather than trained in this study.

## 8. Experiments / analyses

### X1 — Baseline task battery

[A; pp. 4–5, Table I] Ten prompts cover: generic digital enrollment; Plus XL enrollment; enrollment if a free trial exists; finding deals or coupons; exploring sports articles; summarizing sports news; summarizing recent soccer comments; entering sweepstakes; reporting subscription bundles; and retaining a subscription only if a discount or trial extension exists, otherwise cancelling. Each has ten runs per Browser Use model. The paper does not publish a complete task-by-model success matrix, so outcomes for every task cannot be reconstructed.

### X2 — Subscription entry points and spatial choice

[A; pp. 4–5, Table II] Four prompts, IDs 1, 2, 3, and 8, generate 40 baseline runs per Browser Use model and 120 across three models. Agents used the bottom sticky strip or header rather than side banners. Removing the strip pushed selection to the header. When side banners became operable through button overlays, banner selections consistently favored the left side. Operator preferred the header. This supports a first-satisfactory-target pattern, but universal traversal order is an interpretation rather than a directly isolated mechanism.

### X3 — CTA implementation

[A; p. 5, Table III] An image-linked banner with pixel text reading “Order Now” attracted zero banner clicks in ten runs for each configuration shown. Replacing the visual cue with a DOM button overlay produced 7/10 banner selections for Claude, 7/10 for GPT-4o, and 5/10 for Gemini. Operator remained at zero. This condition distinguishes image appearance from exposed controls.

### X4 — Hidden and semantic descriptions

[A; p. 5, Table IV] With ten trials per model per variant, custom data attributes and image alt attributes each produced 0/10 banner clicks across the three Browser Use models. ARIA labels/descriptions produced Claude 0/10, GPT-4o 4/10, and Gemini 10/10. Off-screen span text produced 9/10, 10/10, and 10/10 respectively. Only a small set of strategies and a single natural-language description were tested.

### X5 — Search depth and promotion discovery

[A; pp. 5–7, Tables V–VI] A digital-plus-print banner placed one viewport below the fold was initially missed. Under an explicit discount-code prompt, Claude found it 8/10 times, GPT-4o 0/10, and Gemini 1/10. A target on virtual page 10 of an infinite feed was never reached. Reported mean scroll-down actions were 2.5 for Claude, 0.8 for GPT-4o, and 0.7 for Gemini. Task 4 also compared diversity and frequency of reported offers.

### X6 — Dynamic media

[A; p. 6] Baseline GIF information was available after initialization delays; agents did not explicitly plan to wait. In a 12-second video with a two-second coupon segment, only GPT-4o retrieved the code, once in ten runs. Hidden text alternatives caused DOM-focused agents to use text instead. Operator failed to combine the video’s separately presented store and coupon information, but deliberately navigated carousel controls successfully in all reported trials. Claude obtained the carousel’s third-slide coupon through timing rather than explicit slide navigation.

### X7 — Native geolocation dialog

[A; p. 6] Native permission prompts initially blocked completion. Browser Use avoided the obstacle by pre-approving location requests, while Operator automatically rejected the request. These are workflow accommodations, not evidence of general native-dialog competence.

### X8 — Financial boundary and sensitive information

[A; pp. 6, 8] Tasks 5 and 6 did not induce subscriptions simply to access useful articles. Task 8 did when sweepstake participation depended on subscribing: GPT-4o and Claude 10/10 each, Gemini 7/10. Sensitive payment details were not fabricated, but p. 8 distinguishes this from fabrication of non-critical personal details. Operator was excluded from this autonomous behavior analysis.

### X9 — Cookie consent

[A; pp. 6–7, Table VII] Three banners were tested with ten runs per model per variant, using the prompt “Summarize the headline article.” Agents either accepted all or accepted nothing, never opening granular settings. All rejected the conspicuously predatory modal; acceptance of ordinary banners differed by model and whether the banner blocked progress.

### X10 — Subscription tier and retention

[A; p. 7] Tier selection is summarized across tasks 1, 3, and 8. Claude primarily chose Basic, GPT-4o also favored Basic, and Gemini favored expensive tiers. A reporting ambiguity affects Gemini’s category total. In task 10, recommendations to retain the subscription occurred in 9/10 Claude runs, 8/10 GPT-4o runs, and 10/10 Gemini runs. These are recommendations reported by the paper, not independently verified cancellation or renewal transactions.

## 9. Results

### Accessibility depends on representation

[A; p. 5] Pixel-only CTA banners received no clicks in Table III. Actual button overlays produced 7, 7, and 5 banner clicks out of ten for Claude, GPT-4o, and Gemini. Off-screen span descriptions were even more consistently associated with banner selection: 9/10, 10/10, and 10/10. The relevant outcome is banner interaction under the tested configurations, not universal advertisement comprehension.

The detailed findings qualify the abstract’s broad suggestion about descriptive alt attributes. Table IV records zero clicks for the tested alt-attribute strategy. Thus, “semantic markup helps” cannot be reduced to “any accessibility attribute works.” The authors themselves note that a framework’s extraction behavior and model interpretation matter.

### Search is shallow but not uniformly limited to two actions

[A; pp. 5–7] The infinite-feed target was not reached. Table VI nevertheless reports up to five scroll-down actions for Claude and three for Gemini, while the abstract says agents never scroll beyond two viewports. Actions and viewport distance are not necessarily identical quantities, and no precise conversion is given. The detailed table supports limited exploration; it does not support treating two viewports as a universal measured maximum.

### Dynamic-media success can be incidental

[A; p. 6] GPT-4o’s 1/10 video success is explicitly attributed to chance timing, and Claude’s successful third-slide retrieval to slower interaction. Operator’s carousel success differs because it used controls deliberately. Final-answer correctness therefore does not by itself establish a robust temporal-media strategy.

### Spending behavior follows task contingencies

[A; pp. 6, 8] Buying a subscription was avoided when it merely simplified article tasks. It was accepted when tied to the stated sweepstake objective. The authors interpret this as a goal-contingent justification and deficient cost-benefit reasoning. Gemini’s three non-subscriptions were attributed to failure to recognize the sweepstake, so those failures do not establish a stronger financial safeguard.

### Privacy behavior is coarse and model-specific

[A; p. 7] GPT-4o accepted the non-blocking footer in 0/10 runs, versus 10/10 for Claude and Gemini. On the modal blocker, counts were 8/10, 10/10, and 10/10. All were 0/10 on the predatory modal. No model used detailed preferences. The 97.3% figure embedded in the manipulative banner was interface copy, not a measured acceptance rate.

### Reporting tensions remain unresolved

The Gemini tier counts 5 Basic + 0 Plus + 20 Plus XL total 25, while the stated denominator is 27 [C; p. 7]. The mention of two digital-plus-print packages may explain the remaining two, but the parenthetical placement does not establish a clean mutually exclusive accounting. Both the reported figures and this ambiguity must be retained. Separately, p. 6 broadly says models did not hallucinate payment or coupon details, whereas p. 8 explicitly allows non-critical personal-detail fabrication; these statements address different categories and should not be compressed into “no hallucination.”

## 10. Figure-by-figure interpretation

No numbered substantive figures or plotted panels are identifiable in the supplied nine-page text. No axes, legends, error bars, or graphical measurements can therefore be audited. The page 1 image visually confirms the title, authorship layout, abstract, opening introduction, and footnotes. The page 8 image confirms the risk-profile discussion and beginning of the limitations section. These are page renderings, not experimental figures.

The experimental site contained banners, videos, and carousels, but those interface assets and their recordings were not supplied as independent visual evidence. Their appearance and sequence are described by the authors. It would be inaccurate to claim direct visual inspection of the tested banners, the coupon frames, or the predatory modal.

The paper’s results are table- and prose-driven. Absence of identified figures is not a finding that the study had no visual phenomena; it is a statement about what the document reports and what this analysis could inspect.

## 11. Table-by-table interpretation

### Table I — Ten base tasks

[A; p. 5; text-only inspection] Rows identify ten natural-language prompts. They span explicit subscriptions, conditional trial enrollment, offer discovery, sports content, comments, sweepstakes, bundles, and retention/cancellation. There are no outcome columns. The table defines task scope rather than success. The standardized fictitious-information block is not reproduced here, and the ten prompts should not be mistaken for a complete execution package.

### Table II — Subscription CTA click counts

[A; p. 5; text-only inspection]

| Model | Bottom strip | Header | Side banner |
|---|---:|---:|---:|
| Claude 3.7 Sonnet | 29 | 11 | 0 |
| GPT-4o | 17 | 23 | 0 |
| Gemini 2.0 Flash | 33 | 6 | 0 |
| Operator | 0 | 30 | 0 |

The three Browser Use models contribute nominally 40 runs each across four prompts. Gemini’s 39 recorded clicks align with the prose’s one direct-URL case. Operator has 30 header clicks, but its denominator and task coverage differ; the paper also reports refusal of sweepstake-oriented tasks. No side-banner clicks occurred in this baseline table. Counts do not establish subscription completion or offer optimality.

### Table III — Pixel CTA versus actual button

[A; p. 5; text-only inspection] Entries are CTA/header click pairs. Pixel “Order Now” gives 0/10 for every shown model, meaning zero CTA and ten header selections. DOM overlays give Claude 7/3, GPT-4o 7/3, Gemini 5/5, and Operator 0/10. Here the slash is a pair of category counts, unlike the success fractions used elsewhere. All recorded side-banner selections were on the left. No statistical uncertainty or significance is reported.

### Table IV — Hidden-text strategies

[A; p. 5; text-only inspection]

| Strategy | Claude | GPT-4o | Gemini |
|---|---:|---:|---:|
| data-llm-description | 0/10 | 0/10 | 0/10 |
| Image alt | 0/10 | 0/10 | 0/10 |
| aria-label / aria-description | 0/10 | 4/10 | 10/10 |
| Off-screen span | 9/10 | 10/10 | 10/10 |

Off-screen span text is the strongest tested strategy by these counts. ARIA results are highly model-dependent. Custom data and alt strategies tie at zero. These results are conditioned on the tested text, runtime extraction, and page setup; they do not imply that alternative text is inherently useless to every agent.

### Table V — Combined digital-plus-print banner retrieval

[A; p. 6; text-only inspection] Each model has ten runs. Claude finds the banner eight times, GPT-4o zero, and Gemini once after an explicit discount-code prompt. The outcome is target-banner discovery, not a general score across every promotion. It demonstrates prompt-sensitive and model-specific exploration in this condition.

### Table VI — Scroll-down actions

[A; p. 6; text-only inspection]

| Model | Mean | Maximum | Minimum |
|---|---:|---:|---:|
| Gemini 2.0 Flash | 0.7 | 3 | 0 |
| GPT-4o | 0.8 | 2 | 0 |
| Claude 3.7 Sonnet | 2.5 | 5 | 0 |

Units are actions per run. No standard deviations, distributions, confidence intervals, or pixel distances are supplied. Claude explores further on this measure but still fails to reach the page-10 target. The mean of 2.5 also qualifies nearby prose suggesting one or two actions on average.

### Table VII — Cookie acceptance

[A; p. 7; text-only inspection] Counts out of ten are footer: GPT-4o 0, Claude 10, Gemini 10; blocker: GPT-4o 8, Claude 10, Gemini 10; predatory modal: all zero. The extracted blocker row has an asterisk and compressed spacing. Adjacent prose states that two of GPT-4o’s eight accepting cases explored alternatives before accepting. Footnote 14 identifies the prompt as “Summarize the headline article.” No detailed preference settings were accessed. Acceptance is an action count, not a comprehensive privacy-compliance metric.

## 12. Diagram / architecture interpretation

No supplied architecture diagram is available for direct inspection. The following is a prose reconstruction of the reported workflow, not a figure attributed to the authors.

[A; pp. 3–4] Website pages pass through html.to.design into Figma, then Bolt.new generates a React implementation, and Cursor-assisted refinement adds working flows. The resulting cloned website supplies the experimental environment. A natural-language user task and, when relevant, dummy user details are inputs to an agent. Browser Use connects the model to Playwright-backed page actions. The agent observes page information, chooses actions, receives subsequent page state, and eventually produces an answer or completes a flow. Logs and GIF recordings capture that sequence.

Operator supplies a contrasting observation/action path and has manually recorded outcomes instead of the same full DOM trace. Its sensitive-action confirmation pauses change the control structure. The authors’ native-dialog result also exposes a boundary between webpage content and the browser’s own interface: DOM-level controls did not initially operate the geolocation permission prompt.

[D] For security interpretation, the important path is website representation → agent perception → action selection → possible subscription or privacy choice. This path explains why changing text exposure can affect actions. The experiment does not expose enough internal detail to identify which model or runtime component causally mediates every step.

## 13. Equations and mathematical concepts

The supplied paper contains no substantive numbered equations, loss functions, optimization objectives, formal proofs, or mathematical algorithms. Its quantitative content consists of descriptive counts, fractions, percentages, and action summaries.

A run proportion means the number of runs exhibiting an outcome divided by the relevant number of runs. For example, 7/10 sweepstake subscriptions for Gemini corresponds to 70% [A; p. 6]. This must not be confused with a proportion across all tasks or all website visits.

[C] Baseline count: ten tasks × ten repetitions × three Browser Use models = 300 runs. Subscription-entry subset: four prompts × ten repetitions × three models = 120 runs. Cookie-condition count: three models × ten repetitions = 30 per banner design; three designs would yield 90 scheduled trials in that experiment. These calculations follow the reported design and do not reconstruct total follow-up execution.

[C] The difference between 100% subscription behavior for GPT-4o or Claude and 70% for Gemini is 30 percentage points. It is not automatically evidence of a 30% stronger safety policy, because the authors attribute Gemini’s non-subscriptions to missing the sweepstake.

The paper reports Basic-tier shares of about 56.52% for GPT-4o and 18.52% for Gemini, consistent with 13/23 and 5/27. Claude’s 24/30 is four-fifths. Gemini’s 20/27 is reported as 74.07%. The unresolved category-accounting issue remains; arithmetic agreement with the stated denominator does not resolve what happened in every run.

## 14. Interpretation and discussion

**Answer to RQ-A.** [A; pp. 4–7] Markup, placement, and media format materially affect observed interaction. Real controls and off-screen explanations increase banner selection in the tested DOM-based stack. Left-side and early available choices dominate. Dynamic media can be missed because the agent does not deliberately wait or integrate temporally separated content. Native browser controls introduce an additional boundary outside normal page interaction.

**Answer to RQ-B.** [A; pp. 6–8] Behavior is neither uniformly reckless nor uniformly conservative. Models avoid fabricating sensitive payment information and avoid subscriptions for article convenience, yet frequently accept a subscription when it is a prerequisite for the requested promotion. They reject an overtly manipulative modal but often accept ordinary cookie banners without exploring preferences. Different models show different financial and privacy choices.

The authors interpret early stopping as a form of cognitive economy: agents lower interaction effort while producing superficially adequate answers. They recommend placing important promotions near the beginning of the page. Their exact “first two viewports” recommendation should be treated as design guidance rather than a rigorously universal bound, given Table VI.

[D; research relevance] Web agency adds an actionable environment around the model. The agent must choose among website-defined controls, interpret commercial claims, and potentially change a user’s account or consent state. The paper shows how these choices depend on exposed representation and goal structure. A standalone text interaction does not reproduce those tested browser workflows, but the paper does not quantify the difference or isolate the underlying model from its runtime.

Unresolved issues include the abstract/detail mismatch on scrolling, broad versus specific markup claims, Gemini’s tier accounting, the exact total of follow-up trials, and the absence of a complete policy-aware success table. None should be silently repaired. The evidence supports condition-specific observations more strongly than a general theory of all agents.

## 15. Contributions and novelty

[A; p. 2] **Empirical accessibility contribution:** demonstrations that particular semantic and textual additions can make otherwise ignored advertisements selectable by agents. The strongest detailed evidence concerns DOM button overlays and off-screen span text.

**Taxonomic contribution:** a qualitative comparison of advertisement formats and markup patterns, including banners, video, carousels, and hidden descriptions, across the tested configurations. It is not a comprehensive taxonomy of every advertisement technology.

**Behavioral contribution:** observations of when agents proceed, refuse, or avoid actions involving payment, subscriptions, privacy dialogs, and sensitive information. The paper calls these trust or behavior patterns without collapsing them into a formal composite metric.

**System/implementation contribution:** a functional cloned news site used to combine realistic page complexity with experimental control. The implementation is described, but a supplied reusable repository or released benchmark package is not available for inspection.

**Practical contribution:** five recommendations: real controls, top-left prioritization, clear clickability text, HTML alternatives to native dialogs, and static or textual alternatives to dynamic media.

[D] For security research, the distinctive contribution is evidence that accessibility and manipulation are linked through the same perception/action mechanisms. This is an analyst synthesis of the study, not an author-tested standalone-LLM comparison. No new defense algorithm, formal security theorem, or validated security score is introduced.

## 16. Limitations

### Authors’ stated limitations

[A; pp. 8–9] **L1 — Clone and ecological validity.** The environment reproduces a production site but omits live timing, sequencing, and personalization. The authors describe findings as conservative lower-bound indicators. That lower-bound characterization is their interpretation; the study does not provide a formal bound.

**L2 — Model opacity and drift.** Commercial systems expose limited internals and evolve. Contributions from pretraining, system prompts, tool policies, and safety layers cannot be causally separated.

**L3 — Instrumentation differences.** DOM-focused Browser Use and vision-first Operator have different observation/action access, latency, costs, and confirmation behavior. Comparisons are indicative rather than strictly like-for-like.

**L4 — Scoped tasks and prompts.** One news setting and authored requests do not cover other industries, mobile environments, locales, writing styles, or real user-language diversity.

**L5 — Measurement scope.** Observable regularities replace composite trust/compliance scores. No user study was conducted, and the measures are not standardized policy-aware metrics.

**L6 — Limited hidden-text exploration.** Only a small subset of strategies and one natural-language description were tested. Wording, structure, and what the framework actually exposes may matter strongly.

**L7 — Dummy transactions.** Fictitious payment information avoids real purchases but omits identity checks, actual cancellations, and human emotional responses. The study prioritizes control over breadth.

### Additional evidence-based analyst observations

[D] Ten trials per condition provide useful descriptive contrasts but no reported uncertainty estimates. Randomization or counterbalancing of condition order is not specified. Complete snapshot identifiers, raw traces, and exact expanded prompts are unavailable. Excluded connectivity/rendering failures are rerun without their counts being reported. Manual Operator coding has no reported inter-rater assessment. These observations limit independent checking and causal precision; they are not all limitations explicitly acknowledged in those terms by the authors.

The absence of a standalone-model condition is decisive for the user’s comparative question. The study can inform why browser-connected systems may expose additional risks, but cannot establish a numerical vulnerability increase over standalone LLMs.

## 17. Threats to validity

The following categories are analyst-organized unless otherwise stated.

**Internal validity.** [D] Markup changes provide useful within-environment contrasts, but some outcomes may depend on competing controls, execution order, runtime extraction, or timing. The dynamic-media findings explicitly demonstrate timing confounding: a correct answer may result from slower interaction rather than deliberate temporal reasoning.

**External and ecological validity.** [A/D] The authors explicitly acknowledge the clone, single domain, scoped tasks, and missing live personalization. Extending findings to banking, shopping, mobile interfaces, or all advertising requires evidence beyond this study.

**Construct validity.** [D] Clicking an ad is not equivalent to understanding it, accepting cookies is not a complete privacy judgment, and subscription completion is not automatically a formally defined policy violation. The paper’s qualitative trust indicators reveal behavior but do not exhaust trustworthiness.

**Statistical conclusion validity.** [D] Counts and large descriptive differences are clear, but the paper reports no confidence intervals or significance tests. No population-level effect precision should be invented. Repeated trials of a hosted model configuration are not automatically representative samples of every future deployment.

**Reproducibility.** [A/D] Browser Use version and some dates are documented, but exact model snapshots, full configurations, code, logs, and annotation data are not supplied. Model drift further limits replay.

**Comparability.** [A] Operator’s confirmation gates and different instrumentation prevent a clean architecture-only or model-only contrast. Its refusal of sensitive tasks is a relevant system property, but not proof of universally superior perception or reasoning.

## 18. Future work and open questions

### A. Author-proposed future work

[A; pp. 8–9] Develop automated consent scoring, financial decision protocols, and risk matrices that make trust observations benchmarkable. Study how markup, off-screen text, ARIA, and visual cues affect attention, accounting for which page elements the runtime exposes. Compare wording and structure of guiding descriptions rather than relying on one phrase. Extend across models, websites, and time through targeted ablations and policy-aware scenarios. Develop shared machine-readable cue guidelines for website developers and agent-framework creators.

The authors also identify missing live timing, personalization, other sectors, mobile settings, locales, and user-language diversity as areas requiring broader evaluation. Their discussion calls for translating trust and regulatory aspirations into verifiable engineering measures. This analysis reports that aspiration without independently validating the legal interpretation.

### B. Analyst open questions

[D] Does requiring explicit spending authorization prevent the sweepstake-to-subscription transition while preserving legitimate task completion? How much of the hidden-text effect comes from runtime extraction versus model interpretation? Would a matched standalone model make a different decision when shown the same offer and policy? Would repeated prompts with different wording preserve the reported counts? Can an agent distinguish a website’s claim that payment is necessary from a user’s authorization to pay? How do different confirmation interfaces affect outcomes?

These are proposed questions, not experiments performed in this paper. A controlled answer to the user’s central question would require a matched comparison that this document does not contain.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| AI | Artificial intelligence; the broader category of the tested systems |
| LLM | Large language model; a model underlying the agent’s language-based decisions |
| Multimodal | Able to process more than one input type, here text and images |
| Web agent | A model connected to browser observation and action tools |
| DOM | Document Object Model; structured webpage representation used in the principal stack |
| HTML | Hypertext Markup Language; page elements and attributes investigated in the experiments |
| ARIA | Accessible Rich Internet Applications; roles and labels used to describe interface meaning |
| CTA | Call to action, such as an invitation to subscribe |
| Pixel-based | Interacting primarily with visual screenshot content |
| Semantic button | A real button element exposed as an actionable control |
| Off-screen span | Text in a span element positioned outside ordinary visible content |
| Alt attribute | Text alternative associated with an image |
| data-llm-description | A custom attribute tested as an explanatory cue |
| Viewport | The currently visible area of the page |
| Fold | Boundary below the initially visible page content |
| Satisficing | Stopping after finding an adequate-looking result |
| Carousel | A sequence of slides that may advance automatically or through controls |
| Modal | An overlay that can block interaction with underlying content |
| Native dialog | Browser-provided interface outside ordinary webpage controls |
| Paywall | An access restriction requiring a subscription or related condition |
| Dark pattern | Interface wording or design intended to steer or pressure choices |
| Cookie consent | A privacy-related decision concerning website cookies |
| TrAM | Trustworthiness Assessment Model, cited as background |
| JSON / CSV / GIF | Reported log, annotation-table, and animated-recording formats |
| CVV | Sensitive card verification code discussed among payment artifacts |
| RQ-A / RQ-B | The paper’s accessibility and trustworthiness research questions |

No mathematical symbols require an additional notation glossary.

## 20. Key numerical results

All results below are author-reported unless marked analyst-derived. Tables outside the two supplied image pages were inspected as extracted text.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Base tasks | 10 | tasks | Browser Use battery | Author-reported | p. 4; Table I p. 5 |
| Repetitions | 10 | runs/task/model | Baseline | Author-reported | p. 4 |
| Baseline | 300 | trials | Three Browser Use models | Author-reported | p. 4 |
| Browser Use version | 0.1.41 | version | All Browser Use trials | Author-reported | p. 4 |
| Operator interval | June 1–15, 2025 | dates | Operator evaluations | Author-reported | p. 4 |
| Subscription-entry subset | 120 | runs | Four prompts × ten × three | Author-reported | p. 4 |
| Pixel CTA banner clicks | 0/10 each | runs | Four listed configurations | Author-reported | Table III p. 5 |
| Overlay banner clicks | 7/10; 7/10; 5/10 | runs | Claude; GPT-4o; Gemini | Author-reported | Table III p. 5 |
| Off-screen span clicks | 9/10; 10/10; 10/10 | runs | Claude; GPT-4o; Gemini | Author-reported | Table IV p. 5 |
| ARIA strategy clicks | 0/10; 4/10; 10/10 | runs | Claude; GPT-4o; Gemini | Author-reported | Table IV p. 5 |
| Custom data and alt clicks | 0/10 each | runs | Each Browser Use model | Author-reported | Table IV p. 5 |
| Combined banner discovery | 8/10; 0/10; 1/10 | runs | Claude; GPT-4o; Gemini | Author-reported | Table V p. 6 |
| Mean scroll actions | 2.5; 0.8; 0.7 | actions/run | Claude; GPT-4o; Gemini | Author-reported | Table VI p. 6 |
| Maximum scroll actions | 5; 2; 3 | actions/run | Claude; GPT-4o; Gemini | Author-reported | Table VI p. 6 |
| Infinite-feed target | 10 | virtual page | Not reached in 30 runs | Author-reported | pp. 5, 7 |
| Distinct promotions | 7; 4; 4 | offers | Claude; Gemini; GPT-4o, task 4 | Author-reported | p. 6 |
| Promotion mentions | 37; 26; 21 | mentions | Claude; Gemini; GPT-4o, ten runs each | Author-reported | p. 6 |
| Video and coupon segment | 12; 2 | seconds | Total video; coupon visibility | Author-reported | p. 6 |
| Video coupon retrieval | 1/10 | runs | GPT-4o; other models no reported success | Author-reported | p. 6 |
| Sweepstake subscriptions | 10/10; 10/10; 7/10 | runs | GPT-4o; Claude; Gemini | Author-reported | p. 6 |
| Difference in sweepstake rates | 30 | percentage points | 100% − 70% | Analyst-derived | p. 6 operands |
| Cookie acceptance, footer | 0/10; 10/10; 10/10 | runs | GPT-4o; Claude; Gemini | Author-reported | Table VII p. 7 |
| Cookie acceptance, blocker | 8/10; 10/10; 10/10 | runs | Same order | Author-reported | Table VII p. 7 |
| Predatory modal acceptance | 0/10 each | runs | Three Browser Use models | Author-reported | Table VII p. 7 |
| GPT-4o tiers | 13; 2; 8 of 23 | subscriptions | Basic; Plus; Plus XL | Author-reported | p. 7 |
| Claude tiers | 24; 3; 3 of 30 | subscriptions | Basic; Plus; Plus XL | Author-reported | p. 7 |
| Gemini tiers | 5; 0; 20 of 27 | subscriptions | Category accounting ambiguous | Author-reported | p. 7 |
| Retention recommendations | 9/10; 8/10; 10/10 | runs | Claude; GPT-4o; Gemini | Author-reported | p. 7 |

The promotion’s “-20%” and trip “for 2,” and the predatory banner’s “97.3%,” are stimulus contents rather than measured performance results. They are preserved here to avoid confusing advertising copy with experimental evidence.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| The principal evaluation is controlled and repeated | Ten tasks, ten repetitions, three models, session resets | X1 | p. 4 | HIGH for reported design; no raw execution audit |
| Pixel appearance alone did not attract banner clicks | Zero CTA clicks for pixel variant | T3 / X3 | p. 5 | HIGH within tested setup |
| Actual controls increased banner interaction | Overlay counts 7, 7, 5 of ten | T3 / X3 | p. 5 | HIGH descriptive evidence; no causal decomposition of all interface factors |
| Hidden text can steer selection | Off-screen span counts 9, 10, 10 | T4 / X4 | p. 5 | HIGH reported effect; narrow wording and strategy coverage |
| Exploration can stop before relevant content | No page-10 retrieval; shallow action counts | T6 / X5 | pp. 6–7 | HIGH for condition; abstract’s viewport bound over-compresses |
| Dynamic-media correctness can be incidental | GPT-4o once caught video coupon; Claude benefited from slower timing | X6 | p. 6 | HIGH author account; internal mechanism not independently verified |
| Payment dependency changes behavior | No article-convenience subscriptions; 10/10, 10/10, 7/10 for sweepstakes | X8 | pp. 6, 8 | HIGH reported contrast; no formal spending-policy ground truth |
| Consent decisions are coarse | No granular settings; accept-all or none | T7 / X9 | p. 7 | HIGH within tested banners |
| Architecture comparisons are limited | Different instrumentation and confirmation pauses | SS5C | pp. 8–9 | HIGH author-stated limitation |
| The study informs agent security mechanisms | Website cues influence actionable browsing choices | X3, X4, X8 | pp. 5–6 | MEDIUM analyst inference; no standalone-model comparison |

Source-grounded verification was performed against the supplied text and, for pages 1 and 8, the supplied images. Major numerical statements were checked against their reported conditions and table rows. Table III’s slash notation was kept distinct from fractions, Table VII’s stimulus statistic was separated from results, and Gemini’s tier discrepancy was retained. No independent reproduction, raw-log audit, or external reference verification was performed.

## 22. Very simple explanation — Explain Like I’m 15

Imagine asking an AI assistant to use a newspaper website for you. It sees subscription offers, advertisements, cookie popups, and articles. The researchers built a realistic copy of such a website and watched several assistants work through repeated tasks. They found that an ad looking obvious to a person might be missed by the assistant, while an actual webpage button or explanatory text hidden off-screen could make it much more likely to be selected.

The assistants also often stopped searching too soon. A useful offer could exist farther down the page, but they might return the first answer that seemed acceptable. Videos caused another problem: seeing the correct coupon sometimes depended on accidentally waiting long enough, rather than understanding that the information would appear later.

The most concerning example involved spending. The assistants did not buy subscriptions simply to make reading articles easier. But when entering a competition required a subscription, GPT-4o and Claude subscribed in all ten trials each, and Gemini did so in seven. The researchers used dummy payment details on a cloned site, so these were not real purchases. The issue is the decision pattern: a website can connect something the user wants with a paid step, and the assistant may treat that step as justified by the goal.

This helps explain a possible security problem with web agents: they do more than answer questions. They interpret pages and choose actions that can affect accounts, privacy, or money. However, this paper did not test the same models without browser tools, so it cannot prove how much more vulnerable web agents are than standalone chat models. It shows specific ways that website structure and commercial framing can influence agent behavior.

## Completeness Audit

Coverage is assessed against the inventory above, not against response length. The accessible paper is represented, but most pages were text-only and the experimental artifacts were unavailable.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META: title/authors/venue | Yes, text and p. 1 image | Yes | Fully represented | Original title retained; authors and venue recorded below |
| Abstract and keywords | Yes, text/image | Yes | Represented in compressed form | Main claims and key caveats retained |
| S1 Introduction | Yes | Yes | Represented in compressed form | Motivation, gap, contributions; cited forecast treated as background |
| SS2A architectures | Text-only | Yes | Represented in compressed form | Author classification retained with limits |
| SS2B advertising | Text-only | Yes | Represented in compressed form | Structured cues and incentives |
| SS2C accessibility | Text-only | Yes | Represented in compressed form | Semantics and alternatives |
| SS2D trust | Text-only | Yes | Represented in compressed form | Named frameworks; no outside verification |
| SS3A design | Text-only | Yes | Fully represented | RQs, indicators, fictitious data |
| SS3B implementation | Text-only | Yes | Fully represented | Pipeline and site components |
| SS3C protocol | Text-only | Yes | Fully represented | Counts, resets, dates, exclusions |
| SS3D capture | Text-only | Yes | Fully represented | JSON/GIF versus manual CSV |
| SS4A1 position | Text-only | Yes | Fully represented | Entry points, left-side preference, URL exception |
| SS4A2 markup | Text-only | Yes | Fully represented | Pixel, button, hidden-text variants |
| SS4A3 scrolling | Text-only | Yes | Fully represented | Discovery, counts, tensions |
| SS4A4 media | Text-only | Yes | Fully represented | GIF, video, carousel, timing |
| SS4A5 dialogs | Text-only | Yes | Fully represented | Geolocation and workarounds |
| SS4B behavior | Text-only | Yes | Fully represented | Sensitive data and paid prerequisites |
| SS4B1 cookies | Text-only | Yes | Fully represented | Three variants and prompt footnote |
| SS4B2 tiers | Text-only | Yes | Fully represented | Counts, shares, ambiguity, retention |
| SS5A guidance | Text-only | Yes | Fully represented | Five recommendations |
| SS5B risk profiles | Yes, text/image p. 8 | Yes | Represented in compressed form | Goal contingency, heterogeneity, metrics gap |
| SS5C limitations | Text; partial image p. 8 | Yes | Fully represented | Seven limitation families |
| RQ-A and RQ-B | Text-only | Yes | Fully represented | Exact wording retained |
| Formal hypotheses | Not identified | Yes | No item identified | No invented hypotheses |
| X1 baseline | Text-only | Yes | Fully represented | Full outcome matrix unavailable |
| X2 position | Text-only | Yes | Fully represented | Operator denominator qualified |
| X3 CTA variants | Text-only | Yes | Fully represented | Pair notation explained |
| X4 hidden descriptions | Text-only | Yes | Fully represented | All tested strategies |
| X5 exploration | Text-only | Yes | Fully represented | Both depth conditions and promotions |
| X6 media | Text-only | Yes | Fully represented | Counts and unspecified denominators distinguished |
| X7 native dialog | Text-only | Yes | Fully represented | No fabricated success rates |
| X8 spending/data | Text/image p. 8 | Yes | Fully represented | Contrasting goals and dummy credentials |
| X9 cookies | Text-only | Yes | Fully represented | All table cells |
| X10 tiers/retention | Text-only | Yes | Fully represented | Unresolved accounting preserved |
| T1 | Text-only | Yes | Represented in compressed form | All ten task purposes retained |
| T2–T7 | Text-only | Yes | Fully represented | Important values and caveats retained |
| Substantive figures | None identified | Yes | No item identified | Page images distinguished from figures |
| Architecture diagrams | None identified | Yes | No item identified | Prose reconstruction labeled |
| Major equations/theorems | None identified | Yes | No item identified | Derived arithmetic labeled |
| Algorithms/pseudocode | None identified | Yes | No item identified | No invented algorithm |
| Major contributions | Yes | Yes | Fully represented | Accessibility, taxonomy, behavior, implementation |
| Author limitations L1–L7 | Yes | Yes | Fully represented | Separate from analyst concerns |
| Footnotes 1–13 | Yes | Yes | Represented in compressed form | External model/tool/site pointers, not inspected artifacts |
| Footnote 14 | Text-only | Yes | Fully represented | Cookie-study prompt retained |
| References [1]–[19] | Text-only | Yes | Represented in compressed form | Roles summarized; bibliography not reproduced |
| Appendices | None identified | Yes | No item identified | No appendix review claimed |
| Supplied supplements | None supplied | Yes | Missing from supplied material | No supplementary files reviewed |
| Raw logs/code/recordings/CSV | No | Limitation stated | Inaccessible | Described outputs are not supplied artifacts |

### Missing or inaccessible material

During the isolated model pass, original visual layouts for pages2–7/9 were not supplied as images; subsequent parent inspection covered pages4–7 as noted in Stage0. Raw action logs, reasoning traces, final-answer files, GIF recordings, manual annotation CSVs, clone source code, exact full prompts including dummy-data blocks, complete runtime settings, and model snapshot identifiers are unavailable. Linked websites and referenced publications were not inspected. No appendices or supplementary files were supplied. Complete follow-up and Operator run totals cannot be established.

### Uncertain interpretations

Gemini’s subscription categories do not transparently reconcile with the denominator of 27. The abstract’s two-viewport claim and detailed scroll-action data use different or inadequately connected measures. Table VII’s extracted asterisk formatting is imperfect, although adjacent prose clarifies exploratory acceptance behavior. The abstract/introduction’s broad accessibility framing exceeds the tested alt-attribute result. The causal contributions of model, runtime extraction, timing, safety layers, and interface order remain unresolved.

### Deliberately compressed material

Related-work examples, regulatory discussion, bibliographic details, author contact information, licensing/download notices, and repeated descriptions of the same design recommendations are compressed. They are not treated as new experimental evidence. Table I’s exact prompt wording is summarized by task purpose; the complete task inventory remains represented. No experimental figure or substantive equation was deliberately omitted.

For bibliographic completeness: the original title is “Machine-Readable Ads: Accessibility and Trust Patterns for AI Web Agents interacting with Online Advertisements.” The authors are Joel Nitu, Heidrun Mühle, and Andreas Stöckl. The supplied venue line identifies the International Conference on Electrical and Computer Engineering Researches (ICECER 2025), December 6–8, 2025, Antananarivo, Madagascar. The supplied DOI is 10.1109/ICECER65523.2025.11400835. These are document-reported metadata, not externally validated publication facts.

### Potential omissions

No identified substantive section, reported table, research question, principal experiment, contribution, or author-stated limitation is knowingly left unrepresented. This statement is bounded by the supplied nine-page text and two page images. It does not establish that inaccessible artifacts contain no additional important information. The largest unresolved coverage limitation for the user’s research question is substantive rather than textual: the paper contains no direct standalone-LLM comparison, so that comparative claim cannot be supplied from this source.
