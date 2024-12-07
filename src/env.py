from os import getenv
from typing import Final

from dotenv import load_dotenv


__all__: tuple[str, ...] = (
    "STEAM_API_KEY",
    "REDIS_HOST_IP",
    "REDIS_PORT",
    "REDIS_PASSWORD",
    "CACHE_STEAM_API_DATA_SECONDS",
    "CACHE_IMAGE_API_DATA_SECONDS",
)


load_dotenv()


STEAM_API_KEY: Final[str] = str(getenv("STEAM_API_KEY"))
REDIS_HOST_IP: Final[str] = str(getenv("REDIS_HOST_IP"))
REDIS_PORT: Final[int] = int(str(getenv("REDIS_PORT")))
REDIS_PASSWORD: Final[str] = str(getenv("REDIS_PASSWORD"))
CACHE_STEAM_API_DATA_SECONDS: Final[int] = int(str(getenv("CACHE_STEAM_API_DATA_SECONDS")))
CACHE_IMAGE_API_DATA_SECONDS: Final[int] = int(str(getenv("CACHE_IMAGE_API_DATA_SECONDS")))
