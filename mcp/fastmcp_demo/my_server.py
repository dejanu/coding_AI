#!/usr/bin/env python3

from fastmcp import FastMCP

# stdion and stdout are supported by default

mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello good person {name}!"

if __name__ == "__main__":
    mcp.run()