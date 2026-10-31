const { chromium } = require('playwright');
const slugs = ["wire-and-deceit","the-phish-and-chips","held-to-ransom","keys-to-the-kingdom",
  "the-voice-on-the-phone","the-leaving-do","cloudy-with-a-chance-of-breach","shadow-it",
  "patch-or-perish","the-lost-laptop","the-smart-office","gdpr-for-the-terrified"];
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  await page.setViewportSize({ width: 960, height: 1400 });
  for (const s of slugs) {
    const f = `file:///home/claude/eriu-security-blog/${s}/poster.html`;
    await page.goto(f, { waitUntil: 'load' });
    try { await page.evaluate(() => document.fonts.ready); } catch (e) {}
    await page.waitForTimeout(900);
    const el = await page.$('.poster');
    await el.screenshot({ path: `/home/claude/eriu-security-blog/${s}/${s}.png` });
    console.log('rendered', s);
  }
  await browser.close();
})();
