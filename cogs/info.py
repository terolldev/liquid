import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, MissingPermissions
from disnake.utils import format_dt
from disnake import ApplicationCommandInteraction
import datetime
import os

intents = disnake.Intents.default()
intents.members = True
intents.emojis = True

bot = commands.Bot("l!", intents=intents, test_guild="942485560142995557")


class InfoCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #@bot.slash_command(name="топ", description="Показать топ участников по айди")
    #async def top(self, inter):
      #await inter.response.defer()
      #id = inter.guild.id
      #guild = await bot.fetch_guild(id)
      #members = guild.members
      #await inter.followup.send_message(members)

    global DELEVOPERS
    DELEVOPERS = ["TimEiger", "DenTop"]

    @bot.slash_command(description='Узнать информацию о создателе | Find out information about the creator', options=[
        disnake.Option(
            "разработчик", type=disnake.OptionType.string, choices=DELEVOPERS, required=True
            ),],)
    async def delevopers(self, inter: disnake.CommandInteraction, разработчик=None):
        if разработчик == "TimEiger":
            embed1 = disnake.Embed(title="TimEiger:",
            description="[GitHub1](https://github.com/TimEiger)\n[Twitch](https://www.twitch.tv/tim_eiger)", 
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed1.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed1)
        elif разработчик == "DenTop":
            embed2 = disnake.Embed(title="DenTop", 
            description="[Github](https://github.com/DenTop555)\n[Youtube](https://www.youtube.com/channel/UCvH5UOeMbNvxo-54e1gZ_Gw)", color=0x2e2f33,
            timestamp=datetime.datetime.now())
            embed2.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed2)

    @bot.slash_command(description="Дополнительные ссылки | Additional links")
    async def links(self, inter):
        embed=disnake.Embed(title="🔗 | Ссылки", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> Добавить бота', value='[Тыкни сюда](https://discord.com/api/oauth2/authorize?client_id=942757781444919326&permissions=8&scope=bot%20applications.commands)', inline=True)
        embed.add_field(name='> Поддержка', value='[Тыкни сюда](https://discord.gg/8BJM52ZeNt)', inline=True)
        embed.add_field(name='> Disnake GitHub', value='[Тыкни сюда](https://github.com/DisnakeDev/disnake)', inline=True)
        embed.add_field(name='> Статус бота', value='[Тыкни сюда](https://stats.uptimerobot.com/1qZljs6jYl)', inline=True)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
    
    @bot.slash_command(description="Узнать о сервере | Learn about the server")
    async def server(self, inter):
      ha1 = str(inter.guild.verification_level)
      ha0 = ha1.replace("very_high", "Очень высокая")
      ha2 = ha0.replace("high", "Высокая")
      ha3 = ha2.replace("medium", "Средняя")
      ha4 = ha3.replace("low", "Низкая")
      ha = ha4.replace("none", "null")
      total_member = inter.guild.member_count
      max_member = inter.guild.max_members
      total_channel = len(inter.guild.channels)
      afk_c = inter.guild.afk_channel
      voice_channel = len(inter.guild.voice_channels)
      roles_1 = len(inter.guild.roles)
      roles = int(roles_1 - 1)
      bot = len(list(filter(lambda m: m.bot, inter.guild.members)))
      totals_members = int(total_member - bot)
      bar1 = str(inter.guild.premium_progress_bar_enabled)
      bar2 = bar1.replace("True", "Включенa")
      bar = bar2.replace("False", "Выключенa")
      file = int(inter.guild.filesize_limit / 1000000)
      cr_1 = format_dt(inter.guild.created_at, 'D')
      cr_2 = format_dt(inter.guild.created_at, 'R')

      if afk_c == None:
        
        embed=disnake.Embed(title=f"> 🏜️ | Информация о сервере {inter.guild.name}", description=f"**ID:** {inter.guild.id}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='👥 **| Участники:**', value=f'**Всего:** `{total_member}/{max_member}`\n**Боты:** `{bot}`\n**Участники:** `{totals_members}`\n**Влaделец:** <@!{inter.guild.owner_id}>', inline=True)
        embed.add_field(name='⚓ **| Каналы:**', value=f'**Всего категорий:** `{len(inter.guild.categories)}`\n**Всего Каналов:** `{total_channel}`\n**Текстовые:** `{len(inter.guild.text_channels)}`\n**Голосовые:** `{voice_channel}`\n**Трибун:** `{len(inter.guild.stage_channels)}`\n', inline=True)
        embed.add_field(name='🔖 **| Информация:**', value=f'**Кол-во ролей:** `{roles}`\n**Эмоджи:** `{len(inter.guild.emojis)}`\n**Стикеры:** `{len(inter.guild.stickers)}`', inline=True)
        embed.add_field(name='🚀 **| Бусты:**', value=f'**Кол-во бустов:** `{inter.guild.premium_subscription_count}`\n**Уровень буста:** `{inter.guild.premium_tier}`\n**Шкала прогресса бустов:** `{bar}`', inline=True)
        embed.add_field(name='🔧 **| Прочее:**', value=f'**Проверка сервера:** `{ha}`\n**Макс размер файлов:** `{file}мб`\n**Дата создание сервера:** \n{cr_1} \n({cr_2})', inline=True)
        embed.set_thumbnail(url=inter.guild.icon)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")   
        await inter.response.send_message(embed=embed)
        
      else:    
        embed=disnake.Embed(title=f"> 🏜️ | Информация о сервере {inter.guild.name}", description=f"**ID:** {inter.guild.id}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='👥 **| Участники:**', value=f'**Всего:** `{total_member}/{max_member}`\n**Боты:** `{bot}`\n**Участники:** `{totals_members}`\n**Влaделец:** <@!{inter.guild.owner_id}>', inline=True)
        embed.add_field(name='⚓ **| Каналы:**', value=f'**Всего категорий:** `{len(inter.guild.categories)}`\n**Всего:** `{total_channel}`\n**Текстовые:** `{len(inter.guild.text_channels)}`\n**Голосовые:** `{voice_channel}`\n**Трибун:** `{len(inter.guild.stage_channels)}`\n**Афк канал**: {afk_c.mention}\n', inline=True)
        embed.add_field(name='🔖 **| Информация:**', value=f'**Кол-во ролей:** `{roles}`\n**Эмоджи:** `{len(inter.guild.emojis)}`\n**Стикеры:** `{len(inter.guild.stickers)}`', inline=True)
        embed.add_field(name='🚀 **| Бусты:**', value=f'**Кол-во бустов:** `{inter.guild.premium_subscription_count}`\n**Уровень буста:** `{inter.guild.premium_tier}`\n**Шкала прогресса бустов:** `{bar}`', inline=True)
        embed.add_field(name='🔧 **| Прочее:**', value=f'**Проверка сервера:** `{ha}`\n**Макс размер файлов:** `{file}мб`\n**Дата создание сервера:** \n{cr_1} \n({cr_2})', inline=True)
        embed.set_thumbnail(url=inter.guild.icon)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)

    @bot.user_command(name="Информация о боте")
    async def user_try(self, inter, user: disnake.User):   
      if user.bot == True:
        cr_1 = format_dt(user.created_at, 'R')
        cr_2 = format_dt(user.created_at, 'D')
        jo_1 = format_dt(user.joined_at, 'R')
        jo_2 = format_dt(user.joined_at, 'D')
        falgs = user.public_flags.value
        username = str(user.display_name)
        ver1 = str(user.public_flags.verified_bot)
        ver2 = str(ver1).replace("True", "Да")
        ver = str(ver2).replace("False", "нет")
        guild_d = len(user.mutual_guilds)
        embed = disnake.Embed(title=f"{user} | Информация о боте", description=f"Создан: {cr_1} ({cr_2})\nПрисоединился: {jo_1} ({jo_2})\nФлаги: `{falgs}`\nВерифицирован?: `{ver}`\nОбщих серверов: `{guild_d}`\n\n**Прочее:**\n Упоминание: {user.mention}", colour=user.colour)
        embed.set_thumbnail(url=user.avatar)
        embed.set_footer(text=f"name: {username} | id: {user.id}")
        await inter.response.send_message(embed=embed)
  
      else:
        await inter.response.send_message(embed=disnake.Embed(description="Пользователь не бот", color=0x992D22))

    @bot.slash_command(description='Информация о канале | Channel information')
    async def info_channel(self, inter, канал: disnake.TextChannel):
      cr_1 = format_dt(канал.created_at, 'R')
      cr_2 = format_dt(канал.created_at, 'D')
      slowmod = канал.slowmode_delay
      jump = канал.jump_url
      wswf1 = str(канал.nsfw)
      wswf2 = str(wswf1).replace("True", "Да")
      nswf = str(wswf2).replace("False", "нет")
      if slowmod == 0:

        embed=disnake.Embed(title=f"> 🤖 | Канал: {канал.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> 🍨 | Создан',
                    value=f"{cr_2}\n({cr_1})", inline=True)
        embed.add_field(name='> 🍨 | Находится:',
                    value=f"**В:** `{канал.category}`\n**Позиция:** `{канал.position}`\n**Канал:** [Перейти]({jump})", inline=True)
        embed.add_field(name='> 🍨 | Прочее:',
                    value=f"**NSFW:** `{nswf}`", inline=True)
        embed.set_footer(text=f"ID: {канал.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        embed=disnake.Embed(title=f"> 🤖 | Канал: {канал.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> 🍨 | Создан',
                    value=f"{cr_2}\n({cr_1})", inline=True)
        embed.add_field(name='> 🍨 | Находится:',
                    value=f"**В:** `{канал.category}`\n**Позиция:** `{канал.position}`\n**Канал:** [Перейти]({jump})", inline=True)
        embed.add_field(name='> 🍨 | Прочее:',
                    value=f"**NSFW:** `{nswf}`\n**Слоу-Мод:** `{slowmod}сек`", inline=True)
        embed.set_footer(text=f"ID: {канал.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Информация о голосовом канале | Voice channel information')
    async def info_voice_channel(self, inter, канал: disnake.VoiceChannel):
      cr_1 = format_dt(канал.created_at, 'R')
      cr_2 = format_dt(канал.created_at, 'D')
      jump = канал.jump_url
      users = len(канал.members)
      max = канал.user_limit
      bit = "https://ru.wikipedia.org/wiki/Битрейт"
      bit_rate = int(канал.bitrate / 1000) 
      if max == 0:
        embed=disnake.Embed(title=f"> 🤖 | Канал: {канал.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> 🍨 | Создан',
                    value=f"{cr_2}\n({cr_1})", inline=True)
        embed.add_field(name='> 🍨 | Стат',
                    value=f"[БитРейт]({bit}): {bit_rate}\n\n**Лимит учасников:** `{users}/∞`\n\n**Регион:** {канал.rtc_region}", inline=True)
        embed.add_field(name='> 🍨 | Прочее',
                    value=f"**Упоминание:** {канал.mention}\n\n**Позиция:** {канал.position}", inline=True)
        embed.set_footer(text=f"ID: {канал.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        embed=disnake.Embed(title=f"> 🤖 | Канал: {канал.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> 🍨 | Создан',
                    value=f"{cr_2}\n({cr_1})", inline=True)
        embed.add_field(name='> 🍨 | Стат',
                    value=f"[БитРейт]({bit}): {bit_rate}\n\n**Лимит учасников:** `{users}/{max}`\n\n**Регион:** {канал.rtc_region}", inline=True)
        embed.add_field(name='> 🍨 | Прочее',
                    value=f"**Упоминание:** {канал.mention}\n\n**Позиция:** {канал.position}", inline=True)
        embed.set_footer(text=f"ID: {канал.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      

    @bot.slash_command(description="Информация о роли | Role information")
    async def role_info(self, inter, role: disnake.Role):
        pos = int(role.position)
        cr_1 = format_dt(role.created_at, 'R')
        cr_2 = format_dt(role.created_at, 'D')
        tag = role.tags
        icon = role.icon
        member = len(role.members)
        perms = []
        if icon == None:      
          for perm in role.permissions:
            if perm[1]:
              perms.append(perm[0])
    
              embed=disnake.Embed(title=f"> 🤖 | Роль: {role.name}", color=role.color, timestamp=datetime.datetime.now())
              embed.add_field(name='> 🍨 | Создана',
                  value=f"{cr_2}\n({cr_1})", inline=True)
              embed.add_field(name='> 🏴 | Позиция',
                  value=f"{pos}", inline=True)
              embed.add_field(name='> ⛔ | Права роли',
                  value=f"{', '.join(perms)}\n", inline=True)
              embed.add_field(name='> 🏆 | Прочее',
                  value=f"**Айди:** {role.id}\n**Упоминание роли:** {role.mention}\nЭта роль у `{member}` участников!", inline=True)
              embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          
          await inter.response.send_message(embed=embed)
        else:
          for perm in role.permissions:
            if perm[1]:
              perms.append(perm[0])
              embed=disnake.Embed(title=f"> 🤖 | О роли [{role.name}]", color=role.color, timestamp=datetime.datetime.now())
              embed.add_field(name='> 🍨 | Создана',
                  value=f"{cr_2}\n({cr_1})", inline=True)
              embed.add_field(name='> 🏴 | Позиция',
                  value=f"{pos}", inline=True)
              embed.add_field(name='> ⛔ | Права роли',
                      value=f"{', '.join(perms)}\n", inline=True)
              embed.add_field(name='> 🏆 | Прочее',
                  value=f"**Айди:** {role.id}\n**Упоминание роли:** {role.mention}\n-----------\nЭта роль у `{member}` участников!", inline=True)
    
              embed.set_thumbnail(url=role.icon)
              embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description="Информация о эмоджи | Emoji information", option=[
      disnake.Option(
            "emoji", description="Укажите айди или укажите эмоджи", type=disnake.OptionType.string, required=True,
        ),],)
    async def emoji(self, inter, emoji: disnake.Emoji):
      if emoji.guild == None:
        await inter.response.send_message(embed=disnake.Embed(description="Эмоджи на найдено", color=0x992D22))
      else:
        cr_1 = format_dt(emoji.created_at, 'R')
        embed=disnake.Embed(title=f"> 👑 | О Эмоджи", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='> 🍨 | Создана',
                value=f"{cr_1}\n**Анимированный?:** {emoji.animated}\n**С сервера:** {emoji.guild}({emoji.guild_id})", inline=True)
        embed.set_image(url=emoji.url)
        embed.set_footer(text=f"id: {emoji.id}", icon_url=f"{inter.author.avatar}")
        
        await inter.response.send_message(embed=embed)
  
    @bot.user_command(name="Инфо о участнике")
    async def users(self, inter, пользователь: disnake.Member):
      name = пользователь.name
      avatar = пользователь.avatar
      color = пользователь.colour
      top = пользователь.top_role
      roles1 = len(пользователь.roles)
      roles = int(roles1 - 1)
      nick = пользователь.display_name
      disc = пользователь.discriminator
      created_at = format_dt(пользователь.created_at, 'D')
      joined_at = format_dt(пользователь.joined_at, 'D')
      x = format_dt(пользователь.joined_at, 'R')
      y = format_dt(пользователь.created_at, 'R')
      out_1 = пользователь.current_timeout
      bot1 = str(пользователь.bot)
      bot2 = str(bot1).replace("True", "Да")
      bot = str(bot2).replace("False", "нет")
      
      if out_1 == None:
        embed=disnake.Embed(title=f'> 👤 | Информация о {name}', color=color, timestamp=datetime.datetime.now(), description=f'[{name}#{disc}](https://discord.com/users/{пользователь.id})')
        embed.add_field(name='🧂 | Присоединился:', value=f'{joined_at}({x})', inline=True)
        embed.add_field(name='🍜 | Дата регистрации:', value=f'{created_at}({y})', inline=True)
        embed.add_field(name='🔼 | Высшая роль:', value=f'{top.mention}', inline=True)
        embed.add_field(name='❓ | Серверный никнейм:', value=f'`{nick}`', inline=True)
        embed.add_field(name='📚 | Роли:', value=f'\n**Кол-во ролей:** `{roles}`', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'**Бот:** `{bot}`\n**Упоминание:** {пользователь.mention}', inline=False)
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text=f"ID: {пользователь.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        
        out = format_dt(out_1, 'R')
        embed=disnake.Embed(title=f'> 👤 | Информация о {name}', color=0x2e2f33, timestamp=datetime.datetime.now(), description=f'[{name}#{disc}](https://discord.com/users/{пользователь.id})')
        embed.add_field(name='🧂 | Присоединился:', value=f'{joined_at}({x})', inline=True)
        embed.add_field(name='🍜 | Дата регистрации:', value=f'{created_at}({y})', inline=True)
        embed.add_field(name='🔼 | Высшая роль:', value=f'{top.mention}', inline=True)
        embed.add_field(name='❓ | Серверный никнейм:', value=f'`{nick}`', inline=True)
        embed.add_field(name='📚 | Роли:', value=f'\n**Кол-во ролей:** `{roles}`', inline=True)
        embed.add_field(name='🎟️ | Мут истекает:', value=f'{out}', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'**Бот:** `{bot}`\n**Упоминание:** {пользователь.mention}', inline=False)
        embed.set_thumbnail(url=avatar)
        await inter.response.send_message(embed=embed)
  
  
    @bot.slash_command(description='Информация о пользователе | User information', options=[
        disnake.Option(
            "пользователь", description="Выберите пользователя!", type=disnake.OptionType.user, required=True,
        ),],)
    async def user(self, inter, пользователь):
      name = пользователь.name
      avatar = пользователь.avatar
      color = пользователь.colour
      top = пользователь.top_role.mention
      roles1 = len(пользователь.roles)
      roles = int(roles1 - 1)
      nick = пользователь.display_name
      disc = пользователь.discriminator
      created_at = format_dt(пользователь.created_at, 'D')
      joined_at = format_dt(пользователь.joined_at, 'D')
      x = format_dt(пользователь.joined_at, 'R')
      y = format_dt(пользователь.created_at, 'R')
      out_1 = пользователь.current_timeout
      boting1 = пользователь.bot
      ja = boting1
      
      if out_1 == None:
        embed=disnake.Embed(title=f'> 👤 | Информация о {name}', color=0x2e2f33, timestamp=datetime.datetime.now(), description=f'[{name}#{disc}](https://discord.com/users/{пользователь.id})')
        embed.add_field(name='🧂 | Присоединился:', value=f'{joined_at}({x})', inline=False)
        embed.add_field(name='🍜 | Дата регистрации:', value=f'{created_at}({y})', inline=False)
        embed.add_field(name='🔼 | Высшая роль:', value=f'{top}', inline=False)
        embed.add_field(name='📚 | Роли:', value=f'\n**Кол-во ролей:** `{roles}`', inline=True)
        embed.add_field(name='📚 | Упомянание:', value=f'{пользователь.mention}', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'**Бот:** `{ja}`', inline=True)
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text=f"ID: {пользователь.id}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        out = format_dt(out_1, 'R')
        embed=disnake.Embed(title=f'> 👤 | Информация о {name}', color=0x2e2f33, timestamp=datetime.datetime.now(), description=f'[{name}#{disc}](https://discord.com/users/{пользователь.id})')
        embed.add_field(name='🧂 | Присоединился:', value=f'{joined_at==None}({x==None})', inline=False)
        embed.add_field(name='🍜 | Дата регистрации:', value=f'{created_at}({y})', inline=False)
        embed.add_field(name='🔼 | Высшая роль:', value=f'{top.mention}', inline=False)
        embed.add_field(name='🎟️ | Мут истекает:', value=f'{out}', inline=False)
        embed.add_field(name='📚 | Роли:', value=f'\n**Кол-во ролей:** `{roles}`', inline=True)
        embed.add_field(name='📚 | Упомянание:', value=f'{пользователь.mention}', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'**Бот:** `{ja}`\n', inline=True)
        embed.set_thumbnail(url=avatar)
        await inter.response.send_message(embed=embed)
        
    @bot.message_command(name="Ответь сообщением")
    async def say_message(self, inter, message: disnake.Message):
      cont = message.content
      embed=disnake.Embed(description=cont, color=0x2e2f33)
      embed.set_footer(text=f"Author: {message.author}")
      await inter.response.send_message(embed=embed)

    @bot.message_command(name="Информация о сообщении")
    async def info_message(self, inter, message: disnake.Message):
      y = format_dt(message.created_at, 'R')
      y1 = format_dt(message.created_at, 'D')
      msg = message.edited_at
      react =  "Скоро..." #message.reactions.emoji
      if msg == None:
        cont = message.content
        embed=disnake.Embed(description=f"Содержание: [{cont}]({message.jump_url})", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='📚 | Дата отправки:', value=f'{y}\n({y1})', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'Закреплено: `{message.pinned}`\n Реакции: `{react}`', inline=False)
        embed.set_footer(text=f"{message.author}", icon_url=f"{message.author.avatar}")
        await inter.response.send_message(embed=embed, ephemeral=True)

      else:
        x = format_dt(msg, 'R')
        x1 = format_dt(msg, 'D')
        cont = message.content
        embed=disnake.Embed(description=f"Содержание: [{cont}]({message.jump_url})", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='📚 | Дата отправки:', value=f'{y}\n({y1})', inline=True)
        embed.add_field(name='📚 | Дата последнего редактирование:', value=f'{x}\n({x1})', inline=True)
        embed.add_field(name='📚 | Прочее:', value=f'Закреплено: `{message.pinned}`\n Реакции: `{react}`', inline=False)
        embed.set_footer(text=f"{message.author}", icon_url=f"{message.author.avatar}")
        await inter.response.send_message(embed=embed, ephemeral=True)
        
      
    @bot.message_command(name='Закладка')
    async def book_mark(self, inter, message: disnake.Message):
      cont = message.content
      m = message.jump_url
      embed=disnake.Embed(description=f"Закладка была отправлена в лс!", color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed, ephemeral=True)
      embed2=disnake.Embed(title=f"🔖 | Закладка", description=f'**Канал:** {inter.channel.mention} \n**Сообщение:** [Открыть]({m})\n**Контент:** {cont}', color=0x2e2f33, timestamp=datetime.datetime.now())
      embed2.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.author.send(embed=embed2)

def setup(bot: commands.Bot):
    bot.add_cog(InfoCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")