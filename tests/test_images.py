"""Tests for the Phase 1 image-helper surface (full pipeline lands in Phase 5)."""

from __future__ import annotations

from wikipilot.images import (
    DEFAULT_ALLOWED_MIMES,
    DEFAULT_MAX_BYTES,
    MIME_TO_EXT,
    parse_image_refs,
    rewrite_refs,
    safe_filename,
)


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
