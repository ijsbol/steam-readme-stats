from aiohttp.client import ClientSession

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response

from api._slug_.stats.badge.types import BadgeStyle
from api._slug_.stats.badge.utils import generate_url
from api.utils import get_user_stats
from cache import redis_cache
from env import CACHE_IMAGE_API_DATA_SECONDS


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter()


@router.get(path="/")
async def api_slug_stats_badge_games(
    request: Request,
    steamid: str,
    label: str = "Games",
    color: str = "black",
    label_color: str = "black",
    style: BadgeStyle = "flat-square",
) -> Response:
    cache_key = f"api_slug_stats_badge_games:{steamid}:{label}:{color}:{label_color}:{style}"
    cache_response = await redis_cache.get(cache_key)
    if cache_response is None:
        user_stats = await get_user_stats(steamid)
        game_count = user_stats["game_count"]
        url = generate_url(
            label=label,
            colour=color,
            message=f"{game_count:,}",
            label_colour=label_color,
            style=style,
        )
        async with ClientSession() as session:
            async with session.get(url=url) as resp:
                svg_data = await resp.read()
                await redis_cache.set(cache_key, svg_data, CACHE_IMAGE_API_DATA_SECONDS)
    else:
        svg_data = cache_response

    return Response(
        content=svg_data,
        headers={"Content-Type": "image/svg+xml;charset=utf-8"},
    )
