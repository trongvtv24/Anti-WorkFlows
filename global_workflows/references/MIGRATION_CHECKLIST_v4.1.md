# AWF v4.1 Migration Checklist

Mục tiêu: đồng bộ toàn bộ workflow/skill cũ theo các rule mới đã áp dụng trong repo này.

## 1) Persona & Tone Priority

- [ ] `EXPERT_PERSONA` áp dụng global cho toàn bộ workflows/skills.
- [ ] Không còn `Tone Override` kiểu thân thiện để vô hiệu aggressive/argumentative stance.
- [ ] `awf_manifest.yaml` có `persona_policy` với ưu tiên `expert_persona_global`.

## 2) Stable Memory Safety

- [ ] `/save-brain` bắt buộc chạy stable diff trước khi ghi `brain.json`.
- [ ] Inferred changes cần explicit user approval.
- [ ] Có snapshot trước mutation cho cả `brain.json` và `session.json`.

## 3) Task-Level Resume

- [ ] `session.schema.json` có `current_task_index`, `current_task_id`, `phase_task_progress`.
- [ ] `/code` hỗ trợ `/code resume`.
- [ ] `session_log.txt` dùng format machine-readable cho `task_checkpoint`.

## 4) Visualize → Code Handoff Gate

- [ ] `/visualize` validate `docs/design-specs.md` trước handoff.
- [ ] `/code` chặn task UI nếu thiếu/invalid design specs hoặc thiếu `design-system/MASTER.md` khi được tham chiếu.

## 5) Preventive Red Teaming

- [ ] `/plan` có trigger red-team khi đụng auth/payment/PII/permissions.
- [ ] `/design` có pre-emptive red team checkpoint trước acceptance criteria.

## 6) SEO AI Overview Integration

- [ ] Có workflow entry `/seo-ai-overview`.
- [ ] Skill SEO có tool availability gate ngay từ G0.
- [ ] Có fallback `manual-evidence` khi thiếu tool, không silent fail.

## 7) Validator Hardening

- [ ] `tools/validate_awf.py` chỉ coverage-check file có `type: workflow/skill`.
- [ ] Validator kiểm tra format `task_checkpoint` trong `.brain/session_log.txt` (nếu file tồn tại).
- [ ] Chạy `python tools/validate_awf.py` và đạt `PASS`.

## 8) Deprecated Feature Removal

- [ ] Không còn workflow/skill deprecated trong manifest.
- [ ] Không còn binding hay router entry trỏ tới feature đã loại bỏ.
- [ ] Không còn data/docs runtime cũ gắn với feature đã loại bỏ.

## 9) Quick Verification Commands

```powershell
python tools\validate_awf.py
python tools\audit_workflow_skill_logic.py --strict
rg -n "task_checkpoint|current_task_index|phase_task_progress" global_workflows schemas templates
```
