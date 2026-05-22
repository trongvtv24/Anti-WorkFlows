# Prompt Template — M8: FAQ — từ PAA List

Mảnh cuối, tối ưu cho featured snippet và FAQ schema markup.

---

```
// ROLE
Bạn là [chuyên gia] đang trả lời trực tiếp các câu hỏi thường gặp nhất của [audience].

// TASK
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp, viết phần FAQ:
**Câu hỏi thường gặp về [topic]**

// DANH SÁCH CÂU HỎI (từ PAA list G2):
1. [Câu hỏi 1 — nguyên văn từ PAA]
2. [Câu hỏi 2 — nguyên văn từ PAA]
3. [Câu hỏi 3 — nguyên văn từ PAA]
[4-5 nếu có đủ data]

// CONSTRAINTS
- Mỗi câu trả lời: 80-150 từ
- Câu trả lời phải đủ đứng độc lập — người đọc không cần đọc cả bài vẫn hiểu
- Bắt đầu câu trả lời bằng direct answer (không "Đây là câu hỏi hay...")
- Format Q&A rõ ràng:
  **Q: [câu hỏi nguyên văn]**
  A: [trả lời trực tiếp, súc tích]
- Tone: [tone từ G0]
- Nếu câu hỏi liên quan YMYL: kết thúc câu trả lời bằng "Tham khảo [chuyên gia] để có tư vấn phù hợp tình huống cụ thể."

// TUYỆT ĐỐI KHÔNG:
- Trả lời bằng data không có trong input G4
- Câu trả lời >200 từ — sẽ không được trích vào featured snippet
- Bắt đầu bằng "Câu hỏi này...", "Để trả lời câu hỏi này..."

// BLACKLIST (chuẩn)
[Các pattern blacklist tiêu chuẩn]

// DATA INPUT — cho từng câu hỏi
Q1 data: [paste data relevant cho câu hỏi 1]
Nguồn Q1: [tên] | Tier [1/2/3]

Q2 data: [paste data relevant cho câu hỏi 2]
Nguồn Q2: [tên] | Tier [1/2/3]

[...]

// OUTPUT
1. N câu hỏi đã trả lời
2. Câu nào cần source bổ sung
3. Câu nào có YMYL concern → đã thêm disclaimer chưa
```

---

## Template FAQ cho bài

```markdown
## Câu hỏi thường gặp về [topic]

**Q: [Câu hỏi 1 nguyên văn]**

[Câu trả lời 80-150 từ — bắt đầu bằng direct answer]

---

**Q: [Câu hỏi 2]**

[Câu trả lời]

---

**Q: [Câu hỏi 3]**

[Câu trả lời]
```

## Sau khi viết FAQ — Chuẩn bị schema

Mỗi Q&A trong FAQ sẽ được đưa vào JSON-LD schema ở G6. Đảm bảo:
- Câu hỏi: nguyên văn từ PAA (không paraphrase)
- Câu trả lời: phiên bản ngắn gọn nhất (80-120 từ cho schema)
