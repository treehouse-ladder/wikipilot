"""Tests for ``wikipilot.lint`` rules."""

from __future__ import annotations

from datetime import date

from wikipilot.lint import (
    HUMAN_ONLY_PATHS,
    SEVERITY_ERROR,
    LintContext,
    Linter,
    check_broken_local_image_links,
    check_broken_wikilinks,
    check_citation_density,
    check_disputes_open_questions_structure,
    check_divergence_discipline,
    check_frontmatter,
    check_log_format,
    check_orphans,
    check_ownership_violations,
    check_staleness,
)
from wikipilot.wiki import Page, Vault


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

    def test_claude_branch_underscore_scratch_flagged(self, sample_vault: Vault) -> None:
        """``wiki/_*.md`` is the personal-scratch convention and is human-only."""
        ctx = LintContext.collect(
            sample_vault,
            branch_name="claude/daily-2026-05-11/ai-agents",
            changed_paths=(
                "wiki/_dashboard.md",
                "wiki/_inbox.md",
                "wiki/concepts/_local-scratch.md",
                "wiki/concepts/transformer-attention.md",  # OK
            ),
        )
        issues = check_ownership_violations(ctx)
        flagged = {str(i.path) for i in issues if i.severity == SEVERITY_ERROR}
        assert any("_dashboard.md" in p for p in flagged)
        assert any("_inbox.md" in p for p in flagged)
        assert any("_local-scratch.md" in p for p in flagged)
        assert "wiki/concepts/transformer-attention.md" not in flagged


class TestUnderscoreScratchExempt:
    """``_*.md`` files are exempt from frontmatter/citation/orphan rules."""

    def test_dashboard_with_no_frontmatter_does_not_lint(self, sample_vault: Vault) -> None:
        dashboard = sample_vault.root / "_dashboard.md"
        dashboard.write_text(
            "# Dashboard\n\nThis file has no frontmatter and no citations on purpose.\n",
            encoding="utf-8",
        )
        issues = Linter().run(_ctx(sample_vault))
        flagged_paths = {str(i.path) for i in issues}
        assert not any("_dashboard.md" in p for p in flagged_paths), (
            f"_dashboard.md should be exempt from all lint rules, got: {flagged_paths}"
        )

    def test_underscore_file_in_subfolder_also_exempt(self, sample_vault: Vault) -> None:
        scratch = sample_vault.dir_for("concepts") / "_scratch.md"
        scratch.write_text("# Scratch notes\n\nNo frontmatter on purpose.\n", encoding="utf-8")
        issues = Linter().run(_ctx(sample_vault))
        flagged_paths = {str(i.path) for i in issues}
        assert not any("_scratch.md" in p for p in flagged_paths)


class TestCheckBrokenLocalImageLinks:
    def test_clean_vault_passes(self, sample_vault: Vault) -> None:
        issues = check_broken_local_image_links(_ctx(sample_vault))
        assert issues == []

    def test_remote_url_ignored(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(text + "\n![remote](https://example.com/foo.png)\n", encoding="utf-8")
        issues = check_broken_local_image_links(_ctx(sample_vault))
        assert issues == []

    def test_broken_local_ref_flagged(self, sample_vault: Vault) -> None:
        # Source page references a local asset that doesn't exist on disk.
        target = sample_vault.dir_for("sources") / "example-paper-aabbccdd.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text + "\n\n![missing](../assets/example-paper-aabbccdd/missing.png)\n",
            encoding="utf-8",
        )
        issues = check_broken_local_image_links(_ctx(sample_vault))
        assert any(i.code == "broken-image-ref" for i in issues)
        assert all(i.severity == SEVERITY_ERROR for i in issues)

    def test_existing_local_ref_passes(self, sample_vault: Vault) -> None:
        # Drop a real asset on disk and reference it.
        slug = "example-paper-aabbccdd"
        asset_dir = sample_vault.assets_for(slug)
        asset_dir.mkdir(parents=True, exist_ok=True)
        (asset_dir / "fig.png").write_bytes(b"\x89PNG\r\n\x1a\nfake")
        target = sample_vault.dir_for("sources") / f"{slug}.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text + "\n\n![real](../assets/example-paper-aabbccdd/fig.png)\n",
            encoding="utf-8",
        )
        issues = check_broken_local_image_links(_ctx(sample_vault))
        assert not any(i.code == "broken-image-ref" for i in issues)


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


def _write_synthesis_page(
    sample_vault: Vault,
    *,
    name: str = "lonely.md",
    body: str,
    kind: str = "concept",
) -> None:
    """Helper: write a minimal synthesis page with the given body for divergence tests."""
    target = sample_vault.dir_for("concepts" if kind == "concept" else "entities") / name
    frontmatter = (
        "---\n"
        f'title: "Test Page"\n'
        f"kind: {kind}\n"
        "sources: []\n"
        "last_updated: 2026-05-10\n"
        "last_verified: 2026-05-10\n"
        "freshness_window_days: 30\n"
        "---\n\n"
    )
    target.write_text(frontmatter + body, encoding="utf-8")


class TestCheckDivergenceDiscipline:
    def test_warns_on_page_with_no_disputes_no_open_questions_no_sentinel(
        self, sample_vault: Vault
    ) -> None:
        _write_synthesis_page(
            sample_vault,
            name="bare-claim.md",
            body=("# Bare claim\n\n## Summary\n\nBare summary with [[example-paper-aabbccdd]].\n"),
        )
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert any(
            i.code == "divergence-discipline" and i.path.name == "bare-claim.md" for i in issues
        )

    def test_dispute_entry_satisfies(self, sample_vault: Vault) -> None:
        _write_synthesis_page(
            sample_vault,
            name="has-dispute.md",
            body=(
                "# Has dispute\n\n## Summary\n\nClaim [[example-paper-aabbccdd]].\n\n"
                "## Disputes\n\n"
                "- [[example-paper-aabbccdd]] claims X; "
                "[[another-source-deadbeef]] claims not-X. Status: unresolved\n"
            ),
        )
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert not any(
            i.code == "divergence-discipline" and i.path.name == "has-dispute.md" for i in issues
        )

    def test_open_question_entry_satisfies(self, sample_vault: Vault) -> None:
        _write_synthesis_page(
            sample_vault,
            name="has-question.md",
            body=(
                "# Has question\n\n## Summary\n\nClaim [[example-paper-aabbccdd]].\n\n"
                "## Open questions\n\n- [ ] Real question we want to know about?\n"
            ),
        )
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert not any(
            i.code == "divergence-discipline" and i.path.name == "has-question.md" for i in issues
        )

    def test_sentinel_satisfies(self, sample_vault: Vault) -> None:
        _write_synthesis_page(
            sample_vault,
            name="has-sentinel.md",
            body=(
                "# Has sentinel\n\n## Summary\n\nClaim [[example-paper-aabbccdd]].\n\n"
                "_no contradictions or gaps known yet (last reviewed: 2026-05-11)_\n"
            ),
        )
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert not any(
            i.code == "divergence-discipline" and i.path.name == "has-sentinel.md" for i in issues
        )

    def test_does_not_apply_to_source_pages(self, sample_vault: Vault) -> None:
        # Source pages aren't synthesis — divergence rule must not fire on them.
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert not any(
            i.code == "divergence-discipline" and "sources" in str(i.path).replace("\\", "/")
            for i in issues
        )

    def test_placeholder_only_section_does_not_satisfy(self, sample_vault: Vault) -> None:
        # The seeded `_(none yet ...)_` placeholder should NOT count as a real
        # entry — that's the whole point of the divergence-discipline rule.
        _write_synthesis_page(
            sample_vault,
            name="placeholders.md",
            body=(
                "# Placeholders\n\n## Summary\n\nClaim [[example-paper-aabbccdd]].\n\n"
                "## Disputes\n\n_(none yet)_\n\n"
                "## Open questions\n\n_(none yet)_\n"
            ),
        )
        issues = check_divergence_discipline(_ctx(sample_vault))
        assert any(
            i.code == "divergence-discipline" and i.path.name == "placeholders.md" for i in issues
        )


class TestAliasResolution:
    def test_alias_resolves_in_wikilinks(self, sample_vault: Vault) -> None:
        # Add an entity page that declares aliases for a known abbreviation.
        gpt_path = sample_vault.dir_for("entities") / "gpt-4.md"
        gpt_path.write_text(
            "---\n"
            'title: "GPT-4"\n'
            "kind: entity\n"
            'sources: ["[[example-paper-aabbccdd]]"]\n'
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 60\n"
            'aliases: ["GPT 4", "gpt4"]\n'
            "---\n\n"
            "# GPT-4\n\n## Summary\n\nGPT-4 is a frontier LLM [[example-paper-aabbccdd]].\n\n"
            '> "GPT-4 quote."\n\n'
            "_no contradictions or gaps known yet (last reviewed: 2026-05-11)_\n",
            encoding="utf-8",
        )
        # Add a page that links via the alias slug rather than the canonical slug.
        ref = sample_vault.dir_for("concepts") / "alias-ref.md"
        ref.write_text(
            "---\n"
            'title: "Alias ref"\n'
            "kind: concept\n"
            'sources: ["[[example-paper-aabbccdd]]"]\n'
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 30\n"
            "---\n\n"
            "# Alias ref\n\n## Summary\n\n"
            "See [[gpt4]] for the alias path [[example-paper-aabbccdd]].\n\n"
            '> "Alias quote."\n\n'
            "_no contradictions or gaps known yet (last reviewed: 2026-05-11)_\n",
            encoding="utf-8",
        )
        issues = check_broken_wikilinks(_ctx(sample_vault))
        assert not any(i.code == "broken-wikilink" and "gpt4" in i.message for i in issues), (
            "alias slug 'gpt4' must resolve via the entity's aliases:[]"
        )

    def test_alias_prevents_orphan_warning(self, sample_vault: Vault) -> None:
        # Same setup but only the alias is referenced — orphan check should still pass.
        gpt_path = sample_vault.dir_for("entities") / "gpt-4.md"
        gpt_path.write_text(
            "---\n"
            'title: "GPT-4"\n'
            "kind: entity\n"
            'sources: ["[[example-paper-aabbccdd]]"]\n'
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 60\n"
            'aliases: ["GPT 4", "gpt4"]\n'
            "---\n\n"
            "# GPT-4\n\n## Summary\n\nGPT-4 is a frontier LLM [[example-paper-aabbccdd]].\n\n"
            '> "GPT-4 quote."\n',
            encoding="utf-8",
        )
        # Reference via alias only
        ref = sample_vault.dir_for("concepts") / "alias-only.md"
        ref.write_text(
            "---\n"
            'title: "Alias only"\n'
            "kind: concept\n"
            'sources: ["[[example-paper-aabbccdd]]"]\n'
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 30\n"
            "---\n\n"
            "# Alias only\n\n## Summary\n\nSee [[gpt4]] [[example-paper-aabbccdd]].\n",
            encoding="utf-8",
        )
        issues = check_orphans(_ctx(sample_vault))
        assert not any(i.code == "orphan-page" and i.path.name == "gpt-4.md" for i in issues), (
            "entity referenced only via alias must not be flagged orphan"
        )

    def test_page_aliases_property_returns_empty_when_missing(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        assert page.aliases == []

    def test_page_aliases_property_returns_list_when_present(
        self, sample_vault: Vault, tmp_path
    ) -> None:
        path = tmp_path / "with-aliases.md"
        path.write_text(
            "---\n"
            'title: "X"\n'
            "kind: entity\n"
            "sources: []\n"
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 60\n"
            'aliases: ["A", "B"]\n'
            "---\n\nbody\n",
            encoding="utf-8",
        )
        page = Page.read(path)
        assert page.aliases == ["A", "B"]


class TestComparisonFrontmatterLint:
    def test_missing_comparison_of_flagged(self, sample_vault: Vault, tmp_path) -> None:
        path = tmp_path / "bad-comp.md"
        path.write_text(
            "---\n"
            'title: "Bad"\n'
            "kind: comparison\n"
            "sources: []\n"
            "last_updated: 2026-05-10\n"
            "last_verified: 2026-05-10\n"
            "freshness_window_days: 30\n"
            "compare_fields: [cost]\n"
            "---\n\n# Bad\n",
            encoding="utf-8",
        )
        page = Page.read(path)
        errors = page.validate_frontmatter()
        assert any("comparison_of" in e for e in errors)
