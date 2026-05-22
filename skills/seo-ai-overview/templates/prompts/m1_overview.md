# Prompt Template — M1: Tổng quan / Định nghĩa

Dùng cho mảnh M1. Điền các [placeholder] trước khi gửi cho AI.

---

```
// ROLE
Bạn là [chuyên gia cụ thể — ví dụ: "bác sĩ thú y gia cầm với 10 năm kinh nghiệm thực tế tại ĐBSCL,
đang giải thích cho chủ trang trại gà nhỏ lẻ"].

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp bên dưới, viết phần MỞ ĐẦU / TỔNG QUAN cho bài về:
**[Keyword chính]**

// CONSTRAINTS
- Độ dài: [150-250] từ
- Câu đầu tiên PHẢI trả lời trực tiếp "[Keyword] là gì?" trong dưới 15 từ
- KHÔNG bắt đầu bằng "Trong thế giới ngày nay…", "Từ xưa đến nay…", định nghĩa học thuật khô khan
- Tone: [thân thiện / chuyên môn / thực chiến] — phù hợp với [audience]
- Format: Đoạn văn ngắn 2-3 câu (dễ được trích vào AI Overview dạng definition)
- Sau đoạn định nghĩa: nêu tầm quan trọng thực tế (thiệt hại/lợi ích nếu bỏ qua)
- Gap phải cover: [Gap X được assign cho M1]
- KHÔNG bịa thêm bất kỳ fact nào ngoài data input

// BLACKLIST (không dùng)
- "Điều quan trọng là..."
- "Đáng chú ý rằng..."
- "Không thể phủ nhận rằng..."
- Câu 20+ từ liên tiếp mà không có câu ngắn xen kẽ

// DATA INPUT
[Paste raw data từ G4 cho mảnh M1]
Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy]

// OUTPUT YÊU CẦU
Sau khi viết xong, liệt kê:
1. 2-3 điểm chính đã paraphrase từ input
2. Gap đã được cover như thế nào
3. Điểm nào trong input chưa đủ để viết sâu hơn
```

---

## Ví dụ tốt vs xấu

**❌ Xấu (AI-style):**
> "Sán dây là một loại ký sinh trùng đường ruột thuộc lớp Cestoda, có thể ảnh hưởng đến nhiều loài động vật bao gồm gia cầm. Điều quan trọng là phải hiểu rõ về loại ký sinh trùng này để có biện pháp phòng trị hiệu quả."

**✅ Tốt (tự nhiên):**
> "Sán dây ở gà là loại ký sinh trùng dẹt sống trong ruột non, hút chất dinh dưỡng trực tiếp từ vật chủ. Với đàn gà con dưới 3 tháng tuổi, nhiễm nặng có thể khiến gà chậm lớn 20-30% và tăng tỷ lệ chết non — thiệt hại nhiều chủ trại không nhận ra cho đến khi quá muộn."
