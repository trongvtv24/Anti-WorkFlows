# Prompt Template — M6: Sai lầm thường gặp + Hậu quả thực tế

Đây là **gap lớn nhất** — top bài thường chỉ nói "nên làm gì" mà bỏ qua "đừng làm gì".

---

```
// ROLE
Bạn là [chuyên gia] đã chứng kiến nhiều trường hợp thất bại vì sai lầm phổ biến,
đang chia sẻ kinh nghiệm thực chiến cho [audience] để tránh vết xe đổ.

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần SAI LẦM THƯỜNG GẶP:
**[Tên H2 của mảnh M6]**

// CONSTRAINTS
- Độ dài: [250-400] từ
- Số sai lầm: 4-5 (từ data input — không bịa thêm dù "có vẻ hợp lý")
- Cấu trúc mỗi sai lầm:
  1. Tên sai lầm (ngắn gọn, specific — không chung chung)
  2. Tại sao người ta hay mắc phải (tâm lý/thói quen/thiếu thông tin)
  3. Hậu quả thực tế (có số liệu/ví dụ cụ thể nếu data có)
  4. Cách làm đúng thay thế
- Tone: Thực chiến, không phán xét. Viết như người đã thấy hậu quả, chia sẻ để tránh cho người khác
- Gap phải cover: [Gap X — đây thường là gap lớn nhất cần đặc biệt chú ý]

// TUYỆT ĐỐI KHÔNG:
- Bịa thêm sai lầm không có trong data input
- Phán xét người mắc sai lầm ("người không hiểu biết thường...", "nhiều người thiếu ý thức...")
- Hậu quả mơ hồ ("có thể gây hại", "không tốt") — phải cụ thể nếu data có

// BLACKLIST (chuẩn)
[Các pattern blacklist tiêu chuẩn]

// DATA INPUT
[Paste raw data sai lầm từ G4 — chú thích sai lầm nào từ nguồn nào]
Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy]

// OUTPUT
1. N sai lầm đã cover (đếm)
2. Sai lầm nào có hậu quả cụ thể với số liệu (đánh dấu)
3. Gap coverage — cụ thể section nào cover gap
4. Điểm nào cần thêm data
```

---

## Template cấu trúc từng sai lầm

```markdown
### ❌ Sai lầm [N]: [Tên cụ thể]

**Tại sao hay mắc phải:** [1 câu giải thích tâm lý / thói quen]

**Hậu quả thực tế:** [Cụ thể — có số liệu nếu data có. Ví dụ: "gà chết trong 48h" hoặc "tỷ lệ tái phát tăng 60%"]

**✅ Cách làm đúng:** [1-2 câu hướng dẫn thay thế cụ thể]
```

## Ví dụ minh họa

**❌ Xấu (chung chung):**
> "Nhiều người thường không tuân thủ đúng liều lượng khi điều trị, điều này có thể gây ra nhiều hậu quả không tốt cho sức khỏe vật nuôi."

**✅ Tốt (cụ thể, thực chiến):**
> ### ❌ Sai lầm 2: Dừng thuốc sớm khi thấy gà "khỏe lại"
>
> **Tại sao hay mắc phải:** Sau 3-4 ngày điều trị, gà ăn trở lại và hoạt bát hơn — chủ trại nghĩ đã khỏi và ngừng thuốc để tiết kiệm chi phí.
>
> **Hậu quả:** Sán dây giai đoạn ấu trùng vẫn còn trong niêm mạc ruột. Ngừng sớm khiến kháng thuốc hình thành — đợt điều trị sau cần liều cao hơn 2-3 lần và hiệu quả giảm đáng kể.
>
> **✅ Đúng:** Hoàn thành đủ phác đồ [X] ngày theo hướng dẫn bác sĩ thú y, kể cả khi gà có vẻ hồi phục hoàn toàn.
