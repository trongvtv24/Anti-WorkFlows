# G1 — Cannibalization Check

## Vai trò của stage này

**Bắt buộc · Trước SERP Analysis**

Kiểm tra toàn bộ nội dung đã tồn tại trên site trước khi tạo bài mới. Bài mới trùng keyword với bài cũ rank tốt = hại cả hai.

🎯 **Mục tiêu:** Ra quyết định rõ ràng — tạo mới / update / merge / redirect — trước khi đầu tư thêm thời gian.

---

## Quy trình check từng bước

### Bước 1: Search site: với keyword chính

Dùng `search_web` với query:
```
site:[domain] "[keyword chính]"
```

Ví dụ:
```
site:trangtraiviet.com "bệnh sán dây ở gà"
```

Ghi lại tất cả URL trả về.

### Bước 2: Search với keyword biến thể

Lặp lại với 2-3 biến thể quan trọng:
```
site:[domain] "[biến thể 1]"
site:[domain] "[biến thể 2]"
```

Ví dụ:
```
site:trangtraiviet.com "sán dây gà con"
site:trangtraiviet.com "ký sinh trùng gà"
```

Mục tiêu: Bắt những bài có overlap >50% intent dù không trùng exact keyword.

### Bước 3: Đánh giá bài cũ tìm thấy

Với mỗi URL tìm thấy, đánh giá:
- Bài đang rank vị trí bao nhiêu? (tìm trong SERP)
- Có traffic thực không?
- Intent có giống bài mới không hay chỉ mention thoáng qua?

> **Chỉ những bài cùng search intent mới bị coi là cannibal.**
> Bài chỉ nhắc đến keyword 1-2 lần trong context khác → KHÔNG phải cannibal.

### Bước 4: Check Content Map nội bộ (nếu user cung cấp ở G0)

So sánh với danh sách bài đã publish. Tìm keyword overlap ngay cả với bài chưa rank nhưng đang target intent tương tự.

### Bước 5: Cập nhật Content Map

Sau khi ra quyết định, thêm keyword/URL mới vào Content Map. Nếu user chưa có Content Map → gợi ý tạo bằng template `templates/content_map.md`.

---

## Decision Tree — Ra quyết định

```
┌─────────────────────────────────────────────────────────────────────┐
│ Kết quả tìm kiếm                    → Quyết định                   │
├─────────────────────────────────────────────────────────────────────┤
│ Bài cũ rank Top 1–10               → DỪNG tạo mới.                 │
│                                      Update + mở rộng bài cũ:      │
│                                      thêm section, cập nhật số liệu,│
│                                      bổ sung FAQ.                   │
├─────────────────────────────────────────────────────────────────────┤
│ Bài cũ rank 11–30 (yếu)            → Cân nhắc MERGE:               │
│                                      Viết bài mới hoàn chỉnh →     │
│                                      301 redirect bài cũ sang mới.  │
│                                      Hoặc update toàn bộ bài cũ.   │
│                                      KHÔNG tạo 2 bài riêng.        │
├─────────────────────────────────────────────────────────────────────┤
│ Bài cũ rank 31+ hoặc không traffic → Tạo bài MỚI tốt hơn          │
│                                      rồi 301 redirect bài cũ.      │
├─────────────────────────────────────────────────────────────────────┤
│ Bài cũ khác intent hoàn toàn        → Tạo mới BÌNH THƯỜNG.         │
│                                      Thêm internal link từ bài cũ  │
│                                      → bài mới ở đoạn relevant.    │
├─────────────────────────────────────────────────────────────────────┤
│ Không tìm thấy bài nào              → Tạo mới TỰ DO.               │
│                                      Ghi keyword vào Content Map.  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Báo cáo kết quả cho user

Trình bày kết quả check dưới dạng:

```
📊 KẾT QUẢ CANNIBALIZATION CHECK — [keyword]
Domain: [domain]

🔍 Tìm thấy [N] bài có thể liên quan:
  • [URL 1] — Rank: [vị trí] — Intent overlap: [cao/trung bình/thấp]
  • [URL 2] — Rank: [vị trí] — Intent overlap: [cao/trung bình/thấp]

⚖️ QUYẾT ĐỊNH: [Tạo mới / Update / Merge / Redirect]
📝 Lý do: [giải thích ngắn gọn]

→ [Nếu Tạo mới] Tiếp tục sang G2: SERP Analysis
→ [Nếu Update/Merge] Dừng ở đây — hướng dẫn update bài cũ
```

---

## ⚠️ Quy tắc cứng — Không ngoại lệ

> **KHÔNG BAO GIỜ** tạo 2 bài riêng biệt cùng target exact keyword và cùng search intent trên cùng một domain — dù bài mới "tốt hơn nhiều". Google sẽ phải chọn 1 để rank và thường chọn ngẫu nhiên, làm loãng authority của cả hai.

---

## Output của G1

```
✅ Quyết định: Tạo mới / Update / Merge / Redirect
✅ Content Map cập nhật
✅ Ghi chú bài cũ liên quan (nếu có)
```

**Nếu quyết định = Tạo mới → chuyển sang G2.**
**Nếu không → dừng và thực hiện theo hướng dẫn update/merge.**
