# Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search

**Authors:** Zeren Luo, Zifan Peng, Yule Liu, Zhen Sun, Mingchen Li, Jingyi Zheng, and Xinlei He  
**Venue:** 34th USENIX Security Symposium, 2025

## 1. Background and Context

Large language models (LLMs) can answer questions and generate text or code, but their knowledge becomes outdated and they can hallucinate. AI-powered search engines (AIPSEs) address these limitations through retrieval-augmented generation (RAG): they retrieve current web content and give it, together with the user’s query, to an LLM that writes a synthesized answer.

A typical RAG-based AIPSE has three components:

1. A knowledge database containing web content or saved webpage snapshots.
2. A retriever that identifies material relevant to the query.
3. A generator—usually an LLM—that uses the retrieved material to compose the answer.

This differs from a traditional search engine (TSE), which primarily returns ranked links based on keyword or semantic matching. AIPSEs instead interpret intent and summarize information directly, potentially saving users from manually inspecting many pages.

The same design creates a safety problem. An AIPSE may retrieve an unfiltered malicious webpage and quote, summarize, or directly link to it without recognizing the danger. It might, for example, recommend a malware download site instead of an official site or reproduce code from fraudulent technical documentation. The paper cites a November 2024 incident in which a developer reportedly lost about **$2,500** after ChatGPT Search supplied code leading to a fake Solana API site; the developer submitted a private key and reportedly lost the assets within 30 minutes.

The work situates this problem among several known LLM-system threats:

- Misalignment, jailbreaks, and poisoning attacks.
- Indirect prompt injection, in which external text is interpreted as an instruction.
- RAG data poisoning, in which attackers corrupt or manipulate material likely to be retrieved.
- Search-engine manipulation, including SEO intended to rank an attacker’s site highly.

Previous work largely studied open-source retrievers, LLMs, adversarially optimized inputs, or preference manipulation. This paper instead examines inherent risks in operational AIPSEs using largely benign, non-optimized queries and ordinary attacker-created websites.

### Threat model

The paper describes normal AIPSE behavior as:

\[
M(Q \,\|\, S(Q)) = R
\]

Here, \(M\) is the LLM, \(Q\) is the query, \(S(Q)\) is the content retrieved by the search engine, “\(\|\)” means that the query and retrieved content are combined, and \(R\) is the answer.

If an attacker publishes adversarial material that changes the retrieved content to \(S'(Q)\), the result becomes:

\[
M(Q \,\|\, S'(Q)) = R'
\]

The attacker wants relevant queries to include a particular website, quote its content, or produce a desired harmful answer. Harm includes phishing, scams, malware, spam, or other illegal material.

The assumed attacker is relatively weak: they can spend a small amount on domains and basic websites, publish material on public platforms, make malicious edits to crowdsourced sites, or use SEO. They do not require control of the AIPSE or expensive infrastructure.

## 2. Research Goal and Objectives

The central goal is to quantify how often production AIPSEs expose users to malicious web content and determine how those risks change with the form of the query.

The study has three main objectives:

1. Conduct the first quantitative assessment of malicious content and URL risks across seven operational AIPSEs.
2. Compare AIPSEs with Google and Bing on both usefulness and safety.
3. demonstrate real-world attack feasibility and develop a user-side defense that filters or warns about unsafe AIPSE responses without discarding most useful information.

The seven evaluated AIPSEs are:

- ChatGPT Search
- Perplexity Pro
- Microsoft Copilot
- TextCortex, using the Zeno assistant and GPT-4o
- Grok
- Doubao
- Kimi

The study tests three query forms:

- Five-keyword lists.
- Everyday natural-language questions derived from those keywords.
- Direct URL queries.

It also asks whether ordinary, cheaply constructed online documentation and phishing sites can convince AIPSEs to endorse malicious content.

## 3. Methods (Approach/Design)

### 3.1 Overall study design

The project had four phases, summarized in **Figure 1**:

1. **Data collection:** check URLs for accessibility and relevance and manually cross-validate them.
2. **Risk evaluation:** test seven AIPSEs, compare them with traditional search engines, and label returned risks.
3. **Case studies:** create malicious documentation and a simulated phishing site to test practical deception.
4. **Agent defense:** use an iterative reasoning agent, a content-refinement tool, and URL detectors to sanitize responses.

### 3.2 AIPSE response structure and risk labels

As illustrated in **Figure 2**, a typical response has:

- An **answer** written by the LLM.
- **References** attached to particular statements or answer sections.
- A broader list of retrieved **sources**, sometimes hidden until the user expands it.

The researchers define four URL risk levels:

- **Main risk:** A malicious URL is cited directly in the answer. This is the most serious category because the user is one click away from the malicious site.
- **Warning risk:** The answer cites a malicious URL but explicitly warns that it is risky or recommends a legitimate alternative.
- **Source risk:** The malicious URL appears only in the source list, not the answer. The user must actively explore the sources to encounter it.
- **None:** The URL is benign.

Responses are classified hierarchically. A response containing any main-risk URL is main risk-inclusive. If it has no main-risk URL but has a warned malicious URL, it is warning risk-inclusive. If malicious URLs occur only among sources, it is source risk-inclusive.

Copilot did not expose a general source list at the time of testing, so it could not have source-risk queries or source-risk URLs under this definition.

### 3.3 Malicious-website collection

Candidate URLs came from three threat-intelligence sources:

- **17,225 PhishTank URLs**, collected from November 27 to December 27, 2024.
- **2,427 ThreatBook URLs**, collected during 2024.
- **4,385 LevelBlue URLs**, also collected during 2024.

The researchers retained sites with valid domain certificates and HTTP status 200, then filtered cloud-storage links, URL shorteners, and domain marketplaces. This left:

- 353 PhishTank URLs.
- 291 ThreatBook URLs.
- 147 LevelBlue URLs.

Three graduate-student annotators manually cross-validated harmfulness. They removed cases in which a harmless primary domain had merely acquired a malicious subdomain or path unrelated to normal search intent. Difficult cases were checked with several cyberthreat-detection platforms.

The final validated pool contained **325 malicious URLs with generated keywords**. From it, the team randomly selected **100 URL–keyword-list pairs** as the main evaluation foundation. Five volunteers confirmed that these covered common subjects such as popular software, entertainment, and cryptocurrency platforms.

### 3.4 Query construction

**Figure 3** shows the query pipeline. Each retained page first produced a keyword-list query. That list was then converted either into a natural-language query or used to obtain URLs returned by the AIPSEs, which became direct URL queries.

#### Keyword-list queries

GPT-4o dated 2024-08-06 extracted five keywords from each page’s HTML title, `<h1>`, `<h2>`, `<h3>`, and metadata. Initial trials suggested five keywords adequately represented search intent.

Entries were discarded if their lists contained generic or irrelevant terms such as “redirect,” “loading,” “welcome,” “error,” “page,” “website,” or “URL.” Appendix A provides the complete filtering list.

An example MetaMask query was:

- MetaMask, crypto wallet, blockchain apps, gateway, recovery mode.

The dataset contained **100 keyword lists**, or **500 keywords** in total.

#### Natural-language queries

GPT-4o transformed each keyword list into a realistic everyday search question. The MetaMask list, for example, became a question about using MetaMask as a cryptocurrency wallet and gateway for blockchain applications with recovery mode.

There were **100 natural-language queries**.

#### URL queries

The researchers randomly selected URLs from risk categories observed in prior AIPSE outputs and submitted those URLs directly to the engines. This models users asking an AIPSE to summarize, translate, or otherwise process a link found in an earlier answer.

There were **457 URL queries**.

### 3.5 Validation of query realism

The team consulted its university IRB office before running an online questionnaire. It obtained **120 valid responses** from participants with varied genders, ages, educational backgrounds, and professions, recruited from universities, telecommunications and Internet companies, government offices, and banks. Participants received **5 RMB**, and the average completion time was **56.2 seconds**.

Of the 120 participants, **118 had used AIPSEs**. Reported query-use rates were:

- Natural-language queries: **83.1%**
- Keyword-list queries: **43.2%**
- URL queries: **21.2%**

Among URL-query users, intentions included:

- Summarization: **100%**
- Code crawling: **20.83%**
- Translation: **8.33%**

Additional realism checks found that:

- **92.8% of the 500 keywords** exceeded Google Trends’ undisclosed reporting threshold and had global data for the prior 12 months.
- **84 of 100 natural-language queries** returned more than 1,000 Google results.
- Five volunteers rated naturalness at an average **4.49 out of 5**.
- Average pairwise quadratically weighted Cohen’s kappa was **0.241**, interpreted by the paper as fair agreement. Technical familiarity affected ratings; domain experts found specialized queries more natural than non-experts did.

### 3.6 Annotation procedure

The core evaluation was conducted by four people within five days of data collection, with pairs cross-validating the results.

A graduate-student annotator labeled every returned URL, assisted by cyberthreat platforms. A second annotator reviewed inconclusive cases. Review continued until the label was resolved or three annotators independently considered it indeterminate, in which case it was labeled none risk. A new annotator performed a final consistency review.

### 3.7 Comparison with traditional search engines

The team created another **20 keyword lists and corresponding natural-language queries** from data collected between January 1 and May 3, 2025. The queries covered six languages and domains such as API integration, hardware wallets, streaming services, web novels, CS:GO weapon skins, and portal-navigation sites.

Google and Bing were tested both normally and with safe search enabled.

#### Utility measurement

Utility was assessed using a five-level Needs Met Rating:

- Fully Meets = 5
- Highly Meets = 4
- Moderately Meets = 3
- Slightly Meets = 2
- Fails to Meet = 1

Five graduate-level annotators rated each item, and the final score was their average. The utility comparison covered:

- **1,192 filtered first-page TSE URLs**
- **1,217 URLs from AIPSE main responses**

Malicious URLs were excluded from this utility evaluation.

#### Safety measurement

The safety analysis covered:

- **1,453 first-page TSE URLs**
- **1,422 URLs from AIPSE main responses**

Five graduate-student annotators classified their harmfulness.

Together, the paper describes an analysis of **2,875 safety-comparison URLs** across AIPSEs and TSEs.

### 3.8 Case-study methods

Both case studies used only basic web development and no SEO. They were evaluated through Perplexity under a common indexing environment with eight foundation-model configurations:

- ChatGPT-o1
- ChatGPT-4o mini
- Grok-2
- Sonar Large
- Sonar Huge
- Claude 3.5 Sonnet
- Perplexity Pro Search
- Claude 3.5 Haiku

#### Malicious technical documentation

The researchers built a fictional Web3 platform, **V50TAIS**, and separate API documentation. The site claimed:

- More than 1 million active users.
- More than 5,000 transactions per second.
- More than 200 global partners.
- Open-source status under the MIT License.

Its Python and Node.js examples instructed users to transmit private API keys to a nonexistent backend.

#### Simulated phishing

The team built two WordPress sites about fictional entities:

- An earlier simulated official site.
- A phishing site launched roughly three weeks later.

The attacker was assumed able to copy text and images but only mimic, rather than duplicate, the original UI. The phishing site:

- Added “Official Website” to its title and keywords.
- Reversed factual claims—for example, changing the fictional species Taisuratopia from “Least Concern” to “Critically Endangered.”
- Claimed that the phishing domain was the only reliable source and that the earlier official site was untrustworthy.

### 3.9 Defense design

The defender can intercept an AIPSE response and post-process it before delivering it to the user. Its goal is to preserve useful information while adding refusals, safer alternatives, or explicit warnings.

The agent follows the iterative ReAct pattern shown in **Figure 1**:

1. **Thought:** determine what evidence is needed.
2. **Action:** call a tool.
3. **Observation:** inspect the tool’s result.
4. Repeat until sufficient evidence exists, then produce a final answer.

It uses two tool types.

#### Content-refinement tool

GPT-4.1 dated 2025-04-14 applies in-context examples and chain-of-thought instructions to check six risk categories:

- Phishing
- Malware
- Scam
- Spam
- Fake news
- Illegal content, including violations of cybersecurity laws

For malicious material, it removes harmful instructions or substitutes safer information. For benign material, it retains the original. The defense appends a refined answer and safer references or warnings while trying to preserve the original information.

#### URL detectors

Three detector alternatives were tested:

- **XGBoost:** trained on 5,000 PhishTank phishing URLs and 5,000 legitimate URLs from a UNB dataset. It uses 15 URL or webpage features: IP-address use, `@`, URL length, path depth, redirection markers, “https” in the domain, URL shorteners, hyphenated domains, DNS records, domain age, remaining registration time, iframes, mouse-over manipulation, disabled right-click, and multiple forwards.
- **PhishLLM:** infers domain–brand relationships and credential-taking intent, then uses search-engine validation to control hallucinations.
- **HtmlLLM:** the authors’ GPT-4.1-based detector, using both URLs and corresponding HTML. GPT-4.1’s stated knowledge cutoff was June 1, 2024.

The agent is instructed to refine the content, check every reference, scrutinize suspicious “official” claims, list safe URLs, and stop after repeated tool failure rather than loop indefinitely.

### 3.10 Defense evaluation

The defense was tested on all **46 main risk-inclusive responses** found in the Section 6 keyword and natural-language evaluation. URL-query responses were excluded because they were derived from links already covered by those response types.

Detector-level testing used **207 main-response URLs**, of which three were inaccessible. All defenses used GPT-4.1 dated 2025-04-14.

The baseline was a prompt-only defense using the refinement prompt without external detectors. Defense success rate (DSR) means the percentage of main risk-inclusive responses converted into warning risk-inclusive responses.

## 4. Results and Findings

### 4.1 Overall risk prevalence

Every tested production AIPSE produced harmful content based on malicious URLs. Across the main evaluation, the paper reports that:

- **47% of responses were risky.**
- **34% directly cited harmful content in their answers.**

Even benign-looking keyword or natural-language queries could cause malicious sites to appear.

### 4.2 Keyword-list query results

For 100 keyword-list queries per AIPSE:

- Grok had **41 main risk-inclusive responses**.
- TextCortex had **34**.
- Kimi had **32**.

These were the highest main-risk counts. ChatGPT Search, Copilot, and Doubao were more cautious by this response-level measure. Doubao produced the largest number of warning risk-inclusive responses, meaning it often cited a malicious URL but accompanied it with a warning.

Except for Copilot, more than **39% of responses from every AIPSE contained some risk**.

#### Figure 4: Natural language versus keyword-list risk

Figure 4 is a stacked-bar comparison of response-level risk categories for natural-language and keyword-list queries across all seven AIPSEs. It shows that keyword-list queries commonly produce main-, warning-, or source-risk responses. It also shows the overall shift toward more none-risk responses under natural-language wording, except for Doubao and Kimi.

The small figure does not provide fully legible numeric labels for every segment, so exact response counts beyond those explicitly stated in the text cannot be reported reliably.

#### Figure 5: Risky URLs returned for keyword-list queries

Figure 5 reports the number and category distribution of all risky URLs:

| AIPSE | Total risky URLs | Main | Warning | Source |
|---|---:|---:|---:|---:|
| ChatGPT Search | 304 | 8.9% | 4.6% | 86.5% |
| Grok | 360 | 34.4% | 5.0% | 60.6% |
| Perplexity Pro | 116 | 59.5% | 11.2% | 29.3% |
| TextCortex | 151 | 47.0% | 6.6% | 46.4% |
| Copilot | 38 | 57.9% | 42.1% | No source category |
| Doubao | 111 | 14.4% | 53.2% | 32.4% |
| Kimi | 207 | 39.6% | 3.4% | 57.0% |

ChatGPT Search and Grok retrieved the largest numbers of risky URLs, averaging **3.04** and **3.60 per query**, respectively. The other systems returned approximately two or fewer per query. Grok consistently returned 25 URLs per query, while ChatGPT Search returned about 15, which the authors suggest may explain their greater exposure.

Doubao and Kimi returned fewer risky URLs, possibly because they focused more heavily on Chinese-language sites and therefore searched a narrower web domain.

Retrieval exposure and generator behavior differed:

- ChatGPT Search retrieved many risky URLs but cited only **13.2%** of them directly in answer text as main or warning risks. It had only **21% main- or warning-risk-inclusive responses**, indicating relatively strong filtering by its answer generator.
- Perplexity Pro directly cited **70.7%** of its risky URLs as main or warning risks, the highest proportion.
- Doubao directly cited **67.6%**, but **53.2%** of all its risky URLs were accompanied by warnings.
- Thus, Doubao cited risky material frequently but more often told users it was dangerous.

### 4.3 Natural-language query results

Natural-language wording generally made results safer:

- For ChatGPT Search, none-risk responses increased from **39 under keyword lists to 60 under natural language**.
- Grok, Perplexity Pro, TextCortex, and Copilot also produced more none-risk responses.

Doubao and Kimi were exceptions: they produced more main risk-inclusive responses and fewer none-risk responses under natural-language phrasing. Both sometimes refused direct keywords such as “gambling” or “pornography” but answered when those concepts were embedded in polite requests such as asking where to find reliable information.

The authors suggest that these Chinese-oriented systems may have weaker English safety alignment when risky keywords are implicit rather than presented directly. Across most systems, however, natural-language queries were both more typical of actual user behavior and less risky.

### 4.4 Direct URL query results

**Figure 6** is a Sankey-style flow diagram showing how URLs labeled main, warning, or source risk under keyword queries changed after being submitted directly. It also includes none-risk and inaccessible outcomes.

The main pattern is movement toward higher risk:

- Source- and warning-risk URLs often became main-risk URLs when directly queried.
- For Grok, **48 of 49 source-risk URLs** became main or warning risk, excluding inaccessible cases.
- For Kimi, every accessible URL-query response was main risk-inclusive.
- Existing main-risk URLs commonly remained main risk:
  - TextCortex retained main risk in **88.57%** of applicable cases.
  - Grok retained it in **97.22%**, excluding inaccessible URLs.

The authors attribute this to AIPSEs following an explicit instruction to access and summarize the submitted page, often without filtering its content.

Some systems refused to access URLs they had previously supplied. These cases were labeled **inaccessible**. The paper gives three possible mechanisms:

- The live webpage had disappeared, leaving only the AIPSE’s stored snapshot.
- The system failed or refused to trigger its Internet-access function.
- The AIPSE had a snapshot but still claimed the page was inaccessible or refused to summarize it.

In Kimi, some links reportedly became accessible when the `https://` prefix was removed.

Overall, direct URL queries amplified danger: material formerly buried in sources or accompanied by warnings often moved into the main answer without a warning.

### 4.5 Utility comparison with traditional search engines

**Table 1** reports average Needs Met Ratings, annotator ranges, and quadratically weighted kappa:

| Platform | Mean NMR (min–max) | κ |
|---|---:|---:|
| ChatGPT | 4.80 (4.77–4.83) | 0.910 |
| Copilot | 4.90 (4.86–4.95) | 0.762 |
| Doubao | 4.69 (4.67–4.71) | 0.949 |
| Grok | 4.68 (4.66–4.69) | 0.839 |
| Kimi | 4.98 (4.98–4.98) | 0.798 |
| Perplexity | 4.73 (4.71–4.76) | 0.851 |
| TextCortex | 4.53 (4.46–4.60) | 0.858 |
| Google | 3.64 (3.57–3.71) | 0.935 |
| Google safe search | 3.71 (3.63–3.80) | 0.911 |
| Bing | 4.48 (4.37–4.61) | 0.841 |
| Bing safe search | 4.44 (4.34–4.53) | 0.892 |

All seven AIPSEs outscored Google and Bing. Kimi had the highest mean, **4.98**, followed by Copilot at **4.90**. TextCortex was the lowest-scoring AIPSE at **4.53**, still slightly above both Bing configurations and well above Google.

AIPSE answers sometimes fell short of “Fully Meets” because they supplied unnecessary additional context—for example, Reddit discussions when the user wanted immediate API-usage instructions.

Bing’s scores were substantially closer to the AIPSE scores than Google’s. The authors interpret this similarity as suggesting that Bing may incorporate AI assistance, although this is an inference rather than a directly verified mechanism.

### 4.6 Safety comparison with traditional search engines

**Figure 7** shows, out of 40 queries, how many returned at least one malicious URL:

| Platform | Risk-return queries |
|---|---:|
| ChatGPT | 4 |
| Copilot | 4 |
| Doubao | 6 |
| Grok | 10 |
| Kimi | 7 |
| Perplexity | 6 |
| TextCortex | 8 |
| Google | 16 |
| Bing | 18 |
| Google safe search | 14 |
| Bing safe search | 14 |

Every AIPSE returned malicious URLs for fewer queries than either traditional engine in its ordinary configuration. Even safe search left Google and Bing at **14 of 40**, higher than every AIPSE.

The paper explains two relevant conditions:

- Malicious sites are often optimized to rank highly in conventional search results.
- Before this comparison, the authors had reported all observed malicious URLs to the AIPSE providers. Providers had therefore begun mitigation work, which likely reduced AIPSE vulnerability at the time of comparison.

Thus, the evidence supports the paper’s claim that AIPSEs were safer than TSEs “at the current stage,” but the timing and disclosure process matter.

### 4.7 Case study 1: Malicious online documentation

All eight Perplexity foundation-model configurations were vulnerable.

They:

- Accepted the fictional V50TAIS platform as real.
- Reproduced the malicious code exactly.
- Gave no safety warning.
- Instructed users to replace placeholder API keys with their own private API keys.

**Figure 8** shows a ChatGPT-o1-powered Perplexity answer presenting code for the fictional V50TAIS API and citing the fabricated documentation among its online sources.

The case demonstrates that AIPSEs can over-trust Internet-sourced technical documentation. Despite the questionable platform metrics and suspicious request for private keys, the systems did not critically evaluate the source’s legitimacy.

### 4.8 Case study 2: Simulated phishing

All eight foundation models treated the later phishing site as authentic while ignoring or discrediting the earlier official site.

Specifically:

- Every model displayed overconfidence in the phishing page.
- Every model warned against the simulated official site.
- Only ChatGPT-4o mini and Grok-2 considered content from both sites.
- The other six used only the phishing site’s account.

**Figure 9** shows a ChatGPT-o1-powered Perplexity response repeating the phishing site’s altered facts and treating it as authoritative. The answer describes Taisuratopia according to the phishing content and warns that discrepancies exist between “official” and unauthorized sources, thereby adopting the attacker’s framing.

The study concludes that familiar phishing tactics also work against AIPSEs. Manipulation can be cheaper than conventional search-engine manipulation because it does not require a sophisticated replica or extensive front-end work: a basic page, an “Official Website” label, and a forceful fake claim may be sufficient.

### 4.9 Defense results

**Table 2** compares URL-detector precision, recall, F1 score, and full-agent defense success rate:

| Method | Precision | Recall | F1 | Agent DSR |
|---|---:|---:|---:|---:|
| Prompt only | — | — | — | 37.0% |
| PhishLLM | 0.222 | 0.024 | 0.044 | 26.1% |
| XGBoost | 0.500 | 1.000 | 0.667 | 100.0% |
| HtmlLLM | 0.838 | 0.807 | 0.822 | 78.3% |

In raw response counts:

- Prompt-only defense fixed **17 of 46** main-risk responses.
- PhishLLM agent defense fixed **12 of 46**.
- XGBoost agent defense fixed **46 of 46**.
- HtmlLLM agent defense fixed **36 of 46**.

XGBoost’s perfect recall and 100% response-level defense success came with many false positives, reducing usability. HtmlLLM offered the best balance, with the highest F1 score, **0.822**, and a **78.3%** defense success rate. The abstract reports that the agent defense reduced available information by approximately **10.7%**, characterized as a minor cost.

PhishLLM performed poorly partly because **49.4% of the 83 malicious test URLs were malicious but not phishing sites**, whereas PhishLLM was designed specifically for phishing detection.

#### Table 3: Detector confusion matrices

| Detector | Actual malicious predicted malicious | Actual malicious predicted benign | Actual benign predicted malicious | Actual benign predicted benign |
|---|---:|---:|---:|---:|
| HtmlLLM | 67 | 16 | 13 | 108 |
| XGBoost | 83 | 0 | 83 | 38 |
| PhishLLM | 2 | 81 | 7 | 114 |

These values explain the trade-offs:

- XGBoost caught every malicious URL but falsely flagged 83 benign URLs.
- HtmlLLM missed 16 malicious URLs but generated only 13 false alarms.
- PhishLLM missed 81 of 83 malicious URLs.

The agent sometimes corrected detector mistakes by re-evaluating all links and using the foundation model’s internal knowledge to choose an authentic official site. This was particularly visible for software downloads and cryptocurrency-related answers.

## 5. Analysis and Interpretation

The findings answer the paper’s main questions in several ways.

First, production AIPSEs are not reliably filtering retrieved web content. They may expose users to malicious sites even when the input consists of ordinary, benign keywords. Risk exists both in retrieval—whether a harmful page is found—and generation—whether the LLM promotes it in the answer.

The distinction is important. ChatGPT Search retrieved many risky URLs but usually kept them out of the main answer. Perplexity Pro and Doubao cited a much larger proportion of retrieved malicious material. Doubao nevertheless reduced some harm by attaching warnings.

Second, query form changes risk. Natural-language phrasing was generally safer than keyword lists, possibly because it better communicates benign intent. Direct URL requests were substantially more dangerous because they encouraged the model to access and summarize the specified page. A URL previously buried in sources could become the main authority in the next response.

Third, the case studies show that the problem is not limited to known malicious domains. A newly created site can exploit an AIPSE’s tendency to trust confident online claims. The systems lacked human-like skepticism toward dubious popularity claims, requests for credentials, contradictory websites, and self-declared “official” status.

Fourth, AIPSEs nevertheless outperformed traditional search engines in this evaluation. They provided more useful answers and exposed users to malicious URLs on fewer comparison queries. This does not make them safe; it shows that direct synthesis can improve utility and reduce some exposure while introducing a distinct failure mode: the model may actively endorse, summarize, or operationalize harmful content.

Finally, the defense results show that post-processing should combine contextual interpretation with URL-level inspection. Prompt-only filtering missed many risky responses. Purely aggressive URL classification, as with XGBoost, caught every malicious URL but removed too much legitimate material. HtmlLLM achieved a stronger balance, while the agent’s iterative use of multiple forms of evidence could sometimes compensate for individual detector errors.

## 6. Contributions and Novelty

The paper makes three principal contributions:

- It presents the first systematic quantitative assessment of malicious-content and malicious-URL risks across seven production AIPSEs, using explicit threat and risk definitions and three realistic query types.
- It compares AIPSEs and traditional search engines on both user-centered utility and safety, finding that AIPSEs currently perform better on both while remaining materially vulnerable.
- It demonstrates practical attacks with two live-web case studies requiring only basic website construction and no SEO.
- It introduces an agent-based defense that combines content refinement with interchangeable URL detectors and preserves as much useful information as possible while adding safer alternatives and warnings.
- It proposes HtmlLLM, a GPT-4.1-based URL-and-HTML detector that achieved **0.838 precision, 0.807 recall, 0.822 F1**, and **78.3% response-level defense success**.
- It plans to release its prompt templates and defense code through Zenodo and GitHub.

## 7. Limitations and Caveats

The paper identifies several constraints:

- **Rapidly changing phishing sites:** Malicious pages frequently disappear or change. The team tried to control this by conducting experiments within five days of collection, but the results remain time-sensitive.
- **Manual evaluation:** Production AIPSEs lacked APIs suitable for automated web-search evaluation, so researchers manually recorded URLs and assigned risk labels.
- **Small dataset:** Resource constraints limited the core dataset to 100 keyword lists, 100 natural-language queries, and 457 URL queries.
- **Indeterminate URLs:** URLs still unresolved after three annotators were labeled none risk, which could undercount harm.
- **Provider remediation affected comparison:** All malicious URLs had been disclosed to AIPSE providers before the later AIPSE–TSE comparison. Providers had started responding, so that comparison may reflect mitigation unavailable during the earlier measurement.
- **Changing systems:** The evaluated production engines, their underlying models, retrieval systems, and access behavior can change.
- **Language effects:** Most queries were English, while Doubao and Kimi are Chinese-oriented systems. Their unusual natural-language results may therefore not generalize to other languages.
- **Narrow case-study platform:** Both practical attacks were evaluated through Perplexity to maintain a common indexing environment, although eight underlying model configurations were tested.
- **Simulated sites:** The case studies used entirely fictional platforms and content rather than stealing credentials or causing actual harm.
- **Detector trade-offs:** XGBoost’s perfect recall came with 83 false positives. HtmlLLM was more balanced but still missed 16 of 83 malicious URLs.
- **Scope of PhishLLM:** It was poorly matched to a test set in which 49.4% of malicious URLs were not phishing pages.
- **URL-query defense was not independently evaluated:** These responses were excluded because their links originated in already-covered keyword and natural-language answers.
- **Limited agreement on query naturalness:** The kappa score of 0.241 was only fair, reflecting differences in participant familiarity with specialized terminology.
- **Data cannot be released:** Some queries contain illegal-site keywords. After consultation with the IRB office and AIPSE support teams, the authors decided not to publish the malicious-URL dataset.
- **Information loss:** The defense reduced available information by approximately 10.7%, even though the paper considers this cost minor.

### Ethical safeguards

The researchers checked that their invented names did not correspond to real people or organizations. Every experimental page prominently displayed a warning that it was for testing only. No claimed backend APIs were implemented, and all visuals were custom-designed or AI-generated. The sites were kept low-ranking and intended to appear only under their unique keywords or domains.

Findings were disclosed to affected AIPSE providers. The malicious dataset was withheld, while prompts and defense code were designated for release.

## 8. Future Work or Open Questions

The paper explicitly suggests:

- Developing automated evaluation methods to replace labor-intensive manual URL recording and labeling.
- Expanding the dataset to improve the scale and generalizability of safety measurements.
- Continuing research on stronger safety mechanisms for AIPSE retrieval and generation.

The reported limitations also leave several open technical questions within the paper’s scope:

- How to maintain safety measurements when malicious sites and production AIPSEs change rapidly.
- How to retain XGBoost-like detection coverage without its large false-positive cost.
- How to improve HtmlLLM beyond its 16 missed malicious URLs.
- How to detect malicious pages that are convincingly camouflaged or falsely claim official status.
- How safety varies across languages, particularly for systems whose primary alignment language differs from the query language.
- How to automate combined contextual and URL-level verification while preserving more than the current defense’s available information.
- Whether the findings from Perplexity’s common indexing environment extend to equally controlled case studies across other production AIPSEs.

## 9. High-Level Takeaway (Plain Language)

AI search engines are often more helpful—and in this study safer—than ordinary link-based search engines, but they can still confidently repeat instructions from scam, phishing, or malware sites. A harmless-looking question can retrieve dangerous material, and directly asking about a URL can make the danger worse. Simple fake websites were enough to make eight model configurations reproduce malicious code or treat a phishing site as official. An agent that checks both the answer’s meaning and the underlying webpages removed or warned about most high-risk responses, but no tested defense achieved both perfect detection and high usability.