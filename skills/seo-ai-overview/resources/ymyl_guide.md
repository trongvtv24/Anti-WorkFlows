# YMYL Classification Guide

Hướng dẫn phân loại YMYL (Your Money or Your Life) và cách xử lý tương ứng. Xác định ngay từ G0.

---

## Phân loại YMYL

### ⚠️ YMYL Cao — Yêu cầu nghiêm ngặt nhất

**Lĩnh vực:**
- Sức khỏe con người: bệnh tật, thuốc, phẫu thuật, tâm lý
- Tài chính cá nhân: đầu tư, bảo hiểm, tín dụng, tiết kiệm
- Pháp lý: hợp đồng, quyền lợi, tố tụng
- An toàn thực phẩm (ảnh hưởng sức khỏe người)
- An toàn công cộng: tai nạn, thiên tai, khẩn cấp

**Yêu cầu bắt buộc:**
- ✅ Chỉ dùng **Tier 1 source**
- ✅ Có disclaimer rõ ràng tại MỌI phần có liều lượng/khuyến nghị y tế
- ✅ Không đưa ra khuyến nghị tuyệt đối ("chắc chắn chữa khỏi", "100% an toàn")
- ✅ Có câu chuyển về chuyên gia: "Tham khảo bác sĩ/chuyên gia trước khi thực hiện"
- ✅ Cân nhắc ghi rõ tác giả/reviewer có chuyên môn

**Template disclaimer YMYL Cao:**
```
⚠️ Lưu ý: Thông tin trong bài này chỉ mang tính tham khảo giáo dục.
Không thay thế cho tư vấn y tế chuyên nghiệp. Vui lòng tham khảo
bác sĩ hoặc chuyên gia y tế được cấp phép trước khi thực hiện bất
kỳ phương pháp điều trị nào.
```

---

### ~ YMYL Trung bình — Thận trọng

**Lĩnh vực:**
- Thú y: bệnh động vật, thuốc thú y, phẫu thuật thú y
- Nông nghiệp: thuốc bảo vệ thực vật, phân bón, quy trình chăn nuôi
- Sức khỏe động vật nuôi
- Dinh dưỡng (thực vật/động vật, không phải người)

**Yêu cầu:**
- ✅ Dùng **Tier 1-2 source**. Tier 3 chỉ bổ sung
- ✅ Disclaimer tại phần điều trị/liều lượng
- ✅ Ghi rõ: liều lượng có thể thay đổi theo điều kiện cụ thể
- ✅ Câu chuyển: "Tham khảo bác sĩ thú y trước khi dùng thuốc"

**Template disclaimer YMYL Trung bình:**
```
Lưu ý: Liều lượng và phác đồ điều trị trên chỉ mang tính tham khảo.
Thực tế có thể khác nhau tùy thuộc vào trọng lượng, tuổi, tình trạng
sức khỏe cụ thể của từng con vật. Hãy tham khảo bác sĩ thú y
trước khi áp dụng.
```

---

### ✓ YMYL Thấp — Quy trình standard

**Lĩnh vực:**
- Du lịch, khách sạn, nhà hàng
- Ẩm thực (công thức nấu ăn thông thường)
- Công nghệ, phần mềm, gadget
- Lifestyle, thời trang, làm đẹp (không liên quan y tế)
- Giáo dục phổ thông

**Yêu cầu:**
- Quy trình standard — không cần disclaimer đặc biệt
- Tier 1-2-3 đều có thể dùng (ưu tiên theo thứ tự)
- Không có quy tắc source đặc biệt

---

### ⊘ Non-YMYL — Linh hoạt nhất

**Lĩnh vực:**
- Giải trí, phim ảnh, âm nhạc
- Game, esports
- Mẹo vặt, DIY, sở thích cá nhân
- Humor, lifestyle nhẹ nhàng

**Yêu cầu:**
- Quy trình đơn giản hóa
- Có thể rút gọn số mảnh (5 mảnh thay vì 8)
- Có thể bỏ qua một số bước verify chặt chẽ
- Source không cần Tier nghiêm ngặt

---

## Decision Flow — Xác định YMYL

```
Bài viết về sức khỏe người / tài chính / pháp lý?
  → Có → YMYL CAO

Bài về thú y / nông nghiệp / sức khỏe động vật?
  → Có → YMYL TRUNG BÌNH

Bài về du lịch / ẩm thực / công nghệ / lifestyle?
  → Có → YMYL THẤP

Còn lại (giải trí, game, mẹo vặt)?
  → NON-YMYL
```

---

## YMYL và E-E-A-T

Google đánh giá cao E-E-A-T đặc biệt với YMYL. Cách thể hiện trong bài:

| Yếu tố | Cách thể hiện |
|--------|--------------|
| **Experience** | Case study thực tế, ví dụ cụ thể từ thực tế |
| **Expertise** | Dẫn chuyên gia, trích nguồn Tier 1 |
| **Authoritativeness** | Cite tổ chức uy tín, link ra ngoài Tier 1 |
| **Trustworthiness** | Disclaimer rõ ràng, thừa nhận giới hạn, không overclaim |
