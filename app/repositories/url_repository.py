from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError

from app.models.url import Url
from app.core.logger import logger


class UrlRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_url(self, url: str) -> Optional[Url]:
        try:
            url = self.db_session.query(Url).filter(Url.original_url == url).first()
            if url:
                logger.info(f"Url {url} fetched successfully.")
                return {"original_url": url.original_url, "short_url": url.short_url}
        except SQLAlchemyError as e:
            logger.error(f"Error fetching url {url}: {e}")
            raise e

    def get_short_url(self, short_url: str) -> Optional[Url]:
        try:
            short_url = self.db_session.query(Url).filter(Url.short_url == short_url).first()
            if short_url:
                logger.info(f"Url {short_url} fetched successfully.")
            else:
                logger.info(f"No short url found  {short_url}.")
            return short_url
        except SQLAlchemyError as e:
            logger.error(f"Error fetching url {short_url}: {e}")
            raise e

    def create_url(self, url: Url) -> Url:
        try:
            self.db_session.add(url)
            self.db_session.commit()
            self.db_session.refresh(url)
            logger.info(f"Url created successfully: {url}")
            return url
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise e
