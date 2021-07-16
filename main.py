import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
import logging
from mutagen.mp3 import MP3
import time

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
FFMPEG_PATH = os.getenv('FFMPEG_PATH')

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
    """Rolls a die (yes misleading I know)"""
    await ctx.send(random.randint(1, 6))


@bot.command()
async def toss(ctx):
    """Tosses a coin"""
    result = ["Heads", "Tails"]
    await ctx.send(result[random.randint(0, 1)])


@bot.command()
async def join(ctx):
    """Just joins a vc and does nothing else, just for comedic effect"""
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if not voice_client:
        pass
    else:
        await ctx.send("Already connected to a voice channel")
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command()
async def lessgo(ctx):
    
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_client = voice_channel
    # print(voice_channel.is_connected())

    # voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    # if not voice_client:
    if voice_channel is None:
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            voice_channel = ctx.message.author.voice.channel
            await voice_channel.connect()
    # else:
    else:
        print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        voice_channel = voice_client.channel
        # await voice_channel.connect()
        
    # print(voice_client.channel.voice)


    # channel = ctx.author.voice.channel
    # await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    print(voice_channel)
    # print("\n\n\n", server, "\n\n\n")
    print("\n\n\n", voice_channel, "\n\n\n")
    # channel = ctx.author.voice.channel
    # await voice_channel.connect()
    songLen = MP3("resources/lessgo.mp3").info.length
    voice_channel.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source="resources/lessgo.mp3"))
    # await ctx.voice_client.disconnect()
    print("\n\n\n\ndaboogie\n\n\n\n")
    time.sleep(round(songLen)+1)
    await voice_channel.disconnect()
    


@bot.command()
async def leave(ctx):
    """Leaves joined vc"""
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


print(MP3("resources/lessgo.mp3").info.length)
keepAlive()
bot.run(TOKEN)