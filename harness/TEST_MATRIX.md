# Test Matrix

This file maps product behavior to proof.

Do not mark a row implemented until validation evidence exists.

## Status Values

| Status | Meaning |
| --- | --- |
| planned | Accepted intended behavior, not implemented |
| in_progress | Actively being built |
| implemented | Implemented and proof exists |
| changed | Contract changed after earlier implementation |
| retired | No longer part of the product contract |

## Matrix

| Story | Contract | Unit | Integration | E2E | Platform | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TBD | Add rows when story packets are created | no | no | no | no | planned | none |

## Evidence Rules

- Unit proof covers pure domain and application rules.
- Integration proof covers backend enforcement, data integrity, providers, jobs,
  or service contracts.
- E2E proof covers user-visible flows.
- Platform proof covers shell, deployment, mobile, desktop, or runtime behavior
  that cannot be proven lower down.
- A story can omit a proof column only if the story explains why.

