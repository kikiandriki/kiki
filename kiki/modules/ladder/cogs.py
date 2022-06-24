"""Ladder cogs.
"""

from discord.ext import commands
from discord.message import Message

from kiki.utils import api


class Ladder(commands.Cog):
    """Ladder cog.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        """Called whenever a message is sent.
        """

        # Ignore bots.
        if message.author.bot:
            return

        # Ignore messages not sent in lounge.
        if message.channel.id != 604373743837511693:
            return

        # Send the API request.
        await api.post("ladder", f"/messages/{message.author.id}")
