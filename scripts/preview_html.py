#!/usr/bin/env python3
"""Generate a local HTML preview of train.jsonl with KaTeX-rendered LaTeX."""

from __future__ import annotations

import argparse
import json
import re
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JSONL = ROOT / "data" / "train.jsonl"
DEFAULT_OUTPUT = ROOT / "drafts" / "preview.html"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ramanujan Dataset Preview</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <style>
    :root { color-scheme: light dark; }
    body {
      font-family: system-ui, -apple-system, sans-serif;
      line-height: 1.5;
      max-width: 920px;
      margin: 0 auto;
      padding: 1rem 1.25rem 3rem;
    }
    h1 { font-size: 1.35rem; margin-bottom: 0.25rem; }
    .meta { color: #666; font-size: 0.9rem; margin-bottom: 1rem; }
    .toolbar {
      display: flex; flex-wrap: wrap; gap: 0.5rem 1rem;
      align-items: end; margin-bottom: 1.25rem;
      padding: 0.75rem 1rem; border-radius: 8px;
      background: rgba(127,127,127,0.08);
    }
    label { display: flex; flex-direction: column; font-size: 0.8rem; gap: 0.2rem; }
    input, select, button {
      font: inherit; padding: 0.35rem 0.5rem; border-radius: 4px;
      border: 1px solid rgba(127,127,127,0.35);
    }
    button { cursor: pointer; background: rgba(127,127,127,0.12); }
    button:hover { background: rgba(127,127,127,0.2); }
    .entry {
      border: 1px solid rgba(127,127,127,0.25);
      border-radius: 8px; padding: 0.85rem 1rem; margin-bottom: 0.75rem;
    }
    .entry-id {
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 0.85rem; font-weight: 600; margin-bottom: 0.35rem;
    }
    .topic { font-size: 0.78rem; color: #666; margin-bottom: 0.5rem; }
    .content { font-size: 1.05rem; }
    .raw {
      display: none; margin-top: 0.6rem; padding: 0.6rem;
      font-family: ui-monospace, monospace; font-size: 0.78rem;
      white-space: pre-wrap; word-break: break-word;
      background: rgba(127,127,127,0.08); border-radius: 4px;
    }
    .entry.show-raw .raw { display: block; }
    .katex-display { margin: 0.5rem 0; overflow-x: auto; }
    .empty { color: #666; font-style: italic; padding: 2rem 0; text-align: center; }
    .pager { display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }
    .pager span { font-size: 0.85rem; color: #666; }
  </style>
</head>
<body>
  <h1>Ramanujan Dataset — LaTeX Preview</h1>
  <p class="meta">Rendered with KaTeX. Toggle “Show source” on any entry to compare raw LaTeX.</p>
  <div class="toolbar">
    <label>Part
      <select id="part"><option value="">All</option></select>
    </label>
    <label>Chapter
      <select id="chapter"><option value="">All</option></select>
    </label>
    <label>Search id
      <input id="search" type="search" placeholder="RN-P1-C02-Entry03" size="28">
    </label>
    <label>Per page
      <select id="pageSize">
        <option value="25">25</option>
        <option value="50" selected>50</option>
        <option value="100">100</option>
        <option value="500">500</option>
      </select>
    </label>
    <div class="pager">
      <button id="prev" type="button">Prev</button>
      <span id="pageInfo"></span>
      <button id="next" type="button">Next</button>
    </div>
    <button id="toggleAllRaw" type="button">Show all source</button>
  </div>
  <div id="list"></div>
  <script id="data" type="application/json">__ENTRIES__</script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <script>
    const entries = JSON.parse(document.getElementById("data").textContent);
    const partSel = document.getElementById("part");
    const chapterSel = document.getElementById("chapter");
    const searchEl = document.getElementById("search");
    const pageSizeEl = document.getElementById("pageSize");
    const listEl = document.getElementById("list");
    const pageInfo = document.getElementById("pageInfo");
    let page = 0;
    let showAllRaw = false;

    function parseId(id) {
      const m = id.match(/^RN-P(\\d+)-C(\\d+)-/);
      return m ? { part: m[1], chapter: m[2] } : { part: "", chapter: "" };
    }

    const parts = [...new Set(entries.map(e => parseId(e.id).part).filter(Boolean))].sort((a,b)=>a-b);
    for (const p of parts) {
      const opt = document.createElement("option");
      opt.value = p; opt.textContent = "P" + p;
      partSel.appendChild(opt);
    }

    function chaptersForPart(p) {
      const set = new Set();
      for (const e of entries) {
        const info = parseId(e.id);
        if (!p || info.part === p) set.add(info.chapter);
      }
      return [...set].sort((a,b)=>a-b);
    }

    function refreshChapterOptions() {
      const p = partSel.value;
      chapterSel.innerHTML = '<option value="">All</option>';
      for (const c of chaptersForPart(p)) {
        const opt = document.createElement("option");
        opt.value = c; opt.textContent = "Ch." + (+c);
        chapterSel.appendChild(opt);
      }
    }

    function filtered() {
      const p = partSel.value;
      const c = chapterSel.value;
      const q = searchEl.value.trim().toLowerCase();
      return entries.filter(e => {
        const info = parseId(e.id);
        if (p && info.part !== p) return false;
        if (c && info.chapter !== c) return false;
        if (q && !e.id.toLowerCase().includes(q)) return false;
        return true;
      });
    }

    function renderMath(el) {
      if (typeof renderMathInElement === "function") {
        renderMathInElement(el, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
          ],
          throwOnError: false,
        });
      }
    }

    function render() {
      const rows = filtered();
      const size = +pageSizeEl.value;
      const pages = Math.max(1, Math.ceil(rows.length / size));
      if (page >= pages) page = pages - 1;
      const slice = rows.slice(page * size, (page + 1) * size);
      pageInfo.textContent = rows.length
        ? `Page ${page + 1} / ${pages} (${rows.length} entries)`
        : "0 entries";
      listEl.innerHTML = "";
      if (!slice.length) {
        listEl.innerHTML = '<p class="empty">No entries match the current filters.</p>';
        return;
      }
      for (const e of slice) {
        const div = document.createElement("article");
        div.className = "entry" + (showAllRaw ? " show-raw" : "");
        div.innerHTML =
          `<div class="entry-id">${e.id}</div>` +
          `<div class="topic">${(e.topics || []).join(", ")}</div>` +
          `<div class="content">${e.content.replace(/&/g,"&amp;").replace(/</g,"&lt;")}</div>` +
          `<pre class="raw">${e.content.replace(/&/g,"&amp;").replace(/</g,"&lt;")}</pre>` +
          `<button type="button" class="rawBtn">Show source</button>`;
        div.querySelector(".rawBtn").addEventListener("click", () => div.classList.toggle("show-raw"));
        listEl.appendChild(div);
      }
      renderMath(listEl);
    }

    partSel.addEventListener("change", () => { refreshChapterOptions(); page = 0; render(); });
    chapterSel.addEventListener("change", () => { page = 0; render(); });
    searchEl.addEventListener("input", () => { page = 0; render(); });
    pageSizeEl.addEventListener("change", () => { page = 0; render(); });
    document.getElementById("prev").addEventListener("click", () => { if (page > 0) { page--; render(); } });
    document.getElementById("next").addEventListener("click", () => {
      const pages = Math.ceil(filtered().length / +pageSizeEl.value);
      if (page + 1 < pages) { page++; render(); }
    });
    document.getElementById("toggleAllRaw").addEventListener("click", (ev) => {
      showAllRaw = !showAllRaw;
      ev.target.textContent = showAllRaw ? "Hide all source" : "Show all source";
      document.querySelectorAll(".entry").forEach(el => el.classList.toggle("show-raw", showAllRaw));
    });

    refreshChapterOptions();
    render();
  </script>
</body>
</html>
"""


def load_entries(path: Path, part: int | None, chapter: int | None) -> list[dict]:
    entries: list[dict] = []
    part_re = re.compile(rf"^RN-P{part}-") if part else None
    chapter_re = re.compile(rf"^RN-P\d+-C{chapter:02d}-") if chapter else None
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            entry_id = record["id"]
            if part_re and not part_re.match(entry_id):
                continue
            if chapter_re and not chapter_re.match(entry_id):
                continue
            entries.append(record)
    return entries


def write_preview(entries: list[dict], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(entries, ensure_ascii=False)
    output.write_text(HTML.replace("__ENTRIES__", payload), encoding="utf-8")


def serve_file(path: Path, port: int) -> None:
    directory = path.parent

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

    url = f"http://127.0.0.1:{port}/{path.name}"
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Serving {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview train.jsonl with rendered LaTeX")
    parser.add_argument("--input", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--part", type=int, help="Only include one part (1–5)")
    parser.add_argument("--chapter", type=int, help="Only include one chapter number")
    parser.add_argument("--open", action="store_true", help="Open preview in the browser")
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Serve preview over HTTP (keeps KaTeX CDN working reliably)",
    )
    parser.add_argument("--port", type=int, default=8000, help="Port for --serve (default: 8000)")
    args = parser.parse_args()

    entries = load_entries(args.input, args.part, args.chapter)
    if not entries:
        raise SystemExit("No entries matched the filters.")

    write_preview(entries, args.output)
    print(f"Wrote {len(entries)} entries to {args.output}")

    if args.serve:
        serve_file(args.output, args.port)
    elif args.open:
        webbrowser.open(args.output.as_uri())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
