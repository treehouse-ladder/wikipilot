---
title: "Muse Spark Open"
kind: entity
sources: ["[[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]]", "[[meta-releases-muse-spark-open-says-it-is-most-capable-us-based-open-model-f8f922cc]]"]
last_updated: "2026-10-16"
last_verified: "2026-10-16"
freshness_window_days: 30
---

## Summary

Muse Spark Open is Meta's purpose-built open-weight model, released October 2026 under the Muse Model License (free for most commercial use) [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]]. With 816B total parameters and 42B active (sparse MoE), a 1M-token context window, and native multimodal input (text, image, video, audio), it is the largest-parameter open-weight model in Meta's history and Meta's entry into the US open-weights competitive race [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]].

Meta positions it as the "most capable US-built open-weight model," a plausible claim given the US open-weights field (Inkling, Nemotron-3 trail the Chinese leaders at GLM-5.3 60 and Kimi K3 57), but benchmarks are vendor-reported only — no independent AA Intelligence Index placement yet [[meta-releases-muse-spark-open-says-it-is-most-capable-us-based-open-model-f8f922cc]]. The model card notes it trails some closed Chinese models (Kimi K3, GLM-5.3) on Terminal-Bench 2.1 [[meta-releases-muse-spark-open-says-it-is-most-capable-us-based-open-model-f8f922cc]].

Meta explicitly distinguishes this from its closed frontier line: "We will generally not open-source our most powerful models, so Muse Wonder Full remains closed" — confirming Muse Spark Open is a purpose-built open-weight sibling to the closed Muse Wonder line, not a lagged or leaked version of the top-tier model [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]].

**Availability**: weights on HuggingFace, Amazon SageMaker AI, Google Cloud Model Garden; hosted APIs via Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, Together AI; runtime support for SGLang, vLLM, TensorRT-LLM, HF Transformers, Apple MLX, llama.cpp, Unsloth, with hardware optimizations for AMD, Apple, Intel, Nvidia [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]].

> Muse Spark Open is the most capable US-built open-weight model to date, built for coding and AI agents. [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]]

> The model has 816 billion total parameters with 42 billion active, a 1 million token context window, and native multimodal input across text, image, video, and audio. [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]]

> We will generally not open-source our most powerful models, so Muse Wonder Full remains closed. [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]]

> The model trails some closed Chinese models like Kimi K3 and GLM 5.3 on specific coding benchmarks such as Terminal-Bench 2.1. [[meta-releases-muse-spark-open-says-it-is-most-capable-us-based-open-model-f8f922cc]]

## See also
- [[muse-spark]] — Meta's closed frontier model line (Muse Spark 1.x series, superseded by Muse Wonder)
- [[frontier-models]] — frontier LLM landscape topic

## Disputes
- Benchmark independence: [[introducing-muse-spark-open-the-most-capable-us-open-weight-model-to-date-499fcbd0]] and [[meta-releases-muse-spark-open-says-it-is-most-capable-us-based-open-model-f8f922cc]] report benchmarks from Meta alone; the "most capable US-built open-weight" claim has no independent AA Intelligence Index corroboration yet. Status: unresolved — pending independent evaluation.

## Open questions
- [ ] What does Muse Spark Open score on the AA Intelligence Index once independently benchmarked? Does it surpass GLM-5.3 (60, MIT) and Kimi K3 (57) for released open-weights leadership?
- [ ] Does the Muse Model License "limited commercial terms" restrict use cases that matter for game developers or agents (e.g., fine-tuning for proprietary game data, commercial redistribution of derivative models)?
