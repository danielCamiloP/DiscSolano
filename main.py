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

    if message.content.endswith("incineradas lmao"):
        await message.add_reaction("<:KEKW:808869398642819072>")

client.run(my_secret)
