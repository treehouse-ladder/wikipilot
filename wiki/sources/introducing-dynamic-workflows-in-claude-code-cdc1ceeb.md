---
fetched_at: &id001 2026-06-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: cdc1ceeb
sources: []
title: "Introducing dynamic workflows in Claude Code"
topic: agentic-coding
url: "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code"
---

## Excerpts

> We're introducing dynamic workflows in Claude Code, helping Claude take on the most challenging tasks end-to-end. Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

> When a workflow kicks off, Claude plans dynamically based on your prompt, breaks it into subtasks, and fans the work out across subagents running in parallel. Results are checked before they're folded in, and you come back to a single, coordinated answer. Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until the answers converge—which is how a workflow reaches results a single pass can't.

> Jarred Sumner used dynamic workflows to port Bun from Zig to Rust with 99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge.

> Dynamic workflows are available today in research preview in the Claude Code CLI, Desktop, and the VS Code extension for Max, Team, and Enterprise (if admin enabled) plans, as well as on the Claude API, on Amazon Bedrock, Vertex AI, and Microsoft Foundry.

> Ultracode is a Claude Code setting that combines xhigh reasoning effort with automatic workflow orchestration. With it on, Claude plans a workflow for each substantive task instead of waiting for you to ask.
