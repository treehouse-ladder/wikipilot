---
title: "Gemini 4 Neon"
kind: entity
aliases: ["Neon", "gemini-4-neon", "Gemini 4 Neon (xhigh)"]
sources:
  - "[[introducing-gemini-4-neon-be0aed2f]]"
  - "[[gemini-4-neon-model-card-93dc5dee]]"
  - "[[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]]"
last_updated: 2026-11-19
last_verified: 2026-11-19
freshness_window_days: 14
input_cost_per_mtoken: 3.00
output_cost_per_mtoken: 15.00
cost_source: "[[introducing-gemini-4-neon-be0aed2f]]"
aa_intelligence_index: 61
aa_intelligence_index_source: "[[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

**Gemini 4 Neon** is Google DeepMind's mid-tier frontier model, launched 2026-11-19, positioned between Gemini 4 Carbon (long-horizon, $4/$20 per Mtoken) and Gemini 4 Hydrogen (fast everyday work) [[gemini-4-neon-model-card-93dc5dee]]. At xhigh effort it **scores 61 on the Artificial Analysis Intelligence Index**, ranking **#3 globally** (behind Claude Fable 5.2 at 65 and GPT-6.2 Astra at 62) and **#2 on the Vals Index** [[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]]. It also claims **#1 on Zapier AutomationBench and Andon Labs Vending-Bench 2** [[introducing-gemini-4-neon-be0aed2f]].

> Gemini 4 Neon ranks #3 overall on the Artificial Analysis Intelligence Index with a score of 61, and #2 on the Vals Index. It also reports #1 results on Zapier's AutomationBench and Andon Labs' Vending-Bench 2. [[introducing-gemini-4-neon-be0aed2f]]

**Pricing and context:** $3/$15 per Mtoken, **1M-token context window**, knowledge cutoff March 2026 [[introducing-gemini-4-neon-be0aed2f]]. At xhigh effort the average task cost is **$6.44 — ~17% cheaper than Gemini 4 Carbon** ($7.76/task); at low effort it is the **cheapest option at $0.75/task**; task time is ~21 min at xhigh vs ~36 min for Carbon [[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]].

> Gemini 4 Neon is priced at $3 per million input tokens and $15 per million output tokens, and costs $6.44 per Intelligence Index task on average, about 17% less than Gemini 4 Carbon. [[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]]

Effort-level scores: 60 (high), 55 (medium), 44 (low) [[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]]. Access is broad: Gemini API, Google AI Studio, Gemini for business, Google Antigravity (Pro/Ultra), Gemini app (Pro/Ultra) [[introducing-gemini-4-neon-be0aed2f]]. A **cyber-focused Fairwind Program variant** is being provided to trusted defenders (same program used for Gemini 4 Carbon's initial cyber-defender release) [[gemini-4-neon-model-card-93dc5dee]].

> Gemini 4 Neon sits between Gemini 4 Carbon, which handles the hardest long-horizon projects, and Gemini 4 Hydrogen, which handles fast everyday work. The stated knowledge cutoff is March 2026. [[gemini-4-neon-model-card-93dc5dee]]

**Note on aa_intelligence_index value:** The stored value of 61 is at the **xhigh** effort level on the AA Intelligence Index v5 basis. Lower effort levels: 60 (high), 55 (medium), 44 (low). Not directly comparable to v4.x-scale values on other pages until the wiki-wide backfill pass is complete.

## Disputes

- [[google-continues-to-accelerate-its-release-cadence-with-gemini-4-neon-61858885]] (Artificial Analysis) scores Gemini 4 Carbon at 60 (high) in the Neon comparison; [[gemini-4-carbon-is-the-new-1-on-the-artificial-analysis-intelligence-index-v5-53854855]] previously placed Carbon at 59 (High). The Carbon score change from 59 to 60 appears to reflect an index re-calibration or re-measurement — the two sources cannot be directly compared without knowing whether the index basis or effort level changed. Status: unresolved.

## Open questions

- [ ] The aa_intelligence_index stored here (61) is at xhigh effort — the same level where Gemini 4 Carbon was benchmarked at 60 (high) in the Neon analysis. Is this xhigh–xhigh comparison the right basis for the wiki's main `aa_intelligence_index` field, or should we store a canonical per-effort-level breakdown as a list?
- [ ] Do Zapier AutomationBench and Andon Labs Vending-Bench 2 have third-party methodology disclosures? Both are cited only from the Google product announcement [[introducing-gemini-4-neon-be0aed2f]]; corroboration pending.
- [ ] Does the Fairwind Program variant ship the same commercial pricing ($3/$15 per Mtoken) as the standard Neon model, or is it a separately-licensed cyber-focused deployment? [[gemini-4-neon-model-card-93dc5dee]] is silent on pricing for the Fairwind variant.

## See also

- [[gemini-4-carbon]] — longer-horizon predecessor in Google's Gemini 4 line
- [[gemini-4-hydrogen]] — faster everyday-work sibling in Google's Gemini 4 line
