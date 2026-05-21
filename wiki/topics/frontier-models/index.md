---
title: Frontier LLM landscape
kind: topic
sources: ["[[introducing-claude-opus-47-b8af8104]]", "[[claude-opus-47-everything-you-need-to-know-751c1827]]", "[[introducing-gpt-55-dfe7e0c6]]", "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]", "[[gemini-31-pro-model-card-225ab705]]", "[[gemini-3-deep-think-advancing-science-research-and-engineering-e98b788f]]", "[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]", "[[introducing-claude-sonnet-46-c4a45eed]]", "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]", "[[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]", "[[introducing-mistral-3-3772caab]]", "[[artificial-analysis-intelligence-index-07e9d51e]]", "[[gdpval-measuring-the-performance-of-our-models-on-real-world-tasks-bc53ab6b]]", "[[the-llama-4-herd-a-new-era-of-natively-multimodal-ai-7554c7f6]]"]
last_updated: 2026-05-20
last_verified: 2026-05-20
freshness_window_days: 30
---

# Frontier LLM landscape

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary (2026-05-20 update)

The frontier-LLM landscape in mid-May 2026 is a four-way contest between Anthropic, OpenAI, Google DeepMind, and DeepSeek, with xAI, Alibaba (Qwen), Meta (Llama), and Mistral providing competitive flank pressure — especially on open weights.

### Current intelligence leaders (Artificial Analysis Intelligence Index v4.0)

As of May 2026, GPT-5.5 (xhigh) leads at 60, followed by GPT-5.5 (high) at 59, then a three-way tie at 57 between Claude Opus 4.7 (Adaptive, Max), Gemini 3.1 Pro Preview, and GPT-5.4 (xhigh) [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]. Qwen3.7 Max (released May 19) also scores 57, making it the most intelligent open-ecosystem reasoning model on this index [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]. The Intelligence Index is a 10-evaluation aggregate (GDPval-AA, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, Humanity's Last Exam, GPQA Diamond, CritPt, Tau-squared-Bench Telecom) [[artificial-analysis-intelligence-index-07e9d51e]].

> GPT-5.5 (xhigh) currently ranks #1 on the Artificial Analysis LLM Leaderboard with an Intelligence Index score of 60.

> The Artificial Analysis Intelligence Index v4.0 incorporates 10 evaluations.

### Anthropic

Claude Opus 4.7 (released April 16, 2026) is the leader on GDPval-AA at 1,753 Elo — ~79 Elo points clear of the next models [[claude-opus-47-everything-you-need-to-know-751c1827]]. It also takes #2 on AA-Omniscience behind Gemini 3.1 Pro, driven primarily by reduced hallucination. Cost per Intelligence Index run is ~$4,406, ~11% less than Opus 4.6 despite scoring 4 points higher [[claude-opus-47-everything-you-need-to-know-751c1827]].

> Opus 4.7 is the new leader on GDPval-AA, scoring 1,753 Elo, around 79 Elo points ahead of the next closest models.

> Claude Opus 4.7 is our most intelligent model, with state-of-the-art performance on coding, agentic tasks, and reasoning.

Claude Sonnet 4.6 (released Feb 17, 2026) added a 1M-token context window in beta at unchanged $3/$15 per Mtoken pricing, jumped 8 points on the AA Intelligence Index (to 51) over Sonnet 4.5, and scored 60.4% on ARC-AGI-2 with 120k thinking tokens at high effort [[introducing-claude-sonnet-46-c4a45eed]].

> Sonnet 4.6 features a 1M token context window in beta. Pricing remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.

### OpenAI

GPT-5.5 (released April 23, 2026) is positioned as more token-efficient than GPT-5.4 despite higher per-token pricing, with major gains in agentic coding, computer use, and knowledge work [[introducing-gpt-55-dfe7e0c6]].

> GPT-5.5 is priced higher than GPT-5.4, but it is both more intelligent and much more token efficient, delivering better results with fewer tokens.

OpenAI's GDPval benchmark (open-sourced 220-task gold subset, 44 occupations across the top 9 US-GDP sectors covering $3T of annual labor) has become a de-facto frontier evaluation, now incorporated into the AA Intelligence Index v4.0 as GDPval-AA [[gdpval-measuring-the-performance-of-our-models-on-real-world-tasks-bc53ab6b]].

> The primary evaluation metric is head-to-head human expert comparison. OpenAI has open-sourced a gold subset of 220 tasks.

### Google DeepMind

Gemini 3.1 Pro Preview supports 1M-token input and up to 64k-token output, priced at $2/$12 per Mtoken below 200k input, jumping to $4/$18 above 200k — the first major frontier model to officially tier prices by context length [[gemini-31-pro-model-card-225ab705]].

> Input price: $2.00 for prompts <= 200k tokens, $4.00 for prompts > 200k tokens.

Gemini 3 Deep Think reached 3455 Elo on Codeforces and gold-medal level on IMO 2025 [[gemini-3-deep-think-advancing-science-research-and-engineering-e98b788f]].

> Gemini 3 Deep Think attained a staggering Elo of 3455 on Codeforces ... and reached gold-medal level performance on the International Math Olympiad 2025.

### Open weights and Chinese labs

DeepSeek V4 (released April 24, 2026) is a 1.6T MoE (49B active, V4-Pro) and 284B MoE (13B active, V4-Flash), both with 1M context, both released under the MIT license. V4-Pro-Max scores 80.6% SWE-bench Verified and 3,206 Codeforces — surpassing GPT-5.4's 3,168 [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]].

> The model weights are licensed under the MIT License. V4-Pro's Codeforces rating of 3,206 surpasses GPT-5.4's 3,168.

Mistral Large 3 (released December 2025) is a sparse MoE with 41B active and 675B total parameters under Apache 2.0 [[introducing-mistral-3-3772caab]]. Llama 4 Scout (17B active, 16 experts) ships with a 10M-token context window — currently the longest in any frontier-class open model [[the-llama-4-herd-a-new-era-of-natively-multimodal-ai-7554c7f6]].

> Llama 4 Scout offers an industry-leading context window of 10M.

Qwen3.7 Max (released May 19, 2026) reaches AA Intelligence Index 57 with a 1M-token context, putting Alibaba's frontier offering at parity with closed-source leaders [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]].

### xAI

Grok 4.3 (released April 30, 2026) hit AA Intelligence Index 53, with the largest single-benchmark improvement on GDPval-AA (+321 Elo over Grok 4.20). API pricing of $1.25/$2.50 per Mtoken is well below the frontier median [[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]].

> Grok 4.3 (high) costs $1.25 per 1M input tokens and $2.50 per 1M output tokens.

## Recent updates

_(none yet — populated by the Daily Research routine.)_

## Comparisons

Pre-declared comparison pages (Phase 9 Pattern A) for this topic. Listed
in prose backticks until the underlying entity pages exist; once they do,
the topic-researcher (or `wikipilot compare new`) writes them to
`wiki/comparisons/`:

- [[cost-comparison]] — input/output $/Mtoken across frontier models (created 2026-05-20).
- `benchmark-comparison` — SWE-bench / GPQA / MMLU / ARC-AGI scores.
- `context-window-comparison` — max context + long-context pricing.
- `reasoning-mode-comparison` — reasoning availability, effort/quality
  knobs, cost.

## Disputes

- [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] claims V4-Pro-Max scores 80.6% on SWE-bench Verified, but OpenAI has stopped reporting SWE-bench Verified scores after an audit found every frontier model tested could reproduce verbatim gold patches or problem-statement specifics, indicating training-data contamination; on SWE-bench Pro the leaderboard inverts. Status: unresolved — SWE-bench Pro is the more credible frontier signal in 2026 but Verified scores are still widely quoted in launch materials.
- [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims GPT-5.5 ranks #1 on aggregate AA Intelligence Index at 60, but [[claude-opus-47-everything-you-need-to-know-751c1827]] claims Claude Opus 4.7 leads GDPval-AA (the agentic/economic-value sub-benchmark) by 79 Elo points. Status: unresolved — aggregate-index leadership and agentic-task leadership are coming apart, so 'best model' is task-dependent in mid-2026.

## Open questions

- [ ] Has DeepSeek R2 (reasoning model) actually been released as of 2026-05-20, or has only V4 shipped? Search results are inconsistent.
- [ ] What is the methodological difference between SWE-bench Verified and SWE-bench Pro that explains the inverted rankings?
- [ ] Does GPT-5.5's #1 AA Intelligence Index ranking hold up on long-horizon agentic benchmarks where Claude Opus 4.7 currently leads?
- [ ] Is Gemini 3 Deep Think's 3455 Codeforces Elo measured against the live competition population or against a curated/historical task pool?
- [ ] ARC-AGI-2 went from 54% to 98% in 4 months. Is this genuine capability progress or contamination?

## See also

- [purpose](purpose.md)
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
- [[deepseek-v4]]
