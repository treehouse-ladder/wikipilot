---
title: "MAI-Thinking-1"
kind: entity
aliases: ["MAI Thinking 1", "Microsoft MAI-Thinking-1", "mai-thinking-1"]
sources: ["[[introducing-mai-thinking-1-0e3e1662]]", "[[microsoft-build-2026-mai-keynote-transcript-77c10a37]]"]
last_updated: 2026-06-05
last_verified: 2026-06-05
freshness_window_days: 30
---

## Summary

MAI-Thinking-1 is Microsoft AI's first in-house reasoning model, announced at Build 2026 on June 2, 2026 [[introducing-mai-thinking-1-0e3e1662]]. It is a sparse mixture-of-experts model with ~35B active parameters out of ~1T total, supporting a 256,000-token context window, trained end-to-end by Microsoft on commercially licensed data with no distillation from OpenAI, Anthropic, or other third-party models [[introducing-mai-thinking-1-0e3e1662]]. The model is available in private preview through Microsoft Foundry and is compatible with the Chat Completions API; public pricing has not been finalized, and it will become available through third-party inference providers including Fireworks AI, Baseten, and OpenRouter [[introducing-mai-thinking-1-0e3e1662]].

> MAI-Thinking-1 is a 35-billion active parameter reasoning model trained on commercially licensed data... a mid-sized sparse Mixture of Experts model with 35 billion active parameters and a 256,000-token context window, trained from scratch on enterprise-grade, commercially licensed data, without distillation from any third-party model.

Headline benchmarks: 97.0% on AIME 2025, 94.5% on AIME 2026, 84.2% on GPQA Diamond, 87.7% on LiveCodeBench v6, 73.5% on SWE-bench Verified, 52.8% on SWE-Bench Pro, 84.9% on HMMT February 2026 [[introducing-mai-thinking-1-0e3e1662]]. Microsoft frames the SWE-Bench Pro number as matching Claude Opus 4.6, and reports that blind human raters on Surge preferred MAI-Thinking-1 over Claude Sonnet 4.6 across single and multi-turn tasks [[introducing-mai-thinking-1-0e3e1662]]. When run on Microsoft's in-house MAIA 200 chip the model delivers 30% better performance-per-dollar and 1.4x performance-per-watt versus NVIDIA GB200 [[microsoft-build-2026-mai-keynote-transcript-77c10a37]].

> MAI-Thinking-1 reaches 97.0% on AIME 2025, and 94.5% on AIME 2026. It's at 53% on SWE Bench Pro, placing it right alongside Opus 4.6 on one of the toughest coding benchmarks.

> When running MAI models on the MAIA 200 chip end-to-end, Microsoft sees 30% better performance per dollar as well as a 1.4x performance-per-watt gain versus GB200.

## Disputes

- [[introducing-mai-thinking-1-0e3e1662]] claims MAI-Thinking-1 ties Claude Opus 4.6 on SWE-Bench Pro at 52.8% and is preferred over Sonnet 4.6 in Surge blind side-by-sides; the public Anthropic frontier has since moved to Opus 4.7 (64.3% SWE-Bench Pro) and Opus 4.8 (69.2% SWE-Bench Pro) [[claude-opus-4-8-benchmarks-explained-60247f20]], so on Microsoft's own benchmark MAI-Thinking-1 trails the current Anthropic frontier by 12-16 points. Status: unresolved — the parity claim is true against the comparison Microsoft chose (Opus 4.6) but not against the current frontier.

## Open questions

- [ ] What is MAI-Thinking-1's score on the Artificial Analysis Intelligence Index (Opus 4.8: 61.4, GPT-5.5 xhigh: 60, Gemini 3.1 Pro: 57)? Microsoft has not published an AA result.
- [ ] When does MAI-Thinking-1 leave private preview and what will its public per-token pricing be vs. Opus 4.6 ($5/$25 per Mtoken) and MAI-Code-1-Flash ($0.75/$4.50)?
- [ ] Is MAI-Thinking-1's 73.5% SWE-bench Verified competitive with Kimi K2.6 (80.2%) and DeepSeek V4-Pro (80.6%) once contamination is controlled?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[claude-opus-4.8]]
- [[gpt-5.5]]
