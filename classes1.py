class Fruit:
    def __init__(self, name, colour, flavour, poisonous):
        self.name = name
        self.colour = colour
        self.flavour = flavour
        self.poisonous = poisonous

    def description(self):
        print("I am a {} {} and I taste {}.".format(self.colour, self.name, self.flavour))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
