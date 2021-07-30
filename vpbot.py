# Import modules
import random
import yaml
from io import *
from itertools import combinations
from collections import defaultdict
from time import time
from markdownify import markdownify as md
from collections import Counter
import feedparser

class VPBot:
    """
    Virtual Pet Bot Class.
    Designed to control the behavior of the bot
    """
    # Fixed parameters
    # * happiness threshold and drop
    hapiness_threshold = 50.
    happiness_drop = 20.
    # * fullness threshold and drop
    fullness_threshold = 50.
    fullness_drop = 25
    wordsolutions = []
    wordtrial = []
    
    def __init__(self, name="Teddy"):
        # Virtual pet name
        self.vpname = name
        # Set happiness and fullness
        self.happiness = 100.
        self.fullness = 100.

    def rssfeed(self):

        # Création d'une instance
        news_feed = feedparser.parse('http://feeds.dzone.com/publications')

        # Propriétés du flux
        #print(news_feed.feed.keys())

        # Titre du flux
        #print("Feed Title:", news_feed.feed.title) 

        # Sous-titre du flux
        #print("Feed Subtitle:", news_feed.feed.subtitle)

        # Lien du flux
        #print("Feed Link:", news_feed.feed.link, "\n")

        # Propriétés de chaque item du flux
        #print(news_feed.entries[0].keys())

        #for entry in news_feed.entries:
        #    print(f"{entry.title} --> {entry.link}")
    
        # Récupération du deernier feed (dernier bulletin CERT-FR)
        reply = "\n"
        for i in range(0, 3):#:5): #len(news_feed.entries)):
            #if i == (len(news_feed.entries)-1):
            if i < len(news_feed.entries)-1:
                print("Alert: {} \nLink: {}".format(news_feed.entries[i]['title'], news_feed.entries[i]['id']))
                reply += "**[{}]({})**\n".format(news_feed.entries[i]['title'],news_feed.entries[i]['id'])
                #reply += "[Link]({})".format(news_feed.entries[0]['id'])
                reply += "_{}_\n".format(news_feed.entries[i].published)
                reply += "{}\n".format(" ".join(md(news_feed.entries[i]['summary']).split()))
                #reply += "[Link]({})".format(news_feed.entries[0]['id'])
                reply += "\n"
                print(reply)
        return reply

    def _mood(self):
        """
        Estimate the mood of the virtual pet given happiness and fullness level
        """
        if(self.fullness >= self.fullness_threshold and self.happiness >= self.happiness_threshold):
            status = "Happy!"
        elif(self.fullness < self.fullness_threshold and self.happiness >= self.happiness_threshold):
            status = "Hungry!"
        elif (self.fullness >= self.fullness_threshold and self.happiness < self.happiness_threshold):
            status = "Bored!"
        else:
            status = "Hungry and bored!"
        return status

    def _modify_happiness(self, inc=0.):
        self.happiness = max(0, min(self.happiness + inc, 100.))

    def _modify_fullness(self, inc=0.):
        self.fullness = max(0, min(self.fullness + inc, 100.))

    # Activities
    def feed(self, message):
        """
        Feed the virtual pet with some emoji, for example:
        !teddybot :pretzel:
        """
        # Open favourite_food.yaml
        with open("resources/favourite_food.yaml", 'r', encoding="utf-8") as fyaml:
            favourite = yaml.load(fyaml, Loader=yaml.FullLoader)

        # Check for emoji in message
        # * Split the message content
        msg = message.content.split()
        if len(msg) > 1:
            if demojize(msg[1]) in food:
                # Create the reply
                reply = ">>> Teddy aime bien {} !".format(msg[1])
                # Increase fullness
                self._modify_fullness(inc=20.)
            else:
                # Create the reply
                reply = ">>> Teddy n'aime pas {} !".format(msg[1])

            return reply

    def teach(self):
        """
        You can teach something to the virtual pet by give him a valide wikipedia link
        """
        #urllib.request.urlopen(url)
        pass

    def play(self):
        pass

    def play_shifumi(self, message):
        shifumimoji = {'pierre': ':rock: ', 'feuille': ':leaves: ', 'ciseaux': ':scissors: '}
        try:
            play = message.content.split()
            play_stat = play[1].lower()
            if (play_stat in ['pierre', 'feuille', 'ciseaux']):
                player_return = shifumimoji[play_stat] + play_stat
                shifumi = [':rock: pierre', ':leaves: feuille', ':scissors: ciseaux']
                # Update happiness
                self._modify_happiness(inc=10.)
            return player_return + " **vs** " + random.choice(shifumi)
        except:
            return ">>> pierre :rock:, feuille :leaves:, ciseaux :scissors:."

    # Actions
    def excuse_generator(self):

        with open("resources/excusegen01.yaml", 'r', encoding="utf-8") as fyaml:
            part01 = yaml.load(fyaml, Loader=yaml.FullLoader)

        with open("resources/excusegen02.yaml", 'r', encoding="utf-8") as fyaml:
            part02 = yaml.load(fyaml, Loader=yaml.FullLoader)

        with open("resources/excusegen03.yaml", 'r', encoding="utf-8") as fyaml:
            part03 = yaml.load(fyaml, Loader=yaml.FullLoader)

        # Join strings to create the reply
        replyTuple = (
            "C'est pas ma faute, c'est",
            random.choice(part01),
            "qui",
            random.choice(part02),
            random.choice(part03),
            "."
        )
        return " ".join(replyTuple)

    def jcvd_generator(self):
        """
        Randomly generate JCVD sentences.
        """

        with open("resources/jcvdgen01.yaml", 'r', encoding="utf-8") as fyaml:
            part01 = yaml.load(fyaml, Loader=yaml.FullLoader)

        with open("resources/jcvdgen02.yaml", 'r', encoding="utf-8") as fyaml:
            part02 = yaml.load(fyaml, Loader=yaml.FullLoader)

        with open("resources/jcvdgen03.yaml", 'r', encoding="utf-8") as fyaml:
            part03 = yaml.load(fyaml, Loader=yaml.FullLoader)

        with open("resources/jcvdgen04.yaml", 'r', encoding="utf-8") as fyaml:
            part04 = yaml.load(fyaml, Loader=yaml.FullLoader)

        # Join strings to create the reply
        replyTuple = (
            ">>>",
            random.choice(part01),
            random.choice(part02),
            "car",
            random.choice(part03),
            random.choice(part04),
            "\n_-Teddy Van Damme_."
            )

        return " ".join(replyTuple)

    def heightball(self, message):
        """
        Magic 8-ball is supposed to predict the future and answer any question asked.

        :param message: class discord.Message
        :return: string
        """

        # Magic 8-Ball avalaible answers
        answers = [
            "Essaye plus tard", "Essaye autre chose", "Pas d'avis", "C'est ton destin", "Le sort en est jeté",
            "Une chance sur deux", "D'après moi oui", "C'est certain", "Oui absolument", "Tu peux compter dessus",
            "Sans aucun doute", "Très probable", "Oui", "C'est bien parti", "C'est non", "Peu probable",
            "Faut pas rêver",
            "N'y compte pas", "Impossible"
        ]

        # Check the message content
        msg = message.content.split()
        if len(msg) > 1:
            # Message has a content (other than command !Teddy8Ball
            # Randomly selects an answer and returns the reply.
            return ":8ball: " + random.choice(answers) + "!"
        else:
            # Message does not have any content (other than command !Teddy8Ball
            return "Tu dois poser une question!"

    def cbait_generator(self, message):
        cperson = yaml.load(open("resources/cbait_person.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
        cobject = yaml.load(open("resources/cbait_object.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
        caction = yaml.load(open("resources/cbait_action.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)
        cfinal = yaml.load(open("resources/cbait_final.yaml", 'r', encoding="utf-8"), Loader=yaml.FullLoader)

        if (random.random() > 0.6):
            # Template 1
            person1 = random.choice(cperson)
            person2 = random.choice(cperson)
            while(person1 == person2):
                person1 = random.choice(cperson)
                person2 = random.choice(cperson)
            if person1 == "GuildMember":
                person1 = message.author.mention
            if person2 == "GuildMember":
                person2 = message.author.mention
            final1 = random.choice(cfinal)
            if person1 == "le Roi des burgondes":
                final1 = "Interprètre! Cuillère!"
            if person2 == "le Roi des burgondes":
                final1 = "Salsifi!"
            if person1 == "Provençal le Gaulois":
                final1 = "C'est pas faux!"
            if person2 == "Provençal le Gaulois":
                final1 = "Il en a gros!"
            if person1 == "Merlin" or person2 == "Merlin":
                final1 = "Il manque pas de toupet!"
            if person1 == "Leodagan" or person2 == "Leodagan":
                final1 = "Il lui dit merde!"
            reply = ">>> " + person1 + " rencontre " + person2 + "! " + final1
        else:
            # Template 2
            action1 = random.choice(caction)
            object1 = random.choice(cobject)
            final1 = random.choice(cfinal)
            reply = ">>> Je " + action1 + " " + object1 + "! " + final1
        return reply


    def word_game(self, message):
        msg = message.content.split()
        with open('resources/wordlist_fr.txt', 'r') as dictword:
            wordlist = dictword.readlines()
            wordlist = [x.strip() for x in wordlist]

        if len(msg) > 1 and msg[1].lower() == '!start':
            print("IN START")
            alphabet = ['a', 'e', 'i', 'o', 'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
            voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
            check = False
            while(check == False):

                check_letters = False
                while(check_letters == False):
                    count_voyelles = 0
                    self.wordtrial = []

                    for i in range(0, 9):
                        self.wordtrial.append(random.choice(alphabet))
                        if self.wordtrial[-1] in voyelles:
                            count_voyelles += 1
                    if count_voyelles >= 2:
                        check_letters = True

                # Check if words exist
                letters = Counter(self.wordtrial)
                self.wordsolutions = []
                solutions = [word for word in wordlist if not Counter(word) - letters]
                if len(solutions) > 0:
                    for i in range(len(solutions)):
                        if(len(solutions[i]) > 2 and len(solutions[i]) < 9):
                            self.wordsolutions.append(solutions[i])

                if len(self.wordsolutions) > 2:
                    check = True

                print(self.wordsolutions)

            # Create the return letters
            reply = ''
            for i in range(9):
                reply += ':regional_indicator_'+self.wordtrial[i]+': '

            return reply

        elif len(msg) > 1 and  msg[1].lower() == '!stop':
            print("IN STOP")
            if self.wordsolutions:
                # Create the return letters
                reply = 'Les solutions pour:\n'
                for i in range(9):
                    reply += ':regional_indicator_' + self.wordtrial[i] + ': '
                reply += '\n'
                for i in range(len(self.wordsolutions)):
                    reply += self.wordsolutions[i]+', '
                reply += '\n'
                self.wordtrial = []
                self.wordsolutions = []
                return reply
            else:
                self.wordtrial = []
                self.wordsolutions = []
            return "Aucun jeu en cours! Lancez `!teddymots !start` pour commencer!"

        elif len(msg) > 1:
            print("IN ELIF 1")
            if(self.wordsolutions):
                if(msg[1] in self.wordsolutions):
                    return message.author.mention+" Oui :)"
                else:
                    return message.author.mention+"Non :("
            else:
                return "Aucun jeu en cours! Lancez `!teddymots !start` pour commencer!"

        elif len(msg) == 1:
            print("IN ELIF 2")
            if (self.wordsolutions):
                # Create the return letters
                reply = ''
                for i in range(9):
                    reply += ':regional_indicator_' + self.wordtrial[i] + ': '

                return reply
            else:
                return "Aucun jeu en cours! Lancez `!teddymots !start` pour commencer!"