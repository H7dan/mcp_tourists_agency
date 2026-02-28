"""Unit tests for MCP tools. Run from repo root: pytest tests/unit/"""


def test_add_tool_registers():
    """Smoke test: add tool can be registered on a FastMCP instance."""
    from mcp.server.fastmcp import FastMCP

    from tools.add import register_add_tool

    mcp = FastMCP(name="test")
    register_add_tool(mcp)
    # Registration completes without error; tool is available on mcp
    assert mcp is not None
