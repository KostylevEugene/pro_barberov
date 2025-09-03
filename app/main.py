import uvicorn
from fastapi import FastAPI

from app.settings.settings import app_settings
from app.api.routers import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=app_settings.app_port,
        reload=app_settings.debug,
        workers=app_settings.app_workers,
    )
