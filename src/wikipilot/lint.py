"""Lint rules for the wiki vault.

Each rule is a free function that takes a ``LintContext`` and returns a list
of ``LintIssue`` objects. The ``Linter`` class composes them and is what the
``wikipilot lint`` CLI subcommand calls.

Rules implemented in Phase 1:

- ``check_frontmatter`` — required keys present and well-typed
- ``check_log_format`` — ``log.md`` headings match the documented schema
- ``check_broken_wikilinks`` — every ``[[link]]`` resolves to a page or alias
- ``check_orphans`` — synthesis pages with no inbound wikilinks
- ``check_staleness`` — pages whose ``last_verified`` is older than
  ``freshness_window_days`` (per-page, falls back to topic default 30)
- ``check_citation_density`` — synthesis pages whose ``## Summary`` has
  paragraphs without any ``[[source-...]]`` link
- ``check_disputes_open_questions_structure`` — sections, when present,
  parse cleanly
- ``check_ownership_violations`` — when ``branch_name`` looks like a
  ``claude/*`` branch, flag any modified human-only paths
- ``check_broken_local_image_links`` (Phase 5) — image refs that point at
  local paths must resolve to a file under ``wiki/assets/`` (otherwise the
  ``download-source-images`` skill probably didn't run)
- ``check_updates_order`` — topic ``## Recent updates`` logs must be
  newest-first (the event log is append-at-top)
- ``check_summary_shrinkage`` — warn when a regenerated topic ``## Summary``
  drops a large fraction of its citations vs the previous git revision
- ``check_tool_profile`` — entity pages with ``profile: tool`` carry every
  profile field with the configured enum values and list shapes (see
  CLAUDE.md "Tool entity profile"); error severity, never auto-fixed
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from wikipilot.config import ToolProfilesConfig, WikipilotConfig
from wikipilot.images import parse_image_refs
from wikipilot.tools import (
    PROFILE_FIELDS,
    PROFILE_LIST_FIELDS,
    PROFILE_LIST_SOURCE_FIELDS,
    PROFILE_SCALAR_SOURCE_FIELDS,
    UNKNOWN,
    is_tool_page,
)
from wikipilot.wiki import (
    Page,
    Vault,
    _coerce_date,
    parse_log_headings,
    slugify,
)
from wikipilot.wikilinks import resolve_wikilink

DEFAULT_FRESHNESS_WINDOW_DAYS = 30

HUMAN_ONLY_PATHS: tuple[str, ...] = (
    "topics.yaml",
    "CLAUDE.md",
    "AGENTS.md",
    "wikipilot.toml",
    "README.md",
    "LICENSE",
    "prompts/",
    ".claude/",
    "docs/",
)
"""Files and directory prefixes that ``claude/*`` branches must not modify.

``wiki/topics/<id>/purpose.md`` is also human-only but is checked separately
because the prefix-only test would over-match on other ``topics/`` content.
"""

LLM_ONLY_PATHS: tuple[str, ...] = (
    "wiki/index.md",
    "wiki/log.md",
    "wiki/sources/",
    "wiki/reports/",
    "wiki/answers/",
    "wiki/decks/",
    "wiki/assets/",
)


SEVERITY_ERROR = "error"
SEVERITY_WARNING = "warning"
SEVERITY_INFO = "info"


@dataclass(frozen=True)
class LintIssue:
    """One finding from a lint rule."""

    severity: str
    code: str
    path: Path
    message: str
    line: int | None = None

    def render(self) -> str:
        loc = f"{self.path}" + (f":{self.line}" if self.line else "")
        return f"{self.severity.upper():7} {self.code:32} {loc}\n         {self.message}"


@dataclass
class LintContext:
    vault: Vault
    pages: list[Page] = field(default_factory=list)
    today: date = field(default_factory=date.today)
    config: WikipilotConfig | None = None
    branch_name: str | None = None
    changed_paths: tuple[str, ...] = ()
    min_citations_per_paragraph: int = 1
    default_freshness_window_days: int = DEFAULT_FRESHNESS_WINDOW_DAYS
    previous_summary_citations: dict[str, int] = field(default_factory=dict)
    """Prior ``## Summary`` citation counts keyed by vault-relative path string.

    Populated best-effort from the previous committed git revision by the
    ``wikipilot lint`` CLI (empty in unit tests and outside a git repo). The
    ``check_summary_shrinkage`` rule consults it to warn when a regenerated
    topic Summary drops a large fraction of its citations vs the prior commit
    — a "did the projection over-prune?" review signal, not data-loss
    detection (the immutable ``## Recent updates`` log is the real backstop).
    """
    summary_shrinkage_threshold: float = 0.4
    """Fractional drop in ``## Summary`` citation count that trips the warning."""

    @classmethod
    def collect(
        cls,
        vault: Vault,
        *,
        today: date | None = None,
        config: WikipilotConfig | None = None,
        branch_name: str | None = None,
        changed_paths: Iterable[str] = (),
    ) -> LintContext:
        pages = [
            Page.read(p)
            for p in sorted(vault.iter_markdown_files())
            if not _is_lint_exempt(p, vault)
        ]
        return cls(
            vault=vault,
            pages=pages,
            today=today or date.today(),
            config=config,
            branch_name=branch_name,
            changed_paths=tuple(changed_paths),
        )

    def synthesis_pages(self) -> list[Page]:
        return [p for p in self.pages if p.kind in {"topic", "concept", "entity", "answer"}]

    def known_slugs(self) -> set[str]:
        slugs: set[str] = set()
        for page in self.pages:
            slugs.add(page.path.stem)
            if page.kind == "topic":
                slugs.add(page.path.parent.name)
            if title := page.title:
                slugs.add(slugify(title))
            for alias in page.aliases:
                slugs.add(alias)
                slugs.add(slugify(alias))
        return slugs


def _is_synthesis_page(page: Page) -> bool:
    """Pages where citation discipline + divergence-discipline lint apply.

    Comparisons are explicitly excluded — they're tables aggregated from
    entity pages, not prose synthesis. Citations live on the entity pages
    and the comparison body is a generated view (see `compare.py`).
    """
    return page.kind in {"topic", "concept", "entity", "answer"}


def _is_purpose_md(path: Path, vault: Vault) -> bool:
    return path.name == "purpose.md" and path.parent.parent == vault.dir_for("topics")


def _is_lint_exempt(path: Path, vault: Vault) -> bool:
    """True if ``path`` is exempt from every schema-enforcing lint rule.

    Exemptions:

    - ``wiki/index.md`` and ``wiki/log.md`` — special files with their own
      structural rules (catalog + journal).
    - ``wiki/topics/<id>/purpose.md`` — human-only topic charter, schema-free.
    - Any ``_*.md`` file anywhere in the vault — personal scratch convention
      (leading-underscore == private). The auto-merge gate also treats these
      as human-only (see :func:`_is_human_only`) so a Claude branch touching
      them blocks the gate.
    """
    if path.name.startswith("_"):
        return True
    if path.parent == vault.root and path.name in {"index.md", "log.md"}:
        return True
    return path.name == "purpose.md" and path.parent.parent == vault.dir_for("topics")


def check_frontmatter(ctx: LintContext) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if _is_purpose_md(page.path, ctx.vault):
            continue
        for error in page.validate_frontmatter():
            issues.append(
                LintIssue(
                    severity=SEVERITY_ERROR,
                    code="frontmatter",
                    path=page.path,
                    message=error,
                )
            )
    return issues


def check_log_format(ctx: LintContext) -> list[LintIssue]:
    issues: list[LintIssue] = []
    log_path = ctx.vault.log_path
    if not log_path.exists():
        return issues
    text = log_path.read_text(encoding="utf-8")
    valid_headings = {match[3] for match in parse_log_headings(text)}
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line.startswith("## "):
            continue
        if line in valid_headings:
            continue
        issues.append(
            LintIssue(
                severity=SEVERITY_ERROR,
                code="log-format",
                path=log_path,
                line=line_no,
                message=(
                    f"log heading {line!r} does not match `## [YYYY-MM-DD] kind | subject` "
                    "(kind in: daily, query, health, manual)"
                ),
            )
        )
    return issues


def check_broken_wikilinks(ctx: LintContext) -> list[LintIssue]:
    known = ctx.known_slugs()
    issues: list[LintIssue] = []
    for page in ctx.pages:
        for link in page.wikilinks():
            if resolve_wikilink(link, known):
                continue
            issues.append(
                LintIssue(
                    severity=SEVERITY_ERROR,
                    code="broken-wikilink",
                    path=page.path,
                    message=f"[[{link}]] does not resolve to a known page slug",
                )
            )
    return issues


def check_orphans(ctx: LintContext) -> list[LintIssue]:
    inbound: dict[str, set[Path]] = {}
    for page in ctx.pages:
        for link in page.wikilinks():
            inbound.setdefault(link, set()).add(page.path)
            inbound.setdefault(slugify(link), set()).add(page.path)
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not _is_synthesis_page(page):
            continue
        slug = page.path.stem
        topic_slug = page.path.parent.name if page.kind == "topic" else None
        if inbound.get(slug) or (topic_slug and inbound.get(topic_slug)):
            continue
        if any(inbound.get(a) or inbound.get(slugify(a)) for a in page.aliases):
            continue
        issues.append(
            LintIssue(
                severity=SEVERITY_WARNING,
                code="orphan-page",
                path=page.path,
                message=f"no other page links to {slug!r}",
            )
        )
    return issues


def check_staleness(ctx: LintContext) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not _is_synthesis_page(page):
            continue
        if page.is_stale(today=ctx.today, default_window=ctx.default_freshness_window_days):
            verified = page.last_verified
            if verified is None:
                detail = "page has never been verified"
            else:
                window = page.freshness_window_days or ctx.default_freshness_window_days
                age = (ctx.today - verified).days
                detail = f"last_verified {verified.isoformat()} is {age}d old (window: {window}d)"
            issues.append(
                LintIssue(
                    severity=SEVERITY_WARNING,
                    code="stale-page",
                    path=page.path,
                    message=detail,
                )
            )
    return issues


_PARAGRAPH_SPLIT_RE = re.compile(r"\n\s*\n")
_SOURCE_LINK_RE = re.compile(r"\[\[(?:source-|[^\]\n]+source[^\]\n]*)?[^\]\n]*\]\]")
_ALL_WIKILINK_RE = re.compile(r"\[\[[^\]\n]+\]\]")


def check_citation_density(ctx: LintContext) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not _is_synthesis_page(page):
            continue
        summary = _extract_section(page.content, "## Summary")
        if summary is None:
            continue
        for paragraph in _PARAGRAPH_SPLIT_RE.split(summary):
            text = paragraph.strip()
            if not text or text.startswith(">") or text.startswith("- "):
                continue
            wikilinks = _ALL_WIKILINK_RE.findall(text)
            if len(wikilinks) < ctx.min_citations_per_paragraph:
                snippet = text.replace("\n", " ")[:80]
                issues.append(
                    LintIssue(
                        severity=SEVERITY_WARNING,
                        code="citation-density",
                        path=page.path,
                        message=(
                            f"## Summary paragraph has fewer than "
                            f"{ctx.min_citations_per_paragraph} [[wikilink]] citations: "
                            f"{snippet!r}"
                        ),
                    )
                )
    return issues


def check_disputes_open_questions_structure(ctx: LintContext) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not _is_synthesis_page(page):
            continue
        if (disputes := _extract_section(page.content, "## Disputes")) is not None:
            for line in disputes.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("_"):
                    continue
                if not stripped.startswith("- "):
                    issues.append(
                        LintIssue(
                            severity=SEVERITY_WARNING,
                            code="disputes-format",
                            path=page.path,
                            message=f"## Disputes entry must start with '- ': {stripped!r}",
                        )
                    )
                    continue
                if "claims" not in stripped or "Status:" not in stripped:
                    issues.append(
                        LintIssue(
                            severity=SEVERITY_WARNING,
                            code="disputes-format",
                            path=page.path,
                            message=(
                                "## Disputes entry must mention 'claims' and 'Status:' "
                                f"per CLAUDE.md: {stripped!r}"
                            ),
                        )
                    )
        if (open_qs := _extract_section(page.content, "## Open questions")) is not None:
            for line in open_qs.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("_"):
                    continue
                if not stripped.startswith("- ["):
                    issues.append(
                        LintIssue(
                            severity=SEVERITY_WARNING,
                            code="open-questions-format",
                            path=page.path,
                            message=(
                                "## Open questions entry must be a checkbox bullet "
                                f"('- [ ] question'): {stripped!r}"
                            ),
                        )
                    )
    return issues


_REMOTE_SCHEMES: tuple[str, ...] = ("http://", "https://", "data:", "mailto:")


def check_broken_local_image_links(ctx: LintContext) -> list[LintIssue]:
    """Flag image refs that point at local paths but resolve to nothing.

    The ``download-source-images`` skill rewrites remote image URLs to
    ``../assets/<slug>/<file>``. A broken local ref means either the asset
    was never downloaded or the source page references a stale name; both
    block auto-merge so the researcher can re-run the skill.
    """
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not page.content:
            continue
        for ref in parse_image_refs(page.content):
            src = ref.src.strip()
            if not src or src.startswith(_REMOTE_SCHEMES):
                continue
            if src.startswith("#"):
                continue
            try:
                resolved = (page.path.parent / src).resolve()
            except OSError:
                continue
            if resolved.exists():
                continue
            issues.append(
                LintIssue(
                    severity=SEVERITY_ERROR,
                    code="broken-image-ref",
                    path=page.path,
                    message=(
                        f"local image {src!r} does not exist (did download-source-images run?)"
                    ),
                )
            )
    return issues


_DIVERGENCE_SENTINEL_RE = re.compile(
    r"_no contradictions or gaps known yet \(last reviewed: \d{4}-\d{2}-\d{2}\)_",
)


def _section_is_only_placeholder(section: str | None) -> bool:
    """Return True when a section is missing or only contains an italic placeholder.

    The Phase 1 lint already accepts ``_(none)_`` / ``_(none yet ...)_`` in
    ``## Disputes`` and ``## Open questions`` as the "nothing here" signal.
    For divergence-discipline we treat any section whose every non-blank
    line either starts with ``_`` (italic placeholder) or is empty as
    "no real content".
    """
    if section is None:
        return True
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("_") and stripped.endswith("_"):
            continue
        return False
    return True


def check_divergence_discipline(ctx: LintContext) -> list[LintIssue]:
    """Warn on synthesis pages with no Disputes, no Open questions, and no sentinel.

    From the Karpathy gist comment thread (localwolfpackai → okkie2): every
    synthesis page should either flag at least one counter-argument / data
    gap, or explicitly state that none were found. Easy to satisfy with a
    one-line sentinel; severity is warning so a fresh page can land
    without blocking auto-merge while reminding the author to think about
    contradictions.
    """
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if not _is_synthesis_page(page):
            continue
        disputes = _extract_section(page.content, "## Disputes")
        open_qs = _extract_section(page.content, "## Open questions")
        if not _section_is_only_placeholder(disputes):
            continue
        if not _section_is_only_placeholder(open_qs):
            continue
        if _DIVERGENCE_SENTINEL_RE.search(page.content):
            continue
        issues.append(
            LintIssue(
                severity=SEVERITY_WARNING,
                code="divergence-discipline",
                path=page.path,
                message=(
                    "synthesis page has no ## Disputes entries, no ## Open questions, "
                    "and no '_no contradictions or gaps known yet (last reviewed: YYYY-MM-DD)_' "
                    "sentinel — add one of the three (see CLAUDE.md 'Divergence check')"
                ),
            )
        )
    return issues


def check_ownership_violations(ctx: LintContext) -> list[LintIssue]:
    if not ctx.branch_name or not ctx.branch_name.startswith("claude/"):
        return []
    issues: list[LintIssue] = []
    for path in ctx.changed_paths:
        normalized = path.replace("\\", "/")
        if _is_human_only(normalized):
            issues.append(
                LintIssue(
                    severity=SEVERITY_ERROR,
                    code="ownership-violation",
                    path=Path(normalized),
                    message=(
                        f"branch {ctx.branch_name!r} modified human-only path "
                        f"{normalized!r}; auto-merge gate must block"
                    ),
                )
            )
    return issues


def _is_human_only(path: str) -> bool:
    if path in HUMAN_ONLY_PATHS:
        return True
    for prefix in HUMAN_ONLY_PATHS:
        if prefix.endswith("/") and path.startswith(prefix):
            return True
    if path.startswith("wiki/topics/") and path.endswith("/purpose.md"):
        return True
    # Personal scratch convention: any ``_*.md`` file anywhere in the vault is
    # human-owned (dashboards, inboxes, hand-written notes). Mirrors the same
    # leading-underscore check in :func:`_is_lint_exempt`.
    last_segment = path.rsplit("/", 1)[-1]
    return path.startswith("wiki/") and path.endswith(".md") and last_segment.startswith("_")


def _extract_section(content: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^{re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        return None
    return match.group(1)


_UPDATES_HEADING_RE = re.compile(r"^### Updates (\d{4}-\d{2}-\d{2})\b", re.MULTILINE)


def check_updates_order(ctx: LintContext) -> list[LintIssue]:
    """Topic ``## Recent updates`` logs must be newest-first (descending dates).

    The log is an immutable, append-at-top event stream (see CLAUDE.md
    "Topic-page summaries are a regenerated view"). The ``wiki-merger`` inserts
    every new ``### Updates YYYY-MM-DD`` block at the top, so a date that is
    older-than the one above it signals the insert went to the wrong place
    (or a hand edit reordered the log). Warning severity: it surfaces the bug
    without hard-blocking auto-merge.
    """
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if page.kind != "topic":
            continue
        section = _extract_section(page.content, "## Recent updates")
        if section is None:
            continue
        dates: list[str] = _UPDATES_HEADING_RE.findall(section)
        for newer, older in zip(dates, dates[1:], strict=False):
            if older > newer:
                issues.append(
                    LintIssue(
                        severity=SEVERITY_WARNING,
                        code="updates-order",
                        path=page.path,
                        message=(
                            f"## Recent updates is not newest-first: "
                            f"'### Updates {older}' appears below '### Updates {newer}' "
                            "(the log is append-at-top; newest entries go on top)"
                        ),
                    )
                )
                break
    return issues


def _count_section_wikilinks(content: str, heading: str) -> int:
    section = _extract_section(content, heading)
    if section is None:
        return 0
    return len(_ALL_WIKILINK_RE.findall(section))


def check_summary_shrinkage(ctx: LintContext) -> list[LintIssue]:
    """Warn when a topic ``## Summary`` drops a large fraction of its citations.

    Topic Summaries are a regenerated view; a full rewrite that prunes too
    aggressively is the one residual risk of the event-sourcing model. The
    immutable log is the lossless backstop, so this is a review signal rather
    than an error: it asks "did the projection over-prune?" Only fires when the
    caller populated ``previous_summary_citations`` (the CLI does this from the
    previous git revision; unit tests inject it directly).
    """
    if not ctx.previous_summary_citations:
        return []
    issues: list[LintIssue] = []
    for page in ctx.pages:
        if page.kind != "topic":
            continue
        rel = str(page.path.relative_to(ctx.vault.root)).replace("\\", "/")
        prior = ctx.previous_summary_citations.get(rel)
        if not prior:  # missing or zero — no baseline to compare against
            continue
        current = _count_section_wikilinks(page.content, "## Summary")
        if current >= prior:
            continue
        drop_fraction = (prior - current) / prior
        if drop_fraction < ctx.summary_shrinkage_threshold:
            continue
        issues.append(
            LintIssue(
                severity=SEVERITY_WARNING,
                code="summary-shrinkage",
                path=page.path,
                message=(
                    f"## Summary citations dropped {prior}->{current} "
                    f"({drop_fraction:.0%} >= {ctx.summary_shrinkage_threshold:.0%}) "
                    "vs the previous revision — confirm the regenerated view didn't "
                    "over-prune still-frontier claims (the ## Recent updates log is the backstop)"
                ),
            )
        )
    return issues


_TOOL_SOURCE_RE = re.compile(r"^\[\[[^\[\]|#\n]+\]\]$")


def _is_source_ref(value: Any) -> bool:
    """True for ``null`` or a single ``[[slug]]`` wikilink string."""
    if value is None:
        return True
    return isinstance(value, str) and bool(_TOOL_SOURCE_RE.match(value.strip()))


def check_tool_profile(ctx: LintContext) -> list[LintIssue]:
    """Entity pages with ``profile: tool`` must carry a complete, well-typed profile.

    Error severity: the profile is the machine-readable surface the user's
    asset-generation benchmark reads (``wikipilot tools`` /
    ``wikipilot tool-changes``), so a missing field or an off-enum value is
    a broken contract, not a style nit. Deliberately NOT auto-fixable — the
    only correct fix for a missing value is a sourced value or the literal
    ``unknown``, and the lint-fixer must never invent either.

    Checks (allowed values from ``wikipilot.toml [tool_profiles]``):

    - every key in :data:`PROFILE_FIELDS` present;
    - ``modality`` in ``modalities``; ``status`` in ``status_values``;
    - ``access`` a non-empty list, each item in ``access_values``;
    - ``tasks`` a non-empty list of strings;
    - ``model_ids`` a list of strings; a ``prefix:`` entry must use a
      configured ``model_id_prefixes`` entry;
    - ``arena_rank`` and ``arena_rank_source`` lists of equal length;
      ``arena_rank_source`` items ``[[wikilink]]`` or ``null``;
    - scalar ``*_source`` siblings ``[[wikilink]]`` or ``null``;
    - ``last_release`` an ISO date or the literal ``unknown``;
    - scalar text fields non-empty (``unknown`` is fine, ``""`` is not).
    """
    cfg: ToolProfilesConfig = (
        ctx.config.tool_profiles if ctx.config is not None else ToolProfilesConfig()
    )
    issues: list[LintIssue] = []

    def problem(page: Page, message: str) -> None:
        issues.append(
            LintIssue(
                severity=SEVERITY_ERROR,
                code="tool-profile",
                path=page.path,
                message=message,
            )
        )

    for page in ctx.pages:
        if not is_tool_page(page):
            continue
        md = page.metadata
        missing = [f for f in PROFILE_FIELDS if f not in md]
        if missing:
            problem(page, f"profile: tool is missing field(s): {missing}")
        # Enums.
        modality = md.get("modality")
        if "modality" in md and modality not in cfg.modalities:
            problem(
                page,
                f"modality {modality!r} not in [tool_profiles].modalities {list(cfg.modalities)}",
            )
        status = md.get("status")
        if "status" in md and status not in cfg.status_values:
            problem(
                page,
                f"status {status!r} not in [tool_profiles].status_values {list(cfg.status_values)}",
            )
        # Lists.
        for list_field in PROFILE_LIST_FIELDS:
            if list_field not in md:
                continue
            value = md[list_field]
            if not isinstance(value, list):
                problem(page, f"{list_field} must be a list (got {type(value).__name__})")
                continue
            if list_field in {"access", "tasks"} and not value:
                problem(page, f"{list_field} must be a non-empty list")
            if any(not isinstance(item, str) or not item.strip() for item in value):
                problem(page, f"{list_field} entries must be non-empty strings")
        access = md.get("access")
        if isinstance(access, list):
            bad = [a for a in access if a not in cfg.access_values]
            if bad:
                problem(
                    page,
                    f"access value(s) {bad} not in [tool_profiles].access_values "
                    f"{list(cfg.access_values)}",
                )
        model_ids = md.get("model_ids")
        if isinstance(model_ids, list):
            for item in model_ids:
                if not isinstance(item, str) or ":" not in item:
                    continue
                prefix = item.split(":", 1)[0]
                if prefix not in cfg.model_id_prefixes:
                    problem(
                        page,
                        f"model_ids entry {item!r} uses unknown prefix {prefix!r} "
                        f"(allowed: {list(cfg.model_id_prefixes)}; vendor ids are unprefixed)",
                    )
        # Sources.
        for src_field in PROFILE_SCALAR_SOURCE_FIELDS:
            if src_field in md and not _is_source_ref(md[src_field]):
                problem(page, f"{src_field} must be a single [[source-slug]] wikilink or null")
        for src_field in PROFILE_LIST_SOURCE_FIELDS:
            if src_field not in md:
                continue
            value = md[src_field]
            if not isinstance(value, list):
                problem(page, f"{src_field} must be a list (got {type(value).__name__})")
                continue
            if any(not _is_source_ref(item) for item in value):
                problem(page, f"{src_field} entries must be [[source-slug]] wikilinks or null")
            base_field = src_field[: -len("_source")]
            base = md.get(base_field)
            if isinstance(base, list) and len(base) != len(value):
                problem(
                    page,
                    f"{src_field} must have the same length as {base_field} "
                    f"({len(value)} vs {len(base)})",
                )
        # Dates / scalars.
        if "last_release" in md:
            lr = md["last_release"]
            if not (lr == UNKNOWN or _coerce_date(lr) is not None):
                problem(page, f"last_release must be an ISO date or 'unknown' (got {lr!r})")
        for text_field in (
            "vendor",
            "open_weights_license",
            "hardware_floor",
            "pricing",
            "commercial_use",
        ):
            if text_field in md:
                value = md[text_field]
                if value is None or (isinstance(value, str) and not value.strip()):
                    problem(
                        page,
                        f"{text_field} must be a non-empty string (write the literal 'unknown' "
                        "when no source states it)",
                    )
    return issues


@dataclass
class Linter:
    """Compose all lint rules and run them against a ``LintContext``."""

    rules: tuple = (
        check_frontmatter,
        check_log_format,
        check_broken_wikilinks,
        check_broken_local_image_links,
        check_orphans,
        check_staleness,
        check_citation_density,
        check_disputes_open_questions_structure,
        check_divergence_discipline,
        check_updates_order,
        check_summary_shrinkage,
        check_tool_profile,
        check_ownership_violations,
    )

    def run(self, ctx: LintContext) -> list[LintIssue]:
        issues: list[LintIssue] = []
        for rule in self.rules:
            issues.extend(rule(ctx))
        issues.sort(key=lambda i: (i.severity != SEVERITY_ERROR, str(i.path), i.code))
        return issues

    @staticmethod
    def has_errors(issues: list[LintIssue]) -> bool:
        return any(i.severity == SEVERITY_ERROR for i in issues)
