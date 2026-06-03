"""Real-qmd integration tests.

These tests exercise the actual qmd Python API (and through it,
sentence-transformers + torch + the Qwen embedding model) against a tiny
on-disk vault, then drive ``qmd_search`` from ``scripts/qmd_mcp_server.py``
to confirm the round-trip.

Skipped when qmd isn't importable (covers CI without the heavy deps).
Marked ``slow`` because the first run downloads + loads the embedding model
(~30s); subsequent runs reuse the HF cache.

Run only the fast tests::

    pytest -m "not slow"

Run integration tests explicitly::

    pytest -m integration
"""

from __future__ import annotations

from pathlib import Path

import pytest

from wikipilot.qmd_index import index_vault, qmd_available

pytestmark = [
    pytest.mark.skipif(not qmd_available(), reason="qmd not installed"),
    pytest.mark.slow,
    pytest.mark.integration,
]


@pytest.fixture
def tiny_vault(tmp_path: Path) -> tuple[Path, Path]:
    """Create a tiny vault with two distinguishable docs, return (vault, db_path)."""
    vault = tmp_path / "wiki"
    vault.mkdir()
    (vault / "attention.md").write_text(
        "# Multi-head attention\n\n"
        "Multi-head attention layers project queries, keys, and values "
        "through learned linear maps before computing scaled dot-product "
        "attention in parallel across heads.\n",
        encoding="utf-8",
    )
    (vault / "tokenizer.md").write_text(
        "# Byte-pair encoding tokenizer\n\n"
        "Byte-pair encoding (BPE) merges the most frequent adjacent token "
        "pairs iteratively to build a sub-word vocabulary suited to "
        "open-vocabulary text.\n",
        encoding="utf-8",
    )
    db = tmp_path / ".qmd" / "test.db"
    return vault, db


def test_real_index_then_search(
    tiny_vault: tuple[Path, Path], monkeypatch: pytest.MonkeyPatch
) -> None:
    vault, db = tiny_vault

    try:
        result = index_vault(vault, db_path=db)
    except OSError as exc:
        if "huggingface.co" in str(exc):
            pytest.skip(f"HuggingFace not reachable (network/rate-limit): {exc}")
        raise
    assert result.ok is True
    assert result.added == 2
    assert result.updated == 0
    assert result.deleted == 0
    assert db.exists()

    # Drive qmd_search against the built DB via WIKIPILOT_QMD_DB.
    monkeypatch.setenv("WIKIPILOT_QMD_DB", str(db))

    import qmd_mcp_server

    info = qmd_mcp_server.qmd_collection_info()
    assert info["document_count"] == 2
    assert info["embedding_dim"] is not None and info["embedding_dim"] > 0

    hits = qmd_mcp_server.qmd_search("attention heads", top_k=5)
    assert hits, "expected at least one hit for an obviously-matching query"
    paths = [h["path"] for h in hits]
    # The attention page should rank above the tokenizer page for this query.
    assert "attention.md" in paths
    top = hits[0]
    assert top["path"] == "attention.md"
    assert top["score"] > 0


def test_real_incremental_skip_on_unchanged(
    tiny_vault: tuple[Path, Path],
) -> None:
    vault, db = tiny_vault
    try:
        first = index_vault(vault, db_path=db)
    except OSError as exc:
        if "huggingface.co" in str(exc):
            pytest.skip(f"HuggingFace not reachable (network/rate-limit): {exc}")
        raise
    assert first.added == 2
    assert first.skipped == 0

    second = index_vault(vault, db_path=db)
    assert second.added == 0
    assert second.updated == 0
    assert second.deleted == 0
    assert second.skipped == 2
