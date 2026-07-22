# BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

**Authors:** Jason Wei*, Zhiqing Sun*, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, and Amelia Glaese  
**Affiliation:** OpenAI  
\*Equal contribution

## 1. Background and Context

The internet contains enormous amounts of information, but finding a specific obscure fact can require searching many pages, combining scattered clues, and repeatedly changing search strategies. The authors argue that human browsing is constrained by limited memory and knowledge, distraction and fatigue, and an inability to examine many possibilities in parallel. A sufficiently capable AI agent, by contrast, could potentially search tirelessly and retrieve any well-specified fact from the open web—even if doing so required examining thousands of pages.

Existing information-retrieval and question-answering benchmarks generally emphasize facts that a person can find within about ten minutes. Recent language models have largely saturated many such benchmarks. Meanwhile, AI systems are progressing from chatbots to reasoning models and autonomous agents that can use internet tools for extended investigations.

The paper introduces **BrowseComp**, short for “Browsing Competition,” to evaluate this more demanding form of web research. BrowseComp contains **1,266 questions** requiring agents to find hard-to-locate, deeply entangled information. Questions typically specify several indirect constraints rather than directly naming the subject. Solving them therefore requires searching a large candidate space, checking factual claims, linking evidence across sources, and ruling out alternatives.

BrowseComp is designed around two complementary properties:

- **Hard to solve:** The questions should resist ordinary searches, existing models, and at least ten minutes of human investigation.
- **Easy to verify:** Each question has a short, self-contained reference answer, so a proposed answer can be compared directly with the reference.

The paper treats BrowseComp as analogous to a programming competition: success demonstrates an important core skill, but does not completely represent real-world usefulness. BrowseComp measures persistent, creative information discovery, not the full range of browsing tasks such as answering common questions, writing long reports, or resolving ambiguous user requests.

To reduce benchmark leakage into model-training data, the paper asks readers not to reproduce dataset examples publicly and includes a canary string that can be used to identify and filter the benchmark from training corpora.

## 2. Research Goal and Objectives

The central goal is to create and validate a benchmark that measures whether AI agents can **persistently and strategically browse the internet to retrieve a single, difficult-to-find fact**.

The paper specifically aims to:

1. Construct challenging questions that cannot be answered through a few straightforward searches.
2. Keep answers short and grading simple despite the difficulty of finding them.
3. Measure the roles of reasoning, browsing tools, persistent search, and test-time computation.
4. compare human performance with several OpenAI models.
5. Examine whether model performance improves with increased browsing effort and repeated attempts.
6. Evaluate whether models accurately express uncertainty about their answers.
7. Analyze differences in task difficulty and identify defective or ambiguous benchmark items.

No formal statistical hypotheses or significance tests are presented.

## 3. Methods (Approach/Design)

### 3.1 Dataset construction

BrowseComp was created entirely by human trainers. Its instructions largely followed those used for SimpleQA: trainers wrote fact-seeking questions with a **single, short, indisputable answer** that should remain stable over time and be supported by evidence.

Questions were commonly constructed through an **inversion process**:

1. A trainer began with a known “seed,” such as a person, event, publication, or artifact.
2. The trainer identified several characteristics associated with it.
3. Those characteristics were turned into an indirect question whose answer was difficult to discover.
4. The known seed became the short reference answer.

This design makes verification easier than discovery. Once an answer is proposed, a few searches may establish that it meets the constraints. Finding it from scratch, however, can require investigating thousands of possible candidates.

The paper provides examples involving combinations of facts about a historical soccer match, a fictional character, and a research publication. These illustrate that questions often combine dates, biographical details, event properties, and other constraints that are unlikely to occur together in a simple search result.

### 3.2 Difficulty criteria

Trainers applied three checks intended to produce genuinely difficult questions:

1. **Failure of contemporary models:** Trainers verified that GPT-4o with and without browsing, OpenAI o1, and an early Deep Research model could not solve the question.
2. **Resistance to simple search:** Trainers performed five basic Google searches and confirmed that the answer was not readily available on the first result pages.
3. **Human difficulty:** Questions were intended to be difficult enough that another person could not solve them within ten minutes.

The ten-minute requirement was not enforced for every item. For a portion of the dataset, a second trainer attempted the question. Trainers whose questions were solved more than **40%** of the time were asked to revise them.

### 3.3 Handling alternative valid answers

Inverted questions create a structural uncertainty: the provided reference answer is known to satisfy the clues, but it is not always feasible to prove that no other answer also satisfies them. Exhaustively checking every candidate could be prohibitively time-consuming.

To reduce this risk:

- Trainers were required to be familiar enough with the subject to be reasonably confident that the answer was unique.
- They added further constraints when uniqueness was uncertain.
- If another trainer found a different valid answer within ten minutes, the question creator received feedback and revised the item.

The dataset therefore aims to have a unique valid answer, but uniqueness is described as **likely rather than guaranteed**.

### 3.4 Topic selection and classification

Trainers were encouraged to write questions about subjects that personally interested them. The authors expected this to make annotation more engaging and improve question quality.

Topics were assigned after collection by a prompted ChatGPT model rather than being labeled directly by the trainers.

### 3.5 Human evaluation

Human trainers from the same broader group that created the dataset attempted BrowseComp questions, but they were not permitted to solve their own questions and did not know the reference answers.

They were prohibited from using AI assistants, specifically ChatGPT, Claude, Perplexity, Grok, or Gemini. They could search normally and could give up only after attempting a question for approximately two hours. They self-reported the time required.

Of the full **1,266-item** dataset, **11 questions** were not attempted for various reasons, leaving **1,255 human attempts**.

### 3.6 Model evaluation

The authors evaluated systems with different combinations of internal reasoning and web access:

- **GPT-4o:** `gpt-4o-2024-08-06`, without browsing.
- **GPT-4o with browsing:** `gpt-4o-search-preview-2025-03-11`.
- **GPT-4.5:** `gpt-4.5-preview-2025-02-27`, without browsing.
- **OpenAI o1:** `o1-2024-12-17`, medium reasoning effort, without browsing.
- **OpenAI Deep Research:** an agent explicitly trained for persistent web browsing.

The paper notes that Deep Research was trained on data specifically intended to make it good at BrowseComp-type tasks.

Models were instructed to return:

- An explanation,
- A succinct exact answer, and
- A confidence score from 0% to 100%.

### 3.7 Grading

Because reference answers are short strings, an AI judge determined whether the predicted answer was semantically equivalent to the reference. The authors used the same grading prompt as Humanity’s Last Exam.

The judge:

1. Extracted the final exact answer from the response.
2. Compared only that answer with the supplied reference.
3. Marked it correct when the two matched, allowing a small error margin for numerical answers.
4. Marked inconsistent, ambiguous, non-equivalent, or missing answers incorrect.
5. Extracted the stated confidence, defaulting to 100% if none was supplied.

### 3.8 Calibration analysis

The authors assessed whether model confidence corresponded to actual correctness. This matters because an agent can be unreliable even when occasionally correct if it confidently presents wrong answers. Calibration error was calculated for each evaluated model, although the paper does not provide the formula in the supplied text.

### 3.9 Additional test-time computation

Two forms of increased test-time computation were studied:

- **Greater browsing effort within one run:** Full evaluations were performed using different browsing-effort levels.
- **Parallel sampling:** Deep Research generated **64 outputs per question**, each with a confidence score. The outputs were combined using three selection methods:

  - **Majority voting:** Choose the answer appearing most frequently.
  - **Weighted voting:** Weight each answer’s vote by the confidence assigned by the model.
  - **Best-of-N:** Select the single answer with the highest model-assigned confidence.

The authors evaluated how accuracy changed as the number of parallel samples increased from 1 to 64.

### 3.10 Pass-rate analysis and dataset cleaning

To analyze item difficulty, the authors ran **64 trials per question** for both OpenAI o1 and Deep Research across all tasks. An item’s pass rate was the fraction of those trials that produced the correct answer.

For questions that Deep Research never answered correctly, the model was subsequently given the ground-truth answer and asked to retrieve supporting web evidence. This tested whether those questions were genuinely unsolvable or merely difficult to solve without guidance.

## 4. Results and Findings

### 4.1 Dataset composition

**Figure 2** is a pie chart showing the topic distribution across the 1,266 questions:

| Topic | Questions | Share |
|---|---:|---:|
| TV shows and movies | 205 | 16.2% |
| Other | 197 | 15.6% |
| Science and technology | 173 | 13.7% |
| Art | 127 | 10.0% |
| History | 125 | 9.9% |
| Sports | 123 | 9.7% |
| Music | 116 | 9.2% |
| Video games | 71 | 5.6% |
| Geography | 70 | 5.5% |
| Politics | 59 | 4.7% |

The benchmark is therefore spread across many domains rather than being dominated by a single technical or academic subject. TV and film form the largest category, while politics is the smallest listed category.

### 4.2 Human performance

**Table 2** reports the human evaluation:

| Outcome | Result |
|---|---:|
| Questions attempted | 1,255 |
| Human gave up after two hours | 888/1,255 (70.8%) |
| Solved by a human | 367/1,255 (29.2%) |
| Trainer and reference answers agreed among solved items | 317/367 (86.4%) |

Thus, experienced trainers solved fewer than one-third of attempted questions. Even among questions they considered solved, their answers matched the original reference only **86.4%** of the time.

**Figure 3** contains two time histograms:

- The left histogram covers questions humans solved. Solution times vary widely: some questions were completed in under an hour, while many required approximately two or three hours. The visible distribution is concentrated broadly around 60–180 minutes, with a prominent peak near two hours and a smaller number extending toward 300 minutes.
- The right histogram covers abandoned questions. Most give-ups cluster near 120 minutes because trainers were required to work for at least about two hours before stopping. A smaller number were reported above that threshold.

The figure reinforces that BrowseComp is difficult even for humans familiar with the benchmark’s style. The authors nevertheless caution that these trainers were not elite competitive web searchers. Some abandoned items might be solvable by professionals such as detectives or investigative journalists if they had enough time.

### 4.3 Baseline model accuracy

**Table 3** reports the following results:

| Model | Accuracy | Calibration error |
|---|---:|---:|
| GPT-4o | 0.6% | 69% |
| GPT-4o with browsing | 1.9% | 82% |
| GPT-4.5 | 0.9% | 68% |
| OpenAI o1 | 9.9% | 65% |
| Deep Research | 51.5% | 91% |

GPT-4o and GPT-4.5 achieved close to zero accuracy, demonstrating that the benchmark’s obscure, multi-step factual questions are generally inaccessible to models lacking effective web investigation.

Adding browsing to GPT-4o raised accuracy from **0.6% to 1.9%**, an absolute improvement of 1.3 percentage points, but performance remained extremely low. The authors interpret this as evidence that access to search tools alone is insufficient. Successful agents also need to choose useful search paths, reason strategically, and correctly interpret retrieved material.

OpenAI o1, despite having no browsing capability in this evaluation, reached **9.9%**, substantially exceeding GPT-4o with browsing. The paper suggests that strong reasoning and internal knowledge can sometimes reconstruct or surface an answer without live web access.

Deep Research achieved **51.5%**, far outperforming every other evaluated model and solving approximately half of the benchmark. The authors attribute this result to its ability to:

- Search autonomously and persistently,
- Evaluate and synthesize multiple sources,
- Change its strategy when early searches fail,
- Process large amounts of web information, and
- Support its claims with citations.

These abilities are particularly relevant to BrowseComp’s niche and non-intuitive questions.

### 4.4 Confidence calibration

All evaluated systems had high calibration errors, ranging from **65% to 91%**. The two browsing-enabled systems were especially poorly calibrated:

- GPT-4o with browsing: **82% calibration error**
- Deep Research: **91% calibration error**

Deep Research was therefore the most accurate model but also had the largest reported calibration error. The authors infer that web access may make models more confident even when their conclusions are wrong. This is especially concerning for high-stakes or ambiguous information-seeking tasks because users may have difficulty distinguishing correct research from confident error.

### 4.5 Scaling with browsing effort

**Figure 1** plots BrowseComp accuracy against test-time compute on a logarithmic horizontal scale for an early Deep Research model. Each point represents a complete evaluation run using a different level of browsing effort.

Accuracy rises smoothly from roughly **9% at the lowest shown effort to slightly above 50% at the highest shown effort**. The intermediate points follow a steady increasing pattern rather than showing a sudden threshold. Exact compute values are not labeled in the supplied figure, so the relationship can be described only as monotonic scaling with increasing test-time compute.

This result indicates that allowing an agent to spend more effort searching directly improves its ability to solve BrowseComp questions.

### 4.6 Parallel sampling and answer aggregation

**Figure 4** plots Deep Research accuracy against the number of parallel samples per task for majority voting, confidence-weighted voting, and best-of-N selection.

Approximate values visible in the graph are:

| Parallel samples | Best-of-N | Weighted voting | Majority voting |
|---:|---:|---:|---:|
| 1 | 0.52 | 0.52 | 0.52 |
| 2 | 0.60 | 0.60 | 0.53 |
| 4 | 0.67 | 0.65 | 0.58 |
| 8 | 0.71 | 0.67 | 0.63 |
| 16 | 0.74 | 0.69 | 0.66 |
| 32 | 0.76 | 0.69 | 0.67 |
| 64 | 0.78 | 0.70 | 0.67 |

These values are read approximately from the plotted points; the paper’s text gives the broader conclusion that the three aggregation methods improve performance by **15% to 25%** compared with one attempt.

Best-of-N consistently performs best and continues improving as more samples are added, reaching approximately **78% accuracy at 64 samples**. Weighted voting reaches about **70%**, while majority voting plateaus near **67%**.

The strong performance of best-of-N suggests that Deep Research’s confidence contains useful relative information. Although its confidence values are badly calibrated as absolute probabilities, the model often assigns higher confidence to its correct outputs than to its incorrect ones. In the authors’ terms, it frequently has an internal indication that it is right even when it cannot translate that signal into a well-calibrated probability.

### 4.7 Distribution of task difficulty

**Figure 5** compares the distribution of 64-trial pass rates for OpenAI o1 and Deep Research.

For Deep Research:

- **16% of tasks** had a 100% pass rate, meaning every trial solved them.
- **14% of tasks** had a 0% pass rate, meaning none of the 64 trials solved them.
- Many tasks occupied intermediate pass-rate bins, showing a broad continuum of difficulty.

For OpenAI o1, the figure labels the zero-pass-rate group as **79.3%**. Thus, nearly four-fifths of tasks were never solved by o1 across the 64 trials. Its remaining tasks are spread thinly across nonzero pass rates, with only small percentages reaching high pass rates.

The contrasting distributions show that BrowseComp is not uniformly difficult. Some items are reliably solvable by Deep Research, some are intermittently solvable, and others resist repeated attempts entirely. Performance depends on the item’s structure and domain.

### 4.8 Follow-up on zero-pass-rate items

When Deep Research was given the ground-truth answer for tasks it had never solved and was asked to find supporting evidence, it succeeded in most cases. This shows that many zero-pass-rate questions were not impossible to verify or unsupported by the web. Instead, they were extremely difficult to discover from the clues alone.

The result supports the paper’s claim that BrowseComp measures more than basic retrieval. It tests whether an agent can:

- Persist after unsuccessful searches,
- Reformulate searches flexibly,
- Identify promising directions,
- Combine fragmented evidence, and
- Navigate a large candidate space without being told the answer.

### 4.9 Dataset auditing

BrowseComp initially contained **1,287 tasks**. The authors reviewed **118 tasks** on which Deep Research had a 0% pass rate. They identified **21 defective items** whose labeled answers:

- Did not match the required answer format,
- Were ambiguous because of the question’s phrasing, or
- Were incorrect after further reasoning.

Those 21 items were removed, producing the final **1,266-question** benchmark. This auditing process demonstrates that model failure can reveal annotation problems as well as genuinely hard questions.

## 5. Analysis and Interpretation

The findings support the benchmark’s intended design. BrowseComp is easy to grade but difficult for both humans and models to solve. Human trainers abandoned **70.8%** of attempted questions after approximately two hours, while ordinary language models achieved below 1% accuracy. Even adding browsing to GPT-4o produced only **1.9%**, showing that a search interface without effective reasoning and persistence does not solve the problem.

The comparison between GPT-4o with browsing and o1 without browsing suggests that browsing capability and reasoning capability make separate contributions. Browsing gives access to information, but reasoning is needed to decide what to search for, connect indirect clues, and judge whether evidence is reliable. Deep Research combines both capabilities and consequently achieves much higher accuracy.

The test-time scaling results indicate that browsing performance is not fixed after training. More search effort within a run and more independent trials both improve results. This is especially important for questions whose answers are straightforward to recognize once discovered but difficult to locate initially.

Best-of-N improves more than majority voting because correct answers need not be the most frequent outputs. A model may generate a correct answer only occasionally but assign it unusually high confidence. This makes confidence useful for ranking candidate answers even though the numerical confidence values themselves remain unreliable.

The pass-rate analysis reveals several kinds of questions:

- Questions that Deep Research solves consistently,
- Questions it solves only under some search trajectories, and
- Questions that require guidance before it can locate supporting evidence.

The success of evidence retrieval after revealing the answer suggests that the hardest part is often discovering the right entity or search path, not verifying the final fact.

Relative to earlier retrieval benchmarks, BrowseComp focuses specifically on information that cannot ordinarily be found by a human within ten minutes. Early browsing agents with few tool calls and weak backtracking are therefore expected to struggle. More recent reasoning agents trained through reinforcement learning are described as more likely to achieve at least double-digit performance.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **A new benchmark for persistent web browsing:** BrowseComp contains 1,266 questions centered on obscure, entangled information rather than easily searchable facts.
- **A hard-to-find, easy-to-check format:** The benchmark separates the difficulty of information discovery from the difficulty of grading by using short reference answers.
- **A human-created difficulty process:** Questions were screened against multiple models, simple search attempts, and—in a subset of cases—other human trainers.
- **Evidence about the importance of reasoning and browsing together:** Browsing alone produced little improvement for GPT-4o, while Deep Research’s combination of strategic reasoning and persistent tool use achieved 51.5%.
- **Evidence of test-time scaling:** Accuracy increased smoothly with greater browsing effort and rose further when multiple independent attempts were aggregated.
- **Evaluation of aggregation strategies:** Best-of-N reached approximately 78% accuracy with 64 samples and outperformed weighted and majority voting.
- **A task-level difficulty analysis:** Sixty-four trials per question exposed a wide distribution of pass rates and helped identify 21 flawed dataset items.
- **An open evaluation resource:** The benchmark is made available through OpenAI’s `simple-evals` repository to support work on more trustworthy and reliable browsing agents.

## 7. Limitations and Caveats

The paper identifies several important limitations:

- **BrowseComp is not a realistic distribution of ordinary user queries.** It deliberately emphasizes rare, difficult facts rather than common information needs.
- **It does not evaluate long-form responses.** Answers are short strings, so the benchmark avoids measuring report quality, organization, completeness, and explanation.
- **It sidesteps ambiguity resolution.** Real user requests may be underspecified, whereas BrowseComp aims for a single reference answer.
- **Uniqueness is not guaranteed.** Because questions are constructed around a known answer, another undiscovered answer may occasionally satisfy the same clues.
- **Strong benchmark performance may not generalize to all browsing tasks.** Finding obscure facts is only one component of useful internet assistance.
- **The human comparison is not a ceiling on human ability.** Trainers were experienced with the dataset but were not professional investigators or competitive search specialists.
- **Model confidence is unreliable.** Browsing-enabled systems, especially Deep Research, were highly overconfident according to the reported calibration errors.
- **Deep Research received relevant training.** Its 51.5% score should be interpreted with the explicit caveat that it was trained on data intended to improve BrowseComp-style performance.
- **The grader is model-based.** Semantic equivalence is determined by an AI judge rather than entirely through deterministic exact matching or manual review.
- **The benchmark primarily uses textual evidence.** It does not evaluate research that requires extracting information from images, audio, video, or interactive web interfaces.
- **Dataset defects remain possible.** Review of the hardest items found formatting mismatches, ambiguity, and incorrect labels; although 21 such questions were removed, the construction method cannot absolutely guarantee that every remaining item is unique and flawless.
- **High-compute performance is expensive.** The strongest aggregation result requires up to 64 full outputs per question, substantially more test-time work than a single attempt.

## 8. Future Work or Open Questions

The authors explicitly identify several directions:

- Develop future benchmarks that require interaction with **images, video, audio, and interactive webpages**, rather than relying primarily on textual web evidence.
- Evaluate additional AI agents on BrowseComp and gather feedback from researchers.
- Use the open benchmark to encourage work on more **trustworthy and reliable** browsing agents.

The results also leave open questions directly raised by the paper’s analyses:

- How can browsing agents preserve the useful ranking signal in their confidence while producing accurately calibrated probabilities?
- How can agents achieve the benefits of extensive browsing and 64-way sampling with less test-time computation?
- How well does BrowseComp performance transfer to real user tasks involving ambiguity, long answers, and broader forms of web interaction?
- How can benchmark construction better guarantee that no alternative valid answer exists?
- What search, backtracking, and reformulation mechanisms distinguish intermittently solvable questions from those that remain at a 0% pass rate?

## 9. High-Level Takeaway (Plain Language)

BrowseComp tests whether an AI can find a very specific fact hidden among many websites when ordinary searching is not enough. Its 1,266 questions are intentionally difficult but have short answers that are easy to check. Humans solved only 29.2% of attempted questions, ordinary models scored near zero, and OpenAI Deep Research reached 51.5%. Giving that agent more browsing effort or multiple independent attempts raised performance substantially, with best-of-64 selection reaching about 78%. The central lesson is that successful web research requires more than access to a search tool: an agent must reason, persist, change strategies, connect scattered clues, and recognize when it has found the right answer—while still learning to communicate uncertainty reliably.