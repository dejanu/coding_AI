#!/usr/bin/env python3
import asyncio
from fastmcp import Client

# stdio connection to the server
client = Client("my_server.py")

# http connection to the server
# client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client as c:
        result = await c.call_tool("greet", {"name": name})
        # result is a CallToolResult object
        print(result.data)

asyncio.run(call_tool("Alex"))