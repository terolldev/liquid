from time import sleep
import disnake
from disnake.ext import commands
import random
from disnake import ApplicationCommandInteraction
import datetime
import aiohttp
from disnake import TextInputStyle
from disnake import Webhook


bot = commands.Bot(test_guilds=[942485560142995557])


class MyModal(disnake.ui.Modal):
      def __init__(self):
        # The details of the modal, and its components
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Укажите текст",
              custom_id="name",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=305
            ),
        ]
        super().__init__(
            title="Отправить эмбед",
            custom_id="create_tag",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        input = inter.text_values
        embed = disnake.Embed(description=input["name"], colour=disnake.Colour.from_rgb(54, 57, 62))
        embed.set_author(name=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        embed2=disnake.Embed(description='Сообщение было отправлено!', color=0x2e2f33)
        await inter.response.send_message(embed=embed2, ephemeral=True)
        await inter.channel.send(embed=embed)

class MyModal2(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Суть Багa",
              placeholder="Укажите текст",
              custom_id="syt",
              style=TextInputStyle.short,
              min_length=1,
              max_length=300
            ),
          disnake.ui.TextInput(
              label="Баг",
              placeholder="Укажите текст",
              custom_id="name1",
              style=TextInputStyle.paragraph,
              min_length=20,
              max_length=300
            ),
          disnake.ui.TextInput(
              label="Доп.Ссылки",
              placeholder="Укажите ссылки скринов, видео, фрапсы, и т.п..",
              custom_id="url",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=400,
              required=False
            ),
        ]
        super().__init__(
            title="Отправить баг",
            custom_id="create_tag",
            components=components,
            timeout=300
        )
      async def callback(self, inter: disnake.ModalInteraction):
        async with aiohttp.ClientSession() as session:
            input1 = inter.text_values
            url_1 = input1["url"]=None
            if url_1 == None:
              embed = disnake.Embed(title=input1["syt"], description=input1["name1"], colour=disnake.Colour.from_rgb(54, 57, 62))
              embed.set_author(name=f"{inter.author}", icon_url=f"{inter.author.avatar}")
              embed.set_footer(text=f"ID: {inter.author.id}", icon_url=f"https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
              embed2=disnake.Embed(title='> ✅ | Баг', description='Данный баг был отправлен разработчикам!', color=0x2e2f33)
              await inter.response.send_message(embed=embed2, ephemeral=True)
              webhook = Webhook.from_url('https://discord.com/api/webhooks/954348466488885328/S88VTsYvnpeERns_boZNhjhxYNk5J3i_Z0YicC3evKbzAMfBo-KhK0rC9Zem2S8bDMm0', session=session)
              await webhook.send(embed=embed, username='Bugs?')
            else:
              embed = disnake.Embed(title=input1["syt"], description=input1["name1"], colour=disnake.Colour.from_rgb(54, 57, 62))
              embed.set_author(name=f"{inter.author}", icon_url=f"{inter.author.avatar}")
              embed.set_footer(text=f"ID: {inter.author.id}", icon_url=f"https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
              embed.add_field(name='Доп ссылки:',
                  value=url_1, inline=True)
              embed2=disnake.Embed(title='> ✅ | Баг', description='Данный баг был отправлен разработчикам!', color=0x2e2f33)
              await inter.response.send_message(embed=embed2, ephemeral=True)
              webhook = Webhook.from_url('https://discord.com/api/webhooks/954348466488885328/S88VTsYvnpeERns_boZNhjhxYNk5J3i_Z0YicC3evKbzAMfBo-KhK0rC9Zem2S8bDMm0', session=session)
              await webhook.send(embed=embed, username='Bugs?')


class TextCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=25, type=commands.BucketType.user)
    @bot.slash_command(description="Сказать от имени бота | Speak as a bot")
    async def say(inter: disnake.AppCmdInter):
        await inter.response.send_modal(modal=MyModal())
      
    @commands.cooldown(rate=1, per=600, type=commands.BucketType.user)
    @bot.slash_command(description="Сообщить о баге | Report a bug")
    async def bug(inter: disnake.AppCmdInter):
      await inter.response.send_modal(modal=MyModal2())
    
def setup(bot: commands.Bot):
    bot.add_cog(TextCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")