from aiohttp.client import ClientSession

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response

from api._slug_.stats.badge.types import BadgeStyle, Format
from api._slug_.stats.badge.utils import generate_url
from api.utils import get_user_stats
from cache import redis_cache
from env import CACHE_IMAGE_API_DATA_SECONDS


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter()


def _format_playtime(playtime: int, format: Format) -> str:
    if format == "total_days":
        days = playtime // (24 * 60)
        return f"{days:,} days"
    elif format == "total_hours":
        hours = playtime // 60
        return f"{hours:,} hours"
    elif format == "total_minutes":
        return f"{playtime:,} minutes"
    elif format == "days_and_hours":
        days = playtime // (24 * 60)
        remaining_minutes = playtime % (24 * 60)
        hours = remaining_minutes // 60
        return str(f"{days:,} days {hours} hours")
    elif format == "hours_and_minutes":
        hours = playtime // 60
        remaining_minutes = playtime % (60)
        return str(f"{hours:,} hours {remaining_minutes} minutes")
    elif format == "full":
        days = playtime // (24 * 60)
        remaining_minutes = playtime % (24 * 60)
        hours = remaining_minutes // 60
        remaining_minutes %= 60
        return str(f"{days:,} days {hours} hours {remaining_minutes} minutes")
    else:
        raise NotImplemented("Unreachable code.")


@router.get(path="/")
async def api_slug_stats_badge_playtime(
    request: Request,
    steamid: str,
    label: str = "Playtime",
    color: str = "black",
    format: Format = "full",
    label_color: str = "black",
    style: BadgeStyle = "flat-square",
) -> Response:
    cache_key = f"api_slug_stats_badge_playtime:{steamid}:{format}:{label}:{color}:{label_color}:{style}"
    cache_response = await redis_cache.get(cache_key)
    if cache_response is None:
        user_stats = await get_user_stats(steamid)
        formatted_playtime = _format_playtime(
            playtime=user_stats["total_minutes"],
            format=format,
        )
        url = generate_url(
            label=label,
            colour=color,
            message=formatted_playtime,
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
