import discord
from dotenv import load_dotenv
import os

load_dotenv()

'''connection to discord'''
client=discord.Client()

# register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
    
