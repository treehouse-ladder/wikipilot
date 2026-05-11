"""Tests for ``scripts/maybe_automerge.py`` (the CLI shim)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "maybe_automerge.py"


def _ok(stdout: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], 0, stdout, "")


@pytest.fixture
def repo_with_config(tmp_path: Path) -> Path:
    config = tmp_path / "wikipilot.toml"
    config.write_text(
        "[automerge.common]\n"
        "require_lint_green = true\n"
        "require_tests_green = true\n"
        "block_human_only_file_changes = true\n"
        "\n"
        "[automerge.daily_research]\n"
        "max_files_changed_per_topic = 40\n"
        "max_total_diff_lines_per_topic = 1500\n"
        "\n"
        "[automerge.wiki_query]\n"
        "max_files_changed = 8\n"
        "max_total_diff_lines = 400\n"
        "\n"
        "[automerge.weekly_health]\n"
        "max_files_changed = 60\n"
        "max_total_diff_lines = 2000\n",
        encoding="utf-8",
    )
    return config


def _import_main():
    sys.path.insert(0, str(REPO_ROOT))
    from scripts.maybe_automerge import main as cli_main

    return cli_main


def _gh_payload(
    files: list[str], additions: int = 5, conclusion: str = "SUCCESS", state: str = "OPEN"
) -> str:
    return json.dumps(
        {
            "number": 99,
            "state": state,
            "files": [{"path": p} for p in files],
            "additions": additions,
            "deletions": 0,
            "isDraft": False,
            "statusCheckRollup": [{"conclusion": conclusion}],
        }
    )


def test_passes_returns_zero_and_invokes_automerge(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(_gh_payload(["wiki/concepts/x.md"]))
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_fails_returns_zero_and_comments(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            # Touch CLAUDE.md to trigger ownership-violation -> gate blocks.
            return _ok(_gh_payload(["CLAUDE.md"]))
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "did NOT pass" in out
    assert "CLAUDE.md" in out
    assert any(c[:3] == ["gh", "pr", "comment"] for c in calls)
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_route_choice_enforced(repo_with_config: Path) -> None:
    cli_main = _import_main()
    with pytest.raises(SystemExit):
        cli_main(["--pr", "99", "--route", "bogus", "--config", str(repo_with_config)])


def test_failing_checks_blocks(repo_with_config: Path) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(_gh_payload(["wiki/concepts/x.md"], conclusion="FAILURE"))
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    assert any(c[:3] == ["gh", "pr", "comment"] for c in calls)


def test_query_route_smaller_threshold(repo_with_config: Path) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            files = [f"wiki/concepts/x{i}.md" for i in range(9)]  # exceeds wiki_query gate
            return _ok(_gh_payload(files))
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--pr", "99", "--route", "wiki_query", "--config", str(repo_with_config)])
    assert rc == 0
    assert any(c[:3] == ["gh", "pr", "comment"] for c in calls)
