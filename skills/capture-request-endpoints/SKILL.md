---
type: skill
name: capture-request-endpoints
description: >-
  Captures all network requests from a running Chrome/Chromium browser via
  Chrome DevTools Protocol (CDP). Attaches to all tabs, iframes, workers, and
  service workers. Saves full request+response data (URL, method, headers,
  postData, status, response headers, body, timing) to a JSON file on the
  Desktop. Input: capture duration in seconds. Output: timestamped JSON file
  on the Desktop (configurable). Use when the user wants to monitor, audit, or
  reverse-engineer HTTP requests made by a browser or a Chrome Extension.
---

# capture-request-endpoints

## Overview

Captures **every network request** sent by a running Chrome/Chromium browser
(including requests from Chrome Extensions, Service Workers, iframes, and Web
Workers) using the Chrome DevTools Protocol (CDP) over a WebSocket connection.

Each captured entry contains the **maximum available information**:
- Request: method, URL, headers, postData, documentURL, target info
- Response: status code, MIME type, headers, **full body**, latency in ms
- Metadata: timestamp, requestId, resource type, which tab/worker sent it

Output is a single JSON array written to a file on the Desktop (or a custom
path you specify).

## Dependencies

- **Node.js** (v16+) – must be on PATH.
- **`ws` npm package** – must be installed in the working directory or globally.
  Install with: `npm install ws` inside the project directory, or use the
  existing `invisible-capturer` project which already has it.
- **Chrome/Chromium** must be running with `--remote-debugging-port=<port>`.
  The Antigravity Browser starts Chrome with this flag automatically on port 9222.

> [!IMPORTANT]
> If Chrome is NOT running with a debug port, the script will scan ports
> 9222–9230 automatically. If none are found, it exits with an error.

## Quick Start

```bash
# 1. Navigate to a directory that has the 'ws' npm package installed
cd C:\Users\Trong\.gemini\antigravity-ide\scratch\invisible-capturer

# 2. Run a 5-minute capture (300 seconds), output to Desktop
node scripts\capture.js --duration 300

# 3. Custom port and output path
node scripts\capture.js --duration 60 --port 9222 --output "C:\Users\Trong\Desktop\my-capture.json"
```

## Utility Script

### `scripts/capture.js`

**Subcommand / Usage:**

```
node capture.js [options]

Options:
  --duration <seconds>   (REQUIRED) How long to capture in seconds
  --port <number>        CDP debug port (default: 9222, auto-scans 9222-9230)
  --output <path>        Output JSON file path
                         (default: Desktop\capture-<timestamp>.json)
  --no-body              Skip fetching response bodies (faster, smaller output)
```

**Output JSON structure per entry:**
```json
{
  "time": "2026-05-21T03:54:45.702Z",
  "requestId": "924.3147",
  "type": "Fetch",
  "method": "GET",
  "url": "https://www.facebook.com/api/graphql/",
  "headers": { "...": "..." },
  "postData": null,
  "documentURL": "https://www.facebook.com/",
  "targetTitle": "Facebook",
  "targetType": "page",
  "responseStatus": 200,
  "responseMimeType": "application/json",
  "responseHeaders": { "...": "..." },
  "responseBody": "{\"data\": ...}",
  "durationMs": 142
}
```

## AI Step-by-Step Execution Guide

To execute this skill, the AI must follow this structured, interactive workflow. **Do not execute steps in parallel; always verify the outcome of the current step before proceeding.**

### Giai đoạn 1: Kiểm tra tiền đề (Pre-checks)
1. **Tìm cổng CDP của Chrome**:
   Chạy lệnh sau để kiểm tra xem Chrome có đang chạy với cổng debug hay không và xác định các tiến trình Chrome:
   ```powershell
   Get-Process chrome | Select-Object Id, CommandLine -ErrorAction SilentlyContinue
   ```
   *Nếu không tìm thấy CommandLine hoặc cổng debug, hướng dẫn người dùng chạy Chrome thủ công bằng lệnh:*
   ```powershell
   & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
   ```
2. **Kiểm tra Node.js**:
   Xác minh Node.js đã được cài đặt:
   ```powershell
   node -v
   ```
3. **Kiểm tra thư viện `ws`**:
   Kiểm tra xem thư mục `node_modules\ws` có tồn tại trong thư mục skill hoặc thư mục đích không. Nếu thiếu, tiến hành cài đặt:
   ```powershell
   npm install ws
   ```

### Giai đoạn 2: Khởi chạy Capture
1. **Định hình tham số**:
   Xác định thời gian capture (ví dụ: `--duration 120` cho 2 phút) và đường dẫn lưu file (mặc định sẽ lưu ở Desktop).
2. **Chạy script capture**:
   Chạy lệnh PowerShell (thay thế tham số bằng thông tin thực tế):
   ```powershell
   node skills\capture-request-endpoints\scripts\capture.js --duration 120
   ```
   *Lưu ý: Nếu cần tối ưu hóa hiệu năng, thêm cờ `--no-body`.*

### Giai đoạn 3: Phân tích & Báo cáo kết quả
1. **Đọc tệp kết quả**:
   Sau khi hoàn tất, định dạng và đọc tệp JSON được tạo ở Desktop:
   - Liệt kê tổng số requests đã bắt được.
   - Nhận diện các domain chính (Top Domains) và các API endpoints quan trọng.
2. **Báo cáo lại cho người dùng**:
   Tổng hợp kết quả, cấu trúc JSON và các endpoint bắt được theo cách rõ ràng, dễ hiểu.

---

## Logic & Edge-Case Handling

### 1. Tối ưu hóa MIME-Type để tránh Out of Memory (OOM)
Để tránh hiện tượng treo trình duyệt hoặc tràn bộ nhớ Node.js khi bắt các file binary dung lượng lớn (ảnh, video, audio, fonts), mã nguồn `capture.js` đã được cấu hình bộ lọc MIME-Type.
- **Quy tắc**: Chỉ tải về nội dung phản hồi (`responseBody`) cho các loại MIME-Type thuộc dạng văn bản (textual):
  - `json` (application/json)
  - `xml` (application/xml, text/xml)
  - `html` (text/html)
  - `text` (text/plain, text/csv, v.v.)
  - `javascript` (application/javascript, text/javascript)
  - `css` (text/css)
- **Ảnh hưởng**: Đối với hình ảnh (PNG, JPEG), video (MP4), hay file nhị phân khác, thuộc tính `responseBody` sẽ tự động trả về `null` giúp tiết kiệm RAM cực kỳ hiệu quả mà vẫn giữ đầy đủ thông tin Header.

### 2. Xử lý lỗi không tìm thấy cổng CDP
- Nếu script báo lỗi: `No Chrome debug port found in range 9222-9230.`
- **Xử lý**: 
  1. Yêu cầu người dùng tắt hoàn toàn Chrome (kể cả chạy ngầm).
  2. Khởi chạy lại Chrome bằng lệnh bật cổng remote-debugging ở cổng `9222`.
  3. Kiểm tra lại bằng cách truy cập `http://localhost:9222/json/version` trong trình duyệt hoặc qua `curl`.

---

## Rate Limiting

Kỹ năng này hoạt động **hoàn toàn trên máy cục bộ (localhost)** để giao tiếp với Chrome qua cổng CDP. Không có giới hạn tần suất (Rate limits) nào từ bên ngoài được áp dụng. Script sẽ tự động điều tiết theo tần suất gửi request thực tế của trình duyệt Chrome.

## Common Mistakes

1. **`ws` module not found** – Di chuyển vào thư mục dự án và chạy `npm install ws` hoặc sử dụng thư mục chứa sẵn dependencies.
2. **Không bật Remote Debugging trên Chrome** – Phải đảm bảo Chrome được bật bằng cờ `--remote-debugging-port=9222`.
3. **Response body nhận giá trị `null`** – Điều này bình thường đối với các tài nguyên được tải từ cache (không truyền qua mạng) hoặc các request OPTIONS (preflight). Đối với các định dạng phi văn bản (như hình ảnh/phương tiện truyền thông), body cũng được bỏ qua một cách an toàn để tránh tràn bộ nhớ.
