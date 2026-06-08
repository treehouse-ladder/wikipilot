---
fetched_at: &id001 2026-06-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: bbb7a8dae33b3ae4546f8cf46591604bbce397fb80fae5c86771bb73fe43c9f3
sources: []
title: 'A harness for every task: dynamic workflows in Claude Code'
topic: frontier-models
url: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
---

## Excerpts

> A dynamic workflow is a JavaScript script that orchestrates subagents at scale. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.

> Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

> Jarred Sumner used dynamic workflows to port Bun from Zig to Rust with 99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge.

> A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer. Progress is saved as the run goes, so a job that's interrupted picks up where it left off.