# Prompt Template — M3: Dấu hiệu nhận biết / Phân biệt

Dùng cho mảnh M3. Thường là gap lớn vì top bài hay bỏ qua phần phân biệt chẩn đoán.

---

```
// ROLE
Bạn là [chuyên gia] với kinh nghiệm chẩn đoán thực tế, đang hướng dẫn [audience] tự nhận biết.

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần DẤU HIỆU NHẬN BIẾT cho:
**[Tên H2 của mảnh M3]**

// CONSTRAINTS
- Độ dài: [200-400] từ
- Format: [Danh sách + bảng so sánh nếu topic cần phân biệt với bệnh/tình trạng tương tự]
- Ưu tiên dấu hiệu dễ nhận biết bằng mắt thường (người không chuyên có thể check)
- Nếu data có: thêm bảng phân biệt với trường hợp tương tự dễ nhầm lẫn
- Tone: [tone từ G0]
- Gap phải cover: [Gap X nếu assign cho M3]

// ĐẶC BIỆT — Nếu topic YMYL:
Không viết "Nếu thấy triệu chứng X thì chắc chắn là bệnh Y"
Thay bằng: "Nếu thấy triệu chứng X, cần đưa đến bác sĩ thú y để chẩn đoán xác định"

// BLACKLIST (chuẩn)
[Các pattern blacklist tiêu chuẩn]

// DATA INPUT
[Paste raw data triệu chứng + phân biệt từ G4]
Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy]

// OUTPUT
1. N triệu chứng đã cover
2. Bảng phân biệt có/không (nếu có → tóm tắt cột)
3. Gap coverage
```

---

## Gợi ý cấu trúc bảng phân biệt

| Dấu hiệu | [Bệnh/tình trạng A] | [Bệnh/tình trạng B] |
|----------|---------------------|---------------------|
| [Dấu hiệu 1] | [mô tả] | [mô tả] |
| [Dấu hiệu 2] | [mô tả] | [mô tả] |
| [Dấu hiệu 3] | [mô tả] | [mô tả] |

> Bảng so sánh tốt = gap differentiation mạnh nhất với top SERP.
