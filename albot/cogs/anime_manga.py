import logging

import discord
from discord.ext import commands

COG_HELP = """TODO"""

class Weeb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)
        
    @commands.command(name='weeb')
    async def entry(self, context, *args):
      
    def anime(args[0]):
        anime = []
        if args:
            name = args[0]
        else:
            await context.send("Bad args")
        anime.apend(name)
        print anime
        return anime

    def manga(args[0]):
        manga = []
        if args:
            name = args[0]
        else:
            await context.send("Bad args")
        anime.apend(name)
        print manga
        return manga

    if args[0] == "anime":
        anime(args[1])
    if args[0] == "manga":
        manga(args[1])

    await context.send(str(args))

def setup(bot):
    bot.add_cog(
        Weeb(bot)
    )
