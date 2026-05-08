# Feature Intake

Every implementation prompt enters intake before code changes.

## Intake Flow

```text
User prompt
  -> classify input type
  -> restate as work item
  -> find affected product docs and stories
  -> run risk checklist
  -> choose lane
```

## Input Types

| Type | Use When | Artifact |
| --- | --- | --- |
| New spec | Turning a user-provided spec into project contracts | Spec intake, product docs, candidate epics |
| Spec slice | Implementing selected accepted behavior | Story packet |
| Change request | Fixing or refining accepted behavior | Story packet or direct patch |
| New initiative | Adding a larger area with multiple stories | Initiative note and story packets |
| Maintenance request | Technical, dependency, security, or operational work | Story, validation report, or decision |
| Harness improvement | Improving agent workflow or proof quality | Harness docs or backlog item |

## Lanes

### Tiny

Use for low-risk docs, copy, names, or narrow edits.

Requirements:

- Patch directly.
- Keep affected docs current.
- Run available quick checks.
- Update harness files only if friction was found.

### Normal

Use for story-sized behavior with bounded blast radius.

Requirements:

- Create or update one story file from `harness/templates/story.md`.
- Link relevant product docs.
- Add or update validation expectations.
- Implement the smallest vertical slice.
- Update `docs/TEST_MATRIX.md` or `harness/TEST_MATRIX.md`.

### High-Risk

Use when work can affect security, data, contracts, or multiple platforms.

Requirements:

- Create a story folder from `harness/templates/high-risk-story/`.
- Fill `execplan.md`, `overview.md`, `design.md`, and `validation.md`.
- Ask for human confirmation if direction is ambiguous.
- Record a decision when behavior or architecture changes meaningfully.

## Risk Checklist

| Risk Flag | Applies When Work Touches |
| --- | --- |
| Auth | Login, logout, sessions, JWT, passwords, refresh tokens |
| Authorization | Roles, permissions, tenant or account scope |
| Data model | Schema, migrations, uniqueness, deletion, retention |
| Audit/security | Audit logs, privacy, sensitive data, access logs |
| External systems | Email, payments, cloud, queues, webhooks, provider SDKs |
| Public contracts | API shape, response envelope, client-visible behavior |
| Cross-platform | Desktop, mobile, browser, native shell, deep links |
| Existing behavior | Already implemented or test-covered behavior changes |
| Weak proof | Unclear or missing tests around affected behavior |
| Multi-domain | More than one product domain changes at once |

## Classification

```text
0-1 flags: tiny or normal, based on code impact
2-3 flags: normal with stronger validation
4+ flags: high-risk
hard gate: high-risk unless user explicitly narrows scope
```

Hard gates: auth, authorization, data loss or migration, audit/security,
external provider behavior, and weakening validation requirements.

## Output

At the end of intake, produce:

```text
Lane: normal
Reason: touches API contract and weak proof.
Docs: docs/product/permissions.md
Story: docs/stories/epics/E01-access/US-003-update-role.md
Validation: unit, integration, E2E
```

