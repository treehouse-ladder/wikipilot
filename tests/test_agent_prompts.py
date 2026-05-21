"""Agent-prompt invariants enforced from Python.

These tests assert small textual / YAML-frontmatter properties on the
markdown files in ``.claude/agents/`` that the rest of the system depends
on but cannot enforce statically. The most important one: the
``wiki-merger`` agent MUST NOT declare ``append-log`` or ``update-index``
in its skills frontmatter, and its body MUST forbid writing
``wiki/log.md`` and ``wiki/index.md``. If either contract is broken, the
Daily Research routine's parallel-merge correctness is gone — every
topic PR will once again append to the same line range of those two
shared files, and the merge queue will dequeue all but one PR per run.
See ``CLAUDE.md`` "Daily run workflow" and ``prompts/daily_runner.md``
for the full design rationale.
"""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO_ROOT / ".claude" / "agents"


def _frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} missing YAML frontmatter"
    _, fm, _ = text.split("---\n", 2)
    parsed = yaml.safe_load(fm)
    assert isinstance(parsed, dict), f"{path} frontmatter must be a YAML mapping"
    return parsed


def _body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} missing YAML frontmatter"
    _, _, body = text.split("---\n", 2)
    return body


class TestWikiMergerInvariants:
    """Enforced contract on `.claude/agents/wiki-merger.md`."""

    AGENT_PATH = AGENTS_DIR / "wiki-merger.md"

    def test_agent_file_exists(self) -> None:
        assert self.AGENT_PATH.exists(), (
            "wiki-merger agent prompt must exist at .claude/agents/wiki-merger.md"
        )

    def test_does_not_declare_append_log_skill(self) -> None:
        fm = _frontmatter(self.AGENT_PATH)
        skills = set(fm.get("skills") or [])
        assert "append-log" not in skills, (
            "wiki-merger MUST NOT declare the append-log skill — "
            "wiki/log.md is written exclusively by the daily report PR. "
            "Re-adding this skill brings back the parallel-topic-PR conflict "
            "cascade. See CLAUDE.md 'Daily run workflow'."
        )

    def test_does_not_declare_update_index_skill(self) -> None:
        fm = _frontmatter(self.AGENT_PATH)
        skills = set(fm.get("skills") or [])
        assert "update-index" not in skills, (
            "wiki-merger MUST NOT declare the update-index skill — "
            "wiki/index.md is written exclusively by the daily report PR. "
            "Re-adding this skill brings back the parallel-topic-PR conflict "
            "cascade. See CLAUDE.md 'Daily run workflow'."
        )

    def test_body_explicitly_forbids_log_and_index_writes(self) -> None:
        body = _body(self.AGENT_PATH)
        assert "wiki/log.md" in body, (
            "wiki-merger.md must explicitly mention wiki/log.md in its Don'ts "
            "so the contract is discoverable from inside the prompt"
        )
        assert "wiki/index.md" in body, (
            "wiki-merger.md must explicitly mention wiki/index.md in its Don'ts "
            "so the contract is discoverable from inside the prompt"
        )

    def test_still_declares_ingest_source_skill(self) -> None:
        """Sanity check: the refactor removed two skills but kept ingest-source.
        Source pages still live on per-topic branches (one page per source
        URL), and only the ingest-source skill writes them.
        """
        fm = _frontmatter(self.AGENT_PATH)
        skills = set(fm.get("skills") or [])
        assert "ingest-source" in skills, (
            "wiki-merger must still declare the ingest-source skill — "
            "topic PRs write source pages, just not log.md/index.md"
        )
