"""Auth0 utilities.
"""

# System imports.
import os
import time
import json
import base64
from typing import Optional, Tuple

import aiohttp

# Utility imports.
from kiki.utils import Singleton


class __TokenSingleton(Singleton):
    """Singleton to handle storing tokens and expirations.
    """

    expires: int = 0
    token: str = ""

    async def get_token(self) -> str:
        """Wrapper to return cached token or fresh.
        """

        # Fetch a new token if the old one expired.
        if (not self.token or self.expires > int(time.time()) - 60):
            expires, token = await self.__fetch_token()
            self.expires = expires
            self.token = token

        # Return the token.
        return self.token

    async def __fetch_token(self) -> Tuple[int, str]:
        """Fetch an API token from Auth0.
        """

        # Check configuration.
        client_id = os.environ.get("AUTH0_CLIENT_ID")
        client_secret = os.environ.get("AUTH0_CLIENT_SECRET")
        if (not client_id or not client_secret):
            return 0, None

        # Fetch a new token.
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://kikiandriki.us.auth0.com/oauth/token",
                json={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "audience": "kikiandriki",
                    "grant_type": "client_credentials",
                }
            ) as response:
                json_body = await response.json()
                expires_in = json_body.get("expires_in", 0)
                token: Optional[str] = json_body.get("access_token")

        # Throw if no token.
        if not token:
            raise Exception("Failed to retrieve token.")

        # Determine expiration.
        expires: int = int(time.time() + expires_in)

        # Return the responses.
        return expires, token


async def get_token():
    """Wrapper to get a token from Auth0.
    """

    # Return the token.
    auth0 = __TokenSingleton()
    return await auth0.get_token()
