#!/usr/bin/env python3
"""Print how many of the three goal clauses pass on trunk. Stdlib only."""
from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8") if Path("index.html").is_file() else ""
caddy = (
    Path("deploy/drop.caddy").read_text(encoding="utf-8")
    if Path("deploy/drop.caddy").is_file()
    else ""
)

n = 0
# approved earlier design: English-default grid, not the vinyl/serif overshoot
if 'lang="en"' in html and "vinyl" not in html.lower() and "Instrument Serif" not in html:
    n += 1
# English/Persian language button
if 'id="lang-btn"' in html and "فارسی" in html and html.count("data-i18n") >= 20:
    n += 1
# drop reachable at /drop — the Caddy fragment that puts the portal under that path
if "handle_path /drop/*" in caddy and "farzad-drop:8080" in caddy:
    n += 1

print(n)
