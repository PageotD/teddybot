import os
import discord
import random
import yaml

def teddyvd_generator():
    teddyvd1 = yaml.load(open("teddyvd1.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    teddyvd2 = yaml.load(open("teddyvd2.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    teddyvd3 = yaml.load(open("teddyvd3.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    teddyvd4 = yaml.load(open("teddyvd4.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
    # Join strings to create the reply
    replyTuple = (">>>",
        random.choice(teddyvd1),
        random.choice(teddyvd2),
        "car",
        random.choice(teddyvd3),
        random.choice(teddyvd4),
        "\n_-Teddy Van Damme_."
    )
    return " ".join(replyTuple)

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

def heightball(message):
    """
    Magic 8-ball is supposed to predict the future and answer any question asked.

    :param message: class discord.Message
    :return: string
    """

    # Magic 8-Ball avalaible answers
    answers = [
        "Essaye plus tard", "Essaye autre chose", "Pas d'avis", "C'est ton destin", "Le sort en est jeté",
        "Une chance sur deux", "D'après moi oui", "C'est certain", "Oui absolument", "Tu peux compter dessus",
        "Sans aucun doute", "Très probable", "Oui", "C'est bien parti", "C'est non", "Peu probable", "Faut pas rêver",
        "N'y compte pas", "Impossible"
    ]

    # Check the message content
    msg = message.content.split()
    if len(msg) > 1:
        # Message has a content (other than command !Teddy8Ball
        # Randomly selects an answer and returns the reply.
        return ":8ball: "+random.choice(answers)+"!"
    else:
        # Message does not have any content (other than command !Teddy8Ball
        return "Tu dois poser une question!"

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
