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

bot = commands.Bot("l!", intents=intents, test_guild=942485560142995557)




class CsCommand(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot

  @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
  @bot.slash_command(description="Кейсы в дискорде")
  async def case(self, inter):

    drop_case = random.choice([blue, purple, pink, seriy, golden, red, blue, blue, blue, blue, seriy, seriy, blue, blue, blue, blue, blue, blue, blue])
    if drop_case == blue:
        embed=disnake.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.blue(), timestamp=datetime.datetime.now())   
        embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
        await inter.response.send_message(embed=embed)
      
    elif drop_case == purple:
      embed=disnake.Embed(
              title="Кейс Кс-го",
              description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.purple(), timestamp=datetime.datetime.now())
      embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
      await inter.response.send_message(embed=embed)
    elif drop_case == seriy:
        embed=disnake.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.from_rgb(54, 57, 62), timestamp=datetime.datetime.now())
        embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
        await inter.response.send_message(embed=embed)
    elif drop_case == golden:
        embed=disnake.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.gold(), timestamp=datetime.datetime.now())
        embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
        await inter.response.send_message(embed=embed)
    elif drop_case == red:
        embed=disnake.Embed(
              title="Кейс Кс-го",
              description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.red(), timestamp=datetime.datetime.now())
        embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
        await inter.response.send_message(embed=embed)
    elif drop_case == pink:
        embed=disnake.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}||{random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=disnake.Colour.from_rgb(255, 20, 147), timestamp=datetime.datetime.now())
        embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
        await inter.response.send_message(embed=embed)
    
def setup(bot: commands.Bot):
    bot.add_cog(CsCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")