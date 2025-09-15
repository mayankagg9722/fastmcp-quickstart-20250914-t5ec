from fastmcp import FastMCP

# Create a comprehensive MCP server for testing
mcp = FastMCP("TestMCPServer")

# Mathematical Tools
@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

# System Utilities
@mcp.tool
def echo(message: str) -> str:
    """Echoes back the given message."""
    return f"Echo: {message}"


if __name__ == "__main__":
    mcp.run()