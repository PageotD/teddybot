import os
import discord
import re
import random
import yaml
import time
from emoji import UNICODE_EMOJI, demojize

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

def teddygotchi(message, hungrylvl, eattime):
    """
    """
    # Calculate
    t0 = time.time()
    hungrylvl = (t0 - eattime) / 3600. * 100.
    print(eattime, t0, hungrylvl)
    food = [
        ":apple:", ":red_apple:", ":green_apple:", ":pear:", ":tangerine:", ":lemon:", ":banana:", ":watermelon:",
        ":grapes:", ":blueberries:", ":strawberry:", ":melon:", ":cherries:", ":peach:", ":mango:",
        ":pineapple:", ":coconut:", ":beer_mug:"
    ]
    # Check the message content

    msg = message.content.split()
    if len(msg) > 1:
        #for emoji in UNICODE_EMOJI:
        #    print(emoji)
        print(demojize(msg[1]))
        if demojize(msg[1]) in food:
            print(demojize(msg[1]))
            eattime = time.time()
            reply=">>> Teddy aime bien {} !".format(msg[1])
        else:
            reply = ">>> Teddy n'aime pas {} !".format(msg[1])
    else:
        if hungrylvl <= 5.:
            reply = ">>> Teddy n'a pas faim."
        elif hungrylvl > 5. and hungrylvl <= 25:
            reply = ">>> Teddy commence a un peu faim."
        elif hungrylvl > 25. and hungrylvl <= 50:
            reply = ">>> Teddy commence à avoir faim."
        elif hungrylvl > 50. and hungrylvl <= 75:
            reply = ">>> Teddy a faim."
        elif hungrylvl > 75:
            reply = ">>> Teddy a grave la dalle ! Faut le nourrir là !"

    return reply

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
