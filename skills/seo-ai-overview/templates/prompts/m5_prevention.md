# Prompt Template — M5: Phòng ngừa / Duy trì / Best Practice

---

```
// ROLE
Bạn là [chuyên gia] với góc nhìn phòng ngừa thực tế, đang chia sẻ kinh nghiệm
cho [audience] để tránh tái phát.

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần PHÒNG NGỪA:
**[Tên H2 của mảnh M5]**

// CONSTRAINTS
- Độ dài: [200-350] từ
- Format: Checklist hoặc timeline (tùy topic — checklist tốt hơn cho phòng ngừa định kỳ,
  timeline tốt hơn cho quy trình tuần tự)
- Hành động cụ thể, có thể thực hiện ngay — không chung chung
- Nếu có lịch định kỳ (hàng tuần/tháng/quý) → format timeline rõ ràng
- Tone: [tone từ G0]
- Gap phải cover: [Gap X nếu có]

// BLACKLIST (chuẩn)
[Các pattern blacklist tiêu chuẩn]

// DATA INPUT
[Paste raw data phòng ngừa từ G4]
Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy]

// OUTPUT
1. N biện pháp phòng ngừa đã cover
2. Format đã dùng (checklist/timeline)
3. Gap coverage
```

---

## Gợi ý format Checklist

```markdown
**Checklist phòng ngừa [topic] — Áp dụng [định kỳ]:**

- [ ] [Hành động 1 — cụ thể]
- [ ] [Hành động 2 — cụ thể]
- [ ] [Hành động 3 — cụ thể, nếu có trong data: kèm tần suất hoặc thông số]
```

## Gợi ý format Timeline

```markdown
**Lịch [phòng ngừa/bảo dưỡng/kiểm tra]:**

🗓️ **Hàng tuần:** [Việc cần làm]
🗓️ **Hàng tháng:** [Việc cần làm]
🗓️ **Hàng quý:** [Việc cần làm]
🗓️ **Hàng năm:** [Việc cần làm]
```
