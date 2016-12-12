import pickle
import time
import Pets
import Pet_actions 


class World:
    def __init__(self):
        self.money = 500
        self.list_of_pets = {"cat": [Pets.Cat, 100], "dog": [Pets.Dog, 150], "bird": [Pets.Bird, 100], "fish": [Pets.Fish, 50]}
        self.my_pets = {}
        self.playing = True


    def new_game(self):
        chosen_pet = ""
        while chosen_pet not in self.list_of_pets:
            print("Welcome to Stephanie's pet shop. You have {} to spend! Our pet shop currently contains:".format(self.money))
            for pet, pet_object in self.list_of_pets.items():
                print("{}: ${}".format(pet.capitalize(), pet_object[1]))
            chosen_pet = input("Which would you like to purchase? ").lower()
        new_pet_name = input("What would you like to name your pet? ").capitalize()
        new_pet = self.list_of_pets[chosen_pet][0](new_pet_name)
        self.money -= self.list_of_pets[chosen_pet][1]
        print(new_pet)
        new_pet.print_stats()
        self.my_pets[new_pet.name] = new_pet
        print("Congratulations on your new pet! You currently have {} pet(s). As time goes by, your pets will get hungry, bored, and tired. It is your job to keep them healthy and happy.".format(len(self.my_pets)))

    def turn(self):
        time.sleep(5)
        for pet_name, pet in self.my_pets.items():
            print("")
            pet.time_passes()
            pet.print_stats()
        print("What would you like to do next? Your options are:")
        for action in Pet_actions.available_actions:
            print("{}: type '{}'".format(action.name, action.keyword))
        next_action = input(">> ")




def start_game():
    load = False
    global my_world
    while not load:
        want_to_load = input("Would you like to load a saved game? ")
        if want_to_load.lower()[0] == 'y': 
            saved_game = input("What is your saved game called? ") + ".pet" 
            try:
                my_world = pickle.load(open(saved_game, "rb"))
                load = True
            except FileNotFoundError:  
                print("Sorry, no saved game with that name exists.")
        elif want_to_load.lower()[0] == 'n':
            my_world = World()
            my_world.new_game()
            load = True



start_game()
my_world.turn()





