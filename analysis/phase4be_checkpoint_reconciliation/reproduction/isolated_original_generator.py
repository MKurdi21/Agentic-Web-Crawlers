"""Refresh recoverable corpus state without model calls or summary edits."""

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('G:\\My Drive\\Papers\\Agentic Web Crawlers')
STATE = ROOT / "analysis"
OUTPUT = Path('G:\\My Drive\\Papers\\Agentic Web Crawlers\\analysis\\phase4be_checkpoint_reconciliation\\reproduction')
REQUIRED = [
    "Plain-Language Orientation", "Document Roadmap", "Background and Context",
    "Research Problem and Gap", "Research Questions", "Assumptions / Threat Model",
    "Methodology", "Experiments / Analyses", "Results", "Figure-by-Figure",
    "Table-by-Table", "Diagram / Architecture", "Equations and Mathematical",
    "Interpretation and Discussion", "Contributions and Novelty", "Limitations",
    "Threats to Validity", "Future Work and Open Questions",
    "Terminology and Notation Glossary", "Key Numerical Results", "Evidence Map",
    "Very Simple Explanation",
]


def digest(path):
    if not path.is_file():
        return None
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def resolve(value):
    path = (ROOT / value.replace("\\", "/")).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Path outside repository: {value}")
    return path


def normalized(value):
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def check_structure(path):
    if not path.is_file():
        return {"passed": False, "missing": [], "characters": 0}
    text = path.read_text(encoding="utf-8-sig")
    headings = re.findall(r"(?m)^#{1,6}\s+(.+)$", text)
    clean = [normalized(h) for h in headings]
    missing = []
    positions = []
    for number, title in enumerate(REQUIRED, 1):
        matches = [i for i, h in enumerate(clean)
                   if re.match(rf"^{number}\s+", h)
                   and normalized(title) in h]
        if matches:
            positions.append(matches[0])
        else:
            missing.append(f"{number}. {title}")
    if not any("stage 0" in h for h in clean):
        missing.append("Stage 0")
    if not any("completeness audit" in h for h in clean):
        missing.append("Completeness Audit")
    ordered = positions == sorted(set(positions))
    return {"passed": not missing and ordered and len(text) >= 20000,
            "missing": missing, "numbered_sections_in_order": ordered,
            "characters": len(text)}


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    temporary.replace(path)


def main():
    now = '2026-09-28T00:14:51.262910+00:00'
    with (STATE / "manifest.csv").open(encoding="utf-8-sig", newline="") as stream:
        manifest = list(csv.DictReader(stream))
    reviews = json.loads((STATE / "reviews.json").read_text(encoding="utf-8"))
    prompt_hash = digest(STATE / "PROMPT.md")
    if not prompt_hash:
        raise ValueError("Missing saved prompt")
    issues = []
    all_pdfs = [ROOT / p for p in ['01_Core_Web_Agent_Architectures/AutoWebGLM_A_Large_Language_Model-based_Web_Navigating_Agent.pdf', '01_Core_Web_Agent_Architectures/GPT-4V(ision)_is_a_Generalist_Web_Agent_if_Grounded.pdf', '01_Core_Web_Agent_Architectures/Go-Browse_Training_Web_Agents_with_Structured_Exploration.pdf', '01_Core_Web_Agent_Architectures/LASER_LLM_Agent_with_State-Space_Exploration_for_Web_Navigation.pdf', '01_Core_Web_Agent_Architectures/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf', '01_Core_Web_Agent_Architectures/WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models.pdf', '02_Web_Agent_Benchmarks_Environments/BEARCUBS_A_benchmark_for_computer-using_web_agents.pdf', '02_Web_Agent_Benchmarks_Environments/BrowseComp_A_Simple_Yet_Challenging_Benchmark_for_Browsing_Agents.pdf', '02_Web_Agent_Benchmarks_Environments/MMInA_Benchmarking_Multihop_Multimodal_Internet_Agents.pdf', '02_Web_Agent_Benchmarks_Environments/Mind2Web_Towards_a_Generalist_Agent_for_the_Web.pdf', '02_Web_Agent_Benchmarks_Environments/The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf', '02_Web_Agent_Benchmarks_Environments/VisualWebArena_Evaluating_Multimodal_Agents_on_Realistic_Visual_Web_Tasks.pdf', '02_Web_Agent_Benchmarks_Environments/WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf', '02_Web_Agent_Benchmarks_Environments/WebLINX_Real-World_Website_Navigation_with_Multi-Turn_Dialogue.pdf', '02_Web_Agent_Benchmarks_Environments/WebShop_Towards_Scalable_Real-World_Web_Interaction_with_Grounded_Language_Agents.pdf', '02_Web_Agent_Benchmarks_Environments/WorkArena_How_Capable_are_WebAgents_at_Solving_Common_Knowledge_Work_Tasks.pdf', '02_Web_Agent_Benchmarks_Environments/WorkArena_Towards_Compositional_Planning_and_Reasoning-based_Common_Knowledge_Work_Tasks.pdf', '03_Agentic_Search_Scraping_Info_Seeking/AutoScraper_A_Progressive_Understanding_Web_Agent_for_Web_Scraper_Generation.pdf', '03_Agentic_Search_Scraping_Info_Seeking/Mind2Web_2_Evaluating_Agentic_Search_with_Agent-as-a-Judge.pdf', '03_Agentic_Search_Scraping_Info_Seeking/WebDancer_Towards_Autonomous_Information_Seeking_Agency.pdf', '03_Agentic_Search_Scraping_Info_Seeking/WebGPT_Browser-assisted_question-answering_with_human_feedback.pdf', '03_Agentic_Search_Scraping_Info_Seeking/WebSailor_Navigating_Super-human_Reasoning_for_Web_Agent.pdf', '03_Agentic_Search_Scraping_Info_Seeking/WebWalker_Benchmarking_LLMs_in_Web_Traversal.pdf', '03_Agentic_Search_Scraping_Info_Seeking/Webscraper_Leverage_Multimodal_Large_Language_Models_for_Index-Content_Web_Scraping.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AGENTFUZZER_Generic_Black-Box_Fuzzing_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AdvAgent_Controllable_Blackbox_Red-teaming_on_Web_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/AgentVigil_Generic_Black-Box_Red-teaming_for_Indirect_Prompt_Injection_against_LLM_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Attacking_Vision-Language_Computer_Agents_via_Pop-ups.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Commercial_LLM_Agents_Are_Already_Vulnerable_to_Simple_Yet_Dangerous_Attacks.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Dissecting_Adversarial_Robustness_of_Multimodal_LM_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/EIA_ENVIRONMENTAL_INJECTION_ATTACK_ON_GENERALIST_WEB_AGENTS_FOR_PRIVACY_LEAKAGE.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/How_Much_Can_We_Trust_LLM_Search_Agents_Measuring_Endorsement_Vulnerability_to_Web_Content_Manipulation.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Identifying_AI_Web_Scrapers_Using_Canary_Tokens.pdf', "04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Not_What_You've_Signed_Up_For_Compromising_Real-World_LLM-Integrated_Applications_with_Indirect_Prompt_Injection.pdf", '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/One_Polluted_Page_Is_Enough_Evaluating_Web_Content_Pollution_in_Generative_Recommenders.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Overcoming_the_Retrieval_Barrier_Indirect_Prompt_Injection_in_the_Wild_for_LLM_Systems.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Prompt_Injection_Attack_to_Tool_Selection_in_LLM_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/Unsafe_LLM-Based_Search_Quantitative_Analysis_and_Mitigation_of_Safety_Risks_in_AI_Web_Search.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/VPI-Bench_Visual_Prompt_Injection_Attacks_for_Computer-Use_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WAAA_Web_Adversaries_Against_Agentic_Browsers.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WebCloak_Characterizing_and_Mitigating_Threats_from_LLM-Driven_Web_Agents_as_Intelligent_Scrapers.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/WebInject_Prompt_Injection_Attack_to_Web_Agents.pdf', '04_Adversarial_Web_Prompt_Injection_Content_Manipulation/When_AI_Meets_the_Web_Prompt_Injection_Risks_in_Third-Party_AI_Chatbot_Plugins.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/AI_Agent_Traps.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/AgentLAB_Benchmarking_LLM_Agents_against_Long-Horizon_Attacks.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Breaking_Agents_Compromising_Autonomous_LLM_Agents_Through_Malfunction_Amplification.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Context_manipulation_attacks_Web_agents_are_susceptible_to_corrupted_memory.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Hidden_in_Memory_Sleeper_Memory_Poisoning_in_LLM_Agents.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/How_Adversarial_Environments_Mislead_Agentic_AI.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Its_a_TRAP_Task-Redirecting_Agent_Persuasion_Benchmark_for_Web_Agents.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web-Use_Agents.pdf', '05_Agentic_Traps_Persistence_Adaptive_Attacks/Mind_the_Web_The_Security_of_Web_Use_Agents.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/Autonomy_Comes_with_Costs_Detecting_Denial-of-Service_Vulnerabilities_Caused_by_Resource_Abusing_in_LLM-based_Agents.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/Beyond_Max_Tokens_Stealthy_Resource_Amplification_via_Tool_Calling_Chains_in_LLM_Agents.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/Denial_of_wallet_Defining_a_looming_threat_to_serverless_computing.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/Overthinking_Loops_in_Agents_A_Structural_Risk_via_MCP_Tools.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/RecurGuard_Runtime_Monitoring_for_Reasoning-Token_Consumption_Attacks.pdf', '06_Resource_Exhaustion_Availability_Denial_of_Wallet/When_Agents_Do_Not_Stop_Uncovering_Infinite_Agentic_Loops_in_LLM_Agents.pdf', '07_Security_Benchmarks_Evaluation/AgentDojo_A_Dynamic_Environment_to_Evaluate_Prompt_Injection_Attacks_and_Defenses_for_LLM_Agents.pdf', '07_Security_Benchmarks_Evaluation/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf', '07_Security_Benchmarks_Evaluation/Indirect_Prompt_Injections_Are_Firewalls_All_You_Need_or_Stronger_Benchmarks.pdf', '07_Security_Benchmarks_Evaluation/ST-WebAgentBench_A_Benchmark_for_Evaluating_Safety_and_Trustworthiness_in_Web_Agents.pdf', '07_Security_Benchmarks_Evaluation/SafeArena_Evaluating_the_Safety_of_Autonomous_Web_Agents.pdf', '07_Security_Benchmarks_Evaluation/SecureWebArena_A_Holistic_Security_Evaluation_Benchmark_for_LVLM-based_Web_Agents.pdf', '07_Security_Benchmarks_Evaluation/WASP_Benchmarking_Web_Agent_Security_Against_Prompt_Injection_Attacks.pdf', '08_Defenses_Guards_Containment/ACE_A_Security_Architecture_for_LLM-Integrated_App_Systems.pdf', '08_Defenses_Guards_Containment/Attention_is_All_You_Need_to_Defend_Against_Indirect_Prompt_Injection_Attacks_in_LLMs.pdf', '08_Defenses_Guards_Containment/BrowseSafe_Understanding_and_Preventing_Prompt_Injection_Within_AI_Browser_Agents.pdf', '08_Defenses_Guards_Containment/Defeating_Prompt_Injections_by_Design.pdf', '08_Defenses_Guards_Containment/Defending_Against_Indirect_Prompt_Injection_Attacks_With_Spotlighting.pdf', '08_Defenses_Guards_Containment/IsolateGPT_An_Execution_Isolation_Architecture_for_LLM-Based_Agentic_Systems.pdf', '08_Defenses_Guards_Containment/MELON_Provable_Defense_Against_Indirect_Prompt_Injection_Attacks_in_AI_Agents.pdf', '08_Defenses_Guards_Containment/PlanGuard_Defending_Agents_against_Indirect_Prompt_Injection_via_Planning-based_Consistency_Verification.pdf', '08_Defenses_Guards_Containment/Prismata_Confining_Cross-Site_Prompt_Injection_in_Web_Agents.pdf', '08_Defenses_Guards_Containment/SecAlign_Defending_Against_Prompt_Injection_with_Preference_Optimization.pdf', '08_Defenses_Guards_Containment/SnapGuard_Lightweight_Prompt_Injection_Detection_for_Screenshot-Based_Web_Agents.pdf', '08_Defenses_Guards_Containment/StruQ_Defending_Against_Prompt_Injection_with_Structured_Queries.pdf', '08_Defenses_Guards_Containment/The_Task_Shield_Enforcing_Task_Alignment_to_Defend_Against_Indirect_Prompt_Injection_in_LLM_Agents.pdf', '08_Defenses_Guards_Containment/Untrusted_Content_Masking_for_Web_Agents_with_Security_Guarantees.pdf', '08_Defenses_Guards_Containment/WARD_Adversarially_Robust_Defense_of_Web_Agents_Against_Prompt_Injections.pdf', '08_Defenses_Guards_Containment/WebAgentGuard_A_Reasoning-Driven_Guard_Model_for_Detecting_Prompt_Injection_Attacks_in_Web_Agents.pdf', '08_Defenses_Guards_Containment/ceLLMate_Sandboxing_Browser_AI_Agents.pdf', '09_Progress_Long_Horizon_Benign_Controls/AgentRewardBench_Evaluating_Automatic_Evaluations_of_Web_Agent_Trajectories.pdf', '09_Progress_Long_Horizon_Benign_Controls/An_Illusion_of_Progress_Assessing_the_Current_State_of_Web_Agents.pdf', '09_Progress_Long_Horizon_Benign_Controls/FocusAgent_Simple_Yet_Effective_Ways_of_Trimming_the_Large_Context_of_Web_Agents.pdf', '09_Progress_Long_Horizon_Benign_Controls/GUIDE_Interpretable_GUI_Agent_Evaluation_via_Hierarchical_Diagnosis.pdf', '09_Progress_Long_Horizon_Benign_Controls/Odysseys_Benchmarking_Web_Agents_on_Realistic_Long_Horizon_Tasks.pdf', '09_Progress_Long_Horizon_Benign_Controls/The_Long-Horizon_Task_Mirage_Diagnosing_Where_and_Why_Agentic_Systems_Break.pdf', '09_Progress_Long_Horizon_Benign_Controls/WebChoreArena_Evaluating_Web_Browsing_Agents_on_Realistic_Tedious_Web_Tasks.pdf', '10_Traditional_Crawling_Crawler_Traps/Detection_of_crawler_traps_formalization_and_implementation—defeating_protection_on_internet_and_on_the_TOR_network.pdf', '10_Traditional_Crawling_Crawler_Traps/IRLbot_Scaling_to_6_Billion_Pagesand_Beyond.pdf', '10_Traditional_Crawling_Crawler_Traps/Measuring_What_the_Crawler_Sees_Discovery_Curves_Core_Persistence_and_Shell_Dynamics_in_Longitudinal_Web_Crawls.pdf', '10_Traditional_Crawling_Crawler_Traps/The_Impact_of_Crawl_Policy_on_Web_Search_Effectiveness.pdf', '10_Traditional_Crawling_Crawler_Traps/Web_Crawling.pdf', '11_Surveys_Taxonomies_SoK/A_Survey_on_Autonomy-Induced_Security_Risks_in_Large_Model-Based_Agents.pdf', '11_Surveys_Taxonomies_SoK/A_Survey_on_Trustworthy_LLM_Agents_Threats_and_Countermeasures.pdf', '11_Surveys_Taxonomies_SoK/A_Systematic_Survey_of_Security_Threats_and_Defenses_in_LLM-Based_AI_Agents_A_Layered_Attack_Surface_Framework.pdf', '11_Surveys_Taxonomies_SoK/SoK_Attack_and_Defense_Landscape_of_Agentic_AI_Systems.pdf', '11_Surveys_Taxonomies_SoK/Talk_is_Not_Cheap_A_Taxonomy_and_Benchmark_Coverage_Audit_for_LLM_Attacks.pdf', '11_Surveys_Taxonomies_SoK/Toward_Secure_LLM_Agents_Threat_Surfaces_Attacks_Defenses_and_Evaluation.pdf', '12_Contextual_Borderline/AWE_Adaptive_Agents_for_Dynamic_Web_Penetration_Testing.pdf', '12_Contextual_Borderline/AndroidWorld_A_Dynamic_Benchmarking_Environment_for_Autonomous_Agents.pdf', '12_Contextual_Borderline/BackdoorAgent_A_Unified_Framework_for_Backdoor_Attacks_on_LLM-based_Agents.pdf', '12_Contextual_Borderline/Dont_Click_That_Teaching_Web_Agents_to_Resist_Deceptive_Interfaces.pdf', '12_Contextual_Borderline/DoomArena_A_framework_for_Testing_AI_Agents_Against_Evolving_Security_Threats.pdf', '12_Contextual_Borderline/EvoCrawl_Exploring_Web_Application_Code_and_State_using_Evolutionary_Search.pdf', '12_Contextual_Borderline/Gorilla_Large_Language_Model_Connected_with_Massive_APIs.pdf', '12_Contextual_Borderline/InjecAgent_Benchmarking_Indirect_Prompt_Injections_in_Tool-Integrated_Large_Language_Model_Agents.pdf', '12_Contextual_Borderline/SkillTrojan_Backdoor_Attacks_on_Skill-Based_Agent_Systems.pdf', '12_Contextual_Borderline/The_Hidden_Dangers_of_Browsing_AI_Agents.pdf', '12_Contextual_Borderline/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools.pdf', '12_Contextual_Borderline/YURASCANNER_Leveraging_LLMs_for_Task-driven_Web_App_Scanning.pdf', '99_Duplicates/Exact/AgentRewardBench_Evaluating_Automatic_Evaluations_of_Web_Agent_Trajectories.pdf', '99_Duplicates/Exact/Formalizing_and_Benchmarking_Prompt_Injection_Attacks_and_Defenses.pdf', '99_Duplicates/Exact/The_BrowserGym_Ecosystem_for_Web_Agent_Research.pdf', '99_Duplicates/Exact/The_Long-Horizon_Task_Mirage_Diagnosing_Where_and_Why_Agentic_Systems_Break.pdf', '99_Duplicates/Exact/WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H01/source.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H02/source.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H03/source.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H04/source.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H05/source.pdf', 'analysis/phase4_rehearsal/private_source_material/holdout_sources/H06/source.pdf', 'analysis/phase4b_resumed_validation/private_source_material/B02/source.pdf', 'analysis/phase4b_validation/private_source_material/B01/source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_4f_yzfv7/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_4t9_snno/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_51alpp3q/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_9eft7ee9/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity__qonfnrg/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_b8q7cnqy/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_djj3rwt3/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_en992ph1/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_gmsu7rhe/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_i9u0e1yi/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_irlz7xvd/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_j480q_a1/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_jxxkhkj2/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_nr73syv9/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_o22qon5j/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_p70fl3p_/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_pnsc7e_z/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_qdnnhn6e/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_sb8ai9uc/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_tvpf6niz/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_wsz_gl0w/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/science_integrity_z7imq48p/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_3z52xzlg/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_7yurmel6/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity__pnlcrg1/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_bf_xn_fl/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_j74k3svx/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_j8o13sia/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_k6bqljb4/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_vrd9j6v3/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4be_freeze_repair_and_validation/NEVER_PACKAGE/synthetic_science_integrity/science_integrity_wuogy62h/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf', 'analysis/phase4br_remediation/private_source_material/original_phase4b/private_source_material/B01/source.pdf']]
    canonical = [p for p in all_pdfs if "99_Duplicates" not in p.relative_to(ROOT).parts]
    duplicates = [p for p in all_pdfs if p not in canonical]
    mapped = [resolve(row["Pdf"]) for row in manifest]
    for path in set(canonical) - set(mapped):
        issues.append(f"Unmapped PDF: {relative(path)}")
    for key in ("Pdf", "SummaryName", "StageTarget", "FinalTarget"):
        for value, count in Counter(r[key].casefold() for r in manifest).items():
            if count > 1:
                issues.append(f"Manifest collision in {key}: {value}")
    baseline_path = STATE / "baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else None
    if baseline and baseline["prompt_sha256"] != prompt_hash:
        issues.append("Saved prompt changed since recovery; review generation and approval provenance")
    staged_paths = {resolve(row["StageTarget"]) for row in manifest}
    for path in (ROOT / ".summary_v2").glob("*.md"):
        if path.resolve() not in staged_paths:
            issues.append(f"Unmapped staged draft: {relative(path)}")
    records = []
    for row in manifest:
        source, draft, final = (resolve(row[key]) for key in ("Pdf", "StageTarget", "FinalTarget"))
        source_hash, draft_hash, final_hash = map(digest, (source, draft, final))
        structure = check_structure(draft)
        status = "pending" if draft_hash is None else "structural_pass" if structure["passed"] else "needs_repair"
        if not source_hash:
            issues.append(f"Missing source: {row['Pdf']}")
        review = reviews.get(row["SummaryName"], {})
        reviewed = bool(source_hash and draft_hash and structure["passed"] and
                        review.get("source_sha256") == source_hash and
                        review.get("prompt_sha256") == prompt_hash and
                        review.get("draft_sha256") == draft_hash and
                        review.get("reviewed_at") and review.get("notes_path") and
                        resolve(review["notes_path"]).is_file())
        if reviewed:
            status = "promoted" if final_hash == draft_hash else "source_verified"
        if baseline:
            prior = baseline["papers"].get(row["SummaryName"], {})
            if prior and prior["source_sha256"] != source_hash:
                issues.append(f"Source changed since recovery: {row['SummaryName']}")
        run_file = STATE / "evidence" / Path(row["SummaryName"]).stem / "run.json"
        run = json.loads(run_file.read_text(encoding="utf-8-sig")) if run_file.exists() else None
        records.append({**row, "status": status, "source_sha256": source_hash,
                        "prompt_sha256": prompt_hash, "draft_sha256": draft_hash,
                        "final_sha256": final_hash, "structure": structure,
                        "source_review_valid": reviewed,
                        "last_generation": run,
                        "generation_provenance": "see evidence; hashes observed now do not prove original generation inputs"})
    duplicate_records = []
    source_hashes = {r["source_sha256"] for r in records if r["source_sha256"]}
    for path in duplicates:
        sha = digest(path)
        duplicate_records.append({"path": relative(path), "sha256": sha,
                                  "matches_canonical": sha in source_hashes})
        if sha not in source_hashes:
            issues.append(f"Archived PDF has no canonical hash match: {relative(path)}")
    counts = dict(Counter(r["status"] for r in records))
    snapshot = {"schema_version": 1, "updated_at": now, "prompt_sha256": prompt_hash,
                "usage_plan_remaining": None, "concurrency_default": 1, "batch_size": 2,
                "canonical_pdf_count": len(canonical), "total_pdf_count": len(all_pdfs),
                "counts": counts, "issues": issues, "duplicates": duplicate_records,
                "orphan_candidate_directories": [p.name for p in ROOT.glob(".summary_work_*") if p.is_dir()],
                "papers": records}
    if baseline is None:
        write_json(baseline_path, {"created_at": now, "prompt_sha256": prompt_hash,
                                  "papers": {r["SummaryName"]: {k: r[k] for k in
                                    ("source_sha256", "draft_sha256", "final_sha256")}
                                             for r in records}})
    write_json(OUTPUT / "checkpoint.json", snapshot)
    lines = ["# Analysis Checkpoint", "", f"Updated: {now}", "",
             f"Corpus: {len(canonical)} canonical PDFs; {len(duplicates)} archived duplicates.",
             f"Saved prompt SHA256: `{prompt_hash}`", "",
             "## Progress", "", "| Status | Papers |", "|---|---:|"]
    lines.extend(f"| {status} | {counts.get(status, 0)} |" for status in
                 ("pending", "needs_repair", "structural_pass", "source_verified", "promoted"))
    lines += ["", "Structural passes are unreviewed drafts. No scientific accuracy or complete",
              "visual coverage is implied. Existing older summaries remain in Summaries/.", "",
              "## Recovery", "", "Read [WORKFLOW.md](WORKFLOW.md). Refresh with `python scripts/summary_state.py`.",
              "Usage allowance is unknown. User preference: two papers per batch, run sequentially; checkpoint each paper.",
              "Inspect process command lines before treating scratch directories as abandoned.", "",
              "## Next Pending Papers", ""]
    lines += [f"- `{r['SummaryName']}`: `{r['Pdf']}`" for r in records if r["status"] == "pending"][:5]
    lines += ["", "## Issues", ""] + ([f"- {issue}" for issue in issues] or ["No corpus mapping or duplicate-hash issues detected."])
    runs = [r for r in records if r["last_generation"]]
    lines += ["", "## Recorded Runs", ""]
    lines += [f"- `{r['SummaryName']}`: {r['last_generation']['status']}. "
              "See its evidence directory for the log; running status can be stale after a crash."
              for r in runs] or ["No runs recorded by the durable runner yet."]
    lines += ["", "## All Papers", "", "| Paper / Filename | State |", "|---|---|"]
    lines += [f"| {r['SummaryName']} | {r['status']} |" for r in records]
    temp = OUTPUT / "CHECKPOINT.md.tmp"
    temp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    temp.replace(OUTPUT / "CHECKPOINT.md")
    print(json.dumps({"counts": counts, "issues": issues}, indent=2))


if __name__ == "__main__":
    main()
