import discord
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

'''connection to discord'''
client=discord.Client()

def get_quote(): # return a quote from api
    response = requests.get("https://zenquotes.io/api/random")
    # convert response to json
    json_data = json.loads(response.text)
    # q stands for quote; a stands for author
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

# register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    '''if message.content.startswith('$hello'):
        await message.channel.send('Hello!')'''
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
    
