from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/ping")
async def liveness_ping() -> JSONResponse:
    return JSONResponse(content=dict(message="OK"))
