from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = Field(8000, env="PORT")
    VERSION: str = Field("1.8.0", env="VERSION")
    class Config:
        env_file = ".env"

settings = Settings()