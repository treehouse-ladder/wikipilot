---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 9fa759b72385cdecdf59660d48a3a9bd4f6f419e8a77026091818c594be75130
sources: []
title: Harness design for long-running application development (Anthropic Engineering)
topic: agentic-coding
url: https://www.anthropic.com/engineering/harness-design-long-running-apps
---

## Excerpts

> The final result was a three-agent architecture — planner, generator, and evaluator — that produced rich full-stack applications over multi-hour autonomous coding sessions.

> Taking inspiration from Generative Adversarial Networks (GANs), we designed a multi-agent structure with a generator and evaluator agent. The generator-evaluator loop maps naturally onto the software development lifecycle, where code review and QA serve the same structural role as the design evaluator.

> The agents were run as one continuous session across the whole build, with the Claude Agent SDK's automatic compaction handling context growth along the way. Claude Opus 4.5 largely removed 'context anxiety' behavior, so context resets could be dropped from this harness entirely.