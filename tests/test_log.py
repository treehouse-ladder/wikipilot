"""Tests for ``wikipilot.log`` (append + report writers)."""

from __future__ import annotations

from datetime import date

import pytest

from wikipilot.log import (
    HealthReport,
    RunReport,
    append_log_entry,
    write_health_report,
    write_run_report,
)
from wikipilot.wiki import Page, Vault, parse_log_headings


class TestAppendLogEntry:
    def test_appends_well_formed(self, sample_vault: Vault) -> None:
        original = sample_vault.log_path.read_text(encoding="utf-8")
        original_count = len(parse_log_headings(original))
        append_log_entry(
            sample_vault,
            kind="daily",
            subject="ai-agents — 2 sources, 7 pages",
            summary="Ingested 2 papers about agent eval.",
            today=date(2026, 5, 11),
        )
        text = sample_vault.log_path.read_text(encoding="utf-8")
        headings = parse_log_headings(text)
        assert len(headings) == original_count + 1
        last = headings[-1]
        assert last[0] == "2026-05-11"
        assert last[1] == "daily"
        assert "ai-agents" in last[2]

    def test_rejects_bad_kind(self, sample_vault: Vault) -> None:
        with pytest.raises(ValueError, match="Unknown log kind"):
            append_log_entry(sample_vault, kind="bogus", subject="x", summary="y")

    def test_rejects_pipe_in_subject(self, sample_vault: Vault) -> None:
        with pytest.raises(ValueError, match="'\\|'"):
            append_log_entry(sample_vault, kind="daily", subject="a | b", summary="y")

    def test_creates_log_if_missing(self, sample_vault: Vault) -> None:
        sample_vault.log_path.unlink()
        append_log_entry(
            sample_vault,
            kind="manual",
            subject="bootstrap",
            summary="initial entry",
            today=date(2026, 5, 11),
        )
        assert sample_vault.log_path.exists()
        text = sample_vault.log_path.read_text(encoding="utf-8")
        assert "## [2026-05-11] manual | bootstrap" in text


class TestWriteRunReport:
    def test_writes_report_legacy_caller(self, sample_vault: Vault) -> None:
        """Callers that don't populate the curator fields still produce a valid report."""
        report = RunReport(
            routine="daily_research",
            run_date=date(2026, 5, 11),
            run_id="daily-2026-05-11-001",
            topics_processed=["ai-agents"],
            sources_added=["[[example-paper-aabbccdd]]"],
            pages_touched=["wiki/concepts/transformer-attention.md"],
            runtime_seconds=42.5,
            token_usage={"opus-4.7": 12_345, "sonnet": 6_789, "haiku": 1_234},
            pr_links=["https://github.com/x/y/pull/1"],
            new_disputes=["[[transformer-attention]]: scaling claim disputed"],
            new_open_questions=["FP8 attention behavior under agentic loops"],
        )
        path = write_run_report(sample_vault, report)
        assert path.exists()
        page = Page.read(path)
        assert page.kind == "report"
        assert page.metadata["routine"] == "daily_research"
        assert page.metadata["run_id"] == "daily-2026-05-11-001"
        # New editorial sections still render even when empty:
        assert "## Today's brief" in page.content
        assert "_Curator produced no must-read items today._" in page.content
        # Accounting moved under a <details> block:
        assert "<details>" in page.content
        assert "## Run accounting" in page.content
        assert "12,345" in page.content

    def test_writes_report_with_curator_output(self, sample_vault: Vault) -> None:
        report = RunReport(
            routine="daily_research",
            run_date=date(2026, 5, 22),
            run_id="daily-2026-05-22-002",
            topics_processed=["frontier-models", "agentic-coding"],
            sources_added=[],
            pages_touched=[],
            runtime_seconds=180.0,
            token_usage={},
            pr_links=[],
            new_disputes=[],
            new_open_questions=[],
            brief=(
                "## Today's brief\n\n"
                "- **[[claude-opus-4.7]]**: took #1 on GDPval-AA [[src-a]]. "
                "**Why it matters:** ships agentic work to production."
            ),
            leader_changes=(
                "## Leader changes\n\n"
                "- **`gdpval_aa_elo`**: [[claude-opus-4.7]] took #1 [[src-a]]."
            ),
            watchlist=(
                "## Watchlist\n\n- **[[muse-spark]]**: open-weights candidate [[src-b]]."
            ),
            model_snapshot=(
                "### Cost\n\n| Entity | input |\n| --- | --- |\n"
                "| [[opus]] | _unknown_ |\n\n"
                "### Benchmarks\n\n| Entity | gdp |\n| --- | --- |\n"
                "| [[opus]] | **1753** |"
            ),
            notable_findings_by_topic=[
                "- **[[frontier-models]]**: GLM-5 released [[glm-5]].",
                "- **[[agentic-coding]]**: SWE-Chain numbers [[swe-chain]].",
            ],
        )
        path = write_run_report(sample_vault, report)
        page = Page.read(path)
        body = page.content
        # Editorial sections render verbatim.
        assert "## Today's brief\n\n- **[[claude-opus-4.7]]**" in body
        assert "## Leader changes\n\n- **`gdpval_aa_elo`**" in body
        assert "## Watchlist\n\n- **[[muse-spark]]**" in body
        # Frontier model snapshot wraps the transcluded tables.
        assert "## Frontier model snapshot" in body
        assert "**1753**" in body
        # Notable findings section renders one bullet per topic.
        assert "## Notable findings by topic" in body
        assert "GLM-5 released" in body
        assert "SWE-Chain numbers" in body
        # Section order: brief BEFORE accounting.
        assert body.index("## Today's brief") < body.index("## Run accounting")
        assert body.index("## Frontier model snapshot") < body.index("## Run accounting")

    def test_section_order_editorial_first(self, sample_vault: Vault) -> None:
        """`## Today's brief` precedes `## Leader changes` precedes `## Frontier model snapshot`."""
        report = RunReport(
            routine="daily_research",
            run_date=date(2026, 5, 22),
            run_id="order-test",
            topics_processed=[],
            sources_added=[],
            pages_touched=[],
            runtime_seconds=None,
            token_usage={},
            pr_links=[],
            new_disputes=[],
            new_open_questions=[],
            brief="## Today's brief\n\n- a [[s]]",
            leader_changes="## Leader changes\n\n- b [[s]]",
            watchlist="## Watchlist\n\n- c [[s]]",
            model_snapshot="snapshot body",
            notable_findings_by_topic=["- d"],
        )
        path = write_run_report(sample_vault, report)
        body = path.read_text(encoding="utf-8")
        brief = body.index("## Today's brief")
        leaders = body.index("## Leader changes")
        snapshot = body.index("## Frontier model snapshot")
        watchlist = body.index("## Watchlist")
        notable = body.index("## Notable findings by topic")
        disputes = body.index("## Disputes & open questions")
        accounting = body.index("## Run accounting")
        assert brief < leaders < snapshot < watchlist < notable < disputes < accounting


class TestWriteHealthReport:
    def test_writes_health_report(self, sample_vault: Vault) -> None:
        report = HealthReport(
            run_date=date(2026, 5, 17),
            run_id="health-2026-05-17-001",
            stale_pages=["wiki/concepts/stale-concept.md"],
            citation_density_failures=["wiki/concepts/thin-citations.md"],
            new_disputes=["[[transformer-attention]]: paraphrase contradiction"],
            orphan_pages=[],
            broken_wikilinks=[],
            runtime_seconds=120.0,
            token_usage={"sonnet": 50_000},
        )
        path = write_health_report(sample_vault, report)
        assert path.name == "health-2026-05-17.md"
        page = Page.read(path)
        assert page.metadata["routine"] == "weekly_health"
        assert "## Stale pages" in page.content
        assert "## Citation-density failures" in page.content
        assert "## New disputes" in page.content
