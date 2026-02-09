"""
Тул для деления двух чисел.
"""

from mcp.server.fastmcp import FastMCP


def register_divide_tool(mcp: FastMCP) -> None:
    """Регистрирует тул divide на переданном экземпляре FastMCP."""

    @mcp.tool()
    def divide(a: float, b: float) -> float:
        """
        Разделить первое число на второе и вернуть результат.

        Пример:
            divide(10, 2) -> 5.0
            divide(7, 2) -> 3.5

        Raises:
            ValueError: Если делитель равен нулю.
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
