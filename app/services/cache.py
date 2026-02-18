from app.core.cache import async_redis_client
from app.db.session import SessionLocal
from app.models.url import URL

CACHE_PREFIX = "url:v1:"
CLICK_PREFIX = "clicks:"
DEFAULT_TTL = 3600  # 1 hour


async def get_cached_url(short_code: str) -> str | None:
    key = CACHE_PREFIX + short_code
    return await async_redis_client.get(key)


async def set_cached_url(short_code: str, original_url: str, ttl: int = DEFAULT_TTL):
    key = CACHE_PREFIX + short_code
    await async_redis_client.setex(key, ttl, original_url)


async def increment_cache(short_code: str) -> None:
    await async_redis_client.incr(CLICK_PREFIX + short_code)
