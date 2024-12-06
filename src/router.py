from fastapi import FastAPI
import uvicorn

from api._slug_.stats.router import router as api_slug_stats_router
from api._slug_.stats.badge.playtime.router import router as api_slug_stats_badge_playtime_router


app = FastAPI()


app.include_router(api_slug_stats_router, prefix="/api/{steamid}/stats")
app.include_router(api_slug_stats_badge_playtime_router, prefix="/api/{steamid}/stats/badge/playtime")


uvicorn.run(app)
