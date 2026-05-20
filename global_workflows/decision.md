---
description: Record durable product, architecture, risk, or validation decisions
# AWF_METADATA_START
type: workflow
name: "decision"
command: "/decision"
awf_version: "4.0.0"
workflow_version: "1.0.0"
status: active
category: "architecture"
risk_level: "medium"
triggers:
  - "/decision"
  - "record decision"
  - "architecture decision"
  - "ADR"
inputs:
  - "decision_context"
  - "user_request"
  - "project_context"
outputs:
  - "decision_record"
reads:
  - "awf_manifest.yaml"
  - "global_workflows/GLOBAL_SAFETY_TRUTHFULNESS_GATE.md"
  - "harness/templates/decision.md"
writes:
  - "docs/decisions/"
required_gates:
  - "global_safety_truthfulness_gate"
skill_hooks:
  required:
    - "harness-decision-log"
  conditional:
    - "awf-diagramming"
    - "context-engineering"
handoff:
  next_workflows:
    - "/plan"
    - "/design"
    - "/story"
    - "/code"
# AWF_METADATA_END
---

# WORKFLOW: /decision - Harness Decision Record

## Purpose

Record durable decisions that affect product truth, architecture, risk, or
validation. Decision records keep future agents from re-litigating settled
tradeoffs.

## Skill Activation Contract (Workflow ↔ Skill)

- `harness-decision-log` (required): luôn ghi decision record theo template chuẩn.
- `awf-diagramming` (conditional): bật khi decision cần sơ đồ để làm rõ impact hoặc boundary.
- `context-engineering` (conditional): bật khi context mâu thuẫn hoặc có nhiều nguồn fact cạnh tranh.

Không được kết luận decision nếu còn open question chưa tách riêng.

## Use When

- Architecture direction changes.
- Scope or product behavior changes.
- Validation requirements are added, removed, or weakened.
- A high-risk story chooses between meaningful alternatives.
- A repeated failure pattern leads to a harness rule.

## Steps

1. Read `harness/templates/decision.md`.
2. Separate repo-observed facts, user-provided facts, assumptions, and
   recommendations.
3. Write the decision under `docs/decisions/NNNN-short-title.md`.
4. Link the related story, product doc, or validation report.
5. Hand off to `/plan`, `/design`, `/story`, or `/code`.

## Guardrails

- Do not bury open questions inside accepted decisions.
- Do not weaken validation without explicit user confirmation.
- Mark superseded decisions instead of silently deleting history.
