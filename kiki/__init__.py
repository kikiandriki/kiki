"""Module entrypoint.
"""

# System imports.
import logging

# External imports.
from discord.ext.commands import Bot
from discord.ext.commands import when_mentioned
from discord.ext.commands import CommandNotFound

from kiki.utils import api


class Kiki(Bot):
    """The Kiki bot."""

    def __init__(self, **kwargs):
        """Initialize the bot."""

        # Continue with the usual initialization.
        super().__init__(command_prefix=when_mentioned, help_command=None, **kwargs)

        # Load all modules.
        self.load_extension("kiki.modules.ladder")

    async def on_ready(self):
        """Discord Bot on ready."""

        # Log a message.
        logging.info("Logged in as %s#%s.", self.user.name,
                     self.user.discriminator)

    async def on_command_error(self, context, exception):
        """Called when a command error is raised."""

        # If the error is that the command was not found, skip.
        if isinstance(exception, CommandNotFound):
            return

        # Otherwise, continue with the usual process.
        return await super().on_command_error(context, exception)
