"""Wikilink resolution + auto-fix shared between the lint, merger, and lint-fixer.

The three call sites for wikilink resolution used to each implement their own
version:

- ``wikipilot.lint.check_broken_wikilinks`` parsed the lint context's known
  slugs and reported any unresolved ``[[link]]`` as a hard error.
- The ``wiki-merger`` agent didn't validate at all — it wrote whatever
  ``summary_addition`` prose the topic-researcher produced verbatim, even
  when the embedded slugs were typos.
- The ``wiki-lint-fixer`` agent (Phase 11) wants to repair broken wikilinks
  post-CI by globbing for the actual target.

This module is the single source of truth so all three share one resolution
table and one auto-fix heuristic. See ``CLAUDE.md`` "Layer 6" for the broader
design (the topic-researcher emits a deterministic ``slug`` on every source,
the merger validates pre-commit, the lint-fixer mops up anything that slipped
through).

Public API
----------

- :func:`resolve_wikilink` — pure ``bool``; checks ``target`` against a slug
  set. No I/O.
- :func:`autofix_wikilink` — best-effort lookup for unresolved targets; returns
  the unambiguous canonical slug, or ``None`` when zero/multiple candidates
  exist. The auto-fix only fires when the answer is unambiguous; ambiguity
  is the caller's signal to escalate.
- :func:`resolve_or_fix_in_files` — bulk API the merger uses pre-commit:
  rewrites every fixable link in place and returns a structured report so
  the caller can fail loud when anything remains unresolved.

Auto-fix heuristic
------------------

Two-pass match per unresolved target:

1. **SHA-suffix match.** Source page slugs look like
   ``<title-slug>-<sha8>`` where ``sha8`` is the first eight hex chars of
   ``sha256(normalize_url(url))``. The SHA is unique per source, so if the
   broken target ends in ``-[0-9a-f]{8}`` we look for a single existing page
   whose stem ends with the same SHA. Catches the common "topic-researcher
   mistyped one character before the SHA" case (PR #47's ``at-io-2026`` vs
   ``at-i-o-2026`` was exactly this).
2. **Slugify match.** For targets without a SHA suffix (synthesis pages —
   concepts, entities, topics, comparisons, answers), look for a single
   existing page whose stem or title slugifies to the same value as the
   target. Picks up alias/case variants that the ``known_slugs`` set already
   handles for resolution but that the merger needs to *rewrite* to the
   canonical form before commit.

Both passes require exactly one candidate. Zero matches → ``None`` (the
caller treats it as unresolvable). Multiple matches → ``None`` (ambiguity is
unsafe to auto-fix; the human needs to pick).
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from wikipilot.wiki import Page, Vault, parse_wikilinks, slugify

_SHA_SUFFIX_RE = re.compile(r"-([0-9a-f]{8})$")


def resolve_wikilink(
    target: str,
    known: set[str] | frozenset[str],
    extra: set[str] | frozenset[str] = frozenset(),
) -> bool:
    """Return True when ``target`` resolves against ``known`` ∪ ``extra``.

    Mirrors the lint's resolution semantics: a target resolves if either the
    raw target or its slugified form is in the combined slug set. The
    ``extra`` parameter lets callers extend the set with slugs not yet
    written to disk (e.g. the slugs from a Proposal's ``sources`` list that
    the merger hasn't yet committed).
    """
    if not target:
        return False
    cleaned = target.strip()
    if not cleaned:
        return False
    combined = known | extra
    if cleaned in combined:
        return True
    slugified = slugify(cleaned)
    return bool(slugified) and slugified in combined


def autofix_wikilink(target: str, vault: Vault) -> str | None:
    """Return the canonical slug for ``target`` when an unambiguous match exists.

    Returns ``None`` when zero or more than one candidate matches — both are
    cases the caller must escalate (zero means human review; multiple means
    the auto-fix would have to guess between equally-valid options).

    The vault is scanned via :meth:`Vault.iter_markdown_files`, so this picks
    up sources, concepts, entities, topic indices, comparisons, answers, and
    any future markdown page beneath the vault root — without hard-coding
    the page kinds here.
    """
    cleaned = (target or "").strip()
    if not cleaned:
        return None

    sha_match = _SHA_SUFFIX_RE.search(cleaned)
    if sha_match:
        sha = sha_match.group(1)
        candidates = _candidates_by_sha_suffix(vault, sha)
        if len(candidates) == 1:
            return candidates[0]
        return None

    candidates = _candidates_by_slugify(vault, cleaned)
    if len(candidates) == 1:
        return candidates[0]
    return None


def _candidates_by_sha_suffix(vault: Vault, sha: str) -> list[str]:
    """Return distinct stems that end with ``-<sha>``."""
    suffix = f"-{sha}"
    seen: set[str] = set()
    for path in vault.iter_markdown_files():
        stem = path.stem
        if stem.endswith(suffix):
            seen.add(stem)
    return sorted(seen)


def _candidates_by_slugify(vault: Vault, target: str) -> list[str]:
    """Return distinct stems whose stem-or-title slugifies to slugify(target)."""
    needle = slugify(target)
    if not needle:
        return []
    seen: set[str] = set()
    for path in vault.iter_markdown_files():
        stem = path.stem
        if slugify(stem) == needle:
            seen.add(stem)
            continue
        # Title-based match: read the page lazily and compare slugified title.
        try:
            page = Page.read(path)
        except Exception:  # noqa: BLE001 — non-page files (e.g. malformed) are skipped
            continue
        if page.title and slugify(page.title) == needle:
            seen.add(stem)
    return sorted(seen)


@dataclass
class ResolveReport:
    """Outcome of :func:`resolve_or_fix_in_files`.

    - ``resolved``: targets that already pointed at a known slug; no rewrite.
    - ``autofixed``: tuples of ``(path, old_target, new_target)`` describing
      every link the helper rewrote. Useful for the merger to log how often
      Layer 6's safety net actually fires.
    - ``unresolved``: targets the auto-fix couldn't resolve unambiguously.
      A non-empty list is the merger's signal to abort the topic.
    """

    resolved: list[str] = field(default_factory=list)
    autofixed: list[tuple[Path, str, str]] = field(default_factory=list)
    unresolved: list[tuple[Path, str]] = field(default_factory=list)


def resolve_or_fix_in_files(
    paths: Iterable[Path],
    vault: Vault,
    *,
    proposal_slugs: set[str] | frozenset[str] = frozenset(),
) -> ResolveReport:
    """Resolve every ``[[link]]`` in ``paths``; rewrite fixable ones in place.

    Algorithm per file:

    1. Build the known-slug set from the vault (page stems, topic dirs,
       slugified titles, declared aliases — same logic as the lint).
    2. Combine with ``proposal_slugs`` (slugs the caller knows will exist
       post-commit but aren't on disk yet — the merger passes its proposal's
       source slugs here).
    3. For each ``[[target]]`` in the file: if it resolves, record it; if
       not, try :func:`autofix_wikilink`. On unambiguous match, rewrite the
       file in place. Otherwise record the unresolved target.

    The file is rewritten only when at least one auto-fix lands; this keeps
    ``mtime`` stable for files that didn't need any repair.

    The caller decides what to do with ``ResolveReport.unresolved``. The
    merger raises ``MergerError`` so the orchestrator aborts the topic; the
    lint-fixer reports ``resolved: false`` for the PR.
    """
    known = _known_slugs(vault)
    extra = set(proposal_slugs)
    report = ResolveReport()

    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        targets = parse_wikilinks(text)
        if not targets:
            continue

        new_text = text
        changed = False
        for target in targets:
            cleaned = target.strip()
            if resolve_wikilink(cleaned, known, extra):
                report.resolved.append(cleaned)
                continue
            fixed = autofix_wikilink(cleaned, vault)
            if fixed is None:
                report.unresolved.append((path, cleaned))
                continue
            # Rewrite this specific [[target]] occurrence to [[fixed]].
            new_text = _rewrite_wikilink(new_text, cleaned, fixed)
            report.autofixed.append((path, cleaned, fixed))
            changed = True

        if changed:
            path.write_text(new_text, encoding="utf-8")

    return report


def _rewrite_wikilink(text: str, old: str, new: str) -> str:
    """Replace every ``[[old]]`` / ``[[old|alias]]`` / ``[[old#section]]`` with the new slug.

    Preserves any alias or section suffix on each occurrence so the caller's
    intent (display text, section anchor) survives the rewrite. Uses a
    deliberate character-class fence so a target embedded inside a longer
    wikilink target doesn't accidentally match.
    """
    pattern = re.compile(
        r"\[\["
        + re.escape(old)
        + r"(?P<suffix>(?:#[^\[\]|\n]+?)?(?:\|[^\[\]\n]+?)?)\]\]"
    )

    def _sub(match: re.Match[str]) -> str:
        suffix = match.group("suffix") or ""
        return f"[[{new}{suffix}]]"

    return pattern.sub(_sub, text)


def _known_slugs(vault: Vault) -> set[str]:
    """Build the resolution table the lint uses.

    Duplicated here (instead of importing :class:`wikipilot.lint.LintContext`)
    so this module stays at the same layering as ``wiki.py`` and doesn't
    take a dependency on the lint module. The lint will be refactored to
    consume this helper in the same change (see :func:`wikipilot.lint.check_broken_wikilinks`).
    """
    slugs: set[str] = set()
    for path in vault.iter_markdown_files():
        try:
            page = Page.read(path)
        except Exception:  # noqa: BLE001 — malformed files are reported by the frontmatter lint
            slugs.add(path.stem)
            continue
        slugs.add(path.stem)
        if page.kind == "topic":
            slugs.add(path.parent.name)
        if title := page.title:
            slugs.add(slugify(title))
        try:
            aliases = page.aliases
        except Exception:  # noqa: BLE001
            aliases = []
        for alias in aliases:
            slugs.add(alias)
            slugs.add(slugify(alias))
    return slugs
