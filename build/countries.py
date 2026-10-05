# 국가 데이터는 data/countries.json 에 있습니다 — 수정 후 python build/build.py 실행
import json, os

VERIFIED = "2026-10-05"
# GitHub Pages 주소. 정식 도메인을 연결하면 여기만 수정
SITE_URL = "https://endbstns620-design.github.io/ipguknote"
BASE = "/ipguknote/"  # 사이트가 놓인 경로 (정식 도메인이면 "/")
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfzPvt9mvo_EEJuLjgAv7bi-6wBXkqENe1_P9BGquR_B4YgpA/viewform"

with open(os.path.join(os.path.dirname(__file__), "data", "countries.json"), encoding="utf-8") as f:
    COUNTRIES = json.load(f)

REGIONS = [
    ("east-asia", "동북아시아"),
    ("southeast-asia", "동남아시아"),
    ("resort", "괌·팔라우·몰디브"),
    ("longhaul", "뉴질랜드·캐나다"),
]

# 제휴 슬롯 — href를 실제 제휴 링크로 바꾸면 됩니다 (비어 있으면 화면에 안 보임)
AFFILIATES = [
    {
        "key": "esim",
        "title": "eSIM / 데이터",
        "desc": "도착하자마자 지도·메신저 쓰기",
        "href": ""
    },
    {
        "key": "insurance",
        "title": "여행자보험",
        "desc": "출국 전날까지 가입 가능",
        "href": ""
    },
    {
        "key": "card",
        "title": "트래블카드 / 환전",
        "desc": "현지 ATM 인출 수수료 줄이기",
        "href": ""
    },
    {
        "key": "pickup",
        "title": "공항 픽업",
        "desc": "밤 도착이면 미리 예약",
        "href": ""
    }
]
