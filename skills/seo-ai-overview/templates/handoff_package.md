# Template: Handoff Package

Output cuối cùng của G7. Đây là gói bàn giao hoàn chỉnh cho user sau khi QA pass.

---

## HANDOFF PACKAGE — [Keyword chính]

**Ngày hoàn thành:** [dd/mm/yyyy]
**Agent:** SEO AI Overview v2.0
**QA Result:** [X/8 PASS]

---

## 📄 Item 1: Full Draft Bài Viết

> [Paste toàn bộ bài viết ở đây — Markdown format]

```markdown
# [Tiêu đề H1]

[Sapo 100-150 từ]

## [H2 — Mảnh 1]

[Nội dung mảnh 1]

[INTERNAL LINK → "Tên bài liên quan"]

## [H2 — Mảnh 2]

[Nội dung mảnh 2]

...

## Câu hỏi thường gặp

**Q: [Câu hỏi 1 từ PAA]**

A: [Trả lời 80-150 từ]

**Q: [Câu hỏi 2]**

A: [Trả lời]

## Kết luận

[3 action items cụ thể + CTA]
```

---

## ✅ Item 2: QA Report

| # | Tiêu chí | Kết quả | Ghi chú |
|---|---------|---------|---------|
| ① | Fact Accuracy | PASS / FAIL | |
| ② | Gap Coverage | PASS / FAIL | [N]/5 gap |
| ③ | Anti-AI Pattern | PASS / FAIL | |
| ④ | YMYL Compliance | PASS / FAIL / N/A | |
| ⑤ | SEO Structure | PASS / FAIL | |
| ⑥ | Meta Assets | PASS / FAIL | |
| ⑦ | Cannibalization Final | PASS / FAIL | |
| ⑧ | Format & Readability | PASS / FAIL | |

**Tổng kết:** [X]/8 PASS

---

## ⚠️ Item 3: Verify List

Những điểm anh cần kiểm tra trước khi publish:

1. **[Fact X]** — Nguồn hiện tại: [Y] (Tier [N]) — Cần: xác nhận thêm bằng nguồn độc lập
2. **[Fact Z]** — Mâu thuẫn giữa [nguồn A] và [nguồn B] — Cần: anh quyết định dùng số liệu nào
3. **[Số liệu W]** — Chưa tìm được source VN cụ thể — Cần: tìm thêm hoặc loại bỏ

> Nếu Verify List trống → không có điểm nào cần check thêm.

---

## 🔧 Item 4: Meta Assets

### Meta Description (~155 ký tự):
```
[Meta description hoàn chỉnh — đếm ký tự trước khi paste]
```
**Ký tự:** [đếm] / 155

### Alt Text gợi ý:
```
Ảnh 1 (vị trí: [mô tả vị trí]): "[alt text]"
Ảnh 2 (vị trí: [mô tả vị trí]): "[alt text]"
Ảnh 3 (vị trí: [mô tả vị trí]): "[alt text]"
```

### FAQ Schema JSON-LD (paste vào <head> hoặc plugin):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Câu hỏi 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Câu trả lời 1]"
      }
    },
    {
      "@type": "Question",
      "name": "[Câu hỏi 2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Câu trả lời 2]"
      }
    }
  ]
}
```

---

## 📊 Item 5: Content Map Entry mới

Thêm dòng này vào Content Map:

| Keyword | URL Slug | Search Intent | YMYL | Word Count | Ngày | Status |
|---------|----------|--------------|------|-----------|------|--------|
| [keyword chính] | /[slug-goi-y] | [informational] | [level] | [~X từ] | [dd/mm] | Draft |

---

## 📋 Checklist Publish cho Editor

Trước khi nhấn Publish, editor cần:
- [ ] Thêm ảnh vào đúng vị trí (theo alt text gợi ý)
- [ ] Thay `[INTERNAL LINK → "..."]` bằng link thật
- [ ] Paste FAQ schema JSON-LD vào head/plugin
- [ ] Set meta description đúng như trên
- [ ] Review Verify List — xử lý các điểm chưa chắc
- [ ] Cập nhật status Content Map thành "Published" sau khi đăng
