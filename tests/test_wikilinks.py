"""Tests for ``wikipilot.wikilinks`` — shared resolve + auto-fix helpers."""

from __future__ import annotations

from pathlib import Path

from wikipilot.wiki import Vault
from wikipilot.wikilinks import (
    ResolveReport,
    autofix_wikilink,
    resolve_or_fix_in_files,
    resolve_wikilink,
)


class TestResolveWikilink:
    def test_resolves_against_known(self) -> None:
        known = {"transformer-attention", "anthropic"}
        assert resolve_wikilink("transformer-attention", known) is True
        assert resolve_wikilink("anthropic", known) is True

    def test_resolves_via_slugify(self) -> None:
        known = {"transformer-attention"}
        assert resolve_wikilink("Transformer Attention", known) is True

    def test_extra_set_unions_with_known(self) -> None:
        assert (
            resolve_wikilink(
                "from-proposal-abc12345",
                known=set(),
                extra={"from-proposal-abc12345"},
            )
            is True
        )

    def test_unresolved_returns_false(self) -> None:
        assert resolve_wikilink("totally-not-real", {"some-other"}) is False

    def test_empty_target_returns_false(self) -> None:
        assert resolve_wikilink("", {"anything"}) is False
        assert resolve_wikilink("   ", {"anything"}) is False


class TestAutofixWikilinkShaSuffix:
    def test_unique_sha_match_returns_canonical_stem(self, sample_vault: Vault) -> None:
        # The sample vault has ``sources/example-paper-aabbccdd.md``. A target
        # with a typo before the SHA (e.g. ``example-papre-aabbccdd``) should
        # still resolve via the SHA suffix.
        assert autofix_wikilink("example-papre-aabbccdd", sample_vault) == "example-paper-aabbccdd"

    def test_exact_match_via_sha(self, sample_vault: Vault) -> None:
        assert autofix_wikilink("example-paper-aabbccdd", sample_vault) == "example-paper-aabbccdd"

    def test_no_match_returns_none(self, sample_vault: Vault) -> None:
        # SHA that doesn't exist anywhere in the vault.
        assert autofix_wikilink("some-page-deadc0de", sample_vault) is None

    def test_ambiguous_sha_returns_none(self, sample_vault: Vault, tmp_path: Path) -> None:
        # Create a second source with the same SHA suffix → ambiguous → None.
        second = sample_vault.dir_for("sources") / "different-page-aabbccdd.md"
        second.write_text(
            "---\ntitle: Different page\nkind: source\nurl: https://other\nsha256: x\n"
            "fetched_at: 2026-05-10\ntopic: ai-agents\nimage_count: 0\nsources: []\n"
            "last_updated: 2026-05-10\nlast_verified: 2026-05-10\nfreshness_window_days: 365\n---\n"
            "\nbody\n",
            encoding="utf-8",
        )
        assert autofix_wikilink("example-paper-aabbccdd", sample_vault) is None


class TestAutofixWikilinkSlugify:
    def test_slugify_match_via_title(self, sample_vault: Vault) -> None:
        # The sample vault has ``concepts/transformer-attention.md`` with
        # title "Transformer attention" — both stem and title slugify to the
        # same thing, so a casing/spacing typo should resolve.
        assert autofix_wikilink("Transformer Attention", sample_vault) == "transformer-attention"

    def test_no_slug_match_returns_none(self, sample_vault: Vault) -> None:
        assert autofix_wikilink("something-totally-unrelated", sample_vault) is None


class TestResolveOrFixInFiles:
    def test_resolved_targets_recorded(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(text + "\nSee [[anthropic]] for more.\n", encoding="utf-8")
        report = resolve_or_fix_in_files([target], sample_vault)
        assert "anthropic" in report.resolved
        assert report.autofixed == []
        assert report.unresolved == []

    def test_autofix_rewrites_file_in_place(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        # Insert a wikilink with a typo before the SHA suffix that matches
        # the only ``-aabbccdd`` source in the vault.
        target.write_text(
            text + "\nThis source [[example-papre-aabbccdd]] discussed it.\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files([target], sample_vault)
        assert len(report.autofixed) == 1
        path, old, new = report.autofixed[0]
        assert path == target
        assert old == "example-papre-aabbccdd"
        assert new == "example-paper-aabbccdd"
        # The file on disk now contains the corrected slug.
        assert "[[example-paper-aabbccdd]]" in target.read_text(encoding="utf-8")
        assert "[[example-papre-aabbccdd]]" not in target.read_text(encoding="utf-8")
        assert report.unresolved == []

    def test_unresolvable_link_recorded(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text + "\nThis page [[truly-nonexistent-12345678]] won't fix.\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files([target], sample_vault)
        assert report.autofixed == []
        assert any(link == "truly-nonexistent-12345678" for _, link in report.unresolved)

    def test_proposal_slugs_treated_as_known(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text + "\nNew source [[soon-to-exist-deadbeef]] just landed.\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files(
            [target], sample_vault, proposal_slugs={"soon-to-exist-deadbeef"}
        )
        # Resolved against the proposal-supplied slug; no rewrite, no error.
        assert "soon-to-exist-deadbeef" in report.resolved
        assert report.autofixed == []
        assert report.unresolved == []

    def test_alias_and_section_suffix_preserved_on_rewrite(self, sample_vault: Vault) -> None:
        target = sample_vault.dir_for("concepts") / "transformer-attention.md"
        text = target.read_text(encoding="utf-8")
        # The typo target has a section anchor and an alias — both should
        # survive the rewrite to the canonical slug.
        target.write_text(
            text + "\nSee [[example-papre-aabbccdd#section|the paper]] for details.\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files([target], sample_vault)
        assert len(report.autofixed) == 1
        rewritten = target.read_text(encoding="utf-8")
        assert "[[example-paper-aabbccdd#section|the paper]]" in rewritten

    def test_empty_paths_yields_empty_report(self, sample_vault: Vault) -> None:
        report = resolve_or_fix_in_files([], sample_vault)
        assert isinstance(report, ResolveReport)
        assert report.resolved == []
        assert report.autofixed == []
        assert report.unresolved == []
