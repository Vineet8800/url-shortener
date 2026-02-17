from app.core.cache import redis_client

CACHE_PREFIX = "url:v1:"
DEFAULT_TTL = 3600  # 1 hour


async def get_cached_url(short_code: str) -> str | None:
    key = CACHE_PREFIX + short_code
    return await redis_client.get(key)


async def set_cached_url(short_code: str, original_url: str, ttl: int = DEFAULT_TTL):
    key = CACHE_PREFIX + short_code
    await redis_client.setex(key, ttl, original_url)
