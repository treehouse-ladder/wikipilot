---
name: qmd-search
description: |
  Thin wrapper around the wikipilot-qmd MCP server's `qmd_search` tool
  (served by scripts/qmd_mcp_server.py — qmd 0.1.2 itself does not ship
  an MCP server). Searches the local wiki via hybrid BM25 + vector
  retrieval, then dedupes results against the last N entries in
  wiki/log.md so the topic-researcher doesn't re-propose pages whose
  source was added today. Also exposes `qmd_collection_info` for
  diagnostic "is the index alive?" checks.
allowed_tools:
  - Bash
  - Read
---

# qmd-search

## When to use

- `topic-researcher` calls this BEFORE WebSearch, on every research run, to discover what the wiki already says about a candidate concept.
- `query-answerer` calls this FIRST before falling back to WebSearch — if the wiki has the answer, no external call is needed.
- `wiki-disputes-scanner` uses this to load the candidate page sets selected by `disputes_seed.py`.

## Contract

- Tool: `qmd_search(query, top_k=10, rerank=False, filters_json=None)` on the `wikipilot-qmd` MCP connector.
- Input: a natural-language query string. Optional `top_k` (1–50, default 10), `rerank` (slower cross-encoder rerank), and `filters_json` (a JSON object of metadata constraints, e.g. `{"path": "topics/agentic-coding/index.md"}`).
- Output: ranked list of `{path, score, bm25_score, vector_score, rerank_score, text, metadata}`. The skill dedupes against the last N (default 50) ingest entries in `wiki/log.md` so freshly-ingested sources don't keep showing up.
- Companion tool: `qmd_collection_info()` returns `{name, document_count, chunk_count, embedding_dim, db_path}` — call when you need to confirm the index is non-empty.

## Setup

The `wikipilot-qmd` MCP server is auto-loaded from the project-scoped [`.mcp.json`](../../../.mcp.json) at the repo root, with [`/.claude/settings.json`](../../../.claude/settings.json) pre-approving it via `enabledMcpjsonServers`. No manual connector registration is required in claude.ai or Cursor — the project files do all the wiring. See [`docs/qmd-setup.md`](../../../docs/qmd-setup.md) for the local-dev install and the Windows stdio caveat, and [`docs/routines-setup.md`](../../../docs/routines-setup.md) for the routine-side allowed-tools configuration (you do need to add `mcp__wikipilot-qmd__qmd_search` and `mcp__wikipilot-qmd__qmd_collection_info` to each routine's allowed-tools list, because the routine UI does not auto-populate MCP tool names).

## What this skill does NOT do

- It does not search the live web. WebSearch is a separate tool, used as a fallback for `query-answerer` and as the primary discovery mechanism for `topic-researcher`.
- It does not write to the index. `wikipilot index-wiki` is what refreshes qmd's index after writes; the cloud setup script runs it on every routine start.
