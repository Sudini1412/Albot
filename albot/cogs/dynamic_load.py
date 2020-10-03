import logging

import discord
from discord.ext import commands


class DynamicLoad(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)

    def _reload_all_cogs(self):
        self.logging.info("Reloading cogs...")

        _reloaded = []
        for cog in self.bot.extensions.keys():
            if cog == __name__:
                # skip
                continue
            try:
                self.bot.reload_extension(cog)
            except Exception:
                 self.logging.error(f"{name} failed to reload: raised exception: {e}")
            else:
                _reloaded.append(cog)
        return _reloaded

    @commands.command(name='dloader')
    async def entry(self, context, *args):
        self.logging.info(f"entry called with {args}")

        if args:
            if args[0] == "all":
                reloaded = self._reload_all_cogs()
                await context.send(f"Reloaded {str(reloaded)}")

        else:
            await context.send("TODO: help")



def setup(bot):
    bot.add_cog(
        DynamicLoad(bot)
    )
