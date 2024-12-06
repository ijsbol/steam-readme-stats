from fastapi import FastAPI
import uvicorn

from api.stats._slug_.router import router

app = FastAPI()


app.include_router(router, prefix="/api/stats/{steamid}")


uvicorn.run(app)
