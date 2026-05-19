# G0 — Project Intake & Scope Definition

## Vai trò của stage này

**Bắt buộc · Trước mọi bước khác**

Làm rõ tất cả thông tin đầu vào trước khi bắt đầu. Agent không được giả định bất cứ điều gì không được user xác nhận.

🎯 **Mục tiêu:** Có đủ context để thực thi toàn bộ quy trình mà không phải dừng hỏi giữa chừng.

---

## 8 câu hỏi bắt buộc — Hỏi user trước khi bắt đầu

Trình bày dưới dạng một form rõ ràng, hỏi tất cả 8 câu trong **một lần** (không hỏi lần lượt từng câu):

```
📋 Trước khi bắt đầu, em cần anh xác nhận một số thông tin:

1. 🏷️ LĨNH VỰC & WEBSITE
   Website thuộc lĩnh vực gì? (thú y, ẩm thực, tài chính, sức khỏe, công nghệ, du lịch...)
   Loại website: blog cá nhân / e-commerce / trang chuyên ngành / doanh nghiệp?

2. 👥 AUDIENCE MỤC TIÊU
   Người đọc là ai? Trình độ hiểu biết:
   □ Người dùng phổ thông mới tìm hiểu
   □ Người có kiến thức cơ bản
   □ Chuyên gia / kỹ thuật viên
   (Ví dụ: "nông dân nhỏ lẻ ĐBSCL" khác hoàn toàn "kỹ sư chăn nuôi trang trại lớn")

3. 🔑 KEYWORD MỤC TIÊU
   Keyword chính là gì?
   Đã có search volume data chưa?
   Có keyword phụ / LSI keyword muốn cover không?

4. 🌐 DOMAIN WEBSITE
   Domain cụ thể là gì? (bắt buộc để check cannibalization)
   Ví dụ: trangtraiviet.com, suckhoe123.vn

5. 📏 ĐỘ DÀI BÀI VIẾT
   □ Ngắn ~1500 từ
   □ Trung bình ~2500 từ
   □ Dài ~3500+ từ
   □ Để em tự xác định dựa vào SERP

6. 🗣️ TONE & VOICE
   □ Thân thiện / gần gũi phổ thông
   □ Chuyên môn học thuật
   □ Thực chiến có số liệu
   □ Brand voice riêng (nếu có, cung cấp 1-2 bài mẫu)

7. 📐 FORMAT ĐẶC BIỆT
   Cần format nào? (tick tất cả phù hợp)
   □ Bảng so sánh  □ Checklist  □ Warning/Danger box
   □ FAQ section   □ Infographic gợi ý  □ Để em tự quyết

8. 📚 DANH SÁCH BÀI ĐÃ PUBLISH
   Có file/doc danh sách bài cũ (keyword, URL) không?
   Nếu không có → em sẽ dùng site: search để check
```

---

## Xử lý thông tin sau khi nhận từ user

### Bước 1: Xác định YMYL Level

Dựa vào lĩnh vực website, phân loại ngay:

| Level | Lĩnh vực | Xử lý |
|-------|----------|-------|
| ⚠️ **YMYL Cao** | Sức khỏe người, thuốc, tài chính cá nhân, pháp lý, an toàn thực phẩm | Chỉ dùng Tier 1 source. Bắt buộc có disclaimer. Không đưa khuyến nghị tuyệt đối. |
| ~ **YMYL Trung bình** | Thú y, nông nghiệp, sức khỏe động vật, dinh dưỡng | Tier 1-2 source. Disclaimer ở phần điều trị/liều lượng. |
| ✓ **YMYL Thấp** | Du lịch, ẩm thực, công nghệ, lifestyle, làm đẹp, giáo dục | Quy trình standard. Không cần disclaimer đặc biệt. |
| ⊘ **Non-YMYL** | Giải trí, game, mẹo vặt, sở thích cá nhân | Có thể rút gọn số mảnh, bỏ một số bước verify. |

### Bước 2: Xác định số mảnh target

- ~1500 từ → **5 mảnh**
- ~2500 từ → **6-7 mảnh**
- ~3500+ từ → **7-8 mảnh**

### Bước 3: Tổng hợp Intake Brief

Điền vào template `templates/intake_brief.md` với thông tin đã thu thập. Output trực tiếp cho user xác nhận trước khi sang G1.

---

## Output của G0

```
✅ Intake Brief đầy đủ
✅ YMYL Level đã xác định
✅ Tone Profile đã ghi nhận
✅ Content Map nếu user cung cấp
```

**Sau khi user confirm Intake Brief → chuyển sang G1.**

---

## ⚠️ Lưu ý quan trọng

- Nếu user không cung cấp domain → **DỪNG, yêu cầu domain trước khi tiếp tục**. Không thể check cannibalization mà không có domain.
- Nếu user không có keyword data → ghi nhận và thực hiện basic keyword research ở bước này bằng `search_web`.
- Nếu user cung cấp brand voice mẫu → đọc kỹ tone trước khi viết.
