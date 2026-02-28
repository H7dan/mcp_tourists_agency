"""
Minimal MCP server for the `mcp_tourists_agency` project.

Provides:
- a simple `add(a, b)` tool to verify MCP wiring;
- HTTP transport (`streamable-http`) on port 8001 by default (set FASTMCP_PORT to override).

Run from repo root:

    cd services/mcp_server && pip install -r requirements.txt && python server.py

Or with PYTHONPATH from root:

    pip install -r services/mcp_server/requirements.txt
    PYTHONPATH=services/mcp_server python services/mcp_server/server.py

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

    register_all_tools(mcp)

    return mcp


def main() -> None:
    """
    Application entry point.

    Runs FastMCP with streamable-http. Default port 8001 (FASTMCP_PORT) to avoid
    conflict with orchestrator (8000). MCP client connects to http://host:port/mcp.
    """
    mcp = create_server()
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
