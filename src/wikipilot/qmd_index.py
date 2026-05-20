"""Index the wiki into a qmd-backed hybrid BM25 + vector collection.

qmd 0.1.2 (https://github.com/chengzhag/qmd-py) is an on-device hybrid search
library. It exposes a ``SqliteQmdClient`` Python API but does NOT ship an MCP
server — the MCP shim that subagents talk to is in ``scripts/qmd_mcp_server.py``
and reads from the same SQLite DB this module writes to.

This module:

- Detects whether qmd is importable (replacing the old "qmd on PATH" check).
- Indexes every markdown file under a vault into a SQLite-backed collection.
- Tracks ``mtime_ns`` per document in metadata so incremental runs only
  re-embed files that actually changed.
- Cleans up orphan documents whose source file no longer exists.

The indexer uses the Python API directly (no subprocess) so it's fast,
testable with an injected fake client, and avoids the cost of spinning up
a new Python interpreter per document.
"""

from __future__ import annotations

import contextlib
import importlib.util
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from qmd.core.client import SqliteQmdClient

DEFAULT_COLLECTION = "wikipilot"
DEFAULT_DB_DIR = ".qmd"
DEFAULT_DB_NAME = "wiki.db"


class QmdError(RuntimeError):
    """Raised on unrecoverable qmd indexing failure (e.g. corrupt DB)."""


@dataclass(frozen=True)
class IndexResult:
    """Outcome of an :func:`index_vault` call.

    The legacy ``indexed_files`` field is preserved for backward compatibility
    with callers that only want a single count; new code should read the
    granular ``added``/``updated``/``deleted``/``skipped`` counters.
    """

    ok: bool
    qmd_available: bool
    indexed_files: int
    added: int
    updated: int
    deleted: int
    skipped: int
    message: str
    db_path: Path | None = None


class _ClientFactory(Protocol):
    def __call__(self, db_path: str) -> Any: ...


def qmd_available() -> bool:
    """Return ``True`` iff the ``qmd`` package is importable in this interpreter.

    Replaces the legacy ``shutil.which("qmd")`` check: we now talk to qmd via
    its Python API, not its CLI, so PATH is irrelevant.
    """
    return importlib.util.find_spec("qmd") is not None


def default_db_path(vault_root: Path) -> Path:
    """Default qmd DB location: ``<vault_root.parent>/.qmd/wiki.db``."""
    return Path(vault_root).resolve().parent / DEFAULT_DB_DIR / DEFAULT_DB_NAME


def index_vault(
    vault_root: Path,
    *,
    full: bool = False,
    db_path: Path | None = None,
    collection_name: str = DEFAULT_COLLECTION,
    client_factory: _ClientFactory | None = None,
) -> IndexResult:
    """Index every ``.md`` file under ``vault_root`` into the qmd collection.

    Incremental mode (default): for each file, compare its ``mtime_ns`` to the
    value stored in the document's metadata. Skip if unchanged; otherwise
    upsert. Also delete documents whose source file no longer exists.

    Full mode (``full=True``): drop and recreate the collection, then add
    every file from scratch. Use after schema changes, when corruption is
    suspected, or when the embedding model is upgraded.

    ``client_factory`` is injectable so unit tests can swap in an in-memory
    fake without pulling in qmd or downloading embedding weights.
    """
    if not qmd_available() and client_factory is None:
        return IndexResult(
            ok=False,
            qmd_available=False,
            indexed_files=0,
            added=0,
            updated=0,
            deleted=0,
            skipped=0,
            message=(
                "qmd not importable. Install with `pip install qmd` and re-run; "
                "see docs/qmd-setup.md for the local-dev setup."
            ),
        )

    vault_root = Path(vault_root).resolve()
    if db_path is None:
        db_path = default_db_path(vault_root)
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    factory = client_factory or _default_client_factory
    try:
        client = factory(db_path=str(db_path))
    except Exception as exc:
        raise QmdError(f"failed to open qmd db at {db_path}: {exc}") from exc

    try:
        if full:
            # Collection might not exist yet; that's fine for --full.
            with contextlib.suppress(Exception):
                client.delete_collection(collection_name)

        coll = client.collection(collection_name)

        existing_ids = set(coll.list_documents()) if not full else set()
        existing_meta: dict[str, dict[str, Any]] = {}
        for doc_id in existing_ids:
            doc = coll.get_document(doc_id)
            if doc is None:
                continue
            meta = doc.get("metadata") or {}
            if isinstance(meta, dict):
                existing_meta[doc_id] = meta

        files = sorted(_iter_vault_markdown(vault_root))
        wanted_ids: set[str] = set()
        added = updated = skipped = 0

        for file_path in files:
            doc_id = file_path.relative_to(vault_root).as_posix()
            wanted_ids.add(doc_id)
            try:
                mtime_ns = file_path.stat().st_mtime_ns
            except OSError:
                continue

            prior = existing_meta.get(doc_id)
            if not full and prior is not None and prior.get("mtime_ns") == mtime_ns:
                skipped += 1
                continue

            try:
                markdown = file_path.read_text(encoding="utf-8")
            except OSError:
                continue

            metadata = {"path": doc_id, "mtime_ns": mtime_ns}
            coll.add_document(document_id=doc_id, markdown=markdown, metadata=metadata)
            if prior is None:
                added += 1
            else:
                updated += 1

        deleted = 0
        for doc_id in existing_ids - wanted_ids:
            coll.delete_document(doc_id)
            deleted += 1

        message = (
            f"{len(files)} file(s) on disk; "
            f"added {added}, updated {updated}, deleted {deleted}, skipped {skipped} "
            f"(db: {db_path})"
        )
        return IndexResult(
            ok=True,
            qmd_available=True,
            indexed_files=len(files),
            added=added,
            updated=updated,
            deleted=deleted,
            skipped=skipped,
            message=message,
            db_path=db_path,
        )
    finally:
        with contextlib.suppress(Exception):
            client.close()


def _default_client_factory(db_path: str) -> SqliteQmdClient:
    """Construct the real qmd client. Imported lazily so unit tests don't pay
    the cost of loading the embedding model.
    """
    from qmd.core.client import SqliteQmdClient

    return SqliteQmdClient(db_path=db_path)


def _iter_vault_markdown(vault_root: Path) -> Iterable[Path]:
    """Yield every indexable ``.md`` file under ``vault_root``.

    Mirrors :meth:`wikipilot.wiki.Vault.iter_markdown_files`'s rules (skip
    dotfile-prefixed directories and files) without importing ``Vault`` so
    this module stays usable from environments that haven't fully imported
    the wiki primitives (e.g. the MCP server).
    """
    for path in Path(vault_root).rglob("*.md"):
        if any(part.startswith(".") for part in path.parts):
            continue
        yield path
