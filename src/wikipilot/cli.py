"""Wikipilot command-line interface.

Phase 0 ships only the ``wikipilot`` entry point and a ``--version`` flag so the
package is installable and importable. Subcommands (``lint``, ``init-vault``,
``validate-topics``, ``freshness-report``, ``deck``, ``index-wiki``,
``research``, ``query``) land in Phase 1.
"""

from __future__ import annotations

import click

from wikipilot import __version__


@click.group(help="Wikipilot: autonomous-research wiki maintained by Claude Code Cloud Routines.")
@click.version_option(__version__, prog_name="wikipilot")
def main() -> None:
    """Top-level entry point."""


if __name__ == "__main__":
    main()
