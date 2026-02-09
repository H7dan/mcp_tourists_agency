"""
Тул для вычитания двух чисел.
"""

from mcp.server.fastmcp import FastMCP


def register_subtract_tool(mcp: FastMCP) -> None:
    """Регистрирует тул subtract на переданном экземпляре FastMCP."""

    @mcp.tool()
    def subtract(a: int, b: int) -> int:
        """
        Вычесть второе число из первого и вернуть результат.

        Пример:
            subtract(5, 3) -> 2
            subtract(10, 7) -> 3
        """
        return a - b
