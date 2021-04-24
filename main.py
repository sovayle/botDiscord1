import discord
import os
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author ==client.user:
    return

  if message.content.startswith('praise to lord daryl!'):
    await message.channel.send('praise to lord daryl!')

  if message.content.startswith('finally...i control AI'):
    await message.channel.send('Ofcourse! Accountants are old news now as well')  

client.run(os.getenv('TOKEN'))
