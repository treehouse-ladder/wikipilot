---
title: "Muse Spark"
kind: entity
sources: ["[[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]", "[[introducing-muse-spark-1-1-f8a95609]]", "[[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]]", "[[muse-spark-1-2-3d7d1796]]", "[[introducing-muse-code-and-muse-spark-1-2-a73147b0]]", "[[introducing-muse-glimmer-c60b75d4]]"]
last_updated: "2026-08-11"
last_verified: "2026-08-06"
freshness_window_days: 30
---

## Summary

Muse Spark is Meta's first frontier-class model since Llama 4 Maverick (April 2025) and — notably — the first Meta model not released as open weights [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]. It scores 52 on the Artificial Analysis Intelligence Index, placing it in the top 5 models benchmarked, ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax-M2.7, and Grok 4.20, and behind Gemini 3.1 Pro Preview, GPT-5.4, and Claude Opus 4.6. The jump is dramatic relative to Meta's open-weight history: Llama 4 Maverick and Scout scored 18 and 13 respectively as non-reasoning models, so Muse Spark closes most of the frontier gap in a single release.

Muse Spark is a multimodal reasoning model that can process text, image, and speech input and generate text output [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]. It has a context window of 260k tokens. The model is not open source and is not yet accessible via an API, but Meta has shared they expect API access to come soon. Currently, Muse Spark is gated to Meta's first-party products: Meta AI, Facebook, Instagram, and Threads.

> Muse Spark scores 52 on the Artificial Analysis Intelligence Index, placing it within the top 5 models benchmarked. It sits ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax-M2.7, Grok 4.20 and behind Gemini 3.1 Pro Preview, GPT-5.4 and Claude Opus 4.6.

> It is the first frontier-class model from Meta since Llama 4 Maverick was released in April 2025, and notably the first Meta model that is not being released as open weights.

> Muse Spark essentially closes the gap to the frontier in a single release.

**Update 2026-07-09 — Muse Spark 1.1.** Meta released Muse Spark 1.1 on July 9, 2026, resolving the open questions about API availability and pricing: it is the first Meta frontier model behind a paid API (the new Meta Model API, public preview) rather than gated to first-party apps [[introducing-muse-spark-1-1-f8a95609]]. Independent placement: Artificial Analysis scores Muse Spark 1.1 (xhigh) at **AA Intelligence Index v4.1 = 51**, up 8 points from Muse Spark 1.0's 43, tied with GLM-5.2 (max), GPT-5.4 (xhigh) and GPT-5.6 Luna (max), three points behind Grok 4.5 (high, 54) [[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]]. The context window grew from 260k to **1M tokens**, with full multimodal input (images, video, PDFs), built-in search with citations, and parallel tool calling [[introducing-muse-spark-1-1-f8a95609]]. Pricing is aggressive — **$1.25 input / $4.25 output per Mtoken** (~1/4 of Anthropic/OpenAI flagship rates), ~$0.26 per Intelligence-Index task [[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]]. It leads Meta-reported scaled/professional tool use (MCP Atlas 88.1, JobBench 54.7) but trails frontier leaders on contamination-resistant coding (SWE-Bench Pro 61.5 vs Opus 4.8's 69.2) [[introducing-muse-spark-1-1-f8a95609]].

> Developers can now build with Muse Spark 1.1 via the new Meta Model API, now in public preview. Muse Spark 1.1 has a context window of 1 million tokens. [[introducing-muse-spark-1-1-f8a95609]]

> Meta's Muse Spark 1.1 (xhigh) scores 51 on the Artificial Analysis Intelligence Index and gains 8 points over Muse Spark 1.0 (43) in three months... three points behind Grok 4.5 (high, 54). [[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]]

**Update 2026-08-06 — Muse Spark 1.2 + Muse Code.** Meta released Muse Spark 1.2 on August 5, 2026 via the Meta Model API; Artificial Analysis independently scores Muse Spark 1.2 (xhigh) at **AA Intelligence Index v4.1 = 54**, up 3 points from Muse Spark 1.1 (51) and 11 from Muse Spark 1.0 (43, April) [[muse-spark-1-2-3d7d1796]]. It enters effectively **tied with Grok 4.5 (high, 54)** and **one point behind GPT-5.5 (xhigh, 55)**, narrowly behind the unchanged top cluster (Claude Opus 5 max 61, Fable 5 60, GPT-5.6 Sol 59, Kimi K3 57), so it does **not** displace any frontier leader [[muse-spark-1-2-3d7d1796]]. Pricing is unchanged at **$1.25 input / $4.25 output per Mtoken**, with an additional data-sharing contributor tier at $0.10/$0.20 [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]. Muse Spark 1.2 was **co-trained with Muse Code**, Meta's terminal coding agent, using rejection-sampled harness trajectories — the first production instance of a model co-trained with its own agentic harness [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]. Muse Spark 1.2 is now Meta's current per-lab flagship, superseding Muse Spark 1.1 (51).

> Muse Spark 1.2 (xhigh) scores 54 on the Artificial Analysis Intelligence Index, up 3 points from Muse Spark 1.1 (51) and 11 points from Muse Spark 1.0 (43, April). It enters effectively tied with GPT-5.5 (xhigh, 55) and Grok 4.5 (high, 54). Muse Spark 1.2 (xhigh) costs $1.25 per 1M input tokens and $4.25 per 1M output tokens. [[muse-spark-1-2-3d7d1796]]

> Muse Spark 1.2 was co-trained with Muse Code ... training that included rejection sampled harness trajectories and recipe optimizations alongside the integration of the Muse Code toolset. [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]

Five days after Muse Spark 1.2, Meta released **Muse Glimmer**, a 30B Apache-2.0 open-weights model optimized for agentic coding [[introducing-muse-glimmer-c60b75d4]]. Unlike the API-only Muse Spark line, Muse Glimmer is open-weights, letting users run it in their own harness rather than via the Meta Model API. Meta reports strong full-task benchmark scores (SWE-Bench, MCP-Atlas, τ-Bench, DeepSearch QA), but these are Meta's own numbers — no independent third-party verification yet [[introducing-muse-glimmer-c60b75d4]].

> Muse Glimmer is a new 30B model from Meta released under a clean Apache 2.0 license, optimized for end-to-end agentic task completion. It achieves strong success rates on full-task benchmarks including DeepSearch QA, MCP-Atlas, tau-Bench and SWE-Bench, measuring its ability to work within scaffolds, write and debug code, and resolve multi-turn requests from start to finish. [[introducing-muse-glimmer-c60b75d4]]

## Disputes

- [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]] claims Muse Spark (AA Index 52) sits "within the top 5 models benchmarked" and "behind Gemini 3.1 Pro Preview, GPT-5.4 and Claude Opus 4.6"; however, since this source's publication, Anthropic released Claude Opus 4.7 (AA Index 57, April 16 2026), Claude Opus 4.8 (AA Index 61.4, May 28 2026), and Claude Fable 5 (AA Index 64.9, June 9 2026), all of which rank above Muse Spark's 52. Status: unresolved (confidence: high; sweep: 2026-06-14)
- [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]] reports Muse Spark 1.0 scored 52 on the Artificial Analysis Intelligence Index (v4.0, April 2026); [[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]] reports Muse Spark 1.0 scored 43 on AA Intelligence Index v4.1. The Summary's 52 is the v4.0 score while the body's "1.0 (43)" is the v4.1 re-score. Both are valid measurements but without explicit version labels in the Summary, readers may interpret them as conflicting scores for the same model version. Status: unresolved (confidence: medium; sweep: 2026-07-19) — the Summary should clarify the AA Index version for the 52 score.

## Open questions

- [ ] Does Muse Spark's AA Index 52 hold on contamination-resistant benchmarks (SWE-bench Pro), or does Meta's single-release frontier jump look weaker on harder evals?
- [ ] Is Muse Spark a clean-room new architecture or a continuation/scale-up of the Llama line?
- [ ] What does Meta's pivot away from open weights with Muse Spark imply for the open/closed competitive balance going forward?
- [ ] When will API access become available, and what will the pricing structure be relative to other frontier models?
- [ ] Where does Muse Spark now rank on the AA Intelligence Index relative to the post-May releases (Opus 4.7, Opus 4.8, Fable 5)?
- [ ] Does Muse Spark 1.1's Meta-reported tool-use leadership (MCP Atlas, JobBench) reproduce on the independent AA Coding Agent Index, or is it a vendor-eval artifact given the mid-cluster AA Intelligence Index of 51? [[muse-spark-1-1-meta-gains-8-intelligence-index-points-in-three-months-56cc77a0]]
- [ ] Does Muse Spark 1.2 (AA Index v4.1 = 54) improve on Muse Spark 1.1's contamination-resistant coding (SWE-Bench Pro 61.5) and Meta-reported tool-use leadership, or is the +3 aggregate gain concentrated in non-coding evals? [[muse-spark-1-2-3d7d1796]]

## See also

- [[muse-code]]
- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
