"""Tests for ``.claude/agents/*.md`` and ``.claude/skills/*/SKILL.md``.

These tests are entirely structural — they don't run any LLM. They verify:

- Every skill manifest parses as YAML and carries the required keys.
- Every agent manifest parses as YAML, declares a model, and references
  only skills that actually exist on disk.
- Per the Phase 2 plan, all 5 agents and all 8 skills are present with the
  documented model assignments (Opus 4.7 for topic-researcher and
  query-answerer, Sonnet for orchestrators and merger/scanner, Haiku for
  linter).
"""

from __future__ import annotations

from pathlib import Path

import frontmatter
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = REPO_ROOT / ".claude" / "agents"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"

EXPECTED_AGENTS: dict[str, str] = {
    "topic-researcher": "claude-opus-4-7",
    "wiki-merger": "claude-sonnet-4-5",
    "wiki-linter": "claude-haiku-4-5",
    "query-answerer": "claude-opus-4-7",
    "wiki-disputes-scanner": "claude-sonnet-4-5",
    "conflict-resolver": "claude-opus-4-7",
    "daily-brief-curator": "claude-opus-4-7",
    "wiki-lint-fixer": "claude-opus-4-7",
}

EXPECTED_SKILLS: tuple[str, ...] = (
    "ingest-source",
    "update-index",
    "lint-wiki",
    "append-log",
    "download-source-images",
    "qmd-search",
    "query-back-fill",
    "disputes-scan",
)


def _load_manifest(path: Path) -> tuple[dict, str]:
    post = frontmatter.load(path)
    return dict(post.metadata), post.content


@pytest.mark.parametrize("skill_name", EXPECTED_SKILLS)
def test_skill_manifest_valid(skill_name: str) -> None:
    path = SKILLS_DIR / skill_name / "SKILL.md"
    assert path.exists(), f"missing skill: {path}"
    metadata, body = _load_manifest(path)
    assert metadata.get("name") == skill_name, (
        f"{path}: 'name' must equal directory name {skill_name!r}; got {metadata.get('name')!r}"
    )
    assert isinstance(metadata.get("description"), str), f"{path}: 'description' must be a string"
    assert metadata["description"].strip(), f"{path}: 'description' must be non-empty"
    assert body.strip().startswith("# "), f"{path}: body must start with a top-level heading"


@pytest.mark.parametrize("agent_name,expected_model", list(EXPECTED_AGENTS.items()))
def test_agent_manifest_valid(agent_name: str, expected_model: str) -> None:
    path = AGENTS_DIR / f"{agent_name}.md"
    assert path.exists(), f"missing agent: {path}"
    metadata, body = _load_manifest(path)
    assert metadata.get("name") == agent_name
    assert isinstance(metadata.get("description"), str) and metadata["description"].strip()
    assert metadata.get("model") == expected_model, (
        f"{path}: model must be {expected_model!r} per the per-agent model selection table; "
        f"got {metadata.get('model')!r}"
    )
    tools = metadata.get("tools")
    assert isinstance(tools, list) and tools, f"{path}: 'tools' must be a non-empty list"
    skills = metadata.get("skills") or []
    assert isinstance(skills, list)
    for skill in skills:
        assert (SKILLS_DIR / skill / "SKILL.md").exists(), (
            f"{path}: declared skill {skill!r} has no manifest at .claude/skills/{skill}/"
        )


def test_no_orphan_agent_or_skill_files() -> None:
    on_disk_agents = {p.stem for p in AGENTS_DIR.glob("*.md")}
    assert on_disk_agents == set(EXPECTED_AGENTS), (
        f"agents on disk {on_disk_agents} do not match expected {set(EXPECTED_AGENTS)}"
    )
    on_disk_skills = {p.parent.name for p in SKILLS_DIR.glob("*/SKILL.md")}
    assert on_disk_skills == set(EXPECTED_SKILLS), (
        f"skills on disk {on_disk_skills} do not match expected {set(EXPECTED_SKILLS)}"
    )


def test_topic_researcher_documents_citation_discipline() -> None:
    path = AGENTS_DIR / "topic-researcher.md"
    body = path.read_text(encoding="utf-8")
    for required_keyword in [
        "purpose.md",
        "Open questions",
        "Disputes",
        "[[source-slug]]",
        "quote",
        "structured proposal",
    ]:
        assert required_keyword in body, (
            f"topic-researcher.md must mention {required_keyword!r} (citation discipline / mandates)"
        )


def test_wiki_merger_documents_cross_page_sweep() -> None:
    path = AGENTS_DIR / "wiki-merger.md"
    body = path.read_text(encoding="utf-8").lower()
    assert "cross-page sweep" in body
    assert "append-only" in body
    assert "human-only" in body


def test_wiki_disputes_scanner_never_resolves() -> None:
    body = (AGENTS_DIR / "wiki-disputes-scanner.md").read_text(encoding="utf-8").lower()
    assert (
        "never auto-resolve" in body
        or "never resolve" in body
        or "do not resolve" in body
        or "never auto-resolves" in body
    )


def test_query_answerer_qmd_first() -> None:
    body = (AGENTS_DIR / "query-answerer.md").read_text(encoding="utf-8").lower()
    assert "qmd-search" in body
    assert body.find("qmd-search") < body.find("websearch") or "qmd-search first" in body


def test_daily_brief_curator_cites_glosses_and_rubric() -> None:
    """The curator MUST mention benchmark_glosses reuse + the rubric prompt
    + the citation-discipline rule, otherwise the editorial top of the
    daily report risks ad-hoc benchmark interpretations the user hasn't
    aligned with."""
    body = (AGENTS_DIR / "daily-brief-curator.md").read_text(encoding="utf-8")
    assert "benchmark_glosses" in body
    assert "cost_glosses" in body
    assert "daily_brief_curator.md" in body
    assert "[[source-slug]]" in body
    # No-bullet-without-citation must be stated explicitly as a hard rule.
    body_lower = body.lower()
    assert (
        "no bullet ships" in body_lower
        or "don't ship a bullet without a citation" in body_lower
        or "no bullets without a citation" in body_lower
    )


def test_daily_brief_curator_rubric_exists() -> None:
    rubric = REPO_ROOT / "prompts" / "daily_brief_curator.md"
    assert rubric.exists()
    body = rubric.read_text(encoding="utf-8").lower()
    # Anchor priorities must reference both lenses.
    assert "best games" in body
    assert "agentic" in body


def test_topic_researcher_documents_entity_field_updates() -> None:
    body = (AGENTS_DIR / "topic-researcher.md").read_text(encoding="utf-8")
    assert "entity_field_updates" in body
    assert "frontier_models" in body
    assert "roster" in body


def test_wiki_merger_applies_entity_field_updates() -> None:
    body = (AGENTS_DIR / "wiki-merger.md").read_text(encoding="utf-8")
    assert "entity_field_updates" in body
    assert "verified_today" in body
