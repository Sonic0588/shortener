from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = "https://shortener.xyz"


settings = Settings()
