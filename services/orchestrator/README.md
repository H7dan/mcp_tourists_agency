# Orchestrator

Receives messages from bot, returns responses. LLM + MCP integration later.

Run from repo root:
```bash
pip install -r services/orchestrator/requirements.txt
PYTHONPATH=. python services/orchestrator/main.py
```

Or from this directory:
```bash
pip install -r requirements.txt
PYTHONPATH=../.. python main.py
```

Listens on port 8000 by default (MCP server uses 8001). Set `ORCHESTRATOR_PORT` to override.
