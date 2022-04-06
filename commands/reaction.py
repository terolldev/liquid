import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, MissingPermissions
from disnake import ApplicationCommandInteraction
import datetime
import random
import os

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

class ReactCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Поцеловать учатника", options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=True),],)
    async def kiss(self, inter, пользователь=None):
      if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
      else:
        kiss = random.choice([
               'https://i.imgur.com/II1bakc.gif',
               'https://i.imgur.com/MzAjNdv.gif',
               'https://i.imgur.com/eKcWCgS.gif',
               'https://i.imgur.com/3aX4Qq2.gif',
               'https://i.imgur.com/uobBW9K.gif',
               'https://i.imgur.com/uobBW9K.gif',
               'https://i.imgur.com/FozOXkB.gif',
               'https://i.imgur.com/7GhTplD.gif'
               ])
        embed=disnake.Embed(title='Реакция: поцеловать', description=f'{inter.author.mention} поцеловал(-а) {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_image(url=kiss)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      
    @bot.slash_command(description='Ударить пользователя | Hit user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def hit(self, inter, пользователь=None):
      if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
      elif пользователь == None:
        hit = random.choice([
            'https://i.imgur.com/Y4VKTdu.gif',
            'https://i.imgur.com/KnppKOB.gif',
            'https://i.imgur.com/UY6LR1C.gif',
            'https://i.imgur.com/wfM5y7Q.gif',
            'https://i.imgur.com/iCq5Xb2.gif',
            'https://i.imgur.com/MJQdQAx.gif',
            'https://i.imgur.com/ZEVPNfM.gif',
            'https://i.imgur.com/xiK3Low.gif',
            'https://i.imgur.com/0x4Wd6q.gif'
          ])
        embed=disnake.Embed(title='Реакция: ударить', description=f'{inter.author.mention} ударил(-а) всех!', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_image(url=hit)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        hit1 = random.choice([
            'https://i.imgur.com/Y4VKTdu.gif',
            'https://i.imgur.com/KnppKOB.gif',
            'https://i.imgur.com/UY6LR1C.gif',
            'https://i.imgur.com/wfM5y7Q.gif',
            'https://i.imgur.com/iCq5Xb2.gif',
            'https://i.imgur.com/MJQdQAx.gif',
            'https://i.imgur.com/ZEVPNfM.gif',
            'https://i.imgur.com/xiK3Low.gif',
            'https://i.imgur.com/0x4Wd6q.gif'
          ])
        embed=disnake.Embed(title='Реакция: ударить', description=f'{inter.author.mention} ударил(-а) {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_image(url=hit1)
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Погладить пользователя | Pat user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def pat(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          pat = random.choice([
            'https://i.imgur.com/2lacG7l.gif',
            'https://i.imgur.com/UWbKpx8.gif',
            'https://i.imgur.com/4ssddEQ.gif',
            'https://i.imgur.com/2k0MFIr.gif',
            'https://i.imgur.com/LUypjw3.gif',
            'https://i.imgur.com/F3cjr3n.gif',
            'https://i.imgur.com/NNOz81F.gif'
          ])
          embed=disnake.Embed(title='Реакция: погладить', description=f'{inter.author.mention} погладил(-а) всех!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=pat)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          pat1 = random.choice([
            'https://i.imgur.com/2lacG7l.gif',
            'https://i.imgur.com/UWbKpx8.gif',
            'https://i.imgur.com/4ssddEQ.gif',
            'https://i.imgur.com/2k0MFIr.gif',
            'https://i.imgur.com/LUypjw3.gif',
            'https://i.imgur.com/F3cjr3n.gif',
            'https://i.imgur.com/NNOz81F.gif'
          ])
          embed=disnake.Embed(title='Реакция: погладить', description=f'{inter.author.mention} погладил(-а) {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=pat1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)



    @bot.slash_command(description='Обнять пользователя | Hug user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def hug(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          hug = random.choice([
            'https://i.imgur.com/r9aU2xv.gif',
            'https://i.imgur.com/wOmoeF8.gif',
            'https://i.imgur.com/nrdYNtL.gif',
            'https://i.imgur.com/BPLqSJC.gif',
            'https://i.imgur.com/ntqYLGl.gif',
            'https://i.imgur.com/v47M1S4.gif',
            'https://i.imgur.com/82xVqUg.gif',
            'https://i.imgur.com/6qYOUQF.gif',
            'https://i.imgur.com/UMm95sV.gif'
          ])
          embed=disnake.Embed(title='Реакция: обнять', description=f'{inter.author.mention} обнял(-а) всех!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=hug)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          hug1 = random.choice([
            'https://i.imgur.com/r9aU2xv.gif',
            'https://i.imgur.com/wOmoeF8.gif',
            'https://i.imgur.com/nrdYNtL.gif',
            'https://i.imgur.com/BPLqSJC.gif',
            'https://i.imgur.com/ntqYLGl.gif',
            'https://i.imgur.com/v47M1S4.gif',
            'https://i.imgur.com/82xVqUg.gif',
            'https://i.imgur.com/6qYOUQF.gif',
            'https://i.imgur.com/UMm95sV.gif'
          ])
          embed=disnake.Embed(title='Реакция: обнять', description=f'{inter.author.mention} обнял(-а) {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=hug1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Выстрелить пользователя | Shot user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def shot(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          shot = random.choice([
            'https://i.imgur.com/u2Wpnjw.gif',
            'https://i.imgur.com/6DkYg9N.gif',
            'https://i.imgur.com/DbnBVjJ.gif',
            'https://i.imgur.com/9bWT18J.gif',
            'https://i.imgur.com/rIs4E6Y.gif'
          ])
          embed=disnake.Embed(title='Реакция: выстрелить', description=f'{inter.author.mention} расстрелял всех!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=shot)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          shot1 = random.choice([
            'https://i.imgur.com/u2Wpnjw.gif',
            'https://i.imgur.com/6DkYg9N.gif',
            'https://i.imgur.com/DbnBVjJ.gif',
            'https://i.imgur.com/9bWT18J.gif',
            'https://i.imgur.com/rIs4E6Y.gif'
          ])
          embed=disnake.Embed(title='Реакция: выстрелить', description=f'{inter.author.mention} выстрелил(-а) в {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=shot1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Уснуть | Sleep')
    async def sleep(self, inter):
          sleep = random.choice([
            'https://i.imgur.com/GBlaGYc.gif',
            'https://i.imgur.com/PKys6GG.gif',
            'https://i.imgur.com/e5VyGdA.gif',
            'https://i.imgur.com/Gfw2LTE.gif',
            'https://i.imgur.com/XytOEEm.gif',
            'https://i.imgur.com/E4diLx6.gif',
            'https://i.imgur.com/Fm7XWfl.gif',
            'https://i.imgur.com/UJCXsmy.gif',
            'https://i.imgur.com/yiNPyc7.gif'
          ])
          embed=disnake.Embed(title='Реакция: уснуть', description=f'{inter.author.mention} уснул(-а)', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=sleep)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Дать пощёчину пользователя | Slap user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def slap(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          slap = random.choice([
            'https://i.imgur.com/HYJHoG7.gif',
            'https://i.imgur.com/9GxTsgl.gif',
            'https://i.imgur.com/uwHDm3r.gif',
            'https://i.imgur.com/mT4VjD6.gif',
            'https://i.imgur.com/w66ZqGR.gif',
            'https://i.imgur.com/oSoudVd.gif',
            'https://i.imgur.com/1FyrbwB.gif',
            'https://i.imgur.com/mtJt6kL.gif',
            'https://i.imgur.com/T9w8eFV.gif'
          ])
          embed=disnake.Embed(title='Реакция: пощёчина', description=f'{inter.author.mention} дал(-а) пощёчину всем!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=slap)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          slap1 = random.choice([
            'https://i.imgur.com/HYJHoG7.gif',
            'https://i.imgur.com/9GxTsgl.gif',
            'https://i.imgur.com/uwHDm3r.gif',
            'https://i.imgur.com/mT4VjD6.gif',
            'https://i.imgur.com/w66ZqGR.gif',
            'https://i.imgur.com/oSoudVd.gif',
            'https://i.imgur.com/1FyrbwB.gif',
            'https://i.imgur.com/mtJt6kL.gif',
            'https://i.imgur.com/T9w8eFV.gif'
          ])
          embed=disnake.Embed(title='Реакция: пощёчина', description=f'{inter.author.mention} дал(-а) пощёчину {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=slap1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Заплакать | Cry')
    async def cry(self, inter):
          cry = random.choice([
            'https://i.imgur.com/1kgcgPG.gif',
            'https://i.imgur.com/OgZjIr1.gif',
            'https://i.imgur.com/44E0eHi.gif',
            'https://i.imgur.com/MF2wKCT.gif',
            'https://i.imgur.com/uwZRY5t.gif'
          ])
          embed=disnake.Embed(title='Реакция: заплакать', description=f'{inter.author.mention} заплкал(-а)', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=cry)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Бежать от пользователя | Run from the user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def run(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          run = random.choice([
            'https://i.imgur.com/JMVc5eV.gif',
            'https://i.imgur.com/FvWMFlD.gif',
            'https://i.imgur.com/ZF54zRf.gif',
            'https://i.imgur.com/FMNN1vP.gif',
            'https://i.imgur.com/f2G4KhW.gif',
            'https://i.imgur.com/LAzrCjl.gif',
            'https://i.imgur.com/P35ne0U.gif',
            'https://i.imgur.com/d5KZGGW.gif',
            'https://i.imgur.com/wIdkQWm.gif'
          ])
          embed=disnake.Embed(title='Реакция: бежать', description=f'{inter.author.mention} бежит!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=run)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          run1 = random.choice([
            'https://i.imgur.com/JMVc5eV.gif',
            'https://i.imgur.com/FvWMFlD.gif',
            'https://i.imgur.com/ZF54zRf.gif',
            'https://i.imgur.com/FMNN1vP.gif',
            'https://i.imgur.com/f2G4KhW.gif',
            'https://i.imgur.com/LAzrCjl.gif',
            'https://i.imgur.com/P35ne0U.gif',
            'https://i.imgur.com/d5KZGGW.gif',
            'https://i.imgur.com/wIdkQWm.gif'
          ])
          embed=disnake.Embed(title='Реакция: бежать', description=f'{inter.author.mention} бежит от {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=run1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Укусить пользователя | Bite user', options=[
          disnake.Option(
                "пользователь", description="Укажите пользователя!", type=disnake.OptionType.user, required=False),],)
    async def bite(self, inter, пользователь=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif пользователь == None:
          bite = random.choice([
            'https://i.imgur.com/VFjoWe4.gif',
            'https://i.imgur.com/oZXIbQ9.gif',
            'https://i.imgur.com/qQzKwP9.gif',
            'https://i.imgur.com/WxYtS74.gif',
            'https://i.imgur.com/S6Je2yz.gif',
            'https://i.imgur.com/RxcxL2z.gif',
            'https://i.imgur.com/ffQ87DP.gif',
            'https://i.imgur.com/ykQA3hF.gif',
            'https://i.imgur.com/8hGUk4o.gif'
          ])
          embed=disnake.Embed(title='Реакция: укусить', description=f'{inter.author.mention} укусил(-а) всех!', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=bite)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)
        else:
          bite1 = random.choice([
            'https://i.imgur.com/VFjoWe4.gif',
            'https://i.imgur.com/oZXIbQ9.gif',
            'https://i.imgur.com/qQzKwP9.gif',
            'https://i.imgur.com/WxYtS74.gif',
            'https://i.imgur.com/S6Je2yz.gif',
            'https://i.imgur.com/RxcxL2z.gif',
            'https://i.imgur.com/ffQ87DP.gif',
            'https://i.imgur.com/ykQA3hF.gif',
            'https://i.imgur.com/8hGUk4o.gif'
          ])
          embed=disnake.Embed(title='Реакция: укусить', description=f'{inter.author.mention} укусил(-а) {пользователь.mention}', color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(url=bite1)
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(ReactCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")