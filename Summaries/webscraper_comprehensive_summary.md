# **Webscraper: Leverage Multimodal Large Language Models for Index-Content Web Scraping**

**Authors:** Guan-Lun Huang and Yuh-Jzer Joung  
**Affiliation:** Department of Information Management, National Taiwan University, Taipei, Taiwan

## **1. Background and Context**

Web crawling and scraping supply data for large-scale applications, including the pre-training of large language models. Timely and accurate scraping is especially valuable for news websites because their rapidly updated information supports applications such as public-opinion analysis and decision-making by governments, businesses, and other organizations.

Modern websites, however, are difficult to scrape with traditional techniques:

- Older websites generally embedded their content directly in static HTML.
- Contemporary sites commonly use JavaScript to load content dynamically, including through infinite scrolling.
- Users may need to click buttons, scroll, or perform other interactions before the desired information appears.
- Pages contain irrelevant material such as advertisements and scripts.
- Expert-written crawlers are often tied to a particular page structure. They require substantial manual work and may break whenever the website changes.

The paper divides modern web scraping into two connected stages:

1. **Web navigation:** An autonomous agent interacts with the website to expose the desired information.
2. **Web Information Extraction (WIE):** The exposed information is parsed from the website’s semi-structured HTML.

Previous multimodal web agents such as SeeAct and WebVoyager use visual understanding to operate browsers, although the paper reports that their abilities decline in more complex desktop environments. More general systems such as Anthropic’s Computer Use employ an iterative **Observe–Reason–Act** process: the agent observes the current screen, reasons about the next step, performs an action, and repeats.

Web information extraction has separately progressed from brittle, rule-based wrappers to LLM-based methods. Although modern LLM approaches can achieve high accuracy, their computational expense makes them difficult to use for large-scale scraping. Recent systems therefore use an LLM once to generate a reusable, inexpensive scraper. AutoScraper, for example, progressively generates and validates XPath expressions. The paper argues that XPath-based approaches remain oriented toward finding individual data points rather than comprehensively extracting a large structured collection, such as every relevant product listed on a catalog page.

The resulting research gap is the absence of a unified framework that combines advanced navigation with an efficient, data-centered strategy for extracting many related records from dynamic websites.

### **The index-and-content architecture**

Webscraper specifically targets the common **index-and-content** website design:

- An **index page** serves as a directory containing many items and links—for example, a news category, product-search results, a video gallery, or a social-media feed.
- Each **content page** is reached through an index-page link and contains detailed information about one item, such as a complete news article or product description.

This structure appears across news portals, e-commerce sites, video platforms, and social-media services.

---

## **2. Research Goal and Objectives**

The paper’s main objective is to turn a general-purpose multimodal GUI agent into a specialized, autonomous scraper for dynamic index-and-content websites.

Webscraper is designed to:

- Navigate interactive websites using screenshots and human-like mouse and keyboard operations.
- Decide autonomously when browser interaction is needed and when HTML should be parsed directly.
- Extract many related records into one structured output.
- Handle repeated operations such as pagination, parsing, merging, and deduplication.
- Improve accuracy over an unmodified general-purpose agent.
- Generalize beyond news websites to other index-and-content domains, particularly e-commerce.

The paper presents three explicit contributions:

1. Demonstrating that MLLM-based prompt design is feasible for index-and-content scraping.
2. Improving extraction accuracy by combining an MLLM agent with specialized extraction tools.
3. Testing whether the framework generalizes to e-commerce scraping.

The study does not state formal hypotheses or numbered research questions. Its experiments effectively test whether structured prompting and purpose-built tools improve scraping accuracy over a zero-shot Computer Use agent, and whether those benefits extend to a second domain.

---

## **3. Methods (Approach/Design)**

### **3.1 Task specification and expected output**

Each scraping task begins with one natural-language prompt defining:

- The target website.
- The scope of the crawl.
- The fields to extract.

The paper gives the following kind of task as an example: scrape the first two pages of the BBC US–Canada news section and retrieve each article’s title, link, and content.

A successful task produces a single JSON file containing a list of objects. Each object represents one extracted item and includes its requested fields.

### **3.2 Foundational agent**

Webscraper uses Anthropic’s **Computer Use** framework as its base. This framework supplies an MLLM-driven agent that receives both the user’s task and a system prompt, examines the environment, reasons about the task, and selects tools.

The experiments used the model identified as `claude-3-7-sonnet-20250219`. Temperature was set to **0** to reduce sampling variability.

### **3.3 Native environment tools**

The base agent can use three native tools:

- **Computer:** Provides visual access and GUI actions, including viewing the screen, moving the pointer, clicking, and scrolling. This is the primary means of navigating a website in a human-like way.
- **Bash:** Supports command-line operations such as managing files, running scripts, and issuing network requests such as `curl`.
- **Str Editor:** Allows the agent to create, inspect, and modify files, including extraction scripts.

### **3.4 Custom tools**

Webscraper adds two specialized tools.

#### **Parse Tool**

The Parse Tool converts raw HTML into structured data by outsourcing the entire parsing operation to a stronger reasoning model. It sends the HTML and the user’s requirements to that model, which writes a task-specific Python script. The script is then executed in a GPT code-interpreter environment to generate the structured output.

The methodology section refers to the delegated model as **GPT-o3**, while the experimental settings more specifically identify it as **OpenAI GPT-o3-mini**.

The authors give three reasons for this delegation:

- It protects the main agent’s limited context window from verbose code-generation and execution details.
- It assigns the critical index-page parsing task to a more capable specialized reasoning model, intended to improve the reliability of the initial data collection.
- It keeps the central system prompt focused on high-level strategy rather than detailed parsing instructions.

#### **Merge Tool**

The Merge Tool combines lists collected over multiple scraping iterations. It:

- Aggregates structured records.
- Deduplicates repeated entries.
- Consolidates results across operations such as pagination.

This is important when a task must process several index pages before producing one final dataset.

### **3.5 Guiding prompt and staged procedure**

The framework uses a crawler-specific system prompt to coordinate a structured **five-stage extraction process**. This guidance is appended to the default Computer Use system prompt.

The supplied article extraction states that five stages exist but does not enumerate or describe the five stages individually. Their exact names, ordering, and detailed instructions therefore cannot be recovered from the provided text.

### **3.6 System architecture and Figure 1**

**Figure 1** presents the overall architecture. The Computer Use agent receives the user and system prompts, then selects from two tool groups:

- Native environment tools, shown at the upper right.
- Custom scraping tools, shown at the lower right and highlighted in yellow.

The central prompt coordinates the agent’s use of these tools so that it can navigate the site, parse HTML, merge repeated results, and produce structured data. The extracted figure caption and surrounding text identify the components and their relationships, but no additional labels or processing details beyond those described above are recoverable from the provided extraction.

### **3.7 Experimental configurations**

The authors compared three configurations:

1. **Baseline Agent**
   - A zero-shot use of the default Computer Use agent.
   - Receives the scraping request directly.
   - Does not receive the crawler-specific prompt.
   - Does not have access to the custom Parse or Merge tools.

2. **Webscraper (Prompt Only)**
   - Adds the guiding system prompt to the baseline agent.
   - Disables the functional Parse and Merge tools.
   - Instead, embeds descriptions of the tools’ intended operations in the prompt, allowing the agent to imitate the workflow with its ordinary capabilities.

3. **Webscraper (Prompt + Tool)**
   - The complete proposed framework.
   - Includes both the guiding prompt and working Parse and Merge tools.

Each run began with a clean Firefox browser instance.

### **3.8 News benchmark**

The primary benchmark consisted of **six mainstream Chinese- and English-language news websites**. They represented different structures and interaction patterns, including:

- Infinite scrolling.
- Button-based pagination.
- Dynamic content loading.

The extracted paper does not provide all six website names. It mentions LTN as one example but otherwise labels sites generically in the reported stability table.

For each site, the researchers created a **Golden**, or ground-truth, dataset using a manually written deterministic crawler. It contained the exact:

- Article URLs.
- Titles.
- Article contents.

These records served as the evaluation reference.

### **3.9 Evaluation metrics**

The study uses **ROUGE-L** to compare extracted titles and article bodies with the Golden dataset. ROUGE-L measures overlap based on the longest common subsequence. In practical terms, it rewards retaining the reference material in the right order while tolerating some structural noise.

The authors preferred it over strict exact matching for long news articles because scraped articles may contain advertisements or other noise. They state that ROUGE-L penalizes:

- **Over-extraction**, through lower precision.
- **Under-extraction**, through lower recall.

The final article-level metric, called **Correctness**, is binary. An article counts as correct only when all three conditions hold:

1. Its URL exactly matches the reference URL.
2. Its title has ROUGE-L of at least **0.8**.
3. Its content has ROUGE-L of at least **0.8**.

The authors justify the **0.8** threshold in two ways:

- IBM watsonx uses 0.8 as a meaningful lower boundary for high similarity, although the paper acknowledges that no universal academic threshold exists.
- In the authors’ observations, extractions containing only minor noise generally scored above 0.8, whereas serious failures—such as partial extraction or LLM-generated rather than copied content—scored below **0.3**.

### **3.10 Stability and number of runs**

The researchers examined the **95% confidence-interval half-width** across all **nine experimental settings** to determine an adequate number of repeated runs.

The confidence-interval half-width decreased considerably until approximately **30 runs**, after which the improvement slowed. The authors therefore used **30 runs** as a balance between measurement precision and computational expense.

They also repeated selected experiments after **seven days** to test temporal stability.

### **3.11 E-commerce generalization test**

The framework was additionally evaluated on two large e-commerce platforms:

- **Momo**, described as Taiwan’s largest e-commerce platform.
- **Amazon**.

The tasks involved extracting structured product attributes such as prices and ratings. Because these fields are more precisely defined than long news articles, the study used a stricter Correctness criterion requiring a near-exact match. The paper does not supply the complete mathematical or field-by-field definition of this stricter metric.

---

## **4. Results and Findings**

### **4.1 Experimental convergence — Figure 2**

**Figure 2** plots the 95% confidence-interval half-width against the number of runs for a representative scenario.

The curve falls sharply as the number of runs approaches **30**, then becomes comparatively flat. The figure marks this area as an **“elbow point,”** indicating diminishing returns: runs beyond 30 produce relatively little additional precision compared with their computational cost.

The extraction does not provide the exact values of the confidence-interval half-width at individual sample sizes. Only the overall curve shape and the elbow around \(n=30\) can be recovered.

### **4.2 Temporal stability — Table 1**

The authors compared performance at an initial time \(T\) and seven days later, \(T+7\), for three sampled news sites.

| Website | Baseline at T | Baseline at T+7 | Prompt + Tool at T | Prompt + Tool at T+7 |
|---|---:|---:|---:|---:|
| Website 3 | 0.103 | 0.061 | 0.511 | 0.533 |
| Website 4 | 0.277 | 0.317 | 0.648 | 0.673 |
| Website 5 | 0.145 | 0.179 | 0.820 | 0.820 |

The full framework’s changes were:

- **Website 3:** 0.511 to 0.533, an absolute increase of 0.022.
- **Website 4:** 0.648 to 0.673, an absolute increase of 0.025.
- **Website 5:** unchanged at 0.820.

The paper summarizes these changes as variance of less than **5%** on every sampled website, supporting the temporal consistency of the proposed method.

The baseline varied more visibly in some cases—for example, Website 3 fell from 0.103 to 0.061—but the paper’s temporal-stability conclusion focuses on the proposed method.

### **4.3 Main news-site results — Figure 3**

**Figure 3** compares the three experimental configurations across all six news websites.

The recoverable findings are:

- **Webscraper (Prompt + Tool)** outperformed the Baseline Agent on all six sites.
- The full framework also outperformed **Webscraper (Prompt Only)** on every site.
- The baseline often achieved a success rate below **50%** on sites requiring multi-page navigation.
- The full framework’s advantage was especially substantial on complex sites with pagination.
- The baseline had difficulty finding and operating pagination controls.
- On **LTN**, the baseline successfully handled the relevant interaction only **twice in 30 runs**.
- The guided Webscraper agent handled these dynamic interactions more reliably.
- The guided method was also better on tasks without pagination. The prompt taught the agent useful browser shortcuts, including **Ctrl+F**, to locate particular content sections; the baseline struggled with this behavior.

These comparisons support two separate effects:

1. A structured prompt gives the agent important procedural knowledge.
2. Functional Parse and Merge tools add further gains beyond prompting alone.

The extracted document includes Figure 3’s caption and narrative interpretation, but not readable bar heights, data labels, or a numerical table for the six websites. Therefore, exact per-site Correctness scores and statistical test results cannot be recovered. Although the paper repeatedly describes the improvements as significant, it does not report p-values or the specific significance test in the provided text.

### **4.4 E-commerce results — Table 2**

The e-commerce results were:

| Website | Baseline | Prompt Only | Prompt + Tool |
|---|---:|---:|---:|
| Momo | 0.000 | 0.040 | **0.242** |
| Amazon | 0.027 | 0.138 | **0.422** |

The ranking was identical on both platforms:

1. Prompt + Tool performed best.
2. Prompt Only was second.
3. The Baseline Agent performed worst.

Specific comparisons include:

- On **Momo**, the baseline scored **0.000**, Prompt Only scored **0.040**, and the full framework scored **0.242**.
- On **Amazon**, the baseline scored **0.027**, Prompt Only scored **0.138**, and the full framework scored **0.422**.
- The full framework’s score was lower on Momo (**0.242**) than on Amazon (**0.422**), an absolute difference of **0.180**.

These results show that the combination of prompting and functional tools also improves performance outside the news domain, although absolute accuracy remains limited.

### **4.5 Momo extraction ambiguity — Figure 4**

**Figure 4** shows a Momo product page containing several competing price fields. The agent is required to identify the **market price**, but the page simultaneously displays other figures such as a promotional price and a discounted price. The competing price region is highlighted with a red box.

The authors attribute Momo’s lower score to this ambiguity: several plausible values are visible at once, making it difficult for the agent to determine which one corresponds to the requested field.

The extracted article does not preserve the exact price amounts or all readable interface labels in Figure 4. Consequently, the precise values displayed in the screenshot cannot be reported.

### **4.6 Overall empirical pattern**

Across the news and e-commerce tests, the same performance ordering held:

\[
\text{Prompt + Tool} > \text{Prompt Only} > \text{Baseline}
\]

The evidence indicates that:

- General-purpose interaction alone is insufficient for reliable large-scale extraction.
- Procedural prompting improves navigation and workflow decisions.
- Actual parsing and merging tools provide an additional benefit beyond descriptions of those operations in a prompt.
- Page design and field ambiguity materially affect performance.
- Multi-page navigation is a particularly serious weakness of the unmodified baseline.

No negative reversal was reported: the full framework was not said to underperform Prompt Only or the baseline on any tested website.

---

## **5. Analysis and Interpretation**

The authors interpret the results as evidence that effective web scraping requires more than giving a general-purpose browsing agent access to a browser.

General agents may be competent at multi-step interaction, but the paper argues that they are fundamentally inefficient for extracting large collections. State-of-the-art agents such as Browser Use commonly process content sequentially, one page at a time. On an index page containing many links, this approach repeatedly consumes context-window space and can eventually cause the task to fail.

Webscraper instead emphasizes a data-centered strategy:

- It obtains the relevant index information.
- It programmatically generates a script that can be reused for all associated content pages.
- It merges and deduplicates records across iterations.

The authors regard generating one reusable script as more efficient and robust than repeatedly asking the MLLM to interact with every content page. The framework therefore separates the parts of the task that benefit from visual reasoning from those that are better handled by programmatic parsing.

The ablation comparison reinforces this interpretation. Prompt Only consistently improves upon the baseline, showing that strategic guidance matters. Prompt + Tool then improves upon Prompt Only everywhere, showing that prompting cannot fully substitute for functional extraction and aggregation capabilities.

The results also show that task difficulty depends on the website’s presentation. Momo’s multiple simultaneous price fields illustrate a semantic ambiguity problem: even if the page can be accessed and parsed, the agent may still have difficulty determining which visible field corresponds to the user’s requested concept.

Overall, the experiments answer the paper’s practical questions affirmatively:

- A structured MLLM prompt can guide index-and-content scraping.
- Specialized tools improve extraction success beyond prompting alone.
- The same approach transfers from news sites to e-commerce platforms.
- Generalization does not eliminate domain-specific difficulty, as shown by the modest absolute scores and lower result on Momo.

---

## **6. Contributions and Novelty**

The paper’s main contributions are:

- **A specialized framework for index-and-content scraping:** Webscraper adapts a general multimodal GUI agent to extract many linked records from dynamic sites.
- **A combination of visual navigation and HTML parsing:** The agent can interact with the interface through screenshots, mouse actions, keyboard actions, and scrolling, while also invoking programmatic HTML extraction.
- **A structured prompting strategy:** A crawler-specific system prompt coordinates a five-stage workflow, although the supplied extraction does not disclose the five stages individually.
- **Purpose-built parsing and aggregation tools:** The Parse Tool delegates code generation and execution to a stronger reasoning model, while the Merge Tool consolidates and deduplicates results across pages.
- **Context-preserving delegation:** Detailed parsing work is moved outside the main agent’s context, allowing the main agent to concentrate on strategy and navigation.
- **An evaluation criterion suited to long-form scraping:** Correctness combines exact URL matching with ROUGE-L thresholds for titles and article bodies, accommodating minor content noise while rejecting incomplete or generated text.
- **Empirical evaluation on varied dynamic websites:** The experiments cover six Chinese and English news sites with several interaction patterns.
- **Cross-domain evaluation:** Tests on Momo and Amazon show that the framework applies beyond news to e-commerce index-and-content pages.
- **A demonstration of complementary prompt and tool effects:** The ablation experiment shows that strategic prompting helps, but real parsing and merging tools produce additional improvements.

---

## **7. Limitations and Caveats**

### **Explicitly identified technical limitations**

- **Complex navigation remains fragile.** Visual grounding can fail, including inaccurate clicks after browser zooming.
- **Generated parsing code can be buggy.** Both Webscraper and the baseline may produce incorrect scripts when HTML structures are inconsistent.
- **The architecture is domain-limited.** Webscraper is designed for index-and-content websites and is not presented as a universal solution for every web architecture.
- **Real-time WebSocket streams are not handled well.** Such sites may not expose information through the index-and-content pattern expected by the framework.
- **Advanced virtual scrolling is difficult.** Some websites remove off-screen content from the DOM as the user scrolls, which can prevent ordinary parsing from seeing the complete collection.
- **Semantically ambiguous fields lower accuracy.** Momo’s multiple simultaneous price fields made it difficult to identify the requested market price.
- **Absolute e-commerce performance is modest.** Even the best configuration achieved only **0.242** on Momo and **0.422** on Amazon under the stricter metric.

### **Evaluation constraints evident in the paper**

- The principal benchmark contains only **six news websites**, followed by two e-commerce platforms.
- Only three websites appear in the seven-day temporal-stability table.
- Temporal stability was assessed over a single **seven-day interval**, so longer-term resilience to website redesigns was not demonstrated.
- The paper states that improvements are significant, but the provided text contains no p-values, formal hypothesis test, or named significance-testing procedure.
- Exact numerical results for all six news websites cannot be recovered from the supplied Figure 3 extraction.
- The six news websites are not all named in the supplied text, limiting site-by-site interpretation.
- The stricter e-commerce Correctness metric is described as requiring a near-exact match, but its complete formal definition is not supplied.
- The paper identifies a five-stage prompting process but does not enumerate those stages in the provided extraction.
- The Parse Tool relies on an additional reasoning model and code-interpreter environment, introducing extra computational dependencies and cost even though delegation protects the main agent’s context.
- The framework has not yet converted successful runs into a completely deterministic scraper; an LLM remains involved in the described workflow, retaining some cost and stochasticity.

### **Ethical caveats and safeguards**

The authors acknowledge that large-scale scraping can create concerns involving:

- Copyright.
- Excessive server load.
- Misuse of collected information.

They applied the following safeguards:

- Only publicly accessible information was scraped.
- The experiments did not bypass login walls, paywalls, or other access controls.
- Scraping was performed at low frequency.
- Significant delays were inserted between requests.
- The total collected volume was minimal and described as a negligible portion of normal website traffic.
- Data was used only for academic evaluation.
- The collected data was not redistributed and will not be used commercially.

---

## **8. Future Work or Open Questions**

The authors propose two main research directions.

### **8.1 Compile successful runs into deterministic scrapers**

A successful agent trajectory and its validated code could be converted into one reusable deterministic program, potentially using Selenium or Playwright.

This would create a **one-shot generation process**:

1. The LLM navigates the site and develops the scraper once.
2. The successful actions and code are compiled into a stable program.
3. Later scraping runs execute the deterministic program without further LLM involvement.

The intended benefits are:

- Lower ongoing cost.
- Less randomness between runs.
- Greater robustness.
- Elimination of repeated LLM intervention after the scraper has been generated.

### **8.2 Combine GUI perception with web-infrastructure awareness**

The authors also propose expanding the agent from a GUI-only operator into a technically aware analyst that can inspect:

- DOM mutations.
- Real-time changes to page source.
- Network traffic.
- Network protocols such as WebSockets.
- Underlying API endpoints.

Monitoring DOM changes could help the agent understand and handle dynamic mechanisms such as virtual scrolling. Inspecting network requests could allow it to discover a site’s data APIs and retrieve data directly instead of operating entirely through the visible interface.

The envisioned future system would combine visual interaction with knowledge of the web’s underlying architecture, potentially producing a more general and efficient scraper.

Open problems therefore include reliable handling of:

- Inconsistent HTML.
- Visual-grounding failures.
- Virtualized interfaces.
- WebSocket-based streams.
- Ambiguous fields.
- Automatic conversion of successful agent behavior into a dependable reusable program.

---

## **9. High-Level Takeaway (Plain Language)**

Webscraper gives an AI browser agent a step-by-step scraping strategy plus dedicated tools for turning web pages into structured records and combining results across pages. On six news sites and two shopping platforms, this complete combination worked consistently better than either a general browser agent or prompting alone, especially when the task required pagination or processing many linked pages. The main lesson is that an AI that can click around a website is not automatically an effective data collector: reliable large-scale scraping also requires specialized parsing, aggregation, and reusable-code strategies.