from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, UTC

from app.api.deps import get_db, get_current_user
from app.schemas.url import URLCreate, URLResponse
from app.models.url import URL
from app.services.shortener import generate_unique_short_code
from app.core.config import settings
from app.models.users import User

router = APIRouter()


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
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db),
):
    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    if url.expires_at and url.expires_at < datetime.now(UTC):
        raise HTTPException(status_code=410, detail="URL expired")

    # Increment click count
    url.clicks += 1
    db.commit()

    return RedirectResponse(url.original_url)
