# 국가 데이터는 data/countries.json 에 있습니다 — 수정 후 python build/build.py 실행
import json, os

VERIFIED = "2026-10-05"
# GitHub Pages 주소. 정식 도메인을 연결하면 여기만 수정
SITE_URL = "https://ipguknote.com"
BASE = "/"  # 사이트가 놓인 경로 (정식 도메인이면 "/")
# 검색엔진 소유확인 코드 (content 값만). 비어 있으면 태그를 넣지 않아요.
GOOGLE_VERIFY = "YxY2f6U9yoPJfsTSQ8SFUiZrHlhAiHVAdFz5KydUfgo"
NAVER_VERIFY = "f6b9bc06ce70d9c3db9ef40c7655f1d48662a16f"
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
        # TODO: 마이리얼트립 '광고 링크 만들기'로 만든 제휴 링크로 교체 (지금은 일반 상품 주소라 수수료 없음)
        "href": "https://www.myrealtrip.com",
        "by_country": {
            "vietnam": "https://www.myrealtrip.com/offers/138780",
            "japan": "https://www.myrealtrip.com/offers/138635",
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
