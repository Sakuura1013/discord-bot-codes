import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event()
async def on_ready(ctx):
    await ctx.send("Type $suggestion to take a suggestion about how can we stop pollution.")

@bot.command()
async def suggestion(ctx):
    informations = ["You can recycle more. Don't forget that lots of used papers can save more trees.",
                    "You can use plastic bags less. You can use eco-friendly bags, they don't give any harm the environment.",
                    "Do not throw your trashes to the streets. It's polluting the environment. It's better if you throw them into recycling bins.",
                    "You can plant trees. It is also a nice and relaxing activity.",
                    "You can turn off your lights when you're not using them. This will help you to make energy save.",
                    "Do not waste water. Turn off your tapes if you don't use them."]
    give_information = random.choice(informations)
    await ctx.send(give_information)

"""@bot.command()
async def suggestion2(ctx):
    await ctx.send("You can use plastic bags less. You can use eco-friendly bags, they don't give any harm the environment.")"""

bot.run("TOKEN")
