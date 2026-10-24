"""Tests for ``wikipilot tool-changes`` (``wikipilot.tool_changes``)."""

from __future__ import annotations

import json
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

import pytest
from click.testing import CliRunner

from tests.test_tools import SOURCE_SLUG, write_tool_entity
from wikipilot.cli import main
from wikipilot.config import ToolProfilesConfig
from wikipilot.tool_changes import (
    EMPTY_MESSAGE,
    compute_tool_changes,
    render_json,
    render_markdown,
    resolve_baseline_rev,
)
from wikipilot.wiki import Page, Vault, WikiError

BASE = "1111111111111111111111111111111111111111"
HEAD = "2222222222222222222222222222222222222222"


class FakeGit:
    """Minimal ``git`` stand-in keyed on the subcommand.

    ``baseline`` maps ``entities/<slug>.md`` → file text as it was at BASE.
    """

    def __init__(self, baseline: dict[str, str] | None = None, *, fail_rev_parse: bool = False):
        self.baseline = baseline or {}
        self.fail_rev_parse = fail_rev_parse
        self.calls: list[list[str]] = []

    def __call__(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        self.calls.append(args)
        sub = args[3]  # ["git", "-C", root, <sub>, ...]
        if sub == "rev-parse":
            if self.fail_rev_parse:
                return _cp(128, "", "fatal: bad revision")
            if "--verify" in args:
                return _cp(0, BASE + "\n")
            return _cp(0, HEAD + "\n")
        if sub == "rev-list":
            return _cp(0, BASE + "\n")
        if sub == "ls-tree":
            names = [f"wiki/{k}" for k in self.baseline]
            return _cp(0, "\n".join(names) + ("\n" if names else ""))
        if sub == "show":
            spec = args[4]
            rel = spec.split(":", 1)[1].removeprefix("wiki/")
            if rel in self.baseline:
                return _cp(0, self.baseline[rel])
            return _cp(128, "", "fatal: path does not exist")
        return _cp(1, "", f"unexpected {sub}")


def _cp(code: int, out: str, err: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(args=[], returncode=code, stdout=out, stderr=err)


@pytest.fixture
def git_vault(sample_vault: Vault) -> Vault:
    """Sample vault with a fake ``.git`` marker so repo-root discovery works."""
    (sample_vault.root.parent / ".git").mkdir()
    return sample_vault


def _snapshot(vault: Vault, slug: str) -> str:
    return (vault.dir_for("entities") / f"{slug}.md").read_text(encoding="utf-8")


def _set(vault: Vault, slug: str, **fields: Any) -> None:
    path = vault.dir_for("entities") / f"{slug}.md"
    page = Page.read(path)
    page.metadata.update(fields)
    page.write()


class TestCompute:
    def test_no_changes(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault)
        git = FakeGit({"entities/meshy.md": _snapshot(git_vault, "meshy")})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert report.is_empty
        assert report.baseline_rev == BASE and report.head_rev == HEAD
        assert render_markdown(report).splitlines()[2] == EMPTY_MESSAGE

    def test_scalar_change_carries_source_and_url(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault)
        before = _snapshot(git_vault, "meshy")
        _set(
            git_vault,
            "meshy",
            pricing="$0.20/generation (2026-06-01)",
            pricing_source=f"[[{SOURCE_SLUG}]]",
            last_verified=date(2026, 6, 1),
        )
        git = FakeGit({"entities/meshy.md": before})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert len(report.changes) == 1
        change = report.changes[0]
        assert change.entity == "meshy" and change.field == "pricing"
        assert change.old == "unknown" and change.new == "$0.20/generation (2026-06-01)"
        assert change.source_slug == SOURCE_SLUG
        expected_url = Page.read(git_vault.dir_for("sources") / f"{SOURCE_SLUG}.md").metadata["url"]
        assert change.source_url == expected_url
        assert change.last_verified == "2026-06-01"
        md = render_markdown(report)
        assert (
            "- [[meshy]] `pricing`: `unknown` → `$0.20/generation (2026-06-01)` [[example-paper-aabbccdd]]"
            in md
        )

    def test_list_change_compared_as_list(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault)
        before = _snapshot(git_vault, "meshy")
        _set(
            git_vault,
            "meshy",
            arena_rank=["AA Image-to-3D: #1 (2026-05-01)", "arena.ai image-to-3d: #2 (2026-06-01)"],
            arena_rank_source=[f"[[{SOURCE_SLUG}]]", f"[[{SOURCE_SLUG}]]"],
        )
        git = FakeGit({"entities/meshy.md": before})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert [c.field for c in report.changes] == ["arena_rank"]
        assert report.changes[0].old == ["AA Image-to-3D: #1 (2026-05-01)"]
        assert len(report.changes[0].new) == 2
        assert report.changes[0].source_slug == SOURCE_SLUG

    def test_untracked_field_change_ignored(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault)
        before = _snapshot(git_vault, "meshy")
        _set(git_vault, "meshy", vendor="Meshy Inc.", hardware_floor="24 GB VRAM")
        git = FakeGit({"entities/meshy.md": before})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert report.is_empty

    def test_new_tool_reported_with_full_profile(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault, slug="tripo")
        git = FakeGit({})  # nothing at baseline
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert report.changes == []
        assert [t["slug"] for t in report.new_tools] == ["tripo"]
        assert report.new_tools[0]["access"] == ["api", "fal"]
        assert "**New tool** [[tripo]] (3d; access: api, fal; status: active)" in render_markdown(
            report
        )

    def test_removed_tool_reported(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault, slug="gone")
        before = _snapshot(git_vault, "gone")
        (git_vault.dir_for("entities") / "gone.md").unlink()
        git = FakeGit({"entities/gone.md": before})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert report.removed_tools == ["gone"]
        assert "**Removed tool** `gone`" in render_markdown(report)

    def test_entity_that_gained_profile_counts_as_new(self, git_vault: Vault) -> None:
        # At baseline the page existed but had no `profile: tool`.
        write_tool_entity(git_vault)
        plain = _snapshot(git_vault, "meshy").replace("profile: tool\n", "")
        git = FakeGit({"entities/meshy.md": plain})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        assert [t["slug"] for t in report.new_tools] == ["meshy"]

    def test_json_contract(self, git_vault: Vault) -> None:
        write_tool_entity(git_vault)
        before = _snapshot(git_vault, "meshy")
        _set(git_vault, "meshy", status="deprecated", status_source=f"[[{SOURCE_SLUG}]]")
        git = FakeGit({"entities/meshy.md": before})
        report = compute_tool_changes(
            git_vault, ToolProfilesConfig(), baseline_rev=BASE, git_runner=git
        )
        payload = json.loads(render_json(report))
        assert set(payload) == {
            "schema_version",
            "baseline_rev",
            "head_rev",
            "changes",
            "new_tools",
            "removed_tools",
        }
        assert payload["schema_version"] == 1
        assert set(payload["changes"][0]) == {
            "entity",
            "field",
            "old",
            "new",
            "source_slug",
            "source_url",
            "last_verified",
        }


class TestResolveBaseline:
    def test_requires_exactly_one_selector(self, git_vault: Vault) -> None:
        with pytest.raises(WikiError, match="exactly one"):
            resolve_baseline_rev(git_vault, git_runner=FakeGit())
        with pytest.raises(WikiError, match="exactly one"):
            resolve_baseline_rev(
                git_vault, since=date(2026, 1, 1), since_rev="abc", git_runner=FakeGit()
            )

    def test_since_rev_verified(self, git_vault: Vault) -> None:
        git = FakeGit()
        assert resolve_baseline_rev(git_vault, since_rev="abc", git_runner=git) == BASE
        assert any("--verify" in c for c in git.calls)

    def test_since_rev_unresolvable(self, git_vault: Vault) -> None:
        with pytest.raises(WikiError, match="does not resolve"):
            resolve_baseline_rev(
                git_vault, since_rev="nope", git_runner=FakeGit(fail_rev_parse=True)
            )

    def test_since_date_uses_rev_list_end_of_day(self, git_vault: Vault) -> None:
        git = FakeGit()
        assert resolve_baseline_rev(git_vault, since=date(2026, 10, 1), git_runner=git) == BASE
        rev_list = next(c for c in git.calls if c[3] == "rev-list")
        assert "--before=2026-10-01T23:59:59" in rev_list

    def test_outside_git_repo(self, sample_vault: Vault) -> None:
        with pytest.raises(WikiError, match="not inside a git repository"):
            resolve_baseline_rev(sample_vault, since_rev="abc", git_runner=FakeGit())


class TestCli:
    def test_requires_selector(self, sample_vault: Vault) -> None:
        result = CliRunner().invoke(main, ["tool-changes", "--vault", str(sample_vault.root)])
        assert result.exit_code == 2
        assert "exactly one" in result.output

    def test_real_git_smoke(self, tmp_path: Path) -> None:
        """End-to-end against a real throwaway repo: baseline commit → edit → diff."""
        import shutil

        repo = tmp_path / "repo"
        shutil.copytree(Path(__file__).parent / "fixtures" / "sample_vault", repo / "wiki")
        vault = Vault.at(repo / "wiki")
        write_tool_entity(vault)
        env = {
            "GIT_AUTHOR_NAME": "t",
            "GIT_AUTHOR_EMAIL": "t@t",
            "GIT_COMMITTER_NAME": "t",
            "GIT_COMMITTER_EMAIL": "t@t",
        }

        def git(*args: str) -> str:
            import os

            res = subprocess.run(
                ["git", "-C", str(repo), *args],
                capture_output=True,
                text=True,
                check=True,
                env={**os.environ, **env},
            )
            return res.stdout.strip()

        git("init", "-q")
        git("add", "-A")
        git("commit", "-q", "-m", "baseline")
        base_sha = git("rev-parse", "HEAD")
        _set(vault, "meshy", status="preview", status_source=f"[[{SOURCE_SLUG}]]")
        git("add", "-A")
        git("commit", "-q", "-m", "change")

        result = CliRunner().invoke(
            main,
            [
                "tool-changes",
                "--since-rev",
                base_sha,
                "--format",
                "json",
                "--vault",
                str(vault.root),
            ],
        )
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["baseline_rev"] == base_sha
        assert payload["changes"][0]["field"] == "status"
        assert payload["changes"][0]["old"] == "active"
        assert payload["changes"][0]["new"] == "preview"
