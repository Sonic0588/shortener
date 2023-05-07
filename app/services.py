import hashlib
import os

from .repositories import AbstractLinksRepository
from .settings import settings


def create_short_link(long_link: str, links_repo: AbstractLinksRepository) -> str:
    link_id = make_link_id(long_link)
    links_repo.add(long_link, link_id)
    return os.path.join(settings.BASE_URL, link_id)


def make_link_id(link: str) -> str:
    return hashlib.sha256(bytes(link, "utf-8")).hexdigest()
