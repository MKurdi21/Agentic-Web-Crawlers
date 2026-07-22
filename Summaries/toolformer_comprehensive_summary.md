# Toolformer: Language Models Can Teach Themselves to Use Tools

**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom  
**Affiliations:** Meta AI Research and Universitat Pompeu Fabra

## 1. Background and Context

Large language models can solve many tasks from instructions or a few examples, especially as they grow larger. However, scaling alone does not fully solve several basic weaknesses:

- They cannot directly access current information.
- They may invent or “hallucinate” facts.
- They struggle with low-resource languages.
- They are unreliable at exact arithmetic.
- They lack an inherent awareness of the current date and the passage of time.

External tools—such as search engines, calculators, calendars, translation systems, and question-answering systems—can compensate for these weaknesses. Earlier tool-using systems, however, generally required either substantial human supervision or task-specific prompts demonstrating exactly which tool to use and how to use it.

The paper proposes two requirements for a more general solution:

- Tool use should be learned through self-supervision rather than extensive human annotation. Besides reducing cost, this allows the model—not a human annotator—to determine which information is useful for its own predictions.
- The language model should retain its general abilities and independently decide when to call a tool, which tool to select, what arguments to provide, and how to incorporate the returned result.

The work relates to retrieval-augmented language-model pretraining, supervised and prompted tool use, and bootstrapping or self-training. Its distinction is that the model explicitly learns to request information only when that information helps it predict subsequent text, without task-specific tool-use demonstrations at evaluation time.

## 2. Research Goal and Objectives

The central goal is to determine whether a pretrained language model can teach itself to use multiple external tools through simple textual API calls.

The authors seek to demonstrate that a model can:

1. Generate candidate API calls from only a few demonstrations of each API.
2. identify useful calls using its own language-modeling loss rather than human labels;
3. learn when, how, and which tool to call;
4. improve zero-shot performance across factual, mathematical, multilingual, and temporal tasks;
5. retain its ordinary language-modeling ability; and
6. learn tool use across different model sizes, revealing when this capability emerges.

The resulting model, **Toolformer**, is based primarily on a 6.7-billion-parameter GPT-J model.

## 3. Methods (Approach/Design)

### Overall self-supervised process

Toolformer begins with a plain-text language-modeling dataset \(C\) and converts it into an augmented dataset \(C^*\) containing API calls and their results. It then fine-tunes the original model on this augmented text.

An API call is represented as an API name plus an input. Its textual form includes special markers for the start and end of the call and an arrow separating the request from its result. In practice, the authors use existing character sequences—`[`, `]`, and `->`—so that the model’s vocabulary does not need to be modified.

**Figure 2** presents the three main data-generation stages:

1. **Sample candidate calls:** Given ordinary text, the language model proposes positions and possible API calls.
2. **Execute calls:** Each proposed call is sent to the relevant tool to obtain a textual result.
3. **Filter calls:** A call is retained only if supplying its request and result reduces the model’s loss when predicting the following text.

In the figure’s example, the sentence “Pittsburgh is also known as the Steel City” produces two candidate questions. Asking what other name Pittsburgh is known by returns “Steel City” and helps predict the continuation, so it is retained. Asking which country Pittsburgh is in returns “United States” but does not help predict “the Steel City,” so it is removed. The retained call is inserted into the original sentence.

### Sampling candidate API calls

For each tool, the authors write a prompt containing a small number of human-written examples. The model then annotates ordinary text with possible calls.

At every position in a text, the system calculates the probability that the next token starts an API call. Positions exceeding a sampling threshold \(\tau_s\) are retained, up to the top \(k\) positions. At each position, up to \(m\) candidate calls are sampled. Examples are discarded if the model fails to generate the closing API token.

**Figure 3** shows the question-answering prompt. It instructs the model to insert questions that would provide information needed to complete a passage. Demonstrations include asking where Joe Biden was born before “Scranton” and asking what other name Coca-Cola is known by before “Coke.”

The default generation settings are:

- Sampling threshold \(\tau_s=0.05\)
- At most \(k=5\) candidate positions per text
- Up to \(m=5\) calls per position
- Filtering threshold \(\tau_f=1.0\)

Because calculator and translation opportunities are relatively rare, those tools use:

- \(\tau_s=0\)
- \(k=20\)
- \(m=10\)
- \(\tau_f=0.5\)

### Executing and filtering calls

Each proposed call is executed using the relevant API. Every response must be representable as one text sequence.

For a call at position \(i\), the authors calculate a weighted cross-entropy loss over the subsequent tokens. In simple terms, this measures how difficult the continuation is for the model to predict.

They compare:

- \(L_i^+\): prediction loss when the model receives both the API call and its result;
- \(L_i^-\): the better of prediction without any call and prediction with the call but without its result.

A call is retained if:

\[
L_i^- - L_i^+ \geq \tau_f
\]

Thus, the result must reduce future-token loss by at least the filtering threshold. Subsequent tokens receive declining weights, using unnormalized weights \(\max(0,1-0.2t)\), so a tool result is rewarded mainly when it helps close to where it was inserted.

During filtering, the call and result are provided as a prefix rather than inserted into the middle of the passage. Before fine-tuning, inserting unfamiliar API syntax within a passage could itself disrupt the model and artificially worsen perplexity.

### Fine-tuning and inference

After filtering, calls from all tools are combined and inserted into their original texts. Apart from these insertions, the augmented corpus contains the same underlying text as the original corpus. The authors argue that this helps preserve general language ability.

Toolformer is fine-tuned using the standard next-token language-modeling objective. At inference time, ordinary decoding continues until the model emits the arrow token indicating that it expects an API response. Generation pauses, the appropriate API is called, and decoding resumes after inserting the result and closing marker.

### The five tools

**Table 1** gives representative inputs and outputs:

- **Question answering:** A factual question such as where the Knights of Columbus was founded returns “New Haven, Connecticut.”
- **Wikipedia search:** A query such as “Fishing Reel Types” returns a relevant Wikipedia snippet.
- **Calculator:** `27 + 4 * 2` returns `35`.
- **Calendar:** Takes no input and returns a sentence such as “Today is Monday, January 30, 2023.”
- **Machine translation:** The French phrase *sûreté nucléaire* returns “nuclear safety.”

The implementations are:

1. **Question answering:** Atlas, a retrieval-augmented model fine-tuned on Natural Questions. Atlas-large generates training data; Atlas-xxl is used during inference.
2. **Calculator:** A Python-based calculator supporting the four basic arithmetic operations. Results are rounded to two decimal places, and invalid expressions return no result.
3. **Wikipedia search:** A BM25 retriever indexing the KILT Wikipedia dump. It provides broader information than the QA system, but Toolformer must extract the relevant content itself.
4. **Machine translation:** The 600M-parameter NLLB model, supporting 200 languages. fastText detects the input language, and output is always English.
5. **Calendar:** A no-input API returning the current date.

**Figure 1** illustrates autonomous use of four APIs:

- QA identifies the Massachusetts Medical Society as the publisher of *The New England Journal of Medicine*.
- The calculator turns \(400/1400\) into 0.29.
- Translation renders Spanish *tortuga* as “turtle.”
- Wikipedia search retrieves information explaining California’s Brown Act.

### Training data and heuristics

The base corpus is a subset of CCNet. To reduce annotation cost, tool-specific heuristics identify passages where a call is likely to help.

For the calculator, passages are considered if they contain mathematical relationships, calculation-related expressions followed by numbers, or at least three nearby numbers. Only 1% of documents satisfying merely the broad three-number criterion are retained.

For calendar examples, the document date is approximated from its URL. Texts without an extractable date are removed, leaving about 18% of documents.

For translation, the system keeps paragraphs containing a non-English 10-token chunk surrounded by English. fastText must classify the chunk as non-English with confidence above 0.8. Chunks containing only numbers or symbols are removed. Calls whose input appears only after the proposed call are also deleted because inference cannot look ahead.

**Table 2** reports the number of retained examples at different filtering thresholds:

| API | \(\tau_f=0.5\) | \(\tau_f=1.0\) | \(\tau_f=2.0\) |
|---|---:|---:|---:|
| Question answering | 51,987 | 18,526 | 5,135 |
| Wikipedia search | 207,241 | 60,974 | 13,944 |
| Calculator | 3,680 | 994 | 138 |
| Calendar | 61,811 | 20,587 | 3,007 |
| Machine translation | 3,156 | 1,034 | 229 |

Stricter filtering sharply reduces data volume, particularly for calculator and translation calls.

### Fine-tuning configuration

Training uses:

- Up to 25,000 examples per API
- Maximum sequence length of 1,024
- Effective batch size of 128
- Learning rate \(1\times10^{-5}\)
- Linear warmup over the first 10% of training
- Up to 2,000 training steps
- Perplexity evaluation every 500 steps on 1,000 CCNet development examples
- Selection of the best checkpoint
- DeepSpeed ZeRO-3 with BF16
- Eight NVIDIA A100 40GB GPUs

### Models and evaluation design

The principal comparisons are:

- **GPT-J:** Unmodified pretrained model
- **GPT-J + CC:** GPT-J fine-tuned on the plain CCNet subset
- **Toolformer (disabled):** Toolformer with API calls prohibited during decoding
- **Toolformer:** API-enabled model
- **OPT (66B)**
- **GPT-3 (175B):** Original `davinci`, without instruction fine-tuning

OPT and GPT-3 are approximately 10 and 25 times larger than the 6.7B-parameter GPT-J-based models.

All downstream tests use prompted **zero-shot** evaluation: instructions are given, but no task-specific demonstrations are provided. Toolformer is allowed at most one API call per input. During decoding, it can initiate a call whenever the API-start token is among the top \(k=10\) token choices, rather than only when it is the single most likely token.

## 4. Results and Findings

### Factual completion: LAMA

The authors evaluate SQuAD, Google-RE, and T-REx subsets of LAMA. Only examples with the missing item at the end are retained. A response is correct if the answer appears among the first five generated words. Wikipedia search is disabled because LAMA statements come directly from Wikipedia.

**Table 3:**

| Model | SQuAD | Google-RE | T-REx |
|---|---:|---:|---:|
| GPT-J | 17.8 | 4.9 | 31.9 |
| GPT-J + CC | 19.2 | 5.6 | 33.2 |
| Toolformer (disabled) | 22.1 | 6.3 | 34.9 |
| **Toolformer** | **33.8** | **11.5** | **53.5** |
| OPT (66B) | 21.6 | 2.9 | 30.1 |
| GPT-3 (175B) | 26.8 | 7.0 | 39.8 |

Toolformer improves over the strongest non-tool GPT-J baseline by 11.7, 5.2, and 18.6 points on the three datasets. It also surpasses OPT and GPT-3. It uses QA for 98.1% of examples, another tool for 0.7%, and no tool for 1.2%.

### Mathematical reasoning

The tests are ASDiv, SVAMP, and MAWPS. The first predicted number is evaluated, except that if the response includes an equation, the first number after the equals sign is used.

**Table 4:**

| Model | ASDiv | SVAMP | MAWPS |
|---|---:|---:|---:|
| GPT-J | 7.5 | 5.2 | 9.9 |
| GPT-J + CC | 9.6 | 5.0 | 9.3 |
| Toolformer (disabled) | 14.8 | 6.3 | 15.0 |
| **Toolformer** | **40.4** | **29.4** | **44.0** |
| OPT (66B) | 6.0 | 4.9 | 7.9 |
| GPT-3 (175B) | 14.0 | 10.0 | 19.8 |

Toolformer with APIs more than doubles the disabled model’s performance on every task and clearly exceeds both larger models. It selects the calculator on 97.9% of examples. Even the disabled version improves over GPT-J, which the authors attribute to fine-tuning on many calculator calls and numerical results.

### Open-domain question answering

The datasets are Web Questions, Natural Questions, and TriviaQA. A result is correct if the answer occurs within the first 20 generated words. Toolformer’s QA API is disabled to avoid making the task trivial—especially because that API was trained on Natural Questions—so it mainly uses Wikipedia search.

**Table 5:**

| Model | WebQS | NQ | TriviaQA |
|---|---:|---:|---:|
| GPT-J | 18.5 | 12.8 | 43.9 |
| GPT-J + CC | 18.4 | 12.2 | 45.6 |
| Toolformer (disabled) | 18.9 | 12.6 | 46.7 |
| **Toolformer** | **26.3** | **17.7** | **48.8** |
| OPT (66B) | 18.6 | 11.4 | 45.7 |
| GPT-3 (175B) | 29.0 | 22.6 | 65.9 |

Toolformer improves over all GPT-J-based baselines and uses Wikipedia search for 99.3% of examples, but remains below GPT-3. The authors attribute this partly to the simple retriever returning poor matches and Toolformer’s inability to inspect multiple results or reformulate an unsuccessful query.

### Multilingual question answering

MLQA supplies an English context and a question in Spanish, German, Hindi, Vietnamese, Simplified Chinese, or Arabic. The answer must appear within ten generated words. The translation tool is used on 63.8%–94.9% of examples depending on language, except Hindi, where it is used only 7.3%.

**Table 6:**

| Model | Spanish | German | Hindi | Vietnamese | Chinese | Arabic |
|---|---:|---:|---:|---:|---:|---:|
| GPT-J | 15.2 | 16.5 | 1.3 | 8.2 | 18.2 | 8.2 |
| GPT-J + CC | 15.7 | 14.9 | 0.5 | 8.3 | 13.7 | 4.6 |
| Toolformer (disabled) | 19.8 | 11.9 | 1.2 | 10.1 | 15.0 | 3.1 |
| Toolformer | 20.6 | 13.5 | 1.4 | 10.6 | 16.8 | 3.7 |
| OPT (66B) | 0.3 | 0.1 | 1.1 | 0.2 | 0.7 | 0.1 |
| GPT-3 (175B) | 3.4 | 1.1 | 0.1 | 1.7 | 17.7 | 0.1 |
| GPT-J, all-English input | 24.3 | 27.0 | 23.9 | 23.3 | 23.1 | 23.6 |
| GPT-3, all-English input | 24.7 | 27.2 | 26.1 | 24.9 | 23.6 | 24.0 |

API access consistently improves Toolformer over its disabled version, showing useful translation behavior. Nevertheless, it does not consistently beat vanilla GPT-J because CCNet fine-tuning harms some languages, possibly through distribution shift.

OPT and GPT-3 perform unexpectedly poorly because they often fail to answer in English despite being instructed to do so. Their much stronger performance when both question and context are supplied in English supports the interpretation that the multilingual component causes the difficulty.

### Temporal reasoning

The study uses:

- **TEMPLAMA:** Time-changing Wikidata facts for 2010–2020.
- **DATESET:** A newly generated collection of questions requiring knowledge of a presumed current date.

**Table 7:**

| Model | TEMPLAMA | DATESET |
|---|---:|---:|
| GPT-J | 13.7 | 3.9 |
| GPT-J + CC | 12.9 | 2.9 |
| Toolformer (disabled) | 12.7 | 5.9 |
| **Toolformer** | **16.3** | **27.3** |
| OPT (66B) | 14.5 | 1.3 |
| GPT-3 (175B) | 15.5 | 0.8 |

Toolformer leads on both datasets. On TEMPLAMA, however, it uses the calendar in only 0.2% of examples; the gains mostly come from QA and Wikipedia search because the named entities are often too specific for the date alone to help.

On DATESET, the improvement is attributable to the calendar, which is used on 54.8% of examples.

**Table 11** describes DATESET’s construction. The authors randomly choose 500 current dates and generate past and future dates within a four-year range. Seven template groups produce:

- 400 questions asking how many days ago or until a date;
- 800 asking what calendar unit applied a specified time ago;
- 800 asking what unit will apply after a future interval;
- 400 asking the weekday of a past or future date;
- 4,000 asking about the day before yesterday, yesterday, today, tomorrow, or the day after tomorrow;
- 1,800 asking when a U.S. federal holiday occurs that year;
- 1,200 asking the interval to or from such a holiday.

The total is **9,400 questions**.

### Preservation of language modeling

Perplexity is evaluated on WikiText and 10,000 held-out CCNet documents.

**Table 8:**

| Model | WikiText | CCNet |
|---|---:|---:|
| GPT-J | 9.9 | 10.6 |
| GPT-J + CC | 10.3 | 10.5 |
| Toolformer (disabled) | 10.3 | 10.5 |

Fine-tuning on CCNet slightly improves held-out CCNet perplexity but slightly worsens WikiText. Crucially, adding API calls to the training data produces no additional perplexity cost relative to ordinary CCNet fine-tuning when APIs are disabled.

The authors do not report perplexity with APIs enabled because computing it would require marginalizing over every possible API call at every position, which is intractable.

### Scaling behavior

**Figure 4** plots average LAMA, mathematics, and QA performance against model size for GPT-2 models with 124M, 355M, 775M, and 1.6B parameters and GPT-J at 6.7B. Blue lines represent Toolformer with APIs; red lines represent the same models with APIs disabled; dotted lines show GPT-3 performance.

The key pattern is that useful tool use emerges at approximately **775M parameters**. The smallest models perform similarly with and without APIs. Larger models improve both at solving tasks unaided and at using tools, leaving a substantial enabled-versus-disabled gap even at 6.7B parameters. Wikipedia search on QA is the main exception: smaller models gain somewhat from it, possibly because search is comparatively easy to use.

### Decoding strategy

**Table 9** measures how the top-\(k\) API triggering rule affects T-REx and WebQS. “AC” is performance when an API is called; “NC” is performance when none is called.

| \(k\) | T-REx All | AC | NC | Calls | WebQS All | AC | NC | Calls |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.9 | — | 34.9 | 0.0% | 18.9 | — | 18.9 | 0.0% |
| 1 | 47.8 | 53.0 | 44.3 | 40.3% | 19.3 | 17.1 | 19.9 | 8.5% |
| 3 | 52.9 | 58.0 | 29.0 | 82.8% | 26.3 | 26.5 | 6.6 | 99.3% |
| 10 | 53.5 | 54.0 | 22.5 | 98.1% | 26.3 | 26.4 | — | 100.0% |

Increasing \(k\) makes calls much more frequent. T-REx improves substantially even with ordinary greedy decoding (\(k=1\)), while WebQS requires a modest increase in \(k\) before search calls become common.

At \(k=1\), the model shows partial calibration: the cases where it declines to call an API score 44.3 on T-REx and 19.9 on WebQS, exceeding the respective no-API averages of 34.9 and 18.9. Thus, it tends to call tools on examples it would otherwise find harder. This selectivity disappears at larger \(k\).

### Quality of generated calls

**Table 10** orders examples by the filtering score \(L_i^- - L_i^+\). High scores generally correspond to calls that visibly help predict subsequent text:

- Wikipedia retrieves information about the Flodden Window: score **5.49**, useful.
- Calendar supplies the date before a reference to “March 10”: **2.11**, useful.
- QA supplies the Nile’s length, 6,853 km: **2.08**, useful.
- Calculator computes \(735/499=1.47\): **1.59**, useful.
- A Wikipedia query for “Fast train success” returns irrelevant information yet still lowers loss: **0.92**, judged not useful.
- Translation renders Portuguese as “The Best Schools in Jersey”: **0.70**, useful.
- Calendar precedes “Easter Egg Hunt”: **0.33**, judged useful.
- Calculator incorrectly treats \(85/23\) as relevant to a later 65% statement: **−0.02**, not useful.
- An unrelated calendar call in a Disneyland passage scores **−0.41**, not useful.
- A malformed QA question, “Who was last time I was with?”, scores **−1.23**, not useful.

The filtering signal therefore corresponds reasonably well—but not perfectly—to intuitive usefulness. The authors note that some retained noise may be beneficial because it teaches the model not to follow every API result blindly.

## 5. Analysis and Interpretation

The experiments support the paper’s primary claim: a model can learn multi-tool use from its own candidate annotations and prediction-loss feedback.

The largest gains appear where a tool directly addresses the task’s bottleneck:

- QA supplies missing facts for LAMA.
- The calculator performs exact operations for math problems.
- Wikipedia search supplies broad factual evidence for open-domain QA.
- Translation helps interpret non-English questions.
- The calendar provides the current-date context needed by DATESET.

Fine-tuning on API-containing text can also improve some internal abilities even when tools are disabled, most clearly in mathematics. However, this effect is much smaller than the gain from actually executing calls.

Toolformer’s comparison with much larger models shows that external capabilities can sometimes compensate for parameter count. The 6.7B model surpasses 66B OPT and 175B GPT-3 on LAMA, mathematical reasoning, and temporal tasks. It does not surpass GPT-3 on open-domain QA or consistently surpass GPT-J on MLQA.

The scaling results indicate that generating syntactically valid calls is not sufficient: a model must be large enough—around 775M parameters in these experiments—to understand when returned information is useful and incorporate it effectively.

The results also expose a distinction between single-step tasks and tasks requiring interaction. Toolformer performs well when one well-chosen call is sufficient. It is weaker when it would need to reformulate a search, inspect several results, or use one tool’s output as another tool’s input.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It introduces **Toolformer**, a general language model that learns to call multiple external tools through textual APIs.
- It proposes a self-supervised procedure in which the model generates its own candidate calls and retains those that reduce future-token prediction loss.
- It teaches one model to select among QA, Wikipedia search, calculation, translation, and calendar tools without task-specific tool demonstrations during evaluation.
- It preserves the original language-modeling text while adding calls, avoiding an additional perplexity penalty from tool-use training.
- It demonstrates large zero-shot gains for a 6.7B-parameter model, including performance above much larger OPT and GPT-3 models on several task families.
- It provides evidence that effective tool use is scale-dependent and begins to emerge at roughly 775M parameters in the tested model family.
- It introduces DATESET, a 9,400-example temporal benchmark constructed to require knowledge of a current date.

Unlike approaches that always append retrieved information, Toolformer explicitly learns whether information should be requested. Unlike heavily supervised or task-specific tool-use methods, its tool behavior is learned from a few API demonstrations and self-generated training examples.

## 7. Limitations and Caveats

The authors identify several important limitations:

- **No chained calls:** Toolformer cannot feed one tool’s output into another. Calls for each API are generated independently, so the training data contains no chains.
- **No interactive use:** It cannot browse multiple search results, assess them iteratively, or reformulate an unsuccessful query.
- **One-call evaluation restriction:** Experiments permit at most one call per input to prevent call loops. This prevents strategies such as querying the calendar and then using the date in a QA request.
- **Prompt sensitivity:** Whether Toolformer calls an API can depend strongly on the exact wording of the input.
- **Sample inefficiency:** Processing more than one million documents can yield only a few thousand useful calculator examples.
- **No cost awareness:** Decisions do not account for the tool-dependent computational cost of an API call.
- **Imperfect filtering:** A reduction in language-modeling loss does not always correspond to a semantically useful result.
- **Simple search infrastructure:** The BM25 Wikipedia system often returns poor matches, contributing to weaker QA performance than GPT-3.
- **Possible distribution shift:** Fine-tuning on the selected CCNet data harms performance for some languages and slightly worsens WikiText perplexity.
- **Calendar data approximation:** Training assumes the date inferred from a document URL is the relevant document date, and this can be extracted for only about 18% of documents.
- **Tool-specific evaluation constraints:** Wikipedia search is disabled on LAMA, and QA is disabled on open-domain QA, to avoid unfair or trivial solutions.
- **Limited calculator:** It supports only basic arithmetic and rounds results to two decimal places.
- **Scale dependence:** Models below roughly 775M parameters generally do not benefit much from tool access.
- **Enabled perplexity is unavailable:** The study verifies preservation of language modeling only with API calls disabled because exact enabled-model perplexity is computationally intractable.

## 8. Future Work or Open Questions

The paper points to several extensions:

- Generate training examples containing **chains of calls**, allowing one tool’s result to become another tool’s input.
- Make tools interactive, particularly by allowing search-result browsing, repeated searches, and query reformulation.
- Apply the self-supervised generation and filtering process iteratively to improve sample efficiency, as in bootstrapping methods.
- Incorporate the computational cost of each tool into the decision about whether to call it.
- Improve search quality and allow the model to examine multiple retrieved results.
- Reduce sensitivity to prompt wording.
- Investigate better data selection or training procedures that avoid multilingual distribution shifts.
- Study how to prevent repetitive call loops while allowing more than one useful call.
- Further explore why effective tool use emerges only beyond a certain model scale.

## 9. High-Level Takeaway (Plain Language)

Toolformer teaches a language model to recognize when it needs outside help. Starting from only a few examples of each tool, the model invents possible API calls, keeps the ones that make later text easier to predict, and trains on those calls. A 6.7B-parameter model learned to look up facts, search Wikipedia, calculate answers, translate questions, and check dates, producing large zero-shot gains and sometimes beating models many times larger. Its present form is strongest when one well-chosen call solves the problem; it cannot yet conduct multi-step or interactive tool use.