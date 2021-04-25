import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]

if "responding" not in db.keys():
  db["responding"] = True

words = ["-hi", "-yo", "-hello", "-wassup", "-hi!" , "-HI" , "-HELLO"]

bot_responses = [
  "maybe the real bots were the friends we made along the way",
  "apparantly you have a big cock",
  "sometimes life is depressing right?",
  "what up G",
  "fuck u"
]

bot_friendly_responses = [
  "is the weather cloudy today?",
  "yo are you good",
  "it could have been better right",
  "would u prefer me over her?"
]

dababy_responses = ["dababy", "Dababy", "dabenby", "DaBaby", "Dabenby", "DaBenby", "DABENBY", "dababi", "DABABY", "DABABY", "Lets go"]

letsgo_responses = ["lets go", "let's go!", "LETS GO", "Let's proceed...i mean lets go", "les go",
  "Let's go!", "Let's Go!", "lesgo", "Lets Go", "Lets go"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]  

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

bothi = ['hi azim bot' , 'hi rakyat bot']
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))   

@client.event
async def on_message(message):
  userid = message.author.name
  if message.author ==client.user:
    return
  elif userid == 'harrod12345' and message.content.startswith('-p'):
    return 
  elif userid == 'harrod12345' and message.content.startswith('-'):
    await message.channel.send('sorry Ben u are benned...i mean banned')
    return  

  msg = message.content  

  if any(word in msg for word in words):
    myid = message.author.display_name
    await message.channel.send('%s , ' % myid + random.choice(bot_friendly_responses))
  
  elif any(word in msg for word in bothi):
    await message.channel.send(random.choice(bot_responses))

  elif any(word in msg for word in dababy_responses):
    await message.channel.send(random.choice(letsgo_responses))   

  elif message.content.startswith('-inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options.append(db["encouragements"])

    elif any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  elif msg.startswith("-new"):
    encouraging_message = msg.split("-new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")  

  elif msg.startswith("-del"):
    encouragements =[]
    if "encouragements" in db.keys():
      index = int(msg.split("-del",1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)   

  elif msg.startswith("-list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  elif msg.startswith("-responding"):
    value = msg.split("-responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  elif message.content.startswith('praise to lord daryl!'):
    for i in range(5):
      await message.channel.send('praise to lord daryl!')

  elif message.content.startswith('among us'):
    for i in range(5):
      await message.channel.send('AMOGUS??')

  elif message.content.startswith('-yes'):
    await message.channel.send('you know it.')

  elif message.content.startswith('-no'):
    await message.channel.send('yea i was just kidding')     

  elif message.content.startswith('fuck u'):
    await message.channel.send('no u')

  elif message.content.startswith('best valorant'):
    await message.channel.send('aqil')

  elif message.content.startswith('ben'):
    await message.channel.send('ben gei')    

  else:
    return      
                     
keep_alive()
client.run(os.getenv('TOKEN'))  
