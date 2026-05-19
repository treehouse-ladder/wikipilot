---
title: Agentic coding tools and harnesses
kind: topic
sources:
  - "[[automate-work-with-routines-claude-code-routines-docs-d09f612e]]"
  - "[[cursor-2-0-multi-agents-and-composer-changelog-4665f068]]"
  - "[[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]]"
  - "[[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]]"
last_updated: 2026-05-12
last_verified: 2026-05-12
freshness_window_days: 30
---

# Agentic coding tools and harnesses

See [[purpose]] for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

The agentic-coding tool layer in 2026 has converged on three structural primitives: parallel subagents with isolated workspaces, persistent cloud routines for unattended work, and sandboxed shell execution as the default safety story. Cursor 2.0 ships "up to eight agents in parallel on a single prompt" using "git worktrees or remote machines to prevent file conflicts," with each agent in "its own isolated copy of your codebase" [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]]. Anthropic's Claude Code Routines (research preview) generalize the same pattern to scheduled / API / GitHub triggers running in the cloud, where "a routine is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors" that "execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed" [[automate-work-with-routines-claude-code-routines-docs-d09f612e]].

> Run up to eight agents in parallel on a single prompt. This uses git worktrees or remote machines to prevent file conflicts. Each agent operates in its own isolated copy of your codebase.

> A routine is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically. Routines execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed.

The subagent primitive has become an industry-wide convention, with documentation now shipping across "OpenAI Codex, Claude Code, Gemini CLI (experimental), Mistral Vibe, OpenCode, Visual Studio Code, and Cursor" [[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]]. This convergence in API surface is meaningful — it lets evaluation harnesses and tooling target one mental model rather than per-vendor abstractions. The dominant evaluation harness for coding-agent capability remains SWE-bench Verified, "a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI" where "human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable" [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]].

> The subagents pattern is widely supported in coding agents now. Documentation across a number of different platforms: OpenAI Codex subagents, Claude Code subagents, Gemini CLI subagents (experimental), Mistral Vibe subagents, OpenCode agents, Subagents in Visual Studio Code, Cursor Subagents.

> SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI. Human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information.

For evaluating language models directly (as opposed to bespoke agent stacks), SWE-bench's bash-only track standardizes on mini-SWE-agent: "a minimal bash environment. No tools, no special scaffold structure; just a simple ReAct agent loop" [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]]. Cursor 2.0 also positions a vendor-trained model — Composer — as part of the agentic-coding stack: "Introducing our first agentic coding model. Composer is a frontier model that is 4x faster than similarly intelligent models" [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]]. The "4x faster" claim lacks public methodology and is filed under `## Disputes` below.

## Recent updates

- Cursor 2.0 (Oct 29, 2025) introduces multi-agent dispatch, the Composer agentic-coding model, sandboxed terminals on macOS (now GA), and Plan Mode in Background [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]].
- Anthropic's Claude Code Routines moves Claude Code from per-session interactive use to unattended cloud execution with three trigger types (Scheduled, API, GitHub) and per-routine bearer tokens for programmatic dispatch [[automate-work-with-routines-claude-code-routines-docs-d09f612e]].
- OpenAI Codex shipped subagents to general availability in March 2026, "after several weeks of preview behind a feature flag" — closing the feature gap with Claude Code's earlier subagent implementation [[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]].
- SWE-bench Verified's mini-SWE-agent harness moved to v2.x, switching from string-parsed actions to tool-calling APIs; v1.x and v2.x leaderboard rows are explicitly noted as not directly comparable [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]].
- Sandboxing is now the default behavior for agent-issued shell commands on Cursor's macOS builds; previously this was opt-in [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]].

## Comparisons

The comparison pages below are pre-declared by the charter; they are
written to `wiki/comparisons/` once the topic-researcher has accumulated
≥ 2 entity pages with the relevant frontmatter fields. Listed here in
prose backticks (not double-bracket wiki links) so the broken-wikilink
lint stays quiet until each page actually exists:

- `agentic-ide-comparison` — Claude Code vs Cursor vs Codex vs Aider on
  parallel-subagents, prompt caching, MCP, cost, sandbox model.
- `agent-eval-harness-comparison` — SWE-bench variants vs RE-Bench.

## Disputes

- [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]] claims Cursor's Composer model is "4x faster than similarly intelligent models" without naming the comparison set or the harness used to measure speed; [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]] explicitly notes that even within one harness (mini-SWE-agent), "results of release 1.x and 2.x are not necessarily comparable to each other" — making vendor-side speed claims hard to verify without the full prompt set. Status: unresolved (confidence: medium; sweep: 2026-05-12)

## Open questions

- [ ] What is the cache-invalidation behavior of multi-agent setups when one agent edits a file mid-run that another agent has cached? Cursor's worktree-per-agent design [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]] avoids file-level conflicts but the prompt-cache implications across worktrees aren't documented in the changelog.
- [ ] Does Claude Code Routines' "Anthropic-managed cloud infrastructure" [[automate-work-with-routines-claude-code-routines-docs-d09f612e]] use the same prompt-caching tier as interactive sessions, and if not, what does that imply for cost-per-routine-run vs cost-per-interactive-session?
- [ ] Among the seven vendors documented to support subagents [[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]], do they share a common interchange format (e.g. is a Codex custom-agent TOML portable to Claude Code), or is the convergence purely in concept?

## See also

- [[purpose]]
