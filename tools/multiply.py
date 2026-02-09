"""
Тул для умножения двух чисел.
"""

from mcp.server.fastmcp import FastMCP


def register_multiply_tool(mcp: FastMCP) -> None:
    """Регистрирует тул multiply на переданном экземпляре FastMCP."""

    @mcp.tool()
    def multiply(a: int, b: int) -> int:
        """
        Умножить два числа и вернуть результат.

        Пример:
            multiply(2, 3) -> 6
        """
        return a * b
