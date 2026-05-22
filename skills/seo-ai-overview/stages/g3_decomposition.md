# G3 — Topic Decomposition

## Vai trò của stage này

**Kiến trúc nội dung**

Biến topic rộng thành 5-8 mảnh hẹp, độc lập. Mỗi mảnh = một nhóm câu hỏi cụ thể = một query riêng ở G4.

🎯 **Mục tiêu:** Outline hoàn chỉnh, mỗi mảnh có scope đủ hẹp để query chính xác và verify độc lập.

---

## 4 Nguyên tắc phân mảnh — PHẢI tuân thủ

### Nguyên tắc 1: Mỗi mảnh trả lời một nhóm câu hỏi cụ thể
Nếu một mảnh trả lời nhiều nhóm câu hỏi rất khác nhau → **tách làm 2**.

### Nguyên tắc 2: Overlap tối đa 15%
Nội dung giống nhau không được xuất hiện ở 2 mảnh. Nếu overlap >15% → **merge 2 mảnh lại**.

### Nguyên tắc 3: Mỗi mảnh query được độc lập
Agent phải có khả năng Google riêng từng mảnh và lấy kết quả chất lượng.
- Mảnh quá rộng → khó query → tách nhỏ hơn
- Mảnh quá hẹp → merge vào mảnh liền kề

### Nguyên tắc 4: Số lượng mảnh theo độ dài target
```
5 mảnh  ≈ ~1500 từ
6-7 mảnh ≈ ~2500 từ
7-8 mảnh ≈ ~3500+ từ
```

---

## Template 8 mảnh chuẩn

Điều chỉnh template này theo topic cụ thể. Có thể bỏ bớt hoặc gộp mảnh:

| Mảnh | Nội dung | Format phù hợp |
|------|----------|----------------|
| **M1** | Tổng quan + Định nghĩa + Tại sao quan trọng | Đoạn văn (capture featured snippet) |
| **M2** | Nguyên nhân / Cơ chế / Nguồn gốc | Danh sách có giải thích |
| **M3** | Dấu hiệu nhận biết + Phân biệt với trường hợp tương tự | Bảng so sánh nếu topic cần |
| **M4** | Giải pháp / Điều trị / Cách thực hiện | Step-by-step + bảng tóm tắt |
| **M5** | Phòng ngừa / Duy trì / Best Practice | Checklist hoặc timeline |
| **M6** | Sai lầm thường gặp + Hậu quả thực tế | **Thường là gap lớn nhất** |
| **M7** | Số liệu / Cập nhật mới nhất (VN 2025-2026) | Nếu có data — đây là gap AI Overview không có |
| **M8** | FAQ — rút từ PAA list G2 | Q&A format (FAQ schema markup) |

### Chi tiết từng mảnh

**M1 - Tổng quan:** Giải thích topic là gì, tầm quan trọng, thiệt hại/lợi ích thực tế nếu bỏ qua. Câu đầu phải trả lời "X là gì?" trong <15 từ.

**M2 - Nguyên nhân:** Tại sao xảy ra? Cơ chế hoạt động? Yếu tố thuận lợi/rủi ro? Phần này thường phù hợp format danh sách có giải thích.

**M3 - Nhận biết:** Làm thế nào biết? Phân biệt với trường hợp tương tự? 
> 💡 Cơ hội gap lớn vì top bài thường bỏ qua phần phân biệt chẩn đoán.

**M4 - Giải pháp:** Cụ thể nhất có thể: tên sản phẩm/phương pháp, liều lượng/thông số, thứ tự thực hiện, thời gian, lưu ý đặc biệt. Đây là phần người đọc cần nhất → đầu tư nhiều nhất.

**M5 - Phòng ngừa:** Làm gì để không xảy ra lần sau? Checklist phòng ngừa định kỳ? Thường phù hợp format checklist hoặc timeline.

**M6 - Sai lầm:** 
> 💡 **Đây thường là gap lớn nhất.** Top bài thường chỉ nói "nên làm gì" mà không nói "đừng làm gì và sẽ ra sao". Section này tạo differentiation mạnh nhất.

**M7 - Số liệu:** Tình hình hiện tại, thống kê mới nhất, thay đổi chính sách/sản phẩm gần đây. Thêm vào nếu có data — đây thường là gap mà AI Overview không có vì data quá mới.

**M8 - FAQ:** 3-5 câu hỏi từ PAA list (G2). Format Q&A rõ ràng, mỗi câu trả lời 80-150 từ. Tối ưu cho featured snippet và FAQ schema markup.

---

## Tích hợp Gap List vào Outline

> ⚠️ **Bước quan trọng — Không được bỏ qua**

Sau khi phân mảnh xong, đối chiếu với Gap List từ G2:

1. Mỗi điểm trong Gap List **PHẢI** được assign rõ vào một mảnh cụ thể
2. Nếu gap nào không thuộc mảnh nào → thêm sub-section vào mảnh phù hợp nhất
3. **Gap List phải được phủ 100% trong outline**

Ví dụ:
```
Gap 1: "Bảng so sánh 5 loại thuốc trị sán dây tại VN" → Assign vào M4
Gap 2: "Số liệu tỷ lệ nhiễm sán dây ở ĐBSCL 2025"  → Assign vào M7
Gap 3: "Sai lầm dùng thuốc quá liều gây chết gà con" → Assign vào M6
```

---

## Trình bày Outline cho user

```
📋 OUTLINE — "[keyword]"
Mục tiêu: ~[X] từ | [N] mảnh

M1: [Tên mảnh] (~[Y] từ)
    ├── [Sub-point chính]
    ├── [Sub-point chính]
    └── 🎯 Gap assigned: [gap nào từ Gap List]

M2: [Tên mảnh] (~[Y] từ)
    ├── [Sub-point chính]
    └── 🎯 Gap assigned: [gap nào]

[... tiếp tục cho từng mảnh]

━━━━━━━━━━━━━━━━━━━━━━━
Query template cho G4:
  M1: "[query hẹp cho mảnh 1]"
  M2: "[query hẹp cho mảnh 2]"
  [...]
```

---

## Output của G3

```
✅ Outline 5-8 mảnh với heading tạm
✅ Gap assignment cho từng mảnh
✅ Query template cho G4
```

**Xác nhận Outline với user → chuyển sang G4.**
