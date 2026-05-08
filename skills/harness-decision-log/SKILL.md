---
name: harness-decision-log
description: >
  Create durable decision records for product, architecture, risk, and
  validation choices that affect future work.
version: 1.0.0
# AWF_METADATA_START
type: skill
name: "harness-decision-log"
skill_version: "1.0.0"
status: active
category: "architecture"
activation: "conditional"
priority: "medium"
risk_level: "medium"
allowed_side_effects:
  - "write_decision_after_request"
requires_confirmation: false
related_workflows:
  - "/decision"
  - "/plan"
  - "/design"
  - "/audit"
required_gates:
  - "global_safety_truthfulness_gate"
# AWF_METADATA_END
---

# Harness Decision Log

## Purpose

Use `harness/templates/decision.md` to record decisions that shape future agent
work.

## Procedure

1. State the context and pressure that forced the decision.
2. Separate accepted facts from assumptions.
3. Record alternatives considered.
4. List positive consequences and tradeoffs.
5. Link the related story, product doc, validation report, or prior decision.

## Guardrails

- Do not delete prior decisions silently.
- Mark superseded decisions explicitly.
- Do not weaken validation requirements without user confirmation.

