import logging

import discord
from discord.ext import commands

COG_HELP = """TODO"""

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)
        
    @commands.command(name='anime')
    async def entry(self, context, *args):
        await context.send(str(args))

def setup(bot):
    bot.add_cog(
        Anime(bot)
    )
