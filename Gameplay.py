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

	# if infront is true that means it takes into account direction. if false then character loots space on top.
	def interactObj(self, character, mapCord, inFront):
		inp = ""
		if inFront:
			x1, y1 = character.charDirection(character.getDirection())
		else:
			x1, y1 = 0, 0
		if 0 <= character.getX() + x1 < len(mapCord[0]) and 0 <= character.getY() + y1 < len(mapCord):
			print(mapCord[character.getY() + y1][character.getX() + x1].showDescription())
			print(mapCord[character.getY() + y1][character.getX() + x1].showOptions())
			inp = input(": ")
			self.result = mapCord[character.getY() + y1][character.getX() + x1].interact(inp, character)
		else:
			self.result = "You can't interact with this object."

	# def serachArray(self, inventory):
	# 	selection = ""
	# 	while selection != "e":
	# 		try:
	# 			inventory.showInventory()
	# 			print("e: exit inventory")
	# 			selection = input("Choose your option: ")
	# 			selection = int(selection)
	# 			print(inventory.getInventory()[selection].getName())
	# 			print(inventory.getInventory()[selection].getDescription())
	# 			print("")
	# 		except (ValueError, IndexError):
	# 			print("This option is not valid.")

	def inventoryMenu(self, player):
		selection = ""
		while selection != "e":
			try:
				player.showInventory()
				print("e: exit inventory")
				selection = input("Choose your option: ")
				selection = int(selection)
				print(player.getInventory()[selection].getName())
				print(player.getInventory()[selection].getDescription())
				print("POSSIBLE ACTIONS:")
				print("1. Drop Item\n"
					  "e. exit possible actions")
			except (ValueError, IndexError):
				print("This option is not valid.")


	# for the player character actions only
	def characterActions(self, act, mapCord, playerCharacter, isSingleCommand):
		commandHandlers = {
			"e": lambda: playerCharacter.moveCharacter(mapCord, "right"),
			"q": lambda: playerCharacter.moveCharacter(mapCord, "left"),
			"w": lambda: playerCharacter.moveCharacter(mapCord, "forward"),
			"a": lambda: playerCharacter.moveCharacter(mapCord, "sideleft"),
			"s": lambda: playerCharacter.moveCharacter(mapCord, "backward"),
			"d": lambda: playerCharacter.moveCharacter(mapCord, "sideright"),
			"f": lambda: self.interactObj(playerCharacter, mapCord, True),
			"F": lambda: self.interactObj(playerCharacter, mapCord, False),
			"i": lambda: self.inventoryMenu(playerCharacter)
		}

		# to make it single command, remove for loop and change a to act.

		if not isSingleCommand:
			for a in act:
				handler = commandHandlers.get(a)
				if handler:
					handler()
					# due to the way commands are handled if someone interacts with an object - if the user has keys after the interact key then the interactions are overwritten by the not a valid command message
					# this prevents the interaction response from being overwritten.
					if a=="f" or a=="F":
						break
				else:
					self.result = "ERROR: Not a valid command"
		else:
			handler = commandHandlers.get(act)
			if handler:
				handler()
			else:
				self.result = "ERROR: Not a valid command"

