// 입국노트 — 신청 시작 시각 계산기, 캘린더 알림, 체크리스트, 나라 검색
(function () {
  var pad = function (n) { return String(n).padStart(2, "0"); };
  var HOUR = 3600000;

  // 특정 시간대에서 ms 시점의 UTC 대비 오프셋(ms)
  function tzOffset(ms, tz) {
    var f = new Intl.DateTimeFormat("en-US", {
      timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", second: "2-digit"
    });
    var p = {};
    f.formatToParts(new Date(ms)).forEach(function (x) { p[x.type] = x.value; });
    return Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute, +p.second) - Math.floor(ms / 1000) * 1000;
  }
  // 현지 벽시계 시각 → UTC ms
  function zoned(y, mo, d, h, mi, tz) {
    var guess = Date.UTC(y, mo, d, h, mi);
    var u = guess - tzOffset(guess, tz);
    return guess - tzOffset(u, tz);
  }
  function fmt(ms, tz) {
    var o = { month: "long", day: "numeric", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" };
    if (tz) o.timeZone = tz;
    return new Intl.DateTimeFormat("ko-KR", o).format(new Date(ms));
  }
  function remain(ms) {
    var m = Math.round(ms / 60000);
    var d = Math.floor(m / 1440), h = Math.floor((m % 1440) / 60), mm = m % 60;
    var out = [];
    if (d) out.push(d + "일");
    if (h) out.push(h + "시간");
    if (!d && mm) out.push(mm + "분");
    return out.join(" ") || "곧";
  }

  // 기준 시각(ref) 계산: arrival = 현지 시간대, departure = 이 기기 시간대
  function base(c, p, t) {
    if (c.ref === "arrival" && c.iana) return zoned(p[0], p[1] - 1, p[2], t[0], t[1], c.iana);
    return new Date(p[0], p[1] - 1, p[2], t[0], t[1]).getTime();
  }
  function shift(c, rule, p, t, b) {
    if (rule.type === "hours") return b - rule.value * HOUR;
    if (rule.type === "days") {
      if (rule.ref === "arrival" && c.iana) {
        // 도착일 포함 N일: 확실히 접수되는 날짜(도착일 0시 기준 N-1일 전)
        return zoned(p[0], p[1] - 1, p[2] - (rule.value - 1), 0, 0, c.iana);
      }
      return b - rule.value * 24 * HOUR;
    }
    return null;
  }

  function calc(c, dateStr, timeStr) {
    var p = dateStr.split("-").map(Number);
    var t = (timeStr || "12:00").split(":").map(Number);
    var b = base(c, p, t);
    var r = { base: b, open: null, deadline: null };
    if (c.wtype !== "anytime") r.open = shift(c, { type: c.wtype, value: c.wval, ref: c.ref }, p, t, b);
    if (c.dl) {
      var db = c.dl.ref === c.ref ? b : null;
      if (db !== null) r.deadline = shift(c, c.dl, p, t, db);
    }
    return r;
  }

  function icsDate(ms) {
    var d = new Date(ms);
    return d.getUTCFullYear() + pad(d.getUTCMonth() + 1) + pad(d.getUTCDate()) + "T" +
      pad(d.getUTCHours()) + pad(d.getUTCMinutes()) + "00Z";
  }
  function downloadIcs(c, ms, label) {
    var lines = [
      "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ipguknote//KO", "CALSCALE:GREGORIAN",
      "BEGIN:VEVENT",
      "UID:" + c.slug + "-" + ms + "@ipguknote",
      "DTSTAMP:" + icsDate(Date.now()),
      "DTSTART:" + icsDate(ms),
      "DTEND:" + icsDate(ms + 1800000),
      "SUMMARY:" + c.name + " " + c.form + " " + label,
      "DESCRIPTION:공식 사이트에서 직접 신청하세요: " + c.url,
      "URL:" + c.url,
      "BEGIN:VALARM", "TRIGGER:PT0M", "ACTION:DISPLAY", "DESCRIPTION:" + c.name + " 입국신고 " + label, "END:VALARM",
      "END:VEVENT", "END:VCALENDAR"
    ];
    var blob = new Blob([lines.join("\r\n")], { type: "text/calendar;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = c.slug + "-입국신고-알림.ics";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }

  function readCountry(el) {
    var d = el.dataset;
    return {
      slug: d.slug, name: d.name, form: d.form, url: d.url, iana: d.iana || "",
      ref: d.ref, wtype: d.wtype, wval: Number(d.wval), tzlabel: d.tzlabel,
      dl: d.dl ? JSON.parse(d.dl) : null
    };
  }

  document.querySelectorAll("[data-calc]").forEach(function (box) {
    var sel = box.querySelector("select");
    var date = box.querySelector("input[type=date]");
    var time = box.querySelector("input[type=time]");
    var out = box.querySelector(".calc-out");
    var labels = box.querySelectorAll("[data-reflabel]");
    var anyNote = box.querySelector(".calc-anytime");
    var fields = box.querySelector(".calc-fields");
    var last = null;

    function current() { return readCountry(sel ? sel.options[sel.selectedIndex] : box); }

    function relabel(c) {
      var word = c.ref === "arrival" ? "도착" : "출발";
      var where = c.ref === "arrival" ? "현지" : "출발 공항 현지";
      labels.forEach(function (l) { l.textContent = word + " " + l.dataset.reflabel + " (" + where + ")"; });
      var noCalc = c.wtype === "anytime" && !c.dl;
      if (anyNote) anyNote.hidden = !noCalc;
      if (fields) fields.hidden = noCalc;
      if (noCalc) out.hidden = true;
    }

    function run() {
      var c = current();
      relabel(c);
      if (!date.value || (c.wtype === "anytime" && !c.dl)) { out.hidden = true; return; }
      var r = calc(c, date.value, time.value);
      last = { c: c, r: r };
      var now = Date.now();
      var showTz = c.ref === "arrival" && c.iana;
      var state;
      if (now >= r.base) state = '<p class="badge badge-gray">' + (c.ref === "arrival" ? "도착" : "출발") + ' 시각이 이미 지났어요</p>';
      else if (r.deadline !== null && now > r.deadline) state = '<p class="badge badge-red">신청 마감 시각이 지났어요</p>';
      else if (r.open === null || now >= r.open) state = '<p class="badge badge-green">지금 바로 신청할 수 있어요</p>';
      else state = '<p class="badge badge-amber">' + remain(r.open - now) + " 뒤부터 신청 가능</p>";

      var rows = "";
      if (r.open !== null) {
        if (showTz) {
          rows += "<dt>신청 시작 (현지)</dt><dd>" + fmt(r.open, c.iana) + "</dd>";
          rows += "<dt>신청 시작 (한국 시간)</dt><dd><strong>" + fmt(r.open, "Asia/Seoul") + "</strong></dd>";
        } else {
          rows += "<dt>신청 시작</dt><dd><strong>" + fmt(r.open) + "</strong></dd>";
        }
      }
      if (r.deadline !== null) {
        rows += "<dt>신청 마감" + (showTz ? " (한국 시간)" : "") + "</dt><dd><strong>" +
          fmt(r.deadline, showTz ? "Asia/Seoul" : null) + "</strong></dd>";
      }
      rows += "<dt>" + (c.ref === "arrival" ? "도착" : "출발") + "</dt><dd>" + fmt(r.base, showTz ? c.iana : null) + "</dd>";
      var note = showTz ? c.tzlabel + "으로 계산했어요." : "출발 공항 현지 시각 기준이에요. 한국에서 출발하면 한국 시간 그대로 보면 돼요.";
      var btn = r.open !== null ? '<button type="button" class="btn btn-ghost" data-ics="open">시작 알림 추가</button>'
        : r.deadline !== null ? '<button type="button" class="btn btn-ghost" data-ics="deadline">마감 알림 추가</button>' : "";
      out.innerHTML = state + '<dl class="calc-dl">' + rows + "</dl>" +
        '<p class="calc-note">' + note + "</p>" +
        '<div class="calc-actions">' + btn +
        '<a class="btn btn-primary" href="' + c.url + '" target="_blank" rel="noopener">공식 사이트 열기</a></div>';
      out.hidden = false;
    }

    out.addEventListener("click", function (e) {
      var b = e.target.closest("[data-ics]");
      if (!b || !last) return;
      if (b.dataset.ics === "open") downloadIcs(last.c, last.r.open, "신청 시작");
      else downloadIcs(last.c, last.r.deadline - 6 * HOUR, "신청 마감 6시간 전");
    });
    [date, time].forEach(function (el) { el.addEventListener("input", run); });
    if (sel) sel.addEventListener("change", run);
    relabel(current());
  });

  // 나라 검색
  var q = document.getElementById("country-search");
  if (q) {
    q.addEventListener("input", function () {
      var v = q.value.trim().toLowerCase();
      document.querySelectorAll("[data-region-block]").forEach(function (blk) {
        var shown = 0;
        blk.querySelectorAll("[data-search]").forEach(function (card) {
          var ok = !v || card.dataset.search.toLowerCase().indexOf(v) !== -1;
          card.hidden = !ok;
          if (ok) shown++;
        });
        blk.hidden = shown === 0;
      });
    });
  }

  // 체크리스트 (이 브라우저에만 저장)
  document.querySelectorAll("[data-checklist]").forEach(function (list) {
    var key = "ipguknote-check-" + list.dataset.checklist;
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem(key) || "{}"); } catch (e) {}
    var boxes = list.querySelectorAll("input[type=checkbox]");
    var counter = list.querySelector(".check-count");
    function update() {
      var n = 0;
      boxes.forEach(function (b) { if (b.checked) n++; });
      if (counter) counter.textContent = n + " / " + boxes.length;
    }
    boxes.forEach(function (b, i) {
      b.checked = !!saved[i];
      b.addEventListener("change", function () {
        saved[i] = b.checked;
        try { localStorage.setItem(key, JSON.stringify(saved)); } catch (e) {}
        update();
      });
    });
    update();
  });
})();

// 상단 시계 (서울 시간, 공항 전광판 느낌)
(function () {
  var el = document.querySelector("[data-clock] span");
  if (!el) return;
  var f = new Intl.DateTimeFormat("en-GB", { timeZone: "Asia/Seoul", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23" });
  function tick() { el.textContent = f.format(new Date()); }
  tick(); setInterval(tick, 1000);
})();
