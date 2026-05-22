"""Tests for ``wikipilot.wiki`` primitives."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from wikipilot.wiki import (
    REQUIRED_FRONTMATTER,
    WIKI_DIRS,
    Page,
    Vault,
    WikiError,
    is_personal_scratch,
    parse_log_headings,
    parse_wikilinks,
    reset_vault,
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


# ---------------------------------------------------------------------------
# reset_vault — fork onboarding helper
# ---------------------------------------------------------------------------
#
# Hard rule: every test in this section uses ``tmp_path`` (pytest's per-test
# OS-tmp dir). The workspace's live vault is never targeted. The
# string-literal regression guard at the bottom of this file enforces that
# no future contributor adds a test pointing at the workspace-relative
# vault path (constructed at runtime in the guard itself so it does not
# appear as a literal anywhere else in this file).


def _make_populated_vault(root: Path) -> None:
    """Build a vault under ``root`` that mimics a forker's inherited content.

    Includes: real WIKI_DIRS skeleton, populated source/concept/entity/answer/
    report markdown, two topic folders (purpose.md + index.md), a per-source
    asset folder, ``.obsidian/`` config, ``_dashboard.md`` plus a personal
    ``_inbox.md``, and ``.gitkeep`` files in every subdirectory.
    """
    root.mkdir(parents=True, exist_ok=True)
    (root / "index.md").write_text("# Index\n\n## Topics\n- [[ai-agents]]\n", encoding="utf-8")
    (root / "log.md").write_text(
        "# Log\n\n## [2026-05-10] daily | ai-agents — 1 source\n\nFoo.\n",
        encoding="utf-8",
    )
    (root / "_dashboard.md").write_text(
        "# Dashboard\n\n```dataview\nFROM ...\n```\n", encoding="utf-8"
    )
    (root / "_inbox.md").write_text("# Inbox\n\n- something to read\n", encoding="utf-8")
    for sub in WIKI_DIRS:
        sub_dir = root / sub
        sub_dir.mkdir(parents=True, exist_ok=True)
        (sub_dir / ".gitkeep").write_text("", encoding="utf-8")
    (root / "sources" / "example-source-aabbccdd.md").write_text(
        "---\nkind: source\n---\nseed source content\n", encoding="utf-8"
    )
    (root / "sources" / "another-source-deadbeef.md").write_text(
        "---\nkind: source\n---\nseed source content\n", encoding="utf-8"
    )
    (root / "concepts" / "transformer-attention.md").write_text(
        "---\nkind: concept\n---\nconcept content\n", encoding="utf-8"
    )
    (root / "entities" / "anthropic.md").write_text(
        "---\nkind: entity\n---\nentity content\n", encoding="utf-8"
    )
    (root / "answers" / "2026-05-10-what-is-attention.md").write_text(
        "---\nkind: answer\n---\nanswer content\n", encoding="utf-8"
    )
    (root / "reports" / "2026-05-10.md").write_text(
        "---\nkind: report\n---\nreport content\n", encoding="utf-8"
    )
    (root / "comparisons" / "cost-comparison.md").write_text(
        "---\nkind: comparison\n---\ncomparison content\n", encoding="utf-8"
    )
    (root / "topics" / "ai-agents").mkdir(parents=True, exist_ok=True)
    (root / "topics" / "ai-agents" / "purpose.md").write_text(
        "# ai-agents charter\n", encoding="utf-8"
    )
    (root / "topics" / "ai-agents" / "index.md").write_text(
        "---\nkind: topic\n---\ntopic landing\n", encoding="utf-8"
    )
    (root / "topics" / "frontier-models").mkdir(parents=True, exist_ok=True)
    (root / "topics" / "frontier-models" / "purpose.md").write_text(
        "# frontier-models charter\n", encoding="utf-8"
    )
    (root / "topics" / "frontier-models" / "index.md").write_text(
        "---\nkind: topic\n---\ntopic landing\n", encoding="utf-8"
    )
    asset_dir = root / "assets" / "example-source-aabbccdd"
    asset_dir.mkdir(parents=True, exist_ok=True)
    (asset_dir / "00-image.png").write_bytes(b"\x89PNG\r\n\x1a\nfake-png-bytes")
    obsidian = root / ".obsidian"
    obsidian.mkdir(parents=True, exist_ok=True)
    (obsidian / "app.json").write_text("{}", encoding="utf-8")
    snippets = obsidian / "snippets"
    snippets.mkdir(parents=True, exist_ok=True)
    (snippets / "callouts.css").write_text("/* callouts */", encoding="utf-8")


class TestIsPersonalScratch:
    def test_underscore_md_matches(self) -> None:
        assert is_personal_scratch("_dashboard.md")
        assert is_personal_scratch("_inbox.md")

    def test_non_underscore_does_not_match(self) -> None:
        assert not is_personal_scratch("dashboard.md")
        assert not is_personal_scratch("index.md")

    def test_underscore_non_md_does_not_match(self) -> None:
        # Defensive: the convention is _*.md specifically.
        assert not is_personal_scratch("_local.txt")


class TestResetVaultDryRun:
    def test_dry_run_does_not_mutate(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)
        before = sorted(p.relative_to(vault).as_posix() for p in vault.rglob("*") if p.is_file())

        summary = reset_vault(vault, dry_run=True)

        assert summary.dry_run is True
        assert summary.mutated is False
        assert summary.total_deletions > 0
        # Files on disk are unchanged.
        after = sorted(p.relative_to(vault).as_posix() for p in vault.rglob("*") if p.is_file())
        assert before == after

    def test_dry_run_summary_lists_seeded_content(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        summary = reset_vault(vault, dry_run=True)

        deleted_names = {p.name for p in summary.files_to_delete}
        # Maintainer source files queued for deletion.
        assert "example-source-aabbccdd.md" in deleted_names
        assert "transformer-attention.md" in deleted_names
        # Topic folders queued as directory deletions.
        deleted_dir_names = {p.name for p in summary.dirs_to_delete}
        assert "ai-agents" in deleted_dir_names
        assert "frontier-models" in deleted_dir_names
        # Per-source asset folder queued.
        assert "example-source-aabbccdd" in deleted_dir_names
        # index.md and log.md scheduled for reset (not deletion).
        reset_names = {p.name for p in summary.files_to_reset}
        assert reset_names == {"index.md", "log.md"}
        # Personal scratch + obsidian config preserved.
        preserved_files = {p.name for p in summary.files_preserved}
        assert "_dashboard.md" in preserved_files
        assert "_inbox.md" in preserved_files
        assert any(p.name == ".obsidian" for p in summary.dirs_preserved)


class TestResetVaultMutation:
    def test_wipes_seed_content(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        summary = reset_vault(vault)

        assert summary.mutated is True
        assert summary.dry_run is False
        # Maintainer content is gone.
        assert not (vault / "sources" / "example-source-aabbccdd.md").exists()
        assert not (vault / "concepts" / "transformer-attention.md").exists()
        assert not (vault / "entities" / "anthropic.md").exists()
        assert not (vault / "answers" / "2026-05-10-what-is-attention.md").exists()
        assert not (vault / "reports" / "2026-05-10.md").exists()
        assert not (vault / "comparisons" / "cost-comparison.md").exists()
        # Topic folders are gone.
        assert not (vault / "topics" / "ai-agents").exists()
        assert not (vault / "topics" / "frontier-models").exists()
        # Per-source asset folder is gone.
        assert not (vault / "assets" / "example-source-aabbccdd").exists()

    def test_preserves_obsidian_config(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        reset_vault(vault)

        assert (vault / ".obsidian" / "app.json").exists()
        assert (vault / ".obsidian" / "snippets" / "callouts.css").exists()

    def test_preserves_personal_scratch(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)
        # Add a deeper personal scratch file inside concepts/ to confirm the
        # _*.md rule applies wiki-wide, not just at the root.
        (vault / "concepts" / "_local-notes.md").write_text("personal", encoding="utf-8")

        reset_vault(vault)

        assert (vault / "_dashboard.md").exists()
        assert (vault / "_dashboard.md").read_text(encoding="utf-8").startswith("# Dashboard")
        assert (vault / "_inbox.md").exists()
        assert (vault / "concepts" / "_local-notes.md").exists()

    def test_preserves_gitkeeps(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        reset_vault(vault)

        for sub in WIKI_DIRS:
            assert (vault / sub).is_dir()
            assert (vault / sub / ".gitkeep").exists(), f"missing .gitkeep in {sub}/"

    def test_recreates_missing_subdirs(self, tmp_path: Path) -> None:
        # If a forker has accidentally deleted one of the WIKI_DIRS, reset
        # restores the skeleton. (Matches init-vault's post-condition.)
        vault = tmp_path / "vault"
        _make_populated_vault(vault)
        import shutil as _shutil

        _shutil.rmtree(vault / "comparisons")

        reset_vault(vault)

        assert (vault / "comparisons").is_dir()
        assert (vault / "comparisons" / ".gitkeep").exists()

    def test_idempotent_on_empty_vault(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        first = reset_vault(vault)
        assert first.total_deletions > 0

        # Second run should be a no-op (no deletions, no resets).
        second = reset_vault(vault)
        assert second.total_deletions == 0
        # index.md and log.md still queued for "reset" because they exist
        # and are schema files, but the on-disk state is unchanged after
        # the second run.
        assert (vault / "index.md").exists()
        assert (vault / "log.md").exists()


class TestResetVaultKeepTopics:
    def test_keep_topics_preserves_topic_tree(self, tmp_path: Path) -> None:
        vault = tmp_path / "vault"
        _make_populated_vault(vault)

        reset_vault(vault, keep_topics=True)

        # topics/ tree survives in full.
        assert (vault / "topics" / "ai-agents" / "purpose.md").exists()
        assert (vault / "topics" / "ai-agents" / "index.md").exists()
        assert (vault / "topics" / "frontier-models" / "purpose.md").exists()
        # But sources, concepts, entities are still wiped.
        assert not (vault / "sources" / "example-source-aabbccdd.md").exists()
        assert not (vault / "concepts" / "transformer-attention.md").exists()


class TestResetVaultGuards:
    def test_missing_path_raises(self, tmp_path: Path) -> None:
        with pytest.raises(WikiError, match="does not exist"):
            reset_vault(tmp_path / "nope")

    def test_file_path_raises(self, tmp_path: Path) -> None:
        target = tmp_path / "not-a-dir.txt"
        target.write_text("hello", encoding="utf-8")
        with pytest.raises(WikiError, match="not a directory"):
            reset_vault(target)

    def test_unrelated_directory_refused(self, tmp_path: Path) -> None:
        # Directory exists but doesn't look like a Wikipilot vault — no
        # index.md, no canonical subdirs. The helper must refuse rather than
        # delete unknown content.
        unrelated = tmp_path / "Documents"
        unrelated.mkdir()
        (unrelated / "personal-notes.md").write_text("important", encoding="utf-8")
        (unrelated / "photos").mkdir()
        (unrelated / "photos" / "vacation.jpg").write_bytes(b"jpg")

        with pytest.raises(WikiError, match="does not look like a Wikipilot vault"):
            reset_vault(unrelated)

        # Untouched.
        assert (unrelated / "personal-notes.md").exists()
        assert (unrelated / "photos" / "vacation.jpg").exists()


def test_no_test_targets_workspace_vault() -> None:
    """Regression guard: forbid workspace-relative vault paths in test code.

    The reset_vault test suite is destructive. To make absolutely sure no
    future contributor adds a test that points at the workspace's live
    vault by accident, we grep this file's own source for the most common
    accidental literals: a workspace-relative ``Path()`` of the vault
    directory and a positional ``Vault.at()`` of the same.

    The forbidden tokens are constructed at runtime so they do not appear
    as literals anywhere else in this file (which would make the guard
    trip on its own assertion message).
    """
    source_path = Path(__file__)
    text = source_path.read_text(encoding="utf-8")
    vault_dirname = "wiki"
    forbidden_tokens = [
        f'Path("{vault_dirname}")',
        f"Path('{vault_dirname}')",
        f'Vault.at("{vault_dirname}")',
        f"Vault.at('{vault_dirname}')",
        f'reset_vault("{vault_dirname}")',
        f"reset_vault('{vault_dirname}')",
    ]
    for token in forbidden_tokens:
        assert token not in text, (
            f"tests/test_wiki.py contains the forbidden literal {token!r} — "
            "this file must only target tmp_path-rooted vaults to keep the "
            "workspace's live vault safe."
        )
