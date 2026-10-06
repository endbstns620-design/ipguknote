# 국가 데이터는 data/countries.json 에 있습니다 — 수정 후 python build/build.py 실행
import json, os

VERIFIED = "2026-10-06"
# GitHub Pages 주소. 정식 도메인을 연결하면 여기만 수정
SITE_URL = "https://ipguknote.com"
BASE = "/"  # 사이트가 놓인 경로 (정식 도메인이면 "/")
# 검색엔진 소유확인 코드 (content 값만). 비어 있으면 태그를 넣지 않아요.
GOOGLE_VERIFY = "YxY2f6U9yoPJfsTSQ8SFUiZrHlhAiHVAdFz5KydUfgo"
NAVER_VERIFY = "f6b9bc06ce70d9c3db9ef40c7655f1d48662a16f"
# 구글 애널리틱스 측정 ID (비우면 통계 코드를 넣지 않아요)
GA_ID = "G-HC71Z01TFX"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfzPvt9mvo_EEJuLjgAv7bi-6wBXkqENe1_P9BGquR_B4YgpA/viewform"

with open(os.path.join(os.path.dirname(__file__), "data", "countries.json"), encoding="utf-8") as f:
    COUNTRIES = json.load(f)

REGIONS = [
    ("east-asia", "동북아시아"),
    ("southeast-asia", "동남아시아"),
    ("resort", "괌·팔라우·몰디브"),
    ("longhaul", "뉴질랜드·캐나다"),
]

# 제휴 슬롯 — 링크가 비어 있으면 화면에 안 보여요.
#   href       : 기본 링크 (모든 나라 공통)
#   by_country : 나라별 링크 {"vietnam": "https://...", "japan": "https://..."} — 있으면 기본 링크보다 우선
#   check      : 체크리스트에 넣을 문구 (링크가 있을 때만 체크리스트에 추가)
AFFILIATES = [
    {
        "key": "esim",
        "title": "eSIM / 데이터",
        "desc": "도착하자마자 지도·메신저 쓰기",
        "check": "현지 데이터(eSIM·유심·로밍) 준비",
        # 마이리얼트립 제휴 링크 (광고 링크 만들기로 생성, 2026-10-06)
        "href": "",
        "by_country": {
            "vietnam": "https://myrealt.rip/uGqZ7a",
            "japan": "https://myrealt.rip/uGqj81",
            "thailand": "https://myrealt.rip/uGtF92",
            "philippines": "https://myrealt.rip/uGv89d",
            "guam": "https://myrealt.rip/uGtI8a",
        },
    },
    {
        "key": "pickup",
        "title": "공항 픽업",
        "desc": "밤 도착이면 미리 예약",
        "check": "",
        "href": "",
        "by_country": {},
    },
    {
        "key": "insurance",
        "title": "여행자보험",
        "desc": "출국 전날까지 가입 가능",
        "check": "여행자보험 가입 여부 확인",
        "href": "",
        "by_country": {},
    },
    {
        "key": "card",
        "title": "트래블카드 / 환전",
        "desc": "현지 ATM 인출 수수료 줄이기",
        "check": "",
        "href": "",
        "by_country": {},
    },
]

# 나라별 제휴 카드 (계산기 아래, 최대 3개). href가 빈 항목은 화면에 안 보여요.
#   1) eSIM  2) 패스트트랙(없는 나라는 공항 이동)  3) 후기 많은 상품
AFF_BY_COUNTRY = {
    "vietnam": [
        {"title": "베트남 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uGqZ7a"},
        {"title": "다낭 공항 패스트트랙", "desc": "입국심사 줄 서지 않기 · 후기 680+", "href": "https://myrealt.rip/uL43f1", "src": "https://experiences.myrealtrip.com/products/5541964"},
        {"title": "나트랑 패스트트랙+공항픽업", "desc": "입국부터 호텔까지 한 번에 · 후기 730+", "href": "https://myrealt.rip/uL5193", "src": "https://experiences.myrealtrip.com/products/4743060"},
    ],
    "thailand": [
        {"title": "태국 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uGtF92"},
        {"title": "수완나품 공항 패스트트랙", "desc": "입국심사 줄 서지 않기 · 후기 330+", "href": "https://myrealt.rip/uL5273", "src": "https://experiences.myrealtrip.com/products/4887254"},
        {"title": "방콕 공항 픽업·샌딩", "desc": "방콕·파타야 시내까지 · 후기 2,600+", "href": "https://myrealt.rip/uL53a8", "src": "https://experiences.myrealtrip.com/products/3514003"},
    ],
    "philippines": [
        {"title": "필리핀 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uGv89d"},
        {"title": "세부 막탄 공항 패스트트랙", "desc": "입국·출국 빠른 수속", "href": "https://myrealt.rip/uL581c", "src": "https://experiences.myrealtrip.com/products/3570420"},
        {"title": "세부 공항 픽업·샌딩", "desc": "공항에서 호텔까지 · 후기 110+", "href": "https://myrealt.rip/uL5963", "src": "https://experiences.myrealtrip.com/products/3446459"},
    ],
    "japan": [
        {"title": "일본 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uGqj81"},
        {"title": "나리타 스카이라이너", "desc": "나리타 공항 → 도쿄 시내 · 후기 4,200+", "href": "https://myrealt.rip/uL5A2f", "src": "https://experiences.myrealtrip.com/products/5869252"},
        {"title": "간사이 라피트 편도", "desc": "간사이 공항 → 오사카 난바 · 후기 1만+", "href": "https://myrealt.rip/uL5Bb5", "src": "https://experiences.myrealtrip.com/products/5869248"},
    ],
    "guam": [
        {"title": "괌 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uGtI8a"},
        {"title": "괌 공항 픽업", "desc": "공항에서 호텔까지 편도·왕복", "href": "https://myrealt.rip/uL5H18", "src": "https://experiences.myrealtrip.com/products/3446566"},
        {"title": "괌 돌핀크루즈", "desc": "돌고래+스노클링 · 후기 510+", "href": "https://myrealt.rip/uL5Jbd", "src": "https://experiences.myrealtrip.com/products/3446615"},
    ],
    "taiwan": [
        {"title": "대만 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uL5K36", "src": "https://experiences.myrealtrip.com/products/3443049"},
    ],
    "singapore": [
        {"title": "싱가포르 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uL5Lcb", "src": "https://experiences.myrealtrip.com/products/3443064"},
    ],
    "malaysia": [
        {"title": "말레이시아 eSIM", "desc": "도착하자마자 지도·메신저 쓰기", "href": "https://myrealt.rip/uL5Mce", "src": "https://experiences.myrealtrip.com/products/3443078"},
    ],
}
HOME_AFF = ["vietnam", "japan", "thailand"]  # 첫 화면에 eSIM 카드를 보여줄 나라
