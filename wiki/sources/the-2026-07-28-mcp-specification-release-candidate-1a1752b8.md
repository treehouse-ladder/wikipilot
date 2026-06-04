---
fetched_at: &id001 2026-06-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1a1752b8
sources: []
title: "The 2026-07-28 MCP Specification Release Candidate"
topic: agentic-coding
url: "https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/"
---

## Excerpts

> The release candidate for the next Model Context Protocol (MCP) specification includes a stateless protocol core, the Extensions framework, Tasks, MCP Apps, authorization hardening, and a formal deprecation policy. The release candidate is available now and the final specification ships on July 28, 2026.

> The protocol is now stateless: no handshake, no session id, any request can hit any server instance. Previously, every MCP connection required an initialize handshake that returned an Mcp-Session-Id, pinning clients to a specific server instance. In 2026-07-28, that handshake is gone. Every request is now self-contained — protocol version, client info, and capabilities travel in _meta on every request.

> The Tasks extension reshapes the lifecycle around the stateless model: a server can answer tools/call with a task handle, and the client drives it with tasks/get, tasks/update, and tasks/cancel. Task creation is server-directed: the client advertises the extension and the server decides when a call should run as a task.

> A remote MCP server that previously needed sticky sessions, a shared session store, and deep packet inspection at the gateway can now run behind a plain round-robin load balancer, route traffic on an Mcp-Method header, and let clients cache tools/list responses for as long as the server's ttlMs permits.

> This release contains breaking changes, and there's a ten-week window for SDK maintainers and client implementers to validate the changes against real workloads. The feature lifecycle policy gives every feature an Active, Deprecated, and Removed lifecycle with at least twelve months between deprecation and the earliest possible removal.
