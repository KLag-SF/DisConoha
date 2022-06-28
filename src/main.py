#!/usr/bin/env python3
from datetime import date
import os
import shutil
import sys
from time import strftime

import discord

import discordSettings
import conoha_dict

TOKEN = discordSettings.TOKEN
C_DICT = conoha_dict.C_DICT
WORDS = C_DICT.keys()
CHANNELS = []
IMG_DIR = "/opt/disConoha/assets/img/"

client = discord.Client()

@client.event
async def on_message(message):
    msg = message.content

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
    
    if message.channel.id not in CHANNELS:
        with open("../channels.dat", "w") as f:
            f.write(f"{message.channel.id}\n")

def daemonize(client):
    pid = os.fork()

    if pid > 0:
        with open("/var/run/disConoha.pid", "w") as f:
            f.write(str(pid)+"\n")

        sys.exit()

    if pid == 0:
        client.run(TOKEN)

async def notify_update():
    with open("release.txt", "r") as f:
        msg = f.read()
    
    for id in CHANNELS:
        ch = client.get_channel(id)
        ch.send(msg)

    if not os.path.exists("../assets/releases"):
        os.makedirs("../assets/releases")
    
    today = date.today.strftime("%y%m%d")
    fname = f"release_{today}.txt"
    shutil.move("../release.txt", f"../assets/releases/{fname}")
    

def main():
    if os.path.exists("../channels.dat") and os.path.isfile("../channels.dat"):
        with open("../channels.dat", "r") as f:
            CHANNELS = f.readlines()

    if os.path.exists("../release.txt") and os.path.isfile("../release.txt"):
        notify_update()

    if "-t" not in sys.argv:
        while True:
            daemonize(client)
    else:
        client.run(TOKEN)

if __name__ == "__main__":
   main()