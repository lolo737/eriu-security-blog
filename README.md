# eriu-security-blog

The **Eriu Technology** security-awareness series — short, story-led, plain-English briefings on the threats that actually hit small businesses. Awareness and defence only; no build instructions.

## Live site

With GitHub Pages on (Settings → Pages → Deploy from a branch → `main` / root):

**https://lolo737.github.io/eriu-security-blog/**

The root `index.html` is the landing page; each briefing lives in its own folder with an article (`index.html`), a standalone `poster.html`, the poster PNG and a Markdown copy.

## The 14 briefings

1. **Plug & Prey** — BadUSB / HID injection (the found USB stick)
2. **Free Wi-Fi, Dear Price** — public & rogue Wi-Fi, evil twins
3. **Wire & Deceit** — invoice fraud / business email compromise
4. **The Phish & Chips** — phishing
5. **Held to Ransom** — ransomware & tested backups
6. **Keys to the Kingdom** — password reuse & MFA
7. **The Voice on the Phone** — AI voice-clone / deepfake fraud
8. **The Leaving Do** — offboarding & dormant access
9. **Cloudy with a Chance of Breach** — M365/Google account takeover
10. **Shadow IT** — unsanctioned apps
11. **Patch or Perish** — unpatched software
12. **The Lost Laptop** — device loss & encryption
13. **The Smart Office** — IoT (printers, cameras, routers)
14. **GDPR for the Terrified** — data protection in plain words

## House style

Every briefing follows the same shape: a story-led, Jerry-voice intro that makes someone actually read → a one-page poster that carries the gist → a plain-English explainer (what it is · how it works · why it's dangerous · how you stop it). Dark cyber look, cyan/amber/red/green accents.

## Adding a post

Add the copy to `blog_content.py`, run the generator, render the poster, rebuild the landing page — it drops in as a new folder and a card. No new repo needed.

— *Eriu Technology · eriu.tech*
