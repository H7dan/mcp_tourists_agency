"""
Base MCP server for the 'mcp_tourists_agency' project.

Сейчас сервер минимальный:
- один тестовый тул `add(a, b)` для проверки, что MCP работает;
- HTTP-транспорт (streamable-http) на http://localhost:8000/mcp.

Как запускать (после установки зависимостей из requirements.txt):

    python server.py

Потом вы сможете добавить новые модули/тулы (например, работу с DALL·E)
внутрь пакета `tools`.
"""

from mcp.server.fastmcp import FastMCP

from tools import register_all_tools


def create_server() -> FastMCP:
    """
    Создаёт и настраивает экземпляр MCP-сервера.

    Здесь удобно будет в будущем добавлять:
    - регистрацию новых тулов;
    - ресурсы;
    - промпты;
    - авторизацию и т.п.
    """
    mcp = FastMCP(
        name="Tourists Agency MCP",
        json_response=True,
    )

    # Регистрируем все тулзы проекта в одном месте.
    register_all_tools(mcp)

    return mcp


def main() -> None:
    """
    Точка входа в приложение.

    По умолчанию FastMCP с транспортом `streamable-http` поднимает HTTP‑сервер
    на порту 8000 с endpoint'ом `/mcp`, т.е.:
        http://localhost:8000/mcp

    К этому адресу уже может подключаться любой MCP‑клиент (например,
    MCP Inspector или IDE, поддерживающая MCP).
    """
    mcp = create_server()
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()

