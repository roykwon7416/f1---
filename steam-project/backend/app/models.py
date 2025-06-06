from pydantic import BaseModel

class GameSummary(BaseModel):
    appid: int
    name: str
    genre: str
    owners: int               # 구매자 수 추정값
    players_2weeks: int       # 평균 2주 플레이어 수
    average_playtime: int     # 분 단위