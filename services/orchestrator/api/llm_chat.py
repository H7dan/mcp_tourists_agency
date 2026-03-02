"""Internal LLM + MCP chat orchestration.

Right now this module only provides a stub implementation so that the
Telegram bot → orchestrator → LLM chain is wired end‑to‑end.
Real LLM + MCP logic will be added later.
"""

from shared.models import OrchestratorRequest, OrchestratorResponse


async def run_llm_chat(req: OrchestratorRequest) -> OrchestratorResponse:
    """Run LLM + tools flow for a single orchestrator request (stub)."""
    # Stub implementation: echo back that the orchestrator received the text.
    # Later this will call a real LLM backend and MCP tools.
    return OrchestratorResponse.success(
        f"LLM stub: orchestrator received your message: {req.text!r}. "
        "LLM + MCP integration is not implemented yet."
    )

