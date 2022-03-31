import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, MissingPermissions
from disnake.utils import format_dt
from disnake import ApplicationCommandInteraction
import datetime
import random
import os
from asyncio import sleep

import platform
from .assets.drop import blue, purple, red, pink, seriy, stattrack, golden, gama, gloves, pat, blue1

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot("l!", intents=intents, test_guild="942485560142995557")




class TestCommand(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot


  @commands.slash_command()
  async def command(self, inter):
    print("This code is ran every time any subcommand is invoked")


  @command.sub_command()
  async def a(self, inter, option: int):
    await inter.response.send_message(f"You ran /command foo a {option}")



def setup(bot: commands.Bot):
    bot.add_cog(TestCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")