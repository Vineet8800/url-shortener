import redis
import redis.asyncio as async_redis
from app.core.settings import settings

async_redis_client = async_redis.Redis.from_url(
    settings.REDIS_HOST,
    decode_responses=True
)

sync_redis_client = redis.Redis.from_url(
    settings.REDIS_HOST,
    decode_responses=True
)
