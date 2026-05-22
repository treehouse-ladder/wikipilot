"""Tests for the ``wikipilot recover-prs`` CLI subcommand."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from wikipilot.cli import main


def _ok(stdout: str = "", returncode: int = 0) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, "")


@pytest.fixture
def cli_runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def repo_with_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Drop a minimal wikipilot.toml into a temp directory and chdir into it.

    The CLI defaults to ``./wikipilot.toml`` for ``--config``; chdir-ing means
    the test can omit the flag and still get a real config.
    """
    config_text = (
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
        "max_total_diff_lines = 2000\n"
    )
    cfg = tmp_path / "wikipilot.toml"
    cfg.write_text(config_text, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    return cfg


def _pr_view_payload(
    *,
    files: list[str] | None = None,
    additions: int = 5,
    conclusion: str = "SUCCESS",
    number: int = 1,
) -> str:
    return json.dumps(
        {
            "number": number,
            "state": "OPEN",
            "files": [{"path": p} for p in (files or ["wiki/concepts/x.md"])],
            "additions": additions,
            "deletions": 0,
            "isDraft": False,
            "statusCheckRollup": [{"conclusion": conclusion}],
            "isCrossRepository": False,
            "author": {"login": "rauriemo"},
        }
    )


# PR Watcher v2's centralized trust check now fires inside every gate call.
# The recover-prs CLI uses ``apply_gate`` (full gate, including CI) which
# means ``view_pr`` makes two extra subprocess calls per PR:
#   - ``gh repo view --json nameWithOwner`` to resolve owner/repo
#   - ``gh api repos/<owner>/<repo>/pulls/<num>`` to fetch author_association
# Tests that want recover-prs to succeed on a "trusted MEMBER PR" baseline
# must mock those two endpoints; tests that want to exercise the untrusted
# path override the api response.
_OWNER_REPO_PAYLOAD = json.dumps({"nameWithOwner": "treehouse-ladder/wikipilot"})
_TRUSTED_API_PAYLOAD = json.dumps(
    {"user": {"login": "rauriemo"}, "author_association": "MEMBER"}
)


def _trusted_handler(args):
    """Return canned ``gh repo view`` / ``gh api`` responses for the trusted
    baseline, or ``None`` to let the caller's fake_run handle the args."""
    if args[:3] == ["gh", "repo", "view"]:
        return _ok(stdout=_OWNER_REPO_PAYLOAD)
    if args[:2] == ["gh", "api"]:
        return _ok(stdout=_TRUSTED_API_PAYLOAD)
    return None


def test_empty_pr_list_exits_zero(cli_runner: CliRunner, repo_with_config: Path) -> None:
    def fake_run(args, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout="[]")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs"])
    assert result.exit_code == 0, result.output
    assert "0 PRs to recover" in result.output


def test_dry_run_skips_gh_mutations(cli_runner: CliRunner, repo_with_config: Path) -> None:
    pr_list = json.dumps(
        [
            {"number": 7, "headRefName": "claude/daily-2026-05-21/x"},
            {"number": 8, "headRefName": "claude/query-2026-05-21-y"},
            {"number": 9, "headRefName": "claude/health-2026-05-21"},
        ]
    )

    pr_views = {
        7: _pr_view_payload(number=7),
        8: _pr_view_payload(number=8),
        9: _pr_view_payload(number=9),
    }

    calls: list[list[str]] = []

    def fake_run(args, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            pr_num = int(args[3])
            return _ok(stdout=pr_views[pr_num])
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs", "--dry-run"])
    assert result.exit_code == 0, result.output
    # All three rows should appear in the tabular output.
    for pr in (7, 8, 9):
        assert str(pr) in result.output
    # Dry-run must NEVER mutate GH.
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)
    assert not any(c[:3] == ["gh", "pr", "comment"] for c in calls)


def test_enumerates_claude_branches_and_invokes_apply_gate(
    cli_runner: CliRunner, repo_with_config: Path
) -> None:
    pr_list = json.dumps(
        [
            {"number": 11, "headRefName": "claude/daily-2026-05-21/agentic-coding"},
            {"number": 12, "headRefName": "claude/query-2026-05-21-q"},
            {"number": 13, "headRefName": "claude/health-2026-05-21"},
        ]
    )
    pr_views = {
        11: _pr_view_payload(number=11),
        12: _pr_view_payload(number=12),
        13: _pr_view_payload(number=13),
    }
    calls: list[list[str]] = []

    def fake_run(args, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            pr_num = int(args[3])
            return _ok(stdout=pr_views[pr_num])
        trusted = _trusted_handler(args)
        if trusted is not None:
            return trusted
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs"])
    assert result.exit_code == 0, result.output
    # apply_gate -> enable_automerge for each PR.
    merges = [c for c in calls if c[:3] == ["gh", "pr", "merge"]]
    assert len(merges) == 3
    # Route inference per PR — the route label appears in the row output.
    assert "daily_research" in result.output
    assert "wiki_query" in result.output
    assert "weekly_health" in result.output


def test_skips_non_claude_branches_in_all_mode(
    cli_runner: CliRunner, repo_with_config: Path
) -> None:
    pr_list = json.dumps(
        [
            {"number": 22, "headRefName": "fix/some-thing"},
            {"number": 23, "headRefName": "claude/daily-2026-05-21/x"},
        ]
    )
    pr_views = {
        22: _pr_view_payload(number=22),
        23: _pr_view_payload(number=23),
    }
    calls: list[list[str]] = []

    def fake_run(args, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            pr_num = int(args[3])
            return _ok(stdout=pr_views[pr_num])
        trusted = _trusted_handler(args)
        if trusted is not None:
            return trusted
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs", "--all"])
    assert result.exit_code == 0, result.output
    assert "skip" in result.output
    assert "22" in result.output
    # The claude/* PR still gets merged; the human PR does NOT.
    merges = [c for c in calls if c[:3] == ["gh", "pr", "merge"]]
    assert len(merges) == 1


def test_default_filters_out_non_claude_heads(
    cli_runner: CliRunner, repo_with_config: Path
) -> None:
    """Without --all, non-claude branches in the gh pr list response are dropped client-side."""
    pr_list = json.dumps(
        [
            {"number": 22, "headRefName": "fix/some-thing"},
            {"number": 23, "headRefName": "claude/daily-2026-05-21/x"},
        ]
    )
    pr_views = {23: _pr_view_payload(number=23)}

    def fake_run(args, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(stdout=pr_views[int(args[3])])
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs"])
    assert result.exit_code == 0, result.output
    # The non-claude head is dropped before being printed.
    assert "fix/some-thing" not in result.output
    assert "23" in result.output


def test_tabular_summary_header(cli_runner: CliRunner, repo_with_config: Path) -> None:
    pr_list = json.dumps([{"number": 31, "headRefName": "claude/daily-2026-05-21/x"}])

    def fake_run(args, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(stdout=_pr_view_payload(number=31))
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs"])
    assert result.exit_code == 0, result.output
    assert "PR" in result.output
    assert "ROUTE" in result.output
    assert "DECISION" in result.output


def test_custom_base_branch_forwarded(cli_runner: CliRunner, repo_with_config: Path) -> None:
    """``--base release-2026`` passes through to ``gh pr list --base release-2026``."""
    calls: list[list[str]] = []

    def fake_run(args, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout="[]")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs", "--base", "release-2026"])
    assert result.exit_code == 0, result.output
    list_calls = [c for c in calls if c[:3] == ["gh", "pr", "list"]]
    assert list_calls
    call = list_calls[0]
    assert "--base" in call
    assert call[call.index("--base") + 1] == "release-2026"


def test_dry_run_blocked_pr_does_not_mutate(cli_runner: CliRunner, repo_with_config: Path) -> None:
    """A PR that would block (e.g. human-only path) still doesn't call gh pr comment in dry-run."""
    pr_list = json.dumps([{"number": 41, "headRefName": "claude/daily-2026-05-21/x"}])

    def fake_run(args, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(stdout=pr_list)
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(stdout=_pr_view_payload(number=41, files=["CLAUDE.md"]))
        return _ok()

    calls: list[list[str]] = []

    def recording_run(args, **kwargs):
        calls.append(list(args))
        return fake_run(args, **kwargs)

    with patch("subprocess.run", side_effect=recording_run):
        result = cli_runner.invoke(main, ["recover-prs", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "blocked" in result.output
    assert "CLAUDE.md" in result.output or "human-only" in result.output
    # Dry-run NEVER posts a comment.
    assert not any(c[:3] == ["gh", "pr", "comment"] for c in calls)


def test_gh_pr_list_failure_exits_two(cli_runner: CliRunner, repo_with_config: Path) -> None:
    def fake_run(args, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(returncode=1, stdout="boom")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        result = cli_runner.invoke(main, ["recover-prs"])
    assert result.exit_code == 2
    assert "ERROR" in result.output or "ERROR" in (result.stderr or "")
