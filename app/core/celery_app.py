from celery import Celery
from app.core.settings import settings
from celery.schedules import crontab


celery_app = Celery(
    "url_shortener",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.conf.update(
    imports=['app.tasks']
)

celery_app.conf.beat_schedule = {
    "sync-clicks-every-60-seconds": {
        "task": "app.tasks.click_sync.sync_clicks_to_db",
        "schedule": 60.0,
    }
}
