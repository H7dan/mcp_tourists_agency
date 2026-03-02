# Project structure

Summary of the repository layout and how services relate.

## Containers (4)

| Container       | Role |
|-----------------|------|
| **llm**         | LLM service (e.g. Ollama). |
| **db**          | Database (PostgreSQL or other). |
| **orchestrator**| Single entry point for all clients: receives requests, calls LLM + MCP, returns responses. No Telegram-specific logic. |
| **tg_bot**      | Telegram adapter only: receives messages → calls orchestrator (HTTP) → sends reply. |

Flow: **User → Bot → Orchestrator → LLM + MCP (+ DB)**. Other clients (Web, API) can call the orchestrator the same way.

**Note:** `docker/docker-compose.yml` is currently a placeholder; services are run locally (see below).

## Folder layout

```
mcp_tourists_agency/
├── docker/
│   ├── docker-compose.yml    # placeholder; define llm, db, orchestrator, bot when ready
│   └── .env.example
│
├── services/
│   ├── llm/                  # Container: LLM (placeholder)
│   ├── db/                   # Container: DB + migrations (placeholder)
│   ├── tg_bot/               # Telegram bot (aiogram 3); calls orchestrator HTTP
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── .env.example
│   ├── orchestrator/         # FastAPI: /health, POST /v1/chat (LLM + MCP integration TBD)
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── api/
│   │   │   └── chat.py
│   │   └── requirements.txt
│   └── mcp_server/           # MCP server + tools (stdio; port 8001 if needed)
│       ├── server.py
│       ├── requirements.txt
│       ├── .env.example
│       └── tools/            # add, subtract, multiply, divide
│
├── shared/                   # Shared code: DTOs, constants, messages, utils (no service logic)
│   ├── models/               # OrchestratorRequest, OrchestratorResponse, etc.
│   ├── messages/             # User-facing copy (welcome, errors, placeholders)
│   ├── constants.py
│   └── utils.py
│
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
│
├── docs/
├── .cursor/
├── .gitignore
└── README.md
```

## Responsibilities

- **services/llm**, **services/db** — infrastructure only (placeholders).
- **services/tg_bot** — Telegram handlers (aiogram 3); calls orchestrator over HTTP; uses `shared` for DTOs, constants, and messages.
- **services/orchestrator** — FastAPI app: `GET /health`, `POST /v1/chat` (request body: `user_id`, `chat_id`, `text`; returns `{text}` or `{error}`). Stub implementation; LLM + MCP integration planned. Depends on `shared`.
- **services/mcp_server** — MCP tools (add, subtract, multiply, divide); can use `shared` for request/response shapes.
- **shared** — single source of truth: `models/` (DTOs), `messages/` (user-facing copy), `constants.py`, `utils.py`. Used by tg_bot, orchestrator, and optionally mcp_server.
- **tests** — unit tests (isolated) and integration tests (services together).

## Running locally

- **Orchestrator:** from repo root, `PYTHONPATH=. python services/orchestrator/main.py` (default: `http://0.0.0.0:8000`). Config: `ORCHESTRATOR_PORT`, `ORCHESTRATOR_HOST`.
- **Telegram bot:** from repo root, `PYTHONPATH=. python services/tg_bot/main.py`. Requires `BOT_TOKEN` and optionally `ORCHESTRATOR_URL` in `services/tg_bot/.env` (see `.env.example`). If `ORCHESTRATOR_URL` is unset, bot shows a placeholder message.
- **MCP server:** from repo root, `cd services/mcp_server && pip install -r requirements.txt && python server.py` (or set `PYTHONPATH` and run from root).
- **Full stack (Docker):** not yet defined; `docker compose -f docker/docker-compose.yml` is a placeholder. Use the commands above to run services locally.
