# Shared constants (tool names, limits, error codes) used across services.
# User-facing text lives in shared.messages.

# Orchestrator API (bot ↔ orchestrator)
ORCHESTRATOR_CHAT_ENDPOINT = "/v1/chat"

# Orchestrator 400: request has no text (error code in response body)
ERROR_TEXT_REQUIRED = "text_required"
