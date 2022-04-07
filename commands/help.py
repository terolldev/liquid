import datetime
from asyncio import sleep
import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.emojis = True

bot = commands.Bot("l!", intents=intents, test_guild=942485560142995557)

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
                    '\n`/8ball [вопрос]` — Шар гаданий\n`/random_pass [seed]` — Генерирует рандомный пароль\n`/meme` — Рандомные мем\n`/ben [вопрос]` — Задать вопрос бену\n`/calculator [выбор] [первое_число] [второе_число]` — Посчитать пример с помощью бота\n`/coinflip [сторона]` — Подбросить монетку\n`/fake_ban [пользователь] [причина]` — Фейк бан',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
            await interaction.response.edit_message(embed=embed)
      elif opt == "Информация":
          embed=disnake.Embed(title="> 🔎 | Информация",
          description='`/links` — Ссылки бота\n`/stats` — Статистика бота\n' +
            '`/about` — Информация о боте\n`/server` — Узнать информацию о сервере\n`/user [пользователь]` — Узнать информацию о участнике\n`/role_info [роль]` — Покажет информация о роли\n`/emoji [кастомное эмоджи]` — Покажет информацию о эмоджи\n`/info_channel [канал]` — Покажет информацию о канале\n`/bug` — Отправить баг\n`/info_voice_channnel [голосовой-канал]` — Покажет информацию о голосовом канале\n `/virable` — Show virable bot',
          color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
          await interaction.response.edit_message(embed=embed)
      elif opt == "Модерация":
          embed=disnake.Embed(title="> 🔧 | Модерация",
          description='`/clear [сообщений]` — Очистить сообщения\n`/slowmode [время]` — Поставить слоумод в канале\n' +
                 '`/ban [пользователь] [причина]` — Забанить пользователя\n`/kick [пользователь] [причина]` — Кикнуть пользователя\n`/giverole [пользователь] [роль]` — Выдать роль пользователю\n`/removerole [пользователь] [роль]` — Забрать роль у пользователя\n`/mute [пользователь] [время] [причина]` — Замьютить пользователя\n`/unmute [пользователь] [причина]` — Размьютить пользователя\n`/lock [канал]` — Заблокировать канал для отправки сообщений\n`/unlock [канал]` — Разблокировать канал для отправки сообщений\n`/dm [пользователь] [текст]` — Отправить пользователю сообщение в лс\n`/say` — Сказать от имени бота(ваше имя будет видно)\n`/vote` — Создать голосование\n`/embed` — Отправить эмбед',
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

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Справка по командам | Command Help")
    async def help(interaction):

        # Create the view containing our dropdown
        view = DropdownView()

        # Sending a message containing our view
        await interaction.response.defer()
        embed=disnake.Embed(title="> 📖 | Команды", description="Чтобы узнать подробнее о командах используйте меню ниже!", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name='🔎 | Информация', value='`/links` `/stats` `/about` `/server` `/user` `/role_info` `/emoji` `/info_channel` `/bug` `/info_voice_channel` `/virable`', inline=False)
        embed.add_field(name='🔨 | Утилиты', value='`/avatar` `/random` `/search` `/random_dog` `/random_cat` `/random_fox` `/random_bird` `/ships` `/8ball` `/random_pass` `/meme` `/ben` `/calculator` `/conflip` `/fake_ban`', inline=False)
        embed.add_field(name='🔧 | Модерация', value='`/clear` `/slowmode` `/ban` `/kick` `/giverole` `/removerole` `/mute` `/unmute` `/lock` `/unlock` `/dm` `/say` `/vote` `/embed`', inline=False)
        embed.add_field(name='🚀 | Активности', value='`/create_invite`', inline=False)
        embed.add_field(name='👍 | Реакции', value='`/hit` `/hug` `/pat` `/shot` `/kiss` `/sleep` `/slap` `/cry` `/run` `/bite`', inline=False)
        embed.add_field(name='🎮 | Игры', value='`/br` `/case` `/guess`', inline=False)
        embed.set_footer(text=f"© Liquid 2021-2022. Все права защищены.", icon_url="https://cdn.discordapp.com/attachments/824353537080557569/952513431267868722/Frame_21.png")
        await interaction.followup.send(embed=embed, view=view)

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
print(f"> Command {__name__} is ready\n----------\n")