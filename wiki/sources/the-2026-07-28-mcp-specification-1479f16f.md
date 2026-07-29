---
fetched_at: &id001 2026-07-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1479f16fea091e4acdf29c4644a8256ec71757fba54141579a75d0293e5b5abf
sources: []
title: The 2026-07-28 MCP Specification
topic: agentic-coding
url: https://blog.modelcontextprotocol.io/posts/2026-07-28/
---

## Excerpts

> The 2026-07-28 specification delivers a stateless core that scales on ordinary HTTP infrastructure.

> The Mcp-Session-Id header and the protocol-level session are removed, meaning any MCP request can land on any server instance, and sticky routing and shared session stores are no longer required.

> Standard MCP request headers (Mcp-Method, Mcp-Name) are now required on Streamable HTTP POST requests so load balancers, gateways, and rate-limiters can route on the operation without inspecting the body.

> ttlMs and cacheScope fields are required on results from list endpoints, with ttlMs allowing clients to cache responses and cacheScope controlling whether shared intermediaries may cache.

> The Enterprise-Managed Authorization extension is now stable, allowing organizations to centrally manage authorization for MCP servers.

> Roots, Sampling, and Logging features are deprecated but remain functional during the deprecation window.

> The 2026-07-28 specification is published as final, replacing 2025-11-25.