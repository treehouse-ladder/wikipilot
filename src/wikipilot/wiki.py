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
import shutil
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass, field
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


# ---------------------------------------------------------------------------
# Vault skeletons (shared between ``init-vault`` and ``reset-vault``)
# ---------------------------------------------------------------------------

INDEX_SKELETON = """# Index

The catalog of every page in this wiki.

This file is **LLM-write, human-read**.

## Topics

_(none yet)_

## Concepts

_(none yet)_

## Entities

_(none yet)_

## Comparisons

_(none yet)_

## Sources

_(none yet)_

## Answers

_(none yet)_

## Reports

_(none yet)_
"""

LOG_SKELETON_TEMPLATE = """# Log

Chronological, append-only record of every routine run. Parseable with `grep "^## \\[" wiki/log.md`.

This file is **LLM-write, human-read**.

---

## [{date}] manual | bootstrap

Empty wiki initialized.
"""


def render_log_skeleton(today: date | None = None) -> str:
    """Return the canonical ``log.md`` skeleton string for today's date."""
    today = today or date.today()
    return LOG_SKELETON_TEMPLATE.format(date=today.isoformat())


# ---------------------------------------------------------------------------
# Obsidian config seeding (default initial state for forkers/fresh clones)
# ---------------------------------------------------------------------------
#
# Some files under ``wiki/.obsidian/`` (notably ``graph.json``) mutate on every
# Obsidian launch — zoom scale jitters, the collapse-filter toggle flips when
# any panel is opened — which produces noisy diffs that conflict with merges.
# We solve this by:
#
# 1. ``.gitignore`` excludes the mutating file itself (``graph.json``), so a
#    user's local state is never replaced by a pull.
# 2. We track a sibling template (``graph.template.json``) that carries the
#    canonical default state (schema-aligned color groups). This file does
#    NOT mutate at runtime, so it diffs cleanly across machines and is safe
#    to ship as the maintainer-curated default.
# 3. ``seed_obsidian_config`` runs at vault setup (``init-vault`` / ``reset-
#    vault``) and copies each ``<name>.template.json`` to ``<name>.json``
#    IFF the target is missing. Existing user-customized files are never
#    touched. The result: brand-new vaults boot with the maintainer's
#    default colors; established vaults keep whatever the user customized.
#
# This pattern generalizes: any future ``*.template.json`` dropped into
# ``.obsidian/`` is auto-seeded the same way (e.g. a future
# ``app.template.json`` if we ever ship one).

# Suffix used to mark a tracked default-state template file. Lives next to
# the real file it seeds, with the same stem (so ``graph.json`` is seeded
# from ``graph.template.json``).
_OBSIDIAN_TEMPLATE_SUFFIX = ".template.json"


def _target_for_template(template: Path) -> Path:
    """Return the ``<name>.json`` path a ``<name>.template.json`` file seeds.

    ``foo.template.json`` -> ``foo.json``. Lives in the same directory.
    """
    stem = template.name[: -len(_OBSIDIAN_TEMPLATE_SUFFIX)]
    return template.parent / f"{stem}.json"


def seed_obsidian_config(vault_root: Path) -> list[Path]:
    """Copy every ``*.template.json`` under ``<vault>/.obsidian/`` to its
    sibling target IFF the target file does not already exist.

    Returns the list of target paths that were freshly created. An existing
    target is never overwritten (this is what guarantees a pull-and-reset
    never clobbers a user's customized graph view, bookmarks, etc.).

    No-ops gracefully when ``<vault>/.obsidian/`` does not exist or contains
    no templates — callers can invoke unconditionally.
    """
    obsidian_dir = vault_root / ".obsidian"
    if not obsidian_dir.is_dir():
        return []
    seeded: list[Path] = []
    for template in sorted(obsidian_dir.glob(f"*{_OBSIDIAN_TEMPLATE_SUFFIX}")):
        if not template.is_file():
            continue
        target = _target_for_template(template)
        if target.exists():
            continue
        shutil.copyfile(template, target)
        seeded.append(target)
    return seeded


def _file_matches_skeleton(path: Path, skeleton: str) -> bool:
    """True when ``path`` exists and its content equals ``skeleton``."""
    if not path.exists():
        return False
    try:
        return path.read_text(encoding="utf-8") == skeleton
    except OSError:
        return False


_LOG_SKELETON_BOOTSTRAP_RE = re.compile(
    r"^## \[\d{4}-\d{2}-\d{2}\] manual \| bootstrap\s*$",
    re.MULTILINE,
)


def _is_log_skeleton(path: Path) -> bool:
    """True when ``log.md`` looks like the canonical bootstrap-only skeleton.

    The skeleton template parametrizes today's date, so we can't compare
    byte-for-byte; instead we accept any log file that contains exactly
    one heading and that heading is a ``manual | bootstrap`` entry with
    a valid date. Any additional ``## [...] ...`` entries mean real run
    history exists and the file should be reset.
    """
    if not path.exists():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    headings = re.findall(r"^## \[", text, re.MULTILINE)
    if len(headings) != 1:
        return False
    return bool(_LOG_SKELETON_BOOTSTRAP_RE.search(text))


# ---------------------------------------------------------------------------
# Vault reset (fork onboarding)
# ---------------------------------------------------------------------------
#
# ``reset_vault`` is the destructive counterpart to ``init-vault``. It wipes
# the maintainer's content from a forked vault back down to the empty
# skeleton. The signature deliberately has **no default** for ``root``: every
# caller must pass an explicit ``Path``, so ``Path("wiki")`` cannot sneak in
# via a default argument and accidentally target the workspace's live vault.
#
# Preservation rules (see ``CLAUDE.md`` "Personal scratch convention" and the
# plan in ``.cursor/plans/add_reset-vault_command_*.plan.md``):
#
# - ``wiki/.obsidian/``      — pre-configured reader setup, kept verbatim.
# - ``wiki/_dashboard.md``   — content-agnostic Dataview starter, kept verbatim.
# - any ``_*.md`` anywhere   — personal scratch (lint-exempt, sweep-exempt).
# - ``.gitkeep``             — kept inside every WIKI_DIRS subdirectory.
# - ``index.md``, ``log.md`` — rewritten to the canonical skeleton strings.
# - WIKI_DIRS subdirectories — recreated if missing, contents wiped.
#
# When ``keep_topics=True`` the entire ``wiki/topics/`` tree (purpose.md +
# index.md) is preserved as-is. This is the "I share the maintainer's topic
# set" power-user path; the default (``keep_topics=False``) deletes every
# ``topics/<id>/`` subdirectory.


def is_personal_scratch(name: str) -> bool:
    """Return True for files matching the ``_*.md`` personal-scratch convention.

    Per the schema in ``CLAUDE.md``, any markdown file whose basename starts
    with ``_`` is human-only: lint-exempt, sweep-exempt, gate-blocked on
    ``claude/*`` branches. ``reset_vault`` preserves these files anywhere in
    the vault so a forker who has already started taking notes does not lose
    them.
    """
    return name.startswith("_") and name.endswith(".md")


@dataclass
class ResetSummary:
    """Plan + receipt for a ``reset_vault`` call.

    Returned in both dry-run mode (where ``mutated`` is False and no I/O has
    happened) and post-mutation mode (where ``mutated`` is True and the lists
    describe what was actually deleted/preserved).
    """

    root: Path
    dry_run: bool
    mutated: bool
    files_to_delete: list[Path] = field(default_factory=list)
    dirs_to_delete: list[Path] = field(default_factory=list)
    files_to_reset: list[Path] = field(default_factory=list)
    files_preserved: list[Path] = field(default_factory=list)
    dirs_preserved: list[Path] = field(default_factory=list)

    @property
    def total_deletions(self) -> int:
        return len(self.files_to_delete) + len(self.dirs_to_delete)

    def is_empty(self) -> bool:
        """True when the vault was already at the empty-skeleton state."""
        return not (self.files_to_delete or self.dirs_to_delete or self.files_to_reset)


def _looks_like_vault(root: Path) -> bool:
    """Heuristic: does ``root`` resemble a Wikipilot vault?

    Requires ``index.md`` at the root and at least four of the canonical
    ``WIKI_DIRS`` as subdirectories. This is intentionally permissive (a
    half-bootstrapped vault still passes) but rejects obviously-unrelated
    targets like ``~/Documents`` or a pip cache directory.
    """
    if not root.is_dir():
        return False
    if not (root / "index.md").exists():
        return False
    present = sum(1 for sub in WIKI_DIRS if (root / sub).is_dir())
    return present >= 4


def _plan_reset(root: Path, *, keep_topics: bool) -> ResetSummary:
    """Walk the vault and decide what would be deleted, reset, or preserved."""
    summary = ResetSummary(root=root, dry_run=True, mutated=False)

    obsidian_dir = root / ".obsidian"
    if obsidian_dir.is_dir():
        summary.dirs_preserved.append(obsidian_dir)

    # Root-level files.
    for child in sorted(root.iterdir()):
        if child.is_dir():
            continue
        name = child.name
        if name == "index.md":
            if not _file_matches_skeleton(child, INDEX_SKELETON):
                summary.files_to_reset.append(child)
            else:
                summary.files_preserved.append(child)
        elif name == "log.md":
            # The log skeleton is parametrized by date; treat any well-formed
            # bootstrap entry as already-skeleton.
            if not _is_log_skeleton(child):
                summary.files_to_reset.append(child)
            else:
                summary.files_preserved.append(child)
        elif is_personal_scratch(name) or name == ".gitkeep":
            summary.files_preserved.append(child)
        else:
            # Other root-level files (e.g. stray notes a forker created)
            # are preserved by default — we only touch known schema files.
            summary.files_preserved.append(child)

    # Each WIKI_DIRS subdirectory.
    for sub in WIKI_DIRS:
        sub_dir = root / sub
        if not sub_dir.is_dir():
            continue
        if sub == "topics" and keep_topics:
            # Power-user path: preserve the entire topics/ tree as-is.
            summary.dirs_preserved.append(sub_dir)
            continue
        if sub == "topics":
            # Delete every topic folder; recreate the empty topics/ dir
            # post-mutation so .gitkeep can land back in place.
            for entry in sorted(sub_dir.iterdir()):
                if entry.is_dir():
                    summary.dirs_to_delete.append(entry)
                elif entry.name == ".gitkeep" or is_personal_scratch(entry.name):
                    summary.files_preserved.append(entry)
                else:
                    summary.files_to_delete.append(entry)
            continue
        if sub == "assets":
            # Delete every per-source asset folder; .gitkeep stays.
            for entry in sorted(sub_dir.iterdir()):
                if entry.is_dir():
                    summary.dirs_to_delete.append(entry)
                elif entry.name == ".gitkeep" or is_personal_scratch(entry.name):
                    summary.files_preserved.append(entry)
                else:
                    summary.files_to_delete.append(entry)
            continue
        # Standard wipe: delete *.md files (except _*.md and .gitkeep).
        for entry in sorted(sub_dir.iterdir()):
            if entry.is_dir():
                # Unexpected nested dir under e.g. concepts/ — leave it alone.
                summary.dirs_preserved.append(entry)
            elif entry.name == ".gitkeep" or is_personal_scratch(entry.name):
                summary.files_preserved.append(entry)
            else:
                summary.files_to_delete.append(entry)

    return summary


def reset_vault(
    root: Path,
    *,
    keep_topics: bool = False,
    dry_run: bool = False,
) -> ResetSummary:
    """Reset a Wikipilot vault back to the empty skeleton.

    Parameters
    ----------
    root:
        The vault directory. **No default** — callers must pass an explicit
        ``Path``. ``Path("wiki")`` never sneaks in via a signature default.
    keep_topics:
        When True, preserve the entire ``topics/`` tree (purpose.md +
        index.md). Default False — every ``topics/<id>/`` subdirectory is
        deleted.
    dry_run:
        When True, plan the reset and return the ``ResetSummary`` without
        mutating any files. Use this from the CLI to populate the
        confirmation prompt.

    Returns
    -------
    ResetSummary
        Describes what was (or would be) deleted, reset, and preserved. The
        ``root`` field is the absolute resolved path the helper actually
        operated on.

    Raises
    ------
    WikiError
        When ``root`` does not exist, is not a directory, or does not look
        like a Wikipilot vault (missing ``index.md`` or fewer than four
        canonical subdirectories present).
    """
    resolved = Path(root).resolve()
    if not resolved.exists():
        raise WikiError(f"Vault path does not exist: {resolved}")
    if not resolved.is_dir():
        raise WikiError(f"Vault path is not a directory: {resolved}")
    if not _looks_like_vault(resolved):
        raise WikiError(
            f"Path does not look like a Wikipilot vault (missing index.md or "
            f"fewer than 4 canonical subdirectories present): {resolved}. "
            "If this really is your vault, run 'wikipilot init-vault' first."
        )

    summary = _plan_reset(resolved, keep_topics=keep_topics)
    summary.root = resolved

    if dry_run:
        return summary

    # Mutate. Order: delete files, delete dirs, recreate skeleton dirs and
    # .gitkeeps. Index/log skeletons are written by the CLI (it owns the
    # skeleton strings); the helper signals which files need rewriting via
    # ``files_to_reset`` and the CLI executes that step.
    for path in summary.files_to_delete:
        path.unlink()
    for directory in summary.dirs_to_delete:
        shutil.rmtree(directory)

    # Ensure every WIKI_DIRS subdirectory exists with a .gitkeep, matching
    # ``init-vault``'s post-condition.
    for sub in WIKI_DIRS:
        sub_dir = resolved / sub
        sub_dir.mkdir(parents=True, exist_ok=True)
        gitkeep = sub_dir / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")

    summary.dry_run = False
    summary.mutated = True
    return summary
