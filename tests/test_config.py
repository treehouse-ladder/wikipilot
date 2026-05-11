"""Tests for ``wikipilot.config`` loaders and validators."""

from __future__ import annotations

from pathlib import Path

import pytest

from wikipilot.config import (
    ConfigError,
    load_topics,
    load_wikipilot_config,
)


class TestLoadTopics:
    def test_loads_sample(self, sample_topics_path: Path) -> None:
        topics = load_topics(sample_topics_path)
        assert len(topics) == 1
        topic = topics[0]
        assert topic.id == "ai-agents"
        assert "agentic LLM" in topic.search_hints[0]
        assert "arxiv.org" in topic.allowlist_domains
        assert topic.frequency == "daily"
        assert topic.max_sources_per_run == 3

    def test_repo_topics_yaml_is_valid(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        topics = load_topics(repo_root / "topics.yaml")
        assert topics == []

    def test_missing_purpose_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            "topics:\n  - id: foo\n    display_name: Foo\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="missing required keys"):
            load_topics(path)

    def test_empty_purpose_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            'topics:\n  - id: foo\n    display_name: Foo\n    purpose: "  "\n',
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="purpose"):
            load_topics(path)

    def test_unknown_key_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            "topics:\n  - id: foo\n    display_name: Foo\n    purpose: P\n    bogus: 1\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="unknown keys"):
            load_topics(path)

    def test_bad_frequency_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            "topics:\n  - id: foo\n    display_name: Foo\n    purpose: P\n    frequency: hourly\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="frequency"):
            load_topics(path)

    def test_duplicate_ids_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            "topics:\n"
            "  - id: foo\n    display_name: Foo\n    purpose: P\n"
            "  - id: foo\n    display_name: Foo2\n    purpose: P2\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="duplicate"):
            load_topics(path)

    def test_negative_max_sources_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text(
            "topics:\n  - id: foo\n    display_name: Foo\n    purpose: P\n    max_sources_per_run: -1\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="positive integer"):
            load_topics(path)

    def test_top_level_must_be_mapping(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text("- not a mapping\n", encoding="utf-8")
        with pytest.raises(ConfigError):
            load_topics(path)

    def test_missing_topics_key(self, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text("other: thing\n", encoding="utf-8")
        with pytest.raises(ConfigError, match="missing 'topics:'"):
            load_topics(path)


class TestLoadWikipilotConfig:
    def test_loads_sample(self, sample_config_path: Path) -> None:
        config = load_wikipilot_config(sample_config_path)
        assert config.automerge_common.block_human_only_file_changes is True
        assert config.daily_research.max_files_changed_per_topic == 40
        assert config.wiki_query.max_files_changed == 8
        assert config.weekly_health.max_total_diff_lines == 2000
        assert config.images.enabled is True
        assert config.images.max_image_bytes == 5_242_880
        assert "image/png" in config.images.allowed_mimes
        assert config.branches.prefix == "claude"

    def test_missing_file_uses_defaults(self, tmp_path: Path) -> None:
        config = load_wikipilot_config(tmp_path / "missing.toml")
        assert config.automerge_common.require_lint_green is True
        assert config.images.enabled is True

    def test_repo_config_is_valid(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        config = load_wikipilot_config(repo_root / "wikipilot.toml")
        assert config.daily_research.max_files_changed_per_topic == 40
