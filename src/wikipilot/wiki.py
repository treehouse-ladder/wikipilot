"""Wiki primitives: vault traversal, page I/O, frontmatter validation, wikilinks.

This module is the lowest layer above the filesystem. Everything above it
(``sources``, ``lint``, ``log``, ``deck``) goes through ``Vault`` and ``Page``
rather than touching paths directly so the test fixtures stay tractable.

Design notes
------------
- ``Vault`` is a thin wrapper around the wiki root directory; it owns the
  path-resolution rules so the rest of the codebase never hard-codes
  ``wiki/concepts/...``.
- ``Page`` wraps ``frontmatter.Post`` and adds typed access to the schema
  fields documented in ``CLAUDE.md`` (``last_updated``, ``last_verified``,
  ``freshness_window_days``, ``sources``).
- We deliberately keep the ``[[wikilink]]`` parser permissive: it accepts
  Obsidian's ``[[target|alias]]`` and ``[[target#section]]`` forms but always
  returns the resolved target slug.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import frontmatter

WIKI_DIRS: tuple[str, ...] = (
    "topics",
    "concepts",
    "entities",
    "comparisons",
    "sources",
    "answers",
    "reports",
    "decks",
    "assets",
)

VALID_KINDS: tuple[str, ...] = (
    "topic",
    "concept",
    "entity",
    "comparison",
    "source",
    "answer",
    "report",
)

REQUIRED_FRONTMATTER: tuple[str, ...] = (
    "title",
    "kind",
    "last_updated",
    "last_verified",
    "freshness_window_days",
    "sources",
)

WIKILINK_RE = re.compile(r"\[\[([^\[\]|#\n]+?)(?:#[^\[\]|\n]+?)?(?:\|[^\[\]\n]+?)?\]\]")


def slugify(text: str) -> str:
    """Return a URL/file-safe slug.

    Strips diacritics, lowercases, collapses non-alphanumerics into hyphens.
    Used for both wiki page slugs and source filenames.
    """
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_only.lower()
    hyphenated = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return hyphenated


def parse_wikilinks(text: str) -> list[str]:
    """Return the resolved targets of every ``[[link]]`` in ``text``.

    Aliases (``[[target|alias]]``) and section references (``[[target#h]]``)
    collapse to ``target``. Order is preserved; duplicates are kept.
    """
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(text)]


def parse_log_headings(log_text: str) -> list[tuple[str, str, str, str]]:
    """Parse every ``## [YYYY-MM-DD] kind | subject`` heading from ``log.md``.

    Returns a list of ``(date_str, kind, subject, raw_line)`` tuples in file
    order. Headings that do not match the schema are skipped; the
    ``check_log_format`` lint rule reports them separately.
    """
    pattern = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\]\s+(\w+)\s*\|\s*(.+)$", re.MULTILINE)
    return [
        (m.group(1), m.group(2), m.group(3).strip(), m.group(0)) for m in pattern.finditer(log_text)
    ]


@dataclass(frozen=True)
class Vault:
    """The wiki vault root and the standard subdirectories beneath it."""

    root: Path

    @classmethod
    def at(cls, root: Path | str) -> Vault:
        return cls(root=Path(root).resolve())

    @property
    def index_path(self) -> Path:
        return self.root / "index.md"

    @property
    def log_path(self) -> Path:
        return self.root / "log.md"

    def dir_for(self, kind: str) -> Path:
        if kind not in WIKI_DIRS:
            raise ValueError(f"Unknown vault subdirectory: {kind!r}")
        return self.root / kind

    def topic_dir(self, topic_id: str) -> Path:
        return self.root / "topics" / topic_id

    def topic_index(self, topic_id: str) -> Path:
        return self.topic_dir(topic_id) / "index.md"

    def topic_purpose(self, topic_id: str) -> Path:
        return self.topic_dir(topic_id) / "purpose.md"

    def assets_for(self, source_slug: str) -> Path:
        return self.root / "assets" / source_slug

    def page_path(self, kind: str, slug: str) -> Path:
        if kind == "topic":
            return self.topic_index(slug)
        if kind in {"concept", "entity", "comparison"}:
            return self.dir_for(kind + "s") / f"{slug}.md"
        if kind in {"source", "answer", "report"}:
            return self.dir_for(kind + "s") / f"{slug}.md"
        raise ValueError(f"Cannot derive page path for kind {kind!r}")

    def iter_markdown_files(self, *, include_topics: bool = True) -> Iterable[Path]:
        """Yield every ``.md`` file beneath the vault root.

        Skips dotfiles and ``.gitkeep``. Topics directory is included by
        default; pass ``include_topics=False`` to skip it.
        """
        for path in self.root.rglob("*.md"):
            if any(part.startswith(".") for part in path.parts):
                continue
            if not include_topics and "topics" in path.relative_to(self.root).parts:
                continue
            yield path


@dataclass
class Page:
    """A markdown page in the vault.

    Wraps a parsed ``frontmatter.Post`` plus the absolute path on disk. All
    schema-aware accessors normalize types (e.g. ``date`` strings become
    ``date`` objects) so callers can treat the API uniformly.
    """

    path: Path
    metadata: dict[str, Any]
    content: str

    @classmethod
    def read(cls, path: Path) -> Page:
        post = frontmatter.load(path)
        return cls(path=Path(path), metadata=dict(post.metadata), content=post.content)

    @classmethod
    def from_dict(cls, path: Path, metadata: dict[str, Any], content: str) -> Page:
        return cls(path=Path(path), metadata=dict(metadata), content=content)

    def write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        post = frontmatter.Post(self.content, **self.metadata)
        with self.path.open("wb") as handle:
            frontmatter.dump(post, handle)

    @property
    def title(self) -> str | None:
        value = self.metadata.get("title")
        return str(value) if value is not None else None

    @property
    def kind(self) -> str | None:
        value = self.metadata.get("kind")
        return str(value) if value is not None else None

    @property
    def sources(self) -> list[str]:
        raw = self.metadata.get("sources") or []
        if not isinstance(raw, list):
            raise WikiError(f"{self.path}: 'sources' must be a list, got {type(raw).__name__}")
        return [str(item) for item in raw]

    @property
    def last_updated(self) -> date | None:
        return _coerce_date(self.metadata.get("last_updated"))

    @property
    def last_verified(self) -> date | None:
        return _coerce_date(self.metadata.get("last_verified"))

    @property
    def freshness_window_days(self) -> int | None:
        value = self.metadata.get("freshness_window_days")
        if value is None:
            return None
        return int(value)

    @property
    def aliases(self) -> list[str]:
        """Obsidian-native ``aliases:`` frontmatter (Phase 9 Pattern C).

        Lets ``[[GPT-4]]``, ``[[GPT 4]]``, ``[[gpt4]]`` all resolve to the same
        page when the entity declares them. Returns an empty list when the
        key is absent. Non-string entries are coerced via ``str()`` so a YAML
        list of mixed types still produces something the lint can slugify.
        """
        raw = self.metadata.get("aliases") or []
        if not isinstance(raw, list):
            raise WikiError(
                f"{self.path}: 'aliases' must be a list of strings, got {type(raw).__name__}"
            )
        return [str(item) for item in raw]

    def wikilinks(self) -> list[str]:
        return parse_wikilinks(self.content)

    def bump_freshness(self, *, verified: bool, today: date | None = None) -> None:
        today = today or date.today()
        self.metadata["last_updated"] = today
        if verified:
            self.metadata["last_verified"] = today

    def is_stale(self, *, today: date | None = None, default_window: int = 30) -> bool:
        today = today or date.today()
        verified = self.last_verified
        if verified is None:
            return True
        window = (
            self.freshness_window_days if self.freshness_window_days is not None else default_window
        )
        return (today - verified).days > window

    def validate_frontmatter(self) -> list[str]:
        """Return human-readable validation errors; empty list means valid."""
        errors: list[str] = []
        for key in REQUIRED_FRONTMATTER:
            if key not in self.metadata:
                errors.append(f"missing required frontmatter key: {key!r}")
        if (kind := self.metadata.get("kind")) is not None and kind not in VALID_KINDS:
            errors.append(f"invalid kind {kind!r}; expected one of {VALID_KINDS}")
        for date_key in ("last_updated", "last_verified"):
            if date_key in self.metadata and _coerce_date(self.metadata[date_key]) is None:
                errors.append(f"{date_key!r} is not a valid YYYY-MM-DD date")
        if "freshness_window_days" in self.metadata:
            try:
                window = int(self.metadata["freshness_window_days"])
                if window <= 0:
                    errors.append("freshness_window_days must be a positive integer")
            except (TypeError, ValueError):
                errors.append("freshness_window_days must be an integer")
        if "sources" in self.metadata and not isinstance(self.metadata["sources"], list):
            errors.append("sources must be a list of [[wikilink]] strings")
        if "aliases" in self.metadata and not isinstance(self.metadata["aliases"], list):
            errors.append("aliases must be a list of strings")
        if self.metadata.get("kind") == "comparison":
            comparison_of = self.metadata.get("comparison_of")
            if not isinstance(comparison_of, list) or len(comparison_of) < 2:
                errors.append(
                    "comparison pages require 'comparison_of' as a list of at least 2 entity slugs"
                )
            compare_fields = self.metadata.get("compare_fields")
            if not isinstance(compare_fields, list) or len(compare_fields) < 1:
                errors.append(
                    "comparison pages require 'compare_fields' as a list of at least 1 field name"
                )
        return errors


class WikiError(RuntimeError):
    """Raised by wiki-layer helpers on schema or I/O violations."""


def _coerce_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None
