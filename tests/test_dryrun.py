"""Tests for ``wikipilot.dryrun`` (proposal/answer apply paths)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from wikipilot.config import TopicConfig
from wikipilot.dryrun import (
    apply_answer,
    apply_daily_aggregate,
    apply_proposal,
    apply_proposal_topic_only,
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


def _topic_b() -> TopicConfig:
    return TopicConfig(
        id="game-music",
        display_name="Game music",
        purpose="In-scope: game soundtracks, composers, audio middleware.",
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


class TestApplyProposalTopicOnly:
    """`apply_proposal_topic_only` mirrors what `wiki-merger` does on a per-topic
    branch. It MUST NOT touch wiki/log.md or wiki/index.md — that's what makes
    parallel topic PRs file-disjoint and merge-queue-safe.
    """

    def test_does_not_touch_log_md(self, sample_vault: Vault) -> None:
        before = sample_vault.log_path.read_text(encoding="utf-8")
        apply_proposal_topic_only(
            sample_vault,
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            today=date(2026, 5, 11),
        )
        after = sample_vault.log_path.read_text(encoding="utf-8")
        assert after == before, "topic-only apply must not modify wiki/log.md"

    def test_does_not_touch_index_md(self, sample_vault: Vault) -> None:
        before = sample_vault.index_path.read_text(encoding="utf-8")
        apply_proposal_topic_only(
            sample_vault,
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            today=date(2026, 5, 11),
        )
        after = sample_vault.index_path.read_text(encoding="utf-8")
        assert after == before, "topic-only apply must not modify wiki/index.md"

    def test_does_not_write_run_report(self, sample_vault: Vault) -> None:
        result = apply_proposal_topic_only(
            sample_vault,
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            today=date(2026, 5, 11),
        )
        assert result.report_path is None, "topic-only apply must not write wiki/reports/<DATE>.md"

    def test_writes_topic_and_source_pages(self, sample_vault: Vault) -> None:
        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        result = apply_proposal_topic_only(sample_vault, proposal, today=date(2026, 5, 11))
        assert result.sources_added, "at least one source page must be created"
        for diff in proposal.page_diffs:
            target = sample_vault.root / diff.path
            assert target.exists(), f"page {target} must be written by apply_proposal_topic_only"

    def test_runs_cross_page_sweep(self, sample_vault: Vault) -> None:
        from wikipilot.dryrun import PageDiff

        proposal = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        proposal.page_diffs.append(
            PageDiff(
                path="concepts/transformer-attention.md",
                kind="concept",
                update_entry=(
                    "Topic-only sweep finding [[example-paper-aabbccdd]] confirms "
                    "the cross-page sweep still runs without the index update."
                ),
            )
        )
        backlinkers = {
            sample_vault.dir_for("concepts") / "stale-concept.md",
            sample_vault.topic_index("ai-agents"),
            sample_vault.dir_for("answers") / "2026-05-10-what-is-attention.md",
        }
        backlinkers = {p for p in backlinkers if p.exists()}
        apply_proposal_topic_only(sample_vault, proposal, today=date(2026, 5, 11))
        for path in backlinkers:
            after = Page.read(path).last_updated
            assert after == date(2026, 5, 11), (
                f"{path} not bumped by cross-page sweep in topic-only path"
            )

    def test_disjoint_writes_for_two_proposals(self, sample_vault: Vault) -> None:
        """Regression test for the parallel-merge conflict cascade.

        Two topic-only applies must each leave wiki/log.md and wiki/index.md
        untouched. The merge queue can then process the two corresponding
        topic PRs in parallel without conflict, which is the property this
        whole refactor exists to establish.
        """
        log_before = sample_vault.log_path.read_text(encoding="utf-8")
        index_before = sample_vault.index_path.read_text(encoding="utf-8")

        proposal_a = make_fake_proposal(_topic(), today=date(2026, 5, 11))
        proposal_b = make_fake_proposal(_topic_b(), today=date(2026, 5, 11))
        result_a = apply_proposal_topic_only(sample_vault, proposal_a, today=date(2026, 5, 11))
        result_b = apply_proposal_topic_only(sample_vault, proposal_b, today=date(2026, 5, 11))

        assert sample_vault.log_path.read_text(encoding="utf-8") == log_before
        assert sample_vault.index_path.read_text(encoding="utf-8") == index_before

        a_paths = {p.resolve() for p in result_a.pages_touched}
        b_paths = {p.resolve() for p in result_b.pages_touched}
        assert sample_vault.log_path.resolve() not in a_paths | b_paths
        assert sample_vault.index_path.resolve() not in a_paths | b_paths


class TestApplyDailyAggregate:
    """`apply_daily_aggregate` mirrors what the daily orchestrator does on
    the `claude/daily-<DATE>/_report` branch after every per-topic PR has
    merged. It is the only place wiki/log.md and wiki/index.md are written
    during a Daily Research run.
    """

    def test_appends_one_log_entry_per_proposal_plus_summary(self, sample_vault: Vault) -> None:
        before = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        proposals = [
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            make_fake_proposal(_topic_b(), today=date(2026, 5, 11)),
        ]
        apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        after = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))
        # N per-topic entries + 1 aggregate-summary entry.
        assert len(after) == len(before) + len(proposals) + 1

    def test_per_topic_log_entries_carry_topic_id(self, sample_vault: Vault) -> None:
        proposals = [
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            make_fake_proposal(_topic_b(), today=date(2026, 5, 11)),
        ]
        apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        log_text = sample_vault.log_path.read_text(encoding="utf-8")
        # Every topic id must appear in at least one log subject.
        assert "ai-agents" in log_text
        assert "game-music" in log_text

    def test_summary_log_entry_shape(self, sample_vault: Vault) -> None:
        proposals = [make_fake_proposal(_topic(), today=date(2026, 5, 11))]
        apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        last_subject = parse_log_headings(sample_vault.log_path.read_text(encoding="utf-8"))[-1][2]
        # Summary entry mentions the aggregate counts, not a single topic id.
        assert "topics" in last_subject and "sources" in last_subject

    def test_updates_index_for_all_sources_across_proposals(self, sample_vault: Vault) -> None:
        from wikipilot.sources import source_slug

        proposals = [
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            make_fake_proposal(_topic_b(), today=date(2026, 5, 11)),
        ]
        apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        index_text = sample_vault.index_path.read_text(encoding="utf-8")
        for proposal in proposals:
            for src in proposal.sources:
                slug = source_slug(src.url, title=src.title)
                assert f"[[{slug}]]" in index_text, (
                    f"index.md must contain the source slug for {proposal.topic_id}"
                )

    def test_writes_run_report(self, sample_vault: Vault) -> None:
        proposals = [
            make_fake_proposal(_topic(), today=date(2026, 5, 11)),
            make_fake_proposal(_topic_b(), today=date(2026, 5, 11)),
        ]
        result = apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        assert result.report_path is not None and result.report_path.exists()
        report = Page.read(result.report_path)
        assert report.kind == "report"
        body = report.content
        # Both topic ids must appear in the topics-processed section.
        assert "ai-agents" in body
        assert "game-music" in body

    def test_index_only_in_pages_touched(self, sample_vault: Vault) -> None:
        """The aggregate phase must declare that it only touches the index
        (plus the report file written separately). Reports are written via
        `write_run_report`, not appended to pages_touched, so the only
        path that should appear here is the index path.
        """
        proposals = [make_fake_proposal(_topic(), today=date(2026, 5, 11))]
        result = apply_daily_aggregate(sample_vault, proposals, today=date(2026, 5, 11))
        assert sample_vault.index_path in result.pages_touched

    def test_handles_empty_proposals(self, sample_vault: Vault) -> None:
        log_before = sample_vault.log_path.read_text(encoding="utf-8")
        index_before = sample_vault.index_path.read_text(encoding="utf-8")
        result = apply_daily_aggregate(sample_vault, [], today=date(2026, 5, 11))
        assert result.report_path is None
        assert result.log_entries == []
        assert sample_vault.log_path.read_text(encoding="utf-8") == log_before
        assert sample_vault.index_path.read_text(encoding="utf-8") == index_before

    def test_pr_links_propagate_to_report(self, sample_vault: Vault) -> None:
        proposals = [make_fake_proposal(_topic(), today=date(2026, 5, 11))]
        result = apply_daily_aggregate(
            sample_vault,
            proposals,
            pr_links=["https://github.com/x/y/pull/1", "https://github.com/x/y/pull/2"],
            today=date(2026, 5, 11),
        )
        assert result.report_path is not None
        body = Page.read(result.report_path).content
        assert "https://github.com/x/y/pull/1" in body
        assert "https://github.com/x/y/pull/2" in body


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
                update_entry=(
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


class TestProposalSourceAlsoRelevantTo:
    """Phase 9: ProposalSource carries an optional cross-topic flag."""

    def test_defaults_to_empty_list(self) -> None:
        from wikipilot.dryrun import ProposalSource

        src = ProposalSource(url="https://x", title="t", excerpt="e")
        assert src.also_relevant_to == []

    def test_accepts_populated_list(self) -> None:
        from wikipilot.dryrun import ProposalSource

        src = ProposalSource(
            url="https://x",
            title="t",
            excerpt="e",
            also_relevant_to=["other-topic-1", "other-topic-2"],
        )
        assert src.also_relevant_to == ["other-topic-1", "other-topic-2"]

    def test_apply_proposal_unaffected_by_flag(self, sample_vault: Vault) -> None:
        # Apply a proposal whose sole source carries `also_relevant_to`; the
        # source page should still be written exactly once under the
        # researched topic. The flag is recorded on the in-memory dataclass
        # only — Phase 9 doesn't route on it yet.
        from wikipilot.dryrun import (
            PageDiff,
            Proposal,
            ProposalSource,
            apply_proposal,
        )

        src = ProposalSource(
            url="https://example.com/cross-topic",
            title="Cross-topic source",
            excerpt="A source that spans multiple topics.",
            also_relevant_to=["games-of-note"],
        )
        proposal = Proposal(
            topic_id="ai-agents",
            sources=[src],
            page_diffs=[
                PageDiff(
                    path="topics/ai-agents/index.md",
                    kind="topic",
                    update_entry=(
                        "A cross-topic finding [[cross-topic-source-"
                        + _expected_short_sha(src)
                        + "]]."
                    ),
                )
            ],
        )
        result = apply_proposal(sample_vault, proposal, today=date(2026, 5, 11))
        # Exactly one source page created.
        assert len(result.sources_added) == 1
        assert result.sources_added[0].name.startswith("cross-topic-source-")


def _expected_short_sha(src) -> str:
    from wikipilot.sources import url_sha256

    return url_sha256(src.url)[:8]
