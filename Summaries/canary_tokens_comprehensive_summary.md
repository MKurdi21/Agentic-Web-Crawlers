# Identifying AI Web Scrapers Using Canary Tokens

**Authors:** Steven Seiden, Triss Ren, Caroline Zhang, Taein Kim, Enze Liu, and Emily Wenger

## 1. Background and Context

Large language models and AI chatbots use web-scraped information in two main ways:

1. During pre-training and fine-tuning, large collections of web content teach models general language and knowledge.
2. During inference—when answering a user—they may retrieve external web content to obtain current or more accurate information.

Inference-time retrieval can use either:

- **Pre-indexed content:** Material previously collected by a proprietary crawler or a third-party search engine and stored in an index or cache. Relevant passages are supplied to the model through retrieval-augmented generation (RAG).
- **On-demand retrieval:** A crawler visits a webpage while the chatbot is generating its answer.

This matters because training alone does not give chatbots knowledge of events after their training cutoff and does not eliminate hallucinations. Web retrieval helps address those limitations, and many chatbot providers advertise search capabilities. At the same time, large-scale scraping can increase bot traffic, disrupt services, and create privacy, copyright, legal, and ethical concerns.

Website owners may try to control scraping through mechanisms such as `robots.txt`. The Robots Exclusion Protocol lets a site list which self-reported User-Agents should or should not crawl it, but it is a voluntary request rather than a technical barrier. Scrapers may ignore directives, selectively comply, or conceal themselves behind ordinary browser User-Agents. More aggressive defenses can return errors such as HTTP 403, serve CAPTCHAs or decoy pages, or manipulate content so it is less useful to models.

Most earlier anti-AI-scraping work focused on preventing material from entering training datasets—for example, Fawkes, Glaze, and Nightshade manipulate images to make them unsuitable for unauthorized model training. Other work studies consent signals, `robots.txt` adoption, or webpage manipulations that interfere with information extraction. Much less was known about scraping performed for query-time chatbot retrieval.

Existing methods for identifying AI crawlers mainly use:

- Providers’ voluntary disclosures;
- Community-maintained crawler lists;
- One-off measurements by researchers or practitioners.

These sources can be incomplete, outdated, erroneous, or vulnerable to User-Agent spoofing. They also do not reveal the complete chain through which a third-party search crawler may collect information that later appears in another company’s chatbot.

**Figure 1** presents the underlying content flow. A website owner first publishes information after a model has been trained. A user later asks a chatbot about that information. The chatbot either retrieves a previously indexed webpage or scrapes the website directly, parses the retrieved content, and incorporates it into its response. Consequently, an answer may mix knowledge acquired during training with information retrieved at query time.

## 2. Research Goal and Objectives

The paper’s main goal is to develop and evaluate an automatic way for an ordinary third party to infer which web scrapers supply content to production AI chatbots, without trusting the scrapers’ claimed identities.

It asks three research questions:

- **RQ1:** Which User-Agents do AI chatbots use to obtain web content when generating responses?
- **RQ2:** How do chatbots obtain that content—through live retrieval, caches, or both?
- **RQ3:** Can simple blocking measures, specifically taking a site offline or disallowing bots through `robots.txt`, affect the content returned by chatbots?

The authors also seek to determine whether providers’ public descriptions of their crawlers match observable behavior and whether content continues to appear after a website owner attempts to withdraw access.

## 3. Methods (Approach/Design)

### Canary-token attribution

The paper introduces **canary tokens**: distinctive pieces of otherwise ordinary website content that are customized for each visiting scraper. The central observation is that content shown to a crawler may later reappear in a chatbot response. A chatbot’s output can therefore act as an attribution side channel.

**Figure 2** illustrates the three-step pipeline:

1. **Deploy tokenized websites:** Each scraper receives a distinct version of a webpage. For example, one visitor might see that Alice is from “New York” and likes “ice cream,” while another sees “Los Angeles” and “pie.”
2. **Query chatbots:** The researchers ask each chatbot about Alice or the equivalent fictitious entity.
3. **Infer the scraper:** If the response says “New York” and “ice cream,” it is linked to the scraper that received those values; “Los Angeles” and “pie” points to the other scraper.

### Websites and infrastructure

The researchers purchased **20 `.com` domains** with no recent ICANN history and hosted them on Google Cloud. The sites imitated common website types, such as company sites and artists’ portfolios.

Each website:

- Used a hand-written template rather than model-generated text;
- Contained **10 canary-token placeholders**, distributed throughout the page to reduce the effect of stripping or truncation;
- Described benign, fictitious entities;
- Avoided overlap with real people or organizations;
- Used fictitious phone numbers, educational institutions, and other details.

An example template says that Alice is from token `CT1` and likes token `CT2`. Values were generated with Python’s Faker library and random-number generation.

The researchers encouraged discovery by:

- Submitting the sites to Google and Bing webmaster tools;
- Following Brave Search’s indexing process, including form submission and repeated visits;
- Placing hidden links to all 20 domains on other sites they controlled.

### Defining a distinct scraper

A scraper identity was defined as a unique pair:

\[
(\text{User-Agent},\ \text{Autonomous System Number})
\]

The ASN identifies the network from which the request originated. Visitors with the same User-Agent and ASN were treated as the same scraper and consistently received the same token set. New pairs received fresh tokens.

The authors chose this definition as a balance between simplicity and granularity. The method could instead incorporate IP ranges, TLS fingerprints, browser fingerprints, or behavioral signals.

### Token generation and quality control

The smallest token-value space contained **4,761 possible values**. Sites averaged **592 unique User-Agent/ASN pairs**, making collisions relatively unlikely.

Nevertheless, the researchers detected several ambiguities:

- The same value was occasionally assigned to different visitors.
- A value could represent different variables for different visitors, such as one person’s name versus another person’s parent.
- One token could be a substring of another, such as “Port” within “West Port.”
- Numbers and dates could coincide with unrelated chatbot output.
- Chatbots sometimes rounded numerical values.

They conservatively discarded all ambiguous assignments, substring-based matches, and numerical-token matches rather than resolving them manually.

### Prompting the chatbots

Because the systems were black boxes, the researchers tested prompts on pilot websites outside the main experiment. They selected a two-query interaction intended to encourage complementary retrieval behavior:

1. The first query asked the chatbot to search the internet for detailed information about a named fictitious person or company.
2. A follow-up asked whether variant websites, discrepancies, or more recent information existed.

Every prompt contained:

- A description of the target entity without revealing its tokens;
- Instructions about which sources to search;
- Questions corresponding to tokenized variables;
- Formatting rules to simplify extraction, including English output, dates in `YYYY-MM-DD`, phone numbers in `XXX-XXX-XXXX`, and numbers without comma separators.

Appendix C shows a full ChatGPT interaction. ChatGPT reproduced numerous tokenized biographical details, cited the experimental site, and later said that no conflicting or more current source was available.

### Token extraction and scraper matching

The authors extracted tokens using hand-written regular expressions and text-matching rules. Each extracted token was mapped back to the User-Agent/ASN pair that received it.

For chatbot \(\ell\) and scraper \(s\), they counted:

- \(T_\ell(s)\): total tokens in the chatbot’s responses associated with that scraper;
- \(W_\ell(s)\): distinct website-query interactions in which that scraper was observed.

A scraper-chatbot match was accepted when either:

- At least **two associated tokens** were found, or
- Evidence appeared across more than **one website interaction**.

The implementation used thresholds \(t=2\) and \(w=1\), with the practical intent of rejecting a scraper identity supported by only one token from one website. The equation in the extracted paper refers once to \(F_\ell(s)\), although the preceding definition names this quantity \(W_\ell(s)\); the text does not resolve this notation inconsistency.

### Robustness

Potential false positives include a chatbot hallucinating a token or retrieving a similarly named real entity. Each token came from a space of at least \(10^3\) values, giving an incidental single-token probability on the order of \(10^{-3}\) and a two-token collision probability on the order of \(10^{-6}\). With 10 independently selected tokens assigned to a scraper, the probability that all matches are accidental decreases exponentially.

False negatives can arise when content is truncated, a model omits a value it received, generation randomness suppresses it, or a chatbot’s presentation policy excludes it. Multiple websites and repeated query rounds increase the chance of collecting sufficient evidence. These failures reduce coverage but do not, according to the authors, create incorrect positive attributions.

### Chatbot sample

The study tested **22 production chatbots**:

- ChatGPT
- Claude
- Copilot
- Deepseek
- Duck.ai
- ERNIE
- Gemini
- GLM
- Granite
- Grok
- Hunyuan
- Kimi
- Liquid
- Llama
- Mistral
- Nova
- Perplexity
- Qwen
- Reka
- Solar
- Step-3
- Venice

They were selected from systems with web-search capabilities listed on LMArena and OpenRouter, supplemented with products such as Microsoft Copilot that place proprietary search infrastructure around another company’s model.

Queries were submitted through web-search-enabled APIs when possible. Otherwise, the team automated web interfaces with Selenium or `nodriver`; systems resistant to automation were queried manually. Every tailored query for each of the 20 sites was sent to every chatbot in all experimental conditions, and responses were stored in a database.

### Experimental conditions and timeline

The experiment covered several months and used three accessibility conditions:

- **Condition 1—Fully accessible:** Sites remained online in their default configuration.
- **Condition 2—Offline:** Previously accessible sites were taken down.
- **Condition 3—Blocked:** Sites remained online, but `robots.txt` disallowed all bots.

**Figure 3** shows three stages:

1. All 20 sites remained online for **two months**, after which all chatbots were queried once.
2. Ten sites were taken offline and the other ten received restrictive `robots.txt` files. Both groups were queried after **one week** and again after **two weeks**.
3. All sites were restored and the restrictions removed. Chatbots were queried after **one week** and again after **two weeks**.

The two-month initial wait reflected anecdotal evidence that sites of this size may take up to six weeks to propagate through online indexes.

### Visitor volume

**Table 2** shows that the sites received substantial crawler traffic:

| Statistic | User-Agents | ASNs | Unique User-Agent/ASN visitors |
|---|---:|---:|---:|
| Minimum across sites | 313 | 154 | 313 |
| Maximum across sites | 477 | 226 | 674 |
| Mean per site | 405.95 | 192.4 | 592.2 |
| Across all sites | 2,765 | 549 | 4,042 |

The least visited site had 313 unique pairs and the most visited had 674. SEO treatment, styling, and length were similar, so content subject matter was the main stated difference among sites.

## 4. Results and Findings

### 4.1 Mapping chatbots to scrapers

The method elicited attributable tokens from **18 of 22 systems**. Deepseek, Hunyuan, GLM, and Liquid did not return information about the experimental sites and were excluded from scraper mapping. Failure to observe tokens does not prove that these systems never accessed the sites.

The researchers grouped observed agents into:

- **First-party declared agents:** Consistent with the provider’s documentation;
- **Third-party search agents:** Search-engine crawlers operated outside the chatbot provider;
- **Generic browser agents:** Requests presenting themselves as ordinary browsers or other applications.

#### Known first-party agents

The study found **10 User-Agent strings** belonging to publicly declared first-party agents. Examples include:

- ChatGPT — `OAI-SearchBot`
- Copilot — `Bingbot`
- Duck.ai — `DuckAssistBot`
- ERNIE — `Baiduspider`
- Gemini — `Googlebot`
- Granite — `GranitePlayground`
- Llama — `meta-externalagent` and `meta-webindexer`
- Nova — `Amazonbot`
- Perplexity — `PerplexityBot`

These expected matches served as a validation of the canary-token approach.

#### Generic browser identities

Six of the 18 attributable systems returned content linked to generic browser-like agents. The narrative identifies ERNIE, Grok, Solar, Qwen, and Kimi as notable examples; Table 3 also records generic-browser observations for Reka.

- **ERNIE:** Chrome in the online baseline, plus Baiduspider under later conditions.
- **Grok:** Googlebot, Chrome, and Safari.
- **Qwen:** Googlebot and Chrome.
- **Reka:** Googlebot and Chrome.
- **Solar:** Chrome, Safari, Firefox, and Edge; no first-party crawler was identified.
- **Kimi:** A particularly large, diverse set of browser/application identities.

**Table 4** groups Kimi’s measured identities as Chrome, Edge, Googlebot, Obsidian, Qaxbrowser, QQBrowser, QuarkPC, SLBrowser, and WindowsWechat. The authors infer that Kimi may rotate through many User-Agent strings, possibly to evade bot detection.

#### Reliance on third-party search crawlers

Content linked to Googlebot, Bingbot, or Bravebot appeared in **10 of the 18 attributable systems**. Examples include:

- Claude, Mistral, and Venice — Bravebot;
- Copilot — Bingbot;
- Gemini, Grok, Perplexity, Qwen, Reka, and Step-3 — Googlebot.

Some relationships were documented, such as Claude’s use of Brave. Others, including Perplexity and Qwen returning Googlebot-associated content, were not publicly documented.

The researchers checked the ASNs for these visits and found that the traffic originated from the expected search companies’ networks. They therefore interpret these observations as chatbots ingesting search-engine results rather than unrelated scrapers merely spoofing search User-Agents.

This creates an indirect supply chain: blocking a known AI crawler may not stop a chatbot that receives the site through a search index. A site might have to leave conventional search indexing entirely, sacrificing discoverability.

#### Stage 1 token evidence

Appendix Table 9 reports baseline evidence in greater detail:

- ChatGPT/OAI-SearchBot: **68 tokens across 11 sites**
- Claude/Bravebot: **88 across 20**
- Copilot/Bingbot: **57 across 17**
- Duck.ai/DuckAssistBot: **56 across 9**
- ERNIE/Chrome: **6 across 1**
- Gemini/Googlebot: two observed versions, **78 across 12** and **43 across 6**
- Granite/GranitePlayground: **75 across 12**
- Grok/Googlebot: **1,130 across 129 listed website visits**, and Chrome: **20 across 5**. The value 129 exceeds the study’s 20 sites and is reproduced as printed; the paper does not explain it.
- Llama/meta-externalagent: **46 across 9**; `meta-webindexer`: **91 across 1**
- Mistral/Bravebot: **66 across 19**
- Nova/Amazonbot: **81 across 15**
- Perplexity/PerplexityBot: **110 across 17**; two Googlebot versions: **10 across 7** and **6 across 4**
- Qwen/Googlebot: **103 across 20**
- Reka/Googlebot: **56 across 10** and **52 across 8** for two versions
- Solar/Chrome: **29 across 1**; Safari: **2 across 1**; Firefox: **2 across 1**
- Venice/Bravebot: **63 across 17**

Kimi’s individual identities generally appeared on only one site each, but collectively covered numerous Chrome, Edge, Googlebot, application-browser, and WindowsWechat variants.

Appendix Table 10 enumerates **39 exact Stage 1 User-Agent strings**, including declared crawler strings and many platform-, browser-, version-, and application-specific strings. The main analysis appropriately aggregates these long strings into families.

**Answer to RQ1:** Chatbots vary substantially. Some use declared first-party agents, some use browser-like identities, and many obtain information through third-party search crawlers rather than directly visiting the source site.

### 4.2 Persistence and caching after sites went offline

After the initial period, ten sites were taken offline. Many chatbots continued returning their tokenized information one and two weeks later.

For third-party search-backed systems, content remained available after one week offline for **seven of the eight chatbots** that had ingested content through Googlebot, Bingbot, or Bravebot. This is consistent with search engines retaining indexed copies after the original page becomes unreachable.

Persistence also occurred for generic browser agents:

- Grok continued returning Chrome-associated information;
- ERNIE continued returning Chrome-associated information;
- Solar continued returning Chrome-associated information.

Thus, persistence was not limited to third-party search indexes. Some content retrieved through browser-like agents also remained available after the source disappeared.

ERNIE showed an unusual transition. In the online baseline, the study observed Chrome but not Baiduspider. Once the sites were offline, it observed Baiduspider-associated content. The authors offer two possible explanations:

1. Baiduspider was present initially but the prompts failed to elicit it.
2. ERNIE prefers a browser-like retrieval path while a site is live and falls back to Baidu’s search index once it is unavailable.

Table 5 tracks observations over baseline, one and two weeks offline, and one and two weeks after restoration. Persistent agents across all or nearly all checkpoints included OAI-SearchBot, Bravebot for Claude, Bingbot, Googlebot for Gemini and Grok, Bravebot for Mistral and Venice, PerplexityBot and Perplexity’s Googlebot source, Qwen’s Googlebot, and Reka’s Googlebot. Some less persistent identities reappeared after restoration, while others were observed only at isolated checkpoints.

**Answer to RQ2:** Caching or retention is common. Many systems returned the sites’ content after at least one week offline, whether it had originally arrived through a search crawler, first-party agent, or browser-like agent.

### 4.3 Effectiveness of taking sites offline and using `robots.txt`

The third research question focused on **post-scraping controls**: content had already been collected before the owner withdrew access.

Of the 18 systems with attributable evidence, **12 continued returning content in both blocking conditions**—offline and restricted by `robots.txt`. Therefore, neither measure reliably removed already scraped information from chatbot answers.

The study observed slightly more User-Agent families in the `robots.txt` condition than in the offline condition. This is consistent with the possibility that some systems bypassed the restriction, but it is not proof. Differences in elicitation, cache state, retrieval routes, and other confounders could produce the same pattern.

**Duck.ai was the only measured chatbot that stopped returning the experimental content under both offline and `robots.txt` restrictions.** The authors infer that it likely considers signals such as current site availability and crawler directives before deciding whether to return stored content.

Table 6 shows substantial persistence during and after `robots.txt` blocking. OAI-SearchBot, Claude’s Bravebot, Bingbot, Gemini’s Googlebot, Grok’s Googlebot and Chrome agents, Mistral’s Bravebot, Nova’s Amazonbot, Qwen’s Googlebot and Chrome agent, and Venice’s Bravebot were among the identities seen repeatedly. Bold marks in the original table identify agents observed under `robots.txt` that had not appeared in the corresponding offline condition.

**Answer to RQ3:** Taking a site offline or adding a universal `robots.txt` prohibition after scraping is generally ineffective at preventing chatbots from returning its content.

### 4.4 Token filtering

Appendix Table 7 quantifies the conservative filtering applied at each checkpoint:

| Checkpoint | Tokens found | Numerical confusions | Subset confusions | Token overlaps | Below threshold | Total discarded |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 2,325 | 618 | 102 | 207 | 1 | 928 |
| 1 week offline | 797 | 229 | 39 | 66 | 2 | 336 |
| 2 weeks offline | 585 | 221 | 22 | 60 | 2 | 305 |
| 1 week back online | 1,097 | 314 | 70 | 91 | 4 | 479 |
| 2 weeks back online | 1,262 | 363 | 72 | 113 | 7 | 555 |
| 1 week blocked | 1,366 | 356 | 82 | 186 | 3 | 627 |
| 2 weeks blocked | 1,192 | 327 | 76 | 137 | 0 | 540 |
| 1 week post-block | 1,465 | 400 | 85 | 178 | 9 | 672 |
| 2 weeks post-block | 1,506 | 432 | 96 | 186 | 2 | 716 |

These exclusions reduce sensitivity but make the retained scraper associations more conservative.

## 5. Analysis and Interpretation

The results show that the path from a webpage to a chatbot answer is often indirect and difficult for site owners to observe.

First, matching expected agents such as OAI-SearchBot, Bingbot, Bravebot, and other declared crawlers supports the validity of the canary-token method. The same method also reveals undeclared or unexpected routes, including ordinary-looking browsers and third-party search indexes.

Second, a chatbot can incorporate content from multiple scraping sources. A single provider may use a declared crawler, a generic browser agent, and a search-engine index. This explains why blocking only a provider’s documented bot may fail.

Third, User-Agent-based controls have a structural weakness. User-Agent strings are self-reported, and some retrieval traffic looks like ordinary browser use. Kimi’s many browser and application identities are the clearest case. Even truthful bot identification is insufficient when the actual collector is a third-party search engine whose index later feeds the chatbot.

Fourth, removing access does not necessarily remove data already collected. Continued responses after one or two weeks offline indicate that both chatbot providers and search services can retain content. The experiment does not determine exact cache locations or retention durations, but it establishes that “real-time” content retrieval can include non-live, cached information.

Fifth, the comparison between offline and `robots.txt` conditions does not establish that particular crawlers violated the protocol. Continued output could reflect prior caching rather than a new prohibited visit. The paper therefore distinguishes the practical result—content remains available—from the unresolved mechanism.

These findings raise broader questions about consent and responsibility. Data collection and chatbot use may be performed by different organizations, complicating copyright, privacy, and consent analysis. Preferences expressed to the original collector may not automatically follow the data through downstream indexes and chatbot systems.

## 6. Contributions and Novelty

The paper makes several main contributions:

- It introduces a **canary-token method** for linking content in chatbot answers to particular User-Agent/ASN scraper identities without trusting the crawler’s claimed purpose.
- It demonstrates the method across **20 controlled websites and 22 production chatbots**.
- It successfully obtains scraper evidence for **18 systems**, including expected first-party agents and previously undocumented retrieval routes.
- It shows that some chatbots retrieve information through **generic browser identities**, making ordinary User-Agent blocking difficult.
- It exposes widespread dependence on **third-party search crawlers**, including relationships not publicly documented.
- It experimentally demonstrates that cached web content often remains available to chatbots after the source site is taken offline.
- It shows that post-scraping measures such as taking a site offline or adding restrictive `robots.txt` directives generally do not prevent already collected content from appearing in answers.
- It offers a technique that publishers, bot-detection vendors, and infrastructure providers could deploy to improve monitoring and blocking.
- It provides anonymized aggregated data, an example tokenized website, and a ChatGPT interaction script through the authors’ public code repository.

## 7. Limitations and Caveats

The authors identify several limitations:

- Only **20 websites** were used.
- Queries came from a single geographic and network vantage point: a U.S. university campus.
- Providers may use different retrieval infrastructure for different sites, content types, or locations.
- The method requires a chatbot to emit enough tokens. Scrapers can be missed when content is truncated, not surfaced by the chatbot, or not retrieved during the observation window.
- Results depend on the chosen prompts, websites, experimental timing, and observation period.
- The study’s relatively short duration likely emphasizes inference-time retrieval rather than scraping for model training.
- A User-Agent/ASN pair is a deliberately simple identity definition and may merge or split infrastructure imperfectly.
- Ambiguous, numerical, substring, and colliding tokens were discarded. This improves reliability but can increase false negatives.
- The experiment cannot always distinguish cached results from fresh crawling. Consequently, continued content under `robots.txt` does not prove that a crawler ignored the directive.
- The authors do not determine the exact location, age, or retention policy of caches.
- Four chatbots yielded no attributable tokens, so the study cannot characterize their retrieval paths.
- Scaling canary tokens could affect user experience.
- Adversarial crawlers might attempt to detect tokens or evade attribution by rotating User-Agents.
- The study covers textual webpages only.

There are also source-level caveats: the matching equation uses \(F_\ell(s)\) where the associated quantity is defined as \(W_\ell(s)\), and one Stage 1 table reports 129 website visits for a Googlebot/Grok association despite the experiment containing 20 sites. These appear in the supplied text without clarification.

## 8. Future Work or Open Questions

The authors propose several extensions:

- Enrich scraper fingerprints with IP ranges, TLS fingerprints, browser fingerprints, and behavioral characteristics.
- Deploy more websites, use more geographic vantage points, and observe systems for longer periods.
- Apply the approach over model-development timescales to investigate scraping for training, not only inference-time retrieval.
- Measure operational properties such as cache-retention periods and the speed with which chatbots incorporate newly published information.
- Adapt canary attribution to images, audio, and video.
- Develop tokens that remain unobtrusive to human visitors and robust against adversarial detection or rotating User-Agents.
- Study how consent and usage preferences can be preserved, verified, and enforced when data moves among website crawlers, search engines, indexes, and chatbot providers.
- Examine ongoing efforts to expand `robots.txt` so website operators can express AI collection and usage preferences, while addressing how those preferences propagate through multi-party supply chains.

## 9. High-Level Takeaway (Plain Language)

The researchers gave every web crawler a slightly different version of the same fictitious websites, then checked which version appeared in chatbot answers. This let them trace chatbot content back to particular crawlers. Across 22 chatbots, they found that some used their advertised bots, others looked like ordinary browsers, and many relied on Google, Bing, or Brave search crawlers. Once information had been collected, taking a site offline or blocking bots through `robots.txt` usually did not stop chatbots from repeating it. The study therefore shows that AI web retrieval is more indirect and persistent than public crawler lists suggest, making meaningful control over scraped content difficult.