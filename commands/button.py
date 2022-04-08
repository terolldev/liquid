import datetime
from asyncio import sleep
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.emojis = True

bot = commands.Bot("l!", intents=intents, test_guild=942485560142995557)



# Defines a simple view of row buttons.
class RowButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(label="Update", style=ButtonStyle.green)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message(embed=disnake.Embed(title="test"))

class Button(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(name="тест", description="ты как эту команду нашел?")
    async def command_button(self, interaction):
        await interaction.response.send_messaage(embed=disnake.Embed(title="Test!"), view=RowButtons())

def setup(bot: commands.Bot):
    bot.add_cog(Button(bot))
print(f"> Command {__name__} is ready\n----------\n")