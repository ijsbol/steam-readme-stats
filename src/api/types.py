from typing import TypedDict


__all__: tuple[str, ...] = (
    "UserStats",
)


class UserStats(TypedDict):
    total_minutes: int
    game_count: int
