---
title: "MiniMax M3"
kind: entity
sources:
  - "[[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]"
  - "[[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]]"
  - "[[minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks-96b02e45]]"
  - "[[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]"
last_updated: 2026-06-07
last_verified: 2026-06-07
freshness_window_days: 30
input_cost_per_mtoken: 0.60
output_cost_per_mtoken: 2.40
cost_source: "[[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]"
swe_bench_verified: null
swe_bench_verified_source: null
aa_intelligence_index: null
aa_intelligence_index_source: null
gdpval_aa_elo: null
gdpval_aa_elo_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# MiniMax M3

## Summary

MiniMax M3 is MiniMax's flagship open-weight frontier model, launched June 1, 2026 [[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]. It is the first open-weight model to combine frontier-tier coding, a 1M-token context window, and native multimodality (image + video input + computer use) in a single architecture [[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]. The architectural innovation is MiniMax Sparse Attention (MSA), delivering per-token compute at 1M context that is 1/20 that of MiniMax M2 [[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]].

> M3 reaches frontier capability on coding and agentic tasks, introduces the brand-new MSA (MiniMax Sparse Attention) supporting up to 1M context, and is a natively multimodal model.

> at a context length of 1 million, M3's per-token compute is just 1/20 that of the previous-generation model.

Vendor-reported benchmark headlines: 59.0% on SWE-Bench Pro (vs GPT-5.5 58.6%, Gemini 3.1 Pro 54.2%), 66.0% on Terminal-Bench 2.1, 83.52 on BrowseComp [[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]].

> MiniMax-M3 posts 59.0 on SWE-Bench Pro, 66.0 on Terminal Bench 2.1, 83.52 on BrowseComp, 74.2 on MCP Atlas, and 70.06 on OSWorld-Verified.

API pricing: $0.60/$2.40 per Mtoken (≤512K); $1.20/$4.80 for 512K-1M context [[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]. This makes M3 roughly 5-10% of the cost of GPT-5.5 ($5/$30) at vendor-claimed parity on SWE-Bench Pro [[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]].

> MiniMax-M3 costs $0.60 per million input tokens and $2.40 per million output tokens on the official Pay-as-You-Go plan.

Open weights and a technical report were promised within ~10 days of launch on Hugging Face and GitHub [[minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks-96b02e45]].

> Weights will be released within 10 days of launch. The API is live now. The model costs $0.60 per million input tokens.

## Disputes

- [[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]] reports M3 SWE-Bench Pro 59.0% beating GPT-5.5 (58.6%), but [[minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks-96b02e45]] notes MiniMax ran the benchmark on its own infrastructure using agent scaffolding (Claude Code, Mini-SWE-Agent, Terminus) and no independent third-party replication exists at launch. Status: unresolved — vendor-reported parity claims pending independent verification.

## Open questions

- [ ] When the open weights land on Hugging Face (~June 11, 2026), will independent SWE-Bench Pro replications confirm vendor-reported scores within the typical 2-4 point variance?
- [ ] Does MiniMax M3 score on the Artificial Analysis Intelligence Index — does it crack the 50+ tier shared by GPT-5.5 / Opus 4.8 / Gemini 3.1 Pro?
- [ ] Does the native multimodal computer-use capability + open weights + 1M context make M3 the new baseline for self-hosted agentic-coding harnesses (Cline, OpenHands) over DeepSeek V4-Pro?

## See also

- [[deepseek-v4]]
- [[claude-opus-4.8]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
