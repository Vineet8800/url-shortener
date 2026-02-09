from datetime import datetime
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl
    expires_at: datetime | None = None


class URLResponse(BaseModel):
    short_url: str

    class Config:
        from_attributes = True
