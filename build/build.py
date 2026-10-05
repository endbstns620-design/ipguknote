"""입국노트 정적 페이지 생성기 — 실행: python build/build.py (프로젝트 폴더에서)"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from countries import COUNTRIES, AFFILIATES, VERIFIED, SITE_URL, REGIONS, BASE, FORM_URL
from guides import GUIDES

with open(os.path.join(os.path.dirname(__file__), "data", "fields.json"), encoding="utf-8") as _f:
    FIELDS = json.load(_f)


def field_guide(c):
    f = FIELDS.get(c["slug"])
    if not f:
        return ""
    basis = ("공식 화면·매뉴얼 기준으로 정리했어요." if f["confidence"] == "high"
             else "일부 항목은 공식 안내와 화면 캡처가 있는 여행 가이드를 함께 참고했어요. 실제 화면의 표현이 조금 다를 수 있어요.")
    ko = {True: "공식 사이트에서 한국어 화면을 고를 수 있어요.", False: "공식 사이트에 한국어 화면이 없어요. 아래 번역표를 옆에 두고 작성하세요."}.get(
        f["korean_ui"], "한국어 화면 제공 여부가 확인되지 않았어요. 아래 번역표를 옆에 두고 작성하세요.")
    secs = ""
    for s in f["sections"]:
        has_ui = any(x.get("ko_ui") for x in s["fields"])
        rows = "".join(
            f"""<div class="fg-row{' fg4' if has_ui else ''}"><div class="fg-label">{e(x['label'])}{' <span class="req">필수</span>' if x.get('required') else ''}</div>
{f'<div class="fg-ui"><span class="fg-ui-tag">한국어 화면</span>{e(x.get("ko_ui") or "-")}</div>' if has_ui else ''}<div class="fg-ko">{e(x['ko'])}</div><div class="fg-how">{e(x['how'])}</div></div>"""
            for x in s["fields"])
        head = ('<div class="fg-head fg4"><span>화면 영문 항목</span><span>한국어 화면 표시</span><span>실제 뜻</span><span>이렇게 적어요</span></div>'
                if has_ui else '<div class="fg-head"><span>화면 영문 항목</span><span>뜻</span><span>이렇게 적어요</span></div>')
        secs += f'<details class="fg-sec"><summary>{e(s["title"])} <span class="fg-n">{len(s["fields"])}개 항목</span></summary>{head}{rows}</details>'
    pit = "".join(f"<li>{e(p)}</li>" for p in f.get("pitfalls", []))
    src = " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>' for t, u in f.get("sources", []))
    return f"""
<section class="card fieldguide" id="field-guide">
  <div class="panel-head"><h2>항목별 번역표</h2><span class="tag">영문 항목 → 한글</span></div>
  <p class="small" style="margin-top:0"><strong style="color:var(--yellow)">{e(f.get('korean_ui_note') or ko)}</strong><br><span class="muted">{basis} 입국노트는 양식을 대신 작성하거나 파일로 배포하지 않아요. 공식 사이트 화면을 보면서 참고하세요.</span></p>
  {secs}
  {f'<div class="warn" style="margin-top:16px"><h2>한국인이 자주 틀리는 부분</h2><ul class="tips">{pit}</ul></div>' if pit else ''}
  <p class="small muted" style="margin-bottom:0">번역표 참고 자료: {src}</p>
</section>"""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "입국노트"
e = html.escape
PAGES = []  # sitemap용 경로
# 공식 자료 미확인으로 내린 나라 — 예전 주소로 들어오면 홈으로 보냄
REMOVED = ["laos", "timor-leste", "bangladesh", "saipan", "sint-maarten", "curacao", "russia",
           "brunei", "india", "papua-new-guinea", "cuba", "dominican-republic", "jamaica", "aruba", "bermuda", "barbados", "saint-lucia", "trinidad-and-tobago", "panama", "guatemala", "colombia", "chile", "mauritius", "nigeria", "cape-verde"]

GENERAL_CHECK = [
    "여권 유효기간 6개월 이상 남았는지 확인",
    "왕복(또는 출국) 항공권 예약 확인서",
    "숙소 주소를 영문으로 메모",
]


def page(path, title, desc, body, jsonld=None, index=True):
    """path: 사이트 루트 기준 경로 ('' = 홈, 'vietnam/' 등)"""
    depth = path.count("/")
    up = "../" * depth
    home = up or "./"
    url = SITE_URL + "/" + path
    if index:
        PAGES.append(path)
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    robots = "" if index else '<meta name="robots" content="noindex">'
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{robots}
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b2d55">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=IBM+Plex+Sans+KR:wght@400;600;700&display=swap">
<link rel="icon" href="{up}assets/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{up}assets/icon-180.png">
<link rel="stylesheet" href="{up}assets/style.css">
{ld}
</head>
<body>
<div class="notice">정부 사이트가 아니에요 · 대행하지 않아요 · 신고는 각국 공식 사이트에서 무료로 직접</div>
<header class="top"><div class="wrap">
  <a class="logo" href="{home}" aria-label="입국노트 홈"><img src="{up}assets/logo.svg" alt="" width="30" height="30"><b>입국<span>노트</span></b></a>
  <div class="top-right"><span class="clock" data-clock><small>서울</small><span>--:--</span></span></div>
  <nav><a href="{up}#countries">나라별</a><a href="{up}guide/">가이드</a><a href="{up}guide/fake-sites/">가짜 사이트 구별</a></nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <p>입국노트는 해외 전자 입국신고를 직접 할 수 있도록 공식 정보를 정리한 안내 사이트입니다. 어떤 정부 기관과도 관련이 없으며 신고 대행이나 개인정보 수집을 하지 않습니다.</p>
  <p>정보 최종 확인: {VERIFIED}. 제도는 예고 없이 바뀔 수 있으니 출발 전 공식 사이트에서 한 번 더 확인하세요.</p>
  <p>일부 링크는 제휴 링크이며, 구매 시 입국노트가 수수료를 받을 수 있습니다. 이용자가 내는 가격은 같습니다.</p>
  <p><a href="{up}about/">운영 원칙·개인정보</a> · <a href="{up}contact/">정보 오류 제보·문의</a> · <a href="{up}guide/">가이드</a></p>
</div></footer>
<script src="{up}assets/app.js"></script>
</body>
</html>
"""


def flap(text, cls="flap"):
    spans = "".join(
        f'<span class="sp" style="--i:{i}"> </span>' if ch == " " else f'<span style="--i:{i}">{e(ch)}</span>'
        for i, ch in enumerate(text))
    return f'<span class="{cls}" aria-label="{e(text)}">{spans}</span>'


def status_tag(c):
    m = c["mandatory"]
    if m.startswith("의무"):
        cls = "st-req"
    elif m == "권장":
        cls = "st-adv"
    else:
        cls = "st-opt"
    out = f'<span class="status {cls}">{e(m.split(" ")[0])}</span>'
    if not is_free(c):
        out += '<span class="status st-fee">공식 요금</span>'
    return f'<span class="status-cell">{out}</span>'


def country_attrs(c):
    dl = f" data-dl='{json.dumps(c['deadline'], ensure_ascii=False)}'" if c.get("deadline") else ""
    v = c["window"]["value"] if c["window"]["value"] is not None else 0
    return (f'data-slug="{c["slug"]}" data-name="{e(c["name"])}" data-form="{e(c["form_short"])}" '
            f'data-url="{e(c["url"])}" data-iana="{c.get("iana") or ""}" data-ref="{c["window"]["ref"]}" '
            f'data-wtype="{c["window"]["type"]}" data-wval="{v}" data-tzlabel="{e(c["tz_label"])}"{dl}')


def calc_fields():
    return """
    <div class="calc-fields fields">
      <div><label for="d" data-reflabel="날짜">도착 날짜 (현지)</label><input id="d" type="date"></div>
      <div><label for="t" data-reflabel="시각">도착 시각 (현지)</label><input id="t" type="time" value="12:00"></div>
    </div>
    <p class="calc-anytime badge badge-green" hidden>출발 전 언제든 작성할 수 있어요. 신청 시작 시각을 기다릴 필요가 없어요.</p>"""



def affiliate_block():
    items = []
    for a in AFFILIATES:
        inner = f'<h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p>'
        if a["href"]:
            items.append(f'<a href="{e(a["href"])}" target="_blank" rel="sponsored noopener">{inner}</a>')
    if not items:
        return ""  # 제휴 링크가 하나도 없으면 섹션 자체를 숨김
    return f"""
<section>
  <h2>입국신고 말고, 출국 전에 챙길 것</h2>
  <div class="aff">{''.join(items)}</div>
  <p class="small muted">제휴 링크입니다. 입국노트는 이 링크로 수수료를 받을 수 있지만, 입국신고 자체로는 어떤 돈도 받지 않습니다.</p>
</section>"""


def guide_list(up, only=None):
    gs = [g for g in GUIDES if not only or g["slug"] in only]
    return '<ul class="guide-list">' + "".join(
        f'<li><a href="{up}guide/{g["slug"]}/">{e(g["title"])}</a></li>' for g in gs) + "</ul>"


def is_free(c):
    return c["fee"].strip() == "무료"


def region_groups():
    for key, label in REGIONS:
        cs = [c for c in COUNTRIES if c["region"] == key]
        if cs:
            yield key, label, cs


def compare_table(up):
    body = ""
    for key, label, cs in region_groups():
        body += f'<tr class="group"><th colspan="4">{e(label)}</th></tr>'
        body += "".join(
            f"""<tr><td>{c['flag']} <a href="{up}{c['slug']}/">{e(c['name'])}</a><br><span class="small muted">{e(c['form_short'])}</span></td>
<td>{e(c['mandatory'])}</td><td>{e(c['window_text'])}</td><td><code>{e(c['domain'])}</code></td></tr>"""
            for c in cs)
    return f"""<div class="table-scroll"><table class="compare">
      <thead><tr><th>국가</th><th>의무</th><th>신청 시점</th><th>공식 주소</th></tr></thead>
      <tbody>{body}</tbody>
    </table></div>"""


def build_index():
    n = len(COUNTRIES)
    blocks = ""
    for key, label, cs in region_groups():
        rows = "".join(
            f"""<a class="board-row" style="--i:{i}" href="{c['slug']}/" data-search="{e(c['name'])} {e(c['form_short'])} {c['slug']} {c['code']}">
  <span class="code">{c['code']}</span>
  <span class="dest"><span class="flag">{c['flag']}</span>{e(c['name'])}{' <span class="ko-tag">번역표</span>' if c['slug'] in FIELDS else ''}</span>
  <span class="form-name">{e(c['form_short'])}</span>
  <span class="opens">{e(c['window_text'])}</span>
  {status_tag(c)}
</a>"""
            for i, c in enumerate(cs))
        blocks += f"""<div class="region board" data-region-block>
  <div class="board-title"><h3>{e(label)}</h3><span>{len(cs)}개국</span></div>
  <div class="board-head"><span>공항</span><span>나라</span><span>신고서</span><span>신청 가능 시점</span><span>의무 여부</span></div>
  {rows}
</div>"""
    options = "".join(
        f'<optgroup label="{e(label)}">' + "".join(
            f'<option {country_attrs(c)}>{c["flag"]} {e(c["name"])} — {e(c["form_short"])}</option>' for c in cs) + "</optgroup>"
        for key, label, cs in region_groups())
    body = f"""
<h1>해외 입국신고,<br><span class="hl">공식 사이트에서 무료로</span> 직접 하세요</h1>
<p class="lead">한국인이 많이 가는 {n}개국의 전자 입국신고를 한곳에 정리했어요.</p>
<ul class="hero-points">
  <li><b>언제부터</b> 신청할 수 있는지 계산</li>
  <li><b>공식 사이트</b>로 바로 이동</li>
  <li>영문 항목을 한글로 풀어 쓴 <b>번역표</b> ({len(FIELDS)}개국)</li>
</ul>

<section>
  <div class="card calc" data-calc>
    <div class="panel-head"><h2>언제부터 신청할 수 있을까?</h2><span class="tag">계산기</span></div>
    <div class="fields"><div class="full"><label for="c">여행 국가</label><select id="c">{options}</select></div></div>
    {calc_fields()}
    <div class="calc-out" hidden></div>
  </div>
</section>

<section id="countries">
  <h2>나라별 안내</h2>
  <input id="country-search" class="search" type="search" placeholder="나라 이름 검색 (예: 일본, 괌)" aria-label="나라 검색">
  {blocks}
  <p class="small muted">한국인이 많이 가는 나라 중 공식 온라인 입국신고가 있는 곳만 실었어요. 여기 없는 나라는 2026년 10월 기준 종이 카드를 쓰거나, 돈을 내는 전자여행허가(ETA)·비자만 있거나, 공식 자료로 확인되지 않은 곳이에요.</p>
</section>

<section id="fake">
  <div class="warn">
    <h2>결제창이 나오면 공식 사이트가 아니에요</h2>
    <p>"arrival card", "e-travel" 같은 이름의 유료 대행 사이트가 많아요. 입국노트에 실린 나라의 공식 입국신고는 모두 <strong>무료</strong>예요.</p>
    <p class="small" style="margin-bottom:0"><a href="guide/fake-sites/">가짜 사이트 5초 구별법 →</a> · <a href="guide/compare/">{n}개국 공식 주소 표 →</a></p>
  </div>
</section>

<section>
  <h2>자주 찾는 가이드</h2>
  {guide_list("")}
</section>
{affiliate_block()}
"""
    ld = {"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": SITE_URL + "/",
          "description": f"전 세계 {n}개국 전자 입국신고 공식 사이트 안내"}
    return page("", f"해외 전자 입국신고 총정리 — 일본·베트남·태국·괌 등 {n}개국 | 입국노트",
                f"Visit Japan Web, 베트남·태국 입국신고, 괌 EDF 등 전 세계 {n}개국 전자 입국신고를 공식 사이트에서 직접 하는 방법과 신청 시점 계산기.",
                body, ld)


RELATED = {
    "vietnam": ["fake-sites", "timing", "family"],
    "thailand": ["fake-sites", "multi-country", "family"],
    "philippines": ["philippines-red-qr", "fake-sites", "family"],
    "malaysia": ["timing", "multi-country", "fake-sites"],
    "singapore": ["family", "timing", "multi-country"],
}
DEFAULT_RELATED = ["fake-sites", "timing", "family"]


def build_country(c):
    up = "../"
    steps = "".join(f"<li>{e(s)}</li>" for s in c["steps"])
    tips = "".join(f"<li>{e(s)}</li>" for s in c["tips"])
    checks = c["needs"] + GENERAL_CHECK + [f"공식 사이트에서 {c['form_short']} 제출", "받은 QR·확인 메일 캡처해 두기"]
    checklist = "".join(f'<label><input type="checkbox"><span>{e(x)}</span></label>' for x in checks)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    sources = " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>' for t, u in c["sources"])
    region_label = dict(REGIONS)[c["region"]]
    sib = [o for o in COUNTRIES if o["region"] == c["region"] and o is not c]
    others = " · ".join(f'<a href="{up}{o["slug"]}/">{o["flag"]} {e(o["name"])}</a>' for o in sib)
    free = is_free(c)
    fee_short = "무료" if free else "공식 요금 있음"
    lead_fee = "공식 사이트에서 <strong>무료</strong>예요." if free else f"공식 요금: {e(c['fee'])}"
    low = ""
    if c.get("confidence") == "low":
        low = """<section class="warn"><h2>확인이 더 필요한 정보예요</h2><p style="margin:0">이 나라는 제도가 막 바뀌었거나 공식 안내가 엇갈려요. 출발 전 항공사나 해당국 대사관 안내를 꼭 함께 확인하세요.</p></section>"""
    has_calc = not (c["window"]["type"] == "anytime" and not c.get("deadline"))
    calc = f"""
<section>
  <div class="card calc" data-calc {country_attrs(c)}>
    <div class="panel-head"><h2>내 비행기 기준으로 계산하기</h2><span class="tag">계산기</span></div>
    {calc_fields()}
    <div class="calc-out" hidden></div>
  </div>
</section>""" if has_calc else ""
    body = f"""
<p class="crumb"><a href="{up}">입국노트</a> › {e(region_label)} › {e(c['name'])}</p>
<h1>{e(c['name'])} {e(c['form_short'])} 작성법</h1>
<p class="lead">{e(c['form'])}. {lead_fee} {e(c['window_text'])} 신청할 수 있어요.</p>

<section class="fids">
  <div class="fids-top"><span class="code">{c['code']}</span><span class="where">{c['flag']} {e(c['name'])}</span><span style="margin-left:auto">{status_tag(c)}</span></div>
  <div class="fids-grid">
    <div class="fids-cell"><b>신고서</b><span>{e(c['form_short'])}</span></div>
    <div class="fids-cell"><b>신청 가능 시점</b><span style="color:var(--blue)">{e(c['window_text'])}</span></div>
    <div class="fids-cell"><b>비용</b><span style="color:{'var(--green)' if free else 'var(--red)'}">{e(fee_short)}</span></div>
  </div>
</section>
{low}
<section>
  <div class="card gate">
    <div class="panel-head" style="margin-bottom:0"><h2>공식 사이트</h2><span class="tag">여기서 신청</span></div>
    <span class="domain">{e(c['domain'])}</span>
    <a class="btn btn-primary" href="{e(c['url'])}" target="_blank" rel="noopener">공식 사이트에서 신청하기{' (무료)' if free else ''} →</a>
    <p class="small muted" style="margin:0">{e(c['status'])}</p>
    {f'<p class="basis"><strong>공식 주소 근거:</strong> {e(c["official_basis"])}</p>' if c.get("official_basis") else ''}
    {'' if free else f'<p class="small" style="margin:0"><strong>요금 안내:</strong> {e(c["fee"])}</p>'}
  </div>
</section>
{calc}
<section class="card">
  <div class="panel-head"><h2>신청 순서</h2></div>
  <ol class="steps">{steps}</ol>
  <p class="small muted" style="margin-bottom:0">{e(c['result'])}</p>
</section>

{field_guide(c)}
<section class="card checklist" data-checklist="{c['slug']}">
  <div class="panel-head"><h2>준비물 체크리스트</h2><span class="check-count"></span></div>
  {checklist}
  <p class="small muted" style="margin:8px 0 0">체크 상태는 이 기기의 브라우저에만 저장돼요.</p>
</section>

<section class="warn">
  <h2>알아두세요</h2>
  <ul class="tips">{tips}</ul>
</section>

<section>
  <h2>자주 묻는 질문</h2>
  {faq}
</section>

<section>
  <h2>함께 보면 좋은 가이드</h2>
  {guide_list(up, RELATED.get(c['slug'], DEFAULT_RELATED))}
</section>
{affiliate_block()}
<p class="small muted">참고한 공식 안내: {sources} (최종 확인 {VERIFIED})<br>
틀린 정보를 발견하면 <a href="{up}contact/">제보해 주세요</a>.</p>
{f'<p class="small muted">{e(region_label)} 다른 나라: {others}</p>' if others else ''}
"""
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    desc = (f"{c['name']} {c['form_short']} 공식 사이트와 작성법. "
            + ("공식 사이트에서 무료. " if free else "")
            + f"{c['window_text']} 신청. 신청 순서, 준비물, 가짜 유료 사이트 주의사항.")
    return page(f"{c['slug']}/", f"{c['name']} 입국신고 {c['form_short']} 작성법 {VERIFIED[:4]} | 입국노트", desc, body, ld)


def build_compare_body(up):
    return f"""
<p>온라인 입국신고가 있는 {len(COUNTRIES)}개 나라의 의무 여부, 신청 시점, 공식 주소를 모았어요. 공식 주소가 아닌 곳에서 결제를 요구하면 대행 사이트예요.</p>
{compare_table(up)}
<p class="small muted">시각 기준(72시간)과 날짜 기준(3일)의 차이는 <a href="{up}guide/timing/">이 글</a>에 정리했어요. 의무가 '선택'이나 '권장'인 나라는 종이 신고서로도 입국할 수 있지만, 미리 하면 줄이 짧아져요.</p>
"""


def build_guide(g):
    up = "../../"
    body_html = g["body"]
    if body_html == "__COMPARE__":
        body_html = build_compare_body(up)
    body_html = body_html.replace("{up}", up)
    more = guide_list(up, [x["slug"] for x in GUIDES if x is not g])
    body = f"""
<p class="crumb"><a href="{up}">입국노트</a> › <a href="{up}guide/">가이드</a></p>
<article class="article">
<h1>{e(g['title'])}</h1>
<p class="small muted">최종 확인 {VERIFIED}</p>
{body_html}
</article>
<section>
  <h2>다른 가이드</h2>
  {more}
</section>
{affiliate_block()}
"""
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
          "dateModified": VERIFIED, "author": {"@type": "Organization", "name": SITE}}
    return page(f"guide/{g['slug']}/", f"{g['title']} | 입국노트", g["desc"], body, ld)


def build_guide_index():
    up = "../"
    items = "".join(
        f"""<a class="card country" href="{g['slug']}/"><h3>{e(g['title'])}</h3><p>{e(g['desc'])}</p></a>"""
        for g in GUIDES)
    body = f"""
<p class="crumb"><a href="{up}">입국노트</a> › 가이드</p>
<h1>입국신고 가이드</h1>
<p class="lead">자주 헷갈리는 상황별로 정리했어요.</p>
<section class="stack">{items}</section>
"""
    return page("guide/", "해외 입국신고 가이드 모음 | 입국노트", "가짜 사이트 구별, 신청 시점, 가족 여행, 여러 나라 여행 등 해외 입국신고 상황별 가이드.", body)


def build_about():
    up = "../"
    body = f"""
<p class="crumb"><a href="{up}">입국노트</a> › 운영 원칙</p>
<h1>운영 원칙과 개인정보</h1>
<section class="card">
  <h2>입국노트가 하는 일</h2>
  <ul class="tips">
    <li>전 세계 전자 입국신고 공식 정보를 한국어로 정리합니다.</li>
    <li>신고는 항상 각국 정부 공식 사이트로 연결합니다.</li>
    <li>정보는 매월 공식 사이트 기준으로 다시 확인하며, 마지막 확인일을 표시합니다. (최종 확인 {VERIFIED})</li>
  </ul>
</section>
<section class="card">
  <h2>입국노트가 하지 않는 일</h2>
  <ul class="tips">
    <li>입국신고·비자 신청을 대행하지 않습니다.</li>
    <li>여권번호 등 개인정보를 받지 않습니다. 회원가입이나 입력 저장 기능이 없습니다.</li>
    <li>입국신고와 관련해 어떤 요금도 받지 않습니다.</li>
  </ul>
</section>
<section class="card">
  <h2>개인정보 처리</h2>
  <p>계산기에 넣는 날짜와 시각은 이용자 기기 안에서만 계산되며 서버로 전송되지 않습니다. 체크리스트 체크 상태는 이용자 브라우저(localStorage)에만 저장되고, 브라우저 데이터를 지우면 함께 삭제됩니다.</p>
  <p>제보는 구글 설문지(Google Forms)로 받아요. 적은 내용(선택 입력한 이메일 포함)은 답변과 정보 수정에만 쓰고, 처리 후 1년 안에 삭제합니다. 여권번호 같은 개인정보는 적지 마세요.</p>
  <p style="margin-bottom:0">방문 통계 도구나 제휴 링크 제공사가 쿠키를 사용할 수 있으며, 이 경우 해당 내용을 이 페이지에 추가로 안내합니다.</p>
</section>
<section class="card">
  <h2>제휴 링크 고지</h2>
  <p style="margin-bottom:0">일부 페이지의 eSIM·보험·환전 등 링크는 제휴 링크입니다. 이를 통해 구매하면 입국노트가 수수료를 받을 수 있으며, 이용자가 내는 가격은 달라지지 않습니다.</p>
</section>
<section class="card">
  <h2>정보 오류 제보</h2>
  <p style="margin-bottom:0">바뀐 제도나 잘못된 정보를 발견하면 <a href="{up}contact/">제보 양식</a>으로 알려주세요.</p>
</section>
"""
    return page("about/", "운영 원칙·개인정보 | 입국노트", "입국노트는 입국신고를 대행하지 않고 개인정보를 받지 않는 무료 안내 사이트입니다.", body)


def build_contact():
    up = "../"
    body = f"""
<p class="crumb"><a href="{up}">입국노트</a> › 제보·문의</p>
<h1>정보 오류 제보·문의</h1>
<p class="lead">바뀐 제도, 틀린 정보, 추가했으면 하는 나라를 알려주세요.</p>
<section class="card">
  <div class="panel-head"><h2>제보 양식</h2></div>
  <p>종류(정보 오류 제보·나라 추가 요청·제휴 문의·기타)와 내용을 적어 주세요. 답장을 원하면 이메일도 남겨 주세요(선택).</p>
  <p class="small muted">여권번호 등 개인정보는 적지 마세요. 입국신고 대행 요청은 받지 않아요. 제보는 구글 설문지로 받아요.</p>
  <a class="btn btn-primary" href="{FORM_URL}" target="_blank" rel="noopener">제보 양식 열기 →</a>
</section>
"""
    return page("contact/", "정보 오류 제보·문의 | 입국노트", "입국노트 정보 오류 제보와 문의.", body)


def build_thanks():
    body = """<h1>보내주셔서 고맙습니다</h1><p class="lead">확인 후 정보를 고치거나 답장드릴게요.</p>
<p><a class="btn btn-primary" href="../../">처음으로</a></p>"""
    return page("contact/thanks/", "접수 완료 | 입국노트", "제보 접수 완료", body, index=False)


def build_sitemap():
    urls = "".join(f"<url><loc>{SITE_URL}/{p}</loc><lastmod>{VERIFIED}</lastmod></url>" for p in PAGES)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


if __name__ == "__main__":
    write("index.html", build_index())
    for c in COUNTRIES:
        write(f"{c['slug']}/index.html", build_country(c))
    write("guide/index.html", build_guide_index())
    for g in GUIDES:
        write(f"guide/{g['slug']}/index.html", build_guide(g))
    write("about/index.html", build_about())
    write("contact/index.html", build_contact())
    nf = page("404/", "페이지를 찾을 수 없어요 | 입국노트", "입국노트",
              '<h1>페이지를 찾을 수 없어요</h1><p><a class="btn btn-primary" href="/">처음으로 돌아가기</a></p>', index=False)
    write("404.html", nf.replace('"../', '"' + BASE).replace('href="/"', 'href="' + BASE + '"'))
    for old in REMOVED:
        write(f"{old}/index.html", f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={BASE}"><link rel="canonical" href="{SITE_URL}/"><title>입국노트</title></head>
<body><p>공식 자료가 확인되지 않아 안내를 내렸어요. <a href="{BASE}">처음으로</a></p></body></html>''')
    write("sitemap.xml", build_sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
