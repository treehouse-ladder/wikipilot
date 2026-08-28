---
title: "Qwen3.8-Flash-Next"
kind: entity
aliases: ["Qwen3.8 Flash Next", "qwen3.8-flash-next", "Qwen 3.8 Flash Next"]
sources: ["[[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]", "[[qwen-qwen3-8-flash-next-eb79656c]]"]
last_updated: 2026-08-28
last_verified: 2026-08-28
freshness_window_days: 30
input_cost_per_mtoken: 0.00
output_cost_per_mtoken: 0.00
cost_source: "[[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]"
aa_intelligence_index: 56
aa_intelligence_index_source: "[[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]"
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

**Qwen3.8-Flash-Next** is Alibaba's efficient open-weights model and an experimental preview of the **Qwen4 architecture**, released 2026-08-26 on Hugging Face [[qwen-qwen3-8-flash-next-eb79656c]]. It scores **56 on the Artificial Analysis Intelligence Index v4.1.1**, placing it "well above average among other open weight models of similar size (median: 28)" [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]].

> Qwen3.8-Flash-Next scores 56 on the Artificial Analysis Intelligence Index, placing it well above average among other open weight models of similar size (median: 28). [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]

The model is a **Mixture-of-Experts with 180B total / 6B active parameters** — the fewest active parameters of any model at AA II 56, making it the new **intelligence-per-active-param leader in the sub-20B-active open-weights segment** [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]. This compares favorably to GLM-5.3-Flash, which scores 57 with 18B active parameters (3× more active compute for ~1 more intelligence point).

> Qwen3.8-Flash-Next is a Mixture of Experts (MoE) model with 180 billion total parameters, but only 6 billion active parameters are used during inference. [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]

**Architecture — QSA (Qwen Sparse Attention):** The model introduces the Qwen4 architectural signature: **Gated DeltaNet + Qwen Sparse Attention (QSA)**. QSA operates at the **micro-block level** rather than the token level, reducing long-context KV-cache latency significantly compared to the Gated DeltaNet + Gated Attention pairing in the Qwen3.8 line [[qwen-qwen3-8-flash-next-eb79656c]].

> This experimental preview of the architecture that will underpin Qwen4 is built around a fundamental rethinking of how the core components of modern large language models (LLMs) interact at scale. [[qwen-qwen3-8-flash-next-eb79656c]]

> Hybrid Attention with QSA: The Gated DeltaNet and Gated Attention pairing has been reworked into Gated DeltaNet and Qwen Sparse Attention (QSA). Rather than selecting individual tokens for processing, QSA operates at the micro-block level. This cuts long-context latency significantly. [[qwen-qwen3-8-flash-next-eb79656c]]

**Context window:** 262,144 tokens natively, **extensible to 1,000,000 tokens**. Supports text, image, and video input [[qwen-qwen3-8-flash-next-eb79656c]].

> The model supports text, image, and video input, outputs text, and has a 256k tokens context window. [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]

> Context Length: 262,144 natively and extensible up to 1,000,000 tokens. [[qwen-qwen3-8-flash-next-eb79656c]]

**Verbosity caveat:** AA flags it as "faster than average, however very verbose" — a per-task cost multiplier on output-heavy agentic loops that offsets the low active-parameter inference cost [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]].

> Qwen3.8-Flash-Next is amongst the leading models in intelligence and well priced when comparing to other open weight models of similar size, and it's also faster than average, however very verbose. [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]

**Pricing:** Listed as $0.00 per Mtoken on artificialanalysis.ai as of 2026-08-28 — a preview placeholder; commercial pricing has not yet been announced [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]].

## Disputes

- [ ] Pricing at $0.00 per Mtoken is a placeholder, not a real commercial price. Status: unresolved — pending official Alibaba/Qwen pricing announcement.

## Open questions

- [ ] What pricing will Qwen3.8-Flash-Next carry once it exits preview? [[qwen3-8-flash-next-intelligence-performance-price-analysis-0ab95401]]
- [ ] Does QSA micro-block sparse attention yield measurable quality gains over pure-transformer or token-level sparse-attention at long contexts (256K–1M), or is the benefit primarily latency/KV-cache? [[qwen-qwen3-8-flash-next-eb79656c]]

## See also

- [[frontier-models]]
- [[benchmark-leaders]]
- [[cost-comparison]]
