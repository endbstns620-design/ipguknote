# 가이드 글 — body는 HTML. 링크는 사이트 루트 기준 상대경로 "{up}" 사용
GUIDES = [
    {
        "slug": "fake-sites",
        "title": "가짜 입국신고 사이트 구별법 — 결제창이 나오면 멈추세요",
        "short": "가짜 유료 사이트 구별법",
        "desc": "Visit Japan Web, 베트남·태국 입국신고, 괌 EDF 등 전자 입국신고는 대부분 무료예요. 공식처럼 보이는 유료 대행 사이트를 구별하는 5가지 방법.",
        "body": """
<p>전자 입국신고는 <strong>정부 공식 사이트에서 무료</strong>예요. 입국노트에 실린 나라는 모두 신청 요금이 없어요. 그런데 검색하면 공식처럼 생긴 유료 대행 사이트가 먼저 나오는 경우가 많아요.</p>

<h2>각국 정부도 공식 경고했어요</h2>
<ul class="tips">
  <li><strong>태국:</strong> 이민국이 "돈을 받는 가짜 TDAC 사이트"를 공식 경고했어요.</li>
  <li><strong>말레이시아:</strong> 가짜 MDAC 사이트가 최대 80달러를 받은 사례가 보고됐어요.</li>
  <li><strong>싱가포르:</strong> ICA는 수수료를 받는 제3자 상업 서비스가 ICA와 무관하다고 안내해요.</li>
  <li><strong>베트남:</strong> 공안부가 공식 입국신고 시스템을 사칭하는 사이트를 주의하라고 경고했어요.</li>
  <li><strong>한국:</strong> 2026년 3월 중국에서 "한국 입국신고 11만 원 대행" 사이트가 퍼져 주중대사관이 수사를 요청했어요.</li>
</ul>

<h2>5초 구별법</h2>
<ol class="steps">
  <li><strong>주소를 보세요.</strong> 공식 주소는 대부분 .gov / .go / .gob / .govt 같은 정부 도메인이에요. 정부 도메인이 아닌 공식 사이트(괌·팔라우 등)도 있어요. 이런 나라는 입국노트 나라별 페이지에 "공식 주소 근거"를 적어 두었으니, 주소가 한 글자도 다르지 않은지 비교하세요.</li>
  <li><strong>카드 결제창이 나오면 멈추세요.</strong> 입국노트에 실린 나라의 공식 입국신고에는 결제 단계가 없어요.</li>
  <li><strong>"처리 속도 선택", "승인률 99%" 같은 문구를 의심하세요.</strong> 입국신고는 심사가 아니라 신고라서 이런 문구가 필요 없어요.</li>
  <li><strong>사이트 맨 아래를 보세요.</strong> "민간 대행 업체", "정부와 무관" 같은 문구가 작게 적혀 있으면 대행 사이트예요.</li>
  <li><strong>검색 결과 맨 위 광고를 조심하세요.</strong> '광고' 표시가 붙은 링크는 공식 사이트가 아닐 가능성이 높아요.</li>
</ol>

<h2>이미 결제했다면</h2>
<ul class="tips">
  <li>대행 사이트에서 실제로 신고가 됐는지 알 수 없다면, <strong>공식 사이트에서 직접 다시 제출</strong>하는 것이 안전해요.</li>
  <li>결제를 취소하고 싶다면 사이트의 환불 정책을 확인한 뒤 카드사 고객센터에 문의하세요.</li>
</ul>
<p><a class="btn btn-primary" href="{up}guide/compare/">나라별 공식 주소 표 보기</a></p>
""",
    },
    {
        "slug": "compare",
        "title": "나라별 전자 입국신고 한눈에 비교 (의무 여부·신청 시점·공식 주소)",
        "short": "나라별 한눈에 비교",
        "desc": "일본 Visit Japan Web부터 베트남·태국·괌·뉴질랜드·캐나다까지, 전자 입국신고가 있는 나라의 의무 여부와 신청 시점, 공식 주소를 한 표로 비교해요.",
        "body": "__COMPARE__",
    },
    {
        "slug": "timing",
        "title": "입국신고 '72시간 전'과 '3일 전'은 뭐가 다를까?",
        "short": "72시간 vs 3일 차이",
        "desc": "태국·필리핀은 도착 72시간 전, 싱가포르·말레이시아·베트남은 날짜 기준 3일. 신청 시작 시점을 헷갈리지 않는 법.",
        "body": """
<p>나라마다 "도착 72시간 전부터"와 "도착 3일 전부터"라고 안내하는데, 둘은 계산 방식이 달라요.</p>

<h2>시각 기준: 72시간 (태국·필리핀)</h2>
<p>도착 예정 <strong>시각</strong>에서 정확히 72시간을 거꾸로 세요. 10월 10일 오전 9시 30분(현지) 도착이면 <strong>10월 7일 오전 9시 30분(현지)</strong>부터 신청할 수 있어요.</p>
<p>한국과의 시차도 생각해야 해요. 태국은 한국보다 2시간 느려서, 위 예시는 한국 시간으로 10월 7일 오전 11시 30분이에요.</p>

<h2>날짜 기준: 3일 (싱가포르, 말레이시아, 베트남)</h2>
<p>싱가포르는 <strong>도착일을 포함해 3일</strong>이에요. ICA 공식 예시: "6월 30일 도착이면 6월 28일부터 제출 가능".</p>
<p>말레이시아와 베트남도 "도착(입국) 3일 이내"로 안내해요. 입국노트 계산기는 싱가포르와 같은 방식(도착일 포함 3일)으로, 확실히 접수되는 날짜를 보여줘요.</p>

<h2>가장 쉬운 방법</h2>
<p>각 나라 페이지의 계산기에 도착 날짜와 시각만 넣으세요. 신청 시작 시각을 한국 시간으로 보여주고, <strong>캘린더 알림</strong>도 만들어 줘요.</p>
""",
    },
    {
        "slug": "philippines-red-qr",
        "title": "필리핀 eTravel QR코드가 빨간색으로 나왔을 때",
        "short": "eTravel QR 빨간색 해결",
        "desc": "필리핀 eTravel 등록 후 QR코드가 빨간색이면 정보가 불완전하거나 건강 관련 확인이 필요하다는 뜻이에요. 원인과 대처법.",
        "body": """
<p>필리핀 eTravel은 등록을 마치면 QR코드를 줘요. 색깔에 따라 의미가 달라요.</p>

<h2>초록색 vs 빨간색</h2>
<ul class="tips">
  <li><strong>초록색:</strong> 입력 정보가 올바르고 완전하다는 뜻이에요. 바로 입국심사로 갈 수 있어요.</li>
  <li><strong>빨간색:</strong> 정보가 불완전하거나 틀렸을 때, 또는 최근 질병이나 감염 노출 이력이 신고됐을 때 나와요.</li>
</ul>

<h2>빨간색이 나왔다면</h2>
<ol class="steps">
  <li>공식 사이트 <a href="https://etravel.gov.ph/" target="_blank" rel="noopener">etravel.gov.ph</a>에서 입력 내용을 다시 확인해요.</li>
  <li>여권번호, 항공편명, 날짜, 숙소 주소에 오타가 없는지 봐요.</li>
  <li>수정(업데이트)한 뒤 새 QR을 저장해요. 등록과 수정 모두 무료예요.</li>
  <li>건강 신고 때문이라면 공항 검역 안내에 따라요.</li>
</ol>

<h2>잊지 마세요</h2>
<ul class="tips">
  <li>QR코드는 <strong>비행기 탑승 전 항공사 직원</strong>이 먼저 확인해요. 공항 가기 전에 캡처해 두세요.</li>
  <li>등록은 도착 72시간 전부터 가능해요.</li>
</ul>
<p><a class="btn btn-primary" href="{up}philippines/">필리핀 eTravel 전체 안내</a></p>
""",
    },
    {
        "slug": "family",
        "title": "가족·단체 여행 입국신고, 한 명이 다 해도 될까?",
        "short": "가족·단체 여행 입국신고",
        "desc": "아이를 포함한 동행자 모두 입국신고 대상이에요. 싱가포르는 공식 그룹 제출 기능이 있고, 다른 나라는 공식 사이트 화면에서 동행자 추가 여부를 확인하세요.",
        "body": """
<p>가족 여행에서 가장 많이 헷갈리는 부분은 "아이도 해야 하나?", "한 사람이 다 해도 되나?"이에요.</p>

<h2>아이도 대상이에요</h2>
<p>각국 공식 안내는 국적 기준으로 "외국인 입국자"를 대상으로 해요. 나이 예외가 따로 안내돼 있지 않다면 <strong>아이와 아기도 각자의 여권 정보로 신고</strong>해야 해요.</p>

<h2>한 명이 대신 입력할 수 있나요?</h2>
<ul class="tips">
  <li><strong>싱가포르:</strong> 공식 '그룹 제출(Group Submission)' 기능이 있어요. 같은 일정으로 함께 여행하는 일행을 한 사람이 한 번에 제출할 수 있어요.</li>
  <li><strong>베트남·태국·필리핀·말레이시아:</strong> 동행자 추가 화면이 있는지 공식 사이트에서 확인하세요. 없으면 한 명씩 따로 제출하면 돼요. 대표자가 가족 것을 대신 입력하는 것 자체는 문제가 없어요.</li>
</ul>

<h2>미리 준비하면 빨라요</h2>
<ol class="steps">
  <li>가족 모두의 여권 사진면을 휴대폰에 찍어 둬요.</li>
  <li>항공편명과 숙소 영문 주소를 메모장에 한 번만 적어 두고 복사해서 써요.</li>
  <li>받은 QR·확인 메일은 사람별로 이름을 붙여 저장해요.</li>
</ol>
<p class="small muted">허위 신고는 처벌 대상이 될 수 있어요(싱가포르 ICA 안내). 각자의 정보를 정확히 입력하세요.</p>
""",
    },
    {
        "slug": "multi-country",
        "title": "동남아 여러 나라를 이어서 여행할 때 입국신고 순서",
        "short": "여러 나라 이어서 여행할 때",
        "desc": "방콕→싱가포르→쿠알라룸푸르처럼 여러 나라를 도는 여행이라면, 나라마다 그 나라 도착 시각 기준으로 따로 신고해야 해요.",
        "body": """
<p>방콕 → 싱가포르 → 쿠알라룸푸르처럼 여러 나라를 이어서 가는 일정이라면, 출발 전에 한꺼번에 신고할 수 없는 경우가 많아요.</p>

<h2>핵심: 나라마다 '그 나라 도착 시각' 기준</h2>
<p>신청 가능 시점은 한국 출발일이 아니라 <strong>그 나라에 도착하는 시각</strong>을 기준으로 계산해요. 예를 들어 10일 방콕 도착, 15일 싱가포르 도착이라면:</p>
<ul class="tips">
  <li>태국 TDAC: 7일부터 신청 (한국에서 출발 전에 처리)</li>
  <li>싱가포르 SG Arrival Card: 13일부터 제출 (태국 여행 중에 처리)</li>
</ul>

<h2>여행 중에 놓치지 않으려면</h2>
<ol class="steps">
  <li>각 나라 페이지 계산기에 그 나라 도착 날짜와 시각을 넣어요.</li>
  <li>"캘린더에 알림 추가"로 나라별 알림을 미리 만들어 둬요.</li>
  <li>여행 중 알림이 울리면 공식 사이트에서 바로 제출해요. 데이터가 되는 eSIM이 있으면 편해요.</li>
</ol>

<h2>같은 나라에 다시 들어갈 때</h2>
<p>방콕 → 싱가포르 → 다시 방콕처럼 한 나라를 두 번 들어가면, 입국할 때마다 새로 신고하는 방식이라고 생각하세요. 첫 입국 때 받은 QR을 재사용할 수 없어요.</p>
""",
    },
    {
        "slug": "tdac-edit",
        "title": "태국 TDAC 잘못 입력했을 때 수정하는 법 (다시 낼 필요 없어요)",
        "short": "태국 TDAC 수정 방법",
        "desc": "태국 디지털 입국카드(TDAC)에 항공편·숙소·날짜를 잘못 적었다면 공식 사이트의 Update Arrival Card로 무료 수정할 수 있어요. 고칠 수 없는 항목 3가지와 수정 순서.",
        "body": """
<p>태국 TDAC를 제출한 뒤 항공편이나 숙소, 날짜가 바뀌었다면 <strong>새로 낼 필요 없이 공식 사이트에서 고치면 돼요.</strong> 수정도 무료예요.</p>

<h2>준비할 것 3가지</h2>
<ul class="tips">
  <li><strong>TDAC 번호</strong> (TH Digital Arrival Card No.) — 제출 후 받은 카드와 이메일에 적혀 있어요.</li>
  <li><strong>생년월일</strong></li>
  <li><strong>국적</strong> (Republic of Korea)</li>
</ul>

<h2>수정 순서</h2>
<ol class="steps">
  <li>공식 사이트 <a href="https://tdac.immigration.go.th/" target="_blank" rel="noopener">tdac.immigration.go.th</a>에 들어가 <strong>Update Arrival Card</strong>를 눌러요.</li>
  <li>TDAC 번호, 생년월일, 국적을 넣고 <strong>Search</strong>를 눌러요.</li>
  <li>바꿀 내용을 고쳐요. 앞 단계로 돌아가려면 <strong>Previous</strong>, 그만두려면 <strong>Cancel</strong>이에요.</li>
  <li>이메일 주소를 넣고 약관에 동의한 뒤 <strong>Submit</strong>을 눌러요.</li>
  <li>수정된 카드를 <strong>다시 내려받아</strong> 저장해요. 예전 캡처는 지워 두는 게 헷갈리지 않아요.</li>
</ol>

<h2>이 3가지는 고칠 수 없어요</h2>
<p>공식 매뉴얼에 따르면 제출한 뒤에는 아래 항목을 바꿀 수 없어요.</p>
<ul class="tips">
  <li>여권상 영문 이름 (Full Name)</li>
  <li>국적</li>
  <li>생년월일</li>
</ul>
<p>이 셋 중 하나가 틀렸다면 수정 메뉴로는 해결이 안 돼요. 공식 매뉴얼에는 이 경우 어떻게 하라는 안내가 따로 없어서, 출발 전에 공식 사이트에서 정확한 정보로 다시 작성할 수 있는지 확인하고, 애매하면 항공사나 태국 이민국에 문의하세요.</p>

<h2>가족·일행이 함께 낼 때</h2>
<p>한 번에 <strong>최대 10명</strong>까지 묶어서 제출할 수 있고, 앞 사람 정보를 복사해 쓸 수 있어요. 일정이 같은 가족이라면 이 기능이 편해요.</p>

<h2>주의하세요</h2>
<ul class="tips">
  <li>공식 주소는 <strong>tdac.immigration.go.th</strong> 하나예요. 이름이 비슷한 다른 주소에서 수정·재발급 비용을 받으면 대행 사이트예요.</li>
  <li>수정한 뒤에는 이메일로 받은 최신 카드를 저장해 두고, 입국심사 때 그걸 보여주세요.</li>
</ul>
<p class="small muted">참고: <a href="https://tdac.immigration.go.th/manual/en/index.html" target="_blank" rel="noopener">태국 이민국 TDAC 공식 매뉴얼</a></p>
<p><a class="btn btn-primary" href="{up}thailand/">태국 TDAC 전체 안내 보기</a></p>
""",
    },
    {
        "slug": "vjw-qr",
        "title": "비짓재팬웹(Visit Japan Web) QR코드가 안 나올 때 확인할 3가지",
        "short": "비짓재팬웹 QR 안 나올 때",
        "desc": "Visit Japan Web에서 입국심사·세관 QR코드가 안 보인다면 대부분 등록이 덜 끝난 경우예요. 공식 매뉴얼 기준으로 확인할 3가지와 공항 가기 전 팁.",
        "body": """
<p>Visit Japan Web에 정보를 다 넣었는데 QR코드가 안 보인다면, 대부분 <strong>등록이 하나 덜 끝난 경우</strong>예요. 공식 매뉴얼 기준으로 아래 3가지를 차례로 확인하세요.</p>

<h2>1. 입국심사와 세관 신고를 둘 다 등록했나요?</h2>
<p>QR코드는 두 가지 등록을 <strong>모두</strong> 끝내야 나와요.</p>
<ul class="tips">
  <li><strong>외국인 입국기록</strong> (Disembarkation Card for Foreigner) — 입국심사용</li>
  <li><strong>휴대품·별송품 신고</strong> (Declaration of Accompanied Articles and Unaccompanied Articles) — 세관용</li>
</ul>
<p>한쪽만 등록하고 멈추면 QR 화면까지 가지 않아요. 일정 화면에서 두 항목이 모두 '등록 완료'인지 보세요.</p>

<h2>2. 'QR코드 표시' 버튼을 눌렀나요?</h2>
<p>등록을 마쳐도 QR이 바로 뜨지 않아요. 일정 화면에서 <strong>입국심사·세관 신고 QR코드 표시</strong> 버튼을 따로 눌러야 보여요.</p>

<h2>3. 동반 가족의 세관 신고도 끝냈나요?</h2>
<p>동반 가족을 함께 등록했다면, 가족의 세관 신고까지 마쳐야 QR이 나올 수 있어요. 아이 몫도 빠뜨리지 마세요.</p>

<h2>공항 가기 전에</h2>
<ul class="tips">
  <li>QR이 보이면 <strong>바로 캡처</strong>해 두세요. 공항 와이파이가 느리면 로그인부터 오래 걸려요.</li>
  <li>도착 몇 시간 전까지는 등록을 끝내 두는 게 안전해요. 기내에서 급하게 하지 마세요.</li>
  <li>Visit Japan Web은 일본 디지털청의 무료 서비스예요. 등록을 대신해 준다며 돈을 받는 곳은 공식이 아니에요.</li>
</ul>
<p class="small muted">참고: <a href="https://www.vjw.digital.go.jp/manual/main/visitjapanweb_manual_en.html" target="_blank" rel="noopener">Visit Japan Web 공식 이용 매뉴얼</a></p>
<p><a class="btn btn-primary" href="{up}japan/">일본 Visit Japan Web 전체 안내 보기</a></p>
""",
    },
    {
        "slug": "forgot",
        "title": "입국신고 깜빡하고 출발했다면? 나라별 공항 대처법",
        "short": "입국신고 깜빡했을 때",
        "desc": "태국 TDAC·싱가포르 SG Arrival Card·괌 EDF는 도착 공항에서 할 수 있고, 대만은 출발 공항 체크인 카운터 QR로 할 수 있어요. 일본·베트남은 의무가 아니에요. 공식 안내 기준 나라별 대처법.",
        "body": """
<p>입국신고를 안 하고 비행기를 탔더라도 대부분 방법이 있어요. 다만 <strong>필리핀처럼 탑승 전에 확인하는 나라</strong>는 공항 가기 전에 꼭 해야 해요. 아래는 각국 공식 안내로 확인한 내용만 적었어요.</p>

<h2>도착해서 해도 되는 나라</h2>
<ul class="tips">
  <li><strong>태국 (TDAC):</strong> 수완나품·돈므앙·푸껫·치앙마이·핫야이 공항에 키오스크와 와이파이가 있어요. 내려서 작성하면 돼요. (태국 이민국 TDAC FAQ)</li>
  <li><strong>싱가포르 (SG Arrival Card):</strong> 안 냈으면 입국심사 전에 도착해서 제출해야 해요. 그만큼 심사가 늦어져요. (싱가포르 ICA)</li>
  <li><strong>괌 (EDF):</strong> 공항 수하물 찾는 곳에 키오스크가 있어요. 가족은 대표 1명이 내면 돼요. (괌 관광청)</li>
</ul>

<h2>출발 공항에서 해야 하는 나라</h2>
<ul class="tips">
  <li><strong>대만 (TWAC):</strong> 안 하면 입국심사를 진행할 수 없어요. 출발 공항 체크인 카운터에 QR코드가 붙어 있으니 <strong>탑승 전에</strong> 휴대폰으로 작성하세요. (대만 이민서)</li>
  <li><strong>필리핀 (eTravel):</strong> 비행기 타기 전에 항공사 직원이 QR을 확인해요. 도착 후 작성할 수 있다는 공식 안내는 확인되지 않아서, <strong>체크인 전에</strong> 끝내야 해요.</li>
</ul>

<h2>의무가 아닌 나라</h2>
<ul class="tips">
  <li><strong>일본 (Visit Japan Web):</strong> 의무가 아니에요. 세관은 종이 신고서를 그대로 쓸 수 있어요. (일본 세관)</li>
  <li><strong>베트남 (사전 입국신고):</strong> 공안부가 "의무가 아닌 선택"이라고 발표했어요. 안 했으면 일반 입국심사 줄로 가면 돼요.</li>
</ul>

<h2>공식 안내가 불분명한 나라 — 출발 전에 하세요</h2>
<ul class="tips">
  <li><strong>말레이시아 (MDAC):</strong> 의무예요. "늦어도 도착 시"까지 가능하다는 정부 기관 안내가 있지만, 공항 키오스크 안내는 확인되지 않아요.</li>
  <li><strong>인도네시아 (All Indonesia):</strong> 의무예요. 도착 시 작성 가능 여부는 공식 사이트에서 확인되지 않았어요.</li>
</ul>

<h2>도착 공항에서 급하게 할 때</h2>
<ol class="steps">
  <li>공항 와이파이에 먼저 연결해요.</li>
  <li>검색하지 말고 <strong>입국노트 나라별 페이지의 공식 주소</strong>로 들어가요. 급할 때 유료 대행 사이트에 걸리기 쉬워요.</li>
  <li>여권, 항공편명, 숙소 영문 주소를 준비해요. 숙소 주소는 예약 메일에서 복사하면 빨라요.</li>
</ol>
<p class="small muted">참고: <a href="https://tdac.immigration.go.th/manual/en/faq.html" target="_blank" rel="noopener">태국 TDAC FAQ</a> · <a href="https://ask.gov.sg/ica/questions/clos83fv6018p5k0wm8lb89d2" target="_blank" rel="noopener">싱가포르 ICA</a> · <a href="https://www.immigration.gov.tw/5475/5478/141457/142068/398041/" target="_blank" rel="noopener">대만 이민서</a> · <a href="https://www.visitguam.com/about-guam/entry-and-exit-formalities/" target="_blank" rel="noopener">괌 관광청</a> · <a href="https://www.customs.go.jp/english/passenger/declaration/declaration_app.html" target="_blank" rel="noopener">일본 세관</a> · <a href="https://en.bocongan.gov.vn/article/immigration-department-launches-pre-arrival-information-system-1778670404" target="_blank" rel="noopener">베트남 공안부</a></p>
<p><a class="btn btn-primary" href="{up}guide/compare/">나라별 공식 주소 표 보기</a></p>
""",
    },
    {
        "slug": "sgac-edit",
        "title": "싱가포르 SG Arrival Card 수정하는 법 · 확인 메일이 안 올 때",
        "short": "SG Arrival Card 수정·메일",
        "desc": "항공편이나 날짜가 바뀌면 SG Arrival Card를 새로 내면 돼요. 새 것이 예전 것을 대신하고 취소할 필요도 없어요. 확인 메일이 안 올 때와 e-Pass 찾는 법까지 싱가포르 ICA 공식 안내 기준.",
        "body": """
<p>싱가포르 입국카드(SG Arrival Card)는 일정이 바뀌어도 걱정할 필요 없어요. <strong>새로 한 번 더 내면 끝</strong>이에요.</p>

<h2>항공편·날짜가 바뀌었을 때</h2>
<ul class="tips">
  <li>바뀐 정보로 <strong>SG Arrival Card를 다시 제출</strong>해요. 새로 낸 것이 예전 것을 대신해요.</li>
  <li>예전 것을 <strong>취소할 필요는 없어요.</strong></li>
  <li>건강 상태가 바뀐 경우에는 'Update SGAC' 기능으로 고칠 수 있어요. 고친 뒤 PDF를 다시 내려받거나 MyICA 앱에서 확인해요.</li>
</ul>

<h2>확인 메일이 안 올 때</h2>
<ol class="steps">
  <li><strong>스팸·정크 메일함</strong>을 먼저 보세요. 확인 메일에는 DE 번호가 적혀 있어요.</li>
  <li>제출 직후 화면에서 <strong>PDF를 내려받을 수 있어요.</strong> 메일이 안 와도 이걸 저장해 두세요.</li>
  <li>입국할 때는 확인 메일(휴대폰 화면이나 출력본)을 보여주면 돼요.</li>
  <li>입국 후 받는 전자 방문 허가증(e-Pass)을 못 받았다면 <a href="https://eservices.ica.gov.sg/sgarrivalcard/epassenquiry" target="_blank" rel="noopener">ICA e-Pass 조회 페이지</a>에서 찾을 수 있어요.</li>
</ol>
<p>이메일 주소는 꼭 넣으세요. 안 넣으면 확인 메일을 못 받고 입국심사가 늦어질 수 있어요.</p>

<h2>꼭 알아둘 것</h2>
<ul class="tips">
  <li><strong>제출 시점:</strong> 도착일을 포함해 3일 전부터예요. 6월 30일 도착이면 6월 28일부터 낼 수 있어요.</li>
  <li><strong>여행 한 번에 하나:</strong> 싱가포르에 다시 들어올 때마다 새로 내야 해요.</li>
  <li><strong>환승만 하는 경우:</strong> 입국심사를 거치지 않고 공항 안에서 환승하면 안 내도 돼요.</li>
  <li><strong>무료:</strong> ICA 공식 사이트나 MyICA 앱에서만 내세요. ICA는 돈을 받는 비공식 사이트 63곳을 공개 경고했어요.</li>
</ul>
<p class="small muted">참고: <a href="https://www.ica.gov.sg/enter-transit-depart/entering-singapore/sg-arrival-card" target="_blank" rel="noopener">싱가포르 ICA SG Arrival Card</a> · <a href="https://ask.gov.sg/ica/questions/clos83fv801995k0wmiszar0x" target="_blank" rel="noopener">ICA 공식 Q&amp;A</a></p>
<p><a class="btn btn-primary" href="{up}singapore/">싱가포르 입국카드 전체 안내 보기</a></p>
""",
    },
    {
        "slug": "twac",
        "title": "대만 온라인 입국신고(TWAC) 꼭 해야 할까? 수정 방법까지",
        "short": "대만 입국신고 의무·수정",
        "desc": "2025년 10월부터 대만은 종이 입국카드를 없애고 온라인 입국신고(TWAC)를 의무로 바꿨어요. 한국인도 대상이고, 제출 후 언제든 온라인으로 고칠 수 있어요. 대만 이민서 공식 안내 기준.",
        "body": """
<p>대만은 <strong>2025년 10월 1일부터 종이 입국카드를 없앴어요.</strong> 무비자로 가는 한국인도 온라인 입국신고(TWAC)를 해야 해요.</p>

<h2>핵심만 정리</h2>
<ul class="tips">
  <li><strong>대상:</strong> 방문 비자나 무비자로 들어가는 외국인 (한국인 관광객 포함)</li>
  <li><strong>시점:</strong> 도착 3일 전부터 낼 수 있어요.</li>
  <li><strong>비용:</strong> 무료예요.</li>
  <li><strong>안 하면:</strong> 입국심사를 진행할 수 없어요.</li>
  <li><strong>가족·일행:</strong> 한 번에 최대 16명까지 같이 낼 수 있어요.</li>
</ul>

<h2>잘못 입력했거나 일정이 바뀌었을 때</h2>
<p>대만 이민서 안내에 따르면 제출한 뒤에도 <strong>온라인에서 언제든 확인하고 고칠 수 있어요.</strong> 다시 낼 필요 없이 공식 사이트에서 내 신고서를 찾아 수정하세요.</p>

<h2>깜빡하고 공항에 왔다면</h2>
<p>출발 공항 <strong>체크인 카운터에 TWAC QR코드</strong>가 붙어 있어요. 비행기 타기 전에 휴대폰으로 작성하세요.</p>

<h2>헷갈리기 쉬운 것</h2>
<ul class="tips">
  <li><strong>"7일 전부터"라는 글:</strong> 예전 대사관 공지에 남아 있는 내용이에요. 지금 대만 이민서 공식 안내는 <strong>3일 전</strong>이에요.</li>
  <li><strong>자동출입국(e-Gate) 등록자:</strong> e-Gate에 등록했다고 TWAC가 면제된다는 공식 안내는 찾지 못했어요. 그냥 내는 게 안전해요.</li>
  <li><strong>거류증(ARC) 소지자:</strong> 공식 안내는 방문객을 대상으로 해서, 거류증이 있는 사람은 대상이 아니에요.</li>
</ul>
<p class="small muted">참고: <a href="https://www.immigration.gov.tw/5385/7229/7238/398036/" target="_blank" rel="noopener">대만 이민서 공지</a> · <a href="https://www.immigration.gov.tw/5475/5478/141457/142068/398041/" target="_blank" rel="noopener">영문 안내</a></p>
<p><a class="btn btn-primary" href="{up}taiwan/">대만 입국신고 전체 안내 보기</a></p>
""",
    },
]
