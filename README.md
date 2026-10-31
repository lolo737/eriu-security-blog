# eriu-security-blog

The **Eriu Technology** security-awareness series — short, story-led, plain-English briefings on the threats that actually hit small businesses. Awareness and defence only; no build instructions.

## Live site

With GitHub Pages on (Settings → Pages → Deploy from a branch → `main` / root), the blog is live at:

**https://lolo737.github.io/eriu-security-blog/**

The root `index.html` is the landing page; each post lives in its own folder.

## Structure

```
index.html                  → landing page (lists all briefings)
plug-and-prey/              → Plug & Prey (BadUSB / HID injection)
  index.html               · the article
  poster.html              · standalone poster
  security-awareness_piece.png
  security-awareness_piece.md
free-wifi/                 → Free Wi-Fi, Dear Price (public / rogue Wi-Fi)
  index.html               · the article
  poster.html              · standalone poster
  free_wifi_dear_price.png
  free_wifi_dear_price.md
```

## House style

Every briefing follows the same shape: a story-led, Jerry-voice intro that makes someone actually read → a one-page poster that carries the gist → a plain-English explainer (what it is · how it works · why it's dangerous · how you stop it). Dark cyber look, cyan/amber/red/green accents.

## Adding a post

Drop a new folder (e.g. `wire-and-deceit/`) with its `index.html`, `poster.html`, PNG and `.md`, then add a card to the root `index.html`. No new repo needed.

— *Eriu Technology · eriu.tech*
