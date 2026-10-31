# -*- coding: utf-8 -*-
import html
exec(open("/home/claude/blog_content.py").read())

def esc(s): return html.escape(s, quote=False)

# 2 existing + 12 generated
cards = [
  ("./plug-and-prey/","./plug-and-prey/security-awareness_piece.png","Plug & Prey",
   "It looks like a mouse. It types like an intruder.",
   "The USB stick you found outside work, and why plugging it in is the whole attack. BadUSB / HID-injection, in plain English."),
  ("./free-wifi/","./free-wifi/free_wifi_dear_price.png","Free Wi-Fi, Dear Price",
   "The network with no password has no conscience.",
   "The Faustian pact at the departure gate — evil-twin hotspots, what they can read, and why you never bank on public Wi-Fi."),
]
for p in POSTS:
    cards.append(("./%s/"%p["slug"], "./%s/%s.png"%(p["slug"],p["slug"]), p["title"], p["tagline"], p["subtitle"]))

card_html = ""
for href,thumb,title,sub,hook in cards:
    card_html += ('<a class="card" href="%s"><div class="thumb"><img src="%s" alt="%s poster" loading="lazy"></div>'
                  '<div class="txt"><h2>%s</h2><div class="sub">%s</div><div class="hook">%s</div>'
                  '<div class="read">Read the briefing &rarr;</div></div></a>\n'
                  % (href, thumb, esc(title), esc(title), esc(sub), esc(hook)))

CSS = """
  :root{--cy:#00dbcc;--am:#ffb81a;--rd:#f54447;--gn:#40ea99;--ink:#d7e7ea;--soft:#aec3c7;--mut:#7f969b;--line:rgba(0,219,204,.18);}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:radial-gradient(90% 38% at 50% -5%, rgba(0,219,204,.12), transparent 60%),linear-gradient(180deg,#041216 0%,#02090b 100%);background-attachment:fixed;color:var(--ink);font-family:'Inter',system-ui,sans-serif;line-height:1.7;font-size:18px;-webkit-font-smoothing:antialiased;padding:0 18px 90px}
  .wrap{max-width:820px;margin:0 auto}
  header.top{border-bottom:1px solid var(--line);padding:22px 0;margin-bottom:54px;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
  .brand{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--cy)}
  .brand b{color:var(--ink);font-weight:500}.brand a{color:var(--am);text-decoration:none}
  .hero{margin-bottom:56px}
  h1{font-family:'Oswald',sans-serif;font-weight:700;line-height:1.0;font-size:clamp(42px,8vw,72px);text-transform:uppercase;color:#eafcfd;letter-spacing:.005em;margin-bottom:18px}
  .hero p{font-size:21px;color:var(--soft);max-width:620px;line-height:1.5}
  .hero .meta{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin-top:22px}
  .seclabel{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--cy);margin-bottom:22px;border-bottom:1px solid var(--line);padding-bottom:10px}
  .posts{display:flex;flex-direction:column;gap:26px}
  .card{display:grid;grid-template-columns:150px 1fr;gap:24px;align-items:stretch;border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none;background:rgba(5,16,19,.55);transition:border-color .15s,transform .15s}
  .card:hover{border-color:rgba(0,219,204,.5);transform:translateY(-2px)}
  .card .thumb{overflow:hidden;background:#01080a;border-right:1px solid var(--line)}
  .card .thumb img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
  .card .txt{padding:22px 24px 22px 0;display:flex;flex-direction:column;justify-content:center}
  .card h2{font-family:'Oswald',sans-serif;font-weight:700;text-transform:uppercase;font-size:26px;color:#eafcfd;letter-spacing:.01em;margin-bottom:8px}
  .card .sub{color:var(--am);font-size:14px;font-weight:600;margin-bottom:10px}
  .card .hook{color:var(--soft);font-size:16px;line-height:1.5}
  .card .read{color:var(--cy);font-family:'JetBrains Mono',monospace;font-size:12.5px;letter-spacing:.1em;margin-top:14px;text-transform:uppercase}
  footer{margin-top:64px;padding-top:22px;border-top:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.08em;color:var(--mut);text-transform:uppercase;line-height:1.9}
  @media(max-width:540px){.card{grid-template-columns:1fr}.card .thumb{height:150px;border-right:0;border-bottom:1px solid var(--line)}.card .txt{padding:0 22px 22px}}
"""

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">'

page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Eriu Technology — Security Awareness</title>
<meta name="description" content="Plain-language security-awareness briefings for Irish SMBs, from Eriu Technology. Story-led, no jargon, defence only.">
%s<style>%s</style></head><body><div class="wrap">
<header class="top"><div class="brand"><b>Eriu Technology</b> &nbsp;·&nbsp; Security Awareness</div><div class="brand"><a href="https://eriu.tech">eriu.tech &rarr;</a></div></header>
<section class="hero"><h1>Security, in plain English.</h1>
<p>Short, story-led briefings on the threats that actually hit small businesses — no jargon, no scare-selling, just what the attack is and how you lock it out. Awareness and defence only.</p>
<div class="meta">Eriu Technology &nbsp;·&nbsp; for Irish SMBs &nbsp;·&nbsp; %d briefings</div></section>
<div class="seclabel">The Briefings</div>
<div class="posts">
%s</div>
<footer>Eriu Technology &nbsp;·&nbsp; eriu.tech &nbsp;·&nbsp; Security-awareness briefings<br>Awareness &amp; defence only &nbsp;·&nbsp; No build instructions</footer>
</div></body></html>""" % (FONTS, CSS, len(cards), card_html)

open("/home/claude/eriu-security-blog/index.html","w").write(page)
print("landing rebuilt with", len(cards), "cards")
