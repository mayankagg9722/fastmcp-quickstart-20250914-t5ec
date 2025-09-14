from fastmcp import FastMCP
import json
import datetime
import random
import requests
from typing import List, Dict, Any, Optional

# Create a comprehensive MCP server for testing
mcp = FastMCP(
    name="TestMCPServer",
    instructions="""
        This is a comprehensive MCP server for testing various functionalities.
        Available tools:
        - Mathematical operations (add, multiply, power)
        - Text processing (reverse_text, count_words, capitalize_words)
        - Data operations (generate_random_data, format_json)
        - Time utilities (current_time, days_between)
        - Web utilities (fetch_url, get_status_code)
        - System utilities (echo, generate_uuid)
    """,
)

# Mathematical Tools
@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raises base to the power of exponent."""
    return base ** exponent

# Text Processing Tools
@mcp.tool
def reverse_text(text: str) -> str:
    """Reverses the given text."""
    return text[::-1]

@mcp.tool
def count_words(text: str) -> int:
    """Counts the number of words in the given text."""
    return len(text.split())

@mcp.tool
def capitalize_words(text: str) -> str:
    """Capitalizes the first letter of each word in the text."""
    return text.title()

# Data Generation Tools
@mcp.tool
def generate_random_data(count: int = 5) -> List[Dict[str, Any]]:
    """Generates random test data with specified count."""
    data = []
    for i in range(count):
        data.append({
            "id": i + 1,
            "name": f"User_{random.randint(1000, 9999)}",
            "age": random.randint(18, 80),
            "score": round(random.uniform(0, 100), 2),
            "active": random.choice([True, False])
        })
    return data

@mcp.tool
def format_json(data: str) -> str:
    """Formats a JSON string with proper indentation."""
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=2)
    except json.JSONDecodeError:
        return "Invalid JSON format"

# Time Utilities
@mcp.tool
def current_time() -> str:
    """Returns the current date and time."""
    return datetime.datetime.now().isoformat()

@mcp.tool
def days_between(date1: str, date2: str) -> int:
    """Calculates the number of days between two dates (YYYY-MM-DD format)."""
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except ValueError:
        return -1

# Web Utilities
@mcp.tool
def fetch_url(url: str) -> str:
    """Fetches content from a URL and returns the response text (limited to first 1000 chars)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text[:1000] + ("..." if len(response.text) > 1000 else "")
    except requests.RequestException as e:
        return f"Error fetching URL: {str(e)}"

@mcp.tool
def get_status_code(url: str) -> int:
    """Gets the HTTP status code for a given URL."""
    try:
        response = requests.head(url, timeout=10)
        return response.status_code
    except requests.RequestException:
        return -1

# System Utilities
@mcp.tool
def echo(message: str) -> str:
    """Echoes back the given message."""
    return f"Echo: {message}"

@mcp.tool
def generate_uuid() -> str:
    """Generates a random UUID string."""
    import uuid
    return str(uuid.uuid4())

# Resource for testing
@mcp.resource("test://data")
def get_test_data() -> str:
    """Returns sample test data."""
    return json.dumps({
        "server": "TestMCPServer",
        "version": "1.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "sample_data": generate_random_data(3)
    }, indent=2)

if __name__ == "__main__":
    print("Starting FastMCP Test Server...")
    print("Available tools:")
    print("- Mathematical: add, multiply, power")
    print("- Text: reverse_text, count_words, capitalize_words")
    print("- Data: generate_random_data, format_json")
    print("- Time: current_time, days_between")
    print("- Web: fetch_url, get_status_code")
    print("- System: echo, generate_uuid")
    print("\nServer running on stdio...")
    mcp.run()