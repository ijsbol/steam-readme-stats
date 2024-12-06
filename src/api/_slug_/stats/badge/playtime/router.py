from typing import Literal, Optional, Union
from urllib.parse import urlencode, quote

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from api.utils import get_user_stats


__all__: tuple[str, ...] = (
    "router",
)


Format = Union[
    Literal["total_days"],          # x days
    Literal["total_hours"],         # x hours
    Literal["total_minutes"],       # x minutes
    Literal["days_and_hours"],      # x days y hours
    Literal["hours_and_minutes"],   # x hours y minutes
    Literal["full"],                # x days y hours z minutes
]


BadgeStyle = Union[
    Literal["flat"],
    Literal["flat-square"],
    Literal["for-the-badge"],
    Literal["plastic"],
    Literal["social"],
]


router = APIRouter()


def _generate_url(
    label: str,
    message: str,
    colour: str,
    label_color: str,
    style: BadgeStyle,
    link: Optional[str],
) -> str:
    args = {
        "labelColor": label_color,
        "style": style,
        "link": link,
        "logo": "steam",
    }
    if link is None:
        del args["link"]
    return (
        "https://img.shields.io/badge/"
        + quote(label)
        + "-"
        + quote(message)
        + "-"
        + quote(colour)
        + "?" + urlencode(args)
    )


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
async def api_slug_stats_badge(
    request: Request,
    steamid: str,
    label: str = "Playtime",
    colour: str = "black",
    format: Format = "full",
    label_color: str = "black",
    style: BadgeStyle = "flat-square",
    link: Optional[str] = None,
) -> RedirectResponse:
    user_stats = await get_user_stats(steamid)
    formatted_playtime = _format_playtime(
        playtime=user_stats["total_minutes"],
        format=format,
    )
    url = _generate_url(
        label=label,
        colour=colour,
        message=formatted_playtime,
        label_color=label_color,
        style=style,
        link=link,
    )
    return RedirectResponse(url=url)
