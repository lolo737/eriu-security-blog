// Render posters with real Google fonts (Oswald/Inter/JetBrains Mono) from local @fontsource files,
// for sandboxes that can't reach fonts.googleapis.com. Usage: FONTDIR=/path/node_modules/@fontsource node render_fonts.js <slug...>
const { chromium } = require('playwright');
const path = require('path');
const FD = process.env.FONTDIR || '/tmp/fonts/node_modules/@fontsource';
const f = (pkg, name) => 'file://' + path.join(FD, pkg, 'files', name);
const face = (fam, w, url) => `@font-face{font-family:'${fam}';font-weight:${w};font-style:normal;src:url('${url}') format('woff2');}`;
const css = [
  ...[600,700].map(w => face('Oswald', w, f('oswald', `oswald-latin-${w}-normal.woff2`))),
  ...[400,500,600,700].map(w => face('Inter', w, f('inter', `inter-latin-${w}-normal.woff2`))),
  face('JetBrains Mono', 400, f('jetbrains-mono', 'jetbrains-mono-latin-400-normal.woff2')),
].join('\n');
(async () => {
  const slugs = process.argv.slice(2);
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  await page.setViewportSize({ width: 960, height: 1400 });
  for (const s of slugs) {
    await page.goto(`file://${path.resolve(__dirname, '..', s, 'poster.html')}`, { waitUntil: 'load' });
    await page.addStyleTag({ content: css });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(900);
    const el = await page.$('.poster');
    await el.screenshot({ path: path.resolve(__dirname, '..', s, `${s}.png`) });
    console.log('rendered', s);
  }
  await browser.close();
})();
