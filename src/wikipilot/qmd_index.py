"""Wrapper around the qmd CLI for incremental indexing of the wiki.

qmd is the local hybrid BM25+vector search tool we expose as an MCP connector
to subagents (see ``docs/qmd-setup.md`` and ``docs/routines-setup.md``). This
module just shells out to the binary; it does not require qmd to be
installed at import time so unit tests can mock it freely.

Phase 1 ships the subprocess wrapper plus a graceful "qmd not installed"
fallback. Phase 4 wires it into ``preflight.py`` so a routine fails fast if
qmd is missing on the cloud env.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


class QmdError(RuntimeError):
    """Raised on qmd subprocess failure."""


@dataclass(frozen=True)
class IndexResult:
    ok: bool
    qmd_available: bool
    indexed_files: int
    message: str


def qmd_available() -> bool:
    """Return ``True`` iff a ``qmd`` executable is on ``PATH``."""
    return shutil.which("qmd") is not None


def index_vault(
    vault_root: Path,
    *,
    full: bool = False,
    runner: callable = subprocess.run,
) -> IndexResult:
    """Run ``qmd index`` against ``vault_root`` and return a structured result.

    ``runner`` is injectable so tests can swap in a fake without touching
    subprocess. The default ``subprocess.run`` shells out to the real qmd
    binary if present.
    """
    if not qmd_available():
        return IndexResult(
            ok=False,
            qmd_available=False,
            indexed_files=0,
            message=(
                "qmd not found on PATH. Install with `pip install qmd` and "
                "re-run; see docs/qmd-setup.md for the local-dev setup."
            ),
        )
    args = ["qmd", "index", str(vault_root)]
    if full:
        args.append("--full")
    try:
        result = runner(args, capture_output=True, text=True, check=False)
    except OSError as exc:
        raise QmdError(f"failed to launch qmd: {exc}") from exc
    if result.returncode != 0:
        return IndexResult(
            ok=False,
            qmd_available=True,
            indexed_files=0,
            message=f"qmd exited {result.returncode}: {result.stderr.strip() or result.stdout.strip()}",
        )
    indexed = _parse_indexed_count(result.stdout)
    return IndexResult(
        ok=True,
        qmd_available=True,
        indexed_files=indexed,
        message=result.stdout.strip() or "ok",
    )


def _parse_indexed_count(stdout: str) -> int:
    """Extract a file-count from qmd's stdout, or 0 if the format is unknown."""
    for token in stdout.split():
        if token.isdigit():
            return int(token)
    return 0
