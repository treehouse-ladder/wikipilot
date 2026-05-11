---
title: "Transformer attention"
kind: concept
sources:
  - "[[example-paper-aabbccdd]]"
last_updated: 2026-05-10
last_verified: 2026-05-10
freshness_window_days: 30
---

# Transformer attention

## Summary

Attention computes a weighted sum of value vectors using key-query similarity [[example-paper-aabbccdd]]. The original formulation scales by sqrt(d_k) [[example-paper-aabbccdd]].

> "Attention is a weighted sum of value vectors where the weights are derived from the similarity of queries to keys."

## Disputes

- [[example-paper-aabbccdd]] claims sqrt(d_k) scaling is necessary; [[another-source-deadbeef]] claims not-needed for small models. Status: unresolved

## Open questions

- [ ] How does attention behave with FP8 precision in agentic loops?

## See also

- [[ai-agents]]
