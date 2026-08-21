---
fetched_at: &id001 2026-08-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 7b19f9decc56773774fc6f9cf5c5dfe1446090aaaf0b50b7d74aff51f9482cb1
sources: []
title: 'LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks'
topic: agentic-coding
url: https://arxiv.org/abs/2608.01964
---

## Excerpts

> LongHorizon-Harness reformulates long-horizon execution as a task-state management problem, maintaining the task state explicitly outside execution and updating it only with facts independently verified from the environment.

> The approach uses a Manage-Execute-Audit (MEA) loop that employs a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round.

> Existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions.