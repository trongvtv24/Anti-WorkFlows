---
name: harness-feature-intake
description: >
  Classify user requests into tiny, normal, or high-risk lanes before planning
  or implementation. Use with /intake and before large feature work.
version: 1.0.0
# AWF_METADATA_START
type: skill
name: "harness-feature-intake"
skill_version: "1.0.0"
status: active
category: "planning"
activation: "conditional"
priority: "high"
risk_level: "low"
allowed_side_effects:
  - "none"
requires_confirmation: false
related_workflows:
  - "/intake"
  - "/plan"
  - "/code"
required_gates:
  - "global_safety_truthfulness_gate"
# AWF_METADATA_END
---

# Harness Feature Intake

## Purpose

Apply `harness/FEATURE_INTAKE.md` before implementation. The skill decides the
work lane and the next durable artifact.

## Procedure

1. Classify input type.
2. Restate the work item.
3. Count risk flags.
4. Choose tiny, normal, or high-risk lane.
5. Name affected product docs, story path, validation layers, and next workflow.

## Output

```text
Lane:
Input type:
Risk flags:
Reason:
Docs:
Story:
Validation:
Next workflow:
```

