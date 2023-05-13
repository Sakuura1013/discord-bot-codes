import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
number = 0

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event()
async def on_ready(ctx):
    await ctx.send('Type "$guess" to start the game.')
    await ctx.send('Type "$attempt" to make a prediction.')


@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')
    global number
    number = random.randint(1, 10)
    print(number)

@bot.command()
async def attempt(ctx, guess=0):  
    global number 
    await ctx.send(f'Your guess is {guess}!')
    if (guess==number):
        await ctx.send("おめでとうございます！")
    else: 
        await ctx.send("Try again!")


bot.run("TOKEN")
