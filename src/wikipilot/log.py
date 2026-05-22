r"""Append-only log + per-run / weekly health report writers.

The wiki keeps a chronological journal at ``wiki/log.md``. Every routine run
appends one entry per topic processed (Daily Research), one entry per
question answered (Wiki Query), and one entry per sweep (Weekly Health).
Each entry has the exact form

    ## [YYYY-MM-DD] kind | subject

    One-line summary.

so the log is greppable with ``grep "^## \[" wiki/log.md`` (Karpathy's idiom).
``parse_log_headings`` in ``wiki.py`` rejects entries that don't match.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from wikipilot.wiki import Page, Vault

VALID_LOG_KINDS: tuple[str, ...] = ("daily", "query", "health", "manual")


@dataclass(frozen=True)
class RunReport:
    """The contents of one ``wiki/reports/YYYY-MM-DD.md`` page.

    Stored on disk as a regular wiki page (frontmatter + markdown body) so
    Obsidian renders it natively and the lint can validate frontmatter.

    The render order is intentionally editorial-first: the curator's
    ``## Today's brief``, ``## Leader changes`` (cost / benchmark #1 swaps),
    ``## Frontier model snapshot`` (transcluded comparison tables),
    ``## Watchlist``, and ``## Notable findings by topic`` come BEFORE the
    accounting tail (which lives under a collapsible ``<details>``). The
    user is the primary reader; counts and PR links are bookkeeping.

    Legacy callers that don't populate the curator fields still produce a
    valid report — the new sections render as ``_None._`` or are omitted
    cleanly when their input is empty.
    """

    routine: str
    run_date: date
    run_id: str
    topics_processed: list[str]
    sources_added: list[str]
    pages_touched: list[str]
    runtime_seconds: float | None
    token_usage: dict[str, int]
    pr_links: list[str]
    new_disputes: list[str]
    new_open_questions: list[str]
    notes: str = ""
    # Curator output (see `.claude/agents/daily-brief-curator.md`).
    # Each is already-formatted markdown that begins with its `## Heading`.
    brief: str = ""
    leader_changes: str = ""
    watchlist: str = ""
    # Already-formatted markdown showing the regenerated cost + benchmark
    # comparison tables. Typically assembled by the orchestrator from the
    # body (minus frontmatter) of `wiki/comparisons/cost-comparison.md` and
    # `wiki/comparisons/benchmark-leaders.md`.
    model_snapshot: str = ""
    # One markdown bullet per topic — the head sentence of the
    # researcher's `summary_addition`, prefixed with `[[topic-id]]`. Renders
    # as `## Notable findings by topic`.
    notable_findings_by_topic: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class HealthReport:
    """The contents of one ``wiki/reports/health-YYYY-MM-DD.md`` page."""

    run_date: date
    run_id: str
    stale_pages: list[str]
    citation_density_failures: list[str]
    new_disputes: list[str]
    orphan_pages: list[str]
    broken_wikilinks: list[str]
    runtime_seconds: float | None
    token_usage: dict[str, int]
    notes: str = ""


def append_log_entry(
    vault: Vault,
    *,
    kind: str,
    subject: str,
    summary: str,
    today: date | None = None,
) -> None:
    """Append a single ``## [YYYY-MM-DD] kind | subject`` block to ``log.md``."""
    if kind not in VALID_LOG_KINDS:
        raise ValueError(f"Unknown log kind {kind!r}; expected one of {VALID_LOG_KINDS}")
    if "|" in subject:
        raise ValueError("subject may not contain '|' (it is the kind/subject delimiter)")
    today = today or date.today()
    log_path = vault.log_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(_LOG_HEADER + "\n", encoding="utf-8")
    block = f"\n## [{today.isoformat()}] {kind} | {subject.strip()}\n\n{summary.strip()}\n"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(block)


def write_run_report(vault: Vault, report: RunReport) -> Path:
    """Write a per-run report to ``wiki/reports/YYYY-MM-DD.md`` and return the path.

    If a same-day report already exists it is overwritten — the Daily Research
    orchestrator is expected to write the report exactly once per run, after
    every topic has been processed.
    """
    path = vault.dir_for("reports") / f"{report.run_date.isoformat()}.md"
    metadata = {
        "title": f"Daily run report — {report.run_date.isoformat()}",
        "kind": "report",
        "routine": report.routine,
        "run_id": report.run_id,
        "sources": [],
        "last_updated": report.run_date,
        "last_verified": report.run_date,
        "freshness_window_days": 365,
    }
    body = _render_run_report_body(report)
    page = Page.from_dict(path, metadata, body)
    page.write()
    return path


def write_health_report(vault: Vault, report: HealthReport) -> Path:
    """Write a weekly health report to ``wiki/reports/health-YYYY-MM-DD.md``."""
    path = vault.dir_for("reports") / f"health-{report.run_date.isoformat()}.md"
    metadata = {
        "title": f"Weekly health report — {report.run_date.isoformat()}",
        "kind": "report",
        "routine": "weekly_health",
        "run_id": report.run_id,
        "sources": [],
        "last_updated": report.run_date,
        "last_verified": report.run_date,
        "freshness_window_days": 365,
    }
    body = _render_health_report_body(report)
    page = Page.from_dict(path, metadata, body)
    page.write()
    return path


_LOG_HEADER = """# Log

Chronological, append-only record of every routine run. Parseable with `grep "^## \\[" wiki/log.md`.

This file is **LLM-write, human-read**. Do not hand-edit; routines maintain it.

---
"""


def _render_run_report_body(report: RunReport) -> str:
    """Render a Daily Research report body, editorial-first.

    Section order (top is what the user reads first):

    1. ``## Today's brief`` — the curator's must-reads.
    2. ``## Leader changes`` — only when a #1 swapped today.
    3. ``## Frontier model snapshot`` — the regenerated cost + benchmark tables.
    4. ``## Watchlist`` — the curator's high-signal-but-not-must-read items.
    5. ``## Notable findings by topic`` — one bullet per topic.
    6. ``## Disputes & open questions`` — append-only state, all topics.
    7. ``## Run accounting`` (``<details>``) — counts, PRs, runtime, notes.
    """
    sections: list[str] = []
    if report.brief.strip():
        sections.append(report.brief.strip())
    else:
        sections.append("## Today's brief\n\n_Curator produced no must-read items today._")
    if report.leader_changes.strip():
        sections.append("")
        sections.append(report.leader_changes.strip())
    if report.model_snapshot.strip():
        sections.append("")
        sections.append("## Frontier model snapshot")
        sections.append("")
        sections.append(report.model_snapshot.strip())
    if report.watchlist.strip():
        sections.append("")
        sections.append(report.watchlist.strip())
    if report.notable_findings_by_topic:
        sections.append("")
        sections.append("## Notable findings by topic")
        sections.append("")
        sections.append("\n".join(report.notable_findings_by_topic))
    sections.append("")
    sections.append("## Disputes & open questions")
    sections.append("")
    sections.append("### New disputes")
    sections.append(_bullet_list(report.new_disputes) or "_None._")
    sections.append("")
    sections.append("### New open questions")
    sections.append(_bullet_list(report.new_open_questions) or "_None._")
    sections.append("")
    sections.append(_render_run_accounting(report))
    return "\n".join(sections) + "\n"


def _render_run_accounting(report: RunReport) -> str:
    """Render the collapsible bookkeeping block at the bottom of the report.

    Wrapped in ``<details>`` so the editorial top of the page stays the
    landing surface in Obsidian. Counts, PR links, runtime, token usage,
    and notes all live here — they're useful for audit and recovery but
    not the user's primary read.
    """
    inner: list[str] = ["", "## Run accounting", ""]
    inner.append(f"- Routine: `{report.routine}`")
    inner.append(f"- Run id: `{report.run_id}`")
    inner.append(f"- Topics processed: {len(report.topics_processed)}")
    inner.append(f"- Sources added: {len(report.sources_added)}")
    inner.append(f"- Pages touched: {len(report.pages_touched)}")
    if report.runtime_seconds is not None:
        inner.append(f"- Runtime: {report.runtime_seconds:.1f}s")
    if report.token_usage:
        usage_lines = [
            f"  - {model}: {tokens:,}" for model, tokens in sorted(report.token_usage.items())
        ]
        inner.append("- Token usage by tier:\n" + "\n".join(usage_lines))
    inner.extend(
        [
            "",
            "### Topics processed",
            _bullet_list(report.topics_processed) or "_None._",
            "",
            "### Sources added",
            _bullet_list(report.sources_added) or "_None._",
            "",
            "### Pages touched",
            _bullet_list(report.pages_touched) or "_None._",
            "",
            "### Pull requests",
            _bullet_list(report.pr_links) or "_None._",
        ]
    )
    if report.notes:
        inner.extend(["", "### Notes", report.notes.strip()])
    body = "\n".join(inner)
    return (
        "<details>\n"
        "<summary>Run accounting (counts, PRs, runtime, notes)</summary>\n"
        f"{body}\n"
        "\n</details>"
    )


def _render_health_report_body(report: HealthReport) -> str:
    sections = [
        "## Summary",
        f"- Run id: `{report.run_id}`",
        f"- Stale pages: {len(report.stale_pages)}",
        f"- Citation-density failures: {len(report.citation_density_failures)}",
        f"- New disputes filed: {len(report.new_disputes)}",
        f"- Orphan pages: {len(report.orphan_pages)}",
        f"- Broken wikilinks: {len(report.broken_wikilinks)}",
    ]
    if report.runtime_seconds is not None:
        sections.append(f"- Runtime: {report.runtime_seconds:.1f}s")
    if report.token_usage:
        usage_lines = [
            f"  - {model}: {tokens:,}" for model, tokens in sorted(report.token_usage.items())
        ]
        sections.append("- Token usage by tier:\n" + "\n".join(usage_lines))
    sections.extend(
        [
            "",
            "## Stale pages",
            _bullet_list(report.stale_pages) or "_None._",
            "",
            "## Citation-density failures",
            _bullet_list(report.citation_density_failures) or "_None._",
            "",
            "## New disputes",
            _bullet_list(report.new_disputes) or "_None._",
            "",
            "## Orphan pages",
            _bullet_list(report.orphan_pages) or "_None._",
            "",
            "## Broken wikilinks",
            _bullet_list(report.broken_wikilinks) or "_None._",
        ]
    )
    if report.notes:
        sections.extend(["", "## Notes", report.notes.strip()])
    return "\n".join(sections) + "\n"


def _bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
