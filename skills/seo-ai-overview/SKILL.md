---
type: skill
name: seo-ai-overview
description: >
  SEO AI Overview Agent — Tự động hóa toàn bộ quy trình sản xuất bài SEO chất lượng cao
  theo framework 8 giai đoạn (G0→G7): từ Project Intake đến bài viết hoàn chỉnh kèm
  meta assets, đủ chất lượng để Google trích dẫn vào AI Overview.
  Dùng khi: user yêu cầu viết bài SEO, tạo nội dung chuẩn AI Overview, nghiên cứu từ khóa.
---

# 🤖 SEO AI Overview Agent — SKILL.md

## Mô tả

Skill này biến AI Agent thành một **SEO Co-pilot** thực sự: nhận keyword → tự chạy toàn bộ pipeline research + phân tích + viết + QA → bàn giao bài viết hoàn chỉnh.

**Triết lý cốt lõi:** AI Overview cho biết Google đang tổng hợp những gì đã có. Bài mới không được spin lại — mà phải cung cấp những gì AI Overview **không có**: số liệu địa phương, case study thực tế, phân tích chuyên sâu, cảnh báo thực chiến.

---

## 🚀 Cách trigger skill này

Các câu lệnh/yêu cầu sẽ kích hoạt skill:
- `"Viết bài SEO về [keyword]"`
- `"Tạo bài chuẩn AI Overview về [chủ đề]"`
- `"Research và viết content SEO cho [topic]"`
- `/seo-ai-overview [keyword]`
- `/seo [keyword]`

---

## 📋 Yêu cầu

**Tools cần có:**
- `search_web` — Tìm kiếm SERP, phân tích AI Overview, query từng mảnh nội dung
- `browser_subagent` — Crawl nội dung top bài rank, đọc chi tiết nguồn Tier 1-2

**Fallback khi không có search:**
- Agent yêu cầu user paste thủ công: nội dung AI Overview, heading top 5 bài, raw data từng mảnh
- Vẫn có thể thực hiện G0, G3, G5, G6, G7 mà không cần search

## Tool Availability Gate (BẮT BUỘC ở G0)

Trước khi chạy G1:

1. Kiểm tra tool availability:
   - Có `search_web` không?
   - Có `browser_subagent` không?
2. Nếu thiếu một hoặc cả hai:
   - Báo rõ tool nào thiếu.
   - Chuyển sang chế độ `manual-evidence`.
   - Yêu cầu user cung cấp input thay thế (AI Overview copy, top URL, raw facts).
3. Không được silent fail. Mọi fallback phải được thông báo rõ trong Intake Brief.

---

## 📂 Cấu trúc skill

```
seo-ai-overview/
├── SKILL.md                    ← File này (entry point)
├── stages/
│   ├── g0_intake.md
│   ├── g1_cannibalization.md
│   ├── g2_serp_analysis.md
│   ├── g3_decomposition.md
│   ├── g4_querying.md
│   ├── g5_writing.md
│   ├── g6_assembly.md
│   └── g7_final_qa.md
├── templates/
│   ├── intake_brief.md
│   ├── gap_list.md
│   ├── outline.md
│   ├── content_map.md
│   ├── handoff_package.md
│   └── prompts/
│       ├── m1_overview.md … m8_faq.md
└── resources/
    ├── blacklist_patterns.md
    ├── source_tier_guide.md
    ├── ymyl_guide.md
    └── qa_checklist.md
```

---

## ▶️ Thứ tự thực thi — BẮT BUỘC theo đúng thứ tự

Khi nhận yêu cầu viết bài SEO, agent **PHẢI** đọc và thực thi từng stage theo thứ tự sau:

### 1. Đọc `stages/g0_intake.md`
Thu thập đủ thông tin từ user trước khi làm bất cứ điều gì. Không bao giờ giả định.

### 2. Đọc `stages/g1_cannibalization.md`
Check xem đã có bài tương tự chưa. Ra quyết định: Tạo mới / Update / Merge / Redirect.

### 3. Đọc `stages/g2_serp_analysis.md`
Phân tích SERP sâu. Output: Gap List 3-5 điểm **cụ thể và đo lường được**.

### 4. Đọc `stages/g3_decomposition.md`
Chia topic thành 5-8 mảnh độc lập. Gắn Gap vào từng mảnh.

### 5. Đọc `stages/g4_querying.md`
Query và thu thập data cho từng mảnh. Score nguồn theo Tier. Tuyệt đối không dùng knowledge nội tại nếu không có source.

### 6. Đọc `stages/g5_writing.md`
Viết từng mảnh, revise tối đa 3 vòng/mảnh.

### 7. Đọc `stages/g6_assembly.md`
Lắp ghép, loại bỏ AI pattern, thêm internal link, tạo meta assets.

### 8. Đọc `stages/g7_final_qa.md`
QA 8 tiêu chí. Tạo Handoff Package hoàn chỉnh trước khi bàn giao.

---

## ⚠️ Quy tắc cứng — KHÔNG được vi phạm

1. **Không hallucinate số liệu.** Thà ghi "Chưa đủ dữ liệu" còn hơn bịa fact.
2. **Không tạo 2 bài cùng intent trên 1 domain.** Luôn check cannibalization trước.
3. **Không bỏ qua QA.** Bài không qua G7 không được bàn giao.
4. **Không spin lại AI Overview.** Bài mới phải có ít nhất 3 gap cụ thể so với top SERP.
5. **YMYL cao → chỉ dùng Tier 1-2 source.** Không ngoại lệ.

---

## 📊 Outputs cuối cùng

Sau khi hoàn thành G7, agent bàn giao **Handoff Package** gồm:
1. ✅ Full draft bài viết (Markdown/HTML)
2. ✅ QA Report 8 tiêu chí (Pass/Fail)
3. ✅ Verify List (những điểm user cần check thêm)
4. ✅ Meta Assets (meta description, alt text, FAQ schema JSON-LD)
5. ✅ Content Map cập nhật
