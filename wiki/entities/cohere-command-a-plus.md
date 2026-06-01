---
title: "Cohere Command A+"
kind: entity
aliases: ["Command A+", "command-a-plus", "Cohere Command A Plus"]
sources: ["[[introducing-command-a-94d80d08]]", "[[cohere-launches-open-weights-model-command-a-more-than-a-year-since-the-command-a-release-7a929ac1]]"]
last_updated: 2026-06-01
last_verified: 2026-06-01
freshness_window_days: 30
---

## Summary

Cohere Command A+ is a 218B-total / 25B-active sparse Mixture-of-Experts model released May 20, 2026 under the Apache 2.0 license — Cohere's first fully Apache-2.0-licensed open-weights model, ending the CC-BY-NC commercial restriction that constrained Command R+ adoption [[introducing-command-a-94d80d08]]. The model runs on as few as two NVIDIA H100s (or a single Blackwell B200) at W4A4 quantization, supports 48 languages and a 128K context window, and ships with native citation grounding for agentic enterprise workflows [[introducing-command-a-94d80d08]].

> Cohere released Command A+ on May 20, 2026: a 218B sparse Mixture-of-Experts model with 25B active parameters, Apache 2.0 licensed, that runs on as few as 2 H100 GPUs. The model is released under the Apache 2.0 license, which is OSI-approved and imposes no revenue caps, naming requirements, or use-case restrictions.

Command A+ scores 37 on the Artificial Analysis Intelligence Index — above the median (30) for open-weights models in its size class, but well below the Chinese open-weights frontier (Kimi K2.6 / MiMo-V2.5-Pro at 54, GLM-5.1 at 51) [[cohere-launches-open-weights-model-command-a-more-than-a-year-since-the-command-a-release-7a929ac1]]. The interesting wrinkle is the licensing-axis frontier: Command A+ is the first 200B-class open-weights model under unrestricted Apache 2.0, a stricter open-source bar than the MIT-licensed Chinese leaders, and a meaningful win for sovereign / on-prem enterprise agentic deployment.

> Command A+ scores 37 on the Artificial Analysis Intelligence Index, placing it above average among other open weight models of similar size (median: 30).

> Command A+ is a mixture-of-experts (MoE) model that is an efficient, versatile, and privately deployable LLM built for high-performance agentic tasks with minimal compute overhead. In practice, this enables Command A+ to run on as little as two NVIDIA H100s or a single NVIDIA Blackwell GPU, with virtually no quality degradation.

## Disputes

- [[cohere-launches-open-weights-model-command-a-more-than-a-year-since-the-command-a-release-7a929ac1]] places Cohere Command A+ at AA Intelligence Index 37 (above the median 30 for its size class) and frames it as the first fully Apache-2.0 200B-class open-weights frontier-adjacent model; the established Chinese open-weights frontier (Kimi K2.6 / MiMo-V2.5-Pro at 54, GLM-5.1 at 51) sits 14-17 AA-Index points higher under MIT license. Status: unresolved — 'leading open-weights model' depends on whether you weight aggregate intelligence (Chinese MIT leaders) or licensing strictness (Cohere Apache 2.0).

## Open questions

- [ ] Does Cohere Command A+'s Apache-2.0 license translate into measurably different sovereign/regulated agentic-deployment adoption versus the MIT-licensed Chinese leaders?
- [ ] Does Command A+'s native-citation grounding reduce hallucination rates in agentic-coding loops, or is it primarily a documentation/audit-trail feature?

## See also

- [[frontier-models]]
- [[glm-5]]
- [[kimi-k2.6]]
- [[mimo-v2.5-pro]]
