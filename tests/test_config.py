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
        """The committed `topics.yaml` parses cleanly. Phase 8 seeded two
        starter topics; future commits may add or remove. We only assert
        that whatever's in the file is schema-valid (the parser raises on
        malformed entries) and that every topic has a non-empty purpose."""
        repo_root = Path(__file__).resolve().parents[1]
        topics = load_topics(repo_root / "topics.yaml")
        for topic in topics:
            assert topic.id
            assert topic.display_name
            assert topic.purpose.strip()
            assert topic.frequency in {"daily", "weekly"}

    def test_repo_topics_have_purpose_md(self) -> None:
        """Every topic in `topics.yaml` must have a `wiki/topics/<id>/purpose.md`
        — `scripts/preflight.py` aborts cloud routine runs without it. Catching
        the violation in CI saves the user a failed Cloud Routine run."""
        repo_root = Path(__file__).resolve().parents[1]
        topics = load_topics(repo_root / "topics.yaml")
        missing = [
            t.id for t in topics if not (repo_root / "wiki/topics" / t.id / "purpose.md").exists()
        ]
        assert not missing, (
            f"topics in topics.yaml without wiki/topics/<id>/purpose.md: {missing} "
            "(see docs/runbook.md 'Adding a topic')"
        )

    def test_repo_topics_have_index_md(self) -> None:
        """Every topic also needs a `wiki/topics/<id>/index.md` (the synthesis page)."""
        repo_root = Path(__file__).resolve().parents[1]
        topics = load_topics(repo_root / "topics.yaml")
        missing = [
            t.id for t in topics if not (repo_root / "wiki/topics" / t.id / "index.md").exists()
        ]
        assert not missing, f"topics in topics.yaml without wiki/topics/<id>/index.md: {missing}"

    def test_repo_topics_carry_phase9_safety_cap(self) -> None:
        """Phase 9 regression guard: every seeded topic MUST set
        `max_sources_per_run: 20` (the uniform safety cap). Earlier phases
        used a tiered scheme (3, 5, 8); Phase 9 deliberately moved away from
        per-topic numeric quality levers in favor of cross-cutting relevance
        criteria + an inclusion-biased prompt. If you find yourself wanting
        to lower this number, edit `purpose.md` or `CLAUDE.md` instead.
        """
        repo_root = Path(__file__).resolve().parents[1]
        topics = load_topics(repo_root / "topics.yaml")
        wrong = [(t.id, t.max_sources_per_run) for t in topics if t.max_sources_per_run != 20]
        assert not wrong, (
            f"Phase 9 sets max_sources_per_run uniformly to 20 (safety cap, not a "
            f"quality lever). These topics drifted: {wrong}. See "
            "wiki/topics/<id>/purpose.md and CLAUDE.md 'Cross-cutting relevance criteria'."
        )

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
        # Phase 9 bumped daily_research thresholds from 40 / 1500 to 80 / 3000
        # to match the inclusion-biased researcher; see wikipilot.toml.
        repo_root = Path(__file__).resolve().parents[1]
        config = load_wikipilot_config(repo_root / "wikipilot.toml")
        assert config.daily_research.max_files_changed_per_topic == 80
        assert config.daily_research.max_total_diff_lines_per_topic == 3000


class TestConflictResolverConfig:
    """Coverage for the ``[automerge.conflict_resolver]`` trust-model block.

    PR Watcher v2 dropped ``ci_wait_timeout_sec`` and
    ``self_heal_max_attempts`` (GitHub's native auto-merge handles CI
    waits; self-heal is parked until observed-need data justifies it).
    The trust knobs survive because they're consulted by every gate code
    path that may queue ``gh pr merge --squash --auto``.
    """

    def test_defaults_when_block_omitted(self, tmp_path: Path) -> None:
        config = load_wikipilot_config(tmp_path / "missing.toml")
        assert config.conflict_resolver.trusted_associations == (
            "OWNER",
            "MEMBER",
            "COLLABORATOR",
        )
        assert config.conflict_resolver.trusted_authors == ()

    def test_defaults_when_keys_omitted_from_block(self, tmp_path: Path) -> None:
        """Setting only one trust key leaves the other at the documented
        default — important because the live wikipilot.toml may ship one
        without the other, and we don't want the gate to suddenly demote
        every PR just because the config wasn't fully updated."""
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            '[automerge.conflict_resolver]\ntrusted_authors = ["wikipilot-bot"]\n',
            encoding="utf-8",
        )
        config = load_wikipilot_config(path)
        assert config.conflict_resolver.trusted_associations == (
            "OWNER",
            "MEMBER",
            "COLLABORATOR",
        )
        assert config.conflict_resolver.trusted_authors == ("wikipilot-bot",)

    def test_explicit_override_parses(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[automerge.conflict_resolver]\n"
            'trusted_associations = ["OWNER"]\n'
            'trusted_authors = ["wikipilot-bot", "dependabot[bot]"]\n',
            encoding="utf-8",
        )
        config = load_wikipilot_config(path)
        assert config.conflict_resolver.trusted_associations == ("OWNER",)
        assert config.conflict_resolver.trusted_authors == (
            "wikipilot-bot",
            "dependabot[bot]",
        )

    def test_association_case_normalized_to_upper(self, tmp_path: Path) -> None:
        """``"member"`` lowercased in TOML should still validate; the GitHub
        REST API returns associations in upper-case, so we normalize on read."""
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            '[automerge.conflict_resolver]\ntrusted_associations = ["owner", "member"]\n',
            encoding="utf-8",
        )
        config = load_wikipilot_config(path)
        assert config.conflict_resolver.trusted_associations == ("OWNER", "MEMBER")

    def test_unknown_association_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            '[automerge.conflict_resolver]\ntrusted_associations = ["MEMBER", "BOGUS"]\n',
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="BOGUS"):
            load_wikipilot_config(path)

    def test_empty_trusted_associations_allowed(self, tmp_path: Path) -> None:
        """An empty list means "no association is trusted" — every PR is
        blocked from auto-merge unless its author is in trusted_authors.
        Niche but valid configuration; do not reject it as malformed."""
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[automerge.conflict_resolver]\ntrusted_associations = []\n",
            encoding="utf-8",
        )
        config = load_wikipilot_config(path)
        assert config.conflict_resolver.trusted_associations == ()

    def test_trusted_associations_must_be_list(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[automerge.conflict_resolver]\ntrusted_associations = 'MEMBER'\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="list of strings"):
            load_wikipilot_config(path)

    def test_trusted_authors_must_be_list_of_strings(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[automerge.conflict_resolver]\ntrusted_authors = [1, 2]\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="must be a string"):
            load_wikipilot_config(path)

    def test_unknown_key_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[automerge.conflict_resolver]\nbogus_field = 1\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="unknown keys"):
            load_wikipilot_config(path)

    def test_repo_config_ships_trust_block(self) -> None:
        """The committed wikipilot.toml ships the trust knobs with the
        documented defaults."""
        repo_root = Path(__file__).resolve().parents[1]
        config = load_wikipilot_config(repo_root / "wikipilot.toml")
        assert config.conflict_resolver.trusted_associations == (
            "OWNER",
            "MEMBER",
            "COLLABORATOR",
        )
        assert config.conflict_resolver.trusted_authors == ()


class TestFrontierModelsConfig:
    """``[frontier_models]`` — roster + benchmarks + cost_fields + glosses.

    The strict gloss validator exists to prevent acronym-soup columns from
    landing in the daily brief: every benchmark / cost field MUST have a
    matching one-line gloss in the config, or load fails. The tests below
    pin that contract.
    """

    def test_defaults_when_block_omitted(self, tmp_path: Path) -> None:
        config = load_wikipilot_config(tmp_path / "missing.toml")
        assert config.frontier_models.roster == ()
        assert config.frontier_models.benchmarks == ()
        assert config.frontier_models.cost_fields == ()
        assert config.frontier_models.benchmark_glosses == {}
        assert config.frontier_models.cost_glosses == {}

    def test_loads_full_block(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[frontier_models]\n"
            'roster = ["claude-opus-4.7", "gpt-5.5"]\n'
            'benchmarks = ["aa_intelligence_index"]\n'
            'cost_fields = ["input_cost_per_mtoken"]\n\n'
            "[frontier_models.benchmark_glosses]\n"
            'aa_intelligence_index = "Aggregate intelligence."\n\n'
            "[frontier_models.cost_glosses]\n"
            'input_cost_per_mtoken = "USD/Mtoken input."\n',
            encoding="utf-8",
        )
        config = load_wikipilot_config(path)
        assert config.frontier_models.roster == ("claude-opus-4.7", "gpt-5.5")
        assert config.frontier_models.benchmarks == ("aa_intelligence_index",)
        assert config.frontier_models.cost_fields == ("input_cost_per_mtoken",)
        assert (
            config.frontier_models.benchmark_glosses["aa_intelligence_index"]
            == "Aggregate intelligence."
        )
        assert (
            config.frontier_models.cost_glosses["input_cost_per_mtoken"]
            == "USD/Mtoken input."
        )

    def test_missing_benchmark_gloss_rejected(self, tmp_path: Path) -> None:
        """A benchmark column without a matching gloss fails config load —
        the whole point is to force the user to explain the column before
        it ships to the daily brief."""
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[frontier_models]\n"
            'benchmarks = ["aa_intelligence_index", "cybench"]\n\n'
            "[frontier_models.benchmark_glosses]\n"
            'aa_intelligence_index = "Aggregate intelligence."\n',
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="cybench"):
            load_wikipilot_config(path)

    def test_missing_cost_gloss_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[frontier_models]\n"
            'cost_fields = ["input_cost_per_mtoken"]\n\n'
            "[frontier_models.cost_glosses]\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="input_cost_per_mtoken"):
            load_wikipilot_config(path)

    def test_empty_gloss_value_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[frontier_models]\n"
            'benchmarks = ["aa_intelligence_index"]\n\n'
            "[frontier_models.benchmark_glosses]\n"
            'aa_intelligence_index = ""\n',
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="non-empty"):
            load_wikipilot_config(path)

    def test_unknown_key_rejected(self, tmp_path: Path) -> None:
        path = tmp_path / "wikipilot.toml"
        path.write_text(
            "[frontier_models]\nbogus = true\n",
            encoding="utf-8",
        )
        with pytest.raises(ConfigError, match="unknown keys"):
            load_wikipilot_config(path)

    def test_repo_config_loads_with_full_roster(self) -> None:
        """The committed wikipilot.toml ships a full roster + glosses for
        every benchmark and cost field."""
        repo_root = Path(__file__).resolve().parents[1]
        config = load_wikipilot_config(repo_root / "wikipilot.toml")
        fm = config.frontier_models
        assert "claude-opus-4.7" in fm.roster
        assert "aa_intelligence_index" in fm.benchmarks
        assert "input_cost_per_mtoken" in fm.cost_fields
        # Every column has a registered gloss (load would have failed otherwise).
        for col in fm.benchmarks:
            assert fm.benchmark_glosses[col]
        for col in fm.cost_fields:
            assert fm.cost_glosses[col]
