"""
Minimal MCP server for the `mcp_tourists_agency` project.

Provides:
- a simple `add(a, b)` tool to verify MCP wiring;
- HTTP transport (`streamable-http`) on http://localhost:8000/mcp.

Run locally with:

    python server.py

Extend later by adding new tools and modules under the `tools` package.
"""

from mcp.server.fastmcp import FastMCP

from tools import register_all_tools


def create_server() -> FastMCP:
    """
    Create and configure a FastMCP server instance.

    Centralizes tool, resource, prompt, and auth registration so startup logic
    stays in one place.
    """
    mcp = FastMCP(
        name="Tourists Agency MCP",
        json_response=True,
    )

    # Регистрируем все тулзы проекта в одном месте.
    register_all_tools(mcp)

    return mcp


def main() -> None:
    """
    Application entry point.

    Runs FastMCP with the default `streamable-http` transport on port 8000 so
    any MCP client can connect to the `/mcp` endpoint.
    """
    mcp = create_server()
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()

