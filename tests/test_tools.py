"""Tests for the tool-profile layer: enumerator, lint rule, config, CLI dump."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

import pytest
from click.testing import CliRunner

from wikipilot.cli import main
from wikipilot.config import ConfigError, ToolProfilesConfig, load_wikipilot_config
from wikipilot.lint import LintContext, Linter, check_tool_profile
from wikipilot.tools import (
    PROFILE_FIELDS,
    SCHEMA_VERSION,
    build_registry,
    iter_tool_entities,
    render_registry_markdown,
    strip_wikilink,
    tool_record,
    tools_for_topic,
)
from wikipilot.wiki import Page, Vault

SOURCE_SLUG = "example-paper-aabbccdd"  # exists in the sample vault


def write_tool_entity(vault: Vault, slug: str = "meshy", **overrides: Any) -> Path:
    """Write a lint-clean ``profile: tool`` entity into ``vault`` and return its path."""
    metadata: dict[str, Any] = {
        "title": slug.title(),
        "kind": "entity",
        "aliases": [slug.upper()],
        "sources": [f"[[{SOURCE_SLUG}]]"],
        "last_updated": date(2026, 5, 10),
        "last_verified": date(2026, 5, 10),
        "freshness_window_days": 30,
        "profile": "tool",
        "modality": "3d",
        "tasks": ["image-to-3d"],
        "vendor": "Meshy",
        "model_ids": ["meshy-7", "fal:fal-ai/meshy/v7"],
        "access": ["api", "fal"],
        "open_weights_license": "unknown",
        "hardware_floor": "unknown",
        "pricing": "unknown",
        "pricing_source": None,
        "commercial_use": "unknown",
        "commercial_use_source": None,
        "status": "active",
        "status_source": f"[[{SOURCE_SLUG}]]",
        "last_release": date(2026, 5, 1),
        "arena_rank": ["AA Image-to-3D: #1 (2026-05-01)"],
        "arena_rank_source": [f"[[{SOURCE_SLUG}]]"],
    }
    metadata.update(overrides)
    for key, value in list(metadata.items()):
        if value is ...:  # sentinel: delete the key
            del metadata[key]
    body = (
        f"# {slug}\n\n## Summary\n\nA tool [[{SOURCE_SLUG}]].\n\n> quote\n\n"
        "## See also\n\n- [[ai-agents]]\n\n"
        "_no contradictions or gaps known yet (last reviewed: 2026-05-10)_\n"
    )
    path = vault.dir_for("entities") / f"{slug}.md"
    Page.from_dict(path, metadata, body).write()
    # Link it from the index so the orphan rule stays quiet.
    index = vault.index_path
    index.write_text(index.read_text(encoding="utf-8") + f"\n- [[{slug}]]\n", encoding="utf-8")
    return path


def _ctx(vault: Vault) -> LintContext:
    return LintContext.collect(vault, today=date(2026, 5, 10))


class TestEnumerator:
    def test_empty_vault_has_no_tools(self, sample_vault: Vault) -> None:
        assert list(iter_tool_entities(sample_vault)) == []

    def test_finds_tool_and_skips_plain_entities(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault)
        tools = list(iter_tool_entities(sample_vault))
        assert [t.slug for t in tools] == ["meshy"]  # `anthropic` has no profile

    def test_skips_personal_scratch(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault, slug="_scratch-tool")
        assert list(iter_tool_entities(sample_vault)) == []

    def test_tools_for_topic_uses_modality_topics(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault, slug="meshy", modality="3d")
        write_tool_entity(sample_vault, slug="suno", modality="music")
        cfg = ToolProfilesConfig()
        assert [t.slug for t in tools_for_topic(sample_vault, cfg, "ai-in-game-dev")] == ["meshy"]
        assert [t.slug for t in tools_for_topic(sample_vault, cfg, "generative-media-models")] == [
            "suno"
        ]
        assert tools_for_topic(sample_vault, cfg, "game-music") == []

    def test_record_shape_and_source_url(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault)
        tool = next(iter(iter_tool_entities(sample_vault)))
        record = tool_record(sample_vault, tool)
        for key in PROFILE_FIELDS:
            assert key in record
        assert record["status_source"] == SOURCE_SLUG  # wikilink stripped
        src_url = Page.read(sample_vault.dir_for("sources") / f"{SOURCE_SLUG}.md").metadata["url"]
        assert record["status_source_url"] == src_url
        assert record["pricing_source"] is None and record["pricing_source_url"] is None
        assert record["arena_rank_source"] == [SOURCE_SLUG]
        assert record["arena_rank_source_url"] == [src_url]
        assert record["last_release"] == "2026-05-01"
        assert record["last_verified"] == "2026-05-10"
        assert record["path"].endswith("entities/meshy.md")

    def test_registry_is_versioned(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault)
        registry = build_registry(sample_vault, head_rev="abc123")
        assert registry["schema_version"] == SCHEMA_VERSION == 1
        assert registry["head_rev"] == "abc123"
        assert len(registry["tools"]) == 1
        md = render_registry_markdown(registry)
        assert "| [[meshy]] | 3d | Meshy | api, fal | active |" in md

    def test_strip_wikilink(self) -> None:
        assert strip_wikilink("[[foo-bar]]") == "foo-bar"
        assert strip_wikilink("[[foo-bar|Foo]]") == "foo-bar"
        assert strip_wikilink("foo-bar") == "foo-bar"
        assert strip_wikilink(None) is None


class TestToolProfileLint:
    def test_clean_profile_passes(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault)
        issues = check_tool_profile(_ctx(sample_vault))
        assert issues == [], "\n".join(i.render() for i in issues)
        # And the whole linter has no errors on it.
        all_issues = Linter().run(_ctx(sample_vault))
        errors = [i for i in all_issues if i.severity == "error" and i.path.name == "meshy.md"]
        assert errors == [], "\n".join(i.render() for i in errors)

    def test_non_tool_entity_untouched(self, sample_vault: Vault) -> None:
        assert check_tool_profile(_ctx(sample_vault)) == []

    def test_missing_field_is_error(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault, pricing=...)
        issues = check_tool_profile(_ctx(sample_vault))
        assert any("missing field" in i.message and "pricing" in i.message for i in issues)
        assert all(i.severity == "error" and i.code == "tool-profile" for i in issues)

    @pytest.mark.parametrize(
        ("overrides", "needle"),
        [
            ({"modality": "hologram"}, "modality"),
            ({"status": "retired"}, "status"),
            ({"access": "api"}, "access must be a list"),
            ({"access": []}, "non-empty"),
            ({"access": ["api", "telepathy"]}, "access value(s)"),
            ({"model_ids": ["hf:org/model"]}, "unknown prefix"),
            ({"arena_rank_source": []}, "same length"),
            ({"status_source": "not-a-wikilink"}, "status_source"),
            ({"last_release": "soon"}, "last_release"),
            ({"vendor": ""}, "vendor"),
            ({"tasks": []}, "tasks"),
        ],
    )
    def test_bad_values_flagged(
        self, sample_vault: Vault, overrides: dict[str, Any], needle: str
    ) -> None:
        write_tool_entity(sample_vault, **overrides)
        issues = check_tool_profile(_ctx(sample_vault))
        assert any(needle in i.message for i in issues), "\n".join(i.render() for i in issues)

    def test_unknown_literal_accepted_everywhere(self, sample_vault: Vault) -> None:
        write_tool_entity(
            sample_vault,
            vendor="unknown",
            last_release="unknown",
            arena_rank=[],
            arena_rank_source=[],
            status_source=None,
        )
        assert check_tool_profile(_ctx(sample_vault)) == []

    def test_uses_config_enums(self, sample_vault: Vault, tmp_path: Path) -> None:
        write_tool_entity(sample_vault, modality="hologram")
        cfg_path = tmp_path / "wikipilot.toml"
        cfg_path.write_text(
            "[tool_profiles]\nmodalities = ['hologram']\n"
            "[tool_profiles.modality_topics]\nhologram = 'ai-in-game-dev'\n",
            encoding="utf-8",
        )
        config = load_wikipilot_config(cfg_path)
        ctx = LintContext.collect(sample_vault, today=date(2026, 5, 10), config=config)
        assert check_tool_profile(ctx) == []


class TestToolProfilesConfig:
    def test_defaults_when_block_omitted(self, tmp_path: Path) -> None:
        cfg = load_wikipilot_config(tmp_path / "missing.toml")
        tp = cfg.tool_profiles
        assert "3d" in tp.modalities
        assert tp.tracked_fields == ("status", "pricing", "commercial_use", "arena_rank")
        assert tp.modalities_for_topic("ai-in-game-dev") == ("3d", "rig", "motion")

    def test_repo_config_maps_every_modality(self) -> None:
        cfg = load_wikipilot_config(Path(__file__).parent.parent / "wikipilot.toml")
        tp = cfg.tool_profiles
        assert set(tp.modality_topics) == set(tp.modalities)
        assert set(tp.modality_topics.values()) == {"generative-media-models", "ai-in-game-dev"}

    def test_unmapped_modality_rejected(self, tmp_path: Path) -> None:
        p = tmp_path / "wikipilot.toml"
        p.write_text(
            "[tool_profiles]\nmodalities = ['image', 'video']\n"
            "[tool_profiles.modality_topics]\nimage = 'generative-media-models'\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="missing entries for \\['video'\\]"):
            load_wikipilot_config(p)

    def test_unknown_modality_in_map_rejected(self, tmp_path: Path) -> None:
        p = tmp_path / "wikipilot.toml"
        p.write_text(
            "[tool_profiles]\nmodalities = ['image']\n"
            "[tool_profiles.modality_topics]\nimage = 'a'\nvideo = 'b'\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="unknown modalities"):
            load_wikipilot_config(p)

    def test_unknown_key_rejected(self, tmp_path: Path) -> None:
        p = tmp_path / "wikipilot.toml"
        p.write_text("[tool_profiles]\nroster = ['meshy']\n", encoding="utf-8")
        with pytest.raises(ConfigError, match="unknown keys"):
            load_wikipilot_config(p)


class TestToolsCli:
    def test_json_dump(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault)
        result = CliRunner().invoke(
            main, ["tools", "--format", "json", "--vault", str(sample_vault.root)]
        )
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["schema_version"] == 1
        assert [t["slug"] for t in payload["tools"]] == ["meshy"]
        assert payload["tools"][0]["access"] == ["api", "fal"]

    def test_topic_filter(self, sample_vault: Vault) -> None:
        write_tool_entity(sample_vault, slug="meshy", modality="3d")
        write_tool_entity(sample_vault, slug="suno", modality="music")
        result = CliRunner().invoke(
            main,
            [
                "tools",
                "--topic",
                "generative-media-models",
                "--format",
                "json",
                "--vault",
                str(sample_vault.root),
            ],
        )
        assert result.exit_code == 0, result.output
        assert [t["slug"] for t in json.loads(result.output)["tools"]] == ["suno"]

    def test_topic_and_modality_exclusive(self, sample_vault: Vault) -> None:
        result = CliRunner().invoke(
            main,
            ["tools", "--topic", "x", "--modality", "3d", "--vault", str(sample_vault.root)],
        )
        assert result.exit_code == 2
