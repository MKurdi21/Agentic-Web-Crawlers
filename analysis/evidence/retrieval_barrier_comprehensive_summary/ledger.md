# Retrieval Barrier: Cumulative Evidence Ledger

Status: partial source review in progress; no review attestation issued.
Source and prompt fingerprints are in `run.json` and the global checkpoint.

## Accessibility and Inventory Corrections

- The available PDF has 20 pages. Native extraction reported no low-text pages.
- The initial renderer selected pages 1, 2, 4-14, 19, and 20. Rendering alone does
  not establish inspection. This recovery pass directly inspected pages 10 and
  11, including Figure 9 and Table 2. Other pages remain to be reviewed here.
- `accessibility.json` reports `appendix_pages_detected: [11]`. This is a false
  positive for an appendix boundary: page 11 starts with a continuation that
  refers to Appendix A.3. The heuristic detects references, not reliable section
  boundaries. Determine appendix coverage from the PDF itself.
- Source text contains NUL characters. Use `rg -a` for searches. Equations and
  table alignment require visual confirmation despite readable surrounding text.

## Verified Source Observations

| Object | Source | Observation | Status / Caveat |
|---|---|---|---|
| Figure 9 | p. 10 | Heatmap reports RAG attack success rate across 11 LLMs and 11 datasets. The injected target is the answer Yes; the color scale runs from 0 to 1. | [B] Axes, cells, caption inspected. Do not conflate ASR with retrieval recall. |
| Figure 9 setup | p. 10, section 5.1 continuation | Queries where the clean system already gives the target answer are excluded. Results average five random seeds. | [A] Definition affects the denominator and interpretation. |
| Figure 9 model-count discrepancy | p. 10, heatmap versus caption/setup | The caption and text say 11 LLMs, but the visible chart contains 12 model rows: six Qwen rows, four Llama rows, and two Vicuna rows (6 + 4 + 2 = 12). | [C] Analyst-counted rows; retain both counts and investigate without silently reconciling them. |
| Table 2 | p. 11 | Columns separate targeted answer, phishing worm, tool misuse, single-agent code execution, and multi-agent code execution; model blocks are GPT-4o and GPT-4o-mini. | [B] Preserve task and model conditions. |
| Multi-agent code execution, Ours (Fusion) | p. 11, Table 2, GPT-4o block | R@5 = 1; SIM = .85; ASR = .80 +/- .07. | [B] Exact table representation transcribed with ASCII uncertainty notation. |
| Multi-agent code execution, Ours (CEM) | p. 11, Table 2, GPT-4o block | R@5 = 1; SIM = .78; ASR = .72 +/- .16. | [B] A different method from Fusion. |
| Multi-agent code execution, Ours (Fusion) | p. 11, Table 2, GPT-4o-mini block | R@5 = 1; SIM = .83; ASR = .36 +/- .09. | [B] Do not generalize the GPT-4o result to this model. |
| Table 2 uncertainty | p. 11, Metric paragraph | Each experiment is repeated five times with different random seeds; mean and standard deviation are reported. | [A] The displayed uncertainty is not a confidence interval. |
| Query adaptation | pp. 10-11, section 5.2 | An agent may reformulate the original user query before retrieval. | [A] This qualifies comparisons with the RAG setting. |

## Remaining Work

Read and inventory the complete document, including the actual appendix and
all substantive panels, equations, algorithms, and experiments. Revisit the
draft after generation and compare the observations above with its wording.
No global completeness or numerical verification claim is established by this
partial ledger. Continue with pages 1-9 and 12-20, then resolve cross-references.
