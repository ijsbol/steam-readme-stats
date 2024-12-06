from typing import Optional

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from api._slug_.stats.badge.types import BadgeStyle, Format
from api._slug_.stats.badge.utils import generate_url
from api.utils import get_user_stats


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter()


@router.get(path="/")
async def api_slug_stats_badge(
    request: Request,
    steamid: str,
    label: str = "Games",
    colour: str = "black",
    format: Format = "full",
    label_color: str = "black",
    style: BadgeStyle = "flat-square",
    link: Optional[str] = None,
) -> RedirectResponse:
    user_stats = await get_user_stats(steamid)
    game_count = user_stats["game_count"]
    return RedirectResponse(url=generate_url(
        label=label,
        colour=colour,
        message=f"{game_count:,}",
        label_color=label_color,
        style=style,
        link=link,
    ))
