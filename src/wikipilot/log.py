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

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wikipilot.wiki import Page, Vault

VALID_LOG_KINDS: tuple[str, ...] = ("daily", "query", "health", "manual")


@dataclass(frozen=True)
class RunReport:
    """The contents of one ``wiki/reports/YYYY-MM-DD.md`` page.

    Stored on disk as a regular wiki page (frontmatter + markdown body) so
    Obsidian renders it natively and the lint can validate frontmatter.
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
    sections = [
        "## Summary",
        f"- Routine: `{report.routine}`",
        f"- Run id: `{report.run_id}`",
        f"- Topics processed: {len(report.topics_processed)}",
        f"- Sources added: {len(report.sources_added)}",
        f"- Pages touched: {len(report.pages_touched)}",
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
            "## Topics processed",
            _bullet_list(report.topics_processed) or "_None._",
            "",
            "## Sources added",
            _bullet_list(report.sources_added) or "_None._",
            "",
            "## Pages touched",
            _bullet_list(report.pages_touched) or "_None._",
            "",
            "## Pull requests",
            _bullet_list(report.pr_links) or "_None._",
            "",
            "## New disputes",
            _bullet_list(report.new_disputes) or "_None._",
            "",
            "## New open questions",
            _bullet_list(report.new_open_questions) or "_None._",
        ]
    )
    if report.notes:
        sections.extend(["", "## Notes", report.notes.strip()])
    return "\n".join(sections) + "\n"


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
