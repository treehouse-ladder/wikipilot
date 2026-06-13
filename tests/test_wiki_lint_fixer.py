"""Tests for ``.claude/agents/wiki-lint-fixer.md`` + the rewrite logic it drives.

Two layers:

- **Prompt invariants** (text-only): the agent's frontmatter pins the model
  + tools the orchestrator dispatches against, and the body explicitly
  names the allowlist + hard-block list so the contract is discoverable
  from inside the prompt.
- **Golden rewrite tests** (Python): end-to-end exercises of the broken-
  wikilink repair path the agent calls through (``autofix_wikilink`` plus
  ``resolve_or_fix_in_files``) on synthetic vault fixtures that reproduce
  the exact failure shape from PR #47. These complement the unit tests in
  ``tests/test_wikilinks.py``; the focus here is on the realistic end-to-
  end shape (a source page with a SHA suffix that the prose mistyped).
"""

from __future__ import annotations

from pathlib import Path

import yaml

from wikipilot.wiki import Vault
from wikipilot.wikilinks import (
    autofix_wikilink,
    resolve_or_fix_in_files,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENT_PATH = REPO_ROOT / ".claude" / "agents" / "wiki-lint-fixer.md"


def _frontmatter() -> dict[str, object]:
    text = AGENT_PATH.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{AGENT_PATH} missing YAML frontmatter"
    _, fm, _ = text.split("---\n", 2)
    parsed = yaml.safe_load(fm)
    assert isinstance(parsed, dict)
    return parsed


def _body() -> str:
    text = AGENT_PATH.read_text(encoding="utf-8")
    _, _, body = text.split("---\n", 2)
    return body


# ---------------------------------------------------------------------------
# Prompt invariants
# ---------------------------------------------------------------------------


class TestPromptInvariants:
    def test_agent_file_exists(self) -> None:
        assert AGENT_PATH.exists(), (
            "wiki-lint-fixer agent prompt must exist at .claude/agents/wiki-lint-fixer.md"
        )

    def test_uses_opus_model(self) -> None:
        # Auto-fix is judgment-heavy (resolve broken-wikilink targets
        # correctly, not just delete them) — the per-agent model table in
        # CLAUDE.md pins this agent to Opus 4.8. A regression to a smaller
        # model here would tank fix quality.
        fm = _frontmatter()
        assert fm.get("model") == "claude-opus-4-8", (
            f"wiki-lint-fixer must run on Opus 4.8; got {fm.get('model')!r}"
        )

    def test_declares_required_tools(self) -> None:
        fm = _frontmatter()
        tools = set(fm.get("tools") or [])
        assert {"Read", "Grep", "Edit", "Bash"}.issubset(tools), (
            "wiki-lint-fixer needs Read/Grep/Edit/Bash to read the failing PR, "
            "rewrite files, and force-push"
        )

    def test_allowlist_documented_in_body(self) -> None:
        body = _body()
        for category in (
            "broken-wikilink",
            "broken-image-ref",
            "frontmatter",
            "log-format",
        ):
            assert category in body, (
                f"wiki-lint-fixer body must document the {category!r} auto-fix policy explicitly"
            )

    def test_hard_block_documented_in_body(self) -> None:
        body = _body()
        for blocker in ("ownership-violation", "pytest"):
            assert blocker in body, f"wiki-lint-fixer body must document the {blocker!r} hard-block"

    def test_uses_shared_wikilinks_library(self) -> None:
        # The whole point of Layer 6's shared library is that all three
        # call sites (lint, merger pre-commit, lint-fixer) use one
        # resolution table. If a future edit replaces the autofix_wikilink
        # call with an inline glob, the lint and the fixer would diverge
        # again — which is exactly the bug the shared library exists to
        # prevent.
        body = _body()
        assert "wikipilot.wikilinks" in body or "autofix_wikilink" in body, (
            "wiki-lint-fixer body must reference the shared "
            "wikipilot.wikilinks helper rather than re-implementing the glob"
        )

    def test_requeues_via_apply_static_gate(self) -> None:
        # Centralized trust check + auto-merge queue. Bypassing this would
        # let the fixer push past the trust gate — the same boundary the
        # rest of the system relies on.
        body = _body()
        assert "maybe_automerge.py" in body, (
            "wiki-lint-fixer must re-queue auto-merge via "
            "scripts/maybe_automerge.py (which calls apply_static_gate)"
        )

    def test_uses_force_with_lease_not_force(self) -> None:
        body = _body()
        assert "--force-with-lease" in body, (
            "wiki-lint-fixer must force-push with --force-with-lease so "
            "concurrent operator pushes win"
        )


# ---------------------------------------------------------------------------
# Golden rewrite tests (exercise the library the agent calls into)
# ---------------------------------------------------------------------------


class TestBrokenWikilinkRewrite:
    """End-to-end rewrite scenarios mirrored from real CI failures.

    These are deliberately layered above ``tests/test_wikilinks.py``:
    those tests pin the unit behavior of the helpers; these pin the
    realistic shape of the failures the agent is dispatched against
    (broken slug embedded in synthesis-page prose, source page already
    exists at the canonical slug, agent rewrites in place).
    """

    def test_pr47_style_repair(self, sample_vault: Vault) -> None:
        """PR #47 reproduction.

        Source page lives at ``sources/google-launches-...-at-i-o-2026-94069342.md``
        (slugify turns ``I/O`` into ``i-o``); the topic-researcher's prose
        wrote ``[[google-launches-...-at-io-2026-94069342]]`` instead. The
        SHA suffix is unique → the autofix can find the canonical slug
        unambiguously and the rewrite lands.
        """
        canonical_slug = "google-launches-antigravity-2-0-at-i-o-2026-94069342"
        broken_slug = "google-launches-antigravity-2-0-at-io-2026-94069342"
        source_path = sample_vault.dir_for("sources") / f"{canonical_slug}.md"
        source_path.write_text(
            "---\n"
            'title: "Google launches Antigravity 2.0 at I/O 2026"\n'
            "kind: source\n"
            "url: https://example.com/google-io-2026\n"
            "sha256: 94069342deadbeef\n"
            "fetched_at: 2026-05-24\n"
            "topic: frontier-models\n"
            "image_count: 0\n"
            "sources: []\n"
            "last_updated: 2026-05-24\n"
            "last_verified: 2026-05-24\n"
            "freshness_window_days: 365\n"
            "---\n"
            "\n## Excerpts\n\n> Quote.\n",
            encoding="utf-8",
        )
        topic_path = sample_vault.dir_for("topics") / "ai-agents" / "index.md"
        text = topic_path.read_text(encoding="utf-8")
        topic_path.write_text(
            text + f"\nGoogle's announcement [[{broken_slug}]] is notable.\n",
            encoding="utf-8",
        )

        report = resolve_or_fix_in_files([topic_path], sample_vault)
        rewritten = topic_path.read_text(encoding="utf-8")

        assert len(report.autofixed) == 1
        _, old, new = report.autofixed[0]
        assert old == broken_slug
        assert new == canonical_slug
        assert f"[[{canonical_slug}]]" in rewritten
        assert f"[[{broken_slug}]]" not in rewritten
        assert report.unresolved == []

    def test_zero_candidate_targets_left_for_human(self, sample_vault: Vault) -> None:
        """A target that doesn't match any existing page or SHA must NOT
        be silently rewritten. The agent's hard-block contract: if the
        autofix can't find an unambiguous match, leave the PR alone."""
        topic_path = sample_vault.dir_for("topics") / "ai-agents" / "index.md"
        topic_path.write_text(
            topic_path.read_text(encoding="utf-8")
            + "\nThis source [[completely-hallucinated-7f8a9b0c]] never existed.\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files([topic_path], sample_vault)
        assert report.autofixed == []
        assert any(slug == "completely-hallucinated-7f8a9b0c" for _, slug in report.unresolved)

    def test_ambiguous_sha_match_leaves_link_alone(self, sample_vault: Vault) -> None:
        """If two source pages share the same SHA suffix (extremely rare
        but possible when SHA truncation collides), the rewrite is unsafe.
        The agent must report unresolved rather than guessing."""
        sources = sample_vault.dir_for("sources")
        for name in ("first-source-deadbeef.md", "second-source-deadbeef.md"):
            (sources / name).write_text(
                "---\n"
                f"title: {name}\n"
                "kind: source\n"
                "url: https://example.com/" + name + "\n"
                "sha256: deadbeef\n"
                "fetched_at: 2026-05-24\n"
                "topic: ai-agents\n"
                "image_count: 0\n"
                "sources: []\n"
                "last_updated: 2026-05-24\n"
                "last_verified: 2026-05-24\n"
                "freshness_window_days: 365\n"
                "---\n\n## Excerpts\n\n> x\n",
                encoding="utf-8",
            )
        # Direct autofix call — no rewrite should happen because the
        # heuristic correctly returns None for ambiguous SHA matches.
        assert autofix_wikilink("typo-source-deadbeef", sample_vault) is None

    def test_section_anchor_and_alias_preserved(self, sample_vault: Vault) -> None:
        """A real-world prose citation often uses ``[[slug#heading|display]]``.
        The rewrite must preserve both the section anchor and the alias so
        the page still renders identically post-fix."""
        canonical = "preserve-anchors-paper-12345678"
        (sample_vault.dir_for("sources") / f"{canonical}.md").write_text(
            "---\n"
            'title: "Preserve anchors paper"\n'
            "kind: source\n"
            "url: https://example.com/preserve\n"
            "sha256: 12345678\n"
            "fetched_at: 2026-05-24\n"
            "topic: ai-agents\n"
            "image_count: 0\n"
            "sources: []\n"
            "last_updated: 2026-05-24\n"
            "last_verified: 2026-05-24\n"
            "freshness_window_days: 365\n"
            "---\n\n## Excerpts\n\n> x\n",
            encoding="utf-8",
        )
        topic_path = sample_vault.dir_for("topics") / "ai-agents" / "index.md"
        topic_path.write_text(
            topic_path.read_text(encoding="utf-8")
            + "\nSee [[preserve-anchors-papre-12345678#method|the method section]].\n",
            encoding="utf-8",
        )
        report = resolve_or_fix_in_files([topic_path], sample_vault)
        rewritten = topic_path.read_text(encoding="utf-8")
        assert len(report.autofixed) == 1
        assert f"[[{canonical}#method|the method section]]" in rewritten
