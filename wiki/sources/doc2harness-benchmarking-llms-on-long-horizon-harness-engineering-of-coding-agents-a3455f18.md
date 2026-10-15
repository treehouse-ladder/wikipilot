---
title: "Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents"
kind: source
url: "https://arxiv.org/abs/2610.20344"
sha256: "a3455f18"
fetched_at: "2026-10-15"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-10-15
last_verified: 2026-10-15
freshness_window_days: 365
---

## Excerpts

> Existing coding-agent benchmarks score task success under a fixed harness and never evaluate the harness-engineering skill itself. Doc2Harness is a two-stage benchmark: a build model, working inside a fixed builder harness, writes a complete candidate harness in an isolated container from a development document and an interface-only contract skeleton; a scripted mock model then drives that harness end-to-end in separate containers. Each test case is judged on four observable channels — requests sent to the model, files on disk, process exit code, and command output — with positive controls to rule out vacuous passes.

> Across 19 frontier models evaluated with three builds each on 328 test cases, GPT-6 Astra scores highest at 53.05% and the weakest model scores 27.44%; failures cluster around how cross-cutting functionality is split across modules.
