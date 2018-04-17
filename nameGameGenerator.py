import random

names = []
adjectives = ["Cool", "Crazy", "Epic", "Fantastic", "Godlike", "Awesome", "Unprofen", "Legendary", "Heroic", "Rare"]
word_2 = ["Game", "Program", "Battle", "Python Game", "Battle Simulator", "Tournament"]
word_3 = ["for", "without", "of"]
word_4 = ["drunken dwarfs", "drunken trolls", "humans", "artifficial intelligences", "gamers", "programmers", "nerds", "drunken elfs", "drunken lizards", "Dumb Lizards", "dumb and drunken trolls", "dumb and drunken elfs", "soup-sucking, dumb and drunken elfs", "soup-sucking robots with creepy red eyes", "maniacly laughing robots with laser-shooting eyes", "maniacly laughing elfs with red eyes, pistols and pink unicorn armor"]

for x in range(5):
	name = random.choice(adjectives) + " " + random.choice(word_2) + " " + random.choice(word_3) + " " + random.choice(word_4)
	print(name)
