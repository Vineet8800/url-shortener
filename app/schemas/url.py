from datetime import datetime
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl
    expires_at: datetime | None = None


class URLResponse(BaseModel):
    short_url: str

    class Config:
        from_attributes = True


class UserUrlResponse(BaseModel):
    short_code: str
    long_url: str
    expiration: datetime | None
    clicks: int

    class Config:
        from_attributes = True
