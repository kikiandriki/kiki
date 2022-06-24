"""Primary application entrypoint.
"""

import os
import logging

from dotenv import load_dotenv

from kiki import Kiki


# Load variables from .env file.
load_dotenv()

# Set the basic logging configuration.
logging.basicConfig(level=logging.INFO)


def app():
    """The application function."""

    # Assert the token variable.
    try:
        token = os.environ["BOT_TOKEN"]
    except KeyError:
        logging.error("You must specify the bot token under BOT_TOKEN.")
        return
    logging.debug("Token is %s", token)

    # Initialize the bot.
    bot = Kiki()

    # Run the bot.
    bot.run(token)
