---
title: "Probe-and-Refine Tuning of Repository Guidance for Coding Agents"
kind: source
url: "https://arxiv.org/abs/2606.20512"
sha256: "86f1891b"
fetched_at: "2026-06-21"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-06-21
last_verified: 2026-06-21
freshness_window_days: 365
---

## Excerpts

> LLM-based coding agents need higher-level operational knowledge about a repository (which files house which subsystems, how to run the test suite, which workflows have historically led to wrong fixes) that does not exist in the code itself. Engineers typically maintain AGENTS.md files to supply this context as instructions for coding agents, but whether they help is contested.

> [Probe-and-refine] introduces a procedure that uses synthetic bug-fix probes to iteratively diagnose and patch a repository's guidance file through single-shot LLM calls, with no agent loop or tool use during tuning.

> On SWE-bench Verified across four independent trials with Qwen3.5-35B-A3B at 200 steps, probe-and-refine achieves 33.0% mean resolve rate vs. 28.3% for the static knowledge base.
