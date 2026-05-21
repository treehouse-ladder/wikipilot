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
    author_login: str = "rauriemo",
    is_cross_repository: bool = False,
    head_owner: str = "treehouse-ladder",
) -> str:
    """Render the ``gh pr view --json`` payload the watcher fetches.

    Defaults to a trusted-author shape (org member, head ref in this repo)
    so existing assertions keep firing the enforce path. Tests that want
    to exercise the read_only / untrusted path pass overrides explicitly.
    """
    return json.dumps(
        {
            "headRefName": head,
            "state": state,
            "isDraft": is_draft,
            "labels": [{"name": name} for name in (labels or [])],
            "isCrossRepository": is_cross_repository,
            "author": {"login": author_login},
            "headRepositoryOwner": {"login": head_owner},
        }
    )


def _rest_payload(
    *,
    author_association: str = "MEMBER",
    author_login: str = "rauriemo",
) -> str:
    """Render the ``gh api repos/.../pulls/<n>`` REST payload (subset).

    The watcher only reads ``author_association`` off this response so the
    rest of the upstream REST schema is omitted.
    """
    return json.dumps(
        {
            "user": {"login": author_login},
            "author_association": author_association,
        }
    )


_DEFAULT_OWNER_REPO_PAYLOAD = json.dumps({"nameWithOwner": "treehouse-ladder/wikipilot"})


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
    handlers: dict[str, list[subprocess.CompletedProcess[str]]],
    calls: list[list[str]],
    *,
    api_payload: str | None = None,
    owner_repo_payload: str = _DEFAULT_OWNER_REPO_PAYLOAD,
):
    """Build a ``subprocess.run`` stand-in that pops from a per-prefix queue.

    Match order:

    1. Exact ``args[:3]`` match against ``handlers``.
    2. ``args[:2]`` prefix match against ``handlers`` (so a test can stub
       every ``gh api ...`` call with a single ``"gh api"`` handler).
    3. Trust-guard fallbacks. The watcher always issues ``gh repo view --json
       nameWithOwner`` (for owner/repo resolution) and ``gh api repos/<o>/<r>/pulls/<n>``
       (for ``author_association``) when the head ref matches a claude/*
       template. To avoid duplicating those handlers in every test, the
       helper synthesizes defaults: a fixed ``nameWithOwner`` payload and a
       ``MEMBER`` association unless the test overrides via ``api_payload``.
    4. Final fallback: a generic 0-exit ``CompletedProcess``.
    """
    default_api = api_payload if api_payload is not None else _rest_payload()

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        key3 = " ".join(args[:3])
        queue = handlers.get(key3)
        if queue:
            return queue.pop(0) if len(queue) > 1 else queue[0]
        key2 = " ".join(args[:2])
        queue = handlers.get(key2)
        if queue:
            return queue.pop(0) if len(queue) > 1 else queue[0]
        if args[:3] == ["gh", "repo", "view"]:
            return _ok(stdout=owner_repo_payload)
        if args[:2] == ["gh", "api"]:
            return _ok(stdout=default_api)
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


# ---------------------------------------------------------------------------
# Trust-guard regression suite
# ---------------------------------------------------------------------------
#
# A hostile fork PR (or any non-trusted contributor) can in principle pick a
# claude/daily-… branch name and try to coerce the watcher into queueing
# auto-merge. The guard added in `_is_trusted_for_enforce` must demote every
# such PR to read_only regardless of how the branch name is shaped.
#
# The matrix below covers:
#   - fork PR + claude/* head + MEMBER author     -> read_only (fork beats assoc)
#   - same-repo PR + claude/* + NONE association  -> read_only (untrusted)
#   - same-repo PR + claude/* + MEMBER            -> enforce (control)
#   - same-repo PR + claude/* + NONE in allowlist -> enforce (override)
#   - REST API failure on author_association      -> read_only (fail closed)
#   - human (non-claude) head                     -> read_only (trust check skipped)


def test_fork_pr_with_claude_branch_forces_readonly(repo_with_config: Path, capsys) -> None:
    """A claude/* branch coming from a fork must NOT enable auto-merge.

    The author_association is MEMBER (i.e. the attacker happens to also be
    an org member), so the trust check passes on association alone — the
    ``isCrossRepository`` belt-and-suspenders is what catches this.
    """
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(
                stdout=_meta(
                    head="claude/daily-2026-05-21/agentic-coding",
                    is_cross_repository=True,
                    head_owner="attacker",
                )
            ),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert "fork=True" in out
    assert "read_only" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_untrusted_association_forces_readonly(repo_with_config: Path, capsys) -> None:
    """``author_association == NONE`` on a claude/* head is demoted to read_only.

    The fork bit is false (so an external contributor pushing to a branch
    they somehow have write access to) — the association check alone has
    to catch this case.
    """
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(
                stdout=_meta(
                    head="claude/daily-2026-05-21/x",
                    author_login="random-contributor",
                )
            ),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    fake = _build_fake_run(
        handlers,
        calls,
        api_payload=_rest_payload(author_association="NONE", author_login="random-contributor"),
    )
    with patch("subprocess.run", side_effect=fake):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert "assoc='NONE'" in out
    assert "read_only" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_member_author_with_claude_branch_enforces(repo_with_config: Path, capsys) -> None:
    """Control case: the canonical happy path (MEMBER + same-repo + claude/daily)
    still drives the enforce path and queues auto-merge on green CI."""
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
    assert "mode=enforce" in out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_explicit_trusted_author_allowlist(tmp_path: Path, capsys) -> None:
    """An untrusted association is overridden when the author is in
    ``trusted_authors``. Lets the user whitelist a dedicated bot account
    that has no org membership without granting it collaborator status."""
    config_path = tmp_path / "wikipilot.toml"
    config_path.write_text(
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
        "self_heal_max_attempts = 3\n"
        'trusted_authors = ["wikipilot-bot"]\n',
        encoding="utf-8",
    )
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(
                stdout=_meta(
                    head="claude/daily-2026-05-21/x",
                    author_login="wikipilot-bot",
                )
            ),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    fake = _build_fake_run(
        handlers,
        calls,
        api_payload=_rest_payload(author_association="NONE", author_login="wikipilot-bot"),
    )
    with patch("subprocess.run", side_effect=fake):
        rc = cli_main(["--pr", "42", "--config", str(config_path)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "mode=enforce" in out
    assert "auto-merge enabled" in out
    assert any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_author_association_fetch_failure_fails_closed(repo_with_config: Path, capsys) -> None:
    """If ``gh api`` fails (network blip, missing scope, unauth), the trust
    check must return False — never queue auto-merge on a missing signal."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [_ok(stdout=_meta()), _ok(stdout=_pr_view_payload())],
        "gh pr checks": [_ok()],
        "gh api": [_ok(returncode=1, stderr="HTTP 401")],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert "read_only" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_repo_view_failure_fails_closed(repo_with_config: Path, capsys) -> None:
    """If ``gh repo view`` fails so owner/repo can't be resolved, the trust
    check must still return False (no association = untrusted)."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [_ok(stdout=_meta()), _ok(stdout=_pr_view_payload())],
        "gh pr checks": [_ok()],
        "gh repo view": [_ok(returncode=1, stderr="not a gh repo")],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert not any(c[:3] == ["gh", "pr", "merge"] and "--auto" in c for c in calls)


def test_non_claude_branch_skips_author_check_entirely(repo_with_config: Path, capsys) -> None:
    """For a non-claude head ref the route is already None so the trust
    check is short-circuited — no ``gh api`` call is made (saves one RTT
    on every human PR the watcher sees)."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(head="fix/some-thing", author_login="external-contributor")),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    with patch("subprocess.run", side_effect=_build_fake_run(handlers, calls)):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "read_only" in out
    assert not any(c[:2] == ["gh", "api"] for c in calls)
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)


def test_collaborator_association_is_trusted(repo_with_config: Path, capsys) -> None:
    """COLLABORATOR (external contributor invited via Settings) is in the
    default trust set — first-class support for invited collaborators."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(author_login="invited-friend")),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    fake = _build_fake_run(
        handlers,
        calls,
        api_payload=_rest_payload(author_association="COLLABORATOR", author_login="invited-friend"),
    )
    with patch("subprocess.run", side_effect=fake):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "mode=enforce" in out


def test_contributor_association_is_not_trusted_by_default(repo_with_config: Path, capsys) -> None:
    """``CONTRIBUTOR`` (any previous successful PR) is intentionally NOT in
    the default trusted set — letting it in would mean anyone who's ever
    landed a typo fix could later open a claude/* PR that auto-merges."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(author_login="past-contributor")),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    fake = _build_fake_run(
        handlers,
        calls,
        api_payload=_rest_payload(
            author_association="CONTRIBUTOR", author_login="past-contributor"
        ),
    )
    with patch("subprocess.run", side_effect=fake):
        rc = cli_main(["--pr", "42", "--config", str(repo_with_config)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "not trusted" in out
    assert "read_only" in out


class TestIsTrustedForEnforce:
    """Direct unit tests for the trust helper, independent of the gh layer.

    The end-to-end watcher tests above pin behavior through the CLI; these
    pin the pure-function semantics so refactors of the helper can't drift
    without a test fire.
    """

    @pytest.fixture
    def default_config(self):
        from wikipilot.config import PRWatcherConfig

        return PRWatcherConfig()

    @pytest.fixture
    def authors_only_config(self):
        from wikipilot.config import PRWatcherConfig

        return PRWatcherConfig(
            trusted_associations=(),
            trusted_authors=("wikipilot-bot",),
        )

    @staticmethod
    def _is_trusted(**kwargs):
        from scripts.pr_watcher_gate import _is_trusted_for_enforce

        return _is_trusted_for_enforce(**kwargs)

    def test_fork_pr_is_never_trusted(self, default_config) -> None:
        assert (
            self._is_trusted(
                is_fork=True,
                association="MEMBER",
                author_login="rauriemo",
                config=default_config,
            )
            is False
        )

    def test_fork_pr_with_explicit_allowlist_still_not_trusted(self, authors_only_config) -> None:
        """Even a whitelisted login can't merge from a fork. The
        ``isCrossRepository`` bit is the strongest signal we have that
        the head ref is outside our control."""
        assert (
            self._is_trusted(
                is_fork=True,
                association="NONE",
                author_login="wikipilot-bot",
                config=authors_only_config,
            )
            is False
        )

    def test_member_in_same_repo_is_trusted(self, default_config) -> None:
        assert (
            self._is_trusted(
                is_fork=False,
                association="MEMBER",
                author_login="rauriemo",
                config=default_config,
            )
            is True
        )

    def test_none_association_without_allowlist_match_is_untrusted(self, default_config) -> None:
        assert (
            self._is_trusted(
                is_fork=False,
                association="NONE",
                author_login="stranger",
                config=default_config,
            )
            is False
        )

    def test_explicit_author_allowlist_overrides_untrusted_association(
        self, authors_only_config
    ) -> None:
        assert (
            self._is_trusted(
                is_fork=False,
                association="NONE",
                author_login="wikipilot-bot",
                config=authors_only_config,
            )
            is True
        )

    def test_empty_author_login_does_not_match_empty_allowlist(self, default_config) -> None:
        """The default ``trusted_authors`` is empty; an empty author_login
        must not coincidentally satisfy ``"" in ()``. Both sides being
        falsy can't be allowed to short-circuit to True."""
        assert (
            self._is_trusted(
                is_fork=False,
                association="NONE",
                author_login="",
                config=default_config,
            )
            is False
        )


def test_trust_check_runs_before_ci_wait(repo_with_config: Path, capsys) -> None:
    """Untrusted PRs should still go through the CI wait (read_only mode
    still wants to *report* on CI status), but they must NOT call
    ``gh pr merge`` at any point. This guards against a future refactor
    that swaps the order of operations."""
    cli_main = _import_main()
    calls: list[list[str]] = []
    handlers = {
        "gh pr view": [
            _ok(stdout=_meta(head="claude/daily-2026-05-21/x", author_login="stranger")),
            _ok(stdout=_pr_view_payload()),
        ],
        "gh pr checks": [_ok()],
    }
    fake = _build_fake_run(
        handlers,
        calls,
        api_payload=_rest_payload(author_association="NONE", author_login="stranger"),
    )
    with patch("subprocess.run", side_effect=fake):
        cli_main(["--pr", "42", "--config", str(repo_with_config)])
    # CI wait runs (it's harmless and informative).
    assert any(c[:3] == ["gh", "pr", "checks"] for c in calls)
    # But absolutely no merge mutation.
    assert not any(c[:3] == ["gh", "pr", "merge"] for c in calls)
