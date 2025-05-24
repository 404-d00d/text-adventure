# MADE BY DAVID TRAN
import math
import os
import platform

char0 = [4, 2, 2, 1, 1]  # [character determiner, x, y, direction(1=N,2=E,3=S,4=W), room]

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]],  # List of coordinates for the map
        [[1.0, ""], [7.0, ""], [3.1, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""], [1.0, ""]]]

cord1 = [[[1.0, ""], [1.0, ""], [1.0, ""]],  # List of coordinates for the map
        [[2.0, ""], [0.0, ""], [3.1, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [1.0, ""], [1.0, ""]]]

chars = [char0]

maps = [cord, cord1]

act = ""

res = ""

# handles direction regarding character movement
def charDirection(direction):
    x1, y1 = {
        1: (0, -1),  # N
        2: (1, 0),   # E
        3: (0, 1),   # S
        4: (-1, 0),  # W
    }[direction]
    return x1, y1

# Clears terminal window so interface looks clean.
def clearScreen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# dictionary for how map is represented
def representOb(mapCord, x, y):
    tile = math.floor(mapCord[y][x][0])
    symbolMap = {
        1: "N",   # wall
        3: "A",   # toilet
        6: "0",   # mirror
        2: "|",   # closed door
        7: "Q",   # sink
        -2: "_",  # open door
        0: "."    # empty space
    }
    return symbolMap.get(tile, " ") # if no number matches the dictionary return a blank space.


def printChar(characters): # governs player character/direction they face
    if characters[0] == 4:
        playerChar = {
            1: "^",
            2: ">",
            3: "v",
            4: "<"
        }[characters[3]]
        return playerChar
    elif characters[0] == 3:
        otherChar = {
            1: "M",
            2: "3",
            3: "W",
            4: "E"
        }[characters[3]]
        return otherChar
    elif characters[0] == 2:
        otherChar2 = {
            1: "n",
            2: "ↄ",
            3: "u",
            4: "c"
        }[characters[3]]
        return otherChar2

def printDisplay(characters, mapCord): # prints out objects and characters in map
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            charac = False
            if x == len(mapCord[0]) - 1: # checks if print reaches end of line, switches to new line/properly prints out spaces
                for z in range(len(characters)): # checks if current block is a player character
                    if characters[z][1] == x and characters[z][2] == y:
                        print(printChar(characters[z]))
                        charac = True
                if not charac:
                    print(representOb(mapCord, x, y))
            else:
                for z in range(len(characters)): # checks if current block is a player character
                    if characters[z][1] == x and characters[z][2] == y:
                        print(printChar(characters[z]), end=" ")
                        charac = True
                if not charac:
                    print(representOb(mapCord, x, y), end=" ")
    print("-----")

# moves character
def moveCharacter(character, mapCord, command):
    # Step 1: Rotate character
    if command == "e":  # turn right
        character[3] = (character[3] % 4) + 1
        return
    elif command == "q":  # turn left
        character[3] = 4 if character[3] == 1 else character[3] - 1
        return

    # Step 2: Determine movement vector based on command and direction
    forwardMap = {
        'w': 0,
        'a': 3,
        's': 2,
        'd': 1
    }
    if command not in forwardMap:
        return  # invalid movement key

    # Rotate direction to get movement vector
    direction = character[3]
    offset = (forwardMap[command] + direction - 1) % 4 + 1

    dx, dy = charDirection(offset)

    # Step 3: Calculate new position
    newX = character[1] + dx
    newY = character[2] + dy

    # Step 4: Check boundaries
    if 0 <= newY < len(mapCord) and 0 <= newX < len(mapCord[0]):
        # Step 5: Check for passable tile
        if mapCord[newY][newX][0] <= 0:
            character[1] = newX
            character[2] = newY

# governs character interactions with objects and how objects are modified
def interactObj(character, mapCord):
    global res
    inp = ""
    x1, y1 = charDirection(character[3])
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            if character[1] + x1 == x and character[2] + y1 == y:
                if math.floor(mapCord[y][x][0]) == 3:
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
                        if mapCord[y][x][0] == 3:
                            res = ("You lift up the toilet lid.\n"
                                  "The bowl is clear and clean.\n"
                                  "The water in the bowl is transparent, letting you see the inside of the toilet bowl.\n"
                                  "Much like the outside of the toilet, the inside of the basin is white.")
                        elif mapCord[y][x][0] == 3.1:
                            res = ("You lift up the toilet lid.\n"
                                  "The bowl is filled with water, chunks of food, and bile.\n"
                                  "The bile and food chunks float on the water's surface, and are mixed together cleanly.\n"
                                  "It's hard to tell what is bile and what are the food chunks.\n"
                                  "You immediately close the toilet lid, just to avoid adding more to that accursed pile.")
                    elif inp == "2":
                        res = ("You push down on the toilet handle on the tank.\n"
                              "You hear the sound of water flowing into the toilet bowl, followed by the sound of water rushing down the pipes.\n"
                              "It's eventually followed by the rush of water back into the toilet basin.")
                        mapCord[y][x][0] = 3
                    else:
                        res = ("You do nothing.")
                elif abs(mapCord[y][x][0]) == 2:
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
                        res = ("The paint on the door appears to be a recent coat.\n"
                               "There is some noticable grain on the door, along with tiny bumps on the door.\n"
                               "The doorknob has fingerprint marks on it, from constant usage of staff and guests in the room.")
                    elif inp == "2":
                        if mapCord[y][x][0] == -2:
                            res = ("You grab the doorknob, and push the door away from you.\n"
                                   "It locks into the door frame with a thud.\n"
                                   "As you let go of the doorknob, it springs back into the locked position with a click.\n"
                                   "It is now closed.")
                            mapCord[y][x][0] *= -1
                        elif mapCord[y][x][0] == 2:
                            res = ("You grab the doorknob, and twist it to the right.\n"
                                   "The door unlocks as you pull it towards your body.\n"
                                   "It is now open.")
                            mapCord[y][x][0] *= -1
                    else:
                        res = ("You do nothing.")


def gamePlay(act):
    global res
    commandHandlers = {
        "e": lambda: moveCharacter(char0, cord, "e"),
        "q": lambda: moveCharacter(char0, cord, "q"),
        "w": lambda: moveCharacter(char0, cord, "w"),
        "a": lambda: moveCharacter(char0, cord, "a"),
        "s": lambda: moveCharacter(char0, cord, "s"),
        "d": lambda: moveCharacter(char0, cord, "d"),
        "f": lambda: interactObj(char0, cord),
    }

    for a in act:
        handler = commandHandlers.get(a)
        if handler:
            handler()
        else:
            res = "ERROR: Not a valid command"

def main():
    clearScreen()
    global res

    print("You wake up, and find yourself on the floor, laying on your back.\n"
          "You blink rapidly, and soon push yourself off the ground, and stand upright, your drowsiness fading as quickly as you woke up.\n")

    pauser = input()


    while char0[4] != 3:
        if char0[1] == 4 and char0[2] == 1:
            char0[4] = 3
        #elif char0[1] == 0 and char0[2] == 1:
        else:
            clearScreen()
            printDisplay(chars, maps[0])
            print(res)
            res = ""
            print("-----")
            print("You are in a bathroom.\n"
                  "It is brightly lit by flourescent light tubes placed up on the tan ceiling, emmiting harsh light.\n"
                  "The smell of lavender and soap permeates the room.\n"
                  "A toilet, sink and mirror, shower-stall, and bathtub are inside the room.\n"
                  "The wall is pure white, with no blemishes and marks on it.\n"
                  "The floor is tiled tan and white, alternating between each color every row.\n"
                  "Much like the walls, there are no blemishes or marks on the floor.")
            act = input("COMMAND: ")
            gamePlay(act)


    print("You leave the bathroom.\n"
          "CONGRATULATIONS. YOU HAVE BEATEN THE GAME")
    act = input("Press ENTER to exit.")

main()
