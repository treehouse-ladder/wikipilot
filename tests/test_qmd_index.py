"""Tests for :mod:`wikipilot.qmd_index`.

Uses an in-memory fake client/collection so the tests run without qmd's
embedding model and without touching SQLite. The fake honors the same
contract :func:`index_vault` relies on:

- ``add_document(document_id, markdown, metadata)`` is an upsert.
- ``get_document(document_id)`` returns ``{id, markdown, metadata, chunk_count}``.
- ``list_documents()`` returns a list of document ids.
- ``delete_document(document_id)`` removes the doc.
- ``client.collection(name)`` returns the same collection per name.
- ``client.delete_collection(name)`` wipes it.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from wikipilot.qmd_index import (
    DEFAULT_COLLECTION,
    IndexResult,
    QmdError,
    default_db_path,
    index_vault,
    qmd_available,
)


class _FakeCollection:
    def __init__(self) -> None:
        self._docs: dict[str, dict] = {}
        # Optional: ids in this set will be reported by list_documents but
        # get_document() returns None — simulates a torn DB / stale index.
        self.get_returns_none_for: set[str] = set()
        # Optional: ids in this set will be in list_documents() but get_document()
        # returns a doc with a non-dict metadata — exercises the type check.
        self.return_non_dict_metadata_for: set[str] = set()

    def add_document(self, document_id: str, markdown: str, metadata: dict | None = None) -> None:
        # Re-adding clears any synthetic "stale entry" flag — once the indexer
        # has written the doc, get_document should return real data.
        self.get_returns_none_for.discard(document_id)
        self.return_non_dict_metadata_for.discard(document_id)
        self._docs[document_id] = {
            "id": document_id,
            "markdown": markdown,
            "metadata": dict(metadata or {}),
            "chunk_count": 1,
        }

    def get_document(self, document_id: str) -> dict | None:
        if document_id in self.get_returns_none_for:
            return None
        if document_id in self.return_non_dict_metadata_for:
            return {
                "id": document_id,
                "markdown": "",
                "metadata": "not-a-dict",
                "chunk_count": 0,
            }
        return self._docs.get(document_id)

    def list_documents(self) -> list[str]:
        # Include the synthetic ids so the indexer sees them as "existing".
        ids = set(self._docs) | self.get_returns_none_for | self.return_non_dict_metadata_for
        return sorted(ids)

    def delete_document(self, document_id: str) -> None:
        self._docs.pop(document_id, None)
        self.get_returns_none_for.discard(document_id)
        self.return_non_dict_metadata_for.discard(document_id)


class _FakeClient:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._collections: dict[str, _FakeCollection] = {}
        self.closed = False

    def collection(self, name: str) -> _FakeCollection:
        return self._collections.setdefault(name, _FakeCollection())

    def delete_collection(self, name: str) -> None:
        self._collections.pop(name, None)

    def close(self) -> None:
        self.closed = True


def _make_factory() -> tuple[list[_FakeClient], object]:
    """Return (list-of-clients-created, factory-callable)."""
    created: list[_FakeClient] = []

    def factory(db_path: str) -> _FakeClient:
        client = _FakeClient(db_path)
        created.append(client)
        return client

    return created, factory


def _make_vault(tmp_path: Path, files: dict[str, str]) -> Path:
    """Materialize ``files`` (relpath -> body) under a fresh vault root."""
    vault = tmp_path / "wiki"
    vault.mkdir()
    for relpath, body in files.items():
        full = vault / relpath
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return vault


class TestQmdAvailable:
    def test_returns_bool(self) -> None:
        assert isinstance(qmd_available(), bool)


class TestDefaultDbPath:
    def test_under_repo_root(self, tmp_path: Path) -> None:
        vault = tmp_path / "wiki"
        vault.mkdir()
        assert default_db_path(vault) == tmp_path.resolve() / ".qmd" / "wiki.db"


class TestIndexVaultMissingQmd:
    def test_no_client_factory_and_no_qmd_returns_clear_message(
        self, tmp_path: Path, monkeypatch
    ) -> None:
        monkeypatch.setattr("wikipilot.qmd_index.qmd_available", lambda: False)
        result = index_vault(tmp_path)
        assert isinstance(result, IndexResult)
        assert result.ok is False
        assert result.qmd_available is False
        assert "qmd not importable" in result.message


class TestIndexVaultIncremental:
    def test_empty_vault_creates_collection_and_indexes_nothing(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {})
        _, factory = _make_factory()
        result = index_vault(vault, client_factory=factory)
        assert result.ok is True
        assert result.indexed_files == 0
        assert result.added == 0
        assert result.deleted == 0
        assert result.db_path == default_db_path(vault)

    def test_adds_every_file_on_first_run(self, tmp_path: Path) -> None:
        vault = _make_vault(
            tmp_path,
            {
                "index.md": "# Index",
                "concepts/a.md": "# A",
                "topics/x/index.md": "# Topic X",
            },
        )
        created, factory = _make_factory()
        result = index_vault(vault, client_factory=factory)
        assert result.ok is True
        assert result.added == 3
        assert result.updated == 0
        assert result.deleted == 0
        assert result.skipped == 0
        coll = created[0].collection(DEFAULT_COLLECTION)
        assert sorted(coll.list_documents()) == [
            "concepts/a.md",
            "index.md",
            "topics/x/index.md",
        ]

    def test_unchanged_file_is_skipped_on_second_run(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {"a.md": "# A"})
        created, factory = _make_factory()
        index_vault(vault, client_factory=factory)
        kept_client = created[0]

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        result2 = index_vault(vault, client_factory=kept_factory)
        assert result2.added == 0
        assert result2.updated == 0
        assert result2.deleted == 0
        assert result2.skipped == 1

    def test_modified_file_is_updated(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {"a.md": "# A v1"})
        created, factory = _make_factory()
        index_vault(vault, client_factory=factory)
        # Re-use the same in-memory client so we see the persisted state.
        kept_client = created[0]

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        (vault / "a.md").write_text("# A v2", encoding="utf-8")
        import os
        import time

        time.sleep(0.01)
        os.utime(vault / "a.md", None)
        result2 = index_vault(vault, client_factory=kept_factory)
        assert result2.added == 0
        assert result2.updated == 1
        assert result2.skipped == 0
        coll = kept_client.collection(DEFAULT_COLLECTION)
        assert coll.get_document("a.md")["markdown"] == "# A v2"

    def test_removed_file_is_deleted(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {"a.md": "# A", "b.md": "# B"})
        created, factory = _make_factory()
        index_vault(vault, client_factory=factory)
        kept_client = created[0]

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        (vault / "b.md").unlink()
        result2 = index_vault(vault, client_factory=kept_factory)
        assert result2.added == 0
        assert result2.updated == 0
        assert result2.deleted == 1
        coll = kept_client.collection(DEFAULT_COLLECTION)
        assert coll.list_documents() == ["a.md"]

    def test_dotfile_dirs_are_skipped(self, tmp_path: Path) -> None:
        vault = _make_vault(
            tmp_path,
            {
                "a.md": "# A",
                ".obsidian/workspace.md": "# config",
                ".qmd/index/state.md": "# state",
            },
        )
        created, factory = _make_factory()
        result = index_vault(vault, client_factory=factory)
        assert result.added == 1
        coll = created[0].collection(DEFAULT_COLLECTION)
        assert coll.list_documents() == ["a.md"]


class TestIndexVaultFull:
    def test_full_drops_collection_first(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {"a.md": "# A", "b.md": "# B"})
        created, factory = _make_factory()
        index_vault(vault, client_factory=factory)
        kept_client = created[0]

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        (vault / "c.md").write_text("# C", encoding="utf-8")
        result = index_vault(vault, full=True, client_factory=kept_factory)
        assert result.added == 3
        assert result.updated == 0
        assert result.skipped == 0
        coll = kept_client.collection(DEFAULT_COLLECTION)
        assert sorted(coll.list_documents()) == ["a.md", "b.md", "c.md"]


class TestIndexVaultErrors:
    def test_factory_failure_wraps_in_qmd_error(self, tmp_path: Path) -> None:
        vault = _make_vault(tmp_path, {"a.md": "# A"})

        def boom(db_path: str) -> _FakeClient:
            raise RuntimeError("disk full")

        with pytest.raises(QmdError, match="failed to open qmd db"):
            index_vault(vault, client_factory=boom)

    def test_get_document_returning_none_is_tolerated(self, tmp_path: Path) -> None:
        # Pre-seed a client whose collection lists a stale id but returns None
        # from get_document. The indexer must skip that prior-meta lookup
        # without crashing, and the file should be re-added.
        vault = _make_vault(tmp_path, {"a.md": "# A"})
        kept_client = _FakeClient(db_path=str(default_db_path(vault)))
        coll = kept_client.collection(DEFAULT_COLLECTION)
        coll.get_returns_none_for.add("a.md")

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        result = index_vault(vault, client_factory=kept_factory)
        assert result.ok is True
        # Treated as a new doc because prior metadata couldn't be read.
        assert result.added == 1
        assert result.updated == 0
        assert kept_client.collection(DEFAULT_COLLECTION).get_document("a.md") is not None

    def test_non_dict_prior_metadata_is_tolerated(self, tmp_path: Path) -> None:
        # Same shape as above but get_document returns a doc whose metadata
        # is a string, not a dict — the indexer must skip the mtime check
        # rather than crash.
        vault = _make_vault(tmp_path, {"a.md": "# A"})
        kept_client = _FakeClient(db_path=str(default_db_path(vault)))
        coll = kept_client.collection(DEFAULT_COLLECTION)
        coll.return_non_dict_metadata_for.add("a.md")

        def kept_factory(db_path: str) -> _FakeClient:
            return kept_client

        result = index_vault(vault, client_factory=kept_factory)
        assert result.ok is True
        # The id was in list_documents() but had no dict metadata, so
        # existing_meta has no entry for it — re-added as a new doc.
        assert result.added == 1


class TestIndexVaultIOErrors:
    """OSError on file metadata or read should not crash the whole run.

    The indexer is meant to be resilient: a single un-statable / un-readable
    file is logged-and-skipped, the rest of the vault is still indexed.
    Easiest deterministic way to exercise these branches is to monkeypatch
    Path.stat / Path.read_text with a path-aware side effect.
    """

    def test_stat_oserror_skips_file(self, tmp_path: Path, monkeypatch) -> None:
        vault = _make_vault(tmp_path, {"good.md": "# Good", "bad.md": "# Bad"})
        real_stat = Path.stat

        def flaky_stat(self, *args, **kwargs):
            if self.name == "bad.md":
                raise OSError("stat failed")
            return real_stat(self, *args, **kwargs)

        monkeypatch.setattr(Path, "stat", flaky_stat)

        created, factory = _make_factory()
        result = index_vault(vault, client_factory=factory)
        assert result.ok is True
        # Only good.md made it in; bad.md was skipped at the stat() step.
        assert result.added == 1
        coll = created[0].collection(DEFAULT_COLLECTION)
        assert coll.list_documents() == ["good.md"]

    def test_read_text_oserror_skips_file(self, tmp_path: Path, monkeypatch) -> None:
        vault = _make_vault(tmp_path, {"good.md": "# Good", "bad.md": "# Bad"})
        real_read = Path.read_text

        def flaky_read(self, *args, **kwargs):
            if self.name == "bad.md":
                raise OSError("read failed")
            return real_read(self, *args, **kwargs)

        monkeypatch.setattr(Path, "read_text", flaky_read)

        created, factory = _make_factory()
        result = index_vault(vault, client_factory=factory)
        assert result.ok is True
        # bad.md statted ok but failed to read — it's neither added nor crashed.
        assert result.added == 1
        coll = created[0].collection(DEFAULT_COLLECTION)
        assert coll.list_documents() == ["good.md"]


class TestIndexResultDataclass:
    def test_legacy_indexed_files_field_preserved(self) -> None:
        r = IndexResult(
            ok=True,
            qmd_available=True,
            indexed_files=3,
            added=2,
            updated=1,
            deleted=0,
            skipped=0,
            message="ok",
        )
        assert r.indexed_files == 3
        assert r.added == 2
