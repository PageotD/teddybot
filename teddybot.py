import os
import discord
import platform

from datetime import datetime
import time
import random
from dotenv import load_dotenv
load_dotenv()

from teddyActions import teddygotchi

from vpbot import VPBot


client = discord.Client()

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
    print(" * python version: {}".format(platform.python_version()))
    print(" * discord.py version: {}".format(discord.__version__))
    print("------------------------------------------------------------")
    print(" * logged in as {0.user}:".format(client))
    for guild in client.guilds:
      print("   * {} ({} members)".format(
          guild.name,
          guild.member_count))
    print("------------------------------------------------------------")
    print(" * Initialize virtual pet ...")
    client.vpbot = VPBot("Teddy")
    print("------------------------------------------------------------")

@client.event
async def on_message(message):

  # we do not want the bot to reply to itself
  if message.author.id == client.user.id:
    return

  # Random excuse generator
  if message.content.lower().startswith('!teddybot'):
    await message.reply(client.vpbot.excuse_generator(), mention_author=True)

  # Magic 8-Ball
  elif message.content.lower().startswith('!teddy8ball'):
    await message.reply(client.vpbot.heightball(message), mention_author=True)

  # Random JCVD sentence generator
  elif message.content.lower().startswith('!teddyvd'):
    await message.channel.send(client.vpbot.jcvd_generator())

  # Random clickbait generator
  elif message.content.lower().startswith('!teddybait'):
    print(message.guild)
    await message.channel.send(client.vpbot.cbait_generator(message))

  # Play Shifumi with the vpbot
  elif message.content.lower().startswith('!teddyshifumi'):
    await message.reply(client.vpbot.play_shifumi(message) , mention_author=True)

  # Virtual pet behavior and stats
  elif message.content.lower().startswith('!teddygotchi'):
    reponse = teddygotchi(message, client.hungrylvl, client.eattime)
    await message.reply(reponse, mention_author=True)

  elif message.content.lower().startswith('!teddystatus'): #message.content == "=displayembed":
      status_description = ":small_blue_diamond: discord.py version: "+str(discord.__version__)+"\n"
      status_description += ":small_blue_diamond: Guild(s):\n"
      print(" * logged in as {0.user}:".format(client))
      for guild in client.guilds:
          status_description += "    - "+str(guild.name)+" :white_check_mark:\n"
      embed = discord.Embed(
          title="Teddy Bot Status",
          description=status_description,
          colour=discord.Colour.blue()
      )

      embed.set_footer(text="Developing Evoli Tamagotchi...")
      #embed.set_image(url="https://cdn.discordapp.com/attachments/520265639680671747/533389224913797122/rtgang.jpeg")
      embed.set_thumbnail(url="https://img1.freepng.fr/20190207/grw/kisspng-eevee-pixel-art-image-eevee-pixel-art-maker-5c5ce3d3859cc0.9955544915495915075473.jpg")
          #url="https://cdn.discordapp.com/app-icons/866664714615128064/1800f16c3114e8a385585c1eb06e13fa.png?size=64")
          #url="https://64.media.tumblr.com/18a645e8cae6526b567b17919ea65d54/tumblr_n49u4s74II1skxu51o1_500.gifv")
      #embed.set_author(name="Teddy Bot v0.3",
      #                 icon_url="https://cdn.discordapp.com/app-icons/866664714615128064/1800f16c3114e8a385585c1eb06e13fa.png?size=64")
      #embed.add_field(name="Field Name", value="Field Value", inline=False)
      #embed.add_field(name="Field Name", value="Field Value", inline=True)
      #embed.add_field(name="Field Name", value="Field Value", inline=True)

      await message.channel.send(embed=embed)

client.run(os.environ.get("TOKEN"))