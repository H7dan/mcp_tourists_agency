"""Pytest fixtures and config shared by unit and integration tests."""

import sys
from pathlib import Path

# Allow importing mcp_server packages (e.g. tools) when running pytest from repo root.
_repo_root = Path(__file__).resolve().parent.parent
_mcp_server = _repo_root / "services" / "mcp_server"
if _mcp_server.exists() and str(_mcp_server) not in sys.path:
    sys.path.insert(0, str(_mcp_server))
