__all__: tuple[str, ...] = (
    "STEAM_API_KEY",
)


from os import getenv
from typing import Final

from dotenv import load_dotenv


load_dotenv()


STEAM_API_KEY: Final[str] = str(getenv("STEAM_API_KEY"))
