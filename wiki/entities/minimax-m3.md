---
title: "MiniMax M3"
kind: entity
sources:
  - "[[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]"
  - "[[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]]"
  - "[[minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks-96b02e45]]"
  - "[[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]"
  - "[[minimax-m3-intelligence-performance-price-analysis-418bc9a9]]"
last_updated: 2026-06-08
last_verified: 2026-06-08
freshness_window_days: 30
input_cost_per_mtoken: 0.60
output_cost_per_mtoken: 2.40
cost_source: "[[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]"
swe_bench_verified: null
swe_bench_verified_source: null
aa_intelligence_index: 55
aa_intelligence_index_source: "[[minimax-m3-intelligence-performance-price-analysis-418bc9a9]]"
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

MiniMax M3 received its independent Artificial Analysis Intelligence Index placement at 55 (Reasoning configuration) on June 2, 2026 — well above the 23 average for comparable models, edging the prior open-weights co-leaders Kimi K2.6 and MiMo-V2.5-Pro (both 54) and making M3 the new public-leaderboard open-weights #1 on AA Intelligence Index v4.0 [[minimax-m3-intelligence-performance-price-analysis-418bc9a9]]. AA notes two practical caveats for production use: M3 generated 91M tokens to complete the Intelligence Index battery (vs the 29M average — roughly 3x verbose) and runs at only 41 tokens/sec, 'notably slow' on the AA speed comparator.

> MiniMax-M3 (Reasoning) achieves a score of 55 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (averaging 23).

> At 41 tokens per second, MiniMax-M3 is notably slow.

> When evaluating the Intelligence Index, it generated 91M tokens, which is very verbose in comparison to the average of 29M.

AA's published price on the same listing is $0.30/$1.20 per Mtoken — half the $0.60/$2.40 the launch materials and OpenRouter listing reported. The discrepancy is unresolved (see Disputes).

> Pricing for MiniMax-M3 is $0.30 per 1M input tokens (somewhat expensive, average: $0.25) and $1.20 per 1M output tokens (somewhat expensive, average: $0.87).

## Disputes

- [[minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost-11226d25]] reports M3 SWE-Bench Pro 59.0% beating GPT-5.5 (58.6%), but [[minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks-96b02e45]] notes MiniMax ran the benchmark on its own infrastructure using agent scaffolding (Claude Code, Mini-SWE-Agent, Terminus) and no independent third-party replication exists at launch. Status: unresolved — vendor-reported parity claims pending independent verification.
- [[minimax-m3-intelligence-performance-price-analysis-418bc9a9]] reports M3 pricing at $0.30/$1.20 per Mtoken, while the existing source reports $0.60/$2.40 per Mtoken on MiniMax's official PayG plan at launch. Status: unresolved — could be a post-launch price cut, a tier mismatch (AA evaluating an AA-specific tier), or measurement of the ≤512K input bucket vs the 512K-1M bucket; flagged for re-verification when MiniMax publishes the technical report.

## Open questions

- [ ] When the open weights land on Hugging Face (~June 11, 2026), will independent SWE-Bench Pro replications confirm vendor-reported scores within the typical 2-4 point variance?
- [ ] Does MiniMax M3 score on the Artificial Analysis Intelligence Index — does it crack the 50+ tier shared by GPT-5.5 / Opus 4.8 / Gemini 3.1 Pro?
- [ ] Does the native multimodal computer-use capability + open weights + 1M context make M3 the new baseline for self-hosted agentic-coding harnesses (Cline, OpenHands) over DeepSeek V4-Pro?
- [ ] Does M3's 91M-token Intelligence Index verbosity [[minimax-m3-intelligence-performance-price-analysis-418bc9a9]] translate into a ~3x effective cost multiplier on long-horizon agentic-coding loops where output dominates?
- [ ] Does M3's 41 tok/s output speed [[minimax-m3-intelligence-performance-price-analysis-418bc9a9]] cap its viability as a parallel-subagent worker model under dynamic-workflow style harnesses?

## See also

- [[deepseek-v4]]
- [[claude-opus-4.8]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
