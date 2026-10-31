# -*- coding: utf-8 -*-
import os, re, html, json

OUT = "/home/claude/eriu-security-blog"

def to_html(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    return s
def to_plain(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'\*(.+?)\*', r'\1', s)
    return html.escape(s, quote=False)

POSTER_CSS = """
  :root{--cy:#00dbcc;--am:#ffb81a;--rd:#f54447;--gn:#40ea99;--ink:#d2e6ea;--mut:#8aa0a6;}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#01080a;color:var(--ink);font-family:'Inter',system-ui,sans-serif;display:flex;justify-content:center;padding:28px 14px;min-height:100vh}
  .poster{position:relative;width:100%;max-width:900px;overflow:hidden;border:1px solid rgba(0,219,204,.25);border-radius:6px;
    background:radial-gradient(120% 60% at 50% -8%, rgba(0,219,204,.28), transparent 60%),radial-gradient(130% 55% at 50% 108%, rgba(245,68,71,.16), transparent 60%),linear-gradient(180deg,#053037 0%,#031417 42%,#01080a 100%);
    box-shadow:0 0 70px rgba(0,219,204,.12), inset 0 0 160px rgba(0,0,0,.8);padding:46px 40px 34px}
  .poster::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(180deg,rgba(0,0,0,.26) 0 1px,transparent 1px 5px);mix-blend-mode:multiply;opacity:.55}
  .poster::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:3;box-shadow:inset 0 0 180px 40px rgba(0,0,0,.9)}
  .layer{position:relative;z-index:4}
  .classbar{border:1px solid rgba(0,219,204,.7);background:rgba(0,219,204,.08);font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.2em;color:var(--cy);text-transform:uppercase;padding:9px 12px;text-align:center}
  .hero{text-align:center;padding:34px 0 6px}
  .title{font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;line-height:.92;font-size:clamp(52px,11vw,104px);letter-spacing:.01em;color:#eafcfd;text-shadow:-3px 0 rgba(245,68,71,.85),3px 0 rgba(0,219,204,.85),0 0 34px rgba(0,219,204,.5);text-transform:uppercase}
  .tag{font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:600;color:var(--am);letter-spacing:.1em;font-size:clamp(15px,2.5vw,23px);margin-top:18px;text-transform:uppercase}
  .sub{max-width:680px;margin:14px auto 0;color:#bcd2d6;font-size:16px;line-height:1.5}
  .stack{display:flex;flex-direction:column;gap:22px;margin-top:30px}
  .panel{border:1.5px solid;border-radius:14px;padding:22px 26px 24px;background:rgba(5,16,19,.72)}
  .p-cy{border-color:rgba(0,219,204,.85)}.p-am{border-color:rgba(255,184,26,.85)}.p-rd{border-color:rgba(245,68,71,.85)}.p-gn{border-color:rgba(64,234,153,.85)}
  .kick{font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;letter-spacing:.14em;font-size:19px;text-transform:uppercase;margin-bottom:12px}
  .kick.cy{color:var(--cy)}.kick.am{color:var(--am)}.kick.rd{color:var(--rd)}.kick.gn{color:var(--gn)}
  .body{font-size:16.5px;line-height:1.5;color:var(--ink)}
  .steps{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:14px}
  .step{background:rgba(0,219,204,.08);border-radius:10px;padding:12px 14px 15px}
  .step .n{font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;font-size:30px;color:var(--cy);line-height:1}
  .step .t{font-size:13.5px;line-height:1.32;color:var(--ink);margin-top:6px}
  .ex{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
  .e{background:rgba(255,184,26,.08);border-radius:10px;padding:14px 13px 15px}
  .e b{display:block;font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;letter-spacing:.03em;font-size:15px;color:#ffe4a6;text-transform:uppercase;margin-bottom:6px}
  .e span{font-size:13px;line-height:1.3;color:var(--ink)}
  .alert{border:2px solid var(--rd);background:rgba(245,68,71,.12);border-radius:14px;padding:20px 24px;display:flex;gap:18px;align-items:flex-start}
  .alert .bang{font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;font-size:40px;color:var(--rd);line-height:.9;flex:none}
  .alert .atxt b{display:block;font-family:'Oswald','Arial Narrow',Impact,sans-serif;font-weight:700;letter-spacing:.06em;font-size:21px;color:#ffd4d5;text-transform:uppercase;margin-bottom:5px}
  .alert .atxt span{font-size:15.5px;line-height:1.45;color:#f3d9da}
  ul.hit{list-style:none;display:flex;flex-direction:column;gap:9px}
  ul.hit li{display:flex;gap:11px;font-size:16px;line-height:1.42}
  ul.hit li::before{content:"\\25B8";font-weight:700;flex:none}
  .rd li::before{color:var(--rd)}.gn li::before{color:var(--gn)}
  .credits{text-align:center;margin-top:26px;color:var(--mut);font-family:'JetBrains Mono',monospace}
  .credits .c1{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:#9fb6bb}
  .credits .c2{font-size:11px;letter-spacing:.1em;margin-top:8px;line-height:1.6;text-transform:uppercase}
"""

ARTICLE_CSS = """
  :root{--cy:#00dbcc;--am:#ffb81a;--rd:#f54447;--gn:#40ea99;--ink:#d7e7ea;--soft:#aec3c7;--mut:#7f969b;--line:rgba(0,219,204,.18);}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:radial-gradient(90% 40% at 50% -5%, rgba(0,219,204,.10), transparent 60%),linear-gradient(180deg,#041216 0%,#02090b 100%);background-attachment:fixed;color:var(--ink);font-family:'Inter',system-ui,sans-serif;line-height:1.72;font-size:18px;-webkit-font-smoothing:antialiased;padding:0 18px 80px}
  .wrap{max-width:720px;margin:0 auto}
  header.top{border-bottom:1px solid var(--line);padding:22px 0;margin-bottom:40px;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
  .brand{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--cy)}
  .brand b{color:var(--ink);font-weight:500}
  .brand a{color:var(--cy);text-decoration:none}
  .toplink{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;color:var(--am);text-decoration:none;border:1px solid rgba(255,184,26,.5);padding:6px 12px;border-radius:6px}
  .toplink:hover{background:rgba(255,184,26,.1)}
  h1.title{font-family:'Oswald',sans-serif;font-weight:700;line-height:1.02;font-size:clamp(40px,8vw,64px);letter-spacing:.005em;color:#eafcfd;text-transform:uppercase;margin-bottom:14px}
  .deck{font-size:21px;color:var(--soft);line-height:1.5;max-width:620px}
  .byline{font-family:'JetBrains Mono',monospace;font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin-top:22px}
  figure.hero{margin:40px 0 8px}
  figure.hero a{display:block;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 0 50px rgba(0,219,204,.10)}
  figure.hero img{display:block;width:100%;height:auto}
  figure.hero figcaption{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--mut);margin-top:10px;text-align:center;letter-spacing:.06em}
  figure.hero a:hover{border-color:rgba(0,219,204,.45)}
  article{margin-top:46px}
  article h2{font-family:'Oswald',sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.04em;font-size:27px;color:#eafcfd;margin:46px 0 16px;padding-top:10px}
  article h2 .num{color:var(--cy);margin-right:10px}
  article p{margin:0 0 20px;color:var(--ink)}
  article p.lead{font-size:20px}
  article em{color:#eef7f8;font-style:italic}
  article strong{color:#fff}
  .kicker{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--cy);border:1px solid var(--line);border-radius:5px;padding:4px 10px;margin-bottom:14px}
  ul{list-style:none;margin:0 0 22px;display:flex;flex-direction:column;gap:11px}
  ul li{display:flex;gap:12px;color:var(--ink)}
  ul li::before{content:"\\25B8";flex:none;color:var(--am);font-weight:700}
  ul.danger li::before{color:var(--rd)}ul.defend li::before{color:var(--gn)}
  ol.steps{list-style:none;counter-reset:s;margin:0 0 22px;display:flex;flex-direction:column;gap:12px}
  ol.steps li{counter-increment:s;display:flex;gap:16px;align-items:baseline}
  ol.steps li::before{content:counter(s);font-family:'Oswald',sans-serif;font-weight:700;font-size:26px;color:var(--cy);flex:none;width:30px}
  .callout{border:2px solid var(--rd);background:rgba(245,68,71,.10);border-radius:12px;padding:20px 24px;margin:0 0 26px}
  .callout b{display:block;font-family:'Oswald',sans-serif;font-weight:700;letter-spacing:.05em;text-transform:uppercase;font-size:22px;color:#ffd4d5;margin-bottom:8px}
  .callout p{margin:0;color:#f3d9da;font-size:17px}
  hr{border:0;border-top:1px solid var(--line);margin:40px 0}
  .outro{color:var(--soft);font-size:16.5px;font-style:italic}
  footer{margin-top:54px;padding-top:22px;border-top:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.08em;color:var(--mut);text-transform:uppercase;line-height:1.8}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

def poster_html(p):
    steps = "".join('<div class="step"><div class="n">%d</div><div class="t">%s</div></div>' % (i+1, to_plain(s)) for i,s in enumerate(p["steps"]))
    ex = "".join('<div class="e"><b>%s</b><span>%s</span></div>' % (to_plain(l), to_plain(c)) for l,c in p["examples"])
    danger = "".join('<li>%s</li>' % to_plain(x) for x in p["danger"])
    defend = "".join('<li>%s</li>' % to_plain(x) for x in p["defend"])
    return """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — Eriu Security Awareness</title>%s<style>%s</style></head><body><div class="poster"><div class="layer">
<div class="classbar">Security Awareness Briefing &nbsp;//&nbsp; Eriu Technology &nbsp;//&nbsp; Defensive Use Only</div>
<div class="hero"><h1 class="title">%s</h1><div class="tag">%s</div><p class="sub">%s</p></div>
<div class="stack">
<section class="panel p-cy"><div class="kick cy">01 / What it is</div><p class="body">%s</p></section>
<section class="panel p-cy"><div class="kick cy">02 / How it works</div><div class="steps">%s</div><p class="body" style="color:var(--am);font-weight:600;font-size:15.5px">%s</p></section>
<section class="panel p-am"><div class="kick am">%s</div><p class="body">%s</p><div class="ex">%s</div></section>
<section class="alert"><div class="bang">!</div><div class="atxt"><b>%s</b><span>%s</span></div></section>
<section class="panel p-rd"><div class="kick rd">03 / Why it's dangerous</div><ul class="hit rd">%s</ul></section>
<section class="panel p-gn"><div class="kick gn">04 / How you stop it</div><ul class="hit gn">%s</ul></section>
</div>
<div class="credits"><div class="c1">%s</div><div class="c2">An Eriu Technology security briefing &nbsp;·&nbsp; Awareness &amp; defence only</div></div>
</div></div></body></html>""" % (
        to_plain(p["title"]), FONTS, POSTER_CSS, p["ptitle"], to_plain(p["tagline"]), to_plain(p["subtitle"]),
        to_plain(p["what"]), steps, to_plain(p["outcome"]), to_plain(p["sec3_label"]), to_plain(p["sec3_intro"]), ex,
        to_plain(p["alert_title"]), to_plain(p["alert_body"]), danger, defend, to_plain(p["credit_line"]))

def article_html(p):
    intro = "".join('<p class="lead">%s</p>' % to_html(p["intro"][0]) if i==0 else '<p>%s</p>' % to_html(x) for i,x in enumerate(p["intro"]))
    steps = "".join('<li>%s</li>' % to_html(s) for s in p["steps"])
    ex = "".join('<li><strong>%s</strong> — %s</li>' % (to_html(l), to_html(c)) for l,c in p["examples"])
    danger = "".join('<li>%s</li>' % to_html(x) for x in p["danger"])
    defend = "".join('<li>%s</li>' % to_html(x) for x in p["defend"])
    return """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — Eriu Technology</title><meta name="description" content="%s">%s<style>%s</style></head><body><div class="wrap">
<header class="top"><div class="brand"><b>Eriu Technology</b> &nbsp;·&nbsp; Security Awareness</div><a class="toplink" href="../">&larr; All briefings</a></header>
<h1 class="title">%s</h1><p class="deck">%s</p><div class="byline">Eriu Technology &nbsp;·&nbsp; 31 October 2026</div>
<figure class="hero"><a href="poster.html"><img src="%s.png" alt="%s poster"></a><figcaption>The one-page briefing. Click for the full-size poster.</figcaption></figure>
<article>
<span class="kicker">%s</span>
%s
<h2>What it actually is</h2><p>%s</p>
<h2><span class="num">01</span>How it works</h2><ol class="steps">%s</ol><p>%s</p>
<h2>%s</h2><p>%s</p><ul>%s</ul>
<div class="callout"><b>%s</b><p>%s</p></div>
<h2><span class="num">02</span>Why it's dangerous</h2><ul class="danger">%s</ul>
<h2><span class="num">03</span>How you stop it</h2><ul class="defend">%s</ul>
<hr><p class="outro">%s</p>
</article>
<footer>Eriu Technology &nbsp;·&nbsp; eriu.tech &nbsp;·&nbsp; Security-awareness briefings<br>Awareness &amp; defence only &nbsp;·&nbsp; No build instructions</footer>
</div></body></html>""" % (
        to_html(p["title"]), to_html(p["subtitle"]), FONTS, ARTICLE_CSS,
        to_html(p["title"]), to_html(p["subtitle"]), p["slug"], to_html(p["title"]),
        to_html(p["intro_kicker"]), intro, to_html(p["what"]), steps, to_html(p["outcome"]),
        to_html(p["sec3_label"]), to_html(p["sec3_intro"]), ex, to_html(p["alert_title"]), to_html(p["alert_body"]),
        danger, defend, to_html(p["outro"]))

def md(p):
    fm = "---\ntitle: \"%s\"\ndescription: %s\nauthor: Eriu Technology\ndate: 2026-10-31\ntags: [security-awareness, smb-security]\n---\n\n" % (p["title"], p["subtitle"])
    out = fm + "![%s poster](./%s.png)\n\n" % (p["title"], p["slug"])
    out += "## %s\n\n" % p["intro_kicker"]
    out += "\n\n".join(p["intro"]) + "\n\n"
    out += "## What it actually is\n\n%s\n\n" % p["what"]
    out += "## How it works\n\n" + "\n".join("%d. %s" % (i+1,s) for i,s in enumerate(p["steps"])) + "\n\n%s\n\n" % p["outcome"]
    out += "## %s\n\n%s\n\n" % (p["sec3_label"], p["sec3_intro"]) + "\n".join("- **%s** — %s" % (l,c) for l,c in p["examples"]) + "\n\n"
    out += "## ⚠ %s\n\n%s\n\n" % (p["alert_title"], p["alert_body"])
    out += "## Why it's dangerous\n\n" + "\n".join("- %s" % x for x in p["danger"]) + "\n\n"
    out += "## How you stop it\n\n" + "\n".join("- %s" % x for x in p["defend"]) + "\n\n"
    out += "---\n\n*%s*\n" % p["outro"]
    return out

exec(open("/home/claude/blog_content.py").read())

for p in POSTS:
    d = os.path.join(OUT, p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d,"poster.html"),"w").write(poster_html(p))
    open(os.path.join(d,"index.html"),"w").write(article_html(p))
    open(os.path.join(d,"%s.md"%p["slug"]),"w").write(md(p))
    print("built", p["slug"])

print(json.dumps([p["slug"] for p in POSTS]))
