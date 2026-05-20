"""Tests for ``scripts/qmd_mcp_server.py``.

Exercises the tool callables directly (not over MCP transport) by injecting
a fake collection. This keeps tests offline and fast — no embedding model,
no qmd import, no SQLite.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import contextlib  # noqa: E402

import qmd_mcp_server  # noqa: E402
from qmd_mcp_server import (  # noqa: E402
    _hit_to_dict,
    _opt_float,
    _resolve_collection_name,
    _resolve_db_path,
    qmd_collection_info,
    qmd_search,
)


class _FakeHit:
    def __init__(
        self,
        *,
        text: str,
        score: float,
        bm25_score: float | None = None,
        vector_score: float | None = None,
        rerank_score: float | None = None,
        metadata: dict | None = None,
    ) -> None:
        self.text = text
        self.score = score
        self.bm25_score = bm25_score
        self.vector_score = vector_score
        self.rerank_score = rerank_score
        self.metadata = metadata or {}


class _FakeInfo:
    def __init__(self, *, name: str, document_count: int, chunk_count: int, embedding_dim: int):
        self.name = name
        self.document_count = document_count
        self.chunk_count = chunk_count
        self.embedding_dim = embedding_dim


class _FakeCollection:
    def __init__(self, hits: list[_FakeHit] | None = None, info: _FakeInfo | None = None) -> None:
        self._hits = hits or []
        self._info = info or _FakeInfo(
            name="wikipilot", document_count=0, chunk_count=0, embedding_dim=384
        )
        self.calls: list[dict[str, Any]] = []

    def hybrid_search(self, *, query, top_k, rerank, filters):
        self.calls.append({"query": query, "top_k": top_k, "rerank": rerank, "filters": filters})
        return list(self._hits)

    def info(self):
        return self._info


def _install_fake_collection(monkeypatch, coll: _FakeCollection) -> None:
    @contextlib.contextmanager
    def _fake_open():
        yield coll

    monkeypatch.setattr(qmd_mcp_server, "_open_collection", _fake_open)


class TestResolveDbPath:
    def test_defaults_to_qmd_wiki_db(self, monkeypatch) -> None:
        monkeypatch.delenv("WIKIPILOT_QMD_DB", raising=False)
        assert _resolve_db_path() == Path(".qmd") / "wiki.db"

    def test_honors_env_var(self, monkeypatch, tmp_path) -> None:
        custom = tmp_path / "custom.db"
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(custom))
        assert _resolve_db_path() == custom


class TestResolveCollectionName:
    def test_default(self, monkeypatch) -> None:
        monkeypatch.delenv("WIKIPILOT_QMD_COLLECTION", raising=False)
        assert _resolve_collection_name() == "wikipilot"

    def test_override(self, monkeypatch) -> None:
        monkeypatch.setenv("WIKIPILOT_QMD_COLLECTION", "alt")
        assert _resolve_collection_name() == "alt"


class TestQmdSearch:
    def test_returns_normalized_dicts(self, monkeypatch) -> None:
        coll = _FakeCollection(
            hits=[
                _FakeHit(
                    text="hello world",
                    score=0.9,
                    bm25_score=0.5,
                    vector_score=0.4,
                    rerank_score=None,
                    metadata={"path": "concepts/a.md", "mtime_ns": 1},
                ),
                _FakeHit(text="other", score=0.7, metadata={"path": "concepts/b.md"}),
            ]
        )
        _install_fake_collection(monkeypatch, coll)
        out = qmd_search("hello", top_k=5)
        assert len(out) == 2
        assert out[0]["path"] == "concepts/a.md"
        assert out[0]["score"] == pytest.approx(0.9)
        assert out[0]["bm25_score"] == pytest.approx(0.5)
        assert out[0]["vector_score"] == pytest.approx(0.4)
        assert out[0]["rerank_score"] is None
        assert out[0]["text"] == "hello world"
        assert out[0]["metadata"]["mtime_ns"] == 1
        assert coll.calls[0] == {
            "query": "hello",
            "top_k": 5,
            "rerank": False,
            "filters": None,
        }

    def test_empty_query_returns_empty(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        assert qmd_search("   ") == []
        assert coll.calls == []

    def test_top_k_clamped_to_max(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        qmd_search("q", top_k=9999)
        assert coll.calls[0]["top_k"] == 50

    def test_top_k_clamped_to_min(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        qmd_search("q", top_k=0)
        assert coll.calls[0]["top_k"] == 1

    def test_rerank_flag_forwarded(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        qmd_search("q", rerank=True)
        assert coll.calls[0]["rerank"] is True

    def test_filters_json_parsed(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        qmd_search("q", filters_json='{"path": "concepts/x.md"}')
        assert coll.calls[0]["filters"] == {"path": "concepts/x.md"}

    def test_invalid_filters_json_raises_clear_error(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        with pytest.raises(RuntimeError, match="not valid JSON"):
            qmd_search("q", filters_json="{bad json")

    def test_non_object_filters_json_raises(self, monkeypatch) -> None:
        coll = _FakeCollection()
        _install_fake_collection(monkeypatch, coll)
        with pytest.raises(RuntimeError, match="JSON object"):
            qmd_search("q", filters_json="[1, 2, 3]")


class TestQmdCollectionInfo:
    def test_returns_full_info_dict(self, monkeypatch) -> None:
        coll = _FakeCollection(
            info=_FakeInfo(name="wikipilot", document_count=16, chunk_count=49, embedding_dim=1024)
        )
        _install_fake_collection(monkeypatch, coll)
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(Path("custom.db").resolve()))
        out = qmd_collection_info()
        assert out["name"] == "wikipilot"
        assert out["document_count"] == 16
        assert out["chunk_count"] == 49
        assert out["embedding_dim"] == 1024
        assert out["db_path"].endswith("custom.db")


class TestOpenCollectionErrors:
    def test_missing_db_raises_clear_error(self, monkeypatch, tmp_path) -> None:
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(tmp_path / "nope.db"))

        class _FakeClient:
            def __init__(self, db_path):
                pytest.fail("should not be reached when DB doesn't exist")

        monkeypatch.setitem(
            sys.modules,
            "qmd.core.client",
            type("M", (), {"SqliteQmdClient": _FakeClient})(),
        )
        with (
            pytest.raises(RuntimeError, match="qmd index not found"),
            qmd_mcp_server._open_collection(),
        ):
            pass

    def test_qmd_import_failure_raises_runtime_error(self, monkeypatch, tmp_path) -> None:
        # Module exists in sys.modules but lacks SqliteQmdClient — Python raises
        # ImportError("cannot import name 'SqliteQmdClient'") which the shim
        # converts into a clear RuntimeError.
        db = tmp_path / "exists.db"
        db.write_bytes(b"")
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(db))
        stub_module = type("M", (), {})()
        monkeypatch.setitem(sys.modules, "qmd.core.client", stub_module)
        with (
            pytest.raises(RuntimeError, match="qmd is not importable"),
            qmd_mcp_server._open_collection(),
        ):
            pass

    def test_happy_path_yields_collection_and_closes_client(self, monkeypatch, tmp_path) -> None:
        db = tmp_path / "wiki.db"
        db.write_bytes(b"")  # existence check only; the fake client never reads it.
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(db))
        monkeypatch.setenv("WIKIPILOT_QMD_COLLECTION", "wikipilot")

        sentinel_collection = object()
        constructed: list[str] = []
        closed_flags: list[bool] = []

        class _FakeClient:
            def __init__(self, db_path: str) -> None:
                constructed.append(db_path)
                self._closed = False

            def collection(self, name: str) -> object:
                assert name == "wikipilot"
                return sentinel_collection

            def close(self) -> None:
                self._closed = True
                closed_flags.append(True)

        monkeypatch.setitem(
            sys.modules,
            "qmd.core.client",
            type("M", (), {"SqliteQmdClient": _FakeClient})(),
        )

        with qmd_mcp_server._open_collection() as coll:
            assert coll is sentinel_collection
        assert constructed == [str(db.resolve())]
        assert closed_flags == [True]

    def test_close_failure_is_swallowed(self, monkeypatch, tmp_path) -> None:
        # The finally block uses contextlib.suppress so a flaky close() must
        # not propagate to callers.
        db = tmp_path / "wiki.db"
        db.write_bytes(b"")
        monkeypatch.setenv("WIKIPILOT_QMD_DB", str(db))

        class _FakeClient:
            def __init__(self, db_path: str) -> None:
                pass

            def collection(self, name: str) -> object:
                return object()

            def close(self) -> None:
                raise RuntimeError("closing exploded")

        monkeypatch.setitem(
            sys.modules,
            "qmd.core.client",
            type("M", (), {"SqliteQmdClient": _FakeClient})(),
        )
        with qmd_mcp_server._open_collection() as coll:
            assert coll is not None


class TestHitToDict:
    def test_handles_missing_attrs_gracefully(self) -> None:
        class Empty:
            text = ""
            score = 0.0
            metadata = {}

        out = _hit_to_dict(Empty())
        assert out["path"] is None
        assert out["score"] == 0.0
        assert out["bm25_score"] is None
        assert out["text"] == ""

    def test_non_dict_but_dict_convertible_metadata_is_normalized(self) -> None:
        # Some qmd backends may return metadata as an iterable of (k, v) pairs
        # rather than a dict. The shim must coerce that into a real dict.
        class Hit:
            text = "x"
            score = 0.5
            metadata = [("path", "concepts/x.md"), ("kind", "concept")]

        out = _hit_to_dict(Hit())
        assert out["path"] == "concepts/x.md"
        assert out["metadata"] == {"path": "concepts/x.md", "kind": "concept"}

    def test_non_string_path_in_metadata_becomes_none(self) -> None:
        class Hit:
            text = ""
            score = 0.0
            metadata = {"path": 123}

        out = _hit_to_dict(Hit())
        assert out["path"] is None


class TestOptFloat:
    def test_none_passes_through(self) -> None:
        assert _opt_float(None) is None

    def test_int_coerced(self) -> None:
        assert _opt_float(3) == 3.0

    def test_garbage_becomes_none(self) -> None:
        assert _opt_float("not a float") is None


class TestToolRegistration:
    """Guard against silent regressions in the @mcp.tool() decorations.

    FastMCP's ToolManager exposes ``list_tools()`` as a public API; we use it
    rather than the underlying ``_tools`` dict so the test survives minor
    internal refactors of FastMCP.
    """

    def test_both_tools_registered(self) -> None:
        tools = qmd_mcp_server.mcp._tool_manager.list_tools()
        names = {t.name for t in tools}
        assert "qmd_search" in names
        assert "qmd_collection_info" in names

    def test_search_tool_signature_has_expected_params(self) -> None:
        search = qmd_mcp_server.mcp._tool_manager.get_tool("qmd_search")
        assert search is not None
        params = search.parameters.get("properties", {})
        assert "query" in params
        assert "top_k" in params
        assert "rerank" in params
        assert "filters_json" in params
