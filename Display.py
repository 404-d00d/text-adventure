import os
import platform
import math


# governs how the display for the map and character should show up
class Display:
	# Clears terminal window so interface looks clean.
	def clearScreen(self):
		if platform.system() == "Windows":
			os.system('cls')
		else:
			os.system('clear')

	# dictionary for how map is represented - values and symbols can be swapped depending on user preferences
	def representOb(self, mapObject):
		if mapObject.getID() > 0:
			tile = math.floor(mapObject.getID())
		else:
			tile = math.ceil(mapObject.getID())
		symbolMap = {
			1: "N",   			# wall
			3: "A",   			# toilet
			6: "0",   			# mirror
			2: "|",   			# closed door - vertical wall
			7: "Q",   			# sink
			-2: "_",  			# open door - vertical wall
			0: ".",   			# empty space
			4: "_",	  			# closed door - horizontal wall
			-4: "|"	  	# open door - horizontal wall
		}
		return symbolMap.get(tile, " ") # if no number matches the dictionary return a blank space.

	def printChar(self, characters): # governs player character/direction they face
		if characters.getID() == 0:
			playerChar = {
				1: "^",
				2: ">",
				3: "v",
				4: "<"
			}[characters.getDirection()]
			return playerChar
		elif characters.getID() == 1:
			otherChar = {
				1: "M",
				2: "3",
				3: "W",
				4: "E"
			}[characters.getDirection()]
			return otherChar
		elif characters.getID() == 2:
			otherChar2 = {
				1: "n",
				2: "ↄ",
				3: "u",
				4: "c"
			}[characters.getDirection()]
			return otherChar2

	def printDisplay(self, characters, mapCord): # prints out objects and characters in map
		for y in range(len(mapCord)):
			for x in range(len(mapCord[0])):
				charac = False
				if x == len(mapCord[0]) - 1: # checks if print reaches end of line, switches to new line/properly prints out spaces
					for z in range(len(characters)): # checks if current block is a player character
						if characters[z].getX() == x and characters[z].getY() == y:
							print(self.printChar(characters[z]))
							charac = True
					if not charac:
						print(self.representOb(mapCord[y][x]))
				else:
					for z in range(len(characters)): # checks if current block is a player character
						if characters[z].getX() == x and characters[z].getY() == y:
							print(self.printChar(characters[z]), end=" ")
							charac = True
					if not charac:
						print(self.representOb(mapCord[y][x]), end=" ")
		print("-----")
