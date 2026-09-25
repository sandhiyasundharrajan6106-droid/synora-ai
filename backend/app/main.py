from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database.db import init_db

app = FastAPI(
    title="Synora AI API",
    description="Prototype athlete cognitive readiness API",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "Synora AI"}


@app.get("/")
def root():
    return {
        "service": "Synora AI",
        "status": "running",
        "message": "Synora AI backend is running.",
        "health": "/health",
    }
