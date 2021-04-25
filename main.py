import discord
import os
import requests
import json
import random
my_secret = os.environ['TOKEN']

client = discord.Client()
wordz = ["hi", "yo", "hello", "wassup", "hi!" , "HI" , "HELLO"]

wordz2 = [
  "yo whats good",
  "apparantly you have a big cock",
  "sometimes life is depressing right?",
  "what up G",
  "fuck u"

]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author ==client.user:
    return

  msg = message.content  

  if any(word in msg for word in wordz):
    myid = message.author.display_name
    await message.channel.send('%s ,yo wus good ' % myid)

  if message.content.startswith('hi azim bot'):
    await message.channel.send(random.choice(wordz2))  

  if message.content.startswith('praise to lord daryl!'):
    for i in range(5):
      await message.channel.send('praise to lord daryl!')

  if message.content.startswith('among us'):
    for i in range(5):
      await message.channel.send('AMOGUS??')

  if message.content.startswith('yes'):
    await message.channel.send('you know it, gayboy')

  if message.content.startswith('no'):
    await message.channel.send('yea i was just kidding')                   

client.run(os.getenv('TOKEN'))
