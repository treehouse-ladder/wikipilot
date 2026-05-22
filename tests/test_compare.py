"""Tests for ``wikipilot.compare`` (Phase 9 Pattern A)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest
from click.testing import CliRunner

from wikipilot.cli import main
from wikipilot.compare import (
    UNKNOWN_VALUE,
    aggregate_entity_fields,
    regenerate_comparison,
    render_comparison_table,
    write_comparison_page,
)
from wikipilot.lint import LintContext, Linter
from wikipilot.wiki import Page, Vault, WikiError


def _seed_entity(vault: Vault, slug: str, *, title: str, extra: dict[str, object]) -> Path:
    path = vault.dir_for("entities") / f"{slug}.md"
    metadata: dict[str, object] = {
        "title": title,
        "kind": "entity",
        "sources": ["[[example-paper-aabbccdd]]"],
        "last_updated": date(2026, 5, 11),
        "last_verified": date(2026, 5, 11),
        "freshness_window_days": 60,
    }
    metadata.update(extra)
    body = (
        f"# {title}\n\n## Summary\n\n"
        f"{title} entry seeded for comparison tests [[example-paper-aabbccdd]].\n\n"
        f'> "{title} test seed quote."\n'
    )
    Page.from_dict(path, metadata, body).write()
    return path


class TestAggregateEntityFields:
    def test_returns_per_entity_field_map(self, sample_vault: Vault) -> None:
        _seed_entity(
            sample_vault,
            "alpha",
            title="Alpha",
            extra={"cost_per_mtoken": "5", "context_window": "200000"},
        )
        _seed_entity(
            sample_vault,
            "beta",
            title="Beta",
            extra={"cost_per_mtoken": "8"},
        )
        out = aggregate_entity_fields(
            sample_vault,
            ["alpha", "beta"],
            ["cost_per_mtoken", "context_window"],
        )
        assert out["alpha"]["cost_per_mtoken"] == "5"
        assert out["alpha"]["context_window"] == "200000"
        assert out["beta"]["cost_per_mtoken"] == "8"
        assert "context_window" not in out["beta"]

    def test_missing_entity_returns_empty_dict(self, sample_vault: Vault) -> None:
        out = aggregate_entity_fields(sample_vault, ["nonexistent"], ["any_field"])
        assert out == {"nonexistent": {}}


class TestRenderComparisonTable:
    def test_deterministic_output(self) -> None:
        aggregated = {
            "alpha": {"cost": "5", "ctx": "200k"},
            "beta": {"cost": "8", "ctx": "1m"},
        }
        first = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["cost", "ctx"],
            title="Cost comparison",
        )
        second = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["cost", "ctx"],
            title="Cost comparison",
        )
        assert first == second

    def test_missing_value_renders_unknown(self) -> None:
        aggregated = {"alpha": {"cost": "5"}, "beta": {}}
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["cost", "ctx"],
            title="t",
        )
        assert UNKNOWN_VALUE in out
        assert "[[alpha]]" in out
        assert "[[beta]]" in out

    def test_row_and_column_order_preserved(self) -> None:
        aggregated = {
            "z-entity": {"f1": "a", "f2": "b"},
            "a-entity": {"f1": "c", "f2": "d"},
        }
        out = render_comparison_table(
            aggregated,
            entity_slugs=["z-entity", "a-entity"],
            fields=["f1", "f2"],
            title="t",
        )
        z_pos = out.find("[[z-entity]]")
        a_pos = out.find("[[a-entity]]")
        assert 0 < z_pos < a_pos, "row order must follow caller-provided entity_slugs"


class TestWriteComparisonPage:
    def test_round_trip_lint_clean(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={"cost": "8"})
        path = write_comparison_page(
            sample_vault,
            "cost-comparison",
            title="Cost comparison",
            entity_slugs=["alpha", "beta"],
            fields=["cost"],
            today=date(2026, 5, 11),
        )
        assert path.exists()
        page = Page.read(path)
        assert page.kind == "comparison"
        assert page.metadata["comparison_of"] == ["alpha", "beta"]
        assert page.metadata["compare_fields"] == ["cost"]
        # Frontmatter must be schema-valid (kind == comparison + lists present).
        assert page.validate_frontmatter() == []
        # And the linter must not flag any errors on the new comparison page.
        ctx = LintContext.collect(sample_vault, today=date(2026, 5, 11))
        issues = [i for i in Linter().run(ctx) if i.path == path]
        assert not any(i.severity == "error" for i in issues), (
            "fresh comparison page must be lint-error-free; got: "
            + "\n".join(i.render() for i in issues)
        )

    def test_rejects_too_few_entities(self, sample_vault: Vault) -> None:
        with pytest.raises(WikiError, match="at least 2 entities"):
            write_comparison_page(
                sample_vault,
                "bad",
                title="Bad",
                entity_slugs=["only-one"],
                fields=["cost"],
            )

    def test_rejects_zero_fields(self, sample_vault: Vault) -> None:
        with pytest.raises(WikiError, match="at least 1 field"):
            write_comparison_page(
                sample_vault,
                "bad",
                title="Bad",
                entity_slugs=["a", "b"],
                fields=[],
            )


class TestRegenerateComparison:
    def test_idempotent_bumps_only_last_updated(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={"cost": "8"})
        path = write_comparison_page(
            sample_vault,
            "cost-comparison",
            title="Cost comparison",
            entity_slugs=["alpha", "beta"],
            fields=["cost"],
            today=date(2026, 5, 11),
        )
        original_verified = Page.read(path).last_verified
        # Regenerate "later" — last_updated should bump, last_verified should stick.
        regenerate_comparison(sample_vault, "cost-comparison", today=date(2026, 6, 1))
        page = Page.read(path)
        assert page.last_updated == date(2026, 6, 1)
        assert page.last_verified == original_verified

    def test_picks_up_new_entity_field_values(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={})
        write_comparison_page(
            sample_vault,
            "cost-comparison",
            title="Cost comparison",
            entity_slugs=["alpha", "beta"],
            fields=["cost"],
            today=date(2026, 5, 11),
        )
        first_text = (sample_vault.dir_for("comparisons") / "cost-comparison.md").read_text(
            encoding="utf-8"
        )
        assert UNKNOWN_VALUE in first_text  # beta has no cost yet
        # Backfill beta's cost on its entity page.
        beta_path = sample_vault.dir_for("entities") / "beta.md"
        beta = Page.read(beta_path)
        beta.metadata["cost"] = "8"
        beta.write()
        regenerate_comparison(sample_vault, "cost-comparison", today=date(2026, 5, 11))
        regen_text = (sample_vault.dir_for("comparisons") / "cost-comparison.md").read_text(
            encoding="utf-8"
        )
        assert "| 8 |" in regen_text


class TestCompareCli:
    def test_cli_new_creates_page(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={"cost": "8"})
        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "compare",
                "new",
                "cost-comparison",
                "--of",
                "alpha,beta",
                "--fields",
                "cost",
                "--title",
                "Cost comparison",
                "--vault",
                str(sample_vault.root),
            ],
        )
        assert result.exit_code == 0, result.output
        assert (sample_vault.dir_for("comparisons") / "cost-comparison.md").exists()
        assert "Created comparison" in result.output

    def test_cli_regenerate_idempotent(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={"cost": "8"})
        write_comparison_page(
            sample_vault,
            "cost-comparison",
            title="Cost comparison",
            entity_slugs=["alpha", "beta"],
            fields=["cost"],
            today=date(2026, 5, 11),
        )
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["compare", "regen", "cost-comparison", "--vault", str(sample_vault.root)],
        )
        assert result.exit_code == 0, result.output
        assert "Regenerated comparison" in result.output
        # Second regenerate is also a no-error operation.
        result2 = runner.invoke(
            main,
            ["compare", "regen", "cost-comparison", "--vault", str(sample_vault.root)],
        )
        assert result2.exit_code == 0, result2.output

    def test_cli_missing_comparison_returns_error(self, sample_vault: Vault) -> None:
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["compare", "regen", "no-such", "--vault", str(sample_vault.root)],
        )
        assert result.exit_code == 2
        assert "no comparison page" in result.output


class TestComparisonExcludedFromSynthesisLints:
    def test_citation_density_skips_comparison(self, sample_vault: Vault) -> None:
        _seed_entity(sample_vault, "alpha", title="Alpha", extra={"cost": "5"})
        _seed_entity(sample_vault, "beta", title="Beta", extra={"cost": "8"})
        write_comparison_page(
            sample_vault,
            "cost-comparison",
            title="Cost comparison",
            entity_slugs=["alpha", "beta"],
            fields=["cost"],
        )
        from wikipilot.lint import check_citation_density

        ctx = LintContext.collect(sample_vault, today=date(2026, 5, 11))
        issues = check_citation_density(ctx)
        for issue in issues:
            assert issue.path.name != "cost-comparison.md"


class TestHighlightLeaders:
    def test_bolds_first_italicizes_second_higher_is_better(self) -> None:
        aggregated = {
            "alpha": {"score": 60},
            "beta": {"score": 57},
            "gamma": {"score": 50},
        }
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta", "gamma"],
            fields=["score"],
            title="t",
            highlight_leaders=True,
        )
        assert "**60**" in out  # leader bolded
        assert "_57_" in out  # runner-up italicized
        assert "| 50 |" in out  # third place untouched

    def test_inverts_ordering_for_cost_fields(self) -> None:
        aggregated = {
            "cheap": {"cost": 1.25},
            "mid": {"cost": 3.00},
            "premium": {"cost": 15.00},
        }
        out = render_comparison_table(
            aggregated,
            entity_slugs=["cheap", "mid", "premium"],
            fields=["cost"],
            title="t",
            highlight_leaders=True,
            cost_fields=["cost"],
        )
        assert "**1.25**" in out
        assert "_3.0_" in out
        assert "| 15.0 |" in out

    def test_unknown_values_excluded_from_ranking(self) -> None:
        aggregated = {
            "alpha": {"score": 60},
            "beta": {},
            "gamma": {"score": 70},
        }
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta", "gamma"],
            fields=["score"],
            title="t",
            highlight_leaders=True,
        )
        assert "**70**" in out  # gamma is #1
        assert "_60_" in out  # alpha is #2 (beta has no value)
        assert UNKNOWN_VALUE in out

    def test_single_numeric_value_only_bolds_no_italic(self) -> None:
        aggregated = {"alpha": {"score": 42}, "beta": {}}
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            title="t",
            highlight_leaders=True,
        )
        assert "**42**" in out
        assert "_42_" not in out  # no runner-up to italicize


class TestShowGlosses:
    def test_renders_legend_block_above_table(self) -> None:
        aggregated = {"alpha": {"score": 60}, "beta": {"score": 50}}
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            title="Benchmark",
            show_glosses=True,
            glosses={"score": "Aggregate intelligence; higher is better."},
        )
        legend_pos = out.find("## What each column means for me")
        table_pos = out.find("| Entity |")
        assert legend_pos > 0
        assert table_pos > legend_pos
        assert "Aggregate intelligence" in out

    def test_missing_gloss_falls_back_to_placeholder(self) -> None:
        from wikipilot.compare import NO_GLOSS_PLACEHOLDER

        aggregated = {"alpha": {"score": 60}, "beta": {"score": 50}}
        out = render_comparison_table(
            aggregated,
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            title="t",
            show_glosses=True,
            glosses={},
        )
        assert NO_GLOSS_PLACEHOLDER in out


class TestComputeLeaderChanges:
    """Cover the prior-revision diff path.

    The implementation calls ``_find_repo_root`` on the vault root to bound
    the ``git -C`` invocation. Tests seed a ``.git`` placeholder dir inside
    the tempdir vault so the resolution succeeds, then inject a fake
    runner to stand in for the real ``git show HEAD:<path>`` call.
    """

    @staticmethod
    def _seed_git_marker(vault: Vault) -> None:
        (vault.root.parent / ".git").mkdir(exist_ok=True)

    def test_returns_none_when_git_show_fails(self, sample_vault: Vault) -> None:
        from wikipilot.compare import compute_leader_changes

        self._seed_git_marker(sample_vault)
        path = sample_vault.dir_for("comparisons") / "x.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")

        def fake_runner(args: list[str]):  # type: ignore[no-untyped-def]
            import subprocess

            return subprocess.CompletedProcess(args, returncode=128, stdout="", stderr="not found")

        result = compute_leader_changes(
            sample_vault,
            path,
            aggregated={"alpha": {"score": 60}, "beta": {"score": 50}},
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            git_runner=fake_runner,
        )
        assert result is None

    def test_detects_leader_swap_from_prior_revision(self, sample_vault: Vault) -> None:
        """When the prior revision had `**beta**` bolded for `score` and today's
        aggregated puts alpha at #1, emit a bullet announcing the swap."""
        from wikipilot.compare import compute_leader_changes

        self._seed_git_marker(sample_vault)
        prior_table = (
            "# title\n\n## Summary\n\nblah\n\n"
            "| Entity | score |\n"
            "| --- | --- |\n"
            "| [[alpha]] | _50_ |\n"
            "| [[beta]] | **60** |\n"
        )

        def fake_runner(args: list[str]):  # type: ignore[no-untyped-def]
            import subprocess

            return subprocess.CompletedProcess(args, returncode=0, stdout=prior_table, stderr="")

        path = sample_vault.dir_for("comparisons") / "x.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
        result = compute_leader_changes(
            sample_vault,
            path,
            aggregated={"alpha": {"score": 70}, "beta": {"score": 60}},
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            git_runner=fake_runner,
        )
        assert result is not None
        assert "[[alpha]]" in result
        assert "[[beta]]" in result
        assert "took #1" in result

    def test_no_change_returns_none(self, sample_vault: Vault) -> None:
        from wikipilot.compare import compute_leader_changes

        self._seed_git_marker(sample_vault)
        prior_table = (
            "# title\n\n## Summary\n\nblah\n\n"
            "| Entity | score |\n"
            "| --- | --- |\n"
            "| [[alpha]] | **60** |\n"
            "| [[beta]] | _50_ |\n"
        )

        def fake_runner(args: list[str]):  # type: ignore[no-untyped-def]
            import subprocess

            return subprocess.CompletedProcess(args, returncode=0, stdout=prior_table, stderr="")

        path = sample_vault.dir_for("comparisons") / "x.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
        result = compute_leader_changes(
            sample_vault,
            path,
            aggregated={"alpha": {"score": 70}, "beta": {"score": 50}},
            entity_slugs=["alpha", "beta"],
            fields=["score"],
            git_runner=fake_runner,
        )
        assert result is None  # alpha was leader before and after
