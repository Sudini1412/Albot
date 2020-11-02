import logging

import discord
from discord.ext import commands

COG_HELP = """Usage:
download message_format
"""

CHECK = "\U0001F48B"
AUTHOR = "dustpancake"
HISTORY_LIMIT = 300


class Downloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)

    async def _get_attachments(self, context, username):
        async for m in context.history(limit=HISTORY_LIMIT).filter(
            lambda m: m.author.name == username
        ):

            # skip if no attachments
            if not m.attachments:
                continue

            done = False
            for reac in m.reactions:
                if reac.me and reac.emoji == CHECK:
                    self.logging.info(f"Already obtained {m}")
                    done = True

            # skip if already downloaded
            if done:
                continue

            for i in m.attachments:
                yield i
                await (m.add_reaction(CHECK))

    @commands.command(name="download")
    async def entry(self, context, *args):

        if context.author.name != AUTHOR:
            await context.send("This function is not available to you.")

        if args:
            username = args[0]

            async for i in self._get_attachments(context, username):
                self.logging.info(f"Downloading {i.filename}...")

                await context.send(f"Downloading {i.filename}...")
                await i.save("mc2/"+i.filename)

                # mark as done
                await context.send(
                    f"{CHECK} Done {i.size}/{i.size} bytes.".format(i.filename)
                )
        else:
            await context.send(COG_HELP)


def setup(bot):
    #bot.add_cog(
    #    Downloader(bot)
    #)
    pass
