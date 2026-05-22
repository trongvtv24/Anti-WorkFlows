# G7 — Final QA — 8 Tiêu chí

## Vai trò của stage này

**Kiểm soát chất lượng cuối**

Agent tự chạy toàn bộ checklist trước khi bàn giao. **Bài không qua QA không được bàn giao cho user.**

🎯 **Mục tiêu:** Bài đạt chuẩn publish — không để lỗi đến tay editor.

---

## QA Checklist — 8 Tiêu chí bắt buộc

Chạy từng tiêu chí, đánh dấu **PASS** hoặc **FAIL + ghi chú cụ thể**:

---

### ① Fact Accuracy

**Yêu cầu:** Mọi số liệu, tên thuốc/sản phẩm, liều lượng, tỷ lệ %, triệu chứng đều khớp ít nhất 2 nguồn độc lập. Nguồn được ghi rõ hoặc available để verify.

**Cách check:**
- Đọc lại toàn bài, highlight mọi số liệu/fact cụ thể
- Đối chiếu với raw data từ G4
- Bất kỳ fact nào không có trong raw data → FAIL

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Ghi chú: ___`

---

### ② Gap Coverage

**Yêu cầu:** Ít nhất 3/5 điểm trong Gap List (từ G2) đã được cover cụ thể, có thể đọc và xác nhận trong bài. Không phải chỉ mention thoáng qua.

**Cách check:**
- Mở Gap List từ G2
- Tìm từng gap trong bài — nó được cover ở section nào, cụ thể như thế nào?
- "Mention thoáng qua" ≠ "cover cụ thể"

**Kết quả:** `[ ] PASS ([N]/5 gap covered)` / `[ ] FAIL — Gap thiếu: ___`

---

### ③ Anti-AI Pattern

**Yêu cầu:** Không có pattern nào trong blacklist G6. Đọc to 3 đoạn ngẫu nhiên — nhịp câu có tự nhiên không? Không phải toàn câu dài đều nhau.

**Cách check:**
- Đọc to đoạn mở bài, một đoạn giữa bài, đoạn kết bài
- Kiểm tra từng pattern trong `resources/blacklist_patterns.md`
- Đặc biệt: câu đầu các đoạn không bắt đầu bằng pattern AI

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Pattern tìm thấy: ___`

---

### ④ YMYL Compliance

**Yêu cầu:** Nếu là topic YMYL (cao hoặc trung bình): có disclaimer rõ ràng tại phần điều trị/liều lượng, không đưa ra khuyến nghị tuyệt đối, có câu "tham khảo chuyên gia/bác sĩ".

**Cách check:**
- Xác nhận YMYL level từ G0
- Nếu YMYL cao/trung bình: tìm disclaimer trong M4 (Giải pháp/Điều trị)
- Không có từ như "chắc chắn", "100% hiệu quả", "đảm bảo chữa khỏi"

**Kết quả:** `[ ] PASS` / `[ ] N/A (Non-YMYL)` / `[ ] FAIL — Thiếu: ___`

---

### ⑤ SEO Structure

**Yêu cầu:** H1 có keyword chính, H2 bao phủ intent chính, keyword xuất hiện tự nhiên (không dồn vào 1 đoạn), heading hierarchy H1→H2→H3 đúng thứ tự.

**Cách check:**
- H1 (title) chứa keyword chính?
- Keyword xuất hiện trong: H1, Sapo, 1-2 H2 đầu, đoạn kết?
- Không có H3 mà không có H2 cha?
- Keyword density hợp lý (không cảm giác nhồi nhét)?

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Vấn đề: ___`

---

### ⑥ Meta Assets

**Yêu cầu:** Meta description ~150-155 ký tự có keyword. Alt text cho ảnh. FAQ schema JSON-LD (nếu có FAQ). Internal link placeholder với anchor text.

**Cách check:**
- Meta description: đếm ký tự, có keyword không, không cắt giữa chừng?
- Alt text: có đủ 3-5 ảnh không?
- FAQ schema: valid JSON không? Tất cả Q&A trong FAQ đều vào schema không?
- Internal links: có anchor text tự nhiên, không phải "click vào đây"?

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Thiếu: ___`

---

### ⑦ Cannibalization Final

**Yêu cầu:** Confirm lần cuối: bài mới không trùng exact keyword + intent với bất kỳ bài nào trên site. Content Map đã được cập nhật với bài mới này.

**Cách check:**
- Keyword và intent có giống với bài nào trong Content Map không?
- Content Map đã thêm entry mới chưa?

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Trùng với: ___`

---

### ⑧ Format & Readability

**Yêu cầu:** Sẵn sàng paste vào CMS (Markdown hoặc HTML cơ bản). Có đủ format đặc biệt theo yêu cầu G0. Không có ký tự lạ hay formatting lỗi.

**Cách check:**
- Format đặc biệt đã yêu cầu ở G0 (bảng, checklist, warning box) có đủ không?
- Heading hierarchy rõ ràng bằng #, ##, ### ?
- Không có ký tự thừa, link broken, ký tự lạ?

**Kết quả:** `[ ] PASS` / `[ ] FAIL — Vấn đề: ___`

---

## QA Report — Template bàn giao

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 QA REPORT — "[keyword]"
Ngày QA: [dd/mm/yyyy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① Fact Accuracy          [PASS / FAIL]: ___
② Gap Coverage           [PASS / FAIL]: ___ gap covered
③ Anti-AI Pattern        [PASS / FAIL]: ___
④ YMYL Compliance        [PASS / FAIL / N/A]: ___
⑤ SEO Structure          [PASS / FAIL]: ___
⑥ Meta Assets            [PASS / FAIL]: ___
⑦ Cannibalization Final  [PASS / FAIL]: ___
⑧ Format & Readability   [PASS / FAIL]: ___

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KẾT QUẢ TỔNG: [X/8 PASS]

⚠️ CẦN SỬA TRƯỚC KHI PUBLISH:
  • [Mục 1 cần sửa]
  • [Mục 2 cần sửa]

✅ SẴN SÀNG BÀNG GIAO: [Có / Chưa — cần sửa trước]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Handoff Package — 5 items bàn giao cho user

Sau khi QA đạt (8/8 PASS hoặc các FAIL đã được sửa):

### Item 1: Full Draft Bài Viết
- Format: Markdown hoặc HTML cơ bản
- Bao gồm: đầy đủ heading hierarchy, internal link placeholder, warning box, bảng, checklist
- Sẵn sàng paste vào CMS

### Item 2: QA Report
- 8 tiêu chí với trạng thái PASS/FAIL
- Ghi chú cụ thể nếu có vấn đề còn lại

### Item 3: Verify List cho User
Những điểm agent không thể tự verify hoàn toàn:
- Số liệu thiếu source chắc chắn
- Điểm mâu thuẫn giữa nguồn chưa giải quyết được
- Fact cần chuyên gia trong ngành xác nhận

Format:
```
⚠️ VERIFY LIST — Anh cần kiểm tra trước khi publish:
1. [Fact X] — Nguồn: [Y] — Cần: [xác nhận / tìm source chắc hơn]
2. [Fact Z] — Mâu thuẫn giữa [A] và [B] — Cần: [quyết định dùng source nào]
```

### Item 4: Meta Assets
- Meta description (~155 ký tự)
- Alt text gợi ý (3-5 ảnh, sắp xếp theo thứ tự trong bài)
- FAQ schema JSON-LD (sẵn sàng paste vào `<head>` hoặc plugin schema)

### Item 5: Content Map cập nhật
Entry mới cần thêm vào Content Map:
```
Keyword: [keyword chính]
URL dự kiến: [slug gợi ý]
Search intent: [informational/transactional/navigational]
YMYL level: [cao/trung bình/thấp/non-YMYL]
Ngày tạo: [dd/mm/yyyy]
Status: [draft → cần review]
```

---

## ⚠️ Khi nào KHÔNG nên dùng framework này

> Framework này **không phù hợp** khi:
> 1. Topic cần original research, dữ liệu điều tra thực địa — phải có người thực viết
> 2. Muốn tạo nội dung thực sự evergreen và khác biệt về tư duy — cần author có expertise thật
> 3. Topic cực kỳ nhạy cảm mà agent không thể verify độc lập
>
> Trong những trường hợp này, framework là hỗ trợ nghiên cứu và outline — không phải viết toàn bộ.

---

## Output của G7 — Handoff hoàn chỉnh

```
✅ Bài viết hoàn chỉnh (Markdown/HTML)
✅ QA Report 8 tiêu chí
✅ Verify List cho user
✅ Meta Assets đầy đủ
✅ Content Map entry mới
```
