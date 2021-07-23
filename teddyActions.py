import os
import discord
import re
import random
import yaml
import time
from emoji import UNICODE_EMOJI, demojize


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
        ":pineapple:", ":coconut:", ":beer_mug:", ":pizza:", ":pretzel:"
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
            reptype = random.random()
            if(reptype < 0.2):
                reply = ">>> Teddy n'aime pas {} !".format(msg[1])
            elif reptype >= 0.2:
                zone=[
                    "dans la tête !",
                    "dans les genoux !",
                    "dans les dents !"
                ]
                reply = ">>> Teddy te renvoie {} {} !".format(msg[1], random.choice(zone))
    else:
        if hungrylvl <= 5.:
            reply = ">>> Teddy n'a pas faim."
        elif hungrylvl > 5. and hungrylvl <= 25:
            reply = ">>> Teddy a un peu faim."
        elif hungrylvl > 25. and hungrylvl <= 50:
            reply = ">>> Teddy commence à avoir faim."
        elif hungrylvl > 50. and hungrylvl <= 75:
            reply = ">>> Teddy a faim."
        elif hungrylvl > 75:
            reply = ">>> Teddy a grave la dalle ! Faut le nourrir là !"

    return reply
