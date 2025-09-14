from fastmcp import FastMCP

# Create a server instance with instructions
mcp = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides mathematical tools.
        Call multiply() to multiply two numbers together.
    """,
)

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

if __name__ == "__main__":
    mcp.run()