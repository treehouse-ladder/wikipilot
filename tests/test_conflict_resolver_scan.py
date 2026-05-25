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
    status_check_rollup: list[dict] | None = None,
    auto_merge_request: dict | None = None,
) -> dict:
    return {
        "number": number,
        "headRefName": head,
        "baseRefName": "main",
        "mergeStateStatus": state,
        "isCrossRepository": is_cross_repository,
        "author": {"login": author_login},
        "title": title,
        "statusCheckRollup": status_check_rollup or [],
        "autoMergeRequest": auto_merge_request,
    }


def _green_check() -> dict:
    return {"conclusion": "SUCCESS", "state": "SUCCESS"}


def _failing_check(run_id: int = 12345) -> dict:
    return {
        "conclusion": "FAILURE",
        "state": "COMPLETED",
        "name": "ruff + pytest + wikipilot lint",
        "detailsUrl": (
            f"https://github.com/treehouse-ladder/wikipilot/actions/runs/{run_id}/job/9999"
        ),
    }


_BROKEN_WIKILINK_LOG = """\
ruff + pytest + wikipilot lint\tlint\t2026-05-24T09:27:21Z ERROR   broken-wikilink                  wiki/topics/agentic-coding/index.md
ruff + pytest + wikipilot lint\tlint\t2026-05-24T09:27:21Z          [[google-launches-at-io-2026-94069342]] does not resolve
ruff + pytest + wikipilot lint\tlint\t2026-05-24T09:27:21Z Process completed with exit code 1
"""

_PYTEST_FAIL_LOG = """\
============================= test session starts ==============================
FAILED tests/test_thing.py::test_bad - AssertionError: expected 1, got 2
"""


_OWNER_REPO_PAYLOAD = json.dumps({"nameWithOwner": "treehouse-ladder/wikipilot"})
_TRUSTED_API_PAYLOAD = json.dumps({"author_association": "MEMBER"})


_EMPTY_MERGE_QUEUE_PAYLOAD = json.dumps(
    {"data": {"repository": {"mergeQueue": {"entries": {"nodes": []}}}}}
)


def _fake_run(
    *,
    pr_list_payload: str,
    api_payloads: dict[int, str] | None = None,
    run_logs: dict[int, str] | None = None,
    merge_queue_payload: str | None = None,
):
    """Build a ``subprocess.run`` stand-in for the scan's call sequence.

    ``api_payloads`` maps PR number to a ``gh api`` JSON response so a
    single test can mix trusted and untrusted authors across PRs.

    ``run_logs`` maps Actions workflow-run ID to the body that
    ``gh run view <id> --log-failed`` returns. Used by the BLOCKED →
    ``lint_fix`` triage path so the test can assert on classifier output
    without hitting the real GitHub API.

    ``merge_queue_payload`` is the JSON body returned for the GraphQL
    query the scan issues once at start to snapshot the repo's merge
    queue. Defaults to an empty queue — the steady state on most repos.
    Pass a payload whose ``mergeQueue.entries.nodes`` lists PR numbers
    to exercise the "already queued via merge queue" path.
    """
    calls: list[list[str]] = []
    api_payloads = api_payloads or {}
    run_logs = run_logs or {}
    merge_queue_body = merge_queue_payload or _EMPTY_MERGE_QUEUE_PAYLOAD

    def fake_run(args, capture_output=True, text=True, check=False, **kwargs):
        calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            return _ok(pr_list_payload)
        if args[:3] == ["gh", "repo", "view"]:
            return _ok(_OWNER_REPO_PAYLOAD)
        if args[:3] == ["gh", "api", "graphql"]:
            # Snapshot of the repo's merge queue for the base branch.
            return _ok(merge_queue_body)
        if args[:2] == ["gh", "api"]:
            for num, payload in api_payloads.items():
                if f"/pulls/{num}" in args[2]:
                    return _ok(payload)
            return _ok(_TRUSTED_API_PAYLOAD)
        if args[:3] == ["gh", "run", "view"]:
            try:
                run_id = int(args[3])
            except (IndexError, ValueError):
                return _ok("")
            return _ok(run_logs.get(run_id, ""))
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
    assert entry["dispatch_kind"] == "rebase"
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
    assert out[0]["dispatch_kind"] == "rebase"
    assert out[0]["route"] == "wiki_query"


def test_clean_pr_with_pending_ci_is_filtered_out(empty_config: Path, capsys) -> None:
    """A CLEAN PR whose CI hasn't completed yet doesn't need our help —
    GitHub will queue it on its own when the rollup turns green. We only
    intervene when auto-merge was demonstrably skipped."""
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


# ---------------------------------------------------------------------------
# dispatch_kind triage (Phase 11 — three handlers, one scan)
# ---------------------------------------------------------------------------


def test_clean_pr_without_automerge_yields_requeue(empty_config: Path, capsys) -> None:
    """Cause 1 in the original incident: the in-routine ``gh pr merge --auto``
    call was skipped, so a CLEAN PR with green CI is sitting unmerged.
    The scan emits ``dispatch_kind: requeue`` so the orchestrator can
    re-run :func:`apply_static_gate` without an LLM dispatch."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=46,
                head="claude/daily-2026-05-24/agentic-coding",
                state="CLEAN",
                status_check_rollup=[_green_check(), _green_check()],
                auto_merge_request=None,
            )
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 1
    assert out[0]["number"] == 46
    assert out[0]["dispatch_kind"] == "requeue"
    assert out[0]["merge_state_status"] == "CLEAN"


def test_clean_pr_with_automerge_already_set_is_filtered_out(empty_config: Path, capsys) -> None:
    """If GitHub already has ``--auto`` queued, we have nothing to do —
    the merge will land when CI completes. Emitting a requeue entry
    would just no-op against an already-queued PR but cost a scan-output
    line each push."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=47,
                head="claude/daily-2026-05-24/x",
                state="CLEAN",
                status_check_rollup=[_green_check()],
                auto_merge_request={"enabledAt": "2026-05-24T10:00:00Z"},
            )
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_clean_pr_present_in_merge_queue_is_filtered_out(empty_config: Path, capsys) -> None:
    """On repos with the merge_queue ruleset enabled, queued PRs have
    ``autoMergeRequest: null`` even though they ARE queued (and will
    merge on their own). The scan reads the queue snapshot via
    GraphQL and drops PRs whose number it finds there — preventing
    the requeue dispatch from re-queueing a PR that's already
    minutes from merging.

    This closes the over-fire that, on 2026-05-25, would have
    cascaded once the Conflict Resolver routine was changed to fire
    on a cron schedule rather than only on push events."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=57,
                head="claude/daily-2026-05-25/frontier-models",
                state="CLEAN",
                status_check_rollup=[_green_check()],
                auto_merge_request=None,
            )
        ]
    )
    merge_queue_body = json.dumps(
        {
            "data": {
                "repository": {
                    "mergeQueue": {"entries": {"nodes": [{"pullRequest": {"number": 57}}]}}
                }
            }
        }
    )
    fake_run, _ = _fake_run(pr_list_payload=payload, merge_queue_payload=merge_queue_body)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_clean_pr_not_in_merge_queue_still_yields_requeue(empty_config: Path, capsys) -> None:
    """Belt-and-suspenders: a CLEAN+green PR that is NOT in the merge
    queue snapshot still gets the requeue dispatch — that's exactly
    the orphan-CLEAN case the routine exists to fix. The merge-queue
    check filters out queued PRs, it doesn't suppress the dispatch
    for genuinely orphan PRs."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=99,
                head="claude/daily-2026-05-26/x",
                state="CLEAN",
                status_check_rollup=[_green_check()],
                auto_merge_request=None,
            )
        ]
    )
    merge_queue_body = json.dumps(
        {
            "data": {
                "repository": {
                    "mergeQueue": {"entries": {"nodes": [{"pullRequest": {"number": 57}}]}}
                }
            }
        }
    )
    fake_run, _ = _fake_run(pr_list_payload=payload, merge_queue_payload=merge_queue_body)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 1
    assert out[0]["number"] == 99
    assert out[0]["dispatch_kind"] == "requeue"


def test_blocked_pr_with_fixable_lint_yields_lint_fix(empty_config: Path, capsys) -> None:
    """Cause 2 in the original incident: BLOCKED PR with broken-wikilink
    errors. The scan fetches the failing log, classifies it as auto-fixable,
    and emits ``dispatch_kind: lint_fix`` with the categories + excerpt
    so the Opus subagent has everything it needs without a second fetch."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=47,
                head="claude/daily-2026-05-24/ai-in-game-dev",
                state="BLOCKED",
                status_check_rollup=[_failing_check(run_id=998877)],
            )
        ]
    )
    fake_run, _ = _fake_run(
        pr_list_payload=payload,
        run_logs={998877: _BROKEN_WIKILINK_LOG},
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert len(out) == 1
    entry = out[0]
    assert entry["dispatch_kind"] == "lint_fix"
    assert entry["merge_state_status"] == "BLOCKED"
    assert entry["lint_categories"] == ["broken-wikilink"]
    assert "[[google-launches-at-io-2026-94069342]]" in entry["lint_excerpt"]


def test_blocked_pr_with_pytest_failure_is_filtered_out(empty_config: Path, capsys) -> None:
    """Pytest failures are a hard blocker — likely a real code bug, not
    a fixable artifact. The fixer must not touch them; leave for human."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=48,
                head="claude/daily-2026-05-24/x",
                state="BLOCKED",
                status_check_rollup=[_failing_check(run_id=777)],
            )
        ]
    )
    fake_run, _ = _fake_run(
        pr_list_payload=payload,
        run_logs={777: _PYTEST_FAIL_LOG},
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_blocked_pr_without_failing_run_is_filtered_out(empty_config: Path, capsys) -> None:
    """BLOCKED for some non-CI reason (e.g. required review) and no failing
    workflow run — nothing the lint-fixer can grab."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=49,
                head="claude/daily-2026-05-24/x",
                state="BLOCKED",
                status_check_rollup=[_green_check()],
            )
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload)
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_blocked_pr_with_empty_log_is_filtered_out(empty_config: Path, capsys) -> None:
    """If ``gh run view --log-failed`` returns nothing (deleted run, auth
    blip), classify cannot decide — skip until the next push."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=50,
                head="claude/daily-2026-05-24/x",
                state="BLOCKED",
                status_check_rollup=[_failing_check(run_id=555)],
            )
        ]
    )
    fake_run, _ = _fake_run(pr_list_payload=payload, run_logs={555: ""})
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    assert json.loads(capsys.readouterr().out) == []


def test_three_dispatch_kinds_emit_in_order(empty_config: Path, capsys) -> None:
    """End-to-end: a realistic mix where one PR needs rebase, one needs
    requeue, and one needs lint_fix. All three should appear with the
    correct dispatch_kind."""
    cli_main = _import_main()
    payload = json.dumps(
        [
            _pr(
                number=100,
                head="claude/daily-2026-05-24/a",
                state="DIRTY",
            ),
            _pr(
                number=101,
                head="claude/daily-2026-05-24/b",
                state="CLEAN",
                status_check_rollup=[_green_check()],
                auto_merge_request=None,
            ),
            _pr(
                number=102,
                head="claude/daily-2026-05-24/c",
                state="BLOCKED",
                status_check_rollup=[_failing_check(run_id=42)],
            ),
        ]
    )
    fake_run, _ = _fake_run(
        pr_list_payload=payload,
        run_logs={42: _BROKEN_WIKILINK_LOG},
    )
    with patch("subprocess.run", side_effect=fake_run):
        rc = cli_main(["--base", "main", "--config", str(empty_config)])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    kinds = {e["number"]: e["dispatch_kind"] for e in out}
    assert kinds == {100: "rebase", 101: "requeue", 102: "lint_fix"}


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
