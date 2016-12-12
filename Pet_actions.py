import Pets


x = 2
available_actions = []

class Action():
    def __init__(self, method, name, keyword):
        self.method = method
        self.keyword = keyword
        self.name = name
        available_actions.append(self)

    def __str__(self):
        return "{}: {}".format(self.keyword, self.name)

class Interact(Action):
	def __init__(self, pet, what_to_do):
		self.pet = pet
		self.what_to_do = what_to_do
		self.pet = pet
		available_actions = {}
	

def help_me():
    for action in available_actions:
        print("{}: type {}".format(action.name, action.keyword))

def buy():
    print("here's where you buy stuff")

def quit_game():
    really_quit = input("Would you really like to quit the game? ")
    want_to_save = input("Would you like to save your game? ")


Quit = Action(quit_game, "Quit the game", "quit")
End_turn = Action(print("Next turn"), "End the current turn", "end")
Buy_stuff = Action(buy, "Buy something from the pet store", "buy")
#Interact = Action(interact, "Interact with one of your pets", "interact")
Help_me = Action(help_me, "Get a list of available actions and how to do them", "help")
