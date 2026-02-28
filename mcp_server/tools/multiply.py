"""
Provide multiplication as its own MCP tool for reuse across future features.
"""

from mcp.server.fastmcp import FastMCP


def register_multiply_tool(mcp: FastMCP) -> None:
    """Attach the `multiply` tool to the given FastMCP server for remote calls."""

    @mcp.tool()
    def multiply(a: int, b: int) -> int:
        """
        Multiply two integers and return the product.

        Keeps numeric operations together so clients can rely on one MCP server.
        """
        return a * b
