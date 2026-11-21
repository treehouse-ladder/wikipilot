---
fetched_at: &id001 2026-11-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e45fd791e1fe03c27509e5cfc6fcacfeb1c5b0665a232d00558d4f3fb339f62b
sources: []
title: External sandboxes for coding agents
topic: agentic-coding
url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/
---

## Excerpts

> Code executed by the agent runs inside a dedicated sandbox while the agent itself lives outside of that sandbox. The project ships three sandbox server implementations: external-sandbox-v86 runs a Node.js server which then uses v86 to run Alpine Linux inside WebAssembly; a container-based Python server; and a Python server using Microsoft's Quicksand library. All three offer the same localhost API. You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want to execute code. The sandboxes also include an optional allow-list proxy for HTTP/HTTPS traffic, plus a credential replacement mechanism so the agent can make authenticated calls without holding the secret.