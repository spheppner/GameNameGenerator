import random

names = []
adjectives = ["Cool", "Crazy", "Epic", "Fantastic", "Godlike", "Awesome", "Unprofen", "Legendary", "Heroic", "Rare", "Profen", "Very Rare", "Funny", "Dumb", "Very Cool", "Drunken", "Stinking", "Japanese", "Austrian", "Australian", "American", "European", "Asien", "South America"]

word_2 = ["Game", "Program", "Battle", "Python Game", "Battle Simulator", "Tournament"]
word_3 = ["for", "without", "of"]
word_4 = ["drunken dwarfs", "drunken trolls", "humans", "artifficial intelligences", "gamers", "programmers", "nerds", "drunken elfs", "drunken lizards", "Dumb Lizards", "dumb and drunken trolls", "dumb and drunken elfs", "soup-sucking, dumb and drunken elfs", "soup-sucking robots", "maniacly laughing robots", "maniacly laughing and stinking elfs", "rotten skelettons", "stinking humans", "stinking programmers", "stinking and rotten humans", "stinking and rotten programmers", "rotten gamers", "stinking gamers", "stinking, dumb, and high elfs"]
word_5 = ["creepy red eyes", "laser-shooting eyes", "pink unicorn armor", "golden shining armor", "silver armor", "armor out of pure gold", "armor out of bones", "armor out of stinking socks"]

while True:
	hm = input("[*] How many names do you want to have? > ")
	try:
		test = int(hm)
	except ValueError:
		continue
	if hm == "":
		continue
	elif hm != "":
		break

for x in range(int(hm)):
	name = random.choice(adjectives) + " " + random.choice(word_2) + " " + random.choice(word_3) + " " + random.choice(word_4) + " with " + random.choice(word_5)
	names.append(name)
	print("-----------------------------------------------------------")
	print(str(x) + ": " + name)
	
while True:
	c = input("[*] Do you want to save the words? (Y/N) > ")
	if c == "":
		continue
	elif c.lower() == "y":
		with open("gamenames.txt","w") as f:
			for x in range((len(names))):
				f.write("-----------------------------------------------------------\n")
				f.write(str(x) + ": " + names[x] + "\n")
		print("[+] Successfully saved!")
		break
	elif c.lower() == "n":
		print("Okay, then!")
		break
