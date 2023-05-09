import os
import random
import string

from .repositories import AbstractLinksRepository
from .settings import settings


def create_short_link(long_link: str, links_repo: AbstractLinksRepository) -> str:
    link_id = generate_link_id(7)
    links_repo.add(long_link, link_id)
    return os.path.join(settings.BASE_URL, link_id)


def generate_link_id(id_length: int, chars: str = string.ascii_letters) -> str:
    return "".join(random.choice(chars) for _ in range(id_length))
