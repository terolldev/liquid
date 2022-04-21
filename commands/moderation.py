
import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, MissingPermissions
from disnake import ApplicationCommandInteraction
import datetime
import asyncio
import time

intents = disnake.Intents.default()
intents.members = True
intents.all()

bot = commands.Bot(intents=intents)

class ModCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot  
    #kick member
    @commands.has_permissions(kick_members=True)
    @bot.user_command(name="Кикнуть", description="Кикнуть пользователя | User kick", default_permission="kick_members")
    async def kick_member(self, inter, member: disnake.Member):
        if member == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            await member.kick(reason=f'Mod: {inter.author}/{inter.author.id}')
            embed=disnake.Embed(title="> 🎉 | Кик",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {member.mention}',
              color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)

    #ban user command
    @commands.has_permissions(ban_members = True)
    @bot.user_command(name="Забанить", description="Забанить пользователя | User ban", default_permission="ban_members")
    async def ban_member(self, inter, member: disnake.Member):
        if member == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            await member.ban(reason=f'Mod: {inter.author}/{inter.author.id}')
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {member.mention}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
    #kick
    @commands.has_permissions(kick_members=True)
    @bot.slash_command(description="Кикнуть пользователя | User kick", default_permission="kick_members", options=[
        disnake.Option("пользователь", description="Укажите пользователя для кика!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False),],)
    async def kick(self, inter, пользователь: disnake.Member, причина=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif причина == None:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были кикнуты на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** Без причины', color=0x2e2f33)
            await пользователь.send(embed=embed)
            await пользователь.kick(reason=f'Mod: {inter.author}/{inter.author.id}')
            embed=disnake.Embed(title="> 🎉 | Кик",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** Без причины',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
        else:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были кикнуты на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** {причина}', color=0x2e2f33)
            await пользователь.send(embed=embed)
            await пользователь.kick(reason=f'{причина} (Mod: {inter.author}/{inter.author.id})')
            embed=disnake.Embed(title="> 🎉 | Кик",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Причина:** {причина}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
    #ban
    @commands.has_permissions(ban_members = True)
    @bot.slash_command(description="Бан пользователя | User ban", options=[
        disnake.Option("пользователь", description="Укажите пользователя для бана!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False),],)
    async def ban(self, inter, пользователь: disnake.Member, причина=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif причина == None:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были забанены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** Без причины', color=0x2e2f33)
            await пользователь.ban(reason=f'Mod: {inter.author}/{inter.author.id}')
            await пользователь.send(embed=embed)
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** Без причины',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
        else:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были забанены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** {причина}', color=0x2e2f33)
            await пользователь.ban(reason=f'{причина} (Mod: {inter.author}/{inter.author.id})')
            await пользователь.send(embed=embed)
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** {причина}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
          
    #Слоу мод
    @commands.has_permissions(manage_messages = True)
    @bot.slash_command(description="Поставить слоумод | Install slowmod", default_permission="manage_messages", options=[
        disnake.Option(
            "время", description="Укажите время слоу-мода в текущем канале(0 если отключить)", type=disnake.OptionType.number, required=True, min_value=0, max_value=21600
        ),],)
    async def slowmode(self, inter, время: int):
      if время == 0:
        if время == inter.channel.slowmode_delay:
            embed=disnake.Embed(description="**Причина:**\n> Слоумод уже отключен в этом канале!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
          embed = disnake.Embed(title="> ✅ | Слоумод",
           description=f"**Модератор:** {inter.author.mention}\nОтключил слоу-мод в канале",
            color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.channel.edit(slowmode_delay=время)
          await inter.response.send_message(embed=embed)
      elif время == inter.channel.slowmode_delay:
            embed=disnake.Embed(description="**Причина:**\n> Слоумод уже на этом времени!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
      elif время < 60:
        embed = disnake.Embed(title="> ✅ | Слоумод",
         description=f"**Модератор:** {inter.author.mention}\n**Слоумод:** {int(время / 1)} секунд",
          color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.channel.edit(slowmode_delay=время)
        await inter.response.send_message(embed=embed)
      elif время > 60:
        embed = disnake.Embed(title="> ✅ | Слоумод",
         description=f"**Модератор:** {inter.author.mention}\n**Слоумод:** {int(время//60)} минут {int(время%60)} секунд",
          color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.channel.edit(slowmode_delay=время)
        await inter.response.send_message(embed=embed)
        
    #clear
    @commands.has_permissions(manage_messages = True)
    @bot.slash_command(description="Очистка чата | Chat cleanup", options=[
        disnake.Option(
            "число", description="Укажите количество сообщение которое хотите удалить в текущем канале", type=disnake.OptionType.number, required=True, min_value=1, max_value=100
        ),],)
    async def clear(self, inter, число: int):
      await inter.channel.purge(limit=int(число))
      embed = disnake.Embed(title="> ✅ | Очистка", description=f"**Модератор:** {inter.author.mention}\n**Сообщений:** {int(число)}",
             color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed)
      
    #give role
    @commands.has_permissions(manage_roles=True)
    @bot.slash_command(description="Выдать роль | Give role", options=[
        disnake.Option("пользователь", description="Укажите пользователя которому выдать роль!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "роль", description="Укажите роль!", type=disnake.OptionType.role, required=True),],)
    async def giverole(self, inter, пользователь: disnake.Member, роль: disnake.Role):
      await пользователь.add_roles(роль)
      embed=disnake.Embed(title="> ✅ |  Изменение ролей", description=f"**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Роль:** <@&{роль.id}>", color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed)
    #remove role
    @commands.has_permissions(manage_roles=True)
    @bot.slash_command(description="Забрать роль | Remove role", options=[
        disnake.Option("пользователь", description="Укажите пользователя у которого хотите забрать роль!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "роль", description="Укажите роль!", type=disnake.OptionType.role, required=True),],)
  
    async def removerole(self, inter, пользователь: disnake.Member, роль: disnake.Role):
      await пользователь.remove_roles(роль)
      embed=disnake.Embed(title="> ✅ |  Изменение ролей", description=f"**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Роль:** <@&{роль.id}>", color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      
      await inter.response.send_message(embed=embed)
    #mute
    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="Замьютить пользователя | User mute", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для мьюта!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "минуты", description="Укажите на сколько минут замьютить!", type=disnake.OptionType.number, required=True, min_value=1, max_value=40320),
        disnake.Option(
            "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False
        ),],)
    async def mute(self, inter, пользователь: disnake.Member, минуты: int, причина=None):
      out_1 = пользователь.current_timeout
      if out_1 == None:
        if пользователь.bot == True:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать бота!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
          minuts = минуты * 60
          if минуты < 60:
            if пользователь == inter.author:
                embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            elif причина == None:
                await пользователь.timeout(duration=minuts, reason=f'Mod: {inter.author}')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** Без причины',
                color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** Без причины', color=0x2e2f33)
                await пользователь.send(embed=embed)
            else:
                await пользователь.timeout(duration=minuts, reason=f'{причина} (ID: {inter.author.id})')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Время:**  {int(минуты%60)} минут\n**Причина:** {причина}',
                color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** {причина}', color=0x2e2f33)
                await пользователь.send(embed=embed)
          elif минуты > 60:
            if пользователь == inter.author:
                embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            elif причина == None:
                await пользователь.timeout(duration=minuts, reason=f'Mod: {inter.author}')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** Без причины',
                color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** Без причины', color=0x2e2f33)
                await пользователь.send(embed=embed)
            else:
                await пользователь.timeout(duration=minuts, reason=f'{причина} (ID: {inter.author.id})')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** {причина}',
                color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** {причина}', color=0x2e2f33)
                await пользователь.send(embed=embed)
      else:
            embed=disnake.Embed(description="**Причина:**\n> Пользователь уже замьючен!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        
    #un mute
    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="Размьютить пользователя | User unmute", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для мьюта!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False
        ),],)
    async def unmute(self, inter, пользователь: disnake.Member, причина=None):
        out_1 = пользователь.current_timeout
      
        if out_1 == None:
            embed=disnake.Embed(description="**Причина:**\n> Пользователь не замьючен!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif причина == None:
            await пользователь.timeout(duration=None, reason=f'Mod: {inter.author}')
            embed=disnake.Embed(title="> 🎉 | Размьют",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** Без причины',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
            embed=disnake.Embed(title=f'> 🛠️ | Вы были размьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** Без причины', color=0x2e2f33)
            await пользователь.send(embed=embed)
        else:
            await пользователь.timeout(duration=None, reason=f'{причина} (ID: {inter.author.id})')
            embed=disnake.Embed(title="> 🎉 | Размьют",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Причина:** {причина}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
            embed=disnake.Embed(title=f'> 🛠️ | Вы были размьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** {причина}', color=0x2e2f33)
            await пользователь.send(embed=embed)
    #lock
    @commands.has_permissions(manage_channels=True)
    @bot.slash_command(description="Заблокировать канал | Lock channel", options=[
        disnake.Option(
            "канал", description="Укажите канал который хотите заблокировать!", type=disnake.OptionType.channel, required=True),],)
    async def lock(inter, канал : disnake.TextChannel=None):
      канал = канал or inter.канал
      overwrite = канал.overwrites_for(inter.guild.default_role)
      overwrite.send_messages = False
      await канал.set_permissions(inter.guild.default_role, overwrite=overwrite)
      embed=disnake.Embed(title='> ✅ |  Канал закрыт', description=f'Канал {канал.mention} был заблокирован для сообщений!', color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @bot.slash_command(description="Разблокировать канал | Unlock channel", options=[
        disnake.Option(
            "канал", description="Укажите канал который хотите разблокировать!", type=disnake.OptionType.channel, required=True),],)
    async def unlock(inter, канал: disnake.TextChannel=None):
        канал = канал or inter.канал
        overwrite = канал.overwrites_for(inter.guild.default_role)
        overwrite.send_messages = True
        await канал.set_permissions(inter.guild.default_role, overwrite=overwrite)
        embed=disnake.Embed(title='> ✅ |  Канал открыт', description=f'Канал {канал.mention} был разблокирован для сообщений!', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
    #unlock
    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Отправить сообщение участнику в лс | Send message user in DM", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "текст", description="Укажите текст который отправить!", type=disnake.OptionType.string, required=True),],)
    async def dm(self, inter, пользователь: disnake.Member, текст: str):
      await inter.response.defer()
      embed=disnake.Embed(title='> ✅ |  Успешно', description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Сообщение:** {текст}', color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.followup.send(embed=embed)
      embed=disnake.Embed(description=f'**Модератор:** {inter.author.mention}\n**Сообщение модерации:** {текст}', color=0x2e2f33)
      await пользователь.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description='Создать голосование | Create vote')
    async def vote(self, inter, текст: str):
      embed=disnake.Embed(title='> 📢 | Голосование', description=f'{текст}', color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed)
      message = await inter.original_message()
      await message.add_reaction('👍')
      await message.add_reaction('👎')

def setup(bot: commands.Bot):
    bot.add_cog(ModCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")