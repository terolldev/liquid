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


class Embed1(disnake.ui.Modal):
      def __init__(self):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
              label="Заголовок",
              placeholder="Укажите текст",
              custom_id="title",
              style=TextInputStyle.short,
              min_length=1,
              max_length=305,
              required=False
            ),
            disnake.ui.TextInput(
              label="Описание",
              placeholder="Укажите текст",
              custom_id="des",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=305,
              required=True,
            ),
              disnake.ui.TextInput(
              label="Футер(подвал)",
              placeholder="Укажите текст",
              custom_id="footer",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=305,
              required=False
            ),
        ]
        super().__init__(
            title="Отправить эмбед",
            custom_id="create_tag",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        input = inter.text_values
        if input['title'] == None:
            embed=disnake.Embed(description=f"{input['des']}")
            embed.set_footer(text=f"{input['footer']}")
        elif input['footer'] == None:
            embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}")
        elif input['title'] and input['footer'] == None:
            embed=disnake.Embed(description=f"{input['des']}")
        else:
            embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}")
            embed.set_footer(text=f"{input['footer']}")
        

class Embed(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    @commands.has_permissions(administrator=True)
    @commands.cooldown(rate=1, per=25, type=commands.BucketType.user)
    @bot.slash_command(description="Create embed | Создать эмбед")
    async def embed(inter: disnake.AppCmdInter):
        await inter.response.send_modal(modal=Embed1())
    
def setup(bot: commands.Bot):
    bot.add_cog(Embed(bot))
print(f"> command {__name__} is ready\n----------\n")