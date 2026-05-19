# Source Credibility Matrix — 4 Tier

Hướng dẫn đánh giá độ tin cậy của nguồn thông tin. Áp dụng bắt buộc ở G4.

---

## Tier 1 — Ưu tiên tuyệt đối ✅

> Với YMYL Cao: **CHỈ dùng Tier này**. Không ngoại lệ.

### Quốc tế
- WHO (World Health Organization)
- FAO (Food and Agriculture Organization)
- OIE (World Organisation for Animal Health)
- CDC (Centers for Disease Control)
- Nghiên cứu peer-reviewed có DOI trên PubMed, ScienceDirect, ResearchGate

### Việt Nam
- Bộ Nông nghiệp và Phát triển Nông thôn (NN&PTNT)
- Bộ Y tế
- Cục Thú y
- Cục An toàn thực phẩm
- Trường Đại học Nông nghiệp Hà Nội
- Trường Đại học Nông Lâm TP.HCM
- Học viện Nông nghiệp Việt Nam
- Viện Chăn nuôi Quốc gia

### Cách ghi nguồn Tier 1:
```
Nguồn: Cục Thú y | Tier 1 | Ngày: 15/03/2025 | URL: [link]
```

---

## Tier 2 — Chấp nhận được ✅

> Luôn ghi rõ tên nguồn và ngày publish. Chú thích conflict of interest nếu là nhà sản xuất.

### Tổ chức / Hiệp hội
- Hiệp hội Chăn nuôi Việt Nam
- Hiệp hội Thú y Việt Nam
- Hiệp hội Gia cầm Việt Nam
- Tạp chí chuyên ngành có ISSN (Khoa học Kỹ thuật Chăn nuôi, Thú y...)

### Doanh nghiệp / Chuyên gia
- Website chính thức của nhà sản xuất thuốc thú y uy tín (ghi rõ: *có thể có conflict of interest*)
- Bệnh viện thú y, phòng khám thú y có website chính thức
- Chuyên gia được công nhận bởi tổ chức ngành (có bio rõ ràng)

### Cách ghi nguồn Tier 2:
```
Nguồn: Công ty Vemedim | Tier 2 [⚠️ nhà sản xuất] | Ngày: 10/01/2025 | URL: [link]
```

---

## Tier 3 — Dùng thận trọng ⚠️

> Chỉ dùng khi Tier 1-2 không có thông tin cụ thể. **Không dùng độc lập** — cần có Tier 1/2 confirm cùng fact.

### Báo chí chính thống
- Báo Nông nghiệp Việt Nam (nongnghiep.vn)
- TTXVN (Vietnam+)
- VnExpress (chuyên mục Khoa học, Sức khỏe)
- Tuổi Trẻ (tin tức khoa học có chuyên gia dẫn chứng)
- Cổng thông tin điện tử tỉnh/huyện

### Cách ghi nguồn Tier 3:
```
Nguồn: Báo Nông nghiệp VN | Tier 3 | Ngày: 20/02/2025 | URL: [link]
⚠️ Cần xác nhận thêm bằng Tier 1/2
```

---

## Không dùng — Loại bỏ ngay ❌

| Loại nguồn | Lý do |
|-----------|-------|
| Blog không rõ tác giả | Không có accountability |
| Facebook group, diễn đàn | Không được verify |
| Wikipedia | Dùng để tìm source gốc trong phần references, không trích dẫn trực tiếp |
| TikTok, YouTube (trừ kênh chính thức tổ chức Tier 1/2) | Không peer-reviewed |
| Trang bán thuốc/sản phẩm không rõ nguồn | Quảng cáo, không objective |
| Mạng xã hội cá nhân | Dù là chuyên gia, cần website/tài liệu chính thức |

---

## Quick Reference — YMYL × Tier

| YMYL Level | Tier tối thiểu | Ghi chú |
|-----------|---------------|---------|
| YMYL Cao | Tier 1 ONLY | Sức khỏe người, thuốc, phẫu thuật |
| YMYL Trung bình | Tier 1-2 | Thú y, nông nghiệp — Tier 3 chỉ để bổ sung |
| YMYL Thấp | Tier 1-2-3 | Du lịch, ẩm thực, công nghệ |
| Non-YMYL | Bất kỳ có credibility | Giải trí, sở thích |

---

## Conflict of Interest — Cần ghi chú

Khi dùng nguồn có potential conflict of interest (nhà sản xuất, đơn vị có lợi ích kinh tế):

1. Ghi rõ trong raw data: `[⚠️ CoI: nhà sản xuất sản phẩm X]`
2. Trong bài viết, nếu trích dẫn: *"Theo [tên công ty], nhà sản xuất [sản phẩm X]..."*
3. Luôn cross-check với nguồn không có CoI
