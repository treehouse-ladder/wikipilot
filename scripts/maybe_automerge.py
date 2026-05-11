"""Apply the per-route auto-merge gate to one PR.

Invoked once per PR by the routine orchestrator (after ``gh pr create``).
Reads thresholds from ``wikipilot.toml``, fetches the PR via ``gh pr view
--json``, and either:

  - enables ``gh pr merge --squash --auto`` if every gate criterion passes,
  - posts a structured review checklist as a PR comment otherwise.

Usage::

    python scripts/maybe_automerge.py --pr 42 --route daily_research

Routes: ``daily_research`` | ``wiki_query`` | ``weekly_health``.

The actual gate logic lives in ``wikipilot.git_ops.evaluate_gate`` /
``apply_gate`` so it stays unit-testable. This script is the thin CLI shim.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from wikipilot.config import load_wikipilot_config
from wikipilot.git_ops import VALID_ROUTES, apply_gate

DEFAULT_CONFIG_PATH = Path("wikipilot.toml")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", type=int, required=True, help="PR number to gate.")
    parser.add_argument(
        "--route",
        type=str,
        required=True,
        choices=sorted(VALID_ROUTES),
        help="Which routine produced this PR (selects the gate thresholds).",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to wikipilot.toml (default: ./wikipilot.toml).",
    )
    args = parser.parse_args(argv)

    config = load_wikipilot_config(args.config)
    decision = apply_gate(args.pr, route=args.route, config=config)
    if decision.automerge:
        print(f"PR #{args.pr}: gate passed; auto-merge enabled.")
        return 0
    print(f"PR #{args.pr}: gate did NOT pass. Review checklist posted as PR comment.")
    for reason in decision.reasons:
        print(f"  - {reason}")
    if decision.blocked_paths:
        print("  Human-only paths modified:")
        for p in decision.blocked_paths:
            print(f"    - {p}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
