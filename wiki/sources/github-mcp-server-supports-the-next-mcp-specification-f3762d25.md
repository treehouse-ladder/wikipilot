---
fetched_at: &id001 2026-07-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f3762d253a5abb7b2abfc50b9382a32628020aae379ade050434d0df1042ab26
sources: []
title: GitHub MCP Server supports the next MCP specification
topic: agentic-coding
url: https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification/
---

## Excerpts

> The MCP protocol is going stateless on 28th July 2026, and the GitHub MCP Server supports the latest spec ahead of the official release. The new stateless core means MCP deployments are now easy to scale. Database writes on initialize are gone, and database reads are gone from every call, which makes things snappier without users losing anything. Clients can also complete the handshake in parallel. MCP added official conformance tests. Strict validation helps agents to verify their work. Sessions and initialize are both removed, so you can connect to servers faster and easier.