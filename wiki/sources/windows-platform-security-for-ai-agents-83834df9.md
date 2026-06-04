---
fetched_at: &id001 2026-06-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 83834df9
sources: []
title: "Windows platform security for AI agents"
topic: agentic-coding
url: "https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/"
---

## Excerpts

> Windows now treats AI agents as first-class principals with their own identity, distinct from the human user, so that the OS can enforce capability boundaries and audit who—or what—performed an action. Agent identities are issued and revoked through Microsoft Entra ID and are scoped per-agent, per-session.

> Microsoft Execution Containers (MXC) provide kernel-enforced sandboxing for untrusted model output, plugins, and tools. MXC boots significantly faster than a traditional Hyper-V VM and consumes less memory than an equivalent container when running a typical agent loop, making per-task sandboxing economical at agent-fleet scale.

> Containment policies in MXC are declarative: developers describe what an agent should be able to read, write, or contact, and the kernel enforces those boundaries regardless of how the agent is prompted or what its model decides to do. This is structurally distinct from prompt-level approval gates.

> The Windows Agent Runtime ships in the Dev Channel preview and will reach general availability with Windows 11 25H2. Developers can integrate Agent Identity and MXC through NuGet packages aligned with the Microsoft Agent Framework, OpenAI Agents SDK, LangChain, Semantic Kernel, and Azure AI Foundry.
