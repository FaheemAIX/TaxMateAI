from pathlib import Path
import os

print("Current Working Directory:", os.getcwd())
print(".env exists:", Path(".env").exists())

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

UPLOAD_DIR = Path("storage/uploads")