---
fetched_at: 2026-07-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: 2026-07-04
last_verified: 2026-07-04
sha256: 358490a4046e406c079e94ccafccd9a9dea1537d2d047787087c86042ee2efb4
sources: []
title: 'DuneSlide: Two Critical RCE vulnerabilities via Zero-Click Prompt Injection
  in Cursor IDE'
topic: agentic-coding
url: https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/
---

## Excerpts

> Both flaws use the same trick: get the agent to write one file it should not be allowed to write, then use that write to turn the sandbox off. CVE-2026-50548 abuses a setting where the sandbox permits writes into a command's working folder, and that folder is an optional parameter, working_directory, on Cursor's run_terminal_cmd tool. When the agent sets it to a non-default path, Cursor adds that path to the allowed-write list without question. Exploiting either of these critical vulnerabilities allows a threat actor to overwrite critical system files (like the cursorsandbox binary), transforming sandboxed commands into unsandboxed RCE and leading to full system compromise on both the host machine and connected SaaS workspaces. Both bugs are patched in Cursor 3.0, released April 2, and every version before 3.0 is affected.