from ast import literal_eval

from aiohttp.client import ClientSession

from api.types import UserStats
from cache import redis_cache
from env import CACHE_STEAM_API_DATA_SECONDS, STEAM_API_KEY


__all__: tuple[str, ...] = (
    "get_user_stats",
)


async def get_user_stats(steamid: str) -> UserStats:
    cache_key = f"IPlayerService/GetOwnedGames::{steamid}"
    cached_data = await redis_cache.get(cache_key)
    if cached_data is None:
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
        await redis_cache.set(cache_key, str(response), ex=CACHE_STEAM_API_DATA_SECONDS)
    else:
        response = literal_eval(cached_data.decode("utf-8"))

    games = response["games"]
    total_playtime = sum([g["playtime_forever"] for g in games])

    return UserStats(
        total_minutes=total_playtime,
        game_count=response["game_count"],
    )
