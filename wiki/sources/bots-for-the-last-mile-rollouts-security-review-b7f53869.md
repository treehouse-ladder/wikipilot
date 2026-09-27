---
fetched_at: &id001 2026-09-27
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: b7f5386936f0c35c94527e3ccf30ed709d5077ffb400f390ceecb31a2695406b
sources: []
title: 'Bots for the last mile: Rollouts, Security Review'
topic: agentic-coding
url: https://cursor.com/blog/rollouts-and-security-reviewer
---

## Excerpts

> Rollouts attaches a monitor to every pull request and watches the change as it deploys, reporting change health per environment: verified healthy, regression detected, or inconclusive.

> When a pull request opens, Rollouts reads the diff and the systems it touches, then writes a monitoring plan as a PR comment.

> Rollouts connects to Origin or GitHub for source control, to your continuous delivery system for deploy events, and to Datadog and other telemetry providers for signals.

> Security Review reads every pull request in the context of the codebase and posts one review comment reporting exploitable bugs.

> Security Review looks for injection across SQL, command, and template surfaces, along with authentication and authorization bypasses, including checks that a refactor stopped running.

> Both are available today on Teams and Enterprise plans.
