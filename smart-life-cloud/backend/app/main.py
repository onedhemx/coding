from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import init_db
from .routers import auth, organizations, devices, telemetry, events


def create_app() -> FastAPI:
    app = FastAPI(title="Smart Life Cloud", version="0.1.0")

    # CORS for local development and SPA frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # tighten in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def _startup() -> None:
        init_db()

    # Routers
    app.include_router(auth.router)
    app.include_router(organizations.router)
    app.include_router(devices.router)
    app.include_router(telemetry.router)
    app.include_router(events.router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    # Common readiness/liveness aliases
    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    @app.get("/ready")
    def ready():
        return {"status": "ok"} 

    # Optional root info
    @app.get("/")
    def root():
        return {"service": "Smart Life Cloud", "version": app.version, "status": "ok"}

    return app


app = create_app()
