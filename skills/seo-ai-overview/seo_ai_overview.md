---
description: "📈 SEO AI Overview end-to-end workflow"
# AWF_METADATA_START
type: workflow
name: "seo_ai_overview"
command: "/seo-ai-overview"
awf_version: "4.0.0"
workflow_version: "1.0.0"
status: active
category: "content"
risk_level: "medium"
triggers:
  - "/seo-ai-overview"
  - "/seo ai overview"
  - "seo ai overview"
  - "ai overview seo"
inputs:
  - "user_request"
  - "project_context"
outputs:
  - "workflow_result"
reads:
  - "awf_manifest.yaml"
writes:
  - "content/seo-ai-overview/*.md"
  - ".brain/claims.md"
required_gates: []
skill_hooks:
  required:
    - "seo-ai-overview"
  conditional: []
handoff:
  next_workflows: []
# AWF_METADATA_END
---

# WORKFLOW: /seo-ai-overview - AI Overview Content Engine

Mục tiêu: đưa `skills/seo-ai-overview` thành luồng chính thức có entry point rõ ràng.

## Skill Activation Contract (Workflow ↔ Skill)

- `seo-ai-overview` (required): luôn chạy full pipeline G0→G7.
- `awf-research-agent` (conditional): bật khi cần mở rộng fact-check đa nguồn, competitor scan, hoặc verify claim nhạy cảm.
- `seo` (conditional): bật khi cần technical/on-page/schema/internal-link checklist để chuẩn bị publish.

Nếu thiếu tool hoặc thiếu evidence đầu vào, chuyển `manual-evidence mode` thay vì bỏ qua stage.

## Flow chuẩn (BẮT BUỘC)

1. G0 Intake + Tool Availability Check
2. G1 Cannibalization Check
3. G2 SERP Analysis
4. G3 Decomposition
5. G4 Querying + Source Scoring
6. G5 Writing
7. G6 Assembly
8. G7 Final QA + Handoff

## Guardrails bắt buộc

- Không bỏ qua G1 cannibalization.
- Không viết nội dung mới khi intent trùng bài cũ mà chưa có quyết định update/merge/redirect.
- Nếu thiếu `search_web` hoặc `browser_subagent`, phải chuyển `manual-evidence mode`; không silent fail.
- Fact không có nguồn phải gắn `needs verification`, không được viết như fact đã xác thực.

## Output tối thiểu

- Full draft (Markdown/HTML)
- QA report
- Verify list
- Meta assets
- Content map cập nhật

## Next Steps

1. `/save-brain` để lưu claim ledger và context.
2. Nếu cần publish, chuyển workflow publish tương ứng.
