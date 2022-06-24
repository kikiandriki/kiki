"""API utilities.
"""

# External imports.
import os
from typing import Dict, Optional, Literal
import aiohttp

# Utility imports.
from kiki.utils import auth0


def _get_base_url(api: Literal["ladder"]) -> str:
    """Get the API base URL.
    """

    api_urls = {
      "disque": os.environ.get("API_DISQUE_BASE_URL", "http://localhost:3001"),
      "ladder": os.environ.get("API_LADDER_BASE_URL", "http://localhost:3002"),
    }

    return api_urls[api]


async def get(api: Literal["ladder"], url: str):
    """Wrapper for HTTP GET requests.
    """

    base_url = _get_base_url(api)
    token = await auth0.get_token()

    async with aiohttp.ClientSession(
        headers={"Authorization": f"Bearer {token}"}
    ) as session:
        async with session.get(f"{base_url}{url}") as response:
            return await response.json()


async def put(api: Literal["ladder"], url: str, data: Optional[Dict[str, any]]):
    """Wrapper for HTTP PUT requests.
    """

    base_url = _get_base_url(api)
    token = await auth0.get_token()

    async with aiohttp.ClientSession(
        headers={"Authorization": f"Bearer {token}"}
    ) as session:
        async with session.put(f"{base_url}{url}", json=data) as response:
            return await response.json()


async def post(api: Literal["ladder"], url: str, data: Optional[Dict[str, any]] = None):
    """Wrapper for HTTP POST requests.
    """

    base_url = _get_base_url(api)
    token = await auth0.get_token()

    async with aiohttp.ClientSession(
        headers={"Authorization": f"Bearer {token}"}
    ) as session:
        async with session.post(f"{base_url}{url}", json=data) as response:
            return await response.json()


async def delete(api: Literal["ladder"], url: str):
    """Wrapper for HTTP DELETE requests.
    """

    base_url = _get_base_url(api)
    token = await auth0.get_token()

    async with aiohttp.ClientSession(
        headers={"Authorization": f"Bearer {token}"}
    ) as session:
        async with session.delete(f"{base_url}{url}") as response:
            return await response.json()
