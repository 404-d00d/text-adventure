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
		if 0 <= character.getX() + x1 < len(mapCord[0]) and 0 <= character.getY() + y1 < len(mapCord):
			print(mapCord[character.getY() + y1][character.getX() + x1].showDescription())
			print(mapCord[character.getY() + y1][character.getX() + x1].showOptions())
			inp = input(": ")
			self.result = mapCord[character.getY() + y1][character.getX() + x1].interact(inp, character)
		else:
			self.result = "You can't interact with this object."

	def inventoryMenu(self, player):
		selection = ""
		while selection != "e":
			try:
				player.showInventory()
				print("e: exit inventory")
				selection = input("Choose your option: ")
				selection = int(selection)
				print(player.inventory[selection].getName())
				print(player.inventory[selection].getDescription())
			except (ValueError, IndexError):
				print("This option is not valid.")


	# for the player character actions only
	def characterActions(self, act, mapCord, playerCharacter):
		commandHandlers = {
			"e": lambda: playerCharacter.moveCharacter(mapCord, "right"),
			"q": lambda: playerCharacter.moveCharacter(mapCord, "left"),
			"w": lambda: playerCharacter.moveCharacter(mapCord, "forward"),
			"a": lambda: playerCharacter.moveCharacter(mapCord, "sideleft"),
			"s": lambda: playerCharacter.moveCharacter(mapCord, "backward"),
			"d": lambda: playerCharacter.moveCharacter(mapCord, "sideright"),
			"f": lambda: self.interactObj(playerCharacter, mapCord),
			"i": lambda: self.inventoryMenu(playerCharacter)
		}

		for a in act:
			handler = commandHandlers.get(a)
			if handler:
				handler()
				# due to the way commands are handled if someone interacts with an object - if the user has keys after the interact key then the interactions are overwritten by the not a valid command message
				# this prevents the interaction response from being overwritten.
				if a=="f":
					break
			else:
				self.result = "ERROR: Not a valid command"
