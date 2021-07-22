import os
import discord

from datetime import datetime
import time
import random
from dotenv import load_dotenv
load_dotenv()

from teddyActions import excuse_generator, heightball, shifumi, teddyvd_generator, teddygotchi

client = discord.Client()

client.countMsgTeddy = 0
client.hungrylvl = 100.
client.eattime = time.time()

@client.event
async def on_ready():
    """
    discord.on_ready()
    Called when the client is done preparing the data received from Discord. Usually
    after login is successful and the Client.guilds and co. are filled up.
    """
    print("------------------------- START UP -------------------------")
    print(" * date: {}".format(datetime.now()))
    print(" * discord.py version: {}".format(discord.__version__))
    print("------------------------------------------------------------")
    print(" * logged in as {0.user}:".format(client))
    for guild in client.guilds:
      print("   * {} ({} members)".format(
          guild.name,
          guild.member_count))
    print("------------------------------------------------------------")

@client.event
async def on_message(message):
  client.countMsgTeddy += 1
  # we do not want the bot to reply to itself
  if message.author.id == client.user.id:
    return

  if message.content.lower().startswith('!teddybot'):
    excuse = excuse_generator()
    print(message.author, message.author.name, message.author.id)
    await message.reply(excuse, mention_author=True)

  elif message.content.lower().startswith('!teddy8ball'):
    answer = heightball(message)
    await message.reply(answer, mention_author=True)

  elif message.content.lower().startswith('!teddyvd'):
    reponse = teddyvd_generator()
    await message.channel.send(reponse)

  elif message.content.lower().startswith('!teddyshifumi'):
    reponse = shifumi(message)
    await message.reply(reponse, mention_author=True)

  elif message.content.lower().startswith('!teddygotchi'):
    reponse = teddygotchi(message, client.hungrylvl, client.eattime)
    await message.reply(reponse, mention_author=True)

  elif(client.countMsgTeddy > 25 and random.random() > 0.95):
    client.countMsgTeddy = 0
    replies = [
      'Vous feriez mieux de lire le wiki au lieu de papoter! :face_with_monocle:',
      'Concentrez-vous! :confused:',
      'Je vais dire à JP que vous glandez sur Discord! :scream:'
    ]
    await message.channel.send(random.choice(replies))


client.run(os.environ.get("TOKEN"))
