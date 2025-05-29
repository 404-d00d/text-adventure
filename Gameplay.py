from Character import Character
import math

class Gameplay:
	# governs character interactions with objects and how objects are modified
	def __init__(self):
		self.result = ""

	def showResult(self):
		return self.result

	def setResult(self, message):
		self.result = message

	def clearResult(self):
		self.result = ""

	def interactObj(self, character, mapCord):
		inp = ""
		x1, y1 = character.charDirection(character.getDirection())
		if 0 <= character.getX() + x1 <= len(mapCord[0]) and 0 <= character.getY() + y1 <= len(mapCord):
			if math.floor(mapCord[character.getY() + y1][character.getX() + x1][0]) == 3:
				print("You see a toilet.\n"
					  "It is porcelain white, with no blemishes or marks on the body.\n"
					  "The tank lid and tank of the toilet appear to be bolted to the toilet basin and the wall itself.\n"
					  "The toilet lid and toilet basin are white and clean as the rest of the toilet.\n"
					  "The toilet is shiny, reflecting the light from the celing light tubes.\n"
					  "The toilet lid is closed.")
				print("-----")
				print("1. Look Closer\n"
					  "2. Interact\n"
					  "Any Other Option. Do Nothing")
				inp = input(": ")
				if inp == "1":
					if mapCord[character.getY() + y1][character.getX() + x1][0] == 3:
						self.result = ("You lift up the toilet lid.\n"
							  "The bowl is clear and clean.\n"
							  "The water in the bowl is transparent, letting you see the inside of the toilet bowl.\n"
							  "Much like the outside of the toilet, the inside of the basin is white.")
					elif mapCord[character.getY() + y1][character.getX() + x1][0] == 3.1:
						self.result = ("You lift up the toilet lid.\n"
							  "The bowl is filled with water, chunks of food, and bile.\n"
							  "The bile and food chunks float on the water's surface, and are mixed together cleanly.\n"
							  "It's hard to tell what is bile and what are the food chunks.\n"
							  "You immediately close the toilet lid, just to avoid adding more to that accursed pile.")
				elif inp == "2":
					self.result = ("You push down on the toilet handle on the tank.\n"
						  "You hear the sound of water flowing into the toilet bowl, followed by the sound of water rushing down the pipes.\n"
						  "It's eventually followed by the rush of water back into the toilet basin.")
					mapCord[character.getY() + y1][character.getX() + x1][0] = 3
				else:
					self.result = ("You do nothing.")
			elif abs(mapCord[character.getY() + y1][character.getX() + x1][0]) == 2:
				print("You see a door.\n"
					  "It is chalk-white, with a grayish trim around the edges of the door.\n"
					  "The doorknob is to the center-right of the door itself, and is brass colored.\n"
					  "It is clean and has no dust or dirt on it.")
				print("-----")
				print("1. Look Closer\n"
					  "2. Interact\n"
					  "Any Other Option. Do Nothing")
				inp = input(": ")
				if inp == "1":
					self.result = ("The paint on the door appears to be a recent coat.\n"
						   "There is some noticable grain on the door, along with tiny bumps on the door.\n"
						   "The doorknob has fingerprint marks on it, from constant usage of staff and guests in the room.")
				elif inp == "2":
					if mapCord[character.getY() + y1][character.getX() + x1][0] == -2:
						self.result = ("You grab the doorknob, and push the door away from you.\n"
							   "It locks into the door frame with a thud.\n"
							   "As you let go of the doorknob, it springs back into the locked position with a click.\n"
							   "It is now closed.")
						mapCord[character.getY() + y1][character.getX() + x1][0] *= -1
					elif mapCord[character.getY() + y1][character.getX() + x1][0] == 2:
						self.result = ("You grab the doorknob, and twist it to the right.\n"
							   "The door unlocks as you pull it towards your body.\n"
							   "It is now open.")
						mapCord[character.getY() + y1][character.getX() + x1][0] *= -1
				else:
					self.result = "You do nothing."
			else:
				self.result = "You can't interact with this object."
		else:
			self.result = "You can't interact with this object."

	# for the player character actions only
	def characterActions(self, act, mapCord, playerCharacter):
		commandHandlers = {
			"e": lambda: playerCharacter.moveCharacter(mapCord, "e"),
			"q": lambda: playerCharacter.moveCharacter(mapCord, "q"),
			"w": lambda: playerCharacter.moveCharacter(mapCord, "w"),
			"a": lambda: playerCharacter.moveCharacter(mapCord, "a"),
			"s": lambda: playerCharacter.moveCharacter(mapCord, "s"),
			"d": lambda: playerCharacter.moveCharacter(mapCord, "d"),
			"f": lambda: self.interactObj(playerCharacter, mapCord),
		}

		for a in act:
			handler = commandHandlers.get(a)
			if handler:
				handler()
			else:
				self.result = "ERROR: Not a valid command"
