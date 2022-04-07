import disnake
from disnake.ext import commands
from bottoken import token_id
import random
import time
from datetime import datetime, timezone
import datetime
from png import *
from disnake import Webhook
from disnake.utils import format_dt
import asyncio.tasks
from disnake import TextInputStyle
from asyncio.tasks import sleep
import datetime
import os
from disnake.ext.commands import has_permissions, MissingPermissions, BotMissingPermissions
from disnake.errors import *
import aiohttp


intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot("l!", intents=intents, test_guild=942485560142995557)


@bot.event
async def on_ready():
    print(f"Бот запущен на {bot.user.name}")
    print(f"Disnake.py API версия: {disnake.__version__}")
    print(f"Кол-во команд: {len(bot.slash_commands)}")
    print(f"Май павелитель: DenTop и TimEiger")
    print("-------------------")
    global starttime 
    starttime = time.time()
    async with aiohttp.ClientSession() as session:
      ru_embed = disnake.Embed(title="Рестарт", description="Бот был перезапущен", colour=0xffe100,  timestamp=datetime.datetime.now())
      ru_embed.set_author(name="Liquid", icon_url=bot.user.avatar)

      en_embed = disnake.Embed(title="Restart", description="The bot has been restarted", colour=0xffe100, timestamp=datetime.datetime.now())
      en_embed.set_author(name="Liquid", icon_url=bot.user.avatar)
      ru_b = Webhook.from_url('https://discord.com/api/webhooks/957629271143223307/MEbTyxE2ODlUE5dPbpFYJM6eiv2meIGIegLkIvMy2ftZ-dwi5AJWFUAJFjdz3pAkeK0R', session=session)
      en_b = Webhook.from_url('https://discord.com/api/webhooks/957688258538668149/lGDyma8iICR5h5DwvQojBEm39S9WzovswqJJEDPZeAuwn2IdPuyZzgPQv6ZzNuwvzpRj', session=session)
      await ru_b.send(embed=ru_embed, username='Liquid')
      await en_b.send(embed=en_embed, username='Liquid')
  
    while True:
      await bot.change_presence(
            activity=disnake.Streaming(
                name=f'/help | {len(bot.guilds)} servers', url='https://www.twitch.tv/discord', twitch_name="discord", game="Minecraft"))
      await asyncio.sleep(300)

@bot.event
async def on_guild_join(guild):
  async with aiohttp.ClientSession() as session:
    web = Webhook.from_url('https://discord.com/api/webhooks/957681356505227314/eElGeWW8NEAPDERuxaexKeVtonLvf6Wx3zXRrriNH34UAP6Ch7gADR-QpW9QXB02_LrK', session=session)
    cr_1 = format_dt(guild.created_at, 'D')
    cr_2 = format_dt(guild.created_at, 'R')
    embed1=disnake.Embed(title=f'> 🏘️ | Бот зашёл на {guild.name} ({guild.id})', description=f'**Участников:** `{guild.member_count}`\n**Бустов:** `{guild.premium_tier}`\n**Дата создания:** {cr_1} ({cr_2})\n**Создатель:** `{guild.owner}` (`{guild.owner.id}`)', color=0x2e2f33, timestamp=datetime.datetime.now())
    embed1.set_author(name='Liquid', icon_url=bot.user.avatar)
    await web.send(embed=embed1, username="Server?")
    embed=disnake.Embed(description='**Спасибо за добавление нашего бота**\n> Узнать все команды: `/help`', color=0x2e2f33, timestamp=datetime.datetime.now())
    embed.set_author(name='Liquid', icon_url=bot.user.avatar)
    channel = guild.system_channel
    if channel == None:
      channel_1 = await guild.create_text_channel("Liquid Welcome", reason="Bot joined server | Бот зашел на сервер")  
      await channel_1.send(embed=embed)
    else:
      await channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
  async with aiohttp.ClientSession() as session:
    web = Webhook.from_url('https://discord.com/api/webhooks/957681356505227314/eElGeWW8NEAPDERuxaexKeVtonLvf6Wx3zXRrriNH34UAP6Ch7gADR-QpW9QXB02_LrK', session=session)
    cr_1 = format_dt(guild.created_at, 'D')
    cr_2 = format_dt(guild.created_at, 'R')
    embed=disnake.Embed(title=f'> 🏘️ | Бот вышел с {guild.name} ({guild.id})', description=f'**Участников:** `{guild.member_count}`\n**Бустов:** `{guild.premium_tier}`\n**Дата создания:** {cr_1} ({cr_2})\n**Создатель:** `{guild.owner}` (`{guild.owner.id}`)', color=0x2e2f33, timestamp=datetime.datetime.now())
    embed.set_author(name='Liquid', icon_url=bot.user.avatar)
    await web.send(embed=embed, username="Server?")

@bot.event
async def on_command_error(ctx, error):
  if ctx.author.id == 665271319545511939:  
    await ctx.reply(error)
  elif ctx.author.id == 853671362819391498:
    await ctx.reply(error)
  else:
    return
  
@bot.command()
async def lls(ctx, id):
  if ctx.author.id == 853671362819391498:
    await ctx.guild.leave()
    await ctx.send("Успешно")  
  elif ctx.author.id == 665271319545511939:
    await ctx.send("Успешно") 
    await ctx.guild.leave()
  else:
    return

@bot.event
async def on_slash_command_error(interaction, error):
    if isinstance (error, MissingPermissions):
        embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно прав для этого действия",
        color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error, commands.BotMissingPermissions):
        embed=disnake.Embed(description=f"**Причина:**\n> `{error}",
        color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance(error, commands.CommandOnCooldown):
      times = round(error.retry_after, 2)
      if times < 60:
        embed=disnake.Embed(description=f"**Причина:**\n> Подождите: {int(times / 1)} секунд",
        color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
      elif times > 60:
        embed=disnake.Embed(description=f"**Причина:**\n> Подождите: \n# {int(times/60)} минут {int(times%60)} секунд",
        color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error, commands.EmojiNotFound):
      embed=disnake.Embed(description=f"**Причина:**\n> Эмоджи не найдено, укажите правильно", color=0xed4947, timestamp=datetime.datetime.now())
      embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
      embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
      await interaction.response.send_message(embed=embed, ephemeral=True)
      await interaction.followup.send(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(description="**Причина:**\n> У меня недостаточно прав", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
      find = "EmojiNotFound"
      finds = "Command raised an exception: NameError: name 'starttime' is not defined"
      if find in str(error):
        embed=disnake.Embed(description=f"**Причина:**\n> Попробуйте другое эмоджи, или добавьте меня на сервер где это эмоджи", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        await interaction.response.send_message(embed=embed, ephemeral=True)
      elif finds in str(error):
        embed=disnake.Embed(description="**Причина:**\n> Извините но я не могу найти дату когда я запустился.\n# Повторите попытку позже...", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Подождите...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        await interaction.followup.send(embed=embed)
      else:
        embed=disnake.Embed(description=f"**Причина:**\n> Подробнее:\n{error}", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.event
async def on_message_command_error(interaction, error):
    if isinstance (error, MissingPermissions):
        embed=disnake.Embed(description="**Причина:**\n> У вас недостаточно прав", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(description="**Причина:**\n> У меня недостаточно прав", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed=disnake.Embed(description=f"**Причина:**\n> Подробнее:\n{error}", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.event
async def on_user_command_error(interaction, error):
    if isinstance (error, MissingPermissions):
        embed=disnake.Embed(description="**Причина:**\n> У вас недостаточно прав", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(description="**Причина:**\n> У меня недостаточно прав", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed=disnake.Embed(description=f"**Причина:**\n> Подробнее:\n{error}", color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
@bot.slash_command(description="Статистика бота | Bot statistics")
async def stats(inter):
  await inter.response.defer()
  msg = len(bot.cached_messages)
  channels = len([member for member in bot.get_all_channels()])
  cogs_total = len(bot.cogs)
  cogs_toal = int(cogs_total + 1)
  ping = round(bot.latency * 1000)
  uptime = format_dt(starttime, 'R')
  uptime1 = str(datetime.timedelta(seconds=int(round(time.time()-starttime))))
  embed = disnake.Embed(title=f'> 🚀 | Статистика',
                        color=0x2e2f33, timestamp=datetime.datetime.now())
  embed.add_field(name='> ⌛ | Серверов:', value=f'`{len(bot.guilds)}`')
  embed.add_field(name='> 🧭 | Пользователей:', value=f'**`{len(bot.users)}`**')
  embed.add_field(name='> 📰 | Каналов:', value=f'**`{channels}`**')
  embed.add_field(name='> 🎧 | Ап Тайм:', value=f'`{uptime1}`')
  embed.add_field(name='> 🎉 | Запущен:', value=f'{uptime}')
  embed.add_field(name='> 📲 | Пинг:', value=f'**`{ping}`**')
  embed.add_field(name='> 🧶 | Прочее:', value=f'**Кол-во сообщение:** `{msg}`\n**Модулей в боте:** `{cogs_toal}`')
  embed.set_footer(text = inter.author.name, icon_url = inter.author.avatar)
  await inter.followup.send(embed=embed)


@bot.slash_command(description="Информация о боте | Bot Information")
async def about(self, inter):
  total_size = 0
  start_path = '.' # To get size of current directory for path, dirs, files in os.walk(start_path): 
  for path, dirs, files in os.walk(start_path):
    for f in files: 
      fp = os.path.join(path, f) 
      total_size += os.path.getsize(fp)
  await inter.response.defer()
  total_command1 = len(bot.slash_commands)
  total_command = int(total_command1 - 2)
  total_message = len(bot.message_commands)
  total_user = len(bot.user_commands)
  cr_2 = format_dt(bot.user.created_at, 'D')
  cr_1 = format_dt(bot.user.created_at, 'R')
  total = int(total_command + total_message + total_user )
  embed=disnake.Embed(title="> 🤖 | О боте", colour=disnake.Colour.random(), timestamp=datetime.datetime.now())
  embed.add_field(name='🍨 Разработчики:',
                value=f'\n**`DenTop#6149\nTimEiger#4524`**', inline=True)
  embed.add_field(name='> ✈️ | Язык бота:',
                value=f'**`Disnake.py`**', inline=True)
  embed.add_field(name='> ℹ️ | Префикс бота:',
                value=f'**`/`**', inline=True)
  embed.add_field(name='> ℹ️ | Версия disnake.py',
                value=f'**`{disnake.__version__}`**', inline=True)
  embed.add_field(name='> 💿 | файлы:',
                value=f'**`{int(total_size / 1000000)}`**Кб', inline=True)
  embed.add_field(name='> :inbox_tray: | Кол-во команд',
                value=f'**Слеш:** `{total_command}`\n**Message :** `{total_message}`\n**User:** `{total_user}`\n\n**Всего команд:** `{total}`', inline=True)
  embed.add_field(name='> 🧱 | Прочее',
                value=f'**Бот:**\n**Имя:** {bot.user}\n**Создан:** {cr_2} ({cr_1})\n**Тэги:** {bot.user.locale}', inline=False)
  embed.set_thumbnail(url=bot.user.avatar)
  embed.set_footer(text=f"bot id: {bot.user.id}", icon_url=f"{inter.author.avatar}")
  await inter.followup.send(embed=embed)

#load commands/

bot.load_extension("commands.util")
bot.load_extension("commands.moderation")
bot.load_extension("commands.info")
bot.load_extension("commands.activity")
bot.load_extension("commands.reaction")
bot.load_extension("commands.case_cs")
bot.load_extension("commands.textinput")
bot.load_extension("commands.embed")
bot.load_extension("commands.help")
#bot.load_extension("commands.button")

bot.run(token_id)
