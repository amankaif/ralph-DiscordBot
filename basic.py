import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
import logging

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

client = discord.Client()

# Event handlers

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    voiceChannels = guild.voice_channels
    print(client.user)
    print(voiceChannels)
    print([vc.name for vc in voiceChannels])


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0] == "_":
        await message.channel.send("call detected")
        text = message.content[1:].strip()
        split = text.split()
        command = split[0]
        print(command)
        if command == "help":
            print("""These are the currently supported commands:
            presence: syntax = _presence """)

    if message.content == '99!':
        response = "Nine Nine!!"
        await message.channel.send(response)


client.run(TOKEN)