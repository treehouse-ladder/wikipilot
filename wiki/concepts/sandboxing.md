---
title: "Sandboxing (agentic coding)"
kind: concept
sources:
  - "[[how-we-contain-claude-across-products-64af1d1a]]"
  - "[[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]]"
  - "[[cursor-2-0-multi-agents-and-composer-changelog-4665f068]]"
  - "[[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]]"
  - "[[ai-agents-may-always-fall-for-prompt-injections-ad0e4e5e]]"
  - "[[build-2026-furthering-windows-as-the-trusted-platform-for-development-0e85a5a9]]"
  - "[[windows-platform-security-for-ai-agents-83834df9]]"
  - "[[sandlock-confining-ai-agent-code-with-unprivileged-linux-primitives-6c9c9e93]]"
last_updated: 2026-06-06
last_verified: 2026-06-04
freshness_window_days: 30
---

# Sandboxing (agentic coding)

## Summary

Sandboxing in agentic coding is the practice of constraining where and how an agent can act by applying OS-level defenses to the environment in which the agent runs. The containment layer uses process sandboxes, VMs, filesystem boundaries, and egress controls to establish a hard ceiling on blast radius, enabling agents to run with fewer manual approval prompts while limiting the damage any single compromised action can cause [[how-we-contain-claude-across-products-64af1d1a]].

Anthropic's Claude Code sandboxing implementation enforces two primary boundaries — filesystem isolation and network isolation — built on top of OS primitives such as Linux bubblewrap and macOS seatbelt [[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]]. Network egress is gated through a unix domain socket connected to a proxy server running outside the sandbox. This architecture safely reduced permission prompts by 84% in Claude Code by moving from per-action approval to environment-level containment.

> When building containment and defense systems, Anthropic applies defenses to the environment in which the agent runs, constraining where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls.

Cursor's sandboxed terminals on macOS moved from opt-in to default behavior in Cursor 2.0 (October 2025) [[cursor-2-0-multi-agents-and-composer-changelog-4665f068]], signaling industry-wide convergence on sandboxing as the baseline safety posture for agent-issued shell commands.

## Containment as the structural answer to approval fatigue (2026-06-01)

Anthropic's [[how-we-contain-claude-across-products-64af1d1a]] frames containment (sandboxes, VMs, filesystem boundaries, egress controls) as the only durable answer to the **approval-fatigue problem** they measured in Claude Code telemetry.

> Telemetry showed users approved roughly 93% of permission prompts, and the more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision.

Auto mode's two-stage defense (input-layer prompt-injection probe + Sonnet 4.6 transcript classifier with fast single-token filter + chain-of-thought only on flagged transcripts) is positioned as a substitute for the human approver — but only because containment puts a hard ceiling on the blast radius.

> When building containment and defense systems, Anthropic applies defenses to the environment in which the agent runs, constraining where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls.

The post also discloses three responsibly-disclosed Claude Code vulnerabilities (mid-2025 to January 2026) that executed code before user consent, and a February 2026 internal red-team that successfully phished an Anthropic employee into launching Claude Code with a malicious prompt — concrete evidence that the input-layer defense alone is insufficient.

## Limitations and the trust-level problem

While sandboxing bounds blast radius, it does not address the underlying **trust-level confusion** identified in systematic prompt-injection research. A meta-analysis of 78 studies found that attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are employed, with tool outputs being treated as trusted instructions at the same level as system instructions [[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]].

> A meta-analysis of 78 recent studies from 2021-2026 found that attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are employed.

A theoretical analysis argues this is not merely an engineering gap but a fundamental trade-off: the prevailing defense paradigm of data-instruction separation both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior, because "an adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows" [[ai-agents-may-always-fall-for-prompt-injections-ad0e4e5e]].

> We argue that the prevailing defense paradigm of data-instruction separation both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. An adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows.

This means OS-level sandboxing is best understood as blast-radius containment rather than a complete security solution — it prevents exfiltration and limits filesystem damage, but it does not prevent an agent from being induced to run a malicious local payload that respects the sandbox boundary.

## OS-level agent principals and kernel-enforced containment (Build 2026)

At Build 2026 (June 2), Microsoft announced two Windows platform changes that extend sandboxing to the OS level. **Microsoft Execution Containers (MXC)** is "a policy-driven execution layer that lets developers declare what an agent can access (e.g., files, network) with containment boundaries enforced at runtime" [[build-2026-furthering-windows-as-the-trusted-platform-for-development-0e85a5a9]]. The isolation semantics are described as "dynamically composable based on intent and risk" — distinct from the fixed per-process sandboxes used by Claude Code and Cursor.

> Microsoft Execution Containers (MXC) is a policy-driven execution layer that lets developers declare what an agent can access (e.g., files, network) with containment boundaries enforced at runtime.

The deeper architectural change is **agent-as-OS-principal**: "Windows now treats AI agents as first-class principals with their own identity, distinct from the human user, so that the OS can enforce capability boundaries and audit who—or what—performed an action" [[windows-platform-security-for-ai-agents-83834df9]]. Agent identities are issued and revoked through Microsoft Entra ID and scoped per-agent, per-session.

> Windows now treats AI agents as first-class principals with their own identity, distinct from the human user, so that the OS can enforce capability boundaries and audit who—or what—performed an action. Agent identities are issued and revoked through Microsoft Entra ID and are scoped per-agent, per-session.

This is a principle-level OS change that addresses trust-level confusion at the OS layer rather than the application layer. Microsoft's marketing implies a stronger guarantee than the Contextual Integrity impossibility result permits — MXC can bound blast radius and attribute actions to agent identities, but whether it can reliably distinguish injected from legitimate flows in the presence of an adversary who can always construct a context where a blocked flow appears legitimate remains an open question (filed on [[agentic-coding]]).

## Open questions

- [ ] What's the false-negative rate of the Sonnet 4.6 transcript classifier on adversarial inputs designed by red teams? (Not disclosed.)
- [ ] Does sandboxing compose cleanly with cloud-execution platforms (Claude Code Routines, Cursor Automations, Antigravity Managed Agents), or do those environments require a different containment model?
- [ ] How do the disclosed Claude Code vulnerabilities (code execution before user consent) relate to the sandbox boundary — were they sandbox escapes or pre-sandbox execution?
- [ ] Does Microsoft MXC's declarative containment policy compose with Claude Code's bubblewrap/seatbelt sandbox when Claude Code runs on Windows — superset or parallel layer requiring dual configuration?
- [ ] Does Windows' agent-as-OS-principal identity model propagate into the agent's audit trail well enough to make agent-attributable security regressions traceable post-hoc?
- [ ] Does MXC defeat the Contextual Integrity impossibility result, or is it purely blast-radius containment with better attribution?

## See also

- [[agentic-coding]]
- [[agent-sandboxing]]
- [[prompt-injection-attacks-on-agentic-coding-assistants-a-systematic-analysis-of-vulnerabilities-in-skills-tools-and-protocol-ecosystems-300ff8a5]]
- [[making-claude-code-more-secure-and-autonomous-anthropic-engineering-c765441e]]
