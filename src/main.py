#!/usr/bin/env python3
import os
import sys
import logging

import discord

import discordSettings
import conoha_dict

TOKEN = discordSettings.TOKEN
C_DICT = conoha_dict.C_DICT
WORDS = C_DICT.keys()
IMG_DIR = "/opt/disConoha/assets/img/"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

logging.basicConfig(filename="/var/log/disConoha.log", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.debug("disConoha has successfully initialized.")

@client.event
async def on_message(message):
    msg = message.content
    log.debug(msg)
    if msg in WORDS:
        imgPath = IMG_DIR + C_DICT[msg] + ".png"
        await message.channel.send(file=discord.File(imgPath))
    elif msg in C_DICT.values():
        imgPath = IMG_DIR + msg + ".png"
        await message.delete()
        await message.channel.send(file=discord.File(imgPath))
        await message.channel.send(content=f"By {message.author}")
    elif msg == "!words":
        word_list = conoha_dict.get_word_list()
        await message.channel.send(word_list)
    elif msg == "!id" or msg == "!ids":
        id_list = conoha_dict.get_imgID_list()
        await message.channel.send(id_list)

def daemonize(client):
    pid = os.fork()
    if pid > 0:
        with open('/var/run/disConoha.pid', 'w') as f:
            f.write(str(pid)+"\n")
    
        sys.exit()
    if pid == 0:
        log.debug("Client is now running.")
        client.run(TOKEN)

if __name__ == '__main__':
    if '-t' not in sys.argv:
        while True:
            daemonize(client)
    else:
        client.run(TOKEN)
