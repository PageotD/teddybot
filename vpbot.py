# Import modules
import yaml

class VPBot:
    """
    Virtual Pet Bot Class.
    Designed to control the behavior of the bot
    """
    # Fixed parameters
    # * happiness threshold and drop
    self.hapiness_threshold = 50.
    self.happiness_drop = 20.
    # * fullness threshold and drop
    self.fullness_threshold = 50.
    self.fullness_drop = 25

    def __init__(self, name="Teddy"):
        # Virtual pet name
        self.vpname = name
        # Set happiness and fullness
        self.happiness = 100.
        self.fullness = 100.

    def _mood(self):
        """
        Estimate the mood of the virtual pet given happiness and fullness level
        """
        if(self.fullness >= self.fullness_threshold and self.happiness >= self.happiness_threshold):
            status "Happy!"
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
        pass

    def play(self):
        pass

    def feed(self):
        pass

    # Actions
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