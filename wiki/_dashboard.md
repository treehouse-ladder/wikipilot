# Wiki Dashboard

> [!info] Personal dashboard
> This file is `wiki/_dashboard.md`. The leading underscore marks it as personal scratch — exempt from the lint, exempt from the agents' cross-page sweep, and human-only for the auto-merge gate. Edit freely; the routines will never touch it. See `CLAUDE.md` "Personal scratch convention".

> [!tip] How to use this page
> - Bookmark it (right-click in the tab → **Bookmark**) so it's one keystroke away.
> - Optionally pin it as your default "Open" target: Settings → Files & Links → Default location for new notes → keep your habit of opening this file first.
> - Press **`Ctrl/Cmd-P`** → "**Dataview: Force refresh**" if a query looks stale.
> - Every block below is a live query. Edit the source of this file to add your own.

---

## Topics at a glance

```dataview
TABLE WITHOUT ID
  Topic,
  length(rows) AS "Sources",
  max(rows.fetched_at) AS "Most recent source"
FROM "sources"
WHERE topic
GROUP BY topic AS Topic
SORT Topic ASC
```

```dataview
TABLE WITHOUT ID
  file.link AS "Topic page",
  last_updated AS "Last updated",
  last_verified AS "Last verified",
  length(file.outlinks) AS "Outlinks"
FROM "topics"
WHERE kind = "topic"
SORT last_updated DESC
```

---

## Recently added sources (last 7 days)

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  topic AS "Topic",
  fetched_at AS "Fetched"
FROM "sources"
WHERE date(today) - date(fetched_at) <= dur(7 days)
SORT fetched_at DESC
LIMIT 25
```

---

## Recently touched synthesis pages (last 7 days)

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  kind AS "Kind",
  last_updated AS "Updated"
FROM "concepts" OR "entities" OR "topics" OR "answers" OR "comparisons"
WHERE date(today) - date(last_updated) <= dur(7 days)
SORT last_updated DESC
LIMIT 25
```

---

## Pages needing re-verification

Pages whose `last_verified` is older than their `freshness_window_days`. Open the page, re-confirm the claims still hold, bump `last_verified` to today.

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  kind AS "Kind",
  last_verified AS "Last verified",
  (date(today) - date(last_verified)).days AS "Days old",
  freshness_window_days AS "Window"
FROM "concepts" OR "entities" OR "topics" OR "answers"
WHERE last_verified
  AND (date(today) - date(last_verified)).days > (freshness_window_days OR 30)
SORT (date(today) - date(last_verified)).days DESC
LIMIT 20
```

---

## All open questions

Every `## Open questions` checkbox across the wiki, grouped by source page. Resolve a question by editing the bullet into a real claim (with a `[[source]]` citation) on the host page — don't tick the checkbox without sourcing it.

```dataview
TASK
FROM "concepts" OR "entities" OR "topics" OR "answers"
WHERE !completed
GROUP BY file.link
SORT file.path ASC
```

---

## Unresolved disputes

Pages with a `## Disputes` section. Click in, read the bullets, and resolve any `Status: unresolved` per the `docs/runbook.md` "Resolving a dispute" workflow. The Weekly Health routine appends new candidates here every Sunday.

> [!note] Dataview can't filter list items by content, so this lists every synthesis page that *has* a `## Disputes` section. Page-level filtering happens in your head after clicking through. To search for the literal status, use `Ctrl/Cmd-Shift-F` → `"Status: unresolved"`.

```dataview
LIST
FROM "concepts" OR "entities" OR "topics" OR "answers"
WHERE contains(file.outlinks.path, "")  /* dummy clause; below filters by section heading text */
WHERE regexmatch("(?m)^## Disputes\\s*$", file.frontmatter.title) OR true
LIMIT 0
```

```dataviewjs
// dvjs scan: list synthesis pages whose body contains a literal "Status: unresolved" bullet.
const pages = dv.pages('"concepts" OR "entities" OR "topics" OR "answers"');
const out = [];
for (const p of pages) {
  const tfile = app.vault.getAbstractFileByPath(p.file.path);
  if (!tfile) continue;
  const body = await app.vault.cachedRead(tfile);
  const matches = (body.match(/Status: unresolved/g) || []).length;
  if (matches > 0) {
    out.push({ link: p.file.link, count: matches, kind: p.kind });
  }
}
out.sort((a, b) => b.count - a.count);
dv.table(
  ["Page", "Kind", "Unresolved disputes"],
  out.map((r) => [r.link, r.kind, r.count]),
);
```

---

## Recent answers (last 30 days)

```dataview
TABLE WITHOUT ID
  file.link AS "Answer",
  question AS "Question",
  last_updated AS "Answered"
FROM "answers"
WHERE date(today) - date(last_updated) <= dur(30 days)
SORT last_updated DESC
LIMIT 15
```

---

## Orphan synthesis pages

Synthesis pages that no other page links to. Either backlink them from a relevant topic / concept, or delete if no longer relevant.

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  kind AS "Kind",
  last_updated AS "Last touched"
FROM "concepts" OR "entities" OR "answers"
WHERE length(file.inlinks) = 0
SORT last_updated DESC
LIMIT 15
```

---

## Quick search recipes

Paste these into the global search (**Ctrl/Cmd-Shift-F**) to filter the vault by topic or by status. Adjust the topic id as needed:

- `path:"sources/" "topic: agentic-coding"` — every source ingested for one topic
- `path:"wiki/" "Status: unresolved"` — every unresolved dispute, anywhere
- `path:"wiki/" "- [ ]"` — every open question
- `path:"reports/" "daily"` — every daily research report (newest in `reports/` ascending)
- `path:"reports/" "health"` — every weekly health report

## Local-graph deep-dive (the killer pattern)

When working on a topic, open its `index.md` (e.g., `[[agentic-coding]]`), then `Ctrl/Cmd-P` → **Open local graph view**. Set the depth slider to **2**. You now see the topic page plus every concept, entity, source, comparison, and answer that's at most two hops away — the topic's neighborhood in one frame. The color groups from `graph.json` carry over.
