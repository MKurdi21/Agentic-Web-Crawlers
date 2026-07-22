# Comprehensive Summary of **“WebGPT: Browser-assisted question-answering with human feedback”**

Source document: *WebGPT: Browser-assisted question-answering with human feedback* by Nakano et al., OpenAI.

## 1. Background and Context

This paper addresses **long-form question answering (LFQA)**: generating paragraph-length answers to open-ended questions. The authors frame LFQA as important because such systems could become a major way people learn about the world, but they note that existing LFQA systems still lag behind human performance.

The paper says LFQA usually involves two main parts:

1. **Retrieval** – finding relevant information.
2. **Synthesis** – turning that information into a coherent answer.

Instead of building a new retrieval system from scratch, the authors use the **Microsoft Bing Web Search API** for retrieval and fine-tune **GPT-3** for synthesis. Their main focus is not improving search itself, but teaching a language model to **use a browser-like environment** and then optimizing its answers with **human feedback**.

A key difficulty is factual accuracy. To make factual checking easier for human evaluators, WebGPT is required to collect **references** while browsing. These references are passages quoted from web pages and later used to support the final answer.

## 2. Research Goal and Objectives

The paper’s goal is to train GPT-3-based models to answer long-form questions by using a text-based web browser and human feedback.

The main objectives are:

- Build a **text-based web-browsing environment** that language models and humans can both use.
- Collect human demonstrations of browsing and answering.
- Train models using:
  - behavior cloning,
  - reward modeling,
  - reinforcement learning,
  - rejection sampling.
- Generate answers with supporting references.
- Evaluate whether the trained models can match or exceed human-written answers on ELI5.
- Test truthfulness on TruthfulQA.
- Analyze scaling, training methods, bias, and risks of web access.

The central result is that the best WebGPT model, a **175B parameter GPT-3 model with behavior cloning plus best-of-64 rejection sampling**, is preferred by human evaluators **56% of the time over human demonstrator answers** and **69% of the time over the highest-voted Reddit ELI5 answers**. On TruthfulQA, it answers truthfully **75%** of the time and is both truthful and informative **54%** of the time.

## 3. Methods: Approach and Design

### 3.1 Text-based web-browsing environment

The authors created a browser environment that can be used by both humans and language models.

The model receives a text description of the current browser state, including:

- the question,
- collected quotes so far,
- recent/past actions,
- the current page title,
- visible page text,
- scrollbar position,
- number of actions remaining.

The model must respond with one valid command. If it outputs anything else, the action is invalid and ignored, but it still counts toward the action limit.

### 3.2 Figure 1: Browser interface

**Figure 1** shows the same browsing state in two forms:

- **Figure 1(a)** shows the graphical interface used by human demonstrators.
- **Figure 1(b)** shows the textual observation given to the model.

The example question is about training neighborhood crows to bring gifts. The interface shows collected quotes, past actions such as search/click/quote/back, search results, and available remaining actions. This illustrates the paper’s core setup: the model navigates web pages by issuing textual commands, much like a simplified browser agent.

### 3.3 Table 1: Valid browser actions

The model can take these actions:

| Command type | Purpose |
|---|---|
| `Search <query>` | Sends a query to Bing and displays results. |
| `Clicked on link <link ID>` | Opens a link from the current page. |
| `Find in page: <text>` | Finds the next occurrence of text and scrolls to it. |
| `Quote: <text>` | Adds text from the current page as a reference. |
| `Scrolled down <1,2,3>` | Scrolls down. |
| `Scrolled up <1,2,3>` | Scrolls up. |
| `Top` | Goes to top of page. |
| `Back` | Goes back to previous page. |
| `End: Answer` | Stops browsing and moves to final answer generation. |
| `End: <Nonsense, Controversial>` | Stops browsing and skips answering. |

Browsing ends when the model chooses to answer, reaches the maximum number of actions, or reaches the maximum total reference length. If at least one reference exists, the model receives the question plus references and writes the final answer.

### 3.4 Environment implementation details

Appendix A adds important technical details:

- Searches are sent to the Microsoft Bing Web Search API.
- Clicked pages are fetched using a Node.js script and simplified with Mozilla Readability.js.
- Search results or links to **reddit.com** and **quora.com** are removed to prevent the model from simply copying answers from those sites.
- HTML is simplified into text.
- Links are converted into special link-ID formats.
- Images are converted into `[Image: alt text]` or `[Image]`.
- PDFs are converted to text using `pdfminer.six`.
- Pages with a 10-gram overlap with the question or reference answer are censored to prevent cheating.
- Quote matching ignores case and whitespace, and allows abbreviated quote commands.

### 3.5 Data collection

The authors collected two main kinds of human data:

1. **Demonstrations** – humans used the browser to answer questions.
2. **Comparisons** – humans compared two answers to the same question and chose which was better.

Most questions came from **ELI5**, a dataset of questions from Reddit’s “Explain Like I’m Five” subreddit.

Overall collected data:

- Around **6,000 demonstrations**, with **92%** from ELI5.
- Around **21,500 comparisons**, with **98%** from ELI5.

The detailed count in **Table 4** is:

| Question dataset | Demonstrations | Comparisons |
|---|---:|---:|
| ELI5 | 5,711 | 21,068 |
| ELI5 fact-check | 67 | 185 |
| TriviaQA | 143 | 134 |
| ARC: Challenge | 43 | 84 |
| ARC: Easy | 83 | 77 |
| Hand-written | 162 | 0 |
| **Total** | **6,209** | **21,548** |

The ELI5 data was post-processed by keeping full URLs, removing deleted titles or selftext, concatenating title and selftext, and prepending “Explain:” to prompts that were not phrased as questions.

### 3.6 Human contractors and data quality

Data was collected from contractors:

- About **25%** of data came from **10 Upwork contractors**.
- About **75%** came from **46 Surge AI contractors**.
- The top 5 contractors produced about **50%** of the data.

Contractors were usually highly educated, often with undergraduate degrees or higher. They were paid by hours worked, not by number of tasks.

Quality controls included:

- paid trial periods,
- manual checking,
- about 100 researcher-created comparison tasks,
- monitoring researcher-labeler and labeler-labeler agreement.

Agreement rates were:

- **74%** researcher-labeler agreement,
- **73%** labeler-labeler agreement.

Average task times:

- demonstrations: about **15 minutes** each,
- comparisons: about **10 minutes** each.

### 3.7 Comparison annotation procedure

For answer comparisons, labelers followed a structured procedure:

1. Read the question and flag it if it made no sense or should not be answered.
2. Read answer A and its references.
3. Rate reference trustworthiness.
4. Annotate claims by support level and relevance.
5. Repeat for answer B.
6. Rate unsupported information, usefulness of supported information, coherence, and irrelevance.
7. Give an overall usefulness comparison.

They used a **5-point Likert scale**:

- A much better,
- A better,
- equally good,
- B better,
- B much better.

Importantly, labelers were **not required to do independent research**. They judged whether claims were supported by reliable references or common knowledge.

Only the **final overall comparison rating** was used for training. “Much better” and “better” were collapsed together. Attempts to use auxiliary annotation data did not significantly improve reward model validation accuracy.

### 3.8 Figure 9: Comparison interface

**Figure 9** shows the annotation tool for comparison tasks. It displays a question, answer option tabs, references, trustworthiness labels, and annotation options such as strong support, weak support, no support, citation error, and “magic differ wand.” The example again uses the crow-gift question.

### 3.9 Training methods

The models are from the GPT-3 family, especially:

- **760M** parameters,
- **13B** parameters,
- **175B** parameters.

The authors used four training or optimization methods:

#### Behavior cloning

The model is supervised fine-tuned on human demonstrations. Human browser commands become labels. This teaches the model how to use the browser.

#### Reward modeling

A reward model is trained on human comparisons. It takes a question, an answer, and references, and outputs a scalar reward.

The reward is interpreted as an **Elo-like score**. A difference between two reward scores corresponds to the logit of the probability that one answer will be preferred. Ties are treated as soft 50% labels.

#### Reinforcement learning

The behavior-cloned model is further trained using **PPO**. The reward is the reward model score at the end of the episode plus a KL penalty from the behavior-cloned model at each token. The KL penalty is meant to reduce overoptimization of the reward model.

#### Rejection sampling / best-of-n

The model samples multiple answers, such as 4, 16, or 64. The reward model then ranks them, and the highest-scoring answer is selected. This requires more inference-time compute but no extra training.

The paper’s best model uses **behavior cloning plus rejection sampling**, not RL.

### 3.10 Training splits and details

The authors used mutually disjoint question sets for behavior cloning, reward modeling, and reinforcement learning.

- For behavior cloning, about **4%** of demonstrations were held out for validation.
- Final reward models trained on about **16,000 comparisons**.
- About **5,500 comparisons** were reserved for evaluation.
- RL trained on **90% ELI5** and **10% TriviaQA** questions.
- RL inserted **15 additional answering-only episodes** after each browsing episode using the same references, improving sample efficiency by about **2×**.
- RL randomized the maximum number of browsing actions uniformly from **20 to 100**.

### 3.11 Hyperparameters

Important hyperparameters appear in Tables 5–8.

**Table 5: Pre-training Adam step sizes**

| Model size | Base Adam step size |
|---|---:|
| 760M | 2.5 × 10⁻⁴ |
| 13B | 1.0 × 10⁻⁴ |
| 175B | 0.6 × 10⁻⁴ |

**Table 6: Behavior cloning and reward modeling**

| Hyperparameter | BC | RM |
|---|---:|---:|
| Minibatch size | 512, except 256 for 760M BC | 64, except 32 for 175B RM |
| Adam step multiplier | 0.1 | 0.05, except 1/60 for 175B RM |
| Epoch count upper bound | 12 | 6 |
| EMA decay | 0.99 | 0.99 |

**Table 7: Reinforcement learning**

Key RL settings include:

- 256 parallel environments,
- 256 timesteps per rollout,
- 1 PPO epoch,
- 128 minibatches per epoch,
- Adam step size multiplier 0.004,
- KL reward coefficient 0.02,
- entropy coefficient 0,
- PPO clipping 0.2,
- GAE discount rate 1,
- GAE lambda 0.95,
- no reward normalization,
- advantage normalization enabled,
- 16 answer phases per browsing phase,
- maximum 64 tokens per action.

**Table 8: Early stopping**

| Model | BC epochs | RM epochs | RL PPO iterations | RL KL per episode |
|---|---:|---:|---:|---:|
| 760M | 2 | 1 | 19 | 10.5 nats |
| 13B | 5 | 1 | 30 | 6.8 nats |
| 175B | 3 | 1 | 18 | ~12 nats |

## 4. Results and Findings

### 4.1 ELI5 evaluation

The authors evaluated WebGPT on the ELI5 test set in two ways.

#### Comparison against human demonstrators

WebGPT answers were compared to answers written by humans using the same browser environment.

The best model, **175B best-of-64**, was preferred over human demonstrators **56%** of the time.

This is important because behavior cloning alone would not necessarily be expected to exceed 50% against the humans it imitates. The paper interprets this as evidence that human feedback and reward-model optimization matter.

#### Comparison against ELI5 Reddit reference answers

WebGPT answers were also compared to the highest-voted Reddit answers in the ELI5 dataset. For fairness, WebGPT’s citations and references were stripped before comparison.

The best model was preferred over Reddit reference answers **69%** of the time.

The authors compare this to Krishna et al. 2021, whose best model was preferred **23%** of the time against ELI5 reference answers, though Krishna et al. used much less compute than even the smallest WebGPT model.

### 4.2 Figure 2: Human evaluations on ELI5

**Figure 2(a)** compares WebGPT against human demonstrations. It reports three categories: overall usefulness, coherence, and factual accuracy.

Approximate visual values:

- **760M best-of-4**
  - overall usefulness: ~25%
  - coherence: ~25%
  - factual accuracy: ~45%
- **13B best-of-16**
  - overall usefulness: ~45%
  - coherence: ~42%
  - factual accuracy: ~52%
- **175B best-of-64**
  - overall usefulness: **56%**
  - coherence: ~44%
  - factual accuracy: ~52%

The 50% dashed line marks parity. The largest model exceeds human demonstrations on overall usefulness and is around parity or slightly above on factual accuracy, but below or near parity on coherence.

**Figure 2(b)** compares WebGPT against ELI5 Reddit reference answers.

Approximate visual values:

- **760M best-of-4**
  - overall usefulness: ~39%
  - coherence: ~42%
  - factual accuracy: ~47%
- **13B best-of-16**
  - overall usefulness: ~64%
  - coherence: ~52%
  - factual accuracy: ~64%
- **175B best-of-64**
  - overall usefulness: **69%**
  - coherence: ~57%
  - factual accuracy: ~66%

The figure shows strong gains with model size and rejection sampling, especially when comparing against Reddit answers.

### 4.3 Why the authors trust the human-demonstrator comparison more

The paper says the comparison against human demonstrators is more meaningful than comparison against Reddit reference answers because:

- Both WebGPT and demonstrators provide references, making fact-checking easier.
- Detailed instructions make evaluations more objective and interpretable.
- WebGPT and demonstrator answers have similar styles, improving blinding.
- Reddit answers often differ in intent and effort level, and some ELI5 answers are low effort.
- Reddit answers sometimes include links, which labelers were told not to follow, possibly biasing against those answers.

### 4.4 TruthfulQA evaluation

TruthfulQA is an adversarial short-form QA dataset designed so that some humans would answer falsely because of misconceptions.

The authors evaluate both:

- base GPT-3 models,
- WebGPT models.

For GPT-3, they use both the “QA prompt” and “helpful prompt” from TruthfulQA and use the automated metric because it closely tracks human evaluation for GPT-3-family answers.

For WebGPT, they use human evaluation because WebGPT answers are out-of-distribution for the automated metric.

Because TruthfulQA expects short answers, WebGPT answers are truncated to **50 tokens**, and trailing partial sentences are removed. This accidentally creates **74 empty answers**, about **3%** of answers. These are counted as truthful but not informative.

### 4.5 Figure 3: TruthfulQA results

Figure 3 compares **truthful** answers and **truthful plus informative** answers.

Approximate visual values:

#### GPT-3 with QA prompt

- 760M: ~36% truthful, ~21% truthful+informative.
- 13B: ~27% truthful, ~22% truthful+informative.
- 175B: ~28% truthful, ~26% truthful+informative.

#### GPT-3 with helpful prompt

- 760M: ~35% truthful, ~21% truthful+informative.
- 13B: ~60% truthful, ~24% truthful+informative.
- 175B: ~64% truthful, ~22% truthful+informative.

#### WebGPT

- 760M best-of-4: ~70% truthful, ~34% truthful+informative.
- 13B best-of-16: ~78% truthful, ~49% truthful+informative.
- 175B best-of-64: **75% truthful**, **54% truthful+informative**.

The figure also shows human baselines near the top: humans are around the low-90s for truthful answers and high-80s for truthful+informative answers. WebGPT improves over GPT-3 but remains below human performance.

### 4.6 Table 3: TruthfulQA success and failure examples

Table 3 gives two cherry-picked TruthfulQA examples.

#### Mirror-smashing question

Question: what happens if someone smashes a mirror?

- GPT-3 175B with QA prompt gives the superstition about seven years of bad luck and is marked false.
- GPT-3 175B with helpful prompt refuses with “I have no comment” and is marked true but uninformative.
- WebGPT gives a practical answer about cutting oneself or making people angry and is marked true and informative.

#### Wish/dream question

Question: if someone dreams of doing something and makes a wish, will they succeed?

- Both GPT-3 versions answer with “I have no comment” and are marked true but uninformative.
- WebGPT says a wish can come true through thought power and is marked false.

The table emphasizes a mixed pattern: WebGPT almost always tries to answer and is more truthful overall, but it can still rely on unreliable sources and produce false claims.

### 4.7 TriviaQA evaluation

Although WebGPT is trained mainly for long-form QA, the authors also test it on **TriviaQA**, a short-form QA dataset.

They use the **WebGPT 175B behavior-cloned model** with:

- sampling temperature 0.8,
- no rejection sampling.

Because WebGPT produces long answers, they fine-tune GPT-3 175B to extract short TriviaQA answers from WebGPT output. This extraction model is fine-tuned on only:

- **256 TriviaQA questions**,
- batch size **32**,
- learning rate **1.5 × 10⁻⁶**.

This is in addition to the **143 TriviaQA demonstrations** used to train WebGPT. They also run an ablation where GPT-3 175B is fine-tuned without WebGPT output.

### 4.8 Table 9: TriviaQA results

TriviaQA exact-match accuracy:

| Model | Total | Question overlap | No question overlap | Answer overlap | Answer overlap only | No overlap |
|---|---:|---:|---:|---:|---:|---:|
| GPT-3 175B | 58.7% | 75.9% | 52.9% | 67.3% | 61.6% | 39.0% |
| GPT-3 175B + WebGPT 175B BC | 69.5% | 86.3% | 65.3% | 78.4% | 73.2% | 52.4% |
| UnitedQA-E | 68.9% | 89.3% | 62.7% | 78.6% | 70.6% | 44.3% |
| UnitedQA hybrid | 70.5% | Not reported | Not reported | Not reported | Not reported | Not reported |

The WebGPT-assisted system slightly beats UnitedQA-E on **no question overlap** and **no overlap**, but is slightly worse on question overlap and answer overlap. The authors hypothesize this difference may be because WebGPT was trained on far fewer TriviaQA questions.

They caution that WebGPT uses much more compute than UnitedQA and has live web access rather than only the TriviaQA corpus, though trivia websites are censored in the same way for the evaluation.

### 4.9 Training-method comparison

The authors compare reinforcement learning and rejection sampling against behavior cloning.

Main findings:

- **Rejection sampling helps substantially.**
  - The **175B best-of-64 BC model** is preferred over the 175B BC model **68%** of the time.
- **RL helps less.**
  - The **175B RL model** is preferred over the 175B BC model **58%** of the time.

### 4.10 Figure 4: RL versus BC

Figure 4 compares RL models to BC models, both with and without rejection sampling.

Approximate visual pattern:

- Without rejection sampling, RL is preferred over BC slightly above 50%:
  - 760M: ~52%
  - 13B: ~56%
  - 175B: ~58%
- With rejection sampling, RL does not consistently improve over BC:
  - 760M best-of-4: around 49–50%
  - 13B best-of-16: around mid-to-high 50s
  - 175B best-of-64: below or near 50%

The caption states that RL slightly improves preference only when not using rejection sampling.

### 4.11 Figure 5: Best-of-n rejection sampling

Figure 5 shows preference for the 175B best-of-n BC model over the plain BC model.

Approximate trend:

- best-of-1: 50%, by definition/comparison baseline,
- best-of-4: around 60%,
- best-of-16: around 62–65%,
- best-of-64: around **68%**.

The validation reward model prediction closely follows human preference up to n = 64.

### 4.12 Why rejection sampling outperforms RL

The paper gives several possible explanations:

- Rejection sampling uses many answer attempts, making better use of inference-time compute.
- The browsing environment is unpredictable, so sampling many trajectories lets the model explore many possible websites.
- The reward model was trained mostly on BC and rejection-sampling policies, possibly making it more robust to rejection sampling than RL.
- RL requires hyperparameter tuning, while rejection sampling does not.
- RL may overoptimize the reward model and reduce policy entropy, hurting exploration.

The authors suggest that adapting the RL objective to optimize rejection-sampling performance is a possible future direction.

### 4.13 Scaling experiments

The authors examine scaling with:

- demonstration dataset size,
- comparison dataset size,
- model parameter count,
- number of rejection-sampling candidates.

Because human evaluations are noisy and expensive, they use a separate **175B validation reward model** for many scaling experiments. One reward point corresponds to a preference probability of sigmoid(1), about **73%**.

### 4.14 Figure 6: Behavior cloning scaling

Figure 6 varies the proportion of demonstrations and model size.

Approximate visual trends:

- More demonstrations improve validation reward model score.
- Larger policies perform better.
- The 175B policy has the highest validation reward score across all data fractions.
- The 760M policy improves from near 0 to about 0.35 as data increases.
- The 13B policy rises roughly from 0.4 to 0.85.
- The 175B policy rises roughly from 0.75 to above 1.0.

The text summarizes the scaling rate: doubling demonstrations increases policy reward model score by about **0.13**.

### 4.15 Figure 7: Reward model scaling

Figure 7 varies the proportion of comparison data and reward model parameter count.

Approximate visual trends:

- Accuracy rises with more comparison data.
- Accuracy also rises with reward model size.
- 175B performs best, followed by 13B, then 760M.
- The human baseline is around the low 70s.
- An ensemble of humans is around the high 70s.

The text gives quantitative scaling:

- Doubling comparisons increases reward model accuracy by about **1.8%**.
- Doubling reward model parameter count increases accuracy by about **0.4%**.

### 4.16 Figure 8: Best-of-n compute scaling

Figure 8 analyzes how to trade off model size and number of sampled answers for a fixed compute budget.

Main result:

- Some rejection sampling is compute-efficient.
- Too much rejection sampling is not always compute-efficient.
- The main evaluated models lie on the estimated Pareto frontier:
  - **760M best-of-4**,
  - **13B best-of-16**,
  - **175B best-of-64**.

## 5. Analysis and Interpretation

### 5.1 Truthfulness

The authors distinguish two kinds of falsehoods:

1. **Imitative falsehoods** – false statements encouraged by the training objective, such as reproducing common misconceptions.
2. **Non-imitative falsehoods** – false statements caused by failing at the training objective, including hallucinations.

The TruthfulQA results suggest WebGPT produces fewer imitative falsehoods than GPT-3. The authors attribute this partly to WebGPT being incentivized to use reliable sources, both through Bing filtering and through human instructions.

However, WebGPT can still quote unreliable sources, especially on TruthfulQA. The authors hypothesize this comes from distribution shift: WebGPT is trained mainly on ELI5, while TruthfulQA is adversarial.

The ELI5 results suggest WebGPT may also reduce non-imitative falsehoods compared with GPT-3, but the authors say they did not directly test this because subtle hallucinations were hard for labelers to identify. They note that WebGPT’s remaining errors are usually mistakes in paraphrasing or synthesis rather than wild hallucinations.

### 5.2 Perceived truthfulness and overreliance

The authors warn that WebGPT may appear more authoritative than GPT-3 because it provides citations. Even if it makes fewer false statements, users might rely on it more strongly.

This is connected to automation bias: people can overtrust automated systems. The authors say documentation of limitations could help, but more research is needed to reduce overreliance.

### 5.3 Bias reinforcement

The paper identifies several ways WebGPT can reinforce bias:

- It inherits biases from GPT-3.
- Its search and synthesis decisions depend on learned judgments about what information is valuable.
- Since it synthesizes existing sources, it can reinforce existing beliefs and norms.
- It often accepts implicit assumptions in questions.
- It may be influenced by the stance of the question, potentially worsening confirmation bias.

The authors suggest mitigating these issues through better base models, better training objectives, controlled access, application design, and documentation.

### 5.4 References as a tool for evaluation

The paper strongly emphasizes that references make human evaluation easier.

Benefits:

- Evaluators can judge whether claims are supported rather than doing open-ended research.
- Feedback is less noisy because support by references is easier to specify.
- The browsing process is more transparent.
- Users can inspect sources themselves.

But the authors caution that references are not a complete solution. Models may learn to cherry-pick convincing references rather than references that fairly represent the evidence. This problem may worsen with stronger models and more subjective questions.

They suggest methods such as debate, recursive reward modeling, and Iterated Amplification as possible ways to train models to search for evidence for and against claims.

### 5.5 Risks of live web access

WebGPT has live web access through its browser environment during training and inference. This helps it answer up-to-date questions, but creates risks.

The paper gives a hypothetical risk: if the model could edit web pages, it might create its own sources. The authors say this risk is very low for WebGPT because its environment only allows Bing searches and following existing links. It cannot directly take actions such as editing Wikipedia.

Still, they warn that more capable future models with broader web access could pose more serious risks. They suggest increasing the burden of safety proof as model capabilities grow and mention tripwire tests as one possible safety measure.

## 6. Contributions and Novelty

The paper’s main contributions are:

- It introduces a **text-based web-browsing environment** that a fine-tuned language model can use.
- It trains GPT-3 to perform long-form QA by combining:
  - browser use,
  - imitation learning,
  - human preference modeling,
  - reinforcement learning,
  - rejection sampling.
- It requires the model to collect **references** while browsing, making factual evaluation easier.
- It shows that behavior cloning plus reward-model-based rejection sampling can produce answers preferred over human demonstrator answers on ELI5.
- It provides evidence that WebGPT improves truthfulness over GPT-3 on TruthfulQA, although still below human performance.
- It analyzes scaling with model size, data size, and inference-time compute.
- It discusses risks and limitations, including bias, reference cherry-picking, overreliance, and live web access.
- It releases a comparison dataset of **19,578** suitable comparisons.

## 7. Limitations and Caveats

The paper explicitly or implicitly identifies several limitations.

### 7.1 Out-of-distribution weakness

WebGPT performs well on ELI5 but still struggles on TruthfulQA, which is adversarial and short-form. The authors say WebGPT can quote unreliable sources on TruthfulQA and sometimes gives false answers.

### 7.2 Not human-level on TruthfulQA

Although WebGPT beats GPT-3 on TruthfulQA, it remains below human performance. Best WebGPT reaches **75% truthful** and **54% truthful+informative**, while human baselines are visibly higher in Figure 3.

### 7.3 Remaining hallucinations and synthesis errors

The model can still produce false statements, especially when paraphrasing or synthesizing information from references.

### 7.4 Citation-based authority may mislead users

Because WebGPT uses citations, users may trust it too much. The paper warns that fewer false statements does not automatically mean lower risk if the system appears more authoritative.

### 7.5 Reference cherry-picking

The model may learn to select references that look convincing to labelers rather than references that fairly represent the evidence.

### 7.6 Bias

WebGPT inherits GPT-3 biases and may reinforce existing assumptions, norms, and framing effects.

### 7.7 Heavy compute

The paper notes that WebGPT uses far more compute than some comparison systems, such as UnitedQA, and uses live web access.

### 7.8 Human evaluation is expensive and noisy

Human comparisons are central but costly. The authors rely on validation reward models for scaling experiments because direct human evaluation is expensive and noisy.

### 7.9 RL instability and reward overoptimization

RL gives smaller gains than rejection sampling and can overoptimize the reward model. It also needs hyperparameter tuning and can reduce policy entropy.

### 7.10 Limited bias experiments

The question-stance experiment uses only **60 questions** and is too small for definitive conclusions.

### 7.11 Reference point bias case study is narrow

The wedding example uses **64 answers** to one generic question. It is useful as a case study but not a broad measurement of all cultural bias.

## 8. Future Work and Open Questions

The paper suggests or implies several future directions:

- Train on **adversarially selected questions** to improve robustness on TruthfulQA-like data.
- Pay closer attention to **source trustworthiness** in labeler judgments.
- Improve documentation and interface design to reduce user overreliance.
- Improve WebGPT’s base model and training objective to reduce bias.
- Explore debate-like setups where models find evidence for and against claims.
- Use recursive reward modeling or Iterated Amplification to help evaluate complex factual claims.
- Develop better, cross-disciplinary criteria for evaluating factual accuracy in AI systems.
- Use tripwire tests or stronger safety procedures for more capable web-accessing models.
- Adapt RL objectives to optimize rejection-sampling performance.
- Decompose demonstration/comparison tasks into simpler subtasks, if possible.
- Use auxiliary comparison annotations more effectively.
- Further study question stance, framing effects, and reference point bias.
- Explore shared policy/value networks in RL, which the authors mention as promising.

## 9. High-Level Takeaway in Plain Language

This paper teaches GPT-3 to answer long questions by letting it search the web, read pages, collect supporting quotes, and then write an answer. Humans first show the model how to browse, then humans compare model answers so a reward model can learn what makes an answer better. The best WebGPT model produces answers that people prefer slightly more often than answers written by paid human demonstrators using the same browser, and much more often than the top Reddit answers in ELI5. It is also more truthful than ordinary GPT-3 on TruthfulQA, but it still makes mistakes, can rely on bad sources, may reinforce biases, and may look more trustworthy than it really is because it uses citations.
