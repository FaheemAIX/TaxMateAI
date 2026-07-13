# Import Path for creating platform-independent file paths.
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from the .env file.
    """

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

# Root folder where uploaded documents will be stored.
UPLOAD_DIR = Path("storage/uploads")