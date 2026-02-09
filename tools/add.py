"""
Тул для сложения двух чисел.
"""

from mcp.server.fastmcp import FastMCP


def register_add_tool(mcp: FastMCP) -> None:
    """Регистрирует тул add на переданном экземпляре FastMCP."""

    @mcp.tool()
    def add(a: int, b: int) -> int:
        """
        Сложить два числа и вернуть результат.

        Пример:
            add(2, 3) -> 5
        """
        return a + b
