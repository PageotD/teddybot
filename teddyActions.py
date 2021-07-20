import os
import discord
import random
import yaml

def excuse_generator():
    accuse = yaml.load(open("accuse.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    commettre = yaml.load(open("commettre.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    faute = yaml.load(open("faute.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    # Join strings to create the reply
    replyTuple = (
        "C'est pas ma faute, c'est",
        random.choice(accuse),
        "qui",
        random.choice(commettre),
        random.choice(faute),
        "."
        )
    return " ".join(replyTuple)

def heightball(content):
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

def shifumi(message):
  shifumimoji = {'pierre': ':rock: ', 'feuille': ':leaves: ', 'ciseaux':':scissors: '}
  try:
    play = message.content.split()
    play_stat = play[1].lower()
    if(play_stat in ['pierre', 'feuille', 'ciseaux']):
      player_return = shifumimoji[play_stat]+play_stat
      shifumi = [':rock: pierre', ':leaves: feuille', ':scissors: ciseaux']
    return player_return+" **vs** "+random.choice(shifumi)
  except:
    return -1
