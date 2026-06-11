---
title: "Claude Fable 5"
kind: entity
sources: ["[[claude-fable-5-and-claude-mythos-5-e11fcea9]]", "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]", "[[claude-fable-5-the-first-public-mythos-class-model-672c92f6]]", "[[claude-fable-5-intelligence-performance-price-analysis-ceeaabf7]]"]
last_updated: 2026-06-11
last_verified: 2026-06-11
freshness_window_days: 30
input_cost_per_mtoken: 10.00
output_cost_per_mtoken: 50.00
cost_source: "[[claude-fable-5-and-claude-mythos-5-e11fcea9]]"
aa_intelligence_index: 64.9
aa_intelligence_index_source: "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]"
gdpval_aa_elo: 1932
gdpval_aa_elo_source: "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Claude Fable 5 is Anthropic's first publicly available Mythos-class model, released June 9, 2026 — positioned a tier above Claude Opus 4.8 [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. It debuted at #1 on the Artificial Analysis Intelligence Index at 64.9, roughly 5 points ahead of GPT-5.5 [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]. It also leads GDPval-AA at 1932 Elo and scores 80.3% on SWE-bench Pro — 11 points clear of Opus 4.8 (69.2%) and more than 20 points clear of GPT-5.5 (58.6%) [[claude-fable-5-the-first-public-mythos-class-model-672c92f6]]. Pricing is $10/$50 per Mtoken — exactly 2× Opus 4.8 — with the 90% input-token caching discount preserved [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. The model is available on the Claude API, AWS Bedrock, Vertex AI, and Microsoft Foundry; paid Claude subscribers got free access during June 9–22 in Claude Code via `/model fable`.

> Today, we are launching Claude Fable 5, a Mythos-class model that we've made safe for general use, with capabilities that exceed those of any model we've ever made generally available. Claude Fable 5 is priced at $10 per million input tokens and $50 per million output tokens.

> Claude Fable 5 takes the #1 position on the Artificial Analysis Intelligence Index, scoring 64.9 and setting the highest score on 5 of the 10 underlying benchmarks. Claude Fable 5 scores 1932 on GDPval-AA.

> On SWE-bench Pro, Fable 5 scores 80.3%, an 11-point lead over Opus 4.8 (69.2%) and more than 20 points ahead of GPT-5.5 (58.6%) and Gemini 3.1 Pro (54.2%).

Safety routing: queries in cybersecurity and biology domains are automatically routed to Opus 4.8 in the public Fable 5 deployment [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. The unrestricted underlying model — **Claude Mythos 5** — is available only to vetted cyberdefenders and infrastructure providers via Project Glasswing.

> For a small group of cyberdefenders and infrastructure providers, we are also launching Claude Mythos 5, the same underlying model as Fable 5 but with safeguards lifted in some areas.

## Open questions

- [ ] What is Fable 5's score on CyberGym and ARC-AGI-2 given the cyber/bio routing to Opus 4.8 — are those benchmarks even runnable on the public Fable 5 endpoint?
- [ ] Is the AA Intelligence Index score 64.9 (article text) or 65 (model card)? Reconciliation needed for the comparison page.

## See also

- [[frontier-models]]
- [[claude-opus-4.8]]
- [[claude-mythos-preview]]
