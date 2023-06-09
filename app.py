import discord, subprocess
import os
import asyncio
from datetime import datetime

# -- Bot state --
bot_guild_id = 1116794638011990058
bot_channel_id = 1116794639719076014
        
# -- Initialize bot --
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# -- Utility functions --
async def read_input():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, input)

# -- Event handlers --
@client.event
async def on_ready():
    current_dateTime = datetime.now()
    print(f'{current_dateTime} We have logged in as {client.user}.')
    while True:
        user_input = await read_input()
        if(user_input):
            dest_channel = client.get_channel(bot_channel_id)
            await dest_channel.send(user_input)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'[{datetime.now()}]<@{message.author}>: {message.content}')
    return
    
# -- Start the bot --
client.run(open("token.txt","r").read())
