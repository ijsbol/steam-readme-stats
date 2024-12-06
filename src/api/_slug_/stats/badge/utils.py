
from typing import Optional
from urllib.parse import quote, urlencode

from api._slug_.stats.badge.types import BadgeStyle


__all__: tuple[str, ...] = (
    "generate_url",
)


def generate_url(
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
