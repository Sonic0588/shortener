from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import Session
from sqlalchemy.sql import text


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


class LinksDBRepository(AbstractLinksRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, link_id: str) -> str:
        query = "SELECT long_link FROM urls WHERE link_id = :link_id AND deleted IS NOT true"
        link = self.session.execute(text(query), {"link_id": link_id}).fetchone()
        if not link:
            raise LinkNotFound
        return link.long_link

    def add(self, link: str, link_id: str) -> str:
        query = "INSERT INTO urls (link_id, long_link) VALUES (:link_id, :long_link)"
        self.session.execute(text(query), {"link_id": link_id, "long_link": link})
        self.session.commit()
        return link_id

    def delete(self, link_id: str) -> None:
        query = "UPDATE urls SET deleted = true WHERE link_id = :link_id"
        self.session.execute(text(query), {"link_id": link_id})
        self.session.commit()
