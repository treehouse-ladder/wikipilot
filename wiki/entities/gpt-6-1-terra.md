---
title: "GPT-6.1 Terra"
kind: entity
aliases: ["GPT 6.1 Terra", "gpt61-terra"]
sources: ["[[introducing-gpt-6-1-terra-35e334c1]]", "[[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]]"]
last_updated: 2026-11-08
last_verified: 2026-11-08
freshness_window_days: 30
---

## Summary

**GPT-6.1 Terra** (released 2026-10-26) is OpenAI's cost-optimized model for high-volume professional work, image analysis and computer use, succeeding GPT-5.6 Terra [[introducing-gpt-6-1-terra-35e334c1]]. Standard API pricing is **$1 per Mtoken input / $0.05 cached input / $5 output — 50% below both GPT-5.6 Terra and GPT-6.1 Sol** [[introducing-gpt-6-1-terra-35e334c1]]. It reports **50.3% on Terminal-Bench 4.0 at maximum reasoning effort, more than double GPT-5.6 Terra's 21.5%**, and cuts the low-effort factuality error rate from 53.6% (GPT-5.6 Terra) to 16.7% on OpenAI's internal error-inducing prompt set [[introducing-gpt-6-1-terra-35e334c1]]. It is available to Plus/Pro/Enterprise/Edu users in ChatGPT Work and Codex and via the API as `gpt-6.1-terra`, and meets the Critical cybersecurity threshold under OpenAI's Preparedness Framework.

> GPT-6.1 Terra's standard API prices are 50% lower than GPT-5.6 Terra and GPT-6.1 Sol: $1 per million input tokens, $0.05 per million cached input tokens, and $5 per million output tokens. [[introducing-gpt-6-1-terra-35e334c1]]

> On Terminal-Bench 4.0 at maximum reasoning effort, GPT-6.1 Terra completes 50.3% of tasks, more than double GPT-5.6 Terra's published score of 21.5%. [[introducing-gpt-6-1-terra-35e334c1]]

All figures are OpenAI-reported; no independent third-party evaluation was available at launch.

Independent (Artificial Analysis) evaluation published 2026-11-08 [[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]]: AA Intelligence Index scores by effort — Low 29, Medium 38, High 42, Xhigh 45, Max 51; non-reasoning 30. At max effort gains 6 points over GPT-5.6 Terra at less than a third of the per-task cost ($0.40 vs $1.40). Coding Agent Index v2.0: 48 (vs GPT-6.1 Sol 54, GPT-6 Luna 31). Largest reported Terminal-Bench 4.0 gain (~+20 points). 50-point drop in AA-Omniscience hallucination rate vs GPT-5.6 Terra [[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]]. This resolves the open question "No independent benchmark of GPT-6.1 Terra at launch".

> GPT-6.1 Terra lists at $1 per million input tokens and $5 per million output tokens, versus $2/$12 for GPT-5.6 Terra. [[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]]

> On the Coding Agent Index v2.0 GPT-6.1 Terra scores 48, which is 6 points below GPT-6.1 Sol (54) and 17 points above GPT-6 Luna (31). [[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]]

## Disputes

- [ ] No entry yet.

## Open questions

- [ ] Does GPT-6.1 Terra's AA Coding Agent Index v2.0 score of 48 at max effort generalise to SWE-bench Verified and Terminal-Bench? No third-party eval on those benchmarks is in the wiki yet [[gpt-6-1-terra-pushes-the-cost-efficiency-frontier-e51c1515]].

## See also

- [[frontier-models]]
- [[gpt-6-1-sol]]
- [[gpt-6-astra]]
