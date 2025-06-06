import requests
import re
import math
from functools import lru_cache

# SteamSpy Top100 in 2 weeks API
TOP100_URL = "https://steamspy.com/api.php?request=top100in2weeks"
# SteamSpy 상세 정보 API
DETAIL_URL = "https://steamspy.com/api.php?request=appdetails&appid={appid}"

@lru_cache(maxsize=1)
def fetch_top_games() -> dict:
    res = requests.get(TOP100_URL)
    return res.json() if res.status_code == 200 else {}

@lru_cache(maxsize=256)
def fetch_game_details(appid: int) -> dict:
    res = requests.get(DETAIL_URL.format(appid=appid))
    return res.json() if res.status_code == 200 else {}


def parse_summary(appid: int, summary: dict) -> dict:
    name = summary.get("name", "")

    # 소유자 수 추정: 구매자 수 범위의 기하평균 사용
    owners_str = summary.get("owners", "")
    nums = re.findall(r"\d+", owners_str.replace(",", ""))
    if len(nums) >= 2:
        min_val = int(nums[0])
        max_val = int(nums[1])
        owners = int(round(math.sqrt(min_val * max_val)))
    elif nums:
        owners = int(nums[0])
    else:
        owners = 0

    # 최근 2주 평균 플레이어 수
    players_2weeks = int(summary.get("average_2weeks", 0))

    # 평균 플레이타임 (분)
    average_playtime = int(summary.get("average_forever", 0)) // 60

    # 장르: SteamSpy 상세 정보 API 호출 후 genre 필드에서 추출
    details = fetch_game_details(appid)
    raw_genre = details.get("genre", "")
    genre = raw_genre.split(",")[0] if raw_genre else "알 수 없음"

    return {
        "appid": appid,
        "name": name,
        "genre": genre,
        "owners": owners,
        "players_2weeks": players_2weeks,
        "average_playtime": average_playtime,
    }
