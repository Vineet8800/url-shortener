from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    APP_NAME: str = "URL Shortener"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./shortener.db")
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")
    SECRET_KEY = os.getenv("SECRET_KEY", "0e6c3a9f4f7b8c2d1a5e9b3c6d7f8a1b4c2d9e6f7a1b3c5d8e9f0a2b4c6d8e1")


settings = Settings()
