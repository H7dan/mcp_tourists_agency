"""Shared constants (tool names, limits, error codes) used across services.

User-facing text lives in shared.messages.
"""

# Orchestrator API (bot ↔ orchestrator)
ORCHESTRATOR_CHAT_ENDPOINT = "/v1/chat"

# Orchestrator 400: request has no text (error code in response body)
ERR_TEXT_REQUIRED = "text_required"

# Orchestrator 400: request has structurally invalid fields (types, etc.)
ERR_INVALID_REQUEST = "invalid_request"

# Orchestrator 400: request is missing user_id or chat_id
ERR_USER_ID_REQUIRED = "user_id_required"
ERR_CHAT_ID_REQUIRED = "chat_id_required"