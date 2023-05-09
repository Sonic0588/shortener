from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = "https://shortener.xyz"
    DB_HOST: str = ""
    DB_PASSWORD: str = ""
    DB_USER: str = ""
    DB_DATABASE: str = ""


settings = Settings()
