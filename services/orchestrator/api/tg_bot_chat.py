"""Chat endpoint for Telegram bot: receive message, return response."""

import logging

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from shared.constants import ERR_TEXT_REQUIRED
from shared.models import OrchestratorRequest, OrchestratorResponse, get_request_validation_error
from .llm_chat import run_llm_chat

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/v1/chat")
async def chat(request: Request) -> JSONResponse:
    """
    Receive message from bot, return text response.
    Body: {user_id, chat_id, text}. Response: {text} or {error}.
    """
    try:
        body = await request.json()
    except Exception as e:
        logger.exception("Invalid JSON body: %s", e)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=OrchestratorResponse.failure("invalid_json").to_dict(),
        )

    err = get_request_validation_error(body)
    if err:
        logger.warning("Validation error: %s", err)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": err},
        )

    try:
        req = OrchestratorRequest.from_dict(body)
    except (KeyError, TypeError, ValueError) as e:
        logger.exception("Failed to parse request: %s", e)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": ERR_TEXT_REQUIRED},
        )

    # Hand off to LLM orchestration layer (currently a stub).
    resp = await run_llm_chat(req)
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp.to_dict())

