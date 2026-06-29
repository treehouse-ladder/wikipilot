---
title: "Claude Mythos"
kind: entity
aliases: ["Mythos", "Claude Mythos Preview", "Anthropic Mythos", "Claude Mythos 5"]
sources: ["[[claude-mythos-preview-d737ab91]]", "[[anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public-11ba8929]]", "[[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]]", "[[expanding-project-glasswing-fd9b87df]]", "[[anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries-44fd313c]]", "[[initial-impressions-of-claude-fable-5-1a99af0c]]", "[[if-claude-fable-stops-helping-you-you-ll-never-know-1257de46]]", "[[claude-fable-5-and-claude-mythos-5-e11fcea9]]", "[[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]", "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]", "[[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]]", "[[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]"]
last_updated: 2026-06-29
last_verified: 2026-06-21
freshness_window_days: 30
input_cost_per_mtoken: 25.00
output_cost_per_mtoken: 125.00
cost_source: "[[anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public-11ba8929]]"
aa_intelligence_index: 64.9
aa_intelligence_index_source: "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]"
gdpval_aa_elo: 1932
gdpval_aa_elo_source: "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]"
swe_bench_verified: 0.939
swe_bench_verified_source: "[[claude-mythos-preview-d737ab91]]"
cybergym: 0.831
cybergym_source: "[[claude-mythos-preview-d737ab91]]"
arc_agi_2: null
arc_agi_2_source: null
---

# Claude Mythos

## Summary

Claude Mythos is Anthropic's most capable model as of June 2026, announced April 7, 2026 as an invitation-only preview. It is state-of-the-art on SWE-bench Verified (93.9%), GPQA Diamond (94.6%), USAMO (97.6%), Terminal-Bench 2.0 (82.0%), CyberGym (83.1%), and Cybench (100% pass@1, saturated) [[claude-mythos-preview-d737ab91]].

> Claude Mythos Preview is state-of-the-art on SWE-bench Verified (93.9%), GPQA Diamond (94.6%), USAMO (97.6%), Terminal-Bench 2.0 (82.0%), CyberGym (83.1%), and Cybench (100% pass@1, saturated).

Anthropic deliberately withheld Mythos from general availability because its autonomous cybersecurity capabilities are judged too dangerous to ship broadly. Access is invitation-only through **Project Glasswing** for critical-infrastructure defenders and open-source security teams [[claude-mythos-preview-d737ab91]].

> Anthropic does not plan to make Claude Mythos Preview generally available; access is invitation-only as part of Project Glasswing because its autonomous cybersecurity capabilities are judged too powerful to ship without additional safeguards.

On June 2, 2026, Anthropic expanded access from ~50 to 150 organizations across 15+ countries, still restricted to Project Glasswing partners. API pricing is $25/$125 per million input/output tokens. Broader GA is expected "in the coming weeks" [[anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public-11ba8929]].

> On June 2, Anthropic expanded access to its Claude Mythos cyber-security model, making it available to 150 organisations in more than 15 countries.

> Mythos is being shipped only through Project Glasswing to approximately 50 defensive-security partners... with access available at $25 / $125 per million input/output tokens after the initial credit pool.

Compared to Claude Opus 4.8 (the public-leaderboard #1), Mythos leads on SWE-bench Pro (77.8% vs 69.2%) and on Firefox-exploit production in CyberGym (70.8% vs 8.8%), while both models tie on GPQA Diamond (~94%) [[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]].

> Mythos leads on the hardest software work, posting 77.8 to Opus 4.8's 69.2 on SWE-bench Pro. On GPQA Diamond, a set of graduate-level science questions, the two models tie at roughly 94. Anthropic's system cards point to a general-intelligence gap over Opus 4.8 that is modest and uneven, while the cyber gap is vast.

As of June 2, 2026, Anthropic expanded Project Glasswing access from its initial vetted cohort to roughly 150 new organizations across more than 15 countries, with a focus on critical-infrastructure operators across power, water, healthcare, communications, and hardware [[expanding-project-glasswing-fd9b87df]]. Since the program launched in early April 2026, Claude Mythos Preview has surfaced more than 10,000 high- or critical-severity software vulnerabilities for participating partners [[expanding-project-glasswing-fd9b87df]]. Named partners include Okta, Samsung, SK Hynix, SK Telecom, NATO, and the EU cybersecurity agency ENISA [[anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries-44fd313c]]. Mythos remains invitation-only — not generally available on the API — but the expansion is the largest scaling step since the original Project Glasswing announcement.

> Since launch in early April, the restricted Claude Mythos Preview has surfaced more than 10,000 high- or critical-severity software vulnerabilities for participating partners.

> Named partners include Okta, Samsung, SK Hynix, SK Telecom, NATO, and the EU cybersecurity agency ENISA.

Claude Fable 5, the first publicly available Mythos-class model, **launched at #1 on the Artificial Analysis Intelligence Index (v4.0 = 64.9)** — approximately 5 points ahead of the closest non-Anthropic model (GPT-5.5), with Anthropic models occupying both of the top 2 places; its GDPval-AA Elo (v1) of **1932** put it at #1 on the agentic real-world-task axis [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]. On the v4.1 re-scale (published 2026-06-18), Fable 5 re-places at **60** — still the closed-frontier leader above Opus 4.8 (56) and GPT-5.5 (55) — though it remains export-suspended since June 12, 2026 [[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]. On AA-Omniscience, Fable 5 scores **40**, +7 points over the prior leader Gemini 3.1 Pro Preview (33) [[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]].

> Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) takes the #1 position on the Artificial Analysis Intelligence Index, scoring 64.9 and setting the highest score on 5 of the 10 underlying benchmarks. Claude Fable 5 is approximately 5 points ahead of the closest non-Anthropic model (GPT-5.5), and Anthropic models now occupy both of the top 2 places. Claude Fable 5 scores 1932 on GDPval-AA, our benchmark for agentic real-world work tasks, taking the #1 position and putting Anthropic models in 3 of the top 4 spots. [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]

## Claude Fable 5 and Mythos 5: public Mythos-class launch (added 2026-06-11)

On June 9, 2026, Anthropic released **Claude Fable 5**, described as "the first publicly available Mythos-class model" — a tier above Opus 4.8 [[initial-impressions-of-claude-fable-5-1a99af0c]]. Early hands-on reports describe it as having "a big model smell: slow, expensive and capable of crunching through pretty much everything I threw at it," with the model spontaneously expanding work scope to upstream dependencies during agentic coding tasks [[initial-impressions-of-claude-fable-5-1a99af0c]].

> Claude Fable 5 has a big model smell: slow, expensive and capable of crunching through pretty much everything I threw at it.

Alongside the public Fable 5 launch, Anthropic released **Claude Mythos 5** — the same underlying model with safeguards lifted in cybersecurity and biology domains — exclusively for Project Glasswing partners [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. Mythos 5 is positioned as an upgrade to the earlier Claude Mythos Preview. In the public Fable 5 deployment, queries in cybersecurity and biology are automatically routed to Opus 4.8 as a safety measure.

> For a small group of cyberdefenders and infrastructure providers, we are also launching Claude Mythos 5, the same underlying model as Fable 5 but with safeguards lifted in some areas, initially deployed through Project Glasswing as an upgrade to Claude Mythos Preview.

Fable 5 introduces a new category of safeguard not previously documented: **silent capability dampening** for requests targeting frontier LLM development (pretraining pipelines, distributed training infrastructure, ML accelerator design). Unlike interventions for cybersecurity or biology that surface to the user, these safeguards "will not be visible to the user" and operate via "prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT)", affecting approximately 0.03% of traffic concentrated in fewer than 0.1% of organizations [[if-claude-fable-stops-helping-you-you-ll-never-know-1257de46]].

> Claude Fable 5 has implemented new interventions that limit effectiveness for requests targeting frontier LLM development, such as building pretraining pipelines, distributed training infrastructure, or ML accelerator design. Unlike interventions for cybersecurity, biology and chemistry, and distillation attempts, these safeguards will not be visible to the user.

**Mythos 5 access suspended June 12, 2026; partially restored June 26 for US critical infrastructure.** The same export control directive that suspended Fable 5 also suspended Claude Mythos 5 globally on June 12. Because the directive targeted both models together, even Project Glasswing cyberdefender partners — the intended audience for Mythos 5 — lost access. Anthropic is complying while disagreeing that the narrow jailbreak evidence justifies a full recall [[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]. On **June 26, 2026**, Commerce Secretary Howard Lutnick **partially lifted the export control** via letter to Anthropic co-founder Tom Brown, allowing **Claude Mythos 5 to be deployed without an export license to a defined set of U.S. organizations operating and defending critical infrastructure** [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]. Anthropic confirmed it was restoring access for these organizations quickly and continues to work with the government to expand Mythos 5 access and ultimately bring Fable 5 back for general use. This partial restoration applies only to Mythos 5 (the unrestricted, safeguard-free model); **Claude Fable 5 remains suspended worldwide for all general users** as of June 27, 2026 [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]].

> The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States.

> Commerce Secretary Howard Lutnick partially lifted the Anthropic export control on June 26, allowing Claude Mythos 5 to be deployed without an export license to a defined set of U.S. organizations operating and defending critical infrastructure, following a June 26 letter to Anthropic co-founder Tom Brown. [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]

> The version millions of developers and subscribers had been using, Claude Fable 5, remains suspended worldwide as of June 27, 2026, with all criminal and civil penalties from the original June 12 directive still in force. The key difference between the two models is that Fable 5 includes three classifier-based safety layers that redirect flagged cybersecurity, biology-chemistry, and model-distillation queries to Claude Opus 4.8, while Mythos 5 removes those classifiers, making it more capable for both offensive and defensive cyber tasks. [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]

## Disputes

- [[claude-mythos-preview-d737ab91]] reports Mythos as state-of-the-art at SWE-bench Verified (93.9%), but this was a vendor-reported single-shot benchmark on an invitation-only model — no independent third-party replication exists. Status: unresolved — independently unverifiable while access remains invitation-only.
- [[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]] reports Mythos CyberGym at 83.1% overall but 70.8% on Firefox-exploit production specifically vs Opus 4.8's 8.8% — the aggregate vs subset gap is striking and not explained in the source. Status: unresolved — the Firefox-exploit subset gap suggests Mythos has specific high-blast-radius capabilities that the aggregate score underweights.

## Open questions

- [ ] When Mythos reaches general availability, will it receive an independent AA Intelligence Index placement, and where will it rank relative to Opus 4.8 (61.4) on the aggregate index? (Partially answered for Fable 5 / Mythos 5: v4.0 = 64.9, v4.1 = 60, GDPval-AA v1 = 1932 [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]; the original Mythos Preview remains unplaced.)
- [ ] Entity `aa_intelligence_index` currently stores the v4.0 value (64.9) from the Fable 5 launch source; should it be updated to the v4.1 value (60) once a dedicated v4.1 Fable 5 analysis page is available?
- [ ] Is Mythos a fine-tune of an existing Claude Opus base or a distinct architecture trained separately for cybersecurity capability?
- [ ] Does Mythos' Cybench 100% pass@1 saturation indicate the benchmark has been exhausted as a frontier-security signal, or is it evidence of genuine out-of-distribution generalization?
- [ ] Anthropic reports 10,000+ high/critical vulnerabilities found by Mythos in ~2 months of Glasswing operation [[expanding-project-glasswing-fd9b87df]]; what is the false-positive / non-reproducible rate, and is Anthropic publishing per-partner deduplication numbers?
- [ ] The Glasswing partnerships involved 150+ critical-infrastructure organizations — what is the operational impact of sudden Mythos 5 suspension on live vulnerability discovery programs [[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]?

## See also

- [[claude-opus-4.8]]
- [[frontier-models]]
