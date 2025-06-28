# MADE BY DAVID TRAN

# must import all of these in order for the text game to work properly
from Character import Character
from Display import Display
from Gameplay import Gameplay
from WorldObject import WorldObject
from Doors import Door, LockedDoor, CodeLockedDoor, KeyedLockedDoor
from Toilet import Toilet
from Map import Map
from Item import Item, Key

playerCharacter = Character(0, 2, 2, 1, 1, [])
display = Display()
gamePlay = Gameplay()

# each dictionary corresponds to a room
# left is space player must reach in room : right is (new mapID : position player will be teleported to in next)
mapTransition1 = {(4, 1) : {2 : (1, 1)}}
mapTransition2 = {(0, 1) : {1 : (3, 1)},
				  (2, 9) : {3 : (0, 0)}}

# items in the game
key1 = Key("key", "Worn Door Key", "A key for a hotel room. It is very worn.", False, 12345)

#playerCharacter.addItem(key1)

# objects for the map
space = WorldObject([], 0, "", "", "")
wall = WorldObject([], 1, "", "", "")
sink = WorldObject([], 7, "", "", "")
mirror = WorldObject([], 6, "", "", "")
vdoor = Door([], 2)
vdoor2 = KeyedLockedDoor([], True, 12345, 2)
hdoor = CodeLockedDoor([], True, "1492", 4)
toilet = Toilet([], 3)

cord = [[wall.createUnique([]), wall.createUnique([]), wall.createUnique([]), wall.createUnique([]), wall.createUnique([])],  # List of coordinates for the map
		[wall.createUnique([]), space.createUnique([]), toilet, space.createUnique([]), vdoor],
		[wall.createUnique([]), space.createUnique([]), space.createUnique([]), space.createUnique([key1]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), space.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), space.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), wall.createUnique([]), wall.createUnique([]), wall.createUnique([]), wall.createUnique([])]]

cord1 = [[wall.createUnique([]), hdoor, wall.createUnique([])],  # List of coordinates for the map
		[vdoor, space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), wall.createUnique([])],
		[wall.createUnique([]), space.createUnique([]), vdoor2],
		[wall.createUnique([]), wall.createUnique([]), wall.createUnique([])]]

map1Desc = ("-----\n"
				  "You are in a bathroom.\n"
				  "It is brightly lit and smells like lavender.")
map2Desc = ("-----\n"
				  "You are in a hallway.\n"
				  "It is dull yellow and white and its odor is reminsicent of bleach.")

Map1 = Map(1, cord, mapTransition1, map1Desc)
Map2 = Map(2, cord1, mapTransition2, map2Desc)

characterList = [playerCharacter]

maps = [cord, cord1]
mapObjects = {
	1 : Map1,
	2 : Map2
}

act = ""

res = ""

def main():
	display.clearScreen()

	print("You wake up, and find yourself on the floor, laying on your back.\n"
		  "You blink rapidly, and soon push yourself off the ground, and stand upright, your drowsiness fading as quickly as you woke up.\n")

	pauser = input()

	while playerCharacter.getRoom() != 3:
		# actual block for handling gameplay and display
		display.clearScreen()
		display.printDisplay(characterList, mapObjects.get(playerCharacter.getRoom()).getMap())
		print(gamePlay.showResult())
		gamePlay.clearResult()
		print(mapObjects.get(playerCharacter.getRoom()).getMapSummary())
		act = input("COMMAND: ")
		gamePlay.characterActions(act, mapObjects.get(playerCharacter.getRoom()).getMap(), playerCharacter, False)

		# when moving from room to room - turns are registered - not extra moves.
		# fix this somehow
		transitions = mapObjects.get(playerCharacter.getRoom()).getConnections()
		dictValue = transitions.get((playerCharacter.getX(), playerCharacter.getY()))
		if dictValue != None:
			newRoomID = list(dictValue.keys())
			playerCharacter.setX(dictValue.get(newRoomID[0])[0])
			playerCharacter.setY(dictValue.get(newRoomID[0])[1])
			playerCharacter.changeRoom(newRoomID[0])
			gamePlay.setResult("You enter another room.")

	print("You leave the building.\n"
		  "CONGRATULATIONS. YOU HAVE BEATEN THE GAME")
	act = input("Press ENTER to exit.")

main()
