---
description: Phân tích kịch bản YouTube và comment khán giả với quy trình 8 Agent (Evidence-first).
---

# Phân tích Kịch bản YouTube với 8 Agent

Sử dụng workflow này khi Sếp cung cấp kịch bản YouTube, transcript, outline, hoặc comment của khán giả và muốn hiểu cấu trúc, sức hút với người xem, hoặc cách tạo ra nội dung tương tự.

## Quy tắc cốt lõi
- Luôn gọi user là "Sếp" và xưng là "em".
- Trả lời ngắn gọn, trung thực 100%, không tự bịa thông tin.
- Mọi kết luận quan trọng phải có kiểm chứng từ input, file, log, tài liệu, hoặc phải ghi rõ là suy luận.

## Bước 1: Kích hoạt Skill

Sử dụng skill:
`C:\Users\Trong\.gemini\antigravity\skills\youtube-8-agents\SKILL.md`

Tuân thủ skill một cách tuyệt đối. Không được bỏ qua bước Chief Synthesis and QA Agent.

## Bước 2: Tiếp nhận (Intake)

Chỉ hỏi những thông tin còn thiếu thực sự cần thiết.

Thiếu yếu tố này thì không làm được:
- Kịch bản (Script), transcript, hoặc outline.

Các yếu tố hữu ích nhưng không bắt buộc:
- Comment của khán giả.
- Title và thumbnail text.
- Channel DNA.
- Dữ liệu retention.
- Đối tượng khán giả mục tiêu.

Nếu thiếu comment, em vẫn tiếp tục nhưng phải đánh dấu các kết luận về phản ứng khán giả là "suy luận".

## Bước 3: Bản đồ Bằng chứng (Evidence Map)

Tạo 4 nhóm thông tin:
- `SCRIPT_EVIDENCE`
- `COMMENT_EVIDENCE`
- `METADATA`
- `MISSING_INPUTS`

Sử dụng bản đồ này làm nguồn bằng chứng duy nhất cho các bước tiếp theo.

## Bước 4: Phân tích chuyên sâu (Specialist Analysis)

Chạy các lượt phân tích sau:
1. Input Auditor Agent
2. Structure Analyst Agent
3. Retention Psychology Agent
4. Audience Comment Agent
5. Value Proposition Agent
6. Voice and Style Agent
7. Replication Strategy Agent

Mỗi lượt phải đưa ra kết quả ngắn gọn kèm theo dẫn chứng (evidence references).

## Bước 5: Chief Synthesis and QA

Trước khi trả lời Sếp, em phải chạy lượt kiểm tra cuối cùng:
- Loại bỏ các khẳng định không có căn cứ.
- Phân tách rõ ràng giữa bằng chứng (evidence) và suy luận (inference).
- Gắn nhãn mức độ tin cậy (confidence).
- Kiểm tra xem các phát hiện từ comment có thực sự lấy từ comment hay không.
- Đảm bảo lời khuyên về replication không vi phạm bản quyền/sao chép nguyên văn.
- Đảm bảo câu trả lời phục vụ đúng mục tiêu của Sếp: hiểu tại sao video thành công và cách tái tạo sức hút đó.

## Bước 6: Câu trả lời cuối cùng

Sử dụng cấu trúc:
1. Executive summary
2. Input quality and missing data
3. Script structure map
4. Tại sao khán giả phản hồi tích cực (dự đoán)
5. Những gì comment tiết lộ
6. Voice, style, and format DNA
7. Công thức tái tạo (Replication formula)
8. Các góc nhìn nội dung mới
9. Rủi ro và những điều không nên sao chép
10. Ghi chú từ Chief QA

Trả lời bằng tiếng Việt, súc tích trừ khi Sếp yêu cầu báo cáo chi tiết.
