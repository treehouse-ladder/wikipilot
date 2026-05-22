---
title: "Muse Spark"
kind: entity
sources: ["[[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]"]
last_updated: "2026-05-22"
last_verified: "2026-05-22"
freshness_window_days: 30
---

## Summary

Muse Spark is Meta's first frontier-class model since Llama 4 Maverick (April 2025) and — notably — the first Meta model not released as open weights [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]. It scores 52 on the Artificial Analysis Intelligence Index, placing it in the top 5 models benchmarked, ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax-M2.7, and Grok 4.20, and behind Gemini 3.1 Pro Preview, GPT-5.4, and Claude Opus 4.6. The jump is dramatic relative to Meta's open-weight history: Llama 4 Maverick and Scout scored 18 and 13 respectively as non-reasoning models, so Muse Spark closes most of the frontier gap in a single release.

Muse Spark is a multimodal reasoning model that can process text, image, and speech input and generate text output [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]. It has a context window of 260k tokens. The model is not open source and is not yet accessible via an API, but Meta has shared they expect API access to come soon. Currently, Muse Spark is gated to Meta's first-party products: Meta AI, Facebook, Instagram, and Threads.

> Muse Spark scores 52 on the Artificial Analysis Intelligence Index, placing it within the top 5 models benchmarked. It sits ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax-M2.7, Grok 4.20 and behind Gemini 3.1 Pro Preview, GPT-5.4 and Claude Opus 4.6.

> It is the first frontier-class model from Meta since Llama 4 Maverick was released in April 2025, and notably the first Meta model that is not being released as open weights.

> Muse Spark essentially closes the gap to the frontier in a single release.

## Open questions

- [ ] Does Muse Spark's AA Index 52 hold on contamination-resistant benchmarks (SWE-bench Pro), or does Meta's single-release frontier jump look weaker on harder evals?
- [ ] Is Muse Spark a clean-room new architecture or a continuation/scale-up of the Llama line?
- [ ] What does Meta's pivot away from open weights with Muse Spark imply for the open/closed competitive balance going forward?
- [ ] When will API access become available, and what will the pricing structure be relative to other frontier models?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
