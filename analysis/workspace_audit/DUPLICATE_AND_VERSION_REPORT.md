# Duplicate and version report

Evidence labels: OBSERVED = directly established; INFERRED = interpretation of observations; UNKNOWN = insufficient evidence; CONFLICTING = sources disagree. CURRENT_SYSTEM refers only to live files outside the reference ZIP and audit outputs. Archive citations use `ZIP!rebuild/...:lines` and refer exclusively to REFERENCE_TARGET_ARCHITECTURE. Recommendations are PROPOSED_INTEGRATION, not executed changes.

## Exact content duplicates

OBSERVED: SHA-256 of every discovered PDF yields 117 files, 112 distinct hashes and five groups of two. All extra copies are archived under 99_Duplicates/Exact; no hash duplicates exist between active canonical paths. No exact pair uses differing filenames. The full paths/hashes are in `CORPUS_INVENTORY.csv`.

| Active source | Archived identical path | SHA-256 |
| --- | --- | --- |
| 02_Web_Agent_Benchmarks_Environments/The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf | 99_Duplicates/Exact/The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf | faf67147c8f28aca96ad6174c3ccaf4f127bab91fdeaaf0a8ac92f110e4fe09a |
| 02_Web_Agent_Benchmarks_Environments/WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf | 99_Duplicates/Exact/WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf | 2240e08a747462c59b49796e56985428f592e45d96debfa2aa88286263a4a787 |
| 07_Security_Benchmarks_Evaluation/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf | 99_Duplicates/Exact/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf | 9adb2f4e55bf9bfd171f7ddfc2c5f46c168f1cd28326101552b81fd2ebd2aaec |
| 09_Progress_Long_Horizon_Benign_Controls/AgentRewardBench_Evaluating_Automatic_Evaluations_of_Web_Agent_Trajectories.pdf | 99_Duplicates/Exact/AgentRewardBench_Evaluating_Automatic_Evaluations_of_Web_Agent_Trajectories.pdf | 9c7d44da20f638f58d8aa4f547685eb1ebd9da78127c44493a9f2e31d0e324c9 |
| 09_Progress_Long_Horizon_Benign_Controls/The_Long-Horizon_Task_Mirage_Diagnosing_Where_and_Why_Agentic_Systems_Break.pdf | 99_Duplicates/Exact/The_Long-Horizon_Task_Mirage_Diagnosing_Where_and_Why_Agentic_Systems_Break.pdf | 515851522526216becaadd883a6a1201e45fdc8b4259c3bc55698253c501119c |

CONFLICTING: all five historical inventory `exact_duplicate_of` fields still point to New paths, not their surviving canonical locations (`docs/paper_inventory.csv:114-118`). Byte identity resolves the relationship in this audit without editing those records. The reference's ingest-first hash representative would depend on its new papers-directory scan order (`ZIP!rebuild/scripts/litrevctl.py:131-140`); do not let it silently choose new canonical identities.

## Report-version groups

| Group | Observed evidence | Classification / safe treatment |
| --- | --- | --- |
| Mind the Web (two PDFs) | Same four authors and near-identical title; first-page visual shows ACM ASIA CCS 2026 DOI 10.1145/3779208.3805968 versus arXiv:2510.04965v2 dated 20 Oct 2025; distinct SHA values and abstract wording | PROBABLE_ALTERNATE_VERSION, high identity evidence; preserve separate manifest IDs, no scientific-equivalence adjudication. |
| AGENTFUZZER filename / AgentVigil filename | First file metadata/title says AgentVigil: Generic Black-Box Red-teaming, arXiv:2505.05849v4 14 Jun 2025; other says AgentVigil: Automatic Black-Box Red-teaming, EMNLP 2025 pp23159-23172; same nine authors | PROBABLE_ALTERNATE_VERSION; stale AGENTFUZZER filename is not another system. Both v2 aliases preserved; inspect semantic deltas before contribution grouping. |

Evidence: each corresponding source PDF p.1, text extraction and direct visual inspection during audit; CSV `title_evidence`, `version_relation`, `notes`. Similarity scan over normalized filenames at >=0.87 found these two pairs only; it is a candidate generator, not an exhaustive proof that no other bibliographic relationships exist. Metadata and title-page checks cover all 117 PDFs. No full paper comparison was performed.

| Path | Pages | SHA-256 |
| --- | --- | --- |
| 04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AGENTFUZZER_Generic_Black-Box_Fuzzing_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf | 14 | f41a7b42c8e11de28365641c590d92d9da831ad4bf4aee426e985dc07c2c27b7 |
| 04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AgentVigil_Generic_Black-Box_Red-teaming_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf | 14 | 4bc0b57c44454a82f6d979378e223c49e7367ab137c189394eb9db510a2ffc39 |
| 05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web-Use_Agents.pdf | 17 | 5a834c4ef546307f06cb4d081cce6d026ec9a7029039befbf9ff18bb70831a9a |
| 05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web_Use_Agents.pdf | 13 | d9d8dd67c192eccb3a47c2a13d06258f4250f5c24a2d84516abab9686bd3f7ad |

UNKNOWN: exact independent-study/contribution count. If these two groups each represent one contribution, 112 reports would give 110 candidate groups; do not publish that as adjudicated research-object count. Existing docs only list the Mind-the-Web filename pair (`docs/near_duplicate_candidates.csv:2-3`), so automated folder/hash handling has not resolved the additional AgentVigil relationship.

## Manual review and taxonomy

OBSERVED: 98_Manual_Review has no files, yet two version relationships require semantic review; the directory is not a comprehensive review register. Both organizers classify by ordered filename regexes and assign tags, preserving near-title candidates without auto-merging (`organize_agentic_web_crawlers_new_preferred.py:70-328,510-568`). Original and New-preferring variants disagree on duplicate canonical preference (`original:353-369`; `new_preferred:353-376`). Exact executed flags are unknown. Keep historical aliases, hashes, paths, and version uncertainty during any future import.
