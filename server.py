# server.py
from mcp.server.fastmcp import FastMCP
import requests
import json
# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("bibin was here!!!")
    return a + b

@mcp.tool()
def search_documentation(question_about_capability: str) -> str:
    """Search for an answer to any question from the user related to Documents capability"""
    # Here you can implement your logic to answer the query
    # For demonstration, we'll just return a simple response
    url = 'http://localhost:8000/ask_question'
    headers = {'Content-Type': 'application/json'}
    # data = {'query': 'Where is the config files located?'}
    data = {
        "query": f"{question_about_capability}",
    }
    response = requests.post(url, data=json.dumps(data),headers=headers)
    # mcp.logger.info(f"Response from the server: {response}")
    return response.json()

mcp.run()