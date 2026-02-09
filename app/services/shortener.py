import random
import string

from sqlalchemy.orm import Session
from app.models.url import URL

BASE62 = string.ascii_letters + string.digits
DEFAULT_LENGTH = 7


def generate_short_code(length: int = DEFAULT_LENGTH) -> str:
    return "".join(random.choices(BASE62, k=length))


def generate_unique_short_code(
    db: Session,
    length: int = DEFAULT_LENGTH,
    max_attempts: int = 5
) -> str:
    for _ in range(max_attempts):
        code = generate_short_code(length)
        exists = db.query(URL).filter(URL.short_code == code).first()
        if not exists:
            return code

    raise RuntimeError("Failed to generate unique short code")
