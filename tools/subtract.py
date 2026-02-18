"""
Provide subtraction as an MCP tool so arithmetic operations stay symmetric.
"""

from mcp.server.fastmcp import FastMCP


def register_subtract_tool(mcp: FastMCP) -> None:
    """Attach the `subtract` tool to the given FastMCP server for remote use."""

    @mcp.tool()
    def subtract(a: int, b: int) -> int:
        """
        Subtract the second integer from the first and return the result.

        Mirrors the `add` tool to keep the arithmetic API consistent.
        """
        return a - b
