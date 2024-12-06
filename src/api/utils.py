from aiohttp.client import ClientSession

from api.types import UserStats
from env import STEAM_API_KEY


__all__: tuple[str, ...] = (
    "get_user_stats",
)


async def get_user_stats(steamid: str) -> UserStats:
    async with ClientSession() as session:
        async with session.get(
            url="http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/",
            params={
                "key": STEAM_API_KEY,
                "steamid": steamid,
            },
        ) as resp:
            data = await resp.json()
            response = data["response"]

    games = response["games"]
    total_playtime = sum([g["playtime_forever"] for g in games])

    return UserStats(
        total_minutes=total_playtime,
        game_count=response["game_count"],
    )
