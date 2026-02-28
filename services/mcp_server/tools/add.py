"""
Expose a simple addition tool so clients can verify that MCP wiring works.
"""

from mcp.server.fastmcp import FastMCP


def register_add_tool(mcp: FastMCP) -> None:
    """Attach the `add` tool to the given FastMCP server so clients can call it."""

    @mcp.tool()
    def add(a: int, b: int) -> int:
        """
        Add two integers and return the sum.

        Kept intentionally simple to act as a sanity check tool.
        """
        return a + b
