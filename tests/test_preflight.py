"""Tests for ``scripts/preflight.py``."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.preflight import (  # noqa: E402
    CheckStatus,
    main,
    run_preflight,
)


@pytest.fixture
def fake_repo(tmp_path: Path) -> Path:
    """A minimal repo skeleton: wiki/ + topics.yaml + topics/<id>/purpose.md."""
    (tmp_path / "wiki").mkdir()
    (tmp_path / "wiki" / "topics" / "ai-agents").mkdir(parents=True)
    (tmp_path / "wiki" / "topics" / "ai-agents" / "purpose.md").write_text(
        "# Purpose\n", encoding="utf-8"
    )
    (tmp_path / "topics.yaml").write_text(
        'topics:\n  - id: ai-agents\n    display_name: "AI agents"\n    purpose: "p"\n',
        encoding="utf-8",
    )
    return tmp_path


class TestRunPreflight:
    def test_happy_path(self, fake_repo: Path) -> None:
        result = run_preflight(repo_root=fake_repo, skip_qmd=True)
        assert result.ok, result.render()

    def test_missing_wiki_dir(self, tmp_path: Path) -> None:
        result = run_preflight(repo_root=tmp_path, skip_qmd=True)
        assert result.ok is False
        wiki_check = next(c for c in result.checks if "wiki/ exists" in c.name)
        assert wiki_check.status == CheckStatus.FAIL

    def test_missing_topics_yaml(self, tmp_path: Path) -> None:
        (tmp_path / "wiki").mkdir()
        result = run_preflight(repo_root=tmp_path, skip_qmd=True)
        assert result.ok is False
        topics_check = next(c for c in result.checks if c.name == "topics.yaml")
        assert topics_check.status == CheckStatus.FAIL

    def test_missing_purpose_md(self, tmp_path: Path) -> None:
        (tmp_path / "wiki").mkdir()
        (tmp_path / "topics.yaml").write_text(
            'topics:\n  - id: ai-agents\n    display_name: "AI agents"\n    purpose: "p"\n',
            encoding="utf-8",
        )
        result = run_preflight(repo_root=tmp_path, skip_qmd=True)
        assert result.ok is False
        purpose_check = next(c for c in result.checks if "purpose.md" in c.name)
        assert purpose_check.status == CheckStatus.FAIL
        assert "ai-agents" in purpose_check.message

    def test_invalid_topics_yaml(self, tmp_path: Path) -> None:
        (tmp_path / "wiki").mkdir()
        (tmp_path / "topics.yaml").write_text(
            "topics:\n  - id: foo\n",  # missing display_name + purpose
            encoding="utf-8",
        )
        result = run_preflight(repo_root=tmp_path, skip_qmd=True)
        assert result.ok is False
        topics_check = next(c for c in result.checks if c.name == "topics.yaml")
        assert topics_check.status == CheckStatus.FAIL

    def test_required_env_var_missing(
        self, fake_repo: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("WIKIPILOT_AUTO_MERGE", raising=False)
        result = run_preflight(
            repo_root=fake_repo, skip_qmd=True, required_env=["WIKIPILOT_AUTO_MERGE"]
        )
        assert result.ok is False
        env_check = next(c for c in result.checks if c.name == "env: WIKIPILOT_AUTO_MERGE")
        assert env_check.status == CheckStatus.FAIL

    def test_required_env_var_set(self, fake_repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("WIKIPILOT_AUTO_MERGE", "true")
        result = run_preflight(
            repo_root=fake_repo, skip_qmd=True, required_env=["WIKIPILOT_AUTO_MERGE"]
        )
        env_check = next(c for c in result.checks if c.name == "env: WIKIPILOT_AUTO_MERGE")
        assert env_check.status == CheckStatus.OK

    def test_qmd_not_installed(self, fake_repo: Path) -> None:
        with patch("scripts.preflight.qmd_available", return_value=False):
            result = run_preflight(repo_root=fake_repo)
        qmd_check = next(c for c in result.checks if c.name == "qmd indexed")
        assert qmd_check.status == CheckStatus.FAIL
        assert "qmd not on PATH" in qmd_check.message

    def test_qmd_installed_but_no_index(self, fake_repo: Path) -> None:
        with patch("scripts.preflight.qmd_available", return_value=True):
            result = run_preflight(repo_root=fake_repo)
        qmd_check = next(c for c in result.checks if c.name == "qmd indexed")
        assert qmd_check.status == CheckStatus.WARN

    def test_qmd_installed_with_index(self, fake_repo: Path) -> None:
        (fake_repo / ".qmd").mkdir()
        with patch("scripts.preflight.qmd_available", return_value=True):
            result = run_preflight(repo_root=fake_repo)
        qmd_check = next(c for c in result.checks if c.name == "qmd indexed")
        assert qmd_check.status == CheckStatus.OK


class TestPreflightCli:
    def test_main_returns_zero_on_ok(
        self, fake_repo: Path, monkeypatch: pytest.MonkeyPatch, capsys
    ) -> None:
        monkeypatch.chdir(fake_repo)
        rc = main(["--skip-qmd"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "[OK]" in out

    def test_main_returns_one_on_failure(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys
    ) -> None:
        monkeypatch.chdir(tmp_path)
        rc = main(["--skip-qmd"])
        assert rc == 1
        out = capsys.readouterr().out
        assert "[FAIL]" in out


class TestRender:
    def test_render_includes_status_for_each_check(self, fake_repo: Path) -> None:
        result = run_preflight(repo_root=fake_repo, skip_qmd=True)
        rendered = result.render()
        # Every check should contribute exactly one line.
        assert rendered.count("\n") == len(result.checks) - 1


class TestEnvironmentBinaryChecks:
    def test_git_required(self, fake_repo: Path) -> None:
        # Whatever the host has, git is required and shutil.which decides.
        result = run_preflight(repo_root=fake_repo, skip_qmd=True)
        git_check = next(c for c in result.checks if c.name == "git on PATH")
        if shutil.which("git"):
            assert git_check.status == CheckStatus.OK
        else:
            assert git_check.status == CheckStatus.FAIL
