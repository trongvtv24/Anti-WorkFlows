#!/usr/bin/env node
/**
 * capture.js – Chrome DevTools Protocol network request capturer
 *
 * Usage:
 *   node capture.js --duration <seconds> [--port <number>] [--output <path>] [--no-body]
 *
 * Captures ALL network requests from every tab, iframe, worker, and service
 * worker of a running Chrome/Chromium browser and writes full request+response
 * data to a JSON file.
 */

'use strict';

const http    = require('http');
const fs      = require('fs');
const path    = require('path');
const os      = require('os');
const { parseArgs } = require('util');

// ─── Argument Parsing ────────────────────────────────────────────────────────
let parsedArgs;
try {
  parsedArgs = parseArgs({
    options: {
      duration: { type: 'string' },
      port:     { type: 'string', default: '9222' },
      output:   { type: 'string', default: '' },
      'no-body': { type: 'boolean', default: false },
      help:     { type: 'boolean', default: false },
    },
    strict: true,
  });
} catch (e) {
  console.error('Error:', e.message);
  printHelp();
  process.exit(1);
}

const args = parsedArgs.values;

if (args.help) { printHelp(); process.exit(0); }

const durationSec = parseInt(args.duration, 10);
if (!args.duration || isNaN(durationSec) || durationSec <= 0) {
  console.error('Error: --duration <seconds> is required and must be a positive integer.');
  printHelp();
  process.exit(1);
}

const startPort  = parseInt(args.port, 10);
const fetchBody  = !args['no-body'];
const outputPath = args.output || defaultOutputPath();

function printHelp() {
  console.log(`
Usage: node capture.js --duration <seconds> [options]

Options:
  --duration <seconds>   (REQUIRED) Capture duration in seconds
  --port <number>        CDP debug port to try first (default: 9222)
                         Auto-scans 9222-9230 if specified port is closed
  --output <path>        Output JSON file (default: Desktop/capture-<ts>.json)
  --no-body              Skip fetching response bodies (faster, smaller output)
  --help                 Show this help

Examples:
  node capture.js --duration 300
  node capture.js --duration 60 --port 9223 --output C:\\Users\\me\\Desktop\\out.json
`);
}

function defaultOutputPath() {
  const desktop = path.join(os.homedir(), 'Desktop');
  const ts = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  return path.join(desktop, `capture-${ts}.json`);
}

// ─── State ───────────────────────────────────────────────────────────────────
const captured        = [];       // Final entries written to file
const pendingRequests = {};       // requestId → partial entry (awaiting response)
const attachedWsUrls  = new Set();
let   activeWss       = [];
let   cdpPort         = null;
let   reqCount        = 0;

// ─── Helpers ─────────────────────────────────────────────────────────────────
function httpGet(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`JSON parse error from ${url}: ${e.message}`)); }
      });
    });
    req.on('error', reject);
    req.setTimeout(3000, () => { req.destroy(); reject(new Error(`Timeout: ${url}`)); });
  });
}

function writeOutput() {
  try {
    fs.writeFileSync(outputPath, JSON.stringify(captured, null, 2), 'utf8');
  } catch (e) {
    // Fallback to cwd if Desktop not writable
    const fallback = path.join(process.cwd(), path.basename(outputPath));
    fs.writeFileSync(fallback, JSON.stringify(captured, null, 2), 'utf8');
    console.warn(`⚠️  Could not write to Desktop. Saved to: ${fallback}`);
  }
}

// ─── Port Auto-Scanner ───────────────────────────────────────────────────────
async function findCdpPort(startPort) {
  const portsToTry = [];
  // Put the user-specified port first, then scan 9222-9230
  portsToTry.push(startPort);
  for (let p = 9222; p <= 9230; p++) {
    if (p !== startPort) portsToTry.push(p);
  }

  for (const port of portsToTry) {
    try {
      await httpGet(`http://localhost:${port}/json/version`);
      return port;
    } catch (_) {
      // try next
    }
  }
  return null;
}

// ─── CDP WebSocket Attachment ─────────────────────────────────────────────────
function attachToTarget(target) {
  return new Promise((resolve) => {
    if (!target.webSocketDebuggerUrl) return resolve();
    if (attachedWsUrls.has(target.webSocketDebuggerUrl)) return resolve();
    attachedWsUrls.add(target.webSocketDebuggerUrl);

    let WS;
    const wsCandidates = [
      // 1. Script's own directory (skill ships with node_modules)
      path.join(__dirname, '..', 'node_modules', 'ws'),
      // 2. invisible-capturer project (known location)
      path.join(os.homedir(), '.gemini', 'antigravity-ide', 'scratch', 'invisible-capturer', 'node_modules', 'ws'),
      // 3. Global NODE_PATH / current cwd node_modules
      'ws',
    ];
    for (const candidate of wsCandidates) {
      try { WS = require(candidate); break; } catch (_) {}
    }
    if (!WS) {
      console.error('Error: "ws" npm package not found.');
      console.error('Fix: cd into your project and run: npm install ws');
      console.error('  or: cd C:\\Users\\Trong\\.gemini\\antigravity-ide\\scratch\\invisible-capturer');
      process.exit(1);
    }

    const ws   = new WS(target.webSocketDebuggerUrl);
    let   cmdId = 1;
    const inflight = {}; // id → {resolve}

    activeWss.push(ws);

    function send(method, params = {}) {
      return new Promise((res) => {
        const id = cmdId++;
        inflight[id] = res;
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    ws.on('open', async () => {
      await send('Network.enable', {
        maxResourceBufferSize:  104857600,  // 100 MB
        maxTotalBufferSize:    524288000,   // 500 MB
      });
      resolve();
      console.log(`✅ [${target.type}] ${(target.title || target.url || '').slice(0, 80)}`);
    });

    ws.on('message', async (raw) => {
      let msg;
      try { msg = JSON.parse(raw); } catch (_) { return; }

      // Resolve pending command callbacks
      if (msg.id && inflight[msg.id]) {
        const cb = inflight[msg.id];
        delete inflight[msg.id];
        cb(msg.result || {});
        return;
      }

      if (!msg.method) return;

      // ── Request sent ──────────────────────────────────────────────────────
      if (msg.method === 'Network.requestWillBeSent') {
        const { requestId, request, timestamp, type, documentURL } = msg.params;
        pendingRequests[requestId] = {
          time:        new Date().toISOString(),
          requestId,
          type:        type || 'Unknown',
          method:      request.method,
          url:         request.url,
          headers:     request.headers,
          postData:    request.postData || null,
          documentURL: documentURL || null,
          targetTitle: target.title || target.url || null,
          targetType:  target.type  || null,
          _reqTs:      timestamp,
        };
      }

      // ── Response received ─────────────────────────────────────────────────
      if (msg.method === 'Network.responseReceived') {
        const { requestId, response, timestamp } = msg.params;
        const entry = pendingRequests[requestId];
        if (!entry) return;

        entry.responseStatus     = response.status;
        entry.responseMimeType   = response.mimeType;
        entry.responseHeaders    = response.headers;
        entry.durationMs         = entry._reqTs
          ? Math.round((timestamp - entry._reqTs) * 1000)
          : null;
        delete entry._reqTs;

        // Fetch response body asynchronously
        if (fetchBody) {
          try {
            const result = await send('Network.getResponseBody', { requestId });
            entry.responseBody         = result.body         || null;
            entry.responseBodyEncoding = result.base64Encoded ? 'base64' : 'utf8';
          } catch (_) {
            entry.responseBody = null;
          }
        } else {
          entry.responseBody = null;
        }

        delete pendingRequests[requestId];
        captured.push(entry);
        reqCount++;
        writeOutput();

        const short = entry.url.length > 80 ? entry.url.slice(0, 77) + '...' : entry.url;
        process.stdout.write(`\r[+${reqCount} req] ${entry.method} ${short}`.padEnd(120));
      }

      // ── Load failed ───────────────────────────────────────────────────────
      if (msg.method === 'Network.loadingFailed') {
        const { requestId, errorText } = msg.params;
        const entry = pendingRequests[requestId];
        if (entry) {
          entry.responseStatus = 0;
          entry.responseError  = errorText;
          delete entry._reqTs;
          delete pendingRequests[requestId];
          captured.push(entry);
          reqCount++;
          writeOutput();
        }
      }
    });

    ws.on('error', () => {}); // Silently ignore (target closed etc.)
    ws.on('close', () => {
      activeWss = activeWss.filter(w => w !== ws);
    });
  });
}

// ─── Target Poller ────────────────────────────────────────────────────────────
async function refreshTargets() {
  try {
    const targets = await httpGet(`http://localhost:${cdpPort}/json`);
    const relevant = targets.filter(t =>
      ['page', 'iframe', 'worker', 'service_worker', 'shared_worker'].includes(t.type)
    );
    for (const t of relevant) {
      await attachToTarget(t);
    }
  } catch (_) {}
}

// ─── Summary ──────────────────────────────────────────────────────────────────
function printSummary() {
  console.log('\n\n══════════════════════════════════════════════');
  console.log(`📊 Capture complete — ${captured.length} requests`);
  console.log(`💾 Output: ${outputPath}`);
  console.log('══════════════════════════════════════════════');

  const domainCount = {};
  const endpointCount = {};
  captured.forEach(r => {
    try {
      const u   = new URL(r.url);
      const dom = u.hostname;
      const ep  = dom + u.pathname;
      domainCount[dom]    = (domainCount[dom]    || 0) + 1;
      endpointCount[ep]   = (endpointCount[ep]   || 0) + 1;
    } catch (_) {}
  });

  console.log('\n🌐 Top Domains:');
  Object.entries(domainCount).sort((a, b) => b[1] - a[1]).slice(0, 10)
    .forEach(([d, n]) => console.log(`  ${String(n).padStart(5)}x  ${d}`));

  console.log('\n🔗 Top Endpoints:');
  Object.entries(endpointCount).sort((a, b) => b[1] - a[1]).slice(0, 20)
    .forEach(([e, n]) => console.log(`  ${String(n).padStart(5)}x  ${e}`));
}

// ─── Main ─────────────────────────────────────────────────────────────────────
async function main() {
  console.log(`\n🔍 Scanning for Chrome CDP port (starting at ${startPort})...`);
  cdpPort = await findCdpPort(startPort);

  if (!cdpPort) {
    console.error(`\n❌ No Chrome debug port found in range 9222-9230.`);
    console.error(`   Make sure Chrome is running with --remote-debugging-port=9222`);
    console.error(`   Or launch it with:`);
    console.error(`   "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222`);
    process.exit(1);
  }

  console.log(`✅ Found Chrome on port ${cdpPort}`);
  console.log(`⏱️  Capturing for ${durationSec} seconds...`);
  console.log(`📄 Output: ${outputPath}\n`);

  // Initial attach
  await refreshTargets();

  // Poll for new targets every 3 seconds
  const pollInterval = setInterval(refreshTargets, 3000);

  // Auto-stop after duration
  const stopTimer = setTimeout(() => {
    clearInterval(pollInterval);
    activeWss.forEach(ws => { try { ws.close(); } catch(_) {} });
    printSummary();
    process.exit(0);
  }, durationSec * 1000);

  // Ctrl+C handler
  process.on('SIGINT', () => {
    clearTimeout(stopTimer);
    clearInterval(pollInterval);
    activeWss.forEach(ws => { try { ws.close(); } catch(_) {} });
    printSummary();
    process.exit(0);
  });
}

main().catch(e => {
  console.error('Fatal error:', e.message);
  process.exit(1);
});
