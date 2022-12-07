from pydantic import BaseSettings


class Settings(BaseSettings):
    url: str
    database: str
    username: str
    password: str

    class Config:
        env_file = ".env"
