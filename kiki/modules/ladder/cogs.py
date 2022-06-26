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
        server_id = os.environ.get("SERVER_ID", "558027628502712330")
        emojis = re.findall(r"<:\w*:\d*>", message.content)
        emojis = [int(e.split(':')[2].replace('>', '')) for e in emojis]
        custom_emojis = self.bot.get_guild(int(server_id)).emojis
        valid_emojis = [get(custom_emojis, id=e) for e in emojis]
        emoji_ids = [str(e.id) for e in filter(lambda x: x is not None, valid_emojis)]

        # Send the API requests.
        await api.post("ladder", f"/messages/{message.author.id}")
        await api.post("ladder", f"/emotes/{message.author.id}", emoji_ids)
