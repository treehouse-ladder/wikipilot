"""Tests for ``scripts/pr_watcher_gate.py`` (the watcher CLI shim).

Mirrors the shape of :mod:`tests.test_maybe_automerge` — imports the script's
``main`` function and patches ``subprocess.run`` to canned-respond to every
``gh`` invocation the script makes.
"""

from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "pr_watcher_gate.py"


def _ok(
    stdout: str = "", stderr: str = "", returncode: int = 0
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, stderr)


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
        "max_total_diff_lines = 2000\n"
        "\n"
        "[automerge.pr_watcher]\n"
        "ci_wait_timeout_sec = 60\n"
        "self_heal_max_attempts = 3\n",
        encoding="utf-8",
    )
    return config


def _import_main():
    """Import the script's main as a fresh module each call so module-level
    state (e.g. the ``_heal_signal_printed`` flag) doesn't leak between tests."""
    sys.path.insert(0, str(REPO_ROOT))
    module_name = "scripts.pr_watcher_gate"
    if module_name in sys.modules:
        del sys.modules[module_name]
    module = importlib.import_module(module_name)
    return module.main


def _meta(
    *,
    head: str = "claude/daily-2026-05-21/agentic-coding",
    state: str = "OPEN",
    is_draft: bool = False,
    labels: list[str] | None = None,
) -> str:
    return json.dumps(
        {
            "headRefName": head,
            "state": state,
            "isDraft": is_draft,
            "labels": [{"name": name} for name in (labels or [])],
        }
    )


def _pr_view_payload(
    *,
    files: list[str] | None = None,
    additions: int = 5,
    conclusion: str = "SUCCESS",
    state: str = "OPEN",
    is_draft: bool = False,
    number: int = 42,
) -> str:
    return json.dumps(
        {
            "number": number,
            "state": state,
            "files": [{"path": p} for p in (files or ["wiki/concepts/x.md"])],
            "additions": additions,
            "deletions": 0,
            "isDraft": is_draft,
            "statusCheckRollup": [{"conclusion": conclusion}],
        }
    )


def _build_fake_run(
    handlers: dict[str, list[subprocess.CompletedProcess[str]]], calls: list[list[str]]
):
    """Build a ``subprocess.run`` stand-in that pops from a per-prefix queue.

    Each ``handlers[prefix]`` is a list of canned responses returned in order
    for calls whose ``args[:3]`` joined by spaces equals ``prefix``. Falls
    back to a generic 0-exit ``CompletedProcess`` when no handler matches.
    """

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        key = " ".join(args[:3])
        queue = handlers.get(key)
        if queue:
            return queue.pop(0) if len(queue) > 1 else queue[0]
        return _ok()

    return fake_run


def test_enforce_mode_claude_daily_green_ci_enables_automerge(
    repo_with_config: Path, capsys
) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [_ok(stdout=_meta()), _ok(stdout=_pr_view_payload())],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "route=daily_research" in out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_read_only_mode_for_non_claude_branch_only_comments(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(head="fix/some-thing")),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "read_only" in out
    # Read-only path never queues / disables auto-merge.
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_enforce_red_ci_disables_automerge_and_comments(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(head="claude/query-2026-05-21-x")),
            _ok(stdout=_pr_view_payload(conclusion="FAILURE")),
        ],
        # gh pr checks --watch exits non-zero on red CI.
        "gh pr checks": [_ok(returncode=1, stderr="failed")],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "route=wiki_query" in out
    # CI red on a claude/* PR with no prior heal-attempt labels -> HEAL_NEEDED signal.
    assert "HEAL_NEEDED" in out
    # The gate calls --disable-auto when enforce mode + CI red.
    merges = [c for c in calls if c[:3] == ["gh", "pr", "merge"]]
    assert any("--disable-auto" in c for c in merges)


def test_heal_attempt_label_counter_signals_heal_needed(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(
                stdout=_meta(
                    head="claude/daily-2026-05-21/x",
                    labels=["wikipilot:heal-attempt-1"],
                )
            ),
            _ok(stdout=_pr_view_payload(conclusion="FAILURE")),
        ],
        "gh pr checks": [_ok(returncode=1)],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "HEAL_NEEDED" in out
    assert "next_attempt=2" in out


def test_heal_attempt_label_counter_caps_at_max(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(
                stdout=_meta(
                    head="claude/daily-2026-05-21/x",
                    labels=["wikipilot:heal-attempt-3"],
                )
            ),
            _ok(stdout=_pr_view_payload(conclusion="FAILURE")),
        ],
        "gh pr checks": [_ok(returncode=1)],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "HEAL_CAPPED" in out
    assert "max=3" in out
    assert "HEAL_NEEDED" not in out


def test_idempotent_on_already_merged_pr(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {"gh pr view": [_ok(stdout=_meta(state="MERGED"))]}
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "state=MERGED" in out
    # No gh pr merge / checks / comment calls when the PR is already merged.
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)
    assert not any(c[:3] == ["gh", "pr", "checks"] for c in calls)
    assert not any(c[:3] == ["gh", "pr", "comment"] for c in calls)


def test_skips_draft_prs(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {"gh pr view": [_ok(stdout=_meta(is_draft=True))]}
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "draft" in out.lower()
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_ci_wait_timeout_still_runs_gate_and_exits_zero(repo_with_config: Path, capsys) -> None:
    """A TimeoutExpired on gh pr checks --watch is recoverable; the gate still runs."""
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        key = " ".join(args[:3])
        if key == "gh pr view":
            # First call returns metadata; subsequent calls return PR view.
            view_calls = [c for c in calls if c[:3] == ["gh", "pr", "view"]]
            if len(view_calls) == 1:
                return _ok(stdout=_meta(head="claude/daily-2026-05-21/x"))
            return _ok(stdout=_pr_view_payload(conclusion="PENDING"))
        if key == "gh pr checks":
            raise subprocess.TimeoutExpired(cmd="gh", timeout=1)
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "CI did not finish green" in out


def test_route_inferred_from_branch_drives_threshold(repo_with_config: Path, capsys) -> None:
    """Same PR shape, different head ref -> different route -> different gate."""
    cli_main = _import_main()
    # 9 files exceeds wiki_query gate (max 8) but is fine for daily (max 40).
    big_files = [f"wiki/concepts/x{i}.md" for i in range(9)]

    # First: head is query, expect blocked.
    calls_q: list[list[str]] = []
    handlers_q = {
        "gh pr view": [
            _ok(stdout=_meta(head="claude/query-2026-05-21-q")),
            _ok(stdout=_pr_view_payload(files=big_files)),
        ],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers_q, calls_q)):
        cli_main(["--pr", "42", "--config", str(repo_with_config)])
    out_q = capsys.readouterr().out
    assert "did NOT pass" in out_q
    assert "files" in out_q

    # Second: head is daily, same files -> passes.
    cli_main = _import_main()
    calls_d: list[list[str]] = []
    handlers_d = {
        "gh pr view": [
            _ok(stdout=_meta(head="claude/daily-2026-05-21/x")),
            _ok(stdout=_pr_view_payload(files=big_files)),
        ],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers_d, calls_d)):
        cli_main(["--pr", "42", "--config", str(repo_with_config)])
    out_d = capsys.readouterr().out
    assert "auto-merge enabled" in out_d


def test_skip_ci_wait_flag_skips_gh_pr_checks(repo_with_config: Path) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [_ok(stdout=_meta()), _ok(stdout=_pr_view_payload())],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        cli_main(["--pr", "42", "--config", str(repo_with_config), "--skip-ci-wait"])
    assert not any(c[:3] == ["gh", "pr", "checks"] for c in calls)


def test_missing_pr_metadata_exits_zero(repo_with_config: Path, capsys) -> None:
    cli_main = _import_main()
    calls: list[list[str]] = []

    def fake_run(args, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "view"]:
            return _ok(returncode=1, stderr="not found")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "could not fetch metadata" in out
