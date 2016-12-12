import pickle


saved = input("name your game!: ") + ".pickle"

try:
	test = pickle.load(open(saved, "rb"))
except FileNotFoundError:
	test = 'blank'

print(test)


test = "changed!"

pickle.dump(test, open(saved, "wb"))






