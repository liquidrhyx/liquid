# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import json
from logging import warning
import os

import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

bad_words = ["fuck", "sex", "dick", "penis" , "pussy"]

warning = "Watch your language!"

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.command
async def ping(ctx):
      await ctx.reply(pong!)

@client.event
async def on_message(message):
    if message.content.startswith('inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if any(word in message.content for word in bad_words):
        await message.channel.send(warning, delete_after=10)
        await message.delete()
        
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
