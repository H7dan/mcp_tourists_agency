# Project structure

Summary of the repository layout and how services relate.

## Containers (4)

| Container       | Role |
|-----------------|------|
| **llm**         | LLM service (e.g. Ollama). |
| **db**          | Database (PostgreSQL or other). |
| **orchestrator**| Single entry point for all clients: receives requests, calls LLM + MCP, returns responses. No Telegram-specific logic. |
| **bot**         | Telegram adapter only: receives messages → calls orchestrator (HTTP) → sends reply. |

Flow: **User → Bot → Orchestrator → LLM + MCP (+ DB)**. Other clients (Web, API) can call the orchestrator the same way.

## Folder layout

```
mcp_tourists_agency/
├── docker/
│   ├── docker-compose.yml    # all services
│   └── .env.example
│
├── services/
│   ├── llm/                  # Container: LLM
│   ├── db/                   # Container: DB + migrations
│   └── bot/                  # Container: Telegram bot (calls orchestrator)
│   # orchestrator/            # To add: orchestration API (LLM + MCP client)
│
├── mcp_server/               # MCP server + tools (run in orchestrator or separate)
│   ├── server.py
│   ├── requirements.txt
│   └── tools/
│
├── shared/                   # Shared code: DTOs, constants, utils (no service logic)
│   ├── models/
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

- **services/llm**, **services/db** — infrastructure only.
- **services/bot** — Telegram handlers; calls orchestrator over HTTP; may use `shared` for DTOs/constants.
- **orchestrator** (to add) — orchestration logic and API; depends on `shared`, optionally on `mcp_server` if embedded.
- **mcp_server** — MCP tools; can use `shared` for request/response shapes.
- **shared** — single source of truth for types, constants, and small helpers used by several services.
- **tests** — unit tests (isolated) and integration tests (services together).

## Running locally

- **MCP server only:** from repo root, `cd mcp_server && pip install -r requirements.txt && python server.py` (or set `PYTHONPATH` and run from root).
- **Full stack:** from repo root, `docker compose -f docker/docker-compose.yml up` (after configuring `.env` from `docker/.env.example`).
