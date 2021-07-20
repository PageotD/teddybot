import os
import discord

import random

client = discord.Client()

client.countMsgTeddy = 0

def teddy8ball(content):
  """
  8ball Teddy
  """
  BallChoice =[
    "Essaye plus tard", "Essaye autre chose", "Pas d\'avis","C\'est ton destin", "Le sort en est jeté","Une chance sur deux", "D \'après moi oui","C'est certain", "Oui absolument", "Tu peux compter dessus","Sans aucun doute", "Très probable", "Oui", "C\'est bien parti", "C\'est non", "Peu probable", "Faut pas rêver", "N'y compte pas", "Impossible"
  ]

  seed = 0
  for i in range(len(content)):
    seed += ord(content[i])
  
  random.seed(a=seed)
  return ":8ball: "+random.choice(BallChoice)+" !"

def excuse_generator():

    accuse = ['JP', 'toi', 'un ornithorynque', '@Pierre-Yves','un chien', 'un chat', 'une théorie sur pythagore', 'une version de Windows', 'un iguane',
'un navigateur pas vraiment à jour', 'un avatar', 'un voisin', 'un complot autour de  Matrix',
'un artefact', 'un double maléfique', 'un poisson rouge', 'un historique dans Google']

    commettre = ['a écrasé', 'a remplacé', 'a effacé', 'a altéré', 'a détruit', 'a modifié irrémédiablement', 'a inversé', 'a recyclé', 'a tweeté sur ', 'a recalculé',
'a reparamétré', 'a remis à jour', 'a abandonné', 'a plagié', 'a isolé', 'a volé',
'a trié aléatoirement', 'a renversé de l\'eau sur', 'a perdu', 'a mal interprété',
'a incinéré', 'a fait du tri sélectif sur', 'a caché', 'a reparamétré', 'a mis de côté', 'a fait le mort',
'a mis sur eBay', 'n\'avait pas ajouté en favori sur Facebook', 'n\'a pas aimé sur SnapChat',
'n\'a pas aimé sur Youtube', 'a bu pendant que vous bossiez sur', 'n\'a pas liké',
'a acheté sur Amazon', 'a mal lu']

    faute = ['le wiki', 'le projet', 'le navigateur', 'le travail', 'la session', 'le fichier Excel', 'le document Word',
'le papier', 'le contrat', 'la tentative de connexion', 'le blog', 'l\'article', 'la carte mémoire',
'l\'aide en ligne', 'le rêve d\'un monde meilleur', 'le memento', 'le compte-rendu',
'le fichier dans le Cloud', 'le portfolio', 'le commentaire']

    return "C'est pas ma faute, c'est "+random.choice(accuse)+" qui "+random.choice(commettre)+" "+random.choice(faute)+"."

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
    reponse = teddy8ball(message.content)
    await message.reply(reponse, mention_author=True)

  elif(client.countMsgTeddy > 15 and random.random() > 0.50):
    client.countMsgTeddy = 0
    replies = [
      'Vous feriez mieux de lire le wiki au lieu de papoter! :face_with_monocle:',
      'Concentrez-vous! :confused:',
      'Je vais dire à JP que vous glandez sur Discord! :scream:'
    ]
    await message.channel.send(random.choice(replies))


client.run(os.environ['TOKEN'])
