# Shared helpers (formatting, validation) used by MCP, orchestrator, and bot.


def is_text_empty(text: str | None) -> bool:
    """True if text is missing or only whitespace. Used by bot and orchestrator."""
    return not text or not str(text).strip()
