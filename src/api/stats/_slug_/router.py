from aiohttp import ClientSession
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from env import STEAM_API_KEY


router = APIRouter()


@router.get(path="/")
async def api_stats(
    request: Request,
    steamid: str,
) -> JSONResponse:

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
    days = total_playtime // (24 * 60)
    remaining_minutes = total_playtime % (24 * 60)
    hours = remaining_minutes // 60
    remaining_minutes %= 60

    return JSONResponse(
        content={
            "playtime": {
                "total_minutes": total_playtime,
                "formatted": {
                    "days": days,
                    "hours": hours,
                    "minutes": remaining_minutes,
                }
            },
            "game_count": response["game_count"],
        },
        status_code=200,
    )
