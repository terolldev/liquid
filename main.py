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
    embed1=disnake.Embed(title=f'> 🏘️ | Бот зашёл на {guild.name} ({guild.id})', description=f'**Участников:** `{guild.member_count}`\n**Бустов:** `{guild.premium_tier}`\n**Дата создания:** {cr_1} ({cr_2})\n**Создатель:** `{guild.owner}` (`{guild.owner.id}`)', color=0x2e2f33)
    embed1.set_author(name='Liquid', icon_url='https://cdn.discordapp.com/attachments/945707516334059520/957878635283497040/liquid2.png')
    await web.send(embed=embed1, username="Server?")
    embed=disnake.Embed(description='**Спасибо за добавление нашего бота**\n> Узнать все команды: `/help`', color=0x2e2f33)
    embed.set_author(name='Liquid', icon_url='https://cdn.discordapp.com/attachments/945707516334059520/957878635283497040/liquid2.png')
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
    embed=disnake.Embed(title=f'> 🏘️ | Бот вышел с {guild.name} ({guild.id})', description=f'**Участников:** `{guild.member_count}`\n**Бустов:** `{guild.premium_tier}`\n**Дата создания:** {cr_1} ({cr_2})\n**Создатель:** `{guild.owner}` (`{guild.owner.id}`)', color=0x2e2f33)
    embed.set_author(name='Liquid', icon_url='https://cdn.discordapp.com/attachments/945707516334059520/957878635283497040/liquid2.png')
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
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"```cs\n# У вас недостаточно прав для этого действия\n```",
        color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error, commands.BotMissingPermissions):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"**`Ошибка!:`** ```cs\n# {error}\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance(error, commands.CommandOnCooldown):
      times = round(error.retry_after, 2)
      if times < 60:
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"Подождите: ```cs\n# {int(times / 1)} секунд\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
      elif times > 60:
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"Подождите: ```cs\n# {int(times/60)} минут {int(times%60)} секунд\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error, commands.EmojiNotFound):
      embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"`404`\n```cs\n#  эмоджи не найдено, укажите правильно\n```", color=0x992D22, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
      await interaction.response.send_message(embed=embed, ephemeral=True)
      await interaction.followup.send(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description="```cs\n# У меня недостаточно прав для совершения этого действия\nВыдайте мне роль со всеми правами!\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
      find = "EmojiNotFound"
      findm = "404 Not Found"
      finds = "400 Bad Request"
      if find in str(error):
        embed=disnake.Embed(title="Упс...", description=f"```cs\n#Эмоджи не найдено...\n#Попробуйте другое эмоджи, или добавьте меня на сервер где это эмоджи\n```", color=0x992D22, timestamp=datetime.datetime.now())
        await interaction.response.send_message(embed=embed, ephemeral=True)
      elif findm in str(error):
        return
      elif finds in str(error):
        return
      else:
        embed=disnake.Embed(title="Упс...", description=f"у меня что-то пошло не так\n```cs\n#   Подробнее: \n{error}\n```", color=0x992D22, timestamp=datetime.datetime.now())
        await interaction.followup.send(embed=embed)
        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.event
async def on_message_command_error(interaction, error):
    if isinstance (error, MissingPermissions):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description=f"```cs\n# У вас недостаточно прав для этого действия\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description="```cs\n# У меня недостаточно прав для совершения этого действия\nВыдайте мне роль со всеми правами!\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed=disnake.Embed(title="Упс...", description=f"у меня что-то пошло не так\n```cs\n#   Подробнее: \n{error}\n```", color=0x992D22, timestamp=datetime.datetime.now())
        await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.event
async def on_user_command_error(interaction, error):
    if isinstance (error, MissingPermissions):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description="```cs\n# У вас недостаточно прав для этого действия\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if isinstance (error.original, Forbidden):
        embed=disnake.Embed(title="> 🔔 | Ошибка!", description="```cs\n# У меня недостаточно прав для совершения этого действия\nВыдайте мне роль со всеми правами!\n```",
        color=0x992D22, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed=disnake.Embed(title="Упс...", description=f"у меня что-то пошло не так\n```cs\n#   Подробнее: \n{error}\n```", color=0x992D22, timestamp=datetime.datetime.now())
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
        embed.add_field(name='> ⌛ | Серверов:',
                        value=f'`{len(bot.guilds)}`')
        embed.add_field(name='> 🧭 | Пользователей:',
                        value=f'**`{len(bot.users)}`**')
        embed.add_field(name='> 📰 | Каналов:',
                        value=f'**`{channels}`**')
        embed.add_field(name='> 🎧 | Ап Тайм:',
                        value=f'`{uptime1}`')
        embed.add_field(name='> 🎉 | Запущен:',
                        value=f'{uptime}')
        embed.add_field(name='> 📲 | Пинг:',
                        value=f'**`{ping}`**')
        embed.add_field(name='> 🧶 | Прочее:',
                        value=f'**Кол-во сообщение:** `{msg}`\n**Модулей в боте:** `{cogs_toal}`')
        embed.set_footer(text = inter.author.name, icon_url = inter.author.avatar)
        await inter.followup.send(embed=embed)
    
class Dropdown(disnake.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Информация", description="Узнать команды в категории инфо", emoji="🔎"
            ),
          
            disnake.SelectOption(
                label="Модерация", description="Узнать команды в категории модерации", emoji="🔧"
            ),
            disnake.SelectOption(
                label="Утилиты", description="Узнать команды в категории утилиты", emoji="🔨"
            ),
            disnake.SelectOption(
                label="Активности", description="Узнать команды активности", emoji="🚀"
            ),
            disnake.SelectOption(
                label="Реакции", description="Узнать команды реакций", emoji="👍"
            ),
            disnake.SelectOption(
                label="Игры", description="Узнать игровые команды", emoji="🎮"
            ),
            disnake.SelectOption(
                label="Удалить сообщение", emoji="🗑️"
            ),]

        super().__init__(
            placeholder="Категории",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
      global opt
      opt = self.values[0]
      if opt == "Утилиты":
            embed=disnake.Embed(title=f"> 🔨 | Утилиты",
            description='`/avatar [пользователь]` — покажет аватарку пользователя\n' +
                 '`/random [меньшее число], [большее число]` — покажет число от меньшего до большого' +
                  '\n`/search [поисковик] [текст]` — Найти в поиске ваш текст' +
                   '\n`/random_dog` — рандомная собака\n`/random_cat` — рандомный кот\n`/random_fox` — рандомная лиса' +
                    '\n`/random_bird` — рандомная птица\n`/ships [пользователь]` — покажет вашу любовь с пользователем'+
                    '\n`/8ball [вопрос]` — Шар гаданий\n`/random_pass [seed]` — Генерирует рандомный пароль\n`/ben [вопрос]` — Задать вопрос бену\n`/calculator [выбор] [первое_число] [второе_число]` — Посчитать пример с помощью бота\n`/coinflip [сторона]` — Подбросить монетку\n`/fake_ban [пользователь] [причина]` — Фейк бан',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
            await interaction.response.edit_message(embed=embed)
      elif opt == "Информация":
          embed=disnake.Embed(title="> 🔎 | Информация",
          description='`/links` — Ссылки бота\n`/stats` — Статистика бота\n' +
            '`/delepovers [создатель]` — Ссылки на разработчиков\n`/about` — Информация о боте\n`/server` — Узнать информацию о сервере\n`/user [пользователь]` — Узнать информацию о участнике\n`/role_info [роль]` — Покажет информация о роли\n`/emoji [кастомное эмоджи]` — Покажет информацию о эмоджи\n`/info_channel [канал]` — Покажет информацию о канале\n`/bug` — Отправить баг\n`/info_voice_channnel [голосовой-канал]` — Покажет информациб о голосовом канале',
          color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
          await interaction.response.edit_message(embed=embed)
      elif opt == "Модерация":
          embed=disnake.Embed(title="> 🔧 | Модерация",
          description='`/clear [сообщений]` — Очистить сообщения\n`/slowmode [время]` — Поставить слоумод в канале\n' +
                 '`/ban [пользователь] [причина]` — Забанить пользователя\n`/kick [пользователь] [причина]` — Кикнуть пользователя\n`/giverole [пользователь] [роль]` — Выдать роль пользователю\n`/removerole [пользователь] [роль]` — Забрать роль у пользователя\n`/mute [пользователь] [время] [причина]` — Замьютить пользователя\n`/unmute [пользователь] [причина]` — Размьютить пользователя\n`/lock [канал]` — Заблокировать канал для отправки сообщений\n`/unlock [канал]` — Разблокировать канал для отправки сообщений\n`/dm [пользователь] [текст]` — Отправить пользователю сообщение в лс\n`/say` — Сказать от имени бота(ваше имя будет видно)\n`/vote` — Создать голосование',
          color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
          await interaction.response.edit_message(embed=embed)
      elif opt == "Активности":
          embed=disnake.Embed(title="> 🚀 | Активности",
          description='`/create_invite [активность]` — Использовать дискорд активность',
          color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
          await interaction.response.edit_message(embed=embed)
      elif opt == "Реакции":
        embed=disnake.Embed(title="> 👍 | Реакции", description="`/hit [пользователь]` — Ударить пользователя\n`/hug [пользователь]` — Обнять пользователя\n`/pat [пользователь]` — погладить пользователя\n`/shot [пользователь]` — выстрельнуть в участника\n`/kiss [пользователь]` — Поцеловать пользователя\n`/sleep` — Уснуть\n`/slap [пользователь]` — Дать пощёчину пользователю\n`/cry` — Плакать\n`/run [пользователь]` — Бежать от пользователя\n`/bite [пользователь]` — Укусить пользователя", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.",       
        icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
        await interaction.response.edit_message(embed=embed)
      elif opt == "Игры":
        embed=disnake.Embed(title="> 🎮 | Игры", description="`/br` — Сыграть в кости\n`/case` — Открыть кейс из кс го\n`/guess` — Попробуй отгадать", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.",  
        icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
        await interaction.response.edit_message(embed=embed)      
      elif opt == "Удалить сообщение":
        await interaction.response.edit_message(view=None)
        await sleep(30)
        message = await interaction.original_message()
        await message.delete()




class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())


@bot.slash_command(description="Справка по командам | Command Help")
async def help(interaction):

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await interaction.response.defer()
    embed=disnake.Embed(title="> 📖 | Команды", description="Чтобы узнать подробнее о командах используйте меню ниже!", color=0x2e2f33, timestamp=datetime.datetime.now())
    embed.add_field(name='🔎 | Информация', value='`/links` `/stats` `/delepovers` `/about` `/server` `/user` `/role_info` `/emoji` `/info_channel` `/bug` `/info_voice_channel`', inline=False)
    embed.add_field(name='🔨 | Утилиты', value='`/avatar` `/random` `/search` `/random_dog` `/random_cat` `/random_fox` `/random_bird` `/ships` `/8ball` `/random_pass` `/ben` `/calculator` `/conflip` `/fake_ban`', inline=False)
    embed.add_field(name='🔧 | Модерация', value='`/clear` `/slowmode` `/ban` `/kick` `/giverole` `/removerole` `/mute` `/unmute` `/lock` `/unlock` `/dm` `/say` `/vote`', inline=False)
    embed.add_field(name='🚀 | Активности', value='`/create_invite`', inline=False)
    embed.add_field(name='👍 | Реакции', value='`/hit` `/hug` `/pat` `/shot` `/kiss` `/sleep` `/slap` `/cry` `/run` `/bite`', inline=False)
    embed.add_field(name='🎮 | Игры', value='`/br` `/case` `/guess`', inline=False)
    embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
    await interaction.followup.send(embed=embed, view=view)


@bot.slash_command(description="Информация о боте | Bot Information")
async def about(self, inter):
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
  embed.add_field(name='> 💮 | Версия Python',
            value=f'**`{platform.python_version()}`**', inline=True)
  embed.add_field(name='> :inbox_tray: | Кол-во команд',
            value=f'**Слеш:** `{total_command}`\n**Message :** `{total_message}`\n**User:** `{total_user}`\n\n**Всего команд:** `{total}`', inline=True)
  embed.add_field(name='> 🧱 | Прочее',
            value=f'**Бот:**\n**Имя:** {bot.user}\n**Создан:** {cr_2} ({cr_1})\n**Тэги:** {bot.user.locale}', inline=True)
  embed.set_thumbnail(url=bot.user.avatar)
  embed.set_footer(text=f"bot id: {bot.user.id}", icon_url=f"{inter.author.avatar}")
  await inter.followup.send(embed=embed)

bot.load_extension("cogs.util")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.info")
bot.load_extension("cogs.activity")
bot.load_extension("cogs.reaction")
bot.load_extension("cogs.case_cs")
bot.load_extension("cogs.textinput")

bot.run(token_id)