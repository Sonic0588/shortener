from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

from .models import Link
from .repositories import AbstractLinksRepository, LinksInMemoryRepository
from .services import create_short_link

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/ping")
async def liveness_ping() -> JSONResponse:
    return JSONResponse(content=dict(message="OK"))


@app.get("/{link_id}")
async def get_link(
    link_id: str,
    links_repo: AbstractLinksRepository = Depends(LinksInMemoryRepository),
) -> RedirectResponse:
    long_link = links_repo.get(link_id)
    return RedirectResponse(long_link)


@app.delete("/{link_id}")
async def delete_link(
    link_id: str,
    links_repo: AbstractLinksRepository = Depends(LinksInMemoryRepository),
) -> JSONResponse:
    links_repo.delete(link_id)
    return JSONResponse(content="", status_code=status.HTTP_204_NO_CONTENT)


@app.post("/links")
async def add_link(
    link: Link,
    links_repo: AbstractLinksRepository = Depends(LinksInMemoryRepository),
) -> JSONResponse:
    short_link = create_short_link(link.url, links_repo)
    return JSONResponse(content=dict(short_link=short_link))
