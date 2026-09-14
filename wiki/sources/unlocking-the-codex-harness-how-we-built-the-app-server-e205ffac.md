---
fetched_at: &id001 2026-09-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e205ffac9d9f156d0028feaf325542ac53dc21d301de48f946e7a9ad575c469d
sources: []
title: 'Unlocking the Codex harness: how we built the App Server'
topic: agentic-coding
url: https://openai.com/index/unlocking-the-codex-harness/
---

## Excerpts

> The Codex harness is the agent loop and logic that underlies all Codex experiences.

> The Codex App Server is a client-friendly, bidirectional JSON-RPC API. Codex app-server is the interface Codex uses to power rich clients (for example, the Codex VS Code extension), and you should use it when you want a deep integration inside your own product: authentication, conversation history, approvals, and streamed agent events.

> The Codex harness manages conversation state, stream execution, use tools, enforce configured sandbox and approval policies, and carry work across turns, with Codex app-server exposing those capabilities through a documented client protocol where applications can create threads, start turns, receive events, and handle approval requests.