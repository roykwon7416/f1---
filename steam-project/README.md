# SteamSpy 분석 대시보드

이 프로젝트는 **FastAPI** 기반의 백엔드와 **HTML/CSS/JavaScript** 프론트엔드를 통합하여, SteamSpy 데이터를 시각화하는 웹 애플리케이션입니다.

---

## 요구 사항

* Python 3.8 이상
* pip, venv
* 인터넷 연결 (SteamSpy 및 Steam Store API 호출용)

---

## 프로젝트 구조

```
steam-project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .venv/             # 가상환경
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
└── README.md
```

---

## 설치 및 실행

### 1. 백엔드 설정

```bash
# 프로젝트 루트에서
cd backend

# 가상환경 생성
python -m venv .venv

# Windows PowerShell에서 활성화 (최초 1회에만 실행)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

# Windows CMD에서 활성화
.\.venv\Scripts\activate.bat

# 의존성 설치
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
# backend 디렉토리에서
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

* **대시보드 접속**: [http://localhost:8000/](http://localhost:8000/)
* **API 문서 (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. 프론트엔드 별도 실행 (선택)

프론트엔드를 별도 HTTP 서버로 구동하려면:

```bash
cd frontend
python -m http.server 8080
```

* **대시보드 접속**: [http://localhost:8080/](http://localhost:8080/)

---

## 주요 기능

* **상위 인기 게임 분석**: 소유자 수, 2주 평균 플레이어 수, 평균 플레이타임
* **장르별 요약**: 장르별 총 플레이어 수 차트
* **데이터 필터링**: 장르 및 플레이타임 조건 필터
* **상세 정보**: 개별 게임별 주요 통계
* **CSV 다운로드**: 원하는 데이터를 CSV로 저장

---

## Licence

MIT © 권현진
