"""Preflight checks: fail fast at the top of every routine run.

Verifies the cloud (or local) environment is in a state where the routine
can succeed. Each check returns a :class:`PreflightCheck` with a status and
a human-readable message; the script aggregates and exits non-zero on any
failure.

Run from the routine prompt::

    python scripts/preflight.py

Or from CI::

    python scripts/preflight.py --skip-qmd  # for environments without qmd
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from wikipilot.config import ConfigError, load_topics
from wikipilot.qmd_index import qmd_available

REPO_ROOT_DEFAULT = Path(".")
TOPICS_FILE = "topics.yaml"
WIKI_DIR = "wiki"
TOPICS_SUBDIR = "wiki/topics"


class CheckStatus(StrEnum):
    OK = "ok"
    WARN = "warn"
    FAIL = "fail"


@dataclass(frozen=True)
class PreflightCheck:
    name: str
    status: CheckStatus
    message: str


@dataclass(frozen=True)
class PreflightResult:
    checks: list[PreflightCheck]

    @property
    def ok(self) -> bool:
        return not any(c.status == CheckStatus.FAIL for c in self.checks)

    def render(self) -> str:
        emojis = {CheckStatus.OK: "[OK]", CheckStatus.WARN: "[WARN]", CheckStatus.FAIL: "[FAIL]"}
        lines = [f"{emojis[c.status]:6} {c.name}: {c.message}" for c in self.checks]
        return "\n".join(lines)


def run_preflight(
    *,
    repo_root: Path | None = None,
    skip_qmd: bool = False,
    required_env: Iterable[str] = (),
) -> PreflightResult:
    """Run every preflight check and return aggregated results."""
    repo_root = (repo_root or REPO_ROOT_DEFAULT).resolve()
    checks: list[PreflightCheck] = []
    checks.append(_check_binary("git"))
    checks.append(_check_binary("gh", required=False))
    checks.append(_check_gh_auth())
    checks.append(_check_binary("uv", required=False))
    checks.append(_check_wiki_writable(repo_root / WIKI_DIR))
    checks.append(_check_topics_file(repo_root / TOPICS_FILE, repo_root / TOPICS_SUBDIR))
    if not skip_qmd:
        checks.append(_check_qmd_indexed(repo_root / WIKI_DIR))
    for env_name in required_env:
        checks.append(_check_env_var(env_name))
    return PreflightResult(checks=checks)


def _check_binary(name: str, *, required: bool = True) -> PreflightCheck:
    if shutil.which(name):
        return PreflightCheck(name=f"{name} on PATH", status=CheckStatus.OK, message="found")
    status = CheckStatus.FAIL if required else CheckStatus.WARN
    return PreflightCheck(name=f"{name} on PATH", status=status, message=f"{name!r} not found")


def _check_gh_auth() -> PreflightCheck:
    if not shutil.which("gh"):
        return PreflightCheck(name="gh auth", status=CheckStatus.WARN, message="gh not installed")
    try:
        result = subprocess.run(
            ["gh", "auth", "status"], capture_output=True, text=True, check=False
        )
    except OSError as exc:
        return PreflightCheck(name="gh auth", status=CheckStatus.FAIL, message=str(exc))
    if result.returncode == 0:
        return PreflightCheck(name="gh auth", status=CheckStatus.OK, message="authenticated")
    return PreflightCheck(
        name="gh auth",
        status=CheckStatus.FAIL,
        message="not authenticated (run `gh auth login` or set GITHUB_TOKEN)",
    )


def _check_wiki_writable(wiki_path: Path) -> PreflightCheck:
    if not wiki_path.exists():
        return PreflightCheck(
            name="wiki/ exists", status=CheckStatus.FAIL, message=f"{wiki_path} not found"
        )
    if not wiki_path.is_dir():
        return PreflightCheck(
            name="wiki/ exists", status=CheckStatus.FAIL, message=f"{wiki_path} is not a directory"
        )
    probe = wiki_path / ".preflight-probe"
    try:
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
    except OSError as exc:
        return PreflightCheck(name="wiki/ writable", status=CheckStatus.FAIL, message=str(exc))
    return PreflightCheck(name="wiki/ writable", status=CheckStatus.OK, message=f"{wiki_path}")


def _check_topics_file(topics_path: Path, topics_dir: Path) -> PreflightCheck:
    if not topics_path.exists():
        return PreflightCheck(
            name="topics.yaml", status=CheckStatus.FAIL, message=f"{topics_path} not found"
        )
    try:
        topics = load_topics(topics_path)
    except ConfigError as exc:
        return PreflightCheck(name="topics.yaml", status=CheckStatus.FAIL, message=str(exc))
    missing = [t.id for t in topics if not (topics_dir / t.id / "purpose.md").exists()]
    if missing:
        return PreflightCheck(
            name="topic purpose.md",
            status=CheckStatus.FAIL,
            message=f"missing purpose.md for topics: {missing}",
        )
    return PreflightCheck(
        name="topics.yaml",
        status=CheckStatus.OK,
        message=f"{len(topics)} topic(s); all have purpose.md",
    )


def _check_qmd_indexed(wiki_path: Path) -> PreflightCheck:
    if not qmd_available():
        return PreflightCheck(
            name="qmd indexed",
            status=CheckStatus.FAIL,
            message=("qmd not importable; install with `pip install qmd` (see docs/qmd-setup.md)"),
        )
    qmd_dir = wiki_path.parent / ".qmd"
    if not qmd_dir.exists():
        return PreflightCheck(
            name="qmd indexed",
            status=CheckStatus.WARN,
            message="no .qmd/ index found; run `wikipilot index-wiki` once before first run",
        )
    return PreflightCheck(name="qmd indexed", status=CheckStatus.OK, message=f"{qmd_dir}")


def _check_env_var(name: str) -> PreflightCheck:
    value = os.environ.get(name)
    if value:
        return PreflightCheck(name=f"env: {name}", status=CheckStatus.OK, message="set")
    return PreflightCheck(name=f"env: {name}", status=CheckStatus.FAIL, message="not set")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--skip-qmd", action="store_true", help="Skip the qmd-indexed check.")
    parser.add_argument(
        "--require-env",
        action="append",
        default=[],
        help="Repeatable. Environment variable that must be set.",
    )
    args = parser.parse_args(argv)
    result = run_preflight(
        repo_root=args.repo_root,
        skip_qmd=args.skip_qmd,
        required_env=args.require_env,
    )
    print(result.render())
    return 0 if result.ok else 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
