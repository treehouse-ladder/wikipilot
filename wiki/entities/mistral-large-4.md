---
title: "Mistral Large 4"
kind: entity
aliases: ["le Chonk", "Mistral Large 4 Preview"]
sources: ["[[introducing-mistral-large-4-6f131bbe]]", "[[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]"]
last_updated: 2026-10-07
last_verified: 2026-10-07
freshness_window_days: 60
input_cost_per_mtoken: 1.36
output_cost_per_mtoken: 4.18
cost_source: "[[introducing-mistral-large-4-6f131bbe]]"
aa_intelligence_index: 38
aa_intelligence_index_source: "[[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: 0.82
cybergym_source: "[[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]"
arc_agi_2: null
arc_agi_2_source: null
---

# Mistral Large 4

## Summary

**Mistral Large 4** (preview Oct 6, 2026) is Mistral AI's largest-ever model — a 1.05T-parameter natively multimodal MoE with 49B active parameters, a 1.6B-parameter vision encoder, and a 1M-token context window [[introducing-mistral-large-4-6f131bbe]]. Trained on 3,800 NVIDIA Grace Blackwell GPUs at Mistral's European datacenters on data spanning 160+ languages including all EU official languages, it represents the first European model to enter the near-frontier tier on the AA Intelligence Index.

It scores **38 on the AA Intelligence Index** — making France home to the most intelligent model outside the US and China [[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]. API pricing: $1.36/$4.18 per Mtoken (input/output). Open weights are announced for end-of-October 2026.

Key benchmark results: **CyberGym-E2E-AA 82%** (leads the near-frontier tier, ahead of MiMo-V2.6-Pro 79% and GPT-6 Luna max 78%), DeepSWE v1.1 61.7%, SWE-Atlas-QnA 59.4%, Coding Agent Index 49.8%. Output speed: 116.1 tok/s at 1.46s TTFT.

> Mistral Large 4 is a 1 trillion-parameter natively multimodal mixture-of-experts model (1.05T total, 49B active), nicknamed 'le Chonk'. Training used 3,800 NVIDIA Grace Blackwell GPUs at Mistral's European datacenters on data spanning more than 160 languages, including every official EU language. Weights will be released by the end of October 2026. [[introducing-mistral-large-4-6f131bbe]]

> Mistral Large 4 Preview scores 38 on the Artificial Analysis Intelligence Index, making France home to the most intelligent model outside the US and China. Its strongest results include CyberGym-E2E-AA at 82%, DeepSWE v1.1 at 61.7%, and a Coding Agent Index score of 49.8%. [[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]

## Open questions

- [ ] When Mistral Large 4 weights drop end-of-October, will the open-weight version maintain the preview's AA-38 score, or will there be a performance delta vs. the API preview?
- [ ] The CyberGym-E2E-AA lead (82%) is notable — is this a genuine capability advantage in cybersecurity reasoning, or an artifact of Mistral's multilingual/European-document training distribution?

## See also

- [[frontier-models]]
- [[introducing-mistral-large-4-6f131bbe]]
- [[mistral-has-released-mistral-large-4-making-france-home-to-the-most-intelligent-model-outside-the-us-and-china-ffd46d0a]]
