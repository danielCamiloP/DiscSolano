import discord
from discord.ext import commands
from discord.utils import get
import os
from os import environ

my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix=">")



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.endswith("ano"):
        await message.channel.send("manos en el ano")

    if msg.endswith("lmao"):
        await message.channel.send("lmao")

    if message.endswith("incineradas lmao"):
        emoji = get(bot.get_all_emojis(), name=':KEKW:')
        await bot.add_reaction(message, emoji)

client.run(my_secret)
