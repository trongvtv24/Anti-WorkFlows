---
description: Create harness story packets before implementation
# AWF_METADATA_START
type: workflow
name: "story"
command: "/story"
awf_version: "4.0.0"
workflow_version: "1.0.0"
status: active
category: "planning"
risk_level: "medium"
triggers:
  - "/story"
  - "story packet"
  - "user story"
  - "create story"
inputs:
  - "intake_result"
  - "user_request"
  - "project_context"
outputs:
  - "story_packet"
reads:
  - "awf_manifest.yaml"
  - "global_workflows/GLOBAL_SAFETY_TRUTHFULNESS_GATE.md"
  - "harness/templates/story.md"
  - "harness/templates/high-risk-story/"
writes:
  - "docs/stories/"
  - "docs/product/"
required_gates:
  - "global_safety_truthfulness_gate"
skill_hooks:
  required:
    - "harness-story-writer"
  conditional:
    - "awf-spec-writer"
    - "awf-diagramming"
handoff:
  next_workflows:
    - "/design"
    - "/visualize"
    - "/code"
    - "/proof"
# AWF_METADATA_END
---

# WORKFLOW: /story - Harness Story Packet

## Purpose

Turn accepted work into a durable story packet before implementation. The story
becomes the contract that `/code`, `/test`, `/proof`, and `/audit` check.

## Steps

1. Read the intake result. If none exists, run `/intake` first.
2. Pick the template:
   - normal: `harness/templates/story.md`
   - high-risk: all files under `harness/templates/high-risk-story/`
3. Create the story under `docs/stories/epics/[epic]/`.
4. Link relevant product docs under `docs/product/`.
5. Fill product contract, acceptance criteria, design notes, validation, and
   evidence placeholders.
6. Keep non-goals explicit for high-risk work.
7. Hand off to `/design`, `/visualize`, or `/code`.

## Guardrails

- Do not invent product truth. Use repo-observed facts, user-provided facts, or
  clearly labeled assumptions.
- Do not mark evidence complete before commands are run.
- If the story changes architecture or risk policy, hand off to `/decision`.

