from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults(api_key="TAVILY_API_KEY")
    res = search.run(f"{name}")
    return res[0]["url"]