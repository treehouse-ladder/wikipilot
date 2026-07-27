---
fetched_at: &id001 2026-07-27
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 67bfe96b770ed720c703af6ae06fed5f787e483136a2c27069d824ca22931975
sources: []
title: 'Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the
  Open Weights Mean for the Community'
topic: frontier-models
url: https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei
---

## Excerpts

> Moonshot AI publicly released Kimi K3 on July 16, 2026, with full open-source weights promised by July 27. At 2.8 trillion parameters, it is the first open-source model to reach the 3-trillion-parameter class.

> K3 employs quantization-aware training (QAT) starting from the supervised fine-tuning stage, not post-training quantization. This is a critical distinction — the model learns to compensate for quantization error during training, resulting in significantly less quality degradation.

> MXFP4 weights (Microscaling FP4): Each weight is stored in 4-bit floating point with per-block scaling factors. MXFP4 is supported natively by NVIDIA Blackwell GPUs and AMD MI400 accelerators, making deployment hardware-friendly.

> The MXFP4 weight format means the full 2.8T model requires approximately 1.4 TB of weight storage — substantially less than the ~5.6 TB that FP16 weights would demand. This brings self-hosting within reach of organizations with multi-node GPU clusters (e.g., 8-16 nodes of 8x H100/B200).

> Moonshot's own serving uses the Mooncake disaggregated inference infrastructure, which separates prefill and decode across different node pools and achieves a reported 90% cache hit rate on coding workloads. This architecture enables the aggressive cached input pricing of $0.30/MTok.

> K3 leads all models on SWE Marathon and Program Bench, suggesting particular strength in sustained coding sessions — consistent with the 1M-token context window enabling full-repository understanding.

> GDPval-AA v2: K3 1,687; Fable 5 Max 1,815; GPT-5.6 Sol Max 1,747.8; Opus 4.8 1,600.