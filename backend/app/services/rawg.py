import httpx
from typing import Optional, Dict, Any
from app.core.config import settings

RAWG_BASE_URL = "https://api.rawg.io/api"

async def fetch_games(query: Optional[str] = None, page: int = 1) -> Dict[str, Any]:
    """Fetches games from the RAWG API."""
    async with httpx.AsyncClient() as client:
        params = {"key": settings.RAWG_API_KEY, "page": page, "page_size": 20}
        if query:
            params["search"] = query
            
        response = await client.get(f"{RAWG_BASE_URL}/games", params=params)
        response.raise_for_status()
        return response.json()

async def fetch_game_details(game_id: int) -> Dict[str, Any]:
    """Fetches full details for a single game from RAWG."""
    async with httpx.AsyncClient() as client:
        params = {"key": settings.RAWG_API_KEY}
        response = await client.get(f"{RAWG_BASE_URL}/games/{game_id}", params=params)
        response.raise_for_status()
        return response.json()
