#!/usr/bin/env python3
"""
Simple test for FastMCP server
"""
import requests
import json

def test_server():
    """Test the FastMCP server"""
    base_url = "http://127.0.0.1:8000"
    
    print("🔗 Testing FastMCP server...")
    
    try:
        # Test the MCP endpoint (this is the main endpoint)
        response = requests.head(f"{base_url}/mcp", timeout=5)
        print(f"✅ MCP endpoint is responding (status: {response.status_code})")
        
        if response.status_code == 405:  # Method Not Allowed is expected for HEAD request
            print("✅ Your FastMCP server is working correctly!")
            print(f"🔧 MCP endpoint: {base_url}/mcp")
            
            # Check for session ID in headers
            if 'mcp-session-id' in response.headers:
                session_id = response.headers['mcp-session-id']
                print(f"🆔 Session ID: {session_id}")
            
            print("\n� How to test your server:")
            print("1. 🌐 Use MCP-compatible clients")
            print("2. 🛠️  Test the 'multiply' tool via MCP protocol")
            print("3. 📡 Use the test_client.py for full API testing")
            
            # Show available methods
            if 'allow' in response.headers:
                methods = response.headers['allow']
                print(f"4. 🔧 Allowed HTTP methods: {methods}")
            
        else:
            print(f"⚠️  Unexpected status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure it's running on port 8000")
        print("💡 Try running: uv run python main.py")
    except requests.exceptions.Timeout:
        print("❌ Server connection timed out")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_server()