from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from app.models import GameSummary
from app.services import fetch_top_games, parse_summary

app = FastAPI(title="SteamSpy 분석 API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# API 라우터 정의
@app.get("/api/top-games", response_model=List[GameSummary])
def top_games():
    raw = fetch_top_games()
    return [parse_summary(int(k), v) for k, v in raw.items()]

@app.get("/api/games", response_model=List[GameSummary])
def filtered_games(
    genres: List[str] = Query(None),
    min_time: int = Query(0)
):
    games = top_games()
    return [g for g in games if (not genres or g.genre in genres) and g.average_playtime >= min_time]

@app.get("/api/game/{appid}", response_model=GameSummary)
def single_game(appid: int):
    raw = fetch_top_games()
    data = raw.get(str(appid))
    if not data:
        raise HTTPException(status_code=404, detail="게임을 찾을 수 없습니다.")
    return parse_summary(appid, data)

# 정적 파일 서빙
app.mount(
    "/",
    StaticFiles(directory="../frontend", html=True),
    name="static"
)