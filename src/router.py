from http import HTTPStatus
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn

from api._slug_.stats.router import router as api_slug_stats_router
from api._slug_.stats.badge.playtime.router import router as api_slug_stats_badge_playtime_router
from api._slug_.stats.badge.games.router import router as api_slug_stats_badge_games_router


app = FastAPI()


app.include_router(api_slug_stats_router, prefix="/api/{steamid}/stats")
app.include_router(api_slug_stats_badge_playtime_router, prefix="/api/{steamid}/stats/badge/playtime")
app.include_router(api_slug_stats_badge_games_router, prefix="/api/{steamid}/stats/badge/games")



@app.exception_handler(HTTPStatus.NOT_FOUND)
async def exception_not_found(request: Request) -> RedirectResponse:
    return RedirectResponse(url="https://github.com/ijsbol/steam-readme-stats")


if __name__ == "__main__":
    uvicorn.run(app)
