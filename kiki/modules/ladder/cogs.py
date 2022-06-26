"""Ladder cogs.
"""

import os
import re

from discord.ext import commands
from discord.message import Message
from discord.utils import get

from kiki import Kiki
from kiki.utils import api


class Ladder(commands.Cog):
    """Ladder cog.
    """

    def __init__(self, bot: Kiki):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """Called whenever a message is sent.
        """

        # Ignore bots.
        if message.author.bot:
            return

        # Ignore messages not sent in lounge.
        if str(message.channel.id) != os.environ.get("CHANNEL_ID", "793970769842536458"):
            return

        # Parse valid emojis from message.
        content = message.content
        emojis = [e.split(':')[2].replace('>', '') for e in re.findall(r"<a?:\w*:\d*>", content)]

        # Send the API requests.
        await api.post("ladder", f"/messages/{message.author.id}")
        await api.post("ladder", f"/emotes/{message.author.id}", emojis)
