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

    def test_seeds_obsidian_graph_from_template(self, runner: CliRunner, tmp_path: Path) -> None:
        """``init-vault`` seeds ``.obsidian/graph.json`` from the tracked
        ``graph.template.json`` when the target file is missing — the
        forker/fresh-clone path that restores the default color groups
        without overwriting any existing user customizations."""
        target = tmp_path / "vault"
        target.mkdir()
        obsidian = target / ".obsidian"
        obsidian.mkdir()
        (obsidian / "graph.template.json").write_text(
            '{"colorGroups": ["template-marker"]}', encoding="utf-8"
        )
        # No graph.json yet (the gitignored-but-missing-on-fresh-clone state).
        assert not (obsidian / "graph.json").exists()

        result = runner.invoke(main, ["init-vault", str(target)])

        assert result.exit_code == 0, result.output
        assert "Seeded Obsidian default: .obsidian/graph.json" in result.output.replace("\\", "/")
        assert (obsidian / "graph.json").read_text(encoding="utf-8") == (
            '{"colorGroups": ["template-marker"]}'
        )

    def test_does_not_overwrite_existing_graph_json(
        self, runner: CliRunner, tmp_path: Path
    ) -> None:
        """A re-run of ``init-vault`` on a vault where the user already
        customized ``graph.json`` must leave it untouched. This is the
        contract that lets users run ``init-vault`` as an idempotent
        ``ensure-defaults`` step without losing local tweaks."""
        target = tmp_path / "vault"
        target.mkdir()
        obsidian = target / ".obsidian"
        obsidian.mkdir()
        (obsidian / "graph.template.json").write_text(
            '{"colorGroups": ["template-marker"]}', encoding="utf-8"
        )
        (obsidian / "graph.json").write_text(
            '{"colorGroups": ["user-customized"]}', encoding="utf-8"
        )

        result = runner.invoke(main, ["init-vault", str(target)])

        assert result.exit_code == 0, result.output
        assert "Seeded Obsidian default" not in result.output
        assert (obsidian / "graph.json").read_text(encoding="utf-8") == (
            '{"colorGroups": ["user-customized"]}'
        )


class TestResetVaultCommand:
    """End-to-end coverage of the `reset-vault` CLI command.

    Hard rule: every test in this class targets a tmp_path-rooted vault.
    See the regression guard at the bottom of this file.
    """

    def _topics_with_seeded_topic(self, tmp_path: Path) -> Path:
        """Write a topics.yaml that has the documented header + one seeded topic."""
        path = tmp_path / "topics.yaml"
        path.write_text(
            "# topics.yaml — header comment that must survive reset.\n"
            "#\n"
            "# Schema docs go here.\n"
            "\n"
            "topics:\n"
            "  - id: seeded-topic\n"
            '    display_name: "Seeded"\n'
            "    purpose: |\n"
            "      Seeded purpose.\n"
            '    search_hints: ["x"]\n'
            "    frequency: daily\n"
            "    max_sources_per_run: 20\n"
            "    freshness_window_days: 30\n",
            encoding="utf-8",
        )
        return path

    def test_yes_flag_wipes_and_preserves(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        # Add a personal scratch file deep in the vault to confirm preservation.
        (vault / "_dashboard.md").write_text("# Dashboard\n", encoding="utf-8")
        topics = self._topics_with_seeded_topic(tmp_path)

        result = runner.invoke(
            main,
            ["reset-vault", str(vault), "--yes", "--topics-file", str(topics)],
        )

        assert result.exit_code == 0, result.output
        # Maintainer content gone.
        assert not (vault / "concepts" / "transformer-attention.md").exists()
        assert not (vault / "sources" / "example-paper-aabbccdd.md").exists()
        assert not (vault / "topics" / "ai-agents").exists()
        # Personal scratch survives.
        assert (vault / "_dashboard.md").exists()
        # Skeleton restored.
        assert (vault / "index.md").exists()
        assert (vault / "log.md").exists()
        for sub in ("topics", "concepts", "entities", "sources", "answers", "reports"):
            assert (vault / sub / ".gitkeep").exists()
        # topics.yaml reset, header preserved.
        new_topics = topics.read_text(encoding="utf-8")
        assert "header comment that must survive reset" in new_topics
        assert "topics: []" in new_topics
        assert "seeded-topic" not in new_topics

    def test_typed_basename_confirmation_accepts(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        # Vault basename is "wiki" (per _copy_vault).
        result = runner.invoke(
            main,
            ["reset-vault", str(vault), "--topics-file", str(topics)],
            input=f"{vault.name}\n",
        )
        assert result.exit_code == 0, result.output
        assert "Reset complete" in result.output
        assert not (vault / "concepts" / "transformer-attention.md").exists()

    def test_typed_basename_confirmation_rejects_wrong_input(
        self, runner: CliRunner, tmp_path: Path
    ) -> None:
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        result = runner.invoke(
            main,
            ["reset-vault", str(vault), "--topics-file", str(topics)],
            input="yes\n",  # wrong: should be the basename, not "yes"
        )
        assert result.exit_code == 1
        assert "Aborted" in result.output
        # Vault and topics untouched.
        assert (vault / "concepts" / "transformer-attention.md").exists()
        assert "seeded-topic" in topics.read_text(encoding="utf-8")

    def test_aborts_when_no_tty_and_no_yes(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        result = runner.invoke(
            main,
            ["reset-vault", str(vault), "--topics-file", str(topics)],
            input="",  # empty stdin -> EOF
        )
        assert result.exit_code == 1
        assert (vault / "concepts" / "transformer-attention.md").exists()

    def test_keep_topics_preserves_topics_yaml_and_topic_dirs(
        self, runner: CliRunner, tmp_path: Path
    ) -> None:
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        result = runner.invoke(
            main,
            [
                "reset-vault",
                str(vault),
                "--yes",
                "--keep-topics",
                "--topics-file",
                str(topics),
            ],
        )
        assert result.exit_code == 0, result.output
        # Topic folders preserved.
        assert (vault / "topics" / "ai-agents" / "purpose.md").exists()
        # topics.yaml unchanged (still has the seeded topic).
        assert "seeded-topic" in topics.read_text(encoding="utf-8")
        # Other content still wiped.
        assert not (vault / "sources" / "example-paper-aabbccdd.md").exists()

    def test_unrelated_directory_refused(self, runner: CliRunner, tmp_path: Path) -> None:
        unrelated = tmp_path / "Documents"
        unrelated.mkdir()
        (unrelated / "personal.md").write_text("notes", encoding="utf-8")
        result = runner.invoke(main, ["reset-vault", str(unrelated), "--yes"])
        assert result.exit_code == 2
        assert "does not look like a Wikipilot vault" in result.output
        assert (unrelated / "personal.md").exists()

    def test_idempotent(self, runner: CliRunner, tmp_path: Path) -> None:
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        first = runner.invoke(
            main,
            ["reset-vault", str(vault), "--yes", "--topics-file", str(topics)],
        )
        assert first.exit_code == 0
        second = runner.invoke(
            main,
            ["reset-vault", str(vault), "--yes", "--topics-file", str(topics)],
        )
        assert second.exit_code == 0
        assert "already at the empty-skeleton state" in second.output

    def test_seeds_obsidian_graph_after_reset(self, runner: CliRunner, tmp_path: Path) -> None:
        """``reset-vault`` seeds ``.obsidian/graph.json`` from the tracked
        template after wiping content — so a fresh fork ends up with the
        maintainer's default color groups even though ``graph.json`` is
        gitignored. Pre-existing customized ``graph.json`` files are
        preserved unchanged."""
        vault = _copy_vault(tmp_path)
        topics = self._topics_with_seeded_topic(tmp_path)
        obsidian = vault / ".obsidian"
        obsidian.mkdir(parents=True, exist_ok=True)
        (obsidian / "graph.template.json").write_text(
            '{"colorGroups": ["template-marker"]}', encoding="utf-8"
        )

        result = runner.invoke(
            main,
            ["reset-vault", str(vault), "--yes", "--topics-file", str(topics)],
        )

        assert result.exit_code == 0, result.output
        assert "Seeded Obsidian default: .obsidian/graph.json" in result.output.replace("\\", "/")
        assert (obsidian / "graph.json").read_text(encoding="utf-8") == (
            '{"colorGroups": ["template-marker"]}'
        )

    def test_topics_file_defaults_to_vault_sibling_not_cwd(
        self, runner: CliRunner, tmp_path: Path
    ) -> None:
        """Regression: --topics-file must default to the vault's sibling,
        not a CWD-relative path. A smoke test against /tmp/foo must NEVER
        reach across to the workspace's topics.yaml."""
        vault = _copy_vault(tmp_path)
        sibling_topics = tmp_path / "topics.yaml"
        sibling_topics.write_text(
            "# header\n\ntopics:\n  - id: sibling-topic\n"
            "    display_name: 'X'\n    purpose: 'x'\n"
            "    search_hints: ['x']\n    frequency: daily\n"
            "    max_sources_per_run: 20\n    freshness_window_days: 30\n",
            encoding="utf-8",
        )
        # Create a decoy "topics.yaml" in a separate CWD that should NOT be touched.
        decoy_cwd = tmp_path / "decoy"
        decoy_cwd.mkdir()
        decoy = decoy_cwd / "topics.yaml"
        decoy.write_text(
            "# DECOY — must not be modified\ntopics:\n  - id: decoy\n",
            encoding="utf-8",
        )

        with runner.isolated_filesystem(temp_dir=decoy_cwd):
            # Symlink the decoy into the isolated CWD, then run from there.
            # We can't use isolated_filesystem's auto-CWD because we want
            # to assert against the persistent decoy file.

            try:
                (Path() / "topics.yaml").symlink_to(decoy)
            except (OSError, NotImplementedError):
                # Symlinks may fail on Windows without elevation; fall back
                # to a copy and assert on the copy + the persistent decoy.
                (Path() / "topics.yaml").write_text(
                    decoy.read_text(encoding="utf-8"), encoding="utf-8"
                )

            result = runner.invoke(main, ["reset-vault", str(vault), "--yes"])

            assert result.exit_code == 0, result.output
            # The CLI prints the absolute resolved topics target so the
            # safety scaffolding is auditable from the output.
            assert "Topics file target:" in result.output
            assert str(sibling_topics.resolve()) in result.output
            # Sibling was reset.
            assert "topics: []" in sibling_topics.read_text(encoding="utf-8")
            # The persistent decoy outside the isolated CWD is untouched.
            assert "DECOY" in decoy.read_text(encoding="utf-8")
            # The CWD-local copy/symlink is also untouched (because the CLI
            # derived the target from the vault's parent, not from CWD).
            assert "DECOY" in (Path() / "topics.yaml").read_text(encoding="utf-8")


def test_no_test_targets_workspace_vault_in_test_cli() -> None:
    """Regression guard for tests/test_cli.py — see test_wiki.py for rationale.

    Forbidden tokens are constructed at runtime so they never appear as
    literals anywhere else in this file.
    """
    source_path = Path(__file__)
    text = source_path.read_text(encoding="utf-8")
    vault_dirname = "wiki"
    forbidden_tokens = [
        f'Path("{vault_dirname}")',
        f"Path('{vault_dirname}')",
        f'reset_vault("{vault_dirname}")',
        f"reset_vault('{vault_dirname}')",
        f'"reset-vault", "{vault_dirname}"',
        f"'reset-vault', '{vault_dirname}'",
    ]
    for token in forbidden_tokens:
        assert token not in text, (
            f"tests/test_cli.py contains the forbidden literal {token!r} — "
            "this file must only target tmp_path-rooted vaults to keep the "
            "workspace's live vault safe."
        )


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
    def test_missing_qmd_exits_one(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        vault = _copy_vault(tmp_path)
        monkeypatch.setattr("wikipilot.cli.qmd_available", lambda: False)
        result = runner.invoke(main, ["index-wiki", str(vault)])
        assert result.exit_code == 1
        # Click's CliRunner merges stderr into output by default.
        assert "qmd not importable" in result.output

    def test_qmd_present_indexes_and_exits_zero(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from wikipilot.qmd_index import IndexResult

        vault = _copy_vault(tmp_path)
        monkeypatch.setattr("wikipilot.cli.qmd_available", lambda: True)
        called: dict[str, object] = {}

        def fake_index_vault(vault_path: Path, *, full: bool = False) -> IndexResult:
            called["vault_path"] = vault_path
            called["full"] = full
            return IndexResult(
                ok=True,
                qmd_available=True,
                indexed_files=2,
                added=2,
                updated=0,
                deleted=0,
                skipped=0,
                message="indexed 2 file(s)",
            )

        monkeypatch.setattr("wikipilot.cli.index_vault", fake_index_vault)
        result = runner.invoke(main, ["index-wiki", str(vault), "--full"])
        assert result.exit_code == 0, result.output
        assert called["full"] is True
        assert called["vault_path"] == vault
        assert "indexed 2 file(s)" in result.output

    def test_qmd_present_index_failure_exits_one(
        self, runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from wikipilot.qmd_index import IndexResult

        vault = _copy_vault(tmp_path)
        monkeypatch.setattr("wikipilot.cli.qmd_available", lambda: True)

        def fake_index_vault(vault_path: Path, *, full: bool = False) -> IndexResult:
            return IndexResult(
                ok=False,
                qmd_available=True,
                indexed_files=0,
                added=0,
                updated=0,
                deleted=0,
                skipped=0,
                message="boom",
            )

        monkeypatch.setattr("wikipilot.cli.index_vault", fake_index_vault)
        result = runner.invoke(main, ["index-wiki", str(vault)])
        assert result.exit_code == 1
        assert "boom" in result.output


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
        assert captured["json"] == {"text": "topic_id=ai-agents"}
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
