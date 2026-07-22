# *BEARCUBS: A Benchmark for Computer-Using Web Agents*

**Authors:** Yixiao Song, Katherine Thai, Chau Minh Pham, Yapei Chang, Mazin Nadaf, and Mohit Iyyer  
**Affiliations:** UMass Amherst and University of Maryland, College Park  
**Publication:** Conference on Language Modeling (COLM), 2025

## 1. Background and Context

Modern language-model-based web agents can inspect screen pixels and operate a virtual mouse and keyboard. In principle, this lets them do more than retrieve text: they can watch videos, manipulate interactive databases, navigate three-dimensional environments, solve CAPTCHAs, and play web games.

However, existing benchmarks do not adequately measure these abilities in realistic conditions:

- WebArena and WebShop use synthetic or simulated websites, so they do not capture the instability and unpredictability of the live web.
- Some established benchmarks are approaching saturation. OpenAI Operator reportedly reaches 87% on WebVoyager and 58% on WebArena, while human performance on WebArena is 78%.
- Many benchmarks can be solved from HTML or other text alone, as with Mind2Web, or test only a narrow multimodal skill such as maps or image processing.
- AssistantBench evaluates realistic real-web tasks but intentionally limits interactions such as video understanding.
- Published live-web questions can become contaminated when answers are indexed online. A task originally requiring a video, game, or interactive visualization can then be solved through ordinary text search.

The authors identify four practical obstacles to meaningful live-web evaluation:

1. **Web contamination:** Published questions and answers may enter search indexes or training data.
2. **Text-based workarounds:** An agent may find an indirect textual clue instead of performing the interaction being tested.
3. **Insufficient interaction diversity:** Existing evaluations frequently concentrate on domains such as shopping, travel, or service booking.
4. **Slow evaluation:** Commercial agents often lack APIs and trajectory-export tools, requiring laborious manual execution and screen recording.

BEARCUBS stands for **BEnchmark for Agents with Real-world Computer Use and Browsing Skills**. It is intended as a “small but mighty,” continuously refreshed benchmark that emphasizes difficult-to-bypass interactions with the live web.

## 2. Research Goal and Objectives

The paper’s main goal is to determine how well current web agents can search for and identify factual information when they must interact with real, changing websites.

Its specific objectives are to:

- Create a benchmark of short-answer questions whose solutions require live-web browsing.
- Test both conventional text navigation and genuinely multimodal interaction involving images, audio, video, games, virtual tours, maps, or other dynamic interfaces.
- Prevent multimodal tasks from being solved through search snippets or text-only shortcuts.
- Compare current computer-using agents, search-and-reasoning agents, simple language-model baselines, and humans.
- Analyze not only answer correctness but also execution time, trajectories, source quality, failure behavior, and interaction strategy.
- Identify capabilities that must improve for web agents to approach reliable human-level performance.

The benchmark is not primarily intended to test multilingual querying, even though it includes websites in several languages.

## 3. Methods (Approach/Design)

### 3.1 Benchmark composition

BEARCUBS contains **111 information-seeking questions**:

- **56 text-based questions**
- **55 multimodal questions**
- **108 distinct top-level URLs** across viable human trajectories, excluding Google Search visits

Each question has:

- One short, unique, unambiguous gold answer
- A human-validated trajectory showing a viable solution
- A list of visited websites
- A source or interaction from which the answer can be verified

According to Table 1:

| Question type | Questions | Distinct URLs | Steps/question, mean (min–max) | Webpages/question, mean (min–max) |
|---|---:|---:|---:|---:|
| Text-based | 56 | 61 | 6.5 (3–12) | 3.8 (1–8) |
| Multimodal | 55 | 47 | 5.8 (3–14) | 3.0 (1–6) |
| Overall | 111 | 108 | 6.1 (3–14) | 3.4 (1–8) |

Text-based questions require reading and navigating textual material, such as databases or scanned documents. Multimodal questions require images, video, audio, virtual tours, games, or other real-time interaction.

### 3.2 Question-design criteria

Every accepted question had to satisfy four requirements:

1. **Short but unambiguous:** It must provide enough information to identify one correct answer without unnecessary detail.
2. **Trivial to evaluate:** The answer must be correct, unique, and concise. Lists and sets are excluded, and answer paraphrases are not accepted.
3. **Adversarial to Google Search:** The answer must not appear in prominent search results or snippets when the question or fragments of it are queried. Multimodal questions must also resist text-only agents such as Deep Research.
4. **Publicly accessible:** The answer must be available without payment, account creation, or login.

### 3.3 Collection and validation

Authors wrote **65 of the 111 questions**, covering domains such as music, maps, and games. Upwork freelancers wrote the remainder after training and received **$4 per accepted question**. Only **58.2%** of freelancer-created questions were accepted.

At least two authors verified every question, answer, viable trajectory, and link. The workflow shown in Figure 3 had three stages:

1. **Question writing:** Record the question, viable method, and visited links.
2. **Quality verification:** At least two authors check the sources, trajectory, clarity, uniqueness, and correctness and reject unsuitable questions.
3. **Workaround prevention:** Search extensively for answers in snippets, reject questions answerable directly by ChatGPT, and reject nominally multimodal questions that Deep Research can solve through text.

This filtering removed **13 questions**, mostly because Deep Research found text-only workarounds.

**Figure 2** illustrates such a rejected question. The intended task was to watch a *Phantom Blade Zero* Year of the Snake gameplay trailer and count how often the boss reduced the player’s health. A human could watch the video and determine that the answer was **zero times**. Deep Research instead found a forum comment saying the player’s health bar did not drop and inferred the answer without watching the trailer. The example shows why a nominally multimodal question may fail to measure multimodal ability.

The benchmark is intended to evolve: questions will be replaced when websites change, trajectories become invalid, or answers become available in searchable text.

### 3.4 Human study

Humans who had not previously seen a question could use their browser in any way they wished. They were asked to:

- Start a timer upon reading the question and stop when confident.
- Submit an answer.
- Report the number of dead ends.
- Describe encountered difficulties.
- Rate perceived difficulty.
- Abandon a question if unable to answer it after 15 minutes.

A dead end meant leaving the current page and backtracking or restarting the search.

Because some tasks required language or domain knowledge, the study used suitable annotators. The dataset includes interaction with Arabic, Mandarin Chinese, Hindi, German, Vietnamese, and Finnish websites. Native-speaking volunteers handled Arabic and Chinese; three Upwork annotators handled Hindi, German, and Finnish. English-only sets were attempted by annotators and authors who had not written or validated those questions.

Paid annotators received **$2.50 per question plus a $1 bonus for each correct answer**.

### 3.5 Agents and baselines

Seven commercial web agents were evaluated.

**Search-and-reasoning agents with limited multimodal ability:**

- Grok 3 DeepSearch
- OpenAI Deep Research
- Google Deep Research

**Computer-using agents:**

- Convergence AI Proxy
- Anthropic Computer Use
- OpenAI Operator
- OpenAI ChatGPT Agent

Five baseline configurations were included:

- GPT-4o zero-shot
- DeepSeek R1 zero-shot
- GPT-4o with Google Search snippets
- DeepSeek R1 with Google Search snippets
- Perplexity sonar-pro

For search augmentation, a question was submitted to Serper, a Google Search API, and up to ten result titles and snippets were concatenated with the question. The model was instructed to use only that context and return “No answer found” if it contained no clear answer.

Baseline settings were:

- **GPT-4o-2024-11-20:** maximum 518 tokens, temperature 0
- **DeepSeek R1:** maximum 8,000 tokens, temperature 0

### 3.6 Execution and scoring

Agents were benchmarked between February 23 and March 1, 2025, except:

- Google Deep Research was tested in late May 2025.
- ChatGPT Agent was tested July 18–20, 2025.

For computer-using agents, the authors added an instruction to complete CAPTCHAs, accept necessary prompts, and minimize user intervention. If an agent requested help, it received one instruction to find a solution independently. A second request ended the session.

Each run recorded:

- Final answer
- Time taken
- Full available trajectory

A run ended when the agent answered, abstained, became stuck in a loop, or stopped making progress. The ordinary computer-use limit was **15 minutes**; ChatGPT Agent was allowed **45 minutes** because it sometimes answered correctly after 15 minutes.

An answer counted as correct only if it directly and unambiguously entailed the gold answer. Hedged statements such as “likely” or “I’m leaning toward” were not accepted.

Manual evaluation used four labels:

- Correct
- Wrong
- Uncertain/no direct answer
- None/no answer, including loops

The authors also built a GPT-4o-based automatic evaluator using 17 in-context examples, temperature 0. It cost about **$0.80** and took approximately **1 minute 30 seconds** for all 111 questions.

## 4. Results and Findings

### 4.1 Human performance

Humans achieved **84.7% overall accuracy**, answering 94 questions correctly, 14 incorrectly, and abandoning 3.

By question type:

| Split | Accuracy | Correct | Wrong | Abandoned |
|---|---:|---:|---:|---:|
| Text-based | 83.6% | 46 | 9 in Table 5 | 1 |
| Multimodal | 85.7% | 48 | 5 | 2 |
| Overall | 84.7% | 94 | 14 | 3 |

Table 9 records eight wrong text-based and six wrong multimodal responses, whereas Table 5 shows nine and five, respectively. Both produce the same totals and accuracies; the supplied paper does not explain this split-level discrepancy.

Humans encountered:

- **1.50 dead ends per question overall**
- 1.83 on text-based questions
- 1.22 on multimodal questions
- A maximum of 14 dead ends

Mean completion time was:

- **4 minutes 46 seconds overall**
- 5:19 for text-based questions
- 4:23 for multimodal questions

Observed ranges were:

- Overall: 0:26–27:24
- Text-based: 0:43–27:24
- Multimodal: 0:26–24:14

The main results table reports mean time by answer outcome:

- Correct human answers: 4:24
- Wrong human answers: 5:44
- Correct text-based answers: 5:09
- Wrong text-based answers: 5:07
- Correct multimodal answers: 3:41
- Wrong multimodal answers: 6:41

Annotators rated **55 questions easy, 36 medium, and 20 hard**, so **50.5%** were considered moderate or hard. Text-based questions received 23 easy, 20 medium, and 13 hard ratings; multimodal questions received 32 easy, 16 medium, and 7 hard ratings.

Regardless of correctness, average time by perceived difficulty was:

- Easy: **2:14**
- Medium: **5:32**
- Hard: **10:52**, including abandoned attempts

Humans generally found games, 3D tours, images, and other multimodal tasks easy. Complex data filtering and specialist knowledge, such as music theory, were harder.

### 4.2 Human errors

The most frequent causes were overlooking a question or answer detail and lacking topic knowledge. Other identified causes included poor source selection, obvious oversight, and task complexity.

Table 6 gives three examples:

- A Wingspan-card question required birds from the Asia expansion containing “Great,” but not “Greater,” and living exclusively in wetlands. The annotator was unfamiliar with the game, used a site missing expansion and habitat details, searched individual bird names, and overlooked the Asia-expansion constraint.
- For the October 2024 issue 817 of *Tinkle*, the annotator opened the relevant magazine page but missed the answer displayed there.
- For a tagged Altai snow leopard, the annotator found the correct USGS interface but could not identify map markers at the specified times to compute straight-line travel distance.

The authors conclude that additional time or domain knowledge would probably have enabled the annotators to solve these cases.

### 4.3 Overall model performance

| System | Overall | Text-based | Multimodal |
|---|---:|---:|---:|
| GPT-4o zero-shot | 2.7% | 5.4% | 0.0% |
| DeepSeek R1 zero-shot | 8.1% | 10.7% | 5.5% |
| GPT-4o + Google Search | 0.0% | 0.0% | 0.0% |
| DeepSeek R1 + Google Search | 1.8% | 3.6% | 0.0% |
| Perplexity sonar-pro | 5.4% | 8.9% | 1.8% |
| Grok 3 DeepSearch | 11.7% | 21.4% | 1.8% |
| OpenAI Deep Research | 36.0% | 60.7% | 10.9% |
| Google Deep Research | 23.4% | 42.9% | 3.6% |
| Convergence AI Proxy | 12.6% | 16.1% | 9.1% |
| Anthropic Computer Use | 14.4% | 19.6% | 9.1% |
| OpenAI Operator | 23.4% | 33.9% | 12.7% |
| OpenAI ChatGPT Agent | **65.8%** | **76.8%** | **54.5%** |
| Human | **84.7%** | **83.6%** | **85.7%** |

ChatGPT Agent led all agents but remained **18.9 percentage points below humans overall**. It exceeded Operator by **42.4 points overall** and **41.8 points on multimodal questions**, and exceeded OpenAI Deep Research by **29.8 points overall**.

Humans outperformed ChatGPT Agent by:

- 6.8 points on text-based questions
- 31.2 points on multimodal questions

### 4.4 Answer-label distributions and timing

Across 111 questions:

- **ChatGPT Agent:** 73 correct, 30 wrong, 3 uncertain, 5 none; mean time 9:16 for correct, 16:14 for wrong, and 25:55 for uncertain responses.
- **Operator:** 26 correct, 43 wrong, 13 uncertain, 29 none; 2:59, 3:58, and 8:06.
- **Anthropic Computer Use:** 16 correct, 22 wrong, 73 uncertain, no none; 2:24, 2:35, and 3:35.
- **Proxy:** 14 correct, 44 wrong, 34 uncertain, 19 none; 1:52, 2:41, and 5:24.
- **Google Deep Research:** 26 correct, 39 wrong, 46 uncertain; 4:21, 4:00, and 4:39.
- **OpenAI Deep Research:** 40 correct, 69 wrong, 1 uncertain, 1 none; 4:37, 9:00, and 3:58.
- **Grok 3 DeepSearch:** 13 correct, 95 wrong, 2 uncertain, 1 none; 1:09, 1:24, and 2:05.

ChatGPT Agent’s correct multimodal responses took **13:15 on average**, versus 6:29 for correct text-based responses. Wrong multimodal responses took 18:19. Table 9 prints its uncertain multimodal time as “16.58,” whose punctuation is ambiguous in the supplied text.

Agents generally answered correctly faster than humans but were far less accurate. ChatGPT Agent was the exception in speed: it achieved much higher accuracy but often took longer, partly because it cross-verified information.

The authors summarize a common pattern as **agents succeeding quickly and failing slowly**. Proxy and Operator spent an average of **11:08** and **14:37**, respectively, before becoming trapped in loops and returning no answer. Their unanswered rate rose markedly after ten minutes.

### 4.5 Baseline and search results

The benchmark was not solvable through model memory or simple search snippets:

- DeepSeek R1 was the strongest zero-shot baseline at 8.1%, but trajectory analysis indicated that its correct answers were mainly guesses.
- GPT-4o zero-shot reached 2.7%.
- Adding Google snippets reduced performance to 0% for GPT-4o and 1.8% for DeepSeek R1.
- Perplexity sonar-pro was the best search-augmented system at 5.4%, still below zero-shot DeepSeek R1.

This supports the claim that answers generally cannot be recovered from ordinary snippets and require deeper browsing or interaction.

### 4.6 Multimodal capability

All agents struggled on multimodal questions, even though humans found these slightly easier than text-based questions.

ChatGPT Agent’s 54.5% multimodal accuracy represents a large improvement over earlier computer-use systems. It could solve CAPTCHAs, navigate 3D environments, analyze videos, and interact with games. Nevertheless, it remained well below the human result of 85.7%.

OpenAI Deep Research lacks computer-use capabilities but scored 10.9% on multimodal questions, exceeding Proxy and Anthropic Computer Use at 9.1%. Manual trajectory inspection showed that this was largely guessing or the discovery of textual shortcuts, illustrating how poorly the nominally computer-using agents handled both multimodal interaction and text-based reasoning.

### 4.7 Figure 1: A simple human task that defeats most agents

Figure 1 asks for text below a horizontal line in the right margin of a historical document displayed in AI2’s olmOCR interactive comparison page.

- A human located the document, zoomed in, and answered in **43 seconds**.
- ChatGPT Agent found the correct answer but took **18 minutes**.
- Operator reached the correct section but failed to click the necessary link.
- Proxy did not fully explore the correct page.
- Anthropic Computer Use failed to find the right webpage.

The figure demonstrates how a short chain of precise browsing and visual actions can expose large capability differences.

### 4.8 Agent-specific failures in Table 3

Table 3 provides three representative cases:

1. **Inefficient and opaque search:** For a UMass Amherst tree-identification task, OpenAI Deep Research logged 46 site visits, deduplicated to eight top-level domains. Several were irrelevant. Because its logs exposed only top-level URLs, the exact pages and decisions were unclear.
2. **Ignoring the requested primary source:** Operator found the required *Cambridge Encyclopedia of the World’s Ancient Languages* but left it, used Omniglot instead, and returned “[e]” for the Lycian character E. The answer was wrong both for the question and for the cited alternative source.
3. **Failed game interaction:** Anthropic Computer Use reported that the Patatap website did not respond to keyboard input and declined to identify the circle color produced by pressing “C” against a pink background.

### 4.9 Source reliability

Figure 4 divides each agent’s correct answers among primary, secondary, and ungrounded sources:

| Agent | Primary | Secondary | Ungrounded |
|---|---:|---:|---:|
| Grok 3 DeepSearch | 61.54% | 15.38% | 23.08% |
| OpenAI Deep Research | 61.54% | 25.64% | 12.82% |
| Convergence AI Proxy | 92.86% | 7.14% | 0% |
| Anthropic Computer Use | 87.5% | 12.5% | 0% |
| OpenAI Operator | 89.29% | 7.14% | 3.57% |

Table 9 additionally records ChatGPT Agent as having 72 of its 73 correct answers grounded in primary sources and one ungrounded, with none from secondary sources. Google Deep Research had 25 primary and one ungrounded correct answer.

For OpenAI Deep Research, secondary plus ungrounded sources account for **38.46%** in Figure 4, rounded to **38.5%** in the discussion. An earlier results paragraph says **37.5%**; this is an internal numerical inconsistency in the paper. The underlying counts are 25 primary, 10 secondary, and 5 ungrounded among 40 correct answers.

### 4.10 Automatic evaluator

The automatic answer evaluator attained the following accuracy:

| Agent outputs | Four-way | Binary |
|---|---:|---:|
| Grok 3 DeepSearch | 99.1% | 99.1% |
| OpenAI Deep Research | 96.4% | 96.4% |
| Anthropic Computer Use | 99.1% | 100% |
| Proxy | 99.1% | 100% |
| Operator | 97.3% | 98.2% |

The paper summarizes aggregate performance as **98.2% four-way accuracy** and **98.7% binary accuracy**. Three repeated evaluations of Anthropic and Proxy outputs produced identical results.

### 4.11 Benchmark stability

To test whether 111 questions were enough for stable measurement, DeepSeek R1 was run four times:

- Without Serper: 7.2%, 5.4%, 5.4%, and 5.4%; standard deviation **0.8%**
- With Serper: 1.8%, 0.9%, 2.7%, and 2.7%; standard deviation **0.7%**

Table 10 therefore suggests low run-to-run variance despite the benchmark’s modest size.

## 5. Analysis and Interpretation

BEARCUBS reveals a large separation between agents that appear strong on established benchmarks and agents that can reliably act on the live web.

The central interpretation is that access to a mouse and keyboard does not by itself produce effective computer use. Lower-performing computer agents often avoided intended interactions, relied on guesses or alternative sources, repeated failed actions, or stopped before attempting difficult interfaces.

ChatGPT Agent represents substantial progress because it follows instructions, locates relevant pages, and performs interactions that earlier agents frequently could not. Its 65.8% overall score establishes the strongest reported performance in this study. However, its remaining weaknesses are important:

- Poor fine cursor control
- Difficulty dragging sliders
- Trouble using interactive filters
- Difficulty selecting items from scrollable menus
- Problems viewing complete dynamic tables
- Slow processing and excessive cross-checking
- Incorrect or missing answers after long runs

OpenAI Deep Research’s second-place result shows the strength of specialized search and reasoning. Its 60.7% text score exceeded every tested computer-use agent except ChatGPT Agent. The authors suggest that future computer-using systems may benefit from combining interactive abilities with a strong search agent. However, Deep Research’s reliance on secondary or ungrounded material makes accuracy alone an incomplete measure.

Humans showed the reverse modality pattern from agents: people generally found videos, images, games, and 3D spaces easier, while agents found them much harder. This indicates that multimodal web interaction is not merely an optional extension of text browsing but a central unsolved capability.

The trajectory analysis identifies four broader needs:

- **Interpretability:** Trajectories should be detailed enough to explain decisions but not so verbose that important steps are buried. Grok averaged 69.8 reported steps per question, while Proxy averaged only 6.2. Deep Research exposed vague top-level URLs. These formats prevent fair comparison and make failures hard to diagnose.
- **Source credibility:** Correctness can conceal unreliable sourcing. Agents sometimes ignored the source named in the question or answered from an unverified secondary source.
- **Multimodal interaction:** Agents need better coordinated mouse and keyboard control and methods for handling inaccessible videos, blocked posts, or restricted pages.
- **Planning:** Agents frequently revisited irrelevant or previously unsuccessful pages and accumulated unhelpful information. More structured planning may reduce redundancy and improve retrieval.

Additional behavior included Grok returning its trajectory in a non-English language when that language appeared in the question, which may not serve users seeking help with that language. Grok also tended to produce an answer rather than abstain. Anthropic Computer Use sometimes declared tasks impossible without first making a meaningful attempt.

## 6. Contributions and Novelty

The paper makes several principal contributions:

- It introduces **BEARCUBS**, a public benchmark of 111 short-answer tasks requiring interaction with the live web.
- It emphasizes diverse, difficult-to-bypass multimodal behavior, including video analysis, games, 3D navigation, dynamic databases, and scanned documents.
- It provides every question with a verified answer, viable human trajectory, and list of relevant websites, enabling analysis of both outcomes and strategies.
- It develops a rigorous process for detecting and removing text-based workarounds from multimodal tasks.
- It presents a broad comparison of humans, computer-using agents, search-and-reasoning agents, zero-shot models, and search-augmented baselines.
- It shows that simple search augmentation and closed-book knowledge are insufficient for these tasks.
- It documents a substantial human–agent gap, especially for multimodal interactions that humans consider easy.
- It evaluates source attribution, timing, looping behavior, and trajectory transparency in addition to accuracy.
- It proposes continuous question replacement to combat contamination and broken live-web trajectories.
- It provides an efficient automatic answer evaluator with near-manual classification accuracy.

## 7. Limitations and Caveats

The authors identify several limitations:

- **Single short answers:** Every task has one concise answer, while real requests may have no answer, multiple answers, or require long-form synthesis. Such settings would also need source-quality evaluation for every claim.
- **Limited multilingual scope:** Although several languages are represented, the dataset is too small for systematic conclusions about multilingual or cross-cultural performance.
- **Only 111 questions:** The benchmark is small, although the authors argue that its open-web search space, complex tasks, and low experimental variance keep it informative.
- **Uneven trajectory detail:** Providers expose very different levels of information, making direct comparisons difficult.
- **Manual evaluation burden:** Most agents lacked APIs, so researchers manually submitted prompts, recorded screens, and evaluated runs. Agents averaged nearly five minutes per question, and some exceeded 20 minutes.
- **Contamination remains possible:** Publishing questions allows people or systems to post answers online. Releasing questions without answers reduces but does not eliminate this risk.
- **Live-web instability:** Websites can change, disappear, block access, or invalidate a trajectory.
- **Access restrictions:** Agents were sometimes denied videos, Reddit posts, or other content, complicating the measurement of underlying ability.
- **Workaround detection is difficult:** Deep Research repeatedly uncovered textual shortcuts that humans had not anticipated.
- **Commercial-system timing:** Systems were evaluated on different dates, including ChatGPT Agent several months after most other agents.
- **Different time limits:** ChatGPT Agent received up to 45 minutes, whereas most computer-use agents received 15 minutes.
- **Exact-match-like answer policy:** Answers must be direct and unambiguous; hedges and paraphrases are rejected. This simplifies evaluation but does not capture every form of useful real-world response.
- **Possible anti-distillation obscurity:** Brief trajectories or top-level-only URLs may reflect provider efforts to prevent model distillation, but they also reduce transparency.
- **Internal reporting inconsistencies:** The paper gives 37.5% and approximately 38.5% for Deep Research’s non-primary correct answers, and Tables 5 and 9 differ in how human errors are split between text and multimodal questions.

The study does not report inferential statistical tests or p-values; comparisons are based on descriptive accuracy, timing, and error analyses.

## 8. Future Work or Open Questions

The authors propose:

- Regularly replacing contaminated, broken, or obsolete questions.
- Adding new examples so the benchmark remains current.
- Developing clearer, structured, shareable search and reasoning trajectories.
- Providing APIs and easier trajectory-recording tools to reduce evaluation cost.
- Evaluating source credibility rather than correctness alone.
- Improving mouse, keyboard, and combined interaction skills.
- Developing strategies for inaccessible or restricted web content.
- Improving fine control over sliders, filters, menus, databases, and dynamic tables.
- Designing structured planning mechanisms that reduce repeated and irrelevant actions.
- Combining strong computer-control systems with specialized web-search and reasoning agents.
- Studying multilingual and culturally diverse performance systematically.
- Extending evaluation to questions with no answer, multiple answers, or long-form answers.
- Conducting user studies on behaviors such as always answering rather than abstaining.
- Improving adaptability, transparency, speed, and user-centered behavior.

An ongoing challenge is how to publish a useful open benchmark without making its interactive questions searchable and therefore trivial.

## 9. High-Level Takeaway (Plain Language)

BEARCUBS tests whether AI agents can genuinely use the real web—not merely read search snippets. Humans solved about **85%** of its questions, while the strongest agent, ChatGPT Agent, solved about **66%** and older computer-use agents scored between roughly **13% and 23%**. The hardest gap was in videos, games, 3D environments, and other interactive tasks that people often found easy. The study shows that modern agents have improved substantially, but reliable web assistance still requires better control, faster and more deliberate planning, trustworthy sourcing, and clearer records of how each answer was found.