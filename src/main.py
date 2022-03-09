import asyncio

import discord

import discordSettings
import conoha_dict

TOKEN = discordSettings.TOKEN
C_DICT = conoha_dict.C_DICT
WORDS = C_DICT.keys()
IMG_DIR = "../asset/img/"

client = discord.Client()

@client.event
async def on_message(message):
    msg = message.content
    if msg in WORDS:
        imgPath = IMG_DIR + C_DICT[msg] + ".png"
        await message.channel.send(file=discord.File(imgPath))
    elif msg in C_DICT.values():
        imgPath = IMG_DIR + msg + ".png"
        await message.channel.send(file=discord.File(imgPath))

client.run(TOKEN)