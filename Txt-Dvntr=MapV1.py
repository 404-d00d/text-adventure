# MADE BY DAVID TRAN
from Character import Character
from Display import Display
from Gameplay import Gameplay

playerCharacter = Character(0, 2, 2, 1, 1)
display = Display()
gamePlay = Gameplay()

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]],  # List of coordinates for the map
		[[1.0, ""], [7.0, ""], [3.1, ""], [0.0, ""], [2.0, ""]],
		[[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""], [1.0, ""]]]

cord1 = [[[1.0, ""], [1.0, ""], [1.0, ""]],  # List of coordinates for the map
		[[2.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [1.0, ""]],
		[[1.0, ""], [0.0, ""], [2.0, ""]],
		[[1.0, ""], [1.0, ""], [1.0, ""]]]

characterList = [playerCharacter]

maps = [cord, cord1]

act = ""

res = ""

def main():
	display.clearScreen()

	print("You wake up, and find yourself on the floor, laying on your back.\n"
		  "You blink rapidly, and soon push yourself off the ground, and stand upright, your drowsiness fading as quickly as you woke up.\n")

	pauser = input()

	while playerCharacter.getRoom() != 3:
		# governs room switching
		if playerCharacter.getX() == 4 and playerCharacter.getY() == 1 and playerCharacter.getRoom() == 1:
			gamePlay.setResult("You enter another room.")
			playerCharacter.setX(1)            
			playerCharacter.setY(1)            
			playerCharacter.changeRoom(2)
		elif playerCharacter.getX() == 0 and playerCharacter.getY() == 1 and playerCharacter.getRoom() == 2:
			gamePlay.setResult("You enter another room.")
			playerCharacter.setX(3) 
			playerCharacter.setY(1)
			playerCharacter.changeRoom(1)
		elif playerCharacter.getX() == 2 and playerCharacter.getY() == 9 and playerCharacter.getRoom() == 2:
			gamePlay.setResult("You enter another room.")
			#playerCharacter.setX(2)
			#playerCharacter.setY(9)
			playerCharacter.changeRoom(3)
		# governs character interaction
		elif playerCharacter.getRoom() == 1:
			display.clearScreen()
			display.printDisplay(characterList, maps[0])
			print(gamePlay.showResult())
			gamePlay.clearResult()
			print("-----")
			print("You are in a bathroom.\n"
				  "It is brightly lit by flourescent light tubes placed up on the tan ceiling, emmiting harsh light.\n"
				  "The smell of lavender and soap permeates the room.\n"
				  "A toilet, sink and mirror, shower-stall, and bathtub are inside the room.\n"
				  "The wall is pure white, with no blemishes and marks on it.\n"
				  "The floor is tiled tan and white, alternating between each color every row.\n"
				  "Much like the walls, there are no blemishes or marks on the floor.")
			act = input("COMMAND: ")
			gamePlay.characterActions(act, maps[0], playerCharacter)
		elif playerCharacter.getRoom() == 2:
			display.clearScreen()
			display.printDisplay(characterList, maps[1])
			print(gamePlay.showResult())
			gamePlay.clearResult()
			print("-----")
			print("You are in a hallway.\n"
				  "It is dull yellow and white and its odor is reminsicent of bleach.")
			act = input("COMMAND: ")
			gamePlay.characterActions(act, maps[1], playerCharacter)

	print("You leave the building.\n"
		  "CONGRATULATIONS. YOU HAVE BEATEN THE GAME")
	act = input("Press ENTER to exit.")

main()
