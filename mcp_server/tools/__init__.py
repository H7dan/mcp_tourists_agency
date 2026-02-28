"""
MCP tools package for the `mcp_tourists_agency` project.

Each tool lives in its own module under `tools/`, and this `__init__.py`
centralizes their registration on the server for easier maintenance.
"""

from mcp.server.fastmcp import FastMCP


def register_all_tools(mcp: FastMCP) -> None:
    """
    Register all tools on the given FastMCP instance.

    Imports registration helpers from individual modules so adding a new tool
    only requires an extra import and function call here.
    """
    from .add import register_add_tool
    from .divide import register_divide_tool
    from .multiply import register_multiply_tool
    from .subtract import register_subtract_tool

    register_add_tool(mcp)
    register_divide_tool(mcp)
    register_multiply_tool(mcp)
    register_subtract_tool(mcp)
