import discord
from discord.ext import commands
from discord.utils import get
import json
import os
from os import environ

my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix=">", case_insensitive=True)

sus_words = ["mong","sus","hongo", "mogus", "ඞ"]

const arrayOfUsersNames = ['Babato'];



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content.lower()

    if msg.endswith("ano"):
        await message.channel.send("manos en el ano")

    if msg.endswith("lmao"):
        await message.channel.send("lmao")

    if "incineradas lmao" in msg:
        await message.add_reaction("<:KEKW:808869398642819072>")

    if any(word in msg for word in sus_words) and "f4" not in msg:
        await message.add_reaction("🍄")

    if "panita" in msg:
        await message.add_reaction("<:heart-1:549386842089193482>")

    if "league" in msg:
        await message.channel.send("No. Cringe")

    if msg.startswith("$437"):
        for (let i = 0; i < arrayOfUsersNames.length; i++) {
            if (message.author.username.toLowerCase() === arrayOfUsersNames[i].toLowerCase()) return message.reply('No lo intente zopenco');
        };
        botMsg = msg[4:]
        await message.delete();
        await message.channel.send(botMsg)

async def on_reaction_add(reaction, user):
    embed = reaction.embeds[0]
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji == "emoji 1":
        fixed_channel = bot.get_channel(channel_id)
        await fixed_channel.send(embed=embed)

        await message.add_reaction("🍄")

    else:
        return

client.run(my_secret)
