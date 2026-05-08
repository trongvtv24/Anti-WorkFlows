# Architecture Harness

No application stack should be assumed before a user-provided spec or current
repo evidence supports it.

## Discovery Before Shape

Before proposing implementation shape, identify:

- Product surfaces: browser, mobile, desktop, CLI, API, worker, or service.
- Runtime stack: language, framework, database, queues, providers, hosting.
- Core domains: product concepts that deserve stable names and contracts.
- Boundary inputs: requests, webhooks, jobs, files, credentials, provider data.
- Validation ladder: smallest checks that prove the selected stack.

Record stack choices in `docs/decisions/` when they meaningfully constrain
future work.

## Default Layering

```text
domain <- application <- infrastructure <- interface <- app surfaces
```

## Boundary Rule

Unknown data must be parsed at boundaries before it enters inner code:

- HTTP bodies, params, and query strings.
- Session payloads and identity claims.
- Environment variables.
- Database rows from external clients.
- Platform shell payloads.
- Provider webhooks and async events.

Target flow:

```text
unknown input -> parser -> typed DTO or command -> application use case -> domain object
```

## Observability Contract

Future servers should emit one canonical JSON log line per request with:

- timestamp
- level
- request_id
- user_id when known
- action
- duration_ms
- status_code
- message

Audit logs are product records. Application logs are operational records.

