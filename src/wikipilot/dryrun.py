"""Dry-run dispatcher: simulate proposal/answer flows without calling Anthropic.

The cloud routine produces a structured ``Proposal`` (research) or ``Answer``
(query) which the wiki-merger / query-answerer agents apply to the vault.
This module ships:

- The :class:`Proposal` and :class:`Answer` dataclasses (matching the JSON
  schemas documented in ``CLAUDE.md``).
- Fake-data generators (``make_fake_proposal``, ``make_fake_answer``) that
  produce realistic payloads — citations, a contradiction, an open question,
  one image source — so dry-run exercises the same code paths a live run
  hits.
- Apply functions (``apply_proposal``, ``apply_answer``) that perform the
  source ingest, page writes, cross-page sweep, log append, and back-fill.

The ``wikipilot dry-run`` CLI subcommand wires this up. Tests in
``tests/test_dryrun.py`` round-trip both flows against the sample vault.

This module is the *Python embodiment of the agent flow*, not a replacement
for the agents — at runtime the wiki-merger uses Read/Edit tools driven by
Claude, but it calls the same skills (``ingest-source``, ``update-index``,
``append-log``) which in turn shell out to ``wikipilot`` subcommands or
import these helpers.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from wikipilot.config import TopicConfig
from wikipilot.lint import LintContext, Linter
from wikipilot.log import (
    HealthReport,
    RunReport,
    append_log_entry,
    write_health_report,
    write_run_report,
)
from wikipilot.sources import write_source
from wikipilot.wiki import Page, Vault, slugify


@dataclass
class PageDiff:
    """One page touched by a proposal."""

    path: str
    kind: str  # "topic" | "concept" | "entity" | "answer"
    update_entry: str  # dated `### Updates` log block (topic pages) / synthesis prose (others)
    new_disputes: list[str] = field(default_factory=list)
    new_open_questions: list[str] = field(default_factory=list)


@dataclass
class ProposalSource:
    url: str
    title: str
    excerpt: str
    image_urls: list[str] = field(default_factory=list)
    also_relevant_to: list[str] = field(default_factory=list)
    """Other topic ids this source is also highly relevant to (Phase 9 cross-topic flag).

    Empty by default. The topic-researcher agent populates this when a source
    spans the topic being researched and at least one other configured topic
    (per the cross-cutting relevance criteria in CLAUDE.md). Phase 9 only
    *records* the flag — a future routine iteration can wire routing logic on
    top of it. Apply paths ignore the field; the source page is still written
    once under the researched topic.
    """


@dataclass
class Proposal:
    """The structured payload a `topic-researcher` returns to the orchestrator.

    Mirrors the JSON schema in CLAUDE.md "Proposal schema". Keeping it as a
    dataclass (not raw dict) means the merger and the dry-run share a typed
    contract; the JSON shape is what the agent outputs in a fenced block.
    """

    topic_id: str
    sources: list[ProposalSource]
    page_diffs: list[PageDiff]
    new_disputes: list[str] = field(default_factory=list)
    new_open_questions: list[str] = field(default_factory=list)
    summary_affecting: bool = False
    """Whether this run changes the topic's current-state picture.

    When True, the daily orchestrator dispatches the ``topic-summarizer`` to
    regenerate the topic page's ``## Summary`` view from the (now-updated)
    ``## Recent updates`` log + entity frontmatter. When False, the dated log
    entry is still applied but the Summary is left untouched (no rewrite = no
    drift). See CLAUDE.md "Topic-page summaries are a regenerated view".
    """
    summary_guidance: str = ""
    """What shifted that the summarizer must reflect (empty when not affecting)."""


@dataclass
class Answer:
    """The structured payload `query-answerer` returns for the Wiki Query routine."""

    question: str
    answer_slug: str  # YYYY-MM-DD-<slug>
    summary: str  # markdown body of the answer (with [[wikilinks]] + > quotes)
    sources: list[ProposalSource]
    related_pages: list[str] = field(default_factory=list)  # for back-fill
    issue_url: str | None = None
    run_id: str = ""


@dataclass
class ApplyResult:
    """Side-effects of applying a proposal/answer."""

    pages_touched: list[Path] = field(default_factory=list)
    sources_added: list[Path] = field(default_factory=list)
    log_entries: list[str] = field(default_factory=list)
    report_path: Path | None = None


def make_fake_proposal(topic: TopicConfig, *, today: date | None = None) -> Proposal:
    """Synthesize a realistic proposal for ``topic`` (used by ``dry-run --topic``).

    Includes: two cited claims sharing one source, one contradiction (to
    exercise Disputes append-only), one open question, and one image URL on
    the source (to exercise the image-download skill).
    """
    today = today or date.today()
    src = ProposalSource(
        url=f"https://example.com/{topic.id}/dryrun-paper",
        title=f"Dry-run paper for {topic.display_name}",
        excerpt=(
            "Dry-run papers introduce dry-run-techniques for testing autonomous research "
            "pipelines without spending tokens on real LLM calls."
        ),
        image_urls=[f"https://example.com/{topic.id}/figure-1.png"],
    )
    src_slug = _expected_source_slug(src)
    concept_slug = f"{topic.id}-dryrun-concept"
    diffs = [
        PageDiff(
            path=f"topics/{topic.id}/index.md",
            kind="topic",
            update_entry=(
                f"A dry-run paper [[{src_slug}]] introduces a dry-run technique for testing "
                "research pipelines."
            ),
            new_open_questions=["Do dry-run techniques cover the cross-page sweep correctly?"],
        ),
        PageDiff(
            path=f"concepts/{concept_slug}.md",
            kind="concept",
            update_entry=(
                f"Dry-run concept refers to a synthesized payload [[{src_slug}]] used to "
                "exercise the apply path end-to-end without an Anthropic call."
            ),
            new_disputes=[
                f"[[{src_slug}]] claims dry-run techniques are sufficient; "
                "[[example-paper-aabbccdd]] claims live integration is still required. "
                "Status: unresolved"
            ],
        ),
    ]
    return Proposal(
        topic_id=topic.id,
        sources=[src],
        page_diffs=diffs,
        new_disputes=diffs[1].new_disputes,
        new_open_questions=diffs[0].new_open_questions,
        summary_affecting=True,
        summary_guidance=(
            "Dry-run technique introduced; exercise the gated summarizer dispatch path."
        ),
    )


def make_fake_answer(question: str, *, today: date | None = None) -> Answer:
    """Synthesize a realistic answer for the ``dry-run --query`` flow."""
    today = today or date.today()
    answer_slug = f"{today.isoformat()}-{slugify(question)[:40].rstrip('-')}"
    src = ProposalSource(
        url=f"https://example.com/answers/{slugify(question)[:30]}",
        title=f"Reference for: {question}",
        excerpt=(
            "Answer references introduce evidence supporting the synthesized response. "
            "They are required by the citation discipline."
        ),
    )
    src_slug = _expected_source_slug(src)
    summary = (
        f"## Summary\n\n"
        f"The dry-run answer to {question!r} is: a synthesized response with at least one "
        f"citation [[{src_slug}]] and one supporting quote.\n\n"
        f"> {src.excerpt}\n\n"
        f"## See also\n\n"
        f"- [[transformer-attention]]\n"
    )
    return Answer(
        question=question,
        answer_slug=answer_slug,
        summary=summary,
        sources=[src],
        related_pages=["transformer-attention"],
        run_id=f"dryrun-{today.isoformat()}",
    )


def apply_proposal_topic_only(
    vault: Vault,
    proposal: Proposal,
    *,
    today: date | None = None,
) -> ApplyResult:
    """Apply only the topic-scoped writes: source ingest, page diffs, cross-sweep.

    Mirrors what the ``wiki-merger`` agent does on a per-topic branch in the
    Daily Research routine. **Does not write** to ``wiki/log.md``,
    ``wiki/index.md``, or ``wiki/reports/``. Those three files are batched
    on the daily report PR by :func:`apply_daily_aggregate`, after every
    per-topic PR has merged into ``main``. This split is what makes per-topic
    PRs file-disjoint and therefore parallel-mergeable through the queue —
    see ``CLAUDE.md`` "Daily run workflow".
    """
    today = today or date.today()
    result = ApplyResult()

    for src in proposal.sources:
        record = write_source(
            vault,
            url=src.url,
            title=src.title,
            topic=proposal.topic_id,
            body=src.excerpt,
            today=today,
            image_count=len(src.image_urls),
            excerpts=[src.excerpt],
        )
        if record.created:
            result.sources_added.append(record.page.path)
        result.pages_touched.append(record.page.path)

    for diff in proposal.page_diffs:
        target = vault.root / diff.path
        page = _ensure_page(vault, target, diff)
        if diff.kind == "topic":
            # Topic pages are event-sourced: the dated entry is inserted at the
            # TOP of the immutable ## Recent updates log. The ## Summary view is
            # regenerated separately by the topic-summarizer (an Anthropic-driven
            # agent), so it is intentionally NOT touched here — mirroring the
            # wiki-merger contract. See CLAUDE.md "Topic-page summaries...".
            _prepend_recent_update(page, diff.update_entry, today=today)
        else:
            _append_summary(page, diff.update_entry)
        for entry in diff.new_disputes:
            _append_section_bullet(page, "## Disputes", entry)
        for entry in diff.new_open_questions:
            _append_section_bullet(page, "## Open questions", f"[ ] {entry}")
        page.bump_freshness(verified=True, today=today)
        page.write()
        result.pages_touched.append(target)

    swept = _cross_page_sweep(vault, proposal, today=today)
    result.pages_touched.extend(swept)
    return result


def apply_daily_aggregate(
    vault: Vault,
    proposals: list[Proposal],
    *,
    pr_links: list[str] | None = None,
    notes: str | None = None,
    include_summary: bool = True,
    today: date | None = None,
) -> ApplyResult:
    """Batched aggregate writes for a Daily Research run.

    Writes one ``## [DATE] daily | <topic-id> ...`` log entry per proposal,
    updates ``wiki/index.md`` with every new source/page across all
    proposals, appends the run-summary log entry (when ``include_summary``
    is True), and writes the per-run report at ``wiki/reports/YYYY-MM-DD.md``.
    Idempotent on the index path (``_update_index`` is append-only). Empty
    ``proposals`` is allowed and is a no-op except that no report is written.

    Mirrors what the daily orchestrator does on the
    ``claude/daily-<DATE>/_report`` branch after every per-topic PR has
    merged. This is the ONLY place ``wiki/log.md`` and ``wiki/index.md`` are
    written during a Daily Research run. The single-topic dryrun CLI
    (:func:`apply_proposal`) sets ``include_summary=False`` because for
    one proposal the per-topic line already serves as the summary; in the
    multi-topic production flow the summary line is what backs the
    "<N> topics, <S> sources, <P> pages" entry in ``wiki/log.md``.
    """
    today = today or date.today()
    result = ApplyResult()

    if not proposals:
        return result

    all_source_relpaths: list[str] = []
    all_page_relpaths: list[str] = []
    all_disputes: list[str] = []
    all_open_questions: list[str] = []
    topic_ids: list[str] = []

    for proposal in proposals:
        # The page count in the per-topic log entry is approximate: counted
        # from the proposal payload (sources + page_diffs) rather than from
        # the filesystem, because in production this function runs on the
        # report branch which doesn't see the topic branches' work. The
        # exact pages_touched figure is captured in the run report instead.
        n_sources = len(proposal.sources)
        n_pages = n_sources + len(proposal.page_diffs)
        summary_line = f"{proposal.topic_id} — {n_sources} sources, {n_pages} pages"
        append_log_entry(
            vault,
            kind="daily",
            subject=summary_line,
            summary=f"Daily research applied for topic {proposal.topic_id}.",
            today=today,
        )
        result.log_entries.append(summary_line)

        _update_index(vault, proposal, today=today)

        topic_ids.append(proposal.topic_id)
        for src in proposal.sources:
            slug = _expected_source_slug(src)
            all_source_relpaths.append(f"sources/{slug}.md")
        for diff in proposal.page_diffs:
            all_page_relpaths.append(diff.path)
        all_disputes.extend(proposal.new_disputes)
        all_open_questions.extend(proposal.new_open_questions)

    result.pages_touched.append(vault.index_path)

    if include_summary:
        summary_subject = (
            f"{len(proposals)} topics, "
            f"{sum(len(p.sources) for p in proposals)} sources, "
            f"{len(set(all_page_relpaths) | set(all_source_relpaths))} pages"
        )
        append_log_entry(
            vault,
            kind="daily",
            subject=summary_subject,
            summary=f"Daily research run complete: {len(proposals)} topics aggregated.",
            today=today,
        )
        result.log_entries.append(summary_subject)

    report = RunReport(
        routine="daily_research",
        run_date=today,
        run_id=f"dryrun-daily-{today.isoformat()}",
        topics_processed=topic_ids,
        sources_added=sorted(set(all_source_relpaths)),
        pages_touched=sorted(set(all_page_relpaths) | set(all_source_relpaths)),
        runtime_seconds=None,
        token_usage={},
        pr_links=list(pr_links) if pr_links else [],
        new_disputes=all_disputes,
        new_open_questions=all_open_questions,
        notes=notes or "Generated by `apply_daily_aggregate`; no Anthropic call was made.",
    )
    result.report_path = write_run_report(vault, report)
    return result


def apply_proposal(
    vault: Vault,
    proposal: Proposal,
    *,
    today: date | None = None,
) -> ApplyResult:
    """Single-topic dryrun helper: runs the topic-only and aggregate phases as one unit.

    Used by ``wikipilot dry-run --topic`` (one-shot, no parallelism). In the
    real Daily Research routine the two phases live on different branches —
    see :func:`apply_proposal_topic_only` and :func:`apply_daily_aggregate`.
    """
    today = today or date.today()
    topic_result = apply_proposal_topic_only(vault, proposal, today=today)
    aggregate_result = apply_daily_aggregate(vault, [proposal], include_summary=False, today=today)

    merged = ApplyResult()
    merged.pages_touched = list(topic_result.pages_touched) + list(aggregate_result.pages_touched)
    merged.sources_added = list(topic_result.sources_added)
    merged.log_entries = list(aggregate_result.log_entries)
    merged.report_path = aggregate_result.report_path
    return merged


@dataclass
class WeeklyHealth:
    """Stand-in for the LLM-judge sweep output in dry-run mode."""

    candidate_sets: list[dict[str, object]]
    disputes_filed: list[dict[str, object]]


def make_fake_weekly_health(
    candidate_sets: list[dict[str, object]],
    *,
    today: date | None = None,
) -> WeeklyHealth:
    """Synthesize a fake disputes-scanner result for ``candidate_sets``.

    For each candidate set with ≥ 2 pages, file one synthetic dispute on the
    first page citing the second. Used by ``wikipilot dry-run --weekly-health``
    to exercise apply_weekly_health without an Anthropic call.
    """
    today = today or date.today()
    disputes_filed: list[dict[str, object]] = []
    for cset in candidate_sets:
        pages = list(cset.get("pages", []))  # type: ignore[arg-type]
        if len(pages) < 2:
            continue
        primary, neighbor = pages[0], pages[1]
        disputes_filed.append(
            {
                "page": primary,
                "neighbor": neighbor,
                "trigger": cset.get("trigger", "unknown"),
                "summary": (
                    f"dry-run dispute filed by {cset.get('trigger', 'unknown')!r} "
                    f"on {primary} (neighbor {neighbor})"
                ),
                "confidence": "low",
            }
        )
    return WeeklyHealth(candidate_sets=candidate_sets, disputes_filed=disputes_filed)


def apply_weekly_health(
    vault: Vault,
    weekly: WeeklyHealth,
    *,
    today: date | None = None,
) -> ApplyResult:
    """Apply weekly-health dispute proposals to the vault.

    Mirrors what the disputes-scanner agent does at runtime: append-only
    bullets to ``## Disputes`` (creating the section if absent), bump
    ``last_updated`` (NOT ``last_verified``), then write the health report
    and append the log entry.
    """
    today = today or date.today()
    result = ApplyResult()

    for entry in weekly.disputes_filed:
        page_rel = str(entry["page"])
        page_path = vault.root / page_rel
        if not page_path.exists():
            continue
        page = Page.read(page_path)
        bullet = (
            f"{entry.get('summary', 'dry-run dispute')} "
            f"Status: unresolved (confidence: {entry.get('confidence', 'low')}; "
            f"sweep: {today.isoformat()})"
        )
        _append_section_bullet(page, "## Disputes", bullet)
        page.bump_freshness(verified=False, today=today)
        page.write()
        result.pages_touched.append(page_path)

    ctx = LintContext.collect(vault, today=today)
    issues = Linter().run(ctx)
    stale_pages = sorted(
        {str(i.path.relative_to(vault.root)) for i in issues if i.code == "stale-page"}
    )
    citation_failures = sorted(
        {str(i.path.relative_to(vault.root)) for i in issues if i.code == "citation-density"}
    )
    orphans = sorted(
        {str(i.path.relative_to(vault.root)) for i in issues if i.code == "orphan-page"}
    )
    broken_links = sorted(
        {str(i.path.relative_to(vault.root)) for i in issues if i.code == "broken-wikilink"}
    )
    new_disputes = [
        f"[[{Path(str(d['page'])).stem}]]: {d.get('summary', '')}" for d in weekly.disputes_filed
    ]

    report = HealthReport(
        run_date=today,
        run_id=f"dryrun-health-{today.isoformat()}",
        stale_pages=stale_pages,
        citation_density_failures=citation_failures,
        new_disputes=new_disputes,
        orphan_pages=orphans,
        broken_wikilinks=broken_links,
        runtime_seconds=None,
        token_usage={},
        notes="Generated by `wikipilot dry-run --weekly-health`; no Anthropic call was made.",
    )
    result.report_path = write_health_report(vault, report)
    result.pages_touched.append(result.report_path)

    append_log_entry(
        vault,
        kind="health",
        subject=f"weekly sweep — {len(weekly.disputes_filed)} disputes filed",
        summary=f"Dry-run weekly health sweep across {len(weekly.candidate_sets)} candidate set(s).",
        today=today,
    )
    result.log_entries.append(f"weekly sweep ({len(weekly.disputes_filed)} disputes filed)")
    return result


def apply_answer(
    vault: Vault,
    answer: Answer,
    *,
    today: date | None = None,
) -> ApplyResult:
    """Apply an answer: write the answer page, ingest sources, back-fill, log."""
    today = today or date.today()
    result = ApplyResult()

    for src in answer.sources:
        record = write_source(
            vault,
            url=src.url,
            title=src.title,
            topic="answers",
            body=src.excerpt,
            today=today,
            image_count=len(src.image_urls),
            excerpts=[src.excerpt],
        )
        if record.created:
            result.sources_added.append(record.page.path)
        result.pages_touched.append(record.page.path)

    answer_path = vault.dir_for("answers") / f"{answer.answer_slug}.md"
    metadata: dict[str, object] = {
        "title": answer.question,
        "kind": "answer",
        "question": answer.question,
        "issue_url": answer.issue_url,
        "run_id": answer.run_id or f"dryrun-{today.isoformat()}",
        "sources": [f"[[{_expected_source_slug(src)}]]" for src in answer.sources],
        "last_updated": today,
        "last_verified": today,
        "freshness_window_days": 90,
    }
    if metadata["issue_url"] is None:
        del metadata["issue_url"]
    answer_page = Page.from_dict(answer_path, metadata, answer.summary)
    answer_page.write()
    result.pages_touched.append(answer_path)

    backfilled = _back_fill_answer(vault, answer, today=today)
    result.pages_touched.extend(backfilled)

    append_log_entry(
        vault,
        kind="query",
        subject=f"{answer.question} — answers/{answer.answer_slug}.md",
        summary=f"Dry-run answer for: {answer.question}",
        today=today,
    )
    result.log_entries.append(answer.question)
    return result


def _ensure_page(vault: Vault, path: Path, diff: PageDiff) -> Page:
    if path.exists():
        return Page.read(path)
    today = date.today()
    metadata: dict[str, object] = {
        "title": _title_from_path(path),
        "kind": diff.kind,
        "sources": [],
        "last_updated": today,
        "last_verified": today,
        "freshness_window_days": 30,
    }
    body = f"# {metadata['title']}\n\n## Summary\n\n_(seeded by dry-run)_\n"
    page = Page.from_dict(path, metadata, body)
    page.write()
    return page


def _title_from_path(path: Path) -> str:
    if path.name == "index.md":
        return path.parent.name.replace("-", " ").title()
    return path.stem.replace("-", " ").title()


def _append_summary(page: Page, addition: str) -> None:
    if not addition:
        return
    if "## Summary" not in page.content:
        page.content = page.content.rstrip() + f"\n\n## Summary\n\n{addition}\n"
        return
    parts = re.split(r"(^## )", page.content, flags=re.MULTILINE)
    new_parts: list[str] = []
    in_summary = False
    for part in parts:
        if part == "## ":
            in_summary = False
            new_parts.append(part)
            continue
        if in_summary:
            new_parts.append(part.rstrip() + f"\n\n{addition}\n\n")
            in_summary = False
            continue
        if part.startswith("Summary"):
            in_summary = True
        new_parts.append(part)
    page.content = "".join(new_parts)


def _prepend_recent_update(page: Page, entry: str, *, today: date) -> None:
    """Insert a dated `### Updates <today>` block at the TOP of `## Recent updates`.

    Newest-first and immutable: existing `### Updates` entries are preserved
    verbatim; the new block is placed immediately under the `## Recent updates`
    heading. Creates the section (after `## Summary` if present, else at the end)
    when it doesn't yet exist. Mirrors the wiki-merger's append-at-top contract.
    """
    if not entry:
        return
    block = f"### Updates {today.isoformat()}\n\n{entry.rstrip()}\n"
    heading = "## Recent updates"
    if heading not in page.content:
        insertion = f"\n\n{heading}\n\n{block}"
        summary = re.compile(r"(^## Summary\s*\n)(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
        match = summary.search(page.content)
        if match:
            cut = match.end(2)
            page.content = page.content[:cut].rstrip() + insertion + page.content[cut:]
        else:
            page.content = page.content.rstrip() + insertion
        return
    pattern = re.compile(rf"(^{re.escape(heading)}\s*\n)(\s*)", re.MULTILINE)
    match = pattern.search(page.content)
    insert_at = match.end(1)
    page.content = page.content[:insert_at] + f"\n{block}\n" + page.content[insert_at:]


def _append_section_bullet(page: Page, heading: str, bullet_text: str) -> None:
    """Append a `- bullet` to ``heading``; create the section if it doesn't exist.

    Append-only: existing bullets are preserved verbatim. Idempotent: if the
    same bullet text already exists, no-op.
    """
    bullet = f"- {bullet_text}"
    section_pattern = re.compile(
        rf"(^{re.escape(heading)}\s*\n)(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = section_pattern.search(page.content)
    if not match:
        page.content = page.content.rstrip() + f"\n\n{heading}\n\n{bullet}\n"
        return
    existing = match.group(2)
    if bullet in existing:
        return
    new_section_body = existing.rstrip() + f"\n{bullet}\n"
    page.content = page.content[: match.start(2)] + new_section_body + page.content[match.end(2) :]


def _cross_page_sweep(vault: Vault, proposal: Proposal, *, today: date) -> list[Path]:
    """For each page diff, find pages backlinking the touched slug and bump them.

    Returns the paths that were updated (freshness-bumped). Idempotent —
    running twice updates ``last_updated`` only.

    Does NOT touch ``wiki/index.md`` or ``wiki/log.md``. Index updates are
    batched on the daily report PR via :func:`apply_daily_aggregate`; log
    appends are written there too. Per-topic merger writes to those two
    files would re-introduce the parallel-merge conflict cascade documented
    in ``CLAUDE.md`` "Daily run workflow".
    """
    swept: list[Path] = []
    touched_slugs = set()
    for diff in proposal.page_diffs:
        if diff.kind == "topic":
            touched_slugs.add(Path(diff.path).parent.name)
        else:
            touched_slugs.add(Path(diff.path).stem)

    for path in sorted(vault.iter_markdown_files()):
        if path.name in {"index.md", "log.md"}:
            continue
        relative = path.relative_to(vault.root)
        if any(relative.match(d.path) for d in proposal.page_diffs):
            continue
        page = Page.read(path)
        if not any(slug in page.wikilinks() for slug in touched_slugs):
            continue
        page.bump_freshness(verified=False, today=today)
        page.write()
        swept.append(path)

    return swept


def _update_index(vault: Vault, proposal: Proposal, *, today: date) -> None:
    """Make sure new sources/pages appear in ``wiki/index.md``.

    Append-only; idempotent.
    """
    index_path = vault.index_path
    text = (
        index_path.read_text(encoding="utf-8")
        if index_path.exists()
        else "# Index\n\n## Sources\n\n## Concepts\n\n"
    )
    for src in proposal.sources:
        slug = _expected_source_slug(src)
        line = f"- [[{slug}]]"
        if line in text:
            continue
        text = _append_under_heading(text, "## Sources", line)
    for diff in proposal.page_diffs:
        slug = Path(diff.path).stem if diff.kind != "topic" else Path(diff.path).parent.name
        heading = {
            "topic": "## Topics",
            "concept": "## Concepts",
            "entity": "## Entities",
            "answer": "## Answers",
        }.get(diff.kind, "## Concepts")
        line = f"- [[{slug}]]"
        if line in text:
            continue
        text = _append_under_heading(text, heading, line)
    index_path.write_text(text, encoding="utf-8")


def _append_under_heading(text: str, heading: str, line: str) -> str:
    pattern = re.compile(rf"(^{re.escape(heading)}\s*\n)(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    if not match:
        return text.rstrip() + f"\n\n{heading}\n\n{line}\n"
    existing = match.group(2).rstrip()
    placeholder = "_(none yet"
    if placeholder in existing:
        cleaned_lines = [ln for ln in existing.splitlines() if placeholder not in ln]
        existing = "\n".join(cleaned_lines).strip()
    new_body = (existing + f"\n{line}\n").lstrip("\n")
    if not new_body.endswith("\n"):
        new_body += "\n"
    return text[: match.start(2)] + new_body + text[match.end(2) :]


def _back_fill_answer(vault: Vault, answer: Answer, *, today: date) -> list[Path]:
    """Add an `[[answer-slug]]` reference to each related concept/entity page."""
    backfilled: list[Path] = []
    for related_slug in answer.related_pages:
        candidate_paths = [
            vault.dir_for("concepts") / f"{related_slug}.md",
            vault.dir_for("entities") / f"{related_slug}.md",
        ]
        for path in candidate_paths:
            if not path.exists():
                continue
            page = Page.read(path)
            _append_section_bullet(page, "## See also", f"[[{answer.answer_slug}]]")
            page.bump_freshness(verified=False, today=today)
            page.write()
            backfilled.append(path)
            break
    return backfilled


def _expected_source_slug(src: ProposalSource) -> str:
    """Compute the slug ``write_source`` will assign without writing."""
    from wikipilot.sources import source_slug

    return source_slug(src.url, title=src.title)
