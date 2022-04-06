from time import sleep
import disnake
from disnake.ext import commands
import random
from .assets.stringes import *
from .assets.jn import *
from disnake import ApplicationCommandInteraction
import datetime
import aiohttp
from png import *
from disnake import ButtonStyle, ComponentType
from disnake import *

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, test_guilds=[942485560142995557])

class UtilCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Рандомное число | Random number", options=[
        disnake.Option(
            "мин", description="Укажите минимальное число", type=disnake.OptionType.number, required=True,
        ),
        disnake.Option(
            "макс", description="Укажите максимальное число", type=disnake.OptionType.number, required=True
        ),],)
    async def random(self, inter, мин, макс):
        if мин > макс:
            embed=disnake.Embed(description="**Причина:**\n> Меньшее число, больше чем большее число!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            embed=disnake.Embed(title="> 📉 | Рандомное число!", 
            description=f'```\n{random.randint(мин,макс)}\n```', 
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)

    global SEARCH
    SEARCH = ['Youtube', 'Google', 'Yandex', "DuckDuckGo", "Mail"]
  
    @bot.slash_command(description="Поиск в интернете | Search in internet", options=[
        disnake.Option(
              "поисковик", description="Укажите текст!", type=disnake.OptionType.string, choices=SEARCH, required=True),
        disnake.Option(
              "текст", description="Укажите текст!", type=disnake.OptionType.string, required=True),],)
    async def search(self, inter, поисковик, текст: str):
        await inter.response.defer()
        if поисковик == 'Yandex':
          global ja
          ja = текст
          ja = ja.replace(' ', '+')
          embed=disnake.Embed(title="> 🔎 | Поиск в Яндексе", description=f"[Ссылка на ваш запрос](https://yandex.ru/search/?lr=38&text=" + ja + ")", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/853672698081050634/957286352666394715/1200px-Yandex_Browser_logo.svg.png')
          await inter.followup.send(embed=embed)
        elif поисковик == 'Google':
    
          embed=disnake.Embed(title="> 🔎 | Поиск в Гугле", description=f"[Ссылка на ваш запрос](https://www.google.com/search?q=" + ja + ")", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/853672698081050634/957286352427286538/google-logo-png-google-icon-logo-png-transparent-svg-vector-bie-supply-14.png')
          await inter.followup.send(embed=embed)
        elif поисковик == 'Youtube':
    
          embed=disnake.Embed(title="> 🔎 | Поиск в Ютубе", description=f"[Ссылка на ваш запрос](https://www.youtube.com/results?search_query=" + ja + ")", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/853672698081050634/957286352213401710/174883.png')
          await inter.followup.send(embed=embed)
        elif поисковик == 'DuckDuckGo':
    
          embed=disnake.Embed(title="> 🔎 | Поиск в ДакДакГо", description=f"[Ссылка на ваш запрос](https://duckduckgo.com/?q=" + ja + ")", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945707516334059520/958386437634523166/duckduckgo_logo_2019_192.png')
          await inter.followup.send(embed=embed)
        elif поисковик == 'Mail':
    
          embed=disnake.Embed(title="> 🔎 | Поиск в Майле", description=f"[Ссылка на ваш запрос](https://go.mail.ru/search?q=" + ja + ")", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945707516334059520/958386437273817168/Kak-ubrat-Mail.ru-iz-Firefox.png')
          await inter.followup.send(embed=embed)

    @bot.slash_command(description="Рандомный пароль | Random password", options=[
        disnake.Option(
            "seed", description="Укажите сид пароля", type=disnake.OptionType.number, required=True, min_value=1, max_value=1000000
        ),],)
    async def random_pass(self, inter, seed=None):
        rand = random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings)
        rand1 = random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings)
        rand3 = random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings) + random.choice(strings)
        rand2 = rand + random.choice(els)
        random_end2 = rand+rand2+str(random.choice(numbers))+str(random.choice(numbers))
        random_end6 = rand1+rand3+str(random.choice(numbers))+str(random.choice(numbers))
        randomo = int(seed * 3 - 12)+int(random.randint(1,seed) / 2)
        end = random_end6+random_end2+str(randomo)
        embed=disnake.Embed(description=end, color=0x2e2f33)
        embed.set_author(name=f"Ваш пароль:", icon_url=f"{info_png}")
        await inter.response.send_message(embed=embed, ephemeral=True)
  
    @bot.slash_command(description="Аватар пользователя | User avatar", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для команды!", type=disnake.OptionType.user, required=False),],)
    async def avatar(self, inter, пользователь=None):
        await inter.response.defer()
        if пользователь == None:
            embed = disnake.Embed(title=f"{inter.author}'s аватар", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=f'{inter.author.avatar}')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)
        else:
            embed = disnake.Embed(title=f"{пользователь}'s аватар", color=0x2e2f33,
                    timestamp=datetime.datetime.now())
            embed.set_image(url=пользователь.avatar)
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)

    @bot.slash_command(description="> Рандомный собака | Random dog")
    async def random_dog(self, inter):
        await inter.response.defer()
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()

            embed = disnake.Embed(title="Рандомная собака)!",
                                color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=dogjson['link'])
            embed.set_footer(text=f"Выполнил команду: {inter.author}",
                            icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)
    
    @bot.slash_command(description="> Рандомная птичка | Random bird")
    async def random_bird(self, inter):
        await inter.response.defer()
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/bird')
            birdjson = await request.json()

            embed = disnake.Embed(title="Рандомная птичка)!",
                                color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=birdjson['link'])
            embed.set_footer(text=f"Выполнил команду: {inter.author}",
                            icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)

    @bot.slash_command(description="> Рандомный кот | Random cat")
    async def random_cat(self, inter):
        await inter.response.defer()
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()

            embed = disnake.Embed(title="Рандомный кот)!",
                                color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=catjson['link'])
            embed.set_footer(text=f"Выполнил команду: {inter.author}",
                            icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)

    @bot.slash_command(description="> Рандомная лиса | Random fox")
    async def random_fox(self, inter):
        await inter.response.defer()
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            foxjson = await request.json()

            embed = disnake.Embed(title="Рандомная лиса)!",
                                color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=foxjson['link'])
            embed.set_footer(text=f"Выполнил команду: {inter.author}",
                            icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)

    @bot.slash_command(name="ships", description="Покажет вашу любовь | Will show your love", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя", type=disnake.OptionType.user, required=True,
        ),],)
    async def ships(self, inter, пользователь=None):
        if пользователь.bot == True:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать бота!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(
                title=f"> ❤️ | Любовь %",
                description=
                f"{inter.author.mention} и {пользователь.mention} Ваша любовь составляет - `{random.randint(0,100)}%` ",
                color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"Выполнил команду: {inter.author}")
            await inter.response.send_message(embed=embed)

    @bot.slash_command(name="8ball", description="Шар гаданий | Divination ball", options=[
        disnake.Option(
            "вопрос", description="Введите ваш вопрос", type=disnake.OptionType.string, required=True,
        ),],)
    async def ball(self, inter, вопрос=None):
        reply = ["100% да!", "50 на 50", "Наверное", "Конечно... Нет!", "Нет", "Да", "Скорее всего", "Я вас не понимаю", "Зачем?.. Нет"]
        embed=disnake.Embed(title="> 🎱 | Шар гаданий", description=f"\n> 🙎‍♂️ Ваш вопрос: {вопрос}\n\n> ▶️ Мой ответ: {random.choice(reply)}",
        color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
    
    @bot.slash_command(description="Задать вопрос бену | Ask Ben a Question", options=[
        disnake.Option(
            "вопрос", description="Введите ваш вопрос", type=disnake.OptionType.string, required=True,
        ),],)
    async def ben(self, inter, вопрос=None):
        await inter.response.defer()
        reply=random.choice(['Хо-хо-хо', 'Да', 'Нет'])
        if reply == 'Хо-хо-хо':
            embed=disnake.Embed(title='> 🐶 | Бен', description=f"> 🙎‍♂️ Ваш вопрос: {вопрос}\n\n> ▶️ Ответ бена: Хо-хо-хо", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824353537080557569/950643201797140480/Ho-ho.png")
            await inter.followup.send(embed=embed)
        elif reply == 'Да':
            embed=disnake.Embed(title='> 🐶 | Бен', description=f"> 🙎‍♂️ Ваш вопрос: {вопрос}\n\n> ▶️ Ответ бена: Да", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824353537080557569/950643032498241586/Yes.png")
            await inter.followup.send(embed=embed)
        elif reply == 'Нет':
            embed=disnake.Embed(title='> 🐶 | Бен', description=f"> 🙎‍♂️ Ваш вопрос: {вопрос}\n\n> ▶️ Ответ бена: Нет", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824353537080557569/950643030203977748/No.png")
            await inter.followup.send(embed=embed)
        else:
            await inter.followup.send("ошибка")
        
    @bot.user_command(name="Аватар", description="Аватар пользователя | User avatar")
    async def avatar_member(self, inter, member: disnake.Member):
        await inter.response.defer()
        if member == None:
            embed = disnake.Embed(title=f"{inter.author}'s аватар", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_image(url=f'{inter.author.avatar}')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)
        else:
            embed = disnake.Embed(title=f"{member}'s аватар", color=0x2e2f33,
                    timestamp=datetime.datetime.now())
            embed.set_image(url=member.avatar)
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.followup.send(embed=embed)

    @bot.slash_command(description="Отправить рандомный мем | Send random meme")
    async def meme(self, inter):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
          res = await r.json()
          embed=disnake.Embed(title="> 😂 | Мем", color=0x2e2f33, timestamp=datetime.datetime.now())
          embed.set_image(res['data']['children'] [random.randint(0, 25)]['data']['url'])
          embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
          await inter.response.send_message(embed=embed)

    global Calc
    Calc = ['Сложение', 'Вычитание', 'Умножение', 'Деление']
  
    @bot.slash_command(description='Посчитать пример | Calculate example', options=[
        disnake.Option(
            "выбор", description="Выберите что вам сделать!", type=disnake.OptionType.string, required=True, choices=Calc,
        ),
        disnake.Option(
            "первое_число", description="Выберите 1 число!", type=disnake.OptionType.number, required=True,
        ),
        disnake.Option(
            "второе_число", description="Выберите 2 число!", type=disnake.OptionType.number, required=True,
        ),],)
    async def calculator(self, inter, выбор = None, первое_число = int, второе_число = int):
      if выбор == 'Сложение':
        number = первое_число + второе_число
        embed=disnake.Embed(title='Ответ:', description=f'{int(number)}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      elif выбор == 'Вычитание':
        number = первое_число - второе_число
        embed=disnake.Embed(title='Ответ:', description=f'{int(number)}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      elif выбор == 'Умножение':
        number = первое_число * второе_число
        embed=disnake.Embed(title='Ответ:', description=f'{int(number)}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      elif выбор == 'Деление':
        number = первое_число / второе_число
        embed=disnake.Embed(title='Ответ:', description=f'{int(number)}', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
            embed=disnake.Embed(description="**Причина:**\n> Произошла ошибка!", color=0x992D22, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
  
    @bot.slash_command(description='Сыграть в монетку | Play coin', options=[
        disnake.Option(
            "сторона", description="Выберите сторону монетки!", type=disnake.OptionType.string, choices = ["Орёл", "Решка"], required=True,
        ),],)
    async def coinflip(self, inter, сторона = None):
      rand_m = random.choice(["Орёл", "Решка"])
      if сторона == rand_m:
        embed = disnake.Embed(title='> :coin: | Монетка', description='Поздравляю вы выиграли, сегодня удача на вашей стороне!', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"Выпало: {rand_m}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)
      else:
        embed = disnake.Embed(title='> :coin: | Монетка', description='Вы проиграли, вам не повезло!', color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"Выпало: {rand_m}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Забанить не по настоящему | Ban not for real', options=[
        disnake.Option("пользователь", description="Укажите пользователя для бана!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "причина", description="Укажите причину!", type=disnake.OptionType.string, required=True),],)
    async def fake_ban(self, inter, пользователь: disnake.Member, причина: str):
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** {причина}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Сыграть в кости | Play dice')
    async def br(self, inter):
      numb = random.randint(1, 6)
      embed=disnake.Embed(title="> 🦴 | Кость",
      description=f'\n```{numb}```\n',
      color=0x2e2f33, timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")          
      embed.set_image(url='https://cdn.discordapp.com/attachments/952521401145905193/952525907690651699/4bafdc094573bc82840bfcd05bc92cde_w200.gif')
      await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Сыграть в угадывание | Play guess')
    async def guess(self, inter):
      guess = random.choice(['❌', '💰'])
      guess1 = random.choice(['❌', '💰'])
      guess2 = random.choice(['❌', '💰'])
      guess3 = random.choice(['❌', '💰'])
      guess4 = random.choice(['❌', '💰'])
      guess5 = random.choice(['❌', '💰'])
      guess6 = random.choice(['❌', '💰'])
      guess7 = random.choice(['❌', '💰'])
      guess8 = random.choice(['❌', '💰'])
      guess9 = random.choice(['❌', '💰'])
      guess10 = random.choice(['❌', '💰'])
      guess11 = random.choice(['❌', '💰'])
      guess12 = random.choice(['❌', '💰'])
      guess13 = random.choice(['❌', '💰'])
      guess14 = random.choice(['❌', '💰'])
      guess15 = random.choice(['❌', '💰'])
      guises = f"||{guess1}||||{guess}||||{guess2}||||{guess3}||\n||{guess4}||||{guess5}||||{guess6}||||{guess7}||\n||{guess8}||||{guess9}||||{guess10}||||{guess11}||\n||{guess12}||||{guess13}||||{guess14}||||{guess15}||"
      embed=disnake.Embed(title="> 🍁 | Угадай",
      description=guises,
      color=0x2e2f33, timestamp=datetime.datetime.now())
      end = len(guises.split('💰'))
      end_1 = int(end - 1)
      fale = len(guises.split('❌'))
      fale1 = int(fale - 1)
      embed.set_footer(text=f"Правильных: {end_1} | Не правильных: {fale1}", icon_url=f"{inter.author.avatar}")
      await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(UtilCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")