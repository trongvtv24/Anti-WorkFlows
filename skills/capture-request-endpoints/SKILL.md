---
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

## Workflow

### Step 1 – Check Prerequisites

Before running the script, verify:
1. Chrome/Chromium is open and running with `--remote-debugging-port` flag.
   To check: run `Get-WmiObject Win32_Process -Filter "name='chrome.exe'" | Select-Object CommandLine`
   and confirm `--remote-debugging-port=9222` (or another port) is present.
2. You are in a directory with the `ws` npm package available
   (`node_modules/ws` exists).

### Step 2 – Launch Capture

```bash
node scripts\capture.js --duration <seconds>
```

The script will:
1. Scan for an open CDP port (9222–9230).
2. Fetch all targets (`/json` endpoint).
3. Attach a WebSocket to each target and enable `Network` domain.
4. Begin capturing. New targets (tabs opened mid-session) are detected every 3s.
5. For each completed request, fetch the response body via `Network.getResponseBody`.
6. Write each entry to the output JSON file immediately.
7. Auto-stop after `--duration` seconds and print a summary.

### Step 3 – Review Output

Open the JSON file on the Desktop. Use the summary printed to stdout to
identify top domains and endpoints.

## Rate Limiting

This skill communicates **only with localhost** (CDP on 127.0.0.1). No external
rate limits apply. The script naturally throttles itself to the browser's own
request rate.

## Common Mistakes

1. **`ws` module not found** – Run `npm install ws` in your working directory
   first, or `cd` into `invisible-capturer` which already has it installed.

2. **No CDP port open** – Chrome must have been launched with
   `--remote-debugging-port=9222`. In a normal Chrome session (opened by
   double-clicking), this flag is absent. Use the Antigravity Browser or launch
   Chrome manually:
   ```
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
   ```

3. **Response body is `null` for some requests** – This is normal for:
   - Cached resources (body not available via CDP)
   - Preflight OPTIONS requests
   - Requests completed before the script attached
   Use `--no-body` if body fetching causes performance issues on heavy pages.
