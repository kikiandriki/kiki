"""Ladder module.
Top level of the ladder module.
"""

from .cogs import Ladder


def setup(bot):
    """Set up module.
    """

    bot.add_cog(Ladder(bot))
