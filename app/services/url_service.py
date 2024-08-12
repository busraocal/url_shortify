from typing import Optional
from app.models.url import Url
from app.repositories.url_repository import UrlRepository


class UrlService:
    def __init__(self, db_session):
        self.url_repository = UrlRepository(db_session)

    def get_url(self, url: str) -> Optional[Url]:
        return self.url_repository.get_url(url)

    def get_short_url(self, url: str) -> Optional[Url]:
        return self.url_repository.get_short_url(url)

    def create_url(self, original_url: str, short_url: str) -> Url:
        url = Url(original_url=original_url, short_url=short_url)
        return self.url_repository.create_url(url)
