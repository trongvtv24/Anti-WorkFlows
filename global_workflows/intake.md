---
description: Classify user intent before planning or code
# AWF_METADATA_START
type: workflow
name: "intake"
command: "/intake"
awf_version: "4.0.0"
workflow_version: "1.0.0"
status: active
category: "planning"
risk_level: "low"
triggers:
  - "/intake"
  - "feature intake"
  - "classify request"
  - "risk lane"
inputs:
  - "user_request"
  - "project_context"
outputs:
  - "intake_result"
reads:
  - "awf_manifest.yaml"
  - "global_workflows/GLOBAL_SAFETY_TRUTHFULNESS_GATE.md"
  - "harness/FEATURE_INTAKE.md"
writes:
  - "docs/stories/backlog.md"
  - "harness/TEST_MATRIX.md"
required_gates:
  - "global_safety_truthfulness_gate"
skill_hooks:
  required:
    - "harness-feature-intake"
  conditional:
    - "prompt-optimizer"
handoff:
  next_workflows:
    - "/brainstorm"
    - "/plan"
    - "/story"
# AWF_METADATA_END
---

# WORKFLOW: /intake - Harness Feature Intake

## Purpose

Classify incoming work before planning or code. The output is a small intake
result that says whether the task is tiny, normal, or high-risk, and which
artifact should be created next.

## Required Reading

1. `harness/FEATURE_INTAKE.md`
2. `global_workflows/GLOBAL_SAFETY_TRUTHFULNESS_GATE.md`
3. Existing `docs/product/`, `docs/stories/`, and `harness/TEST_MATRIX.md` when
   present in the target project.

## Steps

1. Identify input type: new spec, spec slice, change request, new initiative,
   maintenance request, or harness improvement.
2. Restate the work item in one sentence.
3. Run the risk checklist from `harness/FEATURE_INTAKE.md`.
4. Choose lane:
   - tiny: patch directly, keep docs current.
   - normal: create or update a story packet.
   - high-risk: create the high-risk story folder and ask for confirmation if
     direction is ambiguous.
5. Name affected product docs and proof layers.
6. Hand off to `/plan`, `/story`, or `/brainstorm`.

## Output Format

```text
Lane: normal
Input type: change request
Reason: touches API contract and weak proof.
Docs: docs/product/api.md
Story: docs/stories/epics/E01-api/US-003-update-response-envelope.md
Validation: unit, integration, E2E
Next workflow: /story
```

