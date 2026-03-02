"""
Orchestrator entry point.

Receives requests from bot (and future clients), returns responses.
Run from repo root: PYTHONPATH=. python services/orchestrator/main.py
"""

import logging
import sys

from fastapi import FastAPI

try:
    # When imported as a package: services.orchestrator.main
    from .config import HOST, PORT
    from .api.tg_bot_chat import router as chat_router
except ImportError:  # pragma: no cover - fallback for direct script execution
    # When run as a script from services/orchestrator: python main.py
    from config import HOST, PORT
    from api.tg_bot_chat import router as chat_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stdout,
)

app = FastAPI(title="Tourists Agency Orchestrator")
app.include_router(chat_router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
