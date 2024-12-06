from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from api.utils import get_user_stats


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter()


@router.get(path="/")
async def api_slug_stats(
    request: Request,
    steamid: str,
) -> JSONResponse:
    user_stats = await get_user_stats(steamid)
    return JSONResponse(
        content=user_stats,
        status_code=200,
    )
