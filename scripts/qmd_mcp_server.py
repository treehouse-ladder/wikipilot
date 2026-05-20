"""qmd MCP server: expose `qmd_search` over stdio to MCP-capable clients.

qmd 0.1.2 doesn't ship its own MCP server, so we provide a tiny shim that
wraps :mod:`qmd.core.client` and serves as a standard MCP tool over stdio.
Register this in ``claude.ai → Settings → Connectors → Add MCP server`` (or
in any other MCP client) with::

    Command: python
    Args:    scripts/qmd_mcp_server.py

The server reads the DB path from ``WIKIPILOT_QMD_DB`` env var, defaulting
to ``.qmd/wiki.db`` relative to the current working directory (which should
be the repo root, the same place ``wikipilot index-wiki`` wrote it).

Tools exposed:

- ``qmd_search(query, top_k=10, rerank=False, filters_json=None)`` — hybrid
  BM25 + vector search over the indexed wiki. Returns one dict per hit with
  ``path``, ``score``, ``bm25_score``, ``vector_score``, ``rerank_score``,
  ``text``, and ``metadata``.
- ``qmd_collection_info()`` — diagnostic: doc count, chunk count, embedding
  dimension. Useful for ``preflight``-style "is the index alive?" checks.

The qmd client (and its embedding model) loads lazily on the first tool
call so server startup is fast and we don't pay the model-load cost when
the client connects but never calls a tool.
"""

from __future__ import annotations

import contextlib
import json
import os
import sys
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

# FastMCP serves JSON-RPC over stdout. Anything that writes to stdout —
# loguru logs from qmd, HuggingFace progress bars, tqdm bars, transformers
# warnings — will corrupt the framing and break the client. Silence them
# BEFORE importing qmd. These are harmless when set unnecessarily.
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
os.environ.setdefault("TQDM_DISABLE", "1")
os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")

try:
    from loguru import logger as _loguru_logger

    _loguru_logger.remove()
    _loguru_logger.add(sys.stderr, level="WARNING")
except ImportError:
    pass

from mcp.server.fastmcp import FastMCP

DEFAULT_COLLECTION = "wikipilot"
DEFAULT_DB_PATH = Path(".qmd") / "wiki.db"

mcp = FastMCP("wikipilot-qmd")


def _resolve_db_path() -> Path:
    raw = os.environ.get("WIKIPILOT_QMD_DB")
    return Path(raw) if raw else DEFAULT_DB_PATH


def _resolve_collection_name() -> str:
    return os.environ.get("WIKIPILOT_QMD_COLLECTION", DEFAULT_COLLECTION)


@contextlib.contextmanager
def _open_collection() -> Iterator[Any]:
    """Open a fresh qmd client + collection for the duration of one call.

    We deliberately do NOT cache the client. FastMCP runs sync tools in
    anyio's threadpool, and sqlite3 connections are thread-affine — a
    cached connection used from a different worker thread on a later tool
    call hangs indefinitely. Constructing per-call is cheap once the
    sentence-transformers model is loaded (which happens at process
    startup the first time and is then class-cached).

    Raises ``RuntimeError`` with a clear message when qmd isn't importable
    or the DB doesn't exist, so MCP clients see a tool error rather than
    a Python traceback.
    """
    try:
        from qmd.core.client import SqliteQmdClient
    except ImportError as exc:
        raise RuntimeError(
            "qmd is not importable in this Python. Install with `pip install qmd` and re-run."
        ) from exc
    db_path = _resolve_db_path().resolve()
    if not db_path.exists():
        raise RuntimeError(
            f"qmd index not found at {db_path}. "
            "Run `wikipilot index-wiki` once before starting the server."
        )
    client = SqliteQmdClient(db_path=str(db_path))
    try:
        yield client.collection(_resolve_collection_name())
    finally:
        with contextlib.suppress(Exception):
            client.close()


@mcp.tool()
def qmd_search(
    query: str,
    top_k: int = 10,
    rerank: bool = False,
    filters_json: str | None = None,
) -> list[dict[str, Any]]:
    """Hybrid BM25 + vector search over the wikipilot qmd index.

    Args:
        query: Natural-language query string.
        top_k: Number of hits to return (default 10, max 50).
        rerank: When true, apply qmd's cross-encoder rerank (slower).
        filters_json: Optional JSON string of metadata filters,
            e.g. ``{"path": "topics/agentic-coding/index.md"}``.

    Returns:
        One dict per hit with ``path`` (the document id, i.e. the
        vault-relative POSIX path), ``score`` (blended ranking score),
        ``bm25_score``, ``vector_score``, ``rerank_score``, ``text``
        (the matched chunk text), and ``metadata`` (the doc's metadata
        as stored at index time).
    """
    if not query.strip():
        return []
    top_k = max(1, min(int(top_k), 50))
    filters: dict[str, Any] | None = None
    if filters_json:
        try:
            parsed = json.loads(filters_json)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"filters_json is not valid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise RuntimeError("filters_json must decode to a JSON object")
        filters = parsed
    with _open_collection() as coll:
        hits: Iterable[Any] = coll.hybrid_search(
            query=query,
            top_k=top_k,
            rerank=rerank,
            filters=filters,
        )
        return [_hit_to_dict(h) for h in hits]


@mcp.tool()
def qmd_collection_info() -> dict[str, Any]:
    """Return diagnostic info about the indexed collection.

    Returns:
        ``{name, document_count, chunk_count, embedding_dim, db_path}``.
    """
    with _open_collection() as coll:
        info = coll.info()
    return {
        "name": getattr(info, "name", _resolve_collection_name()),
        "document_count": getattr(info, "document_count", None),
        "chunk_count": getattr(info, "chunk_count", None),
        "embedding_dim": getattr(info, "embedding_dim", None),
        "db_path": str(_resolve_db_path().resolve()),
    }


def _hit_to_dict(hit: Any) -> dict[str, Any]:
    metadata = getattr(hit, "metadata", None) or {}
    if not isinstance(metadata, dict):
        metadata = dict(metadata) if metadata else {}
    return {
        "path": metadata.get("path") if isinstance(metadata.get("path"), str) else None,
        "score": float(getattr(hit, "score", 0.0) or 0.0),
        "bm25_score": _opt_float(getattr(hit, "bm25_score", None)),
        "vector_score": _opt_float(getattr(hit, "vector_score", None)),
        "rerank_score": _opt_float(getattr(hit, "rerank_score", None)),
        "text": getattr(hit, "text", "") or "",
        "metadata": metadata,
    }


def _opt_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main() -> None:
    """Entry point. Runs the server over stdio (the MCP default).

    Local Windows note: end-to-end testing of this server with the Python
    MCP SDK's ``stdio_client`` may hang on ``tools/call`` because of a
    known stdio interaction between subprocess pipes, anyio, and FastMCP's
    threadpool. The server is correct (covered by unit tests) and works
    in the cloud routine environment (Linux); the limitation only affects
    Python-MCP-SDK-based local smoke tests on Windows. Claude Code and
    Cursor connect to this server via their own MCP transports and are
    not affected.
    """
    mcp.run()


if __name__ == "__main__":
    sys.exit(main() or 0)
