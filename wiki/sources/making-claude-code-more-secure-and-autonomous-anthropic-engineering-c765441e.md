---
fetched_at: &id001 2026-05-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c765441e9673d9570c4052ccf4644932cf50fd6f7a533fcc340661d0c4499585
sources: []
title: Making Claude Code more secure and autonomous (Anthropic Engineering)
topic: agentic-coding
url: https://www.anthropic.com/engineering/claude-code-sandboxing
---

## Excerpts

> Claude Code's sandboxing safely reduces permission prompts by 84%. Claude Code's new sandboxing features enable two boundaries: filesystem and network isolation. These restrictions are built on top of OS level primitives such as Linux bubblewrap and MacOS seatbelt to enforce restrictions at the OS level. Network isolation is achieved by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox.