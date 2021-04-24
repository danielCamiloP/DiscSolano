import discord
from discord.ext import commands

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

client.run(my_secret)
