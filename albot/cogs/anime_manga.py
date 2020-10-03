import logging

import discord
from discord.ext import commands

COG_HELP = """TODO"""

class Weeb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)

        self._anime_list = []
        self._manga_list = []

    def add_anime(self, anime):
        self._anime_list.append(anime)

    def add_manga(self, manga):
        self._manga_list.append(manga)
        
    @commands.command(name='weeb')
    async def entry(self, context, *args):

        if len(args) >= 2:
            which = args[0]
            name = " ".join(args[1:])

            if which == "anime":
                self.add_anime(name)
                await context.send(f"Added anime `{name}`")

            elif which == "manga":
                self.add_manga(name)
                await context.send(f"Added manga `{name}`")

            else:
                await context.send(f"Unknown type `{which}`")

        else:
            await context.send(f"Bad number of arguments.")

def setup(bot):
    bot.add_cog(
        Weeb(bot)
    )
