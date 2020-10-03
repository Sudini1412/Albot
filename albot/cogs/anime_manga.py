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

        if args:
            which = args[0]

            if len(args) >= 2:
                name = " ".join(args[1:])

                if which == "anime":
                    self.add_anime(name)
                    await context.send(f"Added anime `{name}`")

                elif which == "manga":
                    self.add_manga(name)
                    await context.send(f"Added manga `{name}`")
                    
                else:
                    await context.send(f"Unknown type `{which}` to add anime/manga to.")

            else:
                if which == "get_anime":
                    await context.send(f"Anime list: `{str(self._anime_list)}`")

                elif which == "get_manga":
                    await context.send(f"Manga list: `{str(self._manga_list)}`")

                else:
                    await context.send(f"Unknown type `{which}`")

        else:
            await context.send(COG_HELP)


def setup(bot):
    bot.add_cog(
        Weeb(bot)
    )
