# 입국노트 — AI Studio 제작용 통합 파일

# 입국노트 — 해외 전자 입국신고 안내 웹사이트 제작 요청

첨부 파일 4개(countries.json, guides.json, fields.json, calc.ts)를 사용해서 아래 사양의 웹사이트를 만들어 주세요.
**디자인은 자유롭게 제안해 주세요.** 단, 아래의 "반드시 지킬 것"은 내용과 신뢰에 관한 규칙이라 바꾸면 안 됩니다.

---

## 1. 사이트 개요

- 이름: **입국노트** (영문 slug: ipguknote)
- 한 줄 설명: 해외 전자 입국신고를 정부 공식 사이트에서 **직접** 하도록 돕는 한국어 안내 사이트
- 대상: 해외여행 가는 한국인 (모바일 사용자가 대부분 → **모바일 우선**)
- 성격: 정보 안내 + 신청 시점 계산기. **대행 서비스가 아님.** 개인정보를 받지 않음.
- 수익: 나중에 제휴 링크(eSIM·여행자보험·환전·공항픽업)를 붙일 예정. 지금은 자리만 만들고 링크가 비어 있으면 숨김.
- 언어: 한국어. 본문은 해요체로 통일(하단·운영원칙·고정 안내 띠만 합니다체), 짧고 쉬운 문장.

## 2. 반드시 지킬 것 (신뢰·법적 리스크 관련)

1. **모든 페이지 맨 위에 고정 안내 띠**: "입국노트는 정부 사이트가 아니며 신고를 대행하지 않습니다. 입국신고는 각국 공식 사이트에서 직접 하세요. 대부분 무료입니다."
2. **정부 사이트처럼 보이지 않게**: 국가 문장(紋章), 정부 로고, 국기를 브랜드처럼 쓰는 디자인 금지. 국기 이모지는 나라 구분용으로만 사용.
3. **결제·입력 폼 금지**: 여권번호 등 개인정보를 받는 입력창, 결제 기능을 만들지 않음. (계산기의 날짜·시각 입력만 허용, 서버로 보내지 않음)
4. **공식 사이트 버튼이 가장 눈에 띄게**: 나라 페이지의 핵심 행동은 "공식 사이트에서 신청하기" 버튼. 외부 링크는 새 탭(`target="_blank" rel="noopener"`).
5. **데이터를 지어내지 말 것**: 나라 정보는 countries.json 내용만 사용. 없는 나라·없는 정보를 추가하지 않음.
6. **요금 표시 규칙** (현재 15개국은 모두 무료): `fee`가 정확히 "무료"면 "무료"로 표시. 그 외에는 "공식 요금 있음" 배지를 달고 `fee` 문장을 그대로 보여줌.
7. **확인도 낮은 나라**: `confidence`가 "low"인 나라 페이지에는 경고 박스 표시 — "이 나라는 제도가 막 바뀌었거나 공식 안내가 엇갈립니다. 출발 전 항공사나 해당국 대사관 안내를 꼭 함께 확인하세요."
8. **계산 로직은 calc.ts를 그대로 사용** (시간대·날짜 기준 계산이 이미 검증됨). 디자인만 입히세요.
9. 제휴 링크에는 `rel="sponsored noopener"`와 "제휴 링크입니다. 입국노트는 수수료를 받을 수 있지만 입국신고 자체로는 어떤 돈도 받지 않습니다." 문구.
10. 모든 나라 페이지 하단에 `sources`(참고한 공식 안내 링크)와 "최종 확인 {verified}" 날짜 표시.

## 3. 데이터 설명

### countries.json
```
{ "verified": "2026-10-05",
  "regions": [{ "key": "east-asia", "label": "동북아시아" }, ...],   // 표시 순서 그대로
  "countries": [ { ...40개국... } ] }                                 // 배열 순서 = 표시 순서
```
나라 객체 필드:

| 필드 | 뜻 / 사용처 |
|---|---|
| slug | URL 경로 (예: /japan) |
| name, flag | 나라 이름, 국기 이모지 |
| region | regions의 key — 지역별 묶음에 사용 |
| form / form_short | 신고서 정식 이름 / 짧은 이름 (카드 제목: "일본 · Visit Japan Web") |
| url, domain | 공식 신청 주소 / 표시용 도메인 (도메인은 고정폭 글꼴로 크게 보여 사칭 사이트와 비교하게) |
| mandatory | "의무", "의무 (일부 공항)", "권장", "선택" — 배지로 표시 (의무 계열은 강조색, 나머지는 회색) |
| fee | 요금 (위 2-6 규칙) |
| window | 신청 가능 시점 규칙 (calc.ts가 사용) |
| window_text | 신청 시점 설명 문장 (카드·요약에 표시) |
| deadline (일부만) | 신청 마감 규칙 (러시아·카보베르데·콜롬비아) |
| iana, tz_label | 계산기 시간대 / "베트남 시간 기준 (한국보다 2시간 느림)" 같은 설명 |
| result | 제출 후 받는 것(QR 등)과 사용법 |
| status | 시행 시기·적용 공항 등 현황 |
| needs | 필요한 정보 목록 → 체크리스트 |
| steps | 신청 순서 → 번호 목록 |
| tips | 주의사항 → 경고 박스 |
| faq | [[질문, 답], ...] → 아코디언 + FAQPage 구조화 데이터 |
| sources | [[이름, URL], ...] → 하단 출처 |
| confidence | "high"/"medium"/"low" — low만 경고 박스 (2-7) |
| official_basis (일부만) | 정부 도메인이 아닌 공식 주소의 근거 문장 → 공식 사이트 카드 안에 "공식 주소 근거:" 박스로 표시 |

### guides.json
상황별 가이드 글 6개. `body`는 HTML 조각(h2, p, ul.tips, ol.steps 등)이니 그대로 렌더링하고 스타일만 입히세요.
`special: "compare-table"`인 글(compare)은 body 대신 **전체 나라 비교표**(지역별 그룹 행 + 나라/신고서, 의무 여부, 신청 시점, 공식 도메인)를 보여주세요.

### calc.ts
`calc()`, `status()`, `needsCalculator()`, `fmt()`, `ics()` 함수. 파일 맨 아래 검증 예시와 결과가 같아야 합니다.

## 4. 페이지 구성

### ① 메인 (/)
1. 제목: "해외 전자 입국신고, 공식 사이트에서 직접 하세요" + 설명 ("한국인이 많이 가는 나라 중 온라인 입국신고가 있는 15곳…")
2. **신청 시점 계산기** (나라 선택 드롭다운은 지역별 optgroup)
3. **나라 검색창** (이름·신고서 이름·slug로 즉시 필터, 결과 없는 지역은 숨김)
4. **지역별 나라 카드 목록** — 카드: 국기, "나라 · 신고서 짧은이름", window_text, mandatory 배지, (유료면) "공식 요금 있음" 배지
5. 안내 문구: "여기 없는 나라는 2026년 10월 기준 공식 온라인 입국신고가 없거나(종이 카드 또는 신고 없음), 돈을 내는 전자여행허가(ETA)·비자만 있는 곳입니다."
6. 가짜 사이트 경고 박스 ("결제부터 요구하면 의심하세요" + 가이드 링크)
7. 가이드 목록
8. 제휴 영역 (링크 있을 때만)

### ② 나라 페이지 (/{slug}) — 40개
1. 경로 표시: 입국노트 › 지역 › 나라
2. 제목: "{flag} {name} {form_short} 작성법" + 요약 (form, 무료 여부, window_text)
3. 요약 카드 3개: 비용 / 의무 여부 / 신청 시점
4. (confidence low면) 경고 박스
5. **공식 사이트 카드** — domain 크게, 큰 버튼 "공식 사이트에서 신청하기 (무료)", status 문장, 유료면 요금 안내
6. **계산기** (needsCalculator가 true일 때만) — 입력칸 이름은 window.ref에 따라 "도착 날짜 (현지)" 또는 "출발 날짜 (출발 공항 현지)"
7. 신청 순서 (steps) + result
8. 준비물 체크리스트: needs + ["여권 유효기간 6개월 이상 남았는지 확인", "왕복(또는 출국) 항공권 예약 확인서", "숙소 주소를 영문으로 메모", "공식 사이트에서 {form_short} 제출", "받은 QR·확인 메일 캡처해 두기"]. 체크 상태는 localStorage(나라별 키)에 저장, "3 / 9" 같은 진행 표시. localStorage 접근은 try/catch.
9. 알아두세요 (tips)
10. 자주 묻는 질문 (faq 아코디언)
11. 관련 가이드 3개 (기본: fake-sites, timing, family / 필리핀은 philippines-red-qr 우선)
12. 제휴 영역 (링크 있을 때만)
13. 출처 + 최종 확인일 + "틀린 정보 제보" 링크
14. 같은 지역 다른 나라 링크

### ③ 가이드 목록 (/guide) 과 가이드 글 (/guide/{slug}) — 6개
제목, "최종 확인 {verified}", 본문, 다른 가이드 목록.

### ④ 운영 원칙·개인정보 (/about)
- 하는 일: 전 세계 전자 입국신고 공식 정보를 한국어로 정리 / 신고는 항상 공식 사이트로 연결 / 매월 공식 사이트 기준으로 재확인, 마지막 확인일 표시
- 하지 않는 일: 신고·비자 대행 안 함 / 여권번호 등 개인정보 안 받음, 회원가입 없음 / 입국신고 관련 요금 안 받음
- 개인정보: 계산기 입력은 기기 안에서만 계산, 체크리스트는 브라우저(localStorage)에만 저장. 제보 양식 내용은 답변·수정에만 쓰고 처리 후 1년 안에 삭제
- 제휴 링크 고지

### ⑤ 제보·문의 (/contact)
종류(정보 오류 제보 / 나라 추가 요청 / 제휴·광고 문의 / 기타), 내용(필수), 답장 이메일(선택).
"여권번호 등 개인정보는 적지 마세요. 입국신고 대행 요청은 받지 않습니다." 문구.
(Netlify에 배포할 예정이라 `<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">` 형태로 만들어 주면 좋음. 어렵다면 mailto 없이 양식 UI만.)

### 공통 하단(footer)
- "입국노트는 해외 전자 입국신고를 직접 할 수 있도록 공식 정보를 정리한 안내 사이트입니다. 어떤 정부 기관과도 관련이 없으며 신고 대행이나 개인정보 수집을 하지 않습니다."
- "정보 최종 확인: {verified}. 제도는 예고 없이 바뀔 수 있으니 출발 전 공식 사이트에서 한 번 더 확인하세요."
- 제휴 고지 한 줄, 운영 원칙·제보·가이드 링크

## 5. 계산기 화면 동작

- 입력: 날짜, 시각(기본 12:00). 입력 즉시 결과 갱신.
- 결과 상태 배지 (status 함수):
  - waiting → "N일 N시간 뒤부터 신청 가능" (주황)
  - open → "지금 바로 신청할 수 있어요" (초록)
  - closed → "신청 마감 시각이 지났어요" (빨강)
  - passed → "도착(또는 출발) 시각이 이미 지났어요" (회색)
- 결과 표:
  - 도착 기준(iana 있음): 신청 시작 (현지) / **신청 시작 (한국 시간)** 강조 / (마감 있으면) 신청 마감 (한국 시간) / 도착 (현지)
  - 출발 기준: 신청 시작 / (마감) / 출발 — 아래 "출발 공항 현지 시각 기준이에요. 한국에서 출발하면 한국 시간 그대로 보면 돼요."
  - 도착 기준 아래에는 "{tz_label}으로 계산했어요."
- 버튼: "시작 알림 추가"(open 시각으로 .ics 다운로드) 또는 마감만 있으면 "마감 알림 추가"(마감 6시간 전) + "공식 사이트 열기"
- 메인 계산기에서 anytime 나라를 고르면 입력칸을 숨기고 "출발 전 언제든 작성할 수 있어요. 신청 시작 시각을 기다릴 필요가 없어요." 표시

## 6. 기술·SEO 요구

- 결과물은 **정적 사이트로 빌드되어 Netlify에 올릴 수 있어야** 함 (서버·DB 없음). React/Vite 등 사용 가능.
- 각 페이지가 **개별 URL**을 가지고 새로고침해도 열려야 함 (SPA라면 Netlify `_redirects`에 `/* /index.html 200` 포함). 가능하면 페이지별 정적 HTML 생성(검색 노출에 유리).
- 페이지별 `<title>`, meta description, canonical(`https://ipguknote.netlify.app/...`), Open Graph 태그.
  - 메인 title: "해외 전자 입국신고 총정리 15개국 — 일본·동남아·괌·미주 | 입국노트"
  - 나라 title: "{name} 입국신고 {form_short} 작성법 2026 | 입국노트"
  - 나라 description: "{name} {form_short} 공식 사이트와 작성법. (무료면 '공식 사이트에서 무료.') {window_text} 신청. 신청 순서, 준비물, 가짜 유료 사이트 주의사항."
- 나라 페이지에 FAQPage, 가이드에 Article, 메인에 WebSite JSON-LD.
- sitemap.xml, robots.txt 생성.
- 다크 모드 대응, 글자 크기 16px 이상, 터치 영역 44px 이상, 가로 스크롤 없음(표는 내부 스크롤).
- 외부 폰트·라이브러리는 최소화 (Pretendard 정도는 OK).

## 6-2. fields.json (항목별 번역표, 10개국 — 필드에 ko_ui(한국어 화면 표시)가 있으면 표에 "한국어 화면 표시" 열을 추가)
`{slug: {korean_ui, korean_ui_note, sections:[{title, fields:[{label, ko, how, required}]}], pitfalls, sources, confidence}}`
해당 나라 페이지의 체크리스트 위에 "항목별 번역표" 섹션으로 표시: korean_ui_note 강조 → 섹션별 접기(details) → 표(화면 영문 항목 | 뜻 | 이렇게 적어요, required면 '필수' 배지) → pitfalls 경고 박스 → 참고 자료. confidence가 high가 아니면 "일부 항목은 여행 가이드를 함께 참고해 실제 화면 표현이 조금 다를 수 있어요" 표시. 메인 목록에서 번역표가 있는 나라에 '번역표' 배지.

## 7. 디자인 방향 (참고용 — 자유롭게 제안)

- 컨셉: **공항 출도착 전광판(스플릿 플랩 보드)**. 검정 배경 #07090c, 노란 글자 #ffcc1f, 상태색(의무=초록 REQUIRED, 권장=주황 ADVISED, 선택=회색 OPTIONAL, 요금=빨강 FEE).
- 글꼴: Nanum Gothic Coding(전광판 한글), Share Tech Mono(숫자·코드), IBM Plex Sans KR(긴 본문).
- 나라 목록 = 전광판 표(공항코드 | 목적지 | 신고서 | 신청 시점 | 상태), 나라 페이지 상단 = 운항 정보판, 상단에 서울 시각 시계, 로고 글자는 플랩 타일이 넘어가는 애니메이션. 관공서 느낌은 피함.
- 로고: "입국노트" 글자 + 체크 표시가 있는 문서 아이콘.

## 첨부: calc.ts
```
// 입국노트 신청 시점 계산 로직 (기존 사이트에서 검증된 로직 — 디자인과 무관하게 이 로직을 그대로 사용)
// countries.json 의 각 나라: window {type: "hours"|"days"|"anytime", ref: "arrival"|"departure", value}
//                         deadline? {type, value, ref, text}, iana (도착 기준일 때 현지 시간대)

export type Rule = { type: "hours" | "days" | "anytime"; ref: "arrival" | "departure"; value: number | null };
export type Country = {
  slug: string; name: string; url: string; iana?: string | null; tz_label: string;
  window: Rule; deadline?: Rule & { text: string };
};

const HOUR = 3600000;

// 특정 시간대의 UTC 대비 오프셋(ms)
function tzOffset(ms: number, tz: string): number {
  const f = new Intl.DateTimeFormat("en-US", {
    timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit",
  });
  const p: Record<string, string> = {};
  f.formatToParts(new Date(ms)).forEach((x) => (p[x.type] = x.value));
  return Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute, +p.second) - Math.floor(ms / 1000) * 1000;
}

// 현지 벽시계 시각 → UTC ms
function zoned(y: number, mo: number, d: number, h: number, mi: number, tz: string): number {
  const guess = Date.UTC(y, mo, d, h, mi);
  const u = guess - tzOffset(guess, tz);
  return guess - tzOffset(u, tz);
}

// 기준 시각: 도착 기준이면 그 나라 시간대, 출발 기준이면 사용자 기기 시간대(보통 한국)
function baseTime(c: Country, p: number[], t: number[]): number {
  if (c.window.ref === "arrival" && c.iana) return zoned(p[0], p[1] - 1, p[2], t[0], t[1], c.iana);
  return new Date(p[0], p[1] - 1, p[2], t[0], t[1]).getTime();
}

function shift(c: Country, rule: Rule, p: number[], b: number): number | null {
  if (rule.type === "hours") return b - (rule.value ?? 0) * HOUR;
  if (rule.type === "days") {
    if (rule.ref === "arrival" && c.iana) {
      // "도착일 포함 N일": 확실히 접수되는 날짜 = 도착일 0시에서 (N-1)일 전
      return zoned(p[0], p[1] - 1, p[2] - ((rule.value ?? 1) - 1), 0, 0, c.iana);
    }
    return b - (rule.value ?? 0) * 24 * HOUR;
  }
  return null; // anytime
}

export type CalcResult = { base: number; open: number | null; deadline: number | null };

/** dateStr "2026-12-10", timeStr "09:30" (사용자가 입력한 도착/출발 현지 날짜·시각) */
export function calc(c: Country, dateStr: string, timeStr = "12:00"): CalcResult {
  const p = dateStr.split("-").map(Number);
  const t = timeStr.split(":").map(Number);
  const b = baseTime(c, p, t);
  const open = c.window.type === "anytime" ? null : shift(c, c.window, p, b);
  let deadline: number | null = null;
  if (c.deadline && c.deadline.ref === c.window.ref) deadline = shift(c, c.deadline, p, b);
  return { base: b, open, deadline };
}

/** 계산기를 보여줄지: anytime 이면서 마감도 없으면 계산기 대신 "출발 전 언제든 가능" 안내 */
export const needsCalculator = (c: Country) => !(c.window.type === "anytime" && !c.deadline);

/** 상태 판정 */
export function status(r: CalcResult, now = Date.now()) {
  if (now >= r.base) return "passed";          // 도착/출발 시각 지남
  if (r.deadline !== null && now > r.deadline) return "closed"; // 마감 지남
  if (r.open === null || now >= r.open) return "open";         // 지금 신청 가능
  return "waiting";                                            // r.open - now 뒤부터 가능
}

/** 표시용: 도착 기준이면 현지시각 + 한국시각 둘 다, 출발 기준이면 기기 시각만 */
export function fmt(ms: number, tz?: string) {
  return new Intl.DateTimeFormat("ko-KR", {
    month: "long", day: "numeric", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23",
    ...(tz ? { timeZone: tz } : {}),
  }).format(new Date(ms));
}

/** 캘린더 알림(.ics) 문자열 — 신청 시작 시각(또는 마감 6시간 전)에 울림 */
export function ics(c: Country, ms: number, label: string) {
  const d = (x: number) => new Date(x).toISOString().replace(/[-:]/g, "").slice(0, 15) + "Z";
  return [
    "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ipguknote//KO",
    "BEGIN:VEVENT", `UID:${c.slug}-${ms}@ipguknote`, `DTSTAMP:${d(Date.now())}`,
    `DTSTART:${d(ms)}`, `DTEND:${d(ms + 1800000)}`,
    `SUMMARY:${c.name} 입국신고 ${label}`, `DESCRIPTION:공식 사이트에서 직접 신청하세요: ${c.url}`, `URL:${c.url}`,
    "BEGIN:VALARM", "TRIGGER:PT0M", "ACTION:DISPLAY", `DESCRIPTION:${c.name} 입국신고 ${label}`, "END:VALARM",
    "END:VEVENT", "END:VCALENDAR",
  ].join("\r\n");
}

// 검증용 예시 (한국 기기 기준):
// 베트남, 도착 2026-12-10 09:30 → 신청 시작 현지 12월 7일 09:30 / 한국 12월 7일 11:30
// 싱가포르, 도착 2026-12-10 09:30 → 신청 시작 현지 12월 8일 00:00 (도착일 포함 3일)
// 아루바(출발 기준 7일), 출발 2026-12-10 09:30 → 신청 시작 12월 3일 09:30
// 러시아, 도착 2026-12-10 09:30 → 신청 시작 9월 11일경, 마감 한국시각 12월 7일 08:30
```

## 첨부: guides.json
```
[
 {
  "slug": "fake-sites",
  "title": "가짜 입국신고 사이트 구별법 — 결제창이 나오면 멈추세요",
  "short": "가짜 유료 사이트 구별법",
  "desc": "Visit Japan Web, 베트남·태국 입국신고, 괌 EDF 등 전자 입국신고는 대부분 무료예요. 공식처럼 보이는 유료 대행 사이트를 구별하는 5가지 방법.",
  "body": "\n<p>전자 입국신고는 <strong>정부 공식 사이트에서 무료</strong>예요. 입국노트에 실린 나라는 모두 신청 요금이 없어요. 그런데 검색하면 공식처럼 생긴 유료 대행 사이트가 먼저 나오는 경우가 많아요.</p>\n\n<h2>각국 정부도 공식 경고했어요</h2>\n<ul class=\"tips\">\n  <li><strong>태국:</strong> 이민국이 \"돈을 받는 가짜 TDAC 사이트\"를 공식 경고했어요.</li>\n  <li><strong>말레이시아:</strong> 가짜 MDAC 사이트가 최대 80달러를 받은 사례가 보고됐어요.</li>\n  <li><strong>싱가포르:</strong> ICA는 수수료를 받는 제3자 상업 서비스가 ICA와 무관하다고 안내해요.</li>\n  <li><strong>베트남:</strong> 공안부가 공식 입국신고 시스템을 사칭하는 사이트를 주의하라고 경고했어요.</li>\n  <li><strong>한국:</strong> 2026년 3월 중국에서 \"한국 입국신고 11만 원 대행\" 사이트가 퍼져 주중대사관이 수사를 요청했어요.</li>\n</ul>\n\n<h2>5초 구별법</h2>\n<ol class=\"steps\">\n  <li><strong>주소를 보세요.</strong> 공식 주소는 대부분 .gov / .go / .gob / .govt 같은 정부 도메인이에요. 정부 도메인이 아닌 공식 사이트(괌·팔라우 등)도 있어요. 이런 나라는 입국노트 나라별 페이지에 \"공식 주소 근거\"를 적어 두었으니, 주소가 한 글자도 다르지 않은지 비교하세요.</li>\n  <li><strong>카드 결제창이 나오면 멈추세요.</strong> 입국노트에 실린 나라의 공식 입국신고에는 결제 단계가 없어요.</li>\n  <li><strong>\"처리 속도 선택\", \"승인률 99%\" 같은 문구를 의심하세요.</strong> 입국신고는 심사가 아니라 신고라서 이런 문구가 필요 없어요.</li>\n  <li><strong>사이트 맨 아래를 보세요.</strong> \"민간 대행 업체\", \"정부와 무관\" 같은 문구가 작게 적혀 있으면 대행 사이트예요.</li>\n  <li><strong>검색 결과 맨 위 광고를 조심하세요.</strong> '광고' 표시가 붙은 링크는 공식 사이트가 아닐 가능성이 높아요.</li>\n</ol>\n\n<h2>이미 결제했다면</h2>\n<ul class=\"tips\">\n  <li>대행 사이트에서 실제로 신고가 됐는지 알 수 없다면, <strong>공식 사이트에서 직접 다시 제출</strong>하는 것이 안전해요.</li>\n  <li>결제를 취소하고 싶다면 사이트의 환불 정책을 확인한 뒤 카드사 고객센터에 문의하세요.</li>\n</ul>\n<p><a class=\"btn btn-primary\" href=\"/guide/compare/\">나라별 공식 주소 표 보기</a></p>\n"
 },
 {
  "slug": "compare",
  "title": "나라별 전자 입국신고 한눈에 비교 (의무 여부·신청 시점·공식 주소)",
  "short": "나라별 한눈에 비교",
  "desc": "일본 Visit Japan Web부터 베트남·태국·괌·뉴질랜드·캐나다까지, 전자 입국신고가 있는 나라의 의무 여부와 신청 시점, 공식 주소를 한 표로 비교해요.",
  "body": "",
  "special": "compare-table"
 },
 {
  "slug": "timing",
  "title": "입국신고 '72시간 전'과 '3일 전'은 뭐가 다를까?",
  "short": "72시간 vs 3일 차이",
  "desc": "베트남·태국·필리핀은 도착 72시간 전, 말레이시아·싱가포르는 날짜 기준 3일. 신청 시작 시점을 헷갈리지 않는 법.",
  "body": "\n<p>나라마다 \"도착 72시간 전부터\"와 \"도착 3일 전부터\"라고 안내하는데, 둘은 계산 방식이 달라요.</p>\n\n<h2>시각 기준: 72시간 (베트남·태국·필리핀)</h2>\n<p>도착 예정 <strong>시각</strong>에서 정확히 72시간을 거꾸로 세요. 10월 10일 오전 9시 30분(현지) 도착이면 <strong>10월 7일 오전 9시 30분(현지)</strong>부터 신청할 수 있어요.</p>\n<p>한국과의 시차도 생각해야 해요. 베트남·태국은 한국보다 2시간 느려서, 위 예시는 한국 시간으로 10월 7일 오전 11시 30분이에요.</p>\n\n<h2>날짜 기준: 3일 (싱가포르, 말레이시아)</h2>\n<p>싱가포르는 <strong>도착일을 포함해 3일</strong>이에요. ICA 공식 예시: \"6월 30일 도착이면 6월 28일부터 제출 가능\".</p>\n<p>말레이시아도 \"도착 3일 전 이내\"로 안내해요. 입국노트 계산기는 싱가포르와 같은 방식(도착일 포함 3일)으로, 확실히 접수되는 날짜를 보여줘요.</p>\n\n<h2>가장 쉬운 방법</h2>\n<p>각 나라 페이지의 계산기에 도착 날짜와 시각만 넣으세요. 신청 시작 시각을 한국 시간으로 보여주고, <strong>캘린더 알림</strong>도 만들어 줘요.</p>\n"
 },
 {
  "slug": "philippines-red-qr",
  "title": "필리핀 eTravel QR코드가 빨간색으로 나왔을 때",
  "short": "eTravel QR 빨간색 해결",
  "desc": "필리핀 eTravel 등록 후 QR코드가 빨간색이면 정보가 불완전하거나 건강 관련 확인이 필요하다는 뜻이에요. 원인과 대처법.",
  "body": "\n<p>필리핀 eTravel은 등록을 마치면 QR코드를 줘요. 색깔에 따라 의미가 달라요.</p>\n\n<h2>초록색 vs 빨간색</h2>\n<ul class=\"tips\">\n  <li><strong>초록색:</strong> 입력 정보가 올바르고 완전하다는 뜻이에요. 바로 입국심사로 갈 수 있어요.</li>\n  <li><strong>빨간색:</strong> 정보가 불완전하거나 틀렸을 때, 또는 최근 질병이나 감염 노출 이력이 신고됐을 때 나와요.</li>\n</ul>\n\n<h2>빨간색이 나왔다면</h2>\n<ol class=\"steps\">\n  <li>공식 사이트 <a href=\"https://etravel.gov.ph/\" target=\"_blank\" rel=\"noopener\">etravel.gov.ph</a>에서 입력 내용을 다시 확인해요.</li>\n  <li>여권번호, 항공편명, 날짜, 숙소 주소에 오타가 없는지 봐요.</li>\n  <li>수정(업데이트)한 뒤 새 QR을 저장해요. 등록과 수정 모두 무료예요.</li>\n  <li>건강 신고 때문이라면 공항 검역 안내에 따라요.</li>\n</ol>\n\n<h2>잊지 마세요</h2>\n<ul class=\"tips\">\n  <li>QR코드는 <strong>비행기 탑승 전 항공사 직원</strong>이 먼저 확인해요. 공항 가기 전에 캡처해 두세요.</li>\n  <li>등록은 도착 72시간 전부터 가능해요.</li>\n</ul>\n<p><a class=\"btn btn-primary\" href=\"/philippines/\">필리핀 eTravel 전체 안내</a></p>\n"
 },
 {
  "slug": "family",
  "title": "가족·단체 여행 입국신고, 한 명이 다 해도 될까?",
  "short": "가족·단체 여행 입국신고",
  "desc": "아이를 포함한 동행자 모두 입국신고 대상이에요. 싱가포르는 공식 그룹 제출 기능이 있고, 다른 나라는 공식 사이트 화면에서 동행자 추가 여부를 확인하세요.",
  "body": "\n<p>가족 여행에서 가장 많이 헷갈리는 부분은 \"아이도 해야 하나?\", \"한 사람이 다 해도 되나?\"이에요.</p>\n\n<h2>아이도 대상이에요</h2>\n<p>각국 공식 안내는 국적 기준으로 \"외국인 입국자\"를 대상으로 해요. 나이 예외가 따로 안내돼 있지 않다면 <strong>아이와 아기도 각자의 여권 정보로 신고</strong>해야 해요.</p>\n\n<h2>한 명이 대신 입력할 수 있나요?</h2>\n<ul class=\"tips\">\n  <li><strong>싱가포르:</strong> 공식 '그룹 제출(Group Submission)' 기능이 있어요. 같은 일정으로 함께 여행하는 일행을 한 사람이 한 번에 제출할 수 있어요.</li>\n  <li><strong>베트남·태국·필리핀·말레이시아:</strong> 동행자 추가 화면이 있는지 공식 사이트에서 확인하세요. 없으면 한 명씩 따로 제출하면 돼요. 대표자가 가족 것을 대신 입력하는 것 자체는 문제가 없어요.</li>\n</ul>\n\n<h2>미리 준비하면 빨라요</h2>\n<ol class=\"steps\">\n  <li>가족 모두의 여권 사진면을 휴대폰에 찍어 둬요.</li>\n  <li>항공편명과 숙소 영문 주소를 메모장에 한 번만 적어 두고 복사해서 써요.</li>\n  <li>받은 QR·확인 메일은 사람별로 이름을 붙여 저장해요.</li>\n</ol>\n<p class=\"small muted\">허위 신고는 처벌 대상이 될 수 있어요(싱가포르 ICA 안내). 각자의 정보를 정확히 입력하세요.</p>\n"
 },
 {
  "slug": "multi-country",
  "title": "동남아 여러 나라를 이어서 여행할 때 입국신고 순서",
  "short": "여러 나라 이어서 여행할 때",
  "desc": "방콕→싱가포르→쿠알라룸푸르처럼 여러 나라를 도는 여행이라면, 나라마다 그 나라 도착 시각 기준으로 따로 신고해야 해요.",
  "body": "\n<p>방콕 → 싱가포르 → 쿠알라룸푸르처럼 여러 나라를 이어서 가는 일정이라면, 출발 전에 한꺼번에 신고할 수 없는 경우가 많아요.</p>\n\n<h2>핵심: 나라마다 '그 나라 도착 시각' 기준</h2>\n<p>신청 가능 시점은 한국 출발일이 아니라 <strong>그 나라에 도착하는 시각</strong>을 기준으로 계산해요. 예를 들어 10일 방콕 도착, 15일 싱가포르 도착이라면:</p>\n<ul class=\"tips\">\n  <li>태국 TDAC: 7일부터 신청 (한국에서 출발 전에 처리)</li>\n  <li>싱가포르 SG Arrival Card: 13일부터 제출 (태국 여행 중에 처리)</li>\n</ul>\n\n<h2>여행 중에 놓치지 않으려면</h2>\n<ol class=\"steps\">\n  <li>각 나라 페이지 계산기에 그 나라 도착 날짜와 시각을 넣어요.</li>\n  <li>\"캘린더에 알림 추가\"로 나라별 알림을 미리 만들어 둬요.</li>\n  <li>여행 중 알림이 울리면 공식 사이트에서 바로 제출해요. 데이터가 되는 eSIM이 있으면 편해요.</li>\n</ol>\n\n<h2>같은 나라에 다시 들어갈 때</h2>\n<p>방콕 → 싱가포르 → 다시 방콕처럼 한 나라를 두 번 들어가면, 입국할 때마다 새로 신고하는 방식이라고 생각하세요. 첫 입국 때 받은 QR을 재사용할 수 없어요.</p>\n"
 }
]```

## 첨부: fields.json
```
{
 "japan": {
  "slug": "japan",
  "korean_ui": true,
  "korean_ui_note": "공식 매뉴얼 기준 한국어(한국어) UI를 지원해요. 단, 입력값은 모두 영문(로마자)·숫자로 넣어야 해요.",
  "sections": [
   {
    "title": "본인 정보 등록 (Your details / Passport information)",
    "fields": [
     {
      "label": "Do you have a Japanese passport?",
      "ko": "일본 여권 소지 여부",
      "how": "한국 여권 소지자는 'No'를 선택해요.",
      "required": true
     },
     {
      "label": "Do you hold a re-entry permit?",
      "ko": "재입국 허가 소지 여부",
      "how": "일본 재류카드·재입국 허가가 없는 일반 여행자는 'No'를 선택해요.",
      "required": true
     },
     {
      "label": "Passport number",
      "ko": "여권 번호",
      "how": "여권 사진면의 번호를 그대로 입력해요(예: M12345678). 여권 스캔(카메라 읽기)도 가능해요.",
      "required": true
     },
     {
      "label": "Surname",
      "ko": "성",
      "how": "여권 영문 성 그대로 입력해요(예: HONG). 최대 39자예요.",
      "required": true
     },
     {
      "label": "Given name",
      "ko": "이름",
      "how": "여권 영문 이름 그대로, 띄어쓰기·하이픈도 여권과 같게 입력해요(예: GILDONG 또는 GIL-DONG).",
      "required": true
     },
     {
      "label": "Nationality or citizenship",
      "ko": "국적",
      "how": "목록에서 Korea(Republic of Korea, 대한민국)를 선택해요.",
      "required": true
     },
     {
      "label": "Date of birth",
      "ko": "생년월일",
      "how": "생년월일을 선택해요. 영어 화면은 월/일/년(mm/dd/yyyy) 순이라 일·월이 바뀌지 않게 주의해요.",
      "required": true
     },
     {
      "label": "Date of expiry",
      "ko": "여권 만료일",
      "how": "여권에 적힌 기간만료일(Date of expiry)을 입력해요.",
      "required": true
     },
     {
      "label": "Occupation",
      "ko": "직업",
      "how": "드롭다운에서 가장 가까운 것을 골라요(예: 회사원이면 Office worker 계열).",
      "required": true
     },
     {
      "label": "Home address：Country name",
      "ko": "거주지 국가",
      "how": "Korea(Republic of Korea)를 선택해요.",
      "required": true
     },
     {
      "label": "Home address：City name",
      "ko": "거주지 도시",
      "how": "영문 도시명을 입력해요(예: SEOUL, BUSAN).",
      "required": true
     }
    ]
   },
   {
    "title": "입국·귀국 예정 (Planned entry/return)",
    "fields": [
     {
      "label": "Trip name",
      "ko": "여행 이름",
      "how": "나만 보는 메모용 이름이에요. 아무거나 영문으로 넣어도 돼요(예: OSAKA TRIP).",
      "required": true
     },
     {
      "label": "Planned arrival date in Japan",
      "ko": "일본 도착 예정일",
      "how": "항공권의 일본 도착 날짜를 선택해요.",
      "required": true
     },
     {
      "label": "Airline company name",
      "ko": "항공사명",
      "how": "목록에서 항공사를 선택해요(예: Korean Air, Jeju Air).",
      "required": true
     },
     {
      "label": "Flight number (numbers only)",
      "ko": "편명(숫자만)",
      "how": "항공사 코드 없이 숫자만 넣어요(예: KE723 → 723, 7C1101 → 1101).",
      "required": true
     }
    ]
   },
   {
    "title": "일본 연락처·숙소 (Address in Japan)",
    "fields": [
     {
      "label": "Postal code",
      "ko": "우편번호",
      "how": "숙소 우편번호 7자리를 입력하면 주소 일부가 자동 입력돼요(예: 5420081).",
      "required": true
     },
     {
      "label": "Prefecture",
      "ko": "도도부현",
      "how": "숙소가 있는 현을 선택해요(예: Osaka).",
      "required": true
     },
     {
      "label": "City",
      "ko": "시·구",
      "how": "영문으로 입력해요(예: OSAKA-SHI CHUO-KU).",
      "required": true
     },
     {
      "label": "Address",
      "ko": "상세 주소",
      "how": "영문·숫자로 번지까지 입력해요(예: MINAMISEMBA 1CHOME-2-3). 한글·일본어는 안 돼요.",
      "required": true
     },
     {
      "label": "Hotel name, place of stay",
      "ko": "숙소명",
      "how": "예약 확인서의 영문 호텔명을 넣어요(예: HOTEL GRACERY NAMBA).",
      "required": true
     },
     {
      "label": "Contact phone number",
      "ko": "연락처 전화번호",
      "how": "숙소 전화번호나 본인 휴대폰 번호를 숫자로 넣어요.",
      "required": true
     }
    ]
   },
   {
    "title": "입국심사 – 외국인 입국기록 (Immigration clearance / Disembarkation card)",
    "fields": [
     {
      "label": "Purpose of visit",
      "ko": "입국 목적",
      "how": "관광이면 Tourism을 골라요. 'Other'를 고르면 아래 칸을 써야 해요.",
      "required": true
     },
     {
      "label": "Specific purpose for visit",
      "ko": "구체적 방문 목적",
      "how": "Purpose of visit에서 Other를 골랐을 때만 영어로 짧게 써요.",
      "required": null
     },
     {
      "label": "Boarded flight number",
      "ko": "탑승 편명",
      "how": "Planned entry에서 넣은 편명이 이어져요. 다르면 실제 탑승편으로 고쳐요.",
      "required": true
     },
     {
      "label": "Point of embarkation",
      "ko": "출발지",
      "how": "출발 공항을 선택해요(예: Incheon, Gimpo).",
      "required": true
     },
     {
      "label": "Duration of stay in years / months / days",
      "ko": "체재 예정 기간(년/월/일)",
      "how": "3박 4일이면 days에 4처럼 일수만 넣고 나머지는 0으로 둬요.",
      "required": true
     },
     {
      "label": "Deportation/refused entry · Convicted · Prohibited items/firearms (Yes/No)",
      "ko": "강제퇴거·입국거부 이력 / 유죄판결 이력 / 금지물품·총포 소지",
      "how": "해당 사항이 없으면 세 질문 모두 'No'를 선택해요.",
      "required": true
     }
    ]
   },
   {
    "title": "세관 신고 (Customs declaration)",
    "fields": [
     {
      "label": "Questions 1/5 – 5/5",
      "ko": "세관 질문 1~5",
      "how": "금지·제한 물품, 면세범위 초과, 상업용 물품, 타인 부탁 물품, 100만 엔 상당 초과 현금 등 질문에 예/아니오로 답해요. 해당 없으면 모두 No예요.",
      "required": true
     },
     {
      "label": "Quantity of unaccompanied articles",
      "ko": "별송품 개수",
      "how": "따로 부친 짐(택배 등)이 없으면 0이에요.",
      "required": null
     },
     {
      "label": "Alcoholic beverages (Bottle(s)) / Cigarettes (Piece(s)) / Heat-Not-Burn (Box(es)) / Cigars (Piece(s)) / Others (g)",
      "ko": "주류(병)·궐련(개비)·가열담배(갑)·시가(개비)·기타(g)",
      "how": "가지고 오는 수량을 단위에 맞게 넣어요. 담배는 '갑'이 아니라 개비 수예요(1갑=20개비).",
      "required": null
     },
     {
      "label": "Accompanying family members",
      "ko": "동반 가족",
      "how": "미성년 자녀 등 동반가족은 '동반가족'으로 등록하면 세관신고를 대표로 함께 할 수 있어요.",
      "required": false
     }
    ]
   }
  ],
  "pitfalls": [
   "Flight number 칸에 KE723처럼 항공사 코드를 넣으면 안 돼요. 숫자(723)만 넣어요.",
   "영어 화면에서 날짜가 월/일/년 순서라 05/10을 5월 10일로 읽어야 해요. 일·월을 바꿔 넣기 쉬워요.",
   "숙소 주소를 한글이나 일본어로 넣으면 오류가 나요. 예약 확인서의 영문 주소를 복사해 넣어요.",
   "등록만 하고 '입국심사'와 '세관신고' 두 가지를 모두 완료(QR 생성)하지 않는 경우가 많아요. 두 항목 모두 '등록 완료' 상태인지 확인해요."
  ],
  "sources": [
   [
    "Visit Japan Web 공식 매뉴얼(영문, v3.16)",
    "https://www.vjw.digital.go.jp/manual/main/visitjapanweb_manual_en.html"
   ],
   [
    "디지털청 Visit Japan Web 매뉴얼 PDF(v2.00, 2022)",
    "https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/3e9afaa3-b2e7-4f6d-b07d-9697f39d97a3/73099bd6/20220926_en_visit_japan_web_manual_01.pdf"
   ],
   [
    "Visit Japan Web 공식 안내",
    "https://services.digital.go.jp/en/visit-japan-web/"
   ],
   [
    "MATCHA 가이드(보조)",
    "https://matcha-jp.com/en/24525"
   ]
  ],
  "confidence": "high"
 },
 "taiwan": {
  "slug": "taiwan",
  "korean_ui": true,
  "korean_ui_note": "공식 사이트 오른쪽 위 언어 메뉴에 한국어가 있어요(영어·중국어·일본어·한국어·인니어·베트남어·태국어). 영문 이름 칸은 한국어 화면에서도 영어로 입력해야 해요.",
  "sections": [
   {
    "title": "이메일 인증 (Email Verification)",
    "fields": [
     {
      "label": "Email Address",
      "ko": "이메일 주소",
      "how": "확인 메일을 받을 주소를 적고 SEND VERIFICATION CODE를 눌러요. 예: hong@naver.com",
      "required": true
     },
     {
      "label": "Enter Verification Code",
      "ko": "인증번호 입력",
      "how": "메일로 온 인증번호를 넣고 VERIFY CODE를 눌러요. 대소문자는 구분하지 않아요.",
      "required": true
     }
    ]
   },
   {
    "title": "여행자 정보 (Traveler Information)",
    "fields": [
     {
      "label": "Date of Entry Taiwan (DD/MM/YYYY)",
      "ko": "대만 예정 입국일",
      "how": "일/월/연도 순서로 적어요. 예: 15/10/2026. 입국 7일 전부터 제출할 수 있어요.",
      "required": true
     },
     {
      "label": "English Name",
      "ko": "영어 이름",
      "how": "여권 영문 이름을 영문자와 띄어쓰기만으로 적어요. 하이픈 같은 기호는 쓰면 안 돼요. 예: HONG GILDONG",
      "required": true
     },
     {
      "label": "Chinese Name",
      "ko": "한자 이름",
      "how": "선택 항목이에요. 한자 이름이 있으면 번체자로 적고, 없으면 비워 둬요. 예: 洪吉東",
      "required": false
     },
     {
      "label": "Passport Number",
      "ko": "여권 번호",
      "how": "여권 번호를 그대로 적어요. 예: M12345678",
      "required": true
     },
     {
      "label": "Date of Passport Expiry (DD/MM/YYYY)",
      "ko": "여권 만료일",
      "how": "여권의 '기간만료일'을 일/월/연도로 적어요. 발급일과 헷갈리지 마세요. 예: 20/06/2033",
      "required": true
     },
     {
      "label": "Sex",
      "ko": "성별",
      "how": "MALE 또는 FEMALE을 골라요.",
      "required": true
     },
     {
      "label": "Date of Birth (DD/MM/YYYY)",
      "ko": "생년월일",
      "how": "일/월/연도 순서예요. 예: 20/06/1985",
      "required": true
     },
     {
      "label": "Nationality",
      "ko": "국적",
      "how": "대한민국(KOREA, REPUBLIC OF)을 골라요.",
      "required": true
     },
     {
      "label": "Country/ Place of Birth",
      "ko": "출생지(국가)",
      "how": "대부분 대한민국을 골라요.",
      "required": true
     },
     {
      "label": "City/ State or Province",
      "ko": "도시/주 또는 도",
      "how": "출생 도시를 영문으로 적어요. 예: SEOUL",
      "required": null
     },
     {
      "label": "Place of Residence",
      "ko": "거주지",
      "how": "사는 나라를 골라요. 예: 대한민국",
      "required": true
     },
     {
      "label": "Visa Type",
      "ko": "비자 종류",
      "how": "한국인 관광객은 무비자이므로 Visa-Exempt(include TAC)를 골라요.",
      "required": true
     },
     {
      "label": "Visa Number",
      "ko": "비자 번호",
      "how": "비자를 받은 경우에만 나와요. 무비자면 입력하지 않아요.",
      "required": null
     },
     {
      "label": "Country/ Region Code",
      "ko": "국가/지역 코드",
      "how": "한국 번호면 +82를 골라요.",
      "required": true
     },
     {
      "label": "Mobile Number",
      "ko": "휴대폰 번호",
      "how": "맨 앞 0을 빼고 적어요. 예: 1012345678",
      "required": true
     },
     {
      "label": "Occupation",
      "ko": "직업",
      "how": "목록에서 골라요. 예: 회사원은 CLERK/EMPLOYEE/STAFF, 학생은 STUDENT/SCHOLAR/PUPIL",
      "required": true
     },
     {
      "label": "JobTitle",
      "ko": "직함",
      "how": "직업에 따라 나오면 실제 직함을 영문으로 적어요. 예: MANAGER",
      "required": null
     }
    ]
   },
   {
    "title": "일정 (Itinerary)",
    "fields": [
     {
      "label": "Expected Mode of Entry",
      "ko": "입국 수단",
      "how": "비행기면 Air, 배면 Sea를 골라요.",
      "required": true
     },
     {
      "label": "Expected Entry Flight Code",
      "ko": "예정 입국 항공사 코드",
      "how": "편명 앞 영문 2글자만 골라요. 예: KE621이면 KE",
      "required": true
     },
     {
      "label": "Expected Entry Flight Number",
      "ko": "예정 입국 항공편 번호",
      "how": "편명 숫자만 적어요. 예: KE621이면 621",
      "required": true
     },
     {
      "label": "Expected Departure Taiwan Date (DD/MM/YYYY)",
      "ko": "대만 예정 출국일",
      "how": "일/월/연도로 적어요. 입국일보다 뒤여야 해요. 예: 19/10/2026",
      "required": true
     },
     {
      "label": "Expected Mode of Departure",
      "ko": "출국 수단",
      "how": "돌아올 때 비행기면 Air를 골라요.",
      "required": true
     },
     {
      "label": "Expected Departure Flight Code",
      "ko": "예정 출국 항공사 코드",
      "how": "귀국편 항공사 코드를 골라요. 예: KE",
      "required": true
     },
     {
      "label": "Expected Departure Flight Number",
      "ko": "예정 출국 항공편 번호",
      "how": "귀국편 숫자만 적어요. 예: KE622이면 622",
      "required": true
     },
     {
      "label": "Purpose of Visit",
      "ko": "방문 목적",
      "how": "관광이면 '3.觀光 Sightseeing / Travel / Leisure'를 골라요.",
      "required": true
     },
     {
      "label": "Relatives Name",
      "ko": "방문 대상자 이름",
      "how": "목적이 Visit Relative일 때만 나와요. 방문할 친척 이름을 적어요.",
      "required": null
     },
     {
      "label": "Relatives Mobile No",
      "ko": "방문 대상자 전화번호",
      "how": "목적이 Visit Relative일 때만 나와요. 친척 연락처를 적어요.",
      "required": null
     },
     {
      "label": "Reason",
      "ko": "사유",
      "how": "목적이 Others일 때만 나와요. 방문 이유를 영어로 짧게 적어요.",
      "required": null
     },
     {
      "label": "Accommodation in Taiwan",
      "ko": "대만 내 숙소",
      "how": "호텔이면 Hotel Name, 지인 집이면 Residential Address, 경유만 하면 Transfer를 골라요.",
      "required": true
     },
     {
      "label": "Hotel Name",
      "ko": "호텔 이름",
      "how": "예약한 호텔명을 영문 또는 번체로 정확히 적어요. 예: Grand Hyatt Taipei",
      "required": null
     },
     {
      "label": "Residential Address",
      "ko": "거주 주소",
      "how": "지인 집에 묵으면 대만 주소를 적어요. 주소 확인 후 체크박스로 확인해요.",
      "required": null
     }
    ]
   },
   {
    "title": "검토·선언 (Review / Declaration)",
    "fields": [
     {
      "label": "Declaration",
      "ko": "선언",
      "how": "입력 내용이 사실이라는 선언문에 체크하고 SUBMIT을 눌러요. 확인 메일이 와요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "날짜가 전부 DD/MM/YYYY(일/월/연도)라서 한국식(연/월/일)이나 미국식(월/일)으로 적는 실수가 많아요.",
   "영어 이름 칸에 하이픈(GIL-DONG)이나 쉼표를 넣으면 안 돼요. 영문자와 띄어쓰기만 써요.",
   "항공편을 'KE621'로 한 칸에 다 적으려다 막혀요. 항공사 코드(KE)와 숫자(621)를 나눠 넣어요.",
   "숙소를 'TAIPEI'처럼 도시명만 적으면 안 돼요. 호텔 정식 이름이나 실제 주소를 적어요."
  ],
  "sources": [
   [
    "TWAC 공식 사이트(입력 항목·언어 확인)",
    "https://twac.immigration.gov.tw/"
   ],
   [
    "TravelClassroom TWAC 가이드",
    "https://www.travelclassroom.net/eng/taiwan-arrival-card.html"
   ]
  ],
  "confidence": "high"
 },
 "china": {
  "slug": "china",
  "korean_ui": true,
  "korean_ui_note": "한국어로 볼 수 있다는 안내가 여러 곳 있지만 공식 확인은 못 했어요. 정확하게 쓰려면 영어 화면을 권해요.",
  "sections": [
   {
    "title": "여권 업로드 (ID Document Upload)",
    "fields": [
     {
      "label": "Type of ID Document",
      "ko": "신분증(여행증명서) 종류",
      "how": "일반 여권이면 Ordinary Passport를 골라요.",
      "required": true
     },
     {
      "label": "Upload ID Document Page",
      "ko": "여권 정보면 업로드",
      "how": "사진이 있는 여권 정보면을 밝은 곳에서 반사 없이 찍어 올려요. 인식된 정보가 자동 입력돼요.",
      "required": true
     }
    ]
   },
   {
    "title": "기본 정보 (Basic Personal Information)",
    "fields": [
     {
      "label": "Last Name",
      "ko": "성",
      "how": "여권 영문 성을 써요. 예: HONG",
      "required": true
     },
     {
      "label": "First Name",
      "ko": "이름",
      "how": "여권 영문 이름을 붙여서 써요. 예: GILDONG",
      "required": true
     },
     {
      "label": "Gender",
      "ko": "성별",
      "how": "Male(남) 또는 Female(여)을 골라요.",
      "required": true
     },
     {
      "label": "Date of Birth",
      "ko": "생년월일",
      "how": "여권과 같은 생년월일을 골라요.",
      "required": true
     },
     {
      "label": "Country/Region of Citizenship",
      "ko": "국적",
      "how": "Republic of Korea(대한민국)를 골라요. 북한(DPRK)과 헷갈리지 마세요.",
      "required": true
     },
     {
      "label": "ID Number",
      "ko": "여권 번호",
      "how": "여권 번호를 공백 없이 써요. 예: M12345678",
      "required": true
     },
     {
      "label": "Entry Transportation Mode",
      "ko": "입국 교통수단",
      "how": "비행기면 Flight, 배·기차면 해당 항목을 골라요.",
      "required": true
     },
     {
      "label": "Arrival Flight/Train/Vessel Number",
      "ko": "도착 항공편/열차/선박 번호",
      "how": "항공사 코드+숫자로 써요. 예: KE853, CA124",
      "required": true
     },
     {
      "label": "City of Entry",
      "ko": "입국 도시",
      "how": "처음 도착하는 도시를 골라요(성별로 정렬돼요). 예: Beijing, Shanghai",
      "required": true
     },
     {
      "label": "Port of Entry",
      "ko": "입국 공항·항구",
      "how": "도착 공항을 골라요. 예: Shanghai Pudong International Airport",
      "required": true
     }
    ]
   },
   {
    "title": "추가 정보 (Additional Personal Information)",
    "fields": [
     {
      "label": "Chinese Name",
      "ko": "중문 이름",
      "how": "중국식 이름이 있을 때만 써요. 한자 이름이 있어도 비워 둬도 돼요.",
      "required": false
     },
     {
      "label": "Country/Region of Birth",
      "ko": "출생 국가",
      "how": "한국 출생이면 Republic of Korea를 골라요.",
      "required": true
     },
     {
      "label": "City of Birth",
      "ko": "출생 도시",
      "how": "영문으로 써요. 예: SEOUL, BUSAN",
      "required": true
     },
     {
      "label": "Contact Number",
      "ko": "연락처",
      "how": "국가번호 +82를 고르고 맨 앞 0을 뺀 휴대폰 번호를 써요. 예: 1012345678",
      "required": true
     },
     {
      "label": "Email",
      "ko": "이메일",
      "how": "연락받을 이메일을 써요. 예: gildong@naver.com",
      "required": null
     },
     {
      "label": "Do you hold a valid visa or other entry permit?",
      "ko": "유효한 비자·입국허가 보유 여부",
      "how": "비자를 받았으면 Yes 후 비자 번호를 써요. 한국인 무비자 입국이면 No를 고르고 Visa-free 정책을 선택해요.",
      "required": true
     },
     {
      "label": "Entry Policy Selection",
      "ko": "입국 정책 선택",
      "how": "No를 골랐을 때 나와요. 한국 여권 관광·비즈니스 단기 방문이면 무비자(Visa-free Entry) 항목을 골라요.",
      "required": false
     },
     {
      "label": "Visa Number",
      "ko": "비자 번호",
      "how": "비자가 있을 때만 비자 스티커의 번호를 써요.",
      "required": false
     }
    ]
   },
   {
    "title": "중국 내 여행 정보 (Travel Information in China)",
    "fields": [
     {
      "label": "Purpose of Entry",
      "ko": "입국 목적",
      "how": "관광이면 Tourism/Sightseeing, 출장이면 Business 등을 골라요.",
      "required": true
     },
     {
      "label": "Date of Entry",
      "ko": "입국일",
      "how": "중국 도착 날짜를 골라요.",
      "required": true
     },
     {
      "label": "Destination Cities in China",
      "ko": "중국 내 목적지 도시",
      "how": "방문할 도시를 모두 골라요. 예: Shanghai, Hangzhou",
      "required": true
     },
     {
      "label": "Address in China",
      "ko": "중국 내 주소",
      "how": "호텔 예약 확인서의 영문(또는 중문) 주소를 상세히 써요. 예: Hilton Shanghai Hongqiao, 1116 Hongsong East Road, Minhang District",
      "required": true
     },
     {
      "label": "Cities of Transit in China",
      "ko": "중국 내 경유 도시",
      "how": "중국 안에서 거쳐 가는 도시가 있으면 골라요.",
      "required": false
     },
     {
      "label": "Do you have any inviting entities or inviters in China?",
      "ko": "중국 내 초청 기관·초청인 여부",
      "how": "관광객은 보통 No예요. 초청장이 있으면 Yes 후 정보를 써요.",
      "required": true
     },
     {
      "label": "Confirmed Departure Itinerary",
      "ko": "확정된 출국 일정",
      "how": "돌아가는 항공권이 있으면 Yes를 고르고 출국일·편명·출국 공항을 써요. 예: 출국편 KE854",
      "required": null
     }
    ]
   }
  ],
  "pitfalls": [
   "Last Name/First Name을 반대로 써요. Last Name이 성(HONG), First Name이 이름(GILDONG)이에요.",
   "무비자인데 비자 질문에서 Yes를 누르거나 정책 선택을 건너뛰어요. 비자가 없으면 No를 고르고 무비자 항목을 선택해요.",
   "주소를 'Shanghai hotel'처럼 대충 써요. 예약 확인서의 도로명·구까지 상세 주소를 써요.",
   "가족 중 한 명만 작성해요. QR코드는 한 사람당 하나라서 아이까지 각각 만들어야 해요."
  ],
  "sources": [
   [
    "주바베이도스 중국대사관 온라인 입국카드 안내",
    "https://bb.china-embassy.gov.cn/eng/lsyws/202511/t20251128_11762211.htm"
   ],
   [
    "중국 국가이민관리국(NIA) 정책 해설 영상 페이지",
    "https://en.nia.gov.cn/n147418/n147463/c195170/content.html"
   ],
   [
    "NIA 온라인 작성 사이트",
    "https://s.nia.gov.cn/ArrivalCardFillingPC/"
   ],
   [
    "VisasNews 단계별 작성 안내(보조)",
    "https://visasnews.com/en/china-launches-its-digital-arrival-card-today-heres-how-to-complete-it/"
   ],
   [
    "요모매거진 작성법(보조)",
    "https://yomolabs.kr/2026-china-arrival-card-qr"
   ],
   [
    "Egg and Banana 가이드(보조)",
    "https://egg-and-banana.com/china-digital-arrival-card-guide/"
   ],
   [
    "트립닷컴 안내(보조)",
    "https://us.trip.com/guide/arrival/china-arrival-card.html"
   ]
  ],
  "confidence": "medium"
 },
 "vietnam": {
  "korean_ui": true,
  "korean_ui_note": "공식 사이트 오른쪽 위 언어 메뉴에서 '한국어'를 고를 수 있어요. 다만 한국어 화면은 기계 번역이라 '공기 호스(Airline)', '숫자(Number)'처럼 이상한 표현이 섞여 있어요. 아래 표의 '한국어 화면 표시'와 '실제 뜻'을 같이 보세요.",
  "confidence": "high",
  "sections": [
   {
    "title": "시작 (Nationality)",
    "fields": [
     {
      "label": "Nationality",
      "ko_ui": "국적",
      "ko": "국적",
      "how": "'Republic of Korea (KOR)'를 골라요. 목록에서 바로 위에 있는 'Democratic People's Republic of Korea'는 북한이니 절대 고르지 마세요.",
      "required": true
     }
    ]
   },
   {
    "title": "승객 정보 (Passenger Information)",
    "fields": [
     {
      "label": "Expected Arrival Date (DD/MM/YYYY GMT+7)",
      "ko_ui": "예상 도착일",
      "ko": "베트남 도착 예정일",
      "how": "버튼으로 나오는 날짜 중 도착일을 눌러요. 도착 72시간 전부터 신청할 수 있어서 날짜가 3개 정도만 보여요.",
      "required": true
     },
     {
      "label": "Upload Image",
      "ko_ui": "이미지 업로드",
      "ko": "여권 사진 올리기",
      "how": "여권 사진면을 올리면 일부 칸이 자동으로 채워져요. 선택 사항이라 건너뛰어도 돼요.",
      "required": false
     },
     {
      "label": "Passport Type",
      "ko_ui": "여권 유형",
      "ko": "여권 종류",
      "how": "일반 여권이면 'P - Popular Passport'를 골라요.",
      "required": true
     },
     {
      "label": "Passport Number",
      "ko_ui": "여권 번호",
      "ko": "여권 번호",
      "how": "여권 사진면의 번호를 그대로 적어요. 예: M12345678",
      "required": true
     },
     {
      "label": "Date of Expiry (DD/MM/YYYY)",
      "ko_ui": "만료일",
      "ko": "여권 만료일",
      "how": "일/월/연도 순서예요. 2030년 3월 15일이면 15/03/2030으로 적어요.",
      "required": true
     },
     {
      "label": "Gender",
      "ko_ui": "성별",
      "ko": "성별",
      "how": "Male(남성)·Female(여성) 중 골라요. 한국어 화면의 '다른'은 Other(기타)라는 뜻이에요.",
      "required": true
     },
     {
      "label": "Surname",
      "ko_ui": "성",
      "ko": "성(영문)",
      "how": "여권 영문 성을 적어요. 예: HONG",
      "required": false
     },
     {
      "label": "Given Name",
      "ko_ui": "이름",
      "ko": "이름(영문)",
      "how": "여권 영문 이름을 띄어쓰기까지 그대로 적어요. 예: GIL DONG",
      "required": true
     },
     {
      "label": "Date of Birth (DD/MM/YYYY)",
      "ko_ui": "생일",
      "ko": "생년월일",
      "how": "일/월/연도 순서예요. 1985년 7월 2일이면 02/07/1985.",
      "required": true
     },
     {
      "label": "Nationality",
      "ko_ui": "국적",
      "ko": "국적",
      "how": "Republic of Korea가 맞는지 다시 확인해요.",
      "required": true
     },
     {
      "label": "Country Code",
      "ko_ui": "국가 코드",
      "ko": "전화 국가번호",
      "how": "한국은 +82를 골라요.",
      "required": true
     },
     {
      "label": "Phone Number",
      "ko_ui": "전화 번호",
      "ko": "휴대폰 번호",
      "how": "맨 앞 0을 빼고 적어요. 010-1234-5678이면 1012345678.",
      "required": true
     },
     {
      "label": "Email Address",
      "ko_ui": "이메일 주소",
      "ko": "이메일 주소",
      "how": "QR코드가 이 주소로 와요. 자주 쓰는 메일을 정확히 적어요.",
      "required": true
     }
    ]
   },
   {
    "title": "비자 정보 (Visa Information)",
    "fields": [
     {
      "label": "I have read and understood this information.",
      "ko_ui": "저는 이 정보를 읽고 이해했습니다.",
      "ko": "안내를 읽었다는 확인",
      "how": "안내 문구를 읽고 체크해요.",
      "required": true
     },
     {
      "label": "Visa Type / Purpose",
      "ko_ui": "비자 종류/목적",
      "ko": "비자 종류",
      "how": "한국인이 무비자로 여행하면 'Unilateral exemption(일방적 비자 면제)'을 골라요. 전자비자를 받았으면 'Electronic Visa (E-Visa)', 푸꾸옥만 가면 'Phu Quoc Visa Exemption'이에요.",
      "required": true
     },
     {
      "label": "Number",
      "ko_ui": "숫자",
      "ko": "비자 번호",
      "how": "전자비자를 받은 경우 비자 번호를 적어요. 한국어 화면에 '숫자'로 나오지만 '번호'라는 뜻이에요.",
      "required": true
     },
     {
      "label": "Date of Issue (DD/MM/YYYY)",
      "ko_ui": "발행일",
      "ko": "비자 발급일",
      "how": "비자가 있을 때만 적어요.",
      "required": false
     },
     {
      "label": "Date of Expiry (DD/MM/YYYY)",
      "ko_ui": "만료일",
      "ko": "비자 만료일",
      "how": "비자가 있을 때 비자의 만료일을 적어요. 위의 여권 만료일과 헷갈리지 마세요.",
      "required": true
     },
     {
      "label": "Issued Place",
      "ko_ui": "발행 장소",
      "ko": "비자 발급처",
      "how": "비자가 있을 때만 적어요.",
      "required": false
     }
    ]
   },
   {
    "title": "여행 정보 (Trip Information)",
    "fields": [
     {
      "label": "Departure country before Arrival in Vietnam",
      "ko_ui": "베트남 도착 전 출발 장소",
      "ko": "베트남 오기 직전 출발 국가",
      "how": "한국에서 바로 가면 Republic of Korea를 골라요.",
      "required": true
     },
     {
      "label": "First Point of Departure if Transiting Through Multiple country",
      "ko_ui": "여러 곳을 경유하는 경우 첫 번째 출발 지점",
      "ko": "경유했다면 처음 출발한 곳",
      "how": "직항이면 비워 두거나 출발 국가와 같게 해요.",
      "required": false
     },
     {
      "label": "Purpose of Travel",
      "ko_ui": "여행 목적",
      "ko": "여행 목적",
      "how": "관광이면 관광(Tourism) 항목을 골라요.",
      "required": true
     },
     {
      "label": "Mode of Travel",
      "ko_ui": "이동 수단",
      "ko": "입국 방법",
      "how": "비행기면 Air(한국어 화면은 '공')를 골라요.",
      "required": true
     },
     {
      "label": "Mode of Transport",
      "ko_ui": "교통수단",
      "ko": "항공편 종류",
      "how": "일반 항공권은 Commercial을 골라요. 한국어 화면에 '광고'로 잘못 나오지만 '정기 상업 항공편'이라는 뜻이에요. 전세기 여행은 Charter(전세).",
      "required": true
     },
     {
      "label": "Airline",
      "ko_ui": "공기 호스",
      "ko": "항공사",
      "how": "한국어 화면에 '공기 호스'로 나오는 칸이 항공사예요. 예: Vietjet Air, Korean Air",
      "required": true
     },
     {
      "label": "Arrival Airport",
      "ko_ui": "도착 공항",
      "ko": "도착 공항",
      "how": "예: 다낭은 Da Nang, 호치민은 Tan Son Nhat, 하노이는 Noi Bai",
      "required": true
     },
     {
      "label": "Flight Number",
      "ko_ui": "항공편 코드",
      "ko": "항공편 번호",
      "how": "항공권에 적힌 편명을 적어요. 예: VJ963, KE463",
      "required": true
     },
     {
      "label": "Seat Code",
      "ko_ui": "좌석 코드",
      "ko": "좌석 번호",
      "how": "좌석이 정해졌으면 적어요. 예: 23A",
      "required": false
     },
     {
      "label": "Type of Accommodation in Vietnam",
      "ko_ui": "베트남의 숙박 유형",
      "ko": "숙소 종류",
      "how": "호텔·리조트는 Hotel(호텔), 지인 집은 Residential(주거용), 에어비앤비 등은 Others(기타).",
      "required": true
     },
     {
      "label": "Accommodation Address",
      "ko_ui": "숙소 주소",
      "ko": "숙소 주소",
      "how": "호텔 영문 이름과 주소를 적어요. 예: Novotel Danang Premier Han River, 36 Bach Dang, Da Nang",
      "required": true
     },
     {
      "label": "Expected date of departure from Vietnam (DD/MM/YYYY GMT+7)",
      "ko_ui": "베트남 출국 예정일",
      "ko": "베트남에서 나가는 날",
      "how": "귀국 항공편 날짜를 일/월/연도로 적어요.",
      "required": true
     },
     {
      "label": "Next Intended Country of Disembarkation After Vietnam",
      "ko_ui": "베트남 이후 다음 도착 예정 국가",
      "ko": "베트남 다음 행선지",
      "how": "한국으로 돌아오면 Republic of Korea를 골라요.",
      "required": true
     }
    ]
   },
   {
    "title": "확인·제출 (Review & Submit)",
    "fields": [
     {
      "label": "I confirm that the information is correct.",
      "ko_ui": "(확인 체크)",
      "ko": "정보가 맞다는 확인",
      "how": "요약 화면에서 이름·여권번호·날짜를 한 번 더 보고 체크한 뒤 제출해요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "국적 목록에서 북한(Democratic People's Republic of Korea)을 고르는 실수가 있어요. 꼭 'Republic of Korea (KOR)'를 고르세요.",
   "날짜는 모두 일/월/연도(DD/MM/YYYY)예요. 한국식(연/월/일)으로 적지 마세요.",
   "무비자 여행인데 비자 종류에서 'Visa'나 'Bilateral exemption'을 고르는 경우가 많아요. 한국인 무비자는 'Unilateral exemption'이에요.",
   "한국어 화면은 기계 번역이라 '공기 호스'(항공사), '광고'(정기 항공편), '숫자'(번호)처럼 뜻이 틀린 곳이 있어요. 헷갈리면 오른쪽 위에서 English로 바꿔 보세요."
  ],
  "sources": [
   [
    "베트남 출입국관리국 사전 입국신고 공식 화면 (2026-10-05 직접 확인)",
    "https://prearrival.immigration.gov.vn/"
   ]
  ]
 },
 "thailand": {
  "slug": "thailand",
  "korean_ui": true,
  "korean_ui_note": "공식 FAQ가 한국어 등 다국어 지원을 명시하고, 한국어 매뉴얼(성(Family Name) 등 라벨)도 있어요. 입력값은 영어로만 써야 해요.",
  "sections": [
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Family Name",
      "ko": "성",
      "how": "여권 영문 성 그대로 입력해요(예: HONG). 성이 없으면 하이픈(-)을 넣을 수 있어요.",
      "required": true
     },
     {
      "label": "First Name",
      "ko": "이름",
      "how": "여권 영문 이름 그대로 입력해요(예: GILDONG).",
      "required": true
     },
     {
      "label": "Middle Name",
      "ko": "중간 이름",
      "how": "한국인은 보통 없으니 비워 둬요.",
      "required": false
     },
     {
      "label": "Passport Number",
      "ko": "여권 번호",
      "how": "여권 번호를 입력하면 자동으로 대문자로 바뀌어요(예: M12345678).",
      "required": true
     },
     {
      "label": "Nationality/Citizenship",
      "ko": "국적",
      "how": "목록에서 KOREA, REPUBLIC OF를 선택해요. 앞 세 글자(KOR)를 치면 찾기 쉬워요.",
      "required": true
     },
     {
      "label": "Date of Birth",
      "ko": "생년월일",
      "how": "달력에서 선택해요. 제출 후엔 수정이 안 되니 정확히 넣어요.",
      "required": true
     },
     {
      "label": "Occupation",
      "ko": "직업",
      "how": "영어로 입력해요(예: OFFICE WORKER, STUDENT).",
      "required": true
     },
     {
      "label": "Gender",
      "ko": "성별",
      "how": "여권과 같게 Male/Female을 선택해요.",
      "required": true
     },
     {
      "label": "Visa Number",
      "ko": "비자 번호",
      "how": "90일 무비자 관광이면 비워 둬요. 비자가 있을 때만 넣어요.",
      "required": false
     },
     {
      "label": "Country/Territory of Residence",
      "ko": "거주 국가",
      "how": "KOREA, REPUBLIC OF를 선택해요.",
      "required": true
     },
     {
      "label": "City/State of Residence",
      "ko": "거주 도시/주",
      "how": "영문 도시명을 입력해요(예: SEOUL).",
      "required": true
     },
     {
      "label": "Phone Number",
      "ko": "전화번호",
      "how": "국가번호 82와 맨 앞 0을 뺀 번호를 넣어요(예: 82 / 1012345678).",
      "required": true
     },
     {
      "label": "Email",
      "ko": "이메일",
      "how": "확인서(QR)를 받을 이메일이에요. 현재는 필수가 아니지만 넣는 게 좋아요.",
      "required": false
     }
    ]
   },
   {
    "title": "여행 정보 (Trip Information)",
    "fields": [
     {
      "label": "Date of Arrival",
      "ko": "도착일",
      "how": "태국 도착 날짜를 골라요. 도착 3일 전(도착일 포함)부터 제출 가능해요.",
      "required": true
     },
     {
      "label": "Country/Territory where you Boarded",
      "ko": "탑승 국가",
      "how": "인천·김포 출발이면 KOREA, REPUBLIC OF를 선택해요. 경유편이면 마지막 탑승지 국가예요.",
      "required": true
     },
     {
      "label": "Purpose of Travel",
      "ko": "여행 목적",
      "how": "관광이면 HOLIDAY를 선택해요.",
      "required": true
     },
     {
      "label": "Mode of Travel",
      "ko": "교통수단",
      "how": "비행기면 AIR를 선택하고, 이어서 상업용 항공편(COMMERCIAL FLIGHT)을 골라요.",
      "required": true
     },
     {
      "label": "Flight No./Vehicle No.",
      "ko": "항공편 번호/차량 번호",
      "how": "항공사 코드+숫자로 붙여 써요(예: TG659, 7C2201). 최대 20자예요.",
      "required": true
     },
     {
      "label": "Date of Departure",
      "ko": "출국일",
      "how": "귀국편 날짜를 넣어요. 현재는 선택 항목이에요.",
      "required": false
     },
     {
      "label": "Mode of Travel (Departure)",
      "ko": "출국 교통수단",
      "how": "출국 정보를 넣을 때 AIR 등을 선택해요.",
      "required": false
     },
     {
      "label": "Flight No./Vehicle No. (Departure)",
      "ko": "출국 항공편 번호",
      "how": "귀국 편명을 넣어요(예: TG658).",
      "required": false
     }
    ]
   },
   {
    "title": "태국 내 숙소 정보 (Accommodation Information)",
    "fields": [
     {
      "label": "Type of Accommodation",
      "ko": "숙소 유형",
      "how": "호텔이면 HOTEL을 선택해요. 경유만 하는 경우 숙소 대신 경유 여부를 체크해요.",
      "required": true
     },
     {
      "label": "Province",
      "ko": "주(짱왓)",
      "how": "숙소가 있는 주를 골라요(예: BANGKOK, PHUKET).",
      "required": true
     },
     {
      "label": "District/Area",
      "ko": "구(암퍼/켓)",
      "how": "숙소가 있는 구를 골라요(예: WATTHANA).",
      "required": true
     },
     {
      "label": "Sub-District/Sub-Area",
      "ko": "동(땀본/쾡)",
      "how": "숙소가 있는 동을 골라요(예: KHLONG TOEI NUEA).",
      "required": true
     },
     {
      "label": "Post Code",
      "ko": "우편번호",
      "how": "숫자로 입력해요. 구·동을 고르면 자동 입력되기도 해요(예: 10110).",
      "required": true
     },
     {
      "label": "Address",
      "ko": "주소",
      "how": "호텔명과 영문 주소를 입력해요(예: HOTEL NAME, 123 SUKHUMVIT RD).",
      "required": true
     }
    ]
   },
   {
    "title": "건강 신고 (Health Declaration)",
    "fields": [
     {
      "label": "Countries where you stayed within two weeks before arrival",
      "ko": "도착 전 2주 내 체류 국가",
      "how": "한국에서 바로 오면 KOREA, REPUBLIC OF를 선택해요. 황열병 위험국 방문 시 추가 서류가 필요할 수 있어요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "Family Name과 First Name을 바꿔 넣는 실수가 많아요. Family Name은 성(HONG)이에요. 성명·국적·생년월일은 제출 후 수정이 안 돼요.",
   "편명을 숫자만 넣거나 띄어 써요. TG659처럼 항공사 코드와 숫자를 붙여 써요.",
   "도착 3일 전보다 일찍 제출하려 하거나, 수수료를 받는 가짜 TDAC 사이트를 이용하는 경우가 있어요. 공식 사이트(tdac.immigration.go.th)는 무료예요.",
   "숙소 주소를 한글로 쓰거나 Province/District를 잘못 골라요. 예약 확인서의 영문 주소를 기준으로 선택해요."
  ],
  "sources": [
   [
    "TDAC 공식 사이트",
    "https://tdac.immigration.go.th/"
   ],
   [
    "TDAC 공식 FAQ(영문)",
    "https://tdac.immigration.go.th/manual/en/faq.html"
   ],
   [
    "TDAC 공식 FAQ(한국어)",
    "https://tdac.immigration.go.th/manual/kr/faq.html"
   ],
   [
    "TDAC 공식 사용자 가이드",
    "https://tdac.immigration.go.th/manual/en/"
   ],
   [
    "Montmari 단계별 가이드(스크린샷)",
    "https://montmari-asia.com/en/blog/39048/"
   ],
   [
    "Tripseed 필드 목록",
    "https://www.tripseed.com/ultimate-2025-guide-to-the-thailand-digital-arrival-card-tdac-essential-information-for-travel-professionals/"
   ]
  ],
  "confidence": "medium"
 },
 "philippines": {
  "slug": "philippines",
  "korean_ui": true,
  "korean_ui_note": "etravel.gov.ph 첫 화면에서 English/Chinese/Korean/Japanese 중 한국어를 고를 수 있어요. 다만 입력 화면의 일부 항목은 영어로 남아 있을 수 있어요.",
  "sections": [
   {
    "title": "계정 만들기 (Create an account)",
    "fields": [
     {
      "label": "Email address",
      "ko": "이메일 주소",
      "how": "QR코드와 확인 메일을 받을 이메일을 적어요. 예: hong@naver.com",
      "required": true
     },
     {
      "label": "One-Time-Password",
      "ko": "일회용 인증번호(OTP)",
      "how": "이메일로 온 6자리 인증번호를 입력해요.",
      "required": true
     },
     {
      "label": "Password",
      "ko": "비밀번호",
      "how": "영문 대·소문자와 숫자를 섞어 새로 만들어요. 나중에 수정할 때 다시 써야 하니 꼭 기억해 두세요.",
      "required": true
     }
    ]
   },
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Foreign Passport Holder",
      "ko": "외국 여권 소지자",
      "how": "한국 여권이면 'Foreign Passport Holder'를 골라요.",
      "required": true
     },
     {
      "label": "First Name",
      "ko": "이름",
      "how": "여권의 이름(Given name)을 영문 그대로 적어요. 예: GILDONG",
      "required": true
     },
     {
      "label": "Middle Name",
      "ko": "중간 이름",
      "how": "한국인은 보통 없으니 비워 두거나 해당 없음으로 둬요.",
      "required": false
     },
     {
      "label": "Last Name",
      "ko": "성",
      "how": "여권의 성(Surname)을 적어요. 예: HONG",
      "required": true
     },
     {
      "label": "Suffix",
      "ko": "접미사",
      "how": "JR., III 같은 호칭이에요. 한국인은 비워 둬요.",
      "required": false
     },
     {
      "label": "Sex",
      "ko": "성별",
      "how": "여권에 적힌 성별을 골라요.",
      "required": true
     },
     {
      "label": "Birth Date",
      "ko": "생년월일",
      "how": "달력에서 골라요. 월/일/연도 순서로 표시될 수 있으니 순서를 꼭 확인해요. 예: 06/20/1985",
      "required": true
     },
     {
      "label": "Citizenship",
      "ko": "국적",
      "how": "목록에서 한국을 골라요(예: SOUTH KOREAN / KOREA, REPUBLIC OF로 표시).",
      "required": true
     },
     {
      "label": "Country of Birth",
      "ko": "출생 국가",
      "how": "대부분 한국을 골라요. 예: SOUTH KOREA",
      "required": true
     },
     {
      "label": "Mobile Number",
      "ko": "휴대폰 번호",
      "how": "국가번호 +82를 고르고 맨 앞 0을 빼고 적어요. 예: 1012345678",
      "required": true
     },
     {
      "label": "Occupation",
      "ko": "직업",
      "how": "목록에서 가장 가까운 직업을 골라요. 예: 회사원이면 Employee/Worker 계열",
      "required": true
     }
    ]
   },
   {
    "title": "여권 정보 (Passport Information)",
    "fields": [
     {
      "label": "Passport Number",
      "ko": "여권 번호",
      "how": "여권 사진면의 번호를 그대로 적어요. 예: M12345678",
      "required": true
     }
    ]
   },
   {
    "title": "영구 거주 국가 (Permanent Country of Residence)",
    "fields": [
     {
      "label": "Country",
      "ko": "국가",
      "how": "한국에 살면 SOUTH KOREA(대한민국)를 골라요.",
      "required": true
     },
     {
      "label": "House No./Bldg./Street",
      "ko": "집 주소",
      "how": "한국 주소를 영문으로 적어요. 예: 123 Teheran-ro, Gangnam-gu, Seoul",
      "required": true
     }
    ]
   },
   {
    "title": "여행 정보 (Travel Details)",
    "fields": [
     {
      "label": "Travel Type",
      "ko": "여행 구분",
      "how": "필리핀에 들어갈 때는 Arrival을 골라요.",
      "required": true
     },
     {
      "label": "Purpose of Travel",
      "ko": "여행 목적",
      "how": "관광이면 HOLIDAY/PLEASURE/VACATION을 골라요.",
      "required": true
     },
     {
      "label": "Traveller Type",
      "ko": "여행자 유형",
      "how": "일반 승객은 AIRCRAFT PASSENGER를 골라요.",
      "required": true
     },
     {
      "label": "Are you an Overseas Filipino Worker?",
      "ko": "해외 필리핀 노동자(OFW) 여부",
      "how": "한국인 여행자는 No를 골라요.",
      "required": true
     }
    ]
   },
   {
    "title": "항공편 정보 (Flight Information)",
    "fields": [
     {
      "label": "Name of Airline",
      "ko": "항공사 이름",
      "how": "실제 타는 항공사를 골라요. 예: KOREAN AIR",
      "required": true
     },
     {
      "label": "Flight Number",
      "ko": "항공편 번호",
      "how": "항공권의 편명을 적어요. 예: KE621",
      "required": true
     },
     {
      "label": "Seat Number",
      "ko": "좌석 번호",
      "how": "요청되면 탑승권 좌석을 적어요. 예: 32A",
      "required": null
     }
    ]
   },
   {
    "title": "출발지·도착지 (Origin / Destination)",
    "fields": [
     {
      "label": "Country of Origin",
      "ko": "출발 국가",
      "how": "한국에서 출발하면 SOUTH KOREA를 골라요.",
      "required": true
     },
     {
      "label": "Airport of Arrival",
      "ko": "도착 공항",
      "how": "도착하는 필리핀 공항을 골라요. 예: Mactan-Cebu International Airport",
      "required": true
     },
     {
      "label": "Date of Arrival",
      "ko": "도착일",
      "how": "필리핀 도착 날짜를 골라요. 72시간(3일) 전부터 등록할 수 있어요.",
      "required": true
     },
     {
      "label": "Date of Return",
      "ko": "귀국(출국) 날짜",
      "how": "필리핀을 떠나는 날짜를 골라요.",
      "required": null
     }
    ]
   },
   {
    "title": "필리핀 도착 후 체류지 (Destination upon arrival in the Philippines)",
    "fields": [
     {
      "label": "Destination upon arrival",
      "ko": "도착 후 머무를 곳",
      "how": "호텔이면 Hotel을 골라요.",
      "required": true
     },
     {
      "label": "Hotel name",
      "ko": "호텔 이름",
      "how": "예약한 호텔을 검색해 영문으로 골라요. 예: Shangri-La Mactan Resort & Spa",
      "required": true
     }
    ]
   },
   {
    "title": "건강 신고 (Health Declaration)",
    "fields": [
     {
      "label": "Countries visited in the last 30 days",
      "ko": "최근 30일 방문 국가",
      "how": "최근 30일 동안 다녀온 나라가 있으면 골라요. 한국에만 있었다면 한국만 해당돼요.",
      "required": null
     },
     {
      "label": "Health status (symptoms / contact with sick persons)",
      "ko": "증상·감염병 환자 접촉 여부",
      "how": "해당 증상이나 접촉이 없으면 No를 골라요. Yes를 고르면 빨간 QR이 나와요.",
      "required": true
     }
    ]
   },
   {
    "title": "세관 신고 (Customs Declaration)",
    "fields": [
     {
      "label": "Custom Declaration",
      "ko": "세관 신고",
      "how": "신고할 물품(고액 현금 등)이 없으면 신고 없음을 골라요. 있으면 품목을 정확히 적어요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "가짜 eTravel 대행 사이트에서 돈을 내는 경우가 많아요. 공식 사이트는 etravel.gov.ph 하나이고 무료예요.",
   "First Name에 성까지 같이 쓰거나 성과 이름을 바꿔 넣는 실수가 잦아요. First=GILDONG, Last=HONG처럼 나눠 적어요.",
   "생년월일이 월/일/연도 순으로 나올 수 있어서 일과 월이 뒤바뀌기 쉬워요. 제출 전 요약 화면에서 꼭 확인해요.",
   "도착 72시간 전보다 일찍 등록하려다 막히거나, QR코드를 캡처하지 않아 공항에서 못 보여주는 경우가 있어요."
  ],
  "sources": [
   [
    "eTravel 공식 사이트(언어 선택 확인)",
    "https://etravel.gov.ph/"
   ],
   [
    "eTravel 공식 FAQ",
    "https://etravel.gov.ph/frequently-asked-questions"
   ],
   [
    "필리핀관광부 한국사무소 eTravel 안내",
    "https://philippinetourism.co.kr/travel/eTravel"
   ],
   [
    "교원투어 eTravel 작성 가이드(PDF)",
    "https://img-kyowontour.kyowontour.com/guide/etravel_v2.pdf"
   ],
   [
    "Tech Pilipinas eTravel 가이드",
    "https://techpilipinas.com/philippine-etravel-pass/"
   ]
  ],
  "confidence": "medium"
 },
 "malaysia": {
  "slug": "malaysia",
  "korean_ui": false,
  "korean_ui_note": "공식 등록 화면에 한국어 선택이 없어요. 영어로 작성해요.",
  "sections": [
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Name",
      "ko": "이름",
      "how": "여권에 적힌 영문 이름을 한 칸에 그대로 써요. 예: HONG GILDONG",
      "required": true
     },
     {
      "label": "Passport No.",
      "ko": "여권 번호",
      "how": "여권 번호를 공백 없이 입력해요. 예: M12345678",
      "required": true
     },
     {
      "label": "Date of Birth",
      "ko": "생년월일",
      "how": "달력에서 여권과 같은 생년월일을 골라요.",
      "required": true
     },
     {
      "label": "Nationality / Citizenship",
      "ko": "국적",
      "how": "목록에서 'KOR - REPUBLIC OF KOREA'를 골라요. PRK(북한)과 헷갈리지 마세요.",
      "required": true
     },
     {
      "label": "Place of Birth",
      "ko": "출생지",
      "how": "출생 국가를 골라요. 한국 출생이면 REPUBLIC OF KOREA를 선택해요.",
      "required": true
     },
     {
      "label": "Sex",
      "ko": "성별",
      "how": "MALE(남) 또는 FEMALE(여)을 골라요.",
      "required": true
     },
     {
      "label": "Date of Passport Expiry",
      "ko": "여권 만료일",
      "how": "여권에 적힌 만료일을 골라요. 입국일 기준 6개월 이상 남아 있어야 해요.",
      "required": true
     },
     {
      "label": "Email Address",
      "ko": "이메일 주소",
      "how": "확인 메일과 PIN을 받을 이메일을 써요. 예: gildong@naver.com",
      "required": true
     },
     {
      "label": "Confirm Email Address",
      "ko": "이메일 주소 확인",
      "how": "위와 같은 이메일을 한 번 더 입력해요.",
      "required": true
     },
     {
      "label": "Country / Region Code",
      "ko": "국가 번호",
      "how": "한국 휴대폰이면 +82를 골라요.",
      "required": true
     },
     {
      "label": "Mobile No.",
      "ko": "휴대폰 번호",
      "how": "맨 앞 0을 빼고 입력하는 게 안전해요. 예: 1012345678",
      "required": true
     }
    ]
   },
   {
    "title": "여행 정보 (Traveling Information)",
    "fields": [
     {
      "label": "Date of Arrival",
      "ko": "도착일",
      "how": "말레이시아 도착 날짜를 골라요. 제출일 포함 3일 이내 여행만 신청할 수 있어요.",
      "required": true
     },
     {
      "label": "Date of Departure",
      "ko": "출국일",
      "how": "말레이시아를 떠나는 날짜를 골라요.",
      "required": true
     },
     {
      "label": "Flight / Vessel / Transportation No.",
      "ko": "항공편/선박/교통편 번호",
      "how": "항공사 코드+숫자를 공백 없이 써요. 예: KE671, MH067",
      "required": true
     },
     {
      "label": "Mode of Travel",
      "ko": "교통수단",
      "how": "AIR(항공), LAND(육로), SEA(해상) 중에서 골라요. 비행기면 AIR예요.",
      "required": true
     },
     {
      "label": "Last Port of Embarkation before Malaysia",
      "ko": "말레이시아 도착 전 마지막 출발지",
      "how": "말레이시아로 오기 직전에 탄 곳을 골라요. 인천 직항이면 REPUBLIC OF KOREA, 싱가포르 경유면 SINGAPORE예요.",
      "required": true
     },
     {
      "label": "Accommodation of Stay",
      "ko": "숙소 유형",
      "how": "HOTEL/MOTEL/REST HOUSE, RESIDENCE OF FRIENDS/RELATIVES, OTHERS 중에서 골라요. 에어비앤비는 보통 OTHERS예요.",
      "required": true
     },
     {
      "label": "Address (In Malaysia)",
      "ko": "말레이시아 내 주소",
      "how": "숙소 이름과 주소를 영문·숫자로만 써요. 예: Hilton Kuala Lumpur, 3 Jalan Stesen Sentral",
      "required": true
     },
     {
      "label": "State",
      "ko": "주(州)",
      "how": "숙소가 있는 주를 골라요. 예: WILAYAH PERSEKUTUAN KUALA LUMPUR, SABAH",
      "required": true
     },
     {
      "label": "Postcode",
      "ko": "우편번호",
      "how": "숙소 우편번호 5자리를 써요. 예: 50470",
      "required": true
     },
     {
      "label": "City",
      "ko": "도시",
      "how": "숙소가 있는 도시를 골라요. 예: KUALA LUMPUR",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "이름을 성/이름 칸으로 나누는 줄 알고 순서를 바꾸는 경우가 있어요. 칸은 하나뿐이니 여권 표기 그대로 써요.",
   "국적에서 PRK(DEMOCRATIC PEOPLE'S REPUBLIC OF KOREA)를 잘못 고르는 실수가 있어요. KOR - REPUBLIC OF KOREA인지 꼭 확인해요.",
   "출발 1주일 전에 미리 하려다 막혀요. 도착 3일 이내(제출일 포함)에만 제출할 수 있어요.",
   "주소에 쉼표 외 특수문자나 한글을 넣으면 오류가 날 수 있어요. 영문·숫자로만 써요."
  ],
  "sources": [
   [
    "말레이시아 이민청 MDAC 공식 등록 화면",
    "https://imigresen-online.imi.gov.my/mdac/register"
   ],
   [
    "말레이시아 이민청 MDAC 메인",
    "https://imigresen-online.imi.gov.my/mdac/main"
   ],
   [
    "작성 후기(스크린샷, 보조)",
    "https://en.syfaganjarstory.com/how-to-fill-out-the-mdac/"
   ]
  ],
  "confidence": "high"
 },
 "singapore": {
  "slug": "singapore",
  "korean_ui": true,
  "korean_ui_note": "ICA SGAC e-Service에 한국어 번역(ko)이 있고, 기기 언어가 한국어면 '한국어로 전환' 안내가 떠요. 입력은 영어로 해요.",
  "sections": [
   {
    "title": "도착일 (Arrival Date)",
    "fields": [
     {
      "label": "Date of Arrival",
      "ko": "싱가포르 도착 날짜",
      "how": "화면에 나온 날짜 버튼 중 도착일을 골라요. 도착 3일 전부터 제출할 수 있어요.",
      "required": true
     }
    ]
   },
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Full Name (In Passport)",
      "ko": "성명(여권상)",
      "how": "안내 문구가 'Given name followed by Surname'(이름+성 순서)이에요. 예: GILDONG HONG",
      "required": true
     },
     {
      "label": "Passport Number",
      "ko": "여권 번호",
      "how": "여권 번호를 그대로 적어요. 예: M12345678",
      "required": true
     },
     {
      "label": "Date of Passport Expiry",
      "ko": "여권 만료일",
      "how": "DD/MM/YYYY(일/월/연도)로 적어요. 예: 20/06/2033",
      "required": true
     },
     {
      "label": "Sex as indicated in Passport",
      "ko": "여권상 성별",
      "how": "여권대로 MALE 또는 FEMALE을 골라요.",
      "required": true
     },
     {
      "label": "Date of Birth",
      "ko": "생년월일",
      "how": "DD/MM/YYYY로 적어요. 예: 20/06/1985",
      "required": true
     },
     {
      "label": "Nationality/Citizenship",
      "ko": "국적",
      "how": "목록에서 한국(KOREA, REPUBLIC OF / SOUTH KOREA로 표시)을 골라요.",
      "required": true
     },
     {
      "label": "Country/Place of Birth",
      "ko": "출생국/지역",
      "how": "대부분 한국을 골라요.",
      "required": true
     },
     {
      "label": "Place of Residence",
      "ko": "거주지",
      "how": "사는 나라로 한국을 골라요.",
      "required": true
     },
     {
      "label": "Email Address",
      "ko": "이메일 주소",
      "how": "확인 메일과 e-Pass를 받을 이메일을 적어요. 예: hong@naver.com",
      "required": true
     },
     {
      "label": "Country Code",
      "ko": "국가 코드",
      "how": "+82를 골라요.",
      "required": true
     },
     {
      "label": "Mobile Number",
      "ko": "휴대폰 번호",
      "how": "맨 앞 0을 빼고 적어요. 예: 1012345678",
      "required": true
     }
    ]
   },
   {
    "title": "여행 정보 (Trip Information)",
    "fields": [
     {
      "label": "Last City/Port of Embarkation before Singapore",
      "ko": "싱가포르 직전 출발 도시/항구",
      "how": "싱가포르로 오기 직전에 출발한 도시를 검색해 골라요. 예: 인천 출발이면 INCHEON",
      "required": true
     },
     {
      "label": "Purpose of Travel",
      "ko": "여행 목적",
      "how": "관광이면 Holiday/Sightseeing/Leisure를 골라요.",
      "required": true
     },
     {
      "label": "Date of Departure from Singapore",
      "ko": "싱가포르 출국일",
      "how": "DD/MM/YYYY로 적어요. 예: 19/10/2026",
      "required": true
     },
     {
      "label": "Next City/ Port of Disembarkation after Singapore",
      "ko": "싱가포르 다음 도착 도시/항구",
      "how": "귀국하면 INCHEON처럼 다음 목적지를 골라요. 같으면 'Same as Last City'를 체크해요.",
      "required": true
     },
     {
      "label": "Have you ever used a passport under different name to enter Singapore?",
      "ko": "다른 이름의 여권으로 싱가포르에 입국한 적이 있나요?",
      "how": "대부분 NO예요. 개명 전 여권으로 온 적이 있으면 YES 후 이전 이름을 적어요.",
      "required": true
     }
    ]
   },
   {
    "title": "건강 신고 (Health Declaration)",
    "fields": [
     {
      "label": "Do you currently have fever, cough, shortness of breath, headache, vomiting, dizziness or rash?",
      "ko": "현재 발열·기침·호흡곤란·두통·구토·어지럼·발진이 있나요?",
      "how": "증상이 없으면 NO를 골라요.",
      "required": true
     }
    ]
   },
   {
    "title": "교통편 (Transport)",
    "fields": [
     {
      "label": "Mode of Travel",
      "ko": "이동 수단",
      "how": "비행기면 Air를 골라요.",
      "required": true
     },
     {
      "label": "Mode of Transport",
      "ko": "교통 유형",
      "how": "일반 항공편이면 Commercial Flight를 골라요.",
      "required": true
     },
     {
      "label": "Flight Code",
      "ko": "항공사 코드",
      "how": "편명 앞 영문 2글자예요. 예: SQ607이면 SQ",
      "required": true
     },
     {
      "label": "Flight Number",
      "ko": "항공편 번호",
      "how": "편명 숫자만 적어요. 예: 607",
      "required": true
     }
    ]
   },
   {
    "title": "숙소 (Accommodation)",
    "fields": [
     {
      "label": "Type of Accommodation in Singapore",
      "ko": "싱가포르 숙소 유형",
      "how": "호텔이면 Hotel, 지인 집이면 Residential, 경유면 Transit, 당일치기면 Day Trip을 골라요.",
      "required": true
     },
     {
      "label": "Name of Hotel",
      "ko": "호텔 이름",
      "how": "목록에서 예약한 호텔을 골라요. 목록에 없으면 Specify Hotel Name에 영문으로 적어요. 예: Marina Bay Sands",
      "required": null
     },
     {
      "label": "Postal Code",
      "ko": "우편번호",
      "how": "Residential을 고르면 싱가포르 6자리 우편번호를 적어요. 예: 018956",
      "required": null
     },
     {
      "label": "Block Number",
      "ko": "블록 번호",
      "how": "Residential 주소의 블록/건물 번호를 적어요.",
      "required": null
     },
     {
      "label": "Street Name",
      "ko": "도로명",
      "how": "Residential 주소의 도로명을 영문으로 적어요.",
      "required": null
     },
     {
      "label": "Floor Number",
      "ko": "층",
      "how": "해당하면 층수를 적어요.",
      "required": null
     },
     {
      "label": "Unit Number",
      "ko": "호수",
      "how": "해당하면 호수를 적어요.",
      "required": null
     }
    ]
   },
   {
    "title": "검토·신고 (Review / Declaration)",
    "fields": [
     {
      "label": "I have read and agreed to the declaration.",
      "ko": "신고서 내용을 읽고 동의합니다",
      "how": "내용 확인 후 체크하고 제출해요. 받은 확인 메일을 저장해요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "Full Name 칸은 '이름 + 성' 순서(Given name followed by Surname)로 안내돼요. 한국식으로 HONG GILDONG만 고집하지 말고 안내대로 적되, 여권 철자는 그대로 써요.",
   "날짜가 DD/MM/YYYY라서 05/10을 5월 10일로 착각하기 쉬워요. 10월 5일이라는 뜻이에요.",
   "'SG Arrival Card' 이름을 쓴 유료 대행 사이트가 많아요. 공식은 ICA 사이트(eservices.ica.gov.sg)나 MyICA 앱이고 무료예요.",
   "Last City/Port에 경유지가 아닌 출발지를 넣는 실수가 있어요. 싱가포르로 오기 직전에 탑승한 도시를 골라요."
  ],
  "sources": [
   [
    "ICA SGAC 공식 e-Service(방문객 양식)",
    "https://eservices.ica.gov.sg/arrivalcard/sgac/fvipa/submit"
   ],
   [
    "ICA SGAC 공식 첫 화면",
    "https://eservices.ica.gov.sg/arrivalcard/sgac"
   ],
   [
    "VisaTraveler SGAC 작성 가이드",
    "https://www.visatraveler.com/visa/fill-sg-arrival-card-online/"
   ]
  ],
  "confidence": "high"
 },
 "indonesia": {
  "slug": "indonesia",
  "korean_ui": "unknown",
  "korean_ui_note": "출처마다 달라요. 공식 관광청은 인니어·영어·중국어만 안내하고, 한국어도 있다는 보도도 있어요. 영어로 작성하는 걸 전제로 해요.",
  "sections": [
   {
    "title": "시작 (Arrival Card)",
    "fields": [
     {
      "label": "Foreign Visitor",
      "ko": "외국인 방문객",
      "how": "입국카드 서비스에서 Foreign Visitor(외국인 방문객)를 골라요. 한국 여권이면 이걸 선택해요.",
      "required": true
     }
    ]
   },
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Passport Number",
      "ko": "여권 번호",
      "how": "여권 번호를 공백 없이 입력해요. Scan MRZ로 여권 하단을 찍으면 자동 입력돼요. 예: M12345678",
      "required": true
     },
     {
      "label": "Full Name",
      "ko": "전체 이름",
      "how": "여권 영문 이름 그대로 써요. 예: HONG GILDONG",
      "required": true
     },
     {
      "label": "Nationality",
      "ko": "국적",
      "how": "여권 발급 국가로 KOREA, REPUBLIC OF(대한민국)를 골라요.",
      "required": true
     },
     {
      "label": "Date of Birth",
      "ko": "생년월일",
      "how": "여권과 같은 생년월일을 달력에서 골라요.",
      "required": true
     },
     {
      "label": "Place of Birth",
      "ko": "출생지",
      "how": "출생 국가나 도시를 써요. 예: SEOUL 또는 KOREA, REPUBLIC OF",
      "required": null
     },
     {
      "label": "Gender",
      "ko": "성별",
      "how": "Male(남) 또는 Female(여)을 골라요.",
      "required": true
     },
     {
      "label": "Passport Expiry Date",
      "ko": "여권 만료일",
      "how": "여권 만료일을 골라요. 입국일 기준 6개월 이상 남아 있어야 해요.",
      "required": true
     },
     {
      "label": "Mobile Number",
      "ko": "휴대폰 번호",
      "how": "국가번호 +82를 고르고 맨 앞 0을 빼서 써요. 예: 1012345678",
      "required": null
     },
     {
      "label": "Email",
      "ko": "이메일",
      "how": "QR코드를 받을 이메일을 써요. 인증 코드(OTP)가 올 수 있어요. 예: gildong@naver.com",
      "required": true
     },
     {
      "label": "Add Traveller",
      "ko": "동행자 추가",
      "how": "가족·일행을 같은 신청에 추가할 수 있어요. 한 명씩 여권 정보를 넣어요.",
      "required": false
     }
    ]
   },
   {
    "title": "여행 정보 (Travel Details)",
    "fields": [
     {
      "label": "Arrival Date",
      "ko": "인도네시아 도착일",
      "how": "인도네시아 도착 날짜를 골라요. 도착 3일 전부터 작성할 수 있어요.",
      "required": true
     },
     {
      "label": "Departure Date",
      "ko": "인도네시아 출국일",
      "how": "인도네시아를 떠나는 날짜를 골라요.",
      "required": true
     },
     {
      "label": "Do you have a Visa or KITAS/KITAP?",
      "ko": "비자·체류허가 보유 여부",
      "how": "미리 받은 e-VOA(도착비자)·e-Visa가 있으면 Yes로 하고 번호를 써요. 없으면 No로 해요.",
      "required": true
     },
     {
      "label": "Visa Number",
      "ko": "비자 번호",
      "how": "Yes를 고른 경우에만 e-VOA/e-Visa 번호를 써요.",
      "required": false
     }
    ]
   },
   {
    "title": "교통수단·체류지 (Mode of Transport and Address in Indonesia)",
    "fields": [
     {
      "label": "Mode of Transport",
      "ko": "교통수단",
      "how": "AIR(항공) 또는 SEA(해상)를 골라요. 비행기면 AIR예요.",
      "required": true
     },
     {
      "label": "Purpose of Travel",
      "ko": "여행 목적",
      "how": "관광이면 Holiday / Sightseeing / Leisure 같은 항목을 골라요.",
      "required": true
     },
     {
      "label": "Place of Arrival",
      "ko": "도착 공항·항구",
      "how": "도착 공항을 골라요. 예: DPS – I Gusti Ngurah Rai Airport(발리), CGK(자카르타)",
      "required": true
     },
     {
      "label": "Type of Air Transport",
      "ko": "항공 운송 유형",
      "how": "정기 항공편이면 Commercial Flight를 골라요.",
      "required": true
     },
     {
      "label": "Flight Name",
      "ko": "항공사",
      "how": "타고 오는 항공사를 골라요. 예: Korean Air, Garuda Indonesia",
      "required": true
     },
     {
      "label": "Flight Number",
      "ko": "항공편 번호",
      "how": "항공사 코드+숫자로 써요. 예: KE629, GA871",
      "required": true
     },
     {
      "label": "Residence Type",
      "ko": "숙소 유형",
      "how": "호텔이면 Hotel을 골라요. 빌라·지인 집 등은 해당 항목이나 Others를 골라요.",
      "required": true
     },
     {
      "label": "Name of Hotel",
      "ko": "호텔 이름",
      "how": "목록에서 호텔을 검색해 골라요. 안 나오면 Others로 하고 영문 이름·주소를 직접 써요.",
      "required": true
     },
     {
      "label": "Nearest Immigration Office",
      "ko": "가까운 이민국 사무소",
      "how": "숙소 위치에 따라 자동 입력되거나 목록에서 골라요. 발리 남부면 보통 Ngurah Rai 사무소예요.",
      "required": null
     }
    ]
   },
   {
    "title": "신고 (Declaration: 건강·검역·세관)",
    "fields": [
     {
      "label": "Countries visited in the last 21 days",
      "ko": "최근 21일 내 방문국",
      "how": "최근 21일간 머문 나라를 골라요. 한국에서 바로 왔다면 KOREA, REPUBLIC OF만 넣어요.",
      "required": true
     },
     {
      "label": "Health declaration (symptoms)",
      "ko": "건강 상태 질문",
      "how": "발열·기침 등 증상이 있는지 물어요. 증상이 없으면 No를 골라요.",
      "required": true
     },
     {
      "label": "Quarantine declaration (animals, fish, plants and their products)",
      "ko": "검역 질문",
      "how": "동물·식물·과일·씨앗·육가공품 등을 가져오는지 물어요. 김치·육포 등 해당하면 솔직하게 Yes로 해요.",
      "required": true
     },
     {
      "label": "Number of baggage arriving with you",
      "ko": "동반 수하물 개수",
      "how": "부치는 짐과 들고 타는 짐을 합한 개수를 숫자로 써요. 예: 2",
      "required": true
     },
     {
      "label": "Customs declaration (goods)",
      "ko": "세관 신고 질문",
      "how": "면세 한도를 넘는 술·담배·현금(1억 루피아 상당 이상)·상품 등을 묻는 질문이에요. 해당 없으면 No예요.",
      "required": true
     },
     {
      "label": "IMEI registration (mobile devices)",
      "ko": "휴대기기 IMEI 등록",
      "how": "현지에서 쓸 휴대폰·태블릿을 새로 들여오는 경우 묻는 항목이에요. 일반 단기 여행자는 보통 해당 없음으로 해요.",
      "required": null
     }
    ]
   }
  ],
  "pitfalls": [
   "e-VOA(도착비자)와 관광세(Levy)를 이 카드로 냈다고 착각해요. 입국카드와 별개라서 따로 처리해야 해요.",
   "도착 3일보다 일찍 작성하려다 날짜가 막혀요. 도착 3일 전부터 작성해요.",
   "가족이 각각 따로 하거나 대표자만 하고 끝내요. Add Traveller로 동행자를 모두 넣어 각자 QR이 나왔는지 확인해요.",
   "반찬·육포를 가져가면서 검역 질문에 모두 No를 눌러요. 해당 물품이 있으면 Yes로 신고해요."
  ],
  "sources": [
   [
    "인도네시아 관광청 All Indonesia 안내",
    "https://www.indonesia.travel/gb/en/general-information/all-indonesia-app"
   ],
   [
    "카라왕 이민사무소 등록 안내(인니어)",
    "https://karawang.imigrasi.go.id/begini-tata-cara-registrasi-aplikasi-all-indonesia-untuk-pengajuan-kartu-kedatangan/"
   ],
   [
    "WOAH 아시아 사무소 안내 PDF",
    "https://rr-asia.woah.org/app/uploads/2025/09/2025-09-All-Indonesia-Arrival-Card-Guide.pdf"
   ],
   [
    "단계별 작성 가이드(스크린샷, 보조)",
    "https://travelution.com.my/how-to-fill-the-all-indonesia-arrival-card"
   ],
   [
    "바탐 리조트 작성 안내(보조)",
    "https://telunasresorts.com/all-indonesia-app/"
   ],
   [
    "작성 가이드(보조)",
    "https://visa-indonesia.com/visas-and-regulations/indonesia-all-arrival-card-guide/"
   ],
   [
    "한국어 작성 후기(보조)",
    "https://saikno.com/%EB%B0%9C%EB%A6%AC-%EC%98%AC%EC%9D%B8%EB%8F%84%EB%84%A4%EC%8B%9C%EC%95%84all-indonesia-%EC%9E%91%EC%84%B1%EB%B0%A9%EB%B2%95-%EC%9E%85%EA%B5%AD-%EC%A4%80%EB%B9%84%EC%84%9C%EB%A5%98/"
   ]
  ],
  "confidence": "medium"
 },
 "guam": {
  "slug": "guam",
  "korean_ui": true,
  "korean_ui_note": "화면 위 SELECT LANGUAGE에서 영어·일본어·한국어(Korean 한국어)·번체 중국어를 고를 수 있어요. 단, 내용은 영어로 입력해야 해요.",
  "sections": [
   {
    "title": "개인 정보 (Personal Information)",
    "fields": [
     {
      "label": "Passport No./Travel ID",
      "ko": "여권 번호/여행 신분증",
      "how": "여권 번호를 그대로 적어요. 예: M12345678",
      "required": true
     },
     {
      "label": "Country of Issuance",
      "ko": "발급 국가",
      "how": "여권을 발급한 나라로 한국을 골라요(예: Korea, Republic of).",
      "required": true
     },
     {
      "label": "First",
      "ko": "이름",
      "how": "여권 영문 이름을 적어요. 예: GILDONG",
      "required": true
     },
     {
      "label": "Middle",
      "ko": "중간 이름",
      "how": "한국인은 보통 비워 둬요.",
      "required": false
     },
     {
      "label": "Last",
      "ko": "성",
      "how": "여권 영문 성을 적어요. 예: HONG",
      "required": true
     },
     {
      "label": "Arrival Date – to Guam",
      "ko": "괌 도착일",
      "how": "괌에 도착하는 날짜를 골라요. 도착 72시간 전부터 작성할 수 있어요.",
      "required": true
     }
    ]
   },
   {
    "title": "도착 정보 (Arrival Information)",
    "fields": [
     {
      "label": "Airline/Vessel",
      "ko": "항공사/선박",
      "how": "타고 가는 항공사를 골라요. 예: Korean Air",
      "required": true
     },
     {
      "label": "Flight/Voyage No.",
      "ko": "항공편/항해 번호",
      "how": "항공사 선택 후 나오면 편명을 적어요. 예: KE111",
      "required": null
     },
     {
      "label": "Originating From (country from which you started your journey)",
      "ko": "출발 국가(여정을 시작한 나라)",
      "how": "한국에서 출발했다면 한국을 골라요. 경유했더라도 처음 출발한 나라예요.",
      "required": true
     },
     {
      "label": "Originating From (city from which you started your journey)",
      "ko": "출발 도시",
      "how": "처음 출발한 도시를 영문으로 적어요. 예: Seoul 또는 Busan",
      "required": false
     }
    ]
   },
   {
    "title": "주 거주지 (Primary Place of Residence - country/city)",
    "fields": [
     {
      "label": "Country",
      "ko": "국가",
      "how": "사는 나라를 골라요. 목록의 'Korea'를 골라요.",
      "required": true
     },
     {
      "label": "Date of Birth (DD / MM / YYYY)",
      "ko": "생년월일",
      "how": "일(DD)·월(MM)·연도(YYYY)를 각각 골라요. 예: 20 / 06 / 1985",
      "required": true
     },
     {
      "label": "Gender",
      "ko": "성별",
      "how": "여권과 같은 성별을 골라요.",
      "required": true
     },
     {
      "label": "Address/Hotel Name (while on Guam)",
      "ko": "괌 체류 주소/호텔 이름",
      "how": "묵을 호텔 이름을 영문으로 적어요. 예: Dusit Thani Guam Resort",
      "required": true
     },
     {
      "label": "Status",
      "ko": "신분",
      "how": "여행객은 Visitor를 골라요. 괌을 거쳐 다른 곳으로 가면 Transiting이에요.",
      "required": true
     },
     {
      "label": "Total family members (including yourself) traveling with you",
      "ko": "함께 여행하는 가족 수(본인 포함)",
      "how": "본인을 포함한 숫자예요. 혼자면 1, 부부면 2를 골라요. 가족은 1장만 내면 돼요.",
      "required": true
     }
    ]
   },
   {
    "title": "세관 신고 (I am (We are) bringing to Guam:)",
    "fields": [
     {
      "label": "Controlled substances (prescription or otherwise)",
      "ko": "규제 약물(처방약 포함)",
      "how": "해당 약물을 가져가면 Yes, 아니면 No를 골라요.",
      "required": true
     },
     {
      "label": "Firearms (personal owned)",
      "ko": "총기(개인 소유)",
      "how": "대부분 No예요.",
      "required": true
     },
     {
      "label": "Explosives (commercial or consumer grade to include fireworks)",
      "ko": "폭발물(불꽃놀이 포함)",
      "how": "폭죽 등이 없으면 No를 골라요.",
      "required": true
     },
     {
      "label": "Animals or parts of animals or articles manufactured from wildlife",
      "ko": "동물·동물 부위·야생동물 제품",
      "how": "해당 물품이 없으면 No를 골라요.",
      "required": true
     },
     {
      "label": "Animal products including meats, milk or eggs",
      "ko": "육류·우유·계란 등 동물성 제품",
      "how": "육포, 햄, 계란 등을 가져가면 Yes로 신고해요.",
      "required": true
     },
     {
      "label": "Plants or parts of plants, including fresh fruits, vegetables, seeds flowers, or articles made of plant materials",
      "ko": "식물·과일·채소·씨앗·식물 제품",
      "how": "생과일, 채소, 씨앗이 있으면 Yes로 신고해요.",
      "required": true
     },
     {
      "label": "Soil materials or samples, or biological specimens",
      "ko": "흙·생물 표본",
      "how": "대부분 No예요.",
      "required": true
     },
     {
      "label": "Live Service Animal",
      "ko": "살아있는 보조견(서비스 동물)",
      "how": "보조견을 동반하면 Yes를 골라요.",
      "required": true
     },
     {
      "label": "More than five (5) cartons of cigarettes (1,000 cigarettes) or twelve (12) packages of other tobacco products",
      "ko": "담배 5보루(1,000개비) 또는 기타 담배 12갑 초과",
      "how": "면세 한도를 넘게 가져가면 Yes를 골라요.",
      "required": true
     },
     {
      "label": "More than one (1) U.S. gallon/3.7 liters of alcoholic beverage per adult",
      "ko": "성인 1인당 주류 1갤런(3.7L) 초과",
      "how": "소주·와인 합계가 3.7L를 넘으면 Yes를 골라요.",
      "required": true
     },
     {
      "label": "I have (We have) currency of monetary instruments over $10,000 USD or foreign equivalent",
      "ko": "미화 1만 달러 상당 초과 현금·유가증권",
      "how": "가족 합산 1만 달러를 넘으면 Yes를 골라요.",
      "required": true
     },
     {
      "label": "I have (We have) commercial merchandise (goods for resale)",
      "ko": "상업용 물품(판매용)",
      "how": "판매할 물건이 없으면 No를 골라요.",
      "required": true
     },
     {
      "label": "VISITORS - The total value of all articles that will remain in Guam (commercial merchandise only; goods for resale) is: (US$)",
      "ko": "방문객 - 괌에 남길 상업용 물품 총액(미화)",
      "how": "판매용 물품이 없으면 0을 적어요.",
      "required": null
     },
     {
      "label": "Description of Goods:",
      "ko": "물품 설명",
      "how": "앞에서 Yes를 고른 경우 어떤 물건인지 영어로 적어요. 예: Beef jerky 2 packs",
      "required": null
     }
    ]
   },
   {
    "title": "방문객 정보 (Visitor Information)",
    "fields": [
     {
      "label": "Primary reason for this trip",
      "ko": "이번 여행의 주된 목적",
      "how": "관광이면 휴가/관광에 해당하는 항목을 골라요.",
      "required": null
     },
     {
      "label": "This trip to Guam is my:",
      "ko": "이번 괌 방문은",
      "how": "처음인지 재방문인지에 맞게 골라요.",
      "required": null
     },
     {
      "label": "Travel Arrangements were made through a:",
      "ko": "여행 예약 경로",
      "how": "여행사 패키지인지 개별 예약인지 골라요.",
      "required": null
     },
     {
      "label": "Did you book your travel arrangements online?",
      "ko": "온라인으로 예약했나요?",
      "how": "Yes 또는 No를 골라요.",
      "required": null
     },
     {
      "label": "Length of stay",
      "ko": "체류 기간",
      "how": "괌에 머무는 기간(일수)을 적어요. 예: 4",
      "required": null
     },
     {
      "label": "Where will you stay while on Guam (mark all that apply)",
      "ko": "괌 체류 숙소 유형(해당 모두 선택)",
      "how": "호텔이면 Hotel을 체크해요.",
      "required": null
     },
     {
      "label": "Email",
      "ko": "이메일",
      "how": "선택 항목이에요. 괌관광청 소식을 받고 싶을 때만 적어요.",
      "required": false
     },
     {
      "label": "Mobile Phone Number",
      "ko": "휴대폰 번호",
      "how": "선택 항목이에요. 원할 때만 적어요.",
      "required": false
     }
    ]
   },
   {
    "title": "서약 (Certification Statement)",
    "fields": [
     {
      "label": "I CERTIFY THAT I HAVE READ AND UNDERSTAND THE REQUIREMENTS...",
      "ko": "서약 확인",
      "how": "내용을 읽고 체크한 뒤 제출해요. 받은 QR코드를 저장하거나 캡처해요.",
      "required": true
     }
    ]
   }
  ],
  "pitfalls": [
   "가족 여행인데 가족 수(Total family members)에 본인을 빼고 적는 경우가 많아요. 본인 포함 숫자예요.",
   "라면 스프·육포·김치 속 고기류처럼 육류 성분이 든 음식을 신고하지 않으면 압수나 벌금 대상이 될 수 있어요. 애매하면 Yes로 신고해요.",
   "Originating From에 경유지(예: 일본)를 적는 실수가 있어요. 여정을 처음 시작한 나라(한국)를 골라요.",
   "QR코드를 저장하지 않으면 입국 심사 때 다시 작성해야 할 수 있어요. 제출 직후 캡처해요."
  ],
  "sources": [
   [
    "괌 EDF 공식 양식(항목·언어 확인)",
    "https://guamedf.landing.cards/"
   ],
   [
    "괌 세관검역청(CQA)",
    "https://cqa.guam.gov/"
   ],
   [
    "괌관광청 EDF 모바일 안내",
    "https://www.guamvisitorsbureau.com/news/news-releases/mobile-access-to-electronic-declaration-form-launched.html"
   ]
  ],
  "confidence": "medium"
 }
}```

## 첨부: countries.json
```
{
 "verified": "2026-10-05",
 "regions": [
  {
   "key": "east-asia",
   "label": "동북아시아"
  },
  {
   "key": "southeast-asia",
   "label": "동남아시아"
  },
  {
   "key": "resort",
   "label": "괌·팔라우·몰디브"
  },
  {
   "key": "longhaul",
   "label": "뉴질랜드·캐나다"
  }
 ],
 "countries": [
  {
   "slug": "japan",
   "name": "일본",
   "flag": "🇯🇵",
   "region": "east-asia",
   "form": "비지트 재팬 웹 입국·세관 사전등록 (Visit Japan Web)",
   "form_short": "Visit Japan Web",
   "url": "https://services.digital.go.jp/en/visit-japan-web/",
   "domain": "digital.go.jp",
   "mandatory": "선택",
   "fee": "무료",
   "window": {
    "type": "anytime",
    "ref": "departure",
    "value": null
   },
   "window_text": "출발 전 언제든지 (도착 6시간 전까지 완료 권장)",
   "result": "입국심사·세관신고용 QR코드가 나와요. 공항 입국심사대와 세관(또는 통합 키오스크)에서 여권과 함께 QR을 보여주면 돼요.",
   "status": "일본 디지털청이 운영하는 공식 서비스예요. 종이 입국카드·세관신고서도 아직 쓸 수 있어 의무는 아니지만, 등록하면 줄을 덜 서요.",
   "needs": [
    "여권 정보",
    "항공편명·도착일",
    "일본 내 숙소 주소·전화번호",
    "이메일 주소",
    "세관 신고 항목 답변(휴대품 등)"
   ],
   "steps": [
    "Visit Japan Web 공식 사이트에서 이메일로 계정을 만들어요.",
    "본인 정보에 여권을 촬영하거나 직접 입력해 등록해요.",
    "입국·귀국 예정 등록에서 항공편과 숙소를 입력해요.",
    "입국심사 정보와 세관 신고 정보를 각각 등록해요.",
    "QR코드를 캡처해 두고 공항에서 보여줘요."
   ],
   "tips": [
    "일본 단기 관광(90일 이내)은 한국인 무비자라 따로 낼 돈이 없어요. Visit Japan Web 대행이라며 돈을 받는 사이트는 공식이 아니에요.",
    "기내에서 급하게 하지 말고 도착 몇 시간 전까지 미리 끝내 두세요. 공항 와이파이가 느릴 수 있으니 QR은 캡처해 두면 좋아요.",
    "동반 가족(아이 포함)은 한 계정에서 '동반가족'으로 함께 등록할 수 있어요."
   ],
   "faq": [
    [
     "꼭 해야 하나요?",
     "의무는 아니에요. 종이 입국카드와 세관신고서를 써도 되지만, 미리 등록하면 더 빨라요."
    ],
    [
     "QR코드는 몇 개인가요?",
     "입국심사와 세관이 하나의 QR로 합쳐져 있어요. 공항에 따라 두 곳에서 같은 QR을 보여줘요."
    ],
    [
     "한 번 등록하면 다음 여행에도 쓸 수 있나요?",
     "계정과 본인 정보는 남아 있어서, 다음 여행 때는 일정만 새로 등록하면 돼요."
    ]
   ],
   "sources": [
    [
     "일본 디지털청 Visit Japan Web 안내",
     "https://services.digital.go.jp/en/visit-japan-web/"
    ],
    [
     "일본 디지털청 정책 페이지",
     "https://www.digital.go.jp/en/policies/visit_japan_web"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": null,
   "code": "NRT"
  },
  {
   "slug": "taiwan",
   "name": "대만",
   "flag": "🇹🇼",
   "region": "east-asia",
   "form": "대만 온라인 입국신고서 (Taiwan Arrival Card, TWAC)",
   "form_short": "TWAC",
   "url": "https://twac.immigration.gov.tw",
   "domain": "immigration.gov.tw",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "days",
    "ref": "arrival",
    "value": 3
   },
   "window_text": "도착 3일 전부터",
   "result": "제출하면 확인 메일이 와요. 따로 출력할 필요는 없고, 입국심사 때 여권만 내면 돼요.",
   "status": "2025년 10월 1일부터 외국인 방문객은 종이 대신 온라인 입국신고서(TWAC)를 꼭 제출해야 해요. 안 하면 입국심사를 받을 수 없어요.",
   "needs": [
    "여권 정보",
    "항공편명·도착일",
    "대만 내 숙소 주소",
    "방문 목적",
    "이메일 주소"
   ],
   "steps": [
    "대만 이민서 TWAC 공식 사이트에 접속해요.",
    "언어를 고르고 여권 정보를 입력해요.",
    "항공편, 숙소, 방문 목적을 입력해요.",
    "제출 후 확인 메일을 받아 두세요."
   ],
   "tips": [
    "한국인은 무비자로 90일까지 머물 수 있어요. 공식 사이트는 무료이니 돈을 받는 대행 사이트는 피하세요.",
    "제출 후에도 공식 사이트에서 조회·수정할 수 있어요.",
    "깜빡했다면 출발 공항이나 도착 공항에 붙은 QR코드로도 작성할 수 있어요."
   ],
   "faq": [
    [
     "종이 입국카드는 이제 없나요?",
     "네, 2025년 10월부터 온라인 작성이 원칙이에요."
    ],
    [
     "언제 작성하나요?",
     "도착 3일 전부터 작성할 수 있어요."
    ],
    [
     "잘못 입력했어요.",
     "공식 사이트에서 조회 후 수정하면 돼요."
    ]
   ],
   "sources": [
    [
     "대만 내정부 이민서 공지(TWAC 전면 시행)",
     "https://www.immigration.gov.tw/5385/7229/7238/398036/"
    ],
    [
     "대만 내정부 보도자료",
     "https://www.moi.gov.tw/News_Content.aspx?n=4&s=329018"
    ],
    [
     "TWAC 공식 사이트",
     "https://twac.immigration.gov.tw"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": "Asia/Taipei",
   "code": "TPE"
  },
  {
   "slug": "china",
   "name": "중국",
   "flag": "🇨🇳",
   "region": "east-asia",
   "form": "중국 외국인 입국카드 온라인 작성 (Online Arrival Card, NIA)",
   "form_short": "중국 온라인 입국카드",
   "url": "https://s.nia.gov.cn/ArrivalCardFillingPC/",
   "domain": "nia.gov.cn",
   "mandatory": "선택",
   "fee": "무료",
   "window": {
    "type": "anytime",
    "ref": "departure",
    "value": null
   },
   "window_text": "출발 전 언제든지",
   "result": "작성을 마치면 입국 정보가 미리 등록돼요. 입국심사 때 여권을 내면 돼요(화면을 캡처해 두면 좋아요).",
   "status": "2025년 11월 20일부터 중국 국가이민관리국이 온라인 입국카드 작성을 시작했어요. 종이 입국카드도 계속 쓸 수 있어요.",
   "needs": [
    "여권 정보",
    "항공편명·도착일",
    "중국 내 숙소 주소",
    "방문 목적",
    "비자 정보(무비자면 해당 없음)"
   ],
   "steps": [
    "국가이민관리국 공식 사이트, '移民局12367' 앱, 위챗·알리페이 미니프로그램 중 하나로 접속해요.",
    "외국인 입국카드 작성 메뉴를 골라요.",
    "여권, 항공편, 숙소 정보를 입력하고 제출해요.",
    "완료 화면을 캡처해 두세요."
   ],
   "tips": [
    "한국인은 2026년 12월 31일까지 관광 목적 30일 무비자 입국이 가능해요(정책 연장 여부는 출발 전 확인).",
    "국가이민관리국이 공식 사이트를 사칭한 가짜 사이트를 주의하라고 안내했어요. nia.gov.cn 주소인지 꼭 확인하세요.",
    "온라인으로 못 했다면 공항에서 QR을 찍어 작성하거나 종이 카드를 쓰면 돼요."
   ],
   "faq": [
    [
     "꼭 온라인으로 해야 하나요?",
     "아니에요. 선택이고, 종이 입국카드도 그대로 있어요."
    ],
    [
     "단체비자로 가요.",
     "단체비자 소지자는 입국카드 작성 대상에서 빠져요."
    ],
    [
     "돈이 드나요?",
     "공식 채널은 무료예요."
    ]
   ],
   "sources": [
    [
     "중국 국가이민관리국 정책 해설",
     "https://en.nia.gov.cn/n147418/n147463/c191530/content.html"
    ],
    [
     "주뉴욕 중국 총영사관 공지",
     "https://newyork.china-consulate.gov.cn/eng/tzgg/202512/t20251202_11764520.htm"
    ],
    [
     "베이징시 외사판공실 안내",
     "https://wb.beijing.gov.cn/home/index/wsjx/202511/t20251124_4301517.html"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": null,
   "code": "PEK"
  },
  {
   "slug": "vietnam",
   "sources": [
    [
     "베트남 출입국관리국 사전 입국신고",
     "https://prearrival.immigration.gov.vn/"
    ]
   ],
   "name": "베트남",
   "flag": "🇻🇳",
   "form": "사전 입국신고 (Pre-Arrival Information)",
   "form_short": "사전 입국신고",
   "url": "https://prearrival.immigration.gov.vn/",
   "domain": "prearrival.immigration.gov.vn",
   "window": {
    "type": "hours",
    "value": 72,
    "ref": "arrival"
   },
   "window_text": "도착 72시간 전부터",
   "tz_label": "베트남 시간 기준 (한국보다 2시간 느림)",
   "result": "제출 후 이메일로 QR코드 발송 → 입국심사 때 제시",
   "status": "호치민 떤선녓 공항은 2026년 4월 15일부터 의무. 다른 공항으로 확대 중이라 출발 전 공식 사이트에서 확인하세요.",
   "needs": [
    "여권",
    "항공편명",
    "베트남 숙소 주소",
    "방문 목적"
   ],
   "steps": [
    "공식 사이트 prearrival.immigration.gov.vn에 접속해요. 오른쪽 위에서 한국어를 고를 수 있어요.",
    "'Create & Submit'을 누르고 자동입력 방지 문자(CAPTCHA)를 입력해요.",
    "국적에서 'Republic of Korea'를 고르고 여권·연락처를 입력해요.",
    "비자 종류(무비자는 Unilateral exemption)와 항공편·숙소를 입력해요.",
    "확인 후 제출하고, 이메일로 온 QR코드를 저장해 입국심사 때 보여줘요."
   ],
   "tips": [
    "72시간보다 일찍 신청하면 접수되지 않아요.",
    "전자비자(e-Visa)는 별도 절차예요. 무비자 체류 기간을 넘기면 비자가 따로 필요해요.",
    "'vietnam-arrival-card' 같은 이름의 유료 대행 사이트가 많아요. 주소가 .gov.vn으로 끝나는지 확인하세요."
   ],
   "faq": [
    [
     "베트남 입국신고는 돈을 내야 하나요?",
     "아니에요. 베트남 출입국관리국 공식 사이트에서 무료예요. 결제를 요구하면 대행 사이트예요."
    ],
    [
     "언제 신청할 수 있나요?",
     "도착 예정 시각 기준 72시간 전부터 신청할 수 있어요."
    ],
    [
     "안 하면 입국이 거부되나요?",
     "의무 적용 공항에서는 미제출 시 입국심사가 지연될 수 있어요. 미리 제출하는 것이 안전해요."
    ]
   ],
   "mandatory": "의무 (일부 공항)",
   "fee": "무료",
   "confidence": "high",
   "region": "southeast-asia",
   "iana": "Asia/Ho_Chi_Minh",
   "code": "SGN"
  },
  {
   "slug": "thailand",
   "sources": [
    [
     "태국 이민국 TDAC",
     "https://tdac.immigration.go.th/"
    ]
   ],
   "name": "태국",
   "flag": "🇹🇭",
   "form": "태국 디지털 입국카드 (TDAC)",
   "form_short": "TDAC",
   "url": "https://tdac.immigration.go.th/",
   "domain": "tdac.immigration.go.th",
   "window": {
    "type": "hours",
    "value": 72,
    "ref": "arrival"
   },
   "window_text": "도착 72시간(3일) 전부터",
   "tz_label": "태국 시간 기준 (한국보다 2시간 느림)",
   "result": "제출 후 확인서(QR) 발급 → 저장해 두었다가 입국 시 제시",
   "status": "2025년 5월 1일부터 시행. 종이 입국카드(TM6)를 대체해요.",
   "needs": [
    "여권",
    "항공편명",
    "태국 숙소 주소",
    "최근 방문 국가",
    "건강 상태"
   ],
   "steps": [
    "공식 사이트 tdac.immigration.go.th 접속",
    "여권 정보와 연락처 입력",
    "항공편, 숙소, 여행 일정 입력",
    "최근 방문 국가와 건강 상태 신고",
    "제출 후 확인서(QR)를 저장 → 입국 시 제시"
   ],
   "tips": [
    "TDAC는 비자나 입국허가가 아니에요. 입국 절차를 간소화하는 신고서예요.",
    "태국 이민국이 '돈을 받는 가짜 TDAC 사이트'를 공식 경고했어요.",
    "주소가 .go.th로 끝나는지 확인하세요."
   ],
   "faq": [
    [
     "TDAC는 유료인가요?",
     "아니에요. 태국 이민국 공식 사이트에서 무료예요."
    ],
    [
     "언제 신청할 수 있나요?",
     "도착 전 72시간(3일) 이내에 신청해요."
    ],
    [
     "TDAC가 비자인가요?",
     "아니에요. 입국카드를 온라인으로 바꾼 것이며, 비자 요건은 별도로 확인해야 해요."
    ]
   ],
   "mandatory": "의무",
   "fee": "무료",
   "confidence": "high",
   "region": "southeast-asia",
   "iana": "Asia/Bangkok",
   "code": "BKK"
  },
  {
   "slug": "philippines",
   "sources": [
    [
     "eTravel 공식 FAQ",
     "https://etravel.gov.ph/frequently-asked-questions"
    ]
   ],
   "name": "필리핀",
   "flag": "🇵🇭",
   "form": "필리핀 eTravel",
   "form_short": "eTravel",
   "url": "https://etravel.gov.ph/",
   "domain": "etravel.gov.ph",
   "window": {
    "type": "hours",
    "value": 72,
    "ref": "arrival"
   },
   "window_text": "도착 72시간(3일) 전부터",
   "tz_label": "필리핀 시간 기준 (한국보다 1시간 느림)",
   "result": "QR코드 발급 (초록 = 정상, 빨강 = 정보 누락·확인 필요) → 탑승 전 항공사, 입국 시 제시",
   "status": "외국인 입국자 대상 시행 중. 비행기 탑승 전 항공사 직원이 QR코드를 확인해요.",
   "needs": [
    "여권",
    "항공편명",
    "필리핀 숙소 주소",
    "건강 상태"
   ],
   "steps": [
    "공식 사이트 etravel.gov.ph 접속",
    "여행 구분(입국)과 여권 정보 입력",
    "항공편, 숙소, 일정 입력",
    "건강 신고 후 제출",
    "QR코드 저장 → 탑승 수속과 입국심사 때 제시"
   ],
   "tips": [
    "공식 FAQ에 '등록은 완전히 무료이며 온라인 결제가 없다'고 명시돼 있어요.",
    "QR이 빨간색이면 입력 정보를 다시 확인하세요.",
    "주소가 .gov.ph로 끝나는지 확인하세요. etravel이 들어간 비슷한 유료 사이트가 있어요."
   ],
   "faq": [
    [
     "eTravel 등록비가 있나요?",
     "없어요. 공식 사이트 FAQ에 무료라고 명시돼 있어요."
    ],
    [
     "언제 등록하나요?",
     "필리핀 도착 72시간 전부터 등록할 수 있어요."
    ],
    [
     "QR이 빨간색으로 나왔어요.",
     "정보가 불완전하거나 건강 관련 확인이 필요한 경우예요. 입력 내용을 수정하세요."
    ]
   ],
   "mandatory": "의무",
   "fee": "무료",
   "confidence": "high",
   "region": "southeast-asia",
   "iana": "Asia/Manila",
   "code": "MNL"
  },
  {
   "slug": "malaysia",
   "sources": [
    [
     "말레이시아 이민국 MDAC",
     "https://imigresen-online.imi.gov.my/mdac/main"
    ]
   ],
   "name": "말레이시아",
   "flag": "🇲🇾",
   "form": "말레이시아 디지털 입국카드 (MDAC)",
   "form_short": "MDAC",
   "url": "https://imigresen-online.imi.gov.my/mdac/main",
   "domain": "imigresen-online.imi.gov.my",
   "window": {
    "type": "days",
    "value": 3,
    "ref": "arrival"
   },
   "window_text": "도착 3일 전부터",
   "tz_label": "말레이시아 시간 기준 (한국보다 1시간 느림)",
   "result": "제출 후 이메일로 확인 메일 발송 → 저장해 두었다가 입국 시 제시",
   "status": "대부분의 외국인 방문객 대상 시행 중. 비자를 대신하지는 않아요.",
   "needs": [
    "여권",
    "항공편명",
    "말레이시아 숙소 주소",
    "이메일"
   ],
   "steps": [
    "공식 사이트 imigresen-online.imi.gov.my/mdac 접속",
    "여권 정보와 이메일 입력",
    "항공편, 입국 날짜, 숙소 입력",
    "제출 후 확인 메일 저장",
    "입국심사 때 제시"
   ],
   "tips": [
    "가짜 MDAC 사이트가 최대 80달러를 받은 사례가 있어요.",
    "주소가 imi.gov.my로 끝나는지 확인하세요."
   ],
   "faq": [
    [
     "MDAC는 유료인가요?",
     "아니에요. 말레이시아 이민국 공식 사이트에서 무료예요."
    ],
    [
     "언제 제출하나요?",
     "도착 3일 전부터 제출할 수 있어요."
    ]
   ],
   "mandatory": "의무",
   "fee": "무료",
   "confidence": "high",
   "region": "southeast-asia",
   "iana": "Asia/Kuala_Lumpur",
   "code": "KUL"
  },
  {
   "slug": "singapore",
   "sources": [
    [
     "ICA SG Arrival Card 안내",
     "https://www.ica.gov.sg/enter-transit-depart/entering-singapore/sg-arrival-card"
    ]
   ],
   "name": "싱가포르",
   "flag": "🇸🇬",
   "form": "SG 입국카드 (SG Arrival Card)",
   "form_short": "SG Arrival Card",
   "url": "https://www.ica.gov.sg/eservicesandforms/sgarrivalcard",
   "domain": "ica.gov.sg",
   "window": {
    "type": "days",
    "value": 3,
    "ref": "arrival"
   },
   "window_text": "도착일 포함 3일 전부터",
   "tz_label": "싱가포르 시간 기준 (한국보다 1시간 느림)",
   "result": "제출 후 확인 메일 발송. 전자 건강신고가 함께 포함돼요.",
   "status": "모든 입국자 대상 시행 중. 공식 MyICA 앱으로도 제출할 수 있어요.",
   "needs": [
    "여권",
    "항공편명",
    "싱가포르 숙소 주소",
    "건강 상태"
   ],
   "steps": [
    "ICA 공식 사이트(ica.gov.sg) 또는 MyICA 앱 접속",
    "여권 정보 입력",
    "항공편, 숙소, 일정 입력",
    "전자 건강신고 작성 후 제출",
    "확인 메일 저장"
   ],
   "tips": [
    "ICA 공식 안내: 'SGAC 제출은 무료'.",
    "도착일을 포함해 3일 이내에만 제출할 수 있어요. 예를 들어 10일 도착이면 8일부터 가능해요.",
    "주소가 ica.gov.sg인지 확인하세요."
   ],
   "faq": [
    [
     "SG Arrival Card는 유료인가요?",
     "아니에요. ICA 공식 안내에 무료라고 명시돼 있어요."
    ],
    [
     "언제 제출하나요?",
     "도착일을 포함해 3일 이내예요. 10일 도착이면 8일부터 제출할 수 있어요."
    ]
   ],
   "mandatory": "의무",
   "fee": "무료",
   "confidence": "high",
   "region": "southeast-asia",
   "iana": "Asia/Singapore",
   "code": "SIN"
  },
  {
   "slug": "indonesia",
   "name": "인도네시아",
   "flag": "🇮🇩",
   "region": "southeast-asia",
   "form": "올 인도네시아 입국신고서 (All Indonesia Arrival Card)",
   "form_short": "All Indonesia",
   "url": "https://allindonesia.imigrasi.go.id",
   "domain": "imigrasi.go.id",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "days",
    "ref": "arrival",
    "value": 3
   },
   "window_text": "도착 3일 전부터",
   "result": "QR코드가 나와요. 공항이나 항구에서 입국심사·세관 때 보여주면 돼요.",
   "status": "2025년 10월 1일부터 해외에서 들어오는 여행자는 의무로 작성해야 해요. 입국·세관·검역·건강 신고가 하나로 합쳐졌어요(자카르타, 발리, 수라바야 공항, 바탐 항구 등).",
   "needs": [
    "여권 정보",
    "항공편명·도착일",
    "인도네시아 내 숙소 주소",
    "세관 신고 항목 답변",
    "건강 상태 답변"
   ],
   "steps": [
    "All Indonesia 공식 사이트나 앱에 접속해요.",
    "여권 정보와 항공편을 입력해요.",
    "세관·건강 질문에 답하고 제출해요.",
    "받은 QR코드를 저장해 두세요."
   ],
   "tips": [
    "한국인은 관광 시 도착비자(VOA, 유료)가 필요해요. 공식 전자비자 사이트(evisa.imigrasi.go.id)에서 미리 받을 수 있어요.",
    "발리는 별도로 관광세(외국인 관광객 부과금)를 내야 해요. 발리주 공식 사이트에서 내세요.",
    "입국카드 작성은 무료예요. 수수료를 받는 대행 사이트는 공식이 아니에요."
   ],
   "faq": [
    [
     "가족도 각자 해야 하나요?",
     "한 사람씩 작성해야 해요. 한 계정에서 동반자를 추가할 수 있는지는 화면 안내를 확인하세요."
    ],
    [
     "도착비자와 같은 건가요?",
     "아니에요. 입국카드는 무료 신고이고, 비자(VOA)는 따로 돈을 내고 받아요."
    ],
    [
     "너무 일찍 작성하면요?",
     "도착 3일 전부터만 작성할 수 있어요."
    ]
   ],
   "sources": [
    [
     "All Indonesia 공식 사이트(인도네시아 이민국)",
     "https://allindonesia.imigrasi.go.id"
    ],
    [
     "인도네시아 전자비자(VOA) 공식 사이트",
     "https://evisa.imigrasi.go.id"
    ]
   ],
   "confidence": "medium",
   "tz_label": "발리 시간 기준 (자카르타는 1시간 느림)",
   "iana": "Asia/Makassar",
   "code": "DPS"
  },
  {
   "slug": "cambodia",
   "name": "캄보디아",
   "flag": "🇰🇭",
   "region": "southeast-asia",
   "form": "캄보디아 전자 입국신고서 (Cambodia e-Arrival)",
   "form_short": "Cambodia e-Arrival",
   "url": "https://arrival.gov.kh",
   "domain": "arrival.gov.kh",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "days",
    "ref": "arrival",
    "value": 7
   },
   "window_text": "도착 7일 전부터",
   "result": "QR코드가 나와요. 휴대폰에 저장하거나 출력해서 입국심사 때 보여주면 돼요.",
   "status": "모든 여행자가 도착 7일 이내에 제출해야 해요. 종이 입국카드·건강신고서·세관신고서를 하나로 대신해요.",
   "needs": [
    "여권 정보",
    "비자 정보(또는 도착비자 예정)",
    "항공편명·도착일",
    "캄보디아 내 숙소 주소",
    "세관·건강 질문 답변"
   ],
   "steps": [
    "Cambodia e-Arrival 공식 사이트나 앱에 접속해요.",
    "여권과 여행 정보를 입력해요.",
    "건강·세관 질문에 답하고 제출해요.",
    "QR코드를 저장하거나 출력해 두세요."
   ],
   "tips": [
    "한국인은 관광비자(유료)가 필요해요. 도착비자나 캄보디아 공식 전자비자(evisa.gov.kh)로 받을 수 있어요.",
    "'캄보디아 입국카드'를 대행해 준다며 돈을 받는 사이트가 많아요. 공식 주소는 arrival.gov.kh예요.",
    "출력본도 함께 챙기면 휴대폰 배터리가 없을 때 좋아요."
   ],
   "faq": [
    [
     "돈을 내야 하나요?",
     "e-Arrival 작성은 무료예요. 비자는 따로 내요."
    ],
    [
     "언제 하나요?",
     "도착 7일 이내에 하면 돼요."
    ],
    [
     "종이 카드도 쓰나요?",
     "e-Arrival이 종이 입국·건강·세관 서류를 대신해요."
    ]
   ],
   "sources": [
    [
     "캄보디아 관광부 e-Arrival 안내",
     "https://www.tourismcambodia.com/tripplanner/essential-information/cambodia-e-arrival-card.htm"
    ],
    [
     "Cambodia e-Arrival 공식 사이트",
     "https://arrival.gov.kh"
    ]
   ],
   "confidence": "medium",
   "tz_label": "현지 시간 기준",
   "iana": "Asia/Phnom_Penh",
   "code": "PNH"
  },
  {
   "slug": "guam",
   "name": "괌",
   "flag": "🇬🇺",
   "region": "resort",
   "form": "괌 전자 세관신고서 (Guam Electronic Declaration Form, EDF)",
   "form_short": "괌 EDF",
   "url": "https://guamedf.landing.cards/",
   "domain": "guamedf.landing.cards",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "hours",
    "ref": "arrival",
    "value": 72
   },
   "window_text": "괌 도착 72시간 전부터",
   "result": "제출하면 QR코드가 발급돼요. 짐을 찾은 뒤 세관 검사대에서 QR코드(휴대폰 화면 또는 출력본)를 보여주세요.",
   "status": "2021년 도입된 세관·보건 통합 전자신고서로, 2025년 2월 4일부터 종이 신고서가 폐지되어 모든 도착 승객(또는 가족 대표 1명)이 작성해야 해요. 미리 못 했다면 공항 수하물 찾는 곳의 키오스크에서 작성할 수 있어요.",
   "needs": [
    "여권 정보",
    "항공편명과 도착일",
    "괌 숙소 이름·주소",
    "동반 가족 정보(가족 대표 작성 시)",
    "휴대품 정보(음식, 현금, 면세 초과 물품 등)",
    "이메일 주소"
   ],
   "steps": [
    "괌 세관검역청(cqa.guam.gov)에 연결된 공식 EDF 페이지에 접속해요.",
    "도착 72시간 이내에 여권·항공편·숙소 정보를 입력해요.",
    "세관·보건 질문에 답하고 제출해요.",
    "발급된 QR코드를 캡처하거나 저장해요.",
    "도착 후 짐을 찾고 세관에서 QR코드를 보여줘요."
   ],
   "tips": [
    "가족은 대표 1명이 함께 작성할 수 있어요.",
    "공식 신고는 무료예요. 'Guam EDF 신청'을 내세워 돈을 받는 대행 사이트에 주의하세요. 괌 세관검역청(cqa.guam.gov)에 걸린 링크로 들어가는 것이 안전해요.",
    "한국인은 무비자 입국 시 2024년 11월 29일부터 미국 CBP의 G-CNMI ETA(현재 무료, 출발 5일 전 이상 신청 권장) 또는 ESTA가 필요해요."
   ],
   "faq": [
    [
     "ESTA가 있으면 EDF는 안 해도 되나요?",
     "아니에요. ESTA/G-CNMI ETA는 입국 허가이고, EDF는 별도의 세관신고서라 둘 다 필요해요."
    ],
    [
     "휴대폰이 없으면 어떻게 하나요?",
     "괌 공항 수하물 찾는 곳의 키오스크에서 작성할 수 있어요. 다만 줄이 길 수 있으니 미리 작성하세요."
    ],
    [
     "미국 세관신고서(6059B)도 써야 하나요?",
     "괌은 자체 EDF를 사용해요. 출발 전 항공사 안내도 함께 확인하세요."
    ]
   ],
   "sources": [
    [
     "괌 세관검역청 공식 링크",
     "https://cqa.guam.gov/"
    ],
    [
     "괌정부관광청 입출국 안내",
     "https://www.visitguam.com/about-guam/entry-and-exit-formalities/"
    ],
    [
     "괌정부관광청 EDF 도입 발표",
     "https://www.guamvisitorsbureau.com/news/news-releases/guam-goes-digital-with-launch-of-electronic-declaration-form.html"
    ],
    [
     "미 연방관보 G-CNMI ETA 규정",
     "https://www.federalregister.gov/documents/2024/01/18/2024-00645/guam-commonwealth-of-the-northern-mariana-islands-cnmi-visa-waiver-program-automation-and-electronic"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": "Pacific/Guam",
   "official_basis": "괌 세관검역청(cqa.guam.gov) 홈페이지가 이 주소를 공식 신고서로 직접 링크하고 있어요.",
   "code": "GUM"
  },
  {
   "slug": "palau",
   "name": "팔라우",
   "flag": "🇵🇼",
   "region": "resort",
   "form": "팔라우 입국신고서 (Palau Entry Form)",
   "form_short": "팔라우 입국신고서",
   "url": "https://palautravel.pw/",
   "domain": "palautravel.pw",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "hours",
    "ref": "departure",
    "value": 72
   },
   "window_text": "팔라우행 출발 72시간 전부터",
   "result": "제출하면 이메일로 QR코드가 와요. 탑승 수속 때와 팔라우 공항 도착 때 QR코드(휴대폰 화면 또는 출력본)를 보여주세요.",
   "status": "팔라우 세관국경보호국(BCBP)은 2024년 2월 1일부터 입국신고서를 출발 72시간 이내에 온라인으로 제출하도록 안내해요. 모든 방문객이 대상이에요.",
   "needs": [
    "여권 정보",
    "생년월일",
    "항공편 정보",
    "팔라우 숙소 정보",
    "동반 가족 정보(가족 1건 작성 시)",
    "이메일 주소"
   ],
   "steps": [
    "공식 사이트(palautravel.pw)에 접속해요.",
    "출발 72시간 이내에 여권·항공편·숙소 정보를 영어로 입력해요.",
    "가족이면 한 신청서에 함께 넣어 제출해요.",
    "이메일로 온 QR코드를 저장하거나 출력해요.",
    "체크인과 도착 심사 때 QR코드를 보여줘요."
   ],
   "tips": [
    "가족 또는 1인당 1건만 작성하면 되고, 답변은 영어로 써야 해요.",
    "이 신고서는 무료예요. 돈을 받는 사이트는 사기일 수 있다고 호주 정부도 경고해요.",
    "한국인은 도착 시 30일 관광 비자를 받을 수 있어요. 환경보호세(Pristine Paradise Environmental Fee)는 보통 항공권에 포함돼요."
   ],
   "faq": [
    [
     "72시간 기준이 출발인가요, 도착인가요?",
     "팔라우 세관국경보호국은 '출발 72시간 이내'로, 일부 공식 안내는 '도착 72시간 이내'로 적고 있어요. 출발 72시간 안에 작성하면 두 조건을 모두 맞출 수 있어요."
    ],
    [
     "QR코드를 못 받았어요.",
     "스팸함을 확인하고, 그래도 없으면 다시 제출하거나 팔라우 세관국경보호국(immigration@bcbp.pw)에 문의하세요."
    ]
   ],
   "sources": [
    [
     "팔라우 국제공항 입국 요건",
     "https://www.palau-airport.com/entry-requirements"
    ],
    [
     "팔라우 세관국경보호국(BCBP)",
     "https://bcbp.pw/?page_id=159"
    ],
    [
     "팔라우관광청 입국 요건",
     "https://pristineparadisepalau.com/travel-entry-requirements/"
    ],
    [
     "호주 정부 Smartraveller 팔라우",
     "https://www.smartraveller.gov.au/destinations/pacific/palau"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": null,
   "official_basis": "팔라우 국제공항과 팔라우관광청이 이 주소를 공식 입국 양식으로 안내해요. 팔라우 세관국경보호국(bcbp.pw)도 같은 양식을 안내하지만 페이지에서 주소를 직접 확인하지는 못했어요.",
   "code": "ROR"
  },
  {
   "slug": "maldives",
   "name": "몰디브",
   "flag": "🇲🇻",
   "region": "resort",
   "form": "몰디브 여행자 신고서 (IMUGA Traveller Declaration)",
   "form_short": "IMUGA",
   "url": "https://imuga.immigration.gov.mv/",
   "domain": "immigration.gov.mv",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "hours",
    "ref": "arrival",
    "value": 96
   },
   "window_text": "도착 96시간(4일) 전부터",
   "result": "제출하면 QR코드가 메일로 와요. 입국심사 때 여권과 함께 보여주면 돼요.",
   "status": "몰디브에 오는 모든 외국인은 도착 96시간 이내에 여행자 신고서를 제출해야 해요. 입국·세관·건강 신고가 하나로 합쳐져 있어요.",
   "needs": [
    "여권 정보",
    "항공편명·도착일",
    "숙소(리조트·호텔) 예약 정보",
    "세관·건강 질문 답변",
    "이메일 주소"
   ],
   "steps": [
    "IMUGA 공식 사이트에 접속해요.",
    "도착 신고(Arrival)를 골라 여권 정보를 입력해요.",
    "항공편·숙소·세관 질문을 입력하고 제출해요.",
    "메일로 받은 QR코드를 저장해 두세요."
   ],
   "tips": [
    "몰디브는 관광객에게 도착 시 무료 관광비자를 줘요. 숙소 예약 확인서를 꼭 챙기세요.",
    "'IMUGA 대행'이라며 돈을 받는 사이트가 많아요. 공식은 imuga.immigration.gov.mv이고 무료예요.",
    "출국 신고는 현재 필요 없다고 알려져 있어요."
   ],
   "faq": [
    [
     "돈이 드나요?",
     "아니요, 제출은 무료예요."
    ],
    [
     "언제 하나요?",
     "도착 96시간(4일) 이내에 하면 돼요."
    ],
    [
     "리조트가 대신 해 주나요?",
     "리조트가 도와주기도 하지만, 본인이 직접 공식 사이트에서 하면 돼요."
    ]
   ],
   "sources": [
    [
     "몰디브 이민청 관광비자 안내",
     "https://www.immigration.gov.mv/visa/tourist-visa"
    ],
    [
     "IMUGA 공식 사이트",
     "https://imuga.immigration.gov.mv/"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": "Indian/Maldives",
   "code": "MLE"
  },
  {
   "slug": "new-zealand",
   "name": "뉴질랜드",
   "flag": "🇳🇿",
   "region": "longhaul",
   "form": "뉴질랜드 여행자 신고서 (New Zealand Traveller Declaration, NZTD)",
   "form_short": "NZTD",
   "url": "https://www.travellerdeclaration.govt.nz/",
   "domain": "travellerdeclaration.govt.nz",
   "mandatory": "의무",
   "fee": "무료",
   "window": {
    "type": "hours",
    "ref": "departure",
    "value": 24
   },
   "window_text": "뉴질랜드행 여정 출발 24시간 전부터",
   "result": "제출하면 이메일로 참조번호와 입국 안내를 받아요. 신고 내용은 여권에 연결되므로 도착 시 이게이트(eGate)나 심사관에게 여권만 보여주시면 돼요.",
   "status": "2023년 8월부터 종이 입국카드(Passenger Arrival Card)를 대체했으며, 항공·크루즈로 입국하는 모든 사람(시민 포함)이 작성해야 해요. 온라인 작성이 어려운 경우에만 도착 시 종이 양식을 쓸 수 있어요.",
   "needs": [
    "여권 정보",
    "뉴질랜드 내 연락처·숙소 주소",
    "최근 30일 여행 국가",
    "항공편 정보",
    "휴대품 정보(음식, 등산·캠핑 장비, 의약품, 술·담배 등)",
    "NZeTA 또는 비자 정보",
    "이메일 주소"
   ],
   "steps": [
    "공식 사이트(travellerdeclaration.govt.nz) 또는 공식 NZTD 앱에 접속해요.",
    "출발 24시간 전이 되면 신고를 시작하고, 이메일로 받은 참조번호를 보관해요.",
    "여권·항공편·연락처와 휴대품(특히 음식물) 질문에 영어로 답해요.",
    "제출 후 입국 안내 이메일을 확인해요.",
    "도착하면 이게이트 또는 심사대에서 여권을 제시해요."
   ],
   "tips": [
    "가족 단위가 아니라 아기·어린이를 포함해 1인당 1건씩 작성해야 해요.",
    "공식 신고는 무료예요. 수수료를 받는 대행 사이트는 공식 사이트가 아니에요.",
    "한국인은 별도로 전자여행허가 NZeTA(유료, 앱 기준 NZD 17부터)와 국제관광세 IVL(NZD 100)이 필요해요. 처리에 최대 72시간이 걸릴 수 있으니 미리 신청하세요."
   ],
   "faq": [
    [
     "NZTD와 NZeTA는 같은 건가요?",
     "아니에요. NZeTA는 사전 입국허가(유료)이고, NZTD는 무료 입국·세관 신고서예요. 둘 다 필요해요."
    ],
    [
     "질문이 한국어로 나오나요?",
     "질문은 여러 언어로 볼 수 있지만 답변은 영어로 입력해야 해요."
    ],
    [
     "음식을 가져가도 되나요?",
     "가져갈 수는 있지만 반드시 신고해야 해요. 신고하지 않으면 벌금이 부과될 수 있어요."
    ]
   ],
   "sources": [
    [
     "NZTD 공식 사이트",
     "https://www.travellerdeclaration.govt.nz/"
    ],
    [
     "NZTD 작성 안내",
     "https://www.travellerdeclaration.govt.nz/completing-your-declaration/"
    ],
    [
     "뉴질랜드 관세청 NZTD 안내",
     "https://www.customs.govt.nz/about-us/new-zealand-traveller-declaration"
    ],
    [
     "뉴질랜드 이민성 NZeTA",
     "https://www.immigration.govt.nz/visas/new-zealand-electronic-travel-authority-nzeta/"
    ]
   ],
   "confidence": "high",
   "tz_label": "현지 시간 기준",
   "iana": null,
   "code": "AKL"
  },
  {
   "slug": "canada",
   "name": "캐나다",
   "flag": "🇨🇦",
   "region": "longhaul",
   "form": "어라이브캔 사전 세관·입국 신고 (ArriveCAN Advance Declaration)",
   "form_short": "ArriveCAN",
   "url": "https://arrivecan.cbsa-asfc.cloud-nuage.canada.ca/en/welcome",
   "domain": "canada.ca",
   "mandatory": "선택",
   "fee": "무료",
   "window": {
    "type": "hours",
    "ref": "arrival",
    "value": 72
   },
   "window_text": "도착 72시간 전부터",
   "result": "제출이 끝나면 앱·웹에 확인 화면이 나와요. 공항 키오스크나 eGate에서 여권만 스캔하면 미리 낸 신고 내용이 자동으로 불러와져요.",
   "status": "캐나다 국경서비스청(CBSA)의 공식 서비스예요. 토론토·밴쿠버·몬트리올·캘거리 등 주요 국제공항에서 쓸 수 있고, 안 해도 공항 키오스크에서 신고할 수 있어 선택 사항이에요.",
   "needs": [
    "여권 정보",
    "항공편명·도착 공항·도착일",
    "동반 가족 정보(같은 집 거주자 최대 8명)",
    "세관 신고 항목 답변(면세 한도 초과 물품, 현금 1만 캐나다달러 이상 등)"
   ],
   "steps": [
    "ArriveCAN 앱을 설치하거나 공식 웹사이트에 접속해요.",
    "도착 72시간 이내에 '사전 신고(Advance Declaration)'를 선택해요.",
    "여권 정보와 도착 공항·항공편을 입력해요.",
    "세관 질문에 답하고 제출해요.",
    "도착 후 키오스크나 eGate에서 여권을 스캔해 확인해요."
   ],
   "tips": [
    "한국인은 캐나다에 항공으로 입국할 때 전자여행허가(eTA, 7 캐나다달러)가 별도로 필요해요. eTA는 ArriveCAN과 다른 서류이니 출발 전 공식 사이트(canada.ca)에서 꼭 받아 두세요.",
    "제출 후 72시간 안에 공항에서 확인하지 않으면 신고가 만료돼요. 일정이 바뀌면 다시 제출하세요.",
    "ArriveCAN은 무료예요. eTA·ArriveCAN을 대신 해준다며 수수료를 받는 사이트는 공식이 아니에요."
   ],
   "faq": [
    [
     "꼭 해야 하나요?",
     "아니요. 공항 키오스크에서 바로 신고해도 돼요. 미리 하면 대기 시간이 줄어요."
    ],
    [
     "모든 공항에서 되나요?",
     "주요 국제공항에서만 쓸 수 있어요. 도착 공항이 대상인지 앱에서 공항을 고를 때 확인하세요."
    ],
    [
     "eTA를 받았는데 또 해야 하나요?",
     "eTA는 입국 허가, ArriveCAN은 세관·입국 신고라 서로 달라요. ArriveCAN은 선택이에요."
    ]
   ],
   "sources": [
    [
     "캐나다 국경서비스청 – 사전 신고 방법",
     "https://www.canada.ca/en/border-services-agency/services/arrivecan/declaration.html"
    ],
    [
     "캐나다 정부 – ArriveCAN 안내",
     "https://www.canada.ca/en/mobile/arrivecan.html"
    ]
   ],
   "confidence": "high",
   "tz_label": "토론토 시간 기준 (밴쿠버는 3시간 느림)",
   "iana": "America/Toronto",
   "code": "YYZ"
  }
 ]
}```
