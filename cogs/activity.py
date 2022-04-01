import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, MissingPermissions
from disnake import ApplicationCommandInteraction
import datetime
import asyncio

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

class ActivityCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    ALL_ACTIVITIES = [act.name for act in disnake.PartyType]



    @commands.slash_command(options=[
        disnake.Option(
            "активность", description="Укажите кастомную активность", type=disnake.OptionType.string, required=True, choices=ALL_ACTIVITIES
        ),],)
    async def create_invite(self, inter: disnake.ApplicationCommandInteraction,
                            активность: commands.option_enum(ALL_ACTIVITIES)):
        """
        Выбрать кастомную активность | Select custom activity
        """

        if not inter.user.voice:
            embed=disnake.Embed(description="**Причина:**\n> Вы не в голосовом канале!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        voice_channel = inter.user.voice.channel
        link = await voice_channel.create_invite(reason='Activity created',
                                                 target_type=disnake.InviteTarget.embedded_application,
                                                 target_application=getattr(disnake.PartyType, активность))
        embed = disnake.Embed(title="> 🚀 | Активность", description=f"[Открыть активность]({link})", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(ActivityCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")