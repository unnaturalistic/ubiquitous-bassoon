import discord, subprocess
import os
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

channel = client.get_channel(1087016569995006048) # replace with channel_id

@client.event
async def on_ready():
    current_dateTime = datetime.now()
    print(f'{current_dateTime} We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await print('author: ' + client.fetch_user)
    await print('message: ' + message.content)
    message = input()
    await channel.send(message)
client.run(open("token.txt","r").read())

