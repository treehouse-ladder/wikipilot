"""Tests for ``wikipilot.wiki`` primitives."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from wikipilot.wiki import (
    REQUIRED_FRONTMATTER,
    Page,
    Vault,
    parse_log_headings,
    parse_wikilinks,
    slugify,
)


class TestSlugify:
    def test_basic(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_unicode(self) -> None:
        assert slugify("café crème") == "cafe-creme"

    def test_punctuation_collapsed(self) -> None:
        assert slugify("foo!! bar??  baz") == "foo-bar-baz"

    def test_empty(self) -> None:
        assert slugify("") == ""

    def test_numbers_kept(self) -> None:
        assert slugify("Claude 4.7 Opus") == "claude-4-7-opus"


class TestParseWikilinks:
    def test_simple(self) -> None:
        assert parse_wikilinks("see [[foo]] and [[bar]]") == ["foo", "bar"]

    def test_alias(self) -> None:
        assert parse_wikilinks("see [[foo|the foo]]") == ["foo"]

    def test_section_ref(self) -> None:
        assert parse_wikilinks("see [[foo#summary]]") == ["foo"]

    def test_alias_with_section(self) -> None:
        assert parse_wikilinks("see [[foo#summary|the foo summary]]") == ["foo"]

    def test_no_links(self) -> None:
        assert parse_wikilinks("plain text with [brackets] but no links") == []


class TestParseLogHeadings:
    def test_well_formed(self) -> None:
        log = (
            "# Log\n\n"
            "## [2026-05-10] daily | ai-agents — 1 source\n\nFoo.\n\n"
            "## [2026-05-11] query | what is X?\n\nBar.\n"
        )
        headings = parse_log_headings(log)
        assert len(headings) == 2
        assert headings[0][0] == "2026-05-10"
        assert headings[0][1] == "daily"
        assert headings[1][1] == "query"

    def test_malformed_skipped(self) -> None:
        log = "## not a log entry\n\n## [2026-05-10] daily | ok\n\nFoo.\n"
        headings = parse_log_headings(log)
        assert len(headings) == 1


class TestPage:
    def test_read_existing(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        assert page.kind == "concept"
        assert page.title == "Transformer attention"
        assert page.last_verified == date(2026, 5, 10)
        assert page.freshness_window_days == 30
        assert page.sources == ["[[example-paper-aabbccdd]]"]

    def test_validate_clean_page(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        assert page.validate_frontmatter() == []

    def test_validate_missing_keys(self, tmp_path: Path) -> None:
        path = tmp_path / "broken.md"
        path.write_text("---\ntitle: only title\n---\n\nbody\n", encoding="utf-8")
        page = Page.read(path)
        errors = page.validate_frontmatter()
        # All required keys except 'title' should be missing.
        for key in REQUIRED_FRONTMATTER:
            if key == "title":
                continue
            assert any(key in e for e in errors), f"expected error mentioning {key!r}"

    def test_validate_invalid_kind(self, tmp_path: Path) -> None:
        path = tmp_path / "broken.md"
        path.write_text(
            "---\n"
            "title: foo\nkind: bogus\nsources: []\n"
            "last_updated: 2026-05-10\nlast_verified: 2026-05-10\n"
            "freshness_window_days: 30\n---\n\nbody\n",
            encoding="utf-8",
        )
        page = Page.read(path)
        errors = page.validate_frontmatter()
        assert any("invalid kind" in e for e in errors)

    def test_bump_freshness_updates_only(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        old_verified = page.last_verified
        page.bump_freshness(verified=False, today=date(2026, 6, 1))
        assert page.last_updated == date(2026, 6, 1)
        assert page.last_verified == old_verified

    def test_bump_freshness_verified(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        page.bump_freshness(verified=True, today=date(2026, 6, 1))
        assert page.last_verified == date(2026, 6, 1)

    def test_is_stale_detected(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "stale-concept.md")
        assert page.is_stale(today=date(2026, 5, 10)) is True

    def test_is_stale_fresh(self, sample_vault: Vault) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        assert page.is_stale(today=date(2026, 5, 10)) is False

    def test_write_round_trip(self, sample_vault: Vault, tmp_path: Path) -> None:
        page = Page.read(sample_vault.dir_for("concepts") / "transformer-attention.md")
        target = tmp_path / "round-trip.md"
        page.path = target
        page.write()
        reread = Page.read(target)
        assert reread.title == page.title
        assert reread.kind == page.kind
        assert reread.content.strip() == page.content.strip()


class TestVault:
    def test_paths(self, tmp_path: Path) -> None:
        vault = Vault.at(tmp_path / "wiki")
        assert vault.dir_for("concepts") == (tmp_path / "wiki" / "concepts").resolve()
        assert (
            vault.topic_index("foo")
            == (tmp_path / "wiki" / "topics" / "foo" / "index.md").resolve()
        )
        assert (
            vault.topic_purpose("foo")
            == (tmp_path / "wiki" / "topics" / "foo" / "purpose.md").resolve()
        )

    def test_unknown_kind_raises(self, tmp_path: Path) -> None:
        vault = Vault.at(tmp_path)
        with pytest.raises(ValueError):
            vault.dir_for("not-a-real-dir")

    def test_iter_markdown_files(self, sample_vault: Vault) -> None:
        files = list(sample_vault.iter_markdown_files())
        names = {p.name for p in files}
        assert "index.md" in names
        assert "log.md" in names
        assert "transformer-attention.md" in names

    def test_comparisons_dir_known(self, tmp_path: Path) -> None:
        # Phase 9: `comparisons` is a first-class wiki subdirectory, mirroring
        # `concepts` and `entities`.
        vault = Vault.at(tmp_path / "wiki")
        assert vault.dir_for("comparisons") == (tmp_path / "wiki" / "comparisons").resolve()
        assert (
            vault.page_path("comparison", "cost-comparison")
            == (tmp_path / "wiki" / "comparisons" / "cost-comparison.md").resolve()
        )


class TestComparisonKindRoundTrip:
    def test_round_trip_through_page_read_write(self, tmp_path: Path) -> None:
        # Phase 9 Pattern A: `comparison` is a valid kind; round-trip a minimal
        # comparison page through Page.write -> Page.read and confirm the
        # kind/comparison_of/compare_fields keys all survive.
        from datetime import date

        path = tmp_path / "comp.md"
        page = Page.from_dict(
            path,
            metadata={
                "title": "Cost comparison",
                "kind": "comparison",
                "comparison_of": ["alpha", "beta"],
                "compare_fields": ["cost", "ctx"],
                "sources": [],
                "last_updated": date(2026, 5, 11),
                "last_verified": date(2026, 5, 11),
                "freshness_window_days": 30,
            },
            content="# Cost comparison\n\n| Entity | cost | ctx |\n| --- | --- | --- |\n",
        )
        page.write()
        reread = Page.read(path)
        assert reread.kind == "comparison"
        assert reread.metadata["comparison_of"] == ["alpha", "beta"]
        assert reread.metadata["compare_fields"] == ["cost", "ctx"]
        assert reread.validate_frontmatter() == []
