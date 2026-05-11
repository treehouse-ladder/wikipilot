"""Tests for the Phase 1 image-helper surface and the Phase 5 fetch pipeline."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from wikipilot.images import (
    DEFAULT_ALLOWED_MIMES,
    DEFAULT_MAX_BYTES,
    MIME_TO_EXT,
    SKIP_REASONS,
    download_for_source,
    fetch_image,
    parse_image_refs,
    rewrite_refs,
    safe_filename,
    sniff_mime,
)

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff\xe0"
GIF_MAGIC = b"GIF89a"
WEBP_MAGIC = b"RIFF\x00\x00\x00\x00WEBP"
SVG_MAGIC = b"<svg xmlns='http://www.w3.org/2000/svg'></svg>"


@dataclass
class FakeResponse:
    """Minimal stand-in for ``requests.Response``."""

    status_code: int = 200
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes = b""
    chunk_size: int = 8192
    raise_on_iter: Exception | None = None
    closed: bool = False

    def iter_content(self, chunk_size: int) -> Iterator[bytes]:
        if self.raise_on_iter is not None:
            raise self.raise_on_iter
        for i in range(0, len(self.body), chunk_size):
            yield self.body[i : i + chunk_size]

    def close(self) -> None:
        self.closed = True


def make_getter(responses: dict[str, FakeResponse | Exception]) -> object:
    """Return a callable that dispatches by URL to the prepared fakes."""

    def getter(url: str, *, timeout: float) -> FakeResponse:
        if url not in responses:
            raise AssertionError(f"unexpected URL fetched in test: {url}")
        prepared = responses[url]
        if isinstance(prepared, Exception):
            raise prepared
        return prepared

    return getter


class TestSafeFilename:
    def test_includes_sha_prefix(self) -> None:
        name = safe_filename("https://example.com/foo.png", "png")
        assert "-foo." in name
        prefix, _ = name.split("-", 1)
        assert len(prefix) == 8

    def test_extension_used(self) -> None:
        name = safe_filename("https://example.com/foo", "jpg")
        assert name.endswith(".jpg")

    def test_dedupes_extensions(self) -> None:
        name = safe_filename("https://example.com/foo.jpg", "jpg")
        assert name.endswith(".jpg")
        assert ".jpg.jpg" not in name

    def test_default_basename(self) -> None:
        name = safe_filename("https://example.com/", "png")
        assert "image" in name


class TestParseImageRefs:
    def test_markdown_image(self) -> None:
        refs = parse_image_refs("![alt text](https://example.com/foo.png)")
        assert len(refs) == 1
        assert refs[0].alt == "alt text"
        assert refs[0].src == "https://example.com/foo.png"

    def test_html_image(self) -> None:
        refs = parse_image_refs('<img src="https://example.com/foo.png" alt="hello">')
        assert len(refs) == 1
        assert refs[0].src == "https://example.com/foo.png"
        assert refs[0].alt == "hello"

    def test_html_image_self_closing(self) -> None:
        refs = parse_image_refs('<img src="https://example.com/foo.png" />')
        assert len(refs) == 1
        assert refs[0].src == "https://example.com/foo.png"

    def test_mixed_in_order(self) -> None:
        text = (
            "before ![one](https://a/x.png)\n\n"
            'middle <img alt="two" src="https://b/y.png">\n\n'
            "after ![three](https://c/z.png)"
        )
        refs = parse_image_refs(text)
        assert [r.src for r in refs] == [
            "https://a/x.png",
            "https://b/y.png",
            "https://c/z.png",
        ]

    def test_no_images(self) -> None:
        assert parse_image_refs("plain markdown text") == []


class TestRewriteRefs:
    def test_rewrite_markdown(self) -> None:
        text = "![alt](https://example.com/foo.png)"
        result = rewrite_refs(text, {"https://example.com/foo.png": "assets/foo.png"})
        assert result == "![alt](assets/foo.png)"

    def test_rewrite_html(self) -> None:
        text = '<img src="https://example.com/foo.png" alt="x">'
        result = rewrite_refs(text, {"https://example.com/foo.png": "assets/foo.png"})
        assert 'src="assets/foo.png"' in result
        assert 'alt="x"' in result

    def test_unmapped_passthrough(self) -> None:
        text = "![alt](https://other.com/x.png)"
        result = rewrite_refs(text, {"https://example.com/foo.png": "assets/foo.png"})
        assert result == text

    def test_no_mapping(self) -> None:
        text = "![alt](https://example.com/foo.png)"
        assert rewrite_refs(text, {}) == text


class TestImagesConstants:
    def test_default_mimes_include_common_types(self) -> None:
        for mime in ("image/png", "image/jpeg", "image/gif", "image/webp"):
            assert mime in DEFAULT_ALLOWED_MIMES

    def test_max_bytes_is_5mb(self) -> None:
        assert DEFAULT_MAX_BYTES == 5 * 1024 * 1024

    def test_mime_to_ext_complete(self) -> None:
        for mime in DEFAULT_ALLOWED_MIMES:
            assert mime in MIME_TO_EXT


class TestSafeFilenameCollisions:
    """Collision-safety: two URLs sharing a basename get distinct filenames."""

    def test_distinct_urls_distinct_filenames(self) -> None:
        a = safe_filename("https://example.com/foo.png", "png")
        b = safe_filename("https://other.com/foo.png", "png")
        assert a != b
        # Both end with -foo.png but the SHA prefix differs.
        assert a.endswith("-foo.png")
        assert b.endswith("-foo.png")
        assert a.split("-", 1)[0] != b.split("-", 1)[0]

    def test_same_url_same_filename(self) -> None:
        a = safe_filename("https://example.com/foo.png", "png")
        b = safe_filename("https://example.com/foo.png", "png")
        assert a == b

    def test_basename_sanitized(self) -> None:
        name = safe_filename("https://example.com/path/with spaces!@#.png", "png")
        # No raw spaces or unsafe characters in the output.
        assert " " not in name
        assert "!" not in name
        assert "@" not in name
        assert "#" not in name


class TestRewriteRefsAltTextPreserved:
    """Alt-text preservation: rewriting must not strip alt attributes."""

    def test_markdown_alt_kept(self) -> None:
        text = "![accessible alt text](https://example.com/foo.png)"
        rewritten = rewrite_refs(text, {"https://example.com/foo.png": "assets/foo.png"})
        assert "accessible alt text" in rewritten

    def test_html_alt_kept(self) -> None:
        text = '<img alt="hello world" src="https://example.com/foo.png">'
        rewritten = rewrite_refs(text, {"https://example.com/foo.png": "assets/foo.png"})
        assert 'alt="hello world"' in rewritten

    def test_multiple_images_rewritten(self) -> None:
        text = (
            '![a](https://x/1.png)\n\n<img src="https://x/2.png" alt="b">\n\n![c](https://x/3.png)'
        )
        mapping = {
            "https://x/1.png": "assets/1.png",
            "https://x/2.png": "assets/2.png",
            "https://x/3.png": "assets/3.png",
        }
        rewritten = rewrite_refs(text, mapping)
        assert "assets/1.png" in rewritten
        assert "assets/2.png" in rewritten
        assert "assets/3.png" in rewritten
        # No URLs from the original mapping should remain.
        for url in mapping:
            assert url not in rewritten


class TestParseRefsOrderingAndEdgeCases:
    def test_order_preserved(self) -> None:
        text = "![z](https://x/z.png)\n![a](https://x/a.png)"
        refs = parse_image_refs(text)
        assert [r.src for r in refs] == ["https://x/z.png", "https://x/a.png"]

    def test_no_image_in_link(self) -> None:
        # `[text](url)` (without leading !) is a link, not an image.
        refs = parse_image_refs("[link](https://example.com/foo.png)")
        assert refs == []

    def test_data_uri_passthrough(self) -> None:
        # We just record what's there; the fetch step would reject this.
        text = "![inline](data:image/png;base64,iVBORw0KG)"
        refs = parse_image_refs(text)
        assert len(refs) == 1
        assert refs[0].src.startswith("data:")


class TestSniffMime:
    @pytest.mark.parametrize(
        "magic,expected",
        [
            (PNG_MAGIC, "image/png"),
            (JPEG_MAGIC, "image/jpeg"),
            (b"GIF87a", "image/gif"),
            (b"GIF89a", "image/gif"),
            (WEBP_MAGIC, "image/webp"),
            (SVG_MAGIC, "image/svg+xml"),
            (b"<?xml version='1.0'?><svg></svg>", "image/svg+xml"),
        ],
    )
    def test_recognized(self, magic: bytes, expected: str) -> None:
        assert sniff_mime(magic) == expected

    def test_unknown(self) -> None:
        assert sniff_mime(b"random garbage data not an image") is None

    def test_empty(self) -> None:
        assert sniff_mime(b"") is None


class TestFetchImageMime:
    def test_png_round_trip(self, tmp_path: Path) -> None:
        url = "https://example.com/foo.png"
        body = PNG_MAGIC + b"\x00" * 100
        getter = make_getter(
            {
                url: FakeResponse(
                    headers={"Content-Type": "image/png", "Content-Length": str(len(body))},
                    body=body,
                )
            }
        )
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert result.ok
        assert result.path is not None
        assert result.path.exists()
        assert result.path.read_bytes() == body
        assert result.mime == "image/png"
        assert result.bytes_written == len(body)

    def test_disallowed_mime_skipped(self, tmp_path: Path) -> None:
        url = "https://example.com/page.html"
        getter = make_getter(
            {
                url: FakeResponse(
                    headers={"Content-Type": "text/html"},
                    body=b"<html></html>",
                )
            }
        )
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["DISALLOWED_MIME"]
        assert not list(tmp_path.iterdir())

    def test_mime_mismatch_caught(self, tmp_path: Path) -> None:
        url = "https://example.com/lying.png"
        getter = make_getter(
            {
                url: FakeResponse(
                    headers={"Content-Type": "image/png"},
                    body=JPEG_MAGIC + b"\x00" * 100,
                )
            }
        )
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["MIME_MISMATCH"]

    def test_header_only_unknown_bytes_uses_header(self, tmp_path: Path) -> None:
        # When the bytes don't match a known signature but the header is
        # allowed (e.g. WebP variant we don't sniff perfectly), accept the
        # header rather than rejecting silently.
        url = "https://example.com/odd.webp"
        body = b"\x00" * 256  # not RIFF...WEBP, so sniff returns None
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/webp"}, body=body)})
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert result.ok
        assert result.mime == "image/webp"


class TestFetchImageSize:
    def test_oversize_via_content_length(self, tmp_path: Path) -> None:
        url = "https://example.com/huge.png"
        getter = make_getter(
            {
                url: FakeResponse(
                    headers={"Content-Type": "image/png", "Content-Length": "10000000"},
                    body=PNG_MAGIC,
                )
            }
        )
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter, max_bytes=1024)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["OVERSIZE"]
        assert not list(tmp_path.iterdir())

    def test_oversize_via_streaming(self, tmp_path: Path) -> None:
        # Server lies about Content-Length (omits it) but the body is huge.
        url = "https://example.com/sneaky.png"
        body = PNG_MAGIC + b"\x00" * 5000
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/png"}, body=body)})
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter, max_bytes=1024)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["OVERSIZE"]
        assert not list(tmp_path.iterdir())

    def test_empty_body_skipped(self, tmp_path: Path) -> None:
        url = "https://example.com/empty.png"
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/png"}, body=b"")})
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["EMPTY_BODY"]


class TestFetchImageErrors:
    def test_non_http_scheme_rejected(self, tmp_path: Path) -> None:
        result = fetch_image("ftp://example.com/foo.png", dest_dir=tmp_path)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["NON_HTTP"]

    def test_fetch_exception_caught(self, tmp_path: Path) -> None:
        url = "https://example.com/dead.png"
        getter = make_getter({url: ConnectionError("boom")})
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["FETCH_ERROR"]

    def test_bad_status_skipped(self, tmp_path: Path) -> None:
        url = "https://example.com/404.png"
        getter = make_getter({url: FakeResponse(status_code=404)})
        result = fetch_image(url, dest_dir=tmp_path, http_get=getter)
        assert not result.ok
        assert result.skipped_reason == SKIP_REASONS["BAD_STATUS"]


class TestDownloadForSource:
    def test_round_trip(self, tmp_path: Path) -> None:
        url_a = "https://example.com/a.png"
        url_b = "https://example.com/b.jpg"
        body_a = PNG_MAGIC + b"\x00" * 200
        body_b = JPEG_MAGIC + b"\x00" * 200
        content = f'# Source\n\n![alpha]({url_a})\n\n<img src="{url_b}" alt="beta">\n\nEnd.'
        getter = make_getter(
            {
                url_a: FakeResponse(headers={"Content-Type": "image/png"}, body=body_a),
                url_b: FakeResponse(headers={"Content-Type": "image/jpeg"}, body=body_b),
            }
        )

        new_content, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/test-source",
            http_get=getter,
        )
        assert report.downloaded == 2
        assert report.skipped == 0
        for url in (url_a, url_b):
            assert url not in new_content
        # All references rewritten to local relative paths.
        assert "../assets/test-source/" in new_content
        # Alt text preserved.
        assert "![alpha]" in new_content
        assert 'alt="beta"' in new_content

    def test_local_and_data_refs_skipped(self, tmp_path: Path) -> None:
        content = "![local](./already.png)\n\n![data](data:image/png;base64,xx)"
        new_content, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/x",
            http_get=make_getter({}),
        )
        assert report.results == ()
        assert new_content == content

    def test_dedupes_repeated_urls(self, tmp_path: Path) -> None:
        url = "https://example.com/dup.png"
        body = PNG_MAGIC + b"\x00" * 50
        content = f"![one]({url})\n\n![two]({url})"
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/png"}, body=body)})
        new_content, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/dup",
            http_get=getter,
        )
        # Only one fetch performed.
        assert len(report.results) == 1
        assert report.downloaded == 1
        # Both references rewritten to the same local path.
        assert new_content.count("../assets/dup/") == 2

    def test_skip_keeps_original_ref(self, tmp_path: Path) -> None:
        url_good = "https://example.com/good.png"
        url_bad = "https://example.com/bad.html"
        body_good = PNG_MAGIC + b"\x00" * 50
        content = f"![g]({url_good})\n\n![b]({url_bad})"
        getter = make_getter(
            {
                url_good: FakeResponse(headers={"Content-Type": "image/png"}, body=body_good),
                url_bad: FakeResponse(headers={"Content-Type": "text/html"}, body=b"<html/>"),
            }
        )
        new_content, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/mixed",
            http_get=getter,
        )
        assert report.downloaded == 1
        assert report.skipped == 1
        # Good was rewritten; bad was left alone.
        assert "../assets/mixed/" in new_content
        assert url_bad in new_content
        assert url_good not in new_content

    def test_orphan_cleanup(self, tmp_path: Path) -> None:
        # Pre-seed an orphan that the source no longer references.
        orphan = tmp_path / "orphan.png"
        orphan.write_bytes(b"old data")

        url = "https://example.com/keep.png"
        body = PNG_MAGIC + b"\x00" * 50
        content = f"![keep]({url})"
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/png"}, body=body)})

        new_content, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/keep",
            http_get=getter,
            cleanup_orphans=True,
        )
        assert report.orphans_removed == 1
        assert not orphan.exists()
        # The newly downloaded asset survived.
        kept = list(tmp_path.iterdir())
        assert len(kept) == 1
        assert kept[0].name in new_content

    def test_orphan_cleanup_disabled(self, tmp_path: Path) -> None:
        orphan = tmp_path / "orphan.png"
        orphan.write_bytes(b"old data")
        url = "https://example.com/keep.png"
        body = PNG_MAGIC + b"\x00" * 50
        content = f"![keep]({url})"
        getter = make_getter({url: FakeResponse(headers={"Content-Type": "image/png"}, body=body)})
        _, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/keep",
            http_get=getter,
            cleanup_orphans=False,
        )
        assert report.orphans_removed == 0
        assert orphan.exists()


class TestSafeFilenameCollisionInPipeline:
    """The pipeline must put two distinct URLs sharing a basename in
    distinct files even when they land in the same per-source assets dir."""

    def test_distinct_urls_distinct_files(self, tmp_path: Path) -> None:
        body = PNG_MAGIC + b"\x00" * 32
        urls = ["https://a.com/foo.png", "https://b.com/foo.png"]
        content = "".join(f"![alt{i}]({u})\n" for i, u in enumerate(urls))
        getter = make_getter(
            {u: FakeResponse(headers={"Content-Type": "image/png"}, body=body) for u in urls}
        )
        _, report = download_for_source(
            source_content=content,
            assets_dir=tmp_path,
            relative_assets_path="../assets/x",
            http_get=getter,
        )
        assert report.downloaded == 2
        files = list(tmp_path.iterdir())
        assert len({f.name for f in files}) == 2
