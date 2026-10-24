"""Tests for ``wikipilot.sources`` (URL normalization, dedupe, page writes)."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from datetime import date

import pytest

from wikipilot.config import ImagesConfig
from wikipilot.sources import (
    SOURCE_FRESHNESS_WINDOW_DAYS,
    detect_mangled_dollar_amounts,
    find_source,
    ingest_source_with_images,
    list_sources,
    load_excerpts_file,
    normalize_url,
    relative_assets_path,
    source_slug,
    update_image_count,
    url_sha256,
    write_source,
)
from wikipilot.wiki import Page, Vault


class TestDetectMangledDollarAmounts:
    """Shapes bash leaves behind when `$N` is expanded inside double quotes."""

    @pytest.mark.parametrize(
        "text",
        [
            "GPT-5.6 Sol now costs  per million input tokens and 0 per million output tokens.",
            "Claude Fable 5 is priced at 0 per million input tokens.",
            "permits commercial use for organizations under 0M annual revenue",
            "sub-130ms first-chunk latency, down to 0 per million characters.",
            "Pricing starts at  per million input tokens",
            "the division had spent 0 billion on content investments",
            "the limited edition is priced at 0 while the standard is 5",
        ],
    )
    def test_flags_real_corruption(self, text: str) -> None:
        assert detect_mangled_dollar_amounts(text), text

    @pytest.mark.parametrize(
        "text",
        [
            "costs $0.60 per million tokens",
            "priced at $10 per million input tokens and $50 per million output tokens",
            "organizations under $100M annual revenue",
            "exploit rates ranging from 0% (Claude Sonnet 4.5) to 40%",
            "from 0 to 100 in 3 seconds",
            "price of 0.5 per image",
            "latency of 0 ms per frame",
            "released in 2026 under the MIT license",
            "a 1.0B parameter model and a 0.46B distilled variant",
        ],
    )
    def test_ignores_legitimate_prose(self, text: str) -> None:
        assert detect_mangled_dollar_amounts(text) == [], text

    def test_reports_each_hit_once(self) -> None:
        hits = detect_mangled_dollar_amounts("organizations under 0M annual revenue")
        assert len(hits) == 1
        assert "0M annual revenue" in hits[0]


class TestLoadExcerptsFile:
    def test_json_array(self, tmp_path) -> None:
        p = tmp_path / "e.json"
        p.write_text('["quote with $10 per million", "second\\nline"]', encoding="utf-8")
        assert load_excerpts_file(p) == ["quote with $10 per million", "second\nline"]

    def test_json_object(self, tmp_path) -> None:
        p = tmp_path / "e.json"
        p.write_text('{"excerpts": ["a", " b "]}', encoding="utf-8")
        assert load_excerpts_file(p) == ["a", "b"]

    def test_paragraph_text(self, tmp_path) -> None:
        p = tmp_path / "e.txt"
        p.write_text("first quote $4\n\n\nsecond quote\n", encoding="utf-8")
        assert load_excerpts_file(p) == ["first quote $4", "second quote"]

    @pytest.mark.parametrize("content", ["", "   \n", "[]", '{"other": 1}', "[not json"])
    def test_rejects_bad_files(self, tmp_path, content: str) -> None:
        p = tmp_path / "e.json"
        p.write_text(content, encoding="utf-8")
        with pytest.raises(ValueError):
            load_excerpts_file(p)


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


@dataclass
class _FakeResponse:
    status_code: int = 200
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes = b""

    def iter_content(self, chunk_size: int) -> Iterator[bytes]:
        for i in range(0, len(self.body), chunk_size):
            yield self.body[i : i + chunk_size]

    def close(self) -> None:
        pass


def _make_getter(responses: dict[str, _FakeResponse]) -> object:
    def getter(url: str, *, timeout: float) -> _FakeResponse:
        if url not in responses:
            raise AssertionError(f"unexpected URL fetched: {url}")
        return responses[url]

    return getter


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
        reread = Page.read(page.path)
        assert reread.metadata["image_count"] == original + 5


class TestRelativeAssetsPath:
    def test_format(self) -> None:
        assert relative_assets_path("foo-12345678") == "../assets/foo-12345678"


class TestIngestSourceWithImages:
    def test_writes_page_and_downloads_images(self, sample_vault: Vault) -> None:
        url = "https://example.com/papers/with-images"
        img_a = "https://cdn.example.com/fig1.png"
        img_b = "https://cdn.example.com/fig2.png"
        body = f"Summary of the paper.\n\n![figure one]({img_a})\n\n![figure two]({img_b})"
        getter = _make_getter(
            {
                img_a: _FakeResponse(
                    headers={"Content-Type": "image/png"}, body=PNG_MAGIC + b"\x00" * 100
                ),
                img_b: _FakeResponse(
                    headers={"Content-Type": "image/png"}, body=PNG_MAGIC + b"\x00" * 100
                ),
            }
        )

        result = ingest_source_with_images(
            sample_vault,
            url=url,
            title="Paper with images",
            topic="ai-agents",
            body=body,
            today=date(2026, 5, 11),
            http_get=getter,
        )

        assert result.record.created
        assert result.image_count == 2
        # On-disk source page reflects the rewritten content + image_count.
        reread = Page.read(result.record.page.path)
        assert reread.metadata["image_count"] == 2
        rel_prefix = relative_assets_path(result.record.slug)
        assert rel_prefix in reread.content
        assert img_a not in reread.content
        assert img_b not in reread.content

        # Files actually written under wiki/assets/<slug>/.
        asset_dir = sample_vault.assets_for(result.record.slug)
        files = list(asset_dir.iterdir())
        assert len(files) == 2

    def test_idempotent_on_existing_source(self, sample_vault: Vault) -> None:
        existing_url = "https://example.com/papers/attention.pdf"
        result = ingest_source_with_images(
            sample_vault,
            url=existing_url,
            title="Different",
            topic="ai-agents",
            body="ignored",
        )
        assert not result.record.created
        assert result.download is None

    def test_disabled_skips_image_step(self, sample_vault: Vault) -> None:
        url = "https://example.com/papers/no-fetch"
        body = "![one](https://cdn.example.com/x.png)"
        cfg = ImagesConfig(enabled=False)

        # No getter passed; if the pipeline ran, fetch_image would try the
        # default `requests.get` and likely succeed/fail unpredictably.
        result = ingest_source_with_images(
            sample_vault,
            url=url,
            title="No fetch",
            topic="ai-agents",
            body=body,
            today=date(2026, 5, 11),
            images=cfg,
        )
        assert result.record.created
        assert result.download is None
        # Source page kept the original remote URL.
        reread = Page.read(result.record.page.path)
        assert "https://cdn.example.com/x.png" in reread.content

    def test_partial_failure_keeps_remote_ref(self, sample_vault: Vault) -> None:
        url = "https://example.com/papers/partial"
        good = "https://cdn.example.com/g.png"
        bad = "https://cdn.example.com/b.html"
        body = f"![g]({good})\n\n![b]({bad})"
        getter = _make_getter(
            {
                good: _FakeResponse(
                    headers={"Content-Type": "image/png"}, body=PNG_MAGIC + b"\x00" * 100
                ),
                bad: _FakeResponse(headers={"Content-Type": "text/html"}, body=b"<html/>"),
            }
        )
        result = ingest_source_with_images(
            sample_vault,
            url=url,
            title="Partial",
            topic="ai-agents",
            body=body,
            today=date(2026, 5, 11),
            http_get=getter,
        )
        assert result.image_count == 1
        reread = Page.read(result.record.page.path)
        assert reread.metadata["image_count"] == 1
        assert good not in reread.content
        assert bad in reread.content
