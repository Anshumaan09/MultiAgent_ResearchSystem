import os
from tavily import TavilyClient


search_tool = TavilyClient( api_key=os.getenv("TAVILY_API_KEY"))


def search_web(query: str, max_results: int = 5) -> str:
    """
    Search the web using Tavily and return formatted results.
    """

    results = search_tool.search( query=query, max_results=max_results)

    formatted_results = []

    for item in results.get("results", []):
        formatted_results.append( f"""
Title: {item.get('title', '')}
URL: {item.get('url', '')}
Content: {item.get('content', '')}
""".strip())

    return "\n\n".join(formatted_results)