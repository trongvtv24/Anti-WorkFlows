# G4 — Targeted Querying + Source Scoring

## Vai trò của stage này

**Thu thập & Verify dữ liệu**

Query hẹp theo từng mảnh, đánh giá nguồn theo Tier, giải quyết mâu thuẫn giữa nguồn. Không dùng knowledge nội tại nếu không có trong search.

🎯 **Mục tiêu:** Có raw data chính xác, có nguồn gốc rõ ràng, cho từng mảnh — sẵn sàng để viết.

---

## Source Credibility Matrix — 4 Tier

### Tier 1 — Bắt buộc với YMYL Cao ✅
> Ưu tiên tuyệt đối. Với topic YMYL cao, **chỉ dùng Tier này**.

- Cơ quan nhà nước: Bộ NN&PTNT, Cục Thú y, Bộ Y tế, WHO, FAO, OIE
- Nghiên cứu peer-reviewed có DOI
- Trường đại học nông nghiệp/y khoa chính thống
- Tổ chức quốc tế uy tín

### Tier 2 — Chấp nhận được ✅
> Luôn ghi rõ tên nguồn và ngày publish.

- Hiệp hội ngành nghề có uy tín
- Tạp chí chuyên ngành có ISSN
- Nhà sản xuất uy tín (ghi chú conflict of interest)
- Bệnh viện/phòng khám có website chính thức
- Chuyên gia được công nhận trong lĩnh vực

### Tier 3 — Dùng thận trọng ⚠️
> Chỉ dùng khi Tier 1-2 không có thông tin cụ thể. KHÔNG dùng độc lập.

- Báo Nông nghiệp Việt Nam, TTXVN
- VnExpress chuyên mục khoa học
- Cổng thông tin chính phủ địa phương
- Báo chí chính thống khác

### KHÔNG dùng — Loại bỏ ❌
- Blog không rõ tác giả
- Diễn đàn (Facebook group, forum)
- Wikipedia (chỉ dùng để tìm source gốc trong phần references)
- Mạng xã hội cá nhân
- Các site không rõ nguồn gốc chuyên môn

---

## Quy trình query cho từng mảnh

**Thực hiện tuần tự từng mảnh (M1 → M2 → ... → Mn)**

### Bước 1: Tạo query hẹp + intent rõ ràng

Thêm từ khóa chỉ định scope:
- `"nguyên nhân"`, `"triệu chứng"`, `"liều lượng"`, `"phòng ngừa"`
- `"nghiên cứu 2025"`, `"Việt Nam"`, `"ĐBSCL"`

> ❌ Thay vì: `sán dây gà`
> ✅ Dùng: `liều thuốc trị sán dây gà con Praziquantel Việt Nam 2025`

### Bước 2: Ưu tiên AI Overview nhưng không phụ thuộc

- Lấy AI Overview làm điểm khởi đầu
- **Nếu AI Overview thiếu depth, outdated, hoặc không hiển thị:** dùng `browser_subagent` để browse trực tiếp top 3-5 kết quả Tier 1-2
- Tóm tắt bullet các fact then chốt và ghi nguồn

### Bước 3: Extract chỉ phần đúng scope của mảnh

Query overview cho mảnh "nguyên nhân" → chỉ extract phần nguyên nhân, bỏ qua phần điều trị xuất hiện trong cùng kết quả.

> Giữ scope sạch để tránh content overlap giữa mảnh.

### Bước 4: Ghi chú đầy đủ metadata của data

Với mỗi fact quan trọng:
```
Fact: [nội dung fact]
Nguồn: [tên nguồn]
Tier: [1/2/3]
Ngày publish: [dd/mm/yyyy]
URL: [link]
```

> Fact không có nguồn = **không dùng được**. Với số liệu cụ thể (liều thuốc, tỷ lệ %, chi phí) → bắt buộc có nguồn Tier 1 hoặc 2.

### Bước 5: Tìm kiếm gap data chủ động

Dựa vào Gap List từ G2, query cụ thể để tìm:
- Số liệu địa phương VN
- Case study thực tế
- So sánh sản phẩm cụ thể

**Nếu search kỹ vẫn không tìm được:**
→ Ghi: `"Chưa tìm thấy đủ dữ liệu — cần verify thêm"` và flag cho user.
→ **Tuyệt đối không suy diễn hay bịa số liệu.**

---

## Conflict Resolution — Khi nguồn mâu thuẫn nhau

```
┌──────────────────────────────┬──────────────────────────────────────────────┐
│ Tình huống                   │ Xử lý                                        │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Tier khác nhau               │ Ưu tiên Tier cao hơn. Ghi rõ:               │
│                              │ "Theo [Tier 1 source], [fact]. Một số nguồn  │
│                              │ khác ghi nhận [biến thể]."                   │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Cùng Tier, ngày khác         │ Ưu tiên nguồn mới hơn. Ghi ngày publish      │
│                              │ của cả hai để user có thể verify.            │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Cùng Tier, cùng thời điểm    │ Ghi nhận cả hai quan điểm. Thêm câu:        │
│                              │ "Liều/thông số có thể khác nhau tùy điều     │
│                              │ kiện cụ thể — tham khảo chuyên gia."         │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Không giải quyết được        │ Flag cho user TRƯỚC khi viết. Không tự       │
│                              │ quyết với thông tin có thể gây hại.          │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

---

## Template Raw Data Dump — cho từng mảnh

```markdown
## RAW DATA — [Tên mảnh]

### Fact 1: [Tiêu đề ngắn]
[Nội dung fact]
— Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy] | URL: [link]

### Fact 2: [Tiêu đề ngắn]
[Nội dung fact]
— Nguồn: [tên] | Tier [1/2/3] | Ngày: [dd/mm/yyyy] | URL: [link]

### ⚠️ Flag cần verify:
- [Fact chưa đủ source]
- [Mâu thuẫn giữa nguồn A và B]

### Gap coverage:
- Gap [X] từ Gap List: [tìm được / chưa đủ dữ liệu]
```

---

## ⚠️ Quy tắc cứng — Không ngoại lệ

> Agent **không được dùng knowledge nội tại** để bổ sung thông tin nếu không tìm thấy trong kết quả search. Thà ghi rõ "Chưa đủ dữ liệu để xác nhận" còn hơn hallucinate số liệu y tế, liều thuốc, hay thống kê. Một số liệu sai trong bài thú y/y tế có thể gây hại thực tế.

---

## Output của G4

```
✅ Raw data dump theo từng mảnh
✅ Nguồn ghi rõ Tier + ngày
✅ Flag list điểm cần user verify
✅ Conflict notes (nếu có)
```

**Hoàn tất data đủ cho tất cả mảnh → chuyển sang G5.**
**Nếu có flag quan trọng → báo user trước khi tiếp tục.**
