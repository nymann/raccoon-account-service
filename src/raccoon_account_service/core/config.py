from pydantic_settings import BaseSettings

from raccoon_account_service.version import __version__


class Config(BaseSettings):
    title: str = "Raccoon Account Service"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
