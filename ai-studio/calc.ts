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
