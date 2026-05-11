"""Tests for ``wikipilot.lint`` rules."""

from __future__ import annotations

from datetime import date

from wikipilot.lint import (
    HUMAN_ONLY_PATHS,
    SEVERITY_ERROR,
    LintContext,
    Linter,
    check_broken_wikilinks,
    check_citation_density,
    check_disputes_open_questions_structure,
    check_frontmatter,
    check_log_format,
    check_orphans,
    check_ownership_violations,
    check_staleness,
)
from wikipilot.wiki import Vault


def _ctx(vault: Vault, **kwargs: object) -> LintContext:
    today = kwargs.pop("today", date(2026, 5, 10))
    return LintContext.collect(vault, today=today, **kwargs)  # type: ignore[arg-type]


class TestCheckFrontmatter:
    def test_clean_vault_passes(self, sample_vault: Vault) -> None:
        issues = check_frontmatter(_ctx(sample_vault))
        assert issues == []

    def test_missing_keys_flagged(self, sample_vault: Vault) -> None:
        # Mutate one page in the temp vault to drop required fields.
        bad = sample_vault.dir_for("concepts") / "transformer-attention.md"
        bad.write_text("---\ntitle: Foo\n---\n\nbody\n", encoding="utf-8")
        issues = check_frontmatter(_ctx(sample_vault))
        assert any(i.code == "frontmatter" for i in issues)


class TestCheckLogFormat:
    def test_clean_log_passes(self, sample_vault: Vault) -> None:
        issues = check_log_format(_ctx(sample_vault))
        assert issues == []

    def test_malformed_heading_flagged(self, sample_vault: Vault) -> None:
        log_path = sample_vault.log_path
        log_path.write_text(
            "# Log\n\n## not a valid heading\n\n## [2026-05-10] daily | ok\n\nFoo.\n",
            encoding="utf-8",
        )
        issues = check_log_format(_ctx(sample_vault))
        assert len(issues) == 1
        assert issues[0].severity == SEVERITY_ERROR
        assert issues[0].code == "log-format"


class TestCheckBrokenWikilinks:
    def test_clean_vault_passes(self, sample_vault: Vault) -> None:
        # Sample vault contains a wikilink to "another-source-deadbeef" inside
        # a Disputes entry; the corresponding source page exists, so this
        # should be clean.
        issues = check_broken_wikilinks(_ctx(sample_vault))
        bad = [i for i in issues if i.severity == SEVERITY_ERROR]
        assert bad == []

    def test_broken_link_flagged(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        original = target.read_text(encoding="utf-8")
        target.write_text(original + "\nSee [[totally-not-real-page]]\n", encoding="utf-8")
        issues = check_broken_wikilinks(_ctx(sample_vault))
        assert any(i.code == "broken-wikilink" for i in issues)


class TestCheckOrphans:
    def test_orphan_flagged(self, sample_vault: Vault) -> None:
        # Add a brand-new concept page that nothing links to.
        new = sample_vault.dir_for("concepts") / "lonely.md"
        new.write_text(
            "---\n"
            "title: Lonely\nkind: concept\nsources: []\n"
            "last_updated: 2026-05-10\nlast_verified: 2026-05-10\n"
            "freshness_window_days: 30\n---\n\n## Summary\n\nNobody links here.\n",
            encoding="utf-8",
        )
        issues = check_orphans(_ctx(sample_vault))
        assert any(i.code == "orphan-page" and i.path.name == "lonely.md" for i in issues)

    def test_linked_page_not_orphan(self, sample_vault: Vault) -> None:
        issues = check_orphans(_ctx(sample_vault))
        # transformer-attention is referenced by index.md and the answer page
        assert not any(i.path.name == "transformer-attention.md" for i in issues)


class TestCheckStaleness:
    def test_stale_page_flagged(self, sample_vault: Vault) -> None:
        issues = check_staleness(_ctx(sample_vault, today=date(2026, 5, 10)))
        assert any(i.code == "stale-page" and i.path.name == "stale-concept.md" for i in issues)

    def test_fresh_pages_pass(self, sample_vault: Vault) -> None:
        issues = check_staleness(_ctx(sample_vault, today=date(2026, 5, 10)))
        assert not any(i.path.name == "transformer-attention.md" for i in issues)


class TestCheckCitationDensity:
    def test_uncited_paragraph_flagged(self, sample_vault: Vault) -> None:
        issues = check_citation_density(_ctx(sample_vault))
        assert any(
            i.code == "citation-density" and i.path.name == "thin-citations.md" for i in issues
        )

    def test_well_cited_page_passes(self, sample_vault: Vault) -> None:
        issues = check_citation_density(_ctx(sample_vault))
        assert not any(i.path.name == "transformer-attention.md" for i in issues)


class TestCheckDisputesOpenQuestionsStructure:
    def test_clean_vault_passes(self, sample_vault: Vault) -> None:
        issues = check_disputes_open_questions_structure(_ctx(sample_vault))
        assert issues == []

    def test_malformed_dispute_flagged(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        # Replace the well-formed Disputes line with a broken one
        broken = text.replace(
            "- [[example-paper-aabbccdd]] claims sqrt(d_k) scaling is necessary; [[another-source-deadbeef]] claims not-needed for small models. Status: unresolved",
            "no bullet, no claims marker",
        )
        target.write_text(broken, encoding="utf-8")
        issues = check_disputes_open_questions_structure(_ctx(sample_vault))
        assert any(i.code == "disputes-format" for i in issues)

    def test_malformed_open_question_flagged(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        broken = text.replace(
            "- [ ] How does attention behave with FP8 precision in agentic loops?",
            "this is not a checkbox",
        )
        target.write_text(broken, encoding="utf-8")
        issues = check_disputes_open_questions_structure(_ctx(sample_vault))
        assert any(i.code == "open-questions-format" for i in issues)


class TestCheckOwnershipViolations:
    def test_no_branch_no_check(self, sample_vault: Vault) -> None:
        issues = check_ownership_violations(_ctx(sample_vault))
        assert issues == []

    def test_human_branch_no_check(self, sample_vault: Vault) -> None:
        ctx = LintContext.collect(
            sample_vault,
            branch_name="main",
            changed_paths=("CLAUDE.md",),
        )
        issues = check_ownership_violations(ctx)
        assert issues == []

    def test_claude_branch_human_only_modify_flagged(self, sample_vault: Vault) -> None:
        ctx = LintContext.collect(
            sample_vault,
            branch_name="claude/daily-2026-05-11/ai-agents",
            changed_paths=(
                "CLAUDE.md",
                "wiki/topics/ai-agents/purpose.md",
                "topics.yaml",
                "wiki/concepts/transformer-attention.md",  # OK
            ),
        )
        issues = check_ownership_violations(ctx)
        flagged = {str(i.path) for i in issues if i.severity == SEVERITY_ERROR}
        assert "CLAUDE.md" in flagged
        assert "topics.yaml" in flagged
        assert any("purpose.md" in p for p in flagged)
        # The mixed-ownership concept page must NOT be flagged.
        assert "wiki/concepts/transformer-attention.md" not in flagged


class TestLinterEndToEnd:
    def test_runs_all_rules(self, sample_vault: Vault) -> None:
        issues = Linter().run(_ctx(sample_vault))
        # Sample vault is intentionally messy: stale-concept and thin-citations
        # should produce warnings; no errors expected.
        assert not Linter.has_errors(issues)
        codes = {i.code for i in issues}
        assert "stale-page" in codes
        assert "citation-density" in codes

    def test_human_only_constants(self) -> None:
        assert "CLAUDE.md" in HUMAN_ONLY_PATHS
        assert "topics.yaml" in HUMAN_ONLY_PATHS
        assert "wikipilot.toml" in HUMAN_ONLY_PATHS
        assert "prompts/" in HUMAN_ONLY_PATHS
