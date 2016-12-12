import time

class Pet:
    def __init__(self, species, max_health, adjective, tired_rate, boredom_rate):
        self.species = species
        self.max_health = max_health
        self.health = max_health
        self.energy = 100
        self.fun = 100
        self.adjective = adjective
        self.hunger_rate = 5
        self.tired_rate = tired_rate
        self.boredom_rate = boredom_rate
        self.stats = {"Health": [self.health, self.max_health, "hungry", self.hunger_rate], "Energy": [self.energy, 100, "tired", self.tired_rate], "Fun": [self.fun, 100, "bored", self.boredom_rate]}

    def __str__(self):
        return "\nYour pet is {} the {} {}.\n".format(self.name, self.adjective, self.species)

    def alert(self):
        for stat, details in self.stats.items():
            if details[0] <= 0.25 * details[1]:
                print("{} is feeling very {}! Please do something soon!".format(self.name, details[2]))

    def print_stats(self):
        print("{}'s current stats are:\n----------------".format(self.name))
        for stat, details in self.stats.items():
            print("{}     {}".format(stat, details[0]))
        self.alert()
        print("")

    def time_passes(self):
        time.sleep(5)
        for stat, details in self.stats.items():
            details[0] -= details[3]





class Cat(Pet):
    def __init__(self, name):
        self.name = name
        super().__init__(species = "cat", max_health = 100, adjective = "furry", tired_rate = 10, boredom_rate = 2)

class Dog(Pet):
    def __init__(self, name):
        self.name = name
        super().__init__(species = "dog", max_health = 200, adjective = "playful", tired_rate = 2, boredom_rate = 10)

class Bird(Pet):
    def __init__(self, name):
        self.name = name
        super().__init__(species = "bird", max_health = 75, adjective = "beautiful", tired_rate = 2, boredom_rate = 5)

class Fish(Pet):
    def __init__(self, name):
        self.name = name
        super().__init__(species = "fish", max_health = 50, adjective = "peaceful", tired_rate = 2, boredom_rate = 2)