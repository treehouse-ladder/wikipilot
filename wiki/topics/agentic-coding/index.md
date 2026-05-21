---
title: Agentic coding tools and harnesses
kind: topic
sources:
  - "[[automate-work-with-routines-claude-code-routines-docs-d09f612e]]"
  - "[[cursor-2-0-multi-agents-and-composer-changelog-4665f068]]"
  - "[[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]]"
  - "[[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]]"
  - "[[equipping-agents-for-the-real-world-with-agent-skills-2e50ab69]]"
  - "[[introducing-agent-skills-anthropic-5fb2ccf0]]"
  - "[[claude-skills-are-awesome-maybe-a-bigger-deal-than-mcp-simon-willison-7efc395e]]"
  - "[[effective-harnesses-for-long-running-agents-anthropic-engineering-7f7a70a6]]"
  - "[[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]]"
  - "[[code-execution-with-mcp-building-more-efficient-ai-agents-9b88bfec]]"
  - "[[effective-context-engineering-for-ai-agents-anthropic-engineering-126e07cf]]"
  - "[[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]]"
  - "[[introducing-claude-opus-4-7-b8af8104]]"
  - "[[best-practices-for-claude-code-anthropic-engineering-b7723535]]"
  - "[[subagents-openai-codex-developers-openai-com-8334be02]]"
  - "[[building-agents-with-the-claude-agent-sdk-anthropic-engineering-cf56e261]]"
  - "[[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]]"
  - "[[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]]"
  - "[[saving-swe-bench-a-benchmark-mutation-approach-for-realistic-agent-evaluation-0404d7de]]"
  - "[[subagents-agentic-engineering-patterns-3262892c]]"
  - "[[2026-agentic-coding-trends-report-27fe0474]]"
  - "[[swe-context-bench-a-benchmark-for-context-learning-in-coding-aba13bd3]]"
last_updated: 2026-05-21
last_verified: 2026-05-21
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

## Skills, harnesses, and the long-running-agent stack (added 2026-05-20)

A second structural primitive has solidified alongside parallel subagents and cloud routines: **Agent Skills**, framed by Anthropic as folders of "instructions, scripts, and resources that Claude can load when needed" and explicitly designed for cross-platform portability [[equipping-agents-for-the-real-world-with-agent-skills-2e50ab69]] [[introducing-agent-skills-anthropic-5fb2ccf0]]. The pattern is now Claude-Code-native — "SKILL.md files in .claude/skills/" extend Claude with project-specific domain knowledge [[best-practices-for-claude-code-anthropic-engineering-b7723535]] — and Simon Willison argues Skills may be "a bigger deal than MCP" because the unit (a markdown file plus optional scripts) is far simpler than the MCP server protocol [[claude-skills-are-awesome-maybe-a-bigger-deal-than-mcp-simon-willison-7efc395e]].

> Skills are folders that include instructions, scripts, and resources that Claude can load when needed. They can be used across Claude apps, Claude Code, and the API.

> Agent Skills have been published as an open standard. We believe skills should be portable across tools and platforms — the same skill should work whether you're using Claude or other AI platforms.

> A skill is conceptually simple — a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts that the model can run.

> You can create SKILL.md files in .claude/skills/ to give Claude domain knowledge and reusable workflows, extending Claude's knowledge with information specific to your project, team, or domain.

The **long-running-agent harness** has matured into two published Anthropic patterns. The session-bridging pattern uses "an initializer agent that sets up the environment on the first run, and a coding agent that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session" [[effective-harnesses-for-long-running-agents-anthropic-engineering-7f7a70a6]]. The autonomous-full-stack pattern is a three-agent planner/generator/evaluator stack that ran as "one continuous session across the whole build, with the Claude Agent SDK's automatic compaction handling context growth" [[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]] — and notably claims that "Claude Opus 4.5 largely removed 'context anxiety' behavior, so context resets could be dropped from this harness entirely" [[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]]. The harness layer is now packaged as the **Claude Agent SDK** (the Claude Code SDK was renamed "to reflect its broader vision beyond just coding") [[building-agents-with-the-claude-agent-sdk-anthropic-engineering-cf56e261]].

> The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before.

> The final result was a three-agent architecture — planner, generator, and evaluator — that produced rich full-stack applications over multi-hour autonomous coding sessions.

> The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather context, plan, and execute, with context management capabilities such as compaction, which enables an agent to work on a task without exhausting the context window.

**Code execution with MCP** is the cost-engineering counterpart: rather than loading tool definitions up-front, agents "read tool definitions on-demand" and can "write out a conditional tree that gets executed [to save] on 'time to first token' latency rather than having to wait for a model to evaluate an if-statement" [[code-execution-with-mcp-building-more-efficient-ai-agents-9b88bfec]]. This is the operational lever for MCP setups with thousands of tools where naive context loading dominates.

> Code execution with MCP enables agents to use context more efficiently by loading tools on demand, filtering data before it reaches the model, and executing complex logic in a single step.

**Context engineering** is now Anthropic's preferred framing for what was "prompt engineering" — "strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts" [[effective-context-engineering-for-ai-agents-anthropic-engineering-126e07cf]]. The term is meaningful because it captures the multi-session, tool-output-laden reality of agentic coding (vs. a single chat completion).

> Context engineering is the natural progression of prompt engineering. Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

On the **evaluation methodology** side, Anthropic's infrastructure-noise writeup is the most pointed counterweight to the existing SWE-bench Verified claims on this page: "Infrastructure configuration can swing agentic coding benchmarks by several percentage points — sometimes more than the leaderboard gap between top models" [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]]. In their Terminal-Bench 2.0 experiments, "infrastructure error rates dropp[ed] monotonically from 5.8% at strict enforcement to 0.5% when uncapped" [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]] — meaning any vendor SWE-bench score that doesn't pin resource configuration is consuming an unknown fraction of variance.

> Infrastructure configuration can swing agentic coding benchmarks by several percentage points — sometimes more than the leaderboard gap between top models.

> In experiments running Terminal-Bench 2.0 across six resource configurations with different levels of resource headroom, success rates increased with resource headroom, primarily driven by infrastructure error rates dropping monotonically from 5.8% at strict enforcement to 0.5% when uncapped.

The frontier coding-agent model layer has shifted to **Claude Opus 4.7**, which Anthropic positions as "the most capable generally available model to date [...] recommended for the most demanding use cases [...] particularly production-ready code, sophisticated AI agents" [[introducing-claude-opus-4-7-b8af8104]]. The headline coding claim — "On Rakuten-SWE-Bench, Claude Opus 4.7 resolves 3x more production tasks than Opus 4.6" — uses a partner-internal benchmark rather than SWE-bench Verified and is filed under ## Disputes below for methodology asymmetry [[introducing-claude-opus-4-7-b8af8104]].

> Opus 4.7 is the most capable generally available model to date and is recommended for the most demanding use cases where frontier intelligence is needed — particularly production-ready code, sophisticated AI agents, and complex document creation.

> On Rakuten-SWE-Bench, Claude Opus 4.7 resolves 3x more production tasks than Opus 4.6, with double-digit gains in Code Quality and Test Quality.

Finally, the **subagent convergence** noted in the prior synthesis is now backed by the OpenAI primary source. Codex "lets you define custom agents as TOML files in ~/.codex/agents/, which can have custom instructions and be assigned to use specific models" — and Codex itself "handles orchestration across agents, including spawning new subagents, routing follow-up instructions, waiting for results, and closing agent threads" [[subagents-openai-codex-developers-openai-com-8334be02]]. The TOML-vs-Markdown definition format difference (Codex TOML vs Claude Code's `.claude/agents/` markdown) is a concrete interop wedge that the existing open question on subagent portability should now track against.

> Codex lets you define custom agents as TOML files in ~/.codex/agents/, which can have custom instructions and be assigned to use specific models.

> Codex handles orchestration across agents, including spawning new subagents, routing follow-up instructions, waiting for results, and closing agent threads. When many agents are running, Codex waits until all requested results are available, then returns a consolidated response.

## Harness automation and the eval-realism debate (added 2026-05-21)

The harness layer is no longer purely hand-crafted. **Agentic Harness Engineering (AHE)** treats the harness itself as the optimization target, holding the base model fixed while an evolution agent edits "system prompts, tool descriptions, tool implementations, middleware, skills, sub-agents, and long-term memory" under three observability pillars — component, experience, and decision observability — so that "every edit [becomes] a falsifiable contract" [[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]]. The headline result is that "Ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%)" and the "frozen harness transfers to SWE-bench-verified" with "+5.1 to +10.1 percentage points" across base-model families [[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]]. The paper's central claim — "the bottleneck for harness evolution is observability, not agent capability" — is a direct counterweight to the assumption that better harnesses require human craft.

> AHE is a closed loop that addresses [harness evolution] through three matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes.

> Ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO.

On **evaluation realism**, the existing infrastructure-noise critique now has a companion: a benchmark-mutation study argues SWE-bench Verified "fail[s] to reflect how developers interact with chat-based coding assistants in IDEs, leading to systematic overestimation of agent capabilities," measuring that "traditional benchmarks overestimate agent capabilities by 20-50% for publicly available datasets" while "the performance gap narrows to 10-16% for internal benchmarks like SWE-Bench C#" [[saving-swe-bench-a-benchmark-mutation-approach-for-realistic-agent-evaluation-0404d7de]].

> Current benchmarks like SWE-Bench Verified are derived from GitHub issues and fail to reflect how developers interact with chat-based coding assistants in IDEs, leading to systematic overestimation of agent capabilities in real-world scenarios, especially bug fixing.

A distinct eval axis — **context learning** — is staked out by SWE Context Bench, which "groups base tasks and related tasks with shared context across 51 unique repositories and 9 programming languages, evaluating how accurately and efficiently agents solve related issues when prior cases are available in context" [[swe-context-bench-a-benchmark-for-context-learning-in-coding-aba13bd3]]. This measures whether an agent's earlier work on a repo improves its later work — something SWE-bench Verified does not.

> SWE Context Bench groups base tasks and related tasks with shared context across 51 unique repositories and 9 programming languages, evaluating how accurately and efficiently agents solve related issues when prior cases are available in context.

## Subagent practice and the security floor (added 2026-05-21)

Simon Willison's Agentic Engineering Patterns guide frames a subagent as a dispatch where "a coding agent effectively dispatches a fresh copy of itself to achieve a specified goal, with a new context window that starts with a fresh prompt," whose "principle advantage is that it can work with a fresh context in a way that avoids spending tokens from the parent's available limit" [[subagents-agentic-engineering-patterns-3262892c]]. He warns against over-decomposition — "the main value of subagents is in preserving that valuable root context and managing token-heavy operations" — and notes the cost/latency lever of routing subagents to "faster and cheaper models such as Claude Haiku" [[subagents-agentic-engineering-patterns-3262892c]]. This nuances the wiki's prior framing of subagents as primarily a parallelism primitive: the dominant payoff is context preservation, with parallelism and model-routing as secondary wins.

> While it can be tempting to go overboard breaking up tasks across dozens of different specialist subagents, it's important to remember that the main value of subagents is in preserving that valuable root context and managing token-heavy operations.

The **security floor** for shell-and-tool-using agents is sobering. A systematization-of-knowledge study finds that "tool outputs are treated as trusted instructions, which enabled arbitrary behavior redirection since agents process tool outputs with the same trust level as system instructions," and that across 78 studies "attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are employed" [[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]]. The most dangerous class is compound: "a malicious MCP server triggering poisoned skill installation followed by persistent data exfiltration" — directly implicating the Skills and MCP primitives otherwise covered as productivity wins here.

> A meta-analysis of 78 recent studies from 2021-2026 found that attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are employed.

> Compound attacks involving multi-layer attack chains - such as a malicious MCP server triggering poisoned skill installation followed by persistent data exfiltration - were the most damaging and hardest to detect.

Anthropic's **2026 Agentic Coding Trends Report** quantifies the orchestration shift: "software development is shifting from writing code to orchestrating agents that write code," with "multi-agent architectures us[ing] an orchestrator to coordinate specialized agents working in parallel" [[2026-agentic-coding-trends-report-27fe0474]]. The most useful data point counters AI-replaces-engineers framing: "engineers use AI in roughly 60% of their work but report being able to 'fully delegate' only 0-20% of tasks" [[2026-agentic-coding-trends-report-27fe0474]]. As a first-party Anthropic report drawing on customer case studies, it carries a vendor-incentive caveat (filed under Disputes).

> Software development is shifting from writing code to orchestrating agents that write code.

> Anthropic's internal research found that engineers use AI in roughly 60% of their work but report being able to 'fully delegate' only 0-20% of tasks, with the gap explained by effective AI collaboration requiring active human participation - setup, prompting, supervision, validation, and judgment.

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
- [[introducing-claude-opus-4-7-b8af8104]] claims a '3x more production tasks than Opus 4.6' result on Rakuten-SWE-Bench, a partner-internal benchmark whose composition and scoring methodology is not publicly described; [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]] explicitly notes that even within the public SWE-bench Verified harness, leaderboard rows can be incomparable across mini-SWE-agent versions, suggesting any cross-benchmark 'Nx better' claim should be treated as unfalsifiable until the partner benchmark is published. Status: unresolved
- [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]] claims infrastructure configuration can swing agentic coding benchmark scores by 'sometimes more than the leaderboard gap between top models', with measured infrastructure error rates of 5.8% under strict enforcement vs 0.5% uncapped; this directly undercuts the comparability of any SWE-bench Verified score that does not pin the resource configuration used. Status: unresolved
- [[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]] claims 'Claude Opus 4.5 largely removed context anxiety behavior, so context resets could be dropped from this harness entirely', while [[effective-harnesses-for-long-running-agents-anthropic-engineering-7f7a70a6]] presents the opposing pattern of explicit session-bridging via initializer + coding agents handing off via on-disk artifacts; the two patterns may be complementary or may represent unresolved disagreement about whether compaction-within-a-session is sufficient. Status: unresolved
- [[saving-swe-bench-a-benchmark-mutation-approach-for-realistic-agent-evaluation-0404d7de]] claims SWE-bench Verified systematically overestimates real-world agent capability by 20-50% on public datasets (and only 10-16% on a private C# benchmark); [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]] presents SWE-bench Verified as the human-filtered, annotator-reviewed gold standard for coding-agent capability. Status: unresolved
- [[2026-agentic-coding-trends-report-27fe0474]] is a first-party Anthropic report whose "orchestration era" framing is supported primarily by case studies drawn from Anthropic's own customers (Rakuten, CRED, TELUS, Zapier), creating a vendor-incentive asymmetry; this shares Rakuten-partner-benchmark provenance with [[introducing-claude-opus-4-7-b8af8104]], so cross-report claims should not be treated as independent corroboration. Status: unresolved
- [[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]] claims an automatically-evolved harness surpasses the human-designed Codex-CLI harness (77.0% vs 71.9% pass@1 on Terminal-Bench 2) and transfers frozen to SWE-bench-verified; [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]] shows Terminal-Bench scores can swing several percentage points from infrastructure resource configuration, so a 5.1-point harness gain may be partly confounded unless resource configuration was pinned identically. Status: unresolved

## Open questions

- [ ] What is the cache-invalidation behavior of multi-agent setups when one agent edits a file mid-run that another agent has cached? Cursor's worktree-per-agent design [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]] avoids file-level conflicts but the prompt-cache implications across worktrees aren't documented in the changelog.
- [ ] Does Claude Code Routines' "Anthropic-managed cloud infrastructure" [[automate-work-with-routines-claude-code-routines-docs-d09f612e]] use the same prompt-caching tier as interactive sessions, and if not, what does that imply for cost-per-routine-run vs cost-per-interactive-session?
- [ ] Among the seven vendors documented to support subagents [[use-subagents-and-custom-agents-in-codex-simon-willison-march-2026-7be24bde]], do they share a common interchange format (e.g. is a Codex custom-agent TOML portable to Claude Code), or is the convergence purely in concept?
- [ ] How do Agent Skills compose with MCP servers in practice? [[claude-skills-are-awesome-maybe-a-bigger-deal-than-mcp-simon-willison-7efc395e]] frames Skills as 'maybe a bigger deal than MCP' but does not show whether a Skill can wrap or call into an MCP server, or whether the two patterns address overlapping problems.
- [ ] Does code-execution-with-MCP's 'tools as code on a filesystem' design [[code-execution-with-mcp-building-more-efficient-ai-agents-9b88bfec]] break prompt caching when the agent edits the tool definitions mid-session?
- [ ] Are Codex custom-agent TOML files [[subagents-openai-codex-developers-openai-com-8334be02]] portable to Claude Code's markdown-based `.claude/agents/` definitions, or is the cross-vendor subagent convergence purely conceptual?
- [ ] What is the cost-per-completed-app on Opus 4.5/4.6/4.7 in the three-agent planner/generator/evaluator harness [[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]] vs single-agent baselines?
- [ ] Does the Claude Agent SDK rename [[building-agents-with-the-claude-agent-sdk-anthropic-engineering-cf56e261]] change the surface API in a backward-incompatible way, or is it purely a brand change?
- [ ] Does Agentic Harness Engineering [[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]] hold the resource/infrastructure configuration fixed across human-designed and evolved harnesses, given that [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]] showed several-percent swings from config alone?
- [ ] Can the Skills-as-attack-surface finding from [[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]] (poisoned skill installation) be reconciled with the productivity framing of Skills in [[introducing-agent-skills-anthropic-5fb2ccf0]] — what containment does Anthropic's Skills loader provide against a malicious SKILL.md?
- [ ] Does the 20-50% public-vs-10-16% private overestimation gap in [[saving-swe-bench-a-benchmark-mutation-approach-for-realistic-agent-evaluation-0404d7de]] hold when controlling for benchmark difficulty/language rather than just public-vs-private provenance?
- [ ] How does SWE Context Bench's context-learning metric [[swe-context-bench-a-benchmark-for-context-learning-in-coding-aba13bd3]] correlate with the session-bridging long-running-agent harness [[effective-harnesses-for-long-running-agents-anthropic-engineering-7f7a70a6]]?
- [ ] Simon Willison's subagents guidance [[subagents-agentic-engineering-patterns-3262892c]] frames context-preservation as the primary subagent payoff over parallelism; does any published wall-clock measurement separate the context-preservation benefit from the parallelism benefit?

## See also

- [[purpose]]
