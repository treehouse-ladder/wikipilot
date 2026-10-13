---
fetched_at: &id001 2026-10-13
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1772bb3eaf1415bdab1ef0d6b32834785b3ddead45709fdf92ef87fe1a852840
sources: []
title: 'Announcing FrontierCode on Artificial Analysis: can AI models write code maintainers
  would merge?'
topic: frontier-models
url: https://artificialanalysis.ai/articles/frontiercode
---

## Excerpts

> FrontierCode is a coding benchmark from Cognition, built with open-source maintainers, that measures whether an AI-written change is good enough for a maintainer of that repository to merge. Unlike pass/fail test suites, models are also assessed on behaviors like making excessive changes and large diffs, modifying files outside the relevant scope, or adding unhelpful tests.

> Claude Opus 5.5 (max with fallback) leads FrontierCode with an average score of 52% and a pass rate of 58%. GPT-6.1 Sol (max) and Claude Fable 5.1 (max with fallback) follow at 49%. The top open-weights model is MiMo-V2.6-Pro at 45%.

> Pass rate is the share of attempts that complete all blocking criteria, while scores reflect desirable non-blockers too. FrontierCode is a standalone evaluation and is not part of Artificial Analysis Intelligence Index v4.3.2; the implementation uses the primary 100-task set of the benchmark's 150 tasks, with 3 attempts per task.