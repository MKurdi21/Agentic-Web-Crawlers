# Research Mode continuation report

Initial completed: **5**. Newly completed: **10**. Total: **15**. Pending: **90**. Excluded holdouts: **7 (B02–B08)**. Failed/deferred: **none**.

Five sequential batches of two were processed with the existing runner. No architecture or historical experiment changes were made. Existing pilot outputs are byte-identical.

## New deliverables

| Paper | Markdown | Structured record |
|---|---|---|
| AutoWebGLM: A Large Language Model-based Web Navigating Agent | [Summary](summaries/autowebglm_comprehensive_summary.md) | [JSON](records/autowebglm_comprehensive_summary.json) |
| Go-Browse: Training Web Agents with Structured Exploration | [Summary](summaries/go_browse_comprehensive_summary.md) | [JSON](records/go_browse_comprehensive_summary.json) |
| GPT-4V(ision) is a Generalist Web Agent, if Grounded | [Summary](summaries/seeact_comprehensive_summary.md) | [JSON](records/seeact_comprehensive_summary.json) |
| LASER: LLM Agent with State-Space Exploration for Web Navigation | [Summary](summaries/laser_comprehensive_summary.md) | [JSON](records/laser_comprehensive_summary.json) |
| WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | [Summary](summaries/webvoyager_comprehensive_summary.md) | [JSON](records/webvoyager_comprehensive_summary.json) |
| BEARCUBS: A benchmark for computer-using web agents | [Summary](summaries/bearcubs_comprehensive_summary.md) | [JSON](records/bearcubs_comprehensive_summary.json) |
| BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents | [Summary](summaries/browsecomp_comprehensive_summary.md) | [JSON](records/browsecomp_comprehensive_summary.json) |
| Mind2Web: Towards a Generalist Agent for the Web | [Summary](summaries/mind2web_comprehensive_summary.md) | [JSON](records/mind2web_comprehensive_summary.json) |
| MMInA: Benchmarking Multihop Multimodal Internet Agents | [Summary](summaries/mmina_comprehensive_summary.md) | [JSON](records/mmina_comprehensive_summary.json) |
| The BrowserGym Ecosystem for Web Agent Research | [Summary](summaries/browsergym_comprehensive_summary.md) | [JSON](records/browsergym_comprehensive_summary.json) |

## Validation

All fifteen completed Markdown/record pairs passed readback, output/source identity, schema, required ordered sections and source-page checks. The ten additions contain **154 checked claim groups**. Important quantitative claims and selected figures/tables were reviewed; see [review notes](CONTINUATION_REVIEW.md) and [machine-readable results](continuation_validation.json). All fourteen tests passed.

The [catalog](catalog.md) contains fifteen records. [Inventory](inventory.json) retains 112 canonical papers and five archive entries; [progress](progress.json) contains the actual final states. Ten pilot output files and nine monitored historical files are unchanged. All 105 eligible source hashes match the authoritative checkpoint. Reserved canonical PDFs were not opened.

## Extraction concerns

- Source counts and prose/table rankings sometimes conflict (Go-Browse, Bearcubs, BrowseComp, Mind2Web, MMINA, BrowserGym); outputs flag unresolved differences.
- Grounding assistance, unequal evaluation dates/budgets, offline ground-truth histories, judge agreement and conditional denominators limit cross-paper comparisons.
- Skipped evaluations remain unmeasured. Plot estimates remain approximate. Missing external artifacts and incomplete visual legibility remain explicit.
- Seven responses required canonical heading repairs; some quotations required exact source spelling, hyphenation or spacing. Originals and correction notes are retained locally.
- Author risk discussions and analyst relevance are separated from measured attacks. These papers do not establish a controlled comparative vulnerability result.

These are proportional source checks, not independent human scientific validation or exhaustive verification of every narrative sentence.

Resume remaining eligible work only when requested, using `research/.venv/Scripts/python.exe -B scripts/research_mode.py --limit 2`.
