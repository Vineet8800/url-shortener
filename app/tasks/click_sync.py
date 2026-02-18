from app.core.cache import sync_redis_client
from app.db.session import SessionLocal
from app.models.url import URL
from app.core.celery_app import celery_app

CLICK_PREFIX = "clicks:"


@celery_app.task
def sync_clicks_to_db():
    db = SessionLocal()

    keys = sync_redis_client.keys(f"{CLICK_PREFIX}*")

    for key in keys:
        short_code = key.replace(CLICK_PREFIX, "")
        count = int(sync_redis_client.get(key) or 0)

        if count > 0:
            url = db.query(URL).filter(URL.short_code == short_code).first()
            if url:
                url.clicks += count
                db.commit()

            sync_redis_client.delete(key)

    db.close()
