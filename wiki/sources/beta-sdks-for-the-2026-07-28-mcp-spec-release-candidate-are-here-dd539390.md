---
fetched_at: &id001 2026-07-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: dd539390a7c6552caf73a90fcf49f94af6d2799b97e89399a3fe01acf7e9dfff
sources: []
title: Beta SDKs for the 2026-07-28 MCP Spec Release Candidate Are Here
topic: agentic-coding
url: https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/
---

## Excerpts

> Beta releases of the Python, TypeScript, Go, and C# SDKs are now available with support for the 2026-07-28 MCP specification release candidate. The new protocol revision goes stateless, removing the initialize handshake and the protocol-level session, and completing the plan we laid out in The Future of MCP Transports. Clients that speak 2026-07-28 fall back to the initialize handshake when they reach a server on 2025-11-25 or earlier, so old servers and new clients keep interoperating. Under the SDK tier system, Tier 1 SDKs are expected to ship support within this window.