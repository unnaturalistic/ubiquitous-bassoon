import discord, subprocess
import os
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

auth_ids = [592233298646794240]
global started

@client.event
async def on_ready():
    current_dateTime = datetime.now()
    print(f'{current_dateTime} We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    print(message.content)
    cmd = input("cmd input:\n")
    await message.channel.send(f'{cmd}')
    return
client.run(open("token.txt","r").read())
