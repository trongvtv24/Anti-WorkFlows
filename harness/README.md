# AWF Harness Layer

This folder is the reusable artifact and intake layer inside AntiWF_FIN.

AntiWF runs the workflows and skills. The harness defines the durable project
artifacts that keep feature work traceable:

- `FEATURE_INTAKE.md`: classify user intent before implementation.
- `ARCHITECTURE.md`: stack-neutral architecture discovery and boundary rules.
- `TEST_MATRIX.md`: behavior-to-proof control panel.
- `templates/`: spec intake, story, decision, validation, and high-risk story
  templates.

## Operating Rule

Large or risky work should not go straight from prompt to code. Route it through:

```text
/intake -> /plan -> /story -> /design -> /code -> /test -> /proof -> /audit
```

Tiny work may patch directly, but product docs, story evidence, and proof rows
must stay current when product truth changes.

