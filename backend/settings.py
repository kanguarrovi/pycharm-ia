from typing import List
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API configs
    API_V0_STR: str = "/api/v0"
    APP_NAME: str = "Pycharm IA FastAPI Project"
    VERSION: str = "0.0.0"
    DESCRIPTION: str = "A REST API project using FastAPI into PyCharm with AI assistance."

    # Server configs
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    # CORS configs
    CORS_ORIGINS: List[str] = ["*"]

    # Add more settings as needed
    DEBUG: bool = False

    model_config = ConfigDict(
        env_file="../.venv",
        case_sensitive=True
    )

settings = Settings()