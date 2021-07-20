import os
import discord

import random
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

client.countMsgTeddy = 0

from teddyActions import shifumi, heightball, excuse_generator


@client.event
async def on_ready():
    print('-------------------- START-UP --------------------')
    print('* We have logged in as {0.user}'.format(client))
    print('--------------------------------------------------')
 
@client.event
async def on_message(message):
  client.countMsgTeddy += 1
  print(message.content.split())
  # we do not want the bot to reply to itself
  if message.author.id == client.user.id:
    return

  if "!TeddyBot" in message.content.split():
    excuse = excuse_generator()
    await message.reply(excuse, mention_author=True)

  elif message.content.startswith('!Teddy8Ball'):
    reponse = heightball(message.content)
    await message.reply(reponse, mention_author=True)

  elif message.content.startswith('!TeddyShifumi'):
    reponse = shifumi(message)
    if reponse == -1:
      retour = [
        "J\'ai pas compris!",
        "T\'as le choix entre 3 mots, c'est quoi le problème ?",
        "Tu sais pas écrire sérieux ?"
        ]
      await message.reply(random.choice(retour), mention_author=True)
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


client.run(os.environget("TOKEN"))
