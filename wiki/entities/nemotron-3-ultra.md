---
title: "NVIDIA Nemotron 3 Ultra"
kind: entity
aliases: ["Nemotron 3 Ultra", "nemotron-3-ultra", "NVIDIA Nemotron Ultra 550B"]
sources: ["[[nemotron-3-ultra-announced-high-speed-leading-us-open-weights-intelligence-81a38c83]]", "[[nemotron-3-ultra-launches-june-4-the-first-open-frontier-model-built-for-agents-302459f4]]", "[[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]"]
last_updated: 2026-07-16
last_verified: 2026-06-04
freshness_window_days: 30
aa_intelligence_index: 48
aa_intelligence_index_source: "[[nemotron-3-ultra-announced-high-speed-leading-us-open-weights-intelligence-81a38c83]]"
---

## Summary

NVIDIA Nemotron 3 Ultra is a 550B-parameter mixture-of-experts model (55B active per token) announced June 1, 2026 at Jensen Huang's Computex keynote [[nemotron-3-ultra-announced-high-speed-leading-us-open-weights-intelligence-81a38c83]]. As of July 16, 2026, it is superseded as the top-scoring US open-weights model by Thinking Machines' Inkling (v4.1 AA Index = 41 vs Nemotron 3 Ultra's v4.1 = 38), though Nemotron's v4.0 score of 48 was higher before the v4.1 re-scaling [[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]. Both trail the Chinese-led open-weights frontier (GLM-5.2 at v4.1 = 51).

> NVIDIA just announced the release of Nemotron 3 Ultra in Jensen Huang's Computex keynote: at 550B parameters (55B active), this is the largest Nemotron 3 model to date, and it is the most intelligent US open weights model.

The model's headline differentiator is throughput: 300+ tokens/second on a pre-release DeepInfra endpoint versus 50–100 tok/s for similarly-sized Chinese open-weights peers [[nemotron-3-ultra-announced-high-speed-leading-us-open-weights-intelligence-81a38c83]]. Ships in BF16 and NVFP4 quantization, GA June 4 2026 on Hugging Face, ModelScope, OpenRouter, and build.nvidia.com.

> On a pre-release DeepInfra endpoint, Nemotron 3 Ultra served over 300 tokens per second.

The GA launch is now confirmed on schedule [[nemotron-3-ultra-launches-june-4-the-first-open-frontier-model-built-for-agents-302459f4]]. The model is positioned as the first open frontier model purpose-built for agents, with up to 5x faster inference and up to 30% lower cost than open frontier models in its class.

> Nemotron 3 Ultra became available on June 4, 2026 on Hugging Face, ModelScope, OpenRouter, and build.nvidia.com.

## Open questions

- [ ] Does the 3-6x throughput advantage translate to lower wall-clock cost on long-horizon agentic benchmarks, or does the intelligence gap to Kimi K2.6 wash it out?
- [ ] What is the NVFP4-quantized AA Intelligence Index score vs the BF16 baseline of 48?
- [ ] What pricing have DeepInfra, OpenRouter, and NVIDIA NIM settled on at GA on June 4? (GA confirmed, specific pricing not yet published in available sources — pending follow-up.)

## See also

- [[frontier-models]]
