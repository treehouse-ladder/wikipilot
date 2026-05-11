"""Pick candidate page sets for the Weekly Health LLM-judge sweep.

This is the cheap, deterministic, metadata-only step that runs at the
top of every Weekly Health routine. It produces a JSON list of
``{trigger, pages[]}`` candidate sets which the orchestrator then fans
out to ``wiki-disputes-scanner`` subagents (one per set, in parallel).

Two heuristics produce candidate sets:

1. **Per-source** — for each source ingested in the last
   ``--lookback-days`` (default 7), find synthesis pages that *cite*
   that source AND share a wikilink with another candidate. Top-K by
   shared-link overlap. The trigger is ``source_<slug>``. This catches
   the case where a recent source contradicts a claim on an older page.

2. **Stale sweep** — pick the K pages with the oldest ``last_verified``
   that aren't already in any per-source set. Trigger ``stale_sweep``.
   Captures pages that have drifted out of date independently of any
   recent ingest.

The scanner agent reads each candidate set, judges whether the pages
actually disagree, and files ``## Disputes`` proposals — never
auto-resolves anything. By keeping seed selection pure-Python and
metadata-driven, the cost of the sweep stays bounded by the cost of
the *candidates we actually examine*, not the whole wiki.

Usage::

    python scripts/disputes_seed.py
    python scripts/disputes_seed.py --vault wiki --top-k 8 --lookback-days 14
    python scripts/disputes_seed.py --json   # for piping into agents
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from wikipilot.wiki import Page, Vault, parse_wikilinks, slugify

DEFAULT_LOOKBACK_DAYS: int = 7
DEFAULT_TOP_K: int = 10
DEFAULT_STALE_K: int = 10


@dataclass(frozen=True)
class CandidateSet:
    """One candidate set the disputes-scanner will judge."""

    trigger: str
    pages: tuple[str, ...]  # vault-relative POSIX paths


@dataclass(frozen=True)
class SeedResult:
    candidate_sets: tuple[CandidateSet, ...]

    def to_json(self) -> str:
        return json.dumps(
            {"candidate_sets": [{"trigger": c.trigger, "pages": list(c.pages)} for c in self]},
            indent=2,
        )

    def __iter__(self) -> Iterator[CandidateSet]:
        return iter(self.candidate_sets)


def seed_candidates(
    vault: Vault,
    *,
    today: date | None = None,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    top_k: int = DEFAULT_TOP_K,
    stale_k: int = DEFAULT_STALE_K,
) -> SeedResult:
    """Select candidate page sets by overlap heuristics.

    See module docstring for the two heuristics.
    """
    today = today or date.today()
    cutoff = today - timedelta(days=lookback_days)

    synthesis_pages: list[Page] = []
    source_pages: dict[str, Page] = {}  # slug -> Page

    for path in sorted(vault.iter_markdown_files()):
        if path.name in {"index.md", "log.md"} and path.parent == vault.root:
            continue
        try:
            page = Page.read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if page.kind == "source":
            source_pages[path.stem] = page
        elif page.kind in {"topic", "concept", "entity", "answer"}:
            synthesis_pages.append(page)

    backlinks_by_slug: dict[str, set[str]] = defaultdict(set)
    wikilinks_by_page: dict[str, set[str]] = {}
    for page in synthesis_pages:
        rel = _vault_relpath(page.path, vault)
        links = {_resolve_wikilink(link) for link in parse_wikilinks(page.content)}
        wikilinks_by_page[rel] = links
        for link in links:
            backlinks_by_slug[link].add(rel)

    candidate_sets: list[CandidateSet] = []
    used_pages: set[str] = set()

    recent_sources = sorted(
        (
            (slug, page)
            for slug, page in source_pages.items()
            if (fetched := _coerce_date(page.metadata.get("fetched_at"))) is not None
            and fetched >= cutoff
        ),
        key=lambda kv: kv[0],
    )
    for slug, _page in recent_sources:
        candidate_pages = _per_source_candidates(
            slug,
            backlinks_by_slug=backlinks_by_slug,
            wikilinks_by_page=wikilinks_by_page,
            top_k=top_k,
        )
        if len(candidate_pages) < 2:
            # A dispute needs at least two pages to compare.
            continue
        candidate_sets.append(CandidateSet(trigger=f"source_{slug}", pages=tuple(candidate_pages)))
        used_pages.update(candidate_pages)

    stale_pages = _stale_candidates(synthesis_pages, vault=vault, exclude=used_pages, top_k=stale_k)
    if len(stale_pages) >= 2:
        candidate_sets.append(CandidateSet(trigger="stale_sweep", pages=tuple(stale_pages)))

    return SeedResult(candidate_sets=tuple(candidate_sets))


def _per_source_candidates(
    source_slug: str,
    *,
    backlinks_by_slug: dict[str, set[str]],
    wikilinks_by_page: dict[str, set[str]],
    top_k: int,
) -> list[str]:
    """Pages that cite ``source_slug`` ranked by shared-link overlap.

    Two pages "overlap" when they cite the same source AND share at
    least one other wikilink target — those are the most likely places
    where a recent source would contradict an older claim.
    """
    citers = sorted(backlinks_by_slug.get(source_slug, set()))
    if len(citers) < 2:
        return citers

    overlap_score: Counter[str] = Counter()
    for i, page_a in enumerate(citers):
        links_a = wikilinks_by_page.get(page_a, set())
        for page_b in citers[i + 1 :]:
            links_b = wikilinks_by_page.get(page_b, set())
            shared = len(links_a & links_b)
            if shared:
                overlap_score[page_a] += shared
                overlap_score[page_b] += shared
    if not overlap_score:
        # No overlap; still return the citers (the scanner can decide).
        return citers[:top_k]
    ranked = [
        page for page, _score in sorted(overlap_score.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    return ranked[:top_k]


def _stale_candidates(
    pages: list[Page],
    *,
    vault: Vault,
    exclude: set[str],
    top_k: int,
) -> list[str]:
    """Top-K oldest-``last_verified`` pages, ignoring those already in a set."""
    rows: list[tuple[date, str]] = []
    for page in pages:
        rel = _vault_relpath(page.path, vault)
        if rel in exclude:
            continue
        verified = page.last_verified
        if verified is None:
            verified = date.min
        rows.append((verified, rel))
    rows.sort(key=lambda kv: (kv[0], kv[1]))
    return [rel for _, rel in rows[:top_k]]


def _resolve_wikilink(target: str) -> str:
    cleaned = target.strip().rstrip("/")
    return slugify(cleaned) or cleaned


def _vault_relpath(path: Path, vault: Vault) -> str:
    return path.resolve().relative_to(vault.root).as_posix()


def _coerce_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--vault",
        type=Path,
        default=Path("wiki"),
        help="Path to the wiki vault (default: ./wiki).",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=DEFAULT_LOOKBACK_DAYS,
        help=f"How many days back to consider sources 'recent' (default: {DEFAULT_LOOKBACK_DAYS}).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=DEFAULT_TOP_K,
        help=f"Max pages per per-source candidate set (default: {DEFAULT_TOP_K}).",
    )
    parser.add_argument(
        "--stale-k",
        type=int,
        default=DEFAULT_STALE_K,
        help=f"Max pages in the stale-sweep set (default: {DEFAULT_STALE_K}).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON only (suitable for piping into the orchestrator).",
    )
    args = parser.parse_args()

    if not args.vault.exists() or not args.vault.is_dir():
        print(f"ERROR: vault path {args.vault} does not exist", file=sys.stderr)
        return 2

    result = seed_candidates(
        Vault.at(args.vault),
        lookback_days=args.lookback_days,
        top_k=args.top_k,
        stale_k=args.stale_k,
    )
    if args.json:
        print(result.to_json())
        return 0
    if not result.candidate_sets:
        print("No candidate sets produced (nothing to sweep).")
        return 0
    print(f"Produced {len(result.candidate_sets)} candidate set(s):")
    for candidate in result.candidate_sets:
        print(f"  - {candidate.trigger} ({len(candidate.pages)} pages)")
        for page in candidate.pages:
            print(f"      {page}")
    return 0


# Re-export for tests / programmatic callers.
__all__ = [
    "CandidateSet",
    "SeedResult",
    "seed_candidates",
    "main",
]


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
