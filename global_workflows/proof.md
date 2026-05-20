---
description: Map stories and product contracts to validation evidence
# AWF_METADATA_START
type: workflow
name: "proof"
command: "/proof"
awf_version: "4.0.0"
workflow_version: "1.0.0"
status: active
category: "quality"
risk_level: "low"
triggers:
  - "/proof"
  - "test matrix"
  - "validation evidence"
  - "proof status"
inputs:
  - "story_packet"
  - "validation_output"
  - "project_context"
outputs:
  - "proof_matrix_update"
reads:
  - "awf_manifest.yaml"
  - "global_workflows/GLOBAL_SAFETY_TRUTHFULNESS_GATE.md"
  - "harness/TEST_MATRIX.md"
  - "harness/templates/validation-report.md"
writes:
  - "harness/TEST_MATRIX.md"
  - "docs/TEST_MATRIX.md"
  - "reports/validation/*.md"
required_gates:
  - "global_safety_truthfulness_gate"
skill_hooks:
  required:
    - "harness-proof-matrix"
  conditional: []
handoff:
  next_workflows:
    - "/test"
    - "/audit"
    - "/deploy"
# AWF_METADATA_END
---

# WORKFLOW: /proof - Harness Proof Matrix

## Purpose

Connect story claims to real validation evidence. `/proof` prevents "implemented"
from meaning "looks done" without commands, reports, screenshots, or logs.

## Skill Activation Contract (Workflow ↔ Skill)

- `harness-proof-matrix` (required): luôn dùng để map claim → evidence theo matrix chuẩn.

Rule cứng: nếu chưa có command/artifact path thì status phải giữ ở `no|partial`, không được nâng lên `yes`.

## Steps

1. Read the active story packet and acceptance criteria.
2. Read validation output from `/test`, manual smoke checks, browser checks, or
   deployment checks.
3. Update `docs/TEST_MATRIX.md` when the target project owns one; otherwise use
   `harness/TEST_MATRIX.md` as the seed.
4. Write a validation report using `harness/templates/validation-report.md`
   when evidence is non-trivial.
5. Mark each proof column as yes, no, partial, or not applicable.
6. Only mark status `implemented` when evidence is present and linked.

## Evidence Rules

- "PASS" requires the exact command or artifact path.
- "not run" is acceptable, but must stay visible.
- A story can ship with gaps only if the story explains the residual risk.
