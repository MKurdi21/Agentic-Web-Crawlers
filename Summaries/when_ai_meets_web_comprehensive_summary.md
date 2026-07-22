# When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins

**Authors:** Yigitcan Kaya, Anton Landerer, Stijn Pletinckx, Michelle Zimmermann, Christopher Kruegel, and Giovanni Vigna  
**Affiliation:** University of California, Santa Barbara  
**Status:** Accepted to the 2026 IEEE Symposium on Security and Privacy

## 1. Background and Context

Large language models (LLMs) generate responses from a context containing several kinds of information:

- A **system prompt**, which contains the developer’s highest-priority instructions.
- The conversation history, usually labeled with roles such as `user`, `assistant`, and `system`.
- External content retrieved from documents, websites, or tools.
- Tool-use instructions that let the model call external services or functions.

Modern LLMs use an **instruction hierarchy**: developer-controlled `system` instructions should take precedence over lower-trust `user` messages and external data, which should normally appear under a low-privilege `tool` role. This separation is meant to make prompt injection harder.

A **direct prompt injection** places malicious instructions directly in user-controlled input. An **indirect prompt injection** hides instructions in external content—such as a document, search result, product review, or webpage—that is later supplied to the LLM. Prompt injection differs from jailbreaking: prompt injection concerns an attacker subverting an application developer’s intended behavior, whereas jailbreaking mainly concerns bypassing safeguards imposed by the LLM provider.

Public websites increasingly deploy customer-service chatbots through third-party plugins. These plugins offer inexpensive ways for non-expert website developers to:

- Connect to commercial LLM APIs.
- Customize chatbot system prompts.
- Scrape website content into retrieval-augmented generation (RAG) knowledge bases.
- Enable tools such as web search, appointment scheduling, Slack notifications, order tracking, or custom APIs.

Historically, website plugins have suffered from flaws such as cross-site scripting, SQL injection, cross-site request forgery, and remote code execution. Prompt-injection-specific weaknesses in LLM chatbot plugins, however, had received little systematic attention.

The paper argues that plugin implementation is a critical security layer. Even a well-trained LLM cannot reliably enforce its instruction hierarchy if a plugin lets an attacker label malicious content as a privileged `system` or `assistant` message.

## 2. Research Goal and Objectives

The paper presents the first large-scale security study of third-party AI chatbot plugins used on public websites. Its central goal is to determine whether plugin implementations and real-world chatbot configurations preserve or undermine built-in LLM safeguards against prompt injection.

The study has four main objectives:

1. Characterize 17 chatbot plugins and their deployment across more than 10,000 websites.
2. Identify plugin vulnerabilities that enable:
   - Direct injection through forged conversation histories.
   - Indirect injection through scraped website content.
3. Measure real-world chatbot configurations, especially system prompts, enabled tools, and underlying LLM choices.
4. Experimentally determine how plugin behavior, system-prompt design, content insertion method, and model selection affect attack success.

The authors also develop two prototype mitigations:

- **UGCBuster**, which identifies user-generated webpage content that should be excluded or isolated from RAG.
- LLM-assisted hardening of tool instructions against tool hijacking.

## 3. Methods (Approach/Design)

### 3.1 Selecting chatbot plugins

The study focuses on plugins that let website developers customize commercial LLMs and embed them as public-facing chatbots.

For WordPress, the researchers searched its marketplace for “ChatGPT Chatbot,” obtaining 116 results. They excluded plugins that:

- Had fewer than 50 installations.
- Did not use an LLM.
- Used LLMs for content generation rather than chatbots.
- Could not be deployed reliably in the researchers’ local setup.
- Did not support customization using website-specific data.

This produced seven WordPress plugins.

The researchers found generic, platform-independent commercial plugins through search engines and comparison articles. After excluding unpopular, non-functional, or locally unevaluable services, they selected ten. Three additional generic plugins, collectively used by about 300 websites, were excluded because they offered neither a free tier nor a suitable short-term subscription.

The final set contained **17 plugins: seven WordPress and ten generic plugins**. The paper anonymizes them as P1–P17.

### 3.2 Finding deployments in Common Crawl

Each plugin was associated with distinctive HTML markers. The researchers searched the August 2024 Common Crawl archive, which covered 38.3 million registered domains, and deduplicated matches by top-level registered domain.

They found **10,417 websites**, approximately **0.027%** of the archive’s domains. Additional Common Crawl snapshots from January 2023 through April 2025 were used to measure growth.

### 3.3 Plugin architectures and protocols

**Figure 1** diagrams two communication architectures:

1. **Type 1, used by WordPress plugins:**  
   Website visitor → website front end → website back end → LLM provider.  
   The site owner configures a self-funded LLM API key.

2. **Type 2, used by all selected generic plugins:**  
   Website visitor → website front end → commercial plugin provider → LLM provider.  
   The plugin provider manages API access, configuration, logging, and support in exchange for recurring fees.

Three plugins—P5, P9, and P13—use stateful WebSockets. The other 14 use stateless HTTP GET or POST requests. HTTP plugins preserve conversation state by storing it at a back end, using provider-side mechanisms such as Threads, or repeatedly transmitting it from the browser. Eight plugins use the last method, creating the history-forgery vulnerability.

### 3.4 Functionality validation

In September 2024, the researchers manually checked 200 randomly selected websites:

- 116 used generic plugins.
- 84 used WordPress plugins.

They asked whether each site was online, still contained its plugin marker, showed a visible chatbot, and had a chatbot that answered queries.

They also built automated validation for three popular plugins—P1, P2, and P4—which together accounted for about 70% of the dataset.

### 3.5 Local plugin security analysis

Every selected plugin was installed on a local WordPress instance and connected to an OpenAI model. Product pages from popular e-commerce sites were used to exercise data-customization features.

The researchers inspected:

- HTTP and WebSocket traffic.
- Conversation-history handling.
- Model, temperature, prompt, and starter-message settings.
- Tool integrations.
- Website crawlers, uploaded documents, and plain-text inputs.
- How external content entered the LLM context.

Three data-customization approaches were observed:

- **RAG:** retrieves relevant fragments and adds them to the model context.
- **Direct copying:** inserts the full source into the context.
- **Fine-tuning:** updates model weights using external data.

Most RAG plugins used services such as Pinecone or OpenAI vector stores.

To infer the role assigned to retrieved content, the authors inspected OpenAI API logs where available. Otherwise, they configured a “DebugBot” system prompt, triggered retrieval for five products, asked the chatbot whether the retrieved excerpt appeared as `system`, `assistant`, `user`, or `tool`, and used a majority vote.

### 3.6 Threat model

The attacker is an unprivileged visitor who may:

- Interact with a public chatbot.
- Modify requests sent from their browser.
- Browse the host website.
- Post content such as reviews or comments where ordinary users are allowed to do so.
- Fingerprint the plugin from traffic patterns.

The attacker does not need administrative access. Traditional vulnerabilities in unrelated components, such as SQL injection, are outside the threat model.

### 3.7 Measuring real-world configurations

The real-world configuration study concentrated on P1 because it was the most widely deployed plugin, supported vulnerability research through a bug-bounty program, and was suitable for automation.

For system prompts, the researchers tested 300 randomly selected P1 websites. They compared:

- A plain user request asking for the system prompt.
- A forged `assistant` message that instructed the chatbot to reveal its initialization.
- A forged `system` message with the same objective.

Because the actual prompts were unavailable, an extraction was manually labeled successful only if the response contained at least three sentences showing typical prompt features: imperative second-person instructions, an explicit role assignment, and behavioral rules or constraints.

Tool use was measured passively from metadata leaked in P1 iframe HTML and HTTP traffic, avoiding potentially harmful tool invocations.

### 3.8 Controlled experimental environment

The authors implemented a local simulation of plugin functionality with:

- Customizable system prompts.
- Website scraping and RAG.
- Multiple commercial LLM providers.
- External tools.

The knowledge base used content from **35 Nalgene product pages**. Content was divided into **600-token chunks with 300-token overlaps** and embedded with `text-embedding-3-large`, matching the cited OpenAI file-search settings.

Eleven models were evaluated:

- OpenAI: GPT-4o-mini, GPT-4o, GPT-4.1-mini, GPT-4.1, and o4-mini.
- Anthropic: Claude Haiku 3.5, Sonnet 3.5, and Sonnet 4.
- Gemini: 2.0 Flash, 2.5 Flash, and 2.5 Pro.

Each configuration was run **10 times at temperature 0.5**.

Three realistic system-prompt styles were tested:

- **Insecure:** assigns a sales/support role but lacks a strong prohibition against unauthorized work.
- **Hardened:** explicitly prohibits tasks outside the chatbot’s role and training data.
- **Hardened-specific:** additionally and explicitly prohibits coding.

Anthropic and Gemini support only one top-level system message, so experiments with additional forged `system` messages applied only to OpenAI models.

### 3.9 Direct-attack tasks

The controlled direct-injection study tested:

1. **System prompt extraction:** force the model to reveal its initialization.
2. **Task hijacking:** force a sales chatbot to produce Python Fibonacci code.
3. **Tool hijacking:** override a Slack notification tool so that it sends a message to `#general`, using `www.abcxyz.com` as an attacker-supplied topic rather than the configured channel and topics.

The attack was injected as `system`, `assistant`, or `user`, where supported.

### 3.10 Indirect context-hijacking task

The attacker’s malicious product comment instructed the chatbot to use Tavily search for **“Hydro Flask,”** a competing bottle brand, and summarize results with links.

A benign user then asked about the target product. The attack succeeded if the model:

- Called `tavily-web-search` with `query=Hydro Flask`.
- Included URLs from the tool’s results in its response.

Five content-insertion modes were tested:

- Appending retrieved material to the existing system prompt (**SA**).
- A separate `system` message (**S**).
- A separate `assistant` message (**A**).
- A separate `user` message (**U**).
- A low-privilege `tool` message (**T**).

Retrieved content was tested both with and without enclosing data tags. The experiment crossed these modes with the three system-prompt styles and 11 models.

### 3.11 Ethical precautions

For live measurements, targets received multiple opt-out mechanisms. Requests contained a research contact in the User-Agent; the scanning address pointed to a public research and opt-out page; and the same information was supplied through a DNS TXT record.

Data remained internal. Interactions were confined to temporary sessions and did not alter websites or chatbot configuration, although they could create ordinary dashboard logs. The researchers did not post malicious material to real websites.

## 4. Results and Findings

### 4.1 Ecosystem size and growth

**Table 1** reports:

| Plugin type | Plugins | Sites, Aug. 2024 | Sites, Apr. 2025 | Top-1M share, Aug. 2024 | Top-1M share, Apr. 2025 |
|---|---:|---:|---:|---:|---:|
| WordPress | 7 | 3,534 | 5,266 | 4.4% | 4.7% |
| Generic | 10 | 6,883 | 12,208 | 9.1% | 8.1% |
| Total | 17 | 10,417 | 17,474 | 7.5% | 7.1% |

The ecosystem therefore grew from 10,417 detected sites in August 2024 to **17,474 in April 2025**, an increase of nearly 50% during 2025 as described by the paper. Generic-plugin deployments continued rising rapidly, while WordPress-plugin growth slowed.

**Figure 2, left**, plots chatbot-enabled websites from January 2023 to April 2025. The total rises approximately linearly, with generic deployments accounting for most growth.

**Figure 2, right**, plots registration dates for chatbot-site domains beginning in January 2022. It shows a strong registration surge immediately after ChatGPT’s November 2022 release. About **35%** of identified websites were more than ten years old, while **20%** had been registered in the previous two years.

In the August 2024 list:

- **783 sites, or 7.5%,** were in the Tranco Top 1 Million.
- **171 sites, or 1.6%,** were in the Top 100,000.
- Generic-plugin sites were more frequently in the Top 1 Million than WordPress-plugin sites: **9.1% versus 4.4%**.
- More than 80% of sites ranked between the Top 1 Million and Top 3 Million were over five years old.
- Nearly 50 active `.gov` or `.edu` domains appeared outside the Top 1 Million.

Deployments included local governments, universities, charities, manufacturers, and international airports, showing that these plugins are used on both obscure and high-stakes sites.

### 4.2 Functionality in practice

Among 200 manually checked sites:

- **195** were online.
- **180** remained marked as containing a target plugin.
- **162** displayed a visible chatbot.
- **125** responded to queries.

Thus, the overall functional-deployment rate was **62.5% (125/200)**.

The 162 visible chatbots included 69 type-1 and 93 type-2 deployments. Of the 37 visible but non-functional chatbots:

- 30 used type-1 plugins.
- Type-1 failures included:
  - 13 “out of OpenAI quota” errors.
  - 2 deprecated-model errors.
  - 2 cases with no default model.
- Seven used type-2 plugins.
- Type-2 errors included:
  - 3 “unavailable” responses.
  - 1 exceeded-plan error.

Automated testing found functionality rates of:

- **76% for P1.**
- **53% for P2.**
- **96% for P4.**

P1 and P4 are provider-managed type-2 plugins; P2 is a type-1 plugin. P2’s functionality increased to **68% among Top-1M sites** and **74% among Top-100K sites**, suggesting that high-traffic operators maintain deployments more reliably.

### 4.3 Languages and site categories

**Figure 5, left** shows a heavily English-dominated but highly multilingual ecosystem:

- Chatbot sites covered **93 languages**.
- English, Spanish, German, French, and Portuguese together accounted for **81%**.
- The remaining **19%** covered 88 languages, including low-resource languages such as Uzbek and Bosnian.

The paper notes that LLMs tend to perform less reliably and comply more readily with malicious instructions in low-resource settings, potentially increasing risk.

**Figure 5, right** groups sites into categories. Business, e-commerce, education, personal blogs, health, technology, and finance together covered **72%** of deployments. The figure’s bars show business as the largest named category, with e-commerce next; education, blogs, health, technology, and finance form smaller but substantial groups. The supplied visual does not provide exact readable percentages for each individual bar. Sensitive settings such as health increase the potential impact of failures.

### 4.4 Plugin-level risk inventory

**Table 2** catalogs protocols, tool support, site counts, direct-injection roles and logging, third-party scraping, external-content roles, and indirect-injection logging.

The central findings are:

- **Eight HTTP plugins—P1, P2, P4, P7, P11, P12, P16, and P17—accepted browser-supplied message histories without authenticating their integrity.**
- Together, they were deployed on about **8,000 websites**.
- All except P7 allowed forged messages in both `system` and `assistant` roles; P7 allowed `assistant` injection.
- None initially gave administrators a faithful dashboard view of the forged requests.
- **Fifteen of 17 plugins** scraped third-party webpage content.
- **Seven plugins inserted retrieved material as `system` messages**, violating the intended low-trust treatment of external data.
- P7 and P11 were the only affected plugins reported as logging retrieved data in their plugin dashboards; some additional events were visible only through LLM-provider logs.
- P8 used OpenAI’s proprietary RAG tool.
- P14 supported scraped-content customization only through fine-tuning.

Site counts in Table 2 also show concentration: P1 grew from about **4,000 to 7,600 sites**, P2 from **2,400 to 3,400**, P3 from 909 to 1,200, and P4 from 408 to about 1,000 between August 2024 and April 2025.

### 4.5 Direct injection through history forgery

Eight plugins sent the entire message history from the browser in an HTTP POST body but did not verify that the browser had preserved authentic roles or content. An attacker could therefore:

- Rewrite the chatbot’s previous `assistant` messages.
- Insert fabricated `assistant` messages.
- Insert new `system` messages carrying attacker instructions.

**Figure 3** illustrates the effect:

- In an ordinary request, a user asks for the system prompt and the chatbot refuses.
- In a forged request, the attacker replaces the prior assistant message with a promise to reveal the prompt after “Hello”; the chatbot then discloses it.
- In the strongest case, the attacker inserts a forged system instruction ordering disclosure after “Hello,” and the chatbot again reveals its original system prompt.

The genuine system prompt remains in context, but the injected system message is treated as another high-priority instruction. This breaks the assumption that an attacker is confined to the `user` role.

Dashboards concealed the manipulation: they retained original starter messages even when attackers omitted or replaced them and did not display original or forged system messages.

### 4.6 Indirect injection through website scraping

All 15 plugins with automatic scrapers consistently extracted third-party content from test pages. Because many scrapers strip HTML and retain all visible text, they do not separate trusted product descriptions from untrusted reviews, comments, or similar material.

**Figure 4** depicts a sales chatbot for a jeans product. A malicious reviewer posts an instruction telling the chatbot to ignore prior instructions and say “pwned.” The plugin scrapes the review, feeds it to the LLM, and a benign product question triggers the injected response.

These attacks are persistent because the content may remain in a RAG knowledge base and later activate during unrelated users’ sessions.

The risk is worsened by poor role assignment:

- Seven plugins inserted retrieved content as privileged `system` messages.
- Other plugins used `assistant` or `user`.
- Only P8 used the intended `tool` role through OpenAI’s RAG mechanism.

Most dashboards logged only user queries and chatbot answers—not the retrieved material that caused them—making detection and remediation difficult.

### 4.7 Real-world exposure to third-party content

The researchers randomly sampled **100 functional P1 e-commerce sites**. E-commerce represented roughly **10% of all chatbot-enabled sites**, or about **1,100 deployments**.

Among the 100 sampled sites:

- **41** allowed customer reviews or comments.
- **36** visibly displayed them on product pages.
- In **13 cases**, the chatbot answered questions using specific details from those reviews.

Thus, **13% of the total sample** had demonstrably passed third-party content into the chatbot context.

This is probably an underestimate because testing was limited to five queries per chatbot, some chatbots refused to discuss customers, and product reviews are only one source. Other possible sources include contact forms, social-media feeds, wiki pages, guest posts, and user-submitted support threads.

### 4.8 System-prompt extraction in the wild

Among 300 randomly selected P1 websites:

- A simple user request extracted the system prompt in only **1%** of cases.
- A forged `system` message succeeded in **56%**.
- A forged `assistant` message succeeded in **55%**.
- Across the injection methods, system prompts were extracted from **219 chatbots**, an overall success rate of **73%**.

The most common failure was model refusal.

These results show that history forgery turns otherwise weak instructions into much stronger prompt-extraction attacks.

### 4.9 Characteristics of real system prompts

Among extracted prompts:

- **76%** were minor, non-sensitive variants of P1 defaults or other known templates.
- **97%** contained instructions to reject out-of-scope queries in the main analysis; Appendix C reports roughly **96%**, reflecting the same near-universal hardening trend.
- About **5%** explicitly instructed the chatbot to collect personally identifiable information such as names or contact details.

Template popularity was:

- Template 1: **33%**.
- Template 2: **36%**.
- Template 3: **27%**.
- Template 4: **4%**.

**Figure 6** plots cumulative distributions for three similarity measures: 3-gram Jaccard similarity, 3-gram overlap coefficient, and embedding cosine similarity. The overlap measure is an upper bound on Jaccard and captures how much of the shorter text appears in the longer one. By this measure:

- **76%** of real prompts contained more than **80%** of a known template.
- **31%** were exact copies.

Common modifications added a bot name, business-specific information, requests for contact information, or a preferred tone such as concise, polite, persuasive, or sassy.

The paper emphasizes that templates are useful starting points but are static, predictable, and often insufficiently adapted to a site’s functionality, regulation, and threat model.

### 4.10 Real-world tool adoption

In April 2025, P1 leaked metadata identifying **144 unique chatbots with activated tools**. P1 had introduced tool support only in February 2025, indicating rapid uptake.

The most common tools were:

- Tavily Search: **43 chatbots**.
- Calendly: **40**.
- Slack Notification: **10**.
- Custom developer-defined tools: **42**.

Custom tools included order tracking, human-agent escalation, and proprietary APIs. Elsewhere, leaked metadata suggested capabilities such as database access, password recovery, and email generation.

P1 placed tool instructions directly into the system prompt using a formatted tool block. Its HTTP traffic also exposed tool arguments and raw outputs before the model processed them, revealing capabilities to attackers.

### 4.11 Controlled direct-injection results

**Table 3** reports 10 trials for every applicable combination of attack, prompt type, injection role, and model.

#### Role is the dominant plugin-level factor

Across tasks, `user`-role attacks were less effective than attacks injected as `assistant` or `system`. This confirms that role hierarchy provides meaningful protection when the plugin preserves it.

#### System prompt extraction

Across prompt designs:

- `system` injection succeeded in roughly **60%** of cases.
- `assistant` injection succeeded in roughly **30%**.
- `user` injection was much less successful and fell to essentially zero under hardened prompts.

The overall averages per ten trials in Table 3 were:

- Insecure prompt: S **5.4**, A **4.1**, U **2.8**.
- Hardened prompt: S **6.0**, A **3.8**, U **0**.
- Hardened-specific: S **6.0**, A **4.2**, U **0.1**.

Hardening did not reliably stop privileged prompt extraction because the attack targeted provider confidentiality safeguards from an elevated role.

#### Task hijacking

Hardening clearly helped against unauthorized coding:

- Insecure prompts allowed nearly twice as many successes as hardened prompts.
- Hardened prompts allowed roughly twice as many as prompts that explicitly prohibited coding.
- Under an insecure prompt, even ordinary user-role injection succeeded in approximately **20%** of cases.
- Under the hardened-specific prompt, user-role task hijacking had **0% success**.

Overall averages per ten trials were:

- Insecure: S **9.8**, A **5.9**, U **1.0**.
- Hardened: S **6.2**, A **3.8**, U **0**.
- Hardened-specific: S **2.4**, A **1.5**, U **0**.

This means plugins that preserved user-only input reduced attack success, while task-specific prompt rules supplied additional protection.

#### Tool hijacking

Tool hijacking behaved differently. General system-prompt hardening did not stop it and sometimes increased success.

Overall averages per ten trials were:

- Insecure: S **3.0**, A **4.8**, U **3.7**.
- Hardened: S **4.0**, A **6.7**, U **3.8**.
- Hardened-specific: S **6.0**, A **7.1**, U **3.7**.

Depending on provider, even user-role attacks succeeded **20–100%** of the time. This shows that protecting the chatbot’s general role does not necessarily protect each attached tool’s instructions.

#### Model differences

The experiments found:

- Gemini models were the most vulnerable overall and often complied even with `user` injections.
- Larger models were not consistently safer.
- OpenAI’s smaller mini models sometimes outperformed larger OpenAI models.
- Anthropic Haiku was generally less robust than the larger Sonnet models.
- Anthropic models resisted prompt extraction and task hijacking better.
- OpenAI models were more resistant to tool hijacking.
- Robustness therefore depended on both provider and attack type.

### 4.12 Controlled indirect-injection results

**Table 4** reports context-hijacking results over system-prompt designs, wrapped versus unwrapped content, insertion roles, and models.

The main finding is that inserting retrieved content under the **`tool` role was consistently the safest approach**. Non-standard modes produced as much as **five times higher attack success**, depending on configuration.

For unwrapped content, the overall average successes per ten trials were:

- Insecure: SA **4.1**, S **3.8**, A **1.5**, U **3.1**, T **1.3**.
- Hardened: SA **3.5**, S **2.4**, A **1.0**, U **3.8**, T **0.6**.
- Hardened-specific: SA **3.2**, S **2.4**, A **1.5**, U **3.5**, T **0.9**.

For wrapped content:

- Insecure: SA **3.9**, S **0.8**, A **1.8**, U **2.4**, T **0.9**.
- Hardened: SA **3.0**, S **0.2**, A **2.1**, U **3.1**, T **0.9**.
- Hardened-specific: SA **2.8**, S **0.4**, A **1.8**, U **3.2**, T **0.7**.

Appending retrieved content to the system prompt was especially risky for larger advanced models. Success reached **100%** in some configurations involving GPT-4.1, o4-mini, or Sonnet 4. The authors attribute this to stronger models following additional system-level instructions more effectively. Smaller models such as Haiku 3.5, GPT-4o-mini, and Gemini 2.0 Flash were sometimes more robust in this particular insertion mode.

System-prompt hardening reduced indirect attack success by about **20–40%**, but even a hardened prompt combined with correct `tool` insertion still had approximately **5–10% success**.

Wrapping retrieved data in tags provided moderate, model-dependent protection. OpenAI models benefited most, possibly because they had learned to treat marked data fields as non-instructional content. This defense was not standardized among plugins.

Gemini was again the least robust overall, while Anthropic was the most resilient.

### 4.13 Alternative attack prompts

Appendix B tested:

- **Blunt prompts**, which directly state the desired behavior.
- **Ignore-and-instruct prompts**, which begin by telling the model to ignore prior instructions.

Exploiting plugin vulnerabilities increased success by as much as approximately **threefold**. In indirect-injection settings, blunt instructions were sometimes about **four times more effective** than the main role-override prompts. Ignore-and-instruct was the least effective, probably because models are explicitly trained against this familiar pattern.

### 4.14 Additional security weaknesses

The researchers found several problems beyond prompt injection:

- **Visible system prompts:** P7, P8, P16, and P17 exposed administrator-written system prompts as plaintext.
- **Exposed API key:** P12, active on more than 130 sites in August 2024, connected to OpenAI directly from the visitor’s browser and exposed its API key, enabling credit theft or exhaustion.
- **Privacy leaks:** Some chatbots disclosed email addresses and past customer-service interactions.
- Plugins provided no built-in filtering for sensitive data or personally identifiable information; sanitization was left to non-expert website developers.

### 4.15 Prototype defenses

#### UGCBuster

UGCBuster detects user-generated content by:

1. Grouping webpage content by unique paths in the HTML tree.
2. Asking an LLM to identify structural and textual signs such as usernames, comments, timestamps, ratings, or question-and-answer threads.
3. Promoting related detections to shared parent containers.
4. Merging overlapping containers.
5. Assigning confidence scores.
6. Producing machine-readable paths, evidence, and sample text so developers can exclude or specially format those containers.

It was manually validated on **10 e-commerce sites with three pages each**, including irregular and outdated HTML. It consistently found the correct UGC containers, produced **one false positive**, and cost about **$0.05 per page**.

#### Tool-instruction hardening

An LLM rewrote tool instructions to add:

- Generic rules to ignore requests that alter whether or how a tool is called.
- Tool-specific constraints, such as permitting only preconfigured Slack channels and topics.

Repeating the experiments with these hardened instructions reduced attack success by **40–75%**.

### 4.16 Disclosure outcomes

In October 2024, the history-forgery vulnerability was disclosed to P1, P2, P4, P7, P11, P12, P16, and P17.

Within three days, P1, P2, P7, and P12 responded.

- **P1** moved message handling server-side and adopted stronger prompts by December 2024. Its new prompts explicitly prohibited coding. Its default tool instructions nevertheless remained insecure.
- **P2** remained vulnerable because some workflows intentionally allowed message modification, but it added warnings when forged messages were detected.
- The other affected history-forgery plugins did not respond or had not acted.
- Indirect-injection risks were disclosed to P1 and P2, but neither mitigated them.
- P7 promptly fixed plaintext system-prompt exposure.
- P12 partially fixed its exposed API key, but the issue was not fully addressed even after another notification.

## 5. Analysis and Interpretation

The findings support the paper’s central argument: plugin-level design can nullify security properties built into an LLM.

The instruction hierarchy assumes that attackers occupy the low-privilege `user` role and that retrieved data occupies the `tool` role. History forgery lets an attacker change a single role token—from `user` to `system`, for example—and gain developer-level authority. This creates a **distribution shift**: the model was trained to refuse lower-priority attempts to override higher-priority instructions, not to handle malicious text incorrectly labeled as a trusted system message.

The same issue appears in RAG. When plugins place untrusted website text into system prompts, the model cannot distinguish a product description from a malicious customer review. Larger models may actually become more vulnerable in this setting because their improved ability to follow system instructions makes them more responsive to malicious instructions appended there.

The controlled experiments distinguish two kinds of protection:

- **System-prompt hardening** is useful when the attack tries to change the chatbot’s overall assigned task. Explicitly prohibiting coding, for example, stopped user-role coding attacks.
- **Tool-instruction hardening** is separately necessary when an attack targets tool arguments or invocation conditions. A secure general-purpose system prompt does not automatically secure Slack, search, or custom API instructions.

Model choice alone cannot resolve the problem because robustness varies by provider, model size, and attack objective. A model that resists prompt extraction may still be weak against tool hijacking.

The risk is growing because the ecosystem is moving from isolated text generation toward actions with external effects. In early stages, injection mostly changed chatbot text. By April 2025, over 100 P1 deployments had enabled tools, including 42 custom tools potentially connected to databases, order systems, account recovery, or email. Such integrations can turn misleading output into persistent operational harm.

The authors therefore conclude that basic interface discipline—authenticated history, correct role assignment, data isolation, and hardened tool specifications—is essential before more sophisticated defenses can work as intended.

## 6. Contributions and Novelty

The paper makes the following contributions:

- It provides the **first large-scale measurement study** of prompt-injection vulnerabilities in third-party web chatbot plugins.
- It characterizes **17 plugins across more than 10,000 sites**, later measuring 17,474 deployments in April 2025.
- It discovers a message-history integrity failure in eight plugins used by about 8,000 websites.
- It demonstrates that forged `system` and `assistant` messages increase the effectiveness of direct attacks by approximately **3–8 times** in the paper’s overall characterization.
- It shows that 15 plugins indiscriminately scrape third-party webpage content, making persistent indirect injection practical.
- It provides evidence that **13% of a sampled set of e-commerce sites** had already incorporated customer-authored content into chatbot context.
- It measures real-world system-prompt templates, prompt leakage, LLM tools, and tool adoption.
- It systematically evaluates 11 commercial models across direct and indirect attacks, system-prompt styles, injection roles, RAG insertion modes, and data wrapping.
- It demonstrates that non-standard RAG insertion can increase success by up to **fivefold**.
- It identifies the separation between system-prompt security and tool-instruction security.
- It develops two lightweight prototypes: UGCBuster and LLM-assisted tool-instruction hardening.
- It responsibly disclosed multiple vulnerabilities, leading the most widely adopted plugin to move message handling server-side and strengthen its prompts.

## 7. Limitations and Caveats

The paper identifies or implies several constraints:

- HTML-marker scanning may underestimate the chatbot ecosystem. Some plugins are hidden behind server-side or generic chat functionality.
- The study deliberately excludes enterprise platforms such as Zendesk, Tidio, and Intercom, so results concern the plugin-based long tail rather than all web chatbots.
- Three generic plugins, used by approximately 300 sites, were excluded because they could not be tested under a free or short-term plan.
- A Common Crawl marker does not guarantee that a chatbot remains visible or functional; the manual sample found only a 62.5% end-to-end functional rate.
- Fully automated validation was possible for only three plugins because implementations varied in protocols, iframes, authorization, loading, versions, and DOM patterns.
- Roles assigned by some generic plugins had to be inferred by chatbot probing rather than directly inspected.
- The researchers did not possess ground-truth prompts for live sites. Prompt extractions were classified through manually defined linguistic criteria.
- Real-world indirect exposure was evaluated only on 100 P1 e-commerce sites and with at most five queries per chatbot.
- The real-world exposure estimate likely misses hidden review ingestion and non-review sources.
- Ethical constraints prevented posting malicious content on live sites, so actual real-world exploitation was not attempted.
- Live system-prompt extraction changed no persistent configurations but could create logs in plugin dashboards.
- Advanced LLM fingerprinting was not performed; the model experiments instead used broadly supported commercial models.
- The controlled attacks were intentionally simple proofs of concept, not new or optimized attacks.
- The experimental RAG knowledge base came from 35 pages belonging to one water-bottle retailer, limiting the variety of controlled content.
- Custom tools were not invasively tested, so their real-world exploitability remains unknown.
- Calendly was excluded from tool experiments because it only exposed public calendar links.
- Stronger defenses exist, but the paper assumes their engineering and API costs make widespread plugin adoption unlikely.
- UGCBuster was tested on only 10 e-commerce sites, three pages each.
- Tool-hardening effectiveness was evaluated against the study’s attacks, not arbitrary adaptive attackers.
- The program committee’s meta-review specifically notes that the proposed defenses’ security against strong adaptive attacks remains unclear.
- Some exact values in the small Figure 5 bars are not printed legibly; the text supplies only the combined language and category totals.

## 8. Future Work or Open Questions

The paper identifies several priorities:

- Evaluate stronger, adaptive prompt-injection attacks against UGCBuster, content formatting, and hardened tool instructions.
- Develop defenses that remain robust when attackers know and adapt to the protection mechanism.
- Explore attacks that combine LLM weaknesses with traditional web vulnerabilities such as SQL injection.
- Establish standardized plugin interfaces that:
  - Keep conversation history server-side.
  - Authenticate message state.
  - Restrict visitors to `user` messages.
  - Place external data in `tool` messages.
  - Log the complete context supplied to the LLM.
- Develop secure and customizable system-prompt templates tailored to specific functions, regulations, and changing threats.
- Investigate algorithmic prompt generation and LLM-assisted prompt authoring rather than relying on static defaults.
- Create independently hardened instructions and access controls for each tool.
- Study custom tools, especially those connected to databases, account recovery, order management, email, and proprietary APIs.
- Add plugin-level mechanisms for filtering sensitive data and personally identifiable information.
- Improve UGC isolation and assess it across more site types and irregular page structures.
- Standardize wrapping and formatting for retrieved content.
- Continue monitoring low-resource languages and high-stakes sectors.
- Broaden AI-security research beyond flagship agents and copilots to small-team, plugin-based deployments.

## 9. High-Level Takeaway (Plain Language)

Many websites add AI chatbots through convenient third-party plugins, but some of those plugins handle messages and website data in unsafe ways. Eight plugins let visitors forge supposedly trusted system or chatbot messages, and 15 scrape webpage material without separating a store’s own information from customer-written content. These mistakes can make simple prompt injections several times more successful and can even cause chatbots to misuse connected tools.

The main lesson is that an LLM’s built-in protections work only when the surrounding plugin preserves the intended trust boundaries. User input must stay in the `user` role, retrieved data should stay in the `tool` role, message histories must be authenticated, and every connected tool needs its own hardened rules.