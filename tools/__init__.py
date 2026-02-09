"""
Пакет с тулзами MCP‑сервера для проекта `mcp_tourists_agency`.

Идея архитектуры:
- папка `tools/` — общий пакет для всех MCP‑тулов;
- внутри — отдельные файлы для каждого тула (например, `add.py`, `multiply.py` и т.д.);
- этот `__init__.py` централизованно регистрирует все тулзы на сервере.
"""

from mcp.server.fastmcp import FastMCP


def register_all_tools(mcp: FastMCP) -> None:
    """
    Зарегистрировать все тулзы на переданном экземпляре FastMCP.

    Здесь мы импортируем функции регистрации из отдельных модулей
    и вызываем их. Когда добавятся новые файлы с тулзами, достаточно
    дописать сюда ещё один импорт и вызов.
    """

    # Локальные импорты, чтобы избежать циклических зависимостей
    from .add import register_add_tool
    from .multiply import register_multiply_tool
    from .divide import register_divide_tool
    from .subtract import register_subtract_tool

    # Регистрируем все тулзы
    register_add_tool(mcp)
    register_multiply_tool(mcp)
    register_divide_tool(mcp)
    register_subtract_tool(mcp)
