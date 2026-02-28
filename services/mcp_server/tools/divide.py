"""
Provide division as an MCP tool with explicit handling of division by zero.
"""

from mcp.server.fastmcp import FastMCP


def register_divide_tool(mcp: FastMCP) -> None:
    """Attach the `divide` tool to the given FastMCP server for remote calls."""

    @mcp.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide the first number by the second and return the result.

        Raises:
            ValueError: If the divisor is zero to avoid undefined behavior.
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
