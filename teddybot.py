import os
import discord

import random
from dotenv import load_dotenv
load_dotenv()

from teddyActions import excuse_generator, heightball, shifumi

client = discord.Client()

client.countMsgTeddy = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #await channel.send("Pour m'invoquer, un simple `!TeddyBot` en début de message suffit!")

@client.event
async def on_message(message):
  client.countMsgTeddy += 1
  # we do not want the bot to reply to itself
  if message.author.id == client.user.id:
    return

  if message.content.startswith('!TeddyBot'):
    excuse = excuse_generator()
    await message.reply(excuse, mention_author=True)

  elif message.content.startswith('!Teddy8Ball'):
    reponse = heightball(message.content)
    await message.reply(reponse, mention_author=True)

  elif message.content.startswith('!TeddyShifumi'):
    reponse = shifumi(message)
    await message.reply(reponse, mention_author=True)

  elif(client.countMsgTeddy > 15 and random.random() > 0.50):
    client.countMsgTeddy = 0
    replies = [
      'Vous feriez mieux de lire le wiki au lieu de papoter! :face_with_monocle:',
      'Concentrez-vous! :confused:',
      'Je vais dire à JP que vous glandez sur Discord! :scream:'
    ]
    await message.channel.send(random.choice(replies))


client.run(os.environ.get("TOKEN"))
