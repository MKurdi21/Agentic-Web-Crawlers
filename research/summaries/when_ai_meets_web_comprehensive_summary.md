## Stage 0 — Document Accessibility Report

The supplied main document contains extracted text for all 20 physical PDF pages. Thirteen pages also have supplied visual renderings: pp. 1, 3–9, 11–13, 17, and 18. Pages 2, 10, 14–16, 19, and 20 were inspected through supplied text only. No tools, browsing, outside sources, or independent file access were used. The supplied hash is retained as provenance metadata; it was not independently recomputed.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied page-by-page text, pp. 1–20 |
| Apparently missing pages | No gaps in supplied text numbering; independent PDF completeness not verified |
| Visual coverage | Partial: 13 rendered pages, including Figures 1–6 and Tables 1–4 |
| Table readability | Main labels and values readable through text and images; dense cells require careful alignment |
| Equations | No numbered substantive equations identified; role sequences and similarity concepts are readable |
| Appendices | A–D supplied; Appendix C continues through text-only p. 19; Appendix D is text-only |
| Supplementary files | None supplied; metadata reports zero embedded files and no detected supplementary references |
| OCR | Not required for this analysis; native extraction is available |
| Extraction limitations | Listing 8 has visibly corrupted angle-bracket notation in extracted text; image clarifies the intended tag structure |
| Independent verification | No reproduction, repository inspection, citation validation, or current vulnerability verification performed |

The paper is an empirical cybersecurity and AI-systems study: it combines ecosystem measurement, local plugin inspection, limited live-site observations, controlled model experiments, and prototype defenses. This analysis covers the supplied document, not every implementation artifact needed to reproduce it.

Evidence labels throughout are **[A] author-reported**, **[B] directly observable in supplied visuals**, **[C] analyst-derived**, and **[D] analyst interpretation**. No **[E] external information** is introduced. Confidence means confidence in the source-grounded representation: HIGH for clear statements or readable entries, MEDIUM for qualified interpretations or underspecified measurements, LOW for weak graphical estimates, and UNKNOWN where the document cannot establish a point. HIGH confidence in reporting a result does not imply strong statistical evidence for generalization.

## 1. Plain-language orientation

This paper examines customer-facing website chatbots installed through third-party plugins. A website owner can connect such a plugin to a commercial large language model, give it instructions, provide website content, and enable services such as search or notifications. The researchers ask whether the surrounding plugin preserves the security boundaries that the model expects. [A; pp. 1–2]

Their central finding is that some plugins transform an ordinary visitor's input into something the model treats as more authoritative. Eight studied plugins accepted browser-supplied conversation histories without integrity checks. Attackers could alter the apparent conversation, including fabricating assistant messages and, in seven of those plugins, system messages. Separately, 15 plugins scraped third-party website content, such as reviews, into chatbot knowledge. Several inserted that content into privileged positions rather than treating it as untrusted tool output. [A; pp. 6–8]

The researchers identified 17 plugins on 10,417 websites in an August 2024 crawl, measured adoption through April 2025, inspected plugins locally, observed selected live deployments, and tested 11 commercial models in a local simulation. They found that role forgery and unsafe content insertion often increase attack success; system-prompt hardening helps some application-level tasks but does not reliably secure tool use. [A; pp. 3–13]

For the research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the relevant answer is an **analyst inference**: website integrations introduce additional ways for untrusted material to reach the model and additional external actions that an attacker can redirect. This paper demonstrates those mechanisms for plugin-based chatbots. It does **not** directly compare a representative population of standalone LLMs with all web AI agents, and it does not establish that every web agent is more vulnerable. Its strongest comparison holds model and application configuration within a simulation while changing roles and content handling. [D; pp. 10–13]

## 2. Document roadmap

The document moves from deployment discovery to causal testing and remediation. Section 1 introduces the gap and contributions. Section 2 defines LLM customization, tools, prompt injection, and the plugin ecosystem. Section 3 explains plugin selection and website discovery. Section 4 characterizes communication architecture, functionality, growth, popularity, language, and content categories. Section 5 presents the threat model and local vulnerability analysis. Section 6 measures system prompts, tools, and the difficulty of identifying deployed models. Section 7 translates those observations into controlled experiments. Section 8 discusses additional weaknesses, defenses, and distribution shift. Section 9 reports broader implications and disclosure outcomes. Section 10 acknowledges support. References occupy pp. 15–17. [A]

Appendix A supplies experimental prompt listings; Appendix B examines additional prompt styles; Appendix C analyzes real-world system-prompt templates; Appendix D contains the program committee's meta-review. Figures 1–4 appear in the main text; Figures 5–6 appear with appendices. Tables 1–4 respectively summarize deployment counts, plugin risks, direct attacks, and indirect attacks.

The principal analysis inventory is:

| ID | Component | Location |
|---|---|---|
| X1 | Plugin selection and crawl-based discovery | §3, p. 3 |
| X2 | Functionality validation | §4.2, pp. 4–5 |
| X3 | Adoption, popularity, language, and category analysis | §4.2, p. 5; Fig. 5, p. 17 |
| X4 | Local protocol, customization, and vulnerability audit | §5.1–5.3, pp. 6–8 |
| X5 | Existing third-party-content exposure | §5.3, p. 8 |
| X6 | Live system-prompt extraction and classification | §6.1, pp. 8–9 |
| X7 | Passive tool metadata analysis and attempted model identification | §6.2–6.3, pp. 9–10 |
| X8 | Controlled direct attacks: extraction, task hijacking, tool hijacking | §7.1, pp. 10–11 |
| X9 | Controlled indirect context hijacking | §7.2, pp. 12–13 |
| X10 | Additional prompt styles | Appendix B, p. 18 |
| X11 | Template similarity and modification analysis | Appendix C, pp. 18–19 |
| X12 | UGCBuster prototype validation | §8.2, p. 14 |
| X13 | Tool-instruction hardening | §8.2, p. 14 |

No formal hypotheses, numbered equations, theorems, or pseudocode algorithms are supplied. UGCBuster is described procedurally in prose. Prompt Listings 1–16 are methodological artifacts, not instructions to this analyst.

## 3. Background and context

A **large language model (LLM)** receives textual context and generates a response, typically token by token. Context includes developer instructions, earlier conversation messages, and external information. **Temperature** is a generation parameter; the paper varies neither its value nor its effect experimentally, using 0.5 in the controlled trials. [A; pp. 2, 10]

A **system prompt** describes the chatbot's intended behavior. A **role** labels the origin or function of a message: system, assistant, user, or tool. The paper describes an **instruction hierarchy** in which developer-defined instructions receive higher authority than untrusted user input and tool output. The security argument depends on keeping those labels trustworthy. An attacker who can submit a message labeled system gains a capability beyond ordinary user input. [A; pp. 1, 5, 7]

**Retrieval-augmented generation (RAG)** searches an external knowledge base for content relevant to a user query and adds it to the model's context. **Direct copying (DC)** inserts an entire source into context. **Fine-tuning (FT)** changes model weights using external data. These are distinct customization methods; the controlled indirect experiment studies RAG content handling, not all fine-tuning threats. [A; pp. 2, 6]

**Tool use** lets the model invoke external functions or application programming interfaces (APIs). A search tool takes a query; a notification tool takes arguments such as a channel and topic. Tool outputs can add information to context, while tool calls can affect other systems. [A; pp. 2, 9]

**Direct prompt injection** originates in an adversarial interaction with the chatbot. **Indirect prompt injection** reaches the chatbot through external material, even when the current user is benign. A malicious review can therefore influence a later customer's conversation. The paper distinguishes injection against application-developer intentions from **jailbreaking**, which targets provider-imposed safeguards. [A; p. 3]

A **web content management system (WCMS)**, such as WordPress (WP), supports website building through plugins. **Hypertext Markup Language (HTML)** supplies the website structure used for plugin markers and content extraction. **Hypertext Transfer Protocol (HTTP)** requests are stateless; **WebSocket** connections provide stateful communication. HTTP itself is not identified as the vulnerability: the failure is trusting unauthenticated browser-maintained message state. [A; pp. 3–4, 7]

## 4. Research problem and gap

The existing problem is that LLM applications can follow malicious instructions embedded in material that should function as data. The authors argue that earlier security attention concentrated on advanced copilots, coding agents, and browser assistants, while inexpensive plugin-based customer-service chatbots remained poorly understood. [A; pp. 1–3, 14]

The attributed shortcomings of prior approaches are twofold. Traditional plugin research emphasizes cross-site scripting, SQL injection, remote code execution, and cross-site request forgery. LLM security experiments often assume the application preserves the distinction between developer instructions and untrusted content. The studied plugins connect these domains: ordinary integration mistakes can invalidate the assumptions underlying model-level defenses. [A; pp. 3, 13–15]

The research gap concerns both **implementation** and **deployment configuration**. A plugin may allow forged histories or choose unsafe insertion roles; a website owner may select a weak prompt, a particular model, or tool descriptions that are easy to override. The study measures both layers rather than attributing every failure to the model. [A; pp. 1–2, 8]

Scope is deliberately restricted to selected WordPress and platform-agnostic plugins, primarily serving smaller organizations. Enterprise platforms such as Zendesk, Tidio, and Intercom are excluded. Their exclusion is a design decision, not evidence that all enterprise products are secure. The authors describe them as generally less prone to the particular systematic risks under study, without evaluating that proposition here. [A/D; p. 3]

## 5. Research questions, objectives, and hypotheses

The paper does not present formal numbered research questions or statistical hypotheses. Its author-stated objectives can be organized without pretending these are quotations or original question labels:

- **O1:** Characterize the deployment ecosystem of 17 chatbot plugins and their communication patterns. [A; §§3–4]
- **O2:** Identify plugin behavior that permits privileged-role direct injection or unsafe ingestion of external content. [A; §5]
- **O3:** Measure real-world system prompts and activated tools to ground experimental conditions. [A; §6]
- **O4:** Quantify how role handling, content insertion, prompt design, and model choice affect attack success. [A; §7]
- **O5:** Explore lightweight mitigations and report disclosure outcomes. [A; §§8–9]

The user's research question is external to the paper's formal framing. Relevance is **[D] analyst interpretation**: O2 and O4 expose mechanisms by which a web integration can make an underlying LLM easier to misuse, while O3 shows how tools expand possible consequences. No formal hypothesis about universal web-agent superiority or inferiority is tested.

## 6. Assumptions / Threat Model

The adversary is a non-privileged website visitor. They may browse, communicate with the chatbot, send network requests, and post reviews or comments where the site permits this. They are assumed able to identify the plugin, for example from traffic patterns. The LLM provider and application developer are treated as trusted; the visitor and external data source are untrusted. [A; pp. 3, 5–6]

The intended boundary confines adversarial conversational input to the user role. Tool outputs should enter as low-trust tool material. Vulnerable integrations let the attacker cross these boundaries by editing HTTP history or by placing instructions in scraped content that is assigned inappropriate authority. [A; pp. 5–8, 13]

The direct attack surface is the browser-to-plugin request payload. The attacker can replace previous assistant text and, except for P7 among the eight vulnerable plugins, inject system messages. This does not require altering the developer's original system prompt: forged additional messages coexist with original context. [A; p. 7]

The indirect surface is content that a website accepts from third parties and a plugin subsequently scrapes. Persistence arises when this content enters a knowledge base and is later retrieved. The paper also notes direct copying of the visitor's current page as a possible ingestion path. [A; pp. 6–8]

Excluded capabilities include exploiting unrelated plugins or classical vulnerabilities such as SQL injection. The researchers do not place malicious reviews on real third-party sites; existing review exposure is assessed through benign questions. Experimental poisoning and tool misuse occur in the local simulation. [A; pp. 6, 8, 10–12]

Model API constraints matter: Anthropic and Gemini models in these experiments accept a single top-level system message, so additional separate-system-message conditions are unsupported. OpenAI models permit the tested additional system messages. System-append remains possible for all providers because it changes the existing system prompt rather than adding another system message. [A; pp. 10, 12–13]

## 7. Methodology

### Discovery and selection

The WordPress marketplace search used the keywords ChatGPT Chatbot and returned 116 results. Exclusions covered fewer than 50 installations, non-LLM solutions, content-generation rather than chatbot functionality, unreliable local deployment, and lack of website-data customization. Seven WordPress plugins remained. Generic plugins were found through search engines and comparison blogs; unpopular, nonfunctional, or locally untestable options were excluded. Three otherwise relevant generic plugins, together on approximately 300 sites, were also excluded because suitable free or short-term access was unavailable. Ten generic plugins remained. [A; p. 3]

The authors associated each selected plugin with distinctive front-end HTML markers. Searching the August 2024 Common Crawl archive, covering 38.3 million registered domains, produced 10,417 unique websites after deduplication by top-level registered domain. Marker detection establishes apparent deployment, not live functionality. Subsequent crawl snapshots span January 2023 to April 2025. [A; pp. 3–5]

### Functionality and deployment characterization

A September 2024 random spot-check examined 200 websites: 116 generic and 84 WordPress. The four checks were online status, marker retention, visible chatbot, and functional response. Automated validation additionally focused on P1, P2, and P4. The paper explains why a single scalable generic validator is difficult: protocols, dynamic loading, authorization gates, iframes, versions, and configurations differ. [A; pp. 4–5]

Domain age came from WHOIS; popularity used a Tranco list generated on 27 September 2024. Language labels came from crawl annotations, and website categories from Cloudflare's Domain Intelligence API. These are author-used data sources, not services queried for this analysis. [A; p. 5]

### Local plugin audit

Each selected plugin was installed on a local WordPress instance and configured with an OpenAI LLM. Product pages supplied customization content. Network inspection identified transport and state handling. Configuration was grouped into model-based, tool-based, and data-based features. Scrapers were tested on several real-world pages and generally stripped HTML into visible text, including third-party material. Exact plugin versions, the number of scraper test pages, and detailed page-level outcomes are not supplied. [A; p. 6]

For WordPress plugins, API logs revealed content roles. Generic-provider logs were mostly unavailable, so the researchers configured a debugging prompt, triggered product retrieval, and asked the model to identify the preceding content's role. They repeated this for five product names and used majority voting. The method worked in their tests when the model complied; it is not a universal guarantee that a model accurately reports internal role annotations. [A; pp. 6–7]

### Live configuration measurements

The indirect-exposure audit sampled 100 e-commerce sites with functional P1 chatbots. System-prompt extraction sampled 300 P1 sites. Prompt leakage was manually judged by at least three sentences with instruction-like characteristics, allowing paraphrases because ground-truth live prompts were unavailable. Tool metadata was passively observed from P1 iframe HTML and HTTP traffic. P1 was selected for prevalence, a bug-bounty program, and an architecture suited to automation. [A; pp. 8–9]

### Controlled simulation

The local simulator reproduced scraping, RAG, prompt configuration, multiple model providers, and tools. Thirty-five Nalgene product pages supplied a representative knowledge base. Content was chunked into 600-token units with 300-token overlaps and embedded using text-embedding-3-large. No training/test split is described; this is an attack-condition experiment, not a supervised predictive benchmark. Hardware, operating-system details, library versions, random seeds, exact model snapshot identifiers, and full trial logs are not provided. [A; p. 10]

The researchers drafted role-override seed prompts, used ChatGPT to produce five variants per goal, and selected the most effective through trials on a subset of models. They excluded special characters that some plugins might escape. This design measures realistic proof-of-concept exploitation of integration conditions, not the maximum capability of adaptive attackers. Variant-selection model identities and full selection outcomes are not reported. [A; p. 10]

Each supported configuration ran 10 times at temperature 0.5. Metrics were counts of successful outcomes, with provider and overall means in Tables 3–4. No confidence intervals, hypothesis tests, error bars, significance levels, or random-seed protocol are reported. The three prompt conditions are insecure, hardened, and hardened-specific; the last explicitly prohibits coding. Models are GPT-4o-mini, GPT-4o, GPT-4.1-mini, GPT-4.1, o4-mini, Claude Haiku 3.5, Sonnet 3.5, Sonnet 4, Gemini 2.0 Flash, 2.5 Flash, and 2.5 Pro. [A; pp. 9–13]

## 8. Experiments / Analyses

### X1–X3: deployment and functionality

Discovery found 10,417 marker-bearing sites in August 2024 and 17,474 in April 2025. The functionality sample narrowed from 200 sites to 195 online, 180 retaining markers, 162 displaying chatbots, and 125 answering queries. Thus 62.5% of the original sample was functional. This is an explicitly reported deployment estimate, not an attack-success estimate. Thirty-seven visible chatbots failed functionality; 30 used type 1 plugins and seven type 2. Reported causes include quota exhaustion, deprecated models, missing defaults, unavailability, and plan limits. [A; pp. 3–5]

### X4: local vulnerabilities

Eight plugins accepted forgeable browser-supplied histories. Fifteen scraped third-party content. Seven assigned retrieved material to system, four to assistant, three to user, and one to tool, as classified in Table 2. P14 supports fine-tuning with scraped content but is not included in the 15 automated third-party-scraping cases. Logs often omitted forged or retrieved content, limiting developer visibility. [A/B; pp. 6–8]

### X5: real-world content exposure

Among 100 P1 e-commerce sites, 41 allowed reviews/comments, 36 displayed them, and 13 chatbots returned review-specific information. The observed endpoint is incorporation of third-party content, not successful malicious injection. Testing was limited to five questions per chatbot and some refused customer-specific questions. The authors therefore regard the estimate as potentially low. [A; p. 8]

### X6 and X11: prompt extraction and template analysis

Across 300 P1 sites, an ordinary user request extracted instruction-like material in 1% of cases. Forged system and assistant messages yielded 56% and 55%, respectively. The union of successful extractions contained 219 chatbots, or 73%; these percentages overlap and must not be added. Ground-truth live prompts were unavailable. [A; p. 9]

Template comparison used three metrics: 3-gram Jaccard, 3-gram overlap coefficient, and embedding cosine similarity. Seventy-six percent of extracted prompts contained over 80% of a known template by overlap coefficient; 31% were exact copies. Common changes concerned names, organization details, contact collection, and tone. Approximately 5% explicitly requested personally identifiable information. The main text reports 97% with out-of-scope refusal instructions, whereas Appendix C reports roughly 96%; the difference is unresolved. [A; pp. 9, 18–19]

### X7: tools and model identification

The April 2025 scan identified 144 P1 chatbots with activated tools. Tavily Search appeared on 43, Calendly on 40, Slack Notification on 10, and custom tools on 42. These categories are not stated to be mutually exclusive. The experiment selected Search and Notification because their implementations were known. Custom tools were excluded because invasive probing would be necessary; Calendly only exposed public calendar links. The attempted knowledge-cutoff fingerprint proved unreliable, so the researchers selected widely supported vendor models rather than verifying the exact deployed model distribution. [A; pp. 9–10]

### X8a: controlled system-prompt extraction

The manipulated variables are model, system-prompt design, and injection role. Success is detecting ground-truth prompt excerpts in model output. The user-role condition combines attack instruction and trigger in one user message, while privileged-role conditions place attack instructions separately before a triggering user message. Table 3 shows substantial model variation: GPT-4.1 returns 10/10 successful extractions in system and assistant conditions across all three prompt types, but 0/10 in user conditions. o4-mini returns 0/10 throughout this extraction experiment. [A/B; pp. 10–11]

### X8b: controlled task hijacking

The target chatbot is a sales agent for Nalgene bottles. The unauthorized task is generating Python for the Fibonacci sequence. Success is output containing relevant Python code. This tests violation of application scope; coding is not inherently forbidden by the underlying base model. Hardened-specific prompts explicitly forbid coding. For GPT-4o, system/assistant/user counts change from 9/6/0 under insecure prompts to 2/1/0 under hardened prompts and 0/0/0 under hardened-specific prompts. Gemini 2.5 Pro still succeeds 9/10 through assistant injection under hardened-specific instructions. [A/B; pp. 10–11]

### X8c: controlled tool hijacking

The legitimate Notification tool should send configured Nalgene or Purchase notifications to #notifications. The attacker seeks a call with #general and www.abcxyz.com instead. Success requires the tool call with both attacker-selected arguments; delivering a real phishing campaign is not the experiment. Gemini models usually reach 9–10/10 in these conditions, including user-role injections. GPT-4o-mini remains at 0/10 in all reported tool-hijacking cells. Hardening the general system prompt can leave tool misuse unchanged or even increase it. [A/B; p. 11]

### X9: controlled indirect context hijacking

The current user asks about a target Nalgene product. A poisoned content chunk combines the product name with instructions to search for Hydro Flask. Conditions vary model, three prompts, wrapped/unwrapped content, and five insertion modes: system-append, separate system, assistant, user, or tool. Anthropic and Gemini omit separate-system mode. Success requires a tavily-web-search call with query Hydro Flask and inclusion of returned URLs in the response. Retrieval is deliberately facilitated through product-linked attacker text; the study does not estimate uncontrolled real-web retrieval probability. [A; pp. 12–13]

### X10, X12, and X13: supplemental attacks and defenses

Appendix B reports small-scale blunt and ignore-plus-instruct experiments. Plugin vulnerabilities increased success by up to approximately 3×; blunt prompts sometimes outperformed role-override prompts by approximately 4× in indirect settings. Detailed cells and configurations are absent. UGCBuster was manually validated on 10 e-commerce sites with three pages each, identifying UGC containers with one false positive and approximately $0.05 average cost per page. Tool-instruction hardening reduced attack success by a reported 40–75%, but the paper does not provide a full defense-result table or unambiguously specify absolute versus relative reduction. [A; pp. 14, 18]

## 9. Results

The central result is conditional: integrations that preserve roles are generally safer in these tests than integrations allowing attacker-controlled privileged messages or unsafe retrieved-content placement. The paper's abstract reports a 3–8× increase for direct attacks involving unintended behavior; Table 3 supplies configuration-specific evidence rather than a universal multiplier. The 8,000-site exposure is approximate and historically situated; P1 subsequently patched direct history forgery. [A; pp. 1, 6–7, 14]

The ecosystem expanded from 10,417 to 17,474 marker-bearing sites between August 2024 and April 2025. **[C] Analyst-derived:** the increase is 7,057 sites, calculated as 17,474 − 10,417; relative growth is approximately 67.7%, calculated as 7,057 / 10,417 × 100. This interval differs from the introductory statement of nearly 50% growth in 2025 alone, so the two figures should not be treated as directly contradictory. [A/C; pp. 1, 4–5]

Live extraction provides a strong contrast within its operational definition: forged system requests yielded 56%, compared with 1% through the ordinary user request. **[C] Analyst-derived:** this is a 55-percentage-point difference and a 56-fold ratio of the reported rates. Assistant forgery yields a 54-point difference and 55-fold ratio. These are live prompt-extraction comparisons, not the abstract's 3–8× task-hijacking measure. [A/C; p. 9]

Table 3's overall average task-hijacking counts under insecure prompts are 9.8 for system, 5.9 for assistant, and 1.0 for user, each on a scale of 0–10. **[C] Analyst-derived conversions:** approximately 98%, 59%, and 10%, respectively. The system mean includes only the five OpenAI models; assistant/user means include 11 models. Under hardened-specific prompts the reported means are 2.4, 1.5, and 0. Generalization must account for these unequal provider denominators. [A/B/C; p. 11]

For indirect attacks, Table 4's unwrapped insecure overall means are 4.1, 3.8, 1.5, 3.1, and 1.3 for SA/S/A/U/T. Under wrapped hardened conditions they are 3.0, 0.2, 2.1, 3.1, and 0.9. Tool-role insertion has the lowest overall mean in most combinations, but not literally every averaged condition: separate-system insertion is lower in some wrapped comparisons, and individual models show exceptions. The authors' broad robustness conclusion should therefore be read as an aggregate design recommendation, not a cell-by-cell dominance theorem. [A/B/D; pp. 12–13]

General system-prompt hardening is most effective for maintaining application task scope. It does not reliably constrain argument selection for connected tools. The authors consequently distinguish system-prompt robustness from tool-description robustness and recommend hardening tool instructions independently. [A; pp. 11–14]

## 10. Figure-by-figure interpretation

### Figure 1 — Communication architectures, p. 4

This is a two-row flow diagram, not a quantitative plot. Type 1 connects visitor, website front end, website back end, and LLM provider. Type 2 replaces the website-owned intermediary with the commercial plugin provider. Bidirectional arrows indicate request/response exchange. The diagram explains who manages API access and configuration; it does not label every trust boundary, encryption property, or logging path. No axes, numerical scale, uncertainty markers, or performance measurements are present. [B; §4.1]

### Figure 2 — Adoption and domain registrations, p. 5

The left panel plots calendar snapshots from January 2023 through April 2025 against number of websites, with a linear vertical scale from 0 to 18K. Blue, orange, and green distinguish generic, WordPress, and total deployments. All rise; generic growth dominates the final increase, while WordPress growth slows. Exact endpoint counts come from Table 1 and text, not interpolation of the small plot. [A/B]

The right panel plots domain-registration time from January 2022 through September 2024 against number of registrations, on a linear vertical scale labeled 0–90. A ChatGPT-release annotation accompanies a rise around late 2022 and early 2023. The authors interpret this as suggesting some sites were created to use LLMs. The plot cannot establish the causal purpose of registrations. Individual point values, the precise aggregation interval, and confidence bands are not supplied; none are invented here. [A/B/D]

### Figure 3 — Message-history forgery, p. 7

Three horizontal paths contrast untampered, forged-assistant, and forged-system HTTP POST requests. Blue represents the normal history, and red marks attacker-controlled histories. The normal chatbot declines prompt disclosure. A forged assistant promise followed by Hello induces disclosure; a forged system directive similarly induces disclosure of the original prompt. Request boxes, rightward HTTP arrows, and response boxes expose the end-to-end mechanism. This is an illustrative attack trace, not a success-rate plot or proof that every model will behave this way. [B]

### Figure 4 — Malicious-review ingestion, p. 8

A product page contains normal material and Mallory's malicious review; arrows connect the page through a chatbot-processing icon to a sales-agent exchange. The legitimate query asks about Cool Jeans, while the output follows the review's injected instruction. Components distinguish the adversarial content author from the benign chatbot user. The review count and example names are illustrative diagram details, not sample statistics. The figure demonstrates the ingestion-and-response path; the 13% exposure estimate comes from the separate real-site audit. [A/B]

### Figure 5 — Language and category distributions, p. 17

Two linear bar charts show percentages of websites. The left uses ENG, SPA, GER, FRE, POR, and REST, corresponding to English, Spanish, German, French, Portuguese, and the other languages. The y-axis is percent of websites, with labeled ticks through 60. An 88 Languages annotation identifies the residual group. Text supplies exact aggregates: 93 languages overall, 81% in the top five, and 19% across the remaining 88. Individual bar percentages are not precisely labeled and are not promoted to exact values. [A/B]

The right panel uses business, e-commerce, education, blogs, health, technology, finance, and REST. Its linear percentage axis is labeled through 30. The text reports 72% across the seven named categories and roughly 10% e-commerce, around 1,100 sites. This plot describes application diversity, not measured attack differences across languages or industries. Security concerns for low-resource languages are author discussion informed by cited prior work, not a multilingual experiment in this paper. [A/B]

### Figure 6 — Template similarity distributions, p. 18

This cumulative distribution function (CDF) plots similarity score on the horizontal axis and cumulative probability, 0–1, on the vertical axis. Blue, orange, and green represent 3-gram Jaccard, 3-gram overlap, and embedding similarity. The Jaccard curve is generally higher at intermediate thresholds, reflecting lower similarity scores than the other measures. High-score accumulation and jumps near 1 indicate substantial template reuse. Exact statistics—76% above 80% template containment and 31% exact copies—come from text. The figure does not specify the embedding model name, uncertainty intervals, or a detailed similarity-aggregation protocol across templates. [A/B]

## 11. Table-by-table interpretation

### Table 1 — Dataset versions, p. 4

| Plugin group | Plugins | August 2024 sites | April 2025 sites | August Top-1M share | April Top-1M share |
|---|---:|---:|---:|---:|---:|
| WordPress | 7 | 3,534 | 5,266 | 4.4% | 4.7% |
| Generic | 10 | 6,883 | 12,208 | 9.1% | 8.1% |
| All | 17 | 10,417 | 17,474 | 7.5% | 7.1% |

Values are author-reported deployment counts and popularity shares. These are not numbers of verified functioning or successfully attacked sites. The table has no statistical tests or uncertainty intervals. Generic deployments are more numerous and have a greater Top-1M share in both snapshots. [A/B]

### Table 2 — Per-plugin risk inventory, p. 6

The following compact transcription preserves each plugin's transport, tools, approximate deployment counts, direct injection roles, and indirect content role. S/A/U/T mean system/assistant/user/tool; H/W mean HTTP/WebSocket; type 1/2 means website-backend/commercial-provider architecture.

| Plugin | Type | Transport | Tools | Sites Aug→Apr | Direct roles | Third-party scraping / insertion |
|---|---:|---|---|---|---|---|
| P1 | 2 | H | Yes | 4.0K→7.6K | S+A, later patched | Yes / S |
| P2 | 1 | H | Yes | 2.4K→3.4K | S+A | Yes / S |
| P3 | 2 | H | No | 909→1.2K | None | Yes / A |
| P4 | 2 | H | No | 408→1.0K | S+A | Yes / A |
| P5 | 2 | W | Yes | 799→690 | None | Yes / S |
| P6 | 2 | H | Yes | —→625 | None | Yes / A |
| P7 | 1 | H | Yes | 578→610 | A | Yes / U |
| P8 | 1 | H | No | —→557 | None | Yes / T |
| P9 | 2 | W | No | 379→489 | None | Yes / U |
| P10 | 1 | H | No | 365→467 | None | Yes / S |
| P11 | 2 | H | No | 266→439 | S+A | Yes / S |
| P12 | 1 | H | No | 133→203 | S+A | Yes / S |
| P13 | 2 | W | Yes | 60→64 | None | Yes / S |
| P14 | 1 | H | No | 13→18 | None | No; scraped-content FT only |
| P15 | 1 | H | No | 7→18 | None | No |
| P16 | 2 | H | No | 1→18 | S+A | Yes / U |
| P17 | 2 | H | No | 11→13 | S+A | Yes / A |

Dashes are retained rather than interpreted as zero. Counts such as 4.0K are rounded source representations. Tool support is dated April 2025. Direct-injection logging was absent in dashboards, although API-provider logs offered visibility in marked cases. P2 later added a warning. For indirect content, only P7 and P11 show dashboard logging; Table 2 additionally marks provider-log visibility for P2, P8, P9, P10, and P12. P8 uses the provider's proprietary RAG tool. P14's fine-tuning footnote is important because it distinguishes absence of the tested RAG risk from absence of all content-customization risk. [A/B]

### Table 3 — Direct attack outcomes, p. 11

Each cell is successes out of 10, not an already expressed percentage. Columns cross three attack tasks, three prompt designs, and S/A/U roles. Unsupported system cells for Anthropic and Gemini are dashes. Means can be fractional because they average models. No significance notation or error terms appear.

| Task | Prompt | Overall S | Overall A | Overall U |
|---|---|---:|---:|---:|
| Extraction | Insecure | 5.4 | 4.1 | 2.8 |
| Extraction | Hardened | 6.0 | 3.8 | 0 |
| Extraction | Hardened-specific | 6.0 | 4.2 | 0.1 |
| Task hijacking | Insecure | 9.8 | 5.9 | 1.0 |
| Task hijacking | Hardened | 6.2 | 3.8 | 0 |
| Task hijacking | Hardened-specific | 2.4 | 1.5 | 0 |
| Tool hijacking | Insecure | 3.0 | 4.8 | 3.7 |
| Tool hijacking | Hardened | 4.0 | 6.7 | 3.8 |
| Tool hijacking | Hardened-specific | 6.0 | 7.1 | 3.7 |

These are displayed table values. S averages cover five models; A/U cover eleven. Tool-hijacking means rise with hardening in privileged-role conditions, demonstrating that general prompt constraints do not secure every tool argument. Individual zeroes and maxima matter: o4-mini blocks all tested extraction yet is vulnerable to several tool attacks; GPT-4o-mini blocks all tested tool hijacking yet permits system-role extraction. Gemini 2.0 Flash allows 10/10 insecure user task hijacks but 0/10 with hardened prompts. Provider rankings are therefore task- and condition-dependent. The full 11-model cell matrix is deliberately compressed to means and diagnostic examples; no uniform ranking is inferred. [A/B]

### Table 4 — Indirect context hijacking, p. 12

Each entry again counts successes out of 10. Columns cross wrapping, prompt design, and SA/S/A/U/T insertion. SA means appending retrieved content to the existing system prompt; S means a separate system message. Those are materially different conditions.

| Wrapping | Prompt | Overall SA | Overall S | Overall A | Overall U | Overall T |
|---|---|---:|---:|---:|---:|---:|
| Unwrapped | Insecure | 4.1 | 3.8 | 1.5 | 3.1 | 1.3 |
| Unwrapped | Hardened | 3.5 | 2.4 | 1.0 | 3.8 | 0.6 |
| Unwrapped | Hardened-specific | 3.2 | 2.4 | 1.5 | 3.5 | 0.9 |
| Wrapped | Insecure | 3.9 | 0.8 | 1.8 | 2.4 | 0.9 |
| Wrapped | Hardened | 3.0 | 0.2 | 2.1 | 3.1 | 0.9 |
| Wrapped | Hardened-specific | 2.8 | 0.4 | 1.8 | 3.2 | 0.7 |

Separate-S means cover only OpenAI models; other means cover eleven models. Wrapping sharply reduces the separate-S overall average in these data but is not uniformly beneficial in every role or provider. For Gemini 2.5 Pro, wrapped hardened tool insertion succeeds 7/10 versus 3/10 unwrapped. For Sonnet 4, SA succeeds 7–9/10 across conditions, while assistant insertion stays at 0/10. GPT-4o-mini is nearly entirely resistant, with one success in the unwrapped hardened separate-S condition. No statistical significance is reported. The full matrix is compressed, with exceptions retained to avoid presenting aggregate tendencies as guarantees. [A/B]

## 12. Diagram / Architecture Interpretation

Figures 1, 3, and 4 jointly explain the security mechanism. Figure 1 locates the components that mediate access to the model. Figure 3 shows a control-path failure: the browser sends purported conversation state, the intermediary accepts its claimed roles, and the model treats forged instructions as part of context. The attack exploits an authenticity problem before inference rather than requiring a sophisticated malicious sentence. [A/B/D; pp. 4, 7]

Figure 4 shows a data-path failure: an attacker posts website content, the scraper collects it, the knowledge system later retrieves it, and the model follows its instruction during a benign query. The indirect attacker need not participate in the victim's conversation. This path can repeat across later sessions if content remains available or stored. The figure does not establish a measured persistence duration. [A/B; pp. 7–8]

The role sequences on p. 12 distinguish two implementation patterns. In system-append, system context becomes [System Prompt] + [Retrieved Content]. In separate-message insertion, the original system prompt remains and a later [ROLE] message contains retrieved material. Tool-role insertion instead identifies it as output from a RAG tool. These paths are experimental factors, not interchangeable serialization details. [A]

UGCBuster adds an upstream filtering stage: HTML paths → grouped content → LLM-assisted UGC identification → shared-container promotion and overlap merging → confidence-tagged metadata → developer exclusion or review. The document does not supply pseudocode, exact prompts, or a formally verified decision rule. [A; p. 14]

## 13. Equations and mathematical concepts

No numbered mathematical equations, optimization losses, theorems, or proofs are necessary to follow the paper. The quantitatively important concepts are counts, rates, ratios, string similarity, and cumulative distributions.

The controlled attack rate can be represented as **[C] analyst-derived notation**: rate = successful trials / 10. Thus 7 successes means 70% for that specific configuration. A displayed mean of 0.9 means an average of 0.9 successes per 10 trials across the applicable models, approximately 9%; it is not a directly observed fractional trial. Means reported to one decimal are rounded.

For clarity, **[C] explanatory mathematical identities** for Appendix C's named string metrics are Jaccard(A,B) = |A∩B| / |A∪B| and overlap(A,B) = |A∩B| / min(|A|,|B|), where A and B are the compared 3-gram collections interpreted as sets. These formulas are analyst explanations of the named metrics, not displayed equations in the paper. The supplied text does not specify tokenization, character versus word 3-grams, duplicate handling, or empty-set behavior, so reproduction remains underspecified. [A/D; p. 18]

Cosine similarity is named as an embedding comparison, but the embedding model and detailed computation are absent. No numerical embedding formula is attributed to the authors. A CDF at threshold x describes the fraction of comparisons with score at or below x. Figure 6 therefore characterizes a distribution of similarity scores rather than the attack probability at a given similarity. [A/D; p. 18]

Percentages and percentage points are kept separate. For example, 56% versus 1% is a 55-percentage-point difference, while 56/1 is a 56-fold ratio. The source's 20–40% and 40–75% mitigation reductions are retained as reported because a fully specified baseline and absolute/relative interpretation are not provided. [A/C; pp. 9, 13–14]

## 14. Interpretation and discussion

The evidence supports an integration-layer explanation of vulnerability. LLM defenses assume that roles reflect actual provenance. Plugins can invalidate that assumption by letting visitors forge those roles or by promoting scraped data into instruction-bearing context. The model then receives a different security situation from an ordinary low-privilege malicious user message. [A; §§7.3, 8.3]

The authors frame a role change such as user→system as a distribution shift: malicious inputs are placed outside the role conditions assumed in defensive training. This is their mechanistic interpretation; the study does not directly inspect model training data or measure internal representations. [A; p. 14]

Tools introduce a second dimension. A model that refuses unrelated coding may still choose attacker-controlled notification arguments. General scope instructions and tool-specific operational rules protect different behaviors. This explains why hardening can substantially help task hijacking without reliably helping tool hijacking. It does not prove that all stronger instructions worsen tool safety. [A/D; pp. 11–14]

Cross-reference checks reveal several unresolved qualifications:

- Main text p. 9 gives 97% refusal instructions; Appendix C p. 18 gives roughly 96%. No denominator reconciliation is supplied.
- The task-hijacking prose on p. 11 says insecure user injections succeed approximately 20%; Table 3's overall insecure U mean is 1.0/10, approximately 10%. The prose may use another aggregation, but it does not specify one.
- The same prose gives user tool-hijacking success of 20–100% depending on provider; OpenAI provider means in Table 3 are 0–0.2/10, or 0–2%. The stated range cannot describe all displayed provider means as written.
- The indirect-results prose names GPT-4.1 among models highly vulnerable in SA mode; Table 4's GPT-4.1 SA entries range from 0 to 5/10. o4-mini and Gemini 2.5 models provide clearer examples of 10/10 SA success.
- The statement that T is most robust across all settings is stronger than literal cell-wise dominance. Aggregate and individual exceptions are visible in Table 4.
- Listing 13, the basis for the insecure prompt, already contains refusal language. Insecure is a comparative experimental label, not a claim that the original template has no constraints whatsoever.

These discrepancies are reported rather than repaired. They do not erase the broader pattern of harmful role handling, but they reduce confidence in some prose-level numerical generalizations. [D]

## 15. Contributions and novelty

The authors claim the first large-scale systematic study of prompt-injection vulnerabilities in this plugin ecosystem. That priority claim is reproduced as author positioning, without external literature verification. [A; pp. 1–3]

The empirical contribution is a measured deployment ecosystem spanning 17 plugins and more than 10,000 websites, with a later snapshot reaching 17,474. The security contribution is identification of history forgery and unsafe ingestion as practical ways to amplify prompt injection. The methodological contribution is linking local plugin inspection and live configuration observations to a controlled factorial simulation. The configuration contribution is measurement of extracted prompts, template reuse, and enabled tools. [A; p. 2]

The experimental contribution separates role handling, system-prompt design, model choice, wrapping, and content insertion. The implementation contribution consists of UGCBuster and LLM-assisted tool-instruction hardening. The operational contribution includes disclosures and documented vendor responses. There is no new theorem, formal security proof, general-purpose attack optimizer, or publicly established benchmark artifact in the supplied material. [A/D; pp. 10–15]

Appendix D attributes the contribution to an impactful vulnerability and large-scale empirical measurement. This is program-committee assessment reproduced in the paper, not independent confirmation by this analyst. [A; p. 20]

## 16. Limitations

### Authors' stated limitations

The dataset may underestimate the ecosystem. HTML markers do not prove functionality, and generic validation is difficult. Some otherwise relevant plugins were excluded for access limitations. Live system prompts lacked ground truth and were identified heuristically. Role inference for generic plugins depended on model compliance. Real-world review exposure used only five queries per chatbot and excluded malicious posting, likely missing some exposure paths. Model cutoff fingerprinting was unreliable. Custom-tool implementations were not observed or invasively tested. The attacks are proof-of-concept methods rather than newly optimized or advanced strategies. [A; pp. 3–10]

The authors also emphasize that no universally accepted prompt-injection solution exists. Their conclusion expects custom tools could be equally or more vulnerable, but this is explicitly an expectation rather than an experimental finding. [A; pp. 13–14]

Appendix D's committee concern is distinct from an author-authored limitation: security of the proposed defenses against strong adaptive attackers remains unclear. This is a supplied review qualification and is preserved as such. [A; p. 20]

### Additional evidence-based analyst observations

The selected plugins, crawl coverage, and P1-centered live measurements limit representativeness. Counts of marker-bearing sites should not be multiplied into estimates of successfully exploitable live sites without functionality and configuration evidence. Ten trials per condition provide coarse outcome increments and no reported uncertainty. Selecting an effective prompt variant on a subset of tested models can favor those conditions; the paper does not describe a held-out selection evaluation. [D]

The simulation uses one product domain and two known tools. It isolates important variables but cannot reproduce all authorization, rate limiting, moderation, retrieval, or business constraints of deployed systems. UGCBuster's 30-page validation is small and lacks a complete confusion matrix. Tool-hardening reductions lack disaggregated results. Missing plugin versions, model snapshots, seeds, and implementation artifacts restrict exact reproduction. These observations are not presented as author admissions. [D]

## 17. Threats to validity

**Internal validity — analyst assessment:** controlled role and prompt manipulation helps isolate integration effects. However, variant selection and incompletely reported trial protocols limit causal detail. Generic role inference depends on model self-reporting rather than direct logs. Live leakage classification may include paraphrased or generated instruction-like text rather than exact original prompts. [D]

**External validity:** Common Crawl and chosen HTML markers cover only detectable selected plugins. Enterprise products and some paid-only options are excluded. P1 is heavily represented and anchors live configuration measurements. Generalization to browser agents, autonomous multistep systems, other websites, languages, or tool ecosystems requires additional evidence. [D]

**Construct validity:** prompt extraction, Python production, and particular tool calls are operational definitions of success. They capture confidentiality, application scope, and tool-argument integrity, respectively. Review-specific answers indicate data exposure but do not establish actual malicious exploitation. Similarity to a template measures reuse, not a direct security score. [D]

**Statistical conclusion validity:** no significance tests, confidence intervals, or multiple-comparison analysis are reported. Rounded averages and incompatible role support complicate cross-provider aggregation. Zero successes in ten trials is an observed result, not proof of zero underlying vulnerability. [D]

**Ecological validity:** live observations provide grounding, while the simulator deliberately controls content retrieval and attack conditions. Actual attackers may need to overcome posting permission, review moderation, scrape timing, and retrieval relevance; these barriers are not estimated across the deployment population. [D]

**Reproducibility and temporal validity:** configurations and disclosures changed during the study. P1's patch makes historical direct-forgery exposure different from post-disclosure behavior. The paper is not a current vulnerability audit. API model revisions and missing exact versions further limit faithful reruns. [D]

## 18. Future work and open questions

### A. Explicitly proposed directions

The authors leave attacks combining classical web vulnerabilities with LLM exploitation to future research. They call for hardened system-prompt templates, independently hardened tool instructions, and secure customization aligned with specific application threats. Appendix C encourages algorithmic prompt generation and LLM-assisted authoring. The conclusion calls for attention to increasingly integrated custom tools. [A; pp. 6, 11–15, 19]

The supplied meta-review specifically calls for stronger adaptive attacks and defenses resilient to them. Its origin is the committee, not an experiment performed by the authors. [A; p. 20]

### B. Additional open questions — analyst interpretation

How much of the marker-bearing population is currently both functional and exploitable? How accurately can retrieved-content roles be verified without provider logs? How often do poisoned reviews survive moderation and retrieval? Do UGCBuster errors preserve useful trusted content while excluding adversarially disguised UGC? Can tool authorization enforce allowable arguments outside the LLM rather than relying entirely on instructions? How do multistep web agents differ from these customer-service chatbots? [D]

A direct answer to the user's comparative research question would require matched standalone and web-integrated conditions, equivalent attacker objectives, explicit access assumptions, and comparable outcome measures. This paper provides important mechanisms and partial controlled comparisons, not that entire comparative design. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model; the underlying text-generating model |
| API | Application programming interface; a service interface used by plugins and tools |
| WP / WCMS | WordPress / web content management system |
| Plugin | Integration software connecting a website to a configurable chatbot |
| Type 1 / Type 2 | Website-backend mediation / commercial plugin-provider mediation |
| HTTP / WebSocket | Stateless request protocol / stateful bidirectional connection |
| HTML / DOM | Website markup / its structured document-object representation |
| System prompt | Developer instructions defining behavior and constraints |
| S / A / U / T | System / assistant / user / tool message roles |
| Instruction hierarchy | Model-level prioritization based on instruction authority |
| History forgery | Editing browser-supplied conversation history to fabricate authoritative messages |
| RAG | Retrieval-augmented generation; adding query-relevant external knowledge to context |
| DC / FT | Direct copying / fine-tuning |
| SA | System-append mode: attach retrieved material to the existing system prompt |
| SPE | System prompt extraction |
| TaH | Task hijacking; inducing an out-of-scope application task |
| ToH | Tool hijacking; inducing unauthorized tool calls or arguments |
| Context hijacking | Indirectly redirecting the Search tool and displayed result |
| UGC | User-generated content such as reviews or comments |
| UGCBuster | Prototype that identifies UGC containers for filtering or review |
| PII | Personally identifiable information, such as names or contact details |
| CDF | Cumulative distribution function; fraction at or below a score |
| 3-gram | A sequence of three units; the paper does not specify its tokenization |
| Chunk / overlap | A retrieval text segment / repeated text shared by adjacent segments |
| XSS / SQLi / CSRF / RCE | Cross-site scripting / SQL injection / cross-site request forgery / remote code execution |
| CVE | Vulnerability identifier referenced in discussion; records were not independently inspected |
| GDPR / CCPA | Privacy-regulation acronyms mentioned by the authors; no legal verification performed |

The template phrase training data is used loosely in supplied prompts to describe provided information. In a RAG chatbot, retrieved context does not necessarily update model weights. The analysis preserves that distinction. [A/D; pp. 2, 19]

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Selected plugins | 17 | plugins | 7 WP, 10 generic | Author-reported | p. 3 |
| WP search results | 116 | results | Marketplace keyword search | Author-reported | p. 3 |
| WP installation cutoff | 50 | installations | Below cutoff excluded | Author-reported | p. 3 |
| August crawl coverage | 38.3M | domains | Common Crawl archive | Author-reported | p. 3 |
| August chatbot sites | 10,417 | sites | Marker-based, deduplicated | Author-reported | pp. 3–4 |
| April chatbot sites | 17,474 | sites | 5,266 WP; 12,208 generic | Author-reported | pp. 4–5 |
| August→April increase | 7,057; ≈67.7% | sites; percent | 17,474−10,417; divided by 10,417 | Analyst-derived | Table 1, p. 4 |
| Functional sample | 125/200; 62.5% | sites; percent | September 2024 spot-check | Author-reported | p. 4 |
| Automated functionality | 76%; 53%; 96% | percent | P1; P2; P4 | Author-reported | pp. 4–5 |
| P2 high-traffic functionality | 68%; 74% | percent | Top-1M; Top-100K | Author-reported | p. 5 |
| August popular sites | 783; 171 | sites | Top-1M; Top-100K | Author-reported | p. 5 |
| Languages | 93 | languages | Top five cover 81% | Author-reported | p. 5 |
| History-forgery plugins | 8 | plugins | Approx. 8,000 deployments historically | Author-reported | p. 7 |
| Scraping third-party content | 15 | plugins | Local scraper tests | Author-reported | p. 7 |
| System-role retrieved content | 7 | plugins | Table 2 classification | Author-reported | p. 8 |
| Review exposure | 13/100 | sites | Functional P1 e-commerce sample | Author-reported | p. 8 |
| Review permission/display | 41; 36 | sites | Same 100-site sample | Author-reported | p. 8 |
| Live extraction sample | 300 | sites | Randomly selected P1 sites | Author-reported | p. 9 |
| User/system/assistant extraction | 1%; 56%; 55% | percent | Live operational leakage definition | Author-reported | p. 9 |
| Extraction union | 219; 73% | chatbots; percent | At least one successful condition | Author-reported | p. 9 |
| Template overlap/exact copies | 76%; 31% | percent | >80% overlap; exact match | Author-reported | p. 18 |
| Refusal instructions | 97%; roughly 96% | percent | Main text; Appendix C discrepancy | Author-reported | pp. 9, 18 |
| Contact/PII collection | around 5% | percent | Extracted system prompts | Author-reported | p. 18 |
| Activated-tool chatbots | 144 | chatbots | P1, April 2025 | Author-reported | p. 9 |
| Search/calendar/Slack/custom | 43/40/10/42 | chatbots | Categories not established as exclusive | Author-reported | p. 9 |
| Knowledge-base source | 35 | product pages | Nalgene simulation | Author-reported | p. 10 |
| Chunk size/overlap | 600/300 | tokens | text-embedding-3-large embeddings | Author-reported | p. 10 |
| Models/trials/temperature | 11/10/0.5 | models/trials/value | Each supported configuration | Author-reported | pp. 10–13 |
| Insecure TaH means S/A/U | 9.8/5.9/1.0 | successes per 10 | Role denominators differ | Visually readable | Table 3, p. 11 |
| Wrapped hardened indirect T | 0.9 | mean successes per 10 | Eleven-model average | Visually readable | Table 4, p. 12 |
| UGCBuster evaluation | 10×3 | sites×pages | Manual container validation | Author-reported | p. 14 |
| UGCBuster false positives/cost | 1; about $0.05 | case; dollars/page | Small prototype evaluation | Author-reported | p. 14 |
| Tool-hardening reduction | 40–75% | reported reduction | Absolute/relative basis unspecified | Author-reported | p. 14 |
| Template popularity | 33/36/27/4% | percent | Listings 12/13/14/15 | Author-reported | p. 19 |

Approximate source expressions retain their qualifications. No plot-only estimate is used as an exact numerical result.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Plugins can let visitors forge privileged histories | Eight locally examined plugins accept unauthenticated history | T2, F3, X4 | pp. 6–7 | Strong implementation evidence for studied versions; P1 later patched |
| Third-party content enters chatbot knowledge | Fifteen scraper tests; review-specific answers on 13 sampled sites | T2, F4, X4–X5 | pp. 7–8 | Exposure is not measured malicious exploitation |
| Role forgery boosts live extraction | 1% user versus 56% system and 55% assistant | X6 | p. 9 | No live ground-truth prompts; heuristic manual labeling |
| Role restriction helps controlled security | Contrasting S/A/U success counts | T3, X8 | pp. 10–11 | Same simulation, model-specific variation, unequal role support |
| General hardening helps task scope | Lower TaH means with hardened-specific prompts | T3, X8b | p. 11 | Coding-specific protection; not universal robustness |
| General hardening does not secure tools | ToH persists, often at high rates | T3, X8c | p. 11 | Particular Notification tool and chosen attacks |
| RAG insertion affects indirect success | SA/S/A/U/T contrasts | T4, X9 | pp. 12–13 | Tool mode often robust; exceptions prevent universal dominance |
| Lightweight defenses are promising | Container validation; reported hardening reductions | X12–X13 | p. 14 | Small/underspecified evaluations; adaptive security unclear |
| Web integrations add risks beyond text generation | Scraping, role forgery, activated external tools | X4, X7–X9 | pp. 6–13 | Analyst inference; no broad standalone-versus-agent comparison |
| Findings are historically actionable | P1 moves history server-side; P2 adds warnings | Disclosure analysis | pp. 14–15 | Author-reported status at paper time, not current verification |

The first eight rows summarize author findings with source-specific caveats. The ninth is explicitly analyst inference. The tenth is an operational outcome, separate from experimental attack rates.

## 22. Very simple explanation — Explain Like I'm 15

Imagine a website hires an AI sales assistant. The owner gives it rules, customers ask questions, and the assistant reads product information. The model is supposed to know which words came from the owner and which came from a customer. Some plugins let a customer rewrite the apparent conversation and label their own words as if they came from the owner or the assistant. That makes an ordinary attack much more powerful.

A second problem happens when the assistant reads the website. A product review belongs to another customer, so it should be treated cautiously. Some plugins copy reviews together with official product descriptions and give all that text too much authority. A review that contains instructions can then influence the assistant when a different customer asks an innocent question.

The risks grow when the assistant can use tools. An attacker might redirect a search or change where a notification is sent. Telling the assistant to stay focused on sales helps prevent some unrelated tasks, but it does not automatically protect every tool. The software must also preserve message identity, handle outside information carefully, and constrain tool behavior.

This paper shows those problems in selected website chatbots and tests them with several models. It helps explain why web integration can add vulnerabilities to an LLM. It does not prove that every web agent is less secure than every standalone model, and the proposed defenses still need stronger testing.

## Completeness Audit

Coverage is assessed against the supplied inventory, not narrative length. Fully represented means its substantive role and main evidence are explained; compressed means secondary detail or full matrices are deliberately shortened. Text-only pages are explicitly distinguished from visually inspected ones.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes, text and p. 1 image | Yes | Fully represented / compressed metadata | Title retained; authors listed below |
| §1 Introduction and contributions | Yes | Yes | Fully represented | Framing, gap, four contributions |
| §2 LLM background/customization | Yes, text only p. 2 plus p. 3 visual | Yes | Represented in compressed form | Core concepts retained |
| §2 Injection versus jailbreak; plugin prior work | Yes | Yes | Represented in compressed form | Outside references not independently read |
| §3 WP/generic selection and website discovery | Yes | Yes | Fully represented | Exclusions and marker limitations retained |
| §4.1 architecture and protocols | Yes | Yes | Fully represented | Type 1/2; state-management options |
| §4.2 functionality | Yes | Yes | Fully represented | Funnel, failures, automated rates |
| §4.2 growth/popularity | Yes | Yes | Represented in compressed form | Counts, ages, and ranking context |
| §4.2 languages/categories | Yes | Yes | Represented in compressed form | Exact aggregates retained |
| §5 threat model | Yes | Yes | Fully represented | Capabilities, trust, exclusions |
| §5.1 local audit and role inference | Yes | Yes | Fully represented | Five-product majority vote and caveat |
| §5.2 direct history forgery | Yes | Yes | Fully represented | Eight plugins; P7 exception; logging |
| §5.3 indirect injection and exposure | Yes | Yes | Fully represented | Persistence and 100-site audit |
| §6.1 live prompt measurement | Yes | Yes | Fully represented | Labeling, union, ethics, prompt conditions |
| §6.2 tool usage | Yes | Yes | Fully represented | Passive method, counts, exclusions |
| §6.3 model selection | Yes, text only | Yes | Fully represented | Failed cutoff identification preserved |
| §7 experimental setup | Yes, text only p. 10 | Yes | Fully represented | Data, chunks, variants, trials, models |
| §7.1 SPE/TaH/ToH | Yes | Yes | Fully represented | Distinct goals, metrics, conditions |
| §7.2 context hijacking | Yes | Yes | Fully represented | Retrieval, insertion, wrapping, success definition |
| §7.3 takeaways | Yes | Yes | Fully represented | Conditions and exceptions retained |
| §8.1 additional weaknesses | Yes | Yes | Represented in compressed form | Plaintext prompts, API key, privacy |
| §8.2 mitigations | Yes, partly text only | Yes | Fully represented | State integrity, UGC filtering, tool hardening |
| §8.3 distribution shift | Yes, text only | Yes | Fully represented | Author interpretation distinguished |
| §9 conclusion/disclosures | Yes, text only | Yes | Represented in compressed form | Historical fixes and nonresponses |
| §10 acknowledgements | Yes, text only | Yes | Inspected but compressed as non-technical | Funding summarized below |
| References 1–78 | Yes, partial visual / full text | Yes | Inspected but deliberately compressed | Bibliography not independently validated |
| Formal research questions/hypotheses | Checked | Yes | No formal items identified | Informal objectives distinguished |
| X1–X13 analyses | Yes | Yes | Fully represented / compressed results | All distinct analysis families accounted for |
| Figure 1 | Yes, visual | Yes | Fully represented | Communication components and flows |
| Figure 2, both panels | Yes, visual | Yes | Fully represented | Exact versus unlabeled values distinguished |
| Figure 3, three paths | Yes, visual | Yes | Fully represented | Attack-request and output mechanism |
| Figure 4 | Yes, visual | Yes | Fully represented | Illustrative review attack |
| Figure 5, both panels | Yes, visual | Yes | Represented in compressed form | Individual unlabeled bars not estimated |
| Figure 6 | Yes, visual | Yes | Fully represented | CDF axes, metrics, exact textual findings |
| Table 1 | Yes, visual/text | Yes | Fully represented | All displayed numerical cells transcribed |
| Table 2 | Yes, visual/text | Yes | Represented in compressed form | All plugin rows; logging footnotes in prose |
| Table 3 | Yes, visual/text | Yes | Represented in compressed form | Overall means and diagnostic model cells; full matrix omitted |
| Table 4 | Yes, visual/text | Yes | Represented in compressed form | Overall means and exceptions; full matrix omitted |
| Major equations/theorems | Checked | Yes | No substantive numbered items identified | Analyst formulas explicitly labeled |
| Formal algorithms/pseudocode | Checked | Yes | None supplied | UGCBuster prose workflow represented |
| Appendix A, Listings 1–11 | Yes, visual/text | Yes | Represented in compressed form | Roles, targets, triggers, tool template; payloads not fully repeated |
| Appendix B | Yes, visual/text | Yes | Fully represented | Relative findings; detailed results absent |
| Appendix C and C.1, Listings 12–16 | Yes, p. 19 text only | Yes | Represented in compressed form | Similarity, PII, refusals, popularity, coding prohibition |
| Appendix D, D.1–D.4 | Yes, text only | Yes | Fully represented | Committee contribution and adaptive-defense concern |
| Supplied supplementary material | None | Accounted for | Not supplied | No claim of review |
| Major contributions and stated limitations | Yes | Yes | Fully represented | Priority claims unverified externally |

### Additional inventoried details retained in compressed form

The original title is **When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins**. Authors are Yigitcan Kaya, Anton Landerer, Stijn Pletinckx, Michelle Zimmermann, Christopher Kruegel, and Giovanni Vigna, affiliated with the University of California, Santa Barbara. Page 1 states acceptance to IEEE Symposium on Security and Privacy 2026 and shows arXiv:2511.05797v1, dated 8 November 2025. Copyright and contact details are bibliographic/administrative material, not experimental evidence. [A]

The domain-age analysis reports almost 35% older than a decade and 20% registered within two years. Beyond popular sites, more than 80% of domains ranked between Top-1M and Top-3M are older than five years, with nearly 50 .gov/.edu domains active beyond Top-1M. These contextual observations support deployment diversity, not measured exploitability. [A; p. 5]

Additional weaknesses include plaintext system prompts in P7/P8/P16/P17; an exposed API key in P12; and observed leakage of email addresses and past customer-service interactions without a reported prevalence. P12's browser-to-provider exception qualifies the general type 1 backend architecture. Disclosure began in October 2024; four developers responded within three days. P1 moved state server-side and adopted hardened prompts by December; P2 added warnings while retaining vulnerable workflows. P7 fixed visible prompts, and P12's API-key issue was only partially patched. Indirect risks disclosed to P1/P2 were not mitigated as reported. [A; pp. 13–15]

The authors describe ethical precautions: contact-bearing User-Agent, an informational scanning-IP website and DNS record, opt-out mechanisms, internal-only collected data, and temporary interactions without persistent site changes apart from dashboard logs. Acknowledgements name fellowship and research support, including NSF grant 2229876, DHS, and IBM; these do not establish scientific correctness. [A; pp. 9, 15]

### Missing or inaccessible material

No numbered main-document page is missing from the supplied text. Visual renderings for pp. 2, 10, 14–16, 19, and 20 are absent. No code, raw logs, detailed trial outputs, exact plugin versions, model snapshots, random seeds, full variant-selection records, or separate supplementary files are supplied. Native text length and embedded-image metadata do not independently prove that every PDF object was captured.

### Uncertain interpretations

Unresolved items include the 97% versus roughly 96% refusal statistic; prose/table differences for user task hijacking and user tool hijacking; the broad SA-vulnerability example involving GPT-4.1; whether reported defense reductions are relative percentages or percentage points; the precise 3-gram construction and embedding model; generic-plugin role inference under noncompliance; and whether live instruction-like output exactly matches original prompts. Figure 2 registration binning is not explicitly defined. Listing 8's extracted tag characters are corrupted, although the image makes the intended tool-block structure understandable.

### Deliberately compressed material

Full model-by-condition matrices in Tables 3–4 are represented by all overall averages, provider-support caveats, selected diagnostic entries, and counterexamples. Individual unlabeled bar heights and line points are not estimated. Prompt payloads and templates are explained by function rather than copied in full. Bibliographic entries, repetitive examples, administrative notices, and funding details are compressed. These choices preserve substantive distinctions while avoiding a transcription of the document.

### Potential omissions

No known major section, substantive figure, table, appendix, or distinct analysis family in the supplied inventory is left entirely unrepresented. Some fine-grained numerical cells, exact payload wording, individual bibliography details, and unlabeled graphical values are deliberately omitted or compressed as disclosed above. The report is source-grounded analysis of supplied material; it is not a full artifact-level reproduction, an independent security validation, or a direct comprehensive comparison of web agents with standalone LLMs.
