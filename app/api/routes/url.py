from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime, UTC

from app.api.deps import get_db, get_current_user
from app.core.config import settings
from app.schemas.url import URLCreate, URLResponse, UserUrlResponse
from app.services.cache import get_cached_url, set_cached_url
from app.services.shortener import generate_unique_short_code
from app.models.url import URL
from app.models.users import User

from typing import List

router = APIRouter()


@router.get("/urls", response_model=List[UserUrlResponse])
def get_my_urls(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_urls = db.query(URL).filter(URL.user_id == current_user.id)
    return [
        UserUrlResponse(
            short_code=url.short_code,
            long_url=url.original_url,
            expiration=url.expires_at,
            clicks=url.clicks
        )
        for url in user_urls
    ]


@router.post("/shorten", response_model=URLResponse)
def create_short_url(
    payload: URLCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    short_code = generate_unique_short_code(db)

    url = URL(
        original_url=str(payload.original_url),
        short_code=short_code,
        expires_at=payload.expires_at,
        user_id=current_user.id,
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return {
        "short_code": url.short_code,
        "short_url": f"{settings.BASE_URL}/{url.short_code}",
    }


@router.get("/{short_code}")
async def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db),
):
    cached_url = await get_cached_url(short_code)
    if cached_url:
        return RedirectResponse(cached_url)

    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    if url.expires_at and url.expires_at < datetime.now(UTC):
        raise HTTPException(status_code=410, detail="URL expired")

    ttl = int((url.expires_at - datetime.now(UTC)).total_seconds()) if url.expires_at else 3600
    await set_cached_url(short_code, url.original_url, ttl)

    # Increment click count
    url.clicks += 1
    db.commit()

    return RedirectResponse(url.original_url)
