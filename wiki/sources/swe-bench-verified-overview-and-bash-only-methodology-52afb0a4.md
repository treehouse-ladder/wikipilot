---
fetched_at: &id001 2026-05-12
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 52afb0a46b6c14215b1cff609198e4369a44aa193f8ce4d5697b45abf86e1816
sources: []
title: SWE-bench Verified (overview and bash-only methodology)
topic: agentic-coding
url: https://www.swebench.com/verified
---

## Excerpts

> SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI. Human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information.

> While the full leaderboard compares arbitrary systems, we are also interested in evaluating language models directly. To make an apples-to-apples comparison of LMs easier, we evaluate all LMs using mini-SWE-agent in a minimal bash environment. No tools, no special scaffold structure; just a simple ReAct agent loop.