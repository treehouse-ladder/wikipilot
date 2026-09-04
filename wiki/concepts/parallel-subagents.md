---
title: Parallel Subagents
kind: concept
sources:
  - "[[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]"
  - "[[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]"
  - "[[cloud-environment-setup-and-cloud-subagents-in-agents-window-ac3775dd]]"
  - "[[customize-cursor-16819559]]"
  - "[[configuration-smells-in-agents-md-files-common-mistakes-in-configuring-coding-agents-7374633f]]"
  - "[[claude-code-whats-new-week-26-june-22-26-2026-d0712d54]]"
  - "[[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]"
  - "[[build-from-anywhere-with-cursor-for-ios-097d5a19]]"
  - "[[changelog-codex-openai-developers-afbd4293]]"
  - "[[fable-s-judgement-e36be334]]"
  - "[[beyond-resolution-rates-behavioral-drivers-of-coding-agent-success-and-failure-fdcb2bd4]]"
  - "[[the-new-gpt-5-6-family-luna-terra-sol-195d8ae2]]"
  - "[[rewriting-bun-in-rust-15a50b3d]]"
  - "[[claude-code-release-notes-98ffc52d]]"
  - "[[message-your-other-claude-code-sessions-90ee76df]]"
  - "[[claude-code-v2-1-230-to-v2-1-232-major-updates-sub-agent-fork-defaults-and-cross-session-mentions-2308d6cf]]"
  - "[[clawarena-team-benchmarking-subagent-orchestration-and-dynamic-workflows-in-language-model-agents-3a15d772]]"
  - "[[orchbench-evaluating-multi-agent-orchestration-plans-in-isolation-via-deterministic-simulation-c9f42c6d]]"
  - "[[claude-code-v2-1-251-model-switch-hooks-foreground-subagent-streaming-and-prompt-cache-observability-2180229d]]"
  - "[[claude-code-v2-1-259-managed-mcp-servers-and-headless-unattended-permissions-0e371a11]]"
last_updated: 2026-09-04
last_verified: 2026-09-04
freshness_window_days: 30
---

# Parallel Subagents

## Summary

Cursor's 2026-06-04 SDK release adds recursive subagent nesting: a subagent session registers the executor it needs to call Task, so subagents can spawn subagents to any depth with each level keeping its own prompt and model [[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]. This puts Cursor's harness on structural parity with Claude Code's `CLAUDE_CODE_FORK_SUBAGENT` parallel-fork mechanism, but with the orchestration tree explicit in user code (TypeScript/Python SDK) rather than implicit in the agent's tool calls — useful when the orchestration graph itself needs to be tested or version-controlled.

> Subagents can now spawn their own subagents, and a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model. There's nothing to turn on; a subagent session registers the executor it needs to call Task, so nesting works automatically for any agent that defines subagents.

The merge step in parallel-subagent workflows has a measurable cost: Parallel-Synthesis observes that current systems merge fan-out branches by concatenating worker text outputs, discarding parallel structure and re-incurring prefill, and instead has the synthesizer consume the workers' KV caches directly [[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]. This is a concrete attack on the "merge dominates wall-clock" caveat that makes naive parallel subagents not always faster than serial execution.

> Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. We introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents.

Cursor's June 2026 `/in-cloud` update pushes the isolation boundary from worktree-per-subagent to full cloud VM per subagent: a cloud subagent runs on its own VM and branch, keeping long-running or parallel work (CI fixes, issue investigation, codebase exploration) off the local machine while the workspace stays responsive [[cloud-environment-setup-and-cloud-subagents-in-agents-window-ac3775dd]]. Cloud environment setup completes in under ten minutes and is captured in reusable snapshots for faster subsequent starts. This extends the worktree-isolation mental model (Cursor 2.0, nested subagents) to a full per-subagent VM isolation boundary — structurally heavier but with stronger blast-radius containment for parallel work.

> You can use /in-cloud to spin up a cloud subagent in its own VM to work on the next task you submit. It runs on its own VM and branch, so your local workspace stays clean and responsive. This is especially useful for isolating long-running or parallel work like fixing CI, investigating an issue, or exploring a codebase while you keep working locally.

**Team-wide skill/MCP distribution for parallel-subagent contexts.** Cursor 3.9's Customize page consolidates plugins, skills, MCPs, subagents, rules, commands, and hooks into one place manageable at user/team/workspace scope, with a popularity leaderboard and one-click install across a team [[customize-cursor-16819559]]. This operationalizes the configuration-distribution layer for parallel-subagent workflows: when every team member can spawn subagents with shared skills/MCPs via the leaderboard, curation becomes an organizational asset rather than per-developer config drift — the failure mode catalogued as Skill Leakage (35% prevalence) in the AGENTS.md configuration-smells study [[configuration-smells-in-agents-md-files-common-mistakes-in-configuring-coding-agents-7374633f]].

> You can now add and manage plugins, skills, MCPs, subagents, rules, commands, and hooks at the user, team, or workspace level, and even bring your own custom MCPs. Cursor now shows you a leaderboard of the most popular plugins, skills, and MCPs across your team. [[customize-cursor-16819559]]

**Claude Code v2.1.259 adds org-level managed MCP servers (Sep 2026).** The release introduces `managedMcpServers` as a managed setting, allowing organizations to provide HTTP/SSE MCP servers to every user [[claude-code-v2-1-259-managed-mcp-servers-and-headless-unattended-permissions-0e371a11]]. This is Claude Code's organizational MCP distribution mechanism — structurally parallel to Cursor's team-level MCP management but implemented via a managed-settings push rather than a popularity-leaderboard pull. When a central MCP server is managed, every forked subagent inherits it without per-user configuration, which addresses the Skill Leakage config-drift failure mode from the same centralized angle as Cursor's team-level curation, but without the leaderboard discoverability layer.

> Added managedMcpServers managed setting for organizations to provide HTTP/SSE MCP servers to every user. [[claude-code-v2-1-259-managed-mcp-servers-and-headless-unattended-permissions-0e371a11]]

**Claude Code background-subagent permission surfacing closes the silent-denial gap.** Claude Code Week 26 (June 22–26) added background-subagent permission prompts to the main session: when a background subagent requests a tool, the permission dialog surfaces in the main session showing which agent is asking, and Esc denies only that tool rather than halting the entire workflow [[claude-code-whats-new-week-26-june-22-26-2026-d0712d54]]. This closes a critical gap in parallel-subagent workflows: previously a background-subagent denial was silent and irrecoverable without restarting the agent, breaking the "fork-and-forget" parallelism model that makes subagents viable for fan-out tasks.

> Background subagents now surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies only that tool. [[claude-code-whats-new-week-26-june-22-26-2026-d0712d54]]

**Claude Code v2.1.198: built-in Explore subagent now inherits the main session's model (July 2026).** The release escalates the built-in Explore agent's default model from Haiku to the main session's model (capped at Opus) [[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]. For parallel-subagent workflows this trades token cost for exploration quality — Explore is a subagent that typically gathers context across a large repo, so upgrading it from Haiku to Sonnet/Opus increases the per-exploration-task token spend but may reduce the number of exploration rounds needed. This is the reverse cost-quality tradeoff from the background-session durability and permission-surfacing improvements the wiki already tracks: those reduced friction with no quality regression, while the Explore upgrade deliberately spends more tokens per call.

> The built-in Explore agent now inherits the main session's model (capped at opus) instead of running on haiku. [[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]

**Mobile oversight of parallel-subagent workflows lands across vendors (Cursor iOS, June 2026).** Cursor for iOS allows launching and managing parallel always-on cloud agents from a phone, with Live Activities tracking up to eight agents at once on the lock screen and push notifications on agent turn completion [[build-from-anywhere-with-cursor-for-ios-097d5a19]]. This extends the mobile-control-plane pattern to the IDE-native agent side (joining Codex Remote) and shifts the approval/oversight modality for parallel long-running subagents from desktop to mobile — stressing post-flight verification that already scales poorly on larger screens.

> Get a push notification when an agent finishes a turn, and track up to eight agents at once with Live Activities on the lock screen and Dynamic Island. [[build-from-anywhere-with-cursor-for-ios-097d5a19]]

**Codex closes a silent subagent-failure hole (July 2026).** OpenAI's Codex changelog reports that parent agents now receive terminal subagent errors instead of seeing failed subagent work as an empty successful completion [[changelog-codex-openai-developers-afbd4293]]. This reliability fix is directly relevant to parallel-subagent orchestration harnesses where a masked subagent failure would corrupt the parent's synthesis step — the merge-step cost tax that Parallel-Synthesis targets is worse when the parent merges empty/failed output without knowing it failed.

> Parent agents now receive terminal subagent errors instead of seeing failed work as an empty successful completion. [[changelog-codex-openai-developers-afbd4293]]

**Per-task model downgrade as a default subagent operating pattern (Simon Willison, July 2026).** Willison escalates the subagent model-routing lever from a manual per-call choice into a standing instruction: "For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent" — the agent itself picks the tier (Sonnet for substantive implementation, Haiku for trivial/mechanical edits), runs the implementation in a subagent with a self-contained prompt, and returns to the top-tier main loop for review before committing [[fable-s-judgement-e36be334]]. He reports a concrete cost outcome (throughput up, Fable allowance depleting more slowly). The open caveat is that [[beyond-resolution-rates-behavioral-drivers-of-coding-agent-success-and-failure-fdcb2bd4]] finds the base LLM is the primary driver of outcome, so a self-selected cheaper implementation model may trade more resolve-rate than the token savings suggest — the value depends on the main-loop review step actually catching the resulting regressions.

> For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent. [[fable-s-judgement-e36be334]]

**OpenAI's GPT-5.6 moves subagent dispatch into the model API itself (July 2026).** The GPT-5.6 launch introduces *Multi-agent* as a first-class Responses API primitive: the model can "spin up subagents for parallel, focused work" — the sub-agent pattern "now baked into the core API" rather than being a harness-level orchestration layer [[the-new-gpt-5-6-family-luna-terra-sol-195d8ae2]]. This is a significant architectural boundary shift — parallel subagents have to date been harness features (`CLAUDE_CODE_FORK_SUBAGENT`, Cursor SDK recursive nesting, Codex custom-agents) layered on top of a tool-calling model; GPT-5.6 relocates dispatch into the model's own surface, making subagent orchestration a model capability rather than purely a harness capability. The implications for harness-vs-model attribution are open: if subagent fan-out becomes a built-in model feature, does the harness's measured contribution to SWE-bench/Terminal-Bench scores shrink?

> Multi-agent lets the model spin up subagents for parallel, focused work — the sub-agent pattern now baked into the core API. [[the-new-gpt-5-6-family-luna-terra-sol-195d8ae2]]

**Claude Code v2.1.217 adds a session-wide concurrency cap (20 concurrent subagents by default).** Distinct from the new per-session spawn budget (200 spawns via `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`), a separate concurrency cap (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, default 20) prevents any single message from fanning out unbounded background agents simultaneously [[claude-code-changelog-v2-1-212-to-v2-1-218-july-1822-2026-79752d66]]. The two limits compose: the concurrency cap governs how many agents run at once; the spawn budget governs the total for the session. The `context: fork` skill attribute now runs in the background by default (opt-out with `background: false`), making background delegation the default posture for skill-driven fan-out.

> Added a cap on concurrently-running subagents (default 20, override with `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) so one message can't fan out unbounded background agents. [[claude-code-changelog-v2-1-212-to-v2-1-218-july-1822-2026-79752d66]]

**Claude Code dynamic workflows now default to fewer than 15 agents (August 2026).** The release notes walk back the unbounded-fan-out framing tracked on [[agentic-coding]], setting dynamic workflows to "default to a medium size guideline (aim for fewer than 15 agents)" and removing Opus 4.7 from fast mode [[claude-code-release-notes-98ffc52d]]. This is a notable tempering of the earlier "hundreds of parallel subagents in a single session" research-preview positioning — a shipped conservative default suggests the unbounded-fan-out story carries real cost/coordination penalties in practice rather than being the recommended path. The absence of published data tying agent count to dynamic-workflow success rate leaves the question of whether 15 is a measured optimum or a pure cost ceiling open.

> Changed dynamic workflows to default to a medium size guideline (aim for fewer than 15 agents), and removed Opus 4.7 from fast mode so /fast now applies to Opus 5 and Opus 4.8. [[claude-code-release-notes-98ffc52d]]

**Claude Code makes subagent forking the default and adds cross-session agent-to-agent messaging (August 2026).** Two shifts land together. First, `subagent_type: "fork"` is now the default subagent type: a forked subagent inherits the full conversation and prompt cache, `@`-mentioning another session by name becomes a prompt affordance, and non-teammate spawns in interactive sessions run in the background by default [[claude-code-v2-1-230-to-v2-1-232-major-updates-sub-agent-fork-defaults-and-cross-session-mentions-2308d6cf]]. Fork-by-default makes the cheap, context-preserving fork — rather than a fresh-context child — the standard delegation, operationalizing the context-preservation-over-parallelism framing noted above (Willison) while concentrating the inherited-cache-invalidation risk. Second, cross-session messaging (v2.1.224+, macOS/Linux) is on by default: a session discovers reachable peers via `ListAgents` and delivers a thin text message via `SendMessage`, never sharing conversation history or files [[message-your-other-claude-code-sessions-90ee76df]]. This is a distinct coordination surface from in-session fan-out — it links independent long-running sessions across machines rather than parent-spawned children, extending the parallel-subagent mental model from a spawn tree to a peer mesh.

> Subagent forking is now on by default: a subagent_type: "fork" subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default. [[claude-code-v2-1-230-to-v2-1-232-major-updates-sub-agent-fork-defaults-and-cross-session-mentions-2308d6cf]]

> A message is a piece of text one Claude writes to another, never conversation history or files. Claude discovers the target with ListAgents and sends with SendMessage, so you never call either tool yourself. [[message-your-other-claude-code-sessions-90ee76df]]

**Orchestration-plan quality is now measurable in isolation from worker capability (August 2026).** Two new subagent-management benchmarks arrive that score the manager's coordination skill independently of raw model strength: ClawArena-Team deliberately constrains the manager (text-only perception, partial workspace access, a fixed locally-served subagent pool) so score deltas reflect management skill, not raw capability [[clawarena-team-benchmarking-subagent-orchestration-and-dynamic-workflows-in-language-model-agents-3a15d772]]; OrchBench evaluates the orchestration *plan* alone via deterministic simulation without ever invoking worker agents, measuring quality/makespan/token cost and finding that preserving task-critical information beats adding more agents [[orchbench-evaluating-multi-agent-orchestration-plans-in-isolation-via-deterministic-simulation-c9f42c6d]]. Both reinforce the context-preservation-over-parallelism thread this page tracks from Willison [[fable-s-judgement-e36be334]] and fork-by-default [[claude-code-v2-1-230-to-v2-1-232-major-updates-sub-agent-fork-defaults-and-cross-session-mentions-2308d6cf]], now with execution-free benchmarks quantifying the coordination-layer payoff independently of the subagent pool's raw capability.

> The main agent is deliberately constrained: it natively perceives only text and directly accesses only part of the workspace. It commands a fixed, locally served subagent pool, so score differences reflect management skill, not raw capability. [[clawarena-team-benchmarking-subagent-orchestration-and-dynamic-workflows-in-language-model-agents-3a15d772]]

> We find that preserving task-critical information is more important than simply increasing the number of agents, and a systematic study of orchestration strategies across workflows containing up to 1,000 subtasks reveals previously hidden coordination failures. [[orchbench-evaluating-multi-agent-orchestration-plans-in-isolation-via-deterministic-simulation-c9f42c6d]]

**Claude Code v2.1.251 adds foreground subagent streaming and prompt-cache observability (August 2026).** Foreground subagent tool calls and results now live-stream to Remote Control clients — background subagents, still the default, remain status-only [[claude-code-v2-1-251-model-switch-hooks-foreground-subagent-streaming-and-prompt-cache-observability-2180229d]]. A new per-session prompt-cache line in `/cost` reports hit ratio, misses, tokens re-cached, and warm/cold state, giving concrete observability into the cache-invalidation behavior that the fork-by-default open question (below) flags as the default failure mode [[claude-code-v2-1-251-model-switch-hooks-foreground-subagent-streaming-and-prompt-cache-observability-2180229d]]. SessionStart resume hooks now receive session staleness and an estimated re-cache cost, turning the previously-invisible warm/cold decision into a hookable signal.

> Added live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only). Added a per-session prompt-cache line to /cost (hit ratio, misses, tokens re-cached, warm/cold). [[claude-code-v2-1-251-model-switch-hooks-foreground-subagent-streaming-and-prompt-cache-observability-2180229d]]

## Disputes

- [[build-programmatic-agents-with-the-cursor-sdk-fe66773e]] (cited on this page) attributes nested subagent nesting to the **2026-06-04** Cursor SDK release; [[custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-7da739cc]] (cited on the agentic-coding topic page) attributes the same Cursor SDK nested subagent feature to **2026-06-10**, framing both Claude Code and Cursor SDK as shipping "within 24 hours of each other on 2026-06-10." Status: unresolved — both sources are primary-source Cursor/Anthropic documentation; the date discrepancy is either a staging/preview vs GA distinction, or a documentation error on one source. (Confidence: medium; sweep: 2026-08-16)

## Open questions

- [ ] Does direct KV-cache synthesis (Parallel-Synthesis) hold up when worker branches used different system prompts or models, or does it require homogeneous workers to share a cacheable prefix?
- [ ] Does a fork-default subagent's inherited prompt cache [[claude-code-v2-1-230-to-v2-1-232-major-updates-sub-agent-fork-defaults-and-cross-session-mentions-2308d6cf]] survive the parent editing a file mid-run, or does fork-by-default simply make the cache-invalidation cliff the default failure mode for delegated work?
- [ ] Cross-session SendMessage shares only thin text, never context [[message-your-other-claude-code-sessions-90ee76df]] — is there any prompt-cache or context sharing between independent peer sessions, or must each peer re-derive shared context from scratch, setting a coordination-cost floor for multi-session (as opposed to spawn-tree) workflows?

## See also

- [[agentic-coding]]
