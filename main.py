import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
import logging

from keepAlive import keepAlive

# Setting up logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Loading environment variables

load_dotenv("discord.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

description = '''These are the currently available functions and their descriptions :
Basic syntax = _<func> <args(optional)>
'''

# Setting intents

intents = discord.Intents.default()
# intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='_', description=description, intents=intents)

reminderList = []

# List of functions

funcs = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# @bot.command()
# async def roll(ctx, dice: str):
#     """Rolls a dice in NdN format."""
#     try:
#         rolls, limit = map(int, dice.split('d'))
#
#     except:
#         await ctx.send('Format has to be in NdN!')
#         return


@bot.command()
async def dice(ctx):
    """Rolls a dice"""
    await ctx.send(random.randint(1, 6))


@bot.command()
async def toss(ctx):
    """Tosses a coin"""
    result = ["Heads", "Tails"]
    await ctx.send(result[random.randint(0, 1)])

keepAlive()
bot.run(TOKEN)