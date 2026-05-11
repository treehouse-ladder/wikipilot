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
