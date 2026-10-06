// 카카오톡·SNS 미리보기 카드(1200x630) 생성: node build/make_og.cjs
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const countries = JSON.parse(fs.readFileSync(path.join(root, 'build/data/countries.json'), 'utf8'));
const fields = JSON.parse(fs.readFileSync(path.join(root, 'build/data/fields.json'), 'utf8'));
const bg = 'data:image/jpeg;base64,' + fs.readFileSync(path.join(root, 'assets/airport.jpg')).toString('base64');
const logo = fs.readFileSync(path.join(root, 'assets/logo.svg'), 'utf8');
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function html({eyebrow, title, sub, pills, code}) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0}
  body{width:1200px;height:630px;font-family:"Noto Sans CJK KR","Noto Color Emoji",sans-serif;color:#0b2545;position:relative;overflow:hidden;background:#fff}
  .bg{position:absolute;inset:0;background:url(${bg}) center/cover;opacity:.55}
  .fade{position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.97) 48%,rgba(255,255,255,.55) 78%,rgba(255,255,255,.25) 100%)}
  .wrap{position:absolute;inset:0;padding:64px 72px;display:flex;flex-direction:column}
  .brand{display:flex;align-items:center;gap:14px;font-size:30px;font-weight:900;letter-spacing:-.5px}
  .brand svg{width:56px;height:56px}
  .eyebrow{margin-top:54px;font-size:30px;font-weight:700;color:#3b5b85}
  h1{margin-top:10px;font-size:${title.length > 9 ? 70 : 84}px;line-height:1.12;font-weight:900;letter-spacing:-2px}
  .sub{margin-top:18px;font-size:32px;font-weight:500;color:#334e70}
  .pills{margin-top:auto;display:flex;gap:12px;flex-wrap:wrap}
  .pill{font-size:27px;font-weight:700;padding:12px 22px;border-radius:999px;background:#0b2545;color:#fff}
  .pill.y{background:#ffcc1f;color:#0b2545}
  .pill.l{background:#e8f1fb;color:#0b2545;border:2px solid #c9d9ee}
  .code{display:inline-block;vertical-align:middle;margin-left:14px;font-family:"DejaVu Sans Mono",monospace;font-size:24px;font-weight:700;color:#ffcc1f;background:#0b2545;padding:4px 12px;border-radius:8px;letter-spacing:3px}
  .url{position:absolute;right:64px;top:70px;font-size:26px;font-weight:700;color:#0b2545;background:rgba(255,255,255,.85);padding:8px 16px;border-radius:10px}
  </style></head><body><div class="bg"></div><div class="fade"></div>
  <div class="wrap">
    <div class="brand">${logo}<span>입국노트</span></div>
    <div class="eyebrow">${esc(eyebrow)}${code ? `<span class="code">${esc(code)}</span>` : ''}</div>
    <h1>${title}</h1>
    <div class="sub">${esc(sub)}</div>
    <div class="pills">${pills.map(p => `<span class="pill ${p[1]||''}">${esc(p[0])}</span>`).join('')}</div>
  </div>
  <div class="url">ipguknote.com</div>
  </body></html>`;
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const jobs = [['home', {
    eyebrow: '해외 전자 입국신고 15개국 총정리',
    title: '공식 사이트에서<br>무료로 직접 하세요',
    sub: '🇯🇵 일본 · 🇻🇳 베트남 · 🇹🇭 태국 · 🇵🇭 필리핀 · 🇬🇺 괌 외',
    pills: [['신청 시각 계산기', 'y'], ['공식 주소 확인'], ['가짜 유료 사이트 주의', 'l']],
  }]];
  for (const c of countries) {
    const free = c.fee.trim() === '무료';
    const pills = [[c.window_text, 'y'], [free ? '공식 사이트 무료' : '공식 요금 있음']];
    if (fields[c.slug]) pills.push(['영문 항목 번역표', 'l']);
    else pills.push(['작성 순서 정리', 'l']);
    jobs.push([c.slug, {
      eyebrow: `${c.flag} ${c.name} 전자 입국신고`,
      title: esc(`${c.name} 입국신고`),
      sub: `${c.form_short} 작성법 · 2026 최신`,
      pills, code: c.code,
    }]);
  }
  for (const [name, d] of jobs) {
    await p.setContent(html(d), { waitUntil: 'load' });
    await p.screenshot({ path: path.join(root, 'assets/og', name + '.jpg'), type: 'jpeg', quality: 86 });
  }
  await b.close();
  console.log('made', jobs.length);
})();
