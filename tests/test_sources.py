"""Tests for ``wikipilot.sources`` (URL normalization, dedupe, page writes)."""

from __future__ import annotations

from datetime import date

from wikipilot.sources import (
    SOURCE_FRESHNESS_WINDOW_DAYS,
    find_source,
    list_sources,
    normalize_url,
    source_slug,
    update_image_count,
    url_sha256,
    write_source,
)
from wikipilot.wiki import Vault


class TestNormalizeUrl:
    def test_lowercase_scheme_and_host(self) -> None:
        assert normalize_url("HTTPS://EXAMPLE.com/Foo") == "https://example.com/Foo"

    def test_strip_fragment(self) -> None:
        assert normalize_url("https://example.com/foo#bar") == "https://example.com/foo"

    def test_sort_query_params(self) -> None:
        a = normalize_url("https://example.com/foo?b=2&a=1")
        b = normalize_url("https://example.com/foo?a=1&b=2")
        assert a == b

    def test_root_path_normalized(self) -> None:
        assert normalize_url("https://example.com") == "https://example.com/"
        assert normalize_url("https://example.com/") == "https://example.com/"

    def test_trailing_slash_stripped(self) -> None:
        assert normalize_url("https://example.com/foo/") == "https://example.com/foo"

    def test_default_scheme(self) -> None:
        assert normalize_url("example.com/foo").endswith("/foo")


class TestUrlSha256:
    def test_deterministic(self) -> None:
        assert url_sha256("https://example.com/x") == url_sha256("https://example.com/x")

    def test_normalization_dedupes(self) -> None:
        assert url_sha256("HTTPS://Example.com/x") == url_sha256("https://example.com/x")

    def test_different_paths_diff_hashes(self) -> None:
        assert url_sha256("https://example.com/a") != url_sha256("https://example.com/b")


class TestSourceSlug:
    def test_uses_title(self) -> None:
        slug = source_slug("https://example.com/x", title="An Example Paper")
        assert slug.startswith("an-example-paper-")

    def test_falls_back_to_path(self) -> None:
        slug = source_slug("https://example.com/foo/bar.html")
        assert slug.startswith("bar-html-")

    def test_falls_back_to_host(self) -> None:
        slug = source_slug("https://example.com/")
        assert slug.startswith("example-com-")


class TestWriteSource:
    def test_creates_new_source(self, sample_vault: Vault) -> None:
        record = write_source(
            sample_vault,
            url="https://example.com/new-paper",
            title="A new paper",
            topic="ai-agents",
            body="Summary of the paper.",
            today=date(2026, 5, 11),
            excerpts=["A direct quote.", "Another quote."],
        )
        assert record.created is True
        assert record.page.kind == "source"
        assert record.page.metadata["url"] == "https://example.com/new-paper"
        assert record.page.metadata["topic"] == "ai-agents"
        assert record.page.metadata["image_count"] == 0
        assert record.page.freshness_window_days == SOURCE_FRESHNESS_WINDOW_DAYS
        assert "## Excerpts" in record.page.content
        assert "> A direct quote." in record.page.content
        assert "> Another quote." in record.page.content

    def test_dedupes_by_normalized_url(self, sample_vault: Vault) -> None:
        write_source(
            sample_vault,
            url="https://example.com/same",
            title="First",
            topic="ai-agents",
            body="b1",
        )
        record2 = write_source(
            sample_vault,
            url="HTTPS://Example.com/same/",
            title="Second",
            topic="ai-agents",
            body="b2",
        )
        assert record2.created is False
        assert record2.page.title == "First"

    def test_existing_returned_unchanged(self, sample_vault: Vault) -> None:
        existing_url = "https://example.com/papers/attention.pdf"
        record = write_source(
            sample_vault,
            url=existing_url,
            title="Different title",
            topic="ai-agents",
            body="b",
        )
        assert record.created is False
        assert record.page.title == "An example paper on attention"


class TestFindSource:
    def test_finds_by_normalized_url(self, sample_vault: Vault) -> None:
        page = find_source(sample_vault, "HTTPS://Example.com/papers/attention.pdf")
        assert page is not None
        assert page.title == "An example paper on attention"

    def test_returns_none_for_unknown(self, sample_vault: Vault) -> None:
        assert find_source(sample_vault, "https://example.com/never-seen") is None


class TestListSources:
    def test_returns_all(self, sample_vault: Vault) -> None:
        sources = list_sources(sample_vault)
        assert len(sources) == 2
        slugs = {s.path.stem for s in sources}
        assert "example-paper-aabbccdd" in slugs
        assert "another-source-deadbeef" in slugs


class TestUpdateImageCount:
    def test_persists_count(self, sample_vault: Vault) -> None:
        sources = list_sources(sample_vault)
        page = sources[0]
        original = page.metadata["image_count"]
        update_image_count(page, original + 5)
        from wikipilot.wiki import Page

        reread = Page.read(page.path)
        assert reread.metadata["image_count"] == original + 5
