from typing import Optional, Union

from redis.asyncio import BlockingConnectionPool, Redis

from env import REDIS_HOST_IP, REDIS_PASSWORD, REDIS_PORT


__all__: tuple[str, ...] = (
    "redis_cache",
)


class RedisTypeAlias:
    async def get(self, ref: str) -> Optional[bytes]: ...
    async def set(self, ref: str, data: Union[str, bytes], ex: int) -> bytes: ...
    async def delete(self, ref: str) -> bytes: ...
    async def flushall(self) -> None: ...
    async def flushdb(self) -> None: ...


redis_cache: RedisTypeAlias = Redis(  # pyright: ignore[reportAssignmentType]
    encoding="utf-8",
    connection_pool=BlockingConnectionPool.from_url(  # pyright: ignore[reportUnknownMemberType]
        url=f"redis://{REDIS_HOST_IP}:{REDIS_PORT}",
        password=REDIS_PASSWORD,
    ),
)