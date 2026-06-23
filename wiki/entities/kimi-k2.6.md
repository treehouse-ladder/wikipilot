---
title: "Kimi K2.6"
kind: entity
sources: ["[[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]", "[[multi-modal-model-kimi-k2-6-pricing-774b549a]]", "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]", "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]", "[[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]", "[[glm-5-1-intelligence-performance-price-analysis-fb6f086c]]", "[[kimi-k2-7-code-9c6b3767]]", "[[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]]"]
last_updated: 2026-06-23
last_verified: "2026-05-21"
freshness_window_days: 30
input_cost_per_mtoken: 0.95
output_cost_per_mtoken: 4.00
cost_source: "[[multi-modal-model-kimi-k2-6-pricing-774b549a]]"
aa_intelligence_index: 54
aa_intelligence_index_source: "[[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]"
gdpval_aa_elo: 1520
gdpval_aa_elo_source: "[[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]"
swe_bench_verified: 0.802
swe_bench_verified_source: "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]"
cybergym: 0.413
cybergym_source: "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]"
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Kimi K2.6 is Moonshot AI's frontier open-weights model. It scored 54 on the Artificial Analysis Intelligence Index on release (April 2026), placing it within 3 AA-Index points of the closed-frontier leader [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]. As of May 2026, Kimi K2.6 is co-tied at 54 with Xiaomi's MiMo-V2.5-Pro as the joint top open-weights model [[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]. Kimi K2.6 also scores 1,520 Elo on GDPval-AA — the highest open-weights GDPval-AA score recorded at its release.

> Moonshot's Kimi K2.6 is the new leading open weights model, landing at #4 on the Artificial Analysis Intelligence Index (54) behind only Anthropic, Google, and OpenAI (all 57). Kimi K2.6 achieves an Elo of 1520 on the GDPval-AA evaluation.

> Kimi K2.6 (54) and MiMo-V2.5-Pro (54) are tied as the top open weights models by Intelligence Index.

Moonshot's hosted Kimi K2.6 API is priced at $0.95 per million input tokens (cache miss) and $4.00 per million output tokens; cache-hit input drops to $0.16/M [[multi-modal-model-kimi-k2-6-pricing-774b549a]]. Context window is 262,144 tokens.

> Kimi K2.6 ... Input Price (Cache Hit) `$0.16` ... Input Price (Cache Miss) `$0.95` ... Output Price `$4.00` ... Context Window 262,144 tokens.

On [[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]] Kimi K2.6 scores 80.2% — the leading open-weights score on SWE-bench Verified, within 8.5 points of GPT-5.5. On [[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]] it scores only 41.3%, well behind the frontier closed models — suggesting Kimi K2.6's strengths are concentrated in generalist code/reasoning rather than adversarial cyber-security agentic tasks.

> Kimi K2.6 (80.2%, new open-weight) ties MiniMax M2.5.

> Kimi K2.6 ... 0.413 [CyberGym].

**Kimi K2.7 Code (released June 12, 2026)** is K2.6's direct successor for coding-specialist tasks — same 1T total / 32B active MoE architecture, retrained for long-horizon agentic coding [[kimi-k2-7-code-9c6b3767]]. Key benchmark improvements over K2.6: Kimi Code Bench v2 62.0 vs. 50.9 (+21.8%), MCP Atlas 76.0 vs. 69.4, MCP Mark Verified 81.1 vs. 72.8; ~30% fewer thinking tokens than K2.6. AA Intelligence Index v4.1: 42 (vs K2.6's 43) [[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]].

> With substantial improvements on real-world long-horizon coding tasks, it strengthens end-to-end task completion across complex software engineering workflows...reducing thinking-token usage by approximately 30% compared with Kimi K2.6. [[kimi-k2-7-code-9c6b3767]]

## Disputes

- [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]] calls Kimi K2.6 "the new leading open weights model" (sole #4 at AA Index 54, released April 20, 2026), but [[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]] reports MiMo-V2.5-Pro also at 54 (released April 22, 2026), creating a co-leadership tie. Status: unresolved — both models share the top open-weights position at 54; neither is the sole leader.

## Open questions

- [ ] ARC-AGI-2 score for Kimi K2.6 — not yet on the BenchLM ARC-AGI-2 leaderboard as of 2026-05-20.
- [ ] GLM-5.1 now edges Kimi K2.6 on Code Arena WebDev (1534 vs 1529 Elo) per [[glm-5-1-intelligence-performance-price-analysis-fb6f086c]] — does this hold across other agentic-coding benchmarks, or is Kimi K2.6's GDPval-AA 1520 Elo still representative of its agentic-task ceiling?

## See also

- [[frontier-models]]
- [[glm-5]]
- [[claude-opus-4.7]]
