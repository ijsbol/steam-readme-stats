
from typing import Literal, Union


__all__: tuple[str, ...] = (
    "BadgeStyle",
    "Format",
)


BadgeStyle = Union[
    Literal["flat"],
    Literal["flat-square"],
    Literal["for-the-badge"],
    Literal["plastic"],
    Literal["social"],
]


Format = Union[
    Literal["total_days"],          # x days
    Literal["total_hours"],         # x hours
    Literal["total_minutes"],       # x minutes
    Literal["days_and_hours"],      # x days y hours
    Literal["hours_and_minutes"],   # x hours y minutes
    Literal["full"],                # x days y hours z minutes
]
