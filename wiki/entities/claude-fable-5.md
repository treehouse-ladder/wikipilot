---
title: "Claude Fable 5"
kind: entity
sources: ["[[claude-fable-5-and-claude-mythos-5-e11fcea9]]", "[[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]", "[[claude-fable-5-the-first-public-mythos-class-model-672c92f6]]", "[[claude-fable-5-intelligence-performance-price-analysis-ceeaabf7]]", "[[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]", "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]", "[[announcing-aa-briefcase-a-frontier-knowledge-work-evaluation-9a51826e]]", "[[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]", "[[redeploying-claude-fable-5-fdd9745e]]", "[[commerce-department-gives-green-light-for-anthropic-to-bring-back-fable-5-e657d00f]]", "[[more-details-on-fable-5-s-cyber-safeguards-and-our-jailbreak-framework-aaef033d]]", "[[sqlite-utils-4-0rc2-mostly-written-by-claude-fable-for-about-149-25-e673d7b5]]"]
last_updated: 2026-07-08
last_verified: 2026-07-08
freshness_window_days: 30
input_cost_per_mtoken: 10.00
output_cost_per_mtoken: 50.00
cost_source: "[[claude-fable-5-and-claude-mythos-5-e11fcea9]]"
aa_intelligence_index: 60
aa_intelligence_index_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
gdpval_aa_elo: 1818
gdpval_aa_elo_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Claude Fable 5 is Anthropic's first publicly available Mythos-class model, released June 9, 2026 — positioned a tier above Claude Opus 4.8 [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. It debuted at #1 on the Artificial Analysis Intelligence Index at 64.9, roughly 5 points ahead of GPT-5.5 [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]]. It also leads GDPval-AA at 1932 Elo and scores 80.3% on SWE-bench Pro — 11 points clear of Opus 4.8 (69.2%) and more than 20 points clear of GPT-5.5 (58.6%) [[claude-fable-5-the-first-public-mythos-class-model-672c92f6]]. Pricing is $10/$50 per Mtoken — exactly 2× Opus 4.8 — with the 90% input-token caching discount preserved [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. The model is available on the Claude API, AWS Bedrock, Vertex AI, and Microsoft Foundry; paid Claude subscribers got free access during June 9–22 in Claude Code via `/model fable`.

> Today, we are launching Claude Fable 5, a Mythos-class model that we've made safe for general use, with capabilities that exceed those of any model we've ever made generally available. Claude Fable 5 is priced at $10 per million input tokens and $50 per million output tokens.

> Claude Fable 5 takes the #1 position on the Artificial Analysis Intelligence Index, scoring 64.9 and setting the highest score on 5 of the 10 underlying benchmarks. Claude Fable 5 scores 1932 on GDPval-AA.

> On SWE-bench Pro, Fable 5 scores 80.3%, an 11-point lead over Opus 4.8 (69.2%) and more than 20 points ahead of GPT-5.5 (58.6%) and Gemini 3.1 Pro (54.2%).

Safety routing: queries in cybersecurity and biology domains are automatically routed to Opus 4.8 in the public Fable 5 deployment [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. The unrestricted underlying model — **Claude Mythos 5** — is available only to vetted cyberdefenders and infrastructure providers via Project Glasswing.

> For a small group of cyberdefenders and infrastructure providers, we are also launching Claude Mythos 5, the same underlying model as Fable 5 but with safeguards lifted in some areas.

**Access suspended June 12, 2026; Mythos 5 partially restored June 26 for US critical infrastructure; Fable 5 restored globally July 1, 2026.** The US Commerce Department issued an export control directive on June 12 requiring Anthropic to disable Claude Fable 5 globally. Anthropic complied immediately, citing inability to reliably exclude foreign nationals from its user base. The stated trigger was a reported narrow jailbreak (asking the model to read a codebase for vulnerability fixes) — Anthropic publicly disputes this justification [[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]. On **June 26, 2026**, Commerce Secretary Howard Lutnick partially lifted the export control via letter to Anthropic co-founder Tom Brown, allowing **Claude Mythos 5** (the unrestricted, safeguard-free variant) to be deployed without an export license to a defined set of US organizations operating and defending critical infrastructure [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]. **On July 1, 2026, the Commerce Department fully lifted the export controls** and Fable 5 resumed globally on Claude Platform, Claude.ai, Claude Code, and Claude Cowork [[redeploying-claude-fable-5-fdd9745e]] [[commerce-department-gives-green-light-for-anthropic-to-bring-back-fable-5-e657d00f]]. The restoration came with an upgraded safety classifier that blocks the Amazon-reported vulnerability-disclosure technique in >99% of cases; flagged requests are rerouted to Opus 4.8 with user notification. Pro/Max/Team/Enterprise plans get Fable 5 for up to 50% of weekly usage limits through July 7, reverting to usage-credit billing thereafter. AWS, Google Cloud, and Microsoft Foundry re-enablement is pending.

> Anthropic received the directive from the government on June 12, 2026 at 5:21pm ET... Anthropic is complying with the government's legal directive and is removing access to Fable 5 and Mythos 5 for all users.

> Claude Fable 5 (with fallback) leads at 60 but is currently unavailable [on the Artificial Analysis Intelligence Index v4.1].

> Claude Fable 5 with fallback scored 1818 [on GDPval-AA v2] but is currently unavailable.

> Commerce Secretary Howard Lutnick partially lifted the Anthropic export control on June 26, allowing Claude Mythos 5 to be deployed without an export license to a defined set of U.S. organizations operating and defending critical infrastructure, following a June 26 letter to Anthropic co-founder Tom Brown. [[claude-fable-5-still-offline-as-us-clears-mythos-5-for-critical-infrastructure-7a5ed327]]

> As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted. Fable 5 will be available starting tomorrow, Wednesday, July 1, to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork. [[redeploying-claude-fable-5-fdd9745e]]

> Working closely with the government, we trained an improved safety classifier that targets and blocks the behavior described in the report. Users will be notified if a request to Fable 5 is blocked, and the request will instead be sent to Opus 4.8. The new classifier means that the specific technique described in the Amazon report is blocked in over 99% of cases. [[redeploying-claude-fable-5-fdd9745e]]

**AA-Briefcase leadership.** Fable 5 leads the new AA-Briefcase multi-week agentic knowledge-work benchmark — a long-horizon evaluation with linked tasks, thousands of input files, and deliverables (spreadsheets, presentations, memos) graded on analytical quality and presentation [[announcing-aa-briefcase-a-frontier-knowledge-work-evaluation-9a51826e]]. However, Fable 5 is one of the highest token users at ~139k output tokens per task — reinforcing the verbosity-as-cost-multiplier caveat for long-horizon agentic loops.

> AA-Briefcase is a new frontier agentic evaluation measuring how well AI models perform realistic, long-horizon knowledge work across multi-week scenarios. Claude Fable 5 leads the benchmark and is one of the highest token users, averaging 139k output tokens per task.

**Redeployed July 1, 2026 — export controls lifted June 30.** The US Commerce Department export controls on Fable 5 (and Mythos 5) were lifted June 30, 2026, and Fable 5 returned globally on July 1 across the Claude Platform, Claude.ai, Claude Code, and Claude Cowork — ending the June 12 global suspension [[redeploying-claude-fable-5-fdd9745e]]. Availability terms: for Pro, Max, Team and select Enterprise plans, Fable 5 is included for up to 50% of weekly usage limits through July 7, then reverts to usage credits at the unchanged $10/$50 per Mtoken list price [[redeploying-claude-fable-5-fdd9745e]]. With Fable 5 accessible again at AA Intelligence Index v4.1 = 60, it re-takes the publicly-accessible aggregate-intelligence #1 from Opus 4.8 (56). Anthropic's redeployment testing found the triggering vulnerability-identification jailbreak was not unique to Fable 5 — many less capable models identified the same vulnerabilities — and it is proposing an industry jailbreak-severity framework (narrow vs universal) with Amazon, Microsoft, Google and other Glasswing partners [[redeploying-claude-fable-5-fdd9745e]] [[more-details-on-fable-5-s-cyber-safeguards-and-our-jailbreak-framework-aaef033d]].

> As of June 30, the export controls on Fable 5 and Mythos 5 have been lifted. Fable 5 will be available starting July 1 to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork. [[redeploying-claude-fable-5-fdd9745e]]

**Real-world agentic-coding cost data point (July 2026): ~$149.25 to mostly-write sqlite-utils 4.0rc2, surfacing five release blockers.** Simon Willison used Claude Fable 5 to drive sqlite-utils toward its 4.0 stable release, with the model authoring most of the 4.0rc2 work for about $149.25 and flagging five significant problems he had not spotted himself, categorized as release blockers [[sqlite-utils-4-0rc2-mostly-written-by-claude-fable-for-about-149-25-e673d7b5]]. This is a disclosed-cost, single-maintainer field data point on the cost/quality tradeoff for a real open-source library release — framing Fable 5's value as verification and review (finding blockers a human missed) as much as raw code generation.

> Fable identified some significant problems I hadn't spotted myself — five that it categorized as release blockers. [[sqlite-utils-4-0rc2-mostly-written-by-claude-fable-for-about-149-25-e673d7b5]]

> Claude Opus 4.8 (max, 56) is the most intelligent available model according to the Artificial Analysis Intelligence Index v4.1. Claude Fable 5 (with fallback) leads at 60 but is currently unavailable; GPT-5.5 (xhigh) scores 55. [[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]

> GDPval-AA v2 is the highest weighted evaluation in the Intelligence Index v4.1. Claude Opus 4.8 scored 1638 on GDPval-AA v2, the highest among available models (Claude Fable 5 with fallback scored 1818 but is currently unavailable; GPT-5.5 xhigh scored 1531). [[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]

## Open questions

- [ ] What is Fable 5's score on CyberGym and ARC-AGI-2 given the cyber/bio routing to Opus 4.8 — are those benchmarks even runnable on the public Fable 5 endpoint?
- [ ] Is the AA Intelligence Index score 64.9 (article text) or 65 (model card)? Reconciliation needed for the comparison page.
- [x] Will Fable 5 return to general availability, and on what timeline? Anthropic says it is 'working to restore access' but provides no timeline [[statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos-5-00131728]]. **Resolved 2026-07-01:** Export controls fully lifted; Fable 5 restored globally on July 1 [[redeploying-claude-fable-5-fdd9745e]].
- [ ] Does the new safety classifier's Opus 4.8 fallback affect Fable 5's published benchmark scores (AA Intelligence Index, GDPval-AA, SWE-bench Pro) — are those scores from the pre-classifier version or the now-live routed version? [[redeploying-claude-fable-5-fdd9745e]]
- [ ] At $149.25 for a single maintainer's RC work [[sqlite-utils-4-0rc2-mostly-written-by-claude-fable-for-about-149-25-e673d7b5]], what is the cost per merged PR or per release for a solo open-source maintainer using Fable 5 at the $10/$50 per Mtoken list price — and how does that compare with Opus 4.8 ($5/$25) for the same quality of output on similarly-scoped tasks?

## See also

- [[frontier-models]]
- [[claude-opus-4.8]]
- [[claude-mythos-preview]]
