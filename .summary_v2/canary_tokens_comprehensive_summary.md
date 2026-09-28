# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes. Complete page-labeled text for pages 1–19 was supplied. |
| Accessible page range | 1–19. |
| Apparently missing pages | None. |
| Visually rendered pages | Pages 1–12 and 16–18. |
| Pages not visually rendered | Pages 13–15 and 19. Their native extracted text was supplied, but their visual layout was not independently inspected. |
| Figures | Figures 1–3 were visually inspected on rendered pages 3, 5, and 8. |
| Tables | Tables 1–10 are available through extracted text. Tables 1–10 were also visually rendered except that Table 10 continues onto unrendered page 19; its final rows remain available as native text. |
| Equations | Equation (1) is visible on rendered page 6. It contains a likely notation inconsistency discussed below. |
| Appendices | Appendices A–D are present on pages 14–19. |
| Supplementary material | No separate supplementary file was supplied. Appendix B refers to an external code/data repository, but it was not inspected under closed-document mode. |
| OCR requirement | None indicated: every page has native extracted text. OCR-sensitive notation was nevertheless checked against the rendered equation where possible. |
| Embedded images | One embedded image was mechanically detected on page 3; the rendered page shows Figure 1. |
| Truncation | No textual page appears truncated. The visual rendering set omits pages 13–15 and 19. |
| Important access limitation | The paper repeatedly refers to “Conference’17, July 2017,” but its arXiv mark says version 1, 13 May 2026 (p. 1). The supplied material does not establish whether “Conference’17” is a template placeholder or actual venue information. |
| Source boundary | Closed-document mode. Everything below is based only on the supplied paper and page images. No external facts or validation are introduced. |

# 1. Plain-Language Orientation

This is an empirical computer-security and web-measurement paper about identifying which automated web visitors supply information to commercial artificial-intelligence chatbots.

The underlying difficulty is attribution. A website owner can see visitors’ self-reported **User-Agent** strings, but those strings may be incomplete, misleading, generic, or spoofed. Conversely, when a chatbot answers a question using a website, the owner ordinarily cannot tell which crawler collected that information or whether the chatbot obtained it directly, through a search engine, or from a cache.

The authors introduce a controlled tracing technique based on **canary tokens**. They created 20 fictitious websites, each containing 10 information fields. The server presented different field values—such as a different hometown or favorite food—to each distinct visitor, identified by its User-Agent and Autonomous System Number (ASN). The researchers then asked 22 production chatbots questions whose answers required those fields. If a chatbot repeated values shown only to one visitor identity, those values linked the chatbot’s answer to that visitor.

The principal author-reported findings are:

- The method elicited identifiable scraper evidence for 18 of 22 chatbots (§5.1, p. 10).
- Ten observed User-Agent strings were already declared by their associated providers, supporting the method’s face validity (§5.1, p. 10).
- Six of the 18 observable systems returned content tied to generic-browser User-Agents (§5.1, p. 10).
- Ten of those 18 returned content tied to Googlebot, Bingbot, or Bravebot, showing substantial reliance on third-party search infrastructure (§5.1, p. 10).
- Seven of eight chatbots tied to those search crawlers still returned the content after sites had been offline for one week (§5.2, p. 10).
- Twelve of the 18 observable chatbots continued returning content under both the offline and restrictive-`robots.txt` conditions (§5.3, p. 12).
- Duck.ai was the only measured chatbot that stopped returning the content in both blocking conditions (§5.3, p. 12).

The central contribution is methodological: the chatbot’s output becomes an **attribution side channel**. Distinct content variants allow an unprivileged website operator to infer which observed visitor supplied data to which chatbot, without trusting the visitor’s claimed organizational identity (§3, pp. 4–6).

# 2. Document Roadmap

The document is an empirical security/systems measurement paper with the following inventory:

| ID | Original location | Content |
|---|---|---|
| S1 | Abstract, p. 1 | Problem, canary-token method, 22-system study, broad claims. |
| S2 | §1, pp. 1–2 | Motivation, contributions, headline findings. |
| S3 | §2, pp. 2–4 | Background and related work. |
| SS3.1 | §2.1 | Training-time versus inference-time scraping; cached and live retrieval. |
| SS3.2 | §2.2 | Existing crawler-identification methods; RQ1 and RQ2. |
| SS3.3 | §2.3 | Blocking and content-control methods; RQ3. |
| S4 | §3, pp. 4–6 | Canary-token attribution method. |
| SS4.1 | §3.1 | Website templates, token assignment, visitor identity. |
| SS4.2 | §3.2 | Two-prompt chatbot-query procedure. |
| SS4.3 | §3.3 | Token extraction and formal matching rule. |
| SS4.4 | §3.4 | False-positive and false-negative analysis. |
| S5 | §4, pp. 6–8 | Experimental implementation. |
| SS5.1 | §4.1 | Domains, hosting, indexing, token generation and filtering. |
| SS5.2 | §4.2 | Selection and querying of 22 chatbots. |
| SS5.3 | §4.3 | Three accessibility conditions and timeline. |
| S6 | §5, pp. 9–12 | Results. |
| SS6.1 | §5.1 | RQ1: mapping chatbots to scrapers. |
| SS6.2 | §5.2 | RQ2: persistence/caching. |
| SS6.3 | §5.3 | RQ3: offline and `robots.txt` blocking. |
| S7 | §6, pp. 12–13 | Limitations, implications, and future work. |
| A1 | Appendix A, p. 14 | Ethical considerations. |
| A2 | Appendix B, p. 14 | Open-science repository description. |
| A3 | Appendix C, pp. 14–15 | Complete example ChatGPT interaction. |
| A4 | Appendix D, pp. 15–19 | Tables 7–10. |

Substantive objects comprise three figures, ten tables, one numbered equation, three explicit research questions, three main experimental stages, and no pseudocode, theorem, lemma, formal hypothesis, or inferential statistical test.

# 3. Background and Context

A **web scraper** is an automated program that retrieves web content (§2.1, p. 2). A **User-Agent** is an HTTP header string through which a browser or bot describes itself (§2.2, p. 3). The declaration is not enforced; a client can use a generic or misleading string.

An **Autonomous System Number (ASN)** identifies the network organization associated with traffic. The paper treats `(User-Agent, ASN)` as a visitor identity (§3.1, p. 5).

Web data reaches chatbots in two broad phases (§2.1, p. 2):

1. **Training time:** scraped pages form part of pre-training or fine-tuning corpora.
2. **Inference time:** a deployed chatbot consults external web data while answering.

Inference-time access may use:

- a previously constructed index or cache, incorporated through **Retrieval-Augmented Generation (RAG)**; or
- an on-demand scraper that fetches a page during response generation.

The **Robots Exclusion Protocol (REP)** lets a site publish `robots.txt`, requesting that named User-Agents avoid specified content. It is a voluntary request, not a technical access barrier (§2.3, p. 4).

A **canary token** here is not a secret credential. It is a distinctive content value assigned to one visitor identity. Reappearance in a chatbot response is evidence that information shown to that identity entered the chatbot’s retrieval chain (§3, p. 4).

# 4. Research Problem and Gap

## Existing problem

Site owners may wish to identify and restrict AI-related scraping because of service load, privacy, copyright, consent, or other concerns (§1, pp. 1–2). Access controls often depend on knowing the scraper’s identity.

## Shortcomings of earlier approaches, as reported by the authors

Existing identification relies chiefly on:

- providers’ voluntary disclosures;
- community-maintained lists; and
- one-off researcher or practitioner tests (§2.2, p. 3).

The authors argue that these sources can be incomplete, outdated, erroneous, non-scalable, or vulnerable to User-Agent spoofing.

Prior anti-scraping research primarily concerns training data, image corruption, consent signaling, or content degradation. It does not establish how to attribute real-time chatbot retrieval or how already-collected content behaves after blocking (§2.3, pp. 3–4).

## Research gap

The paper identifies three unknowns:

- which observed visitor identities actually feed individual chatbots;
- whether chatbots fetch live content or rely on stored/indexed copies; and
- whether taking a site offline or adding `robots.txt` after collection suppresses later chatbot answers.

## Motivation and scope

The scope is post-deployment web retrieval by 22 production chatbots, observed using 20 controlled English-language fictitious `.com` sites. The work does not directly determine model-training membership or all infrastructure used by each provider.

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

- **RQ1:** “Which User-Agents do AI chatbots use to source web content when generating responses?” (§2.2, p. 3)
- **RQ2:** “How do AI chatbots source web content when generating responses? Do they retrieve content live or rely on caches?” (§2.2, p. 3)
- **RQ3:** “Can simple site blocking techniques like taking sites offline or using robots.txt affect AI chatbots’ retrieved content?” (§2.3, p. 4)

## Objectives

The authors aim to:

- develop an automatic attribution method that does not rely solely on providers’ declarations;
- map observable scrapers to chatbots;
- investigate retention of scraped content; and
- measure the effects of post-scraping unavailability and `robots.txt` restrictions.

## Hypotheses

No formal hypotheses are stated. The study poses exploratory research questions rather than pre-registered directional predictions.

# 6. Assumptions / Threat Model

The paper does not provide a conventional adversarial threat model, but its system assumptions are identifiable.

## System assumptions

- Content served to an observed visitor may later appear in a chatbot answer (§3, p. 4).
- Canary values are sufficiently distinctive to make repeated accidental matches unlikely (§3.4, p. 6).
- The mapping from visitor identity to issued tokens is accurately retained.
- Chatbot prompts can elicit at least some retrieved fields.
- A `(User-Agent, ASN)` pair is an adequate operational identity for the main experiment (§3.1, p. 5).

## Trusted components

Implicitly trusted components include the researchers’ web servers, token-assignment database, response logs, hand-written matching rules, and network/ASN observations.

## Concealment and ambiguity considered

Potential visitors can:

- use generic browser User-Agents;
- rotate User-Agents;
- spoof names;
- access content indirectly through a search engine; or
- retrieve content without causing the chatbot to reproduce a token.

The method is intended to tolerate misleading labels because it associates output with a concrete visitor tuple, but it cannot always determine the organizational actor behind a generic-browser visit.

## Excluded or unresolved capabilities

The experiment does not establish:

- whether a token entered pre-training rather than inference-time storage;
- whether an intermediary transformed or forwarded the data;
- precise cache architecture or retention time;
- whether `robots.txt` was violated during the restricted period; or
- all geographically or content-dependent scraper infrastructures.

# 7. Methodology

## 7.1 Study design

This is a longitudinal, controlled web-measurement experiment. Twenty sites served visitor-specific variants; 22 chatbots were queried under three accessibility conditions over several months (§4, pp. 6–8).

## 7.2 Website construction

The researchers purchased 20 `.com` domains with no recent Internet Corporation for Assigned Names and Numbers (ICANN) history and hosted one fictitious site per domain on Google Cloud (§4.1, pp. 6–7). Templates imitated ordinary entities such as companies or artist portfolios.

Each template had 10 token placeholders distributed throughout the site to reduce loss from stripping or truncation. Content was hand-written, benign, and designed not to overlap real entities.

Discoverability measures included:

- submission to Google and Bing webmaster tools;
- following Brave Search submission/indexing guidance; and
- hidden links connecting the 20 sites from other researcher-controlled sites (§4.1, p. 7).

## 7.3 Token creation and assignment

Tokens were generated using Python Faker and random-number generation. Each unseen `(User-Agent, ASN)` pair received a fresh, stable 10-token variant; repeat visits from the same pair received the same values (§§3.1, 4.1, pp. 5, 7).

The smallest token-value space reportedly contained 4,761 possibilities. The paper reports an average of 592.2 distinct visitor pairs per site (Table 2, p. 8).

## 7.4 Quality control

The authors discarded:

- tokens duplicated across visitors;
- a value assigned to different semantic variables across visitors;
- substring matches, such as “Port” inside “West Port”;
- numerical/date-token matches, because unrelated numbers could coincide; and
- matches failing the formal score (§4.1, p. 7; Table 7, p. 16).

This is conservative: it sacrifices sensitivity to reduce ambiguous attributions.

## 7.5 Chatbot sample

The authors selected 22 production chatbots with web-search capability, based primarily on LMArena and OpenRouter listings plus search-provider systems (Table 1, p. 7):

ChatGPT, Claude, Copilot, Deepseek, Duck.ai, ERNIE, Gemini, GLM, Granite, Grok, Hunyuan, Kimi, Liquid, Llama, Mistral, Nova, Perplexity, Qwen, Reka, Solar, Step-3, and Venice.

Responses were collected through a web-search API where available, automated web interfaces using Selenium or nodriver otherwise, and manual interaction when automation was blocked (§4.2, p. 7). No library versions, model-version identifiers, sampling parameters, random seeds, hardware specifications, or response counts are reported.

## 7.6 Prompt procedure

Each chatbot-site interaction used two prompts (§§3.2, 4.2, pp. 5, 7–8):

1. A primary prompt asked the chatbot to search the internet, answer one question for each website variable, and obey formatting rules.
2. A follow-up asked for variant sites, discrepancies, and more current information.

A pilot on sites outside the main study informed this design, but the pilot sample size and results are not supplied.

## 7.7 Token extraction

Responses were searched using hand-written regular expressions and text-matching rules (§3.3, p. 6). A returned token was mapped to the `(User-Agent, ASN)` pair that had received it.

## 7.8 Experimental conditions and controls

- **Condition 1—online baseline:** all 20 sites accessible for two months.
- **Condition 2—offline:** 10 sites taken down.
- **Condition 3—blocked:** the other 10 remained online but used `robots.txt` to disallow all bots.

After one and two weeks, chatbots were queried. All sites were then restored, restrictions removed, and querying repeated after one and two further weeks (Figure 3; §4.3, p. 8).

The split provides contemporaneous offline and `robots.txt` groups, but the paper does not report random assignment, balancing criteria, or a crossover between the two sets.

## 7.9 Metrics and statistical methods

Primary measurements were:

- extracted-token counts;
- number of websites producing evidence for a visitor identity;
- binary presence/absence of an attributed User-Agent by stage; and
- descriptive counts of systems exhibiting behaviors.

No confidence intervals, hypothesis tests, effect sizes, or correction for repeated probing are reported.

# 8. Experiments / Analyses

## X1 — Baseline scraper-to-chatbot mapping

**Purpose:** answer RQ1.

**Setup:** after two months online, query all 22 chatbots about all 20 sites and match returned tokens to visitor pairs (§4.3, p. 8).

**Result:** evidence was obtained for 18 chatbots; none was obtained for Deepseek, Hunyuan, GLM, or Liquid (§5.1, p. 10). Table 9 gives baseline token and website counts.

**Caveat:** absence of tokens is not evidence that those four systems never accessed the sites; it may be a false negative.

## X2 — Offline persistence

**Purpose:** test RQ2 and part of RQ3.

**Setup:** take 10 previously indexed sites offline and query after one and two weeks, then again one and two weeks after restoration (Figure 3; Table 5).

**Result:** content tied to search-engine and generic-browser agents often persisted. Seven of eight systems associated with Googlebot, Bingbot, or Bravebot still returned content after one offline week (§5.2, p. 10).

**Interpretation:** the authors treat this as evidence that cached or retained copies are common.

**Caveat:** the experiment detects persistence, not the exact storage location, mechanism, or cache age.

## X3 — Restrictive `robots.txt`

**Purpose:** answer RQ3 by comparing unavailable sites with accessible-but-disallowed sites.

**Setup:** keep 10 sites online but add a file disallowing all bots; query after one and two weeks, then after restoration (Figure 3; Table 6).

**Result:** 12 of the 18 observable systems returned content in both blocking conditions (§5.3, p. 12). Slightly more User-Agent families appeared under `robots.txt` than offline, but the authors explicitly decline to treat this as proof of protocol violation.

**Caveat:** already-cached data can produce answers without a new restricted-period visit.

## X4 — Token-quality filtering

Table 7 (p. 16) records token removals separately for nine measurement points. For example, baseline extraction found 2,325 tokens and discarded 928 due to numerical confusion, substring confusion, overlap, or score failure. This analysis protects precision but may lower recall.

## X5 — Ethical and open-science procedures

Appendix A says the study was declared exempt by the institutional review board; IP information was anonymized and sensitive fields hashed. The researchers sought to avoid burdening external services by deploying their own sites (p. 14).

Appendix B reports that example code, an example site and script, and anonymized aggregate data are available in a repository. The repository was not supplied or inspected.

# 9. Results

## RQ1: Which User-Agents feed chatbot answers?

The systems varied substantially (§5.1, pp. 9–10):

- Ten first-party declared User-Agent strings were recovered.
- Six of 18 observable chatbots showed generic-browser-associated content.
- Ten of 18 showed content associated with Googlebot, Bingbot, or Bravebot.
- Kimi produced the broadest mixture: Chrome, Edge, Googlebot, Obsidian, Qaxbrowser, QQBrowser, QuarkPC, SLBrowser, and WindowsWechat families (Tables 4 and 9).
- Solar’s observed matches were exclusively generic-browser families.
- Some relationships were not publicly documented in the authors’ collected documentation, including Googlebot associations for systems such as Qwen and Perplexity (Tables 3 and 8).

The authors checked the ASN associated with third-party search-agent tokens and report that the visits originated from the expected search companies’ networks (§5.1, p. 10). They therefore favor indirect acquisition through search results over spoofing for those cases.

That reasoning does not apply equally to generic-browser identities, whose operator attribution remains less direct.

## RQ2: Live retrieval or caches?

Many systems continued to emit old tokens after origins became unreachable:

- Seven of eight systems tied to the three named third-party search crawlers persisted after one offline week.
- Grok, ERNIE, and Solar also returned generic-Chrome-associated content after sites went offline (§5.2, pp. 10–11).
- Tables 5 and 6 show persistence across several one- and two-week observations.

The supported conclusion is that retained or indexed content is common. The data do not quantify a cache hit rate or show that every returned value came from one specific cache layer.

## RQ3: Do simple post-scraping controls work?

Twelve of 18 observable systems continued producing attributed content in both offline and `robots.txt` conditions (§5.3, p. 12). Duck.ai uniquely stopped in both.

The authors’ conclusion is expressly limited to **post-scraping** blocking: once content has already been collected, taking the origin offline or posting a disallow rule often does not erase downstream copies.

## Baseline detail from Table 9

Selected Stage 1 observations include:

- ChatGPT/OAI-SearchBot: 68 tokens across 11 sites.
- Claude/Bravebot: 88 across 20.
- Copilot/Bingbot: 57 across 17.
- Duck.ai/DuckAssistBot: 56 across 9.
- Granite/GranitePlayground: 75 across 12.
- Mistral/Bravebot: 66 across 19.
- Nova/Amazonbot: 81 across 15.
- Perplexity/PerplexityBot: 110 across 17.
- Qwen/Googlebot: 103 across 20.
- Venice/Bravebot: 63 across 17.

These are attributed-token counts, not accuracy percentages.

# 10. Figure-by-Figure Interpretation

## Figure 1 — How web data enters a chatbot response

**Location:** p. 3; introduced in §2.1, p. 2.

This is a conceptual flow diagram, not a quantitative plot. It has no axes, units, scale, confidence intervals, or numerical measurements.

The left-to-right sequence is:

1. A website is published.
2. It may be independently scraped and indexed.
3. A model may ingest that material during training, or a deployed chatbot may retrieve it later.
4. A user queries the chatbot.
5. The chatbot assesses the information need.
6. Retrieval follows one of two paths: cached/indexed content or live scraping.
7. Retrieved content is parsed and used in response generation.

The diagram’s key distinction is the fork between **Option 1: pull cached webpage** and **Option 2: scrape**. It supports RQ2 by showing why a returned answer alone does not reveal which path was used.

**Caveat:** the diagram is an author-proposed generalization, not an observed trace of all 22 systems.

## Figure 2 — Canary-token attribution pipeline

**Location:** p. 5; method introduced on p. 4.

This three-stage architecture is the paper’s methodological core:

1. **Deploy websites with canary tokens.** A common template is filled differently for scraper 1 and scraper *n*. Visitor identity includes User-Agent and ASN.
2. **Query chatbots.** Each chatbot searches for the fictitious entity.
3. **Infer scraper association.** If the response repeats “New York/ice cream,” it is linked to scraper 1; “Los Angeles/pie” links to scraper *n*.

Blue arrows show data or query flow. The colored phrases are example tokens, not measured results. The website-to-scraper branching demonstrates differentiated serving; the response-to-scraper arrow demonstrates reverse attribution.

**Caveat:** one chatbot may combine tokens from multiple visitors, so the mapping need not be one-to-one.

## Figure 3 — Measurement timeline

**Location:** p. 8.

This is a vertical time-flow diagram with three stages:

- Stage 1: 20 sites online for two months, followed by one baseline query round.
- Stage 2: 10 sites offline and 10 `robots.txt`-blocked; both groups queried after one and two weeks.
- Stage 3: all sites restored; each prior group queried after one and two weeks.

Blue, purple, and green boxes distinguish baseline, offline, and blocked groups. Dashed separators divide the stages.

The diagram establishes temporal ordering and comparison conditions. It does not itself report outcomes.

**Potential ambiguity:** the figure shows waiting/query sequencing, but the paper does not give calendar dates or exact query counts within each “query” event.

# 11. Table-by-Table Interpretation

## Table 1 — Chatbot sample

**Location:** p. 7.

Lists 22 chatbots and publishers. It defines the system sample but provides no version numbers or dates of access. There is no ranking or baseline.

## Table 2 — Site traffic

**Location:** p. 8.

| Measure | Minimum/site | Maximum/site | Average/site | Distinct across all sites |
|---|---:|---:|---:|---:|
| User-Agents | 313 | 477 | 405.95 | 2,765 |
| ASNs | 154 | 226 | 192.4 | 549 |
| Unique `(User-Agent, ASN)` visitors | 313 | 674 | 592.2 | 4,042 |

The table establishes that each site attracted hundreds of visitor identities. “Across all sites” is a deduplicated aggregate, not the sum of site-level averages.

## Table 3 — Main chatbot/User-Agent mapping

**Location:** p. 9.

Rows are AI systems and observed User-Agent families. Columns classify each family, indicate whether it appeared while sites were online, offline, or blocked, and whether the relationship was publicly known.

It excludes Deepseek, Hunyuan, GLM, and Liquid because no response tokens were measured. Dashes mean not observed under a status; checkmarks mean observed. It supports all three RQs at a high level.

**Important qualification:** “publicly known” is based on the authors’ documentation sources, not an exhaustive external proof.

## Table 4 — Kimi User-Agent families

**Location:** p. 10.

Lists nine Kimi-associated families: Chrome, Edge, Googlebot, Obsidian, Qaxbrowser, QQBrowser, QuarkPC, SLBrowser, and WindowsWechat. Eight are labeled generic-browser agents and Googlebot is third-party search.

It supports the authors’ inference that Kimi may rotate through many identities. Rotation is an interpretation; the table directly establishes only multiple associated strings.

## Table 5 — Offline condition

**Location:** p. 11.

Rows are chatbot/User-Agent pairs; columns are online baseline, one and two weeks down, and one and two weeks back online. Checkmarks indicate successful attribution at that measurement.

The table shows widespread persistence but also irregular appearance and disappearance. For example, ERNIE’s Baiduspider appears after the baseline, motivating two alternative explanations in the prose: baseline elicitation failure or fallback behavior.

No percentages or statistical uncertainty are supplied.

## Table 6 — `robots.txt` condition

**Location:** p. 11.

Uses the same structure for one and two weeks blocked and one and two weeks post-block. Bold checkmarks denote observations present here but absent from Condition 2.

It shows more observed families in some blocked measurements than offline measurements, but the authors caution that this does not prove restricted-period crawling.

## Table 7 — Token filtering

**Location:** p. 16.

Nine columns cover baseline, four offline/restoration measurements, and four blocked/post-block measurements.

| Measurement | Found | Discarded |
|---|---:|---:|
| Baseline | 2,325 | 928 |
| 1 week offline | 797 | 336 |
| 2 weeks offline | 585 | 305 |
| 1 week back online | 1,097 | 479 |
| 2 weeks back online | 1,262 | 555 |
| 1 week blocked | 1,366 | 627 |
| 2 weeks blocked | 1,192 | 540 |
| 1 week post-block | 1,465 | 672 |
| 2 weeks post-block | 1,506 | 716 |

Discard categories are numerical confusion, subset confusion, token overlap, and below-score results. Numerical confusion dominates every column.

**Analyst-derived example:** baseline retained candidates after listed discards equal `2,325 − 928 = 1,397`, assuming “Total Tokens Discarded” is fully inclusive. The paper does not itself label this as the final valid-token count.

## Table 8 — Documentation sources

**Location:** p. 16.

Provides URLs used to classify publicly documented agents for 11 systems. Claude has two sources. Systems absent from this table may lack listed documentation, but absence does not prove that no documentation exists.

## Table 9 — Detailed baseline results

**Location:** p. 17.

Compares self-declared agents with measured agents, identifies the corresponding full-string row in Table 10, and gives token counts and websites visited out of 20.

Multiple numbers within a cell correspond to multiple User-Agent variants. Kimi has the densest set. Tables 3–4 aggregate this detail.

A notable textual/table issue is that Solar’s generic Edge family appears in Tables 3 and 5/6, while the visible Stage 1 portion of Table 9 lists Chrome, Safari, and Firefox but no Edge row. This is not necessarily contradictory: Edge may have appeared only after Stage 1.

## Table 10 — Full User-Agent strings

**Location:** pp. 18–19.

Lists 39 full strings underlying family-level reporting:

- rows 1–4: DuckAssistBot, GranitePlayground, and Meta agents;
- rows 5–6: Googlebot variants;
- rows 7–35: generic/browser-like variants and OAI-SearchBot;
- rows 36–39: Amazonbot, Bingbot, Bravebot, and PerplexityBot.

The main text deliberately compresses these into families. Page 19 was not visually rendered, so rows 37–39 were inspected through native text only.

# 12. Diagram / Architecture Interpretation

The method forms a closed attribution loop:

`Visitor request → visitor-specific content → chatbot retrieval chain → chatbot response → token extraction → visitor lookup`

The website server is both the content source and measurement instrument. Its input is a request carrying network and User-Agent information. Its output is a stable, customized page. The chatbot is externally controlled and treated as a black box. Its prompted response becomes observable output. The matching database joins that output back to the original visitor.

There is no direct instrumentation inside a chatbot or search provider. Consequently, the architecture identifies **which issued content variant is represented in an answer**, not every internal hop by which it arrived.

# 13. Equations and Mathematical Concepts

## Equation (1) — Binary chatbot–scraper match

**Location:** §3.3, p. 6.

The paper defines:

- \(S\): set of scraper identities.
- \(s=(UA,ASN)\): one scraper identity.
- \(\ell\): a chatbot.
- \(T_\ell(s)\in\mathbb{Z}_{\ge0}\): total extracted tokens associated with \(s\) in responses from \(\ell\).
- \(W_\ell(s)\in\mathbb{Z}_{\ge0}\): number of distinct website-query interactions in which \(s\) is observed.
- \(t,w\): thresholds, set to \(t=2\) and \(w=1\).

The intended rule is:

\[
M_\ell(s)=
\begin{cases}
\text{yes}, & T_\ell(s)\ge t \;\lor\; W_\ell(s)\ge w\\
\text{no}, & T_\ell(s)<t \;\land\; W_\ell(s)<w
\end{cases}
\]

In plain language, the authors intend to accept a link when there is evidence from at least two tokens or from at least one qualifying website interaction.

### Notation inconsistency

The rendered equation and extracted text use \(F_\ell(s)\) inside the decision rule, although the preceding definition introduces \(W_\ell(s)\), not \(F_\ell(s)\). No \(F_\ell(s)\) is defined. This is a text–equation inconsistency; \(W_\ell(s)\) is likely intended, but that correction is an analyst interpretation.

### Threshold-description ambiguity

The authors then state that \(t=2,w=1\) “ignores any scraper identity that is associated with only one token from one website.” Under the displayed logical rule, however, one token observed in one website interaction would satisfy \(W_\ell(s)\ge1\), yielding “yes.” Therefore, the equation, parameter statement, and prose cannot all be literally correct.

The supplied material does not resolve whether the intended rule was:

- at least two tokens **or** evidence across more than one website;
- at least two tokens **and** one website;
- a differently defined \(W\)/\(F\); or
- another implementation condition.

This matters because it determines the minimum evidence needed for attribution.

## Collision argument

The authors say an accidental match from a space of size \(|V|\) is on the order of \(1/|V|\). With a space of at least \(10^3\), a single-token coincidence is described as roughly \(10^{-3}\), and two independent coincidences as roughly \(10^{-6}\) (§3.4, p. 6).

This is an order-of-magnitude rationale, not an empirical false-positive rate. Elsewhere the smallest actual token space is reported as 4,761 (§4.1, p. 7), which is consistent with being at least \(10^3\) but more specific.

# 14. Interpretation and Discussion

The experiments answer RQ1 by showing that chatbot retrieval cannot reliably be understood from provider-branded crawler names alone. Some answers map to declared agents, others to ordinary-looking browsers, and others to external search crawlers.

They answer RQ2 by demonstrating output persistence after origins became unreachable. That is strong evidence for retained downstream copies, but not a direct observation of cache architecture.

They answer RQ3 narrowly: post-collection `robots.txt` and removal from the web do not reliably prevent previously acquired facts from appearing. The design does not test whether a restrictive rule posted **before first access** prevents initial collection.

The authors emphasize supply-chain opacity. A site may permit search indexing for discoverability while unknowingly enabling chatbot retrieval through the search provider. Consent or exclusion preferences may therefore need to propagate across organizations, not just be enforced at the origin.

No formal hypothesis testing is performed. Claims are supported by repeated observational matches and controlled availability changes rather than statistical inference.

# 15. Contributions and Novelty

## Conceptual contribution

The chatbot’s response is framed as an attribution side channel: differentiated content can reveal its upstream visitor.

## Methodological contribution

A repeatable three-part technique combines visitor-specific content serving, targeted chatbot prompting, and reverse token lookup.

## Systems contribution

The authors deployed 20 controlled sites, collected visitor identities, automated or manually queried 22 production systems, and followed them across multiple availability states.

## Empirical contribution

The study documents:

- first-party, generic-browser, and third-party-search associations;
- previously undocumented associations in the authors’ comparison;
- persistence after site removal;
- weak post-scraping effectiveness of simple controls; and
- one contrasting system, Duck.ai, that stopped returning content in both blocking conditions.

## Artifact contribution

Appendix B reports the release of example code and anonymized aggregate data. The artifact itself was not supplied.

# 16. Limitations

## Authors' stated limitations

From §6, pp. 12–13:

- Only 20 websites were studied.
- Queries came from one vantage point: a U.S. university campus network.
- Providers may use different infrastructure by site, content type, or geography.
- Scrapers producing insufficient observable evidence may be missed.
- Prompt choice, site design, and observation window affect observability.
- The observation window is relatively short and likely emphasizes inference-time retrieval.
- Scaling may affect user experience.
- Adversaries may try to detect tokens or rotate User-Agents.
- The operational identity `(User-Agent, ASN)` is relatively simple.

## Additional evidence-based analyst observations

These are analyst observations, not author admissions:

- Equation (1)’s undefined \(F_\ell(s)\) and its apparent conflict with the prose leave the implemented acceptance threshold uncertain.
- The paper does not report exact chatbot/model versions, access dates, API configurations, decoding settings, repetition counts, or the number of responses analyzed.
- The 10/10 allocation to offline and blocked conditions is not described as randomized or balanced.
- Binary checkmarks do not expose how much evidence supported each stage-level match.
- Query wording explicitly asks for web search and may not represent ordinary user behavior.
- Manual, API, and browser-automated collection modes may induce different retrieval behavior.
- The same site content remained associated with previously issued tokens, so persistence does not identify whether a system used its own cache, a search index, another intermediary, or a preserved conversation state.
- Public-documentation classification is based on the sources assembled by the authors and may not be exhaustive.
- The paper uses “reliably” without presenting an independently labeled ground-truth test set, sensitivity estimate, or confidence interval.
- Website traffic consisted largely of bots according to the authors, but human/bot classification procedures are not detailed.

# 17. Threats to Validity

## Internal validity

The controlled sites and differentiated tokens strongly connect emitted values to issued variants. Threats include duplicate tokens, substring matches, numerical coincidences, prompt stochasticity, and the uncertain match equation. The authors mitigate several through conservative filtering and repeated websites/queries.

## Construct validity

A token match measures exposure to content shown to a `(User-Agent, ASN)` pair. It does not necessarily measure direct ownership or operation of that scraper by the chatbot provider. Likewise, “cache” operationally means persistence after origin loss, not direct inspection of a caching component.

## External validity

Twenty fictitious `.com` sites, one network vantage point, and a limited observation window may not generalize to large publishers, other languages, jurisdictions, content types, or geographic regions.

## Statistical conclusion validity

The paper reports descriptive counts but no uncertainty estimates or statistical tests. Chance-match reasoning assumes sufficiently large and effectively independent token spaces; real generated categories may not be uniformly distributed.

## Ecological validity

Artificial sites and unusually comprehensive prompts may attract or exercise retrieval systems differently from ordinary pages and ordinary user questions.

## Reproducibility

The described repository improves potential reproducibility, but exact deployed sites are anonymized and retained for ongoing work. Model services and crawler behavior can change. The repository was not supplied for this analysis.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

From §6, pp. 12–13:

- enrich scraper identity with IP ranges, Transport Layer Security (TLS) fingerprints, and behavior;
- run longer and larger studies to detect model-training scraping;
- measure cache-retention policies;
- measure how quickly chatbots incorporate new information;
- extend canary methods to images, audio, and video;
- design tokens robust to adversarial detection and User-Agent rotation; and
- explore preservation and enforcement of consent signals across supply chains.

## B. Additional open questions

- What exact match rule was implemented despite Equation (1)’s inconsistency?
- How long does each system retain content beyond the two-week windows?
- Would `robots.txt` deployed before any indexing prevent initial acquisition?
- Do results change under randomized site assignment or a crossover design?
- How do geography, language, domain reputation, and page popularity affect crawler selection?
- Can generic-browser visitors be attributed without relying on User-Agent labels?
- What fraction of actual retrieval events produce observable response tokens?
- How stable are these mappings across chatbot/model updates?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| AI chatbot | A conversational system that can generate answers and may retrieve web information. |
| ASN | Autonomous System Number; an identifier for the network organization from which traffic originates. |
| Attribution side channel | An indirect signal—in this case chatbot output—that reveals an upstream data source. |
| Cache | A stored copy that can be reused without fetching the original page again. |
| Canary token | A distinctive value given to a particular visitor so its later reappearance can reveal a data path. |
| Crawler/scraper | Automated software that requests web pages. |
| False negative | A real scraper relationship that the procedure fails to detect. |
| False positive | A relationship inferred even though the visitor did not actually supply the content. |
| Generic-browser agent | A User-Agent resembling an ordinary browser or other general application. |
| First-party declared agent | A crawler identity publicly associated with the chatbot provider. |
| Inference time | The period when a deployed model generates an answer. |
| LLM | Large language model. |
| RAG | Retrieval-Augmented Generation: giving retrieved external material to a model while it answers. |
| REP | Robots Exclusion Protocol. |
| `robots.txt` | A site-root file requesting that specified bots avoid specified paths. |
| Third-party search agent | A crawler belonging to a search provider other than the chatbot’s owner. |
| Token collision | The same or confusable token being associated with multiple visitors. |
| User-Agent | A client-supplied HTTP string describing the browser or bot. |
| \(S\) | Set of scraper identities. |
| \(s=(UA,ASN)\) | One operational scraper identity. |
| \(T_\ell(s)\) | Number of attributed tokens for chatbot \(\ell\) and visitor \(s\). |
| \(W_\ell(s)\) | Number of website-query interactions showing visitor \(s\) for chatbot \(\ell\). |
| \(F_\ell(s)\) | Undefined symbol appearing in Equation (1), likely a typographical inconsistency. |
| \(t,w\) | Decision thresholds, reported as 2 and 1. |
| \(M_\ell(s)\) | Binary decision on whether chatbot \(\ell\) matches visitor \(s\). |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Websites | 20 | sites | Main deployment | Author-reported | §4.1, p. 6 |
| Canary placeholders | 10 | per site | Template design | Author-reported | §3.1, p. 4 |
| Chatbots | 22 | systems | Study sample | Author-reported | Table 1, p. 7 |
| Systems yielding scraper evidence | 18 | systems | All results | Author-reported | §5.1, p. 10 |
| Systems yielding no tokens | 4 | systems | Deepseek, Hunyuan, GLM, Liquid | Author-reported | Table 3; §5.1 |
| Initial online period | 2 | months | Condition 1 | Author-reported | §4.3, p. 8 |
| Offline group | 10 | sites | Condition 2 | Author-reported | §4.3, p. 8 |
| `robots.txt` group | 10 | sites | Condition 3 | Author-reported | §4.3, p. 8 |
| Minimum visitors per site | 313 | `(UA,ASN)` pairs | Entire online period | Visually readable | Table 2, p. 8 |
| Maximum visitors per site | 674 | pairs | Entire online period | Visually readable | Table 2 |
| Mean visitors per site | 592.2 | pairs/site | Entire online period | Visually readable | Table 2 |
| Distinct visitors overall | 4,042 | pairs | Across sites | Visually readable | Table 2 |
| Smallest token space | 4,761 | possible values | Token generation | Author-reported | §4.1, p. 7 |
| Match threshold \(t\) | 2 | tokens | Matching rule | Author-reported, but rule uncertain | §3.3, p. 6 |
| Match threshold \(w\) | 1 | interaction | Matching rule | Author-reported, but rule uncertain | §3.3, p. 6 |
| Approximate one-token coincidence | \(10^{-3}\) | probability order | Space at least \(10^3\) | Author-reported | §3.4, p. 6 |
| Approximate two-token coincidence | \(10^{-6}\) | probability order | Independence assumption | Author-reported | §3.4, p. 6 |
| Declared-agent strings found | 10 | strings | RQ1 | Author-reported | §5.1, p. 10 |
| Systems with generic-browser evidence | 6 of 18 | systems | Observable systems | Author-reported | §5.1 |
| Systems with major search-agent evidence | 10 of 18 | systems | Googlebot/Bingbot/Bravebot | Author-reported | §5.1 |
| Search-backed systems persisting offline | 7 of 8 | systems | After one week offline | Author-reported | §5.2, p. 10 |
| Systems persisting in both blocking conditions | 12 of 18 | systems | Offline and `robots.txt` | Author-reported | §5.3, p. 12 |
| Systems stopping in both | 1 | system | Duck.ai | Author-reported | §5.3 |
| Baseline tokens found | 2,325 | tokens | Before filtering | Visually readable | Table 7, p. 16 |
| Baseline tokens discarded | 928 | tokens | Quality filters | Visually readable | Table 7 |
| Baseline remainder | 1,397 | tokens | \(2325-928\), assuming inclusive total | Analyst-derived | Table 7 |
| Full measured User-Agent strings | 39 | strings | Stage 1 list | Visually/textually readable | Table 10, pp. 18–19 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Canary variants can identify known chatbot scrapers. | Ten observed strings matched declared agents. | X1; Tables 3, 8, 9 | §5.1, p. 10 | Moderate internal validation; not an independent benchmark. |
| Some chatbot retrieval resembles ordinary browser traffic. | Six of 18 observable systems linked to generic-browser strings. | X1; Tables 3–4, 9 | §5.1 | Strong descriptive evidence for association; operator identity less certain. |
| Third-party search infrastructure supplies many chatbots. | Ten of 18 associated with Googlebot, Bingbot, or Bravebot; ASNs reportedly matched expected networks. | X1; Tables 3, 9 | §5.1, p. 10 | Stronger than User-Agent alone; internal intermediary path remains unobserved. |
| Kimi may rotate User-Agents. | Nine families and many full variants associated with Kimi. | Tables 4, 9, 10 | §5.1 | Rotation is author inference, not directly observed session-by-session. |
| Search-indexed content persists after origin removal. | Seven of eight search-agent-associated systems returned content after one offline week. | X2; Table 5 | §5.2 | Supports retention/indexing, not a particular cache implementation. |
| Browser-like scraper content can also persist. | Grok, ERNIE, and Solar returned generic-Chrome-associated content after sites went offline. | X2; Table 5 | §5.2, pp. 11–12 | Descriptive evidence; storage location unknown. |
| Post-scraping offline and `robots.txt` controls often fail to suppress answers. | Twelve of 18 systems returned content in both conditions. | X2–X3; Tables 5–6 | §5.3, p. 12 | Strong for this post-collection setup; not a test of pre-collection blocking. |
| Duck.ai responded to blocking signals. | It stopped returning attributed content in both restricted conditions. | Tables 5–6 | §5.3 | Suggestive; could also reflect elicitation variability. |
| The method has low accidental-collision risk. | Token-space argument and conservative filtering. | Eq. 1; Table 7 | §§3.4, 4.1 | Theoretical order-of-magnitude argument; match-rule inconsistency weakens reproducibility. |

# 22. Very Simple Explanation

Imagine making 20 fake websites. Whenever a different robot visits, the website quietly gives that robot a unique version of the facts. One robot might see that Alice lives in New York and likes ice cream; another might see Los Angeles and pie.

Next, you ask different AI chatbots about Alice. If one answers “New York” and “ice cream,” you can look in your records and determine which visitor received that exact combination. The chatbot has effectively carried the visitor’s fingerprint back to you.

The researchers found that chatbots get information through many routes: their own named crawlers, ordinary-looking browser identities, and search engines such as Google, Bing, and Brave. Information often remained available even after the original site disappeared or asked all robots to stay away. The important lesson is that once web information enters a chatbot/search supply chain, changing the original website may not remove copies already stored elsewhere.

# Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text and rendered p. 1 | Yes | Fully represented | Problem, method, sample, and claims covered. |
| §1 Introduction | Yes | Yes | Fully represented | Motivation and four headline findings integrated. |
| §2 Background | Yes | Yes | Represented in compressed form | Prior literature grouped by function rather than citation-by-citation. |
| §2.1 AI web scraping | Yes | Yes | Fully represented | Training, indexes, live retrieval, RAG. |
| §2.2 Identifying scraping | Yes | Yes | Fully represented | User-Agent limitations and RQ1/RQ2. |
| §2.3 Preventing scraping | Yes | Yes | Represented in compressed form | Defense families and RQ3 included. |
| §3 Method | Yes | Yes | Fully represented | All four substantive subsections included. |
| §3.1 Deployment/token serving | Yes | Yes | Fully represented | Templates, stable variants, identity rule. |
| §3.2 Querying | Yes | Yes | Fully represented | Pilot-derived two-query design. |
| §3.3 Inference | Yes | Yes | Fully represented | Extraction, mapping, and Equation (1). |
| §3.4 Robustness | Yes | Yes | Fully represented | False positives/negatives and mitigations. |
| §4 Experiment setup | Yes | Yes | Fully represented | Infrastructure, systems, prompts, conditions. |
| §4.1 Website deployment | Yes | Yes | Fully represented | Hosting, indexing, token QA. |
| §4.2 Chatbot querying | Yes | Yes | Fully represented | 22 systems and collection modes. |
| §4.3 Measurement setup | Yes | Yes | Fully represented | Three stages and timing. |
| §5 Results | Yes | Yes | Fully represented | Organized by RQ. |
| §5.1 Mapping | Yes | Yes | Fully represented | Three User-Agent categories and counts. |
| §5.2 Caching | Yes | Yes | Fully represented | Search and generic-agent persistence. |
| §5.3 Blocking | Yes | Yes | Fully represented | 12/18 and Duck.ai result. |
| §6 Discussion | Yes | Yes | Fully represented | Implications, limitations, future work. |
| RQ1 | Yes | Yes | Fully represented | Linked to X1 and Tables 3–4, 9–10. |
| RQ2 | Yes | Yes | Fully represented | Linked to X2 and Table 5. |
| RQ3 | Yes | Yes | Fully represented | Linked to X2/X3 and Tables 5–6. |
| Formal hypotheses | Yes | Yes | Not present | Paper uses exploratory RQs. |
| Figure 1 | Visually inspected | Yes | Fully represented | Conceptual retrieval flow. |
| Figure 2 | Visually inspected | Yes | Fully represented | Attribution pipeline. |
| Figure 3 | Visually inspected | Yes | Fully represented | Timeline and conditions. |
| Table 1 | Visually/textually inspected | Yes | Fully represented | All systems named. |
| Table 2 | Visually/textually inspected | Yes | Fully represented | All values reported. |
| Table 3 | Visually/textually inspected | Yes | Represented in compressed form | Major rows and categories covered; not every checkmark repeated. |
| Table 4 | Visually/textually inspected | Yes | Fully represented | All nine families listed. |
| Table 5 | Visually/textually inspected | Yes | Represented in compressed form | Pattern and important exceptions reported; full checkmark matrix not duplicated. |
| Table 6 | Visually/textually inspected | Yes | Represented in compressed form | Same compression as Table 5. |
| Table 7 | Visually/textually inspected | Yes | Fully represented | Totals reported; category-by-column matrix compressed. |
| Table 8 | Visually/textually inspected | Yes | Represented in compressed form | Purpose and coverage given; URLs not repeated. |
| Table 9 | Visually/textually inspected | Yes | Represented in compressed form | Principal counts given; dense Kimi variants summarized. |
| Table 10 | Pages 18 visually and textually; p. 19 text only | Yes | Represented in compressed form | Full 39 strings not reproduced because they are repetitive technical identifiers. |
| Equation (1) | Visually/textually inspected | Yes | Fully represented, uncertain | Undefined \(F\) and threshold conflict disclosed. |
| Algorithms/pseudocode | Yes | Yes | Not present | Method is prose plus Equation (1). |
| Appendix A | Text inspected; page not rendered | Yes | Fully represented | Ethics and privacy measures. |
| Appendix B | Text inspected; page not rendered | Yes | Fully represented | Repository description only; external artifact absent. |
| Appendix C | Text inspected; pages not rendered | Yes | Represented in compressed form | Full prompt/response example summarized. |
| Appendix D | Yes, partial visual rendering | Yes | Fully represented across Tables 7–10 | Table 10 continuation visually unavailable. |
| References | Yes | Yes | Inspected but deliberately compressed | Categories and relevant positioning covered; 81 entries not individually summarized. |
| Author-stated limitations | Yes | Yes | Fully represented | All substantive limitations included. |
| Contributions | Yes | Yes | Fully represented | Conceptual, methodological, system, empirical, artifact. |
| Supplementary material | No | Yes | Missing from supplied material | No separate supplement supplied. |
| Open-science repository | Description only | Yes | Referenced but inaccessible | Not inspected under closed-document instruction. |

## Missing or inaccessible material

- Visual renderings for pages 13–15 and 19 were not supplied.
- Table 10’s last three rows were available as native text but not visually cross-checked.
- The code/data repository described in Appendix B was not supplied and was not accessed.
- The deployed sites, raw chatbot responses, full token-assignment database, and raw traffic logs were not supplied.
- No separate supplementary file was provided.
- Exact chatbot versions, measurement dates, source code implementation of the match rule, and complete per-query records are absent from the paper.

## Uncertain interpretations

- Equation (1) uses undefined \(F_\ell(s)\) where the prose defines \(W_\ell(s)\).
- The displayed OR rule with \(w=1\) conflicts with the claim that a single token from one website is ignored.
- “Conference’17, July 2017” conflicts temporally with the 2026 arXiv marking and appears potentially templated; the supplied document does not resolve it.
- Generic-browser matches identify content paths to visitor tuples but do not conclusively identify the organization controlling those requests.
- Persistence implies retention somewhere in the retrieval chain but does not reveal the cache owner or architecture.
- Kimi’s “rotation” is a reasonable author inference from many strings, not a directly traced rotation sequence.
- The meaning of some Table 5/6 absences is uncertain because a missing token may reflect retrieval absence, response-generation variance, or matching failure.

## Deliberately compressed material

- The 81-reference bibliography was classified by its role rather than summarized citation by citation.
- Repetitive checkmark matrices in Tables 3, 5, and 6 were summarized around the claims they support.
- Table 10’s 39 long User-Agent strings were grouped into functional families; their complete text remains in the supplied source.
- Appendix C’s long example answer was compressed to its methodological role.
- Table 7’s complete confusion-category matrix was summarized with every total and representative filtering logic.

## Potential omissions

No known substantive section, subsection, research question, experiment, figure, table, numbered equation, contribution, author-stated limitation, or supplied appendix is unrepresented. The principal unavoidable gaps concern unsupplied raw artifacts, the external repository, unrendered page layouts, and the unresolved match-rule notation.