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
  - "[[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]]"
  - "[[cursor-changelog-pr-review-build-plan-in-parallel-and-split-prs-may-7-2026-29f64665]]"
  - "[[improving-cursor-s-agent-for-openai-codex-models-cursor-blog-a876aa9c]]"
  - "[[continually-improving-our-agent-harness-cursor-blog-173ad132]]"
  - "[[swe-webdevbench-evaluating-coding-agent-application-platforms-as-virtual-software-agencies-c47cb7a6]]"
  - "[[enabling-claude-code-to-work-more-autonomously-anthropic-270c90d1]]"
  - "[[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]"
  - "[[scaling-managed-agents-decoupling-the-brain-from-the-hands-8537165d]]"
  - "[[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]"
  - "[[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]"
  - "[[skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks-1743f5a5]]"
last_updated: 2026-05-22
last_verified: 2026-05-22
freshness_window_days: 30
---

# Agentic coding tools and harnesses

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
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

## Sandboxing-as-autonomy and the Cursor harness layer (added 2026-05-21 run 2)

The sandboxing story now has an Anthropic first-party writeup with concrete numbers: Claude Code's OS-level sandbox "safely reduces permission prompts by 84%" by enforcing two boundaries — filesystem and network isolation — "built on top of OS level primitives such as Linux bubblewrap and MacOS seatbelt" [[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]]. Network egress is gated through "a unix domain socket connected to a proxy server running outside the sandbox." This is the operational containment story the prompt-injection SoK on this page called for — it directly addresses the data-exfiltration class, though it does not by itself defend against the trusted-tool-output trust-level problem.

> Claude Code's sandboxing safely reduces permission prompts by 84%. These restrictions are built on top of OS level primitives such as Linux bubblewrap and MacOS seatbelt to enforce restrictions at the OS level. Network isolation is achieved by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox.

The same autonomy push ships at the product layer as **checkpoints**: "a checkpoint system [that] automatically saves your code state before each change" with instant rewind via `/rewind` (or double-Esc), scoped to "Claude's edits and not user edits or bash commands" [[enabling-claude-code-to-work-more-autonomously-anthropic-270c90d1]]. Checkpoints frame subagents, hooks, and background tasks as safe for unattended work.

> Anthropic's new checkpoint system automatically saves your code state before each change, and you can instantly rewind to previous versions by tapping Esc twice or using the /rewind command. Checkpoints apply to Claude's edits and not user edits or bash commands.

Cursor's harness layer is now documented across three first-party posts. The May 7 2026 release adds in-editor PR review, plan-level parallelism, and an automated **Split PRs** flow; the `/multitask` command "break[s] down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously" [[cursor-changelog-pr-review-build-plan-in-parallel-and-split-prs-may-7-2026-29f64665]]. On harness construction, Cursor frames the harness and the model as jointly determinative — "the harness and the model together determine how good the agent is" — and runs both public benchmarks and a private suite, **CursorBench** [[continually-improving-our-agent-harness-cursor-blog-173ad132]]. Cross-vendor interop: aligning Cursor's harness to OpenAI's Codex models required making "the names and definitions of tools in Cursor closer to their shell equivalents like rg (ripgrep)" and capturing reasoning items via the Responses API [[improving-cursor-s-agent-for-openai-codex-models-cursor-blog-a876aa9c]] — evidence that subagent/tool convergence is shallow at the API surface.

> The /multitask command is now available in the editor for running async subagents to parallelize your requests; it will break down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously.

> The harness and the model together determine how good the agent is, maintaining public benchmarks alongside their own eval suite called CursorBench.

> To encourage tool calling, they made the names and definitions of tools in Cursor closer to their shell equivalents like rg (ripgrep).

On the **eval-realism** axis, SWE-WebDevBench extends the benchmark-realism debate to full-stack app-generation platforms using "a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics" across six platforms [[swe-webdevbench-evaluating-coding-agent-application-platforms-as-virtual-software-agencies-c47cb7a6]]. Its headline finding is a "steep production-readiness cliff, where no platform scores above 60% on engineering quality" alongside "frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure" and "no platform exceeding 65% Security Score."

> A steep production-readiness cliff, where no platform scores above 60% on engineering quality. Widespread security and infrastructure failures, with no platform exceeding 65% Security Score.

## Parallel-agents at scale and the managed-agents architecture (added 2026-05-22)

The parallel-subagents primitive now has its most concrete published case study. Anthropic ran an agent team where "multiple Claude instances work in parallel on a shared codebase without active human intervention" to build a Rust C compiler, and report hard scale numbers: "over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V [...] 2 billion input tokens and 140 million output tokens across two weeks" [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]. Two harness insights stand out. First, time-blindness mitigation: "Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress," so the harness prints progress infrequently and defaults to a 1%/10% sampled test run [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]. Second, the monolithic-task problem: parallelism is trivial when there are many independent failing tests, but "compiling the Linux kernel is one giant task" — the fix was "to use GCC as an online known-good compiler oracle to compare against," decomposing the monolith into per-file work each agent could take in parallel [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]. This is direct evidence for Simon Willison's earlier framing that subagents' payoff is context preservation plus specialization, not just raw parallelism — here "one agent was tasked with coalescing any duplicate code [...] another [...] improving the performance of the compiler itself" [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]].

> Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V. The project consumed 2 billion input tokens and generated 140 million output tokens across two weeks.

> When agents started to compile the Linux kernel, they got stuck. Unlike a test suite with hundreds of independent tests, compiling the Linux kernel is one giant task. The fix was to use GCC as an online known-good compiler oracle to compare against. This let each agent work in parallel, fixing different bugs in different files, until Claude's compiler could eventually compile all files.

The harness layer itself is being abstracted. Anthropic's Managed Agents design decouples "the brain from the hands," making each hand a tool behind "a simple interface (execute(name, input) -> string) that supports any custom tool, any MCP server, and their own tools" [[scaling-managed-agents-decoupling-the-brain-from-the-hands-8537165d]]. The architectural payoff is substrate-independence — "the harness doesn't know whether the sandbox is a container, a phone, or a Pokemon emulator, and because no hand is coupled to any brain, brains can pass hands to one another" — and the harness becomes the locus of prompt-cache optimization: "fetched events can be transformed in the harness before being passed to Claude's context window, with transformations including context organization for prompt cache hit rate" [[scaling-managed-agents-decoupling-the-brain-from-the-hands-8537165d]]. This is the hosted-execution counterpart to the Claude Agent SDK already covered on this page.

> Decoupling the brain from the hands makes each hand a tool, with a simple interface (execute(name, input) -> string) that supports any custom tool, any MCP server, and their own tools. The harness doesn't know whether the sandbox is a container, a phone, or a Pokemon emulator, and because no hand is coupled to any brain, brains can pass hands to one another.

## Skills, measured; and the next wave of eval benchmarks (added 2026-05-22)

The Skills primitive now has empirical evidence rather than only design framing. SkillsBench evaluates 86 tasks across 11 domains under no-Skills / curated-Skills / self-generated-Skills conditions over 7,308 trajectories, finding curated Skills "raise average pass rate by 16.2 percentage points, but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas" [[skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks-1743f5a5]]. Two findings cut against optimistic Skills framing: "self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming," and "focused Skills with 2-3 modules outperform comprehensive documentation" [[skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks-1743f5a5]]. The +4.5pp software-engineering figure is notably the smallest domain gain, tempering the wiki's prior framing of Skills (per Anthropic and Simon Willison) as a broad productivity win for coding.

> Curated Skills raise average pass rate by 16.2 percentage points (pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming.

The eval-harness landscape continues to fragment past single-issue resolution. SWE-Chain measures multi-step package upgrades — "12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements, where each transition builds on the agent's prior codebase" — reporting a *public* leaderboard number with Claude-Opus-4.7 (Claude Code) at "60.8% resolving, 80.6% precision, and 68.5% F1" [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]. This public Opus-4.7 figure is useful as a methodology-disclosed contrast to the partner-internal Rakuten-SWE-Bench '3x' claim already disputed on this page. SWE-Cycle adds the full-lifecycle axis — "the first benchmark evaluating agents across the complete issue resolution lifecycle [...] 489 high-quality instances [...] both Isolated Task evaluation and a FullCycle setting" — and, more pointedly, introduces SWE-Judge, an LLM-based eval protocol whose central claim is that "even within Isolated Tasks, traditional deterministic script evaluation produces severe misjudgments and false signals" [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]. That escalates the eval-realism debate from "the tasks are unrealistic" (benchmark-mutation, SWE-WebDevBench) to "the *scoring mechanism itself* is unreliable."

> SWE-Chain contains 12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements, where each transition builds on the agent's prior codebase. Claude-Opus-4.7 (Claude Code) leads at 60.8% resolving, 80.6% precision, and 68.5% F1.

> A major innovation of this work is the introduction of SWE-Judge, an evaluation methodology. Even within Isolated Tasks, traditional deterministic script evaluation produces severe misjudgments and false signals, while SWE-Judge provides a reliable assessment protocol across all four SWE-Cycle tasks and is strongly validated against human annotations.

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
- [[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]] claims OS-level sandboxing (bubblewrap/seatbelt + network proxy) reduces permission prompts by 84% and contains prompt-injected agents from exfiltration; [[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]] claims attack success rates exceed 85% against state-of-the-art defenses with adaptive strategies and that tool outputs are trusted at system-instruction level — so the sandbox bounds blast radius but does not address the underlying trust-level confusion the SoK identifies as the root cause. Status: unresolved
- [[swe-webdevbench-evaluating-coding-agent-application-platforms-as-virtual-software-agencies-c47cb7a6]] claims no app-generation platform scores above 60% on engineering quality (a 'production-readiness cliff'); [[2026-agentic-coding-trends-report-27fe0474]] claims 2026 is the era where development shifts to orchestrating agents that write code, implying production-grade output is increasingly delegable. The two are in tension on how production-ready autonomous full-stack output actually is. Status: unresolved
- [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] claims that even on isolated tasks, traditional deterministic pass/fail script evaluation "produces severe misjudgments and false signals" and proposes SWE-Judge (LLM-based, human-validated) as a corrective; [[swe-bench-verified-overview-and-bash-only-methodology-52afb0a4]] presents deterministic test-patch scoring as the trusted, annotator-reviewed gold standard for coding-agent capability — so the two disagree on whether deterministic scripts are sufficient as the scoring mechanism. Status: unresolved
- [[skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks-1743f5a5]] claims curated Skills add only +4.5pp on Software Engineering tasks (vs +51.9pp Healthcare) and that 16 of 84 tasks show negative deltas, while self-generated Skills give no average benefit; [[introducing-agent-skills-anthropic-5fb2ccf0]] and [[claude-skills-are-awesome-maybe-a-bigger-deal-than-mcp-simon-willison-7efc395e]] frame Skills as a broadly valuable, possibly MCP-superseding productivity primitive for coding. Status: unresolved
- [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]] claims (public), methodology-disclosed Claude-Opus-4.7 (Claude Code) score of 60.8% resolving on chained package upgrades; [[introducing-claude-opus-4-7-b8af8104]] reports a partner-internal Rakuten-SWE-Bench '3x more production tasks than Opus 4.6' with undisclosed composition — the public SWE-Chain number is the kind of disclosed baseline the Rakuten claim lacks, but the two benchmarks are not directly comparable. Status: unresolved

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
- [ ] Does Claude Code's OS-level sandbox [[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]] compose with Claude Code Routines' Anthropic-managed cloud infra [[automate-work-with-routines-claude-code-routines-docs-d09f612e]] — i.e. is the cloud routine sandbox the same bubblewrap/proxy model, or a different containerization tier?
- [ ] Cursor's per-model tool alignment for Codex (renaming tools to rg-style shell equivalents, Responses-API reasoning capture) [[improving-cursor-s-agent-for-openai-codex-models-cursor-blog-a876aa9c]] suggests the cross-vendor subagent/tool 'convergence' is shallow at the API surface — is there any published measurement of how much harness-level per-model tuning moves SWE-bench/Terminal-Bench scores independent of the base model?
- [ ] Does CursorBench [[continually-improving-our-agent-harness-cursor-blog-173ad132]] pin infrastructure/resource configuration, given that [[quantifying-infrastructure-noise-in-agentic-coding-evals-anthropic-engineering-c78d84ac]] showed several-percent score swings from config alone?
- [ ] Cursor's automated Split PRs flow [[cursor-changelog-pr-review-build-plan-in-parallel-and-split-prs-may-7-2026-29f64665]] proposes independent PRs from chat context — how does it detect cross-slice dependencies, and what is the false-independence rate (slices marked independent that actually conflict on merge)?
- [ ] Does SWE-WebDevBench's frontend-backend decoupling finding [[swe-webdevbench-evaluating-coding-agent-application-platforms-as-virtual-software-agencies-c47cb7a6]] persist under the autonomous three-agent planner/generator/evaluator harness [[harness-design-for-long-running-application-development-anthropic-engineering-9fa759b7]], or is the decoupling an artifact of single-pass app-platform generation?
- [ ] Does the C-compiler agent-team result [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]] generalize beyond the unusual property that a known-good oracle (GCC) existed to decompose the monolithic compile task — i.e. how do you parallelize a monolithic task with no oracle to diff against?
- [ ] What is the per-completed-task cost delta between the Managed Agents brain/hands-decoupled architecture [[scaling-managed-agents-decoupling-the-brain-from-the-hands-8537165d]] and a coupled single-session harness, given the extra event-transformation layer it inserts before context?
- [ ] SkillsBench finds self-generated Skills provide no average benefit [[skillsbench-benchmarking-how-well-agent-skills-work-across-diverse-tasks-1743f5a5]]; does this contradict the Agentic Harness Engineering claim that an evolution agent can productively edit its own skills/sub-agents [[agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-agent-harnesses-56d6e4c6]], or is AHE's human-in-the-loop observability the missing ingredient?
- [ ] Does SWE-Judge's LLM-based scoring [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] introduce model-family bias (does an LLM judge score agents using the same base model more favorably), and is that bias measured against the human-annotation validation set?
- [ ] How does Claude-Opus-4.7's 60.8% on SWE-Chain [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]] degrade across the chain length — is the per-transition success rate roughly constant, or does error accumulate so that long chains collapse?

## See also

- [purpose](purpose.md)
