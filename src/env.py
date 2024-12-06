from os import getenv
from typing import Final

from dotenv import load_dotenv


__all__: tuple[str, ...] = (
    "STEAM_API_KEY",
)


load_dotenv()


STEAM_API_KEY: Final[str] = str(getenv("STEAM_API_KEY"))
