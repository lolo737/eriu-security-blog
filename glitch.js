/* Eriu briefings: TikTok-style RGB-split glitch on headlines.
   Self-contained: injects its own CSS, wraps heading text, no changes to the page layout.
   Respects prefers-reduced-motion (static colour split only). */
(function () {
  if (window.__eriuGlitch) return; window.__eriuGlitch = true;
  var css = [
    '.gl{position:relative;display:inline-block;max-width:100%;vertical-align:top;isolation:isolate;',
    'text-shadow:0 0 7px rgba(0,219,204,.42),0 0 22px rgba(0,219,204,.18);animation:gl-current 3.8s infinite steps(1,end)}',
    '.gl::before,.gl::after{content:attr(data-glitch);position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:hidden;white-space:inherit}',
    '.gl::before{color:#00f6ff;text-shadow:2px 0 #00f6ff,-2px 0 #ff2bd6;clip-path:inset(0 0 68% 0);transform:translateX(-2px);opacity:.78;animation:gl-a 2.7s infinite steps(1,end)}',
    '.gl::after{color:#ff36c9;text-shadow:2px 0 #ff36c9,-2px 0 #00eaff;clip-path:inset(72% 0 0 0);transform:translateX(2px);opacity:.72;animation:gl-b 3.1s infinite steps(1,end)}',
    '@keyframes gl-current{0%,88%,91%,94%,100%{text-shadow:0 0 7px rgba(0,219,204,.42),0 0 22px rgba(0,219,204,.18)}89%{text-shadow:3px 0 #00f6ff,-3px 0 #ff2bd6,0 0 18px #00eaff}90%{text-shadow:-2px 0 #00f6ff,2px 0 #ff2bd6,0 0 25px #ff2bd6}92%{text-shadow:0 0 5px #00f6ff,0 0 30px #00f6ff,0 0 42px rgba(255,43,214,.55)}}',
    '@keyframes gl-a{0%,82%,86%,100%{clip-path:inset(0 0 68% 0);transform:translateX(-2px);opacity:.68}83%{clip-path:inset(18% 0 55% 0);transform:translateX(7px);opacity:1}84%{clip-path:inset(4% 0 76% 0);transform:translateX(-6px);opacity:.95}85%{clip-path:inset(35% 0 42% 0);transform:translateX(5px);opacity:1}}',
    '@keyframes gl-b{0%,74%,79%,100%{clip-path:inset(72% 0 0 0);transform:translateX(2px);opacity:.62}75%{clip-path:inset(48% 0 24% 0);transform:translateX(-7px);opacity:1}76%{clip-path:inset(66% 0 8% 0);transform:translateX(6px);opacity:.95}77%{clip-path:inset(22% 0 58% 0);transform:translateX(-4px);opacity:1}78%{clip-path:inset(80% 0 0 0);transform:translateX(8px);opacity:.9}}',
    '@media (prefers-reduced-motion:reduce){.gl,.gl::before,.gl::after{animation:none}}'
  ].join('');
  function wrap(h) {
    if (!h || h.querySelector('.gl') || h.closest('.card')) return;
    var kids = Array.prototype.slice.call(h.childNodes).filter(function (n) {
      return !(n.nodeType === 1 && n.classList.contains('num'));
    });
    var text = kids.map(function (n) { return n.textContent; }).join('').replace(/\s+/g, ' ').trim();
    if (!text) return;
    var span = document.createElement('span');
    span.className = 'gl'; span.setAttribute('data-glitch', text);
    kids.forEach(function (n) { span.appendChild(n); });
    h.appendChild(span);
  }
  function run() {
    var st = document.createElement('style'); st.id = 'eriu-glitch-css'; st.textContent = css;
    document.head.appendChild(st);
    var list = document.querySelectorAll('h1.title, article h2, .hero h1, .wrap > h1');
    Array.prototype.forEach.call(list, wrap);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
