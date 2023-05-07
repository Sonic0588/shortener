from abc import ABC, abstractmethod
from typing import Dict


class LinkNotFound(Exception):
    pass


class LinkAlreadyExists(Exception):
    pass


class AbstractLinksRepository(ABC):
    @abstractmethod
    def get(self, link_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def add(self, link: str, link_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def delete(self, link_id: str) -> None:
        raise NotImplementedError


class LinksInMemoryRepository(AbstractLinksRepository):
    links: Dict[str, str] = dict()

    def get(self, link_id: str) -> str:
        if link_id not in self.links:
            raise LinkNotFound
        return self.links[link_id]

    def add(self, link: str, link_id: str) -> str:
        if link_id in self.links:
            raise LinkAlreadyExists
        self.links[link_id] = link
        return link_id

    def delete(self, link_id: str) -> None:
        if link_id not in self.links:
            raise LinkNotFound
        del self.links[link_id]
