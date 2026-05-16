import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_JWT_SECRET: str
    RAWG_API_KEY: str
    CORS_ALLOW_ORIGINS: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
