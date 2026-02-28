"""Orchestrator config from environment."""

import os

# Port 8000: main API for bot and clients. MCP server uses 8001 to avoid conflict.
PORT = int(os.getenv("ORCHESTRATOR_PORT", "8000"))
HOST = os.getenv("ORCHESTRATOR_HOST", "0.0.0.0")
