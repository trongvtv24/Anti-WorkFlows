# G6 — Assembly + Humanization + Internal Linking

## Vai trò của stage này

**Lắp ghép & Tinh chỉnh**

Lắp ghép các mảnh thành bài hoàn chỉnh, loại bỏ toàn bộ pattern AI, chèn internal link, và tạo meta assets.

🎯 **Mục tiêu:** Bài đọc như người viết — không gây déjà vu với top 5 SERP — sẵn sàng publish.

---

## Phần A: Cấu trúc bài hoàn chỉnh — Theo thứ tự

### A1. Title (H1) — Tối ưu keyword + lợi ích + năm

**Công thức:**
```
[Keyword chính]: [Lợi ích cụ thể hoặc con số] [Năm]
```

Tiêu chuẩn:
- Tối đa **65 ký tự**
- Keyword phải xuất hiện đầu tiên
- Có năm hiện tại (tăng CTR)

Ví dụ tốt:
> *"Bệnh Sán Dây ở Gà Con: Nguyên Nhân, Điều Trị & Phòng Ngừa Hiệu Quả 2026"*

### A2. Sapo / Mở bài — 100-150 từ

**Cấu trúc:**
1. Nêu vấn đề thực tế (không phải định nghĩa khô khan)
2. Thiệt hại/hậu quả cụ thể nếu bỏ qua
3. Những gì bài này sẽ giải quyết (không viết "Bài viết này sẽ hướng dẫn…")
4. Câu chuyển tự nhiên vào nội dung

> ❌ **Không bắt đầu bằng định nghĩa.** Ví dụ sai: "Sán dây là loại ký sinh trùng..."
> ✅ **Bắt đầu bằng vấn đề thực tế.** Ví dụ đúng: "Đàn gà con của anh đang bỏ ăn, xù lông dù thời tiết ổn..."

### A3. Nội dung chính (H2s) — Theo thứ tự mảnh từ G3

- Chèn từng mảnh đã approve vào đúng vị trí
- Thêm câu **transition ngắn** (1-2 câu) giữa các mảnh để bài mượt mà
- Không để heading đứng liền nhau mà không có câu dẫn

### A4. FAQ Section — Từ PAA list G2

Format chuẩn:
```
**Q: [câu hỏi nguyên văn từ PAA]**

A: [trả lời 80-150 từ, súc tích, đủ đứng độc lập không cần đọc bài]
```

3-5 câu Q&A. Phần này quan trọng cho schema markup và featured snippet.

### A5. Kết bài — Takeaway + CTA cụ thể

- Tóm **3 điểm hành động cụ thể** người đọc cần làm ngay
- CTA rõ ràng, không phải "Liên hệ chúng tôi"

Ví dụ tốt:
> *"Nếu gà con có triệu chứng xù lông kèm tiêu chảy, bước đầu tiên là cách ly ngay và kiểm tra phân dưới kính hiển vi..."*

---

## Phần B: Blacklist Pattern AI — Cấm tuyệt đối

Đọc chi tiết tại `resources/blacklist_patterns.md`. Tóm tắt nhanh:

| Pattern | Ví dụ bị cấm |
|---------|-------------|
| Câu mở đầu AI-style | "Điều quan trọng là…" / "Đáng chú ý rằng…" / "Rõ ràng là…" |
| Transition lặp | "Hơn nữa" / "Ngoài ra" / "Bên cạnh đó" — tối đa 2 lần/bài |
| Cấu trúc AI đặc trưng | "Không chỉ A mà còn B" liên tiếp nhiều câu |
| Đoạn kết sáo rỗng | "Tóm lại, rõ ràng rằng…" / "Như đã phân tích ở trên…" |
| Passive voice liên tiếp | "được thực hiện / được áp dụng / được đề xuất" — không quá 2 câu liên tiếp |
| Câu dài đồng đều | Toàn đoạn câu 20+ từ — phải có câu 8-12 từ xen kẽ mỗi 3 câu |
| Fluff | "Đây là vấn đề rất quan trọng cần được quan tâm đúng mức" không có fact sau |

### Cách check nhanh:

Đọc to 3 đoạn ngẫu nhiên trong bài:
- Có nghe tự nhiên không?
- Có bắt gặp pattern nào trong bảng trên không?
- Nhịp câu có đa dạng (ngắn - dài xen kẽ) không?

---

## Phần C: Internal Linking Protocol

### C1. Tìm bài liên quan từ Content Map

Dùng danh sách bài đã publish (từ G0) để tìm bài có topic liên quan tự nhiên.
> Chỉ link khi thực sự phù hợp ngữ cảnh — không link cưỡng bức.

### C2. Chèn placeholder vào đúng vị trí

Format placeholder:
```
[INTERNAL LINK → "Tên bài cụ thể" / URL nếu biết]
```

Ví dụ:
```
[INTERNAL LINK → "Bệnh cầu trùng ở gà: hướng dẫn phòng ngừa"]
```

Chèn vào ngay câu có context liên quan, **không phải cuối bài**.

### C3. Anchor text tự nhiên

| ❌ Sai | ✅ Đúng |
|--------|---------|
| "click vào đây" | "hướng dẫn phòng ngừa cầu trùng ở gà" |
| "[keyword exact match]" | "bảng so sánh các loại vắc-xin gia cầm" |
| "xem thêm" | "cách phân biệt sán dây và cầu trùng" |

### C4. Giới hạn số lượng

```
Tối đa 3-4 internal link / 1500 từ
Tỷ lệ: ~2 link / 1000 từ
```

Quá nhiều link = dấu hiệu spam với Google và làm giảm UX.

---

## Phần D: Meta Assets — Draft sẵn trong G6

### D1. Meta Description

```
Công thức: [Keyword chính] + [1 lợi ích cụ thể] + [CTA ngắn]
Độ dài: ~150-155 ký tự (không cắt giữa chừng)
```

Ví dụ tốt:
> *"Tìm hiểu nguyên nhân, triệu chứng và cách điều trị bệnh sán dây ở gà con đúng cách. Hướng dẫn thực tế từ chuyên gia thú y Việt Nam."*

### D2. Alt Text gợi ý (3-5 ảnh)

Format:
```
Ảnh 1: [mô tả cụ thể] — [keyword phụ tự nhiên]
Ví dụ: "Gà con bị sán dây với triệu chứng xù lông và kém ăn"
```

### D3. FAQ Schema JSON-LD

Nếu bài có FAQ section, draft sẵn JSON-LD:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Câu hỏi 1 từ FAQ]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Câu trả lời 1]"
      }
    },
    {
      "@type": "Question",
      "name": "[Câu hỏi 2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Câu trả lời 2]"
      }
    }
  ]
}
```

---

## Output của G6

```
✅ Full draft bài hoàn chỉnh có heading hierarchy
✅ Meta description ~155 ký tự
✅ Alt text gợi ý (3-5 ảnh)
✅ Internal link placeholder với anchor text
✅ FAQ schema JSON-LD (nếu có FAQ section)
```

**Hoàn tất G6 → chuyển sang G7 Final QA.**
