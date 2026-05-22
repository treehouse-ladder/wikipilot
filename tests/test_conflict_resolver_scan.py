"""Tests for ``scripts/conflict_resolver_scan.py`` (PR Watcher v2 scan).

The scan's job is to enumerate every open ``claude/*`` PR to ``main``
that is *dispatch-worthy* — DIRTY (text conflicts) or BEHIND
(out-of-date with base) and from a trusted author. Anything else is
filtered out client-side. These tests pin that filter behavior against
a fake ``gh pr list``.
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


def _ok(
    stdout: str = "", *, returncode: int = 0, stderr: str = ""
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, stderr)


@pytest.fixture
def empty_config(tmp_path: Path) -> Path:
    config = tmp_path / "wikipilot.toml"
    # Default branches templates + default trust config.
    config.write_text("", encoding="utf-8")
    return config


def _import_main():
    sys.path.insert(0, str(REPO_ROOT))
    module_name = "scripts.conflict_resolver_scan"
    if module_name in sys.modules:
        del sys.modules[module_name]
    module = importlib.import_module(module_name)
    return module.main


def _pr(
    *,
    number: int,
    head: str,
    state: str = "DIRTY",
    is_cross_repository: bool = False,
    author_login: str = "rauriemo",
    title: str = "wiki(x): daily 2026-05-22",
) -> dict:
    return {
        "number": number,
        "headRefName": head,
        "baseRefName": "main",
        "mergeStateStatus": state,
        "isCrossRepository": is_cross_repository,
        "author": {"login": author_login},
        "title": title,
    }


_OWNER_REPO_PAYLOAD = json.dumps({"nameWithOwner": "treehouse-ladder/wikipilot"})
_TRUSTED_API_PAYLOAD = json.dumps({"author_association": "MEMBER"})


def _fake_run(
    *,
    pr_list_payload: str,
    api_payloads: dict[int, str] | None = None,
):
    """Build a ``subprocess.run`` stand-in for the scan's call sequence.

    ``api_payloads`` maps PR number to a ``gh api`` JSON response so a
    single test can mix trusted and untrusted authors across PRs.
    """
    calls: list[list[str]] = []
    api_payloads = api_payloads or {}

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(pr_list_payload)
        if args[:3] == ["gh", "repo", "view"]:
            return _ok(_OWNER_REPO_PAYLOAD)
        if args[:2] == ["gh", "api"]:
            # args[2] is the endpoint, e.g. repos/o/r/pulls/28
            for num, payload in api_payloads.items():
                if f"/pulls/{num}" in args[2]:
                    return _ok(payload)
            return _ok(_TRUSTED_API_PAYLOAD)
        return _ok()

    return fake_run, calls


def test_empty_pr_list_returns_empty_array(empty_config: Path, capsys) -> None:
    cli_main = _import_main()
    fake_run, _ = _fake_run(pr_list_payload="[]")
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert json.loads(out) == []


def test_dirty_claude_pr_is_emitted(empty_config: Path, capsys) -> None:
    cli_main = _import_main()
    payload = json.dumps(
        [_pr(number=28, head="claude/daily-2026-05-22/frontier-models", state="DIRTY")]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 1
    entry = out[0]
    assert entry["number"] == 28
    assert entry["head_ref"] == "claude/daily-2026-05-22/frontier-models"
    assert entry["base_ref"] == "main"
    assert entry["route"] == "daily_research"
    assert entry["merge_state_status"] == "DIRTY"
    assert entry["author_association"] == "MEMBER"


def test_behind_claude_pr_is_emitted(empty_config: Path, capsys) -> None:
    """BEHIND (not just DIRTY) is also dispatch-worthy — a simple rebase
    unblocks GitHub's auto-merge queue even when there are no textual
    conflicts to resolve."""
    cli_main = _import_main()
    payload = json.dumps([_pr(number=29, head="claude/query-2026-05-22-x", state="BEHIND")])
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 1
    assert out[0]["merge_state_status"] == "BEHIND"
    assert out[0]["route"] == "wiki_query"


def test_clean_pr_is_filtered_out(empty_config: Path, capsys) -> None:
    cli_main = _import_main()
    payload = json.dumps([_pr(number=30, head="claude/daily-2026-05-22/foo", state="CLEAN")])
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert out == []


def test_unknown_merge_state_is_skipped(empty_config: Path, capsys) -> None:
    """GitHub hasn't computed mergeability yet — skip rather than race;
    the next push will re-evaluate."""
    cli_main = _import_main()
    payload = json.dumps([_pr(number=31, head="claude/daily-2026-05-22/foo", state="UNKNOWN")])
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_non_claude_head_is_filtered_out(empty_config: Path, capsys) -> None:
    """The Conflict Resolver only touches routine-produced PRs. A human's
    DIRTY PR is left alone (the human resolves it themselves)."""
    cli_main = _import_main()
    payload = json.dumps([_pr(number=32, head="fix/some-thing", state="DIRTY")])
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_fork_pr_is_filtered_out(empty_config: Path, capsys) -> None:
    """An untrusted PR (here: from a fork) must NOT be queued for the
    Opus subagent — even when the head ref shape would match a route."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=33,
                head="claude/daily-2026-05-22/foo",
                state="DIRTY",
                is_cross_repository=True,
            )
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_untrusted_association_is_filtered_out(empty_config: Path, capsys) -> None:
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=34,
                head="claude/daily-2026-05-22/foo",
                state="DIRTY",
                author_login="stranger",
            )
        ]
    )
    api_payloads = {34: json.dumps({"author_association": "NONE"})}
    fake_run, _ = _fake_run(pr_list_payload=payload, api_payloads=api_payloads)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_api_failure_treats_pr_as_untrusted(empty_config: Path, capsys) -> None:
    """A transient ``gh api`` failure must fail-closed — never queue the
    Opus subagent on a PR whose trust signal couldn't be fetched."""
    cli_main = _import_main()
    payload = json.dumps([_pr(number=35, head="claude/daily-2026-05-22/foo", state="DIRTY")])

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(payload)
        if args[:3] == ["gh", "repo", "view"]:
            return _ok(_OWNER_REPO_PAYLOAD)
        if args[:2] == ["gh", "api"]:
            return _ok(returncode=1, stderr="HTTP 401")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_mixed_list_emits_only_dispatch_worthy_entries(empty_config: Path, capsys) -> None:
    """End-to-end: a realistic mix where one PR is dirty+trusted, one is
    clean, one is dirty but a fork, and one isn't a claude/* branch.
    Only the first should land in the JSON output."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(number=40, head="claude/daily-2026-05-22/a", state="DIRTY"),
            _pr(number=41, head="claude/daily-2026-05-22/b", state="CLEAN"),
            _pr(
                number=42,
                head="claude/daily-2026-05-22/c",
                state="DIRTY",
                is_cross_repository=True,
            ),
            _pr(number=43, head="feature/manual", state="DIRTY"),
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert [e["number"] for e in out] == [40]


def test_gh_failure_exits_two(empty_config: Path, capsys) -> None:
    cli_main = _import_main()

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(returncode=1, stderr="rate limited")
        return _ok()

    with patch("subprocess.run", side_effect=fake_run), pytest.raises(SystemExit) as exc_info:
        cli_main(["--base", "main", "--config", str(empty_config)])
    assert exc_info.value.code == 2
    err = capsys.readouterr().err
    assert "rate limited" in err
