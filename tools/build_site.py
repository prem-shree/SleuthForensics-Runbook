#!/usr/bin/env python3
"""Build the static documentation site from docs/*.md into the repository root.

No third-party dependencies. Renders the markdown subset used in this repository:
headings, paragraphs, fenced code, blockquotes, GFM tables, lists, rules and inline
formatting. Output is plain HTML that works without JavaScript.

Usage:  python3 tools/build_site.py
"""
import html
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT_PAGES = os.path.join(ROOT, "p")

GROUPS = [
    ("Start here", ["30", "31", "38"]),
    ("Research & catalogue", ["00", "01", "21"]),
    ("Operating model", ["02", "03", "28", "35", "32"]),
    ("Runbook architecture", ["04", "19", "20", "22", "23"]),
    ("Engagement types", ["24", "25", "26", "27"]),
    ("Client information & output", ["05", "33", "08", "34", "14"]),
    ("Evidence & tools", ["06", "07", "36"]),
    ("Product & architecture", ["09", "11", "12", "10", "37", "39", "40", "13"]),
    ("Programme", ["15", "16", "17", "18", "29"]),
]

SHORT = {
    "00": "Research findings", "01": "Service catalogue v1", "02": "Users & roles",
    "03": "Engagement lifecycle", "04": "Runbook architecture", "05": "Questionnaire architecture",
    "06": "Evidence model", "07": "Tools & templates", "08": "Findings & reporting",
    "09": "Information architecture", "10": "Data model", "11": "UX structure",
    "12": "Visual design direction", "13": "Security architecture", "14": "Excel exports",
    "15": "Assumptions & questions", "16": "Implementation plan", "17": "Governing constraints",
    "18": "Provenance & validation", "19": "Engagement type spec", "20": "Shared modules",
    "21": "Engagement catalogue v2", "22": "Core spine", "23": "Archetype modules",
    "24": "ETS — Assessment", "25": "ETS — Testing", "26": "ETS — Investigation",
    "27": "ETS — Continuous", "28": "Checklists & gates", "29": "Architecture amendments",
    "30": "Decisions needed", "31": "Confirmed decisions", "32": "Operating policies",
    "33": "Questionnaire instruments", "34": "Report templates", "35": "Decision trees",
    "36": "Tool capabilities", "37": "Data schema", "38": "Placeholder register",
    "39": "API & permissions", "40": "Build & operations",
}


DESC = {
    "00": "Everything the website actually says, and the design consequences drawn from it.",
    "01": "The first pass: 41 engagement types derived from site copy. Superseded by 21.",
    "02": "Five roles, the capability matrix, and the rules no role can be granted past.",
    "03": "Eleven phases built on Sleuth's own published six-step method, and the emergency path.",
    "04": "Why a runbook is a composition of versioned modules, not a document.",
    "05": "How client questionnaires are composed, and why answers carry source and confidence.",
    "06": "The L0-L5 provenance ladder, chain of custody, integrity failure and disposition.",
    "07": "Why procedures reference capability rather than product, and the template library.",
    "08": "The finding model, report composition and the QA review workflow.",
    "09": "Seven top-level items, not seventeen - and what deliberately isn't navigation.",
    "10": "Two planes: versioned content, and execution that pins a version forever.",
    "11": "Screen by screen, each worked through message, user, context, priority, risk, UI.",
    "12": "Design language extended from Sleuth's live brand. Flat, bordered, undecorated.",
    "13": "Threat model, access control, evidence protection, audit and the secrets position.",
    "14": "Excel as a projection of the registers, never a source.",
    "15": "The original open questions and the decision register.",
    "16": "Phased delivery, and why runbook authoring is the critical path rather than code.",
    "17": "Sleuth's seven binding rules, and how each is enforced rather than merely stated.",
    "18": "Provenance and validation as data fields, so 'needs confirmation' is queryable.",
    "19": "The schema for the sixteen facts each engagement type must supply.",
    "20": "The change-once guarantee: reference not copy, extension points, impact analysis.",
    "21": "The recommended 20 engagement types, consolidated against four tests.",
    "22": "59 procedures across 10 shared modules, inherited by every engagement type.",
    "23": "A1-A4 execution modules, 50 procedures, drafted against public standards.",
    "24": "Six assessment and advisory engagement types, populated.",
    "25": "Seven authorised technical testing engagement types, populated.",
    "26": "Five investigation and response engagement types, populated.",
    "27": "Two continuous engagement types, populated.",
    "28": "Seven gates, 63 conditions, and why facts beat ticks.",
    "29": "Deltas to findings, reporting, roles, data model, navigation, UX and exports.",
    "30": "Plain English, with a recommendation for each decision.",
    "31": "What Sleuth confirmed, what it closed, and what a blanket yes did not resolve.",
    "32": "Intrusiveness ceiling, severity, safeguarding, red team, standards and thresholds.",
    "33": "368 questions across all 20 engagement types, roughly 60 per cent inherited.",
    "34": "Twenty report templates, around 65 per cent generated from records.",
    "35": "Sixteen decision trees with recorded traversal.",
    "36": "97 vendor-neutral tool capabilities. The catalogue ships empty by design.",
    "37": "61 tables, 15 enforced invariants, row-level security at the database.",
    "38": "17 defaults applied, 5 shapes specified, 7 blocking, 5 facts outstanding.",
    "39": "58 routes and four independently sufficient layers of permission enforcement.",
    "40": "Environments, two kinds of migration, backup, observability and incident continuity.",
}

STATS = [
    ("20", "engagement types"),
    ("4", "execution archetypes"),
    ("109", "shared procedures"),
    ("7", "gates &middot; 63 conditions"),
    ("368", "client questions"),
    ("61", "database tables"),
    ("0%", "SME-validated"),
    ("7", "blocking placeholders"),
]

# ---------------------------------------------------------------- inline

CODE_TOKEN = "\x00CODE%d\x00"


def inline(text):
    """Render inline markdown. Code spans are extracted first so their contents
    are escaped but never re-processed."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1), quote=False))
        return CODE_TOKEN % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)

    # links: [label](target) — rewrite sibling .md targets to .html
    def link(m):
        label, target = m.group(1), m.group(2)
        if target.endswith(".md"):
            target = target[:-3] + ".html"
        rel = 'rel="noopener" target="_blank"' if target.startswith("http") else ""
        return f'<a href="{html.escape(target, quote=True)}" {rel}>{label}</a>'

    text = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", text)

    for i, span in enumerate(spans):
        text = text.replace(CODE_TOKEN % i, f"<code>{span}</code>")
    return text


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "section"


# ---------------------------------------------------------------- blocks


def is_table_sep(line):
    return bool(re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", line)) and "-" in line


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render(md):
    """Markdown -> (html, toc entries)."""
    lines = md.split("\n")
    out, toc = [], []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]

        # fenced code
        if line.lstrip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            body = html.escape("\n".join(buf), quote=False)
            out.append(f'<div class="codewrap"><pre><code>{body}</code></pre></div>')
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level, raw = len(m.group(1)), m.group(2).strip()
            rendered = inline(raw)
            anchor = slugify(raw)
            if level in (2, 3):
                toc.append({"level": level, "text": re.sub(r"<[^>]+>", "", rendered), "id": anchor})
            out.append(f'<h{level} id="{anchor}">{rendered}'
                       f'<a class="anchor" href="#{anchor}" aria-label="Link to this section">#</a>'
                       f'</h{level}>')
            i += 1
            continue

        # horizontal rule
        if re.match(r"^\s*(---|\*\*\*|___)\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # table
        if "|" in line and i + 1 < n and is_table_sep(lines[i + 1]):
            head = split_row(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            body = ""
            for r in rows:
                r = (r + [""] * len(head))[:len(head)]
                body += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead>'
                       f"<tbody>{body}</tbody></table></div>")
            continue

        # blockquote
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and (lines[i].lstrip().startswith(">") or
                             (buf and lines[i].strip() and not lines[i].lstrip().startswith("#"))):
                if not lines[i].lstrip().startswith(">"):
                    break
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner, _ = render("\n".join(buf))
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        # lists
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            ordered = bool(re.match(r"\d+\.", m.group(2)))
            items, base = [], len(m.group(1))
            while i < n:
                mm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", lines[i])
                if not mm or len(mm.group(1)) < base:
                    break
                if len(mm.group(1)) > base:            # nested: fold into parent
                    items[-1] += "\n" + lines[i]
                    i += 1
                    continue
                items.append(mm.group(3))
                i += 1
                # continuation lines
                while i < n and lines[i].strip() and not re.match(
                        r"^(\s*)([-*+]|\d+\.)\s+", lines[i]) and lines[i].startswith(" " * (base + 2)):
                    items[-1] += " " + lines[i].strip()
                    i += 1
            li = ""
            for it in items:
                if "\n" in it:
                    first, rest = it.split("\n", 1)
                    nested = "\n".join(l[base + 2:] if len(l) > base + 2 else l
                                       for l in rest.split("\n"))
                    sub, _ = render(nested)
                    li += f"<li>{inline(first)}{sub}</li>"
                else:
                    li += f"<li>{inline(it)}</li>"
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>{li}</{tag}>")
            continue

        # blank
        if not line.strip():
            i += 1
            continue

        # paragraph
        buf = []
        while i < n and lines[i].strip() and not re.match(
                r"^(#{1,6}\s|\s*(---|\*\*\*|___)\s*$|\s*>|\s*([-*+]|\d+\.)\s)", lines[i]) \
                and not lines[i].lstrip().startswith("```") \
                and not ("|" in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
            buf.append(lines[i])
            i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(b.strip() for b in buf))}</p>")

    return "\n".join(out), toc


# ---------------------------------------------------------------- shell

def shell(title, subtitle, nav, content, toc, depth, extra_class=""):
    up = "../" if depth else ""
    toc_html = ""
    if toc:
        items = "".join(
            f'<a class="l{t["level"]}" href="#{t["id"]}">{html.escape(t["text"], quote=False)}</a>'
            for t in toc)
        toc_html = f'<aside class="toc"><div class="toc-h">On this page</div>{items}</aside>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} — Sleuth Runbook Platform</title>
<meta name="description" content="{html.escape(subtitle)}">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body class="{extra_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="{up}index.html">Sleuth&nbsp;&middot;&nbsp;Runbook Platform</a>
    <span class="badge">Design proposal &middot; not built</span>
    <button class="navtoggle" id="navtoggle" aria-label="Toggle navigation" aria-expanded="false">Menu</button>
  </div>
</header>
<div class="layout">
  <nav class="sidebar" id="sidebar" aria-label="Documents">
    <div class="search-wrap">
      <input type="search" id="q" placeholder="Search…" aria-label="Search documents" autocomplete="off">
      <div id="results" class="results" hidden></div>
    </div>
    {nav}
  </nav>
  <main id="main" class="content">
    {content}
    <footer class="pagefoot">
      <p>Sleuth Forensics — internal runbook &amp; engagement platform. Design documentation.
      Nothing here is SME-validated; see <a href="{up}p/17-governing-constraints.html">governing constraints</a>.</p>
    </footer>
  </main>
  {toc_html}
</div>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def build_nav(current, depth):
    up = "../" if depth else ""
    parts = []
    for group, nums in GROUPS:
        parts.append(f'<div class="navgroup"><div class="navgroup-h">{html.escape(group)}</div>')
        for num in nums:
            slug = SLUGS.get(num)
            if not slug:
                continue
            cls = "on" if slug == current else ""
            parts.append(f'<a class="{cls}" href="{up}p/{slug}.html">'
                         f'<span class="num">{num}</span>{html.escape(SHORT[num])}</a>')
        parts.append("</div>")
    return "".join(parts)


# ---------------------------------------------------------------- main

files = sorted(f for f in os.listdir(DOCS) if f.endswith(".md"))
SLUGS = {f[:2]: f[:-3] for f in files}

os.makedirs(OUT_PAGES, exist_ok=True)
for old in os.listdir(OUT_PAGES):
    os.remove(os.path.join(OUT_PAGES, old))

index_entries = []
search_index = []

for f in files:
    num = f[:2]
    slug = f[:-3]
    md = open(os.path.join(DOCS, f), encoding="utf-8").read()
    m = re.search(r"^#\s+(.*)$", md, re.M)
    title = m.group(1).strip() if m else slug
    body, toc = render(md)
    nav = build_nav(slug, depth=1)
    subtitle = SHORT.get(num, title)
    page = shell(title, subtitle, nav, body, toc, depth=1)
    open(os.path.join(OUT_PAGES, slug + ".html"), "w", encoding="utf-8").write(page)

    index_entries.append((num, slug, title))
    search_index.append({
        "n": num, "s": slug, "t": title, "d": SHORT.get(num, ""),
        "h": [t["text"] for t in toc][:40],
    })

# ---- home page
stat_html = "".join(
    f'<div class="stat"><span class="v">{v}</span><span class="k">{k}</span></div>'
    for v, k in STATS)

index_html = ""
for group, nums in GROUPS:
    rows = ""
    for num in nums:
        slug = SLUGS.get(num)
        if not slug:
            continue
        rows += (f'<a class="ix" href="p/{slug}.html">'
                 f'<span class="ix-n">{num}</span>'
                 f'<span class="ix-b"><span class="ix-t">{html.escape(SHORT[num])}</span>'
                 f'<span class="ix-d">{html.escape(DESC.get(num, ""))}</span></span></a>')
    index_html += (f'<section class="ixgroup"><h2>{html.escape(group)}</h2>'
                   f'<div class="ixlist">{rows}</div></section>')

home_body = f"""
<div class="hero">
  <p class="kicker">Architecture &amp; UX proposal &mdash; for review before implementation</p>
  <h1>Sleuth Forensics<br>Internal Runbook &amp; Engagement Platform</h1>
  <p class="lede">An internal platform that answers one question for a consultant at any point in any
  engagement: <strong>what exactly do I need to do next to execute this correctly?</strong></p>
  <p class="note">No application code has been written. Everything here is a specification, and
  nothing in it is SME-validated. Seven governing constraints issued by Sleuth are binding on all of
  it &mdash; see <a href="p/17-governing-constraints.html">17 &middot; Governing constraints</a>.</p>
  <div class="stats">{stat_html}</div>
</div>

<div class="startrow">
  <a class="start" href="p/21-engagement-catalogue-v2.html">
    <span class="s-n">Start with the catalogue</span>
    <span class="s-d">21 public services resolved to 20 engagement types across four archetypes.</span></a>
  <a class="start" href="p/30-decisions-needed.html">
    <span class="s-n">Then the decisions</span>
    <span class="s-d">Plain English, with a recommendation for each. All 17 confirmed on 21 Sep.</span></a>
  <a class="start" href="p/38-placeholder-register.html">
    <span class="s-n">Then what is still open</span>
    <span class="s-d">Seven blocking placeholders, five facts only Sleuth can supply.</span></a>
</div>

{index_html}
"""
home = shell("Overview", "Architecture and UX proposal for Sleuth Forensics' internal engagement platform.",
             build_nav("", depth=0), home_body, [], depth=0, extra_class="home")
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(home)

open(os.path.join(ROOT, "search-index.json"), "w", encoding="utf-8").write(
    json.dumps(search_index, separators=(",", ":")))
open(os.path.join(ROOT, ".nojekyll"), "w").write("")

print(f"built {len(files)} pages + index")
