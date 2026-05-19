# QA Checklist — 8 Tiêu chí

Dùng trong G7 để agent tự kiểm tra trước khi bàn giao. In ra hoặc copy vào Handoff Package.

---

## FINAL QA CHECKLIST — [Keyword]

**Ngày QA:** [dd/mm/yyyy]
**Agent chạy QA:** SEO AI Overview v2.0

---

### ① Fact Accuracy ☐ PASS ☐ FAIL

**Yêu cầu:** Mọi số liệu, tên thuốc/sản phẩm, liều lượng, tỷ lệ %, triệu chứng đều khớp ít nhất 2 nguồn độc lập.

**Check:**
- [ ] Đã đọc lại toàn bài và highlight mọi fact cụ thể?
- [ ] Mọi fact đều có trong raw data G4?
- [ ] Không có số liệu nào không rõ nguồn?

**Kết quả:** ☐ PASS ☐ FAIL
**Ghi chú (nếu FAIL):** _______________

---

### ② Gap Coverage ☐ PASS ☐ FAIL

**Yêu cầu:** Ít nhất 3/5 gap trong Gap List được cover cụ thể, đọc được và xác nhận trong bài.

**Check:**
- [ ] Gap 1: ☐ Covered ☐ Chưa ☐ N/A
- [ ] Gap 2: ☐ Covered ☐ Chưa ☐ N/A
- [ ] Gap 3: ☐ Covered ☐ Chưa ☐ N/A
- [ ] Gap 4: ☐ Covered ☐ Chưa ☐ N/A
- [ ] Gap 5: ☐ Covered ☐ Chưa ☐ N/A

**Tổng:** [N]/5 gap covered

**Kết quả:** ☐ PASS (≥3/5) ☐ FAIL (<3/5)
**Ghi chú:** _______________

---

### ③ Anti-AI Pattern ☐ PASS ☐ FAIL

**Yêu cầu:** Không có pattern nào trong blacklist. Nhịp câu tự nhiên.

**Check:**
- [ ] Đã đọc to 3 đoạn ngẫu nhiên — nghe tự nhiên?
- [ ] Không có câu bắt đầu bằng "Điều quan trọng là / Đáng chú ý rằng / Rõ ràng là"?
- [ ] "Hơn nữa / Ngoài ra / Bên cạnh đó" mỗi từ ≤ 2 lần/bài?
- [ ] Có câu ngắn (8-12 từ) xen kẽ trong mỗi đoạn?
- [ ] Không có đoạn kết kiểu "Tóm lại, rõ ràng rằng..."?
- [ ] Không quá 2 câu passive liên tiếp?

**Kết quả:** ☐ PASS ☐ FAIL
**Pattern tìm thấy (nếu FAIL):** _______________

---

### ④ YMYL Compliance ☐ PASS ☐ FAIL ☐ N/A

**YMYL Level (từ G0):** [ ] Cao [ ] Trung bình [ ] Thấp [ ] Non-YMYL

**Check (chỉ với YMYL Cao/Trung bình):**
- [ ] Có disclaimer rõ ràng tại phần điều trị/liều lượng?
- [ ] Không có câu "chắc chắn chữa khỏi / 100% an toàn / đảm bảo hiệu quả"?
- [ ] Có câu "tham khảo bác sĩ / chuyên gia" ít nhất 1 lần trong phần M4?
- [ ] Source tại M4 đều Tier 1-2?

**Kết quả:** ☐ PASS ☐ FAIL ☐ N/A (Non-YMYL)
**Ghi chú:** _______________

---

### ⑤ SEO Structure ☐ PASS ☐ FAIL

**Check:**
- [ ] H1 (title) chứa keyword chính?
- [ ] Keyword xuất hiện trong Sapo (100-150 từ đầu)?
- [ ] Keyword có trong ít nhất 2 H2 quan trọng?
- [ ] Heading hierarchy đúng thứ tự H1→H2→H3 (không có H3 mà không có H2 cha)?
- [ ] Title ≤ 65 ký tự?
- [ ] Keyword không bị nhồi nhét vào 1 đoạn duy nhất?

**Kết quả:** ☐ PASS ☐ FAIL
**Ghi chú:** _______________

---

### ⑥ Meta Assets ☐ PASS ☐ FAIL

**Check:**
- [ ] Meta description đã viết?
- [ ] Meta description ≤ 155 ký tự?
- [ ] Meta description có keyword chính?
- [ ] Alt text cho 3-5 ảnh?
- [ ] Internal link placeholder có anchor text tự nhiên?
- [ ] FAQ schema JSON-LD đã draft (nếu có FAQ)?
- [ ] JSON-LD valid (không có lỗi cú pháp)?

**Số ký tự meta description:** _____ / 155

**Kết quả:** ☐ PASS ☐ FAIL
**Ghi chú:** _______________

---

### ⑦ Cannibalization Final ☐ PASS ☐ FAIL

**Check:**
- [ ] Keyword + intent không trùng với bài nào trong Content Map hiện tại?
- [ ] Content Map đã được cập nhật với entry mới?

**Kết quả:** ☐ PASS ☐ FAIL
**Bài trùng (nếu FAIL):** _______________

---

### ⑧ Format & Readability ☐ PASS ☐ FAIL

**Check:**
- [ ] Heading hierarchy dùng # / ## / ### đúng?
- [ ] Các format đặc biệt đã yêu cầu ở G0 có đủ? (bảng / checklist / warning box)
- [ ] Không có ký tự lạ, link broken, formatting lỗi?
- [ ] Sẵn sàng paste vào CMS không cần chỉnh sửa lớn?
- [ ] Internal link placeholder đã đánh dấu rõ?

**Kết quả:** ☐ PASS ☐ FAIL
**Ghi chú:** _______________

---

## KẾT QUẢ TỔNG

| Tiêu chí | Kết quả |
|---------|---------|
| ① Fact Accuracy | ☐ PASS ☐ FAIL |
| ② Gap Coverage | ☐ PASS ☐ FAIL |
| ③ Anti-AI Pattern | ☐ PASS ☐ FAIL |
| ④ YMYL Compliance | ☐ PASS ☐ FAIL ☐ N/A |
| ⑤ SEO Structure | ☐ PASS ☐ FAIL |
| ⑥ Meta Assets | ☐ PASS ☐ FAIL |
| ⑦ Cannibalization | ☐ PASS ☐ FAIL |
| ⑧ Format | ☐ PASS ☐ FAIL |

**TỔNG:** [  ]/8 PASS

**Sẵn sàng bàn giao:** ☐ Có — đạt đủ tiêu chí ☐ Chưa — cần sửa trước

---

## Các điểm cần sửa trước khi bàn giao

1. _______________
2. _______________
3. _______________
