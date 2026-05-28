---
fetched_at: &id001 2026-05-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f9ff221789e0942ded4a02e1f52be26f5aaab06ad877ede8e216af949dcb07cc
sources: []
title: 'An open-source spec for Codex orchestration: Symphony'
topic: agentic-coding
url: https://openai.com/index/open-source-codex-orchestration-symphony/
---

## Excerpts

> Symphony is an agent orchestrator that turns a project-management board like Linear into a control plane for coding agents. Every open task gets an agent, agents run continuously, and humans review the results.

> Symphony continuously watches the task board and ensures that every active task has an agent running in the loop until it's done. If an agent crashes or stalls, Symphony restarts it. If new work appears, Symphony picks it up and starts organizing work.

> The workflow is built based on ticket statuses, using the task manager Linear as a state machine. Because the orchestrator runs on devboxes and never sleeps, tasks can be added from anywhere and an agent will pick them up.

> Among some teams at OpenAI, the number of landed PRs increased by 500% in the first three weeks. At its center sits SPEC.md, a single Markdown file that documents the protocol, agent lifecycle management, retries and backoff, paired with the Elixir reference implementation, which uses Erlang/OTP supervision trees for process-level fault tolerance.