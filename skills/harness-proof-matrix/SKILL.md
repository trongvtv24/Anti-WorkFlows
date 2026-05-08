---
name: harness-proof-matrix
description: >
  Maintain the behavior-to-proof matrix and validation reports so implemented
  claims are backed by commands, logs, screenshots, or report artifacts.
version: 1.0.0
# AWF_METADATA_START
type: skill
name: "harness-proof-matrix"
skill_version: "1.0.0"
status: active
category: "quality"
activation: "conditional"
priority: "high"
risk_level: "low"
allowed_side_effects:
  - "write_validation_report_after_request"
requires_confirmation: false
related_workflows:
  - "/proof"
  - "/test"
  - "/audit"
required_gates:
  - "global_safety_truthfulness_gate"
# AWF_METADATA_END
---

# Harness Proof Matrix

## Purpose

Update `docs/TEST_MATRIX.md` or seed it from `harness/TEST_MATRIX.md` after
validation. The matrix records what proof exists and what risk remains.

## Procedure

1. Read the active story packet.
2. Collect exact commands and artifact paths.
3. Mark proof columns as yes, no, partial, or not applicable.
4. Link evidence.
5. Keep status below `implemented` until proof exists.

## Evidence Standards

- Command output must be from the current session.
- Screenshots or reports must have stable file paths.
- Missing proof must stay visible as a gap.

