"""Tests for ``wikipilot.cli`` subcommand surface."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from click.testing import CliRunner

from wikipilot.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def _copy_vault(tmp_path: Path) -> Path:
    dst = tmp_path / "wiki"
    shutil.copytree(FIXTURES / "sample_vault", dst)
    return dst


def _copy_topics(tmp_path: Path) -> Path:
    dst = tmp_path / "topics.yaml"
    shutil.copy(FIXTURES / "sample_topics.yaml", dst)
    return dst


class TestLintCommand:
    def test_clean_vault_succeeds(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        result = runner.invoke(main, ["lint", str(vault)])
        assert result.exit_code == 0, result.output

    def test_broken_link_fails(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        bad = vault / "concepts" / "transformer-attention.md"
        bad.write_text(bad.read_text(encoding="utf-8") + "\nsee [[ghost-page]]\n", encoding="utf-8")
        result = runner.invoke(main, ["lint", str(vault)])
        assert result.exit_code == 1
        assert "broken-wikilink" in result.output

    def test_branch_ownership_check(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        result = runner.invoke(
            main,
            [
                "lint",
                str(vault),
                "--branch",
                "claude/daily-2026-05-11/ai-agents",
                "--changed-path",
                "CLAUDE.md",
            ],
        )
        assert result.exit_code == 1
        assert "ownership-violation" in result.output


class TestInitVaultCommand:
    def test_creates_skeleton(self, runner: CliRunner, tmp_path: Path) -> None:
        target = tmp_path / "vault"
        result = runner.invoke(main, ["init-vault", str(target)])
        assert result.exit_code == 0
        assert (target / "index.md").exists()
        assert (target / "log.md").exists()
        for sub in (
            "topics",
            "concepts",
            "entities",
            "sources",
            "answers",
            "reports",
            "decks",
            "assets",
        ):
            assert (target / sub).is_dir()
            assert (target / sub / ".gitkeep").exists()

    def test_skip_existing(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        original_index = (vault / "index.md").read_text(encoding="utf-8")
        result = runner.invoke(main, ["init-vault", str(vault)])
        assert result.exit_code == 0
        assert (vault / "index.md").read_text(encoding="utf-8") == original_index

    def test_force_overwrites(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        original_index = (vault / "index.md").read_text(encoding="utf-8")
        result = runner.invoke(main, ["init-vault", str(vault), "--force"])
        assert result.exit_code == 0
        assert (vault / "index.md").read_text(encoding="utf-8") != original_index


class TestValidateTopicsCommand:
    def test_valid_topics(self, runner: CliRunner, tmp_path: Path) -> None:
        topics = _copy_topics(tmp_path)
        result = runner.invoke(main, ["validate-topics", str(topics)])
        assert result.exit_code == 0
        assert "ai-agents" in result.output
        assert "1 topic" in result.output

    def test_invalid_topics_exits_2(self, runner: CliRunner, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text("topics:\n  - id: foo\n", encoding="utf-8")
        result = runner.invoke(main, ["validate-topics", str(path)])
        assert result.exit_code == 2
        assert "ERROR" in result.output

    def test_empty_topics_ok(self, runner: CliRunner, tmp_path: Path) -> None:
        path = tmp_path / "topics.yaml"
        path.write_text("topics: []\n", encoding="utf-8")
        result = runner.invoke(main, ["validate-topics", str(path)])
        assert result.exit_code == 0
        assert "0 topics" in result.output


class TestFreshnessReportCommand:
    def test_lists_pages_in_age_order(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        result = runner.invoke(main, ["freshness-report", str(vault)])
        assert result.exit_code == 0
        # Stale page should appear before fresh ones.
        stale_pos = result.output.find("stale-concept.md")
        fresh_pos = result.output.find("transformer-attention.md")
        assert stale_pos != -1 and fresh_pos != -1
        assert stale_pos < fresh_pos


class TestDeckCommand:
    def test_generates_deck(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        topics = _copy_topics(tmp_path)
        result = runner.invoke(
            main,
            ["deck", "ai-agents", "--vault", str(vault), "--topics", str(topics)],
        )
        assert result.exit_code == 0, result.output
        deck_path = vault / "decks" / "ai-agents.md"
        assert deck_path.exists()
        text = deck_path.read_text(encoding="utf-8")
        assert "marp: true" in text

    def test_unknown_topic_errors(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        topics = _copy_topics(tmp_path)
        result = runner.invoke(
            main,
            ["deck", "does-not-exist", "--vault", str(vault), "--topics", str(topics)],
        )
        assert result.exit_code == 2
        assert "not found" in result.output


class TestIngestCommand:
    def test_creates_source_with_disabled_images(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        config = tmp_path / "wikipilot.toml"
        config.write_text(
            "[images]\nenabled = false\n",
            encoding="utf-8",
        )
        result = runner.invoke(
            main,
            [
                "ingest",
                "--url",
                "https://example.com/papers/cli-ingest",
                "--topic",
                "ai-agents",
                "--title",
                "CLI Ingest Test",
                "--excerpt",
                "A direct quote.",
                "--vault",
                str(vault),
                "--config",
                str(config),
            ],
        )
        assert result.exit_code == 0, result.output
        assert "Created source" in result.output
        # The source page is on disk under the slug printed.
        sources = list((vault / "sources").glob("cli-ingest-test-*.md"))
        assert len(sources) == 1
        text = sources[0].read_text(encoding="utf-8")
        assert "> A direct quote." in text

    def test_idempotent_repeat(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        config = tmp_path / "wikipilot.toml"
        config.write_text("[images]\nenabled = false\n", encoding="utf-8")
        args = [
            "ingest",
            "--url",
            "https://example.com/papers/attention.pdf",  # already in fixture
            "--topic",
            "ai-agents",
            "--title",
            "Different title",
            "--vault",
            str(vault),
            "--config",
            str(config),
        ]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert "Existing source returned" in result.output


class TestIndexWikiCommand:
    def test_no_qmd_exits_zero(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        # Whether or not qmd is installed on CI, the command should give a
        # graceful exit; we don't mock here because the CLI handles both paths
        # by exiting 0 when qmd is missing.
        result = runner.invoke(main, ["index-wiki", str(vault)])
        assert result.exit_code == 0


class TestResearchAndQueryCommands:
    def _write_creds(self, tmp_path: Path) -> Path:
        creds = tmp_path / "creds.toml"
        creds.write_text(
            '[research]\nfire_url = "https://x.example.com/fire"\ntoken = "y"\n'
            '[query]\nfire_url = "https://y.example.com/fire"\ntoken = "z"\n',
            encoding="utf-8",
        )
        return creds

    def test_research_success(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creds = self._write_creds(tmp_path)
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(creds))
        from wikipilot import api_client

        captured: dict[str, object] = {}

        def fake_post(url: str, *, json: dict, headers: dict, timeout: float):  # noqa: A002
            captured["url"] = url
            captured["json"] = json

            class R:
                status_code = 202
                text = "{}"
                headers: dict[str, str] = {}

                def json(self) -> dict[str, object]:
                    return {"run_id": "r-cli"}

            return R()

        monkeypatch.setattr(api_client, "_default_post", fake_post)
        result = runner.invoke(main, ["research", "--topic", "ai-agents"])
        assert result.exit_code == 0, result.output
        assert "run_id=r-cli" in result.output
        assert captured["json"] == {"topic_id": "ai-agents"}
        assert captured["url"] == "https://x.example.com/fire"

    def test_query_success(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creds = self._write_creds(tmp_path)
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(creds))
        from wikipilot import api_client

        def fake_post(url: str, *, json: dict, headers: dict, timeout: float):  # noqa: A002
            class R:
                status_code = 202
                text = "{}"
                headers: dict[str, str] = {}

                def json(self) -> dict[str, object]:
                    return {"run_id": "q-cli"}

            return R()

        monkeypatch.setattr(api_client, "_default_post", fake_post)
        result = runner.invoke(main, ["query", "what is x?"])
        assert result.exit_code == 0, result.output
        assert "run_id=q-cli" in result.output

    def test_query_failure_exits_1(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        creds = self._write_creds(tmp_path)
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(creds))
        from wikipilot import api_client

        def fake_post(url: str, *, json: dict, headers: dict, timeout: float):  # noqa: A002
            class R:
                status_code = 500
                text = ""
                headers: dict[str, str] = {}

                def json(self) -> dict[str, object]:
                    return {"error": "boom"}

            return R()

        monkeypatch.setattr(api_client, "_default_post", fake_post)
        result = runner.invoke(main, ["query", "what?"])
        assert result.exit_code == 1
        assert "status=500" in result.output
        assert "boom" in result.output

    def test_query_credentials_missing(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(tmp_path / "missing.toml"))
        result = runner.invoke(main, ["query", "what?"])
        assert result.exit_code == 2
        assert "credentials file not found" in result.output
