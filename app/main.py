from fastapi import FastAPI
from app.core.settings import settings
from app.db.session import engine
from app.db.base import Base

from app.api.routes import url_router
from app.api.routes.auth import router as auth_router
import app.models


app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(url_router)
app.include_router(auth_router)


@app.get("/")
def health_check():
    return {"status": "ok"}
