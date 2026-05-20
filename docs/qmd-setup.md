# qmd setup

[qmd](https://pypi.org/project/qmd/) is the on-device hybrid BM25 + vector search library Wikipilot indexes the wiki into. Subagents read it over MCP via the small shim at [`scripts/qmd_mcp_server.py`](../scripts/qmd_mcp_server.py) — qmd itself does **not** ship an MCP server, so we provide one.

The cloud routines install qmd during their setup script (see [`routines-setup.md`](routines-setup.md)). This page covers local-dev install for `wikipilot index-wiki`, `wikipilot dry-run`, and registering the MCP server with Claude Code / Cursor locally.

## What gets installed

`pip install qmd` pulls down qmd 0.1.2 (`chengzhag/qmd-py`) and its heavyweight transitives: `sentence-transformers`, `torch`, `transformers`, `scikit-learn`, `sqlite-vec`. First-time installs are ~1–2 GB on disk and a few minutes on a typical connection. Subsequent reinstalls are fast.

`qmd` 0.1.2 has a packaging gap: its pytest plugin imports `rank_bm25` without declaring it as a dep. We add it explicitly in `pyproject.toml` so `uv sync` / `pip install -e .` always include it.

## Local install

```powershell
# Inside the wikipilot venv:
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
qmd --help
```

If you previously installed qmd into your system Python by accident, install it into the venv explicitly:

```powershell
.\.venv\Scripts\python.exe -m pip install qmd rank_bm25 mcp
```

## Initial index

```powershell
wikipilot index-wiki --full
```

The first index call also triggers a one-time download of the `Qwen/Qwen3-Embedding-0.6B` model (~600 MB) from HuggingFace into `~/.cache/huggingface/`. After that, the embedding model is cached for the life of the machine. Total first-run cost for the wiki: ~30 s including model load.

The DB lands at `.qmd/wiki.db` (sibling of `wiki/`). `.qmd/` is already in `.gitignore` — don't commit it.

## Refresh after writes

```powershell
wikipilot index-wiki   # incremental: skips files whose mtime is unchanged
```

The incremental indexer compares each file's `st_mtime_ns` against the value stored on the document's metadata. Unchanged files are skipped; new files are added; removed files are deleted from the collection. Typical incremental run on the real wiki: under a second.

The cloud setup script runs `wikipilot index-wiki` on every routine start so cloud runs always see fresh content. Locally you can run it after every batch of edits, or wire it into a pre-commit hook.

## MCP server (subagents talk to qmd through this)

qmd 0.1.2 doesn't ship an MCP server. [`scripts/qmd_mcp_server.py`](../scripts/qmd_mcp_server.py) is the small (~150-line) FastMCP-based shim that:

- Exposes a `qmd_search(query, top_k, rerank, filters_json)` tool that proxies to `qmd.core.collection.SqliteCollection.hybrid_search`.
- Exposes a `qmd_collection_info()` tool for diagnostics (doc count, embedding dim).
- Reads the DB path from the `WIKIPILOT_QMD_DB` env var (default: `.qmd/wiki.db` relative to the server's CWD).
- Opens a fresh qmd client per tool call (no caching) — necessary because FastMCP runs sync tools in anyio's threadpool and `sqlite3.Connection` is thread-affine.

### How the connector is wired (no UI registration needed)

Wikipilot ships a project-scoped `.mcp.json` at the repo root that registers the shim as a stdio MCP server. Claude Code (CLI, Cursor, and Cloud Routines) auto-loads it on every session that starts in the project.

`.mcp.json` (committed to git):

```json
{
  "mcpServers": {
    "wikipilot-qmd": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "scripts/qmd_mcp_server.py"],
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
```

`uv run` is used so the shim always picks up the project's `.venv` (which has `qmd`, `mcp`, `rank_bm25` installed via `uv sync --frozen --extra dev`). No global `pip install qmd` is required.

Project-scoped `.mcp.json` servers normally trigger a one-time approval prompt the first time you open the project. Wikipilot pre-approves `wikipilot-qmd` via `.claude/settings.json`:

```json
{
  "enabledMcpjsonServers": ["wikipilot-qmd"]
}
```

That keeps cloud routines from sitting on an approval prompt that no human is there to click.

> **Note:** the **claude.ai → Settings → Connectors** dialog ("Add custom connector") is for **remote, URL-based** MCP servers only. It does not accept stdio servers. Don't try to register `wikipilot-qmd` there — leave the dialog closed and let the project-scoped `.mcp.json` do its job.

### Verifying the connector loaded

In Cursor (or any Claude Code CLI):

- `Cmd/Ctrl-Shift-P → MCP: Show servers` should list `wikipilot-qmd` connected with **2 tools**: `qmd_search` and `qmd_collection_info`.
- In the agent panel, `Should be in your tools list as `mcp__wikipilot-qmd__qmd_search` and `mcp__wikipilot-qmd__qmd_collection_info`.

If the server doesn't appear, the most common cause is a stale `.venv` — run `uv sync --frozen --extra dev` from the repo root and reopen the editor.

### Local Windows caveat

Running the MCP server end-to-end against an MCP **client** on Windows (e.g. testing with the Python MCP SDK's `stdio_client`) currently hangs after the first `tools/call` due to a known stdio interaction between subprocess pipes, anyio, and FastMCP's threadpool. This does not affect:

- The server's correctness (unit + real-qmd integration tests cover the tool functions directly).
- Cloud routine usage (cloud env is Linux, where the issue doesn't manifest).
- Live use in Claude Code / Cursor (both connect via their own MCP transport that doesn't hit the Python `stdio_client` path).

If you need a local smoke test on Windows, exercise `qmd_collection_info()` — it returns immediately. For full end-to-end testing, defer to the cloud routine's first run.

## Verifying the local index is alive

A quick Python REPL check (with the venv active):

```python
from qmd.core.client import SqliteQmdClient
client = SqliteQmdClient(db_path=".qmd/wiki.db")
coll = client.collection("wikipilot")
info = coll.info()
print(f"docs={info.document_count} chunks={info.chunk_count} dim={info.embedding_dim}")
for h in coll.hybrid_search("parallel subagents", top_k=3):
    print(f"  {h.metadata.get('path')!r} score={h.score:.3f}")
client.close()
```

You should see your indexed pages with non-zero scores.

## Why qmd specifically

- Hybrid BM25 + vector means typo-tolerance + synonym-tolerance without an external API call.
- Local-only — no data leaves the machine.
- Sized for personal-wiki scale (hundreds to low thousands of pages); we'd revisit if your wiki grew past ~10k pages.

The trade-off: qmd doesn't ship an MCP server itself, so we maintain `scripts/qmd_mcp_server.py`. The shim is ~150 lines and unit-tested; the upstream coupling is minimal (just `qmd.core.client.SqliteQmdClient`).

## Troubleshooting

| Symptom | Fix |
|---|---|
| `wikipilot index-wiki` → `qmd not importable. Install with pip install qmd` | qmd isn't installed in your active interpreter. Activate the venv (`.\.venv\Scripts\Activate.ps1`), then `pip install qmd rank_bm25 mcp`. |
| `pytest` fails with `ModuleNotFoundError: No module named 'rank_bm25'` on qmd's pytest plugin | Same fix — `pip install rank_bm25`. Pinned in `pyproject.toml` so this should self-resolve after `pip install -e ".[dev]"`. |
| `qmd_search` returns empty / stale results | Re-index: `wikipilot index-wiki --full`. The full mode wipes the collection and re-embeds every file. |
| First `index-wiki` takes forever | One-time HF model download (~600 MB). Watch `~/.cache/huggingface/hub/` grow; subsequent runs reuse the cached weights. |
| `qmd_collection_info` reports zero docs after indexing | The MCP server is pointing at a different DB than `wikipilot index-wiki` wrote to. Set `WIKIPILOT_QMD_DB` in `.mcp.json`'s `env` block (or as a session env var). |
| `wikipilot-qmd` server not in the MCP list | Claude Code didn't discover `.mcp.json`. Confirm you opened the project at the repo root (not a parent dir), and that `.claude/settings.json` includes `wikipilot-qmd` in `enabledMcpjsonServers`. Restart the session. |
| Tried to add `wikipilot-qmd` in claude.ai → Settings → Connectors and it asks for a URL | That dialog is for **remote** MCP servers only. Cancel; our shim is stdio-based and is wired through `.mcp.json` automatically — no manual registration. |
