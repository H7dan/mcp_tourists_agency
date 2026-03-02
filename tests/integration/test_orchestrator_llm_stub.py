"""Integration tests for orchestrator ↔ LLM stub flow.

Run from repo root:
    pytest tests/integration/test_orchestrator_llm_stub.py
"""

from fastapi.testclient import TestClient

from services.orchestrator.main import app


def _make_client() -> TestClient:
    return TestClient(app)


def test_chat_endpoint_success_uses_llm_stub() -> None:
    """Happy path: valid request goes through tg_bot_chat → llm_chat stub."""
    client = _make_client()

    payload = {"user_id": 123, "chat_id": 456, "text": "hello from tests"}
    response = client.post("/v1/chat", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "text" in data
    assert "LLM stub" in data["text"]
    assert "hello from tests" in data["text"]


def test_chat_endpoint_requires_text() -> None:
    """Validation: empty text should be rejected with 400 and error field."""
    client = _make_client()

    payload = {"user_id": 1, "chat_id": 2, "text": "   "}
    response = client.post("/v1/chat", json=payload)

    assert response.status_code == 400
    data = response.json()

    assert "error" in data

