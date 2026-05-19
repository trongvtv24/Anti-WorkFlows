# Prompt Template — M2: Nguyên nhân / Cơ chế / Nguồn gốc

Dùng cho mảnh M2. Điền các [placeholder] trước khi gửi.

---

```
// ROLE
Bạn là [chuyên gia phù hợp topic] đang giải thích cho [audience].

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần NGUYÊN NHÂN / CƠ CHẾ cho:
**[Tên H2 của mảnh M2]**

// CONSTRAINTS
- Độ dài: [200-350] từ
- Format: Danh sách có giải thích (numbered hoặc bulleted, tùy số lượng nguyên nhân)
- Mỗi nguyên nhân: [Tên ngắn gọn] → [giải thích cơ chế tại sao] → [hậu quả thực tế nếu có trong data]
- KHÔNG liệt kê nguyên nhân mà không giải thích "tại sao"
- Tone: [tone từ G0]
- Gap phải cover: [Gap X nếu có assign cho M2]
- KHÔNG bịa thêm nguyên nhân nào không có trong data input

// BLACKLIST
- "Ngoài ra", "Hơn nữa", "Bên cạnh đó" — tối đa 1 lần trong phần này
- Câu dài >20 từ liên tiếp mà không có câu ngắn
- Passive voice >2 câu liên tiếp

// DATA INPUT
[Paste raw data nguyên nhân từ G4]
Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy]

// OUTPUT
Sau khi viết:
1. Liệt kê N nguyên nhân đã cover (đếm)
2. Gap coverage check
3. Điểm nào cần source bổ sung
```

---

## Gợi ý cấu trúc từng nguyên nhân

```
**[Tên nguyên nhân ngắn gọn]**
[1-2 câu giải thích cơ chế / tại sao điều này xảy ra]
[1 câu hậu quả thực tế nếu data có]
```

Ví dụ:
> **Vệ sinh chuồng trại kém**
> Trứng sán dây tồn tại trong đất ẩm và phân gà có thể sống đến 6 tháng ở nhiệt độ thường. Gà con ăn phải trứng từ nền chuồng bẩn là con đường lây nhiễm phổ biến nhất tại các trang trại nhỏ lẻ ĐBSCL.
