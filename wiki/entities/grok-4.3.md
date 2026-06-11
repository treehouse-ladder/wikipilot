---
title: "Grok 4.3"
kind: entity
sources: ["[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]", "[[grok-build-0-1-on-api-c60c4a6b]]", "[[grok-imagine-1-5-preview-7668cc26]]", "[[grok-ai-new-model-triples-parameter-count-targets-coding-lead-release-expected-mid-june-083853d8]]", "[[grok-v9-rolls-into-tesla-cars-and-x-why-musk-s-distribution-flywheel-worries-ai-rivals-46ba11d8]]"]
last_updated: 2026-06-11
last_verified: 2026-06-09
freshness_window_days: 30
input_cost_per_mtoken: 1.25
output_cost_per_mtoken: 2.50
cost_source: "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]"
aa_intelligence_index: 53
aa_intelligence_index_source: "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]"
gdpval_aa_elo: 1500
gdpval_aa_elo_source: "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Grok 4.3 is xAI's frontier reasoning model, released April 30, 2026 [[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]. It is priced well below the reasoning-model median at $1.25/$2.50 per million input/output tokens, and scores 53 on the Artificial Analysis Intelligence Index. Grok 4.3's largest single-benchmark improvement was on GDPval-AA, where it scores 1,500 Elo — up 321 Elo from Grok 4.20 0309 v2's 1,179.

> Grok 4.3 (high) was released on April 30, 2026. Grok 4.3 (high) scores 53 on the Artificial Analysis Intelligence Index. The largest single benchmark improvement is on GDPval-AA, where Grok 4.3 scores an ELO of 1500, up 321 points from Grok 4.20 0309 v2's score of 1179. Grok 4.3 (high) costs $1.25 per 1M input tokens and $2.50 per 1M output tokens.

xAI's Grok 4.3 generation includes the dedicated coding model Grok Build 0.1 (public beta, xAI API, June 2026): 256k-token context, native MCP support, multimodal text+image, served at 100+ tokens/sec, priced at $1/$2 per Mtoken [[grok-build-0-1-on-api-c60c4a6b]]. Separately, Grok V9-Medium — a 1.5T-parameter (3x V8-small) base model trained on licensed Cursor session data — completed training on May 25, 2026, with public release projected for mid-June 2026 [[grok-ai-new-model-triples-parameter-count-targets-coding-lead-release-expected-mid-june-083853d8]]. In the multimodal generation lane, Grok Imagine 1.5 Preview debuted at #1 on the Artificial Analysis Video Arena Image-to-Video leaderboard at 1404 Elo with native synchronized audio and 15-second clips [[grok-imagine-1-5-preview-7668cc26]].

> Grok Build 0.1, xAI's fastest coding model, is now available via the xAI API in public beta. It is priced at $1 per million input tokens and $2 per million output tokens.

> Grok V9-Medium has completed training at 1.5 trillion parameters — three times the current production 0.5T V8-small model. It was trained on Cursor data.

> Grok Imagine 1.5 Preview debuted at number one on the Artificial Analysis Video Arena Image-to-Video leaderboard with an Elo rating of 1404.

**Update 2026-06-10**: xAI has begun rolling out Grok V9-Medium — the 1.5T-parameter successor to the Grok 4.3 generation — into Tesla vehicles and the X social network, ahead of a clean public API release [[grok-v9-rolls-into-tesla-cars-and-x-why-musk-s-distribution-flywheel-worries-ai-rivals-46ba11d8]]. Musk said V9-Medium completed training on June 5, 2026, three times the size of the production v8-small. Independent benchmarks have not yet landed.

> xAI has begun pushing Grok V9-Medium, its largest model yet, into Tesla's connected-car fleet and the X social network. Grok V9-Medium completed training on June 5, 2026 at 1.5 trillion parameters — about three times the size of the current v8-small production model.

_no contradictions or gaps known yet (last reviewed: 2026-06-09)_

## Open questions

- [ ] SWE-bench Verified, Cybench, and ARC-AGI-2 scores for Grok 4.3 — pending researcher sweep.
- [ ] Grok Build 0.1 published 100+ tok/sec and $1/$2 Mtoken pricing but xAI has not yet published a SWE-bench Verified or AA Intelligence Index score for the model itself [[grok-build-0-1-on-api-c60c4a6b]] — independent benchmarks pending.
- [ ] Does Grok V9-Medium replace Grok 4.3 on the xAI API, or run as a separate model? Pricing/capability comparison TBD pending public release.

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
