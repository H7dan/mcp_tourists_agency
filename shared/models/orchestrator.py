"""
DTOs for orchestrator ↔ bot communication.

Request: bot sends user_id, chat_id, text.
Response: orchestrator returns text (or error for failure).
"""

from dataclasses import dataclass

from shared.constants import ERROR_TEXT_REQUIRED
from shared.utils import is_text_empty


def get_request_validation_error(data: dict) -> str | None:
    """
    Check request body for /v1/chat. Returns error code if invalid, None if ok.
    Orchestrator should return 400 with {"error": code} when this is not None.
    """
    if is_text_empty(data.get("text")):
        return ERROR_TEXT_REQUIRED
    return None


@dataclass(frozen=True)
class OrchestratorRequest:
    """Request body: bot → orchestrator."""

    user_id: int
    chat_id: int
    text: str

    def to_dict(self) -> dict:
        return {"user_id": self.user_id, "chat_id": self.chat_id, "text": self.text}

    @classmethod
    def from_dict(cls, data: dict) -> "OrchestratorRequest":
        return cls(
            user_id=int(data["user_id"]),
            chat_id=int(data["chat_id"]),
            text=str(data["text"]).strip(),
        )


@dataclass(frozen=True)
class OrchestratorResponse:
    """Response body: orchestrator → bot. Success: text set. Error: error set."""

    text: str | None = None
    error: str | None = None

    def to_dict(self) -> dict:
        out: dict = {}
        if self.text is not None:
            out["text"] = self.text
        if self.error is not None:
            out["error"] = self.error
        return out

    @classmethod
    def from_dict(cls, data: dict) -> "OrchestratorResponse":
        return cls(
            text=data.get("text"),
            error=data.get("error"),
        )

    @classmethod
    def success(cls, text: str) -> "OrchestratorResponse":
        return cls(text=text, error=None)

    @classmethod
    def failure(cls, error: str) -> "OrchestratorResponse":
        return cls(text=None, error=error)
