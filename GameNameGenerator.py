import random

names = []

with open("word1.txt","r") as f:
	fr1 = f.read()
	word_1 = fr1.split(",")
	
with open("word2.txt","r") as f:
	fr2 = f.read()
	word_2 = fr2.split(",")

with open("word3.txt","r") as f:
	fr3 = f.read()
	word_3 = fr3.split(",")
	
with open("word4.txt","r") as f:
	fr4 = f.read()
	word_4 = fr4.split(",")
	
with open("word5.txt","r") as f:
	fr5 = f.read()
	word_5 = fr5.split(",")
			
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
	name = random.choice(word_1) + " " + random.choice(word_2) + " " + random.choice(word_3) + " " + random.choice(word_4) + " with " + random.choice(word_5)
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
