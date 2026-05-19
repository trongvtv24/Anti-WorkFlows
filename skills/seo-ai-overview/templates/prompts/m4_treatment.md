# Prompt Template — M4: Giải pháp / Điều trị / Cách thực hiện (YMYL)

Đây là mảnh quan trọng nhất — người đọc cần nhất. Với YMYL, phải có disclaimer.

---

```
// ROLE
Bạn là [chuyên gia — ví dụ: "bác sĩ thú y chuyên gia cầm"] đang hướng dẫn thực tế
cho [audience]. Bạn ưu tiên thông tin chính xác và an toàn trên hết.

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần GIẢI PHÁP / ĐIỀU TRỊ:
**[Tên H2 của mảnh M4]**

// YMYL LEVEL: [Cao / Trung bình]
[Nếu YMYL Cao hoặc Trung bình — bắt buộc thêm disclaimer ở cuối phần này:
"⚠️ Lưu ý: Thông tin trên chỉ mang tính tham khảo. Liều lượng và phác đồ thực tế
cần được bác sĩ thú y / bác sĩ xác nhận dựa trên tình trạng cụ thể."]

// CONSTRAINTS
- Độ dài: [300-500] từ (phần này đầu tư nhiều nhất)
- Format: Step-by-step numbered list + bảng tóm tắt nếu data có nhiều options
- Với mỗi loại thuốc/phương pháp (nếu có trong data):
  * Tên hoạt chất → Liều lượng → Cách dùng → Thời gian → Lưu ý
- Cụ thể nhất có thể — tên sản phẩm, thông số, thứ tự thực hiện
- Gap phải cover: [Gap X — thường là bảng so sánh thuốc, số liệu cụ thể VN]

// TUYỆT ĐỐI KHÔNG:
- Thêm tên thuốc, liều lượng, tỷ lệ % nào KHÔNG có trong data input
- Viết "100% hiệu quả", "chắc chắn chữa khỏi", "đảm bảo an toàn"
- Bỏ qua disclaimer nếu YMYL Cao hoặc Trung bình

// BLACKLIST (chuẩn)
[Các pattern blacklist tiêu chuẩn]

// DATA INPUT (chỉ Tier 1-2 cho YMYL)
[Paste raw data điều trị từ G4 — bắt buộc ghi rõ Tier]
Nguồn: [tên] | Tier [1/2] | Ngày: [dd/mm/yyyy]

// OUTPUT
1. Danh sách các phương pháp/thuốc đã cover (đếm)
2. Bảng tóm tắt có/không và nội dung
3. Disclaimer đã thêm chưa (Y/N)
4. Gap coverage
5. Điểm nào thiếu source — cần user verify
```

---

## Template bảng tóm tắt thuốc/phương pháp

| Tên thuốc/phương pháp | Hoạt chất | Liều dùng | Cách dùng | Thời gian | Lưu ý |
|----------------------|-----------|-----------|-----------|-----------|-------|
| [Tên 1] | [hoạt chất] | [liều] | [cách] | [thời gian] | [lưu ý] |
| [Tên 2] | [hoạt chất] | [liều] | [cách] | [thời gian] | [lưu ý] |

*Nguồn: [tên nguồn Tier 1/2] — [ngày]*

---

## Template disclaimer theo YMYL level

**YMYL Cao:**
```
⚠️ **Quan trọng:** Thông tin trên chỉ mang tính tham khảo giáo dục, không thay thế
cho tư vấn y tế chuyên nghiệp. Hãy tham khảo bác sĩ được cấp phép trước khi thực
hiện bất kỳ phương pháp điều trị nào.
```

**YMYL Trung bình (thú y):**
```
Lưu ý: Liều lượng và phác đồ điều trị có thể thay đổi tùy theo trọng lượng, tuổi,
tình trạng sức khỏe cụ thể của từng con vật. Tham khảo bác sĩ thú y trước khi áp dụng.
```
