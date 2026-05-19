# G5 — Content Writing — Từng mảnh

## Vai trò của stage này

**Viết nội dung**

Viết từng mảnh riêng biệt, không viết toàn bài một lần. Mỗi mảnh review xong mới sang mảnh tiếp theo.

🎯 **Mục tiêu:** Nội dung chính xác 100%, cover gap, viết cho người đọc — không phải cho AI.

---

## Cấu trúc prompt chuẩn — Dùng cho từng mảnh

Đọc prompt template tương ứng trong `templates/prompts/` trước khi viết từng mảnh:
- M1 → `templates/prompts/m1_overview.md`
- M2 → `templates/prompts/m2_cause.md`
- M3 → `templates/prompts/m3_symptoms.md`
- M4 → `templates/prompts/m4_treatment.md`
- M5 → `templates/prompts/m5_prevention.md`
- M6 → `templates/prompts/m6_mistakes.md`
- M7 → `templates/prompts/m7_data.md`
- M8 → `templates/prompts/m8_faq.md`

### Template chung — Điền vào cho từng mảnh

```
// PHẦN 1: ROLE DEFINITION
Bạn là [chuyên gia cụ thể phù hợp topic + audience].
// Ví dụ: "Bạn là bác sĩ thú y gia cầm với 10 năm kinh nghiệm thực tế tại ĐBSCL,
//         đang tư vấn cho chủ trang trại gà nhỏ lẻ."

// PHẦN 2: TASK + CONSTRAINTS
Dựa CHÍNH XÁC và CHỈ trên dữ liệu tôi cung cấp bên dưới, hãy viết nội dung cho phần:
**[Tên mảnh / Heading]**

Yêu cầu bắt buộc:
- Ngôn ngữ: tiếng Việt tự nhiên, gần gũi với [audience]
- Tone: [tone từ G0]
- Độ dài: [số từ target] từ
- Giữ nguyên độ chính xác fact 100%. KHÔNG bịa thêm bất kỳ số liệu, tên, liều, hoặc fact nào không có trong input.
- Nếu thông tin input thiếu một điểm → ghi rõ "Dựa trên dữ liệu hiện có..." và gợi ý tham khảo chuyên gia.
- Phải cover gap này từ Gap List: [điểm gap được assign cho mảnh này]
- Format target: [prose / danh sách / bảng — dựa vào G2 featured snippet analysis]

KHÔNG được:
- Bắt đầu câu bằng "Điều quan trọng là", "Đáng chú ý rằng", "Rõ ràng là"
- Dùng "Hơn nữa", "Ngoài ra", "Bên cạnh đó" quá 2 lần trong một đoạn
- Viết toàn câu dài 20+ từ — phải có câu ngắn 8-12 từ xen kẽ
- Kết đoạn bằng "Tóm lại, rõ ràng rằng..."

// PHẦN 3: DATA INPUT
Dữ liệu input (đã extract và verify nguồn):
[Paste raw data từ G4 — ghi rõ: Nguồn: [tên] · Tier [1/2/3] · Ngày: [dd/mm/yyyy]]

// PHẦN 4: OUTPUT YÊU CẦU
Sau khi viết xong, liệt kê riêng:
1. 3 điểm chính bạn đã paraphrase từ input (để tôi verify)
2. Điểm gap từ Gap List đã được cover như thế nào
3. Điểm nào trong input chưa đủ sâu → cần user tìm thêm
```

---

## Tiêu chí Accept / Reject từng mảnh

### ✅ ACCEPT nếu:
- Mọi fact khớp 100% với data input — không có số liệu nào ngoài nguồn đã cung cấp
- Ít nhất 1 điểm từ Gap List được cover một cách cụ thể, không chung chung
- Không có pattern AI trong blacklist (xem `resources/blacklist_patterns.md`)
- Có câu ngắn xen kẽ câu dài. Không phải toàn câu phức tạp dài dòng

### ❌ REJECT nếu:
- Xuất hiện liều thuốc, tỷ lệ %, số liệu cụ thể nào không có trong data input
- Dài hơn 30% so với target mà không có nội dung mới thực sự — đó là padding
- Câu mở đầu bắt đầu bằng các pattern AI blacklist
- Không cover được gap nào từ Gap List

---

## Quy trình Revise — Tối đa 3 vòng

### R1 — Accuracy Check
So sánh từng fact với data input. Highlight bất kỳ số liệu/tên nào không có trong source.

Yêu cầu sửa specific:
> *"Liều X không có trong input, xóa hoặc thay bằng 'tham khảo bác sĩ thú y'."*

### R2 — Gap & Quality Check
Gap được cover chưa? Câu có tự nhiên không?

Yêu cầu sửa specific:
> *"Bổ sung bảng so sánh 4 loại thuốc đã có trong input. Viết lại câu đầu đoạn 2 — đang bắt đầu bằng 'Đáng chú ý'."*

### R3 — Final Polish
Đọc to lần cuối. Nhịp câu ổn không? Transition mượt không?

> ⚠️ Nếu sau 3 vòng vẫn chưa đạt → **dừng, flag cho user**, không tiếp tục loop vô hạn.

---

## Quy trình thực thi từng mảnh

```
[Mảnh Mn]
    ↓
Đọc raw data từ G4 cho mảnh này
    ↓
Điền prompt template (role + constraints + data + output)
    ↓
Viết draft
    ↓
R1: Accuracy check → sửa nếu cần
    ↓
R2: Gap + Quality → sửa nếu cần
    ↓
R3: Final polish → sửa nếu cần
    ↓
Accept? → Yes: lưu draft, sang mảnh tiếp
         → No (sau R3): flag user, chờ input thêm
```

**Hoàn thành một mảnh trước khi sang mảnh tiếp theo.**

---

## Output của G5

```
✅ Draft từng mảnh đã approve
✅ Checklist verify điểm cần kiểm tra thêm
✅ Ghi chú gap coverage của từng mảnh
```

**Tất cả mảnh đã approve → chuyển sang G6.**
