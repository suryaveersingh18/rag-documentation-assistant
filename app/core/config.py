from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "RAG Technical Documentation Assistant"

    environment: str = "development"
    debug: bool = True

    google_api_key: str = Field(..., alias="GOOGLE_API_KEY")

    llm_model: str = Field(
        default="gemini-2.5-flash-lite",
        alias="LLM_MODEL",
    )

    llm_temperature: float = Field(
        default=0.0,
        alias="LLM_TEMPERATURE",
    )

    embedding_model: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2",
        alias="EMBEDDING_MODEL",
    )

    chroma_db: str = Field(
        default="database/chroma",
        alias="CHROMA_DB",
    )

    collection_name: str = Field(
        default="technical_docs",
        alias="COLLECTION_NAME",
    )

    top_k: int = Field(
        default=5,
        alias="TOP_K",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()