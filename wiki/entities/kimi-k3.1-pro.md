---
title: "Kimi K3.1 Pro"
kind: entity
aliases: ["kimi k3.1 pro", "Kimi-K3.1-Pro"]
sources: ["[[kimi-k3-1-pro-launches-at-4th-on-the-intelligence-index-and-will-lead-open-weights-models-c9f225d9]]", "[[kimi-k3-1-pro-intelligence-performance-price-analysis-fb7b4f33]]", "[[moonshotai-kimi-k3-1-pro-hugging-face-f4a904d0]]"]
last_updated: 2026-11-06
last_verified: 2026-11-06
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 10.00
cost_source: "[[kimi-k3-1-pro-intelligence-performance-price-analysis-fb7b4f33]]"
aa_intelligence_index: 55
aa_intelligence_index_source: "[[kimi-k3-1-pro-launches-at-4th-on-the-intelligence-index-and-will-lead-open-weights-models-c9f225d9]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# Kimi K3.1 Pro

## Summary

Moonshot AI's **Kimi K3.1 Pro** (launched 2026-10-23) is a 2.8-trillion-parameter Mixture-of-Experts model with **104B active parameters** that entered the Artificial Analysis Intelligence Index at **#4 with a score of 55**, trailing only Claude Opus 5.5 (max with fallback, 58), Claude Sonnet 5.5 (max with fallback, 56) and Muse Wonder Full (max, 56) — a +11-point gain over base Kimi K3 (max, 44) on the current index basis [[kimi-k3-1-pro-launches-at-4th-on-the-intelligence-index-and-will-lead-open-weights-models-c9f225d9]]. It is priced at **$2/$10 per Mtoken with $0.20 per Mtoken cache-hit input** at an estimated **$2.11 per Intelligence Index task** [[kimi-k3-1-pro-intelligence-performance-price-analysis-fb7b4f33]]. The model card confirms architecture: **93 layers, 896 experts with 16 selected per token**, 160K vocabulary, 1,048,576-token context, MoonViT-V2 vision encoder (401M parameters) for Image-Text-to-Text, and MXFP4/MXFP8 quantization-aware training [[moonshotai-kimi-k3-1-pro-hugging-face-f4a904d0]]. As of 2026-11-06 the **weights are published on Hugging Face** at `moonshotai/Kimi-K3.1-Pro` under the **Kimi K3.1 Pro License** — restrictive rather than fully open: deployments with >100M MAU or >$20M monthly revenue must display 'Kimi K3.1-Pro' in the UI, and MaaS access (inference/fine-tuning via API to third parties) requires a separate Moonshot AI agreement [[moonshotai-kimi-k3-1-pro-hugging-face-f4a904d0]]. The MaaS restriction places K3.1 Pro in a more restrictive tier than the MIT-licensed GLM-5.3 or the Modified-MIT-licensed Kimi K3.

> Kimi K3.1 Pro scores 55 on the Artificial Analysis Intelligence Index, placing fourth overall, trailing only Claude Opus 5.5 (max with fallback, 58), Claude Sonnet 5.5 (max with fallback, 56) and Muse Wonder Full (max, 56). This is an 11-point gain over Kimi K3 (max, 44). Kimi K3.1 Pro has 2.8 trillion total parameters with 104 billion active parameters. Weights are not yet published; Moonshot is expected to release them soon after launch. Once the weights are released, Kimi K3.1 Pro will be the highest-scoring open weights model. [[kimi-k3-1-pro-launches-at-4th-on-the-intelligence-index-and-will-lead-open-weights-models-c9f225d9]]

> Pricing for Kimi K3.1 Pro is $2 per 1M input tokens and $10 per 1M output tokens, with cache hits at $0.20 per 1M tokens. The estimated cost to run the Artificial Analysis Intelligence Index is $2.11 per task. [[kimi-k3-1-pro-intelligence-performance-price-analysis-fb7b4f33]]

> Kimi K3.1 Pro is an open-weight, natively multimodal agentic model, and our most capable 3T-class model to date. With a 1-million-token context window, Kimi K3.1 Pro delivers substantial improvements in coding, 3D creation, financial research, factual accuracy, and other agentic capabilities. [[moonshotai-kimi-k3-1-pro-hugging-face-f4a904d0]]

## Disputes

## Open questions

- [x] When do Kimi K3.1 Pro's open weights land, and under what license? **Resolved 2026-11-06**: weights published on Hugging Face at `moonshotai/Kimi-K3.1-Pro` under the Kimi K3.1 Pro License — restrictive for MaaS and large commercial use, not Modified MIT [[moonshotai-kimi-k3-1-pro-hugging-face-f4a904d0]].
- [ ] What are Kimi K3.1 Pro's SWE-bench Pro and AA Coding Agent Index placements? Only the aggregate AA Intelligence Index (55) was reported. [[kimi-k3-1-pro-launches-at-4th-on-the-intelligence-index-and-will-lead-open-weights-models-c9f225d9]]

## See also

- [[kimi-k3]]
- [[claude-opus-5.5]]
- [[claude-sonnet-5.5]]
- [[frontier-models]]
