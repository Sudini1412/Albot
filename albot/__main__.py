import os
import logging

from albot import Albot


if __name__ == '__main__':
    logging.basicConfig(level=20)
    logging.info("Starting albot...")
    bot = Albot()
    bot.load_all_available_cogs()
    bot.run(os.environ['DISCORD_TOKEN'])
