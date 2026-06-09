---
title: "Claude Mythos"
kind: entity
aliases: ["Mythos", "Claude Mythos Preview", "Anthropic Mythos"]
sources: ["[[claude-mythos-preview-d737ab91]]", "[[anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public-11ba8929]]", "[[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]]", "[[expanding-project-glasswing-fd9b87df]]", "[[anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries-44fd313c]]"]
last_updated: 2026-06-09
last_verified: 2026-06-09
freshness_window_days: 30
input_cost_per_mtoken: 25.00
output_cost_per_mtoken: 125.00
cost_source: "[[anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public-11ba8929]]"
aa_intelligence_index: null
aa_intelligence_index_source: null
gdpval_aa_elo: null
gdpval_aa_elo_source: null
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

## Disputes

- [[claude-mythos-preview-d737ab91]] reports Mythos as state-of-the-art at SWE-bench Verified (93.9%), but this was a vendor-reported single-shot benchmark on an invitation-only model — no independent third-party replication exists. Status: unresolved — independently unverifiable while access remains invitation-only.
- [[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]] reports Mythos CyberGym at 83.1% overall but 70.8% on Firefox-exploit production specifically vs Opus 4.8's 8.8% — the aggregate vs subset gap is striking and not explained in the source. Status: unresolved — the Firefox-exploit subset gap suggests Mythos has specific high-blast-radius capabilities that the aggregate score underweights.

## Open questions

- [ ] When Mythos reaches general availability, will it receive an independent AA Intelligence Index placement, and where will it rank relative to Opus 4.8 (61.4) on the aggregate index?
- [ ] Is Mythos a fine-tune of an existing Claude Opus base or a distinct architecture trained separately for cybersecurity capability?
- [ ] Does Mythos' Cybench 100% pass@1 saturation indicate the benchmark has been exhausted as a frontier-security signal, or is it evidence of genuine out-of-distribution generalization?
- [ ] Anthropic reports 10,000+ high/critical vulnerabilities found by Mythos in ~2 months of Glasswing operation [[expanding-project-glasswing-fd9b87df]]; what is the false-positive / non-reproducible rate, and is Anthropic publishing per-partner deduplication numbers?

## See also

- [[claude-opus-4.8]]
- [[frontier-models]]
