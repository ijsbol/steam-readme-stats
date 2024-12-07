
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
    label_colour: str,
    style: BadgeStyle,
) -> str:
    args = {
        "labelColor": label_colour,
        "style": style,
        "logo": "steam",
    }
    return (
        "https://img.shields.io/badge/"
        + quote(label)
        + "-"
        + quote(message)
        + "-"
        + quote(colour)
        + "?" + urlencode(args)
    )
