"""Tests for ``wikipilot.dryrun`` (proposal/answer apply paths)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from wikipilot.config import TopicConfig
from wikipilot.dryrun import (
    apply_answer,
    apply_proposal,
    make_fake_answer,
    make_fake_proposal,
)
from wikipilot.lint import LintContext, Linter
from wikipilot.wiki import Page, Vault, parse_log_headings


def _topic() -> TopicConfig:
    return TopicConfig(
        id="ai-agents",
        display_name="AI agents and agentic systems",
        purpose="In-scope: research and engineering on autonomous LLM agents.",
    )


class TestMakeFakeProposal:
    def test_includes_required_shape(self) -> None:
        proposal = make_fake_proposal(_topic())
        assert proposal.topic_id == "ai-agents"
        assert len(proposal.sources) >= 1
        assert all(s.url and s.title and s.excerpt for s in proposal.sources)
        assert any(s.image_urls for s in proposal.sources)
        assert proposal.page_diffs
        assert any(d.new_disputes for d in proposal.page_diffs)
        assert any(d.new_open_questions for d in proposal.page_diffs)


class TestApplyProposal:
    def test_round_trip_writes_source_and_pages(self, sample_vault: Vault) -> None:
        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        result = apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        assert result.sources_added, "at least one source page must be created"
        assert result.report_path is not None and result.report_path.exists()
        for diff in proposal.page_diffs:
            target = sample_vault.root / diff.path
            assert target.exists(), f"page {target} must be written by apply_proposal"
            page = Page.read(target)
            assert "## Summary" in page.content
            if diff.new_disputes:
                assert "## Disputes" in page.content
            if diff.new_open_questions:
                assert "## Open questions" in page.content

    def test_log_entry_appended(self, sample_vault: Vault) -> None:
        before = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        apply_proposal(
            sample_vault,
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            today=date(2026, 5, 11),
        )
        after = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        assert len(after) == len(before) + 1
        assert after[-1][1] == "daily"
        assert "ai-agents" in after[-1][2]

    def test_source_dedupe(self, sample_vault: Vault) -> None:
        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        first = apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        n_sources_before = len(list((sample_vault.dir_for("sources")).glob("*.md")))
        # Apply again with the same proposal — should not double-write the source.
        apply_proposal(sample_vault, proposal, today=date(2026, 5, 12))
        n_sources_after = len(list((sample_vault.dir_for("sources")).glob("*.md")))
        assert n_sources_after == n_sources_before, "duplicate source pages must not be written"
        assert first.sources_added, "first apply must have created a source page"

    def test_index_updated(self, sample_vault: Vault) -> None:
        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        index_text = sample_vault.index_path.read_text(encoding="utf-8")
        for src in proposal.sources:
            from wikipilot.sources import source_slug

            slug = source_slug(src.url, title=src.title)
            assert f"[[{slug}]]" in index_text


class TestCrossPageSweep:
    def test_touching_concept_updates_backlinking_pages(self, sample_vault: Vault) -> None:
        # Build a proposal that touches `transformer-attention` so the sweep
        # walks every page that backlinks it.
        topic = _topic()
        proposal = make_fake_proposal(topic, today=date(2026, 5, 11))
        # Add a page-diff for transformer-attention itself.
        from wikipilot.dryrun import PageDiff

        proposal.page_diffs.append(
            PageDiff(
                path="concepts/transformer-attention.md",
                kind="concept",
                summary_addition=(
                    "A new dry-run finding [[example-paper-aabbccdd]] confirms attention "
                    "behavior under FP8 precision."
                ),
            )
        )
        # Capture pre-update timestamps on backlinking pages.
        backlinkers = {
            sample_vault.dir_for("concepts") / "stale-concept.md",
            sample_vault.topic_index("ai-agents"),
            sample_vault.dir_for("answers") / "2026-05-10-what-is-attention.md",
        }
        before = {p: Page.read(p).last_updated for p in backlinkers if p.exists()}
        apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        for path, prev in before.items():
            after = Page.read(path).last_updated
            assert after is not None
            assert prev is None or after >= prev
            # The transformer-attention page itself is in page_diffs, so it
            # also gets bumped — that's fine. We're verifying the SWEEP
            # touched pages NOT in page_diffs.
            if path.name != "transformer-attention.md":
                assert after == date(2026, 5, 11), f"{path} not bumped by cross-page sweep"


class TestApplyAnswer:
    def test_round_trip_writes_answer_page(self, sample_vault: Vault) -> None:
        answer = make_fake_answer("What is attention?", today=date(2026, 5, 11))
        result = apply_answer(sample_vault, answer, today=date(2026, 5, 11))
        target = sample_vault.dir_for("answers") / f"{answer.answer_slug}.md"
        assert target.exists()
        page = Page.read(target)
        assert page.kind == "answer"
        assert page.metadata["question"] == "What is attention?"
        assert "## Summary" in page.content
        assert target in result.pages_touched

    def test_back_fill_into_related_pages(self, sample_vault: Vault) -> None:
        answer = make_fake_answer("What is attention?", today=date(2026, 5, 11))
        apply_answer(sample_vault, answer, today=date(2026, 5, 11))
        related = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = related.read_text(encoding="utf-8")
        assert f"[[{answer.answer_slug}]]" in text, (
            "back-fill must add the answer wikilink to the related concept page"
        )

    def test_log_entry_for_query(self, sample_vault: Vault) -> None:
        before = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        apply_answer(
            sample_vault, make_fake_answer("Q?", today=date(2026, 5, 11)), today=date(2026, 5, 11)
        )
        after = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        assert len(after) == len(before) + 1
        assert after[-1][1] == "query"

    def test_idempotent_back_fill(self, sample_vault: Vault) -> None:
        answer = make_fake_answer("What is attention?", today=date(2026, 5, 11))
        apply_answer(sample_vault, answer, today=date(2026, 5, 11))
        apply_answer(sample_vault, answer, today=date(2026, 5, 12))
        related = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = related.read_text(encoding="utf-8")
        assert text.count(f"[[{answer.answer_slug}]]") == 1


class TestDryRunLeavesVaultLintable:
    def test_lint_clean_after_apply(self, sample_vault: Vault) -> None:
        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        ctx = LintContext.collect(sample_vault, today=date(2026, 5, 11))
        issues = Linter().run(ctx)
        # The dry-run output must not introduce ERROR-severity lint issues.
        # Warnings (existing stale page, etc.) are allowed.
        errors = [i for i in issues if i.severity == "error"]
        assert errors == [], "\n".join(i.render() for i in errors)


class TestDryRunCli:
    def test_cli_topic_dispatch(self, sample_vault: Vault, tmp_path: Path) -> None:
        from click.testing import CliRunner

        from wikipilot.cli import main

        # Need a topics.yaml in a place the CLI can find.
        topics_path = tmp_path / "topics.yaml"
        topics_path.write_text(
            'topics:\n  - id: ai-agents\n    display_name: "AI agents"\n    purpose: "test purpose"\n',
            encoding="utf-8",
        )
        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "dry-run",
                "--topic",
                "ai-agents",
                "--vault",
                str(sample_vault.root),
                "--topics",
                str(topics_path),
            ],
        )
        assert result.exit_code == 0, result.output
        assert "Touched" in result.output

    def test_cli_query_dispatch(self, sample_vault: Vault, tmp_path: Path) -> None:
        from click.testing import CliRunner

        from wikipilot.cli import main

        topics_path = tmp_path / "topics.yaml"
        topics_path.write_text(
            'topics:\n  - id: ai-agents\n    display_name: "AI agents"\n    purpose: "test purpose"\n',
            encoding="utf-8",
        )
        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "dry-run",
                "--query",
                "what is attention?",
                "--vault",
                str(sample_vault.root),
                "--topics",
                str(topics_path),
            ],
        )
        assert result.exit_code == 0, result.output
        assert "Wrote answer" in result.output

    def test_cli_requires_exactly_one(self, sample_vault: Vault, tmp_path: Path) -> None:
        from click.testing import CliRunner

        from wikipilot.cli import main

        topics_path = tmp_path / "topics.yaml"
        topics_path.write_text("topics: []\n", encoding="utf-8")
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["dry-run", "--vault", str(sample_vault.root), "--topics", str(topics_path)],
        )
        assert result.exit_code == 2
        result2 = runner.invoke(
            main,
            [
                "dry-run",
                "--topic",
                "x",
                "--query",
                "y",
                "--vault",
                str(sample_vault.root),
                "--topics",
                str(topics_path),
            ],
        )
        assert result2.exit_code == 2


class TestImageRefsInProposal:
    def test_proposal_includes_image_url(self) -> None:
        proposal = make_fake_proposal(_topic())
        assert any(s.image_urls for s in proposal.sources), (
            "every dry-run proposal must include at least one image URL "
            "to exercise the download-source-images path"
        )
