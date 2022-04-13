
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
              label="Автор",
              placeholder="Укажите текст",
              custom_id="author",
              style=TextInputStyle.short,
              min_length=1,
              max_length=30,
              required=False
            ),
            disnake.ui.TextInput(
              label="Заголовок",
              placeholder="Укажите текст",
              custom_id="title",
              style=TextInputStyle.short,
              min_length=1,
              max_length=50,
              required=False
            ),
            disnake.ui.TextInput(
              label="Описание",
              placeholder="Укажите текст",
              custom_id="des",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=1000,
              required=True,
            ),
              disnake.ui.TextInput(
              label="Футер(подвал)",
              placeholder="Если хотите указать дату -> {timestamp}",
              custom_id="footer",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=30,
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
        input['author'] = input['author'].replace('{author}', f'{inter.author}')
        input['des'] = input['des'].replace('{author.mention}', f'{inter.author.mention}')

        footer = input['footer'].replace("{timestamp}", "")
        if input['title'] == None:
          if "{timestamp}" in input['footer']:
            embed=disnake.Embed(description=f"{input['des']}", colour=disnake.Colour.random(), timestamp=datetime.datetime.now())
            embed.set_author(name=f"{input['author']}")
            embed.set_footer(text=f"{footer}")
          else:
            embed=disnake.Embed(description=f"{input['des']}")
            embed.set_footer(text=f"{footer}")
            embed.set_author(name=f"{input['author']}")
        elif input['author'] == None:
          if "{timestamp}" in input['footer']:
            embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}", colour=disnake.Colour.random(), timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{footer}")
          else:
            embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}", colour=disnake.Colour.random())
            embed.set_footer(text=f"{footer}")
        elif input['footer'] == None:
          embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}", colour=disnake.Colour.random())
          embed.set_author(name=f"{input['author']}")
          await inter.response.send_message("Успешно", ephemeral=True)
          await inter.channel.send(embed=embed)
        elif input['title'] and input['footer'] and input['author'] == None:
            embed=disnake.Embed(description=f"{input['des']}", colour=disnake.Colour.random())
        else:
          if "{timestamp}" in input['footer']:
              embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}", colour=disnake.Colour.random(), timestamp=datetime.datetime.now())
              embed.set_author(name=f"{input['author']}")
              embed.set_footer(text=f"{footer}")
          else:
            embed=disnake.Embed(title=f"{input['title']}", description=f"{input['des']}", colour=disnake.Colour.random())
            embed.set_footer(text=f"{footer}")
            embed.set_author(name=f"{input['author']}")
        await inter.channel.send(embed=embed)
        await inter.response.send_message("Успешно", ephemeral=True)

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