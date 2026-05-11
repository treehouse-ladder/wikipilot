"""Tests for the Phase 7 weekly-health dry-run pipeline."""

from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path

import pytest
from click.testing import CliRunner
from disputes_seed import seed_candidates

from wikipilot.cli import main
from wikipilot.dryrun import (
    apply_weekly_health,
    make_fake_weekly_health,
)
from wikipilot.lint import LintContext, Linter
from wikipilot.wiki import Page, Vault

FIXTURES = Path(__file__).parent / "fixtures"


def _copy_vault(tmp_path: Path) -> Path:
    dst = tmp_path / "wiki"
    shutil.copytree(FIXTURES / "sample_vault", dst)
    return dst


class TestMakeFakeWeeklyHealth:
    def test_files_dispute_per_set_with_two_pages(self) -> None:
        sets = [
            {"trigger": "source_x", "pages": ["a.md", "b.md", "c.md"]},
            {"trigger": "source_y", "pages": ["alone.md"]},  # too few, skipped
            {"trigger": "stale_sweep", "pages": ["d.md", "e.md"]},
        ]
        weekly = make_fake_weekly_health(sets)
        assert len(weekly.disputes_filed) == 2
        triggers = {d["trigger"] for d in weekly.disputes_filed}
        assert triggers == {"source_x", "stale_sweep"}


class TestApplyWeeklyHealth:
    def test_writes_dispute_and_health_report(self, sample_vault: Vault) -> None:
        seed = seed_candidates(sample_vault, today=date(2026, 5, 11))
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        result = apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))

        assert result.report_path is not None
        assert result.report_path.exists()
        assert result.report_path.name == "health-2026-05-11.md"
        # Pages touched include each disputed page + the report.
        touched_names = {p.name for p in result.pages_touched}
        assert "health-2026-05-11.md" in touched_names

        # Each disputed page now has the dispute bullet appended (Status: unresolved).
        for entry in weekly.disputes_filed:
            page_path = sample_vault.root / str(entry["page"])
            text = page_path.read_text(encoding="utf-8")
            assert "## Disputes" in text
            assert "Status: unresolved" in text
            assert "sweep: 2026-05-11" in text

    def test_only_bumps_last_updated(self, sample_vault: Vault) -> None:
        seed = seed_candidates(sample_vault, today=date(2026, 5, 11))
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        # Snapshot last_verified BEFORE apply.
        before = {}
        for entry in weekly.disputes_filed:
            page = Page.read(sample_vault.root / str(entry["page"]))
            before[entry["page"]] = page.last_verified

        apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))

        for entry in weekly.disputes_filed:
            page = Page.read(sample_vault.root / str(entry["page"]))
            assert page.last_updated == date(2026, 5, 11)
            # last_verified must NOT have been bumped (scanner doesn't verify).
            assert page.last_verified == before[entry["page"]]

    def test_idempotent_dispute_append(self, sample_vault: Vault) -> None:
        seed = seed_candidates(sample_vault, today=date(2026, 5, 11))
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))
        apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))

        # Re-running with the same weekly should not duplicate bullets.
        for entry in weekly.disputes_filed:
            page_path = sample_vault.root / str(entry["page"])
            text = page_path.read_text(encoding="utf-8")
            sweep_count = text.count("sweep: 2026-05-11")
            assert sweep_count == 1, f"duplicated bullet on {entry['page']}: {sweep_count}"

    def test_missing_page_skipped_gracefully(self, sample_vault: Vault) -> None:
        weekly = make_fake_weekly_health(
            [{"trigger": "ghost", "pages": ["nope/missing.md", "other/missing.md"]}]
        )
        result = apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))
        # Report still written, no pages modified.
        assert result.report_path is not None
        assert all(p.name == "health-2026-05-11.md" for p in result.pages_touched)

    def test_report_includes_lint_summary(self, sample_vault: Vault) -> None:
        seed = seed_candidates(sample_vault, today=date(2026, 5, 11))
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        result = apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))
        report_text = result.report_path.read_text(encoding="utf-8")
        # The fixture has stale-concept (stale-page) and thin-citations (citation-density).
        assert "Stale pages" in report_text
        assert "Citation-density failures" in report_text


class TestDryRunWeeklyHealthCli:
    def test_cli_invokes_full_pipeline(self, tmp_path: Path) -> None:
        runner = CliRunner()
        vault = _copy_vault(tmp_path)
        # Need a topics.yaml even though weekly-health doesn't use it; the CLI
        # shares a default and passes it through the click validator.
        topics = tmp_path / "topics.yaml"
        shutil.copy(FIXTURES / "sample_topics.yaml", topics)
        result = runner.invoke(
            main,
            [
                "dry-run",
                "--weekly-health",
                "--vault",
                str(vault),
                "--topics",
                str(topics),
            ],
        )
        assert result.exit_code == 0, result.output
        assert "Sweep dispatched" in result.output
        assert "Health report" in result.output
        assert (vault / "reports").glob("health-*.md")

    def test_cli_rejects_multiple_modes(self, tmp_path: Path) -> None:
        runner = CliRunner()
        vault = _copy_vault(tmp_path)
        topics = tmp_path / "topics.yaml"
        shutil.copy(FIXTURES / "sample_topics.yaml", topics)
        result = runner.invoke(
            main,
            [
                "dry-run",
                "--topic",
                "ai-agents",
                "--weekly-health",
                "--vault",
                str(vault),
                "--topics",
                str(topics),
            ],
        )
        assert result.exit_code == 2
        assert "exactly one of --topic, --query, or --weekly-health" in result.output


class TestWeeklyHealthLintsClean:
    def test_post_apply_vault_lints_clean(self, sample_vault: Vault) -> None:
        seed = seed_candidates(sample_vault, today=date(2026, 5, 11))
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        apply_weekly_health(sample_vault, weekly, today=date(2026, 5, 11))
        ctx = LintContext.collect(sample_vault, today=date(2026, 5, 11))
        issues = Linter().run(ctx)
        # Errors are not allowed; warnings (stale, citation-density) are fine.
        errors = [i for i in issues if i.severity == "error"]
        assert errors == [], "\n".join(i.render() for i in errors)


# Convenience export for the smoke check above to avoid Linter import warnings.
__all__ = ["pytest"]
