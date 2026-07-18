from pathlib import Path
import os

# print("Current Working Directory:", os.getcwd())
# print(".env exists:", Path(".env").exists())

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

# Root folder where uploaded documents will be stored.
UPLOAD_DIR = Path("storage/uploads")

# Root folder where FAISS index and chunk files will be stored.
VECTORSTORE_DIR = Path("storage/vectorstore")

# Create storage directories automatically if they do not exist.
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

'''parents=True allows Python to create all missing parent directories automatically. If storage/ or vectorstore/ does not exist, Python creates the complete directory hierarchy instead of raising a FileNotFoundError.

Python always tries to create the directory.
If it already exists:
exist_ok=False (default) → ❌ Raise FileExistsError
exist_ok=True → ✅ Ignore the error and continue

exist_ok=True prevents Python from raising an exception if the directory already exists, making the operation safe to execute every time the application starts.
'''