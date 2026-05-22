"""Tests for ``scripts/maybe_automerge.py`` (the static-gate CLI shim).

PR Watcher v2 switched this script from ``apply_gate`` to
``apply_static_gate``: the local CI prediction is gone and GitHub's own
required-status-checks rule holds the merge until CI is green. The
script's contract is now "queue ``--auto`` iff the deterministic gate
(file count, diff lines, human-only paths, trust) passes; otherwise
post a checklist comment". That contract is what these tests pin down.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "maybe_automerge.py"


def _ok(stdout: str = "", *, returncode: int = 0) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, "")


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
    if "scripts.maybe_automerge" in sys.modules:
        del sys.modules["scripts.maybe_automerge"]
    from scripts.maybe_automerge import main as cli_main

    return cli_main


def _gh_payload(
    files: list[str],
    additions: int = 5,
    conclusion: str = "SUCCESS",
    state: str = "OPEN",
    *,
    is_cross_repository: bool = False,
    author_login: str = "rauriemo",
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
            "isCrossRepository": is_cross_repository,
            "author": {"login": author_login},
        }
    )


_OWNER_REPO_PAYLOAD = json.dumps({"nameWithOwner": "treehouse-ladder/wikipilot"})
_TRUSTED_API_PAYLOAD = json.dumps(
    {"user": {"login": "rauriemo"}, "author_association": "MEMBER"}
)


def _fake_run(
    *,
    pr_view_payload: str,
    api_payload: str = _TRUSTED_API_PAYLOAD,
    owner_repo_payload: str = _OWNER_REPO_PAYLOAD,
):
    """Build a ``subprocess.run`` stand-in for the static gate's call sequence."""
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(pr_view_payload)
        if args[:3] == ["gh", "repo", "view"]:
            return _ok(owner_repo_payload)
        if args[:2] == ["gh", "api"]:
            return _ok(api_payload)
        return _ok()

    return fake_run, calls


def test_passes_returns_zero_and_invokes_automerge(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    fake_run, calls = _fake_run(pr_view_payload=_gh_payload(["wiki/concepts/x.md"]))
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
    # Touch CLAUDE.md -> ownership-violation -> static gate blocks.
    fake_run, calls = _fake_run(pr_view_payload=_gh_payload(["CLAUDE.md"]))
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


def test_static_gate_ignores_pending_ci_and_queues_automerge(
    repo_with_config: Path, capsys
) -> None:
    """The whole point of the v2 cutover: pending CI (rollup empty)
    must still queue ``--auto``. GitHub's required-status-checks rule
    is what now holds the merge until CI goes green."""
    cli_main = _import_main()
    # statusCheckRollup empty -> CI not yet started. The static gate
    # MUST still queue --auto in this case (the bug we're fixing).
    payload = json.dumps(
        {
            "number": 99,
            "state": "OPEN",
            "files": [{"path": "wiki/concepts/x.md"}],
            "additions": 5,
            "deletions": 0,
            "isDraft": False,
            "statusCheckRollup": [],
            "isCrossRepository": False,
            "author": {"login": "rauriemo"},
        }
    )
    fake_run, calls = _fake_run(pr_view_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_failing_ci_still_queues_automerge_for_github_to_hold(
    repo_with_config: Path, capsys
) -> None:
    """Even a red CI rollup must queue ``--auto``. GitHub's
    required-status-checks rule then refuses to merge. The local script
    no longer predicts CI — that prediction was the bug."""
    cli_main = _import_main()
    fake_run, calls = _fake_run(
        pr_view_payload=_gh_payload(["wiki/concepts/x.md"], conclusion="FAILURE")
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_query_route_smaller_threshold(repo_with_config: Path) -> None:
    cli_main = _import_main()
    files = [f"wiki/concepts/x{i}.md" for i in range(9)]  # exceeds wiki_query gate
    fake_run, calls = _fake_run(pr_view_payload=_gh_payload(files))
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--pr", "99", "--route", "wiki_query", "--config", str(repo_with_config)])
    assert rc == 0
    assert any(c[:3] == ["gh", "pr", "comment"] for c in calls)


def test_untrusted_author_blocks_automerge(repo_with_config: Path, capsys) -> None:
    """Centralized trust check fires regardless of how the orchestrator
    called the script. An untrusted author NEVER queues ``--auto``."""
    cli_main = _import_main()
    api_payload = json.dumps({"author_association": "NONE", "user": {"login": "stranger"}})
    fake_run, calls = _fake_run(
        pr_view_payload=_gh_payload(["wiki/concepts/x.md"], author_login="stranger"),
        api_payload=api_payload,
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "did NOT pass" in out
    assert "not trusted" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_fork_pr_blocks_automerge(repo_with_config: Path, capsys) -> None:
    """A claude/* PR opened from a fork must NOT queue auto-merge,
    even if the author happens to be an org member."""
    cli_main = _import_main()
    fake_run, calls = _fake_run(
        pr_view_payload=_gh_payload(["wiki/concepts/x.md"], is_cross_repository=True),
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(
            ["--pr", "99", "--route", "daily_research", "--config", str(repo_with_config)]
        )
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert "fork=True" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)
