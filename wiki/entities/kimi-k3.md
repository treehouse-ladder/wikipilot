---
title: "Kimi K3"
kind: entity
sources: ["[[kimi-k3-intelligence-performance-price-analysis-5d65f998]]", "[[kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5-bce8423e]]", "[[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]]", "[[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]]"]
last_updated: 2026-07-24
last_verified: 2026-07-24
freshness_window_days: 30
input_cost_per_mtoken: 3.00
output_cost_per_mtoken: 15.00
cost_source: "[[kimi-k3-intelligence-performance-price-analysis-5d65f998]]"
aa_intelligence_index: 57
aa_intelligence_index_source: "[[kimi-k3-intelligence-performance-price-analysis-5d65f998]]"
gdpval_aa_elo: 1668
gdpval_aa_elo_source: "[[kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5-bce8423e]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Kimi K3 is Moonshot AI's proprietary closed frontier model, debuting at **AA Intelligence Index v4.1 = 57** — currently ranked 4th overall, behind Claude Fable 5 (60), GPT-5.6 Sol (max) (59), and GPT-5.6 Sol (xhigh) (58), and **one point above Claude Opus 4.8 (56)** [[kimi-k3-intelligence-performance-price-analysis-5d65f998]].

> Kimi K3 ranks 4th on the Artificial Analysis Intelligence Index at 57, behind Claude Fable 5 (60), GPT-5.6 Sol (max) (59), and GPT-5.6 Sol (xhigh) (58). [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]

Kimi K3 has **2.8 trillion parameters** with a **1M-token context window**, designed for frontier-intelligence scenarios including software engineering, knowledge work, and deep reasoning [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]. The model weights are not publicly available.

**Open-weights status (updated 2026-07-24):** Kimi K3 is not a permanently closed model. Moonshot AI committed to releasing the full 2.8-trillion-parameter weights on Hugging Face on **July 27, 2026** under a **Modified MIT license** (the same license used by K2.6 and K2.7-Code), which would make it the **leading open-weights model** by a wide margin over GLM-5.2 (AA Intelligence Index v4.1 = 51) and DeepSeek V4-Pro (44) [[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]] [[kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5-bce8423e]]. Moonshot's first-party tech blog describes it as "the world's first open 3T-class model" [[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]]. The earlier "proprietary closed / weights not publicly available" framing is therefore time-bound to the July 16–26 API-only launch window.

> Kimi K3 is the world's first open 3T-class model — frontier performance across coding, knowledge work, and reasoning, with native multimodality and 1M context. [[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]]

**Architecture (first-party — resolves the dense-vs-MoE open question):** Kimi K3 is a **Mixture-of-Experts** model that activates **16 of 896 experts (~50B active parameters)** per token via a Stable LatentMoE framework, built on two new components — **Kimi Delta Attention (KDA)**, a gated delta-rule linear-attention variant that swaps scalar forgetting for channel-wise forgetting, and **Attention Residuals (AttnRes)** — together yielding an ~**2.5x improvement in scaling efficiency vs Kimi K2** [[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]].

> Kimi K3 has scaled up Mixture of Experts (MoE) sparsity, effectively activating 16 out of 896 experts when paired with a Stable LatentMoE framework ... an approximate 2.5x improvement in overall scaling efficiency compared to Kimi K2. [[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]]

**Self-hosting barrier:** the released weights total ~**1.4TB** (≈594GB in BF16), with community GGUF Q4 quantizations expected to reduce this to ~300–400GB — a material infrastructure hurdle that partly offsets the open-weights advantage for smaller shops [[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]].

> Kimi K3's open weights arrive July 27. The catch is 1.4TB ... The model is reported at approximately 594 GB in BF16 format, with community GGUF quantizations (Q4) likely reducing this to 300–400 GB. [[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]]

> Kimi K3 has 2.8 trillion parameters. It features a 1M-token context window and is designed for frontier intelligence scenarios such as software engineering, knowledge work, and deep reasoning. [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]

Pricing via the Kimi API is **$3.00 per 1M input tokens** and **$15.00 per 1M output tokens** — matching Claude Sonnet 5's post-introductory cost tier and priced at 0.3× Opus 4.8's $5/$25 rate for a model one index-point above it on the AA Intelligence Index [[kimi-k3-intelligence-performance-price-analysis-5d65f998]].

> Kimi K3 costs $3.00 per 1M input tokens and $15.00 per 1M output tokens (based on Kimi's API). [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]

A notable efficiency caveat: Kimi K3 generates an average of **130M tokens per Intelligence Index task** — more than **twice the average (63M)** — and runs at **62 tokens/sec**, slower than the 70 tok/sec mean [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]. This verbosity is a real cost multiplier on output-dominated agentic loops.

On the highest-weighted GDPval-AA v4.1 sub-evaluation, Kimi K3's **GDPval-AA v2 Elo is 1668** — placing it above Opus 4.8 (reported as 1600 in the same source) and below Fable 5 (1818), and translating to approximately **$0.94 per completed task** at the $3/$15 per Mtoken rate [[kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5-bce8423e]]. The same profile confirms native multimodal input support (text, images, documents) and approximately 21% fewer output tokens per task than Kimi K2.6.

> Kimi K3 achieves a GDPval-AA v2 Elo of 1668. [[kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5-bce8423e]]

> When evaluating the Intelligence Index, Kimi K3 generated 130M tokens, which is very verbose in comparison to the average of 63M. At 62 tokens per second, Kimi K3 is slower than average (70). [[kimi-k3-intelligence-performance-price-analysis-5d65f998]]

## Disputes

- [[kimi-k3-tech-blog-open-frontier-intelligence-0d83e2aa]] and [[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]] establish Kimi K3 as an open-weights model with full 2.8T weights scheduled for Hugging Face on July 27, 2026 under a Modified MIT license, whereas this page's Summary states Kimi K3 is Moonshot AI's proprietary closed frontier model whose weights are not publicly available. Status: unresolved — the open-weights commitment is firm but the weights had not physically landed as of 2026-07-24; the "closed" framing is superseded on the July 27 drop.

## Open questions

- [ ] Will Kimi K3's 2.8T weights land on Hugging Face on the scheduled July 27, 2026 date, and does the ~1.4TB (594GB BF16) footprint make self-hosting practical without GGUF Q4 (~300–400GB) quantization? [[kimi-k3-s-open-weights-arrive-july-27-the-catch-is-1-4tb-56e05201]]
- [ ] How does Kimi K3's verbosity (130M tokens per Intelligence Index task, 2× average) translate to per-completed-agentic-task cost vs Opus 4.8 at 56 (one index-point below but ~$5/$25)?

## See also

- [[frontier-models]] — topic landing page
- [[kimi-k2.6]] — prior Moonshot AI open-weights model
- [[benchmark-leaders]] — comparison table
- [[cost-comparison]] — model cost comparison
