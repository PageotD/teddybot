import os
import discord

import random

client = discord.Client()

client.countMsgTeddy = 0

from teddyActions import shifumi, heightball, excuse_generator


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #await channel.send("Pour m'invoquer, un simple `!TeddyBot` en début de message suffit!")
 
@client.event
async def on_message(message):
  client.countMsgTeddy += 1
  print(message.content.split())
  # we do not want the bot to reply to itself
  if message.author.id == client.user.id:
    return

  if message.content.startswith('!TeddyBot'):
    excuse = excuse_generator()
    await message.reply(excuse, mention_author=True)

  elif "!TeddyBot" in message.content.split():
    excuse = excuse_generator()
    await message.reply(excuse, mention_author=True)

  elif message.content.startswith('!Teddy8Ball'):
    reponse = heightball(message.content)
    await message.reply(reponse, mention_author=True)

  elif message.content.startswith('!TeddyShifumi'):
    reponse = shifumi(message)
    if reponse == -1:
      await message.reply("J'ai pas compris!", mention_author=True)
    else:
      await message.reply(reponse, mention_author=True)

  elif(client.countMsgTeddy > 15 and random.random() > 0.50):
    client.countMsgTeddy = 0
    replies = [
      'Vous feriez mieux de lire le wiki au lieu de papoter! :face_with_monocle:',
      'Concentrez-vous! :confused:',
      'Je vais dire à JP que vous glandez sur Discord! :scream:'
    ]
    await message.channel.send(random.choice(replies))


#client.run(os.environ['TOKEN'])
client.run("ODY2NjY0NzE0NjE1MTI4MDY0.YPV2aQ.Olg-F5XWoimguOqw1-NPX79f1Xs")