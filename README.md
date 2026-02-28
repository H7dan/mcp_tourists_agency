# MCP Tourists Agency Server

MCP (Model Context Protocol) сервер для турагентства на Python. В перспективе — несколько сервисов (LLM, БД, оркестратор, Telegram-бот).

## Описание

Проект содержит MCP‑сервер с инструментами (tools) для туристических данных. Используется FastMCP и транспорт HTTP (streamable-http). Структура заложена под дальнейшее добавление оркестратора, бота и других клиентов.

## Структура проекта

См. **[docs/architecture.md](docs/architecture.md)** — описание контейнеров, папок и ответственности.

Кратко:

```
mcp_tourists_agency/
├── docker/                 # docker-compose и .env.example
├── services/
│   ├── llm/                # Контейнер LLM
│   ├── db/                 # Контейнер БД
│   └── tg_bot/                # Telegram-бот
├── mcp_server/             # MCP-сервер и тулзы
│   ├── server.py
│   ├── requirements.txt
│   └── tools/
├── shared/                 # Общие модели, константы, утилиты
├── tests/                  # unit/ и integration/
└── docs/
```

## Установка и запуск MCP-сервера

1. Установите зависимости и запустите сервер:

```bash
cd mcp_server
pip install -r requirements.txt
python server.py
```

Сервер будет доступен на `http://localhost:8000/mcp`.

2. Либо из корня репозитория (если `pip install` уже выполнен для `mcp_server`):

```bash
pip install -r mcp_server/requirements.txt
cd mcp_server && python server.py
```

## Остановка сервера

В терминале: **Ctrl + C** (Windows/Linux) или **Cmd + C** (Mac).

## Подключение к серверу

### Через Cursor IDE

Используется `.cursor/mcp.json` (URL `http://127.0.0.1:8000/mcp`). После запуска `python server.py` из папки `mcp_server` тулзы доступны в Cursor.

### Через MCP Inspector

1. Запустите инспектор:
   ```bash
   npx -y @modelcontextprotocol/inspector
   ```
2. Транспорт: **HTTP**, URL: `http://127.0.0.1:8000/mcp` → **Connect**.

## Доступные тулзы

- `add(a, b)` — сложение двух чисел
- `multiply(a, b)` — умножение двух чисел
- `divide(a, b)` — деление двух чисел
- `subtract(a, b)` — вычитание двух чисел

## Разработка

- **Новые тулзы:** создайте модуль в `mcp_server/tools/`, реализуйте `register_<name>_tool(mcp)`, добавьте импорт и вызов в `mcp_server/tools/__init__.py` в `register_all_tools()`.
- **Общая логика:** модели и константы для нескольких сервисов — в `shared/`.
- **Архитектура:** см. [docs/architecture.md](docs/architecture.md).
