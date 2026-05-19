# G2 — SERP Analysis & Gap Mapping

## Vai trò của stage này

**Cốt lõi của toàn bộ framework**

Phân tích sâu AI Overview và top 5 kết quả để tìm ra những gì bài mới phải làm tốt hơn. Không có Gap List → không có lý do để bài mới tồn tại.

🎯 **Mục tiêu:** Xác định "lý do tồn tại" cụ thể của bài mới so với những gì đang rank.

---

## Phần A: Phân tích AI Overview

Dùng `search_web` với keyword chính. Ghi lại nội dung AI Overview (nếu xuất hiện).

### A1. Ghi lại những ý AI Overview đang tổng hợp

Liệt kê đầy đủ các heading / bullet point / đoạn văn AI Overview đang hiển thị.

> Đây là **"bản đồ những gì đã có"**. Bài mới phải bổ sung những gì nằm ngoài bản đồ này.

### A2. Xác định điểm yếu của AI Overview

AI Overview thường yếu ở các vùng sau — ghi lại từng điểm còn thiếu:

| Vùng yếu | Câu hỏi kiểm tra |
|----------|-----------------|
| Số liệu địa phương | AI Overview có số liệu VN / năm hiện tại không? |
| Ví dụ thực tế cụ thể | Có case study hay tình huống thực không? |
| So sánh sản phẩm/phương pháp | Có bảng so sánh cụ thể không? |
| Cảnh báo thực chiến | Có cảnh báo sai lầm / hậu quả không? |
| Hướng dẫn từng bước chi tiết | Có step-by-step actionable không? |

### A3. Ghi lại format AI Overview đang dùng

- Dạng đoạn văn?
- Dạng danh sách bullet?
- Dạng bảng?

> Bài mới cần format phần quan trọng nhất theo dạng này để tăng cơ hội được trích dẫn. Ghi lại để áp dụng ở G5.

---

## Phần B: Phân tích Top 5 bài đang rank

Dùng `browser_subagent` để crawl heading structure của top 5 URL.

### B1. Mapping cấu trúc heading của từng bài

Tạo bảng mapping:

```
URL 1: [title]
  H1: [...]
  H2: [...]
  H2: [...]
  H3: [...]

URL 2: [title]
  H1: [...]
  H2: [...]
  ...
```

Tìm:
- **Pattern chung**: Section nào xuất hiện ở ≥3/5 bài → **BẮT BUỘC** có trong bài mới
- **Gap**: Section nào không bài nào cover → **CƠ HỘI** của bài mới

### B2. Đo độ dài trung bình

Ước tính word count của top 5. Tính trung bình.

> Bài mới nên dài hơn 15-25% nếu có nội dung thực sự để thêm. **Không nhồi chữ để đủ số — quality over quantity.**

Nếu user đã chỉ định độ dài ở G0 → dùng theo chỉ định. Chỉ override nếu chênh lệch quá lớn (>50%).

### B3. Check format đặc biệt của top bài

- Bảng so sánh?
- Checklist?
- Video embed?
- Tool tương tác?

Nếu format đặc biệt xuất hiện ở bài rank tốt → Google đánh giá cao format này cho topic này.

### B4. Thu thập People Also Ask (PAA)

Copy toàn bộ câu hỏi PAA hiện tại. Đây là intent chưa được trả lời đầy đủ.

> PAA list sẽ dùng ở G3 (phân mảnh M8-FAQ) và G5 (viết FAQ section).

### B5. Thu thập Related Searches

Ghi 8-10 related search ở cuối trang SERP. Một số gợi ý sub-topic bổ sung hoặc keyword phụ cần nhắc đến.

---

## Phần C: Tạo Gap List — Output BẮT BUỘC của G2

### Định nghĩa Gap List

Gap List là danh sách **3-5 điểm cụ thể** mà bài mới sẽ làm tốt hơn tất cả top 5 SERP hiện tại.

**Tiêu chuẩn chấp nhận:**
- ✅ Mỗi điểm cụ thể, đo lường được
- ✅ Ví dụ tốt: *"Thêm bảng so sánh 5 loại thuốc trị sán dây phổ biến tại VN kèm giá thị trường 2026 — không bài nào có"*
- ❌ Không chấp nhận gap mơ hồ: *"viết hay hơn"* hay *"chi tiết hơn"*

### 4 câu hỏi để tìm gap chất lượng

1. **Số liệu địa phương**: Số liệu VN / 2025-2026 nào còn thiếu hoàn toàn trên SERP?
2. **Case study thực tế**: Ví dụ cụ thể nào audience target cần mà AI Overview và top 5 không có?
3. **Cảnh báo thực chiến**: Sai lầm / hậu quả thực tế nào chưa bài nào mention đầy đủ?
4. **Tool / bảng / checklist**: Công cụ hữu ích nào mà top 5 không có nhưng sẽ rất giá trị?

---

## Trình bày kết quả G2 cho user

```
📊 SERP ANALYSIS REPORT — "[keyword]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AI OVERVIEW: [Có / Không]
Format: [đoạn văn / danh sách / bảng]
Điểm yếu phát hiện:
  • [điểm yếu 1]
  • [điểm yếu 2]

📑 TOP 5 PATTERN CHUNG (phải có trong bài mới):
  • [section 1]
  • [section 2]
  • [section 3]

🎯 GAP LIST (lý do tồn tại của bài mới):
  Gap 1: [mô tả cụ thể]
  Gap 2: [mô tả cụ thể]
  Gap 3: [mô tả cụ thể]
  [Gap 4-5 nếu có]

❓ PAA LIST:
  1. [câu hỏi 1]
  2. [câu hỏi 2]
  3. [câu hỏi 3]
  ...

📏 Độ dài target: [~X từ] (SERP avg: [Y từ] + 20%)
📐 Format target snippet: [prose / list / table]
```

---

## Output của G2

```
✅ SERP Map (heading structure top 5)
✅ Gap List (3–5 điểm cụ thể, đo lường được)
✅ PAA List đầy đủ
✅ Featured Snippet format target
✅ Độ dài target (nếu không chỉ định ở G0)
```

**Xác nhận Gap List với user → chuyển sang G3.**
