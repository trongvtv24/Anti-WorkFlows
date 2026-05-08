---
name: harness-story-writer
description: >
  Create or update story packets from harness templates so feature work has a
  product contract, acceptance criteria, validation plan, and evidence section.
version: 1.0.0
# AWF_METADATA_START
type: skill
name: "harness-story-writer"
skill_version: "1.0.0"
status: active
category: "planning"
activation: "conditional"
priority: "high"
risk_level: "medium"
allowed_side_effects:
  - "write_story_after_request"
requires_confirmation: false
related_workflows:
  - "/story"
  - "/plan"
  - "/code"
required_gates:
  - "global_safety_truthfulness_gate"
# AWF_METADATA_END
---

# Harness Story Writer

## Purpose

Use harness templates to turn accepted work into durable story packets before
implementation.

## Procedure

1. Use `harness/templates/story.md` for normal work.
2. Use all files under `harness/templates/high-risk-story/` for high-risk work.
3. Link product docs and decisions.
4. Keep acceptance criteria observable.
5. Keep validation expectations explicit.
6. Leave evidence empty until proof exists.

## Required Story Sections

- Status
- Lane
- Product Contract
- Acceptance Criteria
- Validation
- Harness Delta
- Evidence

